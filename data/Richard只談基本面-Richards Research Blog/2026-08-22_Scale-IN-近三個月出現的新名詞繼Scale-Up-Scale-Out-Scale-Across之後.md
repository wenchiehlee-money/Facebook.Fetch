---
post_id: "1591014012715299"
title: "Scale-IN 近三個月出現的新名詞(繼Scale Up, Scale Out, Scale Across之後)"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02UfFVyGjQupx5V6XBLZC49qcFjB2V7DkQ2cE7uQ6Yjqu1YysdBcynjD9jdMcaKoEbl&id=100054201473657"
creation_time_utc: "2026-08-22T10:09:51+00:00"
fetched_at_utc: "2026-09-01T04:42:39.947356+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU5MTAxNDAxMjcxNTI5OQ=="
page_canonical_url: ""
---

# Scale-IN 近三個月出現的新名詞(繼Scale Up, Scale Out, Scale Across之後)

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02UfFVyGjQupx5V6XBLZC49qcFjB2V7DkQ2cE7uQ6Yjqu1YysdBcynjD9jdMcaKoEbl&id=100054201473657
Scale-IN 近三個月出現的新名詞(繼Scale Up, Scale Out, Scale Across之後)
Google網路從OCS Tours到Dragonfly拓樸

------------"近年來，規模內斂（scale-in）也開始出現。「這是一個新詞，僅在三個月內才開始，」Ayar Labs 產品管理主管 Vishal Chandrasekar 表示。「它指的是從 GPU 輸出的頻寬，並維持在單一機箱內的數量。」

這些定義直到最近，可以總結如下： 

擴展內是指單一伺服器或單一電路板上的處理器間。
Scale-in is between processors in a single server or on a single board. 

放大是在機架內，使用銅線接線，允許使用記憶體語意進行程式設計。（劇透警告：這篇內容已過時。） 
Scale-up is within a rack, wired using copper, and allows programming using memory semantics. (Spoiler alert: this is now out of date.) 

擴展是在機架間進行，並採用乙太網路 RDMA 語意。它越來越多地使用光纖互連。 
Scale-out is between racks and employs Ethernet RDMA semantics. It increasingly uses optical interconnect. 

跨地擴展是指不同資料中心園區間，並涉及光纖。
Scale-across is between different data-center campuses and involves fiber.

除了擴大內（scale-in）之外，擴大化（scale-up）也在不斷演進。運算叢集正逐漸超越單一機架的範圍，招募鄰近機架中的伺服器。現在互連距離變長，銅可能不再是最佳媒介。因此，纖維正逐漸滲透到擴大規模化。 

「如果要放在架子裡，你大概會用銅，」Chandrasekar 解釋。「如果是相鄰的架子，你就在邊緣，但假設你堅持用銅。如果你要進入相鄰貨架以外的地方，就得選光學瞄準鏡。」   
......
如先前定義的擴展，包含三個要素：單機架、銅線與記憶體語意。前兩者現正逐漸被淘汰，剩下的定義因素是記憶語意的使用。  

Synopsys 介面知識產權產品管理總監 Priyank Shukla 說：「軟體人員定義擴展為一個作業系統領域，只有一個記憶體。」「所以，如果你正在執行一個程序，處理器可以寫入一個記憶體位置，不管那個記憶體在哪裡。」 
“Software guys define scale-up as one operating system domain where they have one memory,” said Priyank Shukla, director of product management, interface IP at Synopsys. “So, if you’re running a process, the processor can write to one memory location, regardless of where that memory is.” 

典型的放大與擴展實作會最小化跳數。Chandrasekar 表示：「在擴展領域內，每顆 GPU 都只需跳一跳就能連接其他 GPU。」「如果你說的是鱗片，那就像兩跳而已。」 
Typical implementations of scale-up and scale-out minimize the number of hops. “Within the scale-up domain, every GPU is just one hop away from every other GPU,” said Chandrasekar. “If you’re talking scale-out, it’s like two hops.” 

一跳的放大預期由新的 UALink 標準強制執行。Shukla 解釋：「UALink 的擴展架構旨在維持單跳加速器之間的連接性。」「即使擴展領域已超越單一機架，加速器間的通訊仍設計僅能通過單一 UALink 交換器。因此，跨機架連接加速器本身並不一定需要交換器對交換器的拓撲，否則會增加跳躍。單一交換器可在機架架構的不同位置設置，例如機架頂端（ToR）或機架中置（MoR）部署，但關鍵在於加速器流量仍僅在端點間經過單一交換器。」 

一旦擴展域擴展到機架之外，相同的延遲與跳數限制會將注意力從互連媒介轉移到連結加速器、交換器與伺服器的更廣泛網路拓撲。
Once scale-up domains extend beyond the rack, the same latency and hop-count constraints shift attention from interconnect media to the broader network topology that links accelerators, switches, and servers. 
......
兩者的主要差異在於從一台伺服器到另一台所需的跳數。用葉片和書脊，就是一體。環面則取決於位置。上方路徑顯示有四個跳躍。 

Chandrasekar 指出：「如果你想從一端的 GPU 跳到另一端的 GPU，過程中有很多跳躍。」光纖可實現足夠長的路徑以提升功率與效能。但每一跳都會帶來一些效率的低落，因為這類網路的典型建構方式是封包交換。封包的標頭中包含必須在每個交換器或路由器檢查的雜訊。 

光學技術不懂封包。因此，上述四跳路徑在每一跳都要求將光訊號轉換為電訊號。進入電氣領域後，可以確定下一跳，但在訊號進行下一跳之前，必須先轉換回光學。 

這些在每個節點反覆轉換會降低延遲並消耗相當多的能量。有沒有更好的光網路建構方式？ 
......
新的是資料中心因封包路由而在光與電領域間反覆轉換的挑戰。Aguilar解釋：「資料的移動方式是選擇一個粗壯的無限頻寬光纖訊號，放入電氣開關，將光訊號轉換成電訊號，讀取封包，然後路由到另一顆顯示卡。」「那個光電光迴路消耗大量電力，增加延遲，並推高資料中心的成本。大約15年前，Google 開始研究這個領域，約10年前，他們用基於微機電系統（MEMS）的光學電路開關實現了這個目標。」 

公司在每台路由器上只使用可調整的MEMS鏡像。這些鏡子會將來自源光纖的雷射光反射到該路徑的目的地光纖上。這些系統會在每個節點設置，提供從來源到目的地的清晰路徑，無需轉換。這種方法稱為光電路交換（OCS）。 
......
Google 的實作

Google 發現 OCS 很有幫助。「過去八年來，我們一直深度整合 OCS 與波分多工（WDM）到木星（他們的網路）中，」作者、Google 人工智慧與基礎建設資深副總裁兼首席技術專家 Amin Vahdat 在 2022 年的一篇論文中指出。「OCS 與我們的軟體定義網路（SDN）架構結合，帶來了新功能：支援異質技術的增量網路建置;更高的效能與更低的延遲、成本與功耗;即時應用優先權與通訊模式;以及零停機升級。Jupiter 在將流量完成率降低 10% 的同時，吞吐量提升 30%，耗電量減少 40%，成本降低 30%，停機時間比最知名的替代方案少 50×。」

省電反映了多項改變。「你要省去一半的收發機，省去所需的液冷，還有開關本身的ASIC/電子元件，然後用光學解決方案取代，」Aguilar說。 

在 OCS 中，當大量資料必須在兩台伺服器間流動時，背景網路會先設定整個路由的鏡像，然後流程可以繼續進行，無需轉換或路由決策。但關鍵在於，這些資料都來自同一個地方，也都送到同一個地方。沒有任何資料可以分支並傳送到其他節點。這也讓這個優化是針對特定工作負載而設計的。 

若採用此方法針對短時間且頻繁的資料突發，將花費更多時間在建立與拆除路由上，而非傳送資料。以道路的比喻來說，如果有比整條路線還長的車隊，從洛杉磯到波士頓保留整條路可能比較合理。在這種情況下，道路被佔用時沒有人能使用，但沒有任何部分是閒置的。這類似於需要 OCS 的長資料流。 

「光學電路切換對於『大象流』來說很合理，這是我聽過別人用的術語，」阿吉拉爾說。「這比這些『老鼠流』的爆發好多了。這比較適合 AI 和大型語言模型的學習與推論。」 

由於OCS依賴於在有效載荷傳輸開始前預留端到端光學路徑，其效能也取決於配置這些路徑的控制平面。

新的訊號系統

背景網路會在流程建立時配置鏡像。類似於訊號系統7，這是一個與光網路並行運行的慢速乙太網路控制網路。「你們有一個低頻寬的乙太網路，可以重新配置交換器和資料路由，」Aguilar 說。 

重新配置網路不會花太久時間，但確實需要時間，這也是為什麼這種方式只適用於長時間流量的原因。即便如此，網路配置並不是限制新設定能持續多久的關鍵。「瓶頸是收發器鎖，」阿吉拉爾說。 

用兩個網路取代一個網路看起來可能更複雜，但控制網路其實並不複雜。「你仍然有乙太網路連接機架與機架，將管線導向正確位置，但這是更簡單、更優雅的解決方案，」他說。而且這也不會顯著增加資本成本。「乙太網路交換器很便宜。乙太網路交換器只是一個簡單的低頻寬指令中心。」 

封包與電路

混合 上圖1中的環面網路採用點對點連接，電路交換有利於多跳連接。但葉片/主幹架構不同：它包含交換器和路由器。這種架構也能從OCS中受益嗎？ 

在環面範例中，流是端到端的。這也可以用葉片/書脊組合，雖然跳躍次數少，省電效果也比較差。有些公司正在檢視，例如葉軸網路的頂層是否可以是 OCS，讓來源和目的路由器在輸入端接收多個封包，然後將封包打包傳送到目的路由器，在那裡封包被擷取後，最後以電氣方式傳送到最終節點。 

「OCS 光學終端會接到一個開關，之後就是電氣化的，」Synopsys 的 Shukla 說。 
 
只要流量足夠穩定，且多個來自來源端的封包連接到最終路由器，那麼在兩個交換器之間開啟光路可能是合理的。如圖2所示，這看似簡單，但如果路由器間的路徑複雜且經過多個節點，這樣的電路可能是合理的。 

Google 的 OCS 已經成定局，事實上，他們正從環面網路轉向另一種稱為蜻蜓的配置。其他公司尚未部署此類網路，無論是環面或其他樹狀方案，但坊間傳聞不同公司正考慮用於不同網路的 OCS。
Google’s OCS is a done deal, and in fact, they’re moving from a torus network to yet another configuration called a dragonfly. Other companies have yet to deploy such a network, whether torus or some other tree-style option, but word on the street is that OCS is being considered by different companies for different networks.  

「人們看到這個問題時會說，『我們能否在葉片和脊樑結構中利用這項技術，用 OCS 取代第二層，同時保留第一層的雲端封包交換？』」Chandrasekar 說。 
“People are looking at that saying, ‘Can we use that technology in leaf and spine structures to replace the second layer with an OCS while keeping the first layer cloud packet switching?’” said Chandrasekar. 
......
光學進一步
擴張 這兩項發展都涉及光學在資料中心的參與度提升。隨著擴展，現在它會與銅線連接最長的連接，使整個放大連接組合成為銅線與光纖的混合。 

光學標準會有幫助。「OCP正試圖制定標準，讓每個人都能在這個生態系統中遊玩，」Aguilar說。「Google 已經開發了很多專有功能，必須標準化才能被採用，否則它就無法正常運作。」 

 如果這項計畫成功，會不會因為需求突然激增而讓光學供應商感到壓力？根據計畫中的生產規模和產業合併，Aguilar 並不這麼認為。「根據我們的預測，未來五年我們都還算可以，」他說。「我們的代工廠合作夥伴因預期成長已開始擴展，而 Nvidia 則宣布對 Lumentum 投資 20 億美元，並為 OCS 投資 20 億美元 Coherent。」 

同時，OCS提供了一種方法，讓光纖在兩個目的地間的長距離流量中更有效率，並為資料中心提供了一種全新的光連接配置方式。「當你嘗試做這些對記憶體延遲敏感的操作時，你會想減少跳數，純粹在光學領域確實有幫助，」Aguilar 指出。 

此外，新的聯盟也在形成。例如，Lightmatter 最近加入了 Nvidia 的 NVLink 生態系統。但工作還在。 "

https://semiengineering.com/coppers-grip-on-ai-scaling-is-starting-to-slip/
