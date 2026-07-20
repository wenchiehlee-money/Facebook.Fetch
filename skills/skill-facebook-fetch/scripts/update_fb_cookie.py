#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract Facebook cookie and update GitHub secret FB_COOKIE.

Primary method — Chrome DevTools MCP (must be run from Claude Code):
  Claude Code uses the chrome-devtools MCP server to capture cookies directly
  from live browser network requests.  This bypasses Chrome 127+ App-Bound
  Encryption entirely because the cookie is read from the request header, not
  from the encrypted cookie store.

  When invoked from Claude Code, the flow is:
    1. mcp__chrome-devtools__navigate_page  →  https://www.facebook.com/<page>
    2. mcp__chrome-devtools__list_network_requests  →  find the document GET
    3. mcp__chrome-devtools__get_network_request(reqid=<doc>)
       →  read "cookie" from Request Headers
       →  read fb_dtsg from a POST request URL param (fb_dtsg=...) or body
    4. python tools/update_fb_cookie.py --cookie "..." --fb-dtsg "..."

Fallback — Cookie-Editor Chrome extension JSON export (manual):
  If MCP is unavailable, export cookies manually and place the JSON file in
  the Downloads folder.  The script will detect and import it automatically.

Usage:
  # MCP-assisted (Claude Code provides cookie via --cookie flag):
  python tools/update_fb_cookie.py --cookie "<raw cookie string>" [--fb-dtsg "<token>"]

  # Manual fallback (Cookie-Editor JSON in Downloads):
  python tools/update_fb_cookie.py
"""

from __future__ import annotations

import argparse
import io
import json
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


FACEBOOK_URL = "https://www.facebook.com"
DOWNLOADS_DIR = Path.home() / "Downloads"
WATCH_TIMEOUT_SECONDS = 180
COOKIE_EDITOR_STORE_URL = "https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm"

MCP_INSTRUCTIONS = """
══════════════════════════════════════════════════════════════════════
  此腳本需透過 Claude Code + Chrome DevTools MCP 取得 cookie。

  請在 Claude Code 對話中輸入：
      python tools/update_fb_cookie.py

  Claude 會自動執行以下流程：
    1. 導航至 https://www.facebook.com（若未登入請先登入）
    2. 從 network request headers 取得 cookie 字串
    3. 從 POST 請求取得 fb_dtsg token
    4. 以 --cookie / --fb-dtsg 參數呼叫本腳本更新 GitHub Secret
    5. 觸發 daily_fetch workflow

  若不在 Claude Code 環境中，請改用 Cookie-Editor 備用方案（見下方）。
══════════════════════════════════════════════════════════════════════
"""

EXTENSION_INSTRUCTIONS = """
══════════════════════════════════════════════════════════════════════
  備用方案：Cookie-Editor 擴充套件

  【首次設定】（只需做一次）
  Chrome 正在開啟 Cookie-Editor 安裝頁面...
  點「加到 Chrome」安裝

  【每次更新 cookie 的步驟】
  Step 1. 在 Chrome 確認已登入 Facebook（https://www.facebook.com）
  Step 2. 點工具列的 Cookie-Editor 圖示（餅乾圖案）
          → 點右上角的「Export」按鈕（向上箭頭）
          → 選「Export as JSON」
          → 儲存到 Downloads 資料夾（使用預設檔名即可）

  腳本正在自動偵測 Downloads 資料夾中的匯出檔案...
  （最多等待 180 秒，匯出後自動繼續）
══════════════════════════════════════════════════════════════════════
"""


# ---------------------------------------------------------------------------
# Cookie-Editor fallback
# ---------------------------------------------------------------------------

def _parse_cookie_editor_json(path: Path) -> dict[str, str] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(data, list) or not data:
        return None
    if "name" not in data[0] or "value" not in data[0]:
        return None
    return {
        c["name"]: c["value"]
        for c in data
        if "facebook.com" in c.get("domain", "")
    } or None


def _find_recent_cookie_export(after_time: float) -> dict[str, str] | None:
    if not DOWNLOADS_DIR.exists():
        return None
    for f in DOWNLOADS_DIR.glob("*.json"):
        try:
            if f.stat().st_mtime > after_time:
                result = _parse_cookie_editor_json(f)
                if result and ("c_user" in result or "xs" in result):
                    print(f"  找到匯出檔案: {f.name}")
                    return result
        except Exception:
            continue
    return None


def _get_cookies_via_extension_export() -> str:
    print(EXTENSION_INSTRUCTIONS)
    start_time = time.time()

    recent = _find_recent_cookie_export(start_time - 300)
    if recent and "c_user" in recent and "xs" in recent:
        print("  偵測到最近的匯出檔案，直接使用。")
        return "; ".join(f"{k}={v}" for k, v in recent.items())

    webbrowser.open(FACEBOOK_URL)
    time.sleep(1)
    webbrowser.open(COOKIE_EDITOR_STORE_URL)

    print(f"  等待 Downloads 資料夾出現 JSON 匯出檔案（最多 {WATCH_TIMEOUT_SECONDS} 秒）...")
    print("  （匯出後按 Enter 可跳過倒數）")

    import threading
    result_holder: list[dict[str, str] | None] = [None]
    stop_event = threading.Event()

    def watcher() -> None:
        deadline = time.time() + WATCH_TIMEOUT_SECONDS
        while time.time() < deadline and not stop_event.is_set():
            found = _find_recent_cookie_export(start_time)
            if found:
                result_holder[0] = found
                stop_event.set()
                return
            time.sleep(1)

    t = threading.Thread(target=watcher, daemon=True)
    t.start()
    try:
        input()
        stop_event.set()
    except (EOFError, KeyboardInterrupt):
        stop_event.set()
    t.join(timeout=2)

    if result_holder[0] is None:
        result_holder[0] = _find_recent_cookie_export(start_time)

    result_dict = result_holder[0]
    if not result_dict:
        print("\n未偵測到匯出檔案。請確認 Cookie-Editor 已安裝並完成匯出。")
        return ""
    if "c_user" not in result_dict or "xs" not in result_dict:
        print(f"警告：匯出的 cookie 有 {len(result_dict)} 個，但缺少 c_user 或 xs。")
        confirm = input("仍要繼續更新 GitHub secret？(y/N): ").strip().lower()
        if confirm != "y":
            return ""

    return "; ".join(f"{k}={v}" for k, v in result_dict.items())


# ---------------------------------------------------------------------------
# GitHub secret & workflow
# ---------------------------------------------------------------------------

def update_github_secret(name: str, value: str) -> bool:
    result = subprocess.run(
        ["gh", "secret", "set", name, "--body", value],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print(f"GitHub secret {name} 已更新")
        return True
    print(f"更新失敗: {result.stderr.strip()}")
    return False


def trigger_workflow() -> None:
    result = subprocess.run(
        ["gh", "workflow", "run", "daily_fetch.yml"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print("已觸發 daily_fetch workflow，約 1 分鐘後可在 Actions 頁面查看結果")
    else:
        print(f"觸發 workflow 失敗: {result.stderr.strip()}")


def _apply(cookie: str, fb_dtsg: str | None) -> int:
    keys = {k.split("=")[0].strip() for k in cookie.split(";")}
    has_c_user = "c_user" in keys
    has_xs = "xs" in keys
    print(f"Cookie 欄位數: {len(keys)}，c_user={'✓' if has_c_user else '✗'}，xs={'✓' if has_xs else '✗'}")
    print(f"Cookie 預覽: {cookie[:80]}...")
    if not update_github_secret("FB_COOKIE", cookie):
        return 1
    if fb_dtsg:
        print(f"fb_dtsg 預覽: {fb_dtsg[:40]}...")
        if not update_github_secret("FB_DTSG", fb_dtsg):
            return 1
    trigger_workflow()
    return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Update FB_COOKIE GitHub secret")
    parser.add_argument("--cookie", help="Raw cookie string from browser network request (MCP flow)")
    parser.add_argument("--fb-dtsg", dest="fb_dtsg", help="fb_dtsg CSRF token (MCP flow)")
    args = parser.parse_args()

    if args.cookie:
        # MCP flow: cookie provided directly by Claude Code
        return _apply(args.cookie, args.fb_dtsg)

    # No cookie provided — check if running interactively
    print(MCP_INSTRUCTIONS)
    print("備用方案：嘗試 Cookie-Editor 匯出...")
    cookie = _get_cookies_via_extension_export()
    if not cookie:
        return 1
    return _apply(cookie, None)


if __name__ == "__main__":
    raise SystemExit(main())
