---
post_id: "1459900359159999"
title: "首款可量產的CXL DRAM KV Cache Server，一台11TB DRAM，不可思議的是還相容於Nvidia的Dynamo軟體，可以統一設計整套LLM Inference KV Cache卸載策略，Blackwell GPU/HBM-Grace CPU/DRAM-Penguin CXL DRAM Server-Local SSDs-Nvidia DPU ICMS(改名CMX STX) SSD Rack-Network SSD/HDD"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0S9QyKejUrSPWAyErm57Myt8Nk3uHS32aAQS2VJCUT3TYsJZqfVmyeorxFg64Gmzfl&id=100054201473657"
creation_time_utc: "2026-03-20T16:32:20+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/655892267_1459893702493998_7402461089862807945_n.jpg?stp=dst-jpg_s600x600_tt6&_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=fCqM6B94744Q7kNvwFGe3GH&_nc_oc=Adqh9jNg5OxuIkmj1H06S19Qbt98IvpDQc0mh1JxFz1PXowmDvg89lnn0u4hEC_IbYU&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=HrZTGRjqeemWumWJLH7IFw&_nc_ss=78100&oh=00_Af9sOw-xUjZeYexs7I_ZOj34w7Omujrjivibs2n37iWXJg&oe=6A384E44"
feedback_id: "ZmVlZGJhY2s6MTQ1OTkwMDM1OTE1OTk5OQ=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 首款可量產的CXL DRAM KV Cache Server，一台11TB DRAM，不可思議的是還相容於Nvidia的Dynamo軟體，可以統一設計整套LLM Inference KV Cache卸載策略，Blackwell GPU/HBM-Grace CPU/DRAM-Penguin CXL DRAM Server-Local SSDs-Nvidia DPU ICMS(改名CMX STX) SSD Rack-Network SSD/HDD

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0S9QyKejUrSPWAyErm57Myt8Nk3uHS32aAQS2VJCUT3TYsJZqfVmyeorxFg64Gmzfl&id=100054201473657

![首款可量產的CXL DRAM KV Cache Server，一台11TB DRAM，不可思議的是還相容於Nvidia的Dynamo軟體，可以統一設計整套LLM Inference KV Cache卸載策略，Blackwell GPU/HBM-Grace CPU/DRAM-Penguin CXL DRAM Server-Local SSDs-Nvidia DPU ICMS(改名CMX STX) SSD Rack-Network SSD/HDD](https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/655892267_1459893702493998_7402461089862807945_n.jpg?stp=dst-jpg_s600x600_tt6&_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=fCqM6B94744Q7kNvwFGe3GH&_nc_oc=Adqh9jNg5OxuIkmj1H06S19Qbt98IvpDQc0mh1JxFz1PXowmDvg89lnn0u4hEC_IbYU&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=HrZTGRjqeemWumWJLH7IFw&_nc_ss=78100&oh=00_Af9sOw-xUjZeYexs7I_ZOj34w7Omujrjivibs2n37iWXJg&oe=6A384E44)
首款可量產的CXL DRAM KV Cache Server，一台11TB DRAM，不可思議的是還相容於Nvidia的Dynamo軟體，可以統一設計整套LLM Inference KV Cache卸載策略，Blackwell GPU/HBM-Grace CPU/DRAM-Penguin CXL DRAM Server-Local SSDs-Nvidia DPU ICMS(改名CMX STX) SSD Rack-Network SSD/HDD

之前寫過認為2H26有機會CXL Memory Pool有可能開始貢獻DRAM需求，後來有看到報導說CXL沒有那麼快，2027才有可能，我想大量也許是2027年吧! 在AI應用成為Memory/Storage主流，而AI從LLM到軟硬體架構快速演變的時候，要計算未來一年兩年的DRAM需求，實在不容易，不容易也要去探討，不然怎麼估計demand呢? 今天看到一篇外文方向改變的DRAM報告，理由全部是supply side的理由，相對而言supply很好問，demand在AI時代很難預測，但沒辦法還是得去想個方向、因素等，如果完全忽略AI架構的快速演進，那demand的想法、方向，從何而來呢? 因為現在AI related DRAM demand已經佔50%以上，廣義加上通用Server DRAM demand已經佔60%，不探討AI需求內涵，怎麼估D/S呢?

例如Nvidia才剛發表ICMS(改名為BF4 STX/CMX平台)SSD Rack不久的GTC，CXL Memory Pool又將開始慢慢滲入市場，以因應已龐大又快速成長的inference需求，而CXL標準剛發展的時候根本還沒有生成式AI，調整到3.0時代，一方面規格改進，加上配合AI發展，可望加速被普及

By the way, Penguin Solution可能大家很陌生，Smart Mudular可能比較聽過，和宜鼎類似的工控DRAM/SSD模組品牌

----------"Penguin Solutions 推出業界首款可量產的基於 CXL 的 KV Cache Server，專為優化企業級推論效能而設計，包括代理型 AI。結果是更低的延遲、更高的吞吐量、GPU 叢集的效率提升、嚴格的服務水準協議（SLA）持續達成，以及更快的首次代幣交付時間（TTFT）
......
Penguin 的 MemoryAI 快取伺服器加速了依賴記憶體的 AI 流程，整合了 3 TB DDR5 主記憶體及最多八張 1TB 的 CXL 擴充卡（AIC），提升記憶體容量。
......
支援更大上下文大小與並行性：Penguin 的 MemoryAI KV 快取伺服器對於需要大型上下文視窗與最低延遲的企業級任務尤其重要，包括即時金融新聞解析、龐大 10-K 資料集上的檢索增強生成（RAG）及法規遵循分析

叢集記憶體層級彈性：伺服器提供的基於 CXL 的 KV 快取，創造出新的叢集記憶體層級，以補充現有的高頻寬記憶體（HBM）與系統 DRAM，速度是基於 NVMe 的 10 倍。這為卸載 KV 資料提供了新的彈性，以加快存取速度

與 NVIDIA Dynamo 相容性：此解決方案相容於 NVIDIA Dynamo，NVIDIA 用於 KV 快取記憶體卸載的軟體架構

成本效益與能源效率：伺服器透過增加大型記憶體池，使組織能最大化 GPU 的有效利用，並透過調整 GPU 與記憶體的大小來優化叢集。此外，該解決方案運作效率高，耗電量低於同等 GPU 伺服器

https://www.hpcwire.com/off-the-wire/penguin-solutions-introduces-industrys-first-production-ready-cxl-based-kv-cache-server/
