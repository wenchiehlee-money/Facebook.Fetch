#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Single entry point for the daily Facebook fetch pipeline.

This mirrors .github/workflows/daily_fetch.yml step-by-step so that running
this script locally (e.g. via the skill-facebook-fetch skill) produces the
same data/ and README.md state as the scheduled GitHub Actions run. The
workflow itself calls this script — there is exactly one implementation of
the pipeline, not two copies that can drift.

Steps (each can be skipped independently via CLI flags):
  1. reset new_post_count to 0 in every data/*/latest_fetch_summary.json
  2. fetch saved lists (requires FB_COOKIE)
  3. fetch every page in data/fetch_urls.txt (requires FB_COOKIE, FB_DTSG)
  4. rebuild README.md
  5. update raw_facebook_fetch.csv
  6. detect total new posts across all summary files
  7. (optional, --commit) git add/commit/push
  8. (optional, --trigger-sync) gh workflow run sync-to-biztrends.yml
  9. (optional, --create-issue) open a GitHub issue if any page hit exit code 2
     (expired FB_COOKIE)
"""
from __future__ import annotations

import argparse
import glob
import io
import json
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[3]
FETCH_URLS_FILE = REPO_ROOT / "data" / "fetch_urls.txt"
SAVED_LISTS = [
    "https://www.facebook.com/saved/?list_id=10222174769398438&referrer=SAVE_DASHBOARD_NAVIGATION_PANEL",
]


def load_env_value(name: str) -> str:
    import os

    if os.environ.get(name):
        return os.environ[name]
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith(f"{name}="):
                return line[len(name) + 1 :]
    return ""


def reset_new_post_counts() -> None:
    for f in glob.glob(str(REPO_ROOT / "data" / "*" / "latest_fetch_summary.json")):
        payload = json.loads(Path(f).read_text(encoding="utf-8"))
        payload["new_post_count"] = 0
        Path(f).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Reset new_post_count in all summary files")


def fetch_saved_lists(cookie: str) -> None:
    for url in SAVED_LISTS:
        print(f"::group::Fetching saved list {url}")
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "fetch_saved_list.py"), url, "--cookie", cookie],
            cwd=REPO_ROOT,
        )
        if result.returncode != 0:
            print(f"Warning: Failed to fetch saved list {url}")
        print("::endgroup::")


def run_daily_fetch(cookie: str, fb_dtsg: str, months_back: int) -> bool:
    """Returns True if any page reported an expired-cookie exit code (2)."""
    auth_failed = False
    if not FETCH_URLS_FILE.exists():
        print(f"No such file: {FETCH_URLS_FILE}", file=sys.stderr)
        return auth_failed

    for line in FETCH_URLS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.rstrip("\n")
        if not line.strip() or line.strip().startswith("#"):
            continue
        parts = line.split("\t")
        url = parts[0].strip()
        page_name = parts[1].strip() if len(parts) > 1 and parts[1].strip() else None
        if not url:
            continue

        print(f"::group::Fetching {url}")
        if months_back != 0:
            count_arg = "50"
            extra_args = ["--months-back", str(months_back)]
        else:
            count_arg = "20"
            extra_args = []

        cmd = [
            sys.executable, str(REPO_ROOT / "fetch_facebook_posts.py"), url,
            "--count", count_arg,
            "--cookie", cookie,
            "--fb-dtsg", fb_dtsg,
        ]
        if page_name:
            cmd += ["--page-name", page_name]
        cmd += extra_args

        result = subprocess.run(cmd, cwd=REPO_ROOT)
        if result.returncode == 2:
            auth_failed = True
            print(f"::warning::Cookie expired for {url} (exit 2)")
        elif result.returncode != 0:
            print(f"Warning: Failed to fetch {url} (exit {result.returncode})")
        print("::endgroup::")

    return auth_failed


def rebuild_readme() -> None:
    subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "rebuild_readme.py")], cwd=REPO_ROOT, check=False)


def update_fetch_csv() -> None:
    subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "update_fetch_csv.py")], cwd=REPO_ROOT, check=False)


def detect_new_posts() -> int:
    total = 0
    for f in glob.glob(str(REPO_ROOT / "data" / "*" / "latest_fetch_summary.json")):
        payload = json.loads(Path(f).read_text(encoding="utf-8"))
        total += payload.get("new_post_count", 0)
    print(f"Total new posts: {total}")
    return total


def commit_and_push(new_post_count: int) -> None:
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=REPO_ROOT, check=False)
    subprocess.run(
        ["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"],
        cwd=REPO_ROOT, check=False,
    )
    subprocess.run(["git", "add", "README.md", "raw_facebook_fetch.csv"], cwd=REPO_ROOT, check=False)
    if new_post_count != 0:
        subprocess.run(["git", "add", "data/"], cwd=REPO_ROOT, check=False)

    staged = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT)
    if staged.returncode == 0:
        print("Nothing staged, skipping commit")
        return

    if new_post_count != 0:
        message = f"Daily fetch: added {new_post_count} new posts"
        detail = "Automated fetch from Facebook pages."
    else:
        message = "chore: refresh facebook fetch metadata"
        detail = None

    commit_cmd = ["git", "commit", "-m", message]
    if detail:
        commit_cmd += ["-m", detail]
    subprocess.run(commit_cmd, cwd=REPO_ROOT, check=True)
    subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=REPO_ROOT, check=True)


def trigger_sync() -> None:
    result = subprocess.run(["gh", "workflow", "run", "sync-to-biztrends.yml"], cwd=REPO_ROOT)
    if result.returncode != 0:
        print("Warning: failed to trigger sync-to-biztrends.yml")


def create_expired_cookie_issue() -> None:
    existing = subprocess.run(
        ["gh", "issue", "list", "--state", "open", "--search", "FB_COOKIE expired",
         "--json", "number", "--jq", ".[0].number"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if existing.stdout.strip():
        return
    subprocess.run(
        [
            "gh", "issue", "create",
            "--title", "FB_COOKIE expired — daily fetch blocked",
            "--body",
            "The GitHub secret `FB_COOKIE` has expired (Facebook error 1357001: "
            "登入以繼續).\n\nRun `python skills/skill-facebook-fetch/scripts/update_fb_cookie.py` "
            "locally to refresh the cookie and re-trigger the workflow.",
        ],
        cwd=REPO_ROOT, check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--months-back", type=int, default=0,
                         help="回溯月數（0 = 僅抓最新；1 = 抓近 30 天，用於補資料）")
    parser.add_argument("--cookie", default=None, help="省略則從環境變數/.env 讀取 FB_COOKIE")
    parser.add_argument("--fb-dtsg", default=None, help="省略則從環境變數/.env 讀取 FB_DTSG")
    parser.add_argument("--commit", action="store_true", help="抓取後 git add/commit/push（預設關閉）")
    parser.add_argument("--trigger-sync", action="store_true",
                         help="有新貼文時觸發 sync-to-biztrends.yml（預設關閉，需要 gh CLI）")
    parser.add_argument("--create-issue", action="store_true",
                         help="cookie 過期時開 GitHub issue（預設關閉，需要 gh CLI）")
    parser.add_argument("--skip-saved-lists", action="store_true", help="跳過珍藏清單抓取")
    args = parser.parse_args()

    cookie = args.cookie or load_env_value("FB_COOKIE")
    fb_dtsg = args.fb_dtsg or load_env_value("FB_DTSG")
    if not cookie:
        print("錯誤：請提供 --cookie 或設定環境變數 FB_COOKIE", file=sys.stderr)
        return 1

    reset_new_post_counts()

    if not args.skip_saved_lists:
        fetch_saved_lists(cookie)

    auth_failed = run_daily_fetch(cookie, fb_dtsg, args.months_back)

    rebuild_readme()
    update_fetch_csv()
    new_post_count = detect_new_posts()

    if args.commit:
        commit_and_push(new_post_count)

    if args.trigger_sync and new_post_count != 0:
        trigger_sync()

    if auth_failed:
        if args.create_issue:
            create_expired_cookie_issue()
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
