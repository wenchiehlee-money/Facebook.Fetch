---
post_id: "10227386891738239"
title: "前幾天分享了一個把「書變成 Agent Skill」的開源工具，今天看到另一個很有意思的方向："
page_title: "股票"
source_page: "Brian Jhang"
requested_url: "https://www.facebook.com/saved/?list_id=10222174769398438&referrer=SAVE_DASHBOARD_NAVIGATION_PANEL"
post_url: "https://www.facebook.com/iambrianjhang/posts/pfbid0Hzv6BaETRKLHvAt6ZWq17a85QmAhTgcdZr335Cqb4vohTZSjobcvHgmg4N5rQxDnl"
creation_time_utc: ""
fetched_at_utc: "2026-09-22T06:03:09.156795+00:00"
source: "saved_list"
---

# 前幾天分享了一個把「書變成 Agent Skill」的開源工具，今天看到另一個很有意思的方向：

來源：Brian Jhang
原文連結: https://www.facebook.com/iambrianjhang/posts/pfbid0Hzv6BaETRKLHvAt6ZWq17a85QmAhTgcdZr335Cqb4vohTZSjobcvHgmg4N5rQxDnl
前幾天分享了一個把「書變成 Agent Skill」的開源工具，今天看到另一個很有意思的方向：
直接把一本 PDF / EPUB，變成真正的有聲書。

最近研究了一個開源項目 abogen。

它不是單純把文字丟進 TTS，輸出一個 MP3。

而是開始把整套 Audiobook Production Workflow 做起來。

你可以直接丟進：
PDF
EPUB
TXT
Markdown

甚至 SRT / ASS / VTT 字幕。

它會幫你處理章節，再輸出成：
MP3 / FLAC / OPUS / WAV

甚至是完整的：

M4B + Chapters + Metadata + Book Cover

也就是拿到 Audiobook Player 裡，真的會看到：
第一章
第二章
第三章……

而不是一個 10 小時長到不知道播到哪裡的 MP3。

另外一個我覺得很實用的功能是：
同步字幕。

它可以在產生語音的同時生成 SRT / ASS 字幕，而且可以選：
Sentence
逐字
2～3 Words
Sentence Highlighting

所以它不只適合「把電子書變有聲書」。

拿來做：
YouTube 旁白
TikTok / Reels
Podcast 素材
教學影片
文章轉語音

都滿實用。

它的核心語音模型使用 Kokoro-82M。

而且可以把 Model + Voices 先下載到電腦。

之後：
完全離線跑。

這件事我很喜歡。

因為你不一定需要：
把整本書上傳到某個 Cloud TTS
按分鐘付 API 費用
把自己的文件送到第三方 Server

你的電腦自己就是 Audiobook Factory。

而且現在它甚至開始往「AI 有聲書製作工具」演化。

新版 Web UI 已經加入：
Supertonic TTS

Voice Mixer
可以把不同 Voice 混合成自己的 Voice Profile。

Pronunciation Override
碰到人名、品牌、專有名詞念錯，可以單獨調整。

甚至還加入：
Speaker / Role Assignment

也就是同一本書，可以讓不同角色使用不同聲音。

開始有點像：
Theatrical Audiobook。

除此之外，它還可以接 OpenAI-compatible LLM。

例如接本機 Ollama，在文字真正送進 TTS 之前，先讓 LLM 處理不好朗讀的文字、縮寫與特殊格式。

最後生成完成後，甚至可以：
直接 Push 到自己的 Audiobookshelf。

這已經不是「文字轉語音」了。

而是一條：
Book → Text Processing → Voice → Chapters → Subtitles → Metadata → Audiobook Library

的完整 Pipeline。

作者 Demo 裡，一台 RTX 2060 Mobile，約 3,000 characters 的文字，生成 3 分 28 秒語音只花約 11 秒。

當然，整本書的速度還是會依 CPU / GPU 與設定不同。

目前 Windows / Mac / Linux 都能跑，NVIDIA GPU 可以加速，Linux 也支援 AMD ROCm。

GitHub 現在約 5,800 Stars，MIT 開源。

我覺得這類工具背後有一個很有意思的變化：
以前想把一本書變成 Audiobook，是一個「內容製作」工作。

要錄音、剪輯、切章節、整理 Metadata。

現在開始變成：
丟一本 EPUB 進去 → 等 AI 跑完 → 得到完整 Audiobook。

AI 正在把越來越多原本屬於「媒體製作」的工作，壓縮成一條自動化 Pipeline。

相關 Repo 我放留言。

如果你平常有大量 電子書、PDF、長文章，或者自己做 YouTube / Podcast / 知識型內容，這個很值得收藏。

以前 AI 只是幫你念文字。
現在，你自己的電腦開始可以直接變成一間有聲書製作公司。
