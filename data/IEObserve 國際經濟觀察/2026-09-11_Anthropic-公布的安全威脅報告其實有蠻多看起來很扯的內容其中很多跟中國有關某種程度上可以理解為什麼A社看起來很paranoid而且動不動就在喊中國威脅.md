---
post_id: "1603809117770377"
title: "Anthropic 公布的安全威脅報告其實有蠻多看起來很扯的內容，其中很多跟中國有關，某種程度上可以理解為什麼A社看起來很paranoid而且動不動就在喊中國威脅。"
page_title: ""
requested_url: "https://www.facebook.com/intleconobserve"
final_url: "https://www.facebook.com/intleconobserve"
post_url: "https://www.facebook.com/intleconobserve/posts/pfbid02UUTP3Nxek9NDtg54VyLyjNK7etzqzbGRXwjr1Evs7bRbnzK4Fri4kcjE9anN8fkGl"
creation_time_utc: "2026-09-11T02:59:31+00:00"
fetched_at_utc: "2026-09-30T03:42:42.401092+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-ord5-2.xx.fbcdn.net/v/t39.30808-6/801045202_1603808157770473_5618577919198388266_n.jpg?stp=dst-jpg_p843x403_tt6&_nc_cat=102&ccb=1-7&_nc_sid=127cfc&_nc_ohc=cPaU6fCIqOsQ7kNvwFTJy1W&_nc_oc=AdoPxAI4e3gJb1PtnIwIisDb7xuviS4G7YlrB6uyGjHZhHqpLa10YXvvV9RmdELFQ6o&_nc_zt=23&_nc_ht=scontent-ord5-2.xx&_nc_gid=vlyjdiGChyyRZUWgxk7cLg&_nc_ss=7e120&oh=00_AQPMav88ecxFO5LYHf2Qg7ATdyuvhhJjM5_GgPpIsxp1dA&oe=6AC24CED"
feedback_id: "ZmVlZGJhY2s6MTYwMzgwOTExNzc3MDM3Nw=="
page_canonical_url: ""
---

# Anthropic 公布的安全威脅報告其實有蠻多看起來很扯的內容，其中很多跟中國有關，某種程度上可以理解為什麼A社看起來很paranoid而且動不動就在喊中國威脅。

原文連結: https://www.facebook.com/intleconobserve/posts/pfbid02UUTP3Nxek9NDtg54VyLyjNK7etzqzbGRXwjr1Evs7bRbnzK4Fri4kcjE9anN8fkGl

![Anthropic 公布的安全威脅報告其實有蠻多看起來很扯的內容，其中很多跟中國有關，某種程度上可以理解為什麼A社看起來很paranoid而且動不動就在喊中國威脅。](https://scontent-ord5-2.xx.fbcdn.net/v/t39.30808-6/801045202_1603808157770473_5618577919198388266_n.jpg?stp=dst-jpg_p843x403_tt6&_nc_cat=102&ccb=1-7&_nc_sid=127cfc&_nc_ohc=cPaU6fCIqOsQ7kNvwFTJy1W&_nc_oc=AdoPxAI4e3gJb1PtnIwIisDb7xuviS4G7YlrB6uyGjHZhHqpLa10YXvvV9RmdELFQ6o&_nc_zt=23&_nc_ht=scontent-ord5-2.xx&_nc_gid=vlyjdiGChyyRZUWgxk7cLg&_nc_ss=7e120&oh=00_AQPMav88ecxFO5LYHf2Qg7ATdyuvhhJjM5_GgPpIsxp1dA&oe=6AC24CED)
Anthropic 公布的安全威脅報告其實有蠻多看起來很扯的內容，其中很多跟中國有關，某種程度上可以理解為什麼A社看起來很paranoid而且動不動就在喊中國威脅。
----
#狸貓換太子：Moonshot（Kimi）與 DeepSeek 的中間人竊取與嚴重洩密

靜默轉發（Silent Relay）： 月之暗面（Moonshot）與 DeepSeek 均被發現將其自身產品使用者的對話請求，在用戶完全不知情的情況下偷偷轉發給美方的 Claude 模型處理，再將結果回傳給用戶。

兩家公司藉由這種中間人代理架構，一方面免去自身伺服器的運算成本，另一方面暗中側錄使用者的真實問答作為蒸餾訓練材料。

思維簽名重放攻擊（Thinking Signature Replay Attack）： 為了防止蒸餾，Anthropic 僅在 API 中回傳加密的「思維簽名」（Thinking Signature）。

Moonshot 與 DeepSeek 研發出跨會話重放技術，將保存的加密簽名在新會話中重新誘使 Claude 解碼為明文思考鏈，藉此完全瓦解技術防護。

不可控的敏感數據外洩： 由於這兩家廠商將使用者的原始輸入無差別轉發至美國伺服器，直接導致其國內用戶與企業的極度機密資訊裸奔：

#解放軍與國防軍工監視影像： 一名隸屬解放軍的用戶將成都市數百個天網監視器畫面（包含解放軍設施及中國電子科技集團 CETC 研究所周邊）輸入 Kimi 進行「異常行為分析」，該即時監控數據直接被 Moonshot 轉發至 Anthropic。

#俄羅斯國防部與外國藥廠機密： DeepSeek 轉發的請求中，包含了俄羅斯國防部外包 IT 工程師輸入的政府資料庫連線即時憑證；以及某跨國大藥廠在東南亞四國高達數千萬美元的資本支出（CapEx）工廠擴建預算明細。

#中國公安警務大數據： 公安局技術人員在開發「利用身分證號碼進行軌跡比對」的警務案件系統時，原始代碼與資料庫結構全數經由 DeepSeek 轉發至境外。

#次級黑市轉售：商湯（SenseTime）與 MiniMax
報告指出，中企對西方算力與模型能力的渴望催生了龐大的灰色「API 轉發站（Transfer Stations）」黑市。MiniMax 被查出設立無明顯關聯的海外空殼公司，專門搭建只提供 OpenAI 與 Anthropic 模型存取的轉發中繼服務，目的純粹是攔截真實使用者的提示詞來訓練自己的模型

而商湯科技（SenseTime）則直接向第三方黑市數據商採購這類被非法側錄的 Claude 對話數據，用於架構其自身的蒸餾訓練管線。

阿里巴巴（Alibaba / Qwen）的 #超大規模蒸餾
阿里巴巴發動了 Anthropic 監控史上規模最大的蒸餾攻擊。透過注入固定提示詞，強制模型在輸出終端答案前以標籤寫出完整的內部思考步驟。

這些思維鏈數據隨後被轉化為監督微調（SFT）資料集，直接灌入其主力開源模型 Qwen 3.5、3.6 與 3.7 的訓練流程中，涵蓋底層核心開發、長期複雜推理與 Agent 工具使用能力。

#非法的工業級蒸餾 所謂非法蒸餾，是指未經授權透過自動化程式向高階「教師模型」（如 Claude Opus）發送數百萬次具針對性的複雜邏輯提示，竊取其內部的推理軌跡（Reasoning Traces），並將這些高品質數據用於訓練本土的「學生模型」，從而在極短時間內、花費極低算力成本取得頂級代碼與推理能力。

#跨國鎮壓與涉台輿情情資處置（GTG-14021 與 GTG-14022）
地方公安局網警與警校研究生利用 Claude Code 操作輿情監控系統，追蹤海外異議人士（如知名社群帳號「李老師不是你老師」）。

#管控名單生成： 操作者透過反覆誘導（Re-prompting），規避模型的安全防護，直接由 AI 產出對境內 10 名維權訪民的具體管控方案，包括截訪、強制「約談」及通訊定位限制。

#涉台輿情重構： 承包商（GTG-14022）每天處理數十篇外媒與台灣媒體報導，將台灣的外交與文化活動自動標註為「對主權之威脅」，並將涉及人權的詞彙套上諷刺引號，轉化為向中共高層匯報的「三戰」（心理戰、法律戰、輿論戰）專報。

#敘利亞維吾爾人的跨國誘捕（GTG-14010）
一名不具備阿拉伯語能力的中國外包人員，利用 AI 監控逾 100 個 WhatsApp 群組與 Telegram 頻道，篩選出在敘利亞具有軍事背景或生活困頓的維吾爾族人。

透過 Claude 扮演中東方言軍事顧問，該操作者以流利的敘利亞阿拉伯語進行多日臥底對話，企圖以虛擬貨幣或資金報酬招募線人，並鎖定其在新疆境內家屬以施加壓力。
