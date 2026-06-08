---
post_id: "122189719562936895"
title: "最近市場又開始傳一個版本：輝達下週 GTC 會推新系統，GPU 加 Groq LPU，不用 DRAM，改用 SRAM，所以 HBM、DRAM 需求要被打掉。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61578106860333"
final_url: "https://www.facebook.com/profile.php?id=61578106860333"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02LdXnPzYE9knhenyS5xzCK2HEP827JwjFsPgsc4F1VTZM4VRT4TeJFmdqSmhwWvqml&id=61578106860333"
creation_time_utc: "2026-03-16T01:16:31+00:00"
fetched_at_utc: "2026-06-08T07:33:22.963947+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-sjc3-1.xx.fbcdn.net/v/t39.30808-6/652095491_122189719496936895_8408541322676360213_n.jpg?stp=cp6_dst-jpg_s600x600_tt6&_nc_cat=110&ccb=1-7&_nc_sid=833d8c&_nc_ohc=cg65vf7eztQQ7kNvwEq7C13&_nc_oc=AdqffiFyjlNZA71u5iyTkHKyWAzo26Mli-AjQ-PePnx_pG6-MdlWV2UpYK3LzLBqJrA&_nc_zt=23&_nc_ht=scontent-sjc3-1.xx&_nc_gid=H9rLM-Qz50modJRZwP9qfg&_nc_ss=7e120&oh=00_Af8_vzK9nz-LP4dbQSWpeTtDiYjNB1QVz_Yuoq_Q4Td2Bw&oe=6A2C5BC6"
feedback_id: "ZmVlZGJhY2s6MTIyMTg5NzE5NTYyOTM2ODk1"
page_canonical_url: ""
---

# 最近市場又開始傳一個版本：輝達下週 GTC 會推新系統，GPU 加 Groq LPU，不用 DRAM，改用 SRAM，所以 HBM、DRAM 需求要被打掉。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02LdXnPzYE9knhenyS5xzCK2HEP827JwjFsPgsc4F1VTZM4VRT4TeJFmdqSmhwWvqml&id=61578106860333

![最近市場又開始傳一個版本：輝達下週 GTC 會推新系統，GPU 加 Groq LPU，不用 DRAM，改用 SRAM，所以 HBM、DRAM 需求要被打掉。](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.30808-6/652095491_122189719496936895_8408541322676360213_n.jpg?stp=cp6_dst-jpg_s600x600_tt6&_nc_cat=110&ccb=1-7&_nc_sid=833d8c&_nc_ohc=cg65vf7eztQQ7kNvwEq7C13&_nc_oc=AdqffiFyjlNZA71u5iyTkHKyWAzo26Mli-AjQ-PePnx_pG6-MdlWV2UpYK3LzLBqJrA&_nc_zt=23&_nc_ht=scontent-sjc3-1.xx&_nc_gid=H9rLM-Qz50modJRZwP9qfg&_nc_ss=7e120&oh=00_Af8_vzK9nz-LP4dbQSWpeTtDiYjNB1QVz_Yuoq_Q4Td2Bw&oe=6A2C5BC6)
最近市場又開始傳一個版本：輝達下週 GTC 會推新系統，GPU 加 Groq LPU，不用 DRAM，改用 SRAM，所以 HBM、DRAM 需求要被打掉。

這種說法，幾乎每一段都錯。

先看官方資訊。NVIDIA 這次 GTC 2026 公開主軸是 agentic AI、inference、physical AI、AI factories 與整個 AI stack。外界現在看到的，多數是媒體對新推理晶片的推測與延伸，不是 NVIDIA 已經正式公布的產品規格。 

真正的問題，是很多人根本沒有搞清楚記憶體階層。

SRAM 很快，延遲很低，適合放最熱的資料、最關鍵的路徑，做片上 buffer、cache，或某些極低延遲推理架構。Groq 官方對自家 LPU 的描述也很清楚：核心特色是 single core 加上 on-chip SRAM，用數百 MB 等級的 SRAM 當主要權重儲存，目的是把延遲壓低、把資料搬移減到最少。這是在強化特定推理場景，不是在宣告主記憶體可以消失。 

為什麼不能這樣理解？因為 SRAM 的物理與成本結構，天生就不適合取代 DRAM。SRAM 面積大、密度低、每 bit 成本高，長期都拿來做高速近端記憶體；DRAM 則是用來承接大容量、可擴展、成本較合理的主記憶體需求。這不是市場情緒，也不是法人話術，是半導體最基本的物理與經濟性。學術資料也明確指出，SRAM 與 DRAM 在系統裡一直扮演不同角色，前者換速度，後者換容量與成本效率。 

所以如果 NVIDIA 真的在推理產品裡導入更多 Groq 式架構，合理的解讀不是「DRAM 被取代」，而是 AI 基礎設施的 memory hierarchy 正在切得更細。片上 SRAM 負責最熱資料、最低延遲；HBM 負責高頻寬主記憶體；更外層還有 DRAM、SSD、甚至更大規模的儲存層。這會讓不同工作負載找到更適合的落點，而不是把原本的 HBM、DRAM 一筆勾銷。 

而且別忘了，AI 推理不是只有一個指標。你不能只看 decode latency，就說整個系統不需要 DRAM。只要模型更大、context 更長、batch 更多、agent workflow 更複雜，容量需求還是會往外層記憶體堆疊出去。SRAM 可以優化一段路，不可能獨力吃下整個資料中心級推理需求。Groq 自己的架構優勢，是把特定推理路徑做得更快、更可預測，不是把大型模型服務變成只靠 SRAM 就能運作。 

從產業角度看，這反而是利多，不是利空。

因為 AI 正在從單一 GPU 訓練架構，走向多層次、多硬體分工的時代。訓練是一套，通用推理是一套，低延遲即時推理又是一套，agent orchestration、networking、memory tiering、storage 也各有自己的角色。Reuters 對 GTC 的預期也是 NVIDIA 會把 inference、agent orchestration、networking 與整體基礎設施講得更完整，重點是把產品線做寬，不是把 GPU 與 HBM 路線推翻。 

所以這件事最該破解的謬誤只有一句：

SRAM 變多，不代表 DRAM 變少；很多時候，SRAM 變多，代表整個系統做得更細、更快，最後反而把整體推理規模做大，連帶把 HBM、DRAM、SSD 一起往上拉。

看 AI 基礎建設，最怕的就是把局部最佳解，誤當成全系統替代方案。SRAM 是重要的一層，但它不是主記憶體的終結者。真正會發生的，是記憶體分層越來越細，算力與資料流動越來越複雜，整個產業的總量繼續往上走。

如果下週 GTC 真有新推理產品，我會更關注三件事：第一，SRAM 主要切入 prefill 還是 decode；第二，跟 GPU/HBM 是互補還是獨立部署；第三，系統層是想降低單位 token 成本，還是要搶即時 agent 與 physical AI 市場。這三件事，看懂了，才知道受惠的是誰。
