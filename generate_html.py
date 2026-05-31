#!/usr/bin/env python3
"""生成 F2 English Grammar 所有交互式 HTML 页面"""

import os

HTML_DIR = "/home/xmren/Documents/ebooks/karina book/F2/english/grammar/study_materials/html"

NAV_COMMON = """
<nav class="top-nav">
<div class="top-nav-inner">
<a href="index.html" class="logo">📚 Grammar <span>F2</span></a>
<ul class="nav-links">
<li><a href="index.html">首頁</a></li>
<li><a href="unit1_study.html">U1</a></li>
<li><a href="unit1_test.html">U1測</a></li>
<li><a href="unit2_study.html">U2</a></li>
<li><a href="unit2_test.html">U2測</a></li>
<li><a href="unit3_study.html">U3</a></li>
<li><a href="unit3_test.html">U3測</a></li>
<li><a href="unit4_study.html">U4</a></li>
<li><a href="unit4_test.html">U4測</a></li>
<li><a href="unit5_study.html">U5</a></li>
<li><a href="unit5_test.html">U5測</a></li>
<li><a href="unit6_review.html">U6</a></li>
<li><a href="unit7_study.html">U7</a></li>
<li><a href="unit7_test.html">U7測</a></li>
<li><a href="unit8_study.html">U8</a></li>
<li><a href="unit8_test.html">U8測</a></li>
</ul>
</div>
</nav>"""

FOOTER = '<footer><p>F2 English Grammar &copy; 互動學習平台 &mdash; 祝考試順利！🎯</p></footer>'

def head(title, active_link=""):
    active_style = ""
    if active_link:
        active_style = f'<style>.nav-links a[href="{active_link}"]{{background:rgba(255,255,255,0.15);color:#fff!important}}</style>'
    return f'''<!DOCTYPE html>
<html lang="zh-Hans">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="css/style.css">
{active_style}
</head>
<body>
{NAV_COMMON}
<div class="container">'''

def tail():
    return f'''</div>
{FOOTER}
<script src="js/script.js"></script>
</body>
</html>'''

def card(content):
    return f'<div class="card">{content}</div>'

def table(headers, rows):
    thead = "<thead><tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr></thead>"
    tbody = "<tbody>"
    for row in rows:
        tbody += "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>"
    tbody += "</tbody>"
    return f'<div class="table-wrap"><table>{thead}{tbody}</table></div>'

def callout(typ, label, text):
    return f'<div class="callout {typ}"><strong>{label}</strong><p>{text}</p></div>'

def mc_question(num, stem, options, correct, note=""):
    opts_html = ""
    for letter, text in options:
        checked = ' checked' if letter == 'A' else ''
        opts_html += f'<label><input type="radio" name="q{num}" value="{letter}"{checked}> {letter}. {text}</label>'
    note_html = f"<br><small>{note}</small>" if note else ""
    return f'''<div class="question" data-correct="{correct}">
<p><strong>{num}.</strong> {stem}{note_html}</p>
<div class="options">{opts_html}</div>
<div class="answer-reveal" style="display:none;margin-top:8px;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ 答案：<strong>{correct}</strong></div>
</div>'''

def fill_question(num, stem, correct, hint=""):
    hint_html = f' <small style="color:#64748b">({hint})</small>' if hint else ""
    return f'''<div class="question" data-correct="{correct}">
<p><strong>{num}.</strong> {stem}{hint_html}</p>
<input type="text" class="fill-input" placeholder="輸入答案..." style="width:80%;padding:8px 12px;border:2px solid #e2e8f0;border-radius:6px;font-size:0.95rem;">
<div class="answer-reveal" style="display:none;margin-top:8px;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ 答案：<strong>{correct}</strong></div>
</div>'''

def test_buttons():
    return '''<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:24px;padding:16px;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
<button id="btn-show-answers" style="padding:10px 20px;background:#2563eb;color:#fff;border:none;border-radius:6px;cursor:pointer;font-size:0.95rem;">📖 顯示所有答案</button>
<button id="btn-hide-answers" style="padding:10px 20px;background:#64748b;color:#fff;border:none;border-radius:6px;cursor:pointer;font-size:0.95rem;">🙈 隱藏所有答案</button>
<button id="btn-calc-score" style="padding:10px 20px;background:#16a34a;color:#fff;border:none;border-radius:6px;cursor:pointer;font-size:0.95rem;">📊 計算分數</button>
<div id="score-box" style="display:none;padding:12px 20px;background:#f0fdf4;border-radius:6px;border:1px solid #16a34a;">
<p style="margin:0;font-size:1.1rem;">得分：<span class="score-num" style="font-weight:700;color:#16a34a;font-size:1.3rem;">—</span></p>
<p style="margin:4px 0 0;font-size:0.9rem;color:#64748b;">正確 / 總數：<span class="score-detail">0 / 0</span></p>
</div>
</div>'''

# ============================================================
# Unit 2 Study Material
# ============================================================
def gen_unit2_study():
    content = card("""
<h1>Unit 2: Talking about the past 複習教材</h1>
<p>本教材涵蓋 <strong>Simple Past Tense（一般過去式）</strong>、<strong>Past Continuous Tense（過去進行式）</strong>、<strong>Present Perfect Tense（現在完成式）</strong>、<strong>Present Perfect Continuous Tense（現在完成進行式）</strong>、<strong>Past Perfect Tense（過去完成式）</strong> 以及 <strong>Past Perfect Continuous Tense（過去完成進行式）</strong>。</p>
""")

    content += card("""
<h2>2.1 Simple Past Tense（一般過去式）</h2>
""" + table(["使用場景", "說明", "例句"], [
    ["過去完成的動作", "過去某明確時間點發生並結束", "I <strong>visited</strong> my grandmother yesterday.<br>She <strong>bought</strong> a new dress last week."],
    ["過去的事實或狀態", "過去存在的事實或情況", "He <strong>lived</strong> in London when he was a child."],
    ["過去重複的習慣", "過去經常做的事", "My grandfather <strong>walked</strong> to school every day."],
]) + """
<h3>動詞變化規則</h3>
""" + table(["規則", "例子"], [
    ["大部分加 -ed", "work→worked, play→played"],
    ["以 -e 結尾加 -d", "live→lived, like→liked"],
    ["子音+y 改y為i加-ed", "study→studied, cry→cried"],
    ["母音+y 直接加-ed", "stay→stayed, play→played"],
    ["重讀閉音節雙寫加-ed", "stop→stopped, plan→planned"],
    ["不規則動詞（需背誦）", "go→went, eat→ate, see→saw"],
]) + """
<h3>常見時間副詞</h3>
<ul>
<li><strong>yesterday</strong> — I met her yesterday.</li>
<li><strong>last night / last week / last month / last year</strong></li>
<li><strong>ago</strong> — She left ten minutes ago.</li>
<li><strong>in + 年份</strong> — He was born in 2010.</li>
</ul>
""")

    content += card("""
<h2>2.2 Past Continuous Tense（過去進行式）</h2>
<p><strong>結構：</strong><code>was / were + 現在分詞（V-ing）</code></p>
""" + table(["使用場景", "說明", "例句"], [
    ["過去某刻正在進行", "強調在過去某一刻正在發生", "I <strong>was doing</strong> homework at 8 p.m. last night."],
    ["兩個動作同時進行", "同時發生的兩個長動作", "While I <strong>was cooking</strong>, my brother <strong>was watching</strong> TV."],
    ["一個動作被另一個打斷", "長動作（進行式）被短動作（簡單式）打斷", "I <strong>was taking</strong> a shower when the phone <strong>rang</strong>."],
    ["營造背景氛圍", "描述故事背景", "The sun <strong>was shining</strong>, the birds <strong>were singing</strong>."],
]) + """
<h3>⚠️ Simple Past vs Past Continuous</h3>
""" + table(["Simple Past", "Past Continuous"], [
    ["動作已完成", "動作未完成（正在進行）"],
    ["I <strong>watched</strong> a movie.（看完了）", "I <strong>was watching</strong> a movie.（還沒看完）"],
]))

    content += card("""
<h2>2.3 Present Perfect Tense（現在完成式）</h2>
<p><strong>結構：</strong><code>has / have + 過去分詞（past participle）</code></p>
""" + table(["使用場景", "說明", "例句"], [
    ["經驗", "強調是否發生過，不關心具體時間", "I <strong>have visited</strong> Japan twice."],
    ["過去對現在有影響", "動作結果影響到現在", "I <strong>have lost</strong> my keys.（現在找不到）"],
    ["持續到現在", "與 since / for 搭配", "We <strong>have lived</strong> here for ten years."],
]) + """
<h3>常見時間副詞</h3>
""" + table(["副詞", "意思", "例句"], [
    ["ever", "曾經（疑問句）", "Have you ever seen a ghost?"],
    ["never", "從未", "I have never been to the US."],
    ["already", "已經", "She has already left."],
    ["yet", "尚未", "I haven't finished yet."],
    ["just", "剛剛", "They have just arrived."],
    ["since", "自從", "He has worked here since 2020."],
    ["for", "持續了", "We have known each other for five years."],
]))

    content += card("""
<h2>2.4 Present Perfect Continuous（現在完成進行式）</h2>
<p><strong>結構：</strong><code>has / have + been + V-ing</code></p>
""" + table(["使用場景", "說明", "例句"], [
    ["持續到現在的動作", "強調持續性和未完成", "I <strong>have been studying</strong> for three hours."],
    ["強調持續長度", "關注動作本身持續多久", "She <strong>has been waiting</strong> since 8 a.m."],
    ["對現在有可見結果", "結果是動作持續造成的", "You look tired. Have you been working all night?"],
]) + """
<h3>Present Perfect vs Present Perfect Continuous</h3>
""" + table(["Present Perfect", "Present Perfect Continuous"], [
    ["強調結果或完成", "強調持續的過程"],
    ["I <strong>have read</strong> the book.（看完了）", "I <strong>have been reading</strong> the book.（還在看）"],
    ["可用 stative verbs", "只用 action verbs"],
    ["I have known him for years. ✅", "✗ I have been knowing him."],
]))

    content += card("""
<h2>2.5 Past Perfect Tense（過去完成式）</h2>
<p><strong>結構：</strong><code>had + 過去分詞</code></p>
""" + table(["使用場景", "說明", "例句"], [
    ["「過去的過去」", "先發生的動作用 Past Perfect", "When I arrived, the train <strong>had already left</strong>."],
    ["過去某時間前已完成", "截至過去某時間已完成", "By the time he was 18, he <strong>had visited</strong> 15 countries."],
]))

    content += card("""
<h2>2.6 Past Perfect Continuous（過去完成進行式）</h2>
<p><strong>結構：</strong><code>had + been + V-ing</code></p>
""" + table(["使用場景", "說明", "例句"], [
    ["過去某時間之前一直在進行", "強調持續", "When I got home, mom <strong>had been cooking</strong> for 2 hours."],
    ["過去動作的結果", "過去有明顯證據", "Her eyes were red because she <strong>had been crying</strong>."],
]))

    content += card("""
<h2>2.7 六大時態對比總結表</h2>
""" + table(["時態", "結構", "核心用法", "常見時間詞"], [
    ["Simple Past", "V-ed / 不規則", "過去完成的動作", "yesterday, ago, last week"],
    ["Past Continuous", "was/were + V-ing", "過去某刻正在進行", "at that time, when, while"],
    ["Present Perfect", "have/has + V-ed₂", "過去到現在的經驗/結果", "ever, never, since, for"],
    ["Present Perfect Continuous", "have/has + been + V-ing", "持續到現在（強調過程）", "for, since, all day"],
    ["Past Perfect", "had + V-ed₂", "過去的過去", "by the time, before, after"],
    ["Past Perfect Continuous", "had + been + V-ing", "過去某時間前一直在進行", "for, since, by the time"],
]))

    content += card("""
<h2>考核要點總結 ✅</h2>
<ol>
<li><strong>Simple Past</strong> 用於已結束的過去動作，常與 yesterday / ago / last week 連用。</li>
<li><strong>Past Continuous</strong> 強調過去某刻正在進行；常見 when + 簡單式（打斷）或 while + 進行式（同時）。</li>
<li><strong>Present Perfect</strong> 連接過去和現在；不能與明確的過去時間連用。</li>
<li><strong>Present Perfect Continuous</strong> 強調動作的持續性；只用於 action verbs。</li>
<li><strong>Past Perfect</strong> 用於「過去的過去」— 先發生的動作。</li>
<li><strong>Past Perfect Continuous</strong> 強調過去某時間之前一直在進行的動作。</li>
</ol>
""" + callout("warning", "⚠️ 重點提醒",
    "Present Perfect 絕不能與明確的過去時間（yesterday, last week, ago）連用！這是考試必考陷阱！"))

    return head("Unit 2 — Talking about the past", "unit2_study.html") + content + tail()


# ============================================================
# Unit 2 Practice Test
# ============================================================
def gen_unit2_test():
    mc = [
        (1, "When I arrived at the party, everyone ______ already ______ home.",
         [("A", "has; gone"), ("B", "had; gone"), ("C", "was; going"), ("D", "did; go")], "B"),
        (2, "She ______ Chinese for three years before she moved to Hong Kong.",
         [("A", "studied"), ("B", "has been studying"), ("C", "had been studying"), ("D", "studies")], "C"),
        (3, "I ______ my homework yet. Can you give me five more minutes?",
         [("A", "haven't finished"), ("B", "didn't finish"), ("C", "wasn't finishing"), ("D", "hadn't finished")], "A"),
        (4, "While I ______ TV last night, the power suddenly went out.",
         [("A", "watched"), ("B", "was watching"), ("C", "have watched"), ("D", "had watched")], "B"),
        (5, "We ______ each other since we were in primary school.",
         [("A", "knew"), ("B", "were knowing"), ("C", "have known"), ("D", "had known")], "C"),
        (6, "By the time the teacher arrived, the students ______ the classroom.",
         [("A", "already cleaned"), ("B", "have already cleaned"), ("C", "had already cleaned"), ("D", "were already cleaning")], "C"),
        (7, "My mother ______ dinner when I got home from school.",
         [("A", "cooks"), ("B", "has cooked"), ("C", "had cooked"), ("D", "was cooking")], "D"),
        (8, "I ______ never ______ to Japan. Is it nice?",
         [("A", "have; been"), ("B", "had; been"), ("C", "did; go"), ("D", "was; going")], "A"),
        (9, "She looks exhausted because she ______ all day.",
         [("A", "works"), ("B", "worked"), ("C", "has been working"), ("D", "had worked")], "C"),
        (10, "We ______ tennis yesterday afternoon. It was fun!",
         [("A", "play"), ("B", "played"), ("C", "have played"), ("D", "had played")], "B"),
    ]

    fills = [
        (11, "I _______________ (already / finish) my homework before my mother came home.", "had already finished"),
        (12, "She _______________ (wait) for the bus for 30 minutes when it finally arrived.", "had been waiting"),
        (13, "They _______________ (live) in this city since 2015.", "have lived || have been living"),
        (14, "Tom _______________ (not / do) his homework last night because he was too tired.", "did not do || didn't do"),
        (15, "While we _______________ (have) dinner, the telephone rang.", "were having"),
        (16, "I _______________ (never / try) sushi before. Let's order some!", "have never tried"),
        (17, "By the time we reached the cinema, the movie _______________ (already / start).", "had already started"),
        (18, "She _______________ (study) English for five years, and she speaks very well.", "has been studying"),
        (19, "The ground was wet. It _______________ (rain) all night.", "had been raining"),
        (20, "My grandfather _______________ (work) as a teacher for 30 years before he retired.", "had worked || had been working"),
    ]

    errs = [
        (21, "I have seen a great movie yesterday with my friends.", "I saw a great movie yesterday with my friends."),
        (22, "She was knowing the answer but she didn't say anything.", "She knew the answer but she didn't say anything."),
        (23, "They have been living in Hong Kong since five years.", "They have been living in Hong Kong for five years."),
        (24, "When I arrived, she already left.", "When I arrived, she had already left."),
        (25, "He didn't went to school because he was sick.", "He didn't go to school because he was sick."),
    ]

    content = card("""
<h1>Unit 2: Talking about the Past — Practice Test</h1>
<p><strong>總分：100 分 | 建議時限：45 分鐘</strong></p>
<p>本測驗涵蓋 Simple Past、Past Continuous、Present Perfect、Present Perfect Continuous、Past Perfect 及 Past Perfect Continuous。</p>
""")

    content += card("<h2>Section A: Multiple Choice（選擇題）— 10 題（每題 2 分）</h2><p>Choose the best answer to complete each sentence.</p>" +
                    "".join(mc_question(n, s, o, c) for n, s, o, c in mc))

    content += card("<h2>Section B: Fill in the Blanks（填空）— 10 題（每題 3 分）</h2><p>Fill in the blanks with the correct form of the verb in brackets.</p>" +
                    "".join(fill_question(n, s, c) for n, s, c in fills))

    content += card("<h2>Section C: Error Correction（改錯）— 5 題（每題 4 分）</h2><p>Each sentence has ONE grammar mistake. Write the corrected sentence.</p>" +
                    "".join(f'<div class="question" data-answer="{c}"><p><strong>{n}.</strong> {s}</p><div class="answer-reveal" style="display:none;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {c}</div></div>' for n, s, c in errs))

    content += card("<h2>Section D: Sentence Rewriting（句子改寫）— 5 題（每題 6 分）</h2><p>Rewrite the sentences according to the instructions.</p>" +
                    "".join(fill_question(n, s, c) for n, s, c in [
                        (26, "I was sleeping. The earthquake happened. (Combine using Past Continuous + Simple Past)", "I was sleeping when the earthquake happened."),
                        (27, "I started learning French three years ago and I still learn it now. (Rewrite using Present Perfect)", "I have learned French for three years. || I have been learning French for three years."),
                        (28, "First, she finished her homework. Then, she watched TV. (Rewrite using Past Perfect)", "She had finished her homework before she watched TV."),
                        (29, "I have ever tried Korean food. (Change to negative)", "I have never tried Korean food."),
                        (30, "It started raining at 8 a.m. It is still raining now. (Rewrite using Present Perfect Continuous)", "It has been raining since 8 a.m."),
                    ]))

    content += card(test_buttons())

    return head("Unit 2 — Practice Test", "unit2_test.html") + content + tail()


# ============================================================
# Unit 3 Study Material
# ============================================================
def gen_unit3_study():
    content = card("""
<h1>Unit 3: Talking about the future 複習教材</h1>
<p>本教材涵蓋 <strong>Simple Present for future</strong>、<strong>Present Continuous for future</strong>、<strong>be going to</strong>、<strong>will / shall</strong>、<strong>Future Continuous</strong> 及 <strong>Future Perfect</strong>。</p>
""")

    content += card("""
<h2>3.1 五種將來表達方式總覽</h2>
""" + table(["表達方式", "結構", "核心用法", "例句"], [
    ["Simple Present", "一般現在式", "按時間表", "The train <strong>leaves</strong> at 7 p.m."],
    ["Present Continuous", "am/is/are + V-ing", "已計劃好", "I <strong>am meeting</strong> my friends tonight."],
    ["be going to", "am/is/are going to + V", "打算/有跡象預測", "It <strong>is going to rain</strong>."],
    ["will", "will + base form", "即時決定/預測/承諾", "I <strong>will help</strong> you."],
    ["Future Continuous", "will be + V-ing", "未來某刻正在進行", "I <strong>will be flying</strong> to Japan."],
    ["Future Perfect", "will have + V-ed₂", "未來某刻前已完成", "By 2028 I <strong>will have graduated</strong>."],
]))

    content += card("""
<h2>3.2 Simple Present for Future</h2>
<p>用在公共交通工具、學校時間表、電影場次等按時間表發生的事。</p>
<ul>
<li>The bus <strong>leaves</strong> at 8:15 tomorrow morning.</li>
<li>The exam <strong>starts</strong> at 9 a.m. next Monday.</li>
<li>School <strong>ends</strong> on July 15th.</li>
</ul>
""")

    content += card("""
<h2>3.3 Present Continuous for Future</h2>
<p>用於已計劃好的個人安排（通常涉及他人，有具體時間）。</p>
<ul>
<li>I <strong>am having</strong> dinner with my family tonight.</li>
<li>She <strong>is flying</strong> to London next Tuesday.</li>
<li>We <strong>are meeting</strong> at the cinema at 6 p.m.</li>
</ul>
""")

    content += card("""
<h2>3.4 be going to</h2>
<p>表示意圖/打算，或有跡象的預測。</p>
<ul>
<li>I <strong>am going to learn</strong> Mandarin next year. (打算)</li>
<li>Look at those clouds! It <strong>is going to rain</strong>. (有跡象)</li>
</ul>
<h3>對比：be going to vs will</h3>
""" + table(["be going to", "will"], [
    ["之前已決定的打算", "說話時才決定"],
    ["有跡象的預測", "無跡象的主觀猜測"],
]))

    content += card("""
<h2>3.5 will / shall</h2>
<p><strong>will</strong> 用於即時決定、預測、承諾、提議、威脅。</p>
<ul>
<li>I <strong>will</strong> get it. (即時決定)</li>
<li>I think it <strong>will</strong> be sunny. (預測)</li>
<li>I promise I <strong>will</strong> help. (承諾)</li>
</ul>
<p><strong>shall</strong> 主要用於提議（Shall I...? / Shall we...?）。</p>
<ul>
<li><strong>Shall</strong> we go now?</li>
<li><strong>Shall</strong> I open the window?</li>
</ul>
""")

    content += card("""
<h2>3.6 Future Continuous（未來進行式）</h2>
<p><strong>結構：</strong><code>will be + V-ing</code></p>
<ul>
<li>This time tomorrow, I <strong>will be sitting</strong> on the beach.</li>
<li>At 8 p.m. tonight, we <strong>will be having</strong> dinner.</li>
</ul>
""")

    content += card("""
<h2>3.7 Future Perfect（未來完成式）</h2>
<p><strong>結構：</strong><code>will have + 過去分詞</code></p>
<ul>
<li>By the time you arrive, I <strong>will have finished</strong> my homework.</li>
<li>Next month, I <strong>will have lived</strong> here for five years.</li>
</ul>
""")

    content += card("""
<h2>考核要點總結 ✅</h2>
<ol>
<li>時間表用 <strong>Simple Present</strong>：The train leaves at 6 a.m.</li>
<li>個人安排用 <strong>Present Continuous</strong>：I am meeting her tonight.</li>
<li>打算/有跡象用 <strong>be going to</strong>：It is going to rain.</li>
<li>即時決定/預測用 <strong>will</strong>：I will help you.</li>
<li>提議用 <strong>Shall</strong>：Shall we go?</li>
<li>未來某刻正在進行用 <strong>Future Continuous</strong></li>
<li>未來某刻已完成用 <strong>Future Perfect</strong></li>
</ol>
""" + callout("danger", "⚠️ 易錯點", """
<strong>if/when 從句不用 will：</strong>✗ If it <em>will rain</em>, I will stay home. → ✓ If it <em>rains</em>, I will stay home.<br>
<strong>will 後用原形：</strong>✗ I will to go. → ✓ I will go.<br>
<strong>be going to 後用原形：</strong>✗ I am going to meeting. → ✓ I am going to meet.
"""))

    return head("Unit 3 — Talking about the future", "unit3_study.html") + content + tail()


# ============================================================
# Unit 3 Practice Test
# ============================================================
def gen_unit3_test():
    mc = [
        (1, "The train to Beijing ______ at 8:30 a.m. tomorrow.",
         [("A","will leave"),("B","leaves"),("C","is going to leave"),("D","is leaving")], "B"),
        (2, "I promise I ______ you with your project this weekend.",
         [("A","am helping"),("B","help"),("C","will help"),("D","am going to help")], "C"),
        (3, "Look at those dark clouds! It ______ soon.",
         [("A","will rain"),("B","is raining"),("C","rains"),("D","is going to rain")], "D"),
        (4, "We ______ dinner at a fancy restaurant tonight. I've already booked.",
         [("A","will have"),("B","are having"),("C","have"),("D","shall have")], "B"),
        (5, "By the time you arrive, I ______ all my packing.",
         [("A","will finish"),("B","will be finishing"),("C","will have finished"),("D","am finishing")], "C"),
        (6, 'A: The phone is ringing! B: Don\'t worry, I ______ it.',
         [("A","am getting"),("B","get"),("C","will get"),("D","am going to get")], "C"),
        (7, "This time next week, we ______ on a beach in Thailand!",
         [("A","are lying"),("B","will be lying"),("C","will have lain"),("D","lie")], "B"),
        (8, "If it ______ tomorrow, we will cancel the picnic.",
         [("A","will rain"),("B","rains"),("C","is raining"),("D","is going to rain")], "B"),
        (9, "I ______ my doctor at 3 p.m. tomorrow. I have an appointment.",
         [("A","am seeing"),("B","will see"),("C","see"),("D","shall see")], "A"),
        (10, "______ we go to the cinema this evening?",
         [("A","Will"),("B","Do"),("C","Are"),("D","Shall")], "D"),
    ]
    fills = [
        (11, "The concert _______________ (start) at 7:30 p.m. sharp.", "starts"),
        (12, "I _______________ (help) you carry those bags. They look heavy.", "will help"),
        (13, "She _______________ (study) abroad next year. She has already applied.", "is going to study"),
        (14, "According to the forecast, it _______________ (be) sunny tomorrow.", "will be"),
        (15, "This time tomorrow, I _______________ (take) my final exam.", "will be taking"),
        (16, "By the end of this year, my parents _______________ (live) here for 20 years.", "will have lived"),
        (17, 'A: What are your plans? B: I _______________ (travel) to Japan with my family.', "am going to travel || am travelling"),
        (18, "The supermarket _______________ (open) at 9 a.m. and _______________ (close) at 10 p.m.", "opens; closes"),
        (19, "I _______________ (finish) the report by the time the boss arrives.", "will have finished"),
        (20, "Watch out! You _______________ (drop) that glass!", "are going to drop"),
    ]
    errs = [
        (21, "I am going to meeting my friends after school today.", "I am going to meet my friends after school today."),
        (22, "If it will rain tomorrow, we will stay at home.", "If it rains tomorrow, we will stay at home."),
        (23, "I will helping you with your homework if you need me.", "I will help you with your homework if you need me."),
        (24, "Look at that car! It will crash into the tree!", "Look at that car! It is going to crash into the tree!"),
        (25, "The bus will leave at 8 a.m. tomorrow according to the timetable.", "The bus leaves at 8 a.m. tomorrow according to the timetable."),
    ]
    content = card("<h1>Unit 3: Talking about the Future — Practice Test</h1><p><strong>總分：100 分 | 建議時限：45 分鐘</strong></p>")
    content += card("<h2>Section A: Multiple Choice 10題（每題2分）</h2>" + "".join(mc_question(n,s,o,c) for n,s,o,c in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>" + "".join(fill_question(n,s,c) for n,s,c in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>" +
                    "".join(f'<div class="question" data-answer="{c}"><p><strong>{n}.</strong> {s}</p><div class="answer-reveal" style="display:none;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {c}</div></div>' for n,s,c in errs))
    content += card("<h2>Section D: Sentence Rewriting 5題（每題6分）</h2>" +
                    "".join(fill_question(n,s,c) for n,s,c in [
                        (26, "I plan to visit my grandparents this weekend. (用 be going to)", "I am going to visit my grandparents this weekend."),
                        (27, "At midnight tonight, I will sleep. (用 Future Continuous)", "At midnight tonight, I will be sleeping."),
                        (28, "I will finish the project before next Friday. (用 Future Perfect)", "I will have finished the project by next Friday."),
                        (29, "We have arranged to meet at the library at 3 p.m. (用 Present Continuous for future)", "We are meeting at the library at 3 p.m."),
                        (30, "Do you want me to open the window? (用 Shall)", "Shall I open the window?"),
                    ]))
    content += card(test_buttons())
    return head("Unit 3 — Practice Test", "unit3_test.html") + content + tail()


# ============================================================
# Unit 4 Study Material
# ============================================================
def gen_unit4_study():
    content = card("""
<h1>Unit 4: The Passive（被動語態）複習教材</h1>
""")

    content += card("""
<h2>4.1 主動 vs 被動</h2>
""" + table(["", "主動語態", "被動語態"], [
    ["重點", "誰做動作", "誰承受動作"],
    ["結構", "主語 + 動詞 + 受詞", "主語 + be + 過去分詞 + (by + 施動者)"],
    ["例句", "The cat <strong>ate</strong> the fish.", "The fish <strong>was eaten</strong> by the cat."],
]) + """
<h3>何時用被動？</h3>
<ul>
<li><strong>施動者不明確或不重要：</strong>My bike <strong>was stolen</strong> last night.</li>
<li><strong>強調承受者：</strong>The injured man <strong>was taken</strong> to hospital.</li>
<li><strong>正式/客觀語境：</strong>It <strong>is believed</strong> that the economy will improve.</li>
</ul>
""")

    content += card("""
<h2>4.2 各時態的被動結構</h2>
""" + table(["時態", "被動結構", "例句"], [
    ["Simple Present", "am/is/are + V-ed₂", "English <strong>is spoken</strong> worldwide."],
    ["Present Continuous", "am/is/are + being + V-ed₂", "A road <strong>is being built</strong>."],
    ["Simple Past", "was/were + V-ed₂", "The letter <strong>was sent</strong> yesterday."],
    ["Past Continuous", "was/were + being + V-ed₂", "The car <strong>was being repaired</strong>."],
    ["Present Perfect", "have/has + been + V-ed₂", "The work <strong>has been finished</strong>."],
    ["Past Perfect", "had + been + V-ed₂", "It <strong>had been completed</strong>."],
    ["will future", "will + be + V-ed₂", "The meeting <strong>will be held</strong>."],
    ["be going to", "am/is/are going to + be + V-ed₂", "It <strong>is going to be solved</strong>."],
    ["Modals", "modal + be + V-ed₂", "This <strong>must be finished</strong> today."],
]))

    content += card("""
<h2>4.3 情態動詞被動式</h2>
<p><strong>公式：情態動詞 + be + 過去分詞</strong></p>
<ul>
<li>can → can <strong>be solved</strong></li>
<li>must → must <strong>be finished</strong></li>
<li>should → should <strong>be cleaned</strong></li>
<li>may/might → may <strong>be cancelled</strong></li>
<li>have to → has to <strong>be done</strong></li>
</ul>
""" + callout("tip", "💡 記憶口訣", "情態動詞被動式 = 情態動詞 + <strong>be</strong> + 過去分詞。情態動詞後面永遠用 be，不用 is/are/was/were！"))

    content += card("""
<h2>4.4 have / get something done（使役被動）</h2>
<p><strong>結構：</strong>have / get + 受詞 + 過去分詞</p>
<p><strong>意思：</strong>讓別人做某事（僱人或找人做）</p>
<ul>
<li>I <strong>had my hair cut</strong> yesterday.（我去剪了頭髮）</li>
<li>She <strong>had her car repaired</strong> last week.</li>
<li>He <strong>had his wallet stolen</strong> on the bus.（遭遇不幸）</li>
<li>I need to <strong>get my phone fixed</strong>.（口語用法）</li>
</ul>
""" + callout("warning", "⚠️ 對比", "I <em>cut</em> my hair.（我自己剪）vs I <em>had my hair cut</em>.（去理髮店剪）"))

    content += card("""
<h2>考核要點 ✅</h2>
<ol>
<li>被動語態公式：be + 過去分詞（be 隨時態變化）</li>
<li>何時用被動：施動者不明確/不重要、強調承受者、正式書面語</li>
<li>各時態被動：記住 be 的時態變化</li>
<li>情態動詞被動：modal + <strong>be</strong> + V-ed₂</li>
<li>have/get sth done：找人做某事</li>
</ol>
""" + callout("danger", "⚠️ 易錯點", """
• 忘記 be 動詞：✗ The window broken. → ✓ The window <strong>was</strong> broken.<br>
• 進行式忘了 being：✗ is built now → ✓ is <strong>being</strong> built now<br>
• 情態後誤用 is：✗ must is done → ✓ must <strong>be</strong> done<br>
• 不及物動詞無被動：✗ was happened → ✓ happened
"""))

    return head("Unit 4 — The Passive", "unit4_study.html") + content + tail()


# ============================================================
# Unit 4 Practice Test
# ============================================================
def gen_unit4_test():
    mc = [
        (1, "English ______ in many countries around the world.",
         [("A","is speaking"),("B","is spoken"),("C","speaks"),("D","is being spoken")], "B"),
        (2, "The new hospital ______ at the moment. It will open next year.",
         [("A","is built"),("B","is being built"),("C","builds"),("D","was built")], "B"),
        (3, "All the homework ______ by the students before the deadline.",
         [("A","must finish"),("B","must be finished"),("C","must finished"),("D","must be finish")], "B"),
        (4, "The famous painting ______ by a thief last night.",
         [("A","stole"),("B","is stolen"),("C","was stolen"),("D","has stolen")], "C"),
        (5, "I need to ______ my phone ______ because the screen is broken.",
         [("A","have; fix"),("B","have; fixed"),("C","have; fixing"),("D","have; to fix")], "B"),
        (6, "A new bridge ______ across the river next year.",
         [("A","will build"),("B","will be built"),("C","is building"),("D","has built")], "B"),
        (7, "The problem ______ yet. We are still working on it.",
         [("A","hasn't solved"),("B","hasn't been solved"),("C","wasn't solved"),("D","isn't solving")], "B"),
        (8, "Dinner ______ by my mother every evening.",
         [("A","is cooked"),("B","cooks"),("C","is cooking"),("D","is being cooked")], "A"),
        (9, "The car ______ when I arrived at the garage.",
         [("A","repaired"),("B","was repairing"),("C","was being repaired"),("D","has been repaired")], "C"),
        (10, "The concert ______ to next month because of the typhoon.",
         [("A","has postponed"),("B","has been postponed"),("C","postponed"),("D","is postponing")], "B"),
    ]
    fills = [
        (11, "The chef prepares the salad. → The salad _______________", "is prepared"),
        (12, "The students will finish the project. → The project _______________", "will be finished"),
        (13, "Someone has stolen my bike. → My bike _______________", "has been stolen"),
        (14, "The police caught the thief yesterday. → The thief _______________", "was caught yesterday"),
        (15, "You must return the books by Friday. → The books _______________", "must be returned by Friday"),
        (16, "The government is building a new airport. → A new airport _______________", "is being built"),
        (17, "My mother had already made the cake. → The cake _______________", "had already been made"),
        (18, "They are going to open a new shopping mall. → A new shopping mall _______________", "is going to be opened"),
        (19, "Someone should clean the classroom. → The classroom _______________", "should be cleaned"),
        (20, "The company has offered her a job. → She _______________", "has been offered a job"),
    ]
    errs = [
        (21, "The window broken by a ball yesterday.", "The window was broken by a ball yesterday."),
        (22, "The letter is send every morning.", "The letter is sent every morning."),
        (23, "This work must is finished by 5 p.m. today.", "This work must be finished by 5 p.m. today."),
        (24, "She had her hair cutted at the salon.", "She had her hair cut at the salon."),
        (25, "The accident was happened near my school.", "The accident happened near my school."),
    ]
    content = card("<h1>Unit 4: The Passive — Practice Test</h1><p><strong>總分：100 分 | 建議時限：45 分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題2分）</h2>" + "".join(mc_question(n,s,o,c) for n,s,o,c in mc))
    content += card("<h2>Section B: 主動改被動 10題（每題3分）</h2><p>Rewrite from active to passive. Omit the agent unless necessary.</p>" +
                    "".join(fill_question(n,s,c) for n,s,c in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>" +
                    "".join(f'<div class="question" data-answer="{c}"><p><strong>{n}.</strong> {s}</p><div class="answer-reveal" style="display:none;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {c}</div></div>' for n,s,c in errs))
    content += card("<h2>Section D: Sentence Rewriting 5題（每題6分）</h2>" +
                    "".join(fill_question(n,s,c) for n,s,c in [
                        (26, "Someone delivers the newspapers every morning. (用被動)", "The newspapers are delivered every morning."),
                        (27, "A professional photographer took our wedding photos. (用 have sth done)", "We had our wedding photos taken by a professional photographer."),
                        (28, "Shakespeare wrote Romeo and Juliet. (保留施動者)", "Romeo and Juliet was written by Shakespeare."),
                        (29, "You can solve this problem easily. (用情態被動)", "This problem can be solved easily."),
                        (30, "People believe that exercise is good for health. (用被動)", "Exercise is believed to be good for health."),
                    ]))
    content += card(test_buttons())
    return head("Unit 4 — Practice Test", "unit4_test.html") + content + tail()


# ============================================================
# Unit 5 Study Material
# ============================================================
def gen_unit5_study():
    content = card("""
<h1>Unit 5: Conditional Sentences — 條件句完整攻略</h1>
""")
    content += card("""
<h2>1. 四類條件句對比表</h2>
""" + table(["類別", "用法", "If 子句", "主要子句", "例句"], [
    ["Type 0 🔵", "一般事實", "present simple", "present simple", "If you heat ice, it melts."],
    ["Type 1 🟢", "未來可能", "present simple", "will + V", "If it rains, I will stay home."],
    ["Type 2 🟡", "現在不真實", "past simple", "would + V", "If I had money, I would travel."],
    ["Type 3 🔴", "過去不真實", "had + V-ed₂", "would have + V-ed₂", "If I had studied, I would have passed."],
]) + """
<h3>🎯 判斷流程</h3>
<pre style="background:#f1f5f9;padding:16px;border-radius:8px;line-height:1.8;">
一般事實/科學定律？ → Type 0 (if + present, present)
未來有可能發生？ → Type 1 (if + present, will + V)
與現在事實相反？ → Type 2 (if + past, would + V)
與過去事實相反？ → Type 3 (if + had + V-ed₂, would have + V-ed₂)
</pre>""")

    content += card("""
<h2>2. Type 3 詳細說明</h2>
<p>表達 <strong>遺憾</strong>、<strong>失望</strong>、<strong>對過去的假設</strong>。</p>
<p><strong>公式：</strong>If + had + V-ed₂, would have + V-ed₂</p>
<ul>
<li>✅ If I <strong>had known</strong>, I <strong>would have met</strong> you.</li>
<li>✅ If she <strong>had not been</strong> ill, she <strong>would have joined</strong> us.</li>
</ul>
<h3>Type 2 vs Type 3 對比</h3>
""" + table(["", "Type 2 (現在不真實)", "Type 3 (過去不真實)"], [
    ["時間", "現在", "過去"],
    ["事實", "I am not rich now.", "I didn't study hard."],
    ["句子", "If I were rich, I would travel.", "If I had studied, I would have passed."],
    ]))

    content += card("""
<h2>3. might have vs could have vs would have</h2>
""" + table(["情態動詞", "含義", "確定程度", "例句"], [
    ["would have", "一定會", "100%", "If you had asked, I <strong>would have helped</strong> you."],
    ["could have", "本來可以", "70-80%", "If you had told me, I <strong>could have helped</strong>."],
    ["might have", "也許會", "40-60%", "If you had eaten it, you <strong>might have been</strong> sick."],
]) + callout("tip", "💡 記憶口訣", "「would 肯定，could 可以，might 可能」"))

    content += card("""
<h2>4. wish / if only 用法</h2>
""" + table(["時間", "結構", "例子", "事實"], [
    ["現在願望 🔵", "wish + past simple", "I wish I <strong>were</strong> taller.", "I am NOT taller."],
    ["過去願望 🔴", "wish + had + V-ed₂", "I wish I <strong>had been</strong> careful.", "I was NOT careful."],
]) + """
<p><strong>if only</strong> 比 wish 語氣更強烈，常用於感嘆句。</p>
<ul>
<li>If only I <strong>had studied</strong>! (多麼希望我學了！)</li>
</ul>
""" + callout("warning", "⚠️ 考試重點", "I wish I <strong>were</strong>… 和 If I <strong>were</strong> you… 是必考固定用法！主詞為 I/he/she/it 時用 were 而非 was。"))

    content += card("""
<h2>5. 易錯點提醒</h2>
""" + table(["錯誤 ❌", "正確 ✅", "原因"], [
    ["If it <strong>will rain</strong>…", "If it <strong>rains</strong>…", "if 子句用 present，不用 will"],
    ["If I <strong>have</strong> known…", "If I <strong>had</strong> known…", "Type 3 用 had + V-ed₂"],
    ["…I would <strong>said</strong> hello.", "…I would <strong>have said</strong> hello.", "主句用 would have + V-ed₂"],
    ["I wish I <strong>am</strong> taller.", "I wish I <strong>were</strong> taller.", "現在願望用過去式"],
    ["If you heat ice, it <strong>will melt</strong>.", "If you heat ice, it <strong>melts</strong>.", "科學事實用 Type 0"],
]))

    return head("Unit 5 — Conditional Sentences", "unit5_study.html") + content + tail()


# ============================================================
# Unit 5 Practice Test
# ============================================================
def gen_unit5_test():
    mc = [
        (1, "If you ________ ice, it floats.", [("A","will heat"),("B","heat"),("C","heated"),("D","had heated")], "B"),
        (2, "If I ________ you, I would apologise immediately.", [("A","am"),("B","was"),("C","were"),("D","have been")], "C"),
        (3, "If it rains tomorrow, we ________ the picnic.", [("A","cancel"),("B","cancelled"),("C","will cancel"),("D","would cancel")], "C"),
        (4, "If she had studied medicine, she ________ a doctor now.", [("A","will be"),("B","would be"),("C","would have been"),("D","had been")], "B"),
        (5, "I wish I ________ more careful in the last exam.", [("A","am"),("B","was"),("C","were"),("D","had been")], "D"),
        (6, "If you ________ me earlier, I could have helped you.", [("A","tell"),("B","told"),("C","had told"),("D","have told")], "C"),
        (7, "If you had eaten spoiled food, you ________ sick.", [("A","will be"),("B","would be"),("C","might have been"),("D","are")], "C"),
        (8, "If only I ________ how to swim when I was young!", [("A","learn"),("B","learned"),("C","had learned"),("D","would learn")], "C"),
        (9, "If he hadn't missed the bus, he ________ late for the interview.", [("A","wouldn't be"),("B","wouldn't have been"),("C","won't be"),("D","isn't")], "B"),
        (10, "She wishes she ________ more time last week.", [("A","has"),("B","had"),("C","had had"),("D","would have")], "C"),
        (11, "If you mix red and blue, you ________ purple.", [("A","will get"),("B","get"),("C","would get"),("D","got")], "B"),
        (12, "If I ________ what you were going through, I would have been more understanding.", [("A","know"),("B","knew"),("C","had known"),("D","would know")], "C"),
    ]
    fills = [
        (13, "If you ________ (heat) water to 100°C, it boils.", "heat"),
        (14, "If I ________ (have) enough money, I will buy a new phone.", "have"),
        (15, "If I ________ (be) you, I would accept the offer.", "were"),
        (16, "If he ________ (not / waste) so much time, he would have finished on time.", "had not wasted || hadn't wasted"),
        (17, "I wish I ________ (can) fly like a bird.", "could"),
        (18, "If she ________ (study) harder last term, she would have got better grades.", "had studied"),
        (19, "If you had told the truth, the teacher ________ (not / punish) you.", "would not have punished || wouldn't have punished"),
        (20, "If only I ________ (not / forget) to bring my umbrella!", "had not forgotten || hadn't forgotten"),
        (21, "If it ________ (rain) tomorrow, the match will be cancelled.", "rains"),
        (22, "He wishes he ________ (not / spend) all his savings last year.", "had not spent || hadn't spent"),
        (23, "If you had arrived five minutes earlier, you ________ (meet) the famous singer.", "would have met"),
        (24, "If I ________ (know) her phone number, I would call her right now.", "knew"),
    ]
    errs = [
        (25, "If I will see him, I will give him your message.", "If I see him, I will give him your message."),
        (26, "If I was you, I would not make the same mistake.", "If I were you, I would not make the same mistake."),
        (27, "If she had studied harder, she would passed the exam.", "If she had studied harder, she would have passed the exam."),
        (28, "I wish I am taller so that I can play basketball better.", "I wish I were taller so that I can play basketball better."),
        (29, "If you had told me about the party, I could come.", "If you had told me about the party, I could have come."),
    ]
    content = card("<h1>Unit 5: Conditional Sentences — Practice Test</h1><p><strong>滿分：100 分 | 建議時間：45 分鐘</strong></p>")
    content += card("<h2>Part 1: Multiple Choice 12題×3分=36分</h2>" + "".join(mc_question(n,s,o,c) for n,s,o,c in mc))
    content += card("<h2>Part 2: Fill in the Blanks 12題×3分=36分</h2>" + "".join(fill_question(n,s,c) for n,s,c in fills))
    content += card("<h2>Part 3: Error Correction 5題×3分=15分</h2>" +
                    "".join(f'<div class="question" data-answer="{c}"><p><strong>{n}.</strong> {s}</p><div class="answer-reveal" style="display:none;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {c}</div></div>' for n,s,c in errs))
    content += card("<h2>Part 4: Sentence Rewriting 8題（答案見下方）</h2>" +
                    "".join(fill_question(n,s,c) for n,s,c in [
                        (30, "I didn't take the medicine, so I didn't get better quickly. (改Type3)", "If I had taken the medicine, I would have got better quickly."),
                        (31, "He didn't study, and he failed the test. (用 wish)", "He wishes he had studied for the test."),
                        (32, "She is not tall enough to reach the shelf. (用 If only)", "If only she were taller!"),
                        (33, "I don't have a car, so I cannot drive you. (改Type2)", "If I had a car, I would drive you to the airport."),
                        (34, "They didn't save money, now they can't buy a house. (用 wish)", "They wish they had saved money."),
                        (35, "We didn't leave early, so we missed the train. (Type3 + could have)", "If we had left early, we could have caught the train."),
                        (36, "I want to become a pilot, but I have poor eyesight. (If only)", "If only I had better eyesight!"),
                        (37, "The alarm didn't ring, so I overslept and was late. (Type3 + might have)", "If the alarm had rung, I might not have been late for school."),
                    ]))
    content += card("<h2>Part 5: Matching 3題×2分=6分</h2>" +
                    "".join(fill_question(n,s,c) for n,s,c in [
                        (38, "If I had known you were coming, … (配對) → B", "B"),
                        (39, "If you heat ice, … (配對) → C", "C"),
                        (40, "If I had checked the weather forecast, … (配對) → A", "A"),
                    ]))
    content += card(test_buttons())
    return head("Unit 5 — Practice Test", "unit5_test.html") + content + tail()


# ============================================================
# Unit 6 Review Test
# ============================================================
def gen_unit6_review():
    mc = [
        (1, "Water ______ at 100 degrees Celsius.", [("A","boil"),("B","boils"),("C","is boiling"),("D","has boiled")], "B"),
        (2, "Look! The children ______ basketball.", [("A","play"),("B","plays"),("C","are playing"),("D","is playing")], "C"),
        (3, "I ______ a headache. Can I take a rest?", [("A","am having"),("B","have"),("C","has"),("D","having")], "B"),
        (4, "When I arrived, everyone ______ already ______.", [("A","has; left"),("B","had; left"),("C","was; leaving"),("D","did; leave")], "B"),
        (5, "By the time you get home, I ______ dinner ready.", [("A","will have"),("B","will be having"),("C","have had"),("D","had")], "A"),
        (6, "If I ______ you, I would accept the offer.", [("A","am"),("B","was"),("C","were"),("D","have been")], "C"),
        (7, "English ______ in many countries.", [("A","speaks"),("B","is spoken"),("C","is speaking"),("D","has spoken")], "B"),
        (8, "I wish I ______ more time to prepare for the exam.", [("A","have"),("B","had"),("C","would have"),("D","had had")], "B"),
        (9, "She ______ Chinese for three years. She speaks it quite well.", [("A","learns"),("B","learned"),("C","has been learning"),("D","had learned")], "C"),
        (10, "If it rains tomorrow, we ______ the picnic.", [("A","cancel"),("B","cancelled"),("C","will cancel"),("D","would cancel")], "C"),
        (11, "The chef ______ the soup at the moment.", [("A","tastes"),("B","is tasting"),("C","taste"),("D","has tasted")], "B"),
        (12, "A new hospital ______ near my house next year.", [("A","will build"),("B","will be built"),("C","is building"),("D","builds")], "B"),
        (13, "I ______ never ______ to Disneyland.", [("A","have; been"),("B","had; been"),("C","did; go"),("D","was; going")], "A"),
        (14, "If she had studied harder, she ______ the exam.", [("A","will pass"),("B","would pass"),("C","would have passed"),("D","passes")], "C"),
        (15, "We usually ______ to the cinema but this week we ______ at home.", [("A","go; stay"),("B","go; are staying"),("C","are going; stay"),("D","goes; stays")], "B"),
    ]
    fills = [
        (16, "Please be quiet! I _______________ (try) to concentrate.", "am trying"),
        (17, "She _______________ (already / finish) her homework before her mother came home.", "had already finished"),
        (18, "If I _______________ (be) rich, I would travel around the world.", "were"),
        (19, "The new road _______________ (build) at the moment.", "is being built"),
        (20, "I _______________ (meet) my friends for dinner tonight. We have booked.", "am meeting"),
        (21, "By the end of this year, I _______________ (live) here for five years.", "will have lived"),
        (22, "If you _______________ (heat) ice, it melts.", "heat"),
        (23, "She _______________ (not / have) a car, so she takes the bus.", "does not have || doesn't have"),
        (24, "The report _______________ (must / finish) before Friday.", "must be finished"),
        (25, "If I _______________ (know) about the party, I would have gone.", "had known"),
    ]
    errs = [
        (26, "I am wanting to buy a present.", "I want to buy a present."),
        (27, "I have seen a great movie yesterday.", "I saw a great movie yesterday."),
        (28, "If I will have time, I will help you.", "If I have time, I will help you."),
        (29, "The window broken by a ball yesterday.", "The window was broken by a ball yesterday."),
        (30, "Look at those clouds! It will rain soon.", "Look at those clouds! It is going to rain soon."),
    ]
    content = card("<h1>Unit 6: Review Test 1 — Units 1-5 綜合複習</h1><p><strong>總分：100 分 | 建議時限：60 分鐘</strong></p>")
    content += card("<h2>Section A: Multiple Choice 15題（每題2分=30分）</h2>" + "".join(mc_question(n,s,o,c) for n,s,o,c in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分=30分）</h2>" + "".join(fill_question(n,s,c) for n,s,c in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分=20分）</h2>" +
                    "".join(f'<div class="question" data-answer="{c}"><p><strong>{n}.</strong> {s}</p><div class="answer-reveal" style="display:none;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {c}</div></div>' for n,s,c in errs))
    content += card("<h2>Section D: Sentence Rewriting 5題（每題4分=20分）</h2>" +
                    "".join(fill_question(n,s,c) for n,s,c in [
                        (31, "The chef cooks dinner every evening. (改被動)", "Dinner is cooked by the chef every evening."),
                        (32, "First she finished homework, then she went out. (用Past Perfect)", "She had finished her homework before she went out."),
                        (33, "I don't have a car, so I can't drive to work. (改Type2條件句)", "If I had a car, I would drive to work."),
                        (34, "We have arranged to visit our grandparents this Sunday. (用Present Continuous)", "We are visiting our grandparents this Sunday."),
                        (35, "I didn't study hard for the exam, so I failed. (用wish)", "I wish I had studied hard for the exam."),
                    ]))
    content += card(test_buttons())
    return head("Unit 6 — Review Test", "unit6_review.html") + content + tail()


# ============================================================
# Unit 7 Study Material
# ============================================================
def gen_unit7_study():
    content = card("""
<h1>Unit 7: Verb + to-infinitive and Verb + Gerund</h1>
<p>英文中，某些動詞後面可以接 <strong>to-infinitive（不定式）</strong> 或 <strong>gerund（動名詞，即 V-ing）</strong>，但含義可能相似或完全不同。</p>
""")

    content += card("""
<h2>類別 1：意義相近的動詞</h2>
""" + table(["動詞", "to-infinitive", "gerund", "備註"], [
    ["begin", "began to rain", "began raining", "意思相同"],
    ["start", "started to cry", "started crying", "意思相同"],
    ["continue", "continued to talk", "continued talking", "意思相同"],
    ["hate", "hate to get up", "hate getting up", "口語中gerund更常見"],
    ["like / love", "likes to read", "likes reading", "意思相同"],
    ["prefer", "prefer to drink tea", "prefer drinking tea", "意思相同"],
]) + callout("warning", "⚠️ 特殊規則", """
進行式中用 to-inf：✗ It is beginning <em>raining</em>. → ✅ It is beginning <strong>to rain</strong>.<br>
+ know/realize/understand 用 to-inf：✗ begin <em>realizing</em> → ✅ begin <strong>to realize</strong>
"""))

    content += card("""
<h2>類別 2：意義改變的動詞 ⭐ 重點！</h2>
""" + table(["動詞", "+ to-infinitive", "+ gerund"], [
    ["remember", "記得要去做（未做）", "記得做過（已做）"],
    ["forget", "忘記去做（未做）", "忘記做過（已做）"],
    ["stop", "停下為了去做", "停止正在做的事"],
    ["try", "努力去做", "試試某方法"],
]) + """
<h3>記憶口訣</h3>
<ul>
<li><strong>to-do → 未做；doing → 已做</strong></li>
<li><strong>stop doing = 不做；stop to do = 停下為了做</strong></li>
<li><strong>try to do = 努力嘗試；try doing = 試試看</strong></li>
</ul>
""")

    content += card("""
<h2>go + gerund 常見搭配</h2>
""" + table(["短語", "中文"], [
    ["go shopping", "去購物"], ["go swimming", "去游泳"], ["go fishing", "去釣魚"],
    ["go hiking", "去遠足"], ["go camping", "去露營"], ["go running", "去跑步"],
    ["go skiing", "去滑雪"], ["go dancing", "去跳舞"], ["go sightseeing", "去觀光"],
    ["go jogging", "去慢跑"], ["go bowling", "去打保齡球"], ["go skating", "去溜冰"],
]))

    content += card("""
<h2>易錯點提醒</h2>
""" + table(["錯誤 ❌", "正確 ✅", "解析"], [
    ["I remember <strong>to lock</strong> the door, but I can't find my keys.", "I remember <strong>locking</strong> the door…", "已鎖了門（已做），用 gerund"],
    ["Please remember <strong>locking</strong> the door before you leave.", "Please remember <strong>to lock</strong>…", "還沒鎖（未做），用 to-inf"],
    ["He stopped <strong>to smoke</strong> because the doctor told him to quit.", "He stopped <strong>smoking</strong>…", "戒煙（停止抽煙）"],
    ["It is beginning <strong>raining</strong>.", "It is beginning <strong>to rain</strong>.", "進行式中用 to-inf"],
]))

    return head("Unit 7 — Verb + to-inf. & Gerund", "unit7_study.html") + content + tail()


# ============================================================
# Unit 7 Practice Test
# ============================================================
def gen_unit7_test():
    mc = [
        (1, "Please remember _____ the windows before you leave.", [("A","closing"),("B","to close"),("C","close"),("D","closed")], "B"),
        (2, "I will never forget _____ my favourite singer last year.", [("A","to see"),("B","seeing"),("C","see"),("D","saw")], "B"),
        (3, "The doctor advised me to stop _____ fast food.", [("A","to eat"),("B","eat"),("C","eating"),("D","ate")], "C"),
        (4, "She was tired, so she stopped _____ a short rest.", [("A","having"),("B","to have"),("C","have"),("D","had")], "B"),
        (5, "If the computer doesn't work, try _____ it off and on.", [("A","to turn"),("B","turning"),("C","turn"),("D","turned")], "B"),
        (6, "He tried his best _____ the heavy box.", [("A","lifting"),("B","lift"),("C","to lift"),("D","lifted")], "C"),
        (7, "It is beginning _____ dark outside.", [("A","getting"),("B","to get"),("C","get"),("D","got")], "B"),
        (8, "Did you remember _____ your grandmother? She said you didn't call.", [("A","to call"),("B","calling"),("C","call"),("D","called")], "A"),
        (9, "My father loves _____ golf at weekends.", [("A","to play"),("B","playing"),("C","play"),("D","both A and B")], "D"),
        (10, "Let's go _____ at the new shopping mall!", [("A","to shop"),("B","shop"),("C","shopping"),("D","shopped")], "C"),
        (11, "He began _____ how much his parents had done only when he became a father.", [("A","understanding"),("B","understand"),("C","to understand"),("D","understood")], "C"),
        (12, "I regret _____ you that your application has been rejected.", [("A","telling"),("B","to tell"),("C","tell"),("D","told")], "B"),
    ]
    fills = [
        (13, "She enjoys ______________ (swim) in the sea.", "swimming"),
        (14, "I have decided ______________ (study) abroad.", "to study"),
        (15, "He forgot ______________ (lock) the car door, so thieves stole his bag.", "to lock"),
        (16, "Do you remember ______________ (meet) me at the library last Monday?", "meeting"),
        (17, "My mother suggested ______________ (go) to the beach.", "going"),
        (18, "The teacher continued ______________ (explain) the grammar rules.", "to explain || explaining"),
        (19, "When I'm stressed, I find that ______________ (listen) to music helps.", "listening"),
        (20, "Please don't forget ______________ (bring) your calculator to the exam.", "to bring"),
        (21, "He stopped ______________ (tie) his shoelaces when he saw his friend.", "to tie"),
        (22, "I tried ______________ (study) with music on, but I couldn't concentrate.", "studying"),
        (23, "She will never forget ______________ (visit) the Great Wall when she was ten.", "visiting"),
        (24, "The weather is starting ______________ (get) colder.", "to get"),
    ]
    errs = [
        (25, 'I remembered locking the door before leaving. Actually, I forgot locking it.', 'I forgot to lock it.'),
        (26, "When she heard the news, she stopped to cry and wiped away her tears.", "She stopped crying and wiped away her tears."),
        (27, "They continued playing the game despite the rain.", "No error"),
        (28, "It's beginning getting dark, so we'd better hurry home.", "It's beginning to get dark, so we'd better hurry home."),
        (29, "He tried to use the new software but found it too complicated.", "No error"),
        (30, "I regret telling you that you have failed the test.", "I regret to tell you that you have failed the test."),
    ]
    content = card("<h1>Unit 7: Verb + to-infinitive and Gerund — Practice Test</h1><p><strong>總分：40 分 | 建議時間：45 分鐘</strong></p>")
    content += card("<h2>Section A: MC 12題（每題1分）</h2>" + "".join(mc_question(n,s,o,c) for n,s,o,c in mc))
    content += card("<h2>Section B: Fill in 12題（每題1分）</h2>" + "".join(fill_question(n,s,c) for n,s,c in fills))
    content += card("<h2>Section C: Error Correction 6題（每題2分）</h2>" +
                    "".join(f'<div class="question" data-answer="{c}"><p><strong>{n}.</strong> {s}</p><div class="answer-reveal" style="display:none;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {c}</div></div>' for n,s,c in errs))
    content += card("<h2>Section D: Sentence Rewriting 5題（每題2分）</h2>" +
                    "".join(fill_question(n,s,c) for n,s,c in [
                        (31, '"Need to buy milk on my way home" (用 remember)', 'remember to buy some milk on her way home'),
                        (32, "He tried hard to open the window, but it was stuck. (用 try)", "tried to open the window, but it was stuck"),
                        (33, "She takes a break from working every two hours to stretch. (用 stop)", "stops to stretch her legs every two hours"),
                        (34, "I called mother yesterday because I didn't want to forget. (用 remember)", "remembered to call my mother yesterday"),
                        (35, "We went to the beach and swam in the sea. (用 go)", "went swimming in the sea"),
                    ]))
    content += card(test_buttons())
    return head("Unit 7 — Practice Test", "unit7_test.html") + content + tail()


# ============================================================
# Unit 8 Study Material
# ============================================================
def gen_unit8_study():
    content = card("""
<h1>Unit 8: Adjective + to-infinitive 形容詞 + 不定式</h1>
<p>本教材涵蓋 <strong>It + be + adj + to-infinitive</strong>、<strong>S + be + adj + to-infinitive</strong>、<strong>too + adj + to-infinitive</strong> 及 <strong>adj + enough + to-infinitive</strong> 結構。</p>
""")

    content += card("""
<h2>8.1 It + be + adjective + to-infinitive</h2>
<p><strong>結構：</strong>It + be + 形容詞 + to-infinitive</p>
<p>It 作形式主語，真正的主語是後面的 to-infinitive 片語。</p>
<ul>
<li><strong>It is important</strong> to study for the exam.</li>
<li><strong>It is dangerous</strong> to swim alone.</li>
<li><strong>It is impossible</strong> to finish in one day.</li>
</ul>
""" + table(["類別", "形容詞", "例句"], [
    ["重要性", "important, necessary, essential", "It is vital to stay hydrated."],
    ["難易度", "easy, difficult, possible, impossible", "It is easy to make mistakes."],
    ["評價", "good, bad, nice, great, wonderful", "It is wonderful to have you here."],
    ["安全性", "safe, dangerous, risky", "It is not safe to cross here."],
    ["禮貌", "polite, rude, kind, generous", "It is polite to say thank you."],
]))

    content += card("""
<h2>8.2 Subject + be + adjective + to-infinitive</h2>
<p><strong>結構：</strong>S + be + adj + to-infinitive</p>
<ul>
<li>I <strong>am happy to help</strong> you. （感受）</li>
<li>He <strong>is kind to lend</strong> me his bike. （品質）</li>
<li>She <strong>was surprised to find</strong> the gift. （情感）</li>
</ul>
<h3>⚠️ 兩種結構的區別</h3>
""" + table(["結構", "主語", "重點", "例句"], [
    ["It + be + adj + to V", "It（形式主語）", "評價「做某事」", "It is important to exercise."],
    ["S + be + adj + to V", "人/物", "描述「某人」的感受", "I am happy to help."],
]))

    content += card("""
<h2>8.3 too + adjective + to-infinitive</h2>
<p><strong>結構：</strong>too + 形容詞 + to-infinitive</p>
<p><strong>意思：</strong>太⋯⋯以致不能⋯⋯（否定含義）</p>
<ul>
<li>The box <strong>is too heavy to carry</strong>.</li>
<li>She <strong>is too young to drive</strong>.</li>
<li>He <strong>is too tired to study</strong>.</li>
</ul>
""" + callout("tip", "💡 口訣", "「too + 形容詞 + to-infinitive = 太⋯⋯以至於不能⋯⋯」"))

    content += card("""
<h2>8.4 adjective + enough + to-infinitive</h2>
<p><strong>結構：</strong>形容詞 + enough + to-infinitive</p>
<p><strong>意思：</strong>足夠⋯⋯可以做某事（肯定含義）</p>
<ul>
<li>He <strong>is old enough to drive</strong>.</li>
<li>I <strong>am tall enough to reach</strong> the shelf.</li>
<li>She <strong>is smart enough to solve</strong> the problem.</li>
</ul>
""" + callout("warning", "⚠️ enough 位置很重要！", """
形容詞 + enough：old <strong>enough</strong>, tall <strong>enough</strong>（✗ enough old）<br>
enough + 名詞：<strong>enough</strong> money, <strong>enough</strong> time
"""))

    content += card("""
<h2>8.5 too...to vs enough...to 對比</h2>
""" + table(["too + adj + to V（否定）", "adj + enough + to V（肯定）"], [
    ["She is <strong>too short to reach</strong> the shelf.", "She is <strong>tall enough to reach</strong> the shelf."],
    ["The water is <strong>too cold to swim</strong> in.", "The water is <strong>warm enough to swim</strong> in."],
    ["He is <strong>too busy to help</strong> us.", "He is <strong>free enough to help</strong> us."],
]))

    content += card("""
<h2>考核要點 ✅</h2>
<ol>
<li><strong>It + be + adj + to V</strong>：評價做某事（It is important to...）</li>
<li><strong>S + be + adj + to V</strong>：描述人的感受/品質（I am happy to...）</li>
<li><strong>too + adj + to V</strong>：太⋯⋯而不能（否定含義）</li>
<li><strong>adj + enough + to V</strong>：足夠⋯⋯可以（肯定含義）</li>
<li><strong>enough 的位置</strong>：形容詞後（old enough）、名詞前（enough money）</li>
</ol>
""" + callout("danger", "⚠️ 易錯點", """
• 忘記 It 作形式主語：✗ To study is important. → ✅ It is important to study.<br>
• enough 位置錯誤：✗ enough old → ✅ old enough<br>
• 不定式前忘記 to：✗ happy help → ✅ happy <strong>to</strong> help<br>
• too...to 誤用肯定：✗ too young to not drive → ✅ too young to drive
"""))

    return head("Unit 8 — Adjective + to-infinitive", "unit8_study.html") + content + tail()


# ============================================================
# Unit 8 Practice Test
# ============================================================
def gen_unit8_test():
    mc = [
        (1, "It is important ______ for the exam.", [("A","study"),("B","studying"),("C","to study"),("D","studied")], "C"),
        (2, "She is ______ to drive a car. She is only 15.", [("A","too young"),("B","young enough"),("C","too young not"),("D","enough young")], "A"),
        (3, "I am very happy ______ you here today.", [("A","see"),("B","seeing"),("C","to see"),("D","saw")], "C"),
        (4, "He is ______ to solve the problem by himself.", [("A","too clever"),("B","clever enough"),("C","enough clever"),("D","so clever")], "B"),
        (5, "It was very kind ______ me with my luggage.", [("A","for you to help"),("B","of you to help"),("C","that you help"),("D","you to help")], "B"),
        (6, "The box is ______ for me to lift. Can you help?", [("A","too heavy"),("B","heavy enough"),("C","enough heavy"),("D","so heavy")], "A"),
        (7, "______ is difficult to learn a new language.", [("A","This"),("B","That"),("C","It"),("D","What")], "C"),
        (8, "You are ______ to win the competition!", [("A","too lucky"),("B","lucky enough"),("C","enough lucky"),("D","so lucky")], "B"),
        (9, "The water is ______ to swim in. Let's go!", [("A","too warm"),("B","warm enough"),("C","enough warm"),("D","so warm")], "B"),
        (10, "It was very rude ______ during the meeting.", [("A","of him to leave"),("B","for him to leave"),("C","that he leave"),("D","him to leave")], "A"),
    ]
    fills = [
        (11, "It ______________________________ (important / wear) a seatbelt.", "is important to wear"),
        (12, "She ______________________________ (kind / lend) me her notes.", "was kind to lend"),
        (13, "The coffee is ______________________________ (hot / drink).", "too hot to drink"),
        (14, "He is ______________________________ (tall / reach) the top shelf.", "tall enough to reach"),
        (15, "______________ is dangerous ______________ (swim) alone in the sea.", "It; to swim"),
        (16, "We were ______________________________ (surprised / hear) the news.", "surprised to hear"),
        (17, "The problem is ______________________________ (difficult / solve) in 5 min.", "too difficult to solve"),
        (18, "Are you ______________________________ (old / vote) in the next election?", "old enough to vote"),
        (19, "It was very ______________________________ (silly / him / believe) that story.", "silly of him to believe"),
        (20, "I am ______________________________ (tired / go) out tonight.", "too tired to go"),
    ]
    errs = [
        (21, "It is important studying hard for the exam.", "It is important to study hard for the exam."),
        (22, "He is enough old to drive a car.", "He is old enough to drive a car."),
        (23, "I am very happy help you with your homework.", "I am very happy to help you with your homework."),
        (24, "The bag is too heavy that I cannot carry it.", "The bag is too heavy to carry."),
        (25, "It was very kind for him to donate money.", "It was very kind of him to donate money."),
    ]
    content = card("<h1>Unit 8: Adjective + to-infinitive — Practice Test</h1><p><strong>總分：100 分 | 建議時限：40 分鐘</strong></p>")
    content += card("<h2>Section A: MC 10題（每題2分）</h2>" + "".join(mc_question(n,s,o,c) for n,s,o,c in mc))
    content += card("<h2>Section B: Fill in 10題（每題3分）</h2>" + "".join(fill_question(n,s,c) for n,s,c in fills))
    content += card("<h2>Section C: Error Correction 5題（每題4分）</h2>" +
                    "".join(f'<div class="question" data-answer="{c}"><p><strong>{n}.</strong> {s}</p><div class="answer-reveal" style="display:none;padding:8px 12px;background:#f0fdf4;border-radius:6px;border-left:4px solid #16a34a;">✅ {c}</div></div>' for n,s,c in errs))
    content += card("<h2>Section D: Sentence Rewriting 5題（每題6分）</h2>" +
                    "".join(fill_question(n,s,c) for n,s,c in [
                        (26, "Learning a new language is fun. (用 It + be + adj)", "It is fun to learn a new language."),
                        (27, "She is so young that she cannot watch this movie. (用 too...to)", "She is too young to watch this movie."),
                        (28, "He is very strong. He can carry the piano. (用 adj + enough)", "He is strong enough to carry the piano by himself."),
                        (29, "It was generous of her to donate all that money. (用 S + be + adj)", "She was generous to donate all that money."),
                        (30, "I am so busy that I cannot take a holiday this year. (用 too...to)", "I am too busy to take a holiday this year."),
                    ]))
    content += card(test_buttons())
    return head("Unit 8 — Practice Test", "unit8_test.html") + content + tail()


# ============================================================
# Generate all files
# ============================================================
def main():
    files = {
        "unit2_study.html": gen_unit2_study(),
        "unit2_test.html": gen_unit2_test(),
        "unit3_study.html": gen_unit3_study(),
        "unit3_test.html": gen_unit3_test(),
        "unit4_study.html": gen_unit4_study(),
        "unit4_test.html": gen_unit4_test(),
        "unit5_study.html": gen_unit5_study(),
        "unit5_test.html": gen_unit5_test(),
        "unit6_review.html": gen_unit6_review(),
        "unit7_study.html": gen_unit7_study(),
        "unit7_test.html": gen_unit7_test(),
        "unit8_study.html": gen_unit8_study(),
        "unit8_test.html": gen_unit8_test(),
    }

    for name, content in files.items():
        path = os.path.join(HTML_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Created: {name} ({len(content)} chars)")

if __name__ == "__main__":
    main()
