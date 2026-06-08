---
post_id: "27523070910611299"
title: "〔輝達自研Olympus核心架構：資料中心壓過x86與標準ARM，下一步跨進消費端〕"
page_title: ""
requested_url: "https://www.facebook.com/eric.lin77"
final_url: "https://www.facebook.com/eric.lin77"
post_url: "https://www.facebook.com/eric.lin77/posts/pfbid0Lwsxk2bRhytSd22mufrJdpVDvB1PkfyiXnwywGawSTq7EWuXdiRzPxn8QumcEFeCl"
creation_time_utc: "2026-05-28T04:14:27+00:00"
fetched_at_utc: "2026-06-08T07:06:49.596226+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-iad6-1.xx.fbcdn.net/v/t39.30808-6/710755584_27523042660614124_2455283623011515731_n.jpg?stp=dst-jpg_p843x403_tt6&_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=JOFW4D4ITCAQ7kNvwG4tvnn&_nc_oc=Adr5YJAszuucqlvLHtq6Jjlm43oGy3H-cgYOaT-BSs2zdd_HzIEG7-yrw1NBe8f4Fy8&_nc_zt=23&_nc_ht=scontent-iad6-1.xx&_nc_gid=OsWfeLeDNPgQd7gtEgyJgA&_nc_ss=7e120&oh=00_Af_SIE6K-ZJtSU1UbjSQsZ3RTA-mU1-80Gt3C1H0f0Y1SQ&oe=6A2C3531"
feedback_id: "ZmVlZGJhY2s6Mjc1MjMwNzA5MTA2MTEyOTk="
page_canonical_url: ""
---

# 〔輝達自研Olympus核心架構：資料中心壓過x86與標準ARM，下一步跨進消費端〕

原文連結: https://www.facebook.com/eric.lin77/posts/pfbid0Lwsxk2bRhytSd22mufrJdpVDvB1PkfyiXnwywGawSTq7EWuXdiRzPxn8QumcEFeCl

![〔輝達自研Olympus核心架構：資料中心壓過x86與標準ARM，下一步跨進消費端〕](https://scontent-iad6-1.xx.fbcdn.net/v/t39.30808-6/710755584_27523042660614124_2455283623011515731_n.jpg?stp=dst-jpg_p843x403_tt6&_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=JOFW4D4ITCAQ7kNvwG4tvnn&_nc_oc=Adr5YJAszuucqlvLHtq6Jjlm43oGy3H-cgYOaT-BSs2zdd_HzIEG7-yrw1NBe8f4Fy8&_nc_zt=23&_nc_ht=scontent-iad6-1.xx&_nc_gid=OsWfeLeDNPgQd7gtEgyJgA&_nc_ss=7e120&oh=00_Af_SIE6K-ZJtSU1UbjSQsZ3RTA-mU1-80Gt3C1H0f0Y1SQ&oe=6A2C3531)
〔輝達自研Olympus核心架構：資料中心壓過x86與標準ARM，下一步跨進消費端〕

Phoronix拿到工程版的輝達（Nvidia）Vera CPU，跑完一輪基準測試後給的結論很直接：這是它測過效能最強的ARM資料中心處理器，純CPU工作負載贏過超微（AMD）的EPYC Turin、英特爾（Intel）的Xeon Granite Rapids，世代效能的幾何平均提升1.63倍。

Vera是輝達第二代資料中心CPU，接替2022年的Grace。兩代最大的差別在核心：Grace用的是安謀（ARM）標準的Neoverse-V2，Vera則換成輝達全自研的Olympus。

輝達在最新一季法說會宣布Vera開出200億美元的標準CPU營收規模，市場很快把這筆生意讀成ARM架構的勝利。這個讀法搞錯了對象。Vera沒有用ARM的標準核心，它只授權了ARM的指令集，核心的管線、執行單元、快取全是輝達自己設計的88顆Olympus。Grace那一代向ARM買核心IP，Vera這一代把這塊支出省掉了。

真正的問題在Olympus這顆核心做對了什麼，讓它贏過所有用標準核心的ARM CPU，甚至比其他自研ARM核心都強。這個問題的答案，決定了未來幾年資料中心、甚至消費端CPU的競爭走向。

〔Olympus把蘋果M等級的自研核心帶進資料中心〕

Olympus的指令擷取與解碼前端做到10-wide，這個寬度目前只有蘋果（Apple）的M系列達到過。ARM自家的Neoverse不論V2還是新一代V3，前端都停在8-wide；用Neoverse核心的那一票客製CPU，AWS的Graviton 5、Google的Axion、微軟（Microsoft）的Cobalt 200，全部繼承了這個天花板。前端寬度直接決定每個週期能餵多少指令進管線，Olympus再配上能單週期評估兩個分支的神經分支預測器，單核IPC比Grace提升約1.5倍。

把核心做到蘋果M的高度，在資料中心是頭一次。資料中心自研核心這條路，蘋果不走，M系列只留給自家Mac，不進伺服器，因為資料中心處理器的核心規模需求和消費端不同，過於複雜的核心設計會限制核心規模，導致競爭力不足；高通（Qualcomm）的Oryon出自Nuvia，那支團隊原本的目標就是做資料中心核心，代號Phoenix，被高通買下後轉去做筆電晶片，到今天沒有伺服器產品，架構上也比蘋果M4保守、前端更窄，因為他們也遇到類似的問題。

輝達是第一個把蘋果M等級的自研核心真正放進資料中心的公司。Phoronix說Vera贏過所有公有雲的客製ARM方案，原因就在這裡：那些方案底下是8-wide的Neoverse，Olympus不是同一個量級。

〔四項系統設計讓Vera成為Rubin拆不開的最強協處理器〕

同等級的核心，理論上別人也造得出來。Vera真正難以被替換的地方在核心之外的四項系統設計，而這四項全是蘋果M和高通Oryon不碰的領域。

Olympus是第一個原生支援FP8的CPU核心，每顆核心有六組128-bit的SVE2引擎，能直接跑 FP8DOT2 和 FP8DOT4 指令。CPU和GPU用同一種數值格式，大型語言模型推論的預填階段，資料從CPU進到GPU不必先轉格式，省掉一整層格式轉換的延遲。

它的Spatial Multithreading把每顆核心的管線、快取、暫存器實體切開，兩條執行緒各有專屬資源，跟傳統SMT的時間切片不同，88顆核心給到176條執行緒而效能不互相干擾。

對外連接上，Vera用NVLink-C2C以1.8 TB/s的頻寬連Rubin GPU，是PCIe Gen 6的七倍；記憶體端配LPDDR5X做到1.2 TB/s，而EPYC Turin和Xeon Granite Rapids那套12通道DDR5大約只有600到700 GB/s。

這四項加起來，Olympus的角色就變了。它是Rubin GPU系統裡分不開的協處理器，效能要放進整套系統來看，不是單獨一顆CPU的規格表。蘋果M、高通Oryon都是獨立CPU，既沒有也不需要這些東西。

輝達在法說會把話講得很白：過去算的是每顆核心多少錢，AI時代算的是每塊錢買到多少token，Vera是為代理式AI設計的CPU。它的價值來自它在整套AI系統裡拆不開的位置，核心數量不是賣點。

〔Olympus壓過標準ARM與x86，連安謀親自下場的晶片也不敵〕

用Neoverse核心的那一票標準ARM CPU，是和Olympus距離拉得最開的一組。Graviton 5、Axion、Cobalt 200、AmpereOne全擠在同一個位置：賣價格、賣核心密度的通用雲端CPU。Neoverse V3比V2在典型伺服器工作負載只提升9到16%，前端還是8-wide，這條線追不上Olympus，因為它們的設計目標從來不是榨單核效能，是服務雲端原生的多租戶工作負載。

x86陣營的處境不一樣。EPYC Turin已經輸給Vera 10%，Xeon 6980P輸55%。超微的EPYC Venice、英特爾的Diamond Rapids接下來會推出，規格就算做得漂亮，它們比的還是每顆核心多少錢這條老指標。Vera不在這條指標上跟它們較量，它較量的是整套AI系統的token效率。

受影響最深的其實是ARM自己。ARM真正賺錢的是權利金，而權利金費率隨授權深度遞增，買Cortex、Neoverse核心IP的費率，遠高於只授權指令集、核心自己設計。輝達上一代Grace買的就是Neoverse核心IP，到Vera改成只授權指令集自研Olympus，等於把ARM收費最高的那層繞過去。

蘋果、高通早就走自研，輝達現在在資料中心也走上這條路，ARM最重要的幾個客戶都在繞過Cortex和Neoverse。

ARM的反制是自己下場賣晶片。2026年3月，ARM推出35年來第一顆自製處理器AGI CPU，跟Meta共同開發，最多136顆核心，想用整顆晶片的營收補回流失的IP收入。

但ARM能用的核心還是自家的Neoverse V3，前端一樣停在8-wide。Phoronix說Vera贏過所有用標準ARM核心的方案，這句話現在連ARM自己的AGI CPU都算進去。ARM賭上商業模式轉型親自做的旗艦晶片，在單核高度上甩不開自己核心的天花板，否則就無法取得核心規模的擴展，而Olympus已經成功跨過這個Arm跨不過去的難關。

〔下一代N2若換Olympus，自研核心將複製到消費端〕

Olympus的下一步已經有跡可循。輝達和聯發科（MediaTek）的第一代消費晶片N1X在2026年上市，用的是ARM標準的Cortex核心，走的是GB10那條路線，不是Olympus。但業界已經傳出，2027年第三季接棒的N2可能改用Olympus衍生的自研核心，輝達也揭露過它有一條自研ARM CPU的長期藍圖，Vera之後接的是Rosa。

如果N2真的採用Olympus核心或繼任架構，自研核心這條路就會從資料中心複製到消費端。它正面對上的就會是英特爾和超微的x86消費CPU，在單核效能的標竿上和蘋果M並列，通吃從資料中心到消費端的所有平台。

而ARM在消費端又少掉一個用Cortex核心IP的客戶。

市場以為Vera那筆200億美元證明了ARM贏過x86，實際上Olympus證明的是自研核心對授權核心的優勢，而ARM自己，反而被自研核心給狠狠的鞭打了。

#輝達Vera,#Olympus核心,#自研CPU,#ARM核心IP,#Neoverse,#蘋果M,#x86競爭,#代理式AI
