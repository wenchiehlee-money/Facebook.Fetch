---
name: skill-facebook-fetch
description: 管理 Facebook.Fetch 專案的每日粉專/珍藏清單貼文抓取 — 本機執行與 GitHub Actions 共用同一支 run_daily_fetch.py，更新過期的 FB_COOKIE、手動觸發並監看 daily_fetch workflow、排查已知的資料夾命名衝突與 sync 觸發失敗問題。
---

# Facebook Fetch Skill (Facebook 粉專/珍藏清單抓取維運技能)

此技能封裝 `wenchiehlee-money/Facebook.Fetch` 專案（本機路徑 `github.com/Facebook.Fetch`）每日抓取排程的維運 SOP：
更新過期登入 cookie、本機或手動觸發/監看 GitHub Actions workflow，以及排查已知的資料收斂錯誤。

**單一實作、雙重執行路徑：** `.github/workflows/daily_fetch.yml` 本身就是呼叫
`scripts/run_daily_fetch.py`（見下方「本機執行完整抓取流程」），而不是在 YAML 裡另外重寫一份
bash 邏輯。因此本技能在本機執行 `run_daily_fetch.py` 得到的 `data/`、`README.md`、
`raw_facebook_fetch.csv` 結果，跟排程觸發 GitHub Actions 的結果是**同一套程式碼路徑**，
不會有兩份邏輯各自漂移的問題。

實際抓取邏輯（`fetch_facebook_posts.py`、`fetch_saved_list.py`）與 GitHub Actions
定義保留在來源 repo 中，本技能不複製核心抓取邏輯，只複製兩支維運/編排腳本讓技能能自包含使用：
- `scripts/update_fb_cookie.py`（來源 repo `tools/update_fb_cookie.py` 的副本）
- `scripts/run_daily_fetch.py`（來源 repo `scripts/run_daily_fetch.py` 的副本，
  YAML workflow 呼叫的正是這支腳本）

若來源 repo 內兩支檔案存在，一律優先使用來源 repo 版本（較新、且是唯一真正被 CI 執行的版本），
本技能內附的副本僅作為技能自包含的備援。

## 前置需求

- 在 `Facebook.Fetch` repo 目錄下執行所有指令。
- `gh` CLI 需登入對 `wenchiehlee-money/Facebook.Fetch` 有 `repo`+`workflow` 權限的帳號；
  若目前作用中帳號不是該擁有者，先切換：
  ```bash
  gh auth switch --user wenchiehlee-money
  ```
  操作完成後記得切回原本預設帳號（`gh auth switch --user <原帳號>`），避免影響其他 repo 的操作。
- Chrome DevTools MCP（`mcp__chrome-devtools__*`）用於從已登入的瀏覽器分頁擷取新 cookie。

## 命令說明

| 情境 | 指令 |
|---|---|
| 更新過期的 FB_COOKIE / FB_DTSG | 見下方「更新 Cookie 流程」；備援腳本 `<SKILL_DIR>/scripts/update_fb_cookie.py` |
| 本機執行完整抓取流程（跟 CI 同一份邏輯） | 見下方「本機執行完整抓取流程」 |
| 手動觸發 GitHub Actions 抓取 | `gh workflow run daily_fetch.yml` |
| 監看執行狀態直到完成 | `gh run watch <run-id> --exit-status` |
| 查詢最近執行紀錄 | `gh run list --workflow daily_fetch.yml --limit 3` |
| 回溯抓取近 30 天貼文（補資料用） | `gh workflow run daily_fetch.yml -f months_back=1` |

## 本機執行完整抓取流程

`run_daily_fetch.py` 是 `daily_fetch.yml` 唯一呼叫的實作，涵蓋：重置 new_post_count →
抓珍藏清單 → 依 `data/fetch_urls.txt` 逐頁抓取 → 重建 README → 更新
`raw_facebook_fetch.csv` → 統計新貼文數 →（可選）commit/push →（可選）觸發 sync →
（可選）cookie 過期時開 issue。預設只做到「更新 CSV / README」，commit、觸發 sync、
開 issue 都是 opt-in flag，避免本機執行時不小心動到 git 或觸發下游 workflow。

```bash
# 只抓資料、更新 README/CSV，不 commit、不觸發任何東西（本機測試用）
python <SKILL_DIR>/scripts/run_daily_fetch.py --cookie "$FB_COOKIE" --fb-dtsg "$FB_DTSG"

# 完全比照 CI 行為（commit/push + 觸發 sync + cookie 過期開 issue）
python <SKILL_DIR>/scripts/run_daily_fetch.py --cookie "$FB_COOKIE" --fb-dtsg "$FB_DTSG" \
  --commit --trigger-sync --create-issue

# 回溯抓近 30 天（補資料）
python <SKILL_DIR>/scripts/run_daily_fetch.py --cookie "$FB_COOKIE" --fb-dtsg "$FB_DTSG" --months-back 1
```

FB_COOKIE / FB_DTSG 省略 `--cookie`/`--fb-dtsg` 時會自動從環境變數或 repo 根目錄的 `.env` 讀取。

## 更新 Cookie 流程

1. `mcp__chrome-devtools__navigate_page` 導航至 `https://www.facebook.com`（若該分頁尚未登入，
   先提醒使用者手動登入後再繼續 — 回應標頭 `set-login:logged-in` 代表登入有效，
   `set-login:logged-out` 且 cookie 被標記 `deleted` 代表尚未登入或已過期）。
2. `mcp__chrome-devtools__list_network_requests`（`resourceTypes: ["document"]`）取得該次導航的
   document request，用 `mcp__chrome-devtools__get_network_request` 讀出 Request Headers 中的
   `cookie` 字串。
3. 從同一批次的 XHR/fetch 請求（例如 `POST /ajax/bnzai`）URL query string 中取得 `fb_dtsg`
   （URL-decode `%3A` → `:`）。
4. 執行（在 `Facebook.Fetch` repo 目錄下）：
   ```bash
   python <SKILL_DIR>/scripts/update_fb_cookie.py --cookie "<cookie 字串>" --fb-dtsg "<fb_dtsg>"
   ```
   若來源 repo 的 `tools/update_fb_cookie.py` 存在且較新，優先使用該檔案（本技能的副本僅為備援，
   兩者行為應保持一致）。此腳本會更新 GitHub Secrets `FB_COOKIE`、`FB_DTSG` 並自動觸發
   `daily_fetch.yml`。
   （若不在 Claude Code / MCP 環境，腳本支援 Cookie-Editor 擴充套件匯出 JSON 的備援流程，
   直接執行 `python <SKILL_DIR>/scripts/update_fb_cookie.py` 不帶參數即可。）

## 已知問題與排查

### 1. Facebook GraphQL Rate Limiting（code 1675004）
GitHub Actions runner IP 在同一小時內執行超過 ~5-6 次會被限流，回傳 0 篇貼文。
**處置：** 不要在短時間內重複手動觸發 daily_fetch；排定的每日排程（01:10 UTC）本身是安全的。

### 2. Cookie 過期（Facebook error 1357001 "請登入以繼續"）
`fetch_facebook_posts.py` / `fetch_saved_list.py` 遇到此錯誤會以 Exit Code 2 中斷。
`daily_fetch.yml` 已將「Fetch saved lists」步驟排在「Run daily fetch」之前，
避免粉專抓取中斷導致珍藏清單完全沒被執行到。
**處置：** 依上方「更新 Cookie 流程」重新取得 cookie。

### 3. 資料夾命名 fallback 衝突（folder-name collision，已知未修復）
`fetch_facebook_posts.py` 決定貼文輸出資料夾名稱的邏輯（約在 `page_title = args.page_name or
payload["page"]["title"] or urlsplit(url).path.strip("/") or "Facebook Page"`）：
當該次抓取因登入態 HTML 結構不同等原因，未能解析出頁面標題（`page.title` 為 `null`）時，
會退回使用「URL path slug」當資料夾名。若 `data/fetch_urls.txt` 該列沒有指定 `page_name`
（Tab 分隔的第二欄），且既有資料夾原本是用中文頁面標題建立的，就會產生**新的重複資料夾**，
新貼文因此「沒有跟原本的 group 分在一起」。

實測（2026-07-20 那次 cookie 更新後手動觸發的 daily_fetch）顯示這**不是零星個案，而是系統性**：
當次執行對幾乎所有英文 slug 網址的標題解析都失敗（`page.title: null`），導致
`FinGuider`、`ForexStrategist`、`GreenHornFans`、`MarketingDataScienceTMR`、`stocksardine`、
`raikk6`、`dextermchang`、`intleconobserve`、`yutinghaosfinance` 全部另外產生了 slug 資料夾，
和既有的中文標題資料夾（`FinGuider 美股資訊網`、`李其展的外匯交易致勝兵法`、`綠角財經筆記`、
`行銷資料科學`、`股魚`、`美股探路客`、`大會計師 張明輝`、`IEObserve 國際經濟觀察`、
`游庭皓的財經皓角`）並存。

更嚴重的情況：`data/fetch_urls.txt` 中多筆 `profile.php?id=...` 網址若都沒有指定
`page_name`，一旦標題解析失敗，會全部退回相同的 `profile.php`（URL slug 不含 query
string），導致**不同 Facebook 個人檔案的貼文被混進同一個資料夾**。

**判斷是否發生碰撞：** 對可疑的 slug 資料夾執行
`grep -l "requested_url.*<url>" data/*/latest_fetch_summary.json`，
若同一個 `requested_url` 命中兩個以上的資料夾，就是碰撞，需人工合併。

**處置（已對 2026-07-20 這次全部合併完成）：**
- `data/fetch_urls.txt` 現在每一列都已補上正確的正式 `page_name`（不是 slug），
  這樣即使未來標題解析再次失敗，也會直接寫回正確的資料夾，不會再產生新的碰撞。
- 合併既有重複/混雜資料夾的做法：比對 `latest_fetch_summary.json` 的 `requested_url`
  找出真正的來源資料夾，用 `post_id` 去重後把 slug 資料夾的 `.md` 搬進正式資料夾，
  重建 `index.md`，刪除清空後的 slug 資料夾，最後跑 `python scripts/rebuild_readme.py`。
- 根本修復方向（尚未實作於程式碼）：`fetch_facebook_posts.py` 的 fallback 應改用「先掃描既有
  `data/*/latest_fetch_summary.json` 找出 `requested_url` 相符的資料夾」，找不到才退回
  slug；且 slug fallback 應納入 query string（如 `id=` 值）以避免多個 `profile.php` 碰撞。
  在此修復落地前，`data/fetch_urls.txt` 每列都要有正確的 `page_name` 作為主要防線。

### 4. 「Trigger sync to biztrends.TW」步驟 403 失敗（已修復）
該步驟使用 `gh workflow run sync-to-biztrends.yml` 觸發另一個 workflow，
預設 `github.token` 沒有權限觸發其他 workflow 的 `workflow_dispatch`（HTTP 403
"Resource not accessible by integration"）。已改用 repo 既有的 PAT
`secrets.REPO_FILE_SYNC_WENCHIEHLEE_MONEY1`（與 checkout 步驟同一組 secret）。

## 使用範例

```bash
gh auth switch --user wenchiehlee-money
gh workflow run daily_fetch.yml
gh run list --workflow daily_fetch.yml --limit 1
gh run watch <run-id> --exit-status
gh auth switch --user <原本的預設帳號>
```
