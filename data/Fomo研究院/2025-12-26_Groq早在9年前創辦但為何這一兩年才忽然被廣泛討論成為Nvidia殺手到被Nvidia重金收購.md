---
post_id: "122165836460771552"
title: "Groq早在9年前創辦，但為何這一兩年才忽然被廣泛討論，成為「Nvidia殺手」？到被Nvidia重金「收購」？"
page_title: "Fomo研究院"
requested_url: "https://www.facebook.com/profile.php?id=61573146584049"
final_url: "https://www.facebook.com/people/Fomo%E7%A0%94%E7%A9%B6%E9%99%A2/61573146584049/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0Rzm7QSWamjrwd49CKVB1WPpXCiPbqeQ7T44meqH26LoHG7vwvCznJxwVWGnu7BR7l&id=61573146584049"
creation_time_utc: "2025-12-26T12:19:05+00:00"
fetched_at_utc: "2026-05-04T08:42:23.231444+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/605785751_122165836436771552_905640079186725322_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=7b2446&_nc_ohc=EpqhlON5LJAQ7kNvwF4BMHL&_nc_oc=AdrzlikwhJtrxenMAsvQ62vIFsH-Iagjey_1A0ETnZib7Xs16qEHkZNMaz96Cka8_5Y&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=7igOQNN-J3vxUjsNr82QDg&_nc_ss=78100&oh=00_Af50_hv9Qanv975ZW-42hz-UFFmz9qw5s3dCE_MdqDDYRQ&oe=69FE26BF"
feedback_id: "ZmVlZGJhY2s6MTIyMTY1ODM2NDYwNzcxNTUy"
page_canonical_url: "https://www.facebook.com/people/Fomo%E7%A0%94%E7%A9%B6%E9%99%A2/61573146584049/"
---

# Groq早在9年前創辦，但為何這一兩年才忽然被廣泛討論，成為「Nvidia殺手」？到被Nvidia重金「收購」？

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0Rzm7QSWamjrwd49CKVB1WPpXCiPbqeQ7T44meqH26LoHG7vwvCznJxwVWGnu7BR7l&id=61573146584049

![Groq早在9年前創辦，但為何這一兩年才忽然被廣泛討論，成為「Nvidia殺手」？到被Nvidia重金「收購」？](https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/605785751_122165836436771552_905640079186725322_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=7b2446&_nc_ohc=EpqhlON5LJAQ7kNvwF4BMHL&_nc_oc=AdrzlikwhJtrxenMAsvQ62vIFsH-Iagjey_1A0ETnZib7Xs16qEHkZNMaz96Cka8_5Y&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=7igOQNN-J3vxUjsNr82QDg&_nc_ss=78100&oh=00_Af50_hv9Qanv975ZW-42hz-UFFmz9qw5s3dCE_MdqDDYRQ&oe=69FE26BF)
Groq早在9年前創辦，但為何這一兩年才忽然被廣泛討論，成為「Nvidia殺手」？到被Nvidia重金「收購」？
​
2016 年，當 TPU之父Jonathan Ross 離開 Google 創立 Groq 時，他給自己的新發明取了一個看似狂妄的名字：LPU (Language Processing Unit，語言處理單元)。
​
在當時，這簡直是行銷上的自殺。那一年，AI 的主流戰場是圖像識別（ImageNet），而不是語言。
​
大語言模型（LLM）的概念還處於嬰兒期，將晶片命名為「語言處理單元」，就像在汽車剛發明時，宣稱自己造了一架「飛機」一樣，既超前又令人困惑。
​
Groq做了一個在當時看來極其冒險的硬體決策：拋棄 HBM（高頻寬記憶體），全押 SRAM（靜態隨機存取記憶體）。
​
這是一個關於「容量」與「速度」的終極取捨。
​
▋Nvidia的選擇 (HBM)
​
這就像是一輛巨大的貨車。它能裝載海量的貨物（數據），一次可以運送 80GB 甚至更多的模型權重。
​
但它的缺點是，貨車裝卸貨很慢，而且倉庫（記憶體）離工廠（計算核心）有一段距離，數據傳輸存在物理瓶頸。
​
▋Groq 的選擇 (SRAM)： 
​
這就像是一輛法拉利跑車。它的後備箱非常小（單個晶片只有 230MB 容量），裝不了多少東西。
​
但它的速度快得驚人。Groq 將 SRAM 直接鋪在計算核心旁邊，數據傳輸速度達到了驚人的 80TB/s——這是Nvidia HBM 速度的 10 倍以上。
​
這就是 LPU 速度神話的物理基礎。在 LPU 上，數據不需要在倉庫和工廠之間來回奔波，它就在手邊。
​
然而，這也是 Groq 早期最大的軟肋。
​
因為 SRAM 非常昂貴且佔空間，單顆 LPU 無法裝下任何現代的大型 AI 模型。
​
要運行一個大模型，你需要將數百顆 LPU 連接在一起，讓它們像一個巨型大腦一樣協同工作。
​
在 2016 年到 2022 年間，這被視為一種極其不經濟的架構。
​
「為什麼我要買 500 顆晶片來跑一個模型，而Nvidia的一顆晶片就能裝下？」這是當時投資人和客戶最常問的問題。
​
▋孤獨的先知
​
在 ChatGPT 爆發之前的歲月裡，Groq 是一個孤獨的異類。
​
當時的 AI 市場由「訓練」主導。訓練需要的是吞吐量（Throughput），是讓貨車一次拉最多的貨。Nvidia的 GPU 是為此而生的王者。
​
而 Groq 專注的是「推理」的延遲（Latency），也就是法拉利送貨的速度。那時，沒有人需要法拉利。
​
大家都在做離線的數據分析，晚上把數據丟進去，第二天早上看結果，快一秒慢一秒根本沒人在乎。
​
在這段時間中，根本沒人關心推理。投資人看不懂為什麼要追求極致的低延遲，客戶也不在乎 0.2 秒和 1 秒的區別。
​
Groq 曾數次瀕臨破產，Ross 甚至不得不自掏腰包維持公司運轉。
​
Jonathan Ross 和他的團隊在沒有掌聲的舞台上堅持了八年。他們被嘲笑為「偏科生」，被質疑技術路線走進了死胡同。他們製造了一把屠龍刀，卻發現世界上只有殺雞的需求。
​
直到 2022 年底，OpenAI 發布了 ChatGPT。
​
一夜之間，世界變了。AI 不再是後台的批處理任務，變成了前台的即時對話。用戶開始在乎每一個字的生成速度。延遲成為了新的痛點。
​
Groq 等待的風，終於來了。
​
這家「離經叛道」的公司，終於迎來它命運的轉折點。
​
而這筆交易的重要性，當然不止於此。我在聖誕節趕工了一整天，寫好了篇Nvidia「收購」Groq的深入分析，看完全文後，你會對這筆交易的戰略價值有不同的理解。
​
這篇萬多字的深入分析將會限時免費48小時，有興趣的朋友，到我Substack訂閱我的電子報，就可以閱讀完整分析。
​
- KP
