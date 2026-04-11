"""
seed_ap_ca_div1.py — AP Current Affairs Division 1: 2024 Elections & Cabinet
ఆంధ్రప్రదేశ్ కరెంట్ అఫైర్స్ — విభాగం 1: 2024 ఎన్నికలు & కేబినెట్
"""
import json as _json

SECTIONS_JSON = [
    {
        "title": "2024 AP అసెంబ్లీ ఎన్నికలు",
        "sub": "AP Assembly Elections 2024 — Basic Details",
        "audio": "2024 ఆంధ్రప్రదేశ్ శాసనసభ ఎన్నికలు మే 13, 2024న జరిగాయి. ఫలితాలు జూన్ 4, 2024న ప్రకటించారు. మొత్తం 175 అసెంబ్లీ సీట్లకు ఎన్నికలు జరిగాయి. మెజారిటీ మార్క్ 88. పోలింగ్ శాతం 81.86%. దార్సి నియోజకవర్గంలో అత్యధిక పోలింగ్ 90.91%. తిరుపతి నియోజకవర్గంలో అత్యల్ప పోలింగ్ 63.32%. ఇది లోక్‌సభ ఎన్నికలతో పాటు ఒకేసారి జరిగింది."
    },
    {
        "title": "కూటమి విజయం",
        "sub": "TDP-JSP-BJP Alliance Victory — Seat Count & Vote Share",
        "audio": "TDP-JSP-BJP కూటమి మొత్తం 164 సీట్లు గెలుచుకుంది. TDP 144 నియోజకవర్గాల్లో 135 సీట్లు గెలిచింది. JSP 21 నియోజకవర్గాల్లో పోటీ చేసి 21 సీట్లూ గెలిచింది (100% strike rate!). BJP 10 నియోజకవర్గాల్లో 8 సీట్లు గెలిచింది. కూటమి మొత్తం ఓట్ల శాతం 53% కంటే ఎక్కువ. YSRCP 175 సీట్లు పోటీ చేసి కేవలం 11 సీట్లు గెలిచింది. 2019లో YSRCP 151 సీట్లు గెలిచింది."
    },
    {
        "title": "లోక్‌సభ ఫలితాలు AP",
        "sub": "Lok Sabha 2024 Results — AP (25 Seats)",
        "audio": "ఆంధ్రప్రదేశ్ నుండి మొత్తం 25 లోక్‌సభ స్థానాలు ఉన్నాయి. TDP 17 స్థానాల్లో పోటీ చేసి 16 గెలిచింది. JSP 2 స్థానాల్లో 2 గెలిచింది (కాకినాడ: తంగెళ్ళ ఉదయ్ శ్రీనివాస్; మచిలీపట్నం: వల్లభనేని బాలశౌరి). BJP 6 స్థానాల్లో 3 గెలిచింది. కూటమి మొత్తం 21 లోక్‌సభ స్థానాలు గెలిచింది. YSRCP 25 స్థానాల్లో 4 మాత్రమే గెలిచింది. పవన్ కళ్యాణ్ పిఠాపురం అసెంబ్లీ MLA మాత్రమే — ఆయన లోక్‌సభ ఎన్నికల్లో పోటీ చేయలేదు. పిఠాపురం పరిధిలో కాకినాడ లోక్‌సభ స్థానంలో JSP తంగెళ్ళ ఉదయ్ శ్రీనివాస్ గెలిచారు."
    },
    {
        "title": "కేబినెట్ నిర్మాణం",
        "sub": "Cabinet Formation — Composition & Key Dates",
        "audio": "నాల్గవ నాయుడు మంత్రివర్గం జూన్ 12, 2024న శపథ స్వీకారం చేసింది. జూన్ 14, 2024న పోర్ట్‌ఫోలియో పంపిణీ జరిగింది. మొత్తం 25 మంత్రులు (CM తో సహా). TDP నుండి 21, JSP నుండి 3, BJP నుండి 1 మంత్రి. 17 మంది తొలిసారి మంత్రులు (first-timers). 3 మంది మహిళా మంత్రులు. 8 మంది BC వర్గాల మంత్రులు. 2 SC, 1 ST, 1 Muslim మంత్రులు."
    },
    {
        "title": "CM & DCM — పదవులు",
        "sub": "Chief Minister & Deputy CM Details",
        "audio": "ముఖ్యమంత్రి నల్లపాటి చంద్రబాబు నాయుడు కుప్పం నియోజకవర్గం నుండి. ఇది ఆయన నాల్గవ సారి ముఖ్యమంత్రి పదవి. TDP స్థాపకుడు NTR (నందమూరి తారక రామారావు) 1982లో స్థాపించారు. CBN GAD, Law & Order, Public Enterprises నిర్వహిస్తారు. ఉపముఖ్యమంత్రి పవన్ కళ్యాణ్ JSP నాయకుడు, పిఠాపురం నుండి. పంచాయతీ రాజ్, గ్రామీణాభివృద్ధి, అడవులు, పర్యావరణం, సైన్స్ అండ్ టెక్నాలజీ పోర్ట్‌ఫోలియో."
    },
    {
        "title": "కీలక మంత్రులు — పోర్ట్‌ఫోలియో",
        "sub": "Key Ministers and their Portfolios",
        "audio": "నారా లోకేష్ HRD (విద్య), IT ఎలక్ట్రానిక్స్, RTG. వంగలపూడి అనిత Home Affairs, Disaster Management. పయ్యావుల కేశవ్ Finance, Planning, Commercial Taxes. సత్యకుమార్ యాదవ్ (BJP, ధర్మవరం) Health, Medical Education — BJP నుండి ఏకైక మంత్రి. నాస్యం మొహమ్మద్ ఫారూఖ్ (నందల్) Law & Justice, Minority Welfare — ఏకైక ముస్లిం మంత్రి. కొలుసు పార్థసారథి Housing, I&PR. గొట్టిపాటి రవికుమార్ Energy. మండిపల్లి రాంప్రసాద్ రెడ్డి (రాయచోటి) Transport, Youth & Sports. అనగాని సత్యప్రసాద్ Revenue, Stamps & Registration."
    },
    {
        "title": "JSP మంత్రులు & ఇతర మంత్రులు",
        "sub": "JSP Ministers & Other Key Ministers",
        "audio": "JSP నుండి 3 మంత్రులు: పవన్ కళ్యాణ్ (DCM), నాదెండ్ల మనోహర్ (Civil Supplies, Consumer Affairs), కందుల దుర్గేష్ (Tourism, Culture & Cinematography). ఇతర TDP మంత్రులు: P. నారాయణ — MAUD. నిమ్మల రమానాయుడు (పాలకొల్లు) — Water Resources. BC జనార్దన్ రెడ్డి (బనగానపల్లె) — Roads & Buildings, Infrastructure & Investments. కొండపల్లి శ్రీనివాస్ (గజపతినగరం) — MSME, SERP, NRI Affairs. డోలా శ్రీ బాలవీరాంజనేయ స్వామి (కొండపి SC) — Social Welfare, Disabled & Senior Citizen Welfare. వాసంసెట్టి సుభాష్ (రామచంద్రాపురం) — Labour, Factories & Boilers. కొలు రవీంద్ర (మచిలీపట్నం) — Mines & Geology, Excise. అనం రమానారాయణ రెడ్డి (ఆత్మకూరు) — Endowments. తి.గ. భారతి (కర్నూల్) — Industries & Commerce, Food Processing."
    },
    {
        "title": "రాజ్యాంగ పదవులు & ముఖ్య వ్యక్తులు",
        "sub": "Constitutional Positions & Key Officials",
        "audio": "ఆంధ్రప్రదేశ్ గవర్నర్ జస్టిస్ ఎస్. అబ్దుల్ నజీర్, ఫిబ్రవరి 2023 నుండి (మాజీ సుప్రీంకోర్టు న్యాయమూర్తి). శాసనసభ స్పీకర్ అయ్యన్న పాత్రుడు (TDP), జూన్ 2024లో ఎన్నుకున్నారు. AP రాష్ట్రసభ స్థానాలు 11. ముఖ్య కార్యదర్శి నీరబ్ కుమార్ ప్రసాద్ (IAS 1992). పయ్యావుల కేశవ్ ఆర్థికమంత్రిగా ఫిబ్రవరి 28, 2025న బడ్జెట్ సమర్పించారు."
    },
]

# MCQ_DATA: (section_idx, difficulty, question_te, opt_a, opt_b, opt_c, opt_d, answer, explanation_te)
MCQ_DATA = [
    # ---- Section 0: Assembly Elections Basic ----
    (0, 1,
     "2024 AP శాసనసభ ఎన్నికలు ఏ తేదీన జరిగాయి?",
     "మే 13, 2024", "జూన్ 4, 2024", "ఏప్రిల్ 13, 2024", "మే 4, 2024",
     "a",
     "2024 AP అసెంబ్లీ ఎన్నికలు మే 13, 2024న జరిగాయి. ఫలితాలు జూన్ 4, 2024న ప్రకటించారు."),

    (0, 1,
     "2024 AP అసెంబ్లీ ఎన్నికల ఫలితాలు ఏ తేదీన ప్రకటించారు?",
     "మే 13, 2024", "జూన్ 4, 2024", "జూన్ 12, 2024", "జూన్ 14, 2024",
     "b",
     "2024 AP ఎన్నికల ఫలితాలు జూన్ 4, 2024న వెలువడ్డాయి. మే 13న ఓటింగ్ జరిగింది."),

    (0, 1,
     "2024 AP శాసనసభలో మొత్తం ఎన్ని సీట్లు ఉన్నాయి?",
     "170", "178", "175", "180",
     "c",
     "ఆంధ్రప్రదేశ్ శాసనసభలో మొత్తం 175 సీట్లు ఉన్నాయి. మెజారిటీకి 88 సీట్లు అవసరం."),

    (0, 2,
     "2024 AP అసెంబ్లీ ఎన్నికల్లో మొత్తం పోలింగ్ శాతం ఎంత?",
     "75.86%", "81.86%", "79.86%", "85.86%",
     "b",
     "2024 AP అసెంబ్లీ ఎన్నికల్లో మొత్తం పోలింగ్ శాతం 81.86%."),

    (0, 2,
     "2024 AP ఎన్నికల్లో అత్యధిక పోలింగ్ శాతం నమోదు చేసిన నియోజకవర్గం?",
     "తిరుపతి", "విజయవాడ", "దార్సి", "రాజమండ్రి",
     "c",
     "దార్సి (Darsi) నియోజకవర్గంలో అత్యధిక పోలింగ్ 90.91% నమోదైంది."),

    (0, 2,
     "2024 AP ఎన్నికల్లో అత్యల్ప పోలింగ్ శాతం నమోదు చేసిన నియోజకవర్గం?",
     "కర్నూలు", "తిరుపతి", "గుంటూరు", "విజయవాడ",
     "b",
     "తిరుపతి నియోజకవర్గంలో అత్యల్ప పోలింగ్ 63.32% నమోదైంది."),

    # ---- Section 1: Alliance Victory ----
    (1, 1,
     "2024 AP ఎన్నికల్లో TDP-JSP-BJP కూటమి మొత్తం ఎన్ని సీట్లు గెలిచింది?",
     "160", "164", "170", "175",
     "b",
     "TDP-JSP-BJP కూటమి 175 సీట్లలో 164 సీట్లు గెలుచుకుంది — AP చరిత్రలో అసాధారణ విజయం."),

    (1, 1,
     "2024 AP ఎన్నికల్లో TDP ఎన్ని సీట్లు గెలిచింది?",
     "130", "135", "140", "144",
     "b",
     "TDP 144 నియోజకవర్గాల్లో పోటీ చేసి 135 సీట్లు గెలిచింది."),

    (1, 1,
     "2024 AP ఎన్నికల్లో JSP ఎన్ని సీట్లు పోటీ చేసి ఎన్ని గెలిచింది?",
     "21 లో 18", "21 లో 21", "25 లో 21", "20 లో 21",
     "b",
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
     "2024 AP ఎన్నికల్లో TDP ఓట్ల శాతం సుమారు ఎంత?",
     "~30%", "~39%", "~45%", "~50%",
     "b",
     "TDP ఓట్ల శాతం సుమారు 39.18%. YSRCP ఓట్ల శాతం కూడా ~39.37% — దాదాపు సమానం, కానీ సీట్లలో తేడా చాలా ఉంది!"),

    # ---- Section 2: Lok Sabha ----
    (2, 1,
     "ఆంధ్రప్రదేశ్ నుండి మొత్తం ఎన్ని లోక్‌సభ స్థానాలు ఉన్నాయి?",
     "21", "23", "25", "28",
     "c",
     "AP నుండి మొత్తం 25 లోక్‌సభ స్థానాలు ఉన్నాయి."),

    (2, 1,
     "2024 AP లోక్‌సభ ఎన్నికల్లో కూటమి ఎన్ని స్థానాలు గెలిచింది?",
     "19", "21", "23", "25",
     "b",
     "TDP-JSP-BJP కూటమి AP లో 25 లోక్‌సభ స్థానాల్లో 21 గెలిచింది."),

    (2, 2,
     "2024 అసెంబ్లీ ఎన్నికల్లో పవన్ కళ్యాణ్ ఏ నియోజకవర్గం నుండి గెలిచారు? ఆయన లోక్‌సభకు కూడా పోటీ చేశారా?",
     "అనకాపల్లి, లోక్‌సభ కూడా గెలిచారు", "పిఠాపురం, అసెంబ్లీ మాత్రమే", "రాజమండ్రి, అసెంబ్లీ మాత్రమే", "కాకినాడ, లోక్‌సభ మాత్రమే",
     "b",
     "పవన్ కళ్యాణ్ పిఠాపురం అసెంబ్లీ (MLA) నుండి గెలిచారు — లోక్‌సభ ఎన్నికల్లో పోటీ చేయలేదు! కాకినాడ లోక్‌సభ స్థానంలో JSP తంగెళ్ళ ఉదయ్ శ్రీనివాస్ గెలిచారు."),

    # ---- Section 3: Cabinet Formation ----
    (3, 1,
     "చంద్రబాబు నాయుడు నాల్గవ మంత్రివర్గం శపథ స్వీకారం ఏ తేదీన జరిగింది?",
     "జూన్ 4, 2024", "జూన్ 12, 2024", "జూన్ 14, 2024", "జూలై 1, 2024",
     "b",
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

    # ---- Section 4: CM & DCM ----
    (4, 1,
     "AP ముఖ్యమంత్రి చంద్రబాబు నాయుడు ఏ నియోజకవర్గం నుండి?",
     "మంగళగిరి", "కుప్పం", "ఉరవకొండ", "నెల్లూరు",
     "b",
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
     "రాపూరు", "అనకాపల్లి", "పిఠాపురం", "రాజమండ్రి",
     "b",
     "పవన్ కళ్యాణ్ పిఠాపురం నియోజకవర్గం (తూర్పు గోదావరి జిల్లా) నుండి గెలిచారు."),

    (4, 3,
     "CBN పోర్ట్‌ఫోలియోలో కింది వాటిలో ఏది చేర్చలేదు?",
     "GAD", "Finance", "Law & Order", "Public Enterprises",
     "b",
     "CBN నాయుడు GAD, Law & Order, Public Enterprises నిర్వహిస్తారు. Finance పోర్ట్‌ఫోలియో పయ్యావుల కేశవ్‌కు ఇచ్చారు."),

    # ---- Section 5: Key Ministers & Portfolios ----
    (5, 1,
     "AP ఆర్థిక మంత్రి (Finance Minister) ఎవరు?",
     "నారా లోకేష్", "అచ్చెన్నాయుడు", "పయ్యావుల కేశవ్", "వంగలపూడి అనిత",
     "c",
     "పయ్యావుల కేశవ్ (TDP) AP ఆర్థిక మంత్రి. ఆయన ఉరవకొండ నియోజకవర్గం (అనంతపురం జిల్లా) నుండి ఎన్నికయ్యారు, ఫిబ్రవరి 28, 2025న బడ్జెట్ సమర్పించారు."),

    (5, 1,
     "AP హోం మంత్రి (Home Minister) ఎవరు?",
     "పవన్ కళ్యాణ్", "వంగలపూడి అనిత", "అచ్చెన్నాయుడు", "నాస్యం ఫారూఖ్",
     "b",
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
     "అనగాని సత్య ప్రసాద్ — Revenue", "సత్యకుమార్ యాదవ్ — Health", "కందుల దుర్గేష్ — Social Welfare", "నాదెండ్ల మనోహర్ — Civil Supplies",
     "b",
     "BJP నుండి సత్యకుమార్ యాదవ్ (ధర్మవరం MLA) ఏకైక మంత్రి — Health, Family Welfare, Medical Education పోర్ట్‌ఫోలియో."),

    (5, 2,
     "AP కేబినెట్‌లో ఏకైక ముస్లిం మంత్రి ఎవరు?",
     "అసదుద్దీన్ ఓవైసీ", "నాస్యం మొహమ్మద్ ఫారూఖ్", "అబ్దుల్ నజీర్", "ఇమ్రాన్ ఖాన్",
     "b",
     "నాస్యం మొహమ్మద్ ఫారూఖ్ (TDP, నందల్) Law & Justice, Minority Welfare మంత్రి — ఏకైక ముస్లిం మంత్రి."),

    (5, 2,
     "AP కేబినెట్‌లో Energy (విద్యుత్) పోర్ట్‌ఫోలియో ఎవరికి?",
     "మండిపల్లి రాంప్రసాద్ రెడ్డి", "కొండపల్లి శ్రీనివాస్", "గొట్టిపాటి రవికుమార్", "అనగాని సత్యప్రసాద్",
     "c",
     "గొట్టిపాటి రవికుమార్ (TDP, అద్దంకి) Energy (విద్యుత్) పోర్ట్‌ఫోలియో నిర్వహిస్తారు."),

    (5, 3,
     "AP Transport & Youth Affairs మంత్రి ఎవరు?",
     "కొండపల్లి శ్రీనివాస్", "మండిపల్లి రాంప్రసాద్ రెడ్డి", "అనగాని సత్యప్రసాద్", "నిమ్మల రమానాయుడు",
     "b",
     "మండిపల్లి రాంప్రసాద్ రెడ్డి (TDP, రాయచోటి) Transport, Youth & Sports పోర్ట్‌ఫోలియో నిర్వహిస్తారు."),

    # ---- Section 6: JSP Ministers & Others ----
    (6, 1,
     "JSP నుండి AP కేబినెట్‌లో ఎంత మంది మంత్రులు ఉన్నారు?",
     "1", "2", "3", "4",
     "c",
     "JSP నుండి 3 మంది మంత్రులు: పవన్ కళ్యాణ్ (DCM), నాదెండ్ల మనోహర్, కందుల దుర్గేష్."),

    (6, 2,
     "AP Civil Supplies మంత్రి ఎవరు? వారి పార్టీ?",
     "పవన్ కళ్యాణ్, JSP", "నాదెండ్ల మనోహర్, JSP", "కందుల దుర్గేష్, JSP", "కొలుసు పార్థసారథి, TDP",
     "b",
     "నాదెండ్ల మనోహర్ (JSP) Civil Supplies, Consumer Affairs, Food Safety పోర్ట్‌ఫోలియో. JSP నుండి రెండో మంత్రి."),

    (6, 2,
     "AP Tourism, Culture & Cinematography మంత్రి ఎవరు?",
     "నాదెండ్ల మనోహర్", "కందుల దుర్గేష్", "సత్యకుమార్ యాదవ్", "అచ్చెన్నాయుడు",
     "b",
     "కందుల దుర్గేష్ (JSP, నిడదవోలు) Tourism, Culture & Cinematography పోర్ట్‌ఫోలియో నిర్వహిస్తారు. JSP నుండి మూడో మంత్రి."),

    (6, 3,
     "AP MSME, SERP, NRI Affairs మంత్రి ఎవరు?",
     "మండిపల్లి రాంప్రసాద్ రెడ్డి", "కొండపల్లి శ్రీనివాస్", "అనగాని సత్యప్రసాద్", "గొట్టిపాటి రవికుమార్",
     "b",
     "కొండపల్లి శ్రీనివాస్ (TDP, గజపతినగరం) MSME, SERP, NRI Affairs పోర్ట్‌ఫోలియో."),

    # ---- Section 7: Constitutional Positions ----
    (7, 1,
     "2024 నాటికి ఆంధ్రప్రదేశ్ గవర్నర్ ఎవరు?",
     "జస్టిస్ అబ్దుల్ నజీర్", "తమిళిసై సౌందరరాజన్", "బిశ్వభూషణ్ హరిచందన్", "ఆర్ఎన్ రవి",
     "a",
     "జస్టిస్ ఎస్. అబ్దుల్ నజీర్ AP గవర్నర్ (ఫిబ్రవరి 2023 నుండి). ఆయన మాజీ సుప్రీంకోర్టు న్యాయమూర్తి."),

    (7, 1,
     "AP శాసనసభ స్పీకర్ ఎవరు (2024)?",
     "అయ్యన్న పాత్రుడు", "నారా లోకేష్", "పయ్యావుల కేశవ్", "పవన్ కళ్యాణ్",
     "a",
     "అయ్యన్న పాత్రుడు (TDP) జూన్ 2024లో AP శాసనసభ స్పీకర్‌గా ఎన్నుకున్నారు."),

    (7, 2,
     "AP నుండి రాజ్యసభ (Rajya Sabha) స్థానాలు ఎన్ని?",
     "7", "9", "11", "13",
     "c",
     "ఆంధ్రప్రదేశ్ నుండి 11 రాజ్యసభ స్థానాలు ఉన్నాయి."),

    (7, 3,
     "AP Finance Minister పయ్యావుల కేశవ్ ఏ నియోజకవర్గం నుండి ఎన్నికయ్యారు?",
     "నెల్లూరు", "ఉరవకొండ", "కుప్పం", "ధర్మవరం",
     "b",
     "పయ్యావుల కేశవ్ ఉరవకొండ నియోజకవర్గం (అనంతపురం జిల్లా) నుండి ఎన్నికయ్యారు."),
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
