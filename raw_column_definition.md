# Raw CSV Column Definitions - Facebook.Fetch

## raw_facebook_fetch.csv (Facebook Article Fetch Records)

**Source:** `raw_facebook_fetch.csv`
**Data Source:** Facebook page scraping
**Update Frequency:** Daily automated updates (1:10 AM CST)
**Extraction Strategy:** Scrape latest posts from configured Facebook pages, store each post as Markdown, and export one CSV row per stored article.

### Columns

| Column | Type | Description | Source Field | Notes |
|---|---|---|---|---|
| `process_timestamp` | datetime | Timestamp when the page was most recently fetched (CST) | `latest_fetch_summary.json.fetched_at_utc` | `YYYY-MM-DD HH:MM CST` |
| `page_name` | string | Facebook page display name | Scraped metadata / folder name |  |
| `page_url` | string | Facebook page URL used by the fetch | Fetch summary |  |
| `new_post_count` | integer | Number of new posts found in the latest fetch for this page | Fetch summary | Repeated on each article row for the page |
| `total_post_count` | integer | Total posts stored in the local page directory | System | `len(data/{page_name}/*.md)` |
| `follower_count` | string | Page follower count string | Scraped metadata | e.g., `6.2 萬位追蹤者` |
| `post_id` | string | Facebook post identifier | Markdown front matter |  |
| `title` | string | First non-empty post text line | Markdown front matter |  |
| `post_url` | string | Original Facebook post URL | Markdown front matter |  |
| `creation_time_utc` | datetime | Original post creation timestamp in UTC | Markdown front matter | Used as content date for downstream Lag checks |
| `creation_date` | date | Date portion of `creation_time_utc` | Derived | `YYYY-MM-DD` |
| `fetched_at_utc` | datetime | Timestamp when this article metadata was fetched | Markdown front matter |  |
| `fetched_at_cst` | datetime | `fetched_at_utc` converted to CST | Derived | `YYYY-MM-DD HH:MM CST` |
| `source` | string | Extraction source | Markdown front matter | e.g., `public_graphql` |
| `attachment_type` | string | Attachment type if present | Markdown front matter |  |
| `attachment_url` | string | Attachment URL if present | Markdown front matter |  |
| `markdown_path` | string | Local Markdown article path | System | Relative to repository root |
