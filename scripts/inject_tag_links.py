#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
"""
Inject 'Tag to TAIEX.TW' and 'Tag to biztrends.TW' links into Facebook.Fetch .md files.

Usage:
    python scripts/inject_tag_links.py --all          # backfill all existing .md files
    python scripts/inject_tag_links.py --files f1 f2  # specific files (used by GitHub Action)
    python scripts/inject_tag_links.py --update-index # only refresh index.md badges
"""

import argparse
import csv
import re
import urllib.parse
from pathlib import Path

TAIEX_REPO     = "wenchiehlee-money/TAIEX.TW"
BIZTRENDS_REPO = "wenchiehlee-money/biztrends.TW"
FB_FETCH_REPO  = "wenchiehlee-money/Facebook.Fetch"

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

TAIEX_TAGGED_MARKERS     = ("📌 新增貼文至TAIEX.TW比對", "🔄 已標記", "✅ 已比對")
BIZTRENDS_TAGGED_MARKERS = ("📌 新增貼文至biztrends.TW比對", "🔄 已標記至biztrends.TW", "✅ 已比對至biztrends.TW")

# Keep backward-compat alias
TAGGED_MARKERS = TAIEX_TAGGED_MARKERS

# shields.io badge color per repo — color identifies the repo, emoji identifies the state
# Add new repos here to scale to 3, 4, 5+ repos
SHIELD_COLORS: dict[str, str] = {
    "TAIEX.TW":     "lightgreen",
    "biztrends.TW": "yellow",
}

_EMOJI_ENC = {
    "📌": "%F0%9F%93%8C",
    "🔄": "%F0%9F%94%84",
    "✅": "%E2%9C%85",
}

def make_shield(repo_label: str, status: str) -> str:
    """Return a shields.io badge markdown string, or '' if no status."""
    if not status:
        return ""
    emoji_enc = _EMOJI_ENC.get(status, "")
    if not emoji_enc:
        return ""
    color = SHIELD_COLORS.get(repo_label, "lightgrey")
    return f"![{repo_label}](https://img.shields.io/badge/-{emoji_enc}-{color})"


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
                alias = col[:-2].upper()
                if alias in _CONCEPT_OVERRIDES:
                    mapping.setdefault(alias, _CONCEPT_OVERRIDES[alias])
                elif alias in mapping:
                    pass
                else:
                    mapping.setdefault(alias, alias)

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
    q_match = re.search(r'[Qq]([1-4])', filename)
    year_match = re.search(r'(\d{4})', filename)
    if q_match and year_match:
        return f"{year_match.group(1)} Q{q_match.group(1)}"
    return ""


def build_issue_url(symbol: str, rel_path: str, period: str, repo: str) -> str:
    title = f"{symbol} {period} 財報標記".strip()
    params = {
        "template": "earnings_tag.yml",
        "title":    title,
        "symbol":   symbol,
        "file_path": rel_path,
        "period":   period,
    }
    qs = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return f"https://github.com/{repo}/issues/new?{qs}"


def inject_file(md_path: Path, repo_root: Path, sym_map: dict[str, str]) -> bool:
    """Append TAIEX.TW tag link to .md file. Returns True if file was modified."""
    content = md_path.read_text(encoding="utf-8")

    if any(m in content for m in TAIEX_TAGGED_MARKERS):
        return False

    rel_path = md_path.relative_to(repo_root).as_posix()
    stem     = md_path.stem

    symbol = extract_symbol(stem, sym_map)
    if not symbol:
        return False

    period    = extract_period(stem)
    issue_url = build_issue_url(symbol, rel_path, period, TAIEX_REPO)

    tag_section = (
        "\n\n---\n"
        f"[📌 新增貼文至TAIEX.TW比對]({issue_url})\n"
    )
    md_path.write_text(content + tag_section, encoding="utf-8")
    return True


def inject_file_biztrends(md_path: Path, repo_root: Path, sym_map: dict[str, str]) -> bool:
    """Append biztrends.TW tag link to .md file. Returns True if file was modified."""
    content = md_path.read_text(encoding="utf-8")

    if any(m in content for m in BIZTRENDS_TAGGED_MARKERS):
        return False

    rel_path = md_path.relative_to(repo_root).as_posix()
    stem     = md_path.stem

    symbol = extract_symbol(stem, sym_map)
    if not symbol:
        return False

    period    = extract_period(stem)
    issue_url = build_issue_url(symbol, rel_path, period, BIZTRENDS_REPO)

    tag_section = (
        "\n\n---\n"
        f"[📌 新增貼文至biztrends.TW比對]({issue_url})\n"
    )
    md_path.write_text(content + tag_section, encoding="utf-8")
    return True


def get_badge_status(md_path: Path) -> str:
    """Return TAIEX.TW badge status: ✅ / 🔄 / 📌 / ''"""
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


def get_biztrends_badge_status(md_path: Path) -> str:
    """Return biztrends.TW badge status: ✅ / 🔄 / 📌 / ''"""
    try:
        content = md_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    if "✅ 已比對至biztrends.TW" in content:
        return "✅"
    if "🔄 已標記至biztrends.TW" in content:
        return "🔄"
    if "📌 新增貼文至biztrends.TW比對" in content:
        return "📌"
    return ""


def update_index(repo_root: Path) -> int:
    """Scan all data/**/index.md files and prefix each list item with shields.io badges.

    Format (colored shields.io badges before date, one per repo):
      - `YYYY-MM-DD` [title](file.md)                                        → neither tagged
      - ![TAIEX.TW](…lightgreen…) `YYYY-MM-DD` [title](file.md)             → TAIEX only
      - ![TAIEX.TW](…) ![biztrends.TW](…yellow…) `YYYY-MM-DD` [title](link) → both

    Returns number of index files updated.
    """
    updated = 0
    # Match list items — strip badges before OR after date (handles old and new formats)
    item_re = re.compile(
        r'^- (?:(?:!\[[^\]]*\]\([^)]*\)|[✅🔄📌])\s+)*(`\d{4}-\d{2}-\d{2}` )(?:[✅🔄📌]\s+)?(\[.*?\]\(([^)]+\.md)\))(.*)$'
    )

    for index_path in sorted(repo_root.glob("data/**/index.md")):
        page_dir = index_path.parent
        lines    = index_path.read_text(encoding="utf-8").splitlines(keepends=True)
        new_lines = []
        changed   = False

        for line in lines:
            m = item_re.match(line.rstrip("\n"))
            if m:
                date_part, link_part, md_filename, rest = m.groups()
                md_file = page_dir / md_filename
                taiex_status     = get_badge_status(md_file) if md_file.exists() else ""
                biztrends_status = get_biztrends_badge_status(md_file) if md_file.exists() else ""
                # Only show 🔄 / ✅ — 📌 is injected automatically and would appear on
                # every post, making the index noisy. It lives in the post file as an action button.
                shields = " ".join(filter(None, [
                    make_shield("TAIEX.TW",     taiex_status     if taiex_status     in ("🔄", "✅") else ""),
                    make_shield("biztrends.TW", biztrends_status if biztrends_status in ("🔄", "✅") else ""),
                ]))
                badge_str = f"{shields} " if shields else ""
                new_line = f"- {badge_str}{date_part}{link_part}{rest}\n"
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
    parser = argparse.ArgumentParser(description="Inject TAIEX.TW and biztrends.TW tag links into .md files")
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
        files = [f for f in files if f.name != "index.md"]
    else:
        files = [Path(f).resolve() for f in args.files]

    total = modified = biz_modified = skipped = 0
    for f in files:
        total += 1
        if not f.exists():
            print(f"  [skip] not found: {f}")
            skipped += 1
            continue
        tagged     = inject_file(f, repo_root, sym_map)
        biz_tagged = inject_file_biztrends(f, repo_root, sym_map)
        if tagged:
            print(f"  [TAIEX tagged]     {f.relative_to(repo_root)}")
            modified += 1
        if biz_tagged:
            print(f"  [biztrends tagged] {f.relative_to(repo_root)}")
            biz_modified += 1
        if not tagged and not biz_tagged:
            skipped += 1

    print(f"\nDone: TAIEX {modified} tagged, biztrends {biz_modified} tagged, {skipped} skipped, {total} total")

    # Always refresh index after injection
    update_index(repo_root)


if __name__ == "__main__":
    main()
