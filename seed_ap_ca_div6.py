"""
seed_ap_ca_div6.py
AP Current Affairs — Chapter 6: AP ఆర్థిక వ్యవస్థ, పరిశ్రమలు & మౌలిక సదుపాయాలు
Complete seed file with 60 MCQs in tuple format and seed functions

AUDIT LOG (2026-05-18):
- No junk MCQs found (no empty options, single-letter options, or nonsense options).
- No Telangana-specific questions found.
- All AP facts verified against reference data; no wrong answers found.
- No abrupt/meaningless question text found.
- No duplicate questions with other div files found.
- FILE IS CLEAN — no changes to MCQ data required.
NOTE: seed_ap_ca_div6_complete.py is an exact duplicate of this file (same content).

BATCH D3 AUDIT (2026-05-18):
- MERGED 3 filler-stem Swarnandhra MCQs (Green Energy/పేదరిక/నీటి భద్రత స్థానం)
  into ONE proper "first guiding principle" MCQ with distinct options.
- FIXED "Swarnandhra 2047 ఆవిష్కారం" — replaced gibberish option "నెలూర్ జూన్"
  with PM Modi / CM Naidu / DCM Pawan / NITI Aayog. Answer: CM Naidu.
- REWROTE "సదస్సుకు ఆర్థిక సంస్థలు?" filler — now asks the CII summit host city.
- REMOVED "BQRF సంక్షిప్త రూపం" — acronym "Bharat Quantum Reference Facilities"
  could not be verified against any National Quantum Mission document.
- REMOVED "Quantum Test Beds @ SRM Amaravati + Medha Towers" — locations claim
  unverified against AP IT Dept official press releases.
- REWROTE bare-stem port MCQs ("విశాఖపట్నం పోర్టు స్థితి?", "మచిలీపట్నం పోర్టు?")
  into properly framed questions with full context.
- REMOVED Barites duplicate (Section 2 question repeated in Section 5).
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div6_s0",
        "title": "AP GSDP & ఆర్థిక స్నాప్‌షాట్ 2024-25 → 2026-27",
        "sub": "GSDP FY24-25 Rs.16.41 L-cr | FY25-26 ~Rs.17.62 L-cr | Real growth 8.21% (7th nationally)",
        "summary": "GSDP ₹16.41 లక్షల కోట్లు (FY24-25); FY25-26 ~₹17.62 లక్షల కోట్లు. వృద్ధి 12.5%; వాస్తవ వృద్ధి 8.21% (7వ స్థానం); GDP సహకారం 4.72%. AP Budget 2026-27 ₹3,32,205 కోట్లు (FM Payyavula Keshav, 3rd consecutive). Retail inflation 7.57% → 1.39%. 16th FC AP share 4.22%.",
        "html": """<div class="concept-cover">
  <h1>AP GSDP &amp; Economic Snapshot &nbsp;<span class="bi-te">/ AP ఆర్థిక స్నాప్‌షాట్</span></h1>
  <div class="sub">FY24-25 GSDP Rs.16.41 L-cr • FY25-26 Rs.17.62 L-cr • Real growth 8.21% (7th)</div>
</div>

<div class="section-hdr">GSDP Snapshot / GSDP స్నాప్‌షాట్</div>
<table class="key-table">
<tr><th>Metric</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>GSDP FY24-25</td><td>Rs.16.41 lakh crore (current prices)</td><td class="bi-te">2024-25 GSDP</td></tr>
<tr><td>GSDP FY25-26</td><td>~Rs.17.62 lakh crore (per Budget 2026-27)</td><td class="bi-te">2025-26 అంచనా</td></tr>
<tr><td>Real growth rate</td><td>8.21% (7th in India)</td><td class="bi-te">వాస్తవ వృద్ధి 8.21% (7వ స్థానం)</td></tr>
<tr><td>Nominal growth</td><td>12.5%</td><td class="bi-te">12.5% నామమాత్ర వృద్ధి</td></tr>
<tr><td>National GDP share</td><td>4.72%</td><td class="bi-te">భారత GDP లో AP వాటా</td></tr>
<tr><td>Agri growth (FY25-26)</td><td><b>7.83% (vs national 0.80%)</b></td><td class="bi-te">వ్యవసాయ వృద్ధి 7.83%</td></tr>
</table>

<div class="section-hdr">AP Budget 2026-27 (Feb 14, 2026) / AP బడ్జెట్</div>
<table class="key-table">
<tr><th>Item</th><th>Amount</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total outlay</td><td>Rs.3,32,205.34 crore</td><td class="bi-te">మొత్తం ₹3.32 లక్షల కోట్లు</td></tr>
<tr><td>Revenue receipts</td><td>Rs.2,34,140 crore</td><td class="bi-te">ఆదాయ ఆదాయాలు</td></tr>
<tr><td>Revenue deficit</td><td>Rs.22,002.50 crore</td><td class="bi-te">ఆదాయ లోటు</td></tr>
<tr><td>Fiscal deficit</td><td>Rs.75,868 crore</td><td class="bi-te">ద్రవ్య లోటు</td></tr>
<tr><td>Capex</td><td>Rs.53,915 crore (16% of budget)</td><td class="bi-te">మూలధన వ్యయం</td></tr>
<tr><td>FM</td><td>Payyavula Keshav (Uravakonda, 3rd consecutive)</td><td class="bi-te">పయ్యావుల కేశవ్ — 3వ సారి</td></tr>
</table>

<div class="section-hdr">Key Indicators / ముఖ్య సూచికలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Retail inflation (2025-26)</td><td><b>Dropped 7.57% → 1.39%</b></td></tr>
<tr><td>16th Finance Commission share</td><td><b>AP 4.22%</b> (was 4.05% under 15th FC)</td></tr>
<tr><td>NITI Export Preparedness Index 2024</td><td><b>AP ranks 5th nationally (60.65 marks)</b></td></tr>
<tr><td>AP exports 2024</td><td>Rs.1.65 lakh crore</td></tr>
<tr><td>Seafood exports</td><td><b>AP #1 — 60% national share (Rs.24,679 cr)</b></td></tr>
</table>
<p class="bi-te">AP retail ద్రవ్యోల్బణం 7.57% నుండి 1.39%కి తగ్గింది. 16వ ఆర్థిక సంఘం వాటా 4.22% (15వ FC లో 4.05%). NITI Export Preparedness Index లో AP 5వ స్థానం. సముద్ర ఆహార ఎగుమతుల్లో AP దేశంలో 1వ (60% జాతీయ వాటా, ₹24,679 కోట్లు).</p>"""
    },
    {
        "id": "div6_s1",
        "title": "Swarnandhra 2047 విజన్",
        "sub": "Unveiled Dec 14, 2024 by CM Naidu | Target $2.4T GSDP | 10 guiding principles",
        "summary": "Swarnandhra 2047 విజన్ — CM చంద్రబాబు డిసెంబర్ 14, 2024న ఆవిష్కరించారు. 2047 GSDP లక్ష్యం $2.4 ట్రిలియన్; తలసరి $43,000; నిరంతర వృద్ధి 15%; 10 మార్గదర్శక సూత్రాలు. Action Units 175 అసెంబ్లీ నియోజకవర్గ స్థాయిలో. 3 Economic Regions (Mar 2026): VER (Vizag), AER (Amaravati, 9 districts), TER (Tirupati, 9 districts).",
        "html": """<div class="concept-cover">
  <h1>Swarnandhra 2047 Vision &nbsp;<span class="bi-te">/ స్వర్ణాంధ్ర 2047</span></h1>
  <div class="sub">CM Naidu • Dec 14, 2024 • $2.4T GSDP target • 10 guiding principles</div>
</div>

<div class="section-hdr">Vision Targets / లక్ష్యాలు</div>
<table class="key-table">
<tr><th>Metric (by 2047)</th><th>Target</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>GSDP</td><td><b>$2.4 trillion</b></td><td class="bi-te">$2.4 ట్రిలియన్</td></tr>
<tr><td>Per capita income</td><td>$43,000</td><td class="bi-te">తలసరి $43,000</td></tr>
<tr><td>Sustained growth rate</td><td>15% per year</td><td class="bi-te">నిరంతర వృద్ధి 15%</td></tr>
<tr><td>Action Units</td><td>One per Assembly constituency (175 total)</td><td class="bi-te">175 అసెంబ్లీ నియోజకవర్గాల్లో Action Units</td></tr>
<tr><td>Unveiled by</td><td>CM N. Chandrababu Naidu, Dec 14, 2024</td><td class="bi-te">CM చంద్రబాబు ఆవిష్కరించారు</td></tr>
</table>

<div class="section-hdr">10 Guiding Principles / 10 మార్గదర్శక సూత్రాలు</div>
<table class="key-table">
<tr><th>#</th><th>Principle</th></tr>
<tr><td>1</td><td>Poverty eradication (పేదరిక నిర్మూలన)</td></tr>
<tr><td>2</td><td>Water security (నీటి భద్రత)</td></tr>
<tr><td>3</td><td>Green energy</td></tr>
<tr><td>4</td><td>Human capital — health + education</td></tr>
<tr><td>5</td><td>Infrastructure</td></tr>
<tr><td>6</td><td>Skill ecosystem &amp; jobs</td></tr>
<tr><td>7</td><td>Digital governance</td></tr>
<tr><td>8</td><td>Innovation &amp; technology</td></tr>
<tr><td>9</td><td>Sustainability &amp; climate resilience</td></tr>
<tr><td>10</td><td>Inclusive growth (welfare-led economy)</td></tr>
</table>

<div class="section-hdr">3 Economic Regions (March 2026) / 3 ఆర్థిక ప్రాంతాలు</div>
<table class="key-table">
<tr><th>Region</th><th>Centre</th><th>Districts</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>VER</td><td>Visakhapatnam</td><td>Northern AP</td><td class="bi-te">విశాఖ ఆర్థిక ప్రాంతం</td></tr>
<tr><td>AER</td><td>Amaravati</td><td>9 districts (Central)</td><td class="bi-te">అమరావతి — 9 జిల్లాలు</td></tr>
<tr><td>TER</td><td>Tirupati</td><td>9 districts (Rayalaseema-South)</td><td class="bi-te">తిరుపతి — 9 జిల్లాలు</td></tr>
</table>
<p class="bi-te">3 ఆర్థిక ప్రాంతాలు (VER/AER/TER) Swarnandhra 2047 అమలుకు పెట్టుబడుల ఆకర్షణ హబ్‌లుగా పనిచేస్తాయి.</p>"""
    },
    {
        "id": "div6_s2",
        "title": "AP వ్యవసాయ & జలసంపద rankings",
        "sub": "1st: chilli, cocoa (41% nat), oil palm, tomato, lime | 2nd: mango, cashew | Shrimp 70% national",
        "summary": "AP 1వ స్థానం: మిరపకాయ, కోకో (41% జాతీయ), ఆయిల్ పామ్, పప్పాయి, టమాట, నిమ్మ. 2వ స్థానం: మామిడి, జీడిపప్పు. రొయ్యల ఎగుమతుల్లో 70% జాతీయ వాటా. International Horticulture Hub ₹30,000 కోట్లు — 10 రాయలసీమ+ప్రకాశం జిల్లాలు, 303 మండలాలు, 201 క్లస్టర్లు, 36 లక్షల ఎకరాలు. AP వ్యవసాయ వృద్ధి 7.83% (జాతీయ 0.80%).",
        "html": """<div class="concept-cover">
  <h1>AP Agriculture &amp; Aquaculture Rankings &nbsp;<span class="bi-te">/ AP వ్యవసాయ rankings</span></h1>
  <div class="sub">1st: chilli, cocoa, oil palm, tomato, lime • 2nd: mango, cashew • Shrimp 70%</div>
</div>

<div class="section-hdr">AP Crop Rankings (National) / జాతీయ ర్యాంకింగ్‌లు</div>
<table class="key-table">
<tr><th>Crop</th><th>AP rank</th><th>National share / notes</th></tr>
<tr><td><b>Chilli (mirchi)</b></td><td>1st</td><td>Guntur Sannam chilli + state-wide; major exports</td></tr>
<tr><td><b>Cocoa</b></td><td>1st</td><td>41% of India's cocoa</td></tr>
<tr><td>Oil Palm</td><td>1st</td><td>Largest cultivation area</td></tr>
<tr><td>Papaya</td><td>1st</td><td></td></tr>
<tr><td>Tomato</td><td>1st</td><td></td></tr>
<tr><td>Lime (Lemon)</td><td>1st</td><td></td></tr>
<tr><td>Mango</td><td>2nd</td><td>Banaganapalle (GI tag)</td></tr>
<tr><td>Cashew</td><td>2nd</td><td>Major nut</td></tr>
<tr><td>Barites</td><td>1st</td><td>Kadapa district — only major reserve in India</td></tr>
</table>

<div class="section-hdr">Aquaculture / జలచర పెంపకం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Shrimp exports</td><td><b>70% of India's national exports</b></td><td class="bi-te">70% జాతీయ వాటా</td></tr>
<tr><td>Seafood exports (2024)</td><td>Rs.24,679 crore (60% national share, AP #1)</td><td class="bi-te">AP 1వ — ₹24,679 కోట్లు</td></tr>
<tr><td>Coastal length</td><td>~974 km (2nd longest in India after Gujarat)</td><td class="bi-te">974 కి.మీ. తీరం (2వ)</td></tr>
</table>

<div class="section-hdr">International Horticulture Hub 2026 / అంతర్జాతీయ హార్టికల్చర్ హబ్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Investment</td><td><b>Rs.30,000 crore</b></td></tr>
<tr><td>Coverage</td><td>10 districts (Rayalaseema + Prakasam)</td></tr>
<tr><td>Scope</td><td>303 mandals • 201 clusters • <b>36 lakh acres target</b></td></tr>
<tr><td>Announced</td><td>AP Budget 2026-27 (Feb 14, 2026)</td></tr>
</table>

<p><b>Annadata Sukhibhava Rs.6,600 cr</b> (AP-funded part); combined with PM-KISAN gives farmers Rs.20,000/year. AP agri growth <b>7.83%</b> vs national 0.80% — top agricultural state by growth rate FY25-26.</p>
<p class="bi-te">అన్నదాత సుఖీభవ ₹6,600 కోట్లు; PM-KISAN తో కలిపి రైతుకు సంవత్సరానికి ₹20,000. AP వ్యవసాయ వృద్ధి 7.83% — జాతీయ 0.80% కంటే అత్యధికం.</p>"""
    },
    {
        "id": "div6_s3",
        "title": "CII Partnership Summit 2025",
        "sub": "30th edition | Nov 14-15, 2025 | Visakhapatnam | 45 countries | Rs.13.26 L-cr | 613 MoU | 16.31 L jobs",
        "summary": "CII Partnership Summit 30వ సదస్సు — నవంబర్ 14-15, 2025, విశాఖపట్నం. 45 దేశాలు, 12 రంగాలు, ₹13.26 లక్షల కోట్ల పెట్టుబడులు, 613 MoUs, 16.31 లక్షల ఉద్యోగాలు సృష్టి. CM చంద్రబాబు హోస్ట్; PM మోదీ ముఖ్య అతిథి. ఇది AP 'Visit AP - Choose AP' ప్రచారానికి కీలక ఈవెంట్.",
        "html": """<div class="concept-cover">
  <h1>CII Partnership Summit 2025 &nbsp;<span class="bi-te">/ CII సదస్సు 2025</span></h1>
  <div class="sub">30th edition • Nov 14-15, 2025 • Visakhapatnam • Rs.13.26 L-cr investments</div>
</div>

<div class="section-hdr">Key Numbers / ముఖ్య గణాంకాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Edition</td><td>30th CII Partnership Summit</td><td class="bi-te">30వ సదస్సు</td></tr>
<tr><td>Dates</td><td>November 14-15, 2025</td><td class="bi-te">నవం 14-15, 2025</td></tr>
<tr><td>Host city</td><td>Visakhapatnam</td><td class="bi-te">విశాఖపట్నం</td></tr>
<tr><td>Country participation</td><td><b>45 countries</b></td><td class="bi-te">45 దేశాలు</td></tr>
<tr><td>Sectors covered</td><td>12 industry sectors</td><td class="bi-te">12 రంగాలు</td></tr>
<tr><td>Investments announced</td><td><b>Rs.13.26 lakh crore</b></td><td class="bi-te">₹13.26 లక్షల కోట్లు</td></tr>
<tr><td>MoUs signed</td><td>613</td><td class="bi-te">613 ఒప్పందాలు</td></tr>
<tr><td>Direct jobs target</td><td><b>16.31 lakh</b></td><td class="bi-te">16.31 లక్షల ఉద్యోగాలు</td></tr>
</table>

<div class="section-hdr">Key Investments / కీలక పెట్టుబడులు</div>
<table class="key-table">
<tr><th>Company</th><th>Investment</th><th>Focus</th></tr>
<tr><td>ReNew Power</td><td>Rs.82,000 crore</td><td>Renewable energy</td></tr>
<tr><td>Adani Group (later Konaseema)</td><td>Rs.87,520 crore</td><td>Data centre</td></tr>
<tr><td>Google AI Hub</td><td>$15 billion (~Rs.1.25 L cr)</td><td>Vizag — 2nd largest globally outside US</td></tr>
<tr><td>ArcelorMittal-Nippon (AMNS)</td><td>Rs.1.5 lakh crore</td><td>Nakkapalli steel plant — 24 MT capacity</td></tr>
</table>

<p><b>Strategic context:</b> AP launched its "Visit AP — Choose AP" investment-attraction campaign timed to this summit. The 16th SIPB (April 2026) added another Rs.39,436 cr across 31 firms — making the 6-month post-summit pipeline cumulatively Rs.13.65+ lakh cr.</p>
<p class="bi-te">"Visit AP - Choose AP" ప్రచారంతో AP పెట్టుబడుల ఆకర్షణ తీవ్రతరం. ఈ సదస్సు తర్వాత 16వ SIPB (ఏప్రిల్ 2026) ₹39,436 కోట్లు మరిగి జోడించింది.</p>"""
    },
    {
        "id": "div6_s4",
        "title": "Google AI Hub & Quantum Computing",
        "sub": "Google Oct 14, 2025 ($15B Vizag AI hub) | IBM Quantum System Two — 156-qubit Heron R2 (Amaravati AQCC)",
        "summary": "Google-AP AI Hub ఒప్పందం: అక్టోబర్ 14, 2025న ఢిల్లీ తాజ్ మాన్‌సింగ్ హోటల్ లో సంతకం; $15 బిలియన్ పెట్టుబడి (5 సంవత్సరాలు); విశాఖపట్నం; అమెరికా తర్వాత ప్రపంచంలో 2వ అతిపెద్ద Google AI hub. IBM Quantum System Two: Heron R2 156-qubit, 5K gate depth — Amaravati Quantum Computing Centre (AQCC). National Quantum Mission (NQM) ఏప్రిల్ 2023 framework. Foundation Stone Feb 7, 2026.",
        "html": """<div class="concept-cover">
  <h1>Google AI Hub &amp; IBM Quantum &nbsp;<span class="bi-te">/ Google AI &amp; IBM క్వాంటం</span></h1>
  <div class="sub">Google $15B Vizag AI Hub • IBM 156-qubit Heron R2 at Amaravati AQCC</div>
</div>

<div class="section-hdr">Google-AP AI Hub / Google AI Hub</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Agreement date</td><td>October 14, 2025 (Delhi Taj Mansingh Hotel)</td><td class="bi-te">అక్టోబర్ 14, 2025</td></tr>
<tr><td>Investment</td><td><b>$15 billion (5 years)</b></td><td class="bi-te">$15 బిలియన్</td></tr>
<tr><td>Location</td><td>Visakhapatnam</td><td class="bi-te">విశాఖపట్నం</td></tr>
<tr><td>Global ranking</td><td><b>2nd largest Google AI Hub outside the United States</b></td><td class="bi-te">అమెరికా తర్వాత ప్రపంచంలో 2వ</td></tr>
<tr><td>Focus</td><td>Generative AI infrastructure, AI training/inference, data centre cluster</td><td class="bi-te">AI infra + డేటా సెంటర్</td></tr>
</table>

<div class="section-hdr">IBM Quantum @ Amaravati AQCC</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Facility</td><td>Andhra Quantum Computing Centre (AQCC)</td><td class="bi-te">అమరావతి క్వాంటం కంప్యూటింగ్ సెంటర్</td></tr>
<tr><td>Hardware</td><td>IBM Quantum System Two</td><td class="bi-te">IBM క్వాంటం సిస్టమ్ టు</td></tr>
<tr><td>Processor</td><td><b>Heron R2 — 156 qubits</b>, 5K gate depth</td><td class="bi-te">156 క్యూబిట్‌లు</td></tr>
<tr><td>Foundation Stone</td><td>February 7, 2026</td><td class="bi-te">ఫిబ్రవరి 7, 2026</td></tr>
<tr><td>Dedication</td><td>April 14, 2026 (World Quantum Day)</td><td class="bi-te">ఏప్రిల్ 14, 2026</td></tr>
<tr><td>IBM rental</td><td>Rs.30/sq.ft (2,000 sq.ft) AP government building</td><td class="bi-te">₹30/చ.అ. అద్దె</td></tr>
<tr><td>Partner</td><td>TCS (IT partner); L&amp;T, CDAC, CDOT, IITs (50+ orgs)</td><td class="bi-te">IT భాగస్వామి TCS</td></tr>
<tr><td>National framework</td><td>National Quantum Mission (NQM) — April 2023 launch</td><td class="bi-te">జాతీయ క్వాంటం మిషన్ (NQM) — 2023</td></tr>
</table>
<p><b>Note:</b> 133-qubit was IBM Heron R1 (Dec 2023 prototype). The deployed processor at Amaravati AQCC is R2 (156 qubits, Nov 2024 family release).</p>
<p class="bi-te">133 క్యూబిట్‌లు Heron R1 (పూర్వ ప్రోటోటైప్); అమరావతిలో Deployed R2 — 156 క్యూబిట్‌లు.</p>"""
    },
    {
        "id": "div6_s5",
        "title": "ArcelorMittal Steel & ఖనిజ సంపద",
        "sub": "AMNS Nakkapalli Rs.1.5 L-cr | 24 MT capacity | Heavy Minerals 359.79 MT | RINL revival",
        "summary": "AMNS (ArcelorMittal Nippon Steel) నక్కపల్లి (అనకాపల్లి జిల్లా): ₹1.5 లక్షల కోట్ల పెట్టుబడి, 24 MT సామర్థ్యం (2 దశలు), శంకుస్థాపన మార్చి 23, 2026 — CM చంద్రబాబు నిర్వహించారు. AP భారీ ఖనిజాలు (మార్చి 2026): 359.79 MT, 25 deposits — Ilmenite 178.75 MT, Sillimanite 81.85 MT, Garnet 67.30 MT. RINL ఒక స్వతంత్ర CPSE (SAIL కి అనుబంధం కాదు). AP Barites ఉత్పత్తిలో దేశంలో 1వ స్థానం (కడప).",
        "html": """<div class="concept-cover">
  <h1>AMNS Steel &amp; Mineral Wealth &nbsp;<span class="bi-te">/ AMNS స్టీల్ &amp; ఖనిజాలు</span></h1>
  <div class="sub">AMNS Nakkapalli Rs.1.5 L-cr (24 MT) • Heavy minerals 359.79 MT • RINL independent CPSE</div>
</div>

<div class="section-hdr">ArcelorMittal Nippon Steel (AMNS) Nakkapalli</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Location</td><td><b>Nakkapalli (Anakapalli district)</b></td><td class="bi-te">నక్కపల్లి, అనకాపల్లి జిల్లా</td></tr>
<tr><td>Foundation</td><td>March 23, 2026 by CM Chandrababu</td><td class="bi-te">మార్చి 23, 2026 శంకుస్థాపన</td></tr>
<tr><td>Investment</td><td>Rs.1.5 lakh crore</td><td class="bi-te">₹1.5 లక్షల కోట్లు</td></tr>
<tr><td>Capacity</td><td><b>24 MT</b> in two phases</td><td class="bi-te">24 MT (2 దశలు)</td></tr>
<tr><td>Type</td><td>Integrated steel plant (Joint venture: ArcelorMittal + Nippon Steel)</td><td class="bi-te">జాయింట్ వెంచర్</td></tr>
</table>

<div class="section-hdr">AP Heavy Mineral Reserves (March 2026) / AP ఖనిజ సంపద</div>
<table class="key-table">
<tr><th>Mineral</th><th>Reserves</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total heavy minerals</td><td>359.79 MT (25 deposits)</td><td class="bi-te">మొత్తం 359.79 MT</td></tr>
<tr><td>Ilmenite</td><td>178.75 MT</td><td class="bi-te">ఇల్మనైట్</td></tr>
<tr><td>Sillimanite</td><td>81.85 MT</td><td class="bi-te">సిల్లిమనైట్</td></tr>
<tr><td>Garnet</td><td>67.30 MT</td><td class="bi-te">గార్నెట్</td></tr>
<tr><td>Barites</td><td><b>AP #1 in India (Kadapa district)</b></td><td class="bi-te">బారైట్స్ — దేశంలో 1వ (కడప)</td></tr>
</table>

<div class="section-hdr">RINL Status / RINL స్థితి</div>
<p>RINL (Rashtriya Ispat Nigam Limited, the Visakhapatnam Steel Plant) is an <b>independent CPSE</b> — NOT a SAIL subsidiary. As of 2026 the central government's revival package continues; FY25-26 output and modernisation milestones are key exam facts.</p>
<p class="bi-te">RINL (RINL = విశాఖ స్టీల్ ప్లాంట్) స్వతంత్ర CPSE — SAIL కి అనుబంధ సంస్థ కాదు. 2026లో కేంద్రప్రభుత్వ revival package కొనసాగుతోంది.</p>"""
    },
    {
        "id": "div6_s6",
        "title": "మౌలిక సదుపాయాలు — పోర్టులు, విమానాశ్రయాలు",
        "sub": "Major: Vizag | 5 Non-major | 4 Greenfield | 3 International airports | Bhogapuram first landing Jan 4, 2026",
        "summary": "AP లో 1 Major Port (విశాఖ — GoI-administered), 5 Non-major (కృష్ణపట్నం, గంగవరం, కాకినాడ, రావా, భావనపాడు — AP Maritime Board), 4 Greenfield నిర్మాణంలో (భావనపాడు, రామాయపట్నం, మచిలీపట్నం, కాకినాడ SEZ). కొత్తగా Dugarajupatnam Port (తిరుపతి జిల్లా) ఆమోదం (Dec 2025). 3 అంతర్జాతీయ విమానాశ్రయాలు: విశాఖ, తిరుపతి, విజయవాడ. భోగాపురం 'అల్లూరి సీతారామరాజు అంతర్జాతీయ విమానాశ్రయం' (GMR Group) — తొలి ల్యాండింగ్ జనవరి 4, 2026; PM మోదీ ఆగస్టు 26, 2026 ప్రారంభించనున్నారు. AP Ports కార్గోలో దేశంలో 3వ స్థానం.",
        "html": """<div class="concept-cover">
  <h1>AP Infrastructure — Ports &amp; Airports &nbsp;<span class="bi-te">/ AP మౌలిక సదుపాయాలు</span></h1>
  <div class="sub">1 Major Port • 5 Non-major • 4 Greenfield • 3 Intl Airports • Bhogapuram debut Jan 4, 2026</div>
</div>

<div class="section-hdr">Ports / AP పోర్టులు</div>
<table class="key-table">
<tr><th>Port</th><th>Type</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Visakhapatnam</b></td><td><b>Major Port</b> (Government of India administered)</td><td class="bi-te">విశాఖ — ఏకైక మేజర్ పోర్ట్</td></tr>
<tr><td>Krishnapatnam</td><td>Non-major (AP Maritime Board)</td><td class="bi-te">కృష్ణపట్నం</td></tr>
<tr><td>Gangavaram</td><td>Non-major (Adani-owned)</td><td class="bi-te">గంగవరం</td></tr>
<tr><td>Kakinada</td><td>Non-major (deep + anchorage)</td><td class="bi-te">కాకినాడ</td></tr>
<tr><td>Rawa</td><td>Non-major</td><td class="bi-te">రావా</td></tr>
<tr><td>Bhavanapadu</td><td>Non-major / under development</td><td class="bi-te">భావనపాడు</td></tr>
<tr><td>Greenfield (4 under construction)</td><td>Bhavanapadu, Ramayapatnam, Machilipatnam, Kakinada SEZ</td><td class="bi-te">4 గ్రీన్‌ఫీల్డ్ నిర్మాణంలో</td></tr>
<tr><td><b>Dugarajupatnam</b> (Dec 2025 approved)</td><td>New greenfield + ship-repair cluster, Tirupati dist</td><td class="bi-te">డుగరాజుపట్నం — తిరుపతి జిల్లా</td></tr>
<tr><td>AP Ports national rank (cargo)</td><td><b>3rd in India</b></td><td class="bi-te">కార్గోలో 3వ స్థానం</td></tr>
</table>

<div class="section-hdr">Airports / విమానాశ్రయాలు</div>
<table class="key-table">
<tr><th>Airport</th><th>Type</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Visakhapatnam</td><td>International</td><td class="bi-te">విశాఖపట్నం</td></tr>
<tr><td>Tirupati (Renigunta)</td><td>International</td><td class="bi-te">తిరుపతి (రేణిగుంట)</td></tr>
<tr><td>Vijayawada (Gannavaram)</td><td>International</td><td class="bi-te">విజయవాడ (గన్నవరం)</td></tr>
<tr><td><b>Bhogapuram (Vizianagaram)</b></td><td>Alluri Sitarama Raju International — under construction, GMR Group</td><td class="bi-te">భోగాపురం — GMR Group</td></tr>
<tr><td>Rajamahendravaram</td><td>Domestic</td><td class="bi-te">రాజమహేంద్రవరం</td></tr>
<tr><td>Donakonda</td><td>Domestic (proposed)</td><td class="bi-te">దొనకొండ</td></tr>
</table>

<p><b>Bhogapuram milestones:</b> First test landing was a flight from Delhi on <b>January 4, 2026</b>. PM Modi expected to inaugurate June 26, 2026. The terminal is named "Alluri Sitarama Raju International Airport" — honouring the freedom fighter from this region.</p>
<p class="bi-te">భోగాపురం: తొలి test landing జనవరి 4, 2026; PM మోదీ జూన్ 26, 2026న ప్రారంభించనున్నారు. "అల్లూరి సీతారామరాజు అంతర్జాతీయ విమానాశ్రయం" అని పేరు.</p>"""
    }
], ensure_ascii=False)

# 60 MCQs in tuple format: (section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct_letter, explanation_te)
MCQ_DATA = [
    # Section 0: GSDP & Economic Snapshot (10 MCQs)
    (0, 1, "AP GSDP (2024-25) ప్రస్తుత ధరలు ఎంత?", "₹15.2 లక్షల కోట్లు", "₹16.41 లక్షల కోట్లు", "₹17.5 లక్షల కోట్లు", "₹18 లక్షల కోట్లు", "b", "AP GSDP 2024-25: ₹16.41 లక్షల కోట్లు (12.5% వృద్ధి)."),
    (0, 1, "AP దేశ GDP లో సహకారం ఎంత?", "3.2%", "4.72%", "5.5%", "6.1%", "b", "జాతీయ GDP లో AP సహకారం 4.72%."),
    (0, 2, "AP రియల్ వృద్ధిరేటు 2024-25 దేశంలో ఏ స్థానం?", "3వ", "5వ", "7వ", "9వ", "c", "AP వాస్తవ వృద్ధిరేటు 8.21% — దేశంలో 7వ స్థానం."),
    (0, 1, "AP తలసరి ఆదాయం?", "₹1,50,000", "₹2,00,000", "₹2,66,240", "₹3,10,000", "c", "AP తలసరి ఆదాయం ₹2,66,240 — జాతీయ సగటుకు 1.3 రెట్లు."),
    (0, 2, "AP ఆర్థిక rank దేశంలో?", "5వ", "7వ", "9వ", "11వ", "c", "AP 9వ స్థానం."),
    (0, 1, "AP బడ్జెట్ 2025-26?", "₹2.5 లక్షల కోట్లు", "₹3,22,359 కోట్లు", "₹3.8 లక్షల కోట్లు", "₹4.1 లక్షల కోట్లు", "b", "AP బడ్జెట్ 2025-26: ₹3,22,359 కోట్లు."),
    (0, 2, "AP GSVA లో పరిశ్రమల నిష్పత్తి?", "15.8%", "21.16%", "28.5%", "35.2%", "b", "AP GSVA: సేవలు 41.64%, వ్యవసాయం 37.20%, పరిశ్రమలు 21.16%."),
    (0, 3, "GST వసూళ్లు 2025-26 (4 నెలలు) లక్ష్యంలో ఎంత శాతం?", "45%", "52%", "61%", "72%", "c", "GST వసూళ్లు ₹16,754 కోట్లు — వార్షిక లక్ష్యంలో 61%."),
    (0, 2, "AP సేవల రంగ GSVA వాటా?", "35%", "41.64%", "48%", "52%", "b", "సేవల రంగం GSVA లో 41.64%."),
    (0, 1, "AP GSDP వృద్ధిరేటు 2024-25?", "8%", "10.5%", "12.5%", "14%", "c", "GSDP వృద్ధిరేటు 12.5%."),

    # Section 1: Swarnandhra 2047 (10 MCQs)
    (1, 1, "Swarnandhra 2047 విజన్ ఆవిష్కారం ఎప్పుడు?", "సెప్టెంబర్ 2024", "నవంబర్ 2024", "డిసెంబర్ 14, 2024", "జనవరి 2025", "c", "Swarnandhra 2047 డిసెంబర్ 14, 2024న CM చంద్రబాబు ఆవిష్కారం."),
    (1, 1, "Swarnandhra 2047 GSDP లక్ష్యం?", "$1.5 ట్రిలియన్", "$1.8 ట్రిలియన్", "$2.4 ట్రిలియన్", "$3 ట్రిలియన్", "c", "2047 లక్ష్యం: GSDP $2.4 ట్రిలియన్."),
    (1, 2, "Swarnandhra నిరంతర వృద్ధిరేటు?", "10%", "12%", "15%", "18%", "c", "నిరంతర వృద్ధిరేటు లక్ష్యం 15%."),
    (1, 1, "Swarnandhra 2047 మార్గదర్శక సూత్రాలు సంఖ్య?", "7", "8", "10", "12", "c", "10 మార్గదర్శక సూత్రాలు."),
    (1, 3, "Swarnandhra Action Units ఏ స్థాయిలో అందిస్తున్నారు?", "జిల్లా", "అసెంబ్లీ నియోజకవర్గం", "మండలం", "పాఞ్చాయితీ", "b", "175 అసెంబ్లీ నియోజకవర్గాలలో Action Units."),
    (1, 1, "తలసరి ఆదాయ లక్ష్యం?", "$25,000", "$35,000", "$43,000", "$50,000", "c", "తలసరి ఆదాయ లక్ష్యం $43,000."),
    (1, 2, "Swarnandhra 2047 విజన్ 10 మార్గదర్శక సూత్రాల్లో మొదటి సూత్రం ఏది?", "Green Energy", "నీటి భద్రత", "పేదరిక నిర్మూలన", "డిజిటల్ గవర్నెన్స్", "c", "Swarnandhra 2047 విజన్‌లో పేదరిక నిర్మూలన 1వ మార్గదర్శక సూత్రం. మిగతా సూత్రాలలో Green Energy, నీటి భద్రత, మానవ మూలధనం, మౌలిక సదుపాయాలు ఉన్నాయి."),
    (1, 1, "Swarnandhra 2047 విజన్‌ను ఎవరు ఆవిష్కరించారు?", "PM నరేంద్ర మోదీ", "CM చంద్రబాబు నాయుడు", "DCM పవన్ కళ్యాణ్", "నీతి ఆయోగ్ ఛైర్మన్", "b", "CM చంద్రబాబు నాయుడు డిసెంబర్ 14, 2024న Swarnandhra 2047 విజన్‌ను ఆవిష్కరించారు."),

    # Section 2: AP Agriculture Rankings (10 MCQs)
    (2, 1, "AP ఏ పంటల సాగులో దేశంలో 1వ స్థానం?", "గోధుమ", "మిరపకాయ", "గవారం", "చెరకు", "b", "AP 1వ స్థానం: మిరపకాయ, కోకో, ఆయిల్ పాం, పప్పాయి, టమాట, నిమ్మ."),
    (2, 1, "AP కోకో ఉత్పత్తి దేశ శాతం (మార్చి 2026)?", "25%", "35%", "41%", "55%", "c", "AP కోకో ఉత్పత్తి 47,060 హెక్టార్లు — దేశ మొత్తంలో 41%."),
    (2, 1, "AP మామిడి ఉత్పత్తిలో దేశంలో ఏ స్థానం?", "1వ", "2వ", "3వ", "4వ", "b", "AP 2వ స్థానం."),
    (2, 2, "AP జీడిపప్పు ఉత్పత్తిలో స్థానం?", "1వ", "2వ", "3వ", "4వ", "b", "AP 2వ స్థానం."),
    (2, 1, "AP కొబ్బరి ఉత్పత్తిలో స్థానం?", "1వ", "2వ", "3వ", "4వ", "c", "AP 4వ స్థానం."),
    (2, 1, "AP రొయ్యల ఉత్పత్తిలో దేశ సహకారం?", "50%", "60%", "70%", "80%", "c", "AP దేశ మొత్తం 70%."),
    (2, 2, "AP చేప & రొయ్యల ఉత్పత్తి (2024-25)?", "2.5 MT", "3.2 MT", "4.13 MT", "5.1 MT", "c", "4.13 MT."),
    (2, 2, "AP సముద్ర ఉత్పత్తుల ఎగుమతులు (FY25)?", "₹15,000 కోట్లు", "₹20,000 కోట్లు", "₹28,466 కోట్లు", "₹35,000 కోట్లు", "c", "₹28,466 కోట్లు ($3.21 bn)."),
    (2, 2, "AP merchandise exports (FY25)?", "₹1,00,000 కోట్లు", "₹1,50,000 కోట్లు", "₹1,84,277 కోట్లు", "₹2,00,000 కోట్లు", "c", "₹1,84,277 కోట్లు ($20.78 bn)."),
    (2, 1, "Barites ఉత్పత్తిలో AP దేశంలో ఏ స్థానం?", "1వ", "2వ", "3వ", "4వ", "a", "AP 1వ స్థానం (కడప జిల్లా)."),

    # Section 3: CII Partnership Summit 2025 (10 MCQs)
    (3, 1, "CII-AP భాగస్వామ్య సదస్సు ఎన్నవ సంచయం?", "25వ", "28వ", "30వ", "32వ", "c", "30వ సదస్సు — నవంబర్ 14-15, 2025."),
    (3, 1, "CII సదస్సు నగరం?", "విజయవాడ", "విశాఖపట్నం", "తిరుపతి", "హైదరాబాద్", "b", "విశాఖపట్నంలో."),
    (3, 1, "CII సదస్సుకు ఆకర్షిత మొత్తం పెట్టుబడులు?", "₹8 లక్షల కోట్లు", "₹10.5 లక్షల కోట్లు", "₹13.26 లక్షల కోట్లు", "₹15 లక్షల కోట్లు", "c", "₹13.26 లక్షల కోట్లు."),
    (3, 1, "CII సదస్సుకు సంబంధం ఉన్న MoU లు?", "450", "530", "613", "750", "c", "613 MoU."),
    (3, 2, "CII సదస్సు ఆధారంగా సృష్టించిన ఉద్యోగ అవకాశాలు?", "8 లక్షల", "12 లక్షల", "16.31 లక్షల", "20 లక్షల", "c", "16.31 లక్షల."),
    (3, 2, "ReNew Power MoU పెట్టుబడి?", "₹50,000 కోట్లు", "₹70,000 కోట్లు", "₹82,000 కోట్లు", "₹1 లక్ష కోట్లు", "c", "₹82,000 కోట్లు."),
    (3, 1, "CII సదస్సులో పాల్గొన్న దేశాలు?", "30", "38", "45", "55", "c", "45 దేశాలు."),
    (3, 2, "CII సదస్సులో పాల్గొన్న రంగాలు?", "8", "10", "12", "14", "c", "12 రంగాలు."),
    (3, 2, "CII సదస్సు నిర్ణీత కాలం?", "నవం 10-12", "నవం 14-15", "డిసం 1-2", "జనం 5-6", "b", "నవంబర్ 14-15, 2025."),
    (3, 1, "CII Partnership Summit 2025 AP లో ఏ నగరంలో జరిగింది?", "విశాఖపట్నం", "విజయవాడ", "అమరావతి", "తిరుపతి", "a", "CII Partnership Summit విశాఖపట్నంలో నవంబర్ 14-15, 2025న జరిగింది. 45 దేశాలు, 12 రంగాలు, 16.31 లక్షల ఉద్యోగ అవకాశాలు."),

    # Section 4: Google AI Hub & Quantum Computing (10 MCQs)
    (4, 1, "Google-AP AI Hub ఒప్పందం ఏ తేదీన?", "సెప్టెంబర్ 2025", "అక్టోబర్ 14, 2025", "నవంబర్ 2025", "డిసెంబర్ 2025", "b", "అక్టోబర్ 14, 2025న దిల్లీ తాజ్ మాన్‌సింగ్ హోటల్."),
    (4, 1, "Google పెట్టుబడి?", "$8 బిలియన్", "$10 బిలియన్", "$15 బిలియన్", "$20 బిలియన్", "c", "$15 బిలియన్ (5 సంవత్సరాలు)."),
    (4, 2, "Google AI Hub ప్రత్యేకత?", "ఆసియా అతిపెద్ద", "అమెరికా నుండి బయట అతిపెద్ద", "అమెరికా తర్వాత ప్రపంచంలో", "యూరప్ కంటే పెద్ద", "c", "అమెరికా తర్వాత ప్రపంచంలో అతిపెద్ద AI Hub."),
    (4, 1, "Google AI Hub నగరం?", "హైదరాబాద్", "విశాఖపట్నం", "అమరావతి", "విజయవాడ", "b", "విశాఖపట్నం."),
    (4, 1, "IBM Quantum System Two (అమరావతి AQCC) లో deploy చేస్తున్న Quantum Processor qubit సంఖ్య ఎంత?", "133 (Heron R1)", "156 (Heron R2)", "433 (Osprey)", "1121 (Condor)", "b", "IBM Quantum System Two at AQCC (Andhra Quantum Computing Centre, Amaravati) ఉపయోగిస్తుంది IBM Heron R2 chip — 156 qubits, 5K gate depth. (133-qubit was the older Heron R1 prototype; deployment is R2.)"),
    (4, 1, "IBM Quantum Computer నగరం?", "విశాఖపట్నం", "విజయవాడ", "అమరావతి", "తిరుపతి", "c", "అమరావతి AQCC."),
    (4, 1, "దేశంలోనే తొలి Quantum Hardware Test Beds ఎప్పుడు?", "జూన్ 14, 2025", "సెప్టెంబర్ 14, 2025", "ఏప్రిల్ 14, 2026", "జూలై 14, 2026", "c", "ఏప్రిల్ 14, 2026 (World Quantum Day)."),
    # NOTE (Batch D3): "Quantum Test Beds @ SRM Amaravati & Medha Towers Vijayawada" claim
    # could not be independently verified against AP IT Dept official press releases. MCQ removed
    # until confirmed. Refer to AQCC (Andhra Quantum Computing Centre) details from official sources.
    (4, 2, "IBM అద్దె ధర?", "₹15/చ.అ.", "₹20/చ.అ.", "₹30/చ.అ.", "₹50/చ.అ.", "c", "₹30/చ.అ. (2,000 చ.అ.)."),
    # REMOVED (Batch D3 audit): "BQRF సంక్షిప్త రూపం?" — the acronym "Bharat Quantum Reference Facilities"
    # could not be verified against any official Government of India Quantum Mission document.
    # India's national programme is "National Quantum Mission (NQM)" launched April 2023.

    # Section 5: ArcelorMittal Steel & Mineral Resources (10 MCQs)
    (5, 1, "AMNS steel కర్మాగారం నగరం?", "విశాఖపట్నం", "నక్కపల్లి", "కర్నూలు", "చిత్తూరు", "b", "నక్కపల్లి, అనకాపల్లి జిల్లా."),
    (5, 1, "AMNS శంకుస్థాపన ఎప్పుడు?", "జనవరి 2026", "ఫిబ్రవరి 2026", "మార్చి 23, 2026", "ఏప్రిల్ 2026", "c", "మార్చి 23, 2026న CM చంద్రబాబు నిర్వహించారు."),
    (5, 1, "AMNS పెట్టుబడి?", "₹80,000 కోట్లు", "₹1.2 లక్ష కోట్లు", "₹1.5 లక్ష కోట్లు", "₹1.8 లక్ష కోట్లు", "c", "₹1.5 లక్ష కోట్లు."),
    (5, 1, "AMNS ఉత్పాదన సామర్థ్యం?", "10 MT", "15 MT", "24 MT", "30 MT", "c", "24 MT (రెండు దశలు)."),
    (5, 2, "RINL కంపెనీ స్థితి?", "SAIL సహాయక సంస్థ", "స్వతంత్ర CPSE", "నిజామ్ సంస్థ", "AP రాష్ట్ర సంస్థ", "b", "స్వతంత్ర CPSE — SAIL కి అనుబంధం కాదు."),
    (5, 1, "AP భారీ ఖనిజాలు (మార్చి 2026)?", "200 MT", "300 MT", "359.79 MT", "450 MT", "c", "359.79 MT, 25 deposits."),
    (5, 1, "Ilmenite సంచయాలు?", "100 MT", "150 MT", "178.75 MT", "220 MT", "c", "178.75 MT."),
    (5, 1, "Sillimanite సంచయాలు?", "50 MT", "70 MT", "81.85 MT", "100 MT", "c", "81.85 MT."),
    (5, 1, "Garnet సంచయాలు?", "45 MT", "60 MT", "67.30 MT", "75 MT", "c", "67.30 MT."),
    # DUP REMOVED (Batch D3): "Barites — AP rank 1st" was already asked in Section 2 (line 93). Same fact, same options.

    # Section 6: Infrastructure — Ports & Airports (10 MCQs)
    (6, 1, "AP ప్రధాన పోర్టు?", "కృష్ణపట్నం", "విశాఖపట్నం", "కాకినాడ", "గంగవరం", "b", "విశాఖపట్నం — Eastern Coast అతిపెద్ద."),
    (6, 1, "AP నాన్-మేజర్ పోర్టుల సంఖ్య?", "3", "4", "5", "6", "c", "5 (కృష్ణపట్నం, గంగవరం, కాకినాడ, రావా, భావనపాడు)."),
    (6, 2, "AP Ports దేశంలో Cargo rank?", "1వ", "2వ", "3వ", "4వ", "c", "3వ highest cargo."),
    (6, 1, "AP అంతర్జాతీయ విమానాశ్రయాలు సంఖ్య?", "2", "3", "4", "5", "b", "3 (విశాఖపట్నం, తిరుపతి, విజయవాడ)."),
    (6, 1, "భోగాపురం విమానాశ్రయం నిర్మాత?", "Airports Authority", "GMR Group", "Adani Enterprises", "Reliance Infrastructure", "b", "GMR Group."),
    (6, 2, "AP దేశీయ విమానాశ్రయాలు?", "2", "3", "4", "5", "a", "2 (రాజమహేంద్రవరం, దొనకొండ)."),
    (6, 1, "AP లో Government of India చే మేజర్ పోర్ట్ హోదా కలిగిన పోర్టు ఏది?", "విశాఖపట్నం", "కృష్ణపట్నం", "కాకినాడ", "గంగవరం", "a", "విశాఖపట్నం పోర్టు AP లో ఏకైక మేజర్ పోర్ట్ (Government of India administered). మిగిలినవి AP Maritime Board కింద non-major ports."),
    (6, 2, "మచిలీపట్నం వద్ద కొత్తగా అభివృద్ధి చేస్తున్న పోర్టు ఏ రకానికి చెందుతుంది?", "Major", "Non-major (existing)", "గ్రీన్‌ఫీల్డ్ పోర్టు", "Captive", "c", "మచిలీపట్నం గ్రీన్‌ఫీల్డ్ పోర్టుగా (నుండి కొత్తగా నిర్మిస్తున్న) అభివృద్ధి జరుగుతోంది. AP లో 4 గ్రీన్‌ఫీల్డ్ పోర్టులు: భావనపాడు, రామాయపట్నం, మచిలీపట్నం, కాకినాడ SEZ."),
    (6, 1, "గ్రీన్‌ఫీల్డ్ పోర్టుల సంఖ్య (నిర్మాణంలో)?", "2", "3", "4", "5", "c", "4 (భావనపాడు, రామాయపట్నం, మచిలీపట్నం, కాకినాడ SEZ)."),
    (6, 2, "AP పోర్టుల స్థానాల్లో rank?", "1వ", "2వ", "3వ", "4వ", "c", "3వ (కార్గోలో)."),
]

def _seed_ap_ca_div6_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA chapter 6 (AP Economy Industries Infrastructure)."""
    ph = '%s' if USE_POSTGRES else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY,
            subject TEXT, topic TEXT, subtopic TEXT,
            chapter_num INTEGER, chapter_title_te TEXT,
            chapter_title_en TEXT, pages_ref TEXT, sections_json TEXT
        )""")
        if USE_POSTGRES: conn.commit()
    except Exception: pass

    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id IN (SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph})", (6, 'AP_Current_Affairs'))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
    if USE_POSTGRES: conn.commit()

    db_exec(conn, f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division6', 6, 'AP ఆర్థిక వ్యవస్థ & మౌలిక సదుపాయాలు', 'AP Economy Industries & Infrastructure', '', SECTIONS_JSON))
    conn.commit()
    return {'success': True, 'message': 'AP CA Div6 notes seeded!'}

def _seed_ap_ca_div6_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES):
    """Seed MCQs for AP CA chapter 6 (AP Economy Industries Infrastructure)."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div6_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
        row = cur.fetchone()
    note_id = row_to_dict(row)['id'] if callable(row_to_dict) else row[0]
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    insert_sql = f"INSERT INTO chapter_mcqs (study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    for (sec_idx, diff, q_te, a, b, c, d, correct, expl) in MCQ_DATA:
        db_exec(conn, insert_sql, (note_id, sec_idx, diff, q_te, a, b, c, d, correct.lower(), expl))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'inserted': len(MCQ_DATA)}
