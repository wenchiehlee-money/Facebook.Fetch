#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract Facebook cookie and update GitHub secret FB_COOKIE.

Chrome 127+ App-Bound Encryption (ABE) prevents external tools from reading
session cookies directly.  This script uses the chrome-devtools MCP server
(if available) to navigate Facebook and capture cookies from network requests.

Flow:
  1. Navigate to facebook.com via chrome-devtools MCP
  2. If not logged in, prompt user to log in (fills email automatically)
  3. Reload and extract full cookie string from request headers
  4. Update GitHub secret FB_COOKIE
  5. Trigger daily_fetch.yml workflow
"""

from __future__ import annotations

import io
import sys

if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import json
import os
import subprocess
import time
import webbrowser
from pathlib import Path


FACEBOOK_URL = "https://www.facebook.com"
DOWNLOADS_DIR = Path.home() / "Downloads"
WATCH_TIMEOUT_SECONDS = 180
FB_EMAIL = "wjlee@csie.nctu.edu.tw"


# ---------------------------------------------------------------------------
# Method 1: chrome-devtools MCP (fully automatic after login)
# ---------------------------------------------------------------------------

def _get_cookies_via_mcp() -> str | None:
    """
    Use the chrome-devtools MCP server to capture Facebook cookies from
    network request headers (includes HttpOnly cookies like c_user and xs).

    Returns the raw cookie header string, or None if MCP is not available.
    This function is called from within a Claude Code session that has the
    chrome-devtools MCP enabled.
    """
    # This method only works when run inside a Claude Code / MCP session.
    # When invoked standalone (python update_fb_cookie.py), MCP is not available.
    # The actual MCP logic lives in the Claude Code conversation.
    print("  [MCP] 此方法需在 Claude Code 對話中透過 MCP 工具執行。")
    print("  [MCP] 若您看到此訊息，請在 Claude Code 中執行以下流程：")
    print("        1. 導航到 https://www.facebook.com")
    print("        2. 重新載入頁面")
    print("        3. 從 reqid 的 request headers 取得 cookie 欄位")
    return None


# ---------------------------------------------------------------------------
# Method 2: browser_cookie3 (Chrome < 127 only)
# ---------------------------------------------------------------------------

def _get_cookies_browser_cookie3() -> dict[str, str] | None:
    try:
        import browser_cookie3  # type: ignore
        cj = browser_cookie3.chrome(domain_name=".facebook.com")
        return {c.name: c.value for c in cj}
    except ImportError:
        return None
    except Exception as e:
        print(f"  [browser_cookie3] 失敗: {e}")
        return None


# ---------------------------------------------------------------------------
# Method 3: Cookie-Editor Chrome extension JSON export
# ---------------------------------------------------------------------------

EXTENSION_INSTRUCTIONS = """
══════════════════════════════════════════════════════════════════════
  Chrome 148 的 App-Bound Encryption 讓外部程式無法直接讀取 cookie。
  備用方案：Cookie-Editor 擴充套件（2 次點擊）

  【首次設定 — 安裝擴充套件】（只需做一次）
  Chrome 正在開啟 Cookie-Editor 安裝頁面...
  點「加到 Chrome」安裝

  【每次更新 cookie 的步驟】（共 2 步）
  Step 1. 在 Chrome 確認已登入 Facebook（https://www.facebook.com）
  Step 2. 點工具列的 Cookie-Editor 圖示（餅乾圖案）
          → 點右上角的「Export」按鈕（向上箭頭）
          → 選「Export as JSON」
          → 儲存到 Downloads 資料夾（使用預設檔名即可）

  腳本正在自動偵測 Downloads 資料夾中的匯出檔案...
  （最多等待 180 秒，匯出後自動繼續）
══════════════════════════════════════════════════════════════════════
"""

COOKIE_EDITOR_STORE_URL = "https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm"


def _parse_cookie_editor_json(path: Path) -> dict[str, str] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(data, list):
        return None
    if not data or "name" not in data[0] or "value" not in data[0]:
        return None
    fb_cookies = {}
    for c in data:
        domain = c.get("domain", "")
        if "facebook.com" in domain:
            fb_cookies[c["name"]] = c["value"]
    return fb_cookies if fb_cookies else None


def _find_recent_cookie_export(before_time: float) -> dict[str, str] | None:
    if not DOWNLOADS_DIR.exists():
        return None
    for f in DOWNLOADS_DIR.glob("*.json"):
        try:
            if f.stat().st_mtime > before_time:
                result = _parse_cookie_editor_json(f)
                if result and ("c_user" in result or "xs" in result):
                    print(f"  找到匯出檔案: {f.name}")
                    return result
        except Exception:
            continue
    return None


def _get_cookies_extension_export() -> dict[str, str] | None:
    print(EXTENSION_INSTRUCTIONS)
    start_time = time.time()

    recent = _find_recent_cookie_export(start_time - 300)
    if recent and "c_user" in recent and "xs" in recent:
        print("  偵測到最近的匯出檔案，直接使用。")
        return recent

    webbrowser.open(FACEBOOK_URL)
    time.sleep(1)
    webbrowser.open(COOKIE_EDITOR_STORE_URL)

    print(f"  等待 Downloads 資料夾中出現 JSON 匯出檔案（最多 {WATCH_TIMEOUT_SECONDS} 秒）...")
    print("  （匯出後按 Enter 可跳過倒數）")

    import threading
    result_holder: list[dict[str, str] | None] = [None]
    stop_event = threading.Event()

    def watcher():
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
    return result_holder[0]


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def get_facebook_cookies() -> str:
    print("嘗試自動方法: browser_cookie3 (Chrome <127)...")
    result = _get_cookies_browser_cookie3()
    if result and "c_user" in result and "xs" in result:
        print(f"  → 成功取得 {len(result)} 個 cookie")
        return "; ".join(f"{k}={v}" for k, v in result.items())
    elif result is None:
        print("  → 不可用")
    else:
        print(f"  → 取得 {len(result)} 個 cookie，但缺少 c_user/xs（Chrome 148 ABE 限制）")

    # Fallback: Cookie-Editor extension export
    result_dict = _get_cookies_extension_export()
    if result_dict is None:
        print("\n未偵測到匯出檔案。請確認 Cookie-Editor 已安裝並完成匯出。")
        return ""
    if "c_user" not in result_dict or "xs" not in result_dict:
        print(f"警告：匯出的 cookie 有 {len(result_dict)} 個，但缺少 c_user 或 xs。")
        confirm = input("仍要繼續更新 GitHub secret？(y/N): ").strip().lower()
        if confirm != "y":
            return ""

    print(f"Cookie 欄位數: {len(result_dict)}，c_user={'✓' if 'c_user' in result_dict else '✗'}，xs={'✓' if 'xs' in result_dict else '✗'}")
    return "; ".join(f"{k}={v}" for k, v in result_dict.items())


# ---------------------------------------------------------------------------
# Accept cookie string directly (used by MCP-assisted flow)
# ---------------------------------------------------------------------------

def update_from_cookie_string(cookie: str) -> int:
    """Update GitHub secret and trigger workflow from a raw cookie string."""
    if not cookie:
        return 1
    keys = {k.split("=")[0].strip() for k in cookie.split(";")}
    has_c_user = "c_user" in keys
    has_xs = "xs" in keys
    print(f"Cookie 欄位數: {len(keys)}，c_user={'✓' if has_c_user else '✗'}，xs={'✓' if has_xs else '✗'}")
    print(f"\nCookie 預覽: {cookie[:80]}...\n")
    if not update_github_secret(cookie):
        return 1
    trigger_workflow()
    return 0


# ---------------------------------------------------------------------------
# GitHub secret & workflow
# ---------------------------------------------------------------------------

def update_github_secret(cookie_value: str) -> bool:
    result = subprocess.run(
        ["gh", "secret", "set", "FB_COOKIE", "--body", cookie_value],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print("GitHub secret FB_COOKIE 已更新")
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


def main() -> int:
    cookie = get_facebook_cookies()
    if not cookie:
        return 1
    print(f"\nCookie 預覽: {cookie[:80]}...\n")
    if not update_github_secret(cookie):
        return 1
    trigger_workflow()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
