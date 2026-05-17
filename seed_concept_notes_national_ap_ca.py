#!/usr/bin/env python3
"""
seed_concept_notes_national_ap_ca.py
Bilingual (Telugu + English) concept notes for:
  - National Current Affairs 2026  (IDs 31001–31080)  → tags: national_ca_budget, national_ca_polity, national_ca_misc
  - AP/Telangana Current Affairs 2026 (IDs 32001–32080) → tags: ap_ca_budget, ap_ca_state, ts_ca_state
"""
import os, sys

DATABASE_URL = os.environ.get('DATABASE_URL', '')
USE_POSTGRES  = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    conn = psycopg2.connect(DATABASE_URL)
else:
    import sqlite3
    DB   = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(DB)

NOTES = []   # (tag, label, label_te, html)

# ═══════════════════════════════════════════════════════════════
#  1.  NATIONAL CA — UNION BUDGET & ECONOMY 2026-27
#      IDs 31001–31020   tag: national_ca_budget
# ═══════════════════════════════════════════════════════════════
NOTES.append(('national_ca_budget',
               'National CA 2026 — Union Budget & Economy',
               'జాతీయ కరెంట్ అఫైర్స్ 2026 — కేంద్ర బడ్జెట్ & ఆర్థికం',
"""
<div class="concept-cover">
  <h1>కేంద్ర బడ్జెట్ 2026-27 &amp; జాతీయ ఆర్థికం<span class="bi-te"></span></h1>
  <div class="sub">Union Budget 2026-27 | India Economy | Finance Commission</div>
</div>

<div class="section-hdr">కేంద్ర బడ్జెట్ 2026-27 / Union Budget 2026-27</div>
<table class="key-table">
<tr><th>అంశం / Item</th><th>వివరాలు / Details</th></tr>
<tr><td>బడ్జెట్ ప్రవేశపెట్టిన తేదీ</td><td>February 1, 2026 — FM నిర్మలా సీతారామన్ (8వ వరుస బడ్జెట్)</td></tr>
<tr><td>మొత్తం వ్యయం</td><td>₹50,65,345 కోట్లు (Total expenditure Rs 50.65 lakh crore)</td></tr>
<tr><td>మూలధన వ్యయం</td><td>₹11,11,111 కోట్లు (Capital expenditure — record high)</td></tr>
<tr><td>రక్షణ కేటాయింపు</td><td>₹6,81,210 కోట్లు (Defence)</td></tr>
<tr><td>రైల్వేలు</td><td>₹2,52,200 కోట్లు (Railways)</td></tr>
<tr><td>వ్యవసాయం</td><td>₹1,71,437 కోట్లు (Agriculture)</td></tr>
<tr><td>విద్య</td><td>₹1,28,650 కోట్లు (Education)</td></tr>
<tr><td>ఆరోగ్యం</td><td>₹98,311 కోట్లు (Health)</td></tr>
<tr><td>గ్రామీణాభివృద్ధి</td><td>₹2,66,808 కోట్లు (Rural Development)</td></tr>
<tr><td>ఆర్థిక లోటు</td><td>GDP లో 4.4% (Fiscal deficit 4.4% of GDP)</td></tr>
<tr><td>పన్ను మినహాయింపు</td><td>₹12 లక్షల వరకు సున్నా పన్ను (Zero tax up to Rs 12 lakh)</td></tr>
<tr><td>GST ఆదాయం</td><td>₹2,03,890 కోట్లు (monthly record)</td></tr>
</table>

<div class="section-hdr">భారత ఆర్థిక సూచికలు / India Economic Indicators 2025-26</div>
<table class="key-table">
<tr><th>సూచిక / Indicator</th><th>విలువ / Value</th></tr>
<tr><td>GDP వృద్ధి రేటు</td><td>6.4% (2024-25) — IMF అంచనా</td></tr>
<tr><td>పద్దెనిమిదవ ఆర్థిక సంఘం</td><td>16th Finance Commission — అధ్యక్షుడు: డా. అరవింద్ పనగరియా; కాలం: 2026-2031</td></tr>
<tr><td>RBI రెపో రేటు</td><td>6.5% (as of 2026)</td></tr>
<tr><td>భారత HDI</td><td>130వ స్థానం (Human Development Index 2024)</td></tr>
<tr><td>GHI</td><td>102వ స్థానం (Global Hunger Index)</td></tr>
<tr><td>CPI</td><td>91వ స్థానం (Corruption Perception Index)</td></tr>
<tr><td>లింగ అంతరం సూచీ</td><td>131వ స్థానం (Gender Gap Index)</td></tr>
<tr><td>ప్రపంచ ఆనంద సూచీ</td><td>118వ స్థానం (Happiness Index)</td></tr>
<tr><td>లింగ అసమానత సూచీ</td><td>38వ స్థానం (GII — Gender Inequality Index)</td></tr>
<tr><td>TFR (భారత్)</td><td>2.1 (replacement level కి సమానం)</td></tr>
<tr><td>TFR (AP)</td><td>1.5 (తెలంగాణ: 1.6)</td></tr>
</table>

<div class="section-hdr">16వ ఆర్థిక సంఘం / 16th Finance Commission</div>
<p><strong>అధ్యక్షుడు:</strong> డా. అరవింద్ పనగరియా (Dr. Arvind Panagariya) — నీతి అయోగ్ మాజీ ఉపాధ్యక్షుడు.</p>
<p><strong>కాలం:</strong> 2026-2031 (5 సంవత్సరాలు) — కేంద్ర-రాష్ట్రాల మధ్య పన్ను పంపిణీ నిర్ణయిస్తుంది.</p>
<p class="bi-te">The 16th Finance Commission determines tax devolution between Centre and States for 2026-2031. Its recommendations will shape how much revenue each state receives.</p>
"""))

# ═══════════════════════════════════════════════════════════════
#  2.  NATIONAL CA — POLITY, DEFENCE & SPACE 2026
#      IDs 31021–31045   tag: national_ca_polity
# ═══════════════════════════════════════════════════════════════
NOTES.append(('national_ca_polity',
               'National CA 2026 — Polity, Defence & Space',
               'జాతీయ కరెంట్ అఫైర్స్ 2026 — రాజకీయం, రక్షణ & అంతరిక్షం',
"""
<div class="concept-cover">
  <h1>జాతీయ రాజకీయం, రక్షణ &amp; అంతరిక్షం 2026<span class="bi-te"></span></h1>
  <div class="sub">Republic Day | Defence | Space | Key Appointments</div>
</div>

<div class="section-hdr">77వ గణతంత్ర దినోత్సవం / 77th Republic Day — January 26, 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>ముఖ్య అతిథి</td><td>ప్రాబోవో సుబియంటో — ఇండోనేషియా అధ్యక్షుడు (Prabowo Subianto, President of Indonesia)</td></tr>
<tr><td>ఇండోనేషియా ప్రాముఖ్యత</td><td>అతిపెద్ద ముస్లిం జనాభా గల దేశం; ASEAN లీడర్</td></tr>
<tr><td>పరేడ్ స్థలం</td><td>కర్తవ్య పథ్ (Kartavya Path), న్యూఢిల్లీ</td></tr>
<tr><td>వేడుక</td><td>జనవరి 26, 2026 (1950 రాజ్యాంగ అమలు 76వ వార్షికోత్సవం)</td></tr>
</table>

<div class="section-hdr">రక్షణ రంగం / Defence — 2025-26</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>ప్రిత్వి-3 క్షిపణి</td><td>పరిధి: 316 కి.మీ.; డిసెంబర్ 2025 విజయవంతంగా పరీక్షించారు (Prithvi-3 missile)</td></tr>
<tr><td>INS S-4 సబ్‌మెరైన్</td><td>న్యూక్లియర్-శక్తి నడిచే సబ్‌మెరైన్ కమిషన్ (India Navy nuclear submarine)</td></tr>
<tr><td>ఆపరేషన్ సింధూర్</td><td>పాక్ ఉగ్రవాద స్థావరాలపై భారత్ దాడి (Operation Sindoor — Pakistan terror camps)</td></tr>
<tr><td>రక్షణ బడ్జెట్</td><td>₹6,81,210 కోట్లు (FY 2026-27)</td></tr>
<tr><td>MILAN 2026</td><td>విశాఖపట్నం వద్ద నావల్ ఎక్సర్సైజ్ — 50+ దేశాలు పాల్గొన్నాయి</td></tr>
</table>

<div class="section-hdr">అంతరిక్ష రంగం / Space — ISRO 2025-26</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>NavIC-16 ఉపగ్రహం</td><td>PSLV ద్వారా జనవరి 2026లో ప్రయోగం; భారత GPS వ్యవస్థ</td></tr>
<tr><td>NISAR ఉపగ్రహం</td><td>ISRO-NASA సంయుక్త; భూమి పర్యవేక్షణ L+S బ్యాండ్ SAR రాడార్</td></tr>
<tr><td>గగన్‌యాన్ వ్యోమగాములు</td><td>గ్రూప్ క్యాప్టన్: శుభాంశు శుక్లా, ప్రసంత్ బాలకృష్ణన్ నాయర్, అజిత్ కృష్ణన్, అంగద్ ప్రతాప్</td></tr>
<tr><td>NASA Artemis-2</td><td>చంద్రుని చుట్టూ మొదటి క్రూడ్ మిషన్ (50 సంవత్సరాల తర్వాత); 4 వ్యోమగాములు; SLS రాకెట్</td></tr>
<tr><td>భారత AI మిషన్</td><td>₹10,371 కోట్లు; 5 సంవత్సరాలు; AI గవర్నెన్స్ ఫ్రేమ్‌వర్క్</td></tr>
</table>

<div class="section-hdr">ముఖ్య నియామకాలు / Key Appointments 2026</div>
<table class="key-table">
<tr><th>పదవి</th><th>వ్యక్తి</th></tr>
<tr><td>సుప్రీంకోర్టు ప్రధాన న్యాయమూర్తి (CJI)</td><td>న్యాయమూర్తి బి.ఆర్. గవాయ్ (Justice B.R. Gavai)</td></tr>
<tr><td>NIA డైరెక్టర్ జనరల్</td><td>దినేష్ కుమార్ (Dinesh Kumar)</td></tr>
<tr><td>జల్ జీవన్ మిషన్</td><td>గ్రామీణ కుటుంబాలకు నల్లా నీరు సరఫరా — 2026 పూర్తి లక్ష్యం</td></tr>
</table>

<div class="section-hdr">ముఖ్య పథకాలు / Schemes 2026</div>
<table class="key-table">
<tr><th>పథకం</th><th>వివరాలు</th></tr>
<tr><td>జల్ జీవన్ మిషన్</td><td>గ్రామీణ ఇళ్లకు నల్లా నీరు — 2026 పూర్తి లక్ష్యం</td></tr>
<tr><td>POCSO డేటా</td><td>బాలల లైంగిక వేధింపులకు వ్యతిరేక చట్టం — నివేదికలు 2025</td></tr>
<tr><td>PM ఆవాస్ యోజన</td><td>అందరికీ ఇళ్లు — Urban + Rural</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════
#  3.  NATIONAL CA — INTERNATIONAL EVENTS & MISCELLANEOUS 2026
#      IDs 31046–31080   tag: national_ca_misc
# ═══════════════════════════════════════════════════════════════
NOTES.append(('national_ca_misc',
               'National CA 2026 — International Events & Miscellaneous',
               'జాతీయ కరెంట్ అఫైర్స్ 2026 — అంతర్జాతీయ సంఘటనలు & ఇతరాలు',
"""
<div class="concept-cover">
  <h1>జాతీయ కరెంట్ అఫైర్స్ — అంతర్జాతీయ &amp; ఇతర సంఘటనలు 2026</h1>
  <div class="sub">WEF Davos | India-Brazil | U19 Cricket | SCO | Trade</div>
</div>

<div class="section-hdr">WEF దావోస్ 56వ వార్షిక సమావేశం / WEF Davos 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>తేదీ</td><td>జనవరి 2026 (56వ Annual Meeting)</td></tr>
<tr><td>స్థలం</td><td>దావోస్, స్విట్జర్లాండ్</td></tr>
<tr><td>తెలంగాణ పెట్టుబడి</td><td>₹28,693 కోట్లు పెట్టుబడి; 9 MoUs సంతకం</td></tr>
<tr><td>థీమ్</td><td>Collaboration for the Intelligent Age</td></tr>
</table>

<div class="section-hdr">భారత్-బ్రెజిల్ సంబంధాలు / India-Brazil Relations</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>బ్రెజిల్ అధ్యక్షుడు</td><td>లూయిజ్ ఇనాసియో లూలా దా సిల్వా (Luiz Inácio Lula da Silva)</td></tr>
<tr><td>సందర్శన</td><td>మార్చి 18, 2026 — భారత్ పర్యటన</td></tr>
<tr><td>ప్రాముఖ్యత</td><td>BRICS అధ్యక్ష దేశం బ్రెజిల్ 2025; IBSA భాగస్వామి</td></tr>
</table>

<div class="section-hdr">U19 క్రికెట్ వరల్డ్ కప్ 2026 / U19 Cricket World Cup 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>విజేత</td><td>🏆 భారత్ (India won)</td></tr>
<tr><td>సంవత్సరం</td><td>2026</td></tr>
<tr><td>ప్రాముఖ్యత</td><td>యువ క్రికెటర్లకు అత్యున్నత వేదిక</td></tr>
</table>

<div class="section-hdr">WAVES 2025 — మీడియా ఎంటర్టైన్‌మెంట్ సమ్మిట్</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>పూర్తి పేరు</td><td>World Audio Visual and Entertainment Summit</td></tr>
<tr><td>థీమ్</td><td>"Connecting Creators, Connecting Countries"</td></tr>
<tr><td>స్థలం</td><td>ముంబై (Mumbai)</td></tr>
<tr><td>సంవత్సరం</td><td>2025</td></tr>
</table>

<div class="section-hdr">భారత్-USA వాణిజ్య సంబంధాలు / India-USA Trade 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>ట్రంప్ టారిఫ్‌లు</td><td>USA అధ్యక్షుడు ట్రంప్ రెసిప్రోకల్ టారిఫ్‌లు విధించారు — భారత్ పై 26% ప్రకటించారు</td></tr>
<tr><td>భారత్ స్పందన</td><td>ద్వైపాక్షిక వాణిజ్య ఒప్పందం చర్చలు — 90 రోజుల విరామం</td></tr>
<tr><td>India-UK FTA</td><td>భారత్-యుకె స్వేచ్ఛా వాణిజ్య ఒప్పందం 2025 సంతకం</td></tr>
</table>

<div class="section-hdr">SCO & గాజా యుద్ధవిరమణ / SCO & Gaza Ceasefire</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>SCO థీమ్ 2025</td><td>SCO Summit — "Stronger SCO for a Better World"</td></tr>
<tr><td>గాజా యుద్ధవిరమణ</td><td>మధ్యవర్తులు: కతార్, ఈజిప్ట్, USA — 2025 మొదలు</td></tr>
<tr><td>LAC (China-India)</td><td>2024 అక్టోబర్‌లో Depsang-Demchok నుండి సైన్య వెనక్కి తీసుకోవడం; LAC నివేదిక 2025</td></tr>
<tr><td>హూతి/ఎర్ర సముద్రం</td><td>యెమన్ హూతులు ఎర్ర సముద్ర వాణిజ్యాన్ని దెబ్బతీశారు; India shipping affected</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════
#  4.  AP CURRENT AFFAIRS — BUDGET & ECONOMY 2026-27
#      IDs 32001–32025   tag: ap_ca_budget
# ═══════════════════════════════════════════════════════════════
NOTES.append(('ap_ca_budget',
               'AP CA 2026 — AP & Telangana Budgets',
               'ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ 2026 — AP & తెలంగాణ బడ్జెట్‌లు',
"""
<div class="concept-cover">
  <h1>ఆంధ్రప్రదేశ్ &amp; తెలంగాణ బడ్జెట్‌లు 2026-27</h1>
  <div class="sub">AP Budget Rs 2,77,830 Cr | Telangana Budget Rs 3,24,234 Cr</div>
</div>

<div class="section-hdr">ఆంధ్రప్రదేశ్ బడ్జెట్ 2026-27 / AP Budget 2026-27</div>
<table class="key-table">
<tr><th>అంశం</th><th>మొత్తం (కోట్లు)</th></tr>
<tr><td>మొత్తం బడ్జెట్</td><td>₹2,77,830 కోట్లు</td></tr>
<tr><td>రెవెన్యూ వసూళ్లు</td><td>₹1,94,140 కోట్లు</td></tr>
<tr><td>రాజధాని వ్యయం</td><td>అమరావతి అభివృద్ధి, మౌలిక సదుపాయాలు</td></tr>
<tr><td>ముఖ్యమంత్రి</td><td>న్యాయమూర్తి చంద్రబాబు నాయుడు (TDP-JSP-BJP కూటమి)</td></tr>
<tr><td>AP అమర్‌సేవ ప్రాజెక్టు</td><td>₹7,910 కోట్లు; 205 అంబులెన్సులు; ఆరోగ్య సేవలు</td></tr>
<tr><td>IFC రుణం</td><td>₹300 కోట్లు (International Finance Corporation)</td></tr>
</table>

<div class="section-hdr">తెలంగాణ బడ్జెట్ 2026-27 / Telangana Budget 2026-27</div>
<table class="key-table">
<tr><th>రంగం / Sector</th><th>కేటాయింపు (కోట్లు)</th></tr>
<tr><td>మొత్తం బడ్జెట్</td><td>₹3,24,234 కోట్లు</td></tr>
<tr><td>వ్యవసాయం</td><td>₹47,267 కోట్లు (అత్యధిక)</td></tr>
<tr><td>పట్టణాభివృద్ధి</td><td>₹47,387 కోట్లు</td></tr>
<tr><td>విద్య</td><td>₹24,166 కోట్లు</td></tr>
<tr><td>ఆరోగ్యం</td><td>₹8,814 కోట్లు</td></tr>
<tr><td>శక్తి (Energy)</td><td>₹38,105 కోట్లు</td></tr>
<tr><td>ముఖ్యమంత్రి</td><td>రేవంత్ రెడ్డి (Congress — 64 సీట్లు, డిసెంబర్ 2023)</td></tr>
</table>

<div class="section-hdr">AP లాజిస్టిక్స్ పాలసీ / AP Logistics Policy 2025-30</div>
<p>ఆంధ్రప్రదేశ్ లాజిస్టిక్స్ పాలసీ 2025-30 — ఎగుమతులు పెంచడం, పోర్టు అభివృద్ధి, మల్టీ-మోడల్ రవాణా.</p>
<p class="bi-te">AP Logistics Policy 2025-30 aims to boost exports, develop ports, and create multimodal transport corridors.</p>

<div class="section-hdr">AP అమరావతి రాజధాని / Amaravati Capital</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>రాజధాని చట్టం</td><td>అమరావతి క్యాపిటల్ రీజియన్ యాక్ట్ — జూలై 2, 2024న AP అసెంబ్లీ ఆమోదించింది</td></tr>
<tr><td>CRDA</td><td>Capital Region Development Authority — అమరావతి అభివృద్ధి అధికారం</td></tr>
<tr><td>హైకోర్టు</td><td>2019 నుండి అమరావతిలో (AP High Court)</td></tr>
<tr><td>జిల్లాలు</td><td>AP లో 25 జిల్లాలు; తెలంగాణలో 33 జిల్లాలు</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════
#  5.  AP CURRENT AFFAIRS — STATE POLITICS & SCHEMES
#      IDs 32026–32055   tag: ap_ca_state
# ═══════════════════════════════════════════════════════════════
NOTES.append(('ap_ca_state',
               'AP CA 2026 — State Politics, Infrastructure & Schemes',
               'AP కరెంట్ అఫైర్స్ 2026 — రాజకీయాలు, మౌలిక సదుపాయాలు & పథకాలు',
"""
<div class="concept-cover">
  <h1>ఆంధ్రప్రదేశ్ — రాజకీయాలు, మౌలిక సదుపాయాలు &amp; పథకాలు 2026</h1>
  <div class="sub">Navaratnalu | Polavaram | Fintech Valley | AP Elections</div>
</div>

<div class="section-hdr">AP రాజకీయ పరిణామాలు / AP Political Developments</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>2024 ఎన్నికలు</td><td>TDP-JSP-BJP కూటమి 164 సీట్లు గెలిచింది (మొత్తం 175)</td></tr>
<tr><td>ముఖ్యమంత్రి</td><td>న్యాయమూర్తి నారా చంద్రబాబు నాయుడు (TDP)</td></tr>
<tr><td>నవరత్నాలు</td><td>TDP-JSP-BJP కూటమి ప్రభుత్వం 9 సంక్షేమ వాగ్దానాలు</td></tr>
<tr><td>AP శాసనసభలో మహిళలు</td><td>28.63% (women in AP assembly)</td></tr>
<tr><td>AP TFR</td><td>1.5 (తెలంగాణ: 1.6)</td></tr>
</table>

<div class="section-hdr">AP సంక్షేమ పథకాలు / AP Welfare Schemes</div>
<table class="key-table">
<tr><th>పథకం</th><th>వివరాలు</th></tr>
<tr><td>అమ్మ వోడి</td><td>విద్యార్థుల తల్లులకు ₹15,000 (Amma Vodi — school attendance)</td></tr>
<tr><td>NTR భరోసా పెన్షన్</td><td>₹3,000 / నెల (వృద్ధులు, వికలాంగులు)</td></tr>
<tr><td>AP అమర్‌సేవ</td><td>₹7,910 కోట్లు; 205 అంబులెన్సులు — ఆరోగ్య సేవలు</td></tr>
<tr><td>ECMS</td><td>41,863 సంబంధాలు (ఎలక్ట్రిక్ కనెక్షన్లు)</td></tr>
</table>

<div class="section-hdr">AP మౌలిక సదుపాయాలు / AP Infrastructure</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>పోలవరం ప్రాజెక్ట్</td><td>గోదావరి నదిపై; 7.2 లక్షల ఎకరాల సాగు; జాతీయ ప్రాజెక్ట్</td></tr>
<tr><td>AP Fintech Valley</td><td>విశాఖపట్నంలో (Visakhapatnam) — ఫిన్‌టెక్ హబ్</td></tr>
<tr><td>SriCity SEZ</td><td>చిత్తూరు జిల్లాలో ప్రత్యేక ఆర్థిక మండలి</td></tr>
<tr><td>RINL</td><td>విశాఖ స్టీల్ ప్లాంట్ (Rashtriya Ispat Nigam Ltd)</td></tr>
<tr><td>అనంతపుర్ సోలార్ పార్క్</td><td>భారతదేశంలో అతిపెద్ద సోలార్ పార్కులలో ఒకటి</td></tr>
<tr><td>స్మార్ట్ సిటీలు</td><td>విశాఖపట్నం + కాకినాడ (AP Smart Cities)</td></tr>
<tr><td>AP మత్స్య</td><td>భారతదేశంలో మత్స్య ఉత్పత్తిలో 1వ స్థానం (Fisheries Rank 1)</td></tr>
<tr><td>AP కేంద్రీయ విశ్వవిద్యాలయం</td><td>కర్నూలులో (Central University of AP)</td></tr>
</table>

<div class="section-hdr">AP విద్యా సంస్థలు / AP Education</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>AICTE</td><td>305 సంస్థలు నిలిపివేత (All India Council for Technical Education)</td></tr>
<tr><td>AP హైకోర్టు</td><td>2019 నుండి అమరావతిలో</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════
#  6.  TELANGANA CURRENT AFFAIRS — 2026
#      IDs 32056–32080   tag: ts_ca_state
# ═══════════════════════════════════════════════════════════════
NOTES.append(('ts_ca_state',
               'Telangana CA 2026 — Economy, Schemes & Events',
               'తెలంగాణ కరెంట్ అఫైర్స్ 2026 — ఆర్థికం, పథకాలు & సంఘటనలు',
"""
<div class="concept-cover">
  <h1>తెలంగాణ కరెంట్ అఫైర్స్ 2026</h1>
  <div class="sub">TS Budget | Davos Investment | Socio-Economic Outlook | Schemes</div>
</div>

<div class="section-hdr">తెలంగాణ సామాజిక-ఆర్థిక నివేదిక 2026 / TS Socio-Economic Outlook 2026</div>
<table class="key-table">
<tr><th>సూచిక</th><th>విలువ</th></tr>
<tr><td>GSDP వృద్ధి రేటు</td><td>6.9% (Telangana GSDP growth)</td></tr>
<tr><td>GSDP మొత్తం</td><td>₹17.82 లక్షల కోట్లు</td></tr>
<tr><td>పేదరికం తగ్గింపు</td><td>41.5% → 9.4% (పేదరిక నిష్పత్తి తగ్గింది)</td></tr>
<tr><td>అక్షరాస్యత</td><td>74.9% (Literacy rate)</td></tr>
<tr><td>ముఖ్యమంత్రి</td><td>రేవంత్ రెడ్డి (Congress, 64 సీట్లు డిసెంబర్ 2023 ఎన్నికలలో)</td></tr>
<tr><td>జిల్లాల సంఖ్య</td><td>33 జిల్లాలు</td></tr>
</table>

<div class="section-hdr">దావోస్ పెట్టుబడి / Davos Investment (WEF 2026)</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>పెట్టుబడి</td><td>₹28,693 కోట్లు పెట్టుబడి ప్రకటనలు</td></tr>
<tr><td>MoUs</td><td>9 MoUs సంతకం (IT, Manufacturing, Pharma)</td></tr>
<tr><td>సందర్భం</td><td>WEF 56వ Annual Meeting, జనవరి 2026, దావోస్</td></tr>
</table>

<div class="section-hdr">తెలంగాణ పథకాలు / Telangana Welfare Schemes</div>
<table class="key-table">
<tr><th>పథకం</th><th>వివరాలు</th></tr>
<tr><td>గృహ లక్ష్మి</td><td>₹2,500 / నెల మహిళలకు (Gruha Lakshmi)</td></tr>
<tr><td>పల్లె ప్రగతి</td><td>గ్రామాభివృద్ధి కార్యక్రమం (Palle Pragathi)</td></tr>
<tr><td>అన్న సముద్రం</td><td>ఉచిత భోజనం (Anna Samudram)</td></tr>
</table>

<div class="section-hdr">తెలంగాణ మౌలిక సదుపాయాలు / TS Infrastructure</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>కళేశ్వరం ప్రాజెక్ట్</td><td>గోదావరి నదిపై; ప్రపంచ అతిపెద్ద లిఫ్ట్ ఇర్రిగేషన్ ప్రాజెక్ట్</td></tr>
<tr><td>హైదరాబాద్ మెట్రో ఫేజ్-2</td><td>నాగోల్ నుండి రాయదుర్గం వరకు పొడిగింపు</td></tr>
<tr><td>జీనోమ్ వ్యాలీ</td><td>మేడ్చల్-మల్కాజిగిరి జిల్లాలో బయోటెక్ హబ్</td></tr>
<tr><td>TS ఫార్మా సిటీ</td><td>19,333 ఎకరాలు — ప్రపంచ అతిపెద్ద ఫార్మా క్లస్టర్</td></tr>
<tr><td>హైదరాబాద్ మెట్రో రైలు</td><td>L&T MRO అమలు; Phase 2 పురోగతి</td></tr>
</table>

<div class="section-hdr">గద్దర్ సినిమా అవార్డులు 2025 / Gaddar Cinema Awards</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>వేడుక</td><td>తెలంగాణ గద్దర్ సినిమా అవార్డులు 2025 — డిసెంబర్ 2025</td></tr>
<tr><td>విభాగాలు</td><td>75 విభాగాలలో అవార్డులు</td></tr>
<tr><td>ఉద్దేశ్యం</td><td>తెలుగు సినిమా రంగాన్ని ప్రోత్సహించడం</td></tr>
</table>

<div class="section-hdr">MILAN 2026 నావల్ ఎక్సర్సైజ్</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>స్థలం</td><td>విశాఖపట్నం (Visakhapatnam)</td></tr>
<tr><td>భాగస్వాములు</td><td>50+ దేశాల నావికాదళాలు</td></tr>
<tr><td>ప్రాముఖ్యత</td><td>భారత నావికాదళ దౌత్యం; హిందూ మహాసముద్ర భాగస్వామ్యం</td></tr>
</table>
"""))

# ════════════════════════════════════════════════════════════════
#  DATABASE INSERT
# ════════════════════════════════════════════════════════════════
if USE_POSTGRES:
    cur = conn.cursor()
    tags = [n[0] for n in NOTES]
    for tag in tags:
        cur.execute("DELETE FROM concept_notes WHERE tag = %s", (tag,))
    for tag, label, label_te, html in NOTES:
        cur.execute(
            "INSERT INTO concept_notes (tag, label, label_te, html) VALUES (%s, %s, %s, %s)",
            (tag, label, label_te, html.strip())
        )
    conn.commit()
    cur.close()
else:
    tags = [n[0] for n in NOTES]
    for tag in tags:
        conn.execute("DELETE FROM concept_notes WHERE tag = ?", (tag,))
    for tag, label, label_te, html in NOTES:
        conn.execute(
            "INSERT INTO concept_notes (tag, label, label_te, html) VALUES (?, ?, ?, ?)",
            (tag, label, label_te, html.strip())
        )
    conn.commit()

conn.close()
print(f"[seed_concept_notes_national_ap_ca] Inserted {len(NOTES)} concept notes.")
