---
post_id: "1448427830307252"
title: "只聽Broadcom法說沒和產業及NV資料對照的話可能讓人對Nvidia AI擴展網路有些誤解"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0k7H5qsGKf8e3ahEJ3AXBc1kCHWFWsVmWkopjGBf9cvuhH6u6pX5aY9JMUXAwntGjl&id=100054201473657"
creation_time_utc: "2026-03-05T17:07:31+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0k7H5qsGKf8e3ahEJ3AXBc1kCHWFWsVmWkopjGBf9cvuhH6u6pX5aY9JMUXAwntGjl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ0ODQyNzgzMDMwNzI1Mg=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 只聽Broadcom法說沒和產業及NV資料對照的話可能讓人對Nvidia AI擴展網路有些誤解

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0k7H5qsGKf8e3ahEJ3AXBc1kCHWFWsVmWkopjGBf9cvuhH6u6pX5aY9JMUXAwntGjl&id=100054201473657
只聽Broadcom法說沒和產業及NV資料對照的話可能讓人對Nvidia AI擴展網路有些誤解

1. Broadcom搶了Nvidia Scale-Up NVLink的市場?

去年以前，根本沒有高速Scale Up Switch市場，只有Nvidia一家，Google、AWS(PCIe Switch)、AMD、所有ASIC/XPU從大到小到新創都沒有，因為拓樸架構不同，只有Nvidia從第二代A100開始即使只有8顆GPU放UBB上互聯也有6~4顆NVLink Switch晶片構成兩層拓樸，但本版去年六月開始發文，說未來Scale Up Switch將是一個 "全新的" 數百億美元的新市場，因為除了Google以外，所有的GPU/XPU Scale Up互聯都開始兩層拓樸使用Sacle Up Switch，外賣市場幾乎是從無到有，全新的市場，不是說Boradcom進來Nvidia就會少，兩家的Scale Up Switch IC都會大成長

NVLink Switch自己成長以外，對外授權的NVLink Fusion，XPU-to-XPU需要買NVLink Switch晶片，CPU-to-XPU的CPU客戶只要買IP或chiplet，CPU-to-XPU的XPU客戶要買chiplet

2.  Ethernet入侵Scale Up市場?

對的，但這就是Broadcom採取的產品方向SUE/ESUN，去年本版已經寫過多次Broadcom Ethernet基礎的Scale Up Switch產品，這次法說不是新的東西，相信有追蹤的人都知道這過去一年的發展

3. Scale Out/Networking由Ethernet成為主流，將侵蝕Nvidia的IB市場?

Ethernet已成Scale Out網路的主流技術，這是對的，但這也是大家都知道的事情，一年前就底定這個趨勢了， Nvidia當然也知道，所以Nvidia這兩年也不斷發展Ethernet網路Spectrum X產品線，Nvidia自己的Ethernet Switch(Spectrum X產品線)業績也經超過Infiniband Switch(Quantum X產品線)的業績

就是說， Nvidia的IB被侵蝕沒錯，但Nvidia並不一定被侵蝕，因為NV的Ethernet Switch大成長，我覺得隨著 "搭售"、GPU共同推廣Spectrum X Ethernet Switch，Scale Out Switch市場Nvidia的市佔率今年不但沒有被侵蝕更有可能是提升的，只是不是IB而是Ethernet，Nvidia自己已經比市場提早完成了IB到Ethernet的轉移布局，加上市場大餅隨AI高速成長，IB不會消失，雙軌並行但偏特定需求市場

AI Scale Out Switch無疑市場大成長，Broadcom和Nvidia都會成長，而且Nvidia市佔率未必下滑(我沒數字)，因為NV Spectrum X Switch比別人的Ethernet Switch貴，產量和產值市佔率可能不同

例如前陣子Nvidia力推的ICMS(Inference Context Memory Storage)就是搭配自家的Spectrum X Ethernet Switch而不是IB Switch
