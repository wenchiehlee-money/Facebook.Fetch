---
post_id: "1443609780789057"
title: "老黃對CPU看法的轉變，AI Agent和後訓練任務中CPU重要性提升"
page_title: "Richard只談基本面-Richard's Research Blog"
requested_url: "https://www.facebook.com/profile.php?id=100054201473657"
final_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
post_url: "https://www.facebook.com/permalink.php?story_fbid=pfbid0vHLia7jjUoYieoa9QN1KhBxjbfGpoqKkGEHA6orUvAd8XXehR5zma16qmNK3H92Al&id=100054201473657"
creation_time_utc: "2026-02-27T13:23:53+00:00"
fetched_at_utc: "2026-06-17T12:44:23.919157+00:00"
source: "public_graphql"
attachment_type: ""
attachment_url: ""
image_url: ""
feedback_id: "ZmVlZGJhY2s6MTQ0MzYwOTc4MDc4OTA1Nw=="
page_canonical_url: "https://www.facebook.com/people/Richard%E5%8F%AA%E8%AB%87%E5%9F%BA%E6%9C%AC%E9%9D%A2-Richards-Research-Blog/100054201473657/"
---

# 老黃對CPU看法的轉變，AI Agent和後訓練任務中CPU重要性提升

原文連結: https://www.facebook.com/permalink.php?story_fbid=pfbid0vHLia7jjUoYieoa9QN1KhBxjbfGpoqKkGEHA6orUvAd8XXehR5zma16qmNK3H92Al&id=100054201473657
老黃對CPU看法的轉變，AI Agent和後訓練任務中CPU重要性提升

記得嗎?之前不只一次法說，老黃對CPU的說法是，GPU正在、即將取代很多很多的傳統CPU應用，都要轉成GPU "加速運算"，CPU的未來都會轉變成GPU的成長空間TAM，雖然說話當時NV也有獨立的Grace CPU產品線，有沒有注意到，這次老黃這兩三年來第一次講CPU only的重要性、應用和未來，CPU only，在AI訓練之前的資料處理、工具tools、Post-training(之前寫的coding model的RL強化學習需要大量的compiling後評估程式的結果進入獎勵回饋系統)、Grace/Vera有卓越的單執行緒性能、And so some of the use cases in the entire pipeline of artificial intelligence includes using a lot of CPUs.

------"但在最高層級，我們對CPU的架構決策與全球其他CPU有根本不同。它是唯一支援 LPDDR5 的資料中心 CPU。其設計重點在於極高的資料處理能力。原因在於我們感興趣的大多數運算問題都是資料驅動的，人工智慧就是其中之一。單執行緒的效能和頻寬比例更是驚人。

我們做出這些架構決策，是因為在整個階段，從資料處理開始的人工智慧不同階段，在你開始訓練之前，你必須先做資料處理。所以你會看到資料處理、預訓練和後期訓練，現在 AI 正在學習如何使用工具。而工具的使用，許多工具是在純 CPU 環境中運行，或是在 CPU 與 GPU 加速環境下運行。而 Vera 則被設計成優秀的後續訓練 CPU。因此，人工智慧整個流程中的某些應用案例包括大量使用 CPU。我們愛 CPU 和 GPU。當你像我們這樣將演算法加速到極限時，Amdahl 定律會建議你需要非常非常快的單執行緒 CPU，這也是為什麼我們打造 Grace 是為了在單執行緒效能上表現出色，而 Vera 的表現遠超這點。

But at the highest level, we made fundamentally different architecture decisions about our CPUs compared to the rest of the world's CPUs. It's the only data center CPU that supports LPDDR5. It is designed to be focused on very high data processing capabilities. And the reason for that is because most of the computing problems that we're interested in are data-driven, artificial intelligence being one. And the single-threaded performance and its ratio with bandwidth is just off the charts.

And we made those architectural decisions because in the entire phase, the different phases of AI from data processing, before you even do training, you have to do data processing. So you have data processing, pre-training and in post-training now, the AIs are learning how to use tools. And the usage of tools, many of those tools run in CPU-only environments or they run in CPU with GPU-accelerated environments. And Vera was designed to be an excellent CPU for post-training. And so some of the use cases in the entire pipeline of artificial intelligence includes using a lot of CPUs. We love CPUs as well as GPUs. And when you accelerate the algorithms to the limit as we have, Amdahl's Law would suggest that you need really, really fast single-threaded CPUs, and that's the reason why we built Grace to be extraordinary to be great at single-threaded performance, and Vera is off the charts better than that."
