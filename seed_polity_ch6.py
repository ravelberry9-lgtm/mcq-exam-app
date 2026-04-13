# seed_polity_ch6.py
# Chapter 6: Citizenship
# (పౌరసత్వం)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total Sections: 9 | Total MCQs: 51 | PYQs: 6
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# PYQ: 10th element (index 9) = 'APPSC' or 'UPSC'
# ─────────────────────────────────────────────

import json as _json

POLITY_CH6_SECTIONS = [
    {
        "title": "6.1 పౌరసత్వం — పరిచయం మరియు రాజ్యాంగ అనుచ్ఛేదాలు",
        "sub": "Articles 5–11 · Part II · Citizenship at Commencement · Article 11",
        "audio": """పౌరసత్వం — పరిచయం (Introduction to Citizenship):

రాజ్యాంగంలో పౌరసత్వం:
• Part II (Articles 5–11) — రాజ్యాంగ అమలు సమయం (Commencement) లో పౌరసత్వం
• ఇవి తాత్కాలిక నిబంధనలు — శాశ్వత పౌరసత్వ చట్టం పార్లమెంట్ చేస్తుంది

ముఖ్యమైన ఆర్టికల్స్:
• Article 5  — రాజ్యాంగ అమలు సమయంలో పౌరసత్వం (Citizenship at Commencement)
• Article 6  — పాకిస్తాన్ నుండి వలసవచ్చిన వారి పౌరసత్వం
• Article 7  — పాకిస్తాన్‌కు వలసపోయి తిరిగి వచ్చిన వారి పౌరసత్వం
• Article 8  — విదేశాలలో నివసించే భారత సంతతి వారి పౌరసత్వం
• Article 9  — స్వచ్ఛందంగా విదేశ పౌరసత్వం తీసుకున్న వారికి పౌరసత్వం రద్దు
• Article 10 — పౌరసత్వ హక్కుల కొనసాగింపు
• Article 11 — పార్లమెంట్‌కు పౌరసత్వాన్ని చట్టం ద్వారా నియంత్రించే అధికారం

Article 11 ప్రాముఖ్యత:
• పార్లమెంట్ Citizenship Act 1955 చేసింది
• Citizenship Act 1955 పౌరసత్వ సంపాదన మరియు కోల్పోవడాన్ని నియంత్రిస్తుంది"""
    },
    {
        "title": "6.2 పౌరసత్వ సంపాదన — Citizenship Act 1955",
        "sub": "5 Methods · Birth · Descent · Registration · Naturalisation · Incorporation of Territory",
        "audio": """Citizenship Act 1955 — పౌరసత్వ సంపాదన పద్ధతులు:

పౌరసత్వం 5 పద్ధతుల్లో సంపాదించవచ్చు:

1. జన్మ ద్వారా (By Birth):
   • 1950 జనవరి 26 తర్వాత, 2003 జూలై 1 కంటే ముందు భారతదేశంలో జన్మించిన వారు
   • 2003 తర్వాత: తల్లిదండ్రులిద్దరూ భారత పౌరులైతే మాత్రమే

2. వంశావళి ద్వారా (By Descent):
   • విదేశాలలో జన్మించిన వారికి, తండ్రి/తల్లి భారత పౌరులైతే

3. నమోదు ద్వారా (By Registration):
   • భారత సంతతి వారు, Commonwealth దేశాల పౌరులు
   • 7 సంవత్సరాల నివాసం తర్వాత నమోదు

4. సహజీకరణ ద్వారా (By Naturalisation):
   • విదేశీయులకు 11 సంవత్సరాల నివాసం (గత 12 లో 11)
   • Commonwealth దేశాలకు 5 సంవత్సరాలు

5. భూభాగ విలీనం ద్వారా (By Incorporation of Territory):
   • కొత్త భూభాగం భారతదేశంలో విలీనమైనపుడు
   • ఉదా: Goa 1961, Sikkim 1975"""
    },
    {
        "title": "6.3 పౌరసత్వం కోల్పోవడం",
        "sub": "3 Methods of Loss · Renunciation · Termination · Deprivation",
        "audio": """పౌరసత్వం కోల్పోవడం (Loss of Citizenship) — 3 పద్ధతులు:

1. స్వచ్ఛంద త్యాగం (Renunciation):
   • వ్యక్తి స్వయంగా పౌరసత్వాన్ని వదులుకోవడం
   • మైనర్ పిల్లలు కూడా పౌరసత్వం కోల్పోతారు
   • వారు వయస్సుకు వచ్చాక తిరిగి తీసుకోవచ్చు

2. సమాప్తి (Termination):
   • స్వచ్ఛందంగా విదేశ పౌరసత్వం తీసుకున్నపుడు
   • Article 9 ప్రకారం అప్రమేయంగా (Automatically) రద్దవుతుంది

3. వంచన (Deprivation):
   • ప్రభుత్వం పౌరసత్వం రద్దు చేయడం
   • మోసంగా పౌరసత్వం సంపాదించినప్పుడు
   • రాష్ట్రానికి వ్యతిరేకంగా వ్యవహరించినప్పుడు
   • యుద్ధకాలంలో శత్రువుతో సహకరించినప్పుడు

ముఖ్యమైన విషయం:
• Renunciation = వ్యక్తి చొరవ (Voluntary)
• Termination = స్వతహాగా రద్దు (Automatic)
• Deprivation = ప్రభుత్వం రద్దు (Compulsory)"""
    },
    {
        "title": "6.4 ఏకైక పౌరసత్వం vs ద్వంద్వ పౌరసత్వం",
        "sub": "Single Citizenship · USA Dual Citizenship · Fundamental Rights for Citizens Only",
        "audio": """ఏకైక పౌరసత్వం (Single Citizenship):

భారత రాజ్యాంగం సిద్ధాంతం:
• భారత పౌరులకు ఒకే పౌరసత్వం — రాష్ట్ర పౌరసత్వం లేదు
• UK మోడల్ అనుసరించారు

USA తో తేడా:
• USA: రెండు స్థాయిల పౌరసత్వం (Dual Citizenship)
  — Federal Citizenship (American)
  — State Citizenship (Californian, Texan etc.)
• India: ఒక్క స్థాయి పౌరసత్వం మాత్రమే

ఏకైక పౌరసత్వం ప్రయోజనాలు:
• జాతీయ సమైక్యత (National Integration)
• దేశమంతటా సమాన హక్కులు
• రాష్ట్రాల మధ్య వివక్ష లేకుండా

పౌరులకు మాత్రమే లభించే హక్కులు (Citizen-only Rights):
• Fundamental Rights అన్నీ పౌరులకు — కానీ కొన్ని అందరికీ
• Art 15, 16 — వివక్ష నిషేధం, ప్రభుత్వ ఉద్యోగావకాశాలు
• Art 19 — 6 రకాల స్వేచ్ఛలు (పౌరులకు మాత్రమే)
• Art 29, 30 — సాంస్కృతిక మరియు విద్యా హక్కులు"""
    },
    {
        "title": "6.5 OCI, NRI మరియు PIO — విదేశీ భారతీయులు\nOverseas Indians · OCI Card · NRI · PIO",
        "sub": "Overseas Citizen of India · Non-Resident Indian · Person of Indian Origin",
        "audio": """విదేశాల్లో ఉండే భారతీయులకు సంబంధించిన వర్గాలు:

1. NRI (Non-Resident Indian — అనివాసి భారతీయుడు):
   • భారత పౌరసత్వం కలిగి విదేశాల్లో నివసిస్తున్న వారు
   • భారత పాస్‌పోర్ట్ కలిగి ఉంటారు
   • పూర్తి పౌరసత్వ హక్కులు కలిగి ఉంటారు

2. PIO (Person of Indian Origin — భారత సంతతి వ్యక్తి):
   • విదేశ పాస్‌పోర్ట్ కలిగి, భారత సంతతి వ్యక్తులు
   • ముందు తరాలలో భారత పౌరులు అయినవారు
   • 2015 నుండి PIO కార్డ్ OCI లో విలీనమైంది

3. OCI (Overseas Citizen of India — విదేశీ భారత పౌరుడు):
   • 2005 లో Citizenship (Amendment) Act ద్వారా ప్రవేశపెట్టారు
   • Pakistan, Bangladesh మినహా అన్ని దేశాల్లో ఉన్న భారత సంతతి వారికి
   • జీవితకాల వీసా, అనేక హక్కులు కలిగి ఉంటారు
   • కానీ: ఓటు హక్కు లేదు, ప్రభుత్వ ఉద్యోగాలు లేవు, రాజ్యాంగ పదవులు లేవు

OCI — పూర్తి పౌరసత్వం కాదు:
• OCI = Dual Citizenship కాదు
• OCI కార్డుదారులు భారత పౌరులు కారు"""
    },
    {
        "title": "6.6 పౌరసత్వ సవరణ చట్టం 2019 (CAA)\nCAA 2019 · Citizenship Amendment Act · Religious Minorities · NRC",
        "sub": "CAA 2019 · 6 Religions · 3 Countries · Cut-off Date Dec 31 2014 · NRC",
        "audio": """పౌరసత్వ సవరణ చట్టం 2019 (Citizenship Amendment Act — CAA):

ముఖ్య విషయాలు:
• Parliament ద్వారా డిసెంబర్ 2019 లో ఆమోదించబడింది
• జనవరి 10, 2020 నుండి అమలు

CAA 2019 — ఎవరికి వర్తిస్తుంది?
• దేశాలు: పాకిస్తాన్, అఫ్గానిస్తాన్, బంగ్లాదేశ్ (ముస్లిం మెజారిటీ దేశాలు)
• మతాలు: హిందూ, సిక్కు, బౌద్ధ, జైన, పార్సీ, క్రిస్టియన్ (6 మతాల మైనారిటీలు)
• Cut-off date: డిసెంబర్ 31, 2014 కంటే ముందు వచ్చిన వారికి
• నివాస అర్హత: 11 సంవత్సరాల బదులు 5 సంవత్సరాల నివాసం

CAA ఏమి చేస్తుందంటే:
• పై 3 దేశాల నుండి వచ్చిన మతపరమైన హింసకు గురైన మైనారిటీలకు
• త్వరిత పౌరసత్వ మార్గం కల్పిస్తుంది

NRC (National Register of Citizens):
• Assam NRC 2019 — సంబంధం ఉంది కానీ CAA కి భిన్నమైనది
• CAA = పౌరసత్వ ఇవ్వడం | NRC = పౌరులను గుర్తించడం"""
    },
    {
        "title": "6.7 కామన్‌వెల్త్ పౌరసత్వం మరియు రాజ్యాంగ నిబంధనలు\nCommonwealth Citizenship · Article 8 · Reciprocal Arrangements",
        "sub": "Commonwealth · Article 8 · Reciprocal Rights · Registration Process",
        "audio": """కామన్‌వెల్త్ పౌరసత్వం (Commonwealth Citizenship):

భారత రాజ్యాంగం మరియు కామన్‌వెల్త్:
• India 1947 లో Commonwealth లో చేరింది
• Commonwealth దేశాల పౌరులకు భారతదేశంలో ప్రత్యేక స్థానం

Article 8 — విదేశాల్లో ఉన్న భారత సంతతి వారు:
• విదేశాల్లో ఉన్న భారత సంతతి వ్యక్తులు (Parents/Grandparents భారత పౌరులైన వారు)
• Indian diplomatic mission లో నమోదు చేసుకుంటే పౌరత్వం పొందవచ్చు

కామన్‌వెల్త్ పౌరులకు Registration ద్వారా పౌరత్వం:
• 5 సంవత్సరాల నివాసం తర్వాత (సహజీకరణలో 11 సంవత్సరాలు కాదు)
• Citizenship Act 1955, Section 5 ప్రకారం

రాజ్యాంగ అనుచ్ఛేదాల సారాంశం:
• Article 5  : జనవరి 26, 1950 న భారతదేశంలో నివసించిన వారికి పౌరసత్వం
• Article 6  : పాకిస్తాన్ నుండి వలసవచ్చిన వారికి (July 19, 1948 కట్-ఆఫ్)
• Article 7  : పాకిస్తాన్‌కు వెళ్ళి తిరిగి వచ్చిన వారికి (Permit of Resettlement)
• Article 9  : విదేశ పౌరసత్వం తీసుకుంటే స్వతహాగా రద్దు
• Article 10 : పార్లమెంట్ చట్టం ప్రకారం పౌరసత్వ కొనసాగింపు
• Article 11 : పార్లమెంట్ పౌరసత్వ చట్టం చేసే అధికారం"""
    },
    {
        "title": "6.8 పౌరసత్వం — సమగ్ర విశ్లేషణ (Bilingual)\nCitizenship Act 1955 · Complete Analysis · APPSC Focus",
        "sub": "All 5 Acquisition Methods · All 3 Loss Methods · OCI · CAA 2019 · Key Articles",
        "audio": """Citizenship — Complete Analysis (సమగ్ర విశ్లేషణ):

Constitution Provisions (రాజ్యాంగ నిబంధనలు):
• Part II, Articles 5–11 deal with citizenship
• Article 11: Parliament has power to regulate citizenship by law
• Parliament enacted Citizenship Act, 1955

Citizenship Act 1955 — Acquisition (సంపాదన):
1. By Birth (జన్మ ద్వారా) — Jus Soli principle (initially)
2. By Descent (వంశావళి ద్వారా) — Jus Sanguinis principle
3. By Registration (నమోదు ద్వారా) — 7 years residence
4. By Naturalisation (సహజీకరణ ద్వారా) — 11 years residence
5. By Incorporation of Territory (భూభాగ విలీనం ద్వారా)

Citizenship Act 1955 — Loss (కోల్పోవడం):
1. Renunciation (స్వచ్ఛంద త్యాగం) — Voluntary
2. Termination (సమాప్తి) — Automatic on acquiring foreign citizenship
3. Deprivation (వంచన) — Government action

India = Single Citizenship (ఏకైక పౌరసత్వం):
• Unlike USA which has Dual Citizenship (Federal + State)
• All citizens of India are citizens of India only — not of any State

OCI Card (2005):
• Not full citizenship — No voting rights, No government jobs
• Life-long visa, social/educational rights granted
• Pakistan and Bangladesh nationals ineligible

CAA 2019:
• 6 minority religions from Pakistan, Afghanistan, Bangladesh
• Cut-off: December 31, 2014
• Reduced residence requirement: 5 years (instead of 11)

Key Fact: India does NOT allow Dual Citizenship
(Dual Citizenship = OCI కాదు — OCI is a special status, not citizenship)"""
    },
    {
        "title": "6.9 సినిమాటిక్ కథ — పౌరత్వం కోసం పోరాటం",
        "sub": "Story Section · Citizenship Journey · No MCQs",
        "audio": """కథ: పౌరత్వం కోసం పోరాటం

1947 లో దేశ విభజన జరిగింది. లక్షలాది మంది ప్రజలు పాకిస్తాన్ నుండి భారతదేశానికి వలసవచ్చారు. వారిలో రాజేందర్ కుమార్ అనే ఒక వ్యక్తి కూడా ఉన్నాడు. అతను లాహోర్ నుండి వచ్చి ఢిల్లీలో స్థిరపడ్డాడు.

రాజేందర్ కుమార్‌కు సందేహం వచ్చింది: "నేను ఇప్పుడు భారత పౌరుడినా?" Article 6 సమాధానం ఇచ్చింది — 1948 జూలై 19 కంటే ముందు వచ్చినవారికి స్వయంచాలకంగా పౌరసత్వం ఇవ్వబడింది.

కానీ అతని కొడుకు అమేరికాలో పని చేస్తున్నాడు. అతనికి ప్రశ్న వచ్చింది — "నాకు అమేరికన్ పౌరసత్వం తీసుకుంటే భారత పౌరసత్వం ఏమవుతుంది?" Article 9 సమాధానం: స్వతహాగా (Automatically) భారత పౌరసత్వం రద్దవుతుంది.

అతని మనవడు అమేరికాలో పుట్టాడు, కానీ భారత మూలాలు ఇష్టపడ్డాడు. అతను OCI కార్డు తీసుకున్నాడు. "పూర్తి పౌరత్వం కాకపోయినా, భారత భూమిపై నడవగలను, చదువుకోగలను" అని సంతోషపడ్డాడు.

ఈ మూడు తరాల కథ మనకు నేర్పుతుంది: పౌరత్వం కేవలం చట్టపరమైన హోదా మాత్రమే కాదు — అది ఒక గుర్తింపు, ఒక బాధ్యత, ఒక వారసత్వం.

Article 11 ద్వారా పార్లమెంట్ ఈ సంక్లిష్టమైన సంబంధాలను నియంత్రించే అధికారాన్ని పొందింది. Citizenship Act 1955 ఈ నిబంధనలను స్పష్టంగా నిర్వచించింది."""
    },
]

# ─────────────────────────────────────────────
# MCQ LIST
# Format: (sec_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, expl)
# PYQ:    (sec_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, expl, exam_type)
# ─────────────────────────────────────────────

POLITY_CH6_MCQS = [
    # ── Section 0 : Articles 5–11 Introduction ──────────────────────────────
    (0, 1,
     "రాజ్యాంగంలో పౌరసత్వానికి సంబంధించిన అనుచ్ఛేదాలు ఏ భాగంలో ఉన్నాయి?",
     "Part I", "Part II", "Part III", "Part IV",
     "b",
     "Articles 5–11 రాజ్యాంగంలోని Part II లో ఉన్నాయి. ఇవి రాజ్యాంగ అమలు సమయంలో పౌరసత్వాన్ని నిర్వచిస్తాయి."),

    (0, 1,
     "పౌరసత్వాన్ని పార్లమెంట్ చట్టం ద్వారా నియంత్రించే అధికారాన్ని ఏ అనుచ్ఛేదం ఇస్తుంది?",
     "Article 5", "Article 8", "Article 9", "Article 11",
     "d",
     "Article 11 పార్లమెంట్‌కు పౌరసత్వ సంపాదన మరియు కోల్పోవడాన్ని చట్టం ద్వారా నియంత్రించే అధికారాన్ని ఇస్తుంది. దీని ఆధారంగా Citizenship Act 1955 చేయబడింది."),

    (0, 2,
     "పాకిస్తాన్ నుండి వలసవచ్చిన వారి పౌరసత్వాన్ని ఏ అనుచ్ఛేదం నిర్వచిస్తుంది?",
     "Article 5", "Article 6", "Article 7", "Article 8",
     "b",
     "Article 6 పాకిస్తాన్ నుండి భారతదేశానికి వలసవచ్చిన వారి పౌరసత్వాన్ని నిర్వచిస్తుంది. July 19, 1948 కట్-ఆఫ్ తేదీగా పెట్టారు."),

    (0, 2,
     "స్వచ్ఛందంగా విదేశ పౌరసత్వం తీసుకున్నపుడు భారత పౌరసత్వం అప్రమేయంగా రద్దయ్యే అనుచ్ఛేదం ఏది?",
     "Article 7", "Article 8", "Article 9", "Article 10",
     "c",
     "Article 9 ప్రకారం ఏ వ్యక్తి అయినా స్వచ్ఛందంగా విదేశ పౌరసత్వం తీసుకుంటే అతని/ఆమె భారత పౌరసత్వం స్వతహాగా (Automatically) రద్దవుతుంది."),

    (0, 3,
     "పాకిస్తాన్‌కు వెళ్ళి తిరిగి 'Permit of Resettlement' తో వచ్చిన వారికి పౌరసత్వం కల్పించే అనుచ్ఛేదం?",
     "Article 5", "Article 6", "Article 7", "Article 8",
     "c",
     "Article 7 పాకిస్తాన్‌కు వలసపోయి Permit of Resettlement లేదా Return Permit తో తిరిగి వచ్చిన వారి పౌరసత్వాన్ని నిర్వచిస్తుంది."),

    (0, 3,
     "విదేశాల్లో ఉన్న భారత సంతతి వ్యక్తులు (Grandparents/Parents భారత పౌరులైన వారు) Indian mission లో నమోదు చేసుకుంటే పౌరసత్వం లభించే అనుచ్ఛేదం?",
     "Article 6", "Article 7", "Article 8", "Article 10",
     "c",
     "Article 8 విదేశాల్లో నివసించే భారత సంతతి వ్యక్తులకు సంబంధించినది. వారు Indian Diplomatic Mission లో నమోదు చేసుకుంటే పౌరసత్వం పొందవచ్చు."),

    (0, 4,
     "రాజ్యాంగం Article 10 ప్రకారం ఒక వ్యక్తి పౌరుడిగా కొనసాగడానికి ఏ నిబంధన వర్తిస్తుంది?",
     "రాజ్యపతి ఆమోదం అవసరం",
     "Article 9 ప్రకారం రద్దు కాకూడదు, పార్లమెంట్ చట్టానికి లోబడి ఉండాలి",
     "Supreme Court అనుమతి అవసరం",
     "రాష్ట్ర అసెంబ్లీ ఆమోదం అవసరం",
     "b",
     "Article 10 ప్రకారం ఒక వ్యక్తి Article 9 ద్వారా రద్దు కాకపోతే మరియు పార్లమెంట్ చేసిన పౌరసత్వ చట్టానికి లోబడి ఉంటే పౌరుడిగా కొనసాగుతాడు."),

    # ── Section 1 : Citizenship Act 1955 — Acquisition ──────────────────────
    (1, 1,
     "పౌరసత్వ చట్టం 1955 ప్రకారం పౌరసత్వం సంపాదించడానికి ఎన్ని పద్ధతులు ఉన్నాయి?",
     "3", "4", "5", "6",
     "c",
     "Citizenship Act 1955 ప్రకారం పౌరసత్వం 5 పద్ధతుల్లో సంపాదించవచ్చు: జన్మ, వంశావళి, నమోదు, సహజీకరణ, భూభాగ విలీనం."),

    (1, 1,
     "భారత పౌరసత్వాన్ని నియంత్రించే ప్రధాన చట్టం ఏది?",
     "Citizenship Act 1950", "Citizenship Act 1955", "Citizenship Act 1960", "Citizenship Act 1985",
     "b",
     "Citizenship Act 1955 అనేది Article 11 కింద పార్లమెంట్ చేసిన చట్టం. ఇది పౌరసత్వ సంపాదన మరియు కోల్పోవడాన్ని నియంత్రిస్తుంది."),

    (1, 2,
     "సహజీకరణ (Naturalisation) ద్వారా పౌరసత్వానికి సాధారణంగా ఎన్ని సంవత్సరాల నివాసం అవసరం?",
     "5 సంవత్సరాలు", "7 సంవత్సరాలు", "10 సంవత్సరాలు", "11 సంవత్సరాలు",
     "d",
     "సహజీకరణ ద్వారా పౌరసత్వానికి గత 12 సంవత్సరాలలో కనీసం 11 సంవత్సరాలు భారతదేశంలో నివసించాలి."),

    (1, 2,
     "నమోదు (Registration) ద్వారా పౌరసత్వానికి ఎన్ని సంవత్సరాల నివాసం అవసరం?",
     "5 సంవత్సరాలు", "7 సంవత్సరాలు", "9 సంవత్సరాలు", "11 సంవత్సరాలు",
     "b",
     "Registration పద్ధతిలో 7 సంవత్సరాల నివాసం అవసరం. కానీ Commonwealth దేశాల పౌరులకు 5 సంవత్సరాలు చాలు."),

    (1, 3,
     "Goa పోర్చుగీస్ పాలన నుండి విమోచించబడి భారతదేశంలో విలీనమైన సంవత్సరం?",
     "1954", "1956", "1961", "1975",
     "c",
     "Goa 1961 లో Operation Vijay ద్వారా పోర్చుగీస్ పాలన నుండి విమోచించబడి భారతదేశంలో విలీనమైంది. ఇది 'భూభాగ విలీనం ద్వారా పౌరసత్వం' కి ఉదాహరణ."),

    (1, 3,
     "2003 నాటి Citizenship Amendment Act తర్వాత జన్మ ద్వారా పౌరసత్వానికి ఏ నిబంధన చేర్చబడింది?",
     "తల్లి మాత్రమే భారత పౌరురాలైతే సరిపోతుంది",
     "తండ్రి మాత్రమే భారత పౌరుడైతే సరిపోతుంది",
     "తల్లిదండ్రులిద్దరూ భారత పౌరులైతే మాత్రమే పౌరసత్వం",
     "విదేశాల్లో జన్మించినా తల్లి భారత పౌరురాలైతే చాలు",
     "c",
     "2003 సవరణ తర్వాత, 2004 జనవరి 3 నుండి, భారతదేశంలో జన్మించినవారికి పౌరసత్వానికి తల్లిదండ్రులిద్దరూ భారత పౌరులైతేనే పౌరసత్వం లభిస్తుంది."),

    (1, 4,
     "వంశావళి (By Descent) ద్వారా పౌరసత్వ సంపాదనలో 2003 సవరణ ప్రకారం ఏ మార్పు వచ్చింది?",
     "తల్లి మాత్రమే భారత పౌరురాలైనా పాపకు పౌరసత్వం",
     "తండ్రి స్థానంలో తల్లి పేరు కూడా చేర్చారు",
     "ఇప్పుడు ఈ పద్ధతి పూర్తిగా రద్దు చేయబడింది",
     "విదేశంలో పుట్టిన 18 సంవత్సరాల లోపు పిల్లలకే వర్తిస్తుంది",
     "b",
     "2003 సవరణకు ముందు తండ్రి భారత పౌరుడైతే మాత్రమే వంశావళి ద్వారా పౌరసత్వం. 2003 తర్వాత తల్లి లేదా తండ్రి ఏ ఒక్కరైనా భారత పౌరులైతే చాలు."),

    # ── Section 2 : Loss of Citizenship ────────────────────────────────────
    (2, 1,
     "పౌరసత్వం కోల్పోవడానికి ఎన్ని పద్ధతులు ఉన్నాయి?",
     "2", "3", "4", "5",
     "b",
     "పౌరసత్వం 3 పద్ధతుల్లో కోల్పోవచ్చు: స్వచ్ఛంద త్యాగం (Renunciation), సమాప్తి (Termination), వంచన (Deprivation)."),

    (2, 1,
     "వ్యక్తి స్వయంగా పౌరసత్వాన్ని వదులుకోవడానికి ఏ పద్ధతి అంటారు?",
     "Termination", "Deprivation", "Renunciation", "Cancellation",
     "c",
     "Renunciation (స్వచ్ఛంద త్యాగం) అనేది వ్యక్తి స్వయంగా పౌరసత్వాన్ని వదులుకోవడం. ఇది పూర్తిగా స్వచ్ఛంద చర్య."),

    (2, 2,
     "ప్రభుత్వం పౌరసత్వాన్ని బలవంతంగా రద్దు చేసే పద్ధతి ఏది?",
     "Renunciation", "Termination", "Deprivation", "Cancellation",
     "c",
     "Deprivation (వంచన) అనేది ప్రభుత్వం పౌరసత్వాన్ని బలవంతంగా రద్దు చేయడం. మోసంగా పౌరసత్వం పొందినప్పుడు లేదా రాష్ట్రానికి వ్యతిరేకంగా వ్యవహరించినప్పుడు జరుగుతుంది."),

    (2, 2,
     "Renunciation ద్వారా తల్లి/తండ్రి పౌరసత్వం వదులుకుంటే మైనర్ పిల్లలకు ఏమవుతుంది?",
     "పిల్లలకు పౌరసత్వంపై ప్రభావం ఉండదు",
     "పిల్లలు కూడా పౌరసత్వం కోల్పోతారు, 18 తర్వాత తిరిగి తీసుకోవచ్చు",
     "పిల్లలకు Supreme Court ముందు అప్పీల్ చేయవచ్చు",
     "పిల్లల పౌరసత్వం రాష్ట్ర ప్రభుత్వం నిర్ణయిస్తుంది",
     "b",
     "Renunciation ద్వారా తల్లి/తండ్రి పౌరసత్వం వదులుకుంటే మైనర్ పిల్లలు కూడా పౌరసత్వం కోల్పోతారు. కానీ వారు 18 సంవత్సరాలు నిండిన తర్వాత తిరిగి పొందవచ్చు."),

    (2, 3,
     "Termination మరియు Renunciation మధ్య ప్రధాన తేడా ఏమిటి?",
     "Termination = ప్రభుత్వ చర్య; Renunciation = స్వచ్ఛంద చర్య",
     "Termination = స్వతహాగా రద్దు; Renunciation = స్వచ్ఛంద వదులుకోవడం",
     "Termination = కోర్ట్ ద్వారా; Renunciation = రాష్ట్రపతి ద్వారా",
     "రెండూ ఒకే విషయం — వేర్వేరు పేర్లు మాత్రమే",
     "b",
     "Termination అంటే విదేశ పౌరసత్వం తీసుకున్నప్పుడు స్వతహాగా (Automatically) రద్దు. Renunciation అంటే వ్యక్తి స్వయంగా స్వచ్ఛందంగా వదులుకోవడం."),

    (2, 4,
     "పౌరసత్వ Deprivation ఏ పరిస్థితిలో వర్తించదు?",
     "మోసంగా పౌరసత్వం పొందినప్పుడు",
     "యుద్ధకాలంలో శత్రువుతో సహకరించినప్పుడు",
     "రాష్ట్రానికి వ్యతిరేకంగా వ్యవహరించినప్పుడు",
     "వ్యక్తి మరొక దేశంలో పెట్టుబడి పెట్టినప్పుడు",
     "d",
     "Deprivation మోసంగా పౌరసత్వం పొందడం, యుద్ధకాలంలో శత్రువుతో సహకరించడం, రాజ్యానికి వ్యతిరేకంగా వ్యవహరించడం వంటి పరిస్థితులలో వర్తిస్తుంది. కేవలం విదేశీ పెట్టుబడి కారణంగా వర్తించదు."),

    # ── Section 3 : Single Citizenship ──────────────────────────────────────
    (3, 1,
     "భారత రాజ్యాంగం ఏ రకమైన పౌరసత్వ వ్యవస్థను అనుసరిస్తుంది?",
     "ద్వంద్వ పౌరసత్వం", "ఏకైక పౌరసత్వం", "బహుళ పౌరసత్వం", "రాష్ట్ర పౌరసత్వం",
     "b",
     "భారత రాజ్యాంగం ఏకైక పౌరసత్వం (Single Citizenship) అనుసరిస్తుంది. అందరికీ ఒకే భారత పౌరసత్వం — రాష్ట్ర పౌరసత్వం లేదు."),

    (3, 1,
     "ద్వంద్వ పౌరసత్వం (Dual Citizenship — Federal + State) ఏ దేశంలో ఉంటుంది?",
     "UK", "Canada", "USA", "Australia",
     "c",
     "USA లో Dual Citizenship ఉంటుంది — Federal Citizenship (American) మరియు State Citizenship (Californian, Texan etc.). భారతదేశంలో ఇలా ఉండదు."),

    (3, 2,
     "ఏకైక పౌరసత్వం ప్రధానంగా ఏ ప్రయోజనం కలిగిస్తుంది?",
     "విదేశాల్లో పౌరులకు రక్షణ", "జాతీయ సమైక్యత మరియు సమాన హక్కులు",
     "రాష్ట్రాల స్వాయత్తత", "పన్ను మినహాయింపులు",
     "b",
     "ఏకైక పౌరసత్వం జాతీయ సమైక్యతను (National Integration) కాపాడుతుంది. దేశమంతటా పౌరులకు సమాన హక్కులు లభిస్తాయి — రాష్ట్రాల మధ్య వివక్ష ఉండదు."),

    (3, 2,
     "భారత రాజ్యాంగంలో ఏకైక పౌరసత్వ విధానం ఏ దేశం నుండి స్వీకరించారు?",
     "USA", "Canada", "UK", "France",
     "c",
     "ఏకైక పౌరసత్వం UK (United Kingdom) మోడల్ అనుసరించి స్వీకరించారు. UK లో కూడా ఒక్క స్థాయి పౌరసత్వం మాత్రమే ఉంటుంది."),

    (3, 3,
     "కేవలం పౌరులకు మాత్రమే (Not aliens) లభించే Fundamental Right ఏది?",
     "Article 14 — సమానత్వ హక్కు",
     "Article 21 — జీవించే హక్కు",
     "Article 19 — 6 స్వేచ్ఛలు",
     "Article 32 — రాజ్యాంగ పరిహారాల హక్కు",
     "c",
     "Article 19 కింద 6 రకాల స్వేచ్ఛలు (Freedom of Speech, Assembly, Association etc.) కేవలం పౌరులకు మాత్రమే వర్తిస్తాయి. Article 14, 21, 32 అందరికీ వర్తిస్తాయి."),

    (3, 4,
     "కింది వాటిలో Citizenship కలిగి ఉండటం తప్పనిసరి అయిన రాజ్యాంగ పదవి ఏది?",
     "Supreme Court జడ్జి",
     "Attorney General of India",
     "రాష్ట్రపతి (President of India)",
     "Finance Commission Chairman",
     "c",
     "రాష్ట్రపతి (President of India) పదవికి అభ్యర్థి తప్పనిసరిగా భారత పౌరుడు అయి ఉండాలి (Article 58). ఇది వ్యక్తిగతంగా పౌరసత్వం అవసరమైన ముఖ్యమైన రాజ్యాంగ పదవి."),

    # ── Section 4 : OCI, NRI, PIO (Bilingual) ───────────────────────────────
    (4, 1,
     "OCI కార్డు ఎప్పుడు ప్రవేశపెట్టారు?\nOCI card was introduced in which year?",
     "2000", "2003", "2005", "2010",
     "c",
     "OCI (Overseas Citizen of India) కార్డు 2005 లో Citizenship (Amendment) Act ద్వారా ప్రవేశపెట్టారు.\nOCI card was introduced in 2005 through the Citizenship (Amendment) Act."),

    (4, 1,
     "NRI (Non-Resident Indian) అంటే ఎవరు?\nWho is an NRI?",
     "విదేశ పౌరసత్వం కలిగి భారత సంతతికి చెందిన వ్యక్తి\nA person of Indian origin with foreign citizenship",
     "భారత పౌరసత్వం కలిగి విదేశాల్లో నివసించే వ్యక్తి\nAn Indian citizen residing abroad",
     "OCI కార్డు కలిగిన వ్యక్తి\nA person holding OCI card",
     "పాకిస్తాన్ నుండి వలసవచ్చిన వ్యక్తి\nA person who migrated from Pakistan",
     "b",
     "NRI అంటే భారత పౌరసత్వం కలిగి విదేశాల్లో నివసించే వ్యక్తి. వారికి భారత పాస్‌పోర్ట్ ఉంటుంది మరియు పూర్తి పౌరసత్వ హక్కులు ఉంటాయి.\nNRI is an Indian citizen living abroad with an Indian passport and full citizenship rights."),

    (4, 2,
     "OCI కార్డుదారులకు ఏ హక్కు ఉండదు?\nWhich right is NOT available to OCI card holders?",
     "జీవితకాల వీసా / Life-long visa",
     "విద్య మరియు సామాజిక హక్కులు / Educational and social rights",
     "ఓటు హక్కు / Voting rights",
     "భారతదేశంలో ప్రయాణించే హక్కు / Right to travel to India",
     "c",
     "OCI కార్డుదారులకు జీవితకాల వీసా, విద్య/సామాజిక హక్కులు ఉంటాయి కానీ ఓటు హక్కు, ప్రభుత్వ ఉద్యోగాలు, రాజ్యాంగ పదవులు ఉండవు.\nOCI holders have life-long visa but no voting rights, government jobs, or constitutional posts."),

    (4, 2,
     "2015 తర్వాత PIO కార్డుకు ఏమైంది?\nWhat happened to PIO card after 2015?",
     "PIO కార్డు రద్దు చేయబడింది / PIO card was cancelled",
     "PIO కార్డు OCI కార్డులో విలీనమైంది / PIO card was merged with OCI card",
     "PIO కార్డు NRI కార్డుగా మారింది / PIO card became NRI card",
     "PIO కార్డు కొనసాగింది — ఎటువంటి మార్పు లేదు / PIO card continued unchanged",
     "b",
     "2015 లో PIO (Person of Indian Origin) కార్డు OCI కార్డులో విలీనమైంది. పాత PIO కార్డులు OCI కార్డులుగా మారాయి.\nIn 2015, PIO card was merged into OCI card scheme."),

    (4, 3,
     "OCI కార్డుకు అర్హత లేని దేశాల పౌరులు ఎవరు?\nCitizens of which countries are NOT eligible for OCI card?",
     "USA మరియు UK పౌరులు / Citizens of USA and UK",
     "పాకిస్తాన్ మరియు బంగ్లాదేశ్ పౌరులు / Citizens of Pakistan and Bangladesh",
     "China మరియు Russia పౌరులు / Citizens of China and Russia",
     "Canada మరియు Australia పౌరులు / Citizens of Canada and Australia",
     "b",
     "పాకిస్తాన్ మరియు బంగ్లాదేశ్ దేశాల పౌరులు OCI కార్డుకు అర్హులు కారు. భారత సంతతికి చెందినవారు అయినా ఈ రెండు దేశాల పౌరులకు OCI కార్డు ఇవ్వరు.\nCitizens of Pakistan and Bangladesh are ineligible for OCI card even if of Indian origin."),

    (4, 4,
     "OCI, NRI, PIO గురించి సరైన వాక్యం ఏది?\nWhich statement about OCI, NRI, PIO is CORRECT?",
     "OCI = పూర్తి Dual Citizenship / OCI = Full Dual Citizenship",
     "NRI కి భారత పాస్‌పోర్ట్ ఉండదు / NRI does not have Indian passport",
     "OCI పూర్తి పౌరసత్వం కాదు — ఒక ప్రత్యేక హోదా మాత్రమే / OCI is not full citizenship — just a special status",
     "PIO 2015 తర్వాత కూడా ప్రత్యేకంగా కొనసాగింది / PIO continued separately after 2015",
     "c",
     "OCI పూర్తి పౌరసత్వం (Dual Citizenship) కాదు — ఇది ఒక ప్రత్యేక హోదా మాత్రమే. OCI కార్డుదారులకు ఓటు హక్కు మరియు ప్రభుత్వ ఉద్యోగాలు ఉండవు.\nOCI is not dual citizenship — it is a special status without voting rights or government jobs."),

    # ── Section 5 : CAA 2019 (Bilingual) ────────────────────────────────────
    (5, 1,
     "పౌరసత్వ సవరణ చట్టం 2019 (CAA) ఏ సంవత్సరంలో పార్లమెంట్ ఆమోదించింది?\nIn which year was CAA passed by Parliament?",
     "2018", "2019", "2020", "2021",
     "b",
     "పౌరసత్వ సవరణ చట్టం 2019 డిసెంబర్ 2019 లో పార్లమెంట్ ఆమోదించింది మరియు జనవరి 10, 2020 నుండి అమలులోకి వచ్చింది.\nCAA was passed by Parliament in December 2019 and came into force on January 10, 2020."),

    (5, 1,
     "CAA 2019 ప్రకారం ఏ 3 దేశాల మైనారిటీలకు ప్రయోజనం కలుగుతుంది?\nCAA 2019 benefits minorities from which 3 countries?",
     "Afghanistan, Bangladesh, Myanmar",
     "Pakistan, Bangladesh, Afghanistan",
     "Pakistan, Myanmar, Sri Lanka",
     "Bangladesh, Nepal, Afghanistan",
     "b",
     "CAA 2019 పాకిస్తాన్, బంగ్లాదేశ్, అఫ్గానిస్తాన్ — ముస్లిం మెజారిటీ 3 దేశాల నుండి వచ్చిన మతపరమైన మైనారిటీలకు వర్తిస్తుంది.\nCAA 2019 benefits religious minorities from Pakistan, Bangladesh, and Afghanistan."),

    (5, 2,
     "CAA 2019 ప్రకారం ఏ 6 మతాలకు చెందిన మైనారిటీలకు ప్రయోజనం కలుగుతుంది?\nCAA 2019 covers minorities of which 6 religions?",
     "హిందూ, ముస్లిం, సిక్కు, బౌద్ధ, జైన, పార్సీ",
     "హిందూ, సిక్కు, బౌద్ధ, జైన, పార్సీ, క్రిస్టియన్",
     "హిందూ, సిక్కు, బౌద్ధ, జైన, పార్సీ, యూదు",
     "హిందూ, ముస్లిం, సిక్కు, బౌద్ధ, క్రిస్టియన్, పార్సీ",
     "b",
     "CAA 2019 హిందూ, సిక్కు, బౌద్ధ, జైన, పార్సీ మరియు క్రిస్టియన్ — 6 మతాల మైనారిటీలకు వర్తిస్తుంది. ముస్లింలు ఈ జాబితాలో లేరు.\nCAA covers Hindu, Sikh, Buddhist, Jain, Parsi, and Christian minorities — not Muslims."),

    (5, 2,
     "CAA 2019 ప్రకారం నివాస అర్హత ఎన్ని సంవత్సరాలకు తగ్గించారు?\nCAA 2019 reduced residence requirement to how many years?",
     "3 సంవత్సరాలు / 3 years", "5 సంవత్సరాలు / 5 years",
     "7 సంవత్సరాలు / 7 years", "9 సంవత్సరాలు / 9 years",
     "b",
     "CAA 2019 సాధారణ 11 సంవత్సరాల బదులు 5 సంవత్సరాల నివాస అర్హతను నిర్ణయించింది.\nCAA 2019 reduced the residence requirement from 11 years to 5 years for eligible refugees."),

    (5, 3,
     "CAA 2019 లో Cut-off date ఏది?\nWhat is the cut-off date in CAA 2019?",
     "December 31, 2013",
     "December 31, 2014",
     "December 31, 2015",
     "January 26, 2015",
     "b",
     "CAA 2019 కింద ప్రయోజనానికి అర్హత పొందడానికి డిసెంబర్ 31, 2014 కంటే ముందు భారతదేశంలోకి రావాలి.\nThe cut-off date for CAA 2019 is December 31, 2014."),

    (5, 3,
     "CAA మరియు NRC మధ్య సంబంధం గురించి సరైన వాక్యం ఏది?\nWhich statement correctly distinguishes CAA from NRC?",
     "CAA మరియు NRC ఒకే విషయం / CAA and NRC are the same",
     "CAA = పౌరసత్వం ఇవ్వడం; NRC = పౌరులను గుర్తించడం / CAA gives citizenship; NRC identifies citizens",
     "NRC CAA లో భాగం / NRC is part of CAA",
     "CAA రద్దు అయిన తర్వాత NRC వర్తిస్తుంది / NRC applies after CAA is revoked",
     "b",
     "CAA = పౌరసత్వాన్ని ఇవ్వడం (నిర్దిష్ట మైనారిటీలకు). NRC = పౌరులను గుర్తించే జాతీయ రిజిస్టర్. రెండూ వేర్వేరు విషయాలు.\nCAA grants citizenship to specific refugees; NRC identifies existing citizens — they are separate processes."),

    (5, 4,
     "CAA 2019 ని రాజ్యాంగం ప్రకారం సవాలు చేయడానికి ఆధారంగా ఉపయోగించగలిగే అనుచ్ఛేదం?\nWhich constitutional article could be used to challenge CAA 2019?",
     "Article 14 — సమానత్వ హక్కు / Right to Equality",
     "Article 19 — స్వేచ్ఛలు / Freedoms",
     "Article 32 — రాజ్యాంగ పరిహారాలు / Constitutional Remedies",
     "Article 25 — మత స్వాతంత్ర్యం / Religious Freedom",
     "a",
     "CAA 2019 ని Article 14 (సమానత్వ హక్కు) ఉల్లంఘనగా సవాలు చేయవచ్చు — ఎందుకంటే ఇది మతం ఆధారంగా వర్గీకరిస్తుంది. Supreme Court లో ఈ విషయంపై పిటిషన్లు దాఖలు అయ్యాయి.\nCAA 2019 can be challenged under Article 14 (Right to Equality) as it classifies based on religion."),

    # ── Section 6 : Commonwealth Citizenship & Articles ─────────────────────
    (6, 1,
     "Citizenship Act 1955 ఏ Article కింద చేయబడింది?",
     "Article 5", "Article 9", "Article 10", "Article 11",
     "d",
     "Citizenship Act 1955 Article 11 కింద పార్లమెంట్ చేసిన చట్టం. Article 11 పార్లమెంట్‌కు పౌరసత్వాన్ని చట్టం ద్వారా నియంత్రించే అధికారాన్ని ఇస్తుంది."),

    (6, 1,
     "Commonwealth దేశాల పౌరులకు Registration ద్వారా పౌరసత్వానికి ఎన్ని సంవత్సరాల నివాసం అవసరం?",
     "3 సంవత్సరాలు", "5 సంవత్సరాలు", "7 సంవత్సరాలు", "11 సంవత్సరాలు",
     "b",
     "Commonwealth దేశాల పౌరులకు Registration ద్వారా పౌరసత్వానికి 5 సంవత్సరాల నివాసం అవసరం. సాధారణ Registration కి 7 సంవత్సరాలు."),

    (6, 2,
     "Article 5 ప్రకారం రాజ్యాంగ అమలు (Commencement) తేదీ ఏది?",
     "August 15, 1947", "November 26, 1949", "January 26, 1950", "January 26, 1952",
     "c",
     "Article 5 ప్రకారం రాజ్యాంగ అమలు (Commencement) తేదీ జనవరి 26, 1950. ఆ తేదీన భారతదేశంలో నివసిస్తున్న మరియు అర్హులైన వారికి పౌరసత్వం ఇవ్వబడింది."),

    (6, 2,
     "Article 6 ప్రకారం పాకిస్తాన్ నుండి వచ్చిన వారికి పౌరసత్వం పొందడానికి ఏ కట్-ఆఫ్ తేదీ ఉంది?",
     "August 15, 1947", "July 19, 1948", "January 26, 1949", "January 26, 1950",
     "b",
     "Article 6 ప్రకారం July 19, 1948 పాకిస్తాన్ నుండి వలసలకు కట్-ఆఫ్ తేదీ. ఈ తేదీ ముందు వచ్చిన వారికి స్వతహాగా, తర్వాత వచ్చిన వారికి నమోదు ద్వారా పౌరసత్వం."),

    (6, 3,
     "India Commonwealth లో చేరిన సంవత్సరం?",
     "1945", "1947", "1950", "1952",
     "b",
     "భారతదేశం 1947 లో స్వాతంత్ర్యం పొందిన తర్వాత Commonwealth లో చేరింది. India Republic అయిన తర్వాత కూడా Commonwealth లో కొనసాగింది."),

    (6, 4,
     "Article 8 కింద విదేశాల్లో ఉన్న భారత సంతతి వ్యక్తులు నమోదు చేసుకోవాల్సిన చోటు?",
     "భారత రాష్ట్రాల ముఖ్యమంత్రి కార్యాలయంలో",
     "భారత Indian Diplomatic Mission లో",
     "Supreme Court లో",
     "Union Home Ministry లో",
     "b",
     "Article 8 ప్రకారం విదేశాల్లో ఉన్న భారత సంతతి వ్యక్తులు Indian Diplomatic Mission (Embassy/Consulate) లో నమోదు చేసుకుంటే పౌరసత్వం పొందవచ్చు."),

    # ── Section 7 : Comprehensive Analysis (Bilingual) ──────────────────────
    (7, 1,
     "భారత రాజ్యాంగంలో పౌరసత్వానికి సంబంధించిన Articles ఏ సంఖ్యల వరకు ఉన్నాయి?\nCitizenship articles in Indian Constitution span which range?",
     "Articles 1–5", "Articles 5–11", "Articles 12–35", "Articles 36–51",
     "b",
     "రాజ్యాంగంలో Part II, Articles 5–11 పౌరసత్వానికి సంబంధించినవి. ఇవి రాజ్యాంగ అమలు సమయంలో తాత్కాలిక నిబంధనలు.\nArticles 5–11 in Part II deal with citizenship at commencement of the Constitution.",
     "APPSC"),

    (7, 1,
     "కింది వాటిలో పౌరసత్వ సంపాదన పద్ధతి కానిది ఏది?\nWhich of the following is NOT a method of acquiring citizenship?",
     "By Birth / జన్మ ద్వారా",
     "By Naturalisation / సహజీకరణ ద్వారా",
     "By Employment / ఉద్యోగం ద్వారా",
     "By Registration / నమోదు ద్వారా",
     "c",
     "పౌరసత్వ సంపాదన 5 పద్ధతులు: జన్మ, వంశావళి, నమోదు, సహజీకరణ, భూభాగ విలీనం. 'ఉద్యోగం ద్వారా' అనేది పద్ధతి కాదు.\n5 methods of acquiring citizenship: Birth, Descent, Registration, Naturalisation, Territory incorporation — Employment is NOT one.",
     "APPSC"),

    (7, 2,
     "OCI కార్డు మరియు Dual Citizenship గురించి సరైన వాక్యం ఏది?\nWhich statement about OCI and Dual Citizenship is CORRECT?",
     "OCI = Dual Citizenship / OCI అంటే రెండు దేశాల పౌరసత్వం",
     "India Dual Citizenship అనుమతిస్తుంది / India allows Dual Citizenship",
     "OCI పూర్తి పౌరసత్వం కాదు — ప్రత్యేక హోదా మాత్రమే / OCI is not citizenship — it is a special status",
     "NRI లకు OCI తో పాటు Dual Citizenship ఉంటుంది / NRI have Dual Citizenship along with OCI",
     "c",
     "OCI పూర్తి పౌరసత్వం (Dual Citizenship) కాదు. భారతదేశం Dual Citizenship అనుమతించదు. OCI ఒక ప్రత్యేక హోదా — ఓటు హక్కు, ప్రభుత్వ ఉద్యోగాలు ఉండవు.\nOCI is not dual citizenship — India doesn't allow dual citizenship. OCI is a special status without voting rights.",
     "UPSC"),

    (7, 2,
     "CAA 2019 ప్రకారం ఏ మతానికి చెందిన వ్యక్తులు ఆ 3 దేశాల నుండి వచ్చినా CAA కింద అర్హులు కారు?\nMembers of which religion from those 3 countries are NOT covered under CAA 2019?",
     "హిందువులు / Hindus", "బౌద్ధులు / Buddhists",
     "ముస్లింలు / Muslims", "పార్సీలు / Parsis",
     "c",
     "CAA 2019 హిందూ, సిక్కు, బౌద్ధ, జైన, పార్సీ, క్రిస్టియన్ మైనారిటీలకు వర్తిస్తుంది. పాకిస్తాన్, బంగ్లాదేశ్, అఫ్గానిస్తాన్ నుండి వచ్చిన ముస్లింలు CAA కింద అర్హులు కారు.\nMuslims from those 3 countries are not covered under CAA 2019. It covers 6 non-Muslim minority religions.",
     "UPSC"),

    (7, 3,
     "Single Citizenship మరియు Dual Citizenship మధ్య తేడా గురించి సరైన వాక్యం ఏది?\nWhich statement correctly distinguishes Single from Dual Citizenship?",
     "Single Citizenship = 2 స్థాయిలు; Dual Citizenship = 1 స్థాయి",
     "India = Single; USA = Dual (Federal + State Level)",
     "India = Dual; USA = Single",
     "రెండు దేశాలలో Single Citizenship వ్యవస్థ ఉంది",
     "b",
     "India = Single Citizenship (ఒక్క స్థాయి మాత్రమే). USA = Dual Citizenship (Federal American + State — Californian/Texan etc.). UK మోడల్ అనుసరించి India Single Citizenship అవలంబించింది.\nIndia follows Single Citizenship (UK model); USA has Dual Citizenship at Federal and State levels.",
     "APPSC"),

    (7, 4,
     "పౌరసత్వం కోల్పోవడం — సరైన జత ఏది?\nWhich is the CORRECT match for modes of losing citizenship?",
     "Renunciation = Automatic; Termination = Voluntary; Deprivation = Court order",
     "Renunciation = Voluntary; Termination = Automatic; Deprivation = Government action",
     "Renunciation = Government action; Termination = Voluntary; Deprivation = Automatic",
     "Renunciation = Court order; Termination = Automatic; Deprivation = Voluntary",
     "b",
     "Renunciation = స్వచ్ఛంద (Voluntary); Termination = స్వతహాగా రద్దు (Automatic — విదేశ పౌరసత్వం తీసుకున్నపుడు); Deprivation = ప్రభుత్వ చర్య (Government action).\nRenunciation=Voluntary; Termination=Automatic (on acquiring foreign citizenship); Deprivation=Government action.",
     "UPSC"),
]

# ─────────────────────────────────────────────
# SEED FUNCTIONS
# ─────────────────────────────────────────────

def _seed_polity_ch6_notes_inner(db, chapter_id: int):
    """Insert study-note sections for Chapter 6 (Citizenship)."""
    for idx, sec in enumerate(POLITY_CH6_SECTIONS):
        existing = db.execute(
            "SELECT id FROM study_notes WHERE chapter_id=? AND section_index=?",
            (chapter_id, idx)
        ).fetchone()
        if not existing:
            db.execute(
                "INSERT INTO study_notes (chapter_id, section_index, title, subtitle, audio_text) "
                "VALUES (?,?,?,?,?)",
                (chapter_id, idx, sec["title"], sec["sub"], sec["audio"])
            )
    db.commit()


def _seed_polity_ch6_mcqs_inner(db, chapter_id: int):
    """Insert MCQs for Chapter 6 (Citizenship)."""
    for row in POLITY_CH6_MCQS:
        sec_idx, diff = row[0], row[1]
        q, a, b, c, d = row[2], row[3], row[4], row[5], row[6]
        correct, expl = row[7], row[8]
        exam_type = row[9] if len(row) > 9 else None

        existing = db.execute(
            "SELECT id FROM chapter_mcqs WHERE chapter_id=? AND question=?",
            (chapter_id, q)
        ).fetchone()
        if not existing:
            db.execute(
                "INSERT INTO chapter_mcqs "
                "(chapter_id, section_index, difficulty, question, "
                " option_a, option_b, option_c, option_d, correct_answer, explanation, exam_type) "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (chapter_id, sec_idx, diff, q, a, b, c, d, correct, expl, exam_type)
            )
    db.commit()
