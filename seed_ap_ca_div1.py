"""
seed_ap_ca_div1.py — AP Current Affairs Division 1: 2024 Elections & Cabinet
ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ — విభాగం 1: 2024 ఎన్నికలు & కేబినెట్

AUDIT CHANGES (2026-05-18):
1. FIXED wrong correct_answer: DCM పవన్ కళ్యాణ్ constituency question —
   was "d" (అనకాపల్లి), corrected to "c" (పిఠాపురం). Pawan Kalyan won from
   Pithapuram, not Anakkapalli. Key fact confirmed.
2. REMOVED 2 junk MCQs: "ఎన్నికల ధర్మం?" (meaningless question/options) and
   "JSP సఫలత సూచన?" (vague category question with no factual value).
3. FIXED DGP: was "చింతలపూడి ద్వారకా తిరుమల", corrected to
   "హరీష్ కుమార్ గుప్తా" (IPS 1992, from Jan 31 2025). Div01 HTML ground truth.
4. FIXED Chief Secretary: was "నీరబ్ కుమార్ ప్రసాద్", corrected to
   "జి. సాయి ప్రసాద్" (IAS 1991, from Mar 1 2026). Div01 HTML ground truth.
5. FIXED Darsi constituency district: was wrong "చిత్తూరు", corrected to
   "ప్రకాశం" — Darsi is in Prakasam district, not Chittoor.

BATCH D1 AUDIT (2026-05-18):
6. PURGED ~44 junk-stem duplicate MCQs (lines 311-525, 535-581 in prior version).
   Bare-stem framing like "JSP విజయం?", "AP లోక్‌సభ స్థానాలు?", "Health మంత్రి?",
   "CBN పోర్ట్‌ఫోలియో?" — these were low-quality duplicates of earlier well-framed
   MCQs (or contained filler options like "సరిగ్గా/తెలియదు/గానీ/లేదు").
   Retained 3 well-framed bureaucracy MCQs (CS, DGP, Governor appointment).
7. FIXED Pithapuram district: was "తూర్పు గోదావరి", corrected to "కాకినాడ"
   (Pithapuram moved to Kakinada district in the 2022 reorganisation).
Result: ~84 MCQs → ~40 MCQs, all well-framed with full context.
"""
import json as _json

SECTIONS_JSON = [
    {
        "title": "2024 AP అసెంబ్లీ ఎన్నికలు",
        "sub": "AP Assembly Elections 2024 — Basic Details",
        "audio": "2024 ఆంధ్రప్రదేశ్ శాసనసభ ఎన్నికలు మే 13, 2024న జరిగాయి. ఫలితాలు జూన్ 4, 2024న ప్రకటించారు. మొత్తం 175 అసెంబ్లీ సీట్లకు ఎన్నికలు జరిగాయి. మెజారిటీ మార్క్ 88. పోలింగ్ శాతం 81.86%. దార్సి నియోజకవర్గంలో అత్యధిక పోలింగ్ 90.91%. తిరుపతి నియోజకవర్గంలో అత్యల్ప పోలింగ్ 63.32%. ఇది లోక్‌సభ ఎన్నికలతో పాటు ఒకేసారి జరిగింది.",
        "html": """<div class="concept-cover">
  <h1>2024 AP Assembly Elections &nbsp;<span class="bi-te">/ 2024 AP అసెంబ్లీ ఎన్నికలు</span></h1>
  <div class="sub">Single phase • May 13, 2024 • 175 seats • Held with Lok Sabha</div>
</div>

<div class="section-hdr">Election Schedule / ఎన్నికల షెడ్యూల్</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total seats</td><td>175 Assembly + 25 Lok Sabha</td><td class="bi-te">175 అసెంబ్లీ + 25 లోక్‌సభ</td></tr>
<tr><td>Polling date</td><td>May 13, 2024 (single phase)</td><td class="bi-te">మే 13, 2024 (ఒకే విడత)</td></tr>
<tr><td>Counting</td><td>June 4, 2024</td><td class="bi-te">జూన్ 4, 2024</td></tr>
<tr><td>Held with</td><td>18th Lok Sabha Elections</td><td class="bi-te">18వ లోక్‌సభ ఎన్నికలతో పాటు</td></tr>
<tr><td>Majority mark</td><td>88 seats</td><td class="bi-te">మెజారిటీ మార్క్: 88</td></tr>
<tr><td>Total voters</td><td>~4.09 crore (~40.9 million)</td><td class="bi-te">~4.09 కోట్ల ఓటర్లు</td></tr>
</table>

<div class="section-hdr">Polling Statistics / పోలింగ్ గణాంకాలు</div>
<table class="key-table">
<tr><th>Metric</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Overall turnout</td><td><b>81.86%</b></td><td class="bi-te">మొత్తం పోలింగ్ శాతం</td></tr>
<tr><td>Highest turnout constituency</td><td>Darsi (Prakasam) — 90.91%</td><td class="bi-te">దార్సి, ప్రకాశం జిల్లా</td></tr>
<tr><td>Lowest turnout constituency</td><td>Tirupati — 63.32%</td><td class="bi-te">తిరుపతి</td></tr>
<tr><td>Postal ballots</td><td>~4.5 lakh (employees, defence, NRI)</td><td class="bi-te">పోస్టల్ బ్యాలెట్లు</td></tr>
</table>

<p><b>Result preview:</b> The TDP-JSP-BJP coalition won 164 of 175 Assembly seats — a record sweep. YSRCP collapsed from 151 (2019) to 11 seats. Chandrababu Naidu (TDP) sworn in as 17th AP CM on June 12, 2024 (4th term).</p>
<p class="bi-te">కూటమి (TDP-JSP-BJP) 164 సీట్లు గెలిచి భారీ విజయం సాధించింది. YSRCP 151 → 11 సీట్లకు పడిపోయింది. చంద్రబాబు 4వసారి AP CM గా జూన్ 12, 2024న ప్రమాణ స్వీకారం చేశారు.</p>"""
    },
    {
        "title": "కూటమి విజయం",
        "sub": "TDP-JSP-BJP Alliance Victory — Seat Count & Vote Share",
        "audio": "TDP-JSP-BJP కూటమి మొత్తం 164 సీట్లు గెలుచుకుంది. TDP 144 నియోజకవర్గాల్లో 135 సీట్లు గెలిచింది. JSP 21 నియోజకవర్గాల్లో పోటీ చేసి 21 సీట్లూ గెలిచింది (100% strike rate!). BJP 10 నియోజకవర్గాల్లో 8 సీట్లు గెలిచింది. కూటమి మొత్తం ఓట్ల శాతం 53% కంటే ఎక్కువ. YSRCP 175 సీట్లు పోటీ చేసి కేవలం 11 సీట్లు గెలిచింది. 2019లో YSRCP 151 సీట్లు గెలిచింది.",
        "html": """<div class="concept-cover">
  <h1>TDP-JSP-BJP Alliance Victory &nbsp;<span class="bi-te">/ కూటమి విజయం</span></h1>
  <div class="sub">164/175 seats • 53.7% vote share • Historic sweep</div>
</div>

<div class="section-hdr">Party-wise Seat Results / పార్టీవారీ ఫలితాలు</div>
<table class="key-table">
<tr><th>Party</th><th>Contested</th><th>Won</th><th>Strike rate</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>TDP</b></td><td>144</td><td><b>135</b></td><td>93.75%</td><td class="bi-te">TDP — 135 సీట్లు</td></tr>
<tr><td><b>JSP</b></td><td>21</td><td><b>21</b></td><td><b>100%</b></td><td class="bi-te">JSP — 100% స్ట్రైక్ రేట్</td></tr>
<tr><td><b>BJP</b></td><td>10</td><td><b>8</b></td><td>80.00%</td><td class="bi-te">BJP — 8 సీట్లు</td></tr>
<tr><td><b>Alliance total</b></td><td>175</td><td><b>164</b></td><td>93.71%</td><td class="bi-te"><b>కూటమి మొత్తం 164</b></td></tr>
<tr><td>YSRCP</td><td>175</td><td>11</td><td>6.29%</td><td class="bi-te">YSRCP 175 లో 11 మాత్రమే</td></tr>
<tr><td>INC + Others</td><td>175+</td><td>0</td><td>0%</td><td class="bi-te">కాంగ్రెస్ + ఇతరులు 0</td></tr>
</table>

<div class="section-hdr">Vote-Share Comparison / ఓట్ల శాతం పోలిక</div>
<table class="key-table">
<tr><th>Party</th><th>2019 vote%</th><th>2024 vote%</th><th>Swing</th></tr>
<tr><td>TDP</td><td>39.17%</td><td>45.60%</td><td>+6.43</td></tr>
<tr><td>JSP</td><td>5.53%</td><td>~6.25%</td><td>+0.72</td></tr>
<tr><td>BJP</td><td>0.84%</td><td>~2.83%</td><td>+1.99</td></tr>
<tr><td><b>Alliance</b></td><td>~45.5%</td><td><b>~53.68%</b></td><td>+8.18</td></tr>
<tr><td>YSRCP</td><td>49.95%</td><td>39.37%</td><td>-10.58</td></tr>
</table>

<p><b>Why a record sweep:</b> The TDP-JSP-BJP seat-sharing was precisely tuned (TDP 144, JSP 21, BJP 10) with no overlap. Combined with the YSRCP's ~10-point vote loss and high anti-incumbency, the alliance converted vote-share into a seat avalanche. Notably, the YSRCP's 39.37% vote (still 2nd highest) yielded just 11 seats — a textbook FPTP collapse.</p>
<p class="bi-te">కూటమి సీట్ల కేటాయింపు నిర్దుష్టంగా (TDP 144 + JSP 21 + BJP 10 = 175) ఏ సీటులోనూ overlap లేకుండా జరిగింది. YSRCP వ్యతిరేకత మరియు 10 శాతం ఓట్ల పతనంతో కూటమి సీట్లుగా మారింది. YSRCP 39.37% ఓట్లు ఉన్నా కేవలం 11 సీట్లు — FPTP వ్యవస్థలో classic collapse.</p>"""
    },
    {
        "title": "లోక్‌సభ ఫలితాలు AP",
        "sub": "Lok Sabha 2024 Results — AP (25 Seats)",
        "audio": "ఆంధ్రప్రదేశ్ నుండి మొత్తం 25 లోక్‌సభ స్థానాలు ఉన్నాయి. TDP 17 స్థానాల్లో పోటీ చేసి 16 గెలిచింది. JSP 2 స్థానాల్లో 2 గెలిచింది (కాకినాడ: తంగెళ్ళ ఉదయ్ శ్రీనివాస్; మచిలీపట్నం: వల్లభనేని బాలశౌరి). BJP 6 స్థానాల్లో 3 గెలిచింది. కూటమి మొత్తం 21 లోక్‌సభ స్థానాలు గెలిచింది. YSRCP 25 స్థానాల్లో 4 మాత్రమే గెలిచింది. పవన్ కళ్యాణ్ పిఠాపురం అసెంబ్లీ MLA మాత్రమే — ఆయన లోక్‌సభ ఎన్నికల్లో పోటీ చేయలేదు. పిఠాపురం పరిధిలో కాకినాడ లోక్‌సభ స్థానంలో JSP తంగెళ్ళ ఉదయ్ శ్రీనివాస్ గెలిచారు.",
        "html": """<div class="concept-cover">
  <h1>Lok Sabha 2024 — AP Results &nbsp;<span class="bi-te">/ లోక్‌సభ ఫలితాలు AP</span></h1>
  <div class="sub">25 LS seats • Alliance won 21 • YSRCP won 4</div>
</div>

<div class="section-hdr">Seat Allocation & Results / సీట్ల కేటాయింపు మరియు ఫలితాలు</div>
<table class="key-table">
<tr><th>Party</th><th>Contested</th><th>Won</th><th>Strike rate</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>TDP</b></td><td>17</td><td><b>16</b></td><td>94.12%</td><td class="bi-te">TDP — 16 సీట్లు</td></tr>
<tr><td><b>JSP</b></td><td>2</td><td><b>2</b></td><td>100%</td><td class="bi-te">JSP — Kakinada + Machilipatnam</td></tr>
<tr><td><b>BJP</b></td><td>6</td><td><b>3</b></td><td>50%</td><td class="bi-te">BJP — 3 సీట్లు</td></tr>
<tr><td><b>Alliance total</b></td><td>25</td><td><b>21</b></td><td>84%</td><td class="bi-te"><b>కూటమి 21</b></td></tr>
<tr><td>YSRCP</td><td>25</td><td>4</td><td>16%</td><td class="bi-te">YSRCP 4 (2019: 22)</td></tr>
</table>

<div class="section-hdr">JSP Lok Sabha Winners / JSP లోక్‌సభ విజేతలు</div>
<table class="key-table">
<tr><th>Constituency</th><th>Winner</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Kakinada</td><td>Tangella Uday Srinivas</td><td class="bi-te">తంగెళ్ళ ఉదయ్ శ్రీనివాస్</td></tr>
<tr><td>Machilipatnam</td><td>Vallabhaneni Balashowry</td><td class="bi-te">వల్లభనేని బాలశౌరి</td></tr>
</table>

<p><b>Pawan Kalyan's situation:</b> JSP chief Pawan Kalyan contested ONLY the Pithapuram Assembly seat (won) — he did NOT contest any Lok Sabha seat in 2024. Within Pithapuram's LS-overlap area, the Kakinada Lok Sabha seat went to fellow JSP candidate Tangella Uday Srinivas.</p>
<p class="bi-te">పవన్ కళ్యాణ్ పిఠాపురం అసెంబ్లీ స్థానం మాత్రమే పోటీ చేసి గెలిచారు — ఆయన లోక్‌సభ ఎన్నికల్లో పోటీ చేయలేదు. పిఠాపురం పరిధిలోని కాకినాడ లోక్‌సభ స్థానంలో JSP తంగెళ్ళ ఉదయ్ శ్రీనివాస్ గెలిచారు.</p>

<p><b>National impact:</b> The TDP became the 3rd-largest party in NDA at the Centre with its 16 LS seats (after BJP 240 and JD-U 12), giving Naidu a crucial role in coalition arithmetic. Two TDP MPs joined the Union Cabinet — K. Ram Mohan Naidu (Civil Aviation) and Pemmasani Chandra Sekhar (MoS, Rural Development).</p>
<p class="bi-te">జాతీయ స్థాయిలో TDP 16 LS సీట్లతో NDA లో 3వ అతిపెద్ద పార్టీగా మారింది. K. రామ్ మోహన్ నాయుడు (పౌర విమానయాన మంత్రి) మరియు పెమ్మసాని చంద్రశేఖర్ (గ్రామీణాభివృద్ధి సహాయ మంత్రి) కేంద్ర కేబినెట్ లో చేరారు.</p>"""
    },
    {
        "title": "కేబినెట్ నిర్మాణం",
        "sub": "Cabinet Formation — Composition & Key Dates",
        "audio": "నాల్గవ నాయుడు మంత్రివర్గం జూన్ 12, 2024న శపథ స్వీకారం చేసింది. జూన్ 14, 2024న పోర్ట్‌ఫోలియో పంపిణీ జరిగింది. మొత్తం 25 మంత్రులు (CM తో సహా). TDP నుండి 21, JSP నుండి 3, BJP నుండి 1 మంత్రి. 17 మంది తొలిసారి మంత్రులు (first-timers). 3 మంది మహిళా మంత్రులు. 8 మంది BC వర్గాల మంత్రులు. 2 SC, 1 ST, 1 Muslim మంత్రులు.",
        "html": """<div class="concept-cover">
  <h1>Cabinet Formation 2024 &nbsp;<span class="bi-te">/ కేబినెట్ నిర్మాణం</span></h1>
  <div class="sub">25 ministers (incl. CM) • Sworn-in Jun 12 • Portfolios Jun 14</div>
</div>

<div class="section-hdr">Key Dates / కీలక తేదీలు</div>
<table class="key-table">
<tr><th>Event</th><th>Date</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Election results</td><td>June 4, 2024</td><td class="bi-te">ఎన్నికల ఫలితాలు</td></tr>
<tr><td>4th Naidu cabinet oath</td><td>June 12, 2024</td><td class="bi-te">శపథ స్వీకారం</td></tr>
<tr><td>Portfolio allocation</td><td>June 14, 2024</td><td class="bi-te">పోర్ట్‌ఫోలియో పంపిణీ</td></tr>
<tr><td>Venue</td><td>Kesarapalli, NTR District (near Vijayawada)</td><td class="bi-te">కేసరపల్లి, NTR జిల్లా</td></tr>
</table>

<div class="section-hdr">Cabinet Composition / కేబినెట్ కూర్పు</div>
<table class="key-table">
<tr><th>Category</th><th>Count</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Total ministers (incl. CM)</td><td><b>25</b></td><td class="bi-te">మొత్తం 25 మంత్రులు</td></tr>
<tr><td>From TDP</td><td>21</td><td class="bi-te">TDP నుండి</td></tr>
<tr><td>From JSP</td><td>3</td><td class="bi-te">JSP నుండి</td></tr>
<tr><td>From BJP</td><td>1</td><td class="bi-te">BJP నుండి (సత్యకుమార్ యాదవ్)</td></tr>
<tr><td>First-time ministers</td><td>17</td><td class="bi-te">తొలిసారి మంత్రులు</td></tr>
<tr><td>Women ministers</td><td>3</td><td class="bi-te">మహిళా మంత్రులు</td></tr>
<tr><td>BC ministers</td><td>8</td><td class="bi-te">BC వర్గాల మంత్రులు</td></tr>
<tr><td>SC / ST / Muslim</td><td>2 / 1 / 1</td><td class="bi-te">SC / ST / ముస్లిం</td></tr>
</table>

<p><b>Social engineering:</b> The cabinet had the highest BC representation (8 out of 25 = 32%) in any AP cabinet to date — a deliberate signal aligned with the alliance's election messaging. The single Muslim minister is Nasyam Mohammad Farooq (TDP, Nandyal) holding Law & Justice + Minority Welfare.</p>
<p class="bi-te">8 మంది BC మంత్రులు (32%) — AP చరిత్రలో అతిపెద్ద BC ప్రాతినిధ్యం. ఏకైక ముస్లిం మంత్రి నాస్యం మొహమ్మద్ ఫారూఖ్ (నంద్యాల) Law & Justice, Minority Welfare పోర్ట్‌ఫోలియో నిర్వహిస్తారు.</p>"""
    },
    {
        "title": "CM & DCM — పదవులు",
        "sub": "Chief Minister & Deputy CM Details",
        "audio": "ముఖ్యమంత్రి నల్లపాటి చంద్రబాబు నాయుడు కుప్పం నియోజకవర్గం నుండి. ఇది ఆయన నాల్గవ సారి ముఖ్యమంత్రి పదవి. TDP స్థాపకుడు NTR (నందమూరి తారక రామారావు) 1982లో స్థాపించారు. CBN GAD, Law & Order, Public Enterprises నిర్వహిస్తారు. ఉపముఖ్యమంత్రి పవన్ కళ్యాణ్ JSP నాయకుడు, పిఠాపురం నుండి. పంచాయతీ రాజ్, గ్రామీణాభివృద్ధి, అడవులు, పర్యావరణం, సైన్స్ అండ్ టెక్నాలజీ పోర్ట్‌ఫోలియో.",
        "html": """<div class="concept-cover">
  <h1>CM & DCM Profiles &nbsp;<span class="bi-te">/ CM &amp; DCM పదవులు</span></h1>
  <div class="sub">Naidu (4th term, Kuppam) • Pawan Kalyan (DCM, Pithapuram)</div>
</div>

<div class="section-hdr">Chief Minister — N. Chandrababu Naidu</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full name</td><td>Nara Chandrababu Naidu (NCBN)</td><td class="bi-te">నల్లపాటి చంద్రబాబు నాయుడు</td></tr>
<tr><td>Born</td><td>April 20, 1950, Naravaripalle (Chittoor)</td><td class="bi-te">ఏప్రిల్ 20, 1950</td></tr>
<tr><td>Constituency</td><td><b>Kuppam</b> (Chittoor) — 9th win</td><td class="bi-te">కుప్పం (చిత్తూరు)</td></tr>
<tr><td>Party</td><td>TDP (founded by NTR, March 29, 1982)</td><td class="bi-te">TDP (NTR 1982లో స్థాపన)</td></tr>
<tr><td>Tenure</td><td><b>4th term</b> as CM (1995-99, 1999-2004, 2014-19, 2024-)</td><td class="bi-te">4వసారి ముఖ్యమంత్రి</td></tr>
<tr><td>Sworn in</td><td>June 12, 2024 (17th CM of AP)</td><td class="bi-te">17వ AP ముఖ్యమంత్రి</td></tr>
<tr><td>Portfolios</td><td>GAD, Law &amp; Order, Public Enterprises, Real Time Governance</td><td class="bi-te">GAD + Law &amp; Order + PE</td></tr>
</table>

<div class="section-hdr">Deputy CM — K. Pawan Kalyan</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Full name</td><td>Konidela Kalyan Babu (stage: Pawan Kalyan)</td><td class="bi-te">కొణిదెల కళ్యాణ్ బాబు</td></tr>
<tr><td>Born</td><td>September 2, 1971, Bapatla</td><td class="bi-te">సెప్టెంబర్ 2, 1971</td></tr>
<tr><td>Constituency</td><td><b>Pithapuram</b> (Kakinada dist) — first-time MLA</td><td class="bi-te">పిఠాపురం (కాకినాడ జిల్లా)</td></tr>
<tr><td>Party</td><td>Jana Sena Party (JSP) — founded March 14, 2014</td><td class="bi-te">జనసేన పార్టీ (2014)</td></tr>
<tr><td>Profession</td><td>Actor (elder brother: Chiranjeevi)</td><td class="bi-te">నటుడు (అన్న: చిరంజీవి)</td></tr>
<tr><td>Portfolios</td><td>Panchayati Raj, Rural Development, Forests, Environment, Science &amp; Tech</td><td class="bi-te">పంచాయతీ రాజ్ + గ్రామీణాభివృద్ధి + అడవులు + పర్యావరణం + S&amp;T</td></tr>
</table>

<p><b>Historic firsts:</b> This is the first AP cabinet with a Deputy CM since 2014 division. JSP joining the cabinet (3 ministers) ended its three-decade outsider phase. Naidu's 4th term makes him the longest-serving AP CM cumulatively (over 14 years across terms).</p>
<p class="bi-te">2014 విభజన తర్వాత AP లో మొదటి ఉపముఖ్యమంత్రి. JSP నుండి 3 మంత్రులు ప్రభుత్వంలో చేరారు. చంద్రబాబు 4 సార్లు మొత్తంగా 14+ సంవత్సరాలు ముఖ్యమంత్రిగా — AP చరిత్రలో ఎక్కువ కాలం.</p>"""
    },
    {
        "title": "కీలక మంత్రులు — పోర్ట్‌ఫోలియో",
        "sub": "Key Ministers and their Portfolios",
        "audio": "నారా లోకేష్ HRD (విద్య), IT ఎలక్ట్రానిక్స్, RTG. వంగలపూడి అనిత Home Affairs, Disaster Management. పయ్యావుల కేశవ్ Finance, Planning, Commercial Taxes — 2025-26 బడ్జెట్ ₹3,22,359 కోట్లు. సత్యకుమార్ యాదవ్ (BJP, ధర్మవరం) Health, Medical Education — BJP నుండి ఏకైక మంత్రి. నాస్యం మొహమ్మద్ ఫారూఖ్ (నంద్యాల) Law & Justice, Minority Welfare — ఏకైక ముస్లిం మంత్రి. కొలుసు పార్థసారథి (నూజివీడు, కృష్ణా జిల్లా) Housing, I&PR. గొట్టిపాటి రవికుమార్ Energy. మండిపల్లి రాంప్రసాద్ రెడ్డి (రాయచోటి) Transport, Youth & Sports. అనగాని సత్యప్రసాద్ Revenue, Stamps & Registration.",
        "html": """<div class="concept-cover">
  <h1>Key Ministers — Portfolios &nbsp;<span class="bi-te">/ కీలక మంత్రులు</span></h1>
  <div class="sub">Lokesh (HRD/IT) • Anita (Home) • Keshav (Finance) • Yadav (Health)</div>
</div>

<div class="section-hdr">High-Profile Portfolios / ముఖ్య పోర్ట్‌ఫోలియోలు</div>
<table class="key-table">
<tr><th>Minister</th><th>Constituency</th><th>Portfolios</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Nara Lokesh</b></td><td>Mangalagiri (Guntur)</td><td>HRD (Education), IT &amp; Electronics, Real-Time Governance</td><td class="bi-te">నారా లోకేష్ (CBN కుమారుడు)</td></tr>
<tr><td><b>Vangalapudi Anita</b></td><td>Payakaraopeta (Anakapalli)</td><td>Home Affairs, Disaster Management</td><td class="bi-te">వంగలపూడి అనిత (హోం)</td></tr>
<tr><td><b>Payyavula Keshav</b></td><td>Uravakonda (Anantapur)</td><td>Finance, Planning, Commercial Taxes</td><td class="bi-te">పయ్యావుల కేశవ్ (ఆర్థిక మంత్రి)</td></tr>
<tr><td><b>Satyakumar Yadav</b> (BJP)</td><td>Dharmavaram (Anantapur)</td><td>Health, Medical Education, Family Welfare</td><td class="bi-te">సత్యకుమార్ యాదవ్ — BJP ఏకైక మంత్రి</td></tr>
<tr><td><b>Nasyam Mohammad Farooq</b></td><td>Nandyal</td><td>Law &amp; Justice, Minority Welfare</td><td class="bi-te">నాస్యం మొహమ్మద్ ఫారూఖ్ — ఏకైక ముస్లిం మంత్రి</td></tr>
</table>

<div class="section-hdr">Other Important Portfolios / ఇతర ముఖ్య పోర్ట్‌ఫోలియోలు</div>
<table class="key-table">
<tr><th>Minister</th><th>Portfolio</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Kolusu Parthasarathy</td><td>Housing, I&amp;PR</td><td class="bi-te">కొలుసు పార్థసారథి (నూజివీడు, కృష్ణా)</td></tr>
<tr><td>Gottipati Ravikumar</td><td>Energy</td><td class="bi-te">గొట్టిపాటి రవికుమార్ (అద్దంకి)</td></tr>
<tr><td>Mandipalli Ramprasad Reddy</td><td>Transport, Youth &amp; Sports</td><td class="bi-te">మండిపల్లి రాంప్రసాద్ రెడ్డి (రాయచోటి)</td></tr>
<tr><td>Anagani Satya Prasad</td><td>Revenue, Stamps &amp; Registration</td><td class="bi-te">అనగాని సత్యప్రసాద్</td></tr>
<tr><td>P. Narayana</td><td>Municipal Administration &amp; Urban Development (MAUD)</td><td class="bi-te">P. నారాయణ — MAUD</td></tr>
<tr><td>Nimmala Ramanaidu</td><td>Water Resources</td><td class="bi-te">నిమ్మల రమానాయుడు (పాలకొల్లు)</td></tr>
</table>

<p><b>Budget 2025-26:</b> Finance Minister Payyavula Keshav presented the AP 2025-26 budget on February 28, 2025 totalling <b>₹3,22,359 crore</b> — with allocations for Super Six schemes, Polavaram, Amaravati. Subsequent 2026-27 Budget tabled in February 2026 with continued Super Six focus.</p>
<p class="bi-te">పయ్యావుల కేశవ్ ఫిబ్రవరి 28, 2025న 2025-26 బడ్జెట్ ₹3,22,359 కోట్లు సమర్పించారు. సూపర్ సిక్స్ + పోలవరం + అమరావతి కేటాయింపులు.</p>"""
    },
    {
        "title": "JSP మంత్రులు & ఇతర మంత్రులు",
        "sub": "JSP Ministers & Other Key Ministers",
        "audio": "JSP నుండి 3 మంత్రులు: పవన్ కళ్యాణ్ (DCM), నాదెండ్ల మనోహర్ (Civil Supplies, Consumer Affairs), కందుల దుర్గేష్ (Tourism, Culture & Cinematography). ఇతర TDP మంత్రులు: P. నారాయణ — MAUD. నిమ్మల రమానాయుడు (పాలకొల్లు) — Water Resources. BC జనార్దన్ రెడ్డి (బనగానపల్లె) — Roads & Buildings, Infrastructure & Investments. కొండపల్లి శ్రీనివాస్ (గజపతినగరం) — MSME, SERP, NRI Affairs. డోలా శ్రీ బాలవీరాంజనేయ స్వామి (కొండపి SC) — Social Welfare, Disabled & Senior Citizen Welfare. వాసంసెట్టి సుభాష్ (రామచంద్రాపురం) — Labour, Factories & Boilers. కొలు రవీంద్ర (మచిలీపట్నం) — Mines & Geology, Excise. అనం రమానారాయణ రెడ్డి (ఆత్మకూరు) — Endowments. తి.గ. భారతి (కర్నూల్) — Industries & Commerce, Food Processing.",
        "html": """<div class="concept-cover">
  <h1>JSP & Remaining Ministers &nbsp;<span class="bi-te">/ JSP &amp; ఇతర మంత్రులు</span></h1>
  <div class="sub">3 JSP cabinet ministers • Constituency-wise allocation</div>
</div>

<div class="section-hdr">JSP Ministers (3) / JSP నుండి 3 మంత్రులు</div>
<table class="key-table">
<tr><th>Minister</th><th>Constituency</th><th>Portfolio</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Pawan Kalyan</b></td><td>Pithapuram (Kakinada)</td><td>Deputy CM + Panchayati Raj/Rural Dev/Forests/Env/S&amp;T</td><td class="bi-te">DCM — JSP అధ్యక్షుడు</td></tr>
<tr><td>Nadendla Manohar</td><td>Tenali (Guntur)</td><td>Civil Supplies, Consumer Affairs, Food Safety</td><td class="bi-te">నాదెండ్ల మనోహర్</td></tr>
<tr><td>Kandula Durgesh</td><td>Nidadavolu (East Godavari)</td><td>Tourism, Culture &amp; Cinematography</td><td class="bi-te">కందుల దుర్గేష్</td></tr>
</table>

<div class="section-hdr">Remaining TDP Ministers / ఇతర TDP మంత్రులు</div>
<table class="key-table">
<tr><th>Minister</th><th>Constituency</th><th>Portfolio</th></tr>
<tr><td>BC Janardhan Reddy</td><td>Banaganapalle</td><td>Roads &amp; Buildings, Infrastructure &amp; Investments</td></tr>
<tr><td>Kondapalli Srinivas</td><td>Gajapathinagaram</td><td>MSME, SERP, NRI Affairs</td></tr>
<tr><td>Dola Sri Balaveeranjaneya Swamy</td><td>Kondapi (SC)</td><td>Social Welfare, Disabled &amp; Senior Citizen Welfare</td></tr>
<tr><td>Vasamsetti Subhash</td><td>Ramachandrapuram</td><td>Labour, Factories &amp; Boilers</td></tr>
<tr><td>Kollu Ravindra</td><td>Machilipatnam</td><td>Mines &amp; Geology, Excise</td></tr>
<tr><td>Anam Ramanarayana Reddy</td><td>Atmakur</td><td>Endowments</td></tr>
<tr><td>T.G. Bharati</td><td>Kurnool</td><td>Industries &amp; Commerce, Food Processing</td></tr>
<tr><td>Kollabathula Manikya Vara Prasada Rao</td><td>Pendurthi</td><td>BC Welfare, Information &amp; Public Relations</td></tr>
</table>

<p><b>Women ministers (3):</b> Vangalapudi Anita (Home), T.G. Bharati (Industries), Savita (Tribal Welfare). <b>SC ministers (2):</b> Dola Swamy + one more. <b>ST minister (1):</b> Gummadi Sandhya Rani (Kuruba, ST Welfare).</p>
<p class="bi-te">3 మహిళా మంత్రులు: వంగలపూడి అనిత (హోం), తి.గ. భారతి (పరిశ్రమలు), సవిత (గిరిజన సంక్షేమం). 2 SC, 1 ST మంత్రులు ఉన్నారు.</p>"""
    },
    {
        "title": "రాజ్యాంగ పదవులు & ముఖ్య వ్యక్తులు",
        "sub": "Constitutional Positions & Key Officials",
        "audio": "ఆంధ్రప్రదేశ్ గవర్నర్ జస్టిస్ ఎస్. అబ్దుల్ నజీర్, ఫిబ్రవరి 2023 నుండి (మాజీ సుప్రీంకోర్టు న్యాయమూర్తి). శాసనసభ స్పీకర్ చింతకాయల అయ్యన్నపాత్రుడు (TDP, నర్సీపట్నం), జూన్ 2024లో ఎన్నుకున్నారు. డిప్యూటీ స్పీకర్ రఘురామ కృష్ణ రాజు (TDP, ఉండి). శాసనమండలి చైర్మన్ కొయ్యే మోషేన్ రాజు — YSRCP పాలన నుండి కొనసాగుతున్నారు. DGP హరీష్ కుమార్ గుప్తా (IPS 1992 batch, జనవరి 31, 2025 నుండి). AP రాష్ట్రసభ స్థానాలు 11. ముఖ్య కార్యదర్శి జి. సాయి ప్రసాద్ (IAS 1991 batch, మార్చి 1, 2026 నుండి). పయ్యావుల కేశవ్ ఆర్థికమంత్రిగా ఫిబ్రవరి 28, 2025న 2025-26 బడ్జెట్ ₹3,22,359 కోట్లు సమర్పించారు.",
        "html": """<div class="concept-cover">
  <h1>Constitutional &amp; Bureaucratic Posts &nbsp;<span class="bi-te">/ రాజ్యాంగ పదవులు</span></h1>
  <div class="sub">Governor • Speaker • DGP • CS • HC CJ</div>
</div>

<div class="section-hdr">Constitutional Posts / రాజ్యాంగ పదవులు</div>
<table class="key-table">
<tr><th>Post</th><th>Holder</th><th>Since</th><th class="bi-te">వివరణ</th></tr>
<tr><td><b>Governor</b></td><td>Justice S. Abdul Nazeer</td><td>Feb 2023</td><td class="bi-te">జస్టిస్ ఎస్. అబ్దుల్ నజీర్ (మాజీ సుప్రీంకోర్టు న్యాయమూర్తి)</td></tr>
<tr><td>Assembly Speaker</td><td>Chintakayala Ayyanna Patrudu</td><td>Jun 2024</td><td class="bi-te">చింతకాయల అయ్యన్నపాత్రుడు (TDP, నర్సీపట్నం)</td></tr>
<tr><td>Deputy Speaker</td><td>Raghurama Krishnam Raju</td><td>Jun 2024</td><td class="bi-te">రఘురామ కృష్ణం రాజు (TDP, ఉండి)</td></tr>
<tr><td>Council Chairman</td><td>Koyye Moshenu Raju</td><td>Cont. from YSRCP era</td><td class="bi-te">కొయ్యే మోషేన్ రాజు</td></tr>
<tr><td>High Court CJ</td><td>Justice Lisa Gill (6th CJ)</td><td>Apr 25, 2026</td><td class="bi-te">జస్టిస్ లిసా గిల్ (6వ CJ)</td></tr>
</table>

<div class="section-hdr">Top Bureaucracy / అధికారిక పదవులు</div>
<table class="key-table">
<tr><th>Post</th><th>Officer</th><th>Batch</th><th>Since</th></tr>
<tr><td><b>Chief Secretary</b></td><td>G. Sai Prasad</td><td>IAS 1991</td><td>Mar 1, 2026</td></tr>
<tr><td><b>DGP</b></td><td>Harish Kumar Gupta</td><td>IPS 1992</td><td>Jan 31, 2025</td></tr>
<tr><td>Finance Secretary</td><td>Peeyush Kumar</td><td>IAS</td><td>—</td></tr>
</table>
<p class="bi-te">CS: జి. సాయి ప్రసాద్ (IAS 1991 batch, మార్చి 1, 2026 నుండి). గతంలో: నీరబ్ కుమార్ ప్రసాద్ (Jun-Dec 2024) → కె. విజయానంద్ (Jan-Feb 2026) → జి. సాయి ప్రసాద్.</p>
<p class="bi-te">DGP: హరీష్ కుమార్ గుప్తా (IPS 1992 batch, జనవరి 31, 2025 నుండి).</p>

<div class="section-hdr">AP Legislature Strength / AP శాసనం</div>
<table class="key-table">
<tr><th>Body</th><th>Seats</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Lok Sabha (AP)</td><td>25</td><td class="bi-te">25 లోక్‌సభ స్థానాలు</td></tr>
<tr><td>Rajya Sabha (AP)</td><td>11</td><td class="bi-te">11 రాజ్యసభ స్థానాలు</td></tr>
<tr><td>Legislative Assembly</td><td>175 (+1 nom. Anglo-Indian abolished 2020)</td><td class="bi-te">175 శాసనసభ స్థానాలు</td></tr>
<tr><td>Legislative Council</td><td>58</td><td class="bi-te">58 శాసన మండలి స్థానాలు</td></tr>
</table>

<p><b>Budget context:</b> FM Payyavula Keshav tabled the AP 2025-26 budget on February 28, 2025 totalling <b>₹3,22,359 crore</b>. The 2026-27 budget was tabled in February 2026 by the same FM, continuing Super Six allocations alongside Polavaram, Amaravati capital city development, and Quantum Valley.</p>
<p class="bi-te">2025-26 బడ్జెట్ ₹3,22,359 కోట్లు ఫిబ్రవరి 28, 2025న పయ్యావుల కేశవ్ సమర్పించారు. 2026-27 బడ్జెట్ ఫిబ్రవరి 2026లో సమర్పించబడింది.</p>"""
    },
]

# MCQ_DATA: (section_idx, difficulty, question_te, opt_a, opt_b, opt_c, opt_d, answer, explanation_te)
MCQ_DATA = [
    (0, 1,
     "2024 AP శాసనసభ ఎన్నికలు ఏ తేదీన జరిగాయి?",
     "మే 13, 2024", "జూన్ 4, 2024", "ఏప్రిల్ 13, 2024", "మే 4, 2024",
     "a",
     "2024 AP అసెంబ్లీ ఎన్నికలు మే 13, 2024న జరిగాయి. ఫలితాలు జూన్ 4, 2024న ప్రకటించారు."),

    (0, 1,
     "2024 AP అసెంబ్లీ ఎన్నికల ఫలితాలు ఏ తేదీన ప్రకటించారు?",
     "జూన్ 4, 2024", "మే 13, 2024", "జూన్ 12, 2024", "జూన్ 14, 2024",
     "a",
     "2024 AP ఎన్నికల ఫలితాలు జూన్ 4, 2024న వెలువడ్డాయి. మే 13న ఓటింగ్ జరిగింది."),

    (0, 1,
     "2024 AP శాసనసభలో మొత్తం ఎన్ని సీట్లు ఉన్నాయి?",
     "170", "178", "175", "180",
     "c",
     "ఆంధ్రప్రదేశ్ శాసనసభలో మొత్తం 175 సీట్లు ఉన్నాయి. మెజారిటీకి 88 సీట్లు అవసరం."),

    (0, 2,
     "2024 AP అసెంబ్లీ ఎన్నికల్లో మొత్తం పోలింగ్ శాతం ఎంత?",
     "81.86%", "75.86%", "79.86%", "85.86%",
     "a",
     "2024 AP అసెంబ్లీ ఎన్నికల్లో మొత్తం పోలింగ్ శాతం 81.86%."),

    (0, 2,
     "2024 AP ఎన్నికల్లో అత్యధిక పోలింగ్ శాతం నమోదు చేసిన నియోజకవర్గం?",
     "తిరుపతి", "విజయవాడ", "దార్సి", "రాజమండ్రి",
     "c",
     "దార్సి (Darsi) నియోజకవర్గంలో అత్యధిక పోలింగ్ 90.91% నమోదైంది."),

    (0, 2,
     "2024 AP ఎన్నికల్లో అత్యల్ప పోలింగ్ శాతం నమోదు చేసిన నియోజకవర్గం?",
     "తిరుపతి", "కర్నూలు", "గుంటూరు", "విజయవాడ",
     "a",
     "తిరుపతి నియోజకవర్గంలో అత్యల్ప పోలింగ్ 63.32% నమోదైంది."),

    (1, 1,
     "2024 AP ఎన్నికల్లో TDP-JSP-BJP కూటమి మొత్తం ఎన్ని సీట్లు గెలిచింది?",
     "164", "160", "170", "175",
     "a",
     "TDP-JSP-BJP కూటమి 175 సీట్లలో 164 సీట్లు గెలుచుకుంది — AP చరిత్రలో అసాధారణ విజయం."),

    (1, 1,
     "2024 AP ఎన్నికల్లో TDP ఎన్ని సీట్లు గెలిచింది?",
     "135", "130", "140", "144",
     "a",
     "TDP 144 నియోజకవర్గాల్లో పోటీ చేసి 135 సీట్లు గెలిచింది."),

    (1, 1,
     "2024 AP ఎన్నికల్లో JSP ఎన్ని సీట్లు పోటీ చేసి ఎన్ని గెలిచింది?",
     "21 లో 21", "21 లో 18", "25 లో 21", "20 లో 21",
     "a",
     "JSP 21 నియోజకవర్గాల్లో పోటీ చేసి 21 సీట్లూ గెలిచింది — 100% strike rate!"),

    (1, 2,
     "2024 AP ఎన్నికల్లో YSRCP ఎన్ని సీట్లు గెలిచింది?",
     "11", "21", "25", "31",
     "a",
     "YSRCP 175 సీట్లు పోటీ చేసి కేవలం 11 సీట్లు గెలిచింది. 2019లో 151 సీట్లు గెలిచింది."),

    (1, 2,
     "2024 AP ఎన్నికల్లో BJP ఎన్ని సీట్లు పోటీ చేసి ఎన్ని గెలిచింది?",
     "10 లో 8", "10 లో 10", "12 లో 8", "8 లో 8",
     "a",
     "BJP 10 నియోజకవర్గాల్లో పోటీ చేసి 8 సీట్లు గెలిచింది."),

    (1, 3,
     "2024 AP ఎన్నికల్లో TDP ఓట్ల శాతం (రాష్ట్రవ్యాప్తంగా) సుమారు ఎంత?",
     "~30%", "~39%", "~45%", "~50%",
     "c",
     "TDP ఓట్ల శాతం 45.6% (రాష్ట్రవ్యాప్తంగా మొత్తం). YSRCP ఓట్ల శాతం 39.37% — సీట్లలో మాత్రమే కాదు, ఓట్లలో కూడా TDP దెబ్బ తీసింది!"),

    (2, 1,
     "ఆంధ్రప్రదేశ్ నుండి మొత్తం ఎన్ని లోక్‌సభ స్థానాలు ఉన్నాయి?",
     "21", "23", "25", "28",
     "c",
     "AP నుండి మొత్తం 25 లోక్‌సభ స్థానాలు ఉన్నాయి."),

    (2, 1,
     "2024 AP లోక్‌సభ ఎన్నికల్లో కూటమి ఎన్ని స్థానాలు గెలిచింది?",
     "21", "19", "23", "25",
     "a",
     "TDP-JSP-BJP కూటమి AP లో 25 లోక్‌సభ స్థానాల్లో 21 గెలిచింది."),

    (2, 2,
     "2024 అసెంబ్లీ ఎన్నికల్లో పవన్ కళ్యాణ్ ఏ నియోజకవర్గం నుండి గెలిచారు? ఆయన లోక్‌సభకు కూడా పోటీ చేశారా?",
     "పిఠాపురం, అసెంబ్లీ మాత్రమే", "అనకాపల్లి, లోక్‌సభ కూడా గెలిచారు", "రాజమండ్రి, అసెంబ్లీ మాత్రమే", "కాకినాడ, లోక్‌సభ మాత్రమే",
     "a",
     "పవన్ కళ్యాణ్ పిఠాపురం అసెంబ్లీ (MLA) నుండి గెలిచారు — లోక్‌సభ ఎన్నికల్లో పోటీ చేయలేదు! కాకినాడ లోక్‌సభ స్థానంలో JSP తంగెళ్ళ ఉదయ్ శ్రీనివాస్ గెలిచారు."),

    (3, 1,
     "చంద్రబాబు నాయుడు నాల్గవ మంత్రివర్గం శపథ స్వీకారం ఏ తేదీన జరిగింది?",
     "జూన్ 12, 2024", "జూన్ 4, 2024", "జూన్ 14, 2024", "జూలై 1, 2024",
     "a",
     "నాల్గవ నాయుడు మంత్రివర్గం జూన్ 12, 2024న శపథ స్వీకారం చేసింది."),

    (3, 1,
     "AP కేబినెట్ 2024లో మొత్తం ఎంత మంది మంత్రులు ఉన్నారు?",
     "20", "22", "25", "30",
     "c",
     "AP కేబినెట్ 2024లో CM తో సహా మొత్తం 25 మంత్రులు ఉన్నారు."),

    (3, 2,
     "AP కేబినెట్ 2024లో TDP నుండి ఎంత మంది మంత్రులు ఉన్నారు?",
     "19", "20", "21", "22",
     "c",
     "AP కేబినెట్‌లో TDP నుండి 21 మంది మంత్రులు ఉన్నారు. JSP నుండి 3, BJP నుండి 1."),

    (3, 2,
     "AP కేబినెట్ 2024లో మొదటిసారి మంత్రి అయిన వారు ఎంత మంది?",
     "10", "13", "17", "20",
     "c",
     "AP కేబినెట్ 2024లో 17 మంది తొలిసారి మంత్రులు (first-time ministers)."),

    (3, 2,
     "AP కేబినెట్ 2024లో మహిళా మంత్రులు ఎంత మంది?",
     "1", "2", "3", "4",
     "c",
     "AP కేబినెట్‌లో 3 మంది మహిళా మంత్రులు ఉన్నారు."),

    (4, 1,
     "AP ముఖ్యమంత్రి చంద్రబాబు నాయుడు ఏ నియోజకవర్గం నుండి?",
     "మంగళగిరి", "నెల్లూరు", "ఉరవకొండ", "కుప్పం",
     "d",
     "చంద్రబాబు నాయుడు కుప్పం నియోజకవర్గం (చిత్తూరు జిల్లా) నుండి ఎన్నికయ్యారు."),

    (4, 1,
     "2024లో AP ఉపముఖ్యమంత్రి పదవి ఎవరికి దక్కింది?",
     "నారా లోకేష్", "పయ్యావుల కేశవ్", "పవన్ కళ్యాణ్", "అచ్చెన్నాయుడు",
     "c",
     "పవన్ కళ్యాణ్ (JSP) AP ఉప ముఖ్యమంత్రి అయ్యారు. ఆయన JSP అధ్యక్షుడు."),

    (4, 1,
     "చంద్రబాబు నాయుడు 2024లో ఎన్నో సారి AP ముఖ్యమంత్రి అయ్యారు?",
     "2వ సారి", "3వ సారి", "4వ సారి", "5వ సారి",
     "c",
     "చంద్రబాబు నాయుడు 2024లో నాల్గవ సారి AP ముఖ్యమంత్రి అయ్యారు."),

    (4, 2,
     "DCM పవన్ కళ్యాణ్ ఏ నియోజకవర్గం నుండి గెలిచారు?",
     "రాపూరు", "రాజమండ్రి", "పిఠాపురం", "అనకాపల్లి",
     "c",
     "పవన్ కళ్యాణ్ పిఠాపురం నియోజకవర్గం (కాకినాడ జిల్లా) నుండి గెలిచారు. (Pithapuram is in Kakinada district post the 2022 reorganisation, not East Godavari.)"),

    (4, 3,
     "CBN పోర్ట్‌ఫోలియోలో కింది వాటిలో ఏది చేర్చలేదు?",
     "GAD", "Public Enterprises", "Law & Order", "Finance",
     "d",
     "CBN నాయుడు GAD, Law & Order, Public Enterprises నిర్వహిస్తారు. Finance పోర్ట్‌ఫోలియో పయ్యావుల కేశవ్‌కు ఇచ్చారు."),

    (5, 1,
     "AP ఆర్థిక మంత్రి (Finance Minister) ఎవరు?",
     "నారా లోకేష్", "అచ్చెన్నాయుడు", "పయ్యావుల కేశవ్", "వంగలపూడి అనిత",
     "c",
     "పయ్యావుల కేశవ్ (TDP) AP ఆర్థిక మంత్రి. ఆయన ఉరవకొండ నియోజకవర్గం (అనంతపురం జిల్లా) నుండి ఎన్నికయ్యారు, ఫిబ్రవరి 28, 2025న బడ్జెట్ సమర్పించారు."),

    (5, 1,
     "AP హోం మంత్రి (Home Minister) ఎవరు?",
     "పవన్ కళ్యాణ్", "నాస్యం ఫారూఖ్", "అచ్చెన్నాయుడు", "వంగలపూడి అనిత",
     "d",
     "వంగలపూడి అనిత (TDP, పాయకరాపేట) AP Home Affairs, Disaster Management మంత్రి."),

    (5, 1,
     "AP IT & HRD మంత్రి ఎవరు?",
     "చంద్రబాబు నాయుడు", "పవన్ కళ్యాణ్", "నారా లోకేష్", "సత్యకుమార్ యాదవ్",
     "c",
     "నారా లోకేష్ (TDP, మంగళగిరి) HRD (Education), IT Electronics & Communications మంత్రి. ఆయన CBN కుమారుడు."),

    (5, 1,
     "AP Health మంత్రి ఎవరు? వారి పార్టీ?",
     "సత్యకుమార్ యాదవ్, BJP", "కొండపల్లి శ్రీనివాస్, TDP", "నాదెండ్ల మనోహర్, JSP", "కందుల దుర్గేష్, JSP",
     "a",
     "సత్యకుమార్ యాదవ్ (BJP, ధర్మవరం) Health, Family Welfare, Medical Education మంత్రి. BJP నుండి ఏకైక మంత్రి!"),

    (5, 2,
     "AP కేబినెట్‌లో BJP నుండి ఏకైక మంత్రి ఎవరు? వారి పోర్ట్‌ఫోలియో?",
     "అనగాని సత్య ప్రసాద్ — Revenue", "నాదెండ్ల మనోహర్ — Civil Supplies", "కందుల దుర్గేష్ — Social Welfare", "సత్యకుమార్ యాదవ్ — Health",
     "d",
     "BJP నుండి సత్యకుమార్ యాదవ్ (ధర్మవరం MLA) ఏకైక మంత్రి — Health, Family Welfare, Medical Education పోర్ట్‌ఫోలియో."),

    (5, 2,
     "AP కేబినెట్‌లో ఏకైక ముస్లిం మంత్రి ఎవరు?",
     "అసదుద్దీన్ ఓవైసీ", "ఇమ్రాన్ ఖాన్", "అబ్దుల్ నజీర్", "నాస్యం మొహమ్మద్ ఫారూఖ్",
     "d",
     "నాస్యం మొహమ్మద్ ఫారూఖ్ (TDP, నంద్యాల) Law & Justice, Minority Welfare మంత్రి — ఏకైక ముస్లిం మంత్రి."),

    (5, 2,
     "AP కేబినెట్‌లో Energy (విద్యుత్) పోర్ట్‌ఫోలియో ఎవరికి?",
     "మండిపల్లి రాంప్రసాద్ రెడ్డి", "కొండపల్లి శ్రీనివాస్", "గొట్టిపాటి రవికుమార్", "అనగాని సత్యప్రసాద్",
     "c",
     "గొట్టిపాటి రవికుమార్ (TDP, అద్దంకి) Energy (విద్యుత్) పోర్ట్‌ఫోలియో నిర్వహిస్తారు."),

    (5, 3,
     "AP Transport & Youth Affairs మంత్రి ఎవరు?",
     "కొండపల్లి శ్రీనివాస్", "నిమ్మల రమానాయుడు", "అనగాని సత్యప్రసాద్", "మండిపల్లి రాంప్రసాద్ రెడ్డి",
     "d",
     "మండిపల్లి రాంప్రసాద్ రెడ్డి (TDP, రాయచోటి) Transport, Youth & Sports పోర్ట్‌ఫోలియో నిర్వహిస్తారు."),

    (6, 1,
     "JSP నుండి AP కేబినెట్‌లో ఎంత మంది మంత్రులు ఉన్నారు?",
     "1", "2", "3", "4",
     "c",
     "JSP నుండి 3 మంది మంత్రులు: పవన్ కళ్యాణ్ (DCM), నాదెండ్ల మనోహర్, కందుల దుర్గేష్."),

    (6, 2,
     "AP Civil Supplies మంత్రి ఎవరు? వారి పార్టీ?",
     "పవన్ కళ్యాణ్, JSP", "కొలుసు పార్థసారథి, TDP", "కందుల దుర్గేష్, JSP", "నాదెండ్ల మనోహర్, JSP",
     "d",
     "నాదెండ్ల మనోహర్ (JSP) Civil Supplies, Consumer Affairs, Food Safety పోర్ట్‌ఫోలియో. JSP నుండి రెండో మంత్రి."),

    (6, 2,
     "AP Tourism, Culture & Cinematography మంత్రి ఎవరు?",
     "నాదెండ్ల మనోహర్", "అచ్చెన్నాయుడు", "సత్యకుమార్ యాదవ్", "కందుల దుర్గేష్",
     "d",
     "కందుల దుర్గేష్ (JSP, నిడదవోలు) Tourism, Culture & Cinematography పోర్ట్‌ఫోలియో నిర్వహిస్తారు. JSP నుండి మూడో మంత్రి."),

    (6, 3,
     "AP MSME, SERP, NRI Affairs మంత్రి ఎవరు?",
     "మండిపల్లి రాంప్రసాద్ రెడ్డి", "గొట్టిపాటి రవికుమార్", "అనగాని సత్యప్రసాద్", "కొండపల్లి శ్రీనివాస్",
     "d",
     "కొండపల్లి శ్రీనివాస్ (TDP, గజపతినగరం) MSME, SERP, NRI Affairs పోర్ట్‌ఫోలియో."),

    (7, 1,
     "2024 నాటికి ఆంధ్రప్రదేశ్ గవర్నర్ ఎవరు?",
     "జస్టిస్ అబ్దుల్ నజీర్", "తమిళిసై సౌందరరాజన్", "బిశ్వభూషణ్ హరిచందన్", "ఆర్ఎన్ రవి",
     "a",
     "జస్టిస్ ఎస్. అబ్దుల్ నజీర్ AP గవర్నర్ (ఫిబ్రవరి 2023 నుండి). ఆయన మాజీ సుప్రీంకోర్టు న్యాయమూర్తి."),

    (7, 1,
     "AP శాసనసభ స్పీకర్ ఎవరు (2024)?",
     "అయ్యన్న పాత్రుడు", "నారా లోకేష్", "పయ్యావుల కేశవ్", "పవన్ కళ్యాణ్",
     "a",
     "చింతకాయల అయ్యన్నపాత్రుడు (TDP, నర్సీపట్నం) జూన్ 2024లో AP శాసనసభ స్పీకర్‌గా ఎన్నుకున్నారు."),

    (7, 2,
     "AP నుండి రాజ్యసభ (Rajya Sabha) స్థానాలు ఎన్ని?",
     "7", "9", "11", "13",
     "c",
     "ఆంధ్రప్రదేశ్ నుండి 11 రాజ్యసభ స్థానాలు ఉన్నాయి."),

    (7, 3,
     "AP Finance Minister పయ్యావుల కేశవ్ ఏ నియోజకవర్గం నుండి ఎన్నికయ్యారు?",
     "నెల్లూరు", "ధర్మవరం", "కుప్పం", "ఉరవకొండ",
     "d",
     "పయ్యావుల కేశవ్ ఉరవకొండ నియోజకవర్గం (అనంతపురం జిల్లా) నుండి ఎన్నికయ్యారు."),

    (7, 2,
     "AP ముఖ్య కార్యదర్శి (Chief Secretary) ఎవరు (మార్చి 2026 నుండి)?",
     "నీరబ్ కుమార్ ప్రసాద్", "కె. విజయానంద్", "జి. సాయి ప్రసాద్", "హరీష్ కుమార్ గుప్తా",
     "c",
     "జి. సాయి ప్రసాద్ (IAS 1991 batch) మార్చి 1, 2026 నుండి AP ముఖ్య కార్యదర్శి. గతంలో: నీరబ్ కుమార్ ప్రసాద్ (Jun–Dec 2024) → కె. విజయానంద్ (Jan–Feb 2026)."),

    # AUDIT 2026-05-18 (Batch D1): Removed ~44 junk-stem duplicate MCQs.
    # Bare-stem framing like "JSP విజయం?", "AP లోక్‌సభ స్థానాలు?", "Health మంత్రి?"
    # was producing low-quality MCQs that duplicated earlier well-framed questions.
    # Retained well-framed bureaucracy MCQs (CS, DGP, Governor appointment).

    (7, 3,
     "AP DGP (పోలీసు డైరెక్టర్ జనరల్) ఎవరు?",
     "నీరబ్ కుమార్ ప్రసాద్", "రఘురామ కృష్ణ రాజు", "హరీష్ కుమార్ గుప్తా", "జి. సాయి ప్రసాద్",
     "c",
     "హరీష్ కుమార్ గుప్తా (IPS 1992 batch) జనవరి 31, 2025 నుండి AP DGP పూర్తి బాధ్యతలు నిర్వహిస్తున్నారు."),

    (7, 1,
     "గవర్నర్ నియమితుడు ఎంచిన సంస్థ?",
     "రాష్ట్ర విధానసభ", "రాష్ట్రపతి", "లోక్‌సభ", "ఉచ్చ న్యాయాలయం",
     "b",
     "AP గవర్నర్ రాష్ట్రపతి ద్వారా నియమితుడయ్యారు."),

]


def _seed_ap_ca_div1_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP Current Affairs Division 1."""
    ph = '%s' if USE_POSTGRES else '?'
    # Ensure table exists
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT 'AP_Current_Affairs',
            subtopic TEXT DEFAULT '',
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '',
            pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if USE_POSTGRES: conn.commit()
    except Exception: pass

    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (1, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True, 'message': 'AP CA Div1 notes already seeded.'}
    if row and force:
        db_exec(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (1, 'AP_Current_Affairs'))
    if USE_POSTGRES: conn.commit()

    db_exec(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division1',
         1,
         '2024 ఎన్నికలు & AP కేబినెట్',
         '2024 Elections & AP Cabinet',
         '',
         _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'AP CA Div1 notes seeded!'}


def _seed_ap_ca_div1_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES):
    """Seed MCQs for AP Current Affairs Division 1."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (1, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div1_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (1, 'AP_Current_Affairs'))
        row = cur.fetchone()
    note_id = row_to_dict(row)['id']
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    for (sec_idx, diff, q_te, a, b, c, d, correct, expl) in MCQ_DATA:
        db_exec(conn, insert_sql,
                (note_id, sec_idx, diff, q_te, a, b, c, d, str(correct).lower(), expl))
    if USE_POSTGRES: conn.commit()
    easy   = sum(1 for m in MCQ_DATA if m[1] == 1)
    medium = sum(1 for m in MCQ_DATA if m[1] == 2)
    hard   = sum(1 for m in MCQ_DATA if m[1] == 3)
    return {
        'success': True,
        'message': f'AP CA Div1 MCQs seeded! Total: {len(MCQ_DATA)}',
        'inserted': len(MCQ_DATA), 'easy': easy, 'medium': medium, 'hard': hard
    }


def seed(conn):
    """Standalone seed function (for direct script execution)."""
    import sqlite3

    class _FakeExec:
        def __init__(self, conn): self.conn = conn
        def __call__(self, c, sql, params=()):
            cur = c.execute(sql, params)
            return cur

    def _row_to_dict(row):
        if hasattr(row, 'keys'):
            return dict(row)
        return {'id': row[0]}

    _seed_ap_ca_div1_notes_inner(conn, _FakeExec(conn), _row_to_dict, False, force=True)
    conn.commit()
    _seed_ap_ca_div1_mcqs_inner(conn, _FakeExec(conn), _row_to_dict, False)
    conn.commit()
    print(f"[seed_ap_ca_div1] Seeded {len(MCQ_DATA)} MCQs for AP CA Division 1")


if __name__ == "__main__":
    import sqlite3, os
    db = os.path.join(os.path.dirname(__file__), "questions.db")
    conn = sqlite3.connect(db)
    seed(conn)
    conn.close()
