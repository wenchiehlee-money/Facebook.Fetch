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
    4. python skills/skill-facebook-fetch/scripts/update_fb_cookie.py --cookie "..." --fb-dtsg "..."

Secondary method — Chrome CDP WebSocket (Automatic local run):
  If Chrome is started with debugging enabled (port 9222), the script will
  automatically connect to it via WebSocket, retrieve cookies, evaluate fb_dtsg
  CSRF token, update GitHub secrets, and trigger the fetch workflow.

Fallback — Cookie-Editor Chrome extension JSON export (manual):
  If both automatic methods fail, export cookies manually and place the JSON
  file in the Downloads folder. The script will detect and import it automatically.

Usage:
  # Fully Automatic (requires Chrome running with --remote-debugging-port=9222):
  python skills/skill-facebook-fetch/scripts/update_fb_cookie.py

  # MCP-assisted / CLI argument:
  python skills/skill-facebook-fetch/scripts/update_fb_cookie.py --cookie "<raw cookie>" [--fb-dtsg "<token>"]
"""

from __future__ import annotations

import argparse
import io
import json
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path

if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


FACEBOOK_URL = "https://www.facebook.com"
DOWNLOADS_DIR = Path.home() / "Downloads"
WATCH_TIMEOUT_SECONDS = 180
COOKIE_EDITOR_STORE_URL = "https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm"

CDP_INSTRUCTIONS = """
══════════════════════════════════════════════════════════════════════
  正在偵測本機 Chrome 遠端偵錯埠 (localhost:9222)...
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
# CDP WebSocket automatic extraction
# ---------------------------------------------------------------------------

def try_auto_extract_via_cdp() -> tuple[str, str] | None:
    """Attempt to extract cookies and fb_dtsg via local Chrome CDP port 9222."""
    print(CDP_INSTRUCTIONS.strip())
    try:
        response = urllib.request.urlopen("http://localhost:9222/json", timeout=2)
        pages = json.loads(response.read().decode('utf-8'))
    except Exception:
        print("  ❌ 無法連線至 localhost:9222 (偵錯模式未開啟或尚無網頁)")
        return None

    fb_page = None
    for p in pages:
        if "facebook.com" in p.get("url", ""):
            fb_page = p
            break
    if not fb_page and pages:
        fb_page = pages[0]

    if not fb_page:
        print("  ❌ Chrome 中沒有開啟任何分頁")
        return None

    ws_url = fb_page.get("webSocketDebuggerUrl")
    if not ws_url:
        print("  ❌ 分頁沒有 webSocketDebuggerUrl 資訊")
        return None

    print(f"  偵測到分頁: {fb_page.get('title', 'Unknown')[:30]} ({fb_page.get('url')[:40]}...)")
    print("  正在嘗試透過 WebSocket 擷取憑證資訊...")
    
    try:
        import websocket
        ws = websocket.create_connection(ws_url, suppress_origin=True, timeout=5)
    except Exception as e:
        print(f"  ❌ WebSocket 連線失敗: {e}")
        return None

    try:
        # 1. Get cookies
        ws.send(json.dumps({
            "id": 1,
            "method": "Network.getCookies",
            "params": {
                "urls": ["https://www.facebook.com"]
            }
        }))
        
        cookies = []
        for _ in range(10):
            try:
                resp = json.loads(ws.recv())
                if resp.get("id") == 1:
                    cookies = resp.get("result", {}).get("cookies", [])
                    break
            except Exception:
                break

        cookie_keys = {c["name"] for c in cookies}
        if "c_user" not in cookie_keys or "xs" not in cookie_keys:
            print("  ❌ 警告：未取得關鍵 c_user 或 xs Cookie，請確認已登入 Facebook")
            ws.close()
            return None

        cookie_str = "; ".join(f"{c['name']}={c['value']}" for c in cookies)

        # 2. Get fb_dtsg
        ws.send(json.dumps({
            "id": 2,
            "method": "Runtime.evaluate",
            "params": {
                "expression": '(() => { try { return require("DTSGInitialData").token; } catch(e) { try { return document.getElementsByName("fb_dtsg")[0].value; } catch(e2) { return ""; } } })()',
                "returnByValue": True
            }
        }))

        fb_dtsg = ""
        for _ in range(10):
            try:
                resp = json.loads(ws.recv())
                if resp.get("id") == 2:
                    fb_dtsg = resp.get("result", {}).get("result", {}).get("value", "")
                    break
            except Exception:
                break

        ws.close()
        print("  ✅ 成功自動擷取 Cookie 與 fb_dtsg！")
        return cookie_str, fb_dtsg
    except Exception as e:
        print(f"  ❌ 擷取過程中發生錯誤: {e}")
        try:
            ws.close()
        except Exception:
            pass
        return None


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
        print(f"  GitHub secret {name} 已更新")
        return True
    print(f"  更新失敗: {result.stderr.strip()}")
    return False


def trigger_workflow() -> None:
    result = subprocess.run(
        ["gh", "workflow", "run", "daily_fetch.yml"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print("  已觸發 daily_fetch workflow，約 1 分鐘後可在 Actions 頁面查看結果")
    else:
        print(f"  觸發 workflow 失敗: {result.stderr.strip()}")


def _apply(cookie: str, fb_dtsg: str | None) -> int:
    keys = {k.split("=")[0].strip() for k in cookie.split(";")}
    has_c_user = "c_user" in keys
    has_xs = "xs" in keys
    print(f"Cookie 欄位數: {len(keys)}，c_user={'✓' if has_c_user else '✗'}，xs={'✓' if has_xs else '✗'}")
    print(f"Cookie 預覽: {cookie[:80]}...")

    # 1. 偵測目前的 active 帳號
    current_user = ""
    try:
        status_res = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        lines = status_res.stdout.splitlines()
        for idx, line in enumerate(lines):
            if "Active account: true" in line:
                for j in range(idx - 1, -1, -1):
                    if "Logged in to" in lines[j]:
                        if "wenchiehlee-investment" in lines[j]:
                            current_user = "wenchiehlee-investment"
                        elif "wenchiehlee" in lines[j]:
                            current_user = "wenchiehlee"
                        elif "wj-lee_Barco" in lines[j]:
                            current_user = "wj-lee_Barco"
                        elif "wenchiehlee-money" in lines[j]:
                            current_user = "wenchiehlee-money"
                        break
                break
    except Exception:
        pass

    # 2. 自動切換至擁有權限的 wenchiehlee-money 帳號
    switched = False
    if current_user and current_user != "wenchiehlee-money":
        print(f"  偵測到目前 active 帳號為 {current_user}，正在切換至 wenchiehlee-money...")
        switch_res = subprocess.run(["gh", "auth", "switch", "--user", "wenchiehlee-money"], capture_output=True, text=True)
        if switch_res.returncode == 0:
            switched = True
        else:
            print(f"  警告：無法自動切換帳號，將嘗試以當前帳號執行: {switch_res.stderr.strip()}")

    # 3. 更新秘密與觸發 workflow
    success = True
    if not update_github_secret("FB_COOKIE", cookie):
        success = False
    if success and fb_dtsg:
        print(f"  fb_dtsg 預覽: {fb_dtsg[:40]}...")
        if not update_github_secret("FB_DTSG", fb_dtsg):
            success = False

    if success:
        trigger_workflow()

    # 4. 還原原本的 active 帳號
    if switched and current_user:
        print(f"  正在還原回原來的 {current_user} 帳號...")
        subprocess.run(["gh", "auth", "switch", "--user", current_user], capture_output=True, text=True)

    return 0 if success else 1


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Update FB_COOKIE GitHub secret")
    parser.add_argument("--cookie", help="Raw cookie string from browser network request (MCP flow)")
    parser.add_argument("--fb-dtsg", dest="fb_dtsg", help="fb_dtsg CSRF token (MCP flow)")
    args = parser.parse_args()

    if args.cookie:
        # MCP flow: cookie provided directly by arguments
        return _apply(args.cookie, args.fb_dtsg)

    # 1. 優先嘗試自動從 localhost:9222 偵錯瀏覽器中擷取
    cdp_result = try_auto_extract_via_cdp()
    if cdp_result:
        cookie, fb_dtsg = cdp_result
        return _apply(cookie, fb_dtsg)

    # 2. 自動擷取失敗，退回到傳統的 Cookie-Editor 檔案匯出方案
    print("\n  自動擷取失敗，將啟動備用方案 (Cookie-Editor JSON)...")
    cookie = _get_cookies_via_extension_export()
    if not cookie:
        return 1
    return _apply(cookie, None)


if __name__ == "__main__":
    raise SystemExit(main())
