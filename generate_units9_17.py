#!/usr/bin/env python3
"""生成 F2 English Grammar Units 9-17 学习材料与测试题 HTML"""

import os, sys

HTML_DIR = "/home/xmren/Documents/ebooks/karina book/F2/english/grammar/study_materials/html"

NAV = """
<nav class="top-nav">
<div class="top-nav-inner">
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
</ul>
</div>
</nav>"""

FOOTER = '<footer><p>F2 English Grammar &copy; 互動學習平台 &mdash; 祝考試順利！🎯</p></footer>'

def head(title, active):
    return f'''<!DOCTYPE html>
<html lang="zh-Hans">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><link rel="stylesheet" href="css/style.css">
<style>.nav-links a[href="{active}"]{{background:rgba(255,255,255,0.15);color:#fff!important}}</style>
</head><body>{NAV}<div class="container">'''

def tail():
    return f'</div>{FOOTER}<script src="js/script.js"></script></body></html>'

def card(c):
    return f'<div class="card">{c}</div>'

def table(h, rows):
    th = "<thead><tr>"+"".join(f"<th>{x}</th>" for x in h)+"</tr></thead>"
    tb = "<tbody>"
    for r in rows:
        tb += "<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>"
    return f'<div class="table-wrap"><table>{th}{tb}</table></div>'

def callout(typ, label, text):
    return f'<div class="callout {typ}"><strong>{label}</strong><p>{text}</p></div>'

def mc_q(n, stem, opts, ans):
    o = "".join(f'<label><input type="radio" name="q{n}" value="{l}"> {l}. {t}</label>' for l,t in opts)
    return f'''<div class="question" data-correct="{ans}">
<p><strong>{n}.</strong> {stem}</p><div class="options">{o}</div>
<div class="answer-reveal" style="display:none;margin:8px 0;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ 答案：<strong>{ans}</strong></div></div>'''

def fill_q(n, stem, ans):
    return f'''<div class="question" data-correct="{ans}">
<p><strong>{n}.</strong> {stem}</p>
<input type="text" class="fill-input" placeholder="輸入答案..." style="width:80%;padding:8px 12px;border:2px solid #e2e8f0;border-radius:6px;font-size:0.95rem;">
<div class="answer-reveal" style="display:none;margin:8px 0;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ 答案：<strong>{ans}</strong></div></div>'''

def err_q(n, stem, ans):
    return f'<div class="question" data-answer="{ans}"><p><strong>{n}.</strong> {stem}</p><div class="answer-reveal" style="display:none;margin:8px 0;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {ans}</div></div>'

def btns():
    return '''<div style="display:flex;gap:12px;flex-wrap:wrap;margin:24px 0;padding:16px;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
<button id="btn-show-answers" style="padding:10px 20px;background:#2563eb;color:#fff;border:none;border-radius:6px;cursor:pointer;">📖 顯示答案</button>
<button id="btn-hide-answers" style="padding:10px 20px;background:#64748b;color:#fff;border:none;border-radius:6px;cursor:pointer;">🙈 隱藏答案</button>
<button id="btn-calc-score" style="padding:10px 20px;background:#16a34a;color:#fff;border:none;border-radius:6px;cursor:pointer;">📊 計分</button>
<div id="score-box" style="display:none;padding:12px 20px;background:#f0fdf4;border-radius:6px;border:1px solid #16a34a;">
<p style="margin:0;font-size:1.1rem;">得分：<span class="score-num" style="font-weight:700;color:#16a34a;font-size:1.3rem;">—</span></p>
<p style="margin:4px 0 0;font-size:0.9rem;color:#64748b;"><span class="score-detail">0/0</span></p></div></div>'''

# ============================================================
# UNIT 9: To-infinitives and -ing forms
# ============================================================
def unit9_study():
    c = card("""
<h1>Unit 9: To-infinitives and -ing Forms（不定式與動名詞進階）</h1>
<p>本單元延續 Unit 7-8 的內容，深入學習 to-infinitive 和 -ing form 在不同語境中的用法。</p>
""")
    c += card("""
<h2>9.1 To-infinitive after Nouns（名詞後接不定式）</h2>
<p>to-infinitive 可以放在名詞後面，說明該名詞的用途或目的。</p>
<ul>
<li>Would you like <strong>something to drink</strong>?</li>
<li>He has <strong>many skills to apply</strong> to the group project.</li>
<li>I have a lot of <strong>work to do</strong>.</li>
</ul>
""" + table(["結構", "例句"], [
    ["something + to-inf", "Can you give me something to eat?"],
    ["nothing + to-inf", "There is nothing to worry about."],
    ["someone + to-inf", "She needs someone to talk to."],
    ["noun phrase + to-inf", "She has a decision to make."],
]))

    c += card("""
<h2>9.2 Adjective + To-infinitive（形容詞 + 不定式）</h2>
<p>某些形容詞後可接 to-infinitive 表示情感或評價。</p>
<ul>
<li>I am <strong>pleased to announce</strong> the winner.</li>
<li>We are <strong>happy to help</strong>.</li>
<li>She was <strong>surprised to see</strong> him.</li>
</ul>
""")

    c += card("""
<h2>9.3 Object Pronoun after To-infinitive</h2>
<p><strong>⚠️ 要點：</strong>當 to-infinitive 跟在名詞/代詞後面時，後面不能再放受詞代詞（it, them 等），因為名詞本身就是不定式的受詞。</p>
""" + table(["錯誤 ❌", "正確 ✅"], [
    ["She borrowed a novel to read <strong>it</strong> during the holidays.", "She borrowed a novel to read during the holidays."],
    ["I need a pen to write <strong>it</strong> with.", "I need a pen to write with."],
]) + callout("danger", "⚠️ 易錯點", "✗ I need a knife to cut <em>it</em> with. → ✓ I need a knife to cut with. (名詞 knife 本身已是 cut 的受詞，不能再加 it)"))

    c += card("""
<h2>9.4 To-infinitive with a Preposition（不定式 + 介詞）</h2>
<p>有時 to-infinitive 後面需要搭配一個介詞，結構為：名詞/代詞 + to-infinitive + 介詞。</p>
""" + table(["例句", "說明"], [
    ["She needs a hotel <strong>to stay at</strong>.", "住在旅館（stay at）"],
    ["He is looking for a restaurant <strong>to eat at</strong>.", "在餐廳吃飯（eat at）"],
    ["I need a chair <strong>to stand on</strong>.", "站在椅子上（stand on）"],
    ["He is a pleasant person <strong>to work with</strong>.", "與某人工作（work with）"],
]))

    c += card("""
<h2>9.5 Writing Focus: have + noun + to-infinitive</h2>
<p>表達「有某事要做」：</p>
<ul>
<li>I still <strong>have a lot of work to do</strong>.</li>
<li>She <strong>has two more reports to write</strong>.</li>
<li>They still <strong>have many problems to solve</strong>.</li>
</ul>
""")

    c += card("""
<h2>考核要點 ✅</h2>
<ol>
<li>to-infinitive 可放在名詞後表用途（something to drink）</li>
<li>形容詞後可接 to-infinitive（pleased to announce）</li>
<li>名詞為不定式受詞時，不再加受詞代詞</li>
<li>不定式後可能需要介詞（a hotel to stay at）</li>
<li>have + noun + to-infinitive 表「有⋯⋯要做」</li>
</ol>
""")
    return head("Unit 9 — To-infinitives & -ing", "unit9_study.html") + c + tail()

def unit9_test():
    mc = [
        (1,"Would you like something ______?",[("A","drink"),("B","drinking"),("C","to drink"),("D","drunk")],"C"),
        (2,"She borrowed a novel ______ during the holidays.",[("A","to read it"),("B","to read"),("C","reading"),("D","for reading")],"B"),
        (3,"I need a chair ______.",[("A","to stand"),("B","to stand on"),("C","standing"),("D","for standing")],"B"),
        (4,"We are pleased ______ the winner.",[("A","announce"),("B","announcing"),("C","to announce"),("D","announced")],"C"),
        (5,"He is a pleasant person ______.",[("A","to work"),("B","to work with"),("C","working"),("D","for working")],"B"),
        (6,"I still have a lot of work ______.",[("A","do"),("B","doing"),("C","to do"),("D","done")],"C"),
        (7,"She has a decision ______.",[("A","make"),("B","making"),("C","to make"),("D","made")],"C"),
        (8,"He is looking for a restaurant ______.",[("A","to eat"),("B","to eat at"),("C","eating"),("D","for eating")],"B"),
        (9,"There is nothing ______.",[("A","to worry"),("B","to worry about"),("C","worrying"),("D","for worrying")],"B"),
        (10,"I need someone ______.",[("A","to talk"),("B","to talk to"),("C","talking"),("D","talk")],"B"),
    ]
    fills = [
        (11,"Would you like something _______________ (drink)?", "to drink"),
        (12,"She needs a hotel _______________ (stay at).", "to stay at"),
        (13,"I am pleased _______________ (announce) the winner.", "to announce"),
        (14,"She has many skills _______________ (apply) to the project.", "to apply"),
        (15,"There is nothing _______________ (worry about).", "to worry about"),
        (16,"I need a pen _______________ (write with).", "to write with"),
        (17,"She still has two more reports _______________ (write).", "to write"),
        (18,"He is a nice person _______________ (work with).", "to work with"),
        (19,"I was surprised _______________ (see) him there.", "to see"),
        (20,"We are happy _______________ (help) you.", "to help"),
    ]
    errs = [
        (21,"She borrowed a novel to read it during the holidays.", "She borrowed a novel to read during the holidays."),
        (22,"I need a knife to cut it with.", "I need a knife to cut with."),
        (23,"He is looking for a restaurant to eat.", "He is looking for a restaurant to eat at."),
        (24,"Would you like something for drink?", "Would you like something to drink?"),
        (25,"I still have a lot of work for doing.", "I still have a lot of work to do."),
    ]
    content = card("<h1>Unit 9: To-infinitives & -ing — Practice Test</h1><p><strong>總分：100分 | 建議時限：40分鐘</strong></p>")
    content += card("<h2>Section A: Multiple Choice 10題（每題3分=30分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分=30分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分=20分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Sentence Rewriting 5題（每題4分=20分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"I want to drink something. → I want something _______________", "to drink"),
            (27,"He needs a hotel. He can stay at it. → He needs a hotel _______________", "to stay at"),
            (28,"She is happy. She helps others. → She is happy _______________", "to help others"),
            (29,"I have work. I must do it. → I have work _______________", "to do"),
            (30,"He is a good person. We can work with him. → He is a good person _______________", "to work with"),
        ]))
    content += card(btns())
    return head("Unit 9 — Practice Test", "unit9_test.html") + content + tail()

# ============================================================
# UNIT 10: Expressions + -ing
# ============================================================
def unit10_study():
    c = card("""
<h1>Unit 10: Expressions + -ing（表達式 + 動名詞）</h1>
<p>本單元學習各種常跟 -ing 形式的固定表達式。</p>
""")
    c += card("""
<h2>10.1 There + be + noun + -ing</h2>
<p>表示「有⋯正在做某事」。</p>
<ul>
<li><strong>There were</strong> some workmen <strong>taking down</strong> the scaffolding when I arrived.</li>
<li><strong>There have been</strong> lots of rumours <strong>spreading</strong> round town.</li>
<li><strong>There will be</strong> a lot of tourists <strong>coming</strong> for the festival.</li>
</ul>
""")
    c += card("""
<h2>10.2 It's no good / no use + -ing</h2>
<p>表示「做⋯⋯是沒用的」。</p>
<ul>
<li><strong>It's no use arguing</strong> with him.</li>
<li><strong>It's no good crying</strong> over spilt milk.</li>
<li><strong>It's no use trying</strong> to convince her.</li>
</ul>
""" + callout("tip", "💡 對比", "It's no use arguing with him.（-ing 形式）≠ It's useless to argue with him.（不定式也可，但 -ing 更常見）"))

    c += card("""
<h2>10.3 It's (not) worth + -ing</h2>
<p>表示「值得 / 不值得做⋯⋯」。</p>
<ul>
<li><strong>It's worth visiting</strong> the museum.</li>
<li><strong>It's not worth worrying</strong> about.</li>
<li><strong>Is it worth buying</strong> such an expensive bag?</li>
</ul>
""")

    c += card("""
<h2>10.4 It's a waste of time/money + -ing</h2>
<p>表示「做⋯⋯是浪費時間/金錢」。</p>
<ul>
<li><strong>It's a waste of time watching</strong> that show.</li>
<li><strong>It's a waste of money buying</strong> such cheap products.</li>
</ul>
<p><strong>spend/waste time/money + -ing</strong> 也可表達類似含義：</p>
<ul>
<li>He <strong>spent hours trying</strong> to do the crossword puzzle.</li>
<li>Don't <strong>waste time playing</strong> video games all day.</li>
</ul>
""")

    c += card("""
<h2>10.5 Have difficulty + -ing</h2>
<p>表示「做⋯⋯有困難」。</p>
<ul>
<li>I <strong>had difficulty finding</strong> a taxi.</li>
<li>She <strong>has difficulty expressing</strong> herself in English.</li>
</ul>
""" + callout("danger", "⚠️ 易錯點", "✗ I have difficulty <em>to express</em> myself. → ✓ I have difficulty <strong>expressing</strong> myself. (have difficulty 後用 -ing，不用 to-infinitive)"))

    c += card("""
<h2>10.6 Be busy + -ing</h2>
<p>表示「忙於做某事」。</p>
<ul>
<li>She's <strong>busy preparing</strong> for her exam.</li>
<li>I'm <strong>busy working</strong> on a project.</li>
</ul>
""")

    c += card("""
<h2>10.7 Go + -ing（户外活動）</h2>
""" + table(["短語", "意思"], [
    ["go camping", "去露營"], ["go hiking", "去遠足"], ["go fishing", "去釣魚"],
    ["go swimming", "去游泳"], ["go shopping", "去購物"], ["go sightseeing", "去觀光"],
]))

    c += card("""
<h2>10.8 Be used to / Get used to + -ing</h2>
<p><strong>be used to + -ing</strong> = 習慣於做某事</p>
<ul>
<li>I <strong>am used to getting</strong> up early.</li>
<li>She <strong>is used to living</strong> in a big city.</li>
</ul>
<p><strong>get used to + -ing</strong> = 逐漸習慣做某事</p>
<ul>
<li>It didn't take long for him to <strong>get used to driving</strong> on the left.</li>
</ul>
""" + callout("warning", "⚠️ 對比 used to", """
<strong>be/get used to + -ing</strong>（習慣於）≠ <strong>used to + infinitive</strong>（過去習慣）<br>
• I <em>am used to getting</em> up early.（我習慣早起）<br>
• I <em>used to get</em> up early.（我以前早起，現在不了）
"""))

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>There + be + noun + -ing（有人正在做某事）</li>
<li>It's no good/use + -ing（做⋯沒用）</li>
<li>It's (not) worth + -ing（值得/不值得）</li>
<li>spend/waste time/money + -ing（花費/浪費時間金錢做）</li>
<li>have difficulty + -ing（做⋯有困難）</li>
<li>be busy + -ing（忙於）</li>
<li>go + -ing（户外活動）</li>
<li>be/get used to + -ing（習慣於）≠ used to + inf（過去習慣）</li>
</ol>""")
    return head("Unit 10 — Expressions + -ing", "unit10_study.html") + c + tail()

def unit10_test():
    mc = [
        (1,"It's no use ______ with him. He won't change his mind.",[("A","argue"),("B","arguing"),("C","to argue"),("D","argued")],"B"),
        (2,"There ______ a lot of tourists coming for the festival.",[("A","is"),("B","will be"),("C","has"),("D","have")],"B"),
        (3,"She is busy ______ for her exam.",[("A","prepare"),("B","preparing"),("C","to prepare"),("D","prepared")],"B"),
        (4,"I had difficulty ______ a taxi in the rain.",[("A","find"),("B","finding"),("C","to find"),("D","found")],"B"),
        (5,"It's not worth ______ about such small things.",[("A","worry"),("B","worrying"),("C","to worry"),("D","worried")],"B"),
        (6,"He spent the whole afternoon ______ video games.",[("A","play"),("B","playing"),("C","to play"),("D","played")],"B"),
        (7,"It's a waste of time ______ that movie.",[("A","watch"),("B","watching"),("C","to watch"),("D","watched")],"B"),
        (8,"She is used to ______ up early in the morning.",[("A","get"),("B","getting"),("C","got"),("D","gets")],"B"),
        (9,"Let's go ______ this weekend!",[("A","camp"),("B","camping"),("C","to camp"),("D","camped")],"B"),
        (10,"I have difficulty ______ myself in English.",[("A","express"),("B","expressing"),("C","to express"),("D","expressed")],"B"),
    ]
    fills = [
        (11,"It's no use _______________ (argue) with him.", "arguing"),
        (12,"There were some workmen _______________ (take down) the scaffolding.", "taking down"),
        (13,"She is busy _______________ (prepare) for her exam.", "preparing"),
        (14,"I had difficulty _______________ (find) a taxi.", "finding"),
        (15,"It's worth _______________ (visit) the museum.", "visiting"),
        (16,"He spent hours _______________ (try) to fix the computer.", "trying"),
        (17,"Don't waste time _______________ (play) video games.", "playing"),
        (18,"She is used to _______________ (live) in a big city.", "living"),
        (19,"It didn't take long to get used to _______________ (drive) on the left.", "driving"),
        (20,"Let's go _______________ (shop) this afternoon.", "shopping"),
    ]
    errs = [
        (21,"It's no use to argue with him.", "It's no use arguing with him."),
        (22,"I have difficulty to express myself in English.", "I have difficulty expressing myself in English."),
        (23,"She is busy to prepare for her exam.", "She is busy preparing for her exam."),
        (24,"It's not worth to worry about it.", "It's not worth worrying about it."),
        (25,"I am used to wake up early.", "I am used to waking up early."),
    ]
    content = card("<h1>Unit 10: Expressions + -ing — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"It is useless to argue with him. (用 no use) → It's _______________", "no use arguing with him"),
            (27,"She is busy. She is preparing for the test. (合併) → She is busy _______________", "preparing for the test"),
            (28,"I find it difficult to express myself. (用 have difficulty) → I have difficulty _______________", "expressing myself"),
            (29,"He wasted money. He bought cheap products. (合併) → He wasted money _______________", "buying cheap products"),
            (30,"She now finds it normal to live here. (用 used to) → She is used to _______________", "living here"),
        ]))
    content += card(btns())
    return head("Unit 10 — Practice Test", "unit10_test.html") + content + tail()

# ============================================================
# UNIT 11: Bare Infinitive
# ============================================================
def unit11_study():
    c = card("""
<h1>Unit 11: Bare Infinitive（原形不定式）</h1>
<p>本單元學習哪些情況使用 <strong>不帶 to 的不定式</strong>（bare infinitive）。</p>
""")
    c += card("""
<h2>11.1 Let's / Why don't we/you / Why not + Bare Infinitive</h2>
<p>用於提出建議：</p>
<ul>
<li><strong>Let's go</strong> for a swim. It's hot today.</li>
<li><strong>Why don't we go</strong> to the cinema?</li>
<li><strong>Why not try</strong> again?</li>
</ul>
""")
    c += card("""
<h2>11.2 Verbs of Perception + Object + Bare Infinitive / -ing</h2>
<p>感官動詞（see, watch, hear, notice, smell）+ 受詞 + 原形不定式（強調動作全過程）或 -ing（強調正在進行）。</p>
""" + table(["結構", "含義", "例句"], [
    ["see + object + bare inf", "看見整個過程", "I <strong>saw</strong> Tom <strong>get off</strong> the bus and walk into the shop."],
    ["see + object + -ing", "看見正在進行", "I <strong>saw</strong> Tom <strong>waiting</strong> for a bus."],
    ["hear + object + bare inf", "聽見整個過程", "We <strong>heard</strong> her <strong>sing</strong> the whole song."],
    ["hear + object + -ing", "聽見正在進行", "We <strong>heard</strong> someone <strong>singing</strong> in the next room."],
]))

    c += card("""
<h2>11.3 Joining Two Infinitives（連接兩個不定式）</h2>
<p>用 and, or, but, except, than, as well as 連接兩個不定式時，第二個不定式通常省略 to。</p>
<ul>
<li>I'd like <strong>to go and buy</strong> some snacks.</li>
<li>Do you want <strong>to come with us or wait</strong> here?</li>
<li>He wanted to do nothing <strong>but play</strong> his guitar all day.</li>
<li>We could do nothing <strong>except hope</strong>.</li>
<li>It's easier <strong>to do the job yourself than ask</strong> anyone else.</li>
</ul>
""")

    c += card("""
<h2>11.4 Expressions with 'do' + Bare Infinitive</h2>
<p>某些含 do 的表達式後可用 bare infinitive 或 to-infinitive：</p>
""" + table(["表達式", "例句"], [
    ["All I did was (to)...", "All I did was (to) drink more water."],
    ["What I have done is (to)...", "What I have done is (to) send an email."],
    ["The only thing you can do is (to)...", "The only thing you can do is (to) wait."],
]))

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>Let's / Why don't we/you / Why not + 原形動詞（提議）</li>
<li>感官動詞 see/hear/watch + object + bare inf（完整動作）vs -ing（正在進行）</li>
<li>and/or/but/except/than/as well as 連接兩個不定式時，第二個常省 to</li>
<li>All I did was / What I have done is + (to) + 原形</li>
</ol>""")
    return head("Unit 11 — Bare Infinitive", "unit11_study.html") + c + tail()

def unit11_test():
    mc = [
        (1,"Let's ______ for a swim!",[("A","go"),("B","to go"),("C","going"),("D","went")],"A"),
        (2,"Why don't we ______ a movie tonight?",[("A","watch"),("B","to watch"),("C","watching"),("D","watched")],"A"),
        (3,"I saw him ______ the bus and walk into the shop.",[("A","get off"),("B","getting off"),("C","to get off"),("D","got off")],"A"),
        (4,"I heard someone ______ in the next room.",[("A","sing"),("B","singing"),("C","to sing"),("D","sang")],"B"),
        (5,"All I did was ______ more water.",[("A","drink"),("B","to drink"),("C","drinking"),("D","both A and B")],"D"),
        (6,"The only thing you can do is ______ for their call.",[("A","wait"),("B","to wait"),("C","waiting"),("D","both A and B")],"D"),
        (7,"I'd like to go and ______ some snacks.",[("A","buy"),("B","to buy"),("C","buying"),("D","bought")],"A"),
        (8,"Why not ______ again?",[("A","try"),("B","to try"),("C","trying"),("D","tried")],"A"),
        (9,"We watched the sun ______ below the horizon.",[("A","set"),("B","setting"),("C","to set"),("D","sets")],"A"),
        (10,"He wanted nothing but ______ his guitar.",[("A","play"),("B","to play"),("C","playing"),("D","played")],"A"),
    ]
    fills = [
        (11,"Let's _______________ (go) for a walk.", "go"),
        (12,"Why don't we _______________ (watch) a movie?", "watch"),
        (13,"I saw her _______________ (cross) the road and enter the building.", "cross"),
        (14,"I heard someone _______________ (sing) in the next room.", "singing"),
        (15,"All I did was _______________ (wait) for you.", "wait || to wait"),
        (16,"The only thing you can do is _______________ (hope).", "hope || to hope"),
        (17,"Why not _______________ (try) again?", "try"),
        (18,"I'd like to sit down and _______________ (rest).", "rest"),
        (19,"We could do nothing except _______________ (wait).", "wait"),
        (20,"He saw the children _______________ (play) in the park when he passed by.", "playing"),
    ]
    errs = [
        (21,"Let's to go for a swim.", "Let's go for a swim."),
        (22,"I saw him to get off the bus.", "I saw him get off the bus."),
        (23,"Why don't we to watch a movie?", "Why don't we watch a movie?"),
        (24,"All I did was to waiting for you.", "All I did was (to) wait for you."),
        (25,"He wanted nothing but to playing his guitar.", "He wanted nothing but play his guitar."),
    ]
    content = card("<h1>Unit 11: Bare Infinitive — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"Shall we go for a walk? (用 Let's) → _______________", "Let's go for a walk"),
            (27,"You should try again. (用 Why not) → _______________", "Why not try again"),
            (28,"I watched the process: the sun set below the horizon. (用 bare inf) → I watched the sun _______________", "set below the horizon"),
            (29,"I only waited for you, nothing else. (用 All I did) → All I did _______________", "was (to) wait for you"),
            (30,"You can only wait. (用 The only thing) → The only thing _______________", "you can do is (to) wait"),
        ]))
    content += card(btns())
    return head("Unit 11 — Practice Test", "unit11_test.html") + content + tail()

# ============================================================
# UNIT 12: Conjunctions / Linking Words
# ============================================================
def unit12_study():
    c = card("""
<h1>Unit 12: Conjunctions and Linking Words（連接詞與連接語）</h1>
<p>本單元學習如何用連接詞和連接語表達對比、讓步、原因、目的和結果。</p>
""")
    c += card("""
<h2>12.1 對比和讓步（Contrast & Concession）</h2>
""" + table(["連接詞", "用法", "例句"], [
    ["although / though / even though", "讓步（+ 從句）", "<strong>Although</strong> it rained, we enjoyed the picnic."],
    ["despite / in spite of", "讓步（+ 名詞/-ing）", "<strong>Despite</strong> the rain, we enjoyed the picnic."],
    ["however / nevertheless", "對比（另起一句）", "It rained. <strong>However</strong>, we enjoyed the picnic."],
    ["while / whereas", "對比兩個事實", "Tom likes sports <strong>while</strong> Jerry prefers reading."],
]))

    c += card("""
<h2>12.2 原因（Reason）</h2>
""" + table(["連接詞", "用法", "例句"], [
    ["because", "+ 從句", "She stayed home <strong>because</strong> she was sick."],
    ["because of", "+ 名詞", "She stayed home <strong>because of</strong> her illness."],
    ["since / as", "+ 從句（已知原因）", "<strong>Since</strong> you're tired, let's rest."],
]))

    c += card("""
<h2>12.3 目的（Purpose）</h2>
""" + table(["連接詞", "用法", "例句"], [
    ["so that", "+ 從句", "I left early <strong>so that</strong> I wouldn't miss the bus."],
    ["in order to", "+ 不定式", "I left early <strong>in order to</strong> catch the bus."],
]))

    c += card("""
<h2>12.4 結果（Result）</h2>
""" + table(["連接詞", "用法", "例句"], [
    ["so...that", "so + adj/adv + that", "The box was <strong>so heavy that</strong> I couldn't lift it."],
    ["such...that", "such + noun + that", "It was <strong>such a heavy box that</strong> I couldn't lift it."],
]))

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>although/though/even though + 從句；despite/in spite of + 名詞/-ing</li>
<li>however/nevertheless 另起新句表對比</li>
<li>because + 從句；because of + 名詞</li>
<li>so that + 從句表目的；in order to + 不定式</li>
<li>so + adj/adv + that；such + noun + that 表結果</li>
</ol>""")
    return head("Unit 12 — Conjunctions", "unit12_study.html") + c + tail()

def unit12_test():
    mc = [
        (1,"______ it rained, we enjoyed the picnic.",[("A","Despite"),("B","Although"),("C","Because of"),("D","However")],"B"),
        (2,"She stayed home ______ she was sick.",[("A","because of"),("B","because"),("C","despite"),("D","although")],"B"),
        (3,"He left early ______ he wouldn't miss the bus.",[("A","so that"),("B","so"),("C","because"),("D","although")],"A"),
        (4,"Tom likes sports ______ Jerry prefers reading.",[("A","however"),("B","while"),("C","despite"),("D","because")],"B"),
        (5,"The box was ______ heavy that I couldn't lift it.",[("A","such"),("B","so"),("C","very"),("D","too")],"B"),
        (6,"It was ______ a heavy box that I couldn't lift it.",[("A","so"),("B","such"),("C","very"),("D","too")],"B"),
        (7,"______ the rain, they continued playing.",[("A","Although"),("B","Despite"),("C","Because"),("D","So")],"B"),
        (8,"She worked hard ______ she could pass the exam.",[("A","so that"),("B","so as"),("C","in order"),("D","because")],"A"),
        (9,"You're tired. ______, let's take a break.",[("A","Despite"),("B","However"),("C","Therefore"),("D","Because")],"C"),
        (10,"______ you're tired, let's rest.",[("A","Because of"),("B","Despite"),("C","Since"),("D","However")],"C"),
    ]
    fills = [
        (11,"_______________ (雖然) it rained, we enjoyed the picnic.", "Although || Though || Even though"),
        (12,"She stayed home _______________ (因為) her illness.", "because of"),
        (13,"I left early _______________ (為了) I wouldn't miss the bus.", "so that"),
        (14,"Tom likes sports _______________ (而) Jerry prefers reading.", "while || whereas"),
        (15,"The box was _______________ heavy _______________ I couldn't lift it.", "so; that"),
        (16,"It was _______________ a heavy box _______________ I couldn't lift it.", "such; that"),
        (17,"_______________ (儘管) the rain, they continued playing.", "Despite || In spite of"),
        (18,"She worked hard _______________ (為了) pass the exam.", "in order to"),
        (19,"_______________ (既然) you're tired, let's rest.", "Since || As"),
        (20,"It rained. _______________ (然而), we enjoyed the picnic.", "However || Nevertheless"),
    ]
    errs = [
        (21,"Despite it rained, we enjoyed the picnic.", "Although it rained, we enjoyed the picnic. / Despite the rain, we enjoyed the picnic."),
        (22,"She stayed home because of she was sick.", "She stayed home because she was sick."),
        (23,"The box was such heavy that I couldn't lift it.", "The box was so heavy that I couldn't lift it."),
        (24,"It was so a heavy box that I couldn't lift it.", "It was such a heavy box that I couldn't lift it."),
        (25,"He left early for not missing the bus.", "He left early so that he wouldn't miss the bus."),
    ]
    content = card("<h1>Unit 12: Conjunctions — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"We enjoyed the picnic even though it rained. (用 despite) → _______________", "We enjoyed the picnic despite the rain."),
            (27,"Because she was sick, she stayed home. (用 because of) → _______________", "She stayed home because of her sickness."),
            (28,"The coffee is very hot. I cannot drink it. (用 so...that) → _______________", "The coffee is so hot that I cannot drink it."),
            (29,"He studied hard because he wanted to pass the exam. (用 so that) → _______________", "He studied hard so that he could pass the exam."),
            (30,"She left early. She wanted to catch the first train. (用 in order to) → _______________", "She left early in order to catch the first train."),
        ]))
    content += card(btns())
    return head("Unit 12 — Practice Test", "unit12_test.html") + content + tail()

# ============================================================
# UNIT 13: Quantifiers with Relative Pronouns
# ============================================================
def unit13_study():
    c = card("""
<h1>Unit 13: Quantifiers with Relative Pronouns（數量詞 + 關係代詞）</h1>
<p>本單元學習 how many/much, some of which/whom 等數量詞與關係代詞的搭配。</p>
""")
    c += card("""
<h2>13.1 Quantifier + of + whom/which</h2>
<p>在關係從句中，可用「數量詞 + of + whom/which」來修飾人或事物。</p>
""" + table(["數量詞", "例句"], [
    ["some of whom/which", "She has painted a lot of paintings, <strong>some of which</strong> are very famous."],
    ["many of whom/which", "His cousins, <strong>many of whom</strong> he had never met, were all at the party."],
    ["a few of whom/which", "She has several friends, <strong>a few of whom</strong> are from Japan."],
    ["most of whom/which", "The students, <strong>most of whom</strong> had studied hard, passed the exam."],
    ["all of whom/which", "I have three brothers, <strong>all of whom</strong> are taller than me."],
    ["none of whom/which", "The answers, <strong>none of which</strong> were correct, disappointed the teacher."],
    ["both of whom/which", "She has two daughters, <strong>both of whom</strong> are doctors."],
    ["neither of whom/which", "He suggested two plans, <strong>neither of which</strong> was feasible."],
    ["each of whom/which", "The team members, <strong>each of whom</strong> contributed a lot, were praised."],
]))

    c += card("""
<h2>13.2 Preposition + whom/which</h2>
<p>介詞可以放在關係代詞 whom/which 前面（正式用法）。</p>
<ul>
<li>The person <strong>to whom</strong> you spoke is the manager.</li>
<li>The company <strong>for which</strong> she works is based in London.</li>
<li>The topic <strong>about which</strong> we talked was very interesting.</li>
</ul>
""")

    c += card("""
<h2>13.3 whose（所有格關係代詞）</h2>
<p><strong>whose</strong> 表示「⋯⋯的」，可指人或物。</p>
<ul>
<li>I know a girl <strong>whose</strong> father is a famous singer.</li>
<li>That's the house <strong>whose</strong> roof was damaged in the storm.</li>
</ul>
""")

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>some/many/most/all/none/both/neither/each + of + whom/which</li>
<li>介詞 + whom/which 的正式用法</li>
<li>whose 表「⋯⋯的」，可指人或物</li>
</ol>""")
    return head("Unit 13 — Quantifiers & Relative Pronouns", "unit13_study.html") + c + tail()

def unit13_test():
    mc = [
        (1,"She has three brothers, all of ______ are taller than her.",[("A","who"),("B","whom"),("C","which"),("D","them")],"B"),
        (2,"He has many paintings, some of ______ are very valuable.",[("A","who"),("B","whom"),("C","which"),("D","them")],"C"),
        (3,"I know a girl ______ father is a famous singer.",[("A","who"),("B","whom"),("C","whose"),("D","which")],"C"),
        (4,"The person to ______ you spoke is the manager.",[("A","who"),("B","whom"),("C","which"),("D","whose")],"B"),
        (5,"She has two daughters, both of ______ are doctors.",[("A","who"),("B","whom"),("C","which"),("D","them")],"B"),
        (6,"I have several friends, a few of ______ are from Japan.",[("A","who"),("B","whom"),("C","which"),("D","them")],"B"),
        (7,"The answers, none of ______ were correct, disappointed the teacher.",[("A","who"),("B","whom"),("C","which"),("D","them")],"C"),
        (8,"He suggested two plans, neither of ______ was feasible.",[("A","who"),("B","whom"),("C","which"),("D","them")],"C"),
        (9,"The company for ______ she works is based in London.",[("A","who"),("B","whom"),("C","which"),("D","that")],"C"),
        (10,"That's the house ______ roof was damaged in the storm.",[("A","who"),("B","whom"),("C","whose"),("D","which")],"C"),
    ]
    fills = [
        (11,"She has three brothers, all of _______________ are taller than her.", "whom"),
        (12,"He has many paintings, some of _______________ are very valuable.", "which"),
        (13,"I know a girl _______________ father is a famous singer.", "whose"),
        (14,"The person to _______________ you spoke is the manager.", "whom"),
        (15,"She has two daughters, both of _______________ are doctors.", "whom"),
        (16,"The students, most of _______________ studied hard, passed.", "whom"),
        (17,"He suggested two plans, neither of _______________ was feasible.", "which"),
        (18,"That's the house _______________ roof was damaged.", "whose"),
        (19,"The topic about _______________ we talked was interesting.", "which"),
        (20,"I have three books, all of _______________ are borrowed from the library.", "which"),
    ]
    errs = [
        (21,"She has three brothers, all of who are taller than her.", "all of whom are taller than her."),
        (22,"I know a girl who father is a famous singer.", "whose father is a famous singer."),
        (23,"The person to who you spoke is the manager.", "to whom you spoke is the manager."),
        (24,"The company for which she works is based in London.", "No error"),
        (25,"He suggested two plans, neither of them was feasible.", "neither of which was feasible."),
    ]
    content = card("<h1>Unit 13: Quantifiers & Relative Pronouns — Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"She has three brothers. All of them are taller than her. (合併) → She has three brothers, _______________", "all of whom are taller than her"),
            (27,"The topic was interesting. We talked about it. (用 about which) → The topic _______________", "about which we talked was interesting"),
            (28,"I know a girl. Her father is a singer. (用 whose) → I know a girl _______________", "whose father is a singer"),
            (29,"He has many paintings. Some of them are valuable. (合併) → He has many paintings, _______________", "some of which are valuable"),
            (30,"She has two plans. Neither plan was feasible. (用 neither of which) → She has two plans, _______________", "neither of which was feasible"),
        ]))
    content += card(btns())
    return head("Unit 13 — Practice Test", "unit13_test.html") + content + tail()

# ============================================================
# UNIT 14: Adjective + Preposition
# ============================================================
def unit14_study():
    c = card("""
<h1>Unit 14: Adjective + Preposition（形容詞 + 介詞）</h1>
<p>本單元學習形容詞與特定介詞的搭配用法。</p>
""")
    c += card("""
<h2>14.1 常見形容詞 + 介詞搭配</h2>
""" + table(["形容詞 + 介詞", "用法", "例句"], [
    ["fond of", "喜歡", "Children are <strong>fond of</strong> ice-cream."],
    ["keen on", "熱衷於", "I'm not very <strong>keen on</strong> football."],
    ["crazy about", "狂熱於", "She's <strong>crazy about</strong> dancing."],
    ["good at", "擅長", "Keira is <strong>good at</strong> cycling."],
    ["good for", "對⋯有益", "Swimming is <strong>good for</strong> you."],
    ["good to", "對⋯友善", "Mrs Wong is <strong>good to</strong> every student."],
    ["angry at/with", "對某人生氣", "The customer was <strong>angry at/with</strong> the salesperson."],
    ["angry at/about", "對某事生氣", "She was <strong>angry about</strong> the delay."],
    ["happy about/with", "對某事滿意", "He was <strong>happy about/with</strong> his results."],
    ["happy for", "為某人高興", "We are <strong>happy for</strong> you."],
    ["disappointed about/at/by/with", "對某事失望", "She was <strong>disappointed about</strong> the results."],
    ["disappointed in/with", "對某人失望", "I'm <strong>disappointed in</strong> you."],
]))

    c += card("""
<h2>14.2 nice/kind/good/friendly/rude/polite + to</h2>
<p>描述對待某人的行為態度時用 to。</p>
<ul>
<li>They were very <strong>nice to</strong> us.</li>
<li>She is always <strong>polite to</strong> her teachers.</li>
<li>He was <strong>rude to</strong> the waiter.</li>
</ul>
""")

    c += card("""
<h2>14.3 for + 形容詞（說明原因）</h2>
<p>用 <strong>for</strong> 說明某種情緒的原因。</p>
<ul>
<li>She was angry with him <strong>for being late</strong>.</li>
<li>I'm grateful <strong>for your help</strong>.</li>
<li>He is famous <strong>for his novels</strong>.</li>
</ul>
""")

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>fond of / keen on / crazy about（喜好）</li>
<li>good at（擅長）/ good for（有益）/ good to（友善）</li>
<li>angry at/with + 人；angry at/about + 事</li>
<li>happy about/with + 事；happy for + 人</li>
<li>disappointed about/at/by/with + 事；disappointed in/with + 人</li>
<li>nice/kind/rude/polite + to someone</li>
<li>for + 名詞/-ing 說明原因</li>
</ol>""")
    return head("Unit 14 — Adjective + Preposition", "unit14_study.html") + c + tail()

def unit14_test():
    mc = [
        (1,"Children are fond ______ ice-cream.",[("A","of"),("B","on"),("C","with"),("D","for")],"A"),
        (2,"She's crazy ______ dancing.",[("A","of"),("B","about"),("C","with"),("D","for")],"B"),
        (3,"Keira is good ______ cycling.",[("A","of"),("B","at"),("C","for"),("D","to")],"B"),
        (4,"Swimming is good ______ your health.",[("A","of"),("B","at"),("C","for"),("D","to")],"C"),
        (5,"The customer was angry ______ the salesperson.",[("A","of"),("B","about"),("C","at/with"),("D","for")],"C"),
        (6,"I'm not very keen ______ football.",[("A","of"),("B","on"),("C","at"),("D","for")],"B"),
        (7,"We are happy ______ your success.",[("A","of"),("B","for"),("C","about/with"),("D","to")],"C"),
        (8,"She was disappointed ______ her exam results.",[("A","of"),("B","in/with"),("C","about/at/by"),("D","for")],"C"),
        (9,"The teacher is always polite ______ her students.",[("A","of"),("B","to"),("C","with"),("D","for")],"B"),
        (10,"He is famous ______ his novels.",[("A","of"),("B","at"),("C","for"),("D","to")],"C"),
    ]
    fills = [
        (11,"Children are fond _______________ ice-cream.", "of"),
        (12,"She's crazy _______________ dancing.", "about"),
        (13,"Keira is good _______________ cycling.", "at"),
        (14,"Swimming is good _______________ your health.", "for"),
        (15,"I'm not very keen _______________ football.", "on"),
        (16,"The customer was angry _______________ the salesperson.", "at || with"),
        (17,"She was angry _______________ the delay.", "about || at"),
        (18,"We are happy _______________ your success.", "about || with"),
        (19,"He was rude _______________ the waiter.", "to"),
        (20,"She was disappointed _______________ her son's behaviour.", "in || with"),
    ]
    errs = [
        (21,"Children are fond with ice-cream.", "fond of ice-cream"),
        (22,"She's crazy for dancing.", "crazy about dancing"),
        (23,"Keira is good for cycling (擅長).", "good at cycling"),
        (24,"He was angry with the delay (對事).", "angry about/at the delay"),
        (25,"He was rude with the waiter.", "rude to the waiter"),
    ]
    content = card("<h1>Unit 14: Adjective + Preposition — Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"I like ice-cream a lot. (用 fond) → I am _______________", "fond of ice-cream"),
            (27,"She is very interested in dancing. (用 crazy) → She is _______________", "crazy about dancing"),
            (28,"He plays tennis well. (用 good) → He is _______________", "good at tennis"),
            (29,"She was angry with him because he was late. (用 for) → She was angry with him _______________", "for being late"),
            (30,"The students were disappointed with their exam results. (用 about) → The students were disappointed _______________", "about their exam results"),
        ]))
    content += card(btns())
    return head("Unit 14 — Practice Test", "unit14_test.html") + content + tail()

# ============================================================
# UNIT 15: Question Tags
# ============================================================
def unit15_study():
    c = card("""
<h1>Unit 15: Question Tags（附加疑問句）</h1>
<p>附加疑問句是放在陳述句末尾的短小問句，用於徵求同意或確認信息。</p>
""")
    c += card("""
<h2>15.1 基本規則</h2>
""" + table(["陳述句", "附加問句", "規則"], [
    ["This cake is delicious,", "<strong>isn't it?</strong>", "肯定 + 否定"],
    ["You are Jerry's sister,", "<strong>aren't you?</strong>", "肯定 + 否定"],
    ["Marco isn't there,", "<strong>is he?</strong>", "否定 + 肯定"],
    ["He hasn't called,", "<strong>has he?</strong>", "否定 + 肯定"],
]))

    c += card("""
<h2>15.2 助動詞/情態動詞的使用</h2>
<p>附加問句使用與陳述句相同的助動詞/情態動詞。</p>
<ul>
<li>Paul <strong>was</strong> here yesterday, <strong>wasn't</strong> he?</li>
<li>You <strong>couldn't</strong> come last night, <strong>could</strong> you?</li>
<li>Jenny <strong>has gone</strong> to Japan, <strong>hasn't</strong> she?</li>
<li>Daniel <strong>had bought</strong> the cake, <strong>hadn't</strong> he?</li>
</ul>
<p>如果陳述句沒有助動詞，用 do/does/did：</p>
<ul>
<li>You like swimming, <strong>don't</strong> you?</li>
<li>Your uncle lives in Sha Tin, <strong>doesn't</strong> he?</li>
<li>She received the book, <strong>didn't</strong> she?</li>
</ul>
""")

    c += card("""
<h2>15.3 特殊情況</h2>
""" + table(["情況", "例句"], [
    ["I am → aren't I?", "I am right, <strong>aren't I</strong>?"],
    ["have 表動作 → do/does/did", "You always have breakfast at home, <strong>don't you</strong>?"],
    ["have 表擁有 → have/has 或 do/does", "Your father has a car, <strong>hasn't he / doesn't he</strong>?"],
    ["somebody/someone → they", "Someone called, <strong>didn't they</strong>?"],
    ["nobody/no one → they (肯定tag)", "Nobody phoned, <strong>did they</strong>?"],
    ["something/anything → it", "Something fell off the shelf, <strong>didn't it</strong>?"],
    ["nothing → it (肯定tag)", "Nothing happened, <strong>did it</strong>?"],
    ["everything → it", "Everything is fine, <strong>isn't it</strong>?"],
    ["this/that → it", "This is your phone, <strong>isn't it</strong>?"],
    ["these/those → they", "Those aren't your books, <strong>are they</strong>?"],
    ["There + be → 用 there", "There was an accident, <strong>wasn't there</strong>?"],
    ["Let's → shall we?", "Let's go, <strong>shall we</strong>?"],
    ["Imperative → won't you?", "Open the door, <strong>won't you</strong>?"],
]))

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>肯定 + 否定 tag；否定 + 肯定 tag</li>
<li>用相同助動詞；無助動詞用 do/does/did</li>
<li>I am → aren't I</li>
<li>somebody/nobody → they；something/nothing → it</li>
<li>this/that → it；these/those → they</li>
<li>There + be → there</li>
<li>Let's → shall we?</li>
</ol>""")
    return head("Unit 15 — Question Tags", "unit15_study.html") + c + tail()

def unit15_test():
    mc = [
        (1,"This cake is delicious, ______?",[("A","is it"),("B","isn't it"),("C","doesn't it"),("D","wasn't it")],"B"),
        (2,"You like swimming, ______?",[("A","don't you"),("B","do you"),("C","aren't you"),("D","isn't you")],"A"),
        (3,"He hasn't called back, ______?",[("A","has he"),("B","hasn't he"),("C","does he"),("D","did he")],"A"),
        (4,"I am right, ______?",[("A","am I not"),("B","am not I"),("C","aren't I"),("D","isn't I")],"C"),
        (5,"Someone called, ______?",[("A","didn't they"),("B","didn't he"),("C","didn't she"),("D","didn't it")],"A"),
        (6,"Nothing happened, ______?",[("A","did it"),("B","didn't it"),("C","does it"),("D","doesn't it")],"A"),
        (7,"This is your phone, ______?",[("A","is this"),("B","isn't this"),("C","isn't it"),("D","is it")],"C"),
        (8,"Let's go for a walk, ______?",[("A","will you"),("B","won't you"),("C","shall we"),("D","shan't we")],"C"),
        (9,"Your father has a car, ______?",[("A","hasn't he"),("B","doesn't he"),("C","both A and B"),("D","isn't he")],"C"),
        (10,"Nobody phoned for me, ______?",[("A","did they"),("B","didn't they"),("C","did he"),("D","didn't he")],"A"),
    ]
    fills = [
        (11,"This cake is delicious, _______________?", "isn't it"),
        (12,"You like swimming, _______________?", "don't you"),
        (13,"He hasn't called back, _______________?", "has he"),
        (14,"I am right, _______________?", "aren't I"),
        (15,"Someone called, _______________?", "didn't they"),
        (16,"Nothing happened, _______________?", "did it"),
        (17,"This is your phone, _______________?", "isn't it"),
        (18,"Let's go, _______________?", "shall we"),
        (19,"Paul was here yesterday, _______________?", "wasn't he"),
        (20,"Everything is fine, _______________?", "isn't it"),
    ]
    errs = [
        (21,"This cake is delicious, is it?", "isn't it"),
        (22,"I am right, am I not?", "aren't I"),
        (23,"Someone called, didn't it?", "didn't they"),
        (24,"Nothing happened, didn't it?", "did it"),
        (25,"Let's go, will you?", "shall we"),
    ]
    content = card("<h1>Unit 15: Question Tags — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"Add a question tag: You are Jerry's sister → You are Jerry's sister, _______________", "aren't you"),
            (27,"Add a question tag: Marco isn't there → Marco isn't there, _______________", "is he"),
            (28,"Add a question tag: You can swim → You can swim, _______________", "can't you"),
            (29,"Add a question tag: She had a good time → She had a good time, _______________", "didn't she"),
            (30,"Add a question tag: There was an accident → There was an accident, _______________", "wasn't there"),
        ]))
    content += card(btns())
    return head("Unit 15 — Practice Test", "unit15_test.html") + content + tail()

# ============================================================
# UNIT 16: Participle Phrases
# ============================================================
def unit16_study():
    c = card("""
<h1>Unit 16: Participle Phrases（分詞短語）</h1>
<p>分詞短語用於給出額外信息，分為現在分詞短語（-ing，主動）和過去分詞短語（-ed/不規則，被動）。</p>
""")
    c += card("""
<h2>16.1 Present Participle Phrases（現在分詞短語）</h2>
<p>以 V-ing 開頭，有主動含義。</p>
<ul>
<li><strong>Hearing</strong> the siren, the driver gave way to the ambulance.</li>
<li><strong>Jogging</strong> beside the river, Janice bumped into an old friend.</li>
</ul>
""")

    c += card("""
<h2>16.2 Past Participle Phrases（過去分詞短語）</h2>
<p>以過去分詞開頭，有被動含義。</p>
<ul>
<li><strong>Annoyed</strong> by the fight, Sheldon left the room.</li>
<li><strong>Not satisfied</strong> with his novel, the writer decided to start again.</li>
</ul>
""")

    c += card("""
<h2>16.3 分詞短語的位置</h2>
""" + table(["位置", "例句"], [
    ["句首", "<strong>Hearing the siren</strong>, the driver gave way."],
    ["句中（加逗號）", "The driver, <strong>hearing the siren</strong>, gave way."],
    ["句末", "The driver gave way, <strong>hearing the siren</strong>."],
]))

    c += card("""
<h2>16.4 分詞短語的用途</h2>
""" + table(["用途", "例句", "含義"], [
    ["同時發生的動作", "<strong>Jogging</strong> beside the river, Janice bumped into a friend.", "正在慢跑時碰到了朋友"],
    ["接連發生的動作", "<strong>Learning</strong> that her uncle had passed away, Annie cried.", "得知消息後哭了"],
    ["原因/結果", "<strong>Falling asleep</strong> on the bus, Chris missed his stop.", "因為睡著了而坐過站"],
    ["條件", "Players <strong>answering</strong> all questions correctly will win.", "如果全部答對就贏"],
    ["背景信息", "<strong>Featuring</strong> big Hollywood stars, the film had a high budget.", "因為有明星所以預算高"],
    ["辨識主語", "The girl <strong>singing</strong> on stage is Peter's sister.", "正在唱歌的那個女孩"],
]))

    c += card("""
<h2>16.5 逗號的使用</h2>
<p><strong>句中加分詞短語時：</strong>如果信息是額外的（非必要），加逗號。</p>
<ul>
<li>Simon's mother, <strong>worried about his safety</strong>, called the police.（額外信息）</li>
</ul>
<p><strong>不加逗號：</strong>如果信息是必要的（用來辨識是哪個）。</p>
<ul>
<li>The woman <strong>wearing a long brown jacket</strong> is Simon's mother.（必要信息）</li>
</ul>
""")

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>現在分詞短語（-ing）= 主動；過去分詞短語 = 被動</li>
<li>分詞短語可放在句首、句中、句末</li>
<li>not 放在分詞短語開頭表否定</li>
<li>分詞短語可表：同時發生、接連發生、原因、條件、背景信息</li>
<li>額外信息加分詞短語時用逗號；必要信息不用</li>
</ol>""")
    return head("Unit 16 — Participle Phrases", "unit16_study.html") + c + tail()

def unit16_test():
    mc = [
        (1,"______ the siren, the driver gave way to the ambulance.",[("A","Heard"),("B","Hearing"),("C","Hear"),("D","To hear")],"B"),
        (2,"______ by the fight, Sheldon left the room.",[("A","Annoying"),("B","Annoyed"),("C","Annoy"),("D","To annoy")],"B"),
        (3,"______ beside the river, Janice bumped into an old friend.",[("A","Jogged"),("B","Jogging"),("C","Jog"),("D","To jog")],"B"),
        (4,"______ satisfied with his novel, the writer started again.",[("A","Not"),("B","No"),("C","Don't"),("D","Doesn't")],"A"),
        (5,"The girl ______ on stage is Peter's sister.",[("A","sang"),("B","singing"),("C","sings"),("D","sung")],"B"),
        (6,"______ on the bus, Chris missed his stop.",[("A","Fell asleep"),("B","Falling asleep"),("C","Fallen asleep"),("D","To fall asleep")],"B"),
        (7,"______ big Hollywood stars, the film had a high budget.",[("A","Featured"),("B","Featuring"),("C","Feature"),("D","To feature")],"B"),
        (8,"______ that her uncle had passed away, Annie cried.",[("A","Learned"),("B","Learning"),("C","Learn"),("D","To learn")],"B"),
        (9,"The woman ______ a long brown jacket is Simon's mother.",[("A","worn"),("B","wearing"),("C","wears"),("D","to wear")],"B"),
        (10,"Players ______ all questions correctly will win a prize.",[("A","answered"),("B","answering"),("C","answer"),("D","answers")],"B"),
    ]
    fills = [
        (11,"_______________ (Hear) the siren, the driver gave way.", "Hearing"),
        (12,"_______________ (Annoy) by the fight, Sheldon left the room.", "Annoyed"),
        (13,"_______________ (Jog) beside the river, Janice bumped into a friend.", "Jogging"),
        (14,"_______________ satisfied with his novel, the writer started again.", "Not"),
        (15,"The girl _______________ (sing) on stage is Peter's sister.", "singing"),
        (16,"_______________ (fall) asleep on the bus, Chris missed his stop.", "Falling"),
        (17,"The film, _______________ (feature) big stars, had a high budget.", "featuring"),
        (18,"_______________ (learn) the news, Annie cried.", "Learning"),
        (19,"The woman _______________ (wear) a brown jacket is Simon's mother.", "wearing"),
        (20,"_______________ (give) a squeaky toy, the dog ran away happily.", "Given"),
    ]
    errs = [
        (21,"Hear the siren, the driver gave way.", "Hearing the siren, the driver gave way."),
        (22,"Annoying by the fight, Sheldon left the room.", "Annoyed by the fight, Sheldon left the room."),
        (23,"Not eat enough, the hiker got lost.", "Not having eaten enough, the hiker got lost."),
        (24,"The girl singing on stage is Peter's sister. (移除不必要的逗號)", "No error"),
        (25,"Simon's mother worried about his safety called the police.", "Simon's mother, worried about his safety, called the police."),
    ]
    content = card("<h1>Unit 16: Participle Phrases — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"The driver heard the siren. He gave way. (合併為分詞短語) → _______________", "Hearing the siren, the driver gave way."),
            (27,"Sheldon was annoyed by the fight. He left the room. (合併) → _______________", "Annoyed by the fight, Sheldon left the room."),
            (28,"Janice was jogging beside the river. She bumped into a friend. (合併) → _______________", "Jogging beside the river, Janice bumped into a friend."),
            (29,"Chris fell asleep on the bus. He missed his stop. (合併) → _______________", "Falling asleep on the bus, Chris missed his stop."),
            (30,"The writer was not satisfied with his novel. He decided to start again. (合併) → _______________", "Not satisfied with his novel, the writer decided to start again."),
        ]))
    content += card(btns())
    return head("Unit 16 — Practice Test", "unit16_test.html") + content + tail()

# ============================================================
# UNIT 17: Relative Clauses (Defining & Non-defining)
# ============================================================
def unit17_study():
    c = card("""
<h1>Unit 17: Relative Clauses（關係從句）</h1>
<p>本單元複習並深入學習限定性（defining）和非限定性（non-defining）關係從句。</p>
""")
    c += card("""
<h2>17.1 Defining Relative Clauses（限定性關係從句）</h2>
<p>提供必要信息來辨識所談論的人或事物，不用逗號。</p>
""" + table(["關係代詞", "用法", "例句"], [
    ["who / that", "指人（主語）", "The person <strong>who/that wrote</strong> this song is a friend of my sister's."],
    ["whom / who / that", "指人（受詞，可省略）", "The manager <strong>(whom/who/that)</strong> I talked to was very helpful."],
    ["which / that", "指物", "The tree <strong>which/that was blown down</strong> was very old."],
    ["when", "指時間", "It was windy on the day <strong>when I got</strong> to Hong Kong."],
    ["where", "指地點", "The park <strong>where we used</strong> to play has been renovated."],
    ["why", "指原因", "The reason <strong>why he called</strong> was to tell me the news."],
]))

    c += card("""
<h2>17.2 省略關係代詞</h2>
<p>當關係代詞在從句中作受詞時，可以省略。</p>
<ul>
<li>The girl <strong>(whom/who/that)</strong> Kenneth has admired for years is Sally.</li>
<li>Do you know the brand of chocolate <strong>(which/that)</strong> Christy loves?</li>
</ul>
""" + callout("danger", "⚠️ 注意", "關係代詞作主語時 <strong>不能省略</strong>：<br>✗ The picture on the wall contains a clue <em>will help us</em>. → <br>✓ The picture on the wall contains a clue <strong>which/that will help us</strong>."))

    c += card("""
<h2>17.3 不要用 what</h2>
<p>關係從句中不要用 what 代替 which/that。</p>
""" + callout("danger", "⚠️ 易錯點", "✗ Have you watched the movie <em>what</em> I talked to you about?<br>✓ Have you watched the movie <strong>which/that</strong> I talked to you about?"))

    c += card("""
<h2>17.4 Non-defining Relative Clauses（非限定性關係從句）</h2>
<p>提供額外信息，用逗號分隔，信息可有可無。不能用 that。</p>
<ul>
<li>Johnny Wong, <strong>whom we met yesterday</strong>, texted me just now.</li>
<li>Joey, <strong>who is currently on a working holiday</strong>, is coming home this summer.</li>
<li>Tyler forgot to bring his book, <strong>which is unlike him</strong>.</li>
</ul>
""" + table(["", "Defining（限定）", "Non-defining（非限定）"], [
    ["必要性", "必要信息", "額外信息"],
    ["逗號", "不用逗號", "用逗號"],
    ["that", "可用 that", "不能用 that"],
    ["省略", "受詞可省略", "不可省略"],
]))

    c += card("""<h2>考核要點 ✅</h2>
<ol><li>who/which/that/when/where/why 引導限定性關係從句</li>
<li>受詞位置的關係代詞可省略；主語位置不可省略</li>
<li>不要用 what 替代 which/that</li>
<li>非限定性關係從句用逗號、不能用 that、不能省略關係代詞</li>
</ol>""")
    return head("Unit 17 — Relative Clauses", "unit17_study.html") + c + tail()

def unit17_test():
    mc = [
        (1,"The person ______ wrote this song is my friend.",[("A","which"),("B","who"),("C","what"),("D","whom")],"B"),
        (2,"The tree ______ was blown down was very old.",[("A","who"),("B","what"),("C","which"),("D","whom")],"C"),
        (3,"Have you watched the movie ______ I talked to you about?",[("A","what"),("B","who"),("C","which"),("D","whom")],"C"),
        (4,"The manager ______ I talked to was very helpful.",[("A","who"),("B","whom"),("C","that"),("D","all of the above")],"D"),
        (5,"Johnny Wong, ______ we met yesterday, texted me.",[("A","which"),("B","that"),("C","whom"),("D","what")],"C"),
        (6,"Non-defining relative clauses use ______.",[("A","commas"),("B","that"),("C","no commas"),("D","what")],"A"),
        (7,"The park ______ we used to play has been renovated.",[("A","which"),("B","where"),("C","when"),("D","why")],"B"),
        (8,"The reason ______ he called was to tell me the news.",[("A","which"),("B","where"),("C","why"),("D","when")],"C"),
        (9,"In defining relative clauses, the object pronoun can be ______.",[("A","omitted"),("B","replaced with what"),("C","always kept"),("D","changed to that")],"A"),
        (10,"______ cannot be used in non-defining relative clauses.",[("A","Who"),("B","Whom"),("C","Which"),("D","That")],"D"),
    ]
    fills = [
        (11,"The person _______________ (who/which) wrote this song is my friend.", "who || that"),
        (12,"The tree _______________ (who/which) was blown down was very old.", "which || that"),
        (13,"The manager _______________ I talked to was very helpful. (可省略？填入答案)", "(whom/who/that) || (可以省略) || omit || omitted"),
        (14,"Have you watched the movie _______________ I talked about? (不要用 what)", "which || that"),
        (15,"Johnny Wong, _______________ we met yesterday, texted me.", "whom || who"),
        (16,"The park _______________ we used to play has been renovated.", "where"),
        (17,"The reason _______________ he called was to tell me the news.", "why"),
        (18,"A defining relative clause gives _______________ information.", "necessary || essential"),
        (19,"Non-defining relative clauses use _______________.", "commas"),
        (20,"_______________ cannot be used in non-defining relative clauses.", "That"),
    ]
    errs = [
        (21,"Have you watched the movie what I talked to you about?", "Have you watched the movie which/that I talked to you about?"),
        (22,"The picture contains a clue will help us solve the riddle.", "The picture contains a clue which/that will help us solve the riddle."),
        (23,"Johnny Wong, that we met yesterday, texted me.", "Johnny Wong, whom/who we met yesterday, texted me."),
        (24,"The park which we used to play has been renovated.", "The park where we used to play has been renovated."),
        (25,"The person wrote this song is my friend.", "The person who/that wrote this song is my friend."),
    ]
    content = card("<h1>Unit 17: Relative Clauses — Practice Test</h1><p><strong>總分：100分 | 時限：40分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題3分）</h2>"+"".join(mc_q(n,s,o,a) for n,s,o,a in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>"+"".join(fill_q(n,s,a) for n,s,a in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>"+"".join(err_q(n,s,a) for n,s,a in errs))
    content += card("<h2>Section D: Rewriting 5題（每題4分）</h2>"+
        "".join(fill_q(n,s,a) for n,s,a in [
            (26,"The person wrote this song. She is my friend. (合併) → The person _______________", "who/that wrote this song is my friend."),
            (27,"I talked to the manager. He was helpful. (合併) → The manager _______________", "(whom/who/that) I talked to was helpful."),
            (28,"The tree was blown down. It was very old. (合併) → The tree _______________", "which/that was blown down was very old."),
            (29,"We used to play in the park. It has been renovated. (用 where) → The park _______________", "where we used to play has been renovated."),
            (30,"He called me. The reason was to tell me the news. (用 why) → The reason _______________", "why he called was to tell me the news."),
        ]))
    content += card(btns())
    return head("Unit 17 — Practice Test", "unit17_test.html") + content + tail()


# ============================================================
# MAIN: Generate all files
# ============================================================
def main():
    os.chdir(HTML_DIR)
    generators = {
        "unit9_study.html": unit9_study,
        "unit9_test.html": unit9_test,
        "unit10_study.html": unit10_study,
        "unit10_test.html": unit10_test,
        "unit11_study.html": unit11_study,
        "unit11_test.html": unit11_test,
        "unit12_study.html": unit12_study,
        "unit12_test.html": unit12_test,
        "unit13_study.html": unit13_study,
        "unit13_test.html": unit13_test,
        "unit14_study.html": unit14_study,
        "unit14_test.html": unit14_test,
        "unit15_study.html": unit15_study,
        "unit15_test.html": unit15_test,
        "unit16_study.html": unit16_study,
        "unit16_test.html": unit16_test,
        "unit17_study.html": unit17_study,
        "unit17_test.html": unit17_test,
    }
    for name, func in generators.items():
        path = os.path.join(HTML_DIR, name)
        content = func()
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ {name} ({len(content)} chars)")

if __name__ == "__main__":
    main()
