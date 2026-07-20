---
post_id: "1509607230855978"
title: "單一GW的 AI 工廠可能需要高達 25 exabytes的Flash memory，才能達到最佳效率， GPU只是一部分，KV cache節省大量GPU運算"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02WdF1FgrV7XWR3wjHWjWwnY8d7Qew9wWKKaEkv8kEcDp85fq6aHgwirVgnFPX4pHHl&id=100054201473657"
creation_time_utc: "2026-05-19T14:05:34+00:00"
fetched_at_utc: "2026-07-20T13:02:55.617710+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTUwOTYwNzIzMDg1NTk3OA=="
page_canonical_url: ""
---

# 單一GW的 AI 工廠可能需要高達 25 exabytes的Flash memory，才能達到最佳效率， GPU只是一部分，KV cache節省大量GPU運算

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02WdF1FgrV7XWR3wjHWjWwnY8d7Qew9wWKKaEkv8kEcDp85fq6aHgwirVgnFPX4pHHl&id=100054201473657
單一GW的 AI 工廠可能需要高達 25 exabytes的Flash memory，才能達到最佳效率， GPU只是一部分，KV cache節省大量GPU運算

----------Nvidia和Solidigm(Hynix group)會談"Storage for the AI Factory Era
......
A New “Middle Tier” of AI Storage To handle this demand, the industry is creating a new tier of storage. Traditionally, systems relied on either extremely fast but expensive Direct Attached Storage (like HBM memory, which costs $10,000 per terabyte) or very high-capacity but slower Network Attached Storage. Flash storage is being used as a tier between those two extremes.

KV Cache Optimizes GPU Performance KV cache has a massive impact on AI Factory performance because it saves a tremendous amount of computation, for example, when ingesting large amounts of data and using it as a source for generating future reports. Since original documents can always be recomputed, this tier of AI storage does not need to strictly adhere to legacy rules requiring perfect durability and fault tolerance, allowing for further design optimizations.
......
Future Outlook of AI Factories In the next three to five years, AI intelligence will be integrated everywhere, resulting in factories of all sizes. That will range from small factory robots and cars to massive gigawatt data centers. A single gigawatt AI factory could require up to 25 exabytes of flash storage to be optimally efficient. Ultimately, the key takeaway is that GPUs are only part of the equation.

During the discussion, Kevin also noted that KV caches are a different tier and type of storage in the data center, fundamentally distinct from other types of storage. KV caches help reduce compute demand in AI clusters, which anyone who has run local models and turned on/off the KV cache can immediately see. These caches need to be high-performance, but from a resilience perspective, if the data is lost, then it can be recomputed. That makes it a different storage tier than most data, which trades speed and latency for resilience.

AI 儲存的新「中間層」為了滿足這個需求，產業正在打造新的儲存層級。傳統上，系統依賴極快速但昂貴的直接附加儲存（Direct Attached Storage，如 HBM 記憶體，價格為每 TB 10,000 美元）或容量極高但速度較慢的網路附加儲存。快閃儲存被用作介於這兩個極端之間的層級。

KV 快取優化 GPU 效能KV 快取對 AI Factory 效能有巨大影響，因為它節省了大量運算，例如在匯入大量資料並將其作為未來報告來源時。由於原始文件可重新計算，此層 AI 儲存不必嚴格遵守要求完美耐久性與容錯性的舊規則，允許進一步優化設計。
......
AI 工廠的未來展望未來三到五年內，人工智慧將全面整合，帶來各種規模的工廠。這些設施將從小型工廠機器人和汽車到超大型吉瓦數據中心不等。單一吉瓦的 AI 工廠可能需要高達 25 艾字節的快閃記憶體，才能達到最佳效率。最終，關鍵結論是 GPU 只是整個方程式的一部分。

在討論中，Kevin 也指出 KV 快取是資料中心中不同層級與類型的儲存，與其他類型的儲存有根本不同。KV 快取有助於降低 AI 叢集的運算需求，任何執行過本地模型並開啟或關閉 KV 快取的人都能立即看到。這些快取必須具備高效能，但從韌性角度來看，如果資料遺失，可以重新計算。這使得它與大多數資料不同的儲存層級，後者是以速度和延遲換取韌性。"

https://www.servethehome.com/storage-for-the-ai-factory-era-solidigm-nvidia-an-interview/
