"""
seed_ap_ca_div4.py — AP Current Affairs Division 4: 2025 August – 2026 April
ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ — విభాగం 4: 2025 ఆగస్టు – 2026 ఏప్రిల్ ముఖ్య సంఘటనలు

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
        "audio": "AP ప్రభుత్వం అమరావతిలో క్వాంటం వ్యాలీ ఏర్పాటు చేసింది. ఆగస్టు 2025లో LTIMindtree తో పాటు 50 పైగా సంస్థలు చేరాయి. నవంబర్ 2025లో AP Quantum Computing Policy విడుదలైంది. ఫిబ్రవరి 7, 2026న CM చంద్రబాబు నాయుడు + కేంద్ర మంత్రి జితేంద్ర సింగ్ ఫౌండేషన్ స్టోన్ వేశారు. IBM Quantum System Two — 156-qubit Heron processor — IBM మరియు TCS (Tata Consultancy Services) సహా L&T, CDAC, IITs పాల్గొంటున్నాయి. ఏప్రిల్ 14, 2026 (World Quantum Day + అంబేద్కర్ జయంతి) నాడు అంకితం లక్ష్యం. తప్పు: Qubit Force నిర్మించింది అని చెప్పడం; నిజం: IBM + TCS."
    },
    {
        "title": "CII 30వ పార్టనర్‌షిప్ సమ్మిట్ — విశాఖపట్నం, నవంబర్ 14-15, 2025",
        "sub": "30th CII Partnership Summit | 61 Countries | ₹10 Lakh Crore investment target | VP inaugurated",
        "audio": "నవంబర్ 14-15, 2025న విశాఖపట్నంలో 30వ CII Partnership Summit జరిగింది. CII అంటే Confederation of Indian Industry. భారత ఉప రాష్ట్రపతి సి.పి. రాధాకృష్ణన్ ప్రారంభించారు. కేంద్ర మంత్రి పీయూష్ గోయల్ అధ్యక్షత; CM చంద్రబాబు సహ అధ్యక్షత. 61 దేశాల నుండి 2000 పైగా delegates పాల్గొన్నారు. ₹10 లక్షల కోట్ల పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు."
    },
    {
        "title": "AP 28 జిల్లాలు — పోలవరం & మర్కాపురం (జనవరి 1, 2026)",
        "sub": "Cabinet Dec 29 | Gazette Dec 31, 2025 | Effective Jan 1, 2026 | Polavaram HQ: Rampachodavaram",
        "audio": "TDP-BJP-JSP ప్రభుత్వం AP జిల్లాలను 26 నుండి 28 కి పెంచింది. డిసెంబర్ 29, 2025న కేబినెట్ ఆమోదించింది. డిసెంబర్ 31, 2025న అధికారిక గెజెట్ నోటిఫికేషన్ జారీ చేశారు. జనవరి 1, 2026 నుండి అమల్లోకి వచ్చాయి. రెండు కొత్త జిల్లాలు: పోలవరం జిల్లా (HQ: రాంపచోడవరం) మరియు మర్కాపురం జిల్లా. AP జిల్లాల చరిత్ర: 2014 విభజన తర్వాత 13 జిల్లాలు; 2022 ఏప్రిల్ 4న 26 జిల్లాలు; 2026 జనవరి 1 నుండి 28 జిల్లాలు."
    },
    {
        "title": "పొట్టి శ్రీరాముల 'బలిదాన విగ్రహం' — అమరావతి (58 అడుగులు)",
        "sub": "Announced Dec 15, 2025 | Location: Amaravati 6.8 acres (NOT Nellore) | Target inauguration Mar 16, 2026",
        "audio": "డిసెంబర్ 15, 2025న పొట్టి శ్రీరాముల 73వ వర్ధంతి సందర్భంగా CM చంద్రబాబు అమరావతిలో 58 అడుగుల 'బలిదాన విగ్రహం' నిర్మించాలని ప్రకటించారు. 6.8 ఎకరాల స్థలం కేటాయించారు. 58 అడుగులు ఎందుకంటే ఆయన నిరాహార దీక్షలో 58వ రోజున (డిసెంబర్ 15, 1952) అమరులయ్యారు. మార్చి 16, 2026 (జన్మదినం) నాడు అంకితం లక్ష్యం. తప్పు: నెల్లూరులో విగ్రహం — నెల్లూరు ఆయన జన్మస్థలం మాత్రమే; విగ్రహం అమరావతిలో."
    },
    {
        "title": "అంతర్జాతీయ ఫ్లీట్ రివ్యూ (IFR) 2026 — విశాఖపట్నం",
        "sub": "Feb 18, 2026 | 74 Countries | 85 Ships | 'United Through Oceans' | INS Sumedha | India's 3rd IFR",
        "audio": "ఫిబ్రవరి 18, 2026న విశాఖపట్నంలో అంతర్జాతీయ ఫ్లీట్ రివ్యూ (IFR) 2026 జరిగింది. రాష్ట్రపతి ద్రౌపది ముర్ము INS సుమేధా (స్వదేశీ Offshore Patrol Vessel) నౌకపై నుండి సమీక్షించారు. 74 దేశాలు పాల్గొన్నాయి. 85 నౌకలు (66 భారతీయ + 19 విదేశీ) + 3 submarines + 60 పైగా aircraft. థీమ్: United Through Oceans. MAHASAGAR vision: Mutual and Holistic Advancement for Security and Growth Across Regions. ఇది భారత్ నిర్వహించిన 3వ IFR (1వ: 2001, 2వ: 2016)."
    },
    {
        "title": "AP Reorganisation (Amendment) Act 2026 — అమరావతి ఏకైక రాజధాని",
        "sub": "Section 5 amended | Amaravati = Sole Capital | April 2026 Parliament | YSRCP 3-capital dispute resolved",
        "audio": "ఏప్రిల్ 2026న భారత పార్లమెంట్ AP Reorganisation (Amendment) Act 2026 ఆమోదించింది. 2014 AP Reorganisation Act లోని Section 5 కి సవరణ. అమరావతిని AP ఏకైక రాజధాని (Sole and Permanent Capital) గా చట్టపరంగా ధృవీకరించారు. నేపథ్యం: YSRCP హయాంలో 3 రాజధానులు ప్రతిపాదించారు — అమరావతి (Legislative), కర్నూలు (Judicial), విశాఖపట్నం (Executive). TDP-BJP 2024లో అధికారంలోకి వచ్చిన తర్వాత అమరావతిని ఏకైక రాజధానిగా నిర్ణయించారు."
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
]

# MCQ_DATA: (section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, answer, explanation_te)
# difficulty: 1=Easy, 2=Medium, 3=Hard
MCQ_DATA = [

    # ==================== Section 0: Quantum Valley ====================

    (0, 1,
     "అమరావతి క్వాంటం వ్యాలీ ఫౌండేషన్ స్టోన్ ఏ తేదీన వేశారు?",
     "ఆగస్టు 15, 2025", "నవంబర్ 1, 2025", "ఫిబ్రవరి 7, 2026", "ఏప్రిల్ 14, 2026",
     "c",
     "అమరావతి క్వాంటం వ్యాలీ టెక్ పార్క్ ఫౌండేషన్ స్టోన్ ఫిబ్రవరి 7, 2026న CM చంద్రబాబు నాయుడు + కేంద్ర మంత్రి జితేంద్ర సింగ్ వేశారు. ఏప్రిల్ 14, 2026 = అంకితం లక్ష్యం (World Quantum Day + అంబేద్కర్ జయంతి)."),

    (0, 1,
     "IBM Quantum System Two — ఏ processor వాడతారు? ఎన్ని qubits?",
     "128-qubit Eagle", "156-qubit Heron", "433-qubit Osprey", "1000-qubit Condor",
     "b",
     "అమరావతిలో ఏర్పాటవుతున్న IBM Quantum System Two లో 156-qubit Heron processor వాడతారు. ఇది దక్షిణ ఆసియాలో అత్యంత శక్తివంతమైన క్వాంటం కంప్యూటర్."),

    (0, 1,
     "అమరావతి క్వాంటం వ్యాలీలో IBM తో కలిసి పని చేస్తున్న ముఖ్య భారతీయ IT కంపెనీ ఏది?",
     "Wipro", "Infosys", "TCS (Tata Consultancy Services)", "HCL Tech",
     "c",
     "అమరావతి క్వాంటం వ్యాలీలో IBM + TCS (Tata Consultancy Services) ముఖ్య భాగస్వాములు. వీరితో పాటు L&T, CDAC, CDOT, IITs, 50+ సంస్థలు ఉన్నాయి."),

    (0, 2,
     "ఏప్రిల్ 14 — IBM Quantum System Two అంకితం లక్ష్య తేదీ — ఇది ఏ రెండు ప్రత్యేక రోజుల కలయిక?",
     "Independence Day + Gandhi Jayanti", "World Quantum Day + అంబేద్కర్ జయంతి", "Science Day + Republic Day", "NTR జయంతి + World Technology Day",
     "b",
     "ఏప్రిల్ 14 = World Quantum Day (ప్రపంచ క్వాంటం దినం) మరియు డాక్టర్ B.R. అంబేద్కర్ జయంతి (Ambedkar Jayanti). ఈ రెండు ముఖ్యమైన రోజులు కలిసే ఏప్రిల్ 14, 2026 నాడు IBM Quantum System Two అంకితం లక్ష్యం."),

    (0, 2,
     "AP Quantum Computing Policy ఏ నెలలో విడుదలైంది?",
     "ఆగస్టు 2025", "సెప్టెంబర్ 2025", "నవంబర్ 2025", "జనవరి 2026",
     "c",
     "AP Quantum Computing Policy నవంబర్ 2025లో విడుదలైంది. ఈ policy ద్వారా AP Quantum Valley కి సంస్థాగత framework ఏర్పడింది."),

    (0, 2,
     "అమరావతి క్వాంటం వ్యాలీలో కంపెనీలు చేరిన నెల ఏది?",
     "ఏప్రిల్ 2025", "జూన్ 2025", "ఆగస్టు 2025", "అక్టోబర్ 2025",
     "c",
     "ఆగస్టు 2025లో LTIMindtree తో పాటు 50+ సంస్థలు అమరావతి క్వాంటం వ్యాలీలో చేరాయి — ప్రాజెక్ట్ ప్రణాళిక మొదలైంది."),

    (0, 3,
     "అమరావతి క్వాంటం వ్యాలీ గురించి ఏది తప్పు?",
     "IBM Quantum System Two వాడతారు", "156-qubit Heron processor", "Qubit Force ముఖ్య నిర్మాత", "TCS భాగస్వామి",
     "c",
     "Qubit Force ఒక చిన్న hardware testbed మాత్రమే — ముఖ్య నిర్మాత కాదు. ముఖ్య భాగస్వాములు IBM + TCS. Foundation Stone: Feb 7, 2026 (ఆగస్టు 2025 కాదు)."),

    # ==================== Section 1: CII 30th Partnership Summit ====================

    (1, 1,
     "30వ CII Partnership Summit 2025 ఎక్కడ జరిగింది?",
     "అమరావతి", "హైదరాబాద్", "విశాఖపట్నం", "విజయవాడ",
     "c",
     "30వ CII Partnership Summit నవంబర్ 14-15, 2025న విశాఖపట్నంలో జరిగింది. ఇది AP కి గొప్ప గుర్తింపు — అంతర్జాతీయ పెట్టుబడి సదస్సు."),

    (1, 1,
     "CII 30వ Partnership Summit 2025 ఎవరు ప్రారంభించారు?",
     "CM చంద్రబాబు నాయుడు", "PM నరేంద్ర మోదీ", "VP సి.పి. రాధాకృష్ణన్", "రాష్ట్రపతి ద్రౌపది ముర్ము",
     "c",
     "CII 30వ Partnership Summit ని భారత ఉప రాష్ట్రపతి సి.పి. రాధాకృష్ణన్ ప్రారంభించారు. Commerce & Industry Minister పీయూష్ గోయల్ అధ్యక్షత వహించారు; CM చంద్రబాబు సహ అధ్యక్షత."),

    (1, 2,
     "CII 30వ Partnership Summit 2025లో ఎన్ని దేశాలు పాల్గొన్నాయి?",
     "45 దేశాలు", "52 దేశాలు", "61 దేశాలు", "74 దేశాలు",
     "c",
     "CII 30వ Partnership Summit 2025లో 61 దేశాల నుండి 2,000 పైగా delegates పాల్గొన్నారు. ₹10 లక్షల కోట్ల పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు."),

    (1, 2,
     "CII అంటే పూర్తి రూపం ఏమిటి?",
     "Central Industrial Institute", "Confederation of Indian Industry", "Council of Indian Investment", "Chamber of Indian Industries",
     "b",
     "CII = Confederation of Indian Industry (కాన్ఫెడరేషన్ ఆఫ్ ఇండియన్ ఇండస్ట్రీ). ఇది భారత్ లో పెట్టుబడులు ఆకర్షించే కోసం ప్రతి సంవత్సరం అంతర్జాతీయ వ్యాపార సదస్సు నిర్వహిస్తుంది."),

    (1, 3,
     "CII 30వ Partnership Summit 2025లో ఏ మొత్తం పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు?",
     "₹1 లక్ష కోటి", "₹5 లక్షల కోట్లు", "₹10 లక్షల కోట్లు", "₹25 లక్షల కోట్లు",
     "c",
     "CII 30వ Partnership Summit 2025లో ₹10 లక్షల కోట్లు (10 Lakh Crore) పెట్టుబడులు ఆకర్షించే లక్ష్యం నిర్ణయించారు. ఇది AP లో పెట్టుబడి వాతావరణాన్ని చూపిస్తుంది."),

    # ==================== Section 2: 28 Districts ====================

    (2, 1,
     "AP లో 28 జిల్లాలు ఏ తేదీ నుండి అమల్లోకి వచ్చాయి?",
     "డిసెంబర్ 29, 2025", "డిసెంబర్ 31, 2025", "జనవరి 1, 2026", "ఫిబ్రవరి 1, 2026",
     "c",
     "AP 28 జిల్లాలు జనవరి 1, 2026 నుండి అమల్లోకి వచ్చాయి. Cabinet ఆమోదం: డిసెంబర్ 29, 2025; Gazette Notification: డిసెంబర్ 31, 2025; అమల్లోకి: జనవరి 1, 2026."),

    (2, 1,
     "AP 28 జిల్లాల్లో కొత్తగా చేరిన రెండు జిల్లాలు ఏవి?",
     "రాజమహేంద్రవరం & ఒంగోలు", "పోలవరం & మర్కాపురం", "ఏలూరు & నాంద్యాల", "పిఠాపురం & ద్వారక తిరుమల",
     "b",
     "AP లో 26 నుండి 28 జిల్లాలకు పెరగడంలో కొత్తగా చేరిన జిల్లాలు పోలవరం జిల్లా మరియు మర్కాపురం జిల్లా."),

    (2, 2,
     "పోలవరం జిల్లా HQ (headquarters) ఏది?",
     "పోలవరం", "ఏలూరు", "రాంపచోడవరం", "భద్రాచలం",
     "c",
     "పోలవరం జిల్లా HQ రాంపచోడవరం (Rampachodavaram). పోలవరం పట్టణం పేరున జిల్లా ఉన్నా HQ మాత్రం రాంపచోడవరం."),

    (2, 2,
     "AP 28 జిల్లాల Gazette Notification ఏ తేదీన జారీ అయింది?",
     "డిసెంబర్ 25, 2025", "డిసెంబర్ 29, 2025", "డిసెంబర్ 31, 2025", "జనవరి 1, 2026",
     "c",
     "AP 28 జిల్లాల అధికారిక Gazette Notification డిసెంబర్ 31, 2025న జారీ అయింది. Cabinet ఆమోదం Dec 29; Gazette: Dec 31; అమల్లో: Jan 1, 2026."),

    (2, 3,
     "AP జిల్లాల సంఖ్య మారిన క్రమం సరైనది ఏది?",
     "23 → 13 → 25 → 28", "23 → 13 → 26 → 28", "13 → 23 → 26 → 28", "10 → 13 → 25 → 28",
     "b",
     "AP జిల్లాల క్రమం: అవిభక్త AP = 23 జిల్లాలు → 2014 విభజన తర్వాత Residuary AP = 13 జిల్లాలు → YSRCP 2022 ఏప్రిల్ 4 = 26 జిల్లాలు → TDP-BJP 2026 జనవరి 1 = 28 జిల్లాలు."),

    # ==================== Section 3: Potti Sriramulu Statue ====================

    (3, 1,
     "పొట్టి శ్రీరాముల 'బలిదాన విగ్రహం' ఎక్కడ నిర్మిస్తున్నారు?",
     "నెల్లూరు", "హైదరాబాద్", "విజయవాడ", "అమరావతి",
     "d",
     "పొట్టి శ్రీరాముల 'బలిదాన విగ్రహం' అమరావతిలో నిర్మిస్తున్నారు — 6.8 ఎకరాల స్థలం కేటాయించారు. నెల్లూరు ఆయన జన్మస్థలం మాత్రమే; విగ్రహం అమరావతిలో."),

    (3, 1,
     "పొట్టి శ్రీరాముల విగ్రహం ఎత్తు 58 అడుగులు నిర్ణయించిన కారణం ఏది?",
     "58 సంవత్సరాలు జీవించారు", "నిరాహార దీక్షలో 58వ రోజున అమరులయ్యారు", "1958లో AP Foundation Day", "58 జిల్లాల కోసం",
     "b",
     "పొట్టి శ్రీరాముల నిరాహార దీక్షలో 58వ రోజున డిసెంబర్ 15, 1952న అమరులయ్యారు. ఆ 58 రోజులకు గుర్తుగా 58 అడుగుల విగ్రహం నిర్ణయించారు."),

    (3, 2,
     "పొట్టి శ్రీరాముల విగ్రహం అంకితం లక్ష్య తేదీ ఏది?",
     "డిసెంబర్ 15, 2025", "జనవరి 26, 2026", "మార్చి 16, 2026", "నవంబర్ 1, 2026",
     "c",
     "పొట్టి శ్రీరాముల విగ్రహం మార్చి 16, 2026 (ఆయన జన్మదినం) నాడు అంకితం చేయాలని లక్ష్యం. ప్రకటన: డిసెంబర్ 15, 2025 (73వ వర్ధంతి)."),

    (3, 2,
     "పొట్టి శ్రీరాముల అమరత్వం తర్వాత ఆంధ్ర రాష్ట్రం ఏ తేదీన ఏర్పడింది?",
     "జనవరి 1, 1953", "అక్టోబర్ 1, 1953", "నవంబర్ 1, 1956", "జనవరి 26, 1950",
     "b",
     "పొట్టి శ్రీరాముల అమరత్వం (డిసెంబర్ 15, 1952) తర్వాత అక్టోబర్ 1, 1953న ఆంధ్ర రాష్ట్రం ఏర్పాటైంది. తర్వాత నవంబర్ 1, 1956న Andhra + Hyderabad కలిసి AP అయింది."),

    (3, 3,
     "పొట్టి శ్రీరాముల గురించి ఏది సరైనది?",
     "జన్మస్థలం అమరావతి; విగ్రహం నెల్లూరులో", "విగ్రహం నెల్లూరులో; జన్మదినం మార్చి 16", "జన్మస్థలం నెల్లూరు; విగ్రహం అమరావతిలో; జన్మదినం మార్చి 16, 1901", "జన్మస్థలం మదనపల్లె; అమరత్వం నెల్లూరులో",
     "c",
     "పొట్టి శ్రీరాముల: జన్మస్థలం = నెల్లూరు (మార్చి 16, 1901); అమరత్వం = డిసెంబర్ 15, 1952 మదనపల్లె లో; విగ్రహం = అమరావతిలో. నెల్లూరు జన్మస్థలం మాత్రమే."),

    # ==================== Section 4: IFR 2026 ====================

    (4, 1,
     "International Fleet Review (IFR) 2026 ఎక్కడ జరిగింది?",
     "ముంబయి", "చెన్నై", "కొచ్చిన్", "విశాఖపట్నం",
     "d",
     "International Fleet Review 2026 ఫిబ్రవరి 18, 2026న విశాఖపట్నం తీర సముద్రంలో జరిగింది. విశాఖ తూర్పు నావల్ కమాండ్ కేంద్రం కావడంతో IFR కి ఆదర్శ స్థలం."),

    (4, 1,
     "IFR 2026 థీమ్ ఏమిటి?",
     "Secure Seas, Secure Nation", "Indian Ocean: Peace and Prosperity", "United Through Oceans", "Blue Economy Rising",
     "c",
     "IFR 2026 థీమ్: 'United Through Oceans' (మహాసముద్రాల ద్వారా ఐక్యత). రాష్ట్రపతి ద్రౌపది ముర్ము INS సుమేధా నౌకపై నుండి సమీక్షించారు."),

    (4, 2,
     "IFR 2026లో రాష్ట్రపతి ముర్ము ఏ నౌకపై నుండి fleet review చేశారు?",
     "INS విక్రమాదిత్య", "INS కోల్‌కతా", "INS సుమేధా", "INS అర్నాల",
     "c",
     "రాష్ట్రపతి ద్రౌపది ముర్ము INS సుమేధా (Sumedha) నౌకపై నుండి IFR 2026 సమీక్షించారు. INS సుమేధా స్వదేశీ నిర్మిత Offshore Patrol Vessel (OPV)."),

    (4, 2,
     "IFR 2026లో ఎన్ని దేశాలు పాల్గొన్నాయి?",
     "52 దేశాలు", "61 దేశాలు", "74 దేశాలు", "90 దేశాలు",
     "c",
     "IFR 2026లో 74 దేశాలు పాల్గొన్నాయి. 85 నౌకలు (66 భారతీయ + 19 విదేశీ) + 3 submarines + 60 పైగా aircraft పాల్గొన్నాయి."),

    (4, 3,
     "భారత్ నిర్వహించిన IFR చరిత్ర క్రమం సరైనది ఏది?",
     "2001 → 2011 → 2026", "2001 → 2016 → 2026", "1998 → 2008 → 2026", "2005 → 2016 → 2026",
     "b",
     "భారత్ నిర్వహించిన IFR లు: 1వ IFR = 2001, 2వ IFR = 2016, 3వ IFR = 2026 (విశాఖపట్నం). IFR 2026 భారత్ నిర్వహించిన 3వ అంతర్జాతీయ ఫ్లీట్ రివ్యూ."),

    (4, 3,
     "MAHASAGAR అంటే ఏమిటి — IFR 2026 సందర్భంగా భారత్ ప్రకటించిన vision?",
     "Maritime and Holistic Agility for Security Across Global Asian Regions", "Mutual and Holistic Advancement for Security and Growth Across Regions", "Maritime Association for Harmony, Security and Growth Across Regions", "Marine and Hydrographic Alliance for Safety, Growth Across Regions",
     "b",
     "MAHASAGAR = Mutual and Holistic Advancement for Security and Growth Across Regions. ఇది IFR 2026 సందర్భంగా భారత్ ప్రకటించిన Indian Ocean అంతర్జాతీయ భాగస్వామ్య vision."),

    # ==================== Section 5: AP Reorganisation Amendment Act ====================

    (5, 1,
     "AP Reorganisation (Amendment) Act 2026 ఏ రాజధానిని AP ఏకైక రాజధానిగా గుర్తించింది?",
     "విజయవాడ", "విశాఖపట్నం", "అమరావతి", "కర్నూలు",
     "c",
     "AP Reorganisation (Amendment) Act 2026 ద్వారా అమరావతిని AP ఏకైక (Sole and Permanent) రాజధానిగా చట్టపరంగా గుర్తించారు. Section 5 of AP Reorganisation Act, 2014 సవరణ."),

    (5, 1,
     "AP Reorganisation (Amendment) Act 2026 AP Reorganisation Act 2014 లోని ఏ Section కి సవరణ?",
     "Section 3", "Section 4", "Section 5", "Section 7",
     "c",
     "AP Reorganisation (Amendment) Act 2026 = 2014 AP Reorganisation Act లోని Section 5 కి సవరణ. Section 5 రాజధాని నగరాన్ని నిర్ణయించే section."),

    (5, 2,
     "YSRCP ప్రభుత్వం ప్రతిపాదించిన మూడు రాజధానుల్లో Judicial Capital (న్యాయ రాజధాని) ఏది?",
     "అమరావతి", "విశాఖపట్నం", "కర్నూలు", "నెల్లూరు",
     "c",
     "YSRCP ప్రభుత్వం మూడు రాజధానులు: అమరావతి (Legislative), కర్నూలు (Judicial), విశాఖపట్నం (Executive). 2026 Amendment Act తర్వాత అమరావతి మాత్రమే రాజధాని."),

    (5, 3,
     "AP Reorganisation Act మొదట ఏ సంవత్సరంలో పార్లమెంట్ ఆమోదించింది?",
     "2009", "2012", "2014", "2019",
     "c",
     "AP Reorganisation Act 2014లో తెలంగాణ-AP విభజన సమయంలో పార్లమెంట్ ఆమోదించింది. ఈ చట్టానికి 2026లో సవరణ చేసి అమరావతిని Legal Capital గా ధృవీకరించారు."),

    # ==================== Section 6: BharatNet ====================

    (6, 1,
     "AP లో BharatNet ప్రాజెక్ట్ కి ఎంత నిధులు కేటాయించారు?",
     "₹1,200 కోట్లు", "₹2,432 కోట్లు", "₹5,000 కోట్లు", "₹8,500 కోట్లు",
     "b",
     "AP లో BharatNet Phase 3 ప్రాజెక్ట్ కి ₹2,432 కోట్లు కేటాయించారు. అమలు సంస్థ: APBIL (Andhra Pradesh BharatNet Infrastructure Limited)."),

    (6, 2,
     "BharatNet AP అమలు సంస్థ పూర్తి పేరు ఏమిటి?",
     "AP Broadband Infrastructure Limited", "Andhra Pradesh BharatNet Infrastructure Limited", "AP Digital Networks Limited", "AP Fiber Optic Corporation",
     "b",
     "BharatNet AP అమలు సంస్థ పేరు APBIL = Andhra Pradesh BharatNet Infrastructure Limited. నిధులు Digital Bharat Nidhi (DBN) నుండి వస్తాయి."),

    (6, 3,
     "BharatNet ప్రాజెక్ట్ లక్ష్యం ఏమిటి?",
     "అన్ని cities కి 5G coverage", "అన్ని gram panchayats కి optical fiber broadband connectivity", "అన్ని జిల్లా కేంద్రాలకు WiFi", "అన్ని రైల్వే స్టేషన్లకు broadband",
     "b",
     "BharatNet లక్ష్యం AP లో అన్ని gram panchayats కి high-speed optical fiber broadband connectivity అందించడం. గ్రామీణ digital divide తొలగించడమే ఉద్దేశ్యం."),

    # ==================== Section 7: AM Green Kakinada ====================

    (7, 1,
     "AM Green కాకినాడ Green Ammonia Plant — ఇది ఏ రికార్డు కలిగి ఉంది?",
     "భారత్ లోనే అతిపెద్ద", "ఆసియాలోనే అతిపెద్ద", "ప్రపంచంలోనే అతిపెద్ద", "దక్షిణ ఆసియాలో మొదటి",
     "c",
     "AM Green కాకినాడ Green Ammonia Plant ప్రపంచంలోనే అతిపెద్ద (World's Largest) Green Ammonia Plant. సామర్థ్యం 1.5 MTPA; పెట్టుబడి ₹13,000 కోట్లు."),

    (7, 1,
     "AM Green కాకినాడ Plant లో Green Ammonia production సామర్థ్యం ఎంత?",
     "0.5 MTPA", "1.0 MTPA", "1.5 MTPA", "2.0 MTPA",
     "c",
     "AM Green కాకినాడ Green Ammonia Plant సామర్థ్యం 1.5 MTPA (Million Tonnes Per Annum). ఇది ప్రపంచంలోనే అతిపెద్ద Green Ammonia Plant."),

    (7, 2,
     "AM Green ఏ parent group కి చెందిన కంపెనీ?",
     "Reliance Group", "Adani Group", "Greenko Group", "NTPC",
     "c",
     "AM Green = Greenko Group అనుబంధ (subsidiary) సంస్థ. Greenko Group Hyderabad ఆధారిత renewable energy company."),

    (7, 2,
     "AM Green కాకినాడ Plant నుండి Green Ammonia ఏ దేశాలకు ఎగుమతి అవుతుంది?",
     "USA, UK, France", "జర్మనీ, జపాన్, సింగపూర్", "China, Russia, Australia", "UAE, Saudi Arabia, Kuwait",
     "b",
     "AM Green కాకినాడ నుండి Green Ammonia జర్మనీ, జపాన్, సింగపూర్ కి ఎగుమతి అవుతుంది. జర్మన్ కంపెనీ Uniper తో ఒప్పందం కుదిరింది."),

    (7, 3,
     "Green Ammonia ఎలా తయారవుతుంది?",
     "Coal gasification ద్వారా Hydrogen; తర్వాత Ammonia", "Natural gas steam reforming ద్వారా", "Renewable energy తో water electrolysis → Hydrogen → Ammonia", "Nuclear power తో direct synthesis",
     "c",
     "Green Ammonia: Renewable energy (solar/wind) → water electrolysis → Green Hydrogen → Haber-Bosch process → Ammonia (NH3). Carbon emissions శూన్యం — అందుకే 'Green' అంటారు."),

    # ==================== Section 8: Auto Driverla Sevalo ====================

    (8, 1,
     "Auto Driverla Sevalo పథకం ఏ తేదీన ప్రారంభమైంది?",
     "ఆగస్టు 15, 2025", "సెప్టెంబర్ 5, 2025", "అక్టోబర్ 4, 2025", "నవంబర్ 1, 2025",
     "c",
     "Auto Driverla Sevalo పథకం అక్టోబర్ 4, 2025న AP ప్రభుత్వం ప్రారంభించింది. Auto, Cab, Maxi Cab drivers కి ఏటా ₹15,000 ఆర్థిక సహాయం."),

    (8, 1,
     "Auto Driverla Sevalo పథకం కింద drivers కి ఏటా ఎంత సహాయం అందిస్తారు?",
     "₹5,000", "₹10,000", "₹15,000", "₹20,000",
     "c",
     "Auto Driverla Sevalo పథకం కింద Auto, Cab, Maxi Cab drivers కి ఏటా ₹15,000 ఆర్థిక సహాయం అందిస్తారు. 2.9 లక్షల మంది అర్హులు."),

    (8, 2,
     "Auto Driverla Sevalo పాత పేరు ఏమిటి?",
     "Vahana Rakshak", "Vahana Mitra", "Driver Bhagya", "Savari Sahayam",
     "b",
     "Auto Driverla Sevalo = పాత Vahana Mitra పథకం పేరు మారింది. TDP ప్రభుత్వం పేరు మార్చి అదే benefit కొనసాగించింది."),

    (8, 3,
     "Auto Driverla Sevalo పథకంలో ఎంత మంది అర్హులైన drivers ఉన్నారు?",
     "1.5 లక్షలు", "2.3 లక్షలు", "2.9 లక్షలు", "4.5 లక్షలు",
     "c",
     "Auto Driverla Sevalo పథకంలో 2.9 లక్షల మంది అర్హులైన drivers లబ్ధిదారులు. Auto, Cab, Maxi Cab drivers అందరికీ వర్తిస్తుంది."),

    # ==================== Section 9: DGP & CS Appointments ====================

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

    (9, 2,
     "TDP ప్రభుత్వం జూన్ 2024లో AP DGP గా ముందుగా ఎవరిని నియమించింది?",
     "హరీష్ కుమార్ గుప్తా", "Ch. ద్వారక తిరుమల రావు", "K.V. రాజేంద్రనాథ్ రెడ్డి", "నీరబ్ కుమార్ ప్రసాద్",
     "b",
     "TDP ప్రభుత్వం జూన్ 20, 2024న అధికారంలోకి వచ్చిన తర్వాత Ch. ద్వారక తిరుమల రావు (IPS 1989 batch) ని DGP గా నియమించింది. తర్వాత జనవరి 31, 2025 నుండి హరీష్ కుమార్ గుప్తా DGP అయ్యారు."),

    (9, 3,
     "AP CS timeline 2024-2026 సరైన క్రమం ఏది?",
     "నీరబ్ (2024) → హరీష్ గుప్తా (2025) → K. విజయానంద్ (2026)", "నీరబ్ (2024) → K. విజయానంద్ (2025) → G. సాయి ప్రసాద్ (2026)", "K. విజయానంద్ (2024) → నీరబ్ (2025) → G. సాయి ప్రసాద్ (2026)", "G. సాయి ప్రసాద్ (2024) → నీరబ్ (2025) → K. విజయానంద్ (2026)",
     "b",
     "AP CS క్రమం: నీరబ్ కుమార్ ప్రసాద్ (జూన్ 2024 – డిసెంబర్ 31, 2024, 1987 IAS) → K. విజయానంద్ (జనవరి 1, 2025 – ఫిబ్రవరి 28, 2026, 1992 IAS) → G. సాయి ప్రసాద్ (మార్చి 1, 2026 నుండి, 1991 IAS)."),

    (9, 3,
     "AP HC Chief Justice జస్టిస్ లిసా గిల్ — AP HC ముఖ్యాలయం ఎక్కడ ఉంది?",
     "హైదరాబాద్", "విజయవాడ", "నెల్లూరు", "అమరావతి",
     "d",
     "AP హైకోర్టు ముఖ్యాలయం అమరావతిలో ఉంది. జస్టిస్ లిసా గిల్ AP HC ప్రధాన న్యాయమూర్తి. SC కొలీజియం సిఫారసు మేరకు రాష్ట్రపతి నియమించారు."),

    # ==================== Section 10: Other Events ====================

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

    (10, 2,
     "ISTC @ IMU విశాఖపట్నం ఏ ప్రాంతంలో మొదటిది?",
     "మొత్తం ఆసియా", "దక్షిణ ఆసియా", "ఆగ్నేయ ఆసియా", "దక్షిణ భారత్",
     "b",
     "ISTC (International Seafarers Training Centre) @ IMU విశాఖపట్నం సెప్టెంబర్ 20, 2025న ప్రారంభమైంది. దక్షిణ ఆసియా (South Asia) లో ఈ స్థాయి అంతర్జాతీయ నావికుల అడ్వాన్స్‌డ్ శిక్షణ కేంద్రం ఇది మొదటిది."),

    (10, 2,
     "AP Universal Health Policy AP కేబినెట్ ఏ తేదీన ఆమోదించింది?",
     "ఆగస్టు 1, 2025", "సెప్టెంబర్ 4, 2025", "అక్టోబర్ 2, 2025", "నవంబర్ 15, 2025",
     "b",
     "AP కేబినెట్ Universal Health Policy సెప్టెంబర్ 4, 2025న ఆమోదించింది. ఆరోగ్య శ్రీ విస్తరణ — అన్ని కుటుంబాలకు ఆదాయ పరిమితి లేకుండా ఆరోగ్య కవరేజ్."),

    (10, 3,
     "TDP స్థాపించిన నేత ఎవరు? CM చంద్రబాబు నాయుడు TDP స్థాపకునికి ఏమి అవుతారు?",
     "TDP స్థాపకుడు: CM చంద్రబాబు; సంబంధం: అల్లుడు", "TDP స్థాపకుడు: NTR; సంబంధం: అల్లుడు", "TDP స్థాపకుడు: NTR; సంబంధం: కొడుకు", "TDP స్థాపకుడు: నీలం సంజీవ రెడ్డి; సంబంధం: వారసుడు",
     "b",
     "TDP స్థాపకుడు: N.T. రామారావు (NTR), మార్చి 29, 1982. CM నారా చంద్రబాబు నాయుడు = NTR అల్లుడు (son-in-law). చంద్రబాబు భార్య: NTR కుమార్తె నారా భువనేశ్వరి."),

]


def _seed_ap_ca_div4_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study note for Division 4 — 2025 Aug – 2026 Apr."""
    import pathlib

    ph = "%s" if USE_POSTGRES else "?"
    existing = db_exec(
        conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
        ("AP_Current_Affairs", 4)
    ).fetchone()

    if existing and not force:
        return

    html_path = pathlib.Path(__file__).parent / "static" / "notes" / "ap_ca_div4_notes.html"
    content_html = html_path.read_text(encoding="utf-8") if html_path.exists() else ""
    sections_json_str = _json.dumps(SECTIONS_JSON, ensure_ascii=False)

    if existing:
        db_exec(conn, f"""
            UPDATE study_notes SET
                chapter_title_te={ph}, chapter_title_en={ph},
                pages_ref={ph}, sections_json={ph}, content={ph}
            WHERE id={ph}
        """, (
            "2025 ఆగస్టు–2026 ఏప్రిల్ ముఖ్య సంఘటనలు",
            "2025 August–2026 April Major Events",
            "Div-4 • Eenadu+Sakshi verified • Aug 2025–Apr 2026 | DGP: హరీష్ కుమార్ గుప్తా | CS: G.సాయి ప్రసాద్",
            sections_json_str,
            content_html,
            existing[0]
        ))
    else:
        db_exec(conn, f"""
            INSERT INTO study_notes
                (topic, subject, subtopic, chapter_num, chapter_title_te, chapter_title_en,
                 pages_ref, sections_json, content)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})
        """, (
            "AP_Current_Affairs",
            "AP Current Affairs",
            "AP Events Aug 2025–Apr 2026",
            4,
            "2025 ఆగస్టు–2026 ఏప్రిల్ ముఖ్య సంఘటనలు",
            "2025 August–2026 April Major Events",
            "Div-4 • Eenadu+Sakshi verified • Aug 2025–Apr 2026 | DGP: హరీష్ కుమార్ గుప్తా | CS: G.సాయి ప్రసాద్",
            sections_json_str,
            content_html,
        ))

    if hasattr(conn, "commit"):
        conn.commit()


def _seed_ap_ca_div4_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for Division 4."""
    ph = "%s" if USE_POSTGRES else "?"

    note_row = db_exec(
        conn,
        f"SELECT id FROM study_notes WHERE topic={ph} AND chapter_num={ph}",
        ("AP_Current_Affairs", 4)
    ).fetchone()
    if not note_row:
        return

    note_id = note_row[0]

    existing_count = db_exec(
        conn,
        f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}",
        (note_id,)
    ).fetchone()[0]

    if existing_count > 0 and not force:
        return

    if force:
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    for (sec_idx, diff, q_te, a, b, c, d, ans, exp_te) in MCQ_DATA:
        db_exec(conn, f"""
            INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})
        """, (note_id, sec_idx, diff, q_te, a, b, c, d, ans, exp_te))

    if hasattr(conn, "commit"):
        conn.commit()
