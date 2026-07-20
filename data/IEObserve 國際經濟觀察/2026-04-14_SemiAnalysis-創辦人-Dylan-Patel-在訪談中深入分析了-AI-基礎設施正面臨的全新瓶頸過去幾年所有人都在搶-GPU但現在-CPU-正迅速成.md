---
post_id: "1478495090301781"
title: "SemiAnalysis 創辦人 Dylan Patel 在訪談中深入分析了 AI 基礎設施正面臨的全新瓶頸。過去幾年所有人都在搶 GPU，但現在 CPU 正迅速成為制約 AI 發展的關鍵資源，而且壓力正在蔓延到記憶體、儲存，甚至晶片製造產能。"
page_title: ""
requested_url: "https://www.facebook.com/intleconobserve"
final_url: "https://www.facebook.com/intleconobserve"
post_url: "https://www.facebook.com/intleconobserve/posts/pfbid0QZSGwDV9TtPnc3nbD2cHji4rzCEGhDica8m7drZzj4kvG82iNJbx5xTW57ecYsnvl"
creation_time_utc: "2026-04-14T02:12:44+00:00"
fetched_at_utc: "2026-05-08T22:50:27.786451+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent.ftpe8-1.fna.fbcdn.net/v/t39.30808-6/672667368_1478494910301799_7667026434637748406_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=109&ccb=1-7&_nc_sid=13d280&_nc_ohc=kNyCMeifUO4Q7kNvwEOAXap&_nc_oc=AdrQoBa8zsJGRJlo3VwX0W804Jw_gxOBBA9PMG5QrbgHgncZemeu3YXXh0egK7s_aUY&_nc_zt=23&_nc_ht=scontent.ftpe8-1.fna&_nc_gid=p74OJb0F4SVgXPxVqpiQOg&_nc_ss=78100&oh=00_Af5AsTlGlXOoI6VV0Y3kSElIkHarJLkfCiDKVIJPBt_TTw&oe=6A045121"
feedback_id: "ZmVlZGJhY2s6MTQ3ODQ5NTA5MDMwMTc4MQ=="
page_canonical_url: ""
---

# SemiAnalysis 創辦人 Dylan Patel 在訪談中深入分析了 AI 基礎設施正面臨的全新瓶頸。過去幾年所有人都在搶 GPU，但現在 CPU 正迅速成為制約 AI 發展的關鍵資源，而且壓力正在蔓延到記憶體、儲存，甚至晶片製造產能。

原文連結: https://www.facebook.com/intleconobserve/posts/pfbid0QZSGwDV9TtPnc3nbD2cHji4rzCEGhDica8m7drZzj4kvG82iNJbx5xTW57ecYsnvl

![SemiAnalysis 創辦人 Dylan Patel 在訪談中深入分析了 AI 基礎設施正面臨的全新瓶頸。過去幾年所有人都在搶 GPU，但現在 CPU 正迅速成為制約 AI 發展的關鍵資源，而且壓力正在蔓延到記憶體、儲存，甚至晶片製造產能。](https://scontent.ftpe8-1.fna.fbcdn.net/v/t39.30808-6/672667368_1478494910301799_7667026434637748406_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=109&ccb=1-7&_nc_sid=13d280&_nc_ohc=kNyCMeifUO4Q7kNvwEOAXap&_nc_oc=AdrQoBa8zsJGRJlo3VwX0W804Jw_gxOBBA9PMG5QrbgHgncZemeu3YXXh0egK7s_aUY&_nc_zt=23&_nc_ht=scontent.ftpe8-1.fna&_nc_gid=p74OJb0F4SVgXPxVqpiQOg&_nc_ss=78100&oh=00_Af5AsTlGlXOoI6VV0Y3kSElIkHarJLkfCiDKVIJPBt_TTw&oe=6A045121)
SemiAnalysis 創辦人 Dylan Patel 在訪談中深入分析了 AI 基礎設施正面臨的全新瓶頸。過去幾年所有人都在搶 GPU，但現在 CPU 正迅速成為制約 AI 發展的關鍵資源，而且壓力正在蔓延到記憶體、儲存，甚至晶片製造產能。

#為什麼CPU突然不夠用了

Dylan Patel 指出，AI 發展初期 CPU 的角色非常輕量，主要用於儲存、checkpoint 和資料預處理。推論端也很單純，「模型還不夠好，沒辦法做 agentic 的事情。你送一段文字進去，它回一段文字，就這麼簡單，所以不太需要 CPU。」

轉折點出現在大約 15、16 個月前 O1 preview 推出之後。在那之前，驗證模型輸出的方式很簡單，可能只是用正規表達式檢查結構化輸出是否正確。

但隨著強化學習（RL）被深度整合進訓練流程，驗證機制層層升級。「從 regex 變成各種分類器，從分類器變成程式碼的單元測試和編譯，再從那裡變成 agentic 流程，模型會去呼叫資料庫，或是跟物理模擬、生物模擬這類 CPU 密集型的環境互動。」

這個生成器與驗證器之間的迴圈在過去幾年間越來越緊密。而最近六個月，coding agent 的營收從約 20 億美元暴增到超過 100 億美元，agent 的運行時間也大幅拉長。「像 S4 Codex 可以連續工作六、七個小時都沒問題。」在這段時間裡，agent 會不斷呼叫資料庫、抓取資料、自主執行各種操作，全部都需要 CPU 資源。

#整個雲端市場的CPU都被吃光了

Patel 觀察到，過去六個月整個雲端市場的 CPU 幾乎被耗盡。他舉了一個所有開發者都能感受到的例子：「不知道你們最近有沒有常用 GitHub？它真的很不穩定。」原因是 Microsoft 把手上多餘的 CPU 全賣給了其他人，「他們跟 Anthropic 和 OpenAI 都簽了約，結果就是他們自己幾乎沒有 CPU 剩下了。」

過去 GPU 伺服器和 CPU 伺服器之間的比例差距極大，「100 MW 的 GPU 可能只需要 1 MW 甚至更少的 CPU 來支撐。」但現在這個比例正在快速拉近，無論是 RL 訓練還是 agentic 推論都在大量消耗 CPU。Amazon 今年安裝的 CPU 伺服器數量相比去年年增了三倍。

OpenAI 的做法更能說明 CPU 短缺的嚴重程度。「OpenAI 的技術堆疊以前幾乎全部跑在 x86 CPU 上，但 Amazon 手上有大量 ARM CPU，所以他們就把整套程式碼移植過去了。」

Patel 說，「就是那種不管什麼架構，只要能拿到 CPU 我就移植的狀態。通常開發者懶得做這種事，直接去別的地方找資源就好，但問題是現在別的地方也沒有了。」他也指出，OpenAI 與 Amazon 近期簽約的動機之一，就是 OpenAI 直接跑去跟 Amazon 說：把你的 CPU 給我。

#RL訓練與Agent將持續推高CPU需求

Patel 認為 CPU 需求的成長不會放緩，反而會加速。早期的 RL 訓練主要做數學證明，資源需求很低，「模型產生一堆輸出，把它認為正確的答案送到伺服器驗證就行了。」但隨著 RL 變得更複雜，模型在 agentic 過程中會多次編譯、執行單元測試，生成器送往驗證器的頻率大幅增加。

「想像一下未來一兩年的模型訓練，比如一個機器人模型在世界模型（world model）裡導航，試著撿起東西、放下東西。每一個動作都需要被物理模型驗證，而那個物理模型跑在 CPU 上。」

Patel 說，「這比跑單元測試或數學證明需要的 CPU 多太多了。回頭看 O1，它能做的就只有數學。現在像 GPT 5.4 或 Opus 4.6 已經能做 agentic 軟體開發了，但下一階段的模型要理解的是，比如我需要綁鞋帶，綁的時候拉力是多少、材料的抗拉強度是多少，每一步都要被計算驗證，而且驗證的頻率和運算強度會隨時間持續增加。」

#GPU越強CPU需求越大

GPU 效能的代際提升也在加劇 CPU 的壓力。「GPU 每一代功耗越來越高，一顆 GPU 隨著時間推移會對應越來越多的 CPU。」Patel 指出，GPU 每一代都在漲價，但 vCPU 的價格基本持平甚至微降，所以每升級一代 GPU，所需搭配的 CPU 數量就會進一步增加。

還有一個實務層面的因素：GPU 太貴了，不能讓它閒置等待。客戶寧可付費維持一批 CPU 處於 warm pool 狀態，確保 GPU 一產出結果就有 CPU 可以接手驗證。

「GPU 基本上沒有隨需即用（on-demand）的。Lambda 有五萬多顆 GPU，只有四千顆是 on-demand 的，而且永遠賣完。大家都在簽至少好幾個月，多數是好幾年的長約。」如果驗證端的 CPU 沒有準備好，GPU 就只能乾等，等於直接浪費已經付出的高額成本。

#供應鏈全面吃緊：記憶體、儲存、消費端都受衝擊

CPU 短缺只是冰山一角。Patel 指出整個硬體供應鏈都在承壓：記憶體（DRAM）價格過去一年漲了四倍，還會繼續上漲；SSD 也漲了三到四倍，預計還會再漲至少 60%。Intel 和 AMD 都表示產能全部售罄，已向客戶發出漲價通知。「它們已經不是在彼此競爭了，而是在比誰能生產更多、賣更多。」

這股壓力直接波及消費端。「現在要買一台 PC 很難，因為太貴了。Apple 的 Mac Mini 也幾乎賣完了。」CPU、記憶體和儲存的產能在資料中心與消費端之間有一定程度的替代性，而資料中心是更缺乏彈性的買家，正在把價格推高。Patel 直言：「說白了就是犧牲一般消費者。」

#CPU市場的多元化競爭

CPU 市場正經歷前所未有的多元化。過去基本上就是 Intel 和 AMD 兩家，現在 Nvidia 推出了 Vera CPU，Amazon 有 Graviton 已經做到第五、六代，Microsoft 和 Google 也開始大量部署自研 CPU，ARM 即將推出自有品牌的 CPU，Meta 和 Cloudflare 等公司已經表態採用。

「淘金潮來的時候，連拿著壞掉鋤頭的人都能賣鋤頭。」Patel 說。過去 Nvidia 的 Grace CPU 做獨立部署幾乎沒人用，「就是沒那麼好。」但現在情況不同了，可能是 CPU 本身改善了，可能是搭售策略更好了，但更根本的原因就是市場上有產能的人就是贏家，「因為別人都沒有了。」

至於市場何時回歸常態，Patel 認為當供需缺口逐漸收窄，最終還是會回到品質和效能的競爭。

#先進製程的產能爭奪戰

AI 對先進製程的爆炸性需求正在重塑整個半導體產業的格局。AMD 的 MI350、Amazon 的 Trainium 3、Google 的 TPU v7，還有 Nvidia 即將發表的 Ruben，全部都是三奈米製程。這些 AI 晶片正在擠壓所有其他客戶的產能。

「TSMC 已經叫 Apple 趕快從三奈米移到二奈米，因為所有 AI 晶片都要用三奈米的產能。小型手機晶片比大型 AI 晶片更容易製造，所以 AI 晶片正在把其他人擠出去。」Patel 說，Qualcomm 和 MediaTek 也被要求讓路。「這三家公司現在反而在考慮，是不是該去用 Intel 的產能，因為 Intel 不會叫它們走，畢竟 Intel 自己的先進製程也追不上。」

他也點出了 Nvidia 收購 Groq 背後不常被討論的邏輯。「Groq 是在 Samsung 製造的，因為 TSMC 三奈米根本沒有多餘的產能給 Nvidia。如果 AI 的需求真的像我們預期的那麼瘋狂，明年只會更瘋狂，那就隨便做出一顆還行的晶片，它都賣得掉。」

#Intel能因此翻身嗎

被問到 CPU 需求暴增是否能拯救 Intel，Patel 的回答很直接：「短期會好一點，但不是那種公司就得救了的狀況。公司估值看的是未來現金流。」他指出 AMD 和 Amazon 等競爭對手遲早會補上產能缺口，Intel 的短期獲利窗口有限。

但 Intel 的另一個機會來自一個意想不到的方向。AI 吃掉了 TSMC 三奈米和未來二奈米的所有產能，逼得 Apple、Qualcomm、MediaTek 這些原本不會考慮 Intel 的公司開始評估使用 Intel 的代工服務。這可能才是 Intel 真正的轉機所在。


---
[📌 新增貼文至TAIEX.TW比對](https://github.com/wenchiehlee-money/TAIEX.TW/issues/new?template=earnings_tag.yml&title=%E8%B2%BC%E6%96%87%E6%A8%99%E8%A8%98&symbol=&file_path=data%2Fintleconobserve%2F2026-04-14_SemiAnalysis-%E5%89%B5%E8%BE%A6%E4%BA%BA-Dylan-Patel-%E5%9C%A8%E8%A8%AA%E8%AB%87%E4%B8%AD%E6%B7%B1%E5%85%A5%E5%88%86%E6%9E%90%E4%BA%86-AI-%E5%9F%BA%E7%A4%8E%E8%A8%AD%E6%96%BD%E6%AD%A3%E9%9D%A2%E8%87%A8%E7%9A%84%E5%85%A8%E6%96%B0%E7%93%B6%E9%A0%B8%E9%81%8E%E5%8E%BB%E5%B9%BE%E5%B9%B4%E6%89%80%E6%9C%89%E4%BA%BA%E9%83%BD%E5%9C%A8%E6%90%B6-GPU%E4%BD%86%E7%8F%BE%E5%9C%A8-CPU-%E6%AD%A3%E8%BF%85%E9%80%9F%E6%88%90.md&period=)


---
[📌 新增貼文至biztrends.TW比對](https://github.com/wenchiehlee-money/biztrends.TW/issues/new?template=earnings_tag.yml&title=%E8%B2%BC%E6%96%87%E6%A8%99%E8%A8%98&symbol=&file_path=data%2Fintleconobserve%2F2026-04-14_SemiAnalysis-%E5%89%B5%E8%BE%A6%E4%BA%BA-Dylan-Patel-%E5%9C%A8%E8%A8%AA%E8%AB%87%E4%B8%AD%E6%B7%B1%E5%85%A5%E5%88%86%E6%9E%90%E4%BA%86-AI-%E5%9F%BA%E7%A4%8E%E8%A8%AD%E6%96%BD%E6%AD%A3%E9%9D%A2%E8%87%A8%E7%9A%84%E5%85%A8%E6%96%B0%E7%93%B6%E9%A0%B8%E9%81%8E%E5%8E%BB%E5%B9%BE%E5%B9%B4%E6%89%80%E6%9C%89%E4%BA%BA%E9%83%BD%E5%9C%A8%E6%90%B6-GPU%E4%BD%86%E7%8F%BE%E5%9C%A8-CPU-%E6%AD%A3%E8%BF%85%E9%80%9F%E6%88%90.md&period=)
