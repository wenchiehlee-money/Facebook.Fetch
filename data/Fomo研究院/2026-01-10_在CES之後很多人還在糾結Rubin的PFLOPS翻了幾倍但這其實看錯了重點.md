---
post_id: "122167862810771552"
title: "在CES之後，很多人還在糾結Rubin的PFLOPS翻了幾倍，但這其實看錯了重點。"
page_title: "Fomo研究院"
requested_url: "https://www.facebook.com/profile.php?id=61573146584049"
final_url: "https://www.facebook.com/people/Fomo%E7%A0%94%E7%A9%B6%E9%99%A2/61573146584049/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0WhEuW6aH4FuyNHKB5r8NCdHusREoLBBCm3VZfEcewyU4zZmr6MWoubd1AzV6tMkxl&id=61573146584049"
creation_time_utc: "2026-01-10T11:31:52+00:00"
fetched_at_utc: "2026-05-04T08:42:23.231444+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/613727776_122167862786771552_6569322011101108633_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=102&ccb=1-7&_nc_sid=7b2446&_nc_ohc=u1hmIu_fa-0Q7kNvwGe8Wq4&_nc_oc=AdqV3TqiPbTTSUfkCMctkI8-iGrJUNFKwv8sXKmaY4jjtKWODYULFecSTA9fThCHbCI&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=BMrwQ4F_oo8Igx8zyKWbIQ&_nc_ss=78100&oh=00_Af7ej2gdx_WIU3gwZMjDAX4pH8XLEOG-dl5nemXhgGj_5A&oe=69FE1A90"
feedback_id: "ZmVlZGJhY2s6MTIyMTY3ODYyODEwNzcxNTUy"
page_canonical_url: "https://www.facebook.com/people/Fomo%E7%A0%94%E7%A9%B6%E9%99%A2/61573146584049/"
---

# 在CES之後，很多人還在糾結Rubin的PFLOPS翻了幾倍，但這其實看錯了重點。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0WhEuW6aH4FuyNHKB5r8NCdHusREoLBBCm3VZfEcewyU4zZmr6MWoubd1AzV6tMkxl&id=61573146584049

![在CES之後，很多人還在糾結Rubin的PFLOPS翻了幾倍，但這其實看錯了重點。](https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-6/613727776_122167862786771552_6569322011101108633_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=102&ccb=1-7&_nc_sid=7b2446&_nc_ohc=u1hmIu_fa-0Q7kNvwGe8Wq4&_nc_oc=AdqV3TqiPbTTSUfkCMctkI8-iGrJUNFKwv8sXKmaY4jjtKWODYULFecSTA9fThCHbCI&_nc_zt=23&_nc_ht=scontent-tpe1-1.xx&_nc_gid=BMrwQ4F_oo8Igx8zyKWbIQ&_nc_ss=78100&oh=00_Af7ej2gdx_WIU3gwZMjDAX4pH8XLEOG-dl5nemXhgGj_5A&oe=69FE1A90)
在CES之後，很多人還在糾結Rubin的PFLOPS翻了幾倍，但這其實看錯了重點。

黃仁勳這次真正祭出的殺招，不是更強的GPU，而是「極致協同設計（Extreme Co-design）」。

這一次，NVIDIA不再只是給你一顆引擎，而是直接把整台F1賽車的底盤、傳動、甚至連維修站的補給系統（六顆晶片）全部焊死在一起。

▋核心困境：「網路之牆」

要理解Rubin的設計哲學，必須先理解AI基礎設施現在面臨的瓶頸：等待。

簡單來說，GPU的算力增長速度遠遠超過了數據傳輸的速度。結果就是，耗資數百萬美元的GPU叢集，其真實利用率常常只有40-50%。

剩下的時間，這些昂貴的矽晶片都在「空轉」，焦急地等待數據從網路的另一端緩慢爬來。這不僅是效率問題，更是經濟災難。

不斷推進GPU的性能其實也無濟於事，只要一天其他部件效率沒有提高，連接的效果沒有變好，真實利用率只會保持在低位。

Vera Rubin的誕生，就是為了用一種極其徹底的「系統工程」手段，徹底推倒這堵牆。

▋六位一體的協同作戰

Rubin平台的靈魂在於「極致協同設計」（Extreme Co-design）。這意味著平台上的六顆晶片，從設計的第一天起，就不是獨立的零件，而是作為一個統一的機櫃級系統被同時構思、同時優化。

讓我們來認識一下這顆晶片上的的每個成員：

1. Vera CPU — 數據總指揮：

在以訓練為主的時代，AI是「計算密集型」任務。GPU利用率高達85-95%，而CPU僅負責加載數據、調度任務，利用率低至10-20%。

當時的共識是：「CPU無關緊要，隨便一顆Xeon都能用。」

但到了2025-2026的「推理時代」，情況完全反轉。AI推理的第一步（把文字變標記）和最後一步（把標記變文字）都是CPU密集型的工作。

GPU處理一個Token只要微秒級，但CPU進行批次處理（Batching）可能要毫秒級。這1000倍的速度差，導致GPU有99%的時間在等CPU把下一批數據準備好。

當我們進入「長文本（Long-context）」和「代理型 AI（Agentic AI）」時代，CPU需要管理的KV Cache規模呈幾何級數增長。如果CPU慢，GPU利用率會直接從90%掉到40%。

這就是Vera CPU存在的理由。它並非一顆像Xeon那樣的通用CPU，而是一顆為AI協調而生的88核定製化Arm處理器。

它的架構被優化，專門用於處理Token化、請求批處理、以及在三級記憶體（GPU HBM4、CPU DRAM、ICMS儲存）之間進行複雜的KV Cache調度。

它與Rubin GPU之間那條1.8 TB/s的NVLink-C2C高速通道，正是為了實現這種無縫、低延遲的協調而存在。

▋2. BlueField-4 DPU — 基礎設施總管：

我們先來理解一下黃仁勳口中的「第三運算支柱」：DPU（數據處理單元）。它的唯一使命，就是在資料中心內高效地移動數據。

在現代的超大型AI資料中心裡，有一種東西叫 「資料中心稅」(Datacenter Tax)：意指CPU有大約30%~40%的效能都被浪費在處理網路封包、安全檢查這些「雜事」上，而不是在跑真正的AI程式。

有了DPU，它就能把這30%的雜事接手過來，CPU就能100%全力投入在指揮AI運算。一個DPU本質上是一個小型電腦，整合了多核CPU（負責控制）、高性能網路介面（負責數據處理）和硬體加速引擎。

這正是BlueField-4在Rubin體系中的角色。它內建一顆64核Grace CPU，專門處理所有與AI計算無關的「髒活累活」：網路封包處理、ICMS儲存I/O協調、安全隔離、遙測監控。

這就像為CEO配備了一個萬能的執行長辦公室，讓他可以專心於戰略決策。

正是因為BlueField-4接管了所有基礎設施工作，Vera CPU才得以被徹底解放，100%專注於更高價值的AI協調任務。

▋其餘成員：各司其職，協同作戰

2. Rubin GPU — 算力引擎：

50 PFLOPS的推理性能固然亮眼，但那只是標題。真正的重要在於22 TB/s的HBM4記憶體頻寬，是Blackwell的近三倍。

為何這如此重要？因為當前最前沿的長文本推理（Long-Context）和專家模型（MoE），瓶頸從來不在於計算，而在於記憶體頻寬。

3. NVLink 6 Switch — 機櫃內神經系統：

如果說GPU是肌肉，NVLink 6就是連接它們的神經。它將每顆GPU的雙向頻寬翻倍至3.6 TB/s，在72顆GPU之間建立了一個真正的「全通訊」（all-to-all）網路。

這徹底消除了MoE模型中因數據交換而產生的內部瓶頸，如同為大腦的每個神經元都建立了直連通路。

4. ConnectX-9 SuperNIC — 智慧交通警察：

傳統網卡是被動的。而SuperNIC則是一個主動的「交通警察」，它在數據流量產生的源頭就進行整形和擁塞控制。它不是在交通堵塞後去疏導，而是在一開始就杜絕了堵塞發生的可能。

5. Spectrum-6 Ethernet Switch — 跨系統高速公路：

如果NVLink 6是機櫃內的「局域網」，Spectrum-6就是連接數千個機櫃的「廣域網」。它採用了先進的矽光子技術，以5倍的能效提升，將整個資料中心連接成一個無縫的、巨大的AI工廠。

▋協同設計如何解決真實痛點？

還記得我前幾天提過的「推論上下文記憶體儲存平台」（Inference Context Memory Storage Platform）嗎？(還未看的快去看)

這之所以可能，是因為BlueField從設計之初就知道Spectrum-X的傳輸模式，而GPU的軟體也知道何時該預取數據等等。結果是，長文本處理速度提升5倍。

而專家模型(MoE)需要在大量GPU之間進行密集的「全通訊」，Blackwell的NVLink在超過60顆GPU後就會達到飽和。

在Rubin的架構中NVLink 6將頻寬翻倍，並將SHARP（網路內計算）功能直接整合進交換器，分擔了大量通信開銷。

這使得訓練同樣規模的MoE模型，所需的GPU數量僅為Blackwell的四分之一，代表效率上升了4倍。

▋從賣「零件」到賣「系統」，護城河的再次加深

Vera Rubin的發布，標誌著NVIDIA商業模式和競爭壁壘的重大轉變：

單一晶片的FLOPS競賽正在變得次要。AMD的MI500或許能在原始算力上追平Rubin GPU，但它能同時拿出與之完美匹配的BlueField、NVLink和全套軟體生態嗎？

這套六晶片協同設計的架構，與CUDA軟體生態深度綁定，創造了巨大的轉換成本。

客戶購買的不再是一塊GPU，而是一整套預先整合、深度優化的「AI工廠解決方案」。這種系統級的鎖定，遠比單一硬體的性能優勢更為堅固。

Vera Rubin 宣告了「拼湊零件」時代的結束，和「系統為王」時代的到來。

Rubin平台上的每一項技術單獨來看都是「進化」，但當它們被「協同設計」這個核心理念串聯起來時，其產生的化學反應是「顛覆性」的。

這個主題收錄在最新的<週末筆記>中，裡面包含了今年CES 2026中你最需要知道的主題。<週末筆記>完全免費，只需要訂閱就可以免費閱讀。

- KP
