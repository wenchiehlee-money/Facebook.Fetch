---
post_id: "1560763495740351"
title: "任何擔心Kimi K3影響AI硬體支出的人，應該都要先知道一件事，Kimi K3不是像Deepseek、GLM 5.2這種幾千億參數的\"相對小\"模型，Kimi K3的參數量高達2.8兆，和Anthropic和OpenAI幾個一流前沿模型屬於同一個參數規模等級的\"大模型\""
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02cKVarZAxVzCqFsypR5AqADBNgBeJCXHvCqkCfgeKnQUMgfypYa4Z2PcRY6d3EPe4l&id=100054201473657"
creation_time_utc: "2026-07-18T04:31:44+00:00"
fetched_at_utc: "2026-07-20T13:02:55.617710+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU2MDc2MzQ5NTc0MDM1MQ=="
page_canonical_url: ""
---

# 任何擔心Kimi K3影響AI硬體支出的人，應該都要先知道一件事，Kimi K3不是像Deepseek、GLM 5.2這種幾千億參數的"相對小"模型，Kimi K3的參數量高達2.8兆，和Anthropic和OpenAI幾個一流前沿模型屬於同一個參數規模等級的"大模型"

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02cKVarZAxVzCqFsypR5AqADBNgBeJCXHvCqkCfgeKnQUMgfypYa4Z2PcRY6d3EPe4l&id=100054201473657
任何擔心Kimi K3影響AI硬體支出的人，應該都要先知道一件事，Kimi K3不是像Deepseek、GLM 5.2這種幾千億參數的"相對小"模型，Kimi K3的參數量高達2.8兆，和Anthropic和OpenAI幾個一流前沿模型屬於同一個參數規模等級的"大模型"

這意味什麼？

1.Kimi K3如果流行，推論所消耗的算力不會比目前閉源前沿模型少

演算法改進可能會減少硬體資源，但各種演算法cost down各家公司一直進行從未停止，而且參數量影響算力需求更直接，Kimi K3不但把開源模型尺寸拉到一兆參數以上，更直接跳數倍到2.8兆

2.如同以前曾流行過的開源模型Llama系列、Deepseek系列，開源之後各界會有幾百幾千個公開加未公開更多的"後訓練"版本出來，後訓練算力=2.8兆參數大模型x幾百幾千幾萬次(倍)後訓練算力需求，雖然單次比單次後訓練算力需求比預訓練算力需求少

3.Kimi K3開源對用戶是省掉高昂預訓練研發費用攤提，每家Hyperscsler和CSP都可拿去用，AWS/微軟/Google也可加入他們本有的開源模型庫經營雲端開源模型推論業務，但因為2.8T參數量，消耗掉的算力資源並不一定比Open AI和Anthropic領先模型少

4.Kimi K3如果被企業大量採用，因為企業買HGX B300自用比雲端大家共用對硬體使用較沒效率，總算力需求更大，例如一台CSP GB300 NVL72給1000人共用，這些用量由不同企業分別自購9台HGX B300 NVL8本地推論，HBM參數要存幾個copy、同時佔用幾倍用量？9倍，HBM用量多9倍，2.8T要2800GB或4 bits精度1400GB，多9倍用量，先不計算GPU使用率

5.用戶省掉的成本，是昂貴的研發費用和預訓練費用的攤提和模型公司的利潤，不是省推論硬體開支

重點一個，Kimi K3不是小模型，是和GPT 5.5、Opus規模類似的大模型，對硬體需求不會減少
