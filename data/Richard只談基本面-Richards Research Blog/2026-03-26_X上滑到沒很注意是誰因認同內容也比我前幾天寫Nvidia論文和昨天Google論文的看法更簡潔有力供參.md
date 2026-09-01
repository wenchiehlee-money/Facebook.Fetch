---
post_id: "1464952268654808"
title: "X上滑到沒很注意是誰因認同內容也比我前幾天寫Nvidia論文和昨天Google論文的看法更簡潔有力供參"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0suBwtWMjFRwGsJVKr3W6MKVC16rAk29Tt8hRqDFK11F2AfHfXoqMhpiV1Mm5nDJSl&id=100054201473657"
creation_time_utc: "2026-03-26T13:13:12+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ2NDk1MjI2ODY1NDgwOA=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# X上滑到沒很注意是誰因認同內容也比我前幾天寫Nvidia論文和昨天Google論文的看法更簡潔有力供參

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0suBwtWMjFRwGsJVKr3W6MKVC16rAk29Tt8hRqDFK11F2AfHfXoqMhpiV1Mm5nDJSl&id=100054201473657
X上滑到沒很注意是誰因認同內容也比我前幾天寫Nvidia論文和昨天Google論文的看法更簡潔有力供參

前沿模型商已沒人用FP16做KV Cache了，TurboQuant論文8X算力/6X記憶體比較的是不存在的對手，改進幅度有限(如以FP4到3 bits就是改進25%)，這點昨天我是推測而此文作者確認，還不包括前沿模型商自研未公開的許多KV Cache壓縮方法

---------"The market is worried about memory because of  $GOOGL's TurboQuant compression of the KV Cache shows you how little investors know about specific technical changes and what they actually mean. Some of my thoughts on this topic:

1. The TurboQuant concept is not new; it was already published one year ago as an arXiv (April 2025). 

2. The paper has benchmarked the 8x performance increase in computing attention when there is an FP32 setup and a 6x memory reduction assessment on the FP16 baseline. Frontier AI labs do not run FP32/FP16 KV cache for inference in production today. Most of the inference on leading AI labs is run on FP8, some even FP4, so the claimed savings on HBM are much lower if you compare them to actual current productions. Also, every frontier AI lab is already compressing their KV cache as much as they can before this paper was published (this is nothing new in terms of the direction of the market). So the savings compared to what is being used mostly today are smaller than the 8x and 6x numbers.

2. When we get some savings on memory (they are happening all the time, through different iterations), we get better models that are able to serve a bigger context window. The difference in quality between a model with a 1M context window and a smaller context window model is enormous. This time will be no different; usage will grow even more as a result of this, as models get better and are able to have bigger context windows, and HBM demand will continue to grow (even for inference, where these optimizations are taking place).

4. Funny enough, with DeepSeek's Multi-head Latent Attention introduction (back in Jan 2025), the KV cache was compressed by a lot more than this and still resulted in drastically more memory demand."

https://x.com/RihardJarc/status/2037134084833464492?s=20
