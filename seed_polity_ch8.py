# seed_polity_ch8.py
# Chapter 8: Fundamental Rights (Part II)
# (ప్రాథమిక హక్కులు - రెండవ భాగం)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
# Total MCQs: 46 | PYQs: 7
# Format   : Bilingual (Telugu + English)
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# PYQ: 10th element (index 9) = 'APPSC' or 'UPSC'
# ─────────────────────────────────────────────

import json as _json

POLITY_CH8_MCQS = [

    # ══════════════════════════════════════════
    # SECTION 0 — Article 23: Forced Labour & Trafficking
    # ══════════════════════════════════════════

    # Easy
    (0, 1,
     "ఆర్టికల్ 23 దేనిని నిషేధిస్తుంది?\n(What does Article 23 prohibit?)",
     "పిల్లల చాకిరీ మాత్రమే / Child labour only",
     "మానవ అక్రమ రవాణా మరియు బలవంతపు శ్రమ (బేగారి) / Human trafficking and forced labour (begar)",
     "మత వివక్ష / Religious discrimination",
     "అంటరానితనం / Untouchability",
     "b",
     "ఆర్టికల్ 23 — Traffic in human beings (మానవ అక్రమ రవాణా) మరియు Begar (వేతనం లేకుండా బలవంతపు శ్రమ) నిషేధిస్తుంది. Citizens + Non-citizens అందరికీ రక్షణ.\nArticle 23 prohibits traffic in human beings and begar (unpaid forced work). Protection available to all — citizens and non-citizens alike."),

    (0, 1,
     "Bonded Labour System Abolition Act ఏ సంవత్సరం చేశారు?\n(In which year was the Bonded Labour System Abolition Act enacted?)",
     "1956", "1966", "1976", "1986",
     "c",
     "Bonded Labour System (Abolition) Act 1976 — వేతన బానిసత్వాన్ని రద్దు చేసింది. ఇది ఆర్టికల్ 23 అమలు చట్టం.\nBonded Labour System (Abolition) Act 1976 abolished bonded/wage slavery. It is an implementing legislation for Article 23. Immoral Traffic (Prevention) Act 1956 is also related to Art 23."),

    # Moderate
    (0, 2,
     "ఆర్టికల్ 23 ప్రకారం రాజ్యం compulsory service విధించగలదా?\n(Can the State impose compulsory service under Article 23?)",
     "ఏ కారణానికైనా విధించవచ్చు / Can impose for any reason",
     "Public purposes కోసం విధించవచ్చు — కానీ Religion/Race/Caste/Class వివక్ష లేకుండా / Yes for public purposes — but no discrimination on religion/race/caste/class",
     "అసలు విధించలేదు / Cannot impose at all",
     "కేవలం మహిళలకు మినహాయింపు / Only women are exempted",
     "b",
     "Art 23(2): State, public purposes (military/national service) కోసం compulsory service విధించవచ్చు — కానీ Religion, Race, Caste, Class ఆధారంగా వివక్ష చేయలేరు.\nUnder Art 23(2), the State can impose compulsory service for public purposes (e.g. military service) but must not discriminate on grounds of Religion, Race, Caste or Class."),

    (0, 2,
     "ఆర్టికల్ 23 ఎవరికి వర్తిస్తుంది?\n(Against whom is Article 23 enforceable?)",
     "కేవలం భారత పౌరులకు / Only Indian citizens",
     "కేవలం State కి వ్యతిరేకంగా / Only against the State",
     "అందరికీ (పౌరులు + అపౌరులు) వర్తిస్తుంది; Private individuals పైనా / All persons including non-citizens; enforceable against private individuals too",
     "కేవలం minority వర్గాలకు / Only minorities",
     "c",
     "Art 23 ఒక ప్రత్యేక FR — State మాత్రమే కాదు, Private individuals పైనా వర్తిస్తుంది. Citizens + Non-citizens అందరికీ రక్షణ.\nArt 23 is unique — it is enforceable against private individuals also, not just the State. It protects all persons — citizens and non-citizens alike."),

    # Tough — PUDR Case
    (0, 3,
     "People's Union for Democratic Rights v. Union of India (1982) కేసులో Supreme Court ఏమి నిర్ణయించింది?\n(What did SC hold in PUDR v. UOI 1982?)",
     "Art 23 కేవలం శారీరక బలవంతానికే వర్తిస్తుంది / Art 23 applies only to physical coercion",
     "Minimum wages చెల్లించకపోవడం = Art 23 కింద forced labour; economic compulsion సరిపోతుంది / Non-payment of minimum wages = forced labour; economic compulsion suffices",
     "Art 23 private individuals కు వర్తించదు / Art 23 does not apply to private individuals",
     "Forced labour కేవలం Govt employees కు వర్తిస్తుంది / Forced labour applies only to Govt employees",
     "b",
     "PUDR v. UOI (1982) — SC: Minimum wages చెల్లించకపోవడం = Art 23 కింద forced labour. Explicit physical coercion అవసరం లేదు — economic compulsion సరిపోతుంది.\nPUDR v. UOI (1982): SC held non-payment of minimum wages = forced labour under Art 23. Physical coercion is not required — economic compulsion (working under economic necessity without fair wages) is sufficient."),

    # Toughest
    (0, 4,
     "Assertion (A): Article 23 is enforceable against private individuals, not just the State.\nReason (R): Most Fundamental Rights are enforceable only against the State, but Article 23 creates an obligation on everyone.\n\nAssertion (A): ఆర్టికల్ 23 Private individuals పైనా అమలు పరచవచ్చు.\nReason (R): చాలా FRs State పైనే వర్తిస్తాయి, కానీ Art 23 అందరిపైనా వర్తిస్తుంది.",
     "A మరియు R రెండూ సరైనవి, R అనేది A కి సరైన వివరణ / Both correct, R explains A",
     "A మరియు R రెండూ సరైనవి, కానీ R వివరణ కాదు / Both correct, R does not explain A",
     "A సరైనది, R తప్పు / A correct, R wrong",
     "A తప్పు, R సరైనది / A wrong, R correct",
     "a",
     "Art 23 private individuals పైనా వర్తిస్తుంది (A — correct). ఇది చాలా FRs కంటే భిన్నం — చాలా FRs Art 12 State పైనే వర్తిస్తాయి (R — correct, explains A).\nArt 23 binds private individuals too (A — correct). This is unlike most FRs which apply only against the 'State' as defined in Art 12. R correctly explains why A is true."),

    # PYQ — APPSC
    (0, 2,
     "ఏ ఆర్టికల్ ప్రకారం బేగారి (Begar) మరియు బలవంతపు వెట్టి చాకిరీ నిషేధం? [APPSC Group 2]\n(Which article prohibits begar and other forms of forced labour?)",
     "ఆర్టికల్ 22 / Article 22", "ఆర్టికల్ 23 / Article 23",
     "ఆర్టికల్ 24 / Article 24", "ఆర్టికల్ 25 / Article 25",
     "b",
     "ఆర్టికల్ 23 — Traffic in human beings మరియు Begar (forced labour) నిషేధిస్తుంది. APPSC లో ఇది తరచుగా వచ్చే ప్రశ్న. Bonded Labour System Abolition Act 1976 దీని అమలు చట్టం.\nArticle 23 prohibits traffic in human beings and begar. Bonded Labour System (Abolition) Act 1976 is the implementing law. Frequently asked in APPSC Group 2.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 1 — Article 24: Child Labour
    # ══════════════════════════════════════════

    # Easy
    (1, 1,
     "ఆర్టికల్ 24 ప్రకారం ఏ వయసు వరకు పిల్లలను factories మరియు mines లో పని చేయించరాదు?\n(Below what age does Article 24 prohibit employment in factories and mines?)",
     "12 సంవత్సరాల కంటే తక్కువ / Below 12",
     "14 సంవత్సరాల కంటే తక్కువ / Below 14",
     "16 సంవత్సరాల కంటే తక్కువ / Below 16",
     "18 సంవత్సరాల కంటే తక్కువ / Below 18",
     "b",
     "ఆర్టికల్ 24 — 14 సంవత్సరాల కంటే తక్కువ వయసు పిల్లలను Factories, Mines లేదా hazardous employment లో పని చేయించరాదు.\nArticle 24 prohibits employment of children below 14 years of age in factories, mines or any hazardous employment. Child Labour (Prohibition & Regulation) Act 1986 implements this."),

    # Moderate
    (1, 2,
     "2016 Child Labour Amendment Act ప్రకారం 14-18 సంవత్సరాల పిల్లలకు ఏ పని నిషేధం?\n(Under the 2016 Amendment, what work is prohibited for children aged 14–18?)",
     "అన్ని రకాల పని / All types of work",
     "Hazardous employment (ప్రమాదకరమైన పని) మాత్రమే / Only hazardous employment",
     "Factory work మాత్రమే / Only factory work",
     "Government work మాత్రమే / Only government work",
     "b",
     "2016 Amendment: 14 కింద పిల్లలు — అన్ని occupations నిషేధం. 14-18 సంవత్సరాల మధ్య — Hazardous employment నిషేధం; family enterprises మరియు entertainment (non-hazardous) లో exemption.\n2016 Amendment: Children below 14 — banned from ALL occupations. Children 14–18 — banned from hazardous employment only; family/entertainment work exempted if non-hazardous."),

    # Tough
    (1, 3,
     "ఆర్టికల్ 24 మరియు ఆర్టికల్ 21A తో సంబంధం ఏమిటి?\n(What is the connection between Article 24 and Article 21A?)",
     "రెండూ అసంబంధం / Both are unrelated",
     "Art 21A (86th Amdt 2002) = 6-14 పిల్లలకు ఉచిత విద్య; Art 24 = 14 కింద పిల్లలను hazardous work నుండి రక్షిస్తుంది — రెండూ కలిసి child protection framework / Art 21A = free education 6-14; Art 24 = protection from hazardous work — together form child protection",
     "Art 21A = child labour నిషేధం / Art 21A = child labour prohibition",
     "Art 24 = పిల్లలకు ఉచిత విద్య / Art 24 = free education for children",
     "b",
     "Art 24 = hazardous work నుండి రక్షణ (14 కింద). Art 21A (86th Amendment 2002) = 6-14 వయసు పిల్లలకు ఉచిత నిర్బంధ విద్య హక్కు. RTE Act 2009 దీనిని అమలు చేస్తుంది.\nArt 24 protects children below 14 from hazardous work. Art 21A (86th Amdt 2002) gives the right to free and compulsory education for ages 6–14. Together they form a comprehensive child protection framework."),

    # PYQ — APPSC
    (1, 2,
     "ఏ ఆర్టికల్ 14 సంవత్సరాల కంటే తక్కువ వయసు పిల్లలను కర్మాగారాల్లో పని చేయించడాన్ని నిషేధిస్తుంది? [APPSC Group 2]\n(Which article prohibits employment of children below 14 in factories?)",
     "ఆర్టికల్ 23 / Article 23", "ఆర్టికల్ 24 / Article 24",
     "ఆర్టికల్ 25 / Article 25", "ఆర్టికల్ 21A / Article 21A",
     "b",
     "ఆర్టికల్ 24 — 14 కింద పిల్లలను Factories, Mines, Hazardous employment లో నిషేధిస్తుంది. Art 23 = Forced Labour; Art 21A = Right to Education (6-14).\nArticle 24 prohibits employment of children below 14 in factories, mines or hazardous work. Art 23 = forced labour; Art 21A = right to education. Frequently asked in APPSC Group 2.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 2 — Articles 25 & 26: Freedom of Religion
    # ══════════════════════════════════════════

    # Easy
    (2, 1,
     "ఆర్టికల్ 25 ఏ హక్కును కల్పిస్తుంది?\n(What right does Article 25 guarantee?)",
     "మత స్థాపన మాత్రమే / Only right to establish religion",
     "స్వేచ్ఛగా మత ఆచరణ, ప్రచారం — Freedom of conscience and free profession, practice and propagation of religion",
     "అన్ని మతాలకు రాజ్య మద్దతు / State support to all religions",
     "మతపరమైన న్యాయస్థానాలు / Religious courts",
     "b",
     "ఆర్టికల్ 25 — Freedom of conscience and free profession, practice and propagation of religion. Citizens + non-citizens అందరికీ. Subject to: Public order, Morality, Health.\nArticle 25 guarantees freedom of conscience, profession, practice and propagation of religion to ALL persons (citizens + non-citizens), subject to public order, morality and health."),

    (2, 1,
     "Shirur Math Case (1954) ఏ విషయంలో ముఖ్యమైనది?\n(Why is the Shirur Math Case 1954 significant?)",
     "మైనారిటీ విద్యా సంస్థల స్థాపన / Minority educational institutions",
     "Matters of religion (రక్షించబడినవి) vs Secular activities (State regulate చేయగలవు) distinction — both Art 25 & 26",
     "Art 17 అంటరానితనం నిర్వచనం / Untouchability definition",
     "Citizenship నిర్వచనం / Citizenship definition",
     "b",
     "Shirur Math Case 1954 — SC: 'Matter of religion' = courts రక్షిస్తాయి (protected); 'Secular activities of religion' = State regulate చేయవచ్చు. ఇది Art 25 & 26 వ్యాఖ్యానంలో landmark case.\nShirur Math (1954): SC drew distinction between 'matter essentially religious' (protected under Art 25/26) and 'secular activities associated with religion' (State can regulate). Landmark for interpreting religious freedom."),

    # Moderate — Propagation
    (2, 2,
     "Rev Stainislaus v. State of Madhya Pradesh (1977) కేసులో SC ఏమి నిర్ణయించింది?\n(What did SC hold in Rev Stainislaus v. State of MP 1977?)",
     "Art 25 ప్రకారం బలవంతంగా మత మార్పిడి చేయించే హక్కు ఉంది / Art 25 includes right to forcibly convert others",
     "Art 25 లో 'Propagation' = persuasion/teaching ద్వారా మత ప్రచారం; force/fraud/allurement ద్వారా conversion హక్కు కాదు / 'Propagation' = sharing by persuasion; no right to convert by force/fraud",
     "State anti-conversion laws రాజ్యాంగ విరుద్ధం / State anti-conversion laws are unconstitutional",
     "'Propagation' అంటే conversion తో సమానం / 'Propagation' means the same as conversion",
     "b",
     "Rev Stainislaus 1977 — SC: Art 25 లో 'Propagation' = peaceful sharing/teaching of religious beliefs (ALLOWED). Force/Fraud/Allurement ద్వారా మత మార్పిడి = Art 25 లో లేదు. State anti-conversion laws = Valid.\n'Propagation' under Art 25 means sharing/explaining religious beliefs through persuasion. It does NOT include a right to convert others by force, fraud or allurement. State anti-conversion laws are constitutionally valid."),

    (2, 2,
     "ఆర్టికల్ 26 ప్రకారం religious denominations కు ఏ హక్కులు ఉన్నాయి?\n(What rights do religious denominations have under Article 26?)",
     "మత పన్నులు వసూలు చేయడం / Collect religious taxes",
     "మత/దానధర్మ సంస్థలు స్థాపించడం, మత వ్యవహారాలు నిర్వహించడం, property సంపాదించి నిర్వహించడం / Establish institutions, manage religious affairs, acquire and administer property",
     "రాష్ట్ర పాఠశాలల్లో మత బోధన / Religious instruction in state schools",
     "రాజ్యాంగ సవరణ చేయడం / Amend the Constitution",
     "b",
     "Art 26 — 'Denomination' అంటే ఒక మతానికి చెందిన విభాగం (e.g., Shaivites/Vaishnavites in Hinduism). Denominations కు 4 హక్కులు: (a) institutions స్థాపన, (b) మత వ్యవహారాల నిర్వహణ, (c) property సంపాదన, (d) property నిర్వహణ. Subject to public order, morality, health.\nArt 26 gives religious denominations (a section of a religion with distinct beliefs/practices) 4 rights: establish institutions, manage religious affairs, acquire and administer property — subject to public order, morality and health."),

    # Tough
    (2, 3,
     "ఆర్టికల్ 25(2)(b) ప్రకారం State ఏమి చేయగలదు?\n(What can the State do under Article 25(2)(b)?)",
     "అన్ని మతాలను నిషేధించవచ్చు / Prohibit all religions",
     "Hindu temples అన్ని వర్గాలకు (SCs/STs తో సహా) తెరవాలని చట్టం చేయవచ్చు / Make laws throwing open Hindu temples to all Hindus including SCs/STs",
     "Government schools లో Hinduism బోధించవచ్చు / Teach Hinduism in government schools",
     "Minority religions ని regulate చేయలేదు / Cannot regulate minority religions",
     "b",
     "Art 25(2)(b): State can make laws providing for social welfare/reform including throwing open Hindu religious institutions to all Hindus (including SCs/STs). Temple Entry laws draw their constitutional basis from here.\nArt 25(2)(b) allows the State to make laws for social reform — including laws that open Hindu temples to all sections of Hindus including SCs/STs. This is the constitutional basis for temple entry legislation."),

    # PYQ — UPSC
    (2, 2,
     "అధికరణం 25 గురించి సరైనది ఏది? / Which of the following is correct about Article 25 of the Indian Constitution? [UPSC Style]",
     "It is available only to Indian citizens / భారత పౌరులకు మాత్రమే",
     "It is subject to public order, morality and health / ఇది public order, morality, health కి లోబడి ఉంటుంది",
     "It prohibits propagation of religion / మత ప్రచారాన్ని నిషేధిస్తుంది",
     "It prevents the State from regulating secular activities / రాజ్యం secular activities regulate చేయలేదు",
     "b",
     "Art 25 — Freedom of religion, subject to: Public order, Morality, Health, and other FR provisions. Citizens + non-citizens రెండింటికీ వర్తిస్తుంది. 'Propagation' = allowed; forced conversion = not allowed.\nArt 25 is available to all persons (citizens + non-citizens), subject to public order, morality and health. Propagation of religion is allowed; State can regulate secular activities associated with religion.",
     "UPSC"),

    # ══════════════════════════════════════════
    # SECTION 3 — Articles 27 & 28
    # ══════════════════════════════════════════

    # Easy
    (3, 1,
     "ఆర్టికల్ 27 ప్రకారం ఏ పని నిషేధం?\n(What does Article 27 prohibit?)",
     "మతాన్ని ఆచరించడం / Practising religion",
     "ఒక నిర్దిష్ట మతాన్ని ప్రచారం చేయడానికి పన్నులు వసూలు చేయడం / Compelling payment of taxes for promotion of any particular religion",
     "Government schools లో మత బోధన / Religious instruction in Govt schools",
     "Minority schools స్థాపించడం / Establishing minority schools",
     "b",
     "Art 27 — ఏ పౌరుడూ ఒక నిర్దిష్ట మతాన్ని ప్రచారం చేయడానికి / నిర్వహించడానికి Tax చెల్లించేలా బలవంతం చేయలేరు. Secular purposes కోసం fees = OK.\nArt 27 prohibits compelling any person to pay taxes for promotion or maintenance of any particular religion. Fees for secular purposes (e.g. road near a temple) are allowed."),

    (3, 1,
     "ఆర్టికల్ 28 ప్రకారం ఏ రకం పాఠశాలల్లో మత బోధన పూర్తిగా నిషేధం?\n(In which type of schools is religious instruction completely prohibited under Article 28?)",
     "State recognized schools / రాజ్య గుర్తింపు పొందిన పాఠశాలలు",
     "Minority schools / మైనారిటీ పాఠశాలలు",
     "Wholly State maintained schools (పూర్తిగా రాజ్య నిధులతో నడిచే) / Wholly maintained by State funds",
     "Aided schools / సహాయక పాఠశాలలు",
     "c",
     "Art 28 — Wholly State maintained schools లో మత బోధన పూర్తిగా నిషేధం. State aided schools లో మత బోధన ఐచ్ఛికం (consent అవసరం). Trust/endowment schools — మత బోధన అనుమతి. Minority schools — పూర్తి స్వేచ్ఛ.\nArt 28: Wholly State-maintained schools — religious instruction completely prohibited. State-aided schools — optional (consent needed). Trust/endowment schools — allowed. Minority schools — full freedom."),

    # Moderate
    (3, 2,
     "ఆర్టికల్ 28 ప్రకారం 'Consent' నిబంధన ఏమిటి?\n(What is the consent requirement under Article 28?)",
     "మత బోధనకు రాష్ట్ర అనుమతి అవసరం / State permission needed",
     "విద్యార్థులు మత బోధన / ఆచరణకు హాజరు కావాలంటే వారి (లేదా guardian) consent తప్పనిసరి / Consent of student (or guardian if minor) mandatory to attend religious instruction/worship",
     "మత బోధనకు court అనుమతి అవసరం / Court permission needed",
     "పేరెంట్లు తప్పనిసరిగా మత బోధనకు అనుమతి ఇవ్వాలి / Parents must compulsorily permit",
     "b",
     "Art 28(3): ఏ state-recognised లేదా state-aided educational institution లోనూ ఏ వ్యక్తిని వారి (లేదా minor అయితే guardian) consent లేకుండా మత బోధన / ఆచరణలో పాల్గొనేలా బలవంతం చేయలేరు.\nArt 28(3): No person attending any state-recognised or state-aided institution shall be required to take part in any religious instruction or worship without their own consent (or guardian's consent if a minor)."),

    # ══════════════════════════════════════════
    # SECTION 4 — Articles 29 & 30
    # ══════════════════════════════════════════

    # Easy
    (4, 1,
     "ఆర్టికల్ 30 ప్రకారం minority educational institutions స్థాపించే హక్కు ఎవరికి ఉంది?\n(Who has the right to establish minority educational institutions under Article 30?)",
     "కేవలం మత మైనారిటీలకు / Only religious minorities",
     "కేవలం భాషా మైనారిటీలకు / Only linguistic minorities",
     "అన్ని మత మరియు భాషా మైనారిటీలకు / All minorities — religious OR linguistic",
     "కేవలం Scheduled Castes కు / Only Scheduled Castes",
     "c",
     "Art 30(1): All minorities, whether based on religion OR language, shall have the right to establish and administer educational institutions. ఇది మత మైనారిటీలు + భాషా మైనారిటీలు ఇద్దరికీ వర్తిస్తుంది.\nArt 30(1) covers BOTH religious minorities and linguistic minorities — both have the right to establish and administer educational institutions of their choice."),

    (4, 1,
     "TMA Pai Foundation Case (2002) దేనికి సంబంధించినది?\n(What is the TMA Pai Foundation Case 2002 about?)",
     "Preamble amendment / ప్రస్తావన సవరణ",
     "Minority status is determined STATE-WISE — not nationwide / మైనారిటీ హోదా రాష్ట్ర స్థాయిలో నిర్ణయిస్తారు",
     "Art 21 interpretation / ఆర్టికల్ 21 వ్యాఖ్యానం",
     "Presidential election / రాష్ట్రపతి ఎన్నిక",
     "b",
     "TMA Pai Foundation Case 2002 — SC: Minority status రాష్ట్ర స్థాయిలో నిర్ణయిస్తారు. ఒక సంస్థ ఒక రాష్ట్రంలో minority, వేరే రాష్ట్రంలో majority కావచ్చు. ఉదా: Sikhs — Punjab లో majority, other states లో minority.\nTMA Pai Foundation (2002): Minority status is determined STATE-WISE, not nationwide. Thus Sikhs are a majority in Punjab but a minority in other states. Minority education institutions determined accordingly."),

    # Moderate
    (4, 2,
     "ఆర్టికల్ 29(2) ప్రకారం రాజ్య సహాయం పొందే విద్యా సంస్థలలో ప్రవేశ నిరాకరణ ఏ ఆధారాలపై నిషేధం?\n(On what grounds is denial of admission in state-aided institutions prohibited under Art 29(2)?)",
     "కేవలం religion మరియు caste / Only religion and caste",
     "Religion, Race, Caste, Language / మతం, జాతి, కులం, భాష",
     "Religion మాత్రమే / Religion only",
     "Caste మరియు Language మాత్రమే / Only caste and language",
     "b",
     "Art 29(2): ఏ పౌరుడికీ state maintained లేదా state aided educational institution లో ప్రవేశం Religion, Race, Caste, Language ఆధారాలపై నిరాకరించరాదు.\nArt 29(2): No citizen shall be denied admission to any state-maintained or state-aided educational institution on grounds of Religion, Race, Caste or Language. This is a fundamental guarantee applicable to all citizens."),

    # Tough
    (4, 3,
     "ఆర్టికల్ 29 మరియు ఆర్టికల్ 30 మధ్య ముఖ్యమైన వ్యత్యాసం ఏమిటి?\n(Key distinction between Article 29 and Article 30?)",
     "రెండూ కేవలం minorities కు మాత్రమే / Both apply only to minorities",
     "Art 29 = 'any section of citizens' (minorities + others); Art 30 = only minorities (religious/linguistic) / Art 29 covers all sections including majority; Art 30 only minorities",
     "Art 30 = 'any section of citizens'; Art 29 = only minorities / Reverse",
     "రెండూ ఒకటే / Both identical",
     "b",
     "Art 29: 'Any section of citizens' — minorities తో పాటు majorities కూడా language/culture రక్షించుకోవచ్చు. Art 30: 'All minorities' — specifically minorities (religious OR linguistic) మాత్రమే education institutions స్థాపించగలరు. ఇది exam లో తరచుగా అడిగే వ్యత్యాసం.\nArt 29 applies to 'any section of citizens' (including majorities) for conserving language/culture. Art 30 applies specifically to 'minorities' (religious or linguistic) for establishing and administering educational institutions."),

    # PYQ — APPSC
    (4, 2,
     "ఏ ఆర్టికల్ మైనారిటీలకు విద్యా సంస్థలు స్థాపించే మరియు నిర్వహించే హక్కు కల్పిస్తుంది? [APPSC Group 2]\n(Which article gives minorities the right to establish and administer educational institutions?)",
     "ఆర్టికల్ 28 / Article 28", "ఆర్టికల్ 29 / Article 29",
     "ఆర్టికల్ 30 / Article 30", "ఆర్టికల్ 31 / Article 31",
     "c",
     "ఆర్టికల్ 30 — అన్ని మత మరియు భాషా మైనారిటీలకు విద్యా సంస్థలు స్థాపించే మరియు నిర్వహించే హక్కు. State సహాయం ఇవ్వడంలో minority institutions తో వివక్ష చూపరాదు.\nArticle 30 guarantees all religious and linguistic minorities the right to establish and administer educational institutions. The State cannot discriminate against them while granting aid. Frequently asked in APPSC Group 2.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 5 — Articles 31A, 31B, 31C
    # ══════════════════════════════════════════

    # Easy
    (5, 1,
     "Ninth Schedule (నవమ షెడ్యూల్) ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చారు?\n(By which amendment was the Ninth Schedule added?)",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "1వ సవరణ 1951 / 1st Amendment 1951",
     "44వ సవరణ 1978 / 44th Amendment 1978",
     "25వ సవరణ 1971 / 25th Amendment 1971",
     "b",
     "Ninth Schedule ను 1వ రాజ్యాంగ సవరణ 1951 ద్వారా చేర్చారు. భూసంస్కరణ చట్టాలను court challenges నుండి రక్షించడం దీని ఉద్దేశం.\nNinth Schedule was added by the 1st Constitutional Amendment 1951. Its purpose was to protect land reform laws from judicial challenge. Currently 280+ laws are in the Ninth Schedule."),

    # Moderate
    (5, 2,
     "IR Coelho Case (2007) లో Supreme Court ఏమి నిర్ణయించింది?\n(What did SC hold in IR Coelho Case 2007?)",
     "Ninth Schedule లోని అన్ని చట్టాలు challenge చేయలేమని / All Ninth Schedule laws are immune",
     "April 24, 1973 తర్వాత Ninth Schedule లో చేర్చిన చట్టాలు Basic Structure violate చేస్తే challenge చేయవచ్చు / Laws added after April 24, 1973 can be challenged if they violate Basic Structure",
     "Ninth Schedule రద్దు చేయాలని / Ninth Schedule should be abolished",
     "Art 31B రాజ్యాంగ వ్యతిరేకం / Art 31B is unconstitutional",
     "b",
     "IR Coelho Case 2007 (9-judge bench): April 24, 1973 (Kesavananda Bharati date) తర్వాత Ninth Schedule లో చేర్చిన చట్టాలు — Basic Structure violate చేస్తే challenge చేయవచ్చు. ముందు చేర్చినవి పూర్తిగా immune.\nIR Coelho (2007): Laws added to Ninth Schedule AFTER April 24, 1973 (Kesavananda Bharati date) can be challenged if they violate the Basic Structure. Laws added before that date remain immune from judicial challenge."),

    # Tough
    (5, 3,
     "ఆర్టికల్ 31C (25th Amendment 1971) ప్రకారం ఏ DPSPs అమలు చేసే చట్టాలు Art 14 & 19 ఆధారంగా challenge చేయలేరు?\n(Laws implementing which DPSPs are protected under Art 31C from challenge under Art 14 & 19?)",
     "Art 38 మరియు 40 / Art 38 and 40",
     "Art 39(b) మరియు 39(c) / Art 39(b) and 39(c)",
     "Art 44 మరియు 45 / Art 44 and 45",
     "Art 36 మరియు 37 / Art 36 and 37",
     "b",
     "Art 31C (25th Amendment 1971): Laws implementing DPSP Art 39(b) (distribution of material resources) మరియు Art 39(c) (prevention of concentration of wealth) — Art 14 & 19 ఆధారంగా challenge చేయలేరు. Kesavananda (1973) struck down absolute immunity clause.\nArt 31C protects laws implementing DPSP Art 39(b) (equitable distribution of material resources) and 39(c) (prevention of wealth concentration) from challenge under Art 14 & 19. Kesavananda (1973) struck down the part that totally excluded judicial review."),

    # ══════════════════════════════════════════
    # SECTION 6 — Article 32: Remedies & 5 Writs
    # ══════════════════════════════════════════

    # Easy
    (6, 1,
     "Dr. B.R. Ambedkar ఆర్టికల్ 32 ని ఏమని పిలిచారు?\n(How did Dr. Ambedkar describe Article 32?)",
     "రాజ్యాంగం యొక్క పాదపీఠం / Foot of Constitution",
     "రాజ్యాంగం యొక్క హృదయం మరియు ఆత్మ / Heart and Soul of the Constitution",
     "రాజ్యాంగం యొక్క మేల్కట్ట / Superstructure of Constitution",
     "రాజ్యాంగం యొక్క పరిచయం / Introduction of Constitution",
     "b",
     "Dr. B.R. Ambedkar: 'The most important Article — the very soul and heart of the Constitution.' Art 32 లేకుండా FRs కేవలం అర్థం లేని మాటలు అవుతాయి.\nDr. Ambedkar called Art 32 'the most important article — the very soul and heart of the Constitution.' Without it, Fundamental Rights would be meaningless — it is the mechanism to enforce them."),

    (6, 1,
     "Habeas Corpus రిట్ దేనికి వాడతారు?\n(What is the Habeas Corpus writ used for?)",
     "Public official కి legal duty చేయమని / Compel official to perform duty",
     "అక్రమ నిర్బంధం నుండి వ్యక్తిని విడుదల చేయడానికి / Release a person from illegal detention",
     "Inferior court decision రద్దు చేయడానికి / Quash inferior court's decision",
     "Public office అక్రమ ఆక్రమణను సవాలు చేయడానికి / Challenge unlawful office occupancy",
     "b",
     "Habeas Corpus ('You shall have the body') — అత్యంత ముఖ్యమైన రిట్. అక్రమంగా నిర్బంధించిన వ్యక్తిని court ముందు హాజరు పరచమని ఆదేశిస్తుంది. Citizens + non-citizens రెండింటికీ వర్తిస్తుంది.\nHabeas Corpus ('You shall have the body') — most important writ. Directs production of an illegally detained person before the court. Available to all — citizens and non-citizens."),

    (6, 1,
     "Mandamus రిట్ ఎవరికి వ్యతిరేకంగా వేయలేరు?\n(Against whom can Mandamus NOT be issued?)",
     "District Collector / జిల్లా కలెక్టర్",
     "Public Corporation / పబ్లిక్ కార్పొరేషన్",
     "President of India లేదా Governor of a State / రాష్ట్రపతి లేదా గవర్నర్",
     "Municipal Commissioner / మునిసిపల్ కమిషనర్",
     "c",
     "Mandamus రిట్ President of India లేదా Governor of a State కి వ్యతిరేకంగా వేయలేరు. అలాగే private individuals కి వ్యతిరేకంగా కూడా వేయలేరు. Only against public officials/bodies to perform their legal duties.\nMandamus cannot be issued against the President of India or the Governor of a State. It also cannot be issued against private individuals or bodies — only against public officials or bodies with a legally enforceable duty."),

    # Moderate
    (6, 2,
     "Prohibition మరియు Certiorari రిట్‌ల మధ్య ముఖ్య వ్యత్యాసం ఏమిటి?\n(Key difference between Prohibition and Certiorari writs?)",
     "రెండూ ఒకటే ఉపయోగం / Both serve the same purpose",
     "Prohibition = decision కి ముందు (BEFORE decision); Certiorari = decision తర్వాత (AFTER decision) — రెండూ judicial/quasi-judicial bodies పై మాత్రమే / Prohibition before; Certiorari after decision",
     "Certiorari = decision కి ముందు; Prohibition = తర్వాత / Reverse order",
     "రెండూ Private individuals పై వేయవచ్చు / Both can be issued against private individuals",
     "b",
     "Prohibition: Inferior court jurisdiction దాటకుండా ముందే ఆపడానికి (before decision). Certiorari: Inferior court decision తర్వాత రద్దు చేయడానికి (after decision). రెండూ judicial/quasi-judicial bodies పై మాత్రమే; administrative bodies పై వేయలేరు.\nProhibition prevents an inferior court from exceeding its jurisdiction BEFORE a decision is made. Certiorari quashes a decision AFTER it is made. Both apply only to judicial or quasi-judicial bodies, not to administrative bodies."),

    (6, 2,
     "Quo Warranto రిట్ file చేయడానికి ఎవరికి అర్హత ఉంటుంది?\n(Who has locus standi to file Quo Warranto?)",
     "కేవలం aggrieved person మాత్రమే / Only aggrieved party",
     "Public office తో directly సంబంధమున్న వ్యక్తులు మాత్రమే / Only persons directly affected",
     "ఏ సభ్యుడైనా — Any member of public (aggrieved party అవసరం లేదు) / Any member of the public — no aggrieved party required",
     "కేవలం Attorney General మాత్రమే / Only Attorney General",
     "c",
     "Quo Warranto లో locus standi (standing) విస్తృతం — ఏ సభ్యుడైనా (any member of public) file చేయవచ్చు; aggrieved party అవసరం లేదు. Public office అక్రమంగా ఆక్రమించడం = public interest matter.\nQuo Warranto has wide locus standi — ANY member of the public can file it without being an aggrieved party. This is unlike Mandamus/Certiorari which require an aggrieved party. It reflects the public interest in lawful occupancy of public office."),

    # Tough
    (6, 3,
     "Art 32 (SC writs) మరియు Art 226 (HC writs) మధ్య ముఖ్య వ్యత్యాసం ఏమిటి?\n(Key difference between Art 32 SC writs and Art 226 HC writs?)",
     "Art 32 scope విస్తృతం; Art 226 scope తక్కువ / Art 32 wider",
     "Art 226 (HC) scope విస్తృతం — FR violations + any other purpose; Art 32 (SC) = only FR enforcement / HC wider; SC only for FR",
     "రెండూ ఒకే scope / Same scope",
     "Art 226 పై Art 32 superior / Art 32 superior to Art 226",
     "b",
     "Art 32 (Supreme Court): Only for enforcement of Fundamental Rights. Art 226 (High Courts): Writs for FR violations + 'any other purpose' — wider scope. కానీ Art 32 under SC = more authoritative.\nArt 226 (HC) has WIDER jurisdiction — it can issue writs for FR violations AND for any other purpose (e.g. ordinary legal rights). Art 32 (SC) can only be invoked for enforcement of Fundamental Rights. However, SC writs are more authoritative."),

    # PYQ — UPSC
    (6, 2,
     "అధికారాన్ని మించి వ్యవహరించకుండా ఏ రిట్ ఇస్తారు? / Which of the following writs is issued to an inferior court to prevent it from exceeding its jurisdiction? [UPSC Style]",
     "Habeas Corpus", "Mandamus", "Prohibition", "Certiorari",
     "c",
     "Prohibition writ = inferior court jurisdiction exceed అవ్వకుండా ముందే ఆపడం (BEFORE decision is made). Certiorari = inferior court decision తర్వాత రద్దు చేయడం (AFTER decision).\nProhibition prevents an inferior court from exceeding its jurisdiction BEFORE a decision. Certiorari quashes a decision AFTER it has been made. Habeas Corpus = illegal detention. Mandamus = compel public duty.",
     "UPSC"),

    # PYQ — APPSC
    (6, 2,
     "ఏ రిట్ ని 'అత్యంత ముఖ్యమైన రిట్' గా పరిగణిస్తారు? [APPSC Group 2]\n(Which writ is considered the most important?)",
     "Mandamus — legal duty నిర్వహణ కోసం / Mandamus",
     "Habeas Corpus — అక్రమ నిర్బంధం నుండి విముక్తి కోసం; వ్యక్తి స్వేచ్ఛను రక్షిస్తుంది / Habeas Corpus — protects personal liberty",
     "Certiorari — court decisions రద్దు కోసం / Certiorari",
     "Quo Warranto — office నుండి తొలగించడం కోసం / Quo Warranto",
     "b",
     "Habeas Corpus = most important writ. వ్యక్తి స్వేచ్ఛ (personal liberty) కాపాడటానికి వాడే అత్యంత ముఖ్యమైన రక్షణ సాధనం. Citizens + Non-citizens అందరికీ వర్తిస్తుంది.\nHabeas Corpus is the most important writ — it safeguards personal liberty by ordering the release of an illegally detained person. It applies to all — citizens and non-citizens. Frequently asked in APPSC Group 2.",
     "APPSC"),

    # ══════════════════════════════════════════
    # SECTION 7 — Articles 33, 34, 35 & Emergency FR Suspension
    # ══════════════════════════════════════════

    # Easy
    (7, 1,
     "ఆర్టికల్ 35 ప్రకారం Part III FRs కోసం చట్టాలు చేసే అధికారం ఎవరికి ఉంది?\n(Who has power to make laws to enforce Part III FRs under Art 35?)",
     "రాష్ట్ర శాసనసభలు మాత్రమే / State legislatures only",
     "Parliament మాత్రమే (State legislatures కాదు) / Parliament only (not state legislatures)",
     "రాష్ట్రపతి మాత్రమే / President only",
     "Supreme Court / Supreme Court",
     "b",
     "Art 35: ONLY Parliament (not state legislatures) can make laws to prescribe punishments for violations of Art 17 (Untouchability) & Art 23 (Forced Labour), and make laws for Art 16(3), 32(3), 33, 34.\nArt 35: Only Parliament (NOT state legislatures) can make laws to enforce certain provisions of Part III, including prescribing punishment for violations of Art 17 (untouchability) and Art 23 (forced labour)."),

    # Moderate
    (7, 2,
     "National Emergency (Art 352) మరియు Art 359 time లో ఏ FRs suspend చేయలేరు?\n(Which FRs can NEVER be suspended even during Emergency?)",
     "Art 14 మరియు Art 19 / Art 14 and Art 19",
     "Art 17 మరియు Art 32 / Art 17 and Art 32",
     "Art 20 మరియు Art 21 / Art 20 and Art 21",
     "Art 25 మరియు Art 30 / Art 25 and Art 30",
     "c",
     "Art 20 (Protection against conviction) మరియు Art 21 (Right to life & personal liberty) — ఎట్టి పరిస్థితుల్లోనూ suspend చేయలేరు. National Emergency లో Art 19 automatically suspended. Art 359 ద్వారా other FRs suspend చేయవచ్చు కానీ Art 20 & 21 కాదు.\nArt 20 (protection against double jeopardy/self-incrimination) and Art 21 (right to life & liberty) can NEVER be suspended — not even during a National Emergency. Art 19 is automatically suspended under Art 352. Other FRs may be suspended by Presidential Order under Art 359, except Art 20 and 21."),

    # Tough
    (7, 3,
     "Art 33 ప్రకారం Parliament ఏ వర్గాల వ్యక్తుల FRs ని restrict/abrogate చేయగలదు?\n(For whom can Parliament restrict/abrogate FRs under Art 33?)",
     "కేవలం IAS officers మరియు Judges / Only IAS officers and Judges",
     "Armed Forces, Para-military, Intelligence agencies, Police maintaining public order / All four categories",
     "Central Government employees మాత్రమే / Central Govt employees only",
     "అందరి FRs ని restrict చేయవచ్చు / Can restrict FRs of all persons",
     "b",
     "Art 33: Parliament can restrict/abrogate FRs for (a) Members of Armed Forces, (b) Para-military forces, (c) Intelligence agencies, (d) Police forces maintaining public order. Purpose = maintain discipline and proper discharge of duties.\nArt 33 empowers Parliament to restrict or abrogate FRs for (a) Armed Forces members, (b) para-military forces, (c) intelligence agency personnel, (d) persons in forces maintaining public order — to ensure discipline."),

    # Toughest
    (7, 4,
     "కింది జంటలు సరైనవేనా?\n(1) Art 19 automatically suspended during National Emergency (Art 352)\n(2) Art 359 requires a Presidential Order to suspend FRs\n(3) Art 35 allows State legislatures to enforce FRs\n(4) Art 20 & 21 can never be suspended\nAre these statements correct?",
     "1, 2 మరియు 4 మాత్రమే సరైనవి / Only 1, 2 and 4 correct",
     "1, 2 మరియు 3 మాత్రమే / Only 1, 2 and 3",
     "అన్నీ సరైనవి / All four correct",
     "2 మరియు 4 మాత్రమే / Only 2 and 4",
     "a",
     "1 ✓ (Art 19 automatically suspended on proclamation of National Emergency under Art 352). 2 ✓ (Art 359 requires a separate Presidential Order — NOT automatic). 3 ✗ (Art 35 = ONLY Parliament, not state legislatures). 4 ✓ (Art 20 & 21 = never suspended).\n1 ✓ Art 19 suspends automatically under Art 352. 2 ✓ Art 359 needs a separate Presidential Order (not automatic). 3 ✗ Art 35 empowers Parliament only (not state legislatures). 4 ✓ Art 20 & 21 can never be suspended even during Emergency."),

    # PYQ — APPSC
    (7, 2,
     "Emergency time లో ఏ FRs ని suspend చేయలేరు? [APPSC Group 2]\n(Which FRs cannot be suspended during Emergency?)",
     "ఆర్టికల్ 14 మరియు 15 / Art 14 and 15",
     "ఆర్టికల్ 17 మరియు 18 / Art 17 and 18",
     "ఆర్టికల్ 20 మరియు 21 / Art 20 and 21",
     "ఆర్టికల్ 25 మరియు 26 / Art 25 and 26",
     "c",
     "Art 20 (Double jeopardy, self-incrimination రక్షణ) మరియు Art 21 (Right to life & liberty) — ఎటువంటి Emergency లోనూ suspend చేయలేరు. ఇవి absolute protection. APPSC Group 2 లో ఇది చాలా important question.\nArt 20 and Art 21 cannot be suspended under ANY Emergency — they are absolute. Art 20 protects against double jeopardy and self-incrimination. Art 21 protects the right to life and personal liberty. Frequently asked in APPSC Group 2.",
     "APPSC"),

]



import json as _json


def _seed_polity_ch8_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "8.1 ఆర్టికల్ 23: బలవంతపు వెట్టి చాకిరీ నిషేధం", "sub": "Art 23 · Forced Labour · Trafficking · Bonded Labour", "audio": ""},
    {"title": "8.2 ఆర్టికల్ 24: బాలల చాకిరీ నిషేధం", "sub": "Art 24 · Child Labour · Factories · Mines · Hazardous", "audio": ""},
    {"title": "8.3 ఆర్టికల్ 25-26: మతస్వాతంత్ర్యం", "sub": "Art 25 · Art 26 · Freedom of Religion · Conscience", "audio": ""},
    {"title": "8.4 ఆర్టికల్ 27-28: మతం మరియు విద్య", "sub": "Art 27 · Art 28 · Religious Taxation · Institutions", "audio": ""},
    {"title": "8.5 ఆర్టికల్ 29-30: సాంస్కృతిక మరియు విద్యా హక్కులు", "sub": "Art 29 · Art 30 · Minority Rights · Language · Script", "audio": ""},
    {"title": "8.6 ఆర్టికల్ 31A-31C: రక్షిత చట్టాలు", "sub": "Art 31A · Art 31B · Art 31C · 9th Schedule · Property", "audio": ""},
    {"title": "8.7 ఆర్టికల్ 32: రాజ్యాంగ పరిహారాల హక్కు", "sub": "Art 32 · Writs · Habeas Corpus · Mandamus · Certiorari", "audio": ""},
    {"title": "8.8 ఆర్టికల్ 33-35 మరియు అత్యవసర నిలుపు", "sub": "Art 33 · Art 34 · Art 35 · Emergency · FR Suspension", "audio": ""}
]
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
        (8, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch8 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (8, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 8,
         'ప్రాథమిక హక్కులు భాగం II',
         'Fundamental Rights Part II',
         'Ch.8',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch8 notes seeded!'}


def _seed_polity_ch8_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (8, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch8_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (8, 'Indian_Polity'))
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
    for mcq in POLITY_CH8_MCQS:
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

    total = len(POLITY_CH8_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch8 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
