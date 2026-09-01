---
post_id: "1455904229559612"
title: "Disaggregated Inference(P/D Inf.)已成推論主流方法，AWS和Cerebres合作，Prefiller用AWS Trainium XPU，Decoder用Cerebras CS-3，KV Cache使用AWS專用的EFA NIC Ethernet傳輸"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02B7UmYL2hKS482rebxGZBGUWtuDSXJFfxUXUwgoo9qcsFfRyEsoQAZFj55TM4Zs1Al&id=100054201473657"
creation_time_utc: "2026-03-15T17:19:27+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02B7UmYL2hKS482rebxGZBGUWtuDSXJFfxUXUwgoo9qcsFfRyEsoQAZFj55TM4Zs1Al&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ1NTkwNDIyOTU1OTYxMg=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# Disaggregated Inference(P/D Inf.)已成推論主流方法，AWS和Cerebres合作，Prefiller用AWS Trainium XPU，Decoder用Cerebras CS-3，KV Cache使用AWS專用的EFA NIC Ethernet傳輸

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02B7UmYL2hKS482rebxGZBGUWtuDSXJFfxUXUwgoo9qcsFfRyEsoQAZFj55TM4Zs1Al&id=100054201473657
Disaggregated Inference(P/D Inf.)已成推論主流方法，AWS和Cerebres合作，Prefiller用AWS Trainium XPU，Decoder用Cerebras CS-3，KV Cache使用AWS專用的EFA NIC Ethernet傳輸

1. 本版之前推測(1)Prefiller和Decoder可以不同的晶片異質合作，因為是透過Scale out Etherent傳輸KV cache，被證實了，(2)談Nvidia CPX Rack的時候認為獨立CPX機櫃搭配VR NVL72機櫃(而不是固定8:8的VR CPX NVL混合機櫃)，可視不同工作負載達到Prefiller:Decoder彈性數目配置，PxDy的x和y可自由配置，是比較好的方案，被證實了，兩家公司新聞稿有提到 "different prefill/decode ratios"

2. 這是Nvidia的威脅，之前Cerebras有許多弱點不成威脅，現在AWS Trainium Prefiller + Cerebras CS-3 Decoder，解決了Cerebras的一些弱點例如VRAM不夠大，將成Nvidia的威脅，NV要加快腳步推出自己的solution，雖然之前有Rubin CPX方案，還沒量產而且還有更動的消息(例如GDDR7改HBM或更換為LPX?)，AWS + Cerebras是現成機種，已經可以佈署，客戶可能要寫兩種軟體分別控制Trainium和Cerebras?

----------"在拆分模式下，Trainium 專注於預填工作。它會計算 KV 快取，並透過亞馬遜的高速 EFA 互連傳送到 WSE。Cerebras WSE 會根據結果專門執行解碼，每秒產生數千個輸出標記，而 GPU 則需數百個。此架構充分發揮各處理器的優勢，為 AWS 客戶帶來 5 倍的高速令牌量提升。
In disaggregated mode, Trainium focuses exclusively on prefill work. It computes the KV cache and sends it to the WSE via Amazon's high-speed EFA interconnect. The Cerebras WSE takes the result and exclusively performs decode, generating thousands of output tokens per second versus hundreds on GPUs. 
........
大多數客戶會混合使用不同預填充/解碼比例的工作負載，傳統聚合方式仍是理想選擇。我們預期大多數客戶會想要兩者的存取權，並能將工作負載路由到最適合他們的配置。
Disaggregated is ideal when you have large, stable workloads. Most customers run a mix of workloads with different prefill/decode ratios, where the traditional aggregated approach is still ideal. We expect most customers will want access to both and the ability to route workloads to whichever configuration serves them best."
