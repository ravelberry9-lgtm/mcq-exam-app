"""
seed_ap_ca_div5.py — AP Current Affairs Division 5: Art & Culture
ఆంధ్రప్రదేశ్ కళలు & సంస్కృతి — శాశ్వత & కరెంట్ అఫైర్స్

Sources: Eenadu Pratibha + AP Government + PIB + Web verified
Covers: Classical arts, Folk arts, GI Tags, Festivals, UNESCO, Padma Awards, Cultural Events 2024-2026

AUDIT CHANGES (2026-05-18):
1. FIXED wrong correct_answer: "కుమ్మరి సారె గిన్నిస్ రికార్డు సాధించిన కళాకారుడు
   ఏ జిల్లాకు చెందినవాడు?" — answer was "b" (అనంతపురం) but the section text
   and question context clearly state Kakinada district (Tuni town). Corrected
   to "c" (కాకినాడ).
2. FIXED metadata in _seed_ap_ca_div5_notes_inner: chapter_title_te was set to
   'AP వ్యవసాయం & నీటిపారుదల' and chapter_title_en to 'AP Agriculture &
   Irrigation' — both are wrong. This is Art & Culture division. Corrected to
   'AP కళలు & సంస్కృతి' / 'AP Art & Culture'.
"""
import json as _json

SECTIONS_JSON = [
    {
        "title": "కూచిపూడి నృత్యం — UNESCO అమూర్త వారసత్వం (2008)",
        "sub": "Krishna District | 17th century | UNESCO 2008 | Largest performance: 7,002 dancers (2017, Vizag)",
        "audio": "కూచిపూడి ఆంధ్రప్రదేశ్ కృష్ణా జిల్లాలోని కూచిపూడి గ్రామంలో పుట్టిన శాస్త్రీయ నృత్య-నాటక కళారూపం. 17వ శతాబ్దంలో సిద్ధేంద్ర యోగి మార్గదర్శకత్వంలో అభివృద్ధి చెందింది. 2008లో UNESCO అమూర్త సాంస్కృతిక వారసత్వం (Intangible Cultural Heritage) జాబితాలో చేర్చింది. మూడు అంశాలు: నృత్తం (శుద్ధ నృత్యం) + నృత్యం (భావప్రకటన) + నాట్యం (నాటకం). పళ్ళెంపై నాట్యం ప్రపంచంలో ఏకైక కళారూపం. అతిపెద్ద కూచిపూడి ప్రదర్శన: 7,002 మంది నర్తకులు — AP Social Welfare Residential Society, ఆంధ్ర యూనివర్సిటీ, విశాఖపట్నం, ఏప్రిల్ 11, 2017. పద్మ శ్రీ 2026: దీపికా రెడ్డి — 5 దశాబ్దాల పాటు కూచిపూడి నృత్యాన్ని ప్రపంచవ్యాప్తంగా ప్రచారం చేశారు.",
        "html": """<div class="concept-cover">
  <h1>Kuchipudi Dance &nbsp;<span class="bi-te">/ కూచిపూడి నృత్యం</span></h1>
  <div class="sub">Krishna District • 17th c. Siddhendra Yogi • UNESCO ICH 2008 • 7,002 dancers (Guinness 2017)</div>
</div>

<div class="section-hdr">Origin & Key Facts / మూలం &amp; ముఖ్య విషయాలు</div>
<table class="key-table">
<tr><th>Item</th><th>English</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>Place of origin</td><td>Kuchipudi village, Krishna District, AP</td><td class="bi-te">కూచిపూడి గ్రామం, కృష్ణా జిల్లా</td></tr>
<tr><td>Founder</td><td>Siddhendra Yogi (17th century)</td><td class="bi-te">సిద్ధేంద్ర యోగి (17వ శతాబ్దం)</td></tr>
<tr><td>UNESCO recognition</td><td><b>Intangible Cultural Heritage (2008)</b></td><td class="bi-te">అమూర్త సాంస్కృతిక వారసత్వం (2008)</td></tr>
<tr><td>Form type</td><td>Classical Dance-Drama (one of 8 Indian classical dances)</td><td class="bi-te">శాస్త్రీయ నృత్య-నాటకం</td></tr>
<tr><td>Signature element</td><td>Tarangam — dance on the rim of a brass plate</td><td class="bi-te">తరంగం — పళ్ళెంపై నాట్యం</td></tr>
</table>

<div class="section-hdr">Three Components / మూడు అంశాలు</div>
<table class="key-table">
<tr><th>Component</th><th>Meaning</th><th class="bi-te">అర్థం</th></tr>
<tr><td>Nritta (నృత్తం)</td><td>Pure rhythmic dance</td><td class="bi-te">శుద్ధ నృత్యం (లయ ప్రధానం)</td></tr>
<tr><td>Nritya (నృత్యం)</td><td>Expressive dance (abhinaya)</td><td class="bi-te">భావప్రకటనా నృత్యం</td></tr>
<tr><td>Natya (నాట్యం)</td><td>Dramatic narrative element</td><td class="bi-te">నాటక రూపం</td></tr>
</table>

<div class="section-hdr">Records & Awards / రికార్డులు &amp; పురస్కారాలు</div>
<table class="key-table">
<tr><th>Event</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Guinness Record</td><td>7,002 dancers, Andhra University, Vizag, Apr 11, 2017</td><td class="bi-te">7,002 నర్తకులు, ఆంధ్ర యూనివర్సిటీ</td></tr>
<tr><td>Padma Shri 2026</td><td>Deepika Reddy (Kuchipudi)</td><td class="bi-te">దీపికా రెడ్డి — 5 దశాబ్దాల కెరీర్</td></tr>
</table>

<p><b>Why it matters:</b> Kuchipudi is one of India's eight classical dances and the only one originating from AP. UNESCO's 2008 listing was under the Representative List of Intangible Cultural Heritage of Humanity — it protects the living tradition, not a physical site.</p>
<p class="bi-te">కూచిపూడి భారతదేశంలోని 8 శాస్త్రీయ నృత్యాలలో ఒకటి — AP నుండి ఏకైకం. 2008 UNESCO గుర్తింపు Intangible Cultural Heritage of Humanity కింద — జీవంత సంప్రదాయాన్ని పరిరక్షించడం; భౌతిక ప్రదేశం కాదు.</p>"""
    },
    {
        "title": "AP GI ట్యాగ్‌లు — హస్తకళలు & ఆహార ఉత్పత్తులు",
        "sub": "22+ GI Tags | Kalamkari, Kondapalli, Etikoppaka, Uppada Jamdani, Bobbili Veena, Tirupati Laddu, Araku Coffee",
        "audio": "AP కి 2025 వరకు 22+ GI ట్యాగ్‌లు ఉన్నాయి. హస్తకళలు: కళంకారీ (శ్రీకాళహస్తి + మచిలీపట్నం — రెండు వేర్వేరు GI), తోలు బొమ్మలాట, కొండపల్లి బొమ్మలు (కృష్ణా జిల్లా; పొనికి చెక్క), ఎటికొప్పక బొమ్మలు (400+ సంవత్సరాలు), ఉప్పాడ జంధ్యం (రెండువైపులా ఒకే డిజైన్ — ప్రపంచంలో ఏకైక), వెంకటగిరి చీరలు, ధర్మవరం పట్టు చీరలు, మంగళగిరి చీరలు, బొబ్బిలి వీణ (ఒకే జాకు చెక్క = ఏకాండి వీణ), బుడితి గంటలు, ఉదయగిరి కత్తులు, దుర్గి రాతి శిల్పాలు, అల్లగడ్డ రాతి శిల్పాలు, నరసాపురం క్రోచెట్ లేస్. వ్యవసాయ ఉత్పత్తులు: తిరుపతి లడ్డు, బందరు లడ్డు, అత్రేయాపురం పూతరేకులు, గుంటూరు సన్నం మిరపకాయ, బనగానపల్లె మామిడి, అరకు వ్యాలీ అరేబికా కాఫీ.",
        "html": """<div class="concept-cover">
  <h1>AP Geographical Indication (GI) Tags &nbsp;<span class="bi-te">/ AP GI ట్యాగ్‌లు</span></h1>
  <div class="sub">22+ GI tags • Handicrafts + Food products • Statutory protection (GI Act 1999)</div>
</div>

<div class="section-hdr">Handicraft GIs / హస్తకళల GI</div>
<table class="key-table">
<tr><th>Craft</th><th>Origin</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>Srikalahasti Kalamkari</td><td>Tirupati dist (hand-drawn)</td><td class="bi-te">శ్రీకాళహస్తి కళంకారీ — చేతి గీతలు</td></tr>
<tr><td>Machilipatnam Kalamkari</td><td>Krishna dist (block-print)</td><td class="bi-te">మచిలీపట్నం కళంకారీ — బ్లాక్ ప్రింట్</td></tr>
<tr><td>Kondapalli Toys</td><td>Krishna dist — Poniki wood</td><td class="bi-te">కొండపల్లి బొమ్మలు — పొనికి చెక్క</td></tr>
<tr><td>Etikoppaka Toys</td><td>Anakapalli dist — 400+ yrs, lacquer</td><td class="bi-te">ఎటికొప్పక బొమ్మలు — లాకర్ ఫినిష్</td></tr>
<tr><td>Uppada Jamdani Saree</td><td>Kakinada dist — same design both sides</td><td class="bi-te">ఉప్పాడ జంధ్యం — ఇరువైపులా ఒకే డిజైన్</td></tr>
<tr><td>Bobbili Veena</td><td>Vizianagaram — Ekanda (single Jackwood)</td><td class="bi-te">బొబ్బిలి వీణ — ఏకాండి, జాకు చెక్క</td></tr>
<tr><td>Other textiles</td><td>Venkatagiri, Dharmavaram silk, Mangalagiri</td><td class="bi-te">వెంకటగిరి, ధర్మవరం, మంగళగిరి చీరలు</td></tr>
<tr><td>Stone craft</td><td>Durgi, Allagadda stone sculptures; Udayagiri knives</td><td class="bi-te">దుర్గి, అల్లగడ్డ శిల్పాలు; ఉదయగిరి కత్తులు</td></tr>
<tr><td>Other</td><td>Budithi brass, Narsapur crochet lace, Tholu Bommalata</td><td class="bi-te">బుడితి గంటలు, నరసాపురం క్రోచెట్</td></tr>
</table>

<div class="section-hdr">Food / Agricultural GIs / వ్యవసాయ GI</div>
<table class="key-table">
<tr><th>Product</th><th>Origin</th><th class="bi-te">తెలుగు</th></tr>
<tr><td><b>Tirupati Laddu</b></td><td>TTD prasadam (world's highest-selling)</td><td class="bi-te">తిరుపతి లడ్డు — TTD ప్రసాదం</td></tr>
<tr><td>Bandar Laddu</td><td>Machilipatnam sweet</td><td class="bi-te">బందరు లడ్డు</td></tr>
<tr><td>Atreyapuram Pootharekulu</td><td>East Godavari — rice-paper sweet</td><td class="bi-te">అత్రేయాపురం పూతరేకులు</td></tr>
<tr><td>Guntur Sannam Chilli</td><td>Guntur — long red chilli</td><td class="bi-te">గుంటూరు సన్నం మిరపకాయ</td></tr>
<tr><td>Banaganapalle Mango</td><td>Nandyal dist (also called Benishan)</td><td class="bi-te">బనగానపల్లె మామిడి</td></tr>
<tr><td>Araku Valley Arabica Coffee</td><td>Alluri Sitharama Raju dist — tribal cultivation</td><td class="bi-te">అరకు వ్యాలీ కాఫీ — గిరిజన సేద్యం</td></tr>
</table>

<p><b>What is a GI Tag?</b> A Geographical Indication is a sign that identifies a product as originating from a specific region with qualities linked to that origin. Governed in India by the GI Act, 1999, valid for 10 years (renewable). It prevents commercial misuse and supports local artisans.</p>
<p class="bi-te">GI ట్యాగ్ — ఒక ఉత్పత్తి నిర్దిష్ట భౌగోళిక ప్రాంతం నుండి వచ్చిందని, ఆ ప్రాంత గుణాలు ఉన్నాయని సూచించే చిహ్నం. భారతదేశంలో GI చట్టం 1999 ప్రకారం 10 సంవత్సరాలకు చెల్లుబాటు (పునరుద్ధరించవచ్చు). స్థానిక కళాకారులకు రక్షణ.</p>"""
    },
    {
        "title": "విజయవాడ ఉత్సవ్ 2025 — గిన్నిస్ రికార్డు (డప్పు కళాకారులు)",
        "sub": "Sep 22, 2025 | 11 days | 284 events | 3000+ artists | Largest Dappu Assembly | Guinness Record",
        "audio": "సెప్టెంబర్ 22, 2025న ప్రారంభమైన విజయవాడ ఉత్సవ్ 11 రోజులు; 284 కార్యక్రమాలు. విజయదశమి నాడు 'విజయవాడ దసరా కార్నివాల్ వాక్' — ఇందిరాగాంధీ మైదానం నుండి బెంజి సర్కిల్ వరకు 3 కి.మీ. మేర 3,000 మంది కళాకారులు. అతిపెద్ద డప్పు కళాకారుల సమ్మేళనానికి గిన్నిస్ రికార్డు (Largest Dappu Artists Assembly). CM నారా చంద్రబాబు నాయుడుకు సర్టిఫికెట్ అందించారు. ప్రదర్శించిన కళారూపాలు: డప్పు, నాసిక్ డ్రమ్స్, కళిక, లంబాడీ, దిమ్సా, కోలాటం, కూచిపూడి, కథకళి, అఘోర, గొరిల్లా నృత్యం.",
        "html": """<div class="concept-cover">
  <h1>Vijayawada Utsav 2025 &nbsp;<span class="bi-te">/ విజయవాడ ఉత్సవ్ 2025</span></h1>
  <div class="sub">Sep 22 - Oct 2, 2025 • 11 days • 284 events • Guinness — Largest Dappu Assembly</div>
</div>

<div class="section-hdr">Festival Snapshot / ఉత్సవం వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Start date</td><td>September 22, 2025</td><td class="bi-te">సెప్టెంబర్ 22, 2025</td></tr>
<tr><td>Duration</td><td>11 days (concluded on Vijayadashami)</td><td class="bi-te">11 రోజులు</td></tr>
<tr><td>Total events</td><td>284 cultural programmes</td><td class="bi-te">284 కార్యక్రమాలు</td></tr>
<tr><td>Total artists</td><td>3,000+ performers</td><td class="bi-te">3,000+ కళాకారులు</td></tr>
<tr><td>Carnival route</td><td>Indira Gandhi Stadium → Benz Circle (3 km)</td><td class="bi-te">ఇందిరాగాంధీ మైదానం → బెంజి సర్కిల్</td></tr>
</table>

<div class="section-hdr">Guinness Record / గిన్నిస్ రికార్డు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Record category</td><td><b>Largest Dappu Artists Assembly</b></td><td class="bi-te">అతిపెద్ద డప్పు కళాకారుల సమ్మేళనం</td></tr>
<tr><td>Certificate presented to</td><td>CM N. Chandrababu Naidu</td><td class="bi-te">CM చంద్రబాబు నాయుడు</td></tr>
<tr><td>Occasion</td><td>Vijayadashami (Vijayawada Dasara Carnival Walk)</td><td class="bi-te">విజయవాడ దసరా కార్నివాల్ వాక్</td></tr>
</table>

<div class="section-hdr">Art Forms Featured / ప్రదర్శించిన కళారూపాలు</div>
<table class="key-table">
<tr><th>Type</th><th>Examples</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>Telugu folk</td><td>Dappu, Kolatam, Kalika</td><td class="bi-te">డప్పు, కోలాటం, కళిక</td></tr>
<tr><td>Tribal</td><td>Lambadi, Dhimsa, Gorilla dance</td><td class="bi-te">లంబాడీ, దిమ్సా, గొరిల్లా</td></tr>
<tr><td>Classical</td><td>Kuchipudi, Kathakali</td><td class="bi-te">కూచిపూడి, కథకళి</td></tr>
<tr><td>Other</td><td>Nasik Drums, Aghora</td><td class="bi-te">నాసిక్ డ్రమ్స్, అఘోర</td></tr>
</table>

<p><b>Significance:</b> The Dappu (or Tappeta Gullu) is a traditional AP percussion instrument played by SC-community drummers. The Guinness record showcases the state's commitment to reviving folk arts and giving them international visibility. The 3 km Dasara Carnival Walk is now positioned as an annual cultural anchor for Vijayawada tourism.</p>
<p class="bi-te">డప్పు AP సాంప్రదాయ తాళవాద్యం (SC-సమాజ కళాకారులు ఎక్కువగా వాయిస్తారు). ఈ గిన్నిస్ రికార్డు జానపద కళలకు అంతర్జాతీయ గుర్తింపునిచ్చింది. 3 కి.మీ. దసరా కార్నివాల్ ఇకపై వార్షిక సాంస్కృతిక ఆకర్షణగా మారనుంది.</p>"""
    },
    {
        "title": "కుమ్మరి సారె గిన్నిస్ రికార్డు — తిరుమలనీడి సాయి, తుని (Dec 2025)",
        "sub": "Dec 9, 2025 | World's Smallest Motorized Potter's Wheel | 91 grams | 67x50x47mm | Tuni, Kakinada",
        "audio": "కాకినాడ జిల్లా తుని పట్టణానికి చెందిన తిరుమలనీడి సాయి ప్రపంచంలో అతి చిన్న మోటారుతో నడిచే కుమ్మరి సారె తయారు చేసి గిన్నిస్ రికార్డు సాధించారు. కొలతలు: 67 మి.మీ. పొడవు × 50 మి.మీ. వెడల్పు × 47 మి.మీ. ఎత్తు; బరువు 91 గ్రాములు. ప్లాస్టిక్ షీటు, DC మోటారు, ఇనుప చక్రం, చిన్న బ్యాటరీతో గంటలో సిద్ధం. జూన్ 10న వీడియో పంపగా, డిసెంబరు 9, 2025న ధ్రువపత్రం అందింది. సాయి 2023లో 33 గ్రాముల అతి చిన్న వాషింగ్ మెషిన్ కూడా గిన్నిస్ రికార్డులో చేర్చారు.",
        "html": """<div class="concept-cover">
  <h1>Smallest Potter's Wheel — Guinness &nbsp;<span class="bi-te">/ కుమ్మరి సారె గిన్నిస్</span></h1>
  <div class="sub">Tirumalanidi Sai • Tuni, Kakinada • 91 g • Dec 9, 2025</div>
</div>

<div class="section-hdr">The Achiever / కళాకారుడు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Name</td><td>Tirumalanidi Sai</td><td class="bi-te">తిరుమలనీడి సాయి</td></tr>
<tr><td>Hometown</td><td>Tuni, <b>Kakinada district</b></td><td class="bi-te">తుని, కాకినాడ జిల్లా</td></tr>
<tr><td>Previous Guinness</td><td>2023 — World's smallest washing machine (33 g)</td><td class="bi-te">2023 — 33 గ్రా. వాషింగ్ మెషిన్</td></tr>
</table>

<div class="section-hdr">The Record / రికార్డు వివరాలు</div>
<table class="key-table">
<tr><th>Spec</th><th>Value</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Category</td><td>World's smallest motorized potter's wheel</td><td class="bi-te">అతి చిన్న మోటారు కుమ్మరి సారె</td></tr>
<tr><td>Length</td><td>67 mm</td><td class="bi-te">పొడవు 67 మి.మీ.</td></tr>
<tr><td>Width</td><td>50 mm</td><td class="bi-te">వెడల్పు 50 మి.మీ.</td></tr>
<tr><td>Height</td><td>47 mm</td><td class="bi-te">ఎత్తు 47 మి.మీ.</td></tr>
<tr><td>Weight</td><td><b>91 grams</b></td><td class="bi-te"><b>91 గ్రాములు</b></td></tr>
<tr><td>Materials</td><td>Plastic sheet, DC motor, iron disc, small battery</td><td class="bi-te">ప్లాస్టిక్ షీటు + DC మోటారు + ఇనుప చక్రం</td></tr>
<tr><td>Build time</td><td>1 hour</td><td class="bi-te">గంటలో పూర్తి</td></tr>
<tr><td>Video submitted</td><td>June 10, 2025</td><td class="bi-te">జూన్ 10, 2025న వీడియో</td></tr>
<tr><td>Certificate</td><td>December 9, 2025</td><td class="bi-te">డిసెంబర్ 9, 2025న సర్టిఫికెట్</td></tr>
</table>

<p><b>Cultural angle:</b> The potter's wheel (kummari saare) is one of the oldest tools in Indian craft. Tuni in Kakinada district is part of AP's traditional pottery belt. Sai's miniature works combine grassroots craft knowledge with electronics — a unique India-made innovation that has earned two Guinness records within three years.</p>
<p class="bi-te">కుమ్మరి సారె భారతీయ చేతిపనుల్లోని పురాతన పనిముట్టు. తుని AP సాంప్రదాయ కుమ్మరి ప్రాంతం. సాయి సూక్ష్మ నమూనాలు సాంప్రదాయ చేతిపని జ్ఞానం + ఎలక్ట్రానిక్స్‌ను కలిపి — మూడేళ్లలో రెండు గిన్నిస్ రికార్డులు సాధించారు.</p>"""
    },
    {
        "title": "UNESCO Tentative List 2025 — తిరుమల కొండలు & ఎర్రమట్టి దిబ్బలు",
        "sub": "Aug 27, 2025 | Tirumala Hills (Silathoranam) | Erra Matti Dibbalu (Bhimili, 1500 acres) | 3 worldwide",
        "audio": "ఆగస్టు 27, 2025న AP యొక్క రెండు ప్రదేశాలు UNESCO World Heritage Tentative List లో చేర్చబడ్డాయి. తిరుమల కొండలు: 2.5 బిలియన్ సంవత్సరాల రాళ్ళు + Proterozoic శిలల కలయిక (Eparchaean Unconformity); సిలాతోరణం (Silathoranam) — 1.5 బిలియన్ సంవత్సరాల సహజ రాతి వంపు. ఎర్రమట్టి దిబ్బలు (Erra Matti Dibbalu): భీమిలి, విశాఖపట్నం; 1,500 ఎకరాల తీర ప్రాంతం; ప్రపంచంలో కేవలం 3 మాత్రమే అటువంటి భూ నిర్మాణాలు; జాతీయ జియో-హెరిటేజ్ మాన్యుమెంట్; 1886లో ఆంగ్లేయ భూవిజ్ఞానశాస్త్రవేత్త William King అధ్యయనం. Tentative List = మొదటి దశ మాత్రమే; పూర్తి World Heritage Site కాదు. 2025లో మొత్తం 7 భారత స్థలాలు చేర్చబడ్డాయి.",
        "html": """<div class="concept-cover">
  <h1>UNESCO Tentative List 2025 &nbsp;<span class="bi-te">/ UNESCO అస్థిర జాబితా 2025</span></h1>
  <div class="sub">Aug 27, 2025 • Tirumala Hills + Erra Matti Dibbalu • 2 AP sites among 7 India entries</div>
</div>

<div class="section-hdr">Site 1 — Tirumala Hills / తిరుమల కొండలు</div>
<table class="key-table">
<tr><th>Feature</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Location</td><td>Tirupati district, AP</td><td class="bi-te">తిరుపతి జిల్లా</td></tr>
<tr><td>Key formation</td><td><b>Silathoranam</b> — natural stone arch, 1.5 billion years old</td><td class="bi-te">సిలాతోరణం — 1.5 బిలియన్ సంవత్సరాల సహజ రాతి వంపు</td></tr>
<tr><td>Geological boundary</td><td>Eparchaean Unconformity (~2.5 billion year rocks)</td><td class="bi-te">Eparchaean Unconformity</td></tr>
<tr><td>Significance</td><td>One of the rarest natural arches in Asia</td><td class="bi-te">ఆసియాలోని అరుదైన సహజ ఆర్చ్</td></tr>
</table>

<div class="section-hdr">Site 2 — Erra Matti Dibbalu / ఎర్రమట్టి దిబ్బలు</div>
<table class="key-table">
<tr><th>Feature</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Location</td><td>Bhimili, <b>Visakhapatnam district</b></td><td class="bi-te">భీమిలి, విశాఖపట్నం</td></tr>
<tr><td>Area</td><td>~1,500 acres of coastal red-sand dunes</td><td class="bi-te">1,500 ఎకరాలు తీర ఎర్రమట్టి దిబ్బలు</td></tr>
<tr><td>Global rarity</td><td><b>Only 3 such coastal formations in the world</b></td><td class="bi-te">ప్రపంచంలో 3 మాత్రమే</td></tr>
<tr><td>First studied</td><td>William King (British geologist), 1886</td><td class="bi-te">William King — 1886లో</td></tr>
<tr><td>National status</td><td>National Geo-Heritage Monument (GSI)</td><td class="bi-te">జాతీయ జియో-హెరిటేజ్ మాన్యుమెంట్</td></tr>
</table>

<div class="section-hdr">Process & Context / ప్రక్రియ</div>
<table class="key-table">
<tr><th>Stage</th><th>Meaning</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>Tentative List</td><td>First step — countries shortlist sites</td><td class="bi-te">తొలి దశ — దేశం షార్ట్‌లిస్ట్</td></tr>
<tr><td>Nomination Dossier</td><td>Detailed dossier (after 1+ year)</td><td class="bi-te">విస్తృత నివేదిక</td></tr>
<tr><td>Final inscription</td><td>UNESCO World Heritage Committee</td><td class="bi-te">UNESCO కమిటీ నిర్ణయం</td></tr>
</table>

<p><b>Important distinction:</b> The Tentative List is NOT a World Heritage Site. It is merely a list of properties a State Party intends to nominate. In August 2025, India added 7 new sites; AP contributed 2 (Tirumala + Erra Matti Dibbalu). India now has 62 sites on the Tentative List and 43 inscribed World Heritage Sites.</p>
<p class="bi-te">ముఖ్య గమనిక: Tentative List అంటే World Heritage Site కాదు — ఇది దేశం nominate చేయాలనుకునే ప్రాంతాల జాబితా మాత్రమే. ఆగస్టు 2025లో భారతదేశం 7 కొత్త ప్రాంతాలు చేర్చింది; AP నుండి 2 (తిరుమల + ఎర్రమట్టి దిబ్బలు).</p>"""
    },
    {
        "title": "తెలుగు సాంస్కృతిక కేంద్రం, అమరావతి — ₹119.27 కోట్లు (Mar 2026)",
        "sub": "₹119.27 Crore | CRDA 59th meeting Mar 10, 2026 | Neerukonda | 2000-seat auditorium | Telugu language museum",
        "audio": "మార్చి 10, 2026న సీఆర్‌డీఏ 59వ సమావేశం (CM చంద్రబాబు అధ్యక్షతన) ₹119.27 కోట్లతో అమరావతిలో తెలుగు సాంస్కృతిక కేంద్రం నిర్మించాలని ఆమోదించింది. స్థానం: నీరుకొండ, అమరావతి; 5 ఎకరాలు. సదుపాయాలు: 2,000-సీట్ల ఆడిటోరియం + 1,000 మంది ఓపెన్-ఎయిర్ థియేటర్ + తెలుగు భాష మ్యూజియం. నిర్మాణం: 95,170 చ.అ.; G+1; గ్రీన్ బిల్డింగ్ నిబంధనలు; EPC విధానం. అమలు: అమరావతి గ్రోత్ అండ్ ఇన్‌ఫ్రాస్ట్రక్చర్ కార్పొరేషన్. CM వ్యాఖ్యలు: 'తెలుగు వైభవాన్ని ప్రపంచానికి చాటిచెప్పేలా అమరావతిని అభివృద్ధి చేయాలి'.",
        "html": """<div class="concept-cover">
  <h1>Telugu Cultural Centre, Amaravati &nbsp;<span class="bi-te">/ తెలుగు సాంస్కృతిక కేంద్రం</span></h1>
  <div class="sub">₹119.27 crore • CRDA 59th meeting (Mar 10, 2026) • Neerukonda • 2,000-seat auditorium</div>
</div>

<div class="section-hdr">Approval & Location / అనుమతి &amp; ప్రదేశం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Approving body</td><td>CRDA (Capital Region Development Authority)</td><td class="bi-te">CRDA</td></tr>
<tr><td>Meeting</td><td><b>59th CRDA meeting</b>, Mar 10, 2026</td><td class="bi-te">59వ సీఆర్‌డీఏ సమావేశం</td></tr>
<tr><td>Chair</td><td>CM N. Chandrababu Naidu</td><td class="bi-te">CM చంద్రబాబు అధ్యక్షతన</td></tr>
<tr><td>Cost</td><td><b>₹119.27 crore</b></td><td class="bi-te">₹119.27 కోట్లు</td></tr>
<tr><td>Location</td><td>Neerukonda, Amaravati capital region</td><td class="bi-te">నీరుకొండ, అమరావతి</td></tr>
<tr><td>Land area</td><td>5 acres</td><td class="bi-te">5 ఎకరాలు</td></tr>
</table>

<div class="section-hdr">Facilities / సదుపాయాలు</div>
<table class="key-table">
<tr><th>Component</th><th>Capacity / Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Indoor auditorium</td><td><b>2,000 seats</b></td><td class="bi-te">2,000-సీట్ల ఆడిటోరియం</td></tr>
<tr><td>Open-air theatre</td><td>1,000 people</td><td class="bi-te">1,000 మంది ఓపెన్-ఎయిర్</td></tr>
<tr><td>Telugu Language Museum</td><td>Heritage of Telugu language &amp; literature</td><td class="bi-te">తెలుగు భాష మ్యూజియం</td></tr>
<tr><td>Built-up area</td><td>95,170 sq ft (G+1)</td><td class="bi-te">95,170 చ.అ.</td></tr>
<tr><td>Construction norm</td><td>Green Building, EPC mode</td><td class="bi-te">గ్రీన్ బిల్డింగ్ + EPC</td></tr>
<tr><td>Executing agency</td><td>Amaravati Growth &amp; Infrastructure Corporation</td><td class="bi-te">అమరావతి గ్రోత్ &amp; ఇన్‌ఫ్రాస్ట్రక్చర్ కార్పొరేషన్</td></tr>
</table>

<p><b>Strategic vision:</b> CM Naidu has positioned Amaravati as the cultural showcase of the Telugu people. The centre will host classical music, dance, theatre and Telugu-language preservation activities. It complements other capital-region cultural projects like the Handloom Museum and complements the Avakai Festival (Jan 2026) anchor events.</p>
<p class="bi-te">CM వ్యాఖ్యలు: "తెలుగు వైభవాన్ని ప్రపంచానికి చాటిచెప్పేలా అమరావతిని అభివృద్ధి చేయాలి". కేంద్రం శాస్త్రీయ సంగీతం, నృత్యం, రంగస్థలం, తెలుగు భాషా పరిరక్షణ కార్యక్రమాలు నిర్వహిస్తుంది. చేనేత మ్యూజియం + ఆవకాయ ఫెస్టివల్ తో పాటు అమరావతి సాంస్కృతిక కేంద్రంగా రూపాంతరం.</p>"""
    },
    {
        "title": "నేతన్న భరోసా & హ్యాండ్లూమ్ మ్యూజియం (Aug 7, 2025)",
        "sub": "₹25,000/family/year | National Handloom Day Aug 7 | Mangalagiri | Handloom Museum Amaravati | Free electricity",
        "audio": "జాతీయ చేనేత దినోత్సవం (ఆగస్టు 7, 2025) నాడు మంగళగిరిలో CM చంద్రబాబు నేతన్న భరోసా పథకం ప్రకటించారు. చేనేత కార్మికులకు ₹25,000/కుటుంబం/సంవత్సరం. ఉచిత విద్యుత్: చేనేత మగ్గాలకు 200 యూనిట్లు, మరమగ్గాలకు 500 యూనిట్లు. వ్యయం ₹193 కోట్లు/సంవత్సరం. GST: 5% చేనేత వస్త్రాలపై ప్రభుత్వమే రీయింబర్స్ (₹15 కోట్లు). అమరావతి రాజధాని నగరంలో హ్యాండ్లూమ్ మ్యూజియం ఏర్పాటు.",
        "html": """<div class="concept-cover">
  <h1>Nethanna Bharosa &amp; Handloom Museum &nbsp;<span class="bi-te">/ నేతన్న భరోసా</span></h1>
  <div class="sub">National Handloom Day (Aug 7, 2025) • Mangalagiri • ₹25,000/family/yr</div>
</div>

<div class="section-hdr">Scheme Snapshot / పథకం వివరాలు</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Announced on</td><td>National Handloom Day, Aug 7, 2025</td><td class="bi-te">జాతీయ చేనేత దినోత్సవం</td></tr>
<tr><td>Venue of launch</td><td>Mangalagiri (Guntur dist)</td><td class="bi-te">మంగళగిరి</td></tr>
<tr><td>Announced by</td><td>CM N. Chandrababu Naidu</td><td class="bi-te">CM చంద్రబాబు</td></tr>
<tr><td>Direct cash benefit</td><td><b>₹25,000/family/year</b></td><td class="bi-te">₹25,000/కుటుంబం/సంవత్సరం</td></tr>
<tr><td>Annual outlay</td><td>~₹193 crore/year</td><td class="bi-te">₹193 కోట్లు/సంవత్సరం</td></tr>
</table>

<div class="section-hdr">Power &amp; GST Benefits / విద్యుత్ &amp; GST లాభాలు</div>
<table class="key-table">
<tr><th>Component</th><th>Benefit</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Free power — handloom</td><td>200 units/month</td><td class="bi-te">చేనేత మగ్గాలు: 200 యూనిట్లు</td></tr>
<tr><td>Free power — powerloom</td><td>500 units/month</td><td class="bi-te">మరమగ్గాలు: 500 యూనిట్లు</td></tr>
<tr><td>GST reimbursement</td><td>5% GST on handloom fabrics reimbursed by State</td><td class="bi-te">5% GST రీయింబర్స్</td></tr>
<tr><td>GST reimbursement outlay</td><td>~₹15 crore</td><td class="bi-te">₹15 కోట్లు</td></tr>
</table>

<div class="section-hdr">Handloom Museum, Amaravati / చేనేత మ్యూజియం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">వివరణ</th></tr>
<tr><td>Location</td><td>Amaravati Capital City</td><td class="bi-te">అమరావతి రాజధాని</td></tr>
<tr><td>Purpose</td><td>Showcase AP weaves — Mangalagiri, Venkatagiri, Dharmavaram silk, Uppada Jamdani, Pochampally borders</td><td class="bi-te">AP చేనేతలు: మంగళగిరి, వెంకటగిరి, ధర్మవరం, ఉప్పాడ ప్రదర్శన</td></tr>
</table>

<p><b>Context — National Handloom Day:</b> Observed on August 7 every year (since 2015) to commemorate the Swadeshi Movement launch (Aug 7, 1905). AP has historically been a top handloom state with 1.2+ lakh handloom workers. Nethanna Bharosa restores direct income support after the prior YSRCP-era scheme was discontinued.</p>
<p class="bi-te">జాతీయ చేనేత దినోత్సవం: 2015 నుండి ప్రతి సంవత్సరం ఆగస్టు 7న — 1905 స్వదేశీ ఉద్యమం ప్రారంభాన్ని స్మరిస్తూ. AP లో 1.2 లక్షల+ చేనేత కార్మికులు. నేతన్న భరోసా YSRCP తర్వాతి కాలంలో ఆగిన ప్రత్యక్ష ఆర్థిక సహాయాన్ని పునరుద్ధరిస్తోంది.</p>"""
    },
    {
        "title": "ఆవకాయ ఫెస్టివల్ & ఇతర సాంస్కృతిక వేడుకలు 2025-2026",
        "sub": "Avakai Festival Jan 8-10, 2026 | Vijayawada | 28 events | Free | Punnami Ghat | Jaggannathota State Festival",
        "audio": "ఆవకాయ: అమరావతి ఫెస్టివల్ ఆఫ్ సినిమా, కల్చర్ అండ్ లిటరేచర్ — జనవరి 8–10, 2026; పున్నమి ఘాట్ + భవాని ఐలాండ్, విజయవాడ; 28 ప్రత్యేక కార్యక్రమాలు + 4 వర్క్‌షాపులు; ఉచిత ప్రవేశం. జగ్గన్నఠోట ప్రభలోత్సవం: 17వ శతాబ్దం నుండి; 11 రుద్రప్రభల ఉత్సవం; సంక్రాంతి కనుమ నాడు; డాక్టర్ B.R. అంబేద్కర్ కోనసీమ జిల్లా — ప్రభుత్వం రాష్ట్ర పండుగగా ప్రకటించింది. పర్యేట ఉత్సవం (అహోబిళం): INTACH ద్వారా UNESCO అమూర్త వారసత్వం హోదా కోసం ప్రయత్నం. పద్మ పురస్కారాలు: 2025 పద్మ భూషణ్ (కళ) — నందమూరి బాలకృష్ణ; 2026 పద్మ శ్రీ (కళ) — దీపికా రెడ్డి (కూచిపూడి).",
        "html": """<div class="concept-cover">
  <h1>Avakai Festival & Cultural Events 2025-2026 &nbsp;<span class="bi-te">/ ఆవకాయ &amp; సాంస్కృతిక వేడుకలు</span></h1>
  <div class="sub">Avakai Jan 8-10, 2026 • Jaggannathota state festival • Padma Awards</div>
</div>

<div class="section-hdr">Avakai — Amaravati Festival of Cinema, Culture &amp; Literature</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>Dates</td><td>January 8-10, 2026 (3 days)</td><td class="bi-te">జనవరి 8-10, 2026</td></tr>
<tr><td>Venue</td><td>Punnami Ghat + Bhavani Island, Vijayawada</td><td class="bi-te">పున్నమి ఘాట్ + భవాని ఐలాండ్</td></tr>
<tr><td>Inaugurated by</td><td>CM N. Chandrababu Naidu</td><td class="bi-te">CM చంద్రబాబు నాయుడు</td></tr>
<tr><td>Programmes</td><td>28 events + 4 workshops</td><td class="bi-te">28 కార్యక్రమాలు + 4 వర్క్‌షాపులు</td></tr>
<tr><td>Entry</td><td>Free</td><td class="bi-te">ఉచిత ప్రవేశం</td></tr>
<tr><td>Themes</td><td>Telugu films, literature, music, food, Krishna riverfront tourism push</td><td class="bi-te">తెలుగు సినిమా/సాహిత్యం/సంగీతం/ఆహారం</td></tr>
</table>

<div class="section-hdr">Jaggannathota Prabhalotsavam / జగ్గన్నఠోట ప్రభలోత్సవం</div>
<table class="key-table">
<tr><th>Item</th><th>Detail</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>Origin</td><td>17th century</td><td class="bi-te">17వ శతాబ్దం</td></tr>
<tr><td>Location</td><td>Dr. B.R. Ambedkar Konaseema District (Mori village area)</td><td class="bi-te">డా. B.R. అంబేద్కర్ కోనసీమ జిల్లా</td></tr>
<tr><td>Form</td><td><b>11 Rudraprabhas</b> (decorated temple chariots/columns) festival</td><td class="bi-te">11 రుద్రప్రభల ఉత్సవం</td></tr>
<tr><td>Day</td><td>Sankranti — Kanuma day</td><td class="bi-te">సంక్రాంతి కనుమ నాడు</td></tr>
<tr><td>Status (2026)</td><td>Declared an <b>official State Festival</b> by AP government</td><td class="bi-te">రాష్ట్ర పండుగగా AP ప్రభుత్వ ప్రకటన</td></tr>
</table>

<div class="section-hdr">Other Cultural Initiatives / ఇతర సాంస్కృతిక చర్యలు</div>
<table class="key-table">
<tr><th>Initiative</th><th>Detail</th><th class="bi-te">తెలుగు</th></tr>
<tr><td>Paryata Utsavam, Ahobilam</td><td>INTACH effort for UNESCO Intangible Cultural Heritage status</td><td class="bi-te">పర్యేట ఉత్సవం — INTACH UNESCO ICH ప్రయత్నం</td></tr>
<tr><td>Padma Bhushan 2025 (Art)</td><td>Nandamuri Balakrishna (Telugu cinema)</td><td class="bi-te">2025 పద్మ భూషణ్ — నందమూరి బాలకృష్ణ</td></tr>
<tr><td>Padma Shri 2026 (Art)</td><td>Deepika Reddy (Kuchipudi)</td><td class="bi-te">2026 పద్మ శ్రీ — దీపికా రెడ్డి</td></tr>
</table>

<p><b>Why it matters:</b> The 2026 cultural calendar shows AP's deliberate cultural-tourism push — Avakai is its flagship modern festival (cinema + literature + cuisine), while Jaggannathota's state-festival recognition is a heritage signal. The Ahobilam UNESCO push, if successful, would be AP's second living-tradition listing after Kuchipudi (2008).</p>
<p class="bi-te">2026 సాంస్కృతిక క్యాలెండర్ AP యొక్క సాంస్కృతిక-పర్యాటక ప్రాధాన్యతను చూపిస్తుంది — ఆవకాయ ఆధునిక ఫెస్టివల్ (సినిమా + సాహిత్యం + ఆహారం), జగ్గన్నఠోటకు రాష్ట్ర పండుగ హోదా వారసత్వ సంకేతం. అహోబిళం UNESCO ప్రయత్నం విజయవంతమైతే 2008 కూచిపూడి తర్వాత AP నుండి రెండవ జీవంత సంప్రదాయ గుర్తింపు."""
    },
]

# MCQ_DATA: (section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, answer, explanation_te)
MCQ_DATA = [
    # Section 0 — Kuchipudi
    (0, 1,
     "కూచిపూడి నృత్యం UNESCO అమూర్త సాంస్కృతిక వారసత్వంగా ఏ సంవత్సరం గుర్తింపు పొందింది?",
     "2003", "2006", "2008", "2010",
     "c",
     "కూచిపూడి 2008లో UNESCO Intangible Cultural Heritage of Humanity జాబితాలో చేర్చబడింది. Tangible/World Heritage Site కాదు — ఇది అమూర్త వారసత్వం."),

    (0, 1,
     "కూచిపూడి నృత్యం ఏ జిల్లాలోని గ్రామం నుండి ఉద్భవించింది?",
     "గుంటూరు", "కృష్ణా", "ఏలూరు", "నంద్యాల",
     "b",
     "కూచిపూడి నృత్యం కృష్ణా జిల్లాలోని కూచిపూడి గ్రామంలో పుట్టింది. సిద్ధేంద్ర యోగి 17వ శతాబ్దంలో దీనిని ప్రసిద్ధం చేశారు."),

    (0, 2,
     "అతిపెద్ద కూచిపూడి నృత్య ప్రదర్శనకు గిన్నిస్ రికార్డు — ఎంత మంది నర్తకులు పాల్గొన్నారు?",
     "5,000 మంది", "4,782 మంది", "7,002 మంది", "3,782 మంది",
     "c",
     "7,002 నర్తకులతో AP Social Welfare Residential Educational Institutions Society ఆంధ్ర యూనివర్సిటీ మైదానంలో ఏప్రిల్ 11, 2017న గిన్నిస్ రికార్డు సృష్టించింది."),

    (0, 2,
     "కూచిపూడి నృత్యంలో 'నాట్యం' దేనిని సూచిస్తుంది?",
     "శుద్ధ నృత్యం", "భావప్రకటన", "నాటక రూపం", "సంగీతం",
     "c",
     "కూచిపూడి మూడు అంశాలు: నృత్తం (శుద్ధ నృత్యం), నృత్యం (భావప్రకటన), నాట్యం (నాటక రూపం). నాట్యం = drama/theatrical aspect."),

    # Section 1 — GI Tags
    (1, 1,
     "కళంకారీ చిత్రకళ AP లో ఏ రెండు ప్రాంతాలలో ప్రసిద్ధమైనది?",
     "విశాఖ + విజయవాడ", "శ్రీకాళహస్తి + మచిలీపట్నం", "తిరుపతి + అనంతపురం", "కాకినాడ + రాజమహేంద్రవరం",
     "b",
     "కళంకారీ రెండు ప్రాంతాలు: శ్రీకాళహస్తి (చేతి గీతాల శైలి) + మచిలీపట్నం (బ్లాక్ ప్రింటింగ్ శైలి) — రెండింటికీ వేర్వేరు GI ట్యాగ్‌లు ఉన్నాయి."),

    (1, 1,
     "కొండపల్లి బొమ్మలు ఏ రకమైన చెక్కతో తయారు చేస్తారు?",
     "టేకు చెక్క", "సాగు చెక్క", "పొనికి చెక్క", "జాకు చెక్క",
     "c",
     "కొండపల్లి బొమ్మలు 'పొనికి చెక్క' తో తయారు చేస్తారు — ఇది తేలికపాటి, మృదువైన చెక్క. కృష్ణా జిల్లా కొండపల్లిలో 16వ శతాబ్దం నుండి ఈ కళ అభివృద్ధి చెంది ఉంది."),

    (1, 2,
     "బొబ్బిలి వీణను ఏ ప్రత్యేక పేర్లతో పిలుస్తారు?",
     "కచ్ఛపీ వీణ / త్రిగుణ వీణ", "సరస్వతి వీణ / ఏకాండి వీణ", "వీచిత్ర వీణ / హంస వీణ", "మహతి వీణ / ఆలాపిని వీణ",
     "b",
     "బొబ్బిలి వీణను 'సరస్వతి వీణ' లేదా 'ఏకాండి వీణ' అని పిలుస్తారు. 'ఏకాండి' అంటే ఒకే చెక్క ముక్కతో చేసిన వీణ — జాకు చెక్కను ఉపయోగిస్తారు."),

    (1, 1,
     "ఉప్పాడ జంధ్యం సారె యొక్క ప్రత్యేకత ఏమిటి?",
     "పూత రంగులతో ముద్రిస్తారు", "ఇరువైపులా ఒకే డిజైన్ కనిపిస్తుంది", "బంగారు రంగులో మాత్రమే నేస్తారు", "సిల్కు + కాటన్ మిశ్రమం",
     "b",
     "ఉప్పాడ జంధ్యం సారె ప్రత్యేకత: ఇరువైపులా ఒకే డిజైన్ కనిపించే అరుదైన నేత సాంకేతికత. ప్రపంచంలో ఏకైక అటువంటి చేనేత. తూర్పు గోదావరి జిల్లా ఉప్పాడ."),

    (1, 2,
     "AP లో తిరుపతి లడ్డు GI ట్యాగ్ కింద ఏ సంస్థ ఉత్పత్తి చేస్తుంది?",
     "AP Horticulture Department", "Tirupati Municipal Corporation", "Tirumala Tirupati Devasthanams (TTD)", "AP Food Processing Authority",
     "c",
     "తిరుపతి లడ్డు TTD (Tirumala Tirupati Devasthanams) ప్రసాదం. ఇది ప్రపంచంలో అత్యధికంగా అమ్మే ప్రసాదం. TTD కి GI ట్యాగ్ కింద రక్షణ ఉంది."),

    # Section 2 — Vijayawada Utsav Guinness
    (2, 1,
     "విజయవాడ ఉత్సవ్ 2025 గిన్నిస్ రికార్డు ఏ కళారూపానికి సంబంధించింది?",
     "కూచిపూడి నర్తకులు", "డప్పు కళాకారులు", "కళంకారీ చిత్రకారులు", "తోలు బొమ్మలాట కళాకారులు",
     "b",
     "అతిపెద్ద డప్పు కళాకారుల సమ్మేళనానికి (Largest Dappu Assembly) గిన్నిస్ రికార్డు. విజయవాడ దసరా కార్నివాల్ వాక్ లో 3,000+ కళాకారులు, 2,000+ డప్పు కళాకారులు."),

    (2, 2,
     "విజయవాడ ఉత్సవ్ 2025 — కార్నివాల్ ఏ మార్గంలో జరిగింది?",
     "తాండవ మైదానం → కనకదుర్గ ఆలయం", "ఇందిరాగాంధీ మైదానం → బెంజి సర్కిల్", "ఎగ్జిబిషన్ గ్రౌండ్ → PNB జంక్షన్", "అఘాపే → స్టేషన్ రోడ్",
     "b",
     "విజయవాడ దసరా కార్నివాల్ వాక్ ఇందిరాగాంధీ మైదానం నుండి బెంజి సర్కిల్ వరకు 3 కి.మీ. మేర జరిగింది."),

    # Section 3 — Kummari Saare Guinness
    (3, 1,
     "కుమ్మరి సారె గిన్నిస్ రికార్డు సాధించిన కళాకారుడు ఏ జిల్లాకు చెందినవాడు?",
     "విశాఖపట్నం", "అనంతపురం", "కాకినాడ", "గుంటూరు",
     "c",
     "తిరుమలనీడి సాయి కాకినాడ జిల్లా తుని పట్టణానికి చెందినవాడు. 91 గ్రాముల అతి చిన్న మోటారు కుమ్మరి సారెకు డిసెంబరు 9, 2025న గిన్నిస్ సర్టిఫికెట్ అందింది."),

    (3, 2,
     "తిరుమలనీడి సాయి కుమ్మరి సారె బరువు ఎంత?",
     "33 గ్రాములు", "67 గ్రాములు", "91 గ్రాములు", "120 గ్రాములు",
     "c",
     "91 గ్రాముల బరువు గల అతి చిన్న మోటారుతో నడిచే కుమ్మరి సారెకు గిన్నిస్ రికార్డు. సాయి 2023లో 33 గ్రాముల అతి చిన్న వాషింగ్ మెషిన్ కూడా రికార్డు నమోదు చేశారు."),

    # Section 4 — UNESCO Tentative List
    (4, 1,
     "ఎర్రమట్టి దిబ్బలు (Erra Matti Dibbalu) ఏ జిల్లాలో ఉన్నాయి?",
     "తూర్పు గోదావరి", "విశాఖపట్నం", "శ్రీకాకుళం", "అల్లూరి సీతారామ రాజు",
     "b",
     "ఎర్రమట్టి దిబ్బలు భీమిలి, విశాఖపట్నం జిల్లాలో ఉన్నాయి. 1,500 ఎకరాల తీర ప్రాంతం. ఆగస్టు 27, 2025న UNESCO World Heritage Tentative List లో చేర్చబడ్డాయి."),

    (4, 2,
     "ఎర్రమట్టి దిబ్బలు ప్రపంచంలో ఎన్ని మాత్రమే అటువంటి భూ నిర్మాణాలు ఉన్నాయి?",
     "5", "10", "3", "7",
     "c",
     "ప్రపంచంలో కేవలం 3 మాత్రమే అటువంటి coastal geomorphological formations ఉన్నాయి. 1886లో ఆంగ్లేయ భూవిజ్ఞానశాస్త్రవేత్త William King మొదట అధ్యయనం చేశారు."),

    (4, 2,
     "తిరుమల కొండల 'సిలాతోరణం' ఎంత పురాతనమైనది?",
     "500 మిలియన్ సంవత్సరాలు", "1.5 బిలియన్ సంవత్సరాలు", "2.5 బిలియన్ సంవత్సరాలు", "750 మిలియన్ సంవత్సరాలు",
     "b",
     "తిరుమల కొండల 'సిలాతోరణం' (Silathoranam — Natural Stone Arch) 1.5 బిలియన్ సంవత్సరాలు పురాతనమైనది. Eparchaean Unconformity లో 2.5 బిలియన్ సంవత్సరాల రాళ్ళు ఉన్నాయి."),

    # Section 5 — Telugu Cultural Centre
    (5, 1,
     "అమరావతిలో తెలుగు సాంస్కృతిక కేంద్రానికి CRDA ఎంత వ్యయం ఆమోదించింది?",
     "₹89 కోట్లు", "₹150 కోట్లు", "₹119.27 కోట్లు", "₹200 కోట్లు",
     "c",
     "మార్చి 10, 2026న CRDA 59వ సమావేశం ₹119.27 కోట్లతో తెలుగు సాంస్కృతిక కేంద్రం నిర్మించాలని ఆమోదించింది. స్థానం: నీరుకొండ, అమరావతి."),

    (5, 2,
     "అమరావతి తెలుగు సాంస్కృతిక కేంద్రంలో ఉండే ఆడిటోరియం సీట్లు ఎన్ని?",
     "500 సీట్లు", "1,000 సీట్లు", "1,500 సీట్లు", "2,000 సీట్లు",
     "d",
     "2,000-సీట్ల ఆడిటోరియం + 1,000 మంది ఓపెన్-ఎయిర్ థియేటర్ + తెలుగు భాష మ్యూజియం ఉంటాయి. 5 ఎకరాల స్థలంలో EPC విధానంలో నిర్మిస్తారు."),

    # Section 6 — Nettanna Bharosa
    (6, 1,
     "నేతన్న భరోసా పథకం కింద చేనేత కార్మికులకు ఏటా ఎంత ఆర్థిక సహాయం?",
     "₹10,000", "₹15,000", "₹25,000", "₹50,000",
     "c",
     "నేతన్న భరోసా పథకం కింద చేనేత కార్మికులకు ₹25,000/కుటుంబం/సంవత్సరం. ఆగస్టు 7, 2025 జాతీయ చేనేత దినోత్సవం నాడు మంగళగిరిలో CM ప్రకటించారు."),

    # Section 7 — Festivals and Awards
    (7, 1,
     "2025లో పద్మ భూషణ్ (కళ) పురస్కారం పొందిన తెలుగు సినీ నటుడు?",
     "చిరంజీవి", "నాగార్జున", "నందమూరి బాలకృష్ణ", "వెంకటేష్",
     "c",
     "నందమూరి బాలకృష్ణ 2025లో పద్మ భూషణ్ (కళ) పురస్కారం పొందారు. 5 దశాబ్దాల తెలుగు సినిమా కెరీర్. రాష్ట్రపతి ద్రౌపది ముర్ము అందించారు."),

    (7, 1,
     "2026 పద్మ శ్రీ (కళ) పొందిన కూచిపూడి నర్తకి?",
     "సోభనా నాయుడు", "రాధా రెడ్డి", "యామిని కృష్ణమూర్తి", "దీపికా రెడ్డి",
     "d",
     "దీపికా రెడ్డి 2026 పద్మ శ్రీ (కళ) పొందారు. 5 దశాబ్దాల పాటు కూచిపూడి నృత్యాన్ని ప్రపంచవ్యాప్తంగా ప్రచారం చేశారు."),

    (7, 2,
     "ఆవకాయ ఫెస్టివల్ (జనవరి 2026) ఏ ప్రదేశంలో జరిగింది?",
     "అమరావతి కేపిటల్ రిజియన్", "రాజమహేంద్రవరం రివర్‌ఫ్రంట్", "పున్నమి ఘాట్, విజయవాడ", "భీమిలి బీచ్, విశాఖ",
     "c",
     "ఆవకాయ: అమరావతి ఫెస్టివల్ ఆఫ్ సినిమా, కల్చర్ అండ్ లిటరేచర్ — జనవరి 8–10, 2026, పున్నమి ఘాట్ + భవాని ఐలాండ్, విజయవాడ. 28 కార్యక్రమాలు + 4 వర్క్‌షాపులు. ఉచిత ప్రవేశం."),

    (7, 3,
     "జగ్గన్నఠోట ప్రభలోత్సవం ఏ జిల్లాలో జరుగుతుంది?",
     "శ్రీకాకుళం", "నల్గొండ", "Dr. B.R. అంబేద్కర్ కోనసీమ", "పశ్చిమ గోదావరి",
     "c",
     "జగ్గన్నఠోట ప్రభలోత్సవం డాక్టర్ B.R. అంబేద్కర్ కోనసీమ జిల్లా (జగ్గన్నఠోట)లో జరుగుతుంది. 17వ శతాబ్దం నుండి; 11 రుద్రప్రభల ఉత్సవం. AP ప్రభుత్వం రాష్ట్ర పండుగగా ప్రకటించింది."),

    (7, 2,
     "పర్యేట ఉత్సవం (Paruveta) ఏ ఆలయంలో జరుగుతుంది?",
     "తిరుమల వేంకటేశ్వర", "శ్రీశైలం మల్లికార్జున", "అహోబిళం శ్రీ నారసింహస్వామి", "కనక దుర్గ విజయవాడ",
     "c",
     "పర్యేట ఉత్సవం అహోబిళం (నంద్యాల జిల్లా) లోని శ్రీ నారసింహస్వామి ఆలయంలో జనవరి-ఫిబ్రవరిలో జరుగుతుంది. INTACH ద్వారా UNESCO అమూర్త వారసత్వం హోదా కోసం ప్రయత్నాలు జరుగుతున్నాయి."),
]


def _seed_ap_ca_div5_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 5."""
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (5, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (5, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division5', 5,
         'AP కళలు & సంస్కృతి',
         'AP Art & Culture',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div5 notes seeded!'}
def _seed_ap_ca_div5_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA Division 5 — AP Art & Culture."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (5, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div5_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (5, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print("[div5-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    # Always delete-then-reinsert so seed-file changes are reflected (Postgres dict-row safe).
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    for sec_idx, diff, q, a, b, c, d, ans, expl in MCQ_DATA:
        db_exec(conn, insert_sql, (note_id, sec_idx, diff, q, a, b, c, d, str(ans).lower(), expl))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'inserted': len(MCQ_DATA)}
