---
post_id: "10227670187700461"
title: "Skills 的做法正在更新：一些讓 Skill 更有效的新方法，Simon Scrapes 指出，當 Claude 打開 skill 裡一份很長的 reference 檔案時，並不一定會把整份讀完。它會執行 head -100 指令，只讀前 100 行，用來判斷這份 reference 檔案是否真的包含它需要的資訊。因此，如果重要的規則放在第 100 行之後，對 Claude 來說，那些規則等於"
page_title: "股票"
source_page: "\u5f35\u7dad\u5cf0"
requested_url: "https://www.facebook.com/saved/?list_id=10222174769398438&referrer=SAVE_DASHBOARD_NAVIGATION_PANEL"
post_url: "https://www.facebook.com/jerry.chang.505523/posts/pfbid02zRfaY3CrPrVcqUtQdUV2x3kciDmpYuF6aErtxXvigDX9VbK8yygrBvw5mKFGYkLTl"
creation_time_utc: ""
fetched_at_utc: "2026-10-09T07:18:59.330789+00:00"
source: "saved_list"
---

# Skills 的做法正在更新：一些讓 Skill 更有效的新方法，Simon Scrapes 指出，當 Claude 打開 skill 裡一份很長的 reference 檔案時，並不一定會把整份讀完。它會執行 head -100 指令，只讀前 100 行，用來判斷這份 reference 檔案是否真的包含它需要的資訊。因此，如果重要的規則放在第 100 行之後，對 Claude 來說，那些規則等於不存在。他參考的檔案是官方的Skills best practices

來源：\u5f35\u7dad\u5cf0
原文連結: https://www.facebook.com/jerry.chang.505523/posts/pfbid02zRfaY3CrPrVcqUtQdUV2x3kciDmpYuF6aErtxXvigDX9VbK8yygrBvw5mKFGYkLTl
Skills 的做法正在更新：一些讓 Skill 更有效的新方法，Simon Scrapes 指出，當 Claude 打開 skill 裡一份很長的 reference 檔案時，並不一定會把整份讀完。它會執行 head -100 指令，只讀前 100 行，用來判斷這份 reference 檔案是否真的包含它需要的資訊。因此，如果重要的規則放在第 100 行之後，對 Claude 來說，那些規則等於不存在。他參考的檔案是官方的Skills best practices

Skills 在今年年初推出，當時大家學到的做法是：寫好 description、總行數控制在 200 行以內、把 reference 檔案分開放、並且把內容寫成一組指令。但現在規則已經完全改變。如果 reference 檔案超過 100 行，又沒有 content list，被正確使用的機率其實偏低。

Anthropic 也更新了他們的 best practice guide，新增六條類似的規則，而且這些規則適用於所有已經建好的 skill。把這些規則做對，不論由哪個模型來執行，skill 都能給出更穩定的結果。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 第一條：Content Lists

第一條規則是在任何超過 100 行的 reference 檔案最上方放一份 content list，也就是類似目錄的索引。這樣 Claude 可以讀完整份檔案，或是直接跳到它需要的那個段落。

Anthropic 自己的範例是一份 API reference。檔案最上方是 contents，下面列出五行：authentication and setup、core methods、advanced features、error handling patterns、code examples。接著每一個段落依序放在 contents 之後，例如 authentication and setup 這一段就在下方。

做法很簡單：進入 Claude Code 或 Cowork（Cowork 現在已經和 chat 合併，所以是 Claude Code 或 Chat），逐一檢查 .claude/skills 資料夾裡的每個 skill。找出所有超過 100 行的 reference 檔案，在最上方加上與標題相符的 content list，就完成了。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 第二條：Degrees of Freedom

Simon 表示，這一條徹底改變了他看待 skill 的方式。以前他把每個 skill 都當成需要相同細節程度，盡可能給出同樣精確的指令。但現實中的商業流程並不是這麼非黑即白。

Anthropic 的說法是，skill 裡的細節程度，應該取決於任務有多脆弱、變化有多大。他們稱之為設定適當的 degrees of freedom，共分三個層級。

高 freedom 是純文字指令。Anthropic 的範例是 code review 流程：檢查結構、找出 bug、針對可讀性與可維護性提出改善建議，再確認是否符合專案慣例。做 code review 有很多好方法，哪一種合適要看實際的程式碼，所以 Claude 只拿到目標，其餘由它自己判斷。這些模型夠聰明，能自行找出達成目標的方式。對不寫程式的企業主來說，這可能是檢討一通銷售電話，或是撰寫一則 LinkedIn 貼文。這類任務屬於高 degrees of freedom，用純文字描述，做法可以保持模糊。

中 freedom 是帶有不同設定的 template。Anthropic 的範例 template 設有不同選項，例如是否包含圖表（true 或 false），輸出格式可以是 markdown、HTML 或其他格式。也就是說，中 freedom 有一個偏好的形狀，是一份允許部分變化的 template，有些變化是可以接受的。例如每週的客戶報告就屬於這一類。

低 degrees of freedom 則用於操作非常脆弱、容易出錯的情況。這時必須非常一致，並且必須遵循特定順序。可以把低 degrees of freedom 想成一條精確的指令。Anthropic 的範例是資料庫 migration，指令內容是：精確地執行這個 script，不要修改指令，不要加任何 flag。對一般使用者來說，只要牽涉金錢或刪除資料的事情都屬於這一類，例如開立發票、移除會員。這些情境需要嚴格遵守，因此會給一個固定的 script，或是只留下很少甚至沒有可變動的參數。

Simon 從這些規則中歸納出三個重點。第一，同一個 skill 可以混用不同層級。例如發票 skill 裡的撰寫內容步驟可以是高 degrees of freedom，而建立發票的步驟則可以鎖得很死，採用低 degrees of freedom。

第二，針對每一個步驟，要問的問題是：如果 Claude 用不同的方式做，會發生什麼事？如果答案是影響不大，就可以給更高的 degrees of freedom，放寬限制。但如果會造成重大後果，就必須給低 degrees of freedom。

第三，低 freedom 通常代表的是 script，而不是更多的純文字說明。有了 script，就能讓 Claude 每一次都用完全相同的方式完成同一件事。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 第三條：先在每個模型上測試

第三條聽起來理所當然，但實際上幾乎沒有人在做。撰寫與測試 skill 時，多半只用一個模型，可能選了 Sonnet、Opus，或是新的 Fable 系列模型，通常就是當月最新的那一個。Simon 坦承自己有時也會這樣做。但 Anthropic 指出，skill 的結果取決於底層的模型，這其實相當顯而易見。因此，需要在打算使用的每一個模型上測試，並依照該模型所需的細節程度來撰寫 skill。

而合適的細節程度已經有很大的改變。大約 6 到 8 個月前，一些較舊的模型會跳過步驟，所以當時的做法是寫編號清單，並用大寫字母強調重點，例如 important。現在對於部分較新的高階推理模型，情況完全相反。Fable 5 guide 提到，為舊模型開發的 skill 對它來說往往過於 prescriptive，甚至可能讓輸出變差。因此 Anthropic 建議，如果模型在沒有那些舊指令時表現更好，就把它們移除。

不過，一些較小的模型，例如較早期的 Sonnet 模型，進步幅度並沒有那麼大。所以 best practices 頁面針對每個模型提供一個問題。測試不同模型時，對 Claude Haiku 要問的是：這個 skill 對 Haiku 來說，提供的引導是否足夠？對 Sonnet 要問的是：這個 skill 是否清楚且有效率？對 Opus 要問的是：這個 skill 是否避免了過度解釋？不同模型需要不同程度的細節，所以除非只打算搭配某個特定模型，否則 skill 必須落在對這三者都適用的位置。

Simon 強烈建議，把最常用的 skill 用同一個任務依序在 Haiku、Opus、Sonnet 上各跑一次。如果 Haiku 漏掉某個步驟，那個步驟要不是需要寫得更清楚，就是應該改成 script，也就是給它低 degrees of freedom。因為 script 在每一個模型上的執行結果都相同。

另外，如果 Opus 在同一個任務上，使用 skill 的表現比沒有 skill 時更差，就要開始從 skill 中刪減指令，直到 Opus 的表現變好為止。而且如果打算分享這些 skill，記得在 YAML front matter（也就是 skill 開頭的那個區塊）寫明這個 skill 預期搭配哪些模型使用。

接下來的規則，是關於 skill 的檔案如何配置，以及它如何檢查自己的工作。首先從檔案巢狀結構開始，也就是在 skill 裡嵌套 reference 檔案時不該怎麼做。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 第四條：Nested References

Anthropic 表示，SKILL.md 的主體應該保持在 500 行以內，並把它當成其他所有內容的目錄頁。當內容接近這個上限時，建議拆分成獨立的檔案。這正是 nesting 出現的地方：既然拆成了不同的 reference 檔案，就必須從 SKILL.md 指向這些檔案。

Anthropic 的範例是一個 PDF skill。SKILL .md 放指令，旁邊有一份 forms guide 和一份 reference guide，前者說明如何填寫表單的範例，後者是 API reference。Claude 在讀這個 skill 時，只有在某個步驟需要時，才會打開 reference 檔案與 forms 檔案。

實際的 skill 目錄結構大致如下：PDF skill 底下有 SKILL .md 檔案、forms.md（表單填寫指南）、reference（API reference）、examples，以及獨立的 scripts 資料夾。這些 scripts 就是低 degrees of freedom 的所在，需要它們被精確且一致地照原樣執行。值得注意的是，scripts 是被執行的，並不會被讀進記憶體，所以 Claude 不會在這些 scripts 上耗用任何 context。

Anthropic 接著提供更多 skill 配置的建議：當一個 skill 涵蓋多個領域時，應依領域拆分 reference。他們的範例是一個資料 skill，分別有 finance、sales、product 與 marketing 的獨立檔案，因此詢問營收的問題永遠不會載入 marketing.md 檔案。同理，如果是客戶報告的 skill，就可以一個客戶一個檔案。

接著談 nested references。這就是開頭提到的 head -100 問題發揮作用之處。如果 SKILL.md 指向 advance.md，而 advance.md 又指向 details.md，Claude 比較可能只預覽 advance.md。結果位於鏈條最底端的 details.md 資訊，只會被讀到一部分。

解法是讓每一個 reference 檔案都直接從 SKILL.md 連結，只往下一層。Anthropic 建議把所有 references 保持在距離 SKILL.md 一層的深度。做法是打開 SKILL.md，列出它指向的每一個檔案，找出任何只能透過另一個檔案才能到達的檔案，這件事也可以請 Claude 代勞。然後確保這些檔案全部直接從 SKILL.md 連結出去。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 第五條：使用 Checklists

下一條規則是替較長的流程提供一份完整的 checklist，因為 Claude 其實很喜歡這個做法。對於這些複雜的工作、複雜的 skill，Anthropic 建議把工作拆成步驟，並給 Claude 一份 checklist，讓它複製到回覆中，並在進行時逐項勾選。以其中的 research progress 為例，五個不同的步驟被寫成一份 checklist。

這聽起來似乎與 Anthropic 更新後的 prompting 建議相反，後者主張把整個任務交給模型，而不是給出 prescriptive 的步驟，但其實並不矛盾。步驟適用於順序真的重要的情況，例如先檢查資料，再根據資料建立報告。如果順序並不重要，就仍然不需要 checklist。

Anthropic 的範例沒有使用任何程式碼，是一個 research synthesis 工作流程，checklist 只有五行，而且不是非常 prescriptive。像是 read all source documents（閱讀所有來源文件）、identify key themes（找出關鍵主題），只給目標，仍然留有模糊空間。每個步驟下方再附上一小段說明。

其中最值得指出的是第五步 verify citations（驗證引用）：檢查每一項主張是否引用了正確的來源文件，如果引用不完整，就回到第三步。這句「回到第三步」，就是防止 Claude 把失敗的步驟勾選起來然後繼續往下走的關鍵。這實際上就是 self-verification，也屬於下一條規則的一部分，也就是讓 skill 具備自我回饋的機制，修正自己的行動方向。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 第六條：Self-Correction Loops

Anthropic 針對 skill 輸出驗證提出的模式是：執行一項或一組檢查，修正錯誤，然後重複這些步驟，直到通過為止。他們表示，這會大幅提升輸出品質。而且檢查本身不一定要是程式碼。

在他們的第一個範例中，檢查依據基本上是一份 style guide。Claude 先起草，再對照 guide 審查草稿，標註每一個問題以及它違反的段落，然後修訂，再審查一次，只有全部通過才會定稿。對一般使用者來說，這份 style guide 可以是自己的 brand voice 文件，拿來檢查與驗證輸出。

這也是 skill 開始自我改進的流程。當某份草稿因為 voice 文件裡還沒有的原因而未通過時，可以讓 Claude 在這次執行結束時建議一條新規則。使用者核准這條規則後，它就會寫進文件，下一次執行就會依照這條新規則檢查。Fable 5 guide 也明確指出，這個模型擅長根據在任務中學到的內容來更新 skills。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 第七條：Dependencies

最後一條規則是以可攜性為前提來建置 skill。現在也許只有自己一個人在 Claude 上工作，但如果同事安裝了每天使用的 skill，會發生什麼事？它幾乎一定會在第一天就壞掉。

原因是，建置的 skill 在自己的筆電上能運作，是因為半年前已經安裝了所有 dependencies 和函式庫，而且早就忘了裡面包含哪些 dependencies。但在同事的電腦上，或是全新的 Claude Code 與 Cowork session 裡，這些東西並不存在，dependency 需要先被安裝。

這條規則是：不要假設工具已經安裝。做得不好的例子是寫「使用 PDF library 處理檔案」。比較好的做法是在每個 skill 裡都寫類似「安裝所需的套件」這樣的句子，並附上套件名稱。因為如果已經安裝，它就會略過這個步驟，Claude 夠聰明，能理解套件已安裝並跳過。

對 skill 裡的每一個 script，都要把安裝指令放在該 script 旁邊。如果是要與團隊分享 skill，或是販售 skill，這會是一個天差地別的差異：一個是第一天就能運作的 skill，另一個則是需要協助設定，甚至需要持續維護的 skill。

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
▍ 總結

把這些整合起來，就是一整組新規則。超過 100 行的長檔案要有 content list。同一個 skill 可以使用多種 degrees of freedom。要在實際使用的模型上測試，並把模型記錄在 skill 的 front matter 裡。references 只放一層深。要有 checklist。要有 feedback loop。dependencies 要在 skill 裡明確寫出來。

Simon 也提到，這些修正大多與 skill 裡的文字措辭無關。他認為，skill 的品質越來越取決於檔案如何配置，以及它執行哪些檢查，遠多於指令寫得好不好，尤其是在模型越來越擅長理解不同目標、並為自己產生指令的情況下。
