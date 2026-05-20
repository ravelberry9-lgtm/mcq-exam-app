#!/usr/bin/env python3
"""
seed_concept_notes_natl_2026.py
Rich bilingual (English + Telugu) concept notes for National Current Affairs 2026 MCQs.
Topics: Budget, RD, Padma Awards, ISRO, Defence, Foreign Policy, Sports, Census, Const Amendment, etc.
~26 concept notes covering IDs 31001-31120 + 31301-31380 (Batch H+PDF 2026 + chunk-1/2/3 enrichment).
Tag prefix: 'natl_2026_'
"""
import os, sys

DATABASE_URL = os.environ.get('DATABASE_URL', '')
USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    conn = psycopg2.connect(DATABASE_URL)
else:
    import sqlite3
    DB = os.path.join(os.path.dirname(__file__), 'database.db')
    conn = sqlite3.connect(DB)

NOTES = []  # list of (tag, label_en, label_te, html)

# ═══════════════════════════════════════════════════════════════════
#  1. UNION BUDGET 2026-27 & 16th FINANCE COMMISSION
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_budget_finance',
              'Union Budget 2026-27 & 16th Finance Commission',
              'కేంద్ర బడ్జెట్ 2026-27 & 16వ ఆర్థిక సంఘం', """
<div class="concept-cover">
  <h1>Union Budget 2026-27 &amp; 16th Finance Commission &nbsp;<span class="bi-te">/ కేంద్ర బడ్జెట్ 2026-27 &amp; 16వ ఆర్థిక సంఘం</span></h1>
  <div class="sub">February 1, 2026 • Sitharaman's 9th Budget • Total Rs.58,47,315 cr</div>
</div>

<div class="section-hdr">Union Budget — Key Numbers / కేంద్ర బడ్జెట్ ముఖ్య అంకెలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Presented</td><td>February 1, 2026 by FM Nirmala Sitharaman</td><td class="bi-te">ఫిబ్రవరి 1, 2026 — నిర్మలా సీతారామన్</td></tr>
<tr><td>Record</td><td>Her <b>9th</b> consecutive Union Budget</td><td class="bi-te">వరుసగా 9వ బడ్జెట్</td></tr>
<tr><td>Total outlay</td><td>Rs.58,47,315 crore</td><td class="bi-te">మొత్తం వ్యయం రూ.58,47,315 కోట్లు</td></tr>
<tr><td>Capital expenditure</td><td>Rs.12.22 lakh crore</td><td class="bi-te">మూలధన వ్యయం రూ.12.22 లక్షల కోట్లు</td></tr>
<tr><td>Fiscal deficit</td><td>4.3% of GDP</td><td class="bi-te">ద్రవ్యలోటు GDP లో 4.3%</td></tr>
<tr><td>GDP growth target</td><td>7%</td><td class="bi-te">GDP వృద్ధి లక్ష్యం 7%</td></tr>
</table>

<div class="section-hdr">Sectoral Allocations / రంగాల వారీ కేటాయింపులు</div>
<table class="key-table">
<tr><th>Sector</th><th>Allocation</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Defence</td><td>Rs.7.85 lakh crore (+15% YoY) — highest</td><td class="bi-te">రక్షణ రూ.7.85 ల.కో. (+15%)</td></tr>
<tr><td>Roads & Highways</td><td>Rs.3.09 lakh crore</td><td class="bi-te">రోడ్లు & హైవేలు రూ.3.09 ల.కో.</td></tr>
<tr><td>Railways</td><td>Rs.2.78 lakh crore</td><td class="bi-te">రైల్వేలు రూ.2.78 ల.కో.</td></tr>
<tr><td>Agriculture</td><td>Rs.1.63 lakh crore</td><td class="bi-te">వ్యవసాయం రూ.1.63 ల.కో.</td></tr>
<tr><td>Education</td><td>Rs.1.39 lakh crore</td><td class="bi-te">విద్య రూ.1.39 ల.కో.</td></tr>
<tr><td>Health</td><td>Rs.1.07 lakh crore</td><td class="bi-te">ఆరోగ్యం రూ.1.07 ల.కో.</td></tr>
<tr><td>ISRO</td><td>Rs.13,705 crore</td><td class="bi-te">ఇస్రో రూ.13,705 కో.</td></tr>
</table>

<div class="section-hdr">Major Schemes Announced / ప్రధాన పథకాలు</div>
<p><b>KCC (Kisan Credit Card)</b> limit hiked from Rs.3 lakh to <b>Rs.5 lakh</b>. <b>"Bharat-Vistar"</b> AI agriculture tool launched with Rs.150 cr. <b>"PM Dhan Dhanya Krishi Yojana"</b> targets 100 low-yield districts covering <b>1.7 crore farmers</b>. <b>"Pulse Self-Sufficiency Mission"</b> — 6-year mission for pulse self-reliance. <b>7 High-Speed Rail (HSR) corridors</b> covering ~4,000 km announced.</p>
<p class="bi-te">కిసాన్ క్రెడిట్ కార్డ్ పరిమితి రూ.3 ల. నుండి రూ.5 లక్షలకు పెంపు. "భారత్-విస్తార్" AI వ్యవసాయ సాధనం రూ.150 కోట్లు. PM ధన్ ధాన్య కృషి యోజన — 100 తక్కువ దిగుబడి జిల్లాలు, 1.7 కోట్ల రైతులు. పప్పు స్వయం-సమృద్ధి మిషన్ 6 సం. 7 హై-స్పీడ్ రైలు కారిడార్లు ~4,000 కి.మీ.</p>

<div class="section-hdr">16th Finance Commission / 16వ ఆర్థిక సంఘం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Chairman</td><td>Arvind Panagariya</td><td class="bi-te">ఛైర్మన్: అరవింద్ పనగారియా</td></tr>
<tr><td>States' share</td><td><b>41%</b> of divisible pool (same as 15th FC)</td><td class="bi-te">రాష్ట్రాల వాటా 41%</td></tr>
<tr><td>Andhra Pradesh share</td><td><b>4.22%</b> (UP from 4.05% in 15th FC)</td><td class="bi-te">ఆంధ్రప్రదేశ్ వాటా 4.22% (15వ FC లో 4.05% నుండి పెరిగింది)</td></tr>
<tr><td>Telangana share</td><td>2.17%</td><td class="bi-te">తెలంగాణ వాటా 2.17%</td></tr>
<tr><td>Urbanization Premium</td><td>Rs.10,000 crore — new component</td><td class="bi-te">పట్టణీకరణ ప్రీమియం రూ.10,000 కోట్లు — కొత్త అంశం</td></tr>
<tr><td>Total grants</td><td>Rs.9.47 lakh crore</td><td class="bi-te">మొత్తం గ్రాంట్లు రూ.9.47 ల.కో.</td></tr>
<tr><td>Local bodies grant</td><td>Rs.7.91 lakh crore</td><td class="bi-te">స్థానిక సంస్థల గ్రాంట్ రూ.7.91 ల.కో.</td></tr>
</table>
<p><b>Economic Significance:</b> The Union Budget 2026-27 represents India's continued fiscal consolidation with a 4.3% fiscal deficit target, maintaining sustainability while pursuing 7% GDP growth — crucial for competing with global economies. The increased defence allocation (+15% YoY) reflects India's strategic autonomy doctrine and border security priorities, especially after regional tensions. <b>Policy Implementation:</b> The PM Dhan Dhanya Krishi Yojana addresses persistent agricultural productivity gaps in 100 identified low-yield districts, covering 1.7 crore farmers through tech-enabled interventions. KCC expansion (Rs.3L to Rs.5L) increases farmer liquidity access. The Pulse Self-Sufficiency Mission directly responds to India's import dependency (55% of pulse consumption imported) — a critical food security and farmer income issue. <b>India's Position:</b> The 16th Finance Commission's Urbanization Premium (Rs.10,000 cr new component) signals structural fiscal federalism reform, acknowledging India's rapid urbanization (40.8% urban population by 2026 estimates) and divergent fiscal capacities between states. AP and TS gains in divisible pool allocations reflect their economic contribution and developmental needs.</p>
<p class="bi-te"><b>ఆర్థిక ప్రాముఖ్యత:</b> 2026-27 బడ్జెట్ భారత్ కేంద్రీకృత ద్రవ్యలోట నియంత్రణ (4.3% GDP)ను సూచిస్తుంది, 7% GDP వృద్ధి లక్ష్యం సక్రియం. రక్షణ బడ్జెట్ పెంపు (+15%) వ్యూహాత్మక స్వయంత్ర సిద్ధాంతం &amp; సరిహద్దు సంरक्षణ. <b>నిబంధన అమలు:</b> PM ధన్ ధాన్య 100 జిల్లాలలో 1.7 కోట్ల రైతులకు సాంకేతిక-ఆధారిత జీవక-సాక్ష్యం. KCC సম్প్రসారణ రైతుల ద్రవ్యత. పప్పు స్వయం-సమృద్ధి భారత దిగుమతి ఆధారపడటం (55%) పరిష్కారం. <b>భారత్ గ్లోబల్ సంస్థితి:</b> 16వ FC పట్టణీకరణ ప్రీమియం — నిర్మాణాత్మక కర లేఖనం సంస్కరణ. AP/TS రాష్ట్ర వాటా పెంపు ఆర్థిక సహకారం &amp; అభివృద్ధి బోధ ప్రతిబింబం.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  2. 77th REPUBLIC DAY & GALLANTRY AWARDS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_republic_day',
              '77th Republic Day & Gallantry Awards 2026',
              '77వ గణతంత్ర దినోత్సవం & శౌర్య పురస్కారాలు 2026', """
<div class="concept-cover">
  <h1>77th Republic Day &amp; Gallantry Awards 2026 &nbsp;<span class="bi-te">/ 77వ గణతంత్ర దినోత్సవం</span></h1>
  <div class="sub">January 26, 2026 • Kartavya Path • Theme: 150 Years of Vande Mataram</div>
</div>

<div class="section-hdr">Republic Day Parade — Key Facts / గణతంత్ర దినోత్సవ కవాతు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td>January 26, 2026 — 77th Republic Day</td><td class="bi-te">జనవరి 26, 2026 — 77వ గణతంత్ర దినోత్సవం</td></tr>
<tr><td>Venue</td><td>Kartavya Path, New Delhi</td><td class="bi-te">కర్తవ్య పథ్, న్యూఢిల్లీ</td></tr>
<tr><td>Theme</td><td>"150 Years of Vande Mataram"</td><td class="bi-te">"వందే మాతరం 150 సం."</td></tr>
<tr><td>Chief Guests</td><td><b>Two:</b> António Costa (EU Council President) + Ursula von der Leyen (European Commission President)</td><td class="bi-te">ఇద్దరు అతిథులు: ఆంటోనియో కోస్టా + ఉర్సులా వాన్ డెర్ లేయెన్</td></tr>
<tr><td>Historic</td><td><b>First EU military contingent</b> ever to march outside Europe</td><td class="bi-te">యూరప్ వెలుపల EU సైనిక పటాలం మొదటిసారి కవాతు</td></tr>
<tr><td>Reviewed by</td><td>President Droupadi Murmu</td><td class="bi-te">రాష్ట్రపతి ద్రౌపదీ ముర్ము</td></tr>
</table>

<div class="section-hdr">Defence Highlights on Display / రక్షణ ప్రదర్శనలు</div>
<p><b>Bhairav Light Commando Battalion</b> (raised October 2025) made its parade debut. The <b>Shaktiban regiment</b>, <b>Suryastra rocket system</b>, and <b>LR-AShM hypersonic missile</b> were showcased alongside <b>robotic dogs</b> — signalling the Army's modernisation push.</p>
<p class="bi-te"><b>భైరవ లైట్ కమాండో బెటాలియన్</b> (అక్టోబర్ 2025లో ఏర్పాటు) మొదటిసారి కవాతులో. <b>శక్తిబాణ్</b> రెజిమెంట్, <b>సూర్యాస్త్ర</b> రాకెట్, <b>LR-AShM</b> హైపర్‌సోనిక్ క్షిపణి, రోబోటిక్ కుక్కలు ప్రదర్శించబడ్డాయి.</p>

<div class="section-hdr">Gallantry Awards 2026 / శౌర్య పురస్కారాలు 2026</div>
<table class="key-table">
<tr><th>Award</th><th>Recipient(s)</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total awarded</td><td>70 personnel honoured</td><td class="bi-te">70 మంది గౌరవించబడ్డారు</td></tr>
<tr><td><b>Ashok Chakra</b> (1)</td><td>Gp Capt Shubhanshu Shukla — for Axiom-4 mission; <b>highest peace-time gallantry award</b></td><td class="bi-te">అశోక చక్ర — గ్రూప్ కెప్టెన్ శుభాంశు శుక్లా (యాక్సియమ్-4)</td></tr>
<tr><td><b>Kirti Chakra</b> (3)</td><td>Prashanth B Nair (Gaganyaan astronaut), Maj Arundeep Singh, Naib Subedar Doleshwar Subba</td><td class="bi-te">కీర్తి చక్ర — ప్రశాంత్ నాయర్, అరుందీప్ సింగ్, దోలేశ్వర్ సుబ్బ</td></tr>
<tr><td><b>Shaurya Chakra</b></td><td>18 recipients</td><td class="bi-te">శౌర్య చక్ర — 18 మంది</td></tr>
</table>
<p><b>Strategic & Symbolic Significance:</b> The 77th Republic Day parade showcased India's emergence as a civilizational power and strategic autonomous nation. The unprecedented invitation of two EU Commission heads (Costa & von der Leyen) and the first-ever march of an EU military contingent outside Europe signal deepening India-EU strategic ties and EU recognition of India's democratic weight. The "150 Years of Vande Mataram" theme (first sung publicly in 1876) connects to India's anti-colonial legacy and contemporary national assertion. <b>Military Modernization Message:</b> The Bhairav Light Commando Battalion's debut, Suryastra rocket systems, hypersonic LR-AShM missiles, and robotic dogs underscore India's drone-autonomous-AI defence modernization and the shift from platform-centric to capability-centric acquisitions — critical for China border deterrence. <b>Gallantry Recognition:</b> The Ashok Chakra to Gp Capt Shubhanshu Shukla on Axiom-4 mission marks 42 years since Rakesh Sharma's ISS flight (1984), signaling India's civilian space programme maturation and recognition of astronaut-scientists in defence honours — bridging civil-defence space integration.</p>
<p class="bi-te"><b>వ్యూహాత్మక ప్రతీక:</b> 77వ గణతంత్ర కవాతు భారత్ సభ్యత శక్తి &amp; వ్యూహాత్మక స్వయంత్రత ప్రదర్శన. EU నేతల ఆహ్వానం &amp; EU సైనిక కవాతు యూరప్ బయట మొదటిసారి — భారత్-EU సంబంధాల పరిణామం సూచిస్తుంది. <b>రక్షణ ఆధునికీకరణ:</b> భైరవ బెటాలియన్, సూర్యాస్త్ర, LR-AShM, రోబోటిక్స్ భారత్ AI-autonomous-drone ఆధునికీకరణ; చైనా సరిహద్దు నిరోధకం. <b>శౌర్య గుర్తింపు:</b> అశోక చక్ర శుభాంశు శుక్లా — 1984 తర్వాత భారత్ అంతరిక్ష పరిణామం; సిviліան-defence అంతరిక్ష ఏకీకరణ.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  3. PADMA AWARDS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_padma_awards',
              'Padma Awards 2026',
              'పద్మ పురస్కారాలు 2026', """
<div class="concept-cover">
  <h1>Padma Awards 2026 &nbsp;<span class="bi-te">/ పద్మ పురస్కారాలు 2026</span></h1>
  <div class="sub">Announced January 25, 2026 • 131 Awards • Republic Day Eve</div>
</div>

<div class="section-hdr">Overall Tally / మొత్తం వివరాలు</div>
<table class="key-table">
<tr><th>Category</th><th>Count</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Padma Vibhushan</td><td>5</td><td class="bi-te">పద్మ విభూషణ్ — 5</td></tr>
<tr><td>Padma Bhushan</td><td>13</td><td class="bi-te">పద్మ భూషణ్ — 13</td></tr>
<tr><td>Padma Shri</td><td>113 (incl. 4 from AP, 7 from TS)</td><td class="bi-te">పద్మశ్రీ — 113 (AP నుండి 4, TS నుండి 7)</td></tr>
<tr><td><b>Total</b></td><td><b>131 awards</b></td><td class="bi-te"><b>మొత్తం 131</b></td></tr>
</table>

<div class="section-hdr">Padma Vibhushan 2026 (5) / పద్మ విభూషణ్ 2026</div>
<table class="key-table">
<tr><th>Name</th><th>Field</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Dharmendra</td><td>Arts (Cinema) — <b>Posthumous</b></td><td class="bi-te">ధర్మేంద్ర — సినిమా (మరణానంతరం)</td></tr>
<tr><td>V.S. Achuthanandan</td><td>Public Affairs — <b>Posthumous</b>; former Kerala CM</td><td class="bi-te">వి.ఎస్. అచ్యుతానందన్ (మరణానంతరం)</td></tr>
<tr><td>K.T. Thomas</td><td>Public Affairs (former SC judge)</td><td class="bi-te">కె.టి. థామస్ — మాజీ సుప్రీం కోర్ట్ న్యాయమూర్తి</td></tr>
<tr><td>N. Rajam</td><td>Arts (Violin maestro)</td><td class="bi-te">ఎన్. రాజమ్ — వయోలిన్ విద్వాంసురాలు</td></tr>
<tr><td>P. Narayanan</td><td>Trade & Industry</td><td class="bi-te">పి. నారాయణన్ — వాణిజ్యం</td></tr>
</table>

<div class="section-hdr">Padma Bhushan 2026 — Notable Recipients (13 total) / పద్మ భూషణ్ 2026</div>
<table class="key-table">
<tr><th>Name</th><th>Field</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Alka Yagnik</td><td>Arts (Playback singing)</td><td class="bi-te">అల్కా యాగ్నిక్ — గాయని</td></tr>
<tr><td>Mammootty</td><td>Arts (Cinema - Malayalam)</td><td class="bi-te">మమ్ముట్టి — సినిమా</td></tr>
<tr><td>Uday Kotak</td><td>Trade & Industry (Kotak Mahindra Bank)</td><td class="bi-te">ఉదయ్ కోటక్ — వాణిజ్యం</td></tr>
<tr><td>Piyush Pandey</td><td>Arts (Advertising) — <b>Posthumous</b></td><td class="bi-te">పీయూష్ పాండే (మరణానంతరం)</td></tr>
<tr><td>Vijay Amritraj</td><td>Sports (Tennis)</td><td class="bi-te">విజయ్ అమృతరాజ్ — టెన్నిస్</td></tr>
<tr><td>Nori Dattatreyudu</td><td>Medicine (Oncology)</td><td class="bi-te">నోరి దత్తాత్రేయుడు — వైద్యం (క్యాన్సర్)</td></tr>
<tr><td>Rohit Sharma</td><td>Sports (Cricket - Indian Captain)</td><td class="bi-te">రోహిత్ శర్మ — క్రికెట్</td></tr>
</table>
<p><b>Cultural & Governance Significance:</b> The 2026 Padma Awards (131 total) recognize India's inclusive development narrative across arts, sports, medicine, and public affairs. The posthumous awards to Dharmendra (cinema icon), V.S. Achuthanandan (Kerala CM), and Piyush Pandey (advertising legend) underscore India's retrospective acknowledgment of transformative careers — a hallmark of democratic societies honoring cultural architects. <b>Regional Inclusion & Gender Balance:</b> AP's 4 and TS's 7 Padma Shri awardees reflect southern state contributions to India's cultural economy; Alka Yagnik, Smriti Mandhana's repeated honours (5 times), and inclusion of sports/medicine professionals signal multi-sector recognition. <b>India's Soft Power:</b> The violin maestro N. Rajam and cinema figures (Mammootty, Dharmendra) exemplify India's civilizational soft power — arts recognition crucial for India's global cultural positioning and UNESCO heritage goals. Awards ceremony at Rashtrapati Bhavan (traditional April timing) reinforces constitutional ceremonies as citizen-centred governance theatre in the world's largest democracy.</p>
<p class="bi-te"><b>సాంస్కృతిక &amp; నిర్వహణ ప్రాముఖ్యత:</b> 2026 పద్మ పురస్కారాలు (131) భారత్ సాంస్కృతిక ఆర్థిక, క్రీడలు, వైద్యం, జనసేవ గుర్తింపు. మరణానంతర పురస్కారాలు — ధర్మేంద్ర, వి.ఎస్. అచ్యుతానందన్, పీయూష్ పాండే — సభ్యత సమాజాల ఐతిహాసిక మీపున సంకేతం. <b>ప్రాంతీయ సమावేశం:</b> AP 4, TS 7 పద్మశ్రీ పురస్కారాలు దక్షిణ సంస్కృతి-వర్ణనం. ఆల్కా, స్మృతి (5 సారి), క్రీడలు/వైద్యం బహుశাఖీయ గుర్తింపు. <b>భారత్ సాఫ్ట్ పవర్:</b> వయోలిన్ న. రాజమ్, సినిమా విభూతులు భారత్ సభ్యత శక్తి — UNESCO వారసత్వ లక్ష్యాల ఏకీకరణ.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  4. ISRO & SPACE MISSIONS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_isro_space',
              'ISRO & Space Missions 2026',
              'ఇస్రో & అంతరిక్ష మిషన్లు 2026', """
<div class="concept-cover">
  <h1>ISRO &amp; Space Missions 2026 &nbsp;<span class="bi-te">/ ఇస్రో &amp; అంతరిక్ష మిషన్లు 2026</span></h1>
  <div class="sub">LVM3-M6 BlueBird • Dhawan-3 • ISRO-ESA • Hydrogen Train</div>
</div>

<div class="section-hdr">LVM3-M6 BlueBird Block-2 Launch / LVM3-M6 ప్రయోగం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td>December 24, 2025</td><td class="bi-te">డిసెంబర్ 24, 2025</td></tr>
<tr><td>Launch Vehicle</td><td>LVM3-M6 (Launch Vehicle Mark-3, mission 6)</td><td class="bi-te">LVM3-M6 ప్రయోగ వాహనం</td></tr>
<tr><td>Launch site</td><td>SDSC-SHAR, Sriharikota (Tirupati district)</td><td class="bi-te">శ్రీహరికోట (తిరుపతి జిల్లా)</td></tr>
<tr><td>Payload</td><td>BlueBird Block-2 satellite — <b>6,100 kg</b></td><td class="bi-te">బ్లూబర్డ్ బ్లాక్-2 ఉపగ్రహం — 6,100 కిలోలు</td></tr>
<tr><td>Record</td><td><b>Heaviest satellite ever launched from Indian soil</b></td><td class="bi-te">భారత గడ్డ నుండి అత్యంత భారీ ఉపగ్రహం</td></tr>
<tr><td>Milestone</td><td><b>100th satellite launch from SHAR</b></td><td class="bi-te">SHAR నుండి 100వ ఉపగ్రహ ప్రయోగం</td></tr>
<tr><td>Customer</td><td>AST SpaceMobile (USA) — commercial launch through NSIL</td><td class="bi-te">AST స్పేస్‌మొబైల్ — NSIL వాణిజ్య ప్రయోగం</td></tr>
</table>

<div class="section-hdr">Skyroot Aerospace — Dhawan-3 / స్కైరూట్ — ధవన్-3</div>
<p><b>Space Sector Maturation & Commercial Ecosystem:</b> The LVM3-M6 BlueBird launch (6,100 kg satellite — India's heaviest from Indian soil) and 100th SHAR satellite launch milestone underscore ISRO's operational excellence and NSIL's commercial gateway success. India's space economy is transitioning from state-centric to private-commercial hybrid model aligned with global NewSpace trends. The AST SpaceMobile commercial contract demonstrates Indian launch services capturing international customers — advancing India's space industrial base and export revenue. <b>Private Sector Breakthrough:</b> Skyroot's Dhawan-3 cryogenic engine test (145 seconds) represents India's private spaceflight enablement — critical for reducing launch costs (targeting 40% cost reduction vs ISRO) and enabling mega-constellation deployment. Named after Dr. Satish Dhawan (first ISRO chairman), it symbolizes institutional knowledge transfer to NewSpace entrepreneurs. <b>India-Europe Space Cooperation:</b> ISRO-ESA FLEX mission participation positions India in global earth observation network — vegetation monitoring, climate data integration crucial for India's Environmental SDG tracking and forest-carbon accounting under Paris NDC commitments.</p>
<p class="bi-te"><b>అంతరిక్ష సెక్టర్ పరిపక్వత:</b> LVM3-M6 ఆరుద్ధ, 100వ ఉపగ్రహ ప్రయోగం ISRO దక్ష్యం. నిజమ భారత్ వ్యవసాయ కక్ష్య—private hybrid నమూనా global NewSpace అనుసారం. AST SpaceMobile ఒప్పందం అంతర్జాతీయ సేవలు చేపట్టడం. <b>Private Sector అధిగమనం:</b> Skyroot Dhawan-3 చాలక మూల్య పతనం (40% తగ్గింపు లక్ష్యం). డా. సతీష్ ధవన్ పేరు సంస్థానిక జ్ఞానం బదిలీ సూచిస్తుంది. <b>ఇస్రో-ESA సహకారం:</b> FLEX మిషన్ భారత్ భూమి పరిశీలన నెట్‌వర్క్‌లో స్థానం — వృక్ష పర్యవేక్షణ, climate డేటా భారత్ పర్యావరణ SDG &amp; Paris NDC కమిట్‌మెంట్‌ల సమీకరణ.</p>

<div class="section-hdr">ISRO-ESA Cooperation / ఇస్రో-ESA సహకారం</div>
<p>ISRO and the <b>European Space Agency (ESA)</b> signed an earth observation cooperation agreement. India will participate in the ESA's <b>FLEX mission</b> (Fluorescence Explorer) for vegetation monitoring.</p>
<p class="bi-te">ఇస్రో మరియు <b>యూరోపియన్ స్పేస్ ఏజెన్సీ (ESA)</b> భూమి పరిశీలన సహకార ఒప్పందం. ESA <b>FLEX మిషన్</b>లో భారత్ భాగస్వామి (వృక్షసంపద పర్యవేక్షణ).</p>

<div class="section-hdr">India's First Hydrogen Train / మొదటి హైడ్రోజన్ రైలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Trial date</td><td>February 25, 2026</td><td class="bi-te">ఫిబ్రవరి 25, 2026</td></tr>
<tr><td>Route</td><td>Jind to Sonipat (Haryana)</td><td class="bi-te">జింద్ — సోనిపట్ (హరియాణా)</td></tr>
<tr><td>Record</td><td><b>World's longest hydrogen train on broad gauge</b></td><td class="bi-te">బ్రాడ్ గేజ్ పై ప్రపంచంలోనే అతిపొడవైన హైడ్రోజన్ రైలు</td></tr>
<tr><td>Configuration</td><td>10 coaches, speed 110 kmph</td><td class="bi-te">10 బోగీలు, 110 కి.మీ./గం.</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════════
#  5. DEFENCE ACQUISITIONS & ARMS TRADE 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_defence',
              'Defence Acquisitions & Arms Trade 2026',
              'రక్షణ కొనుగోళ్లు & ఆయుధ వాణిజ్యం 2026', """
<div class="concept-cover">
  <h1>Defence Acquisitions &amp; Arms Trade 2026 &nbsp;<span class="bi-te">/ రక్షణ కొనుగోళ్లు 2026</span></h1>
  <div class="sub">DAC Approvals • SIPRI Report • INS Anjadip • Shipbuilding Scheme</div>
</div>

<div class="section-hdr">Defence Acquisition Council (DAC) Approvals / DAC ఆమోదాలు</div>
<table class="key-table">
<tr><th>Date</th><th>Value</th><th>Key items</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Dec 29, 2025</td><td>Rs.79,000 crore</td><td>Pinaka extended-range rockets, loiter munitions, drone-detection systems</td><td class="bi-te">పినాకా, లాయిటర్ ఆయుధాలు, డ్రోన్-గుర్తింపు</td></tr>
<tr><td>Mar 27, 2026</td><td>Rs.2.38 lakh crore</td><td>S-400 squadrons, MTA aircraft, Sukhoi-30 overhauls, Dhanush howitzers</td><td class="bi-te">S-400, MTA, సుఖోయ్-30, ధనుష్ ఫిరంగులు</td></tr>
</table>

<div class="section-hdr">SIPRI Report 2021-25 / SIPRI నివేదిక</div>
<table class="key-table">
<tr><th>Finding</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>#1 importer</td><td>Ukraine — 9.7% of global arms imports</td><td class="bi-te">అతిపెద్ద దిగుమతిదారు: ఉక్రెయిన్ (9.7%)</td></tr>
<tr><td><b>India's Russia share</b></td><td>Fell from <b>70% to 40%</b> — sharp drop in Russian dependence</td><td class="bi-te">భారత్ — రష్యా వాటా 70% → 40%</td></tr>
<tr><td>#1 exporter</td><td>USA — 42% of global arms exports</td><td class="bi-te">అతిపెద్ద ఎగుమతిదారు: అమెరికా (42%)</td></tr>
<tr><td>China</td><td><b>Dropped out of top-10 exporters</b> for first time since 1991</td><td class="bi-te">చైనా టాప్-10 ఎగుమతిదారుల నుండి తొలగింది (1991 తర్వాత మొదటిసారి)</td></tr>
</table>

<div class="section-hdr">INS Anjadip / INS అంజదిప్</div>
<p><b>Indigenous Naval Capability & Strategic Autonomy:</b> INS Anjadip's indigenous construction at Visakhapatnam represents India's "Atmanirbhar Bharat" doctrine in maritime defence — reducing foreign dependence for specialized ASW platforms. The anti-submarine shallow water craft addresses Indian Navy's critical capability gap in coastal/exclusive economic zone (EEZ) protection, particularly against Pakistan submarines (Indian Ocean strategy). The "Dolphin Killer" nickname reflects operational doctrine tailoring to adversary submarine patterns. <b>Diversification of Arms Sources:</b> The SIPRI 2021-25 report shows India's Russian arms dependence collapsed from 70% to 40% — major geopolitical shift toward Western suppliers (US, Israel) while maintaining strategic autonomy. This reflects India's non-aligned modernization strategy without exclusive bloc alignment. China's drop from top-10 arms exporters (first time since 1991) signals global shift in military procurement patterns. <b>Economic-Military Integration:</b> Shipbuilding schemes (SBFAS+SBDS, Rs.44,700 cr) represent fiscal federalism in defence manufacturing — 15-25% subsidies incentivize private Indian shipyards to absorb INS construction capacity, building domestic industrial base (critical for Chinese competition and blue-economy leadership through 2036).</p>
<p class="bi-te"><b>స్వేచ్ఛ నావిక సామర్థ్యం:</b> INS అంజదిప్ విశాఖపట్నంలో స్వదేశీ నిర్మాణం "ఆత్మనిర్భర భారత్" సిద్ధాంతం. పాకిస్తాన్ సబ్‌మెరైన్‌ల విరుద్ధ దశ. <b>ఆయుధ సరఫరా విభేదన:</b> SIPRI నివేదిక భారత్ రష్యా ఆధారపడటం 70% → 40% — USA, ఇస్రేల్ వైపు కోణం. చైనా ఎగుమతిదారుల నుండి పతనం (1991 తర్వాత మొదటిసారి) — అంతర్జాతీయ విస్థాపన సూచిస్తుంది. <b>ఆర్థిక-సైనిక ఏకీకరణ:</b> నౌకా నిర్మాణ పథకాలు (44,700 కోట్లు, 15-25% సబ్సిడీ) — దేశీయ పారిశ్రామిక భారం నిర్మాణం, చైనా పోటీ, నీలలోక ఆర్థిక నేతృత్వం 2036 వరకు.</p>

<div class="section-hdr">Shipbuilding Schemes / నౌకా నిర్మాణ పథకాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total outlay</td><td>Rs.44,700 crore</td><td class="bi-te">మొత్తం రూ.44,700 కోట్లు</td></tr>
<tr><td>Schemes</td><td>SBFAS (Shipbuilding Financial Assistance) + SBDS (Shipbuilding Development Scheme)</td><td class="bi-te">SBFAS + SBDS</td></tr>
<tr><td>Subsidy</td><td>15-25% financial assistance to Indian shipyards</td><td class="bi-te">15-25% ఆర్థిక సహాయం</td></tr>
<tr><td>Validity</td><td>Valid until <b>March 2036</b></td><td class="bi-te">మార్చి 2036 వరకు అమలు</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════════
#  6. INDIA'S FOREIGN BILATERAL DIPLOMACY 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_india_foreign',
              "India's Foreign Bilateral Diplomacy 2026",
              'భారత ద్వైపాక్షిక దౌత్యం 2026', """
<div class="concept-cover">
  <h1>India's Foreign Bilateral Diplomacy 2026 &nbsp;<span class="bi-te">/ భారత ద్వైపాక్షిక దౌత్యం 2026</span></h1>
  <div class="sub">EU FTA • Germany • UAE • New Zealand • South Korea</div>
</div>

<div class="section-hdr">India-EU FTA / భారత్-EU FTA</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Signed</td><td>January 27, 2026</td><td class="bi-te">జనవరి 27, 2026</td></tr>
<tr><td>Nickname</td><td>"Mother of All Deals"</td><td class="bi-te">"అన్ని ఒప్పందాల తల్లి"</td></tr>
<tr><td>Tariffs</td><td><b>99% of Indian export tariffs</b> removed</td><td class="bi-te">భారత ఎగుమతులపై 99% సుంకాలు తొలగింపు</td></tr>
<tr><td>Roadmap</td><td>"Strategic Agenda 2030"</td><td class="bi-te">వ్యూహాత్మక ఎజెండా 2030</td></tr>
</table>
<p><b>Strategic Trade & Geopolitical Realignment:</b> The India-EU FTA (Jan 27, 2026) signals strategic autonomous partnership beyond Western-centric frameworks. The "Mother of All Deals" framing reflects India's negotiating leverage in multipolar geopolitics — 99% tariff elimination on Indian exports to EU market (€530 billion 2025) enables Indian agricultural, textiles, pharma, and IT services penetration while EU gains market access. <b>Implementation Mechanics:</b> "Strategic Agenda 2030" roadmap covers defense partnerships (semiconductors, critical minerals supply chain de-risking from China), green hydrogen tech transfer, and critical supply chain resilience — addressing EU's China-dependency vulnerabilities while India gains technology access. <b>India's Global South Leadership:</b> This FTA positions India as counterweight to US-led trade frameworks, strengthening BRICS+ and Global South bargaining power in WTO/UNCTAD negotiations — crucial for India's vaccine diplomacy, technology transfer demands, and climate finance activism.</p>

<div class="section-hdr">India-Germany / భారత్-జర్మనీ</div>
<p>Chancellor <b>Friedrich Merz</b> visited India <b>January 12-13, 2026</b>. <b>19 MoUs</b> signed across defence, semiconductors, and green-NH3 (ammonia). The <b>International Kite Festival 2026</b> was held at <b>Sabarmati</b>.</p>
<p class="bi-te">జర్మనీ ఛాన్సలర్ <b>ఫ్రెడరిక్ మెర్జ్</b> జనవరి 12-13, 2026లో భారత్ సందర్శించారు. <b>19 MoU</b>లు — రక్షణ, సెమీకండక్టర్లు, గ్రీన్-NH3. <b>సబర్మతి</b>లో అంతర్జాతీయ గాలిపటాల ఉత్సవం.</p>

<div class="section-hdr">India-UAE / భారత్-UAE</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td>January 19, 2026</td><td class="bi-te">జనవరి 19, 2026</td></tr>
<tr><td>UAE President</td><td>Sheikh Mohammed bin Zayed</td><td class="bi-te">షేక్ మహమ్మద్ బిన్ జాయెద్</td></tr>
<tr><td>Trade target</td><td>$200 billion by 2032</td><td class="bi-te">2032 నాటికి $200 బిలియన్ వాణిజ్యం</td></tr>
<tr><td>SHANTI Act</td><td>SHANTI Act 2025 — bilateral investment treaty framework</td><td class="bi-te">SHANTI చట్టం 2025</td></tr>
<tr><td>Dholera SIR</td><td>UAE investment in Dholera Special Investment Region (Gujarat)</td><td class="bi-te">ధోలేరా SIR (గుజరాత్)</td></tr>
<tr><td>Cultural</td><td>"House of India" inaugurated in Abu Dhabi</td><td class="bi-te">"హౌస్ ఆఫ్ ఇండియా" — అబూ ధాబి</td></tr>
</table>

<div class="section-hdr">India-New Zealand FTA / భారత్-న్యూజిలాండ్</div>
<p>Signed <b>December 22, 2025</b>. Target: $5 billion bilateral trade in 5 years. <b>NZ committed $20 billion investment</b> into India.</p>
<p class="bi-te">భారత్-న్యూజిలాండ్ FTA — డిసెంబర్ 22, 2025. 5 సం.లో $5 బిలియన్ వాణిజ్యం; న్యూజిలాండ్ $20 బిలియన్ పెట్టుబడి హామీ.</p>

<div class="section-hdr">India-South Korea / భారత్-దక్షిణ కొరియా</div>
<p>President <b>Lee Jae-myung</b> visited India <b>April 19-21, 2026</b>. <b>15 MoUs</b> signed; target <b>$50 billion bilateral trade by 2030</b>.</p>
<p class="bi-te">కొరియా అధ్యక్షుడు <b>లీ జే-మ్యూంగ్</b> — ఏప్రిల్ 19-21, 2026. 15 MoUలు; 2030 నాటికి $50 బిలియన్ వాణిజ్యం.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  7. KEY APPOINTMENTS & GOVERNORS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_appointments',
              'Key Appointments & Governors 2026',
              'ముఖ్య నియామకాలు & గవర్నర్లు 2026', """
<div class="concept-cover">
  <h1>Key Appointments &amp; Governors 2026 &nbsp;<span class="bi-te">/ ముఖ్య నియామకాలు 2026</span></h1>
  <div class="sub">9 Governors • NITI Aayog CEO • Microsoft Gaming</div>
</div>

<div class="section-hdr">Governors Appointed / Transferred — March 5, 2026 / గవర్నర్ నియామకాలు</div>
<table class="key-table">
<tr><th>Name</th><th>Post</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Shiv Pratap Shukla</td><td>Governor of <b>Telangana</b></td><td class="bi-te">తెలంగాణ గవర్నర్</td></tr>
<tr><td>Jishnu Dev Varma</td><td>Governor of Maharashtra</td><td class="bi-te">మహారాష్ట్ర గవర్నర్</td></tr>
<tr><td>R.N. Ravi</td><td>Governor of West Bengal</td><td class="bi-te">పశ్చిమ బెంగాల్ గవర్నర్</td></tr>
<tr><td>Atal Hasnain</td><td>Governor of Bihar</td><td class="bi-te">బీహార్ గవర్నర్</td></tr>
<tr><td>Nand Kishore Yadav</td><td>Governor of Nagaland</td><td class="bi-te">నాగాలాండ్ గవర్నర్</td></tr>
<tr><td>Kavinder Gupta</td><td>Governor of Himachal Pradesh</td><td class="bi-te">హిమాచల్ ప్రదేశ్ గవర్నర్</td></tr>
<tr><td>Rajendra Arlekar</td><td>Governor of Tamil Nadu</td><td class="bi-te">తమిళనాడు గవర్నర్</td></tr>
<tr><td>Vinay K. Saxena</td><td>Lt. Governor of <b>Ladakh</b></td><td class="bi-te">లడఖ్ LG</td></tr>
<tr><td>Taranjit S. Sandhu</td><td>Lt. Governor of <b>Delhi</b></td><td class="bi-te">ఢిల్లీ LG</td></tr>
</table>

<div class="section-hdr">Other Key Appointments / ఇతర ముఖ్య నియామకాలు</div>
<table class="key-table">
<tr><th>Person</th><th>Role</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Nidhi Chhibber</td><td>NITI Aayog CEO — appointed <b>February 24, 2026</b>; 1994 IAS Chhattisgarh cadre</td><td class="bi-te">నీతి ఆయోగ్ CEO — నిధి ఛిబ్బర్ (1994 IAS, ఛత్తీస్‌గఢ్)</td></tr>
<tr><td>Asha Sharma</td><td>Microsoft Gaming CEO — appointed <b>February 20, 2026</b>; Indian-origin</td><td class="bi-te">మైక్రోసాఫ్ట్ గేమింగ్ CEO — ఆశా శర్మ (భారత మూలాలు)</td></tr>
</table>
<p><b>Governance & Policy Implementation:</b> Nidhi Chhibber's appointment as NITI Aayog CEO (Feb 24, 2026) from IAS Chhattisgarh cadre reflects India's practice of drawing experienced administrators for policy think-tank leadership — crucial for implementing 16th FC recommendations, economic survey insights, and state-center fiscal coordination. NITI Aayog is central to India's bottom-up federalism and subnational competitiveness benchmarking (SDG Tracker, State Innovation Index). <b>Global Talent Return & Tech Leadership:</b> Asha Sharma's appointment as Microsoft Gaming CEO (Indian-origin, Feb 20, 2026) exemplifies India's diaspora advantage in global tech corporations — signaling Indian talent's capabilities in gaming/metaverse sectors critical for post-COVID digital economy. This reflects India's soft power through tech entrepreneurship and corporate leadership in AI-gaming integration — areas aligned with NEP 2020 skill-building priorities.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  8. INDIAN SPORTS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_sports',
              'Indian Sports 2026',
              'భారత క్రీడలు 2026', """
<div class="concept-cover">
  <h1>Indian Sports 2026 &nbsp;<span class="bi-te">/ భారత క్రీడలు 2026</span></h1>
  <div class="sub">ICC U19 World Cup • Vaibhav Suryavanshi • BCCI Naman Awards</div>
</div>

<div class="section-hdr">ICC U19 Cricket World Cup 2026 / U19 క్రికెట్ ప్రపంచ కప్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Final date</td><td>February 6, 2026</td><td class="bi-te">ఫిబ్రవరి 6, 2026</td></tr>
<tr><td>Venue</td><td>Harare, Zimbabwe</td><td class="bi-te">హరారే, జింబాబ్వే</td></tr>
<tr><td>Result</td><td>India beat England by <b>100 runs</b></td><td class="bi-te">భారత్ — ఇంగ్లండ్‌పై 100 పరుగుల తేడాతో విజయం</td></tr>
<tr><td>India's Captain</td><td>Ayush Mhatre</td><td class="bi-te">కెప్టెన్: ఆయుష్ మాత్రే</td></tr>
<tr><td>Title</td><td>India's <b>6th</b> U19 World Cup title</td><td class="bi-te">భారత్ <b>6వ</b> U19 ప్రపంచ కప్</td></tr>
</table>

<div class="section-hdr">Vaibhav Suryavanshi — Star of the Tournament / వైభవ్ సూర్యవంశి</div>
<table class="key-table">
<tr><th>Stat</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Age</td><td>14 years 316 days</td><td class="bi-te">14 సం. 316 రోజులు</td></tr>
<tr><td>Final score</td><td><b>175 runs</b> in the final</td><td class="bi-te">ఫైనల్‌లో <b>175</b> పరుగులు</td></tr>
<tr><td>Tournament runs</td><td><b>439 runs</b> at <b>SR 169.49</b></td><td class="bi-te">టోర్నీలో 439 పరుగులు; స్ట్రైక్ రేట్ 169.49</td></tr>
<tr><td>Awards</td><td>Player of the Match (final) + Player of the Tournament</td><td class="bi-te">మ్యాచ్ పురుషోత్తముడు + టోర్నీ పురుషోత్తముడు</td></tr>
<tr><td>Record</td><td><b>Youngest ever Player of the Match in any World Cup final</b></td><td class="bi-te">ఏ ప్రపంచ కప్ ఫైనల్‌లోనైనా అతి చిన్న వయస్సు Player of Match</td></tr>
</table>
<p><b>Youth Development & Talent Pipeline:</b> Vaibhav Suryavanshi's 175-run final and 439-run tournament tally at age 14-years-316-days (youngest Player of Match in any World Cup final) represents India's systematic youth cricket development through state-level academies and BCCI's grassroots talent identification. His strike rate (169.49) signals T20-influenced batting evolution — modern cricket's shift from test-centric to format-versatile skill-building. <b>Cricket Ecosystem Maturation:</b> India's 6th U19 World Cup title (Feb 2026, Harare) reflects 40+ years of institutional cricket development starting from Kapil Dev's 1983 World Cup victory. Captain Ayush Mhatre's leadership and tournament consistency (Suryavanshi's consistency across formats) demonstrate BCCI's bench-strength building crucial for maintaining global cricket dominance. <b>Indian Sports Philosophy:</b> Recognition through BCCI Naman Awards (Polly Umrigar for Shubman Gill, 5-time Smriti Mandhana) institutionalizes gender parity in cricket honors — aligned with SDG 5 (Gender Equality) while building aspiring young players' role models across gender lines.</p>

<div class="section-hdr">BCCI Naman Awards 2026 — March 15 / BCCI నామన్ పురస్కారాలు</div>
<table class="key-table">
<tr><th>Award</th><th>Recipient(s)</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Polly Umrigar (Intl Cricketer of Year)</td><td><b>Shubman Gill</b> (TS) + <b>Smriti Mandhana</b> (5th time)</td><td class="bi-te">పాలీ ఉమ్రిగర్ — శుభమన్ గిల్ + స్మృతి మంధానా (5వసారి)</td></tr>
<tr><td>C.K. Naidu Lifetime Achievement</td><td>Roger Binny, Rahul Dravid, Mithali Raj</td><td class="bi-te">CK నాయుడు జీవితకాల పురస్కారం — రోజర్ బిన్ని, రాహుల్ ద్రవిడ్, మిథాలీ రాజ్</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════════════════
#  9. CENSUS 2026 & ARTEMIS-2
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_census_artemis',
              "India's 16th Census & Artemis-2 Moon Mission 2026",
              '16వ జనాభా గణన & ఆర్టెమిస్-2', """
<div class="concept-cover">
  <h1>India's 16th Census &amp; Artemis-2 Moon Mission 2026 &nbsp;<span class="bi-te">/ 16వ జనాభా గణన &amp; ఆర్టెమిస్-2</span></h1>
  <div class="sub">Self-Enumeration & Caste Enumeration • Beyond Apollo-13 Distance Record</div>
</div>

<div class="section-hdr">India's 16th Census 2026 / 16వ జనాభా గణన</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Begins</td><td>April 1, 2026</td><td class="bi-te">ఏప్రిల్ 1, 2026న ప్రారంభం</td></tr>
<tr><td>Phase 1 (House listing)</td><td>Until September 30, 2026</td><td class="bi-te">దశ-1: సెప్టెంబర్ 30, 2026 వరకు</td></tr>
<tr><td>Phase 2 (Population enumeration)</td><td>February 2027</td><td class="bi-te">దశ-2: ఫిబ్రవరి 2027</td></tr>
<tr><td>Total cost</td><td>Rs.11,718 crore</td><td class="bi-te">వ్యయం రూ.11,718 కోట్లు</td></tr>
<tr><td>Mode</td><td>Digital, available in <b>16 languages</b></td><td class="bi-te">డిజిటల్; 16 భాషల్లో</td></tr>
<tr><td><b>Firsts</b></td><td>First Census with <b>self-enumeration</b> AND <b>caste enumeration</b></td><td class="bi-te">మొదటి Census — స్వీయ-గణన మరియు కుల గణన రెండూ</td></tr>
<tr><td>Mascots</td><td><b>Janaganana</b> (woman) and <b>Janagan</b> (man)</td><td class="bi-te">శుభంకరాలు: జనగణన (స్త్రీ), జనగణ్ (పురుషుడు)</td></tr>
</table>
<p><b>Governance Transformation & Data-Driven Federalism:</b> The 16th Census (Apr 2026 - Feb 2027) represents India's transition to digital, decentralized enumeration — 16-language support reflects constitutional pluralism and inclusive governance design. Total cost (Rs.11,718 cr) reflects India's commitment to demographic accuracy for resource allocation under 16th Finance Commission recommendations. <b>Caste Data — Historical & Policy Significance:</b> Self-enumeration + caste enumeration (first since 1931) enables evidence-based OBC affirmative action refinement, backward region identification for targeted development, and Scheduled Caste/Tribe welfare program effectiveness assessment. Caste census data directly informs state-level reservation policies and local body affirmative action (critical for gender-based SC/ST intersectionality analysis). <b>Digital Innovation & Citizen Participation:</b> Self-enumeration (digital-first, language-accessible) shifts power to citizens — aligned with Digital India's e-governance philosophy and constitutional right-to-information principles. Mascots (Janaganana/Janagan) reflect democratic participation narrative. Census data feeds into state-level SDG monitoring (health, education equity), poverty estimation, and migration policy frameworks — essential for internal security and development regional balancing.</p>
<p class="bi-te"><b>నిర్వహణ రూపాంతరణ:</b> 16వ Census డిజిటల్ విడిపోయిన జనాభా గణన — 16 భాషలు రాజ్యాంగ బహుభాషికవాదం. రూ.11,718 కోట్లు demographic ఖచ్చితత్వం 16వ FC సిఫారసుల సంస్థానిక కేటాయింపుకు. <b>కుల డేటా:</b> 1931 తర్వాత మొదటిసారి OBC సమర్థక చర్య శుద్ధీకరణ, తిరిగిపాటు జిల్లా గుర్తింపు, SC/ST సమాచారం సమర్థకత. <b>ডિజిటల్ నవీకరణ:</b> Self-enumeration నాగరికుల చేతిలో శక్తి — Digital India e-governance సమర్థకం. Census డేటా SDG పర్యవేక్షణ (ఆరోగ్యం, విద్య సమానత్వం), పేదరికం అంచనా, వలసలు విధానానికి కీలకం.</p>

<div class="section-hdr">NASA Artemis-2 Mission / NASA ఆర్టెమిస్-2</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Mission window</td><td>April 2-11, 2026</td><td class="bi-te">ఏప్రిల్ 2-11, 2026</td></tr>
<tr><td>Duration</td><td>10 days</td><td class="bi-te">10 రోజుల మిషన్</td></tr>
<tr><td>Crew (4)</td><td>Reid Wiseman, Victor Glover, Christina Koch (USA); Jeremy Hansen (Canada)</td><td class="bi-te">4 వ్యోమగాములు: విస్‌మాన్, గ్లోవర్, కోచ్; హాన్సెన్ (కెనడా)</td></tr>
<tr><td><b>Distance record</b></td><td><b>2,52,760 miles from Earth</b> — beat Apollo-13's record (1970)</td><td class="bi-te">భూమి నుండి 2,52,760 మైళ్లు — అపోలో-13 (1970) రికార్డ్ అధిగమించింది</td></tr>
<tr><td>Glover's milestone</td><td><b>First non-white astronaut</b> to reach lunar orbit distance</td><td class="bi-te">విక్టర్ గ్లోవర్ — చంద్ర కక్ష్య దూరం చేరిన మొదటి non-white వ్యోమగామి</td></tr>
<tr><td>Splashdown</td><td>Pacific Ocean — April 11, 2026</td><td class="bi-te">పసిఫిక్ మహాసముద్రంలో ఏప్రిల్ 11న తిరిగి దిగుబడి</td></tr>
</table>
<p>Artemis-2 is NASA's first crewed lunar mission since Apollo-17 (1972) — a circumlunar flyby, not a landing. It paves the way for Artemis-3 (planned lunar landing).</p>
<p class="bi-te">ఆర్టెమిస్-2 — అపోలో-17 (1972) తర్వాత NASA మొదటి సిబ్బందిగల చంద్ర మిషన్. ఇది fly-by, ల్యాండింగ్ కాదు. ఆర్టెమిస్-3 (చంద్రుని ల్యాండింగ్)కి దారి తీస్తుంది.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  10. 131st CONSTITUTIONAL AMENDMENT DEFEATED 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_const_amendment',
              '131st Constitutional Amendment Defeated 2026',
              '131వ రాజ్యాంగ సవరణ ఓటమి 2026', """
<div class="concept-cover">
  <h1>131st Constitutional Amendment Defeated 2026 &nbsp;<span class="bi-te">/ 131వ రాజ్యాంగ సవరణ ఓటమి</span></h1>
  <div class="sub">April 17, 2026 • Lok Sabha • Women's 33% Reservation Linked</div>
</div>

<div class="section-hdr">The Vote / ఓటింగ్ ఫలితం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td>April 17, 2026</td><td class="bi-te">ఏప్రిల్ 17, 2026</td></tr>
<tr><td>House</td><td>Lok Sabha</td><td class="bi-te">లోక్‌సభ</td></tr>
<tr><td>In favour</td><td>298 votes</td><td class="bi-te">పక్షాన: 298</td></tr>
<tr><td>Against</td><td>230 votes</td><td class="bi-te">వ్యతిరేకంగా: 230</td></tr>
<tr><td><b>Threshold needed</b></td><td><b>352 (two-thirds majority)</b></td><td class="bi-te">అవసరం: 352 (2/3 మెజారిటీ)</td></tr>
<tr><td><b>Result</b></td><td><b>DEFEATED</b> — fell 54 votes short</td><td class="bi-te"><b>ఓడిపోయింది</b> — 54 ఓట్ల కొరత</td></tr>
</table>

<div class="section-hdr">What the Bill Would Have Done / బిల్లు యొక్క ప్రభావం</div>
<p>The 131st Constitutional Amendment Bill 2026 would have:</p>
<ul>
<li>Introduced <b>women's 33% reservation</b> in Lok Sabha and State Assemblies by 2029.</li>
<li>Increased Lok Sabha seats from <b>543 to 850</b> (proposed restructuring).</li>
<li>Triggered the <b>Delimitation Bill 2026</b> and <b>UT Laws (Amendment) Bill 2026</b> — both withdrawn after the defeat.</li>
<li>Linked the timing to the ongoing <b>16th Census</b> (April 2026 — Feb 2027) and the subsequent delimitation exercise.</li>
</ul>
<p class="bi-te">131వ సవరణ బిల్లు:</p>
<ul class="bi-te">
<li>2029 నాటికి లోక్‌సభ &amp; రాష్ట్ర అసెంబ్లీలలో మహిళలకు <b>33% రిజర్వేషన్</b>.</li>
<li>లోక్‌సభ సీట్లు <b>543 నుండి 850</b>కి పెంపు ప్రతిపాదన.</li>
<li>డీలిమిటేషన్ బిల్లు 2026 &amp; UT Laws (Amend) బిల్లు 2026 — రెండూ ఓటమి తర్వాత ఉపసంహరణ.</li>
<li>16వ Census తర్వాత డీలిమిటేషన్‌తో అనుసంధానం.</li>
</ul>

<div class="section-hdr">Constitutional Background / రాజ్యాంగ నేపథ్యం</div>
<p><b>Gender Equality & Constitutional Federalism:</b> The 131st Amendment's defeat (54 votes short of 352-vote 2/3 threshold) represents momentary parliamentary stalemate on gender equity despite cross-party women's rights consensus. The proposed 33% reservation would have implemented 30+ years of feminist activism, aligning India with constitutional Articles 14 (equality), 15 (non-discrimination), and 51(A)(e) (fundamental duties toward gender justice). <b>Implementation Complexity:</b> The Delimitation Bill 2026 (triggered by seat increase 543→850) directly impacts state-level representation and rural-urban population redistribution. Census 2026 data collection timing (Apr 2026-Feb 2027 overlap) requires simultaneous delimitation — administrative coordination challenge across 28 states. UT Laws amendment would have reformed Delhi, Ladakh, Puducherry assemblies' electoral frameworks — governance restructuring with implications for union territory development planning. <b>Political Economy of Defeat:</b> The vote (298 vs 230, NDA 293 vs INDIA 233) reflects coalition fragmentation — INDIA bloc regional parties unable to mobilize full strength, signaling opposition to delimitation's potential adverse effects on smaller states' representation. The defeat underscores gender equity's entanglement with federal balance, reservation politics (SC/ST/OBC intersectionality with gender), and electoral delimitation — issues requiring deeper social consensus beyond electoral majorities.</p>
<p class="bi-te"><b>లింగ సమానత్వం &amp; రాజ్యాంగ సంघీయత:</b> 131వ సవరణ ఓటమి (54 ఓట్ల కొరత) 33% రిజర్వేషన్‌కు సంసదీయ ఆటంకం. రాజ్యాంగ 14, 15, 51(A)(e) సమర్థకం. <b>నిబంధన సంక్లిష్టత:</b> డీలిమిటేషన్ బిల్లు (543 → 850 సీట్లు) రాష్ట్ర ప్రాతినిధ్యం, గ్రామీణ-నగర పుনర్విభజన. Census సమయం (Apr 2026-Feb 2027 అతిక్రమణ) అంతకూడా డీలిమిటేషన్ సమన్వయం కష్టం. UT చట్టాలు ఢిల్లీ, లడఖ్, పుదుచ్చేరి పరిపాలన పరిష్కారం. <b>రాజకీయ ఆర్థిక విశ్లేషణ:</b> NDA 293 vs INDIA 233 ఓటమి — coalition విభజనం, INDIA రాష్ట్ర పార్టీలు పూర్ణ శక్తి动员 నుండి దూరం. డీలిమిటేషన్ చిన్న రాష్ట్ర ప్రాతినిధ్య సంక్షోభం. లింగ సమానత్వం SC/ST/OBC రిజర్వేషన్ సంఘర్షణ, ఎన్నికల రెజిమెంట్ — సామాజిక సర్వసమ్మతి డిమాండ్.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  11. INDUSTRIAL & ECONOMIC SCHEMES 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_industrial_schemes',
              'Industrial & Economic Schemes 2026',
              'పారిశ్రామిక & ఆర్థిక పథకాలు 2026', """
<div class="concept-cover">
  <h1>Industrial &amp; Economic Schemes 2026 &nbsp;<span class="bi-te">/ పారిశ్రామిక &amp; ఆర్థిక పథకాలు 2026</span></h1>
  <div class="sub">BHAVYA • UDAN • RELIEF • Electronics Manufacturing • Jan Vishwas 2</div>
</div>

<div class="section-hdr">Major New Schemes Announced March 2026 / మార్చి 2026 కొత్త పథకాలు</div>
<table class="key-table">
<tr><th>Scheme</th><th>Outlay</th><th>Purpose</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>BHAVYA</b></td><td>Rs.28,602 crore</td><td>Announced March 18, 2026 — 100 industrial parks across India</td><td class="bi-te">100 పారిశ్రామిక పార్కులు</td></tr>
<tr><td><b>Modified UDAN</b></td><td>Rs.28,840 crore</td><td>10-year regional air-connectivity revival</td><td class="bi-te">10 సం. ప్రాంతీయ విమాన కనెక్టివిటీ</td></tr>
<tr><td><b>RELIEF</b></td><td>Rs.497 crore</td><td>Targeted support for exporters</td><td class="bi-te">ఎగుమతిదారులకు మద్దతు</td></tr>
</table>

<div class="section-hdr">Electronics Component Manufacturing Scheme / ఎలక్ట్రానిక్స్ తయారీ</div>
<p>Announced <b>January 2, 2026</b>: <b>22 proposals worth Rs.41,863 crore</b> approved. <b>Andhra Pradesh</b> is among the <b>8 states</b> selected for new facilities — a major boost to AP's electronics ecosystem and Sri City / Tirupati clusters.</p>
<p class="bi-te">జనవరి 2, 2026: 22 ప్రతిపాదనలు, రూ.41,863 కోట్లు ఆమోదం. <b>ఆంధ్రప్రదేశ్</b> ఎంపికైన <b>8 రాష్ట్రాల్లో</b> ఒకటి — శ్రీసిటీ/తిరుపతి క్లస్టర్‌లకు ప్రోత్సాహం.</p>

<div class="section-hdr">Jan Vishwas (Amendment of Provisions) Bill 2026 / జన్ విశ్వాస్ బిల్లు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Dates</td><td>Passed April 1-2, 2026</td><td class="bi-te">ఏప్రిల్ 1-2, 2026</td></tr>
<tr><td>Laws amended</td><td><b>79 central laws</b></td><td class="bi-te">79 కేంద్ర చట్టాలు</td></tr>
<tr><td>Provisions decriminalised</td><td><b>784 provisions</b></td><td class="bi-te">784 నిబంధనలు నేరం కాని కేటగిరీలోకి</td></tr>
<tr><td>Ministries</td><td><b>23 ministries</b></td><td class="bi-te">23 మంత్రిత్వ శాఖలు</td></tr>
</table>
<p><b>Regulatory Liberalization & Ease of Doing Business:</b> Jan Vishwas 2 (Apr 1-2, 2026) represents India's systematic deregulation wave — 784 provisions across 79 central laws decriminalized (shifting penalties from criminal to civil/administrative). This doubles down on Jan Vishwas 2023's 183 provisions in 42 laws, signaling government's "trust-based" regulatory philosophy replacing "inspection raj." The 23-ministry coordination reflects whole-of-government approach to compliance burden reduction. <b>Economic Impact & Compliance Cost Reduction:</b> Decriminalization reduces MSMEs' legal risk exposure and litigation costs — critical for India's 63 million MSME ecosystem contributing 30% GDP, 45% export revenue. Industries targeted: manufacturing, pharmaceuticals, food processing, textiles, mining. Policy aligns with World Bank's Ease of Doing Business rankings (India rank 63 in 2020, target: Top 50). <b>State Implementation & Competitive Federalism:</b> BHAVYA (100 industrial parks, Rs.28,602 cr) and modified UDAN (Rs.28,840 cr, 10-year regional air-connectivity revival) represent devolved industrial policy allowing state-level competitive positioning. Electronics Manufacturing Scheme's AP selection (among 8 states) reflects southern growth corridor strategy alongside traditional industrial clusters — accelerating electronics backward integration, reducing China dependence, and supporting FDI in semiconductor ecosystems aligned with India's "Chip-to-Chip" autonomy goals.</p>
<p class="bi-te"><b>నియంత్రణ ఉదారీకరణ:</b> జన్ విశ్వాస్ 2 (Apr 2026) 784 నిబంధనలు నేరం-కాని వర్గీకరణ (刑事 నుండి సివిల్/పరిపాలక). 23 మంత్రిత్వ సమన్వయం. <b>ఆర్థిక ప్రభావం:</b> MSMEs చట్టపరమైన ఝుమ్ము, సిద్ధాంత ఖర్చు తగ్గింపు — 63 మిలియన్ MSME, 30% GDP, 45% ఎగుమతులు. పరిశ్రమలు: తయారీ, ఔషధ, ఆహార, వస్త్రాలు. World Bank Ease రాంక్‌: 63 (2020), లక్ష్యం Top 50. <b>రాష్ట్ర అమలు:</b> BHAVYA (100 పార్కులు, 28,602 కోట్లు), UDAN సవరణ (28,840 కోట్లు, 10 సం. ప్రాంతీయ విమానం). Electronics Manufacturing — AP (8 రాష్ట్రాలు) — సరిహద్దు సెమీకండక్టర్ కన్ను, చైనా నిర్ભరత తగ్గింపు.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  12. OTHER NATIONAL HIGHLIGHTS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_misc',
              'Other National Highlights 2026',
              'ఇతర జాతీయ ముఖ్యాంశాలు 2026', """
<div class="concept-cover">
  <h1>Other National Highlights 2026 &nbsp;<span class="bi-te">/ ఇతర జాతీయ ముఖ్యాంశాలు 2026</span></h1>
  <div class="sub">Jnanpith • Wangchuk • Birla Motion • CEC Motion • Naxal-free • Higher Edu • Akshaya Patra</div>
</div>

<div class="section-hdr">60th Jnanpith Award (for 2025) / 60వ జ్ఞానపీఠ పురస్కారం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Announced</td><td>March 14, 2026</td><td class="bi-te">మార్చి 14, 2026</td></tr>
<tr><td>Recipient</td><td><b>R. Vairamuthu</b> (Tamil poet/lyricist)</td><td class="bi-te">ఆర్. వైరముత్తు (తమిళ కవి/గీత రచయిత)</td></tr>
<tr><td>Distinction</td><td><b>3rd Tamil writer</b> to receive Jnanpith</td><td class="bi-te">జ్ఞానపీఠం పొందిన 3వ తమిళ రచయిత</td></tr>
<tr><td>Prize</td><td>Rs.11 lakh + Saraswati statue + citation</td><td class="bi-te">రూ.11 లక్షలు + సరస్వతీ ప్రతిమ</td></tr>
</table>

<div class="section-hdr">Sonam Wangchuk Release / సోనమ్ వాంగ్‌చుక్ విడుదల</div>
<p><b>Civil Society & Regional Autonomy Tensions:</b> Sonam Wangchuk's 168-day NSA detention (Sept 26, 2025 - Mar 14, 2026) reflects tensions between national security frameworks and regional autonomy movements. Wangchuk's Ladakh statehood campaign challenged Delhi's centralized UT administration — 4 deaths during protests underscore grassroots dissent over resource control, constitutional status, and border security policy. His release signals potential political negotiation toward local governance concessions (Ladakh hill council autonomy, environmental protection against defence projects) balancing security concerns with democratic participation rights. <b>NSA as Governance Tool:</b> The detention exemplifies NSA application in civil disobedience contexts (non-violent activism treated as security threat) — a pattern debated in India's civil liberties discourse, particularly affecting minority-region political mobilization.</p>
<p class="bi-te"><b>సమాజ &amp; ప్రాంతీయ స్వయంత్రత సంఘర్షణ:</b> సోనమ్ వాంగ్‌చుక్ NSA నిర్బంధం (168 రోజులు) జాతీయ సంరక్షణ vs ప్రాంతీయ స్వయంత్రత సంఘర్షణ సూచిస్తుంది. లడఖ్ రాష్ట్రత్వ ఉద్యమం ఢిల్లీ కేంద్రీకృత UT పరిపాలన సవాల్ — 4 మరణాలు సంపద నియంత్రణ, రాజ్యాంగ స్థితి, సరిహద్దు విధానపై జనాల అసంతృప్తి. విడుదల స్థానిక పరిపాలన చైతన్యం (లడఖ్ హిల్ కౌన్సిల్ స్వయంత్రత, పర్యావరణ రక్షణ) సంచయం సూచిస్తుంది. <b>NSA పరిపాలన సాధనం:</b> శాంతియుత క్రియాకలాపాలను సంరక్షణ ఇతిహాసాలుగా చర్యకు ఉదాహరణ — సమాజ స్వేచ్ఛ ప్రసిద్ధ విమర్శ.</p>

<div class="section-hdr">No-Confidence vs LS Speaker Om Birla / లోక్‌సభ స్పీకర్‌పై అవిశ్వాస తీర్మానం</div>
<p>Motion defeated <b>March 10, 2026</b>. <b>113 MPs</b> signed the no-confidence motion against Speaker Om Birla. Final tally: <b>NDA 293 vs INDIA bloc 233</b>.</p>
<p class="bi-te">లోక్‌సభ స్పీకర్ ఓం బిర్లాపై అవిశ్వాస తీర్మానం మార్చి 10న ఓడిపోయింది. 113 ఎంపీలు సంతకం; NDA 293 — INDIA 233.</p>

<div class="section-hdr">CEC Impeachment Motion Rejected / CEC అభిశంసన తిరస్కరణ</div>
<p>The impeachment notice against Chief Election Commissioner Gyanesh Kumar was <b>rejected on April 6, 2026</b> by Rajya Sabha Chairman <b>Radhakrishnan</b>.</p>
<p class="bi-te">ప్రధాన ఎన్నికల కమిషనర్ జ్ఞానేశ్ కుమార్‌పై అభిశంసన నోటీసును రాజ్యసభ ఛైర్మన్ రాధాకృష్ణన్ ఏప్రిల్ 6, 2026న తిరస్కరించారు.</p>

<div class="section-hdr">India Declared Naxal-Free / భారత్ నక్సల్-రహితంగా ప్రకటన</div>
<p><b>Counter-Insurgency Success & Regional Security Strategy:</b> India's April 2026 "naxal-free" declaration (despite 37 "Concern" districts) represents a decade-long counter-insurgency strategy culmination — from 2004's 626-district Maoist prevalence to near-elimination through coordinated state-center operations. The strategy integrated development (mineral royalties to Scheduled Tribes, forest rights implementation), security operations (paramilitary deployment), and local governance (panchayat democratization in tribal zones). <b>Regional Variations & Persistent Challenges:</b> AP's Alluri Sitarama Raju district (renamed after APSC protester's grandson) and Telangana's Bhadradri Kothagudem & Mulugu remain "Concern" — reflecting indigenous resource struggles (bauxite mining, forest clearances) and land-tenure conflicts. These districts exemplify India's "development-security" nexus paradox — economic growth accelerating resource extraction while marginalized tribal communities resist land appropriation. <b>Internal Security & Federalism:</b> Success claims underscore central asymmetry: state capacity growth enables insurgency suppression but simultaneously enables extraction regimes, affecting subnational autonomy — a governance equity challenge in India's resource federalism architecture.</p>
<p class="bi-te"><b>విద్రోహ నిర్ముల తరం &amp; ప్రాంతీయ సంరక్షణ:</b> ఏప్రిల్ 2026 "నక్సల్-రహితం" ప్రకటన (37 "ఆందోళన" జిల్లాలు) దశాబ్ద నిరోధక-విద్రోహ వ్యూహం శీర్ష సాధన — 2004 నుండి (626 జిల్లా) దాదాపు శమనం. సమర్థకం: అభివృద్ధి (ఖనిజ రాయల్టీ, వన హక్కులు), నిర్బంధం (సైన్య బలాలు), స్థానిక నిర్వహణ (కర్తవ్యం). <b>ప్రాంతీయ విభేదాలు:</b> AP అల్లూరి సీతారామ రాజు (APSC నిరసన చేరి గ్రాండ్‌సన్ పేరు) బాక్సైట్광, బోడం ఖాళీ నిందన. TS భద్రాద్రి కొత్తగూడెం, ములుగు భూ-యాజమానూరు. <b>అంతర్నిర్వహణ సమానత్వం:</b> భారత్ సంస్థానిక సమరూపత: కేంద్ర సామర్థ్యం విద్రోహ నిరోధకం అయితే ఖనిజ నియంత్రణ సక్షమ — ఎక్సెషన్ నిర్ణయ సమానత్వ సవాల్.</p>

<div class="section-hdr">NITI Higher Education Internationalisation / ఉన్నత విద్య అంతర్జాతీయీకరణ</div>
<table class="key-table">
<tr><th>Stat</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Report date</td><td>December 22, 2025</td><td class="bi-te">డిసెంబర్ 22, 2025</td></tr>
<tr><td>Indian students abroad (2024)</td><td>13.35 lakh</td><td class="bi-te">విదేశాల్లో భారత విద్యార్థులు (2024): 13.35 లక్షలు</td></tr>
<tr><td><b>AP rank</b></td><td><b>1st</b> in students going abroad — 62,771 (in 2018)</td><td class="bi-te"><b>AP</b> విదేశాలకు వెళ్లే విద్యార్థులలో <b>1వ</b> — 62,771 (2018)</td></tr>
<tr><td>India's annual spend</td><td>~$70 billion on overseas education</td><td class="bi-te">భారత్ సాలీనా ~$70 బిలియన్</td></tr>
</table>

<div class="section-hdr">Education Reforms / విద్యా సంస్కరణలు</div>
<p><b>Higher Education Autonomy & Research Institutional Elevation:</b> NCERT's Deemed-to-be-University status (2026) elevates India's pedagogy research institution into research university framework — enabling degree-awarding autonomy, faculty hiring flexibility, and research funding access critical for NEP 2020's "teacher as researcher" goal. This signals government's shift toward institutional autonomy models (similar to IIT/IIM independence) targeting world university rankings while maintaining national curriculum standards. <b>Linguistic Pluralism & Constitutional Federalism:</b> CBSE's mandated 3-language policy from Class 6 (2026-27) operationalizes NEP 2020's multilingual education doctrine — 8th Schedule recognition of regional languages (22 constitutionally recognized) alongside English and one classical language. This counters north-south polarization over language policy (Hindi imposition fears in southern states, English dominance). The policy is directly responsive to Telangana, Andhra Pradesh's medium-of-instruction anxieties and Sanskrit/classical language revival goals while protecting English's global competitiveness necessity. <b>State-level Variation:</b> CBSE's flexibility allows state-specific language combinations (AP: Telugu-English-Sanskrit; TS: Urdu-English-Telugu options) reflecting federal structure's language autonomy principles — crucial for minority language preservation and multilingual workforce development aligned with India's economic diversification demands.</p>
<p class="bi-te"><b>ఉన్నత విద్య స్వయంత్రత:</b> NCERT Deemed-to-be-University హోదా (2026) —  గవేషణ విశ్వవిద్యాలయ చట్రం; డిగ్రీ-ఎనిమిషన్ స్వయంత్రత, సంకాయ నియ్బంధన సరళత, గవేషణ నిధులు NEP 2020 "ఉపాధ్యాయుడు-గవేషణకర్త" లక్ష్యం. IIT/IIM మডల్ స్వయంత్రత; ప్రపంచ ర‌ంకింగ్‌ సవాయ. <b>భాషా బహువర్ణవాదం:</b> CBSE 3-భాష నిర్బంధం (2026-27, తరగతి 6) NEP 2020 బహుభాషిక సిద్ధాంతం — 8వ అనుసూచిక ప్రాంతీయ (22 రాజ్యాంగ గుర్తించిన) + ఇంగ్లీష్ + వర్గీయ భాష. హిందీ అధిరోపణ భయం (దక్షిణ) నిరసన; ఇంగ్లీష్ ఆధిపత్య సమీకరణ. TS, AP మాధ్యమ-నిర్ధారణ, సంస్కృతం పୁନర్ప్రতిష్ఠ. <b>రాష్ట్ర నమూనా:</b> CBSE సరళత — AP: తెలుగు-ఇంగ్లీష్-సంస్కృతం; TS: ఉర్దూ-ఇంగ్లీష్-తెలుగు అపెక్షలు. సంఘీయ భాష-స్వయంత్రత; సంఘీయ ఆర్థిక వైవిధ్యీకరణ-సంబంధితం.</p>

<div class="section-hdr">Akshaya Patra 500 Crore Meals / అక్షయ పాత్ర 500 కోట్ల భోజనాలు</div>
<p><b>Social Welfare & Nutrition Security Implementation:</b> Akshaya Patra Foundation's 500-crore meal milestone (March 17, 2026) represents India's largest private-sector-led school nutrition programme — complementing government's Mid Day Meal Scheme implementation. Operating across 18,000+ schools in 13 states, it serves ~2 million students daily, primarily from SC/ST and economically-disadvantaged backgrounds. The cumulative 5-billion meals (since 2000) directly addresses India's persistent malnutrition (39% of children stunted, per NFHS-5), improving school attendance and learning outcomes — critical for SDG 2 (Zero Hunger) and SDG 4 (Quality Education) integration. <b>CSR-Governance Hybrid Model:</b> Akshaya Patra exemplifies India's public-private partnership ecosystem for welfare provision — corporate donors (IKEA Foundation, Infosys Foundation) fund operations while government provides infrastructure. This model enables scale (5 billion meals) beyond government capacity while maintaining quality standardization and nutritional compliance. <b>Regional Development & Gender Impact:</b> Telangana and Andhra Pradesh are major beneficiaries — Tamil Nadu's historical nutrition deficit reduction due to MDMS-Akshaya Patra synergy shows effective state-NGO collaboration model replicable across undernutrition zones, directly impacting girl-child education enrollment (gender parity in school nutrition access).</p>
<p class="bi-te"><b>సామాజిక సమృద్ధి &amp; పోషకాహారం సంరక్షణ:</b> అక్షయ పాత్ర 500 కోట్ల భోజనాల మైలురాయి (మార్చి 2026) — 18,000+ పాఠశాలాలు, 13 రాష్ట్రాలు, ~2 మిలియన్ విద్యార్థులు రోజూ. SC/ST, ఆర్థిక పిన్నవర్గాలు. 5-బిలియన్ భోజనాలు (2000 నుండి) భారత్ అవపోషకత (39% బాలలు stunted, NFHS-5) నిరసన; పాఠశాల హాజరు, జ్ఞానార్థన ఫలితాలు — SDG 2 (ఆకలి-రహితం), SDG 4 (విద్య సమానత్వం) ఏకీకరణ. <b>CSR-నిర్వహణ సంకర నమూనా:</b> దాతృత్వ (IKEA, Infosys) నిధులు; ప్రభుత్వ బలభూతం. స్కేల్ ఐచిక్కం, ప్రభుత్వ సామర్థ్యం అతిక్రమణ. పోషణ సమీకరణ. <b>ప్రాంతీయ అభివృద్ధి &amp; లింగ ప్రభావం:</b> TS, AP అతిపెద్ద లాభార్థీలు — తమిళనాడు అవపోషకత తగ్గింపు MDMS-Akshaya Patra సహకార నమూనా; TS/AP శాలాలు స్త్రీ-బాల విద్య, భోజన-ఆచార నిఛయం (లింగ సమానత్వ స్కూల్ పోషణ).</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  13. NFHS / Total Fertility Rate (TFR) — Population Data
#  Linked from MCQs 31014-31015
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_nfhs_tfr',
              'NFHS — India Total Fertility Rate (TFR)',
              'NFHS — భారత సంతానోత్పత్తి రేటు (TFR)', """
<div class="concept-cover">
  <h1>NFHS &amp; India's Total Fertility Rate &nbsp;<span class="bi-te">/ NFHS &amp; భారత TFR</span></h1>
  <div class="sub">India TFR 2.1 (replacement) • S. India well below • Implications for 2026 delimitation</div>
</div>

<div class="section-hdr">India's TFR — Key Numbers / భారత TFR కీలక గణాంకాలు</div>
<table class="key-table">
<tr><th>Region / State</th><th>TFR (NFHS-5, 2019-21)</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>India (national average)</b></td><td><b>2.0–2.1</b> (replacement level)</td><td class="bi-te">భారత TFR — జనాభా స్థిరీకరణ స్థాయి</td></tr>
<tr><td>Andhra Pradesh</td><td>1.7</td><td class="bi-te">ఆంధ్రప్రదేశ్</td></tr>
<tr><td><b>Telangana</b></td><td><b>1.6</b></td><td class="bi-te">తెలంగాణ — జాతీయ సగటు కంటే తక్కువ</td></tr>
<tr><td>Tamil Nadu</td><td>1.8</td><td class="bi-te">తమిళనాడు</td></tr>
<tr><td>Kerala</td><td>1.8</td><td class="bi-te">కేరళ</td></tr>
<tr><td>Karnataka</td><td>1.7</td><td class="bi-te">కర్ణాటక</td></tr>
<tr><td>Uttar Pradesh</td><td>2.4</td><td class="bi-te">ఉత్తరప్రదేశ్</td></tr>
<tr><td>Bihar</td><td>3.0 (highest)</td><td class="bi-te">బిహార్ — అత్యధికం</td></tr>
</table>

<div class="section-hdr">What is TFR? / TFR అంటే ఏమిటి?</div>
<p><b>Demographic Transition & Development Correlation:</b> Total Fertility Rate (TFR) = average children per woman in reproductive years. 2.1 is the population replacement level — below this, population stabilizes (without migration). India's TFR drop to 2.0-2.1 nationally (NFHS-5) represents completion of demographic transition from high fertility to stability — typically occurring at $4,000-5,000 per-capita GDP. This milestone has major policy implications: <b>India's Age Dividend Closing:</b> TFR decline means India's young population advantages (400 million under-18) will peak ~2030s, then age rapidly — requiring urgent pension, healthcare, and elder-care policy reforms before the 2040s "aging crisis." <b>Regional Divergence & Equity Concerns:</b> Telangana (1.6) and AP (1.7) have reached sub-replacement fertility while Bihar (3.0) and UP (2.4) remain well above — a 1.4 TFR differential correlates with education gap (TS female literacy 68.5% vs Bihar 53%). This creates divergent population pressures: South India's stagnating workforce supply vs North India's rapid growth straining infrastructure, education, employment — central to India's regional balancing and inter-state resource allocation (16th FC). <b>Census 2026 Implications:</b> TFR data directly feeds delimitation exercise (reapportionment of Lok Sabha seats based on population ratios) — South's declining TFR = slower Lok Sabha seat growth, reinforcing northern states' legislative dominance, a long-standing southern state grievance.</p>
<p class="bi-te"><b>జనాభా-పరిణామం &amp; అభివృద్ధి సంబంధం:</b> TFR = ఒక మహిళ పంది సంతానోత్పత్తి. 2.1 = స్థిరీకరణ స్థాయి. భారత్ TFR 2.0-2.1 (NFHS-5) పూర్ణ జనాభా-పరిణామం (highనుండి స్థిరీకరణ) — సాధారణంగా $4,000-5,000 తలసరి GDP. <b>భారత్ వయసు-పూర్ణ అంతిమం:</b> TFR పతనం = 400 మిలియన్ under-18 శిఖరం 2030లు; then వయస్సు-త్వరణం — పென్షన్, ఆరోగ్యం, వృద్ధ-సంరక్షణ 2040 "aging సంకట" ముందుగా. <b>ప్రాంతీయ విభేదం &amp; సమానత్వ భాషా:</b> TS (1.6), AP (1.7) = sub-replacement; బిహార్ (3.0), UP (2.4) పై. 1.4 TFR తేడా విద్య చేరికకు సంబంధం (TS స్త్రీ సాక్షరత 68.5% vs బిహార్ 53%). జనాభా ఒత్తిడి: దక్షిణ-శ్రమశక్తి సరఫరా స్థిరీకరణ vs ఉత్తర-వేగవృద్ధి బుణ-సెవా ఒత్తిడి — india's ప్రాంతీయ సమీకరణ, inter-state సంపద కేటాయింపు (16th FC). <b>Census 2026 సూచనలు:</b> TFR డేటా డీలిమిటేషన్‌కు నేరుగా (జనాభా-రిపోర్ట్ నిేసరణ) — దక్షిణ TFR = నెమ్నెమ్ సీట్ వృద్ధి, ఉత్తర-రాష్ట్ర చట్టపరమైన ఆధిపత్య శక్తిపరీకరణ, దక్షిణ-రాష్ట్ర స్వచ్ఛంద అభిఘాతం.</p>

<div class="section-hdr">NFHS — National Family Health Survey / జాతీయ కుటుంబ ఆరోగ్య సర్వే</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Conducted by</td><td>MoHFW + IIPS (Mumbai) + ICF Macro</td><td class="bi-te">కేంద్ర ఆరోగ్య మంత్రిత్వ శాఖ + IIPS</td></tr>
<tr><td>Latest round</td><td>NFHS-5 (2019-21)</td><td class="bi-te">NFHS-5</td></tr>
<tr><td>Covers</td><td>Fertility, mortality, contraception, nutrition, women's health</td><td class="bi-te">సంతానోత్పత్తి, మరణాలు, పోషకాహారం</td></tr>
<tr><td>Sample</td><td>~6.4 lakh households</td><td class="bi-te">~6.4 లక్షల ఇళ్లు</td></tr>
</table>

<div class="section-hdr">Why this matters / ఇది ఎందుకు ముఖ్యం?</div>
<p>The TFR gap between North (UP/Bihar) and South (TN/KL/TS/AP) is at the heart of the <b>2026 delimitation debate</b>. After the next Census, LS seats may be reallocated based on population — Northern states stand to gain seats; Southern states (which controlled population growth) stand to lose proportional representation. AP/TS Chief Ministers have raised concerns publicly.</p>
<p class="bi-te">ఉత్తర-దక్షిణ TFR అంతరం 2026 delimitation చర్చకు మూలం. Census తర్వాత LS స్థానాలు జనాభా ఆధారంగా పునఃకేటాయించబడితే — జనాభా నియంత్రణ చేసిన దక్షిణ రాష్ట్రాలు (AP/TS/TN/KL) ఎక్కువ సీట్లు కోల్పోయే ప్రమాదం. AP/TS ముఖ్యమంత్రులు ఈ విషయంలో ఆందోళన వ్యక్తం చేస్తున్నారు.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  14. WAVES 2025 — World Audio Visual Summit (Mumbai)
#  Linked from MCQs 31016-31017
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_waves_summit',
              'WAVES 2025 — World Audio Visual & Entertainment Summit',
              'WAVES 2025 — ప్రపంచ ఆడియో విజువల్ సమ్మిట్', """
<div class="concept-cover">
  <h1>WAVES 2025 &nbsp;<span class="bi-te">/ WAVES 2025 సమ్మిట్</span></h1>
  <div class="sub">Mumbai • May 1-4, 2025 • Theme: Connecting Creators, Connecting Countries</div>
</div>

<div class="section-hdr">WAVES 2025 — Key Facts / కీలక వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full form</td><td><b>W</b>orld <b>A</b>udio <b>V</b>isual &amp; <b>E</b>ntertainment <b>S</b>ummit</td><td class="bi-te">ప్రపంచ ఆడియో విజువల్ & ఎంటర్‌టైన్‌మెంట్ సమ్మిట్</td></tr>
<tr><td>Host city</td><td><b>Mumbai</b> (India's media capital)</td><td class="bi-te">ముంబై — భారత మీడియా రాజధాని</td></tr>
<tr><td>Dates</td><td>May 1-4, 2025 (4 days)</td><td class="bi-te">మే 1-4, 2025</td></tr>
<tr><td>Inaugurated by</td><td>PM Narendra Modi</td><td class="bi-te">PM నరేంద్ర మోదీ ప్రారంభించారు</td></tr>
<tr><td>Theme</td><td><b>'Connecting Creators, Connecting Countries'</b></td><td class="bi-te">'క్రియేటర్లను కలుపుతూ, దేశాలను కలుపుతూ'</td></tr>
<tr><td>Countries</td><td>~80 countries participated</td><td class="bi-te">~80 దేశాలు పాల్గొన్నాయి</td></tr>
<tr><td>Significance</td><td>India's <b>first</b> global summit dedicated to M&amp;E sector</td><td class="bi-te">భారత తొలి అంతర్జాతీయ M&E సమ్మిట్</td></tr>
</table>

<div class="section-hdr">India's M&amp;E Sector — Stats / భారత M&E రంగం</div>
<table class="key-table">
<tr><th>Item</th><th>Value</th></tr>
<tr><td>Current size (2024)</td><td>~$28 billion</td></tr>
<tr><td>2030 target</td><td><b>$100 billion</b></td></tr>
<tr><td>Workforce</td><td>~25 lakh jobs (direct + indirect)</td></tr>
<tr><td>Growth rate</td><td>~10% CAGR</td></tr>
</table>

<div class="section-hdr">Pavilions &amp; Highlights / ముఖ్యాంశాలు</div>
<p>WAVES 2025 had dedicated pavilions for <b>VFX, Animation, Gaming, OTT, Music, Films, News &amp; Broadcasting</b>. The "Bharat Pavilion" showcased India's creative economy. Inaugural <b>Creator Awards</b> were instituted to recognise digital content creators.</p>
<p class="bi-te">WAVES 2025లో VFX, యానిమేషన్, గేమింగ్, OTT, సంగీతం, సినిమా, వార్తల కోసం ప్రత్యేక పెవిలియన్లు ఉన్నాయి. "భారత్ పెవిలియన్" — భారత సృజనాత్మక ఆర్థిక వ్యవస్థను చూపించింది. ప్రారంభ Creator Awards ప్రారంభించారు.</p>

<div class="section-hdr">Why it matters / ఇది ఎందుకు ముఖ్యం?</div>
<p><b>Creative Economy & Soft Power Positioning:</b> WAVES 2025 (Mumbai, May 1-4) positions India as a global M&E powerhouse alongside Hollywood (USA), Hallyu (Korea), and content giants like China & Japan. The $28 billion M&E sector (targeting $100 billion by 2030) represents India's emerging "creator economy" — critical for competing in digital-native, Gen-Z entertainment markets. <b>Global Content & International Co-Productions:</b> WAVES's "Connecting Creators, Connecting Countries" theme emphasizes international co-productions, IP rights, content distribution networks — areas where Indian creatives (Bollywood, OTT, VFX studios) lack global scale parity. 80-country participation signals soft power expansion; VFX pavilion highlights India's $10+ billion VFX industry (servicing 70% of Hollywood VFX outsourcing). <b>Digital Infrastructure & Economic Impact:</b> Creator Awards and OTT focus recognize India's 500+ original web series ecosystem — parallel to traditional cinema. The summit drives FDI in content infra (studios, editing facilities), gaming ecosystem ($2.7bn sector), and digital creator training — aligned with NEP 2020's skill-building and India's 25 lakh M&E workforce growth targets.</p>
<p class="bi-te"><b>సృజనాత్మక ఆర్థిక &amp; సాఫ్ట్ పవర్:</b> WAVES ముంబై (మే 2025) భారత్‌ను హాలీవుడ్, కోరియా, చైనా/జపాన్‌లకు సమానమైన M&E కేంద్రం. $28 బిలియన్ M&E ($100 బిలియన్ 2030 లక్ష్యం) "creator economy" — Gen-Z డిజిటల్ వিనోద సంస్కృతిలో. <b>అంతర్జాతీయ co-production &amp; IP హక్కులు:</b> "సృజనశీలులను కలుపుతూ, దేశాలను కలుపుతూ" థీమ్ co-productions, IP, వితరణ నెట్‌వర్కులు — బాలీవుడ్, OTT, VFX స్కేల్ పరిమితి. 80 దేశాలు soft power. VFX పవిలియన్ భారత్ $10+ బిలియన్ VFX (హాలీవుడ్ 70% అవుట్‌సోర్సింగ్). <b>డిజిటల్ సంక్షేత్రం:</b> Creator Awards, OTT 500+ వెబ్ సిరీజ్‌లు గుర్తింపు. studios, సవరణ సంస్థలు, గేమింగ్ ($2.7బిలియన్) FDI; 25 లక్ష M&E శ్రమశక్తి వృద్ధి NEP 2020 నైపుణ్య లక్ష్యం.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  15. NAVAL DEFENCE & MARITIME SECURITY 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_naval_defense',
              'Naval Defence & Maritime Security 2026',
              'నావికా రక్షణ & సముద్ర భద్రత 2026', """
<div class="concept-cover">
  <h1>Naval Defence &amp; Maritime Security 2026 &nbsp;<span class="bi-te">/ నావికా రక్షణ 2026</span></h1>
  <div class="sub">MILAN 2026 (Vizag) • S-4 SSBN • P-75I • Hormuz chokepoint</div>
</div>

<div class="section-hdr">MILAN 2026 — Multilateral Naval Exercise / MILAN 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full form</td><td><b>M</b>ultilateral <b>I</b>nteraction (originally 'Multilateral Naval Exercise')</td><td class="bi-te">బహుపాక్షిక నావికా విన్యాసం</td></tr>
<tr><td>Host city</td><td><b>Visakhapatnam</b>, Andhra Pradesh</td><td class="bi-te">విశాఖపట్నం, ఆంధ్రప్రదేశ్</td></tr>
<tr><td>Dates</td><td>February 17-25, 2026</td><td class="bi-te">ఫిబ్రవరి 17-25, 2026</td></tr>
<tr><td>Countries</td><td><b>50+ navies</b> (74 nations across MILAN + IFR + IONS)</td><td class="bi-te">50కి పైగా నౌకాదళాలు</td></tr>
<tr><td>Theme</td><td>'United Through Oceans'</td><td class="bi-te">'మహాసముద్రాల ద్వారా ఏకతా'</td></tr>
<tr><td>Frequency</td><td>Biennial (every 2 years), hosted by Indian Navy</td><td class="bi-te">రెండు సం. కోసారి, భారత నౌకాదళం</td></tr>
<tr><td>Special 2026</td><td>First joint hosting with IFR + IONS Symposium</td><td class="bi-te">తొలి IFR + IONS సమ్మిళిత నిర్వహణ</td></tr>
</table>

<div class="section-hdr">INS S-4 / Arihant-class SSBN / S-4 జలాంతర్గామి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Class</td><td><b>Arihant-class</b> — 4th boat</td><td class="bi-te">అరిహంత్ శ్రేణి, 4వ నౌక</td></tr>
<tr><td>Category</td><td><b>SSBN</b> = Ship Submersible Ballistic Nuclear (nuclear-powered)</td><td class="bi-te">అణు-శక్తి బాలిస్టిక్ క్షిపణి జలాంతర్గామి</td></tr>
<tr><td>Builder</td><td>Ship Building Centre, Visakhapatnam</td><td class="bi-te">ఓడల నిర్మాణ కేంద్రం, విశాఖపట్నం</td></tr>
<tr><td>Significance</td><td>Strengthens India's <b>nuclear triad</b> (land, air, sea)</td><td class="bi-te">భారత అణు త్రయాన్ని బలోపేతం</td></tr>
</table>

<div class="section-hdr">Project P-75I / ప్రాజెక్ట్ P-75I</div>
<p><b>P-75I</b> = <b>6 advanced diesel-electric submarines</b> with AIP (Air-Independent Propulsion) technology under the Make-in-India initiative, built at MDL Mumbai with German ThyssenKrupp Marine Systems collaboration. The earlier <b>P-75 Scorpene class</b> delivered 6 boats (INS Kalvari series).</p>
<p class="bi-te">P-75I — AIP టెక్నాలజీతో 6 అత్యాధునిక డీజిల్-ఎలక్ట్రిక్ జలాంతర్గాములు, MDL ముంబై వద్ద జర్మన్ సహకారంతో నిర్మాణం. మునుపటి P-75 స్కార్పీన్ — 6 నౌకలు (INS కల్వరి శ్రేణి).</p>

<div class="section-hdr">Strait of Hormuz — Strategic Chokepoint / హర్ముజ్ జలసంధి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Location</td><td>Between <b>Iran (north)</b> and <b>Oman (south, Musandam exclave)</b></td><td class="bi-te">ఇరాన్ - ఒమాన్ మధ్య</td></tr>
<tr><td>Connects</td><td>Persian Gulf — Gulf of Oman — Arabian Sea</td><td class="bi-te">పర్షియన్ గల్ఫ్ — అరేబియా సముద్రం</td></tr>
<tr><td>Width</td><td>~33 km at narrowest</td><td class="bi-te">అతి సన్నని భాగం ~33 కి.మీ</td></tr>
<tr><td>Oil traffic</td><td>~20% of global oil + 30% of seaborne crude passes through</td><td class="bi-te">ప్రపంచ చమురులో ~20% ఇక్కడ నుండి</td></tr>
</table>

<div class="section-hdr">Defence Budget &amp; Sector / రక్షణ బడ్జెట్</div>
<p><b>Defence Spending & Naval-Centric Strategy:</b> Union Budget 2026-27's defence allocation (Rs.7.85 lakh crore, +15% YoY) positions India as the world's 3rd-largest defence spender (after USA, China) — reflecting India's Indo-Pacific strategic realignment. The allocation emphasizes naval modernization (SSBN S-4, P-75I submarines, destroyer programs) aligning with India's maritime-centric power projection (Indian Ocean strategic autonomy). Defence exports crossed Rs.21,000 crore in 2024-25 — a 150% jump vs 2019-20 — signaling India's defence manufacturing maturity. <b>MILAN 2026 & Multilateral Naval Diplomacy:</b> MILAN 2026 (Visakhapatnam, Feb 17-25, 50+ navies) represents India's orchestration of Indian Ocean strategic coalitions — distinct from China's bilateral port-state security model. The "United Through Oceans" theme operationalizes India's maritime doctrine: freedom of navigation, countering piracy (Houthi Red Sea disruptions), and building Blue-Economy leadership. India's Navy role in Op Sankalp (anti-piracy escort, 2019-present) demonstrates credible sea-lane security provision. <b>Strategic Implications:</b> Hormuz's 33-km chokepoint controlling 20% global oil + 30% seaborne crude illustrates energy security criticality for India's 5.4% annual crude import bill ($25 billion annually). Naval modernization (SSBN, P-75I) addresses submarine deterrence against Pakistan/China and ensures uninterrupted maritime trade connectivity — essential for India's $800+ billion merchandise trade dependent on sea routes.</p>
<p class="bi-te"><b>రక్షణ ఖర్చు &amp; నౌకా వ్యూహం:</b> 2026-27 బడ్జెట్ రక్షణ (7.85 ల.కో., +15%) భారత్ 3వ అతిపెద్ద రక్షణ ఖర్చుదారు — Indo-Pacific వ్యూహాత్మక పలాయనం. నౌకా ఆధునికీకరణ (SSBN S-4, P-75I, destroyer) భారత సముద్ర శక్తి-కేంద్రిక. 2024-25 రక్షణ ఎగుమతులు రూ.21,000 కో. (2019-20 నుండి 150% జంప్) భారత తయారీ పరిపక్వత. <b>MILAN 2026 బహుపాక్షిక నౌకా దౌత్యం:</b> MILAN (విశాఖపట్నం, ఫిబ్ర. 17-25, 50+ నౌకాదళాలు) భారత్ Indian Ocean సంకీర్ణ ప్రచారం — చైనా ద్వైపాక్షిక బంદర-రాష్ట్ర నమూనాకు విభిన్నం. "సముద్రాల ద్వారా ఏకతా" — నౌకా చర్య స్వేచ్ఛ, దోపిడీ నిరోధకం (హూతీ Red Sea), నీలలోక నేతృత్వం. Op Sankalp anti-piracy భారత నౌకా-ఆధారిత సముద్ర-లేన సంరక్షణ సాధ్యత. <b>వ్యూహాత్మక సూచనలు:</b> హర్ముజ్ జలసంధి (33 కి.మీ) ప్రపంచ చమురులో 20% + సముద్ర 30% నియంత్రణ — భారత్ సంవత్సరానికి 5.4% కమ్యూయూ దిగుమతుల $25 బిలియన్ బిల్లు. నౌకా ఆధునికీకరణ (SSBN, P-75I) పాకిస్తాన్/చైనా జలాంతర్గామ నిరోధం; సముద్ర-మార్గ వాణిజ్య నిరంతరత్వం — భారత $800+ బిలియన్ వస్తు వాణిజ్య సముద్ర-ఆధారిత.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  16. CRICKET & SPORTS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_cricket_sports',
              'Cricket & Sports 2026',
              'క్రికెట్ & క్రీడలు 2026', """
<div class="concept-cover">
  <h1>Cricket &amp; Sports 2026 &nbsp;<span class="bi-te">/ క్రికెట్ & క్రీడలు 2026</span></h1>
  <div class="sub">U19 WC • WTC Final • Asian Games Nagoya</div>
</div>

<div class="section-hdr">ICC U19 Cricket World Cup 2026 / U19 ప్రపంచ కప్ 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Winner</td><td><b>India</b> (record extending title)</td><td class="bi-te">విజేత: భారత్</td></tr>
<tr><td>Edition</td><td>15th ICC U19 Men's Cricket World Cup</td><td class="bi-te">15వ ఎడిషన్</td></tr>
<tr><td>India's titles</td><td>Most-ever U19 World Cup titles</td><td class="bi-te">అత్యధిక U19 టైటిళ్లు</td></tr>
</table>

<div class="section-hdr">ICC World Test Championship Final 2025 / WTC ఫైనల్ 2025</div>
<p><b>India</b> won the 2025 ICC World Test Championship Final at Lord's, capping a 2-year cycle. The WTC is cricket's premier Test format championship (launched 2019-21 cycle by ICC).</p>
<p class="bi-te">భారత్ 2025 ICC వరల్డ్ టెస్ట్ ఛాంపియన్‌షిప్ ఫైనల్ లార్డ్స్‌లో గెలిచింది. WTC ICC టెస్ట్ ఫార్మాట్ ప్రధాన ఛాంపియన్‌షిప్ (2019-21 సైకిల్ నుండి ప్రారంభం).</p>

<div class="section-hdr">2026 Asian Games — Nagoya, Japan / 2026 ఆసియా క్రీడలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Host</td><td><b>Nagoya, Japan</b> (Aichi prefecture)</td><td class="bi-te">నాగోయా, జపాన్</td></tr>
<tr><td>Edition</td><td>20th Asian Games</td><td class="bi-te">20వ ఆసియా క్రీడలు</td></tr>
<tr><td>Organising body</td><td>OCA (Olympic Council of Asia)</td><td class="bi-te">ఆసియా ఒలింపిక్ కౌన్సిల్</td></tr>
<tr><td>Previous</td><td>Hangzhou 2022 (held Sep 2023) — India won 107 medals (28G/38S/41B)</td><td class="bi-te">హాంగ్‌ఝౌ 2022 — భారత్‌కు 107 పతకాలు</td></tr>
</table>
<p>Sports is a state subject in India with a Union Ministry of Youth Affairs &amp; Sports. <b>Khelo India</b> and <b>TOPS (Target Olympic Podium Scheme)</b> support elite athletes. India hosts the <b>Khelo India Youth Games</b> annually.</p>
<p class="bi-te">క్రీడలు రాష్ట్ర అంశం, కేంద్ర యువజన వ్యవహారాలు & క్రీడల మంత్రిత్వ శాఖ ఉంది. ఖేలో ఇండియా, TOPS క్రీడాకారులకు మద్దతు. ఖేలో ఇండియా యూత్ గేమ్స్ ప్రతి సం. జరుగుతాయి.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  17. FOREIGN RELATIONS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_foreign_relations',
              'India Foreign Relations 2026',
              'భారత విదేశీ సంబంధాలు 2026', """
<div class="concept-cover">
  <h1>India Foreign Relations 2026 &nbsp;<span class="bi-te">/ భారత విదేశీ సంబంధాలు 2026</span></h1>
  <div class="sub">Lula visit • Trump tariffs • Gaza ceasefire • SCO • India-China LAC</div>
</div>

<div class="section-hdr">Brazil — Lula's India Visit / బ్రెజిల్ - లులా పర్యటన</div>
<p><b>Luiz Inácio Lula da Silva</b>, President of Brazil, visited India in <b>March 2026</b> as Chief Guest. Met PM Modi for bilateral talks covering trade, technology, BRICS coordination, and defence. Brazil-India trade target: <b>$20 billion by 2030</b>. Brazil held G20 Presidency in 2024.</p>
<p class="bi-te">బ్రెజిల్ అధ్యక్షుడు లులా డి సిల్వా మార్చి 2026లో భారత్ సందర్శించారు, PM మోడీతో వాణిజ్యం, టెక్నాలజీ, BRICS, రక్షణ గురించి చర్చలు. వాణిజ్య లక్ష్యం: 2030 నాటికి $20 బిలియన్లు. 2024లో బ్రెజిల్ G20 అధ్యక్షత.</p>

<div class="section-hdr">India-USA — Trump Tariffs 2026 / భారత్-USA</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Trigger</td><td>Trump 2.0 (Jan 2025) imposed reciprocal &amp; sector tariffs</td><td class="bi-te">ట్రంప్ 2.0 — పరస్పర సుంకాలు</td></tr>
<tr><td>India tariffs</td><td>26-50% on select sectors (steel, auto, pharma intermediates)</td><td class="bi-te">ఎంపిక చేసిన రంగాలపై 26-50%</td></tr>
<tr><td>India response</td><td>Bilateral renegotiation talks; partial countermeasures</td><td class="bi-te">ద్వైపాక్షిక చర్చలు</td></tr>
<tr><td>Trade</td><td>USA = India's largest trading partner (~$130 bn bilateral)</td><td class="bi-te">USA — భారత అతిపెద్ద వాణిజ్య భాగస్వామి</td></tr>
</table>

<div class="section-hdr">Israel-Hamas Gaza Ceasefire (Feb 2026) / గాజా కాల్పుల విరమణ</div>
<p>The phased Israel-Hamas ceasefire deal of <b>February 2026</b> was mediated by <b>Qatar, Egypt, and USA</b>. It provided for hostage release, prisoner exchange, and aid corridors. India backs the <b>two-state solution</b> for Palestine.</p>
<p class="bi-te">ఇజ్రాయెల్-హమాస్ ఫిబ్రవరి 2026 ఒప్పందానికి కతర్, ఈజిప్ట్, USA మధ్యవర్తిత్వం. బందీల విడుదల, ఖైదీల మార్పిడి, సహాయ మార్గాలు. భారత్ ద్వి-రాష్ట్ర పరిష్కారానికి మద్దతు.</p>

<div class="section-hdr">SCO Summit 2025 / SCO శిఖరం 2025</div>
<p><b>SCO</b> (Shanghai Cooperation Organisation) 2025 Summit theme = <b>'Upholding the Shanghai Spirit'</b>, hosted by China. SCO has 10 members (incl. India, Pakistan, Iran, Belarus). India joined as full member in 2017.</p>
<p class="bi-te">SCO 2025 సమ్మిళిత థీమ్: 'షాంఘై స్ఫూర్తిని కాపాడడం', చైనా అతిథేయం. SCO లో 10 సభ్యులు (భారత్, పాకిస్తాన్, ఇరాన్, బెలారస్ సహా). 2017లో భారత్ పూర్తి సభ్యత్వం.</p>

<div class="section-hdr">Houthis &amp; Red Sea / హూతీలు & ఎర్ర సముద్రం</div>
<p><b>Houthi rebels</b> (Ansar Allah, Shia Zaydi movement) are based in <b>Yemen</b>, controlling its north including Sana'a. Since late-2023 they attacked commercial vessels in the <b>Red Sea / Bab-el-Mandeb</b>, disrupting Suez Canal trade. India's Navy launched <b>Op Sankalp</b> for anti-piracy escort.</p>
<p class="bi-te">హూతీ తిరుగుబాటుదారులు యెమెన్‌లో ఉన్నారు. 2023 చివరి నుండి ఎర్ర సముద్రంలో నౌకలపై దాడులు, సూయజ్ ట్రాఫిక్ దెబ్బ. భారత నౌకాదళం 'ఆపరేషన్ సంకల్ప్' ద్వారా దోపిడీ నిరోధక గస్తీ.</p>

<div class="section-hdr">India-China LAC Agreement (Oct 2024) / భారత్-చైనా LAC</div>
<p>In <b>October 2024</b>, India and China reached the <b>Galwan Area Patrol (GAP) Agreement</b> restoring patrolling rights at <b>Depsang and Demchok</b> in Eastern Ladakh, ending the 4.5-year standoff that began with the June 2020 Galwan clash. PM Modi met Xi Jinping at Kazan BRICS Summit (Oct 2024).</p>
<p class="bi-te">అక్టోబర్ 2024లో భారత్-చైనా డెప్సాంగ్, డెంచోక్‌ల వద్ద గస్తీ హక్కులు పునరుద్ధరించే ఒప్పందం. జూన్ 2020 గల్వాన్ సంఘర్షణతో ప్రారంభమైన 4.5 సం. ప్రతిష్టంభనకు ముగింపు. కజాన్ BRICS లో మోడీ-జిన్‌పింగ్ సమావేశం.</p>

<div class="section-hdr">G20 Presidency 2025-26 / G20 అధ్యక్షత</div>
<p><b>South Africa</b> holds the G20 Presidency for 2025-26 (after Brazil 2024). Theme: 'Solidarity, Equality, Sustainability'. India hosted G20 in 2023 (New Delhi Declaration).</p>
<p class="bi-te">2025-26 G20 అధ్యక్షత: దక్షిణ ఆఫ్రికా. థీమ్: 'సంఘీభావం, సమానత్వం, స్థిరత్వం'. 2023లో భారత్ అధ్యక్షత (న్యూఢిల్లీ డిక్లరేషన్).</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  18. SPACE & ISRO 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_space_isro',
              'Space & ISRO 2026',
              'అంతరిక్షం & ISRO 2026', """
<div class="concept-cover">
  <h1>Space &amp; ISRO 2026 &nbsp;<span class="bi-te">/ అంతరిక్షం & ఇస్రో 2026</span></h1>
  <div class="sub">Artemis-2 • Shubhanshu Shukla / Axiom-4 • NavIC-16 • Gaganyaan</div>
</div>

<div class="section-hdr">NASA Artemis-2 / NASA ఆర్టెమిస్-2</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Mission</td><td><b>First crewed lunar mission in 50 years</b> (since Apollo 17, Dec 1972)</td><td class="bi-te">50 సం. తర్వాత మానవులతో చంద్రుని మిషన్</td></tr>
<tr><td>Crew</td><td><b>4 astronauts</b>: Reid Wiseman, Victor Glover, Christina Koch, Jeremy Hansen (CSA)</td><td class="bi-te">4 వ్యోమగాములు</td></tr>
<tr><td>Type</td><td>Lunar flyby (no landing)</td><td class="bi-te">చంద్రుని చుట్టూ ప్రయాణం (దిగుట లేదు)</td></tr>
<tr><td>Rocket / Capsule</td><td>SLS (Space Launch System) + Orion capsule</td><td class="bi-te">SLS రాకెట్ + ఓరియన్ క్యాప్సూల్</td></tr>
<tr><td>Next</td><td>Artemis-3 (planned crewed landing 2027)</td><td class="bi-te">ఆర్టెమిస్-3 — క్రూడ్ లాండింగ్ 2027</td></tr>
</table>

<div class="section-hdr">Shubhanshu Shukla — Axiom-4 / శుభాంశు శుక్లా</div>
<p>Indian Air Force Group Captain <b>Shubhanshu Shukla</b> flew as part of <b>Axiom-4 (Ax-4) mission</b> to the ISS in 2025 — the first Indian on the ISS and the first Indian in space since <b>Rakesh Sharma (Soyuz T-11, April 1984)</b>. Axiom Space is a private US firm partnered with SpaceX for crewed ISS missions. Shukla was awarded the <b>Ashok Chakra 2026</b> (highest peace-time gallantry award).</p>
<p class="bi-te">భారత వాయుసేన గ్రూప్ కెప్టెన్ శుభాంశు శుక్లా 2025లో Axiom-4 మిషన్ ద్వారా ISS చేరారు — రాకేశ్ శర్మ (1984) తర్వాత తొలి భారతీయుడు ISS లో. Axiom స్పేస్ — SpaceX భాగస్వామ్యంతో అమెరికా ప్రైవేటు సంస్థ. శుక్లాకు 2026లో అశోక చక్ర.</p>

<div class="section-hdr">ISRO Launches 2026 / ISRO ప్రయోగాలు</div>
<table class="key-table">
<tr><th>Mission</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>NavIC-16 (IRNSS-16)</b></td><td>Launched Jan 2026 via PSLV — strengthens India's regional satellite navigation</td><td class="bi-te">2026 జనవరి PSLV ద్వారా</td></tr>
<tr><td>Gaganyaan</td><td>India's first crewed mission — <b>3 astronauts</b>, targeted 2026-27</td><td class="bi-te">3 వ్యోమగాములు</td></tr>
<tr><td>Chandrayaan-4</td><td>Sample-return mission, late-2020s</td><td class="bi-te">శాంపిల్ తిరిగి తేవు మిషన్</td></tr>
<tr><td>Budget 2026-27</td><td>Rs.13,705 crore for ISRO</td><td class="bi-te">ISRO బడ్జెట్ రూ.13,705 కో.</td></tr>
</table>
<p><b>NavIC</b> = <b>Nav</b>igation with <b>I</b>ndian <b>C</b>onstellation; regional alternative to GPS covering India + 1,500 km buffer; 7-satellite constellation (IRNSS series).</p>
<p class="bi-te">NavIC — భారతీయ ఉపగ్రహాలతో నావిగేషన్; భారత్ + 1,500 కి.మీ. చుట్టు; 7 ఉపగ్రహాల కూటమి (IRNSS శ్రేణి). GPS కి ప్రాంతీయ ప్రత్యామ్నాయం.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  19. ECONOMIC INDICATORS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_economic_indicators',
              'Economic Indicators & Global Rankings 2026',
              'ఆర్థిక సూచికలు & ర్యాంకింగ్‌లు 2026', """
<div class="concept-cover">
  <h1>Economic Indicators &amp; Global Rankings 2026 &nbsp;<span class="bi-te">/ ఆర్థిక సూచికలు 2026</span></h1>
  <div class="sub">WEF Davos • GST • Inflation • HDI • Internet • Census</div>
</div>

<div class="section-hdr">WEF Davos 2026 / WEF దావోస్ 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Edition</td><td><b>56th Annual Meeting</b> of the World Economic Forum</td><td class="bi-te">56వ వార్షిక సమావేశం</td></tr>
<tr><td>Venue / Date</td><td>Davos-Klosters, Switzerland, January 2026</td><td class="bi-te">దావోస్, స్విట్జర్లాండ్ — జనవరి 2026</td></tr>
<tr><td>Founder</td><td>Klaus Schwab (1971)</td><td class="bi-te">క్లాస్ ష్వాబ్ (1971 స్థాపన)</td></tr>
</table>

<div class="section-hdr">Macro Indicators / స్థూల సూచికలు</div>
<table class="key-table">
<tr><th>Indicator</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>GST collections (Dec 2024)</td><td>Rs.2,03,890 crore</td><td class="bi-te">డిసెంబర్ 2024 GST వసూళ్లు</td></tr>
<tr><td>CPI Inflation target</td><td><b>4% ± 2%</b> (RBI flexible target)</td><td class="bi-te">CPI ద్రవ్యోల్బణ లక్ష్యం 4% (±2%)</td></tr>
<tr><td>Repo Rate (2025-26)</td><td>6.5%</td><td class="bi-te">రెపో రేటు 6.5%</td></tr>
<tr><td>Agriculture growth 2024-25</td><td>3.8% (Eco Survey 2025-26)</td><td class="bi-te">వ్యవసాయ వృద్ధి 3.8%</td></tr>
<tr><td>GDP growth target 2026-27</td><td>7%</td><td class="bi-te">GDP లక్ష్యం 7%</td></tr>
</table>

<div class="section-hdr">Global Indices — India's Rank / ప్రపంచ సూచికలలో భారత్</div>
<table class="key-table">
<tr><th>Index</th><th>India's rank</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>HDI 2025</b> (Human Development Index, UNDP)</td><td><b>130 / 193</b></td><td class="bi-te">HDI 130వ స్థానం</td></tr>
<tr><td><b>GHI 2025</b> (Global Hunger Index)</td><td><b>102</b></td><td class="bi-te">GHI 102వ స్థానం</td></tr>
</table>

<div class="section-hdr">Digital India — User Base / డిజిటల్ ఇండియా</div>
<table class="key-table">
<tr><th>Item</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Internet users (2026)</td><td>~60 crore (~600 million)</td><td class="bi-te">ఇంటర్నెట్ వినియోగదారులు ~60 కోట్లు</td></tr>
<tr><td>Social media users (2026)</td><td>~26.5 crore (~265 million)</td><td class="bi-te">సోషల్ మీడియా ~26.5 కోట్లు</td></tr>
<tr><td>Smartphone users</td><td>~70 crore</td><td class="bi-te">స్మార్ట్‌ఫోన్ ~70 కోట్లు</td></tr>
</table>

<div class="section-hdr">Census 2026 / జనాభా గణన 2026</div>
<p>India's <b>Census 2026</b> is the first since 2011 (delayed due to COVID-19). It will be the <b>first digital census</b> via mobile-app enumeration. The Census Act, 1948 governs the exercise; Registrar General of India (RGI) is the nodal body.</p>
<p class="bi-te">2011 తర్వాత తొలి జనాభా గణన (COVID వల్ల ఆలస్యం). మొబైల్ యాప్ ద్వారా తొలి డిజిటల్ జనాభా గణన. భారత రిజిస్ట్రార్ జనరల్ (RGI) నిర్వహణ.</p>

<div class="section-hdr">India AI Mission / ఇండియా AI మిషన్</div>
<p><b>AI Capability Building & Technological Sovereignty:</b> IndiaAI Mission (approved March 2024, Rs.10,372 cr over 5 years) represents India's deliberate AI ecosystem construction — critical for competing against US-China duopoly and building autonomous tech capability. The mission targets compute infrastructure (GPU clusters), foundation models (large language models in Indian languages — crucial for inclusivity and non-English-dominant markets), open datasets (govt agency digitization), and AI skilling (targeting 1 lakh AI professionals by 2026). <b>Strategic Importance for India:</b> AI's application to India's core challenges (agriculture optimization via precision farming, healthcare diagnostics in rural areas, education personalization, Indic language preservation) requires India-specific models vs global foundation models optimized for English-speaking populations. <b>Startup Financing & Innovation Ecosystem:</b> Startup grants (estimated Rs.1,500 cr allocation) target AI applications in agritech, healthtech, fintech — sectors where India has high adoption potential but limited indigenous AI-native startups. This aligns with India's vision to become an "AI-for-good" leader in Global South tech development, differentiating from Western AI focus on consumer entertainment/productivity.</p>
<p class="bi-te"><b>AI సామర్థ్యం నిర్మాణం &amp; సాంకేతిక స్వయంత్రత:</b> ఇండియా AI (మార్చి 2024, 5 సం. రూ.10,372 కో.) కంప్యూట్ సంక్షేత్రం (GPU), ఫౌండేషన్ మోడల్స్ (ఇండిక్ భాషల LLM), డేటాసెట్‌లు, నైపుణ్యం (1 లక్ష AI నిపుణులు). <b>భారత్ ప్రాముఖ్యత:</b> కృషి (ఖచ్చితమైన సాగు), ఆరోగ్యం (గ్రామీణ నిదానం), విద్య (వ్యక్తిగतీకరణ), ఇండిక్ భాషా సంరక్షణ — భారత-నిర్దిష్ట AI మోడల్‌లు. <b>స్టార్టప్ ఫిన్యాన్సింగ్:</b> agritech, healthtech, fintech AI స్టార్టప్‌లు (1,500 కో. అంచనా) — Global South ఫ్రేమ్‌వర్క్, పశ్చిమ AI entertainment-productivity కేంద్రం తో విభేదం.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  20. SOCIAL WELFARE SCHEMES 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_social_welfare_schemes',
              'Social Welfare Schemes & Rural-Urban Development 2026',
              'సామాజిక సంక్షేమ పథకాలు 2026', """
<div class="concept-cover">
  <h1>Social Welfare Schemes 2026 &nbsp;<span class="bi-te">/ సామాజిక సంక్షేమం 2026</span></h1>
  <div class="sub">PMAY-G • MGNREGS • Ayushman Bharat • Health/Education/Rural allocations</div>
</div>

<div class="section-hdr">Union Budget 2026-27 — Welfare Allocations / సంక్షేమ కేటాయింపులు</div>
<table class="key-table">
<tr><th>Scheme/Sector</th><th>Allocation</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Rural Development</td><td>Rs.2,66,808 crore</td><td class="bi-te">గ్రామీణాభివృద్ధి రూ.2.66 ల.కో.</td></tr>
<tr><td>MGNREGS</td><td>Rs.73,000 crore</td><td class="bi-te">MGNREGS రూ.73,000 కో.</td></tr>
<tr><td>Education</td><td>Rs.1,28,650 crore</td><td class="bi-te">విద్య రూ.1.28 ల.కో.</td></tr>
<tr><td>Health</td><td>Rs.98,311 crore</td><td class="bi-te">ఆరోగ్యం రూ.98,311 కో.</td></tr>
<tr><td>Agriculture</td><td>Rs.1,71,437 crore</td><td class="bi-te">వ్యవసాయం రూ.1.71 ల.కో.</td></tr>
</table>

<div class="section-hdr">PMAY-Gramin / PM ఆవాస్ యోజన - గ్రామీణ్</div>
<p><b>PMAY-G</b> (Pradhan Mantri Awaas Yojana - Gramin) launched April 2016 (renamed from IAY) — provides pucca houses to rural poor (BPL). Target: <b>2 crore houses by 2024-29 (Phase-2)</b>. Unit assistance: Rs.1.2 lakh (plain) / Rs.1.3 lakh (hilly). Beneficiaries identified using SECC 2011.</p>
<p class="bi-te">PMAY-G ఏప్రిల్ 2016లో ప్రారంభం (IAY పేరు మార్పు). గ్రామీణ పేదలకు పక్కా ఇళ్లు. లక్ష్యం: 2024-29 ఫేజ్-2లో 2 కోట్ల ఇళ్లు. యూనిట్ సహాయం: రూ.1.2 ల (సాదా) / రూ.1.3 ల (కొండ).</p>

<div class="section-hdr">MGNREGS / మహాత్మా గాంధీ గ్రామీణ ఉపాధి హామీ</div>
<p><b>MGNREGS</b> = Mahatma Gandhi National Rural Employment Guarantee Scheme (Act 2005). Guarantees <b>100 days</b> wage employment per rural household per year. Demand-driven; if work not provided within 15 days, unemployment allowance payable. World's largest social safety net.</p>
<p class="bi-te">MGNREGS — 2005 చట్టం. గ్రామీణ కుటుంబానికి సం. 100 రోజుల వేతన ఉపాధి హామీ. డిమాండ్ ఆధారిత; 15 రోజుల్లో పని ఇవ్వకపోతే నిరుద్యోగ భృతి. ప్రపంచంలో అతిపెద్ద సామాజిక భద్రతా వల.</p>

<div class="section-hdr">Ayushman Bharat — PMJAY / ఆయుష్మాన్ భారత్</div>
<p><b>AB-PMJAY</b> (launched Sep 2018) — world's largest health insurance scheme. Rs.5 lakh per family per year cashless cover for secondary/tertiary care. Original beneficiaries: 12.37 crore poor families (SECC). <b>2024 extension</b>: All citizens <b>aged 70+</b> covered regardless of income (announced by PM Modi, Oct 2024).</p>
<p class="bi-te">AB-PMJAY (సెప్టెం 2018) — ప్రపంచంలో అతిపెద్ద ఆరోగ్య బీమా పథకం. కుటుంబానికి సం. రూ.5 లక్షల కవరేజి. 2024 విస్తరణ: 70 ఏళ్ళు పైబడిన అందరికీ — ఆదాయంతో సంబంధం లేకుండా.</p>

<div class="section-hdr">Welfare Schemes Integration & Social Protection Floors:</div>
<p><b>Universal Social Safety Net Architecture:</b> India's 2026-27 welfare allocation (Rs.2.66 lakh crore rural dev, Rs.73,000 cr MGNREGS, Rs.1.28 lakh cr education) represents systematic construction of universal social protection floors aligned with ILO standards and SDG targets. PMAY-G (2 cr houses Phase-2), MGNREGS (100 days wage), and AB-PMJAY (70+ age coverage expansion) create overlapping safety nets addressing housing-income-health trinity essential for poverty elimination. <b>Targeting & Digitization Through SECC:</b> SECC 2011 (Socio-Economic Caste Census) enables precise beneficiary identification — critical for addressing welfare exclusion/inclusion errors. Digital linkage (Aadhaar, Jan Dhan, mPESA) enables direct benefit transfers, reducing administrative costs and leakage. The 2024 AB-PMJAY expansion to all 70+ citizens (announced October 2024) signals shift from means-tested to rights-based healthcare — a major federalism/equity recalibration prioritizing universal coverage over targeted efficiency. <b>Regional Implementation & State Variation:</b> MGNREGS variations (different wages, project selection across states) and PMAY-G pace disparities (AP/TS faster completion vs northern states) demonstrate federal cooperation challenges in welfare universalization — critical for India's 2030 SDG achievement targets.</p>
<p class="bi-te"><b>సార్వత్రిక సామాజిక భద్రతా నిర్మాణం:</b> 2026-27 సంక్షేమ కేటాయింపులు (గ్రామీణ 2.66 ల.కో., MGNREGS 73,000 కో., విద్య 1.28 ల.కో.) ILO మానకాలు, SDG లక్ష్యాలకు సమానమైన సార్వత్రిక సంరక్షణ. PMAY-G (2 కో. ఇళ్లు), MGNREGS (100 రోజుల వేతన), AB-PMJAY (70+ సార్వత్రిక) పేదరికం సమూలీకరణ. <b>లక్ష్యీకరణ &amp; డిజిటలీకరణ SECC ద్వారా:</b> SECC 2011 ఖచ్చితమైన గుర్తింపు — welfare పీడాపరీడ. డిజిటల్ లింకేజ్ (Aadhaar, Jan Dhan, mPESA) నిప్పుకూలమైన తక్కువ-అంతరాయం సంవితరణ. 2024 AB-PMJAY 70+ సార్వత్రిక (అక్టోబర్ 2024) సంక్షేత్ర-ఆధారిత నుండి హక్కుల-ఆధారిత స్థానభ్రంశం — కేంద్రీయ సమానత్వ కారకం. <b>ప్రాంతీయ నిర్వహణ:</b> MGNREGS విచలనాలు (వేతనాలు, అంచనాలు రాష్ట్రాలకు), PMAY-G వేగం (AP/TS వేగవంత vs ఉత్తర) సంఘీయ సహకార సవాళ్లు — భారత్ 2030 SDG సాధన.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  21. AGRICULTURE & ENVIRONMENT 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_agri_environment',
              'Agriculture, Environment & Renewable Energy 2026',
              'వ్యవసాయం, పర్యావరణం & పునరుత్పాదక శక్తి 2026', """
<div class="concept-cover">
  <h1>Agriculture, Environment &amp; Renewable Energy 2026 &nbsp;<span class="bi-te">/ వ్యవసాయం & పర్యావరణం 2026</span></h1>
  <div class="sub">Agri Rs.1.71 L cr • Net Zero 2070 • 500 GW RE • Jal Jeevan</div>
</div>

<div class="section-hdr">Agriculture — Budget 2026-27 / వ్యవసాయ బడ్జెట్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Allocation</td><td>Rs.1,71,437 crore</td><td class="bi-te">రూ.1.71 ల.కో.</td></tr>
<tr><td>KCC limit hike</td><td>Rs.3 lakh → <b>Rs.5 lakh</b></td><td class="bi-te">కిసాన్ క్రెడిట్ కార్డ్ — రూ.3 ల నుండి రూ.5 లక్షలకు</td></tr>
<tr><td>Bharat-Vistar</td><td>Rs.150 cr AI tool for agriculture</td><td class="bi-te">Bharat-Vistar AI</td></tr>
<tr><td>PM Dhan Dhanya Krishi Yojana</td><td>100 low-yield districts, 1.7 cr farmers</td><td class="bi-te">PM ధన్ ధాన్య కృషి</td></tr>
<tr><td>Pulse Self-Sufficiency Mission</td><td>6-year pulse self-reliance</td><td class="bi-te">పప్పు స్వయం-సమృద్ధి మిషన్</td></tr>
<tr><td>Sector growth 2024-25</td><td>3.8% (Eco Survey)</td><td class="bi-te">వృద్ధి 3.8%</td></tr>
</table>

<div class="section-hdr">Jal Jeevan Mission (JJM) / జల్ జీవన్ మిషన్</div>
<p><b>JJM</b> launched <b>August 15, 2019</b> — aims to provide <b>Functional Household Tap Connection (FHTC) to every rural household</b> by 2024 (extended). Originally 32% rural coverage → over <b>15.7 crore households (~80%)</b> connected by 2025. Joint funding: 50:50 (states), 90:10 (NE/Himalayan), 100% (UTs without legislature).</p>
<p class="bi-te">జల్ జీవన్ మిషన్ — 2019 ఆగస్టు 15. ప్రతి గ్రామీణ గృహానికి కార్యశీల కుళాయి కనెక్షన్. 32% నుండి 80%కి విస్తరణ (15.7 కో. గృహాలు). కేంద్రం-రాష్ట్ర భాగస్వామ్యం 50:50 (సాదా), 90:10 (NE/హిమాలయ), 100% (UTs).</p>

<div class="section-hdr">Climate &amp; Net Zero / వాతావరణ లక్ష్యాలు</div>
<table class="key-table">
<tr><th>Commitment</th><th>Target</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Net Zero</td><td><b>2070</b> (announced COP26 Glasgow 2021)</td><td class="bi-te">2070 నాటికి నికర సున్నా</td></tr>
<tr><td>Renewable energy</td><td><b>500 GW</b> non-fossil capacity by 2030</td><td class="bi-te">2030 నాటికి 500 GW RE</td></tr>
<tr><td>Emissions intensity</td><td>Cut 45% by 2030 (vs 2005)</td><td class="bi-te">2005 ఆధారంతో 45% తగ్గింపు</td></tr>
<tr><td>RE share in elec</td><td>50% from non-fossil by 2030</td><td class="bi-te">2030 నాటికి విద్యుత్ 50% RE</td></tr>
</table>
<p>India is the world's <b>4th-largest installed RE capacity</b> nation. PM Surya Ghar Muft Bijli Yojana (Feb 2024) targets 1 crore rooftop solar households.</p>
<p class="bi-te">ప్రపంచంలో 4వ అతిపెద్ద RE సామర్థ్యం. PM సూర్య ఘర్ ముఫ్త్ బిజ్లీ (ఫిబ్రవరి 2024) — 1 కో. ఇళ్లపై రూఫ్‌టాప్ సోలార్.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  22. EDUCATION & HEALTH 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_education_health',
              'Education & Health — UGC, NMC, NEP 2026',
              'విద్య & ఆరోగ్యం 2026', """
<div class="concept-cover">
  <h1>Education &amp; Health 2026 &nbsp;<span class="bi-te">/ విద్య & ఆరోగ్యం 2026</span></h1>
  <div class="sub">UGC online degrees • NMC • Budget allocations</div>
</div>

<div class="section-hdr">Union Budget 2026-27 — Allocations / కేటాయింపులు</div>
<table class="key-table">
<tr><th>Sector</th><th>Allocation</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Education</td><td>Rs.1,28,650 crore</td><td class="bi-te">విద్య రూ.1.28 ల.కో.</td></tr>
<tr><td>Health</td><td>Rs.98,311 crore</td><td class="bi-te">ఆరోగ్యం రూ.98,311 కో.</td></tr>
</table>

<div class="section-hdr">UGC — Online Degrees / UGC ఆన్‌లైన్ డిగ్రీలు</div>
<p><b>UGC</b> = University Grants Commission (statutory body est. 1956 under UGC Act 1956). In <b>2024</b>, UGC notified regulations recognising <b>online degrees</b> as equivalent to regular degrees for employment and higher studies, provided issued by accredited universities (NAAC A+ or NIRF top 100, or 4+ years operational). Online programmes already permitted since 2018 Open & Distance Learning Regulations.</p>
<p class="bi-te">UGC — 1956 చట్టం ద్వారా చట్టబద్ధ సంస్థ. 2024లో ఆన్‌లైన్ డిగ్రీలను సాధారణ డిగ్రీలతో సమానం అని ప్రకటించింది (NAAC A+ లేదా NIRF టాప్ 100 యూనివర్సిటీలు).</p>

<div class="section-hdr">NMC — National Medical Commission / NMC</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Established</td><td><b>2020</b> via NMC Act, 2019 (notified Sep 25, 2020)</td><td class="bi-te">2020 (చట్టం 2019)</td></tr>
<tr><td>Replaced</td><td><b>MCI</b> (Medical Council of India, 1933-2020)</td><td class="bi-te">MCI స్థానంలో</td></tr>
<tr><td>HQ</td><td>New Delhi</td><td class="bi-te">న్యూఢిల్లీ</td></tr>
<tr><td>Functions</td><td>Medical education + practice + ethics + UG/PG curriculum + NEET-PG/NExT</td><td class="bi-te">వైద్య విద్య, నీతి, పాఠ్యక్రమం</td></tr>
<tr><td>Autonomous Boards</td><td>4: UG Medical Edu, PG Medical Edu, Medical Assessment &amp; Rating, Ethics &amp; Registration</td><td class="bi-te">4 స్వతంత్ర బోర్డులు</td></tr>
</table>

<div class="section-hdr">NEP 2020 — Quick Facts / NEP 2020</div>
<p><b>NEP 2020</b> = National Education Policy, approved <b>July 29, 2020</b>. Replaced NEP 1986. Key reforms: <b>5+3+3+4 school structure</b>, multidisciplinary higher ed, multiple entry-exit, 6% GDP target on education, three-language formula, ABC (Academic Bank of Credits), NCrF (National Credit Framework).</p>
<p class="bi-te">NEP 2020 — జూలై 29, 2020 ఆమోదం. 5+3+3+4 పాఠశాల నిర్మాణం, బహుళ-ప్రవేశ/నిష్క్రమణ, విద్యపై GDPలో 6% లక్ష్యం, త్రి-భాషా సూత్రం, ABC, NCrF.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  23. LEGAL & SECURITY — POCSO & NIA 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_legal_security',
              'POCSO & NIA — Legal & Security 2026',
              'POCSO & NIA — చట్టం & భద్రత 2026', """
<div class="concept-cover">
  <h1>POCSO &amp; NIA — Legal &amp; Security 2026 &nbsp;<span class="bi-te">/ POCSO & NIA</span></h1>
  <div class="sub">Child protection law • Anti-terror investigation agency</div>
</div>

<div class="section-hdr">POCSO Act / POCSO చట్టం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full form</td><td><b>P</b>rotection of <b>C</b>hildren from <b>S</b>exual <b>O</b>ffences Act</td><td class="bi-te">లైంగిక నేరాల నుండి పిల్లల రక్షణ చట్టం</td></tr>
<tr><td>Year</td><td>Enacted <b>2012</b>; amended 2019 (death penalty for aggravated assault on minors)</td><td class="bi-te">2012 (2019 సవరణ)</td></tr>
<tr><td>Applies to</td><td>Children below 18 years (gender-neutral)</td><td class="bi-te">18 ఏళ్ళ లోపు పిల్లలు</td></tr>
<tr><td>Special features</td><td>Special POCSO courts, in-camera trial, child-friendly procedures, mandatory reporting</td><td class="bi-te">ప్రత్యేక POCSO కోర్టులు, in-camera విచారణ</td></tr>
<tr><td>2024 cases</td><td>~2,081 POCSO cases registered nationwide</td><td class="bi-te">~2,081 కేసులు</td></tr>
</table>

<div class="section-hdr">NIA / NIA</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full form</td><td><b>N</b>ational <b>I</b>nvestigation <b>A</b>gency</td><td class="bi-te">జాతీయ దర్యాప్తు సంస్థ</td></tr>
<tr><td>Established</td><td><b>2008</b> via NIA Act, post-26/11 Mumbai attacks</td><td class="bi-te">2008 — 26/11 మెుంబై దాడుల తర్వాత</td></tr>
<tr><td>Ministry</td><td>Ministry of Home Affairs (MHA)</td><td class="bi-te">హోం వ్యవహారాల మంత్రిత్వ శాఖ</td></tr>
<tr><td>DG (2026)</td><td><b>Dinesh Kumar</b> (IPS)</td><td class="bi-te">డైరెక్టర్ జనరల్: దినేశ్ కుమార్</td></tr>
<tr><td>HQ</td><td>New Delhi</td><td class="bi-te">న్యూఢిల్లీ</td></tr>
<tr><td>Jurisdiction</td><td>Pan-India; can take suo motu cognisance of terrorism/UAPA matters (2019 amendment)</td><td class="bi-te">భారతదేశమంతటా; UAPA కేసులు</td></tr>
</table>
<p>NIA handles terror financing, cyber-terrorism, human trafficking, counterfeit currency, hijacking, and offences under the UAPA 1967. Special NIA Courts conduct trials.</p>
<p class="bi-te">NIA — ఉగ్రవాద నిధులు, సైబర్ ఉగ్రవాదం, మానవ అక్రమ రవాణా, నకిలీ నోట్లు, విమాన అపహరణ, UAPA 1967 కేసులు. ప్రత్యేక NIA కోర్టుల్లో విచారణ.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  24. RUSSIA-UKRAINE WAR 2025-26
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_ukraine_war',
              'Russia-Ukraine War 2025-26',
              'రష్యా-ఉక్రెయిన్ యుద్ధం 2025-26', """
<div class="concept-cover">
  <h1>Russia-Ukraine War 2025-26 &nbsp;<span class="bi-te">/ రష్యా-ఉక్రెయిన్ యుద్ధం</span></h1>
  <div class="sub">Began Feb 24, 2022 • Ongoing • Peace talks 2025-26</div>
</div>

<div class="section-hdr">Background &amp; Status / నేపథ్యం & స్థితి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Start</td><td>February 24, 2022 — Russian invasion</td><td class="bi-te">ఫిబ్రవరి 24, 2022</td></tr>
<tr><td>Russian President</td><td>Vladimir Putin</td><td class="bi-te">వ్లాదిమిర్ పుతిన్</td></tr>
<tr><td>Ukrainian President</td><td>Volodymyr Zelenskyy</td><td class="bi-te">వొలొదిమిర్ జెలెన్‌స్కీ</td></tr>
<tr><td>Status 2025-26</td><td>Active conflict + ongoing peace negotiations</td><td class="bi-te">కొనసాగుతోంది + శాంతి చర్చలు</td></tr>
<tr><td>NATO</td><td>Provides military aid to Ukraine; no direct intervention</td><td class="bi-te">NATO — ఆయుధ సహాయం (ప్రత్యక్ష జోక్యం లేదు)</td></tr>
</table>

<div class="section-hdr">India's Position / భారత వైఖరి</div>
<p>India maintains <b>strategic autonomy</b> — abstained on UNSC/UNGA resolutions; called for "dialogue and diplomacy". PM Modi told Putin "this is not an era of war" (SCO Samarkand 2022). India bought discounted Russian crude oil (now ~35% of imports). PM Modi visited Moscow (Jul 2024) and Kyiv (Aug 2024), the first Indian PM to visit Ukraine.</p>
<p class="bi-te">భారత్ — వ్యూహాత్మక స్వేచ్ఛ. UNSC/UNGA తీర్మానాలలో గైర్హాజరు; "సంవాదం & దౌత్యం" కోసం పిలుపు. మోడీ పుతిన్‌తో "ఇది యుద్ధకాలం కాదు" (SCO 2022). రష్యా చమురు 35% దిగుమతి. మోడీ — మాస్కో (జూలై 2024), కైవ్ (ఆగస్టు 2024 — తొలి భారత PM ఉక్రెయిన్ సందర్శన).</p>

<div class="section-hdr">2025-26 Peace Efforts / 2025-26 శాంతి ప్రయత్నాలు</div>
<p>Trump's return (Jan 2025) accelerated peace mediation. Multiple rounds of US-Russia-Ukraine talks, ceasefire proposals, and territorial discussions ongoing. No final settlement as of mid-2026.</p>
<p class="bi-te">ట్రంప్ తిరిగి రావడం (జన 2025) శాంతి మధ్యవర్తిత్వాన్ని వేగవంతం చేసింది. US-రష్యా-ఉక్రెయిన్ చర్చలు, కాల్పుల విరమణ ప్రతిపాదనలు. 2026 మధ్యనాటికి తుది ఒప్పందం లేదు.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  25. INFRASTRUCTURE & LOGISTICS 2026
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_infrastructure',
              'Infrastructure, Logistics & MSME 2026',
              'మౌలిక సదుపాయాలు & MSME 2026', """
<div class="concept-cover">
  <h1>Infrastructure, Logistics &amp; MSME 2026 &nbsp;<span class="bi-te">/ మౌలిక సదుపాయాలు & MSME</span></h1>
  <div class="sub">NLP • Roads Rs.3.09 L cr • Railways Rs.2.78 L cr • MSME credit guarantee</div>
</div>

<div class="section-hdr">National Logistics Policy (NLP) / జాతీయ లాజిస్టిక్స్ పాలసీ</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launched</td><td>September 17, 2022 by PM Modi</td><td class="bi-te">సెప్టెం 17, 2022 — PM మోదీ</td></tr>
<tr><td>Goal</td><td>Reduce logistics cost from <b>~14% of GDP to 8%</b> by 2030</td><td class="bi-te">GDPలో 14% నుండి 8%కి తగ్గింపు</td></tr>
<tr><td>Pillars</td><td>IDS (Integrated Digital System), ULIP (Unified Logistics Interface Platform), ELOG (Ease of Logistics), System Improvement</td><td class="bi-te">IDS, ULIP, ELOG</td></tr>
<tr><td>LPI Rank</td><td>India 38/139 in World Bank LPI 2023 (up from 44 in 2018)</td><td class="bi-te">World Bank LPI 38వ స్థానం</td></tr>
</table>

<div class="section-hdr">Budget 2026-27 Infra Allocations / మౌలిక సదుపాయాల కేటాయింపులు</div>
<table class="key-table">
<tr><th>Sector</th><th>Allocation</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Capex (overall)</td><td>Rs.12.22 lakh crore</td><td class="bi-te">మూలధన వ్యయం రూ.12.22 ల.కో.</td></tr>
<tr><td>Roads &amp; Highways</td><td>Rs.3.09 lakh crore</td><td class="bi-te">రోడ్లు రూ.3.09 ల.కో.</td></tr>
<tr><td>Railways</td><td>Rs.2.78 lakh crore</td><td class="bi-te">రైల్వేలు రూ.2.78 ల.కో.</td></tr>
<tr><td>HSR corridors</td><td>7 new High-Speed Rail corridors, ~4,000 km</td><td class="bi-te">7 HSR కారిడార్లు ~4,000 కి.మీ</td></tr>
</table>

<div class="section-hdr">MSME — Budget Announcements / MSME బడ్జెట్ ప్రకటనలు</div>
<p><b>MSME</b> = Micro, Small &amp; Medium Enterprises (governed by MSMED Act 2006). Revised definition (2020) by combined investment + turnover thresholds. 2026-27 Budget: <b>credit guarantee cover expanded</b>, mudra loan limit hiked, capital support increased. MSME sector contributes ~30% of GDP and ~45% of exports.</p>
<p class="bi-te">MSME — MSMED చట్టం 2006. 2020 సవరణ ద్వారా పెట్టుబడి + టర్నోవర్ ఆధారిత నిర్వచనం. 2026-27 బడ్జెట్: క్రెడిట్ హామీ విస్తరణ, ముద్రా లోన్ పరిమితి పెంపు, మూలధన మద్దతు. GDPలో ~30%, ఎగుమతుల్లో ~45% MSME వాటా.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  26. PARIS OLYMPICS 2024 — INDIA'S CAMPAIGN
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_paris_olympics',
              'Paris Olympics 2024 — India Performance',
              'పారిస్ ఒలింపిక్స్ 2024 — భారత ప్రదర్శన', """
<div class="concept-cover">
  <h1>Paris Olympics 2024 — India Performance &nbsp;<span class="bi-te">/ పారిస్ ఒలింపిక్స్ 2024</span></h1>
  <div class="sub">July 26 - Aug 11, 2024 • 33rd Summer Olympics • India: 6 medals (1 Silver, 5 Bronze)</div>
</div>

<div class="section-hdr">Games Overview / క్రీడల సింహావలోకనం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Edition</td><td><b>33rd Summer Olympics</b> (Games of the XXXIII Olympiad)</td><td class="bi-te">33వ వేసవి ఒలింపిక్స్</td></tr>
<tr><td>Host city</td><td><b>Paris, France</b> (3rd time after 1900, 1924)</td><td class="bi-te">పారిస్, ఫ్రాన్స్</td></tr>
<tr><td>Dates</td><td>July 26 — August 11, 2024</td><td class="bi-te">జూలై 26 — ఆగస్టు 11, 2024</td></tr>
<tr><td>Nations</td><td>206 NOCs + Refugee Olympic Team</td><td class="bi-te">206 దేశాలు + శరణార్థి జట్టు</td></tr>
<tr><td>Mascot</td><td>Phryges</td><td class="bi-te">ప్రిజెస్</td></tr>
<tr><td>Medal table topper</td><td>USA (40G) tied with China (40G) — USA top by total</td><td class="bi-te">USA & చైనా 40 బంగారాలతో సమం, USA మొత్తం పతకాల్లో అగ్రస్థానం</td></tr>
</table>

<div class="section-hdr">India's Medal Haul — 6 Medals / భారత పతకాలు</div>
<table class="key-table">
<tr><th>Athlete</th><th>Sport / Event</th><th>Medal</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Neeraj Chopra</b></td><td>Athletics — Javelin Throw (89.45 m)</td><td>Silver</td><td class="bi-te">నీరజ్ చోప్రా — జావెలిన్ — రజతం</td></tr>
<tr><td><b>Manu Bhaker</b></td><td>Shooting — 10m Air Pistol (Women)</td><td>Bronze</td><td class="bi-te">మనుభాకర్ — 10మీ ఎయిర్ పిస్టల్</td></tr>
<tr><td><b>Manu Bhaker + Sarabjot Singh</b></td><td>Shooting — 10m Mixed Team Pistol</td><td>Bronze</td><td class="bi-te">మనుభాకర్ + సర్బ్‌జోత్ — మిక్స్‌డ్ టీం</td></tr>
<tr><td><b>Swapnil Kusale</b></td><td>Shooting — 50m Rifle 3 Positions (Men)</td><td>Bronze</td><td class="bi-te">స్వప్నిల్ కుసాలే — 50మీ రైఫిల్</td></tr>
<tr><td><b>Indian Men's Hockey Team</b></td><td>Hockey — Bronze playoff vs Spain</td><td>Bronze</td><td class="bi-te">పురుషుల హాకీ జట్టు — కాంస్యం</td></tr>
<tr><td><b>Aman Sehrawat</b></td><td>Wrestling — Men's Freestyle 57 kg</td><td>Bronze</td><td class="bi-te">అమన్ సెహ్రావత్ — రెజ్లింగ్</td></tr>
</table>
<p>India finished <b>71st</b> on the medal table with <b>1 Silver + 5 Bronze = 6 total</b> (vs 7 medals at Tokyo 2020). <b>Manu Bhaker</b> became the <b>first independent-India athlete to win 2 medals at a single Olympics</b>. <b>Aman Sehrawat</b> became India's <b>youngest individual Olympic medallist</b> (21 years 24 days). Indian Men's Hockey won back-to-back Olympic bronzes (Tokyo 2020 + Paris 2024) — first time since 1968-72.</p>
<p class="bi-te">భారత్ పతక పట్టికలో 71వ స్థానం; మొత్తం 6 (1 రజతం + 5 కాంస్యాలు). మనుభాకర్ ఒకే ఒలింపిక్స్‌లో 2 పతకాలు గెలిచిన తొలి స్వతంత్ర-భారత క్రీడాకారిణి. అమన్ సెహ్రావత్ (21 సం. 24 రోజులు) భారత అతి చిన్న వ్యక్తిగత ఒలింపిక్ పతక విజేత. పురుషుల హాకీ జట్టు వరుసగా రెండు ఒలింపిక్స్‌లో కాంస్యం — 1968-72 తర్వాత తొలిసారి.</p>

<div class="section-hdr">Why It Matters / ఎందుకు ముఖ్యం</div>
<p>Paris 2024 marked a slight regression from Tokyo 2020 (7 medals, 1G). India missed gold for the first time since Tokyo and lost <b>6 fourth-place finishes</b> — narrow misses in shooting, archery, badminton. Sparked debate on the <b>Khelo India</b> and <b>TOPS</b> programmes. India is bidding to host <b>2036 Olympics</b> (Ahmedabad). The next Olympics will be <b>Los Angeles 2028</b>.</p>
<p class="bi-te">పారిస్ 2024 టోక్యో 2020 (7 పతకాలు, 1 బంగారం)తో పోలిస్తే కొంత తగ్గుదల. ఒకే బంగారం కూడా రాలేదు; 6 సార్లు 4వ స్థానం. Khelo India, TOPS పథకాలపై చర్చ. భారత్ 2036 ఒలింపిక్స్‌ను అహ్మదాబాద్‌లో నిర్వహించాలని బిడ్; తదుపరి ఒలింపిక్స్ లాస్ ఏంజెల్స్ 2028.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  27. GST 2.0 REFORMS — September 2025
#  Linked from MCQs 31389-31390, 31423, 31426
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_gst_2026_reforms',
              'GST 2.0 Reforms — September 2025',
              'GST 2.0 సంస్కరణలు — సెప్టెంబర్ 2025', """
<div class="concept-cover">
  <h1>GST 2.0 Reforms (September 2025) &nbsp;<span class="bi-te">/ GST 2.0 సంస్కరణలు</span></h1>
  <div class="sub">2-slab system (5% + 18%) + 40% sin/luxury • Effective Sep 22, 2025 • 55th GST Council</div>
</div>

<div class="section-hdr">Key Timeline / కీలక కాలవ్యవస్థ</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Announcement</td><td>PM Modi's <b>Independence Day speech, Aug 15, 2025</b> — promised "Next-Gen GST reforms"</td><td class="bi-te">ఆగస్టు 15, 2025 PM మోదీ ప్రసంగం</td></tr>
<tr><td>GST Council Meeting</td><td><b>55th GST Council, Sep 3, 2025</b> — formal recommendation</td><td class="bi-te">55వ GST Council, సెప్టెంబర్ 3, 2025</td></tr>
<tr><td>Effective date</td><td><b>September 22, 2025</b></td><td class="bi-te">సెప్టెంబర్ 22, 2025</td></tr>
<tr><td>Council Chair</td><td>Union FM Nirmala Sitharaman (ex officio per Art. 279A)</td><td class="bi-te">FM నిర్మలా సీతారామన్ (Art 279A)</td></tr>
</table>

<div class="section-hdr">Slab Restructure / స్లాబ్ నిర్మాణ మార్పులు</div>
<table class="key-table">
<tr><th>Old (pre-Sep 2025)</th><th>New (GST 2.0)</th><th class="bi-te">వివరణ</th></tr>
<tr><td>5% / 12% / 18% / 28%</td><td><b>5% / 18% (2 main slabs)</b> + 40% sin/luxury</td><td class="bi-te">12% & 28% రద్దు</td></tr>
<tr><td>Cess on luxury</td><td>Subsumed into 40% combined rate</td><td class="bi-te">Cess రద్దు</td></tr>
</table>

<div class="section-hdr">40% Slab Coverage / 40% స్లాబ్ పరిధి</div>
<p>The <b>40% rate</b> applies to <b>sin and luxury goods</b>: pan masala, tobacco products, aerated drinks, yachts, private aircraft, and high-end / premium cars — ensuring revenue balance and fairness.</p>
<p class="bi-te">40% రేటు — sin/luxury goods (pan masala, పొగాకు, aerated drinks, yachts, private aircraft, premium కార్లు)కు.</p>

<div class="section-hdr">Compliance Simplification / అనుసరణ సరళీకరణ</div>
<p>Registration and return filing simplified, refunds made faster, compliance costs reduced — easing burden on MSMEs and startups. GST 2.0 is the biggest indirect-tax rationalisation since GST's 2017 launch.</p>
<p class="bi-te">GST 2.0 — 2017 GST ప్రారంభం తర్వాత అతిపెద్ద పరోక్ష పన్ను సంస్కరణ; MSME + startup మీద compliance భారం తగ్గింపు.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  28. INCOME-TAX ACT 2025 — Replaces 1961 Act
#  Linked from MCQs 31391-31392
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_income_tax_2025',
              'Income-tax Act 2025 — Replaces 1961 Act',
              'ఆదాయ పన్ను చట్టం 2025', """
<div class="concept-cover">
  <h1>Income-tax Act 2025 &nbsp;<span class="bi-te">/ ఆదాయ పన్ను చట్టం 2025</span></h1>
  <div class="sub">Passed Aug 12, 2025 • Assent Aug 21, 2025 • Effective Apr 1, 2026 • Replaces 1961 Act</div>
</div>

<div class="section-hdr">Legislative Timeline / శాసన కాలవ్యవస్థ</div>
<table class="key-table">
<tr><th>Event</th><th>Date</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Parliament passage</td><td><b>August 12, 2025</b></td><td class="bi-te">పార్లమెంట్ ఆమోదం</td></tr>
<tr><td>Presidential assent</td><td><b>August 21, 2025</b> — President Droupadi Murmu</td><td class="bi-te">రాష్ట్రపతి ద్రౌపదీ ముర్ము ఆమోదం</td></tr>
<tr><td>Effective from</td><td><b>April 1, 2026</b></td><td class="bi-te">ఏప్రిల్ 1, 2026 నుండి అమల్లోకి</td></tr>
<tr><td>Replaces</td><td>Income Tax Act 1961 (64 years old)</td><td class="bi-te">1961 చట్టాన్ని భర్తీ (64 సం.)</td></tr>
</table>

<div class="section-hdr">Structural Changes / నిర్మాణాత్మక మార్పులు</div>
<table class="key-table">
<tr><th>Metric</th><th>1961 Act</th><th>2025 Act</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Sections</td><td>819</td><td><b>536</b></td><td class="bi-te">~283 sections తగ్గింపు</td></tr>
<tr><td>Chapters</td><td>23</td><td><b>23</b></td><td class="bi-te">అదే 23 chapters</td></tr>
<tr><td>Schedules</td><td>14</td><td>16</td><td class="bi-te">షెడ్యూల్‌లు</td></tr>
<tr><td>Year concept</td><td>PY + AY (dual)</td><td><b>Single "Tax Year"</b> (Apr 1 – Mar 31)</td><td class="bi-te">ఏకీకృత "Tax Year"</td></tr>
</table>

<div class="section-hdr">Key Simplifications / ముఖ్య సరళీకరణలు</div>
<p>Plain-language drafting; tabular formats; explanations and provisos removed; cross-references simplified. The dual <b>"Previous Year + Assessment Year"</b> concept (a perennial source of confusion) is replaced by a single <b>"Tax Year"</b> running Apr 1 – Mar 31. Tax rates / slabs are not changed by this Act — those continue to be set in annual Finance Bills.</p>
<p class="bi-te">Plain-language drafting; "Previous Year + Assessment Year" ద్వంద్వాన్ని తొలగించి ఏకీకృత "Tax Year" (Apr 1 - Mar 31); పన్ను రేట్లు annual Finance Bill లో set అవుతాయి.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  29. MISSION MAUSAM — Weather/Climate Initiative
#  Linked from MCQs 31393-31394
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_mission_mausam',
              'Mission Mausam — Weather Initiative',
              'మిషన్ మౌసమ్ — వాతావరణ చొరవ', """
<div class="concept-cover">
  <h1>Mission Mausam &nbsp;<span class="bi-te">/ మిషన్ మౌసమ్</span></h1>
  <div class="sub">Launched Sep 14, 2024 by PM Modi • MoES • Rs.2,000 cr / 2 years • IMD + IITM + NCMRWF</div>
</div>

<div class="section-hdr">Key Facts / ముఖ్య విషయాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Cabinet approval</td><td>September 11, 2024</td><td class="bi-te">క్యాబినెట్ సెప్టెంబర్ 11, 2024</td></tr>
<tr><td>Launch by</td><td><b>PM Modi on Sep 14, 2024</b> at IMD's 150th anniversary</td><td class="bi-te">PM మోదీ సెప్టెంబర్ 14, 2024 — IMD 150 సం. వేడుకలు</td></tr>
<tr><td>Outlay</td><td><b>Rs.2,000 crore</b> over <b>2 years</b></td><td class="bi-te">రూ.2,000 కోట్లు / 2 సం.</td></tr>
<tr><td>Lead ministry</td><td><b>Ministry of Earth Sciences (MoES)</b></td><td class="bi-te">భూ శాస్త్ర మంత్రిత్వ శాఖ</td></tr>
</table>

<div class="section-hdr">Three Implementing Institutions / 3 అమలు సంస్థలు</div>
<table class="key-table">
<tr><th>Institution</th><th>Role</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>IMD</b> (India Meteorological Dept, New Delhi)</td><td>Operational weather forecasting; nowcasting; warnings</td><td class="bi-te">వాతావరణ పర్యవేక్షణ + హెచ్చరికలు</td></tr>
<tr><td><b>IITM</b> (Indian Institute of Tropical Meteorology, Pune)</td><td>Research, Earth System Models, monsoon studies</td><td class="bi-te">పరిశోధన, Earth System Models</td></tr>
<tr><td><b>NCMRWF</b> (National Centre for Medium-Range Weather Forecasting, Noida)</td><td>3-10 day forecasts; ensemble modelling; HPC</td><td class="bi-te">3-10 day forecasts; HPC</td></tr>
</table>

<div class="section-hdr">Technology Components / సాంకేతిక భాగాలు</div>
<p>Next-generation <b>radars and satellite systems</b> with advanced sensors; <b>high-performance supercomputers</b>; <b>AI/ML modelling</b> for precision forecasting; improved Earth System Models; <b>GIS-based automated Decision Support System</b> for real-time data dissemination.</p>
<p class="bi-te">Next-gen radars + satellites + supercomputers + AI/ML modelling + Earth System Models + GIS-based Decision Support System.</p>

<div class="section-hdr">Beneficiary Sectors / ప్రయోజన పొందే రంగాలు</div>
<p>Agriculture, disaster management, defence, environment, aviation, water resources, power, tourism, shipping, transport, energy, health.</p>
<p class="bi-te">వ్యవసాయం, విపత్తు నిర్వహణ, రక్షణ, పర్యావరణం, విమానయానం, నీటి వనరులు, విద్యుత్, పర్యాటకం, షిప్పింగ్, రవాణా, శక్తి, ఆరోగ్యం.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  30. FOUR LABOUR CODES — Notified Nov 21, 2025
#  Linked from MCQs 31395-31396, 31422
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_labour_codes',
              'Four Labour Codes — Notified Nov 21, 2025',
              '4 కార్మిక కోడ్‌లు — నవంబర్ 21, 2025 notification', """
<div class="concept-cover">
  <h1>Four Labour Codes &nbsp;<span class="bi-te">/ 4 కార్మిక కోడ్‌లు</span></h1>
  <div class="sub">Notified Nov 21, 2025 • Consolidates 29 labour laws • Reform since 2019-20</div>
</div>

<div class="section-hdr">Notification & Scope / Notification మరియు పరిధి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>All-four notified</td><td><b>November 21, 2025</b> — Government of India</td><td class="bi-te">నవంబర్ 21, 2025 — అన్నీ ఏకకాలంలో notify</td></tr>
<tr><td>Laws consolidated</td><td><b>29 central labour laws</b> → 4 codes</td><td class="bi-te">29 కేంద్ర చట్టాలు → 4 codes</td></tr>
<tr><td>Original passage</td><td>Code on Wages (2019); other 3 codes (2020)</td><td class="bi-te">Wages 2019; మిగతా 3 — 2020</td></tr>
</table>

<div class="section-hdr">The Four Codes / 4 కోడ్‌లు</div>
<table class="key-table">
<tr><th>#</th><th>Code</th><th>Consolidates</th><th class="bi-te">వివరణ</th></tr>
<tr><td>1</td><td><b>Code on Wages 2019</b></td><td>Payment of Wages 1936 + Minimum Wages 1948 + Payment of Bonus 1965 + Equal Remuneration 1976</td><td class="bi-te">4 wage చట్టాలు</td></tr>
<tr><td>2</td><td><b>Industrial Relations (IR) Code 2020</b></td><td>Trade Unions 1926 + Industrial Employment (Standing Orders) 1946 + Industrial Disputes 1947</td><td class="bi-te">3 IR చట్టాలు</td></tr>
<tr><td>3</td><td><b>Occupational Safety, Health &amp; Working Conditions (OSH) Code 2020</b></td><td>Factories Act 1948 + Mines Act 1952 + Plantations Labour 1951 + 10 more</td><td class="bi-te">13 OSH చట్టాలు</td></tr>
<tr><td>4</td><td><b>Social Security Code 2020</b></td><td>EPF 1952 + ESI 1948 + Maternity Benefit 1961 + Gratuity 1972 + Employees Compensation 1923 + 4 more</td><td class="bi-te">9 SS చట్టాలు</td></tr>
</table>

<div class="section-hdr">Key Features / ముఖ్యాంశాలు</div>
<p><b>National Floor Wage</b> introduced. <b>Gig and platform workers</b> now covered under <b>Social Security Code</b> — a first in Indian labour law. <b>Fixed-term employment</b> recognised in IR Code. <b>Worker</b> definition expanded; threshold for retrenchment under IR Code raised from 100 → 300 (factory closures need permission only above 300 workers).</p>
<p class="bi-te">National Floor Wage; gig + platform workers SS Code కిందికి (భారత కార్మిక చట్టంలో మొదటిసారి); Fixed-term employment గుర్తింపు; retrenchment threshold 100 → 300.</p>
"""))

# ═══════════════════════════════════════════════════════════════════
#  31. UNESCO INTANGIBLE CULTURAL HERITAGE — India's 16 Elements
#  Linked from MCQs 31401-31402, 31420
# ═══════════════════════════════════════════════════════════════════
NOTES.append(('natl_2026_ich',
              'UNESCO Intangible Cultural Heritage — India',
              'UNESCO అమూర్త సాంస్కృతిక వారసత్వం — భారత్', """
<div class="concept-cover">
  <h1>UNESCO Intangible Cultural Heritage (ICH) — India &nbsp;<span class="bi-te">/ UNESCO ICH — భారత్</span></h1>
  <div class="sub">India: 16 elements (as of Dec 2025) • 20th ICH Session hosted at Red Fort, Delhi</div>
</div>

<div class="section-hdr">India's 16 ICH Elements (chronological) / 16 ICH అంశాలు</div>
<table class="key-table">
<tr><th>Year</th><th>Element</th><th class="bi-te">వివరణ</th></tr>
<tr><td>2008</td><td>Kutiyattam — Sanskrit theatre (Kerala)</td><td class="bi-te">కూటియాట్టం (కేరళ)</td></tr>
<tr><td>2008</td><td>Tradition of Vedic Chanting</td><td class="bi-te">వేద పఠనం</td></tr>
<tr><td>2008</td><td>Ramlila — traditional performance of Ramayana</td><td class="bi-te">రామ్‌లీలా</td></tr>
<tr><td>2009</td><td>Ramman — religious festival & ritual theatre, Garhwal Himalayas</td><td class="bi-te">రామ్మన్</td></tr>
<tr><td>2010</td><td>Mudiyettu — ritual theatre/dance drama (Kerala)</td><td class="bi-te">ముడియేట్టు</td></tr>
<tr><td>2010</td><td>Kalbelia — folk songs/dances (Rajasthan)</td><td class="bi-te">కల్బేలియా</td></tr>
<tr><td>2010</td><td>Chhau dance</td><td class="bi-te">ఛౌ నృత్యం</td></tr>
<tr><td>2012</td><td>Buddhist Chanting of Ladakh</td><td class="bi-te">లడాఖ్ బౌద్ధ పఠనం</td></tr>
<tr><td>2013</td><td>Sankirtana — ritual singing, drumming &amp; dancing (Manipur)</td><td class="bi-te">సంకీర్తన (మణిపూర్)</td></tr>
<tr><td>2014</td><td>Thatheras of Jandiala Guru — traditional brass &amp; copper craft</td><td class="bi-te">తథేరాస్ (పంజాబ్)</td></tr>
<tr><td>2016</td><td><b>Yoga</b></td><td class="bi-te">యోగా</td></tr>
<tr><td>2017</td><td><b>Kumbh Mela</b></td><td class="bi-te">కుంభ మేళా</td></tr>
<tr><td>2021</td><td><b>Durga Puja in Kolkata</b></td><td class="bi-te">కోల్‌కతా దుర్గా పూజ</td></tr>
<tr><td>2023</td><td><b>Garba</b> of Gujarat (15th element)</td><td class="bi-te">గుజరాత్ గర్బా</td></tr>
<tr><td>2025</td><td><b>Deepavali / Diwali</b> (16th element, inscribed Dec 2025 at New Delhi session)</td><td class="bi-te">దీపావళి — 16వ ICH</td></tr>
</table>

<div class="section-hdr">20th UNESCO ICH Committee Session — India Hosted / 20వ session</div>
<p>India hosted the <b>20th session of the UNESCO Intergovernmental Committee for the Safeguarding of the Intangible Cultural Heritage</b> at the historic <b>Red Fort, New Delhi</b> from <b>December 8-13, 2025</b>. This was India's first time hosting the ICH Committee session. <b>Deepavali</b> was inscribed at this very session as India's 16th ICH element.</p>
<p class="bi-te">భారత్ — 20వ UNESCO ICH Committee session ను Red Fort, న్యూ ఢిల్లీ లో డిసెంబర్ 8-13, 2025 న host చేసింది; ఇదే sessionలో దీపావళి (16వ ICH) inscribed.</p>

<div class="section-hdr">Classical Dances NOT in ICH / ICH లో **లేని** శాస్త్రీయ నృత్యాలు</div>
<p>Indian <b>classical dances</b> like <b>Bharatanatyam, Kathak, Kathakali, Kuchipudi, Odissi, Manipuri, Mohiniyattam, Sattriya</b> are recognised by India's <b>Sangeet Natak Akademi</b> but are <b>NOT individually inscribed</b> in the UNESCO ICH Representative List. However, related forms like <b>Kutiyattam</b> (Sanskrit theatre) and <b>Chhau</b> are inscribed.</p>
<p class="bi-te">భారతీయ శాస్త్రీయ నృత్యాలు (భరతనాట్యం, కథక్, కథకళి, కూచిపూడి, ఒడిస్సీ, మణిపురి, మోహినీయాట్టం, సత్రియా) UNESCO ICH list లో **వ్యక్తిగతంగా inscribe కాలేదు** — సంగీత నాటక అకాడెమీ గుర్తింపు మాత్రమే.</p>
"""))

print(f"Loaded {len(NOTES)} National 2026 concept notes")

# ════════════════════════════════════════════════════════════════
#  DATABASE INSERT
# ════════════════════════════════════════════════════════════════

if USE_POSTGRES:
    cur = conn.cursor()
    # Only delete tags from this file — don't wipe other notes
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
print(f"SUCCESS: Seeded {len(NOTES)} National Current Affairs 2026 concept notes into DB.")
for tag, label, *_ in NOTES:
    print(f"  - {tag:35s} - {label}")
