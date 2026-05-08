---
post_id: "1480831710068119"
title: "Gavin Baker 與 Dwarkesh Patel 的 AI 硬體是否該賣中國的辯論"
page_title: ""
requested_url: "https://www.facebook.com/intleconobserve"
final_url: "https://www.facebook.com/intleconobserve"
post_url: "https://www.facebook.com/intleconobserve/posts/pfbid0yXGYK7smW7HNKuoF2hnrgU5iX2EwNdeC4AWBEdnYtVi3Ko7dzAj78tAUP4N5Fxxel"
creation_time_utc: "2026-04-17T00:13:05+00:00"
fetched_at_utc: "2026-05-08T22:50:27.786451+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent.ftpe8-3.fna.fbcdn.net/v/t39.30808-6/673949387_1480831350068155_7777776408693189570_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=111&ccb=1-7&_nc_sid=13d280&_nc_ohc=jaSjuzZASVAQ7kNvwE--R1y&_nc_oc=AdoTDaKCvy5SVCuVXyr4N534q1Fmn6oJcJX1n6xWjSZ5VeLdp2YXtWBcrFhx7pt-Fl4&_nc_zt=23&_nc_ht=scontent.ftpe8-3.fna&_nc_gid=GqgnzRkGNPy1bzKsk4H1Zg&_nc_ss=78100&oh=00_Af6urDuYOZxoD8BqKG83Hu5qC2AYOH7y0r1ZkKRsCvEr6Q&oe=6A0434ED"
feedback_id: "ZmVlZGJhY2s6MTQ4MDgzMTcxMDA2ODExOQ=="
page_canonical_url: ""
---

# Gavin Baker 與 Dwarkesh Patel 的 AI 硬體是否該賣中國的辯論

原文連結: https://www.facebook.com/intleconobserve/posts/pfbid0yXGYK7smW7HNKuoF2hnrgU5iX2EwNdeC4AWBEdnYtVi3Ko7dzAj78tAUP4N5Fxxel

![Gavin Baker 與 Dwarkesh Patel 的 AI 硬體是否該賣中國的辯論](https://scontent.ftpe8-3.fna.fbcdn.net/v/t39.30808-6/673949387_1480831350068155_7777776408693189570_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=111&ccb=1-7&_nc_sid=13d280&_nc_ohc=jaSjuzZASVAQ7kNvwE--R1y&_nc_oc=AdoTDaKCvy5SVCuVXyr4N534q1Fmn6oJcJX1n6xWjSZ5VeLdp2YXtWBcrFhx7pt-Fl4&_nc_zt=23&_nc_ht=scontent.ftpe8-3.fna&_nc_gid=GqgnzRkGNPy1bzKsk4H1Zg&_nc_ss=78100&oh=00_Af6urDuYOZxoD8BqKG83Hu5qC2AYOH7y0r1ZkKRsCvEr6Q&oe=6A0434ED)
Gavin Baker 與 Dwarkesh Patel 的 AI 硬體是否該賣中國的辯論

Dwarkesh Patel 近日與 Jensen Huang 進行了一場關於對中國出口管制的對話，其中 Patel 主張美國實驗室可以輕鬆地在不同加速器之間移植模型，因此賣晶片給中國不會產生鎖定效應。Jensen 則反駁，認為運算生態系統具有高度黏性，一旦中國建立起自己的技術棧，美國將失去對全球 AI 基礎設施的影響力。

Gavin Baker 隨後在社群平台上發文回應這場辯論，認為 Patel 的論點建立在一個正在過時的前提之上，並從技術架構和經濟邏輯兩個層面進行了系統性反駁。

#可攜性正在衰退：架構分歧是關鍵
Baker 指出，Patel 所說的「美國實驗室經常在不同加速器之間移植模型」在過去確實成立，但隨著系統層級架構的分歧加劇，真正的可攜性正在流失。

他舉出具體例子：Mi300 和 Mi325 的 scale-up domain 大小與 Hopper 大致相當，但 Blackwell 的 scale-up domain 已經是 Mi355 的九倍。這種差距意味著不同硬體之間的效能落差將持續擴大。

更根本的問題在於拓撲結構的差異。Nvidia 採用 switched scale-up 拓撲，Google 採用 torus 拓撲，兩者的資料傳輸模式截然不同。

當模型被針對特定拓撲進行平行化處理後，移植到另一套系統上的效率損失是結構性的，而非僅僅是調參就能解決的問題。Baker 也提到，越來越多前沿模型正在針對特定硬體進行推論端的共同設計，例如 GB300 機架上的模型，以及 Cerebras 上運行的 Codex。

#從訓練到推論：經濟邏輯的根本轉變
Baker 認為，驅動可攜性衰退的不僅是技術因素，更是經濟邏輯的轉變。過去訓練成本是實驗室的主要開支，電力供應也相對充裕，實驗室的優化目標是降低資本支出。在那個階段，模型可攜性是對供應商創造議價槓桿的有效手段。

但現在推論成本已經遠超訓練成本。尤其是強化學習使得推論實質上成為訓練的一部分。實驗室的優化目標已轉向「每瓦每美元的 token 產出」。

在這個框架下，共同設計的收益遠大於維持可攜性的收益，個別模型在不同系統之間的轉換成本也隨之上升。Baker 認為這正是 Anthropic 與 Nvidia 走到一起的原因：Anthropic 需要 Blackwell 和 Rubin 架構來經濟地推論至少部分模型，而 Mythos 的發布時程可能就與 Rubin 推論用途的供貨時間吻合。

#Anthropic是例外不是常態
Baker 特別點出，Patel 以 Anthropic 跨平台運作的能力作為可攜性的論據，但 Anthropic 恰恰是例外而非常態。Anthropic 作為幾乎所有雲端平台最重要的客戶，擁有跨越模型、晶片和網路全棧操作的條件。

據稱 Anthropic 與 Google 之間有默契，允許 Anthropic 每年招募所需的 TPU 工程師，以確保他們能持續充分利用 TPU 的效能。這種待遇是市場上其他使用者無法複製的。

#中美架構分岔的國安意涵
Baker 最後將討論拉到國家安全層面。他指出，美國和中國的 AI 硬體正在不同的「演化壓力」下發展：美國面臨電力短缺，因此 Nvidia 優化的方向是功耗效率，盡可能延長銅纜互連的使用；中國則電力相對充裕，華為的 Cloudmatrix 384 和 Atlas SuperPod 已經採用光學 scale-up domain，規模遠超 Nvidia 目前的方案，代價是功耗大幅提高。

這套華為系統的網路原語與 Nvidia 系統截然不同，在 Nvidia 上運行良好的模型無法在華為系統上高效運行，反之亦然。Baker 警告，如果中國生態系統獲得動能，中國模型可能不再能在美國硬體上高效運行。

而當中國模型仍然在美國硬體上跑得最好時，美國實際上保有了一定程度的槓桿和控制力。一旦中國建立起完全自主的替代生態系統，這種槓桿就會消失。

Baker 因此認為，這種架構分岔反而強化了向中國出售上一代 GPU 的國安論據。讓中國模型繼續依賴美國硬體棧，比把中國完全推向自主替代方案更符合美國利益。
