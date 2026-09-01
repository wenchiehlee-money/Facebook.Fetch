---
post_id: "1597044982112202"
title: "Google TPU v8"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid036Wq6mi2xmCQgy7HqPYVPT4YdPnu9Vkq5ryVSLJmUPKUfhsozG1wKGsgD7oFY6PAJl&id=100054201473657"
creation_time_utc: "2026-08-29T10:57:15+00:00"
fetched_at_utc: "2026-09-01T04:42:39.947356+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid036Wq6mi2xmCQgy7HqPYVPT4YdPnu9Vkq5ryVSLJmUPKUfhsozG1wKGsgD7oFY6PAJl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU5NzA0NDk4MjExMjIwMg=="
page_canonical_url: ""
---

# Google TPU v8

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid036Wq6mi2xmCQgy7HqPYVPT4YdPnu9Vkq5ryVSLJmUPKUfhsozG1wKGsgD7oFY6PAJl&id=100054201473657
Google TPU v8

1. CPU從x86改為自己的Axion Arm CPU ASIC

2. 8t單計算晶片/6 HBM、8i雙計算晶片/8 HBM/SRAM較大

3. 過去Google 3D Torus拓樸，這對訓練來說比推理更理想，8i改為BoardFly拓圖，通常延遲較低，這對推論很重要，8i的 BoardFly網路最大只需要7跳，而3D Torus最多要16跳

4. 目前已有Open AI Jalapeño和Google TPU兩家公司公開展示其使用AI幫助整個IC晶片設計流程，從RTL design term、AI designer、AI Optimizer、Physical Design Team......"Using AI/TPUs to Build the next AI/TPUs"，這對於所有的IC設計/Fabless公司，包含IC Design Service公司，都是一個明確的信號: AI不只是降本增效，還是攸關生死的競爭力事項: design cycle大幅縮短之下的time to market

------------"除了提供自家內部晶片設計以供推論外，TPU 8i 也因是 Google 自家開發的 CPU Axion 的主要用戶而聞名。TPU 8i 晶片與 Axion CPU 以 2 比 1 的比例配對安裝在 Google 節點內。之前公司使用 x86 CPU 來完成這項任務，因此轉用 Axion 不僅讓 Google 採用自家硬體，也同時轉向 Arm 架構。
......
該公司大致上在推論優化晶片與訓練優化晶片之間交替使用
......
今年，他們改為一年內做兩顆晶片，而不是輪流。由於應用範圍更廣，他們越來越需要獨立晶片。尤其是 MoE，因為它比早期模型更需要通訊和網路流量，帶來新的瓶頸。僅僅提升浮點運算（FLOPS）是不夠的。

這一代硬體也更能優化以處理代理型人工智慧（agentic AI）長的上下文視窗。
......
但重點是，推論每單位運算需要更多的 HBM。推論也需要較高比例的 SRAM 來計算。

從推論成本來看，延遲越低，價格越快上升。這是推論吞吐量隨著每用戶速率升高而下降的經典點。

針對自家晶片，Google 投資了更多 SRAM、更多記憶體和 8i 的頻寬。
......
從推論成本來看，延遲越低，價格越快上升。這是推論吞吐量隨著每用戶速率升高而下降的經典點。

針對自家晶片，Google 投資了更多 SRAM、更多記憶體和 8i 的頻寬。

過去，Google 曾使用過 3D 環面。這對訓練來說比推理更為理想。飛網通常延遲較低，這對推論很重要。8i 的 BoardFly 網路最大有 7 跳，而環面則有 16 跳。
......
TPU8i 的設計優化以有效執行網路內集體。此處理在晶片邊緣靠近網路硬體的 ICI I/O 晶片中處理，而非在運算晶片中處理。這節省了傳輸到計算晶片的時間（包括實際移動資料的時間），同時也省去了 HBM 存取。
......
從高層次來看，8i 與先前的 TPU 推論設計相似。每個封閉的盒子是計算晶片，而紫色盒子則是 I/O 晶片。
......
訓練需要大量的浮點操作和大量的連結。這也是晶片設計的重點所在。

Training requires lot of FLOPS, and lots of connectivity. Which is where the focus has been in the design of the chip.

從整體來看，8t superpod 將搭載 9600 顆晶片，並可存取總共 2PB 的共享 HBM 記憶體。在計算量方面，這是 FP4 計算的 121 EFLOPS。在能源效率方面，這台每瓦的孔徑約為 TPUv7 Ironwood 的兩倍。

然而，並非所有函數都對應到FP4。因此，雖然 FP4 非常實用，但晶片必須有效處理混合的精密訓練複製，這也是 Google 能達到每瓦 2 倍效能的原因。

以下是透過 Google 光學電路交換器（OCS）實現 9600 晶片規模擴展的案例。它同時提供冗餘與可靠性。OCS 可以從較大的 pod 內部動態配置切片。可以創造任何切片大小或形狀。

OCS 也會處理壞晶片，晶片壞掉時丟棄，分配備用節點，從檢查點恢復，然後繼續前進。

Here’s a look at a 9600 chip scale-up domain via the use of Google’s optical circuit switch (OCS). It provides both redundancy and reliability. OCS can dynamically configure slices from within the larger pod. Any slice size or shape can be created.

OCS also handles bad chips, dropping chips when they go bad, allocating a spare node, restoring from a checkpoint, and then moving on.

在前一代的 TPU 中，Google 使用其整體資料中心網路。但 8t 版本改變了，他們引入了專用的 Virgo 網路架構。這支援單一域內的 134K TPU，頻寬為 47 Pbit/s。

Virgo 採用兩層切換拓撲。

In previous generation TPUs, Google used their overall data center network. That changes in 8t, where they introduce the dedicated Virgo network architecture. This supports 134K TPUs in a single domain, for 47 Pbits/second of bandwidth.

Virgo uses a two layer switching topology.

一如既往，RAS 是 Google 的重大優先事項。工作假設是晶片會不穩定，因此架構必須能考慮到這點並繞過故障晶片。本世代新增的 RAS 功能之一是現場單元測試，該系統會在閒置週期中執行，測試晶片是否有任何部分故障。

故障率也會隨溫度呈指數成長，這也意味著冷卻對 Google 來說至關重要。阿累尼烏斯方程式指出，化學劣化（以及半導子磨損）大約每升高10-15°C就會加倍。
......
這是 8t 的方塊圖，與過去的設計非常相似。僅有少數針對訓練的特性有所更改。

還有一整套完整的 TPU 8t 托盤，每個托盤有 4 個 TPU。這是 Google 首次同時進行液冷。之前這些都是風冷的。

接著，我們有8t的機架。Google 的超級群組中有 300 個。

Google 也利用 AI 來協助設計他們的 TPU。這些 AI 模型成功削減了 TPU 8t 的功耗，並節省了訓練與推論晶片的多個部分空間，使 Google 能夠整體擴充更多計算核心。
......
Google 也利用 AI 來協助設計他們的 TPU。這些 AI 模型成功削減了 TPU 8t 的功耗，並節省了訓練與推論晶片的多個部分空間，使 Google 能夠整體擴充更多計算核心。
......
在軟體方面簡要說明，現有的程式碼庫與 TPUv8 世代完全相容。雖然使用 Google 的自訂核心語言 Pallas，但直接用 Python 撰寫具硬體感知的內核，能在 8t 和 8i 上提供最佳效能。

And briefly on the software front, existing codebases are fully compatible with the TPUv8 generation. Though using Google’s custom kernel language, Pallas, allows writing hardware-aware kernels directly in Python will deliver the best possible performance on both 8t and 8i.

過去十年來，Google 一直在打造訓練與推論晶片。這次他們是透過兩者一起加速。但他們整體的設計理念並未改變，採用軟體（編譯器）與硬體開發者之間的緊密共同設計連結，以避免執行時超出必要的工作。"

https://www.servethehome.com/googles-tpuv8s-for-training-and-inference-at-hot-chips-2026/
