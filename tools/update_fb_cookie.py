#!/usr/bin/env python3
"""Extract Facebook cookie from Chrome via Playwright and update GitHub secret FB_COOKIE."""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path


CHROME_EXE = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
CHROME_USER_DATA = Path(os.environ.get("LOCALAPPDATA", "")) / "Google" / "Chrome" / "User Data"


def is_chrome_running() -> bool:
    result = subprocess.run(
        "tasklist", capture_output=True, text=True, shell=True,
    )
    return "chrome.exe" in result.stdout.lower()


def copy_profile_to_temp(tmp_dir: Path) -> None:
    """Copy minimal Chrome profile files needed for cookie decryption."""
    src_default = CHROME_USER_DATA / "Default"
    dst_default = tmp_dir / "Default"
    dst_default.mkdir(parents=True)

    # Local State holds the AES encryption key (DPAPI-wrapped)
    shutil.copy2(CHROME_USER_DATA / "Local State", tmp_dir / "Local State")

    # Copy cookie database
    for name in ("Cookies", "Network"):
        src = src_default / name
        if src.exists():
            if src.is_dir():
                shutil.copytree(src, dst_default / name)
            else:
                shutil.copy2(src, dst_default / name)

    # Network subfolder may hold Cookies in newer Chrome versions
    network_src = src_default / "Network"
    if network_src.is_dir():
        network_dst = dst_default / "Network"
        network_dst.mkdir(exist_ok=True)
        cookie_in_network = network_src / "Cookies"
        if cookie_in_network.exists():
            shutil.copy2(cookie_in_network, network_dst / "Cookies")


def get_facebook_cookies_playwright() -> str:
    from playwright.sync_api import sync_playwright

    if is_chrome_running():
        print("偵測到 Chrome 正在執行中，請關閉所有 Chrome 視窗後重試。")
        return ""

    if not CHROME_EXE.exists():
        print(f"找不到 Chrome 執行檔: {CHROME_EXE}")
        return ""

    with tempfile.TemporaryDirectory(prefix="fb_cookie_") as tmp:
        tmp_dir = Path(tmp)
        print("複製 Chrome 設定檔到暫存目錄...")
        try:
            copy_profile_to_temp(tmp_dir)
        except Exception as e:
            print(f"複製設定檔失敗: {e}")
            return ""

        with sync_playwright() as p:
            print("啟動 Chrome（headless）...")
            ctx = p.chromium.launch_persistent_context(
                user_data_dir=str(tmp_dir),
                executable_path=str(CHROME_EXE),
                headless=False,
                args=["--profile-directory=Default", "--window-position=0,0"],
                timeout=30000,
            )
            page = ctx.new_page()
            print("前往 facebook.com...")
            try:
                page.goto("https://www.facebook.com", wait_until="domcontentloaded", timeout=20000)
            except Exception:
                pass  # timeout is fine, cookies may already be loaded
            cookies = ctx.cookies("https://www.facebook.com")
            ctx.close()

    cookie_dict = {c["name"]: c["value"] for c in cookies}
    if "c_user" not in cookie_dict or "xs" not in cookie_dict:
        print(f"取得 {len(cookie_dict)} 個 cookie，但缺少登入 session (c_user/xs)")
        print("請確認 Chrome 的 Default profile 已登入 Facebook")
        return ""

    print(f"成功取得 {len(cookie_dict)} 個 Facebook cookie")
    return "; ".join(f"{c['name']}={c['value']}" for c in cookies)


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
    if not CHROME_USER_DATA.exists():
        print(f"找不到 Chrome 設定檔目錄: {CHROME_USER_DATA}")
        return 1

    cookie = get_facebook_cookies_playwright()
    if not cookie:
        return 1

    print(f"Cookie 預覽: {cookie[:80]}...\n")

    if not update_github_secret(cookie):
        return 1

    trigger_workflow()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
