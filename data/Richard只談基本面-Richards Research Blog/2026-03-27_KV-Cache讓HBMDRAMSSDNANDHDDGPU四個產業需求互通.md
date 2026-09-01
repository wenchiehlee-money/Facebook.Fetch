---
post_id: "1465929975223704"
title: "KV Cache讓HBM/DRAM、SSD/NAND、HDD、GPU四個產業需求互通"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0FfssLyW8VSvCBSALjnx3VuE2pXb7AbpPy74qRnx7eDxKptXUdegrbTbPod9BPf8Ll&id=100054201473657"
creation_time_utc: "2026-03-27T16:32:22+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-6/656699333_1465931441890224_2878503830537150994_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=6zLiBtAzePEQ7kNvwHZo4di&_nc_oc=AdoAte0EsxKLbI4oC2cmRwAZKEhsc_CcYFp1t6jOgzKjCglSr3cFyopSLi5ifLAGZZA&_nc_zt=23&_nc_ht=scontent-lax3-2.xx&_nc_gid=DO_NxaCmSgswG59FgQAD8w&_nc_ss=78100&oh=00_Af-qnVREXjv4D7uSjk11vhWXocljtRY2FMTRlukMI408DQ&oe=6A386362"
feedback_id: "ZmVlZGJhY2s6MTQ2NTkyOTk3NTIyMzcwNA=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# KV Cache讓HBM/DRAM、SSD/NAND、HDD、GPU四個產業需求互通

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0FfssLyW8VSvCBSALjnx3VuE2pXb7AbpPy74qRnx7eDxKptXUdegrbTbPod9BPf8Ll&id=100054201473657

![KV Cache讓HBM/DRAM、SSD/NAND、HDD、GPU四個產業需求互通](https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-6/656699333_1465931441890224_2878503830537150994_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=6zLiBtAzePEQ7kNvwHZo4di&_nc_oc=AdoAte0EsxKLbI4oC2cmRwAZKEhsc_CcYFp1t6jOgzKjCglSr3cFyopSLi5ifLAGZZA&_nc_zt=23&_nc_ht=scontent-lax3-2.xx&_nc_gid=DO_NxaCmSgswG59FgQAD8w&_nc_ss=78100&oh=00_Af-qnVREXjv4D7uSjk11vhWXocljtRY2FMTRlukMI408DQ&oe=6A386362)
KV Cache讓HBM/DRAM、SSD/NAND、HDD、GPU四個產業需求互通

最近KV Cache這個字爆紅，以前咖啡廳偶爾聽到隔壁聊聯發科、台積電，後來聽到CoWoS、幾奈米，以後如果聽到KV Cache應該不會太意外

以前稍微提過，KV Cache是個有趣的全新資料型式，多年來，Memory(如DRAM)和Storage(如HDD/SSD)的需求是 "井水不犯河水"，雖然都和電腦有關，但需求沒有互通

KV Cache把Memory和Storage的需求打通了，需求可以互通

Why? 因為KV Cache可慢可快可頻繁可不頻繁

以前DRAM身為CPU memory，要極頻繁極快速的讀寫，但不能保存也不需保存，Storage讀寫速度慢頻率低，可保存，用途和需求是井水不犯河水，KV Cache呢? 有時候需要頻繁和快速讀寫，如同DRAM的需求，有時候又可以幾秒鐘、幾分鐘、幾天、幾個月不動不讀不寫，這時候需求像Storage

這就是各大模型服務商使用軟體演算法+既有硬體的卸載offload策略，或Nvidia這種領先廠商幫忙客戶開發卸載軟體+特殊硬體(如ICMS/CMX)或把原本不是為此目的的CXL拿來用

加入HDD，為何，因為SSD和HDD本來就是互通需求互相取代的

所以現在HBM/DRAM、SSD/NAND、HDD三者需求可以互通了

KV Cache甚至進一步把Memory+Storage和GPU/XPU計算晶片的需求打通了

Why? 因為KV Cache可存可算

KV Cache是為減少計算而生，Context存Text檔就每次重新複雜龐大計算量，存KV Cache(一個token約90K~數百K bytes vs 一個英文單字約1.3 tokens)就可以不用計算但是耗費HBM/DRAM或SSD空間(看當時KV Cache是存在那裡)

同樣品質下，多存則少算，少存則多算，互相影響，多用memory/Storage就少用GPU，多用GPU就少用memory/Storage

所以現在HBM/DRAM、SSD/NAND、HDD、GPU/XPU四個產業需求可以互通了

所以現在Samsung, SK Hynix, Micron, Kioxia, Sandisk, Seagate, WD, Nvidia, AMD, XPU/ASIC, 需求有了互通的管道，因為KV Cache而變成生命共同體了

這個觀念其實是老黃講的，我只是把它應用到產業需求的理解上，老黃去年在發表ICMS(CMX)的時候提到KV Cache是一種新的資料型態，需要特別設計的軟硬體架構，老黃是非常清楚也是最早公開提出這觀點的

附圖以前寫CXL的文的時候改過貼過，也是取自老黃演講，充分提到memory和storage需求互通這點，但沒提到和GPU也互通

有沒有覺得某些事情突然合理些了?

還有一個想法，就是KV Cache不是只能同用戶長記憶context自用，多用戶可共享，對規模經濟的影響，一家服務數百萬人的模型商，相對小型模型服務商，有許多許多的多客戶之間共用KV Cache，例如，川普是誰? 伊朗是甚麼國家? 這種問題，最近可能被用戶詢問無數次， 或百科歷史問答等，或coding中有極多的程式碼重複小片段，把答案敘述tokens高關聯KV Cache存起來，大廠可以重複使用千百萬次，小廠幾萬次，同樣的儲存成本(或算力成本)

這是規模經濟、大廠有利，當然也需要廠商的演算法技術力才能發揮，很多實驗要做隨時變更或改進卸載策略，而老黃有整套的軟硬體工具幫客戶更快上手
