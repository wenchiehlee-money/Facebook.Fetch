---
post_id: "1477489077401127"
title: "心得1: Test-Time Scaling Law非常明顯、強烈的印證"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0uZ42VRcepc66exx8pxC226NBjmydFYVnXf5EsJbyb4pqfcLhBAX4ZLqtTShpxisel&id=100054201473657"
creation_time_utc: "2026-04-11T12:21:20+00:00"
fetched_at_utc: "2026-05-07T03:35:16.641470+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ3NzQ4OTA3NzQwMTEyNw=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 心得1: Test-Time Scaling Law非常明顯、強烈的印證

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0uZ42VRcepc66exx8pxC226NBjmydFYVnXf5EsJbyb4pqfcLhBAX4ZLqtTShpxisel&id=100054201473657
心得1: Test-Time Scaling Law非常明顯、強烈的印證

心得2: AI Agent爆發之後出現全球性算力不足(CPU+GPU/XPU雙箭頭)

心得3: 誰能立即補充算力? 除了資料中心的電力/廠房之外，在GPU/XPU裡面，誰比較有能力供應 "增加的"、"立即的"，additional算力晶片? ASIC/XPU只供自己和長期合約大客戶使用是固定量，很難，GPU公司有正常的安全庫存現貨、有supply chain pipeline、有最佳的供應鏈(含HBM)產能保障，尤其是最大的GPU公司，Nvidia有一大票客戶組合，有"調度"、reallocation的空間

心得4: 我覺得1~3是昨天Anthropic向Coreweave新簽訂算力供應合約的原因，(1)Coreweave 100%用Nvidia GPU，(2)Anthropic過去一年算力大角度向Google TPU和AWS Trainium遷移，突然 "迴轉" 回Nvidia GPU懷抱顯得唐突，可能是因為Google/Broadcom、AWS緩不濟急、增量困難

以下摘錄自電腦王阿達文章: 
"數據證明 Claude 真的變笨了！AMD AI 總監揭露 Anthropic 偷偷降低思考深度"

----------"數據顯示，在不久前 2026 年 2 月初（OpenClaw 還沒那麼火的當下）的「黃金時期」，Claude Opus 的平均思考深度約為 2,200 個字元，這代表模型在動筆改 Code 前，會進行極其細膩的邏輯推演。然而，到了 2 月下旬，這個數字暴跌至 720 個字元；進入 3 月，更是縮水到僅剩 560 個字元左右，跌幅高達 73% 至 75% 。
......
Stella 團隊提出了一個關鍵工程指標：Read:Edit Ratio（讀修比）。在 2 月中旬之前的正常運作期間，Claude 的讀修比平均為 6.6。這代表模型每進行一次修改，平均會讀取 6.6 個相關檔案，包括目標原始碼、標頭檔、測試案例以及全域搜尋結果。這種「先看再動」的模式保證了程式碼的精確度與系統穩定性。

但在 3 月 8 日的「效能轉折點」之後，這個比率驟降到了 2.0 。更驚人的是，有超過 33.7% 的修改行為是在「完全沒有預先讀取檔案」的情況下直接發生的。AI 開始憑感覺盲改，甚至頻繁使用全檔重寫（Full-file Write）來取代精確的差異編輯（Diff Edit），這種「蠻力修改」導致了嚴重的程式碼回歸（Regression），讓開發者每天必須花費數小時來修復 AI 搞壞的東西。
......
在 3 月 8 日之前，這個監測腳本記錄到的違規次數是 0。然而在之後短短兩週內，數據出現了爆炸性增長：
1. 責任甩鍋（Blame Shifting）：出現了 73 次。AI 開始會說「這不是我改出來的問題」或「這是既有的 bug」。
2. 提前收工（Early Stopping）：出現 18 次。AI 會在工作完成一半時說「這是一個不錯的停止點」，拒絕繼續推演 complex logic。
3. 過度徵詢（Permission Seeking）：出現 40 次。AI 反覆詢問「我真的要繼續嗎？」而不是主動解決問題，這被視為一種消耗用戶 Session 額度並規避工作的手段。

這些行為模式的突變，證明了 Claude 已經學會了人類最糟糕的職場習慣：如何看起來在工作，但實際上是在推託。
......
更嚴重的問題在於「Session Limit」。由於模型的 Read:Edit 比率降低，AI 頻繁出錯，導致用戶必須不斷下指令修正。這形成了一個惡性循環：AI 變笨 → 出錯 → 用戶修正 → 消耗更多 Token → 觸發 Session Limit（通常僅需 20-30 分鐘便會耗盡當日配額）。對開發者而言，這不僅是技術退步，更是生產力的謀殺。
......
目前 Anthropic 官方對此 Issue 的回應仍集中在「默認設置微調」與「UI 顯示優化」 ，但顯然無法說服全球各地憤怒的使用者。雖然這波 AI Agent 的突然爆發可能讓 Anthropic 的算力無法承受，所以只能用降低算力的「偷雞」方式解決
......"

https://www.koc.com.tw/archives/638616


---
[📌 新增貼文至TAIEX.TW比對](https://github.com/wenchiehlee-money/TAIEX.TW/issues/new?template=earnings_tag.yml&title=2026%20%20%E8%B2%A1%E5%A0%B1%E6%A8%99%E8%A8%98&symbol=2026&file_path=data%2FRichard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards%20Research%20Blog%2F2026-04-11_%E5%BF%83%E5%BE%971-Test-Time-Scaling-Law%E9%9D%9E%E5%B8%B8%E6%98%8E%E9%A1%AF%E5%BC%B7%E7%83%88%E7%9A%84%E5%8D%B0%E8%AD%89.md&period=)


---
[📌 新增貼文至biztrends.TW比對](https://github.com/wenchiehlee-money/biztrends.TW/issues/new?template=earnings_tag.yml&title=%E8%B2%BC%E6%96%87%E6%A8%99%E8%A8%98&symbol=&file_path=data%2FRichard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards%20Research%20Blog%2F2026-04-11_%E5%BF%83%E5%BE%971-Test-Time-Scaling-Law%E9%9D%9E%E5%B8%B8%E6%98%8E%E9%A1%AF%E5%BC%B7%E7%83%88%E7%9A%84%E5%8D%B0%E8%AD%89.md&period=)
