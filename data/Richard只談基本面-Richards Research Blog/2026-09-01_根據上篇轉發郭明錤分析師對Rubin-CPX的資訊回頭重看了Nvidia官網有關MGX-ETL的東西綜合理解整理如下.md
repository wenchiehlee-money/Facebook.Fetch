---
post_id: "1599567628526604"
title: "根據上篇轉發郭明錤分析師對Rubin CPX的資訊，回頭重看了Nvidia官網有關MGX ETL的東西，綜合理解/整理如下:"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02ECJL8r8vrTAnDUbEAgauTwLdt7vmL8s8cfevB2X43dYgQycwhKTSN9MqpQ9wVarTl&id=100054201473657"
creation_time_utc: "2026-09-01T10:38:20+00:00"
fetched_at_utc: "2026-09-02T05:41:12.441822+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02ECJL8r8vrTAnDUbEAgauTwLdt7vmL8s8cfevB2X43dYgQycwhKTSN9MqpQ9wVarTl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU5OTU2NzYyODUyNjYwNA=="
page_canonical_url: ""
---

# 根據上篇轉發郭明錤分析師對Rubin CPX的資訊，回頭重看了Nvidia官網有關MGX ETL的東西，綜合理解/整理如下:

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02ECJL8r8vrTAnDUbEAgauTwLdt7vmL8s8cfevB2X43dYgQycwhKTSN9MqpQ9wVarTl&id=100054201473657
根據上篇轉發郭明錤分析師對Rubin CPX的資訊，回頭重看了Nvidia官網有關MGX ETL的東西，綜合理解/整理如下:

1. Nvidia有兩種Rack、三種跨trays的互聯骨幹(Spine)，組合成六套機架級系統Rack Level System (上次發布5套加上這次共6套)

Rack: (1)MGX NVL、(2)MGX ETL

Spine: (1)NVLink spine、(2)Direct Chip-to-Chip spine(只用於LPX)、(3)Spectrum-X Ethernet spine

Rack System:
(1)Vera Rubin NVL72 + NVLink spine
(2)Groq LPX + Direct Chip-to-Chip spine
(3)Vera CPU + Spectrum-X Ethernet spine
(4)這次重新加入的: Rubin CPX + Spectrum-X Ethernet spine
(5)BlueField-4 STX Storage + Spectrum-X Ethernet spine
(6)Spectrum-6 SPX

2. 重新啟動研發的Rubin CPX Rack System

(1)晶片: Rubin CPX/168GB HBM4

(2)模組(想像成箱子;模組箱)

1個模組箱有8個compute tray，一個compute tray上有8顆Rubin CPX晶片，總共8x8=64顆CPX晶片，外加一個Switch Tray，共9個tray

Scale Up: Compute Tray上的8顆Rubin CPX晶片靠NVLink Scale Up，猜測Compute borad上面有幾顆NVLink Switch晶片，類似HGX架構中UBB上面有4顆NVLink Switch晶片聯結8顆GPU，每顆Rubin CPX NVLink頻寬1~1.5TB/s，不到Rubin的一半

箱內Scale Out: 8個Compute Tray之間，靠Switch Tray中的Spectrum-6 Ethernet晶片網路聯結，全銅線

箱外Scale Out: 模組箱之間的互聯，靠Switch Tray中Spectrum-6 Ethernet透過OSFP光纖進行

(3)Rubin CPX Rack: 可以1~4個模組箱放在一個MGX ETL Rack上，以四個模組箱放一櫃為例:

(Compute Tray x 8 + Switch Tray x 1) x 4 = Compute Tray x 32 + Switch Tray x 4，只是這四個Switch Tray集中放在機櫃中間，不是跟隨自屬的模組箱放一起

1箱=8 x 8 = 64顆Rubin CPX
2箱=8 x 8 x 2 =128顆Rubin CPX
3箱=8 x 8 x 3 = 192顆Rubin CPX
4箱=8 x 8 x 4 = 256顆Rubin CPX

3. 只有同一個Compute Tray之間的8顆GPU透過Scale Up NVLink互聯，其他都是Ethernet Scale Out

想像一台Switch Tary有銅線和光纖同時連到Spectrum-X Ethernet spine骨幹，Compute Tray銅線連到骨幹

MGX ETL這個機架以前比較被忽略，主角是MGX NVLink，回頭看這個機架包容蠻大的，還可以容納多達256張Rubin GPU（HGX Rubin NVL8 系統）、XPU或更多，256張Rubin或Rubin CPX都可以，只是這裡的Rubin是HGX Rubin NVL8，曾聽機殼廠說過即使GB300 NVL72當道，還是有CSP採購HGX B300，只是外界不知道他是作什麼應用? 或是這樣出租單位較小比較好出租(72 vs 8)，這種需求以後就可以用MGX ETL機架，一櫃可裝256顆GPU (32 x 8)，比NVL72一櫃只有72顆密度高很多

4. 理論上一片Compute Tray需要至少一顆CPU，不知道是那一款? Vera或x86?

5. P/D分解推論的配置

P/D分解推論已經變成生產端大規模推論的標準，根據郭明錤分析師的資訊，Nvidia建議CPX和Rubin的比例為1:1，我想客戶可以根據自己的任務不同而調整，之前看到prefiller和decoder是同一款GPU/XPU的時候，一般說xPyD， x、y可以自定配置

Prefill: Rubin CPX 1~4箱或多櫃
Decode: Vera Rubin NVL72或HGX Rubin

因為MGX ETL機櫃設計時可以裝配HGX GPU或別家XPU，所以一個MGX ETL也可以將HGX Rubin和Rubin CPX裝在同一櫃做P/D分解推論

6. P/D分解和AFD的配置，Rubin, Rubin CPX, Groq LPU40可否一起放在MGX ETL機架內?

主流推論技術中，P/D分解(Prefill Decode Disaggregation)已成標準，在P/D分解的基礎上，在建構和Attention-FFN Disaggregation (AFD)，是另一件發展中的趨勢，先做P/D解碼再做AFD，但也可以只做P/D解碼不做AFD，這兩件事是獨立的

Nvidia發表Groq LPX的時候主要針對的是AFD，或嚴格說，是P/D分解+AFD(重點是AFD)，目前Nvidia加上郭明錤分析師的資訊，變成這樣

P/D分解推論
Prefill: Rubin CPX
Decode: GB/VR NVL72
Prefill-Decode互聯: Ethernet

AFD推論
Prefill: GB/VR NVL72
  -Decode-Attention: GB/VR NVL72
  -Decode-FFN/MoE: Groq LPX
  -Loop
Prefill-Decode互聯: Ethernet
Attention-FFN/MoE互聯: Ethernet

目前以上三個互聯業界標準都是用Scale Out Ethernet，可能是因為配置彈性和可擴展性，不受限Scale Up NVLink的固定8或72顆限制

因為Blackwell、Rubin、Rubin CPX都是一般的AI GPU，而LPX Rack中的LPU是SRAM加速低延遲GPU，適合FFN，既然Rubin CPX比Rubin更適合Prefill的話，未來可不可能有以下的夢幻配置:

一個MGX ETL機架3種種晶片
Prefill: Rubin CPX
Decode-Attention: Rubin HGX
Decode-FFN/MoE: Groq LPU40以後

因為目前LPU30是原Groq設計，必須透過Direct Chip-to-Chip spine骨幹互聯，還不可能，但下一代LPU40，如果改為Nvidia各機架標準的Spectrum-X Ethernet spine骨幹，就可以和Rubin HGX和Rubin CPX一起放在MGX ETL機架上

不放在一個機櫃，就是三種機櫃分別數量放在同一區集群內

7. 順便提到Groq LPX，Nvidia官網說得很清楚，VR NVL72和Groq LPX的搭配有以下三種方式(configuration)

Pairing this new low latency, deterministic execution capability of Groq 3 LPX with Vera Rubin NVL72 racks enables multiple serving configurations, including: 

(1)標準P/D分解，LPX要處理KV cache和SRAM儲存權重
Standard prefill-decode disaggregation: Vera Rubin NVL72 handles prefill and hands off the KV cache once per turn. Groq 3 LPX uses this KV cache, along with weights held in SRAM, to perform the entire decode step.

(2)P/D分解後做AFD，decode時VR NVL72做Attention、LPX做FFN，只有暫時性的中間資料需要在兩個rack間傳輸(請注意無論是P/D分解或AFD各racks之間都是靠Ethernet/NIC)，
Attention-FFN disaggregation: Vera Rubin NVL72 computes attention and holds the KV cache in DRAM, while Groq 3 LPX executes the FFN layers. Only intermediate tokens are sent between racks, once per full-attention layer.

(3)LPX跑一個小草稿模型先+大模型檢驗，大模型在NVL72跑，這方法去年開始漸普及，請注意這個(3)和(1)/(2)是獨立的使用情境，不一定要用
External-drafter speculative decoding: Groq 3 LPX runs a small draft model ahead of the large target model on Vera Rubin NVL72, which verifies and commits tokens and returns rejected positions for the next chunk. Each rack keeps its own model’s KV cache and only draft tokens cross the link.

(1)是用在小模型，前面1~6個點都是講前沿大參數模型，就是(2)P/D分解+AFD，(3)則是獨立應用小草稿模型預測+大模型檢驗技術

8. 談這些要幹什麼? 就是試圖了解Nvidia的產品規劃、產品策略和競爭力變強還是變弱，大家都說ASIC/XPU晶片更能專門、客製化針對inference任務最佳化，Google TPU更在大規模集群網路上有自己的技術，GPU既然是GPGPU通用型加速器，在晶片層級就不可能針對特定模型或應用場景最佳化，看起來，Nvidia不斷嘗試在Rack層級、PoD層級、Cluster層級，希望達成兼具效能和彈性的任務最佳化架構，而通常，效能要最佳化/優化、彈性要通用化，效能(各種效能/performance指標)和彈性是互斥的，Nvidia這樣有朝這方向進步嗎?

Nvidia官網文字--------------------------------------------------------

NVIDIA MGX ETL 機架

雖然 NVIDIA MGX NVL 機架提供大規模的可擴展運算領域，但代理式 AI 工作流程則需要高度專業化的節點，以實現極低延遲推論、CPU 沙盒化，以及加速的 KV 快取上下文記憶體。為支援這些多元需求，Vera Rubin 推出了 MGX ETL 機架架構，這是一種全新可配置的 MGX 機架，採用 Spectrum-X 乙太網路骨幹或直接晶片骨幹設計，並利用與 MGX NVL 機架相同的機架規模生態系統。

MGX ETL 與 MGX NVL 機架擁有相同的外型與物理基礎設施，設計上在相同的機械、電力與冷卻包絡下運作。兩個機架將共用由經驗豐富的 MGX 生態系統打造的關鍵機架組件：機架、底盤、托盤、線芯、液冷歧管、快速斷開器、母線（標準與液冷）、支撐支架、側軌、電動層架、漏水控制盤、托盤把手等。

MGX ETL 將使用預先整合且經過驗證的銅線卡匣，搭配 Spectrum-X 乙太網路主幹或直接晶片對晶片主幹。MGX ETL 將利用 MGX 已建立的生態系統與供應鏈，這些生態系統多年來在大量生產中累積了機架架構的建置經驗。

NVIDIA Spectrum-X 乙太網路主幹

搭載 Spectrum-X 乙太網路脊的 MGX ETL 將成為 Vera CPU 機架與 Vera Rubin POD 中 BlueField-4 STX 儲存機架的基礎。機架高度可配置，且可容納多達 256 張 Rubin GPU（HGX Rubin NVL8 系統）、XPU 或更多。

此設計中，1U MGX ETL 交換托盤（基於 Spectrum-6）位於機架中央。後向端口連接銅軸，32個前置OSFP籠提供光學收發器連接至POD其餘部分。

MGX ETL 採用 Spectrum-X 多平面拓撲，將 200 Gb/s 通道分散至多個交換器，實現機架內節點間的完整全對全連接，同時維持單一網路層級。預先整合的銅製主幹提供韌性且節能的連接性（使 ETL 機架間可單層光學元件連接），並將專為 Spectrum-X 以太網設計的無抖動、隔噪及負載平衡延伸至整個 256 晶片機架。
......"
