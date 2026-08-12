---
post_id: "1579768960506471"
title: "------------\"理想狀況下，整個 KV 快取都儲存在 GPU 或 AI 加速器旁邊的 HBM，這樣可以減少物理距離並降低延遲。HBM 約三分之一的容量通常保留給 KV 快取，而神經網路儲存的權重也約佔三分之一，工作中的部分則佔最後三分之一。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid08ZCnVG4AUD8UaZnMWuo2j7S82woFAH7eLA3J7Zh7UPyU9Hf316jzkJXdaZvbypBxl&id=100054201473657"
creation_time_utc: "2026-08-09T13:21:05+00:00"
fetched_at_utc: "2026-08-12T03:28:03.919299+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-dfw6-1.xx.fbcdn.net/v/t39.30808-6/768372630_1579768713839829_7146912955455907828_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=L4irzaHTIW0Q7kNvwF6BZbc&_nc_oc=AdrjykA0BsFC_hKox0JyogG5oyhtZQ-d0BDe8sO1nAXOriDz_C1DNbsT80llcHwwdks&_nc_zt=23&_nc_ht=scontent-dfw6-1.xx&_nc_gid=dEdzn6qqBvy8ecRlcC1bMQ&_nc_ss=7e120&oh=00_AQEdxBuYQmRB3JuYmgZiLCbBM-2gCmk-Zcx7GKuGbSNz_A&oe=6A819F2C"
feedback_id: "ZmVlZGJhY2s6MTU3OTc2ODk2MDUwNjQ3MQ=="
page_canonical_url: ""
---

# ------------"理想狀況下，整個 KV 快取都儲存在 GPU 或 AI 加速器旁邊的 HBM，這樣可以減少物理距離並降低延遲。HBM 約三分之一的容量通常保留給 KV 快取，而神經網路儲存的權重也約佔三分之一，工作中的部分則佔最後三分之一。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid08ZCnVG4AUD8UaZnMWuo2j7S82woFAH7eLA3J7Zh7UPyU9Hf316jzkJXdaZvbypBxl&id=100054201473657

![------------"理想狀況下，整個 KV 快取都儲存在 GPU 或 AI 加速器旁邊的 HBM，這樣可以減少物理距離並降低延遲。HBM 約三分之一的容量通常保留給 KV 快取，而神經網路儲存的權重也約佔三分之一，工作中的部分則佔最後三分之一。](https://scontent-dfw6-1.xx.fbcdn.net/v/t39.30808-6/768372630_1579768713839829_7146912955455907828_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=L4irzaHTIW0Q7kNvwF6BZbc&_nc_oc=AdrjykA0BsFC_hKox0JyogG5oyhtZQ-d0BDe8sO1nAXOriDz_C1DNbsT80llcHwwdks&_nc_zt=23&_nc_ht=scontent-dfw6-1.xx&_nc_gid=dEdzn6qqBvy8ecRlcC1bMQ&_nc_ss=7e120&oh=00_AQEdxBuYQmRB3JuYmgZiLCbBM-2gCmk-Zcx7GKuGbSNz_A&oe=6A819F2C)
------------"理想狀況下，整個 KV 快取都儲存在 GPU 或 AI 加速器旁邊的 HBM，這樣可以減少物理距離並降低延遲。HBM 約三分之一的容量通常保留給 KV 快取，而神經網路儲存的權重也約佔三分之一，工作中的部分則佔最後三分之一。

問題在於現有的 HBM 很少能像供應商想要的那樣大容量儲存 KV 快取。當 KV 快取需求超過 HBM 空間——也就是 AI 提供者撞上記憶體牆時，KV 快取會溢出到下一層儲存，通常是 DRAM 與企業級固態硬碟（SSD）或快閃記憶體的組合。

雖然 SSD 容量大，但它們是透過網路存取，速度比 HBM 或 DRAM 慢。透過其全新的上下文記憶體擴充（CMX）架構，Nvidia 提出了一系列技術與技術——例如即將推出的 BlueField-4 資料處理單元 DPU、利用 RDMA over Converged Ethernet（RoCE）以及自適應路由——以最大化企業快閃陣列上 KV 快取查詢的效率與吞吐量。所有大型快閃陣列儲存廠商都在開發 CMX 產品，準備在今年秋天 BlueField-4 DPU 正式出貨時使用，同時也在開發自家的 KV 快取卸載解決方案以供銷售。
......
HBF 的理念是將它們置於處理器旁邊，提供類似 HBM 的吞吐量，但容量遠高於 HBM 或 DRAM。Gen2 與 Gen3 HBF 預計每堆疊可提供 3 TBps 的讀取頻寬，與目前僅提供 3.3TBps 的 HBM4 相比相當優異。HBF 的實體尺寸、功耗配置與堆疊高度高度，這將有助於晶片製造商將 HBF 整合進未來的 AI 加速器，包括 GPU 與 CPU。

HBM也不會坐視不理。根據韓國科學技術研究院的 HBM 路線圖，HBM5 預計於 2029 年出貨時提供 4TBps 頻寬，接著 2032 年搭載 HBM6 時提供 8TBps，2035 年搭載 HBM7 可達 24TBps，2038 年出貨時則為 64TBps。那些12年後出貨的HBM8模組，將開始接近靜態隨機存取記憶體（SRAM）所能提供的荒謬的100TBps記憶體頻寬。雖然 SRAM 速度非常快，但價格相當昂貴。此外，最大型的 SRAM 晶片，如 Cerebras Systems 的晶片，每顆晶片僅提供 44GB 的片上 SRAM。總是有取捨。

HBF 唯一的缺點是寫入速度非常慢。然而，KV 快取主要是唯讀功能，這消除了這個缺點，使 HBF 有可能成為解決 KV 快取擴充問題的好方案。"

https://www.hpcwire.com/2026/08/04/what-is-high-bandwidth-flash-hbf-and-can-it-overcome-the-ai-memory-wall/
