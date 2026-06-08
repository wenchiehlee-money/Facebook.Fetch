---
post_id: "1516295070187194"
title: "2H26會有許多廠商推出Nvidia CMX平台Flash SSD Rack for G3.5 KV cache level，用SSD降低inference cost，用越多SSD，則Inference同時服務人數越多/GPU重算負載越少，則TCO越低(或者服務品質越好)"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid034fRoJur8JiFRGEAHbsPMRPcbk5FcNUBAqn7X1uDgvzsMhBLfhJhsq3bB6xD6Xnfsl&id=100054201473657"
creation_time_utc: "2026-05-27T15:12:28+00:00"
fetched_at_utc: "2026-06-08T07:33:36.899093+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-sjc6-1.xx.fbcdn.net/v/t39.30808-6/707562881_1516294876853880_5893747560661279159_n.jpg?stp=dst-jpg_p552x414_tt6&_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=2GqOE9QNvRYQ7kNvwFS1RNg&_nc_oc=AdpdDRve4286pO6d3X5KwoGSzjYItHXgQ0AjsTmmH8MsIfbbCtp5-ow0424CuLLMCIo&_nc_zt=23&_nc_ht=scontent-sjc6-1.xx&_nc_gid=hB5kFIRlgwsEAgCj6BqNYg&_nc_ss=7e120&oh=00_Af-LKWu09y80pILK5MsT5OdfB4fPJMpQdGx3y3ZDmlE-dg&oe=6A2C34A0"
feedback_id: "ZmVlZGJhY2s6MTUxNjI5NTA3MDE4NzE5NA=="
page_canonical_url: ""
---

# 2H26會有許多廠商推出Nvidia CMX平台Flash SSD Rack for G3.5 KV cache level，用SSD降低inference cost，用越多SSD，則Inference同時服務人數越多/GPU重算負載越少，則TCO越低(或者服務品質越好)

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid034fRoJur8JiFRGEAHbsPMRPcbk5FcNUBAqn7X1uDgvzsMhBLfhJhsq3bB6xD6Xnfsl&id=100054201473657

![2H26會有許多廠商推出Nvidia CMX平台Flash SSD Rack for G3.5 KV cache level，用SSD降低inference cost，用越多SSD，則Inference同時服務人數越多/GPU重算負載越少，則TCO越低(或者服務品質越好)](https://scontent-sjc6-1.xx.fbcdn.net/v/t39.30808-6/707562881_1516294876853880_5893747560661279159_n.jpg?stp=dst-jpg_p552x414_tt6&_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=2GqOE9QNvRYQ7kNvwFS1RNg&_nc_oc=AdpdDRve4286pO6d3X5KwoGSzjYItHXgQ0AjsTmmH8MsIfbbCtp5-ow0424CuLLMCIo&_nc_zt=23&_nc_ht=scontent-sjc6-1.xx&_nc_gid=hB5kFIRlgwsEAgCj6BqNYg&_nc_ss=7e120&oh=00_Af-LKWu09y80pILK5MsT5OdfB4fPJMpQdGx3y3ZDmlE-dg&oe=6A2C34A0)
2H26會有許多廠商推出Nvidia CMX平台Flash SSD Rack for G3.5 KV cache level，用SSD降低inference cost，用越多SSD，則Inference同時服務人數越多/GPU重算負載越少，則TCO越低(或者服務品質越好)

----------"這些狀態資料會以鍵值（KV）對的形式儲存在快取中。隨著 KV 快取逐漸滿，它會從快速的 HBM 和 DRAM 記憶體溢出到較慢的儲存媒介，這會增加使用者或代理人員所經歷的等待時間。在某些情況下，直接在 GPU 上重新執行預填充工作來重新計算狀態，比等待從較慢的儲存空間拉取 KV 狀態資訊更快。但繳納那種「重新計算稅」顯然不是理想的長期解決方案。

過去幾個月，所有主要的儲存廠商都推出了支援 CMX 架構的策略，CMX 是 Nvidia AI 儲存參考架構 STX 的延伸。BlueField-4 DPU 要到 2026 年下半年才會出貨，因此基於 CMX 和 STX 參考架構的新儲存解決方案尚未上市，儘管許多廠商已有針對 KV 快取問題的解決方法。

MinIO 表示，MemKV 採取全新方法來解決這個問題，沒有技術包袱和緩慢的變通方法。根據 MinIO 技術長 Ugur Tigli 的說法，關鍵在於盡量減少關鍵 AI 推理路徑中的程式碼量，從而最大化回應時間，這也是 MinIO 在其受歡迎的開源 S3 相容物件商店（並將其重新命名為 AI Store）所秉持的理念。

Tigli 告訴 HPCwire：「我們結合過去分散式檔案系統與 S3 儲存的經驗，搭配 AI Stor 與持久儲存，並設計出 MemKV，它本質上就位於那個 G3.5 層。」「這是一個分散式 KV 記憶體，該層所有 GPU 都能存取。」

在 Nvidia 的「G」階層中，G1 指的是直接連接到 GPU 的 HBM，而 G2 則指直接連接到 Nvidia Grace Blackwell 和 Vera Rubin 超級晶片上的 CPU。G3 層是連接 PCIe 的 NVMe 硬碟，位於同一機架內與 Nvidia 超級晶片相鄰，而 G4 則指網路連接儲存。G3.5 指的是一種 CMX 解決方案，技術上是透過 RDMA 和乙太網路連接，但實際以記憶體內速度運行。

MemKV 將直接運行於 OEM 廠商 CMX 儲存設備中的 DPU-4 ARM 核心上。雖然支援 NIXL，但 MemKV 並非依賴 NIXL 來傳輸資料，而是透過 RDMA 實作自己的 I/O 堆疊。MinIO 表示，它能儲存 2 到 16 MB 的區塊大小，這正是 GPU 預期看到的。MemKV 沒有檔案系統或物件儲存，只有透過雙 400 GbE 或 800 GbE 連結進行 RDMA 加速至 JBOF。結果是一套非常快速的系統，能為存放於 PB 級 JBOF 儲存空間的 KV 快取資料提供微秒延遲。

MinIO 表示 MemKV 能大幅降低重新計算稅。使用 AIPerf 基準測試顯示，MemKV 在首次代幣（TTFT）指標上，相較於 GPU 的重新計算狀態提升了 50%。以 128 張 GPU 和 128K 令牌上下文長度大規模運行時，MemKV 將 GPU 利用率從約 50% 提升到 90% 以上。若以一年計，這相當於200萬美元的運算節省

位於 3.5G 層，讓 MemKV 在處理跨多 GPU 的大型 AI 工作負載時具有優勢。3G 解決方案的狀態會綁定到連接到特定 GPU 或 CPU 的 NVMe 硬碟。透過 MemKV 的 3.5G 解決方案，任何 NVMe 硬碟的狀態都能被任何可能需要存取的 GPU 或 CPU 存取。

Tigli 說：「當代理進入企業領域時，這將非常重要，因為代理會溢出大量中間資料，僅靠綁定在 GPU 上是不夠的，」Tigli 說。「他們需要一個全域位址的記憶。」

雖然在生成式與代理式人工智慧的新時代，保持GPU接近其容量運作在經濟上是合理的，但這取決於GPU的實際運作。因為 KV 快取太小而讓 GPU 不斷被重新計算，並不是 AI 工廠中最昂貴硬體的好用法。硬體疫情使得取得部分 NVMe 硬碟變得困難且昂貴，但公司表示，花約 8 萬美元打造一套 1 PB 的 NVMe 系統，透過 MemKV 擴展 KV 快取，仍比花錢買 GPU 更划算。
......
重新計算稅是生產推論中的主要成本驅動因素，而 MemKV 則將其崩潰。」
......
MemKV 現已以預覽模式提供。雖然理論上它可以在任何 ARM 系統上運行，但目前該解決方案仍綁定於 Nvidia BlueField-4 DPU，預計將於 2026 年下半年出貨。
......
Nvidia 對此問題的回應是在 2026 年 1 月初的消費性電子展上推出情境記憶體儲存（CMX）平台。CMX 利用 Nvidia 即將推出的 BlueField-4 資料處理單元（DPU）以及 ConnectX-8 和 -9 SuperNIC，將 KV 快取從連接至其超級晶片的高速 HBM 與 DRAM 記憶體，透過 RDMA 啟用的乙太網路連結，合理地延伸到 Just a-bunch-of-flash（JBOF）NVMe 儲存裝置。CMX 也使用 Nvidia Inference Xfer Library（NIXL）軟體，這是 Nvidia 開發的，旨在加速 AI 推論框架內的點對點通訊，例如其自家的 Dynamo 框架。"

https://www.hpcwire.com/2026/05/26/inside-memkv-minios-3-5g-solution-for-kv-cache-acceleration/
