---
post_id: "1464601455356556"
title: "延續昨天上篇，簡單講，上篇寫的Google TurboQuant對\"目前的\"、\"大規模應用的\" Inference KV Cache記憶體(HBM/DRAM/NAND)"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02XHzaSXH9ahZegRxysAe4bRnfB8rdkFCgxMRiEK1JmKobkgu3FnP4sP4FQWnSg5a8l&id=100054201473657"
creation_time_utc: "2026-03-26T03:44:48+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-6/659078217_1464601402023228_6909615849932731693_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=107&ccb=1-7&_nc_sid=127cfc&_nc_ohc=BqXCQcsZg4YQ7kNvwE1AMWX&_nc_oc=AdpTavS-4yY4q-noJadqpZZi9G9QZe2qL8vvW4mpMk7gq90PGU4nSk0-9KQSqw6OfR8&_nc_zt=23&_nc_ht=scontent-lax3-2.xx&_nc_gid=vNFWwLFUodTv1HFGTkfemg&_nc_ss=78100&oh=00_Af9qjeni9FGgcziXtK85XBvJP4Wfy0cHb3vmzwEHhdglVA&oe=6A3878BF"
feedback_id: "ZmVlZGJhY2s6MTQ2NDYwMTQ1NTM1NjU1Ng=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 延續昨天上篇，簡單講，上篇寫的Google TurboQuant對"目前的"、"大規模應用的" Inference KV Cache記憶體(HBM/DRAM/NAND)

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02XHzaSXH9ahZegRxysAe4bRnfB8rdkFCgxMRiEK1JmKobkgu3FnP4sP4FQWnSg5a8l&id=100054201473657

![延續昨天上篇，簡單講，上篇寫的Google TurboQuant對"目前的"、"大規模應用的" Inference KV Cache記憶體(HBM/DRAM/NAND)](https://scontent-lax3-2.xx.fbcdn.net/v/t39.30808-6/659078217_1464601402023228_6909615849932731693_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=107&ccb=1-7&_nc_sid=127cfc&_nc_ohc=BqXCQcsZg4YQ7kNvwE1AMWX&_nc_oc=AdpTavS-4yY4q-noJadqpZZi9G9QZe2qL8vvW4mpMk7gq90PGU4nSk0-9KQSqw6OfR8&_nc_zt=23&_nc_ht=scontent-lax3-2.xx&_nc_gid=vNFWwLFUodTv1HFGTkfemg&_nc_ss=78100&oh=00_Af9qjeni9FGgcziXtK85XBvJP4Wfy0cHb3vmzwEHhdglVA&oe=6A3878BF)
延續昨天上篇，簡單講，上篇寫的Google TurboQuant對"目前的"、"大規模應用的" Inference KV Cache記憶體(HBM/DRAM/NAND)

沒有影響

因為前沿模型和研究者大家早就用了，2位元KIVI KV Cache量化和壓縮論文開源程式都已經兩年了，還在繼續發展，TurboQuant 2.5/3.5位元壓縮6倍不特別

大家早就在用了，所以沒有影響

有影響的是評分(模型智慧)比以前高，大家用了KV Cache量化智慧降低，TuboQuant用了智慧不會降低，但因為前沿模型沒有公布內部使用的KV Cache量化細節和效果，不知道誰高誰低

重點是Inference智慧提升(無損)，不是容量降低、算力降低
