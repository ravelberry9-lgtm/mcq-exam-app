# seed_polity_ch7.py
# Chapter 7: Fundamental Rights
# (ప్రాథమిక హక్కులు)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total Sections: 9 | Total MCQs: 51 | PYQs: 11
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# PYQ: 10th element (index 9) = 'APPSC' or 'UPSC'
# ─────────────────────────────────────────────

import json as _json

POLITY_CH7_SECTIONS = [
    {
        "title": "7.1 ప్రాథమిక హక్కులు — పరిచయం మరియు లక్షణాలు",
        "sub": "Part III · Articles 12–35 · 6 FRs · Features · Justiciable · Enforceable",
        "audio": """ప్రాథమిక హక్కులు — పరిచయం (Introduction to Fundamental Rights):

రాజ్యాంగంలో స్థానం:
• Part III (Articles 12–35) — Fundamental Rights (ప్రాథమిక హక్కులు)
• Magna Carta of India అని పిలుస్తారు
• USA Bill of Rights (1791) నుండి స్ఫూర్తి పొందారు

మొదట 7 ప్రాథమిక హక్కులు — ఇప్పుడు 6:
• 44వ సవరణ 1978 — Right to Property (Article 19(1)(f) + Article 31) తొలగించారు
• ఇప్పుడు Article 300A కింద చట్టపరమైన హక్కు మాత్రమే

6 ప్రాథమిక హక్కులు:
1. Right to Equality (Articles 14–18)
2. Right to Freedom (Articles 19–22)
3. Right against Exploitation (Articles 23–24)
4. Right to Freedom of Religion (Articles 25–28)
5. Cultural and Educational Rights (Articles 29–30)
6. Right to Constitutional Remedies (Article 32)

ప్రాథమిక హక్కుల ముఖ్య లక్షణాలు:
• Justiciable — కోర్ట్ ద్వారా అమలు చేయించుకోవచ్చు
• Not absolute — reasonable restrictions వర్తిస్తాయి
• Suspension during Emergency (Article 358, 359)
• Parliament సవరించవచ్చు — కానీ Basic Structure రద్దు చేయలేదు
• కొన్ని పౌరులకు మాత్రమే; కొన్ని అందరికీ (citizens + aliens)"""
    },
    {
        "title": "7.2 Article 12 మరియు Article 13 — రాష్ట్రం నిర్వచనం",
        "sub": "Article 12 · Definition of State · Article 13 · Doctrine of Eclipse · Doctrine of Severability",
        "audio": """Article 12 — రాష్ట్రం (State) నిర్వచనం:

'State' అంటే ఏమిటి?
• Government and Parliament of India (కేంద్ర ప్రభుత్వం + పార్లమెంట్)
• State governments and Legislatures (రాష్ట్ర ప్రభుత్వాలు + శాసనసభలు)
• Local Authorities (స్థానిక సంస్థలు — పంచాయతీలు, Municipalities)
• Other Authorities — Rajasthan Electricity Board case లో చెప్పారు

Article 13 — ప్రాథమిక హక్కులకు విరుద్ధమైన చట్టాలు:
• Clause (1): Pre-constitutional laws (1950 జనవరి 26 కంటే ముందు) FR కి విరుద్ధమైతే వాటి FR విరుద్ధ భాగం శూన్యం (Void)
• Clause (2): Parliament/State Legislatures FR కి విరుద్ధమైన చట్టం చేయలేవు
• Clause (3): 'Law' = Ordinances, Orders, Bye-laws, Rules, Regulations, Notifications కూడా

రెండు సిద్ధాంతాలు:
1. Doctrine of Eclipse (గ్రహణ సిద్ధాంతం):
   • Pre-constitutional law FR కి విరుద్ధమైతే 'నిద్రపోతుంది' (Eclipse)
   • FR సవరణ జరిగితే తిరిగి జీవంతమవుతుంది

2. Doctrine of Severability (విభజన సిద్ధాంతం):
   • చట్టంలో FR కి విరుద్ధ భాగం మాత్రమే శూన్యం
   • మిగిలిన చట్టం చెల్లుబాటవుతుంది"""
    },
    {
        "title": "7.3 సమానత్వ హక్కు — Articles 14, 15, 16",
        "sub": "Article 14 · Equality before Law · Equal Protection · Article 15 · Article 16 · Reservation",
        "audio": """సమానత్వ హక్కు (Right to Equality) — Articles 14–18:

Article 14 — సమానత్వ హక్కు:
• "Equality before law" — British concept (Rule of Law — A.V. Dicey)
• "Equal protection of laws" — USA concept (14th Amendment)
• తేడా: Equality before law = Negative concept | Equal protection = Positive concept
• Reasonable Classification అనుమతించబడుతుంది (Intelligible Differentia + Rational Nexus)

Article 15 — వివక్ష నిషేధం:
• మతం, జాతి, కులం, లింగం, జన్మస్థలం ఆధారంగా వివక్ష నిషేధం
• Article 15(3): మహిళలు మరియు పిల్లల కోసం ప్రత్యేక నిబంధనలు అనుమతి
• Article 15(4): వెనుకబడిన వర్గాల కోసం (1st Amendment 1951 లో చేర్చారు)
• Article 15(5): OBC లకు విద్యా సంస్థల్లో రిజర్వేషన్ (93rd Amendment 2005)
• Article 15(6): EWS (Economically Weaker Sections) రిజర్వేషన్ (103rd Amendment 2019)

Article 16 — ప్రభుత్వ ఉద్యోగాల్లో సమాన అవకాశాలు:
• ప్రభుత్వ ఉద్యోగాల్లో అందరికీ సమాన అవకాశాలు
• Article 16(4): వెనుకబడిన వర్గాలకు రిజర్వేషన్ అనుమతి
• Article 16(4A): SC/ST లకు పదోన్నతిలో రిజర్వేషన్ (77th Amendment 1995)
• Article 16(4B): భర్తీ కాని ఖాళీల carry forward (81st Amendment 2000)
• Article 16(6): EWS రిజర్వేషన్ (103rd Amendment 2019)"""
    },
    {
        "title": "7.4 Articles 17 మరియు 18 — అంటరానితనం & బిరుదుల రద్దు",
        "sub": "Article 17 · Abolition of Untouchability · Protection of Civil Rights Act · Article 18 · Titles",
        "audio": """Article 17 — అంటరానితనం రద్దు (Abolition of Untouchability):

ముఖ్య విషయాలు:
• "Untouchability" ఏ రూపంలో అమలు చేసినా శిక్షార్హమైన నేరం
• ఇది absolute right — reasonable restrictions లేవు
• ఈ హక్కు పౌరులకు మాత్రమే కాదు — అందరికీ రక్షణ

చట్టాలు:
• Untouchability Offences Act 1955
• తర్వాత Protection of Civil Rights Act 1955 గా పేరు మారింది (1976)
• SC/ST (Prevention of Atrocities) Act 1989

Article 18 — బిరుదుల రద్దు (Abolition of Titles):
• State ఏ పౌరునికైనా Military/Academic బిరుదులు తప్ప ఇతర బిరుదులు ఇవ్వలేదు
• Bharat Ratna, Padma Awards ఇవ్వడం సాధారణ పౌరులకు అనుమతి ఉంది
  (Supreme Court 1996 చెప్పింది — ఇవి బిరుదులు కావు)
• India పౌరుడు విదేశ ప్రభుత్వం నుండి బిరుదు తీసుకోలేదు (రాష్ట్రపతి అనుమతి తప్పా)
• ప్రభుత్వ ఉద్యోగి విదేశ బిరుదు తీసుకోవడానికి రాష్ట్రపతి అనుమతి అవసరం

మిలిటరీ మరియు విద్యా బిరుదులు (Exemptions):
• PhD, MBBS వంటి Academic degrees — అనుమతి
• General, Colonel వంటి Military titles — అనుమతి"""
    },
    {
        "title": "7.5 స్వేచ్ఛా హక్కు — Article 19 (6 స్వేచ్ఛలు)\nRight to Freedom · Article 19 · 6 Freedoms · Reasonable Restrictions",
        "sub": "Article 19 · Speech · Assembly · Association · Movement · Residence · Profession",
        "audio": """Article 19 — స్వేచ్ఛా హక్కు (Right to Freedom):

మొదట 7 స్వేచ్ఛలు ఉండేవి — ఇప్పుడు 6:
• Article 19(1)(f) — Property right 44th Amendment 1978 ద్వారా తొలగించారు

ప్రస్తుత 6 స్వేచ్ఛలు [Article 19(1)]:
(a) మాట్లాడే మరియు వ్యక్తీకరించే స్వేచ్ఛ (Freedom of Speech and Expression)
(b) శాంతియుతంగా మరియు నిరాయుధంగా సమావేశమయ్యే స్వేచ్ఛ (Freedom of Assembly)
(c) సంఘాలు, యూనియన్లు, సహకార సంఘాలు స్థాపించే స్వేచ్ఛ (Freedom of Association)
    — 97th Amendment 2011 'cooperative societies' చేర్చింది
(d) భారతదేశం అంతటా స్వేచ్ఛగా తిరిగే స్వేచ్ఛ (Freedom of Movement)
(e) భారతదేశంలో ఎక్కడైనా నివసించే స్వేచ్ఛ (Freedom of Residence)
(g) ఏ వృత్తి అయినా చేసుకునే స్వేచ్ఛ (Freedom of Profession)

ఈ స్వేచ్ఛలు కేవలం పౌరులకు మాత్రమే (Not aliens):

Reasonable Restrictions (Article 19(2)–19(6)):
• State reasonable restrictions విధించవచ్చు
• ఉదాహరణలు: National security, public order, decency/morality, defamation, contempt of court

Press Freedom:
• రాజ్యాంగంలో ప్రత్యేకంగా పేర్కొనలేదు
• Article 19(1)(a) లో implied — "Speech and Expression" లో భాగం"""
    },
    {
        "title": "7.6 Articles 20, 21, 21A — నేర విచారణ మరియు జీవించే హక్కు\nArticle 20 · Article 21 · Article 21A · Right to Education",
        "sub": "Double Jeopardy · Self-incrimination · Ex Post Facto · Right to Life · RTE",
        "audio": """Article 20 — నేర విచారణలో రక్షణ (Protection in Conviction):

3 రక్షణలు:
(1) Ex-post facto law (నేరాత్మక చట్టాల నిషేధం):
    • నేరం చేసిన సమయంలో వర్తించిన చట్టం కంటే ఎక్కువ శిక్ష విధించలేరు
(2) Double Jeopardy (ద్వంద్వ నేర విచారణ నిషేధం):
    • ఒకే నేరానికి రెండుసార్లు విచారణ/శిక్ష వేయలేరు
    • US 5th Amendment నుండి స్ఫూర్తి
(3) Self-incrimination నిషేధం:
    • తనకు వ్యతిరేకంగా సాక్ష్యం ఇవ్వడానికి బలవంతం చేయలేరు

Article 21 — జీవించే మరియు వ్యక్తిగత స్వేచ్ఛ హక్కు:
• "No person shall be deprived of his life or personal liberty
  except according to procedure established by law"
• పౌరులకు మాత్రమే కాదు — అందరికీ (aliens కూడా)
• Maneka Gandhi case 1978 తర్వాత అనేక హక్కులు Article 21 కింద చేర్చారు:
  Right to privacy, right to livelihood, right to health, right to education (before 21A),
  right to speedy trial, right to legal aid, right against handcuffing etc.

Article 21A — విద్యా హక్కు (Right to Education):
• 86వ రాజ్యాంగ సవరణ 2002 ద్వారా చేర్చారు
• 6–14 సంవత్సరాల పిల్లలకు ఉచిత మరియు నిర్బంధ విద్య
• Right to Education Act (RTE Act) 2009 అమలు చేయబడింది"""
    },
    {
        "title": "7.7 Article 22 — అరెస్టు మరియు నిరోధక నిర్బంధం\nArticle 22 · Arrest · Preventive Detention · Advisory Board",
        "sub": "Article 22 · Rights on Arrest · 24 Hours · Preventive Detention · 3 Months",
        "audio": """Article 22 — అరెస్టు మరియు నిర్బంధంలో రక్షణ:

సాధారణ అరెస్టు (Ordinary Arrest) లో హక్కులు [Article 22(1)(2)]:
(1) అరెస్టు కారణాలు చెప్పాలి (తనకర్థమయ్యే భాషలో)
(2) న్యాయవాదిని సంప్రదించే హక్కు
(3) 24 గంటల్లోపు magistrate ముందు హాజరుపరచాలి
    (ప్రయాణపు సమయం మినహాయించి)
(4) Magistrate అనుమతి లేకుండా 24 గంటలకు మించి నిర్బంధించలేరు

ఈ హక్కులు వర్తించనివారు:
• శత్రు దేశపు పౌరులు (Enemy aliens)
• Preventive detention చట్టాల కింద నిర్బంధించబడిన వారు

నిరోధక నిర్బంధం (Preventive Detention) [Article 22(4)–(7)]:
• భవిష్యత్ నేర నివారణ కోసం నిర్బంధం
• Advisory Board అనుమతి లేకుండా గరిష్టంగా 3 నెలలు మాత్రమే
• 3 నెలలకు మించాలంటే Advisory Board (High Court జడ్జి హోదా) ఆమోదం

ముఖ్యమైన నిరోధక నిర్బంధ చట్టాలు:
• NSA (National Security Act) 1980 — 12 నెలలు వరకు
• COFEPOSA — అక్రమ వ్యాపారం నివారణ
• UAPA (Unlawful Activities Prevention Act)"""
    },
    {
        "title": "7.8 ప్రాథమిక హక్కులు — సమగ్ర విశ్లేషణ (Bilingual)\nFundamental Rights · Complete Analysis · Articles 12–22",
        "sub": "All 6 FRs Overview · Key Articles · Amendment History · APPSC Focus",
        "audio": """Fundamental Rights — Complete Analysis (సమగ్ర విశ్లేషణ):

Part III (Articles 12–35) — Magna Carta of India:
• Originally 7 FRs → Now 6 (Right to Property removed by 44th Amendment 1978)
• Article 300A: Right to property now a legal right (not fundamental)

Key Articles Summary:
• Art 12: Definition of State (Central/State/Local/Other authorities)
• Art 13: Laws inconsistent with FR are void
• Art 14: Equality before law + Equal protection (UK + USA concepts)
• Art 15: No discrimination on religion, race, caste, sex, place of birth
• Art 16: Equal opportunity in public employment + Reservations
• Art 17: Abolition of Untouchability (absolute right, no restrictions)
• Art 18: Abolition of Titles (except military/academic)
• Art 19: 6 Freedoms (only for citizens; not aliens)
• Art 20: 3 protections in conviction (ex post facto, double jeopardy, self-incrimination)
• Art 21: Right to Life and Personal Liberty (for all — citizens + aliens)
• Art 21A: Right to Education 6–14 years (86th Amendment 2002)
• Art 22: Protection against arrest and preventive detention

Amendments Relating to FRs:
• 1st Amendment 1951 → Art 15(4) — Backward classes reservation
• 44th Amendment 1978 → Right to Property removed
• 77th Amendment 1995 → SC/ST promotion reservation Art 16(4A)
• 86th Amendment 2002 → Art 21A Right to Education
• 93rd Amendment 2005 → Art 15(5) OBC in education
• 97th Amendment 2011 → Cooperative societies in Art 19(1)(c)
• 103rd Amendment 2019 → EWS 10% reservation Art 15(6) + 16(6)"""
    },
    {
        "title": "7.9 సినిమాటిక్ కథ — హక్కుల రక్షణ",
        "sub": "Story Section · FR Journey · No MCQs",
        "audio": """కథ: హక్కుల రక్షణ

1950 లో రాజ్యాంగం అమలులోకి వచ్చినప్పుడు సుందరి అనే ఒక దళిత మహిళకు ఒక గ్రామంలో నీళ్ళు తోడుకోవడానికి అనుమతి నిరాకరించారు. ఆమె ధైర్యంగా High Court కి వెళ్ళింది. Judge ఆమె వాదన విన్నాడు — Article 17 (అంటరానితనం రద్దు) మరియు Article 14 (సమానత్వ హక్కు) ఆమె రక్షణ కలిగిస్తున్నాయని తీర్పు ఇచ్చాడు.

కొన్ని సంవత్సరాల తర్వాత ఒక యువ జర్నలిస్ట్ ప్రభుత్వ అవినీతిపై వ్యాసం రాశాడు. ప్రభుత్వం అతన్ని అరెస్టు చేయబోయింది. కానీ Article 19(1)(a) — వ్యక్తీకరణ స్వేచ్ఛ అతన్ని కాపాడింది. అయితే reasonable restrictions కూడా ఉన్నాయని కోర్ట్ వివరించింది — హక్కులు absolute కావు.

Maneka Gandhi case 1978 లో Supreme Court నిర్ణయం Article 21 ని పూర్తిగా మార్చింది. "జీవించే హక్కు" కేవలం భౌతిక ఉనికి కాదు — గౌరవంగా జీవించే హక్కు, విద్య హక్కు, ఆరోగ్య హక్కు అన్నీ Article 21 లో ఇమిడి ఉన్నాయని నిర్ణయించారు.

2002 లో 86వ సవరణ ద్వారా Article 21A వచ్చింది — 6 నుండి 14 సంవత్సరాల పిల్లలందరికీ ఉచిత నిర్బంధ విద్య. ఆ తీర్పు వెలువడిన రోజు సుందరి మనవడు సంతోషంగా పాఠశాలకు వెళ్ళాడు.

ప్రాథమిక హక్కులు — అవి కేవలం రాజ్యాంగంలో అక్షరాలు కాదు. అవి ప్రతి పౌరుని జీవితాన్ని కాపాడే కవచాలు."""
    },
]

# ─────────────────────────────────────────────
# MCQ LIST
# ─────────────────────────────────────────────

POLITY_CH7_MCQS = [
    # ── Section 0 : Introduction to Fundamental Rights ──────────────────────
    (0, 1,
     "ప్రాథమిక హక్కులు రాజ్యాంగంలో ఏ భాగంలో ఉన్నాయి?",
     "Part I", "Part II", "Part III", "Part IV",
     "c",
     "Fundamental Rights రాజ్యాంగంలోని Part III (Articles 12–35) లో ఉన్నాయి. ఇవి భారత రాజ్యాంగం యొక్క Magna Carta గా పిలువబడతాయి."),

    (0, 1,
     "భారత రాజ్యాంగంలో ప్రస్తుతం ఎన్ని ప్రాథమిక హక్కులు ఉన్నాయి?",
     "5", "6", "7", "8",
     "b",
     "మొదట 7 ప్రాథమిక హక్కులు ఉండేవి. 44వ రాజ్యాంగ సవరణ 1978 ద్వారా Right to Property తొలగించారు. ఇప్పుడు 6 ప్రాథమిక హక్కులు ఉన్నాయి."),

    (0, 2,
     "Right to Property ని ప్రాథమిక హక్కుల జాబితా నుండి తొలగించిన సవరణ?",
     "42nd Amendment 1976", "44th Amendment 1978", "46th Amendment 1982", "52nd Amendment 1985",
     "b",
     "44వ రాజ్యాంగ సవరణ 1978 ద్వారా Right to Property (Article 19(1)(f) మరియు Article 31) ని ప్రాథమిక హక్కుల జాబితా నుండి తొలగించారు. ఇప్పుడు Article 300A కింద చట్టపరమైన హక్కు మాత్రమే."),

    (0, 2,
     "ప్రాథమిక హక్కుల స్ఫూర్తి ఏ దేశం నుండి తీసుకున్నారు?",
     "UK", "France", "USA", "Ireland",
     "c",
     "ప్రాథమిక హక్కులు USA Bill of Rights (1791) నుండి స్ఫూర్తి పొంది రాజ్యాంగంలో చేర్చబడ్డాయి. భారత రాజ్యాంగ Magna Carta గా Part III ని పిలుస్తారు."),

    (0, 3,
     "కింది వాటిలో ప్రాథమిక హక్కు కానిది ఏది?",
     "Right to Equality", "Right to Freedom of Religion",
     "Right to Property", "Right against Exploitation",
     "c",
     "Right to Property 44వ సవరణ 1978 ద్వారా ప్రాథమిక హక్కుల జాబితా నుండి తొలగించారు. ఇప్పుడు అది Article 300A కింద చట్టపరమైన హక్కు మాత్రమే."),

    (0, 3,
     "ప్రాథమిక హక్కులు Absolute Rights అని అనవచ్చా — ఎందుకు?",
     "అవుతాయి — ఏ restriction వేయలేరు",
     "అనవచ్చు — Courts వాటిని రక్షిస్తాయి",
     "అనలేము — Reasonable restrictions వర్తిస్తాయి",
     "అనవచ్చు — Emergency లో కూడా రద్దు కావు",
     "c",
     "ప్రాథమిక హక్కులు Absolute కావు — State reasonable restrictions విధించవచ్చు. అంతేగాక Emergency లో కొన్ని హక్కులు suspend అవుతాయి."),

    (0, 4,
     "Right to Constitutional Remedies (Article 32) ని 'Heart and Soul of the Constitution' అని పిలిచినవారు?",
     "Jawaharlal Nehru", "Dr. B.R. Ambedkar", "Dr. Rajendra Prasad", "Sardar Patel",
     "b",
     "Dr. B.R. Ambedkar Article 32 ని 'Heart and Soul of the Constitution' అని పిలిచారు. ఎందుకంటే ఈ Article లేకుండా మిగిలిన ప్రాథమిక హక్కులకు అర్థం లేదు."),

    # ── Section 1 : Articles 12 & 13 ────────────────────────────────────────
    (1, 1,
     "రాజ్యాంగంలో 'State' నిర్వచనాన్ని ఏ Article ఇస్తుంది?",
     "Article 11", "Article 12", "Article 13", "Article 14",
     "b",
     "Article 12 'State' నిర్వచనాన్ని ఇస్తుంది. State అంటే: కేంద్ర ప్రభుత్వం + పార్లమెంట్ + రాష్ట్ర ప్రభుత్వాలు + స్థానిక సంస్థలు + ఇతర అధికారాలు."),

    (1, 1,
     "ప్రాథమిక హక్కులకు విరుద్ధమైన చట్టాలు శూన్యం అని చెప్పే Article?",
     "Article 12", "Article 13", "Article 14", "Article 32",
     "b",
     "Article 13 ప్రాథమిక హక్కులకు విరుద్ధమైన చట్టాలు శూన్యం (Void) అని చెప్తుంది. Pre-constitutional laws FR కి విరుద్ధమైన మేరకు void."),

    (1, 2,
     "Article 13 లో 'Law' అనే పదం కింది వాటిలో దేన్ని కూడా చేర్చుతుంది?",
     "కేవలం Parliament చేసిన చట్టాలు మాత్రమే",
     "Ordinances, Orders, Rules, Regulations, Notifications కూడా",
     "కేవలం రాష్ట్ర శాసనసభ చేసిన చట్టాలు",
     "కేవలం రాజ్యాంగ సవరణలు",
     "b",
     "Article 13(3) ప్రకారం 'Law' అంటే Parliament మరియు State Legislature చట్టాలే కాదు — Ordinances, Orders, Bye-laws, Rules, Regulations, Notifications కూడా చేర్చారు."),

    (1, 2,
     "Doctrine of Eclipse సంబంధిత Article?",
     "Article 12", "Article 13", "Article 14", "Article 368",
     "b",
     "Doctrine of Eclipse Article 13 కు సంబంధించింది. Pre-constitutional law FR కి విరుద్ధమైతే eclipse అవుతుంది (నిద్రపోతుంది). FR సవరించబడితే తిరిగి జీవంతమవుతుంది."),

    (1, 3,
     "Doctrine of Severability మరియు Doctrine of Eclipse మధ్య ముఖ్య తేడా?",
     "Eclipse = పాత చట్టాలకు; Severability = కొత్త చట్టాలకు",
     "రెండూ ఒకే సందర్భంలో వర్తిస్తాయి",
     "Eclipse = FR కి విరుద్ధ భాగం శూన్యం; Severability = తిరిగి అమలవుతుంది",
     "Eclipse = Courts వర్తిస్తుంది; Severability = Parliament వర్తిస్తుంది",
     "a",
     "Doctrine of Eclipse: Pre-constitutional laws కు వర్తిస్తుంది — FR కి విరుద్ధ భాగం eclipse అవుతుంది, FR సవరించబడతే తిరిగి జీవంతమవుతుంది. Doctrine of Severability: FR కి విరుద్ధ భాగం మాత్రమే void — మిగిలిన చట్టం చెల్లుబాటవుతుంది."),

    (1, 4,
     "Article 12 లో 'Other Authorities' వ్యాఖ్యానం గురించి ముఖ్యమైన Case?",
     "Maneka Gandhi v. Union of India",
     "Kesavananda Bharati v. State of Kerala",
     "Rajasthan State Electricity Board v. Mohan Lal",
     "Golaknath v. State of Punjab",
     "c",
     "Rajasthan State Electricity Board v. Mohan Lal (1967) case లో Supreme Court 'Other Authorities' నిర్వచించింది. State రాజ్యాంగ సంస్థలు కాకపోయినా, State యొక్క ముఖ్యమైన సంస్థలు 'Other Authorities' లో చేరతాయి."),

    # ── Section 2 : Articles 14, 15, 16 ─────────────────────────────────────
    (2, 1,
     "Article 14 రెండు భావనలు ఏ దేశాల నుండి తీసుకున్నారు?",
     "USA మరియు UK", "UK మరియు France", "France మరియు Ireland", "USA మరియు Canada",
     "a",
     "'Equality before law' UK నుండి (A.V. Dicey Rule of Law సిద్ధాంతం); 'Equal protection of laws' USA 14వ Amendment నుండి తీసుకున్నారు."),

    (2, 1,
     "Article 15 ప్రకారం వివక్ష నిషేధం ఏ ఆధారాలపై ఉంది?",
     "మతం, జాతి, కులం, లింగం, జన్మస్థలం",
     "మతం, జాతి, కులం, భాష, వయసు",
     "మతం, కులం, లింగం, ఆర్థిక స్థితి, జన్మస్థలం",
     "జాతి, కులం, లింగం, రాష్ట్రం, ఆర్థిక స్థితి",
     "a",
     "Article 15 మతం (Religion), జాతి (Race), కులం (Caste), లింగం (Sex), జన్మస్థలం (Place of Birth) ఆధారంగా వివక్షను నిషేధిస్తుంది."),

    (2, 2,
     "Article 15(3) ఎవరికి ప్రత్యేక నిబంధనలు అనుమతిస్తుంది?",
     "SC మరియు ST", "OBC మరియు Minorities", "మహిళలు మరియు పిల్లలు", "వికలాంగులు మరియు వృద్ధులు",
     "c",
     "Article 15(3) మహిళలు (Women) మరియు పిల్లలు (Children) కోసం ప్రత్యేక నిబంధనలు చేయడానికి State కి అనుమతి ఇస్తుంది. ఇది వివక్ష నిషేధానికి మినహాయింపు."),

    (2, 2,
     "Article 15(4) ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చారు?",
     "Original Constitution", "1st Amendment 1951", "7th Amendment 1956", "42nd Amendment 1976",
     "b",
     "Article 15(4) మొదటి రాజ్యాంగ సవరణ 1951 ద్వారా చేర్చబడింది. వెనుకబడిన వర్గాలు మరియు SC/ST ల కోసం ప్రత్యేక నిబంధనలు అనుమతిస్తుంది."),

    (2, 3,
     "OBC లకు విద్యా సంస్థల్లో రిజర్వేషన్ కు అనుమతించే Article?",
     "Article 15(3)", "Article 15(4)", "Article 15(5)", "Article 16(4)",
     "c",
     "Article 15(5) 93వ రాజ్యాంగ సవరణ 2005 ద్వారా చేర్చబడింది. OBC లకు ప్రైవేటు మరియు ప్రభుత్వ విద్యా సంస్థల్లో రిజర్వేషన్ కు అనుమతిస్తుంది."),

    (2, 3,
     "Article 16(4A) ఏ వర్గానికి పదోన్నతిలో రిజర్వేషన్ కల్పిస్తుంది?",
     "OBC", "EWS", "SC/ST", "Minorities",
     "c",
     "Article 16(4A) 77వ రాజ్యాంగ సవరణ 1995 ద్వారా చేర్చబడింది. SC/ST వర్గాలకు ప్రభుత్వ ఉద్యోగాల్లో పదోన్నతిలో (Promotion) రిజర్వేషన్ కల్పిస్తుంది."),

    (2, 4,
     "EWS (Economically Weaker Sections) కి 10% రిజర్వేషన్ కల్పించిన రాజ్యాంగ సవరణ?",
     "93rd Amendment 2005", "97th Amendment 2011", "101st Amendment 2016", "103rd Amendment 2019",
     "c",
     "103వ రాజ్యాంగ సవరణ 2019 EWS (Economically Weaker Sections) కి 10% రిజర్వేషన్ కల్పించింది. Articles 15(6) మరియు 16(6) చేర్చబడ్డాయి."),

    # ── Section 3 : Articles 17 & 18 ────────────────────────────────────────
    (3, 1,
     "అంటరానితనం రద్దు చేసిన రాజ్యాంగ అనుచ్ఛేదం?",
     "Article 15", "Article 16", "Article 17", "Article 18",
     "c",
     "Article 17 అంటరానితనం (Untouchability) ని రద్దు చేసింది. ఇది అమలు చేయడం శిక్షార్హమైన నేరం. ఇది Absolute Right — ఎటువంటి restrictions లేవు."),

    (3, 1,
     "Untouchability Offences Act 1955 తర్వాత దేని పేరు మార్చారు?",
     "SC/ST Prevention Act", "Protection of Civil Rights Act 1955", "Dalits Protection Act", "Social Justice Act",
     "b",
     "Untouchability Offences Act 1955 పేరు 1976 లో Protection of Civil Rights Act 1955 గా మార్చారు. ఇది Article 17 ని అమలు చేయడానికి చేసిన చట్టం."),

    (3, 2,
     "Article 18 ప్రకారం State ఏ రకమైన బిరుదులు ఇవ్వలేదు?",
     "Military బిరుదులు", "Academic డిగ్రీలు",
     "Military మరియు Academic తప్ప ఇతర బిరుదులు", "పౌర పురస్కారాలు (Bharat Ratna)",
     "c",
     "Article 18 ప్రకారం State Military మరియు Academic బిరుదులు తప్ప ఇతర బిరుదులు ఇవ్వలేదు. Bharat Ratna, Padma Awards 1996 Supreme Court తీర్పు ప్రకారం 'బిరుదులు' కావు."),

    (3, 2,
     "Article 17 ప్రకారం అంటరానితనం నిషేధం ఏ రకమైన హక్కు?",
     "Relative Right — Reasonable restrictions ఉంటాయి",
     "Absolute Right — Restrictions లేవు",
     "రాష్ట్ర అభీష్టంపై ఆధారపడిన హక్కు",
     "Emergency లో రద్దు అయ్యే హక్కు",
     "b",
     "Article 17 ఒక Absolute Right — ఎటువంటి Reasonable Restrictions వేయడానికి అవకాశం లేదు. అంటరానితనం అమలు చేయడం శిక్షార్హమైన నేరం."),

    (3, 3,
     "భారత పౌరుడు విదేశ ప్రభుత్వం నుండి బిరుదు తీసుకోవడానికి ఏ అనుమతి అవసరం?",
     "Prime Minister అనుమతి", "Supreme Court అనుమతి",
     "రాష్ట్రపతి (President) అనుమతి", "Parliament అనుమతి",
     "c",
     "Article 18 ప్రకారం భారత పౌరుడు విదేశ ప్రభుత్వం నుండి బిరుదు తీసుకోవాలంటే రాష్ట్రపతి (President of India) అనుమతి తప్పనిసరి."),

    (3, 4,
     "SC/ST (Prevention of Atrocities) Act ఏ సంవత్సరంలో చేయబడింది?",
     "1976", "1985", "1989", "1995",
     "c",
     "SC/ST (Prevention of Atrocities) Act 1989 అంటరానితనం మరియు అత్యాచారాల నివారణకు చేయబడింది. ఇది Article 17 ని బలపరుస్తుంది."),

    # ── Section 4 : Article 19 — 6 Freedoms (Bilingual) ────────────────────
    (4, 1,
     "Article 19 కింద ఎన్ని స్వేచ్ఛలు ఉన్నాయి?\nHow many freedoms are guaranteed under Article 19?",
     "4", "5", "6", "7",
     "c",
     "Article 19 కింద ప్రస్తుతం 6 స్వేచ్ఛలు ఉన్నాయి. మొదట 7 ఉండేవి — 44వ సవరణ 1978 ద్వారా Right to Property [Art 19(1)(f)] తొలగించారు.\nCurrently 6 freedoms under Article 19; originally 7 — property right removed by 44th Amendment 1978."),

    (4, 1,
     "Article 19(1) కింద స్వేచ్ఛలు ఎవరికి వర్తిస్తాయి?\nFreedoms under Article 19(1) are available to whom?",
     "అందరికీ (పౌరులు + విదేశీయులు) / All persons (citizens + aliens)",
     "కేవలం పౌరులకు మాత్రమే / Only citizens",
     "కేవలం జన్మతః పౌరులకు / Only citizens by birth",
     "పౌరులు మరియు OCI కార్డుదారులకు / Citizens and OCI card holders",
     "b",
     "Article 19 కింద స్వేచ్ఛలు కేవలం భారత పౌరులకు మాత్రమే వర్తిస్తాయి. విదేశీయులకు (Aliens) ఈ స్వేచ్ఛలు వర్తించవు.\nFreedoms under Article 19 are available only to Indian citizens, not to aliens."),

    (4, 2,
     "97వ రాజ్యాంగ సవరణ 2011 Article 19(1)(c) కి ఏ పదం చేర్చింది?\nWhat did the 97th Amendment 2011 add to Article 19(1)(c)?",
     "Unions / యూనియన్లు",
     "Cooperative societies / సహకార సంఘాలు",
     "Political parties / రాజకీయ పార్టీలు",
     "NGOs / స్వచ్ఛంద సంస్థలు",
     "b",
     "97వ రాజ్యాంగ సవరణ 2011 Article 19(1)(c) కి 'cooperative societies' (సహకార సంఘాలు) అనే పదం చేర్చింది.\n97th Amendment 2011 added 'cooperative societies' to Article 19(1)(c)."),

    (4, 2,
     "Press Freedom ని రాజ్యాంగం ఏ Article కింద implied గా అనుమతిస్తుంది?\nPress Freedom is implied under which Article?",
     "Article 19(1)(a)", "Article 19(1)(b)", "Article 19(1)(c)", "Article 19(1)(g)",
     "a",
     "రాజ్యాంగంలో Press Freedom ని ప్రత్యేకంగా పేర్కొనలేదు. కానీ Article 19(1)(a) — Freedom of Speech and Expression లో Press Freedom implied గా ఉంది.\nPress freedom is implied under Article 19(1)(a) — Freedom of Speech and Expression."),

    (4, 3,
     "Article 19 కింద Reasonable Restrictions విధించే అధికారం ఎవరికి ఉంది?\nWho can impose Reasonable Restrictions under Article 19?",
     "Supreme Court", "President of India", "State (Central/State governments)", "Parliament only",
     "c",
     "Article 19(2) నుండి 19(6) ప్రకారం State (Central/State governments) Reasonable Restrictions విధించవచ్చు. National security, public order, decency/morality, defamation వంటి కారణాలకు.\nState (Central/State governments) can impose Reasonable Restrictions under Articles 19(2)–19(6)."),

    (4, 4,
     "Article 19(1)(g) కింద ఏ స్వేచ్ఛ ఉంది?\nWhat freedom is guaranteed under Article 19(1)(g)?",
     "ఎక్కడైనా నివసించే స్వేచ్ఛ / Freedom of residence",
     "అసెంబ్లీ స్వేచ్ఛ / Freedom of assembly",
     "వ్యాపారం చేసే స్వేచ్ఛ / Freedom of trade or profession",
     "సంఘాలు స్థాపించే స్వేచ్ఛ / Freedom of association",
     "c",
     "Article 19(1)(g) ఏ వృత్తి, వ్యాపారం లేదా వ్యాపకం అయినా చేసుకునే స్వేచ్ఛ (Freedom to practise any profession, or to carry on any occupation, trade or business) ఇస్తుంది.\nArticle 19(1)(g) guarantees freedom of profession, occupation, trade or business.",
     "UPSC"),

    # ── Section 5 : Articles 20, 21, 21A (Bilingual) ────────────────────────
    (5, 1,
     "Article 21 ప్రకారం 'జీవించే హక్కు' ఎవరికి వర్తిస్తుంది?\nTo whom does Article 21 Right to Life apply?",
     "కేవలం పౌరులకు / Only citizens",
     "పౌరులు మరియు OCI కార్డుదారులకు / Citizens and OCI holders",
     "అందరికీ — పౌరులు + విదేశీయులు / All persons — citizens + aliens",
     "కేవలం జన్మతః పౌరులకు / Only citizens by birth",
     "c",
     "Article 21 కేవలం పౌరులకు మాత్రమే కాదు — అందరికీ (పౌరులు మరియు విదేశీయులు) వర్తిస్తుంది.\nArticle 21 applies to all persons — both citizens and aliens — not just citizens."),

    (5, 1,
     "Article 21A విద్యా హక్కు ఏ వయసు వర్గానికి వర్తిస్తుంది?\nRight to Education under Article 21A covers which age group?",
     "5–14 సంవత్సరాలు / 5–14 years", "6–14 సంవత్సరాలు / 6–14 years",
     "6–16 సంవత్సరాలు / 6–16 years", "5–18 సంవత్సరాలు / 5–18 years",
     "b",
     "Article 21A 6–14 సంవత్సరాల పిల్లలకు ఉచిత మరియు నిర్బంధ విద్య హక్కు ఇస్తుంది.\nArticle 21A guarantees free and compulsory education for children aged 6–14 years."),

    (5, 2,
     "Article 21A ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చబడింది?\nArticle 21A was added by which constitutional amendment?",
     "73rd Amendment 1992", "86th Amendment 2002", "93rd Amendment 2005", "97th Amendment 2011",
     "b",
     "Article 21A 86వ రాజ్యాంగ సవరణ 2002 ద్వారా చేర్చబడింది. దీని అమలు కోసం Right to Education Act (RTE Act) 2009 చేయబడింది.\nArticle 21A was added by the 86th Amendment 2002; RTE Act 2009 implements it."),

    (5, 2,
     "Article 20 యొక్క 'Double Jeopardy' రక్షణ ఏ దేశం నుండి తీసుకున్నారు?\nDouble Jeopardy protection in Article 20 is borrowed from which country?",
     "UK", "USA", "Canada", "Australia",
     "b",
     "Double Jeopardy రక్షణ USA యొక్క 5వ Amendment నుండి తీసుకున్నారు. ఒకే నేరానికి రెండుసార్లు విచారణ/శిక్ష వేయరాదు అని Article 20(2) చెప్తుంది.\nDouble Jeopardy protection in Article 20(2) is borrowed from USA's 5th Amendment."),

    (5, 3,
     "Maneka Gandhi v. Union of India (1978) case Article 21 కి ఏ మార్పు తెచ్చింది?",
     "Article 21 రద్దు చేయమని కోరింది",
     "Article 21 కేవలం physical liberty కు పరిమితం అని నిర్ణయించింది",
     "Article 21 విస్తృతంగా వ్యాఖ్యానించి అనేక హక్కులు చేర్చారు",
     "Article 21 కేవలం Criminal cases కు వర్తిస్తుందని నిర్ణయించింది",
     "c",
     "Maneka Gandhi case 1978 లో Supreme Court Article 21 ని విస్తృతంగా వ్యాఖ్యానించింది. Right to privacy, right to livelihood, right to speedy trial, right to health వంటి అనేక హక్కులు Article 21 కింద implied అని నిర్ణయించారు."),

    (5, 3,
     "Article 20(3) — Self-incrimination నిషేధం గురించి సరైన వాక్యం?",
     "నేర అభ్యోపిపై DNA test నిర్బంధంగా చేయవచ్చు",
     "అభ్యోపి తనకు వ్యతిరేకంగా సాక్ష్యం ఇవ్వడానికి బలవంతపెట్టలేరు",
     "Witness లకు కూడా Self-incrimination రక్షణ వర్తిస్తుంది",
     "Civil cases లో కూడా Article 20(3) వర్తిస్తుంది",
     "b",
     "Article 20(3) ప్రకారం నేర అభ్యోపి (accused person) తనకు వ్యతిరేకంగా సాక్ష్యం ఇవ్వడానికి బలవంతపెట్టలేరు. ఇది USA 5th Amendment లాంటిది. Witnesses కు వర్తించదు, Civil cases కు వర్తించదు.",
     "APPSC"),

    (5, 4,
     "Article 20 కింద Ex-post facto law నిషేధం అంటే ఏమిటి?",
     "నేరానికి పూర్వం ఉన్న చట్టం కంటే ఎక్కువ శిక్ష విధించలేరు",
     "నేరం జరిగిన తర్వాత నేరాన్ని నిర్వచించే చట్టం చేయవచ్చు",
     "రెట్రోస్పెక్టివ్ చట్టాలు పూర్తిగా అనుమతించబడతాయి",
     "Civil cases లో Ex-post facto నిషేధం వర్తించదు",
     "a",
     "Article 20(1) Ex-post facto law నిషేధం: ఒక వ్యక్తి నేరం చేసిన సమయంలో వర్తించిన చట్టం కంటే ఎక్కువ శిక్ష విధించలేరు. నేరం జరిగిన తర్వాత ఆ నేరానికి ఎక్కువ శిక్ష పెంచిన చట్టాన్ని Retrospectively అమలు చేయలేరు.",
     "UPSC"),

    # ── Section 6 : Article 22 (Bilingual) ──────────────────────────────────
    (6, 1,
     "అరెస్టు చేయబడిన వ్యక్తిని ఎంత సమయంలో Magistrate ముందు హాజరుపరచాలి?\nWithin what time must an arrested person be produced before a Magistrate?",
     "12 గంటలు / 12 hours", "24 గంటలు / 24 hours",
     "48 గంటలు / 48 hours", "72 గంటలు / 72 hours",
     "b",
     "Article 22(2) ప్రకారం అరెస్టు చేయబడిన వ్యక్తిని 24 గంటల్లోపు (ప్రయాణపు సమయం మినహాయించి) Magistrate ముందు హాజరుపరచాలి.\nArticle 22(2): Arrested person must be produced before a Magistrate within 24 hours (excluding travel time)."),

    (6, 1,
     "Preventive Detention కింద Advisory Board అనుమతి లేకుండా గరిష్ట నిర్బంధ కాలం?\nMaximum detention without Advisory Board approval under Preventive Detention?",
     "1 నెల / 1 month", "2 నెలలు / 2 months",
     "3 నెలలు / 3 months", "6 నెలలు / 6 months",
     "c",
     "Article 22(4) ప్రకారం Preventive Detention కింద Advisory Board అనుమతి లేకుండా గరిష్టంగా 3 నెలలు మాత్రమే నిర్బంధించవచ్చు.\nUnder Article 22(4), preventive detention without Advisory Board approval cannot exceed 3 months.",
     "APPSC"),

    (6, 2,
     "Article 22 కింద సాధారణ అరెస్టులో వ్యక్తికి ఏ హక్కు ఉంది?\nWhat right does an arrested person have under Article 22 in ordinary arrest?",
     "కేవలం Magistrate ముందు హాజరయ్యే హక్కు",
     "న్యాయవాదిని సంప్రదించే హక్కు మరియు అరెస్టు కారణాలు తెలుసుకోవడం",
     "Bail తీసుకోవడం అధికారం",
     "ఉచిత న్యాయ సహాయం పొందే హక్కు",
     "b",
     "Article 22(1) ప్రకారం: అరెస్టు కారణాలు తెలుసుకోవడం, న్యాయవాదిని సంప్రదించే హక్కు. Article 22(2) ప్రకారం: 24 గంటల్లో Magistrate ముందు హాజరు.\nArticle 22: Right to know grounds of arrest + right to consult lawyer + production before Magistrate within 24 hrs."),

    (6, 2,
     "Article 22 రక్షణలు ఎవరికి వర్తించవు?\nTo whom does Article 22 protection NOT apply?",
     "OBC వర్గాలకు", "శత్రు దేశపు పౌరులకు (Enemy Aliens)",
     "మైనర్లకు", "మహిళలకు",
     "b",
     "Article 22 రక్షణలు శత్రు దేశపు పౌరులకు (Enemy Aliens) మరియు Preventive Detention చట్టాల కింద నిర్బంధించబడినవారికి వర్తించవు.\nArticle 22 protections do not apply to enemy aliens and persons detained under preventive detention laws."),

    (6, 3,
     "National Security Act (NSA) 1980 కింద గరిష్ట నిర్బంధ కాలం?\nMaximum detention period under National Security Act (NSA) 1980?",
     "3 నెలలు / 3 months", "6 నెలలు / 6 months",
     "12 నెలలు / 12 months", "24 నెలలు / 24 months",
     "c",
     "National Security Act (NSA) 1980 కింద గరిష్టంగా 12 నెలలు (1 సంవత్సరం) వరకు Preventive Detention చేయవచ్చు.\nUnder NSA 1980, a person can be detained for up to 12 months under preventive detention."),

    (6, 4,
     "Preventive Detention మరియు Punitive Detention మధ్య ముఖ్య తేడా?\nKey difference between Preventive Detention and Punitive Detention?",
     "రెండూ ఒకే విషయం",
     "Preventive = భవిష్యత్ నేర నివారణ; Punitive = నేరం నిరూపించిన తర్వాత శిక్ష",
     "Preventive = Courts విధిస్తాయి; Punitive = ప్రభుత్వం విధిస్తుంది",
     "Preventive = జీవితకాలం; Punitive = కొద్ది నెలలు",
     "b",
     "Preventive Detention = భవిష్యత్తులో నేరం చేయకుండా నివారణ కోసం. Punitive Detention = నేరం నిరూపించబడిన తర్వాత విధించే శిక్ష (Judicial process తర్వాత).\nPreventive Detention prevents future crimes; Punitive Detention punishes after trial.",
     "UPSC"),

    # ── Section 7 : Comprehensive Analysis (Bilingual) ──────────────────────
    (7, 1,
     "కింది Fundamental Rights లో ఏది Emergency లో కూడా Suspend కాదు?\nWhich Fundamental Right cannot be suspended even during Emergency?",
     "Article 19 — 6 Freedoms",
     "Article 14 — Equality",
     "Article 20 మరియు 21 / Articles 20 and 21",
     "Article 22 — Protection against arrest",
     "c",
     "Articles 20 మరియు 21 National Emergency లో కూడా suspend అవ్వవు. Article 358 కారణంగా Article 19 External Emergency లో suspend అవుతుంది. Article 359 వల్ల ఇతర హక్కులు Suspension అవుతాయి — కానీ 20, 21 కావు.\nArticles 20 and 21 cannot be suspended even during a National Emergency.",
     "APPSC"),

    (7, 1,
     "Article 14 లో 'Equality before law' మరియు 'Equal protection of laws' మధ్య తేడా?\nDifference between 'Equality before law' and 'Equal protection of laws' in Article 14?",
     "రెండూ ఒకే విషయం",
     "Equality before law = Negative concept (UK); Equal protection = Positive concept (USA)",
     "Equality before law = Positive; Equal protection = Negative",
     "రెండూ USA నుండి తీసుకున్నారు",
     "b",
     "'Equality before law' = Negative concept — UK Rule of Law (A.V. Dicey) నుండి. 'Equal protection of laws' = Positive concept — USA 14th Amendment నుండి.\n'Equality before law' is a negative concept (UK); 'Equal protection of laws' is a positive concept (USA).",
     "UPSC"),

    (7, 2,
     "కింది వాటిలో Article 21 కింద included అయ్యే హక్కు ఏది?\nWhich right has been read into Article 21 by the Supreme Court?",
     "Right to vote / ఓటు హక్కు",
     "Right to property / ఆస్తి హక్కు",
     "Right to privacy / గోప్యత హక్కు",
     "Right to education for adults / పెద్దలకు విద్య హక్కు",
     "c",
     "Supreme Court అనేక హక్కులను Article 21 కింద Read In చేసింది — Right to privacy (K.S. Puttaswamy case 2017), right to livelihood, right to speedy trial, right to health మొదలైనవి.\nRight to privacy (K.S. Puttaswamy case 2017) has been read into Article 21 by the Supreme Court.",
     "APPSC"),

    (7, 2,
     "Article 15(6) మరియు Article 16(6) ఏ వర్గానికి రిజర్వేషన్ కల్పిస్తాయి?\nArticles 15(6) and 16(6) provide reservation for which category?",
     "SC/ST", "OBC", "Minorities", "EWS (Economically Weaker Sections)",
     "d",
     "Articles 15(6) మరియు 16(6) 103వ రాజ్యాంగ సవరణ 2019 ద్వారా చేర్చబడ్డాయి. EWS (Economically Weaker Sections) కి 10% రిజర్వేషన్ కల్పిస్తాయి.\nArticles 15(6) and 16(6) added by 103rd Amendment 2019 provide 10% reservation for EWS.",
     "APPSC"),

    (7, 3,
     "Fundamental Rights అన్నీ పౌరులకే — aliens కు వర్తించవు — ఇది సరైనదా?\nFundamental Rights apply only to citizens, not aliens — is this correct?",
     "అవుతాయి — అన్నీ పౌరులకే",
     "కాదు — Article 14, 20, 21 అందరికీ వర్తిస్తాయి",
     "అవుతాయి — కానీ Aliens కు ప్రత్యేక అనుమతితో వర్తిస్తాయి",
     "OCI కార్డుదారులకు మాత్రమే అందరూ వర్తిస్తాయి",
     "b",
     "అన్ని FR లు పౌరులకే కావు. Article 14 (Equality), 20 (Protection in conviction), 21 (Right to Life), 25–28 (Religious Freedom) అందరికీ — పౌరులు + Aliens — వర్తిస్తాయి. Article 19 మాత్రమే పౌరులకే.\nNot all FRs apply only to citizens. Articles 14, 20, 21, 25–28 apply to all persons including aliens.",
     "UPSC"),

    (7, 4,
     "కింది జతలలో సరైన జత ఏది (Article — దాని విషయం)?\nWhich pair is correctly matched (Article — Subject)?",
     "Article 17 — Abolition of Titles / బిరుదుల రద్దు",
     "Article 18 — Abolition of Untouchability / అంటరానితనం రద్దు",
     "Article 21A — Right to Education 6–14 years / 6–14 సంవత్సరాల విద్య హక్కు",
     "Article 20 — Right to Life / జీవించే హక్కు",
     "c",
     "Article 21A = Right to Education (6–14 years); Article 17 = Abolition of Untouchability; Article 18 = Abolition of Titles; Article 20 = Protection in Conviction (not Right to Life — that is Article 21).\nArticle 21A = Right to Education (6–14 years) is the correct match.",
     "APPSC"),
]

# ─────────────────────────────────────────────
# SEED FUNCTIONS
# ─────────────────────────────────────────────


def _seed_polity_ch7_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
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
        (7, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch7 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (7, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 7,
         'ప్రాథమిక హక్కులు భాగం I',
         'Fundamental Rights Part I',
         'Ch.7',
         _json.dumps(POLITY_CH7_SECTIONS, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch7 notes seeded!'}


def _seed_polity_ch7_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (7, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch7_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (7, 'Indian_Polity'))
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
    for mcq in POLITY_CH7_MCQS:
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

    total = len(POLITY_CH7_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch7 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
