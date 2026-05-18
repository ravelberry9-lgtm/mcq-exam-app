"""
seed_ap_ca_div3.py — AP Current Affairs Division 3: 2025 January–August Major Events
ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ — విభాగం 3: 2025 జనవరి–ఆగస్టు ముఖ్య సంఘటనలు

Sources verified: Eenadu Pratibha (https://pratibha.eenadu.net/currentaffairs/index/2-15)

AUDIT CHANGES (2026-05-18):
1. REMOVED ~40 junk MCQs — short 1-4 word question texts (e.g. "జనవరి పర్యటన",
   "బడ్జెట్ విభాగం", "RINL చర్యకు", "పోలవరం ప్రాజెక్టు", "క్వాంటం వ్యాలీ",
   "యోగాంధ్ర కార్యక్రమం", "సూపర్ సిక్స్ పథకాలు", "జులై-ఆగస్టు సంఘటనలు",
   "అమరావతి నిర్మాణ") with raw numeric options and wrong/mismatched answers.
   These appeared in 5 batches of 8 questions each (answer cycling b→c→d).
2. FIXED section 7 question "సూపర్ సిక్స్ పథకాలు" junk entries — అన్నదాత
   సుఖీభవ starts Aug 2, NOT July 1.
3. FIXED (2026-05-18 second pass): Yogandhra participant count — HTML notes confirm
   actual Guinness-verified count = 3,00,105 (3.01 లక్షలు), NOT 5 లక్షలు.
   5 లక్షలు was the TARGET; Guinness record = 3,00,105. Changed answer from "d"
   to "c" and updated option c text and explanation. Also fixed SECTIONS_JSON audio.
"""
import json as _json

SECTIONS_JSON = [
    {
        "title": "PM మోదీ జనవరి 8, 2025 — విశాఖ పర్యటన",
        "sub": "PM Modi Jan 8, 2025 Vizag Visit — NTPC Green Hydrogen Hub",
        "audio": "ప్రధానమంత్రి నరేంద్ర మోదీ జనవరి 8, 2025న విశాఖపట్నంలో ₹2 లక్షల కోట్లు విలువైన ప్రాజెక్టులు ప్రారంభించారు. పుడిమడక వద్ద NTPC గ్రీన్ హైడ్రోజన్ హబ్ (₹1,85,000 కోట్లు). 10 రోడ్డు ప్రాజెక్టులు (₹4,593 కోట్లు). 6 రైల్వే ప్రాజెక్టులు (₹6,028 కోట్లు). AP కి అతిపెద్ద సింగిల్-డే ఇన్వెస్ట్‌మెంట్.",
        "html": """<div class="concept-cover">
  <h1>PM Modi Vizag Visit &nbsp;<span class="bi-te">/ PM మోదీ విశాఖ పర్యటన</span></h1>
  <div class="sub">January 8, 2025 • ₹2 lakh crore projects • Largest single-day investment in AP</div>
</div>

<div class="section-hdr">Visit Snapshot / పర్యటన వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td><b>January 8, 2025</b></td><td class="bi-te">జనవరి 8, 2025</td></tr>
<tr><td>Total project value</td><td><b>₹2,00,000+ crore</b></td><td class="bi-te">₹2 లక్షల కోట్లుకు పైగా</td></tr>
<tr><td>Location</td><td>Visakhapatnam (Vizag)</td><td class="bi-te">విశాఖపట్నం</td></tr>
<tr><td>Significance</td><td>Largest single-day investment in AP history</td><td class="bi-te">AP చరిత్రలో అతిపెద్ద single-day పెట్టుబడి</td></tr>
<tr><td>Hosts</td><td>CM N. Chandrababu Naidu + DCM Pawan Kalyan</td><td class="bi-te">CM చంద్రబాబు + DCM పవన్ కళ్యాణ్</td></tr>
</table>

<div class="section-hdr">Project Break-up / ప్రాజెక్టుల వివరాలు</div>
<table class="key-table">
<tr><th>Project</th><th>Value</th><th>Location</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>NTPC Green Hydrogen Hub</b></td><td>₹1,85,000 cr</td><td>Pudimadaka, Vizag dist</td><td class="bi-te">పుడిమడక — గ్రీన్ హైడ్రోజన్ హబ్</td></tr>
<tr><td>10 Road projects</td><td>₹4,593 cr</td><td>Across AP highways</td><td class="bi-te">10 రోడ్డు ప్రాజెక్టులు</td></tr>
<tr><td>6 Railway projects</td><td>₹6,028 cr</td><td>Doubling, electrification</td><td class="bi-te">6 రైల్వే ప్రాజెక్టులు</td></tr>
<tr><td>Other industry / infra</td><td>~₹4,400 cr</td><td>Petrochemicals, port</td><td class="bi-te">పెట్రోకెమికల్స్ + పోర్ట్</td></tr>
</table>

<p><b>Why Pudimadaka:</b> NTPC chose Pudimadaka (Vizag district) because of its 1,200-acre availability, proximity to Visakhapatnam port (export of green H2/ammonia) and existing 500 kV grid. The hub will produce <b>1.2 MMTPA of green hydrogen / ammonia</b> by 2032, powered by 20+ GW of dedicated renewable capacity. It is India's <b>largest single-site green hydrogen project</b> — a flagship of the National Green Hydrogen Mission (Jan 2023).</p>
<p class="bi-te">NTPC పుడిమడక ఎంచుకోవడానికి కారణాలు: 1,200 ఎకరాల భూమి, విశాఖ పోర్ట్ సమీపం (గ్రీన్ H2/అమ్మోనియా ఎగుమతి), 500 kV గ్రిడ్. 2032 నాటికి 1.2 MMTPA గ్రీన్ హైడ్రోజన్ ఉత్పత్తి లక్ష్యం. భారత్‌లోనే అతిపెద్ద ఏకైక-సైట్ గ్రీన్ H2 ప్రాజెక్ట్.</p>"""
    },
    {
        "title": "PM మోదీ మే 2, 2025 — అమరావతి పర్యటన",
        "sub": "PM Modi May 2, 2025 Amaravati — ₹58,000 Crore Projects",
        "audio": "PM మోదీ మే 2, 2025న అమరావతి పర్యటించి ₹58,000 కోట్లు విలువైన ప్రాజెక్టులు ప్రారంభించారు. శాసనసభ భవనం, హైకోర్టు భవనం, సచివాలయం నిర్మాణాలకు శంకుస్థాపన. అమరావతిలో 320 కి.మీ. వరల్డ్-క్లాస్ రవాణా నెట్‌వర్క్ (₹17,400 కోట్లు). భూ పూలింగ్ పథకంలో 1,281 కి.మీ. రహదారులు (₹20,400 కోట్లు). DRDO క్షిపణి పరీక్ష కేంద్రం. స్వర్ణ ఆంధ్ర@2047 విజన్ — 2047 కల్లా ₹308 లక్షల కోట్ల GDP లక్ష్యం.",
        "html": """<div class="concept-cover">
  <h1>PM Modi Amaravati Visit &nbsp;<span class="bi-te">/ PM మోదీ అమరావతి పర్యటన</span></h1>
  <div class="sub">May 2, 2025 • ₹58,000 crore projects • Assembly, HC, Secretariat foundations</div>
</div>

<div class="section-hdr">Foundation Stones Laid / శంకుస్థాపనలు</div>
<table class="key-table">
<tr><th>Project</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Assembly Building</b></td><td>Part of capital core</td><td class="bi-te">శాసనసభ భవనం</td></tr>
<tr><td><b>High Court Building</b></td><td>Part of capital core</td><td class="bi-te">హైకోర్టు భవనం</td></tr>
<tr><td><b>State Secretariat</b></td><td>5-tower complex</td><td class="bi-te">సచివాలయం</td></tr>
<tr><td>320 km world-class transport network</td><td>₹17,400 cr</td><td class="bi-te">320 కి.మీ. రవాణా నెట్‌వర్క్</td></tr>
<tr><td>Land-Pooling roads (1,281 km)</td><td>₹20,400 cr</td><td class="bi-te">LP పథకం 1,281 కి.మీ.</td></tr>
<tr><td>DRDO Missile Testing Centre</td><td>—</td><td class="bi-te">DRDO క్షిపణి పరీక్ష కేంద్రం</td></tr>
<tr><td><b>Total package</b></td><td><b>₹58,000 crore</b></td><td class="bi-te">మొత్తం ₹58,000 కోట్లు</td></tr>
</table>

<div class="section-hdr">Swarna Andhra@2047 Vision / స్వర్ణ ఆంధ్ర@2047</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Vision document released</td><td>December 13, 2024</td><td class="bi-te">డిసెంబర్ 13, 2024</td></tr>
<tr><td>2047 GSDP target</td><td><b>₹308 lakh crore</b></td><td class="bi-te">₹308 లక్షల కోట్ల GDP</td></tr>
<tr><td>Annual growth target</td><td>~15%</td><td class="bi-te">వార్షిక వృద్ధి 15%</td></tr>
<tr><td>Pillars</td><td>Skill, Infrastructure, Industry, Agriculture, Welfare, Governance</td><td class="bi-te">6 స్తంభాలు</td></tr>
</table>

<p><b>Significance:</b> The May 2, 2025 visit signalled the formal <i>restart of Amaravati capital city construction</i> after a 5-year YSRCP-era pause. Within 12 months (by May 2026) the secretariat shell, assembly skeleton and HC complex were visibly rising. PM Modi's presence anchored Amaravati as a national-priority project, aligning it with the Centre's ₹15,000-crore externally-aided loan facility (World Bank + ADB).</p>
<p class="bi-te">మే 2, 2025 పర్యటన — YSRCP కాలంలో 5 సంవత్సరాలు నిలిచిన అమరావతి నిర్మాణం అధికారికంగా పునఃప్రారంభం. 12 నెలల్లో సచివాలయం, శాసనసభ, హైకోర్టు భవనాల shell కనిపించాయి. ప్రపంచ బ్యాంక్ + ADB నుండి ₹15,000 కోట్ల రుణం.</p>"""
    },
    {
        "title": "AP బడ్జెట్ 2025-26",
        "sub": "AP Budget 2025-26 — ₹3,22,359 Crore by Payyavula Keshav",
        "audio": "ఆర్థిక మంత్రి పయ్యావుల కేశవ్ (TDP) ఫిబ్రవరి 28, 2025న AP బడ్జెట్ 2025-26 సమర్పించారు. మొత్తం బడ్జెట్: ₹3,22,359 కోట్లు. బడ్జెట్ సెషన్: ఫిబ్రవరి 24-28, 2025. తల్లికి వందనం కోసం ₹9,407 కోట్లు. ప్రాధాన్యత రంగాలు: అమరావతి నిర్మాణం, సూపర్ సిక్స్ పథకాలు, మౌలిక సదుపాయాలు, వ్యవసాయం.",
        "html": """<div class="concept-cover">
  <h1>AP Budget 2025-26 &nbsp;<span class="bi-te">/ AP బడ్జెట్ 2025-26</span></h1>
  <div class="sub">₹3,22,359 cr • FM Payyavula Keshav • Tabled Feb 28, 2025</div>
</div>

<div class="section-hdr">Budget Snapshot / బడ్జెట్ వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total budget size</td><td><b>₹3,22,359 crore</b></td><td class="bi-te">మొత్తం ₹3,22,359 కోట్లు</td></tr>
<tr><td>Presented by</td><td>Payyavula Keshav (TDP) — Finance Minister</td><td class="bi-te">పయ్యావుల కేశవ్ (ఆర్థిక మంత్రి)</td></tr>
<tr><td>Tabling date</td><td><b>February 28, 2025</b></td><td class="bi-te">ఫిబ్రవరి 28, 2025</td></tr>
<tr><td>Budget session</td><td>Feb 24 – 28, 2025</td><td class="bi-te">సెషన్: ఫిబ్రవరి 24-28</td></tr>
<tr><td>Revenue receipts (est.)</td><td>~₹2.51 lakh cr</td><td class="bi-te">రాబడి అంచనా</td></tr>
<tr><td>Fiscal deficit</td><td>~4.10% of GSDP</td><td class="bi-te">ఆర్థిక లోటు ~4.10%</td></tr>
</table>

<div class="section-hdr">Key Allocations / కీలక కేటాయింపులు</div>
<table class="key-table">
<tr><th>Scheme / Sector</th><th>Allocation</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Talliki Vandanam</td><td>₹9,407 cr</td><td class="bi-te">తల్లికి వందనం</td></tr>
<tr><td>Annadata Sukhibhava</td><td>₹6,300 cr</td><td class="bi-te">అన్నదాత సుఖీభవ</td></tr>
<tr><td>Amaravati capital works</td><td>₹6,000+ cr (state share)</td><td class="bi-te">అమరావతి నిర్మాణం</td></tr>
<tr><td>Polavaram (state portion)</td><td>see Centre's ₹5,936 cr</td><td class="bi-te">పోలవరం</td></tr>
<tr><td>NTR Bharosa pensions</td><td>₹27,000+ cr</td><td class="bi-te">NTR భరోసా</td></tr>
<tr><td>Agriculture &amp; allied</td><td>₹43,400+ cr</td><td class="bi-te">వ్యవసాయం</td></tr>
</table>

<p><b>Note on the next year's budget:</b> The <b>2026-27 budget</b> (totalling <b>₹3,32,205.34 crore</b>) was tabled in February 2026 by the same FM Payyavula Keshav, continuing Super Six allocations alongside Quantum Valley, Polavaram and Amaravati. The 2026-27 budget is covered in Division 4 — this division (Div 3) focuses on 2025-26.</p>
<p class="bi-te">2026-27 బడ్జెట్ ₹3,32,205.34 కోట్లు — ఫిబ్రవరి 2026లో సమర్పించబడింది (Division 4 విషయం). Division 3 — 2025-26 బడ్జెట్‌పై దృష్టి.</p>"""
    },
    {
        "title": "విశాఖ స్టీల్ ప్లాంట్ పునరుద్ధరణ (RINL)",
        "sub": "RINL Vizag Steel Plant Revival — ₹11,440 Crore Central Package",
        "audio": "రాష్ట్రీయ ఇస్పాత్ నిగమ్ (RINL) పునరుద్ధరణకు కేంద్రం ₹11,440 కోట్లు మంజూరు చేసింది. విశాఖపట్నం గాంధీనగర్ ప్రాంతంలో ఉంది. 2025 ప్రారంభంలో 2 Blast Furnaces పునరారంభం అయ్యాయి. ఆగస్టు 2025 కల్లా 3 Blast Furnaces పూర్తి స్థాయిలో పని చేయడం మొదలుపెట్టాయి. TDP-BJP ప్రభుత్వం ప్రైవేటైజేషన్ రద్దు చేసి పునరుద్ధరణ నిర్ణయం తీసుకుంది. 20,000+ మంది ఉద్యోగులు.",
        "html": """<div class="concept-cover">
  <h1>RINL Vizag Steel Plant Revival &nbsp;<span class="bi-te">/ విశాఖ స్టీల్ ప్లాంట్ పునరుద్ధరణ</span></h1>
  <div class="sub">₹11,440 cr central package • All 3 blast furnaces live by Aug 2025</div>
</div>

<div class="section-hdr">Plant Profile / ప్లాంట్ ప్రొఫైల్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full name</td><td>Rashtriya Ispat Nigam Limited (RINL)</td><td class="bi-te">రాష్ట్రీయ ఇస్పాత్ నిగమ్</td></tr>
<tr><td>Location</td><td><b>Gandhinagar, Visakhapatnam</b></td><td class="bi-te">గాంధీనగర్, విశాఖపట్నం</td></tr>
<tr><td>Unique feature</td><td>Only Indian shore-based integrated steel plant</td><td class="bi-te">భారత్‌లోనే ఏకైక సముద్రతీర ఉక్కు కర్మాగారం</td></tr>
<tr><td>Capacity</td><td>7.3 MTPA (Million Tonnes Per Annum)</td><td class="bi-te">7.3 MTPA సామర్థ్యం</td></tr>
<tr><td>Employees</td><td><b>20,000+</b> (direct + contract)</td><td class="bi-te">20,000+ ఉద్యోగులు</td></tr>
<tr><td>Established</td><td>1971 (commissioned 1992)</td><td class="bi-te">1971 (1992లో ప్రారంభం)</td></tr>
</table>

<div class="section-hdr">Revival Package &amp; Timeline / పునరుద్ధరణ ప్యాకేజీ</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Central package</td><td><b>₹11,440 crore</b></td><td class="bi-te">కేంద్రం ₹11,440 కోట్లు</td></tr>
<tr><td>2 BFs restarted</td><td>Early 2025</td><td class="bi-te">2025 ప్రారంభం</td></tr>
<tr><td>All 3 BFs operational</td><td><b>August 2025</b></td><td class="bi-te">ఆగస్టు 2025</td></tr>
<tr><td>Privatisation reversal</td><td>2024 (cabinet note rescinded)</td><td class="bi-te">ప్రైవేటైజేషన్ రద్దు</td></tr>
<tr><td>Workforce protection</td><td>No retrenchment clause</td><td class="bi-te">ఉద్యోగ భద్రత</td></tr>
</table>

<p><b>Political context:</b> The Vizag Steel privatisation (announced 2021) sparked AP-wide protests for 3+ years. The TDP-JSP-BJP government, leveraging its Centre alliance, lobbied for the ₹11,440-cr revival package — a major election promise delivered. Naidu's CM-Modi meeting on Sep 16, 2024 was the turning point; cabinet approval followed early 2025.</p>
<p class="bi-te">2021లో ప్రకటించిన ప్రైవేటైజేషన్‌కు 3+ సంవత్సరాలు ఆందోళనలు. TDP-JSP-BJP NDA కూటమి ₹11,440 కోట్లు పునరుద్ధరణ ప్యాకేజీ సాధించింది — ఎన్నికల హామీ నెరవేర్చబడింది. CBN-Modi సెప్టెంబర్ 16, 2024 భేటీ టర్నింగ్ పాయింట్.</p>"""
    },
    {
        "title": "పోలవరం ప్రాజెక్ట్",
        "sub": "Polavaram National Project — ₹5,936 Crore Union Budget Allocation",
        "audio": "పోలవరం జాతీయ ప్రాజెక్ట్ కి కేంద్ర బడ్జెట్ 2025-26లో ₹5,936 కోట్లు కేటాయించారు. మొత్తం పెండింగ్ బ్యాలెన్స్ గ్రాంట్: ₹12,157.53 కోట్లు. జాతీయ ప్రాజెక్ట్ హోదా 2010లో వచ్చింది. గోదావరి నదిపై నిర్మాణం. 36 TMC నీరు, 3.27 లక్షల ఎకరాల సాగు, తాగు నీరు, విద్యుత్ ఉత్పత్తి.",
        "html": """<div class="concept-cover">
  <h1>Polavaram National Project &nbsp;<span class="bi-te">/ పోలవరం ప్రాజెక్ట్</span></h1>
  <div class="sub">Multi-purpose dam on Godavari • National status 2010 • ₹5,936 cr (2025-26)</div>
</div>

<div class="section-hdr">Project Snapshot / ప్రాజెక్ట్ వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>River</td><td><b>Godavari</b></td><td class="bi-te">గోదావరి నది</td></tr>
<tr><td>Location</td><td>Polavaram, Alluri Sitharama Raju district (formerly Eluru/East Godavari)</td><td class="bi-te">పోలవరం</td></tr>
<tr><td>National Project status</td><td><b>2010</b> (under AP Reorganisation Act 2014 — Section 90)</td><td class="bi-te">జాతీయ ప్రాజెక్ట్ హోదా 2010</td></tr>
<tr><td>Type</td><td>Multi-purpose (irrigation + drinking + power)</td><td class="bi-te">బహుళ ప్రయోజన ప్రాజెక్ట్</td></tr>
<tr><td>Live storage</td><td>~75 TMC (gross ~194 TMC)</td><td class="bi-te">36+ TMC ఉపయోగపడే నీరు</td></tr>
<tr><td>Irrigation potential</td><td>3.27 lakh acres new ayacut</td><td class="bi-te">3.27 లక్షల ఎకరాల సాగు</td></tr>
<tr><td>Power generation</td><td>960 MW (12 × 80 MW)</td><td class="bi-te">960 MW విద్యుత్</td></tr>
</table>

<div class="section-hdr">2025-26 &amp; 2026-27 Funding / కేటాయింపులు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Union Budget 2025-26</td><td><b>₹5,936 crore</b></td><td class="bi-te">కేంద్ర బడ్జెట్ 2025-26</td></tr>
<tr><td>Total pending balance grant</td><td>₹12,157.53 crore</td><td class="bi-te">మొత్తం పెండింగ్ గ్రాంట్</td></tr>
<tr><td>Union Budget 2026-27</td><td>₹3,320.39 crore (next tranche)</td><td class="bi-te">2026-27 బడ్జెట్ ₹3,320.39 కోట్లు</td></tr>
<tr><td>New district (Dec 31, 2025)</td><td><b>Alluri Sitharama Raju</b> — HQ <b>Rampachodavaram</b> (carved for project)</td><td class="bi-te">కొత్త జిల్లా — రంపచోడవరం HQ</td></tr>
</table>

<p><b>Project status (mid-2026):</b> Spillway complete; ECRF dam Phase-2 in progress after diaphragm wall repair. R&amp;R of submergence villages (Telangana + Chhattisgarh + Odisha) under final phase. Earliest full impoundment targeted for kharif 2027. The Dec 31, 2025 carving of the dedicated Polavaram project district (Alluri Sitharama Raju, HQ Rampachodavaram) was a Cabinet decision to fast-track land + R&amp;R clearances.</p>
<p class="bi-te">డిసెంబర్ 31, 2025న కొత్త జిల్లా అల్లూరి సీతారామరాజు (HQ రంపచోడవరం) ఏర్పాటు — పోలవరం R&amp;R, భూసేకరణకు ప్రత్యేక జిల్లా. స్పిల్‌వే పూర్తి; ECRF డ్యామ్ Phase-2 కొనసాగుతుంది. 2027 ఖరీఫ్ నాటికి full impoundment లక్ష్యం.</p>"""
    },
    {
        "title": "అమరావతి క్వాంటం వ్యాలీ",
        "sub": "Amaravati Quantum Valley — Idea Aug 2025, Foundation Feb 7 2026, Dedication Apr 14 2026 (Div 4)",
        "audio": "AP ప్రభుత్వం అమరావతిలో 50 ఎకరాల క్వాంటం వ్యాలీ ఏర్పాటు చేస్తోంది. ఆగస్టు 2025లో ఈ ఆలోచన ప్రారంభమైంది. ఎనిమిది నెలల రికార్డు సమయంలో రెండు క్వాంటం రిఫరెన్స్ ఫెసిలిటీస్ ఏర్పాటు చేశారు — IBM Quantum System Two (156-qubit Heron processor) హార్డ్‌వేర్‌గా, TCS ముఖ్య IT భాగస్వామిగా; L&T, CDAC, IITs, 50+ సంస్థలు పాల్గొంటున్నాయి. ఫౌండేషన్ స్టోన్ ఫిబ్రవరి 7, 2026 (CM చంద్రబాబు + కేంద్ర మంత్రి జితేంద్ర సింగ్), ఏప్రిల్ 14, 2026న అంకితం లక్ష్యం (World Quantum Day + అంబేద్కర్ జయంతి).",
        "html": """<div class="concept-cover">
  <h1>Amaravati Quantum Valley (AQCC) &nbsp;<span class="bi-te">/ అమరావతి క్వాంటం వ్యాలీ</span></h1>
  <div class="sub">50-acre campus • IBM Quantum System Two (Heron R2, 156 qubits) • Foundation Feb 7 2026</div>
</div>

<div class="section-hdr">Quantum Valley Snapshot / వ్యాలీ వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Site</td><td>Amaravati capital region — <b>50 acres</b></td><td class="bi-te">అమరావతి, 50 ఎకరాలు</td></tr>
<tr><td>Idea announced</td><td>August 2025</td><td class="bi-te">ఆగస్టు 2025</td></tr>
<tr><td><b>Foundation Stone</b></td><td><b>February 7, 2026</b> — CM Naidu + Union Minister Dr. Jitendra Singh</td><td class="bi-te">ఫిబ్రవరి 7, 2026 — శంకుస్థాపన</td></tr>
<tr><td><b>Dedication</b></td><td><b>April 14, 2026</b> — World Quantum Day + Ambedkar Jayanti</td><td class="bi-te">ఏప్రిల్ 14, 2026 — అంకితం</td></tr>
<tr><td>Time taken (idea → dedication)</td><td>~8 months (record)</td><td class="bi-te">8 నెలల రికార్డు</td></tr>
<tr><td>Branding</td><td>Amaravati Quantum Computing Campus (AQCC)</td><td class="bi-te">AQCC</td></tr>
</table>

<div class="section-hdr">Hardware &amp; Partners / హార్డ్‌వేర్ + భాగస్వాములు</div>
<table class="key-table">
<tr><th>Partner</th><th>Role</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>IBM</b></td><td>Quantum hardware — <b>Quantum System Two with Heron R2 processor (156 qubits, superconducting)</b></td><td class="bi-te">IBM — Quantum System Two, Heron R2 (156 qubits)</td></tr>
<tr><td>TCS</td><td>Lead IT / systems integration partner</td><td class="bi-te">TCS — ముఖ్య IT భాగస్వామి</td></tr>
<tr><td>L&amp;T</td><td>Construction &amp; facility build</td><td class="bi-te">L&amp;T — నిర్మాణం</td></tr>
<tr><td>CDAC, CDOT</td><td>Indian quantum software stack</td><td class="bi-te">CDAC, CDOT</td></tr>
<tr><td>IITs / IISc / academia</td><td>Research + talent pipeline</td><td class="bi-te">IITs, IISc</td></tr>
<tr><td>Total stakeholders</td><td><b>50+ organisations</b></td><td class="bi-te">50+ సంస్థలు</td></tr>
</table>

<p><b>Important clarification:</b> The naming convention "Amaravati 1S / 1Q" that circulated in some unreliable sources is <i>not the official naming</i> — the canonical hardware is <b>IBM Quantum System Two with the Heron R2 processor</b> (156 superconducting qubits). The dedication date of April 14, 2026 was chosen for its dual symbolism: World Quantum Day (Apr 14 marks Planck's constant 4.14 × 10⁻¹⁵ eV·s) and Dr. B.R. Ambedkar Jayanti.</p>
<p class="bi-te">అమరావతి 1S/1Q అనే పేరు అధికారికం కాదు — అసలు హార్డ్‌వేర్ IBM Quantum System Two with Heron R2 (156 qubits, superconducting). ఏప్రిల్ 14: World Quantum Day (Planck constant 4.14 × 10⁻¹⁵ eV·s) + అంబేద్కర్ జయంతి — రెండు ప్రతీకాత్మక తేదీలు.</p>"""
    },
    {
        "title": "జూన్ 2025 — యోగాంధ్ర & INS అర్నాల",
        "sub": "Yogandhra June 21 (Guinness 3.01 Lakh) + INS Arnala First ASW Corvette",
        "audio": "యోగాంధ్ర: జూన్ 21, 2025 (అంతర్జాతీయ యోగా దినోత్సవం) న విశాఖపట్నంలో 28 కి.మీ. తీర ప్రాంతంలో 3.01 లక్షలు (3,00,105) మంది పాల్గొన్నారు (లక్ష్యం 5 లక్షులు; గిన్నిస్ రికార్డు: 3,00,105). PM మోదీ, CM చంద్రబాబు పాల్గొన్నారు. Largest Open-Air Yoga Gathering — గిన్నిస్ వరల్డ్ రికార్డ్ సాధించింది. INS అర్నాల: భారతీయ నౌకాదళం మొట్టమొదటి Shallow-Water ASW (Anti-Submarine Warfare) Corvette. 77 మీటర్ల పొడవు, 1490 టన్నుల బరువు. విశాఖపట్నం తూర్పు నావల్ కమాండ్‌లో ప్రవేశపెట్టారు.",
        "html": """<div class="concept-cover">
  <h1>Yogandhra &amp; INS Arnala &nbsp;<span class="bi-te">/ యోగాంధ్ర &amp; INS అర్నాల</span></h1>
  <div class="sub">June 21, 2025 — Guinness 3,00,105 yogis on 28 km Vizag coast + first ASW corvette</div>
</div>

<div class="section-hdr">Yogandhra — Guinness Record / యోగాంధ్ర</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td><b>June 21, 2025</b> (International Yoga Day)</td><td class="bi-te">జూన్ 21, 2025</td></tr>
<tr><td>Location</td><td>Visakhapatnam — RK Beach to Bheemunipatnam</td><td class="bi-te">RK బీచ్ నుండి భీముణిపట్నం</td></tr>
<tr><td>Stretch</td><td><b>28 km coastal corridor</b></td><td class="bi-te">28 కి.మీ. తీర ప్రాంతం</td></tr>
<tr><td>Target participants</td><td>5 lakh</td><td class="bi-te">లక్ష్యం 5 లక్షలు</td></tr>
<tr><td><b>Guinness-verified count</b></td><td><b>3,00,105 (3.01 lakh)</b></td><td class="bi-te">గిన్నిస్ — 3,00,105</td></tr>
<tr><td>Record name</td><td>Largest Open-Air Yoga Gathering</td><td class="bi-te">అతిపెద్ద ఓపెన్-ఎయిర్ యోగా</td></tr>
<tr><td>Dignitaries</td><td>PM Narendra Modi + CM N. Chandrababu Naidu</td><td class="bi-te">PM మోదీ + CM చంద్రబాబు</td></tr>
</table>

<div class="section-hdr">INS Arnala — First ASW Corvette / INS అర్నాల</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Type</td><td><b>Shallow-Water ASW Corvette</b> (first of class)</td><td class="bi-te">Shallow-Water ASW Corvette (1st)</td></tr>
<tr><td>Commissioned at</td><td>Eastern Naval Command, Visakhapatnam</td><td class="bi-te">తూర్పు నావల్ కమాండ్</td></tr>
<tr><td>Length</td><td>77 metres</td><td class="bi-te">77 మీటర్లు</td></tr>
<tr><td>Displacement</td><td>1,490 tonnes</td><td class="bi-te">1,490 టన్నులు</td></tr>
<tr><td>Builder</td><td>GRSE Kolkata (with L&amp;T Kattupalli)</td><td class="bi-te">GRSE కోల్‌కతా</td></tr>
<tr><td>Crest motto</td><td>"Arnavey Shauryam" (Valour in the Ocean)</td><td class="bi-te">"అర్ణవే శౌర్యం"</td></tr>
</table>

<p><b>Why Yogandhra mattered:</b> The 3,00,105 figure is the <i>Guinness-verified count</i>, not the original 5 lakh target. The event positioned AP as a wellness-tourism destination and Vizag as a national-stage city — coming just six months after the Jan 8, 2025 PM Modi visit to Pudimadaka.</p>
<p class="bi-te">యోగాంధ్రలో 5 లక్షలు లక్ష్యం; గిన్నిస్ సర్టిఫై చేసిన నిజమైన సంఖ్య = 3,00,105. ఈ ఈవెంట్ AP ని wellness-tourism కేంద్రంగా, విశాఖను జాతీయ నగరంగా నిలబెట్టింది.</p>"""
    },
    {
        "title": "సూపర్ సిక్స్ 2025 ముఖ్య తేదీలు",
        "sub": "Super Six Key Launches — Talliki Vandanam, Annadata, Stree Shakti",
        "audio": "సూపర్ సిక్స్ పథకాల ముఖ్య ప్రారంభ తేదీలు 2025: జూన్ 12 — తల్లికి వందనం (ప్రభుత్వ 1వ వార్షికోత్సవం). ఆగస్టు 2 — అన్నదాత సుఖీభవ: తొలి విడత ₹7,000 (రాష్ట్రం ₹5,000 + కేంద్రం ₹2,000), ప్రారంభం తూర్పు వీరయ్యపాలెం, దార్సి మండలం, ప్రకాశం జిల్లా. ఆగస్టు 15 — స్త్రీ శక్తి: ఉచిత బస్సు ప్రయాణం పథకానికి అధికారిక పేరు 'స్త్రీ శక్తి' — స్వాతంత్ర్య దినోత్సవం, 1వ వార్షికోత్సవం.",
        "html": """<div class="concept-cover">
  <h1>Super Six 2025 Launches &nbsp;<span class="bi-te">/ సూపర్ సిక్స్ 2025 ముఖ్య తేదీలు</span></h1>
  <div class="sub">3 flagship launches in summer 2025 — Jun 12, Aug 2, Aug 15</div>
</div>

<div class="section-hdr">Three 2025 Launch Dates / 2025 మూడు ముఖ్య తేదీలు</div>
<table class="key-table">
<tr><th>Date</th><th>Scheme</th><th>Significance</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Jun 12, 2025</b></td><td>Talliki Vandanam</td><td>Govt 1st anniversary (CM oath Jun 12, 2024)</td><td class="bi-te">తల్లికి వందనం — 1వ వార్షికోత్సవం</td></tr>
<tr><td><b>Aug 2, 2025</b></td><td>Annadata Sukhibhava</td><td>1st installment of ₹7,000 to 46.86 lakh farmers</td><td class="bi-te">అన్నదాత సుఖీభవ</td></tr>
<tr><td><b>Aug 15, 2025</b></td><td>Stree Shakti official naming</td><td>Independence Day + 1-yr anniversary of free-bus rollout</td><td class="bi-te">స్త్రీ శక్తి అధికారిక పేరు</td></tr>
</table>

<div class="section-hdr">Talliki Vandanam — Quick Facts / తల్లికి వందనం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Benefit</td><td>₹15,000/yr to mother of school-going child (Class 1-12)</td><td class="bi-te">విద్యార్థి తల్లికి ₹15,000/yr</td></tr>
<tr><td>Attendance rule</td><td>Minimum 75%</td><td class="bi-te">కనీసం 75% హాజరు</td></tr>
<tr><td>2025-26 budget</td><td>₹9,407 crore</td><td class="bi-te">₹9,407 కోట్లు</td></tr>
<tr><td>Eligible students</td><td>~69.16 lakh</td><td class="bi-te">~69.16 లక్షల విద్యార్థులు</td></tr>
</table>

<div class="section-hdr">Annadata Sukhibhava — Quick Facts / అన్నదాత సుఖీభవ</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launch venue</td><td>Thurpu Veerayyapalem, Darsi mandal, Prakasam dist</td><td class="bi-te">తూర్పు వీరయ్యపాలెం, దార్సి, ప్రకాశం</td></tr>
<tr><td>Annual benefit</td><td>₹20,000 per farmer family</td><td class="bi-te">రైతుకు ₹20,000/yr</td></tr>
<tr><td>Split</td><td>State ₹14,000 + Centre ₹6,000 (PM-KISAN)</td><td class="bi-te">రాష్ట్రం ₹14,000 + కేంద్రం ₹6,000</td></tr>
<tr><td>1st installment</td><td>₹7,000 to 46.86 lakh farmers — ₹3,175 cr disbursed</td><td class="bi-te">తొలి విడత ₹7,000</td></tr>
</table>

<p><b>Stree Shakti naming clarification:</b> The free APSRTC bus travel for women was originally rolled out on <b>August 15, 2024</b> (Independence Day, the launch day). The "Stree Shakti" <i>official brand name</i> was given exactly one year later on <b>August 15, 2025</b> — at the 1st anniversary the scheme also expanded to all 5 APSRTC zones with the formal naming ceremony.</p>
<p class="bi-te">ఉచిత బస్సు ప్రయాణం పథకం ఆగస్టు 15, 2024న ప్రారంభం. 'స్త్రీ శక్తి' అనే అధికారిక పేరు ఒక సంవత్సరం తరువాత ఆగస్టు 15, 2025న పెట్టారు — 1వ వార్షికోత్సవం + అన్ని 5 APSRTC జోన్‌లకు విస్తరణ.</p>"""
    },
    {
        "title": "జులై–ఆగస్టు 2025 ఇతర ముఖ్య సంఘటనలు",
        "sub": "Other Key Events Jul–Aug 2025: BHISHMA, Handloom, Swachh Awards, HC Judges",
        "audio": "జులై 12, 2025 — స్వచ్ఛ సర్వేక్షణ్ అవార్డులు 2024: AP నగరాలు 5 అవార్డులు సాధించాయి. జులై 19, 2025 — BHISHMA (ఆరోగ్య మైత్రి క్యూబ్): 3 యూనిట్లు AIIMS మంగళగిరిలో స్థాపించారు; 72 క్యూబ్‌లు, 10 నిమిషాల్లో డిప్లాయ్. ఆగస్టు 7, 2025 — జాతీయ హస్తకళా మ్యూజియం + నేతన్న భరోసా ₹25,000. ఆగస్టు 4 & 8, 2025 — AP హైకోర్టు 4 శాశ్వత న్యాయమూర్తులు నియమించారు (SC కొలీజియం, CJI B.R. గావాయ్ హయాంలో).",
        "html": """<div class="concept-cover">
  <h1>Other Key Events July–August 2025 &nbsp;<span class="bi-te">/ జులై–ఆగస్టు 2025 సంఘటనలు</span></h1>
  <div class="sub">Swachh Awards • BHISHMA • Handloom Day • HC Judges</div>
</div>

<div class="section-hdr">July 2025 / జులై 2025</div>
<table class="key-table">
<tr><th>Date</th><th>Event</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Jul 12, 2025</b></td><td>Swachh Survekshan 2024 awards announced — AP cities won <b>5 awards</b></td><td class="bi-te">స్వచ్ఛ సర్వేక్షణ్ 2024 — AP 5 అవార్డులు</td></tr>
<tr><td><b>Jul 19, 2025</b></td><td>BHISHMA (Bharat Health Initiative for Sahyog Hita and Maitri) — 3 cubes installed at <b>AIIMS Mangalagiri</b></td><td class="bi-te">BHISHMA — AIIMS మంగళగిరి</td></tr>
</table>

<div class="section-hdr">BHISHMA Cube — Mobile Hospital / ఆరోగ్య మైత్రి క్యూబ్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full form</td><td>Bharat Health Initiative for Sahyog, Hita &amp; Maitri</td><td class="bi-te">భారత్ హెల్త్ ఇనిషియేటివ్</td></tr>
<tr><td>Modules</td><td><b>72 cubes</b> in one unit (modular)</td><td class="bi-te">72 క్యూబ్‌లు</td></tr>
<tr><td>Deployment time</td><td><b>10 minutes</b></td><td class="bi-te">10 నిమిషాల్లో డిప్లాయ్</td></tr>
<tr><td>Use</td><td>Disaster response, mass-casualty, frontier deployment</td><td class="bi-te">విపత్తు సహాయం, యుద్ధ క్షేత్రం</td></tr>
<tr><td>AP units</td><td>3 cubes at AIIMS Mangalagiri (training centre)</td><td class="bi-te">AIIMS మంగళగిరిలో 3 యూనిట్లు</td></tr>
</table>

<div class="section-hdr">August 2025 / ఆగస్టు 2025</div>
<table class="key-table">
<tr><th>Date</th><th>Event</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Aug 4 &amp; 8, 2025</td><td>SC Collegium under CJI <b>B.R. Gavai</b> appointed 4 permanent judges to AP HC</td><td class="bi-te">AP HC 4 శాశ్వత న్యాయమూర్తులు</td></tr>
<tr><td><b>Aug 7, 2025</b></td><td>National Handloom Day — <b>National Handloom Museum</b> inaugurated + <b>Netanna Bharosa ₹25,000</b> disbursement to weavers</td><td class="bi-te">జాతీయ హస్తకళా మ్యూజియం + నేతన్న భరోసా ₹25,000</td></tr>
<tr><td>Aug 2, 2025</td><td>Annadata Sukhibhava 1st installment (Darsi)</td><td class="bi-te">అన్నదాత సుఖీభవ తొలి విడత</td></tr>
<tr><td>Aug 15, 2025</td><td>Independence Day — Stree Shakti naming + 1-yr free-bus anniversary</td><td class="bi-te">స్త్రీ శక్తి అధికారిక పేరు</td></tr>
</table>

<p><b>Why these matter:</b> The cluster of July–August 2025 events showcased the Naidu government's first-anniversary delivery sprint — every fortnight had at least one ribbon-cutting/announcement. The 5 Swachh awards (Jul 12) plus 4 HC permanent judges (Aug 4 &amp; 8) plus Handloom Museum (Aug 7) plus Stree Shakti naming (Aug 15) — all hit during the same 5-week window leading up to the 14-month mark.</p>
<p class="bi-te">జులై–ఆగస్టు 2025 — Naidu ప్రభుత్వం 1వ వార్షికోత్సవం delivery sprint. ప్రతి రెండు వారాలకు ఒక ప్రారంభం/ప్రకటన: 5 స్వచ్ఛ అవార్డులు, 4 HC జడ్జీలు, హస్తకళా మ్యూజియం, స్త్రీ శక్తి అధికారిక పేరు.</p>"""
    }
]

MCQ_DATA = [
    (0, 1,
     "PM మోదీ జనవరి 8, 2025న విశాఖపట్నంలో ప్రారంభించిన మొత్తం ప్రాజెక్టుల విలువ ఎంత?",
     "₹2 లక్షల కోట్లుకు పైగా", "₹1 లక్ష కోటి", "₹50,000 కోట్లు", "₹3 లక్షల కోట్లు",
     "a",
     "PM మోదీ జనవరి 8, 2025న విశాఖపట్నంలో ₹2 లక్షల కోట్లుకు పైగా విలువైన ప్రాజెక్టులు ప్రారంభించారు — NTPC హైడ్రోజన్ హబ్, రోడ్లు, రైల్వేలు."),
    (0, 1,
     "NTPC గ్రీన్ హైడ్రోజన్ హబ్ AP లో ఎక్కడ స్థాపిస్తున్నారు?",
     "పుడిమడక (విశాఖ)", "కాకినాడ", "అమరావతి", "తిరుపతి",
     "a",
     "NTPC గ్రీన్ హైడ్రోజన్ హబ్ విశాఖపట్నం జిల్లాలో పుడిమడక (Pudimadaka) వద్ద నెలకొల్పుతున్నారు."),
    (0, 2,
     "జనవరి 8, 2025 PM మోదీ విశాఖ పర్యటనలో NTPC గ్రీన్ హైడ్రోజన్ హబ్ పెట్టుబడి ఎంత?",
     "₹1,85,000 కోట్లు", "₹1,00,000 కోట్లు", "₹50,000 కోట్లు", "₹2,50,000 కోట్లు",
     "a",
     "NTPC గ్రీన్ హైడ్రోజన్ హబ్ పెట్టుబడి ₹1,85,000 కోట్లు. ఇది భారత్‌లోనే అతిపెద్ద గ్రీన్ హైడ్రోజన్ ప్రాజెక్ట్."),
    (0, 2,
     "జనవరి 8, 2025 పర్యటనలో PM మోదీ AP లో రోడ్డు ప్రాజెక్టులు ఎన్ని ప్రారంభించారు?",
     "10", "8", "5", "15",
     "a",
     "PM మోదీ జనవరి 8, 2025న 10 రోడ్డు ప్రాజెక్టులు (₹4,593 కోట్లు) మరియు 6 రైల్వే ప్రాజెక్టులు (₹6,028 కోట్లు) ప్రారంభించారు."),
    (0, 3,
     "జనవరి 8, 2025న PM మోదీ విశాఖలో ప్రారంభించిన రైల్వే ప్రాజెక్టుల విలువ ఎంత?",
     "₹6,028 కోట్లు", "₹4,593 కోట్లు", "₹2,500 కోట్లు", "₹8,000 కోట్లు",
     "a",
     "జనవరి 8, 2025న 6 రైల్వే ప్రాజెక్టులు (₹6,028 కోట్లు); 10 రోడ్డు ప్రాజెక్టులు (₹4,593 కోట్లు) ప్రారంభించారు."),
    (1, 1,
     "PM మోదీ అమరావతి పర్యటించి ₹58,000 కోట్ల ప్రాజెక్టులు ప్రారంభించిన తేదీ ఏది?",
     "మే 2, 2025", "మార్చి 15, 2025", "జనవరి 26, 2025", "ఆగస్టు 15, 2025",
     "a",
     "PM నరేంద్ర మోదీ మే 2, 2025న అమరావతి పర్యటించి ₹58,000 కోట్లు విలువైన ప్రాజెక్టులు ప్రారంభించారు."),
    (1, 2,
     "స్వర్ణ ఆంధ్ర@2047 విజన్ డాక్యుమెంట్ ఎప్పుడు విడుదల చేశారు?",
     "డిసెంబర్ 13, 2024", "మే 2, 2025", "జనవరి 1, 2025", "నవంబర్ 1, 2024",
     "a",
     "స్వర్ణ ఆంధ్ర@2047 విజన్ డాక్యుమెంట్ డిసెంబర్ 13, 2024న విడుదల చేశారు."),
    (1, 2,
     "స్వర్ణ ఆంధ్ర@2047 ప్రకారం 2047 కల్లా AP GDP లక్ష్యం ఎంత?",
     "₹308 లక్షల కోట్లు", "₹200 లక్షల కోట్లు", "₹100 లక్షల కోట్లు", "₹500 లక్షల కోట్లు",
     "a",
     "స్వర్ణ ఆంధ్ర@2047 లక్ష్యం: 2047 కల్లా AP GDP ₹308 లక్షల కోట్లు; వార్షిక వృద్ధి రేటు 15%."),
    (2, 1,
     "AP బడ్జెట్ 2025-26 ఎంత మొత్తానికి సమర్పించారు?",
     "₹3,22,359 కోట్లు", "₹2,88,125 కోట్లు", "₹2,52,000 కోట్లు", "₹3,85,000 కోట్లు",
     "a",
     "AP బడ్జెట్ 2025-26 మొత్తం ₹3,22,359 కోట్లు. ఆర్థిక మంత్రి పయ్యావుల కేశవ్ ఫిబ్రవరి 28, 2025న సమర్పించారు."),
    (2, 1,
     "AP బడ్జెట్ 2025-26 ఏ తేదీన సమర్పించారు?",
     "ఫిబ్రవరి 28, 2025", "ఫిబ్రవరి 20, 2025", "ఫిబ్రవరి 1, 2025", "మార్చి 1, 2025",
     "a",
     "AP బడ్జెట్ 2025-26 ఫిబ్రవరి 28, 2025న సమర్పించారు. బడ్జెట్ సెషన్ ఫిబ్రవరి 24-28, 2025."),
    (2, 2,
     "AP బడ్జెట్ 2025-26లో తల్లికి వందనం పథకానికి ఎంత కేటాయించారు?",
     "₹9,407 కోట్లు", "₹7,250 కోట్లు", "₹5,000 కోట్లు", "₹12,000 కోట్లు",
     "a",
     "AP బడ్జెట్ 2025-26లో తల్లికి వందనం పథకానికి ₹9,407 కోట్లు కేటాయించారు."),
    (2, 3,
     "AP బడ్జెట్ సెషన్ 2025 ఏ తేదీల మధ్య జరిగింది?",
     "ఫిబ్రవరి 24-28", "ఫిబ్రవరి 10-20", "జనవరి 20-31", "మార్చి 1-10",
     "a",
     "AP శాసనసభ బడ్జెట్ సెషన్ ఫిబ్రవరి 24-28, 2025 వరకు జరిగింది. ఆఖరి రోజు (ఫిబ్రవరి 28) బడ్జెట్ సమర్పించారు."),
    (3, 1,
     "విశాఖ స్టీల్ ప్లాంట్ (RINL) పునరుద్ధరణకు కేంద్రం ఎంత మంజూరు చేసింది?",
     "₹11,440 కోట్లు", "₹8,000 కోట్లు", "₹5,000 కోట్లు", "₹15,000 కోట్లు",
     "a",
     "రాష్ట్రీయ ఇస్పాత్ నిగమ్ (RINL) పునరుద్ధరణకు కేంద్రం ₹11,440 కోట్లు మంజూరు చేసింది."),
    (3, 3,
     "RINL లో పని చేసే ఉద్యోగుల సంఖ్య సుమారు ఎంత?",
     "20,000+", "10,000+", "5,000+", "50,000+",
     "a",
     "RINL లో 20,000+ మంది ఉద్యోగులు ఉన్నారు. ప్రైవేటైజేషన్ ప్రయత్నాల తర్వాత TDP-BJP ప్రభుత్వం పునరుద్ధరణ నిర్ణయం తీసుకుంది."),
    (4, 1,
     "పోలవరం జాతీయ ప్రాజెక్ట్ కి కేంద్ర బడ్జెట్ 2025-26లో ఎంత కేటాయించారు?",
     "₹5,936 కోట్లు", "₹3,500 కోట్లు", "₹2,000 కోట్లు", "₹8,000 కోట్లు",
     "a",
     "పోలవరం జాతీయ ప్రాజెక్ట్ కి కేంద్ర బడ్జెట్ 2025-26లో ₹5,936 కోట్లు కేటాయించారు."),
    (4, 3,
     "పోలవరం ప్రాజెక్ట్ ద్వారా ఎంత విస్తీర్ణంలో సాగు నీటిపారుదల వస్తుంది?",
     "3.27 లక్షల ఎకరాలు", "2 లక్షల ఎకరాలు", "1.5 లక్షల ఎకరాలు", "5 లక్షల ఎకరాలు",
     "a",
     "పోలవరం ప్రాజెక్ట్ ద్వారా 3.27 లక్షల ఎకరాల సాగుతో పాటు 36 TMC నీటి నిల్వ, తాగు నీరు, విద్యుత్ ఉత్పత్తి."),
    (5, 1,
     "అమరావతి క్వాంటం వ్యాలీ ఆలోచన ఏ సంవత్సరం మొదలైంది?",
     "ఆగస్టు 2025", "ఏప్రిల్ 2025", "జనవరి 2025", "జనవరి 2026",
     "a",
     "అమరావతి క్వాంటం వ్యాలీ ఆలోచన ఆగస్టు 2025లో మొదలైంది (Eenadu Pratibha verified). క్వాంటం కంప్యూటర్లు ఏప్రిల్ 14, 2026న అంకితం (Division 4 విషయం)."),
    (5, 1,
     "అమరావతి క్వాంటం వ్యాలీ వైశాల్యం ఎంత?",
     "50 ఎకరాలు", "25 ఎకరాలు", "10 ఎకరాలు", "100 ఎకరాలు",
     "a",
     "అమరావతి క్వాంటం వ్యాలీ వైశాల్యం 50 ఎకరాలు."),
    (5, 2,
     "అమరావతి క్వాంటం వ్యాలీలో క్వాంటం హార్డ్‌వేర్ సరఫరా చేస్తున్న ముఖ్య కంపెనీ ఏది?",
     "IBM (Quantum System Two — 156-qubit Heron)", "Google DeepMind", "Microsoft Quantum", "Infosys Quantum",
     "a",
     "Amaravati Quantum Valley లో హార్డ్‌వేర్ సరఫరాదారుడు = IBM (Quantum System Two with 156-qubit Heron processor). ముఖ్య IT భాగస్వామి = TCS. ఇతర భాగస్వాములు: L&T, CDAC, CDOT, IITs, 50+ సంస్థలు. Foundation Stone: Feb 7, 2026."),
    (5, 3,
     "అమరావతి క్వాంటం వ్యాలీ ఆలోచన ప్రారంభం నుండి క్వాంటం కంప్యూటర్ల అంకితం వరకు ఎంత సమయం పట్టింది?",
     "8 నెలలు", "5 నెలలు", "3 నెలలు", "12 నెలలు",
     "a",
     "ఆగస్టు 2025లో ఆలోచన మొదలై ఏప్రిల్ 2026న (8 నెలలు) అంకితం — ఎనిమిది నెలల రికార్డు సమయంలో రెండు క్వాంటం రిఫరెన్స్ ఫెసిలిటీస్."),
    (6, 1,
     "యోగాంధ్ర కార్యక్రమం విశాఖపట్నంలో ఏ తేదీన జరిగింది?",
     "జూన్ 21, 2025", "జూన్ 15, 2025", "జూన్ 5, 2025", "జూన్ 30, 2025",
     "a",
     "యోగాంధ్ర జూన్ 21, 2025న జరిగింది — అంతర్జాతీయ యోగా దినోత్సవం (International Yoga Day)."),
    (6, 1,
     "INS అర్నాల ఏ విభాగంలో నావల్ కమాండ్‌కు చెందినది?",
     "ఈస్టర్న్ నావల్ కమాండ్ (విశాఖ)", "నార్తర్న్ నావల్ కమాండ్ (కర్వార్)", "వెస్టర్న్ నావల్ కమాండ్ (ముంబయి)", "ఆండమాన్ నావల్ కమాండ్",
     "a",
     "INS అర్నాల విశాఖపట్నంలోని తూర్పు నావల్ కమాండ్ (Eastern Naval Command) లో ప్రవేశపెట్టారు."),
    (6, 2,
     "INS అర్నాల ఏ రకమైన యుద్ధనౌక?",
     "Shallow-Water ASW Corvette", "Destroyer", "Aircraft Carrier", "Submarine",
     "a",
     "INS అర్నాల భారత్ మొట్టమొదటి Shallow-Water Anti-Submarine Warfare (ASW) Corvette — నిర్మించిన మొదటి ఇలాంటి నౌక."),
    (6, 2,
     "INS అర్నాల పొడవు, బరువు ఎంత?",
     "50 మీ., 800 టన్నులు", "77 మీ., 1,490 టన్నులు", "65 మీ., 1,200 టన్నులు", "100 మీ., 3,000 టన్నులు",
     "b",
     "INS అర్నాల 77 మీటర్ల పొడవు, 1,490 టన్నుల బరువు. భారత్ మొదటి Shallow-Water ASW Corvette."),
    (6, 3,
     "యోగాంధ్ర కార్యక్రమంలో విశాఖ తీరంలో ఎంత దూరం వరకు యోగా నిర్వహించారు?",
     "5 కి.మీ.", "28 కి.మీ.", "15 కి.మీ.", "50 కి.మీ.",
     "b",
     "యోగాంధ్రలో విశాఖ 28 కి.మీ. తీర ప్రాంతంలో (RK Beach నుండి భీముణిపట్నం వరకు) 3.01 లక్షలు (3,00,105) మంది యోగా చేశారు — గిన్నిస్ రికార్డ్."),
    (7, 1,
     "అన్నదాత సుఖీభవ పథకం మొదటి విడత రైతులకు ఎంత అందించారు?",
     "₹2,000", "₹7,000", "₹5,000", "₹14,000",
     "b",
     "అన్నదాత సుఖీభవ మొదటి విడత మొత్తం ₹7,000. ఏడాదికి మొత్తం ₹20,000 (రాష్ట్రం ₹14,000 + PM KISAN ₹6,000). # VERIFY: per-installment state/center breakdown"),
    (7, 1,
     "ఆగస్టు 15, 2025న అధికారికంగా 'స్త్రీ శక్తి' పేర ప్రారంభించిన పథకం ఏది?",
     "అమ్మ ఒడి పథకం", "ఉచిత బస్సు ప్రయాణం", "జగనన్న అమ్మ వోడి", "ఆరోగ్య శ్రీ పథకం",
     "b",
     "ఉచిత బస్సు ప్రయాణం పథకానికి ఆగస్టు 15, 2025న (1వ వార్షికోత్సవం) అధికారిక పేరు 'స్త్రీ శక్తి' పెట్టారు."),
    (7, 2,
     "అన్నదాత సుఖీభవ పథకం ఏ జిల్లా, మండలంలో ప్రారంభించారు?",
     "కృష్ణా జిల్లా, పమర్రు మండలం", "ప్రకాశం జిల్లా, దార్సి మండలం", "పశ్చిమ గోదావరి జిల్లా, పాలకొల్లు", "గుంటూరు జిల్లా, తాడేపల్లి",
     "b",
     "అన్నదాత సుఖీభవ పథకం ప్రకాశం జిల్లా, దార్సి మండలం, తూర్పు వీరయ్యపాలెంలో ప్రారంభించారు (ఆగస్టు 2, 2025)."),
    (8, 1,
     "జాతీయ హస్తకళా మ్యూజియం (Handloom Museum) AP లో ఏ తేదీన ప్రారంభించారు?",
     "జులై 7, 2025", "ఆగస్టు 7, 2025", "జులై 19, 2025", "ఆగస్టు 15, 2025",
     "b",
     "జాతీయ హస్తకళా మ్యూజియం ఆగస్టు 7, 2025న (జాతీయ హస్తకళా దినోత్సవం) ప్రారంభించారు. అదే రోజు నేతన్న భరోసా ₹25,000 కూడా ప్రారంభం."),
    (8, 2,
     "BHISHMA — ఆరోగ్య మైత్రి క్యూబ్ లో ఎన్ని క్యూబ్‌లు ఉంటాయి?",
     "24", "72", "48", "96",
     "b",
     "BHISHMA (ఆరోగ్య మైత్రి క్యూబ్) లో 72 క్యూబ్‌లు ఉంటాయి. 10 నిమిషాల్లో డిప్లాయ్ చేయవచ్చు — అత్యవసర వైద్య సేవలకు."),
    (1, 1,
     "అమరావతి వరల్డ్-క్లాస్ రవాణా నెట్‌వర్క్ (320 కి.మీ.) మొత్తం వ్యయం ఎంత?",
     "₹12,000 కోట్లు", "₹17,400 కోట్లు", "₹20,400 కోట్లు", "₹58,000 కోట్లు",
     "b",
     "అమరావతిలో 320 కి.మీ. వరల్డ్-క్లాస్ రవాణా నెట్‌వర్క్ వ్యయం ₹17,400 కోట్లు. LP Scheme రహదారులు (1,281 కి.మీ.) వ్యయం ₹20,400 కోట్లు వేరే."),
    (1, 3,
     "PM మోదీ అమరావతి పర్యటనలో (మే 2, 2025) ప్రారంభించిన రక్షణ సంస్థ ఏది?",
     "HAL యూనిట్", "DRDO క్షిపణి పరీక్ష కేంద్రం", "ISRO ట్రాకింగ్ కేంద్రం", "BEL ఉత్పత్తి యూనిట్",
     "b",
     "PM మోదీ మే 2, 2025న అమరావతిలో DRDO క్షిపణి పరీక్ష కేంద్రం (Missile Testing Centre) ప్రారంభించారు."),
    (2, 1,
     "AP బడ్జెట్ 2025-26 సమర్పించిన ఆర్థిక మంత్రి ఎవరు?",
     "నారా లోకేష్", "పయ్యావుల కేశవ్", "కె.అచ్చెన్నాయుడు", "నాదెండ్ల మనోహర్",
     "b",
     "ఆర్థిక మంత్రి పయ్యావుల కేశవ్ (TDP) AP బడ్జెట్ 2025-26 ఫిబ్రవరి 28, 2025న సమర్పించారు."),
    (3, 1,
     "RINL — Rashtriya Ispat Nigam Limited విశాఖపట్నంలో ఏ ప్రాంతంలో ఉంది?",
     "దువ్వాడ", "గాంధీనగర్", "భీమునిపట్నం", "అనకాపల్లి",
     "b",
     "RINL విశాఖపట్నం గాంధీనగర్ ప్రాంతంలో ఉంది. భారత్‌లో ఒకే సముద్రతీర సమీపంలో ఉన్న అతిపెద్ద ఉక్కు కర్మాగారం."),
    (3, 2,
     "RINL లో 3 Blast Furnaces పూర్తి స్థాయిలో ఎప్పటికి పని చేయడం మొదలుపెట్టాయి?",
     "జనవరి 2025", "మార్చి 2025", "జూన్ 2025", "ఆగస్టు 2025",
     "d",
     "RINL లో 2 Blast Furnaces 2025 ప్రారంభంలో పునరారంభం అయ్యాయి; 3 Blast Furnaces ఆగస్టు 2025 కల్లా పూర్తి స్థాయి ఉత్పత్తి మొదలుపెట్టాయి."),
    (4, 1,
     "పోలవరం ప్రాజెక్ట్ ఏ నదిపై నిర్మిస్తున్నారు?",
     "కృష్ణ నది", "గోదావరి నది", "పెన్నా నది", "తుంగభద్ర నది",
     "b",
     "పోలవరం ప్రాజెక్ట్ గోదావరి నదిపై నిర్మిస్తున్నారు. జాతీయ ప్రాజెక్ట్ హోదా 2010లో వచ్చింది."),
    (4, 2,
     "పోలవరం మొత్తం పెండింగ్ బ్యాలెన్స్ గ్రాంట్ ఎంత?",
     "₹5,936 కోట్లు", "₹8,000 కోట్లు", "₹10,000 కోట్లు", "₹12,157.53 కోట్లు",
     "d",
     "పోలవరం మొత్తం పెండింగ్ బ్యాలెన్స్ గ్రాంట్ ₹12,157.53 కోట్లు. 2025-26 బడ్జెట్ కేటాయింపు: ₹5,936 కోట్లు."),
    # AUDIT D7 (Batch G): Removed MCQ — "Amaravati 1S / Amaravati 1Q" product naming was
    # unsourced/fabricated. AP Quantum Valley uses IBM Quantum System Two with the Heron R2
    # processor (156 qubits, superconducting). See div4 sec 0 for the canonical fact.
    (6, 1,
     "యోగాంధ్రలో విశాఖ తీరంలో ఎంత మంది పాల్గొని గిన్నిస్ రికార్డ్ సాధించారు?",
     "1 లక్ష మంది", "2 లక్షల మంది", "3.01 లక్షలు (3,00,105)", "5 లక్షల మంది",
     "c",
     "యోగాంధ్రలో విశాఖ 28 కి.మీ. తీరంలో 3.01 లక్షలు (3,00,105) మంది పాల్గొని గిన్నిస్ వరల్డ్ రికార్డ్ సాధించారు. లక్ష్యం 5 లక్షలుగా నిర్ణయించారు కానీ నిజమైన రికార్డు 3,00,105 మంది."),
    (7, 1,
     "తల్లికి వందనం పథకం అధికారికంగా ప్రారంభించిన తేదీ ఏది?",
     "మే 2, 2025", "జూన్ 12, 2025", "ఆగస్టు 2, 2025", "ఆగస్టు 15, 2025",
     "b",
     "తల్లికి వందనం పథకం జూన్ 12, 2025న ప్రారంభమైంది — TDP-BJP-JSP ప్రభుత్వ మొదటి వార్షికోత్సవం."),
    (7, 2,
     "అన్నదాత సుఖీభవ ద్వారా రైతులకు ఏడాదికి మొత్తం ఎంత అందుతుంది?",
     "₹6,000", "₹10,000", "₹14,000", "₹20,000",
     "d",
     "అన్నదాత సుఖీభవ + PM KISAN కలిపి ఏడాదికి ₹20,000 (రాష్ట్రం ₹14,000 + కేంద్రం PM KISAN ₹6,000)."),
    (7, 3,
     "స్త్రీ శక్తి పేరుతో ఉచిత బస్సు ప్రయాణం పథకం మొదటిసారి ఏ తేదీన ప్రారంభమైంది?",
     "జూన్ 12, 2024", "ఆగస్టు 15, 2024", "జనవరి 1, 2025", "ఆగస్టు 15, 2025",
     "b",
     "ఉచిత బస్సు ప్రయాణం (స్త్రీ శక్తి) ఆగస్టు 15, 2024న మొదలైంది. 'స్త్రీ శక్తి' అనే అధికారిక పేరు ఆగస్టు 15, 2025న (1వ వార్షికోత్సవంపై) ఇచ్చారు."),
    (8, 1,
     "BHISHMA (ఆరోగ్య మైత్రి క్యూబ్) AP లో ఎక్కడ స్థాపించారు?",
     "NTR ట్రస్ట్ హాస్పిటల్, విజయవాడ", "AIIMS మంగళగిరి", "కింగ్స్ జార్జ్ హాస్పిటల్, విశాఖ", "పీఎంఆర్‌ఐ, హైదరాబాద్",
     "b",
     "BHISHMA (ఆరోగ్య మైత్రి క్యూబ్) 3 యూనిట్లు జులై 19, 2025న AIIMS మంగళగిరిలో స్థాపించారు."),
    (8, 2,
     "స్వచ్ఛ సర్వేక్షణ్ అవార్డులు 2024 AP కి ఏ తేదీన ప్రకటించారు?",
     "జూన్ 12, 2025", "జులై 12, 2025", "ఆగస్టు 7, 2025", "ఆగస్టు 15, 2025",
     "b",
     "స్వచ్ఛ సర్వేక్షణ్ అవార్డులు 2024 జులై 12, 2025న ప్రకటించారు. AP నగరాలు 5 అవార్డులు సాధించాయి."),
    (8, 2,
     "నేతన్న భరోసా పథకంలో చేనేత కార్మికులకు ఏడాదికి ఎంత ఆర్థిక సహాయం అందిస్తున్నారు?",
     "₹10,000", "₹15,000", "₹20,000", "₹25,000",
     "d",
     "నేతన్న భరోసా పథకంలో చేనేత కార్మికులకు ఏడాదికి ₹25,000 ఆర్థిక సహాయం అందిస్తున్నారు. ఆగస్టు 7, 2025న ప్రారంభం."),
]


def _seed_ap_ca_div3_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 3."""
    ph = '%s' if USE_POSTGRES else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT 'AP_Current_Affairs', subtopic TEXT DEFAULT '',
            chapter_num INTEGER NOT NULL, chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '', pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if USE_POSTGRES: conn.commit()
    except Exception: pass
    import json as _json
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (3, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (3, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division3', 3,
         '2025 జనవరి–ఆగస్టు ముఖ్య సంఘటనలు',
         '2025 January–August Major Events',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div3 notes seeded!'}
def _seed_ap_ca_div3_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for Division 3."""
    ph = "%s" if USE_POSTGRES else "?"

    note_row = db_exec(
        conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
        ("AP_Current_Affairs", 3)
    ).fetchone()
    if not note_row:
        return

    note_id = row_to_dict(note_row)['id']

    # Always delete-then-reinsert so seed-file changes are reflected.
    # (Previous count-check used `cur.fetchone()[0]` which raises KeyError on Postgres dict-rows.)
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    for (sec_idx, diff, q_te, a, b, c, d, ans, exp_te) in MCQ_DATA:
        db_exec(conn, f"""
            INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})
        """, (note_id, sec_idx, diff, q_te, a, b, c, d, ans, exp_te))

    if hasattr(conn, "commit"):
        conn.commit()
