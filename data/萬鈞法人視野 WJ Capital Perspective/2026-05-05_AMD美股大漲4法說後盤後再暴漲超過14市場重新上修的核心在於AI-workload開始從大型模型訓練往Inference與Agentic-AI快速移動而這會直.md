---
post_id: "122199025940936895"
title: "AMD美股大漲4%，法說後，盤後再暴漲超過14%，市場重新上修的核心，在於AI workload開始從大型模型訓練，往Inference與Agentic AI快速移動，而這會直接推升CPU、Memory與Storage（美光與閃迪盤後也又漲4%）在AI資料中心中的重要性。"
page_title: "萬鈞法人視野 WJ Capital Perspective"
requested_url: "https://www.facebook.com/profile.php?id=61578106860333"
final_url: "https://www.facebook.com/people/%E8%90%AC%E9%88%9E%E6%B3%95%E4%BA%BA%E8%A6%96%E9%87%8E-WJ-Capital-Perspective/61578106860333/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0U7XdM2iegoPJkM1ZsrZsu7wTt2vZUhzpQ5pC84htqv2wUfneL2tw8gtX9sL9qeEWl&id=61578106860333"
creation_time_utc: "2026-05-05T23:28:26+00:00"
fetched_at_utc: "2026-05-31T10:38:55.055470+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0U7XdM2iegoPJkM1ZsrZsu7wTt2vZUhzpQ5pC84htqv2wUfneL2tw8gtX9sL9qeEWl&id=61578106860333"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTIyMTk5MDI1OTQwOTM2ODk1"
page_canonical_url: "https://www.facebook.com/people/%E8%90%AC%E9%88%9E%E6%B3%95%E4%BA%BA%E8%A6%96%E9%87%8E-WJ-Capital-Perspective/61578106860333/"
---

# AMD美股大漲4%，法說後，盤後再暴漲超過14%，市場重新上修的核心，在於AI workload開始從大型模型訓練，往Inference與Agentic AI快速移動，而這會直接推升CPU、Memory與Storage（美光與閃迪盤後也又漲4%）在AI資料中心中的重要性。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0U7XdM2iegoPJkM1ZsrZsu7wTt2vZUhzpQ5pC84htqv2wUfneL2tw8gtX9sL9qeEWl&id=61578106860333
AMD美股大漲4%，法說後，盤後再暴漲超過14%，市場重新上修的核心，在於AI workload開始從大型模型訓練，往Inference與Agentic AI快速移動，而這會直接推升CPU、Memory與Storage（美光與閃迪盤後也又漲4%）在AI資料中心中的重要性。

AMD Q1營收102.5億美元、年增38%，高於市場預估的98.9億美元；Non-GAAP EPS 1.37美元、年增43%，同樣優於市場預期。真正關鍵的是Data Center營收直接衝到58億美元、年增57%，占整體營收比重超過56%，正式成為AMD最大成長來源，而Q2營收指引直接給到112億美元，上下浮動3億美元，遠高於市場原本預估的105億美元。市場原本擔心AI資本支出在大型模型訓練高峰後可能開始放緩，但這份財報看到的方向，反而是Inference需求正在帶動另一輪AI基礎設施擴張。

Lisa Su這次法說反覆提到Inference與Agentic AI，背後代表的是AI系統開始從「單次推理」進入「長時間持續運行」。過去的大模型訓練，核心瓶頸主要集中在GPU算力與HBM頻寬，但Agentic AI真正進入企業部署後，整個系統需要長時間在線、多Agent協作、持續進行工具調用、Context切換、記憶體讀寫與任務編排，系統延遲來源開始大量往CPU調度、Memory hierarchy、Storage latency與Network throughput移動。

很多人現在談AI伺服器，還停留在GPU數量、HBM容量與NVLink頻寬，但大型Agent系統真正運行後，大量資源消耗其實發生在Sandbox isolation、Task orchestration、File I/O、Memory management與Multi-thread scheduling，而這些全部高度依賴CPU。GPU負責模型推理，但CPU開始重新成為整個AI系統的管理中樞，這也是為什麼最近幾季EPYC需求重新加速成長。

AMD這次同步宣布，Meta規劃部署最高6GW AMD Instinct GPU，首批1GW直接採用客製化MI450，同時Meta也成為第六代EPYC Venice與Verano首批客戶；AWS、Google Cloud、Azure與騰訊雲則全面擴大第五代EPYC實例；Samsung進一步與AMD合作HBM4與下一代DRAM方案。這些訊號背後，其實都在反映AI資料中心的競爭開始從單純GPU堆疊，逐漸往系統級架構升級演進。

TrendForce已經開始看到CPU:GPU配比從過去4:1、8:1，逐漸往1:1靠攏，部分高協作型Agent workload甚至可能出現單GPU搭配多CPU架構。摩根士丹利則預估，2030年前Agentic AI可能新增325億至600億美元CPU市場空間，代表AI伺服器未來幾年的成長邏輯，開始從單純加速器競賽，擴散到整體系統吞吐量競賽。

這也是3443創意最近繼續被各大外資調升的重要背景。市場不斷上修Google CPU相關專案的長期價值。法人圈目前估，今年Google CPU今年出貨量約150萬顆，明年有機會直接跳升到600萬顆，代表創意未來幾年的成長動能，開始從AI ASIC延伸到大型雲端CPU平台。AI產業過去兩年市場焦點幾乎全部集中在GPU算力，但接下來幾年，真正影響AI系統效率與資本支出方向的關鍵，會逐漸往CPU scheduling、Memory bandwidth、Storage latency、Network fabric、Power delivery與Thermal management移動，AI供應鏈的獲利結構，也會開始從單一GPU，往整個系統架構全面擴散。
