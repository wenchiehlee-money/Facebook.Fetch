# Facebook.Fetch

用這個專案抓取指定的 Facebook 頁面連結，並把新貼文存到 `data/` 目錄。

<!-- AUTO-GENERATED:POSTS START -->
## 自動更新清單

### [FinGuider 美股資訊網](data/FinGuider%20%E7%BE%8E%E8%82%A1%E8%B3%87%E8%A8%8A%E7%B6%B2/index.md) (已收錄: 84)

### [Fomo研究院](data/Fomo%E7%A0%94%E7%A9%B6%E9%99%A2/index.md) (已收錄: 293)

### [大會計師 張明輝](data/%E5%A4%A7%E6%9C%83%E8%A8%88%E5%B8%AB%20%E5%BC%B5%E6%98%8E%E8%BC%9D/index.md) (已收錄: 82)

### [李其展的外匯交易致勝兵法](data/%E6%9D%8E%E5%85%B6%E5%B1%95%E7%9A%84%E5%A4%96%E5%8C%AF%E4%BA%A4%E6%98%93%E8%87%B4%E5%8B%9D%E5%85%B5%E6%B3%95/index.md) (已收錄: 299)

### [游庭皓的財經皓角](data/%E6%B8%B8%E5%BA%AD%E7%9A%93%E7%9A%84%E8%B2%A1%E7%B6%93%E7%9A%93%E8%A7%92/index.md) (已收錄: 337)

### [綠角財經筆記](data/%E7%B6%A0%E8%A7%92%E8%B2%A1%E7%B6%93%E7%AD%86%E8%A8%98/index.md) (已收錄: 6)

### [美股探路客](data/%E7%BE%8E%E8%82%A1%E6%8E%A2%E8%B7%AF%E5%AE%A2/index.md) (已收錄: 83)

### [股魚](data/%E8%82%A1%E9%AD%9A/index.md) (已收錄: 20)

### [行銷資料科學](data/%E8%A1%8C%E9%8A%B7%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8/index.md) (已收錄: 68)

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
- `image_url`
- `feedback_id`
- `source`

後面直接接貼文正文，閱讀起來會比把所有貼文塞在同一個 Markdown 檔裡更像單篇文章。

## GitHub Actions

已新增每日排程 workflow：

- `.github/workflows/daily_fetch.yml`

它會：

1. 檢出程式碼
2. 設定 Python 3.11
3. 重設所有 `latest_fetch_summary.json` 的 `new_post_count` 為 0
4. 依序抓取指定清單
5. 如果有任何一個抓取結果 `new_post_count > 0`，則提交並推送到 `main`
