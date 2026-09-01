---
post_id: "1589494969533870"
title: "我覺得這兩年來討論Cerebras的正反兩方人士，為何沒有交集? 可能是因為他們兩方都以為Cerebras用SRAM取代HBM和DRAM(昨天木頭姊是在講這個嗎? 沒看全文不知道)"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid031HLNXFzAyzum7e1Sif4beuFDm7KdWDBJUhUCZ9wA82EHAgWM8J2CpQpCFSHdnhhvl&id=100054201473657"
creation_time_utc: "2026-08-20T14:55:55+00:00"
fetched_at_utc: "2026-09-01T04:42:39.947356+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU4OTQ5NDk2OTUzMzg3MA=="
page_canonical_url: ""
---

# 我覺得這兩年來討論Cerebras的正反兩方人士，為何沒有交集? 可能是因為他們兩方都以為Cerebras用SRAM取代HBM和DRAM(昨天木頭姊是在講這個嗎? 沒看全文不知道)

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid031HLNXFzAyzum7e1Sif4beuFDm7KdWDBJUhUCZ9wA82EHAgWM8J2CpQpCFSHdnhhvl&id=100054201473657
我覺得這兩年來討論Cerebras的正反兩方人士，為何沒有交集? 可能是因為他們兩方都以為Cerebras用SRAM取代HBM和DRAM(昨天木頭姊是在講這個嗎? 沒看全文不知道)

Cerebras並沒有只用SRAM，而是同時用了極大量的DRAM和Flash，放在MemoryX

所以看好Cerebras前景的人一直強調wafer level chip和SRAM速度多快，彷彿沒有其他代價、限制，並且以Cerebras已經和幾家大公司合作，並且公司方發布的超越競爭者的速度來作證明，看壞Cerebras的人則一再強調wafer level chip上面的SRAM太貴太小，一整片wafer(大概相當於十幾顆Blackwell計算晶片算力)上面的VRAM只有44GB SRAM，不論是用SRAM或HBM當VRAM，不論是trainning或Inference，即使只是許多人說的只要做prefill/decode分解推理中的decoder，這三者，training、inference、decoding，VRAM都需要常駐儲存模型參數權重weights，44GB的VRAM根本無法運作大模型，如果要把多台wafer-level-chip串聯起來跑，為了符合SRAM當VRAM的容量需求，就會浪費大量idle算力，所以Cerebras SRAM不能跑大模型，何況Agentic AI和KV cache需求爆炸，SRAM存權重和KV cache都大大不夠用

以上兩方論點有點雞同鴨講，我也覺得奇怪Cerebres官方為何不講清楚，因為Cerebras不是只有SRAM，他有一個很大很大的MemoryX記憶體櫃

Cerebras機架旁邊的超大的MemoryX記憶體系統，用的是DRAM、Flash記憶體，和別人一樣，用來儲存龐大的模型參數權重

我覺得正反兩方，都沒有去注意到Ceberas晶片機櫃旁邊的MemroyX(機櫃)，這裡的DRAM和Flash超大超多，並不是SRAM取代DRAM的議題，根本就是用DRAM儲存權重

重點在MemoryX，和大家一樣使用DRAM和Flash

至於Cebebras官方、CEO，當然是清楚的，但不知道他們為何不好好解釋說: 我們可以跑大模型是因為我們用很多DRAM和Flash，放在MemoryX中，儲存大模型權重，和Cerebras wafer level chip和wafer上的SRAM搭配，才能訓練和推論，也許想要保持SRAM"特殊技術"的神祕感? 因為相對wafer chip本身，MemoryX架構沒公布，資訊很少

所以一方包含Nvidia, AMD, TPU, ASIC
是把DRAM做成HBM加速

另一方Cerebras是把SRAM和DRAM分工，用wafer-level-chip/SRAM加速，用MemoryX存權重，但是這種分工方式、極頻繁的資料搬動，在兩個機櫃之間的搬動，為何不會拖慢速度? 如何加速? 可能是Cerebras的know how?

兩方都要用DRAM(或是DRAM產能做出來的HBM)來存模型權重，用HBM/DRAM(和/或)存KV cache，沒有差異

記憶體漲價，照樣漲到Cerebras (所以不懂木頭姊的邏輯但我沒看全文)

很快的將來以後Nvidia, AMD, TPU, ASIC，也會有邏輯、配置上形似的DRAM Rack和Flash Rack(內部技術和能力一定不同)，都發表過了

DRAM Rack就是業界CXL DRAM Rack
Flash Rack就是Nvidia CMX SSD Rack

------------"Cerebras 硬體採用獨特的拆分記憶體架構，因此 LLM 需要比傳統 AI 模型多 1,000 倍的記憶體。我們沒有依賴靠近GPU的少量HBM，而是設計了專用的外部記憶體裝置MemoryX來儲存權重。MemoryX 採用快閃記憶體、DRAM 及自訂軟體堆疊，以極低延遲的方式進行流水線載入與儲存請求。Cerebras CS-3 MemoryX 的 SKU 容量從 12 TB 到 1.2 PB 不等。
............
我們的 1.2PB 超大規模 SKU 專為 GPT-5 及更高平台設計，能訓練擁有 24 兆個參數的模型。它的記憶體容量是 B200 GPU 的 6,000 倍，是 DGX B200 的 700 倍以上，記憶體容量則是完整機架 NVL72 的 80 倍以上。

換句話說，要匹配單一 CS-3 記憶體容量與 MemoryX 1.2PB 的容量，需要 80 個 NVL72 機架。
............
使用 Cerebras 硬體，一台連接 1.2 PB MemoryX 的 CS-3 就能像在 GPU 上載入 1B 參數模型一樣簡單地載入模型。這使得微調100B到10T參數規模模型變得快速且資本支出效率高。"
----‐----‐-------------
"此外，透過 MemoryX 邊車內存，CS-3 主機伺服器中可使用 24 TB、36 TB、120 TB 或 1,200 TB 的 DRAM 內存來儲存參數。"

https://www.cerebras.ai/blog/cerebras-cs-3-vs-nvidia-b200-2024-ai-accelerators-compared

https://www.nextplatform.com/ai/2026/01/15/cerebras-inks-transformative-10-billion-inference-deal-with-openai/4092155
