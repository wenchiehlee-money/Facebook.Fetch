#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject "Add to group" issue links into data/我的珍藏-*/ post .md files.

Usage:
    python scripts/inject_add_group_links.py --all   # all saved list dirs
    python scripts/inject_add_group_links.py --dir "data/我的珍藏-股票"
"""
from __future__ import annotations
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import argparse
import re
import urllib.parse
from pathlib import Path

REPO           = "wenchiehlee-money/Facebook.Fetch"
TEMPLATE       = "add_group.yml"
ADD_GROUP_MARKER = "📌 新增至追蹤群組"

# Groups already being tracked (skip injecting for these)
EXISTING_WORKFLOWS = {
    "dextermchang", "yutinghaosfinance", "MarketingDataScienceTMR",
    "FinGuider", "GreenHornFans", "stocksardine", "raikk6",
    "61573146584049", "ForexStrategist", "61578106860333",
    "100054201473657", "intleconobserve", "61565088683715",
}


def page_url_from_post_url(post_url: str) -> str:
    """Derive the Facebook page URL from a post permalink."""
    # https://www.facebook.com/PAGE/posts/... → https://www.facebook.com/PAGE
    m = re.match(r"(https://www\.facebook\.com/[^/?#]+)(?:/posts|/videos|/reels)", post_url)
    if m:
        return m.group(1)
    # https://www.facebook.com/permalink.php?story_fbid=...&id=NNN
    m = re.search(r"[?&]id=(\d+)", post_url)
    if m:
        return f"https://www.facebook.com/profile.php?id={m.group(1)}"
    return ""


def is_already_tracked(page_url: str) -> bool:
    for keyword in EXISTING_WORKFLOWS:
        if keyword in page_url:
            return True
    return False


def build_issue_url(group_name: str, facebook_url: str, triggered_by: str) -> str:
    title = f"新增群組: {group_name}"
    params = {
        "template": TEMPLATE,
        "title":    title,
        "group_name":    group_name,
        "facebook_url":  facebook_url,
        "triggered_by":  triggered_by,
    }
    qs = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return f"https://github.com/{REPO}/issues/new?{qs}"


def inject_file(md_path: Path, repo_root: Path) -> bool:
    """Add 'add group' link to .md file. Returns True if modified."""
    content = md_path.read_text(encoding="utf-8", errors="replace")

    if ADD_GROUP_MARKER in content:
        return False  # already injected

    # Extract metadata
    source_page = re.search(r"^source_page:\s*\"([^\"]+)\"", content, re.MULTILINE)
    post_url    = re.search(r"^post_url:\s*\"([^\"]+)\"",    content, re.MULTILINE)

    if not source_page or not post_url:
        return False

    group_name  = source_page.group(1)
    page_url    = page_url_from_post_url(post_url.group(1))

    if not page_url:
        return False

    if is_already_tracked(page_url):
        return False  # already in daily fetch

    rel_path   = md_path.relative_to(repo_root).as_posix()
    issue_url  = build_issue_url(group_name, page_url, rel_path)

    tag_section = (
        "\n\n---\n"
        f"[{ADD_GROUP_MARKER}: {group_name}]({issue_url})\n"
    )
    md_path.write_text(content + tag_section, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="Process all 我的珍藏-* dirs")
    group.add_argument("--dir", help="Process specific directory")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    if args.all:
        dirs = sorted(repo_root.glob("data/我的珍藏-*/"))
    else:
        dirs = [Path(args.dir).resolve()]

    total = modified = skipped = 0
    for d in dirs:
        for f in sorted(d.glob("*.md")):
            if f.name == "index.md":
                continue
            total += 1
            if inject_file(f, repo_root):
                print(f"  [injected] {f.relative_to(repo_root)}")
                modified += 1
            else:
                skipped += 1

    print(f"\nDone: {modified} injected, {skipped} skipped, {total} total")


if __name__ == "__main__":
    main()
