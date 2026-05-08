#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
"""Fetch Facebook saved-list posts and save as Markdown files."""

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

# Reuse helpers from existing script
from fetch_facebook_posts import (
    build_index_markdown,
    build_post_markdown,
    collect_existing_posts,
    slugify_text,
    write_text,
    write_json,
    update_readme,
    parse_markdown_metadata,
    extract_created_date,
    prune_short_posts,
)

DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/147.0.0.0 Safari/537.36"
)
MIN_CHINESE_CHARS = 10  # Lower threshold for saved list items


def fetch_saved_list_html(url: str, cookie: str) -> str:
    # Strip referrer param and use full Chrome headers to get preloaded SSR data
    clean_url = re.sub(r'[&?]referrer=[^&]*', '', url).rstrip('?&')
    headers = {
        "User-Agent": DEFAULT_UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",  # exclude br — Python stdlib can't decompress it
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Cookie": cookie,
    }
    req = request.Request(clean_url, headers=headers)
    with request.urlopen(req, timeout=30) as r:
        raw = r.read()
        try:
            return gzip.decompress(raw).decode("utf-8", errors="replace")
        except Exception:
            return raw.decode("utf-8", errors="replace")


def extract_saved_list_items(html: str) -> list[dict]:
    """Extract SaveListItem records from saved-list page HTML."""
    items = []
    seen: set[str] = set()

    node_re = re.compile(
        r'"__typename":"SaveListItem"[^{]*"id":"([^"]+)"'
        r'.*?"savable_title":\{"text":"((?:[^"\\]|\\.)*)"\}'
        r'.*?"savable_permalink":"((?:[^"\\]|\\.)*)"',
        re.DOTALL,
    )

    for m in node_re.finditer(html):
        item_id, title_raw, url_raw = m.group(1), m.group(2), m.group(3)
        if item_id in seen:
            continue
        seen.add(item_id)

        try:
            title = json.loads(f'"{title_raw}"')
        except Exception:
            title = title_raw.encode().decode("unicode_escape", errors="replace")

        post_url = url_raw.replace("\\/", "/")

        # Count Chinese chars
        chinese = len(re.findall(r"[一-鿿]", title))
        if chinese < MIN_CHINESE_CHARS:
            continue

        items.append({
            "post_id": item_id,
            "post_url": post_url,
            "message": title,
            "creation_time": None,
            "source": "saved_list",
        })

    return items


def extract_list_title(html: str) -> str:
    """Extract the saved list name from page HTML."""
    # Try page <title> first — for saved lists it's the collection name
    t = re.search(r"<title[^>]*>([^<]+)</title>", html, re.IGNORECASE)
    if t:
        title = t.group(1).strip()
        # Exclude generic Facebook titles
        if title and title not in ("Facebook", "Log in", "登入"):
            return title
    # Fallback: look for SaveList name in JSON
    m = re.search(r'"SaveList".*?"name":"([^"]+)"', html, re.DOTALL)
    if m:
        return m.group(1)
    return "我的珍藏"


def build_post_filename_saved(record: dict, index: int) -> str:
    title = record.get("message", "")
    first_line = next((l.strip() for l in title.splitlines() if l.strip()), "saved-post")
    slug = slugify_text(first_line, limit=80)
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    return f"{today}_{slug}.md"


def build_saved_post_markdown(record: dict, list_title: str, url: str) -> str:
    message = record.get("message", "")
    title = next((l.strip() for l in message.splitlines() if l.strip()), "saved post")
    post_url = record.get("post_url", "")
    today = datetime.now(tz=timezone.utc).isoformat()

    lines = [
        "---",
        f'post_id: "{record.get("post_id", "")}"',
        f'title: "{title[:200].replace(chr(34), chr(39))}"',
        f'page_title: "{list_title}"',
        f'requested_url: "{url}"',
        f'post_url: "{post_url}"',
        f'creation_time_utc: ""',
        f'fetched_at_utc: "{today}"',
        f'source: "saved_list"',
        "---",
        "",
        f"# {title}",
        "",
        f"原文連結: {post_url}",
        "",
    ]
    return "\n".join(lines) + message.rstrip() + "\n"


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
            # Update existing
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

    # Build index
    markdown_files = sorted(p for p in posts_dir.glob("*.md") if p.name != "index.md")

    # Minimal payload for index builder
    payload = {
        "fetched_at_utc": fetched_at,
        "requested_url": url,
        "final_url": url,
        "page": {
            "title": list_title,
            "follower_count": None,
            "canonical_url": url,
        },
    }
    write_text(posts_dir / "index.md", build_index_markdown(payload, markdown_files))

    return new_paths, new_ids


def load_env_cookie() -> str:
    """Load FB_COOKIE from .env file in the repo root."""
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        return ""
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("FB_COOKIE="):
            return line[len("FB_COOKIE="):]
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="抓取 Facebook 珍藏清單並存成 Markdown")
    parser.add_argument("url", help="Facebook 珍藏清單網址")
    parser.add_argument("--data-dir", default="data", help="輸出目錄，預設 ./data")
    parser.add_argument("--cookie", default=None, help="登入 Cookie header 值（省略則從 .env 讀取）")
    args = parser.parse_args()

    if args.cookie:
        cookie = args.cookie
    else:
        cookie = load_env_cookie()

    if not cookie:
        print("錯誤：請提供 --cookie 或在 .env 設定 FB_COOKIE", file=sys.stderr)
        return 1

    print(f"抓取珍藏清單: {args.url}")
    html = fetch_saved_list_html(args.url, cookie)

    list_title = extract_list_title(html)
    print(f"清單名稱: {list_title}")

    items = extract_saved_list_items(html)
    print(f"找到貼文: {len(items)} 篇")

    if not items:
        print("未找到任何貼文，請確認 cookie 是否有效且已登入。", file=sys.stderr)
        return 1

    data_dir = Path(args.data_dir)
    folder = f"我的珍藏-{list_title}" if list_title else "我的珍藏"
    posts_dir = data_dir / slugify_text(folder, limit=60, separator=" ")

    fetched_at = datetime.now(tz=timezone.utc).isoformat()
    new_paths, new_ids = write_saved_post_files(posts_dir, items, list_title, args.url, fetched_at)

    summary = {
        "requested_url": args.url,
        "fetched_at_utc": fetched_at,
        "list_title": list_title,
        "total_items": len(items),
        "new_post_count": len(new_ids),
        "new_post_ids": new_ids,
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
