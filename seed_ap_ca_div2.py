"""
seed_ap_ca_div2.py — AP Current Affairs Division 2: TDP-BJP-JSP Government Schemes
ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ — విభాగం 2: ప్రభుత్వ పథకాలు 2024-2026

AUDIT CHANGES (2026-05-18):
1. REMOVED 22 junk MCQs with question text 'తెలుగు ప్రశ్న?' and literal
   single-letter options a/b/c/d — these had no meaningful question text.
2. FIXED wrong correct_answer: 'తల్లికి వందనం నెలకు ఎంత?' —
   was "b" (₹1,250/month), corrected to "b" which is numerically correct
   (₹15,000 ÷ 12 = ₹1,250). Answer kept but noted that the official
   communication is ₹15,000/year not monthly; question corrected to annual.
3. FIXED invented fact: '3 నెలల సమయం' for Deepam 2.0 cylinder delivery wait —
   replaced with correct fact: 48 గంటలు (48 hours) refund per div02 HTML.
   Source: div02_govt_schemes.html ground truth.

BATCH D3 AUDIT (2026-05-18):
4. REWROTE "Super Six గ్రామీణ అభివృద్ధి పథకం" MCQ — had gibberish options
   ("రంగుల్ సుఖం", "కర్మ పథకం", "NTR చేపూ"). Now asks the 3 target groups.
5. REWROTE "Deepam 2.0 lo '2.0' name reason" — had filler options that all
   converged to same answer. Now asks about TDP 2014-19 → 2024 re-launch.
6. REWROTE "నిరుద్యోగ బృతి విభాగం" — fabricated department "సమాజ సంఘం".
   Replaced with the real fact: ₹3,000/month for unemployed.
7. REWROTE "అన్నదాత సుఖీభవ నమోదు ఎక్కడ?" — had gibberish options
   ("రిటి నిర్గమన చేయండి", "అలీ పత్ర నిర్ణయం"). Now lists the real channels.
8. REWROTE "అన్నా కేంటీన్ daily beneficiaries" — unsourced "50,000-100,000"
   figure. Now asks about the ₹5/meal price (officially documented).
9. REWROTE "Super Six fund allocation" word-salad — now asks how many of the
   6 schemes are women-centric (3).
10. REMOVED "Super Six 2026 budget ₹1,50,000 cr" — unsourced fabricated figure.
"""
import json as _json

SECTIONS_JSON = [
    {
        "title": "సూపర్ సిక్స్ హామీలు — పరిచయం",
        "sub": "Super Six Guarantees — Introduction",
        "audio": "TDP-JSP-BJP కూటమి 2024 ఎన్నికల్లో ఇచ్చిన 6 హామీలు 'సూపర్ సిక్స్' అని పిలుస్తారు. 1. దీపం 2.0 (LPG సిలిండర్లు). 2. ఉచిత బస్సు ప్రయాణం (మహిళలకు). 3. నిరుద్యోగ బృతి (₹3,000/నెల). 4. అన్నదాత సుఖీభవ (రైతులకు ₹20,000). 5. తల్లికి వందనం (విద్యార్థుల తల్లులకు ₹15,000). 6. ఆడబిడ్డ నిధి (మహిళలకు ₹1,500/నెల).",
        "html": """<div class="concept-cover">
  <h1>Super Six Guarantees &nbsp;<span class="bi-te">/ సూపర్ సిక్స్ హామీలు</span></h1>
  <div class="sub">TDP-JSP-BJP alliance manifesto • 6 flagship welfare promises • Rolled out 2024-26</div>
</div>

<div class="section-hdr">The Six Guarantees / ఆరు హామీలు</div>
<table class="key-table">
<tr><th>#</th><th>Scheme (English)</th><th class="bi-te">పథకం</th><th>Benefit</th></tr>
<tr><td>1</td><td><b>Deepam 2.0</b></td><td class="bi-te">దీపం 2.0</td><td>3 free LPG cylinders / year</td></tr>
<tr><td>2</td><td><b>Free Bus Travel</b> (Stree Shakti)</td><td class="bi-te">ఉచిత బస్సు / స్త్రీ శక్తి</td><td>Free APSRTC for women + transgender</td></tr>
<tr><td>3</td><td><b>Nirudyoga Bruthi</b></td><td class="bi-te">నిరుద్యోగ బృతి</td><td>₹3,000 / month unemployment allowance</td></tr>
<tr><td>4</td><td><b>Annadata Sukhibhava</b></td><td class="bi-te">అన్నదాత సుఖీభవ</td><td>₹20,000 / year to farmers (with PM-KISAN)</td></tr>
<tr><td>5</td><td><b>Talliki Vandanam</b></td><td class="bi-te">తల్లికి వందనం</td><td>₹15,000 / year to student's mother</td></tr>
<tr><td>6</td><td><b>Aadabidda Nidhi</b></td><td class="bi-te">ఆడబిడ్డ నిధి</td><td>₹1,500 / month (₹18,000/yr) to women</td></tr>
</table>

<div class="section-hdr">Target Groups / లక్షిత వర్గాలు</div>
<table class="key-table">
<tr><th>Group</th><th>Schemes covering them</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Women</td><td>Free Bus, Talliki Vandanam, Aadabidda Nidhi</td><td class="bi-te">3 మహిళా-కేంద్రిత పథకాలు</td></tr>
<tr><td>Farmers</td><td>Annadata Sukhibhava</td><td class="bi-te">రైతులు</td></tr>
<tr><td>Unemployed youth</td><td>Nirudyoga Bruthi</td><td class="bi-te">నిరుద్యోగ యువత</td></tr>
<tr><td>All eligible households</td><td>Deepam 2.0 (LPG)</td><td class="bi-te">అన్ని అర్హ కుటుంబాలు</td></tr>
</table>

<p><b>Political context:</b> The Super Six were launched during the TDP-JSP-BJP 2024 election campaign as a direct response to the YSRCP's "Navaratnalu" welfare suite. Each TDP scheme has an analogue: YSR Pension Kanuka → NTR Bharosa, YSR Amma Vodi → Talliki Vandanam, YSR Rythu Bharosa → Annadata Sukhibhava. Implementation has been staggered between Aug 2024 and 2026, anchored on symbolic dates (Independence Day, AP Foundation Day, govt anniversary).</p>
<p class="bi-te">సూపర్ సిక్స్ హామీలు 2024 ఎన్నికల ముందు YSRCP నవరత్నాలకు సమాధానంగా ప్రకటించారు. ప్రతి పథకం YSRCP స్కీమ్‌కు ప్రత్యామ్నాయం — YSR పెన్షన్ → NTR భరోసా, YSR అమ్మ వొడి → తల్లికి వందనం, YSR రైతు భరోసా → అన్నదాత సుఖీభవ. 2024 ఆగస్టు నుండి 2026 వరకు దశలవారీగా అమలు.</p>"""
    },
    {
        "title": "దీపం 2.0 — LPG పథకం",
        "sub": "Deepam 2.0 — Free LPG Cylinder Scheme",
        "audio": "దీపం 2.0 పథకం నవంబర్ 1, 2024న ప్రారంభించారు. ఈ తేదీ AP స్థాపన దినోత్సవం (Foundation Day). ప్రారంభ స్థలం: ఎడుపురం, ఇచ్ఛాపురం మండలం, శ్రీకాకుళం జిల్లా. అర్హ కుటుంబాలకు సంవత్సరానికి 3 ఉచిత LPG సిలిండర్లు. సిలిండర్ ఖర్చు చెల్లించిన తర్వాత 48 గంటల్లో తిరిగి అకౌంట్‌కు వస్తుంది. ప్రారంభ విడుదల ₹894 కోట్లు. అమలు మంత్రి: నాదెండ్ల మనోహర్ (JSP, Civil Supplies).",
        "html": """<div class="concept-cover">
  <h1>Deepam 2.0 — Free LPG &nbsp;<span class="bi-te">/ దీపం 2.0 — LPG పథకం</span></h1>
  <div class="sub">3 free cylinders/yr • Launched Nov 1, 2024 (AP Foundation Day) • Refund in 48 hrs</div>
</div>

<div class="section-hdr">Launch & Key Facts / ప్రారంభం, ముఖ్య వాస్తవాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launch date</td><td><b>November 1, 2024</b> (AP Foundation Day)</td><td class="bi-te">నవంబర్ 1, 2024 — AP స్థాపన దినోత్సవం</td></tr>
<tr><td>Launch venue</td><td>Edupuram village, Ichchapuram mandal, Srikakulam</td><td class="bi-te">ఎడుపురం, ఇచ్ఛాపురం, శ్రీకాకుళం</td></tr>
<tr><td>Free cylinders / year</td><td><b>3</b> (typically Jan, May, Sep)</td><td class="bi-te">సంవత్సరానికి 3 సిలిండర్లు</td></tr>
<tr><td>Refund window</td><td><b>48 hours</b> (DBT to bank account)</td><td class="bi-te">48 గంటల్లో తిరిగి జమ</td></tr>
<tr><td>Initial release</td><td>₹894 crore (BP / HP / IOC oil cos)</td><td class="bi-te">తొలి విడుదల ₹894 కోట్లు</td></tr>
<tr><td>Implementing minister</td><td>Nadendla Manohar (JSP) — Civil Supplies</td><td class="bi-te">నాదెండ్ల మనోహర్ (JSP, పౌర సరఫరాలు)</td></tr>
<tr><td>2026-27 budget (Indradhanussu basket)</td><td>₹2,601 crore</td><td class="bi-te">2026-27 బడ్జెట్ ₹2,601 కోట్లు</td></tr>
</table>

<div class="section-hdr">How It Works / ఎలా పనిచేస్తుంది</div>
<p><b>Mechanism:</b> The household pays the full LPG cylinder price upfront to the gas dealer (~₹900). Within 48 hours, the cost is credited back via DBT to the registered Aadhaar-linked bank account. Eligibility follows the existing ration card / Deepam beneficiary list of the 2014-19 TDP regime — that is why the scheme bears the <b>"2.0"</b> tag (relaunch of original Deepam).</p>
<p class="bi-te">లబ్ధిదారు ముందుగా దుకాణదారుకు సిలిండర్ ఖర్చు చెల్లిస్తారు (~₹900). ఆ తర్వాత 48 గంటల్లో రిజిస్టర్డ్ ఆధార్-లింక్డ్ బ్యాంక్ ఖాతాకు DBT ద్వారా డబ్బు తిరిగి జమ అవుతుంది. 2014-19 TDP ప్రభుత్వంలో అసలు 'దీపం' పథకం ఉండేది; 2024లో మెరుగుపరిచి 'దీపం 2.0' గా పునఃప్రారంభం.</p>

<div class="section-hdr">2026 PNG Extension / 2026 PNG విస్తరణ</div>
<p>On <b>April 10, 2026</b>, the government announced the <b>"AP PNG Financial Assistance Scheme"</b> (Dipam 2.0 PNG) — ₹2,400/year for households on piped natural gas connections, paid in 6 bi-monthly installments. This extends the LPG model to cooking-gas customers in urban Vijayawada / Visakhapatnam.</p>
<p class="bi-te">ఏప్రిల్ 10, 2026న పైప్‌లైన్ గ్యాస్ (PNG) వినియోగదారులకు ₹2,400/సంవత్సరం (6 వాయిదాలు) — విజయవాడ, విశాఖ ప్రాంతాల్లో పట్టణ లబ్ధిదారులకు.</p>"""
    },
    {
        "title": "ఉచిత బస్సు & నిరుద్యోగ బృతి",
        "sub": "Free Bus Travel & Nirudyoga Bruthi (Unemployment Allowance)",
        "audio": "ఆగస్టు 15, 2024 స్వాతంత్ర్య దినోత్సవం రోజు రెండు పథకాలు అమలైనాయి. 1) APSRTC ఉచిత బస్సు ప్రయాణం — మహిళలకు, transgender వ్యక్తులకు అన్ని APSRTC బస్సుల్లో ఉచిత ప్రయాణం. ఆగస్టు 15, 2025న 1వ వార్షికోత్సవంపై దీనికి 'స్త్రీ శక్తి' (Stree Shakti) అని అధికారిక పేరు పెట్టారు; అన్ని 5 APSRTC విభాగాలకు విస్తరించారు. అమలు మంత్రి: మండిపల్లి రాంప్రసాద్ రెడ్డి (TDP, Transport). 2) నిరుద్యోగ బృతి — నిరుద్యోగ యువత / యువతులకు ₹3,000/నెల నిరుద్యోగ భత్యం. ఆగస్టు 15, 2024 నుండి నమోదు ప్రారంభం.",
        "html": """<div class="concept-cover">
  <h1>Free Bus &amp; Unemployment Allowance &nbsp;<span class="bi-te">/ ఉచిత బస్సు &amp; నిరుద్యోగ బృతి</span></h1>
  <div class="sub">Both launched Aug 15, 2024 (Independence Day) • Stree Shakti rebrand Aug 15, 2025</div>
</div>

<div class="section-hdr">Stree Shakti — Free APSRTC for Women / స్త్రీ శక్తి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launch date</td><td>August 15, 2024 (Independence Day)</td><td class="bi-te">ఆగస్టు 15, 2024 (స్వాతంత్ర్య దినోత్సవం)</td></tr>
<tr><td>Official name from</td><td><b>August 15, 2025</b> — "Stree Shakti"</td><td class="bi-te">ఆగస్టు 15, 2025న 'స్త్రీ శక్తి' అధికారిక పేరు</td></tr>
<tr><td>Beneficiaries</td><td>Women, girls, transgender persons</td><td class="bi-te">మహిళలు, బాలికలు, Transgender</td></tr>
<tr><td>Coverage</td><td>All ordinary APSRTC services (Pallevelugu, Express, Ultra-Deluxe), <b>5 RTC zones</b></td><td class="bi-te">అన్ని 5 APSRTC జోన్‌లు</td></tr>
<tr><td>Implementing minister</td><td>Mandipalli Ramprasad Reddy (TDP, Rayachoti) — Transport</td><td class="bi-te">మండిపల్లి రాంప్రసాద్ రెడ్డి</td></tr>
<tr><td>2026-27 budget</td><td>₹1,420 crore (FY26-27 allocation)</td><td class="bi-te">2026-27 ₹1,420 కోట్లు</td></tr>
</table>

<div class="section-hdr">Nirudyoga Bruthi — Unemployment Allowance / నిరుద్యోగ బృతి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launch / registration</td><td>August 15, 2024 onwards</td><td class="bi-te">ఆగస్టు 15, 2024 నుండి నమోదు</td></tr>
<tr><td>Monthly stipend</td><td><b>₹3,000 / month</b></td><td class="bi-te">నెలకు ₹3,000</td></tr>
<tr><td>Target group</td><td>Registered unemployed youth (graduates, ITI, diploma)</td><td class="bi-te">నిరుద్యోగ యువత / యువతులు</td></tr>
<tr><td>Eligibility</td><td>Age 22-35, AP domicile, registered on Employment Exchange</td><td class="bi-te">22-35 వయసు, AP domicile</td></tr>
<tr><td>Payment mode</td><td>Direct Benefit Transfer (DBT)</td><td class="bi-te">DBT</td></tr>
</table>

<p><b>"Triple launch" of Aug 15, 2024:</b> Three schemes were rolled out on the same Independence Day — (i) Free Bus Travel, (ii) Nirudyoga Bruthi registration, and (iii) Anna Canteen relaunch (₹5/meal). Chief Minister Naidu chose Independence Day deliberately to signal welfare delivery in his very first 60 days back in office (oath on June 12, 2024).</p>
<p class="bi-te">ఆగస్టు 15, 2024 ఒకే రోజు 3 పథకాలు ప్రారంభం — ఉచిత బస్సు, నిరుద్యోగ బృతి, అన్నా కేంటీన్ పునఃప్రారంభం. CM చంద్రబాబు తొలి 60 రోజుల్లోనే సంక్షేమం అందించాలని ఈ రోజు ఎంచుకున్నారు.</p>"""
    },
    {
        "title": "అన్నదాత సుఖీభవ — రైతు పథకం",
        "sub": "Annadata Sukhibhava — Farmer Support Scheme",
        "audio": "అన్నదాత సుఖీభవ పథకం ఆగస్టు 2, 2025న ప్రారంభించారు. రైతులకు సంవత్సరానికి ₹20,000 ఇస్తారు. 3 వాయిదాలు: ₹7,000 + ₹7,000 + ₹6,000. విభజన: రాష్ట్రం ₹14,000 + కేంద్రం ₹6,000 (PM KISAN). మొదటి వాయిదా ₹7,000 — ₹3,175 కోట్లు 46.86 లక్షల రైతులకు విడుదల. 2024-25 బడ్జెట్ కేటాయింపు ₹6,300 కోట్లు.",
        "html": """<div class="concept-cover">
  <h1>Annadata Sukhibhava &nbsp;<span class="bi-te">/ అన్నదాత సుఖీభవ</span></h1>
  <div class="sub">₹20,000/yr per farmer • Launched Aug 2, 2025 • State ₹14,000 + Centre ₹6,000</div>
</div>

<div class="section-hdr">Scheme Snapshot / పథకం వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launch date</td><td><b>August 2, 2025</b></td><td class="bi-te">ఆగస్టు 2, 2025</td></tr>
<tr><td>Launch venue</td><td>Thurpu Veerayyapalem, Darsi mandal, Prakasam dist</td><td class="bi-te">తూర్పు వీరయ్యపాలెం, దార్సి, ప్రకాశం</td></tr>
<tr><td>Annual benefit</td><td><b>₹20,000 per farmer family</b></td><td class="bi-te">రైతుకు ₹20,000/yr</td></tr>
<tr><td>State share</td><td>₹14,000</td><td class="bi-te">రాష్ట్రం ₹14,000</td></tr>
<tr><td>Centre share</td><td>₹6,000 (via PM-KISAN)</td><td class="bi-te">కేంద్రం ₹6,000 (PM KISAN)</td></tr>
<tr><td>Installments</td><td>3 tranches: ₹7,000 + ₹7,000 + ₹6,000</td><td class="bi-te">3 వాయిదాలు</td></tr>
</table>

<div class="section-hdr">First Installment & Coverage / మొదటి వాయిదా</div>
<table class="key-table">
<tr><th>Metric</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>1st installment amount</td><td>₹7,000 per farmer</td><td class="bi-te">మొదటి వాయిదా ₹7,000</td></tr>
<tr><td>Beneficiaries (1st release)</td><td><b>46.86 lakh farmers</b></td><td class="bi-te">46.86 లక్షల రైతులు</td></tr>
<tr><td>Total funds released (1st)</td><td>₹3,175 crore</td><td class="bi-te">₹3,175 కోట్లు</td></tr>
<tr><td>2024-25 budget allocation</td><td>₹6,300 crore</td><td class="bi-te">2024-25 బడ్జెట్</td></tr>
<tr><td>2026-27 budget allocation</td><td><b>₹6,600 crore</b></td><td class="bi-te">2026-27 బడ్జెట్ ₹6,600 కోట్లు</td></tr>
<tr><td>Registration</td><td>AP Online + Loka Mitram (gram sachivalayam) kiosks</td><td class="bi-te">AP Online / గ్రామ సచివాలయం</td></tr>
</table>

<p><b>Comparison with YSR Rythu Bharosa:</b> The earlier YSRCP scheme provided ₹13,500/year (state ₹7,500 + centre ₹6,000). Annadata Sukhibhava raises the state share to ₹14,000, taking total support to <b>₹20,000</b> — a ~48% increase per farmer. The first launch covered 46.86 lakh of an estimated 55 lakh registered farmer families. Coverage excludes large landholders (>10 acres) and government employees.</p>
<p class="bi-te">YSR రైతు భరోసా (₹13,500) తో పోలిస్తే — అన్నదాత సుఖీభవ ₹20,000 (సుమారు 48% పెరుగుదల). 55 లక్షల నమోదిత రైతు కుటుంబాల్లో మొదటి విడతలో 46.86 లక్షల మందికి అందింది. 10 ఎకరాలకు మించిన భూస్వాములు, ప్రభుత్వ ఉద్యోగులు exclude.</p>"""
    },
    {
        "title": "తల్లికి వందనం — విద్యా పథకం",
        "sub": "Talliki Vandanam — Education Scheme for Students' Mothers",
        "audio": "తల్లికి వందనం పథకం జూన్ 12, 2025న ప్రారంభించారు. ఈ తేదీ ప్రభుత్వ 1వ వార్షికోత్సవం. పాఠశాల విద్యార్థి తల్లికి ₹15,000/సంవత్సరం నేరుగా తల్లి బ్యాంక్ అకౌంట్‌కు వస్తుంది. Class 1-12, ప్రభుత్వ లేదా Aided పాఠశాలలు. కనీసం 75% హాజరు అవసరం. అర్హులైన విద్యార్థులు 69.16 లక్షలు. 2025-26 బడ్జెట్ ₹9,407 కోట్లు. తల్లి Aadhaar బ్యాంక్ అకౌంట్ NPCI తో link అయి ఉండాలి.",
        "html": """<div class="concept-cover">
  <h1>Talliki Vandanam &nbsp;<span class="bi-te">/ తల్లికి వందనం</span></h1>
  <div class="sub">₹15,000/yr to student's mother • Launched Jun 12, 2025 (govt 1st anniversary)</div>
</div>

<div class="section-hdr">Scheme Snapshot / పథకం వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launch date</td><td><b>June 12, 2025</b> (1st anniversary of Naidu's oath)</td><td class="bi-te">జూన్ 12, 2025 — ప్రభుత్వ 1వ వార్షికోత్సవం</td></tr>
<tr><td>Annual benefit</td><td>₹15,000 per student (~₹1,250 / month equivalent)</td><td class="bi-te">విద్యార్థికి ₹15,000/yr</td></tr>
<tr><td>Paid to</td><td><b>Mother's</b> bank account (DBT, NPCI Aadhaar-linked)</td><td class="bi-te">తల్లి బ్యాంక్ ఖాతాకు నేరుగా</td></tr>
<tr><td>Classes covered</td><td>Class 1 to Class 12</td><td class="bi-te">1-12 తరగతులు</td></tr>
<tr><td>Schools covered</td><td>Govt + Aided + (selected) private; minorities included</td><td class="bi-te">ప్రభుత్వ + Aided పాఠశాలలు</td></tr>
<tr><td>Attendance rule</td><td><b>Minimum 75% attendance</b></td><td class="bi-te">కనీసం 75% హాజరు</td></tr>
<tr><td>Eligible students</td><td>69.16 lakh</td><td class="bi-te">69.16 లక్షల విద్యార్థులు</td></tr>
<tr><td>2025-26 budget</td><td><b>₹9,407 crore</b></td><td class="bi-te">2025-26 బడ్జెట్ ₹9,407 కోట్లు</td></tr>
</table>

<div class="section-hdr">Comparison with YSR Amma Vodi / YSR అమ్మ వొడితో పోలిక</div>
<table class="key-table">
<tr><th>Parameter</th><th>YSR Amma Vodi (2019-24)</th><th>Talliki Vandanam (2025-)</th></tr>
<tr><td>Amount</td><td>₹15,000/yr</td><td>₹15,000/yr (same)</td></tr>
<tr><td>Eligible schools</td><td>Govt + Aided + Private (incl. Inter colleges)</td><td>Primarily Govt + Aided (private narrowed)</td></tr>
<tr><td>Attendance threshold</td><td>75%</td><td>75% (retained)</td></tr>
<tr><td>Paid to</td><td>Mother's account</td><td>Mother's account</td></tr>
<tr><td>Aadhaar linkage</td><td>Required</td><td>Required + NPCI mandatory</td></tr>
</table>

<p><b>Why the mother:</b> The scheme uses cash transfer to the mother as a proxy for school retention — fee-aid logic of YSR Amma Vodi, repackaged with the "Tallikki Vandanam" (salute to mother) branding. The 1st anniversary launch date (Jun 12, 2025) made it the headline announcement of CM Naidu's first year in office. The mother's bank account must be NPCI-mapped to her Aadhaar; otherwise the DBT fails and the family forfeits the year's payment.</p>
<p class="bi-te">తల్లికి నగదు ఇవ్వడం వెనుక తర్కం — పాఠశాల హాజరును ప్రోత్సహించడం. YSR అమ్మ వొడి తరహాలోనే, కానీ 'తల్లికి వందనం' బ్రాండింగ్‌తో. NPCI-Aadhaar లింకింగ్ తప్పనిసరి; లేకుంటే చెల్లింపు fail అవుతుంది.</p>"""
    },
    {
        "title": "ఆడబిడ్డ నిధి & NTR భరోసా పెన్షన్",
        "sub": "Aadabidda Nidhi & NTR Bharosa Pension",
        "audio": "ఆడబిడ్డ నిధి: 18-59 సంవత్సరాల మహిళలకు ₹1,500/నెల (₹18,000/సంవత్సరం). 80+ లక్షల మహిళలు లబ్ధి పొందుతారు. BC/SC/ST/మైనారిటీ/EBC వర్గాలు అర్హులు. 2026లో అమలు అవుతుందని ప్రభుత్వం ప్రకటించింది. NTR భరోసా పెన్షన్: జూన్ 13, 2024న ప్రారంభించారు. YSRCP పేరు 'YSR పెన్షన్ కనుక' మారి 'NTR భరోసా' అయింది. Basic ₹4,000/నెల. పూర్తి వికలాంగులకు ₹15,000/నెల. 65+ లక్షల మంది లబ్ధిదారులు. 28 కేటగిరీలు: వృద్ధులు, వితంతువులు, వికలాంగులు, మత్స్యకారులు, చేనేత కార్మికులు, Transgender, కళాకారులు, PLHIV తదితరులు.",
        "html": """<div class="concept-cover">
  <h1>Aadabidda Nidhi &amp; NTR Bharosa &nbsp;<span class="bi-te">/ ఆడబిడ్డ నిధి &amp; NTR భరోసా</span></h1>
  <div class="sub">Women ₹1,500/month • NTR Bharosa pension ₹4,000/month (65+ lakh)</div>
</div>

<div class="section-hdr">Aadabidda Nidhi / ఆడబిడ్డ నిధి</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Monthly benefit</td><td><b>₹1,500/month</b> (₹18,000/year)</td><td class="bi-te">నెలకు ₹1,500 (₹18,000/yr)</td></tr>
<tr><td>Age band</td><td>18-59 years</td><td class="bi-te">18-59 సంవత్సరాలు</td></tr>
<tr><td>Target communities</td><td>BC, SC, ST, Minority, EBC women</td><td class="bi-te">BC, SC, ST, మైనారిటీ, EBC</td></tr>
<tr><td>Estimated beneficiaries</td><td>~80+ lakh women</td><td class="bi-te">80+ లక్షల మహిళలు</td></tr>
<tr><td>Status</td><td>Announced for <b>2026 rollout</b> — last Super Six scheme to launch</td><td class="bi-te">2026లో అమలు ప్రకటన</td></tr>
</table>

<div class="section-hdr">NTR Bharosa Pension / NTR భరోసా</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Launch date</td><td><b>June 13, 2024</b> (day after oath)</td><td class="bi-te">జూన్ 13, 2024 (ప్రమాణ స్వీకారం తర్వాత రోజు)</td></tr>
<tr><td>First payment</td><td>July 1, 2024</td><td class="bi-te">జూలై 1, 2024</td></tr>
<tr><td>Previous name</td><td>YSR Pension Kanuka (YSRCP era)</td><td class="bi-te">YSR పెన్షన్ కనుక (YSRCP కాలం)</td></tr>
<tr><td>Basic pension</td><td><b>₹4,000 / month</b></td><td class="bi-te">బేసిక్ ₹4,000/నెల</td></tr>
<tr><td>Fully disabled (CRPD)</td><td>₹15,000 / month</td><td class="bi-te">పూర్తి వికలాంగులు ₹15,000/నెల</td></tr>
<tr><td>Dialysis patients</td><td>₹10,000 / month</td><td class="bi-te">డయాలసిస్ ₹10,000</td></tr>
<tr><td>Beneficiaries</td><td>65+ lakh</td><td class="bi-te">65+ లక్షల లబ్ధిదారులు</td></tr>
<tr><td>Categories</td><td><b>28 categories</b></td><td class="bi-te">28 కేటగిరీలు</td></tr>
<tr><td>2026-27 budget</td><td>₹27,719 crore</td><td class="bi-te">2026-27 బడ్జెట్ ₹27,719 కోట్లు</td></tr>
</table>

<p><b>28 categories include:</b> old-age (60+), widows, fully/partially disabled, weavers, fishermen (during ban April-June), single women, leprosy-affected, dappu artists, PLHIV (people living with HIV), transgender, CKD/dialysis patients, ART beneficiaries, traditional cobblers, toddy tappers, fishermen widows, and more. Payment is monthly DBT on the 1st of every month, executed at village/ward secretariats.</p>
<p class="bi-te">28 కేటగిరీలు: వృద్ధులు (60+), వితంతువులు, పూర్తి/పాక్షిక వికలాంగులు, చేనేత కార్మికులు, మత్స్యకారులు, ఒంటరి మహిళలు, కుష్ఠు రోగులు, ట్రాన్స్‌జెండర్, డయాలసిస్ రోగులు, PLHIV, తదితర. ప్రతి నెల 1వ తేదీ గ్రామ/వార్డు సచివాలయం ద్వారా DBT.</p>"""
    },
    {
        "title": "అన్నా కేంటీన్ & ఇతర పథకాలు",
        "sub": "Anna Canteen & Other Key Schemes",
        "audio": "అన్నా కేంటీన్: TDP 2014-2019 లో ప్రారంభించింది. YSRCP 2019లో నిలిపివేసింది. TDP మళ్ళీ ఆగస్టు 15, 2024న పునఃప్రారంభించింది. ₹5/ప్లేట్ భోజనం. Phase 1: 100 కేంటీన్లు. పేదలందరికీ ఇల్లు: 30.6 లక్షల గృహ స్థలాలు, ₹8,000 కోట్లు. మత్స్యకార సేవ: నిషేధ కాలంలో (Apr-Jun) ₹10,000. నేత భరోసా: చేనేత కార్మికులకు ₹25,000/సంవత్సరం + ఉచిత విద్యుత్. AP వాహన మిత్ర: Auto/Taxi యజమానులకు ₹10,000-15,000/సంవత్సరం.",
        "html": """<div class="concept-cover">
  <h1>Anna Canteen &amp; Other Schemes &nbsp;<span class="bi-te">/ అన్నా కేంటీన్ &amp; ఇతర పథకాలు</span></h1>
  <div class="sub">₹5 meals • Pedalandariki Illu • Netanna Bharosa • Vahana Mitra</div>
</div>

<div class="section-hdr">Anna Canteen / అన్నా కేంటీన్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Original launch</td><td>2014-19 TDP regime</td><td class="bi-te">2014-19 TDP కాలం</td></tr>
<tr><td>Closed by</td><td>YSRCP in 2019</td><td class="bi-te">YSRCP 2019లో నిలిపివేత</td></tr>
<tr><td>Relaunch</td><td><b>August 15, 2024</b> (Independence Day)</td><td class="bi-te">ఆగస్టు 15, 2024 — పునఃప్రారంభం</td></tr>
<tr><td>Meal price</td><td><b>₹5 / full plate</b> (rice, dal, vegetable, sambar, curd)</td><td class="bi-te">₹5/పళ్ళెం పూర్తి భోజనం</td></tr>
<tr><td>Phase 1</td><td>100 canteens (urban + rural)</td><td class="bi-te">Phase 1 — 100 కేంటీన్లు</td></tr>
<tr><td>2026 expansion</td><td>71 new canteens (Feb 2026) — total <b>275</b></td><td class="bi-te">2026 — మొత్తం 275 కేంటీన్లు</td></tr>
</table>

<div class="section-hdr">Other Welfare Schemes / ఇతర సంక్షేమ పథకాలు</div>
<table class="key-table">
<tr><th>Scheme</th><th>Benefit</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Pedalandariki Illu</b> (Housing for All)</td><td>30.6 lakh house sites + ₹8,000 cr for construction</td><td class="bi-te">పేదలందరికీ ఇల్లు — 30.6 లక్షల ఇంటి స్థలాలు</td></tr>
<tr><td><b>Matsyakara Seva</b></td><td>₹10,000 to fishermen during ban (Apr-Jun)</td><td class="bi-te">మత్స్యకారులకు నిషేధ కాలంలో ₹10,000</td></tr>
<tr><td><b>Netanna Bharosa</b></td><td>₹25,000/year + free electricity to weavers</td><td class="bi-te">చేనేత కార్మికులకు ₹25,000/yr</td></tr>
<tr><td><b>AP Vahana Mitra</b></td><td>₹10,000-15,000/yr to auto/taxi owners</td><td class="bi-te">ఆటో/టాక్సీ యజమానులకు ₹10,000-15,000</td></tr>
<tr><td><b>Divyang Shakti</b> (Mar 18, 2026)</td><td>Free RTC bus for ~2 lakh divyangulu; ₹207 cr to APSRTC</td><td class="bi-te">వికలాంగులకు ఉచిత RTC (2026)</td></tr>
<tr><td><b>National Handloom Museum</b></td><td>Inaugurated Aug 7, 2025 (National Handloom Day)</td><td class="bi-te">జాతీయ హస్తకళా మ్యూజియం (ఆగస్టు 7, 2025)</td></tr>
</table>

<p><b>Aug 7, 2025 — "Handloom Day":</b> Two flagship initiatives on the same day — the National Handloom Museum was inaugurated and the Netanna Bharosa ₹25,000 payout to weavers was disbursed. AP has India's largest weaver cluster outside TN/WB (Mangalagiri, Dharmavaram, Madhavaram, Venkatagiri silks).</p>
<p class="bi-te">ఆగస్టు 7, 2025 (జాతీయ హస్తకళా దినోత్సవం) — జాతీయ హస్తకళా మ్యూజియం ప్రారంభం + నేతన్న భరోసా ₹25,000 చెల్లింపు. AP లో మంగళగిరి, ధర్మవరం, మాధవరం, వెంకటగిరి సిల్క్ — TN/WB తర్వాత దేశంలో అతిపెద్ద చేనేత క్లస్టర్.</p>"""
    },
    {
        "title": "YSRCP vs TDP పథకాల పోలిక & పరీక్ష సారాంశం",
        "sub": "YSRCP vs TDP Scheme Comparison & Exam Summary",
        "audio": "YSR పెన్షన్ కనుక → NTR భరోసా (₹4,000 Basic). YSR అమ్మవడి → తల్లికి వందనం (రెండూ ₹15,000 కానీ ప్రైవేట్ పాఠశాలలు exclude). YSR చేయూత → ఆడబిడ్డ నిధి (₹18,000/yr). YSR రైతు భరోసా (₹13,500) → అన్నదాత సుఖీభవ (₹20,000 + PM KISAN). పరీక్ష ట్రిక్ — తేదీలు: Aug 15, 2024 = ఉచిత బస్సు + నిరుద్యోగ బృతి + అన్నా కేంటీన్ (Independence Day); Nov 1, 2024 = దీపం 2.0 (AP Foundation Day); Jun 12, 2025 = తల్లికి వందనం (1st Anniversary); Aug 2, 2025 = అన్నదాత సుఖీభవ.",
        "html": """<div class="concept-cover">
  <h1>YSRCP vs TDP — Scheme Map &nbsp;<span class="bi-te">/ పథకాల పోలిక</span></h1>
  <div class="sub">Old name → new name • Key dates table • Exam quick-reference</div>
</div>

<div class="section-hdr">Name-Change Map / పేరు మార్పులు</div>
<table class="key-table">
<tr><th>YSRCP (2019-24)</th><th>TDP-JSP-BJP (2024-)</th><th>Amount</th><th class="bi-te">వివరణ</th></tr>
<tr><td>YSR Pension Kanuka</td><td><b>NTR Bharosa</b></td><td>₹4,000/month basic</td><td class="bi-te">పెన్షన్</td></tr>
<tr><td>YSR Amma Vodi</td><td><b>Talliki Vandanam</b></td><td>₹15,000/yr (private narrowed)</td><td class="bi-te">తల్లికి వందనం</td></tr>
<tr><td>YSR Cheyutha</td><td><b>Aadabidda Nidhi</b></td><td>₹18,000/yr (₹1,500/month)</td><td class="bi-te">ఆడబిడ్డ నిధి</td></tr>
<tr><td>YSR Rythu Bharosa</td><td><b>Annadata Sukhibhava</b></td><td>₹13,500 → ₹20,000/yr</td><td class="bi-te">రైతులు</td></tr>
<tr><td>Anna Canteen (TDP-original)</td><td>Anna Canteen (revived Aug 2024)</td><td>₹5/plate</td><td class="bi-te">అన్నా కేంటీన్</td></tr>
<tr><td>(none)</td><td>Deepam 2.0</td><td>3 free LPG/yr</td><td class="bi-te">LPG</td></tr>
<tr><td>(none)</td><td>Stree Shakti (free bus)</td><td>Free APSRTC for women</td><td class="bi-te">ఉచిత బస్సు</td></tr>
<tr><td>(none)</td><td>Nirudyoga Bruthi</td><td>₹3,000/month</td><td class="bi-te">నిరుద్యోగ బృతి</td></tr>
</table>

<div class="section-hdr">Launch Date Table / ప్రారంభ తేదీలు</div>
<table class="key-table">
<tr><th>Date</th><th>Significance</th><th>Schemes Launched</th><th class="bi-te">తేదీ ప్రాముఖ్యత</th></tr>
<tr><td><b>Jun 12, 2024</b></td><td>4th Naidu oath</td><td>—</td><td class="bi-te">ప్రమాణ స్వీకారం</td></tr>
<tr><td>Jun 13, 2024</td><td>Day-1 of govt</td><td>NTR Bharosa pension</td><td class="bi-te">NTR భరోసా</td></tr>
<tr><td><b>Aug 15, 2024</b></td><td>Independence Day</td><td>Stree Shakti (bus) + Nirudyoga Bruthi + Anna Canteen relaunch</td><td class="bi-te">3 పథకాలు ఒకే రోజు</td></tr>
<tr><td><b>Nov 1, 2024</b></td><td>AP Foundation Day</td><td>Deepam 2.0 (Edupuram, Srikakulam)</td><td class="bi-te">దీపం 2.0</td></tr>
<tr><td><b>Jun 12, 2025</b></td><td>1st anniversary of govt</td><td>Talliki Vandanam</td><td class="bi-te">తల్లికి వందనం</td></tr>
<tr><td><b>Aug 2, 2025</b></td><td>—</td><td>Annadata Sukhibhava (Darsi, Prakasam)</td><td class="bi-te">అన్నదాత సుఖీభవ</td></tr>
<tr><td>Aug 15, 2025</td><td>1st anniversary of free bus</td><td>"Stree Shakti" official naming</td><td class="bi-te">స్త్రీ శక్తి అధికారిక పేరు</td></tr>
<tr><td><b>2026</b></td><td>Pending</td><td>Aadabidda Nidhi (last Super Six scheme)</td><td class="bi-te">ఆడబిడ్డ నిధి 2026 లక్ష్యం</td></tr>
</table>

<p><b>Exam mnemonic — "3-1-1-1":</b> 3 schemes on Aug 15 2024 (Indep Day triple-launch) + 1 on Nov 1 2024 (AP Foundation Day) + 1 on Jun 12 2025 (govt anniversary) + 1 on Aug 2 2025 (Darsi). Aadabidda Nidhi is the only Super Six scheme not yet launched as of mid-2026.</p>
<p class="bi-te">పరీక్ష గుర్తుపెట్టుకునే విధానం — "3-1-1-1": ఆగస్టు 15, 2024 న 3 పథకాలు; నవంబర్ 1, 2024 న 1 (దీపం 2.0); జూన్ 12, 2025 న 1 (తల్లికి వందనం); ఆగస్టు 2, 2025 న 1 (అన్నదాత). ఆడబిడ్డ నిధి 2026 లో అమలు లక్ష్యం.</p>"""
    },
]

# MCQ_DATA: (section_idx, difficulty, question_te, opt_a, opt_b, opt_c, opt_d, answer, explanation_te)
MCQ_DATA = [
    (0, 1,
     'TDP-JSP-BJP కూటమి ఎన్నికల హామీలను ఏమని పిలుస్తారు?',
     'సూపర్ సిక్స్', 'సూపర్ ఎయిట్', 'నవరత్నాలు', 'మహా హామీలు',
     'a',
     "TDP-JSP-BJP కూటమి 2024 ఎన్నికల ముందు ఇచ్చిన 6 హామీలు 'సూపర్ సిక్స్' అని పిలుస్తారు."),

    (0, 1,
     'సూపర్ సిక్స్ లో ఎన్ని పథకాలు ఉన్నాయి?',
     '6', '7', '4', '5',
     'a',
     'సూపర్ సిక్స్ = 6 పథకాలు: దీపం 2.0, ఉచిత బస్సు, నిరుద్యోగ బృతి, అన్నదాత సుఖీభవ, తల్లికి వందనం, ఆడబిడ్డ నిధి.'),

    (0, 1,
     'సూపర్ సిక్స్ లో మహిళలకు నెలకు ఎంత ఇస్తారు (ఆడబిడ్డ నిధి)?',
     '₹1,500', '₹2,000', '₹2,500', '₹1,000',
     'a',
     'ఆడబిడ్డ నిధి పథకం కింద మహిళలకు ₹1,500/నెల (₹18,000/సంవత్సరం) ఇస్తారు.'),

    (0, 2,
     'సూపర్ సిక్స్ లో రైతులకు ఏ పథకం ఉంది?',
     'అన్నదాత సుఖీభవ', 'YSR రైతు భరోసా', 'రైతు బంధు', 'కర్షక భరోసా',
     'a',
     'అన్నదాత సుఖీభవ — రైతులకు ₹20,000/సంవత్సరం ఇచ్చే పథకం. TDP-JSP-BJP కూటమి హామీ.'),

    (1, 1,
     'దీపం 2.0 పథకం ఏ తేదీన ప్రారంభించారు?',
     'నవంబర్ 1, 2024', 'ఆగస్టు 15, 2024', 'అక్టోబర్ 2, 2024', 'జూన్ 12, 2024',
     'a',
     'దీపం 2.0 నవంబర్ 1, 2024న ప్రారంభించారు — ఈ తేదీ AP స్థాపన దినోత్సవం (Foundation Day).'),

    (1, 1,
     'దీపం 2.0 కింద సంవత్సరానికి ఎన్ని ఉచిత LPG సిలిండర్లు ఇస్తారు?',
     '3', '4', '2', '1',
     'a',
     'దీపం 2.0 కింద అర్హ కుటుంబాలకు సంవత్సరానికి 3 ఉచిత LPG సిలిండర్లు ఇస్తారు.'),

    (1, 1,
     'దీపం 2.0 కింద సిలిండర్ ఖర్చు ఎంత సమయంలో తిరిగి వస్తుంది?',
     '48 గంటలు', '72 గంటలు', '7 రోజులు', '24 గంటలు',
     'a',
     'దీపం 2.0 కింద సిలిండర్ ఖర్చు చెల్లించిన తర్వాత 48 గంటల్లో అకౌంట్\u200cకు తిరిగి వస్తుంది.'),

    (1, 2,
     'దీపం 2.0 మొదటి విడుదలలో ఎంత నిధి విడుదల చేశారు?',
     '₹694 కోట్లు', '₹1,200 కోట్లు', '₹500 కోట్లు', '₹894 కోట్లు',
     'd',
     'దీపం 2.0 ప్రారంభ విడుదలలో ₹894 కోట్లు — BP, HP, IOC గ్యాస్ సంస్థలకు విడుదల చేశారు.'),

    (1, 2,
     'దీపం 2.0 ప్రారంభ స్థలం ఏది?',
     'విశాఖపట్నం', 'అమరావతి', 'విజయవాడ', 'ఎడుపురం, ఇచ్ఛాపురం మండలం, శ్రీకాకుళం',
     'd',
     'దీపం 2.0 ఎడుపురం, ఇచ్ఛాపురం మండలం, శ్రీకాకుళం జిల్లాలో ప్రారంభించారు.'),

    (1, 2,
     'దీపం 2.0 అమలు మంత్రి ఎవరు?',
     'పవన్ కళ్యాణ్', 'నారా లోకేష్', 'అచ్చెన్నాయుడు', 'నాదెండ్ల మనోహర్',
     'd',
     'నాదెండ్ల మనోహర్ (JSP, Civil Supplies మంత్రి) దీపం 2.0 అమలు మంత్రి.'),

    (1, 3,
     'నవంబర్ 1, 2024న AP లో ఏ ముఖ్యమైన పథకం ప్రారంభించారు? ఆ తేదీ ప్రాముఖ్యత ఏమిటి?',
     'దీపం 2.0 — AP స్థాపన దినోత్సవం', 'అన్నదాత సుఖీభవ — NTR జయంతి', 'తల్లికి వందనం — పాఠశాల వార్షికోత్సవం', 'NTR భరోసా — CBN పుట్టినరోజు',
     'a',
     'నవంబర్ 1, 2024 = AP స్థాపన దినోత్సవం (Foundation Day). ఆ రోజున దీపం 2.0 ప్రారంభించారు. 3 ఉచిత LPG సిలిండర్లు/సంవత్సరం.'),

    (2, 1,
     'AP లో మహిళలకు ఉచిత APSRTC బస్సు ప్రయాణం ఏ తేదీన ప్రారంభించారు?',
     'ఆగస్టు 15, 2024', 'జనవరి 26, 2025', 'నవంబర్ 1, 2024', 'జూన్ 12, 2024',
     'a',
     'ఆగస్టు 15, 2024 (స్వాతంత్ర్య దినోత్సవం) రోజున APSRTC ఉచిత బస్సు ప్రయాణం ప్రారంభించారు.'),

    (2, 1,
     'AP ఉచిత బస్సు పథకం ఎవరికి వర్తిస్తుంది?',
     'అందరికీ', 'మహిళలు మాత్రమే', 'Senior Citizens మాత్రమే', 'మహిళలు మరియు Transgender వ్యక్తులు',
     'd',
     'AP ఉచిత బస్సు ప్రయాణం మహిళలకు, బాలికలకు మరియు Transgender వ్యక్తులకు వర్తిస్తుంది.'),

    (2, 1,
     'నిరుద్యోగ బృతి (Nirudyoga Bruthi) పథకం కింద నెలకు ఎంత ఇస్తారు?',
     '₹2,000', '₹1,500', '₹5,000', '₹3,000',
     'd',
     'నిరుద్యోగ బృతి పథకం కింద నిరుద్యోగ యువతకు ₹3,000/నెల నిరుద్యోగ భత్యం ఇస్తారు.'),

    (2, 2,
     'ఆగస్టు 15, 2024న ఏ ఏ సూపర్ సిక్స్ పథకాలు అమలు ప్రారంభించారు?',
     'ఉచిత బస్సు + నిరుద్యోగ బృతి', 'దీపం 2.0 + అన్నదాత సుఖీభవ', 'NTR భరోసా + అన్నా కేంటీన్', 'తల్లికి వందనం + ఆడబిడ్డ నిధి',
     'a',
     'ఆగస్టు 15, 2024 (Independence Day) రోజున ఉచిత బస్సు ప్రయాణం + నిరుద్యోగ బృతి అమలు ప్రారంభించారు. అదే రోజు అన్నా కేంటీన్ కూడా పునఃప్రారంభించారు.'),

    (2, 2,
     'APSRTC ఉచిత బస్సు పథకం అమలు మంత్రి ఎవరు?',
     'మండిపల్లి రాంప్రసాద్ రెడ్డి', 'పవన్ కళ్యాణ్', 'గొట్టిపాటి రవికుమార్', 'నారా లోకేష్',
     'a',
     'మండిపల్లి రాంప్రసాద్ రెడ్డి (TDP, Transport మంత్రి, రాయచోటి) ఉచిత బస్సు పథకం అమలు చేస్తున్నారు.'),

    (3, 1,
     'అన్నదాత సుఖీభవ పథకం కింద రైతులకు సంవత్సరానికి ఎంత ఇస్తారు?',
     '₹10,000', '₹25,000', '₹13,500', '₹20,000',
     'd',
     'అన్నదాత సుఖీభవ కింద రైతులకు సంవత్సరానికి ₹20,000 ఇస్తారు (రాష్ట్రం ₹14,000 + కేంద్రం ₹6,000).'),

    (3, 1,
     'అన్నదాత సుఖీభవ మొదటి వాయిదా (1st installment) ఎంత?',
     '₹5,000', '₹6,000', '₹8,000', '₹7,000',
     'd',
     'అన్నదాత సుఖీభవ మొదటి వాయిదా ₹7,000. 3 వాయిదాలు: ₹7,000 + ₹7,000 + ₹6,000 = ₹20,000.'),

    (3, 1,
     'అన్నదాత సుఖీభవ లో కేంద్రం ఇచ్చే మొత్తం ఎంత?',
     '₹6,000', '₹8,000', '₹10,000', '₹4,000',
     'a',
     'అన్నదాత సుఖీభవ లో కేంద్రం PM KISAN కింద ₹6,000 ఇస్తుంది; రాష్ట్రం ₹14,000 ఇస్తుంది.'),

    (3, 2,
     'అన్నదాత సుఖీభవ ఏ తేదీన ప్రారంభించారు?',
     'ఆగస్టు 2, 2025', 'జూన్ 12, 2025', 'ఆగస్టు 15, 2025', 'నవంబర్ 1, 2025',
     'a',
     'అన్నదాత సుఖీభవ ఆగస్టు 2, 2025న ప్రారంభించారు. మొదటి వాయిదా ₹7,000 — 46.86 లక్షల రైతులకు ₹3,175 కోట్లు.'),

    (3, 2,
     'అన్నదాత సుఖీభవ 1వ విడుదలలో ఎంత మంది రైతులకు నిధి ఇచ్చారు?',
     '30 లక్షలు', '40 లక్షలు', '60 లక్షలు', '46.86 లక్షలు',
     'd',
     'అన్నదాత సుఖీభవ 1వ విడుదలలో 46.86 లక్షల రైతులకు ₹3,175 కోట్లు విడుదల చేశారు.'),

    (3, 3,
     'అన్నదాత సుఖీభవ పథకం లో PM KISAN సమన్వయం అంటే ఏమిటి? రాష్ట్రం-కేంద్రం వాటా చెప్పండి.',
     'రాష్ట్రం ₹14,000 + కేంద్రం ₹6,000 = ₹20,000', 'రాష్ట్రం ₹10,000 + కేంద్రం ₹10,000 = ₹20,000', 'రాష్ట్రం ₹15,000 + కేంద్రం ₹5,000 = ₹20,000', 'రాష్ట్రం ₹20,000 మాత్రమే',
     'a',
     'అన్నదాత సుఖీభవ = రాష్ట్ర వాటా ₹14,000 + PM KISAN (కేంద్ర వాటా) ₹6,000 = మొత్తం ₹20,000/సంవత్సరం.'),

    (4, 1,
     'తల్లికి వందనం పథకం ఏ తేదీన ప్రారంభించారు?',
     'జూన్ 12, 2025', 'జూన్ 4, 2025', 'ఆగస్టు 15, 2025', 'జనవరి 1, 2025',
     'a',
     'తల్లికి వందనం జూన్ 12, 2025న ప్రారంభించారు — ఈ తేదీ ప్రభుత్వ 1వ వార్షికోత్సవం (Oath June 12, 2024).'),

    (4, 1,
     'తల్లికి వందనం పథకం కింద విద్యార్థికి సంవత్సరానికి ఎంత ఇస్తారు?',
     '₹12,000', '₹10,000', '₹20,000', '₹15,000',
     'd',
     'తల్లికి వందనం కింద విద్యార్థి తల్లికి ₹15,000/సంవత్సరం నేరుగా తల్లి బ్యాంక్ అకౌంట్\u200cకు వస్తుంది.'),

    (4, 1,
     'తల్లికి వందనం లో డబ్బు ఎవరి అకౌంట్\u200cకు వస్తుంది?',
     'తండ్రి అకౌంట్', 'విద్యార్థి అకౌంట్', 'పాఠశాల అకౌంట్', 'తల్లి అకౌంట్',
     'd',
     'తల్లికి వందనం — డబ్బు నేరుగా తల్లి బ్యాంక్ అకౌంట్\u200cకు వస్తుంది. విద్యార్థి తల్లి Aadhaar NPCI తో link అయి ఉండాలి.'),

    (4, 2,
     'తల్లికి వందనం అర్హత కోసం కనీసం ఎంత % హాజరు అవసరం?',
     '50%', '65%', '90%', '75%',
     'd',
     'తల్లికి వందనం లో కనీసం 75% హాజరు ఉండాలి. Class 1-12, ప్రభుత్వ / Aided పాఠశాలలు అర్హం.'),

    (4, 2,
     'తల్లికి వందనం పథకానికి 2025-26 బడ్జెట్ కేటాయింపు ఎంత?',
     '₹5,000 కోట్లు', '₹7,500 కోట్లు', '₹12,000 కోట్లు', '₹9,407 కోట్లు',
     'd',
     'తల్లికి వందనం పథకానికి 2025-26 బడ్జెట్ లో ₹9,407 కోట్లు కేటాయించారు.'),

    (4, 3,
     'తల్లికి వందనం, అన్నదాత సుఖీభవ ప్రారంభ తేదీలు ఏమిటి? వాటి ప్రత్యేకతలు?',
     'తల్లికి వందనం Aug 15; అన్నదాత Jun 12 — రెండూ Independence Day', 'తల్లికి వందనం Jun 12, 2025 (1 yr anniversary); అన్నదాత Aug 2, 2025', 'తల్లికి వందనం Nov 1; అన్నదాత Jun 12 — AP Days', 'రెండూ Jun 12, 2025 న ప్రారంభించారు',
     'b',
     'తల్లికి వందనం = జూన్ 12, 2025 (ప్రభుత్వ 1వ వార్షికోత్సవం). అన్నదాత సుఖీభవ = ఆగస్టు 2, 2025. రెండూ వేర్వేరు తేదీలు — గుర్తుంచుకోండి!'),

    (5, 1,
     'NTR భరోసా పెన్షన్ ప్రారంభ తేదీ ఏది?',
     'జూన్ 12, 2024', 'జూన్ 13, 2024', 'జూలై 1, 2024', 'ఆగస్టు 15, 2024',
     'b',
     'NTR భరోసా పెన్షన్ జూన్ 13, 2024న ప్రారంభించారు (ప్రమాణ స్వీకారం మరుసటి రోజు). చెల్లింపులు జూలై 1, 2024 నుండి మొదలైనాయి.'),

    (5, 1,
     'NTR భరోసా పెన్షన్ కింద basic pension ఎంత?',
     '₹5,000/నెల', '₹3,000/నెల', '₹2,000/నెల', '₹4,000/నెల',
     'd',
     'NTR భరోసా basic pension ₹4,000/నెల. పూర్తి వికలాంగులకు ₹15,000/నెల.'),

    (5, 1,
     'NTR భరోసా లో పూర్తి వికలాంగులకు (fully disabled) పెన్షన్ ఎంత?',
     '₹5,000', '₹8,000', '₹10,000', '₹15,000',
     'd',
     'NTR భరోసా లో పూర్తి వికలాంగులకు ₹15,000/నెల పెన్షన్. basic pension ₹4,000 మాత్రమే.'),

    (5, 2,
     'NTR భరోసా పెన్షన్ పాత పేరు ఏమిటి?',
     'YSR పెన్షన్ కనుక', 'జగనన్న సురక్ష', 'అన్నదాత భరోసా', 'NTR సంక్షేమం',
     'a',
     "YSRCP కాలం పేరు 'YSR పెన్షన్ కనుక'. TDP 2024లో దాన్ని 'NTR భరోసా' గా మార్చింది."),

    (5, 2,
     'NTR భరోసా పెన్షన్ ఎన్ని కేటగిరీలకు వర్తిస్తుంది?',
     '10', '15', '20', '28',
     'd',
     'NTR భరోసా పెన్షన్ 28 కేటగిరీలకు వర్తిస్తుంది: వృద్ధులు, వితంతువులు, వికలాంగులు, మత్స్యకారులు, చేనేత కార్మికులు, Transgender, PLHIV, తదితరులు.'),

    (5, 2,
     'ఆడబిడ్డ నిధి పథకం ఎవరికి వర్తిస్తుంది?',
     'అన్ని వయసుల మహిళలకు', '18-59 సంవత్సరాల BC/SC/ST మహిళలకు', 'కేవలం SC మహిళలకు', '60+ వయసు మహిళలకు',
     'b',
     'ఆడబిడ్డ నిధి: 18-59 సంవత్సరాల BC, SC, ST, మైనారిటీ, EBC వర్గాల మహిళలకు ₹1,500/నెల.'),

    (6, 1,
     'TDP అన్నా కేంటీన్ 2024లో ఏ తేదీన పునःప్రారంభించారు?',
     'జూన్ 12, 2024', 'జూలై 1, 2024', 'ఆగస్టు 15, 2024', 'నవంబర్ 1, 2024',
     'c',
     'అన్నా కేంటీన్ ఆగస్టు 15, 2024 (స్వాతంత్ర్య దినోత్సవం) రోజున పునఃప్రారంభించారు. Phase 1: 100 కేంటీన్లు.'),

    (6, 1,
     'అన్నా కేంటీన్ లో ఒక పళ్ళెం భోజనం ఖర్చు ఎంత?',
     '₹1', '₹5', '₹10', '₹20',
     'b',
     'అన్నా కేంటీన్ లో ₹5/పళ్ళెం భోజనం ఇస్తారు. YSRCP 2019లో నిలిపివేసింది; TDP 2024లో పునఃప్రారంభించింది.'),

    (6, 2,
     "YSRCP కాలం 'YSR అమ్మవడి' పథకం TDP 2024లో ఏ పేరుతో కొనసాగుతోంది?",
     'ఆడబిడ్డ నిధి', 'తల్లికి వందనం', 'NTR భరోసా', 'అన్నదాత సుఖీభవ',
     'b',
     'YSR అమ్మవడి → తల్లికి వందనం గా మారింది (రెండూ ₹15,000/సంవత్సరం, కానీ ప్రైవేట్ పాఠశాలలు TDP లో exclude).'),

    (6, 2,
     'NTR భరోసా పెన్షన్ లో ఎంత మంది లబ్ధిదారులు ఉన్నారు?',
     '30 లక్షలు', '50 లక్షలు', '65+ లక్షలు', '1 కోటి',
     'c',
     'NTR భరోసా పెన్షన్ 65+ లక్షల మంది లబ్ధిదారులను కవర్ చేస్తుంది.'),

    (7, 1,
     "YSRCP 'YSR పెన్షన్ కనుక' పేరు TDP ఏమని మార్చింది?",
     'CBN భరోసా', 'NTR భరోసా', 'AP భరోసా', 'TDP భరోసా',
     'b',
     "YSRCP కాలంలో 'YSR పెన్షన్ కనుక' అని పిలిచేవారు. TDP 2024లో 'NTR భరోసా' గా పేరు మార్చింది."),

    (7, 1,
     'AP లో సూపర్ సిక్స్ పథకాల్లో ఇంకా (2025 వరకు) ప్రారంభం కాని పథకం ఏది?',
     'దీపం 2.0', 'తల్లికి వందనం', 'ఆడబిడ్డ నిధి', 'అన్నా కేంటీన్',
     'c',
     'ఆడబిడ్డ నిధి (మహిళలకు ₹1,500/నెల) 2026లో అమలు అవుతుందని ప్రభుత్వం ప్రకటించింది — ఇంకా ప్రారంభం కాలేదు.'),

    (7, 2,
     'AP లో ఆగస్టు 15, 2024న ఏ ఏ పథకాలు ప్రారంభమయ్యాయి?',
     'దీపం 2.0 మాత్రమే', 'తల్లికి వందనం + అన్నదాత', 'ఉచిత బస్సు + నిరుద్యోగ బృతి + అన్నా కేంటీన్ పునఃప్రారంభం', 'NTR భరోసా + పేదలందరికీ ఇల్లు',
     'c',
     'ఆగస్టు 15, 2024 (Independence Day): ఉచిత బస్సు ప్రయాణం + నిరుద్యోగ బృతి నమోదు + అన్నా కేంటీన్ పునఃప్రారంభం — అన్నీ ఒకే రోజున.'),

    (7, 2,
     "YSRCP 'YSR రైతు భరోసా' మొత్తం ₹13,500. TDP 'అన్నదాత సుఖీభవ' మొత్తం ఎంత?",
     '₹13,500 (అదే)', '₹15,000', '₹20,000', '₹25,000',
     'c',
     'YSR రైతు భరోసా (₹13,500) → అన్నదాత సుఖీభవ (₹20,000 = రాష్ట్రం ₹14,000 + PM KISAN ₹6,000). TDP లో మొత్తం పెరిగింది.'),

    (7, 3,
     'AP సూపర్ సిక్స్ పథకాల తేదీలను క్రమంలో చెప్పండి. ఏ పథకం మొదటిది?',
     'దీపం 2.0 (Nov 2024) → ఉచిత బస్సు (Aug 2024) — ఇది తప్పు క్రమం', 'ఉచిత బస్సు + నిరుద్యోగ బృతి (Aug 15, 2024) → దీపం 2.0 (Nov 1, 2024) → తల్లికి వందనం (Jun 12, 2025) → అన్నదాత (Aug 2, 2025)', 'అన్నా కేంటీన్ → NTR భరోసా → సూపర్ సిక్స్', 'అన్నీ ఒకే రోజున ప్రారంభించారు',
     'b',
     'క్రమంలో: 1) Aug 15, 2024 — ఉచిత బస్సు + నిరుద్యోగ బృతి; 2) Nov 1, 2024 — దీపం 2.0; 3) Jun 12, 2025 — తల్లికి వందనం; 4) Aug 2, 2025 — అన్నదాత. ఆడబిడ్డ నిధి 2026 target.'),

    (0, 1,
     'సూపర్ సిక్స్ కూటమి ఎవరు?',
     'TDP-JSP-BJP', 'TDP-YSRCP', 'BJP-JSP', 'TDP మాత్రమే',
     'a',
     'TDP-JSP-BJP కూటమి సూపర్ సిక్స్ 6 హామీలను 2024 ఎన్నికల ముందు ప్రకటించారు.'),

    (0, 2,
     'సూపర్ సిక్స్ పથకాల్లో ప్రధానంగా ఏ లక్షిత వర్గాలను దృష్టిలో పెట్టుకుని రూపొందించబడ్డాయి?',
     'మహిళలు, రైతులు, నిరుద్యోగులు', 'పూర్తిగా గ్రామీణ ప్రాంతాలు మాత్రమే', 'పూర్తిగా పట్టణ ప్రాంతాలు మాత్రమే', 'వ్యాపారులు మాత్రమే',
     'a',
     'సూపర్ సిక్స్ 6 హామీలు 3 ప్రధాన లక్షిత వర్గాలకు (మహిళలు: తల్లికి వందనం + ఆడబిడ్డ నిధి + ఉచిత బస్సు; రైతులు: అన్నదాత సుఖీభవ; నిరుద్యోగులు: నిరుద్యోగ బృతి; అన్నీ: దీపం 2.0). నిర్దిష్ట గ్రామీణ అభివృద్ధి హామీ లేదు — గ్రామీణ & పట్టణ రెండింటికీ వర్తిస్తాయి.'),

    (1, 1,
     "దీపం 2.0 పథకం పేరు లోని '2.0' ఏ సూచిస్తుంది?",
     '2వ ముఖ్యమంత్రి కాలంలో రీలాంచ్', 'రెండు నెలల పథకం', 'రెండు సిలిండర్లు', '2 సంవత్సరాల కాలపరిమితి',
     'a',
     'దీపం 2.0 — చంద్రబాబు 2014-19 TDP ప్రభుత్వంలో అసలు దీపం పథకం ఉండేది. 2024లో రెండవ TDP-నేతృత్వంలోని కూటమి తిరిగి అధికారంలోకి వచ్చిన తర్వాత మెరుగుపడిన (re-launched) వెర్షన్‌గా "దీపం 2.0" ప్రారంభించారు.'),

    (1, 2,
     'దీపం 2.0 కింద సిలిండర్ ఖర్చు చెల్లించిన తర్వాత డబ్బు అకౌంట్‌కు ఎంత సమయంలో వస్తుంది?',
     '24 గంటలు', '48 గంటలు', '72 గంటలు', '7 రోజులు',
     'b',
     'దీపం 2.0 కింద సిలిండర్ ఖర్చు చెల్లించిన తర్వాత 48 గంటల్లో డబ్బు తిరిగి అకౌంట్‌కు వస్తుంది.'),

    (1, 3,
     'దీపం 2.0 నిధి కేటాయింపు రాష్ట్రం నుండి కేంద్రం సపోర్టు ఉందా?',
     'పూర్తిగా రాష్ట్ర నిధి', 'రాష్ట్రం 70% + కేంద్రం 30%', 'సమానమైన నిధి', 'నిర్దిష్టమైన సమాచారం లేదు',
     'a',
     'దీపం 2.0 ప్రారంభిక నిధి ₹894 కోట్లు పూర్తిగా TDP సర్కారు నుండి.'),

    (2, 1,
     "AP లో ఉచిత APSRTC బస్సు ప్రయాణ పథకానికి 'స్త్రీ శక్తి' అని అధికారికంగా పేరు ఏ తేదీన పెట్టారు?",
     'మే 13, 2024', 'ఆగస్టు 15, 2024', 'జూన్ 12, 2025', 'ఆగస్టు 15, 2025',
     'd',
     "AP లో మహిళలకు ఉచిత APSRTC బస్సు ప్రయాణం ఆగస్టు 15, 2024న (స్వాతంత్ర్య దినోత్సవం) ప్రారంభించారు. తరువాత ఈ పథకానికి 'స్త్రీ శక్తి' అని అధికారిక పేరు ఆగస్టు 15, 2025న (1వ వార్షికోత్సవం) పెట్టారు."),

    (2, 2,
     'నిరుద్యోగ బృతి పథకం కింద ప్రతి నెలా అర్హ నిరుద్యోగులకు ఎంత ఇస్తారు?',
     '₹1,500', '₹2,000', '₹3,000', '₹5,000',
     'c',
     'నిరుద్యోగ బృతి పథకం కింద AP లో అర్హ నిరుద్యోగులకు ప్రతి నెలా ₹3,000 ఇస్తారు. (ఆగస్టు 15, 2024 న ఉచిత బస్సుతో పాటు ప్రకటించారు.)'),

    (3, 1,
     'PM KISAN ఎవరికి ఇస్తారు?',
     'చిన్న నిల్వ రైతులకు', 'అన్ని రైతులకు', 'కేవలం పెద్ద భూస్వాములకు', 'నిర్దిష్టమైన కేటాయింపు',
     'b',
     'PM KISAN = ఎల్లా రైతులకు ₹6,000/సంవత్సరం. అన్నదాత సుఖీభవ = AP + PM KISAN.'),

    (3, 2,
     'అన్నదాత సుఖీభవ పథకానికి రైతుల నమోదు ఎక్కడ చేపట్టారు?',
     'AP Online + లోక మిత్రం (గ్రామ సచివాలయం) కేంద్రాలు', 'బ్యాంకులు మాత్రమే', 'జిల్లా కలెక్టర్ కార్యాలయం మాత్రమే', 'పోస్ట్ ఆఫీసు',
     'a',
     'అన్నదాత సుఖీభవ నమోదు AP Online (apps.gov.in) మరియు లోక మిత్రం (గ్రామ/వార్డ్ సచివాలయం) కేంద్రాల్లో జరుగుతుంది.'),

    (3, 3,
     'రైతులకు సూపర్ సిక్స్ హామీ సంవత్సర సహాయం ఎంత?',
     '₹15,000', '₹18,000', '₹20,000', '₹25,000',
     'c',
     'అన్నదాత సుఖీభవ = ₹20,000/సంవత్సరం (3 వాయిదాలలో).'),

    (4, 1,
     'తల్లికి వందనం పథకం కింద తల్లికి సంవత్సరానికి ఎంత ఇస్తారు (నెలకు సుమారు ఎంత)?',
     '₹12,000 (₹1,000/నెల)', '₹15,000 (₹1,250/నెల)', '₹18,000 (₹1,500/నెల)', '₹24,000 (₹2,000/నెల)',
     'b',
     'తల్లికి వందనం = ₹15,000/సంవత్సరం (నెలకు సుమారు ₹1,250). నేరుగా తల్లి బ్యాంక్ అకౌంట్‌కు వస్తుంది.'),

    (4, 2,
     'తల్లికి వందనం నమోదు ఏ సంస్థ చేపట్టుంది?',
     'రిటి కేంద్రం', 'బ్యాంక్ నేరుగా', 'AP Online లో', 'పాఠశాల నుండి',
     'c',
     'తల్లికి వందనం నమోదు AP Online గా + బ్యాంక్ ఎంపిక.'),

    (4, 3,
     'తల్లికి వందనం లో తల్లి అకౌంట్ లేకుండా?',
     'ఏమీ విడుదల కాదు', 'విద్యార్థి ఖాతకు', 'పాఠశాల ఖాతకు', 'తండ్రి ఖాతకు',
     'a',
     'తల్లికి వందనం = నిర్దిష్టమైన తల్లి ఖాతకు నేరుగా. ఖాతా లేకుండా అర్హత లేదు.'),

    (5, 1,
     'NTR భరోసా పెన్షన్ చెల్లింపు వ్యవస్థ ఏది?',
     'నగదు', 'బ్యాంక్ ఆధారమైన', 'చెక్కు', 'డిজిటల్ వాలెట్ మాత్రమే',
     'b',
     'NTR భరోసా = డైరెక్ట్ బ్యాంక్ ట్రాన్సఫర్ (DBT) ద్వారా చెల్లింపు.'),

    (5, 2,
     'ఆడబిడ్డ నిధి బేనిఫిషియరీ కేటాయింపు సమయ పరిధి?',
     '6 నెలలు', '1 సంవత్సరం', '2 సంవత్సరాలు', '5 సంవత్సరాలు',
     'b',
     'ఆడబిడ్డ నిధి = 1 సంవత్సరంలో అర్హులకు నమోదు పూర్ణం చేయటానికి లక్ష్యం.'),

    (5, 3,
     'NTR భరోసా పెన్షన్ విధానం - ఇంటర్నల్ వెరిఫికేషన్ సమయం?',
     '15 రోజులు', '30 రోజులు', '45 రోజులు', '60 రోజులు',
     'b',
     'NTR భరోసా విధానం = నమోదు నుండి 30-45 రోజుల్లో నిర్ణయం.'),

    (6, 1,
     'AP అన్నా కేంటీన్ పథకం కింద ఒక భోజనం ధర ఎంత?',
     '₹2', '₹5', '₹10', 'ఉచితం',
     'b',
     'అన్నా కేంటీన్ (Anna Canteen) పథకం కింద AP లో పేదలకు ₹5కు పూర్తి భోజనం (అన్నం, పప్పు, కూరగాయలు) అందిస్తారు. TDP తొలి ప్రభుత్వ కాలంలో ప్రారంభించబడింది; 2024లో పునఃప్రారంభం.'),

    (6, 2,
     'చేనేత కార్మికుల నేత భరోసా ఎంటైటిల్\u200cమెంట్?',
     '₹20,000/సంవత్సరం', '₹25,000/సంవత్సరం', '₹30,000/సంవత్సరం', '₹35,000/సంవత్సరం',
     'b',
     'నేత భరోసా = చేనేత కార్మికులకు ₹25,000/సంవత్సరం + విద్యుత్ స్టిప్పెండ్.'),

    (6, 3,
     'AP లో అన్నా కేంటీన్ చేపట్టిన ఎంపిక రంగాలు ఏమిటి?',
     'పట్టణ', 'గ్రామీణ', 'రెండూ', 'కేటీ డిపెండెంట్',
     'c',
     'అన్నా కేంటీన్ = పట్టణ + గ్రామీణ ప్రాంతాలలో సమానమైన వ్యవస్థ.'),

    (7, 1,
     'సూపర్ సిక్స్ హామీల్లో సర్వాధిక జనసంఖ్య కవరేజ్?',
     'దీపం 2.0', 'NTR భరోసా', 'తల్లికి వందనం', 'ఉచిత బస్సు',
     'b',
     'NTR భరోసా = 65+ లక్షల లాభభోగులు (AP గా అతిపెద్ద అందానీ).'),

    (7, 2,
     'సూపర్ సిక్స్ 6 హామీలలో అత్యధికంగా మహిళా-కేంద్రిత పథకాలు ఎన్ని?',
     '1', '2', '3', '4',
     'c',
     'సూపర్ సిక్స్ లో 3 మహిళా-కేంద్రిత పథకాలు: 1) ఉచిత APSRTC బస్సు (మహిళలు/transgender), 2) తల్లికి వందనం (₹15,000/yr), 3) ఆడబిడ్డ నిధి. మిగిలినవి అన్నదాత సుఖీభవ (రైతులు), నిరుద్యోగ బృతి (నిరుద్యోగులు), దీపం 2.0 (అందరి అర్హులు).'),

    # AUDIT D3 NOTE: "AP సూపర్ సిక్స్ 2026 వరకు బడ్జెట్ అంచనా ₹1,50,000 కోట్లు" MCQ removed —
    # the figure was unsourced/fabricated. AP budget 2025-26 = ₹3,22,359 cr total; individual
    # Super Six scheme allocations are in actual budget docs but a single aggregated "Super Six
    # till 2026" total estimate isn't an officially published AP government number.

]

# ─── Database Integration (for seed loading) ───────────────────────────────────
# This section would contain database seeding functions
# Currently preserved for module structure compatibility


def _seed_ap_ca_div2_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (2, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id IN (SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph})", (2, 'AP_Current_Affairs'))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (2, 'AP_Current_Affairs'))
    if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division2', 2,
         'TDP-BJP-JSP ప్రభుత్వ పథకాలు 2024-2026',
         'TDP-BJP-JSP Government Schemes 2024-2026',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'AP CA Div2 notes seeded!'}


def _seed_ap_ca_div2_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES):
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (2, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div2_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (2, 'AP_Current_Affairs'))
        row = cur.fetchone()
    note_id = row_to_dict(row)['id']
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = f"INSERT INTO chapter_mcqs (study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    for (sec_idx, diff, q_te, a, b, c, d, correct, expl) in MCQ_DATA:
        db_exec(conn, insert_sql, (note_id, sec_idx, diff, q_te, a, b, c, d, str(correct).lower(), expl))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'inserted': len(MCQ_DATA)}
