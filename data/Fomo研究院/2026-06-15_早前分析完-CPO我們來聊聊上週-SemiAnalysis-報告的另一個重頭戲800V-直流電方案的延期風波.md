---
post_id: "122186237426771552"
title: "早前分析完 CPO，我們來聊聊上週 SemiAnalysis 報告的另一個重頭戲：800V 直流電方案的延期風波。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61573146584049"
final_url: "https://www.facebook.com/profile.php?id=61573146584049"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0xMP2Yj4H27p2nqVnfzUaArkpyKwPjGXD96oZHu5uxXbHK1SVqBviCS5y6DpQz8gBl&id=61573146584049"
creation_time_utc: "2026-06-15T07:15:17+00:00"
fetched_at_utc: "2026-07-20T12:57:19.783956+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-sjc3-1.xx.fbcdn.net/v/t39.30808-6/724660667_122186237378771552_2787361605246562183_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=YPlGIegwOkQQ7kNvwGuMhJ9&_nc_oc=AdqFcsG0u9dIAFje7DBz8wo6EsX33glYxKQH9AUDaBpxS2FZ9sGZF4K1H4fqGDqeFuw&_nc_zt=23&_nc_ht=scontent-sjc3-1.xx&_nc_gid=ATDjN7S_L8wDfU9jr6EQBw&_nc_ss=7e120&oh=00_AQAQ_zi0hnLz88LAtFox_PInlClNIXCSPavqMhNlbktZfA&oe=6A63EB42"
feedback_id: "ZmVlZGJhY2s6MTIyMTg2MjM3NDI2NzcxNTUy"
page_canonical_url: ""
---

# 早前分析完 CPO，我們來聊聊上週 SemiAnalysis 報告的另一個重頭戲：800V 直流電方案的延期風波。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0xMP2Yj4H27p2nqVnfzUaArkpyKwPjGXD96oZHu5uxXbHK1SVqBviCS5y6DpQz8gBl&id=61573146584049

![早前分析完 CPO，我們來聊聊上週 SemiAnalysis 報告的另一個重頭戲：800V 直流電方案的延期風波。](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.30808-6/724660667_122186237378771552_2787361605246562183_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=YPlGIegwOkQQ7kNvwGuMhJ9&_nc_oc=AdqFcsG0u9dIAFje7DBz8wo6EsX33glYxKQH9AUDaBpxS2FZ9sGZF4K1H4fqGDqeFuw&_nc_zt=23&_nc_ht=scontent-sjc3-1.xx&_nc_gid=ATDjN7S_L8wDfU9jr6EQBw&_nc_ss=7e120&oh=00_AQAQ_zi0hnLz88LAtFox_PInlClNIXCSPavqMhNlbktZfA&oe=6A63EB42)
早前分析完 CPO，我們來聊聊上週 SemiAnalysis 報告的另一個重頭戲：800V 直流電方案的延期風波。
​
這件事在市場上鬧得沸沸揚揚。報告出爐隔天，大摩（摩根士丹利）隨即跳出來唱反調，堅稱台灣電源龍頭（如台達電）的 800V 電源機櫃第四季照樣出貨給北美雲端巨頭。
​
一個說「延期到 2028 年後」，一個說「今年下半年照常出貨」，這到底是怎麼回事？
​
▋兩大機構在爭什麼？
​
- SemiAnalysis： 主張 NVIDIA「原生」800V 直流電架構因晶片尚不需要高壓、雙重轉換效率不划算，且面臨「±400V」方案競爭，大規模放量已推遲到 2028 年或更晚。
​
- 大摩： 根據供應鏈調查，Nvidia 800V 直流電源機架預計 2026 年第三季量產、第四季交付。大摩特別提醒：大家必須區分「初期小量出貨」與「全面大規模放量」的差別。
​
▋兩邊都對：因為他們在說不同的「層」
​
事實上，這兩家機構都沒說錯，只是看的是電力架構中不同的「樓層」。
​
第一階段：外掛式電源櫃（Sidecar）—— 大摩眼中的「現在進行式」
​
這就像幫現有機房外掛升級包。不需要重新設計晶片或主機板，只要在伺服器機櫃旁放一尊獨立的「800V 直流電源櫃」（Sidecar），負責把交流電轉成 800V 直流電送進伺服器。
​
這屬於基礎設施升級，正是大摩所說、台達電 正在量產出貨的硬體，時間點在 2026 下半年。
​
第二階段：原生 800V 架構（Native）—— SemiAnalysis 警告的「未來式」
​
這才是終極省電方案。高壓直流電一路暢通無阻地通到晶片旁邊，才進行最後的降壓。這需要晶片、主機板、伺服器在設計之初就完全配合（如未來的 Rubin Ultra 平台）。
​
當未來機櫃功耗飆破 600kW、傳統變壓器塞不下時，這一步是必經之路。但因為高壓電涉及極嚴格的安全法規、防電弧標準尚未成熟，加上晶片研發時程，大規模普及確實被推遲到 2028 年以後。
​
所以，大摩說的出貨是「外掛電源櫃」；SemiAnalysis 說的延期是「伺服器端的原生 800V 架構」。兩者講的根本是不同樓層的事，並不衝突。
​
▋為什麼 ±400V 先行
​
既然原生 800V 還要等，這兩年資料中心要怎麼解決功耗問題？答案是：±400V 雙極直流電。
​
這是一個折衷方案。它利用正 400V 和負 400V 的電位差，在傳輸時同樣能達到 800V 的傳輸效能。但因為「對地電壓」只有 400V，安全風險大降，完全可以沿用現成、極為成熟的電動車（EV）400V 電力元件生態系。
​
這也是為什麼 Google、Meta 等巨頭主導的 OCP Diablo 400 標準正鋪天蓋地地展開，因為它安全、好做、現在就能省電。
​
雖然Nvidia官方更傾向推動純 800V 方案以追求極致效率，但市場目前出現分歧：雲端巨頭大多選擇務實的 ±400V 作為第一步，而Nvidia則繼續為其最高密度的未來機櫃護航純 800V 方案。
​
好消息是，這兩種設計在架構上是相容的。雖然不是簡單的「隨插即用」，但可以漸進式升級。
​
現在部署的外掛式電源櫃都是模組化設計。隨著未來技術成熟，業者可以直接升級這些電源櫃，而不需要把整個資料中心打掉重蓋。
​
對於舊有機房的改建來說，先從 ±400V 開始，以後再升級到 800V，是最安全的做法。
​
這也解釋了為什麼巨頭們不急著一步到位，因為直接跳到原生 800V 的好處，還無法抵消它帶來的法規風險與高昂成本。
​
▋誰受益，誰承壓
​
原生 800V 延遲而 ±400V 按計劃放量，創造了明確的近期贏家和相對輸家。
​
- 近期贏家： 成熟的重電與配電基礎設施公司（如 Vertiv、Legrand、Amphenol）。不論客戶用哪種方案，其配電、連接線材和機櫃現在就能直接出貨。
​
- 面臨壓力： 成長故事與「原生 800V 快速放量」深度綁定的電力半導體廠商（如 Navitas 的 GaN 晶片、Wolfspeed 的 SiC 晶片）。
​
- 左右逢源： 具備「模組化、可升級」設計的電源供應商。以台達電為例，既能吃到現在 ±400V 的過渡期訂單，未來也能順勢升級，不用砍掉重練。
​
▋我的思考
​
這場關於 800V 直流電的延期爭論，本質上和我們之前分析的 CPO 延遲非常相似。
​
兩者都在討論技術轉型，也都是因為大家把不同階段、不同層次的東西混為一談，才產生了「一個說延期、一個說照常出貨」的矛盾。
​
在這個日新月異的 AI 世界裡，技術規格和升級路線實在太多、太快，市場很容易因為訊息不對稱而陷入混亂與恐慌。
​
但對我們來說，這種因為「看錯樓層」而產生的誤解與市場定價偏差，恰恰就是我們看清真相、尋找投資機會的最好時機。
​
這個主題收錄在我最新一期的週末筆記中，另外總共有五個主題，包括：
​
主題一：沒有任何新意的WWDC？
​
主題二：史上最大 IPO ，你應該知道甚麼？
​
主題三：800V 直流電延期風波：SemiAnalysis 與大摩誰才是對的？
​
主題四：甲骨文又被打回原形了？
​
主題五：Token 的減價戰要來了？
​
週末筆記完全免費，你只需要免費訂閱，就能定期收到我最新的看法。
​
- KP
