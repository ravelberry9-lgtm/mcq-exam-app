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
    # ───── Section 0: FR Overview & History ─────
    (0, 1,
     "In which Part of the Constitution are Fundamental Rights placed?\nతెలుగు: ప్రాథమిక హక్కులు ఏ Part?",
     "Part I", "Part II", "Part III (correct)", "Part IV",
     "c",
     "Fundamental Rights are in PART III (Articles 12–35) — called 'MAGNA CARTA' of Indian Constitution. Borrowed from US Bill of Rights. Part III is justiciable — enforceable in courts via Art.32 (Heart and Soul of Constitution per Ambedkar)."),

    (0, 1,
     "How many Fundamental Rights does the Constitution currently provide?\nతెలుగు: ప్రస్తుతం FR ఎన్ని?",
     "5", "6 (correct)", "7", "8",
     "b",
     "Currently 6 FRs: (1) Right to Equality (Art.14-18), (2) Right to Freedom (Art.19-22), (3) Right against Exploitation (Art.23-24), (4) Right to Freedom of Religion (Art.25-28), (5) Cultural & Educational Rights (Art.29-30), (6) Right to Constitutional Remedies (Art.32). Originally 7; Right to Property removed by 44th Amendment 1978."),

    (0, 2,
     "Which Amendment removed Right to Property from Fundamental Rights?\nతెలుగు: ఏ సవరణ Right to Property?",
     "42nd Amendment 1976",
     "44th Amendment 1978 (correct)",
     "46th Amendment 1982",
     "52nd Amendment 1985",
     "b",
     "44th CONSTITUTIONAL AMENDMENT 1978 removed Right to Property from FR list (deleted Art.19(1)(f) and Art.31). It became a CONSTITUTIONAL/LEGAL right under Article 300A. Done to enable land reforms without FR-based challenges."),

    (0, 2,
     "Inspiration for Fundamental Rights came from which country?\nతెలుగు: FR ఏ దేశం నుండి?",
     "UK", "France", "USA (correct)", "Ireland",
     "c",
     "Indian FRs are inspired by US BILL OF RIGHTS (1791 — first 10 amendments to US Constitution). The framework, scope, and judicial review concepts are largely US-based. Differs in details (specific Indian context, more elaborate, includes positive obligations)."),

    (0, 3,
     "Which of the following is NOT a Fundamental Right?\nతెలుగు: FR కానిది?",
     "Right to Equality", "Right to Freedom of Religion",
     "Right to Property / ఆస్తి హక్కు (correct)",
     "Right against Exploitation",
     "c",
     "RIGHT TO PROPERTY is NOT a FR after 1978 — moved to Article 300A as a constitutional/legal right (44th Amendment). Removal was controversial; SC has interpreted Art.300A protectively. Right to Property was a major reason for 1st, 4th, 17th, 25th, 39th, 40th, 42nd Amendments before its eventual removal."),

    (0, 3,
     "Are Fundamental Rights Absolute? Why?\nతెలుగు: FR Absolute నా?",
     "Yes — no restrictions allowed",
     "Yes — Courts protect them",
     "No — Reasonable restrictions apply / కాదు, Reasonable restrictions (correct)",
     "Yes — even during Emergency",
     "c",
     "FRs are NOT absolute. State can impose REASONABLE RESTRICTIONS in interests of: sovereignty, integrity, public order, decency/morality, contempt of court, defamation, incitement to offence, etc. Restrictions must satisfy 'reasonable' test (Art.19(2)-(6)). During NE, even Art.19 can be suspended (Art.358); but Art.20, 21 NEVER suspended (44th Amendment)."),

    (0, 4,
     "Who called Article 32 'Heart and Soul of the Constitution'?\nతెలుగు: 'Heart and Soul' ఎవరు?",
     "Jawaharlal Nehru",
     "Dr. B.R. Ambedkar (correct)",
     "Dr. Rajendra Prasad", "Sardar Patel",
     "b",
     "Dr. B.R. AMBEDKAR called Article 32 (Right to Constitutional Remedies) 'HEART AND SOUL OF THE CONSTITUTION' in Constituent Assembly debate. Without enforcement mechanism (writs to SC), all other FRs would be empty promises. Art.32 is itself a FR (only such enforcement mechanism in any constitution)."),

    # ───── Section 1: Article 12 & 13 ─────
    (1, 1,
     "Which Article defines 'State' for FR purposes?\nతెలుగు: 'State' నిర్వచనం?",
     "Article 11", "Article 12 (correct)", "Article 13", "Article 14",
     "b",
     "Article 12 defines 'STATE' for Part III (FRs): includes (a) Government and Parliament of India, (b) Government and Legislature of every State, (c) all LOCAL authorities (Panchayats, Municipalities), (d) OTHER AUTHORITIES within India or under Government of India's control. SC has expanded scope to include statutory corporations, govt-controlled bodies."),

    (1, 1,
     "Which Article voids laws inconsistent with FRs?\nతెలుగు: FR కి విరుద్ధ చట్టాలు?",
     "Article 12", "Article 13 (correct)", "Article 14", "Article 32",
     "b",
     "Article 13 declares laws inconsistent with FRs as VOID. Art.13(1): pre-Constitution laws void to extent of inconsistency. Art.13(2): post-Constitution laws can't take away FRs. Art.13(3): broad definition of 'law'. Basic engine of FR enforcement and judicial review."),

    (1, 2,
     "Article 13 'law' definition INCLUDES which of these?\nతెలుగు: Art.13 'Law' అంటే?",
     "Only Parliament laws",
     "Ordinances, Orders, Rules, Regulations, Notifications also / ఆర్డినెన్స్, రూల్స్, నోటిఫికేషన్లు కూడా (correct)",
     "Only state legislature laws",
     "Only Constitutional Amendments",
     "b",
     "Art.13(3): 'LAW' includes Ordinances, Orders, Bye-laws, Rules, Regulations, Notifications, Customs/Usages having force of law. BROAD definition ensures all forms of governmental action subject to FR test. EXCEPT: Constitutional Amendments themselves under Art.368 (per Kesavananda Bharati 1973, with basic-structure exception)."),

    (1, 2,
     "Which Article is associated with Doctrine of Eclipse?\nతెలుగు: Doctrine of Eclipse Article?",
     "Article 12", "Article 13 (correct)", "Article 14", "Article 368",
     "b",
     "DOCTRINE OF ECLIPSE (Bhikaji Narain Dhakras 1955): A pre-Constitution law inconsistent with FR is NOT dead but ECLIPSED (dormant). If FR is later amended/removed, the eclipsed law revives. Applies under Art.13(1) only to PRE-Constitution laws — NOT post-Constitution laws (which are void ab initio)."),

    (1, 3,
     "Difference between Doctrine of Eclipse and Doctrine of Severability?\nతెలుగు: Eclipse vs Severability?",
     "Eclipse = pre-Constitution; Severability = applies to part of law / Eclipse pre-Const, Severability part-void (correct)",
     "Both apply same context", "Eclipse void; Severability revives",
     "Eclipse Courts; Severability Parliament",
     "a",
     "ECLIPSE: Pre-Constitution law inconsistent with FR is dormant (eclipsed) but revives if FR amended. SEVERABILITY: A statute partially inconsistent with FR — only the offending PART is struck down (severed); rest of statute survives if separable. Eclipse = TIMING; Severability = SCOPE of invalidity."),

    (1, 4,
     "Important case on 'Other Authorities' interpretation in Article 12?\nతెలుగు: 'Other Authorities' కేసు?",
     "Maneka Gandhi v. Union of India",
     "Kesavananda Bharati v. State of Kerala",
     "Rajasthan State Electricity Board v. Mohan Lal (correct)",
     "Golaknath v. State of Punjab",
     "c",
     "Rajasthan State Electricity Board v. Mohan Lal (1967): SC interpreted 'OTHER AUTHORITIES' in Art.12 broadly. Test: (i) whether body has statutory powers to issue binding directions/orders; (ii) is govt-controlled. Later expanded in Sukhdev Singh, Ajay Hasia, Pradeep Kumar Biswas. Test now: 'STATE INSTRUMENTALITY/AGENCY'."),

    # ───── Section 2: Right to Equality (Art.14-18) ─────
    (2, 1,
     "Article 14's two concepts are borrowed from which countries?\nతెలుగు: Art.14 ఏ దేశాలు?",
     "USA and UK (correct)", "UK and France",
     "France and Ireland", "USA and Canada",
     "a",
     "Article 14 has TWO concepts: (1) 'EQUALITY BEFORE LAW' — borrowed from UK (A.V. Dicey's RULE OF LAW). Negative concept — absence of privilege. (2) 'EQUAL PROTECTION OF LAWS' — borrowed from US 14th Amendment. Positive concept — equal treatment in equal circumstances; reasonable classification permitted."),

    (2, 1,
     "Article 15 prohibits discrimination on which grounds?\nతెలుగు: Art.15 వివక్ష ఆధారాలు?",
     "Religion, race, caste, sex, place of birth / మతం, జాతి, కులం, లింగం, జన్మస్థలం (correct)",
     "Religion, race, caste, language, age",
     "Religion, caste, sex, economic status, birthplace",
     "Race, caste, sex, state, economic status",
     "a",
     "Art.15 prohibits discrimination by State on grounds of: (1) RELIGION, (2) RACE, (3) CASTE, (4) SEX, (5) PLACE OF BIRTH — or any of them. (Note: NOT residence, NOT language, NOT age, NOT economic status — these are not Art.15 grounds, though may be relevant under Art.14)."),

    (2, 2,
     "Article 15(3) permits special provisions for whom?\nతెలుగు: Art.15(3) ఎవరికి?",
     "SC and ST", "OBC and Minorities",
     "Women and Children / మహిళలు + పిల్లలు (correct)",
     "Disabled and Elderly",
     "c",
     "Art.15(3): State can make SPECIAL PROVISIONS for WOMEN and CHILDREN — exception to non-discrimination. Has been used for: women's reservation in panchayats, separate jails, criminal procedure protections, free school meals, scholarships. Considered protective discrimination (positive)."),

    (2, 2,
     "Article 15(4) was added by which Amendment?\nతెలుగు: Art.15(4) ఏ సవరణ?",
     "Original Constitution",
     "1st Amendment 1951 (correct)",
     "7th Amendment 1956",
     "42nd Amendment 1976",
     "b",
     "Art.15(4) added by 1st CONSTITUTIONAL AMENDMENT 1951 (response to Champakam Dorairajan case 1951, which had struck down Madras govt's caste-based reservations). Allows special provisions for SOCIALLY AND EDUCATIONALLY BACKWARD CLASSES (SEBC) or SC/ST. Constitutional foundation for OBC/SC/ST reservations."),

    (2, 3,
     "Which Article enables OBC reservations in private educational institutions?\nతెలుగు: Private విద్యా సంస్థలకు?",
     "Article 15(3)", "Article 15(4)",
     "Article 15(5) (correct)",
     "Article 16(4)",
     "c",
     "Art.15(5) added by 93rd Constitutional Amendment 2005 — allows STATE to make special provisions for SEBC/SC/ST in admissions to PRIVATE educational institutions (whether aided or unaided), EXCLUDING minority institutions covered by Art.30. Validity upheld in Ashoka Kumar Thakur (2008)."),

    (2, 3,
     "Article 16(4A) provides reservation in promotion for whom?\nతెలుగు: Art.16(4A)?",
     "OBC", "EWS",
     "SC/ST / SC/ST (correct)",
     "Minorities",
     "c",
     "Art.16(4A) added by 77th Constitutional Amendment 1995. Provides RESERVATION IN PROMOTION for SC/ST in govt jobs (response to Indra Sawhney 1992 which had barred reservation in promotions). 85th Amendment 2001 added 'consequential seniority'. Subject to creamy layer (M. Nagaraj 2006, Jarnail Singh 2018) and inadequacy of representation."),

    (2, 4,
     "Which Amendment provided 10% EWS reservation?\nతెలుగు: EWS 10% ఏ సవరణ?",
     "93rd Amendment 2005", "97th Amendment 2011",
     "101st Amendment 2016",
     "103rd Amendment 2019 (correct)",
     "d",
     "103rd CONSTITUTIONAL AMENDMENT 2019 added Articles 15(6) and 16(6) — providing 10% reservation for ECONOMICALLY WEAKER SECTIONS (EWS) of unreserved categories. Family income < ₹8 lakh as per current rules. Constitutional validity upheld in Janhit Abhiyan v. Union of India (2022) by 3:2 majority."),

    # ───── Section 3: Untouchability & Titles ─────
    (3, 1,
     "Which Article abolishes Untouchability?\nతెలుగు: అంటరానితనం రద్దు?",
     "Article 15", "Article 16",
     "Article 17 (correct)", "Article 18",
     "c",
     "Article 17: 'Untouchability' is ABOLISHED and its practice in any form is FORBIDDEN. Enforcement of any disability arising out of untouchability is an offence punishable by law. Enacted via Untouchability Offences Act 1955 (later Protection of Civil Rights Act 1955 since 1976) and SC/ST (Prevention of Atrocities) Act 1989."),

    (3, 1,
     "Untouchability Offences Act 1955 was renamed as?\nతెలుగు: 1955 చట్టం పేరు?",
     "SC/ST Prevention Act",
     "Protection of Civil Rights Act 1955 (correct)",
     "Dalits Protection Act", "Social Justice Act",
     "b",
     "Untouchability Offences Act 1955 was RENAMED in 1976 as PROTECTION OF CIVIL RIGHTS ACT 1955 (with stricter penalties). Implements Art.17 by criminalising practice of untouchability. Subsequently strengthened by SC/ST (Prevention of Atrocities) Act 1989 dealing with caste-based atrocities."),

    (3, 2,
     "Article 18 — what kind of titles cannot be conferred by State?\nతెలుగు: Art.18 ఏ బిరుదులు?",
     "Military titles", "Academic degrees",
     "All except military and academic / Military, Academic తప్ప (correct)",
     "Civilian awards (Bharat Ratna)",
     "c",
     "Art.18 abolishes TITLES (except military or academic distinctions). Aims to abolish hereditary titles (Maharaja, Nawab) and equivalents. SC in Balaji Raghavan (1996) upheld Bharat Ratna and Padma awards as NOT 'titles' — they are STATE RECOGNITION, not added to name. Art.18 also forbids citizens accepting foreign titles without President's consent."),

    (3, 2,
     "Article 17 — Right against Untouchability is what kind of right?\nతెలుగు: Art.17 ఏ రకం?",
     "Relative — restrictions apply",
     "Absolute — no restrictions / Absolute (correct)",
     "Depends on State", "Suspended in Emergency",
     "b",
     "Art.17 (Untouchability abolition) is an ABSOLUTE RIGHT — NO reasonable restrictions can be imposed. Available against STATE and PRIVATE PERSONS (horizontal application — unlike most FRs which apply mainly against State). One of few FRs operating against private persons."),

    (3, 3,
     "Indian citizen accepting foreign title needs whose consent?\nతెలుగు: విదేశీ బిరుదు ఎవరి అనుమతి?",
     "PM consent", "SC consent",
     "President of India / రాష్ట్రపతి అనుమతి (correct)",
     "Parliament approval",
     "c",
     "Art.18(2): No citizen of India shall accept any TITLE FROM ANY FOREIGN STATE. Art.18(4): Even non-citizens holding office of profit/trust under State cannot accept any present, emolument, office from foreign state without PRESIDENT'S consent. Aim: prevent foreign influence."),

    (3, 4,
     "SC/ST (Prevention of Atrocities) Act was enacted in?\nతెలుగు: SC/ST POA Act?",
     "1976", "1985",
     "1989 (correct)", "1995",
     "c",
     "SC/ST (PREVENTION OF ATROCITIES) ACT 1989 strengthens implementation of Art.17 — defines specific atrocities against SC/ST as criminal offences with stringent punishment. Special Courts. Amended 2015 (more offences, time-bound trial). Enforcement remains a major challenge."),

    # ───── Section 4: Article 19 — Six Freedoms ─────
    (4, 1,
     "How many freedoms are guaranteed under Article 19?\nతెలుగు: Art.19 స్వేచ్ఛలు?",
     "4", "5", "6 (correct)", "7",
     "c",
     "Currently 6 freedoms under Art.19(1): (a) speech & expression, (b) assemble peaceably, (c) form associations or unions or cooperative societies, (d) movement throughout India, (e) reside and settle anywhere in India, (g) practise any profession/occupation/trade/business. Originally 7; (f) Right to acquire, hold, dispose of property removed by 44th Am 1978."),

    (4, 1,
     "Article 19 freedoms apply to whom?\nతెలుగు: Art.19 ఎవరికి?",
     "All persons (citizens + aliens)",
     "Only citizens / కేవలం పౌరులకే (correct)",
     "Only citizens by birth", "Citizens and OCI holders",
     "b",
     "Art.19 freedoms are available ONLY TO CITIZENS — not to aliens (foreign nationals) or to corporations. Art.14, 20, 21, 22 (mostly) apply to all persons. Companies have separate corporate rights. OCI holders are NOT Indian citizens for FR purposes — only have privileges."),

    (4, 2,
     "What did 97th Amendment 2011 add to Article 19(1)(c)?\nతెలుగు: 97వ సవరణ?",
     "Unions", "Cooperative societies / సహకార సంఘాలు (correct)",
     "Political parties", "NGOs",
     "b",
     "97th Constitutional Amendment 2011: Added 'COOPERATIVE SOCIETIES' to Art.19(1)(c) — making formation of cooperative societies a FR. Also added Part IXB (Art.243ZH-243ZT) on cooperative societies. Aimed at strengthening cooperative movement. SC struck down Part IXB partially in Vipulbhai Chaudhary (2013)."),

    (4, 2,
     "Press Freedom is implied under which Article?\nతెలుగు: Press Freedom Article?",
     "Article 19(1)(a) (correct)", "Article 19(1)(b)",
     "Article 19(1)(c)", "Article 19(1)(g)",
     "a",
     "Press Freedom is NOT EXPRESSLY mentioned in Constitution. SC has held it is implicit in Art.19(1)(a) — Freedom of Speech and Expression. Romesh Thappar v. State of Madras (1950): Free press is essential to democracy. Subject to reasonable restrictions under Art.19(2)."),

    (4, 3,
     "Who can impose Reasonable Restrictions under Article 19?\nతెలుగు: Restrictions ఎవరు?",
     "Supreme Court", "President",
     "State (Centre/State governments) / State (correct)",
     "Parliament only",
     "c",
     "STATE (Centre and State governments through legislation) can impose REASONABLE RESTRICTIONS under Art.19(2)–(6). Grounds vary by clause — sovereignty/integrity, public order, decency, morality, contempt, defamation, incitement, etc. Restrictions must be: (a) by law, (b) reasonable, (c) for permitted grounds. Subject to JR."),

    (4, 4,
     "Article 19(1)(g) provides which freedom?\nతెలుగు: Art.19(1)(g)?",
     "Freedom of residence", "Freedom of assembly",
     "Freedom of profession/trade / వృత్తి/వ్యాపార స్వేచ్ఛ (correct)",
     "Freedom of association",
     "c",
     "Art.19(1)(g): Right to PRACTISE any PROFESSION, or to carry on any OCCUPATION, TRADE or BUSINESS. State may regulate via reasonable restrictions in interests of general public — including professional/technical qualifications and state monopoly on certain trades (Art.19(6)).",
     "UPSC"),

    # ───── Section 5: Articles 20, 21, 21A ─────
    (5, 1,
     "Right to Life under Article 21 applies to whom?\nతెలుగు: Art.21 ఎవరికి?",
     "Only citizens", "Citizens and OCI holders",
     "All persons — citizens + aliens / అందరికీ (correct)",
     "Only citizens by birth",
     "c",
     "Art.21 (Right to Life and Personal Liberty) applies to ALL PERSONS — Indian citizens AND foreigners (aliens). Same with Art.14, 20, 22 (mostly), 25-28. Most expansive FR — SC has read in: privacy, dignity, livelihood, health, environment, speedy trial, legal aid, education (pre-21A), shelter, etc."),

    (5, 1,
     "Right to Education under Article 21A covers what age?\nతెలుగు: Art.21A వయసు?",
     "5–14 years",
     "6–14 years / 6-14 సం. (correct)",
     "6–16 years", "5–18 years",
     "b",
     "Art.21A: State shall provide FREE AND COMPULSORY EDUCATION to all children of age 6 to 14 YEARS. Added by 86th Amendment 2002. Implemented through RIGHT TO EDUCATION (RTE) ACT 2009. Made elementary education a fundamental right (earlier was DPSP under Art.45)."),

    (5, 2,
     "Article 21A was added by which amendment?\nతెలుగు: Art.21A ఏ సవరణ?",
     "73rd Amendment 1992",
     "86th Amendment 2002 (correct)",
     "93rd Amendment 2005",
     "97th Amendment 2011",
     "b",
     "86th CONSTITUTIONAL AMENDMENT 2002 inserted: (1) Art.21A — Right to Education (6-14 years), (2) Art.45 amended (early childhood care under 6 years), (3) Art.51A(k) — fundamental duty for parents/guardians. RTE Act 2009 enacted to implement. Came into force 1 April 2010."),

    (5, 2,
     "'Double Jeopardy' protection in Article 20 borrowed from?\nతెలుగు: Double Jeopardy ఎక్కడ నుండి?",
     "UK", "USA / USA (correct)",
     "Canada", "Australia",
     "b",
     "Art.20(2) DOUBLE JEOPARDY: 'No person shall be PROSECUTED AND PUNISHED for the same offence MORE THAN ONCE.' Borrowed from US 5th AMENDMENT. Applies only to subsequent prosecution AFTER conviction — not to multiple investigations or to civil proceedings. Narrower than US version."),

    (5, 3,
     "Maneka Gandhi v. Union of India (1978) — impact on Article 21?\nతెలుగు: Maneka Gandhi 1978?",
     "Sought to repeal Art.21",
     "Held Art.21 limited to physical liberty",
     "Expanded Art.21 to include many rights / Art.21 విస్తరణ (correct)",
     "Art.21 only for criminal cases",
     "c",
     "Maneka Gandhi v. UoI (1978): LANDMARK case OVERRULED A.K. Gopalan (1950). Held that 'PROCEDURE ESTABLISHED BY LAW' under Art.21 must be FAIR, JUST AND REASONABLE — not arbitrary. Linked Art.14, 19, 21 as 'GOLDEN TRIANGLE'. Opened door for Art.21 to include privacy, dignity, livelihood, environment, etc. — vast expansion."),

    (5, 3,
     "Article 20(3) — Self-incrimination protection — correct statement?\nతెలుగు: Self-incrimination?",
     "DNA test on accused mandatory",
     "Accused cannot be compelled to give evidence against themselves / అభ్యోపి బలవంతంగా సాక్ష్యం (correct)",
     "Witnesses also protected",
     "Applies to civil cases too",
     "b",
     "Art.20(3): 'No person ACCUSED of any offence shall be COMPELLED to be a WITNESS AGAINST HIMSELF.' Protection against SELF-INCRIMINATION. Applies only to: (a) accused persons (not witnesses), (b) criminal cases (not civil), (c) testimonial compulsion (not physical evidence like fingerprints). Selvi v. State of Karnataka (2010): narcoanalysis/polygraph need consent.",
     "APPSC"),

    (5, 4,
     "Article 20 'Ex-post facto law' prohibition means?\nతెలుగు: Ex-post facto?",
     "Cannot impose greater penalty than law in force at time of offence / నేరం సమయం లో ఉన్న చట్టం కంటే ఎక్కువ శిక్ష లేదు (correct)",
     "Can apply law retrospectively",
     "Retrospective laws fully allowed",
     "Civil cases not covered",
     "a",
     "Art.20(1): EX-POST FACTO LAW prohibition — (a) No person convicted for an act not an offence under law in force when committed; (b) No GREATER PENALTY than the maximum prescribed by law in force at time of offence. Protects criminal accused from retroactive criminalisation/heavier punishment. Does NOT apply to civil/tax laws or to procedural changes.",
     "UPSC"),

    # ───── Section 6: Article 22 — Arrest & Detention ─────
    (6, 1,
     "Within what time must arrested person be produced before Magistrate?\nతెలుగు: అరెస్టు తర్వాత ఎన్ని గంటలు?",
     "12 hours",
     "24 hours / 24 గంటలు (correct)",
     "48 hours", "72 hours",
     "b",
     "Art.22(2): Every arrested person must be produced before nearest MAGISTRATE within 24 HOURS of arrest, EXCLUDING travel time. Failure renders detention illegal — habeas corpus available. Constitutional safeguard against arbitrary arrest. Doesn't apply to enemy aliens (Art.22(3)(a)) or preventive detention (Art.22(3)(b))."),

    (6, 1,
     "Maximum preventive detention without Advisory Board approval?\nతెలుగు: Advisory Board లేకుండా?",
     "1 month", "2 months",
     "3 months / 3 నెలలు (correct)",
     "6 months",
     "c",
     "Art.22(4): Person CANNOT be detained under Preventive Detention Law for more than 3 MONTHS unless an ADVISORY BOARD (consisting of HC judges/qualified persons) reports that there is sufficient cause for detention. 44th Amendment 1978 reduced this from earlier 3 months norm and added stricter safeguards.",
     "APPSC"),

    (6, 2,
     "Right of arrested person under Article 22 (ordinary arrest)?\nతెలుగు: Art.22 సాధారణ హక్కులు?",
     "Only Magistrate production",
     "Right to consult lawyer + know grounds of arrest / న్యాయవాది + అరెస్టు కారణాలు (correct)",
     "Bail right", "Free legal aid",
     "b",
     "Art.22(1) [for ORDINARY arrest, NOT preventive detention]: (a) Right to KNOW GROUNDS of arrest 'as soon as may be'; (b) Right to CONSULT and be DEFENDED by a legal practitioner of choice. Art.22(2): Production within 24 hours. Art.39A (DPSP) read with Art.21 also gives free legal aid."),

    (6, 2,
     "Article 22 protections do NOT apply to whom?\nతెలుగు: Art.22 ఎవరికి వర్తించదు?",
     "OBC categories",
     "Enemy aliens / శత్రు దేశ పౌరులు (correct)",
     "Minors", "Women",
     "b",
     "Art.22(3): Protections of Art.22(1)-(2) DO NOT apply to: (a) ENEMY ALIENS, (b) persons detained under PREVENTIVE DETENTION laws. Hence preventive detention has separate safeguards under Art.22(4)-(7). Art.22 effectively splits arrest into 'ordinary' (full safeguards) and 'preventive' (limited safeguards)."),

    (6, 3,
     "Maximum detention period under National Security Act 1980?\nతెలుగు: NSA 1980 గరిష్ట?",
     "3 months", "6 months",
     "12 months / 12 నెలలు (correct)",
     "24 months",
     "c",
     "NATIONAL SECURITY ACT (NSA) 1980: Provides for preventive detention up to 12 MONTHS (1 year). Grounds: prevent action prejudicial to defence, foreign relations, security, public order, supplies/services. Renewable. Subject to Advisory Board review. Other PD laws: COFEPOSA 1974, PIT-NDPS 1988, UAPA, state laws."),

    (6, 4,
     "Difference between Preventive and Punitive Detention?\nతెలుగు: Preventive vs Punitive?",
     "Same",
     "Preventive = pre-empt future crime; Punitive = punishment after conviction / Preventive = ముందస్తు; Punitive = నేరం తర్వాత (correct)",
     "Preventive = Court; Punitive = Govt",
     "Preventive = lifetime; Punitive = months",
     "b",
     "PREVENTIVE DETENTION: Detention BEFORE crime — to PREVENT person from committing prejudicial acts. No trial. Based on subjective satisfaction of authority. Brief duration. Done by EXECUTIVE under PD laws. PUNITIVE DETENTION: Imprisonment AFTER conviction in trial. Based on proof beyond reasonable doubt. Sentence as per law. By JUDICIARY.",
     "UPSC"),

    # ───── Section 7: PYQ Comprehensive ─────
    (7, 1,
     "Which FR cannot be suspended even during a National Emergency?\nతెలుగు: Emergency లో suspend కానిది?",
     "Article 19 — 6 Freedoms", "Article 14 — Equality",
     "Articles 20 and 21 / Art.20, 21 (correct)",
     "Article 22 — Protection against Arrest",
     "c",
     "Articles 20 and 21 CANNOT be suspended even during NE — guaranteed by 44th Amendment 1978 (Art.359(1) proviso). Reverses ADM Jabalpur (1976) which had allowed Art.21 suspension during 1975 Emergency. Art.19 auto-suspends only for War/External Aggression NEs (Art.358 — 44th Am narrowed). Other rights can be suspended via Art.359 Presidential Order.",
     "APPSC"),

    (7, 1,
     "Difference between 'Equality before law' and 'Equal protection of laws'?\nతెలుగు: రెండు తేడా?",
     "Same",
     "Equality before law = Negative (UK); Equal protection = Positive (USA) / UK Negative, USA Positive (correct)",
     "Equality before = Positive; Equal protection = Negative",
     "Both from USA",
     "b",
     "Article 14 has both: 'EQUALITY BEFORE LAW' = NEGATIVE concept from UK (Dicey's RULE OF LAW) — absence of special privileges. 'EQUAL PROTECTION OF LAWS' = POSITIVE concept from US 14th Amendment — equal treatment in equal circumstances; reasonable classification permitted. Together they ensure both formal and substantive equality.",
     "UPSC"),

    (7, 2,
     "Which right has been READ INTO Article 21 by Supreme Court?\nతెలుగు: Art.21 కింద చేర్చబడిన హక్కు?",
     "Right to vote", "Right to property",
     "Right to privacy / గోప్యత హక్కు (correct)",
     "Right to education for adults",
     "c",
     "RIGHT TO PRIVACY held to be FR under Art.21 in K.S. PUTTASWAMY v. UoI (2017) — 9-judge bench unanimous decision overruling earlier MP Sharma (1954) and Kharak Singh (1962) on this point. Other rights read into Art.21: livelihood (Olga Tellis 1985), health (Paschim Banga 1996), shelter, environment (MC Mehta), legal aid, speedy trial, dignity, education (now Art.21A), etc.",
     "APPSC"),

    (7, 2,
     "Articles 15(6) and 16(6) provide reservation for which category?\nతెలుగు: 15(6), 16(6) ఎవరికి?",
     "SC/ST", "OBC", "Minorities",
     "EWS (Economically Weaker Sections) / EWS (correct)",
     "d",
     "Articles 15(6) and 16(6) added by 103rd CONSTITUTIONAL AMENDMENT 2019 — provide 10% RESERVATION for ECONOMICALLY WEAKER SECTIONS (EWS) of unreserved categories. Eligibility: family income < ₹8 lakh, certain land/property limits. Validity upheld 3:2 in Janhit Abhiyan (Nov 2022) by Constitution Bench.",
     "APPSC"),

    (7, 3,
     "FRs apply only to citizens — is this correct?\nతెలుగు: FR అన్నీ పౌరులకే?",
     "Yes — all only to citizens",
     "No — Articles 14, 20, 21, 25-28 apply to all persons / కాదు, Art.14, 20, 21 అందరికీ (correct)",
     "Only with special permission",
     "Only OCI holders",
     "b",
     "FRs are NOT all citizen-only. ALL PERSONS (citizens + aliens): Art.14, 20, 21, 22 (mostly), 25, 27, 28. CITIZEN-ONLY: Art.15, 16, 19, 29(1), 30 (linguistic minorities). Companies/corporations are 'persons' for some FRs (Art.14, 19 to extent applicable to legal persons). NOT applicable to enemy aliens.",
     "UPSC"),

    (7, 4,
     "Which is the CORRECT Article-Subject pair?\nతెలుగు: సరైన జత?",
     "Article 17 — Abolition of Titles",
     "Article 18 — Abolition of Untouchability",
     "Article 21A — Right to Education 6-14 years (correct)",
     "Article 20 — Right to Life",
     "c",
     "CORRECT PAIRS: Art.17 = Abolition of UNTOUCHABILITY (not titles). Art.18 = Abolition of TITLES (not untouchability). Art.20 = Protection in respect of CONVICTION (ex-post facto, double jeopardy, self-incrimination) — NOT Right to Life. Art.21 = Right to Life and Personal Liberty. Art.21A = RIGHT TO EDUCATION 6-14 years (correct as stated).",
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
