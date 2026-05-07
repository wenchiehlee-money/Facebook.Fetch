#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
"""
Inject 'Tag to TAIEX.TW' links into Facebook.Fetch .md files.

Usage:
    python scripts/inject_tag_links.py --all          # backfill all existing .md files
    python scripts/inject_tag_links.py --files f1 f2  # specific files (used by GitHub Action)
"""

import argparse
import re
import urllib.parse
from pathlib import Path

TAIEX_REPO    = "wenchiehlee-money/TAIEX.TW"
FB_FETCH_REPO = "wenchiehlee-money/Facebook.Fetch"

US_SYMBOLS = {
    'AMD', 'NVDA', 'GOOGL', 'AAPL', 'META', 'MSFT', 'AMZN', 'TSM',
    'QCOM', 'AVGO', 'INTC', 'MU', 'WDC', 'ORCL', 'DELL', 'HPQ', 'HPE',
    'ASML', 'ARM', 'SMCI', 'MRVL', 'AMAT', 'LRCX', 'KLAC',
}

TAGGED_MARKERS = ("📌 新增貼文至TAIEX.TW比對", "🔄 已標記", "✅ 已比對")


def extract_symbol(filename: str) -> str:
    name_upper = filename.upper()
    for sym in sorted(US_SYMBOLS, key=len, reverse=True):
        if re.search(rf'\b{sym}\b', name_upper) or sym in name_upper:
            return sym
    # TW 4-digit stock code
    m = re.search(r'(?<!\d)(\d{4})(?!\d)', filename)
    if m:
        return m.group(1)
    return ""


def extract_period(filename: str) -> str:
    # Match patterns like Q1、Q2、Q3、Q4 or 第一季 etc.
    q_match = re.search(r'[Qq]([1-4])', filename)
    year_match = re.search(r'(\d{4})', filename)
    if q_match and year_match:
        return f"{year_match.group(1)} Q{q_match.group(1)}"
    return ""


def build_issue_url(symbol: str, rel_path: str, period: str) -> str:
    title = f"{symbol} {period} 財報標記".strip()
    params = {
        "template": "earnings_tag.yml",
        "title":    title,
        "symbol":   symbol,
        "file_path": rel_path,
        "period":   period,
    }
    qs = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return f"https://github.com/{TAIEX_REPO}/issues/new?{qs}"


def inject_file(md_path: Path, repo_root: Path) -> bool:
    """Append tag link to .md file. Returns True if file was modified."""
    content = md_path.read_text(encoding="utf-8")

    if any(m in content for m in TAGGED_MARKERS):
        return False  # already tagged

    rel_path = md_path.relative_to(repo_root).as_posix()
    stem     = md_path.stem  # filename without .md

    symbol = extract_symbol(stem)
    if not symbol:
        return False  # can't identify stock

    period    = extract_period(stem)
    issue_url = build_issue_url(symbol, rel_path, period)

    tag_section = (
        "\n\n---\n"
        f"[📌 新增貼文至TAIEX.TW比對]({issue_url})\n"
    )
    md_path.write_text(content + tag_section, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser(description="Inject TAIEX.TW tag links into .md files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all",   action="store_true", help="Process all .md files under data/")
    group.add_argument("--files", nargs="+",           help="Specific file paths to process")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    if args.all:
        files = sorted(repo_root.glob("data/**/*.md"))
    else:
        files = [Path(f).resolve() for f in args.files]

    total = modified = skipped = 0
    for f in files:
        total += 1
        if not f.exists():
            print(f"  [skip] not found: {f}")
            skipped += 1
            continue
        if inject_file(f, repo_root):
            print(f"  [tagged] {f.relative_to(repo_root)}")
            modified += 1
        else:
            skipped += 1

    print(f"\nDone: {modified} tagged, {skipped} skipped, {total} total")


if __name__ == "__main__":
    main()
