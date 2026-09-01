---
post_id: "122193919322771552"
title: "AMD 是做 CPU 和 GPU 的，Broadcom 是做 ASIC 的，Google 的 TPU 一直是 Broadcom 設計的。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61573146584049"
final_url: "https://www.facebook.com/profile.php?id=61573146584049"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid03X5Xfi3rbFhPEsk5CLgoCjmv45Gt7eJe3QK1bhkVtLXN4sJTmbyqA3MiGJYwwMqil&id=61573146584049"
creation_time_utc: "2026-08-17T03:49:28+00:00"
fetched_at_utc: "2026-09-01T04:41:25.294115+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-dfw5-1.xx.fbcdn.net/v/t39.30808-6/775777926_122193919142771552_8285900434683596960_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_ohc=qqsxD4sv15YQ7kNvwG3kA9a&_nc_oc=AdpzuLLJ7-5movZZKrdEMVeuVxnfsEVuLBCSxuKESqnU5V6mvVNv9lRKdwKUoaz_dOA&_nc_zt=23&_nc_ht=scontent-dfw5-1.xx&_nc_gid=iC1nAXkraZ-ooba2VwgWjg&_nc_ss=7e120&oh=00_AQLPT0_JSLCbkEpxkBAeREeLYYgyxwzzyY_5JbqOWFVTXA&oe=6A9C2056"
feedback_id: "ZmVlZGJhY2s6MTIyMTkzOTE5MzIyNzcxNTUy"
page_canonical_url: ""
---

# AMD 是做 CPU 和 GPU 的，Broadcom 是做 ASIC 的，Google 的 TPU 一直是 Broadcom 設計的。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid03X5Xfi3rbFhPEsk5CLgoCjmv45Gt7eJe3QK1bhkVtLXN4sJTmbyqA3MiGJYwwMqil&id=61573146584049

![AMD 是做 CPU 和 GPU 的，Broadcom 是做 ASIC 的，Google 的 TPU 一直是 Broadcom 設計的。](https://scontent-dfw5-1.xx.fbcdn.net/v/t39.30808-6/775777926_122193919142771552_8285900434683596960_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_ohc=qqsxD4sv15YQ7kNvwG3kA9a&_nc_oc=AdpzuLLJ7-5movZZKrdEMVeuVxnfsEVuLBCSxuKESqnU5V6mvVNv9lRKdwKUoaz_dOA&_nc_zt=23&_nc_ht=scontent-dfw5-1.xx&_nc_gid=iC1nAXkraZ-ooba2VwgWjg&_nc_ss=7e120&oh=00_AQLPT0_JSLCbkEpxkBAeREeLYYgyxwzzyY_5JbqOWFVTXA&oe=6A9C2056)
AMD 是做 CPU 和 GPU 的，Broadcom 是做 ASIC 的，Google 的 TPU 一直是 Broadcom 設計的。
​
但根據SemiAnalysis最新報導，Google 正在與 AMD 洽談，讓 AMD 參與未來 TPU（v10）的設計。
​
這聽起來像是找一個廚師來幫忙修水管，但如果你理解 Google 到底在解決什麼問題，你就會發現這個選擇非常合理。
​
市場反應十分即時：賣博通，買入AMD。
​
AMD也有做ASIC的嗎？這對博通（Broadcom）是壞消息嗎？
​
▋ Google不想只有一個供應商
​
今年三月，Google 和 Broadcom 剛簽了一份為期五年、覆蓋四代 TPU（v8 到 v11）的合作協議，營收能見度一直拉到 2031 年。
​
而供應鏈多元化這件事，早就在發生了。
​
聯發科已經在 v9 的部分變體上參與設計，主要負責推理和 I/O 封裝。Google 跟 Marvell 也在談推理和內存處理芯片。
​
Broadcom 的 CEO Hock Tan 在六月的財報電話會上自己說了：Google 未來會使用多個供應商。
​
所以 AMD 如果真的加入 v10，它填補的是一個新的位置，而不是搶走 Broadcom 的位置。
​
▋ 為什麼是 AMD？
​
隨著 AI 逐步邁向具備「推理與思考」能力的階段，強化學習（RL） 成為了訓練的核心。
​
在傳統的 AI 訓練架構中， CPU與GPU/TPU是分開安置在主機板上的。
​
當 RL 進行高頻率、密集的「思考與嘗試」反饋循環時，數據必須不斷在 CPU 與加速器之間來回傳輸。
​
這種物理距離產生的Latency與能耗，成為了拖累訓練效率的致命傷。
​
因此，Google想在下一代 TPU 裡，把 CPU 核心直接封裝在加速器旁邊。是物理意義上的「住隔壁」，甚至「疊在一起」。
​
而 AMD 已經把這個問題解決過了。
​
▋ MI300A：一個已經被驗證的答案
​
AMD 的 MI300A 數據中心芯片，就是這個架構的成品。
​
它把 Zen CPU 核心和 GPU 計算晶片直接封裝在同一個基板上，共享同一池 HBM 高速內存，中間用台積電的 SoIC 混合鍵合(Hybrid Bonding)技術連接。
​
台積電用銅對銅的微觀級別直接鍵合，取代了傳統的焊球連接，讓芯片層與層之間的距離幾乎為零。
​
這是目前最先進的封裝技術之一，而 AMD 已經在量產中用過了。
​
Google 要的，就是這個「CPU 住在加速器隔壁」的工程能力。AMD 是極少數已經在量產級別證明過這件事的公司。
​
▋ 市場搞混了兩件事
​
SemiAnalysis 在同一時期下調了 Broadcom 在 2026 下半年到 2027 年的 TPU 出貨量預期。
​
市場立刻把這件事跟 AMD 的傳聞綁在一起，解讀成「Google 把 Broadcom 的訂單分給 AMD 了」。
​
但出貨量下調的原因是 CoWoS 先進封裝的產能瓶頸，以及產能被分配給了其他客戶（Meta 的 MTIA、OpenAI 的定制芯片等），跟 AMD 沒有關係。
​
▋ 餅在變大
​
回到最核心的問題：這對 Broadcom 是壞消息嗎？
​
如果你的思維框架是「Google 的 TPU 預算是一塊固定大小的餅，多一個供應商就少分一份」，那確實是壞消息。
​
但現實是，這塊餅正在以每年翻倍的速度膨脹。Google 的 AI 資本開支在持續上調，TPU 的部署規模在指數級增長。
​
在一個每年增長 50% 到 100% 的市場裡，加入一個新供應商，不代表原有供應商的絕對金額會下降。
​
而AMD 能不能真的拿下這個合作，目前還是傳聞。
​
但 Google，甚至其他玩家，早晚會往混合鍵合（Hybrid Bonding）和 3D 封裝的方向走，幾乎是確定的。
​
因為 AI 訓練的物理需求在那裡。當模型越來越大、訓練循環越來越密集，芯片之間的距離就必須越來越短。短到最後，它們必須疊在一起。
​
我在幾個星期前，曾經詳細分析過3D封裝和混合鍵合(Hybrid Bonding)的整條產業鏈，以及裡面的玩家，裡面的玩家，從 BESI 到 ASMPT，每一個環節的競爭格局、技術壁壘和投資邏輯都講清楚了。
​
這些不是你在傳統媒體能看到的分析，但如果你讀過了這篇分析，你就會清楚了解Google找上AMD這條傳聞的意義。讀完再看這則新聞，你會看到完全不同的東西。
​
誠邀你閱讀全文，鏈結在下方。
​
- KP
