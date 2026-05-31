#!/usr/bin/env python3
"""Append today's fetch results from all latest_fetch_summary.json into raw_facebook_fetch.csv."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

CSV_PATH = Path("raw_facebook_fetch.csv")
DATA_DIR = Path("data")
FIELDNAMES = ["fetched_at_cst", "page_name", "page_url", "new_post_count", "total_post_count", "follower_count"]


def load_existing_keys() -> set[tuple[str, str]]:
    """Return (fetched_at_cst, page_name) pairs already in the CSV."""
    if not CSV_PATH.exists():
        return set()
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        return {(row["fetched_at_cst"], row["page_name"]) for row in csv.DictReader(f)}


def count_posts(page_dir: Path) -> int:
    return len([f for f in page_dir.glob("*.md") if f.name != "index.md"])


def to_cst(utc_str: str) -> str:
    dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
    cst = dt.astimezone(timezone(timedelta(hours=8)))
    return cst.strftime("%Y-%m-%d %H:%M CST")


def main() -> None:
    # We will now overwrite the CSV to ensure only the latest state per page is kept.
    # This prevents "Data Bloat" and fixes the "duplicated" issue.
    page_data: dict[str, dict] = {}

    for summary_path in sorted(DATA_DIR.glob("*/latest_fetch_summary.json")):
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except Exception:
            continue

        page_name = summary.get("page", {}).get("title") or summary_path.parent.name
        fetched_at_cst = to_cst(summary.get("fetched_at_utc", ""))
        
        row = {
            "fetched_at_cst": fetched_at_cst,
            "page_name": page_name,
            "page_url": summary.get("final_url", summary.get("requested_url", "")),
            "new_post_count": summary.get("new_post_count", 0),
            "total_post_count": count_posts(summary_path.parent),
            "follower_count": summary.get("page", {}).get("follower_count", ""),
        }
        
        # If we have multiple entries for the same page_name (shouldn't happen with */ glob, but safe)
        # keep the one with the latest timestamp.
        if page_name not in page_data or fetched_at_cst > page_data[page_name]["fetched_at_cst"]:
            page_data[page_name] = row

    if not page_data:
        print("No data found to write.")
        return

    # Sort by page_name for stability
    sorted_rows = [page_data[k] for k in sorted(page_data.keys())]

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(sorted_rows)

    print(f"Updated {CSV_PATH} with {len(sorted_rows)} latest page records (overwritten).")


if __name__ == "__main__":
    main()
