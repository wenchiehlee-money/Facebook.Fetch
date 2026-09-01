---
post_id: "1461482932335075"
title: "----------\"Scale Up, Scale Out Get a New Partner\""
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0xAzDUMrMivJ35tS3Ku9iH7EK3Fj4rhD4ABZN4ipvWY1Av7ksh5Su9ZnnYp4h4biSl&id=100054201473657"
creation_time_utc: "2026-03-22T12:28:07+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-6/655559480_1461482382335130_8036008700782812258_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=IHCxvytM3KAQ7kNvwHHsdtz&_nc_oc=AdoJIy1djrpEeb5qbqwc3cjRR6hza28LbS6sUGOQG6yVYA60YaqXpQNDNYlUfpWAyVw&_nc_zt=23&_nc_ht=scontent-lax3-2.xx&_nc_gid=X8x8ak9uM3D8cC91Wc9UWA&_nc_ss=78100&oh=00_Af9swa7FIJHQ4YQxC-W94rV47AD-vOzLmjZGDXTgbljmtA&oe=6A3850A0"
feedback_id: "ZmVlZGJhY2s6MTQ2MTQ4MjkzMjMzNTA3NQ=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# ----------"Scale Up, Scale Out Get a New Partner"

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0xAzDUMrMivJ35tS3Ku9iH7EK3Fj4rhD4ABZN4ipvWY1Av7ksh5Su9ZnnYp4h4biSl&id=100054201473657

![----------"Scale Up, Scale Out Get a New Partner"](https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-6/655559480_1461482382335130_8036008700782812258_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=IHCxvytM3KAQ7kNvwHHsdtz&_nc_oc=AdoJIy1djrpEeb5qbqwc3cjRR6hza28LbS6sUGOQG6yVYA60YaqXpQNDNYlUfpWAyVw&_nc_zt=23&_nc_ht=scontent-lax3-2.xx&_nc_gid=X8x8ak9uM3D8cC91Wc9UWA&_nc_ss=78100&oh=00_Af9swa7FIJHQ4YQxC-W94rV47AD-vOzLmjZGDXTgbljmtA&oe=6A3850A0)
----------"Scale Up, Scale Out Get a New Partner"
----------"放大（Scale-up）著重於最小化延遲，而放大（scale-out）則更著重於抖動（jitter）。Scale-across 面臨類似 scale-out 的挑戰
Scale-up focuses on minimizing latency, while scale-out focuses more on jitter. Scale-across has challenges resembling those of scale-out, but it gets a new name because at least some companies address jitter differently over longer distances.

這些概念主要適用於人工智慧與高性能計算（HPC），這些是必須投入大量運算與記憶體的主要工作負載。高性能計算（HPC）已經面臨這個問題一段時間，而人工智慧——無論是訓練還是推理——則以其驚人的演進速度與之相撞。

「HPC 在技術需求上幾乎與 AI 擴展，甚至在某種程度上與 AI 擴展完全一致，」Broadcom 核心切換團隊產品線經理 Robin Grindley 表示。

有些人認為擴展是南北網路，而擴展則是東西網路。跨尺度可以被視為較長距離的尺度，也就是東西向。Cadence 矽解決方案集團設計智慧財產資深行銷總監 Arif Khan 指出：「資料中心中的東西向與南北向網路截然不同。」
Some think of scale-up as a north/south network, with scale-out being an east/west network. Scale-across can be thought of as a longer-distance scale-out, so it would also be east/west. “The east/west and north/south networks in the data center are very different,” noted Arif Khan, senior product marketing group director for design IP in Cadence’s Silicon Solutions Group.
......
Start with scale-up
Scale-up attempts to aggregate compute resources (GPUs, for the most part) to look like one big processor rather than a collection of smaller processors. “The whole idea of this machine learning model is to create a cluster of compute facilities,” explained Priyank Shukla, director of product management, interface IP at Synopsys. “It could be accelerators, it could be GPUs, and you throw a lot of data at this compute facility, and you get a trained model out of it.”

Scale-up is characterized by four primary attributes.

The main interconnect metric to optimize is latency.
It employs so-called memory semantics. That effectively means that all processors see the same memory space.
Assignment of resources is typically static, handled at boot-up.
The shorter distances (relative to scale-out and scale-across) mean that copper is still a viable interconnect technology.

「延遲是關鍵，」Nvidia 網路資深副總裁 Gilad Shainer 表示。「高訊息速率也很重要。它本質上是做載入/儲存操作、網路內運算，以及對計算結果的不同層級的減少。你需要一個支援龐大頻寬的設備，相較於擴展型基礎設施——頻寬是 10 倍。你是在 GPU 間傳輸資料，並且希望它們完全同步，成為一個整體。」
 You need something that supports massive bandwidth compared to a scale-out infrastructure — 10X the bandwidth. You’re moving data between GPUs, and you want them completely synchronized to become one unit.”

記憶體語意實際上允許直接存取本地記憶體，提供最低的延遲。抖動依然存在，就像任何快取系統一樣。如果請求的資料已經存在快取中，延遲會比從 HBM 或 DRAM 擷取時低得多。但如果從記憶體而非快取移動所產生的額外延遲，仍遠小於擴展時可能遇到的延遲。
Memory semantics effectively allow direct access to local memory, which provides the lowest latency. Jitter will still be present, just as it is in any cached system. If a requested piece of data is already in cache, latency will be far lower than if it’s fetched from HBM or DRAM. But any extra delays incurred on a trip to the memory instead of the cache would still be far smaller than what scale-out might experience.

「記憶語意意味著一個加速器所看到的記憶空間，可以透過其他加速器存取，」Shukla 說。「有記憶一致性，意思是加速器看到的東西，其他加速器也會看到同樣的東西。不同的叢集架構用來訓練不同的模型，而在某些叢集中，為了達到這種記憶體效率，你會在功耗和面積上做出妥協。」
“Memory semantics means the memory space one accelerator sees is accessible through other accelerators,” said Shukla. “There is memory coherency, meaning whatever an accelerator sees, other accelerators see the same thing. Different cluster architectures are used to train different models, and in some of these clusters, you compromise on power and area to get this kind of memory efficiency.”

最小化跳數
利用互連結構將 GPU 整合在一起，可能會增加額外延遲，這取決於資料從記憶體路由到請求處理器的情況。早期版本只有一個跳點來取得資料，但有些版本正在考慮多層交換器，可能需要多跳。這種情況下，抖動會稍微上升，但從整體來看，非常低。

「UALink 1.0 被定義為單跳協定，聯盟內部討論單跳可能不夠好，」Cadence 的 Khan 說。「你可能需要考慮多層交換器拓撲，如果你知道資料中心的拓撲如何擴展，以及工作如何分割，就能用靜態路由填充這些路徑。」

適當資源的編排也會在程式載入時進行。靜態配置的特性消除了即時取得資源可能產生的額外延遲。

這個領域也仍在抗拒轉向光互連的誘惑。對於較短距離，銅線可以是較低功耗的技術，因為驅動器只需將資料傳輸到機架高度（若使用中置開關則是機架一半）。光纖電纜僅需電力產生一束光，資料才會傳送到任何地方，因此短距離連接效率不如銅線。較長的銅線則需要更強的驅動器，這正是光纖技術成為競爭的地方。

「我們正盡量在那個區域利用銅，」謝納說。「銅是最省錢、高度可靠，且不耗電的。」

我們至少看到兩種擴展標準（UALink 和一種新的乙太網路變體）。好消息是物理層是相同的;不同的是協定本身。

「不論技術或協定為何，它都是 224G serdes（如果忽略 AMD 作為副業嘗試做的 UALink-128），但其他一切都是基於乙太網路規範，」Khan 指出。「這很有幫助，因為現在你的實體媒介不管是哪個協定都一樣。不同的是上面的協定堆疊。」

Synopsys 的產品管理總監 Rob Kruger 表示：「這些協議都在達成同一目標，只是在功能和底層細節上略有不同。」「不同的客戶會因為某些原因選擇其中一種，不論是因為舊有系統，還是他們認為該協定本身有價值的某些特性。」
......
擴展式（Scale-out）則帶來來自不同機架的資料。它具有以下特點：

主要的互連優化指標是封包抖動。
它採用 RDMA（遠端 DMA）語意，而非記憶體語意。
資源在計算過程中會根據需要動態分配與釋放。
距離變遠，光學技術也開始逐漸普及。
這比較像是一種網路模式。擴展是記憶體位址，而擴展擴展則是傳送封包。顯然，低延遲在這裡也不錯，但問題更多是抖動。
The main interconnect metric to optimize is packet jitter.
It employs RDMA (remote DMA) semantics rather than memory ones.
Resources are dynamically assigned and released as necessary during computation.
Distances are longer, and optical is starting to make inroads.

具體來說，如果封包被丟棄，必須重新發送。如果一個計算有許多實體等待資料以便同步進行，那麼重傳那個封包會迫使其他人等待。讓昂貴的硬體閒置等待可不好。

因此，協定必須是無損的。盡力而為是不夠的。
Protocols, therefore, must be lossless. Best effort isn’t good enough.

不同的叢集可以共享各自記憶中的資料，但它們屬於不同的記憶空間。「根據模型的規模，有些資料可以在一個叢集處理，有些則在另一個叢集中處理，」Shukla 說。「他們可以共享資料——不是記憶，而是指標和張量。」
Different clusters can share data from their respective memories, but they’re different memory spaces. “Based on the size of the model, some data can be worked in one cluster and some in another,” said Shukla. “They can share data — not memory, but pointers and tensors.”

在這裡，出現了新的機器學習模型。「我們不只是在談變形金剛，」舒克拉說。「我們也在討論專家與代理人模型的混合。這些模型為一個模型建立一個叢集，並有另一個叢集執行該模型的另一個版本。而且他們需要在這兩個人之間傳輸資料，而你不可能用單跳開關把所有東西都連接起來。」
Here, there are new machine-learning models. “We are not talking only about transformers,” Shukla said. “We are also talking about mixture-of-experts and agentic models. These models create one cluster for one model and have another cluster that runs another version of that model. And they need data to be transmitted between these two, and you can’t connect all of them with single-hop switches.”

與啟動時設定的擴展不同，擴展資源通常是動態新增的。某些配置可能需要機架間的一致性，但通常不需要。
Unlike scale-up, where the configuration is established at startup, scale-out resources are typically added dynamically. Some configurations may require coherence between racks, but not usually.

舒克拉指出：「加速器是平行分配工作，然後共同累積結果。」「所以你不需要對現在訓練的大多數模型有完整的記憶一致性。」
“Accelerators split work in parallel, and then they accumulate results together,” Shukla noted. “So you don’t need full memory coherency for most of the models being trained today.”
......
In countries where GPUs aren’t as powerful, given geopolitical restrictions, companies may try to bring two or three racks into the scale-up cluster in order to have sufficient GPU power.

“In China, the GPUs are more performance-constrained,” said Maurice Steinman, vice president of engineering at Lightelligence. “If individual nodes have a fraction of the performance of a strong Nvidia or AMD node, the scale-up domain needs to be wider for a given unit of performance in a cluster.”
......
但資料中心的資源終究會耗盡。「我可以有足夠的電力處理10萬到30萬台伺服器，但如果想做到百萬台，我就必須把資料中心分散在不同地方，而且我確實需要以能同時執行單一工作負載的方式連接它們，」Shainer 說。

處理這些問題似乎意味著要進一步擴展到另一個校區。但顯然距離是很重要的。跨規模擴展的運作方式與擴展類似，但處理擁塞的演算法與方法會改變。這使得規模擴大與跨界規模的關係，比規模擴大與擴大規模更為接近。

在此，謝納提供了一個比喻。「如果你在市區開車，想快速從一個地方到另一個地方，你會開得非常靠近前車，」他說。「如果前面的車踩煞車，你也會踩煞車，因為你的空間很小。所以你在控制交通方面會更積極。如果你開更長的距離，車輛間會有更明顯的距離，因此如果你看到前面有車煞車，你有足夠時間反應，所以你會變得不那麼激進，控制方式也會不同。」

Each data center will go its own way
Every data center — or at least every AI data center — will implement these scaling strategies, but they’ll likely do them differently.

“[When training GPT3], Nvidia used NVLink as a scale-up protocol and InfiniBand as scale-out,” said Shukla. “At the same time, Google has always used ICI [inter-chip interconnect], which is based on PCIe, for scale-up, and they have used Ethernet for scale-out.”

It’s important to remember that these descriptions apply to networks and data centers today. The definitions aren’t necessarily fixed. We’ve already seen some blurring between scale-up and scale-out depending on the country. That may continue as data centers evolve. “The lines between scale-up, scale-across, and scale-out seem to be blurring,” cautioned Steinman."

https://semiengineering.com/scale-up-scale-out-get-a-new-partner/
