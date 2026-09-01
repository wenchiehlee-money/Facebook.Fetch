---
post_id: "122225061452502956"
title: "🚀 AI 正從「訓練」走向「推理」，Cerebras 真正的機會才剛開始"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61565088683715"
final_url: "https://www.facebook.com/profile.php?id=61565088683715"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0Pq8NYejf5Kjhr9oyrAzDu7NJs4Cjrxta1GuLkYUf25tZvpdbkuF1FQjNfvLWs2Bwl&id=61565088683715"
creation_time_utc: "2026-08-18T05:46:38+00:00"
fetched_at_utc: "2026-09-01T04:44:49.974389+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-dfw5-1.xx.fbcdn.net/v/t39.30808-6/774105543_122225061332502956_3332016136018708598_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_ohc=XwXx5vEcTUkQ7kNvwFGsfHM&_nc_oc=Adrk5ybzaF1L48A41yWqycrvrhsisJzptL81-30eC6na0RSQFQZdoSaxliPJYlsWmpk&_nc_zt=23&_nc_ht=scontent-dfw5-1.xx&_nc_gid=qRCrgAOtCBt9a8QDITVrTQ&_nc_ss=7e120&oh=00_AQIMQSdBr1XXkHUnDB4-Uy1kQ0T_D8M5_wZmU2MeYHqQAw&oe=6A9C38AE"
feedback_id: "ZmVlZGJhY2s6MTIyMjI1MDYxNDUyNTAyOTU2"
page_canonical_url: ""
---

# 🚀 AI 正從「訓練」走向「推理」，Cerebras 真正的機會才剛開始

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0Pq8NYejf5Kjhr9oyrAzDu7NJs4Cjrxta1GuLkYUf25tZvpdbkuF1FQjNfvLWs2Bwl&id=61565088683715

![🚀 AI 正從「訓練」走向「推理」，Cerebras 真正的機會才剛開始](https://scontent-dfw5-1.xx.fbcdn.net/v/t39.30808-6/774105543_122225061332502956_3332016136018708598_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_ohc=XwXx5vEcTUkQ7kNvwFGsfHM&_nc_oc=Adrk5ybzaF1L48A41yWqycrvrhsisJzptL81-30eC6na0RSQFQZdoSaxliPJYlsWmpk&_nc_zt=23&_nc_ht=scontent-dfw5-1.xx&_nc_gid=qRCrgAOtCBt9a8QDITVrTQ&_nc_ss=7e120&oh=00_AQIMQSdBr1XXkHUnDB4-Uy1kQ0T_D8M5_wZmU2MeYHqQAw&oe=6A9C38AE)
🚀 AI 正從「訓練」走向「推理」，Cerebras 真正的機會才剛開始
⚡ ① 最大核心：Cerebras 押注的是 Inference，而不是 Training
Cerebras 最重要的定位，不是另一家 GPU 公司，而是專注 AI Inference，尤其是 Decode。過去 AI 基礎建設主要圍繞模型訓練，現在隨著 Reasoning、Agentic AI 普及，真正大量消耗算力的階段，將逐漸轉向模型部署與推理。

更重要的是，模型未必會一直往「更大」發展。未來即使模型透過 Distillation 變小，一個 AI Agent 卻可能需要不斷搜尋、呼叫工具、驗證答案、重新推理，導致單一任務需要生成更多 Token。因此，模型變小不代表 AI Compute 需求下降，反而可能讓 Inference 使用量進一步爆發。

🧠 ② WSE 的真正優勢：不是算力，而是速度
Cerebras 的 WSE（Wafer-Scale Engine）把大量運算核心與 SRAM 直接整合在一整片晶圓上。WSE-3 擁有約 90 萬個 AI 優化核心、44GB SRAM，以及約 21 PB/s 的記憶體頻寬，核心優勢就是極高的 Memory Bandwidth 與極低的資料搬移延遲。

這對 Inference 的 Decode 特別重要，因為模型每生成一個 Token，都需要頻繁讀取模型權重。傳統 GPU 主要依賴 HBM，而 Cerebras 則把大量資料盡可能留在晶片內，減少外部記憶體存取，因此能把「下一個 Token 多快出來」做到非常極致。

所以 Cerebras 真正競爭的不是「誰的 FLOPS 比較高」，而是：誰能更快、更低延遲地把答案吐出來。

🔗 ③ Disaggregated Inference：不同晶片開始各司其職
Cerebras 最有意思的地方，是它不一定需要取代 NVIDIA、AMD 或 AWS 的 AI 加速器。未來 AI Inference 可以拆成不同階段，由不同硬體負責最適合自己的工作。

例如 Prefill 需要大量平行運算，可以交給 GPU 或其他 AI Accelerator；接下來進入 Decode，則交給 Cerebras WSE 高速生成 Token。這就是 Disaggregated Inference（分離式推理）。

因此未來的競爭可能不是「Cerebras vs NVIDIA」，而是 AMD / NVIDIA / AWS + Cerebras 組成新的異質 AI 運算架構。這個定位非常重要，因為 Cerebras 可以成為其他 AI 加速器的互補元件，而不只是單純的替代品。

☁️ ④ 真正值得注意的是 Cloud / Services 爆發
Cerebras 正在從單純「賣 AI 晶片」逐漸走向 AI Compute-as-a-Service。最新一季 Core Revenue 達 2.099 億美元，年增 103%，其中 Core Cloud & Services Revenue 更達 1.277 億美元，年增 287%。

這代表商業模式正在改變。硬體銷售比較接近一次性收入，而 Cloud / Inference Services 則可以隨著使用量持續產生收入。隨著 Cloud 業務占比提高，再加上自有運算容量逐步上線，未來有機會同時看到 收入成長、利用率提升與營運槓桿。

📈 ⑤ 2027 年的高速成長，是接下來最重要的驗證
管理層目前預期 2026 年 Core Revenue 約 8.8～8.9 億美元，並表示現有產能已足以支撐 2027 年 Core Revenue 至少成長 3 倍。這代表 Cerebras 接下來的故事，已經不只是「技術很好」，而是進入真正的商業化放量階段。

同時，公司手上的 RPO 約 254 億美元，以及截至 2027 年底超過 600MW 的資料中心容量，提供相當高的收入能見度。不過 RPO 並不等於全部都是純收入，其中包含資料中心 pass-through 等項目，因此真正重要的仍然是 部署速度、實際使用率與每單位運算產生的毛利。

🏭 ⑥ 接下來最大的瓶頸，可能不是需求，而是產能
目前 Cerebras 面對的問題已經逐漸從「有沒有人要買」變成「能不能把需求轉換成真正的運算容量」。公司計畫在 2026 年將製造能力提高 10 倍以上，同時持續擴大資料中心容量。

💰 ⑦ 毛利率改善，代表商業模式開始出現槓桿
最新一季 Core Gross Margin 已達 40.6%，年增約 9.4 個百分點。隨著 Cloud / Services 占比提升，以及更多自有容量取代成本較高的租用設備，毛利率仍有進一步改善的空間。

這也是 Cerebras 最值得期待的地方之一：如果未來同時出現 Revenue 高速成長 + Cloud 占比提升 + Gross Margin 擴張 + Operating Expense 增速下降，那麼公司就可能從單純的高成長 AI 硬體公司，開始進入真正的獲利槓桿階段。

🤖 ⑧ AMD、AWS 是催化劑，但 Cerebras 不應只被看成它們的附屬品
AMD Helios 與 Cerebras 的合作，讓「Prefill + Decode」的分工更加具體；AWS 也採用類似的 Disaggregated Inference 概念。這些合作的重要性不只是帶來訂單，更是在驗證 Cerebras WSE 能否成為下一代 AI Inference 架構的一部分。

如果未來這種架構被更多 AI Data Center 採用，Cerebras 的市場就不必局限於單一客戶或單一平台，而有機會成為跨平台的 Inference Decode Layer。

⚠️ ⑨ 最大風險：技術不是唯一問題
首先是 OpenAI 客戶集中度，大型合約能快速推升收入，但也讓公司對單一客戶的部署節奏更加敏感。其次是 Capacity Execution，10 倍產能擴張能否順利轉化成實際營收，是接下來最重要的執行考驗。最後則是競爭，NVIDIA、AMD、Google、AWS 等公司都在持續優化 Inference，而 AI 硬體迭代速度非常快，Cerebras 必須持續維持自己的速度與成本優勢。

🔥 ⑩ Cerebras 最值得看的，其實是「Inference 時代的基礎設施」
把 Groq、Cerebras、d-Matrix，以及 Google TPU、AWS Trainium / Inferentia、Meta MTIA、Microsoft Maia 放在一起看，會發現 AI ASIC 的競爭已經逐漸從「誰能取代 NVIDIA」轉向 誰能吃到不同 AI Workload 的增量市場。

Cerebras 的特色，就是把自己定位在 Inference-first、低延遲、高 Token 生成速度這條路線。尤其當 Reasoning、Agentic AI 與大量 Token 使用成為趨勢後，AI Compute 的瓶頸可能逐漸從「訓練最大的模型」轉向「如何以最低延遲、最高效率完成大量推理」。

📌觀察
如果未來 AI 從「單次回答」進入大量 Reasoning + Agentic Workflow，Token 使用量會持續增加，而 Prefill 與 Decode 分離也可能成為資料中心的重要架構。這種情況下，Cerebras 就有機會從一家特殊的 AI 晶片公司，逐漸變成 AI Inference 基礎設施的重要一層。

真正要追蹤的三件事就是：
① 2027 年收入能不能按照目前速度放量
② 600MW+ 產能與 10× 製造擴張能不能順利轉成實際使用量
③ Cloud / Services 成長能不能帶動毛利率與獲利能力同步提升

如果這三件事同時成立，Cerebras 的故事就不再只是「一顆很快的 AI 晶片」，而會變成 Inference 時代的一種新型 AI Compute Infrastructure。

#Cerebras #CBRS #AI #AIInference #AgenticAI #AIASIC #WSE #AIInfrastructure #DisaggregatedInference #AMD #AWS #AI晶片
