#!/usr/bin/env python3
"""Build raw_facebook_fetch.csv from fetched Facebook article markdown files."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

CSV_PATH = Path("raw_facebook_fetch.csv")
DATA_DIR = Path("data")
FIELDNAMES = [
    "process_timestamp",
    "page_name",
    "page_url",
    "new_post_count",
    "total_post_count",
    "follower_count",
    "post_id",
    "title",
    "post_url",
    "creation_time_utc",
    "creation_date",
    "fetched_at_utc",
    "fetched_at_cst",
    "source",
    "attachment_type",
    "attachment_url",
    "markdown_path",
]


def count_posts(page_dir: Path) -> int:
    return len([f for f in page_dir.glob("*.md") if f.name != "index.md"])


def to_cst(utc_str: str) -> str:
    dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
    cst = dt.astimezone(timezone(timedelta(hours=8)))
    return cst.strftime("%Y-%m-%d %H:%M CST")


def parse_cst(value: str) -> datetime | None:
    try:
        return datetime.strptime(value, "%Y-%m-%d %H:%M CST").replace(tzinfo=timezone(timedelta(hours=8)))
    except ValueError:
        return None


def load_existing_page_rows() -> dict[str, dict[str, str]]:
    if not CSV_PATH.exists():
        return {}
    latest: dict[str, dict[str, str]] = {}
    try:
        with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                page_name = row.get("page_name", "")
                if not page_name:
                    continue
                existing = latest.get(page_name)
                row_ts = parse_cst(row.get("process_timestamp", ""))
                existing_ts = parse_cst((existing or {}).get("process_timestamp", ""))
                if existing is None or (row_ts and (existing_ts is None or row_ts > existing_ts)):
                    latest[page_name] = {
                        "process_timestamp": row.get("process_timestamp", ""),
                        "page_url": row.get("page_url", ""),
                        "new_post_count": row.get("new_post_count", ""),
                        "follower_count": row.get("follower_count", ""),
                    }
    except (OSError, csv.Error):
        return {}
    return latest


def merge_newest_page_fields(
    page_row: dict[str, str | int], existing_row: dict[str, str] | None
) -> dict[str, str | int]:
    if not existing_row:
        return page_row
    current_ts = parse_cst(str(page_row.get("process_timestamp", "")))
    existing_ts = parse_cst(existing_row.get("process_timestamp", ""))
    if not existing_ts or (current_ts and current_ts >= existing_ts):
        return page_row

    merged = dict(page_row)
    for key in ("process_timestamp", "page_url", "new_post_count", "follower_count"):
        if existing_row.get(key):
            merged[key] = existing_row[key]
    return merged


def parse_markdown_metadata(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    if not text.startswith("---\n"):
        return {}

    metadata: dict[str, str] = {}
    for line in text.splitlines()[1:]:
        if line == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata


def article_rows(page_dir: Path, page_row: dict[str, str | int]) -> list[dict[str, str | int]]:
    rows: list[dict[str, str | int]] = []
    for markdown_path in sorted(page_dir.glob("*.md")):
        if markdown_path.name == "index.md":
            continue
        metadata = parse_markdown_metadata(markdown_path)
        creation_time_utc = metadata.get("creation_time_utc", "")
        fetched_at_utc = metadata.get("fetched_at_utc", "")
        row = {
            **page_row,
            "post_id": metadata.get("post_id", ""),
            "title": metadata.get("title", ""),
            "post_url": metadata.get("post_url", ""),
            "creation_time_utc": creation_time_utc,
            "creation_date": creation_time_utc[:10] if creation_time_utc else "",
            "fetched_at_utc": fetched_at_utc,
            "fetched_at_cst": to_cst(fetched_at_utc) if fetched_at_utc else "",
            "source": metadata.get("source", ""),
            "attachment_type": metadata.get("attachment_type", ""),
            "attachment_url": metadata.get("attachment_url", ""),
            "markdown_path": markdown_path.as_posix(),
        }
        rows.append(row)
    return rows


def main() -> None:
    rows: list[dict[str, str | int]] = []
    existing_page_rows = load_existing_page_rows()
    for summary_path in sorted(DATA_DIR.glob("*/latest_fetch_summary.json")):
        try:
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        page_dir = summary_path.parent
        page_name = summary.get("page", {}).get("title") or page_dir.name
        process_timestamp = to_cst(summary.get("fetched_at_utc", ""))
        page_row = {
            "process_timestamp": process_timestamp,
            "page_name": page_name,
            "page_url": summary.get("final_url", summary.get("requested_url", "")),
            "new_post_count": summary.get("new_post_count", 0),
            "total_post_count": count_posts(page_dir),
            "follower_count": summary.get("page", {}).get("follower_count", ""),
        }
        page_row = merge_newest_page_fields(page_row, existing_page_rows.get(page_name))
        rows.extend(article_rows(page_dir, page_row))
    if not rows:
        print("No data found to write.")
        return
    sorted_rows = sorted(
        rows,
        key=lambda row: (
            str(row.get("page_name", "")),
            str(row.get("creation_time_utc", "")),
            str(row.get("post_id", "")),
        ),
        reverse=True,
    )
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(sorted_rows)
    print(f"Updated {CSV_PATH} with {len(sorted_rows)} article records (overwritten).")


if __name__ == "__main__":
    main()
