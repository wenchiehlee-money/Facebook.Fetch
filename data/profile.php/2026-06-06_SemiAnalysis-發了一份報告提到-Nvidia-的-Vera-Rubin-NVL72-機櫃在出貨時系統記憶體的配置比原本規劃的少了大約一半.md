---
post_id: "122185255922771552"
title: "SemiAnalysis 發了一份報告，提到 Nvidia 的 Vera Rubin NVL72 機櫃在出貨時，系統記憶體的配置比原本規劃的少了大約一半。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61573146584049"
final_url: "https://www.facebook.com/profile.php?id=61573146584049"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02A79zU3gjewaDqs5FqBdYk4ju4S4f6VrBuczWLEvWYeNRvMRpQjV1qXzfKwSQdejDl&id=61573146584049"
creation_time_utc: "2026-06-06T13:37:46+00:00"
fetched_at_utc: "2026-06-08T07:01:42.458119+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-iad6-1.xx.fbcdn.net/v/t39.30808-6/718792655_122185255838771552_1788820813699013763_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=107&ccb=1-7&_nc_sid=127cfc&_nc_ohc=50SyKJCqnGgQ7kNvwESCuEg&_nc_oc=Adq6cvC-mY3RDGw3knT9j93AXk58v3Ii778KUzWfvrIIe_tmcxZc4chVIoaJCE5Npqo&_nc_zt=23&_nc_ht=scontent-iad6-1.xx&_nc_gid=fGzuxfNAt3JQTRF48NVvHA&_nc_ss=7e120&oh=00_Af-RROeLPSordV5v7Tx7gxt1g5_0E6o5THPizKnHI7FzHg&oe=6A2C3BDF"
feedback_id: "ZmVlZGJhY2s6MTIyMTg1MjU1OTIyNzcxNTUy"
page_canonical_url: ""
---

# SemiAnalysis 發了一份報告，提到 Nvidia 的 Vera Rubin NVL72 機櫃在出貨時，系統記憶體的配置比原本規劃的少了大約一半。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02A79zU3gjewaDqs5FqBdYk4ju4S4f6VrBuczWLEvWYeNRvMRpQjV1qXzfKwSQdejDl&id=61573146584049

![SemiAnalysis 發了一份報告，提到 Nvidia 的 Vera Rubin NVL72 機櫃在出貨時，系統記憶體的配置比原本規劃的少了大約一半。](https://scontent-iad6-1.xx.fbcdn.net/v/t39.30808-6/718792655_122185255838771552_1788820813699013763_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=107&ccb=1-7&_nc_sid=127cfc&_nc_ohc=50SyKJCqnGgQ7kNvwESCuEg&_nc_oc=Adq6cvC-mY3RDGw3knT9j93AXk58v3Ii778KUzWfvrIIe_tmcxZc4chVIoaJCE5Npqo&_nc_zt=23&_nc_ht=scontent-iad6-1.xx&_nc_gid=fGzuxfNAt3JQTRF48NVvHA&_nc_ss=7e120&oh=00_Af-RROeLPSordV5v7Tx7gxt1g5_0E6o5THPizKnHI7FzHg&oe=6A2C3BDF)
SemiAnalysis 發了一份報告，提到 Nvidia 的 Vera Rubin NVL72 機櫃在出貨時，系統記憶體的配置比原本規劃的少了大約一半。
​
很快地，市場上就出現了鋪天蓋地的熊市鬼故事：「Nvidia將記憶體需求砍半！」、「記憶體大廠的超級週期要終結了！」
​
這類點擊率極高的陰謀論，完美展現了什麼叫「去脈絡化的斷章取義」。
​
▋不當完美主義者，先通車再說
​
首先，我們要釐清一個關鍵：被「砍半」的，是 CPU 側的系統記憶體（LPDDR5X），而不是 GPU 側那顆最核心、最昂貴的 HBM4（高頻寬記憶體）。
​
在 Rubin 晶片上，負責承擔海量矩陣運算、注意力機制等核心算力的 HBM4，規格與需求完全沒有受到任何影響。
​
那為什麼要動 CPU 側的 LPDDR5X？答案很簡單：供應鏈卡住了，但客戶等不及了。
​
目前，要達到原先規劃的超高容量，必須使用極高密度的 16 層堆疊 LPDDR5X 模組，而這種模組目前的良率與產能極其受限。
​
如果 Nvidia 堅持「規格不攻頂不出貨」，那 Rubin 的量產時程勢必會被嚴重拖累。
​
於是，黃仁勳做了一個非常務實的商業決策：
​
- 降規加速出貨：改用產能成熟的 96 GB 模組，避開供應鏈瓶頸，讓 Rubin 機架能以最快速度送進微軟、Meta 等雲端巨頭（Hyperscalers）的資料中心。
​
- 幫客戶省錢（降低 TCO）：這一降規，直接讓每台機架的成本暴省了 80 萬美元（從約 760 萬美元 降至 680 萬美元）。
-保留升級後路：Blackwell 世代（如 GB300 Ultra）使用的是直接銲死在主機板上的 LPDDR 記憶體；但 Vera Rubin 平台改用了插槽式（Socketed）的 SOCAMM2 模組設計。
​
這種「熱插拔、可現場更換」的設計，意味著 96GB 只是供應鏈極限下的「過渡性配置」。如果客戶未來真的有極致需求，且高密度模組產能跟上了，隨時可以像插拔電腦記憶體一樣，在機房裡直接升級。
​
很明顯，這根本不是 Nvidia 覺得不需要這麼多記憶體了，只不過是一個工程上的妥協。
​
這根本不是需求下滑，只不過是一個「先上車、後補票」的彈性策略。
​
▋反向思考
​
每台機架省下 80 萬美元，加上出貨速度變快，會刺激雲端巨頭下單更多數量的 Rubin 機架。
​
從數學邏輯來看，全球 LPDDR5X 的總產能目前就這麼多。Nvidia 將單機配置減半，意味著原本只能組裝 100 台機櫃的記憶體，現在可以分給 200 台機櫃使用，讓整體 Rubin 平台以雙倍速度鋪開。
​
對記憶體大廠來說，產能依然是滿載被消耗掉的，總體位元（Total Bits）需求根本沒有縮水。
​
相反地，每一台多賣出去的機架，裡面搭載的 HBM4 可是一點都沒少。更別提未來產能緩解後，客戶回頭採購 192GB 模組進行二次升級的「售後拉貨潮」。
​
▋標題之外
​
SemiAnalysis 的創辦人 Dylan Patel 在社群媒體上的回應很直接：「有件事我一直覺得有趣，分享我們報告的人經常漏掉大部分內容。」
​
事實上，複雜的供應鏈分析，在傳播過程中幾乎必然會被簡化。簡化本身不是壞事，但當簡化變成扭曲，當「Nvidia 為了加速出貨而調整系統記憶體配置」變成「記憶體需求腰斬」，訊息的本質就完全走樣了。
​
這次的 SOCAMM 故事是個縮影。相比起記憶體需求的崩潰，這更是 AI 基礎建設正在走向一個更成熟、更分層、更軟體定義的記憶體架構。
​
在這個架構裡，熱資料、溫資料、冷資料有各自適合的載體，而整體的矽需求和儲存需求會隨著 AI 部署的規模持續上升。
​
記憶體超級週期的邏輯沒有改變。瓶頸會在不同層級之間移動，但總需求的方向是清楚的。
​
下次看到「XX 需求腰斬」這種標題時，或許可以先問一句：腰斬的是哪一層？為什麼？這對其他層級有什麼影響？答案通常比標題有趣得多。
​
這個主題收錄在我的週末筆記中，這個星期有5個主題，包括：
​
- 主題一：當 Windows 遇上 CUDA，AI PC 如何權力重組？
​
- 主題二：當 AI 走向「代理人」時代，Intel 如何用 CPU 奪回系統調度權？
​
- 主題三：從回購王變成融資王，Google 為什麼突然募資 850 億美元？
​
- 主題四：拒絕賺快錢，從 Build 2026 看微軟的策略
​
- 主題五：Nvidia 對記憶體需求減半？
​
週末筆記完全免費，你只要訂閱電子報，就能每週免費獲得我對市場的看法。
​
- KP
