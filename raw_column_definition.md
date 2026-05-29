# Raw CSV Column Definitions - Facebook.Fetch

## raw_facebook_fetch.csv (Facebook Page Fetch Summary)

**Source:** `raw_facebook_fetch.csv`
**Data Source:** Facebook page scraping via Selenium
**Update Frequency:** Daily automated updates (1:10 AM CST)
**Extraction Strategy:** Scrape latest posts from Facebook pages and summary statistics (follower count).

### Columns

| Column | Type | Description | Source Field | Notes |
|---|---|---|---|---|
| `fetched_at_cst` | datetime | Timestamp when the data was fetched (CST) | System | `YYYY-MM-DD HH:MM CST` |
| `page_name` | string | Facebook page display name | Scraped | e.g., `FinGuider 美股資訊網` |
| `page_url` | string | Facebook page URL | Input | e.g., `https://www.facebook.com/FinGuider` |
| `new_post_count` | integer | Number of new posts found in this fetch | System |  |
| `total_post_count` | integer | Total posts stored in the local data directory | System | `len(data/{page_name}/*.md)` |
| `follower_count` | string | Page follower count string | Scraped | e.g., `5.9 萬位追蹤者` |
