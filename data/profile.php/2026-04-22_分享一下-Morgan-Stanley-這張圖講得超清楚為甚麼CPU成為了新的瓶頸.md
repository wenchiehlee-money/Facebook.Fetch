---
post_id: "122180098184771552"
title: "分享一下 Morgan Stanley 這張圖，講得超清楚為甚麼CPU成為了新的瓶頸。"
page_title: ""
requested_url: "https://www.facebook.com/profile.php?id=61573146584049"
final_url: "https://www.facebook.com/profile.php?id=61573146584049"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid02TAQSGytwqihVPaKJG6bczFwSPJtRC2ypYtR4HVPYCxJC9BAWr1nxAWjNeXLnMif5l&id=61573146584049"
creation_time_utc: "2026-04-22T04:14:27+00:00"
fetched_at_utc: "2026-07-20T12:57:19.783956+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-sjc6-1.xx.fbcdn.net/v/t39.30808-6/677804417_122180098160771552_7552057192895755302_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=H5LIY1cG4b8Q7kNvwFzfSkz&_nc_oc=AdqVPFT33PLODsigtpP9fYsELJee3O-XKMVnh2gCjPDY7Ma4boUf3mJAupIE1xyuuaE&_nc_zt=23&_nc_ht=scontent-sjc6-1.xx&_nc_gid=IUzpTjJRvU7TfM34oiL4Xw&_nc_ss=7e120&oh=00_AQD8VV1vYzOP0NlxFFjVQO2-I6jLIf7-a9scXb_zsKqZow&oe=6A63E07E"
feedback_id: "ZmVlZGJhY2s6MTIyMTgwMDk4MTg0NzcxNTUy"
page_canonical_url: ""
---

# 分享一下 Morgan Stanley 這張圖，講得超清楚為甚麼CPU成為了新的瓶頸。

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid02TAQSGytwqihVPaKJG6bczFwSPJtRC2ypYtR4HVPYCxJC9BAWr1nxAWjNeXLnMif5l&id=61573146584049

![分享一下 Morgan Stanley 這張圖，講得超清楚為甚麼CPU成為了新的瓶頸。](https://scontent-sjc6-1.xx.fbcdn.net/v/t39.30808-6/677804417_122180098160771552_7552057192895755302_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=H5LIY1cG4b8Q7kNvwFzfSkz&_nc_oc=AdqVPFT33PLODsigtpP9fYsELJee3O-XKMVnh2gCjPDY7Ma4boUf3mJAupIE1xyuuaE&_nc_zt=23&_nc_ht=scontent-sjc6-1.xx&_nc_gid=IUzpTjJRvU7TfM34oiL4Xw&_nc_ss=7e120&oh=00_AQD8VV1vYzOP0NlxFFjVQO2-I6jLIf7-a9scXb_zsKqZow&oe=6A63E07E)
分享一下 Morgan Stanley 這張圖，講得超清楚為甚麼CPU成為了新的瓶頸。
​
先簡單解釋一下圖中的「總延遲百分比（% of Total Latency）」是什麼意思： 它指的是你按下送出後，整個過程到最後拿到答案的等待時間，被拆成兩部分：
​
- 深藍色（GPU Compute）：AI 模型在顯示卡上「思考、產生文字」的時間
​
- 淺米色（CPU Processing）：其他所有「安排工作、叫工具、查資料、整理結果」的後續動作時間
​
兩者加起來永遠是 100%。
​
圖表顯示 AI 任務這些年怎麼一步步進化，也讓 CPU 的角色越來越重要：
​
- Chatbot（簡單聊天機器人，基準）：以前的 ChatGPT 時代，85% 時間都在 GPU 思考，CPU 只佔 15%。
​
- RAG Pipeline（檢索增強生成）：開始會去查資料、抓文件，CPU 時間暴增到 45%。
​
- Coding Assistant（程式碼助手）：要執行程式、debug、處理檔案，CPU 已經反超到 55%。
​
- Multi-tool Agent（多工具代理）：同時叫多個工具、互相配合，CPU 佔 70%。
​
- Research Agent（研究代理）：要做長時間研究、上網瀏覽、寫報告，CPU 衝到 82%。
​
- Complex Orchestration（複雜任務協調）：最先進的智能代理，要自己規劃步驟、記憶上下文、處理錯誤、平行運作多個 AI……CPU 佔到 92%，GPU 只剩 8%。
​
簡單來說就是：任務越複雜、越需要「行動」而不是單純「回答」，CPU 就變成更大的瓶頸。 模型思考得很快，但「秘書團隊」（CPU）安排一切的時間卻越來越長，GPU 常常在旁邊乾等。
​
這不是說GPU不重要，但未來建 AI 系統時，不能再只狂砸顯示卡，還得大幅提升 CPU 運算力、記憶體速度和軟體協調效率。把「大腦（GPU）」和「大腦的秘書團隊（CPU）」比例調平衡，才是王道。
​
我上週深入分析了CPU的整個投資邏輯，不同標的的具體投資機會，我推薦大家都去閱讀一下，你會對整個板塊有不一樣的認知。
​
- KP
