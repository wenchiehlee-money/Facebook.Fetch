---
post_id: "1505160860968537"
title: "Nvidia執行長Jensen Huang回到史丹佛，與學生進行一場橫跨技術、策略、產業政策的深度對話。從agent運算的架構、能源瓶頸，到對AI監管論述的反擊，他用第一性原理拆解這個產業正在經歷的重大轉折。"
page_title: "IEObserve 國際經濟觀察"
requested_url: "https://www.facebook.com/intleconobserve"
final_url: "https://www.facebook.com/intleconobserve"
post_url: "https://www.facebook.com/intleconobserve/posts/pfbid0o96aazKFs5JG1kczHuDFu9SFQMVcaj2nu9H9jZ2rLt3J6m6twgPTBTAmVsqYCn7tl"
creation_time_utc: "2026-05-16T22:14:39+00:00"
fetched_at_utc: "2026-05-31T10:40:01.202678+00:00"
source: "public_graphql"
attachment_type: "Photo"
attachment_url: ""
image_url: "https://scontent.ftpe8-2.fna.fbcdn.net/v/t39.30808-6/701254470_1505159694301987_6485504047330777012_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=101&ccb=1-7&_nc_sid=127cfc&_nc_ohc=n78dJSdIrGIQ7kNvwFHJYe6&_nc_oc=AdpWb3sgTRlBR1XrloHDYscVDpyMXX-uR9_JNjrFkmD7SAzV-KPUMIx3KlP6Zc5QEUo&_nc_zt=23&_nc_ht=scontent.ftpe8-2.fna&_nc_gid=9eKbXSq13yKuq5LCsHmWZw&_nc_ss=78100&oh=00_Af8AadQfGDgwglP0e9JLtoBGKOin6yNytt-Dj9zQRf1cpw&oe=6A21F81E"
feedback_id: "ZmVlZGJhY2s6MTUwNTE2MDg2MDk2ODUzNw=="
page_canonical_url: "https://www.facebook.com/intleconobserve"
---

# Nvidia執行長Jensen Huang回到史丹佛，與學生進行一場橫跨技術、策略、產業政策的深度對話。從agent運算的架構、能源瓶頸，到對AI監管論述的反擊，他用第一性原理拆解這個產業正在經歷的重大轉折。

原文連結: https://www.facebook.com/intleconobserve/posts/pfbid0o96aazKFs5JG1kczHuDFu9SFQMVcaj2nu9H9jZ2rLt3J6m6twgPTBTAmVsqYCn7tl

![Nvidia執行長Jensen Huang回到史丹佛，與學生進行一場橫跨技術、策略、產業政策的深度對話。從agent運算的架構、能源瓶頸，到對AI監管論述的反擊，他用第一性原理拆解這個產業正在經歷的重大轉折。](https://scontent.ftpe8-2.fna.fbcdn.net/v/t39.30808-6/701254470_1505159694301987_6485504047330777012_n.jpg?stp=dst-jpg_s640x640_tt6&_nc_cat=101&ccb=1-7&_nc_sid=127cfc&_nc_ohc=n78dJSdIrGIQ7kNvwFHJYe6&_nc_oc=AdpWb3sgTRlBR1XrloHDYscVDpyMXX-uR9_JNjrFkmD7SAzV-KPUMIx3KlP6Zc5QEUo&_nc_zt=23&_nc_ht=scontent.ftpe8-2.fna&_nc_gid=9eKbXSq13yKuq5LCsHmWZw&_nc_ss=78100&oh=00_Af8AadQfGDgwglP0e9JLtoBGKOin6yNytt-Dj9zQRf1cpw&oe=6A21F81E)
Nvidia執行長Jensen Huang回到史丹佛，與學生進行一場橫跨技術、策略、產業政策的深度對話。從agent運算的架構、能源瓶頸，到對AI監管論述的反擊，他用第一性原理拆解這個產業正在經歷的重大轉折。

#從Hopper到Rubin到Feynman的設計脈絡
每一代Nvidia系統都對應一個運算模式的躍遷。
「Hopper是為一個叫pre-training的全新問題空間設計的。當時我們得出結論，雖然前一代已經很大，但我們應該建造比世界上任何最大的科學超級電腦還要大的系統。當時世界上最大的超級電腦大約3.5億美元，我們在想pre-training會是這麼大的領域、這麼重要的問題，所以我們應該設計多billion美元的系統。」

「在我們考慮做這件事的時候聽起來很瘋狂，你會有正好零個客戶。因為最貴的東西是3.5億美元，而你在建multibillion美元的東西。所以你在建一個正好0客戶的市場，但我們還是基於first principles去做了。」

Grace Blackwell與NVLink 72是為inference設計：「處理神經網路有prefill做context processing和attention processing，還有decode生成tokens。生成tokens需要極高的memory bandwidth，需要的量遠超過一顆晶片能提供的。所以我們把72顆綁在一起，必須發明各種新的switching和interconnect系統，創造了世界上第一台rack-scale電腦。」

「比上一代加速50倍。兩年內我們把某個東西改進50倍，Moore's Law只會給你2倍。」

下一代Vera Rubin是為agents設計：「目標不只是思考，目標是做事。所以Vera Rubin是為agents設計的。」

Huang拆解agent的compute pattern：「你必須load大量memory，long-term memory放儲存，工作memory也要處理。儲存需要能直接跟GPU溝通，你不能把資料從網路儲存複製來複製去，所以儲存直接連到fabric。」

「Agent會用大量工具，所以CPU會非常重要。但當前世代的CPU是為雲端運算設計的，有幾百個core。Agent的CPU不一樣，因為AI是這個多billion美元的系統，它送出一個指令去用一個工具，那個工具會在CPU上跑。同時這個多billion美元的GPU超級電腦在等這一顆CPU，所以這顆CPU真的需要極低latency。」

「所以我們設計了Vera，對單執行緒、多核單執行緒程式碼，它是目前最高效能的CPU。」

關於下一代Feynman：「Feynman來的時候，會像所有軟體，我們今天叫它們agents，過去叫module或submodule。未來你會有agents的系統，agents底下有sub-agents，sub-agents底下還有sub-agents，這群agent的swarm需要什麼樣的電腦？Feynman大概就是關於這個。」

#千倍能源需求與生成式運算的本質
關於能源瓶頸，Huang先談Nvidia能控制的部分：「在我們控制範圍內的就是energy efficiency。看tokens per watt，我們改善了50倍，未來還要繼續用很大的倍數改善，而且會複利累積。」

關於整體需求規模：「未來的電腦會有兩個特性：一個是always generated因為它是智慧的、情境感知的；第二是continuous。生成式運算用continuous方式運作，跟過去基於檢索、按需啟動的pre-recorded computing相比，需要的能源完全不同。」

「我認為我們需要的compute大概是現在的1000倍。我不會驚訝這個數字差個幾個數量級。所以我們需要更多compute，更多能源。」

關於能源來源：「因為過去對sustainable energy成本的擔憂，我們對sustainable energy投資不足。但現在是人類歷史上投資sustainable energy最好的時機，因為market forces非常強。過去你需要政府補貼去蓋太陽能農場、蓋核電廠，現在市場會付錢請你做。」

「Market forces現在這麼強，這是我們升級電網、升級老舊基礎設施、加入各種sustainable energy的最好機會。」

#對AI監管論述的反擊
被問到敵對國家取得Nvidia晶片的議題，Huang把話題拉回基本面。

「我們是做什麼的？我們做GPU。GPU用在電動遊戲，用在送醬油，用在醫療影像。如果你昨天做了CT scan，背後就是Nvidia。Nvidia在世界上每一個醫療影像系統裡。」

「我根本反對、現在這個時刻完全沒道理的是，把Nvidia GPU跟原子彈相提並論。有十億人在用Nvidia GPU。我向你們推薦Nvidia GPU，向我的家人、孩子、我愛的人推薦Nvidia GPU，但我不會向任何人推薦原子彈。那個類比是愚蠢的。」

「如果你從那裡開始，你無法完成整個思路。」

關於「美國公司去外國市場一定會輸」的論點：「為什麼美國公司要去外國市場競爭？反正都會輸。如果你們把這個哲學套用到所有事情上，為什麼早上要起床？我不接受『反正都會輸』。如果你要我輸，你必須打贏我。但我會反擊。」

關於剝奪某些國家通用運算能力的論點：「Nvidia現在是通用運算公司。我剛剛給了你一大堆通用use case。剝奪通用運算能力，只是為了讓一兩家公司獲益，對我來說沒道理。為什麼一整個產業要受苦，只為了另一家公司或一兩家公司獲益？整個美國科技產業是我們的國寶之一。」

「如果我做好我的工作，當你們畢業時，你們會畢業進入人類歷史上最強大的電腦產業、最強大的產業。但如果我們因為某些理由放棄，或透過政策決定我們不能去賣、把三分之二的市場讓給其他公司，到你們畢業的時候，你們會進入一個產業的空殼。」

「我們以前看過這種空殼產業。很久以前，同樣的論點曾經針對美國的電信業。今天美國已經沒有基礎的電信技術了。」

#AI是奇點的論述是不負責任的
對於某些AI公司用singularity論述影響政策，Huang的批評很尖銳。

「某些reasoning system說AI會來，會是一個singularity moment。那個時刻一到，會是世界上最強大的東西。它會像閃電一樣降臨，我們不知道是週三還是週四7點，但它一來就game over。某個機率它會是我們所知社會的終結。」

「拜託，我們都看過《Dune》，我們不需要再演一次。」

「他們在公共場合演出自己的科幻幻想，當所有人都依賴他們的話、相信他們的話時，這是不負責任的。這不是真的。我們對這些系統如何運作不是一無所知，這不是真的。技術會以某種nano秒變成無限強大、然後接管世界，這不是真的。沒有辦法防禦，這不是真的。」

「這些都是編造出來的，而且編造的方式很不幸地傷害到你們所有人。你們在學電腦科學，你們希望畢業時大家還在乎電腦。」

「我們想創造一個對你們正在學習掌握的技術感到樂觀的未來。我們想確保每個人都從AI受益。每個人都該有AI。沒有人該有核彈。你們同意嗎？」

#美國學界缺compute是大學自己的問題
被追問美國學界拿不到compute的問題，Huang的回答出乎意料地直接。

「絕對是、絕對不是。問題是為什麼不是。晶片很多。如果Stanford校長下單，我保證我會交貨。我從沒聽說有人下單給我們，我們沒交貨。這不是真的。你必須下單。」

「真正的問題其實非常不同。Stanford需要compute，科學需要compute。根本問題是這個系統不再被建造來能交付massive scale的compute。」

「想想Stanford所有的研究部門，他們都在不同系所，各自募款、各自拿grant，沒人會分享自己的grant。但沒有一個grant大到能買一個夠大的compute、平常只用一部分、用的時候卻能很驚人。世界遠離了集中式的計算環境，轉向每個人都用筆電。這就是今天的計算環境，所有大學都一樣，Stanford不是孤例。你們沒有10億美元的compute預算，它不存在。」

「但這是誰的錯？Stanford的錯。為什麼我要這麼說？因為當你說某件事是某人的錯，你就賦予了他們去解決的權力。」

「如果是我是Stanford，我就會找方法去改變預算方式、運算方式。你必須aggregate，為自己建一個campus-wide的supercomputer，就像Stanford過去建linear accelerator那樣。我們需要建大家共用的校園級超級電腦。」

「你也可以外包給別人做，那都是可能的。但你確實需要10億美元，需要一筆合理的資金去建這種東西，因為這就是它的成本。」

被問到Stanford有400億美元endowment，Huang的回答更直接：「我會立刻撥10億美元出來，當作雲端服務給每一個學生和研究員，讓他們有AI超級電腦可以用。我會馬上做。」

「當然你必須規劃。如果你想買10億美元的番茄，你不能跑去雜貨店然後說『啊，你扣留番茄不給我』，那很荒謬。所以你必須規劃，必須說明年我們需要10億美元的compute給Stanford，我們會去建。」

#CEO工作的本質：脆弱的職業
被問到CEO最好和最壞的部分，Huang給了一個少見的坦白回答。

「當你是CEO，你有幸做的事是你真的是那個必須構想vision、strategy、execution交集的人。你必須活在那個世界。當你的公司有能力，當你被驚人的電腦科學家圍繞、其中很多來自Stanford，當你被這樣的人圍繞，你有vision時它非常可實現。因為你跟驚人的人在一起，你的vision會更ambitious。」

關於不有趣的部分：「不有趣的部分。當公司表現不好的時候，或在早期我們還在找路的時候，我們大概有四五次差點倒閉。我是說真的差點倒閉，靠最後一口氣，或者被打趴在地上。那些時候，丟臉、屈辱、難受。你常常不知道答案是什麼，常常你在黑暗裡，你害怕。所有我們身為人類會有的感受都會被乘上1000倍、100萬倍。」

「當你是上市公司CEO，你的臉一直在外面。表現好的時候大家高興，表現不好的時候他們很快會告訴你。對我來說這是個非常脆弱的職業。」

#早期Nvidia最大的策略錯誤
被問到早期最大的錯誤，Huang先排除一個常見答案。

「任何熟悉我們歷史的人都會知道，我們第一代產品的架構、技術完全是錯的。不是有點錯，是完全錯。聰明的工程師、專業人士，我們有募到資，做出來這個東西，結果『欸看一下，它完全不能用』。」

「我們用曲面而不是三角形，沒有Z-buffer而是forward texture mapping而不是inverse texture mapping，沒有浮點數。我們什麼都做錯了。」

但他不認為這是真正的錯誤：「那些是技術上的錯誤選擇，但它導致了策略上的天才之舉。怎麼把一家有這種名聲、浪費一堆錢、用兩年半時間做錯方向、被競爭對手包圍的公司，變成今天唯一還在的那家？那個轉變教會我很多，技術很重要，但策略更重要。」

真正的策略錯誤是進入行動裝置市場：「PC或行動裝置起飛的時候，我們被行動領域很重要的公司接觸，要我們做一些行動裝置。我做的選擇是『不感興趣』應該才是答案。但我們決定把一堆資源轉去做行動裝置。」

「我以為我們能加很多價值，但如果我再多想幾步，以我們知道怎麼做、擅長做的事，能交付的價值大概頂多是邊際的。我把公司轉去做行動裝置，長成10億美元的事業。但接著在3G到4G轉換時，我們100%被鎖在外面。Qualcomm在那個轉換中是modem的領導者，那是手機最重要的部分，不是SoC，不是電腦繪圖，連application processor都不是。」

「我可以call it了。如果這種情況再發生一次，我會說『這幾年會是個有趣的機會，但之後我們會被鎖出去，那有什麼意義？我們把資源留給別的地方。』」

復原的方式是把那些低功耗、能效專業轉去當時不存在的應用：「我把所有那些極低功耗和energy efficiency的專業，全部轉去一個當時不存在的應用，叫robotics。Thor就是我們當年用在行動裝置那顆晶片的曾曾曾曾孫。整個世系所有的團隊、所有的專業，對今天到達這裡都很有幫助。」

「但這是合理化說法。當初進入那個市場本身是浪費時間，那才是策略錯誤。」

#在迷霧中做策略：先觀察、再回到第一性原理
關於如何在前景不明時做策略決定：「第一件事是『我觀察到什麼？』然後基於我觀察到的，讓我們reasoning back to first principles。把它全部拆開，問自己『所以接下來會發生什麼？』第一件事，這是個大事嗎？deep learning、computer vision、AlexNet，這是大事嗎？」

「大事的部分是天啊，這裡有兩個工程師，Alex和Ilya，當然還有Hinton，他們做了一個神經網路模型，砰，一擊就壓過所有電腦科學家幾十年來的電腦視覺能力。品質和效能的躍進是個大事。」

「下一個問題是接下來會發生什麼？這能走多遠？如果你能用這種方式做，還能解什麼？如果這能解一些很驚人的問題，這對電腦和computing意味著什麼？你就一直問自己這些問題，一路iterate到first principles。然後你對computing的未來建立mental model，它會在哪裡？能做什麼？」

「然後你建立一個未來的mental model，你公司在裡面會在哪裡，然後從那裡反推回來。」

關於可能犯錯：「當然你可能錯。常常如果你reasoning做得好，你不會完全錯，但也不會完全對。我傾向於很舒服地說：『這些事大概會發生，這些事一定會發生，這些事可能會發生。』基於這個，我們大致該往那個方向走，邊走邊感覺。」

「成功一路上的技巧是，你往這個方向走會耗能量、耗時間、耗錢，那個時間能量和錢都是從別的地方拿走的。追求一個策略的opportunity cost就是真正的成本。所以你必須問自己：怎麼聰明到能減少opportunity cost、增加optionality？」

「沒有簡單答案。很多時候你在試著讓旅程本身為自己付費。」
