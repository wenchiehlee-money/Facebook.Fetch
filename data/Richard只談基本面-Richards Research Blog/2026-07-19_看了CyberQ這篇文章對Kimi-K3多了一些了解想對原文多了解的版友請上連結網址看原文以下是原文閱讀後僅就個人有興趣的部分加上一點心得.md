---
post_id: "1561923368957697"
title: "看了CyberQ這篇文章，對Kimi K3多了一些了解，想對原文多了解的版友請上連結網址看原文，以下是原文閱讀後僅就個人有興趣的部分，加上一點心得:"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid021CqLw17wLaPfycwaYhtdzxZKFGNcjivTnwaWMmX9xQrek7DH9V4kHNRb3M28Lnm4l&id=100054201473657"
creation_time_utc: "2026-07-19T15:51:19+00:00"
fetched_at_utc: "2026-07-20T13:02:55.617710+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU2MTkyMzM2ODk1NzY5Nw=="
page_canonical_url: ""
---

# 看了CyberQ這篇文章，對Kimi K3多了一些了解，想對原文多了解的版友請上連結網址看原文，以下是原文閱讀後僅就個人有興趣的部分，加上一點心得:

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid021CqLw17wLaPfycwaYhtdzxZKFGNcjivTnwaWMmX9xQrek7DH9V4kHNRb3M28Lnm4l&id=100054201473657
看了CyberQ這篇文章，對Kimi K3多了一些了解，想對原文多了解的版友請上連結網址看原文，以下是原文閱讀後僅就個人有興趣的部分，加上一點心得:

正面: Nvidia HGX B300 NVL8、AMD MI350 Server、CSP推論服務、更期望加速企業本地推論市場
不正面: Google

1. K3原生資料精度MXFP4，以每參數4 bits計算，VRAM需要1.4~1.5TB以上，還需要預留程式執行空間，Moonshot官方建議64顆GPU的Supernode，對岸說Supernode這個字通常翻成超節點，可以理解為Scale Up Domain、像NVLink 72等，就是說，Kimi K3以2.8兆參數量，並不是像DeepSeek、Qwen、GLM等開源模型可以在RTX PRO 6000等單機Server上跑動的

我算了一下，HGX B300 NVL8(B200不行)的288GB x 8 =2.3TB應該是可以跑動的，可能因為HGX不像GB300 NVL72名氣大，但是如果要企業本地推理，企業買8顆GPU的HGX B300比72顆的GB300更實際又有擴展彈性，或更便宜的AMD MI350 Server(單顆VRAM也是288GB哦)

2. MoE不管你一次調用幾個專家，全部896個專家權重必須常駐於VRAM中(資料中心Server VRAM都是HBM)，以上1.4~1.5TB VRAM不能少， CyberQ的文章是這樣寫得"值得注意的是 MoE 的一個常見誤解，稀疏啟用省的是每 token 的運算量，不是儲存空間。896 個專家必須全數常駐於服務叢集的記憶體中，這也讓高速互連（NVLink、InfiniBand）成為部署的一級需求，而非選"

3. 其他文章看到Kimi MoE因為將896個專家權重分散存放在各顆GPU VRAM中，所以專家間的資料搬動/溝通，就是GPU之間的資料搬運，非常頻繁，很需要Nvidia NVLink這種高速scale up通訊

4. CyberQ 認為Kimi K3的開源受益者是全球各國的AI推理服務供應商、主權 AI 雲、大型雲端服務公司與擁有足夠GPU叢集的大型企業，可以直接佈署Kimi K3

5. 我個人是覺得HGX B300 NVL8是許多企業可以買得起的範圍內，有機會增加HGX Server銷售量，前兩天寫過一文，期待企業本地推理市場終於要興起

至於其他中小企業，只能上雲使用Kimi K3，但目前看起來，Kimi K3並不便宜，如果不便宜的話，就繼續使用Anthropic或Open AI就好

6. CyberQ的務實解是雲地混合路由建議，本地跑Kimi 2.7前代模型、雲端呼叫旗艦Kimi K3，敏感個資與小型任務留在本地、大型專案與深度推理用到雲端

7. 我個人覺得預算允許的話也可以考慮，更上一層級，本地採購HGX B300 NVL8跑Kimi K3，雲端任務給Anthropic或Open AI

8.還有一個超划算的選項，可能大家一時沒想到，目前和Hopper等級的AMD MI350一台8顆GPU，每顆GPU是288GB HBM3e，和B300一樣的VRAM容量，這樣不用HGX B300，用上一代等級的的AMD MI350即可，如果不在乎速度只在乎跑得動的總成本，而且MI350也有硬體原生支援FP4

AMD MI350 Server是最佳解，GPU是H200等級，但VRAM遠高於H200，又有FP4硬體原生MXPF4精度，是不是最適合!

9. AWS Bedrock、Azure AI Foundry、GCP Gardon/Vertex AI都有開源模型的推論服務，但是大家非常推崇的Google TPU，到目前量產佈署的TPU V7e，沒有FP4原生硬體支援，只有FP8，所以理論上，將來如果三家都有佈署Kimi K3，在GCP上面跑K3成本將最高

10. 還有在模型商的角度，Google的Gemini被擠下前三的地位，而且是被開源模型擠下去的，有點情何以堪

Google雙重不受惠: Gemini被超越、TPU不支援FP4

CyberQ原文:
Kimi K3 開源倒數 1.4TB 權重誰跑得動？「自稱 Claude」爭議下，雲地混合是企業務實解
https://cyberq.tw/2026/07/19/kimi-k3-open-source-13382/

Kimi K3是2.8兆參數的大模型，不會減少算力需求
https://www.facebook.com/share/p/18qvZ3JSdz/

2H26~2027企業本地AI算力需求起飛的可能性和影響(開源GLM 5.2和Kimi K3能力提升)
https://www.facebook.com/share/p/19HeszR7AB/
