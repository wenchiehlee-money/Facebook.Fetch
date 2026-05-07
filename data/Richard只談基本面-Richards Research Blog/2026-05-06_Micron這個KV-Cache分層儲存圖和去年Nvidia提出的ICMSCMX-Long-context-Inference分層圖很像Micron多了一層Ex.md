---
post_id: "1498601811956520"
title: "Micron這個KV Cache分層儲存圖和去年Nvidia提出的ICMS/CMX Long context Inference分層圖很像，Micron多了一層Extension Memory，雖然Micron沒有明講CXL，我們之前用Nivida G1~G4層修改提出的G1.5 or G2.5 CXL memory大概是這個概念"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02iiYiyrDWd2CxFNEfAsSxsS8CnKh7sTyTyrUyi9S1XUKHn7SNzThMyb2DBLCaiifNl&id=100054201473657"
creation_time_utc: "2026-05-06T13:22:11+00:00"
fetched_at_utc: "2026-05-07T04:08:43.685141+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02iiYiyrDWd2CxFNEfAsSxsS8CnKh7sTyTyrUyi9S1XUKHn7SNzThMyb2DBLCaiifNl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ5ODYwMTgxMTk1NjUyMA=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# Micron這個KV Cache分層儲存圖和去年Nvidia提出的ICMS/CMX Long context Inference分層圖很像，Micron多了一層Extension Memory，雖然Micron沒有明講CXL，我們之前用Nivida G1~G4層修改提出的G1.5 or G2.5 CXL memory大概是這個概念

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02iiYiyrDWd2CxFNEfAsSxsS8CnKh7sTyTyrUyi9S1XUKHn7SNzThMyb2DBLCaiifNl&id=100054201473657
Micron這個KV Cache分層儲存圖和去年Nvidia提出的ICMS/CMX Long context Inference分層圖很像，Micron多了一層Extension Memory，雖然Micron沒有明講CXL，我們之前用Nivida G1~G4層修改提出的G1.5 or G2.5 CXL memory大概是這個概念

Context Windows每年增加30倍，儲存在SSD中

我們之前提到KV cache的特點是 "可存可算"、"把memory/Storage和GPU算力打成一片互通有無"，"多存則少算、少存則多算"，Micron這次訪談中提到不少這類概念，Memory和GPU因為KV Cache從兩件事變成一件事，兩個需求變成一個大片需求，請見 "KV Cache讓HBM/DRAM、SSD/NAND、HDD、GPU四個產業需求互通"一文，連結在留言

GPU=Memory算力和存力可以互相替代，不是傳統CPU+DRAM/GPU+VRAM的支援、配合，是直接替代

Micron也提到，KV cache因為太大，HBM/DRAM不夠必須用SSD來儲存，意即我們之前說的，KV cache需求暴增最大受惠者是NAND/SSD

----------"Werner说：“训练用内存来学习，然后遗忘，最终输出一个模型。但推理用内存来记忆。”

推理过程分为两个阶段：预填充（prefill）和解码（decode）。在解码阶段，模型需要不断调用此前的计算结果——也就是所谓的KV缓存（KV Cache）——来生成更准确的答案。

问题在于：如果内存不够存下这些历史状态，模型就必须从头重新计算。Werner解释了这意味着什么：

每一轮重新计算，所需的算力相当于此前所有轮次的总和。也就是说，算力需求是指数级增长的。而如果你能存下上一轮的状态，每一轮只需要线性地多做一步。

换句话说，内存不足会让GPU的算力利用率急剧下降。反过来，Werner指出：“如果你能提供足够快、足够大的内存，理论上可以从GPU中榨取出平方倍的算力。”

推动KV缓存需求膨胀的因素有三个：上下文窗口越来越长、模型参数量越来越大、同时并发使用AI的用户越来越多。Werner透露，目前上下文长度正以每年30倍的速度增长。

内存层级：从HBM到SSD，一条完整的“存储链”
Werner详细梳理了AI数据中心的内存层级结构，从最靠近GPU的高带宽内存（HBM）到最远端的海量SSD，构成一条完整的“存储链”。

第一层：HBM，紧贴GPU，典型容量在10至100GB之间，速度最快，但容量有限。

第二层：主内存（Main Memory），连接至CPU，容量通常是HBM的4至20倍，但速度更慢、距离更远。以英伟达Blackwell系统为例，主内存连接至Grace CPU。

第三层：扩展内存（Expansion Memory），通过光纤连接独立内存模块，目前尚未大规模量产部署，但已是业界关注的方向。

第四层：上下文内存存储（Context Memory Storage），即用SSD来存储KV缓存。Werner指出，英伟达CEO黄仁勋今年已公开谈及这一方向。与HBM相比，SSD的延迟更高、带宽更低，但容量可达HBM的1000倍。

第五层：数据湖，数据中心底层的海量SSD存储，以EB（艾字节）计。

Werner表示，目前整个层级从上到下都处于供不应求的状态：“只要我们发布产品，他们就会消耗掉。只要我们提升容量和性能，他们就会找到方法部署。”
......
Werner表示，目前整个行业都受制于洁净室空间，这一状况短期内难以改变。
......
我们已经无法跟上需求了，其他所有人也一样——英特尔、英伟达、台积电都在说，我们已经满负荷了。晶圆厂不是说长就能长出来的。

市场还没看懂这件事

对于市场的担忧，Werner有不同看法。

他认为，市场目前看到云服务商（CSP）资本开支大幅增加，就开始担心这是否可持续。但他的判断是：“这些企业正在经历一场巨大的革命，其潜力仍然超出大多数人的想象。”

Werner还指出，AI的应用场景远未饱和。训练时代已经过去，推理时代刚刚开始，而Agentic AI（智能体AI）和物理AI（Physical AI）甚至还没有真正大规模落地。“我真的相信，我们只是刚刚触及AI将要带来的变革的表面。”
......
此外，不只是上下文本身——模型规模（即参数量）也在持续增长，这对模型智能至关重要；每次迭代的token数量在增长；同时，每块GPU上并发运行的Agentic AI用户数量也在增长。所有这些因素叠加，使得每块GPU所需的KV缓存量急剧攀升。如果能成功提供足够的内存和存储，理论上可以从GPU中榨取出远超传统模式——即平方级别——的计算效能。
......
第十章：AI为何正在引发存储短缺
Jay： 我想接着问一个让我很感兴趣的问题。靠近GPU的存储器、尽可能大的带宽，这部分需求我很好理解。但听起来存储方面也面临大面积短缺，不只是在计算侧或GPU托盘上，而是覆盖整个数据中心生态系统。这是为什么？

Jeremy： AI对存储的需求来自几个方面。首先，AI本身会生成大量数据。用过Grok或者刷过X（推特）的人都知道，AI图像生成的速度之快，远超任何一个最熟练的表情包制作者，而所有这些内容都会被存下来。我常说，大多数人都是数字囤积狂——我们不太舍得删数据。

不仅如此，AI模型正在让我们每个人——包括那些以前缺乏技术能力来实现创意的人——都能把想法变为现实，至少是数字现实。这是一场面向所有人的创意革命，我们都在创造更多数据。企业也同样如此，AI让他们能够更好地创建和利用自己的数据。而要真正发挥AI的价值，最关键的是把所有数据都存放在可以被快速访问的地方。

AI不只是创造数据，它还要访问数据来提供洞察、解决问题、给出更好的答案。这就带出了存储领域的一个概念——"数据预热"（warming）。我们通常把数据分为"热数据"和"冷数据"。热数据是指近期很可能被访问的数据；冷数据则是那些基本上没人会查的东西，比如十年前的税单。但有了AI，你一提问，它就要翻遍所有数据来找答案——那些曾经的冷数据，正在变暖。一切都在升温。数据越热，就需要越快的存储，因为访问频率大幅增加。

此外，还有另一个令人兴奋的未来增长点：由于没有足够的内存来存储所有KV缓存，数据中心SSD将迎来巨大的增量需求，用于存储查询调度和多轮对话工作流——如果用现有架构来处理，就不得不反复经历我前面说的那种重新计算的循环。
......"

https://www.itiger.com/hans/news/2633977471


---
[📌 新增貼文至TAIEX.TW比對](https://github.com/wenchiehlee-money/TAIEX.TW/issues/new?template=earnings_tag.yml&title=2026%20%20%E8%B2%A1%E5%A0%B1%E6%A8%99%E8%A8%98&symbol=2026&file_path=data%2FRichard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards%20Research%20Blog%2F2026-05-06_Micron%E9%80%99%E5%80%8BKV-Cache%E5%88%86%E5%B1%A4%E5%84%B2%E5%AD%98%E5%9C%96%E5%92%8C%E5%8E%BB%E5%B9%B4Nvidia%E6%8F%90%E5%87%BA%E7%9A%84ICMSCMX-Long-context-Inference%E5%88%86%E5%B1%A4%E5%9C%96%E5%BE%88%E5%83%8FMicron%E5%A4%9A%E4%BA%86%E4%B8%80%E5%B1%A4Ex.md&period=)
