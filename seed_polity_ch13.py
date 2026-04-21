# seed_polity_ch13.py
# Chapter 13 – Parliament: Lok Sabha & Rajya Sabha
# (పార్లమెంట్: లోక్‌సభ మరియు రాజ్యసభ)
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total Sections: 8 | Total MCQs: 65 | PYQs: 16
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# ─────────────────────────────────────────────────────

import json as _json

POLITY_CH13_SECTIONS = [
    {
        "title": "13.1 పార్లమెంట్ పరిచయం — నిర్మాణం",
        "sub": "Art.79–122 · Bicameral · Lok Sabha · Rajya Sabha · President",
        "audio": ""
    },
    {
        "title": "13.2 లోక్‌సభ — నిర్మాణం మరియు సభ్యత్వం",
        "sub": "Art.81 · 543 Seats · States · UTs · Duration · Quorum",
        "audio": ""
    },
    {
        "title": "13.3 లోక్‌సభ స్పీకర్ మరియు డిప్యూటీ స్పీకర్",
        "sub": "Art.93–94 · Election · Powers · Casting Vote · Removal",
        "audio": ""
    },
    {
        "title": "13.4 రాజ్యసభ — నిర్మాణం మరియు ప్రత్యేక అధికారాలు",
        "sub": "Art.80 · 250 Seats · 12 Nominated · Art.249 · Art.312 · Permanent House",
        "audio": ""
    },
    {
        "title": "13.5 రాజ్యసభ చైర్మన్ మరియు డిప్యూటీ చైర్మన్",
        "sub": "VP as Chairman · Art.89 · Deputy Chairman Election · Removal",
        "audio": ""
    },
    {
        "title": "13.6 సభ్యుల అర్హత మరియు అనర్హత",
        "sub": "Art.84 · Art.102 · 10th Schedule · Anti-Defection · 52nd Amendment",
        "audio": ""
    },
    {
        "title": "13.7 లోక్‌సభ vs రాజ్యసభ — పోలిక మరియు సంయుక్త సమావేశం",
        "sub": "Art.108 · Joint Sitting · Money Bill · Special Powers · Comparison",
        "audio": ""
    },
    {
        "title": "13.8 కఠిన ప్రశ్నలు — APPSC/UPSC PYQs",
        "sub": "Pro-tem Speaker · Privileges · Sessions · Dissolution · Art.100",
        "audio": ""
    },
]

POLITY_CH13_MCQS = [

    # ── Section 0: Parliament — Introduction ──────────────────────────────────────
    (0, 1,
     "భారత పార్లమెంట్ లో ఎన్ని సభలు ఉన్నాయి?\n(How many Houses does the Indian Parliament have?)",
     "ఒకటి (Unicameral)", "రెండు (Bicameral)",
     "మూడు (Tricameral)", "నాలుగు",
     "b",
     "భారత పార్లమెంట్ Bicameral (ద్విసభా) — (1) లోక్‌సభ (Lower House / House of the People) మరియు (2) రాజ్యసభ (Upper House / Council of States). రాష్ట్రపతి కూడా పార్లమెంట్ లో భాగం (Art.79). Art.79: 'There shall be a Parliament for the Union which shall consist of the President and two Houses.'"),

    (0, 1,
     "భారత రాజ్యాంగంలో పార్లమెంట్ కు సంబంధించిన నిబంధనలు ఏ భాగంలో (Part) ఉన్నాయి?\n(Parliament provisions are in which Part of the Constitution?)",
     "Part IV", "Part V",
     "Part VI", "Part VII",
     "b",
     "Part V (The Union) లో Articles 79–122 పార్లమెంట్ కు సంబంధించినవి. Art.79 = Constitution of Parliament. Art.80 = Composition of Rajya Sabha. Art.81 = Composition of Lok Sabha. Art.108 = Joint sitting. Art.110 = Money Bill definition."),

    (0, 2,
     "పార్లమెంట్ యొక్క ప్రధాన విధులు ఏవి?\n(What are the main functions of Parliament?)",
     "కేవలం చట్టాలు చేయడం",
     "చట్టాలు చేయడం, బడ్జెట్ ఆమోదించడం, కార్యనిర్వాహక వ్యవస్థపై నియంత్రణ, రాజ్యాంగ సవరణ",
     "కేవలం న్యాయ సమీక్ష",
     "రాష్ట్రాల మధ్య వివాదాలు పరిష్కరించడం",
     "b",
     "పార్లమెంట్ ముఖ్య విధులు: (1) Legislative — చట్టాలు చేయడం, (2) Financial — బడ్జెట్/Appropriation Bill ఆమోదించడం, (3) Executive oversight — No Confidence Motion, Questions, (4) Constitutional — Art.368 సవరణలు, (5) Electoral — President/VP ఎన్నికలో భాగం, (6) Judicial — Impeachment of President/Judges."),

    (0, 1,
     "రాష్ట్రపతి పార్లమెంట్ భాగమా?\n(Is the President a part of Parliament?)",
     "కాదు — రాష్ట్రపతి వేర్వేరు",
     "అవును — Art.79 ప్రకారం రాష్ట్రపతి పార్లమెంట్ లో భాగం",
     "కేవలం రాజ్యసభలో మాత్రమే భాగం",
     "కేవలం సమావేశాల సమయంలో మాత్రమే",
     "b",
     "Art.79: 'There shall be a Parliament for the Union which shall consist of the President and two Houses to be known respectively as the Council of States (Rajya Sabha) and the House of the People (Lok Sabha).' అంటే పార్లమెంట్ = రాష్ట్రపతి + రాజ్యసభ + లోక్‌సభ. కానీ రాష్ట్రపతి ఏ సభలోనూ సభ్యుడు కాదు."),

    # ── Section 1: Lok Sabha — Composition ───────────────────────────────────────
    (1, 1,
     "లోక్‌సభలో గరిష్ట సీట్ల సంఖ్య (రాజ్యాంగం ప్రకారం) ఎంత?\n(Maximum seats in Lok Sabha as per Constitution?)",
     "530", "543",
     "550", "552",
     "c",
     "Art.81 ప్రకారం: గరిష్టంగా 550 సీట్లు — 530 States + 20 UTs. ప్రస్తుతం Lok Sabha లో 543 elected seats ఉన్నాయి (530 states + 13 UTs). 104వ సవరణ 2020 ద్వారా Anglo-Indian nominated seats (2) తొలగించారు. కాబట్టి ఇప్పుడు total = 543 + 0 nominated = 543.",
     "APPSC"),

    (1, 1,
     "లోక్‌సభ పదవీ కాలం ఎంత?\n(What is the term of Lok Sabha?)",
     "3 సంవత్సరాలు", "4 సంవత్సరాలు",
     "5 సంవత్సరాలు", "6 సంవత్సరాలు",
     "c",
     "Art.83(2): లోక్‌సభ పదవీ కాలం మొదటి సమావేశం తేదీ నుండి 5 సంవత్సరాలు. అత్యవసర పరిస్థితి (National Emergency) అమలులో ఉన్నప్పుడు పార్లమెంట్ చట్టం ద్వారా ఒక సారికి 1 సంవత్సరం పొడిగించవచ్చు. రాష్ట్రపతి దీన్ని ముందే రద్దు (Dissolve) చేయగలదు."),

    (1, 1,
     "లోక్‌సభలో Quorum (కోరం) ఎంత?\n(What is the Quorum for Lok Sabha?)",
     "మొత్తు సభ్యత్వంలో 1/5వ వంతు",
     "మొత్తు సభ్యత్వంలో 1/10వ వంతు",
     "50 సభ్యులు",
     "100 సభ్యులు",
     "b",
     "Art.100(3): Quorum = మొత్తు సభ్యత్వంలో 1/10వ వంతు — లోక్‌సభకు 543 × 1/10 ≈ 55 సభ్యులు. రాజ్యసభకు 250 × 1/10 = 25 సభ్యులు. Quorum లేకుండా సభ కొనసాగుతే స్పీకర్ సభను వాయిదా వేయాలి. సాధారణంగా Quorum గురించి అభ్యంతరం లేకుండా సభ కొనసాగుతుంది."),

    (1, 2,
     "లోక్‌సభ సభ్యుడికి కనీస వయసు ఎంత?\n(Minimum age for Lok Sabha membership?)",
     "18 సంవత్సరాలు", "21 సంవత్సరాలు",
     "25 సంవత్సరాలు", "30 సంవత్సరాలు",
     "c",
     "Art.84(b): లోక్‌సభ సభ్యత్వానికి కనీస వయసు 25 సంవత్సరాలు. రాజ్యసభ సభ్యత్వానికి కనీస వయసు 30 సంవత్సరాలు. వోటింగ్ వయసు 18 సంవత్సరాలు (61వ సవరణ 1988). ముఖ్యమంత్రి/గవర్నర్ కు కనీస వయసు నిర్దిష్టంగా లేదు — కేవలం చట్టసభ సభ్యుడైతే చాలు.",
     "APPSC"),

    (1, 2,
     "104వ రాజ్యాంగ సవరణ 2020 లోక్‌సభకు సంబంధించి ఏమి మార్చింది?\n(What did the 104th Amendment 2020 change regarding Lok Sabha?)",
     "సీట్ల సంఖ్య 543 నుండి 550కు పెంచింది",
     "Anglo-Indian nominated seats (2) రద్దు చేసింది",
     "SC/ST రిజర్వేషన్లు పొడిగించింది",
     "లోక్‌సభ పదవీ కాలం 6 సంవత్సరాలకు పెంచింది",
     "b",
     "104వ రాజ్యాంగ సవరణ 2020: Art.331 (Lok Sabha లో Anglo-Indian nominated 2 seats) మరియు Art.333 (State Legislatures లో Anglo-Indian nominated seats) రద్దు చేసింది. ఆ seats 70 సంవత్సరాల వరకు (1950–2020) అందుబాటులో ఉన్నాయి. అదే సవరణ SC/ST రిజర్వేషన్లను మరో 10 సంవత్సరాలు (2030 వరకు) పొడిగించింది."),

    (1, 2,
     "జనాభా ఆధారంగా లోక్‌సభ నియోజకవర్గాల పునర్విభజన (Delimitation) ఏ జనాభా లెక్కల ఆధారంగా జరుగుతుంది?\n(Delimitation of LS constituencies is based on which Census?)",
     "1971 జనాభా లెక్కలు (frozen till 2026)",
     "2001 జనాభా లెక్కలు",
     "2011 జనాభా లెక్కలు",
     "ప్రతి 10 సంవత్సరాలకు స్వయంచాలకంగా మారుతుంది",
     "a",
     "42వ సవరణ 1976: Delimitation 2001 వరకు 1971 census ఆధారంగా freeze చేసింది. 84వ సవరణ 2001: 2026 వరకు 1971 census freeze పొడిగించింది. 2026 తర్వాత 2031 census ఆధారంగా Delimitation జరుగుతుంది. ఉద్దేశ్యం: జనాభా నియంత్రణ చేసిన రాష్ట్రాలు సీట్లు కోల్పోకుండా చేయడం."),

    # ── Section 2: Speaker & Deputy Speaker ──────────────────────────────────────
    (2, 1,
     "లోక్‌సభ స్పీకర్ ఎన్నికను ఏ ఆర్టికల్ నిర్దేశిస్తుంది?\n(Which Article provides for election of Lok Sabha Speaker?)",
     "Art.89", "Art.93",
     "Art.94", "Art.95",
     "b",
     "Art.93: The House of the People shall, as soon as may be, choose two members of the House to be respectively Speaker and Deputy Speaker. స్పీకర్ మరియు డిప్యూటీ స్పీకర్ ను లోక్‌సభ సభ్యులే సాధారణ మెజారిటీతో ఎన్నుకుంటారు. Art.94 = Speaker/DSpeaker పదవి ఖాళీ/తొలగింపు. Art.89 = Rajya Sabha Chairman & Deputy Chairman.",
     "APPSC"),

    (2, 1,
     "లోక్‌సభ స్పీకర్ Casting Vote ఎప్పుడు వినియోగిస్తారు?\n(When does the Lok Sabha Speaker use the Casting Vote?)",
     "ఎప్పుడైనా ఇష్టానుసారం",
     "సభలో సమాన ఓట్లు వచ్చినప్పుడు మాత్రమే (Tie)",
     "బడ్జెట్ ఓటింగ్ సమయంలో",
     "No Confidence Motion సమయంలో",
     "b",
     "Art.100(1): స్పీకర్ సాధారణంగా ఓటు చేయరు — కానీ సమాన ఓట్లు (Tie) వచ్చినప్పుడు Casting Vote (నిర్ణయాత్మక ఓటు) వేస్తారు. ఇది UK House of Commons స్పీకర్ తరహా. స్పీకర్ తన Casting Vote ఎలా వేయాలనే Convention: Status quo (ప్రస్తుత స్థితి) కొనసాగించే వైపు ఓటు వేయాలి."),

    (2, 2,
     "లోక్‌సభ స్పీకర్ ని తొలగించడానికి ఏ మెజారిటీ అవసరం?\n(What majority is needed to remove the Lok Sabha Speaker?)",
     "2/3 మెజారిటీ",
     "సాధారణ మెజారిటీ — కానీ 14 రోజుల ముందు నోటీసు తప్పనిసరి",
     "3/4 మెజారిటీ",
     "రాష్ట్రపతి ఆదేశంతో",
     "b",
     "Art.94: స్పీకర్ తొలగింపు — సభ తీర్మానం ద్వారా (Effective majority of total membership). 14 రోజుల ముందు నోటీసు తప్పనిసరి. ఆ 14 రోజుల్లో స్పీకర్ సభలో అధ్యక్షత వహించవచ్చు కానీ ఓటు వేయలేరు. స్పీకర్ పదవి ఖాళీగా ఉన్నప్పుడు డిప్యూటీ స్పీకర్ వ్యవహరిస్తారు.",
     "APPSC"),

    (2, 2,
     "కొత్త లోక్‌సభ సమావేశమైనప్పుడు, స్పీకర్ ఎన్నుక కాముందు సభను ఎవరు నడిపిస్తారు?\n(Who presides over Lok Sabha before the Speaker is elected in a new House?)",
     "అత్యంత సీనియర్ సభ్యుడు",
     "ముందు లోక్‌సభ స్పీకర్",
     "Pro-tem Speaker — రాష్ట్రపతి నియమిస్తారు",
     "Attorney General",
     "c",
     "Pro-tem Speaker: రాష్ట్రపతి సాధారణంగా అత్యంత సీనియర్ సభ్యుని (service-wise) Pro-tem Speaker గా నియమిస్తారు. Pro-tem Speaker విధి: సభ్యులకు ప్రమాణం చేయించడం మరియు స్పీకర్ ఎన్నిక నిర్వహించడం. స్పీకర్ ఎన్నికైన వెంటనే Pro-tem Speaker పదవి ముగుస్తుంది.",
     "APPSC"),

    (2, 2,
     "లోక్‌సభ సమావేశంలో లేనప్పుడు స్పీకర్ విధులను ఎవరు నిర్వహిస్తారు?\n(Who performs Speaker's duties when Speaker is absent from the House?)",
     "డిప్యూటీ స్పీకర్ (Deputy Speaker)",
     "ప్రధానమంత్రి",
     "సీనియర్ మంత్రి",
     "Attorney General",
     "a",
     "Art.95: స్పీకర్ లేదా డిప్యూటీ స్పీకర్ గైరుహాజరయ్యినప్పుడు, పార్లమెంట్ నిర్ణయించిన సభ్యుడు అధ్యక్షత వహిస్తాడు. సాధారణంగా డిప్యూటీ స్పీకర్ స్పీకర్ స్థానంలో వ్యవహరిస్తారు. Art.93 ప్రకారం డిప్యూటీ స్పీకర్ ని లోక్‌సభ సాధారణ మెజారిటీతో ఎన్నుకుంటుంది."),

    (2, 3,
     "స్పీకర్ తన స్వంత తొలగింపు తీర్మానం పెండింగ్ లో ఉన్నప్పుడు సభకు అధ్యక్షత వహించవచ్చా?\n(Can the Speaker preside when a resolution for their removal is pending?)",
     "అవును — సాధారణంగా అధ్యక్షత వహించగలరు",
     "కాదు — అధ్యక్షత వహించలేరు, కానీ సభలో ఉండవచ్చు మరియు ఓటు వేయవచ్చు\n(Cannot preside, but may be present and vote)",
     "కాదు — వెంటనే పదవి విడవాలి",
     "రాష్ట్రపతి అనుమతితో మాత్రమే అధ్యక్షత వహించవచ్చు",
     "b",
     "Art.94 proviso: While a resolution for removal of the Speaker is pending, the Speaker shall not, though present in the House, preside. అంటే: (1) స్పీకర్ అధ్యక్షత వహించలేరు, (2) కానీ సభలో ఉండవచ్చు, (3) సాధారణ ఓటు వేయవచ్చు (first instance లో) — Casting Vote కాదు, సాధారణ member గా ఓటు వేయగలరు. ఇది పదవి నుండి తొలగింపు కాదు — కేవలం presiding నిషేధం."),

    # ── Section 3: Rajya Sabha ────────────────────────────────────────────────────
    (3, 1,
     "రాజ్యసభలో గరిష్ట సీట్ల సంఖ్య ఎంత?\n(Maximum seats in Rajya Sabha?)",
     "238", "245",
     "250", "260",
     "c",
     "Art.80(1): రాజ్యసభలో గరిష్టంగా 250 సభ్యులు — 238 ఎన్నికైన + 12 రాష్ట్రపతి నామినేట్ చేసిన సభ్యులు. ప్రస్తుతం 245 సభ్యులు — 233 ఎన్నికైన + 12 నామినేట్. Art.80(1)(a): నామినేట్ సభ్యులు కళ, సాహిత్యం, విజ్ఞానం, సమాజ సేవలో ప్రత్యేక జ్ఞానం కలవారు."),

    (3, 1,
     "రాజ్యసభ పదవీ కాలం ఎంత — ఇది శాశ్వత సభ ఎందుకంటారు?\n(What is the term of RS members — why is it called a permanent body?)",
     "5 సంవత్సరాలు — రద్దు కాదు కాబట్టి",
     "6 సంవత్సరాలు — ప్రతి 2 సంవత్సరాలకు 1/3 సభ్యులు రిటైర్ అవుతారు",
     "4 సంవత్సరాలు — రద్దు చేయలేరు కాబట్టి",
     "3 సంవత్సరాలు",
     "b",
     "Art.83(1): రాజ్యసభ రద్దు (Dissolution) చేయలేరు — అందుకే 'Permanent House.' ప్రతి సభ్యుడి పదవీ కాలం 6 సంవత్సరాలు. ప్రతి 2 సంవత్సరాలకు 1/3 సభ్యులు రిటైర్ అయి, కొత్తవారు ఎన్నుకోబడతారు. రాజ్యసభ ఎన్నికలు రాష్ట్ర శాసనసభల ద్వారా (MLA లు) ఒకే బదిలీ ఓటు విధానం (Single Transferable Vote) లో జరుగుతాయి.",
     "APPSC"),

    (3, 2,
     "రాజ్యసభకు సభ్యత్వానికి కనీస వయసు ఎంత?\n(Minimum age for Rajya Sabha membership?)",
     "21 సంవత్సరాలు", "25 సంవత్సరాలు",
     "30 సంవత్సరాలు", "35 సంవత్సరాలు",
     "c",
     "Art.84(b): రాజ్యసభ సభ్యత్వానికి కనీస వయసు 30 సంవత్సరాలు. లోక్‌సభకు 25 సంవత్సరాలు. రాష్ట్ర శాసనసభ (Vidhan Sabha) కు 25 సంవత్సరాలు. రాష్ట్ర శాసన పరిషత్ (Vidhan Parishad) కు 30 సంవత్సరాలు. గవర్నర్ కు 35 సంవత్సరాలు. రాష్ట్రపతి కు 35 సంవత్సరాలు.",
     "APPSC"),

    (3, 2,
     "రాజ్యసభకు ఉన్న ప్రత్యేక అధికారం Art.249 ఏమిటి?\n(What is the special power of Rajya Sabha under Art.249?)",
     "Money Bill పై వీటో అధికారం",
     "రాజ్యసభ 2/3 మెజారిటీతో — రాష్ట్ర జాబితా అంశంపై పార్లమెంట్ చట్టం చేయడానికి అనుమతి",
     "No Confidence Motion పెట్టే అధికారం",
     "బడ్జెట్ ని నేరుగా తిరస్కరించే అధికారం",
     "b",
     "Art.249: Rajya Sabha 2/3 present & voting మెజారిటీతో 'National Interest' తీర్మానం చేస్తే, Parliament రాష్ట్ర జాబితా (State List) పై చట్టాలు చేయవచ్చు — ఒక సంవత్సరం పాటు, renewal సాధ్యం. Art.312: Rajya Sabha 2/3 మెజారిటీ తీర్మానంతో కొత్త All India Services సృష్టించవచ్చు."),

    (3, 2,
     "రాజ్యసభ నామినేట్ సభ్యులు (12) ఏ రంగాల నుండి నామినేట్ అవుతారు?\n(From which fields are the 12 nominated RS members?)",
     "న్యాయవాదులు మరియు న్యాయమూర్తులు",
     "కళ, సాహిత్యం, విజ్ఞానం, సమాజ సేవ",
     "పారిశ్రామికవేత్తలు మరియు వ్యవసాయదారులు",
     "రిటైర్డ్ IAS/IPS అధికారులు",
     "b",
     "Art.80(1)(a): రాష్ట్రపతి 12 మంది సభ్యులను నామినేట్ చేస్తారు — వారు 'literature, science, art and social service' లో ప్రత్యేక జ్ఞానం లేదా అనుభవం కలవారు. ఉదాహరణలు: Sachin Tendulkar (sports/art), Rekha (arts), M.S. Subbalakshmi. Lok Sabha లో nominated seats 104వ సవరణ 2020 తో రద్దయ్యాయి."),

    (3, 3,
     "రాజ్యసభ ఏ విషయంలో లోక్‌సభ కంటే ఎక్కువ అధికారం కలది?\n(In which matter does Rajya Sabha have MORE power than Lok Sabha?)",
     "Money Bill తిరస్కరించడంలో",
     "No Confidence Motion లో",
     "Art.249 (State List) మరియు Art.312 (All India Services) — రాజ్యసభ మాత్రమే తీర్మానం చేయగలదు",
     "బడ్జెట్ ఆమోదించడంలో",
     "c",
     "రాజ్యసభ ప్రత్యేక అధికారాలు (Exclusive powers): (1) Art.249 — రాష్ట్ర జాబితా పై Parliament చట్టానికి అనుమతి, (2) Art.312 — కొత్త All India Services సృష్టింపు. ఇవి రెండూ లోక్‌సభకు లేవు. ఇవి రాజ్యసభ 'Rajya' (రాష్ట్రాలు) రక్షక పాత్ర చూపిస్తాయి."),

    # ── Section 4: Rajya Sabha Chairman & Deputy Chairman ────────────────────────
    (4, 1,
     "రాజ్యసభ చైర్మన్ (Chairman) ఎవరు?\n(Who is the Chairman of Rajya Sabha?)",
     "లోక్‌సభ స్పీకర్", "ప్రధానమంత్రి",
     "ఉపరాష్ట్రపతి (Vice President)", "రాష్ట్రపతి",
     "c",
     "Art.89(1): ఉపరాష్ట్రపతి (Vice President) రాజ్యసభ పదవిపరంగా (ex-officio) చైర్మన్. ఉపరాష్ట్రపతి రాజ్యసభ సభ్యుడు కాదు — కేవలం అధ్యక్షత వహిస్తారు. ఉపరాష్ట్రపతి రాజ్యసభలో ఓటు వేయరు (Tie అయినప్పుడు మాత్రమే Casting Vote). లోక్‌సభ స్పీకర్ తో పోల్చితే ముఖ్యమైన తేడా: VP రాజ్యసభ సభ్యుడు కాదు."),

    (4, 2,
     "రాజ్యసభ డిప్యూటీ చైర్మన్ తొలగింపుకు ఏ మెజారిటీ అవసరం?\n(What majority is needed to remove the Deputy Chairman of Rajya Sabha?)",
     "2/3 మెజారిటీ",
     "సాధారణ మెజారిటీ — 14 రోజుల నోటీసు తో",
     "3/4 మెజారిటీ",
     "రాష్ట్రపతి ఆదేశంతో",
     "b",
     "Art.90: రాజ్యసభ డిప్యూటీ చైర్మన్ తొలగింపు — 14 రోజుల నోటీసు తో రాజ్యసభ తీర్మానం (Effective majority). Art.89(2): రాజ్యసభ స్వయంగా డిప్యూటీ చైర్మన్ ని ఎన్నుకుంటుంది. VP లేదా తన స్థానంలో వ్యవహరించే వ్యక్తి లేనప్పుడు Deputy Chairman అధ్యక్షత వహిస్తారు."),

    (4, 2,
     "ఉపరాష్ట్రపతి రాజ్యసభ చైర్మన్ పదవి వహిస్తున్నప్పుడు రాజ్యసభలో ఓటు వేయగలరా?\n(Can VP as RS Chairman vote in Rajya Sabha?)",
     "అవును, ఎప్పుడైనా",
     "కాదు — ఎప్పుడూ ఓటు వేయలేరు",
     "కేవలం Tie (సమాన ఓట్లు) అయినప్పుడు Casting Vote మాత్రమే",
     "కేవలం బడ్జెట్ ఓటింగ్ లో",
     "c",
     "Art.100(1): Chairman (VP) సాధారణంగా ఓటు వేయరు. Tie అయినప్పుడు మాత్రమే Casting Vote వేస్తారు. ఇది Speaker తో సమానమైన నిబంధన. VP రాజ్యసభ సభ్యుడు కాదు కాబట్టి సాధారణ ఓటు వేసే అర్హత లేదు."),

    (4, 2,
     "రాజ్యసభ చైర్మన్ (VP) తొలగింపు ఎలా జరుగుతుంది?\n(How is the RS Chairman (VP) removed?)",
     "రాజ్యసభ తీర్మానం ద్వారా",
     "లోక్‌సభ తీర్మానం ద్వారా",
     "రాజ్యసభ తీర్మానం + లోక్‌సభ ఆమోదం — ఉపరాష్ట్రపతి తొలగింపు విధానం",
     "రాష్ట్రపతి నిర్ణయంతో",
     "c",
     "VP తొలగింపు Art.67(b): రాజ్యసభ effective majority తీర్మానం + లోక్‌సభ simple majority ఆమోదం. 14 రోజుల ముందు నోటీసు RS కు ఇవ్వాలి. ఇది RS Deputy Chairman తొలగింపు (Art.90) కంటే భిన్నంగా ఉంటుంది. VP తన RS Chairman పదవికి సంబంధించి RS కి బాధ్యత వహిస్తాడు."),

    # ── Section 5: Qualifications & Disqualifications ────────────────────────────
    (5, 1,
     "పార్లమెంట్ సభ్యత్వానికి అనర్హత (Disqualification) ఏ ఆర్టికల్ లో ఉంది?\n(Disqualification for Parliament membership is under which Article?)",
     "Art.84", "Art.99",
     "Art.102", "Art.105",
     "c",
     "Art.102: పార్లమెంట్ సభ్యత్వానికి అనర్హత కారణాలు — (1) కేంద్ర/రాష్ట్ర ప్రభుత్వంలో లాభదాయక పదవి (Office of Profit), (2) పిచ్చివారు లేదా దివాళా, (3) భారత పౌరుడు కాదు, (4) పార్లమెంట్ చట్టం ద్వారా నిర్ణయించిన ఇతర అనర్హతలు, (5) 10వ షెడ్యూల్ ప్రకారం అనర్హత (Anti-Defection)."),

    (5, 2,
     "10వ షెడ్యూల్ (Anti-Defection Law) ఏ సవరణ ద్వారా జోడించారు?\n(10th Schedule / Anti-Defection Law was added by which Amendment?)",
     "42వ సవరణ 1976", "44వ సవరణ 1978",
     "52వ సవరణ 1985", "61వ సవరణ 1988",
     "c",
     "52వ రాజ్యాంగ సవరణ 1985: 10వ షెడ్యూల్ (Anti-Defection Law) జోడించారు — Rajiv Gandhi ప్రభుత్వం. పార్టీ మారిన లేదా పార్టీ ఆదేశాలకు వ్యతిరేకంగా ఓటు వేసిన సభ్యులు అనర్హులవుతారు. Kihoto Hollohan vs Zachillhu (1992) కేసు: Speaker/Chairman నిర్ణయం న్యాయ సమీక్షకు అర్హమైనది.",
     "APPSC"),

    (5, 2,
     "10వ షెడ్యూల్ ప్రకారం 'Merger' (విలీనం) కు కనీసం ఎంత మంది సభ్యులు అవసరం?\n(Under 10th Schedule, how many members are needed for a valid 'Merger'?)",
     "1/3 వంతు సభ్యులు", "1/2 వంతు సభ్యులు",
     "2/3 వంతు సభ్యులు", "3/4 వంతు సభ్యులు",
     "c",
     "91వ సవరణ 2003: 10వ షెడ్యూల్ సవరించింది — 'Split' (1/3 వంతు) అనర్హత నుండి మినహాయింపు తొలగించింది. కేవలం 2/3 వంతు సభ్యులు వేరే పార్టీలో 'Merger' చేసుకుంటే అనర్హత వర్తించదు. విభజన (Split) అనర్హతను నివారించే మార్గం కాదు.",
     "APPSC"),

    (5, 3,
     "'Office of Profit' (లాభదాయక పదవి) ఏది అనర్హతకు కారణమవుతుంది?\n(Which 'Office of Profit' causes disqualification?)",
     "ప్రభుత్వ కంపెనీలో డైరెక్టర్ పదవి",
     "పార్లమెంట్ చట్టం ద్వారా మినహాయింపు ఇవ్వని కేంద్ర/రాష్ట్ర ప్రభుత్వ లాభదాయక పదవి",
     "పార్టీ అధ్యక్ష పదవి",
     "యూనివర్శిటీ ఛాన్సలర్ పదవి",
     "b",
     "Art.102(1)(a): Government of India లేదా రాష్ట్ర ప్రభుత్వం కింద 'Office of Profit' కలిగి ఉంటే అనర్హత. అయితే Parliament by law ఆ పదవిని మినహాయింపు ఇవ్వవచ్చు. రాష్ట్రమంత్రి, PM వంటివి Office of Profit కావు — Parliament law లో exempt. Jaya Bachchan Case (2006): UP Film Development Council పదవి Office of Profit అయింది."),

    (5, 2,
     "సభ్యుడు స్వచ్ఛందంగా పార్టీ సభ్యత్వం వదులుకుంటే 10వ షెడ్యూల్ కింద అనర్హత వస్తుందా?\n(If a member voluntarily gives up party membership, does 10th Schedule disqualification apply?)",
     "కాదు — స్వచ్ఛంద రాజీనామా అనర్హత కాదు",
     "అవును — స్వచ్ఛంద రాజీనామా కూడా అనర్హతకు కారణం",
     "కేవలం RS సభ్యులకు మాత్రమే వర్తిస్తుంది",
     "రాష్ట్రపతి నిర్ణయం మేరకు",
     "b",
     "10వ షెడ్యూల్ Para 2(1)(a): పార్టీ సభ్యత్వం స్వచ్ఛందంగా వదులుకోవడం కూడా disqualification కారణం. 'Voluntarily giving up membership' అంటే formal resignation మాత్రమే కాదు — conduct ద్వారా కూడా resignation implied అవుతుంది (Ravi S. Naik Case). Speaker/Chairman నిర్ణయం judicial review కు అర్హమైనది."),

    # ── Section 6: LS vs RS & Joint Sitting ──────────────────────────────────────
    (6, 1,
     "Money Bill (ధన బిల్లు) ఏ సభలో మాత్రమే ప్రవేశపెట్టవచ్చు?\n(In which House only can a Money Bill be introduced?)",
     "రాజ్యసభలో మాత్రమే",
     "లోక్‌సభలో మాత్రమే",
     "రెండు సభల్లో ఏదైనా",
     "రాష్ట్రపతి నిర్ణయిస్తారు",
     "b",
     "Art.109: Money Bill లోక్‌సభలో మాత్రమే ప్రవేశపెట్టాలి. రాజ్యసభ Money Bill పై 14 రోజుల్లో తన సిఫారసులు పంపాలి లేదా అది passed అయినట్టే. రాజ్యసభ Money Bill ని తిరస్కరించలేదు — కేవలం suggestions మాత్రమే. Art.110: Money Bill నిర్వచనం. స్పీకర్ ఒక బిల్లు Money Bill అని certification ఇస్తారు — అది final."),

    (6, 1,
     "No Confidence Motion (అవిశ్వాస తీర్మానం) ఏ సభలో మాత్రమే పెట్టవచ్చు?\n(In which House only can a No Confidence Motion be moved?)",
     "రాజ్యసభలో మాత్రమే",
     "లోక్‌సభలో మాత్రమే",
     "రెండు సభల్లో",
     "ఏ సభలోనైనా PM నిర్ణయానుసారం",
     "b",
     "No Confidence Motion కేవలం లోక్‌సభలో మాత్రమే — ఎందుకంటే Council of Ministers లోక్‌సభకు మాత్రమే బాధ్యత వహిస్తుంది (Art.75(3)). లోక్‌సభలో No Confidence Motion pass అయితే మంత్రి మండలి రాజీనామా చేయాలి. రాజ్యసభలో Confidence Motion పెట్టే అధికారం లేదు."),

    (6, 2,
     "పార్లమెంట్ సంయుక్త సమావేశం (Joint Sitting) ఏ ఆర్టికల్ కింద జరుగుతుంది?\n(Joint Sitting of Parliament is under which Article?)",
     "Art.100", "Art.105",
     "Art.108", "Art.110",
     "c",
     "Art.108: Joint Sitting of both Houses — రాష్ట్రపతి పిలుపు మేరకు. లోక్‌సభ స్పీకర్ అధ్యక్షత వహిస్తారు. మూడు పరిస్థితుల్లో: (1) ఒక సభ బిల్లు తిరస్కరిస్తే, (2) అసమ్మతులు resolved కాకుండా 6 నెలలు గడిస్తే, (3) ఒక సభ ఆమోదించిన సవరణలను మరో సభ ఆమోదించకపోతే. Money Bill మరియు Constitution Amendment Bill కు Joint Sitting వర్తించదు."),

    (6, 2,
     "Joint Sitting లో నిర్ణయం ఎలా తీసుకుంటారు?\n(How is a decision taken in Joint Sitting?)",
     "రెండు సభల వేర్వేరు మెజారిటీలు కావాలి",
     "రెండు సభల్లో ఉపస్థిత సభ్యుల మొత్తం సాధారణ మెజారిటీ",
     "లోక్‌సభ మెజారిటీ మాత్రమే సరిపోతుంది",
     "2/3 మెజారిటీ అవసరం",
     "b",
     "Joint Sitting లో నిర్ణయం రెండు సభల మొత్తం ఉపస్థిత మరియు ఓటు వేసిన సభ్యుల సాధారణ మెజారిటీతో తీసుకుంటారు. లోక్‌సభలో 543 + రాజ్యసభలో 250 = 793 మొత్తం. ఇప్పటివరకు 3 సార్లు Joint Sitting జరిగింది: Dowry Prohibition 1961, Banking Service Commission 1978, POTA 2002."),

    (6, 3,
     "లోక్‌సభ మరియు రాజ్యసభ ల మధ్య తేడాలలో ఏది సరికాదు?\n(Which of the following is INCORRECT about LS vs RS?)",
     "Money Bill ని RS తిరస్కరించలేదు",
     "No Confidence Motion కేవలం LS లో పెట్టవచ్చు",
     "RS రద్దు చేయలేరు, LS రద్దు చేయవచ్చు",
     "RS Speaker కు RS Chairman కంటే ఎక్కువ అధికారాలు ఉంటాయి",
     "d",
     "LS Speaker మరియు RS Chairman కు తమ తమ సభలలో సమానమైన అధికారాలు ఉంటాయి. తేడా: Speaker RS సభ్యుడు కావచ్చు, Chairman (VP) RS సభ్యుడు కాదు. Anti-defection విషయంలో Speaker/Chairman తీర్పు ఇస్తారు. Speaker ఓటు: Casting Vote మాత్రమే; Chairman కూడా Casting Vote మాత్రమే."),

    (6, 2,
     "రాజ్యాంగ సవరణ బిల్లు (Constitution Amendment Bill) Joint Sitting లో pass చేయవచ్చా?\n(Can a Constitution Amendment Bill be passed in a Joint Sitting?)",
     "అవును — Joint Sitting లో pass అవుతుంది",
     "కాదు — రెండు సభల్లో వేర్వేరుగా Special Majority కావాలి",
     "కేవలం 42వ సవరణ తర్వాత Joint Sitting సాధ్యం",
     "రాష్ట్రపతి అనుమతితో Joint Sitting లో pass చేయవచ్చు",
     "b",
     "Art.368: Constitution Amendment Bill రెండు సభల్లో వేర్వేరుగా — 2/3 present & voting మెజారిటీ + total membership లో simple majority — ఆమోదం పొందాలి. Joint Sitting Art.108 వర్తించదు — Constitution Amendment Bills కు. Money Bills కు కూడా Joint Sitting వర్తించదు. కేవలం Ordinary Bills కు మాత్రమే Joint Sitting.",
     "APPSC"),

    # ── Section 7: Tough MCQs / PYQs ──────────────────────────────────────────────
    (7, 1,
     "పార్లమెంట్ Sessions (సమావేశాలు) ఎన్ని ఉంటాయి?\n(How many sessions does Parliament have in a year?)",
     "2 sessions", "3 sessions",
     "4 sessions", "నిర్ణీత సంఖ్య లేదు",
     "d",
     "రాజ్యాంగంలో Sessions సంఖ్య నిర్ణీతంగా లేదు. ఆచరణలో 3 sessions: (1) Budget Session (Feb–May), (2) Monsoon Session (July–Aug), (3) Winter Session (Nov–Dec). Art.85(1): రాష్ట్రపతి పార్లమెంట్ సమావేశపరచాలి — రెండు sessions మధ్య 6 నెలలకు మించకూడదు."),

    (7, 2,
     "APPSC PYQ: పార్లమెంట్ 'Privilege' (హక్కు) అంటే ఏమిటి?\n(What is Parliamentary 'Privilege'?)",
     "కేవలం MPs కు వర్తించే జీతం మరియు భత్యాలు",
     "సభలో మాట్లాడిన విషయంపై కోర్టులో వ్యాజ్యం పెట్టలేని స్వేచ్ఛ మరియు ఇతర ప్రత్యేక హక్కులు",
     "MP లను arrest చేయలేని హక్కు (సర్వకాల సర్వావస్థల)",
     "ప్రభుత్వ భూమి ఉచితంగా పొందే హక్కు",
     "b",
     "Art.105: Parliamentary Privileges — (1) Freedom of speech in Parliament (Art.105(1)), (2) సభలో మాట్లాడిన/ఓటు వేసిన విషయంపై court proceedings లేవు (Art.105(2)), (3) Contempt of House అధికారం. Parliamentary Privilege arrest immunity: Session సమయంలో civil cases లో మాత్రమే; criminal cases కు వర్తించదు.",
     "APPSC"),

    (7, 2,
     "APPSC PYQ: 'Prorogation' మరియు 'Dissolution' మధ్య తేడా ఏమిటి?\n(Difference between 'Prorogation' and 'Dissolution' of Parliament?)",
     "రెండూ ఒకటే",
     "Prorogation = Session ముగించడం (Pending business survives); Dissolution = లోక్‌సభ రద్దు (Pending Bills lapse)",
     "Dissolution = ఒక Session ముగించడం; Prorogation = Parliament రద్దు",
     "రెండూ రాజ్యసభకు వర్తిస్తాయి",
     "b",
     "Prorogation: రాష్ట్రపతి ఒక Session ముగిస్తారు — Pending business survive చేస్తుంది. Dissolution: లోక్‌సభ రద్దు — అన్ని Pending Bills (except RS లో pending అయినవి) lapse అవుతాయి. Adjournment: Speaker ఒక sitting ముగిస్తారు. Adjournment sine die: తదుపరి తేదీ నిర్ణయించకుండా.",
     "APPSC"),

    (7, 2,
     "APPSC PYQ: లోక్‌సభ స్పీకర్ కు సంబంధించి కింది వాటిలో సరైనది ఏది?\n(Which is correct about Lok Sabha Speaker?)",
     "స్పీకర్ లోక్‌సభ రద్దయిన తర్వాత వెంటనే పదవి ముగుస్తుంది",
     "స్పీకర్ లోక్‌సభ రద్దయినా కొత్త లోక్‌సభ మొదటి సమావేశం వరకు పదవిలో ఉంటారు",
     "స్పీకర్ రాజ్యసభను కూడా అధ్యక్షత వహించగలరు",
     "స్పీకర్ ని రాష్ట్రపతి నియమిస్తారు",
     "b",
     "Art.94 proviso: Speaker shall not vacate office until immediately before the first sitting of the new Lok Sabha. కాబట్టి Dissolution తర్వాత కూడా స్పీకర్ పదవిలో ఉంటారు — కొత్త లోక్‌సభ మొదటి Sitting వరకు. Joint Sitting కు స్పీకర్ అధ్యక్షత వహిస్తారు. స్పీకర్ లోక్‌సభ సభ్యులు ఎన్నుకుంటారు.",
     "APPSC"),

    (7, 3,
     "పార్లమెంట్ సభ్యత్వ అనర్హత విషయంలో నిర్ణయం ఎవరు తీసుకుంటారు?\n(Who decides on disqualification of a Parliament member?)",
     "సుప్రీం కోర్టు",
     "రాష్ట్రపతి — ఎన్నికల సంఘం అభిప్రాయం తీసుకుని",
     "స్పీకర్/చైర్మన్ — 10వ షెడ్యూల్ విషయంలో",
     "లోక్‌సభ మొత్తం ఓటు ద్వారా",
     "b",
     "Art.103: Art.102(1) కింద disqualification విషయంలో రాష్ట్రపతి నిర్ణయం చేస్తారు — Election Commission అభిప్రాయం తీసుకుని (binding). 10వ షెడ్యూల్ (Anti-Defection) విషయంలో Speaker/Chairman నిర్ణయం చేస్తారు. Kihoto Hollohan (1992): Speaker నిర్ణయం judicial review కు అర్హమైనది.",
     "APPSC"),

    (7, 2,
     "రాజ్యసభకు ఉన్న Art.312 ప్రత్యేక అధికారం ఏమిటి?\n(What is the special power of Rajya Sabha under Art.312?)",
     "Money Bill తిరస్కరించే అధికారం",
     "కొత్త రాష్ట్రాలు ఏర్పరచే అధికారం",
     "కొత్త All India Services సృష్టించే అధికారం — 2/3 మెజారిటీ తీర్మానంతో",
     "అత్యవసర పరిస్థితి ప్రకటించే అధికారం",
     "c",
     "Art.312: Rajya Sabha 2/3 present & voting మెజారిటీతో 'National Interest' తీర్మానం చేస్తే Parliament కొత్త All India Services సృష్టించవచ్చు. ప్రస్తుత All India Services: IAS, IPS, IFoS. ఇది RS యొక్క Rajya (States) రక్షక పాత్రలో ఒకటి.",
     "APPSC"),

    (7, 2,
     "లోక్‌సభలో ఒక బిల్లు — రాజ్యసభలో pending ఉన్న బిల్లు లోక్‌సభ రద్దయినప్పుడు lapse అవుతుందా?\n(Does a Bill pending in RS lapse when LS is dissolved?)",
     "రెండూ lapse అవుతాయి",
     "RS లో pending Bill lapse అవ్వదు — LS రద్దయినా",
     "LS లో pending Bill survive అవుతుంది",
     "అన్నీ lapse అవుతాయి",
     "b",
     "LS dissolution తో lapse అయ్యేవి: (1) LS లో pending Bills, (2) LS pass చేసి RS లో pending Bills. Lapse అవ్వనివి: (1) RS లో originated మరియు RS pass చేసి LS లో pending Bills (LS రద్దయినా), (2) President's assent కోసం pending Bills. RS లో pending Bills survive చేయడం RS పాత్ర ముఖ్యత చూపిస్తుంది."),

    (7, 1,
     "సంయుక్త సమావేశం (Joint Sitting) కు ఎవరు అధ్యక్షత వహిస్తారు?\n(Who presides over a Joint Sitting of Parliament?)",
     "రాష్ట్రపతి",
     "ప్రధానమంత్రి",
     "లోక్‌సభ స్పీకర్",
     "రాజ్యసభ చైర్మన్",
     "c",
     "Art.118(4): Joint Sitting అధ్యక్షత లోక్‌సభ స్పీకర్ వహిస్తారు. స్పీకర్ గైరుహాజరు అయినప్పుడు, డిప్యూటీ స్పీకర్ అధ్యక్షత వహిస్తారు. ఇప్పటివరకు జరిగిన 3 Joint Sittings: 1. Dowry Prohibition Bill 1961, 2. Banking Service Commission Repeal Bill 1978, 3. POTA 2002.",
     "APPSC"),

    (7, 2,
     "పార్లమెంట్ సభ్యుల జీతభత్యాలు (Salaries) ఏ నిధి నుండి చెల్లిస్తారు?\n(Salaries of Parliament members are paid from which fund?)",
     "Contingency Fund of India",
     "Public Account of India",
     "Consolidated Fund of India",
     "State Disaster Response Fund",
     "c",
     "MPs జీతభత్యాలు, స్పీకర్ జీతం, Deputy Speaker జీతం — అన్నీ Consolidated Fund of India నుండి చెల్లిస్తారు. Parliament by law MPs జీతాలు నిర్ణయిస్తుంది (Members of Parliament (Salaries and Allowances) Act 1954)."),

    (7, 2,
     "APPSC PYQ: రాజ్యసభ 'Permanent House' అయినా దాని సభ్యులు ఒకేసారి రిటైర్ కావరు — ఎందుకు?\n(Even though RS is permanent, members don't all retire together — why?)",
     "ప్రతి సంవత్సరం 1/4 మంది రిటైర్ అవుతారు",
     "ప్రతి 2 సంవత్సరాలకు 1/3 మంది రిటైర్ అవుతారు",
     "ప్రతి 3 సంవత్సరాలకు 1/2 మంది రిటైర్ అవుతారు",
     "అందరూ 6 సంవత్సరాల తర్వాత ఒకేసారి రిటైర్ అవుతారు",
     "b",
     "Art.83(1) + RS నిబంధన: రాజ్యసభ Staggered retirement — ప్రతి 2 సంవత్సరాలకు 1/3 సభ్యులు రిటైర్ అవుతారు. ఇది సభ Continuity కి భరోసా. పూర్తిగా కొత్త సభ్యులతో RS ఎప్పుడూ పని చేయదు. అందుకే 'Permanent House' — రద్దు అవ్వదు.",
     "APPSC"),

    (7, 2,
     "పార్లమెంట్ సభ్యుడికి విద్యార్హత (Educational Qualification) అవసరమా?\n(Is Educational Qualification required to become a Parliament member?)",
     "అవును — కనీసం గ్రాడ్యుయేట్ అవసరం",
     "అవును — Matriculation అవసరం",
     "కాదు — రాజ్యాంగం విద్యార్హత నిర్ణయించలేదు",
     "కాలేజ్ డిగ్రీ RS కు, Matriculation LS కు",
     "c",
     "Art.84: పార్లమెంట్ సభ్యత్వానికి విద్యార్హత అవసరం లేదు. అవసరమైన అర్హతలు: (1) భారత పౌరుడు, (2) LS కు 25 / RS కు 30 సంవత్సరాలు వయసు, (3) Parliament చేసిన అర్హతలు (Representation of People Act).",
     "APPSC"),

    # ── Extra Section 1: Lok Sabha ─────────────────────────────────────────────────
    (1, 2,
     "లోక్‌సభలో SC మరియు ST కు రిజర్వేషన్లు ఏ ఆర్టికల్ కింద ఉన్నాయి?\n(SC/ST reservations in Lok Sabha are under which Article?)",
     "Art.15", "Art.16",
     "Art.330", "Art.332",
     "c",
     "Art.330: లోక్‌సభలో SC మరియు ST లకు రిజర్వేషన్ సీట్లు. Art.332: రాష్ట్ర శాసనసభలలో SC/ST రిజర్వేషన్లు. ప్రస్తుతం LS లో SC కు 84, ST కు 47 రిజర్వేషన్ సీట్లు. 104వ సవరణ 2020 ఈ రిజర్వేషన్లను 2030 వరకు పొడిగించింది. OBC కు పార్లమెంట్ లో రాజ్యాంగ రిజర్వేషన్ లేదు.",
     "APPSC"),

    (1, 2,
     "లోక్‌సభకు నేరుగా ఎన్నిక పద్ధతి (Electoral System) ఏది?\n(What electoral system is used for Lok Sabha elections?)",
     "Proportional Representation — Single Transferable Vote",
     "First Past the Post (FPTP) — Simple Plurality",
     "List System",
     "Two Round System",
     "b",
     "లోక్‌సభ ఎన్నికలు FPTP (First Past The Post) పద్ధతిలో జరుగుతాయి — అత్యధిక ఓట్లు పొందిన అభ్యర్థి విజయి. రాజ్యసభ ఎన్నికలు Single Transferable Vote (STV) పద్ధతి. రాష్ట్రపతి ఎన్నిక STV పద్ధతి. FPTP పద్ధతిలో majority కాకుండా plurality (మిగతావారికంటే ఎక్కువ) సరిపోతుంది."),

    (1, 3,
     "ఏ రాష్ట్రానికి లోక్‌సభలో అత్యధిక సీట్లు ఉన్నాయి?\n(Which state has the highest number of Lok Sabha seats?)",
     "మహారాష్ట్ర (48)", "పశ్చిమ బెంగాల్ (42)",
     "ఉత్తర ప్రదేశ్ (80)", "రాజస్థాన్ (25)",
     "c",
     "ఉత్తర ప్రదేశ్ (UP) కు లోక్‌సభలో అత్యధిక 80 సీట్లు ఉన్నాయి — జనాభా ఆధారంగా. మహారాష్ట్ర 48, పశ్చిమ బెంగాల్ 42, బిహార్ 40. ఆంధ్రప్రదేశ్ కు 25 సీట్లు (2014 విభజన తర్వాత). తెలంగాణకు 17 సీట్లు. సిక్కిం మరియు మిజోరం కు 1-1 సీటు (అతి తక్కువ)."),

    (1, 2,
     "లోక్‌సభలో రాష్ట్ర ప్రతినిధిత్వం ఏ ఆధారంగా నిర్ణయిస్తారు?\n(Basis for state representation in Lok Sabha?)",
     "సమాన ప్రాతినిధ్యం — అన్ని రాష్ట్రాలకు సమాన సీట్లు",
     "జనాభా ఆధారంగా — అనుపాత ప్రాతినిధ్యం",
     "రాష్ట్ర విస్తీర్ణం ఆధారంగా",
     "రాష్ట్ర ఆదాయం ఆధారంగా",
     "b",
     "Art.81(2): లోక్‌సభలో రాష్ట్ర సీట్లు జనాభా ఆధారంగా నిర్ణయిస్తారు (అనుపాత ప్రాతినిధ్యం). ప్రతి రాష్ట్రానికి కనీసం 1 సీటు హామీ ఉంది. కానీ చిన్న రాష్ట్రాలకు (Goa, Sikkim వంటి) జనాభా కంటే ఎక్కువ ప్రాతినిధ్యం ఉంటుంది proportionally. రాజ్యసభలో మాత్రం ప్రతి రాష్ట్రానికి జనాభా ఆధారంగా allocate అవుతుంది (Art.80)."),

    # ── Extra Section 2: Speaker powers ───────────────────────────────────────────
    (2, 2,
     "లోక్‌సభ స్పీకర్ ఒక బిల్లు 'Money Bill' అని నిర్ణయించే అధికారం ఎవరికి ఉంది?\n(Who has the final authority to certify a Bill as 'Money Bill'?)",
     "రాష్ట్రపతి", "ప్రధానమంత్రి",
     "లోక్‌సభ స్పీకర్", "సుప్రీం కోర్టు",
     "c",
     "Art.110(3): స్పీకర్ నిర్ణయం final — ఒక బిల్లు Money Bill అని certification ఇస్తే అది ప్రశ్నించలేరు. Aadhaar Bill 2016 ని స్పీకర్ Money Bill గా certified చేసారు — Supreme Court దీన్ని Rojer Mathew vs South Indian Bank (2019) కేసులో సమీక్షించింది. Speaker certification judicial review కి అర్హమైనదా అన్న విషయం controversial."),

    (2, 3,
     "స్పీకర్ Casting Vote సాంప్రదాయం (Convention) ప్రకారం ఎలా వేయాలి?\n(According to convention, how should the Speaker cast the Casting Vote?)",
     "ఎప్పుడూ ప్రభుత్వకు అనుకూలంగా",
     "ఎప్పుడూ ప్రతిపక్షానికి అనుకూలంగా",
     "Status quo కొనసాగించే వైపు — మరింత చర్చ సాధ్యమయ్యే వైపు",
     "స్పీకర్ ఇష్టానుసారం",
     "c",
     "British Parliamentary convention (భారతదేశంలో కూడా పాటిస్తారు): Speaker Casting Vote 'Status quo' కొనసాగించే వైపు వేయాలి. అంటే: (1) Bill ని reject చేసే తీర్మానం Tie అయితే — Reject కాదు (bill remain pending), (2) Bill passage కు Tie అయితే — bill pass కాదు. ఇది further debate కి అవకాశం ఇస్తుంది."),

    # ── Extra Section 3: Rajya Sabha details ──────────────────────────────────────
    (3, 2,
     "రాజ్యసభ సభ్యుల ఎన్నికలో ఏ పద్ధతి అనుసరిస్తారు?\n(What method is used to elect Rajya Sabha members?)",
     "Direct election by voters",
     "First Past the Post (FPTP)",
     "Single Transferable Vote (STV) by MLAs",
     "Nomination by President",
     "c",
     "రాజ్యసభ సభ్యులను రాష్ట్ర శాసనసభ సభ్యులు (MLAs) Single Transferable Vote (Proportional Representation) పద్ధతిలో ఎన్నుకుంటారు. Art.80(4). UT లకు (Delhi, Puducherry) కూడా RS ఎన్నికలు జరుగుతాయి — UT Legislature members ఓటు వేస్తారు. నామినేటెడ్ LS సభ్యులు RS ఎన్నికలలో ఓటు వేయలేరు."),

    (3, 2,
     "ఏ రాష్ట్రానికి రాజ్యసభలో అత్యధిక సీట్లు ఉన్నాయి?\n(Which state has the most Rajya Sabha seats?)",
     "మహారాష్ట్ర", "పశ్చిమ బెంగాల్",
     "ఉత్తర ప్రదేశ్", "తమిళనాడు",
     "c",
     "ఉత్తర ప్రదేశ్ కు రాజ్యసభలో అత్యధిక 31 సీట్లు ఉన్నాయి. మహారాష్ట్ర 19, తమిళనాడు 18, పశ్చిమ బెంగాల్ 16. ఆంధ్రప్రదేశ్ కు 11, తెలంగాణకు 7 సీట్లు. సిక్కిం, మిజోరం, నాగాల్యాండ్, గోవా — 1-1 సీటు. జమ్మూ కాశ్మీర్ రాష్ట్ర హోదా తొలగింపు (2019) తర్వాత RS seats frozen."),

    # ── Extra Section 5: Disqualification cases ──────────────────────────────────
    (5, 2,
     "ఒక Independent MP (స్వతంత్ర సభ్యుడు) ఏదైనా పార్టీలో చేరితే Anti-Defection వర్తిస్తుందా?\n(If an Independent MP joins a party after election, does Anti-Defection apply?)",
     "కాదు — Independent MPs కు Anti-Defection లేదు",
     "అవును — ఏదైనా పార్టీలో చేరితే వెంటనే అనర్హులవుతారు",
     "6 నెలల్లో చేరితే మాత్రమే అనర్హత",
     "Speaker నిర్ణయంపై ఆధారపడి ఉంటుంది",
     "b",
     "10వ షెడ్యూల్ Para 2(2): ఒక సభ్యుడు Independent గా ఎన్నికైన తర్వాత ఏదైనా రాజకీయ పార్టీలో చేరితే అనర్హులవుతారు. ఎందుకంటే ఓటర్లు వారిని Independent గా ఎన్నుకున్నారు. Nominated members (RS): ఎన్నికైన తర్వాత 6 నెలల్లో ఏదైనా పార్టీలో చేరవచ్చు — అనర్హత లేదు."),

    (5, 3,
     "Anti-Defection చట్టంలో 'whip' ని ఉల్లంఘించడం అంటే ఏమిటి?\n(What constitutes violation of 'whip' under Anti-Defection law?)",
     "పార్లమెంట్ కు గైరుహాజరు",
     "పార్టీ whip కు వ్యతిరేకంగా ఓటు వేయడం లేదా ఓటింగ్ లో abstain అవడం",
     "ప్రతిపక్ష నేతతో మాట్లాడడం",
     "మీడియాలో పార్టీని విమర్శించడం",
     "b",
     "10వ షెడ్యూల్ Para 2(1)(b): పార్టీ whip కు వ్యతిరేకంగా ఓటు వేయడం లేదా ఓటింగ్ లో పాల్గొనకపోవడం (Abstention against whip) అనర్హత కారణం. అయితే: పార్టీ ముందస్తుగా అనుమతి ఇస్తే లేదా తర్వాత condone చేస్తే అనర్హత వర్తించదు. Whip ప్రాముఖ్యత: Budget vote, No Confidence Motion లలో."),

    # ── Extra Section 6: More LS vs RS ────────────────────────────────────────────
    (6, 2,
     "Financial Bill (ఆర్థిక బిల్లు) మరియు Money Bill మధ్య తేడా ఏమిటి?\n(Difference between Financial Bill and Money Bill?)",
     "రెండూ ఒకటే",
     "Money Bill కేవలం Art.110 items మాత్రమే; Financial Bill అదే + ఇతర నిబంధనలు కూడా కలిగి ఉంటుంది",
     "Financial Bill RS లో ప్రవేశపెట్టవచ్చు, Money Bill కాదు",
     "Financial Bill అధ్యక్ష ఆమోదం అవసరం, Money Bill కాదు",
     "b",
     "Money Bill (Art.110): కేవలం taxation, borrowing, Consolidated Fund expenditure మొదలైన విషయాలకు మాత్రమే సంబంధించినది. Financial Bill: Money Bill items + ఇతర విషయాలు (like ordinary legislation) కలిసి ఉంటాయి. Financial Bill ని RS తిరస్కరించగలదు — Money Bill వలె కాదు. Financial Bill కు Joint Sitting వర్తించవచ్చు."),

    (6, 2,
     "Ordinance (అధ్యాదేశం) పార్లమెంట్ సమావేశంలో లేనప్పుడు జారీ చేయగలరు — ఎవరు?\n(Who can issue an Ordinance when Parliament is not in session?)",
     "ప్రధానమంత్రి", "లోక్‌సభ స్పీకర్",
     "రాష్ట్రపతి — Art.123 కింద", "Attorney General",
     "c",
     "Art.123: పార్లమెంట్ recess లో ఉన్నప్పుడు రాష్ట్రపతి Ordinances జారీ చేయగలరు — Cabinet సిఫారసు మేరకు. Ordinance బలం చట్టంతో సమానం. పార్లమెంట్ తిరిగి సమావేశమైన తేదీ నుండి 6 వారాల్లో Ordinance ని రద్దు చేయకపోతే లేదా ఆమోదించకపోతే అది automatic గా expire అవుతుంది. RC Cooper Case (1970): Ordinance తీర్మానం judicial review కు అర్హమైనది."),

    (6, 3,
     "పార్లమెంట్ 'Question Hour' మరియు 'Zero Hour' తేడా:\n(Difference between Question Hour and Zero Hour in Parliament?)",
     "రెండూ ఒకటే",
     "Question Hour = మొదటి గంట, ముందస్తు నోటీసుతో మంత్రుల నుండి సమాధానాలు; Zero Hour = 12 గంటల తర్వాత, ముందస్తు నోటీసు లేకుండా అత్యవసర విషయాలు",
     "Zero Hour = మొదటి గంట; Question Hour = చివరి గంట",
     "Zero Hour కేవలం RS లో, Question Hour కేవలం LS లో",
     "b",
     "Question Hour: ప్రతి రోజు మొదటి గంట (11–12), ముందస్తు నోటీసుతో Starred/Unstarred/Short Notice Questions. Starred Questions: Oral answer, Supplementary questions అనుమతి. Zero Hour: 12 గంటల తర్వాత, ముందస్తు నోటీసు లేకుండా అత్యవసర విషయాలు లేవనెత్తవచ్చు. Zero Hour రాజ్యాంగంలో లేదు — Parliamentary convention."),

    # ── Extra Section 0/7 ─────────────────────────────────────────────────────────
    (0, 2,
     "పార్లమెంట్ Supremacy అంటే ఏమిటి — భారత్ లో వర్తిస్తుందా?\n(What is Parliamentary Supremacy — does it apply in India?)",
     "అవును — UK వలె పార్లమెంట్ సర్వోన్నతం",
     "కాదు — భారత్ లో రాజ్యాంగ సర్వోన్నతత (Constitutional Supremacy) వర్తిస్తుంది",
     "రాష్ట్రపతి సర్వోన్నతత వర్తిస్తుంది",
     "న్యాయవ్యవస్థ సర్వోన్నతత వర్తిస్తుంది",
     "b",
     "భారత్ లో రాజ్యాంగ సర్వోన్నతత (Constitutional Supremacy) వర్తిస్తుంది — UK వలె Parliament Supremacy కాదు. పార్లమెంట్ రాజ్యాంగ విరుద్ధమైన చట్టాలు చేయలేదు (Art.13). Court రాజ్యాంగ విరుద్ధ చట్టాలను వ్యర్థం (void) చేయగలదు. అదే సమయంలో, Parliament రాజ్యాంగ సవరణ అధికారం కలది (Art.368) — Basic Structure వరకు."),

    (7, 3,
     "UPSC Style: పార్లమెంట్ యొక్క 'Contempt of House' అధికారం గురించి:\n(Regarding Parliament's power of 'Contempt of House'?)",
     "కేవలం సభ్యులు ఈ అధికారాన్ని వినియోగించగలరు",
     "సభ బయటి వ్యక్తులు పార్లమెంట్ ని contempt చేయలేరు",
     "పార్లమెంట్ కు సభలో లేదా బయట దాని గౌరవాన్ని దెబ్బతీసే చర్యలకు శిక్షించే అధికారం ఉంది",
     "Contempt of House court విషయంలో మాత్రమే వర్తిస్తుంది",
     "c",
     "Art.105(3): Parliamentary Privileges include power to punish for contempt — సభలో మాట్లాడిన వారు, బయటి వారు (journalist, citizen) కూడా contempt of Parliament కు గురి కావచ్చు. Contempt అంటే: సభ పని ఆటంకపరచడం, సభ్యులను బెదిరించడం, సభ వ్యవహారాలను తప్పుగా రిపోర్ట్ చేయడం. Privilege Committee ఈ కేసులు పరిశీలిస్తుంది.",
     "UPSC"),

    (7, 2,
     "APPSC PYQ: లోక్‌సభ స్పీకర్ పదవి ఖాళీ అయితే డిప్యూటీ స్పీకర్ కు ఏమి జరుగుతుంది?\n(If the post of Speaker falls vacant, what happens to the Deputy Speaker?)",
     "డిప్యూటీ స్పీకర్ స్వయంచాలకంగా స్పీకర్ అవుతారు",
     "డిప్యూటీ స్పీకర్ స్పీకర్ విధులు నిర్వహిస్తారు — కొత్త స్పీకర్ ఎన్నిక వరకు",
     "సీనియర్ మంత్రి అధ్యక్షత వహిస్తారు",
     "Pro-tem Speaker నియమించాలి",
     "b",
     "Art.95(1): స్పీకర్ పదవి ఖాళీ అయినప్పుడు (resign, removal, vacancy), డిప్యూటీ స్పీకర్ స్పీకర్ విధులు నిర్వహిస్తారు — కొత్త స్పీకర్ ఎన్నికయ్యే వరకు. డిప్యూటీ స్పీకర్ కూడా లేనప్పుడు, Parliament నిర్ణయించిన వ్యక్తి అధ్యక్షత వహిస్తాడు. స్వయంచాలకంగా స్పీకర్ అవ్వరు.",
     "APPSC"),

    (7, 2,
     "రాజ్యసభలో 'Special Majority' (ప్రత్యేక మెజారిటీ) అవసరమయ్యే తీర్మానాలు:\n(Which Rajya Sabha resolutions require Special Majority?)",
     "రాష్ట్రపతి అభిశంసన",
     "Art.249 (State List legislation) మరియు Art.312 (New AIS)",
     "No Confidence Motion",
     "Budget ఆమోదం",
     "b",
     "రాజ్యసభకు Art.249 మరియు Art.312 కింద 2/3 present & voting majority తీర్మానాలు: ఇవి Special Majority అవసరమయ్యే RS exclusive powers. రాష్ట్రపతి అభిశంసన రెండు సభల్లో 2/3 majority కావాలి. Budget మరియు Ordinary resolutions: Simple majority సరిపోతుంది."),
]


# ─────────────────────────────────────────────
#  SEED FUNCTIONS
# ─────────────────────────────────────────────

def _seed_polity_ch13_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    ph = '%s' if use_postgres else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT 'Indian_Polity',
            subtopic TEXT DEFAULT '',
            chapter_num INTEGER NOT NULL,
            chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '',
            pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if use_postgres: conn.commit()
    except Exception:
        pass

    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (13, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch13 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (13, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 13,
         'పార్లమెంట్: లోక్‌సభ మరియు రాజ్యసభ',
         'Parliament: Lok Sabha & Rajya Sabha',
         'Ch.13',
         _json.dumps(POLITY_CH13_SECTIONS, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch13 notes seeded!'}


def _seed_polity_ch13_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = '%s' if use_postgres else '?'
    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4,
                1: 1, 2: 2, 3: 3, 4: 4}

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
        (13, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch13_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (13, 'Indian_Polity'))
        row = cur.fetchone()

    note_id = row_to_dict_fn(row)['id']
    db_exec_fn(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, exam_type, "
        f"q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )

    easy = medium = hard = toughest = pyq = 0
    for mcq in POLITY_CH13_MCQS:
        sec_idx, diff, q, a, b, c, d, correct, expl = mcq[:9]
        exam_type = mcq[9] if len(mcq) > 9 else 'General'
        diff_int = diff_map.get(diff, diff)
        db_exec_fn(conn, insert_sql,
                   (note_id, sec_idx, diff_int, exam_type,
                    q, a, b, c, d, str(correct).lower(), expl))
        if exam_type in ('APPSC', 'UPSC'):
            pyq += 1
        elif diff_int == 1: easy += 1
        elif diff_int == 2: medium += 1
        elif diff_int == 3: hard += 1
        elif diff_int == 4: toughest += 1

    if use_postgres: conn.commit()
    conn.commit()

    total = len(POLITY_CH13_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch13 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
