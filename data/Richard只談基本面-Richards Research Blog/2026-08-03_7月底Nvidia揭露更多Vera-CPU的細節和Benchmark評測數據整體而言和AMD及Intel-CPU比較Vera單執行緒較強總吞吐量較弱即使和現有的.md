---
post_id: "1574618364354864"
title: "7月底Nvidia揭露更多Vera CPU的細節和Benchmark評測數據，整體而言，和AMD及Intel CPU比較，Vera單執行緒較強、總吞吐量較弱，即使和現有的AMD/Intel比較Vera的總吞吐量都輸，何況下一代AMD Venice即將來到，總吞吐量可能輸更多"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02LTe7rerurnXDeZ3kL4ehN4miUVASongPLvXZktbNqrLuyoN53P9bHT3HaLzJ4iovl&id=100054201473657"
creation_time_utc: "2026-08-03T15:30:04+00:00"
fetched_at_utc: "2026-09-01T04:42:39.947356+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02LTe7rerurnXDeZ3kL4ehN4miUVASongPLvXZktbNqrLuyoN53P9bHT3HaLzJ4iovl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU3NDYxODM2NDM1NDg2NA=="
page_canonical_url: ""
---

# 7月底Nvidia揭露更多Vera CPU的細節和Benchmark評測數據，整體而言，和AMD及Intel CPU比較，Vera單執行緒較強、總吞吐量較弱，即使和現有的AMD/Intel比較Vera的總吞吐量都輸，何況下一代AMD Venice即將來到，總吞吐量可能輸更多

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02LTe7rerurnXDeZ3kL4ehN4miUVASongPLvXZktbNqrLuyoN53P9bHT3HaLzJ4iovl&id=100054201473657
7月底Nvidia揭露更多Vera CPU的細節和Benchmark評測數據，整體而言，和AMD及Intel CPU比較，Vera單執行緒較強、總吞吐量較弱，即使和現有的AMD/Intel比較Vera的總吞吐量都輸，何況下一代AMD Venice即將來到，總吞吐量可能輸更多

結論就是，x86 Server CPU在Performance方面還是有其強項

----------"深入探討 NVIDIA Vera CPU 新架構細節
..........
From Olympus to Vera: NVIDIA’s Scalable Coherency Fabric 2
......
其中一個差異化點是 Vera 的 CPU 都安裝在同一塊矽晶片上。雖然 NVIDIA 在 Vera 上採用晶片組chiplets，但它們依功能細分：CPU 核心、輸入輸出與記憶體控制器。這與目前 AMD 和 Intel 的晶片設計相當不同，兩者都將 CPU 核心分散在多個晶片組chiplets——AMD 甚至多達十幾個晶片組chiplets

但這些 CPU 核心是怎麼互相溝通的呢？我們終於透過 NVIDIA 的可擴展相干結構（scalable coherency fabric; SCF）找到答案。從高層次來看，這實際上將 Vera 計算晶片拆分成四個象限/叢集

每個象限又由單一相干交換節點（coherency switch node; CSN）錨定，負責在連接的 CPU 核心、L3 快取、記憶體控制器與 I/O 控制器間路由流量。CSN 也會彼此連接，方便流量流向非本地叢集的 CPU 核心或記憶體控制器時使用。

如 NVIDIA 的圖示所示，每個 CSN 會搭配兩個 CPU 核心叢集（每個 11 個核心），以及兩個 L3 快取區塊（每個 20.5MB）。最後，每個 CSN 有一個記憶體交換節點（Memory Switch Node; MSN）連接相鄰的記憶體控制器晶片組，以及一個橋接交換節點（Bridge Switch Node; BSN）連接 I/O。有趣的是，由於 Vera 只有一個 I/O 晶片組和一個 NVLink-C2C 介面，兩者皆由成對的 BSN 共享。同時，這也表示某個 BSN 會被連接其中一種，而非兩者兼有——也就是說，從 CPU 核心到任一 I/O 介面所需的跳數，會依其較接近哪個介面而異。與本地記憶體存取不同，並非所有核心都與 I/O 出口相等距離。

整體而言，SCF 提供了龐大的頻寬。根據 NVIDIA 的資料，整個結構的頻寬是 3.4TB/秒，略高於整個外部記憶體子系統頻寬的 2.8 倍多。因此，NVIDIA 表示該結構速度足夠快，讓晶片即使採用叢集式組織，仍能有效地作為一顆大型 CPU，每個 CPU 核心都能存取其他 L2 快取池或 MSN，且不會有顯著的延遲損失。換句話說，允許 NVIDIA 採用分散式快取（及分散式一致性）架構，同時維持類似較小單晶片設計的延遲

Vera 效能：偏好單執行緒效能勝過總吞吐量
Vera Performance: Favoring Single-Threaded Performance Over Total Throughput
......
每個人都想展現最好的一面，NVIDIA 在這方面也不例外。這不僅反映在他們選擇的基準測試上——NVIDIA 有單執行緒效能的幻燈片，但沒有多執行緒吞吐量——以及 NVIDIA 的競爭對象：AMD 的 EPYC 9755「Turin」。
......
這仍然是蘋果對蘋果，但可能是在比較紅蘋果和青蘋果
......
這些數據仍讓 Vera 在所有 SPEC CPU 2026 整數基準測試中，單執行緒工作負載都領先
......
NVIDIA 白皮書中還有幾張圖表，也顯示 Olympus 在單執行緒架構上表現優異。以 SPEC CPU 2026 基準測試的一部分為例（NVIDIA 領先 AMD 最大），公司顯示指令擷取操作每週期提升 1.9 至 2.4 倍不等。
......
但未被提及——也是 NVIDIA 開始動搖的地方——是整體晶片吞吐量，而非單核心效能。NVIDIA 的投影片並未提及此問題，甚至他們的白皮書也主要聚焦於單執行緒或中等執行緒的工作負載。直到白皮書最後，當 NVIDIA 公布他們的 SPEC CPU 2026 整數結果時，才提到總晶片吞吐量。結果也沒那麼樂觀。
......
如果我們深入探究官方 SPEC CPU 2026 整數率結果，以更了解 Vera 與其他已發表系統的比較，會發現多款雙插槽系統領先 Vera，包括使用 AMD 自家編譯器達成超過 1000 分的 EPYC 9755 系統。同時，也有EPYC 99×5（都靈密集）系統在相同情境下得分超過1200分。
......
該公司表示，他們設計了高 IPC CPU 核心用於伺服器，特別是針對代理型 AI 工作負載，而今天公布的所有架構細節都支持這點。Olympus CPU 核心非常龐大，不僅晶片大小，前後端的寬度也相當龐大。NVIDIA 採用了多項（無疑會佔晶片空間）功能，例如圖預取，進一步提升每個 CPU 核心的效能。我不認為目前所呈現的許多內容會讓一般 CPU 愛好者感到驚訝，但 Olympus 及其基礎打造的 Vera CPU 看起來是一套設計良好的高效能 CPU 架構。

但這對效能的影響相當複雜，因為從多個角度來看這顆晶片——而且這些角度都合理。一旦 Vera 出貨，第三方可以自由跑基準測試，我一點也不意外 NVIDIA 真的能在單執行緒整數效能上超越現有伺服器晶片領域。當然，Olympus/Vera 似乎是為了贏得這點而設計，而 NVIDIA 向 Vera 提出的工作負載也反映了這個設計目標
......
然而，僅有 88 個 CPU 核心，即使 IPC 很高，NVIDIA 在高吞吐量工作負載下仍難以勝出。在這種情況下，現世代晶片如 AMD 的 EPYC 99xx（Turin Dense）和 Intel 的 Xeon 6+（Clearwater Falls）已經能超越 Vera。

問題就在這裡：這些是與現世代晶片的比較。Vera 的發行時間意味著 NVIDIA 最多只能有短暫的機會窗口，之後 AMD 將開始推出基於即將推出的 Zen 6 架構的 EPYC「Venice」晶片。Venice 正逐漸與 Vera 競爭，且以 16 通道 DDR5-12800 等規格來說，88 核心的 Venice 應該能在 Vera 記憶體頻寬的 10-20% 範圍內。同時，Venice 也會帶來自己的 IPC 與單執行緒效能提升。我們也預期 Venice 擁有比 Vera 更多的 PCIe Gen6 通道，且每個插槽最多可達 256 核心，整體吞吐量能大幅提升。

https://www.servethehome.com/diving-deeper-on-nvidias-vera-cpu-new-architectural-details-and-spec-cpu-2026-benchmarks/3/
