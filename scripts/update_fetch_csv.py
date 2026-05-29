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
    existing = load_existing_keys()
    new_rows: list[dict] = []

    for summary_path in sorted(DATA_DIR.glob("*/latest_fetch_summary.json")):
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except Exception:
            continue

        page_name = summary.get("page", {}).get("title") or summary_path.parent.name
        fetched_at_cst = to_cst(summary.get("fetched_at_utc", ""))
        key = (fetched_at_cst, page_name)

        if key in existing:
            continue

        new_rows.append({
            "fetched_at_cst": fetched_at_cst,
            "page_name": page_name,
            "page_url": summary.get("final_url", summary.get("requested_url", "")),
            "new_post_count": summary.get("new_post_count", 0),
            "total_post_count": count_posts(summary_path.parent),
            "follower_count": summary.get("page", {}).get("follower_count", ""),
        })

    if not new_rows:
        print("No new rows to append.")
        return

    write_header = not CSV_PATH.exists()
    with CSV_PATH.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerows(new_rows)

    print(f"Appended {len(new_rows)} rows to {CSV_PATH}")


if __name__ == "__main__":
    main()
