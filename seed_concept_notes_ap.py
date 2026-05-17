#!/usr/bin/env python3
"""
seed_concept_notes_ap.py
Bilingual (Telugu + English) concept notes for:
  AP Current Affairs 2026  (IDs 32001–32200)
  Tags: ap_ca_budget (32001–32140), ap_ca_state (32041–32200)
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
#  1.  AP CURRENT AFFAIRS — BUDGET & ECONOMY 2025-26 / 2026-27
#      IDs 32001–32140   tag: ap_ca_budget
# ═══════════════════════════════════════════════════════════════
NOTES.append(('ap_ca_budget',
               'AP CA 2026 — AP Budget, Economy & Amaravati',
               'ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ 2026 — బడ్జెట్, ఆర్థికం & అమరావతి',
"""
<div class="concept-cover">
  <h1>ఆంధ్రప్రదేశ్ బడ్జెట్ &amp; ఆర్థికం 2026-27<span class="bi-te"></span></h1>
  <div class="sub">AP Budget ₹2,77,830 Cr | Amaravati Capital | Polavaram | AP Economy</div>
</div>

<div class="section-hdr">ఆంధ్రప్రదేశ్ బడ్జెట్ 2026-27 / AP State Budget 2026-27</div>
<table class="key-table">
<tr><th>అంశం / Item</th><th>వివరాలు / Details</th></tr>
<tr><td>మొత్తం బడ్జెట్</td><td>₹2,77,830 కోట్లు (Total Budget Rs 2,77,830 crore)</td></tr>
<tr><td>ఆదాయ రాబడి</td><td>₹1,94,140 కోట్లు (Revenue Receipts)</td></tr>
<tr><td>ఆర్థిక మంత్రి</td><td>పయ్యావుల కేశవ్ (Finance Minister — TDP)</td></tr>
<tr><td>AP అమర్‌సేవ ప్రాజెక్టు</td><td>₹7,910 కోట్లు; 205 ఆంబులెన్సులు — ఆరోగ్య సేవ</td></tr>
<tr><td>IFC రుణం</td><td>₹300 కోట్లు (International Finance Corporation)</td></tr>
<tr><td>AP లాజిస్టిక్స్ పాలసీ</td><td>2025-2030 — ఎగుమతి అభివృద్ధి, మల్టీ-మోడల్ రవాణా</td></tr>
<tr><td>SC/ST సంక్షేమ కేటాయింపు</td><td>₹25,000 కోట్లకు పైగా (SC/ST Welfare)</td></tr>
<tr><td>ECMS</td><td>41,863 కొత్త విద్యుత్ కనెక్షన్‌లు (ECMS connections)</td></tr>
</table>

<div class="section-hdr">AP GSDP & ఆర్థిక సూచికలు / AP Economy Indicators</div>
<table class="key-table">
<tr><th>సూచిక / Indicator</th><th>విలువ / Value</th></tr>
<tr><td>AP GSDP 2025-26</td><td>₹12 లక్షల కోట్లు అంచనా (Estimated Rs 12 lakh crore)</td></tr>
<tr><td>AP GSDP వృద్ధి రేటు</td><td>8%+ లక్ష్యం (Target)</td></tr>
<tr><td>AP TFR (Total Fertility Rate)</td><td>1.5 (జాతీయ సగటు 2.1 కంటే చాలా తక్కువ)</td></tr>
<tr><td>AP అక్షరాస్యత</td><td>67.02% (Literacy rate — Census 2011)</td></tr>
<tr><td>AP జనాభా</td><td>5.26 కోట్లు (Census 2011)</td></tr>
<tr><td>AP జిల్లాలు</td><td>25 జిల్లాలు (2022 పునర్వ్యవస్థీకరణ తర్వాత)</td></tr>
<tr><td>AP శాసనసభలో మహిళలు</td><td>28.63% (Women in AP Assembly — highest among large states)</td></tr>
<tr><td>SC జనాభా</td><td>దాదాపు 17% (AP SC population)</td></tr>
<tr><td>AP మత్స్య ఉత్పత్తి</td><td>జాతీయంగా 1వ స్థానం (Aquaculture rank — 1st nationally)</td></tr>
<tr><td>AP సోలార్ ఉత్పత్తి</td><td>అనంతపురం — ఆసియాలో అతి పెద్ద సోలార్ పార్క్</td></tr>
</table>

<div class="section-hdr">అమరావతి రాజధాని / Amaravati Capital</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>అమరావతి చట్టం</td><td>అమరావతి క్యాపిటల్ రీజియన్ యాక్ట్ — జులై 2, 2024 (AP Assembly)</td></tr>
<tr><td>CRDA</td><td>Capital Region Development Authority — అమరావతి అభివృద్ధి సంస్థ</td></tr>
<tr><td>రైతుల భూ విరాళం</td><td>33,000+ ఎకరాలు; 29,000+ రైతు కుటుంబాలు</td></tr>
<tr><td>అసెంబ్లీ కాంప్లెక్స్</td><td>వెలగపూడి ప్రాంతంలో నిర్మిస్తున్నారు</td></tr>
<tr><td>AP హైకోర్టు</td><td>2019 నుండి అమరావతిలో పనిచేస్తోంది</td></tr>
<tr><td>AP CRDA చట్టం</td><td>AP Capital Region Development Authority Act 2014</td></tr>
<tr><td>జిల్లా</td><td>గుంటూరు జిల్లా (పాత); ప్రస్తుతం 'గుంటూరు+కృష్ణా' సమీపం</td></tr>
</table>

<div class="section-hdr">పోలవరం ప్రాజెక్ట్ / Polavaram Project</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>నది</td><td>గోదావరి నది (Godavari river)</td></tr>
<tr><td>నీటిపారుదల</td><td>7.2 లక్షల ఎకరాలు (7.2 lakh acres irrigation)</td></tr>
<tr><td>హోదా</td><td>జాతీయ ప్రాజెక్ట్ (National Project)</td></tr>
<tr><td>తాగునీరు</td><td>విశాఖ నగరానికి తాగునీటి పథకం</td></tr>
<tr><td>విద్యుత్</td><td>960 మెగావాట్‌ల జలవిద్యుత్ ఉత్పత్తి</td></tr>
</table>

<div class="section-hdr">AP పోర్టులు & మౌలిక సదుపాయాలు / AP Ports & Infrastructure</div>
<table class="key-table">
<tr><th>పోర్టు/ప్రాజెక్ట్</th><th>వివరాలు</th></tr>
<tr><td>విశాఖపట్నం పోర్టు</td><td>భారతదేశంలో అతిపెద్ద నావికా కమాండ్ స్థావరం — EASTERN NAVAL COMMAND</td></tr>
<tr><td>మచిలీపట్నం పోర్టు</td><td>కృష్ణా జిల్లాలో కొత్త అంతర్జాతీయ పోర్టు అభివృద్ధి</td></tr>
<tr><td>కృష్ణపట్నం పోర్టు</td><td>నెల్లూరు జిల్లాలో; దక్షిణాది అతిపెద్ద వాణిజ్య నౌకాశ్రయాల్లో ఒకటి</td></tr>
<tr><td>కాకినాడ పోర్టు</td><td>తూర్పు గోదావరి జిల్లాలో; చమురు పరిశ్రమ కేంద్రం</td></tr>
<tr><td>AP గ్రీన్‌ఫీల్డ్ హైవే</td><td>అమరావతి-రాయలసీమ కారిడార్</td></tr>
<tr><td>SriCity SEZ</td><td>చిత్తూరు జిల్లాలో ప్రత్యేక ఆర్థిక మండలి; మల్టీ-ప్రొడక్ట్ SEZ</td></tr>
<tr><td>AP Fintech Valley</td><td>విశాఖపట్నంలో ఫిన్‌టెక్ హబ్</td></tr>
<tr><td>RINL</td><td>రాష్ట్రీయ ఇస్పాత్ నిగమ్ — విశాఖ స్టీల్ ప్లాంట్ (Rashtriya Ispat Nigam)</td></tr>
<tr><td>అనంతపురం సోలార్</td><td>ఆసియాలో అతిపెద్ద సోలార్ పార్కుల్లో ఒకటి</td></tr>
<tr><td>Smart Cities</td><td>విశాఖపట్నం + కాకినాడ (Smart Cities Mission)</td></tr>
</table>

<div class="section-hdr">AP Global Investors Summit 2023</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>స్థలం</td><td>విశాఖపట్నం (Visakhapatnam)</td></tr>
<tr><td>నిర్వహణ సంస్థ</td><td>AP ప్రభుత్వం — TDP-JSP-BJP కూటమి</td></tr>
<tr><td>ఉద్దేశ్యం</td><td>దేశ-విదేశ పెట్టుబడులు ఆకర్షించడం</td></tr>
</table>

<div class="section-hdr">MILAN 2026 నావల్ ఎక్సర్సైజ్ / MILAN 2026</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>స్థలం</td><td>విశాఖపట్నం (Visakhapatnam)</td></tr>
<tr><td>భాగస్వాముల సంఖ్య</td><td>50+ దేశాల నావికాదళాలు</td></tr>
<tr><td>ప్రాముఖ్యత</td><td>భారత నావికాదళ దౌత్యం; హిందూ మహాసముద్ర భాగస్వామ్యం</td></tr>
</table>

<div class="section-hdr">తెలంగాణ బడ్జెట్ 2026-27 (సంక్షిప్తంగా) / Telangana Budget 2026-27 (Brief)</div>
<table class="key-table">
<tr><th>రంగం</th><th>కేటాయింపు</th></tr>
<tr><td>మొత్తం బడ్జెట్</td><td>₹3,24,234 కోట్లు</td></tr>
<tr><td>వ్యవసాయం</td><td>₹47,267 కోట్లు (అత్యధిక)</td></tr>
<tr><td>పట్టణాభివృద్ధి</td><td>₹47,387 కోట్లు</td></tr>
<tr><td>విద్యుత్ (Energy)</td><td>₹38,105 కోట్లు</td></tr>
<tr><td>విద్య</td><td>₹24,166 కోట్లు</td></tr>
<tr><td>ఆరోగ్యం</td><td>₹8,814 కోట్లు</td></tr>
<tr><td>TS GSDP వృద్ధి</td><td>6.9% (Telangana GSDP growth)</td></tr>
<tr><td>TS GSDP మొత్తం</td><td>₹17.82 లక్షల కోట్లు</td></tr>
<tr><td>పేదరికం తగ్గింపు</td><td>41.5% → 9.4%</td></tr>
<tr><td>TS అక్షరాస్యత</td><td>74.9%</td></tr>
<tr><td>దావోస్ WEF 2026 పెట్టుబడి</td><td>₹28,693 కోట్లు; 9 MoUs</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════
#  2.  AP CURRENT AFFAIRS — STATE POLITICS, SCHEMES & EVENTS
#      IDs 32041–32200   tag: ap_ca_state
# ═══════════════════════════════════════════════════════════════
NOTES.append(('ap_ca_state',
               'AP CA 2026 — State Politics, Schemes, Infrastructure & Events',
               'AP కరెంట్ అఫైర్స్ 2026 — రాజకీయాలు, పథకాలు, మౌలిక సదుపాయాలు & సంఘటనలు',
"""
<div class="concept-cover">
  <h1>ఆంధ్రప్రదేశ్ — రాజకీయాలు, పథకాలు &amp; సంఘటనలు 2026</h1>
  <div class="sub">2024 AP Elections | Navaratnalu | Polavaram | AP Schemes | Appointments</div>
</div>

<div class="section-hdr">AP 2024 ఎన్నికలు & రాజకీయ పరిణామాలు / 2024 AP Elections</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>2024 ఫలితం</td><td>TDP-JSP-BJP కూటమి 164 సీట్లు గెలిచింది (మొత్తం 175)</td></tr>
<tr><td>YSRCP</td><td>కేవలం 11 సీట్లు (2019లో 151 నుండి భారీ పతనం)</td></tr>
<tr><td>ముఖ్యమంత్రి</td><td>నారా చంద్రబాబు నాయుడు (TDP — 4వ సారి CM)</td></tr>
<tr><td>ఉప ముఖ్యమంత్రి</td><td>పవన్ కళ్యాణ్ (JSP నేత)</td></tr>
<tr><td>గవర్నర్</td><td>ఎస్ అబ్దుల్ నజీర్ (S. Abdul Nazeer)</td></tr>
<tr><td>మహిళా ప్రాతినిధ్యం</td><td>28.63% (AP Assembly)</td></tr>
<tr><td>AP శాసనసభ మొత్తం స్థానాలు</td><td>175 స్థానాలు</td></tr>
<tr><td>AP వెలిపడి ప్రాంతాలు</td><td>25 జిల్లాలు; 175 నియోజకవర్గాలు</td></tr>
</table>

<div class="section-hdr">నవరత్నాలు — TDP-JSP-BJP ప్రభుత్వ ముఖ్య హామీలు / Navaratnalu Schemes</div>
<table class="key-table">
<tr><th>పథకం / Scheme</th><th>వివరాలు / Details</th></tr>
<tr><td>NTR భరోసా పెన్షన్</td><td>₹3,000/నెల — వృద్ధులు, వికలాంగులు (NTR Bharosa Pension)</td></tr>
<tr><td>అమ్మ వోడి</td><td>₹15,000/సంవత్సరం — పిల్లలను బడికి పంపే తల్లులకు (Amma Vodi)</td></tr>
<tr><td>తల్లికి వందనం</td><td>మహిళా సంక్షేమ పథకం (Thalliki Vandanam)</td></tr>
<tr><td>సూపర్ సిక్స్</td><td>6 ముఖ్య ఎన్నికల హామీలు (Super Six promises)</td></tr>
<tr><td>ఉచిత బస్ పాస్</td><td>మహిళలకు ఉచిత APSRTC బస్ ప్రయాణం</td></tr>
<tr><td>గ్రూప్-1 కోచింగ్</td><td>APPSC అభ్యర్థులకు ఉచిత శిక్షణ</td></tr>
</table>

<div class="section-hdr">AP సంక్షేమ పథకాలు (వివరాలు) / AP Welfare Schemes</div>
<table class="key-table">
<tr><th>పథకం</th><th>వివరాలు</th></tr>
<tr><td>NTR భరోసా పెన్షన్</td><td>₹3,000/నెల — వృద్ధులు (60+), వికలాంగులు, వితంతువులు</td></tr>
<tr><td>అమ్మ వోడి</td><td>₹15,000/సంవత్సరం — వారి పిల్లలు పాఠశాలలో చదివే తల్లులందరికీ</td></tr>
<tr><td>AP అమర్‌సేవ</td><td>₹7,910 కోట్లు; 205 ఆంబులెన్సులు — ఆరోగ్య సేవలు</td></tr>
<tr><td>అన్నదాత సుఖీభవ</td><td>రైతులకు పంట రుణ మాఫీ పథకం</td></tr>
<tr><td>YSR రైతు భరోసా</td><td>రైతులకు ఆదాయ రక్షణ; హెక్టారుకు ₹13,500</td></tr>
<tr><td>జగనన్న ఇళ్ళ కార్యక్రమం</td><td>పేదలకు ఇళ్ళు (Housing scheme)</td></tr>
</table>

<div class="section-hdr">AP ముఖ్య నియామకాలు & పదవులు / Key Appointments 2025-26</div>
<table class="key-table">
<tr><th>పదవి</th><th>వ్యక్తి</th></tr>
<tr><td>AP ముఖ్యమంత్రి</td><td>నారా చంద్రబాబు నాయుడు (TDP)</td></tr>
<tr><td>AP ఉప ముఖ్యమంత్రి</td><td>పవన్ కళ్యాణ్ (JSP)</td></tr>
<tr><td>AP గవర్నర్</td><td>ఎస్. అబ్దుల్ నజీర్ (S. Abdul Nazeer)</td></tr>
<tr><td>AP హైకోర్టు ప్రధాన న్యాయమూర్తి</td><td>న్యాయమూర్తి ధీరజ్ సింగ్ ఠాకూర్</td></tr>
<tr><td>AP CRDA కమిషనర్</td><td>CRDA ప్రధాన కమిషనర్</td></tr>
<tr><td>AP DGP</td><td>ఆంధ్రప్రదేశ్ పోలీస్ ఉన్నతాధికారి</td></tr>
<tr><td>తెలంగాణ CM</td><td>ఎ. రేవంత్ రెడ్డి (Congress)</td></tr>
<tr><td>తెలంగాణ గవర్నర్</td><td>జిష్ణు దేవ్ వర్మ (Jishnu Dev Varma)</td></tr>
</table>

<div class="section-hdr">AP విద్య & విశ్వవిద్యాలయాలు / AP Education</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>AP కేంద్రీయ విశ్వవిద్యాలయం</td><td>కర్నూలులో (Kurnool) — Central University of AP</td></tr>
<tr><td>AP IIT</td><td>IIT తిరుపతి (IIT Tirupati)</td></tr>
<tr><td>JNTU</td><td>JNTU అనంతపురం, కాకినాడ</td></tr>
<tr><td>ఆంధ్ర విశ్వవిద్యాలయం</td><td>విశాఖపట్నంలో — తెలుగు నాట పురాతన విశ్వవిద్యాలయం</td></tr>
<tr><td>ఉస్మానియా విశ్వవిద్యాలయం</td><td>హైదరాబాద్ (TS) — 1918లో స్థాపన</td></tr>
<tr><td>AICTE</td><td>305 సంస్థల గుర్తింపు రద్దు (2025)</td></tr>
<tr><td>AP Skill Development</td><td>NSDC తో కలిసి నైపుణ్య శిక్షణ</td></tr>
</table>

<div class="section-hdr">AP పర్యాటకం & ఆధ్యాత్మికత / AP Tourism</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>తిరుమల-తిరుపతి</td><td>ప్రపంచంలో అత్యధిక సందర్శకులు పొందే ఆధ్యాత్మిక కేంద్రం</td></tr>
<tr><td>శ్రీశైలం</td><td>జ్యోతిర్లింగం (Srisailam — Jyotirlinga)</td></tr>
<tr><td>సింహాచలం</td><td>విష్ణు-వరాహ లక్ష్మీనరసింహస్వామి దేవాలయం, విశాఖపట్నం</td></tr>
<tr><td>MILAN 2026</td><td>విశాఖపట్నం నావల్ ఎక్సర్సైజ్ — 50+ దేశాలు</td></tr>
<tr><td>AP పండుగలు</td><td>ఉగాది, శ్రీరామనవమి, కృష్ణాష్టమి — ముఖ్య పండుగలు</td></tr>
</table>

<div class="section-hdr">AP ప్రత్యేక హోదా & విభజన / AP Special Status & Reorganisation</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>AP పునర్వ్యవస్థీకరణ చట్టం</td><td>2014 AP Reorganisation Act — జూన్ 2, 2014 విభజన</td></tr>
<tr><td>ప్రత్యేక హోదా డిమాండ్</td><td>SCS (Special Category Status) — కేంద్రం అంగీకరించలేదు</td></tr>
<tr><td>బ్యాకవర్డ్ జిల్లాలు</td><td>రాయలసీమ + ఉత్తరాంధ్ర — వెనుకబడిన ప్రాంతాలు</td></tr>
<tr><td>RINL వ్యతిరేకత</td><td>AP ప్రభుత్వం విశాఖ స్టీల్ ప్లాంట్ ప్రైవేటీకరణను వ్యతిరేకిస్తోంది</td></tr>
</table>

<div class="section-hdr">తెలంగాణ రాజకీయాలు & పథకాలు (సంక్షిప్తంగా) / Telangana Politics & Schemes</div>
<table class="key-table">
<tr><th>అంశం</th><th>వివరాలు</th></tr>
<tr><td>2023 TS ఎన్నికలు</td><td>Congress 64 సీట్లు గెలిచి అధికారంలోకి వచ్చింది</td></tr>
<tr><td>BRS (TRS)</td><td>39 సీట్లు; KCR నేతృత్వం</td></tr>
<tr><td>TS CM</td><td>రేవంత్ రెడ్డి (Congress)</td></tr>
<tr><td>గృహ లక్ష్మి</td><td>₹2,500/నెల — ఇంటి యజమాని మహిళలకు (Gruha Lakshmi)</td></tr>
<tr><td>అన్న సముద్రం</td><td>రాయితీ ధరలో భోజనం (Anna Samudram)</td></tr>
<tr><td>పల్లె ప్రగతి</td><td>గ్రామీణ అభివృద్ధి & పరిశుభ్రత (Palle Pragathi)</td></tr>
<tr><td>అసరా పెన్షన్</td><td>₹2,016/నెల — సామాజిక భద్రత పెన్షన్ (Asara)</td></tr>
<tr><td>కాళేశ్వరం</td><td>గోదావరి నదిపై లిఫ్ట్ ఇరిగేషన్ — ప్రపంచ అతిపెద్ద</td></tr>
<tr><td>జీనోమ్ వ్యాలీ</td><td>మేడ్చల్-మల్కాజిగిరి — బయోటెక్ హబ్</td></tr>
<tr><td>TS ఫార్మా సిటీ</td><td>19,333 ఎకరాలు — ప్రపంచ అతిపెద్ద ఫార్మా క్లస్టర్</td></tr>
<tr><td>గద్దర్ సినీ అవార్డులు 2025</td><td>డిసెంబర్ 2025 — 75 విభాగాలు</td></tr>
<tr><td>హైదరాబాద్ మెట్రో ఫేజ్-2</td><td>నాగోల్ నుండి రాయదుర్గం వరకు</td></tr>
<tr><td>మేడిగడ్డ బ్యారేజ్</td><td>జగిత్యాల జిల్లా (Kaleshwaram's Medigadda barrage)</td></tr>
<tr><td>HITEC City</td><td>హైదరాబాద్ IT హబ్; Cyber Towers స్థానం</td></tr>
<tr><td>TS IT ఎగుమతులు</td><td>₹2.5 లక్షల కోట్లు (2024-25)</td></tr>
<tr><td>TS ఫార్మా సిటీ జిల్లా</td><td>రంగారెడ్డి జిల్లా (Rangareddy)</td></tr>
<tr><td>TS జిల్లాలు</td><td>33 జిల్లాలు</td></tr>
</table>

<div class="section-hdr">AP 2026లో ముఖ్య సంఘటనలు / AP Key Events 2026</div>
<table class="key-table">
<tr><th>సంఘటన</th><th>వివరాలు</th></tr>
<tr><td>2024 AP వరదలు</td><td>కాకినాడ, ఏలూరు, నాంద్యాల జిల్లాలు తీవ్రంగా ప్రభావితం</td></tr>
<tr><td>MILAN 2026</td><td>విశాఖ నావల్ ఎక్సర్సైజ్ — 50+ దేశాలు; ఫిబ్రవరి 2026</td></tr>
<tr><td>AP Global Investors Summit</td><td>విశాఖపట్నం — పెట్టుబడి ఆకర్షణ</td></tr>
<tr><td>WAVES 2025</td><td>World Audio Visual Entertainment Summit — ముంబై</td></tr>
<tr><td>అమరావతి నిర్మాణం</td><td>పార్లమెంట్ హౌస్, హైకోర్టు, CM క్యాంప్ ఆఫీస్ నిర్మాణం కొనసాగుతోంది</td></tr>
</table>

<p class="bi-te">Key takeaways: AP's 2024 election was a historic landslide for TDP-JSP-BJP coalition with 164/175 seats. Amaravati is being developed as a greenfield capital with the Capital Region Act passed in July 2024. Polavaram on Godavari is the National Project targeting 7.2 lakh acres irrigation. AP leads nationally in aquaculture production and has Asia's largest solar park in Anantapur.</p>
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
print(f"[seed_concept_notes_ap] Inserted {len(NOTES)} AP concept notes (ap_ca_budget, ap_ca_state).")

# ── Patch CONCEPT_MAP in app module if already loaded ──────────────────────────
# The actual seeded AP CA questions use BASE_ID=32201 (not 32001).
# This extends the map so concept notes are found for IDs 32201–33200.
try:
    import sys as _sys
    if 'app' in _sys.modules:
        _app = _sys.modules['app']
        if hasattr(_app, 'CONCEPT_MAP'):
            _existing_lo = {e[0] for e in _app.CONCEPT_MAP}
            if 32201 not in _existing_lo:
                _app.CONCEPT_MAP.extend([
                    (32201, 32600, 'ap_ca_budget'),
                    (32601, 33200, 'ap_ca_state'),
                ])
                print('[seed_concept_notes_ap] Extended CONCEPT_MAP with AP CA div IDs 32201-33200.')
except Exception as _e:
    print(f'[seed_concept_notes_ap] CONCEPT_MAP patch skipped: {_e}')

# Chain-load AP CA div topic notes (10 topic-cluster concept notes, IDs 32201-33200)
import seed_concept_notes_ap_divs  # noqa: E402

# Chain-load individual question concept notes (first 10 AP CA questions, IDs 32001-32010)
import seed_concept_notes_ap_q1to10  # noqa: E402
seed_concept_notes_ap_q1to10.seed()
