---
post_id: "1617745036708863"
title: "嚇我一跳，因為WCCFTECH一篇文章標題寫Muse讓CPU:GPU=40:1"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0GU2LNBv1xkirBZsUGWL8KBhDBuRjxJ5e6jrtLfq3jWahYb1AuHPx9UAUpdNuuYRfl&id=100054201473657"
creation_time_utc: "2026-09-22T14:44:54+00:00"
fetched_at_utc: "2026-09-30T03:40:08.969076+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0GU2LNBv1xkirBZsUGWL8KBhDBuRjxJ5e6jrtLfq3jWahYb1AuHPx9UAUpdNuuYRfl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTYxNzc0NTAzNjcwODg2Mw=="
page_canonical_url: ""
---

# 嚇我一跳，因為WCCFTECH一篇文章標題寫Muse讓CPU:GPU=40:1

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0GU2LNBv1xkirBZsUGWL8KBhDBuRjxJ5e6jrtLfq3jWahYb1AuHPx9UAUpdNuuYRfl&id=100054201473657
嚇我一跳，因為WCCFTECH一篇文章標題寫Muse讓CPU:GPU=40:1

"Meta 的 Muse Agent 為 CPU 引發「Claude Code」時刻，40：1 的 CPU 與 GPU 比例有望重塑 Intel、AMD 與 Arm 的命運
Meta’s Muse Agent Sparks ‘Claude Code’ Moment For CPUs, As 40:1 CPU-To-GPU Ratio Poised To Reshape Intel, AMD, And Arm’s Fortunes"

同時心裡很好奇，這是怎麼算出來的? (1)因為不只是使用者的Agentic AI任務workload千變萬化，就算Meta/OpenAI/Anthropic服務提供商都不見的抓得準，我們知道那些任務該用CPU(例如網路查詢)、那些任務該用GPU(例如分析文意/圖意)，但這些任務的比例如何是怎麼算的呢? (2)再來CPU和GPU的比較 "單位" 是什麼? CPU和CPU比較有很多清楚的benchmark標準單位，GPU和GPU比較也有很多performance標準，之前討論GPU HBM workload卸載offload到CPU Host DRAM再卸載到SSD雖然複雜難算，但至少模型商可能抓得出來，因為這是記憶體，資料就是資料，1 byte存在HBM、DRAM、SSD都是1 byte，但是CPU和GPU要如何比較算力、任務、工作負載workload?  想知道這兩點

文章沒講這兩點，40:1這個數字來自於一位獨立研究者X帳號Damnang貼文，寫到

"They said that in some extreme cases, the CPU to GPU ratio could reach as high as 40:1"
他們提到，在部分極端案例中，CPU 對 GPU 的配比最高可達到 40:1

重點是這個英文是:

極端案例，最高可達40:1，既然是極端就不是平均，語法來說，另一個極端也可能是相反1:40，當然我們相信包含Muse在內的任何Agentic AI都是向CPU移動的(之前說從1:4移動到1:1)

所以，有沒有40:1的數字來源? 沒有，來源是說極端+最高=40:1，WCCFTECH省略了extreme......as high as，標題的40:1就是平均數(不論那一種平均數)的意思，意義大不同，所以40:1世界上沒有人這樣講，是WCCFTECH自己創造(或自己分析歸納屬質文字後判斷而得)的數字

但是我們估計市場數量，需要的是平均而不是極端阿! 極端狀況數字對於market、shipments沒有意義阿! 

"隨著像 Muse 這樣的個人經紀人規模擴大，CPU 需求即將爆炸式增長，CPU 與 GPU 的比例估計從 4：1 到 40：1 不等！事實上，根據高盛的說法，CPU 已經比 GPU 還要多用短期資本支出.
As personal agents like Muse scale, the demand for CPUs is all set to explode, with estimates for the CPU to GPU ratio ranging between 4:1 all the way to 40:1! In fact, according to Goldman Sachs, CPUs are already hogging more of the short-dated CapEx than GPUs."

因為X原始出處沒有這樣說，因此這裡的40:1的estimates就是WCCFTECH作者自己估計的，或者他以為是4:1~40:1? 但讀者想的是1:4(目前CPU是1/GPU是4)到4:1再到40:1......

至於說出extreme......as high as......40:1的他們是誰?是X作者訪問SK Hynix記憶體議題的內容中，插播一句SK Hynix對CPU的談話，就這樣，不是AMD, Intel, NV也不是模型公司或Hyperscaler，有來源、有原文，很好，對不對至少讀者可自行判斷參考性，但是SK Hynix或X作者都沒有說40:1他們是說"極端案例下"、"最高配比"可能40:1

https://wccftech.com/metas-muse-agent-sparks-claude-code-moment-for-cpus-as-401-cpu-to-gpu-ratio-poised-to-reshape-intel-amd-and-arms-fortunes/?utm_source=chatgpt.com
