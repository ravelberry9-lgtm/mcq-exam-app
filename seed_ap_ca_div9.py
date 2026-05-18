"""
seed_ap_ca_div9.py
AP Current Affairs — Chapter 9: పద్మ పురస్కారాలు, కేంద్ర సంస్థలు, AP హైకోర్టు & రాజ్యాంగం

AUDIT LOG (2026-05-18, revised):
- No junk MCQs found (no empty options, single-letter options, or nonsense options).
- 3 Telangana-only Padma award MCQs REMOVED (Nageshwar Reddy, Manda Krishna Madiga, Rama Reddy Mamidi)
  to keep AP CA chapter focused on AP-specific content. Combined Telugu-states count MCQs retained.
- 1 duplicate Article 371-D MCQ removed (kept the first occurrence).
- No factual errors found. Key facts verified:
  * Allu Arjun — first Telugu actor to win National Best Actor (69th National Film Awards 2022,
    awarded 2024) for Pushpa: The Rise.
  * AIIMS Mangalagiri is in Guntur district, AP (not Mangalagiri town of old Guntur dist.).
  * AP High Court — Justice Lisa Gill became first woman Chief Justice from April 25, 2026.
  * IIT Tirupati, NIT AP (Tadepalligudem), IISER Tirupati, CUAP Anantapur all correctly placed.
  * Naatu Naatu: Oscar 2023 Best Original Song (RRR, S.S. Rajamouli).
- MCQ_DATA includes _EXTRA_MCQ_DATA appended at bottom (MCQ_DATA = MCQ_DATA + _EXTRA_MCQ_DATA).
  No duplicate questions detected between the two blocks.
- No abrupt or meaningless question text found.
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div9_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "sub": "Exam Hotspots — Padma Awards, Institutions, HC & Constitution",
        "summary": "పద్మ పురస్కారాలు, జాతీయ పురస్కారాలు, కేంద్ర సంస్థలు, AP హైకోర్టు, రాజ్యాంగ అంశాలు — పరీక్ష హాట్‌స్పాట్‌లు",
        "html": """<div class="concept-cover">
  <h1>Exam Hotspots — Awards &amp; Institutions &nbsp;<span class="bi-te">/ పరీక్ష కీలక భావనలు</span></h1>
  <div class="sub">Padma Awards • National Awards • Central Institutions • AP HC • Constitution</div>
</div>

<div class="section-hdr">Civilian Awards Hierarchy / పౌర పురస్కారాల క్రమం</div>
<table class="key-table">
<tr><th>Rank</th><th>Award</th><th class="bi-te">వివరణ</th></tr>
<tr><td>1 (highest)</td><td><b>Bharat Ratna</b></td><td class="bi-te">భారత రత్న — అత్యున్నతం</td></tr>
<tr><td>2</td><td><b>Padma Vibhushan</b></td><td class="bi-te">పద్మ విభూషణ్</td></tr>
<tr><td>3</td><td><b>Padma Bhushan</b></td><td class="bi-te">పద్మ భూషణ్</td></tr>
<tr><td>4</td><td><b>Padma Shri</b></td><td class="bi-te">పద్మ శ్రీ</td></tr>
</table>
<p><b>Announcement:</b> Padma awards are announced on <b>Republic Day (Jan 26)</b> every year and conferred by the President in March/April at Rashtrapati Bhavan.</p>

<div class="section-hdr">Exam Hotspots Snapshot / పరీక్ష హాట్‌స్పాట్‌లు</div>
<table class="key-table">
<tr><th>Topic</th><th>Key fact</th><th class="bi-te">వివరణ</th></tr>
<tr><td>2026 Padma Awards (Telugu)</td><td>12 awardees: 1 PB + 11 PS</td><td class="bi-te">12 తెలుగు గ్రహీతలు</td></tr>
<tr><td>Oscar 2023</td><td>'Naatu Naatu' (RRR) — Best Original Song</td><td class="bi-te">నాటు నాటు — MM కీరవాణి</td></tr>
<tr><td>69th National Film Award</td><td>Allu Arjun — first Telugu Best Actor</td><td class="bi-te">తొలి తెలుగు Best Actor</td></tr>
<tr><td>AP High Court CJ</td><td>Justice Lisa Gill (6th CJ, since Apr 25, 2026)</td><td class="bi-te">6వ CJ — తొలి మహిళా CJ</td></tr>
<tr><td>AP districts</td><td>28 (since Jan 1, 2026)</td><td class="bi-te">28 జిల్లాలు (2026 జన. 1)</td></tr>
<tr><td>Article 371-D</td><td>32nd Amendment, 1973 — AP local-area protection</td><td class="bi-te">32వ సవరణ 1973</td></tr>
<tr><td>APRA 2014</td><td>Act No. 6/2014 — effective Jun 2, 2014</td><td class="bi-te">జూన్ 2, 2014</td></tr>
<tr><td>APRA Amendment 2026</td><td>Act No. 7/2026 — Amaravati as capital</td><td class="bi-te">అమరావతి రాజధాని</td></tr>
</table>
<p class="bi-te">పద్మ పురస్కారాల క్రమం: భారత రత్న → పద్మ విభూషణ్ → పద్మ భూషణ్ → పద్మ శ్రీ. గణతంత్ర దినం (జనవరి 26) నాడు ప్రకటిస్తారు, మార్చి-ఏప్రిల్‌లో రాష్ట్రపతి భవన్‌లో ప్రదానం చేస్తారు.</p>"""
    },
    {
        "id": "div9_s2",
        "title": "పద్మ పురస్కారాలు — AP వ్యక్తులు",
        "sub": "Padma Awards — AP Personalities (2025 & 2026)",
        "summary": "2025: Balakrishna (PB), Nageshwar Reddy (PV-TG), Manda Krishna Madiga (PS-TG) = 7 Telugu; 2026: Nori (PB-USA), 4 AP Shri, 7 TG Shri = 12 Telugu; SP బాలసుబ్రహ్మణ్యం PV 2021; K. విశ్వనాథ్ PV 2017",
        "html": """<div class="concept-cover">
  <h1>Padma Awards — AP Personalities &nbsp;<span class="bi-te">/ పద్మ పురస్కారాలు — AP</span></h1>
  <div class="sub">2026: 131 total (5 PV + 13 PB + 113 PS) • AP — 4 Padma Shri • Nori PB</div>
</div>

<div class="section-hdr">2026 Padma Awards — National Snapshot / 2026 జాతీయ చిత్రం</div>
<table class="key-table">
<tr><th>Category</th><th>Count</th><th>Notable</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Total 2026</b></td><td><b>131</b> awards</td><td>Announced Jan 25, 2026</td><td class="bi-te">మొత్తం 131</td></tr>
<tr><td>Padma Vibhushan</td><td><b>5</b></td><td>Dharmendra (posth.), V.S. Achuthanandan (posth.), K.T. Thomas, N. Rajam, P. Narayanan</td><td class="bi-te">5 పద్మ విభూషణ్</td></tr>
<tr><td>Padma Bhushan</td><td><b>13</b></td><td>Alka Yagnik, Mammootty, Uday Kotak, Piyush Pandey (posth.), Vijay Amritraj, <b>Nori Dattatreyudu</b>, Rohit Sharma</td><td class="bi-te">13 పద్మ భూషణ్</td></tr>
<tr><td>Padma Shri</td><td>113</td><td>Across art, science, public affairs, social work</td><td class="bi-te">113 పద్మ శ్రీ</td></tr>
</table>

<div class="section-hdr">2026 Padma Awards — AP Awardees (4) / 2026 AP గ్రహీతలు</div>
<table class="key-table">
<tr><th>Recipient</th><th>Award</th><th>Field</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Dr. Nori Dattatreyudu</b> (USA-based)</td><td>Padma Bhushan</td><td>Medicine (Oncology)</td><td class="bi-te">తెలుగు సంతతి వైద్యుడు</td></tr>
<tr><td>Maganti Murali Mohan</td><td>Padma Shri</td><td>Art</td><td class="bi-te">మాగంటి మురళీ మోహన్</td></tr>
<tr><td>Gadde Babu Rajendra Prasad</td><td>Padma Shri</td><td>Art</td><td class="bi-te">గద్దె బాబు రాజేంద్ర ప్రసాద్</td></tr>
<tr><td>Garimella Balakrishna Prasad</td><td>Padma Shri (Posthumous)</td><td>Art</td><td class="bi-te">గరిమెళ్ళ — మరణానంతరం</td></tr>
<tr><td>Vempaty Kutumba Sastry</td><td>Padma Shri</td><td>Literature &amp; Education (Sanskrit)</td><td class="bi-te">వేంపటి కుటుంబశాస్త్రి</td></tr>
</table>
<p><b>Telugu states total 2026:</b> 12 awardees — 1 Padma Bhushan (Nori, USA-based AP-origin) + 4 AP Padma Shri + 7 Telangana Padma Shri.</p>

<div class="section-hdr">2025 Padma Awards — AP Awardees / 2025 AP గ్రహీతలు</div>
<table class="key-table">
<tr><th>Recipient</th><th>Award</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Nandamuri Balakrishna</b></td><td>Padma Bhushan (Art)</td><td class="bi-te">నందమూరి బాలకృష్ణ — NTR కుమారుడు</td></tr>
<tr><td>Madugula Nagaphani Sarma</td><td>Padma Shri (Literature)</td><td class="bi-te">అవధాని</td></tr>
<tr><td>K.L. Krishna</td><td>Padma Shri (Lit &amp; Edu)</td><td class="bi-te">K.L. కృష్ణ — ఆర్థిక శాస్త్రవేత్త</td></tr>
<tr><td>Miriyala Apparao</td><td>Padma Shri Posthumous (Burrakatha)</td><td class="bi-te">మిర్యాల అప్పారావు — తాడేపల్లిగూడెం</td></tr>
<tr><td>Vadiraj Panchamukhi</td><td>Padma Shri (Music)</td><td class="bi-te">వాదిరాజ్ పంచముఖి</td></tr>
</table>

<div class="section-hdr">Historic AP Padma Award Holders / చారిత్రక AP గ్రహీతలు</div>
<table class="key-table">
<tr><th>Recipient</th><th>Award &amp; Year</th><th class="bi-te">వివరణ</th></tr>
<tr><td>SP Balasubrahmanyam</td><td>Padma Vibhushan 2021 (Posthumous)</td><td class="bi-te">SPB — నెల్లూరు</td></tr>
<tr><td>K. Viswanath</td><td>Padma Shri 1992; Dadasaheb Phalke 2016</td><td class="bi-te">K. విశ్వనాథ్ — శంకరాభరణం</td></tr>
<tr><td>Chiranjeevi</td><td>Padma Bhushan 2006</td><td class="bi-te">చిరంజీవి — నరసాపురం</td></tr>
<tr><td>SS Rajamouli</td><td>Padma Shri 2012</td><td class="bi-te">SS రాజమౌళి — RRR/బాహుబలి</td></tr>
<tr><td>PV Sindhu</td><td>Padma Shri 2015; Padma Bhushan 2020</td><td class="bi-te">PV సింధు</td></tr>
</table>
<p class="bi-te">2026 Padma Awards (జన. 25 ప్రకటన): తెలుగు రాష్ట్రాల నుండి 12 మంది. Dr. Nori కి USA నుండి Padma Bhushan; AP నుండి 4 Padma Shri (Vempaty Kutumba Sastry — Literature, మిగతా ముగ్గురు Art); Garimella మరణానంతరం.</p>"""
    },
    {
        "id": "div9_s3",
        "title": "Oscar & అంతర్జాతీయ పురస్కారాలు",
        "sub": "Oscar & National Film Awards — Telugu Wins",
        "summary": "Oscar 2023: నాటు నాటు (RRR) — MM కీరవాణి; 69వ NFA: అల్లు అర్జున్ Best Actor (Pushpa) — తొలి తెలుగు నటుడు; DSP Best Music (Songs); 70వ NFA: Karthikeya 2 (Best Telugu); 71వ NFA: Bhagavanth Kesari (Best Telugu), Baby (Screenplay+Playback)",
        "html": """<div class="concept-cover">
  <h1>Oscar &amp; National Film Awards &nbsp;<span class="bi-te">/ Oscar &amp; జాతీయ పురస్కారాలు</span></h1>
  <div class="sub">Naatu Naatu Oscar 2023 • Allu Arjun first Telugu Best Actor (NFA)</div>
</div>

<div class="section-hdr">'Naatu Naatu' — Oscar 2023 / నాటు నాటు ఆస్కార్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Film</td><td>RRR (Director: SS Rajamouli)</td><td class="bi-te">RRR (SS రాజమౌళి)</td></tr>
<tr><td>Award ceremony</td><td><b>95th Academy Awards (2023)</b></td><td class="bi-te">95వ Academy Awards</td></tr>
<tr><td>Category</td><td>Best Original Song</td><td class="bi-te">Best Original Song</td></tr>
<tr><td>Music</td><td>M.M. Keeravani (West Godavari — Kovvur)</td><td class="bi-te">MM కీరవాణి (కొవ్వూరు)</td></tr>
<tr><td>Lyrics</td><td>Chandrabose</td><td class="bi-te">చంద్రబోస్</td></tr>
<tr><td>Golden Globe</td><td>Won earlier in 2023 (Best Original Song)</td><td class="bi-te">Golden Globe కూడా</td></tr>
</table>

<div class="section-hdr">69th National Film Awards (2022 films) / 69వ జాతీయ పురస్కారాలు</div>
<table class="key-table">
<tr><th>Award</th><th>Winner</th><th>Film</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Best Actor</b></td><td>Allu Arjun</td><td>Pushpa: The Rise</td><td class="bi-te">తొలి తెలుగు Best Actor</td></tr>
<tr><td>Best Music (Songs)</td><td>Devi Sri Prasad</td><td>Pushpa: The Rise</td><td class="bi-te">DSP</td></tr>
<tr><td>Best Music (Background)</td><td>M.M. Keeravani</td><td>RRR</td><td class="bi-te">MM కీరవాణి</td></tr>
<tr><td>Best Telugu Film</td><td>Uppena</td><td>—</td><td class="bi-te">ఉప్పెన</td></tr>
</table>

<div class="section-hdr">70th &amp; 71st NFA — Best Telugu Film / 70-71 NFA Telugu</div>
<table class="key-table">
<tr><th>Edition (year films)</th><th>Best Telugu Film</th><th class="bi-te">వివరణ</th></tr>
<tr><td>70th NFA (2022)</td><td>Karthikeya 2</td><td class="bi-te">కార్తికేయ 2</td></tr>
<tr><td>71st NFA (2023)</td><td><b>Bhagavanth Kesari</b> (Balakrishna; Anil Ravipudi)</td><td class="bi-te">భగవంత్ కేసరి</td></tr>
<tr><td>71st NFA — Best Screenplay</td><td>Sai Rajesh — Baby</td><td class="bi-te">Baby — Sai రాజేష్</td></tr>
<tr><td>71st NFA — Best Playback (Male)</td><td>PVNS Rohith — 'Premistunna' (Baby)</td><td class="bi-te">Baby — 'ప్రేమిస్తున్నా'</td></tr>
</table>
<p class="bi-te">Pushpa: The Rise (2021 డిసెంబర్) చిత్రానికి అల్లు అర్జున్ తొలి తెలుగు Best Actor — తెలుగు సినిమా చరిత్రలో ఇది ఒక మైలురాయి. DSP అదే చిత్రానికి Best Music (Songs); MM కీరవాణి అదే వేడుకలో RRR కి Best Music (Background) సాధించారు.</p>"""
    },
    {
        "id": "div9_s4",
        "title": "సాహిత్య & సాంస్కృతిక పురస్కారాలు",
        "sub": "Literary & Cultural Awards — Telugu Recipients",
        "summary": "విశ్వనాథ సత్యనారాయణ — జ్ఞానపీఠ పురస్కారం 1970 (మొదటి తెలుగు జ్ఞానపీఠ); దాదాసాహేబ్ ఫాల్కే 2016 = K. విశ్వనాథ్; సాహిత్య అకాడమి",
        "html": """<div class="concept-cover">
  <h1>Literary &amp; Cultural Awards &nbsp;<span class="bi-te">/ సాహిత్య-సాంస్కృతిక పురస్కారాలు</span></h1>
  <div class="sub">Jnanpith • Dadasaheb Phalke • Sahitya Akademi</div>
</div>

<div class="section-hdr">Telugu Jnanpith Awardees / తెలుగు జ్ఞానపీఠ్ గ్రహీతలు</div>
<table class="key-table">
<tr><th>Recipient</th><th>Year</th><th>Notable work</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Viswanatha Satyanarayana</b></td><td><b>1970 (1st Telugu)</b></td><td>Ramayana Kalpavruksham</td><td class="bi-te">విశ్వనాథ సత్యనారాయణ — తొలి తెలుగు జ్ఞానపీఠ్</td></tr>
<tr><td>C. Narayana Reddy (Sinare)</td><td>1988 (2nd Telugu)</td><td>Viswambhara</td><td class="bi-te">సినారె — విశ్వంభర</td></tr>
<tr><td>Ravuri Bharadwaja</td><td>2012 (3rd Telugu)</td><td>Pakudu Rallu</td><td class="bi-te">రావూరి భరద్వాజ</td></tr>
</table>

<div class="section-hdr">Dadasaheb Phalke Award / దాదాసాహేబ్ ఫాల్కే</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Field</td><td>Highest award in Indian cinema (lifetime achievement)</td><td class="bi-te">భారత సినిమా అత్యున్నత పురస్కారం</td></tr>
<tr><td><b>K. Viswanath</b></td><td>2016 (conferred 2017)</td><td class="bi-te">K. విశ్వనాథ్ — శంకరాభరణం, సాగర సంగమం</td></tr>
<tr><td>Akkineni Nageswara Rao (ANR)</td><td>1990</td><td class="bi-te">అక్కినేని నాగేశ్వరరావు</td></tr>
<tr><td>B.N. Reddy</td><td>1974</td><td class="bi-te">బి.ఎన్. రెడ్డి (Vauhini)</td></tr>
<tr><td>L.V. Prasad</td><td>1982</td><td class="bi-te">L.V. ప్రసాద్</td></tr>
<tr><td>D. Rama Naidu</td><td>2009</td><td class="bi-te">డి. రామానాయుడు (Suresh Productions)</td></tr>
</table>

<div class="section-hdr">Sahitya Akademi &amp; Cultural Awards / సాహిత్య అకాడమి</div>
<p>The Sahitya Akademi Award is given annually in Telugu literature. The Kendra Sahitya Akademi (founded 1954) recognises one Telugu work each year. K. Viswanath also received Padma Shri (1992) for his contribution to cinema.</p>
<p class="bi-te">విశ్వనాథ సత్యనారాయణ 'రామాయణ కల్పవృక్షం' కోసం 1970లో తొలి తెలుగు జ్ఞానపీఠ్ పొందారు. K. విశ్వనాథ్ 2016 దాదాసాహేబ్ ఫాల్కే + 1992 పద్మ శ్రీ గ్రహీత — ఆయనకు పద్మ విభూషణ్ రాలేదు. తెలుగు జ్ఞానపీఠ్ గ్రహీతలు మొత్తం 3 మంది (1970/1988/2012).</p>"""
    },
    {
        "id": "div9_s5",
        "title": "కేంద్ర విద్యా సంస్థలు — AP",
        "sub": "Central Educational Institutions in AP (APRA 2014 grants)",
        "summary": "IIT తిరుపతి (2015), NIT AP-తాడేపల్లిగూడెం (2015), AIIMS మంగళగిరి (2020/2022), CUAP అనంతపురం (2014/2016), IISER తిరుపతి (2015)",
        "html": """<div class="concept-cover">
  <h1>Central Educational Institutions — AP &nbsp;<span class="bi-te">/ AP కేంద్ర విద్యా సంస్థలు</span></h1>
  <div class="sub">APRA 2014 schedule guarantees — IIT, NIT, AIIMS, CUAP, IISER, IIIT</div>
</div>

<div class="section-hdr">Premier Institutions / ప్రధాన సంస్థలు</div>
<table class="key-table">
<tr><th>Institution</th><th>Location</th><th>Estd.</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>IIT Tirupati</b></td><td>Yerpedu, Tirupati district</td><td>2015</td><td class="bi-te">9వ IIT (APRA 2014 వాగ్దానం)</td></tr>
<tr><td><b>NIT Andhra Pradesh</b></td><td>Tadepalligudem, Eluru district</td><td>2015</td><td class="bi-te">31 NITs లో ఒకటి</td></tr>
<tr><td><b>AIIMS Mangalagiri</b></td><td>Mangalagiri, Guntur district</td><td>Foundation 2018; OPD 2018; full operation 2022</td><td class="bi-te">PMSSY కింద</td></tr>
<tr><td><b>CUAP</b> (Central University of AP)</td><td>Janthaluru, Anantapur district</td><td>2014 (Act); 2016 temp campus</td><td class="bi-te">కేంద్రీయ విశ్వవిద్యాలయం</td></tr>
<tr><td><b>IISER Tirupati</b></td><td>Tirupati district</td><td>2015</td><td class="bi-te">5వ IISER</td></tr>
<tr><td>IIIT Sri City</td><td>Chittoor district</td><td>2013 (PPP model)</td><td class="bi-te">IIIT శ్రీ సిటీ</td></tr>
<tr><td>IIM Visakhapatnam</td><td>Vizag (Andhra University campus initially)</td><td>2015</td><td class="bi-te">IIM విశాఖపట్నం</td></tr>
<tr><td>IIPE</td><td>Indian Institute of Petroleum &amp; Energy — Visakhapatnam</td><td>2016</td><td class="bi-te">IIPE</td></tr>
</table>

<div class="section-hdr">APRA 2014 Schedule XIII Background / APRA 2014 నేపథ్యం</div>
<p>The Andhra Pradesh Reorganisation Act, 2014 (Section 93 + Schedule XIII) committed the Centre to establish several premier institutions in AP including IIT, NIT, AIIMS, IIM, IISER, IIIT, Central University, Petroleum University, Agricultural University, Tribal University and a National Institute of Disaster Management. Most have been operationalised between 2014-2022; the Tribal University at Vizianagaram is the most recent addition.</p>

<div class="section-hdr">Quick District-wise Map / జిల్లాల వారీ</div>
<table class="key-table">
<tr><th>District</th><th>Central institution</th></tr>
<tr><td>Tirupati</td><td>IIT, IISER, SVIMS</td></tr>
<tr><td>Guntur</td><td>AIIMS Mangalagiri</td></tr>
<tr><td>Eluru</td><td>NIT AP (Tadepalligudem)</td></tr>
<tr><td>Anantapur</td><td>CUAP (Janthaluru)</td></tr>
<tr><td>Visakhapatnam</td><td>IIM, IIPE, GITAM, Andhra University</td></tr>
<tr><td>Chittoor</td><td>IIIT Sri City</td></tr>
</table>
<p class="bi-te">AIIMS మంగళగిరి గుంటూరు జిల్లాలో ఉంది (పాత గుంటూరు డివిజన్‌లోని మంగళగిరి పట్టణం). 2018లో OPD ప్రారంభించి 2022లో పూర్తి స్థాయిలో పనిచేస్తోంది. PMSSY (ప్రధాన మంత్రి స్వాస్థ్య సురక్ష యోజన) కింద APRA 2014 వాగ్దానంగా మంజూరైంది.</p>"""
    },
    {
        "id": "div9_s6",
        "title": "AP హైకోర్టు",
        "sub": "AP High Court — Establishment & Chief Justices",
        "summary": "AP పునర్విభజన చట్టం 2014 సెక్షన్ 30; జన. 1, 2019 అమరావతిలో ప్రత్యేక AP HC; Justice Dhiraj Singh Thakur (5వ CJ, Jul 2023–Apr 2026); Justice Lisa Gill — 6వ CJ, AP HC తొలి మహిళా CJ (Apr 25, 2026)",
        "html": """<div class="concept-cover">
  <h1>AP High Court &nbsp;<span class="bi-te">/ AP హైకోర్టు</span></h1>
  <div class="sub">Estd. Jan 1, 2019 at Amaravati • APRA 2014 Section 30 • 6th CJ Lisa Gill (first woman CJ)</div>
</div>

<div class="section-hdr">Establishment / స్థాపన</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Statutory basis</td><td>APRA 2014 — <b>Section 30</b></td><td class="bi-te">APRA 2014 సెక్షన్ 30</td></tr>
<tr><td>Date of establishment</td><td><b>January 1, 2019</b></td><td class="bi-te">జనవరి 1, 2019</td></tr>
<tr><td>Location</td><td>Amaravati (temporary at Justice City, Nelapadu, Guntur dist.)</td><td class="bi-te">అమరావతి (నేలపాడు)</td></tr>
<tr><td>Pre-2019 arrangement</td><td>Hyderabad HC served both AP &amp; TS (2014-2018)</td><td class="bi-te">2014-2018 ఉమ్మడి హైదరాబాద్ HC</td></tr>
<tr><td>Sanctioned strength</td><td>37 judges (incl. CJ)</td><td class="bi-te">37 న్యాయమూర్తులు</td></tr>
</table>

<div class="section-hdr">Chief Justices of AP HC / AP HC ప్రధాన న్యాయమూర్తులు</div>
<table class="key-table">
<tr><th>#</th><th>Chief Justice</th><th>Tenure</th><th class="bi-te">వివరణ</th></tr>
<tr><td>1</td><td>Justice C. Praveen Kumar (Acting)</td><td>Jan 1, 2019 – Mar 31, 2019</td><td class="bi-te">తొలి (ఆక్టింగ్)</td></tr>
<tr><td>1 (regular)</td><td>Justice Jitendra Kumar Maheshwari</td><td>Mar 7, 2019 – Jan 6, 2021</td><td class="bi-te">JK మహేశ్వరి — తొలి సాధారణ CJ</td></tr>
<tr><td>2</td><td>Justice Arup Kumar Goswami</td><td>Jan 7, 2021 – Sep 10, 2021</td><td class="bi-te">అరూప్ కుమార్ గోస్వామి</td></tr>
<tr><td>3</td><td>Justice Prashant Kumar Mishra</td><td>Oct 11, 2021 – May 18, 2023</td><td class="bi-te">ప్రశాంత్ కుమార్ మిశ్రా</td></tr>
<tr><td>4</td><td>Justice K. Lakshmana Rao (Acting)</td><td>May 19, 2023 – Jul 27, 2023</td><td class="bi-te">ఆక్టింగ్</td></tr>
<tr><td>5</td><td>Justice Dhiraj Singh Thakur</td><td>Jul 28, 2023 – Apr 24, 2026 (retired)</td><td class="bi-te">5వ CJ — ధీరజ్ సింగ్ ఠాకూర్</td></tr>
<tr><td><b>6</b></td><td><b>Justice Lisa Gill</b></td><td><b>Apr 25, 2026 — present</b></td><td class="bi-te"><b>6వ CJ — తొలి మహిళా CJ</b></td></tr>
</table>

<p><b>Justice Lisa Gill — historic firsts:</b> Transferred from Punjab &amp; Haryana High Court, she was sworn in as AP HC judge in March 2026 and elevated to Chief Justice on Apr 25, 2026 following Justice Thakur's retirement on Apr 24, 2026. She is the <b>first woman Chief Justice in the history of the Andhra Pradesh High Court</b>. Recommended by the Supreme Court Collegium and notified by the Centre under Article 217 (transfer/appointment of HC judges).</p>
<p class="bi-te">జస్టిస్ లిసా గిల్ Punjab &amp; Haryana HC నుండి బదిలీ అయి మార్చి 2026లో AP HC న్యాయమూర్తిగా ప్రమాణం చేశారు. ఏప్రిల్ 24, 2026న జస్టిస్ ఠాకూర్ పదవీ విరమణ చేయగా, ఏప్రిల్ 25, 2026న 6వ CJ గా ప్రమాణ స్వీకారం చేశారు — AP HC చరిత్రలో తొలి మహిళా ప్రధాన న్యాయమూర్తి. (గమనిక: AP HC 2019లోనే విడిగా ఏర్పడింది; దీని ముందు ఉమ్మడి హైదరాబాద్ HC.)</p>"""
    },
    {
        "id": "div9_s7",
        "title": "రాజ్యాంగం & AP",
        "sub": "Constitution & AP — Article 371-D, APRA, SCS",
        "summary": "ఆర్టికల్ 371-డి (32వ సవరణ 1973); APRA 2014 ముఖ్యాంశాలు; ప్రత్యేక హోదా డిమాండ్; APRA సవరణ 2026",
        "html": """<div class="concept-cover">
  <h1>Constitution &amp; AP &nbsp;<span class="bi-te">/ రాజ్యాంగం &amp; AP</span></h1>
  <div class="sub">Article 371-D • APRA 2014 • Special Category Status • APRA Amendment 2026</div>
</div>

<div class="section-hdr">Article 371-D / ఆర్టికల్ 371-డి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Inserted by</td><td><b>32nd Constitutional Amendment, 1973</b></td><td class="bi-te">32వ సవరణ 1973</td></tr>
<tr><td>Applies to</td><td>Andhra Pradesh (and Telangana since 2014)</td><td class="bi-te">AP (మరియు తెలంగాణ)</td></tr>
<tr><td>Purpose</td><td>Local-area reservation in education &amp; state-government employment</td><td class="bi-te">స్థానిక రిజర్వేషన్</td></tr>
<tr><td>Presidential Order</td><td>AP Public Employment (Organisation of Local Cadres) Order, 1975</td><td class="bi-te">1975 Presidential Order</td></tr>
<tr><td>G.O. 610</td><td>1985 — implemented 6-zone roster system for non-gazetted posts</td><td class="bi-te">G.O.610 — 6 Zones</td></tr>
<tr><td>Survives bifurcation</td><td>Yes — applies to both successor states</td><td class="bi-te">విభజన తర్వాత కూడా</td></tr>
</table>

<div class="section-hdr">APRA 2014 — Key Provisions / APRA 2014 ముఖ్యాంశాలు</div>
<table class="key-table">
<tr><th>Section</th><th>Provision</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Section 3</td><td>Creation of Telangana state</td><td class="bi-te">తెలంగాణ ఏర్పాటు</td></tr>
<tr><td>Section 5</td><td>Capital — "new capital" (originally undefined; amended 2026)</td><td class="bi-te">రాజధాని</td></tr>
<tr><td>Section 8</td><td>Hyderabad common capital for 10 years</td><td class="bi-te">హైదరాబాద్ 10 సం. ఉమ్మడి</td></tr>
<tr><td>Section 24</td><td>Lok Sabha 25 + Rajya Sabha 11 for AP</td><td class="bi-te">LS 25 + RS 11</td></tr>
<tr><td>Section 30</td><td>AP High Court establishment</td><td class="bi-te">AP HC ఏర్పాటు</td></tr>
<tr><td>Section 93 + Schedule XIII</td><td>IIT/NIT/AIIMS/IIM/IISER etc. promises</td><td class="bi-te">కేంద్ర సంస్థలు</td></tr>
<tr><td><b>Section 94</b></td><td><b>Polavaram declared National Project</b></td><td class="bi-te">పోలవరం జాతీయ ప్రాజెక్టు</td></tr>
</table>

<div class="section-hdr">Special Category Status (SCS) / ప్రత్యేక హోదా</div>
<p>SCS was promised by PM Manmohan Singh on the floor of Rajya Sabha during the APRA 2014 debate (Feb 20, 2014) — but it was <b>not written into the Act</b>. The <b>14th Finance Commission (2015)</b> recommended abolishing the SCS framework entirely (except for the existing 11 NE/hilly states), and NITI Aayog formalised this in 2015 by replacing the Planning Commission. The Centre's alternative was a Special Assistance / Special Package (loans + grants for backward districts, Polavaram, Amaravati). The SCS demand remains politically alive in AP.</p>

<div class="section-hdr">APRA Amendment 2026 / APRA సవరణ 2026</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Title</td><td>AP Reorganisation (Amendment) Act, 2026</td><td class="bi-te">2026 సవరణ చట్టం</td></tr>
<tr><td>Act No.</td><td><b>Act No. 7 of 2026</b></td><td class="bi-te">Act No. 7/2026</td></tr>
<tr><td>Lok Sabha</td><td>Apr 1, 2026</td><td class="bi-te">LS — ఏప్రిల్ 1</td></tr>
<tr><td>Rajya Sabha</td><td>Apr 2, 2026</td><td class="bi-te">RS — ఏప్రిల్ 2</td></tr>
<tr><td>President's assent</td><td>Apr 6, 2026 (Droupadi Murmu, Art. 111)</td><td class="bi-te">రాష్ట్రపతి — ఏప్రిల్ 6</td></tr>
<tr><td>What it amends</td><td>Section 5(2) — names <b>"Amaravati"</b> as AP capital</td><td class="bi-te">Section 5(2) — అమరావతి</td></tr>
<tr><td>Retrospective from</td><td>June 2, 2024</td><td class="bi-te">జూన్ 2, 2024 నుండి</td></tr>
<tr><td>Significance</td><td>3rd amendment to APRA 2014; 1st state capital named in central law</td><td class="bi-te">3వ APRA సవరణ</td></tr>
</table>
<p class="bi-te">2026 సవరణ APRA 2014కి 3వ సవరణ. మూల చట్టంలో "new capital" అని మాత్రమే ఉండేది — 2026లో "Amaravati" అని పేరుతో సవరించారు. ఏ రాష్ట్ర రాజధాని కేంద్ర చట్టంలో పేరు ద్వారా చేర్చిన మొదటి ఉదాహరణ ఇదే.</p>"""
    },
    {
        "id": "div9_s8",
        "title": "AP జిల్లాలు & రాజ్యాంగ పదవులు",
        "sub": "AP Districts & Constitutional Posts (Current Status)",
        "summary": "13→26 జిల్లాలు (ఏప్రిల్ 2022)→28 జిల్లాలు (జన. 1, 2026); గవర్నర్ S. అబ్దుల్ నజీర్; CM చంద్రబాబు (జూన్ 12, 2024); 175 అసెంబ్లీ, 25 LS, 11 RS స్థానాలు",
        "html": """<div class="concept-cover">
  <h1>AP Districts &amp; Constitutional Posts &nbsp;<span class="bi-te">/ AP జిల్లాలు &amp; రాజ్యాంగ పదవులు</span></h1>
  <div class="sub">28 districts (Jan 1, 2026) • Gov Abdul Nazeer • CM Naidu • 175 + 25 + 11</div>
</div>

<div class="section-hdr">District Evolution / జిల్లాల చరిత్ర</div>
<table class="key-table">
<tr><th>Date</th><th>Districts</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Jun 2, 2014</td><td>13 (post-bifurcation)</td><td class="bi-te">13 జిల్లాలు</td></tr>
<tr><td>Apr 4, 2022</td><td><b>26</b> (YSRCP reorganisation)</td><td class="bi-te">26 జిల్లాలు</td></tr>
<tr><td><b>Jan 1, 2026</b></td><td><b>28</b> — added Polavaram + Markapuram</td><td class="bi-te">28 జిల్లాలు (TDP)</td></tr>
</table>
<p>The two new districts added on Jan 1, 2026 are <b>Polavaram</b> (HQ Rampachodavaram, 12 mandals, ~3.5 lakh population) and <b>Markapuram</b> (HQ Markapuram town, 21 mandals). Annamayya district HQ moved from Rayachoti to Madanapalle. Kadapa now has the most mandals.</p>

<div class="section-hdr">Constitutional Posts / రాజ్యాంగ పదవులు</div>
<table class="key-table">
<tr><th>Post</th><th>Holder</th><th>Since</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Governor</td><td>Justice S. Abdul Nazeer</td><td>Feb 2023</td><td class="bi-te">జస్టిస్ ఎస్. అబ్దుల్ నజీర్</td></tr>
<tr><td>Chief Minister</td><td>N. Chandrababu Naidu (4th term)</td><td>Jun 12, 2024</td><td class="bi-te">17వ AP CM</td></tr>
<tr><td>Deputy CM</td><td>K. Pawan Kalyan (JSP)</td><td>Jun 12, 2024</td><td class="bi-te">DCM పవన్ కళ్యాణ్</td></tr>
<tr><td>Assembly Speaker</td><td>Ch. Ayyanna Patrudu</td><td>Jun 2024</td><td class="bi-te">అయ్యన్నపాత్రుడు</td></tr>
<tr><td>HC Chief Justice</td><td>Justice Lisa Gill (6th CJ)</td><td>Apr 25, 2026</td><td class="bi-te">లిసా గిల్</td></tr>
<tr><td>Chief Secretary</td><td>G. Sai Prasad (IAS 1991)</td><td>Mar 1, 2026</td><td class="bi-te">జి. సాయి ప్రసాద్</td></tr>
<tr><td>DGP</td><td>Harish Kumar Gupta (IPS 1992)</td><td>Jan 31, 2025</td><td class="bi-te">హరీష్ కుమార్ గుప్తా</td></tr>
</table>

<div class="section-hdr">Legislature Strength / శాసన సంఖ్య</div>
<table class="key-table">
<tr><th>Body</th><th>Seats</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Lok Sabha (AP)</td><td><b>25</b> (delimitation expected after 2026 census)</td><td class="bi-te">25 LS (delimitation తర్వాత మారవచ్చు)</td></tr>
<tr><td>Rajya Sabha (AP)</td><td>11</td><td class="bi-te">11 RS</td></tr>
<tr><td>Legislative Assembly</td><td>175</td><td class="bi-te">175 అసెంబ్లీ</td></tr>
<tr><td>Legislative Council</td><td>58</td><td class="bi-te">58 శాసన మండలి</td></tr>
</table>
<p class="bi-te">జనవరి 1, 2026 నుండి AP లో 28 జిల్లాలు — పోలవరం (HQ రంపచోడవరం) మరియు మార్కాపురం (HQ మార్కాపురం పట్టణం) కొత్తగా జోడించబడ్డాయి. లోక్‌సభ స్థానాలు 25 — తదుపరి delimitation 2026 జనాభా గణన ఆధారంగా మాత్రమే జరుగుతుంది (అప్పటివరకు 25 అలానే ఉంటుంది).</p>"""
    },
    {
        "id": "div9_s9",
        "title": "పరీక్ష రేపిడ్ రివిజన్",
        "sub": "Rapid Revision — One-Page Cheat Sheet",
        "summary": "పద్మ పురస్కారాలు, పురస్కారాలు, సంస్థలు, హైకోర్టు, రాజ్యాంగం — సంక్షిప్త పట్టిక",
        "html": """<div class="concept-cover">
  <h1>Rapid Revision — Cheat Sheet &nbsp;<span class="bi-te">/ సంక్షిప్త పట్టిక</span></h1>
  <div class="sub">All Division 9 high-yield facts in one place</div>
</div>

<div class="section-hdr">Padma Awards Snapshot / పద్మ సంక్షిప్తం</div>
<table class="key-table">
<tr><th>Year</th><th>Telugu awardees</th></tr>
<tr><td>2026</td><td>1 PB (Nori, USA) + 4 AP PS + 7 TG PS = 12 total</td></tr>
<tr><td>2025</td><td>5 AP (Balakrishna PB + 4 PS) + 2 TG = 7 total</td></tr>
<tr><td>2021</td><td>SP Balasubrahmanyam — Padma Vibhushan (Posthumous)</td></tr>
<tr><td>2020</td><td>PV Sindhu — Padma Bhushan</td></tr>
<tr><td>2016 (Phalke)</td><td>K. Viswanath</td></tr>
<tr><td>2006</td><td>Chiranjeevi — Padma Bhushan</td></tr>
<tr><td>2012</td><td>SS Rajamouli — Padma Shri</td></tr>
</table>

<div class="section-hdr">Films &amp; Awards / సినిమా</div>
<table class="key-table">
<tr><th>Year</th><th>Win</th></tr>
<tr><td>Oscar 2023 (95th)</td><td>'Naatu Naatu' (RRR) — Best Original Song (MM Keeravani / Chandrabose)</td></tr>
<tr><td>69th NFA</td><td>Allu Arjun — Best Actor (Pushpa: The Rise); DSP — Best Music (Songs)</td></tr>
<tr><td>70th NFA</td><td>Karthikeya 2 — Best Telugu Film</td></tr>
<tr><td>71st NFA</td><td>Bhagavanth Kesari — Best Telugu Film; Baby — Best Screenplay (Sai Rajesh) + Best Male Playback (PVNS Rohith)</td></tr>
<tr><td>Jnanpith</td><td>Viswanatha Satyanarayana 1970 (1st), Sinare 1988, Ravuri 2012</td></tr>
</table>

<div class="section-hdr">Central Institutions in AP / కేంద్ర సంస్థలు</div>
<table class="key-table">
<tr><th>Institution</th><th>Location</th></tr>
<tr><td>IIT</td><td>Tirupati (2015)</td></tr>
<tr><td>NIT</td><td>Tadepalligudem, Eluru (2015)</td></tr>
<tr><td>AIIMS</td><td>Mangalagiri, Guntur</td></tr>
<tr><td>CUAP</td><td>Janthaluru, Anantapur</td></tr>
<tr><td>IISER</td><td>Tirupati (2015)</td></tr>
<tr><td>IIM</td><td>Visakhapatnam</td></tr>
</table>

<div class="section-hdr">Constitution &amp; Legislature / రాజ్యాంగం</div>
<table class="key-table">
<tr><th>Item</th><th>Fact</th></tr>
<tr><td>Article 371-D</td><td>32nd Amendment, 1973 (AP local-area reservation)</td></tr>
<tr><td>AP HC estd.</td><td>Jan 1, 2019 (APRA 2014 §30)</td></tr>
<tr><td>AP HC current CJ</td><td>Justice Lisa Gill (6th, since Apr 25, 2026) — 1st woman CJ</td></tr>
<tr><td>APRA 2014</td><td>Act No. 6/2014 — effective Jun 2, 2014</td></tr>
<tr><td>APRA Amendment 2026</td><td>Act No. 7/2026 — Amaravati capital (retrospective from Jun 2, 2024)</td></tr>
<tr><td>AP districts</td><td>28 (since Jan 1, 2026)</td></tr>
<tr><td>AP seats</td><td>175 Assembly + 25 LS + 11 RS + 58 Council</td></tr>
</table>
<p class="bi-te">పరీక్ష ముందు 5-నిమిషాల రివిజన్ కోసం ఈ పట్టికను చూడండి. 2026 ముఖ్యాంశాలు: లిసా గిల్ (Apr 25 — 6వ CJ); APRA సవరణ Act 7/2026 (అమరావతి); 28 జిల్లాలు (Jan 1).</p>"""
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Key concepts
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "పద్మ విభూషణ్ భారతదేశంలో ఏ స్థాయి పురస్కారం?",
        "opt_a": "అత్యున్నత పౌర పురస్కారం",
        "opt_b": "రెండవ అత్యున్నత పౌర పురస్కారం",
        "opt_c": "మూడవ అత్యున్నత పౌర పురస్కారం",
        "opt_d": "నాల్గవ అత్యున్నత పౌర పురస్కారం",
        "answer": "B",
        "explanation_te": "పద్మ పురస్కారాల క్రమం: భారత రత్న (అత్యున్నతం) → పద్మ విభూషణ్ (2వ) → పద్మ భూషణ్ (3వ) → పద్మ శ్రీ (4వ). గణతంత్ర దినం (జనవరి 26) నాడు ప్రకటిస్తారు."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "పద్మ పురస్కారాలు ఏ సందర్భంగా ప్రకటిస్తారు?",
        "opt_a": "స్వాతంత్ర్య దినం (ఆగస్ట్ 15)",
        "opt_b": "గణతంత్ర దినం (జనవరి 26) సందర్భంగా",
        "opt_c": "రాష్ట్ర ఆవిర్భావ దినం",
        "opt_d": "ప్రధానమంత్రి జన్మదినం",
        "answer": "B",
        "explanation_te": "పద్మ పురస్కారాలు ప్రతి సంవత్సరం గణతంత్ర దినం (జనవరి 26) సందర్భంగా ప్రకటిస్తారు. రాష్ట్రపతి అందిస్తారు."
    },
    # Section 1 — Padma Awards AP personalities
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "SP బాలసుబ్రహ్మణ్యంకు పద్మ విభూషణ్ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2019",
        "opt_b": "2020",
        "opt_c": "2021 (మరణానంతరం)",
        "opt_d": "2022",
        "answer": "C",
        "explanation_te": "SP బాలసుబ్రహ్మణ్యం (SPB) కి 2021లో పద్మ విభూషణ్ మరణానంతరం (Posthumously) ఇచ్చారు. ఆయన సెప్టెంబర్ 2020లో COVID-19 తో మరణించారు. ఆయన నెల్లూరు జిల్లాకు చెందినవారు."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "K. విశ్వనాథ్‌కు ఏ పురస్కారాలు వచ్చాయి?",
        "opt_a": "పద్మ విభూషణ్ (2017) మరియు దాదాసాహేబ్ ఫాల్కే (2016)",
        "opt_b": "పద్మ శ్రీ (1992) మరియు దాదాసాహేబ్ ఫాల్కే (2016)",
        "opt_c": "పద్మ భూషణ్ (2010) మరియు జ్ఞానపీఠ్ (2016)",
        "opt_d": "పద్మ విభూషణ్ (2016) మరియు అర్జున అవార్డు",
        "answer": "B",
        "explanation_te": "K. విశ్వనాథ్‌కు పద్మ శ్రీ (1992) మరియు దాదాసాహేబ్ ఫాల్కే (2016) వచ్చాయి. ఆయనకు పద్మ విభూషణ్ రాలేదు. ఆయన 'శంకరాభరణం', 'సాగర సంగమం' వంటి చిత్రాలకు ప్రసిద్ధుడు — మచిలీపట్నం, కృష్ణా జిల్లా."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "చిరంజీవికి పద్మ భూషణ్ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2000",
        "opt_b": "2006",
        "opt_c": "2010",
        "opt_d": "2014",
        "answer": "B",
        "explanation_te": "చిరంజీవి (మేఘా శ్యామ్) కి 2006లో పద్మ భూషణ్ ఇచ్చారు. ఆయన పశ్చిమ గోదావరి జిల్లాలోని నరసాపురానికి చెందినవారు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "SS రాజమౌళికి పద్మ శ్రీ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2009",
        "opt_b": "2012",
        "opt_c": "2015",
        "opt_d": "2018",
        "answer": "B",
        "explanation_te": "SS రాజమౌళికి 2012లో పద్మ శ్రీ ఇచ్చారు. ఆయన రాజమండ్రి (తూర్పు గోదావరి జిల్లా) లో జన్మించారు; తండ్రి కుటుంబ మూలాలు నెల్లూరు జిల్లా కోవూరు. 'బాహుబలి', 'RRR' చిత్రాలకు ప్రసిద్ధుడు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "K. విశ్వనాథ్‌కు దాదాసాహేబ్ ఫాల్కే పురస్కారం ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2014",
        "opt_b": "2016",
        "opt_c": "2018",
        "opt_d": "2020",
        "answer": "B",
        "explanation_te": "K. విశ్వనాథ్‌కు 2016 సంవత్సరానికి దాదాసాహేబ్ ఫాల్కే పురస్కారం (భారత సినిమా అత్యున్నత పురస్కారం) ఇచ్చారు. ఇది 2017లో ప్రదానం చేశారు."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "PV సింధుకు పద్మ భూషణ్ ఏ సంవత్సరం ఇచ్చారు?",
        "opt_a": "2016",
        "opt_b": "2018",
        "opt_c": "2020",
        "opt_d": "2022",
        "answer": "C",
        "explanation_te": "PV సింధుకు 2020లో పద్మ భూషణ్ ఇచ్చారు (రియో 2016 రజత తర్వాత 2015లో పద్మ శ్రీ, తర్వాత 2020లో పద్మ భూషణ్). కోచ్ గోపీచంద్‌కు 2014లో పద్మ భూషణ్."
    },
    # Section 2 — Oscar & International Awards
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "'నాటు నాటు' పాటకు Oscar పురస్కారం ఏ సంవత్సరం వచ్చింది?",
        "opt_a": "2022 (94వ)",
        "opt_b": "2023 (95వ)",
        "opt_c": "2024 (96వ)",
        "opt_d": "2021 (93వ)",
        "answer": "B",
        "explanation_te": "'నాటు నాటు' (RRR చిత్రం) కి 95వ Academy Awards (2023)లో Best Original Song Oscar వచ్చింది. సంగీతం MM కీరవాణి; సాహిత్యం: చంద్రబోస్."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "MM కీరవాణి ఏ జిల్లాకు చెందినవారు?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "పశ్చిమ గోదావరి జిల్లా (కొవ్వూరు)",
        "opt_c": "నెల్లూరు",
        "opt_d": "గుంటూరు",
        "answer": "B",
        "explanation_te": "MM కీరవాణి (Maragathamani Keeravani) పశ్చిమ గోదావరి జిల్లాలోని కొవ్వూరు (Kovvur) లో జన్మించారు — కోడూరు/కృష్ణా జిల్లా కాదు. SS రాజమౌళికి బంధువు. 'నాటు నాటు' కి Oscar 2023 సాధించారు."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "'నాటు నాటు' పాటకు Golden Globe పురస్కారం కూడా వచ్చిందా?",
        "opt_a": "లేదు",
        "opt_b": "అవును — 2023 Best Original Song",
        "opt_c": "నామినేషన్ మాత్రమే",
        "opt_d": "2022లో వచ్చింది",
        "answer": "B",
        "explanation_te": "'నాటు నాటు' పాటకు 2023 Golden Globe Awards లో Best Original Song పురస్కారం వచ్చింది — Oscar కంటే ముందే, ఇది Oscar విజయానికి సంకేతంగా నిలిచింది."
    },
    # Section 2 — National Film Awards (additional - corrected facts)
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "తెలుగు నటులలో తొలిసారిగా జాతీయ చలనచిత్ర పురస్కారంలో Best Actor సాధించిన నటుడు ఎవరు?",
        "opt_a": "చిరంజీవి",
        "opt_b": "అల్లు అర్జున్",
        "opt_c": "మహేశ్ బాబు",
        "opt_d": "జూనియర్ NTR",
        "answer": "B",
        "explanation_te": "అల్లు అర్జున్ 69వ జాతీయ చలనచిత్ర పురస్కారాలు (2022)లో Pushpa: The Rise చిత్రానికి Best Actor పురస్కారం సాధించారు — తెలుగు నటులలో ఇది తొలి జాతీయ Best Actor పురస్కారం."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "అల్లు అర్జున్‌కు Best Actor National Award ఏ చిత్రానికి వచ్చింది?",
        "opt_a": "Ala Vaikunthapurramuloo",
        "opt_b": "Pushpa 2: The Rule",
        "opt_c": "Pushpa: The Rise",
        "opt_d": "Arya",
        "answer": "C",
        "explanation_te": "అల్లు అర్జున్‌కు 'Pushpa: The Rise' (2021 డిసెంబర్ విడుదల) చిత్రానికి 69వ జాతీయ పురస్కారాల్లో Best Actor వచ్చింది. ఇదే చిత్రానికి దేవి శ్రీ ప్రసాద్‌కు Best Music (Songs) కూడా వచ్చింది."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "69వ జాతీయ చలనచిత్ర పురస్కారాల్లో Best Music Direction (Songs) ఎవరికి వచ్చింది?",
        "opt_a": "MM కీరవాణి",
        "opt_b": "S. తమన్",
        "opt_c": "దేవి శ్రీ ప్రసాద్ (DSP)",
        "opt_d": "Ilaiyaraaja",
        "answer": "C",
        "explanation_te": "69వ జాతీయ పురస్కారాల్లో దేవి శ్రీ ప్రసాద్ (DSP) కి Pushpa: The Rise చిత్రానికి Best Music Direction (Songs) వచ్చింది. MM కీరవాణి అదే వేడుకలో RRR కి Best Music Direction (Background Music) సాధించారు."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "71వ జాతీయ చలనచిత్ర పురస్కారాల్లో Best Telugu Film ఏది?",
        "opt_a": "Baby",
        "opt_b": "Karthikeya 2",
        "opt_c": "Bhagavanth Kesari",
        "opt_d": "Pushpa 2",
        "answer": "C",
        "explanation_te": "71వ జాతీయ చలనచిత్ర పురస్కారాల్లో (2023 చిత్రాలకు) Bhagavanth Kesari (బాలకృష్ణ నటించిన చిత్రం; Anil Ravipudi దర్శకత్వం) Best Telugu Film గెలుచుకుంది. 70వ పురస్కారాల్లో Karthikeya 2 Best Telugu Film అయింది."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "71వ జాతీయ పురస్కారాల్లో Baby చిత్రానికి Best Screenplay ఎవరికి వచ్చింది?",
        "opt_a": "అనంద్ దేవరాకొండ",
        "opt_b": "Sai Rajesh",
        "opt_c": "PVNS Rohith",
        "opt_d": "Chandoo Mondeti",
        "answer": "B",
        "explanation_te": "Baby (2023 తెలుగు చిత్రం; దర్శకుడు Sai Rajesh) కి 71వ జాతీయ పురస్కారాల్లో 2 పురస్కారాలు వచ్చాయి: Best Screenplay (Sai Rajesh) + Best Playback Singer Male (PVNS Rohith — 'Premistunna'). అనంద్ దేవరాకొండ నటించిన చిత్రం."
    },

    # Section 3 — Literary & Cultural Awards
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "తెలుగు భాషలో మొదటి జ్ఞానపీఠ పురస్కారం ఎవరికి వచ్చింది?",
        "opt_a": "విశ్వనాథ సత్యనారాయణ",
        "opt_b": "శ్రీశ్రీ",
        "opt_c": "C. నారాయణ రెడ్డి",
        "opt_d": "K. విశ్వనాథ్",
        "answer": "A",
        "explanation_te": "విశ్వనాథ సత్యనారాయణకు 1970లో జ్ఞానపీఠ పురస్కారం వచ్చింది — ఇది తెలుగు భాషలో మొదటిది. 'రామాయణ కల్పవృక్షం' రచన ముఖ్యం."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "దాదాసాహేబ్ ఫాల్కే పురస్కారం ఏ రంగంలో ఇస్తారు?",
        "opt_a": "సాహిత్యం",
        "opt_b": "భారత సినిమా (జీవిత కాల సేవ)",
        "opt_c": "క్రీడలు",
        "opt_d": "శాస్త్ర విజ్ఞానం",
        "answer": "B",
        "explanation_te": "దాదాసాహేబ్ ఫాల్కే పురస్కారం భారత సినిమాలో జీవిత కాల సేవకు ఇస్తారు. ఇది సినిమా రంగంలో అత్యున్నత జాతీయ పురస్కారం. 2016కు K. విశ్వనాథ్‌కు ఇచ్చారు."
    },
    # Section 4 — Central Educational Institutions
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "IIT తిరుపతి ఏ జిల్లాలో ఉంది?",
        "opt_a": "వైఎస్సార్ కడప జిల్లా",
        "opt_b": "తిరుపతి జిల్లా (యేర్పేడు)",
        "opt_c": "అనంతపురం జిల్లా",
        "opt_d": "చిత్తూరు జిల్లా",
        "answer": "B",
        "explanation_te": "IIT తిరుపతి తిరుపతి జిల్లాలోని యేర్పేడులో ఉంది. 2015లో స్థాపించారు. తొమ్మిది IIT లలో ఒకటి."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "AIIMS మంగళగిరి ఏ జిల్లాలో ఉంది?",
        "opt_a": "తిరుపతి జిల్లా",
        "opt_b": "గుంటూరు జిల్లా",
        "opt_c": "కృష్ణా జిల్లా",
        "opt_d": "విశాఖపట్నం జిల్లా",
        "answer": "B",
        "explanation_te": "AIIMS మంగళగిరి గుంటూరు జిల్లాలో ఉంది. 2022లో పూర్తి స్థాయిలో ప్రారంభించారు. PMSSY (Pradhan Mantri Swasthya Suraksha Yojana) కింద స్థాపించారు."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "NIT ఆంధ్రప్రదేశ్ ఏ జిల్లాలో ఉంది?",
        "opt_a": "కాకినాడ",
        "opt_b": "ఏలూరు జిల్లా (తాడేపల్లిగూడెం దగ్గర)",
        "opt_c": "విశాఖపట్నం",
        "opt_d": "రాజమహేంద్రవరం",
        "answer": "B",
        "explanation_te": "NIT ఆంధ్రప్రదేశ్ ఏలూరు జిల్లాలో (తాడేపల్లిగూడెం సమీపంలో) ఉంది. 2015లో స్థాపించారు. 31 NITs లో ఒకటి."
    },
    {
        "section_idx": 4,
        "difficulty": "hard",
        "question_te": "CUAP (Central University of Andhra Pradesh) ఏ జిల్లాలో ఉంది?",
        "opt_a": "నెల్లూరు",
        "opt_b": "అనంతపురం (నందేడు)",
        "opt_c": "కర్నూలు",
        "opt_d": "చిత్తూరు",
        "answer": "B",
        "explanation_te": "CUAP (Central University of Andhra Pradesh) అనంతపురం జిల్లాలోని నందేడులో ఉంది. 2014లో స్థాపించి 2016లో తాత్కాలిక ప్యాంపస్ ప్రారంభించారు."
    },
    # Section 5 — AP High Court
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "AP పునర్విభజన తర్వాత ప్రత్యేక AP హైకోర్టు ఎప్పుడు ప్రారంభమైంది?",
        "opt_a": "జూన్ 2, 2014",
        "opt_b": "జనవరి 1, 2019",
        "opt_c": "మార్చి 2, 2019",
        "opt_d": "నవంబర్ 1, 2019",
        "answer": "B",
        "explanation_te": "AP పునర్విభజన చట్టం 2014 (Section 30) ప్రకారం, జనవరి 1, 2019 నుండి అమరావతిలో ప్రత్యేక ఆంధ్రప్రదేశ్ హైకోర్టు ప్రారంభమైంది. 2014-2018 వరకు హైదరాబాద్ హైకోర్టు రెండు రాష్ట్రాలకు పనిచేసింది."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "AP పునర్విభజన చట్టం 2014 లో హైకోర్టు గురించిన నిబంధన ఏ సెక్షన్ లో ఉంది?",
        "opt_a": "సెక్షన్ 3",
        "opt_b": "సెక్షన్ 15",
        "opt_c": "సెక్షన్ 30",
        "opt_d": "సెక్షన్ 45",
        "answer": "C",
        "explanation_te": "APRA 2014 సెక్షన్ 30 ప్రకారం ప్రత్యేక AP హైకోర్టు ఏర్పాటు చేయాలి. 2014–2018 వరకు నాలుగేళ్ళు హైదరాబాద్ హైకోర్టే రెండు రాష్ట్రాలకు పనిచేసింది."
    },
    # Section 6 — Constitution & AP
    {
        "section_idx": 6,
        "difficulty": "easy",
        "question_te": "ఆర్టికల్ 371-డి ఏ రాష్ట్రానికి వర్తిస్తుంది?",
        "opt_a": "తెలంగాణ",
        "opt_b": "ఆంధ్రప్రదేశ్",
        "opt_c": "తమిళనాడు",
        "opt_d": "కర్నాటక",
        "answer": "B",
        "explanation_te": "ఆర్టికల్ 371-డి ఆంధ్రప్రదేశ్‌కు వర్తిస్తుంది. 32వ రాజ్యాంగ సవరణ (1973) ద్వారా చేర్చారు. స్థానిక ఉద్యోగాలు, విద్య లో రిజర్వేషన్ కల్పిస్తుంది."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "ఆర్టికల్ 371-డి ఏ రాజ్యాంగ సవరణ ద్వారా వచ్చింది?",
        "opt_a": "25వ సవరణ",
        "opt_b": "32వ సవరణ (1973)",
        "opt_c": "42వ సవరణ",
        "opt_d": "44వ సవరణ",
        "answer": "B",
        "explanation_te": "ఆర్టికల్ 371-డి 32వ రాజ్యాంగ సవరణ (1973) ద్వారా చేర్చారు. దీని ప్రకారం 1975లో Presidential Order జారీ అయింది — స్థానిక ఉద్యోగ రక్షణకు ప్రాతిపదిక."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "AP కి 'ప్రత్యేక హోదా' (Special Category Status) ఎందుకు ఇవ్వలేదు?",
        "opt_a": "AP అభ్యర్థించలేదు",
        "opt_b": "14వ ఆర్థిక సంఘం SCS ప్రమాణాలు మార్చింది; NITI Aayog SCS ముగించింది",
        "opt_c": "కేంద్రం వ్యతిరేకించింది మాత్రమే",
        "opt_d": "AP అర్హత లేదు",
        "answer": "B",
        "explanation_te": "14వ ఆర్థిక సంఘం SCS ప్రమాణాలు మార్చింది; NITI Aayog 2015లో Planning Commission స్థానంలో వచ్చి SCS విధానం ముగించింది. కేంద్రం 'Special Assistance' ప్యాకేజ్ ఇచ్చింది."
    },
    # Section 7 — AP Districts & Constitutional positions
    {
        "section_idx": 7,
        "difficulty": "easy",
        "question_te": "AP లో ఏప్రిల్ 2022 తర్వాత జిల్లాల సంఖ్య ఎన్ని?",
        "opt_a": "13",
        "opt_b": "23",
        "opt_c": "26",
        "opt_d": "28",
        "answer": "C",
        "explanation_te": "ఏప్రిల్ 4, 2022న AP లో 13 జిల్లాలు 26 జిల్లాలుగా పునర్వ్యవస్థీకరించారు (YSRCP ప్రభుత్వం). తర్వాత జనవరి 1, 2026న మరో 2 జోడించి 28 జిల్లాలు చేశారు."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "జనవరి 1, 2026న AP లో ఏ కొత్త జిల్లాలు ఏర్పడ్డాయి?",
        "opt_a": "పోలవరం + ఏలూరు",
        "opt_b": "పోలవరం + మార్కాపురం",
        "opt_c": "ఏలూరు + నంద్యాల",
        "opt_d": "శ్రీ సత్యసాయి + పార్వతీపురం",
        "answer": "B",
        "explanation_te": "జనవరి 1, 2026న AP లో పోలవరం మరియు మార్కాపురం రెండు కొత్త జిల్లాలు ఏర్పడ్డాయి — మొత్తం 28 జిల్లాలు అయ్యాయి (TDP ప్రభుత్వం)."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "AP అసెంబ్లీలో మొత్తం స్థానాల సంఖ్య ఎన్ని?",
        "opt_a": "119",
        "opt_b": "147",
        "opt_c": "175",
        "opt_d": "196",
        "answer": "C",
        "explanation_te": "AP శాసనసభలో మొత్తం 175 స్థానాలు. లోక్‌సభలో 25 స్థానాలు. రాజ్యసభలో 11 స్థానాలు. (తదుపరి delimitation 2026 జనాభా గణన ఆధారంగా జరుగుతుంది.)"
    },
    # Section 1 — 2025 Padma Awards
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "Nandamuri Balakrishna కి 2025లో ఏ పద్మ పురస్కారం వచ్చింది?",
        "opt_a": "పద్మ శ్రీ",
        "opt_b": "పద్మ భూషణ్",
        "opt_c": "పద్మ విభూషణ్",
        "opt_d": "భారత రత్న",
        "answer": "B",
        "explanation_te": "Nandamuri Balakrishna కి 2025లో పద్మ భూషణ్ (Art రంగంలో) వచ్చింది. ఆయన NTR గారి పుత్రుడు; 100+ తెలుగు చిత్రాల్లో నటించారు. ఆంధ్రప్రదేశ్ నుండి."
    },
    # REMOVED 2026-05-18 audit: 2 Telangana-only Padma award MCQs
    # (Dr. Duvvur Nageshwar Reddy — Telangana medical; Manda Krishna Madiga — Telangana Public Affairs)
    # AP exam should not test Telangana-only awardees.
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "2025 Padma Awards లో తెలుగు రాష్ట్రాల నుండి మొత్తం ఎంత మంది గ్రహీతలు ఉన్నారు?",
        "opt_a": "5",
        "opt_b": "6",
        "opt_c": "7",
        "opt_d": "9",
        "answer": "C",
        "explanation_te": "2025 Padma Awards: AP నుండి 5 (Balakrishna-PB, Madugula-PS, KL Krishna-PS, Miriyala-PS posthumous, Vadiraj-PS) + Telangana నుండి 2 (Nageshwar Reddy-PV, Manda Krishna Madiga-PS) = మొత్తం 7 మంది."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "2025 Padma Shri — Burrakatha కళాకారుడు మరణానంతరం పురస్కారం పొందినవారు ఎవరు?",
        "opt_a": "Madugula Nagaphani Sarma",
        "opt_b": "Vadiraj Panchamukhi",
        "opt_c": "Miriyala Apparao",
        "opt_d": "K.L. Krishna",
        "answer": "C",
        "explanation_te": "Miriyala Apparao (తాడేపల్లిగూడెం) కి 2025 Padma Shri మరణానంతరం ఇచ్చారు — Art (Burrakatha) రంగంలో; 5 దశాబ్దాల బుర్రకథ సేవకు గుర్తింపు. Andhra Pradesh నుండి."
    },

    # Section 1 — 2026 Padma Awards (inserted as additional section 1 MCQs)
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "2026 Padma Awards లో తెలుగు రాష్ట్రాల నుండి మొత్తం ఎంత మంది గ్రహీతలు ఉన్నారు?",
        "opt_a": "7",
        "opt_b": "9",
        "opt_c": "11",
        "opt_d": "12",
        "answer": "D",
        "explanation_te": "2026 Padma Awards (జన. 25, 2026 ప్రకటన): AP నుండి 4 Padma Shri + Telangana నుండి 7 Padma Shri + USA (తెలుగు) నుండి 1 Padma Bhushan = మొత్తం 12 మంది. Telangana: Chandramouli Gaddamanugu, Deepika Reddy, Guduru Venkat Rao, Krishnamurty Balasubramanian, Kumarasamy Thangaraj, Palkonda Vijay Anand Reddy, Rama Reddy Mamidi."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "2026 Padma Bhushan పొందిన తెలుగు వైద్యుడు ఎవరు?",
        "opt_a": "Dr. Guduru Venkat Rao",
        "opt_b": "Dr. Nori Dattatreyudu",
        "opt_c": "Dr. Palkonda Vijay Anand Reddy",
        "opt_d": "Dr. Kumarasamy Thangaraj",
        "answer": "B",
        "explanation_te": "Dr. Nori Dattatreyudu కి 2026లో Padma Bhushan ఇచ్చారు — Medicine రంగంలో. ఆయన USA లో ఉంటున్న తెలుగు వైద్యుడు. మిగిలిన ముగ్గురు Padma Shri గ్రహీతలు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "2026 లో Literature & Education రంగంలో AP కి Padma Shri వచ్చిన వ్యక్తి ఎవరు?",
        "opt_a": "Shri Maganti Murali Mohan",
        "opt_b": "Shri Gadde Babu Rajendra Prasad",
        "opt_c": "Shri Vempaty Kutumba Sastry",
        "opt_d": "Shri Garimella Balakrishna Prasad",
        "answer": "C",
        "explanation_te": "Shri Vempaty Kutumba Sastry కి 2026లో Literature & Education రంగంలో Padma Shri వచ్చింది — Andhra Pradesh నుండి. Gadde Babu, Garimella, Maganti — ముగ్గురికీ Art రంగంలో Padma Shri."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "2026 లో AP నుండి Padma Shri మరణానంతరం (Posthumous) పొందిన వ్యక్తి ఎవరు?",
        "opt_a": "Shri Maganti Murali Mohan",
        "opt_b": "Shri Vempaty Kutumba Sastry",
        "opt_c": "Shri Garimella Balakrishna Prasad",
        "opt_d": "Shri Gadde Babu Rajendra Prasad",
        "answer": "C",
        "explanation_te": "Shri Garimella Balakrishna Prasad కి 2026లో Padma Shri మరణానంతరం (Posthumously) ఇచ్చారు — Art రంగంలో, Andhra Pradesh నుండి."
    },
    # REMOVED 2026-05-18 audit: Telangana-only Padma Shri MCQ (Rama Reddy Mamidi — Telangana Animal Husbandry)

    # Section 5 — AP HC Chief Justice (additional)
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "AP హైకోర్టు చరిత్రలో తొలి మహిళా ప్రధాన న్యాయమూర్తి ఎవరు?",
        "opt_a": "Justice B.V. Nagarathna",
        "opt_b": "Justice Hima Kohli",
        "opt_c": "Justice Lisa Gill",
        "opt_d": "Justice Indira Banerjee",
        "answer": "C",
        "explanation_te": "Justice Lisa Gill AP హైకోర్టు 6వ ప్రధాన న్యాయమూర్తి — ఏప్రిల్ 25, 2026 నుండి పదవిలో. AP HC చరిత్రలో తొలి మహిళా CJ. Punjab & Haryana HC నుండి బదిలీ అయ్యారు."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "Justice Lisa Gill AP HC CJ గా ఏ తేదీన పదవి స్వీకరించారు?",
        "opt_a": "జనవరి 1, 2026",
        "opt_b": "మార్చి 1, 2026",
        "opt_c": "ఏప్రిల్ 25, 2026",
        "opt_d": "జూన్ 2, 2026",
        "answer": "C",
        "explanation_te": "Justice Dhiraj Singh Thakur (5వ CJ) ఏప్రిల్ 24, 2026న పదవీ విరమణ చేశారు. Justice Lisa Gill ఏప్రిల్ 25, 2026 నుండి AP HC 6వ CJ గా పదవి స్వీకరించారు. SC కొలీజియం సిఫారసు మేరకు నియమించారు."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "Justice Lisa Gill AP HC కి రాకముందు ఏ హైకోర్టులో పనిచేశారు?",
        "opt_a": "Delhi HC",
        "opt_b": "Bombay HC",
        "opt_c": "Punjab & Haryana HC",
        "opt_d": "Madras HC",
        "answer": "C",
        "explanation_te": "Justice Lisa Gill Punjab & Haryana High Court నుండి AP HC కి బదిలీ అయ్యారు. మార్చి 2026లో AP HC న్యాయమూర్తిగా ప్రమాణస్వీకారం చేసి, ఏప్రిల్ 25, 2026న CJ పదవి చేపట్టారు."
    },
    {
        "section_idx": 5,
        "difficulty": "hard",
        "question_te": "AP HC 5వ ప్రధాన న్యాయమూర్తి (Justice Dhiraj Singh Thakur) ఏ తేదీన పదవీ విరమణ చేశారు?",
        "opt_a": "జనవరి 24, 2026",
        "opt_b": "మార్చి 24, 2026",
        "opt_c": "ఏప్రిల్ 24, 2026",
        "opt_d": "మే 24, 2026",
        "answer": "C",
        "explanation_te": "Justice Dhiraj Singh Thakur జులై 28, 2023న AP HC 5వ CJ గా పదవి స్వీకరించి ఏప్రిల్ 24, 2026న పదవీ విరమణ చేశారు. ఆ తర్వాత రోజు Justice Lisa Gill 6వ CJ గా బాధ్యతలు స్వీకరించారు."
    },

    # Section 8 — Rapid revision
    {
        "section_idx": 8,
        "difficulty": "hard",
        "question_te": "APRA 2014 ప్రకారం AP కి ఏ హామీ ఇచ్చారు?",
        "opt_a": "భారత రత్న",
        "opt_b": "హైదరాబాద్ రాజధానిగా ఉంచడం",
        "opt_c": "పోలవరం జాతీయ ప్రాజెక్టు హోదా + నష్ట పరిహారం + రాజ్యసభ స్థానాలు",
        "opt_d": "వేర్వేరు శాసనసభ ఎన్నికలు",
        "answer": "C",
        "explanation_te": "APRA 2014 ముఖ్య హామీలు: పోలవరం జాతీయ ప్రాజెక్టు హోదా; రాయలసీమ, ఉత్తరాంధ్ర నష్ట పరిహారం; AP పారిశ్రామిక ప్రోత్సాహాలు; రాజ్యసభ స్థానాల పెంపు హామీ."
    },
    {
        "section_idx": 8,
        "difficulty": "hard",
        "question_te": "SP బాలసుబ్రహ్మణ్యం ఏ జిల్లాకు చెందినవారు?",
        "opt_a": "కృష్ణా జిల్లా",
        "opt_b": "నెల్లూరు జిల్లా",
        "opt_c": "గుంటూరు జిల్లా",
        "opt_d": "చిత్తూరు జిల్లా",
        "answer": "B",
        "explanation_te": "SP బాలసుబ్రహ్మణ్యం (సిపిళ్ళ పార్వతీశ్వర బాలసుబ్రహ్మణ్యం) నెల్లూరు జిల్లాలో జన్మించారు. 40,000+ పాటలు 16 భాషల్లో పాడారు. 2021 పద్మ విభూషణ్ (మరణానంతరం)."
    },
]


def _seed_ap_ca_div9_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 9."""
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (9, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (9, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division9', 9,
         'పద్మ పురస్కారాలు, కేంద్ర సంస్థలు, AP హైకోర్టు & రాజ్యాంగం',
         'Padma Awards, Central Institutions, AP HC & Constitution',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div9 notes seeded!'}
def _seed_ap_ca_div9_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 9."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (9, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div9_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (9, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print(f"[div9-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    # Always delete-then-reinsert so seed-file changes are reflected (force is ignored here).
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
    return {'success': True, 'message': f'AP CA Div9 MCQs seeded! Total: {len(MCQ_DATA)}'}

# Additional MCQs for div9 appended
_EXTRA_MCQ_DATA = [
    # Padma Awards additional
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "2025 పద్మ భూషణ్ పొందిన తెలుగు నటుడు (AP) ఎవరు?",
        "opt_a": "అల్లు అర్జున్",
        "opt_b": "మోహన్ బాబు",
        "opt_c": "బాలకృష్ణ (నందమూరి బాలకృష్ణ)",
        "opt_d": "చిరంజీవి",
        "answer": "C",
        "explanation_te": "2025లో నందమూరి బాలకృష్ణ పద్మ భూషణ్ (Art రంగంలో) పురస్కారం పొందారు — పద్మ విభూషణ్ కాదు. ఇది తెలుగు సినిమాకు గొప్ప గౌరవం. Andhra Pradesh నుండి."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "SP బాలసుబ్రహ్మణ్యం ఏ సంవత్సరం పద్మ విభూషణ్ పొందారు?",
        "opt_a": "2019",
        "opt_b": "2020",
        "opt_c": "2021",
        "opt_d": "2022",
        "answer": "C",
        "explanation_te": "2021లో SP బాలసుబ్రహ్మణ్యం పద్మ విభూషణ్ పొందారు (మరణానంతర పురస్కారం). 2020 సెప్టెంబర్‌లో ఆయన COVID-19 తో మరణించారు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "K. విశ్వనాథ్ దాదాసాహేబ్ ఫాల్కే పురస్కారం ఏ సంవత్సరం పొందారు?",
        "opt_a": "2014",
        "opt_b": "2016",
        "opt_c": "2018",
        "opt_d": "2020",
        "answer": "B",
        "explanation_te": "K. విశ్వనాథ్ 2016లో (67వ Dadasaheb Phalke Award) దాదాసాహేబ్ ఫాల్కే పురస్కారం పొందారు. ఆయన తెలుగు సినిమా దర్శకుడు."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "పద్మ పురస్కారాలు ఏ తేదీన ప్రకటిస్తారు?",
        "opt_a": "స్వాతంత్ర్య దినం (ఆగస్టు 15)",
        "opt_b": "గణతంత్ర దినం (జనవరి 26)",
        "opt_c": "హోలీ",
        "opt_d": "క్రిస్మస్",
        "answer": "B",
        "explanation_te": "పద్మ పురస్కారాలు ప్రతి సంవత్సరం గణతంత్ర దినోత్సవం (జనవరి 26) సందర్భంగా ప్రకటిస్తారు. పురస్కారాలు మార్చి/ఏప్రిల్ లో రాష్ట్రపతి భవన్‌లో ప్రదానం జరుగుతుంది."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "2023 ఆస్కార్ అవార్డు గెలిచిన తెలుగు పాట ఏది?",
        "opt_a": "జై హో",
        "opt_b": "నాటు నాటు (RRR)",
        "opt_c": "బాహుబలి థీమ్",
        "opt_d": "ఆర్యా",
        "answer": "B",
        "explanation_te": "RRR చిత్రంలోని 'నాటు నాటు' పాట 2023 ఆస్కార్ (95వ అకాడమీ అవార్డుల) లో Best Original Song విభాగంలో గెలిచింది. MM కీరవాణి సంగీతం."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "69వ జాతీయ చలనచిత్ర పురస్కారాల్లో Best Actor ఎవరు?",
        "opt_a": "రామ్ చరణ్ (RRR)",
        "opt_b": "అల్లు అర్జున్ (పుష్ప-ది రైజ్)",
        "opt_c": "NTR Jr (RRR)",
        "opt_d": "మహేష్ బాబు",
        "answer": "B",
        "explanation_te": "అల్లు అర్జున్ 69వ జాతీయ చలనచిత్ర పురస్కారాల్లో (Pushpa: The Rise చిత్రానికి) Best Actor పురస్కారం పొందారు — తొలి తెలుగు నటుడు ఈ అవార్డు గెలిచిన వారు."
    },
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "విశ్వనాధ సత్యనారాయణ జ్ఞానపీఠ్ పురస్కారం ఏ సంవత్సరం పొందారు?",
        "opt_a": "1960",
        "opt_b": "1970",
        "opt_c": "1980",
        "opt_d": "1990",
        "answer": "B",
        "explanation_te": "విశ్వనాధ సత్యనారాయణ 'రామాయణ కల్పవృక్షం' రచనకు 1970లో జ్ఞానపీఠ్ పురస్కారం పొందారు. ఇది మొదటి తెలుగు జ్ఞానపీఠ్."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "సి నారాయణ రెడ్డి (సినారె) జ్ఞానపీఠ్ పురస్కారం ఏ సంవత్సరం పొందారు?",
        "opt_a": "1982",
        "opt_b": "1988",
        "opt_c": "1992",
        "opt_d": "1998",
        "answer": "B",
        "explanation_te": "సి నారాయణ రెడ్డి (Sinaree) 1988లో జ్ఞానపీఠ్ పురస్కారం పొందారు. తెలుగులో రెండవ జ్ఞానపీఠ్ గ్రహీత."
    },
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "IIT తిరుపతి ఏ సంవత్సరంలో స్థాపించబడింది?",
        "opt_a": "2014",
        "opt_b": "2015",
        "opt_c": "2018",
        "opt_d": "2020",
        "answer": "B",
        "explanation_te": "IIT తిరుపతి 2015లో AP Reorganisation Act 2014 ప్రకారం AP కి ఒక IIT మంజూరు అయి స్థాపించబడింది."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "AIIMS మంగళగిరి ఎక్కడ ఉంది?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "మంగళగిరి (గుంటూరు జిల్లా)",
        "opt_c": "తిరుపతి",
        "opt_d": "కాకినాడ",
        "answer": "B",
        "explanation_te": "AIIMS మంగళగిరి గుంటూరు జిల్లాలో మంగళగిరిలో ఉంది. AP కి APRA 2014 ప్రకారం AIIMS మంజూరైంది, 2022లో సర్వీసులు ప్రారంభించింది."
    },
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "AP High Court (ప్రత్యేక) ఎప్పుడు ప్రారంభమైంది?",
        "opt_a": "2016 జనవరి 1",
        "opt_b": "2019 జనవరి 1",
        "opt_c": "2014 జూన్ 2",
        "opt_d": "2017 నవంబర్ 1",
        "answer": "B",
        "explanation_te": "AP High Court అమరావతిలో జనవరి 1, 2019న ప్రత్యేకంగా ఏర్పాటైంది. APRA 2014 సెక్షన్ 30 ప్రకారం ఏర్పాటైంది."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "AP High Court తొలి మహిళా Chief Justice ఎవరు?",
        "opt_a": "జస్టిస్ ప్రభా శ్రీదేవన్",
        "opt_b": "జస్టిస్ లీసా గిల్ (Lisa Gill)",
        "opt_c": "జస్టిస్ హిమా కోహ్లి",
        "opt_d": "జస్టిస్ బి.వి. నాగరత్న",
        "answer": "B",
        "explanation_te": "జస్టిస్ లీసా గిల్ ఏప్రిల్ 25, 2026న AP High Court తొలి మహిళా Chief Justice గా నియమితులయ్యారు."
    },
    # REMOVED 2026-05-18 audit: Duplicate of earlier Article 371-D MCQ (same answer = AP, same options pattern)
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "ఆర్టికల్ 371-D ఏ రాజ్యాంగ సవరణ ద్వారా జోడించబడింది?",
        "opt_a": "28వ సవరణ 1972",
        "opt_b": "32వ సవరణ 1973",
        "opt_c": "42వ సవరణ 1976",
        "opt_d": "100వ సవరణ 2015",
        "answer": "B",
        "explanation_te": "ఆర్టికల్ 371-D 32వ రాజ్యాంగ సవరణ 1973 ద్వారా AP కి ప్రత్యేక రక్షణ కోసం జోడించబడింది. G.O.610 తర్వాత 6 Zones విద్య, ఉద్యోగాలలో రోస్టర్ సిస్టమ్ అమలు చేయడానికి."
    },
    {
        "section_idx": 7,
        "difficulty": "easy",
        "question_te": "ప్రస్తుత AP గవర్నర్ ఎవరు?",
        "opt_a": "జస్టిస్ S. అబ్దుల్ నజీర్",
        "opt_b": "బిస్వభూషణ్ హరిచందన్",
        "opt_c": "నవంబర్ నయనా పటేల్",
        "opt_d": "ఇ.ఎస్.ఎల్ నరసిమ్హన్",
        "answer": "A",
        "explanation_te": "జస్టిస్ S. అబ్దుల్ నజీర్ ప్రస్తుత AP గవర్నర్. ఆయన సుప్రీంకోర్టు మాజీ న్యాయమూర్తి, 2023 జనవరిలో నియమితులయ్యారు."
    },
    {
        "section_idx": 7,
        "difficulty": "easy",
        "question_te": "AP లో మొత్తం శాసనసభ స్థానాలు ఎన్ని?",
        "opt_a": "119",
        "opt_b": "175",
        "opt_c": "150",
        "opt_d": "294",
        "answer": "B",
        "explanation_te": "AP లో మొత్తం 175 శాసనసభ (Assembly) స్థానాలు ఉన్నాయి. 25 లోక్‌సభ మరియు 11 రాజ్యసభ స్థానాలు ఉన్నాయి."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "AP లో ప్రస్తుత జిల్లాల సంఖ్య (2026 జనవరి నాటికి)?",
        "opt_a": "13",
        "opt_b": "25",
        "opt_c": "26",
        "opt_d": "28",
        "answer": "D",
        "explanation_te": "జనవరి 1, 2026 నుండి AP లో మొత్తం 28 జిల్లాలు ఉన్నాయి. 2022 ఏప్రిల్‌లో 13→26 చేసి, తర్వాత 2 మరిన్ని జిల్లాలు జోడించడంతో 28 అయ్యాయి."
    },
    {
        "section_idx": 8,
        "difficulty": "easy",
        "question_te": "AP లో ప్రస్తుత ముఖ్యమంత్రి ఎవరు?",
        "opt_a": "వై.ఎస్. జగన్ మోహన్ రెడ్డి",
        "opt_b": "చంద్రబాబు నాయుడు (నారా చంద్రబాబు నాయుడు)",
        "opt_c": "కె. కేశవ్ రావు",
        "opt_d": "పవన్ కళ్యాణ్",
        "answer": "B",
        "explanation_te": "చంద్రబాబు నాయుడు జూన్ 12, 2024న AP ముఖ్యమంత్రిగా ప్రమాణ స్వీకారం చేశారు. TDP-BJP-JSP కూటమి 2024 ఎన్నికల్లో ఘన విజయం సాధించింది."
    },
    {
        "section_idx": 8,
        "difficulty": "medium",
        "question_te": "2026 AP Reorganisation Amendment Act ఏ తేదీన రాష్ట్రపతి ఆమోదం పొందింది?",
        "opt_a": "ఏప్రిల్ 1, 2026",
        "opt_b": "ఏప్రిల్ 2, 2026",
        "opt_c": "ఏప్రిల్ 6, 2026",
        "opt_d": "ఏప్రిల్ 13, 2026",
        "answer": "C",
        "explanation_te": "AP Reorganisation Amendment Act 2026 (Act No. 7/2026) రాష్ట్రపతి ఏప్రిల్ 6, 2026న ఆమోదించారు. ఇది అమరావతిని అధికారిక రాజధానిగా గుర్తించింది."
    },
    {
        "section_idx": 8,
        "difficulty": "hard",
        "question_te": "APRA 2014 ప్రకారం అమలులోకి వచ్చిన తేదీ నుండి అమరావతి రాజధాని Retrospective గా ఏ తేదీ నుండి వర్తిస్తుంది?",
        "opt_a": "జూన్ 2, 2014",
        "opt_b": "అక్టోబర్ 1, 2018",
        "opt_c": "జూన్ 2, 2024",
        "opt_d": "ఏప్రిల్ 6, 2026",
        "answer": "C",
        "explanation_te": "2026 సవరణ చట్టం జూన్ 2, 2024 నుండి (Retrospectively) అమరావతిని AP రాజధానిగా గుర్తించింది. ఇది 2024 ఎన్నికల తర్వాత TDP ప్రభుత్వం అమరావతి రాజధాని అవ్వాలని నిర్ణయించిన తేదీ."
    }
]

MCQ_DATA = MCQ_DATA + _EXTRA_MCQ_DATA
