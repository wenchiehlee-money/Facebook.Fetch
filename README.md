# Facebook.Fetch

用這個專案抓取指定的 Facebook 頁面連結，並把新貼文存到 `data/` 目錄。

<!-- AUTO-GENERATED:POSTS START -->
## 自動更新清單

- 資料夾: `data/大會計師 張明輝`
- 頁面名稱: `大會計師 張明輝`
- Updated: 2026-04-10 00:32 CST
- 已收錄貼文數量: `3`

### 全部貼文

- `2026-04-09` [懂財報可以幫你投資「趨吉避兇」！](data/大會計師 張明輝/2026-04-09_懂財報可以幫你投資趨吉避兇.md)
- `2026-04-08` [40歲前還債、60歲才開始投資......我不是靠少年得志致富的，我是先把債還完，才把人生賺回來](data/大會計師 張明輝/2026-04-08_40歲前還債60歲才開始投資我不是靠少年得志致富的我是先把債還完才把人生賺回來.md)
- `2026-04-07` [繁榮的背後，藏著重資本產業宿命！從財報視角拆解 ＃PCB產業 的關鍵本質](data/大會計師 張明輝/2026-04-07_繁榮的背後藏著重資本產業宿命從財報視角拆解-PCB產業-的關鍵本質.md)

### 最近 7 天貼文

- `2026-04-09` [懂財報可以幫你投資「趨吉避兇」！](data/大會計師 張明輝/2026-04-09_懂財報可以幫你投資趨吉避兇.md)
- `2026-04-08` [40歲前還債、60歲才開始投資......我不是靠少年得志致富的，我是先把債還完，才把人生賺回來](data/大會計師 張明輝/2026-04-08_40歲前還債60歲才開始投資我不是靠少年得志致富的我是先把債還完才把人生賺回來.md)
- `2026-04-07` [繁榮的背後，藏著重資本產業宿命！從財報視角拆解 ＃PCB產業 的關鍵本質](data/大會計師 張明輝/2026-04-07_繁榮的背後藏著重資本產業宿命從財報視角拆解-PCB產業-的關鍵本質.md)

<!-- AUTO-GENERATED:POSTS END -->

## 手動執行

```bash
python3 fetch_facebook_posts.py 'https://www.facebook.com/dextermchang' --count 20
```

## 增量抓取規則

腳本現在是增量模式：

- 只檢查最新一批貼文（預設 20 篇）
- 只新增新的 `post_id`
- 已存在的貼文 Markdown 不會重寫
- `index.md` 會更新成目前文章清單
- `latest_fetch_summary.json` 會記錄這次有沒有抓到新貼文
- `README.md` 會自動更新資料夾名稱、全部貼文清單與最近 7 天貼文

## 輸出結構

目前會輸出到：

- `data/大會計師 張明輝/`

這個資料夾內包含：

- `YYYY-MM-DD_貼文標題.md`：單篇貼文
- `index.md`：文章索引
- `latest_fetch_summary.json`：最近一次抓取摘要

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

## GitHub Actions

已新增每日排程 workflow：

- `.github/workflows/daily_fetch.yml`

它會：

- 每天自動執行抓取
- 自動更新 `README.md` 的貼文清單區塊
- 只有在 `new_post_count > 0` 時才建立 git commit
- 自動 push 到 `main`

如果當天沒有新貼文，workflow 會結束，不會產生新 commit。

注意：如果兩次排程之間新增的貼文數量超過 `--count`，較舊的那幾篇可能會漏掉；目前 workflow 預設檢查最新 20 篇。

## 說明

Facebook 的公開頁面結構很常調整，所以這份腳本仍屬於 best-effort 抓取器。
目前對 `https://www.facebook.com/dextermchang` 已可透過公開 GraphQL 抓到實際貼文內容，並以增量方式保存。
