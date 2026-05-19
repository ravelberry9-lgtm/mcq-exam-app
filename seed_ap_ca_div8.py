"""
seed_ap_ca_div8.py
AP Current Affairs — Chapter 8: AP పర్యావరణం, ISRO & క్రీడలు

FRESHNESS AUDIT (2026-05-19):
- STALE-FIX: SECTIONS_JSON s1 — "State Animal / Bird: Blackbuck / Indian Roller" was wrong.
  AP's state bird since June 2018 is the Rose-ringed Parakeet (Rama Chiluka).
  Indian Roller / Pala Pitta is Telangana's state bird. Updated.
- STALE-FIX: MCQ at section_idx 7 ("AP రాష్ట్ర జంతువు ఏది?") — explanation said
  "రాష్ట్ర పక్షి: Indian Rose-ringed Parakeet" which is correct but contradicted the
  s1 table. Both now aligned to Rose-ringed Parakeet.
- STALE-FIX: National Parks count MCQ at section_idx 0 — said "2 NPs" which contradicts
  every HTML section that lists 3 (Papikonda, Rajiv Gandhi/Lankamala, Sri Venkateswara).
  Corrected to 3.
- STALE-FIX: BlueBird Block-2 rocket was listed as "LVM3-M5" — official ISRO designation
  is LVM3-M6 (6th operational flight of LVM3, the heaviest commercial cargo ever from
  Indian soil, ~6,100 kg payload, surpassing OneWeb's 5,700 kg record).
- STALE-FIX: SHAR section had "AP solar 6 GW" — confirmed via MNRE 2024 data;
  utility-scale ~5.5 GW + rooftop pushes ~6 GW combined; kept.
- ADDED Paris 2024 medal context (Manu Bhaker 2 bronzes — first post-Independence Indian
  with 2 medals same Games; Aman Sehrawat youngest Indian Olympic medallist; Hockey
  team beat Spain for back-to-back bronze; Neeraj Chopra silver).
- ADDED gap-fill MCQs: BlueBird Block-2 details, Asian Games 2026 Nagoya, Coringa
  Ramsar 2024, Papikonda district Eluru/Alluri, Vande Bharat from Tirupati, LVM3-M6,
  Pulicat AP-TN border, Aditya-L1 L1 point.

AUDIT LOG (2026-05-18):
- FIXED: రోళ్లపాడు జిల్లా — "పల్నాడు జిల్లా" was wrong. Corrected to "నందయాల జిల్లా"
  per HTML source: "రోళ్లపాడు వన్యప్రాణి అభయారణ్యం — నందయాల జిల్లా (పూర్వం కర్నూలు)"
- FIXED: SDSC SHAR location — "నెల్లూరు జిల్లా" was wrong. Corrected to "తిరుపతి జిల్లా"
  per HTML source: "శ్రీహరికోట — తిరుపతి జిల్లా, AP (పులికాట్ సరస్సు పక్కన)"
- FIXED: Satwik Rankireddy question/explanation — no gold medal claim; correct as AP
  badminton player at 2024 Paris Olympics (men's doubles with Chirag Shetty)
- No Telangana-specific questions found/included.
- seed_ap_ca_div8_mcqs.py is a standalone tuple export; this file is canonical.

BATCH D2 AUDIT (2026-05-18):
- FIXED fabricated "సెలూరు అభయారణ్యం" → replaced with the real "రోళ్లపాడు
  వన్యప్రాణి అభయారణ్యం" (Rollapadu WLS, నందయాల జిల్లా) — the actual AP sanctuary
  famous for Blackbucks & Great Indian Bustard. Seluru sanctuary does not exist.
- FIXED AP forest area: was "~23,000 sq km / 17%" — corrected to "~29,800 sq km
  / 18.27%" per ISFR 2023 (India State of Forest Report).
- FIXED AP solar capacity: was "9 GW కంటే ఎక్కువ" — corrected to "~6 GW" per
  MNRE 2024 official installed capacity data (utility + rooftop combined).
- SOFTENED SHAR launch breakdown: was "88 success, 5 partial, 11 failure" — the
  failure count was inflated. Replaced with "90%+ success rate; consult ISRO
  official stats" to avoid claims that aren't ISRO-verified.
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div8_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "sub": "Environment, ISRO & Sports — Exam Hotspots",
        "summary": "జాతీయ ఉద్యానవనాలు, పులుల అభయారణ్యాలు, ISRO SDSC SHAR, AP క్రీడావీరులు — పరీక్ష హాట్‌స్పాట్‌లు",
        "html": """<div class="concept-cover">
  <h1>Environment, ISRO &amp; Sports &nbsp;<span class="bi-te">/ పర్యావరణం, ISRO &amp; క్రీడలు</span></h1>
  <div class="sub">National parks • Wildlife sanctuaries • SDSC SHAR • Star athletes</div>
</div>

<div class="section-hdr">Exam Hotspots / పరీక్ష ముఖ్యాంశాలు</div>
<table class="key-table">
<tr><th>Theme</th><th>Why it matters</th><th class="bi-te">వివరణ</th></tr>
<tr><td>National Parks (3)</td><td>Papikonda, Rajiv Gandhi (Lankamala), Sri Venkateswara</td><td class="bi-te">3 జాతీయ ఉద్యానవనాలు</td></tr>
<tr><td>Tiger Reserve</td><td>NSTR — India's largest at ~3,728 sq km</td><td class="bi-te">నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం</td></tr>
<tr><td>Wildlife Sanctuaries</td><td>Coringa (mangroves), Koundinya (elephants), Rollapadu (GIB/Blackbuck)</td><td class="bi-te">కొరింగ, కౌండిణ్య, రోళ్లపాడు</td></tr>
<tr><td>SDSC SHAR</td><td>India's only orbital launchport; 100th launch was NVS-02 (Jan 29, 2025)</td><td class="bi-te">100వ ప్రయోగం NVS-02</td></tr>
<tr><td>AP athletes</td><td>PV Sindhu, Kidambi Srikanth, P. Gopichand, Satwiksairaj Rankireddy</td><td class="bi-te">PV సింధు, శ్రీకాంత్, గోపీచంద్</td></tr>
</table>

<div class="section-hdr">AP at a Glance — Environment / AP పర్యావరణ సారాంశం</div>
<table class="key-table">
<tr><th>Metric</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Forest area (ISFR 2023)</td><td><b>~29,784 sq km</b> ≈ <b>18.27%</b> of state</td><td class="bi-te">~29,784 చ.కి.మీ / 18.27%</td></tr>
<tr><td>National parks</td><td>3</td><td class="bi-te">3 జాతీయ ఉద్యానవనాలు</td></tr>
<tr><td>Wildlife sanctuaries</td><td>13</td><td class="bi-te">13 వన్యప్రాణి అభయారణ్యాలు</td></tr>
<tr><td>Ramsar sites</td><td>Kolleru, Pulicat (shared with TN)</td><td class="bi-te">కొల్లేరు, పులికాట్ — రామ్‌సర్</td></tr>
<tr><td>Solar capacity (2024)</td><td>~6 GW (MNRE — utility + rooftop)</td><td class="bi-te">~6 GW సోలార్ సామర్థ్యం</td></tr>
<tr><td>State Animal / Bird</td><td>Blackbuck / <b>Rose-ringed Parakeet</b> (Rama Chiluka — 2018 change)</td><td class="bi-te">కృష్ణ జింక / రామ చిలుక (పాల పిట్ట కాదు)</td></tr>
</table>

<p><b>How to revise this division:</b> Memorise the 3 national parks with their districts, then the 13 sanctuary-headliner pairings (Coringa→mangroves, Koundinya→elephants, Rollapadu→GIB+Blackbuck). For ISRO, anchor on the SDSC SHAR location (Tirupati district), the 100th launch (NVS-02, Jan 29 2025), and SpaDeX docking (Jan 16, 2025). Sports: medals, dates, and titles.</p>
<p class="bi-te">3 జాతీయ ఉద్యానవనాలు + 13 అభయారణ్యాల హెడ్‌లైనర్‌లు, SDSC SHAR (తిరుపతి జిల్లా), NVS-02 (జన 29, 2025), SpaDeX (జన 16, 2025) — ఈ నాలుగు యాంకర్ ఫాక్ట్‌లతో విభాగం పూర్తిగా క్లియర్.</p>"""
    },
    {
        "id": "div8_s2",
        "title": "జాతీయ ఉద్యానవనాలు",
        "sub": "National Parks of Andhra Pradesh",
        "summary": "పాపికొండలు, రాజీవ్ గాంధీ జాతీయ ఉద్యానవనం (నాగార్జునసాగర్-శ్రీశైలం), శ్రీ వేంకటేశ్వర జాతీయ ఉద్యానవనం",
        "html": """<div class="concept-cover">
  <h1>National Parks of AP &nbsp;<span class="bi-te">/ AP జాతీయ ఉద్యానవనాలు</span></h1>
  <div class="sub">3 National Parks — Papikonda • Rajiv Gandhi (Lankamala) • Sri Venkateswara</div>
</div>

<div class="section-hdr">The Three AP National Parks / మూడు జాతీయ ఉద్యానవనాలు</div>
<table class="key-table">
<tr><th>Park</th><th>District(s)</th><th>Area</th><th>Famous for</th></tr>
<tr><td><b>Papikonda NP</b></td><td>West Godavari, Eluru, Alluri Sitarama Raju</td><td>~1,012 sq km</td><td>Godavari river boat safari; tigers, leopards</td></tr>
<tr><td><b>Rajiv Gandhi NP</b> (Lankamala)</td><td>Kadapa (YSR)</td><td>~2.4 sq km (very small; largely WLS)</td><td>Slender Loris; dry deciduous</td></tr>
<tr><td><b>Sri Venkateswara NP</b></td><td>Tirupati, Chittoor</td><td>~353 sq km</td><td>Red Sanders, Talakona waterfall, slender loris</td></tr>
</table>

<div class="section-hdr">Key Distinctions / గుర్తుంచుకోవలసిన విషయాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Largest NP in AP</td><td>Papikonda (~1,012 sq km)</td><td class="bi-te">పాపికొండలు అతిపెద్దది</td></tr>
<tr><td>NP on Godavari river</td><td>Papikonda (boat safari)</td><td class="bi-te">పాపికొండలు — గోదావరి బోట్ సఫారీ</td></tr>
<tr><td>NP with Red Sanders</td><td>Sri Venkateswara NP (Seshachalam hills)</td><td class="bi-te">శ్రీ వేంకటేశ్వర NP — Red Sanders</td></tr>
<tr><td>NSTR status</td><td>Tiger Reserve / WLS — NOT a National Park</td><td class="bi-te">NSTR పులుల అభయారణ్యం (NP కాదు)</td></tr>
<tr><td>NSTR total area</td><td>~3,728 sq km (AP share ~3,568 sq km)</td><td class="bi-te">మొత్తం ~3,728 చ.కి.మీ</td></tr>
</table>

<p><b>NSTR — special note:</b> Nagarjunasagar-Srisailam Tiger Reserve is India's <b>largest tiger reserve</b> by area, but it is a <i>Wildlife Sanctuary + Tiger Reserve</i>, not a National Park. It spans AP (Nandyal, Prakasam, Palnadu) and Telangana. Often confused with Rajiv Gandhi NP — they are different.</p>
<p class="bi-te">NSTR భారతదేశ అతిపెద్ద పులుల అభయారణ్యం (~3,728 చ.కి.మీ) — ఇది అభయారణ్యం + Tiger Reserve, జాతీయ ఉద్యానవనం కాదు. AP (నంద్యాల, ప్రకాశం, పల్నాడు) మరియు తెలంగాణలో విస్తరించి ఉంది.</p>

<p><b>2026 update:</b> Papikonda eco-tourism circuit expanded under AP Tourism's River Cruise initiative; new boat permits issued for tribal-owned operators. Sri Venkateswara NP saw enhanced Red Sanders Anti-Smuggling Task Force deployment after the 2024 Supreme Court orders.</p>
<p class="bi-te">పాపికొండలు ఎకో టూరిజమ్ సర్క్యూట్ విస్తరణ; Red Sanders Anti-Smuggling Task Force బలోపేతం.</p>"""
    },
    {
        "id": "div8_s3",
        "title": "వన్యప్రాణి అభయారణ్యాలు",
        "sub": "Wildlife Sanctuaries & Wetlands",
        "summary": "కొరింగ మడ అడవులు, కౌండిణ్య ఏనుగుల అభయారణ్యం, రోళ్లపాడు GIB అభయారణ్యం (నందయాల జిల్లా), పులికాట్ సరస్సు",
        "html": """<div class="concept-cover">
  <h1>Wildlife Sanctuaries &amp; Wetlands &nbsp;<span class="bi-te">/ వన్యప్రాణి అభయారణ్యాలు</span></h1>
  <div class="sub">13 WLS in AP • 2 Ramsar wetlands • Headliner-by-headliner</div>
</div>

<div class="section-hdr">Marquee Sanctuaries / ప్రధాన అభయారణ్యాలు</div>
<table class="key-table">
<tr><th>Sanctuary</th><th>District</th><th>Famous for</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Coringa WLS</b></td><td>Kakinada</td><td>AP's largest mangrove; Irrawaddy dolphins; Olive Ridley nesting</td><td class="bi-te">కొరింగ — మడ అడవులు, కాకినాడ</td></tr>
<tr><td><b>Koundinya WLS</b></td><td>Chittoor</td><td>AP's only elephant sanctuary; near Karnataka border</td><td class="bi-te">కౌండిణ్య — ఏకైక ఏనుగుల అభయారణ్యం</td></tr>
<tr><td><b>Rollapadu WLS</b></td><td><b>Nandyal</b> (formerly Kurnool)</td><td>Great Indian Bustard (GIB) + Blackbuck (state animal)</td><td class="bi-te">రోళ్లపాడు — GIB &amp; కృష్ణ జింక, నంద్యాల జిల్లా</td></tr>
<tr><td>Nelapattu WLS</td><td>Tirupati (formerly Nellore)</td><td>Spot-billed Pelicans, Painted Storks — bird haven</td><td class="bi-te">నేలపట్టు — పక్షుల అభయారణ్యం</td></tr>
<tr><td>Pulicat Lake WLS</td><td>Tirupati (AP) + Tamil Nadu</td><td>India's 2nd largest brackish lagoon; flamingoes</td><td class="bi-te">పులికాట్ — 2వ అతిపెద్ద ఉప్పు సరస్సు</td></tr>
<tr><td>Sri Lankamalleswara WLS</td><td>Kadapa</td><td>Slender Loris (Jerdon's Courser nearby)</td><td class="bi-te">శ్రీ లంకమలెశ్వర</td></tr>
<tr><td>Sri Penusila Narasimha WLS</td><td>Nellore</td><td>Velikonda hills; dry deciduous forest</td><td class="bi-te">శ్రీ పేనుశిల నరసింహ</td></tr>
</table>

<div class="section-hdr">Ramsar Wetland Sites / రామ్‌సర్ సైట్లు</div>
<table class="key-table">
<tr><th>Site</th><th>District</th><th>Year listed</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Kolleru Lake</b></td><td>Eluru, West Godavari</td><td>2002</td><td class="bi-te">కొల్లేరు — తాజా నీటి సరస్సు</td></tr>
<tr><td><b>Pulicat Lake</b></td><td>Tirupati (AP share) + TN</td><td>2002</td><td class="bi-te">పులికాట్ — ఉప్పు సరస్సు</td></tr>
<tr><td><b>Coringa</b> mangroves</td><td>Kakinada</td><td>Added in 2024 — AP's 3rd Ramsar site</td><td class="bi-te">కొరింగ — 2024లో జతచేయబడింది</td></tr>
</table>

<p><b>Rollapadu — critical fix:</b> Located in <b>Nandyal district</b> (carved out of Kurnool in the 2022 reorganisation). It is famous for the critically endangered <b>Great Indian Bustard</b> (Jatayuvu) and large herds of <b>Blackbuck</b> — AP's state animal. The earlier-mentioned "Seluru sanctuary" was a fabricated name and does not exist; Rollapadu is the authentic AP GIB sanctuary.</p>
<p class="bi-te">రోళ్లపాడు అభయారణ్యం నంద్యాల జిల్లాలో (2022 పునర్‌వ్యవస్థీకరణలో కర్నూలు నుండి విడిపోయింది). Great Indian Bustard (జటాయువు) మరియు కృష్ణ జింకలకు (AP రాష్ట్ర జంతువు) ప్రసిద్ధి. "సెలూరు అభయారణ్యం" అనేది తప్పు — రోళ్లపాడు మాత్రమే నిజమైన GIB అభయారణ్యం.</p>"""
    },
    {
        "id": "div8_s4",
        "title": "ISRO — SDSC SHAR",
        "sub": "Satish Dhawan Space Centre — Sriharikota",
        "summary": "శ్రీహరికోట స్పేస్ సెంటర్ (తిరుపతి జిల్లా); 100వ ప్రయోగం NVS-02 (జన. 29, 2025); SpaDeX స్పేస్ డాకింగ్ (డిసె. 2024)",
        "html": """<div class="concept-cover">
  <h1>ISRO — SDSC SHAR &nbsp;<span class="bi-te">/ సతీష్ ధవన్ స్పేస్ సెంటర్</span></h1>
  <div class="sub">India's only orbital launchport • Tirupati district • 100+ launches</div>
</div>

<div class="section-hdr">SDSC SHAR Basics / SDSC SHAR ప్రాథమికాంశాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full name</td><td>Satish Dhawan Space Centre — Sriharikota High Altitude Range</td><td class="bi-te">సతీష్ ధవన్ స్పేస్ సెంటర్</td></tr>
<tr><td>Named after</td><td>Satish Dhawan (former ISRO Chairman 1972-84; renamed 2002)</td><td class="bi-te">2002లో పునర్నామకరణం</td></tr>
<tr><td>Location</td><td><b>Sriharikota island, Tirupati district</b>, AP — near Pulicat lake</td><td class="bi-te">శ్రీహరికోట — తిరుపతి జిల్లా (పులికాట్ సరస్సు పక్కన)</td></tr>
<tr><td>Established</td><td>October 1, 1971</td><td class="bi-te">అక్టోబర్ 1, 1971</td></tr>
<tr><td>Launch pads</td><td>FLP (First) + SLP (Second); 3rd SLV pad under construction</td><td class="bi-te">FLP + SLP (3వది నిర్మాణంలో)</td></tr>
</table>

<div class="section-hdr">Landmark 2024-25 Launches / 2024-25 కీలక ప్రయోగాలు</div>
<table class="key-table">
<tr><th>Mission</th><th>Date</th><th>Rocket</th><th>Significance</th></tr>
<tr><td><b>SpaDeX</b></td><td>Dec 30, 2024</td><td>PSLV-C60</td><td>SDX01 + SDX02 — Space Docking Experiment</td></tr>
<tr><td>SpaDeX Docking</td><td><b>Jan 16, 2025</b></td><td>—</td><td>India 4th country to dock in space (after US, Russia, China)</td></tr>
<tr><td><b>NVS-02 (100th launch)</b></td><td>Jan 29, 2025</td><td>GSLV-F15</td><td>NavIC navigation satellite; SDSC SHAR's <b>100th orbital launch</b></td></tr>
<tr><td>EOS-08</td><td>Aug 16, 2024</td><td>SSLV-D3</td><td>Earth observation; SSLV's 3rd flight (operational)</td></tr>
<tr><td><b>BlueBird Block-2 (BlueBird-6)</b></td><td>Dec 24, 2025</td><td><b>LVM3-M6</b> (6th LVM3 op flight)</td><td>AST SpaceMobile direct-to-mobile satellite; <b>heaviest payload ever from Indian soil</b> ~6,100 kg (beat OneWeb 5,700 kg); 223 sq m phased array — largest commercial comsat in LEO</td></tr>
</table>

<div class="section-hdr">Earlier Marquee Missions / గత ముఖ్య మిషన్లు</div>
<table class="key-table">
<tr><th>Mission</th><th>Date</th><th>Highlights</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Chandrayaan-3</td><td>Jul 14, 2023 (launch); Aug 23, 2023 (landing)</td><td>4th country to soft-land Moon; 1st on south pole</td><td class="bi-te">చంద్రయాన్-3 — చంద్ర దక్షిణ ధ్రువం</td></tr>
<tr><td>Aditya-L1</td><td>Sep 2, 2023</td><td>India's 1st solar observatory</td><td class="bi-te">ఆదిత్య-L1 — సూర్య అధ్యయనం</td></tr>
<tr><td>Mangalyaan (MOM)</td><td>Nov 5, 2013</td><td>India's 1st interplanetary mission</td><td class="bi-te">మంగళయాన్</td></tr>
</table>

<p><b>By December 2025</b>, SDSC SHAR had conducted 104+ orbital launch missions with an overall success rate above 90%. The <b>LVM3-M6 / BlueBird Block-2 launch on Dec 24, 2025</b> set the record for the <b>heaviest payload ever from Indian soil</b> — a single 6,100 kg satellite (surpassing OneWeb's previous 5,700 kg record). The satellite is the largest commercial communications satellite ever placed in LEO, with a 223 sq m phased array, and provides direct-to-mobile cellular broadband for AST SpaceMobile (USA). For exact success/failure splits, consult ISRO's official statistics.</p>
<p class="bi-te">డిసెంబర్ 2025 నాటికి SDSC SHAR నుండి 104+ ఆర్బిటల్ మిషన్లు; విజయవంతమైన శాతం 90%+. LVM3-M6 / BlueBird Block-2 (డిసె 24, 2025) — భారత గడ్డ నుండి అతి భారీ పేలోడ్ ~6,100 కిలోలు (గతంలో OneWeb 5,700 కిలోలు రికార్డ్ బద్దలు). LEO లో అతి పెద్ద వాణిజ్య కమ్యూనికేషన్ ఉపగ్రహం — 223 చ.మీ phased array.</p>"""
    },
    {
        "id": "div8_s5",
        "title": "AP క్రీడావీరులు",
        "sub": "AP's Sporting Legends",
        "summary": "PV సింధు — రియో రజతం, టోక్యో కాంస్యం; కిడంబి శ్రీకాంత్ — BWF 2021 రజతం; గోపీచంద్ — గురువు; నితేష్ కుమార్ — Para Olympics స్వర్ణం",
        "html": """<div class="concept-cover">
  <h1>AP's Sporting Legends &nbsp;<span class="bi-te">/ AP క్రీడావీరులు</span></h1>
  <div class="sub">Sindhu • Srikanth • Gopichand • Satwik • Nitesh — badminton heartland</div>
</div>

<div class="section-hdr">Badminton Stars / బ్యాడ్మింటన్ తారలు</div>
<table class="key-table">
<tr><th>Player</th><th>Origin</th><th>Major achievements</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>PV Sindhu</b></td><td>Hyderabad / AP roots</td><td>Rio 2016 Silver, Tokyo 2020 Bronze; BWF World Champion 2019; Paris 2024 flag-bearer; BWF Athletes Commission 2025</td><td class="bi-te">PV సింధు — 2 ఒలింపిక్ పతకాలు</td></tr>
<tr><td><b>Kidambi Srikanth</b></td><td>Born Feb 7, 1993, Guntur</td><td>BWF World Ch'ship 2021 Silver (1st Indian man); 4 Superseries titles 2017; Thomas Cup 2022 champion</td><td class="bi-te">కిడంబి శ్రీకాంత్</td></tr>
<tr><td><b>Pullela Gopichand</b></td><td>Nagandla, Prakasam</td><td>All England Champion 2001; coach of Sindhu &amp; Srikanth; Padma Bhushan 2014; Dronacharya 2009</td><td class="bi-te">పుల్లేల గోపీచంద్</td></tr>
<tr><td><b>Satwiksairaj Rankireddy</b></td><td>Amalapuram, Konaseema (E. Godavari)</td><td>Men's doubles (with Chirag Shetty); BWF World No. 1 2023; Paris 2024 Olympian</td><td class="bi-te">సాత్విక్ సాయిరాజ్ రాంకిరెడ్డి</td></tr>
</table>

<div class="section-hdr">Other Olympians &amp; Paralympians / ఇతర ఒలింపియన్లు</div>
<table class="key-table">
<tr><th>Player</th><th>Sport</th><th>Achievement</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Nitesh Kumar</b></td><td>Para-Badminton</td><td>Paris 2024 Paralympics <b>Gold</b> (SL3 singles)</td><td class="bi-te">నితేష్ కుమార్ — పారిస్ స్వర్ణం</td></tr>
<tr><td>Karnam Malleswari</td><td>Weightlifting</td><td>1st Indian woman Olympic medallist (Sydney 2000 Bronze)</td><td class="bi-te">కర్ణం మల్లేశ్వరి</td></tr>
<tr><td>Pusarla Venkata Sindhu</td><td>(see above)</td><td>Khel Ratna 2016, Padma Bhushan 2020</td><td class="bi-te">PV సింధు పురస్కారాలు</td></tr>
<tr><td>Krishnam Raju Gadiraju</td><td>Shooting</td><td>AP shooting star; multiple national champion</td><td class="bi-te">కృష్ణం రాజు</td></tr>
</table>

<p><b>2024-25 milestones:</b> Sindhu was flag-bearer at the Paris 2024 Olympics Opening Ceremony (with Sharath Kamal). In 2025 she was elected to the BWF Athletes Commission. Satwik &amp; Chirag reclaimed BWF top-3 doubles ranking. Nitesh Kumar's Paralympic gold (Sep 2024) made him the first Indian male para-badminton Paralympic champion.</p>

<div class="section-hdr">India @ Paris 2024 — Wider Context / పారిస్ 2024 సందర్భం</div>
<table class="key-table">
<tr><th>Athlete / team</th><th>Medal</th><th>Why it matters</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Manu Bhaker</b></td><td>2 Bronze (10m air pistol + mixed team w/ Sarabjot Singh)</td><td><b>First Indian post-Independence with 2 medals in a single Olympics</b></td><td class="bi-te">మను భాకర్ — ఒకే ఒలింపిక్‌లో 2 పతకాలు సాధించిన మొదటి స్వాతంత్ర్యానంతర భారతీయురాలు</td></tr>
<tr><td>Neeraj Chopra</td><td>Silver (Javelin)</td><td>India's only silver at Paris 2024</td><td class="bi-te">నీరజ్ చోప్రా — ఏకైక రజతం</td></tr>
<tr><td>Swapnil Kusale</td><td>Bronze (50m rifle 3-positions)</td><td>India's 3rd shooting bronze at Paris</td><td class="bi-te">స్వప్నిల్ కుసాలే</td></tr>
<tr><td><b>Aman Sehrawat</b></td><td>Bronze (men's 57 kg freestyle wrestling)</td><td><b>Youngest Indian Olympic medallist ever</b> (~21)</td><td class="bi-te">అమన్ సెహ్రావత్ — అతి చిన్న భారత ఒలింపిక్ పతక విజేత</td></tr>
<tr><td><b>Indian Hockey Team</b></td><td>Bronze (beat Spain 2-1)</td><td>Back-to-back Olympic bronze (Tokyo 2020 + Paris 2024)</td><td class="bi-te">హాకీ — వరుసగా 2 ఒలింపిక్ కాంస్యాలు</td></tr>
<tr><td>Total India tally</td><td>6 medals (1 silver + 5 bronze)</td><td>Paris 2024 final count</td><td class="bi-te">భారత్ — 6 పతకాలు</td></tr>
</table>
<p><b>Looking ahead — Asian Games 2026:</b> The 20th Asian Games are scheduled for September 19 – October 4, 2026 in Aichi-Nagoya, Japan. Several AP athletes (Satwik, Sindhu, Nitesh) are in contention. The 2030 Asian Games will be hosted in Doha (announced 2024).</p>
<p class="bi-te">2026 ఆసియా క్రీడలు (20వవి) జపాన్‌లోని ఐచి-నాగోయాలో సెప్టెంబర్ 19 – అక్టోబర్ 4, 2026లో జరగనున్నాయి. సాత్విక్, సింధు, నితేష్ వంటి AP క్రీడాకారులు ప్రాతినిధ్యం వహించనున్నారు.</p>"""
    },
    {
        "id": "div8_s6",
        "title": "పర్యావరణ కరెంట్ అఫైర్స్",
        "sub": "Environment Current Affairs & Policy",
        "summary": "Red Sanders రక్షణ, ఆలివ్ రిడ్లీ తాబేళ్ళు, పాపికొండలు ఎకో టూరిజమ్, AP Green Hydrogen Policy",
        "html": """<div class="concept-cover">
  <h1>Environment Current Affairs &nbsp;<span class="bi-te">/ పర్యావరణ కరెంట్ అఫైర్స్</span></h1>
  <div class="sub">Red Sanders • Olive Ridleys • Green Hydrogen • Coringa Ramsar</div>
</div>

<div class="section-hdr">Conservation Headlines / పర్యావరణ ప్రధాన వార్తలు</div>
<table class="key-table">
<tr><th>Topic</th><th>2024-2026 update</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Red Sanders</b> (Pterocarpus santalinus)</td><td>CITES Appendix II protected; endemic to Seshachalam, Veligonda hills (Kadapa, Tirupati, Chittoor, Nandyal); Anti-Smuggling Task Force strengthened 2024</td><td class="bi-te">ఎర్ర చందనం — శేషాచలం, వేలికొండ; రాయలసీమ</td></tr>
<tr><td><b>Olive Ridley turtles</b></td><td>Mass nesting at Coringa &amp; Srikurmam every Nov-Feb; AP Forest Dept hatchery 2025-26</td><td class="bi-te">ఆలివ్ రిడ్లీ తాబేళ్ళు — కొరింగ, శ్రీకూర్మం</td></tr>
<tr><td><b>Coringa Ramsar</b></td><td>Designated as India's 80th Ramsar site in 2024 — AP's 3rd</td><td class="bi-te">కొరింగ — 80వ రామ్‌సర్ సైట్ (2024)</td></tr>
<tr><td><b>Green Hydrogen Hub</b></td><td>AP Green Hydrogen Policy 2023 → Pudimadaka (Anakapalli) selected as National Green Hydrogen Mission Hub in 2024; NTPC + Reliance investment</td><td class="bi-te">పుడిమడక — గ్రీన్ హైడ్రోజన్ హబ్</td></tr>
<tr><td><b>Solar capacity</b></td><td>~6 GW installed (MNRE 2024 — utility + rooftop); target 10 GW by 2030</td><td class="bi-te">~6 GW సోలార్ సామర్థ్యం</td></tr>
</table>

<div class="section-hdr">Policy &amp; Bodies / విధానాలు మరియు సంస్థలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>AP State Biodiversity Board</td><td>Established 2006 under Biological Diversity Act 2002</td><td class="bi-te">AP State Biodiversity Board</td></tr>
<tr><td>AP Pollution Control Board (APPCB)</td><td>HQ Vijayawada; air quality monitoring across 16 cities</td><td class="bi-te">APPCB — విజయవాడ</td></tr>
<tr><td>Mission LiFE in AP</td><td>State action plan launched 2023; eco-clubs in 10,000+ schools</td><td class="bi-te">Mission LiFE</td></tr>
<tr><td>AP Climate Action Plan</td><td>Released Dec 2024; targets net-zero 2070 aligning with India's NDC</td><td class="bi-te">AP వాతావరణ కార్యాచరణ ప్రణాళిక</td></tr>
</table>

<p><b>Red Sanders globally:</b> Pterocarpus santalinus grows ONLY in a small belt of Andhra Pradesh — Seshachalam, Lankamala, Veligonda and Palakonda hills (i.e., Kadapa, Tirupati, Chittoor, Annamayya, Nandyal districts). Its red heartwood is internationally prized for Japanese musical instruments (shamisen) and Chinese furniture — driving heavy smuggling. CITES Appendix II since 1995.</p>
<p class="bi-te">Red Sanders ప్రపంచంలో AP లోనే ఒక చిన్న ప్రాంతంలో పెరుగుతుంది — శేషాచలం, లంకమల, వేలికొండ, పాలకొండ (కడప, తిరుపతి, చిత్తూరు, అన్నమయ్య, నంద్యాల). అంతర్జాతీయంగా అత్యంత విలువైనది (జపాన్ షామిసెన్, చైనా ఫర్నిచర్) — అందుకే అక్రమ రవాణా తీవ్రంగా జరుగుతుంది.</p>"""
    },
    {
        "id": "div8_s7",
        "title": "పర్యావరణ సంఖ్యలు",
        "sub": "Numbers, Areas & Statistics",
        "summary": "ముఖ్య సంఖ్యలు: నాగార్జునసాగర్ వైశాల్యం, కొరింగ మడ జాతులు, SDSC SHAR మొత్తం ప్రయోగాలు",
        "html": """<div class="concept-cover">
  <h1>Key Numbers &amp; Statistics &nbsp;<span class="bi-te">/ ముఖ్య సంఖ్యలు</span></h1>
  <div class="sub">Area • Species count • Launch tally • Capacity</div>
</div>

<div class="section-hdr">Areas &amp; Extents / వైశాల్యాలు</div>
<table class="key-table">
<tr><th>Metric</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>AP forest cover (ISFR 2023)</td><td><b>~29,784 sq km</b> ≈ <b>18.27%</b> of state</td><td class="bi-te">~29,784 చ.కి.మీ / 18.27%</td></tr>
<tr><td>NSTR Tiger Reserve</td><td>~3,728 sq km (total); AP share ~3,568</td><td class="bi-te">NSTR ~3,728 చ.కి.మీ</td></tr>
<tr><td>Papikonda NP</td><td>~1,012 sq km</td><td class="bi-te">పాపికొండలు ~1,012</td></tr>
<tr><td>Sri Venkateswara NP</td><td>~353 sq km</td><td class="bi-te">శ్రీ వేంకటేశ్వర ~353</td></tr>
<tr><td>Coringa mangroves</td><td>~235 sq km (AP's largest)</td><td class="bi-te">కొరింగ ~235 చ.కి.మీ</td></tr>
<tr><td>Pulicat Lake (total)</td><td>~759 sq km (AP share ~84%)</td><td class="bi-te">పులికాట్ ~759 చ.కి.మీ</td></tr>
<tr><td>Kolleru Lake</td><td>~308 sq km (Asia's largest freshwater)</td><td class="bi-te">కొల్లేరు ~308 చ.కి.మీ</td></tr>
</table>

<div class="section-hdr">Biodiversity &amp; Species / జీవవైవిధ్యం</div>
<table class="key-table">
<tr><th>Item</th><th>Count</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Coringa mangrove species</td><td>35+</td><td class="bi-te">కొరింగ — 35+ మడ జాతులు</td></tr>
<tr><td>AP wildlife sanctuaries</td><td>13</td><td class="bi-te">13 అభయారణ్యాలు</td></tr>
<tr><td>AP national parks</td><td>3</td><td class="bi-te">3 జాతీయ ఉద్యానవనాలు</td></tr>
<tr><td>AP tiger reserves</td><td>1 (NSTR; Nallamala)</td><td class="bi-te">1 పులుల అభయారణ్యం</td></tr>
<tr><td>AP elephant reserve</td><td>1 (Rayala — Koundinya)</td><td class="bi-te">1 ఏనుగుల అభయారణ్యం</td></tr>
<tr><td>AP Ramsar sites</td><td>3 (Kolleru, Pulicat, Coringa)</td><td class="bi-te">3 రామ్‌సర్ సైట్లు</td></tr>
</table>

<div class="section-hdr">ISRO &amp; Energy / ISRO &amp; విద్యుత్</div>
<table class="key-table">
<tr><th>Metric</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>SDSC SHAR launches (by Dec 2025)</td><td>104+ (success rate &gt; 90%)</td><td class="bi-te">104+ ప్రయోగాలు</td></tr>
<tr><td>SDSC SHAR 100th launch</td><td>NVS-02 / GSLV-F15 — Jan 29, 2025</td><td class="bi-te">100వ ప్రయోగం — NVS-02</td></tr>
<tr><td>SDSC SHAR established</td><td>Oct 1, 1971</td><td class="bi-te">అక్టోబర్ 1, 1971</td></tr>
<tr><td>AP solar installed (2024)</td><td>~6 GW</td><td class="bi-te">~6 GW</td></tr>
<tr><td>AP wind installed</td><td>~4.1 GW</td><td class="bi-te">~4.1 GW గాలిమర</td></tr>
<tr><td>AP total power capacity</td><td>~26 GW (all sources)</td><td class="bi-te">~26 GW మొత్తం</td></tr>
</table>

<p class="bi-te">అన్ని సంఖ్యలు ISFR 2023, MNRE 2024, ISRO అధికారిక గణాంకాల ఆధారంగా. పరీక్షల కోసం ఈ క్లుప్త పట్టిక ఒక్కసారి చదివితే చాలు.</p>"""
    },
    {
        "id": "div8_s8",
        "title": "పరీక్ష రేపిడ్ రివిజన్",
        "sub": "Rapid Revision — Environment, ISRO, Sports",
        "summary": "పర్యావరణం, ISRO, క్రీడలు — సంక్షిప్త పట్టిక",
        "html": """<div class="concept-cover">
  <h1>Rapid Revision Sheet &nbsp;<span class="bi-te">/ పరీక్ష రేపిడ్ రివిజన్</span></h1>
  <div class="sub">Div8 must-know facts in one screen</div>
</div>

<div class="section-hdr">Environment One-Liners / పర్యావరణ ఏక-పంక్తి</div>
<table class="key-table">
<tr><th>Question</th><th>Answer</th><th class="bi-te">వివరణ</th></tr>
<tr><td>National parks in AP</td><td>3 — Papikonda, Rajiv Gandhi (Lankamala), Sri Venkateswara</td><td class="bi-te">3 NPs</td></tr>
<tr><td>Largest tiger reserve in India</td><td>NSTR (~3,728 sq km)</td><td class="bi-te">NSTR అతిపెద్దది</td></tr>
<tr><td>AP forest cover (ISFR 2023)</td><td>~29,784 sq km / 18.27%</td><td class="bi-te">~29,784 చ.కి.మీ</td></tr>
<tr><td>AP's only elephant sanctuary</td><td>Koundinya WLS (Chittoor)</td><td class="bi-te">కౌండిణ్య</td></tr>
<tr><td>GIB &amp; Blackbuck sanctuary</td><td>Rollapadu (Nandyal district)</td><td class="bi-te">రోళ్లపాడు — నంద్యాల</td></tr>
<tr><td>India's 2nd largest brackish lagoon</td><td>Pulicat Lake</td><td class="bi-te">పులికాట్</td></tr>
<tr><td>AP Ramsar sites</td><td>3 (Kolleru 2002, Pulicat 2002, Coringa 2024)</td><td class="bi-te">3 రామ్‌సర్ సైట్లు</td></tr>
<tr><td>Red Sanders region</td><td>Seshachalam, Veligonda hills — Rayalaseema</td><td class="bi-te">శేషాచలం / రాయలసీమ</td></tr>
<tr><td>AP solar installed</td><td>~6 GW (MNRE 2024)</td><td class="bi-te">~6 GW</td></tr>
<tr><td>Green Hydrogen Hub</td><td>Pudimadaka (Anakapalli)</td><td class="bi-te">పుడిమడక</td></tr>
</table>

<div class="section-hdr">ISRO One-Liners / ISRO ఏక-పంక్తి</div>
<table class="key-table">
<tr><th>Question</th><th>Answer</th></tr>
<tr><td>SDSC SHAR location</td><td>Sriharikota island, <b>Tirupati district</b></td></tr>
<tr><td>SDSC SHAR named after</td><td>Satish Dhawan (former ISRO Chairman)</td></tr>
<tr><td>SDSC SHAR established</td><td>October 1, 1971</td></tr>
<tr><td>SDSC SHAR 100th launch</td><td>NVS-02 on GSLV-F15, <b>Jan 29, 2025</b></td></tr>
<tr><td>India's first space docking</td><td>SpaDeX — Jan 16, 2025 (4th country)</td></tr>
<tr><td>Chandrayaan-3 landing</td><td>Aug 23, 2023 (Moon south pole)</td></tr>
<tr><td>Aditya-L1 launch</td><td>Sep 2, 2023</td></tr>
<tr><td>Heaviest cargo from SHAR</td><td>BlueBird Block-2 — Dec 24, 2025 via LVM3-M6 (~6,100 kg; beat OneWeb's 5,700 kg)</td></tr>
</table>

<div class="section-hdr">Sports One-Liners / క్రీడలు ఏక-పంక్తి</div>
<table class="key-table">
<tr><th>Question</th><th>Answer</th></tr>
<tr><td>PV Sindhu Olympic medals</td><td>Rio 2016 Silver + Tokyo 2020 Bronze</td></tr>
<tr><td>Paris 2024 flag-bearer (India)</td><td>PV Sindhu (with Sharath Kamal)</td></tr>
<tr><td>BWF Athletes Commission 2025</td><td>PV Sindhu elected</td></tr>
<tr><td>Kidambi Srikanth — major medal</td><td>BWF Worlds 2021 Silver (1st Indian man)</td></tr>
<tr><td>Satwik Rankireddy partner</td><td>Chirag Shetty (men's doubles)</td></tr>
<tr><td>Gopichand — All England year</td><td>2001</td></tr>
<tr><td>Nitesh Kumar — Paris 2024</td><td>Paralympic Gold (SL3)</td></tr>
<tr><td>Karnam Malleswari</td><td>Sydney 2000 Bronze — 1st Indian woman Olympic medal</td></tr>
</table>

<p class="bi-te">ఈ మూడు పట్టికలు — పర్యావరణం, ISRO, క్రీడలు — విభాగం 8 ఆఖరి నిమిషం రివిజన్‌కు చాలు. ముఖ్యంగా 2024-25 ISRO మైలురాళ్ళు, రోళ్లపాడు జిల్లా (నంద్యాల) తప్పనిసరిగా గుర్తుంచుకోండి.</p>"""
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Key concepts
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "SDSC SHAR ఏ జిల్లాలో ఉంది?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "తిరుపతి",
        "opt_c": "గుంటూరు",
        "opt_d": "కాకినాడ",
        "answer": "B",
        "explanation_te": "SDSC SHAR (Satish Dhawan Space Centre) శ్రీహరికోట ద్వీపంలో ఉంది — ఇది తిరుపతి జిల్లాలో పులికాట్ సరస్సు పక్కన ఉంది."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "SDSC SHAR పూర్తి అర్థం ఏమిటి?",
        "opt_a": "Satish Dhawan Space Centre — Sriharikota High Altitude Range",
        "opt_b": "Space Development & Science Centre — Sriharikota",
        "opt_c": "Satellite Design & Signal Centre — Sriharikota",
        "opt_d": "South Division Space Coordination — Sriharikota Hangar",
        "answer": "A",
        "explanation_te": "SDSC = Satish Dhawan Space Centre (మాజీ ISRO చైర్మన్ పేరు); SHAR = Sriharikota High Altitude Range."
    },
    # Section 1 — National Parks
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "పాపికొండలు జాతీయ ఉద్యానవనం ఏ నదిపై ఉంది?",
        "opt_a": "కృష్ణా నది",
        "opt_b": "గోదావరి నది",
        "opt_c": "పెన్నా నది",
        "opt_d": "తుంగభద్ర నది",
        "answer": "B",
        "explanation_te": "పాపికొండలు జాతీయ ఉద్యానవనం గోదావరి నది ఒడ్డున పశ్చిమ గోదావరి, ఏలూరు జిల్లాల్లో ఉంది. Boat Safari ఇక్కడ ప్రసిద్ధి."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "శ్రీ వేంకటేశ్వర జాతీయ ఉద్యానవనం ఏ ముఖ్య వృక్ష జాతికి ప్రసిద్ధి?",
        "opt_a": "మడ చెట్లు",
        "opt_b": "Red Sanders (ఎర్ర చందనం)",
        "opt_c": "Sal చెట్లు",
        "opt_d": "Teak చెట్లు",
        "answer": "B",
        "explanation_te": "శ్రీ వేంకటేశ్వర జాతీయ ఉద్యానవనం (తిరుపతి జిల్లా) Red Sanders (Pterocarpus santalinus) కోసం ప్రసిద్ధి — CITES రక్షిత జాతి."
    },
    # Section 2 — Wildlife Sanctuaries
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "భారతదేశంలో అత్యధిక వైశాల్యం గల పులుల అభయారణ్యం ఏది?",
        "opt_a": "కార్బెట్ జాతీయ ఉద్యానవనం",
        "opt_b": "నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం",
        "opt_c": "సుందర్‌బన్స్",
        "opt_d": "బందీపూర్",
        "answer": "B",
        "explanation_te": "నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం (~3,728 చ.కి.మీ) భారతదేశంలో అతి పెద్ద పులుల అభయారణ్యం. ఇది AP మరియు తెలంగాణ రెండు రాష్ట్రాలలో విస్తరించింది."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "AP లో ఏకైక ఏనుగుల అభయారణ్యం ఏది?",
        "opt_a": "కొరింగ",
        "opt_b": "రోళ్లపాడు",
        "opt_c": "కౌండిణ్య",
        "opt_d": "నేలపట్టు",
        "answer": "C",
        "explanation_te": "కౌండిణ్య వన్యప్రాణి అభయారణ్యం (చిత్తూరు జిల్లా) AP లో ఏకైక ఏనుగుల అభయారణ్యం. కర్నాటక సరిహద్దు దగ్గర ఉంది."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "కొరింగ వన్యప్రాణి అభయారణ్యం ఎందుకు ప్రసిద్ధి?",
        "opt_a": "పులుల కోసం",
        "opt_b": "మడ అడవులు — AP అతి పెద్ద Mangrove",
        "opt_c": "ఏనుగుల కోసం",
        "opt_d": "గ్రేట్ ఇండియన్ బస్టర్డ్ కోసం",
        "answer": "B",
        "explanation_te": "కొరింగ (కాకినాడ జిల్లా) AP అతి పెద్ద మడ అడవి. గోదావరి నది ముఖద్వారం వద్ద ఉంది. 35+ మడ చెట్ల జాతులు, Irrawaddy dolphins ఉన్నాయి. Ramsar Wetland Site."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "రోళ్లపాడు వన్యప్రాణి అభయారణ్యం ఏ పక్షికి పేరు పొందింది?",
        "opt_a": "ఫ్లమింగో",
        "opt_b": "Peacock (నెమలి)",
        "opt_c": "Great Indian Bustard (జటాయువు)",
        "opt_d": "పెలికాన్",
        "answer": "C",
        "explanation_te": "రోళ్లపాడు (నందయాల జిల్లా — పూర్వం కర్నూలు జిల్లా) Great Indian Bustard (GIB) కోసం ప్రసిద్ధి. GIB అత్యంత అంతరించిపోయే పక్షి; AP రాష్ట్ర జంతువు Blackbuck కూడా ఇక్కడ ఉంటుంది."
    },
    {
        "section_idx": 2,
        "difficulty": "hard",
        "question_te": "పులికాట్ సరస్సు గురించి సరైన వాక్యం ఏది?",
        "opt_a": "భారత్ అతి పెద్ద ఉప్పు సరస్సు",
        "opt_b": "భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు — ఫ్లమింగో వలస",
        "opt_c": "AP లో ఏకైక Ramsar Site",
        "opt_d": "కొరింగ మడ అడవుల కంటే పెద్దది",
        "answer": "B",
        "explanation_te": "పులికాట్ సరస్సు భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు (చిల్కా (ఒడిశా) అతి పెద్దది). ఫ్లమింగో వలస పక్షులకు ముఖ్య నిలయం. SDSC SHAR శ్రీహరికోట పులికాట్ పక్కన ఉంది."
    },
    # Section 3 — ISRO
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "SDSC SHAR నుండి 100వ ప్రయోగం ఏది?",
        "opt_a": "Chandrayaan-3",
        "opt_b": "SpaDeX",
        "opt_c": "NVS-02 / GSLV-F15",
        "opt_d": "Aditya-L1",
        "answer": "C",
        "explanation_te": "జనవరి 29, 2025న GSLV-F15 రాకెట్ ద్వారా NVS-02 ఉపగ్రహం ప్రయోగం SDSC SHAR నుండి 100వ ప్రయోగం. ఇది NavIC నావిగేషన్ కోసం."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "SpaDeX మిషన్ లో ఏమి జరిగింది?",
        "opt_a": "చంద్రుడిపై ల్యాండింగ్",
        "opt_b": "భారత తొలి స్పేస్ డాకింగ్ — SDX01+SDX02",
        "opt_c": "సూర్యుడి అధ్యయనం",
        "opt_d": "మార్స్ ఆర్బిటర్",
        "answer": "B",
        "explanation_te": "SpaDeX (Space Docking Experiment) — డిసెంబర్ 30, 2024న PSLV-C60 ద్వారా ప్రయోగం; జనవరి 16, 2025న SDX01 (Chaser) + SDX02 (Target) స్పేస్ డాకింగ్ సఫలం."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "స్పేస్ డాకింగ్ సాంకేతికత నేర్పడంలో భారత్ ఏ స్థానంలో ఉంది?",
        "opt_a": "మొదటి",
        "opt_b": "రెండవ",
        "opt_c": "మూడవ",
        "opt_d": "నాల్గవ",
        "answer": "D",
        "explanation_te": "USA, Russia, China తర్వాత భారత్ 4వ దేశంగా స్పేస్ డాకింగ్ సాంకేతికత సాధించింది (SpaDeX — జనవరి 2025)."
    },
    {
        "section_idx": 3,
        "difficulty": "hard",
        "question_te": "NVS-02 ఉపగ్రహం ఏ ప్రయోజనం కోసం?",
        "opt_a": "వాతావరణ పరిశీలన",
        "opt_b": "NavIC నావిగేషన్ వ్యవస్థ",
        "opt_c": "రిమోట్ సెన్సింగ్",
        "opt_d": "సైనిక నిఘా",
        "answer": "B",
        "explanation_te": "NVS-02 NavIC (Navigation with Indian Constellation) వ్యవస్థ కోసం. NavIC భారత స్వదేశీ GPS ప్రత్యామ్నాయం."
    },
    # Section 4 — Sports
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "PV సింధు రియో 2016 ఒలింపిక్స్‌లో ఏ పతకం సాధించింది?",
        "opt_a": "స్వర్ణ పతకం",
        "opt_b": "రజత పతకం",
        "opt_c": "కాంస్య పతకం",
        "opt_d": "పతకం రాలేదు",
        "answer": "B",
        "explanation_te": "PV సింధు రియో 2016లో రజత పతకం మరియు టోక్యో 2020లో కాంస్య పతకం సాధించింది. ఆమె రెండు ఒలింపిక్ పతకాలు సాధించిన అరుదైన భారత క్రీడాకారిణి."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "కిడంబి శ్రీకాంత్ ఏ జిల్లాకు చెందినవాడు?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "గుంటూరు",
        "opt_c": "కర్నూలు",
        "opt_d": "నెల్లూరు",
        "answer": "B",
        "explanation_te": "కిడంబి శ్రీకాంత్ ఫిబ్రవరి 7, 1993న గుంటూరు, AP లో జన్మించాడు. BWF World Championship 2021లో రజత పతకం సాధించాడు."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "2022 Thomas Cup లో భారత్ జట్టులో AP కి చెందిన ముఖ్య సభ్యుడు ఎవరు?",
        "opt_a": "PV సింధు",
        "opt_b": "కిడంబి శ్రీకాంత్",
        "opt_c": "గోపీచంద్",
        "opt_d": "సైనా నెహ్వాల్",
        "answer": "B",
        "explanation_te": "2022 Thomas Cup (పురుషుల టీమ్ బ్యాడ్మింటన్) లో భారత్ తొలిసారి విజయం సాధించింది. శ్రీకాంత్ కీలక సభ్యుడు. ఇది AP గర్వించే విజయం."
    },
    {
        "section_idx": 4,
        "difficulty": "hard",
        "question_te": "PV సింధు 2025లో ఏ పాత్రలో ఎన్నికైంది?",
        "opt_a": "IOC Athletes Commission",
        "opt_b": "BCCI Board Member",
        "opt_c": "BWF Athletes Commission",
        "opt_d": "Olympic Council of Asia",
        "answer": "C",
        "explanation_te": "PV సింధు 2025లో BWF (Badminton World Federation) Athletes Commission సభ్యురాలిగా ఎన్నికైంది — క్రీడా నిర్వహణలో చురుకైన పాత్ర."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "పారిస్ 2024 Olympics Opening Ceremony లో భారత్ జెండా ఆజమాయిషీదారు ఎవరు?",
        "opt_a": "నీరజ్ చోప్రా",
        "opt_b": "PV సింధు",
        "opt_c": "మనుభాకర్",
        "opt_d": "వినేశ్ ఫోగాట్",
        "answer": "B",
        "explanation_te": "పారిస్ 2024 ఒలింపిక్స్ Opening Ceremony లో PV సింధు భారత్ జెండా ఆజమాయిషీదారు. ఆమె AP / తెలుగు పౌరురాలికి ఇది మరింత గర్వప్రదం."
    },
    # Section 5 — Environment Current Affairs
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "Red Sanders (ఎర్ర చందనం) AP లో ఏ ప్రాంతంలో పెరుగుతుంది?",
        "opt_a": "తీర ఆంధ్ర",
        "opt_b": "ఉత్తరాంధ్ర",
        "opt_c": "రాయలసీమ అడవులు",
        "opt_d": "పాపికొండ",
        "answer": "C",
        "explanation_te": "Red Sanders (Pterocarpus santalinus) ప్రత్యేకంగా రాయలసీమ అడవులలో (నంద్యాల, కర్నూలు జిల్లాలు) పెరుగుతుంది. CITES రక్షిత జాతి."
    },
    # Section 6 — Numbers
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "SDSC SHAR నుండి మొత్తం ప్రయోగాలు డిసెంబర్ 2025 నాటికి ఎన్ని?",
        "opt_a": "75",
        "opt_b": "88",
        "opt_c": "100",
        "opt_d": "104",
        "answer": "D",
        "explanation_te": "డిసెంబర్ 2025 నాటికి SDSC SHAR నుండి మొత్తం 104 ప్రయోగ మిషన్‌లు (orbital launches) చేపట్టారు. విజయవంతమైన మిషన్ల శాతం 90% పైగా ఉంది. (Exact success/failure breakdown ISRO అధికారిక గణాంకాల కోసం చూడండి.)"
    },
    # Section 7 — Rapid revision
    {
        "section_idx": 7,
        "difficulty": "hard",
        "question_te": "పులికాట్ సరస్సు AP లో ఏ ప్రత్యేకత ఉంది?",
        "opt_a": "AP అతి పెద్ద తాజా నీటి సరస్సు",
        "opt_b": "AP లో Ramsar Site; భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు",
        "opt_c": "AP అతి పెద్ద మడ అడవి",
        "opt_d": "AP లో ఏకైక నేషనల్ పార్క్",
        "answer": "B",
        "explanation_te": "పులికాట్ సరస్సు Ramsar Convention Wetland Site; భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు (మొదటిది చిల్కా, ఒడిశా). ఇక్కడ SDSC SHAR శ్రీహరికోట ఉంది."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "AP రాష్ట్ర జంతువు ఏది?",
        "opt_a": "పులి",
        "opt_b": "ఏనుగు",
        "opt_c": "కృష్ణజింక (Blackbuck)",
        "opt_d": "సింహం",
        "answer": "C",
        "explanation_te": "AP రాష్ట్ర జంతువు కృష్ణజింక (Blackbuck / Indian Antelope). రోళ్లపాడు వన్యప్రాణి అభయారణ్యంలో (నంద్యాల జిల్లా) ప్రసిద్ధి. AP రాష్ట్ర పక్షి: రామ చిలుక (Rose-ringed Parakeet) — 2018 జూన్‌లో పాల పిట్ట (Indian Roller) నుండి మార్చారు; పాల పిట్ట ఇప్పుడు తెలంగాణ రాష్ట్ర పక్షి."
    },

    # --- additional MCQs ---
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'AP లో పాపికొండలు జాతీయ ఉద్యానవనం ఏ జిల్లాలో ఉంది?',
        'opt_a': 'కృష్ణా జిల్లా',
        'opt_b': 'పశ్చిమ గోదావరి, ఏలూరు జిల్లాలు',
        'opt_c': 'కర్నూలు',
        'opt_d': 'శ్రీకాకుళం',
        'answer': 'B',
        'explanation_te': 'పాపికొండలు జాతీయ ఉద్యానవనం పశ్చిమ గోదావరి మరియు ఏలూరు జిల్లాలలో ఉంది. గోదావరి నది ఒడ్డున విస్తరించి ఉన్న ఈ పార్క్ 1,012 చ.కి.మీ విస్తీర్ణం కలిగి ఉంది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం AP వాటా ఎంత?',
        'opt_a': '~1,000 చ.కి.మీ',
        'opt_b': '~2,000 చ.కి.మీ',
        'opt_c': '~3,568 చ.కి.మీ',
        'opt_d': '~500 చ.కి.మీ',
        'answer': 'C',
        'explanation_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం (NSTR) లో AP వాటా ~3,568 చ.కి.మీ. ఇది భారతదేశంలో అతిపెద్ద పులుల అభయారణ్యాలలో ఒకటి.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'AP రాష్ట్రంలో పులుల అభయారణ్యం ఏ పర్వతశ్రేణిలో ఉంది?',
        'opt_a': 'ఎర్ర అడవులు',
        'opt_b': 'నల్లమల కొండలు',
        'opt_c': 'ఆనమల కొండలు',
        'opt_d': 'శేషాచలం కొండలు',
        'answer': 'B',
        'explanation_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం నల్లమల కొండల మధ్య ఉంది. ఇది AP మరియు తెలంగాణ రాష్ట్రాల మధ్య విస్తరించి ఉంది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'AP లో రాజీవ్ గాంధీ జాతీయ ఉద్యానవనం ఎక్కడ ఉంది?',
        'opt_a': 'విశాఖ జిల్లా',
        'opt_b': 'కడప జిల్లా',
        'opt_c': 'కర్నూలు జిల్లా',
        'opt_d': 'నెల్లూరు జిల్లా',
        'answer': 'B',
        'explanation_te': 'రాజీవ్ గాంధీ జాతీయ ఉద్యానవనం (లంకమల NP) కడప జిల్లాలో ఉంది. 353 చ.కి.మీ విస్తీర్ణంతో ఇది AP లో తక్కువ విస్తీర్ణం కలిగిన జాతీయ ఉద్యానవనం.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'AP లో ఎర్ర చందనం (Red Sanders) ప్రత్యేకంగా ఏ జిల్లాలో పెరుగుతుంది?',
        'opt_a': 'కృష్ణా',
        'opt_b': 'కడప, తిరుపతి, చిత్తూరు జిల్లాలు',
        'opt_c': 'నెల్లూరు',
        'opt_d': 'కర్నూలు',
        'answer': 'B',
        'explanation_te': 'ఎర్ర చందనం (Red Sanders / రక్తచందనం) రాయలసీమలో ముఖ్యంగా కడప, తిరుపతి, చిత్తూరు జిల్లాలలో పెరుగుతుంది. ఇది CITES రక్షిత జాతి మరియు అంతర్జాతీయంగా చాలా విలువైనది.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'పులికాట్ సరస్సు AP కి ఏమిటి?',
        'opt_a': 'మంచినీటి సరస్సు',
        'opt_b': 'భారతదేశంలో 2వ అతి పెద్ద ఉప్పు సరస్సు, ఫ్లమింగో వలస',
        'opt_c': 'హ్రాదరేసర్వాయర్',
        'opt_d': 'ISRO ప్రయోగ కేంద్రం',
        'answer': 'B',
        'explanation_te': 'పులికాట్ సరస్సు భారతదేశంలో 2వ అతి పెద్ద ఉప్పు సరస్సు. ఇది తిరుపతి జిల్లాలో ఉంది మరియు శీతాకాలంలో ఫ్లమింగో వలసలకు ప్రసిద్ధి.',
    },
    {
        'section_idx': 1,
        'difficulty': 'medium',
        'question_te': 'కొరింగ వన్యప్రాణి అభయారణ్యం ఏ జిల్లాలో ఉంది?',
        'opt_a': 'విశాఖపట్నం',
        'opt_b': 'కాకినాడ (తూర్పు గోదావరి)',
        'opt_c': 'కృష్ణా',
        'opt_d': 'నెల్లూరు',
        'answer': 'B',
        'explanation_te': 'కొరింగ వన్యప్రాణి అభయారణ్యం కాకినాడ జిల్లాలో మడ అడవులకు ప్రసిద్ధి. ఇది ఆలివ్ రిడ్లీ తాబేళ్ళ గూళ్ళకు ముఖ్యమైన స్థలం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'ISRO SDSC SHAR కేంద్రం ఎక్కడ ఉంది?',
        'opt_a': 'బెంగళూరు',
        'opt_b': 'హైదరాబాద్',
        'opt_c': 'శ్రీహరికోట (తిరుపతి జిల్లా)',
        'opt_d': 'నెల్లూరు పట్టణం',
        'answer': 'C',
        'explanation_te': 'ISRO సతీష్ ధవన్ స్పేస్ సెంటర్ (SDSC SHAR) తిరుపతి జిల్లాలోని శ్రీహరికోటలో ఉంది (పులికాట్ సరస్సు పక్కన). ఇది భారతదేశంలో ప్రయోగ వాహనాల ప్రయోగ కేంద్రం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'SDSC SHAR కేంద్రం ఏ వ్యక్తి పేరిట నామకరణం జరిగింది?',
        'opt_a': 'విక్రమ్ సారాభాయ్',
        'opt_b': 'సతీష్ ధవన్',
        'opt_c': 'APJ అబ్దుల్ కలామ్',
        'opt_d': 'ఉడుపి రామచంద్ర రావు',
        'answer': 'B',
        'explanation_te': 'SDSC SHAR కేంద్రం ISRO మాజీ అధ్యక్షుడు సతీష్ ధవన్ పేరిట నామకరణం జరిగింది. 2002లో ఆయన మరణం తర్వాత ఈ కేంద్రానికి ఆయన పేరు పెట్టారు.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'చంద్రయాన్-3 చంద్రుని దక్షిణ ధ్రువం వద్ద ఎప్పుడు దిగింది?',
        'opt_a': 'ఆగస్టు 14, 2023',
        'opt_b': 'ఆగస్టు 23, 2023',
        'opt_c': 'జూలై 14, 2023',
        'opt_d': 'సెప్టెంబర్ 5, 2023',
        'answer': 'B',
        'explanation_te': 'చంద్రయాన్-3 లాండర్ "విక్రమ్" మరియు రోవర్ "ప్రజ్ఞాన్" ఆగస్టు 23, 2023న చంద్రుని దక్షిణ ధ్రువ ప్రాంతంలో సురక్షితంగా దిగాయి. భారతదేశం ఈ ఘనత సాధించిన 4వ దేశం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'ఆదిత్య-L1 మిషన్ ఏ కోసం పంపబడింది?',
        'opt_a': 'చంద్రుని అధ్యయనానికి',
        'opt_b': 'సూర్యుని అధ్యయనానికి',
        'opt_c': 'అంగారకుని మిషన్',
        'opt_d': 'GPS నేవిగేషన్',
        'answer': 'B',
        'explanation_te': 'ఆదిత్య-L1 సెప్టెంబర్ 2, 2023న ప్రయోగించబడింది. ఇది సూర్యుని అధ్యయనానికి భారతదేశం పంపిన తొలి మిషన్. L1 పాయింట్ వద్ద ఉంచబడింది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'NavIC అంటే ఏమిటి?',
        'opt_a': 'ISRO ఉపగ్రహ ఉప్పు కేంద్రం',
        'opt_b': 'భారత నావిగేషన్ ఉపగ్రహ వ్యవస్థ',
        'opt_c': 'AP నావిక దళం',
        'opt_d': 'ISRO రాకెట్ రకం',
        'answer': 'B',
        'explanation_te': 'NavIC (Navigation with Indian Constellation) భారత స్వంత నావిగేషన్ ఉపగ్రహ వ్యవస్థ. జనవరి 29, 2025న GSLV-F15 ద్వారా NavIC ఉపగ్రహం ప్రయోగించబడింది - ఇది SDSC SHAR శతక ప్రయోగం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'hard',
        'question_te': 'SDSC SHAR కేంద్రం ఏ సంవత్సరంలో 100వ ప్రయోగం సాధించింది?',
        'opt_a': '2023',
        'opt_b': '2024',
        'opt_c': '2025',
        'opt_d': '2026',
        'answer': 'C',
        'explanation_te': 'జనవరి 29, 2025న GSLV-F15 ప్రయోగంతో SDSC SHAR 100వ ప్రయోగం (శతక ప్రయోగం) సాధించింది. ఇది ISRO కి చాలా ముఖ్యమైన మైలురాయి.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'PV సింధు ఏ క్రీడలో ప్రపంచ ప్రసిద్ధి?',
        'opt_a': 'టెన్నిస్',
        'opt_b': 'బ్యాడ్మింటన్',
        'opt_c': 'క్రికెట్',
        'opt_d': 'షూటింగ్',
        'answer': 'B',
        'explanation_te': 'PV సింధు (పుసర్ల వెంకట సింధు) బ్యాడ్మింటన్ క్రీడలో ప్రపంచ ప్రసిద్ధి. ఆమె రియో 2016 (రజత), టోక్యో 2020 (కాంస్య) ఒలింపిక్ పతకాలు మరియు 2019 BWF వరల్డ్ చాంపియన్‌షిప్ గెలిచింది.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'PV సింధు కి ఏ ఒలింపిక్ పతకాలు వచ్చాయి?',
        'opt_a': 'బంగారం మరియు రజత',
        'opt_b': '2 బంగారం పతకాలు',
        'opt_c': 'రజత (2016), కాంస్య (2020)',
        'opt_d': 'రజత (2016), బంగారం (2020)',
        'answer': 'C',
        'explanation_te': 'PV సింధు రియో 2016 ఒలింపిక్‌లో రజత పతకం, టోక్యో 2020 ఒలింపిక్‌లో కాంస్య పతకం గెలిచింది. ఆమె హైదరాబాద్ కి చెందిన తెలుగు క్రీడాకారిణి.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'పుల్లేల గోపీచంద్ ఏ ముఖ్య పురస్కారాలు పొందారు?',
        'opt_a': 'Padma Bhushan (2014), Dronacharya Award (2009)',
        'opt_b': 'Padma Vibhushan (2017), Arjuna Award',
        'opt_c': 'Padma Shri (2020), Rajiv Gandhi Khel Ratna',
        'opt_d': 'Padma Bhushan (2020), Dronacharya Award (2014)',
        'answer': 'A',
        'explanation_te': 'పుల్లేల గోపీచంద్ — AP బ్యాడ్మింటన్ కోచ్; నాగందల, ప్రకాశం జిల్లా. Padma Bhushan (2014), Dronacharya Award (2009), 2001 All England Champion.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': '2024 ప్యారిస్ ఒలింపిక్స్‌లో పాల్గొన్న AP కి చెందిన ప్రముఖ బ్యాడ్మింటన్ ఆటగాడు ఎవరు?',
        'opt_a': 'పీఆర్ శ్రీజేష్',
        'opt_b': 'నీరజ్ చోప్రా',
        'opt_c': 'సాత్విక్ సాయిరాజ్ రాంకిరెడ్డి',
        'opt_d': 'లక్ష్య సేన్',
        'answer': 'C',
        'explanation_te': 'సాత్విక్ సాయిరాజ్ రాంకిరెడ్డి AP (అమలాపురం, తూర్పు గోదావరి జిల్లా) కి చెందిన బ్యాడ్మింటన్ ఆటగాడు. 2024 ప్యారిస్ ఒలింపిక్స్‌లో మెన్స్ డబుల్స్‌లో (చిరాగ్ శెట్టితో) పాల్గొన్నాడు. BWF World Ranking లో నంబర్ 1 జంట.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'AP లో హంపి ప్రక్కన ఉన్న UNESCO వారసత్వ స్థానం ఏది?',
        'opt_a': 'అమరావతి',
        'opt_b': 'హంపి (కర్ణాటకలో, AP లో కాదు)',
        'opt_c': 'శ్రీశైలం',
        'opt_d': 'లేపాక్షి (గుంటూరు)',
        'answer': 'B',
        'explanation_te': 'హంపి కర్ణాటక రాష్ట్రంలో ఉంది, AP లో కాదు. AP UNESCO వారసత్వ ప్రతిపాదనలో అమరావతి స్తూపం ఉంది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'AP లో ఏ ప్రాజెక్టు జాతీయ ప్రాజెక్టుగా APRA 2014 Section 94 లో గుర్తించబడింది?',
        'opt_a': 'నాగార్జునసాగర్',
        'opt_b': 'పోలవరం ప్రాజెక్టు',
        'opt_c': 'శ్రీశైలం',
        'opt_d': 'తెలుగుగంగ',
        'answer': 'B',
        'explanation_te': 'పోలవరం ప్రాజెక్టు AP Reorganisation Act 2014 Section 94 ద్వారా జాతీయ ప్రాజెక్టుగా గుర్తించబడింది. ఇది పూర్తిగా కేంద్ర ప్రభుత్వ నిధులతో నిర్మించబడుతుంది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'AP లో మొత్తం అడవుల విస్తీర్ణం (ISFR 2023 ప్రకారం) సుమారు ఎంత?',
        'opt_a': '10,000 చ.కి.మీ',
        'opt_b': '23,000 చ.కి.మీ',
        'opt_c': '29,800 చ.కి.మీ',
        'opt_d': '50,000 చ.కి.మీ',
        'answer': 'C',
        'explanation_te': 'India State of Forest Report (ISFR) 2023 ప్రకారం AP అడవుల విస్తీర్ణం ~29,784 చ.కి.మీ — రాష్ట్ర మొత్తం భౌగోళిక ప్రాంతంలో సుమారు 18.27%.',
    },
    {
        'section_idx': 5,
        'difficulty': 'medium',
        'question_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం (మొత్తం) ఎంత విస్తీర్ణం కలిగి ఉంది?',
        'opt_a': '~3,728 చ.కి.మీ',
        'opt_b': '~2,000 చ.కి.మీ',
        'opt_c': '~5,000 చ.కి.మీ',
        'opt_d': '~8,000 చ.కి.మీ',
        'answer': 'A',
        'explanation_te': 'NSTR మొత్తం ~3,728 చ.కి.మీ విస్తీర్ణం కలిగి AP-తెలంగాణ రాష్ట్రాల మీదుగా విస్తరించి ఉంది. ఇది భారతదేశంలో అతిపెద్ద పులుల అభయారణ్యం.',
    },
    {
        'section_idx': 5,
        'difficulty': 'easy',
        'question_te': 'AP లో ఏ వన్యప్రాణి అభయారణ్యం ఆలివ్ రిడ్లీ తాబేళ్ళకు ప్రసిద్ధి?',
        'opt_a': 'నాగార్జునసాగర్',
        'opt_b': 'పాపికొండలు',
        'opt_c': 'కొరింగ',
        'opt_d': 'నేలపట్టు',
        'answer': 'C',
        'explanation_te': 'కొరింగ వన్యప్రాణి అభయారణ్యం కాకినాడ జిల్లాలో ఆలివ్ రిడ్లీ తాబేళ్ళ గూళ్ళకు ముఖ్యమైన స్థలం. మడ అడవులకు కూడా ప్రసిద్ధి.',
    },
    {
        'section_idx': 6,
        'difficulty': 'medium',
        'question_te': 'AP లో Solar Energy సంస్థాపన సామర్థ్యం (installed capacity) 2024 నాటికి సుమారు ఎంత?',
        'opt_a': '~1 GW',
        'opt_b': '~6 GW',
        'opt_c': '~15 GW',
        'opt_d': '~25 GW',
        'answer': 'B',
        'explanation_te': 'MNRE 2024 డేటా ప్రకారం AP లో installed solar capacity సుమారు 5.5–6 GW (utility + rooftop కలిపి). AP solar PLI పథకాల కింద గ్రీన్ హైడ్రోజన్ హబ్‌గా అభివృద్ధి చెందుతోంది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'hard',
        'question_te': 'శేషాచలం కొండలలో ఏ అరుదైన వృక్ష జాతి ముఖ్యంగా కనిపిస్తుంది?',
        'opt_a': 'బొగ్గు',
        'opt_b': 'ఎర్ర చందనం (Red Sanders)',
        'opt_c': 'ఇనుమురాయి',
        'opt_d': 'అల్యూమినా',
        'answer': 'B',
        'explanation_te': 'శేషాచలం కొండలు (చిత్తూరు, కడప జిల్లాలు) ఎర్ర చందనానికి (Red Sanders) ప్రసిద్ధి. ఇది CITES రక్షిత జాతి మరియు అంతర్జాతీయంగా అత్యంత విలువైన వృక్ష జాతి.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'LVM-3 (GSLV Mk3) రాకెట్ ఉపయోగం ఏమిటి?',
        'opt_a': 'చిన్న ఉపగ్రహాలు',
        'opt_b': 'భారీ ఉపగ్రహాల ప్రయోగం',
        'opt_c': 'మిలిటరీ ఉపగ్రహం',
        'opt_d': 'వాతావరణ పరిశోధన',
        'answer': 'B',
        'explanation_te': 'LVM-3 (Launch Vehicle Mark-3) ISRO యొక్క అత్యంత శక్తివంతమైన రాకెట్. చంద్రయాన్-3 మిషన్ ఈ రాకెట్ ద్వారా ప్రయోగించబడింది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'భారతదేశం ఏ మిషన్ తో చంద్రుని దక్షిణ ధ్రువంలో తొలిగా దిగింది?',
        'opt_a': 'చంద్రయాన్-2',
        'opt_b': 'చంద్రయాన్-3',
        'opt_c': 'మంగళయాన్',
        'opt_d': 'ఆదిత్య-L1',
        'answer': 'B',
        'explanation_te': 'చంద్రయాన్-3 ఆగస్టు 23, 2023న చంద్రుని దక్షిణ ధ్రువ ప్రాంతంలో సురక్షితంగా దిగింది. ఈ ఘనత సాధించిన 4వ దేశంగా భారతదేశం నిలిచింది.',
    },
    {
        'section_idx': 1,
        'difficulty': 'medium',
        'question_te': 'AP లో నేలపట్టు అభయారణ్యం ఎందుకు ప్రసిద్ధి?',
        'opt_a': 'పులులు',
        'opt_b': 'ఫ్లమింగో మరియు తెల్ల పెలికాన్లు',
        'opt_c': 'ఏనుగులు',
        'opt_d': 'ఆదివాసీ జాతులు',
        'answer': 'B',
        'explanation_te': 'నేలపట్టు అభయారణ్యం నెల్లూరు జిల్లాలో ఉంది. శీతాకాలంలో ఫ్లమింగో మరియు తెల్ల పెలికాన్లు వలస వస్తాయి, ఇది పక్షి పరిశీలకులకు ప్రసిద్ధ స్థానం.',
    },
    {
        'section_idx': 0,
        'difficulty': 'hard',
        'question_te': 'AP లో ఎన్ని జాతీయ ఉద్యానవనాలు ఉన్నాయి?',
        'opt_a': '1',
        'opt_b': '2',
        'opt_c': '3',
        'opt_d': '4',
        'answer': 'C',
        'explanation_te': 'AP లో 3 జాతీయ ఉద్యానవనాలు ఉన్నాయి: 1) పాపికొండలు NP (పశ్చిమ గోదావరి/ఏలూరు/అల్లూరి జిల్లాలు) 2) రాజీవ్ గాంధీ NP / లంకమల (కడప) 3) శ్రీ వేంకటేశ్వర NP (తిరుపతి/చిత్తూరు). NSTR జాతీయ ఉద్యానవనం కాదు — అది పులుల అభయారణ్యం + వన్యప్రాణి అభయారణ్యం.',
    },
    {
        'section_idx': 5,
        'difficulty': 'easy',
        'question_te': 'AP లో రోళ్లపాడు వన్యప్రాణి అభయారణ్యం ఎందుకు ప్రసిద్ధి?',
        'opt_a': 'ఎర్ర చందనం',
        'opt_b': 'నల్ల జింక (Blackbuck) & గ్రేట్ ఇండియన్ బస్టర్డ్',
        'opt_c': 'పులులు',
        'opt_d': 'ఏనుగులు',
        'answer': 'B',
        'explanation_te': 'రోళ్లపాడు వన్యప్రాణి అభయారణ్యం (Rollapadu Wildlife Sanctuary) నందయాల జిల్లాలో ఉంది — నల్ల జింకలకు (Blackbuck/కృష్ణ జింక) మరియు గ్రేట్ ఇండియన్ బస్టర్డ్ పక్షికి ప్రసిద్ధి. కృష్ణ జింక AP రాష్ట్ర జంతువు.',
    },

    # === FRESHNESS GAP-FILL MCQs (Audit 2026-05-19) ===
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'డిసెంబర్ 24, 2025న SDSC SHAR నుండి ప్రయోగించిన BlueBird Block-2 ఏ రాకెట్‌తో ప్రయోగించబడింది?',
        'opt_a': 'PSLV-C60',
        'opt_b': 'GSLV-F15',
        'opt_c': 'LVM3-M6',
        'opt_d': 'SSLV-D3',
        'answer': 'C',
        'explanation_te': 'BlueBird Block-2 (BlueBird-6, AST SpaceMobile) — డిసెంబర్ 24, 2025న LVM3-M6 (6వ ఆపరేషనల్ ఫ్లైట్) ద్వారా SHAR నుండి ప్రయోగించారు. ఇది ~6,100 కిలోల పేలోడ్ — భారత గడ్డ నుండి అతి భారీ; గత OneWeb రికార్డ్ 5,700 కిలోలు బద్దలు.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'BlueBird Block-2 ఉపగ్రహం ఏ ప్రత్యేకతకు ప్రసిద్ధి?',
        'opt_a': 'మొదటి భారతీయ చంద్రయాన్',
        'opt_b': 'LEO లో అతి పెద్ద వాణిజ్య కమ్యూనికేషన్ ఉపగ్రహం — 223 చ.మీ ఫేజ్డ్ అరే',
        'opt_c': 'మొదటి GPS ఉపగ్రహం',
        'opt_d': 'మొదటి మిలిటరీ నిఘా ఉపగ్రహం',
        'answer': 'B',
        'explanation_te': 'BlueBird Block-2 LEO లో అతి పెద్ద వాణిజ్య కమ్యూనికేషన్ ఉపగ్రహం — 223 చ.మీ ఫేజ్డ్ అరే; AST SpaceMobile (USA) direct-to-mobile broadband అందిస్తుంది — సాధారణ స్మార్ట్‌ఫోన్‌లు terrestrial టవర్లు లేకుండానే connect అవగలవు.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': '2024 పారిస్ ఒలింపిక్స్‌లో భారత్ తరఫున 2 పతకాలు సాధించిన మొదటి స్వాతంత్ర్యానంతర అథ్లెట్ ఎవరు?',
        'opt_a': 'PV సింధు',
        'opt_b': 'మను భాకర్',
        'opt_c': 'వినేశ్ ఫోగాట్',
        'opt_d': 'మీరాబాయి చాను',
        'answer': 'B',
        'explanation_te': 'మను భాకర్ — పారిస్ 2024 ఒలింపిక్స్‌లో 2 కాంస్యాలు (10మీ ఎయిర్ పిస్టల్ + మిక్స్‌డ్ టీమ్ సర్బ్‌జోత్ సింగ్‌తో). స్వాతంత్ర్యానంతరం ఒకే ఒలింపిక్‌లో 2 పతకాలు సాధించిన మొదటి భారతీయురాలు.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'పారిస్ 2024లో అతి చిన్న వయసులో ఒలింపిక్ పతకం సాధించిన భారతీయుడు ఎవరు?',
        'opt_a': 'నీరజ్ చోప్రా',
        'opt_b': 'మను భాకర్',
        'opt_c': 'అమన్ సెహ్రావత్',
        'opt_d': 'స్వప్నిల్ కుసాలే',
        'answer': 'C',
        'explanation_te': 'అమన్ సెహ్రావత్ (~21 ఏళ్ళు) — మెన్స్ ఫ్రీస్టైల్ 57కిలోల రెజ్లింగ్‌లో కాంస్యం (బ్రాంజ్ మ్యాచ్‌లో డేరియన్ టోయ్ క్రూజ్‌ను 13-5 తో ఓడించాడు). ఇది భారత చరిత్రలో అతి చిన్న వయసు ఒలింపిక్ పతక విజయం.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'పారిస్ 2024 ఒలింపిక్స్‌లో భారత హాకీ జట్టు బ్రాంజ్ మ్యాచ్‌లో ఏ దేశాన్ని ఓడించింది?',
        'opt_a': 'జర్మనీ',
        'opt_b': 'నెదర్లాండ్స్',
        'opt_c': 'స్పెయిన్',
        'opt_d': 'ఆస్ట్రేలియా',
        'answer': 'C',
        'explanation_te': 'భారత హాకీ జట్టు పారిస్ 2024లో స్పెయిన్‌ను 2-1తో ఓడించి కాంస్యం సాధించింది — టోక్యో 2020 తర్వాత వరుసగా 2వ ఒలింపిక్ హాకీ పతకం.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'పారిస్ 2024లో భారత్ మొత్తం ఎన్ని పతకాలు సాధించింది?',
        'opt_a': '4 (0 స్వర్ణం)',
        'opt_b': '6 (1 రజతం + 5 కాంస్యాలు)',
        'opt_c': '7 (1 స్వర్ణం)',
        'opt_d': '10',
        'answer': 'B',
        'explanation_te': 'భారత్ పారిస్ 2024లో 6 పతకాలు సాధించింది: 1 రజతం (నీరజ్ చోప్రా — జావెలిన్) + 5 కాంస్యాలు (మను భాకర్ 2, స్వప్నిల్ కుసాలే, అమన్ సెహ్రావత్, హాకీ జట్టు).',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': '20వ ఆసియా క్రీడలు (2026) ఎక్కడ, ఎప్పుడు జరగనున్నాయి?',
        'opt_a': 'హాంగ్‌ఝౌ, చైనా — 2026 జూన్',
        'opt_b': 'ఐచి-నాగోయా, జపాన్ — సెప్టెంబర్ 19 – అక్టోబర్ 4, 2026',
        'opt_c': 'దోహా, ఖతార్ — 2026 నవంబర్',
        'opt_d': 'రియాద్, సౌదీ అరేబియా — 2026 ఆగస్టు',
        'answer': 'B',
        'explanation_te': '20వ ఆసియా క్రీడలు ఐచి-నాగోయా (జపాన్‌)లో సెప్టెంబర్ 19 – అక్టోబర్ 4, 2026లో జరగనున్నాయి (వాయిదా పడిన తర్వాత). 2030 ఆసియా క్రీడలు దోహాకు కేటాయించబడ్డాయి.',
    },
    {
        'section_idx': 5,
        'difficulty': 'easy',
        'question_te': 'కొరింగ మడ అడవులు ఎప్పుడు రామ్‌సర్ సైట్‌గా ప్రకటించబడ్డాయి? అవి AP లో ఎన్నవ Ramsar సైట్?',
        'opt_a': '2002 — 1వది',
        'opt_b': '2024 — AP లో 3వ Ramsar సైట్ (భారత 80వ)',
        'opt_c': '2014 — 2వది',
        'opt_d': '2026 — 4వది',
        'answer': 'B',
        'explanation_te': 'కొరింగ మడ అడవులు 2024లో భారత్ 80వ Ramsar Wetland Site గా ప్రకటించబడ్డాయి — AP లో 3వ Ramsar సైట్ (కొల్లేరు 2002, పులికాట్ 2002, కొరింగ 2024). కాకినాడ జిల్లాలో ఉంది.',
    },
    {
        'section_idx': 1,
        'difficulty': 'medium',
        'question_te': 'పాపికొండలు జాతీయ ఉద్యానవనం ఏ జిల్లాలో విస్తరించింది (2022 పునర్‌వ్యవస్థీకరణ తర్వాత)?',
        'opt_a': 'తూర్పు గోదావరి ఒక్కటే',
        'opt_b': 'పశ్చిమ గోదావరి, ఏలూరు, అల్లూరి సీతారామరాజు జిల్లాలు',
        'opt_c': 'విశాఖపట్నం, విజయనగరం',
        'opt_d': 'కృష్ణా, గుంటూరు',
        'answer': 'B',
        'explanation_te': '2022 పునర్‌వ్యవస్థీకరణ తర్వాత పాపికొండలు NP (~1,012 చ.కి.మీ) పశ్చిమ గోదావరి, ఏలూరు, మరియు అల్లూరి సీతారామరాజు జిల్లాలలో విస్తరించి ఉంది. గోదావరి నది బోట్ సఫారీ ప్రసిద్ధి.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'ఆదిత్య-L1 ఉపగ్రహం ఎక్కడ ఉంచబడింది?',
        'opt_a': 'భూ స్థిర కక్ష్యలో',
        'opt_b': 'భూమి-సూర్యుడి మధ్య L1 Lagrange పాయింట్ వద్ద (~15 లక్షల కి.మీ)',
        'opt_c': 'చంద్రుని కక్ష్యలో',
        'opt_d': 'అంగారక కక్ష్యలో',
        'answer': 'B',
        'explanation_te': 'ఆదిత్య-L1 (సెప్టెంబర్ 2, 2023న ప్రయోగం) భూమి నుండి ~15 లక్షల కిలోమీటర్ల దూరంలో సూర్యుడి దిశగా ఉన్న L1 (Lagrange Point 1) వద్ద జనవరి 6, 2024న ప్రవేశించింది — ఇక్కడ నుండి సూర్యుడిని నిరంతరం పరిశీలించవచ్చు.',
    },
    {
        'section_idx': 7,
        'difficulty': 'easy',
        'question_te': 'AP రాష్ట్ర పక్షి ఏది (2018 మార్పు తర్వాత)?',
        'opt_a': 'పాల పిట్ట (Indian Roller)',
        'opt_b': 'రామ చిలుక (Rose-ringed Parakeet)',
        'opt_c': 'నెమలి',
        'opt_d': 'తెల్ల పెలికాన్',
        'answer': 'B',
        'explanation_te': 'AP రాష్ట్ర పక్షి — రామ చిలుక (Rose-ringed Parakeet, Psittacula krameri). 2018 జూన్‌లో పాల పిట్ట (Indian Roller) నుండి రామ చిలుకగా అధికారికంగా మార్చారు. పాల పిట్ట ఇప్పుడు తెలంగాణ, ఒడిశా, కర్ణాటకలకు రాష్ట్ర పక్షి.',
    },
    {
        'section_idx': 5,
        'difficulty': 'medium',
        'question_te': 'AP లో గ్రీన్ హైడ్రోజన్ హబ్‌గా ఎంపికైన ప్రదేశం ఏది?',
        'opt_a': 'శ్రీహరికోట',
        'opt_b': 'పుడిమడక (అనకాపల్లి జిల్లా)',
        'opt_c': 'తుని',
        'opt_d': 'విశాఖపట్నం పోర్ట్',
        'answer': 'B',
        'explanation_te': 'పుడిమడక (అనకాపల్లి జిల్లా) — National Green Hydrogen Mission Hub గా 2024లో ఎంపిక. AP Green Hydrogen Policy 2023 ఆధారంగా NTPC + Reliance పెట్టుబడులు ప్రకటించారు.',
    },
    {
        'section_idx': 6,
        'difficulty': 'easy',
        'question_te': 'AP లో ఎన్ని Ramsar Wetland సైట్లు ఉన్నాయి (2026 నాటికి)?',
        'opt_a': '1',
        'opt_b': '2',
        'opt_c': '3',
        'opt_d': '4',
        'answer': 'C',
        'explanation_te': '2026 నాటికి AP లో 3 Ramsar సైట్లు: కొల్లేరు (2002), పులికాట్ (2002 — తమిళనాడుతో పంచుకొనేది), కొరింగ మడ అడవులు (2024లో జతచేయబడ్డాయి — భారత 80వ Ramsar సైట్).',
    },
]


def _seed_ap_ca_div8_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 8."""
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (8, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (8, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division8', 8,
         'AP పర్యావరణం, ISRO & క్రీడలు',
         'AP Environment, ISRO & Sports',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div8 notes seeded!'}
def _seed_ap_ca_div8_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 8."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (8, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div8_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (8, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print(f"[div8-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    cur2 = db_exec(conn, f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    count = list(row_to_dict(cur2.fetchone()).values())[0]
    if count > 0 and not force:
        return
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    diff_map = {'easy': 1, 'medium': 2, 'hard': 3, 1: 1, 2: 2, 3: 3}
    for mcq in MCQ_DATA:
        diff = diff_map.get(mcq.get('difficulty', 'medium'), 2)
        q_te = mcq.get('question_te', mcq.get('question_te', ''))
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
    return {'success': True, 'message': f'AP CA Div8 MCQs seeded! Total: {len(MCQ_DATA)}'}
