---
post_id: "1627349215748445"
title: "日經新聞Nekki報導Toshiba打算投資600億日圓將AI資料中心用的HDD產能加倍，目前Toshiba HDD市佔率只有10%，中期目標是提升到30%，不知真假，如果是真......之前WD和Seagate堅持不擴產HDD units，只增加碟片密度(如HAMR)和HDD內碟片數(如12片)來增加容量的作法，被第三名的Toshiba打破"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02ATXxfxaKd44sekyPPP3Sr78pJTetz6GYUMovM2jhiCwUymWoUfhqCmjn3Lbjzu4wl&id=100054201473657"
creation_time_utc: "2026-10-02T14:39:48+00:00"
fetched_at_utc: "2026-10-03T06:22:44.593839+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02ATXxfxaKd44sekyPPP3Sr78pJTetz6GYUMovM2jhiCwUymWoUfhqCmjn3Lbjzu4wl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTYyNzM0OTIxNTc0ODQ0NQ=="
page_canonical_url: ""
---

# 日經新聞Nekki報導Toshiba打算投資600億日圓將AI資料中心用的HDD產能加倍，目前Toshiba HDD市佔率只有10%，中期目標是提升到30%，不知真假，如果是真......之前WD和Seagate堅持不擴產HDD units，只增加碟片密度(如HAMR)和HDD內碟片數(如12片)來增加容量的作法，被第三名的Toshiba打破

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02ATXxfxaKd44sekyPPP3Sr78pJTetz6GYUMovM2jhiCwUymWoUfhqCmjn3Lbjzu4wl&id=100054201473657
日經新聞Nekki報導Toshiba打算投資600億日圓將AI資料中心用的HDD產能加倍，目前Toshiba HDD市佔率只有10%，中期目標是提升到30%，不知真假，如果是真......之前WD和Seagate堅持不擴產HDD units，只增加碟片密度(如HAMR)和HDD內碟片數(如12片)來增加容量的作法，被第三名的Toshiba打破

1. 通常事件分析(1)方向，(2)程度，(3)時間，這次再加一個(0)對象
(0)對象產業: DRAM/HBM, SSD, HDD
(1)方向: KV cache分層儲存bytes供給增加......
(2)程度: HDD大、SSD大、DRAM/HBM小(不是零)
(3)時間: 未來一年多內

2. 為何會影響SSD?

因為(1)SSD和HDD本來就是替代品，長期以來到如今，SSD廠商不斷強調SSD因速度、體積、功耗等優點會一直替代HDD，HDD廠則強調還是有價格便宜、大量儲存的優勢 (2)KV cache是SSD和HDD共同需求來源

一兩年前，SSD和HDD的price per bit大約3~5X，最近一年多，SSD大漲價，price per bit差距沒算但應該拉高到10X以上了，HDD的價格優勢更明顯，資料中心storage server/storage clusters內可以用HDD server也可以用SSD server

3. 為何會影響DRAM/HBM?

雖然速度差異大，但HBM和DRAM是共享DRAM wafer製程和產能的，所以一起講

因為KV cache是HDD、SSD、DRAM/HBＭ共同需求來源，請先參考2026/3/18寫過的文章 "KV Cache讓HBM/DRAM、SSD/NAND、HDD、GPU四個產業需求互通"

因為KV cache是最近一年多來HBM/DRAM和SSD需求爆炸的主要原因之一，Nvidia提出KV cache四層儲存和卸載offload策略，G1 GPU HBM、G2 System DRAM、G3 Local SSD、G4 Shared Object/File(Cold or shared KV content)，另加上G3.5層就不多說，KV cache爆炸多，HBM一定裝不下，必須靠軟體演算法整批量卸載到DRAM再整批溢出卸載到Rack SSD再整批溢出卸載到Network Storage/cluster(SSD或HDD)，所以，雖然DRAM和HBM通常是暫存性資料，和SSD和HDD非揮發性可存永久資料不同，但在KV cache這一個需求是共同需求，一起供給，當HDD供給增加，就會影響到其他幾個記憶媒體，從近到遠SSD、DRAM、HBM

上次還提到KV cache可以影響到GPU因為KV cache是新型態的資料，可算可存，多存則少算，少存則多算，像最近Server CPU降規搭配DRAM和GPU降規搭配HBM，就表示未來能存的KV cache減少就需要耗用更多GPU算力，CAPEX減少但TCO增加，但GPU和HDD較遙遠本段先不談

去年一開始曾有很多質疑SSD速度這麼慢，怎可能處理KV cache? 請注意，不是直接存取，那會慢死，是演算法判斷那片資料很熱，那片資料冷掉......用空檔整片整批資料的卸載offload到下一層記憶體SSD甚至HDD，整片資料轉熱的時候再上載回去，除了Nvidia的G3.5層架構並堆出SSD Rack產品之外，HDD廠商如WD也在官網文章直接強調HDD也是KV cache的stack如附圖和網址

4. 600億日圓小到微不足道

是的，和半導體工廠投資額比較來，Toshiba HDD的600億日圓很小，但是HDD的產能相對半導體，本來就不是資本密集，相對不是資本密集、相對折舊佔COGS遠低於半導體DRAM/NAND，要擴廠，不需要像NAND那樣花那麼多錢、那麼久，這也是HDD cost per bit遠比NAND便宜的主意原因，因為CAPEX小很多可以得到一樣的bytes容量，所以，投資擴廠金額不能跟半導體廠比較金額，10%增加一倍的bytes數，不少，中期目標增加20%到30%市佔率，是不小的容量，儲存資料，SSD或HDD都是一個byte一個byte一樣算

5. 一年內怎麼有可能?

HDD工廠擴充產能要多久不清楚，但一定比半導體廠容易，日經新聞說的2027年底，應該是說2027/4~2028/3月，可能上游零件廠擴廠更困難，不知道Toshiba有沒有跟上游一起協調，如果一年多要擴充完成，可能已經有協調了

6. 總體memory/storage看起來仍然缺貨，但這個事件一年多後可能讓gap缺口縮小一點

以下引用的是三月自己寫的文的摘錄:

KV Cache讓HBM/DRAM、SSD/NAND、HDD、GPU四個產業需求互通
......
以前稍微提過，KV Cache是個有趣的全新資料型式，多年來，Memory(如DRAM)和Storage(如HDD/SSD)的需求是 "井水不犯河水"，雖然都和電腦有關，但需求沒有互通

KV Cache把Memory和Storage的需求打通了，需求可以互通

Why? 因為KV Cache可慢可快可頻繁可不頻繁

以前DRAM身為CPU memory，要極頻繁極快速的讀寫，但不能保存也不需保存，Storage讀寫速度慢頻率低，可保存，用途和需求是井水不犯河水，KV Cache呢? 有時候需要頻繁和快速讀寫，如同DRAM的需求，有時候又可以幾秒鐘、幾分鐘、幾天、幾個月不動不讀不寫，這時候需求像Storage

這就是各大模型服務商使用軟體演算法+既有硬體的卸載offload策略，或Nvidia這種領先廠商幫忙客戶開發卸載軟體+特殊硬體(如ICMS/CMX)或把原本不是為此目的的CXL拿來用
......
加入HDD，為何，因為SSD和HDD本來就是互通需求互相取代的
所以現在HBM/DRAM、SSD/NAND、HDD三者需求可以互通了
......"

https://www.nikkei.com/article/DGXZQOUC2442K0U6A920C2000000/

https://blog.westerndigital.com/5-reasons-hdds-belong-in-the-ai-kv-cache-stack/

https://www.facebook.com/share/p/19Quaoambn/
