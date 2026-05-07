---
post_id: "1494434615706573"
title: "本週NAND SSD大廠Samsung和Sandisk的財報會議，都提到Inference長上下文KV Cache需求爆發對SSD需求的正面影響"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02sWT3J75FBPFC3kT8bNQg6Ej8HkQMUdrAsw8ePq9do4MCwNMDxeG51xLPyeqYDjWCl&id=100054201473657"
creation_time_utc: "2026-05-01T10:55:20+00:00"
fetched_at_utc: "2026-05-07T03:35:16.641470+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ5NDQzNDYxNTcwNjU3Mw=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 本週NAND SSD大廠Samsung和Sandisk的財報會議，都提到Inference長上下文KV Cache需求爆發對SSD需求的正面影響

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02sWT3J75FBPFC3kT8bNQg6Ej8HkQMUdrAsw8ePq9do4MCwNMDxeG51xLPyeqYDjWCl&id=100054201473657
本週NAND SSD大廠Samsung和Sandisk的財報會議，都提到Inference長上下文KV Cache需求爆發對SSD需求的正面影響

Samsung說到因應關鍵值快取KV cache儲存需求上升，計畫以PCIe Gen 6 Server SSD推出市場， 提到GTC 大會上Nvidia提出了CMX架構，將AI Inference資料儲存從HBM擴展到NAND儲存，而非僅依賴HBM，很可能帶動對高效能儲存的需求，例如基於TLC的PCIe Gen 6 SSD

Sandisk說到推論優化如KV cache，以及像RAG這類工作負載，都需要大量高效能、低延遲的Flash記憶體，才能提供即時反應速度與高品質的使用者體驗。這些工作負載擴大資料量，因為系統必須保留上下文、中間資料及大型外部資料集。因此，NAND成為唯一經濟可行的解決方案......考慮到推論架構以及前面關於KV cache的重要性，以及它能根據你對使用情境的假設大幅擴展，對TLC的需求非常非常強烈

去年Nvidia針對長上下文KV cache的分層儲存提出增加G3.5層級的ICMS SSD Rack，今年改進稱為CMX平台，導入Pod內SSD Rack提高KV Cache分層卸載offload策略，一直以來有專業人士認為SSD速度太慢不足以應付KV Cache在推論中所需極頻繁存取需求，但是之前Nvidia和如今的Samsung、Sandisk卻都確認KV Cache暴增大幅促進了SSD的需求，這是怎麼回事呢?

我想關鍵在於，不是讓推論時直接將SSD取代HBM來使用，而是使用"卸載策略"，透過軟體演算法將整批的、整塊的KV Cache，依照使用頻率分層儲存，從G1 HBM、G2 DRAM、G3 Local SSD、G3.5 SSD Rack、G4 Network SSD/HDD，推論程式不是直接從GPU去存取路程遙遠速度又慢的SSD上的KV cache，而是透過分層卸載演算法，在G1~G4之間搬動整大塊KV Cache到HBM，從DRAM/SSD將少用的KV cache搬到HBM，再執行頻繁存取的KV cache推論任務

Nvidia的NIXL函式庫和Dynamo軟體是調動各層KV Cache的工具

如果不加SSD Rack，將AI server內部local SSD全換成大於200TB的大容量SSD，應該也有幫助


---
[📌 新增貼文至TAIEX.TW比對](https://github.com/wenchiehlee-money/TAIEX.TW/issues/new?template=earnings_tag.yml&title=2026%20%20%E8%B2%A1%E5%A0%B1%E6%A8%99%E8%A8%98&symbol=2026&file_path=data%2FRichard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards%20Research%20Blog%2F2026-05-01_%E6%9C%AC%E9%80%B1NAND-SSD%E5%A4%A7%E5%BB%A0Samsung%E5%92%8CSandisk%E7%9A%84%E8%B2%A1%E5%A0%B1%E6%9C%83%E8%AD%B0%E9%83%BD%E6%8F%90%E5%88%B0Inference%E9%95%B7%E4%B8%8A%E4%B8%8B%E6%96%87KV-Cache%E9%9C%80%E6%B1%82%E7%88%86%E7%99%BC%E5%B0%8DSSD%E9%9C%80%E6%B1%82%E7%9A%84%E6%AD%A3%E9%9D%A2%E5%BD%B1%E9%9F%BF.md&period=)
