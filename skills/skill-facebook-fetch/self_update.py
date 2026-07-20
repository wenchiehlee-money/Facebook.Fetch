#!/usr/bin/env python3
"""
self_update.py
此模組會在被 import 時自動檢查遠端 GitHub repo（wenchiehlee/skills）對應 skill
目錄的最新檔案，無論版本號為何，都會直接下載覆寫本地檔案，並在完成後
重新執行當前腳本，使使用者得到最新的實作。
"""
import os
import sys
import urllib.request
from pathlib import Path

REMOTE_REPO = "wenchiehlee/skills"
SKILL_SUBPATH = Path(__file__).resolve().parent.name

def _remote_url(relative_path: str) -> str:
    return f"https://raw.githubusercontent.com/{REMOTE_REPO}/main/common/{SKILL_SUBPATH}/{relative_path}"

def _download_file(rel_path: str, dest_path: Path):
    url = _remote_url(rel_path)
    try:
        with urllib.request.urlopen(url) as resp:
            data = resp.read()
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "wb") as f:
            f.write(data)
        print(f"[self_update] 已下載 {rel_path} → {dest_path}")
    except Exception as e:
        print(f"[self_update] 下載失敗 {rel_path}: {e}", file=sys.stderr)

def _perform_update():
    base_dir = Path(__file__).resolve().parent
    for fn in ["SKILL.md", "metadata.json"]:
        _download_file(fn, base_dir / fn)
    scripts_dir = base_dir / "scripts"
    if scripts_dir.is_dir():
        for py_file in scripts_dir.glob("*.py"):
            _download_file(f"scripts/{py_file.name}", scripts_dir / py_file.name)
    print("[self_update] 更新完成")

def _needs_update() -> bool:
    try:
        with urllib.request.urlopen(_remote_url("SKILL.md")) as resp:
            return resp.status == 200
    except Exception:
        return False

if _needs_update():
    _perform_update()
    os.execv(sys.executable, [sys.executable] + sys.argv)
