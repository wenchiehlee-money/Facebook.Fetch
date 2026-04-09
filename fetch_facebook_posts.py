#!/usr/bin/env python3
"""Fetch public Facebook page posts and save one Markdown file per post."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib import error, parse, request


DEFAULT_UA = "Mozilla/5.0"
PUBLIC_TIMELINE_DOC_ID = "26358137867213918"
PUBLIC_TIMELINE_QUERY_NAME = "ProfileCometTimelineFeedRefetchQuery"
JSON_SCRIPT_RE = re.compile(
    r'<script\s+type="application/json"[^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
POST_URL_PATTERNS = (
    re.compile(r"https://www\\.facebook\\.com/[^\"' <]+/posts/[^\"' <]+", re.IGNORECASE),
    re.compile(r"https://www\\.facebook\\.com/[^\"' <]+/videos/\\d+", re.IGNORECASE),
    re.compile(r"https://www\\.facebook\\.com/reel/\\d+", re.IGNORECASE),
    re.compile(r"https://www\\.facebook\\.com/story\\.php\\?story_fbid=[^\"' <]+", re.IGNORECASE),
)


@dataclass
class FetchResult:
    final_url: str
    html_text: str
    status_code: int


class MetaTagParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "meta":
            return
        attr_map = dict(attrs)
        key = attr_map.get("property") or attr_map.get("name")
        value = attr_map.get("content")
        if key and value:
            self.meta[key] = value


def build_request(url: str, cookie: str | None) -> request.Request:
    headers = {"User-Agent": DEFAULT_UA}
    if cookie:
        headers["Cookie"] = cookie
    return request.Request(url, headers=headers)


def fetch_html(url: str, cookie: str | None) -> FetchResult:
    req = build_request(url, cookie)
    with request.urlopen(req, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        text = response.read().decode(charset, errors="replace")
        return FetchResult(
            final_url=response.geturl(),
            html_text=text,
            status_code=getattr(response, "status", 200),
        )


def parse_meta_tags(html_text: str) -> dict[str, str]:
    parser = MetaTagParser()
    parser.feed(html_text)
    return parser.meta


def normalize_post_url(url: str) -> str:
    cleaned = html.unescape(url).replace("&amp;", "&")
    parsed = parse.urlsplit(cleaned)
    query = parse.parse_qsl(parsed.query, keep_blank_values=True)
    normalized_query = [
        item for item in query if item[0] not in {"__cft__", "__tn__", "locale"}
    ]
    return parse.urlunsplit(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parse.urlencode(normalized_query),
            "",
        )
    )


def extract_post_urls(html_text: str) -> list[str]:
    found: set[str] = set()
    for pattern in POST_URL_PATTERNS:
        for match in pattern.findall(html_text):
            found.add(normalize_post_url(match))
    return sorted(found)


def extract_json_blobs(html_text: str) -> list[Any]:
    blobs: list[Any] = []
    for raw_blob in JSON_SCRIPT_RE.findall(html_text):
        try:
            blobs.append(json.loads(html.unescape(raw_blob)))
        except json.JSONDecodeError:
            continue
    return blobs


def is_post_like_dict(node: dict[str, Any]) -> bool:
    keys = set(node.keys())
    signal_keys = {
        "post_id",
        "post_url",
        "creation_time",
        "feedback",
        "message",
        "wwwURL",
        "url",
    }
    if not keys.intersection(signal_keys):
        return False
    url_value = node.get("post_url") or node.get("wwwURL") or node.get("url")
    if isinstance(url_value, str) and "facebook.com" in url_value:
        return True
    if "creation_time" in node and (
        "message" in node or "feedback" in node or "post_id" in node
    ):
        return True
    return False


def compact_post_record(node: dict[str, Any]) -> dict[str, Any]:
    record: dict[str, Any] = {}
    for key in ("post_id", "creation_time", "post_url", "wwwURL", "url"):
        value = node.get(key)
        if value is not None:
            record[key] = value

    message = node.get("message")
    if isinstance(message, dict):
        text_value = message.get("text")
        if isinstance(text_value, str):
            record["message"] = text_value
    elif isinstance(message, str):
        record["message"] = message

    story = node.get("story")
    if isinstance(story, dict):
        text_value = story.get("message") or story.get("text")
        if isinstance(text_value, str):
            record["story_text"] = text_value

    feedback = node.get("feedback")
    if isinstance(feedback, dict):
        if feedback.get("id"):
            record.setdefault("feedback", {})["id"] = feedback.get("id")
        if feedback.get("url"):
            record.setdefault("feedback", {})["url"] = feedback.get("url")

    return record


def deduplicate_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for record in records:
        key = record.get("post_id") or json.dumps(record, ensure_ascii=False, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(record)
    return deduped


def walk_json(node: Any, found: list[dict[str, Any]]) -> None:
    if isinstance(node, dict):
        if is_post_like_dict(node):
            compacted = compact_post_record(node)
            if compacted:
                found.append(compacted)
        for value in node.values():
            walk_json(value, found)
        return
    if isinstance(node, list):
        for item in node:
            walk_json(item, found)


def extract_post_records_from_html(html_text: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for blob in extract_json_blobs(html_text):
        walk_json(blob, records)
    return deduplicate_records(records)


def extract_public_graphql_context(html_text: str) -> dict[str, str] | None:
    lsd_match = re.search(r'\["LSD",\s*\[\],\s*\{"token":\s*"([^"]+)"\}', html_text)
    jazoest_match = re.search(r"jazoest[^0-9]{0,20}(\d{4,})", html_text)
    user_id_match = re.search(r'"userID":"(\d+)"', html_text)
    vanity_match = re.search(r'"userVanity":"([^"]+)"', html_text)
    if not (lsd_match and jazoest_match and user_id_match):
        return None
    return {
        "lsd": lsd_match.group(1),
        "jazoest": jazoest_match.group(1),
        "user_id": user_id_match.group(1),
        "user_vanity": vanity_match.group(1) if vanity_match else "",
    }


def fetch_public_timeline_parts(html_text: str, count: int) -> list[dict[str, Any]]:
    context = extract_public_graphql_context(html_text)
    if not context:
        return []

    variables = {
        "afterTime": None,
        "beforeTime": None,
        "count": count,
        "cursor": None,
        "feedLocation": "TIMELINE",
        "feedbackSource": 0,
        "focusCommentID": None,
        "id": context["user_id"],
        "memorializedSplitTimeFilter": None,
        "omitPinnedPost": False,
        "postedBy": None,
        "privacy": None,
        "privacySelectorRenderLocation": "COMET_STREAM",
        "referringStoryRenderLocation": "timeline",
        "renderLocation": "timeline",
        "scale": 1,
        "stream_count": count,
        "taggedInOnly": None,
        "trackingCode": None,
        "useDefaultActor": False,
    }

    form = {
        "av": "0",
        "__user": "0",
        "__a": "1",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": PUBLIC_TIMELINE_QUERY_NAME,
        "variables": json.dumps(variables, ensure_ascii=False, separators=(",", ":")),
        "server_timestamps": "true",
        "doc_id": PUBLIC_TIMELINE_DOC_ID,
        "lsd": context["lsd"],
        "jazoest": context["jazoest"],
    }
    data = parse.urlencode(form).encode("utf-8")
    headers = {
        "User-Agent": DEFAULT_UA,
        "Content-Type": "application/x-www-form-urlencoded",
        "x-fb-friendly-name": PUBLIC_TIMELINE_QUERY_NAME,
        "x-fb-lsd": context["lsd"],
    }
    req = request.Request("https://www.facebook.com/api/graphql/", data=data, headers=headers)
    with request.urlopen(req, timeout=30) as response:
        body = response.read().decode("utf-8", errors="replace")

    parts: list[dict[str, Any]] = []
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("for (;;);"):
            line = line[len("for (;;);") :]
        try:
            parts.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return parts


def build_graphql_post_record(node: dict[str, Any]) -> dict[str, Any] | None:
    if node.get("__typename") != "Story":
        return None
    post_id = node.get("post_id")
    permalink = node.get("permalink_url")
    if not post_id or not permalink:
        return None

    comet_sections = node.get("comet_sections") or {}
    message = (((comet_sections.get("content") or {}).get("story") or {}).get("message") or {}).get("text")
    timestamp = (((comet_sections.get("timestamp") or {}).get("story") or {}).get("creation_time"))
    feedback = node.get("feedback") or {}
    attachments = node.get("attachments") or []

    record: dict[str, Any] = {
        "post_id": str(post_id),
        "post_url": normalize_post_url(permalink),
        "creation_time": timestamp,
        "message": message or "",
        "source": "public_graphql",
    }
    if isinstance(feedback, dict) and feedback.get("id"):
        record["feedback"] = {"id": feedback.get("id")}
    if attachments:
        media = (((attachments[0] or {}).get("styles") or {}).get("attachment") or {}).get("media")
        attachment_url = (((attachments[0] or {}).get("styles") or {}).get("attachment") or {}).get("url")
        if attachment_url:
            record["attachment_url"] = normalize_post_url(attachment_url)
        if isinstance(media, dict) and media.get("__typename"):
            record["attachment_type"] = media.get("__typename")
    return record


def walk_graphql_parts(node: Any, found: list[dict[str, Any]]) -> None:
    if isinstance(node, dict):
        record = build_graphql_post_record(node)
        if record:
            found.append(record)
        for value in node.values():
            walk_graphql_parts(value, found)
        return
    if isinstance(node, list):
        for item in node:
            walk_graphql_parts(item, found)


def extract_graphql_post_records(html_text: str, count: int) -> list[dict[str, Any]]:
    parts = fetch_public_timeline_parts(html_text, count)
    if not parts:
        return []
    records: list[dict[str, Any]] = []
    for part in parts:
        walk_graphql_parts(part, records)
    return deduplicate_records(records)


def merge_post_urls(records: list[dict[str, Any]], html_urls: list[str]) -> list[str]:
    urls = set(html_urls)
    for record in records:
        for key in ("post_url", "attachment_url", "wwwURL", "url"):
            value = record.get(key)
            if isinstance(value, str) and value:
                urls.add(normalize_post_url(value))
    return sorted(urls)


def slugify_text(value: str, limit: int = 80) -> str:
    cleaned = re.sub(r"\s+", "-", value.strip())
    cleaned = re.sub(r"[^A-Za-z0-9\u4e00-\u9fff_-]", "", cleaned)
    cleaned = cleaned.strip("-_")
    if not cleaned:
        return "post"
    return cleaned[:limit].rstrip("-_")


def slug_from_url(url: str) -> str:
    parsed = parse.urlsplit(url)
    path = parsed.path.strip("/")
    if path:
        return slugify_text(path.replace("/", "-"), limit=60)
    return parsed.netloc.replace(".", "-")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_output_payload(url: str, result: FetchResult, count: int) -> dict[str, Any]:
    meta = parse_meta_tags(result.html_text)
    html_post_urls = extract_post_urls(result.html_text)
    graphql_records = extract_graphql_post_records(result.html_text, count)
    html_records = extract_post_records_from_html(result.html_text)
    post_records = graphql_records if graphql_records else html_records
    post_urls = merge_post_urls(post_records, html_post_urls)

    notes = [
        "Facebook 公開頁面的 HTML 結構很常變動。",
        "目前腳本會優先使用公開 GraphQL timeline query；失敗時才退回 HTML 解析。",
        "如果公開查詢被 Facebook 調整或限制，可以改用登入後 Cookie 再抓一次。",
        "原始 HTML 與 JSON 會保留，方便後續調整解析規則。",
    ]
    if graphql_records:
        notes.insert(1, f"本次已成功用公開 GraphQL 擷取到 {len(graphql_records)} 篇貼文。")
    else:
        notes.insert(1, "本次公開 GraphQL 沒有回貼文，已退回 HTML 解析。")

    return {
        "requested_url": url,
        "final_url": result.final_url,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "status_code": result.status_code,
        "page": {
            "title": meta.get("og:title") or meta.get("twitter:title"),
            "description": meta.get("og:description") or meta.get("description"),
            "canonical_url": meta.get("og:url"),
            "image": meta.get("og:image"),
        },
        "post_url_count": len(post_urls),
        "post_record_count": len(post_records),
        "post_urls": post_urls,
        "post_records": post_records,
        "notes": notes,
    }


def markdown_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`")


def yaml_escape(value: Any) -> str:
    text = str(value if value is not None else "")
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def format_timestamp(value: Any) -> str:
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()
    return str(value or "")


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return "Facebook Post"


def build_post_markdown(record: dict[str, Any], payload: dict[str, Any]) -> str:
    page = payload.get("page", {})
    message = record.get("message") or record.get("story_text") or ""
    title = first_nonempty_line(message)
    metadata_lines = [
        "---",
        f"post_id: {yaml_escape(record.get('post_id'))}",
        f"title: {yaml_escape(title)}",
        f"page_title: {yaml_escape(page.get('title') or '')}",
        f"requested_url: {yaml_escape(payload.get('requested_url') or '')}",
        f"final_url: {yaml_escape(payload.get('final_url') or '')}",
        f"post_url: {yaml_escape(record.get('post_url') or '')}",
        f"creation_time_utc: {yaml_escape(format_timestamp(record.get('creation_time')))}",
        f"fetched_at_utc: {yaml_escape(payload.get('fetched_at_utc') or '')}",
        f"source: {yaml_escape(record.get('source') or '')}",
        f"attachment_type: {yaml_escape(record.get('attachment_type') or '')}",
        f"attachment_url: {yaml_escape(record.get('attachment_url') or '')}",
        f"feedback_id: {yaml_escape(((record.get('feedback') or {}).get('id')))}",
        f"page_canonical_url: {yaml_escape(page.get('canonical_url') or '')}",
        "---",
        "",
    ]
    lines = metadata_lines
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"原文連結: {record.get('post_url') or ''}")
    lines.append("")
    if message:
        lines.append(message.rstrip())
        lines.append("")
    else:
        lines.append("這篇貼文沒有抓到正文。")
        lines.append("")
    return "\n".join(lines)


def build_index_markdown(payload: dict[str, Any], posts_dir: Path, post_files: list[Path]) -> str:
    page = payload.get("page", {})
    lines = ["# Facebook 貼文索引", ""]
    lines.append(f"- 頁面: {page.get('title') or ''}")
    lines.append(f"- 抓取時間: {payload.get('fetched_at_utc') or ''}")
    lines.append(f"- 貼文數量: {payload.get('post_record_count') or 0}")
    lines.append("")
    lines.append("## 文章列表")
    lines.append("")
    for path, record in zip(post_files, payload.get("post_records", []), strict=False):
        title = first_nonempty_line(record.get("message") or record.get("story_text") or "Facebook Post")
        lines.append(f"- [{title}]({path.name})")
    lines.append("")
    return "\n".join(lines)


def write_post_markdown_files(posts_dir: Path, payload: dict[str, Any]) -> list[str]:
    posts_dir.mkdir(parents=True, exist_ok=True)
    saved_paths: list[str] = []
    post_files: list[Path] = []

    for index, record in enumerate(payload.get("post_records", []), start=1):
        title = first_nonempty_line(record.get("message") or record.get("story_text") or "Facebook Post")
        title_slug = slugify_text(title, limit=50)
        post_id = slugify_text(str(record.get("post_id") or f"post-{index}"), limit=30)
        filename = f"{index:03d}_{post_id}_{title_slug}.md"
        path = posts_dir / filename
        write_text(path, build_post_markdown(record, payload))
        post_files.append(path)
        saved_paths.append(str(path))

    index_path = posts_dir / "index.md"
    write_text(index_path, build_index_markdown(payload, posts_dir, post_files))
    saved_paths.insert(0, str(index_path))
    return saved_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="抓取 Facebook 頁面並把結果存到 ./data")
    parser.add_argument("url", help="Facebook 頁面網址，例如 https://www.facebook.com/dextermchang")
    parser.add_argument("--data-dir", default="data", help="輸出目錄，預設為 ./data")
    parser.add_argument("--count", type=int, default=5, help="嘗試抓取的貼文數量，預設 5")
    parser.add_argument(
        "--cookie",
        default=None,
        help="可選，直接傳入 Cookie header 內容以使用登入 session。",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data_dir = Path(args.data_dir)

    try:
        result = fetch_html(args.url, args.cookie)
    except error.HTTPError as exc:
        print(f"HTTP error: {exc.code} {exc.reason}", file=sys.stderr)
        return 1
    except error.URLError as exc:
        print(f"Network error: {exc.reason}", file=sys.stderr)
        return 1

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    slug = slug_from_url(args.url)
    html_path = data_dir / f"{slug}_{stamp}.html"
    json_path = data_dir / f"{slug}_{stamp}.json"
    posts_dir = data_dir / f"{slug}_{stamp}_posts"

    write_text(html_path, result.html_text)
    payload = build_output_payload(args.url, result, args.count)
    payload["html_snapshot_path"] = str(html_path)
    payload["posts_directory"] = str(posts_dir)
    payload["markdown_files"] = write_post_markdown_files(posts_dir, payload)
    write_json(json_path, payload)

    print(f"已儲存 HTML: {html_path}")
    print(f"已儲存 JSON: {json_path}")
    print(f"已儲存貼文 Markdown 目錄: {posts_dir}")
    print(f"找到貼文網址數量: {payload['post_url_count']}")
    print(f"找到貼文樣式紀錄數量: {payload['post_record_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
