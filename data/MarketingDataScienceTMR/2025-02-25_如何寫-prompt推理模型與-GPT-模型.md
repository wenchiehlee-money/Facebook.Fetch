---
post_id: "944388177804828"
title: "【如何寫 prompt❓－推理模型與 #GPT  模型 🤖 】"
page_title: ""
requested_url: "https://www.facebook.com/MarketingDataScienceTMR"
final_url: "https://www.facebook.com/MarketingDataScienceTMR"
post_url: "https://www.facebook.com/MarketingDataScienceTMR/posts/pfbid02M7WhKow4zGcR3m2JWxKSEr7VEAVTtoL2nCT8AE79ZE5PpB9zZSTAeLhJLU6upaFgl"
creation_time_utc: "2025-02-25T04:15:02+00:00"
fetched_at_utc: "2026-07-20T12:46:13.851741+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent-sjc6-1.xx.fbcdn.net/v/t39.30808-6/486221884_964896772420635_2379490810948243011_n.jpg?stp=dst-jpg_s720x720_tt6&_nc_cat=102&ccb=1-7&_nc_sid=127cfc&_nc_ohc=eUZAE3VKWgUQ7kNvwF3_Pff&_nc_oc=AdrKwskTF5I6I7myPdUXSjplZdP4PDMQyM-mJHeBvIiZp0BzieaqT894v_OKvUhVVkI&_nc_zt=23&_nc_ht=scontent-sjc6-1.xx&_nc_gid=DjWtZujDgmvFtJY6SnaoIA&_nc_ss=7e120&oh=00_AQA3z9-H-_7UpbLAlCJrDlVhBkA3GeXqSGhHFx1opWlRog&oe=6A63E453"
feedback_id: "ZmVlZGJhY2s6OTQ0Mzg4MTc3ODA0ODI4"
page_canonical_url: ""
---

# 【如何寫 prompt❓－推理模型與 #GPT  模型 🤖 】

原文連結: https://www.facebook.com/MarketingDataScienceTMR/posts/pfbid02M7WhKow4zGcR3m2JWxKSEr7VEAVTtoL2nCT8AE79ZE5PpB9zZSTAeLhJLU6upaFgl

![【如何寫 prompt❓－推理模型與 #GPT  模型 🤖 】](https://scontent-sjc6-1.xx.fbcdn.net/v/t39.30808-6/486221884_964896772420635_2379490810948243011_n.jpg?stp=dst-jpg_s720x720_tt6&_nc_cat=102&ccb=1-7&_nc_sid=127cfc&_nc_ohc=eUZAE3VKWgUQ7kNvwF3_Pff&_nc_oc=AdrKwskTF5I6I7myPdUXSjplZdP4PDMQyM-mJHeBvIiZp0BzieaqT894v_OKvUhVVkI&_nc_zt=23&_nc_ht=scontent-sjc6-1.xx&_nc_gid=DjWtZujDgmvFtJY6SnaoIA&_nc_ss=7e120&oh=00_AQA3z9-H-_7UpbLAlCJrDlVhBkA3GeXqSGhHFx1opWlRog&oe=6A63E453)
【如何寫 prompt❓－推理模型與 #GPT  模型 🤖 】

在為兒子、女兒上課時，分享了推理模型（reasoning-models）與 GPT 模型（gpt-models）的差異 💡。

OpenAI 提供兩種模型：推理模型（如 o1 和 o3-mini）、GPT 模型（如 GPT-4o）。

推理模型就好像一位非常聰明且能自行規劃、有自己想法的夥伴（planners）。GPT模型則是一位非常聰明但需要我們提供明確指令的執行者（workhorses）。

這兩類模型各有其適用性，而且與不同模型協作時，方法會有所不同。

推理模型善於執行模糊任務、解決複雜問題，適合複雜問題拆解、邏輯分析、數學推導、程式碼生成等。

GPT 模型善於執行定義和執行步驟明確的任務，適合文本生成、創意寫作、多輪對話、開放性問答等。

在與不同模型進行協作時，給予的提示語（prompt）也會有所不同。

推理模型的提示語通常更為簡潔，重點在於提出明確的任務目標和需求。不需要詳細的逐步指導，過度拆解反而可能限制了模型本身。

GPT 模型的提示語則需要提出引導推理步驟。借助提示語彌補其在邏輯推理上的短板，通過提出分析思考步驟和範例來引導模型思路。

針對不同任務，選擇不同模型，並設計相對應的提示語，才能充分發揮模型的優勢。

由於女兒參加辯論社，會用 AI 協助辯論的準備。我便以「電車難題」🚋 為例，說明如何與推理模型和 GPT 模型進行協作。
過程中，我展示利用相同的問題「你認同電車難題中的功利主義或是道德主義？」，並觀看 o1（推理模型）和 4o（GPT 模型）哪一種模型生成的效果較好？

很明顯地，面對這種開放式的問題，o1 的表現好很多🏆。

接著我再將 prompt 修改成「請先解釋電車難題的定義，再列出並比較功利主義或是道德主義兩種倫理觀的差異，最後請提出你認同電車難題中的功利主義或是道德主義？」

看了生成結果後可發現，這種將「思維鏈」（Chain-of-Throught，CoT）的概念融入到 prompt 中，能大幅提升 GPT 模型的輸出品質。

最後，當所面對的問題複雜且抽象時🧩，不容易根據背後的思維鏈寫出 prompt，這時，只要提出任務目標和需求，推理模型將能給我們很大的驚喜🎉。

例如，「我需要對電車難題進行辯論，假設我是支持功利主義的一方，請盡可能提出我方的論點腳本類型，內容必須將支持道德主義一方的論點與回應也予以涵蓋。此外，另行假設對方能夠預判我方的論點並事先做好防範。因此請另外提供對方預判的可能論點方案，並根據這些預判方案，分別提出所對應的方案。」（結果 o1 給出了 4 種預判方案，以及各預判方案下各 3 種共 12 種的解決方案。女兒看了直呼太厲害了🔥🔥🔥）

各位夥伴們，有空不妨試一下不同公司推出的推理模型與 GPT 模型，讓自己與 AI 的協作能力更強💪。

👀 點我觀看原文：https://bit.ly/4k8LUtt
✏️ 作者：羅凱揚（台科大企管系博士）、鍾皓軒（臺灣行銷研究有限公司創辦人）
PS：OpenAI 兩種模型文章請參考：https://platform.openai.com/docs/guides/reasoning-best-practices#reasoning-models-vs-gpt-models
