#!/usr/bin/env python3
"""生成 Units 18-25 学习材料与测试题 HTML"""

import os

HTML_DIR = "/home/xmren/Documents/ebooks/karina book/F2/english/grammar/study_materials/html"

NAV = """<nav class="top-nav"><div class="top-nav-inner">
<a href="index.html" class="logo">📚 Grammar <span>F2</span></a>
<ul class="nav-links">
<li><a href="index.html">首頁</a></li>
<li><a href="unit1_study.html">U1</a></li><li><a href="unit1_test.html">U1測</a></li>
<li><a href="unit2_study.html">U2</a></li><li><a href="unit2_test.html">U2測</a></li>
<li><a href="unit3_study.html">U3</a></li><li><a href="unit3_test.html">U3測</a></li>
<li><a href="unit4_study.html">U4</a></li><li><a href="unit4_test.html">U4測</a></li>
<li><a href="unit5_study.html">U5</a></li><li><a href="unit5_test.html">U5測</a></li>
<li><a href="unit6_review.html">U6</a></li>
<li><a href="unit7_study.html">U7</a></li><li><a href="unit7_test.html">U7測</a></li>
<li><a href="unit8_study.html">U8</a></li><li><a href="unit8_test.html">U8測</a></li>
<li><a href="unit9_study.html">U9</a></li><li><a href="unit9_test.html">U9測</a></li>
<li><a href="unit10_study.html">U10</a></li><li><a href="unit10_test.html">U10測</a></li>
<li><a href="unit11_study.html">U11</a></li><li><a href="unit11_test.html">U11測</a></li>
<li><a href="unit12_study.html">U12</a></li><li><a href="unit12_test.html">U12測</a></li>
<li><a href="unit13_study.html">U13</a></li><li><a href="unit13_test.html">U13測</a></li>
<li><a href="unit14_study.html">U14</a></li><li><a href="unit14_test.html">U14測</a></li>
<li><a href="unit15_study.html">U15</a></li><li><a href="unit15_test.html">U15測</a></li>
<li><a href="unit16_study.html">U16</a></li><li><a href="unit16_test.html">U16測</a></li>
<li><a href="unit17_study.html">U17</a></li><li><a href="unit17_test.html">U17測</a></li>
<li><a href="unit18_study.html">U18</a></li><li><a href="unit18_test.html">U18測</a></li>
<li><a href="unit19_study.html">U19</a></li><li><a href="unit19_test.html">U19測</a></li>
<li><a href="unit20_study.html">U20</a></li><li><a href="unit20_test.html">U20測</a></li>
<li><a href="unit21_study.html">U21</a></li><li><a href="unit21_test.html">U21測</a></li>
<li><a href="unit22_study.html">U22</a></li><li><a href="unit22_test.html">U22測</a></li>
<li><a href="unit23_study.html">U23</a></li><li><a href="unit23_test.html">U23測</a></li>
<li><a href="unit24_study.html">U24</a></li><li><a href="unit24_test.html">U24測</a></li>
<li><a href="unit25_study.html">U25</a></li><li><a href="unit25_test.html">U25測</a></li>
</ul></div></nav>"""

FOOTER = '<footer><p>F2 English Grammar &copy; 互動學習平台 &mdash; 祝考試順利！🎯</p></footer>'

def head(title, active):
    return f'''<!DOCTYPE html><html lang="zh-Hans"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title><link rel="stylesheet" href="css/style.css">
<style>.nav-links a[href="{active}"]{{background:rgba(255,255,255,0.15);color:#fff!important}}</style>
</head><body>{NAV}<div class="container">'''
def tail(): return f'</div>{FOOTER}<script src="js/script.js"></script></body></html>'
def card(c): return f'<div class="card">{c}</div>'
def table(h,rows): return f'<div class="table-wrap"><table><thead><tr>{"".join(f"<th>{x}</th>" for x in h)}</tr></thead><tbody>{"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)}</tbody></table></div>'
def callout(t,l,text): return f'<div class="callout {t}"><strong>{l}</strong><p>{text}</p></div>'

def mc_q(n,stem,opts,ans):
    o="".join(f'<label><input type="radio" name="q{n}" value="{l}"> {l}. {t}</label>' for l,t in opts)
    return f'<div class="question" data-correct="{ans}"><p><strong>{n}.</strong> {stem}</p><div class="options">{o}</div><div class="answer-reveal" style="display:none;margin:8px 0;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ 答案：<strong>{ans}</strong></div></div>'

def fill_q(n,stem,ans):
    return f'<div class="question" data-correct="{ans}"><p><strong>{n}.</strong> {stem}</p><input type="text" class="fill-input" placeholder="輸入答案..." style="width:80%;padding:8px 12px;border:2px solid #e2e8f0;border-radius:6px;font-size:0.95rem;"><div class="answer-reveal" style="display:none;margin:8px 0;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ 答案：<strong>{ans}</strong></div></div>'

def err_q(n,stem,ans):
    return f'<div class="question" data-answer="{ans}"><p><strong>{n}.</strong> {stem}</p><div class="answer-reveal" style="display:none;margin:8px 0;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {ans}</div></div>'

def btns():
    return '''<div style="display:flex;gap:12px;flex-wrap:wrap;margin:24px 0;padding:16px;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
<button id="btn-show-answers" style="padding:10px 20px;background:#2563eb;color:#fff;border:none;border-radius:6px;cursor:pointer;">📖 顯示答案</button>
<button id="btn-hide-answers" style="padding:10px 20px;background:#64748b;color:#fff;border:none;border-radius:6px;cursor:pointer;">🙈 隱藏答案</button>
<button id="btn-calc-score" style="padding:10px 20px;background:#16a34a;color:#fff;border:none;border-radius:6px;cursor:pointer;">📊 計分</button>
<div id="score-box" style="display:none;padding:12px 20px;background:#f0fdf4;border-radius:6px;border:1px solid #16a34a;">
<p style="margin:0;font-size:1.1rem;">得分：<span class="score-num" style="font-weight:700;color:#16a34a;font-size:1.3rem;">—</span></p>
<p style="margin:4px 0 0;font-size:0.9rem;color:#64748b;"><span class="score-detail">0/0</span></p></div></div>'''

# ========== UNIT 18: Reported Speech (Orders/Requests) ==========
def u18_study():
    c=card('<h1>Unit 18: Reported Speech — Orders & Requests（報告命令與請求）</h1><p>將別人說的話轉述出來，尤其是命令、指示和請求。</p>')
    c+=card('<h2>18.1 基本結構</h2><p>報告命令/請求的結構：<strong>verb + noun/pronoun + to-infinitive</strong></p>'+table(["動詞","用法","例句"],[["tell","告訴某人做","He told me to wait."],["ask","請求某人做","She asked us to help."],["command","命令","The general commanded them to attack."],["instruct","指示","The policeman instructed the driver to stop."],["order","命令","The officer ordered them to leave."],["request","正式請求","He requested everyone to remain seated."]]))
    c+=card('<h2>18.2 直接引語 vs 間接引語</h2>'+table(["直接引語 (Direct)","間接引語 (Reported)"],[['"Please say hello to your sister," said Helen.','Helen asked Paul to say hello to his sister.'],['"Get out of the car!" the policeman said.','The policeman ordered/instructed the driver to get out of the car.'],['"Please don\'t be late," said Mum.','Mum asked me not to be late.'],['"Don\'t run in the corridor," the teacher said.','The teacher told us not to run in the corridor.']]))
    c+=callout("danger","⚠️ 要點","否定命令/請求：tell/ask + not + to-infinitive<br>✗ \"Don't run\" → He told us don't run. → ✓ He told us <strong>not to run</strong>.")
    c+=card('<h2>考核要點 ✅</h2><ol><li>報告命令/請求：動詞 + 人 + to-infinitive</li><li>常用動詞：tell, ask, order, command, instruct, request</li><li>否定式：tell/ask + not + to-infinitive</li></ol>')
    return head("Unit 18 — Reported Speech (Orders)", "unit18_study.html")+c+tail()

def u18_test():
    mc=[(1,'"Please sit down," the teacher said. → The teacher ______ us to sit down.',[("A","said"),("B","told"),("C","spoke"),("D","talked")],"B"),
        (2,'"Don\'t be late," Mum said. → Mum asked me ______ late.',[("A","don\'t be"),("B","not be"),("C","not to be"),("D","to not be")],"C"),
        (3,'"Get out of the car!" → The policeman ______ the driver to get out.',[("A","said"),("B","asked"),("C","ordered"),("D","requested")],"C"),
        (4,'"Please help me," she said. → She ______ me to help her.',[("A","said"),("B","told"),("C","asked"),("D","ordered")],"C"),
        (5,'"Don\'t run in the corridor!" → The teacher told us ______ in the corridor.',[("A","don\'t run"),("B","not run"),("C","not to run"),("D","to not run")],"C"),
        (6,'"Stay where you are!" → The officer ______ them to stay where they were.',[("A","said"),("B","commanded"),("C","spoke"),("D","talked")],"B"),
        (7,'"Please wait here," the receptionist said. → The receptionist requested us ______ here.',[("A","wait"),("B","to wait"),("C","waiting"),("D","waited")],"B"),
        (8,'"Don\'t touch the paintings," the guide said. → The guide instructed us ______ the paintings.',[("A","don\'t touch"),("B","not touch"),("C","not to touch"),("D","to not touch")],"C"),
        (9,'"Finish your homework first," Mum said. → Mum told me ______ my homework first.',[("A","finish"),("B","to finish"),("C","finishing"),("D","finished")],"B"),
        (10,'"Don\'t forget your keys," Dad said. → Dad reminded me ______ my keys.',[("A","don\'t forget"),("B","not forget"),("C","not to forget"),("D","to not forget")],"C")]
    fills=[(11,'"Please sit down" → The teacher asked us _______________.',"to sit down"),(12,'"Don\'t be late" → Mum told me _______________.',"not to be late"),(13,'"Get out of the car!" → The policeman ordered the driver _______________.',"to get out of the car"),(14,'"Please help me" → She asked him _______________.',"to help her"),(15,'"Finish your homework" → Dad told me _______________.',"to finish my homework"),(16,'"Don\'t touch the paintings" → The guide instructed us _______________.',"not to touch the paintings"),(17,'"Wait here" → The receptionist asked us _______________.',"to wait here"),(18,'"Don\'t run" → The teacher told the students _______________.',"not to run"),(19,'"Stay where you are" → The officer commanded them _______________.',"to stay where they were"),(20,'"Don\'t forget your keys" → Dad reminded me _______________.',"not to forget my keys")]
    errs=[(21,'She told me don\'t be late.',"She told me not to be late."),(22,'He asked to me wait.',"He asked me to wait."),(23,'The teacher said us to sit down.',"The teacher told us to sit down."),(24,'Mum asked don\'t run.',"Mum asked me not to run."),(25,'He ordered to them leave.',"He ordered them to leave.")]
    content=card("<h1>Unit 18: Reported Speech (Orders) — Practice Test</h1><p><strong>總分：100分 | 時限：35分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'"Please wait here." (用ask) → She _______________',"asked me to wait here"),(27,'"Don\'t be late." (用tell) → He _______________',"told me not to be late"),(28,'"Finish your work." (用instruct) → The boss _______________',"instructed me to finish my work"),(29,'"Don\'t run." (用tell) → The teacher _______________',"told us not to run"),(30,'"Stay where you are." (用order) → The officer _______________',"ordered them to stay where they were")]))
    content+=card(btns())
    return head("Unit 18 — Practice Test", "unit18_test.html")+content+tail()

# ========== UNIT 19: Reported Speech (Offers/Suggestions) ==========
def u19_study():
    c=card('<h1>Unit 19: Reported Speech — Offers, Suggestions & Advice</h1><p>轉述提議、建議、忠告等。</p>')
    c+=card('<h2>19.1 報告提議/拒絕/同意</h2><p>結構：<strong>agree/offer/promise/refuse + to-infinitive</strong></p>'+table(["動詞","例句"],[["agree + to-inf","He agreed to help me."],["offer + to-inf","Brian offered to take Sally home."],["promise + to-inf","She promised to come early."],["refuse + to-inf","He refused to pay."]]))
    c+=card('<h2>19.2 報告建議/忠告</h2><p>結構：<strong>advise/caution/recommend/remind + object + to-infinitive</strong></p><ul><li>"You should drink plenty of water." → The doctor advised Melinda <strong>to drink</strong> plenty of water.</li><li>"Don\'t go out alone at night." → Dad cautioned me <strong>not to go</strong> out alone at night.</li></ul>')
    c+=card('<h2>19.3 suggest 的特殊用法</h2><p>suggest 有兩種結構：</p>'+table(["結構","例句"],[["suggest + that + 從句","Lily suggested that we (should) go for a swim."],["suggest + -ing","Lily suggested going for a swim."]])+callout("danger","⚠️ 注意","✗ He suggested me to go. → ✓ He suggested that I (should) go. / ✓ He suggested going."))
    c+=card('<h2>考核要點 ✅</h2><ol><li>offer/agree/promise/refuse + to-infinitive</li><li>advise/caution/recommend/remind + 人 + to-infinitive</li><li>suggest + that 從句 / suggest + -ing（不能說 suggest sb to do）</li></ol>')
    return head("Unit 19 — Reported Speech (Offers)", "unit19_study.html")+c+tail()

def u19_test():
    mc=[(1,'Brian offered ______ Sally home.',[("A","take"),("B","to take"),("C","taking"),("D","took")],"B"),
        (2,'The doctor advised Melinda ______ plenty of water.',[("A","drink"),("B","to drink"),("C","drinking"),("D","drank")],"B"),
        (3,'Lily suggested ______ for a swim.',[("A","go"),("B","to go"),("C","going"),("D","went")],"C"),
        (4,'He refused ______ for the damage.',[("A","pay"),("B","to pay"),("C","paying"),("D","paid")],"B"),
        (5,'She promised ______ early.',[("A","come"),("B","to come"),("C","coming"),("D","came")],"B"),
        (6,'Dad cautioned me ______ out alone at night.',[("A","don\'t go"),("B","not go"),("C","not to go"),("D","to not go")],"C"),
        (7,'He agreed ______ me.',[("A","help"),("B","to help"),("C","helping"),("D","helped")],"B"),
        (8,'She reminded me ______ my keys.',[("A","don\'t forget"),("B","not forget"),("C","not to forget"),("D","forget")],"C"),
        (9,'He recommended ______ the early train.',[("A","take"),("B","to take"),("C","taking"),("D","took")],"C"),
        (10,'She suggested that we ______ early.',[("A","leave"),("B","left"),("C","leaving"),("D","to leave")],"A"),
    ]
    fills=[(11,'Brian offered _______________ (take) Sally home.',"to take"),(12,'The doctor advised me _______________ (drink) more water.',"to drink"),(13,'Lily suggested _______________ (go) for a swim.',"going"),(14,'He refused _______________ (pay).',"to pay"),(15,'She promised _______________ (come) early.',"to come"),(16,'Dad cautioned me _______________ (not/go) out alone.',"not to go"),(17,'He agreed _______________ (help) me.',"to help"),(18,'She recommended _______________ (take) the early train.',"taking"),(19,'He suggested that we _______________ (go) early.',"go || should go"),(20,'I advised him _______________ (see) a doctor.',"to see")]
    errs=[(21,'Brian offered taking Sally home.',"Brian offered to take Sally home."),(22,'He suggested me to go swimming.',"He suggested going swimming. / He suggested that we go swimming."),(23,'She promised coming early.',"She promised to come early."),(24,'Dad cautioned me don\'t go out alone.',"Dad cautioned me not to go out alone."),(25,'He refused paying for the damage.',"He refused to pay for the damage.")]
    content=card("<h1>Unit 19: Reported Speech (Offers) — Test</h1><p><strong>總分：100分 | 時限：35分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'"I will help you" (用offer) → He _______________',"offered to help me"),(27,'"You should rest" (用advise) → The doctor _______________',"advised me to rest"),(28,'"Let\'s go swimming" (用suggest) → She _______________',"suggested going swimming || suggested that we go swimming"),(29,'"I won\'t pay" (用refuse) → He _______________',"refused to pay"),(30,'"I\'ll be on time" (用promise) → She _______________',"promised to be on time")]))
    content+=card(btns())
    return head("Unit 19 — Practice Test", "unit19_test.html")+content+tail()

# ========== UNIT 20: Adverbs & Adverbials ==========
def u20_study():
    c=card('<h1>Unit 20: Adverbs and Adverbials（副詞與副詞結構）</h1><p>用副詞和副詞結構表達動作發生的時間、地點和方式。</p>')
    c+=card('<h2>20.1 Adverbs of Time & Place（時間與地點副詞）</h2>'''+table(["結構","時間","地點","例句"],[["單字","now, yesterday","here, there","She is leaving now. I lived here."],["介詞短語","on 24 August","in this building","She is leaving on 24 August."],["從句","when she finished","where I was born","She left when she had finished."]]))
    c+=card('<h2>20.2 時間從句</h2><p>可用 as soon as, before, after, (just) as, while, until 引導時間從句。</p><ul><li>She\'ll leave <strong>as soon as</strong> she gets her visa.</li><li>The phone rang <strong>(just) as</strong> I was leaving.</li><li>He broke his leg <strong>while</strong> playing badminton.</li></ul>')
    c+=card('<h2>20.3 Adverbs of Manner（方式副詞）</h2><p>多數方式副詞由 adj + -ly 構成。但 friendly, lovely, lonely 等以 -ly 結尾的是<strong>形容詞</strong>！</p>'+table(["形容詞","副詞"],[["fluent","speak fluently"],["careful","do carefully"],["friendly (adj!)","treat us in a friendly way"]]))
    c+=card('<h2>20.4 副詞的排列順序</h2><p>一般順序：<strong>方式 + 地點 + 時間</strong></p><ul><li>The children are playing <strong>happily in the park</strong>.</li><li>I slept <strong>very well last night</strong>.</li></ul><p>移動動詞（come, go, walk）後：<strong>地點 + 方式 + 時間</strong></p><ul><li>He went <strong>home quickly after school</strong>.</li></ul>')
    c+=card('<h2>20.5 like vs as</h2><ul><li><strong>like</strong>（介詞）+ 名詞/代詞：Don\'t behave like a child. He looks like Tim.</li><li><strong>as</strong>（連接詞）+ 從句：Please draw it as I described it to you.</li></ul>')
    c+=card('<h2>考核要點 ✅</h2><ol><li>時間從句：as soon as, while, until, before, after, (just) as</li><li>方式副詞：adj + -ly；但 friendly/lovely/lonely 是 adj</li><li>順序：方式+地點+時間；移動動詞：地點+方式+時間</li><li>like + 名詞；as + 從句</li></ol>')
    return head("Unit 20 — Adverbs", "unit20_study.html")+c+tail()

def u20_test():
    mc=[(1,'She always does her homework ______.',[("A","careful"),("B","carefully"),("C","care"),("D","careless")],"B"),
        (2,'He broke his leg ______ he was playing badminton.',[("A","during"),("B","while"),("C","until"),("D","as soon as")],"B"),
        (3,'Don\'t behave ______ a child.',[("A","as"),("B","like"),("C","similar"),("D","alike")],"B"),
        (4,'She is leaving ______ 24 August.',[("A","in"),("B","on"),("C","at"),("D","by")],"B"),
        (5,'The local people are very ______ to visitors.',[("A","friendly"),("B","friendly"),("C","friendlily"),("D","friend")],"A"),
        (6,'He speaks English ______.',[("A","fluent"),("B","fluently"),("C","fluency"),("D","more fluent")],"B"),
        (7,'The phone rang ______ I was leaving.',[("A","just as"),("B","until"),("C","as soon as"),("D","while")],"A"),
        (8,'Please draw it ______ I described it.',[("A","like"),("B","as"),("C","alike"),("D","similar")],"B"),
        (9,'She\'ll leave ______ she gets her visa.',[("A","as soon as"),("B","until"),("C","while"),("D","like")],"A"),
        (10,'He went home quickly ______ school.',[("A","before"),("B","after"),("C","until"),("D","while")],"B")]
    fills=[(11,'She always does her homework _______________ (careful → 副詞).',"carefully"),(12,'He speaks English _______________ (fluent → 副詞).',"fluently"),(13,'The children are playing _______________ (happy) in the park.',"happily"),(14,'He broke his leg _______________ (當) playing badminton.',"while"),(15,'Don\'t behave _______________ (像) a child.',"like"),(16,'Please draw it _______________ (按照) I described it.',"as"),(17,'She\'ll leave _______________ (一⋯就) she gets her visa.',"as soon as"),(18,'The phone rang _______________ (正當) I was leaving.',"just as"),(19,'He went _______________ (回家) quickly after school.',"home"),(20,'I slept very _______________ (好) last night.',"well")]
    errs=[(21,'She speaks English fluent.',"She speaks English fluently."),(22,'Don\'t behave as a child.',"Don\'t behave like a child."),(23,'He broke his leg during he was playing.',"while he was playing"),(24,'The local people are friendlily.',"friendly (adj)"),(25,'She is leaving in 24 August.',"on 24 August")]
    content=card("<h1>Unit 20: Adverbs — Practice Test</h1><p><strong>總分：100分 | 時限：35分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'He is a careful driver. He drives _______________',"carefully"),(27,'She is a fluent speaker. She speaks _______________',"fluently"),(28,'I left. Then she called me. (用 when) → She called _______________',"when I left"),(29,'He behaves like a child. Don\'t _______________',"behave like a child"),(30,'Please draw it according to my description. (用 as) → Draw it _______________',"as I described it")]))
    content+=card(btns())
    return head("Unit 20 — Practice Test", "unit20_test.html")+content+tail()

# ========== UNIT 21: Modal Verbs (Advice & Possibility) ==========
def u21_study():
    c=card('<h1>Unit 21: Modal Verbs — Advice & Possibility（情態動詞：建議與可能性）</h1>')
    c+=card('<h2>21.1 給予建議</h2>'+table(["情態動詞","用法","例句"],[["should","一般建議","You should drink more water."],["ought to","與 should 相似","You ought to see a doctor."],["had better (not)","強烈/緊急建議","You\'d better stop texting. You\'d better not forget."],["must","非常強烈的建議","You must take this course."],["can/could","提出可能解決方案","You can borrow mine."]]))
    c+=card('<h2>21.2 其他建議表達</h2>'+table(["表達方式","例句"],[["It\'s a good idea to...","It\'s a good idea to attend more practice sessions."],["It is advised/recommended that...","It is recommended that you (should) pack warm clothes."],["Let\'s...","Let\'s go to the beach."],["Why not / Why don\'t you...","Why not save up for a new laptop?"],["Shall we...","Shall we postpone the presentation?"],["How about / What about...","How about naming your dog Fluffy?"],["If I were you...","If I were you, I would take the MTR."]]))
    c+=card('<h2>21.3 可能性（Present/Future）</h2>'+table(["情態動詞","可能性","例句"],[["may/might","也許（低-中）","I may/might finish it by tomorrow."],["could","可能（較不確定）","There could be one in my drawer."],["should","應該（相當確定）","She should be here by now."],["must","一定是（非常確定）","He must be at home."],["can\'t","不可能是（否定）","That can\'t be true."]]))
    c+=card('<h2>21.4 可能性（Past）</h2>'+table(["結構","含義","例句"],[["may/might have + V-ed₂","過去也許","The AC may have stopped working."],["could have + V-ed₂","過去可能","She could have taken the wrong bus."],["should have + V-ed₂","本該","You should have received it yesterday."],["must have + V-ed₂","過去一定","He must have forgotten."],["can\'t have + V-ed₂","過去不可能","She can\'t have left already."]]))
    c+=card('<h2>考核要點 ✅</h2><ol><li>should/ought to/had better/must 強度遞增</li><li>had better (not) + 原形動詞（緊急建議）</li><li>suggest/recommend + that 從句或 -ing</li><li>If I were you... (Type 2 條件句)</li><li>should = 預期；must = 肯定；can\'t = 不可能</li><li>may have / could have / must have + V-ed₂（過去推測）</li></ol>')
    return head("Unit 21 — Modal Verbs", "unit21_study.html")+c+tail()

def u21_test():
    mc=[(1,'You look pale. You ______ see a doctor.',[("A","had better"),("B","had better to"),("C","have better"),("D","would better")],"A"),
        (2,'I\'ve bought the tickets. You ______ forget about our date.',[("A","had better not"),("B","hadn\'t better"),("C","better not to"),("D","had not better")],"A"),
        (3,'Where is Joey? She ______ be here by now.',[("A","can"),("B","should"),("C","mustn\'t"),("D","may")],"B"),
        (4,'The AC ______ have stopped working. It\'s very hot.',[("A","can"),("B","should"),("C","may"),("D","must")],"C"),
        (5,'He must ______ forgotten our meeting.',[("A","have"),("B","has"),("C","had"),("D","having")],"A"),
        (6,'You should ______ your exam results yesterday.',[("A","receive"),("B","to receive"),("C","have received"),("D","receiving")],"C"),
        (7,'If I ______ you, I would take the MTR.',[("A","am"),("B","was"),("C","were"),("D","be")],"C"),
        (8,'She can\'t ______ left already. It\'s only 4 p.m.',[("A","have"),("B","has"),("C","had"),("D","having")],"A"),
        (9,'______ we postpone the presentation?',[("A","Let\'s"),("B","Why"),("C","Shall"),("D","How")],"C"),
        (10,'You ______ borrow my book if you need it.',[("A","may"),("B","can"),("C","should"),("D","must")],"B")]
    fills=[(11,'You _______________ (最好) see a doctor.',"had better || \'d better"),(12,'You _______________ (最好別) forget the tickets.',"had better not || \'d better not"),(13,'She _______________ (應該) be here by now.',"should"),(14,'The AC _______________ (可能) have stopped working.',"may || might"),(15,'He _______________ (一定) have forgotten.',"must"),(16,'You should _______________ (have/receive) the results yesterday.',"have received"),(17,'If I _______________ (be) you, I would go.',"were"),(18,'She _______________ (不可能) have left already.',"can\'t"),(19,'_______________ (咱們) go to the beach.',"Let\'s"),(20,'How _______________ (⋯⋯怎麼樣) going for a walk?',"about")]
    errs=[(21,'You had better to see a doctor.',"You had better see a doctor."),(22,'You hadn\'t better forget.',"You had better not forget."),(23,'He must forgotten our meeting.',"He must have forgotten our meeting."),(24,'If I am you, I would go.',"If I were you, I would go."),(25,'She can\'t has left already.',"She can\'t have left already.")]
    content=card("<h1>Unit 21: Modal Verbs — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'It would be a good idea to see a doctor. (用 should) → You _______________',"should see a doctor"),(27,'I advise you not to forget the tickets. (用 had better) → You _______________',"had better not forget the tickets"),(28,'Perhaps she has taken the wrong bus. (用 may) → She _______________',"may have taken the wrong bus"),(29,'It is impossible that he has left. (用 can\'t) → He _______________',"can\'t have left"),(30,'I think it\'s certain that he forgot. (用 must) → He _______________',"must have forgotten")]))
    content+=card(btns())
    return head("Unit 21 — Practice Test", "unit21_test.html")+content+tail()

# ========== UNIT 22: Expressing Preferences ==========
def u22_study():
    c=card('<h1>Unit 22: Expressing Preferences（表達偏好）</h1>')
    c+=card('<h2>22.1 would like / would love</h2>'+table(["結構","例句"],[["would like + to-inf","I\'d like to sing a song."],["would love + to-inf","I\'d love to go to the concert."],["would like / love + noun","Would you like some tea?"]]))
    c+=card('<h2>22.2 would rather</h2><p><strong>would rather + 原形動詞</strong>（與 would prefer to 意思相近）</p><ul><li>I\'d <strong>rather have</strong> ramen.</li><li>I\'d <strong>rather not watch</strong> a horror film. (否定)</li><li>I\'d <strong>rather have tea than coffee</strong>.</li></ul>')
    c+=card('<h2>22.3 prefer</h2>'+table(["結構","例句"],[["prefer + to-inf / gerund","Charlie prefers to travel / travelling by bus."],["prefer + noun + to + noun","I prefer Japanese food to Thai food."],["would prefer + to-inf","I\'d prefer to take a nap."],["would prefer + to...rather than...","I\'d prefer to study French rather than Spanish."]]))
    c+=card('<h2>22.4 比較級表達偏好</h2><ul><li>I like dancing <strong>more than</strong> singing.</li><li>Of all vegetables, I like carrots <strong>(the) most</strong>.</li><li>I don\'t like durians, but I like coriander <strong>even less</strong>.</li></ul>')
    c+=card('<h2>考核要點 ✅</h2><ol><li>would like/love + to-infinitive（想要/渴望做）</li><li>would rather + 原形動詞（寧願）</li><li>would rather + than...（寧願⋯也不）</li><li>prefer + noun + to + noun；prefer + -ing/to-inf</li><li>would prefer + to-inf + rather than + 原形</li></ol>')
    return head("Unit 22 — Preferences", "unit22_study.html")+c+tail()

def u22_test():
    mc=[(1,'I\'d like ________ a song.',[("A","sing"),("B","to sing"),("C","singing"),("D","sang")],"B"),
        (2,'I\'d rather ________ ramen than sushi.',[("A","have"),("B","to have"),("C","having"),("D","had")],"A"),
        (3,'I\'d rather not ________ a horror film.',[("A","watch"),("B","to watch"),("C","watching"),("D","watched")],"A"),
        (4,'I prefer Japanese food ________ Thai food.',[("A","to"),("B","than"),("C","over"),("D","from")],"A"),
        (5,'I\'d prefer ________ a nap rather than go out.',[("A","take"),("B","to take"),("C","taking"),("D","took")],"B"),
        (6,'I\'d love ________ to the concert with you.',[("A","go"),("B","to go"),("C","going"),("D","went")],"B"),
        (7,'I like dancing more ________ singing.',[("A","to"),("B","than"),("C","then"),("D","from")],"B"),
        (8,'Of all fruits, I like apples ________.',[("A","most"),("B","the most"),("C","more"),("D","both A and B")],"D"),
        (9,'Would you like ________ to the party?',[("A","come"),("B","to come"),("C","coming"),("D","came")],"B"),
        (10,'Janice would prefer not ________ to Ocean Park.',[("A","go"),("B","to go"),("C","going"),("D","went")],"B")]
    fills=[(11,'I\'d like _______________ (sing) a song.',"to sing"),(12,'I\'d rather _______________ (have) tea than coffee.',"have"),(13,'I\'d rather not _______________ (watch) a horror film.',"watch"),(14,'I prefer Japanese food _______________ Thai food.',"to"),(15,'I\'d prefer _______________ (take) a nap.',"to take"),(16,'I\'d love _______________ (go) to the concert.',"to go"),(17,'I like dancing more _______________ singing.',"than"),(18,'Of all fruits, I like apples _______________.',"the most || most"),(19,'Would you like _______________ (come) to the party?',"to come"),(20,'I\'d rather have tea _______________ coffee.',"than")]
    errs=[(21,'I\'d like sing a song.',"I\'d like to sing a song."),(22,'I\'d rather to have tea than coffee.',"I\'d rather have tea than coffee."),(23,'I prefer Japanese food than Thai food.',"I prefer Japanese food to Thai food."),(24,'I\'d love go to the concert.',"I\'d love to go to the concert."),(25,'I\'d rather not to watch that film.',"I\'d rather not watch that film.")]
    content=card("<h1>Unit 22: Preferences — Practice Test</h1><p><strong>總分：100分 | 時限：35分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'I want to sing. (用 would like) → I\'d _______________',"like to sing"),(27,'I prefer tea to coffee. (用 rather) → I\'d rather _______________',"have tea than coffee"),(28,'I don\'t want to watch a horror film. (用 rather) → I\'d _______________',"rather not watch a horror film"),(29,'I prefer Japanese food. (用 more than) → I like Japanese food _______________',"more than Thai food"),(30,'I want very much to go to the concert. (用 love) → I\'d _______________',"love to go to the concert")]))
    content+=card(btns())
    return head("Unit 22 — Practice Test", "unit22_test.html")+content+tail()

# ========== UNIT 23: Connectives ==========
def u23_study():
    c=card('<h1>Unit 23: Connectives（連接詞）</h1><p>使用連接詞將觀點聯繫起來，表達附加、對比、原因和結果。</p>')
    c+=card('<h2>23.1 附加（Addition）</h2>'+table(["連接詞","例句"],[["and","He argued with her and she doesn\'t talk to him."],["also","Amy\'s job is mentally demanding. Also, I was very tired."],["besides / moreover / furthermore","This app is not user-friendly. Besides/Moreover, it\'s expensive."],["in addition","In addition, there is a pattern on the back."]]))
    c+=card('<h2>23.2 對比（Contrast）</h2>'+table(["連接詞","例句"],[["but","He spoke very fast, but I had no difficulty."],["or","Which subject will you choose, physics or economics?"]]))
    c+=card('<h2>23.3 原因（Reason）</h2>'+table(["連接詞","例句"],[["because / as / since","We stayed home because/as/since it was raining."],["because of / due to (+ 名詞)","We stayed home because of the rain."]]))
    c+=card('<h2>23.4 結果（Result）</h2>'+table(["連接詞","例句"],[["so","It has been raining for weeks, so the reservoir overflowed."],["(and) as a result","Joyce\'s foot was injured, and as a result she couldn\'t dance."],["therefore / thus / consequently","Therefore/Thus/Consequently, she could not take part."]]))
    c+=card('<h2>23.5 目的（Purpose）</h2>'+table(["連接詞","例句"],[["in order to / so as to","He leaves early in order to avoid traffic."],["so that (+ 從句)","He took a taxi so that he wouldn\'t be late."]]))
    c+=card('<h2>23.6 舉例（Examples）</h2><ul><li><strong>for example / for instance</strong>: Many sports, for example swimming and cycling, keep you fit.</li><li><strong>such as / like</strong>: Bright colours, such as red and orange, were required.</li></ul>')
    c+=card('<h2>考核要點 ✅</h2><ol><li>附加：and, also, besides, moreover, furthermore, in addition</li><li>原因：because/as/since + 從句；because of/due to + 名詞</li><li>結果：so, as a result, therefore, thus, consequently</li><li>目的：in order to, so as to (+ 動詞)；so that (+ 從句)</li><li>舉例：for example, for instance, such as, like</li></ol>')
    return head("Unit 23 — Connectives", "unit23_study.html")+c+tail()

def u23_test():
    mc=[(1,'He spoke very fast, ______ I had no difficulty.',[("A","or"),("B","but"),("C","so"),("D","and")],"B"),
        (2,'We stayed home ______ the rain.',[("A","because"),("B","because of"),("C","since"),("D","as")],"B"),
        (3,'It has been raining for weeks, ______ the reservoir overflowed.',[("A","but"),("B","or"),("C","so"),("D","because")],"C"),
        (4,'He leaves early ______ avoid traffic.',[("A","so that"),("B","in order to"),("C","because"),("D","but")],"B"),
        (5,'Joyce\'s foot was injured, and ______ she couldn\'t dance.',[("A","as a result"),("B","because"),("C","but"),("D","or")],"A"),
        (6,'He took a taxi ______ he wouldn\'t be late.',[("A","so as to"),("B","in order to"),("C","so that"),("D","because")],"C"),
        (7,'Which subject will you choose, physics ______ economics?',[("A","and"),("B","or"),("C","but"),("D","so")],"B"),
        (8,'This app is not user-friendly. ______, it\'s expensive.',[("A","But"),("B","Or"),("C","Moreover"),("D","So")],"C"),
        (9,'Bright colours, ______ red and orange, were required.',[("A","like"),("B","as"),("C","because"),("D","so")],"A"),
        (10,'______, she could not take part in the competition.',[("A","Because"),("B","Therefore"),("C","But"),("D","Or")],"B")]
    fills=[(11,'He spoke very fast, _______________ (但是) I understood.',"but"),(12,'We stayed home _______________ (因為) the rain.',"because of || due to"),(13,'It rained, _______________ (所以) we stayed home.',"so"),(14,'He leaves early _______________ (為了) avoid traffic.',"in order to || so as to"),(15,'He took a taxi _______________ (以便) he wouldn\'t be late.',"so that"),(16,'This app is not user-friendly. _______________ (此外), it\'s expensive.',"Moreover || Furthermore || Besides || In addition"),(17,'Joyce\'s foot was injured, and _______________ (結果) she couldn\'t dance.',"as a result || therefore || consequently"),(18,'Bright colours, _______________ (例如) red and orange, were required.',"such as || like || for example || for instance"),(19,'We stayed home _______________ (因為) it was raining.',"because || as || since"),(20,'_______________ (因此), she could not take part.',"Therefore || Thus || Consequently || As a result")]
    errs=[(21,'He spoke very fast, so I had no difficulty.',"but I had no difficulty."),(22,'We stayed home because of it was raining.',"because it was raining / because of the rain"),(23,'He took a taxi for not being late.',"so that he wouldn\'t be late / in order not to be late"),(24,'He leaves early so that avoid traffic.',"in order to avoid traffic / so that he can avoid traffic"),(25,'This app is not user-friendly. But it\'s expensive.',"Moreover/Furthermore/Besides, it\'s expensive.")]
    content=card("<h1>Unit 23: Connectives — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'He worked hard. He passed the exam. (用 so) → He worked hard, _______________',"so he passed the exam"),(27,'He was sick. He stayed home. (用 because) → He stayed home _______________',"because he was sick"),(28,'He left early. He wanted to avoid traffic. (用 in order to) → He left early _______________',"in order to avoid traffic"),(29,'The app is expensive. Also, it\'s not user-friendly. (用 moreover) → The app is expensive. _______________',"Moreover, it\'s not user-friendly"),(30,'She was injured. She couldn\'t dance. (用 therefore) → She was injured. _______________',"Therefore, she couldn\'t dance")]))
    content+=card(btns())
    return head("Unit 23 — Practice Test", "unit23_test.html")+content+tail()

# ========== UNIT 24: More Connectives ==========
def u24_study():
    c=card('<h1>Unit 24: More Connectives（進階連接詞）</h1>')
    c+=card('<h2>24.1 結果：so...that / such...that</h2>'+table(["結構","例句"],[["so + adj/adv + that","He spoke so fast that I couldn\'t understand."],["such + (a/an) + adj + noun + that","It was such a hot day that we didn\'t go out."]]))
    c+=card('<h2>24.2 such 的特殊用法</h2><ul><li>such + a/an + adj + 單數名詞：such a hot day</li><li>such + adj + 複數名詞：such beautiful flowers</li><li>such + adj + 不可數名詞：such good weather</li></ul>')
    c+=card('<h2>24.3 so that vs so...that</h2>'+callout("danger","⚠️ 區分","<strong>so that</strong>（表目的）：I left early <em>so that</em> I could catch the bus.<br><strong>so...that</strong>（表結果）：I was <em>so tired that</em> I fell asleep."))
    c+=card('<h2>24.4 as a consequence / consequently</h2><ul><li>His qualifications didn\'t meet the requirements, and <strong>as a consequence/and consequently</strong> his application was rejected.</li></ul><h2>24.5 meanwhile / in the meantime</h2><ul><li>I\'ll finish my work. <strong>Meanwhile/In the meantime</strong>, you can start preparing dinner.</li></ul>')
    c+=card('<h2>考核要點 ✅</h2><ol><li>so + adj/adv + that；such + (a/an) + adj + noun + that</li><li>so that（目的）≠ so...that（結果）</li><li>as a consequence / consequently（結果）</li><li>meanwhile / in the meantime（同時）</li></ol>')
    return head("Unit 24 — More Connectives", "unit24_study.html")+c+tail()

def u24_test():
    mc=[(1,'He spoke ______ fast that I couldn\'t understand.',[("A","so"),("B","such"),("C","too"),("D","very")],"A"),
        (2,'It was ______ a hot day that we stayed home.',[("A","so"),("B","such"),("C","too"),("D","such a")],"B"),
        (3,'I was ______ tired that I fell asleep.',[("A","so"),("B","such"),("C","too"),("D","very")],"A"),
        (4,'He left early ______ he could catch the bus.',[("A","so that"),("B","so...that"),("C","such that"),("D","in order")],"A"),
        (5,'She has ______ beautiful flowers!',[("A","so"),("B","such"),("C","such a"),("D","too")],"B"),
        (6,'His application was rejected. ______ he couldn\'t get the job.',[("A","So that"),("B","Such that"),("C","As a consequence"),("D","So as")],"C"),
        (7,'You finish your work. ______, I\'ll start dinner.',[("A","So that"),("B","Such that"),("C","Meanwhile"),("D","Because")],"C"),
        (8,'It was ______ good weather that we went to the beach.',[("A","so"),("B","such"),("C","such a"),("D","too")],"B"),
        (9,'She was ______ a fool that she believed him.',[("A","so"),("B","such"),("C","too"),("D","very")],"B"),
        (10,'He was so foolish ______ he believed the story.',[("A","so"),("B","that"),("C","such"),("D","as")],"B")]
    fills=[(11,'He spoke _______________ fast that I couldn\'t understand him.',"so"),(12,'It was _______________ a hot day that we stayed home.',"such"),(13,'I was _______________ tired that I fell asleep.',"so"),(14,'He left early _______________ (為了) he could catch the bus.',"so that"),(15,'She has _______________ beautiful flowers!',"such"),(16,'It was _______________ good weather that we went to the beach.',"such"),(17,'His application was rejected. _______________ (結果), he couldn\'t get the job.',"As a consequence || Consequently || Therefore"),(18,'You finish your work. _______________ (與此同時), I\'ll make dinner.',"Meanwhile || In the meantime"),(19,'He was _______________ a fool that he believed the story.',"such"),(20,'He was _______________ foolish that he believed the story.',"so")]
    errs=[(21,'He spoke such fast that I couldn\'t understand.',"He spoke so fast that I couldn\'t understand."),(22,'It was so hot day that we stayed home.',"It was such a hot day that we stayed home."),(23,'He left early so that he could catch the bus.',"No error"),(24,'I was so tired, I fell asleep. (可以省略 that)',"No error (that can be omitted)"),(25,'She has so beautiful flowers!',"She has such beautiful flowers!")]
    content=card("<h1>Unit 24: More Connectives — Practice Test</h1><p><strong>總分：100分 | 時限：35分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Proofreading 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'The weather was very hot. We stayed home. (用 so...that) → The weather was _______________',"so hot that we stayed home"),(27,'We had a very hot day. We stayed home. (用 such...that) → It was _______________',"such a hot day that we stayed home"),(28,'I was very tired. I fell asleep. (用 so...that) → I was _______________',"so tired that I fell asleep"),(29,'He wants to catch the bus. He left early. (用 so that) → He left early _______________',"so that he could catch the bus"),(30,'He didn\'t meet the requirements. He was rejected. (用 consequently) → He didn\'t meet the requirements. _______________',"Consequently, he was rejected")]))
    content+=card(btns())
    return head("Unit 24 — Practice Test", "unit24_test.html")+content+tail()

# ========== UNIT 25: Phrasal Verbs ==========
def u25_study():
    c=card('<h1>Unit 25: Phrasal Verbs（短語動詞）</h1><p>短語動詞由動詞 + 介詞/副詞構成，意思常與原動詞不同。</p>')
    c+=card('<h2>25.1 常見短語動詞</h2>'+table(["短語動詞","意思","例句"],[["look after","照顧","I\'m looking after my aunt."],["look into","調查","The police are looking into the case."],["put out","撲滅","They put out the fire in 40 minutes."],["find out","找出/發現","He found out who the murderer was."],["turn down","拒絕","She turned down the offer."],["check in","辦理入住","You can\'t check in now."],["get up","起床","She gets up at 8 o\'clock."],["care for","喜歡","He doesn\'t care for fishing."]]))
    c+=card('<h2>25.2 可分隔 vs 不可分隔</h2>'+table(["類型","例句"],[["可分隔（代詞在中間）","Put <strong>it</strong> out. / Turn <strong>it</strong> down."],["不可分隔","Look after <strong>her</strong>. / Look into <strong>the case</strong>."]]))
    c+=card('<h2>25.3 正式 vs 非正式</h2><ul><li><strong>非正式（短語動詞）</strong>：look into the case / find out the truth</li><li><strong>正式（單字動詞）</strong>：investigate the case / discover the truth</li></ul>')
    c+=card('<h2>考核要點 ✅</h2><ol><li>look after = take care of；look into = investigate；put out = extinguish</li><li>find out = discover；turn down = refuse；check in = register</li><li>代詞短語動詞：代詞放在動詞和介詞之間（put it out）</li><li>不可分短語動詞：受詞放在介詞後（look after her）</li><li>短語動詞用於非正式場合</li></ol>')
    return head("Unit 25 — Phrasal Verbs", "unit25_study.html")+c+tail()

def u25_test():
    mc=[(1,'Can you ______ my cat while I\'m away?',[("A","look into"),("B","look after"),("C","look for"),("D","look up")],"B"),
        (2,'The firemen ______ the fire quickly.',[("A","put up"),("B","put out"),("C","put on"),("D","put off")],"B"),
        (3,'I need to ______ who broke the window.',[("A","find out"),("B","find for"),("C","find in"),("D","find up")],"A"),
        (4,'She ______ the job offer because it paid too little.',[("A","turned up"),("B","turned down"),("C","turned on"),("D","turned off")],"B"),
        (5,'The police are ______ the robbery case.',[("A","looking after"),("B","looking into"),("C","looking for"),("D","looking up")],"B"),
        (6,'You can\'t ______ now. The flight is leaving.',[("A","check out"),("B","check in"),("C","check up"),("D","check on")],"B"),
        (7,'He doesn\'t ______ fishing.',[("A","care for"),("B","care about"),("C","care of"),("D","care with")],"A"),
        (8,'She ______ at 6 a.m. every day.',[("A","gets on"),("B","gets up"),("C","gets in"),("D","gets off")],"B"),
        (9,'Please ______ the light when you leave.',[("A","put out"),("B","turn off"),("C","turn down"),("D","look after")],"B"),
        (10,'I can\'t ______ the meaning of this word.',[("A","look after"),("B","look into"),("C","look up"),("D","look for")],"C")]
    fills=[(11,'Can you _______________ (照顧) my cat?',"look after"),(12,'The firemen _______________ (撲滅) the fire.',"put out"),(13,'I need to _______________ (找出) who did this.',"find out"),(14,'She _______________ (拒絕) the offer.',"turned down"),(15,'The police are _______________ (調查) the case.',"looking into"),(16,'You can\'t _______________ (辦理入住) now.',"check in"),(17,'She _______________ (起床) at 6 a.m.',"gets up"),(18,'He doesn\'t _______________ (喜歡) fishing.',"care for"),(19,'Please _______________ (關掉) the lights.',"turn off || switch off"),(20,'Look _______________ (查詢) the word in a dictionary.',"up")]
    errs=[(21,'Can you look my cat after?',"Can you look after my cat?"),(22,'She turned down it.',"She turned it down."),(23,'The police are looking the case into.',"The police are looking into the case."),(24,'I need to find who did this out.',"I need to find out who did this."),(25,'Please put the fire out. (代詞改寫: Put _______)',"Put it out.")]
    content=card("<h1>Unit 25: Phrasal Verbs — Practice Test</h1><p><strong>總分：100分 | 時限：35分鐘</strong></p>")
    content+=card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content+=card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content+=card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content+=card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in [(26,'Take care of my cat. (用短語動詞) → _______________',"Look after my cat"),(27,'Investigate the case. (用短語動詞) → _______________',"Look into the case"),(28,'I refuse the offer. (用短語動詞) → I _______________',"turn down the offer || turn it down"),(29,'Discover who did this. (用短語動詞) → _______________',"Find out who did this"),(30,'Extinguish the fire. (用短語動詞) → _______________',"Put out the fire || Put it out")]))
    content+=card(btns())
    return head("Unit 25 — Practice Test", "unit25_test.html")+content+tail()

# ============================================================
def main():
    os.chdir(HTML_DIR)
    generators = {
        "unit18_study.html": u18_study, "unit18_test.html": u18_test,
        "unit19_study.html": u19_study, "unit19_test.html": u19_test,
        "unit20_study.html": u20_study, "unit20_test.html": u20_test,
        "unit21_study.html": u21_study, "unit21_test.html": u21_test,
        "unit22_study.html": u22_study, "unit22_test.html": u22_test,
        "unit23_study.html": u23_study, "unit23_test.html": u23_test,
        "unit24_study.html": u24_study, "unit24_test.html": u24_test,
        "unit25_study.html": u25_study, "unit25_test.html": u25_test,
    }
    for name, func in generators.items():
        path = os.path.join(HTML_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(func())
        print(f"✅ {name}")

if __name__ == "__main__":
    main()
