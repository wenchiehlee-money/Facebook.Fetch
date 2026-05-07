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
import csv
import re
import urllib.parse
from pathlib import Path

TAIEX_REPO    = "wenchiehlee-money/TAIEX.TW"
FB_FETCH_REPO = "wenchiehlee-money/Facebook.Fetch"

# Fallback hardcoded symbols (used when ConceptStocks CSVs are unavailable)
_FALLBACK_SYMBOLS: dict[str, str] = {
    'AMD': 'AMD', 'NVDA': 'NVDA', 'GOOGL': 'GOOGL', 'AAPL': 'AAPL',
    'META': 'META', 'MSFT': 'MSFT', 'AMZN': 'AMZN', 'TSM': 'TSM',
    'QCOM': 'QCOM', 'AVGO': 'AVGO', 'INTC': 'INTC', 'MU': 'MU',
    'WDC': 'WDC', 'ORCL': 'ORCL', 'DELL': 'DELL', 'HPQ': 'HPQ',
    'HPE': 'HPE', 'ASML': 'ASML', 'ARM': 'ARM', 'SNDK': 'SNDK',
    'LNVGY': 'LNVGY',
}

# Concept-name → ticker overrides (names extracted from companyinfo column headers)
_CONCEPT_OVERRIDES: dict[str, str] = {
    'SANDISK':  'SNDK',
    'NVIDIA':   'NVDA',
    'NVIIDA':   'NVDA',
    'GOOGLE':   'GOOGL',
    'ALPHABET': 'GOOGL',
    'BROADCOM': 'AVGO',
    'AMAZON':   'AMZN',
    'APPLE':    'AAPL',
    'MICROSOFT':'MSFT',
    'MICRON':   'MU',
    'QUALCOMM': 'QCOM',
    'INTEL':    'INTC',
    'TSMC':     'TSM',
    'LENOVO':   'LNVGY',
    'ORACLE':   'ORCL',
    'META':     'META',
    'OPENAI':   'OPENAI',
}

TAGGED_MARKERS = ("📌 新增貼文至TAIEX.TW比對", "🔄 已標記", "✅ 已比對")


def load_symbols_from_conceptstocks(repo_root: Path) -> dict[str, str]:
    """Load name→ticker mapping from ConceptStocks CSVs (sibling repo).

    Returns dict: {uppercase_name_or_alias: ticker}
    Priority: metadata Ticker > concept column aliases > fallback hardcoded list.
    """
    mapping: dict[str, str] = dict(_FALLBACK_SYMBOLS)
    mapping.update(_CONCEPT_OVERRIDES)

    cs_root = repo_root.parent / "ConceptStocks"

    # 1. raw_conceptstock_company_metadata.csv → Ticker + 公司名稱 keywords
    metadata_path = cs_root / "raw_conceptstock_company_metadata.csv"
    if metadata_path.exists():
        with open(metadata_path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                ticker = (row.get("Ticker") or "").strip()
                name   = (row.get("公司名稱") or "").strip()
                if not ticker or ticker == "-":
                    continue
                mapping[ticker.upper()] = ticker
                # Add first meaningful word of company name as alias
                for word in re.split(r'[\s,.]', name):
                    w = word.strip().upper()
                    if len(w) >= 3 and not w.isdigit():
                        mapping.setdefault(w, ticker)

    # 2. raw_companyinfo.csv → concept column headers (strip 概念)
    companyinfo_path = cs_root / "raw_companyinfo.csv"
    if companyinfo_path.exists():
        with open(companyinfo_path, encoding="utf-8") as f:
            fieldnames = next(csv.reader(f))
        for col in fieldnames:
            if col.endswith("概念"):
                alias = col[:-2].upper()  # strip 概念
                if alias in _CONCEPT_OVERRIDES:
                    mapping.setdefault(alias, _CONCEPT_OVERRIDES[alias])
                elif alias in mapping:
                    pass  # already mapped
                else:
                    mapping.setdefault(alias, alias)  # use alias as ticker

    return mapping


def extract_symbol(filename: str, sym_map: dict[str, str]) -> str:
    """Return ticker for the stock mentioned in filename, or '' if unrecognised."""
    name_upper = filename.upper()

    # Pass 1: exact ticker substring match (short ≤6 chars, all-caps)
    tickers = {a: t for a, t in sym_map.items() if a == t and len(a) <= 6}
    for ticker in sorted(tickers, key=len, reverse=True):
        if ticker in name_upper:
            return tickers[ticker]

    # Pass 2: company name / alias with word boundary (longer aliases like SANDISK)
    aliases = {a: t for a, t in sym_map.items() if a != t or len(a) > 6}
    for alias in sorted(aliases, key=len, reverse=True):
        if re.search(rf'(?<![A-Z]){re.escape(alias)}', name_upper):
            return aliases[alias]

    # Pass 3: TW 4-digit stock code (exclude years 1900-2099)
    for m in re.finditer(r'(?<!\d)(\d{4})(?!\d)', filename):
        code = m.group(1)
        if not (1900 <= int(code) <= 2099):
            return code
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


def inject_file(md_path: Path, repo_root: Path, sym_map: dict[str, str]) -> bool:
    """Append tag link to .md file. Returns True if file was modified."""
    content = md_path.read_text(encoding="utf-8")

    if any(m in content for m in TAGGED_MARKERS):
        return False  # already tagged

    rel_path = md_path.relative_to(repo_root).as_posix()
    stem     = md_path.stem  # filename without .md

    symbol = extract_symbol(stem, sym_map)
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


def get_badge_status(md_path: Path) -> str:
    """Return the current badge status of a .md file.

    Returns one of:
      '✅'  — issue closed (已比對)
      '🔄'  — issue open (已標記)
      '📌'  — tag link injected but no issue yet
      ''    — not tagged at all
    """
    try:
        content = md_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    if "✅ 已比對" in content:
        return "✅"
    if "🔄 已標記" in content:
        return "🔄"
    if "📌 新增貼文至TAIEX.TW比對" in content:
        return "📌"
    return ""


def update_index(repo_root: Path) -> int:
    """Scan all data/**/index.md files and prefix each list item with badge status.

    Format:
      - `YYYY-MM-DD` [title](file.md)           → no badge, no change
      - `YYYY-MM-DD` 📌 [title](file.md)        → has tag link but no issue
      - `YYYY-MM-DD` 🔄 [title](file.md)        → issue submitted
      - `YYYY-MM-DD` ✅ [title](file.md)        → issue closed / compared

    Returns number of index files updated.
    """
    updated = 0
    # Match list item pattern: - `YYYY-MM-DD` [optional_badge ][title](file.md)
    item_re = re.compile(
        r'^(- `\d{4}-\d{2}-\d{2}` )(?:[✅🔄📌]\s+)?(\[.*?\]\(([^)]+\.md)\))(.*)$'
    )

    for index_path in sorted(repo_root.glob("data/**/index.md")):
        page_dir = index_path.parent
        lines    = index_path.read_text(encoding="utf-8").splitlines(keepends=True)
        new_lines = []
        changed   = False

        for line in lines:
            m = item_re.match(line.rstrip("\n"))
            if m:
                prefix, link_part, md_filename, rest = m.groups()
                md_file = page_dir / md_filename
                badge = get_badge_status(md_file) if md_file.exists() else ""
                badge_str = f"{badge} " if badge else ""
                new_line = f"{prefix}{badge_str}{link_part}{rest}\n"
                if new_line != line:
                    changed = True
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        if changed:
            index_path.write_text("".join(new_lines), encoding="utf-8")
            print(f"  [index] updated: {index_path.relative_to(repo_root)}")
            updated += 1

    return updated


def main():
    parser = argparse.ArgumentParser(description="Inject TAIEX.TW tag links into .md files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all",          action="store_true", help="Process all .md files under data/")
    group.add_argument("--files",        nargs="+",           help="Specific file paths to process")
    group.add_argument("--update-index", action="store_true", help="Only update index.md badge status (no injection)")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    if args.update_index:
        n = update_index(repo_root)
        print(f"\nDone: {n} index file(s) updated")
        return

    sym_map = load_symbols_from_conceptstocks(repo_root)
    print(f"  Loaded {len(sym_map)} symbol aliases")

    if args.all:
        files = sorted(repo_root.glob("data/**/*.md"))
        # exclude index.md files
        files = [f for f in files if f.name != "index.md"]
    else:
        files = [Path(f).resolve() for f in args.files]

    total = modified = skipped = 0
    for f in files:
        total += 1
        if not f.exists():
            print(f"  [skip] not found: {f}")
            skipped += 1
            continue
        if inject_file(f, repo_root, sym_map):
            print(f"  [tagged] {f.relative_to(repo_root)}")
            modified += 1
        else:
            skipped += 1

    print(f"\nDone: {modified} tagged, {skipped} skipped, {total} total")

    # Always refresh index after injection
    update_index(repo_root)


if __name__ == "__main__":
    main()
