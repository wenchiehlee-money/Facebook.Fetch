---
post_id: "1481175830365785"
title: "心得1. AI需求同步推升(1)AI Server需求(2)通用Server需求"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02wkPbwH6c2YbzNmvwFoFVA15odytWtCBx93vW8uvQtcXspSoRFbbpV7purLqgo63Pl&id=100054201473657"
creation_time_utc: "2026-04-16T05:41:00+00:00"
fetched_at_utc: "2026-05-07T03:35:16.641470+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ4MTE3NTgzMDM2NTc4NQ=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 心得1. AI需求同步推升(1)AI Server需求(2)通用Server需求

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02wkPbwH6c2YbzNmvwFoFVA15odytWtCBx93vW8uvQtcXspSoRFbbpV7purLqgo63Pl&id=100054201473657
心得1. AI需求同步推升(1)AI Server需求(2)通用Server需求

2. 即使因為缺貨通用型Server成長力道只能出貨到成長13%，但考量過去兩年通用Server成長率只有低個位數，Agentic AI興起讓通用Server重回成長軌道，成長13%，已經比過去兩年明顯進步

3. 兩者共用的材料、零件，優先分配給AI Server，造成通用Server真實缺貨更嚴重，不是常常將tightness吃緊廣義的、買賣端的 "缺貨"，而是有確定交期的成品PO交不出來、有訂單無法排生產排程(沒排好就斷線)、真正的缺貨shortage，必須延後Server訂單交期到明年

4. 通用Server之前到目前最缺貨的零件是CPU和PCB，交期已達近一年，不知道這裡中文交期的定義和lead time是否雷同，近日新增加兩項缺貨零件(1)PMIC (2)BMC，交期延長

5. 目前交期由長到短(意味缺貨嚴重度)排序為:
(1)CPU 近52週
(2)PCB(應指特定材料) 近52週
(3)PMIC 交期從21-26週拉長至35-40週
(4)BMC 交期從11-16週拉長至21-26週

6. PMIC和BMC雖然都是成熟製程，差別是PMIC是極多品項小顆IC的統稱，BMC是少數品項量較大，寡占，出貨對通用Server組裝影響大沒錯，但整體對wafer的消耗應該是PMIC大得多，因為PMIC多品項、多用途、BCD等特定specialty製程、驗證流程，缺貨會更複雜，BMC少數料號、邏輯製程，加單、插單只要晶圓廠願意BMC缺貨相對較PMIC缺貨容易解決

7. PMIC應用廣泛，不只是通用Server/AI Server，車用也很多，不知道那家做多做少，單以整體PMIC比例，VIS應該是PMIC比重最高的foundry

8. 以前缺貨嚴重時，我們稱長短料，最缺的稱短料，如果是消費性產品、季節性產品，有節日旺季、Back to school、衝動型購買等等，一旦時間過了，需求可能就不見了，或者有一部分不見了，系統需求或長料需求就會被短料拖累，這次如果說是通用型Server，這是生產力工具、生財器具，PO/需求postpone但應該不會消失，就是推延的需求會疊加在未來需求裡面疊上去

不像消費性產品，任何理由每次廠商說PO/forecast訂單沒消失只是延後，不同，這種PO延後改交期就是取消未來新的PO，整個長時間段落的總需求是減少的，終端是消費市場的廠商這種說法偏向話術

9. ASIC/XPU最近的新聞遠超過GPU，似乎GPU很慘，長期也許威脅更多，但至少在今年，根據TrendForce資訊，2026年ASIC占整體AI server比例只有27%，大部分還是GPU，之前看到的所有AI應用、需求、租金等等正面訊息，受惠最大的還是GPU

而且，考量Meta、AWS等業者自研晶片調校耗時，有出貨遞延風險，2026年ASIC占整體AI server比例從原本的近28%還微幅下修27%左右
 
----------"TrendForce: 零組件交期拉長壓抑通用型server成長動能，預估2026年整體server出貨量年增13%

儘管2026年AI將同步推升通用型server(general server)與AI server需求，但因供應商優先分配產能給利潤較高的AI server，導致多項通用型server零組件交期明顯拉長；全年整體server出貨原有望年增近20%，因此將保持在13%左右，難以完全反映市場潛在購買力。

通用型server訂單需求穩健，原已面臨PCB、CPU供應吃緊問題，目前兩項核心零組件的交期已長達近一年。此外，近期電源IC、BMC(基板管理控制器) IC交期同樣顯著延長。

PMIC方面，由於AI server對電源密度的需求遠高於通用型server，又屬於供應商優先供貨的品項，八吋晶圓BCD(Bipolar – CMOS – DMOS)製程因此大幅偏向AI PMIC。雪上加霜的是，因Samsung計畫關閉韓國S7八吋晶圓廠，將進一步排擠通用型server使用的PMIC產能，交期因此將從21-26週延長至35-40週。

BMC同樣主要採用成熟製程，晶圓代工廠考量產能有限，傾向先滿足利潤較高、需求更急迫的AI專用晶片訂單，壓縮通用型BMC的產能配額，導致交期從過往的11-16週，拉長至21-26週。

在AI server部分，來自雲端服務供應商(CSP)的強勁需求，將支持2026年出貨量年增約28%，預料ASIC AI server的出貨成長力道將大於GPU AI server。惟考量Meta、AWS等業者自研晶片調校耗時，有出貨遞延風險，TrendForce將2026年ASIC占整體AI server比例從原本的近28%，微調成27%左右，GPU機種維持占大宗。

TrendForce指出，在全球供應鏈配置不均，以及核心半導體零組件交期瓶頸的影響下，通用型server出貨成長相對AI server受限，連帶將造成2026年整體server的出貨表現面臨增長天花板。無法在短期內被滿足的超額訂單和強勁的採購動能，預計將因等候產能、料件到位的時間差，往後延續至2027年。"

https://www.trendforce.com.tw/presscenter/news/20260415-13011.html
