#!/usr/bin/env python3
"""
seed_concept_notes_intl.py
Bilingual (English + Telugu) concept notes for International Current Affairs MCQs.
Topics: International Orgs, Summits, Conflicts, Environment, Science, Sports, Reports, Events, Mideast War
23 concept notes | IDs covered: 20001-30080
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
#  1. INTERNATIONAL ORGANISATIONS — UN & G20
#     IDs: 20001-20016
# ═══════════════════════════════════════════════════════
NOTES.append(('org_un_g20', 'United Nations & G20', 'ఐక్యరాజ్యసమితి & G20', """
<div class="concept-cover">
  <h1>United Nations &amp; G20 &nbsp;<span class="bi-te">/ ఐక్యరాజ్యసమితి &amp; G20</span></h1>
  <div class="sub">Founded 1945 • 193 Members • New York</div>
</div>

<div class="section-hdr">United Nations — Key Facts / ఐక్యరాజ్యసమితి — ముఖ్య వివరాలు</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Founded</td><td>October 24, 1945 (UN Day)</td><td class="bi-te">అక్టోబర్ 24, 1945</td></tr>
<tr><td>HQ</td><td>New York City, USA</td><td class="bi-te">న్యూయార్క్, అమెరికా</td></tr>
<tr><td>Members</td><td>193 member states</td><td class="bi-te">193 సభ్య దేశాలు</td></tr>
<tr><td>Observers</td><td>Vatican (Holy See) + Palestine</td><td class="bi-te">వాటికన్ + పాలస్తీనా (పరిశీలకులు)</td></tr>
<tr><td>SG (9th)</td><td>António Guterres (Portugal) — since Jan 1, 2017; 2nd term through Dec 2026</td><td class="bi-te">అంటోనియో గుటెరస్ — 2017 నుండి; 2వ పదవీకాలం 2026 వరకు</td></tr>
<tr><td>Last joined</td><td>South Sudan (2011)</td><td class="bi-te">చివరగా చేరింది: దక్షిణ సూడాన్ (2011)</td></tr>
</table>

<div class="section-hdr">UN Security Council / భద్రతా మండలి</div>
<table class="key-table">
<tr><th>Type</th><th>Members</th><th>Term</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Permanent (P5)</td><td>USA, UK, France, Russia, China — each has <b>veto power</b></td><td>Permanent</td><td class="bi-te">వీటో అధికారం కలిగిన 5 శాశ్వత సభ్యులు</td></tr>
<tr><td>Non-permanent</td><td>10 elected by UNGA (regional groups)</td><td>2 years</td><td class="bi-te">10 అనిత్య సభ్యులు, UNGA ఎన్నిక</td></tr>
<tr><td>Total UNSC</td><td>15 members</td><td>—</td><td class="bi-te">మొత్తం 15</td></tr>
</table>
<p>UNGA adopted <b>'Pact for the Future'</b> at the Summit of the Future (September 22-23, 2024, New York) — including the Global Digital Compact, aiming to reform global governance.</p>
<p class="bi-te">2024 సెప్టెంబర్‌లో UNGA 'Pact for the Future' ఆమోదించింది — ప్రపంచ పాలనను సంస్కరించేందుకు.</p>

<div class="section-hdr">G20 — 2025 Johannesburg Summit / G20 జోహన్నెస్‌బర్గ్ శిఖరాగ్రం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Summit</td><td>20th G20 — Johannesburg Expo Centre, South Africa</td><td class="bi-te">20వ G20 — జోహన్నెస్‌బర్గ్, దక్షిణాఫ్రికా</td></tr>
<tr><td>Date</td><td>November 22-23, 2025</td><td class="bi-te">నవంబర్ 22-23, 2025</td></tr>
<tr><td>Theme</td><td>'Solidarity, Equality, Sustainability' (Ubuntu philosophy)</td><td class="bi-te">ఉబుంటు తత్వం ఆధారంగా</td></tr>
<tr><td>Historic</td><td>First G20 ever on African continent</td><td class="bi-te">ఆఫ్రికా భూభాగంలో మొదటి G20</td></tr>
<tr><td>Absentee</td><td>USA + Argentina only G20 nations not signing Johannesburg Declaration</td><td class="bi-te">USA + అర్జెంటీనా సంతకం చేయలేదు</td></tr>
<tr><td>Key outcome</td><td>122-point Declaration; UNSC reform demand; Critical Minerals Framework</td><td class="bi-te">UNSC సంస్కరణ డిమాండ్; క్రిటికల్ మినరల్స్ ఫ్రేమ్‌వర్క్్</td></tr>
<tr><td>Next G20</td><td>USA (Miami), 2026</td><td class="bi-te">తదుపరి G20: USA, మయామి 2026</td></tr>
</table>
<p><b>G20 composition:</b> 19 countries + EU + African Union (joined 2023) = 21 effective members. Represents 85% world GDP, 75% global trade.</p>
<p class="bi-te"><b>G20 కూర్పు:</b> 19 దేశాలు + EU + ఆఫ్రికన్ యూనియన్ (2023) = 21 సభ్యులు. ప్రపంచ GDP లో 85%, వాణిజ్యంలో 75% వాటా.</p>
"""))

# ═══════════════════════════════════════════════════════
#  2. INTERNATIONAL ORGANISATIONS — BRICS, G7, NATO
#     IDs: 20017-20039
# ═══════════════════════════════════════════════════════
NOTES.append(('org_brics_g7_nato', 'BRICS, G7 & NATO', 'BRICS, G7 & NATO', """
<div class="concept-cover">
  <h1>BRICS, G7 &amp; NATO &nbsp;<span class="bi-te">/ బ్రిక్స్, G7 &amp; నాటో</span></h1>
  <div class="sub">Key Multilateral Groupings — 2025 Updates</div>
</div>

<div class="section-hdr">BRICS — 2025 Expansion / BRICS విస్తరణ</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full members</td><td><b>11</b> — Original 5 (Brazil, Russia, India, China, S.Africa) + Egypt, Ethiopia, Iran, UAE, Saudi Arabia + <b>Indonesia (Jan 6, 2025)</b></td><td class="bi-te">11 పూర్తి సభ్యులు; ఇండోనేషియా జన. 6, 2025న చేరింది</td></tr>
<tr><td>Indonesia</td><td>First Southeast Asian BRICS member; 11th full member</td><td class="bi-te">మొదటి ఆగ్నేయ ఆసియా BRICS సభ్యుడు</td></tr>
<tr><td>Partner countries (Rio 2025)</td><td>10 new partners: Belarus, Bolivia, Kazakhstan, Cuba, Malaysia, Nigeria, Thailand, Uganda, Uzbekistan, Vietnam</td><td class="bi-te">10 కొత్త భాగస్వామి దేశాలు (రియో 2025)</td></tr>
<tr><td>NDB (BRICS Bank)</td><td>HQ: Shanghai, China — est. 2015</td><td class="bi-te">NDB: షాంఘై, చైనా</td></tr>
<tr><td>GDP share</td><td>~37% of global GDP (PPP) — larger than G7</td><td class="bi-te">PPP లో G7 కంటే పెద్దది</td></tr>
<tr><td>Pakistan</td><td>NOT a BRICS partner — not admitted at Rio 2025</td><td class="bi-te">పాకిస్తాన్ BRICS లో లేదు</td></tr>
<tr><td>2026 Summit</td><td>New Delhi, India (India's BRICS Chairmanship) — Sep 12-13, 2026</td><td class="bi-te">న్యూ ఢిల్లీ, సెప్టెంబర్ 12-13, 2026</td></tr>
</table>
<p>Term 'BRIC' coined by Jim O'Neill (Goldman Sachs) in 2001. South Africa joined 2010 → BRICS. CRA (Contingent Reserve Arrangement) signed 2014, provides short-term liquidity to BRICS members.</p>
<p class="bi-te">'BRIC' అనే పదాన్ని Jim O'Neill (Goldman Sachs) 2001లో రూపొందించాడు. దక్షిణాఫ్రికా 2010లో చేరింది → BRICS.</p>

<div class="section-hdr">G7 — Kananaskis 2025 / G7 — కనాన్‌స్కిస్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>51st G7 Summit</td><td>Kananaskis, Alberta, Canada — June 15-17, 2025</td><td class="bi-te">కెనడా, జూన్ 15-17, 2025</td></tr>
<tr><td>Host PM</td><td>Mark Carney (Canada's new PM since March 2025)</td><td class="bi-te">మార్క్ కార్ని నేతృత్వం</td></tr>
<tr><td>Trump</td><td>Left early after ~12 hours citing Israel-Iran conflict; threatened 35% Canada tariffs</td><td class="bi-te">ట్రంప్ 12 గంటల తర్వాత వెళ్లిపోయాడు</td></tr>
<tr><td>G7 members</td><td>USA, UK, France, Germany, Japan, Canada, Italy (+EU)</td><td class="bi-te">7 అభివృద్ధి చెందిన దేశాలు</td></tr>
<tr><td>Next G7</td><td>France, 2026</td><td class="bi-te">తదుపరి: ఫ్రాన్స్ 2026</td></tr>
</table>
<p>G6 founded 1975 (Rambouillet, France). Canada joined 1976 → G7. Russia suspended from G8 after 2014 Crimea annexation.</p>
<p class="bi-te">G6 స్థాపన 1975. కెనడా 1976లో చేరింది → G7. రష్యాను 2014లో G8 నుండి తొలగించారు.</p>

<div class="section-hdr">NATO — The Hague Summit 2025 / నాటో — హేగ్ శిఖరాగ్రం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Members</td><td><b>32</b> — Sweden became 32nd (March 7, 2024); Finland 31st (April 2023)</td><td class="bi-te">32 సభ్యులు; స్వీడన్ 32వది (2024)</td></tr>
<tr><td>SG</td><td>Mark Rutte (Netherlands) — since October 1, 2024</td><td class="bi-te">మార్క్ రూట్టే — అక్టో. 2024 నుండి</td></tr>
<tr><td>HQ</td><td>Brussels, Belgium (SHAPE in Mons, Belgium)</td><td class="bi-te">బ్రస్సెల్స్, బెల్జియం</td></tr>
<tr><td>Hague Summit</td><td>World Forum, The Hague, Netherlands — June 24-25, 2025</td><td class="bi-te">హేగ్, నెదర్లాండ్స్ — జూన్ 24-25, 2025</td></tr>
<tr><td>5% GDP target</td><td>3.5% core military + 1.5% broader defence sectors; up from 2014's 2% benchmark</td><td class="bi-te">GDP 5% రక్షణ వ్యయం లక్ష్యం</td></tr>
<tr><td>Spain</td><td>Only NATO member that did NOT agree to 5% target</td><td class="bi-te">స్పెయిన్ మాత్రమే అంగీకరించలేదు</td></tr>
<tr><td>Ukraine aid</td><td>€40 billion pledged for 2025; no membership invitation</td><td class="bi-te">ఉక్రెయిన్‌కు €40 బిలియన్ సాయం; సభ్యత్వం లేదు</td></tr>
<tr><td>Article 5</td><td>Collective defence clause — attack on one = attack on all</td><td class="bi-te">సామూహిక రక్షణ నిబంధన</td></tr>
<tr><td>Next summit</td><td>Ankara, Turkey — July 7-8, 2026</td><td class="bi-te">అంకారా, తుర్కియె — జులై 2026</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  3. INTERNATIONAL ORGANISATIONS — QUAD, SCO, ASEAN, IMF, WTO, WHO
#     IDs: 20040-20070
# ═══════════════════════════════════════════════════════
NOTES.append(('org_quad_sco_asean', 'QUAD, SCO, ASEAN & Key Bodies', 'QUAD, SCO, ASEAN & ముఖ్య సంస్థలు', """
<div class="concept-cover">
  <h1>QUAD, SCO, ASEAN &amp; Key Bodies &nbsp;<span class="bi-te">/ ముఖ్య అంతర్జాతీయ సంస్థలు</span></h1>
  <div class="sub">Regional Groupings + Bretton Woods Institutions</div>
</div>

<div class="section-hdr">QUAD & AUKUS</div>
<table class="key-table">
<tr><th>Group</th><th>Members</th><th>Key Fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>QUAD</td><td>USA, India, Japan, Australia</td><td>India hosted QUAD Leaders' Summit 2025 — first on Indian soil; Exercise Malabar = QUAD naval exercise</td><td class="bi-te">2025లో భారత్‌లో మొదటి QUAD శిఖరాగ్రం</td></tr>
<tr><td>AUKUS</td><td>Australia, UK, USA</td><td>Announced Sept 2021; nuclear-powered submarines to Australia; pillar II = AI, quantum, hypersonics</td><td class="bi-te">2021 సెప్టెంబర్‌లో ప్రకటించారు</td></tr>
</table>

<div class="section-hdr">SCO — Shanghai Cooperation Organisation / SCO</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Members</td><td><b>10</b>: China, Russia, Kazakhstan, Kyrgyzstan, Tajikistan, Uzbekistan (2001), India, Pakistan (2017), Iran, Belarus (2024)</td><td class="bi-te">10 పూర్తి సభ్యులు</td></tr>
<tr><td>HQ</td><td>Beijing, China (RATS in Tashkent, Uzbekistan)</td><td class="bi-te">HQ: బీజింగ్; RATS: తాష్కెంట్</td></tr>
<tr><td>Ethos</td><td>'Shanghai Spirit' — mutual trust, equality, non-interference, no military blocs</td><td class="bi-te">శాంఘై స్ఫూర్తి</td></tr>
<tr><td>India joined</td><td>2017 (Astana Summit)</td><td class="bi-te">2017లో భారత్ చేరింది</td></tr>
</table>

<div class="section-hdr">ASEAN</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Founded</td><td>August 8, 1967 — Bangkok Declaration; Founding 5: Thailand, Malaysia, Singapore, Indonesia, Philippines</td><td class="bi-te">ఆగస్ట్ 8, 1967 — బ్యాంకాక్ ప్రకటన</td></tr>
<tr><td>Members</td><td><b>11</b> — Timor-Leste admitted as 11th member at 47th ASEAN Summit, Kuala Lumpur, Oct 26-28, 2025</td><td class="bi-te">11 సభ్యులు; తిమోర్-లెస్టే అక్టో. 2025న చేరింది</td></tr>
<tr><td>2025 Chair</td><td>Malaysia ('Inclusivity and Sustainability')</td><td class="bi-te">2025: మలేషియా అధ్యక్షత</td></tr>
<tr><td>India-ASEAN</td><td>Comprehensive Strategic Partnership (CSP) since Phnom Penh 2022</td><td class="bi-te">2022 నుండి సమగ్ర వ్యూహాత్మక భాగస్వామ్యం</td></tr>
</table>

<div class="section-hdr">IMF, World Bank & WTO</div>
<table class="key-table">
<tr><th>Body</th><th>Head</th><th>HQ</th><th>Key Fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>IMF</td><td>Kristalina Georgieva (Bulgaria) — MD since Oct 2019</td><td>Washington DC</td><td>SDR basket: USD, Euro, CNY, JPY, GBP; India GDP growth ~6.5% (2025-26)</td><td class="bi-te">5 కరెన్సీ SDR బాస్కెట్</td></tr>
<tr><td>World Bank</td><td>Ajay Banga (Indian-American) — since June 2023</td><td>Washington DC</td><td>Replaced 'Ease of Doing Business' with 'Business Ready (B-READY)' report</td><td class="bi-te">అజయ్ బంగా భారతీయ-అమెరికన్</td></tr>
<tr><td>WTO</td><td>Ngozi Okonjo-Iweala (Nigeria) — first African &amp; first woman DG</td><td>Geneva</td><td>Appellate Body non-functional since Dec 2019 (US blocked appointments)</td><td class="bi-te">నైజీరియా నుండి మొదటి DG</td></tr>
<tr><td>WHO</td><td>Dr Tedros Adhanom Ghebreyesus (Ethiopia) — DG since 2017</td><td>Geneva</td><td>USA under Trump (Jan 20, 2025) withdrew from WHO again</td><td class="bi-te">ట్రంప్ WHO నుండి నిష్క్రమించాడు</td></tr>
</table>

<div class="section-hdr">Other Key Organisations</div>
<table class="key-table">
<tr><th>Org</th><th>HQ</th><th>Key Fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>IAEA</td><td>Vienna, Austria</td><td>DG: Rafael Grossi (Argentina) — since Dec 2019</td><td class="bi-te">ఐక్యరాజ్యసమితి అణు నిఘా సంస్థ</td></tr>
<tr><td>UNEP</td><td>Nairobi, Kenya</td><td>Only major UN agency HQ'd in developing country — founded 1972</td><td class="bi-te">అభివృద్ధి చెందుతున్న దేశంలో HQ ఉన్న ఏకైక UN సంస్థ</td></tr>
<tr><td>GAVI</td><td>Geneva, Switzerland</td><td>Vaccine Alliance — founded 2000; won Indira Gandhi Peace Prize 2025</td><td class="bi-te">2025 ఇందిరా గాంధీ శాంతి పురస్కారం</td></tr>
<tr><td>RCEP</td><td>—</td><td>World's largest FTA by GDP — 30% global GDP, 30% population</td><td class="bi-te">ప్రపంచంలోనే అతిపెద్ద FTA</td></tr>
<tr><td>IMEC</td><td>—</td><td>India-Middle East-Europe Economic Corridor — announced G20 New Delhi Sept 2023</td><td class="bi-te">G20 న్యూ ఢిల్లీ 2023లో ప్రకటించారు</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  4. INTERNATIONAL ORGANISATIONS — Environment & Others
#     IDs: 20071-20086
# ═══════════════════════════════════════════════════════
NOTES.append(('org_env_other', 'Environment & Other Organisations', 'పర్యావరణ & ఇతర సంస్థలు', """
<div class="concept-cover">
  <h1>Environment &amp; Other Organisations &nbsp;<span class="bi-te">/ పర్యావరణ &amp; ఇతర సంస్థలు</span></h1>
  <div class="sub">UNOC3 • ISA • FATF • CDRI • INTERPOL • India-UK FTA</div>
</div>

<div class="section-hdr">Environment & Climate Organisations</div>
<table class="key-table">
<tr><th>Org</th><th>HQ / Key Fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>IPCC</td><td>Geneva — assesses climate science, does NOT conduct own research</td><td class="bi-te">వాతావరణ శాస్త్రాన్ని సమీక్షిస్తుంది</td></tr>
<tr><td>UNOC3</td><td>Nice, France — June 2025; co-hosted France &amp; Costa Rica; 'Blue NDC Challenge' launched</td><td class="bi-te">మూడవ UN మహాసముద్ర సదస్సు — Nice 2025</td></tr>
<tr><td>IRENA</td><td>Abu Dhabi, UAE — International Renewable Energy Agency</td><td class="bi-te">అంతర్జాతీయ పునర్వినియోగ ఇంధన సంస్థ</td></tr>
<tr><td>Loss &amp; Damage Fund</td><td>Agreed COP27 (2022), operationalised — for climate-vulnerable developing nations</td><td class="bi-te">COP27లో అంగీకరించారు</td></tr>
</table>

<div class="section-hdr">Other Key Organisations</div>
<table class="key-table">
<tr><th>Org</th><th>HQ</th><th>Key Fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>ISA (Seabed)</td><td>Kingston, Jamaica</td><td>India has 2 polymetallic sulphide exploration contracts — first country with 2</td><td class="bi-te">భారత్ 2 ISA ఒప్పందాలు పొందింది</td></tr>
<tr><td>ISA (Solar)</td><td>Gurugram, India</td><td>International Solar Alliance — launched by Modi at UNGA 2019 with UK</td><td class="bi-te">అంతర్జాతీయ సౌర కూటమి — HQ గురుగ్రామ్</td></tr>
<tr><td>FATF</td><td>Paris, France</td><td>Est. 1989 — combats money laundering, terrorist financing; Pakistan was on grey list</td><td class="bi-te">అంతర్జాతీయ మనీ లాండరింగ్ వ్యతిరేక సంస్థ</td></tr>
<tr><td>CDRI</td><td>New Delhi, India</td><td>Coalition for Disaster Resilient Infrastructure — launched by Modi at UNGA 74th (2019)</td><td class="bi-te">విపత్తు-నిరోధక మౌలిక సదుపాయాల కూటమి</td></tr>
<tr><td>INTERPOL</td><td>Lyon, France</td><td>Est. 1923 — 195 member countries; India's CBI = national bureau for INTERPOL</td><td class="bi-te">అంతర్జాతీయ నేర పోలీసు సంస్థ</td></tr>
<tr><td>OECD</td><td>Paris, France</td><td>Est. 1961 — India applied for membership 2023; accession talks ongoing</td><td class="bi-te">భారత్ 2023లో సభ్యత్వానికి దరఖాస్తు చేసింది</td></tr>
<tr><td>Five Eyes (FVEY)</td><td>—</td><td>Intelligence sharing: USA, UK, Canada, Australia, New Zealand</td><td class="bi-te">5 ఆంగ్ల-భాషా దేశాల నిఘా భాగస్వామ్యం</td></tr>
<tr><td>India-UK FTA</td><td>—</td><td>Signed May 6, 2025 (CETA) — eliminates/reduces tariffs on 99% of Indian goods to UK; bilateral trade $56B, target double by 2030</td><td class="bi-te">భారత్-UK FTA మే 6, 2025 సంతకం</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  5. SUMMITS — G20, G7 & NATO 2025
#     IDs: 21001-21020
# ═══════════════════════════════════════════════════════
NOTES.append(('summit_g20_g7_nato', 'G20, G7 & NATO Summits 2025', 'G20, G7 & NATO శిఖరాగ్రాలు 2025', """
<div class="concept-cover">
  <h1>G20, G7 &amp; NATO Summits 2025 &nbsp;<span class="bi-te">/ G20, G7 &amp; NATO శిఖరాగ్రాలు</span></h1>
  <div class="sub">Johannesburg • Kananaskis • The Hague</div>
</div>

<div class="section-hdr">G20 Johannesburg — Nov 22-23, 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Venue</td><td>Johannesburg Expo Centre, South Africa</td><td class="bi-te">జోహన్నెస్‌బర్గ్, దక్షిణాఫ్రికా</td></tr>
<tr><td>Historic</td><td>First G20 on African soil — South Africa's G20 presidency</td><td class="bi-te">ఆఫ్రికాలో మొదటి G20</td></tr>
<tr><td>Theme</td><td>'Solidarity, Equality, Sustainability' — Ubuntu philosophy ('I am because we are')</td><td class="bi-te">ఉబుంటు తత్వం ఆధారంగా</td></tr>
<tr><td>Declaration</td><td>122-point Johannesburg Declaration — UNSC reform, debt restructuring, fossil fuel transition</td><td class="bi-te">122 అంశాల ప్రకటన</td></tr>
<tr><td>Absentee</td><td>USA + Argentina did not sign; Argentina's FM Quirno called it 'interventionist'</td><td class="bi-te">USA + అర్జెంటీనా సంతకం చేయలేదు</td></tr>
<tr><td>Critical Minerals</td><td>Voluntary Critical Minerals Framework endorsed — tracking labour/environmental standards</td><td class="bi-te">క్రిటికల్ మినరల్స్ ఫ్రేమ్‌వర్క్</td></tr>
<tr><td>Next</td><td>USA (Miami Beach), 2026 — chairmanship handed Jan 12, 2026</td><td class="bi-te">తదుపరి: USA, మయామి 2026</td></tr>
</table>

<div class="section-hdr">G7 Kananaskis — June 15-17, 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>51st G7 Summit</td><td>Kananaskis, Alberta, Canada — remote mountain resort (security)</td><td class="bi-te">51వ G7 — కెనడా</td></tr>
<tr><td>Host</td><td>PM Mark Carney (Liberal Party, Canada's new PM since March 14, 2025)</td><td class="bi-te">PM మార్క్ కార్ని అతిథ్యం</td></tr>
<tr><td>Trump</td><td>Left after ~12 hours — cited Israel-Iran Twelve-Day War; threatened 35% tariffs on Canada</td><td class="bi-te">ట్రంప్ 12 గంటల్లో వెళ్లిపోయాడు</td></tr>
<tr><td>Outcomes</td><td>AI, quantum, critical minerals agreement; $300B frozen Russian assets discussed; China overcapacity criticised</td><td class="bi-te">AI, క్వాంటమ్ ఒప్పందం</td></tr>
<tr><td>Next G7</td><td>France, 2026</td><td class="bi-te">తదుపరి: ఫ్రాన్స్ 2026</td></tr>
</table>

<div class="section-hdr">NATO Hague Summit — June 24-25, 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Venue</td><td>World Forum, The Hague, Netherlands; hosted by PM Dick Schoof</td><td class="bi-te">హేగ్, నెదర్లాండ్స్</td></tr>
<tr><td>SG</td><td>Mark Rutte (Netherlands, former PM 2010-2024) — NATO SG since Oct 1, 2024</td><td class="bi-te">మార్క్ రూట్టే — NATO SG</td></tr>
<tr><td>5% GDP target</td><td><b>3.5%</b> core military + <b>1.5%</b> defence-related = 5% total — up from 2014's 2% benchmark</td><td class="bi-te">GDP 5% రక్షణ వ్యయం లక్ష్యం (2014: 2%)</td></tr>
<tr><td>Spain exception</td><td>Only NATO member refusing 5% target</td><td class="bi-te">స్పెయిన్ మాత్రమే నిరాకరించింది</td></tr>
<tr><td>Ukraine</td><td>€40B aid pledged for 2025; no membership invitation, no timeline</td><td class="bi-te">ఉక్రెయిన్‌కు €40B; సభ్యత్వ ఆహ్వానం లేదు</td></tr>
<tr><td>Next NATO</td><td>Ankara, Turkey — July 7-8, 2026</td><td class="bi-te">తదుపరి: అంకారా, తుర్కియె — జులై 2026</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  6. SUMMITS — BRICS Rio, SCO Tianjin, ASEAN KL 2025
#     IDs: 21021-21040
# ═══════════════════════════════════════════════════════
NOTES.append(('summit_brics_sco_asean', 'BRICS, SCO & ASEAN Summits 2025', 'BRICS, SCO & ASEAN శిఖరాగ్రాలు 2025', """
<div class="concept-cover">
  <h1>BRICS, SCO &amp; ASEAN Summits 2025 &nbsp;<span class="bi-te">/ BRICS, SCO &amp; ASEAN శిఖరాగ్రాలు</span></h1>
  <div class="sub">Rio de Janeiro • Tianjin • Kuala Lumpur</div>
</div>

<div class="section-hdr">17th BRICS Summit — Rio de Janeiro, July 6-7, 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Host</td><td>Brazil (2025 BRICS Chairmanship) — theme: 'Strengthening South-South Cooperation'</td><td class="bi-te">బ్రెజిల్ అధ్యక్షత 2025</td></tr>
<tr><td>Indonesia</td><td>Present as BRICS's 11th full member (joined Jan 6, 2025)</td><td class="bi-te">ఇండోనేషియా 11వ సభ్యుడు</td></tr>
<tr><td>10 new partners</td><td>Belarus, Bolivia, Kazakhstan, Cuba, Malaysia, Nigeria, Thailand, Uganda, Uzbekistan, Vietnam</td><td class="bi-te">10 కొత్త భాగస్వామి దేశాలు</td></tr>
<tr><td>Pakistan</td><td>NOT admitted as BRICS partner at Rio 2025</td><td class="bi-te">పాకిస్తాన్ చేర్చబడలేదు</td></tr>
<tr><td>2026 Summit</td><td>New Delhi, India — Sep 12-13, 2026 (India's BRICS Chairmanship)</td><td class="bi-te">2026 శిఖరాగ్రం: న్యూ ఢిల్లీ</td></tr>
</table>

<div class="section-hdr">25th SCO Summit — Tianjin, China, Aug 31–Sep 1, 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Described as</td><td>Largest SCO summit ever; China held SCO Chairship 2025</td><td class="bi-te">అతిపెద్ద SCO శిఖరాగ్రం</td></tr>
<tr><td>Modi-Xi meeting</td><td>First time Modi met Xi on Chinese soil in 7 years (since Wuhan 2018 informal summit)</td><td class="bi-te">7 సంవత్సరాల తర్వాత చైనాలో మోదీ-Xi సమావేశం</td></tr>
<tr><td>SCO Dev Bank</td><td>New SCO Development Bank established at Tianjin; China pledged $2 billion</td><td class="bi-te">SCO అభివృద్ధి బ్యాంక్ స్థాపన</td></tr>
<tr><td>Pahalgam condemnation</td><td>Tianjin 2025 declaration explicitly condemned Pahalgam terror attack (April 22, 2025)</td><td class="bi-te">పహల్గామ్ దాడిని ఖండించింది</td></tr>
<tr><td>Modi's 3 pillars</td><td>Security (counter-terrorism), Connectivity, Opportunity</td><td class="bi-te">మోదీ 3 స్తంభాలు: భద్రత, కనెక్టివిటీ, అవకాశం</td></tr>
<tr><td>Afghanistan</td><td>Observer status only — NOT a full SCO member</td><td class="bi-te">అఫ్ఘానిస్తాన్: పర్యవేక్షక హోదా మాత్రమే</td></tr>
</table>

<div class="section-hdr">47th ASEAN Summit — Kuala Lumpur, Oct 26-28, 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Chair</td><td>Malaysia (PM Anwar Ibrahim) — theme 'Inclusivity and Sustainability'</td><td class="bi-te">మలేషియా (PM అన్వర్ ఇబ్రహీం)</td></tr>
<tr><td>Timor-Leste</td><td>Formally admitted as ASEAN's <b>11th member</b> — first expansion since Cambodia joined 1999 (26-year gap)</td><td class="bi-te">తిమోర్-లెస్టే 11వ సభ్యుడు — 1999 తర్వాత మొదటి విస్తరణ</td></tr>
<tr><td>KL Peace Accord</td><td>Thailand &amp; Cambodia signed peace accord; Trump &amp; Anwar Ibrahim as witnesses</td><td class="bi-te">థాయ్-కంబోడియా శాంతి ఒప్పందం</td></tr>
<tr><td>ASEAN-China FTA</td><td>FTA 3.0 Upgrade Protocol signed — deepening trade with China</td><td class="bi-te">ASEAN-చైనా FTA 3.0 సంతకం</td></tr>
<tr><td>Next chair</td><td>Philippines — 2026</td><td class="bi-te">తదుపరి: ఫిలిప్పీన్స్ 2026</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  7. SUMMITS — COP Sequence, WEF Davos, APEC 2025-26
#     IDs: 21041-21080
# ═══════════════════════════════════════════════════════
NOTES.append(('summit_cop_davos', 'COP Summits & WEF Davos 2025-26', 'COP శిఖరాగ్రాలు & WEF Davos 2025-26', """
<div class="concept-cover">
  <h1>COP Summits &amp; WEF Davos 2025-26 &nbsp;<span class="bi-te">/ COP శిఖరాగ్రాలు &amp; WEF</span></h1>
  <div class="sub">Baku • Belém • Davos • APEC • WTO</div>
</div>

<div class="section-hdr">COP Sequence — Climate Conferences / COP వాతావరణ సదస్సులు</div>
<table class="key-table">
<tr><th>COP</th><th>Location</th><th>Key Outcome</th><th class="bi-te">ముఖ్య ఫలితం</th></tr>
<tr><td>COP28 (2023)</td><td>Dubai, UAE</td><td>First global stocktake; first language on 'transitioning away from fossil fuels'; Loss &amp; Damage Fund launched</td><td class="bi-te">మొదటి శిలాజ ఇంధన మార్పిడి భాష; Loss &amp; Damage ఫండ్</td></tr>
<tr><td>COP29 (Nov 2024)</td><td>Baku, Azerbaijan</td><td>Baku Climate Unity Pact; developed nations to lead <b>$300 billion/year by 2035</b>; Baku-Belém Roadmap to $1.3T; India called it 'abysmally low'</td><td class="bi-te">అభివృద్ధి చెందిన దేశాలు 2035 నాటికి $300B/సంవత్సరం; భారత్ 'చాలా తక్కువ' అని విమర్శించింది</td></tr>
<tr><td>COP30 (Nov 2025)</td><td>Belém, Brazil</td><td>Belém Package; Baku-Belém Roadmap: <b>$1.3 trillion/year by 2035</b> from ALL actors; Belém Mission to 1.5°C; triple adaptation finance by 2035; Global Climate Finance Accountability Framework</td><td class="bi-te">Baku-Belém Roadmap: 2035 నాటికి $1.3T/సంవత్సరం; అనుకూలన ఫైనాన్స్ 3x పెంపు</td></tr>
<tr><td>COP31 (2026)</td><td>Australia</td><td>Scheduled — next COP</td><td class="bi-te">తదుపరి COP — ఆస్ట్రేలియా 2026</td></tr>
</table>
<p><b>COP</b> = Conference of Parties under UNFCCC (United Nations Framework Convention on Climate Change). Paris Agreement (COP21, 2015): limit warming to well below 2°C, pursue 1.5°C. NDC = Nationally Determined Contribution — each country's emission reduction plan.</p>
<p class="bi-te"><b>COP</b> = UNFCCC సభ్య దేశాల సదస్సు. పారిస్ ఒప్పందం (2015): 2°C కంటే తక్కువ వేడిమి పరిమితి; 1.5°C లక్ష్యం. NDC = జాతీయంగా నిర్ణయించిన విరాళం.</p>

<div class="section-hdr">WEF Davos 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Theme</td><td>'Spirit of Dialogue' — Davos, Switzerland, January 19-23, 2026</td><td class="bi-te">జనవరి 19-23, 2026 — Davos</td></tr>
<tr><td>Key event</td><td>Zelenskyy met Trump at Davos 2026; announced US-Ukraine-Russia trilateral peace talks in Abu Dhabi</td><td class="bi-te">జెలెన్స్కీ-ట్రంప్ సమావేశం; Abu Dhabi శాంతి చర్చలు</td></tr>
<tr><td>WEF HQ</td><td>Cologny, near Geneva, Switzerland</td><td class="bi-te">WEF HQ: స్విట్జర్లాండ్</td></tr>
</table>

<div class="section-hdr">Other Key Summits 2025-26</div>
<table class="key-table">
<tr><th>Summit</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>APEC 2025</td><td>Gyeongju, South Korea</td><td class="bi-te">APEC 2025: గ్యొంగ్జు, దక్షిణ కొరియా</td></tr>
<tr><td>UN Ocean Conf 3 (UNOC3)</td><td>Nice, France — June 2025; France &amp; Costa Rica co-hosted; Blue NDC Challenge; Nairobi UNEP coordinates</td><td class="bi-te">మూడవ UN సముద్ర సదస్సు — Nice 2025</td></tr>
<tr><td>Summit of the Future</td><td>UNGA, New York — Sept 22-23, 2024; adopted 'Pact for the Future'; Global Digital Compact</td><td class="bi-te">భవిష్యత్తు శిఖరాగ్రం — UNGA 2024</td></tr>
<tr><td>WTO MC13</td><td>Abu Dhabi, UAE — Feb 2024; extended e-commerce moratorium; fisheries subsidies</td><td class="bi-te">WTO 13వ మంత్రివర్గ సదస్సు — Abu Dhabi 2024</td></tr>
</table>
"""))

print("Part 1 written — 7 concept notes (Intl Orgs + Summits)")

# ═══════════════════════════════════════════════════════
#  8. CONFLICTS — Operation Sindoor
#     IDs: 22001-22016
# ═══════════════════════════════════════════════════════
NOTES.append(('conflict_sindoor', 'Operation Sindoor 2025', 'ఆపరేషన్ సింధూర్ 2025', """
<div class="concept-cover">
  <h1>Operation Sindoor 2025 &nbsp;<span class="bi-te">/ ఆపరేషన్ సింధూర్ 2025</span></h1>
  <div class="sub">May 7, 2025 • India Strikes 9 Terror Camps in Pakistan/PoK</div>
</div>

<div class="section-hdr">Pahalgam Terror Attack — The Trigger / పహల్గామ్ దాడి</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td>April 22, 2025</td><td class="bi-te">ఏప్రిల్ 22, 2025</td></tr>
<tr><td>Location</td><td>Baisaran Valley, Pahalgam, Anantnag district, J&amp;K</td><td class="bi-te">బైసరన్ లోయ, పహల్గామ్, అనంతనాగ్</td></tr>
<tr><td>Casualties</td><td><b>26 tourists killed</b> — worst terrorist attack in J&amp;K since 2001 Parliament attack</td><td class="bi-te">26 పర్యాటకులు మరణించారు</td></tr>
<tr><td>Perpetrator</td><td>The Resistance Front (TRF) — a proxy of Lashkar-e-Taiba (LeT)</td><td class="bi-te">TRF — LeT ముసుగు సంస్థ</td></tr>
</table>

<div class="section-hdr">Operation Sindoor — India's Strike / ఆపరేషన్ సింధూర్</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td>May 7, 2025</td><td class="bi-te">మే 7, 2025</td></tr>
<tr><td>Duration</td><td>23 minutes — precision strikes</td><td class="bi-te">23 నిమిషాలు — అతి-ఖచ్చితమైన దాడి</td></tr>
<tr><td>Targets</td><td><b>9 terror camps</b> in Pakistan (Punjab province) + PoK — JeM HQ Bahawalpur + LeT HQ Muridke</td><td class="bi-te">9 ఉగ్రవాద శిబిరాలు — బహావల్‌పూర్, ముర్దికే</td></tr>
<tr><td>Target groups</td><td>Jaish-e-Mohammed (JeM) + Lashkar-e-Taiba (LeT) infrastructure — NOT Pakistani military bases</td><td class="bi-te">JeM + LeT మౌలిక సదుపాయాలపై దాడి; పాక్ సైనిక స్థావరాలు లక్ష్యం కాదు</td></tr>
<tr><td>India's objective</td><td>Destroy terror infrastructure; deter future cross-border terrorism</td><td class="bi-te">ఉగ్రవాద మౌలిక సదుపాయాలను నాశనం చేయడం</td></tr>
</table>

<div class="section-hdr">Pakistan's Retaliation & Ceasefire / పాకిస్తాన్ ప్రత్యుత్తరం</div>
<table class="key-table">
<tr><th>Event</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Pakistan operation</td><td>'Operation Bunyan-um-Marsoos' — retaliatory operation, May 10, 2025</td><td class="bi-te">పాక్ ప్రత్యుత్తరం: ఆపరేషన్ బున్యాన్-ఉమ్-మర్సూస్</td></tr>
<tr><td>Ceasefire</td><td>Effective 5:00 PM IST / 4:30 PM PKT on May 10, 2025 (US Secretary Marco Rubio mediated)</td><td class="bi-te">మే 10 సాయంత్రం 5:00 IST కదనవిరమణ; US మధ్యవర్తిత్వం</td></tr>
<tr><td>India's measures</td><td>Suspended Indus Waters Treaty (IWT, 1960); expelled Pakistani diplomats; closed airspace &amp; trade</td><td class="bi-te">సింధు జల ఒప్పందం సస్పెండ్; పాక్ దౌత్యవేత్తలను తిప్పిపంపింది</td></tr>
<tr><td>IWT brokered by</td><td>World Bank (1960) — governs water sharing of 6 Indus rivers between India and Pakistan</td><td class="bi-te">సింధు జల ఒప్పందం 1960 — ప్రపంచ బ్యాంక్ మధ్యవర్తిత్వం</td></tr>
<tr><td>Assessment</td><td>CSS ETH Zürich: India demonstrated air superiority during operation</td><td class="bi-te">CSS ETH Zürich: భారత వాయుదళ ఆధిపత్యం నిరూపితమైంది</td></tr>
</table>
<p><b>SCO Tianjin 2025</b> declaration explicitly condemned the Pahalgam terror attack — significant diplomatic validation for India.</p>
<p class="bi-te"><b>SCO తియాన్జిన్ 2025</b> ప్రకటన పహల్గామ్ దాడిని స్పష్టంగా ఖండించింది — భారత్‌కు దౌత్య మద్దతు.</p>
"""))

# ═══════════════════════════════════════════════════════
#  9. CONFLICTS — Twelve-Day War & Ukraine
#     IDs: 22017-22049
# ═══════════════════════════════════════════════════════
NOTES.append(('conflict_twelve_day', 'Twelve-Day War & Ukraine 2025', 'పన్నెండు రోజుల యుద్ధం & ఉక్రెయిన్ 2025', """
<div class="concept-cover">
  <h1>Twelve-Day War &amp; Ukraine 2025 &nbsp;<span class="bi-te">/ పన్నెండు రోజుల యుద్ధం &amp; ఉక్రెయిన్</span></h1>
  <div class="sub">Israel-Iran June 2025 • Russia-Ukraine</div>
</div>

<div class="section-hdr">Twelve-Day War — June 13-24, 2025 / పన్నెండు రోజుల యుద్ధం</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Duration</td><td>June 13-24, 2025 (12 days)</td><td class="bi-te">జూన్ 13-24, 2025</td></tr>
<tr><td>Israel struck</td><td>Iran's nuclear facilities: <b>Natanz</b> (enrichment), <b>Isfahan</b> (reactor research), <b>Fordow</b> (underground near Qom) + military commanders + 10 nuclear scientists</td><td class="bi-te">నటాంజ్, ఇస్ఫహాన్, ఫోర్డో అణు కేంద్రాలు; 10 శాస్త్రవేత్తలు</td></tr>
<tr><td>IAEA trigger</td><td>June 12, 2025 — IAEA Board declared Iran non-compliant with NPT safeguards (US/EU sponsored); next day Israel attacked</td><td class="bi-te">IAEA జూన్ 12న ఇరాన్‌ను NPT ఉల్లంఘనకారుగా ప్రకటించింది</td></tr>
<tr><td>Iran retaliation</td><td>Operation True Promise III — <b>550+ ballistic missiles + 1,000+ suicide drones</b></td><td class="bi-te">550+ క్షిపణులు + 1,000+ డ్రోన్లు</td></tr>
<tr><td>Iran targeted</td><td>Al Udeid Air Base (Qatar — largest US base), Israeli cities</td><td class="bi-te">Al Udeid Air Base — అతిపెద్ద US మధ్యప్రాచ్య ఆధారం</td></tr>
<tr><td>US role</td><td>Bombed 3 Iranian nuclear sites (Natanz, Isfahan, Fordow) on <b>June 22, 2025</b></td><td class="bi-te">US జూన్ 22న 3 అణు కేంద్రాలు బాంబర్ చేసింది</td></tr>
<tr><td>Casualties killed</td><td>Iran: IRGC chief Hossein Salami + IRGC Aerospace chief Amir Ali Hajizadeh + Armed Forces Chief Mohammad Bagheri; Iran President Pezeshkian wounded</td><td class="bi-te">IRGC అధినేత + Aerospace కమాండర్ + సైన్యాధ్యక్షుడు మరణించారు</td></tr>
<tr><td>Iran arrested</td><td>700+ alleged Mossad agents; executed 5; suspended IAEA cooperation</td><td class="bi-te">700+ మొస్సాద్ ఏజెంట్లను అరెస్టు; IAEA సహకారం నిలిపింది</td></tr>
<tr><td>Ceasefire</td><td>June 24, 2025 — under US pressure</td><td class="bi-te">జూన్ 24, 2025 — US ఒత్తిడిలో కదనవిరమణ</td></tr>
<tr><td>Sequence</td><td>True Promise I (April 13-14, 2024) → True Promise II → True Promise III (Twelve-Day War, June 2025)</td><td class="bi-te">నిజమైన వాగ్దానం I → II → III క్రమం</td></tr>
</table>

<div class="section-hdr">Ukraine-Russia War 2025 / ఉక్రెయిన్-రష్యా యుద్ధం</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Deadliest conflict</td><td>Ukraine = world's deadliest conflict in 2025 — <b>~78,000 fatalities</b> (ACLED data)</td><td class="bi-te">2025లో ప్రపంచంలోనే అత్యంత మారణాత్మక యుద్ధం — 78,000 మరణాలు</td></tr>
<tr><td>Russia invasion</td><td>Full-scale: February 24, 2022 — over 4 years by May 2026</td><td class="bi-te">ఫిబ్రవరి 24, 2022 నుండి</td></tr>
<tr><td>Kursk incursion</td><td>Ukraine's surprise Kursk Oblast incursion (August 2024) — first foreign troops on Russian soil since WWII; N.Korea sent 10,000-12,000 troops to Russia</td><td class="bi-te">ఉక్రెయిన్ కుర్స్క్ ఆక్రమణ; ఉత్తర కొరియా సైనికులు</td></tr>
<tr><td>Ceasefire attempt</td><td>Trump's 3-day Russia-Ukraine ceasefire (May 9-11, 2026) — 1,000 prisoner exchange each side</td><td class="bi-te">ట్రంప్ 3-రోజుల కదనవిరమణ; 1,000 యుద్ధఖైదీల మార్పిడి</td></tr>
<tr><td>Peace talks</td><td>Zelenskyy-Trump met at Davos 2026; US-Ukraine-Russia trilateral talks in Abu Dhabi announced</td><td class="bi-te">Davos 2026లో Zelenskyy-ట్రంప్ సమావేశం</td></tr>
<tr><td>NATO aid</td><td>€40B/year aid; F-16s from Netherlands + Denmark; NO membership invitation</td><td class="bi-te">€40B/సంవత్సరం సాయం; F-16 విమానాలు</td></tr>
</table>

<div class="section-hdr">Gaza & Middle East / గాజా</div>
<p>Gaza ceasefire Phase 1 (January 15, 2025) mediated by <b>Qatar, Egypt, USA</b> — 42-day humanitarian pause with hostage releases. Israel's multi-layer missile defense: Iron Dome (short-range), David's Sling (medium), Arrow (long-range ballistic).</p>
<p class="bi-te">గాజా కదనవిరమణ దశ 1 (జనవరి 15, 2025) — <b>కతార్, ఈజిప్ట్, USA</b> మధ్యవర్తిత్వం. ఇజ్రాయెల్ క్షిపణి రక్షణ: ఐరన్ డోమ్, డేవిడ్'s స్లింగ్, యారో.</p>
"""))

# ═══════════════════════════════════════════════════════
#  10. CONFLICTS — Sudan, Myanmar, Taliban & Global
#      IDs: 22050-22080
# ═══════════════════════════════════════════════════════
NOTES.append(('conflict_global', 'Global Conflicts 2025-26', 'ప్రపంచ సంఘర్షణలు 2025-26', """
<div class="concept-cover">
  <h1>Global Conflicts 2025-26 &nbsp;<span class="bi-te">/ ప్రపంచ సంఘర్షణలు</span></h1>
  <div class="sub">Sudan • Myanmar • Taliban • Houthis • Geopolitics</div>
</div>

<div class="section-hdr">Sudan Civil War / సూడాన్ అంతర్యుద్ధం</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Started</td><td>April 2023 — SAF (Sudanese Armed Forces) vs RSF (Rapid Support Forces)</td><td class="bi-te">ఏప్రిల్ 2023 నుండి — SAF vs RSF</td></tr>
<tr><td>RSF leader</td><td>Mohamed Hamdan Dagalo ('Hemeti')</td><td class="bi-te">RSF నాయకుడు: హెమేటి</td></tr>
<tr><td>Humanitarian</td><td>'World's worst humanitarian crisis' — 10 million+ internally displaced, 2.2 million fled to Chad/Egypt</td><td class="bi-te">ప్రపంచంలోనే అత్యంత తీవ్రమైన మానవతా సంక్షోభం</td></tr>
<tr><td>El Fasher</td><td>Last major SAF-controlled Darfur city — fell to RSF on October 27, 2025</td><td class="bi-te">ఎల్ ఫాషెర్ అక్టోబర్ 27, 2025న RSF స్వాధీనం</td></tr>
<tr><td>Top source</td><td>Sudan = top source of forcibly displaced globally in 2024 (UNHCR)</td><td class="bi-te">2024లో ప్రపంచంలో అత్యంత ఎక్కువ శరణార్థులు</td></tr>
</table>

<div class="section-hdr">Myanmar & Afghanistan / మయన్మార్ & అఫ్ఘానిస్తాన్</div>
<table class="key-table">
<tr><th>Country</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Myanmar</td><td>Civil war since Feb 2021 coup by General Min Aung Hlaing; 90,000+ deaths, 3M+ displaced; ASEAN's Five-Point Consensus (2021) to address crisis</td><td class="bi-te">2021 నుండి అంతర్యుద్ధం; 90,000+ మరణాలు</td></tr>
<tr><td>Afghanistan</td><td>Russia recognized Taliban government on July 3, 2025 — first country to do so officially; Taliban ruling since Aug 2021</td><td class="bi-te">రష్యా జులై 3, 2025న తాలిబాన్ ప్రభుత్వాన్ని గుర్తించింది — మొదటి దేశం</td></tr>
</table>

<div class="section-hdr">Houthis & Key Geopolitical Concepts</div>
<table class="key-table">
<tr><th>Concept</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Houthis</td><td>Ansar Allah — led by Abdul-Malik al-Houthi; attacked Red Sea/Bab el-Mandeb shipping since Oct 2023; US-UK Operation Poseidon Archer targeted Houthi sites</td><td class="bi-te">హూతీలు ఎర్ర సముద్రంలో నౌకలపై దాడులు</td></tr>
<tr><td>IRGC Quds Force</td><td>Iran's external operations — supports Hezbollah (Lebanon), Hamas (Gaza), Houthis (Yemen), PMF (Iraq) — 'Axis of Resistance'</td><td class="bi-te">ఇరాన్ బాహ్య కార్యకలాపాల దళం — ప్రతిఘటన అక్షం</td></tr>
<tr><td>Samson Option</td><td>Israel's undeclared nuclear deterrence — threat of massive retaliation if Israel faces existential threat</td><td class="bi-te">ఇజ్రాయెల్ అణు నిరోధక వ్యూహం</td></tr>
<tr><td>Strait of Hormuz</td><td>Between Iran &amp; Oman — ~20% of global oil + ~20% of global LNG; closed by Iran during 2026 Iran War</td><td class="bi-te">హోర్ముజ్ జలసంధి — 20% ప్రపంచ చమురు; 2026 యుద్ధంలో మూసివేత</td></tr>
<tr><td>New START</td><td>Russia suspended participation Feb 2023 (in response to US Ukraine support)</td><td class="bi-te">రష్యా NEW START నుండి నిష్క్రమించింది (2023)</td></tr>
<tr><td>India's stance</td><td>Neutral in Iran-US-Israel conflict; strategic Chabahar Port interest; EAM Jaishankar engaged both sides</td><td class="bi-te">భారత్ తటస్థ వైఖరి; చాబహార్ పోర్ట్ వ్యూహాత్మక ప్రాముఖ్యత</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  11. ENVIRONMENT — Wildlife & Biodiversity
#      IDs: 25001-25028
# ═══════════════════════════════════════════════════════
NOTES.append(('env_wildlife', 'Wildlife & Biodiversity', 'వన్యప్రాణులు & జీవవైవిధ్యం', """
<div class="concept-cover">
  <h1>Wildlife &amp; Biodiversity &nbsp;<span class="bi-te">/ వన్యప్రాణులు &amp; జీవవైవిధ్యం</span></h1>
  <div class="sub">Tiger Reserves • Ramsar Sites • New Species • IUCN</div>
</div>

<div class="section-hdr">Tiger Reserves in India / భారత పులుల అభయారణ్యాలు</div>
<table class="key-table">
<tr><th>Fact</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total Tiger Reserves</td><td><b>58</b> as of March 2025 — covering ~84,500 sq km; Project Tiger launched 1973; NTCA manages</td><td class="bi-te">58 పులుల అభయారణ్యాలు; ప్రాజెక్ట్ టైగర్ 1973లో ప్రారంభం</td></tr>
<tr><td>Oldest</td><td>Corbett Tiger Reserve, Uttarakhand — est. 1936 as Hailey NP; renamed 1957</td><td class="bi-te">కార్బెట్ — 1936 నుండి, అత్యంత పాతది</td></tr>
<tr><td>Tiger count</td><td>3,682 tigers (2022 AITE) — India holds ~70% of world's wild tigers; MP has most (785)</td><td class="bi-te">3,682 పులులు (2022); MP లో అత్యధికం (785)</td></tr>
<tr><td>MP new reserves</td><td>Ratapani (8th, 2025) + Madhav NP (9th, March 2025) — MP now has most reserves in any state</td><td class="bi-te">రాతాపాని (8వ) + మాధవ NP (9వ) — MP కి అత్యధికం</td></tr>
<tr><td>Pobitora WS</td><td>Assam — est. 1998; 48.81 sq km; highest density of Greater One-Horned Rhinos; Tamulidoba Beel wetland</td><td class="bi-te">పోబితోరా — అసోం; అత్యధిక ఘడియాల సాంద్రత</td></tr>
<tr><td>Shikhna Jwhwlao NP</td><td>Assam — declared 2024, notified Feb 16, 2025; Assam's 3rd national park</td><td class="bi-te">అసోంలో 3వ జాతీయ ఉద్యానవనం</td></tr>
</table>

<div class="section-hdr">New Species Discoveries 2024 / కొత్త జాతులు 2024</div>
<table class="key-table">
<tr><th>Species</th><th>Where Found</th><th>Significance</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Zingiber jagannathii</td><td>Similipal BR, Odisha (Aug 2024)</td><td>New ginger species</td><td class="bi-te">కొత్త అల్లం జాతి — ఒడిశా</td></tr>
<tr><td>Channa nachi</td><td>Meghalaya (Simsang River, Chokpot)</td><td>New snakehead fish</td><td class="bi-te">కొత్త పాము-తల చేప జాతి</td></tr>
<tr><td>3 new frogs</td><td>Kamlang-Namdapha landscape, Arunachal</td><td>Biodiversity hotspot</td><td class="bi-te">అరుణాచల్ ప్రదేశ్‌లో 3 కొత్త కప్ప జాతులు</td></tr>
<tr><td>India 2024 total</td><td>—</td><td>683 new faunal species (459 new to science, 224 new to India) + 433 new floral species; Kerala led with 101 new species</td><td class="bi-te">2024లో 683 కొత్త జంతుజాతులు; కేరళ అగ్రస్థానం (101)</td></tr>
</table>

<div class="section-hdr">IUCN Threatened Species & Ramsar Sites</div>
<table class="key-table">
<tr><th>Topic</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>India threatened spp</td><td>1,174 threatened species — including Great Indian Bustard (CR), Gangetic Dolphin</td><td class="bi-te">1,174 వినాశ ముప్పు జాతులు</td></tr>
<tr><td>Saola</td><td>'Asian Unicorn' — Vietnam-Laos Annamite Mountains; discovered 1992; extremely rare</td><td class="bi-te">ఆసియా యూనికార్న్ — వియత్నాం-లావోస్</td></tr>
<tr><td>Himalayan Musk Deer</td><td>Endangered (IUCN); Schedule I WPA 1972; musk gland makes it poaching target</td><td class="bi-te">హిమాలయ కస్తూరి జింక — IUCN 'ఎండేంజర్డ్'</td></tr>
<tr><td>Ramsar 2024</td><td>New additions: Koonthankulam (Tamil Nadu), Hirekera (Karnataka), others; Ramsar Convention = 1971</td><td class="bi-te">రామ్‌సర్ కన్వెన్షన్ 1971; 2024లో కొత్త తడిభూములు</td></tr>
<tr><td>Ganges Dolphin</td><td>First satellite-tagging: December 18, 2024, Assam — under Project Dolphin (launched 2020); WII led</td><td class="bi-te">మొదటి గంగా డాల్ఫిన్ శాటిలైట్ ట్యాగింగ్ — డిసెంబర్ 2024</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  12. ENVIRONMENT — Climate Change & COP
#      IDs: 25029-25080
# ═══════════════════════════════════════════════════════
NOTES.append(('env_climate_cop', 'Climate Change & COP Outcomes', 'వాతావరణ మార్పు & COP ఫలితాలు', """
<div class="concept-cover">
  <h1>Climate Change &amp; COP Outcomes &nbsp;<span class="bi-te">/ వాతావరణ మార్పు &amp; COP ఫలితాలు</span></h1>
  <div class="sub">Paris Agreement • COP28/29/30 • India's Climate Action</div>
</div>

<div class="section-hdr">COP Framework / COP ఫ్రేమ్‌వర్క్</div>
<table class="key-table">
<tr><th>Term</th><th>Meaning</th><th class="bi-te">వివరణ</th></tr>
<tr><td>UNFCCC</td><td>UN Framework Convention on Climate Change — 1992 Rio Earth Summit</td><td class="bi-te">1992 రియో భూమి సదస్సులో ఆమోదించబడింది</td></tr>
<tr><td>Paris Agreement</td><td>COP21, 2015 — limit warming to well below 2°C, pursue 1.5°C above pre-industrial levels</td><td class="bi-te">2015 పారిస్ ఒప్పందం — 1.5°C లక్ష్యం</td></tr>
<tr><td>NDC</td><td>Nationally Determined Contribution — each country's emission reduction plan under Paris Agreement</td><td class="bi-te">జాతీయంగా నిర్ణయించిన విరాళం</td></tr>
<tr><td>Global stocktake</td><td>First completed at COP28 (Dubai 2023) — assessed collective progress towards Paris goals</td><td class="bi-te">COP28లో మొదటి ప్రగతి సమీక్ష</td></tr>
</table>

<div class="section-hdr">COP28, 29, 30 Key Outcomes</div>
<table class="key-table">
<tr><th>COP</th><th>Year/Place</th><th>Key Outcome</th><th class="bi-te">ముఖ్య ఫలితం</th></tr>
<tr><td>COP28</td><td>2023, Dubai UAE</td><td>First fossil fuel 'transition away' language; Loss &amp; Damage Fund operationalised; first global stocktake</td><td class="bi-te">శిలాజ ఇంధనాల నుండి మళ్ళుట — మొదటిసారి; L&amp;D ఫండ్ ప్రారంభం</td></tr>
<tr><td>COP29</td><td>Nov 2024, Baku Azerbaijan</td><td>Baku Climate Unity Pact; developed countries: <b>$300B/year by 2035</b>; Baku-Belém Roadmap to $1.3T; India called it 'abysmally low'</td><td class="bi-te">$300B/సంవత్సరం; భారత్ విమర్శించింది</td></tr>
<tr><td>COP30</td><td>Nov 2025, Belém Brazil</td><td>Belém Package; $1.3T/year by 2035 from ALL actors; triple adaptation finance by 2035; Belém Mission to 1.5°C; Global Climate Finance Accountability Framework</td><td class="bi-te">అన్ని వర్గాల నుండి $1.3T/సంవత్సరం; అడాప్టేషన్ ఫైనాన్స్ 3x పెంపు</td></tr>
<tr><td>COP31</td><td>2026, Australia</td><td>Next COP — scheduled</td><td class="bi-te">తదుపరి COP — ఆస్ట్రేలియా</td></tr>
</table>

<div class="section-hdr">India's Climate Actions / భారత్ వాతావరణ చర్యలు</div>
<table class="key-table">
<tr><th>Action</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Project Tiger</td><td>Launched 1973; NTCA manages 58 reserves; 2022 count = 3,682 tigers (70% of world's tigers)</td><td class="bi-te">1973లో ప్రారంభం; 58 అభయారణ్యాలు</td></tr>
<tr><td>Project Dolphin</td><td>Launched 2020 — Gangetic &amp; Irrawaddy dolphin conservation; first satellite-tagging Dec 2024</td><td class="bi-te">2020లో ప్రారంభం; 2024లో మొదటి ట్యాగింగ్</td></tr>
<tr><td>CCPI 2025</td><td>India ranked 10th — one of best-performing major economies; published by Germanwatch + CAN</td><td class="bi-te">భారత్ CCPI 2025లో 10వ స్థానం</td></tr>
<tr><td>Social security</td><td>India 2nd globally (ILO) for absolute coverage — 64.3% in 2025 (from 19% in 2015)</td><td class="bi-te">సామాజిక భద్రత కవరేజ్: 19% (2015) → 64.3% (2025)</td></tr>
</table>

<div class="section-hdr">Plastic & Ocean Pollution / ప్లాస్టిక్ & సముద్ర కాలుష్యం</div>
<p>Nurdles = small plastic pellets (1-5mm) used in plastic manufacturing — major ocean pollutant. MSC ELSA 3 (Liberian cargo ship) sank May 25, 2025 — hazardous materials including plastics spilled. Yellow Sea gets its colour from Gobi Desert sand. DPS Flamingo Lake (Maharashtra) declared conservation reserve for flamingos.</p>
<p class="bi-te">నర్డిల్స్ = చిన్న ప్లాస్టిక్ పెల్లెట్లు — సముద్ర కాలుష్యకారులు. పసుపు సముద్రం రంగు గోబీ ఎడారి నుండి వచ్చే ఇసుక వల్ల.</p>
"""))

print("Part 2 appended — Conflicts (3) + Environment (2) = 12 total so far")

# ═══════════════════════════════════════════════════════
#  13. SCIENCE & TECHNOLOGY — ISRO & Space Missions
#      IDs: 26001-26040
# ═══════════════════════════════════════════════════════
NOTES.append(('sci_isro_space', 'ISRO & Space Missions', 'ISRO & అంతరిక్ష యాత్రలు', """
<div class="concept-cover">
  <h1>ISRO &amp; Space Missions &nbsp;<span class="bi-te">/ ISRO &amp; అంతరిక్ష యాత్రలు</span></h1>
  <div class="sub">SpaDeX • Aditya-L1 • Chandrayaan-3 • NASA Missions</div>
</div>

<div class="section-hdr">ISRO Key Missions / ISRO ముఖ్య యాత్రలు</div>
<table class="key-table">
<tr><th>Mission</th><th>Key Facts</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Chandrayaan-3</td><td>Soft landed Moon's South Pole — <b>August 23, 2023</b>; India = 4th country to soft-land (USA, USSR, China); Lander: Vikram; Rover: Pragyan ('wisdom'); <b>National Space Day = Aug 23</b></td><td class="bi-te">ఆగస్టు 23, 2023 — చంద్రుడి దక్షిణ ధ్రువంలో అవతరణ; ఆగస్టు 23 = జాతీయ అంతరిక్ష దినం</td></tr>
<tr><td>Aditya-L1</td><td>India's first solar mission — stationed at Lagrange Point <b>L1</b> (~1.5 million km from Earth); instrument SUIT (Solar Ultraviolet Imaging Telescope) made rare plasma event observation</td><td class="bi-te">L1 లాగ్రాంజ్ పాయింట్‌లో అమర్చబడింది; SUIT సాధనం</td></tr>
<tr><td>SpaDeX</td><td>Space Docking Experiment — 2 satellites (~220 kg each) demonstrate docking/undocking in Low Earth Orbit; technology needed for Gaganyaan &amp; lunar sample return</td><td class="bi-te">అంతరిక్ష డాకింగ్ ప్రయోగం — LEO లో 2 ఉపగ్రహాలు</td></tr>
<tr><td>NISAR</td><td>NASA-ISRO Synthetic Aperture Radar — <b>first joint India-NASA Earth observation mission</b>; launched July 30, 2025 (GSLV-F16); first dual-frequency SAR (L-band + S-band); studies earthquakes, glaciers, forests; observes every part of Earth every 12 days</td><td class="bi-te">NASA-ISRO సంయుక్త భూ పరిశీలన మిషన్; ద్వి-ఆవృత్తి SAR; జులై 30, 2025 ప్రయోగం</td></tr>
<tr><td>PSLV-C61/EOS-09</td><td>Earth Observation Satellite-09 — launched May 18, 2025</td><td class="bi-te">మే 18, 2025 ప్రయోగం</td></tr>
<tr><td>Gaganyaan</td><td>India's human spaceflight mission — India will be <b>4th nation</b> to independently send humans (after USA, Russia/USSR, China); crewed mission (Gaganyaan-4) targeted 2027-28</td><td class="bi-te">గగన్‌యాన్ — భారత్ 4వ దేశంగా మానవులను అంతరిక్షంలో పంపుతుంది</td></tr>
<tr><td>NGLV</td><td>Next Generation Launch Vehicle — LOX-methane engine (reusable booster, like Falcon 9)</td><td class="bi-te">తదుపరి తరం ప్రయోగ వాహనం — పునర్వినియోగ బూస్టర్</td></tr>
<tr><td>LUPEX</td><td>Lunar Polar Exploration Mission — joint ISRO + JAXA (Japan); study water ice at lunar south pole</td><td class="bi-te">ISRO + JAXA సంయుక్త చంద్ర ధ్రువ అన్వేషణ</td></tr>
<tr><td>Chandrayaan-4</td><td>Planned sample-return mission from Moon</td><td class="bi-te">చంద్రుని నమూనా తిరిగి తేవడం</td></tr>
</table>

<div class="section-hdr">NASA Key Missions 2025 / NASA ముఖ్య యాత్రలు</div>
<table class="key-table">
<tr><th>Mission</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>SPHEREx</td><td>Launched <b>March 12, 2025</b> — Vandenberg SFB; studies 450 million galaxies, 100 million stars; creates 3D sky map; orbits at 650 km (SSO)</td><td class="bi-te">మార్చి 12, 2025 ప్రయోగం; 450 మిలియన్ గెలాక్సీలు అధ్యయనం</td></tr>
<tr><td>PUNCH</td><td>Polarimeter to Unify the Corona and Heliosphere — launched <b>March 12, 2025</b> alongside SPHEREx; 4 small spacecraft study solar corona &amp; solar wind</td><td class="bi-te">SPHEREx తో కలిసి ప్రయోగం; సౌర వాతావరణం అధ్యయనం</td></tr>
<tr><td>Europa Clipper</td><td>Heading to Europa (Jupiter's moon); Mars flyby March 2025 for trajectory; Europa has subsurface liquid ocean</td><td class="bi-te">యూరోపా (బృహస్పతి చంద్రుడు) — ద్రవ నీటి సమీపంలో జీవం?</td></tr>
<tr><td>Artemis</td><td>Return humans to Moon; establish lunar settlements; IISc developed brick-making from lunar regolith using Sporosarcina pasteurii bacteria + guar gum</td><td class="bi-te">మళ్ళీ చంద్రుడిపై మానవులు; IISc చంద్ర మట్టి ఇటుకలు</td></tr>
</table>

<div class="section-hdr">Key Concepts / ముఖ్య భావనలు</div>
<table class="key-table">
<tr><th>Term</th><th>Meaning</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Lagrange Point</td><td>Position where gravitational forces of 2 large bodies balance — satellite stays with minimal fuel; L1 (between Earth-Sun), L2 (beyond Earth), L4/L5 (stable)</td><td class="bi-te">2 పెద్ద వస్తువుల గురుత్వాకర్షణ సమతుల్య స్థానం</td></tr>
<tr><td>CME</td><td>Coronal Mass Ejection — massive solar plasma burst; can disrupt satellites, power grids, GPS</td><td class="bi-te">సౌర ప్లాస్మా విస్ఫోటం — ఉపగ్రహాలు, విద్యుత్ గ్రిడ్‌లను దెబ్బతీయవచ్చు</td></tr>
<tr><td>SSO</td><td>Sun-Synchronous Orbit — polar orbit, consistent sun angle; ideal for Earth observation satellites like NISAR</td><td class="bi-te">సూర్య-సమకాలిక కక్ష్య — భూ పరిశీలనకు అనుకూలం</td></tr>
<tr><td>Lunar Regolith</td><td>Loose soil/rock on Moon's surface; IISc used simulants to create bricks for lunar habitats</td><td class="bi-te">చంద్రుని మట్టి — నివాసాల నిర్మాణానికి వాడవచ్చు</td></tr>
<tr><td>ISRO Chairman</td><td>V. Narayanan (current); Ramakrishnan Centre of Excellence at IIT Madras named after former ISRO chief S. Ramakrishnan</td><td class="bi-te">ISRO అధ్యక్షుడు: V. నారాయణన్</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  14. SCIENCE & TECHNOLOGY — AI, Biotech & Other Tech
#      IDs: 26041-26080
# ═══════════════════════════════════════════════════════
NOTES.append(('sci_tech', 'AI, Biotech & Other Science', 'AI, బయోటెక్ & ఇతర విజ్ఞానం', """
<div class="concept-cover">
  <h1>AI, Biotech &amp; Other Science &nbsp;<span class="bi-te">/ AI, బయోటెక్ &amp; ఇతర విజ్ఞానశాస్త్రం</span></h1>
  <div class="sub">ESA Biomass • IIT Innovations • Disease Updates</div>
</div>

<div class="section-hdr">ESA & International Science</div>
<table class="key-table">
<tr><th>Mission/Project</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>ESA Biomass satellite</td><td>7th Earth Explorer satellite under ESA's climate programme; quantifies forest biomass &amp; carbon from space using radar; launched Vega-C rocket, French Guiana</td><td class="bi-te">ESA యొక్క 7వ అర్త్ ఎక్స్‌ప్లోరర్; అడవుల కార్బన్ కొలత</td></tr>
<tr><td>Tianwen-2 (China)</td><td>Dual mission: sample-return from asteroid 2016HO3 (Kamo'oalewa) + explore comet 311P</td><td class="bi-te">చైనా: గ్రహశకలం నుండి నమూనా + తోకచుక్క అన్వేషణ</td></tr>
</table>

<div class="section-hdr">IIT & IISc Innovations / IIT & IISc ఆవిష్కరణలు</div>
<table class="key-table">
<tr><th>Institution</th><th>Innovation</th><th class="bi-te">వివరణ</th></tr>
<tr><td>IIT Madras</td><td>(1) Framework for protecting RC panels from ballistic missiles; (2) India's first <b>cancer genome database</b></td><td class="bi-te">కాన్సర్ జీనోమ్ డేటాబేస్ — భారత్‌లో మొదటిది</td></tr>
<tr><td>IIT Bombay (NCPRE)</td><td>High-efficiency <b>tandem solar cell</b> — higher conversion efficiency than single-layer cells</td><td class="bi-te">హై-ఎఫిషియన్సీ ట్యాండెమ్ సోలార్ సెల్</td></tr>
<tr><td>IISc</td><td>Sporosarcina pasteurii bacteria + guar gum → bricks from lunar/Martian soil simulants; Multiple Sclerosis gut microbiome research (MS patients: more Blautia, Akkermansia; less Bifidobacterium)</td><td class="bi-te">బ్యాక్టీరియా ద్వారా చంద్ర మట్టి ఇటుకలు</td></tr>
<tr><td>IIIT-Delhi</td><td>AMRSense — AI tool analyzing hospital data for early antimicrobial resistance insights</td><td class="bi-te">AMRSense — AMR గుర్తింపు AI సాధనం</td></tr>
</table>

<div class="section-hdr">Disease Updates 2025 / వ్యాధి నవీకరణలు</div>
<table class="key-table">
<tr><th>Disease</th><th>Cause</th><th>Key Fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>African Swine Fever (ASF)</td><td>ASF Virus (DNA virus)</td><td>First in India: Mizoram, Lungsen village, March 21, 2021; kills pigs &amp; wild boars; NOT transmissible to humans</td><td class="bi-te">భారత్‌లో మొదటి ASF: మిజోరాం 2021; మానవులకు వ్యాపించదు</td></tr>
<tr><td>River Blindness (Onchocerciasis)</td><td>Parasitic worm Onchocerca volvulus</td><td>Spreads via blackfly (Simulium genus); ZSI used DNA barcoding to identify blackfly species</td><td class="bi-te">నల్ల ఈగ ద్వారా వ్యాపిస్తుంది; ZSI DNA బార్కోడింగ్</td></tr>
<tr><td>Lumpy Skin Disease</td><td>Capripoxvirus (DNA virus)</td><td>Affects cattle &amp; buffalo; nodular skin lesions; India: outbreaks in Rajasthan, Gujarat</td><td class="bi-te">పశువులను ప్రభావితం చేస్తుంది</td></tr>
<tr><td>Multiple Sclerosis (MS)</td><td>Autoimmune — immune attacks brain &amp; spinal cord</td><td>~1 million in USA, 2.8 million worldwide; gut microbiome role discovered</td><td class="bi-te">మెదడు &amp; వెన్నుపాముపై రోగనిరోధక దాడి</td></tr>
<tr><td>Bird Flu (Avian Influenza)</td><td>Influenza A — H5N1, H5N2</td><td>Zoonotic (can spread to humans); mammalian adaptation concern in 2025</td><td class="bi-te">జూనోటిక్ — జంతువుల నుండి మానవులకు వ్యాపించవచ్చు</td></tr>
<tr><td>Polio (PNG 2025)</td><td>Poliovirus</td><td>Papua New Guinea WHO-declared outbreak 2025; only Afghanistan &amp; Pakistan remain polio-endemic</td><td class="bi-te">PNG 2025 పోలియో ప్రకోపం; అఫ్ఘానిస్తాన్ &amp; పాకిస్తాన్ మాత్రమే ఎండమిక్</td></tr>
</table>

<div class="section-hdr">Japan AI Law 2025</div>
<p>Japan enacted an AI law in May 2025 — flexible, coordination-focused, voluntary responsibility model. Unlike the EU AI Act (risk-based mandatory compliance) — Japan chose a lighter regulatory touch to foster innovation while encouraging industry responsibility.</p>
<p class="bi-te">జపాన్ AI చట్టం మే 2025 — సౌకర్యవంతమైన, స్వచ్ఛంద మోడల్. EU AI Act కంటే తేలికైన నిబంధనలు.</p>
"""))

print("Part 3 appended — Science (2) = 14 total so far")

# ═══════════════════════════════════════════════════════
#  15. SPORTS — Cricket (Champions Trophy, T20 WC, Women's WC)
#      IDs: 27001-27023
# ═══════════════════════════════════════════════════════
NOTES.append(('sports_cricket', 'Cricket — ICC Titles 2025-26', 'క్రికెట్ — ICC టైటిల్స్ 2025-26', """
<div class="concept-cover">
  <h1>Cricket — ICC Titles 2025-26 &nbsp;<span class="bi-te">/ క్రికెట్ — ICC టైటిల్స్</span></h1>
  <div class="sub">Champions Trophy • Women's WC • T20 WC 2026</div>
</div>

<div class="section-hdr">ICC Champions Trophy 2025 (Men) / ICC చాంపియన్స్ ట్రోఫీ 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Host</td><td>Pakistan (PCB hosted); India played in UAE (Dubai) due to political tensions</td><td class="bi-te">PCB నిర్వహించింది; భారత్ UAE లో ఆడింది</td></tr>
<tr><td>Dates</td><td>Feb 19 – March 9, 2025 (15 matches — 3 venues Pakistan + Dubai)</td><td class="bi-te">ఫిబ్రవరి 19 – మార్చి 9, 2025</td></tr>
<tr><td>Final</td><td>India beat New Zealand by <b>4 wickets</b> — March 9, 2025, Dubai International Cricket Stadium</td><td class="bi-te">భారత్ న్యూజిలాండ్‌ను 4 వికెట్లతో ఓడించింది</td></tr>
<tr><td>NZ score</td><td>251/7 in 50 overs</td><td class="bi-te">న్యూజిలాండ్ 251/7</td></tr>
<tr><td>India chase</td><td>254/6 in 49 overs — Rohit Sharma 76 (83b), KL Rahul 34* (unbeaten)</td><td class="bi-te">భారత్ 254/6; రోహిత్ 76, KL రాహుల్ 34*</td></tr>
<tr><td>India's CT wins</td><td>3 times — 2002 (co-winners with Sri Lanka), 2013, 2025 — most successful team</td><td class="bi-te">భారత్ 3 సార్లు చాంపియన్ — అత్యంత విజయవంతమైన జట్టు</td></tr>
<tr><td>Historic</td><td>India won every match without a single defeat — first team in CT history</td><td class="bi-te">భారత్ అన్ని మ్యాచ్‌లు గెలిచింది — CT చరిత్రలో మొదటి జట్టు</td></tr>
<tr><td>Edition</td><td>9th ICC Champions Trophy</td><td class="bi-te">9వ ICC చాంపియన్స్ ట్రోఫీ</td></tr>
</table>

<div class="section-hdr">ICC Women's ODI World Cup 2025</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Host</td><td>India (first time India hosted Women's ODI WC)</td><td class="bi-te">భారత్ మొదటిసారి నిర్వహించింది</td></tr>
<tr><td>Final venue</td><td>Dr. DY Patil Stadium, Navi Mumbai</td><td class="bi-te">నవీ ముంబై</td></tr>
<tr><td>Result</td><td>India beat South Africa by <b>52 runs</b></td><td class="bi-te">భారత్ SA ను 52 పరుగులతో ఓడించింది</td></tr>
<tr><td>India score</td><td>298/7 — Shafali Verma 87, Deepti Sharma key contributor</td><td class="bi-te">భారత్ 298/7; శఫాలీ వర్మ 87</td></tr>
<tr><td>Bowling star</td><td>Deepti Sharma — 5/39 in the final; scored 58 with bat too</td><td class="bi-te">దీప్తి శర్మ 5/39 — ఫైనల్‌లో అద్భుత ప్రదర్శన</td></tr>
<tr><td>SA captain</td><td>Laura Wolvaardt scored 101 — brilliant century in losing cause</td><td class="bi-te">లారా వోల్వార్ట్ 101 చేసినా ఓటమి</td></tr>
<tr><td>India captain</td><td>Harmanpreet Kaur — India's maiden Women's ODI WC title; first Asian women's global title</td><td class="bi-te">హర్మన్‌ప్రీత్ కౌర్ నాయకత్వం; ఆసియా మహిళా జట్టుకు మొదటి ప్రపంచ కప్</td></tr>
</table>

<div class="section-hdr">ICC Men's T20 World Cup 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Host</td><td>India + Sri Lanka co-hosted — Feb 7 – March 8, 2026</td><td class="bi-te">భారత్ + శ్రీలంక సహ-నిర్వహణ</td></tr>
<tr><td>Venues</td><td>8 venues — 5 in India (MA Chidambaram Chennai, Arun Jaitley Delhi, Wankhede Mumbai, Eden Gardens Kolkata, Narendra Modi Ahmedabad) + 3 Sri Lanka</td><td class="bi-te">5 భారత్, 3 శ్రీలంక వేదికలు</td></tr>
<tr><td>Final</td><td>India beat New Zealand by <b>96 runs</b> — March 8, 2026, Narendra Modi Stadium, Ahmedabad</td><td class="bi-te">భారత్ 96 పరుగులతో NZ ను ఓడించింది</td></tr>
<tr><td>India score</td><td>255/5 — highest ever T20 WC final total; Sanju Samson 89 (46b)</td><td class="bi-te">255/5 — T20 WC ఫైనల్‌లో అత్యధిక స్కోర్; సంజు శాంసన్ 89</td></tr>
<tr><td>Bumrah</td><td>Jasprit Bumrah 4/15 — match-winning spell in the final</td><td class="bi-te">బుమ్రా 4/15 — ఫైనల్‌లో మ్యాచ్ నిర్ణయక ప్రదర్శన</td></tr>
<tr><td>India captain</td><td>Rohit Sharma — India's 3rd T20 WC (2007, 2024, 2026) — most by any nation</td><td class="bi-te">రోహిత్ శర్మ; భారత్ 3వ T20 WC — ఏ జాతికైనా అత్యధికం</td></tr>
<tr><td>Format</td><td>20 teams, 4 groups of 5, 55 total matches; top 2 per group to Super 8</td><td class="bi-te">20 జట్లు, 4 గ్రూపులు, 55 మ్యాచ్‌లు</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  16. SPORTS — Chess, Hockey, Tennis, Javelin
#      IDs: 27024-27048
# ═══════════════════════════════════════════════════════
NOTES.append(('sports_chess_tennis', 'Chess, Tennis, Hockey & Athletics', 'చెస్, టెన్నిస్, హాకీ & అథ్లెటిక్స్', """
<div class="concept-cover">
  <h1>Chess, Tennis, Hockey &amp; Athletics &nbsp;<span class="bi-te">/ చెస్, టెన్నిస్, హాకీ &amp; అథ్లెటిక్స్</span></h1>
  <div class="sub">Gukesh • Grand Slams 2025 • Hockey Asia Cup • Neeraj 90m</div>
</div>

<div class="section-hdr">Chess — Gukesh D / చెస్ — గుకేశ్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>World Champion</td><td>D. Gukesh (India) — <b>youngest undisputed World Chess Champion</b> — age 18; December 12, 2024, Singapore</td><td class="bi-te">D. గుకేశ్ — 18 సంవత్సరాల వయసులో ప్రపంచ చాంపియన్</td></tr>
<tr><td>Match result</td><td>Defeated Ding Liren (China) 7.5–6.5 in 14 games</td><td class="bi-te">డింగ్ లిరెన్‌ను 7.5-6.5తో ఓడించాడు</td></tr>
<tr><td>Previous record</td><td>Broke Garry Kasparov's record of youngest world champion (since 1985)</td><td class="bi-te">కాస్పరోవ్ రికార్డు బద్దలు కొట్టాడు (1985 నుండి)</td></tr>
<tr><td>18th Champion</td><td>Gukesh = 18th undisputed World Chess Champion; 2nd Indian after Viswanathan Anand</td><td class="bi-te">18వ ప్రపంచ చాంపియన్; అనంద్ తర్వాత 2వ భారతీయుడు</td></tr>
<tr><td>Women's WC 2025</td><td>Divya Deshmukh (19, Nagpur) won FIDE Women's World Cup 2025 — all-Indian final vs Koneru Humpy; held in Goa</td><td class="bi-te">దివ్యా దేశ్‌ముఖ్ FIDE మహిళా ప్రపంచ కప్ 2025 గెలిచింది — గోవా</td></tr>
</table>

<div class="section-hdr">Tennis Grand Slams 2025</div>
<table class="key-table">
<tr><th>Tournament</th><th>Men's Winner</th><th>Women's Winner</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Australian Open 2025</td><td>Jannik Sinner (Italy) — def. Zverev 6-3, 7-6(4), 6-3</td><td>Madison Keys (USA) — def. Sabalenka</td><td class="bi-te">సిన్నర్ ऑस्ट्रेलियन ओपन 2025</td></tr>
<tr><td>French Open 2025</td><td>Carlos Alcaraz (Spain) — epic 5-set final def. Sinner</td><td>Coco Gauff (USA)</td><td class="bi-te">అల్కారాజ్ ఫ్రెంచ్ ఓపెన్ 2025</td></tr>
<tr><td>Wimbledon 2025</td><td>Jannik Sinner — def. Alcaraz 4-6, 6-4, 6-4, 6-4</td><td>Iga Swiatek (Poland)</td><td class="bi-te">సిన్నర్ వింబుల్డన్ 2025</td></tr>
<tr><td>US Open 2025</td><td>Carlos Alcaraz — def. Sinner 6-2, 3-6, 6-1, 6-4</td><td>Aryna Sabalenka (Belarus)</td><td class="bi-te">అల్కారాజ్ US ఓపెన్ 2025</td></tr>
<tr><td>2025 summary</td><td>Sinner: AO + Wimbledon; Alcaraz: FO + USO — both split 2 each</td><td>Keys: AO; Gauff: FO; Swiatek: W; Sabalenka: USO</td><td class="bi-te">సిన్నర్ + అల్కారాజ్ 2-2 టైటిల్స్ విభజన</td></tr>
</table>

<div class="section-hdr">Hockey & Athletics</div>
<table class="key-table">
<tr><th>Event</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Hockey Asia Cup 2025</td><td>India beat South Korea <b>4-1</b> in final — Rajgir Sports Complex, Bihar; India's <b>4th title</b> (2003, 2007, 2017, 2025); Dilpreet Singh scored 2 goals; qualified for FIH WC 2026</td><td class="bi-te">భారత్ 4-1తో SK ను ఓడించింది — రాజ్‌గిర్, బిహార్; 4వ హాకీ ఆసియా కప్</td></tr>
<tr><td>Neeraj Chopra — 90m</td><td>Doha Diamond League 2025 — threw <b>90.23m</b>; first Indian to cross 90m barrier in javelin; became 25th man in history; reclaimed World No. 1 ranking; training under Jan Železný (Czech, 3x Olympic champion)</td><td class="bi-te">నీరజ్ చోప్రా 90.23m — జావెలిన్‌లో 90m దాటిన మొదటి భారతీయుడు</td></tr>
<tr><td>Neeraj at Paris DL</td><td>Won javelin at Paris Diamond League 2025 too — strong 2025 season; Julian Weber (Germany) beat him at Doha with 91.06m</td><td class="bi-te">పారిస్ డైమండ్ లీగ్‌లో కూడా గెలుపు</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  17. SPORTS — FIFA World Cup, Asian Games, Commonwealth
#      IDs: 27049-27080
# ═══════════════════════════════════════════════════════
NOTES.append(('sports_football_others', 'FIFA WC 2026 & Major Games', 'FIFA WC 2026 & ముఖ్య క్రీడలు', """
<div class="concept-cover">
  <h1>FIFA WC 2026 &amp; Major Games &nbsp;<span class="bi-te">/ FIFA WC 2026 &amp; ముఖ్య క్రీడలు</span></h1>
  <div class="sub">USA-Canada-Mexico • Asian Games • Commonwealth Games</div>
</div>

<div class="section-hdr">FIFA World Cup 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Hosts</td><td>USA + Canada + Mexico — first World Cup with 3 host nations</td><td class="bi-te">USA + కెనడా + మెక్సికో — 3 దేశాల సహ-నిర్వహణ — మొదటిసారి</td></tr>
<tr><td>Teams</td><td><b>48 teams</b> — expanded from 32 (previous WCs 1998-2022)</td><td class="bi-te">48 జట్లు — 32 నుండి పెంపు</td></tr>
<tr><td>Matches</td><td>104 total matches — most in World Cup history (previous: 64 in 2022 Qatar)</td><td class="bi-te">104 మ్యాచ్‌లు — చరిత్రలో అత్యధికం</td></tr>
<tr><td>Group stage</td><td>12 groups of 4 — top 2 advance; then round of 32 (playoffs for 3rd-placed teams)</td><td class="bi-te">12 గ్రూపులు, 4 జట్లు ప్రతి; టాప్-2 అడ్వాన్స్</td></tr>
<tr><td>16 host cities</td><td>11 USA (Atlanta, Boston, Dallas, Houston, Kansas City, LA, Miami, Nashville, NY/NJ, Philadelphia, Seattle) + 3 Canada (Toronto, Vancouver, Guadalajara area) + 2 Mexico (Mexico City, Guadalajara, Monterrey)</td><td class="bi-te">16 నగరాలు — 11 USA, 3 కెనడా, 2 మెక్సికో</td></tr>
<tr><td>Final venue</td><td>MetLife Stadium, East Rutherford, New Jersey (near NYC) — July 19, 2026</td><td class="bi-te">ఫైనల్: MetLife స్టేడియం, NJ — జులై 19, 2026</td></tr>
<tr><td>Opening</td><td>June 11, 2026</td><td class="bi-te">ప్రారంభం: జూన్ 11, 2026</td></tr>
</table>

<div class="section-hdr">FIH Hockey World Cup 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Hosts</td><td>Netherlands + Belgium co-host</td><td class="bi-te">నెదర్లాండ్స్ + బెల్జియం సహ-నిర్వహణ</td></tr>
<tr><td>India qualified</td><td>India qualified by winning Hockey Asia Cup 2025 (Rajgir, Bihar)</td><td class="bi-te">భారత్ హాకీ ఆసియా కప్ 2025 గెలిచి అర్హత పొందింది</td></tr>
</table>

<div class="section-hdr">Asian Games & Commonwealth Games 2026</div>
<table class="key-table">
<tr><th>Event</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>20th Asian Games 2026</td><td>Aichi-Nagoya, Japan — September 19 – October 4, 2026; Japan's first Asian Games since Tokyo 1994</td><td class="bi-te">20వ ఆసియన్ గేమ్స్ — ఐచి-నగోయా, జపాన్; సెప్టెంబర్ 19 – అక్టోబర్ 4, 2026</td></tr>
<tr><td>Commonwealth Games 2026</td><td>Glasgow, Scotland — July 23 – August 2, 2026; Glasgow previously hosted 2014 CWG</td><td class="bi-te">2026 కామన్‌వెల్త్ గేమ్స్ — గ్లాస్గో, స్కాట్లాండ్</td></tr>
</table>

<div class="section-hdr">India's Major Sports Summary 2025-26 / భారత్ ముఖ్య క్రీడా విజయాలు</div>
<table class="key-table">
<tr><th>Achievement</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>CT 2025 (Men)</td><td>Beat NZ by 4 wickets — March 9, Dubai; Rohit captain; unbeaten throughout</td><td class="bi-te">CT 2025: NZ ను 4 వికెట్లతో</td></tr>
<tr><td>Women's ODI WC 2025</td><td>Beat SA by 52 runs — Navi Mumbai; Harmanpreet captain; Deepti Sharma 5/39</td><td class="bi-te">మహిళల ODI WC: SA ను 52 పరుగులతో</td></tr>
<tr><td>T20 WC 2026</td><td>Beat NZ by 96 runs — Ahmedabad; India's 3rd T20 WC; Bumrah 4/15; Samson 89</td><td class="bi-te">T20 WC 2026: NZ ను 96 పరుగులతో</td></tr>
<tr><td>Chess WC 2024</td><td>Gukesh D — youngest champion ever; Singapore</td><td class="bi-te">గుకేశ్ — అత్యంత యువ చెస్ చాంపియన్</td></tr>
<tr><td>Neeraj 90m</td><td>First Indian to cross 90m javelin — Doha DL 2025</td><td class="bi-te">నీరజ్ — 90m దాటిన మొదటి భారతీయుడు</td></tr>
<tr><td>Hockey Asia Cup</td><td>India 4th title — beat SK 4-1, Rajgir Bihar 2025</td><td class="bi-te">హాకీ: 4వ ఆసియా కప్ — రాజ్‌గిర్ 2025</td></tr>
</table>
"""))

print("Part 4 appended — Sports (3) = 17 total so far")

# ═══════════════════════════════════════════════════════
#  18. REPORTS & INDICES — Global Reports
#      IDs: 28001-28044
# ═══════════════════════════════════════════════════════
NOTES.append(('reports_global', 'Global Reports & Rankings', 'ప్రపంచ నివేదికలు & ర్యాంకింగ్‌లు', """
<div class="concept-cover">
  <h1>Global Reports &amp; Rankings &nbsp;<span class="bi-te">/ ప్రపంచ నివేదికలు &amp; ర్యాంకింగ్‌లు</span></h1>
  <div class="sub">Press Freedom • Happiness • Nuclear • Climate • Hunger</div>
</div>

<div class="section-hdr">Press Freedom & Media</div>
<table class="key-table">
<tr><th>Report</th><th>Publisher</th><th>India Rank</th><th>Top Country</th><th class="bi-te">వివరణ</th></tr>
<tr><td>World Press Freedom Index 2025</td><td>RSF (Reporters Without Borders, Paris)</td><td><b>151/180</b></td><td>Finland</td><td class="bi-te">RSF ప్రెస్ స్వాతంత్ర్య సూచిక; భారత్ 151వ స్థానం</td></tr>
<tr><td>US rank</td><td>RSF</td><td>—</td><td>57th (USA)</td><td class="bi-te">USA 57వ స్థానం</td></tr>
</table>
<p>RSF = Reporters Sans Frontières (French) / Reporters Without Borders; HQ: Paris, France. Top 3 (2025): Finland, Estonia, Netherlands.</p>

<div class="section-hdr">Food Security & Humanitarian</div>
<table class="key-table">
<tr><th>Report</th><th>Publisher</th><th>Key Finding</th><th class="bi-te">వివరణ</th></tr>
<tr><td>GRFC 2025</td><td>GNAFC + FSIN (Food Security Information Network)</td><td>295 million people in 53 countries face acute food insecurity</td><td class="bi-te">53 దేశాల్లో 295 మిలియన్ తీవ్ర ఆహార అభద్రత</td></tr>
<tr><td>Global Hunger Index 2024</td><td>Concern Worldwide (Ireland) + Welthungerhilfe (Germany)</td><td>India: <b>105/127</b> — 'Serious' category</td><td class="bi-te">GHI 2024: భారత్ 105వ స్థానం — 'తీవ్రమైన' వర్గం</td></tr>
<tr><td>SOFI Report</td><td>FAO + IFAD + UNICEF + WFP + WHO (jointly)</td><td>State of Food Security and Nutrition in the World</td><td class="bi-te">5 UN సంస్థలు సంయుక్తంగా</td></tr>
<tr><td>UNHCR Global Trends 2024</td><td>UNHCR</td><td>Record <b>123.2 million</b> forcibly displaced globally; children = 40%; Sudan = top source; 73.5M internally displaced</td><td class="bi-te">123.2 మిలియన్ నిర్వాసితులు; సూడాన్ అగ్రస్థానం</td></tr>
</table>

<div class="section-hdr">Climate & Energy Reports</div>
<table class="key-table">
<tr><th>Report</th><th>Publisher</th><th>Key Finding</th><th class="bi-te">వివరణ</th></tr>
<tr><td>CCPI 2025</td><td>Germanwatch + NewClimate Institute + CAN International</td><td>India: <b>10th</b> — top-performing major economy; Denmark = 4th (effective #1, since 1-3 vacant by design); India's renewable energy rated 'Low' despite overall high score</td><td class="bi-te">CCPI 2025: భారత్ 10వ స్థానం; 1-3 స్థానాలు ఖాళీగా ఉంటాయి</td></tr>
<tr><td>World Energy Investment 2025</td><td>IEA (International Energy Agency, Paris)</td><td>Global investment: <b>$3.3 trillion</b>; Clean energy: $2.2T (double fossil fuel $1.1T); China leads clean energy</td><td class="bi-te">$3.3T ఇంధన పెట్టుబడి; శుభ్ర ఇంధనం $2.2T</td></tr>
<tr><td>Carbon Pricing 2025</td><td>World Bank</td><td>80 active carbon pricing instruments globally; cover 28% of global GHG emissions</td><td class="bi-te">80 కార్బన్ ధర మెకానిజమ్స్; ప్రపంచ ఉద్గారాల 28% కవర్</td></tr>
</table>

<div class="section-hdr">SIPRI — Nuclear Warheads 2025</div>
<table class="key-table">
<tr><th>Country</th><th>Warheads (SIPRI 2025)</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Russia</td><td><b>5,459</b> (largest arsenal)</td><td class="bi-te">రష్యా — అత్యధిక అణ్వాయుధాలు</td></tr>
<tr><td>USA</td><td><b>5,177</b></td><td class="bi-te">USA</td></tr>
<tr><td>China</td><td>~500</td><td class="bi-te">చైనా</td></tr>
<tr><td>Pakistan</td><td>~170</td><td class="bi-te">పాకిస్తాన్</td></tr>
<tr><td>India</td><td>~172</td><td class="bi-te">భారత్</td></tr>
<tr><td>Global military spend</td><td>Record <b>~$2.4 trillion</b> in 2024 (SIPRI)</td><td class="bi-te">2024లో ప్రపంచ రక్షణ వ్యయం రికార్డు $2.4T</td></tr>
</table>
<p>SIPRI = Stockholm International Peace Research Institute; HQ: Solna, near Stockholm, Sweden.</p>
<p class="bi-te">SIPRI = స్టాక్‌హోమ్ అంతర్జాతీయ శాంతి పరిశోధన సంస్థ; స్వీడన్.</p>

<div class="section-hdr">Global Peace & Fishing Reports</div>
<table class="key-table">
<tr><th>Report</th><th>Publisher</th><th>Key Finding</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Global Peace Index</td><td>IEP (Institute for Economics and Peace, Sydney)</td><td>Iceland = consistently most peaceful; published annually</td><td class="bi-te">ఐస్‌లాండ్ — అత్యంత శాంతియుతమైన దేశం</td></tr>
<tr><td>Marine Fisheries Review</td><td>FAO</td><td>64.5% stocks fished sustainably; 35.5% overfished</td><td class="bi-te">35.5% సముద్ర చేపలు అతిగా పట్టబడుతున్నాయి</td></tr>
<tr><td>SOFIA (FAO biennial)</td><td>FAO</td><td>State of World Fisheries and Aquaculture — covers global production, trade, consumption</td><td class="bi-te">FAO ద్వైవార్షిక మత్స్య నివేదిక</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  19. REPORTS & INDICES — Economic & Development Indices
#      IDs: 28045-28080
# ═══════════════════════════════════════════════════════
NOTES.append(('reports_economic', 'Development & Economic Indices', 'అభివృద్ధి & ఆర్థిక సూచీలు', """
<div class="concept-cover">
  <h1>Development &amp; Economic Indices &nbsp;<span class="bi-te">/ అభివృద్ధి &amp; ఆర్థిక సూచీలు</span></h1>
  <div class="sub">HDI • SDG • GII • Happiness • CPI • Gender Gap</div>
</div>

<div class="section-hdr">Human Development & SDG</div>
<table class="key-table">
<tr><th>Index</th><th>Publisher</th><th>India Rank/Score</th><th class="bi-te">వివరణ</th></tr>
<tr><td>HDI 2025</td><td>UNDP</td><td>India: <b>134/193</b> — 'Medium Human Development'; measures life expectancy + education + GNI/capita</td><td class="bi-te">HDI 2025: భారత్ 134వ — 'మధ్యస్థ మానవ అభివృద్ధి'</td></tr>
<tr><td>SDG Index 2025</td><td>UN SDSN</td><td>India: <b>99/166</b> — first time in top 100; score improved 57 (2018) → 71 (2025)</td><td class="bi-te">SDG సూచి: భారత్ 99వ — మొదటిసారి టాప్-100</td></tr>
<tr><td>India SDG Index</td><td>NITI Aayog</td><td>Published by NITI Aayog; tracks SDG progress at state level</td><td class="bi-te">NITI Aayog SDG సూచి</td></tr>
</table>

<div class="section-hdr">Happiness & Corruption</div>
<table class="key-table">
<tr><th>Index</th><th>Publisher</th><th>Key Ranking</th><th class="bi-te">వివరణ</th></tr>
<tr><td>World Happiness Report 2025</td><td>UN SDSN</td><td>Finland = <b>8th consecutive year</b> at #1; India = lower ranks</td><td class="bi-te">ఫిన్లాండ్ వరుసగా 8వ సంవత్సరం #1</td></tr>
<tr><td>Corruption Perceptions Index 2024</td><td>Transparency International (Berlin)</td><td>India: <b>93/180</b>; Denmark = #1 (least corrupt, score ~90); scale: 0 (corrupt) to 100 (clean)</td><td class="bi-te">CPI 2024: భారత్ 93వ; డెన్మార్క్ అగ్రస్థానం</td></tr>
</table>

<div class="section-hdr">Innovation & Competitiveness</div>
<table class="key-table">
<tr><th>Index</th><th>Publisher</th><th>India Rank</th><th>Top Country</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Global Innovation Index 2024</td><td>WIPO (Geneva)</td><td><b>39th</b> — dramatic rise from 81st in 2015</td><td>Switzerland</td><td class="bi-te">GII 2024: భారత్ 39వ — 2015లో 81వ</td></tr>
<tr><td>Global Competitiveness</td><td>WEF (Cologny, Geneva)</td><td>—</td><td>—</td><td class="bi-te">WEF ప్రపంచ పోటీతత్వ నివేదిక</td></tr>
<tr><td>Logistics Performance Index</td><td>World Bank</td><td>India: 38th (2023) — improved from 44th (2018)</td><td>—</td><td class="bi-te">LPI 2023: భారత్ 38వ</td></tr>
</table>

<div class="section-hdr">Gender & Social Reports</div>
<table class="key-table">
<tr><th>Index</th><th>Publisher</th><th>India Rank</th><th>Top Country</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Global Gender Gap 2024</td><td>WEF</td><td>India: <b>129/146</b></td><td>Iceland (consistently #1)</td><td class="bi-te">WEF జెండర్ గ్యాప్: భారత్ 129వ; ఐస్‌లాండ్ అగ్రస్థానం</td></tr>
<tr><td>UNFPA SOWP 2025</td><td>UNFPA</td><td>Theme: 'The Real Fertility Crisis' — both very high AND very low fertility pose challenges</td><td>—</td><td class="bi-te">UNFPA: అత్యంత అధిక & అత్యంత తక్కువ జననాల రెండూ సవాళ్లు</td></tr>
<tr><td>India TFR</td><td>NFHS-5</td><td>India TFR = 2.0 (NFHS-5, 2019-21) — below replacement level of 2.1 for first time</td><td>—</td><td class="bi-te">భారత్ TFR 2.0 — మొదటిసారి 2.1 కంటే తక్కువ</td></tr>
</table>

<div class="section-hdr">Health & Education Reports</div>
<table class="key-table">
<tr><th>Report</th><th>Publisher</th><th>Key Finding</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Global TB Report</td><td>WHO</td><td>India = 26% of global TB burden (highest); India target: eliminate TB by 2025 (5 years before SDG 2030)</td><td class="bi-te">భారత్ — 26% ప్రపంచ TB భారం; 2025 నాటికి TB నిర్మూలన లక్ష్యం</td></tr>
<tr><td>UNESCO GEM Report</td><td>UNESCO (Paris)</td><td>272 million children out of school globally</td><td class="bi-te">272 మిలియన్ పిల్లలు పాఠశాలకు వెళ్ళడం లేదు</td></tr>
<tr><td>WESP 2025</td><td>UN DESA</td><td>Global GDP growth: 2.4%; India: 6.3% — fastest major economy</td><td class="bi-te">ప్రపంచ GDP వృద్ధి 2.4%; భారత్ 6.3%</td></tr>
<tr><td>PGI 2.0</td><td>Ministry of Education, India</td><td>73 indicators, 6 domains, 1000 points; Chandigarh topped; Meghalaya at bottom</td><td class="bi-te">PGI 2.0: చండీగఢ్ అగ్రస్థానం; మేఘాలయ చివర</td></tr>
<tr><td>Global Debt</td><td>UNCTAD (Geneva)</td><td>Global public debt reached record $102 trillion</td><td class="bi-te">ప్రపంచ రుణం రికార్డు $102 ట్రిలియన్</td></tr>
<tr><td>Democracy Index</td><td>EIU (Economist Intelligence Unit)</td><td>Published by Economist group's research arm</td><td class="bi-te">EIU ప్రజాస్వామ్య సూచి</td></tr>
</table>
"""))

print("Part 5 appended — Reports (2) = 19 total so far")

# ═══════════════════════════════════════════════════════
#  20. INTL EVENTS — Leadership Changes 2025-26
#      IDs: 29001-29040
# ═══════════════════════════════════════════════════════
NOTES.append(('events_leadership', 'World Leadership Changes 2025-26', 'ప్రపంచ నాయకత్వ మార్పులు 2025-26', """
<div class="concept-cover">
  <h1>World Leadership Changes 2025-26 &nbsp;<span class="bi-te">/ ప్రపంచ నాయకత్వ మార్పులు</span></h1>
  <div class="sub">Japan • USA • Pope • South Korea • Germany • Bangladesh</div>
</div>

<div class="section-hdr">New Leaders 2025-26 / కొత్త నాయకులు</div>
<table class="key-table">
<tr><th>Country/Role</th><th>New Leader</th><th>Date/Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Japan PM</td><td><b>Sanae Takaichi</b> (LDP) — <b>Japan's FIRST EVER female PM</b></td><td>October 21, 2025 — 104th PM; named Japan's first female Finance Minister (Satsuki Katayama)</td><td class="bi-te">సనాయే తకైచి — జపాన్ మొదటి మహిళా PM; అక్టోబర్ 21, 2025</td></tr>
<tr><td>Canada PM</td><td><b>Mark Carney</b> (Liberal Party)</td><td>March 14, 2025; renowned economist, former Bank of Canada &amp; Bank of England governor; Trudeau resigned</td><td class="bi-te">మార్క్ కార్ని — మార్చి 14, 2025; ట్రూడో రాజీనామా తర్వాత</td></tr>
<tr><td>Germany Chancellor</td><td><b>Friedrich Merz</b> (CDU)</td><td>Won federal elections Feb 23, 2025; CDU-CSU coalition victory</td><td class="bi-te">ఫ్రెడరిక్ మెర్జ్ — ఫిబ్రవరి 23, 2025 ఎన్నికలు</td></tr>
<tr><td>USA President (47th)</td><td><b>Donald Trump</b> (Republican) — with <b>JD Vance</b> as VP</td><td>Inaugurated January 20, 2025; withdrew from WHO on Day 1; 35% Canada tariff threats; left G7 early</td><td class="bi-te">ట్రంప్ — జనవరి 20, 2025 ప్రమాణస్వీకారం; JD వాన్స్ VP</td></tr>
<tr><td>South Korea President</td><td><b>Lee Jae-myung</b> (Democratic Party)</td><td>June 3, 2025 snap election win — after Yoon Suk-yeol impeached (declared martial law Dec 3, 2024; Constitutional Court upheld impeachment Apr 4, 2025)</td><td class="bi-te">లీ జే-మయాంగ్ — జూన్ 3, 2025; యూన్ అభిశంసన తర్వాత</td></tr>
<tr><td>Hungary PM</td><td><b>Péter Magyar</b> (Tisza Party)</td><td>April 12, 2026 — defeated Viktor Orbán (PM since 2010, 16 years)</td><td class="bi-te">పేటర్ మాగ్యర్ — ఏప్రిల్ 12, 2026; ఆర్బాన్ 16 సంవత్సరాల తర్వాత ఓటమి</td></tr>
<tr><td>Nepal PM</td><td><b>Balendra Shah</b></td><td>March 27, 2026 — Gen Z protests (Sept 2025) toppled KP Sharma Oli</td><td class="bi-te">నేపాల్ PM: బాలేంద్ర షా — మార్చి 27, 2026</td></tr>
<tr><td>Bangladesh CA</td><td><b>Muhammad Yunus</b></td><td>Nobel Peace 2006 (Grameen Bank microfinance); Chief Advisor heading interim govt after student protests toppled Hasina</td><td class="bi-te">మహమ్మద్ యూనస్ — నోబెల్ 2006 గ్రహీత; అంతర్వర్తి ప్రభుత్వం</td></tr>
<tr><td>Syria</td><td><b>Ahmed al-Sharaa</b> (Abu Mohammad al-Jolani)</td><td>HTS leader — head of transitional govt after Bashar al-Assad fell</td><td class="bi-te">అహ్మద్ అల్-శరా — అసద్ తర్వాత సిరియా పరివర్తన ప్రభుత్వం</td></tr>
</table>

<div class="section-hdr">Pope — Historic Change / పోప్ మార్పు</div>
<table class="key-table">
<tr><th>Event</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Pope Francis died</td><td>April 21, 2025 — age 88; born Jorge Mario Bergoglio (Buenos Aires, Argentina, Dec 17, 1936); first Pope from Latin America; first Jesuit Pope; served 2013-2025</td><td class="bi-te">పోప్ ఫ్రాన్సిస్ ఏప్రిల్ 21, 2025 మరణించారు; వయసు 88; లాటిన్ అమెరికా నుండి మొదటి పోప్</td></tr>
<tr><td>Pope Leo XIV elected</td><td>May 8, 2025 — <b>Robert Prevost</b> (Chicago, Illinois, USA) — <b>FIRST AMERICAN POPE</b> in history; first Pope from Order of Saint Augustine; former missionary in Peru; Lima archdiocese before election</td><td class="bi-te">పోప్ లియో XIV — రాబర్ట్ ప్రేవోస్ట్; మొదటి అమెరికన్ పోప్; మే 8, 2025</td></tr>
</table>

<div class="section-hdr">Nobel Prize 2025 Winners / నోబెల్ 2025</div>
<table class="key-table">
<tr><th>Category</th><th>Winner</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Peace</td><td>María Corina Machado (Venezuela) — democratic rights activist</td><td class="bi-te">వెనెజుయెలా ప్రజాస్వామ్య హక్కుల ఉద్యమకారుడు</td></tr>
<tr><td>Literature</td><td>László Krasznahorkai (Hungary) — Hungary's first Nobel in Literature</td><td class="bi-te">హంగేరీ మొదటి సాహిత్య నోబెల్</td></tr>
<tr><td>Medicine</td><td>Mary Brunkow, Fred Ramsdell, Shimon Sakaguchi — peripheral immune tolerance</td><td class="bi-te">రోగనిరోధక సహనంపై పరిశోధన</td></tr>
<tr><td>Physics</td><td>John Clarke, Michel Devoret, John Martinis — macroscopic quantum tunneling</td><td class="bi-te">క్వాంటమ్ టన్నెలింగ్ ఆవిష్కరణ</td></tr>
<tr><td>Chemistry</td><td>Susumu Kitagawa, Richard Robson, Omar Yaghi — metal-organic frameworks (MOFs)</td><td class="bi-te">మెటల్-ఆర్గానిక్ ఫ్రేమ్‌వర్క్‌లు</td></tr>
<tr><td>Economics</td><td>Joel Mokyr, Philippe Aghion, Peter Howitt — innovation &amp; long-term economic growth</td><td class="bi-te">ఆవిష్కరణ & దీర్ఘకాలిక ఆర్థిక వృద్ధి</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  21. INTL EVENTS — Global Developments & India's Role
#      IDs: 29041-29080
# ═══════════════════════════════════════════════════════
NOTES.append(('events_global', 'Global Events & India Diplomacy 2025-26', 'ప్రపంచ సంఘటనలు & భారత దౌత్యం 2025-26', """
<div class="concept-cover">
  <h1>Global Events &amp; India Diplomacy 2025-26 &nbsp;<span class="bi-te">/ ప్రపంచ సంఘటనలు &amp; భారత దౌత్యం</span></h1>
  <div class="sub">India-UK CETA • ASEAN Expansion • Arts & Culture • WTO • Delhi Largest City</div>
</div>

<div class="section-hdr">India's Key International Events / భారత్ ముఖ్య అంతర్జాతీయ సంఘటనలు</div>
<table class="key-table">
<tr><th>Event</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>India-UK CETA</td><td>Signed <b>July 24, 2025</b> (Comprehensive Economic and Trade Agreement); eliminates tariffs on 99% India goods to UK; bilateral trade $56B; target double by 2030; UK PM: Keir Starmer (Labour, since July 2024)</td><td class="bi-te">భారత్-UK CETA జులై 24, 2025 సంతకం; 99% భారత వస్తువులపై సుంకాలు రద్దు</td></tr>
<tr><td>ISA double contracts</td><td>India secured 2 polymetallic sulphide exploration contracts from ISA — first country with 2 contracts</td><td class="bi-te">భారత్ ISA నుండి 2 ఖనిజ అన్వేషణ ఒప్పందాలు</td></tr>
<tr><td>BHISHM to Maldives</td><td>India gifted BHISHM (Bike-mounted Hospital System) to Maldives on 60th Independence Day — 'Neighbourhood First'</td><td class="bi-te">BHISHM — మాలదీవులకు భారత్ బహుమతి</td></tr>
<tr><td>India-UAE MoU (May 2026)</td><td>Cooperation in strategic petroleum reserves + increased LPG imports — energy security partnership</td><td class="bi-te">భారత్-UAE పెట్రోలియం నిల్వల ఒప్పందం మే 2026</td></tr>
<tr><td>Kailash Mansarovar Yatra</td><td>Suspended since 2020 (COVID + Galwan Valley clash June 2020); DGEMR working on route via Lipulekh Pass; resumed after India-China LAC disengagement (Oct 2024 — Depsang + Demchok resolved)</td><td class="bi-te">కైలాస మానసరోవర్ యాత్ర 2020 నుండి నిలిపివేత; LAC నిష్క్రమణ తర్వాత ప్రయత్నాలు</td></tr>
<tr><td>Operation Sagar Bandhu</td><td>India's operation to assist Sri Lanka during Cyclone Ditwah (November 27, 2025)</td><td class="bi-te">ఆపరేషన్ సాగర్ బంధు — శ్రీలంక సైక్లోన్ సాయం</td></tr>
</table>

<div class="section-hdr">World Events 2025-26</div>
<table class="key-table">
<tr><th>Event</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>ASEAN 11th member</td><td>Timor-Leste admitted Oct 2025 — first expansion since Cambodia joined 1999 (26-year gap)</td><td class="bi-te">తిమోర్-లెస్టే ASEAN 11వ సభ్యుడు — 1999 తర్వాత మొదటి విస్తరణ</td></tr>
<tr><td>Russia recognizes Taliban</td><td>July 3, 2025 — first country to officially recognize Taliban government of Afghanistan</td><td class="bi-te">రష్యా జులై 3, 2025న తాలిబాన్‌ను గుర్తించింది</td></tr>
<tr><td>Delhi largest city</td><td>Delhi (NCR) ranked world's most populous urban area in 2025 by UN Habitat — surpassing Tokyo</td><td class="bi-te">ఢిల్లీ — 2025లో ప్రపంచంలోనే అత్యంత జనసాంద్ర నగరం; టోక్యో చేర్ చేసింది</td></tr>
<tr><td>Jakarta sinking</td><td>Sinking 1-25 cm/year (groundwater extraction); Indonesia moving capital to Nusantara (Borneo island)</td><td class="bi-te">జకార్తా 1-25 cm/సంవత్సరం మునిగిపోతోంది; రాజధాని నుసంతారకు మారుతోంది</td></tr>
<tr><td>CBAM (EU)</td><td>Carbon Border Adjustment Mechanism — full enforcement 2026; 'Fit for 55' package; 55% GHG reduction target</td><td class="bi-te">EU CBAM పూర్తి అమలు 2026 నుండి</td></tr>
<tr><td>PNG Polio 2025</td><td>Papua New Guinea WHO-declared polio outbreak; only Afghanistan + Pakistan remain polio-endemic otherwise</td><td class="bi-te">PNG పోలియో ప్రకోపం 2025</td></tr>
<tr><td>Hawaii Green Fee</td><td>First US state to implement a tourist 'Green Fee' per night — funds conservation</td><td class="bi-te">హవాయి — పర్యాటకుల నుండి 'గ్రీన్ ఫీ' వసూలు</td></tr>
</table>

<div class="section-hdr">Arts, Literature & Other Prizes 2025</div>
<table class="key-table">
<tr><th>Award</th><th>Winner 2025</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Booker Prize</td><td>Banu Mushtaq (Bengaluru) — 'Heart Lamp' (translated by Deepa Bhasthi from Kannada) — first Kannada work to win Booker</td><td class="bi-te">బానూ ముష్తాక్ — 'హార్ట్ లాంప్' (కన్నడ నుండి); మొదటి కన్నడ బుకర్ విజేత</td></tr>
<tr><td>Ballon d'Or Men 2025</td><td>Ousmane Dembélé (France, PSG) — beat Lamine Yamal</td><td class="bi-te">ఓస్మాన్ డెంబేలే (PSG) — Ballon d'Or 2025</td></tr>
<tr><td>Grammy 2025 (67th)</td><td>Kendrick Lamar's 'Not Like Us' — Record of the Year + Song of the Year</td><td class="bi-te">67వ గ్రామీ 2025 — కెండ్రిక్ లామర్</td></tr>
<tr><td>Oscars 97th (2025)</td><td>'Anora' (dir. Sean Baker) — Best Picture, Director, Actress (Mikey Madison), Screenplay; Adrien Brody — Best Actor</td><td class="bi-te">97వ ఆస్కార్ 2025 — 'అనోరా'; అడ్రియన్ బ్రోడీ — బెస్ట్ ఆక్టర్</td></tr>
<tr><td>WTO DG</td><td>Ngozi Okonjo-Iweala (Nigeria) — first African + first woman WTO DG; re-appointed; HQ Geneva</td><td class="bi-te">నోగ్జి ఒకోంజో-ఇవెలా — మొదటి ఆఫ్రికన్ + మొదటి మహిళా WTO DG</td></tr>
<tr><td>CPTPP Chair 2025</td><td>Japan chairs CPTPP 2025; 11 members; UK joined 2024</td><td class="bi-te">CPTPP 2025 అధ్యక్షత: జపాన్</td></tr>
</table>
"""))

print("Part 6 appended — Intl Events (2) = 21 total so far")

# ═══════════════════════════════════════════════════════
#  22. MIDEAST WAR — Twelve-Day War June 2025
#      IDs: 30001-30020
# ═══════════════════════════════════════════════════════
NOTES.append(('mideast_twelve_day', 'Twelve-Day War — June 2025', 'పన్నెండు రోజుల యుద్ధం — జూన్ 2025', """
<div class="concept-cover">
  <h1>Twelve-Day War — June 13-24, 2025 &nbsp;<span class="bi-te">/ పన్నెండు రోజుల యుద్ధం</span></h1>
  <div class="sub">Israel-Iran • Nuclear Sites • IAEA • True Promise III</div>
</div>

<div class="section-hdr">Background / నేపథ్యం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>True Promise sequence</td><td>Iran's direct attacks on Israel: <b>True Promise I</b> (April 13-14, 2024) → <b>True Promise II</b> → <b>True Promise III</b> (Twelve-Day War retaliation, June 2025)</td><td class="bi-te">నిజమైన వాగ్దానం I (ఏప్రిల్ 2024) → II → III (జూన్ 2025)</td></tr>
<tr><td>IAEA trigger</td><td>June 12, 2025 — IAEA Board of Governors declared Iran non-compliant with NPT safeguards (US/EU sponsored resolution); Iran enriched uranium to 60% (near weapons-grade: 90%+)</td><td class="bi-te">IAEA జూన్ 12న ఇరాన్ NPT ఉల్లంఘనగా ప్రకటించింది; ఇరాన్ 60% శుద్ధి చేసింది</td></tr>
<tr><td>JCPOA history</td><td>Iran nuclear deal (2015, P5+1 + EU + Iran); Trump withdrew USA 2018 ('maximum pressure'); Biden re-engagement failed; deal effectively dead by 2025</td><td class="bi-te">JCPOA 2015 ఇరాన్ అణు ఒప్పందం; ట్రంప్ 2018లో నిష్క్రమించాడు</td></tr>
</table>

<div class="section-hdr">The Twelve-Day War — Events / సంఘటనలు</div>
<table class="key-table">
<tr><th>Date</th><th>Event</th><th class="bi-te">వివరణ</th></tr>
<tr><td>June 13, 2025</td><td>Israel launches surprise attack on Iran's nuclear facilities: <b>Natanz</b> (main enrichment, Isfahan Province), <b>Isfahan</b> (reactor research), <b>Fordow</b> (underground, near Qom — extremely hardened); also targeted military commanders &amp; 10 nuclear scientists</td><td class="bi-te">ఇజ్రాయెల్ నటాంజ్, ఇస్ఫహాన్, ఫోర్డో అణు కేంద్రాలపై దాడి</td></tr>
<tr><td>Israel also destroyed</td><td>5 F-14 Tomcat jets, 2 F-5 Tiger jets, 8 AH-1 Cobra helicopters (Iranian air force)</td><td class="bi-te">ఇరాన్ యుద్ధ విమానాలు నాశనం</td></tr>
<tr><td>Iran retaliation</td><td>Operation True Promise III — 550+ ballistic missiles + 1,000+ suicide drones; struck Al Udeid Air Base (Qatar — US's largest ME base); targeted Israeli cities</td><td class="bi-te">550+ క్షిపణులు + 1,000+ డ్రోన్లు; Al Udeid Air Base లక్ష్యం</td></tr>
<tr><td>Iran commanders killed</td><td>Hossein Salami (IRGC CinC) + Amir Ali Hajizadeh (IRGC Aerospace Force chief — missile/drone programme) + Mohammad Bagheri (Armed Forces Chief of Staff)</td><td class="bi-te">3 అగ్ర IRGC/సైనిక కమాండర్లు మరణించారు</td></tr>
<tr><td>Iran President</td><td>Masoud Pezeshkian — wounded in action (WIA); had been elected July 2024</td><td class="bi-te">ఇరాన్ అధ్యక్షుడు పెజెష్కియాన్ గాయపడ్డారు</td></tr>
<tr><td>June 22, 2025</td><td>USA bombed 3 Iranian nuclear sites (Natanz, Isfahan, Fordow) — most direct US military action against Iran ever; US was simultaneously combatant &amp; ceasefire broker</td><td class="bi-te">USA జూన్ 22న 3 ఇరాన్ అణు కేంద్రాలు బాంబర్ చేసింది</td></tr>
<tr><td>Iran's response to US</td><td>700+ alleged Mossad agents arrested; 5 executed; internet blackouts imposed; IAEA cooperation suspended</td><td class="bi-te">700+ మొస్సాద్ ఏజెంట్లు అరెస్ట్; IAEA సహకారం నిలిపింది</td></tr>
<tr><td>Israel casualties</td><td>32 civilians + 1 off-duty soldier killed; 3,238 wounded</td><td class="bi-te">ఇజ్రాయెల్: 33 మరణాలు, 3,238 గాయపడ్డారు</td></tr>
<tr><td>Ceasefire</td><td>June 24, 2025 — under US pressure; US played dual role (combatant + ceasefire broker)</td><td class="bi-te">జూన్ 24, 2025 కదనవిరమణ — US ఒత్తిడి</td></tr>
</table>

<div class="section-hdr">Key Locations / ముఖ్య స్థానాలు</div>
<table class="key-table">
<tr><th>Location</th><th>Significance</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Natanz</td><td>Iran's main uranium enrichment facility — Isfahan Province, ~250 km south of Tehran</td><td class="bi-te">ఇరాన్ ప్రధాన యురేనియం శుద్ధి కేంద్రం</td></tr>
<tr><td>Fordow</td><td>Underground enrichment plant inside a mountain near Qom — extremely hardened (designed to survive airstrikes)</td><td class="bi-te">పర్వతం లోపల భూగర్భ కేంద్రం — బాంబు దాడులను తట్టుకోవడానికి రూపొందించబడింది</td></tr>
<tr><td>Al Udeid AB</td><td>Qatar — US's largest Middle East air base — ~10,000 US personnel; USAF Central Air Forces HQ</td><td class="bi-te">Al Udeid — US అతిపెద్ద మధ్యప్రాచ్య వాయుదళ స్థావరం</td></tr>
<tr><td>IAEA HQ</td><td>Vienna, Austria — DG Rafael Grossi (Argentina)</td><td class="bi-te">IAEA HQ: వియన్నా, ఆస్ట్రియా</td></tr>
</table>
"""))

# ═══════════════════════════════════════════════════════
#  23. MIDEAST WAR — 2026 Iran War
#      IDs: 30021-30080
# ═══════════════════════════════════════════════════════
NOTES.append(('mideast_2026_war', '2026 Iran War', '2026 ఇరాన్ యుద్ధం', """
<div class="concept-cover">
  <h1>2026 Iran War &nbsp;<span class="bi-te">/ 2026 ఇరాన్ యుద్ధం</span></h1>
  <div class="sub">February 28, 2026 — US-Israel Attack • Strait of Hormuz Crisis</div>
</div>

<div class="section-hdr">How It Started / ఎలా ప్రారంభమైంది</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Date</td><td>February 28, 2026 — US + Israel launched coordinated strikes on Iran</td><td class="bi-te">ఫిబ్రవరి 28, 2026 — USA + ఇజ్రాయెల్ సమన్వయ దాడులు</td></tr>
<tr><td>Timing paradox</td><td>Attacks launched DURING active US-Iran nuclear negotiations — made timing highly controversial</td><td class="bi-te">US-ఇరాన్ అణు చర్చలు జరుగుతుండగా దాడి — వివాదాస్పదం</td></tr>
<tr><td>Iran Supreme Leader killed</td><td><b>Ali Khamenei</b> — Iran's Supreme Leader since 1989 (succeeded Ayatollah Khomeini, founder of Islamic Republic) — killed in opening strikes</td><td class="bi-te">అలీ ఖమేని — 1989 నుండి సుప్రీమ్ లీడర్ — మరణించారు</td></tr>
<tr><td>Also killed</td><td>Ali Larijani — former Speaker of Iran's parliament, highly influential politician</td><td class="bi-te">అలీ లారిజాని — ఇరాన్ పార్లమెంట్ మాజీ స్పీకర్ — మరణించాడు</td></tr>
<tr><td>Naim Qassem</td><td>Hezbollah's Secretary-General (succeeded Nasrallah killed by Israel Sept 2024) — killed May 7, 2026</td><td class="bi-te">నయీమ్ కాసిమ్ — హెజ్బుల్లా నాయకుడు — మే 7, 2026 మరణించాడు</td></tr>
</table>

<div class="section-hdr">Strait of Hormuz Crisis / హోర్ముజ్ జలసంధి సంక్షోభం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Iran closed Hormuz</td><td>Iran closed the Strait of Hormuz — between <b>Iran (north) and Oman (south)</b>; ~20% of global oil + ~20% of global LNG passes through</td><td class="bi-te">ఇరాన్ హోర్ముజ్ జలసంధిని మూసివేసింది — 20% ప్రపంచ చమురు</td></tr>
<tr><td>Oil price spike</td><td>Global oil prices spiked dramatically; LNG (Qatar's exports) severely impacted</td><td class="bi-te">ప్రపంచ చమురు ధరలు పెద్దగా పెరిగాయి</td></tr>
<tr><td>US deployment</td><td>2 aircraft carrier strike groups — largest US Middle East military buildup since 2003 Iraq War</td><td class="bi-te">2 US విమానవాహక నౌకా దళాలు — 2003 ఇరాక్ తర్వాత అతిపెద్ద మోహరింపు</td></tr>
</table>

<div class="section-hdr">Iran Strikes US Bases / ఇరాన్ US స్థావరాలపై దాడులు</div>
<table class="key-table">
<tr><th>Country</th><th>US Base Targeted</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Bahrain</td><td>NSA Bahrain / US 5th Fleet HQ</td><td class="bi-te">బహ్రెయిన్ — 5వ ఫ్లీట్ HQ</td></tr>
<tr><td>Jordan</td><td>Al-Tanf area</td><td class="bi-te">జోర్డాన్ — అల్-తాన్ఫ్</td></tr>
<tr><td>Kuwait</td><td>Camp Arifjan</td><td class="bi-te">కువైట్</td></tr>
<tr><td>Qatar</td><td>Al Udeid Air Base (largest US base)</td><td class="bi-te">కతార్ — Al Udeid</td></tr>
<tr><td>Saudi Arabia</td><td>Various facilities</td><td class="bi-te">సౌదీ అరేబియా</td></tr>
<tr><td>UAE</td><td>Various facilities</td><td class="bi-te">UAE</td></tr>
<tr><td>UK (Cyprus)</td><td>Britain's Akrotiri military base on Cyprus struck by Iranian drone</td><td class="bi-te">సైప్రస్‌లో UK Akrotiri స్థావరం</td></tr>
<tr><td>Turkey</td><td>Iranian ballistic missiles intercepted over Turkey (NATO member cooperated)</td><td class="bi-te">తుర్కియె పైన ఇరాన్ క్షిపణులు అడ్డుకోబడ్డాయి</td></tr>
</table>

<div class="section-hdr">Casualties & Ceasefire</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>US casualties</td><td>15 soldiers killed, 538 wounded (as of April 30, 2026)</td><td class="bi-te">USA: 15 మరణాలు, 538 గాయపడ్డారు</td></tr>
<tr><td>Lebanon War</td><td>Concurrent 2026 Lebanon War — 1,000-1,900 Hezbollah fighters killed, 2,000+ total</td><td class="bi-te">లెబనాన్ యుద్ధం: 1,000-1,900 హెజ్బుల్లా మరణాలు</td></tr>
<tr><td>Iran economic damage</td><td>$270 billion – $1 trillion estimated</td><td class="bi-te">ఇరాన్ ఆర్థిక నష్టం: $270B – $1T</td></tr>
<tr><td>Pakistan mediated ceasefire</td><td>Pakistan mediated conditional ceasefire — April 8, 2026; Pakistan's shared border, Muslim identity, and neutrality enabled role</td><td class="bi-te">పాకిస్తాన్ కదనవిరమణ మధ్యవర్తి — ఏప్రిల్ 8, 2026</td></tr>
<tr><td>Key Israeli leaders</td><td>PM Benjamin Netanyahu + Defense Minister Israel Katz + IDF Chief Eyal Zamir</td><td class="bi-te">ఇజ్రాయెల్ నాయకత్వం: Netanyahu + Katz + Zamir</td></tr>
<tr><td>US key leaders</td><td>President Trump + SecDef Pete Hegseth (since Jan 20, 2025) + CENTCOM Gen. Michael Kurilla</td><td class="bi-te">ట్రంప్ + Pete Hegseth + Gen. Kurilla</td></tr>
</table>

<div class="section-hdr">India's Stance / భారత్ వైఖరి</div>
<p>India maintained <b>neutrality</b> in the 2026 Iran War — strategic reasons: India's Chabahar Port investment (~$500M+) in Iran, 8 million Indian diaspora in Gulf, energy imports from Iran &amp; Gulf. EAM S. Jaishankar engaged both sides diplomatically. India evacuated nationals if needed.</p>
<p class="bi-te">భారత్ తటస్థ వైఖరి — చాబహార్ పోర్ట్ పెట్టుబడి, గల్ఫ్‌లో 80 లక్షల భారతీయ ప్రవాసులు, ఇరాన్ & గల్ఫ్ నుండి ఇంధన దిగుమతులు. జైశంకర్ రెండు వైపుల దౌత్యం.</p>

<div class="section-hdr">Key Concepts / ముఖ్య భావనలు</div>
<table class="key-table">
<tr><th>Concept</th><th>Meaning</th><th class="bi-te">వివరణ</th></tr>
<tr><td>IRGC Quds Force</td><td>Iran's external operations — supports Hezbollah, Hamas, Houthis, PMF — 'Axis of Resistance'</td><td class="bi-te">ఇరాన్ బాహ్య కార్యకలాపాల దళం</td></tr>
<tr><td>Samson Option</td><td>Israel's undeclared nuclear deterrence — massive retaliation if existential threat</td><td class="bi-te">ఇజ్రాయెల్ అణు నిరోధ వ్యూహం</td></tr>
<tr><td>Axis of Resistance</td><td>Iran + Hezbollah (Lebanon) + Hamas (Gaza) + Houthis (Yemen) + PMF (Iraq)</td><td class="bi-te">ప్రతిఘటన అక్షం</td></tr>
<tr><td>Chabahar Port</td><td>India's strategic port in southeastern Iran — India invested $500M+; access to Afghanistan &amp; Central Asia bypassing Pakistan</td><td class="bi-te">చాబహార్ — పాకిస్తాన్‌ను దాటి అఫ్ఘానిస్తాన్/మధ్య ఆసియాకు భారత్ మార్గం</td></tr>
</table>
"""))

print("Part 7 appended — Mideast (2) = 23 total DONE!")

# ════════════════════════════════════════════════════════════════
#  DATABASE INSERT
# ════════════════════════════════════════════════════════════════

if USE_POSTGRES:
    cur = conn.cursor()
    # Only delete tags from this file — don't wipe awards notes
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
print(f"SUCCESS: Seeded {len(NOTES)} International Current Affairs concept notes into DB.")
for tag, label, *_ in NOTES:
    print(f"  • {tag:30s} — {label}")
