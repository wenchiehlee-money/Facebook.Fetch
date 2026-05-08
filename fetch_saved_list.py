#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
"""Fetch Facebook saved-list posts (all pages) and save as Markdown files."""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import argparse
import gzip
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib import parse, request

from fetch_facebook_posts import (
    build_index_markdown,
    collect_existing_posts,
    slugify_text,
    write_text,
    write_json,
    update_readme,
)

DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/147.0.0.0 Safari/537.36"
)
MIN_CHINESE_CHARS = 5
PAGINATION_DOC_ID  = "26828271073456469"
PAGINATION_QUERY   = "CometSaveCollectionAllItemsPaginationQuery"


# ── HTTP helpers ────────────────────────────────────────────────────────────

def _chrome_headers(cookie: str, extra: dict | None = None) -> dict:
    h = {
        "User-Agent": DEFAULT_UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Cookie": cookie,
    }
    if extra:
        h.update(extra)
    return h


def _decompress(raw: bytes) -> str:
    try:
        return gzip.decompress(raw).decode("utf-8", errors="replace")
    except Exception:
        return raw.decode("utf-8", errors="replace")


def fetch_html(url: str, cookie: str) -> str:
    clean_url = re.sub(r"[&?]referrer=[^&]*", "", url).rstrip("?&")
    req = request.Request(clean_url, headers=_chrome_headers(cookie))
    with request.urlopen(req, timeout=30) as r:
        return _decompress(r.read())


# ── Auth token extraction ────────────────────────────────────────────────────

def extract_auth(html: str, cookie: str = "") -> dict:
    lsd     = re.search(r'"LSD"[^}]*"token":"([^"]+)"', html)
    dtsg    = re.search(r'"DTSGInitialData"[^}]*"token":"([^"]+)"', html)
    jazoest = re.search(r'jazoest[^\d]*(\d{4,})', html)
    # Try multiple patterns for user ID
    user_id = (
        re.search(r'"USER_ID":"(\d+)"', html) or
        re.search(r'"actorID":"(\d+)"', html) or
        re.search(r'"userID":"(\d+)"', html) or
        re.search(r'c_user=(\d+)', cookie)  # fallback from cookie
    )
    return {
        "lsd":     lsd.group(1)     if lsd     else "",
        "dtsg":    dtsg.group(1)    if dtsg    else "",
        "user_id": user_id.group(1) if user_id else "",
        "jazoest": jazoest.group(1) if jazoest else "",
    }


# ── Saved-list item parsing ──────────────────────────────────────────────────

_NODE_RE = re.compile(
    r'"__typename":"SaveListItem"[^{]*"id":"([^"]+)"'
    r'.*?"savable_title":\{"text":"((?:[^"\\]|\\.)*)"\}'
    r'.*?"savable_permalink":"((?:[^"\\]|\\.)*)"'
    r'.*?"savable_attributes":\[(.*?)\]',
    re.DOTALL,
)


def _parse_source(attrs_raw: str) -> str:
    texts = re.findall(r'"text":"([^"]+)"', attrs_raw)
    # last entry is typically the page/group name
    for t in reversed(texts):
        if t not in ("貼文", "視頻", "1 張相片", "照片", "相片") and not re.match(r"^\d+ 張", t):
            return t
    return texts[-1] if texts else ""


def parse_items(text: str, seen: set[str]) -> list[dict]:
    items = []
    for m in _NODE_RE.finditer(text):
        item_id, title_raw, url_raw, attrs_raw = m.groups()
        if item_id in seen:
            continue
        seen.add(item_id)

        try:
            title = json.loads(f'"{title_raw}"')
        except Exception:
            title = title_raw.encode().decode("unicode_escape", errors="replace")

        if len(re.findall(r"[一-鿿]", title)) < MIN_CHINESE_CHARS:
            continue

        source = _parse_source(attrs_raw)
        items.append({
            "post_id":  item_id,
            "post_url": url_raw.replace("\\/", "/"),
            "message":  title,
            "source":   source,
            "creation_time": None,
        })
    return items


# ── GraphQL pagination ───────────────────────────────────────────────────────

def fetch_next_page(
    collection_id: str,
    cursor: str,
    auth: dict,
    cookie: str,
) -> tuple[str, str | None]:
    """POST to GraphQL pagination endpoint. Returns (response_text, next_cursor|None)."""
    variables = {
        "collectionID": collection_id,
        "count": 10,
        "cursor": cursor,
        "feedLocation": "SAVED_DASHBOARD",
        "feedbackSource": 58,
        "focusCommentID": None,
        "scale": 1,
        "useDefaultActor": False,
        "__relay_internal__pv__CometUFICommentAutoTranslationTyperelayprovider": "AUTO_TRANSLATE",
        "__relay_internal__pv__CometUFICommentAvatarStickerAnimatedImagerelayprovider": False,
        "__relay_internal__pv__CometUFICommentActionLinksRewriteEnabledrelayprovider": False,
        "__relay_internal__pv__IsWorkUserrelayprovider": False,
        "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False,
        "__relay_internal__pv__CometUFISingleLineUFIrelayprovider": True,
        "__relay_internal__pv__CometUFIShareActionMigrationrelayprovider": True,
        "__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider": True,
    }
    form = {
        "av": auth["user_id"],
        "__user": auth["user_id"],
        "__a": "1",
        "fb_dtsg": auth["dtsg"],
        "jazoest": auth["jazoest"],
        "lsd": auth["lsd"],
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": PAGINATION_QUERY,
        "variables": json.dumps(variables, separators=(",", ":")),
        "server_timestamps": "true",
        "doc_id": PAGINATION_DOC_ID,
    }
    data = parse.urlencode(form).encode("utf-8")
    headers = {
        "User-Agent": DEFAULT_UA,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "x-fb-friendly-name": PAGINATION_QUERY,
        "x-fb-lsd": auth["lsd"],
        "Origin": "https://www.facebook.com",
        "Referer": f"https://www.facebook.com/saved/?list_id={collection_id}",
        "Cookie": cookie,
    }
    req = request.Request("https://www.facebook.com/api/graphql/", data=data, headers=headers)
    with request.urlopen(req, timeout=30) as r:
        text = _decompress(r.read())

    cursor_m  = re.search(r'"end_cursor":"([^"]+)"', text)
    has_next  = re.search(r'"has_next_page":(true|false)', text)
    next_cur  = cursor_m.group(1) if cursor_m and has_next and has_next.group(1) == "true" else None
    return text, next_cur


# ── Page title / list name ───────────────────────────────────────────────────

def extract_list_title(html: str) -> str:
    t = re.search(r"<title[^>]*>([^<]+)</title>", html, re.IGNORECASE)
    if t:
        title = t.group(1).strip()
        if title and title not in ("Facebook", "Log in", "登入"):
            return title
    m = re.search(r'"SaveList".*?"name":"([^"]+)"', html, re.DOTALL)
    return m.group(1) if m else "我的珍藏"


def extract_collection_id(url: str) -> str:
    m = re.search(r"list_id=(\d+)", url)
    return m.group(1) if m else ""


def extract_initial_cursor(html: str) -> str | None:
    """Always return cursor if present — Facebook paginates even when hasNext=false in SSR data."""
    m = re.search(r'"end_cursor":"([^"]+)"', html)
    return m.group(1) if m else None


# ── Markdown generation ──────────────────────────────────────────────────────

def build_saved_post_markdown(record: dict, list_title: str, url: str) -> str:
    message  = record.get("message", "")
    title    = next((l.strip() for l in message.splitlines() if l.strip()), "saved post")
    post_url = record.get("post_url", "")
    source   = record.get("source", "")
    today    = datetime.now(tz=timezone.utc).isoformat()

    lines = [
        "---",
        f'post_id: "{record.get("post_id", "")}"',
        f'title: "{title[:200].replace(chr(34), chr(39))}"',
        f'page_title: "{list_title}"',
        f'source_page: "{source}"',
        f'requested_url: "{url}"',
        f'post_url: "{post_url}"',
        f'creation_time_utc: ""',
        f'fetched_at_utc: "{today}"',
        f'source: "saved_list"',
        "---",
        "",
        f"# {title}",
        "",
        f"來源：{source}" if source else "",
        f"原文連結: {post_url}",
        "",
    ]
    return "\n".join(l for l in lines if l is not None) + message.rstrip() + "\n"


def build_post_filename_saved(record: dict, index: int) -> str:
    title = record.get("message", "")
    first_line = next((l.strip() for l in title.splitlines() if l.strip()), "saved-post")
    slug = slugify_text(first_line, limit=80)
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    return f"{today}_{slug}.md"


def write_saved_post_files(
    posts_dir: Path, records: list[dict], list_title: str, url: str, fetched_at: str
) -> tuple[list[str], list[str]]:
    posts_dir.mkdir(parents=True, exist_ok=True)
    existing = collect_existing_posts(posts_dir)
    new_paths: list[str] = []
    new_ids: list[str] = []

    for idx, record in enumerate(records, start=1):
        post_id = str(record.get("post_id", ""))
        if post_id and post_id in existing:
            write_text(existing[post_id], build_saved_post_markdown(record, list_title, url))
            continue

        filename = build_post_filename_saved(record, idx)
        path = posts_dir / filename
        if path.exists():
            path = posts_dir / f"{path.stem}_{post_id or idx}.md"

        write_text(path, build_saved_post_markdown(record, list_title, url))
        new_paths.append(str(path))
        if post_id:
            new_ids.append(post_id)

    markdown_files = sorted(p for p in posts_dir.glob("*.md") if p.name != "index.md")
    payload = {
        "fetched_at_utc": fetched_at,
        "requested_url": url,
        "final_url": url,
        "page": {"title": list_title, "follower_count": None, "canonical_url": url},
    }
    write_text(posts_dir / "index.md", build_index_markdown(payload, markdown_files))
    return new_paths, new_ids


# ── .env loader ──────────────────────────────────────────────────────────────

def load_env_cookie() -> str:
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        return ""
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("FB_COOKIE="):
            return line[len("FB_COOKIE="):]
    return ""


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="抓取 Facebook 珍藏清單（全部分頁）並存成 Markdown")
    parser.add_argument("url", help="Facebook 珍藏清單網址")
    parser.add_argument("--data-dir", default="data", help="輸出目錄，預設 ./data")
    parser.add_argument("--cookie", default=None, help="登入 Cookie（省略則從 .env 讀取）")
    args = parser.parse_args()

    cookie = args.cookie or load_env_cookie()
    if not cookie:
        print("錯誤：請提供 --cookie 或在 .env 設定 FB_COOKIE", file=sys.stderr)
        return 1

    print(f"抓取珍藏清單: {args.url}")
    html = fetch_html(args.url, cookie)

    list_title    = extract_list_title(html)
    collection_id = extract_collection_id(args.url)
    auth          = extract_auth(html, cookie)
    print(f"清單名稱: {list_title}  collection_id={collection_id}")

    seen: set[str] = set()
    all_items = parse_items(html, seen)
    print(f"  第 1 頁: {len(all_items)} 篇")

    # Paginate through remaining pages
    cursor = extract_initial_cursor(html)
    page = 2
    while cursor:
        try:
            page_text, cursor = fetch_next_page(collection_id, cursor, auth, cookie)
            new = parse_items(page_text, seen)
            all_items.extend(new)
            print(f"  第 {page} 頁: {len(new)} 篇（累計 {len(all_items)}）")
            page += 1
        except Exception as e:
            print(f"  分頁錯誤（停止）: {e}", file=sys.stderr)
            break

    print(f"共找到貼文: {len(all_items)} 篇")

    if not all_items:
        print("未找到任何貼文，請確認 cookie 是否有效且已登入。", file=sys.stderr)
        return 1

    data_dir  = Path(args.data_dir)
    folder    = f"我的珍藏-{list_title}" if list_title else "我的珍藏"
    posts_dir = data_dir / slugify_text(folder, limit=60, separator=" ")

    fetched_at = datetime.now(tz=timezone.utc).isoformat()
    new_paths, new_ids = write_saved_post_files(posts_dir, all_items, list_title, args.url, fetched_at)

    summary = {
        "requested_url":  args.url,
        "fetched_at_utc": fetched_at,
        "list_title":     list_title,
        "total_items":    len(all_items),
        "new_post_count": len(new_ids),
        "new_post_ids":   new_ids,
        "new_markdown_files": new_paths,
        "posts_directory": str(posts_dir),
    }
    write_json(posts_dir / "latest_fetch_summary.json", summary)
    update_readme(posts_dir, {
        "page": {"title": folder, "follower_count": None},
        "fetched_at_utc": fetched_at,
    })

    print(f"貼文目錄: {posts_dir}")
    print(f"本次新增貼文: {len(new_ids)} 篇")
    for p in new_paths:
        print(f"  新增: {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
