# Facebook.Fetch

用這個專案抓取指定的 Facebook 頁面連結，並把結果存到 `data/` 目錄。

## 執行方式

```bash
python3 fetch_facebook_posts.py 'https://www.facebook.com/dextermchang'
```

如果你想多抓幾篇：

```bash
python3 fetch_facebook_posts.py 'https://www.facebook.com/dextermchang' --count 5
```

## 輸出內容

每次執行都會產生：

- `*.html`：Facebook 原始 HTML 回應
- `*.json`：整理後的頁面資訊與貼文資料
- `*_posts/`：每篇貼文各自一個 Markdown 檔
- `*_posts/index.md`：貼文索引頁

## 單篇 Markdown 格式

每篇貼文都會各自輸出成一個 `.md` 檔，檔案開頭包含 YAML metadata，例如：

- `post_id`
- `title`
- `post_url`
- `creation_time_utc`
- `fetched_at_utc`
- `attachment_type`
- `attachment_url`
- `feedback_id`
- `source`

後面直接接貼文正文，閱讀起來會比把所有貼文塞在同一個 Markdown 檔裡更像單篇文章。

## 抓取策略

腳本會依序嘗試：

- 從公開頁面 HTML 擷取 `LSD`、`jazoest`、`userID`
- 呼叫公開的 `ProfileCometTimelineFeedRefetchQuery`
- 從 GraphQL 回應遞迴抽出 `post_id`、`permalink_url`、`creation_time`、`message`
- 如果公開 GraphQL 失敗，再退回 HTML 解析

## 說明

Facebook 的公開頁面結構很常調整，所以這份腳本仍屬於 best-effort 抓取器。
目前對 `https://www.facebook.com/dextermchang` 已可透過公開 GraphQL 抓到實際貼文內容，並輸出成一篇貼文一個 Markdown 檔。
