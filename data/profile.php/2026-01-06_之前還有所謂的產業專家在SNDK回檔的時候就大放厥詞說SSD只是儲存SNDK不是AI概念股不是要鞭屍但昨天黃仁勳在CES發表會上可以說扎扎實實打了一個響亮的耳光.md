---
post_id: "122176727930936895"
title: "之前還有所謂的產業專家在SNDK回檔的時候，就大放厥詞說SSD只是儲存，SNDK不是AI概念股，不是要鞭屍，但昨天黃仁勳在CES發表會上可以說扎扎實實打了一個響亮的耳光，除了不小心秀出群聯的Logo，其實給了一套記憶體完整的新成長路線："
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61578106860333"
final_url: "https://www.facebook.com/profile.php?id=61578106860333"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02yMqvbXwLE9B86Uzux7hJRH7wjQKdejqb6qY4HWi3KeGJU7acUYTzmjtWrNxKb9pl&id=61578106860333"
creation_time_utc: "2026-01-06T18:27:51+00:00"
fetched_at_utc: "2026-06-08T07:33:22.963947+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02yMqvbXwLE9B86Uzux7hJRH7wjQKdejqb6qY4HWi3KeGJU7acUYTzmjtWrNxKb9pl&id=61578106860333"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTIyMTc2NzI3OTMwOTM2ODk1"
page_canonical_url: ""
---

# 之前還有所謂的產業專家在SNDK回檔的時候，就大放厥詞說SSD只是儲存，SNDK不是AI概念股，不是要鞭屍，但昨天黃仁勳在CES發表會上可以說扎扎實實打了一個響亮的耳光，除了不小心秀出群聯的Logo，其實給了一套記憶體完整的新成長路線：

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02yMqvbXwLE9B86Uzux7hJRH7wjQKdejqb6qY4HWi3KeGJU7acUYTzmjtWrNxKb9pl&id=61578106860333
之前還有所謂的產業專家在SNDK回檔的時候，就大放厥詞說SSD只是儲存，SNDK不是AI概念股，不是要鞭屍，但昨天黃仁勳在CES發表會上可以說扎扎實實打了一個響亮的耳光，除了不小心秀出群聯的Logo，其實給了一套記憶體完整的新成長路線：

NVIDIA 這次不是在「優化 KV Cache」，而是在「重定義 AI 時代記憶體的邊界與層級」，這對整個記憶體產業的影響，會是結構性的，而不是單點產品升級。

我分三個層次講清楚「改變是什麼」與「影響到誰」。

一、記憶體階層被正式拉長：從「算力附屬」變成「平台資產」

過去十年，AI 記憶體的邏輯其實很單純：
HBM 是算力效率的核心，DDR 是容量與成本的妥協，SSD 是冷資料與 checkpoint 的倉庫。

KV Cache 雖然重要，但一直被視為「暫存資料」，因此只能往 HBM → DDR → 本機 SSD 這條路 offload，最多只到 server 內部。

Vera Rubin + NVIDIA Inference Context Memory Storage Platform 的意義在於：
NVIDIA 正式把「KV Cache」升級為一種「可被共享、可被調度、可被保護的系統級記憶體資產」。

這個轉變有兩個本質差異：
1. KV Cache 不再綁定單一 GPU / Node。
2. 記憶體第一次以 Pod / Rack / Cluster 為最小調度單位。

這會直接導致一個結果：

記憶體需求不再只看「模型大小」，而是看「上下文生命週期 × 並發代理數 × 重用率」。這是結構性放大，而不是線性成長。

二、對 DRAM / NAND 需求的「質變」影響

1. HBM：角色不變，但「壓力被轉移」

HBM 仍然是推論即時計算的不可取代資源，但 Context Memory Storage Platform 的出現，反而會讓 HBM 的使用效率變高，而不是被取代。

原因很簡單：更多 KV Cache 被移出 HBM，HBM 專注在 active token generation，單位 HBM 對應的 token throughput 提升。

這代表：HBM 的需求彈性下降，但單顆 GPU 的算力變現能力提高，對供應鏈來說，HBM 還是「供不應求」，但成長斜率變得更平滑、更長周期，這對 SK hynix / Micron 反而是好事，因為「暴衝 → 暴跌」的風險下降。

2. DDR：不再是「被擠壓的一層」，而是被重新定位，這次架構調整，最容易被低估的是 DDR 的地位變化。

原本的推論路徑裡，DDR 是：HBM 不夠用時的備胎，latency 與 bandwidth 都尷尬的一層。但現在，KV Cache 被往 Scale-Out Storage Memory 移動後，DDR 重新回到「控制、排程、資料結構管理」的角色，尤其是在 BlueField-4 + Grace IP 這類 DPU/CPU 融合設計中，DDR 的需求成長，會更多來自「DPU / Storage Node」，而不是 GPU Server 本身，容量成長可能不爆炸，但「節點數量」會增加，這是典型的 橫向擴張（Scale-Out）型需求。

3. NAND / SSD：真正的結構性受惠者

這是我認為影響最大的地方。

幾個結構性改變：
1. KV Cache 從「冷資料」變成「準熱資料」。
2. 延遲不再只是 storage 問題，而是 inference KPI。
3. 容量不再只是 cost center，而是 throughput multiplier。

這會帶來什麼結果？SSD 不再只是「多少 TB / 美元」，而是「多少 KV / rack / latency bound」。SSD 的需求會從「容量導向」轉為「效能 × 延遲 × 網路親和性」導向，特別適合大容量、企業級、高耐久度 SSD。

真正的贏家是：能快速交付高密度 SSD + DPU-based storage server 的系統廠，以及 NAND 原廠中，能穩定供應高品質 enterprise SSD 的玩家。

三、NVIDIA 真正的野心：把「記憶體」也變成平台收入

如果只從硬體看，這是一個 storage 架構調整；但從 NVIDIA 的角度看，這其實是三件事同時發生：
1. Inference 效率提升 → GPU ROI 提高。
2. BlueField-4 成為 AI 工廠必選件 → DPU 放量。
3. Storage 架構被 NVIDIA 軟體堆疊鎖定。

透過：
 • NVIDIA DOCA™
 • NVIDIA NIXL
 • NVIDIA Dynamo

NVIDIA 實際上是在告訴市場：未來不是「你有多少記憶體」，而是「你的記憶體是不是 NVIDIA 認證、NVIDIA 優化、NVIDIA 調度」。

這會讓非 hyperscaler 客戶 更依賴 NVIDIA 的完整解決方案，而不是自己拼 storage + network + software。

最後總結一下

Vera Rubin 的 Context Memory Storage Platform，不是讓記憶體「更快」，而是讓記憶體「更值錢」。

它把：
 • KV Cache 從暫存 → 資產
 • SSD 從成本 → 效率
 • DPU 從配角 → 關鍵節點

對整個記憶體產業來說，這代表的不是短期需求爆量，
而是一個更長、可預期、且更不容易被取代的成長曲線。AI 推論時代，記憶體不再只是算力的附屬品，而是平台的一部分。
