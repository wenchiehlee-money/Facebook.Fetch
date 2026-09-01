---
post_id: "1453310593152309"
title: "----------\"Lumentum 和 Coherent 可以為 Nvidia 提供許多幫助。首先，就像 CPO 已被添加到 Quantum-X InfiniBand 和 Spectrum-X 乙太網路橫向擴展網路（特別是其交換器 ASIC）中一樣，我們認為最終也必須將 CPO 添加到 Nvidia 的 GPU 計算引擎和 NVSwitch 中。即使 Nvidia 在機架中加入了中板，以取代目前在其「Oberon」NVL72 機架中使用的所有銅纜，情況依然如此。 GPU 的頻寬遲早會提升，而 GPU 邊緣的實體空間不會增加——事實上，多晶片插槽反而加劇了運算和快取面積與插槽週長之比這一問題，而不是改善。in fact, multichip sockets make the beachfront issue – area of compute and cache compared to the circumference of the socket – worse. Not better."
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02FeM8Wv384XhWSr7egpaZJLPP781zsxhzpRf8xvbRkwz5EKD5oToioSWL77AUu1y4l&id=100054201473657"
creation_time_utc: "2026-03-12T09:20:28+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02FeM8Wv384XhWSr7egpaZJLPP781zsxhzpRf8xvbRkwz5EKD5oToioSWL77AUu1y4l&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ1MzMxMDU5MzE1MjMwOQ=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# ----------"Lumentum 和 Coherent 可以為 Nvidia 提供許多幫助。首先，就像 CPO 已被添加到 Quantum-X InfiniBand 和 Spectrum-X 乙太網路橫向擴展網路（特別是其交換器 ASIC）中一樣，我們認為最終也必須將 CPO 添加到 Nvidia 的 GPU 計算引擎和 NVSwitch 中。即使 Nvidia 在機架中加入了中板，以取代目前在其「Oberon」NVL72 機架中使用的所有銅纜，情況依然如此。 GPU 的頻寬遲早會提升，而 GPU 邊緣的實體空間不會增加——事實上，多晶片插槽反而加劇了運算和快取面積與插槽週長之比這一問題，而不是改善。in fact, multichip sockets make the beachfront issue – area of compute and cache compared to the circumference of the socket – worse. Not better.

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02FeM8Wv384XhWSr7egpaZJLPP781zsxhzpRf8xvbRkwz5EKD5oToioSWL77AUu1y4l&id=100054201473657
----------"Lumentum 和 Coherent 可以為 Nvidia 提供許多幫助。首先，就像 CPO 已被添加到 Quantum-X InfiniBand 和 Spectrum-X 乙太網路橫向擴展網路（特別是其交換器 ASIC）中一樣，我們認為最終也必須將 CPO 添加到 Nvidia 的 GPU 計算引擎和 NVSwitch 中。即使 Nvidia 在機架中加入了中板，以取代目前在其「Oberon」NVL72 機架中使用的所有銅纜，情況依然如此。 GPU 的頻寬遲早會提升，而 GPU 邊緣的實體空間不會增加——事實上，多晶片插槽反而加劇了運算和快取面積與插槽週長之比這一問題，而不是改善。in fact, multichip sockets make the beachfront issue – area of compute and cache compared to the circumference of the socket – worse. Not better.

Lumentum 和 Coherent 還有另一個引人注目之處：它們都採用了光路開關optical circuit switches。這意味著，如果英偉達在其擴展網路中採用光路開關作為骨幹，理論上，透過對其 AI 集群拓撲結構進行一些調整，就可以建立一個容量更大、能效更高的 NVSwitch 記憶體域。And that means that Nvidia could, in theory and with some changes in the topology of its AI clusters, build a much larger NVSwitch memory domain – and one that was much more power efficient – if it had an OCS as the spine in its scale up networks.

Lumentum 的 R300 光路開關是基於與 Google 在其「Palomar」MEMS 裝置中採用的相同的微機電系統 (MEMS) 鏡技術。 「Palomar」MEMS 裝置是「Apollo」光路開關 (OCS) 的一部分，而「Apollo」OCS 是過去四代 Google TPU 系統（準確來說是 TPU v4 到 TPU v7）的骨幹。之前的 TPU v1 到 TPU v3 機器採用的是硬連線設計，就像如今 Nvidia 的 GB200 NVL72 和 GB300 NVL72 系統一樣。 ）

光路開關切換設備間特定連結的速度並不快－旋轉微鏡重新配置連接任兩個裝置的任兩根光纖之間的連結需要幾十毫秒的時間。對於需要頻繁進行動態記憶體重配置的交換記憶體架構來說，這個速度太慢了。

但是，遺憾的是，對於人工智慧叢集的記憶體結構的核心——網路的最頂層——並沒有太多理由經常改變它。事實上，Google擁有一個 3D 環面網絡，可以將 9,216 個“Ironwood”TPU v7p 計算引擎聚集到一個共享內存域中，並且通過旋轉幾個鏡像，它可以將該內存域分割成更小的塊，並出售更小的 AI 超級計算機來運行較小的工作負載。

關鍵在於，網路配置更改頻率極低，網路主幹鏈路採用光纖傳輸，光訊號直接在光纖間反射，無需像乙太網路或InfiniBand交換器那樣進行光纖傳輸（無論是在交換器外部的收發器還是內部的CPO中）。如果沒有光路交換機，就無法避免這種功耗。

但如果您擁有像 Lumentum 去年三月發布的 300x300 連接埠 R300 這樣的 OCS 交換器（目前已向多家超大規模資料中心和雲端平台供應商提供樣品），那麼在擁有 10 萬個 XPU 的 AI 叢集系統中，您可以將整體網路功耗降低 65%。 （這是 Lumentum 聲稱的。）電力和時間一樣，都是金錢。延遲也是如此。 Lumentum 表示，OCS 交換器的延遲比乙太網路交換器低 5 到 10 倍。 （前提是設定完成。）以下是 Lumentum OCS 交換器的外觀：

Coherent公司剛開始交付一款以液晶技術為基礎的OCS交換機，目前已有七家客戶正在進行試用。這款資料中心Lightwave交叉連接（DLX）交換器提供64x64連接埠、320x320連接埠和512x512連接埠三種版本。以下是DLX OCS交換器的外觀：

Nvidia 可能正在敲定雷射器的供應協議，但我們強烈懷疑，在「Rubin Ultra」世代的某個時候，當帶有銅中板的新型「Kyber」機架推出時，Nvidia 可能會轉向環形或蜻蜓互連拓撲結構（而不是當前 NVSwitch 記憶體結構的完全連接的樹拓撲結構），並使用 OCS 主幹線將它們全部連接起來。

我們認為英偉達希望 CPO 使用多供應商雷射器，但從長遠來看，它也希望 OCS 設備有兩家供應商。"

https://www.nextplatform.com/connect/2026/03/02/nvidia-sees-the-light-on-silicon-photonics-and-maybe-optical-switching/4093099
