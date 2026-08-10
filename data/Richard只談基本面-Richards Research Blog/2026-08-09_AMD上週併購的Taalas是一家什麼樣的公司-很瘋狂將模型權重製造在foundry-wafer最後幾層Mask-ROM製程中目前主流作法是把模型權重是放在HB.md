---
post_id: "1579839340499433"
title: "AMD上週併購的Taalas是一家什麼樣的公司? 很瘋狂，將模型權重製造在foundry wafer最後幾層Mask ROM製程中，目前主流作法是把模型權重是放在HBM中，少數新創如Cerebras和Groq放在SRAM中，但是SRAM太貴太小放不了大模型，要串聯很多很多顆XPU才行，Taalas把晶片很大部分做了Mask ROM和SRAM，模型權重固定(不能改)製造成晶片的一部分，如附圖"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0qZUJxHe1u1qK9YjQFsj69mKwiWMYREmpcTzqkwAFXufTjD5f34cBh9Am3yLtAFyGl&id=100054201473657"
creation_time_utc: "2026-08-09T15:01:17+00:00"
fetched_at_utc: "2026-08-10T03:16:36.744578+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-iad3-2.xx.fbcdn.net/v/t39.30808-6/768310339_1579830677166966_4833733986724555306_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=TxPZ1AN1IvIQ7kNvwF_YmIv&_nc_oc=AdrP6bCf09BowaZl9bbsAh64nkw-GCqEA0HsLecPc3GPPCebkBN4-RxOOk2F8KUHCoQ&_nc_zt=23&_nc_ht=scontent-iad3-2.xx&_nc_gid=l_8h6nqylc7Hu5P2Ns2OSQ&_nc_ss=7e120&oh=00_AQGgtz1dUafwOqfneU-TBLV4WlFpa7VQJHR0otIH45JFaw&oe=6A7EFC52"
feedback_id: "ZmVlZGJhY2s6MTU3OTgzOTM0MDQ5OTQzMw=="
page_canonical_url: ""
---

# AMD上週併購的Taalas是一家什麼樣的公司? 很瘋狂，將模型權重製造在foundry wafer最後幾層Mask ROM製程中，目前主流作法是把模型權重是放在HBM中，少數新創如Cerebras和Groq放在SRAM中，但是SRAM太貴太小放不了大模型，要串聯很多很多顆XPU才行，Taalas把晶片很大部分做了Mask ROM和SRAM，模型權重固定(不能改)製造成晶片的一部分，如附圖

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0qZUJxHe1u1qK9YjQFsj69mKwiWMYREmpcTzqkwAFXufTjD5f34cBh9Am3yLtAFyGl&id=100054201473657

![AMD上週併購的Taalas是一家什麼樣的公司? 很瘋狂，將模型權重製造在foundry wafer最後幾層Mask ROM製程中，目前主流作法是把模型權重是放在HBM中，少數新創如Cerebras和Groq放在SRAM中，但是SRAM太貴太小放不了大模型，要串聯很多很多顆XPU才行，Taalas把晶片很大部分做了Mask ROM和SRAM，模型權重固定(不能改)製造成晶片的一部分，如附圖](https://scontent-iad3-2.xx.fbcdn.net/v/t39.30808-6/768310339_1579830677166966_4833733986724555306_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=TxPZ1AN1IvIQ7kNvwF_YmIv&_nc_oc=AdrP6bCf09BowaZl9bbsAh64nkw-GCqEA0HsLecPc3GPPCebkBN4-RxOOk2F8KUHCoQ&_nc_zt=23&_nc_ht=scontent-iad3-2.xx&_nc_gid=l_8h6nqylc7Hu5P2Ns2OSQ&_nc_ss=7e120&oh=00_AQGgtz1dUafwOqfneU-TBLV4WlFpa7VQJHR0otIH45JFaw&oe=6A7EFC52)
AMD上週併購的Taalas是一家什麼樣的公司? 很瘋狂，將模型權重製造在foundry wafer最後幾層Mask ROM製程中，目前主流作法是把模型權重是放在HBM中，少數新創如Cerebras和Groq放在SRAM中，但是SRAM太貴太小放不了大模型，要串聯很多很多顆XPU才行，Taalas把晶片很大部分做了Mask ROM和SRAM，模型權重固定(不能改)製造成晶片的一部分，如附圖

1. 晶片內MASK ROM和SRAM，MASK ROM存權重(燒死)、SRAM處理KV cache

2. LLM模型訓練好版本確定後，兩個月即可產出，應該是將晶片前面多層TSMC先做，最後段的MASK ROM層數等權重固定後繼續製造

3. Server不用設計，用標準的PCIe算力卡

4. 可多台機器堆疊擴展處理上兆參數的模型

5. 模型更換的時候，要整片算力卡換掉

6. 我想，當模型版本(含checkpoint小改版)不斷更新的時候，Taalas方法不適合，因為模型改版之後算力卡都要丟掉，但總有一天，模型分化之後，某些模型在某些特定領域逼近最佳解，模型更迭趨緩，例如一個模型可以用一兩年不變，Taalas的方法可以是絕對的特用，極致特用，只能用單一版本模型

7. 例如語音辨識模型，可能很快會到達最佳解

8. 有點像任天堂Mask ROM卡匣，一個遊戲一片卡，Taalas是一個模型一片卡(PCIe)，換卡不換機

------------"將完成的 AI 推論權重直接編碼到晶片的電晶體中，並去除所有為了讓運算引擎可塑性而帶來的軟體雜質，讓公司能持續調整和調整模型。

透過這樣做，你也能徹底簡化 AI 裝置的架構，而 Taalas 所做的那樣，你能消除所有串列與平行運算引擎——尤其是 GPU 和 AI XPU，必須依賴 HBM 堆疊 DRAM 來獲得與浮點數和整數效能相稱頻寬的計算與記憶體之間的壁壘。
......
那麼，究竟什麼是硬編碼推理晶片？它是如何運作的？

「我們基本上有一個架構，將模型嵌入，並將模型和權重硬編碼到我們所謂的遮罩 ROM 回調結構中，該結構與 SRAM 回溯結構搭配使用。兩者合起來能同時儲存模型並執行 KV 快取的所有計算。我們有轉接器和客製化選項——我們都支援這些。這種設計讓我們在運算和儲存方面都能達到超高密度，並且能在這些儲存上以極快的速度進行運算，這正是提升密度並降低成本的原因。」

「在現今世代，我們的硬體連接部分有 80 億個參數，加上 SRAM 讓我們能做 KV 快取、微調等調整。在下一代，我們將能在晶片中處理多達200億個參數。即使有數兆個參數，我們談論的晶片數量也只有幾十顆，這和目前市面上任何其他產品相比都非常非常小。」

ajic 沒有具體說明建築結構——Taalas 目前希望它保持有點黑盒子——但他補充說：

「我們有一套用於遮罩ROM召回結構的方案——硬接線部分——我們可以儲存四個位元，並用單一電晶體完成與之相關的乘法——所有相關操作。所以密度基本上是瘋狂的。這不是核物理——它是完全數位化的。這只是個巧妙的詭計，我們不想公開播出。但一旦你把所有東西硬接上，你就會有機會用完全不同的方式來做事，而不是必須面對改變。重要的是我們可以在一個電晶體中加一個權重，並完成與之相關的乘法。而且你知道，乘數器其實是電腦裡最關鍵的部分。」

「我們發明的東西也不算特別難。這只是個聰明的設計，沒有人看出來，因為沒有人走過這條路。我們是在兩年多前就已經出現，想要徹底消除記憶體與運算之間的障礙。這就是整個計畫的起點。我們想到的第一個方法——基本上也是當時唯一能在可預測時間內產出產品的方法，因為我們不想成為研究教授，三年後卻有失敗的產品——就是迅速轉向這種基於 ROM 的方法。我們開始詳細研究，然後發現這比我們想像的還要好。」

顯而易見的是，每次模型變更，從 Llama 3.1 到 Llama 4，都必須重新調整 HC 晶片。目前，Taalas 專注於將開源模型的權重刻刻刻在 HC 晶片上，但不難想像 Anthropic 和 OpenAI 會拿起電話訂購客製化加速器。連 Google 也許會想試試看。順帶一提，據我們所知，Taalas 已以 Bajic 名義申請了 14 項專利，涵蓋其技術;可能還有更多，因為專利搜尋非常糟糕——即使是 Google 專利也是如此。

在 HC 推論引擎上蝕刻新模型，是更換 HC 晶片設計中的兩層金屬，而非完全拆除。而且訓練模型的成本高達數十億美元，支付相對象徵性的費用來調整 HC 推論引擎以適應新版本或完全不同的模型，並不算什麼大問題。Kharya 表示，訓練一個模型的成本是從 Taalas 獲得合理量度客製化 HC 晶片的 100 倍。
......
透過 Taalas 與台灣積體電路製造有限公司共同打造的「代工優化工作流程」，客戶可在兩個月內從模型權重到可部署的 PCI-Express 卡，實際進行推論。

第一代HC1晶片採用台積電6奈米N6製程實現。以815 mm2來說，現在已經接近晶片的十字線極限（在我們進入高NA製程前，因為那會將準星尺寸減半，這其實並不理想）。每顆HC1晶片封裝上有530億個電晶體，其中大多數很可能是用於ROM和SRAM記憶體。Bajic表示，HC1卡約耗200瓦，而一台雙插槽X86伺服器，內含十張HC1卡，輸出功率為2,500瓦。

順帶一提，因為 HC1 卡速度快，要獲得低延遲推論不需要批次查詢，這代表 Taalas 裝置的頻寬壓力很低。低到如果你想將卡群組起來跑更大模型，PCI-Express 匯流排就足夠了，Taalas 今年晚些時候會允許客戶利用管線平行處理，將工作分散到各 HC 卡之間。事實上，到了夏天，它將擁有一個 Llama 3.1 模型，硬編碼在 HC 晶片中，擁有 200 億參數，年底時將擁有一個 Frontier 級的大型語言模型——可能是 Llama、可能是 DeepSeek，甚至兩者皆有——能在一系列 HC 卡上執行推理。此架構將被稱為 HC2。
......"

https://www.nextplatform.com/compute/2026/02/19/taalas-etches-ai-models-onto-transistors-to-rocket-boost-inference/4092140
