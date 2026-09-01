---
post_id: "1595341905615843"
title: "Cerebras CS-6計畫3D Stack DRAM"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid022EGXYRWyPG2dhMsGmHGjunSrquY4uLiyGtgLTShp7FzXz5h6EEKpVVZckmdcFmsjl&id=100054201473657"
creation_time_utc: "2026-08-27T12:05:33+00:00"
fetched_at_utc: "2026-09-01T04:42:39.947356+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-dfw5-1.xx.fbcdn.net/v/t39.30808-6/788171613_1595341785615855_8440134704820308487_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=106&ccb=1-7&_nc_sid=127cfc&_nc_ohc=JjDyCIQtxiwQ7kNvwEzLQgR&_nc_oc=Adr-Dyx37OfSXCaMY2Z_8W2UMZyPdXTq2xAUjrdPgpkbIiJ0BSKM4VOQsh23Wc5GiCo&_nc_zt=23&_nc_ht=scontent-dfw5-1.xx&_nc_gid=BdOvuZ_Y-k5HS7FWvDDz6Q&_nc_ss=7e120&oh=00_AQImHsFJ7CnU-3lMQYYU9Aq6bn_W-ZvC1p-ZdGfxra4XQw&oe=6A9C124C"
feedback_id: "ZmVlZGJhY2s6MTU5NTM0MTkwNTYxNTg0Mw=="
page_canonical_url: ""
---

# Cerebras CS-6計畫3D Stack DRAM

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid022EGXYRWyPG2dhMsGmHGjunSrquY4uLiyGtgLTShp7FzXz5h6EEKpVVZckmdcFmsjl&id=100054201473657

![Cerebras CS-6計畫3D Stack DRAM](https://scontent-dfw5-1.xx.fbcdn.net/v/t39.30808-6/788171613_1595341785615855_8440134704820308487_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=106&ccb=1-7&_nc_sid=127cfc&_nc_ohc=JjDyCIQtxiwQ7kNvwEzLQgR&_nc_oc=Adr-Dyx37OfSXCaMY2Z_8W2UMZyPdXTq2xAUjrdPgpkbIiJ0BSKM4VOQsh23Wc5GiCo&_nc_zt=23&_nc_ht=scontent-dfw5-1.xx&_nc_gid=BdOvuZ_Y-k5HS7FWvDDz6Q&_nc_ss=7e120&oh=00_AQImHsFJ7CnU-3lMQYYU9Aq6bn_W-ZvC1p-ZdGfxra4XQw&oe=6A9C124C)
Cerebras CS-6計畫3D Stack DRAM

上週討論到，Cerebras並非只用SRAM，運作大參數模型的時候，SRAM太小不夠，參數權重是儲存在集群中的x86 server上的數TB等級DRAM主記憶體上，或者是旁邊一整箱的MemoryX專屬記憶體內(DRAM+Flash)，

現在Cerebras發表未來的CS-6，要將DRAM堆疊在wafer晶片上面，3D stacked DRAM，所以，Cerebras跑"大參數模型"，自始至終到未來都是SRAM+DRAM合作，不是SRAM only (除非要大量的wafer互聯使得SRAM總量足夠)

請注意，他不是堆疊SRAM而是堆疊DRAM

但這難度又更高了，目前Cerebras是用標準DRAM在集群x86 Server中或者MemoryX箱子中，未來3D stacked DRAM要和三大DRAM廠商合作
-----------------------------------------------------
"晶圓級處理器已佔據二維空間中最大的實用空間。大幅增加記憶體意味著要向上擴充，同時保留讓晶圓快速擴展的資料區域性。

2024年，我們開始將這個願景轉化為CS-6法案。透過將晶圓級 SRAM 與運算整合，透過超高頻寬連接的 3D 堆疊 DRAM 進行計算，CS-6 設計上能大幅擴充記憶體容量，同時不犧牲晶圓快速擴展的局部性。

晶圓級SRAM已經濟擴展，甚至能加速最大型模型，包括GPT-5.6 Sol及更高版本。透過緊密整合的 DRAM 系統，每個模型能在每個系統上容納更多設備，減少執行所需的基礎設施。結果是超高速推論，系統體積縮小了十萬倍，讓所有人都能享受超快的 AI 速度。"

https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026
