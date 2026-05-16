# seed_polity_ch14.py
# Chapter 14 – Parliamentary Procedures
# (పార్లమెంటరీ విధానాలు)
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total Sections: 8 | Total MCQs: 60 | PYQs: 8
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# ─────────────────────────────────────────────────────

import json as _json

POLITY_CH14_SECTIONS = [
    {
        "title": "14.1 బిల్లుల రకాలు — వర్గీకరణ",
        "sub": "Ordinary · Money · Financial · Constitution Amendment Bills · Art.107–117",
        "audio": ""
    },
    {
        "title": "14.2 బిల్లు దశలు — పార్లమెంట్‌లో ఆమోదం",
        "sub": "First Reading · Second Reading · Committee Stage · Third Reading · Art.107–111",
        "audio": ""
    },
    {
        "title": "14.3 ప్రశ్నోత్తర సమయం — Zero Hour",
        "sub": "Starred · Unstarred · Short Notice Questions · Zero Hour · Question Hour Rules",
        "audio": ""
    },
    {
        "title": "14.4 తీర్మానాలు మరియు ప్రస్తావనలు",
        "sub": "Adjournment · No-Confidence · Censure · Cut Motions · Calling Attention",
        "audio": ""
    },
    {
        "title": "14.5 బడ్జెట్ విధానం",
        "sub": "Art.112–116 · Annual Financial Statement · Vote on Account · Guillotine · Appropriation · Finance Bill",
        "audio": ""
    },
    {
        "title": "14.6 పార్లమెంటరీ కమిటీలు",
        "sub": "PAC · Estimates Committee · CoPU · Standing Committees · BAC · DRSCs",
        "audio": ""
    },
    {
        "title": "14.7 ప్రత్యేక విధానాలు — రాజ్యాంగ సవరణ",
        "sub": "Art.368 · Simple/Special/Special+Ratification · Private Member Bills",
        "audio": ""
    },
    {
        "title": "14.8 కఠిన ప్రశ్నలు — APPSC/UPSC PYQs",
        "sub": "Money Bill controversy · Lame-duck session · Hung Parliament · Gallery",
        "audio": ""
    },
]

POLITY_CH14_MCQS = [

    # ══════════════ SECTION 0 — Bills (Money/Finance/Ordinary/Private) ══════════════

    (0, 1,
     "In which House of Parliament can a Money Bill be introduced?\nతెలుగు: మనీ బిల్లు ఏ సభలో ప్రవేశపెట్టవచ్చు?",
     "Rajya Sabha / రాజ్యసభ",
     "Lok Sabha only / లోక్‌సభ మాత్రమే (correct)",
     "Both Houses / రెండు సభలు",
     "House decided by President / రాష్ట్రపతి నిర్ణయించే సభ",
     "b",
     "Article 110(1): Money Bill can be introduced ONLY in Lok Sabha (after President's recommendation)."),

    (0, 1,
     "For how many days can Rajya Sabha retain a Money Bill?\nతెలుగు: మనీ బిల్లుకు రాజ్యసభ గరిష్ఠంగా ఎన్ని రోజులు ఉంచుకోవచ్చు?",
     "7 days / 7 రోజులు",
     "14 days / 14 రోజులు (correct)",
     "21 days / 21 రోజులు",
     "1 month / 1 నెల",
     "b",
     "Art.109: RS must return Money Bill within 14 days. If RS doesn't return → Bill is deemed passed in form passed by LS."),

    (0, 2,
     "Which item is included in the Art.110 definition of Money Bill?\nతెలుగు: Art.110 కింద మనీ బిల్లులో ఉండే అంశం?",
     "Salary regulation / జీతాల నియంత్రణ",
     "Imposition/abolition of taxes / పన్నుల విధింపు/రద్దు (correct)",
     "State List items / రాష్ట్ర జాబితా అంశాలు",
     "Police funds / పోలీసు నిధులు",
     "b",
     "Art.110(1) lists 7 items including imposition/abolition/alteration/regulation of taxes, borrowing, custody of Consolidated Fund, etc."),

    (0, 2,
     "Key difference between a Finance Bill and a Money Bill?\nతెలుగు: ఫైనాన్స్ బిల్లు vs మనీ బిల్లు తేడా?",
     "Finance Bill in RS / RS లో",
     "Finance Bill broader — taxation + other provisions / Finance Bill విస్తారం — పన్ను + ఇతర అంశాలు (correct)",
     "Money Bill needs no President's assent / Money Bill కు అనుమతి లేదు",
     "Both same / రెండూ ఒకటే",
     "b",
     "Money Bill = ONLY Art.110 items. Finance Bill = Art.110 items + other matters. Money Bill is a strict subset of Finance Bills."),

    (0, 1,
     "Can an Ordinary Bill be introduced in either House?\nతెలుగు: సాధారణ బిల్లు రెండు సభలలో ప్రవేశపెట్టవచ్చా?",
     "No, only LS / కేవలం LS",
     "Yes, in either House / అవును, రెండు సభల్లో (correct)",
     "Only RS / కేవలం RS",
     "President decides / రాష్ట్రపతి",
     "b",
     "Ordinary Bill (non-Money, non-Constitutional Amendment) can originate in EITHER House. Only Money Bills are restricted to LS."),

    (0, 3,
     "Which statement about Private Member's Bill is correct?\nతెలుగు: ప్రైవేట్ మెంబర్ బిల్లు?",
     "Only ministers can introduce / మంత్రులు మాత్రమే",
     "Friday afternoons reserved for private members / శుక్రవారం సాయంత్రం (correct)",
     "Doesn't need President's assent / రాష్ట్రపతి అవసరం లేదు",
     "Never gets passed / ఎప్పుడూ ఆమోదించబడదు",
     "b",
     "Private Member = MP not in the Government. 2.5 hours every Friday afternoon reserved for Private Member's Bills. Few have ever passed (last one passed in 1970)."),

    (0, 2,
     "Which is correct about a Money Bill in Rajya Sabha?\nతెలుగు: మనీ బిల్లు RS లో?",
     "RS can reject it / తిరస్కరించవచ్చు",
     "RS can amend it / సవరించవచ్చు",
     "RS can only make recommendations; LS may accept/reject / RS సిఫార్సులు మాత్రమే; LS నిర్ణయిస్తుంది (correct)",
     "RS must pass it / తప్పనిసరిగా ఆమోదించాలి",
     "c",
     "Art.109: RS can only suggest amendments (recommendations). LS may accept or reject these. If RS doesn't return in 14 days, Bill is deemed passed."),

    (0, 3,
     "If a Bill has both Art.110 provisions AND non-money provisions, what is it?\nతెలుగు: కొన్ని Art.110 + ఇతరం = ఏది?",
     "Money Bill / మనీ బిల్లు",
     "Financial Bill (Category A) — NOT Money Bill / Financial Bill Cat A (correct)",
     "Financial Bill (Category B) / Financial Bill Cat B",
     "Ordinary Bill / సాధారణ",
     "b",
     "Financial Bill (Category A) under Art.117(1) = contains some Art.110 items + other provisions. NOT a Money Bill, so RS has full powers. Introduced only in LS with President's recommendation."),

    # ══════════════ SECTION 1 — Bill Stages, Joint Sitting, Veto ══════════════

    (1, 1,
     "What happens at the First Reading of a Bill?\nతెలుగు: మొదటి పఠనం?",
     "Discussion on Bill / చర్చ",
     "Introduction and reading of title only / పరిచయం + శీర్షిక మాత్రమే (correct)",
     "Sent to Committee / కమిటీకి",
     "Voting / ఓటింగ్",
     "b",
     "First Reading = formal introduction (mover seeks leave + reads title). NO discussion at this stage. Bill is then published in the Gazette."),

    (1, 2,
     "Which stages are part of Second Reading?\nతెలుగు: రెండవ పఠనంలో ఏ దశలు?",
     "General discussion + Committee stage / సాధారణ చర్చ + కమిటీ దశ (correct)",
     "Voting only / ఓటింగ్",
     "Bill rejection / రద్దు",
     "President's assent / రాష్ట్రపతి",
     "a",
     "Second Reading = (1) General Discussion (broad principles), (2) Committee Stage (clause-by-clause examination), (3) Consideration Stage (House discusses Committee's amendments)."),

    (1, 1,
     "What happens at the Third Reading?\nతెలుగు: మూడవ పఠనం?",
     "Final vote on the Bill / మొత్తం బిల్లుపై ఓటింగ్ (correct)",
     "Committee report submission / కమిటీ నివేదిక",
     "Bill introduced / ప్రవేశపెట్టడం",
     "President signs / రాష్ట్రపతి సంతకం",
     "a",
     "Third Reading = final vote on the Bill as a whole. Only verbal/formal amendments allowed; no major changes. If passed, Bill goes to other House."),

    (1, 2,
     "When does a Joint Sitting NOT take place?\nతెలుగు: Joint Sitting జరగని సందర్భం?",
     "When one House rejects / ఒక సభ తిరస్కరణ",
     "For Money Bills / మనీ బిల్లు (correct)",
     "When Houses disagree / విభేదించినప్పుడు",
     "Bill pending 6 months / 6 నెలలు",
     "b",
     "Joint Sitting (Art.108) does NOT apply to Money Bills (LS supremacy) or Constitutional Amendment Bills (each House must independently pass with special majority)."),

    (1, 3,
     "What is President's 'Pocket Veto'?\nతెలుగు: 'Pocket Veto' అంటే?",
     "Signing the Bill / సంతకం చేయడం",
     "Sending Bill for indefinite discussion / నిరవధిక చర్చ",
     "Taking no action — indefinite inaction / ఎలాంటి నిర్ణయం తీసుకోకుండా వదిలేయడం (correct)",
     "Cancelling Bill / రద్దు",
     "c",
     "Pocket Veto = President neither signs nor returns the Bill — keeps it indefinitely. Used by Pres. Zail Singh on Indian Post Office (Amendment) Bill 1986. Constitution sets no time limit (only 'as soon as possible')."),

    (1, 2,
     "Difference between Select Committee and Joint Committee?\nతెలుగు: Select Committee vs Joint Committee?",
     "Both same / రెండూ ఒకటే",
     "Select = one House members; Joint = both Houses members / Select ఒక సభ; Joint రెండు సభలు (correct)",
     "Select can reject Bill / Select రద్దు",
     "Joint chaired by Speaker / Speaker నేతృత్వం",
     "b",
     "Select Committee = members of ONE House only. Joint Committee = members of BOTH LS and RS. Both examine Bills clause-by-clause and report back."),

    (1, 3,
     "What happens to pending Bills when Parliament is prorogued?\nతెలుగు: Prorogation అయితే Bills?",
     "All lapse / అన్నీ రద్దు",
     "RS bills lapse, LS bills survive / RS lapse, LS survive",
     "All survive — pending Bills do NOT lapse on prorogation / అన్నీ మిగిలి ఉంటాయి (correct)",
     "President decides / రాష్ట్రపతి",
     "c",
     "PROROGATION (end of session) does NOT cause Bills to lapse. They continue in the next session. Only DISSOLUTION of Lok Sabha causes lapsing of LS Bills (and RS Bills passed by LS but pending in RS)."),

    # ══════════════ SECTION 2 — Question Hour, Zero Hour ══════════════

    (2, 1,
     "When is Question Hour held in Parliament?\nతెలుగు: ప్రశ్నోత్తర సమయం ఎప్పుడు?",
     "12 PM / 12 గం.",
     "11 AM to 12 PM (first hour) / 11–12 గం. (correct)",
     "2-4 PM / 2–4 గం.",
     "End of session / ముగింపులో",
     "b",
     "Question Hour = 11 AM to 12 noon (first hour of every sitting day). MPs question ministers about their departments."),

    (2, 1,
     "What is a Starred Question?\nతెలుగు: Starred Question?",
     "Written-answer question / వ్రాతపూర్వక",
     "Oral answer required — supplementary questions allowed / మౌఖిక సమాధానం + అనుబంధ ప్రశ్నలు (correct)",
     "Only Speaker can ask / Speaker మాత్రమే",
     "PM answers / PM",
     "b",
     "STARRED Question (marked with *) = oral answer in House + supplementary questions allowed. Max 20 starred questions per day per House."),

    (2, 2,
     "Short Notice Question requires how many days' notice?\nతెలుగు: Short Notice Question?",
     "15 days / 15 రోజులు",
     "Less than 10 days / 10 రోజుల కంటే తక్కువ (correct)",
     "30 days / 30 రోజులు",
     "No notice / నోటీసు లేదు",
     "b",
     "Short Notice Question = on urgent matter, less than 10 days' notice. Speaker decides if it warrants short-notice treatment. Answered orally."),

    (2, 2,
     "Which is correct about Zero Hour?\nతెలుగు: Zero Hour?",
     "Constitutional time / రాజ్యాంగంలో",
     "Informal time from 12 noon — NOT in Rules of Procedure / 12 గం. నుండి అనధికారిక (correct)",
     "Part of Question Hour / QH లో భాగం",
     "Reserved for Budget / బడ్జెట్",
     "b",
     "Zero Hour = INFORMAL Indian innovation; starts immediately after Question Hour (~12 noon). Members raise urgent issues without prior notice. NOT mentioned in Rules of Procedure or Constitution."),

    (2, 1,
     "What type of answer does an Unstarred Question receive?\nతెలుగు: Unstarred Question?",
     "Oral + supplementaries / మౌఖికం + అనుబంధ",
     "Written answer only — no supplementaries / వ్రాతపూర్వక మాత్రమే; అనుబంధ లేవు (correct)",
     "PM answer / PM",
     "Speaker decides / Speaker",
     "b",
     "UNSTARRED Question = no asterisk; written answer placed on the Table of the House; NO supplementary questions. Max 230 unstarred per day per House."),

    (2, 2,
     "On which days is Question Hour NOT held?\nతెలుగు: Question Hour లేని రోజులు?",
     "Mondays / సోమవారాలు",
     "Day of President's Address and Budget Day / రాష్ట్రపతి ప్రసంగం + బడ్జెట్ రోజు (correct)",
     "Fridays / శుక్రవారాలు",
     "Never skipped / ఎప్పుడూ లేకుండా లేదు",
     "b",
     "Question Hour is suspended on (1) the day of President's Address and (2) the day Budget is presented — to give them precedence."),

    (2, 3,
     "What is 'Special Mention' in Parliament?\nతెలుగు: 'Special Mention'?",
     "Speaker's permission / Speaker అనుమతి",
     "RS member raises important matter without notice — RS equivalent of Zero Hour / RS లో నోటీసు లేకుండా (correct)",
     "LS special resolution / LS తీర్మానం",
     "PM's special speech / PM ప్రసంగం",
     "b",
     "Special Mention = device in RAJYA SABHA for members to raise urgent matters of public importance without prior notice — similar to Zero Hour in Lok Sabha."),

    # ══════════════ SECTION 3 — Motions ══════════════

    (3, 2,
     "Which is correct about Adjournment Motion?\nతెలుగు: Adjournment Motion?",
     "Only RS / కేవలం RS",
     "Only LS, urgent matter of national importance, 50 members support / LS మాత్రమే, 50 సభ్యుల మద్దతు (correct)",
     "It seeks to adjourn House / సభ వాయిదా",
     "Always passed / ప్రతిసారి ఆమోదం",
     "b",
     "Adjournment Motion (LS only) = on urgent matter of national importance; needs support of 50+ members; takes precedence over normal business. Element of CENSURE on Government."),

    (3, 2,
     "In which House can a No-Confidence Motion be introduced?\nతెలుగు: అవిశ్వాస తీర్మానం?",
     "RS only / RS మాత్రమే",
     "Both Houses / రెండూ",
     "Lok Sabha only — Art.75(3) / LS మాత్రమే (correct)",
     "With President's permission, both / రెండూ",
     "c",
     "No-Confidence Motion can be moved ONLY in LS — because the Council of Ministers is collectively responsible to LS (Art.75(3)). Needs 50 members' support."),

    (3, 2,
     "Difference between Censure Motion and No-Confidence Motion?\nతెలుగు: Censure vs No-Confidence తేడా?",
     "Same / రెండూ ఒకటే",
     "Censure on specific policy — passing doesn't force resignation / Censure విధానం — రాజీనామా అవసరం లేదు (correct)",
     "Censure in RS / RS లో",
     "NCM needs President's permission / రాష్ట్రపతి",
     "b",
     "CENSURE = on specific policy/minister; mentions reasons; passing does NOT compel Govt to resign. NO-CONFIDENCE = general; no reasons needed; if passed, Govt MUST resign."),

    (3, 3,
     "What are the types of Cut Motion?\nతెలుగు: Cut Motion రకాలు?",
     "Policy Cut, Economy Cut, Token Cut / 3 రకాలు (correct)",
     "Censure cut, policy cut",
     "Only one type / ఒకే రకం",
     "Two types / రెండే",
     "a",
     "Three Cut Motions: (1) Policy Cut — reduce demand to ₹1; (2) Economy Cut — reduce by specific amount; (3) Token Cut — reduce by ₹100 to express grievance."),

    (3, 2,
     "Who introduces a Calling Attention Motion?\nతెలుగు: Calling Attention Motion?",
     "Government / ప్రభుత్వం",
     "Speaker / Speaker",
     "A member — to draw minister's attention to urgent matter / సభ్యుడు, మంత్రి దృష్టికి (correct)",
     "President / రాష్ట్రపతి",
     "c",
     "Calling Attention Motion = a member with Speaker's permission calls the attention of a minister to a matter of urgent public importance + asks for ministerial reply. Indian innovation since 1954."),

    (3, 2,
     "Within how many days must a No-Confidence Motion be debated after admission?\nతెలుగు: NCM ఎన్ని రోజుల్లోపు?",
     "7 days / 7",
     "10 days / 10 (correct)",
     "15 days / 15",
     "21 days / 21",
     "b",
     "Once admitted by the Speaker, NCM must be debated within 10 days. If not debated, motion lapses."),

    (3, 3,
     "Types of Closure Motion in Parliament?\nతెలుగు: Closure Motion రకాలు?",
     "Simple Closure only / కేవలం Simple",
     "Simple, Kangaroo, Guillotine / 3 రకాలు",
     "Simple, Kangaroo, Closure by Compartments, Guillotine / 4 రకాలు (correct)",
     "Two types / రెండే",
     "c",
     "Four types: (1) Simple Closure, (2) Closure by Compartments, (3) Kangaroo Closure (only important clauses discussed), (4) Guillotine (timed closure)."),

    # ══════════════ SECTION 4 — Budget & Financial Procedure ══════════════

    (4, 1,
     "Annual Financial Statement is under which Article?\nతెలుగు: AFS ఏ ఆర్టికల్?",
     "Art.110",
     "Art.112 (correct)",
     "Art.116",
     "Art.360",
     "b",
     "Article 112 = Annual Financial Statement (Budget). President causes it to be laid before both Houses every year."),

    (4, 2,
     "What is Vote on Account?\nతెలుగు: Vote on Account?",
     "Budget approval / బడ్జెట్ ఆమోదం",
     "Temporary grant for govt expenditure till Budget passed / తాత్కాలిక అనుమతి (correct)",
     "Supplementary Budget / అనుబంధ బడ్జెట్",
     "Appropriation Bill / అప్రూప్రియేషన్",
     "b",
     "Vote on Account (Art.116) = Parliament's grant to enable government to meet expenditure for part of FY pending full Budget passage. Usually 2 months."),

    (4, 2,
     "What does 'Guillotine' mean in Parliamentary terminology?\nతెలుగు: Guillotine?",
     "Speaker's power / Speaker అధికారం",
     "All outstanding demands voted on at end of Budget session without discussion / మిగిలిన demands ఓటింగ్ కు, చర్చ లేకుండా (correct)",
     "Emergency Budget / అత్యవసర బడ్జెట్",
     "Vote on Account / VoA",
     "b",
     "Guillotine = on the last day allotted for discussion of demands for grants, Speaker puts ALL OUTSTANDING DEMANDS to vote without further debate — typically used to wind up debate in time."),

    (4, 2,
     "Why is Appropriation Bill necessary?\nతెలుగు: Appropriation Bill?",
     "For levying taxes / పన్నుల విధింపు",
     "Parliamentary authorization to withdraw from Consolidated Fund — Art.114 / Art.114 (correct)",
     "To allocate to states / రాష్ట్రాలకు",
     "President's salary / రాష్ట్రపతి జీతం",
     "b",
     "Article 114: No money can be withdrawn from Consolidated Fund of India except under appropriation made by law passed by Parliament. Hence Appropriation Bill."),

    (4, 3,
     "What happens if the Finance Bill is NOT passed?\nతెలుగు: Finance Bill ఆమోదించకపోతే?",
     "Nothing / ఏమీ కాదు",
     "New taxes become illegal / కొత్త పన్నులు చట్టవిరుద్ధం",
     "Government must resign — equivalent to loss of confidence / ప్రభుత్వం రాజీనామా; విశ్వాస ఓటు సమానం (correct)",
     "President's Rule / రాష్ట్రపతి పాలన",
     "c",
     "Failure to pass Finance Bill is treated as LOSS OF CONFIDENCE in the Government — by convention, the Government must resign. Same applies to Budget rejection."),

    (4, 2,
     "Supplementary Demands for Grants fall under which Article?\nతెలుగు: Supplementary Demands ఏ ఆర్టికల్?",
     "Art.112",
     "Art.113",
     "Art.115 (correct)",
     "Art.116",
     "c",
     "Article 115 = Supplementary, Additional, or Excess Grants. When the original budget is insufficient, government seeks additional Parliament authorization."),

    (4, 3,
     "From which year did India start presenting Budget on February 1?\nతెలుగు: ఫిబ్రవరి 1న ఎప్పటి నుండి?",
     "2015–16",
     "2016–17",
     "2017–18 (correct)",
     "2000–01",
     "c",
     "From Budget 2017-18, Modi government advanced Budget date from February 28 to February 1 — to ensure Bills are passed before April 1 (FY start) and to give departments more planning time."),

    # ===== Section 5: Parliamentary Committees =====

    (5, 2,
     "Public Accounts Committee (PAC) consists of how many members?\nతెలుగు: PAC సభ్యులు ఎంతమంది?",
     "30 members / 30 సభ్యులు",
     "22 members (15 LS + 7 RS) / 22 (15 లోక్‌సభ + 7 రాజ్యసభ) (correct)",
     "20 members / 20 సభ్యులు",
     "25 members / 25 సభ్యులు",
     "b",
     "PAC has 22 members — 15 from Lok Sabha + 7 from Rajya Sabha. Term: 1 year. Examines CAG reports. Chairperson is appointed by Speaker; by convention, from Opposition since 1967."),

    (5, 2,
     "Estimates Committee has how many members?\nతెలుగు: Estimates Committee సభ్యులు?",
     "22 / 22",
     "30 (all from Lok Sabha) / 30 (అన్నీ లోక్‌సభ నుండి) (correct)",
     "15 / 15",
     "45 / 45",
     "b",
     "Estimates Committee = 30 members, all from Lok Sabha (no Rajya Sabha). Largest financial committee. Term: 1 year. Examines budget estimates and suggests economies. Called 'continuous economy committee'."),

    (5, 3,
     "Which committee examines budget estimates BEFORE expenditure?\nతెలుగు: ఏ committee బడ్జెట్ estimates ముందుగా పరిశీలిస్తుంది?",
     "PAC (after expenditure) / PAC (తర్వాత)",
     "Estimates Committee (before expenditure) / Estimates Committee (correct)",
     "Finance Committee / Finance",
     "Budget Committee / Budget",
     "b",
     "Estimates Committee examines budget estimates BEFORE expenditure (proposals). PAC examines AFTER expenditure (audit). PAC = post-mortem; Estimates = preventive economy."),

    (5, 2,
     "Committee on Public Undertakings (CoPU) has how many members?\nతెలుగు: CoPU సభ్యులు?",
     "15 / 15",
     "22 (15 LS + 7 RS) / 22 (correct)",
     "30 / 30",
     "20 / 20",
     "b",
     "Committee on Public Undertakings (CoPU) = 22 members (15 LS + 7 RS), term 1 year. Examines reports/accounts of public sector undertakings. Created in 1964 on Krishna Menon Committee recommendation."),

    (5, 3,
     "How many Departmentally Related Standing Committees (DRSCs) exist?\nతెలుగు: DRSCs ఎన్ని?",
     "17 / 17",
     "24 (correct)",
     "22 / 22",
     "30 / 30",
     "b",
     "24 DRSCs (since 2004). Each has 31 members (21 LS + 10 RS). Cover all ministries. Tasks: examine bills, demands for grants, annual reports. Created on Rules Committee recommendation."),

    (5, 1,
     "Business Advisory Committee of Lok Sabha is chaired by?\nతెలుగు: BAC ఛైర్మన్?",
     "PM / ప్రధాని",
     "Speaker / స్పీకర్ (correct)",
     "Leader of Opposition / ప్రతిపక్ష నాయకుడు",
     "Parliamentary Affairs Minister / మంత్రి",
     "b",
     "Business Advisory Committee (BAC) of Lok Sabha is chaired by the SPEAKER. 15 members. Allocates time for various items of business. Rajya Sabha BAC is chaired by Vice President (Chairman)."),

    (5, 3,
     "When was Public Accounts Committee (PAC) first established in India?\nతెలుగు: PAC మొదటిగా ఎప్పుడు?",
     "1947 / 1947",
     "1950 / 1950",
     "1921 (correct)",
     "1935 / 1935",
     "c",
     "PAC was first set up in 1921 under Government of India Act 1919 — oldest financial committee in India. Continues today as central tool for parliamentary financial control over executive."),

    # ===== Section 6: Constitutional Amendment =====

    (6, 2,
     "How many types of majorities can be used to amend Constitution under Art.368?\nతెలుగు: Art.368 లో ఎన్ని rakaala majorities?",
     "1 type / 1 రకం",
     "2 types / 2 రకాలు",
     "3 types (Simple, Special, Special + State Ratification) / 3 రకాలు (correct)",
     "4 types / 4 రకాలు",
     "c",
     "Constitutional Amendment under Art.368: (1) Simple Majority (federal features outside 368), (2) Special Majority (most amendments), (3) Special Majority + Ratification by half of states (federal provisions like Art.54, 55, 73, etc.)."),

    (6, 3,
     "What is 'Special Majority' for Constitutional Amendment?\nతెలుగు: Special Majority?",
     "2/3 of total membership / 2/3 మొత్తం సభ్యులు",
     "Majority of TOTAL membership + 2/3 of MEMBERS PRESENT and voting / మెజారిటీ + 2/3 (correct)",
     "Simple majority / సాధారణ మెజారిటీ",
     "3/4 of total membership / 3/4",
     "b",
     "Special Majority (Art.368) = (a) Majority of total membership of each House (>50%) + (b) Majority of 2/3rd of members PRESENT and voting. Both conditions must be met in EACH House separately."),

    (6, 3,
     "Ratification by states is required for amending which provisions?\nతెలుగు: రాష్ట్రాల ratification ఎప్పుడు?",
     "Fundamental Rights / FR",
     "DPSP / DPSP",
     "Federal provisions like Art.54, 55, 73, 162, 7th Schedule (correct)",
     "Preamble / పీఠిక",
     "c",
     "Provisions affecting federal structure require ratification by HALF of state legislatures: Election of President (Art.54, 55), Executive power Union/State (73, 162), SC/HC, distribution of powers (7th Schedule), Art.368 itself."),

    (6, 2,
     "Is Joint Sitting (Art.108) possible for Constitutional Amendment Bills?\nతెలుగు: Constitutional Amendment Bill కు Joint Sitting?",
     "Yes / అవును",
     "No (correct)",
     "Only if President permits / రాష్ట్రపతి permission తో",
     "Sometimes / కొన్నిసార్లు",
     "b",
     "Joint Sitting under Art.108 is NOT possible for Constitutional Amendment Bills. Each House must pass it SEPARATELY by Special Majority. If one rejects, the bill fails — no joint sitting deadlock-breaker."),

    (6, 3,
     "Which Amendment made Presidential assent MANDATORY on Constitutional Amendments?\nతెలుగు: రాష్ట్రపతి assent తప్పనిసరి చేసిన Amendment?",
     "42nd Amendment / 42వ",
     "44th Amendment / 44వ",
     "24th Amendment 1971 (correct)",
     "1st Amendment / 1వ",
     "c",
     "24th Constitutional Amendment Act, 1971 made it COMPULSORY for President to give assent to a Constitutional Amendment Bill (i.e., no veto power). Was passed in response to Golaknath case (1967)."),

    (6, 3,
     "What is the 'Doctrine of Implied Limitations'?\nతెలుగు: Implied Limitations Doctrine?",
     "Parliament has unlimited power / అపరిమిత అధికారం",
     "Parliament cannot amend Basic Structure (Kesavananda Bharati 1973) / Basic Structure amend చేయలేదు (correct)",
     "Only PM can amend / PM మాత్రమే",
     "Amendment requires referendum / రెఫరెండం అవసరం",
     "b",
     "Doctrine of Implied Limitations was articulated in Kesavananda Bharati (1973) — Parliament has wide amending power BUT cannot destroy the BASIC STRUCTURE of the Constitution (judicial review, separation of powers, federalism, secularism, etc.)."),

    # ===== Section 7: Miscellaneous =====

    (7, 2,
     "Who is the FINAL authority to certify a Bill as Money Bill?\nతెలుగు: Money Bill certify చేయుట final authority?",
     "President / రాష్ట్రపతి",
     "PM / ప్రధాని",
     "Lok Sabha Speaker (Art.110(3)) / లోక్‌సభ స్పీకర్ (correct)",
     "Vice President / ఉపరాష్ట్రపతి",
     "c",
     "Article 110(3): Speaker of Lok Sabha is the FINAL authority to certify whether a Bill is a Money Bill or not. His decision is FINAL and cannot be questioned in any court (Art.122 bars judicial review of proceedings)."),

    (7, 3,
     "What is a 'Lame-Duck Session'?\nతెలుగు: Lame-Duck Session?",
     "First session of new Lok Sabha / కొత్త లోక్‌సభ first session",
     "Last session of OUTGOING Lok Sabha after general elections held / ఎన్నికల తర్వాత outgoing LS యొక్క last session (correct)",
     "Joint Sitting / కలిసి సమావేశం",
     "Special session / ప్రత్యేక",
     "b",
     "Lame-Duck Session = the LAST session of the outgoing Lok Sabha after general elections have been held but before the new Lok Sabha is constituted. Members not re-elected become 'lame ducks' — limited mandate."),

    (7, 3,
     "The Aadhaar Act 2016 was certified as which type of Bill?\nతెలుగు: ఆధార్ చట్టం 2016 ఏ రకం?",
     "Ordinary Bill / సాధారణ",
     "Finance Bill / Finance",
     "Money Bill (Speaker's decision controversial) / Money Bill (correct)",
     "Constitutional Amendment / Constitutional",
     "c",
     "Aadhaar Act 2016 was passed as a MONEY BILL — Speaker Sumitra Mahajan's certification was challenged in K.S. Puttaswamy (2018). SC upheld 4:1, but Justice Chandrachud's dissent called it 'fraud on Constitution'."),

    (7, 2,
     "Maximum gap between two parliamentary sessions cannot exceed?\nతెలుగు: రెండు sessions మధ్య gap?",
     "3 months / 3 నెలలు",
     "6 months (Art.85(1)) / 6 నెలలు (correct)",
     "9 months / 9 నెలలు",
     "1 year / 1 సంవత్సరం",
     "b",
     "Article 85(1): There must be a session of each House at least ONCE EVERY SIX MONTHS — i.e., gap between last sitting of one session and first sitting of next cannot exceed 6 months. Ensures regular parliamentary oversight."),

    (7, 3,
     "When was the FIRST No-Confidence Motion moved in India?\nతెలుగు: మొదటి NCM ఎప్పుడు?",
     "1952 / 1952",
     "1963 (against Nehru by Acharya Kripalani) (correct)",
     "1975 / 1975",
     "1947 / 1947",
     "b",
     "First No-Confidence Motion in independent India was moved on 19 August 1963 by Acharya J.B. Kripalani against PM Nehru's government — defeated. So far ~28 NCMs moved; only 3 governments fell (Morarji 1979, V.P.Singh 1990, Vajpayee 1999)."),

    (7, 2,
     "What is a 'Privilege Motion'?\nతెలుగు: Privilege Motion?",
     "Special privilege for ministers / మంత్రులకు ప్రత్యేక",
     "Motion against a member/minister for breach of parliamentary privileges / privileges భంగం (correct)",
     "Money privilege / డబ్బు privilege",
     "Constitutional privilege / రాజ్యాంగ",
     "b",
     "Privilege Motion = moved against a member/minister for BREACH OF PARLIAMENTARY PRIVILEGE (e.g., misleading the House, insulting members). Examined by Privileges Committee. Penalties: warning, suspension, expulsion, imprisonment."),

    (7, 3,
     "What is 'Half-Hour Discussion'?\nతెలుగు: Half-Hour Discussion?",
     "30-min Question Hour / 30 నిమిషాల QH",
     "Discussion on matter of sufficient public importance for 30 mins, no formal motion or vote / 30 నిమిషాల చర్చ (correct)",
     "Half-hour speech / 30 నిమిషాల ప్రసంగం",
     "Lunch break discussion / lunch",
     "b",
     "Half-Hour Discussion is raised on a matter of sufficient PUBLIC IMPORTANCE which has been subject of recent question/answer and needs further elucidation. Permitted 3 days/week. NO formal motion or voting."),

    (7, 3,
     "Vajpayee government fell by ONE VOTE in which year?\nతెలుగు: Vajpayee సర్కార్ ఒక ఓటుతో ఎప్పుడు?",
     "1996 / 1996",
     "1998 / 1998",
     "1999 (NCM lost by 269-270) (correct)",
     "2004 / 2004",
     "c",
     "On 17 April 1999, Vajpayee's NDA government LOST a No-Confidence Motion by ONE VOTE — 269 in favor of Govt vs 270 against. Triggered fall of govt and 1999 elections. Famous for AIADMK (Jayalalithaa) withdrawing support."),

    (7, 2,
     "What is a 'Whip' in parliamentary context?\nతెలుగు: Whip అంటే?",
     "Punishment / శిక్ష",
     "Party directive to members on voting/attendance, issued by party in Parliament / పార్టీ ఆదేశం (correct)",
     "Speaker's instruction / స్పీకర్ ఆదేశం",
     "Government rule / ప్రభుత్వ నియమం",
     "b",
     "Whip = official appointed by political party to ENFORCE PARTY DISCIPLINE — issues directives to members on attending and voting. Defying 3-line whip can lead to disqualification under Anti-Defection Law (10th Schedule)."),

    (7, 3,
     "What is the effect of Lok Sabha Dissolution on pending bills?\nతెలుగు: లోక్‌సభ రద్దుతో pending bills?",
     "All bills die / అన్ని bills చనిపోతాయి",
     "Bills pending in LS or passed by LS but pending in RS LAPSE; bills originating in RS and not passed by LS DO NOT lapse / vary (correct)",
     "All bills continue / అన్నీ కొనసాగుతాయి",
     "Only Money Bills lapse / Money Bills మాత్రమే",
     "b",
     "On Lok Sabha dissolution: (1) Bills pending in LS LAPSE; (2) Bills passed by LS but pending in RS LAPSE; (3) Bills originating in RS, not yet transmitted to LS, DO NOT lapse; (4) Bills passed by both Houses but pending President's assent DO NOT lapse."),

    (7, 1,
     "Parliamentary Privileges are mentioned in which Articles?\nతెలుగు: Parliamentary Privileges Articles?",
     "Art.79, 80 / 79, 80",
     "Art.105 (MPs) and Art.194 (MLAs) (correct)",
     "Art.110, 112 / 110, 112",
     "Art.123, 213 / 123, 213",
     "b",
     "Parliamentary Privileges = Art.105 (MPs of Parliament) and Art.194 (MLAs of State Legislatures). Include freedom of speech in House, immunity from court proceedings for actions in House, immunity from arrest in civil cases (40 days before/after session)."),
]


# ─────────────────────────────────────────────────────────────
def _seed_polity_ch14_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    """Insert Chapter 14 study note row (idempotent)."""
    existing = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=14"
    ).fetchone()
    if existing and not force:
        return

    sections_json = _json.dumps(POLITY_CH14_SECTIONS, ensure_ascii=False)
    ph = '%s' if use_postgres else '?'

    if existing and force:
        db_exec_fn(conn,
            f"UPDATE study_notes SET sections_json={ph}, chapter_title_en={ph}, chapter_title_te={ph} "
            f"WHERE topic='Indian_Polity' AND chapter_num=14",
            (sections_json,
             "Parliamentary Procedures",
             "పార్లమెంటరీ విధానాలు")
        )
        return

    db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, subtopic, chapter_num,
             chapter_title_te, chapter_title_en, pages_ref, sections_json)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        ('GK', 'Indian_Polity', 'Lakshmikanth', 14,
         'పార్లమెంటరీ విధానాలు',
         'Parliamentary Procedures',
         'Ch.14',
         sections_json)
    )


def _seed_polity_ch14_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    """Insert Chapter 14 MCQs (skip if already present)."""
    note_row = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=14"
    ).fetchone()
    if not note_row:
        return
    note_id = row_to_dict_fn(note_row)['id']

    already = db_exec_fn(conn,
        "SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id=?", (note_id,)
    ).fetchone()
    if already and list(already)[0] > 0:
        return

    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4,
                1: 1, 2: 2, 3: 3, 4: 4}

    ph = '%s' if use_postgres else '?'
    for row in POLITY_CH14_MCQS:
        sec_idx, diff_raw, q, a, b, c, d, correct, explanation = row[:9]
        exam_type = row[9] if len(row) > 9 else 'General'
        diff_int = diff_map.get(diff_raw, 2)
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff_int, exam_type,
             q, a, b, c, d, str(correct).lower(), explanation)
        )
