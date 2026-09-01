---
post_id: "122165691302799750"
title: "Nvidia Vera Rubin/VR200 NVL72重點更新，整合我的最新產業調查與Nvidia CEO黃仁勳的2026 CES演講"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61573992511738"
final_url: "https://www.facebook.com/profile.php?id=61573992511738"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0FeB2AV2uS9eJM7Fwm7viH4KtfjReJywKxgFDMW3UVGwvzz4axFDSHwQAuoxKJqv1l&id=61573992511738"
creation_time_utc: "2026-01-06T07:36:55+00:00"
fetched_at_utc: "2026-09-01T05:14:30.289792+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTIyMTY1NjkxMzAyNzk5NzUw"
page_canonical_url: ""
---

# Nvidia Vera Rubin/VR200 NVL72重點更新，整合我的最新產業調查與Nvidia CEO黃仁勳的2026 CES演講

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0FeB2AV2uS9eJM7Fwm7viH4KtfjReJywKxgFDMW3UVGwvzz4axFDSHwQAuoxKJqv1l&id=61573992511738
Nvidia Vera Rubin/VR200 NVL72重點更新，整合我的最新產業調查與Nvidia CEO黃仁勳的2026 CES演講

1. Nvidia將AI伺服器VR200 NVL144 (die-based) 改名為VR200 NVL72 (package-based)。我的調查指出，VR200 NVL72將分為Max Q與Max P兩種power profile。
➢  黃仁勳提到了NVL72，而非先前的NVL144
➢  Max Q與Max P硬體設計相同
➢  Max Q GPU/機櫃功耗 (TGP/TDP)：約1.8/190 (kW)
➢  Max P GPU/機櫃功耗 (TGP/TDP)：約2.3/230 (kW)
➢  兩者均顯著高於GB300 NVL72的1.4/140 (kW)
➢  因應資料中心供電規格，不同power profile提升安裝彈性。此改變也意味著Nvidia開始注意到物理世界對建置AI伺服器的限制，並將其反映在產品規格上

2. VR200 NVL72 Max Q與Max P的GPU散熱設計升級。
➢  兩者均採用微通道冷板 (micro-channel cold plate；MCCP) 搭配鍍金散熱蓋 (gold-plated lid)
➢  市場高度期待GPU TGP達2.3kW後開始採用微通道蓋板 (micro-channel lid；MCL)，但MCL最快需至2H27才會量產

3. 受益於GPU、HBM與NVLink Switch規格升級，VR200 NVL72的AI訓練/推理算力約是GB300 NVL72的3.5/5倍，機櫃的供電也因此大幅提升。
➢  VR200 NVL72的power shelf升級到3*3U 110kW (6×18.3kW PSU) (vs. GB300 NVL72最普遍的8*1U 33kW (6×5.5kW PSU))
➢  VR200 NVL72 power shelf採3+1備援設計
➢  VR200 NVL72的電力進線 (power whip) 提升到100A (vs. GB300 NVL72的60A)，這對資料中心供電要求更高 (如母線 (busway) 與插接箱 (tap-off box)  等設計)。

4. VR200 NVL72的散熱設計更依賴液冷方案。
➢  Compute & NVSwitch tray均採用無風扇設計 (fanless)
➢  機櫃冷卻液流量 (TCS flow) 幾乎增加100% (vs. GB300 NVL72)，有利CDU、分歧管、水冷版與QD規格與/或數量升級
➢  機櫃風量 (Air flow) 需求則降低約80% (以CFM計) (vs. GB300 NVL72)。

5. VR200 NVL72的Compute tray首度採用midplane，落實無線設計 (cableless)。
➢  Midplane關鍵規格包括：44層 (22+22)、M9 CCL (EM896K3)、尺寸約420*60 (mm)。
➢  黃仁勳提到，受益於此設計，Compute tray的組裝時間可由2小時顯著降低到5分鐘 (vs. GB300 NVL72)。

6. 2026年Rubin CoWoS投片量約30-35萬片，預計在1Q26初開始小量試產並於2Q26末量產。VR200 NVL72的機櫃組裝量產預計在3Q26底，考慮到良率爬坡，預計2026/2H26機櫃出貨量約5,000-7,000櫃。

7. 當機櫃功耗達約200kW，54V配電會開始遭遇顯著的空間占用 (銅排/線材) 與轉換效率瓶頸，故VR200 NVL72可視為Oberon機櫃的最後一代方案；後續面對AI算力提升帶來的挑戰，將採用支援800V HVDC的次世代Kyber機櫃設計因應。
