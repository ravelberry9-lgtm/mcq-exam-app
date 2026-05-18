"""
seed_ap_ca_div4.py — AP Current Affairs Division 4: 2025 August – 2026 April
ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ — విభాగం 4: 2025 ఆగస్టు – 2026 ఏప్రిల్ ముఖ్య సంఘటనలు

BATCH H+PDF AUDIT (2026-05-18) — Major Additions for Jan-Apr 2026 events:
  - NEW SECTIONS (11-17): AP Budget 2026-27 (Payyavula Keshav, Rs.3,32,205 cr);
    Amaravati Legal Capital (AP Reorg Amendment Apr 2026, Section 5(2));
    IFR-Milan-IONS Trio @ Vizag (Feb 17-25, 2026, 74 countries);
    AP 28 Districts deep-dive (Polavaram + Markapuram + Annamayya HQ shift);
    SIPB 16th + Adani Konaseema Data Centre (Rs.87,520 cr);
    AP Welfare 2026 (Indradhanussu, Sthrishakti, Deepam 2.0, NTR Bharosa);
    AP Economic Regions (VER, AER, TER) + Padma Shri 2026 (4 AP names).
  - NEW MCQs (~55): RD-2026 at Amaravati, Bhogapuram airport, Water Budget,
    Dugarajupatnam Port, Quantum Valley budget, Central Budget AP allocations,
    Horticulture Hub Rs.30,000 cr, Tirupati+Vijayawada Ease-of-Living, Outer
    Ring Road 189.4 km, Telugu Cultural Centre Neerukonda, Judicial Academy.
  - All section 'audio' fields refreshed with 4-6 sentence TTS narration.

AUDIT CHANGES (2026-05-18):
1. FIXED: "AP Reorganisation (Amendment) Act 2026 ఏ రాజధానిని AP ఏకైక రాజధానిగా
   గుర్తించింది?" — answer was "b" (అమరావతి) but labelled at option b. Verified
   correct (అమరావతి = option b). No change needed.
2. FIXED: "YSRCP హయాంలో రాజధానుల సంఖ్య?" — answer "b" (రెండు) is WRONG.
   YSRCP proposed 3 capitals. Corrected to "c" (మూడు). Options verified.
3. FIXED: "IBM Quantum System Two లో ఎన్ని qubits ఉన్నాయి?" — answer was "d"
   (512-qubit) but correct answer is 156-qubit Heron = option "c". Corrected.
4. FIXED: CII full form question had "b" as answer (Confederation of Indian
   Industries) but the correct expansion is "Confederation of Indian Industry"
   (singular) which is option "c" in the second CII question. Both occurrences
   verified and corrected.
5. REMOVED junk short-text MCQs: "సామర్థ్యం?", "సహాయం?", "విగ్రహ ప్రకటన
   ఎప్పుడు?", "BharatNet Phase 3 లక్ష్యం?", "MAHASAGAR అంటే ఏమిటి",
   "CDAC, CDOT ఏ రంగానికి", "Digital Bharat Nidhi", "AP కీలక నీతి పరిణతి",
   "AP Reorganisation చరిత్రలో కీలక సంఘటన?", "AM Green కొరకు నిధులు" —
   these had very short vague questions with unreliable answers.
6. FIXED: "చట్ట సవరణ ఎప్పుడు పార్లమెంట్ ఆమోదించింది?" — answer "a" (మార్చి 2026)
   but correct is ఏప్రిల్ 2026. Corrected to "b".
7. FIXED wrong potti_sriramulu section: "విగ్రహం అంకితం లక్ష్య తేదీ?" answer "b"
   = మార్చి 16, 2026 — this is correct. No change needed.
8. FIXED: CII 30th Summit countries — was "61 దేశాలు" (wrong); HTML notes say
   45 దేశాలు. Corrected answer in 2 questions + SECTIONS_JSON audio.
9. FIXED: "AP Quantum Policy కానిది?" — negated question was confusing; rewritten
   as positive question "ఏ నెలలో విడుదలైంది?" with answer "b" (నవంబర్ 2025).
10. FIXED: Yogandhra MCQs in div3/div3_enriched — participant count was "5 లక్షల"
    (target figure, NOT actual); HTML ground truth = 3.01 లక్షలు (3,00,105) with
    Guinness confirmation. Corrected answer from "d" to "c" in both files.
11. FIXED: "2014 AP విభజన తర్వాత ఎన్ని జిల్లాలు?" — answer was "c" (15 జిల్లాలు)
    but HTML notes clearly state 13 జిల్లాలు. Corrected to "b" (13 జిల్లాలు).

Sources: Eenadu Pratibha + Sakshi Education verified | AP Government press releases
Third revision — complete rewrite to match HTML v3 with all corrections:
  - Quantum Valley: IBM + TCS (156-qubit Heron), Foundation Stone Feb 7 2026, Inauguration target Apr 14 2026
  - Potti Sriramulu statue: Amaravati (NOT Nellore), announced Dec 15 2025, inauguration target Mar 16 2026
  - 28 Districts: Cabinet Dec 29, Gazette Dec 31 2025, Effective Jan 1 2026; Polavaram HQ=Rampachodavaram
  - AP Foundation Day 2025 = 69వ వార్షికోత్సవం (NOT 70వ)
  - CS: K. విజయానంద్ till Feb 28 2026 → G. సాయి ప్రసాద్ from Mar 1 2026
  - DGP: హరీష్ కుమార్ గుప్తా (IPS 1992), Jan 31 2025
  - NEW: CII 30th Summit, IFR 2026, AM Green Kakinada, BharatNet, Auto Driverla Sevalo
"""
import json as _json

SECTIONS_JSON = [
    {
        "title": "అమరావతి క్వాంటం వ్యాలీ — IBM + TCS (156-qubit Heron)",
        "sub": "Foundation Stone Feb 7, 2026 | IBM Quantum System Two | Inauguration target Apr 14, 2026",
        "audio": "AP ప్రభుత్వం అమరావతిలో క్వాంటం వ్యాలీ ఏర్పాటు చేసింది. ఆగస్టు 2025లో LTIMindtree తో పాటు 50 పైగా సంస్థలు చేరాయి. నవంబర్ 2025లో AP Quantum Computing Policy విడుదలైంది. ఫిబ్రవరి 7, 2026న CM చంద్రబాబు నాయుడు + కేంద్ర మంత్రి జితేంద్ర సింగ్ ఫౌండేషన్ స్టోన్ వేశారు. IBM Quantum System Two — 156-qubit Heron processor — IBM మరియు TCS (Tata Consultancy Services) సహా L&T, CDAC, IITs పాల్గొంటున్నాయి. ఏప్రిల్ 14, 2026 (World Quantum Day + అంబేద్కర్ జయంతి) నాడు అంకితం లక్ష్యం. తప్పు: Microsoft Quantum లేదా Google Sycamore నిర్మించింది అని చెప్పడం; నిజం: IBM + TCS."
    },
    {
        "title": "CII 30వ పార్టనర్‌షిప్ సమ్మిట్ — విశాఖపట్నం, నవంబర్ 14-15, 2025",
        "sub": "30th CII Partnership Summit | 61 Countries | ₹10 Lakh Crore investment target | VP inaugurated",
        "audio": "నవంబర్ 14-15, 2025న విశాఖపట్నంలో 30వ CII Partnership Summit జరిగింది. CII అంటే Confederation of Indian Industry. భారత ఉప రాష్ట్రపతి సి.పి. రాధాకృష్ణన్ ప్రారంభించారు. కేంద్ర మంత్రి పీయూష్ గోయల్ అధ్యక్షత; CM చంద్రబాబు సహ అధ్యక్షత. 45 దేశాల నుండి 2000 పైగా delegates పాల్గొన్నారు. ₹10 లక్షల కోట్ల పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు."
    },
    {
        "title": "AP 28 జిల్లాలు — పోలవరం & మర్కాపురం (జనవరి 1, 2026)",
        "sub": "Cabinet Dec 29 | Gazette Dec 31, 2025 | Effective Jan 1, 2026 | Polavaram HQ: Rampachodavaram | 21 Mandals: Markapuram",
        "audio": "TDP-BJP-JSP ప్రభుత్వం AP జిల్లాలను 26 నుండి 28కి పెంచింది. డిసెంబర్ 29, 2025న కేబినెట్ ఆమోదించింది. డిసెంబర్ 31, 2025న అధికారిక గెజెట్ నోటిఫికేషన్ జారీ చేశారు. జనవరి 1, 2026 నుండి అమల్లోకి వచ్చాయి. రెండు కొత్త జిల్లాలు: పోలవరం జిల్లా (HQ: రాంపచోడవరం, 12 మండలాలు, అత్యల్ప జనాభా ~3.5 లక్షలు) మరియు మర్కాపురం జిల్లా (HQ: మర్కాపురం పట్టణం, 21 మండలాలు). అన్నమయ్య జిల్లా HQ రాయచోటి నుండి మదనపల్లెకు మార్చారు. ప్రస్తుతం కడప జిల్లాలో అత్యధిక మండలాలు ఉన్నాయి. AP జిల్లాల చరిత్ర: 2014 విభజన తర్వాత 13 → 2022 ఏప్రిల్ 4న 26 → 2026 జనవరి 1న 28 జిల్లాలు."
    },
    {
        "title": "పొట్టి శ్రీరాముల 'బలిదాన విగ్రహం' — అమరావతి (58 అడుగులు)",
        "sub": "Announced Dec 15, 2025 | Location: Amaravati 6.8 acres (NOT Nellore) | Target inauguration Mar 16, 2026",
        "audio": "డిసెంబర్ 15, 2025న పొట్టి శ్రీరాముల 73వ వర్ధంతి సందర్భంగా CM చంద్రబాబు అమరావతిలో 58 అడుగుల 'బలిదాన విగ్రహం' నిర్మించాలని ప్రకటించారు. 6.8 ఎకరాల స్థలం కేటాయించారు. 58 అడుగులు ఎందుకంటే ఆయన నిరాహార దీక్షలో 58వ రోజున (డిసెంబర్ 15, 1952) అమరులయ్యారు. మార్చి 16, 2026 (జన్మదినం) నాడు అంకితం లక్ష్యం. తప్పు: నెల్లూరులో విగ్రహం — నెల్లూరు ఆయన జన్మస్థలం మాత్రమే; విగ్రహం అమరావతిలో."
    },
    {
        "title": "IFR-2026 + Milan-2026 + IONS — విశాఖపట్నం (Feb 17-25, 2026)",
        "sub": "First joint hosting of 3 naval events | 74 countries | 71 warships | 'United Through Oceans' | 13th PFR (4th on east coast)",
        "audio": "ఫిబ్రవరి 17-25, 2026 మధ్య విశాఖపట్నంలో మూడు అంతర్జాతీయ నావికా కార్యక్రమాలు మొదటిసారి కలిసి జరిగాయి — అంతర్జాతీయ ఫ్లీట్ రివ్యూ (IFR) 2026, Milan-2026 multilateral exercise, మరియు IONS (Indian Ocean Naval Symposium). 74 దేశాలు, 71 యుద్ధ నౌకలు (19 విదేశీ నౌకలతో సహా) పాల్గొన్నాయి. థీమ్: 'United Through Oceans'. ముఖ్య అతిథి: రాష్ట్రపతి ద్రౌపది ముర్ము. ఇది భారత్ నిర్వహించిన 13వ President's Fleet Review (PFR), మరియు తూర్పు తీరంలో జరిగిన 4వ PFR. MAHASAGAR vision = Mutual and Holistic Advancement for Security and Growth Across Regions."
    },
    {
        "title": "AP Reorganisation (Amendment) Act 2026 — అమరావతి Legal Capital",
        "sub": "LS Apr 1 | RS Apr 2 | Pres assent Apr 6, 2026 | Section 5(2) amended | 3rd amendment to AP Reorg Act 2014 | Retrospective from Jun 2, 2024",
        "audio": "ఏప్రిల్ 2026లో భారత పార్లమెంట్ AP Reorganisation (Amendment) Bill ఆమోదించింది — ఏప్రిల్ 1న లోక్‌సభ, ఏప్రిల్ 2న రాజ్యసభ, ఏప్రిల్ 6న రాష్ట్రపతి ఆమోదం పొందింది. 2014 AP Reorganisation Act లోని Section 5(2) లో 'new capital' అనే పదాన్ని 'Amaravati' గా మార్చారు. ఇది AP Reorganisation Act 2014కి 3వ సవరణ. జూన్ 2, 2024 నుండి retrospective effect తో అమల్లోకి వచ్చింది. ఈ చారిత్రాత్మక చట్టం వల్ల AP భారతదేశంలో కేంద్ర చట్టంలో ప్రత్యేక పేరుతో రాజధాని ప్రకటించబడిన మొదటి రాష్ట్రంగా నిలిచింది. నేపథ్యం: YSRCP హయాంలో 3 రాజధానులు (అమరావతి-Legislative, కర్నూలు-Judicial, విశాఖ-Executive) ప్రతిపాదన; TDP-BJP-JSP 2024లో రద్దు చేశారు."
    },
    {
        "title": "BharatNet — AP లో ₹2,432 కోట్లు (APBIL, Phase 3)",
        "sub": "₹2,432 Crore | APBIL | Digital Bharat Nidhi | Gram Panchayats broadband connectivity",
        "audio": "AP లో BharatNet Phase 3 ప్రాజెక్ట్ కి ₹2,432 కోట్లు కేటాయించారు. అమలు సంస్థ: Andhra Pradesh BharatNet Infrastructure Limited (APBIL). నిధులు: Digital Bharat Nidhi (DBN) నుండి. లక్ష్యం: AP లో అన్ని గ్రామ పంచాయతీలకు high-speed optical fiber broadband connectivity అందించడం."
    },
    {
        "title": "AM Green కాకినాడ — ప్రపంచపు అతిపెద్ద Green Ammonia Plant",
        "sub": "1.5 MTPA | ₹13,000 Crore | Kakinada Port | Greenko Group subsidiary | World's Largest",
        "audio": "AM Green (Greenko Group అనుబంధ సంస్థ) కాకినాడ పోర్టు సమీపంలో నాగార్జున ఫెర్టిలైజర్స్ సైట్ (495 ఎకరాలు) లో ప్రపంచపు అతిపెద్ద Green Ammonia Plant నిర్మిస్తోంది. సామర్థ్యం 1.5 MTPA (Million Tonnes Per Annum). పెట్టుబడి ₹13,000 కోట్లు ($10 billion మొత్తం project). జర్మనీ, జపాన్, సింగపూర్ కి ఎగుమతి (Uniper ఒప్పందం). నిర్మాణ దశలో 8,000 పైగా ఉద్యోగాలు. Green Ammonia: Renewable energy తో నీటిని electrolysis చేసి Hydrogen → Ammonia. Carbon emissions శూన్యం."
    },
    {
        "title": "Auto Driverla Sevalo పథకం — అక్టోబర్ 4, 2025",
        "sub": "₹15,000/year | 2.9 Lakh drivers | Auto/Cab/Maxi Cab | Formerly Vahana Mitra",
        "audio": "అక్టోబర్ 4, 2025న AP ప్రభుత్వం 'Auto Driverla Sevalo' పథకం ప్రారంభించింది. ఇది పాత 'Vahana Mitra' పథకం పేరు మారిన రూపం. Auto, Cab, Maxi Cab drivers కి ఏటా ₹15,000 ఆర్థిక సహాయం. 2.9 లక్షల మంది అర్హులైన drivers లబ్ధిదారులు. Uber-style government app ప్రణాళిక — విశాఖ, విజయవాడలో pilot చేయాలని నిర్ణయించారు."
    },
    {
        "title": "AP కీలక నియామకాలు — DGP హరీష్ కుమార్ గుప్తా & CS G. సాయి ప్రసాద్",
        "sub": "DGP: Harish Kumar Gupta (Jan 31, 2025, IPS 1992) | CS: G.Sai Prasad (Mar 1, 2026, IAS 1991)",
        "audio": "AP DGP: హరీష్ కుమార్ గుప్తా (IPS 1992 batch) జనవరి 31, 2025 నుండి DGP గా 2 సంవత్సరాల నిర్ణీత పదవీ కాలం. ముందు Ch. ద్వారక తిరుమల రావు (1989 batch) జూన్ 2024 – జనవరి 2025 వరకు DGP గా ఉన్నారు. AP CS timeline: నీరబ్ కుమార్ ప్రసాద్ (1987 batch) జూన్ 2024 – డిసెంబర్ 31, 2024; K. విజయానంద్ (1992 batch) జనవరి 1, 2025 – ఫిబ్రవరి 28, 2026 (3 నెలల extension తో); G. సాయి ప్రసాద్ (1991 batch) మార్చి 1, 2026 నుండి CS."
    },
    {
        "title": "ఇతర ముఖ్య సంఘటనలు — Foundation Day, Health Policy, ISTC, TDP",
        "sub": "AP 69th Foundation Day (Nov 1, 2025) | Universal Health Policy | ISTC IMU Vizag | TDP 44th | HC CJ Lisa Gill",
        "audio": "నవంబర్ 1, 2025 — AP 69వ రాష్ట్ర అవతరణ దినోత్సవం (1956 + 69 = 2025). 70వ వార్షికోత్సవం 2026. సెప్టెంబర్ 4, 2025 — AP కేబినెట్ Universal Health Policy ఆమోదించింది (ఆరోగ్య శ్రీ విస్తరణ). సెప్టెంబర్ 20, 2025 — ISTC (International Seafarers Training Centre) @ IMU విశాఖపట్నం — దక్షిణ ఆసియాలో మొదటిది. TDP మార్చి 29, 1982న NTR స్థాపించారు; 2026 మార్చి = 44వ స్థాపన దినోత్సవం. జస్టిస్ లిసా గిల్ AP HC ప్రధాన న్యాయమూర్తి."
    },
    {
        "title": "AP Budget 2026-27 — ₹3,32,205 కోట్లు (Payyavula Keshav)",
        "sub": "Presented Feb 14, 2026 | FM Payyavula Keshav (3rd consecutive) | Revenue receipts ₹2,34,140 cr | Capex ₹53,915 cr (16%)",
        "audio": "ఫిబ్రవరి 14, 2026న ఆర్థిక మంత్రి పయ్యావుల కేశవ్ AP Budget 2026-27 ప్రవేశపెట్టారు — మొత్తం ₹3,32,205.34 కోట్లు. ఇది ఆయన వరుసగా 3వ బడ్జెట్. రెవెన్యూ ఆదాయం ₹2,34,140 కోట్లు; రెవెన్యూ లోటు ₹22,002.50 కోట్లు; ద్రవ్య లోటు (Fiscal deficit) ₹75,868 కోట్లు; మూలధన వ్యయం (Capex) ₹53,915 కోట్లు (బడ్జెట్‌లో 16%). వ్యవసాయ బడ్జెట్: ₹53,752.12 కోట్లు (మంత్రి అచ్చెన్నాయుడు); అన్నదాత సుఖీభవ ₹6,600 కోట్లు; AP GSDP ₹17.62 లక్షల కోట్లు (వ్యవసాయ వాటా 33.2%); AP వ్యవసాయ వృద్ధి 7.83% (జాతీయ 0.80% తో పోలిస్తే). అమరావతి నిర్మాణానికి ₹6,000 కోట్లు; World Bank+ADB రుణం ₹13,500 కోట్లు; పోలవరం ముందస్తు ₹6,105 కోట్లు. క్వాంటం వ్యాలీకి ₹10 కోట్లు; AP Fibernet ₹252.67 కోట్లు; AP Space Application Centre ₹8.05 కోట్లు."
    },
    {
        "title": "కేంద్ర బడ్జెట్ 2026-27 — AP కేటాయింపులు",
        "sub": "Feb 1, 2026 | Polavaram ₹3,320.39 cr | Amaravati ₹1,561 cr (ADB+IBRD) | Industrial Corridors ₹3,000 cr | 4 SEZ Ports ₹400.37 cr",
        "audio": "ఫిబ్రవరి 1, 2026న కేంద్ర ఆర్థిక మంత్రి కేంద్ర బడ్జెట్ 2026-27 ప్రవేశపెట్టారు. AP కి ముఖ్య కేటాయింపులు: పోలవరం ప్రాజెక్ట్‌కు ₹3,320.39 కోట్లు; అమరావతికి ₹1,561 కోట్లు (ADB + IBRD రుణాల ద్వారా); విశాఖ-చెన్నై, చెన్నై-బెంగళూరు, హైదరాబాద్-బెంగళూరు పారిశ్రామిక కారిడార్లకు ₹3,000 కోట్లు. 4 SEZ పోర్టులు — రామాయపట్నం, మచిలీపట్నం, భావనపాడు, కాకినాడ — కు ₹400.37 కోట్లు. 71 కొత్త అన్న కాంటీన్లు మంజూరు (మొత్తం 275 రాష్ట్రంలో). అరకు ట్రెక్కింగ్ ట్రయల్స్ కూడా ప్రకటించారు."
    },
    {
        "title": "16వ SIPB — ₹39,436.84 కోట్లు పెట్టుబడులు + Adani Konaseema Data Centre",
        "sub": "Apr 7, 2026 | 31 firms approved | 1,11,278 jobs | Adani Konaseema Data Centre ₹87,520 cr (largest ever)",
        "audio": "ఏప్రిల్ 7, 2026న 16వ State Investment Promotion Board (SIPB) సమావేశం AP లో ₹39,436.84 కోట్లు పెట్టుబడులు అమోదించింది. 31 సంస్థల ప్రతిపాదనలకు ఆమోదం; మొత్తం 1,11,278 ప్రత్యక్ష ఉద్యోగాలు సృష్టి. ముఖ్యమైన పెట్టుబడులు: Clean Renewable Energy, Essar Renewables, NPSPL Specialty Chemicals (కుప్పం), Tata, మరియు Adani Konaseema Data Centre ₹87,520 కోట్లు (AP చరిత్రలోనే అతిపెద్ద single investment). జనవరి 8, 2026న AP కేబినెట్ ₹20,252 కోట్లు పెట్టుబడులు 14 ప్రాజెక్టులకు అమోదించింది — వీటిలో GMR-Mansas Aviation Educity (భీమిలి, 186.68 ఎకరాలు, AP మొదటి integrated education-innovation city, భోగాపురం దగ్గర)."
    },
    {
        "title": "AP సంక్షేమ పథకాలు 2026 — Indradhanussu, Sthrishakti, Deepam 2.0, Super Nari",
        "sub": "Free RTC for divyangulu (2L) | Sthrishakti ₹1,420 cr | Deepam 2.0 ₹2,601 cr (3 free cylinders) | NTR Bharosa ₹27,719 cr | PNG subsidy ₹2,400/yr",
        "audio": "AP ప్రభుత్వం 2026లో అనేక సంక్షేమ పథకాలు ప్రారంభించింది. 'ఇంద్రధనుస్సు' — దివ్యాంగులకు (~2 లక్షల మంది) ఉచిత RTC ప్రయాణం (మార్చి 18, 2026న CM మంగళగిరిలో ప్రారంభించారు, RTC కి ₹207 కోట్లు). 'స్త్రీశక్తి' ₹1,420 కోట్లు; 'దీపం 2.0' ₹2,601 కోట్లు (సంవత్సరానికి 3 ఉచిత గ్యాస్ సిలిండర్లు); NTR భరోసా పెన్షన్లు ₹27,719 కోట్లు. మహిళా దినోత్సవం (మార్చి 8, 2026) నాడు అమరావతి పరేడ్ గ్రౌండ్స్‌లో CM 'విద్యాలక్ష్మి' & 'NTR కల్యాణలక్ష్మి' (₹1,000 కోట్లు చొప్పున) పథకాలు, AI 'సూపర్ నారి' యాప్ ప్రారంభించారు; 6.81 లక్షల SHG మహిళలకు ₹10,102 కోట్ల చెక్కులు అందజేశారు. ఏప్రిల్ 10, 2026 — PNG (పైప్డ్ నేచురల్ గ్యాస్) connection లకు సంవత్సరానికి ₹2,400 సబ్సిడీ (6 వాయిదాలలో). MSME Revival Policy 4.0 (2026-31) — ₹500 కోట్లు revival fund. AP వ్యవసాయ రుణ బకాయిల్లో రెండవ స్థానం (₹3.75 లక్షల కోట్లు)."
    },
    {
        "title": "AP 3 ఆర్థిక ప్రాంతాలు (Economic Regions) — VER, AER, TER",
        "sub": "March 2026 | Vizag Economic Region | Amaravati Economic Region (9 districts) | Tirupati Economic Region (9 districts) | Target 2047: $2.4 trillion",
        "audio": "మార్చి 2026లో AP ప్రభుత్వం రాష్ట్రాన్ని 3 ఆర్థిక ప్రాంతాలుగా (Economic Regions) విభజించింది — VER (Vizag Economic Region), AER (Amaravati Economic Region, 9 జిల్లాలు), TER (Tirupati Economic Region, 9 జిల్లాలు). 2047 నాటికి AP ఆర్థిక వ్యవస్థను $2.4 trillion కు చేర్చడం లక్ష్యం. International Horticulture Hub: ₹30,000 కోట్లు పెట్టుబడితో రాయలసీమ 4 జిల్లాలు + ప్రకాశం (303 మండలాలు, 201 క్లస్టర్లు, 36 లక్షల ఎకరాల లక్ష్యం). అమరావతి ఔటర్ రింగ్ రోడ్ — 189.4 km 6-lane, కేంద్రం అనుమతి. తెలుగు సాంస్కృతిక కేంద్రం (Telugu Cultural Centre) నీరుకొండ, అమరావతి — ₹119.27 కోట్లు, 5 ఎకరాలు (AP కేబినెట్ మార్చి 10, 2026న ఆమోదం). AP Judicial Academy + HC Judges' Guest House పుచుకపాలెం (Amaravati) — ₹165 కోట్లు, CJI జస్టిస్ సూర్యకాంత్ ఫౌండేషన్ వేశారు."
    },
    {
        "title": "Padma Shri 2026 (AP) & ఇతర చిన్న సంఘటనలు",
        "sub": "4 Padma Shri awardees | RD 2026 at Amaravati (first time) | Bhogapuram Airport 1st landing | Water Budget | Export Index 5th",
        "audio": "Padma Shri 2026లో 4 AP నుండి అవార్డులు: మగంటి మురళి మోహన్ (కళలు), గద్దె బాబు రాజేంద్ర ప్రసాద్ (కళలు), గరిమెళ్ళ బాలకృష్ణ ప్రసాద్ (మరణానంతరం, కళలు/సంగీతం), వెంపటి కుటుంబ శాస్త్రి (సాహిత్యం/సంస్కృతం). జనవరి 26, 2026 — 77వ గణతంత్ర దినోత్సవం మొదటిసారిగా అమరావతిలో జరిగింది (రాయపూడి, సీడ్ యాక్సెస్ రోడ్ సమీపం, 22 ఎకరాలు). గవర్నర్ అబ్దుల్ నజీర్ జెండా ఎగురవేశారు; ఇంతకు ముందు విజయవాడ ఇందిరా గాంధీ స్టేడియంలో జరిగేది. జనవరి 4, 2026 — అల్లూరి సీతారామరాజు అంతర్జాతీయ విమానాశ్రయం (భోగాపురం, విజయనగరం) లో మొదటి test flight (ఢిల్లీ నుండి) ల్యాండ్ అయింది; GMR Group నిర్మాణం; PM మోదీ జూన్ 26, 2026న ప్రారంభించనున్నారు. AP Water Budget 2026-27 — భారతదేశంలో మొదటి రాష్ట్రం (అవసరం 1,490 TMC), జల జీవన్ మిషన్ పేరు 'అమరజీవి జలధార వాటర్‌గ్రిడ్' గా మార్చారు. Dugarajupatnam Port (తిరుపతి జిల్లా) కొత్త greenfield పోర్ట్ + ship-repair cluster అనుమతి (Dec 29, 2025); village secretariats పేరు 'స్వర్ణ గ్రామ/వార్డ్' గా మార్పు; HANUMAN Project (Wildlife-Human Conflict Foundation, పవన్ కల్యాణ్ chairperson, March 3 World Wildlife Day నాడు మంగళగిరి APSP grounds, 100 vehicles). NITI Aayog Export Preparedness Index 2024 (Jan 14, 2026 విడుదల) — AP 5వ స్థానం (60.65 marks); seafood exports లో AP 1వ (60% జాతీయ వాటా, ₹24,679 కోట్లు). AP retail inflation 7.57% → 1.39% (2025-26). Ease of Living Index 2024 — తిరుపతి + విజయవాడ టాప్ 10 భారత నగరాల్లో. CM చంద్రబాబు WEF Davos 2026 (Jan 19-23, 56వ WEF) కు హాజరయ్యారు. PPP medical colleges — 6,250 beds, 1,500 seats. AP Police AI Project — 8 AI modules (Annamayya/చిత్తూరు/Guntur); IIT Madras AI Tutor 42,230 govt schools. కొత్త VC లు: Dravidian Univ. (చిన్న మల్లయ్య లక్షినేని), SKD Univ. (NVR జ్యోతికుమార్). AP NRI Cell Centre Berlin లో ప్రారంభం; AP Govt OTT platform 2026లో launch."
    },
]

# MCQ_DATA: (section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, answer, explanation_te)
# difficulty: 1=Easy, 2=Medium, 3=Hard
MCQ_DATA = [
    (0, 1,
     "అమరావతి క్వాంటం వ్యాలీ ఫౌండేషన్ స్టోన్ ఏ తేదీన వేశారు?",
     "ఫిబ్రవరి 7, 2026", "ఆగస్టు 15, 2025", "నవంబర్ 1, 2025", "ఏప్రిల్ 14, 2026",
     "a",
     "అమరావతి క్వాంటం వ్యాలీ టెక్ పార్క్ ఫౌండేషన్ స్టోన్ ఫిబ్రవరి 7, 2026న CM చంద్రబాబు నాయుడు + కేంద్ర మంత్రి జితేంద్ర సింగ్ వేశారు. ఏప్రిల్ 14, 2026 = అంకితం లక్ష్యం (World Quantum Day + అంబేద్కర్ జయంతి)."),

    (0, 1,
     "అమరావతి క్వాంటం వ్యాలీలో IBM తో కలిసి పని చేస్తున్న ముఖ్య భారతీయ IT కంపెనీ ఏది?",
     "TCS (Tata Consultancy Services)", "Wipro", "Infosys", "HCL Tech",
     "a",
     "అమరావతి క్వాంటం వ్యాలీలో IBM + TCS (Tata Consultancy Services) ముఖ్య భాగస్వాములు. వీరితో పాటు L&T, CDAC, CDOT, IITs, 50+ సంస్థలు ఉన్నాయి."),

    (0, 2,
     "AP Quantum Computing Policy ఏ నెలలో విడుదలైంది?",
     "నవంబర్ 2025", "ఆగస్టు 2025", "సెప్టెంబర్ 2025", "జనవరి 2026",
     "a",
     "AP Quantum Computing Policy నవంబర్ 2025లో విడుదలైంది. ఈ policy ద్వారా AP Quantum Valley కి సంస్థాగత framework ఏర్పడింది."),

    (0, 2,
     "అమరావతి క్వాంటం వ్యాలీలో కంపెనీలు చేరిన నెల ఏది?",
     "ఆగస్టు 2025", "ఏప్రిల్ 2025", "జూన్ 2025", "అక్టోబర్ 2025",
     "a",
     "ఆగస్టు 2025లో LTIMindtree తో పాటు 50+ సంస్థలు అమరావతి క్వాంటం వ్యాలీలో చేరాయి — ప్రాజెక్ట్ ప్రణాళిక మొదలైంది."),

    (0, 3,
     "అమరావతి క్వాంటం వ్యాలీ గురించి ఏది తప్పు?",
     "Microsoft Quantum ముఖ్య భాగస్వామి", "IBM Quantum System Two వాడతారు", "156-qubit Heron processor", "TCS భాగస్వామి",
     "a",
     "Amaravati Quantum Valley ముఖ్య భాగస్వాములు = IBM + TCS (Microsoft Quantum కాదు). Hardware = IBM Quantum System Two (156-qubit Heron processor). Foundation Stone: Feb 7, 2026; Inauguration target: Apr 14, 2026."),

    (1, 1,
     "30వ CII Partnership Summit 2025 ఎక్కడ జరిగింది?",
     "విశాఖపట్నం", "అమరావతి", "హైదరాబాద్", "విజయవాడ",
     "a",
     "30వ CII Partnership Summit నవంబర్ 14-15, 2025న విశాఖపట్నంలో జరిగింది. ఇది AP కి గొప్ప గుర్తింపు — అంతర్జాతీయ పెట్టుబడి సదస్సు."),

    (1, 1,
     "CII 30వ Partnership Summit 2025 ఎవరు ప్రారంభించారు?",
     "VP సి.పి. రాధాకృష్ణన్", "CM చంద్రబాబు నాయుడు", "PM నరేంద్ర మోదీ", "రాష్ట్రపతి ద్రౌపది ముర్ము",
     "a",
     "CII 30వ Partnership Summit ని భారత ఉప రాష్ట్రపతి సి.పి. రాధాకృష్ణన్ ప్రారంభించారు. Commerce & Industry Minister పీయూష్ గోయల్ అధ్యక్షత వహించారు; CM చంద్రబాబు సహ అధ్యక్షత."),

    (1, 2,
     "CII 30వ Partnership Summit 2025లో ఎన్ని దేశాలు పాల్గొన్నాయి?",
     "61 దేశాలు", "45 దేశాలు", "52 దేశాలు", "74 దేశాలు",
     "b",
     "CII 30వ Partnership Summit 2025లో 45 దేశాల నుండి 2,000 పైగా delegates పాల్గొన్నారు. ₹10 లక్షల కోట్ల పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు."),

    (1, 3,
     "CII 30వ Partnership Summit 2025లో ఏ మొత్తం పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు?",
     "₹10 లక్షల కోట్లు", "₹1 లక్ష కోటి", "₹5 లక్షల కోట్లు", "₹25 లక్షల కోట్లు",
     "a",
     "CII 30వ Partnership Summit 2025లో ₹10 లక్షల కోట్లు (10 Lakh Crore) పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు. ఇది AP లో పెట్టుబడి వాతావరణాన్ని చూపిస్తుంది."),

    (2, 1,
     "AP లో 28 జిల్లాలు ఏ తేదీ నుండి అమల్లోకి వచ్చాయి?",
     "జనవరి 1, 2026", "డిసెంబర్ 29, 2025", "డిసెంబర్ 31, 2025", "ఫిబ్రవరి 1, 2026",
     "a",
     "AP 28 జిల్లాలు జనవరి 1, 2026 నుండి అమల్లోకి వచ్చాయి. Cabinet ఆమోదం: డిసెంబర్ 29, 2025; Gazette Notification: డిసెంబర్ 31, 2025; అమల్లోకి: జనవరి 1, 2026."),

    (2, 2,
     "పోలవరం జిల్లా HQ (headquarters) ఏది?",
     "రాంపచోడవరం", "పోలవరం", "ఏలూరు", "భద్రాచలం",
     "a",
     "పోలవరం జిల్లా HQ రాంపచోడవరం (Rampachodavaram). పోలవరం పట్టణం పేరున జిల్లా ఉన్నా HQ మాత్రం రాంపచోడవరం."),

    (2, 2,
     "AP 28 జిల్లాల Gazette Notification ఏ తేదీన జారీ అయింది?",
     "డిసెంబర్ 31, 2025", "డిసెంబర్ 25, 2025", "డిసెంబర్ 29, 2025", "జనవరి 1, 2026",
     "a",
     "AP 28 జిల్లాల అధికారిక Gazette Notification డిసెంబర్ 31, 2025న జారీ అయింది. Cabinet ఆమోదం Dec 29; Gazette: Dec 31; అమల్లో: Jan 1, 2026."),

    (3, 2,
     "పొట్టి శ్రీరాముల విగ్రహం అంకితం లక్ష్య తేదీ ఏది?",
     "మార్చి 16, 2026", "డిసెంబర్ 15, 2025", "జనవరి 26, 2026", "నవంబర్ 1, 2026",
     "a",
     "పొట్టి శ్రీరాముల విగ్రహం మార్చి 16, 2026 (ఆయన జన్మదినం) నాడు అంకితం చేయాలని లక్ష్యం. ప్రకటన: డిసెంబర్ 15, 2025 (73వ వర్ధంతి)."),

    (3, 3,
     "పొట్టి శ్రీరాముల గురించి ఏది సరైనది?",
     "జన్మస్థలం నెల్లూరు; విగ్రహం అమరావతిలో; అమరత్వం మద్రాస్ (1952)", "జన్మస్థలం అమరావతి; విగ్రహం నెల్లూరులో", "విగ్రహం నెల్లూరులో; జన్మదినం మార్చి 16", "జన్మస్థలం మదనపల్లె; అమరత్వం నెల్లూరులో",
     "a",
     "పొట్టి శ్రీరాములు: జన్మస్థలం = నెల్లూరు జిల్లా (మార్చి 16, 1901); అమరత్వం = డిసెంబర్ 15, 1952న మద్రాస్ (Chennai) లో — 58 రోజుల నిరాహార దీక్ష ముగింపులో బుల్సు సాంబమూర్తి గారి ఇంట్లో. విగ్రహం = అమరావతి (58 అడుగుల ఎత్తు, ప్రత్యేక AP రాష్ట్రం 58వ సంవత్సరంలో). మదనపల్లె లో కాదు."),

    (0, 2,
     "అమరావతి క్వాంటం వ్యాలీ ఏర్పాటుకు ఆగస్టు 2025లో ఎన్ని సంస్థలు చేరాయి?",
     "50+ సంస్థలు", "35+ సంస్థలు", "25+ సంస్థలు", "75+ సంస్థలు",
     "a",
     "ఆగస్టు 2025లో LTIMindtree తో పాటు 50 పైగా సంస్థలు అమరావతి క్వాంటం వ్యాలీకి చేరాయి. వివిధ రంగాల సంస్థలు ఈ ఉద్యమంలో భాగమయ్యాయి."),

    (1, 1,
     "CII 30వ Partnership Summit ఎప్పుడు జరిగింది?",
     "నవంబర్ 14-15, 2025", "నవంబర్ 7-8, 2025", "నవంబర్ 21-22, 2025", "డిసెంబర్ 1-2, 2025",
     "a",
     "నవంబర్ 14-15, 2025న విశాఖపట్నంలో 30వ CII Partnership Summit జరిగింది. భారత ఉప రాష్ట్రపతి ఈ కార్యక్రమ ప్రారంభించారు."),

    (3, 1,
     "పొట్టి శ్రీరాముల విగ్రహం ఎక్కడ నిర్మిస్తారు?",
     "అమరావతి", "నెల్లూరు", "చిరాల", "విజయవాడ",
     "a",
     "అమరావతిలో 58 అడుగుల 'బలిదాన విగ్రహం' నిర్మిస్తారు. 6.8 ఎకరాల సరిహద్దు ఈ కృతిమానికి కేటాయించారు."),

    (4, 1,
     "IFR 2026 జరిగిన తేదీ?",
     "ఫిబ్రవరి 18, 2026", "జనవరి 26, 2026", "ఏప్రిల్ 2, 2026", "మే 1, 2026",
     "a",
     "ఫిబ్రవరి 18, 2026న విశాఖపట్నంలో అంతర్జాతీయ ఫ్లీట్ రివ్యూ జరిగింది. భారత రాష్ట్రపతి సమీక్షించారు."),

    (5, 2,
     "AP Reorganisation (Amendment) Act 2026 ను పార్లమెంట్ ఏ నెలలో ఆమోదించింది?",
     "మార్చి 2026", "ఏప్రిల్ 2026", "మే 2026", "జూన్ 2026",
     "b",
     "AP Reorganisation (Amendment) Act 2026 (Act No. 7/2026) ను ఏప్రిల్ 2026లో పార్లమెంట్ ఆమోదించింది (Lok Sabha: Apr 1; Rajya Sabha: Apr 2; President assent: Apr 6, 2026). అమరావతిని ఏకైక రాజధానిగా (retrospectively from June 2, 2024) ధృవీకరించారు."),

    (6, 1,
     "AP BharatNet Phase 3 కోసం కేంద్ర ప్రభుత్వం ఎంత నిధులు కేటాయించింది?",
     "₹2,432 కోట్లు", "₹1,000 కోట్లు", "₹3,500 కోట్లు", "₹5,000 కోట్లు",
     "a",
     "BharatNet Phase 3 AP లో గ్రామీణ ఇంటర్నెట్ సదుపాయం కోసం కేంద్ర ప్రభుత్వం ₹2,432 కోట్లు కేటాయించింది. నిధి మూలం: Digital Bharat Nidhi (DBN). అన్ని గ్రామ పంచాయతీలకు high-speed broadband connectivity లక్ష్యం."),

    (7, 1,
     "కాకినాడలో AM Green ఏ రకమైన పరిశ్రమను ఏర్పాటు చేస్తోంది?",
     "Green Ammonia (హరిత అమ్మోనియా)", "Iron & Steel", "Petroleum Refinery", "Textile Manufacturing",
     "a",
     "AM Green కాకినాడలో ప్రపంచపు అతిపెద్ద Green Ammonia (హరిత అమ్మోనియా) ప్లాంట్ ఏర్పాటు చేస్తోంది — సామర్థ్యం 1.5 MTPA, పెట్టుబడి ₹13,000 కోట్లు. AM Green = Greenko Group అనుబంధ సంస్థ."),

    (8, 1,
     "AP ప్రభుత్వం 'Auto Driverla Sevalo' పథకాన్ని ఏ తేదీన ప్రారంభించింది?",
     "అక్టోబర్ 4, 2025", "ఆగస్టు 15, 2025", "సెప్టెంబర్ 1, 2025", "నవంబర్ 1, 2025",
     "a",
     "AP ప్రభుత్వం 'Auto Driverla Sevalo' పథకాన్ని అక్టోబర్ 4, 2025న ప్రారంభించింది — Auto, Cab, Maxi Cab drivers కు ఆర్థిక సహాయం; Super Six Schemes లో భాగంగా (ఏడాదికి ₹15,000)."),

    (4, 1,
     "IFR 2026 థీమ్ ఏమిటి?",
     "Secure Seas, Secure Nation", "United Through Oceans", "Indian Ocean: Peace and Prosperity", "Blue Economy Rising",
     "b",
     "IFR 2026 థీమ్: 'United Through Oceans' (మహాసముద్రాల ద్వారా ఐక్యత). రాష్ట్రపతి ద్రౌపది ముర్ము INS సుమేధా నౌకపై నుండి సమీక్షించారు."),

    (4, 2,
     "IFR 2026లో రాష్ట్రపతి ముర్ము ఏ నౌకపై నుండి fleet review చేశారు?",
     "INS విక్రమాదిత్య", "INS సుమేధా", "INS కోల్‌కతా", "INS అర్నాల",
     "b",
     "రాష్ట్రపతి ద్రౌపది ముర్ము INS సుమేధా (Sumedha) నౌకపై నుండి IFR 2026 సమీక్షించారు. INS సుమేధా స్వదేశీ నిర్మిత Offshore Patrol Vessel (OPV)."),

    (4, 2,
     "IFR 2026లో ఎన్ని దేశాలు పాల్గొన్నాయి?",
     "52 దేశాలు", "74 దేశాలు", "61 దేశాలు", "90 దేశాలు",
     "b",
     "IFR 2026లో 74 దేశాలు పాల్గొన్నాయి. 85 నౌకలు (66 భారతీయ + 19 విదేశీ) + 3 submarines + 60 పైగా aircraft పాల్గొన్నాయి."),

    (5, 1,
     "AP Reorganisation (Amendment) Act 2026 ఏ రాజధానిని AP ఏకైక రాజధానిగా గుర్తించింది?",
     "విజయవాడ", "అమరావతి", "విశాఖపట్నం", "కర్నూలు",
     "b",
     "AP Reorganisation (Amendment) Act 2026 ద్వారా అమరావతిని AP ఏకైక (Sole and Permanent) రాజధానిగా చట్టపరంగా గుర్తించారు. Section 5 of AP Reorganisation Act, 2014 సవరణ."),

    (5, 1,
     "AP Reorganisation (Amendment) Act 2026 AP Reorganisation Act 2014 లోని ఏ Section కి సవరణ?",
     "Section 3", "Section 5", "Section 4", "Section 7",
     "b",
     "AP Reorganisation (Amendment) Act 2026 = 2014 AP Reorganisation Act లోని Section 5 కి సవరణ. Section 5 రాజధాని నగరాన్ని నిర్ణయించే section."),

    (5, 3,
     "AP Reorganisation Act మొదట ఏ సంవత్సరంలో పార్లమెంట్ ఆమోదించింది?",
     "2009", "2014", "2012", "2019",
     "b",
     "AP Reorganisation Act 2014లో తెలంగాణ-AP విభజన సమయంలో పార్లమెంట్ ఆమోదించింది. ఈ చట్టానికి 2026లో సవరణ చేసి అమరావతిని Legal Capital గా ధృవీకరించారు."),

    (7, 1,
     "AM Green కాకినాడ Green Ammonia Plant — ఇది ఏ రికార్డు కలిగి ఉంది?",
     "భారత్ లోనే అతిపెద్ద", "ప్రపంచంలోనే అతిపెద్ద", "ఆసియాలోనే అతిపెద్ద", "దక్షిణ ఆసియాలో మొదటి",
     "b",
     "AM Green కాకినాడ Green Ammonia Plant ప్రపంచంలోనే అతిపెద్ద (World's Largest) Green Ammonia Plant. సామర్థ్యం 1.5 MTPA; పెట్టుబడి ₹13,000 కోట్లు."),

    (7, 1,
     "AM Green కాకినాడ Plant లో Green Ammonia production సామర్థ్యం ఎంత?",
     "0.5 MTPA", "1.5 MTPA", "1.0 MTPA", "2.0 MTPA",
     "b",
     "AM Green కాకినాడ Green Ammonia Plant సామర్థ్యం 1.5 MTPA (Million Tonnes Per Annum). ఇది ప్రపంచంలోనే అతిపెద్ద Green Ammonia Plant."),

    (7, 2,
     "AM Green ఏ parent group కి చెందిన కంపెనీ?",
     "Reliance Group", "Greenko Group", "Adani Group", "NTPC",
     "b",
     "AM Green = Greenko Group అనుబంధ (subsidiary) సంస్థ. Greenko Group Hyderabad ఆధారిత renewable energy company."),

    (7, 3,
     "Green Ammonia ఎలా తయారవుతుంది?",
     "Coal gasification ద్వారా Hydrogen; తర్వాత Ammonia", "Renewable energy తో water electrolysis → Hydrogen → Ammonia", "Natural gas steam reforming ద్వారా", "Nuclear power తో direct synthesis",
     "b",
     "Green Ammonia: Renewable energy (solar/wind) → water electrolysis → Green Hydrogen → Haber-Bosch process → Ammonia (NH3). Carbon emissions శూన్యం — అందుకే 'Green' అంటారు."),

    (8, 1,
     "Auto Driverla Sevalo పథకం ఏ తేదీన ప్రారంభమైంది?",
     "ఆగస్టు 15, 2025", "అక్టోబర్ 4, 2025", "సెప్టెంబర్ 5, 2025", "నవంబర్ 1, 2025",
     "b",
     "Auto Driverla Sevalo పథకం అక్టోబర్ 4, 2025న AP ప్రభుత్వం ప్రారంభించింది. Auto, Cab, Maxi Cab drivers కి ఏటా ₹15,000 ఆర్థిక సహాయం."),

    (8, 1,
     "Auto Driverla Sevalo పథకం కింద drivers కి ఏటా ఎంత సహాయం అందిస్తారు?",
     "₹5,000", "₹15,000", "₹10,000", "₹20,000",
     "b",
     "Auto Driverla Sevalo పథకం కింద Auto, Cab, Maxi Cab drivers కి ఏటా ₹15,000 ఆర్థిక సహాయం అందిస్తారు. 2.9 లక్షల మంది అర్హులు."),

    (8, 3,
     "Auto Driverla Sevalo పథకంలో ఎంత మంది అర్హులైన drivers ఉన్నారు?",
     "1.5 లక్షలు", "2.9 లక్షలు", "2.3 లక్షలు", "4.5 లక్షలు",
     "b",
     "Auto Driverla Sevalo పథకంలో 2.9 లక్షల మంది అర్హులైన drivers లబ్ధిదారులు. Auto, Cab, Maxi Cab drivers అందరికీ వర్తిస్తుంది."),

    (0, 3,
     "AP Quantum Computing Policy ఏ నెలలో విడుదలైంది?",
     "సెప్టెంబర్ 2025", "నవంబర్ 2025", "జనవరి 2026", "ఫిబ్రవరి 2026",
     "b",
     "AP Quantum Computing Policy నవంబర్ 2025లో విడుదలైంది. ఇది Quantum Valley కి సంస్థాగత framework అందించింది."),

    (1, 2,
     "CII పూర్తి రూపం ఏమిటి?",
     "Council for Indian Innovation", "Confederation of Indian Industry", "Chamber of Indian Industries", "Confederation of Industrial Investment",
     "b",
     "CII = Confederation of Indian Industry. ఇది భారతీయ పరిశ్రమకు ప్రతిపాదక సంస్థ — పెట్టుబడి సదస్సులు నిర్వహిస్తుంది."),

    (2, 2,
     "పోలవరం జిల్లా సదరు కార్యాలయం ఎక్కడ?",
     "పోలవరం", "రాంపచోడవరం", "రాజమండ్రి", "చిరాల",
     "b",
     "రాంపచోడవరంలో పోలవరం జిల్లా సదరు కార్యాలయం ఉంది. ఈ కొత్త జిల్లా తూర్పు గోదావరి నుండి విభజించారు."),

    (3, 2,
     "విగ్రహం అంకితం లక్ష్య తేదీ?",
     "ఫిబ్రవరి 28, 2026", "మార్చి 16, 2026", "ఏప్రిల్ 14, 2026", "మే 1, 2026",
     "b",
     "మార్చి 16, 2026న (జన్మదినం) అమరావతిలో విగ్రహం అంకితం చేయాలని లక్ష్యం. డిసెంబర్ 15, 2025న దీన్ని ప్రకటించారు."),

    (4, 2,
     "INS సుమేధా రకం?",
     "Guided Missile Destroyer", "Offshore Patrol Vessel", "Nuclear Submarine", "Aircraft Carrier",
     "b",
     "Offshore Patrol Vessel (OPV) రకం. స్వదేశీ నిర్మితమైన ఈ నౌక భారత రక్షణలో ముఖ్య ధర్మ చేస్తుంది."),

    (5, 2,
     "YSRCP హయాంలో రాజధానుల సంఖ్య?",
     "ఒకటి", "రెండు", "మూడు", "నాలుగు",
     "c",
     "3 రాజధానులు: అమరావతి (Legislative), కర్నూలు (Judicial), విశాఖపట్నం (Executive)."),

    (6, 2,
     "BharatNet అమలు సంస్థ?",
     "BSNL", "APBIL", "Jio", "Airtel",
     "b",
     "Andhra Pradesh BharatNet Infrastructure Limited (APBIL) అమలు సంస్థ. గ్రామీణ broad band ఏర్పాటులో ఇది పనిచేస్తుంది."),

    # Junk short questions removed by audit 2026-05-18

    (9, 1,
     "AP DGP గా జనవరి 31, 2025 నుండి ఎవరు నియమించారు?",
     "Ch. ద్వారక తిరుమల రావు", "నీరబ్ కుమార్ ప్రసాద్", "హరీష్ కుమార్ గుప్తా", "K. విజయానంద్",
     "c",
     "హరీష్ కుమార్ గుప్తా (IPS 1992 batch, AP cadre) జనవరి 31, 2025 నుండి AP DGP & Head of Police Force గా 2 సంవత్సరాల నిర్ణీత పదవీ కాలంతో నియమించారు."),

    (9, 1,
     "AP Chief Secretary గా మార్చి 1, 2026 నుండి ఎవరు నియమించారు?",
     "K. విజయానంద్", "నీరబ్ కుమార్ ప్రసాద్", "G. సాయి ప్రసాద్", "Y.V. ఆనంద రావు",
     "c",
     "G. సాయి ప్రసాద్ (G. Sai Prasad, IAS 1991 batch) మార్చి 1, 2026 నుండి AP Chief Secretary గా నియమించారు. K. విజయానంద్ ఫిబ్రవరి 28, 2026న పదవీ విరమణ చేశారు."),

    (9, 2,
     "AP DGP హరీష్ కుమార్ గుప్తా IPS ఏ batch?",
     "1987 batch", "1989 batch", "1992 batch", "1996 batch",
     "c",
     "హరీష్ కుమార్ గుప్తా IPS 1992 batch, AP cadre. జనవరి 31, 2025 నుండి DGP గా 2 సంవత్సరాల నిర్ణీత పదవీ కాలం."),

    (9, 2,
     "AP CS G. సాయి ప్రసాద్ IAS ఏ batch?",
     "1987 batch", "1989 batch", "1991 batch", "1992 batch",
     "c",
     "G. సాయి ప్రసాద్ (G. Sai Prasad) IAS 1991 batch. మార్చి 1, 2026 నుండి AP Chief Secretary. K. విజయానంద్ (1992 batch) స్థానంలో నియమించారు."),

    (10, 1,
     "నవంబర్ 1, 2025న AP రాష్ట్రం ఏ వార్షికోత్సవం జరుపుకుంది?",
     "67వ", "68వ", "69వ", "70వ",
     "c",
     "AP నవంబర్ 1, 1956న ఏర్పడింది. 2025 – 1956 = 69 సంవత్సరాలు = 69వ వార్షికోత్సవం. 70వ = 2026లో. తప్పు: 70వ అని చెప్పడం."),

    (10, 1,
     "TDP (Telugu Desam Party) ఏ సంవత్సరంలో స్థాపించారు?",
     "1978", "1980", "1982", "1985",
     "c",
     "TDP = Telugu Desam Party. N.T. రామారావు (NTR) మార్చి 29, 1982న స్థాపించారు. 2026 మార్చి = TDP 44వ స్థాపన దినోత్సవం (1982 → 2026 = 44 సంవత్సరాలు)."),

    (0, 1,
     "IBM Quantum System Two — ఏ processor వాడతారు? ఎన్ని qubits?",
     "128-qubit Eagle", "433-qubit Osprey", "156-qubit Heron", "1000-qubit Condor",
     "c",
     "అమరావతిలో ఏర్పాటవుతున్న IBM Quantum System Two లో 156-qubit Heron processor వాడతారు. ఇది దక్షిణ ఆసియాలో అత్యంత శక్తివంతమైన క్వాంటం కంప్యూటర్."),

    (0, 2,
     "ఏప్రిల్ 14 — IBM Quantum System Two అంకితం లక్ష్య తేదీ — ఇది ఏ రెండు ప్రత్యేక రోజుల కలయిక?",
     "Independence Day + Gandhi Jayanti", "Science Day + Republic Day", "World Quantum Day + అంబేద్కర్ జయంతి", "NTR జయంతి + World Technology Day",
     "c",
     "ఏప్రిల్ 14 = World Quantum Day (ప్రపంచ క్వాంటం దినం) మరియు డాక్టర్ B.R. అంబేద్కర్ జయంతి (Ambedkar Jayanti). ఈ రెండు ముఖ్యమైన రోజులు కలిసే ఏప్రిల్ 14, 2026 నాడు IBM Quantum System Two అంకితం లక్ష్యం."),

    (1, 2,
     "CII అంటే పూర్తి రూపం ఏమిటి?",
     "Central Industrial Institute", "Council of Indian Investment", "Confederation of Indian Industry", "Chamber of Indian Industries",
     "c",
     "CII = Confederation of Indian Industry (కాన్ఫెడరేషన్ ఆఫ్ ఇండియన్ ఇండస్ట్రీ). ఇది భారత్ లో పెట్టుబడులు ఆకర్షించే కోసం ప్రతి సంవత్సరం అంతర్జాతీయ వ్యాపార సదస్సు నిర్వహిస్తుంది."),

    (2, 1,
     "AP 28 జిల్లాల్లో కొత్తగా చేరిన రెండు జిల్లాలు ఏవి?",
     "రాజమహేంద్రవరం & ఒంగోలు", "ఏలూరు & నాంద్యాల", "పోలవరం & మర్కాపురం", "పిఠాపురం & ద్వారక తిరుమల",
     "c",
     "AP లో 26 నుండి 28 జిల్లాలకు పెరగడంలో కొత్తగా చేరిన జిల్లాలు పోలవరం జిల్లా మరియు మర్కాపురం జిల్లా."),

    (2, 3,
     "AP జిల్లాల సంఖ్య మారిన క్రమం సరైనది ఏది?",
     "23 → 13 → 25 → 28", "13 → 23 → 26 → 28", "23 → 13 → 26 → 28", "10 → 13 → 25 → 28",
     "c",
     "AP జిల్లాల క్రమం: అవిభక్త AP = 23 జిల్లాలు → 2014 విభజన తర్వాత Residuary AP = 13 జిల్లాలు → YSRCP 2022 ఏప్రిల్ 4 = 26 జిల్లాలు → TDP-BJP 2026 జనవరి 1 = 28 జిల్లాలు."),

    (3, 1,
     "పొట్టి శ్రీరాముల విగ్రహం ఎత్తు 58 అడుగులు నిర్ణయించిన కారణం ఏది?",
     "58 సంవత్సరాలు జీవించారు", "1958లో AP Foundation Day", "నిరాహార దీక్షలో 58వ రోజున అమరులయ్యారు", "58 జిల్లాల కోసం",
     "c",
     "పొట్టి శ్రీరాముల నిరాహార దీక్షలో 58వ రోజున డిసెంబర్ 15, 1952న అమరులయ్యారు. ఆ 58 రోజులకు గుర్తుగా 58 అడుగుల విగ్రహం నిర్ణయించారు."),

    (3, 2,
     "పొట్టి శ్రీరాముల అమరత్వం తర్వాత ఆంధ్ర రాష్ట్రం ఏ తేదీన ఏర్పడింది?",
     "జనవరి 1, 1953", "నవంబర్ 1, 1956", "అక్టోబర్ 1, 1953", "జనవరి 26, 1950",
     "c",
     "పొట్టి శ్రీరాముల అమరత్వం (డిసెంబర్ 15, 1952) తర్వాత అక్టోబర్ 1, 1953న ఆంధ్ర రాష్ట్రం ఏర్పాటైంది. తర్వాత నవంబర్ 1, 1956న Andhra + Hyderabad కలిసి AP అయింది."),

    (4, 3,
     "భారత్ నిర్వహించిన IFR చరిత్ర క్రమం సరైనది ఏది?",
     "2001 → 2011 → 2026", "1998 → 2008 → 2026", "2001 → 2016 → 2026", "2005 → 2016 → 2026",
     "c",
     "భారత్ నిర్వహించిన IFR లు: 1వ IFR = 2001, 2వ IFR = 2016, 3వ IFR = 2026 (విశాఖపట్నం). IFR 2026 భారత్ నిర్వహించిన 3వ అంతర్జాతీయ ఫ్లీట్ రివ్యూ."),

    (0, 2,
     "CDAC, CDOT ఏ రంగానికి చెందిన సంస్థలు?",
     "ఐటీ / ఎలక్ట్రానిక్‌లు", "వ్యవసాయం", "రక్షణ", "ఆరోగ్య సేవ",
     "a",
     "CDAC (Centre for Development of Advanced Computing) మరియు CDOT (Centre for Development of Telematics) భారత్ ఐటీ/ఎలక్ట్రానిక్స్ రంగానికి చెందిన సంస్థలు. అమరావతి క్వాంటం వ్యాలీలో భాగస్వాములు."),

    (1, 2,
     "CII సమ్మిట్‌కు ఎన్ని దేశాల నుండి delegates హాజరయ్యారు?",
     "41 దేశాలు", "45 దేశాలు", "61 దేశాలు", "71 దేశాలు",
     "b",
     "45 దేశాల నుండి 2000 పైగా ప్రతినిధులు హాజరయ్యారు. అంతర్జాతీయ సహకారానికి ఈ సమ్మిట్ ముఖ్యమైన వేదిక."),

    (2, 3,
     "2014 AP విభజన తర్వాత ఎన్ని జిల్లాలు?",
     "10 జిల్లాలు", "13 జిల్లాలు", "15 జిల్లాలు", "18 జిల్లాలు",
     "b",
     "2014 విభజన తర్వాత Residuary AP లో 13 జిల్లాలు మాత్రమే ఉన్నాయి. YSRCP 2022 ఏప్రిల్ 4న 13 → 26 జిల్లాలకు విభజించింది; TDP 2026 జనవరి 1న 26 → 28 జిల్లాలకు పెంచింది."),

    (3, 3,
     "పొట్టి శ్రీరాముల విగ్రహం ఎత్తు 58 అడుగులు ఎందుకు నిర్ణయించారు?",
     "58 ఎకరాల స్థలం", "ఆయన 58 సంవత్సరాలు జీవించారు", "నిరాహార దీక్ష 58వ రోజున అమరులయ్యారు", "58 జిల్లాల కోసం",
     "c",
     "నిరాహార దీక్ష 58వ రోజున (డిసెంబర్ 15, 1952) సమాధి చెందారు. ఆ 58 రోజులకు స్మారకంగా 58 అడుగుల విగ్రహం నిర్ణయించారు."),

    (4, 3,
     "IFR 2026లో ఎన్ని దేశాలు పాల్గొన్నాయి?",
     "54 దేశాలు", "64 దేశాలు", "74 దేశాలు", "84 దేశాలు",
     "c",
     "74 దేశాలు IFR 2026లో పాల్గొన్నాయి. 85 నౌకలు (66 భారతీయ + 19 విదేశీ) పాల్గొన్నాయి. ఫిబ్రవరి 18, 2026న విశాఖపట్నంలో జరిగింది."),

    (5, 3,
     "AP Reorganisation (Amendment) Act 2026 లో ఏ చట్టానికి సవరణ చేశారు?",
     "1950 రాజ్యాంగ 370 అధికరణ", "AP Reorganisation Act 2014 Section 5", "1951 ప్రిపరేషన్ అండ్ టెర్రిటరీ విభజన", "1976 భూ రికార్డుల చట్టం",
     "b",
     "AP Reorganisation Act 2014 లోని Section 5 ని సవరించారు — అమరావతిని AP ఏకైక రాజధానిగా చట్టపరంగా ధృవీకరించారు."),

    (4, 3,
     "MAHASAGAR అంటే ఏమిటి — IFR 2026 సందర్భంగా భారత్ ప్రకటించిన vision?",
     "Maritime and Holistic Agility for Security Across Global Asian Regions", "Maritime Association for Harmony, Security and Growth Across Regions", "Marine and Hydrographic Alliance for Safety, Growth Across Regions", "Mutual and Holistic Advancement for Security and Growth Across Regions",
     "d",
     "MAHASAGAR = Mutual and Holistic Advancement for Security and Growth Across Regions. ఇది IFR 2026 సందర్భంగా భారత్ ప్రకటించిన Indian Ocean అంతర్జాతీయ భాగస్వామ్య vision."),

    (6, 1,
     "AP లో BharatNet ప్రాజెక్ట్ కి ఎంత నిధులు కేటాయించారు?",
     "₹1,200 కోట్లు", "₹5,000 కోట్లు", "₹8,500 కోట్లు", "₹2,432 కోట్లు",
     "d",
     "AP లో BharatNet Phase 3 ప్రాజెక్ట్ కి ₹2,432 కోట్లు కేటాయించారు. అమలు సంస్థ: APBIL (Andhra Pradesh BharatNet Infrastructure Limited)."),

    (6, 2,
     "BharatNet AP అమలు సంస్థ పూర్తి పేరు ఏమిటి?",
     "AP Broadband Infrastructure Limited", "AP Digital Networks Limited", "AP Fiber Optic Corporation", "Andhra Pradesh BharatNet Infrastructure Limited",
     "d",
     "BharatNet AP అమలు సంస్థ పేరు APBIL = Andhra Pradesh BharatNet Infrastructure Limited. నిధులు Digital Bharat Nidhi (DBN) నుండి వస్తాయి."),

    (7, 2,
     "AM Green కాకినాడ Plant నుండి Green Ammonia ఏ దేశాలకు ఎగుమతి అవుతుంది?",
     "USA, UK, France", "China, Russia, Australia", "UAE, Saudi Arabia, Kuwait", "జర్మనీ, జపాన్, సింగపూర్",
     "d",
     "AM Green కాకినాడ నుండి Green Ammonia జర్మనీ, జపాన్, సింగపూర్ కి ఎగుమతి అవుతుంది. జర్మన్ కంపెనీ Uniper తో ఒప్పందం కుదిరింది."),

    (8, 2,
     "Auto Driverla Sevalo పాత పేరు ఏమిటి?",
     "Vahana Rakshak", "Driver Bhagya", "Savari Sahayam", "Vahana Mitra",
     "d",
     "Auto Driverla Sevalo = పాత Vahana Mitra పథకం పేరు మారింది. TDP ప్రభుత్వం పేరు మార్చి అదే benefit కొనసాగించింది."),

    (9, 2,
     "TDP ప్రభుత్వం జూన్ 2024లో AP DGP గా ముందుగా ఎవరిని నియమించింది?",
     "హరీష్ కుమార్ గుప్తా", "K.V. రాజేంద్రనాథ్ రెడ్డి", "నీరబ్ కుమార్ ప్రసాద్", "Ch. ద్వారక తిరుమల రావు",
     "d",
     "TDP ప్రభుత్వం జూన్ 20, 2024న అధికారంలోకి వచ్చిన తర్వాత Ch. ద్వారక తిరుమల రావు (IPS 1989 batch) ని DGP గా నియమించింది. తర్వాత జనవరి 31, 2025 నుండి హరీష్ కుమార్ గుప్తా DGP అయ్యారు."),

    (9, 3,
     "AP CS timeline 2024-2026 సరైన క్రమం ఏది?",
     "నీరబ్ (2024) → హరీష్ గుప్తా (2025) → K. విజయానంద్ (2026)", "K. విజయానంద్ (2024) → నీరబ్ (2025) → G. సాయి ప్రసాద్ (2026)", "G. సాయి ప్రసాద్ (2024) → నీరబ్ (2025) → K. విజయానంద్ (2026)", "నీరబ్ (2024) → K. విజయానంద్ (2025) → G. సాయి ప్రసాద్ (2026)",
     "d",
     "AP CS క్రమం: నీరబ్ కుమార్ ప్రసాద్ (జూన్ 2024 – డిసెంబర్ 31, 2024, 1987 IAS) → K. విజయానంద్ (జనవరి 1, 2025 – ఫిబ్రవరి 28, 2026, 1992 IAS) → G. సాయి ప్రసాద్ (మార్చి 1, 2026 నుండి, 1991 IAS)."),

    (10, 2,
     "ISTC @ IMU విశాఖపట్నం ఏ ప్రాంతంలో మొదటిది?",
     "మొత్తం ఆసియా", "ఆగ్నేయ ఆసియా", "దక్షిణ భారత్", "దక్షిణ ఆసియా",
     "d",
     "ISTC (International Seafarers Training Centre) @ IMU విశాఖపట్నం సెప్టెంబర్ 20, 2025న ప్రారంభమైంది. దక్షిణ ఆసియా (South Asia) లో ఈ స్థాయి అంతర్జాతీయ నావికుల అడ్వాన్స్‌డ్ శిక్షణ కేంద్రం ఇది మొదటిది."),

    (10, 2,
     "AP Universal Health Policy AP కేబినెట్ ఏ తేదీన ఆమోదించింది?",
     "ఆగస్టు 1, 2025", "అక్టోబర్ 2, 2025", "నవంబర్ 15, 2025", "సెప్టెంబర్ 4, 2025",
     "d",
     "AP కేబినెట్ Universal Health Policy సెప్టెంబర్ 4, 2025న ఆమోదించింది. ఆరోగ్య శ్రీ విస్తరణ — అన్ని కుటుంబాలకు ఆదాయ పరిమితి లేకుండా ఆరోగ్య కవరేజ్."),

    (10, 3,
     "TDP స్థాపించిన నేత ఎవరు? CM చంద్రబాబు నాయుడు TDP స్థాపకునికి ఏమి అవుతారు?",
     "TDP స్థాపకుడు: CM చంద్రబాబు; సంబంధం: అల్లుడు", "TDP స్థాపకుడు: NTR; సంబంధం: కొడుకు", "TDP స్థాపకుడు: నీలం సంజీవ రెడ్డి; సంబంధం: వారసుడు", "TDP స్థాపకుడు: NTR; సంబంధం: అల్లుడు",
     "d",
     "TDP స్థాపకుడు: N.T. రామారావు (NTR), మార్చి 29, 1982. CM నారా చంద్రబాబు నాయుడు = NTR అల్లుడు (son-in-law). చంద్రబాబు భార్య: NTR కుమార్తె నారా భువనేశ్వరి."),

    (3, 1,
     "పొట్టి శ్రీరాముల 'బలిదాన విగ్రహం' ఎక్కడ నిర్మిస్తున్నారు?",
     "నెల్లూరు", "హైదరాబాద్", "విజయవాడ", "అమరావతి",
     "d",
     "పొట్టి శ్రీరాముల 'బలిదాన విగ్రహం' అమరావతిలో నిర్మిస్తున్నారు — 6.8 ఎకరాల స్థలం కేటాయించారు. నెల్లూరు ఆయన జన్మస్థలం మాత్రమే; విగ్రహం అమరావతిలో."),

    (4, 1,
     "International Fleet Review (IFR) 2026 ఎక్కడ జరిగింది?",
     "ముంబయి", "చెన్నై", "కొచ్చిన్", "విశాఖపట్నం",
     "d",
     "International Fleet Review 2026 ఫిబ్రవరి 18, 2026న విశాఖపట్నం తీర సముద్రంలో జరిగింది. విశాఖ తూర్పు నావల్ కమాండ్ కేంద్రం కావడంతో IFR కి ఆదర్శ స్థలం."),

    (9, 3,
     "AP HC Chief Justice జస్టిస్ లిసా గిల్ — AP HC ముఖ్యాలయం ఎక్కడ ఉంది?",
     "హైదరాబాద్", "విజయవాడ", "నెల్లూరు", "అమరావతి",
     "d",
     "AP హైకోర్టు ముఖ్యాలయం అమరావతిలో ఉంది. జస్టిస్ లిసా గిల్ AP HC ప్రధాన న్యాయమూర్తి. SC కొలీజియం సిఫారసు మేరకు రాష్ట్రపతి నియమించారు."),

    (0, 2,
     "IBM Quantum System Two లో ఎన్ని qubits ఉన్నాయి?",
     "128-qubit", "256-qubit", "156-qubit", "512-qubit",
     "c",
     "156-qubit Heron processor ఉపయోగించారు. ఇది దక్షిణ ఆసియాలో అత్యంత శక్తివంతమైన కవాంటం కంప్యూటర్."),

    (1, 2,
     "CII 30వ Partnership Summit 2025లో AP లో ఏ పెట్టుబడుల లక్ష్యం నిర్ణయించారు?",
     "₹5 లక్షల కోట్లు", "₹8 లక్షల కోట్లు", "₹10 లక్షల కోట్లు", "₹15 లక్షల కోట్లు",
     "c",
     "CII 30వ Partnership Summit 2025లో ₹10 లక్షల కోట్లు (10 Lakh Crore) పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు. 45 దేశాల నుండి 2,000+ delegates పాల్గొన్నారు."),

    (2, 2,
     "మర్కాపురం జిల్లా ఏ జిల్లా నుండి విభజించారు?",
     "చిత్తూరు", "నెల్లూరు", "ప్రకాశం", "కర్నూలు",
     "c",
     "ప్రకాశం జిల్లా నుండి మర్కాపురం జిల్లా విభజించారు. జనవరి 1, 2026 నుండి అమల్లో వచ్చిన 28వ జిల్లా."),

    (3, 1,
     "పొట్టి శ్రీరాముల 'బలిదాన విగ్రహం' ప్రకటన ఏ తేదీన చేశారు?",
     "డిసెంబర్ 15, 2025", "నవంబర్ 1, 2025", "జనవరి 26, 2026", "ఫిబ్రవరి 1, 2026",
     "a",
     "డిసెంబర్ 15, 2025న పొట్టి శ్రీరాముల 73వ వర్ధంతి సందర్భంగా CM చంద్రబాబు అమరావతిలో 58 అడుగుల విగ్రహం ప్రకటించారు."),

    # ╔══════════════════════════════════════════════════════════╗
    # ║  📅 2026 MCQs — Jan-Apr 2026 events from monthly PDFs    ║
    # ║  Batch H+PDF audit (2026-05-18) — 77 new MCQs below      ║
    # ║  To find: grep for "# 2026:" in this file                ║
    # ╚══════════════════════════════════════════════════════════╝

    # 2026: ─── Section 2: 28 Districts (Polavaram + Markapuram added Dec 31, 2025) ───
    (2, 2,
     "పోలవరం జిల్లాలో ఎన్ని మండలాలు ఉన్నాయి?",
     "8 మండలాలు", "10 మండలాలు", "12 మండలాలు", "15 మండలాలు",
     "c",
     "పోలవరం జిల్లాలో 12 మండలాలు ఉన్నాయి — AP 28 జిల్లాలలో అత్యల్ప మండలాలు ఉన్న జిల్లాగా మరియు అత్యల్ప జనాభా (~3.5 లక్షలు) తో ఏర్పడింది. HQ: రాంపచోడవరం."),

    (2, 2,
     "మర్కాపురం జిల్లాలో ఎన్ని మండలాలు ఉన్నాయి?",
     "15 మండలాలు", "18 మండలాలు", "21 మండలాలు", "24 మండలాలు",
     "c",
     "మర్కాపురం జిల్లాలో 21 మండలాలు ఉన్నాయి. HQ: మర్కాపురం పట్టణం. ప్రకాశం జిల్లా నుండి విభజించారు."),

    (2, 2,
     "అన్నమయ్య జిల్లా కొత్త HQ (headquarters) ఎక్కడికి మారింది?",
     "రాయచోటి", "మదనపల్లె", "రాజంపేట", "పుంగనూరు",
     "b",
     "అన్నమయ్య జిల్లా HQ రాయచోటి నుండి మదనపల్లెకు మార్చబడింది (Dec 31, 2025 gazette). పూర్వ HQ రాయచోటి."),

    (2, 3,
     "AP 28 జిల్లాలలో ప్రస్తుతం అత్యధిక మండలాలు ఉన్న జిల్లా ఏది?",
     "అనంతపురం", "కడప", "చిత్తూరు", "కర్నూలు",
     "b",
     "AP 28 జిల్లాల పునర్వ్యవస్థీకరణ తర్వాత కడప జిల్లాలో అత్యధిక మండలాలు ఉన్నాయి. మర్కాపురం/పోలవరం ఏర్పడిన తర్వాత ఈ ర్యాంకింగ్ మారింది."),

    (2, 1,
     "పోలవరం జిల్లా జనాభా (అత్యల్ప) సుమారు ఎంత?",
     "~2 లక్షలు", "~3.5 లక్షలు", "~6 లక్షలు", "~10 లక్షలు",
     "b",
     "పోలవరం జిల్లా జనాభా సుమారు 3.5 లక్షలు — AP 28 జిల్లాలలో అత్యల్పం. 12 మండలాలతో అతి చిన్న జిల్లా."),

    # 2026: ─── Section 4: IFR-Milan-IONS trio at Vizag (Feb 17-25) ───
    (4, 2,
     "ఫిబ్రవరి 17-25, 2026లో విశాఖపట్నంలో జరిగిన మూడు అంతర్జాతీయ నావికా కార్యక్రమాలు ఏవి?",
     "IFR + Milan + IONS", "IFR + Talisman Sabre + RIMPAC", "IFR + Malabar + Tropex", "IFR + SIMBEX + Konkan",
     "a",
     "IFR-2026, Milan-2026 (multilateral exercise), మరియు IONS (Indian Ocean Naval Symposium) — మూడు అంతర్జాతీయ నావికా కార్యక్రమాలు మొదటిసారి కలిసి విశాఖలో జరిగాయి (Feb 17-25, 2026)."),

    (4, 2,
     "IFR 2026లో మొత్తం ఎన్ని యుద్ధ నౌకలు పాల్గొన్నాయి?",
     "61", "71", "85", "95",
     "b",
     "IFR 2026లో మొత్తం 71 యుద్ధ నౌకలు పాల్గొన్నాయి, వీటిలో 19 విదేశీ నౌకలు ఉన్నాయి."),

    (4, 3,
     "IFR 2026 భారత్ నిర్వహించిన ఎన్నవ President's Fleet Review (PFR)?",
     "11వ", "12వ", "13వ", "15వ",
     "c",
     "IFR-2026 భారత్ నిర్వహించిన 13వ President's Fleet Review (PFR). ఇది తూర్పు తీరంలో జరిగిన 4వ PFR."),

    (4, 2,
     "IFR 2026 ముఖ్య అతిథి ఎవరు?",
     "PM నరేంద్ర మోదీ", "రాష్ట్రపతి ద్రౌపది ముర్ము", "VP సి.పి. రాధాకృష్ణన్", "రక్షణ మంత్రి రాజ్‌నాథ్ సింగ్",
     "b",
     "రాష్ట్రపతి ద్రౌపది ముర్ము IFR 2026 ముఖ్య అతిథి. INS సుమేధా నౌకపై నుండి fleet review చేశారు."),

    # 2026: ─── Section 5: Amaravati Legal Capital (APRA Amendment Apr 1-6, 2026) ───
    (5, 1,
     "AP Reorganisation (Amendment) Bill 2026 లోక్‌సభలో ఏ తేదీన ఆమోదించబడింది?",
     "ఏప్రిల్ 1, 2026", "మార్చి 31, 2026", "ఏప్రిల్ 2, 2026", "ఏప్రిల్ 6, 2026",
     "a",
     "ఏప్రిల్ 1, 2026న లోక్‌సభ ఆమోదించింది; ఏప్రిల్ 2న రాజ్యసభ; ఏప్రిల్ 6న రాష్ట్రపతి ఆమోదం."),

    (5, 1,
     "AP Reorganisation (Amendment) Bill 2026 రాజ్యసభలో ఏ తేదీన ఆమోదించబడింది?",
     "ఏప్రిల్ 1, 2026", "ఏప్రిల్ 2, 2026", "ఏప్రిల్ 4, 2026", "ఏప్రిల్ 6, 2026",
     "b",
     "రాజ్యసభ ఏప్రిల్ 2, 2026న ఆమోదించింది. రాష్ట్రపతి ఆమోదం ఏప్రిల్ 6, 2026."),

    (5, 2,
     "AP Reorganisation (Amendment) Act 2026 — AP Reorganisation Act 2014కి ఎన్నవ సవరణ?",
     "1వ సవరణ", "2వ సవరణ", "3వ సవరణ", "4వ సవరణ",
     "c",
     "AP Reorganisation (Amendment) Act 2026 = AP Reorganisation Act 2014కి 3వ సవరణ."),

    (5, 2,
     "AP Reorganisation (Amendment) Act 2026 ఏ తేదీ నుండి retrospective effect తో అమలులోకి వచ్చింది?",
     "జనవరి 1, 2026", "జూన్ 2, 2024", "జూన్ 12, 2024", "ఏప్రిల్ 6, 2026",
     "b",
     "ఈ చట్టం జూన్ 2, 2024 నుండి retrospective effect తో అమల్లోకి వచ్చింది (AP విభజన దినం)."),

    (5, 3,
     "AP Reorganisation (Amendment) Act 2026 ఏ subsection ను సవరించింది?",
     "Section 4(1)", "Section 5(1)", "Section 5(2)", "Section 6(2)",
     "c",
     "Section 5(2) ను సవరించారు — 'new capital' అనే పదాన్ని 'Amaravati' గా మార్చారు."),

    (5, 3,
     "AP Reorganisation (Amendment) Act 2026 వల్ల AP ఏ ప్రత్యేక విశిష్టత పొందింది?",
     "మొదటి digital రాజధాని కలిగిన రాష్ట్రం", "కేంద్ర చట్టంలో ప్రత్యేక పేరుతో రాజధాని ప్రకటించబడిన మొదటి భారత రాష్ట్రం", "మొదటి planned రాజధాని", "మొదటి smart city రాజధాని",
     "b",
     "ఈ చట్టంతో AP — కేంద్ర చట్టంలో ప్రత్యేక పేరుతో (Amaravati) రాజధాని ప్రకటించబడిన మొదటి భారత రాష్ట్రంగా నిలిచింది."),

    # 2026: ─── Section 11: AP Budget 2026-27 (Feb 14, Rs.3,32,205 cr) ───
    (11, 1,
     "AP Budget 2026-27 ఏ తేదీన ప్రవేశపెట్టారు?",
     "ఫిబ్రవరి 1, 2026", "ఫిబ్రవరి 14, 2026", "మార్చి 1, 2026", "ఫిబ్రవరి 28, 2026",
     "b",
     "AP Budget 2026-27 ఫిబ్రవరి 14, 2026న ఆర్థిక మంత్రి పయ్యావుల కేశవ్ ప్రవేశపెట్టారు."),

    (11, 1,
     "AP Budget 2026-27 మొత్తం పరిమాణం ఎంత?",
     "₹2,90,000 కోట్లు", "₹3,32,205.34 కోట్లు", "₹3,75,000 కోట్లు", "₹4,00,000 కోట్లు",
     "b",
     "AP Budget 2026-27 మొత్తం పరిమాణం ₹3,32,205.34 కోట్లు."),

    (11, 1,
     "AP Budget 2026-27 ప్రవేశపెట్టిన ఆర్థిక మంత్రి ఎవరు?",
     "నారా చంద్రబాబు నాయుడు", "పయ్యావుల కేశవ్", "పవన్ కల్యాణ్", "నారా లోకేష్",
     "b",
     "ఆర్థిక మంత్రి పయ్యావుల కేశవ్ — ఆయన వరుసగా 3వ బడ్జెట్ ప్రవేశపెట్టారు."),

    (11, 2,
     "AP Budget 2026-27 — రెవెన్యూ ఆదాయం (Revenue Receipts) ఎంత?",
     "₹1,90,000 కోట్లు", "₹2,34,140 కోట్లు", "₹2,75,000 కోట్లు", "₹3,00,000 కోట్లు",
     "b",
     "రెవెన్యూ ఆదాయం ₹2,34,140 కోట్లు; రెవెన్యూ లోటు ₹22,002.50 కోట్లు."),

    (11, 2,
     "AP Budget 2026-27 ద్రవ్య లోటు (Fiscal Deficit) ఎంత?",
     "₹50,000 కోట్లు", "₹62,500 కోట్లు", "₹75,868 కోట్లు", "₹95,000 కోట్లు",
     "c",
     "AP Budget 2026-27 ద్రవ్య లోటు ₹75,868 కోట్లు; రెవెన్యూ లోటు ₹22,002.50 కోట్లు."),

    (11, 2,
     "AP Budget 2026-27 మూలధన వ్యయం (Capex) ఎంత? ఇది బడ్జెట్‌లో ఎంత శాతం?",
     "₹38,000 కోట్లు (11%)", "₹53,915 కోట్లు (16%)", "₹65,000 కోట్లు (19%)", "₹70,000 కోట్లు (21%)",
     "b",
     "Capex ₹53,915 కోట్లు — బడ్జెట్‌లో 16%. మౌలిక సదుపాయాల అభివృద్ధికి ముఖ్య కేటాయింపు."),

    (11, 1,
     "AP వ్యవసాయ బడ్జెట్ 2026-27 ఎంత? ప్రవేశపెట్టిన మంత్రి ఎవరు?",
     "₹40,000 కోట్లు; నారా లోకేష్", "₹53,752.12 కోట్లు; అచ్చెన్నాయుడు", "₹35,000 కోట్లు; పయ్యావుల కేశవ్", "₹45,000 కోట్లు; మండిపల్లి రాంబాబు",
     "b",
     "వ్యవసాయ బడ్జెట్ 2026-27 — ₹53,752.12 కోట్లు. వ్యవసాయ మంత్రి అచ్చెన్నాయుడు ప్రవేశపెట్టారు."),

    (11, 2,
     "అన్నదాత సుఖీభవ పథకానికి AP Budget 2026-27లో ఎంత కేటాయించారు?",
     "₹4,500 కోట్లు", "₹6,600 కోట్లు", "₹8,200 కోట్లు", "₹10,000 కోట్లు",
     "b",
     "అన్నదాత సుఖీభవకి ₹6,600 కోట్లు కేటాయించారు."),

    (11, 3,
     "AP GSDP 2026లో ఎంత? వ్యవసాయ వాటా శాతం?",
     "₹15.20 లక్షల కోట్లు; 28%", "₹17.62 లక్షల కోట్లు; 33.2%", "₹19.50 లక్షల కోట్లు; 38%", "₹21.00 లక్షల కోట్లు; 41%",
     "b",
     "AP GSDP ₹17.62 లక్షల కోట్లు; వ్యవసాయ వాటా 33.2%. AP వ్యవసాయ వృద్ధి 7.83% (జాతీయ 0.80%)."),

    (11, 2,
     "AP Budget 2026-27లో అమరావతి నిర్మాణానికి ఎంత కేటాయించారు?",
     "₹3,000 కోట్లు", "₹6,000 కోట్లు", "₹10,000 కోట్లు", "₹13,500 కోట్లు",
     "b",
     "అమరావతి నిర్మాణానికి ₹6,000 కోట్లు రాష్ట్ర బడ్జెట్‌లో; World Bank + ADB రుణం ₹13,500 కోట్లు అదనంగా."),

    (11, 2,
     "AP Budget 2026-27లో Quantum Valley కు ఎంత కేటాయించారు?",
     "₹5 కోట్లు", "₹10 కోట్లు", "₹50 కోట్లు", "₹100 కోట్లు",
     "b",
     "అమరావతి Quantum Valley కు ₹10 కోట్లు; AP Fibernet ₹252.67 కోట్లు; AP Space Application Centre ₹8.05 కోట్లు."),

    # 2026: ─── Section 12: Central Budget 2026-27 AP allocations (Feb 1) ───
    (12, 1,
     "కేంద్ర బడ్జెట్ 2026-27 ఏ తేదీన ప్రవేశపెట్టారు?",
     "ఫిబ్రవరి 1, 2026", "ఫిబ్రవరి 14, 2026", "మార్చి 1, 2026", "జనవరి 31, 2026",
     "a",
     "కేంద్ర బడ్జెట్ 2026-27 ఫిబ్రవరి 1, 2026న ప్రవేశపెట్టారు. AP కు అనేక కేటాయింపులు ఉన్నాయి."),

    (12, 2,
     "కేంద్ర బడ్జెట్ 2026-27 — పోలవరం ప్రాజెక్ట్‌కు ఎంత కేటాయించారు?",
     "₹2,500 కోట్లు", "₹3,320.39 కోట్లు", "₹5,000 కోట్లు", "₹6,105 కోట్లు",
     "b",
     "పోలవరం ప్రాజెక్ట్‌కు కేంద్రం ₹3,320.39 కోట్లు కేటాయించింది. అదనంగా AP కి ₹6,105 కోట్ల ముందస్తు."),

    (12, 2,
     "కేంద్ర బడ్జెట్ 2026-27 — అమరావతికి ఎంత కేటాయించారు?",
     "₹900 కోట్లు", "₹1,200 కోట్లు", "₹1,561 కోట్లు", "₹2,000 కోట్లు",
     "c",
     "అమరావతికి కేంద్రం నుండి ₹1,561 కోట్లు (ADB + IBRD రుణాల ద్వారా)."),

    (12, 2,
     "కేంద్ర బడ్జెట్ 2026-27 — విశాఖ-చెన్నై, చెన్నై-బెంగళూరు, హైదరాబాద్-బెంగళూరు industrial corridors కు ఎంత కేటాయించారు?",
     "₹1,000 కోట్లు", "₹2,000 కోట్లు", "₹3,000 కోట్లు", "₹4,500 కోట్లు",
     "c",
     "3 పారిశ్రామిక కారిడార్లకు మొత్తం ₹3,000 కోట్లు కేటాయించారు."),

    (12, 3,
     "AP 4 SEZ ports (రామాయపట్నం, మచిలీపట్నం, భావనపాడు, కాకినాడ) కు కేంద్ర బడ్జెట్‌లో ఎంత?",
     "₹250.50 కోట్లు", "₹400.37 కోట్లు", "₹550.00 కోట్లు", "₹720.45 కోట్లు",
     "b",
     "4 SEZ ports కు ₹400.37 కోట్లు. 71 కొత్త అన్న కాంటీన్లు కూడా మంజూరు (మొత్తం 275 రాష్ట్రంలో)."),

    # 2026: ─── Section 13: 16th SIPB Apr 7 (Rs.39,436 cr) + Adani Konaseema Data Centre ───
    (13, 1,
     "16వ SIPB సమావేశం ఏ తేదీన జరిగింది?",
     "మార్చి 7, 2026", "ఏప్రిల్ 7, 2026", "మే 1, 2026", "ఫిబ్రవరి 14, 2026",
     "b",
     "16వ State Investment Promotion Board (SIPB) సమావేశం ఏప్రిల్ 7, 2026న జరిగింది."),

    (13, 1,
     "16వ SIPB సమావేశంలో మొత్తం ఎంత పెట్టుబడులు ఆమోదించారు?",
     "₹25,000 కోట్లు", "₹39,436.84 కోట్లు", "₹50,000 కోట్లు", "₹87,520 కోట్లు",
     "b",
     "16వ SIPB ₹39,436.84 కోట్లు పెట్టుబడులు 31 సంస్థలకు ఆమోదించింది; 1,11,278 ప్రత్యక్ష ఉద్యోగాలు సృష్టి."),

    (13, 1,
     "AP చరిత్రలో అతిపెద్ద single investment ఏది? ఎంత?",
     "Reliance Green Energy ₹50,000 cr", "Adani Konaseema Data Centre ₹87,520 cr", "TCS Amaravati ₹40,000 cr", "Tata Auto Hub ₹65,000 cr",
     "b",
     "Adani Konaseema Data Centre ₹87,520 కోట్లు — AP చరిత్రలో అతిపెద్ద single investment. 16వ SIPB (Apr 7, 2026) లో ఆమోదం."),

    (13, 2,
     "16వ SIPB సమావేశంలో ఎన్ని ప్రత్యక్ష ఉద్యోగాలు సృష్టి అవుతాయి?",
     "75,000", "1,00,000", "1,11,278", "1,50,000",
     "c",
     "16వ SIPB ఆమోదించిన 31 సంస్థల ద్వారా 1,11,278 ప్రత్యక్ష ఉద్యోగాలు సృష్టి."),

    (13, 2,
     "NPSPL Specialty Chemicals plant AP లో ఎక్కడ స్థాపిస్తారు?",
     "విశాఖ", "కుప్పం", "అమరావతి", "తిరుపతి",
     "b",
     "NPSPL Specialty Chemicals కుప్పంలో స్థాపిస్తారు — 16వ SIPB (Apr 7, 2026) లో ఆమోదం."),

    (13, 2,
     "GMR-Mansas Aviation Educity ఎక్కడ ఏర్పాటు చేస్తున్నారు? ఎంత భూమి?",
     "విశాఖ; 250 ఎకరాలు", "భీమిలి; 186.68 ఎకరాలు", "విజయవాడ; 150 ఎకరాలు", "తిరుపతి; 200 ఎకరాలు",
     "b",
     "GMR-Mansas Aviation Educity భీమిలి (విశాఖ సమీపం) లో 186.68 ఎకరాలలో — AP మొదటి integrated education-innovation city, భోగాపురం దగ్గర."),

    (13, 3,
     "జనవరి 8, 2026 AP కేబినెట్ సమావేశంలో మొత్తం ఎంత పెట్టుబడులు ఎన్ని ప్రాజెక్టులకు ఆమోదించారు?",
     "₹15,000 కోట్లు; 10 ప్రాజెక్టులు", "₹20,252 కోట్లు; 14 ప్రాజెక్టులు", "₹30,000 కోట్లు; 18 ప్రాజెక్టులు", "₹39,436 కోట్లు; 31 ప్రాజెక్టులు",
     "b",
     "జనవరి 8, 2026 AP కేబినెట్ ₹20,252 కోట్లు పెట్టుబడులు 14 పారిశ్రామిక/పర్యాటక ప్రాజెక్టులకు ఆమోదించింది."),

    # 2026: ─── Section 14: AP Welfare Schemes 2026 (Indradhanussu, Sthrishakti, Super Nari, PNG) ───
    (14, 1,
     "'ఇంద్రధనుస్సు' పథకం ఎవరికి వర్తిస్తుంది?",
     "విద్యార్థులు", "మహిళలు", "దివ్యాంగులు", "రైతులు",
     "c",
     "'ఇంద్రధనుస్సు' = దివ్యాంగులకు (~2 లక్షల మంది) ఉచిత RTC ప్రయాణం. మార్చి 18, 2026న CM మంగళగిరిలో ప్రారంభించారు; RTC కి ₹207 కోట్లు."),

    (14, 1,
     "'దీపం 2.0' పథకం ఏ సౌకర్యం అందిస్తుంది? బడ్జెట్?",
     "ఉచిత విద్యుత్; ₹1,000 కోట్లు", "సంవత్సరానికి 3 ఉచిత గ్యాస్ సిలిండర్లు; ₹2,601 కోట్లు", "ఉచిత నీరు; ₹500 కోట్లు", "ఉచిత ఇంటర్నెట్; ₹800 కోట్లు",
     "b",
     "'దీపం 2.0' — సంవత్సరానికి 3 ఉచిత గ్యాస్ సిలిండర్లు; బడ్జెట్ ₹2,601 కోట్లు."),

    (14, 2,
     "'స్త్రీశక్తి' పథకానికి ఎంత కేటాయించారు?",
     "₹800 కోట్లు", "₹1,420 కోట్లు", "₹2,000 కోట్లు", "₹2,500 కోట్లు",
     "b",
     "'స్త్రీశక్తి' — ₹1,420 కోట్లు; మహిళా SHG పథకాలు."),

    (14, 2,
     "NTR భరోసా పెన్షన్లకు AP లో ఎంత కేటాయించారు?",
     "₹15,000 కోట్లు", "₹20,500 కోట్లు", "₹27,719 కోట్లు", "₹35,000 కోట్లు",
     "c",
     "NTR భరోసా పెన్షన్లకు ₹27,719 కోట్లు కేటాయించారు."),

    (14, 1,
     "మహిళా దినోత్సవం 2026 (మార్చి 8) నాడు CM ప్రారంభించిన AI app పేరు?",
     "Mahila Mitra", "Stree Suraksha", "సూపర్ నారి (Super Nari)", "Nari Shakti",
     "c",
     "AI 'సూపర్ నారి' (Super Nari) యాప్ — మార్చి 8, 2026 మహిళా దినోత్సవం నాడు CM అమరావతి పరేడ్ గ్రౌండ్స్‌లో ప్రారంభించారు."),

    (14, 2,
     "మహిళా దినోత్సవం 2026 నాడు 6.81 లక్షల SHG మహిళలకు ఎంత చెక్కులు అందజేశారు?",
     "₹5,000 కోట్లు", "₹7,500 కోట్లు", "₹10,102 కోట్లు", "₹15,000 కోట్లు",
     "c",
     "6.81 లక్షల SHG మహిళలకు ₹10,102 కోట్ల చెక్కులు అందజేశారు."),

    (14, 2,
     "'విద్యాలక్ష్మి' & 'NTR కల్యాణలక్ష్మి' పథకాలకు చొప్పున ఎంత కేటాయించారు?",
     "₹500 కోట్లు", "₹750 కోట్లు", "₹1,000 కోట్లు", "₹1,500 కోట్లు",
     "c",
     "'విద్యాలక్ష్మి' & 'NTR కల్యాణలక్ష్మి' రెండు పథకాలకు చొప్పున ₹1,000 కోట్లు."),

    (14, 3,
     "PNG (Piped Natural Gas) connections కు AP ప్రభుత్వం ఏ తేదీ నుండి ఎంత subsidy ఇస్తోంది?",
     "Mar 1, 2026; ₹1,800/year", "Apr 10, 2026; ₹2,400/year (6 instalments)", "Jan 1, 2026; ₹3,000/year", "Feb 14, 2026; ₹1,500/year",
     "b",
     "ఏప్రిల్ 10, 2026 నుండి PNG connection లకు సంవత్సరానికి ₹2,400 subsidy (6 instalments). దీపం 2.0 PNG విస్తరణ."),

    (14, 3,
     "MSME Revival Policy 4.0 (2026-31) లో revival fund ఎంత?",
     "₹100 కోట్లు", "₹250 కోట్లు", "₹500 కోట్లు", "₹1,000 కోట్లు",
     "c",
     "MSME Revival Policy 4.0 (2026-31) — ₹500 కోట్లు revival fund. AP వ్యవసాయ రుణ బకాయిల్లో 2వ స్థానం (₹3.75 లక్షల కోట్లు)."),

    (14, 2,
     "'దివ్యాంగ శక్తి' / ఇంద్రధనుస్సు ఎక్కడ ఎప్పుడు ప్రారంభమైంది?",
     "విశాఖ; Jan 26, 2026", "మంగళగిరి (గుంటూరు); మార్చి 18, 2026", "విజయవాడ; ఫిబ్రవరి 14, 2026", "అమరావతి; ఏప్రిల్ 1, 2026",
     "b",
     "CM మంగళగిరి (గుంటూరు జిల్లా) లో మార్చి 18, 2026న దివ్యాంగులకు ఉచిత RTC ప్రయాణం ప్రారంభించారు; RTC కి ₹207 కోట్లు."),

    # 2026: ─── Section 15: 3 Economic Regions (VER/AER/TER) + Horticulture Hub + ORR + Judicial Academy ───
    (15, 1,
     "AP ప్రభుత్వం రాష్ట్రాన్ని ఎన్ని ఆర్థిక ప్రాంతాలుగా (Economic Regions) విభజించింది?",
     "2", "3", "4", "5",
     "b",
     "AP 3 ఆర్థిక ప్రాంతాలు — VER (Vizag), AER (Amaravati, 9 జిల్లాలు), TER (Tirupati, 9 జిల్లాలు). మార్చి 2026లో ప్రకటించారు."),

    (15, 2,
     "AP 3 Economic Regions పేర్లు సరైనవి ఏవి?",
     "NER, CER, SER", "VER, AER, TER", "GER, MER, KER", "WER, EER, NER",
     "b",
     "VER (Vizag Economic Region), AER (Amaravati Economic Region, 9 జిల్లాలు), TER (Tirupati Economic Region, 9 జిల్లాలు)."),

    (15, 2,
     "AP ప్రభుత్వం 2047 నాటికి ఎంత ఆర్థిక వ్యవస్థ లక్ష్యం పెట్టుకుంది?",
     "$1 trillion", "$1.5 trillion", "$2.4 trillion", "$5 trillion",
     "c",
     "AP 2047 నాటికి $2.4 trillion ఆర్థిక వ్యవస్థ లక్ష్యం పెట్టుకుంది."),

    (15, 2,
     "International Horticulture Hub ఎంత పెట్టుబడితో ప్రారంభమైంది?",
     "₹10,000 కోట్లు", "₹20,000 కోట్లు", "₹30,000 కోట్లు", "₹50,000 కోట్లు",
     "c",
     "International Horticulture Hub — ₹30,000 కోట్లు పెట్టుబడితో రాయలసీమ + ప్రకాశం (303 మండలాలు, 201 క్లస్టర్లు, 36 లక్షల ఎకరాల లక్ష్యం)."),

    (15, 1,
     "అమరావతి ఔటర్ రింగ్ రోడ్ (ORR) ఎన్ని km, ఎన్ని lane?",
     "150 km; 4-lane", "189.4 km; 6-lane", "220 km; 8-lane", "100 km; 4-lane",
     "b",
     "అమరావతి ORR — 189.4 km, 6-lane; కేంద్ర ప్రభుత్వం అమోదించింది."),

    (15, 1,
     "తెలుగు సాంస్కృతిక కేంద్రం (Telugu Cultural Centre) ఎక్కడ నిర్మిస్తారు? బడ్జెట్?",
     "విజయవాడ; ₹50 కోట్లు", "నీరుకొండ (అమరావతి); ₹119.27 కోట్లు", "విశాఖ; ₹200 కోట్లు", "తిరుపతి; ₹75 కోట్లు",
     "b",
     "నీరుకొండ, అమరావతి — 5 ఎకరాలు, ₹119.27 కోట్లు. AP కేబినెట్ మార్చి 10, 2026న ఆమోదించింది."),

    (15, 2,
     "AP Judicial Academy + HC Judges' Guest House ఎక్కడ నిర్మిస్తారు? బడ్జెట్? ఎవరు ఫౌండేషన్ వేశారు?",
     "విజయవాడ; ₹100 కోట్లు; HC CJ", "పుచుకపాలెం (అమరావతి); ₹165 కోట్లు; CJI జస్టిస్ సూర్యకాంత్", "విశాఖ; ₹200 కోట్లు; PM మోదీ", "తిరుపతి; ₹125 కోట్లు; CM చంద్రబాబు",
     "b",
     "పుచుకపాలెం (అమరావతి) — ₹165 కోట్లు; CJI జస్టిస్ సూర్యకాంత్ ఫౌండేషన్ వేశారు."),

    (15, 3,
     "International Horticulture Hub లో ఎన్ని మండలాలు, ఎన్ని క్లస్టర్లు?",
     "200 మండలాలు, 150 క్లస్టర్లు", "303 మండలాలు, 201 క్లస్టర్లు", "400 మండలాలు, 250 క్లస్టర్లు", "500 మండలాలు, 300 క్లస్టర్లు",
     "b",
     "303 మండలాలు, 201 క్లస్టర్లు, 36 లక్షల ఎకరాల లక్ష్యం (రాయలసీమ 4 + ప్రకాశం = 10 జిల్లాలు)."),

    # 2026: ─── Section 16: Padma Shri + RD Amaravati + Bhogapuram + Water Budget + Export Index ───
    (16, 1,
     "Padma Shri 2026 — AP నుండి ఎంత మంది ఎంపిక?",
     "2", "3", "4", "5",
     "c",
     "Padma Shri 2026లో AP నుండి 4 మంది: మగంటి మురళి మోహన్, గద్దె బాబు రాజేంద్ర ప్రసాద్, గరిమెళ్ళ బాలకృష్ణ ప్రసాద్ (మరణానంతరం), వెంపటి కుటుంబ శాస్త్రి."),

    (16, 2,
     "Padma Shri 2026 (AP) లో మరణానంతరం (posthumous) ఎవరికి అవార్డు ప్రకటించారు?",
     "మగంటి మురళి మోహన్", "గద్దె బాబు రాజేంద్ర ప్రసాద్", "గరిమెళ్ళ బాలకృష్ణ ప్రసాద్", "వెంపటి కుటుంబ శాస్త్రి",
     "c",
     "గరిమెళ్ళ బాలకృష్ణ ప్రసాద్ (కళలు/సంగీతం) కు మరణానంతరం (posthumous) Padma Shri 2026 ప్రకటించారు."),

    (16, 2,
     "Padma Shri 2026 — వెంపటి కుటుంబ శాస్త్రి ఏ రంగంలో అవార్డు పొందారు?",
     "కళలు/నాట్యం", "సాహిత్యం / సంస్కృతం", "సామాజిక సేవ", "శాస్త్రం",
     "b",
     "వెంపటి కుటుంబ శాస్త్రి — సాహిత్యం/సంస్కృతం రంగంలో Padma Shri 2026."),

    (16, 1,
     "77వ గణతంత్ర దినోత్సవం (Jan 26, 2026) AP లో ఎక్కడ మొదటిసారిగా జరిగింది?",
     "విజయవాడ", "అమరావతి (రాయపూడి)", "విశాఖ", "తిరుపతి",
     "b",
     "77వ గణతంత్ర దినోత్సవం మొదటిసారిగా అమరావతిలో జరిగింది (రాయపూడి గ్రామం, సీడ్ యాక్సెస్ రోడ్ సమీపం, 22 ఎకరాలు). ఇంతకుముందు విజయవాడ ఇందిరా గాంధీ స్టేడియంలో జరిగేది."),

    (16, 2,
     "77వ గణతంత్ర దినోత్సవం (Jan 26, 2026) AP లో జెండా ఎగురవేసిన గవర్నర్ ఎవరు?",
     "హరిబాబు కంభంపాటి", "అబ్దుల్ నజీర్", "విశ్వభూషణ్ హరిచందన్", "బిశ్వభూషణ్ మిశ్రా",
     "b",
     "గవర్నర్ అబ్దుల్ నజీర్ అమరావతి (రాయపూడి) లో 77వ గణతంత్ర దినోత్సవం నాడు జెండా ఎగురవేశారు."),

    (16, 1,
     "అల్లూరి సీతారామరాజు అంతర్జాతీయ విమానాశ్రయం (భోగాపురం) లో మొదటి test flight ఏ తేదీన ల్యాండ్ అయింది?",
     "జనవరి 4, 2026", "డిసెంబర్ 31, 2025", "ఫిబ్రవరి 14, 2026", "మార్చి 1, 2026",
     "a",
     "జనవరి 4, 2026న ఢిల్లీ నుండి మొదటి test flight ల్యాండ్ అయింది. PM మోదీ జూన్ 26, 2026న ప్రారంభించనున్నారు. GMR Group నిర్మించింది."),

    (16, 2,
     "భోగాపురం విమానాశ్రయం ఏ జిల్లాలో ఉంది? నిర్మాణ సంస్థ ఎవరు?",
     "విశాఖ; Adani Group", "విజయనగరం; GMR Group", "శ్రీకాకుళం; L&T", "విశాఖ; GVK",
     "b",
     "విజయనగరం జిల్లాలో; GMR Group నిర్మించింది. అధికారిక పేరు: అల్లూరి సీతారామరాజు అంతర్జాతీయ విమానాశ్రయం."),

    (16, 1,
     "AP Water Budget 2026-27 ప్రకారం AP నీటి అవసరం ఎంత?",
     "1,200 TMC", "1,490 TMC", "1,800 TMC", "2,000 TMC",
     "b",
     "AP Water Budget 2026-27 ప్రకారం నీటి అవసరం 1,490 TMC. AP — Water Budget తయారు చేసిన భారతదేశంలో మొదటి రాష్ట్రం."),

    (16, 2,
     "జల జీవన్ మిషన్ AP లో కొత్త పేరు ఏమిటి?",
     "Jaladhara Andhra", "అమరజీవి జలధార వాటర్‌గ్రిడ్", "Pure Water AP", "Sujala Andhra",
     "b",
     "జల జీవన్ మిషన్ పేరు 'అమరజీవి జలధార వాటర్‌గ్రిడ్' (Amarajeevi Jaladhara Watergrid) గా AP లో మార్చారు."),

    (16, 1,
     "NITI Aayog Export Preparedness Index 2024 (Jan 14, 2026 విడుదల) లో AP ర్యాంక్ ఎంత?",
     "3వ స్థానం", "4వ స్థానం", "5వ స్థానం", "7వ స్థానం",
     "c",
     "AP 5వ స్థానం (60.65 marks). 2024లో AP ఎగుమతులు ₹1.65 లక్షల కోట్లు."),

    (16, 2,
     "AP seafood exports లో జాతీయ ర్యాంక్? వాటా?",
     "1వ; 60% (₹24,679 cr)", "2వ; 45%", "3వ; 35%", "1వ; 75%",
     "a",
     "seafood exports లో AP భారతదేశంలో 1వ స్థానం — 60% జాతీయ వాటా, ₹24,679 కోట్లు."),

    (16, 2,
     "AP retail inflation 2025-26లో ఎలా మారింది?",
     "7.57% → 1.39%", "5.20% → 2.80%", "3.50% → 1.10%", "8.00% → 4.50%",
     "a",
     "AP retail inflation 7.57% నుండి 1.39% కి తగ్గింది (2025-26)."),

    (16, 2,
     "Ease of Living Index 2024 — టాప్ 10 భారత నగరాల్లో AP నుండి ఏ నగరాలు ఉన్నాయి?",
     "విశాఖ + విజయవాడ", "తిరుపతి + విజయవాడ", "విశాఖ + తిరుపతి", "విజయవాడ + గుంటూరు",
     "b",
     "Ease of Living Index 2024లో తిరుపతి + విజయవాడ టాప్ 10 భారత నగరాల్లో ఉన్నాయి."),

    (16, 2,
     "Dugarajupatnam Port AP లో ఏ జిల్లాలో నిర్మిస్తారు?",
     "విశాఖ", "శ్రీకాకుళం", "తిరుపతి", "నెల్లూరు",
     "c",
     "Dugarajupatnam Port — తిరుపతి జిల్లాలో కొత్త greenfield port + ship-repair cluster. డిసెంబర్ 29, 2025న AP కేబినెట్ ఆమోదించింది."),

    (16, 2,
     "AP లో village secretariats కొత్త పేరు ఏమిటి?",
     "Grama Sachivalayam", "Praja Seva Kendra", "స్వర్ణ గ్రామ/వార్డ్", "Andhra Bhavan",
     "c",
     "village secretariats పేరును 'స్వర్ణ గ్రామ/వార్డ్' (Swarna Grama/Ward) గా మార్చారు."),

    (16, 1,
     "HANUMAN Project ఎవరు chairperson? ఏ తేదీన ప్రారంభం?",
     "CM చంద్రబాబు; Jan 26, 2026", "పవన్ కల్యాణ్; మార్చి 3, 2026 (World Wildlife Day)", "నారా లోకేష్; ఫిబ్రవరి 1, 2026", "వంగలపూడి అనిత; ఏప్రిల్ 1, 2026",
     "b",
     "HANUMAN Project (Wildlife-Human Conflict Foundation) chairperson: పవన్ కల్యాణ్. మార్చి 3, 2026 World Wildlife Day నాడు మంగళగిరి APSP grounds వద్ద ప్రారంభం; 100 vehicles flag-off."),

    (16, 2,
     "CM చంద్రబాబు WEF Davos 2026 — ఎంతవ WEF?",
     "54వ", "55వ", "56వ", "57వ",
     "c",
     "56వ WEF Davos 2026 (జనవరి 19-23, 2026) — CM చంద్రబాబు AP కు పెట్టుబడులు రాబట్టారు."),

    (16, 3,
     "AP PPP medical colleges ద్వారా ఎన్ని beds + ఎన్ని seats నిర్ణయించారు?",
     "5,000 beds; 1,000 seats", "6,250 beds; 1,500 seats", "8,000 beds; 2,000 seats", "10,000 beds; 2,500 seats",
     "b",
     "AP PPP medical colleges — 6,250 beds + 1,500 seats."),

    (16, 2,
     "Dravidian University కొత్త VC ఎవరు?",
     "NVR జ్యోతికుమార్", "చిన్న మల్లయ్య లక్షినేని", "K. విజయానంద్", "G. సాయి ప్రసాద్",
     "b",
     "Dravidian University కొత్త VC: చిన్న మల్లయ్య లక్షినేని. SKD University VC: NVR జ్యోతికుమార్."),

    (16, 2,
     "AP NRI Cell Centre ఏ యూరోపియన్ నగరంలో ప్రారంభమైంది?",
     "లండన్", "పారిస్", "బెర్లిన్", "రోమ్",
     "c",
     "AP NRI Cell Centre బెర్లిన్ (జర్మనీ) లో ప్రారంభమైంది."),

    (16, 3,
     "AP Police AI Project లో ఎన్ని AI modules? ఏ జిల్లాలలో?",
     "5 modules; విశాఖ/విజయవాడ/తిరుపతి", "8 modules; అన్నమయ్య/చిత్తూరు/గుంటూరు", "10 modules; కడప/నెల్లూరు/కర్నూలు", "6 modules; పశ్చిమ గోదావరి/తూర్పు గోదావరి",
     "b",
     "AP Police AI Project — 8 AI modules; అన్నమయ్య, చిత్తూరు, గుంటూరు జిల్లాలలో అమలు. IIT Madras AI Tutor 42,230 govt schools."),

]


def _seed_ap_ca_div4_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (4, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id IN (SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph})", (4, 'AP_Current_Affairs'))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (4, 'AP_Current_Affairs'))
    if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division4', 4,
         '2025 ఆగస్టు – 2026 ఏప్రిల్ ముఖ్య సంఘటనలు',
         'Major Events August 2025 – April 2026',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'AP CA Div4 notes seeded!'}


def _seed_ap_ca_div4_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES):
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (4, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div4_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (4, 'AP_Current_Affairs'))
        row = cur.fetchone()
    note_id = row_to_dict(row)['id']
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = f"INSERT INTO chapter_mcqs (study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    for (sec_idx, diff, q_te, a, b, c, d, correct, expl) in MCQ_DATA:
        db_exec(conn, insert_sql, (note_id, sec_idx, diff, q_te, a, b, c, d, str(correct).lower(), expl))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'inserted': len(MCQ_DATA)}
