---
post_id: "1607420324408001"
title: "3D DRAM似乎勢在必行，速度和成本介於SRAM和HBM中間，但不是單一產業可以獨力完成，晶片廠、軟體廠、模型商要合作，當初HBM是AMD和DRAM公司一起合作，到了HBF已經變這樣: 模型內部的演算法(參數權重和KV cache)、GPU晶片商(HBF和GPU同一個package)、底層搬動資料的工具軟體、系統層級的配合，到了3D DRAM，似乎這些不同產業廠商需要更多整合合作，例如DRAM堆疊是獨立一堆、堆在Logic晶片上面(Cerebras下兩代CS-6)、堆在Logic晶片下面? 和HBM是取代還是配合? SRAM、3D DRAM、HBM在package內怎麼配合? SRAM是當作cache還是當作可以定址的主記憶體(前者是所有CPU/XPU用法，後者是Cerebras和Groq用法)? 模型演算法如何充分利用SRAM、3D DRAM、HBＭ(如果SRAM僅當cache那軟體動不到SRAM是晶片內部電路在管理)"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0Ak2PCqt3t4AAiP9yHPPHiqUaWSHhjxLWErduFqLChS7y5hMMkVbMVsGBmWw9CqHHl&id=100054201473657"
creation_time_utc: "2026-09-10T13:11:42+00:00"
fetched_at_utc: "2026-09-30T03:40:08.969076+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0Ak2PCqt3t4AAiP9yHPPHiqUaWSHhjxLWErduFqLChS7y5hMMkVbMVsGBmWw9CqHHl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTYwNzQyMDMyNDQwODAwMQ=="
page_canonical_url: ""
---

# 3D DRAM似乎勢在必行，速度和成本介於SRAM和HBM中間，但不是單一產業可以獨力完成，晶片廠、軟體廠、模型商要合作，當初HBM是AMD和DRAM公司一起合作，到了HBF已經變這樣: 模型內部的演算法(參數權重和KV cache)、GPU晶片商(HBF和GPU同一個package)、底層搬動資料的工具軟體、系統層級的配合，到了3D DRAM，似乎這些不同產業廠商需要更多整合合作，例如DRAM堆疊是獨立一堆、堆在Logic晶片上面(Cerebras下兩代CS-6)、堆在Logic晶片下面? 和HBM是取代還是配合? SRAM、3D DRAM、HBM在package內怎麼配合? SRAM是當作cache還是當作可以定址的主記憶體(前者是所有CPU/XPU用法，後者是Cerebras和Groq用法)? 模型演算法如何充分利用SRAM、3D DRAM、HBＭ(如果SRAM僅當cache那軟體動不到SRAM是晶片內部電路在管理)

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0Ak2PCqt3t4AAiP9yHPPHiqUaWSHhjxLWErduFqLChS7y5hMMkVbMVsGBmWw9CqHHl&id=100054201473657
3D DRAM似乎勢在必行，速度和成本介於SRAM和HBM中間，但不是單一產業可以獨力完成，晶片廠、軟體廠、模型商要合作，當初HBM是AMD和DRAM公司一起合作，到了HBF已經變這樣: 模型內部的演算法(參數權重和KV cache)、GPU晶片商(HBF和GPU同一個package)、底層搬動資料的工具軟體、系統層級的配合，到了3D DRAM，似乎這些不同產業廠商需要更多整合合作，例如DRAM堆疊是獨立一堆、堆在Logic晶片上面(Cerebras下兩代CS-6)、堆在Logic晶片下面? 和HBM是取代還是配合? SRAM、3D DRAM、HBM在package內怎麼配合? SRAM是當作cache還是當作可以定址的主記憶體(前者是所有CPU/XPU用法，後者是Cerebras和Groq用法)? 模型演算法如何充分利用SRAM、3D DRAM、HBＭ(如果SRAM僅當cache那軟體動不到SRAM是晶片內部電路在管理)

SRAM
3D DRAM
HBM
HBF
Host DRAM (LPDDR)
CXL DRAM
Local SSD (TLC)
SSD Rack (TLC)
SSD Storage (QLC)

------------"模型權重持續增加，KV 快取會隨著上下文長度乘以批次大小而擴展。所以 64 位使用者在 1 萬上下文下大約有 935 GB 的 KV 快取。權重和快取共同造成容量與頻寬問題，雙方都在持續成長。

SRAM 達到頻寬目標，但規模非常小。一對 Corsair SRAM 加速卡在約 1 納秒延遲下可達 300 TB/s，但容量僅約 4 GB。6T SRAM 單元約是 DRAM 單元的 10 倍，洩漏功率在 GB 尺度下可達數十瓦。這使得 SRAM 適合用於推測解碼的草稿模型，而非用於持有前沿模型權重。這似乎就是 NVIDIA 用 Groq 作為例子的用途。

HBM 解決了一半的容量問題，但頻寬方面卻很吃力。每個基座晶片的腳位速度和 I/O 寬度會慢慢提升，堆疊數量也受限於可用封裝的 beachfront，大約每個封裝 8-16 個堆疊。d-Matrix 指出，HBM4 封裝如 NVIDIA Vera Rubin 與 AMD Instinct MI455 的實際頻寬上限約為 20 TB/s。
......
d-Matrix 的答案是直接在 DRAM 晶片上堆疊運算。堆疊造成熱學挑戰，因為數百瓦必須透過溫度敏感的 DRAM 堆疊中 TSV 洩漏，加上紅外線掉落帶來的電力輸出挑戰。d-Matrix 表示，一個不超過 0.5 W/mm²、1-Hi 邏輯疊疊可液冷，並保持 DRAM 溫度低於 100°C。

3D DRAM 介於這兩個極端之間，處於能量階梯上。晶片上的 SRAM 約耗 50 fJ，而 2.5D HBM4 系統在包含晶片級能量後，運行於 2.5 至 5 pJ 之間。垂直三維輸入輸出的能量約為0.3到0.4 pJ，約為HBM的10倍，因為它是無物理的毫米尺度路徑，而非公分尺度的中介器路徑。堆疊層比 HBM 少，也代表模具更大且良率較高。

d-Matrix 現在正將這種技術觀點映射到大型語言模型推論工作負載的行為上。預填充會平行處理多個提示詞，且受運算吞吐量限制;而解碼則一次產生一個標記，且通常受記憶體頻寬限制。注意力可轉為高 GQA 與推測解碼的計算限制，且即使在中等批次規模下，MoE 仍保持記憶體限制。解碼階段需要大量頻寬。
......
由於解碼主導了牆鐘執行時間，記憶體受限部分最為重要。d-矩陣強調大部分推論時間都花在解碼階段，因此提升解碼頻寬能提升整體推理效能。
......
d-Matrix 的具體實作稱為 Raptor。台積電N4邏輯晶片安裝於3D DRAM晶片上，採用36微米面對面堆疊技術，D-Matrix形容此過程經過驗證、低成本、高產量且高良率。
......
現在 d-Matrix 似乎有個矽面積比較，與 HBM4 和 NVIDIA Rubin R200 比較。Raptor 的運算速度約為每平方毫米 32.6 GB/s，而 HBM 元件約為 1.5 GB/s，約為每平方毫米頻寬的 20 倍，且每 GB/s 提升 2.96 mW，對比 40 mW，提升了 13.5 倍。這真是太棒了。"

https://www.servethehome.com/d-matrix-raptor-3d-dram-accelerator-for-generative-inference-at-hot-chips-2026/
