# seed_polity_ch30.py — Tribunals
# Ch30 of M. Lakshmikanth's Indian Polity
# Sections:
#   0 — Administrative Tribunals — Art.323A        (8 MCQs)
#   1 — Other Tribunals — Art.323B                 (8 MCQs)
#   2 — Central Administrative Tribunal (CAT)      (8 MCQs)
#   3 — National Green Tribunal (NGT)              (8 MCQs)
#   4 — National Company Law Tribunal (NCLT)       (8 MCQs)
#   5 — Income Tax Appellate Tribunal & others     (8 MCQs)
#   6 — Tribunal features & comparison             (8 MCQs)
#   7 — Tribunals vs Courts & constitutional basis (8 MCQs)

_CH          = 30
_SUBJECT     = 'GK'
_TOPIC       = 'Indian_Polity'
_TITLE_TE    = 'ట్రిబ్యునళ్ళు'
_TITLE_EN    = 'Tribunals'
_PAGES       = 'Ch 30'
_SECTIONS    = [
    "పరిపాలనా ట్రిబ్యునళ్ళు — Art.323A",
    "ఇతర ట్రిబ్యునళ్ళు — Art.323B",
    "కేంద్ర పరిపాలనా ట్రిబ్యునల్ (CAT)",
    "జాతీయ హరిత ట్రిబ్యునల్ (NGT)",
    "జాతీయ కంపెనీ న్యాయ ట్రిబ్యునల్ (NCLT)",
    "ఆదాయ పన్ను అప్పీలేట్ ట్రిబ్యునల్ & ఇతరాలు",
    "ట్రిబ్యునళ్ళ లక్షణాలు & పోలిక",
    "ట్రిబ్యునళ్ళు vs కోర్టులు & రాజ్యాంగ ఆధారం",
]

NOTES_HTML = """<!DOCTYPE html>
<html lang="te">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ch30 – Tribunals</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;600;700&family=Noto+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Noto Sans Telugu','Noto Sans',sans-serif;font-size:15px;line-height:1.6;background:#f5f5f5;color:#212121}
  .page{width:210mm;min-height:297mm;margin:0 auto 18px;background:#fff;padding:14mm 13mm 12mm;box-shadow:0 2px 8px rgba(0,0,0,.13)}
  .hdr{background:linear-gradient(135deg,#bf360c 0%,#e64a19 100%);color:#fff;border-radius:8px;padding:14px 18px 10px;margin-bottom:14px}
  .hdr h1{font-size:20px;font-weight:700;letter-spacing:.3px}
  .hdr h2{font-size:13px;font-weight:400;opacity:.88;margin-top:3px}
  .badge{display:inline-block;background:rgba(255,255,255,.2);border-radius:12px;padding:2px 10px;font-size:11.5px;margin-top:6px}
  .sh{font-size:14px;font-weight:700;color:#bf360c;background:#fbe9e7;border-left:5px solid #e64a19;border-radius:0 5px 5px 0;padding:5px 10px;margin:12px 0 7px}
  .c{border-radius:6px;padding:9px 12px;margin-bottom:7px;border:1px solid transparent}
  .c.r{background:#fff8f8;border-color:#ffcdd2}
  .c.b{background:#e3f2fd;border-color:#90caf9}
  .c.a{background:#fff8e1;border-color:#ffe082}
  .c.p{background:#f3e5f5;border-color:#ce93d8}
  .c.g{background:#e8f5e9;border-color:#a5d6a7}
  .c.gr{background:#f5f5f5;border-color:#e0e0e0}
  .c.t{background:#fbe9e7;border-color:#ffab91}
  .ch{font-size:13px;font-weight:700;color:#bf360c;border-bottom:1px solid #ffccbc;padding-bottom:4px;margin-bottom:5px}
  .fact{margin:3px 0;font-size:14.5px}
  .fact::before{content:"• ";color:#e64a19;font-weight:700}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:8px}
  table{width:100%;border-collapse:collapse;font-size:13px;margin-top:4px}
  th{background:#bf360c;color:#fff;padding:5px 8px;text-align:left}
  td{padding:4px 8px;border-bottom:1px solid #ffccbc}
  tr:nth-child(even) td{background:#fbe9e7}
  .pills{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
  .pill{background:#bf360c;color:#fff;border-radius:20px;padding:3px 12px;font-size:12.5px}
  .pill.o{background:#e64a19}
  .pill.b{background:#1565c0}
  .pill.g{background:#2e7d32}
  .pill.r{background:#880e4f}
  .pill.p{background:#6a1b9a}
</style>
</head>
<body>

<!-- PAGE 1 -->
<div class="page">
<div class="hdr">
  <h1>Ch 30 — ట్రిబ్యునళ్ళు (Tribunals)</h1>
  <h2>Art.323A • Art.323B • CAT • NGT • NCLT • 42వ సవరణ 1976</h2>
  <span class="badge">Indian Polity</span>
</div>

<!-- Section 1: Art.323A -->
<div class="sh">⚖️ 1. పరిపాలనా ట్రిబ్యునళ్ళు — Art.323A</div>
<div class="two">
  <div class="c b">
    <div class="ch">Art.323A నిబంధనలు</div>
    <div class="fact">Art.323A: 42వ సవరణ (1976) ద్వారా చేర్చబడింది</div>
    <div class="fact">Parliament సర్వీసు విషయాలపై Administrative Tribunals ఏర్పాటు చేయవచ్చు</div>
    <div class="fact">కేంద్ర & రాష్ట్ర సేవకుల నియామకం, షరతులు, సేవా వివాదాలు</div>
    <div class="fact">Administrative Tribunals Act, 1985 కింద CAT స్థాపన</div>
  </div>
  <div class="c t">
    <div class="ch">Art.323A vs Art.323B తేడా</div>
    <div class="fact">Art.323A = Administrative (service) matters మాత్రమే; Parliament alone</div>
    <div class="fact">Art.323B = 9 రంగాలలో Tribunals; Parliament OR State Legislature</div>
    <div class="fact">Art.323A: HC jurisdiction excluded (పాక్షికంగా)</div>
    <div class="fact">Art.323B: HC jurisdiction excluded (Parliament/State law ద్వారా)</div>
  </div>
</div>

<!-- Section 2: Art.323B -->
<div class="sh">📋 2. ఇతర ట్రిబ్యునళ్ళు — Art.323B (9 రంగాలు)</div>
<div class="c a">
  <div class="ch">Art.323B — 9 Specified Matters</div>
  <div class="two">
    <div>
      <div class="fact">1. Taxation</div>
      <div class="fact">2. Foreign Exchange, Import-Export</div>
      <div class="fact">3. Industrial & Labour disputes</div>
      <div class="fact">4. Land reforms</div>
      <div class="fact">5. Ceiling on urban property</div>
    </div>
    <div>
      <div class="fact">6. Elections to Parliament & State Legislatures</div>
      <div class="fact">7. Production, procurement, supply, distribution of essential goods</div>
      <div class="fact">8. Rent & tenancy rights</div>
      <div class="fact">9. Offences against laws on any of above matters</div>
    </div>
  </div>
</div>

<!-- Section 3: CAT -->
<div class="sh">🏛️ 3. కేంద్ర పరిపాలనా ట్రిబ్యునల్ (CAT)</div>
<div class="c g">
  <div class="ch">CAT — Central Administrative Tribunal</div>
  <div class="two">
    <div>
      <div class="fact">స్థాపన: 1985 (Administrative Tribunals Act, 1985)</div>
      <div class="fact">Headquarters: New Delhi</div>
      <div class="fact">Principal Bench: New Delhi; Circuit Benches across India</div>
      <div class="fact">Chairman: Retired SC / HC Judge</div>
    </div>
    <div>
      <div class="fact">పరిధి: Central Govt సేవకులు (IAS, IPS సహా)</div>
      <div class="fact">SC కి direct appeal (HC skip)</div>
      <div class="fact">L. Chandra Kumar case (1997): HC jurisdiction restored</div>
      <div class="fact">SC Art.226/227 writ jurisdiction — CAT orders challenge చేయవచ్చు</div>
    </div>
  </div>
</div>

<!-- Key Tribunals Table -->
<div class="sh">📊 4. ముఖ్యమైన Tribunals</div>
<table>
  <tr><th>Tribunal</th><th>స్థాపన</th><th>రంగం</th><th>చట్టం</th></tr>
  <tr><td>CAT</td><td>1985</td><td>Central Govt service matters</td><td>Administrative Tribunals Act, 1985</td></tr>
  <tr><td>NGT</td><td>2010</td><td>Environmental protection</td><td>NGT Act, 2010</td></tr>
  <tr><td>NCLT</td><td>2016</td><td>Company law matters</td><td>Companies Act, 2013</td></tr>
  <tr><td>NCLAT</td><td>2016</td><td>NCLT appeals</td><td>Companies Act, 2013</td></tr>
  <tr><td>ITAT</td><td>1941</td><td>Income Tax appeals</td><td>Income Tax Act</td></tr>
  <tr><td>CESTAT</td><td>1982</td><td>Customs & Excise</td><td>Customs/Central Excise</td></tr>
  <tr><td>AFT</td><td>2009</td><td>Armed Forces service matters</td><td>Armed Forces Tribunal Act, 2007</td></tr>
  <tr><td>TDSAT</td><td>2000</td><td>Telecom disputes</td><td>TRAI Act, 1997</td></tr>
</table>
</div>

<!-- PAGE 2 -->
<div class="page">

<!-- Section 5: NGT -->
<div class="sh">🌿 5. జాతీయ హరిత ట్రిబ్యునల్ (NGT)</div>
<div class="two">
  <div class="c g">
    <div class="ch">NGT విశేషాలు</div>
    <div class="fact">స్థాపన: అక్టోబర్ 18, 2010 (NGT Act, 2010)</div>
    <div class="fact">Headquarters: New Delhi; Regional Benches: 4</div>
    <div class="fact">Chairperson: Retired SC Judge</div>
    <div class="fact">పరిధి: Environment Protection Act, Water Act, Air Act, Biodiversity Act, Forest Conservation Act</div>
  </div>
  <div class="c b">
    <div class="ch">NGT విశేష అంశాలు</div>
    <div class="fact">India = 3వ దేశం NGT ఉన్న (Australia, New Zealand తర్వాత)</div>
    <div class="fact">Case నిర్ణయం: 6 నెలల్లో తీర్చాలి (statutory)</div>
    <div class="fact">NGT orders పై: SC కి direct appeal</div>
    <div class="fact">Art.21 (Right to Life) + Clean environment = NGT foundation</div>
  </div>
</div>

<!-- Section 6: Tribunals features -->
<div class="sh">⚖️ 6. Tribunals vs Courts</div>
<table>
  <tr><th>విషయం</th><th>Courts</th><th>Tribunals</th></tr>
  <tr><td>స్వభావం</td><td>Constitutional/Statutory</td><td>Statutory (mostly)</td></tr>
  <tr><td>నిర్ణయం</td><td>Judicial</td><td>Quasi-judicial</td></tr>
  <tr><td>సభ్యులు</td><td>Judges (law background)</td><td>Judicial + Technical members</td></tr>
  <tr><td>విచారణ</td><td>Formal procedures (CPC/CrPC)</td><td>Flexible/simplified procedures</td></tr>
  <tr><td>Appeals</td><td>Hierarchical courts</td><td>Mostly direct to SC/HC</td></tr>
  <tr><td>Purpose</td><td>General justice</td><td>Specialized/faster justice</td></tr>
</table>

<!-- Quick Revision Pills -->
<div class="sh">⚡ Quick Revision Pills</div>
<div class="pills">
  <span class="pill">Art.323A = Administrative Tribunals (42వ Amendment 1976)</span>
  <span class="pill o">Art.323B = 9 matters; Parliament or State Legislature</span>
  <span class="pill b">CAT = 1985; Central Govt service disputes</span>
  <span class="pill g">NGT = 2010; Environment; SC judge chairs</span>
  <span class="pill r">NCLT = 2016; Companies Act 2013</span>
  <span class="pill p">ITAT = 1941 (oldest tribunal)</span>
  <span class="pill">L. Chandra Kumar (1997): HC jurisdiction restored over Tribunals</span>
  <span class="pill o">NGT = India's 3rd country with Green Tribunal</span>
  <span class="pill b">AFT = 2009; Armed Forces matters</span>
  <span class="pill g">TDSAT = 2000; Telecom disputes</span>
  <span class="pill r">NGT Headquarters = New Delhi; 4 Regional Benches</span>
  <span class="pill p">CAT = SC judge chairs; appeals direct to SC</span>
</div>
</div>

</body>
</html>"""

_MCQS = [
    # ── Section 0: Administrative Tribunals — Art.323A ───────────────────────
    (0, "easy",
     "Art.323A ని రాజ్యాంగంలో ఏ సవరణ ద్వారా చేర్చారు? / Art.323A was added by which Amendment?",
     "32వ Amendment",
     "42వ Amendment",
     "44వ Amendment",
     "73వ Amendment",
     "b",
     "Art.323A 42వ Constitutional Amendment (1976) ద్వారా రాజ్యాంగంలో చేర్చబడింది. Administrative Tribunals కి రాజ్యాంగ హోదా ఇచ్చింది. / Art.323A inserted by 42nd Constitutional Amendment, 1976 — gave constitutional status to Administrative Tribunals."),

    (0, "easy",
     "Art.323A కింద Tribunals ఏ విషయాలకు సంబంధించి ఏర్పాటు చేయవచ్చు? / Art.323A tribunals deal with?",
     "Tax disputes",
     "Environmental issues",
     "Service matters of public servants",
     "Election disputes",
     "c",
     "Art.323A: కేంద్ర & రాష్ట్ర ప్రభుత్వ సేవకుల recruitment, conditions of service, tenure, pay, leave, seniority — సేవా సంబంధ వివాదాలు. / Art.323A: Tribunals for recruitment and service matters of public servants under Centre and states."),

    (0, "medium",
     "Art.323A కింద Administrative Tribunals ఏర్పాటు చేయగల body ఎవరు? / Who can set up tribunals under Art.323A?",
     "Parliament మాత్రమే",
     "రాష్ట్ర Legislature మాత్రమే",
     "Parliament + State Legislatures రెండూ",
     "రాష్ట్రపతి Order మాత్రమే",
     "a",
     "Art.323A కింద Administrative Tribunals కేవలం Parliament మాత్రమే ఏర్పాటు చేయవచ్చు — రాష్ట్ర Legislatures కాదు. (Art.323B లో రెండూ చేయగలవు.) / Art.323A: Only Parliament can establish administrative tribunals. (Art.323B allows both Parliament and State Legislatures.)"),

    (0, "medium",
     "Administrative Tribunals Act ఏ సంవత్సరం ఆమోదించబడింది? / Administrative Tribunals Act was passed in?",
     "1976",
     "1980",
     "1985",
     "1990",
     "c",
     "Administrative Tribunals Act 1985 లో ఆమోదించబడింది. దీని కింద Central Administrative Tribunal (CAT) మరియు State Administrative Tribunals ఏర్పాటయ్యాయి. / Administrative Tribunals Act, 1985 — under which CAT and State Administrative Tribunals were established."),

    (0, "medium",
     "Art.323A కింద Tribunal నిర్ణయాలపై సాధారణంగా ఏ Court కి appeal చేయవచ్చు? / Appeals from Art.323A Tribunals go to?",
     "District Court",
     "High Court",
     "Supreme Court directly",
     "President",
     "c",
     "Art.323A ప్రకారం originally HC jurisdiction excluded; Supreme Court కి direct appeal. కానీ L. Chandra Kumar case (1997): SC HC jurisdiction (Art.226) restore చేసింది. ఇప్పుడు: HC Division Bench → SC. / Originally: direct appeal to SC. After L. Chandra Kumar (1997): HC can review tribunal orders under Art.226."),

    (0, "medium",
     "Art.323A(2)(d) ప్రకారం Tribunals దేనిని exclude చేయగలవు? / Under Art.323A(2)(d), tribunals can exclude?",
     "Parliament jurisdiction",
     "SC original jurisdiction",
     "HC jurisdiction — service matters కి (except Art.136)",
     "President's powers",
     "c",
     "Art.323A(2)(d): Parliament law ద్వారా HC జ్యూరిస్‌డిక్షన్‌ను Service matters పై (Art.226, 227 under) exclude చేయవచ్చు — SC Art.136 SLP తప్ప. కానీ L. Chandra Kumar case తర్వాత HC jurisdiction partially restored. / Art.323A(2)(d): Parliament can exclude HC jurisdiction over service matters (Art.226/227), except SC Art.136."),

    (0, "hard",
     "L. Chandra Kumar vs. Union of India (1997) కేసు ఏమి నిర్ణయించింది? / What did L. Chandra Kumar case (1997) decide?",
     "CAT రద్దు చేయాలి",
     "CAT orders పై HC Art.226 writ jurisdiction excluded ఉండలేదు — Basic Structure",
     "CAT కి SC జ్యూరిస్‌డిక్షన్ excluded",
     "Tribunal members judges కావాలి",
     "b",
     "L. Chandra Kumar vs. Union of India (1997): SC 7-judge bench — Tribunals, including CAT, orders పై HC (Art.226) మరియు SC (Art.32) judicial review = Basic Structure. HC jurisdiction exclude చేయడం unconstitutional. / L. Chandra Kumar (1997): Exclusion of HC's judicial review over tribunal orders is unconstitutional — judicial review is part of Basic Structure."),

    (0, "toughest",
     "Art.323A మరియు Art.323B మధ్య ముఖ్యమైన తేడా ఏమిటి? / Key difference between Art.323A and Art.323B?",
     "323A environmental; 323B service matters",
     "323A only Parliament; 323B Parliament or State Legislatures; 323A = services only, 323B = 9 specified matters",
     "323A constitutional body; 323B statutory",
     "తేడా లేదు",
     "b",
     "Art.323A: Only Parliament can set up; only service/administrative matters. Art.323B: Both Parliament and State Legislatures can set up; 9 specified subjects (tax, elections, land reforms etc.). / Art.323A: Parliament only + service matters. Art.323B: Parliament/States + 9 subjects."),

    # ── Section 1: Art.323B — Other Tribunals ─────────────────────────────────
    (1, "easy",
     "Art.323B కింద ఏర్పాటు చేయగల Tribunals ఏ విషయాలకు సంబంధించినవి? / Art.323B tribunals cover how many specified matters?",
     "5 matters",
     "7 matters",
     "9 matters",
     "12 matters",
     "c",
     "Art.323B: 9 specified matters పై Parliament లేదా State Legislature Tribunals ఏర్పాటు చేయవచ్చు: Taxation, Foreign Exchange, Industrial/Labour disputes, Land reforms, Urban property ceiling, Elections, Essential goods, Rent/tenancy, Offences against above. / Art.323B: 9 specified matters."),

    (1, "easy",
     "Art.323B కింద Tribunals ఎవరు ఏర్పాటు చేయవచ్చు? / Who can set up tribunals under Art.323B?",
     "Parliament మాత్రమే",
     "రాష్ట్ర Legislature మాత్రమే",
     "Parliament లేదా State Legislature రెండూ",
     "President Order మాత్రమే",
     "c",
     "Art.323B కింద Parliament లేదా State Legislature — రెండూ వాటి పరిధిలోని 9 specified matters పై Tribunals ఏర్పాటు చేయవచ్చు. Art.323A కంటే broader. / Art.323B: Both Parliament and State Legislatures can set up tribunals for 9 specified matters."),

    (1, "medium",
     "Art.323B కింద Elections కి సంబంధించిన వివాదాలకు Tribunal ఏర్పాటు చేయవచ్చా? / Can a tribunal be set up for election disputes under Art.323B?",
     "కాదు — SC మాత్రమే",
     "అవును — Art.323B(2)(f): Elections to Parliament & State Legislatures",
     "కేవలం HC మాత్రమే",
     "EC నిర్ణయిస్తుంది",
     "b",
     "Art.323B(2)(f): Parliament and State Legislature elections కి సంబంధించిన disputes కోసం Tribunals ఏర్పాటు చేయవచ్చు. కానీ presidential/VP elections: SC పరిధి (Art.71) వేరేగా ఉంటుంది. / Art.323B(2)(f): Tribunals can be set up for disputes relating to elections to Parliament and State Legislatures."),

    (1, "medium",
     "Art.323B (Land Reform matters) కింద Land reforms Tribunals ఏ List లో subject? / Land reforms under Art.323B is originally in which List?",
     "Union List",
     "State List",
     "Concurrent List",
     "Residuary",
     "b",
     "Land reforms = State List Entry 18. Art.323B(2)(d) కింద Land reform matters పై State Legislature Tribunals ఏర్పాటు చేయవచ్చు. / Land reforms: State List. Art.323B(2)(d): State Legislatures can set up tribunals for land reform matters."),

    (1, "medium",
     "Art.323B కింద Taxation కి సంబంధించిన Tribunal ఏది? / Tribunal for taxation disputes under Art.323B?",
     "CAT",
     "NGT",
     "ITAT (Income Tax Appellate Tribunal)",
     "CESTAT",
     "c",
     "ITAT (Income Tax Appellate Tribunal) Taxation disputes కి. Art.323B(2)(a): Taxation matters పై Tribunals. ITAT 1941లో స్థాపించబడింది — India యొక్క oldest Tribunal. / ITAT (Income Tax Appellate Tribunal) — handles taxation disputes under Art.323B(2)(a)."),

    (1, "medium",
     "Art.323B(2)(c) Industrial & Labour disputes కోసం ఏ Tribunals ఉన్నాయి? / Tribunals for Industrial & Labour disputes?",
     "CAT",
     "NCLT",
     "Industrial Tribunals & Labour Courts",
     "NGT",
     "c",
     "Art.323B(2)(c): Industrial and labour dispute matters. Industrial Tribunals, Labour Courts = Industries Disputes Act 1947 కింద. / Industrial Tribunals and Labour Courts handle industrial/labour disputes under Art.323B(2)(c)."),

    (1, "hard",
     "Art.323B కింద Urban Property Ceiling కి సంబంधించిన Tribunal ఏది? / Art.323B(2)(e) relates to?",
     "Agricultural land ceiling",
     "Urban immovable property ceiling",
     "Industrial property",
     "Forest land",
     "b",
     "Art.323B(2)(e): Ceiling on urban immovable property — పట్టణ భూ గరిష్ట పరిమితి సంబంధిత వివాదాలు. Urban Land (Ceiling & Regulation) Act, 1976 (now repealed in most states). / Art.323B(2)(e): ceiling on urban immovable property."),

    (1, "toughest",
     "Art.323B Tribunals కి 42వ Amendment ముందు రాజ్యాంగ హోదా ఉందా? / Did Art.323B tribunals have constitutional status before 42nd Amendment?",
     "అవును — original Constitution లో ఉన్నాయి",
     "లేదు — Parliament & State Legislatures ordinary laws ద్వారా ఏర్పాటు చేసేవి",
     "అవును — Art.226 కింద",
     "కేవలం SC ఆమోదంతో",
     "b",
     "42వ Amendment (1976) ముందు Tribunals కి రాజ్యాంగ హోదా లేదు — ordinary legislation ద్వారా ఏర్పాటయ్యేవి. 42వ Amendment Art.323A & 323B చేర్చి constitutional basis ఇచ్చింది. / Before 42nd Amendment (1976): no constitutional basis for tribunals — created by ordinary legislation. 42nd Amendment gave constitutional status via Art.323A & 323B."),

    # ── Section 2: CAT ────────────────────────────────────────────────────────
    (2, "easy",
     "CAT అంటే ఏమిటి? / What does CAT stand for?",
     "Central Arbitration Tribunal",
     "Central Administrative Tribunal",
     "Civil Appellate Tribunal",
     "Central Audit Tribunal",
     "b",
     "CAT = Central Administrative Tribunal. Art.323A + Administrative Tribunals Act, 1985 కింద 1985లో స్థాపించబడింది. / CAT: Central Administrative Tribunal — established in 1985 under Administrative Tribunals Act, 1985."),

    (2, "easy",
     "CAT ఏ సంవత్సరంలో స్థాపించబడింది? / CAT was established in?",
     "1976",
     "1980",
     "1985",
     "1990",
     "c",
     "CAT (Central Administrative Tribunal) Administrative Tribunals Act, 1985 కింద 1985లో స్థాపించబడింది. Principal Bench: New Delhi. / CAT established in 1985 under Administrative Tribunals Act, 1985; Principal Bench in New Delhi."),

    (2, "easy",
     "CAT Chairperson అర్హత ఏమిటి? / Qualification for CAT Chairperson?",
     "IAS Officer",
     "Retired High Court Judge",
     "Retired Supreme Court Judge or Chief Justice of High Court",
     "Union Public Service Commission member",
     "c",
     "CAT Chairperson = Retired Supreme Court Judge లేదా High Court Chief Justice. Members = Judicial members + Administrative members. / CAT Chairperson: retired SC judge or HC Chief Justice."),

    (2, "medium",
     "CAT పరిధిలో ఉండే సేవకులు ఎవరు? / Who falls under CAT's jurisdiction?",
     "Only IAS officers",
     "All Central Govt employees including IAS, IPS (not defence)",
     "Only Gazetted officers",
     "State Govt employees",
     "b",
     "CAT Central Government employees అందరికీ వర్తిస్తుంది — IAS, IPS సహా. కానీ Defence Services (Army, Navy, Air Force) = Armed Forces Tribunal (AFT) పరిధి. / CAT jurisdiction: all central govt employees including IAS, IPS (excluding defence — they go to AFT)."),

    (2, "medium",
     "CAT Benches ఎక్కడ ఉన్నాయి? / How many benches does CAT have?",
     "3 Benches",
     "5 Benches",
     "17 Benches",
     "32 Benches",
     "c",
     "CAT కి Principal Bench (New Delhi) + 16 Circuit/Regular Benches = 17 Benches మొత్తం. Major cities లో అన్ని states cover అవుతాయి. / CAT: Principal Bench (New Delhi) + 16 Regular Benches = 17 benches across India."),

    (2, "medium",
     "CAT orders పై appeal ఎక్కడ వేయవచ్చు? (L. Chandra Kumar తర్వాత) / Where can CAT orders be challenged after L. Chandra Kumar?",
     "Supreme Court directly (SLP)",
     "High Court Division Bench (Art.226), then SC",
     "President petition",
     "Union Cabinet",
     "b",
     "L. Chandra Kumar (1997) తర్వాత: CAT orders → HC Division Bench (Art.226 Writ) → SC (SLP). ముందు: CAT → SC directly. / Post L. Chandra Kumar (1997): CAT → HC Division Bench (Art.226) → SC via SLP."),

    (2, "hard",
     "SATs (State Administrative Tribunals) ఏ రాష్ట్రాలలో ఏర్పాటయ్యాయి? / State Administrative Tribunals exist in which states?",
     "అన్ని రాష్ట్రాలలో",
     "కొన్ని రాష్ట్రాలు మాత్రమే — ఉదా. AP, HP, WB, Karnataka",
     "కేవలం 3 రాష్ట్రాలు",
     "No state has SAT",
     "b",
     "SATs కొన్ని రాష్ట్రాలలో మాత్రమే ఏర్పాటయ్యాయి: Andhra Pradesh, Himachal Pradesh, Karnataka, West Bengal, Odisha, Tamil Nadu తదితర. అన్ని రాష్ట్రాలు ఏర్పాటు చేయలేదు. / SATs exist in select states only (AP, HP, WB, Karnataka etc.); not all states have SATs."),

    (2, "toughest",
     "CAT Judicial Members మరియు Administrative Members తేడా ఏమిటి? / Difference between Judicial and Administrative Members of CAT?",
     "Judicial = retired judges; Administrative = IAS/Civil Service (Group A) officers with 15+ years experience",
     "Judicial = current judges; Administrative = accountants",
     "No difference — both are judges",
     "Judicial = HC judges; Administrative = IAS only",
     "a",
     "CAT Judicial Members: Retired HC Judges లేదా District Judge equivalent experience. Administrative Members: Central Govt Group A officers with at least 15 years experience. / CAT Judicial Members: retired HC judges; Administrative Members: Group A civil servants with 15+ years experience."),

    # ── Section 3: NGT ────────────────────────────────────────────────────────
    (3, "easy",
     "NGT అంటే ఏమిటి? / What does NGT stand for?",
     "National Government Tribunal",
     "National Green Tribunal",
     "National Governance Tribunal",
     "National Grievance Tribunal",
     "b",
     "NGT = National Green Tribunal. Environment సంబంధిత వివాదాల పరిష్కారానికి. / NGT: National Green Tribunal — handles environmental disputes."),

    (3, "easy",
     "NGT ఏ సంవత్సరంలో స్థాపించబడింది? / NGT was established in?",
     "2005",
     "2008",
     "2010",
     "2012",
     "c",
     "NGT అక్టోబర్ 18, 2010 న National Green Tribunal Act, 2010 కింద స్థాపించబడింది. / NGT established on October 18, 2010 under NGT Act, 2010."),

    (3, "easy",
     "NGT Chairperson ఎవరు అవుతారు? / Who chairs the NGT?",
     "Retired IFS Officer",
     "Retired High Court Judge",
     "Retired Supreme Court Judge",
     "Environment Ministry Secretary",
     "c",
     "NGT Chairperson = Retired Supreme Court Judge. Expert Members కూడా ఉంటారు — environment/science background. / NGT Chairperson: retired Supreme Court judge."),

    (3, "medium",
     "NGT Headquarters ఎక్కడ ఉంది? / Where is NGT Headquarters?",
     "Mumbai",
     "Chennai",
     "New Delhi",
     "Bhopal",
     "c",
     "NGT Headquarters New Delhi లో ఉంది. Regional Benches: Bhopal, Pune, Kolkata, Chennai. / NGT HQ: New Delhi. Regional Benches: Bhopal, Pune, Kolkata, Chennai."),

    (3, "medium",
     "NGT ఏ చట్టాల ఉల్లంఘనలపై విచారించగలదు? / NGT has jurisdiction over violations of which Acts?",
     "Only Environment Protection Act",
     "Environment Protection Act, Water Act, Air Act, Forest Conservation Act, Biodiversity Act",
     "Criminal cases related to environment",
     "Land acquisition disputes",
     "b",
     "NGT జ్యూరిస్‌డిక్షన్: Environment Protection Act 1986, Water (Prevention & Control) Act 1974, Air Act 1981, Forest Conservation Act 1980, Biological Diversity Act 2002. / NGT: Environment Protection Act, Water Act, Air Act, Forest Conservation Act, Biodiversity Act."),

    (3, "medium",
     "NGT India ఎన్నవ దేశంగా స్థాపించింది? / India was which country to have a dedicated Green Tribunal?",
     "1వ",
     "2వ",
     "3వ",
     "5వ",
     "c",
     "India NGT స్థాపించిన 3వ దేశం — Australia (Land and Environment Court) మరియు New Zealand తర్వాత. / India is the 3rd country to establish a dedicated Green Tribunal — after Australia and New Zealand."),

    (3, "hard",
     "NGT కేసు disposal కి statutory time limit ఎంత? / Statutory time limit for NGT case disposal?",
     "3 నెలలు",
     "6 నెలలు",
     "1 సంవత్సరం",
     "No time limit",
     "b",
     "NGT Act 2010 Section 18: NGT కేసులు original application దాఖలు అయిన తేదీ నుండి 6 నెలల్లో dispose చేయాలి (statutory obligation). / NGT Act 2010: cases must be disposed of within 6 months of filing (statutory time limit)."),

    (3, "toughest",
     "NGT Art.21 తో ఏ విధంగా connect అవుతుంది? / How is NGT connected to Art.21?",
     "NGT Art.21 కింద created",
     "Clean environment = Right to life (Art.21); NGT enforces this right",
     "NGT Art.21 violations decide చేస్తుంది",
     "NGT రాష్ట్రపతి Art.21 ద్వారా appoint",
     "b",
     "Supreme Court (Subhash Kumar vs. State of Bihar, 1991): Clean environment రక్షణ = Right to Life (Art.21) లో భాగం. NGT ఈ right enforce చేస్తుంది. / Clean environment is part of Right to Life (Art.21 — Subhash Kumar case 1991); NGT enforces this right."),

    # ── Section 4: NCLT ───────────────────────────────────────────────────────
    (4, "easy",
     "NCLT అంటే ఏమిటి? / What does NCLT stand for?",
     "National Civil Law Tribunal",
     "National Company Law Tribunal",
     "National Consumer Law Tribunal",
     "National Corporate Law Tribunal",
     "b",
     "NCLT = National Company Law Tribunal. Company law సంబంధిత వివాదాల పరిష్కారానికి. / NCLT: National Company Law Tribunal — handles company law disputes."),

    (4, "easy",
     "NCLT ఏ చట్టం కింద స్థాపించబడింది? / NCLT was established under?",
     "Companies Act, 1956",
     "Companies Act, 2013",
     "SEBI Act, 1992",
     "Industrial Disputes Act, 1947",
     "b",
     "NCLT Companies Act, 2013 కింద 2016లో స్థాపించబడింది. / NCLT: established under Companies Act, 2013 (operational from June 2016)."),

    (4, "medium",
     "NCLT ముందు Company law disputes ఏ Tribunal handle చేసేది? / Before NCLT, which tribunal handled company disputes?",
     "CAT",
     "CLB (Company Law Board)",
     "ITAT",
     "TDSAT",
     "b",
     "NCLT ముందు CLB (Company Law Board) మరియు High Court Company Bench company disputes handle చేసేవి. NCLT వీటిని replace చేసింది. / Before NCLT: Company Law Board (CLB) and HC Company Bench. NCLT replaced both."),

    (4, "medium",
     "NCLAT అంటే ఏమిటి? / What is NCLAT?",
     "NCLT కి Appellate Tribunal",
     "NCLT కి Sub-Tribunal",
     "Consumer Appellate Tribunal",
     "National Civil Law Appellate Tribunal",
     "a",
     "NCLAT = National Company Law Appellate Tribunal. NCLT orders పై appeals ఇక్కడ వేయవచ్చు. Headquarters: New Delhi. / NCLAT: National Company Law Appellate Tribunal — appellate body for NCLT orders."),

    (4, "medium",
     "IBC (Insolvency & Bankruptcy Code) కేసులు ఏ Tribunal handle చేస్తుంది? / IBC cases are handled by?",
     "CAT",
     "NGT",
     "NCLT",
     "ITAT",
     "c",
     "Insolvency and Bankruptcy Code 2016 కేసులు NCLT handle చేస్తుంది. NCLT Adjudicating Authority for corporate insolvency. / IBC 2016 corporate insolvency cases: NCLT is the Adjudicating Authority."),

    (4, "medium",
     "NCLT Chairperson అర్హత ఏమిటి? / Qualification for NCLT President?",
     "CA or CMA",
     "Retired HC or SC Judge",
     "IAS officer (Secretary level)",
     "Retired CEO",
     "b",
     "NCLT President = Retired HC Judge లేదా SC Judge. Members = Judicial Members + Technical Members. / NCLT President: retired HC or SC judge. Members: judicial + technical."),

    (4, "hard",
     "NCLT merger/acquisition కేసులు ఏ విధంగా handle చేస్తుంది? / NCLT's role in mergers/acquisitions?",
     "NCLT పరిధిలో లేదు",
     "Companies Act 2013 Section 230-232 కింద Scheme of Arrangement/Merger NCLT ఆమోదిస్తుంది",
     "SEBI మాత్రమే approve చేస్తుంది",
     "RBI permission అవసరం",
     "b",
     "Companies Act 2013 Sections 230-232: Company mergers, demergers, amalgamations, arrangements = NCLT ఆమోదించాలి. High Court role ఇప్పుడు NCLT తీసుకుంది. / NCLT approves mergers, demergers, amalgamations under Companies Act 2013 (Sec 230-232)."),

    (4, "toughest",
     "NCLT Benches India లో ఎన్ని ఉన్నాయి? / How many NCLT Benches are there in India?",
     "5 Benches",
     "10 Benches",
     "15 Benches",
     "16 Benches",
     "d",
     "NCLT కి 16 Benches ఉన్నాయి (Principal Bench New Delhi + 15 other Benches across India). / NCLT: 16 benches in India (including Principal Bench at New Delhi)."),

    # ── Section 5: ITAT & Other Tribunals ────────────────────────────────────
    (5, "easy",
     "India లో అత్యంత పాత Tribunal ఏది? / Oldest tribunal in India?",
     "CAT",
     "NGT",
     "ITAT",
     "TDSAT",
     "c",
     "ITAT (Income Tax Appellate Tribunal) 1941లో స్థాపించబడింది — India's oldest Tribunal. Income Tax appeals handle చేస్తుంది. / ITAT (Income Tax Appellate Tribunal): established 1941 — oldest tribunal in India."),

    (5, "easy",
     "CESTAT దేని కోసం? / CESTAT is for?",
     "Environmental disputes",
     "Customs and Excise disputes",
     "Service tax only",
     "Company law",
     "b",
     "CESTAT = Customs, Excise and Service Tax Appellate Tribunal (ఇప్పుడు GST తర్వాత: Customs, Excise and GSTAT). Indirect tax disputes. / CESTAT: Customs, Excise and Service Tax Appellate Tribunal — indirect tax disputes."),

    (5, "medium",
     "AFT (Armed Forces Tribunal) ఏ సంవత్సరంలో స్థాపించబడింది? / AFT was established in?",
     "2005",
     "2007",
     "2009",
     "2011",
     "c",
     "AFT (Armed Forces Tribunal) Armed Forces Tribunal Act 2007 కింద 2009లో operational అయింది. Military service matters handle చేస్తుంది. / AFT: operational since 2009 under Armed Forces Tribunal Act, 2007."),

    (5, "medium",
     "TDSAT దేని కోసం? / TDSAT is for?",
     "Tax disputes",
     "Telecom and broadcasting disputes",
     "Consumer disputes",
     "Company disputes",
     "b",
     "TDSAT = Telecom Disputes Settlement and Appellate Tribunal (2000). TRAI orders పై appeals + telecom sector disputes. / TDSAT: Telecom Disputes Settlement and Appellate Tribunal — telecom and broadcasting disputes (since 2000)."),

    (5, "medium",
     "ITAT Benches అన్ని India లో ఎంత మంది Members ఉంటారు? ITAT Chairperson అర్హత? / ITAT Chairperson qualification?",
     "District Judge",
     "Retired HC Judge",
     "Senior advocate పదవి",
     "IRS Officer (Commissioner level)",
     "b",
     "ITAT President = Retired HC Judge లేదా HC Chief Justice. Accountant Members + Judicial Members ఉంటారు. / ITAT President: retired HC Judge or Chief Justice. Members: judicial + accountant (CA/IRS background)."),

    (5, "medium",
     "DRT (Debt Recovery Tribunal) ఏ చట్టం కింద ఏర్పాటు? / DRT was set up under?",
     "Companies Act",
     "Recovery of Debts and Bankruptcy Act (RDBA) 1993",
     "SARFAESI Act 2002",
     "Banking Regulation Act",
     "b",
     "DRT (Debt Recovery Tribunal) Recovery of Debts Due to Banks and Financial Institutions Act 1993 కింద ఏర్పాటైంది. Bank loans recovery వేగంగా చేయడానికి. / DRT: set up under Recovery of Debts Due to Banks and Financial Institutions Act, 1993."),

    (5, "hard",
     "NCDRC (National Consumer Disputes Redressal Commission) ఏ రంగంలో? / NCDRC deals with?",
     "Company disputes",
     "Consumer disputes — Consumer Protection Act",
     "Labour disputes",
     "Election disputes",
     "b",
     "NCDRC = National Consumer Disputes Redressal Commission (Consumer Protection Act 1986 / 2019). Above District Forum → State Commission → National Commission (NCDRC). / NCDRC: Consumer Protection Act — national apex consumer redressal body."),

    (5, "toughest",
     "Securities Appellate Tribunal (SAT) ఏ విషయాలు handle చేస్తుంది? / What does SAT handle?",
     "Tax disputes",
     "SEBI orders పై appeals",
     "Company insolvency",
     "Telecom disputes",
     "b",
     "SAT = Securities Appellate Tribunal — SEBI (Securities Exchange Board of India) orders పై appeals. SEBI Act 1992 కింద. / SAT: Securities Appellate Tribunal — appeals against SEBI orders under SEBI Act, 1992."),

    # ── Section 6: Tribunal features & comparison ─────────────────────────────
    (6, "easy",
     "Tribunal అనే పదం ఎక్కడ నుండి వచ్చింది? / 'Tribunal' word origin?",
     "Latin 'tribunus' — magistrate's seat",
     "French 'tribunal'",
     "Greek 'tribulos'",
     "Sanskrit 'tribhuja'",
     "a",
     "Tribunal = Latin 'tribunus' (Roman magistrate) నుండి. న్యాయ వ్యవస్థలో quasi-judicial body. / 'Tribunal' derives from Latin 'tribunus' (a Roman magistrate's seat of office)."),

    (6, "easy",
     "Tribunals Quasi-judicial bodies అంటే ఏమిటి? / What are quasi-judicial bodies?",
     "Courts కి రద్దు",
     "Administrative bodies that exercise judicial functions",
     "Legislative bodies",
     "Constitutional bodies only",
     "b",
     "Quasi-judicial bodies = Administrative bodies that have judicial powers — evidence record చేయగలవు, parties విన్నవించుకోవచ్చు, binding orders ఇవ్వగలవు. / Quasi-judicial: administrative bodies exercising judicial functions — hearing parties, taking evidence, giving binding orders."),

    (6, "medium",
     "Tribunals Courts కంటే ఎందుకు ప్రయోజనకరం? / Why are tribunals better than courts?",
     "అవి రాజ్యాంగ bodies కావు",
     "వేగం, expertise, సరళత — specialized justice తక్కువ cost లో",
     "Courts వలె formal",
     "Appeal లేదు కాబట్టి",
     "b",
     "Tribunals ప్రయోజనాలు: (1) Speed — faster than courts; (2) Expertise — technical + judicial members; (3) Simplified procedures; (4) Cost-effective; (5) Decongests regular courts. / Tribunals: faster, expert (technical members), simplified procedures, cost-effective, relieves court burden."),

    (6, "medium",
     "Tribunals కి CPC (Civil Procedure Code) మరియు Evidence Act వర్తిస్తాయా? / Does CPC and Evidence Act apply to Tribunals?",
     "అన్ని Tribunals కి వర్తిస్తాయి",
     "వర్తించవు — Natural Justice principles follow చేస్తాయి",
     "CPC మాత్రమే వర్తిస్తుంది",
     "SC నిర్ణయంపై ఆధారపడి",
     "b",
     "Tribunals CPC & Evidence Act by NOT bound — Natural Justice principles (audi alteram partem, nemo judex in causa sua) + their own procedures follow చేస్తాయి. / Tribunals are not bound by CPC or Evidence Act; they follow principles of natural justice and their own procedures."),

    (6, "medium",
     "Tribunals లో Technical Members ఎందుకు అవసరం? / Why are Technical Members needed in Tribunals?",
     "Legal matters కోసం",
     "Subject-specific expertise — Engineering, Accounts, Environment etc.",
     "Political appointees",
     "Cost తగ్గించడానికి",
     "b",
     "Technical Members subject-specific expertise తెస్తారు: NGT = Environment scientists; ITAT = Chartered Accountants; NCLT = Financial experts; AFT = Military experts. Regular judges కి ఉండని specialized knowledge. / Technical Members provide domain expertise: NGT = scientists; ITAT = CAs; NCLT = financial experts."),

    (6, "hard",
     "Tribunal Independence ఎందుకు ముఖ్యం? / Why is Tribunal independence important?",
     "Government influence నివారించడానికి",
     "Fair, impartial decisions కోసం — Executive pressure లేకుండా",
     "Courts bypass చేయడానికి",
     "Revenue పెంచడానికి",
     "b",
     "Tribunal Independence: Executive/Government pressure లేకుండా fair decisions. Rojer Mathew vs. South Indian Bank (2019): SC prescribed guidelines for Tribunal independence — financial independence, security of tenure, qualified members. / Tribunal independence essential for impartial decisions; SC in Rojer Mathew (2019) laid guidelines for independence."),

    (6, "toughest",
     "Madras Bar Association cases లో Tribunals గురించి SC ఏమి చెప్పింది? / What did SC say about Tribunals in Madras Bar Association cases?",
     "Tribunals unconstitutional",
     "Tribunals cannot replace HCs; must have qualified judicial members; cannot undermine judicial independence",
     "Tribunals should replace all courts",
     "HC jurisdiction completely excluded",
     "b",
     "Madras Bar Association vs. Union of India (multiple cases): SC repeated: (1) Tribunals cannot replace HCs/SC; (2) Judicial members must be from HC/SC judge background; (3) Tribunals must be independent — not under Executive ministries. / Madras Bar Association cases: Tribunals can't replace HCs; need qualified judicial members; must be independent of Executive."),

    (6, "medium",
     "Tribunals Reforms Act 2021 ఏమి చేసింది? / What did Tribunals Reforms Act 2021 do?",
     "Abolished all tribunals",
     "Abolished 9 tribunals and merged them with regular courts/HC",
     "Created 5 new tribunals",
     "Made all tribunals constitutional",
     "b",
     "Tribunals Reforms Act 2021: 9 tribunals రద్దు చేసి వాటి పని HC లు, regular courts తీసుకున్నాయి. ఉదా: IPAB (Intellectual Property Appellate Board), Film Certification Appellate Tribunal (FCAT) రద్దు. / Tribunals Reforms Act 2021: abolished 9 tribunals, merged their functions into HCs and regular courts (e.g., IPAB, FCAT abolished)."),

    # ── Section 7: Tribunals vs Courts & Constitutional Basis ────────────────
    (7, "easy",
     "Tribunals ఏ రకమైన justice provide చేస్తాయి? / What type of justice do Tribunals provide?",
     "Criminal justice",
     "Quasi-judicial/administrative justice",
     "Constitutional justice",
     "International justice",
     "b",
     "Tribunals quasi-judicial/administrative justice provide చేస్తాయి — specialized disputes లో faster, expert resolution. / Tribunals provide quasi-judicial/administrative justice — specialized and faster than regular courts."),

    (7, "easy",
     "Tribunals మరియు ordinary Courts మధ్య ముఖ్య తేడా ఏమిటి? / Key difference between Tribunals and ordinary Courts?",
     "Tribunals criminal cases decide చేస్తాయి",
     "Tribunals subject-specific; Courts general; Tribunals have technical members",
     "Courts faster; Tribunals slower",
     "తేడా లేదు",
     "b",
     "Courts = General jurisdiction (all types of cases); Tribunals = Subject-specific jurisdiction; Technical members; Simplified procedures; Faster disposal. / Courts: general jurisdiction; Tribunals: specialized jurisdiction with technical members and simplified procedures."),

    (7, "medium",
     "Art.136 కింద SC Tribunals decisions review చేయగలదా? / Can SC review tribunal decisions under Art.136?",
     "కేవలం constitutional questions పై",
     "అవును — Art.136 SLP (Special Leave Petition) ద్వారా",
     "కాదు — Tribunals final",
     "కేవలం President రిఫరెన్స్ పై",
     "b",
     "Art.136: SC ఏ court/tribunal నిర్ణయాన్నైనా SLP (Special Leave Petition) ద్వారా review చేయవచ్చు. / Art.136: SC can review any tribunal decision through SLP (Special Leave Petition)."),

    (7, "medium",
     "రాజ్యాంగంలో Tribunals కి ముందు ఏ Article హోదా ఇచ్చింది? / Which Articles in Constitution provide for Tribunals?",
     "Art.312, 315",
     "Art.323A, 323B",
     "Art.280, 282",
     "Art.217, 219",
     "b",
     "Art.323A (42వ Amendment 1976): Administrative Tribunals; Art.323B (42వ Amendment 1976): Other Tribunals. రెండూ Part XIV-A లో ఉన్నాయి. / Art.323A and 323B (inserted by 42nd Amendment 1976) — in Part XIV-A of Constitution."),

    (7, "hard",
     "Tribunals rule of law ని ఎలా strengthen చేస్తాయి? / How do Tribunals strengthen rule of law?",
     "Courts రద్దు చేయడం ద్వారా",
     "Specialized justice + pendency తగ్గించడం + expert decisions",
     "Government కి అనుకూలంగా",
     "Delays increase చేయడం ద్వారా",
     "b",
     "Tribunals rule of law strengthen చేస్తాయి: (1) Specialized decisions — expert members; (2) Court pendency తగ్గించడం; (3) Faster justice; (4) Subject-specific law interpretation. / Tribunals strengthen rule of law: specialized justice, reduce court pendency, faster decisions."),

    (7, "hard",
     "National Tribunal Commission (NTC) ప్రపోజల్ ఏ purpose కోసం? / What is the purpose of proposed National Tribunal Commission (NTC)?",
     "All tribunals abolish చేయడానికి",
     "Tribunals independence + oversight — appointments, service conditions, infrastructure",
     "UPSC కి merger",
     "All tribunal cases SC కి transfer",
     "b",
     "NTC (Proposed): SC (Rojer Mathew case 2019) సిఫారసు — Tribunals independence, appointments oversight, service conditions నిర్వహించడానికి National Tribunal Commission ఏర్పాటు చేయాలి. Executive control తగ్గించడానికి. / NTC (proposed per SC in Rojer Mathew 2019): to oversee tribunal appointments, service conditions, and infrastructure — reducing executive control."),

    (7, "toughest",
     "Rojer Mathew vs. South Indian Bank (2019) లో SC Tribunals గురించి ఏమి చెప్పింది? / SC's key finding in Rojer Mathew (2019) case?",
     "Tribunals constitutional కాదు",
     "Tribunals need independence from Executive; NTC ఏర్పాటు; judicial members qualifications fix చేయాలి",
     "All Tribunals rद्दు",
     "Tribunals HCs కి merge చేయాలి",
     "b",
     "Rojer Mathew vs. South Indian Bank Ltd (2019): SC 5-judge bench — (1) Tribunals must be independent of Executive ministries; (2) National Tribunal Commission (NTC) ఏర్పాటు సిఫారసు; (3) Members qualifications fix; (4) Financed from Consolidated Fund. / Rojer Mathew (2019): Tribunals need executive independence; recommended NTC; standardize qualifications; finance from CFI."),

    (7, "medium",
     "Tribunals Reform (Rationalisation and Conditions of Service) Act 2021 ముఖ్య నిబంధన? / Key provision of Tribunals Reform Act 2021?",
     "CAT రద్దు",
     "9 tribunals రద్దు; 4 సంవత్సరాల fixed term (members); President appoints on Search Committee advice",
     "NGT రద్దు",
     "Finance Commission tribunals control",
     "b",
     "Tribunals Reforms Act 2021: (1) 9 specific tribunals రద్దు; (2) Members: 4-year term (renewable to max 67); (3) Search-cum-Selection Committee President appoints members. / Tribunals Reforms Act 2021: abolished 9 tribunals; members 4-year term; President appoints on Search Committee recommendation."),
]


def _seed_polity_ch30_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json
    ph = '%s' if use_postgres else '?'
    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
        (_TOPIC, _CH))
    rows = cur.fetchall()
    if rows:
        if not force:
            return
        existing_id = (rows[0]['id'] if use_postgres else rows[0][0])
        db_exec_fn(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (existing_id,))
        db_exec_fn(conn, f"DELETE FROM study_notes WHERE id={ph}", (existing_id,))

    db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        (_SUBJECT, _TOPIC, _CH, _TITLE_TE, _TITLE_EN, _PAGES, json.dumps(_SECTIONS, ensure_ascii=False)))


def _seed_polity_ch30_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    import json
    ph = '%s' if use_postgres else '?'
    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
        (_TOPIC, _CH))
    row = cur.fetchone()
    if not row:
        return
    note_id = row['id'] if use_postgres else row[0]

    cur2 = db_exec_fn(conn, f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    cnt = list(cur2.fetchone())[0]
    if cnt >= 64:
        return

    for mcq in _MCQS:
        sec_idx, diff, q, a, b, c, d, correct, expl = mcq
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff, 'General', q, a, b, c, d, correct, expl))

import json
