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

    # ══════════════ SECTION 0 — Parliament Overview ══════════════

    (0, 1,
     "How many Houses does the Indian Parliament have?\nతెలుగు: భారత పార్లమెంట్‌లో ఎన్ని సభలు ఉన్నాయి?",
     "One (Unicameral) / ఒకటి",
     "Two (Bicameral) / రెండు (Bicameral) (correct)",
     "Three (Tricameral) / మూడు",
     "Four / నాలుగు",
     "b",
     "Indian Parliament is BICAMERAL — Lok Sabha (Lower House) + Rajya Sabha (Upper House) + the President (technically also part of Parliament under Art.79)."),

    (0, 1,
     "Parliament provisions are in which Part of the Constitution?\nతెలుగు: పార్లమెంట్ నిబంధనలు ఏ భాగంలో ఉన్నాయి?",
     "Part IV / భాగం IV",
     "Part V / భాగం V (correct — Articles 79-122)",
     "Part VI / భాగం VI",
     "Part VII / భాగం VII",
     "b",
     "Part V (Articles 52-151) covers the Union — Parliament is Articles 79-122. Part IV = DPSP; Part VI = the States."),

    (0, 2,
     "What are the main functions of Parliament?\nతెలుగు: పార్లమెంట్ ప్రధాన విధులు?",
     "Only making laws / కేవలం చట్టాలు",
     "Legislation, Budget approval, Executive control, Constitutional amendment / చట్టాలు + బడ్జెట్ + కార్యనిర్వాహక నియంత్రణ + సవరణ (correct)",
     "Only judicial review / కేవలం న్యాయ సమీక్ష",
     "Settling state disputes / రాష్ట్రాల మధ్య వివాదాలు",
     "b",
     "Parliament has 4 main functions: (1) Legislative — making laws, (2) Financial — Budget, (3) Executive control — accountability of CoM, (4) Constituent — amendments under Art.368."),

    (0, 1,
     "Is the President a part of Parliament?\nతెలుగు: రాష్ట్రపతి పార్లమెంట్‌లో భాగమా?",
     "No, separate / కాదు",
     "Yes — Art.79 says President is part of Parliament / అవును, Art.79 ప్రకారం (correct)",
     "Only in Rajya Sabha / కేవలం రాజ్యసభ",
     "Only during sessions / కేవలం సమావేశాల సమయంలో",
     "b",
     "Article 79: 'There shall be a Parliament for the Union which shall consist of the PRESIDENT and two Houses (Council of States + House of the People).' President is integral part of Parliament."),

    (0, 2,
     "What is Parliamentary Supremacy — does it apply in India?\nతెలుగు: పార్లమెంట్ Supremacy భారత్‌లో ఉందా?",
     "Yes, like UK Parliament is supreme / అవును, UK వలె",
     "No — India has Constitutional Supremacy, not Parliamentary / లేదు; భారత్‌లో రాజ్యాంగ సర్వోన్నతత (correct)",
     "Presidential Supremacy applies / రాష్ట్రపతి",
     "Judicial Supremacy applies / న్యాయ వ్యవస్థ",
     "b",
     "India follows CONSTITUTIONAL SUPREMACY (Constitution is supreme; Parliament can be checked by courts via Judicial Review). UK alone has Parliamentary Supremacy."),

    # ══════════════ SECTION 1 — Lok Sabha ══════════════

    (1, 1,
     "Maximum seats in Lok Sabha as per Constitution? [APPSC]\nతెలుగు: లోక్‌సభ గరిష్ఠ సీట్లు?",
     "530",
     "543",
     "550 (correct — Constitutional max)",
     "552",
     "c",
     "Constitutional maximum = 550 (530 from states + 20 from UTs). Currently 543 elected. (Earlier 552 included 2 Anglo-Indian nominated — abolished by 104th Amendment 2020.)",
     "APPSC"),

    (1, 1,
     "Term of Lok Sabha?\nతెలుగు: లోక్‌సభ పదవీకాలం?",
     "3 years / 3 సం.",
     "4 years / 4 సం.",
     "5 years / 5 సం. (correct)",
     "6 years / 6 సం.",
     "c",
     "Lok Sabha term = 5 years from its first sitting. President can dissolve it earlier. Term can be extended by 1 year at a time during National Emergency."),

    (1, 1,
     "What is the Quorum for Lok Sabha?\nతెలుగు: లోక్‌సభ Quorum?",
     "1/5 of total membership / 1/5",
     "1/10 of total membership / 1/10 (correct)",
     "50 members / 50 సభ్యులు",
     "100 members / 100 సభ్యులు",
     "b",
     "Article 100: Quorum for both Houses = 1/10 of TOTAL membership. For LS that's ~55 members; for RS ~25."),

    (1, 2,
     "Minimum age for Lok Sabha membership? [APPSC]\nతెలుగు: లోక్‌సభ సభ్యుడికి కనీస వయసు?",
     "18 years / 18",
     "21 years / 21",
     "25 years / 25 (correct)",
     "30 years / 30",
     "c",
     "Article 84: minimum age = 25 for LS, 30 for RS.",
     "APPSC"),

    (1, 2,
     "What did the 104th Amendment 2020 change about Lok Sabha?\nతెలుగు: 104వ సవరణ 2020 ఏ మార్పు?",
     "Increased seats 543 → 550 / సీట్లు పెంపు",
     "Abolished Anglo-Indian nominated seats (2) / Anglo-Indian (2) రద్దు (correct)",
     "Extended SC/ST reservation / రిజర్వేషన్లు పొడిగింపు",
     "Term increased to 6 years / 6 సం. కు పెంపు",
     "b",
     "104th Amendment 2020: (1) ABOLISHED 2 Anglo-Indian nominated seats in LS, (2) EXTENDED SC/ST reservation by 10 more years (until 2030)."),

    (1, 2,
     "Lok Sabha constituency delimitation is based on which Census?\nతెలుగు: లోక్‌సభ నియోజకవర్గాలు ఏ census?",
     "1971 Census (frozen till 2026) / 1971 (correct)",
     "2001 Census",
     "2011 Census",
     "Auto-updates every 10 years",
     "a",
     "84th Amendment 2001 + 87th Amendment 2003 froze delimitation based on 1971 Census until 2026 (later extended). This prevents penalising population-control states."),

    (1, 2,
     "SC/ST reservations in Lok Sabha are under which Article? [APPSC]\nతెలుగు: SC/ST రిజర్వేషన్లు ఏ ఆర్టికల్?",
     "Art.15",
     "Art.16",
     "Art.330 (correct)",
     "Art.332",
     "c",
     "Art.330 = SC/ST reservations in Lok Sabha. Art.332 = SC/ST reservations in State Legislative Assemblies.",
     "APPSC"),

    (1, 2,
     "Electoral system used for Lok Sabha?\nతెలుగు: లోక్‌సభ ఎన్నిక పద్ధతి?",
     "Proportional Representation — STV / PR-STV",
     "First Past the Post (FPTP) / FPTP (correct)",
     "List System / List",
     "Two Round System / Two Round",
     "b",
     "Lok Sabha uses FPTP (Simple Plurality). Whoever gets most votes wins, regardless of majority. Same as UK House of Commons. Rajya Sabha uses STV."),

    (1, 3,
     "Which state has the most Lok Sabha seats?\nతెలుగు: లోక్‌సభలో అత్యధిక సీట్లు ఉన్న రాష్ట్రం?",
     "Maharashtra (48) / మహారాష్ట్ర",
     "West Bengal (42) / పశ్చిమ బెంగాల్",
     "Uttar Pradesh (80) / ఉత్తర ప్రదేశ్ (correct)",
     "Rajasthan (25) / రాజస్థాన్",
     "c",
     "UP has 80 LS seats (highest). Maharashtra=48, West Bengal=42, Bihar=40, Tamil Nadu=39."),

    (1, 2,
     "Basis for state representation in Lok Sabha?\nతెలుగు: లోక్‌సభలో రాష్ట్ర ప్రాతినిధ్యం ఆధారం?",
     "Equal representation / సమాన ప్రాతినిధ్యం",
     "Proportional to population / జనాభా ఆధారిత అనుపాత ప్రాతినిధ్యం (correct)",
     "Based on state area / విస్తీర్ణం",
     "Based on state revenue / ఆదాయం",
     "b",
     "LS seats are allocated proportionally based on POPULATION (frozen at 1971 Census). UP largest population = most seats; small states fewer. (Rajya Sabha is similar but per-state basis.)"),

    # ══════════════ SECTION 2 — Lok Sabha Speaker ══════════════

    (2, 1,
     "Election of Lok Sabha Speaker is provided in which Article? [APPSC]\nతెలుగు: లోక్‌సభ స్పీకర్ ఎన్నిక ఏ ఆర్టికల్?",
     "Art.89",
     "Art.93 (correct)",
     "Art.94",
     "Art.95",
     "b",
     "Art.93 = Speaker + Deputy Speaker of Lok Sabha. Art.89 = Chairman of Rajya Sabha. Art.94 = removal of Speaker. Art.95 = Speaker functions when post vacant.",
     "APPSC"),

    (2, 1,
     "When does the Lok Sabha Speaker use the Casting Vote?\nతెలుగు: స్పీకర్ Casting Vote ఎప్పుడు?",
     "Anytime at will / ఎప్పుడైనా",
     "Only when there is a tie / Tie అయినప్పుడు మాత్రమే (correct)",
     "During budget voting / బడ్జెట్ సమయంలో",
     "During no-confidence motion / అవిశ్వాస తీర్మానం",
     "b",
     "Speaker normally does NOT vote. The casting vote is used ONLY to break a tie. Convention: Speaker votes for the status quo (no change)."),

    (2, 2,
     "Majority needed to remove the Lok Sabha Speaker? [APPSC]\nతెలుగు: స్పీకర్ తొలగింపుకు మెజారిటీ?",
     "2/3 majority / 2/3",
     "Simple Majority — with 14 days notice / సాధారణ; 14 రోజుల నోటీసు (correct)",
     "3/4 majority / 3/4",
     "President's order / రాష్ట్రపతి ఆదేశం",
     "b",
     "Speaker can be removed by a SIMPLE MAJORITY of all then-members of LS (Art.94), with at least 14 days' advance notice. Same applies to Deputy Speaker.",
     "APPSC"),

    (2, 2,
     "Who presides over Lok Sabha before the Speaker is elected in a new House? [APPSC]\nతెలుగు: కొత్త లోక్‌సభలో స్పీకర్ ఎన్నుకాముందు?",
     "Senior-most member / సీనియర్ సభ్యుడు",
     "Previous Speaker / గత స్పీకర్",
     "Pro-tem Speaker — appointed by President / Pro-tem Speaker (correct)",
     "Attorney General / AG",
     "c",
     "PRO-TEM SPEAKER (usually senior-most MP) appointed by the President to preside until a new Speaker is elected. Pro-tem also administers oath to new MPs.",
     "APPSC"),

    (2, 2,
     "Who performs Speaker's duties when Speaker is absent?\nతెలుగు: స్పీకర్ లేనప్పుడు ఎవరు?",
     "Deputy Speaker / డిప్యూటీ స్పీకర్ (correct)",
     "Prime Minister / PM",
     "Senior Minister / సీనియర్ మంత్రి",
     "Attorney General / AG",
     "a",
     "Deputy Speaker presides in the Speaker's absence. If both Speaker and Deputy Speaker are absent, a member from the Panel of Chairpersons takes over."),

    (2, 3,
     "Can the Speaker preside when a removal resolution is pending against them?\nతెలుగు: తొలగింపు తీర్మానం pending అయితే స్పీకర్ అధ్యక్షత వహించవచ్చా?",
     "Yes, normally / అవును",
     "No — cannot preside, but may be present and vote / కాదు; కానీ పాల్గొనవచ్చు, ఓటు వేయవచ్చు (correct)",
     "Must immediately resign / వెంటనే రాజీనామా",
     "Only with President's permission / రాష్ట్రపతి అనుమతితో",
     "b",
     "Article 96: Speaker CANNOT preside while their own removal resolution is being considered. But CAN attend, speak, and vote on it (including the casting vote if needed)."),

    (2, 2,
     "Final authority to certify a Bill as a 'Money Bill'?\nతెలుగు: 'Money Bill' అని ఎవరు నిర్ణయిస్తారు?",
     "President / రాష్ట్రపతి",
     "Prime Minister / PM",
     "Lok Sabha Speaker / లోక్‌సభ స్పీకర్ (correct)",
     "Supreme Court / సుప్రీం కోర్టు",
     "c",
     "Article 110(3): Speaker's certification that a Bill is a Money Bill is FINAL — cannot be questioned in any court (per the Constitution)."),

    (2, 3,
     "How should the Speaker cast the Casting Vote per convention?\nతెలుగు: Casting Vote సాంప్రదాయం?",
     "Always for the government / ప్రభుత్వకు అనుకూలం",
     "Always for the opposition / ప్రతిపక్షానికి",
     "For status quo — to allow further discussion / Status quo వైపు (correct)",
     "Speaker's discretion / ఇష్టానుసారం",
     "c",
     "Convention: Speaker votes to MAINTAIN the existing position (status quo) — typically against motions, allowing further deliberation. Borrowed from UK Speaker's tradition."),

    # ══════════════ SECTION 3 — Rajya Sabha ══════════════

    (3, 1,
     "Maximum seats in Rajya Sabha?\nతెలుగు: రాజ్యసభ గరిష్ఠ సీట్లు?",
     "238",
     "245",
     "250 (correct — Constitutional max)",
     "260",
     "c",
     "Constitutional maximum = 250 (238 elected from states/UTs + 12 nominated by President). Currently 245."),

    (3, 1,
     "Term of Rajya Sabha members? Why is RS called permanent? [APPSC]\nతెలుగు: రాజ్యసభ పదవీకాలం + శాశ్వత సభ ఎందుకు?",
     "5 years — not dissolved / 5 సం.",
     "6 years — 1/3 retire every 2 years / 6 సం.; ప్రతి 2 సం. 1/3 retire (correct)",
     "4 years — cannot dissolve / 4 సం.",
     "3 years / 3 సం.",
     "b",
     "Rajya Sabha members serve 6-year terms. 1/3 of members retire every 2 years — so RS itself never dissolves. Hence called 'PERMANENT HOUSE'.",
     "APPSC"),

    (3, 2,
     "Minimum age for Rajya Sabha membership? [APPSC]\nతెలుగు: రాజ్యసభ సభ్యుడికి కనీస వయసు?",
     "21 / 21",
     "25 / 25",
     "30 / 30 (correct)",
     "35 / 35",
     "c",
     "Article 84: 30 for RS, 25 for LS.",
     "APPSC"),

    (3, 2,
     "Special power of Rajya Sabha under Art.249?\nతెలుగు: Art.249 ప్రత్యేక అధికారం?",
     "Veto over Money Bills / Money Bill వీటో",
     "RS can — by 2/3 majority — authorise Parliament to legislate on State List / 2/3 తీర్మానం, రాష్ట్ర జాబితాపై చట్టం (correct)",
     "Power to move No-Confidence / అవిశ్వాస తీర్మానం",
     "Power to reject Budget / బడ్జెట్ తిరస్కరణ",
     "b",
     "Article 249: RS can pass a resolution by 2/3 majority of members present and voting that a State List subject is in 'national interest' — empowering Parliament to legislate on it for 1 year (renewable)."),

    (3, 2,
     "From which fields are the 12 nominated RS members chosen?\nతెలుగు: 12 nominated సభ్యులు ఏ రంగాల?",
     "Lawyers and judges / న్యాయవాదులు",
     "Art, Literature, Science, Social Service / కళ, సాహిత్యం, విజ్ఞానం, సమాజ సేవ (correct)",
     "Industrialists and farmers / పారిశ్రామికవేత్తలు",
     "Retired IAS/IPS / IAS/IPS",
     "b",
     "Article 80(3): President nominates 12 members from among persons distinguished in LITERATURE, SCIENCE, ART, and SOCIAL SERVICE."),

    (3, 3,
     "In which matter does Rajya Sabha have MORE power than Lok Sabha?\nతెలుగు: రాజ్యసభకు ఎక్కువ అధికారం?",
     "Rejecting Money Bills / Money Bill తిరస్కరణ",
     "No-Confidence Motion / అవిశ్వాస తీర్మానం",
     "Art.249 (State List) and Art.312 (All India Services) — only RS can pass / Art.249 + Art.312 (correct)",
     "Budget approval / బడ్జెట్",
     "c",
     "Two EXCLUSIVE RS powers (LS cannot do these): (1) Art.249 — authorise Parliament on State List subject, (2) Art.312 — create new All-India Services. Both need 2/3 RS majority."),

    (3, 2,
     "What method is used to elect Rajya Sabha members?\nతెలుగు: రాజ్యసభ ఎన్నిక పద్ధతి?",
     "Direct election by voters / ప్రజలు నేరుగా",
     "FPTP / FPTP",
     "Single Transferable Vote (STV) by MLAs / STV ద్వారా MLAs (correct)",
     "Nomination by President / రాష్ట్రపతి",
     "c",
     "Members of State Legislative Assemblies (MLAs) elect RS members from their state using STV (Single Transferable Vote — proportional representation). Indirect election."),

    (3, 2,
     "Which state has the most Rajya Sabha seats?\nతెలుగు: రాజ్యసభలో అత్యధిక సీట్లు?",
     "Maharashtra / మహారాష్ట్ర",
     "West Bengal / పశ్చిమ బెంగాల్",
     "Uttar Pradesh / ఉత్తర ప్రదేశ్ (correct — 31)",
     "Tamil Nadu / తమిళనాడు",
     "c",
     "UP = 31 RS seats (highest). Maharashtra=19, Tamil Nadu=18, West Bengal=16, Bihar=16."),

    # ══════════════ SECTION 4 — Rajya Sabha Chairman ══════════════

    (4, 1,
     "Who is the Chairman of Rajya Sabha?\nతెలుగు: రాజ్యసభ చైర్మన్ ఎవరు?",
     "LS Speaker / లోక్‌సభ స్పీకర్",
     "Prime Minister / PM",
     "Vice President / ఉపరాష్ట్రపతి (correct)",
     "President / రాష్ట్రపతి",
     "c",
     "Article 64: VICE PRESIDENT of India is the ex-officio Chairman of Rajya Sabha. Deputy Chairman is elected from RS members."),

    (4, 2,
     "Majority needed to remove the Deputy Chairman of Rajya Sabha?\nతెలుగు: డిప్యూటీ చైర్మన్ తొలగింపు మెజారిటీ?",
     "2/3 majority / 2/3",
     "Simple Majority — with 14 days notice / సాధారణ; 14 రోజుల నోటీసు (correct)",
     "3/4 majority / 3/4",
     "President's order / రాష్ట్రపతి",
     "b",
     "Deputy Chairman is removed by SIMPLE MAJORITY of all then-members of RS, with 14 days' advance notice."),

    (4, 2,
     "Can the VP (as RS Chairman) vote in Rajya Sabha?\nతెలుగు: VP రాజ్యసభలో ఓటు వేయగలరా?",
     "Yes anytime / అవును, ఎప్పుడైనా",
     "No, never / ఎప్పుడూ లేదు",
     "Only Casting Vote during a Tie / కేవలం Tie అయినప్పుడు Casting Vote (correct)",
     "Only on Budget / కేవలం బడ్జెట్",
     "c",
     "VP/RS Chairman is NOT a member of RS — so does not have a regular vote. Only has CASTING VOTE in case of a tie (Article 100)."),

    (4, 2,
     "How is the RS Chairman (VP) removed?\nతెలుగు: VP తొలగింపు?",
     "Resolution by RS only / RS మాత్రమే",
     "Resolution by LS only / LS మాత్రమే",
     "RS resolution by majority of all then-members + LS agreement / RS తీర్మానం + LS ఆమోదం (correct)",
     "President decides / రాష్ట్రపతి",
     "c",
     "Article 67(b): VP is removed by a resolution passed by an EFFECTIVE majority in RS (majority of all then-members) AND AGREED to by LS — unique procedure (no impeachment needed)."),

    # ══════════════ SECTION 5 — Disqualification & Anti-Defection ══════════════

    (5, 1,
     "Disqualification for Parliament membership is under which Article?\nతెలుగు: సభ్యత్వ అనర్హత ఆర్టికల్?",
     "Art.84",
     "Art.99",
     "Art.102 (correct)",
     "Art.105",
     "c",
     "Art.102 = Disqualifications for membership of Parliament (office of profit, unsoundness of mind, undischarged insolvent, non-citizen, etc.). Art.84 = Qualifications. 10th Schedule = Anti-Defection."),

    (5, 2,
     "10th Schedule (Anti-Defection Law) was added by which Amendment? [APPSC]\nతెలుగు: 10వ షెడ్యూల్ ఏ సవరణ?",
     "42nd Amendment 1976",
     "44th Amendment 1978",
     "52nd Amendment 1985 (correct)",
     "61st Amendment 1988",
     "c",
     "52nd Constitutional Amendment 1985 added the Tenth Schedule under Rajiv Gandhi's government — to deter party-hopping and political instability.",
     "APPSC"),

    (5, 2,
     "Under 10th Schedule, how many members are needed for a valid 'Merger'? [APPSC]\nతెలుగు: 'Merger' కోసం?",
     "1/3 / 1/3",
     "1/2 / 1/2",
     "2/3 / 2/3 (correct)",
     "3/4 / 3/4",
     "c",
     "After 91st Amendment 2003: 'Merger' exception requires 2/3 OR MORE members of the original party to merge with another. (Earlier 1/3 was enough — exploited as 'split' loophole, now removed.)",
     "APPSC"),

    (5, 3,
     "Which 'Office of Profit' causes disqualification?\nతెలుగు: 'Office of Profit' అనర్హత?",
     "Govt company director / ప్రభుత్వ కంపెనీ director",
     "Central/State government office of profit NOT exempted by Parliament law / మినహాయింపు లేని కేంద్ర/రాష్ట్ర పదవి (correct)",
     "Party president post / పార్టీ అధ్యక్ష",
     "University Chancellor post / Chancellor",
     "b",
     "Art.102(1)(a): A Central or State government 'office of profit' disqualifies, UNLESS Parliament law specifically exempts that office (e.g., Minister, Speaker)."),

    (5, 2,
     "If a member voluntarily gives up party membership, does 10th Schedule apply?\nతెలుగు: స్వచ్ఛందంగా పార్టీ సభ్యత్వం వదులుకుంటే?",
     "No / కాదు",
     "Yes — voluntary resignation also = disqualification / అవును (correct)",
     "Only for RS members / కేవలం RS",
     "President decides / రాష్ట్రపతి",
     "b",
     "Para 2(1)(a) of 10th Schedule: voluntary giving up of party membership = disqualification. Includes implied conduct (e.g., joining/supporting a different party publicly)."),

    (5, 2,
     "If an Independent MP joins a party, does Anti-Defection apply?\nతెలుగు: Independent MP పార్టీ చేరితే?",
     "No / కాదు",
     "Yes — joining any party causes disqualification / అవును (correct)",
     "Only if within 6 months / 6 నెలల్లో",
     "Speaker decides / Speaker నిర్ణయం",
     "b",
     "Independent MPs CANNOT join any party post-election under Para 2(2) of 10th Schedule. If they do, they're disqualified."),

    (5, 3,
     "What constitutes violation of 'whip' under Anti-Defection law?\nతెలుగు: 'Whip' ఉల్లంఘన?",
     "Absence from Parliament / గైరుహాజరు",
     "Voting against party whip OR abstaining / Whip కి వ్యతిరేకంగా ఓటు / abstain (correct)",
     "Talking with opposition / ప్రతిపక్షంతో",
     "Criticising party in media / మీడియాలో విమర్శ",
     "b",
     "Para 2(1)(b): Voting/abstaining contrary to the whip's direction = disqualification, unless the party condones it within 15 days."),

    # ══════════════ SECTION 6 — Bills, Joint Sitting, LS-RS Differences ══════════════

    (6, 1,
     "In which House only can a Money Bill be introduced?\nతెలుగు: Money Bill ఏ సభలో?",
     "Rajya Sabha only / రాజ్యసభ",
     "Lok Sabha only / లోక్‌సభ మాత్రమే (correct)",
     "Either House / రెండు సభల్లో",
     "President decides / రాష్ట్రపతి",
     "b",
     "Article 110(1): Money Bill can be introduced ONLY in LOK SABHA (after President's recommendation). RS can only suggest amendments (which LS may accept/reject) within 14 days."),

    (6, 1,
     "In which House only can a No-Confidence Motion be moved?\nతెలుగు: అవిశ్వాస తీర్మానం ఏ సభలో?",
     "Rajya Sabha only / రాజ్యసభ",
     "Lok Sabha only / లోక్‌సభ మాత్రమే (correct)",
     "Either House / రెండు",
     "Wherever PM decides / PM నిర్ణయం",
     "b",
     "No-Confidence Motion can be moved ONLY in LS — because the Council of Ministers is collectively responsible to LS (Art.75(3)), not RS."),

    (6, 2,
     "Joint Sitting of Parliament is under which Article?\nతెలుగు: సంయుక్త సమావేశం?",
     "Art.100",
     "Art.105",
     "Art.108 (correct)",
     "Art.110",
     "c",
     "Article 108: President can summon a JOINT SITTING in case of disagreement between LS and RS over an ordinary Bill (NOT for Money Bill, NOT for Constitutional Amendment Bill)."),

    (6, 2,
     "How is a decision taken in a Joint Sitting?\nతెలుగు: Joint Sitting నిర్ణయం?",
     "Separate majorities in both Houses / రెండు సభల వేర్వేరు మెజారిటీలు",
     "Simple majority of total members present and voting in both Houses combined / రెండు సభల కలిపి సాధారణ మెజారిటీ (correct)",
     "Lok Sabha majority alone / LS మెజారిటీ",
     "2/3 majority needed / 2/3",
     "b",
     "Joint Sitting decision = simple majority of TOTAL members present and voting from both Houses combined. LS dominance helps Government (LS = 543 vs RS = 245)."),

    (6, 3,
     "Which is INCORRECT about LS vs RS?\nతెలుగు: సరికానిది ఏది?",
     "RS cannot reject Money Bill / RS Money Bill తిరస్కరించలేదు",
     "No-Confidence only in LS / No-Confidence కేవలం LS",
     "RS not dissolved; LS can be dissolved / RS రద్దు లేదు; LS రద్దు",
     "RS Speaker has more powers than RS Chairman / RS Speaker కు ఎక్కువ అధికారం (INCORRECT — RS has Chairman, not Speaker)",
     "d",
     "Option D is INCORRECT — Rajya Sabha has a CHAIRMAN (Vice President), NOT a 'Speaker'. The other three statements are correct."),

    (6, 2,
     "Can a Constitution Amendment Bill be passed in a Joint Sitting? [APPSC]\nతెలుగు: రాజ్యాంగ సవరణ Joint Sitting?",
     "Yes / అవును",
     "No — both Houses need separate Special Majority / రెండు సభల్లో ప్రత్యేక మెజారిటీ (correct)",
     "Only after 42nd Amendment / 42వ సవరణ తర్వాత",
     "With President's permission / రాష్ట్రపతి అనుమతితో",
     "b",
     "Joint Sitting (Art.108) does NOT apply to Constitution Amendment Bills (Art.368) or Money Bills (Art.110). Constitutional Amendments need Special Majority in BOTH Houses separately.",
     "APPSC"),

    (6, 2,
     "Difference between Financial Bill and Money Bill?\nతెలుగు: Financial Bill vs Money Bill తేడా?",
     "Both same / రెండూ ఒకటే",
     "Money Bill = Art.110 items only; Financial Bill = those + other provisions / Money Bill = Art.110 మాత్రమే; Financial = + ఇతరం (correct)",
     "Financial in RS, Money in LS only / తారుమారు",
     "Financial needs President's assent only / తారుమారు",
     "b",
     "Money Bill = Bill containing ONLY matters listed in Art.110(1)(a-g). Financial Bill = Bill that contains some Art.110 matters PLUS other provisions. Both are introduced in LS."),

    (6, 2,
     "Who can issue an Ordinance when Parliament is not in session?\nతెలుగు: Ordinance ఎవరు?",
     "Prime Minister / PM",
     "LS Speaker / Speaker",
     "President — under Art.123 / రాష్ట్రపతి, Art.123 (correct)",
     "Attorney General / AG",
     "c",
     "Art.123: PRESIDENT can issue Ordinances when Parliament is NOT in session. The Ordinance must be approved by both Houses within 6 weeks of reassembly, otherwise it lapses."),

    (6, 3,
     "Difference between Question Hour and Zero Hour?\nతెలుగు: Question Hour vs Zero Hour?",
     "Both same / రెండూ ఒకటే",
     "QH = first hour, advance notice for ministerial answers; ZH = post-12 noon, no notice, urgent issues / QH మొదటి గంట, నోటీసు; ZH 12 తర్వాత, నోటీసు లేదు (correct)",
     "ZH first; QH last / తారుమారు",
     "ZH only RS; QH only LS / కేవలం",
     "b",
     "QUESTION HOUR (11AM-12PM) = first hour, MPs ask ministers questions with advance notice. ZERO HOUR (immediately after, ~12PM) = informal, no advance notice, MPs raise urgent matters."),

    # ══════════════ SECTION 7 — Sessions, Privileges, Misc ══════════════

    (7, 1,
     "How many sessions does Parliament have in a year?\nతెలుగు: పార్లమెంట్ Sessions ఎన్ని?",
     "2 sessions / 2",
     "3 sessions / 3",
     "4 sessions / 4",
     "No fixed number / నిర్ణీత సంఖ్య లేదు (correct)",
     "d",
     "Constitution doesn't fix the number — but Art.85 says max gap between two sessions = 6 months. Conventionally 3 sessions: Budget (Feb-May), Monsoon (Jul-Sep), Winter (Nov-Dec)."),

    (7, 2,
     "What is Parliamentary 'Privilege'? [APPSC]\nతెలుగు: పార్లమెంట్ 'Privilege' అంటే?",
     "Salary and allowances of MPs / జీతం + భత్యాలు",
     "Freedom from court action for things said in House + other special rights / సభలో మాట్లాడిన దానిపై కోర్టు వ్యాజ్యం నుండి స్వేచ్ఛ + ఇతర ప్రత్యేక హక్కులు (correct)",
     "Right not to be arrested ever / Arrest నుండి స్వేచ్ఛ",
     "Right to free government land / ఉచిత భూమి",
     "b",
     "Article 105: Parliamentary Privileges = (1) freedom of speech in House, (2) immunity from court action for anything said/voted in House, (3) freedom from arrest in civil cases (40 days before/after session), (4) right to publish proceedings.",
     "APPSC"),

    (7, 2,
     "Difference between 'Prorogation' and 'Dissolution'? [APPSC]\nతెలుగు: Prorogation vs Dissolution?",
     "Both same / రెండూ ఒకటే",
     "Prorogation = end of Session (pending business survives); Dissolution = end of LS (pending Bills lapse) / Prorogation = Session ముగింపు; Dissolution = LS రద్దు (correct)",
     "Reverse / తారుమారు",
     "Both apply to RS / రెండూ RS కు",
     "b",
     "PROROGATION = end of a session; the House continues to exist; pending business carried over. DISSOLUTION = end of Lok Sabha; fresh elections required; LS pending Bills LAPSE (RS pending Bills survive).",
     "APPSC"),

    (7, 2,
     "What happens to the LS Speaker when Lok Sabha is dissolved? [APPSC]\nతెలుగు: లోక్‌సభ రద్దయితే Speaker?",
     "Speaker's term ends immediately / వెంటనే ముగుస్తుంది",
     "Speaker continues until first sitting of new Lok Sabha / కొత్త LS మొదటి సమావేశం వరకు (correct)",
     "Speaker presides over Rajya Sabha too / RS కు కూడా",
     "Speaker is appointed by President / రాష్ట్రపతి నియమిస్తారు",
     "b",
     "Article 94 proviso: Speaker continues to hold office until immediately before the first sitting of the next Lok Sabha — to ensure continuity.",
     "APPSC"),

    (7, 3,
     "Who decides on disqualification of a Parliament member? [APPSC]\nతెలుగు: అనర్హత ఎవరు నిర్ణయిస్తారు?",
     "Supreme Court / సుప్రీం కోర్టు",
     "President — on Election Commission's opinion / రాష్ట్రపతి + EC అభిప్రాయం (correct)",
     "Speaker/Chairman — only for 10th Schedule / Speaker — కేవలం 10వ షెడ్యూల్",
     "Lok Sabha by full vote / LS మొత్తం ఓటు",
     "b",
     "Article 103: For Art.102 disqualifications (office of profit, insolvency, etc.) — President decides on EC's opinion. For 10th Schedule (Anti-Defection): Speaker/Chairman decides (option C is correct only for that subset).",
     "APPSC"),

    (7, 2,
     "What is the special power of Rajya Sabha under Art.312? [APPSC]\nతెలుగు: Art.312 ప్రత్యేక అధికారం?",
     "Rejecting Money Bills / Money Bill",
     "Forming new states / కొత్త రాష్ట్రాలు",
     "Creating new All India Services — by 2/3 RS resolution / కొత్త AIS సృష్టి (correct)",
     "Declaring Emergency / అత్యవసర పరిస్థితి",
     "c",
     "Art.312: New All-India Services can be created ONLY if Rajya Sabha (representing states) passes a resolution by 2/3 majority of members present and voting. RS thus protects state interests in AIS creation.",
     "APPSC"),

    (7, 2,
     "Does a Bill pending in RS lapse when LS is dissolved?\nతెలుగు: RS pending Bill LS రద్దయితే lapse అవుతుందా?",
     "Both lapse / రెండూ lapse",
     "RS pending Bill does NOT lapse, even if LS dissolves / RS Bill lapse అవదు (correct)",
     "LS pending survives / LS Bill survive",
     "All lapse / అన్నీ lapse",
     "b",
     "Bills pending in RS (not yet passed by LS) DO NOT lapse on LS dissolution — RS is permanent. Bills pending in LS, or passed by LS but pending in RS, DO lapse."),

    (7, 1,
     "Who presides over a Joint Sitting of Parliament? [APPSC]\nతెలుగు: Joint Sitting అధ్యక్ష?",
     "President / రాష్ట్రపతి",
     "Prime Minister / PM",
     "Lok Sabha Speaker / లోక్‌సభ స్పీకర్ (correct)",
     "Rajya Sabha Chairman / RS Chairman",
     "c",
     "LOK SABHA SPEAKER presides over a Joint Sitting (Art.108). In Speaker's absence, Deputy Speaker; if both absent, RS Deputy Chairman; if all absent, House decides.",
     "APPSC"),

    (7, 2,
     "Salaries of Parliament members are paid from which fund?\nతెలుగు: జీతభత్యాలు ఏ నిధి?",
     "Contingency Fund / Contingency Fund",
     "Public Account / Public Account",
     "Consolidated Fund of India / భారత సంచిత నిధి (correct)",
     "State Disaster Fund / SDF",
     "c",
     "Salaries + allowances of MPs (and most other constitutional officers like President, VP, judges, CAG) are CHARGED on the Consolidated Fund of India (Art.106) — not subject to vote in Parliament."),

    (7, 2,
     "Even though RS is permanent, members don't all retire together — why? [APPSC]\nతెలుగు: ఎందుకు?",
     "Every year 1/4 retire / 1/4",
     "Every 2 years 1/3 retire / ప్రతి 2 సం. 1/3 retire (correct)",
     "Every 3 years 1/2 retire / 1/2",
     "All retire after 6 years together / అందరూ ఒకేసారి",
     "b",
     "1/3 of RS members retire every 2 years (and equal number elected). This staggered retirement ensures RS continuity and never fully dissolves.",
     "APPSC"),

    (7, 2,
     "Is Educational Qualification required to become a Parliament member? [APPSC]\nతెలుగు: విద్యార్హత అవసరమా?",
     "Yes — minimum graduation / అవును, గ్రాడ్యుయేట్",
     "Yes — Matriculation / అవును, Matric",
     "No — Constitution doesn't prescribe educational qualification / కాదు; రాజ్యాంగం నిర్ణయించలేదు (correct)",
     "Different for LS and RS / LS, RS కు వేర్వేరు",
     "c",
     "Constitution does NOT prescribe an educational qualification for MPs/MLAs. Only requires citizenship, age, mental soundness, etc. (Art.84 for Parliament).",
     "APPSC"),

    (7, 3,
     "Regarding Parliament's 'Contempt of House' power [UPSC Style]\nతెలుగు: 'Contempt of House' అధికారం?",
     "Only members can use this power / కేవలం సభ్యులు",
     "Outsiders cannot commit contempt / బయటివారు contempt చేయలేరు",
     "Parliament can punish for actions inside or outside that lower its dignity / సభ లోపల/బయట గౌరవం దెబ్బతీసే చర్యలకు శిక్ష (correct)",
     "Applies only to courts / కేవలం కోర్టు",
     "c",
     "Parliament has the inherent power to punish anyone (member or outsider) who commits 'Contempt of House' — actions that lower the dignity, authority, or honour of the House.",
     "UPSC"),

    (7, 2,
     "If the post of Speaker falls vacant, what happens? [APPSC]\nతెలుగు: Speaker పదవి ఖాళీ?",
     "Deputy Speaker auto-becomes Speaker / Deputy Speaker auto",
     "Deputy Speaker performs Speaker's duties until new election / Deputy Speaker విధులు; కొత్త ఎన్నిక వరకు (correct)",
     "Senior minister presides / సీనియర్ మంత్రి",
     "Pro-tem Speaker appointed / Pro-tem నియామకం",
     "b",
     "Article 95: When Speaker post is vacant, Deputy Speaker performs the duties. New Speaker is then elected by LS to fill the vacancy.",
     "APPSC"),

    (7, 2,
     "Which Rajya Sabha resolutions require Special Majority?\nతెలుగు: RS Special Majority?",
     "President's impeachment / రాష్ట్రపతి అభిశంసన",
     "Art.249 (State List legislation) and Art.312 (New AIS) / Art.249 + Art.312 (correct)",
     "No-Confidence Motion / అవిశ్వాస",
     "Budget approval / బడ్జెట్",
     "b",
     "Both Art.249 (legislating on State List) and Art.312 (creating new All-India Services) require RS to pass a resolution by 2/3 majority of members PRESENT and VOTING."),
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
