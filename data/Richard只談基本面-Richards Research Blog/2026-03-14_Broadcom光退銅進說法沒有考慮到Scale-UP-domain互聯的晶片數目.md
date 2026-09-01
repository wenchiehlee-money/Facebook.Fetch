---
post_id: "1455170362966332"
title: "Broadcom光退銅進說法沒有考慮到Scale UP domain互聯的晶片數目"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0Ejvog6JZidYzGsVT55y34JQ7C3VqokSLfkkbtFym7bmVDZ1DQMbzpf9wxL8uXvL6l&id=100054201473657"
creation_time_utc: "2026-03-14T18:24:20+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/652891881_1455170346299667_1903382999553264745_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=104&ccb=1-7&_nc_sid=833d8c&_nc_ohc=9B9muLf6xAgQ7kNvwEfW5K2&_nc_oc=Ado2pdM3CVaKtXzudtZW-shlSLxPO-tc6UdI2ytaEsGcS6GGe3C7bGK33gpxEY5rs5M&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=mJmKlEJrEooTpWj-b8BMpg&_nc_ss=78100&oh=00_Af-Al2uE3JzHFfHqhdMNYo0LiIeIKLNbYJD1tADmJdR_MA&oe=6A387B58"
feedback_id: "ZmVlZGJhY2s6MTQ1NTE3MDM2Mjk2NjMzMg=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# Broadcom光退銅進說法沒有考慮到Scale UP domain互聯的晶片數目

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0Ejvog6JZidYzGsVT55y34JQ7C3VqokSLfkkbtFym7bmVDZ1DQMbzpf9wxL8uXvL6l&id=100054201473657

![Broadcom光退銅進說法沒有考慮到Scale UP domain互聯的晶片數目](https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/652891881_1455170346299667_1903382999553264745_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=104&ccb=1-7&_nc_sid=833d8c&_nc_ohc=9B9muLf6xAgQ7kNvwEfW5K2&_nc_oc=Ado2pdM3CVaKtXzudtZW-shlSLxPO-tc6UdI2ytaEsGcS6GGe3C7bGK33gpxEY5rs5M&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=mJmKlEJrEooTpWj-b8BMpg&_nc_ss=78100&oh=00_Af-Al2uE3JzHFfHqhdMNYo0LiIeIKLNbYJD1tADmJdR_MA&oe=6A387B58)
Broadcom光退銅進說法沒有考慮到Scale UP domain互聯的晶片數目

微軟CEO說他們接收了Vera Rubin NVL72做驗證測試(工程機送Beta site測試?) Jim Keller再度嘲諷只有72顆晶片太小了，Tenstorrent正在用600顆晶片互聯如同一台電腦(scale UP)，很快會擴增到1000~2000顆晶片

他講得當然是scale UP，才能共享算力、共享記憶體、高速互聯如同操作一台超大電腦，如果是scale OUT早就可互聯超過十萬顆晶片了

Scale UP邏輯拓撲互聯是算力互通疊加、VRAM記憶體疊加共享、互聯速度遠高於Scale OUT數倍，但實體上未必只限定在一個機櫃中，NV、Meta、AWS有兩個機櫃，Google一堆機櫃間OCS互聯成9000多Scale UP domain，但是NV Kyber 576一個機櫃只能塞入144顆Rubin Ultra GPU(576 dies)，不論這是算NVL144或早期說的NVL576，"數量上"都不如其他架構(UALink 1,024 to Google TPU 9000)，當然單顆晶片NV最強而Google OCS傳輸速度嚴格講遠不如Cube內ICI電互聯速度，但144或576未來還是太小，再擴大在實體上必須要跨機櫃，兩個機櫃以上，距離遠銅線就不適合，我覺得NV勢必要盡快研究在NVLink Scale UP domain中使用光互聯，才能擴大144/576，之前有報告說Vera Rubin Ultra Kyber 144/576中一個機櫃中四大箱blade server透過背板PCB和NVLink Switch機箱用電互聯但四大箱彼此之間用CPO光互聯，或者是下一代Feynman才用到Scale UP CPO？GTC看看會不會公布

Broadcom帶來的光退銅進爭議是在Scale UP，2028年之前用銅，Scale OUT應無爭議，但問題是

Broadcom你說的Scale UP用銅就好，有沒有說要聯幾顆XPU？2028年大家聯到一兩千顆XPU放的下一兩台機櫃嗎？更遠的距離不用光嗎？

如果2028年Broadcom的XPU和SUE/ESUN Scale UP只有一兩個機櫃容納的晶片數目，如何和別人競爭？
