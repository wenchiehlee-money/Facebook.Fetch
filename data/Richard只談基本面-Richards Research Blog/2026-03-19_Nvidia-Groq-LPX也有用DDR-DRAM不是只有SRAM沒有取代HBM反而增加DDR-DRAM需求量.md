---
post_id: "1458976512585717"
title: "Nvidia Groq LPX也有用DDR DRAM不是只有SRAM，沒有取代HBM反而增加DDR DRAM需求量"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0275fFXBW7qW79xTHKQyrRsmgPpR1wDdiPKvoiyTfK6E7E3PK9NjhzmHAYPU3oJJa3l&id=100054201473657"
creation_time_utc: "2026-03-19T16:39:22+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ1ODk3NjUxMjU4NTcxNw=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# Nvidia Groq LPX也有用DDR DRAM不是只有SRAM，沒有取代HBM反而增加DDR DRAM需求量

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0275fFXBW7qW79xTHKQyrRsmgPpR1wDdiPKvoiyTfK6E7E3PK9NjhzmHAYPU3oJJa3l&id=100054201473657
Nvidia Groq LPX也有用DDR DRAM不是只有SRAM，沒有取代HBM反而增加DDR DRAM需求量

GTC焦點之一的Groq LPU和LPX Rack一般被強調使用SRAM，沒有特別講DRAM可能有人誤以為不需要DRAM

1. LPU用SRAM但並非取代HBM/DRAM，因為他是分擔、加速Rubin GPU一部分工作(inference decode中的FFN/MoE不含Attention)，並非取代用HBM的Rubin

2. 8顆LPU組成一台LPX Compute Tray(server node)，這一台並非只有LPU，還有一顆CPU，只要是CPU就一定需要DRAM，然後32台LPX Compute Tray組成一台共有256顆LPU的LPX機櫃

對照一台Nvidia HGX NVL8 Server，CPU是x86(未來可用Vera)，裝配1T~2TB~4TB DRAM，UBB上另有裝配HBM的8顆Hopper/Blackwell GPU當加速器Accelerator，同樣的，一台Groq 3 LPX Compute Tray上面有一顆CPU(可能是x86 CPU)，上面有RDIMM DDR DRAM，和8顆LPU加速器Accelerator，LPU/SRAM和Hopper/HBM角色一樣是AI加速器和VRAM的角色，也一樣另外有一顆x86 CPU+DRAM跑作業系統和主程式

3. LPX Compute Tray上面DRAM容量是多少呢? 從兩個線索推測是384GB DDR5 DRAM

(1)Micron法說簡報投影片第11頁最後一點說一台Nvidia Groq 3 LPX機櫃上有Up to 12TB DDR5 DRAM，12TB / 32 Trays = 375左右，因為12TB是取整數加上1000和1024的計算區別會有小差距

(2)Nvidia公布的LPX Compute Tray照片上有一顆Host CPU，有CPU就一定要搭配DRAM，再看照片似乎有4條或6條RDIMM，概算可能是64GB x 6 = 384GB 或96GB x 4 = 384GB

4. 用那種CPU呢? 因為Micron簡報說DDR5那就是x86了，因為Nvidia自己的Grace和Vera是LPDDR5X不是DDR5，而且容量數目也不對，Grace是480/512GB、Vera是1.5TB，都太大了超過375GB左右的範圍

5. LPX Compute Tray上面還有一片BlueField 4 DPU，上面也有on-board 128GB LPDDR5X沒有算在384GB以內，算進去會更多

6. 結論就是LPU on-chip SRAM沒有取代Rubin HBM，而LPX Tray/Rack增加了總DDR DRAM用量，總體是增加DRAM需求
