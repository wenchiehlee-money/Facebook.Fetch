---
post_id: "1488448539638514"
title: "針對agentic AI和multi-agent工作負載的AI資料中心，到底CPU和GPU的搭配比例會多少?  Intel沒有給明確的答案，但是方向性很清楚，數量比例上，大幅度地往CPU移動(1:1?)"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0wUSvPP5sbcNwNia9NECokuoXZGUyMjryUQhKBM388B9si9EtVKxyqMnAJoutGcTWl&id=100054201473657"
creation_time_utc: "2026-04-24T13:47:12+00:00"
fetched_at_utc: "2026-05-07T03:35:16.641470+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ4ODQ0ODUzOTYzODUxNA=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 針對agentic AI和multi-agent工作負載的AI資料中心，到底CPU和GPU的搭配比例會多少?  Intel沒有給明確的答案，但是方向性很清楚，數量比例上，大幅度地往CPU移動(1:1?)

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0wUSvPP5sbcNwNia9NECokuoXZGUyMjryUQhKBM388B9si9EtVKxyqMnAJoutGcTWl&id=100054201473657
針對agentic AI和multi-agent工作負載的AI資料中心，到底CPU和GPU的搭配比例會多少?  Intel沒有給明確的答案，但是方向性很清楚，數量比例上，大幅度地往CPU移動(1:1?)

有趣的是一位分析師提出這個Agentic AI時代CPU TAM的問題，因為他不知道如何建立財務模型，這是常見的現象，一個趨勢起來，或者一個趨勢反轉的時候，有某一個早期時段，無法 "清楚" 描繪未來的輪廓，包含廠商本身

AI模型變化->AI應用變化->軟體->硬體工作負載變化>各種硬體的TAM的變化

過去半年很明顯是Agentic AI起來，啟動了第四個Scaling Law (Pre-training, Post-training, Test-time compute/reasoning, Agentic AI)，讓CPU(+主記憶體)需求暴增，如果在需求訊息鏈領先的前沿模型公司如Anthropic都無法預期到coding和agentic AI需求暴增的起點和斜率(所以才會算力不夠降速降智)，後面的硬體廠商又如何知道? 這個時候，拚的是內心的成長斜率圖(包含時間)，什麼東西的知識/資訊/判斷可影響這個成長斜率圖? 還是源頭(模型、應用)比尾巴重要(forecast、訂單)

分析師說不會建財務模型，就是說這種時候他的報告的數字部分，就不用太在意了

----------"客戶正將伺服器 CPU 部署於加速器旁，且比例正逐漸回歸 CPU，加速器仍是 Frontier AI 的核心，我們將繼續參與、創新並合作
Xeon server demand is seeing strong and sustained momentum. Customers are deploying server CPUs along accelerators in the ratio that is moving back towards CPU. The accelerator remains central to Frontier AI, and we will continue to participate, innovate and partner in that category.
......
過去 90 天來，我們對伺服器 CPU 需求展望有所改善，預期產業及我們自身將迎來雙位數單位強勁成長，動能將延續至 2027 年。
......
推論方面，我認為在協調、控制平面以及管理各種不同的代理資料方面，CPU 效率高得多。所以我認為 CPU 與 GPU 的比例以前是 1 和 8，現在是 1：4，我認為是接近同偶校驗甚至更好的方向。所以我認為需求非常強勁。 Inference side, I think in terms of orchestration, control plane and also managing all the different agent with data, CPU is much more efficient. So I think the ratio of CPU to GPU used to be 1 and 8, and now it's 1:4 and I think towards parity or even better. So I think the demand is very strong.
......
我們認為單位數量會是最大的推手。這是以每核心ASP的比例計算。顯然，資料中心CPU的核心數量正在顯著增加。因此，隨著核心數量增加，ASP數量也會被提升，這顯然是有意義的。
......
Joshua Buchalter
TD Cowen, Research Division

Congrats on the very strong numbers. Actually, I wanted to follow up on Vivek's question from earlier. You gave some metrics on the near-term CPU TAM. But I think investors are directionally really struggling with how to model the CPU demand for agentic workloads. Any help you can provide us longer term about how we should think about growth, whether in terms of units, cores, gigawatts, CapEx? Just anything you can give us? I mean, but bluntly, is the $100 billion number that ARM gave reasonable in your view?

我認為我們關注的一個統計數據是 CPU 與 GPU 的比例。如果你看訓練解決方案，通常運行在 7 到 8 個 GPU 對 1 個 CPU 之間。當我們探討推論時，可能會進入 3 到 4：1 的比例。當你進入代理和多代理時，甚至可能稍微反過來。這也是一種思考方式。
 I think one statistic that we look at is the ratio of CPUs to GPUs. And if you look at training solutions, they're generally running in the kind of 7 to 8 GPUs to 1 CPU. As we look into inference, it's probably getting into like the 3 to 4:1 kind of level. And as you get into agentic and multi-agent, it's one potentially even flip in the other direction a little bit"
......
CPU 如何優化與基礎模型合作，如何優化這些數據，真正推動代理人工智慧的巨大機會。我認為推論市場會更大，實體人工智慧也是另一個大市場。所以我認為這對我們來說是一個機會。雖然很難量化
And so you addressed some of this agentic AI and later on the physical AI, how the CPU optimize working together with the foundation models, how to optimize that and using the data to really drive the massive opportunity in the agentic AI. I think the inference is going to be a much bigger market and the physical AI is another big market. So I think that's an opportunity for us. And it's hard to quantify.


---
[📌 新增貼文至TAIEX.TW比對](https://github.com/wenchiehlee-money/TAIEX.TW/issues/new?template=earnings_tag.yml&title=MU%20%20%E8%B2%A1%E5%A0%B1%E6%A8%99%E8%A8%98&symbol=MU&file_path=data%2FRichard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards%20Research%20Blog%2F2026-04-24_%E9%87%9D%E5%B0%8Dagentic-AI%E5%92%8Cmulti-agent%E5%B7%A5%E4%BD%9C%E8%B2%A0%E8%BC%89%E7%9A%84AI%E8%B3%87%E6%96%99%E4%B8%AD%E5%BF%83%E5%88%B0%E5%BA%95CPU%E5%92%8CGPU%E7%9A%84%E6%90%AD%E9%85%8D%E6%AF%94%E4%BE%8B%E6%9C%83%E5%A4%9A%E5%B0%91-Intel%E6%B2%92%E6%9C%89%E7%B5%A6%E6%98%8E%E7%A2%BA%E7%9A%84%E7%AD%94%E6%A1%88%E4%BD%86%E6%98%AF%E6%96%B9%E5%90%91%E6%80%A7%E5%BE%88%E6%B8%85%E6%A5%9A%E6%95%B8%E9%87%8F%E6%AF%94%E4%BE%8B%E4%B8%8A%E5%A4%A7.md&period=)
