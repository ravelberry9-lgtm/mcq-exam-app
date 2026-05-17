#!/usr/bin/env python3
"""
seed_concept_notes_ap_divs.py
10 bilingual (English + Telugu) topic-cluster concept notes for AP CA div questions.
IDs covered: 32201-33200  |  folder='AP_HC'  |  topic='AP_Current_Affairs_2026'
Topics: Elections, Schemes, Events2025, Events2026, Culture, Economy, History,
        Environment/Sports, Awards/Institutions, APRA Reorganisation
"""
import os, sys

DATABASE_URL = os.environ.get('DATABASE_URL', '')
USE_POSTGRES  = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
else:
    import sqlite3
    DB   = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(DB)

cur  = conn.cursor()
ph   = '%s' if USE_POSTGRES else '?'

cur.execute("""CREATE TABLE IF NOT EXISTS concept_notes
               (tag TEXT PRIMARY KEY, label TEXT NOT NULL,
                label_te TEXT, html TEXT NOT NULL)""")

NOTES = []   # list of (tag, label, label_te, html)

# ═══════════════════════════════════════════════════════════════════
#  1. ELECTIONS & CABINET  (div1)
#     IDs: 32201-32290
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_elections_cabinet', '2024 AP Elections & Cabinet', '2024 AP ఎన్నికలు & కేబినెట్', """
<div class="concept-cover">
  <h1>2024 AP ఎన్నికలు &amp; కేబినెట్ <span class="bi-te">/ 2024 AP Elections &amp; Cabinet</span></h1>
  <div class="sub">TDP-JSP-BJP Alliance Landslide Victory</div>
</div>

<div class="section-hdr">ఎన్నికల వివరాలు / Election Details</div>
<table class="key-table">
<tr><th>అంశం / Item</th><th>వివరాలు / Detail</th></tr>
<tr><td>పోలింగ్ తేదీ</td><td>మే 13, 2024 (May 13, 2024)</td></tr>
<tr><td>ఫలితాల తేదీ</td><td>జూన్ 4, 2024 (June 4, 2024)</td></tr>
<tr><td>మొత్తం స్థానాలు</td><td>175 అసెంబ్లీ సీట్లు (majority mark: 88)</td></tr>
<tr><td>పోలింగ్ శాతం</td><td>81.86%</td></tr>
<tr><td>అత్యధిక పోలింగ్</td><td>దార్సి నియోజకవర్గం — 90.91%</td></tr>
<tr><td>అత్యల్ప పోలింగ్</td><td>తిరుపతి నియోజకవర్గం — 63.32%</td></tr>
<tr><td>లోక్‌సభ స్థానాలు</td><td>AP లో 25 స్థానాలు</td></tr>
</table>

<div class="section-hdr">ఫలితాలు / Election Results</div>
<table class="key-table">
<tr><th>పార్టీ / Party</th><th>అసెంబ్లీ / Assembly</th><th>లోక్‌సభ / Lok Sabha</th></tr>
<tr><td><b>TDP (తెలుగుదేశం పార్టీ)</b></td><td>135</td><td>16</td></tr>
<tr><td>JSP (జనసేన పార్టీ)</td><td>21</td><td>2</td></tr>
<tr><td>BJP (భారతీయ జనతా పార్టీ)</td><td>8</td><td>3</td></tr>
<tr><td><b>కూటమి మొత్తం (Alliance Total)</b></td><td><b>164 / 175</b></td><td><b>21 / 25</b></td></tr>
<tr><td>YSRCP</td><td>11</td><td>4</td></tr>
</table>

<div class="section-hdr">కేబినెట్ / Cabinet Formation</div>
<table class="key-table">
<tr><th>పదవి / Post</th><th>పేరు / Name</th><th>నియోజకవర్గం / Constituency</th></tr>
<tr><td>ముఖ్యమంత్రి (CM) — 4వ సారి</td><td>N. చంద్రబాబు నాయుడు</td><td>కుప్పం</td></tr>
<tr><td>ఉప ముఖ్యమంత్రి (Deputy CM)</td><td>పవన్ కళ్యాణ్ (JSP)</td><td>పిఠాపురం</td></tr>
<tr><td>శపథ గ్రహణ</td><td>జూన్ 12, 2024 (June 12, 2024)</td><td>—</td></tr>
<tr><td>మంత్రుల సంఖ్య</td><td>25 మంత్రులు (TDP:21, JSP:3, BJP:1)</td><td>—</td></tr>
<tr><td>మహిళా మంత్రులు</td><td>3</td><td>—</td></tr>
<tr><td>తొలిసారి మంత్రులు</td><td>17 మంది</td><td>—</td></tr>
<tr><td>ఆర్థిక మంత్రి</td><td>పయ్యావుల కేశవ్</td><td>—</td></tr>
<tr><td>హోం మంత్రి</td><td>వంగలపూడి అనిత</td><td>—</td></tr>
<tr><td>గవర్నర్</td><td>జస్టిస్ S. అబ్దుల్ నజీర్ (Feb 2023 నుండి)</td><td>—</td></tr>
<tr><td>స్పీకర్</td><td>చింతకాయల అయ్యన్నపాత్రుడు</td><td>—</td></tr>
</table>

<div class="section-hdr">కీలక అంశాలు / Key Points</div>
<p>• కూటమి 164 / 175 స్థానాలు గెలిచింది — చారిత్రక మెజారిటీ (Historic majority)</p>
<p>• AP లో మొత్తం 175 అసెంబ్లీ, 25 లోక్‌సభ, 11 రాజ్యసభ స్థానాలు</p>
<p>• చంద్రబాబు నాయుడు 4వ సారి ముఖ్యమంత్రి అయ్యారు (4th term as CM)</p>
<p>• AP 2024 ఎన్నికలు లోక్‌సభ ఎన్నికలతో పాటు జరిగాయి (held simultaneously with Lok Sabha)</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  2. SUPER SIX SCHEMES & WELFARE  (div2)
#     IDs: 32291-32380
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_super_six_schemes', 'AP Super Six Schemes & Welfare', 'AP సూపర్ సిక్స్ పథకాలు & సంక్షేమం', """
<div class="concept-cover">
  <h1>AP సూపర్ సిక్స్ &amp; సంక్షేమ పథకాలు <span class="bi-te">/ AP Super Six &amp; Welfare Schemes</span></h1>
  <div class="sub">TDP-JSP-BJP Alliance Election Guarantees Implemented 2024-2026</div>
</div>

<div class="section-hdr">సూపర్ సిక్స్ పథకాలు / Super Six Schemes</div>
<table class="key-table">
<tr><th>#</th><th>పథకం / Scheme</th><th>వివరాలు / Details</th><th>తేదీ / Date</th></tr>
<tr><td>1</td><td><b>దీపం 2.0 (Deepam 2.0)</b></td><td>ఉచిత 3 LPG సిలిండర్లు/సంవత్సరం మహిళలకు (3 free LPG cylinders/year)</td><td>నవ. 1, 2024 (ఇచ్ఛాపురం, శ్రీకాకుళం)</td></tr>
<tr><td>2</td><td><b>స్త్రీ శక్తి (Stree Shakti)</b></td><td>ఉచిత బస్సు ప్రయాణం మహిళలకు (Free bus travel for women)</td><td>ఆగ. 15, 2024</td></tr>
<tr><td>3</td><td><b>నిరుద్యోగ బృతి</b></td><td>₹3,000/నెల నిరుద్యోగులకు (₹3,000/month to unemployed)</td><td>ఆగ. 15, 2024</td></tr>
<tr><td>4</td><td><b>అన్నదాత సుఖీభవ</b></td><td>₹20,000/సంవత్సరం రైతులకు (State ₹14,000 + Centre PM-KISAN ₹6,000); 46.86 లక్షల రైతులు</td><td>ఆగ. 2, 2025</td></tr>
<tr><td>5</td><td><b>తల్లికి వందనం</b></td><td>₹15,000/సంవత్సరం ప్రభుత్వ పాఠశాల విద్యార్థుల తల్లులకు; 69.16 లక్షల విద్యార్థులు అర్హులు</td><td>జూన్ 12, 2025</td></tr>
<tr><td>6</td><td><b>ఆడబిడ్డ నిధి</b></td><td>₹1,500/నెల (₹18,000/సంవత్సరం) 18-59 సంవత్సరాల మహిళలకు; 80+ లక్షల మంది</td><td>2026 (ప్రణాళిక)</td></tr>
</table>

<div class="section-hdr">ఇతర ముఖ్య పథకాలు / Other Key Schemes</div>
<table class="key-table">
<tr><th>పథకం / Scheme</th><th>వివరాలు / Details</th></tr>
<tr><td>NTR భరోసా పెన్షన్</td><td>₹4,000/నెల; 65+ లక్షల లబ్ధిదారులు; 28 వర్గాలు (renamed from YSR Pension Kanuka)</td></tr>
<tr><td>అన్నా కేంటీన్</td><td>₹5/ప్లేట్ భోజనం; ఆగ. 15, 2024 పునఃప్రారంభం; 100 కేంటీన్లు (Phase 1)</td></tr>
<tr><td>నేతన్న భరోసా</td><td>₹25,000/సంవత్సరం చేనేత కార్మికులకు + 200 యూనిట్లు ఉచిత విద్యుత్</td></tr>
<tr><td>ఆటో డ్రైవర్ల సేవలో</td><td>₹15,000/సంవత్సరం; 2.9 లక్షల ఆటో/క్యాబ్ డ్రైవర్లకు; అక్టో. 4, 2025</td></tr>
<tr><td>మత్స్యకార సేవ</td><td>₹10,000 నిషేధ కాలంలో (ఏప్రిల్-జూన్) మత్స్యకారులకు</td></tr>
<tr><td>మేడారం జాతర సహాయం</td><td>గిరిజన మహిళలకు ప్రత్యేక సహాయం</td></tr>
</table>

<div class="section-hdr">బడ్జెట్ కేటాయింపులు / Budget Allocations 2025-26</div>
<table class="key-table">
<tr><th>పథకం</th><th>కేటాయింపు (Allocation)</th></tr>
<tr><td>తల్లికి వందనం</td><td>₹9,407 కోట్లు</td></tr>
<tr><td>అన్నదాత సుఖీభవ</td><td>₹6,300 కోట్లు</td></tr>
<tr><td>NTR భరోసా పెన్షన్</td><td>₹20,000+ కోట్లు (అంచనా)</td></tr>
<tr><td>AP మొత్తం బడ్జెట్ 2025-26</td><td>₹3,22,359 కోట్లు (Finance Minister: పయ్యావుల కేశవ్; ఫిబ్రవరి 28, 2025)</td></tr>
</table>

<div class="section-hdr">కీలక గుర్తింపు / Key Remember</div>
<p>• సూపర్ సిక్స్ = TDP-JSP-BJP కూటమి 2024 ఎన్నికల హామీలు (Coalition election guarantees)</p>
<p>• అన్నదాత సుఖీభవ = PM-KISAN (₹6,000) + రాష్ట్రం (₹14,000) = ₹20,000 మొత్తం</p>
<p>• దీపం 2.0 — AP Foundation Day నవ. 1, 2024న ప్రారంభం</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  3. MAJOR EVENTS 2025 — JAN TO AUG  (div3_enriched)
#     IDs: 32381-32500
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_events_2025', 'AP Major Events 2025 (Jan–Aug)', 'AP ముఖ్య సంఘటనలు 2025 (జన–ఆగ)', """
<div class="concept-cover">
  <h1>AP ముఖ్య సంఘటనలు 2025 <span class="bi-te">/ AP Major Events 2025</span></h1>
  <div class="sub">PM Modi Visits · Amaravati · RINL · Polavaram · Quantum Valley</div>
</div>

<div class="section-hdr">PM మోదీ జనవరి 2025 పర్యటన — విశాఖపట్నం / PM Modi Jan 8, 2025 Vizag Visit</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>తేదీ</td><td>జనవరి 8, 2025</td></tr>
<tr><td>మొత్తం ప్రాజెక్టుల విలువ</td><td>₹2 లక్ష కోట్లు (₹2 lakh crore)</td></tr>
<tr><td>NTPC గ్రీన్ హైడ్రోజన్ హబ్</td><td>₹1,85,000 కోట్లు; పుడిమడక, విశాఖ జిల్లా (World's largest green hydrogen hub)</td></tr>
<tr><td>రోడ్డు ప్రాజెక్టులు</td><td>10 ప్రాజెక్టులు — ₹4,593 కోట్లు</td></tr>
<tr><td>రైల్వే ప్రాజెక్టులు</td><td>6 ప్రాజెక్టులు — ₹6,028 కోట్లు</td></tr>
</table>

<div class="section-hdr">PM మోదీ మే 2, 2025 అమరావతి పర్యటన / PM Modi May 2, 2025 Amaravati Visit</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>మొత్తం విలువ</td><td>₹58,000 కోట్లు (₹58,000 crore projects)</td></tr>
<tr><td>నిర్మాణాలు</td><td>శాసనసభ భవనం, హైకోర్టు భవనం, సచివాలయం — శంకుస్థాపన</td></tr>
<tr><td>రవాణా నెట్‌వర్క్</td><td>320 km — ₹17,400 కోట్లు</td></tr>
<tr><td>రోడ్లు</td><td>1,281 km — ₹20,400 కోట్లు</td></tr>
<tr><td>DRDO</td><td>క్షిపణి పరీక్ష కేంద్రం శంకుస్థాపన</td></tr>
</table>

<div class="section-hdr">RINL విశాఖ ఉక్కు కర్మాగారం / RINL Vizag Steel Plant</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>కేంద్ర కేటాయింపు</td><td>₹11,440 కోట్లు (Revival package)</td></tr>
<tr><td>Blast Furnaces</td><td>3 Blast Furnaces ఆగ. 2025 నాటికి నడుస్తున్నాయి</td></tr>
<tr><td>ఉద్యోగులు రక్షణ</td><td>20,000+ ఉద్యోగులు పదవులు నిలిపారు</td></tr>
<tr><td>ప్రత్యేక హోదా డిమాండ్</td><td>RINL పునరుద్ధరణలో భాగంగా</td></tr>
</table>

<div class="section-hdr">పోలవరం ప్రాజెక్టు / Polavaram Project</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>యూనియన్ బడ్జెట్ 2025-26 కేటాయింపు</td><td>₹5,936 కోట్లు</td></tr>
<tr><td>మొత్తం పెండింగ్ గ్రాంట్</td><td>₹12,157 కోట్లు</td></tr>
<tr><td>నీటి సామర్థ్యం</td><td>36 TMC (Thousand Million Cubic feet)</td></tr>
<tr><td>సాగు విస్తీర్ణం</td><td>3.27 లక్షల ఎకరాలు</td></tr>
<tr><td>జాతీయ ప్రాజెక్టు హోదా</td><td>అవును — National Project</td></tr>
</table>

<div class="section-hdr">ఇతర ముఖ్య సంఘటనలు 2025 / Other Key Events 2025</div>
<table class="key-table">
<tr><th>తేదీ</th><th>సంఘటన</th></tr>
<tr><td>జన. 29, 2025</td><td>ISRO 100వ ప్రయోగం: NVS-02 నావిగేషన్ శాటిలైట్ — SDSC SHAR, శ్రీహరికోట నుండి</td></tr>
<tr><td>జూన్ 21, 2025</td><td>యోగాంధ్ర — విశాఖ 28 km తీరంలో 5 లక్షల మంది యోగా గిన్నిస్ రికార్డ్</td></tr>
<tr><td>జూలై 12, 2025</td><td>స్వచ్ఛ సర్వేక్షణ్ 2024 — AP నగరాలకు 5 జాతీయ అవార్డులు</td></tr>
<tr><td>ఆగ. 27, 2025</td><td>తిరుమల కొండలు + ఎర్రమట్టి దిబ్బలు UNESCO World Heritage Tentative List లో చేరాయి</td></tr>
<tr><td>సెప్. 4, 2025</td><td>Universal Health Policy (Arogya Sri విస్తరణ) కేబినెట్ ఆమోదం</td></tr>
<tr><td>నవ. 14-15, 2025</td><td>CII 30వ Partnership Summit, విశాఖ — ₹13.26 లక్ష కోట్లు, 613 MoUs, 16.31 లక్షల ఉద్యోగాలు</td></tr>
<tr><td>నవ. 2025</td><td>AP Quantum Computing Policy విడుదల</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════════
#  4. MAJOR EVENTS AUG 2025 – APR 2026  (div4)
#     IDs: 32501-32600
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_events_2026', 'AP Major Events Aug 2025 – Apr 2026', 'AP ముఖ్య సంఘటనలు 2025-26', """
<div class="concept-cover">
  <h1>AP ముఖ్య సంఘటనలు 2025-26 <span class="bi-te">/ AP Major Events Aug 2025–Apr 2026</span></h1>
  <div class="sub">Quantum Valley · IFR 2026 · 28 Districts · APRA Amendment · AP HC</div>
</div>

<div class="section-hdr">అమరావతి క్వాంటం వ్యాలీ / Amaravati Quantum Valley</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>శంకుస్థాపన</td><td>ఫిబ్రవరి 7, 2026 — CM చంద్రబాబు + కేంద్ర మంత్రి జితేంద్ర సింగ్</td></tr>
<tr><td>ప్రారంభం</td><td>ఏప్రిల్ 14, 2026 (World Quantum Day + అంబేద్కర్ జయంతి)</td></tr>
<tr><td>కంప్యూటర్</td><td>IBM Quantum System Two — 156-qubit Heron ప్రాసెసర్</td></tr>
<tr><td>భాగస్వాములు</td><td>IBM + TCS + L&amp;T + CDAC + IITs</td></tr>
<tr><td>ప్రాముఖ్యత</td><td>భారత్‌లో మొదటి, ఆసియాలో అతిపెద్ద Quantum కంప్యూటర్</td></tr>
</table>

<div class="section-hdr">IFR 2026 — అంతర్జాతీయ నౌకాదళ సమావేశం / International Fleet Review 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>తేదీ</td><td>ఫిబ్రవరి 18, 2026</td></tr>
<tr><td>ప్రదేశం</td><td>విశాఖపట్నం</td></tr>
<tr><td>పాల్గొన్న దేశాలు</td><td>74 దేశాలు (74 countries)</td></tr>
<tr><td>నౌకలు</td><td>85 యుద్ధనౌకలు (85 ships)</td></tr>
<tr><td>రాష్ట్రపతి</td><td>ద్రౌపది ముర్ము — INS సుమేధ నౌకపై</td></tr>
<tr><td>థీమ్</td><td>"United Through Oceans"</td></tr>
</table>

<div class="section-hdr">28 జిల్లాలు / AP 28 Districts</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>కేబినెట్ నిర్ణయం</td><td>2025 లో ఆమోదం</td></tr>
<tr><td>అమలు తేదీ</td><td>జనవరి 1, 2026</td></tr>
<tr><td>కొత్త జిల్లాలు</td><td>పోలవరం జిల్లా + మార్కాపురం జిల్లా</td></tr>
<tr><td>పూర్వపు జిల్లాల సంఖ్య</td><td>26 (from 13 old + 13 new 2022)</td></tr>
<tr><td>ప్రస్తుత జిల్లాలు</td><td>28</td></tr>
</table>

<div class="section-hdr">APRA సవరణ చట్టం 2026 / APRA Amendment Act 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>Act నంబర్</td><td>Act No. 7/2026</td></tr>
<tr><td>లోక్‌సభ ఆమోదం</td><td>ఏప్రిల్ 1, 2026</td></tr>
<tr><td>రాజ్యసభ ఆమోదం</td><td>ఏప్రిల్ 2, 2026</td></tr>
<tr><td>రాష్ట్రపతి ఆమోదం</td><td>ఏప్రిల్ 6, 2026</td></tr>
<tr><td>ముఖ్య నిర్ణయం</td><td>అమరావతి — ఏకైక & శాశ్వత రాజధాని (Sole &amp; permanent capital) from June 2, 2024</td></tr>
<tr><td>Section సవరణ</td><td>APRA 2014 Section 5 సవరించబడింది</td></tr>
</table>

<div class="section-hdr">ఇతర ముఖ్య సంఘటనలు / Other Key Events</div>
<table class="key-table">
<tr><th>తేదీ</th><th>సంఘటన</th></tr>
<tr><td>డిసె. 9, 2025</td><td>తుని, కాకినాడ — తిరుమల నీడి సాయి: ప్రపంచపు అతి చిన్న మోటారుతో కదిలే కుమ్మరి సారె గిన్నిస్ రికార్డ్ (91 గ్రాములు)</td></tr>
<tr><td>డిసె. 15, 2025</td><td>పొట్టి శ్రీరాముల్లు 58-అడుగుల విగ్రహం అమరావతిలో ప్రకటన</td></tr>
<tr><td>జన. 1, 2026</td><td>AP 26 → 28 జిల్లాలు అమలు</td></tr>
<tr><td>మార్చి 1, 2026</td><td>G. సాయి ప్రసాద్ AP ముఖ్య కార్యదర్శి (IAS 1991)</td></tr>
<tr><td>మార్చి 10, 2026</td><td>CRDA తెలుగు సాంస్కృతిక కేంద్రం అమరావతి ₹119.27 కోట్లు ఆమోదం; 2,000 సీట్ల ఆడిటోరియం</td></tr>
<tr><td>ఏప్రిల్ 25, 2026</td><td>జస్టిస్ లిసా గిల్ — AP HC 6వ ముఖ్య న్యాయమూర్తి (మొదటి మహిళా CJ)</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════════
#  5. ART, CULTURE & GI TAGS  (div5)
#     IDs: 32601-32640
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_art_culture', 'AP Art, Culture & GI Tags', 'AP కళలు, సంస్కృతి & GI ట్యాగ్‌లు', """
<div class="concept-cover">
  <h1>AP కళలు, సంస్కృతి &amp; GI ట్యాగ్‌లు <span class="bi-te">/ AP Art, Culture &amp; GI Tags</span></h1>
  <div class="sub">Kuchipudi · Kalamkari · GI Tags · Guinness Records · Film Awards</div>
</div>

<div class="section-hdr">కూచిపూడి నృత్యం / Kuchipudi Dance</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>జన్మస్థలం</td><td>కూచిపూడి గ్రామం, కృష్ణా జిల్లా</td></tr>
<tr><td>స్థాపకుడు</td><td>సిద్ధేంద్ర యోగి (17వ శతాబ్దం)</td></tr>
<tr><td>UNESCO గుర్తింపు</td><td>2008 — అమూర్త సాంస్కృతిక వారసత్వం (Intangible Cultural Heritage)</td></tr>
<tr><td>గిన్నిస్ రికార్డ్</td><td>7,002 నర్తకులు — ఆంధ్ర విశ్వవిద్యాలయం, విశాఖ; ఏప్రిల్ 11, 2017</td></tr>
<tr><td>ప్రత్యేకత</td><td>భాగవత మేళాల ఆధారిత శాస్త్రీయ నృత్యం</td></tr>
</table>

<div class="section-hdr">AP GI ట్యాగ్‌లు / AP GI Tags (22+)</div>
<table class="key-table">
<tr><th>ఉత్పత్తి / Product</th><th>ప్రదేశం / Place</th></tr>
<tr><td>కలంకారీ నేత (Kalamkari)</td><td>శ్రీకాళహస్తి (Pen) + మచిలీపట్నం (Block print)</td></tr>
<tr><td>కొండపల్లి బొమ్మలు</td><td>కొండపల్లి, కృష్ణా జిల్లా</td></tr>
<tr><td>ఎటికొప్పక బొమ్మలు</td><td>ఎటికొప్పక, రాజమహేంద్రవరం</td></tr>
<tr><td>ఉప్పాడ జమ్దాని చీర</td><td>ఉప్పాడ, కాకినాడ జిల్లా</td></tr>
<tr><td>బొబ్బిలి వీణ</td><td>బొబ్బిలి, విజయనగరం జిల్లా</td></tr>
<tr><td>తిరుపతి లడ్డు</td><td>తిరుమల, తిరుపతి</td></tr>
<tr><td>అరకు కాఫీ</td><td>అరకు వ్యాలీ, విశాఖ జిల్లా</td></tr>
<tr><td>బంగినపల్లి మామిడి</td><td>నందయాల / కర్నూలు</td></tr>
<tr><td>గుంటూరు సన్నం మిర్చి</td><td>గుంటూరు జిల్లా</td></tr>
<tr><td>బందరు లడ్డు</td><td>మచిలీపట్నం, కృష్ణా జిల్లా</td></tr>
</table>

<div class="section-hdr">చలనచిత్ర పురస్కారాలు / Film Awards</div>
<table class="key-table">
<tr><th>పురస్కారం</th><th>వివరాలు</th></tr>
<tr><td>Oscar 2023 Best Song</td><td>"నాటు నాటు" (RRR చిత్రం) — MM కీరవాణి; తొలి భారతీయ చలనచిత్ర గీతం Oscar</td></tr>
<tr><td>69వ జాతీయ చలనచిత్ర పురస్కారం</td><td>అల్లు అర్జున్ — Best Actor (పుష్ప చిత్రం); తొలి తెలుగు నటుడు</td></tr>
<tr><td>జ్ఞానపీఠ పురస్కారం 1970</td><td>విశ్వనాథ సత్యనారాయణ — తొలి తెలుగు జ్ఞానపీఠ విజేత</td></tr>
</table>

<div class="section-hdr">గిన్నిస్ రికార్డులు & ముఖ్య సంఘటనలు / Guinness Records & Events</div>
<table class="key-table">
<tr><th>సంఘటన</th><th>వివరాలు</th></tr>
<tr><td>విజయవాడ ఉత్సవ్ 2025</td><td>సెప్. 22-అక్టో. 2, 2025; 284 కార్యక్రమాలు; అతిపెద్ద డప్పు కళాకారుల సభ (3,000 మంది) గిన్నిస్</td></tr>
<tr><td>యోగాంధ్ర 2025</td><td>జూన్ 21, 2025; 5 లక్షల మంది; విశాఖ 28 km తీరం; గిన్నిస్ రికార్డ్</td></tr>
<tr><td>ఆవకాయ ఫెస్టివల్</td><td>జన. 8-10, 2026; విజయవాడ; సినిమా, సాహిత్యం, సంస్కృతి</td></tr>
<tr><td>Tirumala Nidi Sai రికార్డ్</td><td>డిసె. 9, 2025; తుని; ప్రపంచపు అతి చిన్న మోటారు సారె (91 గ్రాం)</td></tr>
</table>

<div class="section-hdr">UNESCO గుర్తింపులు / UNESCO Recognitions</div>
<p>• <b>తిరుమల కొండలు</b> + <b>ఎర్రమట్టి దిబ్బలు</b> (భీమిలి, విశాఖ) — ఆగ. 27, 2025న UNESCO World Heritage Tentative List లో చేర్పు</p>
<p>• ఎర్రమట్టి దిబ్బలు — 1,500 ఎకరాలు; ప్రపంచంలో కేవలం 3 చోట్ల మాత్రమే; National Geo-Heritage Monument</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  6. AP ECONOMY, INDUSTRIES & INFRASTRUCTURE  (div6)
#     IDs: 32641-32730
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_economy_infra', 'AP Economy, Industries & Infrastructure', 'AP ఆర్థిక వ్యవస్థ, పరిశ్రమలు & మౌలిక సదుపాయాలు', """
<div class="concept-cover">
  <h1>AP ఆర్థిక వ్యవస్థ &amp; మౌలిక సదుపాయాలు <span class="bi-te">/ AP Economy &amp; Infrastructure</span></h1>
  <div class="sub">GSDP · Swarnandhra 2047 · CII Summit · Agriculture Rankings</div>
</div>

<div class="section-hdr">AP GSDP & ఆర్థిక వ్యవస్థ / AP Economy</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>GSDP 2024-25 (నామమాత్ర)</td><td>₹16.41 లక్ష కోట్లు (₹16.41 lakh crore)</td></tr>
<tr><td>నామమాత్ర వృద్ధి</td><td>12.5%</td></tr>
<tr><td>వాస్తవ వృద్ధి</td><td>8.21% — దేశంలో 7వ స్థానం</td></tr>
<tr><td>తలసరి ఆదాయం</td><td>₹2,66,240 (జాతీయ సగటు కంటే 1.3x)</td></tr>
<tr><td>దేశ GDP లో వాటా</td><td>4.72%</td></tr>
<tr><td>జాతీయ ఆర్థిక ర్యాంకు</td><td>9వ స్థానం</td></tr>
<tr><td>GSVA కూర్పు</td><td>సేవలు 41.64% | వ్యవసాయం 37.20% | పరిశ్రమలు 21.16%</td></tr>
</table>

<div class="section-hdr">స్వర్ణ ఆంధ్ర@2047 విజన్ / Swarnandhra 2047 Vision</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>విడుదల తేదీ</td><td>డిసెంబర్ 13-14, 2024</td></tr>
<tr><td>GSDP లక్ష్యం</td><td>₹308 లక్ష కోట్లు ($2.4 trillion)</td></tr>
<tr><td>తలసరి లక్ష్యం</td><td>$43,000</td></tr>
<tr><td>వృద్ధి లక్ష్యం</td><td>15% నిరంతర వృద్ధి</td></tr>
</table>

<div class="section-hdr">CII 30వ Partnership Summit</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>తేదీ</td><td>నవంబర్ 14-15, 2025</td></tr>
<tr><td>ప్రదేశం</td><td>విశాఖపట్నం</td></tr>
<tr><td>పెట్టుబడులు</td><td>₹13.26 లక్ష కోట్లు</td></tr>
<tr><td>MoU లు</td><td>613 MoUs</td></tr>
<tr><td>ఉద్యోగాలు</td><td>16.31 లక్షల ఉద్యోగాలు</td></tr>
<tr><td>పాల్గొన్న దేశాలు</td><td>61 దేశాలు</td></tr>
</table>

<div class="section-hdr">వ్యవసాయ ర్యాంకులు / Agriculture Rankings</div>
<table class="key-table">
<tr><th>ఉత్పత్తి</th><th>AP ర్యాంకు</th></tr>
<tr><td>మిరపకాయ, కోకో (41%), ఆయిల్ పాం, పసుపు, టొమాటో, నిమ్మ</td><td>1వ స్థానం</td></tr>
<tr><td>మామిడి, జీడిపప్పు</td><td>2వ స్థానం</td></tr>
<tr><td>రొయ్యలు (Shrimp/Prawn)</td><td>దేశ ఉత్పత్తిలో 70%</td></tr>
</table>

<div class="section-hdr">ముఖ్య పరిశ్రమలు & మౌలిక సదుపాయాలు / Key Industries & Infrastructure</div>
<table class="key-table">
<tr><th>పరిశ్రమ / Project</th><th>వివరాలు</th></tr>
<tr><td>ArcelorMittal Nippon Steel (AMNS)</td><td>నక్కపల్లి, విశాఖ; ₹1.5 లక్ష కోట్లు; 24 MT సామర్థ్యం</td></tr>
<tr><td>AM Green గ్రీన్ అమ్మోనియా</td><td>కాకినాడ; 1.5 MTPA; ₹13,000 కోట్లు; ప్రపంచపు అతిపెద్ద</td></tr>
<tr><td>Google AI Hub</td><td>విశాఖపట్నం; $15 billion; ప్రపంచంలో USA తర్వాత 2వ అతిపెద్ద</td></tr>
<tr><td>NTPC గ్రీన్ హైడ్రోజన్ హబ్</td><td>పుడిమడక, విశాఖ; ₹1,85,000 కోట్లు; ప్రపంచపు అతిపెద్ద</td></tr>
<tr><td>BharatNet Phase 3</td><td>AP; ₹2,432 కోట్లు (APBIL); గ్రామ పంచాయతీలకు ఫైబర్</td></tr>
<tr><td>పోర్టులు & విమానాశ్రయాలు</td><td>1 Major Port (విశాఖ), 5 Minor Ports, 3 International Airports; భోగాపురం (GMR)</td></tr>
</table>

<div class="section-hdr">AP బడ్జెట్ 2025-26 / AP Budget</div>
<p>• మొత్తం: <b>₹3,22,359 కోట్లు</b> — పయ్యావుల కేశవ్ ఫిబ్రవరి 28, 2025న ప్రవేశపెట్టారు</p>
<p>• GST వసూళ్లు 2025-26 (4 నెలలు): ₹16,754 కోట్లు = వార్షిక లక్ష్యంలో 61%</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  7. AP HISTORY & FREEDOM FIGHTERS  (div7 + div7_mcqs)
#     IDs: 32731-32800 + 32881-32960
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_history', 'AP History & Freedom Fighters', 'AP చరిత్ర & స్వాతంత్ర్య సమరయోధులు', """
<div class="concept-cover">
  <h1>AP చరిత్ర &amp; స్వాతంత్ర్య సమరయోధులు <span class="bi-te">/ AP History &amp; Freedom Fighters</span></h1>
  <div class="sub">Ancient Dynasties · State Formation · Freedom Fighters · AP HC</div>
</div>

<div class="section-hdr">AP రాష్ట్ర ఏర్పాటు చరిత్ర / AP State Formation</div>
<table class="key-table">
<tr><th>తేదీ / Date</th><th>సంఘటన / Event</th></tr>
<tr><td>అక్టో. 1, 1953</td><td>ఆంధ్ర రాష్ట్రం ఏర్పాటు — రాజధాని కర్నూలు (First CM: టంగుటూరి ప్రకాశం పంతులు)</td></tr>
<tr><td>నవ. 1, 1956</td><td>ఆంధ్రప్రదేశ్ రాష్ట్రం ఏర్పాటు — రాజధాని హైదరాబాద్ (States Reorganisation Act 1956)</td></tr>
<tr><td>జూన్ 2, 2014</td><td>AP Reorganisation Act 2014 అమలు — తెలంగాణ 29వ రాష్ట్రంగా ఏర్పాటు</td></tr>
<tr><td>జూన్ 2, 2024</td><td>హైదరాబాద్ ఉమ్మడి రాజధాని హోదా ముగిసింది (10 సంవత్సరాలు)</td></tr>
</table>

<div class="section-hdr">ప్రాచీన రాజవంశాలు / Ancient Dynasties</div>
<table class="key-table">
<tr><th>రాజవంశం / Dynasty</th><th>రాజధాని / Capital</th><th>ముఖ్య విషయాలు</th></tr>
<tr><td>సాతవాహనులు (Satavahanas)</td><td>అమరావతి / ప్రతిష్టానపురం</td><td>స్థాపకుడు: సిముక; అమరావతి స్తూపం; బౌద్ధమతం</td></tr>
<tr><td>ఇక్ష్వాకులు (Ikshvakus)</td><td>విజయపురి (నాగార్జునకొండ)</td><td>3వ శతాబ్దం; బౌద్ధమత కేంద్రం</td></tr>
<tr><td>విష్ణుకుండినులు</td><td>అమరావతి</td><td>5-7వ శతాబ్దాలు</td></tr>
<tr><td>కాకతీయులు</td><td>వరంగల్</td><td>రుద్రమ దేవి, ప్రతాపరుద్రుడు; రామప్ప గుడి</td></tr>
<tr><td>విజయనగర సామ్రాజ్యం</td><td>హంపి</td><td>శ్రీకృష్ణదేవరాయలు; 1336-1646</td></tr>
<tr><td>రెడ్డి రాజులు</td><td>కొండవీడు / రాజమహేంద్రవరం</td><td>14-15వ శతాబ్దాలు</td></tr>
</table>

<div class="section-hdr">స్వాతంత్ర్య సమరయోధులు / Freedom Fighters from AP</div>
<table class="key-table">
<tr><th>పేరు / Name</th><th>వివరాలు / Details</th></tr>
<tr><td>అల్లూరి సీతారామ రాజు</td><td>1897-1924; రంపా తిరుగుబాటు (Rampa Rebellion) నాయకుడు; "మన్యం వీరుడు"</td></tr>
<tr><td>ఉయ్యాలవాడ నరసింహారెడ్డి</td><td>1857 పూర్వం తిరుగుబాటు; "అమర వీరుడు"</td></tr>
<tr><td>టంగుటూరి ప్రకాశం పంతులు</td><td>"ఆంధ్ర కేసరి"; మొదటి AP CM; స్వాతంత్ర్య సమరయోధుడు</td></tr>
<tr><td>పొట్టి శ్రీరాముల్లు</td><td>58 రోజుల నిరాహారదీక్ష; డిసె. 15, 1952 మరణం; ఆంధ్ర రాష్ట్ర నిర్మాత</td></tr>
<tr><td>కందుకూరి వీరేశలింగం</td><td>సంఘ సంస్కర్త; విధవా వివాహాలు; రాజమహేంద్రవరం</td></tr>
<tr><td>అన్నమయ్య</td><td>శ్రీ వేంకటేశ్వర స్వామి కీర్తనలు; "పద కవితా పితామహుడు"</td></tr>
</table>

<div class="section-hdr">కీలక వ్యక్తులు & కేంద్ర సంస్థలు / Key Facts</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>AP HC స్థాపన</td><td>జనవరి 1, 2019 అమరావతిలో (APRA 2014 Section 30 ప్రకారం)</td></tr>
<tr><td>AP HC 6వ ముఖ్య న్యాయమూర్తి</td><td>జస్టిస్ లిసా గిల్ (ఏప్రిల్ 25, 2026) — మొదటి మహిళా CJ</td></tr>
<tr><td>Potti Sriramulu విగ్రహం</td><td>58-అడుగులు; అమరావతిలో ప్రకటన (డిసె. 15, 2025)</td></tr>
<tr><td>AP ముఖ్య కార్యదర్శి 2026</td><td>G. సాయి ప్రసాద్ (IAS 1991 batch); మార్చి 1, 2026</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════════
#  8. ENVIRONMENT, ISRO & SPORTS  (div8 + div8_mcqs)
#     IDs: 32801-32880 + 32961-33060
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_environment_sports', 'AP Environment, ISRO & Sports', 'AP పర్యావరణం, ISRO & క్రీడలు', """
<div class="concept-cover">
  <h1>AP పర్యావరణం, ISRO &amp; క్రీడలు <span class="bi-te">/ AP Environment, ISRO &amp; Sports</span></h1>
  <div class="sub">National Parks · ISRO Sriharikota · PV Sindhu · Nitesh Kumar</div>
</div>

<div class="section-hdr">AP జాతీయ ఉద్యానవనాలు / AP National Parks</div>
<table class="key-table">
<tr><th>ఉద్యానవనం / National Park</th><th>నది / River</th><th>జిల్లా / District</th><th>ప్రత్యేకత</th></tr>
<tr><td>పాపికొండలు జాతీయ ఉద్యానవనం</td><td>గోదావరి నది</td><td>ఏలూరు, పశ్చిమ గోదావరి</td><td>Tiger Reserve</td></tr>
<tr><td>నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం</td><td>కృష్ణా నది</td><td>నంద్యాల + గుంటూరు</td><td>భారత్‌లో అతిపెద్ద Tiger Reserve; AP వాటా: 3,568 sq km</td></tr>
<tr><td>శ్రీ వేంకటేశ్వర జాతీయ ఉద్యానవనం</td><td>—</td><td>తిరుపతి జిల్లా</td><td>శేషాచలం బయోస్ఫియర్ రిజర్వ్ లో భాగం</td></tr>
</table>

<div class="section-hdr">ముఖ్య పర్యావరణ ప్రదేశాలు / Key Environmental Sites</div>
<table class="key-table">
<tr><th>ప్రదేశం</th><th>వివరాలు</th></tr>
<tr><td>కొరింగ మడ అడవులు (Coringa Mangroves)</td><td>కాకినాడ; భారత్‌లో 2వ అతిపెద్ద మడ అడవులు; Wildlife Sanctuary</td></tr>
<tr><td>పులికాట్ సరస్సు (Pulicat Lake)</td><td>తిరుపతి జిల్లా; భారత్‌లో 2వ అతిపెద్ద ఉప్పు నీటి సరస్సు; ఫ్లెమింగో నివాసం</td></tr>
<tr><td>రోళ్లపాడు GIB అభయారణ్యం</td><td>కర్నూలు జిల్లా; Great Indian Bustard (GIB) రక్షణ</td></tr>
<tr><td>ఎర్రమట్టి దిబ్బలు</td><td>భీమిలి, విశాఖ; 1,500 ఎకరాలు; ప్రపంచంలో కేవలం 3 చోట్ల; National Geo-Heritage Monument; UNESCO Tentative List (2025)</td></tr>
<tr><td>తిరుమల కొండలు</td><td>తిరుపతి; UNESCO Tentative List (ఆగ. 27, 2025)</td></tr>
<tr><td>ఎర్ర చందనం (Red Sanders)</td><td>శేషాచలం కొండలు; స్థానిక జాతి; అక్రమ రవాణా నిరోధకం</td></tr>
<tr><td>ఆలివ్ రిడ్లీ తాబేళ్ళు</td><td>AP తీరంలో గుడ్లు పెడతాయి; రక్షణ కార్యక్రమాలు</td></tr>
</table>

<div class="section-hdr">ISRO — SDSC SHAR, శ్రీహరికోట / ISRO Sriharikota</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>పూర్తి పేరు</td><td>Satish Dhawan Space Centre, Sriharikota Range (SDSC SHAR)</td></tr>
<tr><td>జిల్లా</td><td>తిరుపతి జిల్లా (Tirupati District)</td></tr>
<tr><td>100వ ప్రయోగం</td><td>NVS-02 (Navigation satellite) — జనవరి 29, 2025</td></tr>
<tr><td>SpaDeX</td><td>Space Docking Experiment — డిసెంబర్ 2024; తొలి భారతీయ స్పేస్ డాకింగ్</td></tr>
<tr><td>BHISHMA (Arogya Maitri)</td><td>3 units AIIMS మంగళగిరిలో జులై 19, 2025; 72 cubes; 10 నిమిషాల్లో deploy అవుతాయి</td></tr>
<tr><td>ISTC విశాఖ</td><td>International Seafarers Training Centre; IMU విశాఖ; సెప్. 20, 2025; దక్షిణ ఆసియాలో మొదటిది</td></tr>
</table>

<div class="section-hdr">AP క్రీడా ప్రముఖులు / AP Sports Personalities</div>
<table class="key-table">
<tr><th>క్రీడాకారుడు</th><th>విజయాలు</th></tr>
<tr><td>PV సింధు (బ్యాడ్మింటన్)</td><td>Rio 2016 రజతం + Tokyo 2020 కాంస్యం; 2 Olympic medals గెలిచిన తొలి భారత మహిళ</td></tr>
<tr><td>కిడంబి శ్రీకాంత్</td><td>BWF World Championships 2021 రజతం; గురువు: పుల్లెల గోపీచంద్</td></tr>
<tr><td>నితేష్ కుమార్</td><td>Para Olympics 2024 స్వర్ణం (Badminton SL3 category) — AP ఆటగాడు</td></tr>
<tr><td>పుల్లెల గోపీచంద్</td><td>All England Champion 2001; గోపీచంద్ Badminton Academy, హైదరాబాద్; సింధు & శ్రీకాంత్ కోచ్</td></tr>
</table>

<div class="section-hdr">AP పర్యావరణ విధానాలు / AP Environmental Policies</div>
<p>• AP గ్రీన్ హైడ్రోజన్ విధానం — NTPC హబ్ పుడిమడక ₹1,85,000 కోట్లు</p>
<p>• AP Universal Health Policy — Arogya Sri విస్తరణ; కేబినెట్ సెప్. 4, 2025</p>
<p>• స్వచ్ఛ సర్వేక్షణ్ 2024 — AP నగరాలు 5 జాతీయ అవార్డులు (జులై 12, 2025)</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  9. PADMA AWARDS, AP HC & INSTITUTIONS  (div9)
#     IDs: 32881-32960
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_awards_institutions', 'AP Padma Awards, HC & Institutions', 'AP పద్మ పురస్కారాలు, HC & సంస్థలు', """
<div class="concept-cover">
  <h1>AP పద్మ పురస్కారాలు &amp; కేంద్ర సంస్థలు <span class="bi-te">/ AP Padma Awards &amp; Central Institutions</span></h1>
  <div class="sub">Padma Awards · AP High Court · Central Universities · Constitution</div>
</div>

<div class="section-hdr">పద్మ పురస్కారాల స్థాయిలు / Padma Award Levels</div>
<table class="key-table">
<tr><th>పురస్కారం</th><th>స్థాయి</th><th>ఏర్పాటు సంవత్సరం</th></tr>
<tr><td>పద్మ విభూషణ్ (Padma Vibhushan)</td><td>రెండవ అత్యున్నత పౌర పురస్కారం</td><td>1954</td></tr>
<tr><td>పద్మ భూషణ్ (Padma Bhushan)</td><td>మూడవ అత్యున్నత పౌర పురస్కారం</td><td>1954</td></tr>
<tr><td>పద్మ శ్రీ (Padma Sri)</td><td>నాల్గవ అత్యున్నత పౌర పురస్కారం</td><td>1954</td></tr>
</table>

<div class="section-hdr">AP వ్యక్తులకు పద్మ పురస్కారాలు / Padma Awards to AP Persons</div>
<table class="key-table">
<tr><th>పేరు</th><th>పురస్కారం</th><th>సంవత్సరం</th><th>రంగం</th></tr>
<tr><td>SP బాలసుబ్రహ్మణ్యం</td><td>పద్మ విభూషణ్ (మరణానంతరం)</td><td>2021</td><td>సినిమా / సంగీతం</td></tr>
<tr><td>K. విశ్వనాథ్</td><td>పద్మ విభూషణ్</td><td>2017</td><td>సినిమా దర్శకత్వం</td></tr>
<tr><td>నందమూరి బాలకృష్ణ</td><td>పద్మ భూషణ్</td><td>2025</td><td>కళలు / సినిమా</td></tr>
<tr><td>దీపిక రెడ్డి</td><td>పద్మ శ్రీ</td><td>2026</td><td>కూచిపూడి నృత్యం (5 దశాబ్దాలు)</td></tr>
<tr><td>పుల్లెల గోపీచంద్</td><td>పద్మ భూషణ్</td><td>2014</td><td>క్రీడలు (బ్యాడ్మింటన్)</td></tr>
</table>

<div class="section-hdr">AP హైకోర్టు / AP High Court</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>స్థాపన తేదీ</td><td>జనవరి 1, 2019</td></tr>
<tr><td>ప్రదేశం</td><td>అమరావతి (నాయోరేపల్లి)</td></tr>
<tr><td>చట్ట ప్రాతిపదిక</td><td>APRA 2014 Section 30</td></tr>
<tr><td>6వ ముఖ్య న్యాయమూర్తి</td><td>జస్టిస్ లిసా గిల్ — ఏప్రిల్ 25, 2026 (మొదటి మహిళా CJ)</td></tr>
</table>

<div class="section-hdr">AP లో కేంద్ర సంస్థలు / Central Institutions in AP</div>
<table class="key-table">
<tr><th>సంస్థ</th><th>ప్రదేశం</th><th>ప్రత్యేకత</th></tr>
<tr><td>AIIMS మంగళగిరి</td><td>మంగళగిరి, గుంటూరు జిల్లా</td><td>All India Institute of Medical Sciences</td></tr>
<tr><td>IIT తిరుపతి</td><td>తిరుపతి</td><td>ఇండియన్ ఇన్‌స్టిట్యూట్ ఆఫ్ టెక్నాలజీ</td></tr>
<tr><td>NIT విశాఖపట్నం</td><td>విశాఖపట్నం</td><td>National Institute of Technology</td></tr>
<tr><td>ISRO SDSC SHAR</td><td>శ్రీహరికోట, తిరుపతి</td><td>Space Launch Centre</td></tr>
<tr><td>DRDO క్షిపణి కేంద్రం</td><td>అమరావతి సమీపం</td><td>మే 2025 శంకుస్థాపన</td></tr>
<tr><td>ISTC విశాఖ</td><td>IMU విశాఖ</td><td>International Seafarers Training Centre; దక్షిణ ఆసియాలో మొదటిది</td></tr>
</table>

<div class="section-hdr">రాజ్యాంగ & ప్రభుత్వ వ్యవస్థ / Constitutional Facts</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>AP అసెంబ్లీ స్థానాలు</td><td>175</td></tr>
<tr><td>AP లోక్‌సభ స్థానాలు</td><td>25</td></tr>
<tr><td>AP రాజ్యసభ స్థానాలు</td><td>11</td></tr>
<tr><td>AP గవర్నర్</td><td>జస్టిస్ S. అబ్దుల్ నజీర్ (ఫిబ్రవరి 2023 నుండి)</td></tr>
<tr><td>AP స్పీకర్</td><td>చింతకాయల అయ్యన్నపాత్రుడు</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════════
# 10. APRA 2014 & 2026 REORGANISATION  (div10)
#     IDs: 32961-33060
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('ap_reorganisation', 'AP Reorganisation Act 2014 & 2026', 'APRA 2014 & 2026 పునర్వ్యవస్థీకరణ', """
<div class="concept-cover">
  <h1>AP పునర్వ్యవస్థీకరణ చట్టాలు <span class="bi-te">/ AP Reorganisation Acts 2014 &amp; 2026</span></h1>
  <div class="sub">Bifurcation 2014 · Amaravati Capital · 28 Districts · AP HC</div>
</div>

<div class="section-hdr">APRA 2014 — AP Reorganisation Act 2014</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>Act నంబర్</td><td>Act No. 6/2014</td></tr>
<tr><td>లోక్‌సభ ఆమోదం</td><td>ఫిబ్రవరి 18, 2014</td></tr>
<tr><td>రాజ్యసభ ఆమోదం</td><td>ఫిబ్రవరి 20, 2014</td></tr>
<tr><td>అమలు తేదీ</td><td>జూన్ 2, 2014</td></tr>
<tr><td>తెలంగాణ</td><td>29వ రాష్ట్రంగా ఏర్పాటు; హైదరాబాద్ రాజధాని</td></tr>
<tr><td>ఉమ్మడి రాజధాని</td><td>హైదరాబాద్ — 10 సంవత్సరాలు (2014-2024)</td></tr>
<tr><td>హైదరాబాద్ హోదా ముగింపు</td><td>జూన్ 2, 2024</td></tr>
</table>

<div class="section-hdr">APRA 2014 ముఖ్య నిబంధనలు / Key Provisions</div>
<table class="key-table">
<tr><th>Section</th><th>విషయం</th></tr>
<tr><td>Section 5</td><td>AP రాజధాని నిర్ణయం</td></tr>
<tr><td>Section 30</td><td>AP హైకోర్టు ఏర్పాటు</td></tr>
<tr><td>Section 46</td><td>ఉమ్మడి హైకోర్టు నిర్వహణ (పంచాయితీ వరకు)</td></tr>
<tr><td>Schedule 12</td><td>Polavaram National Project విభజన</td></tr>
</table>

<div class="section-hdr">APRA సవరణ 2026 / APRA Amendment 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>Act నంబర్</td><td>Act No. 7/2026</td></tr>
<tr><td>లోక్‌సభ ఆమోదం</td><td>ఏప్రిల్ 1, 2026</td></tr>
<tr><td>రాజ్యసభ ఆమోదం</td><td>ఏప్రిల్ 2, 2026</td></tr>
<tr><td>రాష్ట్రపతి ఆమోదం</td><td>ఏప్రిల్ 6, 2026</td></tr>
<tr><td>ముఖ్య నిర్ణయం</td><td>అమరావతి — ఏకైక &amp; శాశ్వత రాజధాని (Section 5 సవరణ)</td></tr>
<tr><td>అమలు</td><td>June 2, 2024 నుండి retroactive effect</td></tr>
</table>

<div class="section-hdr">AP రాజధానుల చరిత్ర / AP Capitals History</div>
<table class="key-table">
<tr><th>కాలం</th><th>రాజధాని</th></tr>
<tr><td>1953-1956</td><td>కర్నూలు (ఆంధ్ర రాష్ట్రం)</td></tr>
<tr><td>1956-2014</td><td>హైదరాబాద్ (ఉమ్మడి AP)</td></tr>
<tr><td>2014-2024</td><td>హైదరాబాద్ (ఉమ్మడి రాజధాని) + అమరావతి (ప్రణాళిక)</td></tr>
<tr><td>2024 నుండి</td><td>అమరావతి (ఏకైక శాశ్వత రాజధాని)</td></tr>
</table>

<div class="section-hdr">AP 28 జిల్లాలు / AP 28 Districts</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>పాత జిల్లాలు</td><td>13 (2014 విభజన వరకు)</td></tr>
<tr><td>2022 పునర్వ్యవస్థీకరణ</td><td>13 → 26 జిల్లాలు</td></tr>
<tr><td>2026 కొత్త జిల్లాలు</td><td>పోలవరం జిల్లా + మార్కాపురం జిల్లా</td></tr>
<tr><td>ప్రస్తుత జిల్లాలు</td><td>28 (జనవరి 1, 2026 నుండి)</td></tr>
</table>

<div class="section-hdr">AP రాష్ట్ర స్పెషల్ హోదా / AP Special Status</div>
<p>• APRA 2014 Section 94: AP కి 5 సంవత్సరాలు కేంద్ర ప్రత్యేక ప్రోత్సాహకాలు హామీ</p>
<p>• ప్రత్యేక హోదా (Special Category Status) డిమాండ్ — AP రాజకీయ కేంద్ర బిందువు</p>
<p>• 14వ ఆర్థిక సంఘం 2015: SCS రద్దు; రాష్ట్రాలకు రెవెన్యూ వాటా పెంపు</p>
</p>
"""))

# ─────────────────────────────────────────────────────────────────
#  Seed all notes into DB
# ─────────────────────────────────────────────────────────────────
inserted = 0
for tag, label, label_te, html in NOTES:
    try:
        cur.execute(
            f"INSERT INTO concept_notes (tag, label, label_te, html) VALUES ({ph},{ph},{ph},{ph}) "
            f"ON CONFLICT (tag) DO UPDATE SET label=EXCLUDED.label, label_te=EXCLUDED.label_te, html=EXCLUDED.html",
            (tag, label, label_te, html)
        )
        inserted += 1
    except Exception as e:
        # SQLite doesn't support ON CONFLICT DO UPDATE with same syntax, try replace
        try:
            cur.execute(f"INSERT OR REPLACE INTO concept_notes (tag,label,label_te,html) VALUES ({ph},{ph},{ph},{ph})",
                        (tag, label, label_te, html))
            inserted += 1
        except Exception as e2:
            print(f"[ap-divs-notes] Error seeding {tag}: {e2}")

if not USE_POSTGRES:
    conn.commit()
conn.close()
print(f"[ap-divs-notes] Done. Seeded {inserted}/{len(NOTES)} AP CA div concept notes.")

# ── Runtime patch of app.CONCEPT_MAP ──────────────────────────────
# Remove old generic AP CA div entries (32201-33200) and add 12 topic-specific ones
_AP_DIV_RANGES = [
    (32201, 32290, 'ap_elections_cabinet'),
    (32291, 32380, 'ap_super_six_schemes'),
    (32381, 32500, 'ap_events_2025'),
    (32501, 32600, 'ap_events_2026'),
    (32601, 32640, 'ap_art_culture'),
    (32641, 32730, 'ap_economy_infra'),
    (32731, 32800, 'ap_history'),
    (32801, 32880, 'ap_environment_sports'),
    (32881, 32960, 'ap_awards_institutions'),
    (32961, 33060, 'ap_reorganisation'),
    (33061, 33130, 'ap_history'),
    (33131, 33200, 'ap_environment_sports'),
]
try:
    import sys as _sys
    _app = _sys.modules.get('app') or _sys.modules.get('__main__')
    if _app and hasattr(_app, 'CONCEPT_MAP'):
        _app.CONCEPT_MAP[:] = [
            (lo, hi, tag) for lo, hi, tag in _app.CONCEPT_MAP
            if not (32201 <= lo <= 33200)
        ] + _AP_DIV_RANGES
        print(f'[ap-divs-notes] Patched CONCEPT_MAP with {len(_AP_DIV_RANGES)} AP div topic ranges.')
except Exception as _pe:
    print(f'[ap-divs-notes] CONCEPT_MAP patch skipped: {_pe}')
