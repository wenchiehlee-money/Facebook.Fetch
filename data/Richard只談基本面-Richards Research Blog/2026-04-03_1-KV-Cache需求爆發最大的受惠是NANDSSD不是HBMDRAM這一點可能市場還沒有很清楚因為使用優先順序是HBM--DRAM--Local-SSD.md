---
post_id: "1471511574665544"
title: "1. KV Cache需求爆發最大的受惠是NAND/SSD不是HBM/DRAM，這一點可能市場還沒有很清楚，因為使用優先順序是HBM > DRAM > Local SSD > 外部SSD，認為這也是受惠順序這樣想很自然"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0mfgTJenWoxXThzEdV4mKhctYNKjZpX7pL9U85kZQCKitufwJ2doMDF84sVGVUdhDl&id=100054201473657"
creation_time_utc: "2026-04-03T16:34:45+00:00"
fetched_at_utc: "2026-05-07T03:35:16.641470+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0mfgTJenWoxXThzEdV4mKhctYNKjZpX7pL9U85kZQCKitufwJ2doMDF84sVGVUdhDl&id=100054201473657"
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ3MTUxMTU3NDY2NTU0NA=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 1. KV Cache需求爆發最大的受惠是NAND/SSD不是HBM/DRAM，這一點可能市場還沒有很清楚，因為使用優先順序是HBM > DRAM > Local SSD > 外部SSD，認為這也是受惠順序這樣想很自然

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0mfgTJenWoxXThzEdV4mKhctYNKjZpX7pL9U85kZQCKitufwJ2doMDF84sVGVUdhDl&id=100054201473657
1. KV Cache需求爆發最大的受惠是NAND/SSD不是HBM/DRAM，這一點可能市場還沒有很清楚，因為使用優先順序是HBM > DRAM > Local SSD > 外部SSD，認為這也是受惠順序這樣想很自然

但是因為HBM、DRAM很快就額滿，容量也太小，真正能有效果的卸載KV Cache的是SSD，就是說，HBM容量在GPU/XPU兩三年前設計時就決定、出貨時就裝好，DRAM也類似就是一台Compute tray Grace 480GB x 2 or Vera 1.5TB x 2 DRAM是Nvidia出貨就固定的不能加，而且很快就用滿，無法卸載多少，也不適合保存(KV Cache可能要保存數天以上)

但SSD一台可以擴大到上百TB，還有Nvidia的外接式Bluefield DPU SSD Rack (ICMS or CMX平台)，大倍數增加SSD容量，優先是HBM和DRAM在前，但很快滿掉要靠SSD才能解決KV Cache爆發問題

HBM和DRAM是常數SSD才是KV Cache的因變數(還有上次講過SSD內部做DRAM cache的小容量DRAM)

我想這也是1Q26~2Q26 NAND合約價漲幅大幅度上修2Q26漲幅超過DRAM的主要原因

想想Nvidia真是厲害，去年就提出KV Cache是嚴重問題還專門推出Long context ICMS SSD Rack平台，計畫掌握商機，多賣Grace/Vera CPU和Bluefiled DPU

2. LPDDR將取代DDR5成為Server DRAM的主流

3. 我覺得CXL 3.0標準成熟，可以加大一台Server DRAM容量為數倍，也可以獨立一個DRAM Server/Rack，類似Storage Server(HDD or SSD)，應有機會

4. DRAM原廠庫存今年降到安全水位以下，不到4週

----------"CFM数据显示，AI服务器对存储的需求呈几何级增长：通用服务器通常配置DDR5 512GB-1TB、SSD约4TB，而AI服务器DDR5配置达1.5TB-4TB，eSSD从4/8TB跃升至8/16TB，还需搭载HBM3E/HBM4。2026年，AI服务器在整体服务器出货中占比将突破20%，部分公司甚至达到25%-30%。这种爆发直接推高了存储配置需求——2026年服务器DRAM应用占比将超过50%，需求增速超过40%；Server NAND需求同比增长63%，HBM增长35%，SOCAMM更是暴涨150%。

随着Intel Granite Rapids (GNR)、AMD Turin等平台在2026年扩大应用，DDR5-6400成为标配，并向MRDIMM-8800演进。到2027年，Diamond Rapids和Venice平台将推动DDR5-8000及16通道配置落地，PCIe 6.0 SSD的渗透率也将加速提升。

更值得关注的是LPDDR的"出圈"。邰炜指出，从NVIDIA Blackwell到Rubin架构，SOCAMM（SoC Attached Memory Module）系列快速发展，在高耗能场景中相较RDIMM展现出明显优势。LPDDR based MRDIMM以及加速卡的大量应用，意味着"LPDDR不再是手机和超极本的专属，手机、服务器、汽车都会要抢占LPDDR的产能。"

KV Cache overflow：HBM不堪重负，eSSD成最大赢家

AI推理环节正在催生存储架构的深层变革。邰炜详细解释了KV Cache（键值缓存）机制对大模型推理的重要性——为避免重复计算、减少推理时间，每一层、每个token的Key Value结果都需要存储。但随着大模型从短上下文向长上下文演进，加上高并发推理需求，KV Cache占用空间随token数量和并发请求量线性暴涨。

PPT中的数据直观展示了这一"恐怖"增长：单请求下，上下文从4K token增至128K token，KV Cache存储空间直接增长32倍至64GB；若遇到100个并发请求，需求将达到TB级别。"这个量级的需求，HBM根本承载不了，"邰炜指出，"所以KV Cache的需求开始大规模向NVMe SSD转移。"

这一转移彻底改变了NAND应用格局。CFM预测，2026年AI推理将驱动eSSD成为NAND最大的应用市场，占比达37%，超过Mobile（27%）和PC（12%）。同时，由于NL HDD产能缺口，QLC替代需求不断上升。针对AI推理优化的企业级SSD，其价值标尺已从单纯的容量转向"高可靠性+低时延+高寿命"，eSSD的ASP（平均售价）已达移动NAND的两倍。

供应端的情况进一步加剧了市场紧张。邰炜分析，存储原厂普遍将先进产能优先投入高毛利的AI存储产品，成熟制程与消费级产能被持续挤压。行业库存水位已从2023年的10-12周跌至目前的约4周，处于历史安全线以下。"甚至有刚从原厂下线的产品就立刻插到客户服务器中，这在以往是不可想象的，"邰炜描述道。

更严峻的是产能扩张的时滞。存储产能扩张周期长达18-24个月，新建工厂最早要到2027年才能投产（如三星平泽P5、SK海力士龙仁工厂、美光新加坡工厂等）。邰炜判断："2026年全球没有任何一款主流AI存储产品能实现供需完全平衡。"

价格方面，2025年四季度起存储价格全面上涨，2026年一季度涨幅扩大，预计全年维持上涨态势，但涨幅将逐季收敛，三季度后趋于平稳。不过不同产品将出现分化：AI相关存储（HBM、DDR5、企业级SSD）持续紧俏，而消费类存储面临压力。

技术路线上，HBM正快速迭代，HBM3E向HBM4演进，带宽每代接近翻倍。混合键合技术正逐步取代传统微凸块，成为性能升级的核心。特别值得注意的是Base Die的演变——在HBM3E中仅承担信号转接，但HBM4开始部分计算任务下沉至base die，以解决内存墙问题，"Base Die将成为HBM下一代竞争的决胜点"。

NAND领域，300层以上大规模量产推动单Die成本持续下探，但企业级SSD与消费级NAND正走向两条截然不同的技术路径。标准型NAND应用于消费级，而适配AI的企业级SSD标准被无限拔高。

"AI的痛点，不仅仅是算力，而是数据搬不动，"邰炜一针见血地指出。为解决数据搬运的功耗和延迟问题，存储技术正从传统的"缩制程、加堆叠"走向系统架构的重构。HBM、HBF、CXL、存算一体、近存计算等概念性产品正快速走向商用。"谁能解决AI时代数据搬运的功耗和延迟，谁就能定义下一个10年，"邰炜强调。

与AI存储的火热形成鲜明对比，下游终端市场正经历阵痛。邰炜预计，2026年消费类存储需求将面临下滑：全球手机出货量预计下滑10%-15%，部分厂商最坏情况可能减少30%；PC市场同样承压。成本迅速上升导致消费类市场进入调整期。

然而，端侧AI的发展有望成为新的增长动力，更好的体验带来的产品溢价能够抵抗存储价格压力。邰炜同时提醒行业保持清醒：需警惕AI投资过热带来的阶段性波动，资本涌入与项目扎堆可能导致短期需求透支；同时，存储涨价最终需由终端承担，过度透支需求将反噬整个生态。
......
毫无疑问，存储业已进入AI驱动的超级周期。当存储从"算力的配角"变为"算力的基石"，整个半导体产业链的价值分配逻辑，正在被彻底重写。"

https://www.eet-china.com/news/202604023162.html
