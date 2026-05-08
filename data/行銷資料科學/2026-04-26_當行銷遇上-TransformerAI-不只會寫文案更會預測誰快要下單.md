---
post_id: "1265577452352564"
title: "【當行銷遇上 Transformer：#AI 不只會寫文案，更會預測誰快要下單】"
page_title: "行銷資料科學"
requested_url: "https://www.facebook.com/MarketingDataScienceTMR"
final_url: "https://www.facebook.com/MarketingDataScienceTMR"
post_url: "https://www.facebook.com/MarketingDataScienceTMR/posts/pfbid01S7j2LusiJiJhfG86iwKz42VW4BMb7p6inVLk76SJLCexXZvY4kLM2bZ8GxFg32Bl"
creation_time_utc: "2026-04-26T14:00:52+00:00"
fetched_at_utc: "2026-05-07T04:01:50.086552+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/676822862_1261529482757361_8795569937195854018_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=104&ccb=1-7&_nc_sid=13d280&_nc_ohc=U7MkbhJPNkEQ7kNvwE84arP&_nc_oc=Adp3CcXVONcgzwjYw-72Eatg3w6n9G4Nauyn0VWi_fIAxnPx19Ezyyv95ytE3JbClwM&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=oCDdcLhWt0_ikVexvT3XZA&_nc_ss=78100&oh=00_Af7N0yEFEhwcVRXZKoU7xXNFfc7E_3xSMAvJm1qT5lu9hw&oe=6A01CEDC"
feedback_id: "ZmVlZGJhY2s6MTI2NTU3NzQ1MjM1MjU2NA=="
page_canonical_url: "https://www.facebook.com/MarketingDataScienceTMR"
---

# 【當行銷遇上 Transformer：#AI 不只會寫文案，更會預測誰快要下單】

原文連結: https://www.facebook.com/MarketingDataScienceTMR/posts/pfbid01S7j2LusiJiJhfG86iwKz42VW4BMb7p6inVLk76SJLCexXZvY4kLM2bZ8GxFg32Bl

![【當行銷遇上 Transformer：#AI 不只會寫文案，更會預測誰快要下單】](https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/676822862_1261529482757361_8795569937195854018_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=104&ccb=1-7&_nc_sid=13d280&_nc_ohc=U7MkbhJPNkEQ7kNvwE84arP&_nc_oc=Adp3CcXVONcgzwjYw-72Eatg3w6n9G4Nauyn0VWi_fIAxnPx19Ezyyv95ytE3JbClwM&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=oCDdcLhWt0_ikVexvT3XZA&_nc_ss=78100&oh=00_Af7N0yEFEhwcVRXZKoU7xXNFfc7E_3xSMAvJm1qT5lu9hw&oe=6A01CEDC)
【當行銷遇上 Transformer：#AI 不只會寫文案，更會預測誰快要下單】
這幾年談到 AI，很多企業最先想到的，往往還是寫文案、做圖片、建置客服機器人🤖。

但一篇發表在 2026 年《行銷研究期刊》（Journal of Marketing Research）的論文提醒我們，AI 更強大的地方，可能不是「生成內容」，而是「讀懂行為」。

因為在行銷世界裡，真正困難的問題，常常不是寫出一句吸引人的話💬，而是看懂顧客在一連串點擊、搜尋、開信、造訪之後，究竟是不是正在一步步走向購買。

這篇論文〈顧客旅程的人工智慧分析：一種 Transformer 方法〉（AI for Customer Journeys: A Transformer Approach）的出發點很清楚：現在的顧客旅程，早就不是一條直線，而是由許多接觸點交錯組成🧩。

有人先看到電子郵件（email），再去搜尋，接著點了展示廣告，最後直接進網站下單；也有人先逛官網，隔幾天再回來，過了很久才完成購買。問題在於，企業過去常常只看最後一次接觸，卻忽略了前面那一整串互動，才是真正慢慢推動成交的關鍵🗝️。

這篇研究最巧妙的地方，在於它把顧客旅程想成一句話。對大型語言模型來說，一句話是由很多單字組成；而在這篇研究裡，一段顧客旅程則是由很多接觸點組成。

一次電子郵件點擊、一次搜尋、一次展示廣告曝光、一次直接造訪，都像句子裡的一個字。只有把前後順序一起看，AI 才能知道這個「字」在整段旅程中真正代表什麼。這也是作者選擇用 Transformer 的原因：因為它很擅長處理序列，也很擅長理解前後文。

在研究方法上，作者並不是直接把現成模型搬來使用，而是針對行銷問題做了調整。他們以 Transformer 為核心，設計出一套可以同時從不同角度理解同一段顧客旅程的架構，也就是「多頭自注意力機制」（multi-head self-attention）。

更進一步，他們還把顧客之間的差異放進模型裡，不假設所有人的決策邏輯都一樣，而是允許不同顧客有不同的注意力重點：有些人比較容易被電子郵件推動，有些人則是在自己主動搜尋🔎時，才真正接近購買。

在資料上，作者使用一家飯店業者的真實數據，包含 92,575 位顧客、546,745 次網站造訪，以及 102,375 筆交易。資料涵蓋13種不同來源的流量，例如：直接流量（direct）、自然搜尋（natural search）、付費搜尋（paid search）、電子郵件（email）、展示廣告（display）等，並將三個月資料切成每 12 小時一格的時間序列，追蹤顧客在不同時間經過哪些接觸點，最後是否完成預訂。

結果很明顯。這套模型在預測購買上表現非常強。研究發現，這個 Transformer 模型可以在前 40% 的高潛力顧客中，抓到 100% 的實際轉換者，而其他模型做不到這件事。這代表企業若用這套方法做名單篩選，就更有機會把資源集中在真正快要下單的人身上，而不是平均撒出去。

這篇研究還有幾個很有意思的發現：

1.長期記憶的價值很重要

很多傳統模型比較擅長看短期訊號，但 Transformer 能把更早之前的互動也一起考慮進來，因此更容易抓到那些「很早就埋下，後面才發酵」的關鍵訊號。換句話說，有些接觸點當下看起來沒什麼，但放回整段旅程中，它可能是非常重要的前奏。

2.不同接觸的影響不一樣

例如，直接造訪（direct visit）的影響通常最強，尤其越接近購買時效果越大；而電子郵件（email）、付費搜尋（paid search）這類企業主動發起的接觸，效果通常比較短，也更吃時機。這代表同樣是接觸點，價值並不一樣，出現的時間也很重要。

3.單次旅程也能有效預測

這點特別重要，因為很多企業最想解決的，正是「新客資料少，怎麼判斷誰有機會成交」這個問題。該研究顯示，就算沒有很長的歷史資料，模型仍然有機會從有限的互動序列中，看出哪些人更接近轉換。

最後是這篇研究帶來的幾個管理意涵：

1.不要再只看最後點擊歸因。顧客不是因為最後一個廣告才下單，而是被整段旅程一步一步推向成交。

2.我們需要重新理解「黃金打擊👊時間」。不是越早投、越多投就越好，而是要在顧客真正接近決策時，剛好出現在他面前。

3.企業應該把 AI 用在找高潛力顧客，而不只是拿來自動生成內容。對行銷管理者來說，預測誰快要買，很多時候比多寫一篇文案更有商業價值。

4.未來如果企業有更完整的行銷行動資料，這類模型不只可以預測誰會買，還能進一步幫助我們測試：不同時間、不同接觸、不同策略，究竟哪一種更值得投。

總結來說，這篇研究最值得記住的一句話是：別再把 Transformer 只當成聊天機器人的心臟，它也可以是企業行銷的大腦🧠。當我們開始把點擊、搜尋、造訪、開信，當成一串有意義的語言來閱讀，就更有機會真正讀懂顧客的心。

✏️ 作者：羅凱揚（台科大企管系兼任助理教授）、鍾皓軒（臺灣行銷研究有限公司創辦人）

📖 資料來源：Lu, Z., & Kannan, P. K. (2024, January 5). AI for customer journeys: A transformer approach. Journal of Marketing Research. Advance online publication. https://doi.org/10.1177/00222437251347268


---
[📌 新增貼文至TAIEX.TW比對](https://github.com/wenchiehlee-money/TAIEX.TW/issues/new?template=earnings_tag.yml&title=2026%20%20%E8%B2%A1%E5%A0%B1%E6%A8%99%E8%A8%98&symbol=2026&file_path=data%2F%E8%A1%8C%E9%8A%B7%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%2F2026-04-26_%E7%95%B6%E8%A1%8C%E9%8A%B7%E9%81%87%E4%B8%8A-TransformerAI-%E4%B8%8D%E5%8F%AA%E6%9C%83%E5%AF%AB%E6%96%87%E6%A1%88%E6%9B%B4%E6%9C%83%E9%A0%90%E6%B8%AC%E8%AA%B0%E5%BF%AB%E8%A6%81%E4%B8%8B%E5%96%AE.md&period=)


---
[📌 新增貼文至biztrends.TW比對](https://github.com/wenchiehlee-money/biztrends.TW/issues/new?template=earnings_tag.yml&title=%E8%B2%BC%E6%96%87%E6%A8%99%E8%A8%98&symbol=&file_path=data%2F%E8%A1%8C%E9%8A%B7%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%2F2026-04-26_%E7%95%B6%E8%A1%8C%E9%8A%B7%E9%81%87%E4%B8%8A-TransformerAI-%E4%B8%8D%E5%8F%AA%E6%9C%83%E5%AF%AB%E6%96%87%E6%A1%88%E6%9B%B4%E6%9C%83%E9%A0%90%E6%B8%AC%E8%AA%B0%E5%BF%AB%E8%A6%81%E4%B8%8B%E5%96%AE.md&period=)
