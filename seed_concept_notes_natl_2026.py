#!/usr/bin/env python3
"""
seed_concept_notes_natl_2026.py
Rich bilingual (English + Telugu) concept notes for National Current Affairs 2026 MCQs.
Topics: Budget, RD, Padma Awards, ISRO, Defence, Foreign Policy, Sports, Census, Const Amendment, etc.
~12 concept notes covering IDs 31301-31380 (Batch H+PDF 2026).
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
<p>The 16th FC report covers the 5-year period 2026-27 to 2030-31. The Urbanization Premium is a new structural reform recognising the higher fiscal needs of rapidly urbanising states.</p>
<p class="bi-te">16వ ఆర్థిక సంఘం నివేదిక 2026-27 నుండి 2030-31 వరకు 5 సం. కాలానికి. పట్టణీకరణ ప్రీమియం కొత్త నిర్మాణాత్మక సంస్కరణ.</p>
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
<p>The Ashok Chakra to Gp Capt Shubhanshu Shukla is historic — it recognises his role on the <b>Axiom-4 mission</b> as the first Indian on the ISS since Rakesh Sharma (1984). Peace-time equivalent of the Param Vir Chakra.</p>
<p class="bi-te">శుభాంశు శుక్లాకు అశోక చక్ర — యాక్సియమ్-4 మిషన్‌కు. రాకేశ్ శర్మ (1984) తర్వాత ISS చేరిన మొదటి భారతీయుడు. శాంతి కాల పరమ వీర చక్ర సమానం.</p>
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
<p>Padma awards are conferred annually by the President at Rashtrapati Bhavan around March-April. They are India's highest civilian honours after the Bharat Ratna.</p>
<p class="bi-te">పద్మ పురస్కారాలను రాష్ట్రపతి భవన్‌లో ప్రతి సం. మార్చి-ఏప్రిల్‌లో అందజేస్తారు. భారత రత్న తరువాత భారత అత్యున్నత పౌర పురస్కారాలు.</p>
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
<p>Skyroot Aerospace successfully tested the <b>Dhawan-3 cryogenic engine</b> for <b>145 seconds</b> — a major step for India's private space sector. Named after Dr. Satish Dhawan.</p>
<p class="bi-te">స్కైరూట్ ఏరోస్పేస్ <b>ధవన్-3 క్రయోజెనిక్ ఇంజిన్</b>ను <b>145 సెకన్లు</b> విజయవంతంగా పరీక్షించింది. డా. సతీష్ ధవన్ పేరుతో.</p>

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
<p>Commissioned <b>February 27, 2026</b> at <b>Visakhapatnam</b>. INS Anjadip is an <b>anti-submarine shallow water craft</b>, nicknamed <b>"Dolphin Killer"</b>. Built indigenously, it enhances India's coastal anti-submarine warfare capability.</p>
<p class="bi-te">INS అంజదిప్ — ఫిబ్రవరి 27, 2026న విశాఖపట్నంలో జలప్రవేశం. యాంటీ-సబ్‌మెరైన్ షాలో వాటర్ క్రాఫ్ట్, "డాల్ఫిన్ కిల్లర్" మారుపేరు. భారత్‌లో తయారు.</p>

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
<p>The 16th Census is the first major decennial enumeration since 2011 (the 2021 Census was deferred due to COVID). The inclusion of <b>caste data</b> is the most significant policy change since 1931.</p>
<p class="bi-te">2011 తర్వాత మొదటి దశాబ్ద జనాభా గణన. 1931 తర్వాత మొదటిసారి <b>కుల వివరాలు</b> సేకరణ.</p>

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
<p>Constitutional amendments under <b>Article 368</b> require a special majority — at least two-thirds of members present and voting AND a majority of the total membership. For a 543-seat Lok Sabha, the 2/3 threshold is <b>362</b> (if all attend) but operational at 352 in the day's count.</p>
<p class="bi-te">రాజ్యాంగ సవరణలకు <b>ఆర్టికల్ 368</b> ప్రకారం ప్రత్యేక మెజారిటీ అవసరం — 2/3 మెజారిటీ.</p>
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
<p>Jan Vishwas 2 is the successor to the Jan Vishwas Act 2023 (which decriminalised 183 provisions in 42 laws). It is the largest single ease-of-doing-business deregulation in Indian legislative history.</p>
<p class="bi-te">జన్ విశ్వాస్ 2 — 2023 జన్ విశ్వాస్ చట్టానికి కొనసాగింపు. భారత చట్ట చరిత్రలో అతిపెద్ద single deregulation.</p>
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
<p>Released <b>March 14, 2026</b>. Detained under the <b>National Security Act (NSA)</b> since <b>September 26, 2025</b> following Ladakh statehood protests (in which 4 people were killed).</p>
<p class="bi-te">సోనమ్ వాంగ్‌చుక్ — మార్చి 14, 2026న విడుదల. సెప్టెంబర్ 26, 2025 నుండి NSA కింద నిర్బంధం — లడఖ్ రాష్ట్ర హోదా ఉద్యమ నేపథ్యంలో (4 మంది మరణించారు).</p>

<div class="section-hdr">No-Confidence vs LS Speaker Om Birla / లోక్‌సభ స్పీకర్‌పై అవిశ్వాస తీర్మానం</div>
<p>Motion defeated <b>March 10, 2026</b>. <b>113 MPs</b> signed the no-confidence motion against Speaker Om Birla. Final tally: <b>NDA 293 vs INDIA bloc 233</b>.</p>
<p class="bi-te">లోక్‌సభ స్పీకర్ ఓం బిర్లాపై అవిశ్వాస తీర్మానం మార్చి 10న ఓడిపోయింది. 113 ఎంపీలు సంతకం; NDA 293 — INDIA 233.</p>

<div class="section-hdr">CEC Impeachment Motion Rejected / CEC అభిశంసన తిరస్కరణ</div>
<p>The impeachment notice against Chief Election Commissioner Gyanesh Kumar was <b>rejected on April 6, 2026</b> by Rajya Sabha Chairman <b>Radhakrishnan</b>.</p>
<p class="bi-te">ప్రధాన ఎన్నికల కమిషనర్ జ్ఞానేశ్ కుమార్‌పై అభిశంసన నోటీసును రాజ్యసభ ఛైర్మన్ రాధాకృష్ణన్ ఏప్రిల్ 6, 2026న తిరస్కరించారు.</p>

<div class="section-hdr">India Declared Naxal-Free / భారత్ నక్సల్-రహితంగా ప్రకటన</div>
<p>The Centre declared India <b>"naxal-free" in April 2026</b>. However, <b>37 districts</b> remain under the "Concern" category — including <b>Alluri Sitarama Raju district</b> in Andhra Pradesh and Bhadradri Kothagudem &amp; Mulugu in Telangana.</p>
<p class="bi-te">ఏప్రిల్ 2026లో కేంద్రం భారత్‌ను "నక్సల్-రహితం"గా ప్రకటించింది. అయితే <b>37 జిల్లాలు</b> "ఆందోళన" విభాగంలో ఉన్నాయి — AP అల్లూరి సీతారామ రాజు, TS భద్రాద్రి కొత్తగూడెం, ములుగు.</p>

<div class="section-hdr">NITI Higher Education Internationalisation / ఉన్నత విద్య అంతర్జాతీయీకరణ</div>
<table class="key-table">
<tr><th>Stat</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Report date</td><td>December 22, 2025</td><td class="bi-te">డిసెంబర్ 22, 2025</td></tr>
<tr><td>Indian students abroad (2024)</td><td>13.35 lakh</td><td class="bi-te">విదేశాల్లో భారత విద్యార్థులు (2024): 13.35 లక్షలు</td></tr>
<tr><td><b>AP rank</b></td><td><b>1st</b> in students going abroad — 62,771 (in 2018)</td><td class="bi-te"><b>AP</b> విదేశాలకు వెళ్లే విద్యార్థులలో <b>1వ</b> — 62,771 (2018)</td></tr>
<tr><td>India's annual spend</td><td>~$70 billion on overseas education</td><td class="bi-te">భారత్ సాలీనా ~$70 బిలియన్</td></tr>
</table>

<div class="section-hdr">Education Reforms / విద్యా సంస్కరణలు</div>
<p><b>NCERT</b> granted <b>Deemed-to-be-University</b> status. <b>CBSE 3-language policy</b> mandatory from <b>Class 6</b> in the 2026-27 academic year — implementing NEP 2020.</p>
<p class="bi-te"><b>NCERT</b>కు Deemed-to-be-University హోదా. <b>CBSE 3-భాషల విధానం</b> 2026-27 విద్యా సం. నుండి 6వ తరగతి నుండి తప్పనిసరి — NEP 2020 అమలులో భాగం.</p>

<div class="section-hdr">Akshaya Patra 500 Crore Meals / అక్షయ పాత్ర 500 కోట్ల భోజనాలు</div>
<p>The <b>Akshaya Patra Foundation</b> crossed the historic milestone of <b>500 crore (5 billion) cumulative meals</b> served on <b>March 17, 2026</b> — the world's largest NGO-run school meal programme.</p>
<p class="bi-te">అక్షయ పాత్ర ఫౌండేషన్ — మార్చి 17, 2026న చారిత్రాత్మక <b>500 కోట్ల భోజనాల</b> మైలురాయి అధిగమించింది. ప్రపంచంలోనే అతిపెద్ద NGO పాఠశాల భోజన పథకం.</p>
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
<p><b>Total Fertility Rate</b> = average number of children per woman in her reproductive years. <b>2.1 is the population replacement level</b> — below this, the population stabilises (without migration). India crossed below 2.1 in some surveys post-2022 — a major demographic shift.</p>
<p class="bi-te">TFR అంటే ఒక మహిళ తన పునరుత్పత్తి వయస్సులో సంతానోత్పత్తి చేసే సగటు పిల్లల సంఖ్య. <b>2.1 జనాభా స్థిరీకరణ స్థాయి</b> — దీని కంటే తక్కువ TFR ఉంటే (వలసలు లేకుండా) జనాభా తగ్గుతుంది.</p>

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
<p>WAVES positions India as a global M&amp;E powerhouse alongside Hollywood (USA), Hallyu (Korea), and content giants like China &amp; Japan. The summit aligns with India's "Bharat — VishvaGuru" creative-economy ambitions and competes for international co-production deals.</p>
<p class="bi-te">WAVES — హాలీవుడ్ (USA), హాలియు (కొరియా), చైనా/జపాన్‌లకు పోటీగా భారత్‌ను ప్రపంచ M&E శక్తి కేంద్రంగా నిలబెడుతుంది. భారత్ "విశ్వగురు" సృజనాత్మక ఆర్థిక లక్ష్యానికి అనుగుణం; అంతర్జాతీయ co-production ఒప్పందాలకు దోహదపడుతుంది.</p>
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
