---
post_id: "1597241012092599"
title: "HBF擴增十幾倍VRAM容量以解決HBM不足? 每單位GB成本大幅降低?......除了直覺的超大GPU package內容量規格之外，以往力推的NAND廠商SanDisk和SK Hynix發表的數據都是在實驗室模擬的performance，Oxmiq則是將HBF的實用性用真實生產階段的推理引擎vLLM為模擬基礎，研究得出的HBF的改善、可用性，比NAND廠商認為、宣稱得更為狹窄，認為HBF只有在頻寬需求低的情況下才會勝出，例如以小批量和長上下文稀疏的KV為MoE"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0ifzXQH69b4XzmGZDJNUKARA4ktjZYPAqFpAvVwKNnMyxMbTP8fgfDPQAQk2VDJHQl&id=100054201473657"
creation_time_utc: "2026-08-29T15:44:29+00:00"
fetched_at_utc: "2026-08-30T06:31:53.662955+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0ifzXQH69b4XzmGZDJNUKARA4ktjZYPAqFpAvVwKNnMyxMbTP8fgfDPQAQk2VDJHQl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU5NzI0MTAxMjA5MjU5OQ=="
page_canonical_url: ""
---

# HBF擴增十幾倍VRAM容量以解決HBM不足? 每單位GB成本大幅降低?......除了直覺的超大GPU package內容量規格之外，以往力推的NAND廠商SanDisk和SK Hynix發表的數據都是在實驗室模擬的performance，Oxmiq則是將HBF的實用性用真實生產階段的推理引擎vLLM為模擬基礎，研究得出的HBF的改善、可用性，比NAND廠商認為、宣稱得更為狹窄，認為HBF只有在頻寬需求低的情況下才會勝出，例如以小批量和長上下文稀疏的KV為MoE

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0ifzXQH69b4XzmGZDJNUKARA4ktjZYPAqFpAvVwKNnMyxMbTP8fgfDPQAQk2VDJHQl&id=100054201473657
HBF擴增十幾倍VRAM容量以解決HBM不足? 每單位GB成本大幅降低?......除了直覺的超大GPU package內容量規格之外，以往力推的NAND廠商SanDisk和SK Hynix發表的數據都是在實驗室模擬的performance，Oxmiq則是將HBF的實用性用真實生產階段的推理引擎vLLM為模擬基礎，研究得出的HBF的改善、可用性，比NAND廠商認為、宣稱得更為狹窄，認為HBF只有在頻寬需求低的情況下才會勝出，例如以小批量和長上下文稀疏的KV為MoE

上次說到Nvidia至今不積極支援HBF是其成功率低於50%的原因，或許這是因也是果? 因為實用性比宣稱的狹窄，所以Nvidia沒有全力支持?

Oxmiq是前Intel架構師Raja Koduri創立Oxmiq Labs，以RISC-V架構GPU搭配OXPython軟體方案，挑戰NVIDIA CUDA生態。OXPython讓Python CUDA工作負載無需修改程式碼即可在非NVIDIA GPU上運行，提升平台開放性與彈性，採IP授權模式經營(MTK有投資)

------------"Oxmiq 列出了幾種部署 HBF 的方法，涵蓋僅 HBM 基線、全 HBF 配置，以及 2 個 HBF 與 6 個 HBM 混合。這三者都位於同一成本範圍內，HBF 選項則是以頻寬換取容量。峰值頻寬從 HBM 基準的 22 TB/s 降至全 HBF 的 12.8 TB/s，容量則從 288 GB 跳升至 4 TB。
......
Oxmiq 詳細說明其在機架層級的系統與模擬設置，跨越一個 72 GPU 機架。在FP4使用以解碼為中心的Kimi-K2 1T模型，輸入100萬標記、輸出1K標記，模擬發現以相同的機架和成本，HBF以約0.6倍的頻寬購買約14倍容量。
......
接著 Oxmiq 轉向 HBF 的軟體限制。存取以 64 KB 區塊進行，以達到最大頻寬，開機後資料保留約 24 小時，溫度為 85 攝氏度，並由主機管理生命週期處理。由於記憶體是讀取最佳化且寫入受限，放置成為軟體問題。
......
該公司帶領推論引擎生態系，從生產服務引擎如 vLLM 和 SGLang，到廠商優化的堆疊如 TensorRT-LLM 和 AWS Neuron。Oxmiq 將 vLLM 視為生產預設，也是 HBF 的重點。
......
接著 Oxmiq 會觀察像 Kimi-K3 這樣的模型中記憶體實際放置位置。約有 93% 的位元組是 MoE 專家權重，達 1.45 TB，因此 Oxmiq 認為 HBF 適合 MoE 專家池和 KV 快取卸載，而 HBM 則負責注意力權重和熱資料。
......
在 vLLM 內部，Oxmiq 提出一個外掛，使用 HBF 取代 KV 快取與 MoE 專家池的主機 CPU 釘選記憶體。配備 4 個 HBM 和 4 個 HBF 堆疊的 GPU 可達到 2.2 TB，峰值頻寬約為 17.4 TB/s，遠高於現今的卸載路徑容量。
......
Oxmiq 認為注意力稀少是真正的 HBF 適合。像 DeepSeek Sparse Attention 和 Compressed Sparse Attention 這類稀疏注意力模型，直接符合 HBF 的低頻寬容量區間，但合適度仍取決於該模型風格。
......
Oxmiq 以一系列重點包裝，從比一些主要 NAND 廠商更狹窄的視角來看待 HBF。實際上，它認為 HBF 只有在頻寬需求低的情況下才會勝出，例如以小批量和長上下文稀疏的 KV 為 MoE。

Oxmiq wraps with a set of takeaways that frame HBF through a much narrower lens than some of the major NAND vendors. Really, it concludes that HBF wins only where bandwidth demand is low, such as MoE with small batch and long-context sparse KV.
......
HBF 看起來像是一個容量工具，針對狹窄但真實的推論工作，特別是大型 MoE 模型，專家權重佔主導地位。將記憶體類型與工作負載及部署規模匹配，比每GB的原始美元更重要。在軟體方面，HBF 分配器和配置政策似乎是這套系統尚未實現的缺失環節。不過，這可能比沒有 AI 原生程式工具幫助時，提升幅度要小。看到這樣坦率的鏡頭真的很酷。"

HBF looks like a capacity instrument aimed at a narrow but real slice of inference work, particularly large MoE models where expert weights dominate. Matching memory type to workload and deployment scale matters more than raw dollars per gigabyte. On the software side, it seems like an HBF allocator and placement policy are the missing pieces before this becomes practical. That said, it is probably less of a lift than it would have been without AI-native coding tools to help. It was really neat to see a candid take like this.

https://www.servethehome.com/oxmiq-labs-hbf-in-ai-compute-at-hot-chips-2026/
