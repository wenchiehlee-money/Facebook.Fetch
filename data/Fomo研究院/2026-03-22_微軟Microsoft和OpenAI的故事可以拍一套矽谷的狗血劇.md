---
post_id: "122176506632771552"
title: "微軟（Microsoft）和OpenAI的故事，可以拍一套矽谷的狗血劇。"
page_title: "Fomo研究院"
requested_url: "https://www.facebook.com/profile.php?id=61573146584049"
final_url: "https://www.facebook.com/people/Fomo%E7%A0%94%E7%A9%B6%E9%99%A2/61573146584049/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02cr2dezPpc7p33uXJhoaksw3Ytnb9DjQXMJ3GsFQG6yRR7gabRYM9Wb7qEW7q2mh7l&id=61573146584049"
creation_time_utc: "2026-03-22T04:28:34+00:00"
fetched_at_utc: "2026-05-04T08:42:23.231444+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/656619588_122176506608771552_9054717178512802100_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=108&ccb=1-7&_nc_sid=7b2446&_nc_ohc=j8RGHa-QIT0Q7kNvwHP-jzo&_nc_oc=Adp4E4DaBxAh8NrqFnmm1BkQBUxbWNRDrNsP68-iXaeVRDsABGVjA7B3pWOSUcPREA8&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=xHZ7DUeoUIr74ANKHb0Ecg&_nc_ss=78100&oh=00_Af7HkJhDhGBzzddxw8W55clVfjhADQWnwlkJ4ALau3d5KQ&oe=69FE3303"
feedback_id: "ZmVlZGJhY2s6MTIyMTc2NTA2NjMyNzcxNTUy"
page_canonical_url: "https://www.facebook.com/people/Fomo%E7%A0%94%E7%A9%B6%E9%99%A2/61573146584049/"
---

# 微軟（Microsoft）和OpenAI的故事，可以拍一套矽谷的狗血劇。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02cr2dezPpc7p33uXJhoaksw3Ytnb9DjQXMJ3GsFQG6yRR7gabRYM9Wb7qEW7q2mh7l&id=61573146584049

![微軟（Microsoft）和OpenAI的故事，可以拍一套矽谷的狗血劇。](https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/656619588_122176506608771552_9054717178512802100_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=108&ccb=1-7&_nc_sid=7b2446&_nc_ohc=j8RGHa-QIT0Q7kNvwHP-jzo&_nc_oc=Adp4E4DaBxAh8NrqFnmm1BkQBUxbWNRDrNsP68-iXaeVRDsABGVjA7B3pWOSUcPREA8&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=xHZ7DUeoUIr74ANKHb0Ecg&_nc_ss=78100&oh=00_Af7HkJhDhGBzzddxw8W55clVfjhADQWnwlkJ4ALau3d5KQ&oe=69FE3303)
微軟（Microsoft）和OpenAI的故事，可以拍一套矽谷的狗血劇。
​
故事要從 2019 年說起。那時的 OpenAI 還是個燒錢的非營利組織，微軟像是個眼光獨到的「早期投資人」，豪擲十億美金定下盟約。當時的協議很簡單：我給你錢和算力，你給我技術和獨家。
​
然而，隨著 ChatGPT 的爆發式成長，這段關係發生了質變。OpenAI 對算力的胃口變成了「無底洞」，即便強如微軟，也發現自己無法（也不太想）獨自承擔那天文數字般的基礎設施支出。
​
於是，在 2025 年底，雙方重新修訂了「婚前協議」，正式進入了一種「開放式關係」。微軟放棄了對算力的獨家供應權，允許 OpenAI 去外面找別的「乾爹」（如 Oracle、亞馬遜）買算力，前提是微軟依然得是那個「正宮」（核心 API 必須留在 Azure）。
​
但顯然，OpenAI 這次玩得太過火了，直接觸碰了微軟的底線，氣得「正宮」考慮直接法庭見。
​
▋什麼是「有狀態」的技術漏洞？
​
根據微軟與 OpenAI 在 2025 年底更新的合約，微軟的 Azure 擁有 OpenAI 「無狀態 API」（Stateless API） 的全球獨家託管權。簡單來說，如果你只是傳一個指令給 AI，它回傳一個答案（不記得你是誰，也不存留上下文），這就是「無狀態」，必須走 Azure。
​
然而，OpenAI 與亞馬遜正在玩一個「文字遊戲」：他們為新產品 Frontier 開發了一種「有狀態運行環境」（Stateful Runtime Environment, SRE）。
​
微軟的邏輯： 
​
「只要是用我的模型出的產品，管你有沒有狀態，都得在 Azure 上跑！」
​
OpenAI 的邏輯： 「合約只說『無狀態 API』歸你，但我現在做的是具有長期記憶、能自主運行的 AI 代理（Agents），這不屬於 API 範疇，所以我可以在亞馬遜的 AWS 上跑。」
​
這就像一對夫妻簽了婚前協議，規定「所有在外面賺的薪水都要存入共同帳戶」。結果一方說：「但我現在賺的不是薪水，是投資分紅，所以可以存進我自己的帳戶。」
​
一位接近微軟的消息人士對《金融時報》表示：「我們很清楚我們的合約。如果他們違約，我們就會告他們。如果亞馬遜和OpenAI想賭一把他們律師的創造力，我會賭我們贏，而不是他們。」
​
▋OpenAI 為什麼非要亞馬遜不可？
​
為什麼 OpenAI 冒著撕破臉的風險，也要投奔亞馬遜的懷抱？答案只有兩個字：算力。
​
雖然微軟承諾了高達 2,500億美元的算力支持，但 OpenAI 的胃口是無底洞。亞馬遜這次不僅掏出 500億美元現金，還拿出了殺手鐧：高達 2GW（吉瓦）電力支撐的 Trainium 系列自研晶片。
​
對於 OpenAI 來說，過度依賴微軟的 Azure 是一種戰略窒息。透過與 AWS 合作，OpenAI 不僅獲得了更多樣化的晶片供應，還能直接觸及那些「非 AWS 不用」的企業巨頭。這是一次赤裸裸的「去微軟化」行動，宣告 OpenAI 不再甘於只做微軟的 AI 插件。
​
▋誰才是最後的贏家？
​
這場爭端揭示了一個殘酷的現實：在 AI 時代，「獨家協議」可能只是一張隨時會被重新定義的廢紙。
​
當技術進化的速度快到法律條文追不上時，企業總能找到定義上的「漏洞」來規避約束。OpenAI 試圖證明自己是獨立的平台，而微軟則試圖守住它用百億美金築起的護城河。
​
這場糾紛的最終結果，大概率不會是法庭見，而是一個「技術性妥協」。微軟可能會允許 OpenAI 在 AWS 上運行部分業務，但代價是亞馬遜必須支付高昂的「過路費」給微軟，或者 OpenAI 必須保證 Azure 擁有更優先的功能更新權。
​
這場「500 億美元的法律博弈」告訴我們：在 AI 賽道上，沒有永遠的盟友。即便曾經深愛過，在算力與數據主權面前，大家隨時準備翻臉。
​
這個主題，收錄在我這個星期的<思考筆記>中，當中有6個主題想和你分享，完全免費：
​
主題一：Grok準備拜師華爾街精英？
主題二：毛利率 81%，美光不再是週期股了嗎？
主題三：微軟準備提告OpenAI和亞馬遜？
主題四：光通訊新憲法，巨頭發起的OCI聯盟是為了重新定義規則？
主題五：Nvidia是如何做到一年一更的？
主題六：為何黃仁勳要盛讚OpenClaw?
​
<週末筆記>完全免費，你只需要訂閱我的電子報，就能每個星期獲得該星期最值得關注的所有資訊，以及我的看法。
​
- KP
