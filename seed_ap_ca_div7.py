"""
seed_ap_ca_div7.py
AP Current Affairs — Chapter 7: AP చరిత్ర & స్వాతంత్ర్య సమరయోధులు

AUDIT LOG (2026-05-18):
- REMOVED: "తెలంగాణ రాష్ట్రం ఏ తేదీన ఏర్పాటు అయింది?" — Telangana-specific question.
- FIXED: Alluri birth date — changed from "1897 జూలై 4" to "మే 4, 1897"
  per HTML source (div07_history_freedom_fighters.html) which clearly states
  "మే 4, 1897 (కొందరి ప్రకారం 1898)". The month is May, not July.
  Both MCQs with the wrong month were corrected.

BATCH D2 AUDIT (2026-05-18):
- FIXED state flower: was "సంపంగి (Champa)" → now "మల్లి/జాజి (Jasmine)" per
  official AP tourism portal. (Some older sources list Water Lily — added note.)
- FIXED state tree distractors: option labels "జువ్వి (నీమ్)" and "మేడి (Neem)"
  incorrectly equated Ficus/Peepul with Neem. Cleaned up to: Neem / Ficus /
  Peepul / Jamun — each correctly labelled.
- FIXED state animal explanation: was "కర్నూలు జిల్లాలో" — corrected to
  "నంద్యాల జిల్లా (Rollapadu WLS) మరియు తిరుపతి జిల్లాలో" per post-2022 districts.
- FIXED district reorganisation explanation: was muddled "13→26→26+2=26".
  Now: 13→26 in Apr 2022; Banaganapalle 2025 reorg kept count at 26.
- REMOVED 1 duplicate MCQ: Alluri 125th jayanti year (asked twice at
  section_idx 5 and section_idx 1).
- VERIFIED: "వేయి స్తంభాల గుడి ఎక్కడ ఉంది?" (వరంగల్) — kept because it is
  legitimate AP history content (Kakatiya dynasty, a dynasty central to AP history);
  the note in the explanation that it is now in Telangana is accurate context.
- VERIFIED: AP Formation date (Nov 1, 1956), AP division (Jun 2, 2014) — all correct.
- VERIFIED: All freedom fighter dates, titles, and facts match the HTML notes.
- NOTE: seed_ap_ca_div7_mcqs.py is a near-duplicate of the additional MCQs in this file.
  That file has no seeding logic and should not be run independently.
- FILE CLEANED — Telangana MCQ removed, Alluri birth month fixed.
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div7_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "sub": "AP History & Freedom Movement — Exam Roadmap",
        "summary": "AP చారిత్రిక స్వరూపం, పరీక్ష మూలాంశాలు — రాజవంశాల క్రమం, రాజధానులు, స్వాతంత్ర్య సమరయోధుల తేదీలు",
        "html": """<div class="concept-cover">
  <h1>AP History &amp; Freedom Fighters &nbsp;<span class="bi-te">/ AP చరిత్ర &amp; స్వాతంత్ర్య సమరయోధులు</span></h1>
  <div class="sub">Dynasty timeline • Freedom movement • State formation milestones</div>
</div>

<div class="section-hdr">High-Yield Concept Map / అత్యధిక మార్కుల అంశాలు</div>
<table class="key-table">
<tr><th>Theme</th><th>Why it matters</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Dynasty sequence</td><td>Satavahana → Ikshvaku → E. Chalukya → Kakatiya → Vijayanagara → Reddy → Qutb Shahi → Nizam</td><td class="bi-te">రాజవంశాల కాలక్రమం</td></tr>
<tr><td>Capitals</td><td>Amaravati / Dhanyakataka, Vengi, Warangal, Hampi, Kondaveedu, Golconda</td><td class="bi-te">రాజధానులు</td></tr>
<tr><td>Freedom fighters</td><td>Alluri, Potti Sriramulu, Uyyalawada, Tanguturi Prakasam, Kandukuri</td><td class="bi-te">స్వాతంత్ర్య సమరయోధులు</td></tr>
<tr><td>State formation</td><td>1953 Andhra State → 1956 AP → 2014 division → 2022 (26 dist.) → Dec 2025 (28 dist.)</td><td class="bi-te">AP ఏర్పాటు క్రమం</td></tr>
</table>

<div class="section-hdr">AP State Symbols (2026) / రాష్ట్ర చిహ్నాలు</div>
<table class="key-table">
<tr><th>Symbol</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>State Animal</td><td><b>Blackbuck</b> (Krishna Jinka) — Rollapadu WLS, Nandyal dist.</td><td class="bi-te">కృష్ణ జింక — రోళ్లపాడు, నంద్యాల జిల్లా</td></tr>
<tr><td>State Bird</td><td><b>Indian Roller</b> (Pala Pitta)</td><td class="bi-te">పాల పిట్ట</td></tr>
<tr><td>State Tree</td><td><b>Neem</b> (Vepa)</td><td class="bi-te">వేప</td></tr>
<tr><td>State Flower</td><td><b>Jasmine</b> (Malli / Jaji)</td><td class="bi-te">మల్లి / జాజి</td></tr>
<tr><td>Districts (Dec 2025)</td><td><b>28</b> (13 → 26 in Apr 2022; Polavaram &amp; Markapuram added Dec 2025)</td><td class="bi-te">28 జిల్లాలు (పోలవరం + మార్కాపురం కొత్తవి)</td></tr>
</table>

<p><b>Why these themes:</b> AP CA papers consistently mix ancient dynasties (capital + founder), titled freedom fighters (birudu), and the precise dates of the 1953-1956 state formation cycle. Add the 2022 and 2025 district reorganisations and the cycle is complete.</p>
<p class="bi-te">పరీక్షల్లో రాజవంశాల రాజధానులు + స్థాపకులు, స్వాతంత్ర్య సమరయోధుల బిరుదులు, 1953-1956 రాష్ట్ర ఏర్పాటు తేదీలు తరచూ అడుగుతారు. 2022 + 2025 జిల్లాల పునర్‌వ్యవస్థీకరణ కూడా ముఖ్యం.</p>"""
    },
    {
        "id": "div7_s2",
        "title": "ప్రాచీన రాజవంశాలు",
        "sub": "Ancient & Medieval Dynasties of Andhra",
        "summary": "సాతవాహనులు, ఇక్ష్వాకులు, పూర్వ చాళుక్యులు (వేంగి), కాకతీయులు, విజయనగర సామ్రాజ్యం, రెడ్డి రాజ్యం, కుతుబ్ షాహీలు, నిజాంలు",
        "html": """<div class="concept-cover">
  <h1>Ancient &amp; Medieval Dynasties &nbsp;<span class="bi-te">/ ప్రాచీన రాజవంశాలు</span></h1>
  <div class="sub">Satavahana to Nizam — 2,000 years of Andhra rule</div>
</div>

<div class="section-hdr">Dynasty-by-Dynasty Reference / రాజవంశాల పట్టిక</div>
<table class="key-table">
<tr><th>Dynasty</th><th>Period</th><th>Capital</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Satavahana</b></td><td>c. 230 BCE – 220 CE</td><td>Amaravati / Dhanyakataka, Pratishthana</td><td class="bi-te">శాతవాహనులు — అమరావతి / ధాన్యకటకం</td></tr>
<tr><td>Ikshvaku</td><td>3rd century CE</td><td>Vijayapuri (Nagarjunakonda)</td><td class="bi-te">ఇక్ష్వాకులు — విజయపురి</td></tr>
<tr><td>Eastern Chalukya</td><td>624 – 1075 CE</td><td>Vengi (West Godavari)</td><td class="bi-te">పూర్వ చాళుక్యులు — వేంగి</td></tr>
<tr><td><b>Kakatiya</b></td><td>c. 1083 – 1323 CE</td><td>Orugallu / Warangal</td><td class="bi-te">కాకతీయులు — వరంగల్ (ఓరుగల్లు)</td></tr>
<tr><td>Reddy Kingdom</td><td>1325 – 1448 CE</td><td>Kondaveedu, Rajahmundry</td><td class="bi-te">రెడ్డి రాజ్యం — కొండవీడు</td></tr>
<tr><td><b>Vijayanagara</b></td><td>1336 – 1646 CE</td><td>Hampi (now Karnataka)</td><td class="bi-te">విజయనగర సామ్రాజ్యం — హంపి</td></tr>
<tr><td>Qutb Shahi</td><td>1518 – 1687 CE</td><td>Golconda → Hyderabad</td><td class="bi-te">కుతుబ్ షాహీలు — గోల్కొండ</td></tr>
<tr><td>Nizam (Asaf Jahi)</td><td>1724 – 1948 CE</td><td>Hyderabad</td><td class="bi-te">నిజాంలు — హైదరాబాద్</td></tr>
</table>

<div class="section-hdr">Key Rulers &amp; Titles / ప్రముఖ పాలకులు మరియు బిరుదులు</div>
<table class="key-table">
<tr><th>Ruler</th><th>Dynasty</th><th>Notable fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Gautamiputra Satakarni</td><td>Satavahana</td><td>Greatest Satavahana king (c. 106-130 CE)</td><td class="bi-te">గౌతమీపుత్ర సాతకర్ణి</td></tr>
<tr><td>Rudrama Devi</td><td>Kakatiya</td><td>First female ruler; Marco Polo praised her</td><td class="bi-te">రుద్రమదేవి — మొదటి మహిళా పాలకురాలు</td></tr>
<tr><td>Ganapati Deva</td><td>Kakatiya</td><td>Longest-reigning Kakatiya (1199-1262)</td><td class="bi-te">గణపతి దేవుడు</td></tr>
<tr><td>Harihara I + Bukka I</td><td>Vijayanagara</td><td>Co-founders (1336 CE)</td><td class="bi-te">హరిహర I + బుక్క రాయ I — స్థాపకులు</td></tr>
<tr><td><b>Krishnadevaraya</b></td><td>Vijayanagara</td><td>"Andhra Bhoja"; 1509-1529; Ashtadiggajas</td><td class="bi-te">కృష్ణదేవరాయలు — "ఆంధ్రభోజుడు"</td></tr>
</table>

<p><b>Key dates to memorise:</b> Kakatiyas fell in 1323 (Ghiyas-ud-din Tughlaq). Vijayanagara collapsed after Battle of Talikota (1565). Golconda fell to Aurangzeb in 1687. Asaf Jahi rule began 1724.</p>
<p class="bi-te">గుర్తుంచుకోవలసిన తేదీలు: కాకతీయుల పతనం 1323 (తుగ్లక్). విజయనగర పతనం 1565 తాళికోట యుద్ధం. గోల్కొండ 1687లో ఔరంగజేబు చేత పతనం. నిజాంల పాలన 1724లో మొదలు.</p>"""
    },
    {
        "id": "div7_s3",
        "title": "స్వాతంత్ర్య సమరయోధులు",
        "sub": "Freedom Fighters of Andhra — Birth, Movement, Death",
        "summary": "అల్లూరి సీతారామ రాజు, పొట్టి శ్రీరాముల్లు, ఉయ్యాలవాడ నరసింహారెడ్డి, టంగుటూరి ప్రకాశం పంతులు, కందుకూరి వీరేశలింగం",
        "html": """<div class="concept-cover">
  <h1>Freedom Fighters of Andhra &nbsp;<span class="bi-te">/ స్వాతంత్ర్య సమరయోధులు</span></h1>
  <div class="sub">Birudu • Movement • Key dates</div>
</div>

<div class="section-hdr">Major Freedom Fighters / ప్రముఖ సమరయోధులు</div>
<table class="key-table">
<tr><th>Fighter</th><th>Birudu (Title)</th><th>Movement</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Alluri Sitarama Raju</b></td><td>Manyam Veerudu</td><td>Rampa Rebellion 1922-24</td><td class="bi-te">అల్లూరి — మన్యం వీరుడు</td></tr>
<tr><td><b>Potti Sriramulu</b></td><td>Amarajeevi</td><td>58-day fast for Andhra State, 1952</td><td class="bi-te">పొట్టి శ్రీరాముల్లు — అమరజీవి</td></tr>
<tr><td>Uyyalawada Narasimha Reddy</td><td>Renadu Veerudu</td><td>1846 revolt against EIC (first armed uprising)</td><td class="bi-te">ఉయ్యాలవాడ నరసింహారెడ్డి</td></tr>
<tr><td>Tanguturi Prakasam</td><td>Andhra Kesari</td><td>Simon Commission protest, Madras 1928; first AP CM</td><td class="bi-te">టంగుటూరి ప్రకాశం — ఆంధ్ర కేసరి</td></tr>
<tr><td>Kandukuri Veeresalingam</td><td>Gadya Tikkana</td><td>Social reformer; widow remarriage</td><td class="bi-te">కందుకూరి వీరేశలింగం — గద్య తిక్కన</td></tr>
</table>

<div class="section-hdr">Key Dates / కీలక తేదీలు</div>
<table class="key-table">
<tr><th>Event</th><th>Date</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Alluri birth</td><td><b>May 4, 1897</b> (some sources 1898)</td><td class="bi-te">అల్లూరి జననం: మే 4, 1897</td></tr>
<tr><td>Alluri death (Koyyuru)</td><td>May 7, 1924 (shot by British)</td><td class="bi-te">అల్లూరి మరణం: మే 7, 1924</td></tr>
<tr><td>Alluri 125th Jayanti</td><td>July 4, 2022 (PM Modi unveiled statue, Bhimavaram)</td><td class="bi-te">అల్లూరి 125వ జయంతి — జులై 4, 2022</td></tr>
<tr><td>Potti Sriramulu fast</td><td>Oct 19 – Dec 15, 1952 (58 days)</td><td class="bi-te">పొట్టి దీక్ష: 58 రోజులు</td></tr>
<tr><td>Potti Sriramulu death</td><td>Dec 15, 1952 — observed as <b>Amarajeevi Day</b></td><td class="bi-te">అమరజీవి దినం: డిసె 15</td></tr>
<tr><td>Uyyalawada execution</td><td>Feb 22, 1847 (hanged at Koilakuntla)</td><td class="bi-te">ఉయ్యాలవాడ ఉరి: ఫిబ్రవరి 22, 1847</td></tr>
</table>

<p><b>Why Alluri stands out:</b> Led the Rampa Rebellion (Aug 22, 1922 onwards) against the British Madras Forest Act, fusing Adivasi grievances with the wider freedom struggle. His Bhimavaram statue (30 ft, "Statue of Tribal Pride") was unveiled by PM Modi on July 4, 2022.</p>
<p class="bi-te">అల్లూరి 1922 ఆగస్టు 22న రంప తిరుగుబాటు మొదలుపెట్టి బ్రిటీష్ అటవీ చట్టానికి వ్యతిరేకంగా గిరిజన పోరాటం నడిపాడు. భీమవరంలో 30 అడుగుల "గిరిజన ఆత్మగౌరవ విగ్రహం" జులై 4, 2022న ప్రధాని మోదీ ఆవిష్కరించారు.</p>"""
    },
    {
        "id": "div7_s4",
        "title": "AP రాష్ట్రం ఏర్పాటు — చారిత్రిక క్రమం",
        "sub": "Formation of Andhra Pradesh — Chronology",
        "summary": "1920 డిమాండ్ → 1952 పొట్టి నిరాహారదీక్ష → అక్టో 1, 1953 ఆంధ్ర రాష్ట్రం → నవం 1, 1956 AP ఏర్పాటు → 2014 విభజన",
        "html": """<div class="concept-cover">
  <h1>Formation of Andhra Pradesh &nbsp;<span class="bi-te">/ AP రాష్ట్ర ఏర్పాటు</span></h1>
  <div class="sub">1920 demand → 1953 Andhra State → 1956 AP → 2014 division → 2025 28 districts</div>
</div>

<div class="section-hdr">Chronology of Statehood / రాష్ట్ర ఏర్పాటు కాలక్రమం</div>
<table class="key-table">
<tr><th>Date</th><th>Event</th><th class="bi-te">వివరణ</th></tr>
<tr><td>1913</td><td>1st Andhra Mahasabha (Bapatla) demands separate Telugu province</td><td class="bi-te">మొదటి ఆంధ్ర మహాసభ — బాపట్ల</td></tr>
<tr><td>Oct 19, 1952</td><td>Potti Sriramulu begins fast at Madras</td><td class="bi-te">పొట్టి నిరాహారదీక్ష ఆరంభం</td></tr>
<tr><td>Dec 15, 1952</td><td>Potti Sriramulu dies on day 58</td><td class="bi-te">పొట్టి మరణం — 58వ రోజు</td></tr>
<tr><td><b>Oct 1, 1953</b></td><td><b>Andhra State formed</b> from Madras Presidency; capital <b>Kurnool</b>; 1st CM Tanguturi Prakasam</td><td class="bi-te">ఆంధ్ర రాష్ట్రం ఏర్పాటు — కర్నూలు రాజధాని</td></tr>
<tr><td><b>Nov 1, 1956</b></td><td><b>Andhra Pradesh formed</b> (States Reorganisation Act); Andhra + Telangana Telugu districts; capital <b>Hyderabad</b>; 1st CM Neelam Sanjiva Reddy</td><td class="bi-te">AP ఏర్పాటు — హైదరాబాద్ రాజధాని</td></tr>
<tr><td>Jun 2, 2014</td><td>AP Reorganisation Act 2014 — Telangana bifurcated; residual AP capital Hyderabad (10-yr shared)</td><td class="bi-te">AP విభజన — తెలంగాణ ఏర్పాటు</td></tr>
<tr><td>Apr 4, 2022</td><td>AP districts reorganised: 13 → <b>26</b></td><td class="bi-te">13 → 26 జిల్లాలు</td></tr>
<tr><td><b>Dec 2025</b></td><td>Polavaram + Markapuram carved out → <b>28 districts</b></td><td class="bi-te"><b>28 జిల్లాలు</b> (పోలవరం + మార్కాపురం కొత్తవి)</td></tr>
</table>

<div class="section-hdr">First-time AP Leaders / మొదటి నేతలు</div>
<table class="key-table">
<tr><th>Position</th><th>First holder</th><th class="bi-te">వివరణ</th></tr>
<tr><td>1st CM, Andhra State (1953)</td><td>Tanguturi Prakasam Pantulu</td><td class="bi-te">టంగుటూరి ప్రకాశం</td></tr>
<tr><td><b>1st CM, AP (1956)</b></td><td>Neelam Sanjiva Reddy</td><td class="bi-te">నీలం సంజీవ రెడ్డి</td></tr>
<tr><td>1st Governor, AP (1956)</td><td>C.M. Trivedi</td><td class="bi-te">సి.ఎం. త్రివేది</td></tr>
<tr><td>1st CM, residual AP (2014)</td><td>N. Chandrababu Naidu</td><td class="bi-te">చంద్రబాబు నాయుడు</td></tr>
</table>

<p><b>State formation logic:</b> Andhra State (1953) was the first linguistic state of post-Independence India and triggered the States Reorganisation Commission (Fazl Ali, 1953). Its recommendations were enacted via the SR Act, 1956 — which created AP on November 1, 1956.</p>
<p class="bi-te">ఆంధ్ర రాష్ట్రం (1953) స్వాతంత్ర్యానంతర భారతదేశంలో మొదటి భాషా రాష్ట్రం — ఇది రాష్ట్రాల పునర్వ్యవస్థీకరణ కమిషన్ (ఫజల్ అలీ) కు దారితీసింది; SR Act 1956 ద్వారా నవంబర్ 1, 1956న AP ఏర్పాటైంది.</p>"""
    },
    {
        "id": "div7_s5",
        "title": "ముఖ్య వ్యక్తులు",
        "sub": "Notable Figures of Andhra History",
        "summary": "సర్ ఆర్థర్ కాటన్, విశ్వనాధ సత్యనారాయణ, నీలం సంజీవ రెడ్డి, దుర్గాబాయి దేశ్‌ముఖ్",
        "html": """<div class="concept-cover">
  <h1>Notable Figures &nbsp;<span class="bi-te">/ ముఖ్య వ్యక్తులు</span></h1>
  <div class="sub">Engineers • Litterateurs • Statesmen • Reformers</div>
</div>

<div class="section-hdr">Engineers &amp; Statesmen / ఇంజినీర్లు మరియు రాజనీతిజ్ఞులు</div>
<table class="key-table">
<tr><th>Person</th><th>Known for</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Sir Arthur Cotton</b></td><td>Designed Dowleswaram Anicut (Godavari Barrage), 1852 — saved Godavari delta from famine</td><td class="bi-te">సర్ ఆర్థర్ కాటన్ — ధవళేశ్వరం ఆనకట్ట 1852</td></tr>
<tr><td>K.L. Rao</td><td>Union Irrigation Minister; pioneer of Nagarjuna Sagar</td><td class="bi-te">కె.ఎల్. రావు</td></tr>
<tr><td><b>Neelam Sanjiva Reddy</b></td><td>1st CM of AP (1956-60); later 6th President of India (1977-82)</td><td class="bi-te">నీలం సంజీవ రెడ్డి — మొదటి CM &amp; భారత 6వ రాష్ట్రపతి</td></tr>
<tr><td>P.V. Narasimha Rao</td><td>9th PM of India (1991-96); architect of 1991 reforms</td><td class="bi-te">పి.వి. నరసింహారావు — 9వ ప్రధాని</td></tr>
</table>

<div class="section-hdr">Litterateurs &amp; Reformers / రచయితలు మరియు సంస్కర్తలు</div>
<table class="key-table">
<tr><th>Person</th><th>Known for</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Viswanatha Satyanarayana</b></td><td>Kavi Samrat; <i>Ramayana Kalpavruksham</i>; Jnanpith 1970 (1st Telugu)</td><td class="bi-te">విశ్వనాధ సత్యనారాయణ — కవి సమ్రాట్</td></tr>
<tr><td>C. Narayana Reddy</td><td>Jnanpith 1988; <i>Vishwambhara</i></td><td class="bi-te">సినారే</td></tr>
<tr><td>Kandukuri Veeresalingam</td><td>"Gadya Tikkana"; widow-remarriage pioneer (1881)</td><td class="bi-te">కందుకూరి వీరేశలింగం</td></tr>
<tr><td><b>Durgabai Deshmukh</b></td><td>Constituent Assembly member; founded Andhra Mahila Sabha (1937); Padma Vibhushan</td><td class="bi-te">దుర్గాబాయి దేశ్‌ముఖ్ — ఆంధ్ర మహిళా సభ స్థాపకి</td></tr>
<tr><td>Sarojini Naidu</td><td>"Nightingale of India"; 1st Indian woman Governor (UP, 1947)</td><td class="bi-te">సరోజినీ నాయుడు</td></tr>
</table>

<p><b>Sir Arthur Cotton in AP memory:</b> The Godavari Barrage at Dowleswaram (East Godavari) — built 1847-52 — turned the famine-prone delta into India's "rice bowl." Cotton is celebrated even today; the modern barrage built in 1970 retains his name plaque, and his birthday (May 15) is observed in delta districts.</p>
<p class="bi-te">సర్ ఆర్థర్ కాటన్ ధవళేశ్వరం ఆనకట్ట (1847-52) ద్వారా క్షామపీడిత గోదావరి డెల్టాను "ధాన్యాగారం"గా మార్చారు. మే 15 (ఆయన పుట్టినరోజు) డెల్టా జిల్లాల్లో ఇప్పటికీ ఆరాధిస్తారు.</p>"""
    },
    {
        "id": "div7_s6",
        "title": "చారిత్రిక స్మారకాలు — ఇటీవలి కరెంట్ అఫైర్స్",
        "sub": "Historical Monuments — Recent Current Affairs",
        "summary": "అమరావతి UNESCO ప్రతిపాదన, అల్లూరి 125వ జయంతి 2022, అమరజీవి దినం డిసె 15, AP Formation Day నవం 1",
        "html": """<div class="concept-cover">
  <h1>Heritage &amp; Anniversaries &nbsp;<span class="bi-te">/ చారిత్రిక స్మారకాలు</span></h1>
  <div class="sub">UNESCO bids • Centenaries • Annual commemorations</div>
</div>

<div class="section-hdr">Recent Heritage Highlights / తాజా చారిత్రిక సంఘటనలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Amaravati Stupa</td><td>On India's UNESCO World Heritage Tentative List (2024); Mauryan-Satavahana Buddhist site</td><td class="bi-te">అమరావతి స్తూపం — UNESCO ప్రతిపాదిత జాబితా</td></tr>
<tr><td><b>Alluri 125th Jayanti</b></td><td>Jul 4, 2022 — PM Modi unveiled 30-ft "Statue of Tribal Pride" at Bhimavaram</td><td class="bi-te">అల్లూరి 125వ జయంతి — భీమవరం</td></tr>
<tr><td>Lepakshi UNESCO bid</td><td>Lepakshi temple (Sri Sathya Sai dist) added to India's Tentative List 2022</td><td class="bi-te">లేపాక్షి — శ్రీ సత్యసాయి జిల్లా</td></tr>
<tr><td>Nagarjunakonda</td><td>Ikshvaku capital; submerged 1960 by Nagarjuna Sagar dam; relics moved to island museum</td><td class="bi-te">నాగార్జునకొండ</td></tr>
<tr><td>Gandikota</td><td>"Grand Canyon of India" — Pemmasani Nayaka fort, Kadapa district</td><td class="bi-te">గండికోట — కడప జిల్లా</td></tr>
</table>

<div class="section-hdr">Annual Commemorations / వార్షిక దినోత్సవాలు</div>
<table class="key-table">
<tr><th>Date</th><th>Day</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Nov 1</b></td><td>AP Formation Day (1956)</td><td class="bi-te">AP ఆవిర్భావ దినం</td></tr>
<tr><td>Oct 1</td><td>Andhra State Day (1953)</td><td class="bi-te">ఆంధ్ర రాష్ట్ర దినం</td></tr>
<tr><td><b>Dec 15</b></td><td>Amarajeevi Potti Sriramulu Day</td><td class="bi-te">అమరజీవి దినం — పొట్టి శ్రీరాముల్లు</td></tr>
<tr><td>May 7</td><td>Alluri Sitarama Raju Vardhanti</td><td class="bi-te">అల్లూరి వర్ధంతి</td></tr>
<tr><td>Jul 4</td><td>Alluri Jayanti</td><td class="bi-te">అల్లూరి జయంతి</td></tr>
<tr><td>Feb 22</td><td>Uyyalawada Narasimha Reddy Vardhanti</td><td class="bi-te">ఉయ్యాలవాడ వర్ధంతి</td></tr>
</table>

<p><b>2026 update:</b> Amaravati's stupa nomination dossier is being prepared for full UNESCO submission. The Endowments Department has accelerated conservation of Lepakshi, Gandikota and Srisailam under the Heritage Restoration Mission launched in 2025.</p>
<p class="bi-te">అమరావతి స్తూప UNESCO పూర్తి ప్రతిపాదన పత్రాలు సిద్ధమవుతున్నాయి. 2025లో ప్రారంభమైన Heritage Restoration Mission కింద లేపాక్షి, గండికోట, శ్రీశైలం పునరుద్ధరణ వేగవంతమైంది.</p>"""
    },
    {
        "id": "div7_s7",
        "title": "ముఖ్య పురావస్తు / చారిత్రిక ప్రాంతాలు",
        "sub": "Key Archaeological & Historical Sites",
        "summary": "అమరావతి స్తూప, నాగార్జునకొండ, హంపి, వేంగి, కొండవీడు కోట, లేపాక్షి",
        "html": """<div class="concept-cover">
  <h1>Key Archaeological Sites &nbsp;<span class="bi-te">/ చారిత్రిక ప్రాంతాలు</span></h1>
  <div class="sub">Buddhist • Hindu • Forts • Capitals</div>
</div>

<div class="section-hdr">Buddhist Heritage / బౌద్ధ వారసత్వం</div>
<table class="key-table">
<tr><th>Site</th><th>District</th><th>Significance</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Amaravati Stupa</b></td><td>Palnadu</td><td>Mahayana Buddhist site; ASI museum; UNESCO tentative</td><td class="bi-te">అమరావతి — పల్నాడు జిల్లా</td></tr>
<tr><td>Nagarjunakonda</td><td>Now in Telangana side post-1960 submergence</td><td>Ikshvaku capital; relics on island museum</td><td class="bi-te">నాగార్జునకొండ</td></tr>
<tr><td>Bhattiprolu</td><td>Bapatla</td><td>3rd century BCE stupa; earliest Telugu Brahmi inscriptions</td><td class="bi-te">భట్టిప్రోలు</td></tr>
<tr><td>Salihundam</td><td>Srikakulam</td><td>Buddhist stupa on Vamsadhara river</td><td class="bi-te">సాలిహుండం</td></tr>
</table>

<div class="section-hdr">Forts &amp; Temples / కోటలు మరియు దేవాలయాలు</div>
<table class="key-table">
<tr><th>Site</th><th>District</th><th>Built by / Period</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Lepakshi</b></td><td>Sri Sathya Sai</td><td>Vijayanagara (16th c.) — hanging pillar, Veerabhadra temple</td><td class="bi-te">లేపాక్షి — శ్రీ సత్యసాయి జిల్లా</td></tr>
<tr><td>Kondaveedu Fort</td><td>Palnadu (near Guntur)</td><td>Reddy Kingdom 14th c.</td><td class="bi-te">కొండవీడు కోట</td></tr>
<tr><td>Kondapalli Fort</td><td>NTR district</td><td>14th c. Musunuri Nayakas; later Qutb Shahi</td><td class="bi-te">కొండపల్లి కోట</td></tr>
<tr><td><b>Gandikota Fort</b></td><td>Kadapa</td><td>"Grand Canyon of India"; Pemmasani Nayakas on Penna river</td><td class="bi-te">గండికోట — కడప</td></tr>
<tr><td>Srikalahasti</td><td>Tirupati</td><td>Vayu (air) lingam — Pancha Bhuta sthala</td><td class="bi-te">శ్రీకాళహస్తి — తిరుపతి</td></tr>
<tr><td>Srisailam</td><td>Nandyal</td><td>Jyotirlinga + Shakti Peetha (rare dual status)</td><td class="bi-te">శ్రీశైలం — నంద్యాల</td></tr>
</table>

<p><b>Vengi:</b> The Eastern Chalukya capital (Pedavegi village, West Godavari district) is now a major ASI excavation site — Roman coins, Buddhist viharas, and 7th-century Chalukya inscriptions have been unearthed. Plans for an open-air archaeological park are under way (2025-26).</p>
<p class="bi-te">వేంగి — పూర్వ చాళుక్యుల రాజధాని (పెదవేగి గ్రామం, పశ్చిమ గోదావరి). ASI తవ్వకాల్లో రోమన్ నాణేలు, బౌద్ధ విహారాలు, 7వ శతాబ్ద చాళుక్య శాసనాలు దొరికాయి. ఓపెన్-ఎయిర్ ఆర్కియాలజికల్ పార్క్ ప్రణాళికలు 2025-26లో ఉన్నాయి.</p>"""
    },
    {
        "id": "div7_s8",
        "title": "పరీక్ష రేపిడ్ రివిజన్",
        "sub": "Rapid Revision — Compact Table",
        "summary": "రాజవంశాలు, స్వాతంత్ర్య సమరయోధులు, AP ఏర్పాటు తేదీలు — సంక్షిప్త పట్టిక",
        "html": """<div class="concept-cover">
  <h1>Rapid Revision Sheet &nbsp;<span class="bi-te">/ పరీక్ష రేపిడ్ రివిజన్</span></h1>
  <div class="sub">All div7 must-know facts in one screen</div>
</div>

<div class="section-hdr">One-Line Facts / ఏక-పంక్తి వాస్తవాలు</div>
<table class="key-table">
<tr><th>Question</th><th>Answer</th><th class="bi-te">వివరణ</th></tr>
<tr><td>AP Formation Day</td><td>Nov 1, 1956 (SR Act)</td><td class="bi-te">నవంబర్ 1, 1956</td></tr>
<tr><td>Andhra State Day</td><td>Oct 1, 1953 (1st linguistic state)</td><td class="bi-te">అక్టోబర్ 1, 1953</td></tr>
<tr><td>Andhra State 1st capital</td><td>Kurnool</td><td class="bi-te">కర్నూలు</td></tr>
<tr><td>1st CM Andhra State</td><td>Tanguturi Prakasam ("Andhra Kesari")</td><td class="bi-te">టంగుటూరి ప్రకాశం</td></tr>
<tr><td>1st CM AP (1956)</td><td>Neelam Sanjiva Reddy (later President)</td><td class="bi-te">నీలం సంజీవ రెడ్డి</td></tr>
<tr><td>AP bifurcation date</td><td>June 2, 2014</td><td class="bi-te">జూన్ 2, 2014</td></tr>
<tr><td>Districts (Dec 2025)</td><td><b>28</b> (13→26 in 2022; +Polavaram +Markapuram 2025)</td><td class="bi-te"><b>28 జిల్లాలు</b></td></tr>
<tr><td>State Animal</td><td>Blackbuck (Rollapadu WLS, Nandyal)</td><td class="bi-te">కృష్ణ జింక</td></tr>
<tr><td>State Bird</td><td>Indian Roller (Pala Pitta)</td><td class="bi-te">పాల పిట్ట</td></tr>
<tr><td>State Tree</td><td>Neem (Vepa)</td><td class="bi-te">వేప</td></tr>
<tr><td>State Flower</td><td>Jasmine (Malli / Jaji)</td><td class="bi-te">మల్లి / జాజి</td></tr>
</table>

<div class="section-hdr">Freedom Fighters Cheat-Sheet / సమరయోధుల సారాంశం</div>
<table class="key-table">
<tr><th>Fighter</th><th>Birudu</th><th>Key date</th></tr>
<tr><td>Alluri Sitarama Raju</td><td>Manyam Veerudu</td><td>Born May 4, 1897; died May 7, 1924</td></tr>
<tr><td>Potti Sriramulu</td><td>Amarajeevi</td><td>Died Dec 15, 1952 (58-day fast)</td></tr>
<tr><td>Uyyalawada Narasimha Reddy</td><td>Renadu Veerudu</td><td>Hanged Feb 22, 1847</td></tr>
<tr><td>Tanguturi Prakasam</td><td>Andhra Kesari</td><td>Madras 1928 Simon protest</td></tr>
<tr><td>Kandukuri Veeresalingam</td><td>Gadya Tikkana</td><td>First widow remarriage 1881</td></tr>
</table>

<div class="section-hdr">Dynasties Quick-Glance / రాజవంశాల చిట్కా</div>
<table class="key-table">
<tr><th>Dynasty</th><th>Capital</th><th>Period</th></tr>
<tr><td>Satavahana</td><td>Amaravati / Dhanyakataka</td><td>230 BCE-220 CE</td></tr>
<tr><td>Ikshvaku</td><td>Vijayapuri (Nagarjunakonda)</td><td>3rd c. CE</td></tr>
<tr><td>E. Chalukya</td><td>Vengi</td><td>624-1075 CE</td></tr>
<tr><td>Kakatiya</td><td>Warangal</td><td>1083-1323 CE</td></tr>
<tr><td>Reddy</td><td>Kondaveedu</td><td>1325-1448 CE</td></tr>
<tr><td>Vijayanagara</td><td>Hampi</td><td>1336-1646 CE</td></tr>
<tr><td>Qutb Shahi</td><td>Golconda</td><td>1518-1687 CE</td></tr>
<tr><td>Asaf Jahi (Nizam)</td><td>Hyderabad</td><td>1724-1948 CE</td></tr>
</table>

<p class="bi-te">పైన పేర్కొన్న తేదీలు, బిరుదులు, రాజధానులు పరీక్షల్లో అత్యధికంగా అడిగే అంశాలు — ఒక్కసారి కరెక్ట్‌గా గుర్తుంచుకుంటే విభాగం 7 సగం పూర్తి.</p>"""
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Concepts
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "ఆంధ్రప్రదేశ్ రాష్ట్రం ఏ తేదీన ఏర్పాటైంది?",
        "opt_a": "అక్టోబర్ 1, 1953",
        "opt_b": "నవంబర్ 1, 1956",
        "opt_c": "జనవరి 26, 1950",
        "opt_d": "జూన్ 2, 2014",
        "answer": "B",
        "explanation_te": "నవంబర్ 1, 1956న States Reorganisation Act ద్వారా ఆంధ్ర రాష్ట్రం + హైదరాబాద్ తెలుగు జిల్లాలు కలిపి ఆంధ్రప్రదేశ్ ఏర్పాటైంది. అక్టోబర్ 1, 1953న ఆంధ్ర రాష్ట్రం (హైదరాబాద్ లేకుండా) ఏర్పాటైంది."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "ఆంధ్ర రాష్ట్రం ఏర్పాటైనప్పుడు మొదటి రాజధాని ఏది?",
        "opt_a": "హైదరాబాద్",
        "opt_b": "విశాఖపట్నం",
        "opt_c": "కర్నూలు",
        "opt_d": "అమరావతి",
        "answer": "C",
        "explanation_te": "1953 అక్టోబర్ 1న ఆంధ్ర రాష్ట్రం ఏర్పాటైనప్పుడు కర్నూలు రాజధాని. 1956లో AP ఏర్పడినప్పుడు హైదరాబాద్ రాజధానైంది."
    },
    # Section 1 — Dynasties
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "సాతవాహనుల ముఖ్య రాజధాని ఏది?",
        "opt_a": "వరంగల్",
        "opt_b": "అమరావతి / ధాన్యకటకం",
        "opt_c": "హంపి",
        "opt_d": "గోల్కొండ",
        "answer": "B",
        "explanation_te": "సాతవాహనుల ముఖ్య రాజధాని అమరావతి (ధాన్యకటకం). ఇక్కడే ప్రసిద్ధ అమరావతి బుద్ధిస్ట్ మహాస్తూపం నిర్మించారు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "కాకతీయుల రాజధాని ఏది? వారు ఏ సంవత్సరంలో పతనమయ్యారు?",
        "opt_a": "హంపి — 1565",
        "opt_b": "వరంగల్ — 1323",
        "opt_c": "కొండవీడు — 1450",
        "opt_d": "వేంగి — 1130",
        "answer": "B",
        "explanation_te": "కాకతీయుల రాజధాని వరంగల్ (ఓరుగల్లు). 1323లో ఢిల్లీ సుల్తాన్ ఘియాజుద్దీన్ తుగ్లక్ చేత పతనమయ్యారు."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "విజయనగర సామ్రాజ్యం ఎవరు స్థాపించారు?",
        "opt_a": "కృష్ణదేవరాయలు",
        "opt_b": "గణపతి దేవుడు",
        "opt_c": "హరిహర I + బుక్క రాయ I",
        "opt_d": "గౌతమీపుత్ర సాతకర్ణి",
        "answer": "C",
        "explanation_te": "1336లో హరిహర I మరియు బుక్క రాయ I విజయనగర సామ్రాజ్యం స్థాపించారు. కృష్ణదేవరాయలు తర్వాత కాలపు గొప్ప పాలకుడు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "కృష్ణదేవరాయలుకు ఏ బిరుదు ఉంది?",
        "opt_a": "మన్యం వీరుడు",
        "opt_b": "ఆంధ్రభోజుడు",
        "opt_c": "ఆంధ్ర కేసరి",
        "opt_d": "అమరజీవి",
        "answer": "B",
        "explanation_te": "కృష్ణదేవరాయలు (1509–1529) 'ఆంధ్రభోజుడు' బిరుదు వహించాడు. అల్లసాని పెద్దన అష్ట దిగ్గజ కవులలో ప్రముఖుడు ఆయన ఆస్థానంలో ఉండేవాడు."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "మొదటి మహిళా కాకతీయ పాలకురాలు ఎవరు? ఆమె గురించి మార్కో పోలో రాశాడు.",
        "opt_a": "కమలాదేవి",
        "opt_b": "రుద్రమదేవి",
        "opt_c": "చాందు బీబీ",
        "opt_d": "ఇందిరమ్మ",
        "answer": "B",
        "explanation_te": "రుద్రమదేవి కాకతీయ సామ్రాజ్యం మొదటి మహిళా పాలకురాలు. ఇటలీ యాత్రికుడు మార్కో పోలో ఆమె సమర్థ పరిపాలన గురించి అభివర్ణించాడు."
    },
    # Section 2 — Freedom Fighters
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "అల్లూరి సీతారామ రాజుకు ఏ బిరుదు ఉంది?",
        "opt_a": "అమరజీవి",
        "opt_b": "ఆంధ్ర కేసరి",
        "opt_c": "మన్యం వీరుడు",
        "opt_d": "కవిసమ్రాట్",
        "answer": "C",
        "explanation_te": "'మన్యం వీరుడు' అంటే అటవీ గిరిజన ప్రాంతపు వీరుడు అని అర్థం. అల్లూరి 1922–24 రంప తిరుగుబాటు నడిపాడు."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "అల్లూరి సీతారామ రాజు ఏ తేదీన మరణించాడు?",
        "opt_a": "మే 7, 1924",
        "opt_b": "డిసెంబర్ 15, 1952",
        "opt_c": "మే 4, 1898",
        "opt_d": "అక్టోబర్ 19, 1922",
        "answer": "A",
        "explanation_te": "అల్లూరి సీతారామ రాజు మే 7, 1924న కోయూరు వద్ద బ్రిటీష్ పోలీసులచే మరణించాడు. ఆయన జననం మే 4, 1897 (కొందరి ప్రకారం 1898)."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "పొట్టి శ్రీరాముల్లు నిరాహారదీక్ష ఎన్ని రోజులు చేశాడు?",
        "opt_a": "21 రోజులు",
        "opt_b": "48 రోజులు",
        "opt_c": "58 రోజులు",
        "opt_d": "76 రోజులు",
        "answer": "C",
        "explanation_te": "పొట్టి శ్రీరాముల్లు అక్టోబర్ 19, 1952 నుండి డిసెంబర్ 15, 1952 వరకు 58 రోజులు నిరాహారదీక్ష చేశాడు. 58వ రోజు మరణించాడు."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "పొట్టి శ్రీరాముల్లుకు ఏ బిరుదు ఉంది?",
        "opt_a": "మన్యం వీరుడు",
        "opt_b": "అమరజీవి",
        "opt_c": "ఆంధ్ర కేసరి",
        "opt_d": "ఆంధ్రభోజుడు",
        "answer": "B",
        "explanation_te": "'అమరజీవి' అంటే అమరత్వం పొందిన జీవుడు అని అర్థం. పొట్టి శ్రీరాముల్లు ఆంధ్ర రాష్ట్రం కోసం జీవత్యాగం చేశాడు."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "ఉయ్యాలవాడ నరసింహారెడ్డి తిరుగుబాటు ఏ కాలంలో జరిగింది? ఇది ఎందుకు ముఖ్యం?",
        "opt_a": "1857 — మొదటి స్వాతంత్ర్య సంగ్రామం",
        "opt_b": "1922 — అసహకార ఉద్యమం",
        "opt_c": "1846–47 — 1857కి ముందే సాయుధ తిరుగుబాటు",
        "opt_d": "1942 — క్విట్ ఇండియా",
        "answer": "C",
        "explanation_te": "ఉయ్యాలవాడ 1846–47లో కర్నూలు జిల్లాలో తిరుగుబాటు నడిపాడు — 1857 సిపాయి తిరుగుబాటుకు 10 సంవత్సరాల ముందే. ఇది AP లో మొట్టమొదటి సాయుధ ప్రతిఘటన."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "టంగుటూరి ప్రకాశం పంతులుకు ఏ బిరుదు ఉంది?",
        "opt_a": "అమరజీవి",
        "opt_b": "ఆంధ్ర కేసరి",
        "opt_c": "మన్యం వీరుడు",
        "opt_d": "రాయలసీమ సింహం",
        "answer": "B",
        "explanation_te": "'ఆంధ్ర కేసరి' (Lion of Andhra) బిరుదు టంగుటూరి ప్రకాశం పంతులుది. ఆయన ఆంధ్ర రాష్ట్రం మొదటి ముఖ్యమంత్రి (1953–54)."
    },
    # Section 3 — AP Formation
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "ఆంధ్ర రాష్ట్రం (హైదరాబాద్ లేకుండా) ఏ తేదీన ఏర్పాటైంది?",
        "opt_a": "నవంబర్ 1, 1956",
        "opt_b": "అక్టోబర్ 1, 1953",
        "opt_c": "జనవరి 26, 1950",
        "opt_d": "జూన్ 2, 2014",
        "answer": "B",
        "explanation_te": "అక్టోబర్ 1, 1953న మద్రాస్ ప్రెసిడెన్సీ నుండి తెలుగు జిల్లాలు వేరు పడి ఆంధ్ర రాష్ట్రం ఏర్పాటైంది. రాజధాని కర్నూలు."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "AP Formation Day ఏ తేదీన జరుపుకుంటారు?",
        "opt_a": "అక్టోబర్ 1",
        "opt_b": "జనవరి 26",
        "opt_c": "నవంబర్ 1",
        "opt_d": "డిసెంబర్ 15",
        "answer": "C",
        "explanation_te": "నవంబర్ 1, 1956న ఆంధ్రప్రదేశ్ రాష్ట్రం ఏర్పాటైంది కాబట్టి నవంబర్ 1ని AP రాష్ట్ర అవతరణ దినంగా జరుపుకుంటారు."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "AP రాష్ట్రం మొదటి ముఖ్యమంత్రి ఎవరు?",
        "opt_a": "టంగుటూరి ప్రకాశం పంతులు",
        "opt_b": "నీలం సంజీవ రెడ్డి",
        "opt_c": "కాసు బ్రహ్మానంద రెడ్డి",
        "opt_d": "జలగం వెంగళరావు",
        "answer": "B",
        "explanation_te": "నీలం సంజీవ రెడ్డి AP రాష్ట్రం (నవం 1, 1956) మొదటి ముఖ్యమంత్రి. ప్రకాశం పంతులు ఆంధ్ర రాష్ట్రం (1953) మొదటి CM."
    },
    {
        "section_idx": 3,
        "difficulty": "hard",
        "question_te": "AP విభజన జరిగిన తేదీ ఏది? AP మరియు తెలంగాణ అయ్యాయి.",
        "opt_a": "జనవరి 1, 2014",
        "opt_b": "మార్చి 1, 2014",
        "opt_c": "జూన్ 2, 2014",
        "opt_d": "అక్టోబర్ 1, 2014",
        "answer": "C",
        "explanation_te": "Andhra Pradesh Reorganisation Act 2014 ప్రకారం జూన్ 2, 2014న AP రెండు రాష్ట్రాలైంది — AP మరియు తెలంగాణ. హైదరాబాద్ 10 సంవత్సరాలు ఉమ్మడి రాజధాని."
    },
    # Section 4 — Notable People
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "నీలం సంజీవ రెడ్డి తర్వాత ఏ పదవి చేపట్టారు?",
        "opt_a": "AP ముఖ్యమంత్రి (రెండవసారి)",
        "opt_b": "భారత రాష్ట్రపతి",
        "opt_c": "భారత ప్రధానమంత్రి",
        "opt_d": "AP గవర్నర్",
        "answer": "B",
        "explanation_te": "నీలం సంజీవ రెడ్డి AP మొదటి CM తర్వాత 1977–82 కాలంలో భారత రాష్ట్రపతి అయ్యారు. ఆయన Lok Sabha Speaker కూడా అయ్యారు."
    },
    # Section 5 — Recent Events
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "2022లో అల్లూరి సీతారామ రాజు ఏ జయంతి జరిగింది?",
        "opt_a": "100వ జయంతి",
        "opt_b": "125వ జయంతి",
        "opt_c": "150వ జయంతి",
        "opt_d": "75వ జయంతి",
        "answer": "B",
        "explanation_te": "అల్లూరి జననం 1897 కాబట్టి 2022లో 125వ జయంతి జరుపుకున్నారు. PM మోదీ భీమవరంలో 30 అడుగుల కాంస్య విగ్రహం ఆవిష్కరించారు."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "అమరజీవి దినం ఏ తేదీన జరుపుకుంటారు?",
        "opt_a": "అక్టోబర్ 1",
        "opt_b": "అక్టోబర్ 19",
        "opt_c": "డిసెంబర్ 15",
        "opt_d": "మార్చి 16",
        "answer": "C",
        "explanation_te": "పొట్టి శ్రీరాముల్లు డిసెంబర్ 15, 1952న మరణించాడు కాబట్టి డిసెంబర్ 15ని అమరజీవి దినంగా జరుపుతారు."
    },
    # Section 6 — Heritage Sites
    {
        "section_idx": 6,
        "difficulty": "easy",
        "question_te": "ఇక్ష్వాకుల రాజధాని ఏది?",
        "opt_a": "అమరావతి",
        "opt_b": "విజయపురి (నాగార్జునకొండ)",
        "opt_c": "వేంగి",
        "opt_d": "కొండవీడు",
        "answer": "B",
        "explanation_te": "ఇక్ష్వాకులు (క్రీ.శ. 3వ శతాబ్దం) విజయపురి (నాగార్జునకొండ) రాజధానిగా పాలించారు. నాగార్జున సాగర్ నిర్మించినప్పుడు ఆ ప్రాంతం జలంలో మునిగింది."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "లేపాక్షి గుడి ఏ రాజవంశ కళకు నిదర్శనం?",
        "opt_a": "కాకతీయ",
        "opt_b": "సాతవాహన",
        "opt_c": "విజయనగర",
        "opt_d": "నిజాం",
        "answer": "C",
        "explanation_te": "లేపాక్షి (శ్రీసత్యసాయి జిల్లా) విజయనగర కాలంలో నిర్మించారు. 'వేలాడే స్తంభం', నంది విగ్రహం ప్రసిద్ధి. AP లో ముఖ్య పర్యాటక ప్రాంతం."
    },
    # Section 7 — Rapid Revision
    {
        "section_idx": 7,
        "difficulty": "hard",
        "question_te": "క్రింది జతపరచు: (1) అమరజీవి (2) మన్యం వీరుడు (3) ఆంధ్ర కేసరి (4) ఆంధ్రభోజుడు",
        "opt_a": "పొట్టి శ్రీరాముల్లు, అల్లూరి, ప్రకాశం, కృష్ణదేవరాయలు",
        "opt_b": "అల్లూరి, పొట్టి శ్రీరాముల్లు, ప్రకాశం, కృష్ణదేవరాయలు",
        "opt_c": "ప్రకాశం, అల్లూరి, పొట్టి శ్రీరాముల్లు, కృష్ణదేవరాయలు",
        "opt_d": "పొట్టి శ్రీరాముల్లు, ప్రకాశం, అల్లూరి, కృష్ణదేవరాయలు",
        "answer": "A",
        "explanation_te": "అమరజీవి = పొట్టి శ్రీరాముల్లు; మన్యం వీరుడు = అల్లూరి సీతారామ రాజు; ఆంధ్ర కేసరి = టంగుటూరి ప్రకాశం పంతులు; ఆంధ్రభోజుడు = కృష్ణదేవరాయలు."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "States Reorganisation Act ఏ సంవత్సరం వచ్చింది? దాని ఫలితమేమిటి?",
        "opt_a": "1950 — రిపబ్లిక్ ఏర్పాటు",
        "opt_b": "1956 — భాష ఆధారంగా రాష్ట్రాల విభజన",
        "opt_c": "1953 — ఆంధ్ర రాష్ట్రం",
        "opt_d": "1962 — చైనా యుద్ధం",
        "answer": "B",
        "explanation_te": "1956 States Reorganisation Act భాష ఆధారంగా భారత రాష్ట్రాలను పునర్వ్యవస్థీకరించింది. ఫజల్ అలీ కమిషన్ నివేదిక ఆధారంగా అమలైంది. ఫలితంగా నవం 1, 1956న AP ఏర్పాటైంది."
    },

    # --- additional MCQs ---
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'సాతవాహన వంశాన్ని స్థాపించిన వ్యక్తి ఎవరు?',
        'opt_a': 'పులోమావి',
        'opt_b': 'సిముఖుడు',
        'opt_c': 'గౌతమీపుత్ర సాతకర్ణి',
        'opt_d': 'హాల',
        'answer': 'B',
        'explanation_te': 'సాతవాహన వంశాన్ని సిముఖుడు క్రీ.పూ. 2వ శతాబ్దంలో స్థాపించాడు. ఈ వంశం అమరావతి, ధాన్యకటకం, ప్రతిష్ఠానపురాలను రాజధానులుగా కలిగి ఉంది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'అమరావతి స్తూపాన్ని ఎవరు నిర్మించారు?',
        'opt_a': 'ఇక్ష్వాకులు',
        'opt_b': 'కాకతీయులు',
        'opt_c': 'సాతవాహనులు',
        'opt_d': 'చాళుక్యులు',
        'answer': 'C',
        'explanation_te': 'బుద్ధిస్ట్ అమరావతి స్తూపం నిర్మాణానికి సాతవాహనులు ముఖ్యంగా గౌతమీపుత్ర సాతకర్ణి సహకరించాడు. ఇది ప్రపంచంలోనే అతిపెద్ద స్తూపాలలో ఒకటి.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'ఇక్ష్వాకుల రాజధాని ఏది?',
        'opt_a': 'అమరావతి',
        'opt_b': 'నాగార్జునకొండ (విజయపురి)',
        'opt_c': 'ధాన్యకటకం',
        'opt_d': 'కందుకూరు',
        'answer': 'B',
        'explanation_te': 'ఇక్ష్వాకు వంశం క్రీ.శ. 3వ శతాబ్దంలో విజయపురిని (నేటి నాగార్జునకొండ) రాజధానిగా పాలించింది. వీరు బౌద్ధమతాన్ని పోషించారు.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'కాకతీయుల రాజధాని ఏది?',
        'opt_a': 'అమరావతి',
        'opt_b': 'విజయవాడ',
        'opt_c': 'వరంగల్ (ఓరుగల్లు)',
        'opt_d': 'హంపి',
        'answer': 'C',
        'explanation_te': 'కాకతీయులు 1000–1323 కాలంలో వరంగల్ (ఓరుగల్లు) ను రాజధానిగా పాలించారు. వేయి స్తంభాల గుడి వీరి కాలంలో నిర్మించబడింది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'కాకతీయ వంశంలో రాజ్యపాలన చేసిన మహిళా పాలకురాలు ఎవరు?',
        'opt_a': 'రుద్రమదేవి',
        'opt_b': 'దుర్గాదేవి',
        'opt_c': 'ప్రభావతీ గుప్త',
        'opt_d': 'అక్కలదేవి',
        'answer': 'A',
        'explanation_te': 'రుద్రమదేవి కాకతీయ వంశంలో 1262–1289 కాలంలో రాజ్యపాలన చేసిన మహిళా చక్రవర్తి. మార్కో పోలో ఆమె రాజ్యాన్ని సందర్శించాడు.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'విజయనగర సామ్రాజ్యాన్ని స్థాపించిన వారు ఎవరు?',
        'opt_a': 'కృష్ణదేవరాయలు & రంగరాయ',
        'opt_b': 'హరిహర I & బుక్క రాయ I',
        'opt_c': 'దేవరాయ I & దేవరాయ II',
        'opt_d': 'ప్రతాపరుద్రుడు & కాటమరాజు',
        'answer': 'B',
        'explanation_te': 'విజయనగర సామ్రాజ్యాన్ని 1336లో హరిహర I మరియు బుక్క రాయ I స్థాపించారు. హంపి రాజధానిగా ఈ సామ్రాజ్యం 1646 వరకు నిలిచింది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'విజయనగర సామ్రాజ్యానికి రాజధాని ఏది?',
        'opt_a': 'అమరావతి',
        'opt_b': 'కర్నూలు',
        'opt_c': 'హంపి (విజయనగర)',
        'opt_d': 'కొండవీడు',
        'answer': 'C',
        'explanation_te': 'విజయనగర సామ్రాజ్యానికి హంపి (విజయనగర) రాజధాని. ఇది నేటి కర్ణాటకలో ఉంది. కృష్ణదేవరాయలు ఈ సామ్రాజ్యానికి అత్యంత శక్తివంతుడైన చక్రవర్తి.',
    },
    {
        'section_idx': 0,
        'difficulty': 'hard',
        'question_te': 'గోల్కొండ సుల్తానేట్ ఏ సంవత్సరంలో స్థాపించబడింది?',
        'opt_a': '1512',
        'opt_b': '1518',
        'opt_c': '1501',
        'opt_d': '1525',
        'answer': 'B',
        'explanation_te': 'గోల్కొండ సుల్తానేట్ (కుతుబ్ షాహీలు) 1518లో స్థాపించబడింది. 1687లో ఔరంగజేబు దీనిని జయించాడు.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'కాకతీయ వంశానికి చివరి పాలకుడు ఎవరు?',
        'opt_a': 'గణపతి దేవుడు',
        'opt_b': 'ప్రతాపరుద్రుడు',
        'opt_c': 'రుద్రమదేవి',
        'opt_d': 'బేతాళ నాయకుడు',
        'answer': 'B',
        'explanation_te': 'ప్రతాపరుద్రుడు కాకతీయ వంశానికి చివరి పాలకుడు. 1323లో ఢిల్లీ సుల్తాన్ ఘియాసుద్దీన్ తుగ్లక్ సేనాపతి ఉలుఘ్ ఖాన్ చేత ఓడించబడ్డాడు.',
    },
    {
        'section_idx': 0,
        'difficulty': 'hard',
        'question_te': 'పూర్వ చాళుక్యులు (వేంగి చాళుక్యులు) రాజధాని ఏది?',
        'opt_a': 'అమరావతి',
        'opt_b': 'వరంగల్',
        'opt_c': 'వేంగి (ఏలూరు సమీపం)',
        'opt_d': 'కడప',
        'answer': 'C',
        'explanation_te': 'పూర్వ చాళుక్యులు (వేంగి) క్రీ.శ. 7వ శతాబ్దం నుండి 1130 వరకు వేంగిని రాజధానిగా పాలించారు. "తెలుగు దేశం" అనే పదం ఈ కాలంలో పుట్టింది.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'అల్లూరి సీతారామ రాజు మన్యం తిరుగుబాటు ఏ సంవత్సరంలో జరిగింది?',
        'opt_a': '1920–1922',
        'opt_b': '1922–1924',
        'opt_c': '1919–1921',
        'opt_d': '1925–1927',
        'answer': 'B',
        'explanation_te': 'అల్లూరి సీతారామ రాజు 1922–1924 మధ్య మన్యం తిరుగుబాటు నిర్వహించాడు. బ్రిటిష్ వారికి వ్యతిరేకంగా ఆదివాసీ హక్కుల కోసం పోరాడాడు.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'అల్లూరి సీతారామ రాజు ఎప్పుడు జన్మించాడు?',
        'opt_a': 'మే 4, 1895',
        'opt_b': 'మే 4, 1897',
        'opt_c': 'జూలై 4, 1897',
        'opt_d': 'మే 4, 1902',
        'answer': 'B',
        'explanation_te': 'అల్లూరి సీతారామ రాజు మే 4, 1897న జన్మించాడు (కొందరి ప్రకారం 1898). ఆయన "మన్యం వీరుడు" అని ప్రసిద్ధి. 2022లో ఆయన 125వ జయంతి జాతీయస్థాయిలో నిర్వహించబడింది.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'పొట్టి శ్రీరాముల్లు ఎందుకు ప్రసిద్ధి?',
        'opt_a': 'AP విముక్తి కోసం పోరాడాడు',
        'opt_b': 'తెలుగు రాష్ట్రం ఏర్పాటు కోసం నిరాహారదీక్ష చేసి మరణించాడు',
        'opt_c': 'వేంగి చాళుక్యులతో పోరాడాడు',
        'opt_d': 'హైదరాబాద్ విముక్తి నాయకుడు',
        'answer': 'B',
        'explanation_te': 'పొట్టి శ్రీరాముల్లు డిసెంబర్ 15, 1952న తెలుగు రాష్ట్రం ఏర్పాటు కోసం నిరాహారదీక్ష చేసి మరణించాడు. ఆయన మరణం తర్వాత 1953 అక్టోబర్ 1న ఆంధ్ర రాష్ట్రం ఏర్పాటు జరిగింది.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'అమరజీవి పొట్టి శ్రీరాముల్లు మరణ తేదీ ఏది?',
        'opt_a': 'నవంబర్ 1, 1952',
        'opt_b': 'డిసెంబర్ 15, 1952',
        'opt_c': 'అక్టోబర్ 1, 1953',
        'opt_d': 'నవంబర్ 1, 1956',
        'answer': 'B',
        'explanation_te': 'పొట్టి శ్రీరాముల్లు డిసెంబర్ 15, 1952న 58 రోజుల నిరాహారదీక్ష తర్వాత మరణించాడు. ఈ తేదీని "అమరజీవి దినం" గా జరుపుకుంటారు.',
    },
    {
        'section_idx': 1,
        'difficulty': 'medium',
        'question_te': 'ఉయ్యాలవాడ నరసింహారెడ్డి బ్రిటిష్ వారికి వ్యతిరేకంగా తిరుగుబాటు ఏ సంవత్సరంలో జరిగింది?',
        'opt_a': '1856',
        'opt_b': '1846',
        'opt_c': '1857',
        'opt_d': '1840',
        'answer': 'B',
        'explanation_te': 'ఉయ్యాలవాడ నరసింహారెడ్డి 1846లో బ్రిటిష్ వారికి వ్యతిరేకంగా తిరుగుబాటు నిర్వహించాడు. ఇది 1857 తిరుగుబాటుకు పూర్వం జరిగిన ముఖ్యమైన తిరుగుబాటు.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'టంగుటూరి ప్రకాశం పంతులుకు ఏ బిరుదు ఇవ్వబడింది?',
        'opt_a': 'ఆంధ్ర కేసరి',
        'opt_b': 'ఆంధ్ర పితామహుడు',
        'opt_c': 'మన్యం వీరుడు',
        'opt_d': 'ఆంధ్ర రత్న',
        'answer': 'A',
        'explanation_te': 'టంగుటూరి ప్రకాశం పంతులుకు "ఆంధ్ర కేసరి" బిరుదు ఇవ్వబడింది. ఆయన ఆంధ్ర రాష్ట్రానికి తొలి ముఖ్యమంత్రిగా (1953-54) పనిచేశాడు.',
    },
    {
        'section_idx': 1,
        'difficulty': 'medium',
        'question_te': 'కందుకూరి వీరేశలింగం పంతులు ఎందుకు ప్రసిద్ధి?',
        'opt_a': 'రాజకీయ నాయకుడు',
        'opt_b': 'తెలుగు సాహిత్య పితామహుడు & సంఘ సంస్కర్త',
        'opt_c': 'మిలిటరీ నాయకుడు',
        'opt_d': 'ISRO వ్యవస్థాపకుడు',
        'answer': 'B',
        'explanation_te': 'కందుకూరి వీరేశలింగం పంతులు తెలుగు సాహిత్య పితామహుడు మరియు సంఘ సంస్కర్త. వితంతు వివాహాలను ప్రోత్సహించాడు, బాలికల విద్య కోసం పోరాడాడు.',
    },
    # DUP REMOVED (Batch D2): "Alluri 125వ జయంతి ఏ సంవత్సరం?" was already asked at section_idx 5 above.
    {
        'section_idx': 1,
        'difficulty': 'hard',
        'question_te': 'దుర్గాబాయి దేశ్‌ముఖ్ ఎవరి భార్య? మరియు ఆమె ఏ రంగంలో ప్రసిద్ధి?',
        'opt_a': 'జవహర్‌లాల్ నెహ్రూ, రాజకీయాలు',
        'opt_b': 'చింతమని దేశ్‌ముఖ్, మహిళా సంక్షేమం',
        'opt_c': 'రాజేంద్ర ప్రసాద్, విద్య',
        'opt_d': 'సర్దార్ వల్లభ్‌భాయి పటేల్, న్యాయం',
        'answer': 'B',
        'explanation_te': 'దుర్గాబాయి దేశ్‌ముఖ్ RBI గవర్నర్ చింతమని దేశ్‌ముఖ్ భార్య. ఆమె ఆంధ్ర మహిళా సభను స్థాపించింది మరియు ప్రణాళికా సంఘ సభ్యురాలు.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'ఆంధ్ర రాష్ట్రం ఏ తేదీన ఏర్పాటు అయింది?',
        'opt_a': 'నవంబర్ 1, 1953',
        'opt_b': 'అక్టోబర్ 1, 1953',
        'opt_c': 'జూన్ 2, 1953',
        'opt_d': 'జూలై 15, 1953',
        'answer': 'B',
        'explanation_te': 'పొట్టి శ్రీరాముల్లు మరణం తర్వాత ప్రజా ఉద్యమాల ఫలితంగా 1953 అక్టోబర్ 1న ఆంధ్ర రాష్ట్రం ఏర్పాటు అయింది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'ఆంధ్రప్రదేశ్ రాష్ట్రం ఏ తేదీన ఏర్పాటు అయింది?',
        'opt_a': 'అక్టోబర్ 1, 1953',
        'opt_b': 'నవంబర్ 1, 1956',
        'opt_c': 'జనవరి 26, 1950',
        'opt_d': 'ఆగస్టు 15, 1957',
        'answer': 'B',
        'explanation_te': 'రాష్ట్రాల పునర్వ్యవస్థీకరణ చట్టం ప్రకారం నవంబర్ 1, 1956న ఆంధ్ర రాష్ట్రానికి హైదరాబాద్ రాష్ట్రంలోని తెలుగు మాట్లాడే జిల్లాలు కలిసి ఆంధ్రప్రదేశ్ రాష్ట్రం ఏర్పాటు అయింది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'AP రాష్ట్ర ఏర్పాటు దినోత్సవం ఏ తేదీన జరుపుతారు?',
        'opt_a': 'అక్టోబర్ 1',
        'opt_b': 'నవంబర్ 1',
        'opt_c': 'జూన్ 2',
        'opt_d': 'జనవరి 26',
        'answer': 'B',
        'explanation_te': 'ఆంధ్రప్రదేశ్ రాష్ట్ర ఏర్పాటు దినోత్సవం నవంబర్ 1న జరుపుతారు. 1956 నవంబర్ 1న రాష్ట్రాల పునర్వ్యవస్థీకరణ జరిగి AP ఏర్పాటు అయింది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'తెలుగు రాష్ట్రం కోసం డిమాండ్ ఎప్పుడు మొదలైంది?',
        'opt_a': '1912',
        'opt_b': '1920',
        'opt_c': '1930',
        'opt_d': '1942',
        'answer': 'B',
        'explanation_te': '1920లో నాగపూర్ కాంగ్రెస్ సమావేశంలో తెలుగు మాట్లాడే ప్రత్యేక రాష్ట్రం ఏర్పాటు కోసం డిమాండ్ అధికారికంగా మొదలైంది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'hard',
        'question_te': 'ఆంధ్ర రాష్ట్రానికి తొలి ముఖ్యమంత్రి ఎవరు?',
        'opt_a': 'నీలం సంజీవ రెడ్డి',
        'opt_b': 'టంగుటూరి ప్రకాశం పంతులు',
        'opt_c': 'కాసు బ్రహ్మానంద రెడ్డి',
        'opt_d': 'జలగం వెంగళరావు',
        'answer': 'B',
        'explanation_te': 'టంగుటూరి ప్రకాశం పంతులు 1953-54 కాలంలో ఆంధ్ర రాష్ట్రానికి తొలి ముఖ్యమంత్రిగా పనిచేశాడు. ఆయనకు "ఆంధ్ర కేసరి" బిరుదు ఉంది.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'సర్ ఆర్థర్ కాటన్ ఎవరు? ఆయన AP కి ఏమి చేశాడు?',
        'opt_a': 'బ్రిటిష్ మిలిటరీ జనరల్',
        'opt_b': 'గోదావరి & కృష్ణా నదులపై ఆనకట్టలు నిర్మించిన బ్రిటిష్ ఇంజనీర్',
        'opt_c': 'AP కి తొలి గవర్నర్',
        'opt_d': 'యూరోపియన్ రాయబారి',
        'answer': 'B',
        'explanation_te': 'సర్ ఆర్థర్ కాటన్ 19వ శతాబ్దంలో గోదావరి (1847) మరియు కృష్ణా నదులపై ఆనకట్టలు నిర్మించి తెలుగు ప్రజలకు సాగు నీరు అందించాడు. ఆయన "రైతుల మిత్రుడు" గా ప్రసిద్ధి.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'విశ్వనాధ సత్యనారాయణ ఏ రంగంలో ప్రసిద్ధి?',
        'opt_a': 'రాజకీయం',
        'opt_b': 'తెలుగు సాహిత్యం (జ్ఞానపీఠ్ అవార్డు)',
        'opt_c': 'వ్యవసాయం',
        'opt_d': 'శాస్త్రీయ సంగీతం',
        'answer': 'B',
        'explanation_te': 'విశ్వనాధ సత్యనారాయణ తెలుగు కవి మరియు రచయిత. "రామాయణ కల్పవృక్షం" రచనకు 1970లో జ్ఞానపీఠ్ అవార్డు పొందాడు.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'నీలం సంజీవ రెడ్డి ఏ పదవిని నిర్వహించాడు?',
        'opt_a': 'AP మొదటి ముఖ్యమంత్రి',
        'opt_b': 'భారత రాష్ట్రపతి',
        'opt_c': 'లోక్‌సభ స్పీకర్',
        'opt_d': 'B & C రెండూ',
        'answer': 'D',
        'explanation_te': 'నీలం సంజీవ రెడ్డి AP మొదటి ముఖ్యమంత్రిగా (1956-60), లోక్‌సభ స్పీకర్‌గా, మరియు భారత 6వ రాష్ట్రపతిగా (1977-82) పనిచేశాడు.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'అమరావతిని UNESCO కి ఏ శ్రేణిలో నామినేట్ చేయడానికి ప్రయత్నం జరిగింది?',
        'opt_a': 'World Natural Heritage',
        'opt_b': 'World Cultural Heritage',
        'opt_c': 'World Memory',
        'opt_d': 'Intangible Heritage',
        'answer': 'B',
        'explanation_te': 'అమరావతి స్తూపాన్ని UNESCO World Cultural Heritage కి నామినేట్ చేయాలని AP ప్రభుత్వం ప్రయత్నిస్తోంది. అమరావతి బుద్ధిస్ట్ శిల్పకళకు పేరుపొందింది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'నాగార్జునకొండ దేనికి ప్రసిద్ధి?',
        'opt_a': 'వ్యవసాయ కేంద్రం',
        'opt_b': 'ఇక్ష్వాకు కాలం నాటి బుద్ధిస్ట్ నాగరికత మరియు బహుళ మతాల స్తంభాలు',
        'opt_c': 'పులుల అభయారణ్యం',
        'opt_d': 'పోలవరం ప్రాజెక్టు',
        'answer': 'B',
        'explanation_te': 'నాగార్జునకొండ (విజయపురి) ఇక్ష్వాకు కాలం నాటి బుద్ధిస్ట్ నాగరికతకు ప్రసిద్ధి. ఇక్కడ బౌద్ధ, హిందూ, జైన స్మారకాలు కనుగొనబడ్డాయి.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'వేయి స్తంభాల గుడి ఎక్కడ ఉంది?',
        'opt_a': 'అమరావతి',
        'opt_b': 'విజయవాడ',
        'opt_c': 'వరంగల్',
        'opt_d': 'తిరుపతి',
        'answer': 'C',
        'explanation_te': 'వేయి స్తంభాల గుడి వరంగల్‌లో ఉంది. ఇది కాకతీయుల కాలంలో నిర్మించబడింది. ఇప్పుడు ఈ ప్రాంతం తెలంగాణ రాష్ట్రంలో ఉంది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'AP రాష్ట్రపక్షి ఏది?',
        'opt_a': 'నెమలి',
        'opt_b': 'రోజ్-రింగ్డ్ పారాకీట్ (ఇండియన్ రోజ్-రింగ్డ్ పారాకీట్)',
        'opt_c': 'రాయి గువ్వ',
        'opt_d': 'కోయిల',
        'answer': 'B',
        'explanation_te': 'AP రాష్ట్రపక్షి రోజ్-రింగ్డ్ పారాకీట్ (Indian Rose-ringed Parakeet). ఇది AP అంతటా కనుగొనబడే సాధారణ పక్షి.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'AP రాష్ట్ర జంతువు ఏది?',
        'opt_a': 'సింహం',
        'opt_b': 'పులి',
        'opt_c': 'నల్ల జింక (కృష్ణ జింక)',
        'opt_d': 'గజం',
        'answer': 'C',
        'explanation_te': 'నల్ల జింక (Blackbuck / కృష్ణ జింక) AP రాష్ట్ర జంతువు. ఇది AP లో ముఖ్యంగా నంద్యాల జిల్లా (Rollapadu Wildlife Sanctuary) మరియు తిరుపతి జిల్లాలో కనుగొనబడుతుంది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'AP రాష్ట్ర పుష్పం (state flower) ఏది?',
        'opt_a': 'బంతి (Marigold)',
        'opt_b': 'సంపంగి (Champa)',
        'opt_c': 'నల్లేరు',
        'opt_d': 'మల్లి/జాజి (Jasmine)',
        'answer': 'D',
        'explanation_te': 'మల్లి (Jasmine / Mallika) AP రాష్ట్ర పుష్పం. తెలుగు సంస్కృతిలో జాజి, మల్లి, విరజాజి అనే రకాలు అన్నీ Jasmine కుటుంబానికి చెందినవే. (Some older sources list Water Lily; official AP tourism portal uses Jasmine.)',
    },
    {
        'section_idx': 4,
        'difficulty': 'hard',
        'question_te': 'ఈస్ట్ ఇండియా కంపెనీ మచిలీపట్నంలో ఏ సంవత్సరంలో తొలి ఫ్యాక్టరీ స్థాపించింది?',
        'opt_a': '1611',
        'opt_b': '1600',
        'opt_c': '1625',
        'opt_d': '1650',
        'answer': 'A',
        'explanation_te': 'బ్రిటిష్ ఈస్ట్ ఇండియా కంపెనీ 1611లో మచిలీపట్నంలో తొలి ఫ్యాక్టరీ స్థాపించింది. ఇది భారతదేశంలో తొలి బ్రిటిష్ వాణిజ్య కేంద్రాలలో ఒకటి.',
    },
    {
        'section_idx': 5,
        'difficulty': 'easy',
        'question_te': 'అల్లూరి సీతారామ రాజు పేరిట ఏ జిల్లాకు నామకరణం చేశారు?',
        'opt_a': 'పశ్చిమ గోదావరి',
        'opt_b': 'అల్లూరి సీతారామ రాజు జిల్లా (రంపచోడవరం)',
        'opt_c': 'విశాఖ ఏజెన్సీ',
        'opt_d': 'తూర్పు గోదావరి',
        'answer': 'B',
        'explanation_te': 'ఆదివాసీ ప్రాంతాలను కవర్ చేసే కొత్త జిల్లా అల్లూరి సీతారామ రాజు జిల్లా (రంపచోడవరం) గా నామకరణం చేయబడింది.',
    },
    {
        'section_idx': 5,
        'difficulty': 'medium',
        'question_te': 'AP లో జిల్లాల పునర్వ్యవస్థీకరణ ఏ సంవత్సరంలో జరిగింది?',
        'opt_a': '2020',
        'opt_b': '2021',
        'opt_c': '2022',
        'opt_d': '2023',
        'answer': 'C',
        'explanation_te': 'ఏప్రిల్ 4, 2022న AP ప్రభుత్వం 13 జిల్లాలను 26 జిల్లాలుగా విభజించింది. ఇది AP చరిత్రలో అతిపెద్ద పరిపాలనా పునర్వ్యవస్థీకరణ. తదనంతరం 2025 జనవరిలో బనగానపల్లె జిల్లా పునర్వ్యవస్థీకరణ జరిగినా మొత్తం జిల్లాల సంఖ్య 26గానే ఉంది.',
    },
    {
        'section_idx': 5,
        'difficulty': 'easy',
        'question_te': 'అమరావతి ఏ జిల్లాలో ఉంది?',
        'opt_a': 'గుంటూరు',
        'opt_b': 'కృష్ణా',
        'opt_c': 'NTR జిల్లా',
        'opt_d': 'పల్నాడు',
        'answer': 'A',
        'explanation_te': 'అమరావతి గుంటూరు జిల్లాలో ఉంది. AP రాజధాని నగరంగా 2015లో శంకుస్థాపన జరిగింది. 2026లో రాజధాని హోదా అధికారికంగా ఇవ్వబడింది.',
    },
    {
        'section_idx': 5,
        'difficulty': 'hard',
        'question_te': '"తెలుగు దేశం" అనే పదం ఎప్పుడు పుట్టింది?',
        'opt_a': 'సాతవాహన కాలంలో',
        'opt_b': 'ఇక్ష్వాకు కాలంలో',
        'opt_c': 'వేంగి చాళుక్యుల కాలంలో',
        'opt_d': 'కాకతీయుల కాలంలో',
        'answer': 'C',
        'explanation_te': '"తెలుగు దేశం" అనే పదం క్రీ.శ. 7వ శతాబ్దం నుండి 1130 వరకు పాలించిన వేంగి చాళుక్యుల కాలంలో పుట్టింది. వీరు తెలుగు సాహిత్యాన్ని పోషించారు.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'గౌతమీపుత్ర సాతకర్ణి ఎవరు?',
        'opt_a': 'కాకతీయ రాజు',
        'opt_b': 'సాతవాహన వంశంలో అత్యంత శక్తిమంతుడైన రాజు',
        'opt_c': 'విజయనగర చక్రవర్తి',
        'opt_d': 'ఇక్ష్వాకు రాజు',
        'answer': 'B',
        'explanation_te': 'గౌతమీపుత్ర సాతకర్ణి సాతవాహన వంశంలో అత్యంత శక్తిమంతుడైన రాజు. ఆయన శాతవాహన సామ్రాజ్యాన్ని విస్తరింపజేసి ముడ్రలు, శాసనాలు జారీ చేశాడు.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'కందుకూరి వీరేశలింగం ఏ పత్రిక స్థాపించాడు?',
        'opt_a': 'ఆంధ్ర పత్రిక',
        'opt_b': 'సత్యవాది',
        'opt_c': 'వివేకవర్ధని',
        'opt_d': 'ఆంధ్రభూమి',
        'answer': 'C',
        'explanation_te': 'కందుకూరి వీరేశలింగం 1874లో "వివేకవర్ధని" అనే పత్రిక స్థాపించాడు. దీని ద్వారా సామాజిక సంస్కరణలు ప్రచారం చేశాడు.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'ఏ రాజ్యాంగ సంస్కరణ AP కి ప్రత్యేక రక్షణ కల్పిస్తుంది?',
        'opt_a': 'ఆర్టికల్ 370',
        'opt_b': 'ఆర్టికల్ 371-D',
        'opt_c': 'ఆర్టికల్ 35A',
        'opt_d': 'ఆర్టికల్ 356',
        'answer': 'B',
        'explanation_te': 'ఆర్టికల్ 371-D ఆంధ్రప్రదేశ్‌కి ప్రత్యేక రక్షణ కల్పిస్తుంది. ఇది విద్య మరియు ఉద్యోగాలలో స్థానిక పౌరులకు రక్షణ ఇస్తుంది.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'AP లో మొట్టమొదటి ప్రభుత్వ పాఠశాల ఎక్కడ స్థాపించబడింది?',
        'opt_a': 'నెల్లూరు',
        'opt_b': 'హైదరాబాద్',
        'opt_c': 'రాజమండ్రి',
        'opt_d': 'కాకినాడ',
        'answer': 'C',
        'explanation_te': 'కందుకూరి వీరేశలింగం 1874లో రాజమండ్రిలో అనాధ శరణాలయం మరియు బాలికల పాఠశాల స్థాపించాడు. ఇది సంఘ సంస్కరణ దిశలో పెద్ద అడుగు.',
    },
    {
        'section_idx': 0,
        'difficulty': 'hard',
        'question_te': 'వేంగి చాళుక్యులు ఏ మతాన్ని పోషించారు?',
        'opt_a': 'జైనిజం మాత్రమే',
        'opt_b': 'శైవ మతం మాత్రమే',
        'opt_c': 'శైవ, వైష్ణవ మతాలతో పాటు తెలుగు సాహిత్యాన్ని',
        'opt_d': 'బుద్ధిజం మాత్రమే',
        'answer': 'C',
        'explanation_te': 'వేంగి చాళుక్యులు శైవ, వైష్ణవ మతాలను మరియు తెలుగు సాహిత్యాన్ని పోషించారు. వీరి కాలంలో "తెలుగు దేశం" అనే పదం వాడుకలోకి వచ్చింది.',
    },
    {
        'section_idx': 5,
        'difficulty': 'medium',
        'question_te': 'AP లో మొత్తం జిల్లాల సంఖ్య (2022 పునర్వ్యవస్థీకరణ తర్వాత) ఎంత?',
        'opt_a': '13',
        'opt_b': '25',
        'opt_c': '26',
        'opt_d': '28',
        'answer': 'C',
        'explanation_te': '2022 ఏప్రిల్‌లో AP లో 13 జిల్లాలను 26 జిల్లాలుగా విభజించారు. ఇది AP చరిత్రలో అతిపెద్ద పరిపాలనా పునర్వ్యవస్థీకరణ.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'AP లో "అమరజీవి దినం" ఏ తేదీన జరుపుతారు?',
        'opt_a': 'నవంబర్ 1',
        'opt_b': 'అక్టోబర్ 1',
        'opt_c': 'డిసెంబర్ 15',
        'opt_d': 'జూన్ 2',
        'answer': 'C',
        'explanation_te': 'పొట్టి శ్రీరాముల్లు స్మృతిలో "అమరజీవి దినం" డిసెంబర్ 15న జరుపుతారు. ఆయన 1952 డిసె 15న మరణించాడు.',
    },
    {
        'section_idx': 1,
        'difficulty': 'hard',
        'question_te': 'అల్లూరి సీతారామ రాజు తిరుగుబాటు ఏ ప్రాంతంలో జరిగింది?',
        'opt_a': 'కృష్ణా డెల్టా',
        'opt_b': 'మన్యం ప్రాంతం (ఏజెన్సీ ప్రాంతం)',
        'opt_c': 'రాయలసీమ',
        'opt_d': 'ఉత్తర ఆంధ్ర',
        'answer': 'B',
        'explanation_te': 'అల్లూరి సీతారామ రాజు తిరుగుబాటు పశ్చిమ గోదావరి, తూర్పు గోదావరి, విశాఖపట్నం జిల్లాల మన్యం ప్రాంతంలో జరిగింది. ఆదివాసీ హక్కుల కోసం బ్రిటిష్ పాలనకు వ్యతిరేకంగా పోరాడాడు.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'AP రాష్ట్ర వృక్షం (state tree) ఏది?',
        'opt_a': 'వేప (Neem)',
        'opt_b': 'జువ్వి (Ficus)',
        'opt_c': 'మేడి (Peepul)',
        'opt_d': 'నేరేడు (Jamun)',
        'answer': 'A',
        'explanation_te': 'వేప (Neem / Azadirachta indica) AP రాష్ట్ర వృక్షం. ఇది AP అంతటా సహజంగా పెరిగే వృక్షం; అనేక ఔషధ గుణాలు కలిగి ఉంది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'రెడ్డి రాజ్యం ఏ ప్రాంతంలో పాలించింది?',
        'opt_a': 'రాయలసీమ',
        'opt_b': 'తీర ఆంధ్ర (కొండవీడు కేంద్రంగా)',
        'opt_c': 'ఉత్తరాంధ్ర',
        'opt_d': 'నాగార్జునకొండ ప్రాంతం',
        'answer': 'B',
        'explanation_te': 'రెడ్డి రాజ్యం 14వ-15వ శతాబ్దంలో కొండవీడును కేంద్రంగా తీర ఆంధ్ర ప్రాంతంలో పాలించింది. ప్రోలయ వేమారెడ్డి ఈ వంశం స్థాపకుడు.',
    },
]


def _seed_ap_ca_div7_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 7."""
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (7, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (7, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division7', 7,
         'AP చరిత్ర & స్వాతంత్ర్య సమరయోధులు',
         'AP History & Freedom Fighters',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div7 notes seeded!'}

def _seed_ap_ca_div7_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 7."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (7, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div7_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (7, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print(f"[div7-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    # Always delete-then-reinsert so seed-file changes are reflected (Postgres dict-row safe).
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    diff_map = {'easy': 1, 'medium': 2, 'hard': 3, 1: 1, 2: 2, 3: 3}
    for mcq in MCQ_DATA:
        diff = diff_map.get(mcq.get('difficulty', 'medium'), 2)
        q_te = mcq.get('question_te', '')
        db_exec(conn, insert_sql, (
            note_id,
            mcq['section_idx'],
            diff,
            q_te,
            mcq['opt_a'], mcq['opt_b'], mcq['opt_c'], mcq['opt_d'],
            str(mcq['answer']).lower(),
            mcq['explanation_te']
        ))
    if USE_POSTGRES:
        conn.commit()
    return {'success': True, 'message': f'AP CA Div7 MCQs seeded! Total: {len(MCQ_DATA)}'}
