#!/usr/bin/env python3
"""
seed_concept_notes_national.py
Bilingual (English + Telugu) concept notes for National Current Affairs 2026 MCQs.
3 concept notes: national_ca_budget | national_ca_polity | national_ca_misc
IDs covered: 31001-31300
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

NOTES = []   # list of (tag, label, label_te, html)

# ═══════════════════════════════════════════════════════
#  1. UNION BUDGET 2026-27
#     IDs: 31001-31020
# ═══════════════════════════════════════════════════════
NOTES.append(('national_ca_budget', 'Union Budget 2026-27', 'కేంద్ర బడ్జెట్ 2026-27', """
<div class="concept-cover">
  <h1>Union Budget 2026-27 &nbsp;<span class="bi-te">/ కేంద్ర బడ్జెట్ 2026-27</span></h1>
  <div class="sub">Presented: February 1, 2026 • Finance Minister: Nirmala Sitharaman (8th consecutive budget)</div>
</div>

<div class="section-hdr">Key Budget Figures / ముఖ్య బడ్జెట్ సంఖ్యలు</div>
<table class="key-table">
<tr><th>Item</th><th>Amount</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total Expenditure</td><td><b>₹50,65,345 crore</b></td><td class="bi-te">మొత్తం వ్యయం</td></tr>
<tr><td>Capital Expenditure</td><td><b>₹11,21,304 crore</b> (3.1% of GDP)</td><td class="bi-te">మూలధన వ్యయం</td></tr>
<tr><td>Revenue Expenditure</td><td>₹39,44,041 crore</td><td class="bi-te">రెవెన్యూ వ్యయం</td></tr>
<tr><td>Fiscal Deficit Target</td><td><b>4.4% of GDP</b></td><td class="bi-te">ఆర్థిక లోటు లక్ష్యం</td></tr>
<tr><td>Total Receipts</td><td>₹50,65,345 crore</td><td class="bi-te">మొత్తం రాబడి</td></tr>
<tr><td>GDP Nominal</td><td>~₹3,24,11,544 crore (FY27 estimate)</td><td class="bi-te">నామినల్ GDP అంచనా</td></tr>
<tr><td>National Highways</td><td><b>₹2,87,000 crore</b></td><td class="bi-te">జాతీయ రహదారులు</td></tr>
<tr><td>Defence</td><td>₹6,81,210 crore (2.1% GDP)</td><td class="bi-te">రక్షణ కేటాయింపు</td></tr>
<tr><td>Education</td><td>₹1,48,000 crore+</td><td class="bi-te">విద్య కేటాయింపు</td></tr>
<tr><td>Health</td><td>~2.5% of GDP</td><td class="bi-te">ఆరోగ్య కేటాయింపు</td></tr>
</table>

<div class="section-hdr">Income Tax Slabs 2026-27 (New Regime) / ఆదాయపు పన్ను స్లాబ్‌లు</div>
<table class="key-table">
<tr><th>Income Slab</th><th>Rate</th><th class="bi-te">ఆదాయం</th></tr>
<tr><td>Up to ₹4 lakh</td><td><b>Nil</b></td><td class="bi-te">₹4 లక్షల వరకు: పన్ను లేదు</td></tr>
<tr><td>₹4L – ₹8L</td><td>5%</td><td class="bi-te">₹4L–₹8L: 5%</td></tr>
<tr><td>₹8L – ₹12L</td><td>10%</td><td class="bi-te">₹8L–₹12L: 10%</td></tr>
<tr><td>₹12L – ₹16L</td><td>15%</td><td class="bi-te">₹12L–₹16L: 15%</td></tr>
<tr><td>₹16L – ₹20L</td><td>20%</td><td class="bi-te">₹16L–₹20L: 20%</td></tr>
<tr><td>₹20L – ₹24L</td><td>25%</td><td class="bi-te">₹20L–₹24L: 25%</td></tr>
<tr><td>Above ₹24L</td><td><b>30%</b></td><td class="bi-te">₹24L పైన: 30%</td></tr>
</table>
<p><b>Key relief:</b> Nil tax up to ₹12L income (with rebate u/s 87A). Standard deduction ₹75,000. Gold import duty: <b>6%</b>.</p>
<p class="bi-te"><b>ముఖ్య మినహాయింపు:</b> ₹12 లక్షల వరకు పన్ను లేదు (87A రీబేట్‌తో). స్టాండర్డ్ డిడక్షన్ ₹75,000. బంగారు దిగుమతి సుంకం: 6%.</p>

<div class="section-hdr">Key Budget Announcements / ముఖ్య బడ్జెట్ ప్రకటనలు</div>
<table class="key-table">
<tr><th>Scheme / Policy</th><th>Key Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>PM Kisan Samman Nidhi</td><td>₹6,000/year (3 instalments of ₹2,000) to farmers</td><td class="bi-te">రైతులకు ₹6,000/సంవత్సరం</td></tr>
<tr><td>Viksit Bharat 2047</td><td>Vision: $20 trillion economy by 2047</td><td class="bi-te">2047 నాటికి $20 ట్రిలియన్ ఆర్థిక వ్యవస్థ లక్ష్యం</td></tr>
<tr><td>PMAY (Urban + Rural)</td><td>2 crore additional homes target</td><td class="bi-te">2 కోట్ల అదనపు ఇళ్ళ నిర్మాణం</td></tr>
<tr><td>Insurance FDI</td><td>FDI limit raised to <b>100%</b> in insurance sector</td><td class="bi-te">బీమా రంగంలో FDI పరిమితి 100% కి పెంపు</td></tr>
<tr><td>PM Mudra Yojana</td><td>Loan limit raised to <b>₹20 lakh</b></td><td class="bi-te">ముద్రా రుణ పరిమితి ₹20 లక్షలకు పెంపు</td></tr>
<tr><td>Startup Tax Holiday</td><td>Income tax holiday extended to <b>10 years</b></td><td class="bi-te">స్టార్టప్‌లకు పన్ను మినహాయింపు 10 సంవత్సరాలకు</td></tr>
<tr><td>AB-PMJAY (Ayushman)</td><td>Expanded to citizens 70+ yrs; ₹5L health cover; 3,437 crore claims</td><td class="bi-te">70+ వయస్సు వారికి; ₹5L ఆరోగ్య భీమా</td></tr>
<tr><td>PM Surya Ghar Muft Bijli</td><td>Launched Feb 2024; 300 units free electricity/month for rooftop solar</td><td class="bi-te">ఫిబ్రవరి 2024; నెలకు 300 యూనిట్లు ఉచిత విద్యుత్</td></tr>
<tr><td>Skill India Mission</td><td>₹6,000 crore allocation; 1 crore youth trained/year</td><td class="bi-te">₹6,000 కోట్లు; 1 కోటి యువత శిక్షణ</td></tr>
<tr><td>PM GatiShakti</td><td>Multimodal connectivity; NMP ₹1,11,000 crore</td><td class="bi-te">బహుళ రవాణా అనుసంధానం</td></tr>
<tr><td>India AI Mission</td><td><b>₹10,372 crore</b> for AI infrastructure &amp; research</td><td class="bi-te">AI మిషన్‌కు ₹10,372 కోట్లు</td></tr>
<tr><td>Agri Credit</td><td>₹20 lakh crore agri credit target</td><td class="bi-te">వ్యవసాయ రుణ లక్ష్యం ₹20 లక్ష కోట్లు</td></tr>
<tr><td>MSP Hike 2025-26</td><td>8–10% increase for Kharif crops</td><td class="bi-te">MSP 8–10% పెంపు</td></tr>
<tr><td>NIP</td><td>National Infrastructure Pipeline: ₹1,11,000 crore</td><td class="bi-te">జాతీయ మౌలిక సదుపాయాల పైప్‌లైన్</td></tr>
<tr><td>Semiconductor Dholera</td><td>Tata Electronics fab in Dholera, Gujarat — first in India</td><td class="bi-te">తొలి సెమీకండక్టర్ ఫాబ్ — గుజరాత్, ధోలేరా</td></tr>
</table>

<div class="section-hdr">India Economic Snapshot 2025-26 / భారత ఆర్థిక స్థితి</div>
<table class="key-table">
<tr><th>Indicator</th><th>Value</th><th class="bi-te">సూచిక</th></tr>
<tr><td>GDP Rank (World)</td><td><b>5th largest</b> economy</td><td class="bi-te">5వ అతిపెద్ద ఆర్థిక వ్యవస్థ</td></tr>
<tr><td>GDP Growth (FY26)</td><td>~6.5% (IMF: fastest growing major economy)</td><td class="bi-te">అత్యంత వేగంగా వృద్ధి చెందుతున్న ఆర్థిక వ్యవస్థ</td></tr>
<tr><td>GDP per Capita</td><td>$3,900+</td><td class="bi-te">తలసరి ఆదాయం</td></tr>
<tr><td>Forex Reserves</td><td><b>$704 billion</b></td><td class="bi-te">విదేశీ మారక నిల్వలు</td></tr>
<tr><td>FDI Inflow</td><td>$67 billion (FY25)</td><td class="bi-te">ప్రత్యక్ష విదేశీ పెట్టుబడులు</td></tr>
<tr><td>Exports</td><td>$437 billion (FY25)</td><td class="bi-te">ఎగుమతులు</td></tr>
<tr><td>Trade Deficit</td><td>$200 billion+</td><td class="bi-te">వాణిజ్య లోటు</td></tr>
<tr><td>UPI Transactions</td><td>16.99 billion (Jan 2026)</td><td class="bi-te">UPI లావాదేవీలు జనవరి 2026</td></tr>
<tr><td>National Income</td><td>₹3,00,000 crore+ (NNP at market price)</td><td class="bi-te">జాతీయ ఆదాయం</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  2. NATIONAL POLITY & GOVERNANCE 2024-26
#     IDs: 31021-31045
# ═══════════════════════════════════════════════════════
NOTES.append(('national_ca_polity', 'National Polity & Governance 2024-26', 'జాతీయ రాజ్యాంగం & పాలన 2024-26', """
<div class="concept-cover">
  <h1>National Polity &amp; Governance 2024-26 &nbsp;<span class="bi-te">/ జాతీయ రాజ్యాంగం &amp; పాలన</span></h1>
  <div class="sub">New Criminal Laws • CAA • Elections • Constitutional Appointments • Digital Laws</div>
</div>

<div class="section-hdr">New Criminal Laws (Effective July 1, 2024) / కొత్త నేరన్యాయ చట్టాలు</div>
<table class="key-table">
<tr><th>New Law</th><th>Replaced</th><th>Key Feature</th><th class="bi-te">ముఖ్య మార్పు</th></tr>
<tr><td><b>Bharatiya Nyaya Sanhita (BNS)</b></td><td>Indian Penal Code (IPC) 1860</td><td>Removed sedition; added organized crime &amp; terrorism</td><td class="bi-te">రాజద్రోహం తొలగించారు; సంఘటిత నేరాలు చేర్చారు</td></tr>
<tr><td><b>Bharatiya Nagarik Suraksha Sanhita (BNSS)</b></td><td>CrPC 1973</td><td>Trial in absentia; Zero FIR; 90-day remand</td><td class="bi-te">Zero FIR, గైర్హాజరీలో విచారణ</td></tr>
<tr><td><b>Bharatiya Sakshya Adhiniyam (BSA)</b></td><td>Indian Evidence Act 1872</td><td>Electronic records &amp; e-signatures as evidence</td><td class="bi-te">ఎలక్ట్రానిక్ రికార్డులు సాక్ష్యంగా</td></tr>
</table>
<p>All three laws came into effect on <b>July 1, 2024</b> — the most significant criminal law reform since independence.</p>
<p class="bi-te">మూడు చట్టాలు <b>జూలై 1, 2024</b> నుండి అమల్లోకి వచ్చాయి — స్వాతంత్ర్యం తర్వాత అతిపెద్ద నేరన్యాయ సంస్కరణ.</p>

<div class="section-hdr">Citizenship Amendment Act (CAA) / పౌరసత్వ సవరణ చట్టం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>CAA Passed</td><td>December 2019 (Parliament)</td><td class="bi-te">డిసెంబర్ 2019 లో ఆమోదం</td></tr>
<tr><td>Rules Notified</td><td><b>March 11, 2024</b></td><td class="bi-te">మార్చి 11, 2024న నియమాలు నోటిఫై</td></tr>
<tr><td>Eligible</td><td>Persecuted Hindus, Sikhs, Buddhists, Jains, Parsis, Christians from Pakistan, Bangladesh, Afghanistan (arrived before Dec 31, 2014)</td><td class="bi-te">పాకిస్తాన్, బంగ్లాదేశ్, అఫ్గానిస్తాన్ నుండి హిందువులు, సిక్కులు, బౌద్ధులు, జైనులు, పార్సీలు, క్రైస్తవులు</td></tr>
<tr><td>Excluded</td><td>Muslims not included (secular principle)</td><td class="bi-te">ముస్లింలు చేర్చబడలేదు</td></tr>
<tr><td>Cut-off date</td><td>December 31, 2014</td><td class="bi-te">చివరి తేదీ: డిసెంబర్ 31, 2014</td></tr>
</table>

<div class="section-hdr">Key Constitutional Appointments 2024-26 / ముఖ్య రాజ్యాంగ పదవుల నియామకాలు</div>
<table class="key-table">
<tr><th>Position</th><th>Name</th><th>Since</th><th class="bi-te">పదవి</th></tr>
<tr><td>Chief Justice of India (50th)</td><td><b>Justice Sanjiv Khanna</b></td><td>November 11, 2024</td><td class="bi-te">భారత ప్రధాన న్యాయమూర్తి (50వ)</td></tr>
<tr><td>Chief Election Commissioner</td><td><b>Rajiv Kumar</b></td><td>May 2022</td><td class="bi-te">ముఖ్య ఎన్నికల కమిషనర్</td></tr>
<tr><td>RBI Governor (26th)</td><td><b>Sanjay Malhotra</b></td><td>December 11, 2024</td><td class="bi-te">RBI గవర్నర్ (26వ)</td></tr>
<tr><td>CDS (Chief of Defence Staff)</td><td><b>Gen. Anil Chauhan</b></td><td>September 2022</td><td class="bi-te">చీఫ్ ఆఫ్ డిఫెన్స్ స్టాఫ్</td></tr>
<tr><td>Chief of Naval Staff</td><td><b>Admiral Dinesh Kumar Tripathi</b></td><td>April 2024</td><td class="bi-te">నౌకాదళ అధిపతి</td></tr>
<tr><td>NITI Aayog CEO</td><td><b>B.V.R. Subrahmanyam</b></td><td>2023</td><td class="bi-te">నీతి ఆయోగ్ CEO</td></tr>
<tr><td>SEBI Chairperson</td><td><b>Tuhin Kanta Pandey</b></td><td>March 2025</td><td class="bi-te">SEBI చైర్‌పర్సన్</td></tr>
<tr><td>IRDAI Chairman</td><td><b>Debasish Panda</b></td><td>2022</td><td class="bi-te">IRDAI చైర్మన్</td></tr>
<tr><td>PM (3rd term)</td><td><b>Narendra Modi</b></td><td>June 9, 2024</td><td class="bi-te">PM మోడీ 3వ పదవీకాలం</td></tr>
</table>

<div class="section-hdr">One Nation One Election (ONOE) / ఒకే దేశం ఒకే ఎన్నిక</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Committee</td><td>High-Level Committee chaired by <b>former President Ram Nath Kovind</b></td><td class="bi-te">మాజీ రాష్ట్రపతి రామ్‌నాథ్ కోవింద్ అధ్యక్షతన కమిటీ</td></tr>
<tr><td>Report Submitted</td><td>March 2024</td><td class="bi-te">మార్చి 2024లో నివేదిక సమర్పించారు</td></tr>
<tr><td>Proposal</td><td>Simultaneous Lok Sabha + State Assembly elections</td><td class="bi-te">లోక్‌సభ + రాష్ట్ర అసెంబ్లీ ఒకే సమయంలో</td></tr>
<tr><td>Aim</td><td>Reduce poll expenditure, policy disruption &amp; code of conduct impact</td><td class="bi-te">ఎన్నికల వ్యయం తగ్గించడం</td></tr>
</table>

<div class="section-hdr">Digital Personal Data Protection (DPDP) Act 2023</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Passed</td><td>August 2023 (Parliament)</td><td class="bi-te">ఆగస్ట్ 2023లో ఆమోదం</td></tr>
<tr><td>Applies to</td><td>Digital personal data of Indian citizens</td><td class="bi-te">భారతీయ పౌరుల డిజిటల్ వ్యక్తిగత డేటా</td></tr>
<tr><td>Key Body</td><td>Data Protection Board of India</td><td class="bi-te">డేటా ప్రొటెక్షన్ బోర్డ్ ఆఫ్ ఇండియా</td></tr>
<tr><td>Penalty</td><td>Up to ₹250 crore for data breach</td><td class="bi-te">డేటా ఉల్లంఘనకు ₹250 కోట్ల వరకు జరిమానా</td></tr>
</table>

<div class="section-hdr">SC/ST & Other Constitutional Developments</div>
<table class="key-table">
<tr><th>Development</th><th>Key Ruling / Change</th><th class="bi-te">వివరణ</th></tr>
<tr><td>SC/ST Sub-classification</td><td>Supreme Court (7-judge bench, 2024): States CAN sub-classify SC/ST for reservations</td><td class="bi-te">రాష్ట్రాలు SC/ST లో ఉప-వర్గీకరణ చేయవచ్చు</td></tr>
<tr><td>Ladakh UT</td><td>Created as UT (without legislature) on <b>October 31, 2019</b></td><td class="bi-te">అక్టోబర్ 31, 2019న కేంద్రపాలిత ప్రాంతం</td></tr>
<tr><td>Bharat Ratna 2024</td><td>5 awards: LK Advani (only living), Chaudhary Charan Singh, PV Narasimha Rao, MS Swaminathan, Karpoori Thakur (all posthumous except Advani)</td><td class="bi-te">5 అవార్డులు: LK అద్వానీ (జీవించి ఉన్న ఏకైక వ్యక్తి)</td></tr>
<tr><td>Census 2026</td><td>Estimated population: <b>145 crore</b> (last census 2011: 121 crore)</td><td class="bi-te">2026 జనాభా అంచనా: 145 కోట్లు</td></tr>
<tr><td>RBI Rate Cut</td><td>25 bps cut in February 2025 (repo rate to 6.25%)</td><td class="bi-te">25 bps రేట్ కట్ ఫిబ్రవరి 2025</td></tr>
<tr><td>Agnipath Scheme</td><td>4-year military service; Agniveers (Army, Navy, Air Force)</td><td class="bi-te">4 సంవత్సరాల సేవ; అగ్నివీర్లు</td></tr>
<tr><td>Cooperative Ministry</td><td>New Ministry of Cooperation created (2021); MoS Amit Shah</td><td class="bi-te">2021లో సహకార మంత్రిత్వ శాఖ</td></tr>
<tr><td>India UNSC</td><td>Non-permanent member: 2021-22 term</td><td class="bi-te">UNSC అనిత్య సభ్యత్వం: 2021-22</td></tr>
</table>

<div class="section-hdr">2024 General Elections / 2024 సాధారణ ఎన్నికలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>18th Lok Sabha</td><td>NDA won; PM Modi 3rd consecutive term; BJP 240 seats</td><td class="bi-te">NDA విజయం; PM మోడీ 3వ పదవీకాలం</td></tr>
<tr><td>Home Minister</td><td><b>Amit Shah</b></td><td class="bi-te">హోం మంత్రి</td></tr>
<tr><td>Defence Minister</td><td><b>Rajnath Singh</b></td><td class="bi-te">రక్షణ మంత్రి</td></tr>
<tr><td>EAM</td><td><b>S. Jaishankar</b></td><td class="bi-te">విదేశాంగ మంత్రి</td></tr>
<tr><td>Women Ministers</td><td>11 women ministers in Cabinet</td><td class="bi-te">11 మంది మహిళా మంత్రులు</td></tr>
<tr><td>Maharashtra (Nov 2024)</td><td>Mahayuti alliance (BJP+Shiv Sena (Shinde)+NCP(Ajit)) won</td><td class="bi-te">మహాయుతి కూటమి విజయం</td></tr>
<tr><td>Jharkhand (Nov 2024)</td><td>JMM-Congress-RJD (INDIA bloc) won</td><td class="bi-te">JMM-Congress-RJD విజయం</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  3. NATIONAL CA MISC — Space, Defence, Economy, Sports,
#     Awards, Environment, Schemes & Relations
#     IDs: 31046-31300
# ═══════════════════════════════════════════════════════
NOTES.append(('national_ca_misc', 'National CA 2026 — Space, Defence, Economy & More', 'జాతీయ CA 2026 — అంతరిక్షం, రక్షణ, ఆర్థికం & మరిన్ని', """
<div class="concept-cover">
  <h1>National Current Affairs 2026 &nbsp;<span class="bi-te">/ జాతీయ కరెంట్ అఫైర్స్ 2026</span></h1>
  <div class="sub">Space • Defence • Economy • Sports • Awards • Environment • Schemes</div>
</div>

<div class="section-hdr">Space Missions — ISRO 2024-26 / అంతరిక్ష యాత్రలు</div>
<table class="key-table">
<tr><th>Mission</th><th>Key Facts</th><th class="bi-te">వివరాలు</th></tr>
<tr><td><b>SpaDeX</b> (Space Docking Experiment)</td><td>Launched: <b>Dec 30, 2024</b> on PSLV-C60; India became <b>4th country</b> to demonstrate space docking; 2 satellites (SDX01 &amp; SDX02)</td><td class="bi-te">డిసెంబర్ 30, 2024; స్పేస్ డాకింగ్; 4వ దేశం</td></tr>
<tr><td><b>Chandrayaan-3</b></td><td>Landed south pole of Moon: <b>August 23, 2023</b>; Vikram lander + Pragyan rover; 1st country to land near lunar south pole</td><td class="bi-te">ఆగస్ట్ 23, 2023 చంద్రుడి దక్షిణ ధ్రువం; మొదటి దేశం</td></tr>
<tr><td><b>Gaganyaan G1</b></td><td>India's first crewed space mission planned 2026; crew module test flights ongoing</td><td class="bi-te">భారత తొలి మానవ సహిత అంతరిక్ష యాత్ర 2026</td></tr>
<tr><td><b>Chandrayaan-4</b></td><td>Lunar sample return mission; approved by Cabinet</td><td class="bi-te">చంద్రుని నమూనా తీసుకొచ్చే మిషన్</td></tr>
<tr><td><b>Aditya-L1</b></td><td>India's first solar mission; reached L1 (Lagrange Point 1) halo orbit Jan 6, 2024</td><td class="bi-te">భారత తొలి సౌర పరిశోధన; L1 కక్ష్యలో</td></tr>
<tr><td><b>GSAT-N2</b></td><td>Launched on <b>SpaceX Falcon 9</b> (Nov 2024) — ISRO's 1st commercial use of SpaceX</td><td class="bi-te">SpaceX Falcon 9 ద్వారా నవంబర్ 2024</td></tr>
<tr><td><b>Shubhanshu Shukla</b></td><td>ISRO astronaut; selected for Axiom Mission 4 (Ax-4) on ISS (2025)</td><td class="bi-te">ISS కోసం Axiom Mission 4లో ISRO వ్యోమగామి</td></tr>
<tr><td><b>LVM3-M2</b></td><td>ISRO launched 36 OneWeb broadband satellites (2023)</td><td class="bi-te">36 OneWeb ఉపగ్రహాలు ప్రయోగం</td></tr>
<tr><td><b>Agnikul Cosmos</b></td><td>Private startup; <b>Agnibaan SOrTeD</b> — India's first privately developed rocket launched 2024</td><td class="bi-te">తొలి ప్రైవేట్ రాకెట్ 2024</td></tr>
<tr><td><b>India Space Policy 2023</b></td><td>Allows private players; IN-SPACe regulates; NSIL for commercial launches</td><td class="bi-te">ప్రైవేట్ రంగాన్ని అనుమతించే అంతరిక్ష నీతి</td></tr>
</table>

<div class="section-hdr">Defence — Operations & Equipment 2024-26 / రక్షణ</div>
<table class="key-table">
<tr><th>Event / System</th><th>Key Details</th><th class="bi-te">వివరాలు</th></tr>
<tr><td><b>Pahalgam Attack</b></td><td>April 22, 2025; <b>26 tourists killed</b> in Baisaran meadow, Pahalgam, J&amp;K; Pakistan-backed terror</td><td class="bi-te">ఏప్రిల్ 22, 2025; 26 పర్యాటకులు మరణించారు</td></tr>
<tr><td><b>Operation Sindoor</b></td><td>India's retaliatory strike (May 7, 2025): destroyed <b>9 terrorist camps</b> in Pakistan and PoK; precision strikes using Rafale, Brahmos, drones</td><td class="bi-te">మే 7, 2025; పాకిస్తాన్/PoKలో 9 శిబిరాలు ధ్వంసం</td></tr>
<tr><td><b>HAL Tejas MK-1A</b></td><td>India's LCA; IAF order: <b>97 aircraft</b> from HAL; Made-in-India fighter</td><td class="bi-te">97 Tejas MK-1A యుద్ధ విమానాల ఆర్డర్</td></tr>
<tr><td><b>INS Arighat</b></td><td>India's 2nd SSBN (nuclear ballistic missile submarine); commissioned Aug 2024</td><td class="bi-te">2వ అణ్వాయుధ జలాంతర్గామి; ఆగస్ట్ 2024</td></tr>
<tr><td><b>DRDO Agni-5</b></td><td>ICBM range: <b>5,000+ km</b>; MIRV-capable; nuclear deterrent</td><td class="bi-te">5,000+ కి.మీ. పరిధి; MIRV సక్షమం</td></tr>
<tr><td><b>Pinaka MRLS</b></td><td>Multi-barrel rocket launcher; India exporting to Armenia &amp; others</td><td class="bi-te">బహుళ బ్యారెల్ రాకెట్ లాంచర్; ఎగుమతి అవుతుంది</td></tr>
<tr><td><b>Defence Exports</b></td><td><b>₹21,083 crore</b> (FY24) — all-time high; target ₹50,000 crore by 2030</td><td class="bi-te">₹21,083 కోట్లు (FY24); 2030 నాటికి ₹50,000 కోట్లు లక్ష్యం</td></tr>
<tr><td><b>India-China Border</b></td><td>Depsang-Demchok disengagement deal: <b>October 2024</b>; patrolling resumed after 4 years</td><td class="bi-te">అక్టోబర్ 2024 డెప్సాంగ్-డెంచోక్ ఉపసంహరణ ఒప్పందం</td></tr>
<tr><td><b>INS Vikrant</b></td><td>India's 1st Indigenous aircraft carrier; commissioned <b>September 2, 2022</b></td><td class="bi-te">తొలి స్వదేశీ విమానవాహక నౌక; సెప్టెంబర్ 2, 2022</td></tr>
</table>

<div class="section-hdr">Sports Achievements — India 2024-26 / క్రీడలు</div>
<table class="key-table">
<tr><th>Event</th><th>India's Achievement</th><th class="bi-te">వివరాలు</th></tr>
<tr><td><b>Paris Olympics 2024</b></td><td><b>6 medals total:</b> 1 Silver (Neeraj Chopra - Javelin), 2 Bronze (Manu Bhaker - Pistol x2), 1 Bronze (Hockey vs Germany), 1 Bronze (Aman Sehrawat - Wrestling), + Shooter team bronze</td><td class="bi-te">6 పతకాలు: నీరజ్ వెండి, మను బాఖర్ 2 కాంస్యాలు, హాకీ కాంస్యం</td></tr>
<tr><td><b>T20 World Cup 2024</b></td><td>India won 🏆; beat South Africa in final; held in <b>USA &amp; West Indies</b></td><td class="bi-te">భారత్ విజేత; USA &amp; వెస్ట్ ఇండీస్‌లో జరిగింది</td></tr>
<tr><td><b>Chess World Championship 2024</b></td><td><b>D. Gukesh</b> — youngest ever world chess champion (age 18); beat Ding Liren (China)</td><td class="bi-te">గుకేష్ D — అతిన్న్యూన వయసులో విశ్వ చెస్ చాంపియన్</td></tr>
<tr><td><b>Chess Olympiad 2025</b></td><td>Held in <b>New Delhi, India</b>; India Women team won <b>Gold</b></td><td class="bi-te">న్యూ ఢిల్లీ 2025; భారత మహిళా జట్టు స్వర్ణం</td></tr>
<tr><td><b>Khel Ratna 2024</b></td><td><b>D. Gukesh</b> (Chess) received Major Dhyan Chand Khel Ratna Award</td><td class="bi-te">గుకేష్‌కు ఖేల్ రత్న అవార్డు</td></tr>
<tr><td><b>Kho-Kho WC 2025</b></td><td>India won both Men's &amp; Women's titles (inaugural Kho-Kho World Cup)</td><td class="bi-te">తొలి ఖో-ఖో WCలో భారత్ ద్వంద్వ విజేత</td></tr>
<tr><td><b>Maha Kumbh 2025</b></td><td>Prayagraj; <b>Jan 13 – Feb 26, 2025</b>; <b>45 crore devotees</b> — largest religious gathering ever</td><td class="bi-te">ప్రయాగ్‌రాజ్; 45 కోట్ల భక్తులు — చరిత్రలో అతిపెద్ద మత సమావేశం</td></tr>
<tr><td><b>Khelo India 2025</b></td><td>Hosted by <b>Maharashtra</b></td><td class="bi-te">మహారాష్ట్ర ఆతిథ్యం</td></tr>
</table>

<div class="section-hdr">Awards & Honours 2024-25 / అవార్డులు</div>
<table class="key-table">
<tr><th>Award</th><th>Recipient 2024-25</th><th class="bi-te">వివరాలు</th></tr>
<tr><td>Bharat Ratna 2024</td><td>LK Advani (only living), Chaudhary Charan Singh†, PV Narasimha Rao†, MS Swaminathan†, Karpoori Thakur†</td><td class="bi-te">5 అవార్డులు; అద్వానీ జీవించి ఉన్న ఏకైక వ్యక్తి</td></tr>
<tr><td>Jnanpith Award 2023</td><td><b>Gulzar</b> (Urdu/Hindi) — posthumously 2024 ceremony</td><td class="bi-te">గుల్జార్ (ఉర్దూ/హిందీ)</td></tr>
<tr><td>Padma Vibhushan</td><td><b>Sharda Sinha</b> (posthumous — Bhojpuri folk singer)</td><td class="bi-te">శారదా సిన్హా (మరణానంతరం)</td></tr>
<tr><td>Dadasaheb Phalke</td><td><b>Mithun Chakraborty</b> (2024 — announced with 70th National Film Awards)</td><td class="bi-te">మిథున్ చక్రవర్తి — దాదాసాహెబ్ ఫాల్కే 2024</td></tr>
<tr><td>Sahitya Akademi 2025</td><td><b>Jeet Thayil</b> (English category)</td><td class="bi-te">జీత్ థాయిల్ (ఇంగ్లీష్)</td></tr>
<tr><td>Nobel Peace 2024</td><td><b>Nihon Hidankyo</b> (Japanese atomic bomb survivors group)</td><td class="bi-te">జపాన్ అణుబాంబు బాధితుల సంస్థ</td></tr>
<tr><td>Nobel Literature 2024</td><td><b>Han Kang</b> (South Korea) — first Asian woman Nobel laureate in Literature</td><td class="bi-te">హాన్ కాంగ్ (దక్షిణ కొరియా) — తొలి ఆసియా మహిళ</td></tr>
<tr><td>Nobel Physics 2024</td><td><b>John Hopfield &amp; Geoffrey Hinton</b> (AI neural networks)</td><td class="bi-te">AI న్యూరల్ నెట్‌వర్క్‌లకు నోబెల్</td></tr>
<tr><td>PM Modi Kuwait Award</td><td>PM Modi received Kuwait's highest civilian honour (Jan 2025)</td><td class="bi-te">కువైట్ అత్యున్నత పౌర పురస్కారం PM మోడీకి</td></tr>
</table>

<div class="section-hdr">Environment & Rankings / పర్యావరణం & ర్యాంకింగ్‌లు</div>
<table class="key-table">
<tr><th>Indicator</th><th>India's Status</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Forest Cover</td><td><b>21.76%</b> of total area (FSI 2023)</td><td class="bi-te">మొత్తం వైశాల్యంలో 21.76%</td></tr>
<tr><td>Tiger Count</td><td><b>3,167</b> (2023 Tiger Census) — world's largest</td><td class="bi-te">3,167 పులులు — ప్రపంచంలో అత్యధికం</td></tr>
<tr><td>Ramsar Sites</td><td><b>85+</b> Ramsar wetlands (highest in world)</td><td class="bi-te">85+ రామ్‌సర్ తడి భూములు</td></tr>
<tr><td>UNESCO World Heritage</td><td><b>42 sites</b> (40 cultural + 7 natural)</td><td class="bi-te">42 UNESCO ప్రపంచ వారసత్వ ప్రదేశాలు</td></tr>
<tr><td>Solar Capacity</td><td><b>100 GW+</b> installed (2024); Renewable target: 500 GW by 2030</td><td class="bi-te">100 GW+ సౌర విద్యుత్</td></tr>
<tr><td>Nuclear Power</td><td><b>7,480 MW</b> installed; private sector entry proposed</td><td class="bi-te">7,480 MW అణు విద్యుత్</td></tr>
<tr><td>Green Hydrogen</td><td>National Green Hydrogen Mission: <b>5 MTPA</b> by 2030</td><td class="bi-te">హరిత హైడ్రోజన్: 2030 నాటికి 5 MTPA</td></tr>
<tr><td>Press Freedom Index</td><td>Rank <b>159</b> (RSF 2024, out of 180)</td><td class="bi-te">ప్రెస్ ఫ్రీడమ్ ర్యాంక్: 159</td></tr>
<tr><td>Ease of Doing Business</td><td>Rank <b>63</b> (World Bank)</td><td class="bi-te">వ్యాపార సులభత: 63వ స్థానం</td></tr>
<tr><td>CPI 2024</td><td>Score <b>39/100</b>; Rank 93 (Transparency International)</td><td class="bi-te">అవినీతి నిరోధక సూచి: 39/100</td></tr>
<tr><td>Coal Production</td><td>India achieved <b>1 billion tonnes</b> target (Coal India + captive); CIL: 773 MT+</td><td class="bi-te">1 బిలియన్ టన్నుల బొగ్గు ఉత్పత్తి లక్ష్యం</td></tr>
<tr><td>Happiness Index</td><td>Finland ranked #1 (WHR 2025); India improved ranking</td><td class="bi-te">ఫిన్లాండ్ 1వ స్థానం (WHR 2025)</td></tr>
</table>

<div class="section-hdr">Agriculture & Food / వ్యవసాయం</div>
<table class="key-table">
<tr><th>Item</th><th>Status</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Milk Production</td><td>India <b>#1 globally</b>; 230 MT+/year</td><td class="bi-te">పాల ఉత్పత్తిలో ప్రపంచ #1</td></tr>
<tr><td>Fisheries</td><td>India <b>#3 globally</b> in fish production</td><td class="bi-te">మత్స్య ఉత్పత్తిలో ప్రపంచ #3</td></tr>
<tr><td>Food Grain</td><td><b>332 MT+</b> (2024-25)</td><td class="bi-te">ఆహార ధాన్య ఉత్పత్తి: 332 MT+</td></tr>
<tr><td>Horticulture</td><td><b>355 MT+</b> fruits &amp; vegetables</td><td class="bi-te">ఉద్యానవన ఉత్పత్తి: 355 MT+</td></tr>
<tr><td>Mica Production</td><td>India <b>#1</b> in mica globally</td><td class="bi-te">అభ్రకం ఉత్పత్తిలో #1</td></tr>
<tr><td>Generic Medicines</td><td>India <b>#1</b> generic pharma exporter globally (Pharmacy of the World)</td><td class="bi-te">జెనెరిక్ ఔషధాల ఎగుమతిలో #1 (ప్రపంచ ఫార్మసీ)</td></tr>
<tr><td>Steel</td><td>India <b>#2</b> steel producer globally</td><td class="bi-te">ఉక్కు ఉత్పత్తిలో ప్రపంచ #2</td></tr>
<tr><td>Petroleum Imports</td><td>$120 billion+ (India is 3rd largest oil importer)</td><td class="bi-te">$120 బిలియన్+ పెట్రోలియం దిగుమతులు</td></tr>
</table>

<div class="section-hdr">Key Welfare Schemes / ముఖ్య సంక్షేమ పథకాలు</div>
<table class="key-table">
<tr><th>Scheme</th><th>Key Data</th><th class="bi-te">వివరణ</th></tr>
<tr><td>PMGKAY</td><td>Free food grains to <b>80 crore</b> people (extended to Dec 2028)</td><td class="bi-te">80 కోట్ల మందికి ఉచిత ఆహారం</td></tr>
<tr><td>PMJDY</td><td><b>53 crore</b> accounts opened (financial inclusion)</td><td class="bi-te">53 కోట్ల జన్‌ధన్ ఖాతాలు</td></tr>
<tr><td>Jal Jeevan Mission</td><td><b>95%+</b> rural households with tap water connections</td><td class="bi-te">95%+ గ్రామీణ గృహాలకు నల్లా నీళ్ళు</td></tr>
<tr><td>Ujjwala Yojana</td><td><b>10 crore</b> LPG connections to BPL households</td><td class="bi-te">10 కోట్ల LPG కనెక్షన్లు</td></tr>
<tr><td>Ayushman Bharat</td><td>₹5 lakh health cover; expanded to 70+ age group; 3,437 crore claims</td><td class="bi-te">₹5 లక్షల ఆరోగ్య బీమా; 70+ వయస్సుకు విస్తరణ</td></tr>
<tr><td>PM Jan Aushadhi</td><td>Generic medicines at 80% discount; 10,000+ stores</td><td class="bi-te">80% తక్కువ ధరకు జనరిక్ ఔషధాలు</td></tr>
<tr><td>PMFBY (Crop Insurance)</td><td>PM Fasal Bima Yojana; covers 5 crore+ farmers</td><td class="bi-te">PM ఫసల్ బీమా; 5 కోట్ల+ రైతులు</td></tr>
<tr><td>PM Vishwakarma</td><td>₹13,000 crore for traditional artisans/craftsmen; tool kits + training</td><td class="bi-te">సంప్రదాయ కళాకారులకు ₹13,000 కోట్లు</td></tr>
<tr><td>SBM ODF+</td><td>1,00,000+ villages declared ODF Plus (solid waste management)</td><td class="bi-te">1 లక్ష+ గ్రామాలు ODF Plus</td></tr>
<tr><td>NRLM SHG</td><td>90 lakh+ Self Help Groups under NRLM</td><td class="bi-te">90 లక్షల+ స్వయం సహాయ బృందాలు</td></tr>
<tr><td>ONDC</td><td>Open Network for Digital Commerce; <b>1 crore+</b> daily orders; under Commerce Ministry</td><td class="bi-te">1 కోటి+ రోజువారీ ఆర్డర్లు</td></tr>
<tr><td>DigiYatra</td><td>Biometric boarding at 24+ airports; paperless air travel</td><td class="bi-te">24+ విమానాశ్రయాలలో బయోమెట్రిక్ బోర్డింగ్</td></tr>
<tr><td>5G</td><td>Launched Oct 2022; <b>20 crore+</b> 5G users by 2026</td><td class="bi-te">అక్టోబర్ 2022; 20 కోట్ల+ 5G వినియోగదారులు</td></tr>
<tr><td>Aadhaar</td><td><b>138 crore+</b> Aadhaar enrolled</td><td class="bi-te">138 కోట్ల+ ఆధార్ నమోదు</td></tr>
<tr><td>AIIMS</td><td><b>22 AIIMS</b> operational across India</td><td class="bi-te">22 AIIMS దేశవ్యాప్తంగా</td></tr>
<tr><td>PM ABHIM</td><td>1,50,000+ Health &amp; Wellness Centres (Ayushman Arogya Mandirs)</td><td class="bi-te">1.5 లక్ష+ ఆయుష్మాన్ ఆరోగ్య మందిరాలు</td></tr>
<tr><td>PM E-DRIVE</td><td>EV adoption; target: 30% EV by 2030; import duty cut to 15%</td><td class="bi-te">2030 నాటికి 30% EV; దిగుమతి సుంకం 15%</td></tr>
<tr><td>Vande Bharat Trains</td><td><b>136+</b> Vande Bharat trains operational</td><td class="bi-te">136+ వందే భారత్ రైళ్ళు</td></tr>
</table>

<div class="section-hdr">International Relations / అంతర్జాతీయ సంబంధాలు</div>
<table class="key-table">
<tr><th>Relationship</th><th>Key Data 2024-26</th><th class="bi-te">వివరణ</th></tr>
<tr><td>India-USA Trade</td><td><b>$190 billion</b> bilateral trade</td><td class="bi-te">$190 బిలియన్ ద్వైపాక్షిక వాణిజ్యం</td></tr>
<tr><td>India-Russia Trade</td><td><b>$66 billion</b> (FY25); India buys discounted Russian oil</td><td class="bi-te">$66 బిలియన్ వాణిజ్యం</td></tr>
<tr><td>QUAD 2025</td><td>Summit in <b>Washington DC</b>; India, USA, Japan, Australia</td><td class="bi-te">వాషింగ్టన్ DC సమావేశం 2025</td></tr>
<tr><td>India-UK FTA</td><td>Free Trade Agreement <b>signed 2025</b></td><td class="bi-te">2025లో భారత-UK FTA సంతకం</td></tr>
<tr><td>IMEC</td><td>India-Middle East-Europe Economic Corridor (G20 2023); New Delhi Declaration</td><td class="bi-te">G20 2023లో IMEC ప్రకటన</td></tr>
<tr><td>India-Africa Forum</td><td>India-Africa Forum Summit held in New Delhi</td><td class="bi-te">న్యూ ఢిల్లీలో భారత-ఆఫ్రికా శిఖరాగ్రం</td></tr>
<tr><td>SCO</td><td>India joined SCO as full member in <b>2017</b></td><td class="bi-te">2017లో SCO పూర్ణ సభ్యత్వం</td></tr>
<tr><td>BRICS</td><td>4 new members joined 2024: Egypt, Ethiopia, Iran, UAE (Saudi Arabia + Argentina deferred)</td><td class="bi-te">2024లో 4 కొత్త సభ్యులు చేరారు</td></tr>
<tr><td>BRICS 2025</td><td>Brazil holds BRICS presidency 2025</td><td class="bi-te">బ్రెజిల్ 2025 BRICS అధ్యక్షత</td></tr>
<tr><td>Bangladesh 2024</td><td>Sheikh Hasina resigned Aug 2024 (quota protests); Muhammad Yunus interim PM</td><td class="bi-te">బంగ్లాదేశ్ కోటా నిరసనలు ఆగస్ట్ 2024</td></tr>
<tr><td>WTO DG</td><td><b>Ngozi Okonjo-Iweala</b> (Nigeria) — since 2021</td><td class="bi-te">WTO DG 2021 నుండి</td></tr>
</table>

<div class="section-hdr">NEP 2020 / జాతీయ విద్యా విధానం 2020</div>
<table class="key-table">
<tr><th>Feature</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Structure</td><td><b>5+3+3+4</b> (15 years total)</td><td class="bi-te">5+3+3+4 నిర్మాణం (మొత్తం 15 సంవత్సరాలు)</td></tr>
<tr><td>Mother Tongue</td><td>Medium of instruction up to <b>Grade 5</b> (or Grade 8)</td><td class="bi-te">5వ తరగతి వరకు మాతృభాష</td></tr>
<tr><td>Board Exam</td><td>Holistic Assessment; reduced rote learning</td><td class="bi-te">సమగ్ర మూల్యాంకనం</td></tr>
<tr><td>Higher Education</td><td>4-year UG with multiple entry-exit; Academic Bank of Credits</td><td class="bi-te">4 సంవత్సరాల UG; అకడెమిక్ బ్యాంక్ ఆఫ్ క్రెడిట్స్</td></tr>
</table>

<div class="section-hdr">Key Economic / PSU Data / ముఖ్య ఆర్థిక డేటా</div>
<table class="key-table">
<tr><th>Item</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Unicorns</td><td><b>118+</b> startups (India 3rd globally)</td><td class="bi-te">118+ యూనికార్న్ స్టార్టప్‌లు</td></tr>
<tr><td>MSME Contribution</td><td><b>30%+</b> of GDP; 6.3 crore MSMEs</td><td class="bi-te">GDP లో 30%+ వాటా</td></tr>
<tr><td>PSB Profits</td><td>12 Public Sector Banks; record profits FY24</td><td class="bi-te">12 ప్రభుత్వ రంగ బ్యాంకులు; రికార్డు లాభాలు</td></tr>
<tr><td>NH Construction</td><td><b>34 km/day</b> (target); 1.46 lakh km total NH</td><td class="bi-te">రోజుకు 34 కి.మీ. NH నిర్మాణం</td></tr>
<tr><td>PM CARES Fund</td><td>Established <b>March 2020</b> (COVID-19)</td><td class="bi-te">మార్చి 2020లో COVID-19 కోసం ఏర్పాటు</td></tr>
<tr><td>EPFO Interest</td><td><b>8.15%</b> for FY24</td><td class="bi-te">EPFO 8.15% వడ్డీ రేటు</td></tr>
<tr><td>BharatNet</td><td>Broadband to all Gram Panchayats; 2 lakh+ GPs covered</td><td class="bi-te">అన్ని గ్రామ పంచాయతీలకు బ్రాడ్‌బ్యాండ్</td></tr>
<tr><td>RRTS Delhi-Meerut</td><td>Rapid Rail Transit System; 82 km corridor</td><td class="bi-te">ఢిల్లీ-మీరట్ ర్యాపిడ్ రైల్</td></tr>
<tr><td>Digital Rupee (e-CBDC)</td><td>RBI launched e-Rupee (retail &amp; wholesale CBDC)</td><td class="bi-te">RBI e-రూపీ డిజిటల్ కరెన్సీ</td></tr>
<tr><td>Critical Minerals</td><td>India focuses on Lithium, Cobalt, Nickel, Rare Earth Elements (REE)</td><td class="bi-te">లిథియం, కోబాల్ట్, నికెల్, REE క్రిటికల్ మినరల్స్</td></tr>
<tr><td>India Literacy</td><td><b>77.7%</b> (2011 Census; estimated 80%+ now)</td><td class="bi-te">అక్షరాస్యత 77.7% (2011)</td></tr>
<tr><td>PMEGP</td><td>PM Employment Generation Programme; small mfg &amp; service sector</td><td class="bi-te">చిన్న పరిశ్రమలు, సేవా రంగ ఉపాధి పథకం</td></tr>
<tr><td>NJDG</td><td>National Judicial Data Grid — tracks pending &amp; disposed cases</td><td class="bi-te">న్యాయస్థానాల కేసుల ట్రాకింగ్</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
# Write to DB
# ═══════════════════════════════════════════════════════
cur = conn.cursor()
upserted = 0
for tag, label, label_te, html in NOTES:
    if USE_POSTGRES:
        cur.execute('''
            INSERT INTO concept_notes (tag, label, label_te, html)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (tag) DO UPDATE
              SET label=EXCLUDED.label, label_te=EXCLUDED.label_te, html=EXCLUDED.html
        ''', (tag, label, label_te, html))
    else:
        cur.execute('''
            INSERT OR REPLACE INTO concept_notes (tag, label, label_te, html)
            VALUES (?,?,?,?)
        ''', (tag, label, label_te, html))
    upserted += 1

conn.commit()
conn.close()
print(f'[seed_concept_notes_national] Upserted {upserted} national CA concept notes.')

if __name__ == '__main__':
    print('seed_concept_notes_national.py complete.')
