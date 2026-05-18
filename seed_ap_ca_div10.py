"""
seed_ap_ca_div10.py
AP Current Affairs — Chapter 10: AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026

AUDIT LOG (2026-05-18):
- No junk MCQs found (no empty options, single-letter options, or nonsense options).
- No Telangana-specific scheme questions found.
  (TS context in Amendment Act 2026 questions is legitimate AP reorganisation content.)
- FIXED: Conflicting Polavaram section numbers.
  Original MCQ_DATA Section 2 MCQ said "APRA 2014 Section 90" for Polavaram national project.
  _EXTRA_MCQ_DATA_10 correctly uses Section 94 (answer D). APRA 2014 Section 94 is the correct
  section for Polavaram national project declaration.
  Changes: SECTIONS_JSON summary "Section 90" → "Section 94"; MCQ question and explanation
  at section_idx=2 changed from "Section 90" to "Section 94".
- No abrupt or meaningless question text found.
- Key facts verified: APRA Act No. 6/2014; effective June 2, 2014; Lok Sabha Feb 18, Rajya Sabha
  Feb 20; Amendment 2026 Act No. 7/2026; Lok Sabha Apr 1, Rajya Sabha Apr 2, President Apr 6;
  Amaravati retrospective from June 2, 2024; Article 371-D (32nd Amendment 1973);
  7 mandals transfer Act No. 19/2014.
- ENRICHED 2026-05-18: All 8 SECTIONS_JSON entries now carry `sub` + bilingual rich-HTML
  `html` (concept-cover, section-hdr, key-table, bi-te), matching the seed_ap_ca_div1 pattern.
  HTML covers APRA 2014 dates/Acts, Sections 5/24/30/94, SCS+14th FC, 2026 Amendment timeline,
  Article 371-D + G.O. 610, 7-mandals list, and a rapid-revision sheet.
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div10_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "sub": "Exam Hotspots — APRA 2014 & 2026 Amendment",
        "summary": "APRA 2014 అమలు: జూన్ 2, 2014; హైదరాబాద్ 10 సం. ఉమ్మడి; Act No. 6/2014; Amendment 2026: Act No. 7/2026",
        "html": """<div class="concept-cover">
  <h1>APRA 2014 &amp; 2026 Amendment &nbsp;<span class="bi-te">/ APRA 2014 &amp; 2026 సవరణ</span></h1>
  <div class="sub">Act 6/2014 • Effective Jun 2, 2014 • Amendment Act 7/2026 names Amaravati</div>
</div>

<div class="section-hdr">Two Landmark Statutes / రెండు మైలురాయి చట్టాలు</div>
<table class="key-table">
<tr><th>Statute</th><th>Act No.</th><th>Effective</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>AP Reorganisation Act, 2014</b></td><td>Act No. 6 of 2014</td><td><b>Jun 2, 2014</b></td><td class="bi-te">జూన్ 2, 2014 — విభజన</td></tr>
<tr><td>APRA (Amendment) Act, 2014 — 7 mandals</td><td>Act No. 19 of 2014</td><td>Jul 11, 2014</td><td class="bi-te">7 మండలాల బదిలీ</td></tr>
<tr><td><b>APRA (Amendment) Act, 2026</b></td><td><b>Act No. 7 of 2026</b></td><td>Apr 6, 2026 (retro Jun 2, 2024)</td><td class="bi-te">అమరావతి — 3వ సవరణ</td></tr>
</table>

<div class="section-hdr">Exam Hotspots / పరీక్ష హాట్‌స్పాట్‌లు</div>
<table class="key-table">
<tr><th>Topic</th><th>Key fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>APRA 2014 — Lok Sabha</td><td>Feb 18, 2014</td><td class="bi-te">LS — ఫిబ్రవరి 18, 2014</td></tr>
<tr><td>APRA 2014 — Rajya Sabha</td><td>Feb 20, 2014 (voice vote)</td><td class="bi-te">RS — ఫిబ్రవరి 20, 2014</td></tr>
<tr><td>Telangana formation</td><td>29th state of India — Jun 2, 2014</td><td class="bi-te">29వ రాష్ట్రం</td></tr>
<tr><td>Section 5(2)</td><td>Capital — amended in 2026 to name Amaravati</td><td class="bi-te">రాజధాని — అమరావతి</td></tr>
<tr><td>Section 30</td><td>AP High Court — set up Jan 1, 2019 at Amaravati</td><td class="bi-te">AP HC — జన. 1, 2019</td></tr>
<tr><td>Section 94</td><td>Polavaram declared National Project</td><td class="bi-te">పోలవరం జాతీయ ప్రాజెక్టు</td></tr>
<tr><td>Joint capital period</td><td>Hyderabad for 10 years (2014-2024)</td><td class="bi-te">10 సం. ఉమ్మడి</td></tr>
<tr><td>Asset-debt share</td><td>58.32% AP : 41.68% Telangana (population basis)</td><td class="bi-te">జనాభా ప్రకారం</td></tr>
<tr><td>Article 371-D</td><td>32nd Constitutional Amendment, 1973</td><td class="bi-te">32వ సవరణ, 1973</td></tr>
</table>
<p class="bi-te">APRA 2014 (Act 6/2014) జూన్ 2, 2014న అమల్లోకి వచ్చి, ఆంధ్రప్రదేశ్‌ను విభజించి తెలంగాణను 29వ రాష్ట్రంగా ఏర్పాటు చేసింది. 2026 సవరణ (Act 7/2026) Section 5(2)ని సవరించి అమరావతిని AP రాజధానిగా చట్టబద్ధంగా పేర్కొంది (జూన్ 2, 2024 నుండి Retrospective).</p>"""
    },
    {
        "id": "div10_s2",
        "title": "APRA 2014 — మూల చట్టం వివరాలు",
        "sub": "APRA 2014 — Original Act Full Details",
        "summary": "Lok Sabha: ఫిబ్రవరి 18, 2014; Rajya Sabha: ఫిబ్రవరి 20, 2014; అమలు: జూన్ 2, 2014; తెలంగాణ 29వ రాష్ట్రం",
        "html": """<div class="concept-cover">
  <h1>APRA 2014 — Original Act &nbsp;<span class="bi-te">/ APRA 2014 — మూల చట్టం</span></h1>
  <div class="sub">LS Feb 18 • RS Feb 20 (voice vote) • President Mar 1 • Effective Jun 2, 2014</div>
</div>

<div class="section-hdr">Legislative Passage / చట్టసభల ఆమోదం</div>
<table class="key-table">
<tr><th>Stage</th><th>Date</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Lok Sabha passage</td><td><b>February 18, 2014</b></td><td class="bi-te">LS — ఫిబ్రవరి 18, 2014</td></tr>
<tr><td>Rajya Sabha passage</td><td><b>February 20, 2014</b> (voice vote, opposition walkout)</td><td class="bi-te">RS — ఫిబ్రవరి 20, 2014</td></tr>
<tr><td>President's assent</td><td>March 1, 2014 (Pranab Mukherjee)</td><td class="bi-te">రాష్ట్రపతి — మార్చి 1, 2014</td></tr>
<tr><td><b>Appointed day (effective)</b></td><td><b>June 2, 2014</b></td><td class="bi-te">అమలు — జూన్ 2, 2014</td></tr>
<tr><td>Act number</td><td><b>Act No. 6 of 2014</b></td><td class="bi-te">Act No. 6/2014</td></tr>
</table>

<div class="section-hdr">What the Act Did / చట్టం ఏం చేసింది</div>
<table class="key-table">
<tr><th>Outcome</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>New state created</td><td>Telangana — <b>29th state of India</b></td><td class="bi-te">తెలంగాణ 29వ రాష్ట్రం</td></tr>
<tr><td>Residual AP districts</td><td>13 (later 26 in 2022; 28 from Jan 1, 2026)</td><td class="bi-te">13 జిల్లాలు (2014)</td></tr>
<tr><td>Common capital</td><td>Hyderabad for 10 years (2014-2024)</td><td class="bi-te">హైదరాబాద్ 10 సం.</td></tr>
<tr><td>Asset/debt division</td><td>~58.32% AP : 41.68% Telangana (population)</td><td class="bi-te">జనాభా ప్రకారం</td></tr>
<tr><td>AP Lok Sabha seats</td><td>25 (Section 24)</td><td class="bi-te">25 LS</td></tr>
<tr><td>AP Rajya Sabha seats</td><td>11 (Section 24)</td><td class="bi-te">11 RS</td></tr>
<tr><td>AP Assembly seats</td><td>175 (Telangana: 119)</td><td class="bi-te">175 అసెంబ్లీ</td></tr>
<tr><td>Schedule XIII institutions</td><td>IIT/NIT/AIIMS/IIM/IISER/CUAP/IIPE etc.</td><td class="bi-te">కేంద్ర సంస్థలు</td></tr>
</table>
<p>The APRA 2014 was tabled by Home Minister Sushilkumar Shinde. It is among India's most contested bifurcation laws — the Rajya Sabha passage on Feb 20 happened via voice vote amid opposition walkout. The Act has 13 parts, 108 sections and 13 Schedules. The 11 NE/hilly Special Category states were excluded from any new SCS recommendation; AP's SCS demand survived only as a verbal RS commitment by PM Manmohan Singh.</p>
<p class="bi-te">APRA 2014ని హోంమంత్రి సుశీల్ కుమార్ షిండే ప్రవేశపెట్టారు. ఫిబ్రవరి 20, 2014న RS లో విపక్షాల వాకవుట్ మధ్య voice vote ద్వారా ఆమోదించారు. చట్టానికి 13 భాగాలు, 108 సెక్షన్లు, 13 షెడ్యూళ్లు ఉన్నాయి. తెలంగాణ జూన్ 2, 2014న 29వ రాష్ట్రంగా అవతరించింది.</p>"""
    },
    {
        "id": "div10_s3",
        "title": "కీలక Sections — 5, 30, 94",
        "sub": "Key Sections of APRA 2014 — 5(2), 24, 30, 94",
        "summary": "Section 5(2): రాజధాని నిర్ణయం (2026లో సవరణ); Section 30: AP HC ఏర్పాటు; Section 94: పోలవరం జాతీయ ప్రాజెక్టు",
        "html": """<div class="concept-cover">
  <h1>Key Sections of APRA 2014 &nbsp;<span class="bi-te">/ APRA 2014 కీలక సెక్షన్లు</span></h1>
  <div class="sub">Section 5(2) • Section 24 • Section 30 • Section 94 • Section 93 + Schedule XIII</div>
</div>

<div class="section-hdr">Most Asked Sections / ఎక్కువగా అడిగే Sections</div>
<table class="key-table">
<tr><th>Section</th><th>Subject</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Section 3</td><td>Creation of Telangana state</td><td class="bi-te">తెలంగాణ ఏర్పాటు</td></tr>
<tr><td><b>Section 5(2)</b></td><td>Capital of residual AP (amended 2026 to name Amaravati)</td><td class="bi-te">రాజధాని — 2026లో అమరావతి</td></tr>
<tr><td>Section 8</td><td>Hyderabad common capital for 10 years</td><td class="bi-te">హైదరాబాద్ 10 సం.</td></tr>
<tr><td><b>Section 24</b></td><td>AP — 25 Lok Sabha + 11 Rajya Sabha; 175 Assembly</td><td class="bi-te">25 LS + 11 RS + 175 అసెం.</td></tr>
<tr><td><b>Section 30</b></td><td>AP High Court — separate HC for AP</td><td class="bi-te">AP HC ఏర్పాటు</td></tr>
<tr><td>Section 93 + Schedule XIII</td><td>Central institutions in AP (IIT/NIT/AIIMS/CUAP etc.)</td><td class="bi-te">కేంద్ర సంస్థల వాగ్దానం</td></tr>
<tr><td><b>Section 94</b></td><td><b>Polavaram declared National Project</b></td><td class="bi-te">పోలవరం జాతీయ ప్రాజెక్టు</td></tr>
<tr><td>Sections 84-89</td><td>Water disputes — Krishna &amp; Godavari River Mgmt Boards</td><td class="bi-te">జల వివాదాలు</td></tr>
</table>

<div class="section-hdr">Section 30 — AP High Court / Section 30 — AP HC</div>
<p>Section 30 mandated the Centre to establish a separate High Court for AP. <b>AP HC was operationalised on January 1, 2019 at Amaravati</b> (Justice City, Nelapadu, Guntur district), with Justice Praveen Kumar as the first Acting CJ and Justice JK Maheshwari as the first regular CJ. Before 2019, Hyderabad HC served both successor states. The current CJ (since Apr 25, 2026) is Justice Lisa Gill — first woman CJ of AP HC.</p>

<div class="section-hdr">Section 94 — Polavaram National Project / Section 94 — పోలవరం</div>
<p>Section 94 makes the Polavaram Multipurpose Irrigation Project a <b>National Project</b>, with the Centre obligated to fund construction in full. Submergence-zone mandals from Khammam (Telangana) were transferred to AP via Act No. 19 of 2014 (Jul 11, 2014). The project is expected to irrigate ~7.2 lakh acres in East and West Godavari and feed Krishna delta needs.</p>
<p class="bi-te">Section 30 ప్రకారం AP కి ప్రత్యేక హైకోర్టు ఏర్పడింది (జనవరి 1, 2019, అమరావతి). Section 94 ప్రకారం పోలవరం జాతీయ ప్రాజెక్టు హోదా పొంది, కేంద్రం పూర్తి నిధులు భరించాలి. Section 24 ప్రకారం AP కి 25 LS + 11 RS + 175 అసెంబ్లీ స్థానాలు; Council 58 (1985 పునఃస్థాపన).</p>"""
    },
    {
        "id": "div10_s4",
        "title": "Special Category Status (SCS)",
        "sub": "Special Category Status — Promise, 14th FC, Special Package",
        "summary": "మన్మోహన్ సింగ్ వాగ్దానం (2014); 14వ ఆర్థిక సంఘం రద్దు సిఫారసు (2015); చట్టరూపం లేదు; ఇంకా అమలు కాలేదు",
        "html": """<div class="concept-cover">
  <h1>Special Category Status &nbsp;<span class="bi-te">/ ప్రత్యేక హోదా</span></h1>
  <div class="sub">RS promise Feb 20, 2014 • 14th FC abolished category 2015 • Special Package alternative</div>
</div>

<div class="section-hdr">The SCS Promise / ప్రత్యేక హోదా వాగ్దానం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Who promised</td><td>PM Manmohan Singh (UPA-II)</td><td class="bi-te">మన్మోహన్ సింగ్</td></tr>
<tr><td>Where</td><td>Rajya Sabha floor — Feb 20, 2014</td><td class="bi-te">రాజ్యసభ — ఫిబ్రవరి 20, 2014</td></tr>
<tr><td>Form</td><td>Verbal assurance — <b>not written into APRA 2014</b></td><td class="bi-te">వాగ్దానమే — చట్టంలో లేదు</td></tr>
<tr><td>Duration sought</td><td>5 years (initially); extended to 10 years sought later</td><td class="bi-te">5 → 10 సం.</td></tr>
<tr><td>Then-current SCS states</td><td>11 NE + hilly (Arunachal, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura, J&amp;K, HP, Uttarakhand)</td><td class="bi-te">11 NE/Hilly states</td></tr>
</table>

<div class="section-hdr">14th Finance Commission (2015) / 14వ ఆర్థిక సంఘం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Chairman</td><td>Y.V. Reddy</td><td class="bi-te">వై.వి. రెడ్డి</td></tr>
<tr><td>Recommendation</td><td><b>Abolish the SCS category itself</b> (no fresh SCS to be granted)</td><td class="bi-te">SCS విధానం రద్దు</td></tr>
<tr><td>Compensation route</td><td>Higher devolution (32% → 42% of central taxes)</td><td class="bi-te">42% పంపకం</td></tr>
<tr><td>Centre's response (2016)</td><td>Special Assistance / Special Package for AP instead</td><td class="bi-te">ప్రత్యేక ప్యాకేజీ</td></tr>
</table>

<div class="section-hdr">Special Package &amp; Today's Position / ప్రత్యేక ప్యాకేజీ</div>
<p>Following the 14th FC, the NDA Centre offered AP a Special Package (Sep 2016) comprising EAP (Externally Aided Project) loan support, full central funding of Polavaram, Central institutional grants, and tax/duty incentives for backward Rayalaseema-North Coastal districts. The political demand for full SCS remains alive — TDP, JSP, BJP and YSRCP have all formally backed it in different periods. After the 2024 alliance returned to power, the Centre's stand is to continue Special Package + capital city assistance.</p>
<p class="bi-te">14వ ఆర్థిక సంఘం (వై.వి. రెడ్డి అధ్యక్షతన, 2015) SCS విధానమే రద్దు చేయాలని సిఫారసు చేయడంతో AP కి SCS ఇవ్వడం కష్టమైంది. దానికి బదులు సెప్టెంబర్ 2016లో ప్రత్యేక ప్యాకేజీ — EAP రుణ సహాయం, పోలవరం పూర్తి కేంద్ర నిధులు, వెనుకబడిన జిల్లాలకు రాయితీలు, కేంద్ర సంస్థల గ్రాంట్లు — ప్రకటించారు.</p>"""
    },
    {
        "id": "div10_s5",
        "title": "Amendment Act 2026 — అమరావతి రాజధాని",
        "sub": "APRA Amendment Act 2026 — Amaravati Named as Capital",
        "summary": "AP Reorganisation Amendment Act 2026, Act No. 7/2026; Lok Sabha ఏప్రిల్ 1; Rajya Sabha ఏప్రిల్ 2; రాష్ట్రపతి ఏప్రిల్ 6; అమరావతి జూన్ 2, 2024 నుండి (Retrospective)",
        "html": """<div class="concept-cover">
  <h1>APRA Amendment Act 2026 &nbsp;<span class="bi-te">/ APRA సవరణ చట్టం 2026</span></h1>
  <div class="sub">Act 7/2026 • Section 5(2) amended • Amaravati named • Retrospective Jun 2, 2024</div>
</div>

<div class="section-hdr">Passage Timeline / చట్టం ఆమోద క్రమం</div>
<table class="key-table">
<tr><th>Stage</th><th>Date</th><th class="bi-te">వివరణ</th></tr>
<tr><td>AP Assembly resolution to Centre</td><td>March 28, 2026</td><td class="bi-te">అసెంబ్లీ తీర్మానం</td></tr>
<tr><td>Bill introduced in Lok Sabha</td><td>Late March 2026 (Home Min. Amit Shah)</td><td class="bi-te">LS లో ప్రవేశం</td></tr>
<tr><td><b>Lok Sabha passage</b></td><td><b>April 1, 2026</b></td><td class="bi-te">LS — ఏప్రిల్ 1</td></tr>
<tr><td><b>Rajya Sabha passage</b></td><td><b>April 2, 2026</b></td><td class="bi-te">RS — ఏప్రిల్ 2</td></tr>
<tr><td><b>President's assent</b></td><td><b>April 6, 2026</b> (Droupadi Murmu, Article 111)</td><td class="bi-te">రాష్ట్రపతి — ఏప్రిల్ 6</td></tr>
<tr><td><b>Act number</b></td><td><b>Act No. 7 of 2026</b></td><td class="bi-te">Act No. 7/2026</td></tr>
<tr><td>Retrospective effect</td><td><b>From June 2, 2024</b></td><td class="bi-te">జూన్ 2, 2024 నుండి</td></tr>
</table>

<div class="section-hdr">What the Amendment Does / సవరణ ఏం చేసింది</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Section amended</td><td><b>Section 5(2) of APRA 2014</b></td><td class="bi-te">Section 5(2) సవరణ</td></tr>
<tr><td>Old text</td><td>"new capital" (un-named)</td><td class="bi-te">"నూతన రాజధాని"</td></tr>
<tr><td>New text</td><td><b>"Amaravati"</b> as legal capital of AP</td><td class="bi-te">అమరావతి</td></tr>
<tr><td>Amendment serial</td><td><b>3rd amendment</b> to APRA 2014</td><td class="bi-te">3వ APRA సవరణ</td></tr>
<tr><td>Historic significance</td><td>1st time an Indian state's capital is named via a central law</td><td class="bi-te">కేంద్ర చట్టంలో రాష్ట్ర రాజధాని పేరు — తొలిసారి</td></tr>
</table>

<p>This is the 3rd amendment to APRA 2014 (after the 7-mandals Act of 2014 and a 2018 administrative amendment). It writes <b>"Amaravati"</b> into the parent statute and removes the legal ambiguity that allowed the 3-capital proposals (2020 YSRCP) to surface. The retrospective date (June 2, 2024) corresponds to the day the TDP-JSP-BJP government took office and chose to revive Amaravati. Constitutional basis: Article 3 (Parliament's power to alter state areas) + Article 111 (President's assent).</p>
<p class="bi-te">2026 సవరణ APRA 2014కి 3వ సవరణ. Section 5(2) లో "నూతన రాజధాని" అన్న వాడుకలో ఉన్న వాక్యాన్ని తొలగించి "అమరావతి" అని నిర్దిష్టంగా పేర్కొంది. Retrospective తేదీ జూన్ 2, 2024 — అదే రోజు TDP-JSP-BJP కూటమి ప్రభుత్వం పదవీ స్వీకారం చేసిన రోజు. భారత చరిత్రలో ఒక రాష్ట్ర రాజధానిని కేంద్ర చట్టంలో పేరుతో చేర్చడం ఇదే తొలిసారి.</p>"""
    },
    {
        "id": "div10_s6",
        "title": "Article 371-D & చారిత్రక నేపథ్యం",
        "sub": "Article 371-D, G.O. 610 & States Reorganisation 1956",
        "summary": "Article 371-D: 32వ సవరణ 1973; G.O.610 6 Zones; States Reorganisation Act 1956; ఉమ్మడి AP నవంబర్ 1, 1956",
        "html": """<div class="concept-cover">
  <h1>Article 371-D &amp; Historical Background &nbsp;<span class="bi-te">/ ఆర్టికల్ 371-D &amp; చరిత్ర</span></h1>
  <div class="sub">32nd Amendment 1973 • G.O. 610 (1985) • SRA 1956 • Combined AP Nov 1, 1956</div>
</div>

<div class="section-hdr">Article 371-D / ఆర్టికల్ 371-D</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Inserted by</td><td><b>32nd Constitutional Amendment, 1973</b></td><td class="bi-te">32వ సవరణ, 1973</td></tr>
<tr><td>Applies to</td><td>Andhra Pradesh (and Telangana since 2014)</td><td class="bi-te">AP &amp; తెలంగాణ</td></tr>
<tr><td>Purpose</td><td>Local-area reservation in education + state-government employment</td><td class="bi-te">స్థానిక రిజర్వేషన్</td></tr>
<tr><td>Empowers</td><td>President to make orders defining local cadres and zones</td><td class="bi-te">రాష్ట్రపతి ఉత్తర్వులు</td></tr>
<tr><td>Presidential Order</td><td>AP Public Employment (Organisation of Local Cadres) Order, 1975</td><td class="bi-te">1975 ఉత్తర్వు</td></tr>
<tr><td>Survival post-bifurcation</td><td>Yes — applies to both successor states (APRA 2014 §97)</td><td class="bi-te">విభజన తర్వాత కూడా</td></tr>
</table>

<div class="section-hdr">G.O. 610 (1985) — 6 Zones / G.O. 610</div>
<p>G.O. Ms No. 610 (Dec 30, 1985) of the undivided AP government operationalised Article 371-D by classifying non-gazetted state-government posts under a <b>6-zone roster</b>: Zones I-IV (Coastal Andhra + Rayalaseema), Zones V-VI (Telangana). Each zone reserved a quota of posts for locals based on residential criteria. G.O. 610 has remained the touchstone for "Mulkhi rule" implementation and is frequently litigated.</p>

<div class="section-hdr">States Reorganisation Act, 1956 / రాష్ట్రాల పునర్వ్యవస్థీకరణ చట్టం 1956</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Commission</td><td>Fazal Ali Commission (1953) — Pandit H.N. Kunzru, K.M. Panikkar members</td><td class="bi-te">ఫజల్ అలీ కమిషన్</td></tr>
<tr><td>Basis of reorganisation</td><td>Language (linguistic states)</td><td class="bi-te">భాష ఆధారంగా</td></tr>
<tr><td>Date</td><td><b>November 1, 1956</b></td><td class="bi-te">నవంబర్ 1, 1956</td></tr>
<tr><td>Outcome for Telugu-speakers</td><td>Combined Andhra Pradesh formed by merging Andhra State (1953) with Telugu-speaking areas of Hyderabad State</td><td class="bi-te">ఉమ్మడి AP ఏర్పాటు</td></tr>
<tr><td>Andhra State (separate)</td><td>October 1, 1953 — Telugu areas of Madras Presidency</td><td class="bi-te">ఆంధ్ర రాష్ట్రం — అక్టోబర్ 1, 1953</td></tr>
</table>
<p class="bi-te">భాష ఆధారంగా రాష్ట్రాల పునర్వ్యవస్థీకరణ చట్టం, 1956 ప్రకారం నవంబర్ 1, 1956న ఉమ్మడి ఆంధ్రప్రదేశ్ ఏర్పడింది (1953 ఆంధ్ర రాష్ట్రం + హైదరాబాద్ తెలుగు ప్రాంతాలు). Article 371-Dని 32వ సవరణ 1973 ద్వారా చేర్చి స్థానిక రిజర్వేషన్‌లకు రాజ్యాంగ హక్కు కల్పించారు. దీని ఆధారంగా 1985లో G.O. 610 ద్వారా 6 జోన్ల రోస్టర్ సిస్టమ్ అమల్లోకి వచ్చింది.</p>"""
    },
    {
        "id": "div10_s7",
        "title": "7 మండలాల బదిలీ — ఖమ్మం నుండి AP కి",
        "sub": "7 Mandals Transfer — Khammam to AP (Polavaram)",
        "summary": "APRA Amendment Act No. 19/2014 (జూలై 11, 2014); 7 మండలాలు ఖమ్మం → తూ/ప గోదావరి; పోలవరం కోసం; తెలంగాణ 5 గ్రామాల డిమాండ్",
        "html": """<div class="concept-cover">
  <h1>7 Mandals Transfer &nbsp;<span class="bi-te">/ 7 మండలాల బదిలీ</span></h1>
  <div class="sub">Act No. 19/2014 • Jul 11, 2014 • Khammam to East &amp; West Godavari • Polavaram</div>
</div>

<div class="section-hdr">The Transfer Act / బదిలీ చట్టం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Statute</td><td><b>AP Reorganisation (Amendment) Act, 2014</b></td><td class="bi-te">2014 APRA సవరణ</td></tr>
<tr><td><b>Act number</b></td><td><b>Act No. 19 of 2014</b></td><td class="bi-te">Act No. 19/2014</td></tr>
<tr><td>Lok Sabha passage</td><td><b>July 11, 2014</b></td><td class="bi-te">జూలై 11, 2014</td></tr>
<tr><td>Purpose</td><td>Bring Polavaram submergence-area mandals fully into AP</td><td class="bi-te">పోలవరం ముంపు ప్రాంతం</td></tr>
<tr><td>Originating district</td><td>Khammam, Telangana</td><td class="bi-te">ఖమ్మం జిల్లా</td></tr>
<tr><td>Receiving districts</td><td>East Godavari (4 mandals) + West Godavari (3 mandals)</td><td class="bi-te">తూర్పు 4 + పశ్చిమ 3</td></tr>
</table>

<div class="section-hdr">The 7 Mandals / 7 మండలాలు</div>
<table class="key-table">
<tr><th>Mandal</th><th>Merged into</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Kunavaram (కునవరం)</td><td>East Godavari</td><td class="bi-te">తూర్పు గోదావరి</td></tr>
<tr><td>V.R. Puram (వి.ఆర్. పురం)</td><td>East Godavari</td><td class="bi-te">తూర్పు గోదావరి</td></tr>
<tr><td>Chintur (చింతూరు)</td><td>East Godavari</td><td class="bi-te">తూర్పు గోదావరి</td></tr>
<tr><td>Nellipaka (నెల్లిపాక)</td><td>East Godavari</td><td class="bi-te">తూర్పు గోదావరి</td></tr>
<tr><td>Velerupadu (వేలేర్పాడు)</td><td>West Godavari</td><td class="bi-te">పశ్చిమ గోదావరి</td></tr>
<tr><td>Kukunoor (కుకుణూరు)</td><td>West Godavari</td><td class="bi-te">పశ్చిమ గోదావరి</td></tr>
<tr><td>Burgampahad (బుర్గంపాడు) — partial</td><td>West Godavari</td><td class="bi-te">పశ్చిమ గోదావరి (పాక్షికం)</td></tr>
</table>

<p><b>Telangana's 5-village demand:</b> Telangana has been demanding return of 5 villages (Etapaka, Kannaigudem, Pichukalapadu, Purushottapatnam, Gundala) of the Bhadrachalam division, arguing they lie outside the Polavaram submergence contour. The Supreme Court is seized of the matter. After the 2022 AP district reorganisation, these mandals were folded into the newly carved Alluri Sitarama Raju (ASR) and Eluru districts respectively.</p>
<p class="bi-te">పోలవరం ముంపు ప్రాంతం AP లోనే ఉండేలా చేయడానికి జూలై 11, 2014న Act No. 19/2014 ద్వారా ఖమ్మం జిల్లాలోని 7 మండలాలను తూర్పు, పశ్చిమ గోదావరి జిల్లాలకు బదిలీ చేశారు. తెలంగాణ ఏటపాక, కన్నాయిగూడెం, పిచుకలపాడు, పురుషోత్తపట్నం, గుండాల అనే 5 గ్రామాలను తిరిగి తమకు ఇవ్వాలని డిమాండ్ చేస్తోంది.</p>"""
    },
    {
        "id": "div10_s8",
        "title": "Rapid Revision — పరీక్ష పట్టిక",
        "sub": "Rapid Revision — One-Page Cheat Sheet",
        "summary": "APRA 2014 అన్ని కీలక తేదీలు, Sections, Amendment 2026 వివరాలు — సంక్షిప్త పట్టిక",
        "html": """<div class="concept-cover">
  <h1>Rapid Revision — Cheat Sheet &nbsp;<span class="bi-te">/ సంక్షిప్త పట్టిక</span></h1>
  <div class="sub">All Division 10 high-yield facts in one place</div>
</div>

<div class="section-hdr">Critical Dates / కీలక తేదీలు</div>
<table class="key-table">
<tr><th>Date</th><th>Event</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Feb 18, 2014</td><td>APRA — Lok Sabha passed</td><td class="bi-te">LS ఆమోదం</td></tr>
<tr><td>Feb 20, 2014</td><td>APRA — Rajya Sabha passed (voice vote)</td><td class="bi-te">RS ఆమోదం</td></tr>
<tr><td>Mar 1, 2014</td><td>President Pranab Mukherjee assent</td><td class="bi-te">రాష్ట్రపతి అంగీకారం</td></tr>
<tr><td><b>Jun 2, 2014</b></td><td><b>APRA effective; Telangana = 29th state</b></td><td class="bi-te">అమలు; తెలంగాణ 29వ</td></tr>
<tr><td>Jul 11, 2014</td><td>Act No. 19/2014 — 7 mandals transferred</td><td class="bi-te">7 మండలాల బదిలీ</td></tr>
<tr><td>Jan 1, 2019</td><td>AP HC operationalised at Amaravati (§30)</td><td class="bi-te">AP HC ఏర్పాటు</td></tr>
<tr><td>Apr 1, 2026</td><td>Amaravati Bill — Lok Sabha</td><td class="bi-te">అమరావతి LS</td></tr>
<tr><td>Apr 2, 2026</td><td>Amaravati Bill — Rajya Sabha</td><td class="bi-te">అమరావతి RS</td></tr>
<tr><td>Apr 6, 2026</td><td>President's assent (Act 7/2026)</td><td class="bi-te">రాష్ట్రపతి అంగీకారం</td></tr>
</table>

<div class="section-hdr">Section Snapshot / Sections సంక్షిప్తం</div>
<table class="key-table">
<tr><th>Section</th><th>Subject</th></tr>
<tr><td>5(2)</td><td>Capital (amended 2026 — Amaravati)</td></tr>
<tr><td>8</td><td>Hyderabad common capital 10 yrs</td></tr>
<tr><td>24</td><td>25 LS + 11 RS + 175 Assembly</td></tr>
<tr><td>30</td><td>AP High Court</td></tr>
<tr><td>93 + Sch. XIII</td><td>Central institutions promise</td></tr>
<tr><td>94</td><td>Polavaram National Project</td></tr>
</table>

<div class="section-hdr">Act Numbers / Act Numbers</div>
<table class="key-table">
<tr><th>Act</th><th>Number</th></tr>
<tr><td>APRA original</td><td>Act No. 6 of 2014</td></tr>
<tr><td>APRA 7-mandals amend.</td><td>Act No. 19 of 2014</td></tr>
<tr><td>APRA Amendment 2026 (Amaravati)</td><td>Act No. 7 of 2026</td></tr>
<tr><td>Constitutional basis</td><td>Article 3 + Article 111</td></tr>
<tr><td>Article 371-D</td><td>32nd Amendment, 1973</td></tr>
</table>
<p class="bi-te">పరీక్షకు ఈ పట్టిక 5-నిమిషాల రివిజన్‌కు సరిపోతుంది. ముఖ్య సూత్రం: APRA 2014 = Act 6/2014 (జూన్ 2, 2014); 7 మండలాలు = Act 19/2014 (జూలై 11, 2014); అమరావతి సవరణ = Act 7/2026 (ఏప్రిల్ 6, 2026, retrospective జూన్ 2, 2024).</p>"""
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Key concepts
    {
        "section_idx": 0,
        "question": "Andhra Pradesh Reorganisation Act, 2014 అమల్లోకి వచ్చిన తేదీ ఏది?",
        "options": ["మే 2, 2014", "జూన్ 2, 2014", "జూలై 2, 2014", "ఆగస్టు 2, 2014"],
        "answer": "B",
        "explanation": "APRA 2014 జూన్ 2, 2014న అమల్లోకి వచ్చింది. ఇదే తేదీన తెలంగాణ 29వ రాష్ట్రంగా అవతరించింది."
    },
    {
        "section_idx": 0,
        "question": "APRA 2014 ప్రకారం హైదరాబాద్ ఎన్ని సంవత్సరాలు ఉభయ రాష్ట్రాలకు ఉమ్మడి రాజధానిగా ఉంటుంది?",
        "options": ["5 సంవత్సరాలు", "8 సంవత్సరాలు", "10 సంవత్సరాలు", "15 సంవత్సరాలు"],
        "answer": "C",
        "explanation": "APRA 2014 ప్రకారం హైదరాబాద్ 10 సంవత్సరాలు (2014–2024) AP మరియు తెలంగాణ రెండు రాష్ట్రాలకూ ఉమ్మడి రాజధానిగా ఉంటుంది."
    },
    {
        "section_idx": 0,
        "question": "AP Reorganisation Act 2014 యొక్క Act Number ఏది?",
        "options": ["Act No. 4 of 2014", "Act No. 6 of 2014", "Act No. 8 of 2014", "Act No. 10 of 2014"],
        "answer": "B",
        "explanation": "AP Reorganisation Act 2014 యొక్క Act Number = Act No. 6 of 2014. 2026 Amendment Act Number = Act No. 7 of 2026."
    },
    # Section 1 — APRA 2014 full details
    {
        "section_idx": 1,
        "question": "APRA 2014కి Lok Sabha ఎప్పుడు ఆమోదం తెలిపింది?",
        "options": ["జనవరి 18, 2014", "ఫిబ్రవరి 18, 2014", "మార్చి 18, 2014", "ఏప్రిల్ 18, 2014"],
        "answer": "B",
        "explanation": "APRA 2014కి Lok Sabha ఫిబ్రవరి 18, 2014న మరియు Rajya Sabha ఫిబ్రవరి 20, 2014న ఆమోదం తెలిపాయి. రాష్ట్రపతి మార్చి 1, 2014న సంతకం చేశారు."
    },
    {
        "section_idx": 1,
        "question": "తెలంగాణ భారతదేశంలో ఎన్నవ రాష్ట్రంగా ఏర్పాటైంది?",
        "options": ["27వ రాష్ట్రం", "28వ రాష్ట్రం", "29వ రాష్ట్రం", "30వ రాష్ట్రం"],
        "answer": "C",
        "explanation": "తెలంగాణ జూన్ 2, 2014న భారతదేశంలో 29వ రాష్ట్రంగా అవతరించింది. ప్రస్తుతం 28 రాష్ట్రాలు ఉన్నాయి (J&K UT అయినందున)."
    },
    {
        "section_idx": 1,
        "question": "APRA 2014 ప్రకారం నూతన ఆంధ్రప్రదేశ్ ఎన్ని జిల్లాలతో ఏర్పాటైంది?",
        "options": ["10 జిల్లాలు", "13 జిల్లాలు", "15 జిల్లాలు", "17 జిల్లాలు"],
        "answer": "B",
        "explanation": "APRA 2014 అమలైన జూన్ 2, 2014న నూతన ఆంధ్రప్రదేశ్ 13 జిల్లాలతో ఏర్పాటైంది. తర్వాత 2022 ఏప్రిల్‌లో 26 జిల్లాలుగా, 2026లో 28 జిల్లాలుగా పెరిగాయి."
    },
    # Section 2 — Key Sections
    {
        "section_idx": 2,
        "question": "APRA 2014 యొక్క ఏ Section ఆంధ్రప్రదేశ్ రాజధాని నిర్ణయానికి సంబంధించినది?",
        "options": ["Section 3", "Section 5(2)", "Section 24", "Section 30"],
        "answer": "B",
        "explanation": "APRA 2014 Section 5(2) AP రాజధాని నిర్ణయానికి సంబంధించిన section. దీన్ని 2026 Amendment Act లో సవరించి అమరావతిని అధికారిక రాజధానిగా నిర్ణయించారు."
    },
    {
        "section_idx": 2,
        "question": "APRA 2014 Section 30 దేనికి సంబంధించినది?",
        "options": ["SCS హోదా", "పోలవరం ప్రాజెక్టు", "AP High Court ఏర్పాటు", "నీటి పంపకం"],
        "answer": "C",
        "explanation": "APRA 2014 Section 30 AP కి ప్రత్యేక High Court ఏర్పాటుకు సంబంధించినది. దీని ప్రకారం కేంద్ర ప్రభుత్వానికి AP HC స్థాపించే బాధ్యత ఉంది. AP HC జనవరి 1, 2019న అమరావతిలో ఏర్పాటైంది."
    },
    {
        "section_idx": 2,
        "question": "APRA 2014 Section 94 దేనికి సంబంధించినది?",
        "options": ["Article 371-D", "పోలవరం జాతీయ ప్రాజెక్టు", "Special Category Status", "AP HC"],
        "answer": "B",
        "explanation": "APRA 2014 Section 94 పోలవరం ప్రాజెక్టుకు జాతీయ ప్రాజెక్టు హోదా కల్పించింది. దీని ప్రకారం కేంద్ర ప్రభుత్వం పోలవరం నిధులు పూర్తిగా భరించాలి."
    },
    {
        "section_idx": 2,
        "question": "AP High Court ఏ తేదీన అమరావతిలో ఏర్పాటైంది?",
        "options": ["జూన్ 2, 2017", "జనవరి 1, 2019", "మార్చి 1, 2019", "జూలై 1, 2020"],
        "answer": "B",
        "explanation": "APRA 2014 Section 30 కింద AP కి ప్రత్యేక High Court జనవరి 1, 2019న అమరావతిలో ఏర్పాటైంది. Justice Rakesh Kumar మొదటి Chief Justice."
    },
    # Section 3 — SCS
    {
        "section_idx": 3,
        "question": "AP కి Special Category Status ఇస్తామని 2014లో ఎవరు వాగ్దానం చేశారు?",
        "options": ["నరేంద్ర మోదీ ప్రభుత్వం", "మన్మోహన్ సింగ్ ప్రభుత్వం", "అటల్ బిహారీ వాజ్‌పేయి ప్రభుత్వం", "చంద్రబాబు నాయుడు"],
        "answer": "B",
        "explanation": "2014 APRA Rajya Sabha చర్చ సందర్భంగా మన్మోహన్ సింగ్ నేతృత్వంలోని UPA ప్రభుత్వం AP కి SCS ఇస్తామని వాగ్దానం చేసింది. కానీ ఇది చట్టరూపం తీసుకోలేదు."
    },
    {
        "section_idx": 3,
        "question": "14వ ఆర్థిక సంఘం SCS విషయంలో ఏమి సిఫారసు చేసింది?",
        "options": ["AP కి SCS ఇవ్వాలి", "SCS విధానాన్నే రద్దు చేయాలి", "SCS ని 5 సంవత్సరాలు పొడిగించాలి", "SCS కి బదులు వేరే ప్యాకేజీ ఇవ్వాలి"],
        "answer": "B",
        "explanation": "14వ ఆర్థిక సంఘం (2015) SCS విధానాన్నే రద్దు చేయాలని సిఫారసు చేసింది. ఈ సిఫారసు అమలైంది, దీంతో AP కి SCS ఇచ్చే వీలు లేకుండా పోయింది."
    },
    # Section 4 — Amendment Act 2026
    {
        "section_idx": 4,
        "question": "AP Reorganisation (Amendment) Act, 2026 యొక్క Act Number ఏది?",
        "options": ["Act No. 5 of 2026", "Act No. 7 of 2026", "Act No. 9 of 2026", "Act No. 11 of 2026"],
        "answer": "B",
        "explanation": "AP Reorganisation (Amendment) Act, 2026 యొక్క Act Number = Act No. 7 of 2026. ఇది 2014 మూల చట్టం (Act No. 6 of 2014) Section 5(2) ని సవరించింది."
    },
    {
        "section_idx": 4,
        "question": "అమరావతి బిల్లుకు Lok Sabha ఏ తేదీన ఆమోదం తెలిపింది?",
        "options": ["మార్చి 28, 2026", "ఏప్రిల్ 1, 2026", "ఏప్రిల్ 2, 2026", "ఏప్రిల్ 6, 2026"],
        "answer": "B",
        "explanation": "అమరావతి బిల్లుకు Lok Sabha ఏప్రిల్ 1, 2026న మరియు Rajya Sabha ఏప్రిల్ 2, 2026న ఆమోదం తెలిపాయి. రాష్ట్రపతి ద్రౌపదీ ముర్ము ఏప్రిల్ 6, 2026న సంతకం చేశారు."
    },
    {
        "section_idx": 4,
        "question": "Amendment Act 2026 ప్రకారం అమరావతి ఏ తేదీ నుండి అధికారిక రాజధాని?",
        "options": ["ఏప్రిల్ 6, 2026 నుండి", "మార్చి 28, 2026 నుండి", "జూన్ 2, 2024 నుండి (Retrospective)", "జనవరి 1, 2025 నుండి"],
        "answer": "C",
        "explanation": "Amendment Act 2026 Retrospective గా (వెనక్కి వర్తించే విధంగా) జూన్ 2, 2024 నుండి అమరావతిని అధికారిక రాజధానిగా గుర్తించింది. చట్టం 2026లో ఆమోదించినా, అమరావతి 2024 జూన్ 2 నుండే అధికారిక రాజధాని."
    },
    {
        "section_idx": 4,
        "question": "అమరావతి బిల్లుపై రాష్ట్రపతి ఏ అధికారం కింద సంతకం చేశారు?",
        "options": ["Article 108", "Article 111", "Article 368", "Article 131"],
        "answer": "B",
        "explanation": "రాష్ట్రపతి ద్రౌపదీ ముర్ము Article 111 కింద తమ అధికారాలను ఉపయోగించి అమరావతి బిల్లుపై సంతకం చేశారు. Article 111 — రాష్ట్రపతి Bills కి అంగీకారం తెలిపే Article."
    },
    {
        "section_idx": 4,
        "question": "AP అసెంబ్లీ అమరావతిని రాజధానిగా ప్రకటించాలని కేంద్రానికి ఎప్పుడు తీర్మానం పంపింది?",
        "options": ["మార్చి 28, 2026", "ఫిబ్రవరి 28, 2026", "ఏప్రిల్ 1, 2026", "జనవరి 28, 2026"],
        "answer": "A",
        "explanation": "AP శాసనసభ మార్చి 28, 2026న అమరావతిని రాజధానిగా ప్రకటించాలని కేంద్రానికి తీర్మానం పంపింది. దీన్ని ఆధారంగా కేంద్రం APRA Section 5(2) సవరణ బిల్లు ప్రవేశపెట్టింది."
    },
    # Section 5 — Article 371-D
    {
        "section_idx": 5,
        "question": "Article 371-D ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చబడింది?",
        "options": ["22వ సవరణ, 1969", "32వ సవరణ, 1973", "42వ సవరణ, 1976", "44వ సవరణ, 1978"],
        "answer": "B",
        "explanation": "Article 371-D ని 32వ రాజ్యాంగ సవరణ చట్టం, 1973 ద్వారా ఉమ్మడి AP కి ప్రత్యేక సంరక్షణ కల్పించేందుకు చేర్చారు. ఇది విద్య మరియు ఉద్యోగాల్లో స్థానికత ఆధారంగా రాయితీలు ఇవ్వడానికి అనుమతిస్తుంది."
    },
    {
        "section_idx": 5,
        "question": "ఉమ్మడి AP (States Reorganisation Act 1956 కింద) ఎప్పుడు ఏర్పాటైంది?",
        "options": ["అక్టోబర్ 1, 1953", "నవంబర్ 1, 1956", "జూన్ 2, 1956", "జనవరి 26, 1957"],
        "answer": "B",
        "explanation": "States Reorganisation Act 1956 కింద భాష ఆధారంగా నవంబర్ 1, 1956న ఉమ్మడి ఆంధ్రప్రదేశ్ ఏర్పాటైంది. అక్టోబర్ 1, 1953న ప్రత్యేక ఆంధ్ర రాష్ట్రం (హైదరాబాద్ లేకుండా) ఏర్పాటైంది."
    },
    {
        "section_idx": 5,
        "question": "APRA 2014 ప్రకారం AP లో Rajya Sabha స్థానాలు ఎన్ని?",
        "options": ["7 స్థానాలు", "9 స్థానాలు", "11 స్థానాలు", "13 స్థానాలు"],
        "answer": "C",
        "explanation": "APRA 2014 Section 24 ప్రకారం AP కి 11 Rajya Sabha స్థానాలు, 25 Lok Sabha స్థానాలు, 175 అసెంబ్లీ స్థానాలు ఉన్నాయి."
    },
    # Section 6 — 7 Mandals Transfer
    {
        "section_idx": 6,
        "question": "పోలవరం ప్రాజెక్టు కోసం తెలంగాణ నుండి AP కి బదిలీ చేసిన మండలాల సంఖ్య ఎన్ని?",
        "options": ["5 మండలాలు", "7 మండలాలు", "9 మండలాలు", "11 మండలాలు"],
        "answer": "B",
        "explanation": "APRA Amendment Act 2014 (Act No. 19/2014) ద్వారా తెలంగాణలోని ఖమ్మం జిల్లా నుండి 7 మండలాలు AP కి బదిలీ చేశారు. పోలవరం జాతీయ ప్రాజెక్టు నిర్మాణ ప్రాంతం AP పరిధిలో ఉండేందుకు ఇది చేశారు."
    },
    {
        "section_idx": 6,
        "question": "7 మండలాల బదిలీకి సంబంధించిన AP Reorganisation (Amendment) Act, 2014 యొక్క Act Number ఏది?",
        "options": ["Act No. 6 of 2014", "Act No. 9 of 2014", "Act No. 19 of 2014", "Act No. 25 of 2014"],
        "answer": "C",
        "explanation": "పోలవరం కోసం 7 మండలాల బదిలీకి AP Reorganisation (Amendment) Act, 2014 — Act No. 19 of 2014 పాస్ చేశారు (జూలై 11, 2014). ఇది మూల APRA Act No. 6/2014 కంటే వేరు."
    },
    {
        "section_idx": 6,
        "question": "7 మండలాల బదిలీ చట్టాన్ని Lok Sabha ఎప్పుడు ఆమోదించింది?",
        "options": ["జూన్ 2, 2014", "జూలై 11, 2014", "ఆగస్టు 15, 2014", "సెప్టెంబర్ 1, 2014"],
        "answer": "B",
        "explanation": "7 మండలాల బదిలీ చట్టం (Act No. 19/2014) జూలై 11, 2014న Lok Sabha ఆమోదించింది. ఈ మండలాలు ఖమ్మం జిల్లా నుండి తూర్పు, పశ్చిమ గోదావరి జిల్లాలకు వెళ్ళాయి."
    },
    {
        "section_idx": 6,
        "question": "7 మండలాల్లో తూర్పు గోదావరి జిల్లాలో చేర్చిన మండలం ఏది?",
        "options": ["కుకుణూరు", "వేలేర్పాడు", "కునవరం", "బుర్గంపాడు"],
        "answer": "C",
        "explanation": "కునవరం, వి.ఆర్.పురం, చింతూరు, నెల్లిపాక మండలాలు తూర్పు గోదావరి జిల్లాలో చేర్చారు. వేలేర్పాడు, బుర్గంపాడు, కుకుణూరు పశ్చిమ గోదావరి జిల్లాలో చేర్చారు."
    },
    {
        "section_idx": 6,
        "question": "తెలంగాణ తిరిగి తమకు ఇవ్వాలని డిమాండ్ చేస్తున్న 5 గ్రామాలు ఏ ప్రాంతానికి సంబంధించినవి?",
        "options": ["నల్గొండ", "వరంగల్", "భద్రాచలం", "ఖమ్మం పట్టణం"],
        "answer": "C",
        "explanation": "తెలంగాణ ఏటపాక, కన్నాయిగూడెం, పుచ్చుకలపాడు, పురుషోత్తమపట్నం, గుండాల అనే 5 గ్రామాలు భద్రాచలం డివిజన్ పరిధిలో ఉన్నాయని, అవి పోలవరం మునక ప్రాంతం వెలుపల ఉన్నాయని వాదిస్తోంది."
    },
]

# ── Helper functions ──────────────────────────────────────────────────────────

def _seed_ap_ca_div10_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 10."""
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (10, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (10, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division10', 10,
         'AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026',
         'AP Reorganisation Act 2014 & Amendment 2026',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div10 notes seeded!'}
def _seed_ap_ca_div10_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 10 (AP Reorganisation Act 2014)."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (10, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div10_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (10, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print("[div10-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    # Always delete-then-reinsert so seed-file changes are reflected (force is ignored here).
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    for mcq in MCQ_DATA:
        # Handle both dict formats: "question"/"options" or "question_te"/"opt_a"-"opt_d"
        q_te = mcq.get('question_te', mcq.get('question', ''))
        if 'options' in mcq:
            opts = mcq['options']
            a, b, c, d = (opts + ['', '', '', ''])[:4]
        else:
            a = mcq.get('opt_a', '')
            b = mcq.get('opt_b', '')
            c = mcq.get('opt_c', '')
            d = mcq.get('opt_d', '')
        correct = str(mcq.get('answer', mcq.get('correct', 'a'))).lower()
        expl = mcq.get('explanation_te', mcq.get('explanation', ''))
        sec = mcq.get('section_idx', 0)
        db_exec(conn, insert_sql, (note_id, sec, 2, q_te, a, b, c, d, correct, expl))
    if USE_POSTGRES:
        conn.commit()
    return {'success': True, 'message': f'AP CA Div10 MCQs seeded! Total: {len(MCQ_DATA)}'}

# Additional MCQs for div10 appended
_EXTRA_MCQ_DATA_10 = [
    # AUDIT D7 (Batch G): Removed duplicate — APRA 2014 Lok Sabha date already asked in
    # original MCQ_DATA section 1 (line 93-97).
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "APRA 2014 Rajya Sabha లో ఏ తేదీన ఆమోదం పొందింది?",
        "opt_a": "ఫిబ్రవరి 18, 2014",
        "opt_b": "ఫిబ్రవరి 19, 2014",
        "opt_c": "ఫిబ్రవరి 20, 2014",
        "opt_d": "ఫిబ్రవరి 24, 2014",
        "answer": "C",
        "explanation_te": "APRA 2014 Rajya Sabha లో ఫిబ్రవరి 20, 2014న ఆమోదించబడింది. ఇది భారత పార్లమెంట్ ద్వారా చాలా వివాదాస్పదంగా ఆమోదించబడింది."
    },
    # AUDIT D7 (Batch G): Removed 6 duplicates — these facts already covered in original
    # MCQ_DATA: Act Number (line 85-89), Telangana 29th state (line 100-104), Section 30
    # (line 122-126), Section 94 (line 130-133), Section 5(2) (line 116-119), 10-year joint
    # capital (line 80-82). Kept the unique Rajya Sabha date question above.
    # AUDIT D7 (Batch G): Removed duplicate — SCS Manmohan Singh promise already asked in
    # original MCQ_DATA (line 144-148).
    {
        "section_idx": 3,
        "difficulty": "hard",
        "question_te": "AP-తెలంగాణ ఆస్తుల విభజన నిష్పత్తి ఏమిటి?",
        "opt_a": "50:50",
        "opt_b": "60:40",
        "opt_c": "58.32:41.68 (AP:TG)",
        "opt_d": "70:30",
        "answer": "C",
        "explanation_te": "APRA 2014 ప్రకారం ఉమ్మడి AP ఆస్తులు 58.32% (AP) : 41.68% (తెలంగాణ) నిష్పత్తిలో జనాభా ఆధారంగా విభజించబడ్డాయి."
    },
    # AUDIT D7 (Batch G): Removed duplicate — 14th Finance Commission SCS Special Package
    # recommendation already asked in original MCQ_DATA (line 152-154).
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "AP Reorganisation Amendment Act 2026 Act Number ఏమిటి?",
        "opt_a": "Act No. 5 of 2026",
        "opt_b": "Act No. 6 of 2026",
        "opt_c": "Act No. 7 of 2026",
        "opt_d": "Act No. 10 of 2026",
        "answer": "C",
        "explanation_te": "AP Reorganisation Amendment Act 2026 — Act No. 7 of 2026. ఇది అమరావతిని AP అధికారిక రాజధానిగా పేర్కొంది."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "2026 Amendment Act Lok Sabha లో ఏ తేదీన ఆమోదం పొందింది?",
        "opt_a": "మార్చి 31, 2026",
        "opt_b": "ఏప్రిల్ 1, 2026",
        "opt_c": "ఏప్రిల్ 2, 2026",
        "opt_d": "ఏప్రిల్ 6, 2026",
        "answer": "B",
        "explanation_te": "2026 AP Reorganisation Amendment Act Lok Sabha లో ఏప్రిల్ 1, 2026న ఆమోదించబడింది. Rajya Sabha ఏప్రిల్ 2 న, రాష్ట్రపతి ఏప్రిల్ 6న ఆమోదించారు."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "G.O.610 దేనికి సంబంధించినది?",
        "opt_a": "పోలవరం ప్రాజెక్టు",
        "opt_b": "AP విద్య-ఉద్యోగాలలో 6 Zones రోస్టర్ సిస్టమ్",
        "opt_c": "జల వివాదాలు",
        "opt_d": "రాజధాని నిర్మాణం",
        "answer": "B",
        "explanation_te": "G.O.610 AP లో విద్య-ఉద్యోగాలను 6 Zones లో విభజించి స్థానికులకు రక్షణ కల్పించే రోస్టర్ సిస్టమ్ గురించి. ఆర్టికల్ 371-D కింద అమలైంది."
    },
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "States Reorganisation Act 1956 ఏ ఆధారంగా రాష్ట్రాలను ఏర్పాటు చేసింది?",
        "opt_a": "మతం",
        "opt_b": "భాష",
        "opt_c": "జాతి",
        "opt_d": "ఆర్థిక అభివృద్ధి",
        "answer": "B",
        "explanation_te": "States Reorganisation Act 1956 భాష ఆధారంగా రాష్ట్రాలను పునర్వ్యవస్థీకరించింది. ఫజల్ అలీ కమిషన్ నివేదిక ఆధారంగా అమలైంది. తెలుగు మాట్లాడే ప్రాంతాలు కలిసి AP ఏర్పాటైంది."
    },
    {
        "section_idx": 6,
        "difficulty": "hard",
        "question_te": "AP Reorganisation Amendment Act No. 19 of 2014 దేనికి సంబంధించినది?",
        "opt_a": "రాజధాని నిర్ణయం",
        "opt_b": "7 మండలాలు ఖమ్మం జిల్లా నుండి AP కి బదిలీ",
        "opt_c": "పోలవరం ఆమోదం",
        "opt_d": "SCS మంజూరు",
        "answer": "B",
        "explanation_te": "Amendment Act No. 19 of 2014 (జూలై 11, 2014) ఖమ్మం జిల్లా నుండి 7 మండలాలను తూ/ప గోదావరి జిల్లాలకు బదిలీ చేసింది. పోలవరం ప్రాజెక్టు నిర్మాణం కోసం."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "APRA 2014 ప్రకారం పోలవరం ప్రాజెక్టు నిర్మాణ నిధులు ఎవరు భరించాలి?",
        "opt_a": "AP రాష్ట్ర ప్రభుత్వం",
        "opt_b": "కేంద్ర ప్రభుత్వం పూర్తిగా",
        "opt_c": "AP-తెలంగాణ సమానంగా",
        "opt_d": "ప్రైవేట్ సంస్థలు",
        "answer": "B",
        "explanation_te": "APRA 2014 Section 94 ప్రకారం పోలవరం జాతీయ ప్రాజెక్టుగా కేంద్ర ప్రభుత్వం పూర్తి నిధులు అందించాలి. ఇది AP రాష్ట్రానికి గొప్ప ప్రయోజనం."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "AP Reorganisation Act 2014 Rajya Sabha లో ఎందుకు వివాదాస్పదంగా ఆమోదించబడింది?",
        "opt_a": "ఆర్థిక కారణాలు",
        "opt_b": "Voting లేకుండా Voice Vote ద్వారా విపక్షాల నిరసన మధ్య ఆమోదించడం",
        "opt_c": "సరైన నోటీసు ఇవ్వకుండా",
        "opt_d": "రాష్ట్రపతి ఆమోదం లేకుండా",
        "answer": "B",
        "explanation_te": "APRA 2014 Rajya Sabha లో ఫిబ్రవరి 20, 2014న విపక్షాల తీవ్ర నిరసన మధ్య Voice Vote ద్వారా ఆమోదించబడింది. AP నుండి సభ్యులు వాకవుట్ చేశారు."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "AP రాజ్యాంగ పరిషత్ (State Constituent Assembly) ఎప్పుడు రద్దు అయింది?",
        "opt_a": "1950",
        "opt_b": "1956",
        "opt_c": "1960",
        "opt_d": "AP కి ప్రత్యేక రాజ్యాంగ పరిషత్ లేదు",
        "answer": "D",
        "explanation_te": "AP ఒక భారత రాష్ట్రం. రాష్ట్రాలకు ప్రత్యేక రాజ్యాంగాలు ఉండవు — భారత రాజ్యాంగం మాత్రమే వర్తిస్తుంది."
    },
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "ఉమ్మడి AP (Undivided AP) ఏ సంవత్సరాల మధ్య ఉంది?",
        "opt_a": "1950–2014",
        "opt_b": "1953–2014",
        "opt_c": "1956–2014",
        "opt_d": "1947–2014",
        "answer": "C",
        "explanation_te": "ఉమ్మడి ఆంధ్రప్రదేశ్ నవంబర్ 1, 1956 (రాష్ట్రాల పునర్వ్యవస్థీకరణ) నుండి జూన్ 1, 2014 (APRA అమలు) వరకు 58 సంవత్సరాలు ఉంది."
    }
]

MCQ_DATA = MCQ_DATA + _EXTRA_MCQ_DATA_10
