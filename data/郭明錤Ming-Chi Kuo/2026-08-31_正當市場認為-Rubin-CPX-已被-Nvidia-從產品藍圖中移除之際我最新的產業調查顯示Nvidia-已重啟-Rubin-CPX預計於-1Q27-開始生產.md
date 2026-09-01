---
post_id: "122191286378799750"
title: "正當市場認為 Rubin CPX 已被 Nvidia 從產品藍圖中移除之際，我最新的產業調查顯示，Nvidia 已重啟 Rubin CPX，預計於 1Q27 開始生產。相較舊版，重啟後的 Rubin CPX 擁有更強的預填充（prefill）效能，GPU 規格與機櫃架構也都有明顯改變，足以證明 Nvidia 對 prefill 方案的高度重視。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61573992511738"
final_url: "https://www.facebook.com/profile.php?id=61573992511738"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid063dyxTGJd64GvbY1M2UnFiXs2QTo2hicC4H6axW3NiSvcrzhBZEReTDLVv24oFQjl&id=61573992511738"
creation_time_utc: "2026-08-31T14:04:59+00:00"
fetched_at_utc: "2026-09-01T06:13:18.243978+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTIyMTkxMjg2Mzc4Nzk5NzUw"
page_canonical_url: ""
---

# 正當市場認為 Rubin CPX 已被 Nvidia 從產品藍圖中移除之際，我最新的產業調查顯示，Nvidia 已重啟 Rubin CPX，預計於 1Q27 開始生產。相較舊版，重啟後的 Rubin CPX 擁有更強的預填充（prefill）效能，GPU 規格與機櫃架構也都有明顯改變，足以證明 Nvidia 對 prefill 方案的高度重視。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid063dyxTGJd64GvbY1M2UnFiXs2QTo2hicC4H6axW3NiSvcrzhBZEReTDLVv24oFQjl&id=61573992511738
正當市場認為 Rubin CPX 已被 Nvidia 從產品藍圖中移除之際，我最新的產業調查顯示，Nvidia 已重啟 Rubin CPX，預計於 1Q27 開始生產。相較舊版，重啟後的 Rubin CPX 擁有更強的預填充（prefill）效能，GPU 規格與機櫃架構也都有明顯改變，足以證明 Nvidia 對 prefill 方案的高度重視。

關鍵改變如下：

1. Rubin CPX GPU 規格
CPX 算力接近 Rubin，單顆 GPU 最高功耗也同為 2,300 W。CPX 記憶體改為 168 GB HBM4，低於 Rubin 的 288 GB HBM4，但高於舊版 CPX 的 128 GB GDDR7。

2. 機櫃設計
新版 CPX 採用獨立的 MGX ETL 機櫃，不再像舊版與 Rubin 共櫃。客戶可依需求配置 64、128、192 或 256 顆 CPX。在 CPX 機櫃中，每 64 顆 CPX 組成一個機櫃模組，每個機櫃模組配置 8 個運算托盤（每個托盤有 8 顆 CPX）與 1 個交換機托盤。

3. Scale-up 與 scale-out
NVLink 僅用於同一托盤內 8 顆 CPX GPU 的 scale-up，每顆 CPX 的 NVLink 頻寬為 1–1.5 TB/s（vs. 每顆 Rubin 的 3.6 TB/s）。同一機櫃模組內的托盤間，透過 Spectrum-6 Ethernet（全銅 L1）進行 scale-out；跨機櫃模組時，則由各模組的 Spectrum-6 透過 OSFP 光纖進行 scale-out。

4. 運作方式
CPX 需與 Vera Rubin NVL72 搭配，Nvidia 建議 CPX 與 Rubin 的比例為 1:1。CPX 負責預填充（prefill）並建立 KV cache，再透過 Ethernet RDMA 傳給 Rubin 執行解碼生成（decode）。

5. 產品定位：長上下文 prefill 的最高性價比方案
目前 AI 推論工作量中，超過一半來自處理輸入內容（context）並建立相對應的 KV cache，因此，CPX 以更彈性的部署方式與更低成本承接 prefill。每個運算托盤（有 8 個 CPX）約有 1.34 TB HBM4，足以支援大多數長上下文 prefill 與 KV cache 建立需求。
