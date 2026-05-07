---
post_id: "1479853307164704"
title: "1. 2026年因Agentic AI，CPU從AI間接受惠變直接受惠、配角變主角(之一)、CPU+GPU/XPU雙箭頭"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0KbLeE7DUkHuDUyPVKFdsksbovJ6dz3kdroyis47uN4CA8vC2TvWT3BT3QdKkSeGAl&id=100054201473657"
creation_time_utc: "2026-04-14T14:14:58+00:00"
fetched_at_utc: "2026-05-07T03:35:16.641470+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ3OTg1MzMwNzE2NDcwNA=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 1. 2026年因Agentic AI，CPU從AI間接受惠變直接受惠、配角變主角(之一)、CPU+GPU/XPU雙箭頭

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0KbLeE7DUkHuDUyPVKFdsksbovJ6dz3kdroyis47uN4CA8vC2TvWT3BT3QdKkSeGAl&id=100054201473657
1. 2026年因Agentic AI，CPU從AI間接受惠變直接受惠、配角變主角(之一)、CPU+GPU/XPU雙箭頭

2. AI資料中心CPU:GPU/XPU從1:4~1:8變1:1~1:2，資料中心等級CPU是目前瓶頸，比GPU/XPU還缺

3.假設算一下，AI資料中心GPU/XPU成長60%，CPU:GPU配比從1:5變1:1.5的話，CPU要成長幾%?

4.今年寫過有關CPU的觀察和心得文章放在留言共14篇

----------TrendForce"偉大的再平衡：代理型人工智慧如何重塑 CPU：GPU 比例

代理式人工智慧正推動 CPU：GPU 比例的結構性轉變，並引發供應緊縮，導致英特爾與 AMD 調漲價格。
......
CPU 主要負責壓縮和路由記憶體資料到 GPU。因此，現今的 AI 資料中心運作時，CPU 與 GPU 的比例大約是 1：4 到 1：8。
......
AI 代理的興起正在改變這種平衡。與靜態大型語言模型不同，代理人工智慧設計為能動態與環境互動——規劃任務、呼叫工具、做出決策，並代表使用者採取行動。管理這一切的協調層——排程子任務、工具調用路由、子代理間資料傳遞，以及評估原始請求是否已完成——完全由 CPU 負責。這正是編排成為 CPU 密集型工作負載的原因。
Unlike static LLMs, Agentic AI is designed to interact dynamically with its environment—planning tasks, calling tools, making decisions, and taking actions on behalf of users. The coordination layer that manages all of this—scheduling sub-tasks, routing tool calls, passing data between sub-agents, and evaluating whether the original request has been fulfilled—falls squarely on the CPU. This is what makes Orchestration a CPU-intensive workload.
......
傳統的 CPU 與 GPU 比例必須改變。Arm估計，傳統AI資料中心每GW約需3,000萬CPU核心，但在AI Agent時代，需求將激增至每GW1.2億個，增幅為四倍。未來 CPU 與 GPU 的比例預計將調整至 1：1 至 1：2，顯著提升市場對 CPU 的需求。

CPU 需求在 AI 工作負載與資料中心的通用伺服器中都大幅成長。Intel 與 AMD 於 2026 年第一季末，透過調漲部分 CPU 產品線的價格作為回應。

2026 年 CPU 市場格局

這種需求轉變正在重塑競爭格局。除了傳統的伺服器 CPU 廠商 Intel 和 AMD，一波非傳統的競爭者——GPU 製造商 Nvidia、IP 授權商 Arm，以及包括 AWS、Google 和 Microsoft 在內的主要雲端服務提供商（CSP）——現在正進入伺服器 CPU 市場。
......
AMD預計在2026年將持續從英特爾手中搶佔市場份額。
......
2026 年 3 月，Nvidia 宣布將開始將 Vera CPU 作為獨立產品銷售，以回應客戶對更靈活 CPU：GPU 配置的需求。早期合作夥伴包括阿里巴巴、字節跳動、Cloudflare、CoreWeave、Crusoe、Lambda、Nebius、Nscale、Oracle、Together.AI 和 Vultr

同樣在 2026 年 3 月，Arm 以 Arm AGI CPU 邁出前所未有的步伐進入 CPU 產品市場，結束了 35 年的純粹授權。它基於台積電 N3 架構，採用 Arm Neoverse V3 架構，提供 136/136 核心/執行緒。啟動合作夥伴包括 Meta、Cerebras、Cloudflare、F5、OpenAI、Positron、Rebellions、SAP 及 SK Telecom

Arm 推出了兩種獨立 CPU 機架：一種是風冷版本，整合 60 顆 AGI CPU（8,160/8,160 核心/執行緒，~180 TB 記憶體），以及液冷版本，支援 336 顆 CPU（45,696/45,696 核心/執行緒，1 PB 記憶體）
......
以下我們總結了 2026 年主要 CPU 的核心與執行緒數量。可以觀察到 Intel Xeon 6+（Clearwater Forest）將達到最大核心數 288 個。接著是 AMD EPYC Venice、Intel Xeon 7（Diamond Rapids）和 AmpereOne MX，皆配備 256 核心。然而，由於採用同時多執行緒（SMT）技術，AMD EPYC Venice 能在 256 核心上執行 512 執行緒，達到目前可用的最高執行緒數"

https://insights.trendforce.com/p/agentic-ai-cpu-gpu


---
[📌 新增貼文至TAIEX.TW比對](https://github.com/wenchiehlee-money/TAIEX.TW/issues/new?template=earnings_tag.yml&title=2026%20%20%E8%B2%A1%E5%A0%B1%E6%A8%99%E8%A8%98&symbol=2026&file_path=data%2FRichard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards%20Research%20Blog%2F2026-04-14_1-2026%E5%B9%B4%E5%9B%A0Agentic-AICPU%E5%BE%9EAI%E9%96%93%E6%8E%A5%E5%8F%97%E6%83%A0%E8%AE%8A%E7%9B%B4%E6%8E%A5%E5%8F%97%E6%83%A0%E9%85%8D%E8%A7%92%E8%AE%8A%E4%B8%BB%E8%A7%92%E4%B9%8B%E4%B8%80CPUGPUXPU%E9%9B%99%E7%AE%AD%E9%A0%AD.md&period=)
