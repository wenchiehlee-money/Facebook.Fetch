#!/usr/bin/env python3
"""Open a local helper page that explains how to copy a Facebook Cookie header."""

from __future__ import annotations

import socket
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


HTML_PAGE = """<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Facebook Cookie 複製說明</title>
  <style>
    :root {
      --bg: #f5f1e8;
      --panel: #fffaf0;
      --ink: #1e1b16;
      --muted: #63594b;
      --accent: #165d52;
      --border: #d8ccb9;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Microsoft JhengHei", "Noto Sans TC", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top right, #d9efe8 0, transparent 28%),
        radial-gradient(circle at bottom left, #efe1bf 0, transparent 24%),
        var(--bg);
    }
    main {
      max-width: 900px;
      margin: 48px auto;
      padding: 0 20px;
    }
    .panel {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 28px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
    }
    h1 { margin-top: 0; font-size: 32px; }
    p, li { line-height: 1.7; }
    ol { padding-left: 22px; }
    code, pre {
      font-family: Consolas, "Courier New", monospace;
      background: #f3ede3;
      border-radius: 8px;
    }
    code { padding: 2px 6px; }
    pre {
      padding: 14px;
      overflow-x: auto;
      border: 1px solid var(--border);
    }
    .note {
      margin-top: 18px;
      padding: 14px 16px;
      border-left: 4px solid var(--accent);
      background: #edf7f4;
      color: var(--muted);
    }
  </style>
</head>
<body>
  <main>
    <section class="panel">
      <h1>Facebook Cookie Header 複製說明</h1>
      <p>這個工具不會讀取你的瀏覽器資料，也不會匯出任何 cookie。它只是把手動複製步驟整理成一頁，方便你在 Windows 11 上操作。</p>

      <ol>
        <li>先在 Chrome 或 Edge 登入 Facebook。</li>
        <li>打開 <code>https://www.facebook.com/yutinghaosfinance</code></li>
        <li>按 <code>F12</code> 開啟開發者工具。</li>
        <li>切到 <code>Network</code>。</li>
        <li>重新整理頁面。</li>
        <li>在左側請求清單裡，點一筆送往 <code>facebook.com</code> 的主文件或 GraphQL 請求。</li>
        <li>在右側 <code>Headers</code> 找到 <code>Request Headers</code>。</li>
        <li>找到 <code>cookie:</code> 這一行，複製整段值。</li>
      </ol>

      <p>你最後要貼給我的內容長這樣，但只要貼 <code>cookie:</code> 後面的值即可：</p>
      <pre>sb=...; datr=...; c_user=...; xs=...; fr=...</pre>

      <div class="note">
        <strong>安全提醒</strong><br>
        不要把螢幕截圖貼給我，也不要分享帳號密碼。只需要貼 Request Headers 裡的 cookie 字串。
      </div>
    </section>
  </main>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802
        body = HTML_PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return


def pick_port() -> int:
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


def main() -> int:
    port = pick_port()
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    url = f"http://127.0.0.1:{port}/"
    print(f"已開啟本機說明頁: {url}")
    print("瀏覽器打開後，照頁面步驟從 DevTools 手動複製 Cookie header。")
    webbrowser.open(url)

    try:
        input("完成後按 Enter 結束...")
    finally:
        server.shutdown()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
