# seed_polity_ch17.py
# Chapter 17 — Prime Minister & Council of Ministers
# Total Sections: 8 | Total MCQs: 65 | PYQs: 6
# Sections:
#   0 — Appointment & Qualifications of PM (10 MCQs)
#   1 — Powers & Functions of PM (10 MCQs)
#   2 — Council of Ministers — Composition & Categories (8 MCQs)
#   3 — Collective Responsibility & Individual Responsibility (8 MCQs)
#   4 — Role of Cabinet (8 MCQs)
#   5 — PM & President Relationship (7 MCQs)
#   6 — Kitchen Cabinet / Inner Cabinet (7 MCQs)
#   7 — Miscellaneous / Constitutional Provisions (7 MCQs)

_CH = 17
_SUBJECT = 'GK'
_TOPIC   = 'Indian_Polity'
_TITLE_TE = 'ప్రధానమంత్రి మరియు మంత్రిమండలి'
_TITLE_EN = 'Prime Minister & Council of Ministers'
_PAGES    = 'Ch.17 (Lakshmikanth)'

_NOTES_HTML = '''<p>చాప్టర్ 17 — ప్రధానమంత్రి మరియు మంత్రిమండలి. భారత రాజ్యాంగంలో అనుచ్ఛేదాలు 74–75 కేంద్ర మంత్రిమండలికి సంబంధించినవి. PM దేశ వాస్తవిక కార్యనిర్వాహకుడు (real executive). మంత్రిమండలి సమిష్టి బాధ్యత (collective responsibility) లోక్‌సభకు ఉంటుంది.</p>'''

_SECTIONS = [
    "PM నియామకం & అర్హతలు",
    "PM అధికారాలు & విధులు",
    "మంత్రిమండలి — రకాలు & సంఖ్య",
    "సమిష్టి & వ్యక్తిగత బాధ్యత",
    "కేబినెట్ పాత్ర",
    "PM & రాష్ట్రపతి సంబంధం",
    "కిచెన్ కేబినెట్ / అంతరంగ మండలి",
    "విభిన్న రాజ్యాంగ నిబంధనలు",
]

_MCQS = [
    # ── Section 0: Appointment & Qualifications of PM ──────────────────────────
    (0, "easy",
     "భారత ప్రధానమంత్రిని నియమించే అధికారం ఎవరికి ఉంది? / Who appoints the Prime Minister of India?",
     "లోక్‌సభ స్పీకర్ / Lok Sabha Speaker",
     "రాష్ట్రపతి / President",
     "సుప్రీం కోర్ట్ ప్రధాన న్యాయమూర్తి / Chief Justice of Supreme Court",
     "ఎగువ సభ చైర్మన్ / Chairman of Rajya Sabha",
     "b",
     "అనుచ్ఛేదం 75(1) ప్రకారం ప్రధానమంత్రిని రాష్ట్రపతి నియమిస్తారు. / Under Article 75(1), the Prime Minister is appointed by the President."),

    (0, "easy",
     "ప్రధానమంత్రి అర్హత కోసం ఏ సభకు సభ్యుడిగా ఉండాలి? / PM must be a member of which House?",
     "రాజ్యసభ మాత్రమే / Only Rajya Sabha",
     "లోక్‌సభ మాత్రమే / Only Lok Sabha",
     "పార్లమెంటు ఏ సభైనా / Either House of Parliament",
     "విధానసభ / State Legislative Assembly",
     "c",
     "ప్రధానమంత్రి పార్లమెంటు రెండు సభలలో దేనిలో అయినా సభ్యుడిగా ఉండవచ్చు, కానీ ఆచరణలో లోక్‌సభ సభ్యుడిగా ఉంటారు. / PM can be a member of either House, though in practice they are from Lok Sabha."),

    (0, "medium",
     "పార్లమెంటు సభ్యుడు కాని వ్యక్తి ప్రధానమంత్రిగా నియమించబడినట్లయితే, ఎంత కాలంలో పార్లమెంటు సభ్యుడవ్వాలి? / If a non-MP is appointed PM, within how many months must they become a Parliament member?",
     "3 నెలలు / 3 months",
     "6 నెలలు / 6 months",
     "9 నెలలు / 9 months",
     "12 నెలలు / 12 months",
     "b",
     "అనుచ్ఛేదం 75(5) ప్రకారం 6 నెలల లోపు పార్లమెంటు సభ్యుడవ్వాలి, లేదా పదవి కోల్పోతారు. / Under Art.75(5), within 6 months else office is lost."),

    (0, "medium",
     "ప్రధానమంత్రి పదవి కాలం ఎంత? / What is the term of office of the Prime Minister?",
     "5 సంవత్సరాలు నిర్ణయించబడినవి / Fixed 5 years",
     "రాష్ట్రపతి ఇష్టానుసారం / At the pleasure of President",
     "లోక్‌సభ విశ్వాసం ఉన్నంత కాలం / As long as LS confidence exists",
     "రాజ్యసభ తీర్మానం వరకు / Till RS resolution",
     "c",
     "PM పదవి కాలం నిర్ణయించబడలేదు — లోక్‌సభ విశ్వాసం ఉన్నంత కాలం పదవిలో ఉంటారు. / PM holds office as long as commanding LS majority."),

    (0, "medium",
     "ప్రధానమంత్రి ప్రమాణ స్వీకారం చేయించే వ్యక్తి ఎవరు? / Who administers the oath of office to the PM?",
     "లోక్‌సభ స్పీకర్ / Lok Sabha Speaker",
     "సుప్రీం కోర్ట్ CJI / CJI",
     "రాష్ట్రపతి / President",
     "ఉప రాష్ట్రపతి / Vice-President",
     "c",
     "అనుచ్ఛేదం 75(4) ప్రకారం రాష్ట్రపతి ప్రమాణ స్వీకారం చేయిస్తారు. / Under Art.75(4), President administers oath."),

    (0, "hard",
     "అనుచ్ఛేదం 75 ప్రకారం మంత్రుల సంఖ్య లోక్‌సభ బలంలో ఎంత శాతానికి మించరాదు? / Under Art.75, total ministers shall not exceed what % of LS strength?",
     "10%", "15%", "20%", "25%",
     "b",
     "91వ రాజ్యాంగ సవరణ చట్టం 2003 ద్వారా మొత్తం మంత్రిమండలి సభ్యులు లోక్‌సభ మొత్తం సభ్యుల 15%కి మించరాదు. / 91st Amendment 2003: total ministers ≤ 15% of total LS strength.", 'APPSC'),

    (0, "hard",
     "రాజ్యాంగంలో ప్రధానమంత్రి హోదాను ప్రస్తావించే అనుచ్ఛేదాలు ఏవి? / Articles dealing with PM's position in Constitution?",
     "అనుచ్ఛేదం 52–54 / Art.52–54",
     "అనుచ్ఛేదం 74–75 / Art.74–75",
     "అనుచ్ఛేదం 78–79 / Art.78–79",
     "అనుచ్ఛేదం 85–86 / Art.85–86",
     "b",
     "అనుచ్ఛేదం 74: మంత్రిమండలి నిర్మాణం. అనుచ్ఛేదం 75: PM నియామకం, మంత్రుల నియామకం, బాధ్యత. / Art.74: CoM constitution; Art.75: PM & ministers appointment/responsibility."),

    (0, "medium",
     "ప్రధానమంత్రి రాజ్యసభ సభ్యుడిగా ఉండవచ్చా? / Can Prime Minister be a Rajya Sabha member?",
     "అవున, ఎందుకంటే రాజ్యసభ ఉన్నత సభ / Yes, RS is upper house",
     "కాదు, LS సభ్యుడిగా ఉండాలి / No, must be LS member",
     "అవున, రాజ్యాంగంలో ఏ సభకు చెందాలో పేర్కొనలేదు / Yes, Constitution doesn't specify which House",
     "అవున, కానీ 6 నెలల్లో LS ఎన్నికల్లో నిలబడాలి / Yes but must contest LS within 6 months",
     "c",
     "రాజ్యాంగం PM ఏ సభకు చెందాలో నిర్దేశించలేదు — పార్లమెంటు సభ్యుడిగా ఉంటే సరిపోతుంది. డా. మన్మోహన్ సింగ్ (2004–2014) రాజ్యసభ సభ్యుడిగా PM పదవిలో ఉన్నారు. / Constitution doesn't specify LS or RS; PM must be a member of Parliament. Dr. Manmohan Singh served as PM from RS (2004–2014)."),

    # ── Section 1: Powers & Functions of PM ───────────────────────────────────
    (1, "easy",
     "ప్రధానమంత్రి ప్రభుత్వంలో ఏ పాత్ర పోషిస్తారు? / What role does PM play in government?",
     "రాజ్యాంగపరమైన అధిపతి / Constitutional head",
     "నిజమైన కార్యనిర్వాహకుడు / Real executive",
     "కేవలం సలహాదారు / Mere advisor",
     "న్యాయ అధిపతి / Judicial head",
     "b",
     "రాష్ట్రపతి రాజ్యాంగపరమైన అధిపతి; PM నిజమైన (real) కార్యనిర్వాహకుడు. / President is nominal head; PM is real executive."),

    (1, "medium",
     "PM అధికారాల్లో పార్లమెంటు సమావేశం (session) పెట్టే, వాయిదా వేసే సలహా ఇచ్చే అనుచ్ఛేదం ఏది? / Which article allows PM to advise summoning/proroguing Parliament?",
     "అనుచ్ఛేదం 74 / Art.74",
     "అనుచ్ఛేదం 85 / Art.85",
     "అనుచ్ఛేదం 108 / Art.108",
     "అనుచ్ఛేదం 110 / Art.110",
     "b",
     "అనుచ్ఛేదం 85: రాష్ట్రపతి PM సలహాపై పార్లమెంటు సమావేశాలు ఏర్పాటు చేస్తారు / వాయిదా వేస్తారు. / Art.85: President summons/prorogues Parliament on PM's advice."),

    (1, "medium",
     "ప్రధానమంత్రి కేంద్ర మంత్రుల నియామకంలో ఏ పాత్ర పోషిస్తారు? / What is PM's role in appointment of Union Ministers?",
     "నేరుగా నియమిస్తారు / Directly appoints",
     "పార్లమెంటు ఆమోదం తో నియమిస్తారు / Appoints with Parliament approval",
     "మంత్రులను సిఫారసు చేస్తారు, రాష్ట్రపతి నియమిస్తారు / Recommends; President appoints",
     "మంత్రులను తొలగించే అధికారం మాత్రమే ఉంది / Only power to remove",
     "c",
     "అనుచ్ఛేదం 75(1): PM సిఫారసుపై రాష్ట్రపతి మంత్రులను నియమిస్తారు. PM పోర్ట్‌ఫోలియోలు కేటాయిస్తారు. / Art.75(1): President appoints ministers on PM's advice. PM also allocates portfolios."),

    (1, "medium",
     "నీతి ఆయోగ్‌కు అధ్యక్షుడు ఎవరు? / Who chairs NITI Aayog?",
     "రాష్ట్రపతి / President",
     "ఉప రాష్ట్రపతి / Vice-President",
     "ప్రధానమంత్రి / Prime Minister",
     "ఆర్థిక మంత్రి / Finance Minister",
     "c",
     "PM నీతి ఆయోగ్ (National Institution for Transforming India) అధ్యక్షుడు. / PM is the ex-officio Chairman of NITI Aayog."),

    (1, "hard",
     "అనుచ్ఛేదం 74(2) ప్రకారం మంత్రిమండలి సలహా విషయంలో కోర్టులు ఏం చేయగలవు? / Under Art.74(2), what can courts do regarding Cabinet advice to President?",
     "పూర్తిగా సమీక్షించగలవు / Can fully review",
     "కేవలం రాజ్యసభ అభ్యర్థనపై సమీక్షించగలవు / Only on RS petition",
     "మంత్రులు ఇచ్చిన సలహా విచారించే అధికారం లేదు / Courts cannot enquire into advice tendered by ministers",
     "PM ముందస్తు అనుమతితో సమీక్షించగలవు / With PM's prior permission",
     "c",
     "అనుచ్ఛేదం 74(2): రాష్ట్రపతికి మంత్రులు ఇచ్చిన సలహా విచారించే అధికారం ఏ కోర్టుకూ లేదు — మంత్రిమండలి సలహా న్యాయ సమీక్షకు అతీతం. / Art.74(2): No court shall inquire into the advice tendered by ministers to the President — CoM advice is beyond judicial review."),

    (1, "easy",
     "PM అధ్యక్షతన సమావేశమయ్యే అత్యున్నత నిర్ణయాధికార సంస్థ ఏది? / Highest decision-making body chaired by PM?",
     "అనుసందాన సంఘం / Coordination Committee",
     "కేబినెట్ / Cabinet",
     "జాతీయ భద్రతా మండలి / National Security Council",
     "ఆర్థిక వ్యవహారాల కమిటీ / Committee on Economic Affairs",
     "b",
     "కేబినెట్ PM అధ్యక్షతన సమావేశమవుతుంది మరియు దేశంలో అత్యున్నత నిర్ణయాధికారసంస్థగా పని చేస్తుంది. / Cabinet chaired by PM is the supreme decision-making body."),

    (1, "medium",
     "ప్రధానమంత్రి ఏ అనుచ్ఛేదం ద్వారా రాష్ట్రపతికి సలహా ఇస్తారు? / Under which Article does PM advise the President?",
     "అనుచ్ఛేదం 74 / Art.74",
     "అనుచ్ఛేదం 75 / Art.75",
     "అనుచ్ఛేదం 76 / Art.76",
     "అనుచ్ఛేదం 77 / Art.77",
     "a",
     "అనుచ్ఛేదం 74(1): రాష్ట్రపతికి సహాయం చేయడానికి మరియు సలహా ఇవ్వడానికి PM నేతృత్వంలో మంత్రిమండలి ఉంటుంది. / Art.74(1): There shall be a CoM with PM at head to aid and advise President."),

    (1, "hard",
     "PM 'ప్రభుత్వ ముఖ్య' మరియు 'కేబినెట్ ముఖ్య' — ఈ రెండు పాత్రలు ఏ పండితుడు అభివర్ణించారు? / Who described PM as 'keystone of the Cabinet arch'?",
     "జవహర్‌లాల్ నెహ్రూ / Jawaharlal Nehru",
     "ఆల్‌బిగ్ / Albeig",
     "ఎన్.ఎ. పాల్ఖీవాలా / N.A. Palkhivala",
     "రాధాకుమార్ / Radhakumar",
     "b",
     "Albeig అన్నారు: 'PM is the keystone of the Cabinet arch' — PM లేకుండా మంత్రిమండలి నిలబడదు. / Albeig: 'PM is the keystone of the Cabinet arch.'"),

    # ── Section 2: Council of Ministers — Composition & Categories ─────────────
    (2, "easy",
     "కేంద్ర మంత్రిమండలిలో ఎన్ని వర్గాల మంత్రులు ఉంటారు? / How many categories of ministers are in Union CoM?",
     "2", "3", "4", "5",
     "b",
     "మూడు వర్గాలు: 1) కేబినెట్ మంత్రులు, 2) రాష్ట్ర మంత్రులు, 3) డిప్యూటీ మంత్రులు. / Three categories: Cabinet Ministers, Ministers of State, Deputy Ministers."),

    (2, "medium",
     "కేబినెట్ మంత్రులు మరియు రాష్ట్ర మంత్రులకు ప్రధాన తేడా ఏమిటి? / Main difference between Cabinet Ministers and Ministers of State?",
     "జీతాలు / Salaries",
     "కేబినెట్ సమావేశాలలో పాల్గొనే హక్కు / Right to attend Cabinet meetings",
     "పార్టీ అనుబంధం / Party affiliation",
     "పదవీ కాలం / Term of office",
     "b",
     "కేబినెట్ మంత్రులు కేబినెట్ సమావేశాలకు హాజరవుతారు; రాష్ట్ర మంత్రులు సాధారణంగా హాజరవ్వరు (వారి విభాగానికి సంబంధించిన అంశాలు తప్ప). / Cabinet Ministers attend Cabinet meetings; MoS generally don't."),

    (2, "medium",
     "రాజ్యాంగంలో 'కేబినెట్' అనే పదాన్ని ఎక్కడ నిర్వచించారు? / Where is 'Cabinet' defined in the Constitution?",
     "అనుచ్ఛేదం 74 / Art.74",
     "అనుచ్ఛేదం 352 / Art.352",
     "44వ సవరణ చేర్పు ద్వారా అనుచ్ఛేదం 352(3) / Art.352(3) via 44th Amendment",
     "అనుచ్ఛేదం 356 / Art.356",
     "c",
     "44వ రాజ్యాంగ సవరణ 1978: అనుచ్ఛేదం 352(3)లో 'Cabinet' అనే పదాన్ని నిర్వచించారు — PM + కేబినెట్ మంత్రులు. / 44th Amendment 1978: 'Cabinet' defined in Art.352(3) as PM + Cabinet Ministers."),

    (2, "hard",
     "91వ రాజ్యాంగ సవరణ 2003 కింద మంత్రిమండలి 15% పరిమితికి ఏ సభ బలం ఆధారంగా? / 15% ceiling under 91st Amendment is based on strength of which House?",
     "రాజ్యసభ / Rajya Sabha",
     "లోక్‌సభ / Lok Sabha",
     "రెండు సభల మొత్తం / Total of both Houses",
     "విజయం సాధించిన పార్టీ సభ్యుల సంఖ్య / Winning party members",
     "b",
     "91వ సవరణ: మొత్తం మంత్రులు లోక్‌సభ మొత్తం సభ్యుల 15%కి మించరాదు (ఇది రాష్ట్రాలకు కూడా వర్తిస్తుంది). / 91st Amendment: total ministers ≤ 15% of total LS membership (also applies to states)."),

    (2, "medium",
     "పార్లమెంటరీ సెక్రటరీ (Parliamentary Secretary) అనే పదవి రాజ్యాంగంలో ఉందా? / Is 'Parliamentary Secretary' a constitutional post?",
     "అవును, అనుచ్ఛేదం 75లో ఉంది / Yes, in Art.75",
     "అవును, అనుచ్ఛేదం 77లో ఉంది / Yes, in Art.77",
     "లేదు, రాజ్యాంగేతర పదవి / No, extra-constitutional",
     "అవును, అనుచ్ఛేదం 88లో ఉంది / Yes, in Art.88",
     "c",
     "Parliamentary Secretary పదవి రాజ్యాంగంలో లేదు — ఇది రాజ్యాంగేతర (extra-constitutional) పదవి. / Parliamentary Secretary is not a constitutional post — extra-constitutional."),

    (2, "easy",
     "కేబినెట్ మంత్రులు ఒక్కో మంత్రిత్వ శాఖకు అధిపతిగా ఉంటారు — వీరి హోదా ఏమిటి? / Cabinet Ministers head one ministry — their rank is?",
     "జూనియర్ మంత్రి / Junior Minister",
     "సీనియర్ మంత్రి / Senior Minister",
     "కేబినెట్ రాంక్ / Cabinet rank",
     "రాష్ట్ర మంత్రి స్థాయి / MoS level",
     "c",
     "కేబినెట్ మంత్రులు అత్యున్నత స్థాయి మంత్రులు; స్వతంత్రంగా మంత్రిత్వ శాఖలు నిర్వహిస్తారు. / Cabinet Ministers are the highest rank — independently head ministries."),

    (2, "hard",
     "స్వతంత్ర బాధ్యత గల రాష్ట్ర మంత్రి (MoS independent charge) కేబినెట్ సమావేశాలకు హాజరవ్వగలరా? / Can MoS with independent charge attend Cabinet meetings?",
     "ఎప్పుడూ హాజరవ్వలేరు / Never",
     "ఎల్లప్పుడూ హాజరవ్వగలరు / Always",
     "తమ విభాగానికి సంబంధించిన అంశాలపై పిలిచినప్పుడు మాత్రమే / Only when invited for relevant matters",
     "కేబినెట్ ఆమోదంతో / With Cabinet approval",
     "c",
     "MoS (Independent Charge) తమ పోర్ట్‌ఫోలియోకు సంబంధించిన అంశాలు చర్చించేటప్పుడు కేబినెట్ సమావేశాలకు పిలవబడవచ్చు. / MoS (IC) may be invited to Cabinet meetings when their portfolio is discussed."),

    (2, "medium",
     "కేంద్ర మంత్రిమండలిలో 'Deputy Minister' పదవి గురించి ఏది నిజం? / What is true about 'Deputy Minister' in Union CoM?",
     "కేబినెట్ మంత్రులకు సహాయం చేస్తారు / Assist Cabinet Ministers",
     "స్వతంత్ర మంత్రిత్వ శాఖ నిర్వహిస్తారు / Head independent ministry",
     "PM కి నేరుగా నివేదిస్తారు / Report directly to PM",
     "రాజ్యసభకు మాత్రమే జవాబుదారీ / Accountable only to RS",
     "a",
     "డిప్యూటీ మంత్రులు కేబినెట్ మంత్రులకు సహాయపడతారు; స్వతంత్ర పోర్ట్‌ఫోలియో ఉండదు. / Deputy Ministers assist Cabinet Ministers; no independent portfolio."),

    # ── Section 3: Collective Responsibility & Individual Responsibility ───────
    (3, "easy",
     "మంత్రిమండలి సమిష్టి బాధ్యత (Collective Responsibility) ఏ సభకు ఉంటుంది? / Collective Responsibility of CoM is to which House?",
     "రాజ్యసభ / Rajya Sabha",
     "లోక్‌సభ / Lok Sabha",
     "రెండు సభలకు / Both Houses",
     "రాష్ట్రపతికి / President",
     "b",
     "అనుచ్ఛేదం 75(3): మంత్రిమండలి సమిష్టిగా లోక్‌సభకు జవాబుదారీ. / Art.75(3): CoM is collectively responsible to Lok Sabha."),

    (3, "medium",
     "సమిష్టి బాధ్యత సూత్రానికి అర్థమేమిటి? / What does collective responsibility mean?",
     "ప్రతి మంత్రి వేరే విధానం వ్యక్తం చేయవచ్చు / Each minister expresses different policy",
     "మంత్రిమండలి నిర్ణయాలన్నీ ఒకటిగా ఆమోదించాలి / All Cabinet decisions must be accepted as one",
     "ప్రధాన మంత్రి మాత్రమే జవాబుదారీ / Only PM is responsible",
     "మంత్రులు ప్రత్యేకంగా జవాబుదారీ / Ministers separately responsible",
     "b",
     "సమిష్టి బాధ్యత: మంత్రిమండలి నిర్ణయాలకు అన్ని మంత్రులు బాధ్యులు; నిర్ణయంతో విభేదిస్తే రాజీనామా ఇవ్వాలి. / Collective responsibility: all ministers bound by Cabinet decisions — disagree means resign."),

    (3, "medium",
     "లోక్‌సభలో అవిశ్వాస తీర్మానం ఆమోదమైతే మంత్రిమండలికి ఏమవుతుంది? / If no-confidence motion passes in LS, what happens to CoM?",
     "ఒక్క మంత్రి రాజీనామా చేస్తారు / Only one minister resigns",
     "PM మాత్రమే రాజీనామా చేస్తారు / Only PM resigns",
     "మొత్తం మంత్రిమండలి రాజీనామా చేయాలి / Entire CoM must resign",
     "ఏమీ జరగదు / Nothing happens",
     "c",
     "అవిశ్వాస తీర్మానం ఆమోదమైతే PM తో పాటు మొత్తం మంత్రిమండలి రాజీనామా చేయాలి — సమిష్టి బాధ్యత సూత్రం. / If no-confidence motion passes, entire CoM (including PM) must resign."),

    (3, "hard",
     "వ్యక్తిగత బాధ్యత (Individual Responsibility) ఏ అనుచ్ఛేదంలో పేర్కొనబడింది? / Individual Responsibility of ministers is in which Article?",
     "అనుచ్ఛేదం 74 / Art.74",
     "అనుచ్ఛేదం 75(2) / Art.75(2)",
     "అనుచ్ఛేదం 76 / Art.76",
     "అనుచ్ఛేదం 78 / Art.78",
     "b",
     "అనుచ్ఛేదం 75(2): మంత్రులు రాష్ట్రపతి సంతోషం ఉన్నంత కాలం పదవిలో ఉంటారు (వ్యక్తిగత బాధ్యత). / Art.75(2): Ministers hold office during pleasure of President (individual responsibility)."),

    (3, "medium",
     "మంత్రిమండలి నిర్ణయాన్ని సభలో వ్యతిరేకించే మంత్రి ఏం చేయాలి? / A minister who opposes Cabinet decision in public must?",
     "ప్రజాభిప్రాయం అడగాలి / Seek public opinion",
     "రాజ్యసభకు పిటిషన్ వేయాలి / Petition Rajya Sabha",
     "రాజీనామా చేయాలి / Resign",
     "కేబినెట్ మీటింగ్‌లో మాత్రమే వ్యతిరేకించాలి / Oppose only in Cabinet meeting",
     "c",
     "సమిష్టి బాధ్యత: కేబినెట్ నిర్ణయంతో విభేదించే మంత్రి మొదట రాజీనామా ఇవ్వాలి, తర్వాత వ్యతిరేకించవచ్చు. / Collective responsibility: minister must resign before publicly opposing Cabinet decision."),

    (3, "easy",
     "మంత్రిమండలి సమిష్టి బాధ్యత సూత్రం ఏ దేశ ప్రభుత్వ విధానానికి చెందినది? / Collective responsibility is borrowed from which country's system?",
     "అమెరికా / USA",
     "బ్రిటన్ / Britain",
     "ఫ్రాన్స్ / France",
     "కెనడా / Canada",
     "b",
     "సమిష్టి బాధ్యత సూత్రం బ్రిటన్ వెస్ట్‌మినిస్టర్ విధానం నుండి తీసుకోబడింది. / Collective responsibility is borrowed from the British Westminster system."),

    (3, "hard",
     "రాజ్యసభ సభ్యుడైన మంత్రి అవిశ్వాస తీర్మానంపై లోక్‌సభలో ఓటు వేయగలరా? / Can a minister who is RS member vote in LS on no-confidence motion?",
     "అవును / Yes",
     "లేదు / No",
     "కేవలం PM మాత్రమే / Only PM",
     "స్పీకర్ అనుమతితో / With Speaker's permission",
     "b",
     "రాజ్యసభ సభ్యుడు లోక్‌సభలో ఓటు వేయలేరు. మంత్రిగా ఉన్నా, లోక్‌సభలో ఓటు హక్కు లేదు. / RS member cannot vote in LS — even if a minister."),

    (3, "medium",
     "మంత్రిమండలికి రాజ్యసభకు జవాబుదారీ ఉంటుందా? / Is CoM responsible to Rajya Sabha?",
     "అవును / Yes",
     "లేదు / No",
     "కొంత మేరకు / Partially",
     "రాజ్యాంగ సవరణ తర్వాత మాత్రమే / Only after constitutional amendment",
     "b",
     "మంత్రిమండలి కేవలం లోక్‌సభకు మాత్రమే సమిష్టిగా జవాబుదారీ. రాజ్యసభకు కాదు. / CoM is collectively responsible only to LS — not to RS."),

    # ── Section 4: Role of Cabinet ──────────────────────────────────────────────
    (4, "easy",
     "కేబినెట్ సమావేశాలకు అధ్యక్షత వహించే వ్యక్తి ఎవరు? / Who presides over Cabinet meetings?",
     "రాష్ట్రపతి / President",
     "ఉప రాష్ట్రపతి / Vice-President",
     "ప్రధానమంత్రి / Prime Minister",
     "లోక్‌సభ స్పీకర్ / Lok Sabha Speaker",
     "c",
     "PM కేబినెట్ అధ్యక్షుడు మరియు సమావేశాలకు అధ్యక్షత వహిస్తారు. / PM chairs all Cabinet meetings."),

    (4, "medium",
     "కేబినెట్ యొక్క ప్రధాన విధి ఏమిటి? / What is the main function of the Cabinet?",
     "చట్టాలు చేయడం / Making laws",
     "విదేశాంగ నిర్ణయాలు, విధాన రూపకల్పన / Policy formulation, key decisions",
     "న్యాయ వివాదాలు పరిష్కరించడం / Resolving judicial disputes",
     "రాష్ట్ర ప్రభుత్వాలను నియమించడం / Appointing state govts",
     "b",
     "కేబినెట్ జాతీయ విధాన రూపకల్పన, అన్ని ముఖ్యమైన నిర్ణయాలు, రాష్ట్రపతికి సిఫారసులు చేయడం చేస్తుంది. / Cabinet formulates national policy, takes key decisions, recommends to President."),

    (4, "hard",
     "కేబినెట్ కమిటీలు (Cabinet Committees) ఏ అనుచ్ఛేదంలో ప్రస్తావించబడ్డాయి? / Cabinet Committees are mentioned in which Article?",
     "అనుచ్ఛేదం 74 / Art.74",
     "అనుచ్ఛేదం 77 / Art.77",
     "రాజ్యాంగంలో ప్రత్యేకంగా లేవు / Not specifically in Constitution",
     "అనుచ్ఛేదం 352 / Art.352",
     "c",
     "కేబినెట్ కమిటీలు రాజ్యాంగేతర సంస్థలు — రాజ్యాంగంలో ప్రత్యేకంగా ప్రస్తావించబడలేదు. / Cabinet Committees are extra-constitutional — not specifically mentioned in Constitution."),

    (4, "medium",
     "కేబినెట్ నిర్ణయాలు రికార్డు చేయడానికి బాధ్యత ఏ సంస్థకు ఉంటుంది? / Which body is responsible for recording Cabinet decisions?",
     "PMO (ప్రధానమంత్రి కార్యాలయం) / PMO",
     "కేబినెట్ సెక్రటేరియట్ / Cabinet Secretariat",
     "గృహ మంత్రిత్వ శాఖ / Home Ministry",
     "రాజ్యాంగ సంఘం / Constitutional Assembly",
     "b",
     "కేబినెట్ సెక్రటేరియట్ కేబినెట్ నిర్ణయాలను రికార్డు చేయడం, అమలు పర్యవేక్షణ చేయడం బాధ్యత వహిస్తుంది. / Cabinet Secretariat records Cabinet decisions and monitors implementation."),

    (4, "easy",
     "PMO (Prime Minister's Office) అధికారిక అధిపతి ఎవరు? / Who officially heads the PMO?",
     "కేబినెట్ సెక్రటరీ / Cabinet Secretary",
     "ప్రధాన కార్యదర్శి (Principal Secretary to PM) / Principal Secretary to PM",
     "ఆర్థిక మంత్రి / Finance Minister",
     "లోక్‌సభ స్పీకర్ / Lok Sabha Speaker",
     "b",
     "PMO అధికారిక అధిపతి Principal Secretary to PM లేదా Chief of Staff. / PMO is officially headed by Principal Secretary to PM (or Chief of Staff)."),

    (4, "medium",
     "అత్యవసర పరిస్థితి (Art.352) ప్రకటనకు ముందు కేబినెట్ లిఖిత తీర్మానం అవసరం ఎందువల్ల? / Why is written resolution of Cabinet required before Art.352 proclamation?",
     "రాజ్యసభ ఆదేశం / RS order",
     "44వ రాజ్యాంగ సవరణ సవరించింది / 44th Amendment requirement",
     "ఎల్లప్పుడూ అవసరం / Always required",
     "PM ఇష్టానుసారం / PM's discretion",
     "b",
     "44వ రాజ్యాంగ సవరణ 1978: అనుచ్ఛేదం 352(3): కేబినెట్ లిఖిత తీర్మానం తర్వాతే Emergency ప్రకటన చేయవచ్చు. / 44th Amendment 1978: Art.352(3) requires written resolution of Cabinet before Emergency."),

    (4, "hard",
     "భారత కేబినెట్ ప్రభుత్వ నిర్మాణంలో రాజ్యాంగ స్థానం ఏమిటి? / Constitutional position of Cabinet in Indian government?",
     "రాజ్యాంగ సంస్థ / Constitutional body",
     "చట్టబద్ధ సంస్థ / Statutory body",
     "రాజ్యాంగేతర సంస్థ / Extra-constitutional body",
     "అర్ధ న్యాయ సంస్థ / Quasi-judicial body",
     "a",
     "Cabinet రాజ్యాంగ సంస్థ — 44వ సవరణ తర్వాత Art.352(3)లో నిర్వచించబడింది. / Cabinet is a constitutional body — defined in Art.352(3) after 44th Amendment."),

    (4, "easy",
     "కేబినెట్ కమిటీలలో ముఖ్యమైనది ఏది? / Which is the most important Cabinet Committee?",
     "వ్యవసాయ కమిటీ / Agricultural Committee",
     "భద్రతా వ్యవహారాల కమిటీ (CCS) / Cabinet Committee on Security (CCS)",
     "విద్యా కమిటీ / Education Committee",
     "ఆరోగ్య కమిటీ / Health Committee",
     "b",
     "CCS (Cabinet Committee on Security) PM అధ్యక్షతన — రక్షణ, విదేశాంగ, అంతర్గత భద్రత నిర్ణయాలు తీసుకుంటుంది. / CCS chaired by PM handles defence, foreign affairs, internal security."),

    # ── Section 5: PM & President Relationship ─────────────────────────────────
    (5, "easy",
     "రాష్ట్రపతి PM సలహాను పాటించకుండా స్వంత నిర్ణయాలు తీసుకోగలరా? / Can President act without PM's advice?",
     "అవును, ఎల్లప్పుడూ / Yes, always",
     "42వ సవరణ తర్వాత కాదు / No, after 42nd Amendment",
     "అత్యవసర పరిస్థితిలో మాత్రమే / Only in emergency",
     "రాజ్యసభ అనుమతితో / With RS permission",
     "b",
     "42వ రాజ్యాంగ సవరణ 1976: అనుచ్ఛేదం 74(1) సవరణ — రాష్ట్రపతి మంత్రిమండలి సలహా ప్రకారమే పని చేయాలి. / 42nd Amendment 1976: President must act on the advice of CoM (Art.74(1) amended)."),

    (5, "medium",
     "44వ రాజ్యాంగ సవరణ రాష్ట్రపతి-PM సంబంధంపై ఏం మార్పు చేసింది? / What change did 44th Amendment make to President-PM relationship?",
     "PM అధికారాలు తగ్గించింది / Reduced PM's powers",
     "రాష్ట్రపతి సలహాను ఒకసారి తిరిగి పంపవచ్చు / President may return advice once for reconsideration",
     "రాష్ట్రపతిని PM నియమించవచ్చు / PM can appoint President",
     "రాష్ట్రపతిని తొలగించే అధికారం PM కి ఇచ్చింది / PM given power to remove President",
     "b",
     "44వ రాజ్యాంగ సవరణ 1978: అనుచ్ఛేదం 74(1) — రాష్ట్రపతి మంత్రిమండలి సలహాను ఒకసారి తిరిగి పంపవచ్చు; పునఃపంపిన సలహాపై తప్పనిసరిగా పని చేయాలి. / 44th Amendment: President may return advice once; must act on reconsidered advice."),

    (5, "medium",
     "PM రాష్ట్రపతికి ఏ అనుచ్ఛేదం కింద మంత్రిమండలి నిర్ణయాలు తెలియజేయాలి? / Under which Article PM must inform President of Cabinet decisions?",
     "అనుచ్ఛేదం 74 / Art.74",
     "అనుచ్ఛేదం 78 / Art.78",
     "అనుచ్ఛేదం 85 / Art.85",
     "అనుచ్ఛేదం 77 / Art.77",
     "b",
     "అనుచ్ఛేదం 78: PM బాధ్యతలు — కేంద్ర ప్రభుత్వ నిర్ణయాలు, శాసన ప్రతిపాదనలు రాష్ట్రపతికి తెలియజేయడం. / Art.78: PM duties — communicate Cabinet decisions and legislative proposals to President."),

    (5, "hard",
     "PM పదవి ఖాళీగా ఉన్నప్పుడు రాష్ట్రపతి తన స్వంత విచక్షణతో ఎవరిని PM గా నియమించవచ్చు? / When PM post is vacant, President may on own discretion appoint?",
     "రాజ్యసభ నాయకుడు / Leader of RS",
     "లోక్‌సభలో మెజారిటీ నాయకుడు / Leader of LS majority",
     "సీనియర్ మంత్రి / Senior minister",
     "అత్యవసరకాలంలో CJI / CJI in emergency",
     "b",
     "PM పదవి ఖాళీ అయినప్పుడు రాష్ట్రపతి లోక్‌సభలో మెజారిటీ నాయకుడిని PM గా నియమిస్తారు. సంకీర్ణ ప్రభుత్వంలో విచక్షణ ఉంటుంది. / When PM post falls vacant, President appoints LS majority leader; discretion in hung parliament."),

    (5, "easy",
     "ప్రధానమంత్రి మరియు రాష్ట్రపతి మధ్య అన్ని విషయాలలో ఎవరి అభిప్రాయం ప్రాధాన్యత పొందుతుంది? / Whose opinion prevails in all matters between PM and President?",
     "రాష్ట్రపతి / President",
     "ప్రధానమంత్రి / Prime Minister",
     "సమానంగా / Equally",
     "సుప్రీం కోర్ట్ నిర్ణయిస్తుంది / Supreme Court decides",
     "b",
     "వాస్తవ కార్యనిర్వాహకుడు PM. అనుచ్ఛేదం 74(1) ప్రకారం రాష్ట్రపతి CoM సలహా ప్రకారమే పని చేయాలి. / PM is real executive; President must act on CoM advice per Art.74(1)."),

    (5, "medium",
     "రాష్ట్రపతి PM సలహాను పాటించకపోతే రాజ్యాంగ పరిష్కారం ఏమిటి? / Constitutional remedy if President doesn't follow PM's advice?",
     "సుప్రీం కోర్ట్ జోక్యం / Supreme Court intervention",
     "పార్లమెంటులో అభిశంసన / Impeachment in Parliament",
     "రాజ్యాంగ సంఘట / Constitutional convention pressure",
     "రాజ్యాంగ సవరణ / Constitutional amendment",
     "b",
     "రాష్ట్రపతి రాజ్యాంగ ఉల్లంఘన చేసినట్లయితే అభిశంసన (Art.61) ఏకైక రాజ్యాంగ పరిష్కారం. / Impeachment (Art.61) is the only constitutional remedy for President's constitutional violations."),

    (5, "hard",
     "PM-రాష్ట్రపతి సంబంధంలో 'రాజ్యాంగ ఆచారాలు' (constitutional conventions) ఏ ఉద్దేశంతో అనుసరిస్తారు? / Why are 'constitutional conventions' followed in PM-President relationship?",
     "రాజ్యాంగ నిబంధనలు అసంపూర్ణం కాబట్టి / Because constitutional provisions are incomplete",
     "రాజ్యాంగ స్ఫూర్తిని కాపాడటానికి / To preserve constitutional spirit",
     "న్యాయస్థానాల నిర్ణయాలతో / Through court verdicts",
     "రాజ్యాంగ సవరణలతో / Through amendments",
     "b",
     "PM-రాష్ట్రపతి సంబంధంలో అనేక ఆచారాలు (conventions) పాటించబడతాయి — రాజ్యాంగ స్ఫూర్తికి నిలబెట్టడానికి. / Many conventions govern PM-President relationship — to uphold constitutional spirit."),

    (5, "medium",
     "Art.74(1) ప్రకారం రాష్ట్రపతి మంత్రిమండలి సలహాపై తప్పనిసరిగా వ్యవహరించాలా? / Under Art.74(1), must President act on Cabinet's advice?",
     "కాదు, రాష్ట్రపతి స్వతంత్రంగా నిర్ణయించవచ్చు / No, President can decide independently",
     "అవున, 44వ సవరణ తర్వాత — సలహా తిరిగి పంపవచ్చు, కానీ పునఃపరిశీలించిన సలహా పాటించాలి / Yes, after 44th Amend — can return once; but must act on reconsidered advice",
     "అవున, ఎల్లప్పుడూ మరియు సలహా తిరిగి పంపే అవకాశం లేదు / Yes, always and cannot return advice",
     "కాదు, కానీ సాధారణంగా పాటించాలి / No, but should normally follow",
     "b",
     "44వ రాజ్యాంగ సవరణ 1978: రాష్ట్రపతి మంత్రిమండలి సలహాను ఒకసారి తిరిగి పంపవచ్చు, కానీ రెండవ సారి పాటించాల్సిందే. / 44th Amendment 1978: President may return CoM advice once for reconsideration; but must act on reconsidered advice."),

    # ── Section 6: Kitchen Cabinet / Inner Cabinet ─────────────────────────────
    (6, "easy",
     "'కిచెన్ కేబినెట్' అనే పదం దేనిని సూచిస్తుంది? / What does 'Kitchen Cabinet' refer to?",
     "వంట గది నిర్వాహకులు / Kitchen staff",
     "PM చుట్టూ ఉండే అనధికారిక సలహాదారుల బృందం / Informal group of advisors around PM",
     "సీనియర్ కేబినెట్ మంత్రులు / Senior Cabinet Ministers",
     "జాతీయ భద్రతా మండలి / National Security Council",
     "b",
     "కిచెన్ కేబినెట్ — PM చుట్టూ ఉండే అనధికారిక, విశ్వాసపాత్రమైన సలహాదారుల బృందం. / Kitchen Cabinet — informal group of trusted advisors around PM."),

    (6, "medium",
     "కిచెన్ కేబినెట్ లక్షణాలలో ఏది సరైనది? / Which is correct about Kitchen Cabinet?",
     "రాజ్యాంగ సంస్థ / Constitutional body",
     "రాజ్యాంగేతర, అనధికారిక సంస్థ / Extra-constitutional, informal body",
     "లోక్‌సభకు జవాబుదారీ / Accountable to LS",
     "సుప్రీం కోర్ట్ ద్వారా నియమింపబడుతుంది / Appointed by SC",
     "b",
     "కిచెన్ కేబినెట్ రాజ్యాంగేతర మరియు అనధికారిక — ఇది ఏ సభకూ జవాబుదారీ కాదు. / Kitchen Cabinet is extra-constitutional and informal — not accountable to any House."),

    (6, "hard",
     "భారతదేశంలో 'కిచెన్ కేబినెట్' భావన ఎక్కడ నుండి వచ్చింది? / From where did 'Kitchen Cabinet' concept come to India?",
     "అమెరికా / USA",
     "బ్రిటన్ / Britain",
     "ఫ్రాన్స్ / France",
     "కెనడా / Canada",
     "a",
     "కిచెన్ కేబినెట్ భావన అమెరికా నుండి వచ్చింది — అమెరికన్ అధ్యక్షుల అనధికారిక సలహా బృందాన్ని సూచిస్తుంది. / Kitchen Cabinet concept came from USA — refers to President's informal advisory group."),

    (6, "easy",
     "PMO (ప్రధానమంత్రి కార్యాలయం) లో పని చేసే అధికారులు ఏ సంస్థకు చెందినవారు? / Officers working in PMO belong to which service?",
     "ఒక నిర్దిష్ట సేవ / One specific service",
     "భారత పరిపాలనా సేవ (IAS) మరియు ఇతర సేవలు / IAS and various other services",
     "విదేశాంగ సేవ మాత్రమే / Only Foreign Service",
     "రక్షణ సేవలు మాత్రమే / Only Defence Services",
     "b",
     "PMOలో IAS, IFS, IPS, సైనికులు, సాంకేతిక నిపుణులు — వివిధ సేవలకు చెందినవారు పని చేస్తారు. / PMO has officials from IAS, IFS, IPS, military, technical experts — various services."),

    (6, "medium",
     "PM యొక్క ముఖ్య సలహాదారుడు (Principal Advisor) ఎవరు? / Who is the Principal Advisor to PM?",
     "Cabinet Secretary / కేబినెట్ సెక్రటరీ",
     "Principal Secretary to PM / ప్రిన్సిపల్ సెక్రటరీ",
     "Home Secretary / హోమ్ సెక్రటరీ",
     "National Security Advisor / జాతీయ భద్రతా సలహాదారు",
     "b",
     "Principal Secretary to PM (లేదా Chief of Staff) PM యొక్క ముఖ్య అధికారిక సలహాదారు. / Principal Secretary to PM (or Chief of Staff) is PM's senior official advisor."),

    (6, "hard",
     "NSA (జాతీయ భద్రతా సలహాదారు) ఎవరికి నేరుగా జవాబుదారీగా ఉంటారు? / NSA is directly answerable to whom?",
     "రక్షణ మంత్రి / Defence Minister",
     "ప్రధానమంత్రి / Prime Minister",
     "రాష్ట్రపతి / President",
     "CCS / CCS",
     "b",
     "NSA PM నేతృత్వంలోని CCS (Cabinet Committee on Security) కి జవాబుదారీ; ప్రత్యక్షంగా PM కి నివేదిస్తారు. / NSA reports to PM-chaired CCS; directly answers to PM."),

    (6, "easy",
     "PM కి సహాయపడే 'పీఎంఓ' అంటే ఏమిటి? / What does 'PMO' stand for?",
     "Prime Minister's Organization / ప్రధానమంత్రి సంస్థ",
     "Prime Minister's Office / ప్రధానమంత్రి కార్యాలయం",
     "Parliamentary Members' Office / పార్లమెంటు సభ్యుల కార్యాలయం",
     "Public Ministry Operations / ప్రజా మంత్రిత్వ కార్యకలాపాలు",
     "b",
     "PMO = Prime Minister's Office — PM కి పరిపాలనా సహాయం అందించే కార్యాలయం. / PMO = Prime Minister's Office — provides administrative support to PM."),

    (6, "medium",
     "పార్లమెంటరీ ప్రభుత్వ వ్యవస్థలో 'Cabinet' మరియు 'Council of Ministers' మధ్య తేడా ఏమిటి? / In parliamentary system, difference between Cabinet and Council of Ministers?",
     "రెండూ ఒకే విషయం / Both are same",
     "Cabinet = Cabinet Ministers మాత్రమే; CoM = Cabinet + MoS + Deputy Ministers / Cabinet = Cabinet Ministers only; CoM = Cabinet + MoS + Deputy Ministers",
     "CoM = Cabinet Ministers మాత్రమే / CoM = Cabinet Ministers only",
     "Cabinet = అన్ని మంత్రులు; CoM = Cabinet Ministers మాత్రమే / Cabinet = all ministers; CoM = Cabinet Ministers only",
     "b",
     "Council of Ministers (రాజ్యాంగ సంస్థ, Art.74) = Cabinet Ministers + Ministers of State + Deputy Ministers. Cabinet = కేవలం Cabinet Ministers — అన్నింటినీ నిర్ణయించే చిన్న సమూహం. / CoM (constitutional) = all 3 categories; Cabinet = Cabinet Ministers only — the inner decision-making body."),

    # ── Section 7: Miscellaneous / Constitutional Provisions ──────────────────
    (7, "easy",
     "మంత్రుల ప్రమాణ స్వీకారానికి రాజ్యాంగ అనుచ్ఛేదం ఏది? / Constitutional Article for ministers' oath?",
     "అనుచ్ఛేదం 74 / Art.74",
     "అనుచ్ఛేదం 75(4) / Art.75(4)",
     "అనుచ్ఛేదం 76 / Art.76",
     "అనుచ్ఛేదం 99 / Art.99",
     "b",
     "అనుచ్ఛేదం 75(4): మంత్రులు రాష్ట్రపతి ముందు ప్రమాణ స్వీకారం చేస్తారు. / Art.75(4): Ministers take oath before the President."),

    (7, "medium",
     "కేంద్ర మంత్రులు ఏ షెడ్యూల్‌లో ఉన్న ప్రమాణ పత్రం చదువుతారు? / Ministers take oath from which Schedule?",
     "మూడో షెడ్యూల్ / Third Schedule",
     "ఆరో షెడ్యూల్ / Sixth Schedule",
     "నాల్గో షెడ్యూల్ / Fourth Schedule",
     "మొదటి షెడ్యూల్ / First Schedule",
     "a",
     "తృతీయ షెడ్యూల్ (Third Schedule): PM మరియు మంత్రుల ప్రమాణ పత్రాలు ఉంటాయి. / Third Schedule contains oath forms for PM and ministers."),

    (7, "hard",
     "మంత్రిమండలిలో సభ్యుడు కాకుండా PM కింద ఉండే అత్యుత్తమ అధికారి ఎవరు? / Senior-most official under PM but not a minister?",
     "Principal Secretary to PM",
     "Cabinet Secretary / కేబినెట్ సెక్రటరీ",
     "Home Secretary / హోమ్ సెక్రటరీ",
     "Finance Secretary / ఆర్థిక సెక్రటరీ",
     "b",
     "Cabinet Secretary భారత పరిపాలనా సేవలో అత్యున్నత అధికారి; కేబినెట్ సెక్రటేరియట్ అధిపతి. / Cabinet Secretary is the senior-most IAS officer; heads Cabinet Secretariat."),

    (7, "medium",
     "సంకీర్ణ ప్రభుత్వంలో PM నియామకంలో రాష్ట్రపతి విచక్షణ అధికారం ఉంటుందా? / Does President have discretion in PM appointment in coalition govt?",
     "ఎప్పుడూ లేదు / Never",
     "కొంత మేరకు ఉంటుంది / Limited discretion exists",
     "పూర్తి విచక్షణ ఉంటుంది / Full discretion",
     "సుప్రీం కోర్ట్ నిర్ణయిస్తుంది / SC decides",
     "b",
     "సంకీర్ణ ప్రభుత్వంలో స్పష్టమైన మెజారిటీ లేనప్పుడు రాష్ట్రపతి PM నియామకంలో కొంత విచక్షణ వినియోగించవచ్చు. / In coalition with no clear majority, President has limited discretion in PM appointment."),

    (7, "easy",
     "PM గ్రహించే అధికారిక నివాసం ఏది? / What is PM's official residence?",
     "రాష్ట్రపతి భవన్ / Rashtrapati Bhavan",
     "7, లోక్ కల్యాణ్ మార్గ్ / 7, Lok Kalyan Marg",
     "సౌత్ బ్లాక్ / South Block",
     "హైదరాబాద్ హౌస్ / Hyderabad House",
     "b",
     "PM అధికారిక నివాసం 7, లోక్ కల్యాణ్ మార్గ్ (పూర్వం 7 రేస్ కోర్స్ రోడ్) న్యూ ఢిల్లీలో ఉంది. / PM's official residence is 7, Lok Kalyan Marg (formerly 7 Race Course Road), New Delhi."),

    (7, "hard",
     "లోక్‌సభలో మెజారిటీ కోల్పోయిన PM 'caretaker' హోదాలో పని చేయవచ్చు — ఏ పరిమితులతో? / A PM who lost LS majority can serve as 'caretaker' — with what restrictions?",
     "అన్ని అధికారాలు చెల్లుబాటు అవుతాయి / All powers remain valid",
     "రోజువారీ పాలన మాత్రమే; ముఖ్య నిర్ణయాలు కాదు / Only routine administration; no major decisions",
     "PM పదవి వెంటనే ఖాళీ అవుతుంది / PM office immediately vacated",
     "రాజ్యసభ ఆమోదంతో పని చేయవచ్చు / Can function with RS approval",
     "b",
     "లోక్‌సభ మెజారిటీ కోల్పోయిన PM రాజ్యాంగ ఆచారాన్ని అనుసరించి 'caretaker' హోదాలో రోజువారీ పాలన మాత్రమే చేయాలి. / PM losing LS majority continues as caretaker for routine administration only — convention, not law."),

    (7, "hard",
     "PM జీతం మరియు భత్యాలు ఏ చట్టం కింద నిర్ణయిస్తారు? / PM's salary and allowances are determined under which law?",
     "రాజ్యాంగంలో పేర్కొనబడ్డాయి / Specified in Constitution",
     "Salaries and Allowances of Ministers Act, 1952",
     "Parliament Members Salary Act",
     "Finance Minister నిర్ణయిస్తారు / Decided by Finance Minister",
     "b",
     "Salaries and Allowances of Ministers Act, 1952 కింద PM మరియు మంత్రుల జీతాలు నిర్ణయించబడతాయి. / PM's salary is determined under Salaries and Allowances of Ministers Act, 1952."),

    (7, "medium",
     "అనుచ్ఛేదం 78 కింద PM రాష్ట్రపతికి సమాచారం ఇవ్వాల్సిన విషయాలు ఏవి? / Under Art.78, PM must inform President about which matters?",
     "అన్ని మంత్రిమండలి నిర్ణయాలు మాత్రమే / All Cabinet decisions only",
     "Union వ్యవహారాలకు సంబంధించిన నిర్ణయాలు + రాష్ట్రపతి అడిగిన సమాచారం + వ్యక్తిగత మంత్రి నిర్ణయాలు (కేబినెట్ ముందుకు రాకపోయినా) / Decisions on Union affairs + info requested by President + individual minister decisions (even if not brought before Cabinet)",
     "కేవలం విదేశ విధానం నిర్ణయాలు / Only foreign policy decisions",
     "పార్లమెంటు కార్యక్రమాలు మాత్రమే / Only Parliamentary business",
     "b",
     "Art.78: PM యొక్క 3 విధులు — (a) Union వ్యవహారాల పాలనకు సంబంధించిన నిర్ణయాలు రాష్ట్రపతికి తెలియజేయడం; (b) రాష్ట్రపతి అడిగిన ఇతర సమాచారం ఇవ్వడం; (c) ఒక మంత్రి నిర్ణయించిన విషయాన్ని (కేబినెట్ ముందు పెట్టకపోయినా) రాష్ట్రపతి అడిగితే కేబినెట్ ముందు పెట్టడం. / Art.78: PM's 3 duties to President: (a) communicate CoM decisions; (b) furnish info requested; (c) if President requires, submit for Cabinet consideration any matter decided by a minister alone."),
]


def _seed_polity_ch17_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    ph = '%s' if use_postgres else '?'
    existing = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
        (_SUBJECT, _TOPIC, _CH))
    row = existing.fetchone()
    if row and not force:
        return

    sections_json = __import__('json').dumps(
        [{"title": s, "content": ""} for s in _SECTIONS],
        ensure_ascii=False
    )

    if row and force:
        note_id = row_to_dict_fn(row)['id']
        db_exec_fn(conn,
            f"UPDATE study_notes SET chapter_title_te={ph}, chapter_title_en={ph}, "
            f"pages_ref={ph}, sections_json={ph} WHERE id={ph}",
            (_TITLE_TE, _TITLE_EN, _PAGES, sections_json, note_id))
    else:
        db_exec_fn(conn,
            f"INSERT INTO study_notes (subject, topic, chapter_num, chapter_title_te, "
            f"chapter_title_en, pages_ref, sections_json) VALUES "
            f"({ph},{ph},{ph},{ph},{ph},{ph},{ph})",
            (_SUBJECT, _TOPIC, _CH, _TITLE_TE, _TITLE_EN, _PAGES, sections_json))


def _seed_polity_ch17_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = '%s' if use_postgres else '?'
    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4, 1: 1, 2: 2, 3: 3, 4: 4}

    note_cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
        (_SUBJECT, _TOPIC, _CH))
    note_row = note_cur.fetchone()
    if not note_row:
        return
    note_id = row_to_dict_fn(note_row)['id']

    existing = db_exec_fn(conn,
        f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    count = list(existing.fetchone())[0]
    if count > 0:
        return

    for row in _MCQS:
        sec_idx  = row[0]
        diff_int = diff_map.get(row[1], 1)
        q_te     = row[2]
        opt_a    = row[3]
        opt_b    = row[4]
        opt_c    = row[5]
        opt_d    = row[6]
        correct  = str(row[7]).lower()
        expl     = row[8] if len(row) > 8 else ''
        exam_type = row[9] if len(row) > 9 else 'General'

        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff_int, exam_type,
             q_te, opt_a, opt_b, opt_c, opt_d, correct, expl))
