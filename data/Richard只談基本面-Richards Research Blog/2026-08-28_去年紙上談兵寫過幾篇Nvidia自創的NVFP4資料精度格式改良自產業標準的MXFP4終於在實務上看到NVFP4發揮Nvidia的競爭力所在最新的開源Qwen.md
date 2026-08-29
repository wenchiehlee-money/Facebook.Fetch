---
post_id: "1596405745509459"
title: "去年紙上談兵寫過幾篇Nvidia自創的NVFP4資料精度格式(改良自產業標準的MXFP4)，終於在實務上看到NVFP4發揮Nvidia的競爭力所在，最新的開源Qwen 3.8 Flash-Next模型，使用NVFP4，要發揮模型其FP4精度量化效能，必須使用具備原生NVFP4的Blackwell晶片，別家晶片或NV上代Hopper都不行只能改用FP8變體"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/profile.php?id=100054201473657"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0nsrjmbmnoC9QSLRT164zLnohdJhUKwqvcLfGbhnVDpB136LxfLqkB4FS2KaXFdQ1l&id=100054201473657"
creation_time_utc: "2026-08-28T15:54:07+00:00"
fetched_at_utc: "2026-08-29T07:48:54.332429+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTU5NjQwNTc0NTUwOTQ1OQ=="
page_canonical_url: ""
---

# 去年紙上談兵寫過幾篇Nvidia自創的NVFP4資料精度格式(改良自產業標準的MXFP4)，終於在實務上看到NVFP4發揮Nvidia的競爭力所在，最新的開源Qwen 3.8 Flash-Next模型，使用NVFP4，要發揮模型其FP4精度量化效能，必須使用具備原生NVFP4的Blackwell晶片，別家晶片或NV上代Hopper都不行只能改用FP8變體

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0nsrjmbmnoC9QSLRT164zLnohdJhUKwqvcLfGbhnVDpB136LxfLqkB4FS2KaXFdQ1l&id=100054201473657
去年紙上談兵寫過幾篇Nvidia自創的NVFP4資料精度格式(改良自產業標準的MXFP4)，終於在實務上看到NVFP4發揮Nvidia的競爭力所在，最新的開源Qwen 3.8 Flash-Next模型，使用NVFP4，要發揮模型其FP4精度量化效能，必須使用具備原生NVFP4的Blackwell晶片，別家晶片或NV上代Hopper都不行只能改用FP8變體

-----------------------------------------------------------
"4.3 Qwen3.8 Flash-Next — 具備每層嵌入的 NVFP4
Qwen3.8 Flash-Next 搭載 NVFP4 — NVIDIA 的 FP4 格式，採用 4 位元浮點運算，並以每區塊縮放為單位。Inferact NVFP4 量化檢查點也在 NVFP4 中使用每層嵌入，因此包括 51B n-gram 表格在內的整個模型皆被量化[3]。在磁碟上，NVFP4 檢查點約為 130 GB——是三個中最小的，差距明顯不少。

選擇NVFP4而非通用FP4值得注意。NVFP4 是 NVIDIA Blackwell GPU（B200、GB200、B300、GB300）原生支援的格式，而 vLLM 的 NVFP4 路徑明確要求 Blackwell 格式[3]。在 Hopper（H100/H200）上，必須改用 FP8 檢查點。這是一個有意義的硬體限制：Hopper 上的團隊無法使用最激進的量化。

4.4 比較分析
這三種精準選擇反映了三種不同的投注方式：

DeepSeek（FP4+FP8 混合，QAT）——賭 QAT 訓練的 FP4 專家能保留足夠品質，將預設出貨，且沒有 BF16 的備用方案。最積極的。
GLM（FP8 e4m3 primary，BF16 可用）— 押注 FP8 在壓縮與品質之間取得恰當平衡，同時保留 BF16 參考，供追求最高保真度的使用者使用。
Qwen（NVFP4，僅Blackwell）— 押注生態系統會迅速轉向Blackwell，NVFP4可成為預設，並接受Hopper用戶必須使用FP8變體。"

https://local-ai-zone.github.io/blog/flash-tier-ai-models-comparative-analysis.html

https://www.facebook.com/share/p/18BJfLEzHZ/

https://www.facebook.com/share/p/1CGuwrrz15/
