---
post_id: "1452842013199167"
title: "Meta的AI XPU路線很明確，因為晶片設計到生產要兩年多，此時AI工作負載可能已經改變，Meta的策略是高頻小改，每半年更新一次晶片，但每代晶片是基於上一代的基礎改變，系統、機架設計盡量沿用，隨著AI模型和工作負載調整，並且利用chiplet達到設計彈性，R&R推薦與排行模型/系統是Meta最大的AI應用，這幾代AI XPU主要也是服務R&R訓練和推論"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid09CJdKEcHfpxuAeWC4aVVHoeVbjeFrTuaxAZ9FeTwFrLntd1hA1HBEhAqEixnUNH8l&id=100054201473657"
creation_time_utc: "2026-03-11T17:46:31+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid09CJdKEcHfpxuAeWC4aVVHoeVbjeFrTuaxAZ9FeTwFrLntd1hA1HBEhAqEixnUNH8l&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ1Mjg0MjAxMzE5OTE2Nw=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# Meta的AI XPU路線很明確，因為晶片設計到生產要兩年多，此時AI工作負載可能已經改變，Meta的策略是高頻小改，每半年更新一次晶片，但每代晶片是基於上一代的基礎改變，系統、機架設計盡量沿用，隨著AI模型和工作負載調整，並且利用chiplet達到設計彈性，R&R推薦與排行模型/系統是Meta最大的AI應用，這幾代AI XPU主要也是服務R&R訓練和推論

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid09CJdKEcHfpxuAeWC4aVVHoeVbjeFrTuaxAZ9FeTwFrLntd1hA1HBEhAqEixnUNH8l&id=100054201473657
Meta的AI XPU路線很明確，因為晶片設計到生產要兩年多，此時AI工作負載可能已經改變，Meta的策略是高頻小改，每半年更新一次晶片，但每代晶片是基於上一代的基礎改變，系統、機架設計盡量沿用，隨著AI模型和工作負載調整，並且利用chiplet達到設計彈性，R&R推薦與排行模型/系統是Meta最大的AI應用，這幾代AI XPU主要也是服務R&R訓練和推論

不賭兩年後的模型演變，而是每半年修改一次新晶片，不知道這是不是意味每一代晶片產量不會很大? 但系統和架構可沿用

這樣還需要TPU嗎?????

----------"AI 模型的演進速度比傳統晶片開發週期還快。晶片設計是基於預期的工作負載，但當硬體投入生產時——通常是兩年後——這些工作負載可能已經大幅變動。我們不打算長時間下注等待，而是刻意採取迭代式的方法：每一代 MTIA 都在上一代基礎上成長，使用模組化晶片組，整合最新的 AI 工作負載洞察與硬體技術，並以更短的部署節奏進行。這種更緊密的循環讓我們的硬體更貼合不斷演進的模式，同時促進新技術的更快採用。
AI models are evolving faster than traditional chip development cycles. Chip designs are based on projected workloads, but by the time the hardware reaches production — often two years later — those workloads may have shifted substantially. Rather than placing a bet and waiting for a long period of time, we deliberately take an iterative approach: Each MTIA generation builds on the last, using modular chiplets, incorporating the latest AI workload insights and hardware technologies, and deploying on a shorter cadence. This tighter loop keeps our hardware better aligned with evolving models while enabling faster adoption of new technology.

MTIA 家族現今包括：

MTIA 300：最初針對 R&R 模型進行優化——這是 GenAI 起飛前主流的 Meta 工作負載——其基礎為後續針對生成式 AI 模型優化的晶片奠定了堅實基礎。目前正用於R&R訓練。

MTIA 400：隨著生成式人工智慧的興起，MTIA 300演變成MTIA 400，以更好地支援生成式AI模型，同時維持支援R&R工作負載的能力。MTIA 400 擁有 72 個加速器的擴展領域，提供與領先商用產品的高性能競爭。我們已完成實驗室對 MTIA 400 的測試，並正朝著部署到資料中心的方向前進。

MTIA 450：預見生成式AI推論需求的上升，MTIA 400轉型為MTIA 450，並針對生成式AI推理做了特定優化。由於高頻寬記憶體（HBM）的頻寬是影響生成式AI推論效能的最重要因素，我們將HBM頻寬從MTIA 400加倍至450，遠高於現有主流商用產品。此外，我們引入了為推論工作負載共同設計的低精度資料型態。MTIA 450預定於2027年初大規模部署。

MTIA 500：延續對生成式AI推論的聚焦，MTIA 500將HBM頻寬比MTIA 450提升了50%，並在低精度資料類型中引入了更多創新。MTIA 500 預計於 2027 年大規模部署。
......
MTIA 450：生成式AI推論的飛躍

預見生成式AI推論需求的快速成長，我們將MTIA 400演進為MTIA 450，並透過推動四個領域優化生成式AI推理：

將 HBM 頻寬加倍於先前版本以加速解碼。
將 MX4 FLOPS 提升 75%，以加速專家混合（MoE）前饋網路（FFN）計算。
引入硬體加速，使注意力與FFN計算更有效率（例如，透過緩解Softmax與FlashAttention瓶頸）。
在低精度資料型態中創新。
MTIA 450 超越 FP8/MX8，提供 FP16/BF16 MX4 FLOPS 的 6 倍，反映低精度 FLOPS 在推論中的重要性。MTIA 450 也支援混合低精度計算，且不會產生資料型態轉換所帶來的軟體負擔。最後，它引入了我們自訂的資料型別創新，能維持模型品質並提升 FLOPS，且對晶片面積的影響極小。

MTIA 500：以更少資源交付更多生成式AI推論

隨著生成式AI推論需求持續成長，我們將MTIA 450升級為MTIA 500，以更具成本效益地推動生成式AI推論，HBM頻寬提升50%，HBM容量提升至80%，MX4 FLOPS提升43%。MTIA 500 進一步推動模組化理念，採用 2x2 的小型運算晶片組配置，周圍環繞多個 HBM 堆疊與兩個網路晶片組，並搭配一顆 SoC 晶片組，提供主機 CPU 與可擴展網卡的 PCIe 連線。與 MTIA 450 類似，MTIA 500 也引入了額外的硬體加速與資料型別創新，以解決生成式人工智慧推論中觀察到的瓶頸。

我們的策略：高速、推理優先，以及 PyTorch 原生

高速迭代晶片開發。

鑑於人工智慧創新的快速發展，我們已具備大約每六個月出貨新晶片的能力。這種快速的節奏帶來兩個優勢：

快速適應不斷演進的 AI 技術：隨著新模型架構、低精度資料類型與服務技術的出現，我們能優化最新晶片以適應這些進步，為重要操作員引入硬體加速，並解決計算、記憶體與輸入輸出之間的瓶頸轉移。
快速採用最新硬體技術：例如最新的製程節點、HBM及封裝技術。
我們透過可重複使用且模組化的設計，涵蓋晶片組、機箱、機架及網路基礎設施，實現高速發展。我們將加速器架構為晶片組系統——這些是運算、輸入輸出與網路的離散且可重複使用的組件。由於每個晶片組可獨立升級，我們能在數月內完成改進，而非數年。此外，不同製程節點可製造不同小晶片，以達到性能與功耗要求，成本效益最高。

在系統層級，MTIA 400、450 和 500 都使用相同的機箱、機架和網路基礎架構。因此，每一代新晶片都能納入相同的物理架構，加速從矽片到生產部署的過渡。我們的模組化、可重複使用設計也減少了開發與部署多代晶片所需的資源，而這些高度優化的晶片帶來的好處，能抵銷開發與部署所耗資源的不足。

推論優先

主流 GPU 通常為最嚴苛的工作負載——大規模生成式人工智慧預訓練——打造，然後應用於其他工作負載，如生成式人工智慧推論，通常成本較低。我們採取不同的方法：MTIA 450 和 500 先針對生成式 AI 推論進行優化，然後可依需求支援其他工作負載，包括 R&R 訓練與推論，以及生成式 AI 訓練。這使 MTIA 能夠密切關注生成式人工智慧推論需求的預期成長。

無摩擦採用

MTIA 從一開始就原生建立在業界標準的軟硬體生態系統上——PyTorch、vLLM、Triton 以及開放運算計畫（OCP），而非將採用與相容性視為事後考量。由於 PyTorch 起源於 Meta，並成為最廣泛使用的機器學習框架，MTIA 自然採用 PyTorch 原生的方法。PyTorch、vLLM 與 Triton 共同為開發者提供熟悉的軟體堆疊，允許重用開源社群的資產，並簡化模型遷移。除了業界標準軟體外，MTIA 的系統與機架解決方案也符合 OCP 標準，使 MTIA 能無縫部署於資料中心。"
