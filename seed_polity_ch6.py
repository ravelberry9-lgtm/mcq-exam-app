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
    # ───── Section 0: Constitutional Articles 5-11 ─────
    (0, 1,
     "In which Part of the Constitution are Articles relating to Citizenship found?\nతెలుగు: పౌరసత్వ Articles ఏ Part?",
     "Part I", "Part II (correct)", "Part III", "Part IV",
     "b",
     "Articles 5–11 are in PART II of the Constitution. These define citizenship at COMMENCEMENT of the Constitution (26 Jan 1950) and are TEMPORARY provisions. Article 11 empowers Parliament to make permanent citizenship law (→ Citizenship Act 1955)."),

    (0, 1,
     "Which Article empowers Parliament to regulate citizenship by law?\nతెలుగు: పార్లమెంట్ చట్టం ద్వారా నియంత్రించే Article?",
     "Article 5", "Article 8", "Article 9", "Article 11 (correct)",
     "d",
     "Article 11: Parliament has power to make any provision regarding ACQUISITION and TERMINATION of citizenship by law. Citizenship Act 1955 was enacted under this power."),

    (0, 2,
     "Which Article defines citizenship of those who migrated from Pakistan?\nతెలుగు: పాకిస్తాన్ నుండి వలస Article?",
     "Article 5", "Article 6 (correct)", "Article 7", "Article 8",
     "b",
     "Article 6: Citizenship for persons MIGRATED FROM PAKISTAN to India. Cut-off: 19 July 1948 — those entered before this date got automatic citizenship; those entering after had to register. Reflects post-Partition population movements."),

    (0, 2,
     "Under which Article does Indian citizenship lapse automatically on voluntary acquisition of foreign citizenship?\nతెలుగు: విదేశ పౌరసత్వం తీసుకుంటే రద్దు Article?",
     "Article 7", "Article 8", "Article 9 (correct)", "Article 10",
     "c",
     "Article 9: If a person VOLUNTARILY acquires citizenship of any foreign State, that person SHALL NOT be a citizen of India by virtue of Article 5 or be deemed a citizen of India under Articles 6 or 8. India does NOT permit dual citizenship — automatic termination."),

    (0, 3,
     "Which Article covers persons who returned from Pakistan with Permit of Resettlement?\nతెలుగు: Permit of Resettlement Article?",
     "Article 5", "Article 6", "Article 7 (correct)", "Article 8",
     "c",
     "Article 7: Citizenship for persons who MIGRATED TO PAKISTAN after 1 March 1947 and SUBSEQUENTLY RETURNED to India under a 'Permit of Resettlement' or Return Permit. They could be registered as citizens after at least 6 months residence."),

    (0, 3,
     "Indians abroad whose grandparents/parents were Indian citizens — citizenship article?\nతెలుగు: విదేశీ భారతీయులు Article?",
     "Article 6", "Article 7", "Article 8 (correct)", "Article 10",
     "c",
     "Article 8: Persons of Indian origin residing OUTSIDE INDIA — if they or any of their parents/grandparents were born in undivided India — can be registered as Indian citizens by Indian Diplomatic Mission in country of residence."),

    (0, 4,
     "Under Article 10, what condition applies for continuing as citizen?\nతెలుగు: Article 10 ఏం?",
     "Presidential approval needed",
     "Subject to Article 9 not extinguishing and Parliament's law / Article 9 + Parliament చట్టం (correct)",
     "Supreme Court permission needed",
     "State Assembly approval needed",
     "b",
     "Article 10: Every person who is or is deemed to be a citizen of India under Part II shall, SUBJECT TO PROVISIONS of any law made by Parliament, CONTINUE TO BE such citizen. Citizenship continuance is conditional on Parliament's law (currently Citizenship Act 1955)."),

    # ───── Section 1: Citizenship Act 1955 ─────
    (1, 1,
     "How many modes of acquiring citizenship under Citizenship Act 1955?\nతెలుగు: సంపాదన పద్ధతులు ఎన్ని?",
     "3", "4", "5 (correct)", "6",
     "c",
     "5 modes under Citizenship Act 1955: (1) BIRTH, (2) DESCENT, (3) REGISTRATION, (4) NATURALISATION, (5) INCORPORATION OF TERRITORY (e.g., Goa, Sikkim, Pondicherry)."),

    (1, 1,
     "Primary statute regulating Indian citizenship?\nతెలుగు: ప్రధాన పౌరసత్వ చట్టం?",
     "Citizenship Act 1950", "Citizenship Act 1955 (correct)",
     "Citizenship Act 1960", "Citizenship Act 1985",
     "b",
     "CITIZENSHIP ACT 1955 — enacted under Art.11. Has been amended multiple times: 1986, 1992, 2003, 2005, 2015, 2019. Regulates acquisition, termination, deprivation, and renunciation of Indian citizenship."),

    (1, 2,
     "Years of residence required for Naturalisation?\nతెలుగు: Naturalisation సం.?",
     "5 years", "7 years", "10 years", "11 years (correct)",
     "d",
     "NATURALISATION: Aggregate residence of at least 11 YEARS in India during preceding 14 years AND continuous residence for 12 months immediately before application. Plus other conditions (good character, knowledge of an Indian language, intention to reside in India)."),

    (1, 2,
     "Years of residence required for Registration (general)?\nతెలుగు: Registration సం.?",
     "5 years", "7 years (correct)", "9 years", "11 years",
     "b",
     "REGISTRATION (general persons of Indian origin): 7 YEARS of residence in India before application. For Commonwealth/Ireland citizens: 5 YEARS. For PIO married to Indian citizen and resident: 7 years."),

    (1, 3,
     "Year Goa was incorporated as Indian territory?\nతెలుగు: Goa విలీనం?",
     "1954", "1956", "1961 (correct)", "1975",
     "c",
     "GOA was liberated from Portuguese rule and incorporated into Indian territory in DECEMBER 1961 (Operation Vijay). Citizenship by INCORPORATION OF TERRITORY — Goans deemed Indian citizens. Sikkim was added in 1975 under similar mode."),

    (1, 3,
     "After 2003 amendment, citizenship by birth requires?\nతెలుగు: 2003 సవరణ తర్వాత birth?",
     "Mother alone Indian citizen suffices",
     "Father alone Indian citizen suffices",
     "BOTH parents Indian citizens (or one Indian + other not illegal migrant) / తల్లిదండ్రులు ఇద్దరూ (correct)",
     "Mother Indian abroad suffices",
     "c",
     "After 2003 Citizenship Amendment (effective 3 December 2004): BIRTH IN INDIA gives citizenship only if (a) BOTH parents are Indian citizens, OR (b) one parent Indian and other NOT an illegal migrant. Earlier (1987-2004) needed at least one parent Indian; pre-1987 birth in India alone sufficed."),

    (1, 4,
     "Change in citizenship by Descent in 2003 amendment?\nతెలుగు: Descent 2003 మార్పు?",
     "Mother alone passes citizenship if abroad",
     "Father OR mother (either) Indian suffices for descent / తండ్రి లేదా తల్లి (correct)",
     "Descent route fully abolished",
     "Only minors eligible",
     "b",
     "Pre-2003: Descent required FATHER to be Indian citizen at child's birth abroad. POST-2003: Either FATHER OR MOTHER being Indian citizen suffices. Gender equality reform — also requires registration at Indian Mission for child born abroad after 3 December 2004."),

    # ───── Section 2: Loss of Citizenship ─────
    (2, 1,
     "How many modes of losing citizenship?\nతెలుగు: కోల్పోవడ పద్ధతులు?",
     "2", "3 (correct)", "4", "5",
     "b",
     "3 MODES of losing citizenship under Citizenship Act 1955: (1) RENUNCIATION (voluntary), (2) TERMINATION (automatic on acquiring foreign citizenship), (3) DEPRIVATION (compulsory by govt for fraud, disloyalty, etc.)."),

    (2, 1,
     "Voluntary giving up of citizenship by oneself is called?\nతెలుగు: స్వచ్ఛంద త్యాగం?",
     "Termination", "Deprivation", "Renunciation (correct)", "Cancellation",
     "c",
     "RENUNCIATION (Voluntary): Citizen of full age and capacity may make a declaration renouncing Indian citizenship. On registration of declaration, person ceases to be Indian citizen. Minor children of such person also lose citizenship — but can resume on reaching 18 (within 1 year)."),

    (2, 2,
     "Compulsory cancellation by government is which mode?\nతెలుగు: ప్రభుత్వం బలవంతంగా?",
     "Renunciation", "Termination", "Deprivation (correct)", "Cancellation",
     "c",
     "DEPRIVATION (Compulsory): Government can deprive a NATURALISED or REGISTERED citizen of Indian citizenship on grounds: (a) fraud/concealment in obtaining citizenship; (b) disloyalty to Constitution; (c) trading with enemy in war; (d) imprisoned in any country for 2+ years within 5 years of registration; (e) ordinarily resident outside India for 7 years continuously."),

    (2, 2,
     "Effect on minor children when parent renounces citizenship?\nతెలుగు: Renunciation పిల్లలు?",
     "No effect on children",
     "Children also lose citizenship; can resume after 18 / పిల్లలు కోల్పోతారు, 18 తర్వాత తిరిగి (correct)",
     "Can appeal to SC", "State govt decides",
     "b",
     "When a person RENOUNCES Indian citizenship, EVERY MINOR CHILD of that person also CEASES to be a citizen. However, on attaining 18 years of age, such child may RESUME Indian citizenship by making declaration within 1 year."),

    (2, 3,
     "Key difference between Termination and Renunciation?\nతెలుగు: Termination vs Renunciation?",
     "Termination = govt action; Renunciation = voluntary",
     "Termination = automatic on foreign citizenship; Renunciation = voluntary giving up / Termination = automatic; Renunciation = voluntary (correct)",
     "Termination = court; Renunciation = President", "Both same",
     "b",
     "TERMINATION = AUTOMATIC loss when Indian citizen voluntarily acquires citizenship of another country (under Section 9 of Citizenship Act, mirroring Art.9). NO declaration needed. RENUNCIATION = VOLUNTARY giving up by formal declaration to the government."),

    (2, 4,
     "Which situation does NOT attract Deprivation?\nతెలుగు: Deprivation వర్తించని పరిస్థితి?",
     "Fraud in obtaining citizenship",
     "Trading with enemy during war",
     "Disloyalty to State",
     "Foreign investment by person / విదేశీ పెట్టుబడి (correct)",
     "d",
     "Deprivation grounds (Section 10): (a) FRAUD, (b) DISLOYALTY to Constitution, (c) TRADING WITH ENEMY in war, (d) imprisonment for 2+ years within 5 years of registration, (e) continuous residence abroad for 7 years. MERE FOREIGN INVESTMENT does not trigger deprivation."),

    # ───── Section 3: Single Citizenship & Federal Comparison ─────
    (3, 1,
     "What citizenship system does India follow?\nతెలుగు: భారత్ ఏ వ్యవస్థ?",
     "Dual / ద్వంద్వ", "Single / ఏకైక (correct)",
     "Multiple", "State citizenship",
     "b",
     "India follows SINGLE CITIZENSHIP. Every Indian is a citizen of INDIA — there is no separate state citizenship. This is unlike USA where dual citizenship (federal + state) operates. Aims at NATIONAL UNITY despite federal structure."),

    (3, 1,
     "Which country has Dual Citizenship (Federal + State)?\nతెలుగు: Dual Citizenship ఏ దేశం?",
     "UK", "Canada", "USA (correct)", "Australia",
     "c",
     "USA has DUAL CITIZENSHIP — every American is citizen of (1) United States (federal) AND (2) the state of residence (Californian, Texan, etc.). Each state can have separate citizenship privileges. India's Constitution-makers REJECTED this model to strengthen unity."),

    (3, 2,
     "What does Single Citizenship primarily achieve?\nతెలుగు: ఏకైక పౌరసత్వం ఉద్దేశం?",
     "Protection of citizens abroad",
     "National integration and equal rights / జాతీయ సమైక్యత + సమాన హక్కులు (correct)",
     "State autonomy", "Tax exemptions",
     "b",
     "Single Citizenship promotes NATIONAL INTEGRATION — equal rights for Indians across all states. Prevents inter-state discrimination. Citizens can move freely across India and enjoy same fundamental rights everywhere. Rejects loyalty competition between centre and states."),

    (3, 2,
     "Single Citizenship was adopted from which country's model?\nతెలుగు: ఏ దేశం నుండి?",
     "USA", "Canada", "UK / యూకే (correct)", "France",
     "c",
     "Single Citizenship borrowed from BRITISH (UK) MODEL. Like UK, India has only ONE level of citizenship. Unlike USA which has dual citizenship structure inherited from its origin as confederation of independent states. Constituent Assembly chose UK model for unity."),

    (3, 3,
     "Which Fundamental Right is available ONLY to citizens (not aliens)?\nతెలుగు: కేవలం పౌరులకే?",
     "Article 14 (Equality)", "Article 21 (Life and Liberty)",
     "Article 19 (Six Freedoms) (correct)", "Article 32 (Constitutional Remedies)",
     "c",
     "ARTICLE 19 (six freedoms — speech, assembly, association, movement, residence, profession) is available ONLY to CITIZENS. Articles 14, 21, 25, 32 are available to ALL persons (citizens + aliens). Other citizen-only rights: Art.15, 16, 29, 30 (some specific protections)."),

    (3, 4,
     "Which constitutional post REQUIRES the holder to be an Indian citizen?\nతెలుగు: పౌరసత్వం తప్పనిసరి పదవి?",
     "Supreme Court Judge", "Attorney General",
     "President of India / రాష్ట్రపతి (correct)", "Finance Commission Chairman",
     "c",
     "Article 58: PRESIDENT must be a CITIZEN OF INDIA (and 35+ years, eligible for LS membership). Similarly: Vice-President (Art.66), Governor (Art.157), Judges of SC/HC, MPs/MLAs, Attorney General — all require Indian citizenship."),

    # ───── Section 4: NRI / OCI / PIO ─────
    (4, 1,
     "When was OCI card introduced?\nతెలుగు: OCI ఎప్పుడు?",
     "2000", "2003", "2005 (correct)", "2010",
     "c",
     "OCI (Overseas Citizen of India) card was introduced in AUGUST 2005 through the CITIZENSHIP (AMENDMENT) ACT 2005. Misleadingly named — it is NOT citizenship, only a special status with lifelong visa and certain rights but no voting rights or government jobs."),

    (4, 1,
     "Who is an NRI (Non-Resident Indian)?\nతెలుగు: NRI ఎవరు?",
     "Person of Indian origin with foreign citizenship",
     "Indian citizen residing abroad / భారత పౌరసత్వం + విదేశంలో నివాసం (correct)",
     "OCI card holder", "Migrant from Pakistan",
     "b",
     "NRI = Indian CITIZEN residing ABROAD (for employment/business/education). Holds Indian passport, has full citizenship rights including VOTE (since 2010 amendment by being physically present at constituency on poll day). Tax-defined under Income Tax Act based on days of stay."),

    (4, 2,
     "Which right is NOT available to OCI card holders?\nతెలుగు: OCI కి లేని హక్కు?",
     "Life-long visa / జీవిత visa",
     "Educational and social rights / విద్య + సామాజిక",
     "Voting rights / ఓటు హక్కు (correct)",
     "Right to travel to India / ప్రయాణ హక్కు",
     "c",
     "OCI card holders DO NOT GET: (1) VOTING RIGHTS, (2) Government jobs, (3) Constitutional posts (President, VP, etc.), (4) Right to purchase agricultural/plantation property. They GET: lifelong multiple-entry visa, parity with NRIs in financial/economic/educational matters."),

    (4, 2,
     "What happened to the PIO card after 2015?\nతెలుగు: PIO 2015?",
     "PIO card cancelled",
     "PIO card MERGED with OCI card / OCI లో విలీనమైంది (correct)",
     "PIO card became NRI card",
     "PIO continued unchanged",
     "b",
     "In JANUARY 2015, the PIO (Person of Indian Origin) card scheme was MERGED into OCI scheme via Citizenship (Amendment) Act 2015. All existing PIO cards were deemed to be OCI cards. Now only OCI scheme exists for foreign-citizen Indian-origin persons."),

    (4, 3,
     "Citizens of which countries are NOT eligible for OCI?\nతెలుగు: OCI అర్హత లేని దేశాలు?",
     "USA and UK", "Pakistan and Bangladesh / పాకిస్తాన్ + బంగ్లాదేశ్ (correct)",
     "China and Russia", "Canada and Australia",
     "b",
     "Citizens of PAKISTAN and BANGLADESH (and their lineage) are NOT eligible for OCI — even if of Indian origin. Section 7A(d) Citizenship Act. Aim: security and historical considerations. Sometimes also extended to certain other listed countries via notifications."),

    (4, 4,
     "Which statement about OCI/NRI/PIO is correct?\nతెలుగు: సరైన వాక్యం?",
     "OCI = Full Dual Citizenship", "NRI does not have Indian passport",
     "OCI is NOT full citizenship — only a special status / OCI = ప్రత్యేక హోదా మాత్రమే (correct)",
     "PIO continued separately after 2015",
     "c",
     "CORRECT: OCI is NOT citizenship — special status with lifelong visa. NRI = Indian citizen abroad (full citizenship rights, holds Indian passport). PIO merged into OCI in 2015. India does NOT permit dual citizenship — Art.9 lapses on foreign citizenship."),

    # ───── Section 5: CAA 2019 ─────
    (5, 1,
     "When was CAA 2019 passed by Parliament?\nతెలుగు: CAA 2019 ఎప్పుడు?",
     "2018", "2019 (correct)", "2020", "2021",
     "b",
     "CITIZENSHIP (AMENDMENT) ACT 2019 was passed by Parliament in DECEMBER 2019; received Presidential assent 12 December 2019; came into force 10 January 2020. RULES were notified later in March 2024 — 4+ years after passage due to controversy."),

    (5, 1,
     "CAA 2019 benefits minorities from which 3 countries?\nతెలుగు: ఏ 3 దేశాలు?",
     "Afghanistan, Bangladesh, Myanmar",
     "Pakistan, Bangladesh, Afghanistan / పాకిస్తాన్, బంగ్లాదేశ్, అఫ్గానిస్తాన్ (correct)",
     "Pakistan, Myanmar, Sri Lanka", "Bangladesh, Nepal, Afghanistan",
     "b",
     "CAA 2019 extends fast-track citizenship to RELIGIOUS MINORITIES from 3 specified MUSLIM-MAJORITY neighbouring countries: PAKISTAN, BANGLADESH, AFGHANISTAN. Not Myanmar (Rohingya excluded), not Sri Lanka (Tamils excluded), not Bhutan/Nepal/China."),

    (5, 2,
     "CAA 2019 covers minorities of which 6 religions?\nతెలుగు: ఏ 6 మతాలు?",
     "Hindu, Muslim, Sikh, Buddhist, Jain, Parsi",
     "Hindu, Sikh, Buddhist, Jain, Parsi, Christian / హిందూ, సిక్కు, బౌద్ధ, జైన, పార్సీ, క్రిస్టియన్ (correct)",
     "Hindu, Sikh, Buddhist, Jain, Parsi, Jew",
     "Hindu, Muslim, Sikh, Buddhist, Christian, Parsi",
     "b",
     "CAA 2019 covers 6 NON-MUSLIM minority communities: (1) Hindus, (2) Sikhs, (3) Buddhists, (4) Jains, (5) Parsis (Zoroastrians), (6) Christians — from the 3 countries. MUSLIMS are EXCLUDED. Atheists, Ahmadis, Jews etc. also not specifically covered."),

    (5, 2,
     "CAA 2019 reduced naturalisation residence requirement to?\nతెలుగు: నివాస అర్హత?",
     "3 years", "5 years (correct)", "7 years", "9 years",
     "b",
     "Pre-CAA naturalisation = 11 YEARS residence. CAA 2019 reduced this to 5 YEARS for the eligible minorities from 3 specified countries. Plus general residence pattern + character requirements per Citizenship Act 1955."),

    (5, 3,
     "Cut-off date for CAA 2019 eligibility?\nతెలుగు: Cut-off తేదీ?",
     "31 December 2013", "31 December 2014 (correct)",
     "31 December 2015", "26 January 2015",
     "b",
     "CAA 2019 cut-off date: PERSONS WHO ENTERED INDIA ON OR BEFORE 31 DECEMBER 2014 are eligible. Those who came AFTER this date are NOT covered. The cut-off was a key feature distinguishing 'historical' refugees from later migrants."),

    (5, 3,
     "Difference between CAA and NRC?\nతెలుగు: CAA vs NRC?",
     "Both same",
     "CAA grants citizenship to specific refugees; NRC identifies existing citizens / CAA = పౌరసత్వం; NRC = పౌరుల గుర్తింపు (correct)",
     "NRC is part of CAA", "NRC applies after CAA repealed",
     "b",
     "CAA (Citizenship Amendment Act) = grants CITIZENSHIP to specific religious-minority refugees from 3 countries. NRC (National Register of Citizens) = exercise to IDENTIFY/DOCUMENT existing Indian citizens (currently only in Assam, completed 2019). Separate processes. Combined CAA+NRC concerns drove protests."),

    (5, 4,
     "Which Article is mainly used to challenge CAA 2019 constitutionality?\nతెలుగు: సవాలు చేసే Article?",
     "Article 14 — Right to Equality / Art.14 సమానత్వం (correct)",
     "Article 19", "Article 32", "Article 25",
     "a",
     "ARTICLE 14 (Right to Equality) is the principal ground for CAA challenges in SC. Argument: religion-based classification violates equality. Petitioners argue 'reasonable classification' test fails — why exclude Muslims, Tibetan Buddhists, Sri Lankan Tamils? Petitions pending in SC since 2020."),

    # ───── Section 6: Specific Acts and Dates ─────
    (6, 1,
     "Citizenship Act 1955 was made under which Article?\nతెలుగు: 1955 చట్టం ఏ Article?",
     "Article 5", "Article 9", "Article 10", "Article 11 (correct)",
     "d",
     "Article 11 explicitly empowers Parliament to make law on acquisition and termination of citizenship. CITIZENSHIP ACT 1955 was the comprehensive law made under this power. Articles 5-10 are temporary commencement provisions; Art.11 provides enduring legislative authority."),

    (6, 1,
     "Residence required for Commonwealth citizens for Registration?\nతెలుగు: Commonwealth Registration?",
     "3 years", "5 years (correct)", "7 years", "11 years",
     "b",
     "Commonwealth citizens (including Ireland) require 5 YEARS of residence for Registration as Indian citizen. General Registration requires 7 years. Reflects historical reciprocity arrangements with Commonwealth nations. Earlier this was even more lenient — has been progressively tightened."),

    (6, 2,
     "Date of Constitutional Commencement under Article 5?\nతెలుగు: Commencement తేదీ?",
     "15 August 1947", "26 November 1949",
     "26 January 1950 (correct)", "26 January 1952",
     "c",
     "Article 5 cut-off = 26 JANUARY 1950 (Constitution commencement). Persons (a) DOMICILED in India + (b) born in India OR either parent born in India OR ordinarily resident 5+ years in India — became Indian citizens on this date. Foundation of citizenship at independence."),

    (6, 2,
     "Cut-off date for migration from Pakistan under Article 6?\nతెలుగు: Article 6 కట్-ఆఫ్?",
     "15 August 1947", "19 July 1948 (correct)",
     "26 January 1949", "26 January 1950",
     "b",
     "Article 6 cut-off = 19 JULY 1948 — date when permit system for entry from Pakistan was introduced. Persons migrating BEFORE this date got AUTOMATIC citizenship (subject to Indian-undivided birth/parentage). Migrating AFTER required REGISTRATION with conditions (6 months residence)."),

    (6, 3,
     "When did India join the Commonwealth?\nతెలుగు: Commonwealth?",
     "1945", "1947 (correct)", "1950", "1952",
     "b",
     "India joined Commonwealth in 1947 upon independence. After becoming a REPUBLIC in 1950, India CONTINUED in Commonwealth (London Declaration 1949 allowed republics to remain). India was the first republic to do so — paving the way for other republics."),

    (6, 4,
     "Where do persons of Indian origin abroad register under Article 8?\nతెలుగు: Article 8 ఎక్కడ?",
     "State CM offices", "Indian Diplomatic Mission / Indian Mission (correct)",
     "Supreme Court", "Union Home Ministry",
     "b",
     "Article 8: Persons of Indian origin RESIDING OUTSIDE undivided India can register at INDIAN DIPLOMATIC MISSION (Embassy/Consulate/High Commission) in country of residence. Such persons are deemed Indian citizens upon registration. Used by overseas-born descendants of Indian-origin persons."),

    # ───── Section 7: PYQ-style Comprehensive ─────
    (7, 1,
     "Citizenship Articles in the Indian Constitution span?\nతెలుగు: పౌరసత్వ Articles పరిధి?",
     "Articles 1–5", "Articles 5–11 (correct)",
     "Articles 12–35", "Articles 36–51",
     "b",
     "Articles 5–11 (Part II) deal with citizenship at the commencement of the Constitution. Part II is one of the SHORTEST PARTS of the Constitution (just 7 articles), but it lays foundation. Permanent provisions are in Citizenship Act 1955 enacted under Art.11.",
     "APPSC"),

    (7, 1,
     "Which is NOT a method of acquiring Indian citizenship?\nతెలుగు: సంపాదన పద్ధతి కానిది?",
     "By Birth", "By Naturalisation",
     "By Employment / ఉద్యోగం (correct)",
     "By Registration",
     "c",
     "5 valid modes: BIRTH, DESCENT, REGISTRATION, NATURALISATION, INCORPORATION OF TERRITORY. EMPLOYMENT is NOT a recognised mode under Citizenship Act 1955 — though an employed foreigner may qualify for Naturalisation/Registration after meeting residence conditions.",
     "APPSC"),

    (7, 2,
     "Which statement about OCI and Dual Citizenship is correct?\nతెలుగు: OCI vs Dual Citizenship?",
     "OCI = Dual Citizenship", "India allows Dual Citizenship",
     "OCI is NOT full citizenship — only a special status / OCI = ప్రత్యేక హోదా (correct)",
     "NRIs have Dual Citizenship along with OCI",
     "c",
     "OCI is a SPECIAL STATUS — NOT dual citizenship. India PROHIBITS dual citizenship via Article 9 (automatic loss on acquiring foreign citizenship). OCI has lifelong visa but no vote, no government jobs, no constitutional posts. Misnamed but legally clear it's not citizenship.",
     "UPSC"),

    (7, 2,
     "Members of which religion from CAA's 3 countries are NOT eligible?\nతెలుగు: ఏ మతం CAA కింద లేదు?",
     "Hindus", "Buddhists", "Muslims / ముస్లింలు (correct)", "Parsis",
     "c",
     "CAA 2019 covers 6 minorities (Hindu, Sikh, Buddhist, Jain, Parsi, Christian) from Pakistan/Bangladesh/Afghanistan. MUSLIMS are EXCLUDED from CAA's fast-track. Critics argue this religion-based exclusion violates Art.14 equality. Persecuted Muslim minorities (Ahmadis, Hazaras, Rohingyas) are not covered.",
     "UPSC"),

    (7, 3,
     "Difference between Single and Dual Citizenship?\nతెతెలుగు: Single vs Dual?",
     "Single = 2 levels; Dual = 1 level",
     "India = Single; USA = Dual (Federal + State) / India = Single, USA = Dual (correct)",
     "India = Dual; USA = Single", "Both Single in both countries",
     "b",
     "INDIA: SINGLE CITIZENSHIP (UK model) — only Indian citizenship; no separate state citizenship. USA: DUAL CITIZENSHIP — federal American + state (Californian/Texan etc.). Single citizenship promotes national integration; dual reflects federal-confederation origin in USA.",
     "APPSC"),

    (7, 4,
     "Correct match for modes of LOSING citizenship?\nతెలుగు: కోల్పోవడం మ్యాచ్?",
     "Renunciation = Auto; Termination = Voluntary; Deprivation = Court",
     "Renunciation = Voluntary; Termination = Auto; Deprivation = Govt action / Voluntary, Auto, Govt (correct)",
     "Renunciation = Govt; Termination = Voluntary; Deprivation = Auto",
     "All same",
     "b",
     "RENUNCIATION = VOLUNTARY (citizen's own declaration to give up). TERMINATION = AUTOMATIC (on voluntary acquisition of foreign citizenship — Art.9 / Section 9). DEPRIVATION = GOVERNMENT ACTION (compulsory cancellation for fraud, disloyalty, etc. — only applies to naturalised/registered citizens, not natural-born).",
     "UPSC"),
]

# ─────────────────────────────────────────────
# SEED FUNCTIONS
# ─────────────────────────────────────────────


def _seed_polity_ch6_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    ph = '%s' if use_postgres else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT '',
            subtopic TEXT NOT NULL DEFAULT '',
            chapter_num INTEGER NOT NULL DEFAULT 0,
            chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '',
            pages_ref TEXT NOT NULL DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if use_postgres: conn.commit()
    except Exception:
        pass

    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (6, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch6 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (6, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 6,
         'పౌరసత్వం',
         'Citizenship',
         'Ch.6',
         _json.dumps(POLITY_CH6_SECTIONS, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch6 notes seeded!'}


def _seed_polity_ch6_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = '%s' if use_postgres else '?'

    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS chapter_mcqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            study_note_id INTEGER NOT NULL,
            section_idx INTEGER NOT NULL DEFAULT 0,
            difficulty INTEGER NOT NULL DEFAULT 1,
            exam_type TEXT NOT NULL DEFAULT 'General',
            q_te TEXT NOT NULL,
            opt_a TEXT NOT NULL,
            opt_b TEXT NOT NULL,
            opt_c TEXT NOT NULL,
            opt_d TEXT NOT NULL,
            correct TEXT NOT NULL,
            explanation_te TEXT NOT NULL DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if use_postgres: conn.commit()
    except Exception:
        pass

    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (6, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch6_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (6, 'Indian_Polity'))
        row = cur.fetchone()

    note_id = row_to_dict_fn(row)['id']
    db_exec_fn(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, exam_type, "
        f"q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )

    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4,
                1: 1, 2: 2, 3: 3, 4: 4}
    easy = medium = hard = toughest = pyq = 0
    for mcq in POLITY_CH6_MCQS:
        sec_idx, diff, q, a, b, c, d, correct, expl = mcq[:9]
        exam_type = mcq[9] if len(mcq) > 9 else 'General'
        diff_int = diff_map.get(diff, 2) if not isinstance(diff, int) else diff
        db_exec_fn(conn, insert_sql,
                   (note_id, sec_idx, diff_int, exam_type, q, a, b, c, d,
                    str(correct).lower(), expl))
        if exam_type in ('APPSC', 'UPSC'):
            pyq += 1
        elif diff_int == 1: easy += 1
        elif diff_int == 2: medium += 1
        elif diff_int == 3: hard += 1
        elif diff_int == 4: toughest += 1

    if use_postgres: conn.commit()
    conn.commit()

    total = len(POLITY_CH6_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch6 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
