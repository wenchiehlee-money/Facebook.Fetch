---
post_id: "122177510498936895"
title: "AI 時代正把「最浪費NAND Flash容量的兩件事」同時推到台前：第一是把更多 NAND 拿去換耐寫（pSLC 化）；第二是把更多資料留在更靠近 GPU 的儲存層（KV cache / context）以支撐超長上下文與高吞吐推理。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61578106860333"
final_url: "https://www.facebook.com/profile.php?id=61578106860333"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0hpoRHD6VUEBib8qU8cik9YJjmrPYQ4EXE55yPp7ryJcoLYgmCmEqhAc2vRnmiT3Tl&id=61578106860333"
creation_time_utc: "2026-01-09T21:38:17+00:00"
fetched_at_utc: "2026-06-08T07:33:22.963947+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0hpoRHD6VUEBib8qU8cik9YJjmrPYQ4EXE55yPp7ryJcoLYgmCmEqhAc2vRnmiT3Tl&id=61578106860333"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTIyMTc3NTEwNDk4OTM2ODk1"
page_canonical_url: ""
---

# AI 時代正把「最浪費NAND Flash容量的兩件事」同時推到台前：第一是把更多 NAND 拿去換耐寫（pSLC 化）；第二是把更多資料留在更靠近 GPU 的儲存層（KV cache / context）以支撐超長上下文與高吞吐推理。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0hpoRHD6VUEBib8qU8cik9YJjmrPYQ4EXE55yPp7ryJcoLYgmCmEqhAc2vRnmiT3Tl&id=61578106860333
AI 時代正把「最浪費NAND Flash容量的兩件事」同時推到台前：第一是把更多 NAND 拿去換耐寫（pSLC 化）；第二是把更多資料留在更靠近 GPU 的儲存層（KV cache / context）以支撐超長上下文與高吞吐推理。

這兩件事疊加，會讓 NAND 的「消耗量」跟「看起來的容量需求」完全不是同一件事。

先講 KV cache。長上下文推理要有效率，不可能每次都把歷史重新算一遍，於是 KV cache 變成推理系統的必需品。NVIDIA 在 CES 2026 直接把這件事制度化：當 context window 變大，KV cache 的容量需求會跟著等比例上升，為了讓推理能擴展、降低重算成本與卡在 GPU 記憶體天花板的問題，他們推的是把 inference context / KV cache 延伸到 NVMe SSD 的平台化方案。 ￼

你可以把它理解成一個訊號：過去「推理吃 DRAM/HBM」，未來會變成「推理同時吃 DRAM/HBM + NVMe SSD」，而 SSD 背後就是 NAND。

如果這些 NVMe 層承擔的是更偏向「高寫入頻率、低延遲取用、需要更高耐寫」的工作負載（例如熱資料快取、上下文交換、持久化的 KV cache pool、或各種推理中介資料），系統端就會自然往更高耐寫規格靠攏。耐寫要上去，業界常見的做法之一就是讓部分 TLC 以 pSLC 模式運作，直接把位元密度砍到三分之一，換取更高 P/E cycle 與更穩的寫入表現。 ￼

當 TLC 被當成 pSLC 使用，本質上是把「每 cell 3 bit」硬生生降成「每 cell 1 bit」，用容量去換寫入壽命與效能。換句話說，同一顆 NAND 顆粒如果改跑 pSLC，可用容量就會掉到原本的三分之一；相對地，耐寫度通常能拉高到原本 TLC 的 10 倍以上，甚至更高（不同廠商與製程會有差異）。 

所以合理推出「NAND 顆粒消耗量三倍」，可以從兩個層次的乘法得知：

第一層：同樣可用容量，pSLC 需要 3 倍 raw NAND。這是位元密度的硬規則。第二層：同樣的 AI 服務規模，為了長上下文與高吞吐，把更多 context 從 GPU 記憶體外溢到 NVMe 層，等於把原本不需要落地的資料，變成要在 SSD 上「可管理、可調度、可復用」。 ￼

這就是為什麼我會說：未來 NAND 需求的增長，不只來自「AI 伺服器多了多少台」，而是來自「AI 推理的資料形態改變了」。它不是單純多裝幾顆 SSD，而是 SSD 正在被拉進推理主戰場，吃掉過去由記憶體或重新計算吸收掉的那一段需求。

而在我們拜訪前三大家Flash製造商，你會發現供給端的限制，會把這個結構性需求放大成價格彈性。

近期市場已經在反映「伺服器應用優先」帶來的價格推升。TrendForce 1Q26 的預期：NAND Flash 價格上漲 33%–38% QoQ，是供需正在收緊的短線訊號。另一方面，IDC 也提到 2026 年 NAND 供給成長可能低於歷史常態（約 17% YoY 的量級）。供給增速放慢的背景下，如果需求不是線性成長，而是「有效容量被打折」再疊加「推理資料外溢到 SSD」，價格很容易出現非線性上漲。

把這些拼起來，未來 NAND 的價格上漲潛力，會來自三個更「可被驗證」的驅動，而不是空泛的 AI 題材：

第一，企業級 SSD 的配置量上升是確定趨勢，但更重要的是 SSD 的角色從資料倉庫轉向推理記憶體的延伸層，等於把需求從「容量導向」拉向「效能與耐寫導向」，這會提高每 TB 的 NAND 含量與規格溢價。 ￼

第二，pSLC 化或更高耐寫設計一旦變成推理基礎設施的一部分，raw NAND 的消耗係數就會上升，市場看到的不是「多買一點 SSD」，而是「同樣可用容量要吃更多顆粒」。 ￼

第三，供給端擴產並不會像大家想的那麼快，尤其當記憶體廠把資源往更高毛利、更確定的伺服器應用集中時，其他應用只能用價格去排隊，價格彈性自然放大。 ￼

AI 不只是把 NAND 需求「變大」，它更可能把 NAND 需求「變貴」。在可能預見的未來，可能會跟現在的DRAM一樣變成電子黃金。

因為當 NAND 被用來承擔推理的上下文與快取，它不再是低成本容量商品，而是推理吞吐與能耗效率的一部分；而當 TLC 被迫以 pSLC 的方式去換耐寫，市場看到的將不是容量曲線，而是顆粒曲線。只要推理的長上下文、持久化 KV cache、以及 NVMe 進入推理架構這件事繼續往前走，NAND 的供需就不會回到過去那種「一擴產就崩」的簡單循環，價格的上行空間自然會被重新定價。 ￼
