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

    # ── Section 0: Types of Bills ─────────────────────────────────────────────────
    (0, 1,
     "పార్లమెంట్‌లో ఏ సభలో మనీ బిల్లు ప్రవేశపెట్టవచ్చు?\n(In which House of Parliament can a Money Bill be introduced?)",
     "రాజ్యసభ (Rajya Sabha)", "లోక్‌సభ (Lok Sabha) మాత్రమే",
     "రెండు సభలలోనూ (Both Houses)", "రాష్ట్రపతి నిర్ణయించే సభలో",
     "b",
     "మనీ బిల్లు కేవలం లోక్‌సభలో మాత్రమే ప్రవేశపెట్టవచ్చు (Art.109). ఇది అధికారిక మంత్రి ద్వారా మాత్రమే ప్రవేశపెడతారు.\n(Money Bill can be introduced only in Lok Sabha under Art.109.)"),

    (0, 1,
     "మనీ బిల్లుకు రాజ్యసభ గరిష్టంగా ఎన్ని రోజులు ఉంచుకోవచ్చు?\n(For how many days can Rajya Sabha retain a Money Bill?)",
     "7 రోజులు", "14 రోజులు",
     "21 రోజులు", "1 నెల",
     "b",
     "Art.109 ప్రకారం రాజ్యసభ మనీ బిల్లును గరిష్టంగా 14 రోజులు మాత్రమే ఉంచుకోగలదు. ఆ తర్వాత లోక్‌సభ ఆమోదించినట్లు పరిగణిస్తారు.\n(Under Art.109, RS can retain a Money Bill for max 14 days; thereafter LS is deemed to have passed it.)"),

    (0, 2,
     "Art.110 కింద నిర్వచించిన మనీ బిల్లులో ఏ అంశాలు ఉంటాయి?\n(Which of the following is included in the definition of Money Bill under Art.110?)",
     "జీతాల నియంత్రణ", "పన్నుల విధింపు/రద్దు (Imposition/abolition of taxes)",
     "రాష్ట్ర జాబితా అంశాలు", "పోలీసు నిధులు",
     "b",
     "Art.110: పన్నుల విధింపు, రద్దు, మినహాయింపు, భారత సంఘటిత నిధి నుండి ధన వ్యయం, భారత ప్రభుత్వ అప్పులు — ఇవన్నీ మనీ బిల్లు కిందకు వస్తాయి.\n(Art.110 defines Money Bill as relating to taxes, Consolidated Fund of India expenditure, government borrowings, etc.)"),

    (0, 2,
     "ఫైనాన్స్ బిల్లు మరియు మనీ బిల్లు మధ్య తేడా ఏమిటి?\n(What is the key difference between a Finance Bill and a Money Bill?)",
     "ఫైనాన్స్ బిల్లు రాజ్యసభలో ప్రవేశపెడతారు",
     "ఫైనాన్స్ బిల్లు మనీ బిల్లు కంటే విస్తారమైనది — పన్నుతో పాటు ఇతర అంశాలు కలిగి ఉంటుంది\n(Finance Bill is broader — contains taxation + other provisions)",
     "మనీ బిల్లు రాష్ట్రపతి అనుమతి అవసరం లేదు",
     "రెండూ ఒకటే",
     "b",
     "ఫైనాన్స్ బిల్లులో (Art.117) పన్ను ప్రతిపాదనలతో పాటు ఇతర అంశాలూ ఉంటాయి. ఆర్థిక బిల్లు (Financial Bill Category-A) మనీ బిల్లు నిర్వచనానికి వర్తించదు.\n(Finance Bill under Art.117 contains taxation plus other provisions, broader than a Money Bill.)"),

    (0, 1,
     "సాధారణ బిల్లు (Ordinary Bill) పార్లమెంట్‌లో ఏ సభలో అయినా ప్రవేశపెట్టవచ్చా?\n(Can an Ordinary Bill be introduced in either House of Parliament?)",
     "కాదు, కేవలం లోక్‌సభలో మాత్రమే",
     "అవును, రెండు సభలలోనూ ప్రవేశపెట్టవచ్చు",
     "కేవలం రాజ్యసభలో మాత్రమే",
     "రాష్ట్రపతి నిర్ణయిస్తారు",
     "b",
     "Art.107: సాధారణ బిల్లు (Ordinary Bill) రెండు సభలలోనూ ప్రవేశపెట్టవచ్చు. రెండు సభలూ ఆమోదించాలి.\n(Under Art.107, Ordinary Bills can originate in either House; both Houses must pass them.)"),

    (0, 3,
     "ప్రైవేట్ మెంబర్ బిల్లుకు సంబంధించి సరైన వ్యాఖ్య ఏది?\n(Which statement about Private Member's Bill is correct?)",
     "కేవలం మంత్రులు మాత్రమే ప్రవేశపెట్టవచ్చు",
     "ప్రతి శుక్రవారం సాయంత్రం ప్రైవేట్ బిల్లులకు సమయం కేటాయిస్తారు",
     "ప్రైవేట్ బిల్లు ఆమోదానికి రాష్ట్రపతి అనుమతి అవసరం లేదు",
     "ప్రైవేట్ బిల్లు ఎప్పుడూ ఆమోదించబడదు",
     "b",
     "ప్రతి శుక్రవారం (2.5 గంటలు) ప్రైవేట్ మెంబర్ బిల్లులకు సమయం కేటాయిస్తారు. మంత్రి కాని సభ్యులు ప్రవేశపెట్టవచ్చు.\n(Every Friday afternoon is reserved for Private Member's Bills, introduced by non-minister MPs.)"),

    # ── Section 1: Stages of a Bill ──────────────────────────────────────────────
    (1, 1,
     "బిల్లు మొదటి పఠనం (First Reading) లో ఏమి జరుగుతుంది?\n(What happens at the First Reading of a Bill?)",
     "బిల్లుపై చర్చ జరుగుతుంది",
     "బిల్లు పరిచయం మరియు శీర్షిక చదవడం మాత్రమే\n(Introduction and reading of title only)",
     "కమిటీకి పంపుతారు",
     "ఓటింగ్ జరుగుతుంది",
     "b",
     "మొదటి పఠనంలో కేవలం బిల్లు ప్రవేశపెట్టడం మరియు శీర్షిక చదవడం జరుగుతుంది. ఈ దశలో చర్చ ఉండదు.\n(First Reading: Bill is introduced; only title is read. No debate at this stage.)"),

    (1, 2,
     "రెండవ పఠనం (Second Reading) లో ఏ దశలు ఉంటాయి?\n(Which stages are part of Second Reading of a Bill?)",
     "సాధారణ చర్చ మరియు కమిటీ దశ (General discussion + Committee stage)",
     "ఓటింగ్ మాత్రమే",
     "బిల్లు రద్దు",
     "రాష్ట్రపతి ఆమోదం",
     "a",
     "రెండవ పఠనంలో (Second Reading): 1) సాధారణ చర్చ (General Discussion), 2) కమిటీ దశ (Select/Joint Committee), 3) నివేదిక పరిశీలన (Consideration of Report) — మూడు ఉప-దశలు ఉంటాయి.\n(Second Reading has three sub-stages: General discussion, Committee stage, and Consideration of report.)"),

    (1, 1,
     "మూడవ పఠనంలో (Third Reading) ఏమి జరుగుతుంది?\n(What happens at the Third Reading of a Bill?)",
     "బిల్లు మొత్తంపై ఓటింగ్ జరుగుతుంది (Final vote on the Bill)",
     "కమిటీ నివేదిక సమర్పించబడుతుంది",
     "బిల్లు ప్రవేశపెట్టబడుతుంది",
     "రాష్ట్రపతి సంతకం చేస్తారు",
     "a",
     "మూడవ పఠనంలో బిల్లు మొత్తంపై తుది ఓటింగ్ జరుగుతుంది. ఈ దశలో కేవలం సవరణలు కాదు, మొత్తం బిల్లు అంగీకారం/తిరస్కరణ జరుగుతుంది.\n(Third Reading: Final vote on the entire Bill — accept or reject.)"),

    (1, 2,
     "సంయుక్త సమావేశం (Joint Sitting) జరగని స్థితి ఏది?\n(In which situation does a Joint Sitting NOT take place?)",
     "ఒక సభ బిల్లును తిరస్కరించినప్పుడు",
     "మనీ బిల్లు విషయంలో (In case of Money Bill)",
     "బిల్లుపై సభలు విభేదించినప్పుడు",
     "బిల్లు 6 నెలలు పెండింగ్‌లో ఉన్నప్పుడు",
     "b",
     "మనీ బిల్లు విషయంలో (Art.110) సంయుక్త సమావేశం జరగదు. అలాగే రాజ్యాంగ సవరణ బిల్లుకూ జరగదు. కేవలం సాధారణ బిల్లులకు మాత్రమే Art.108 వర్తిస్తుంది.\n(Joint Sitting under Art.108 does NOT apply to Money Bills or Constitution Amendment Bills.)"),

    (1, 3,
     "రాష్ట్రపతి బిల్లుపై 'Pocket Veto' అంటే ఏమిటి?\n(What is 'Pocket Veto' in relation to a Bill?)",
     "బిల్లుపై సంతకం చేయడం",
     "బిల్లును నిరవధిగా చర్చకు పంపడం",
     "బిల్లుపై నిర్ణయం తీసుకోకుండా వదిలేయడం (No action — indefinite inaction)",
     "బిల్లు రద్దు చేయడం",
     "c",
     "భారత రాజ్యాంగంలో పాకెట్ వీటో కోసం నిర్ణీత సమయ పరిమితి లేదు (US లో 10 రోజులు ఉంది). రాష్ట్రపతి జైల్ సింగ్ (1982–87) Indian Post Office (Amendment) Bill 1986పై నిర్ణయం తీసుకోకుండా వదిలేశారు — ఇది పాకెట్ వీటోకు ప్రముఖ ఉదాహరణ.\n(India's President has no time limit for action on Bills — allows 'Pocket Veto'. President Zail Singh notably used it on the Indian Post Office (Amendment) Bill 1986, not any Amendment Bill.)"),

    # ── Section 2: Question Hour ──────────────────────────────────────────────────
    (2, 1,
     "ప్రశ్నోత్తర సమయం (Question Hour) ఎప్పుడు ఉంటుంది?\n(When is the Question Hour held in Parliament?)",
     "12 గంటలకు", "11 గంటల నుండి 12 గంటల వరకు",
     "2 గంటల నుండి 4 గంటల వరకు", "సమావేశం ముగింపులో",
     "b",
     "పార్లమెంట్ ప్రశ్నోత్తర సమయం సాధారణంగా పూర్వాహ్నం 11:00 నుండి 12:00 గంటల వరకు ఉంటుంది — సమావేశపు మొదటి గంట.\n(Question Hour is the first hour of parliamentary sitting — 11:00 AM to 12:00 PM.)"),

    (2, 1,
     "స్టార్ చేయబడిన ప్రశ్న (Starred Question) అంటే ఏమిటి?\n(What is a Starred Question in Parliament?)",
     "వ్రాతపూర్వక సమాధానం కోసం అడిగే ప్రశ్న",
     "మౌఖిక సమాధానం అవసరమయ్యే ప్రశ్న — అనుబంధ ప్రశ్నలు అడగవచ్చు\n(Oral answer required — supplementary questions allowed)",
     "లోక్‌సభ స్పీకర్ మాత్రమే అడగగలిగే ప్రశ్న",
     "ప్రధానమంత్రి సమాధానం ఇచ్చే ప్రశ్న",
     "b",
     "స్టార్ ప్రశ్న (*): మౌఖిక సమాధానం అవసరం, అనుబంధ ప్రశ్నలు అడగవచ్చు. అన్‌స్టార్ ప్రశ్న: వ్రాతపూర్వక సమాధానం, అనుబంధ ప్రశ్నలు అడగరు.\n(Starred Question requires oral reply; supplementary questions allowed. Unstarred = written reply; no supplementary.)"),

    (2, 2,
     "షార్ట్ నోటీస్ ప్రశ్న (Short Notice Question) ఎంత నోటీసుతో అడగవచ్చు?\n(Short Notice Question can be asked with how many days' notice?)",
     "15 రోజులు", "10 రోజుల కంటే తక్కువ నోటీసుతో",
     "30 రోజులు", "నోటీసు అవసరం లేదు",
     "b",
     "సాధారణంగా ప్రశ్నలకు 10 రోజుల నోటీసు అవసరం. 10 రోజుల కంటే తక్కువ నోటీసుతో అడిగేవి షార్ట్ నోటీస్ ప్రశ్నలు — అత్యవసర స్వభావం ఉంటుంది.\n(Normally 10 days notice is required. Short Notice Questions are asked with less than 10 days notice on urgent matters.)"),

    (2, 2,
     "జీరో అవర్ (Zero Hour) గురించి సరైన వ్యాఖ్య ఏది?\n(Which statement about Zero Hour is correct?)",
     "రాజ్యాంగంలో పేర్కొనబడిన సమయం",
     "12 గంటల నుండి సమావేశాల నియమాలలో లేని అనధికారిక సమయం\n(Informal, not in rules — starts at 12 noon)",
     "ప్రశ్నోత్తర సమయంలో భాగం",
     "బడ్జెట్ చర్చకు కేటాయించిన సమయం",
     "b",
     "జీరో అవర్ సమావేశాల నియమాలలో లేదు — ఇది భారతీయ పార్లమెంటరీ ఆచారం. 12 గంటల నుండి మొదలై, సభ్యులు అత్యవసర అంశాలు లేవనెత్తుతారు.\n(Zero Hour is not mentioned in Parliamentary rules — it's an Indian innovation, starting at 12 noon for urgent public matters.)"),

    (2, 1,
     "అన్‌స్టార్డ్ ప్రశ్న (Unstarred Question) కి ఎలాంటి సమాధానం ఉంటుంది?\n(What type of answer does an Unstarred Question receive?)",
     "మౌఖిక సమాధానం + అనుబంధ ప్రశ్నలు",
     "వ్రాతపూర్వక సమాధానం మాత్రమే — అనుబంధ ప్రశ్నలు అడగరు\n(Written answer only — no supplementary questions)",
     "ప్రధానమంత్రి సమాధానం",
     "స్పీకర్ నిర్ణయిస్తారు",
     "b",
     "అన్‌స్టార్డ్ ప్రశ్నలకు వ్రాతపూర్వక సమాధానం మాత్రమే ఇస్తారు. సభలో మౌఖికంగా చదవరు; అనుబంధ ప్రశ్నలు అడగరు.\n(Unstarred Questions receive only written replies placed on the table; no oral reading and no supplementaries.)"),

    # ── Section 3: Motions ────────────────────────────────────────────────────────
    (3, 2,
     "వాయిదా తీర్మానం (Adjournment Motion) గురించి సరైన వ్యాఖ్య ఏది?\n(Which statement about Adjournment Motion is correct?)",
     "రాజ్యసభలో మాత్రమే ప్రవేశపెట్టవచ్చు",
     "లోక్‌సభలో మాత్రమే, అత్యవసర జాతీయ ప్రాధాన్యత గల అంశంపై — 50 సభ్యుల మద్దతు అవసరం",
     "ఇది సభను వాయిదా వేయాలని కోరే తీర్మానం",
     "ప్రతిసారి ఆమోదిస్తారు",
     "b",
     "వాయిదా తీర్మానం (Adjournment Motion) లోక్‌సభలో మాత్రమే — అత్యవసర జాతీయ ప్రాముఖ్యత గల అంశంపై. దీనికి 50 సభ్యుల మద్దతు అవసరం. ఆమోదమైతే ప్రభుత్వ నైతిక ఓటమి.\n(Adjournment Motion: only in LS, urgent public importance, needs support of 50 members. If passed, it's a censure of the Government.)"),

    (3, 2,
     "అవిశ్వాస తీర్మానం (No-Confidence Motion) ఏ సభలో ప్రవేశపెట్టవచ్చు?\n(In which House can a No-Confidence Motion be introduced?)",
     "రాజ్యసభలో మాత్రమే",
     "రెండు సభలలోనూ",
     "లోక్‌సభలో మాత్రమే — Art.75(3)",
     "రాష్ట్రపతి అనుమతితో రెండింటిలోనూ",
     "c",
     "Art.75(3): మంత్రి మండలి లోక్‌సభకు మాత్రమే జవాబుదారీగా ఉంటుంది. అందువల్ల అవిశ్వాస తీర్మానం (No-Confidence Motion) కేవలం లోక్‌సభలో మాత్రమే ప్రవేశపెట్టవచ్చు. 50 సభ్యుల మద్దతు అవసరం.\n(Art.75(3): Council of Ministers is collectively responsible to Lok Sabha only. NCM introduced only in LS; needs 50 members support.)"),

    (3, 2,
     "నిందా తీర్మానం (Censure Motion) మరియు అవిశ్వాస తీర్మానం మధ్య తేడా ఏమిటి?\n(What is the difference between Censure Motion and No-Confidence Motion?)",
     "రెండూ ఒకటే",
     "నిందా తీర్మానం నిర్దిష్ట విధానంపై — ఆమోదమైతే ప్రభుత్వం రాజీనామా చేయవలసిన అవసరం లేదు\n(Censure is on specific policy — no mandatory resignation if passed)",
     "నిందా తీర్మానం రాజ్యసభలో ప్రవేశపెడతారు",
     "అవిశ్వాస తీర్మానానికి రాష్ట్రపతి అనుమతి అవసరం",
     "b",
     "నిందా తీర్మానం (Censure Motion): నిర్దిష్ట మంత్రి/విధానంపై నిందించడానికి. ఆమోదమైనా ప్రభుత్వం రాజీనామా చేయకపోవచ్చు. అవిశ్వాస తీర్మానం ఆమోదమైతే తప్పనిసరిగా రాజీనామా చేయాలి.\n(Censure Motion targets a specific policy/minister; if passed, govt need not resign. NCM — if passed, govt must resign.)"),

    (3, 3,
     "కట్ మోషన్ (Cut Motion) రకాలు ఏవి?\n(What are the types of Cut Motion?)",
     "Policy Cut, Economy Cut, Token Cut",
     "నిందా కట్, విధాన కట్",
     "ఒకే రకం",
     "రెండే రకాలు",
     "a",
     "మూడు రకాల కట్ మోషన్లు:\n1) Policy Cut: డిమాండ్ ₹1కు తగ్గించడం — విధానాన్ని వ్యతిరేకించడం\n2) Economy Cut: నిర్దిష్ట మొత్తం తగ్గించాలని\n3) Token Cut: ₹100కు తగ్గించడం — నిర్దిష్ట సమస్య ప్రస్తావించడం\n(Three types of Cut Motions: Policy Cut (₹1), Economy Cut (specific amount), Token Cut (₹100 — to raise specific grievance).)"),

    (3, 2,
     "కాలింగ్ అటెన్షన్ మోషన్ (Calling Attention Motion) ఎవరు ప్రవేశపెడతారు?\n(Who introduces a Calling Attention Motion?)",
     "ప్రభుత్వం",
     "స్పీకర్",
     "సభ్యుడు — అత్యవసర అంశంపై మంత్రి దృష్టికి తీసుకురావడానికి\n(By a member — to draw minister's attention to urgent matter)",
     "రాష్ట్రపతి",
     "c",
     "కాలింగ్ అటెన్షన్ మోషన్ భారతీయ పార్లమెంటరీ ఆచారం (1954లో ప్రవేశపెట్టారు). సభ్యుడు స్పీకర్ అనుమతితో అత్యవసర అంశంపై మంత్రి దృష్టికి తెస్తారు.\n(Calling Attention Motion — Indian innovation (introduced 1954). An MP, with Speaker's permission, draws a minister's attention to urgent matter.)"),

    # ── Section 4: Budget Procedure ──────────────────────────────────────────────
    (4, 1,
     "వార్షిక ఆర్థిక వివరణ (Annual Financial Statement) ఏ అనుచ్ఛేదం కింద ఉంటుంది?\n(Under which Article is the Annual Financial Statement provided?)",
     "Art.110", "Art.112",
     "Art.116", "Art.360",
     "b",
     "Art.112: రాష్ట్రపతి ప్రతి సంవత్సరం పార్లమెంట్ ముందు వార్షిక ఆర్థిక వివరణ (బడ్జెట్) ఉంచుతారు. ఇది ఆదాయ-వ్యయాల అంచనాలు చూపిస్తుంది.\n(Art.112: President causes Annual Financial Statement — the Budget — to be laid before Parliament every year.)"),

    (4, 2,
     "వోట్ ఆన్ అకౌంట్ (Vote on Account) అంటే ఏమిటి?\n(What is Vote on Account?)",
     "బడ్జెట్ ఆమోదం",
     "బడ్జెట్ చర్చ ముగిసేంత వరకు ప్రభుత్వ వ్యయానికి తాత్కాలిక అనుమతి\n(Temporary grant for govt expenditure till Budget is passed)",
     "సప్లిమెంటరీ బడ్జెట్",
     "అప్రూప్రియేషన్ బిల్లు",
     "b",
     "వోట్ ఆన్ అకౌంట్ (Art.116): బడ్జెట్ ఆమోదానికి ముందు, ప్రభుత్వ నిత్యావసర వ్యయానికి పార్లమెంట్ తాత్కాలిక అనుమతి ఇస్తుంది. సాధారణంగా 2 నెలల అంచనా వ్యయానికి.\n(Vote on Account — Art.116: Temporary Parliamentary sanction for govt expenditure until Budget is passed, usually for 2 months.)"),

    (4, 2,
     "గిలోటిన్ (Guillotine) అంటే పార్లమెంటరీ పరిభాషలో ఏమిటి?\n(What does 'Guillotine' mean in Parliamentary terminology?)",
     "స్పీకర్ అధికారం",
     "అంచనా సమయం ముగిసినప్పుడు మిగిలిన డిమాండ్లన్నీ చర్చ లేకుండా ఓటింగ్‌కు పెట్టడం\n(All outstanding demands voted at end of Budget session without discussion)",
     "అత్యవసర బడ్జెట్",
     "వోట్ ఆన్ అకౌంట్",
     "b",
     "బడ్జెట్ సమావేశంలో నిర్ణీత తేదీనాడు చర్చించని డిమాండ్లన్నీ ఒకేసారి ఓటింగ్‌కు పెడతారు — దీన్ని గిలోటిన్ (Guillotine) అంటారు.\n(Guillotine: On the last day allotted for Budget, all undiscussed Demands for Grants are put to vote simultaneously without discussion.)"),

    (4, 2,
     "అప్రూప్రియేషన్ బిల్లు (Appropriation Bill) ఎందుకు అవసరం?\n(Why is Appropriation Bill necessary?)",
     "పన్నుల విధింపు కోసం",
     "సంఘటిత నిధి నుండి ధనం తీసుకోవడానికి పార్లమెంట్ అనుమతి — Art.114\n(Parliamentary authorization to withdraw from Consolidated Fund — Art.114)",
     "రాష్ట్రాలకు నిధులు కేటాయించడానికి",
     "రాష్ట్రపతి జీతం చెల్లించడానికి",
     "b",
     "Art.114: భారత సంఘటిత నిధి (Consolidated Fund of India) నుండి ఎలాంటి ధనమైనా తీసుకోవాలంటే అప్రూప్రియేషన్ బిల్లు ఆమోదించాలి. ఇది పార్లమెంట్ ఆమోదించాలి.\n(Art.114: No money can be withdrawn from Consolidated Fund of India without passing an Appropriation Bill.)"),

    (4, 3,
     "ఫైనాన్స్ బిల్లు (Finance Bill) ఆమోదించకపోతే ఏమవుతుంది?\n(What happens if the Finance Bill is not passed?)",
     "ఏమీ కాదు",
     "కొత్త పన్నులు విధించడం చట్టవిరుద్ధం అవుతుంది",
     "ప్రభుత్వం తప్పనిసరిగా రాజీనామా చేయాలి — ఇది విశ్వాస ఓటుతో సమానం\n(Govt must resign — equivalent to loss of confidence)",
     "రాష్ట్రపతి పాలన విధించవచ్చు",
     "c",
     "ఫైనాన్స్ బిల్లు తిరస్కరించబడటం ప్రభుత్వానికి అవిశ్వాస ఓటుతో సమానం. ప్రభుత్వం తప్పనిసరిగా రాజీనామా చేయాలి లేదా లోక్‌సభ రద్దు కోరాలి.\n(Defeat of Finance Bill = No-Confidence in Government. Govt must resign or request dissolution of Lok Sabha.)"),

    # ── Section 5: Parliamentary Committees ──────────────────────────────────────
    (5, 2,
     "ప్రజా లెక్కల కమిటీ (Public Accounts Committee – PAC) లో ఎంత మంది సభ్యులు ఉంటారు?\n(How many members are in the Public Accounts Committee?)",
     "15 మంది మాత్రమే (లోక్‌సభ నుండి)",
     "22 మంది — 15 లోక్‌సభ + 7 రాజ్యసభ",
     "30 మంది",
     "45 మంది",
     "b",
     "PAC: 22 మంది సభ్యులు — 15 లోక్‌సభ నుండి, 7 రాజ్యసభ నుండి. అధ్యక్షుడు 1967 నుండి ప్రతిపక్ష సభ్యుడు అవుతున్నారు.\n(PAC has 22 members — 15 from LS + 7 from RS. Since 1967, Chairman is from Opposition.)"),

    (5, 1,
     "అంచనాల కమిటీ (Estimates Committee) లో ఎంత మంది సభ్యులు ఉంటారు, ఏ సభ నుండి?\n(Estimates Committee has how many members and from which House?)",
     "22 మంది — రెండు సభల నుండి",
     "30 మంది — కేవలం లోక్‌సభ నుండి\n(30 members — only from Lok Sabha)",
     "15 మంది — రాజ్యసభ నుండి",
     "24 మంది — రెండు సభల నుండి",
     "b",
     "అంచనాల కమిటీ (Estimates Committee): 30 మంది సభ్యులు — కేవలం లోక్‌సభ నుండి మాత్రమే. ఇది అతిపెద్ద ఆర్థిక పార్లమెంటరీ కమిటీ. రాజ్యసభ సభ్యులు ఈ కమిటీలో ఉండరు.\n(Estimates Committee: 30 members exclusively from LS — largest financial committee. RS members are NOT part of it.)"),

    (5, 2,
     "PAC మరియు Estimates Committee మధ్య ప్రధాన తేడా ఏమిటి?\n(Key difference between PAC and Estimates Committee?)",
     "రెండూ ఒకటే పని చేస్తాయి",
     "PAC వ్యయం తర్వాత తనిఖీ చేస్తుంది (post-expenditure); Estimates Committee వ్యయానికి ముందు అంచనాలు పరిశీలిస్తుంది (pre-expenditure)\n(PAC — post-audit; Estimates — pre-expenditure review)",
     "Estimates Committee లోక్‌సభలో ఉండదు",
     "PAC కేవలం రక్షణ వ్యయం చూస్తుంది",
     "b",
     "PAC (ప్రజా లెక్కల కమిటీ): కంప్ట్రోలర్ & ఆడిటర్ జనరల్ (CAG) నివేదికలు పరిశీలిస్తుంది — వ్యయం తర్వాత తనిఖీ. Estimates Committee: బడ్జెట్ అంచనాలు పరిశీలిస్తుంది — వ్యయానికి ముందు.\n(PAC scrutinises CAG reports — post-expenditure audit. Estimates Committee examines estimates — pre-expenditure.)"),

    (5, 2,
     "ప్రజా సంస్థల కమిటీ (Committee on Public Undertakings – CoPU) ఎంత మంది సభ్యులు ఉంటారు?\n(How many members does the Committee on Public Undertakings have?)",
     "30 మంది", "15 మంది",
     "22 మంది — 15 లోక్‌సభ + 7 రాజ్యసభ",
     "45 మంది",
     "c",
     "CoPU (Committee on Public Undertakings): 22 మంది సభ్యులు — 15 లోక్‌సభ నుండి, 7 రాజ్యసభ నుండి. ప్రభుత్వ రంగ సంస్థల పని పరిశీలిస్తుంది.\n(CoPU: 22 members — 15 from LS + 7 from RS. It examines the working of Public Sector Undertakings.)"),

    (5, 3,
     "డిపార్ట్‌మెంట్ రిలేటెడ్ స్టాండింగ్ కమిటీలు (DRSCs) ప్రస్తుతం ఎన్ని ఉన్నాయి?\n(How many Departmentally Related Standing Committees currently exist?)",
     "16", "24",
     "12", "30",
     "b",
     "1993లో ప్రవేశపెట్టిన డిపార్ట్‌మెంటల్ స్టాండింగ్ కమిటీలు ప్రస్తుతం 24 ఉన్నాయి. ప్రతి కమిటీలో 31 మంది సభ్యులు (21 LS + 10 RS) ఉంటారు.\n(24 DRSCs were introduced in 1993 (initially 17, expanded to 24). Each committee has 31 members — 21 from LS + 10 from RS.)"),

    (5, 2,
     "బిజినెస్ అడ్వైజరీ కమిటీ (Business Advisory Committee – BAC) అధ్యక్షుడు ఎవరు?\n(Who chairs the Business Advisory Committee?)",
     "ప్రధానమంత్రి", "లోక్‌సభ స్పీకర్",
     "రాజ్యసభ చైర్మన్", "సభ్యులు ఎన్నుకుంటారు",
     "b",
     "లోక్‌సభ బిజినెస్ అడ్వైజరీ కమిటీ అధ్యక్షుడు స్పీకర్. రాజ్యసభ BAC అధ్యక్షుడు చైర్మన్ (VP). ఇది పార్లమెంట్ కార్యక్రమ సమయపాలన నిర్ణయిస్తుంది.\n(BAC Chairman in LS is the Speaker; in RS is the Chairman (VP). It allocates time for parliamentary business.)"),

    # ── Section 6: Constitutional Amendment Procedure ────────────────────────────
    (6, 2,
     "Art.368 కింద రాజ్యాంగ సవరణ విధానంలో ఎన్ని రకాలు ఉన్నాయి?\n(How many methods of Constitutional Amendment exist under Art.368?)",
     "రెండు రకాలు",
     "మూడు రకాలు — సాధారణ మెజారిటీ, ప్రత్యేక మెజారిటీ, ప్రత్యేక మెజారిటీ+అర్ధ రాష్ట్రాల ఆమోదం\n(Three types — Simple majority, Special majority, Special majority + ratification)",
     "నాలుగు రకాలు",
     "ఒకటే రకం",
     "b",
     "రాజ్యాంగ సవరణ మూడు విధాలుగా:\n1) సాధారణ మెజారిటీ (Simple Majority) — Art.368 వర్తించదు\n2) ప్రత్యేక మెజారిటీ (Special Majority) — 2/3 + 50% మొత్తం సభ్యులు\n3) ప్రత్యేక మెజారిటీ + కనీసం సగం రాష్ట్రాల ఆమోదం\n(Three methods: Simple majority (not Art.368), Special majority (2/3 + absolute majority), Special majority + ratification by at least half states.)"),

    (6, 2,
     "రాజ్యాంగ సవరణకు ప్రత్యేక మెజారిటీ (Special Majority) అంటే ఏమిటి?\n(What is 'Special Majority' for Constitutional Amendment?)",
     "సభలో హాజరైన వారిలో 2/3 మెజారిటీ మాత్రమే",
     "మొత్తం సభ్యత్వంలో 50%+ మరియు హాజరై ఓటు చేసిన వారిలో 2/3 — రెండూ అవసరం\n(Absolute majority of total membership AND 2/3 of present and voting — both required)",
     "కేవలం 3/4 మెజారిటీ",
     "సాధారణ మెజారిటీ",
     "b",
     "ప్రత్యేక మెజారిటీ: రెండు షరతులు తప్పనిసరి — (1) మొత్తం సభ్యత్వంలో సగానికి పైగా (Absolute Majority), మరియు (2) హాజరై ఓటు చేసినవారిలో 2/3 (Special Majority). రెండూ కలిపితేనే ఆమోదం.\n(Special Majority: BOTH conditions must be met — (1) majority of total membership (absolute), AND (2) 2/3 of present and voting.)"),

    (6, 3,
     "ఏ అంశాలను సవరించేటప్పుడు రాష్ట్రాల ఆమోదం కూడా అవసరం?\n(For which provisions is ratification by states also required?)",
     "ఏ సవరణకైనా రాష్ట్రాల ఆమోదం అవసరం",
     "కేవలం ఆర్థిక అంశాలకు మాత్రమే",
     "సమాఖ్య లక్షణాలకు — రాష్ట్రపతి ఎన్నిక, SC అధికార పరిధి, రాష్ట్ర జాబితా, ఏడవ షెడ్యూల్, పార్లమెంట్ ప్రాతినిధ్యం\n(Federal features — President's election, SC jurisdiction, 7th Schedule, etc.)",
     "రాజ్యాంగ ప్రాథమిక హక్కుల సవరణకు",
     "c",
     "కింది అంశాల సవరణకు రాష్ట్రాల ఆమోదం (కనీసం సగం రాష్ట్రాలు) అవసరం: రాష్ట్రపతి ఎన్నిక, SC మరియు HC అధికార పరిధి, కేంద్ర-రాష్ట్ర శాసన వ్యాప్తి, సప్తమ షెడ్యూల్, పార్లమెంట్‌లో రాష్ట్ర ప్రాతినిధ్యం, Art.368 స్వయంగా.\n(Federal features needing state ratification: President's election, SC/HC jurisdiction, legislative distribution, 7th Schedule, parliamentary representation of states, Art.368 itself.)"),

    (6, 2,
     "రాజ్యాంగ సవరణ బిల్లుకు సంయుక్త సమావేశం జరుగుతుందా?\n(Can a Joint Sitting be convened for a Constitutional Amendment Bill?)",
     "అవును, Art.108 వర్తిస్తుంది",
     "కాదు — రాజ్యాంగ సవరణ బిల్లుకు Art.108 వర్తించదు; ప్రతి సభ ప్రత్యేకంగా ఆమోదించాలి\n(No — Art.108 does not apply; each House must independently pass it)",
     "కేవలం రాజ్యసభ వ్యతిరేకించినప్పుడు",
     "రాష్ట్రపతి అనుమతితో",
     "b",
     "రాజ్యాంగ సవరణ బిల్లుకు Art.108 (సంయుక్త సమావేశం) వర్తించదు. ప్రతి సభ తప్పనిసరిగా ప్రత్యేకంగా ఆమోదించాలి. రాజ్యసభ తిరస్కరించినా సంయుక్త సమావేశం జరగదు.\n(Art.108 Joint Sitting does NOT apply to Constitutional Amendment Bills. Each House must independently pass with special majority.)"),

    (6, 2,
     "రాజ్యాంగ సవరణ బిల్లుపై రాష్ట్రపతి తన అనుమతిని నిరాకరించగలరా?\n(Can the President withhold assent to a Constitutional Amendment Bill?)",
     "అవును, సాధారణ బిల్లులాంటిదే",
     "కాదు — 24వ సవరణ చట్టం (1971) తర్వాత రాష్ట్రపతి తప్పనిసరిగా ఆమోదం తెలపాలి\n(No — after 24th Amendment 1971, President must give assent)",
     "కేవలం 6 నెలలు ఆలస్యం చేయవచ్చు",
     "అవును, రెండుసార్లు తిరిగి పంపించవచ్చు",
     "b",
     "24వ రాజ్యాంగ సవరణ చట్టం (1971): రాజ్యాంగ సవరణ బిల్లుపై రాష్ట్రపతి తప్పనిసరిగా ఆమోదం (assent) తెలపాలి — నిరాకరించే అధికారం లేదు.\n(24th Constitutional Amendment Act, 1971: President is obligated to give assent to Constitutional Amendment Bills — cannot withhold or return.)"),

    # ── Section 7: Tough PYQs ─────────────────────────────────────────────────────
    (7, 3,
     "మనీ బిల్లు అని నిర్ణయించే అధికారం ఎవరికి ఉంది?\n(Who has the final authority to decide whether a Bill is a Money Bill?)",
     "రాజ్యసభ చైర్మన్",
     "రాష్ట్రపతి",
     "లోక్‌సభ స్పీకర్ — నిర్ణయం తుది మరియు అంతిమం\n(Lok Sabha Speaker — decision is final)",
     "సుప్రీం కోర్టు",
     "c",
     "Art.110(3): మనీ బిల్లు అని లోక్‌సభ స్పీకర్ ధృవీకరిస్తారు. ఆ నిర్ణయం తుది మరియు అన్ని ప్రయోజనాల దృష్ట్యా అంతిమంగా ఉంటుంది. కోర్టులు సాధారణంగా ప్రశ్నించవు.\n(Art.110(3): Speaker of LS certifies a Bill as Money Bill; decision is final for all purposes — courts generally do not question it.)"),

    (7, 3,
     "లేమ్-డక్ సమావేశం (Lame-Duck Session) అంటే ఏమిటి?\n(What is a 'Lame-Duck Session' of Parliament?)",
     "అత్యంత ఉత్పాదకమైన సమావేశం",
     "కొత్త లోక్‌సభ ఎన్నికల తర్వాత మరియు కొత్త లోక్‌సభ మొదలవడానికి ముందు పాత సభ్యుల ద్వారా జరిగే సమావేశం\n(Session held by outgoing LS after new elections but before new LS meets)",
     "రాజ్యసభ ప్రత్యేక సమావేశం",
     "ఆర్థిక అత్యవసర సమావేశం",
     "b",
     "లేమ్-డక్ సమావేశం: కొత్త లోక్‌సభ ఎన్నికయిన తర్వాత, కానీ పని ప్రారంభించడానికి ముందు, పాత లోక్‌సభ సభ్యులు జరిపే సమావేశం. ఓడిపోయిన/రిటైరైన సభ్యులు పాల్గొంటారు.\n(Lame-Duck Session: Session attended by outgoing members who failed to win re-election, held after new elections but before new House meets.)"),

    (7, 4,
     "AADHAAR Act 2016 మనీ బిల్లుగా వర్గీకరించడం వివాదాస్పదమైంది — ఎందుకు?\n(Why was classifying Aadhaar Act 2016 as a Money Bill controversial?)",
     "ఎందుకంటే అది రాజ్యసభలో ప్రవేశపెట్టబడింది",
     "ఆధార్ చట్టం Art.110 నిర్వచనం ప్రకారం పూర్తిగా మనీ బిల్లు కాదు అని విమర్శించారు — రాజ్యసభను దాటవేశారని\n(Critics said it didn't qualify strictly under Art.110 — used to bypass RS)",
     "రాష్ట్రపతి ఆమోదం ఇవ్వలేదు",
     "ఏ వివాదమూ లేదు",
     "b",
     "ఆధార్ చట్టం 2016: స్పీకర్ మనీ బిల్లుగా ధృవీకరించారు — రాజ్యసభ సవరణ అధికారం లేకుండా ఆమోదించారు. సుప్రీం కోర్టు (Jairam Ramesh v. Union of India, 2018 రిఫరెన్స్) ఈ వర్గీకరణను సవాలు చేశారు.\n(Aadhaar Act 2016 certified as Money Bill — bypassed RS. Constitutionality challenged; SC in K.S. Puttaswamy referred the Money Bill classification question to a larger bench.)"),

    (7, 3,
     "పార్లమెంట్ సమావేశానికి సంబంధించి గరిష్ట విరామ కాలం (Maximum Gap between Sessions) ఏమిటి?\n(What is the maximum gap allowed between two Parliamentary sessions?)",
     "3 నెలలు", "4 నెలలు",
     "6 నెలలు",
     "1 సంవత్సరం",
     "c",
     "Art.85(1): పార్లమెంట్ రెండు సమావేశాల మధ్య విరామం 6 నెలలు మించకూడదు. సంవత్సరానికి కనీసం రెండు సమావేశాలు జరగాలి.\n(Art.85(1): Maximum gap between two Parliamentary sessions is 6 months. At least two sessions must be held every year.)"),

    (7, 3,
     "మొదటి అవిశ్వాస తీర్మానం లోక్‌సభలో ఎప్పుడు ప్రవేశపెట్టబడింది?\n(When was the first No-Confidence Motion moved in Lok Sabha?)",
     "1952", "1963",
     "1974", "1979",
     "b",
     "భారత లోక్‌సభలో మొదటి అవిశ్వాస తీర్మానం 1963లో జె.బి. కృపలానీ నేతృత్వంలో ప్రవేశపెట్టారు — నెహ్రూ ప్రభుత్వానికి వ్యతిరేకంగా. ఇది వీగిపోయింది.\n(First No-Confidence Motion in Indian Parliament was moved by J.B. Kripalani in 1963 against Nehru's government — it was defeated.)",
     'APPSC'),

    (7, 4,
     "పార్లమెంట్‌లో 'ప్రివిలేజ్ మోషన్' (Privilege Motion) అంటే ఏమిటి?\n(What is a 'Privilege Motion' in Parliament?)",
     "మంత్రికి ప్రత్యేక హక్కు ఇచ్చే తీర్మానం",
     "సభ్యుడు మంత్రి లేదా ఇతర సభ్యుడు పార్లమెంటరీ హక్కులు ఉల్లంఘించారని ఆరోపించే తీర్మానం\n(Motion alleging breach of Parliamentary privilege by minister/member)",
     "స్పీకర్ తన హక్కులు ప్రకటించే తీర్మానం",
     "ప్రత్యేక మంత్రి హాజరు కోసం తీర్మానం",
     "b",
     "ప్రివిలేజ్ మోషన్ (Privilege Motion): ఒక సభ్యుడు మంత్రి/ఇతర సభ్యుడు పార్లమెంటరీ హక్కులను ఉల్లంఘించారని ఆరోపిస్తే దాఖలు చేసే తీర్మానం. స్పీకర్ ప్రివిలేజ్ కమిటీకి పంపవచ్చు.\n(Privilege Motion: Filed when a member alleges breach of Parliamentary privilege by a minister/member. Speaker may refer it to Privileges Committee.)"),

    (7, 3,
     "లోక్‌సభలో 'హాఫ్ అవర్ డిస్కషన్' (Half-Hour Discussion) ఎప్పుడు జరుగుతుంది?\n(When does 'Half-Hour Discussion' take place in Lok Sabha?)",
     "ప్రశ్నోత్తర సమయంలో",
     "సమావేశం ముందు",
     "సమావేశం చివరి అర గంటలో — నిర్దిష్ట విషయంపై మాట్లాడటానికి\n(In the last half hour of sitting — to elaborate on a specific question)",
     "జీరో అవర్‌లో",
     "c",
     "హాఫ్ అవర్ డిస్కషన్ (Half-Hour Discussion): వారంలో మూడు రోజులు సమావేశం చివరి అర గంటలో జరుగుతుంది. ఇప్పటికే అడిగిన ప్రశ్న నుండి ఉత్పన్నమయిన ముఖ్యమైన అంశంపై చర్చ.\n(Half-Hour Discussion: Held on 3 days a week in the last half-hour of sitting, on a matter of sufficient public importance arising out of a question already asked.)"),

    (7, 4,
     "నిర్ణీత సమావేశ రోజుల కంటే ఎక్కువగా అవిశ్వాస తీర్మానాన్ని ఆమోదించారంటే ఏ ప్రభుత్వం పడిపోయింది?\n(Which government fell after passing a No-Confidence Motion in India for the first time?)",
     "ఇందిరా గాంధీ ప్రభుత్వం (1979)",
     "వాజ్‌పేయి ప్రభుత్వం (1999) — ఒక్క ఓటు తేడాతో\n(Vajpayee Govt 1999 — by one vote margin)",
     "మొరార్జీ దేశాయ్ ప్రభుత్వం (1979)",
     "చంద్రశేఖర్ ప్రభుత్వం (1991)",
     "b",
     "1999లో వాజ్‌పేయి ప్రభుత్వం కేవలం ఒక్క ఓటు తేడాతో అవిశ్వాస తీర్మానంతో పడిపోయింది — 269 vs 270. ఇది భారత పార్లమెంటరీ చరిత్రలో అత్యంత నాటకీయ సంఘటన.\n(Vajpayee's government fell in 1999 by a single vote — 269 to 270 — in the No-Confidence Motion vote. Most dramatic in Indian parliamentary history.)",
     'APPSC'),

    # ── Additional MCQs — Sections 0–7 (filling to ~65 total) ─────────────────

    (0, 2,
     "రాజ్యసభలో మనీ బిల్లుకు సంబంధించి సరైన వ్యాఖ్య ఏది?\n(Which statement about Money Bill in Rajya Sabha is correct?)",
     "రాజ్యసభ మనీ బిల్లును తిరస్కరించవచ్చు",
     "రాజ్యసభ మనీ బిల్లును సవరించవచ్చు",
     "రాజ్యసభ మనీ బిల్లుపై సిఫార్సులు (Recommendations) మాత్రమే చేయగలదు — లోక్‌సభ తిరస్కరించవచ్చు\n(RS can only make recommendations — LS may accept or reject)",
     "రాజ్యసభ మనీ బిల్లు ఆమోదించక తప్పదు",
     "c",
     "Art.109(2): రాజ్యసభ మనీ బిల్లుపై సిఫార్సులు (recommendations) మాత్రమే చేయగలదు. లోక్‌సభ వాటిని ఆమోదించవచ్చు లేదా తిరస్కరించవచ్చు. రాజ్యసభ ఏ నిర్ణయమూ తీసుకోకపోయినా 14 రోజుల తర్వాత ఆమోదించినట్లే.\n(Art.109(2): RS can only recommend amendments; LS may accept or reject. If RS takes no action in 14 days, deemed passed.)"),

    (0, 3,
     "ఒక బిల్లులో కొన్ని నిబంధనలు Art.110 కింద ఉండి, ఇతర నిబంధనలు మనీ బిల్లు కాదని ఉంటే — అది ఏమవుతుంది?\n(If a Bill has some Art.110 provisions and other non-money provisions, what is it?)",
     "అది మనీ బిల్లు అవుతుంది",
     "అది ఆర్థిక బిల్లు (Financial Bill Category A) — మనీ బిల్లు కాదు\n(Financial Bill Category A — NOT a Money Bill)",
     "అది ఆర్థిక బిల్లు (Financial Bill Category B)",
     "అది సాధారణ బిల్లు",
     "b",
     "ఫైనాన్షియల్ బిల్లు (Category A) — Art.117(1): Art.110లో పేర్కొన్న అంశాలు ఉంటే కానీ 'మాత్రమే' ఆ అంశాలు కాకుండా ఇతర నిబంధనలు కూడా ఉంటే — ఇది మనీ బిల్లు కాదు; ఆర్థిక బిల్లు (Category A). ఇది లోక్‌సభలోనే ప్రవేశపెట్టాలి, రాష్ట్రపతి అనుమతి కావాలి.\n(Financial Bill Category A under Art.117(1): Has Art.110 matters + other matters — NOT a Money Bill; must be introduced in LS only with President's recommendation.)"),

    (1, 2,
     "సెలెక్ట్ కమిటీ (Select Committee) మరియు జాయింట్ కమిటీ (Joint Committee) మధ్య తేడా ఏమిటి?\n(Difference between Select Committee and Joint Committee during Bill's committee stage?)",
     "రెండూ ఒకటే",
     "Select Committee ఒక్క సభ సభ్యులతో ఉంటుంది; Joint Committee రెండు సభల సభ్యులతో ఉంటుంది\n(Select = one House members; Joint = members of both Houses)",
     "Select Committee బిల్లు రద్దు చేయగలదు",
     "Joint Committee స్పీకర్ నేతృత్వంలో ఉంటుంది",
     "b",
     "Select Committee: ఒక సభ సభ్యులతో మాత్రమే ఏర్పడుతుంది. Joint Committee: రెండు సభల సభ్యులతో ఏర్పడుతుంది. రెండూ బిల్లు నిర్దిష్ట అంశాలు విచారిస్తాయి.\n(Select Committee = members of one House; Joint Committee = members of both Houses. Both examine the Bill clause by clause.)"),

    (1, 3,
     "పార్లమెంట్ ప్రొరోగేషన్ (Prorogation) అయినప్పుడు పెండింగ్ బిల్లులు ఏమవుతాయి?\n(What happens to pending Bills when Parliament is prorogued?)",
     "అన్నీ రద్దవుతాయి (Lapse) — రద్దు వలె",
     "రాజ్యసభ బిల్లులు రద్దవుతాయి, లోక్‌సభ బిల్లులు మిగిలి ఉంటాయి",
     "అన్నీ మిగిలి ఉంటాయి — సమావేశం ముగుస్తుంది కానీ బిల్లులు రద్దవు, తదుపరి సమావేశంలో కొనసాగుతాయి\n(All remain — prorogation ends session but bills do NOT lapse; they continue next session)",
     "రాష్ట్రపతి నిర్ణయిస్తారు",
     "c",
     "Prorogation (సమావేశం ముగింపు): సభ కూర్చునే సమావేశం ముగుస్తుంది కానీ లోక్‌సభ రద్దు కాదు. పెండింగ్ బిల్లులు రద్దవు కావు — తదుపరి సమావేశంలో కొనసాగుతాయి. రద్దు (Dissolution) అయితేనే లోక్‌సభ పెండింగ్ బిల్లులు రద్దవుతాయి.\n(On Prorogation: session ends but LS is not dissolved — pending bills do NOT lapse; they carry forward. On Dissolution: bills pending in LS lapse.)"),

    (2, 2,
     "పార్లమెంట్ సమావేశంలో 'ప్రశ్నోత్తర సమయం' లేని రోజులు ఏవి?\n(On which days is Question Hour not held in Parliament?)",
     "సోమవారాలు",
     "రాష్ట్రపతి ప్రసంగం ఉన్న రోజు మరియు బడ్జెట్ ప్రవేశపెట్టే రోజు\n(Day of President's Address and Budget Day — no QH)",
     "శుక్రవారాలు",
     "ఏ రోజూ లేని రోజు లేదు",
     "b",
     "రాష్ట్రపతి ఉభయ సభల సంయుక్త సమావేశంలో ప్రసంగించే రోజు మరియు కేంద్ర బడ్జెట్ ప్రవేశపెట్టే రోజు ప్రశ్నోత్తర సమయం ఉండదు.\n(No Question Hour on the day of President's Address to joint sitting and on the day of presentation of Union Budget.)"),

    (2, 3,
     "పార్లమెంట్‌లో 'స్పెషల్ మెన్షన్' (Special Mention) అంటే ఏమిటి?\n(What is 'Special Mention' in Parliament?)",
     "స్పీకర్ ప్రత్యేక అనుమతి",
     "రాజ్యసభలో ముఖ్యమైన అంశంపై నోటీసు లేకుండా సభ్యుడు మాట్లాడడం\n(RS member speaks on important matter without notice — RS equivalent of Zero Hour)",
     "లోక్‌సభ ప్రత్యేక తీర్మానం",
     "ప్రధానమంత్రి ప్రత్యేక ప్రసంగం",
     "b",
     "స్పెషల్ మెన్షన్ (Special Mention): రాజ్యసభలో జీరో అవర్‌కు సమానమైనది. రాజ్యసభ సభ్యుడు అత్యవసర జాతీయ అంశంపై చైర్మన్ అనుమతితో 3 నిమిషాల ప్రసంగం చేయగలరు.\n(Special Mention in RS is equivalent to Zero Hour in LS. An RS member can speak for 3 minutes on urgent national matters with Chairman's permission.)"),

    (3, 2,
     "అవిశ్వాస తీర్మానం (NCM) ఆమోదించిన తేదీ నుండి ఎన్ని రోజులలోపల చర్చ నిర్వహించాలి?\n(Within how many days of admission must No-Confidence Motion be debated?)",
     "7 రోజులు", "10 రోజులు",
     "15 రోజులు", "21 రోజులు",
     "b",
     "లోక్‌సభ నిబంధనావళి Rule 198 ప్రకారం: స్పీకర్ NCM నోటీసు అందుకున్న తేదీ నుండి 10 రోజులలోపు చర్చకు తేది నిర్ణయించాలి. ఈ 10 రోజులలో చర్చ జరిగి ఓటింగ్ పూర్తి అవుతుంది.\n(LS Rules Rule 198: Speaker must fix a date for debate within 10 days of receiving the NCM notice. Debate and vote conclude within this 10-day period.)"),

    (3, 3,
     "క్లోజర్ మోషన్ (Closure Motion) రకాలు ఏవి?\n(What are the types of Closure Motion in Parliament?)",
     "Simple Closure మాత్రమే",
     "Simple Closure, Kangaroo Closure, Guillotine Closure",
     "Simple Closure, Kangaroo Closure, Closure by Compartments, Guillotine",
     "రెండే రకాలు",
     "c",
     "క్లోజర్ మోషన్ రకాలు:\n1) Simple Closure: చర్చ ఆపమని అడగడం\n2) Closure by Compartments: అంశాలను గ్రూపులుగా విభజించి చర్చ ముగించడం\n3) Kangaroo Closure: కొన్ని అంశాలు దాటి ముఖ్యమైన వాటికి దూకడం\n4) Guillotine: బడ్జెట్‌లో చర్చించని డిమాండ్లన్నీ ఒకేసారి ఓటింగ్‌కు\n(Four types: Simple Closure, Closure by Compartments, Kangaroo Closure, Guillotine.)"),

    (4, 2,
     "సప్లిమెంటరీ డిమాండ్స్ (Supplementary Demands for Grants) ఏ అనుచ్ఛేదం కింద ఉంటాయి?\n(Supplementary Demands for Grants fall under which Article?)",
     "Art.112", "Art.113",
     "Art.115", "Art.116",
     "c",
     "Art.115: ఆర్థిక సంవత్సరంలో అనుమతించిన మొత్తం సరిపోకపోతే లేదా కొత్త సేవకు డబ్బు అవసరమైతే సప్లిమెంటరీ డిమాండ్స్ ప్రవేశపెడతారు.\n(Art.115: If the amount granted is insufficient or a need arises for a new service, Supplementary Demands for Grants are presented.)"),

    (4, 3,
     "భారత్‌లో బడ్జెట్ ఫిబ్రవరి 1న ఎప్పటి నుండి ప్రవేశపెట్టడం ప్రారంభించారు?\n(From which year did India start presenting Budget on February 1?)",
     "2015–16 నుండి", "2016–17 నుండి",
     "2017–18 నుండి", "2000–01 నుండి",
     "c",
     "2017–18 నుండి (అరుణ్ జైట్లీ హయాంలో) బడ్జెట్ ఫిబ్రవరి 28 బదులు ఫిబ్రవరి 1న ప్రవేశపెట్టడం ప్రారంభించారు. Railway Budget విలీనం కూడా 2017లో జరిగింది.\n(From 2017-18 budget, India shifted budget presentation from February 28 to February 1 under Finance Minister Arun Jaitley. Railway Budget was also merged.)"),

    (5, 3,
     "సార్వజనిక లెక్కల కమిటీ (PAC) ఎప్పుడు స్థాపించబడింది?\n(When was the Public Accounts Committee established in India?)",
     "1947లో స్వాతంత్ర్యం తర్వాత",
     "1921లో — మాంటేగ్యూ-చెమ్స్‌ఫర్డ్ సంస్కరణల (1919) ఫలితంగా\n(In 1921 — following Montagu-Chelmsford Reforms of 1919)",
     "1950లో రాజ్యాంగం అమలులోకి వచ్చిన తర్వాత",
     "1952లో మొదటి సార్వత్రిక ఎన్నికల తర్వాత",
     "b",
     "PAC 1921లో మాంటేగ్యూ-చెమ్స్‌ఫర్డ్ సంస్కరణల (Government of India Act 1919) ఫలితంగా స్థాపించబడింది — భారతదేశంలో అత్యంత పాతదైన పార్లమెంటరీ కమిటీ.\n(PAC was established in 1921 as a result of Montagu-Chelmsford Reforms (Government of India Act 1919) — the oldest Parliamentary Committee in India.)"),

    (6, 3,
     "రాజ్యాంగ సవరణలో 'Doctrine of Implied Limitations' అంటే ఏమిటి?\n(What is 'Doctrine of Implied Limitations' in constitutional amendments?)",
     "అన్ని అంశాలను సవరించవచ్చు",
     "రాజ్యాంగంలో కొన్ని ప్రాథమిక విషయాలు సవరణకు అతీతమని — కేశవానంద భారతి కేసు నిర్ణయం\n(Some basic features are beyond amendment — Kesavananda Bharati case 1973)",
     "వ్యాఖ్యానించే అధికారం కేవలం రాష్ట్రపతికి ఉంది",
     "పార్లమెంట్ అన్ని అంశాలను సవరించగలదు",
     "b",
     "కేశవానంద భారతి కేసు (1973): పార్లమెంట్ రాజ్యాంగం యొక్క 'Basic Structure' సవరించలేదు. ఇది Implied Limitation — రాజ్యాంగంలో ఎక్కడా పేర్కొనబడలేదు కానీ న్యాయవ్యవస్థ నిర్ణయించింది.\n(Kesavananda Bharati 1973: Parliament cannot amend the 'Basic Structure' of the Constitution — an implied limitation not explicitly stated in the Constitution.)"),

    (7, 3,
     "పార్లమెంటరీ విధానాల్లో 'Whip' అంటే ఏమిటి?\n(What is a 'Whip' in Parliamentary procedures?)",
     "స్పీకర్ అదుపు సాధనం",
     "పార్టీ సభ్యులకు ఓటింగ్ ఆదేశాలు ఇచ్చే అధికారి / ఆదేశ పత్రం\n(Officer/written directive instructing party members how to vote)",
     "అవిశ్వాస తీర్మానం",
     "బిల్లు ఆమోదం నోటీసు",
     "b",
     "విప్ (Whip): పార్టీ నేత జారీ చేసే ఓటింగ్ ఆదేశ పత్రం. Three-Line Whip అత్యంత కఠినమైనది — విప్ ఉల్లంఘిస్తే 10వ షెడ్యూల్ కింద అనర్హత వర్తించవచ్చు.\n(Whip: A written directive by a party leader for members' voting. Three-Line Whip is most stringent — violation may attract disqualification under 10th Schedule.)"),

    (7, 4,
     "లోక్‌సభ 'రద్దు' (Dissolution) తర్వాత పెండింగ్‌లో ఉన్న బిల్లుల పరిస్థితి ఏమిటి?\n(What happens to pending Bills after dissolution of Lok Sabha?)",
     "అన్నీ మిగిలి ఉంటాయి",
     "రాజ్యసభలో పెండింగ్ అయినవి మాత్రమే మిగిలి ఉంటాయి",
     "లోక్‌సభలో ఉన్న అన్ని బిల్లులు రద్దవుతాయి (Lapse); రాజ్యసభలో పెండింగ్ ఉన్న బిల్లులు రద్దవుతాయి; రెండు సభలూ ఆమోదించి రాష్ట్రపతి వద్ద ఉన్న బిల్లులు మిగిలి ఉంటాయి\n(LS bills lapse; RS pending bills lapse; bills with President remain)",
     "రాష్ట్రపతి నిర్ణయం",
     "c",
     "లోక్‌సభ రద్దు (Dissolution) అయినప్పుడు:\n✗ లోక్‌సభలో ఏ దశలో ఉన్న బిల్లులైనా రద్దవుతాయి\n✗ రాజ్యసభలో పెండింగ్ ఉన్న బిల్లులు రద్దవుతాయి\n✓ రెండు సభలూ ఆమోదించి రాష్ట్రపతి ఆమోదం కోసం పెండింగ్ ఉన్న బిల్లులు మిగిలి ఉంటాయి\n(On LS dissolution: all bills in LS lapse; RS pending bills also lapse; only bills passed by both Houses pending President's assent remain.)"),

    (7, 3,
     "పార్లమెంట్ 'ప్రివిలేజులు' (Privileges) ఎక్కడ పేర్కొన్నారు?\n(Where are Parliamentary Privileges mentioned in the Constitution?)",
     "Art.79", "Art.100",
     "Art.105 (LS) మరియు Art.194 (రాష్ట్ర శాసనసభ)",
     "Art.110",
     "c",
     "Art.105: లోక్‌సభ మరియు దాని సభ్యుల హక్కులు (Privileges). Art.194: రాష్ట్ర శాసనసభ సభ్యుల హక్కులు. ముఖ్యమైనది: సభలో మాట్లాడిన దానికి కోర్టులో విచారణ ఉండదు.\n(Art.105: Powers and privileges of Parliament and its members. Art.194: State legislature privileges. Key privilege: Freedom of speech in Parliament — no court proceedings.)"),

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
