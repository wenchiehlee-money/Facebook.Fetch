---
post_id: "1597026322114068"
title: "SambaNova強調模型頻寬利用率(MBU)，除此之外，其各種規格、技術、架構，以2026年的標準來說是出奇的老舊，HBM2e、傳統慢速Ethernet當Scale Up Network(並非新的ESUN)，而且每套SN50系統還必須和Nvidia的H200搭配使用(連這個也不更換到B200?)，不知道Intel是要如何和SambaNova合作?"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid033NZGZkToo4xCY9kY9x5Q6uQnEY2oKw1oYHVEpoRiXVd68REZUUx2omPBu4Au2XVFl&id=100054201473657"
creation_time_utc: "2026-08-29T10:26:31+00:00"
fetched_at_utc: "2026-08-30T06:31:53.662955+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid033NZGZkToo4xCY9kY9x5Q6uQnEY2oKw1oYHVEpoRiXVd68REZUUx2omPBu4Au2XVFl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU5NzAyNjMyMjExNDA2OA=="
page_canonical_url: ""
---

# SambaNova強調模型頻寬利用率(MBU)，除此之外，其各種規格、技術、架構，以2026年的標準來說是出奇的老舊，HBM2e、傳統慢速Ethernet當Scale Up Network(並非新的ESUN)，而且每套SN50系統還必須和Nvidia的H200搭配使用(連這個也不更換到B200?)，不知道Intel是要如何和SambaNova合作?

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid033NZGZkToo4xCY9kY9x5Q6uQnEY2oKw1oYHVEpoRiXVd68REZUUx2omPBu4Au2XVFl&id=100054201473657
SambaNova強調模型頻寬利用率(MBU)，除此之外，其各種規格、技術、架構，以2026年的標準來說是出奇的老舊，HBM2e、傳統慢速Ethernet當Scale Up Network(並非新的ESUN)，而且每套SN50系統還必須和Nvidia的H200搭配使用(連這個也不更換到B200?)，不知道Intel是要如何和SambaNova合作? 

------------"頻寬利用率常被誤解。SambaNova 正在說明他們在這次演講中的意義。簡言之，他們談論的不是HBM頻寬的使用量，而是模型頻寬利用率（MBU）模型。具體來說，這些數據中有多少比例用於快取資料或處理資料使用。
......
FLOPS 數量是 SN40 的 5 倍，且設計上可擴展至更大的 256+ 晶片領域。還有一個獨立的擴展網路，使用 400Gb 網路。

值得注意的是，這裡沒有 I/O 晶片或類似的裝置。相反地，邏輯只有兩個最大準星晶片，記憶體則是 HBM 堆疊。

不過有趣的是，SambaNova 在這裡選擇的 HBM 其實相當過時;SN50 在這裡仍然使用 HBM2e（未來隨著記憶體生產量減少，這會成為問題）。
......
SN50 性能的關鍵在於重疊。SN50 支援所有形式的模型平行性，以及這些模型所建立的集體通訊形式。
......
若要超過 8 個插座，則會使用乙太網路交換器進行擴展網路。連結是分組的，每個節點都連接到這 64 顆晶片插槽配置中的兩個交換器。
......
最終，SambaNova 推廣的形象與其他專門推理晶片公司非常相似，使用一種晶片進行預填充（及中填充），而解碼則使用獨立的加速器（例如 SN50）。具體來說，他們一直使用 NVIDIA H200 + SN50，並使用 RoCE 來進行兩者之間的傳輸。"

https://www.servethehome.com/sambanovas-sn50-rdu-for-ai-at-hot-chips-2026/
