#!/usr/bin/env python3
"""Fetch public Facebook page posts and save only new posts as Markdown files."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
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

    feedback = node.get("feedback")
    if isinstance(feedback, dict) and feedback.get("id"):
        record["feedback"] = {"id": feedback.get("id")}
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

    normalized_permalink = normalize_post_url(permalink)
    message_text = message or ""
    if not message_text.strip() and ("/reel/" in normalized_permalink or "/videos/" in normalized_permalink):
        return None

    record: dict[str, Any] = {
        "post_id": str(post_id),
        "post_url": normalized_permalink,
        "creation_time": timestamp,
        "message": message_text,
        "source": "public_graphql",
    }
    if isinstance(feedback, dict) and feedback.get("id"):
        record["feedback"] = {"id": feedback.get("id")}
    if attachments:
        attachment = ((attachments[0] or {}).get("styles") or {}).get("attachment") or {}
        media = attachment.get("media")
        attachment_url = attachment.get("url")
        if attachment_url:
            record["attachment_url"] = normalize_post_url(attachment_url)
        if isinstance(media, dict) and media.get("__typename"):
            record["attachment_type"] = media.get("__typename")
            thumbnail = media.get("thumbnailImage") or {}
            if isinstance(thumbnail, dict) and thumbnail.get("uri"):
                record["image_url"] = thumbnail.get("uri")
            elif media.get("image") and isinstance(media.get("image"), dict) and media["image"].get("uri"):
                record["image_url"] = media["image"].get("uri")
            elif media.get("photo_image") and isinstance(media.get("photo_image"), dict) and media["photo_image"].get("uri"):
                record["image_url"] = media["photo_image"].get("uri")
            elif media.get("viewer_image") and isinstance(media.get("viewer_image"), dict) and media["viewer_image"].get("uri"):
                record["image_url"] = media["viewer_image"].get("uri")
            elif media.get("previewImage") and isinstance(media.get("previewImage"), dict) and media["previewImage"].get("uri"):
                record["image_url"] = media["previewImage"].get("uri")
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


def slugify_text(value: str, limit: int = 80, separator: str = "-") -> str:
    cleaned = re.sub(r"\s+", separator, value.strip())
    allowed = rf"[^A-Za-z0-9\u4e00-\u9fff_{re.escape(separator)}-]"
    cleaned = re.sub(allowed, "", cleaned)
    cleaned = cleaned.strip(f"{separator}-_")
    if not cleaned:
        return "post"
    return cleaned[:limit].rstrip(f"{separator}-_")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def format_timestamp(value: Any) -> str:
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value, tz=timezone.utc).isoformat()
    return str(value or "")


def yaml_escape(value: Any) -> str:
    text = str(value if value is not None else "")
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return "Facebook Post"


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
        "只有新貼文才會新增 Markdown 檔，既有文章不會重寫。",
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


def build_post_markdown(record: dict[str, Any], payload: dict[str, Any]) -> str:
    page = payload.get("page", {})
    message = record.get("message") or record.get("story_text") or ""
    title = first_nonempty_line(message)
    image_url = record.get("image_url") or ""
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
        f"image_url: {yaml_escape(image_url)}",
        f"feedback_id: {yaml_escape(((record.get('feedback') or {}).get('id')))}",
        f"page_canonical_url: {yaml_escape(page.get('canonical_url') or '')}",
        "---",
        "",
        f"# {title}",
        "",
        f"原文連結: {record.get('post_url') or ''}",
        "",
    ]
    if image_url:
        metadata_lines.extend([
            f"![{title or 'post image'}]({image_url})",
            "",
        ])
    body = message.rstrip() if message else "這篇貼文沒有抓到正文。"
    return "\n".join(metadata_lines) + body + "\n"


def build_index_markdown(payload: dict[str, Any], markdown_files: list[Path]) -> str:
    page = payload.get("page", {})
    lines = ["# Facebook 貼文索引", ""]
    lines.append(f"- 頁面: {page.get('title') or ''}")
    lines.append(f"- 抓取時間: {payload.get('fetched_at_utc') or ''}")
    lines.append(f"- 已收錄貼文數量: {len(markdown_files)}")
    lines.append("")
    lines.append("## 文章列表")
    lines.append("")

    items: list[tuple[str, str, str]] = []
    for path in markdown_files:
        metadata = parse_markdown_metadata(path)
        title = metadata.get("title") or (path.stem.split("_", 1)[1] if "_" in path.stem else path.stem)
        created_date = extract_created_date(metadata, path)
        items.append((created_date, title, path.name))

    for created_date, title, filename in sorted(items, key=lambda item: (item[0], item[1]), reverse=True):
        if created_date:
            lines.append(f"- `{created_date}` [{title}]({filename})")
        else:
            lines.append(f"- [{title}]({filename})")
    lines.append("")
    return "\n".join(lines)


def parse_markdown_metadata(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    if not text.startswith("---\n"):
        return {}

    metadata: dict[str, str] = {}
    lines = text.splitlines()
    for line in lines[1:]:
        if line == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata


def extract_created_date(metadata: dict[str, str], path: Path) -> str:
    creation = metadata.get("creation_time_utc", "")
    if creation:
        return creation[:10]
    if "_" in path.stem:
        return path.stem.split("_", 1)[0]
    return ""


def build_readme_post_line(posts_dir: Path, path: Path) -> str:
    metadata = parse_markdown_metadata(path)
    title = metadata.get("title") or (path.stem.split("_", 1)[1] if "_" in path.stem else path.stem)
    created_date = extract_created_date(metadata, path)
    relative_path = parse.quote(path.as_posix(), safe="/")
    if created_date:
        return f"- `{created_date}` [{title}]({relative_path})"
    return f"- [{title}]({relative_path})"


def build_readme_group_summary(posts_dir: Path) -> str:
    markdown_files = sorted(path for path in posts_dir.glob("*.md") if path.name != "index.md")
    summary_path = posts_dir / "latest_fetch_summary.json"
    page_title = posts_dir.name
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            page_title = summary.get("page", {}).get("title") or page_title
        except (OSError, json.JSONDecodeError):
            pass
    index_path = parse.quote((posts_dir / "index.md").as_posix(), safe="/")
    return f"### [{page_title}]({index_path}) (已收錄: {len(markdown_files)})"


def build_readme_generated_section(data_dir: Path) -> str:
    group_dirs = sorted(
        path for path in data_dir.iterdir()
        if path.is_dir() and (path / "index.md").exists()
    )
    lines = ["## 自動更新清單", ""]
    if not group_dirs:
        lines.append("- 目前沒有 group")
        lines.append("")
        return "\n".join(lines)

    for posts_dir in group_dirs:
        lines.append(build_readme_group_summary(posts_dir))
        lines.append("")
    return "\n".join(lines)


def update_readme(posts_dir: Path, payload: dict[str, Any]) -> None:
    readme_path = Path("README.md")
    try:
        text = readme_path.read_text(encoding="utf-8")
    except OSError:
        return

    start_marker = "<!-- AUTO-GENERATED:POSTS START -->"
    end_marker = "<!-- AUTO-GENERATED:POSTS END -->"
    generated = build_readme_generated_section(posts_dir.parent)
    replacement = f"{start_marker}\n{generated}\n{end_marker}"

    pattern = re.compile(rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}", re.DOTALL)
    text = pattern.sub("", text).strip()

    parts = text.split("\n\n", 2)
    if len(parts) >= 2:
        text = parts[0] + "\n\n" + parts[1] + "\n\n" + replacement
        if len(parts) == 3:
            text += "\n\n" + parts[2]
    else:
        text = replacement + "\n\n" + text

    readme_path.write_text(text.rstrip() + "\n", encoding="utf-8")


def collect_existing_post_ids(posts_dir: Path) -> set[str]:
    existing: set[str] = set()
    if not posts_dir.exists():
        return existing
    for path in posts_dir.glob("*.md"):
        if path.name == "index.md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        match = re.search(r"^post_id:\s*\"([^\"]+)\"", text, re.MULTILINE)
        if match:
            existing.add(match.group(1))
    return existing


def build_post_filename(record: dict[str, Any], index: int) -> str:
    title = first_nonempty_line(record.get("message") or record.get("story_text") or "Facebook Post")
    title_slug = slugify_text(title, limit=80)
    created_date = format_timestamp(record.get("creation_time"))[:10]
    if not created_date or created_date == "":
        created_date = f"post-{index:03d}"
    return f"{created_date}_{title_slug}.md"


def write_post_markdown_files(posts_dir: Path, payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    posts_dir.mkdir(parents=True, exist_ok=True)
    existing_post_ids = collect_existing_post_ids(posts_dir)
    new_paths: list[str] = []
    new_ids: list[str] = []

    for index, record in enumerate(payload.get("post_records", []), start=1):
        post_id = str(record.get("post_id") or "")
        if post_id and post_id in existing_post_ids:
            continue
        filename = build_post_filename(record, index)
        path = posts_dir / filename
        if path.exists():
            suffix = str(record.get("post_id") or index)
            path = posts_dir / f"{path.stem}_{suffix}.md"
        write_text(path, build_post_markdown(record, payload))
        new_paths.append(str(path))
        if post_id:
            new_ids.append(post_id)
            existing_post_ids.add(post_id)

    markdown_files = sorted(path for path in posts_dir.glob("*.md") if path.name != "index.md")
    write_text(posts_dir / "index.md", build_index_markdown(payload, markdown_files))
    return new_paths, new_ids


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="抓取 Facebook 頁面並把新貼文存到 ./data")
    parser.add_argument("url", help="Facebook 頁面網址，例如 https://www.facebook.com/dextermchang")
    parser.add_argument("--data-dir", default="data", help="輸出目錄，預設為 ./data")
    parser.add_argument("--count", type=int, default=20, help="每次檢查的最新貼文數量，預設 20")
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

    payload = build_output_payload(args.url, result, args.count)
    page_title = payload.get("page", {}).get("title") or parse.urlsplit(args.url).path.strip("/") or "Facebook Page"
    posts_dir = data_dir / slugify_text(page_title, limit=120, separator=" ")
    new_markdown_files, new_post_ids = write_post_markdown_files(posts_dir, payload)

    summary = {
        "requested_url": payload["requested_url"],
        "final_url": payload["final_url"],
        "fetched_at_utc": payload["fetched_at_utc"],
        "page": payload["page"],
        "checked_post_count": payload["post_record_count"],
        "new_post_count": len(new_post_ids),
        "new_post_ids": new_post_ids,
        "new_markdown_files": new_markdown_files,
        "posts_directory": str(posts_dir),
        "notes": payload["notes"],
    }
    write_json(posts_dir / "latest_fetch_summary.json", summary)
    update_readme(posts_dir, payload)

    print(f"貼文目錄: {posts_dir}")
    print(f"本次檢查貼文數量: {payload['post_record_count']}")
    print(f"本次新增貼文數量: {len(new_post_ids)}")
    for path in new_markdown_files:
        print(f"新增 Markdown: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
