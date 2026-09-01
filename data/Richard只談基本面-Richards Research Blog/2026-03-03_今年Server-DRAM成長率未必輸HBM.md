---
post_id: "1446918977124804"
title: "今年Server DRAM成長率未必輸HBM"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02JTBQH6M6G8g1CB3T4bXBNbVc7xTSW73exCuaZGD8NRa3C7g3Q3sgY2JWzpQkbDhNl&id=100054201473657"
creation_time_utc: "2026-03-03T15:36:22+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ0NjkxODk3NzEyNDgwNA=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 今年Server DRAM成長率未必輸HBM

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02JTBQH6M6G8g1CB3T4bXBNbVc7xTSW73exCuaZGD8NRa3C7g3Q3sgY2JWzpQkbDhNl&id=100054201473657
今年Server DRAM成長率未必輸HBM

因為HBM是DRAM明星，大部分文章/報告/報導談到GPU/XPU使用的HBM規格和容量提升，卻很少提到這些GPU所搭配的DRAM(CPU host DRAM)容量變化，可能讓人以為AI讓整體DRAM需求增量主因 "只有" HBM，忽略host DRAM是第二條需求支柱，今年誰影響較大還很難說

1. AI GPU/XPU/Server數量增加數字大家很清楚

2. GPU/XPU搭配HBM的規格和容量提升大家很清楚，如

1H25 Blackwell HBM3e 192GB
2H25 Blackwell Ultra HBM3e 288GB，容量提升
2H26 Rubin 新型HBM4但容量維持288GB

3. 但GPU計算板上CPU host DRAM的容量提升，很少報告拿出來比較，容易忽略

GB200 Blackwell x 2 + Grace 480GB DRAM，平均一顆GPU 240GB

GB300 Blackwell Ultra x 2 + Grace 480GB DRAM，平均一顆GPU 240GB DRAM沒有變

Rubin x 2 + Vera 1.5TB，是Grace的 "三倍"，平均一顆GPU 750GB DRAM，一樣變三倍

這是因為Grace是Hopper時代的產品，第一款用在GH200上面，1:1一顆GPU 141GB HBM+480GB DRAM已經不小，以及Grace x 2=Superchip 480GBx2近1TB一台通用Server稍小但還OK，當時480GB LPDDR5X已經不小，但接著兩年Blackwell時代，依然用Grace同一顆舊設計DRAM容量就太小

Vera CPU一次比Grace CPU DRAM容量增加到三倍，480GB到1.5TB，CPU:GPU配比一樣1:2

從GB300到VR NVL72，content HBM容量沒變、DRAM容量卻變三倍

各大報告是不是有點太忽略今年VR系列對host DRAM的content提升了?

當然，Late 2027，Vera的DRAM不變，Rubin Ultra的HBM容量大增，所以，今年DRAM容量大增，明年HBM容量大增，交互替換

所以2026年Server DDR5/DDR5X DRAM需求大增，原因為:

(1)AI Agent中有CPU貢獻的部分(順序、條件、邏輯)、Code LLM後訓練中有compiling用CPU、CoT/Test Time compute思考型模型有CPU貢獻的部分(CPU用DRAM)，資料中心通用型Server(CPU+DRAM) cluster需求增加

(2)AI需求成長下帶動IT基本需求基礎設施支援，讓CPU通用型Server(DRAM)需求提升

(3)Vera搭配的host DRAM比Grace成長為三倍，本文主要談這部分的需求被忽略，平均每顆GPU配比LPDDR5X DRAM從240GB增加到750GB，成長為三倍

(4)推論KV Cache卸載順序HBM下一段就是DRAM，DRAM宜大不宜小

(5)以上趨勢下，Nvidia HGX或AMD OCP UBB/OAM的Server，在CPU主機板這塊的DRAM容量只會更大不會變小，2TB to 4TB......平均一顆GPU搭配2TB/8=250GB~4TB/8=500GB DRAM

(6)這點比較小，BlueField 3/4 DPU用量增加，Server主機上DPU和ICMS controller用DPU都是，NV DPU主要部分就是一顆Grace CPU + NIC，用DRAM，未來一年內CXL 3.1應有一席之地，也很可能增加DRAM Pool，這也是用DRAM不是HBM

以上六點中提到CPU的部分就是搭配DDR DRAM，不是HBM

所以，HBM和DRAM前段顆粒生產設備產能共用，因為TSV佔面積和堆疊良率下降，每單位容量GB使用的wafer產能是DDR DRAM的三倍，加上GPU/XPU數量成長，讓HBM是整體DRAM需求成長主力沒錯，但這些已經廣為人知，以上六點的Server DDR5 DRAM本身的需求成長，有些可能並未被納入想像中
