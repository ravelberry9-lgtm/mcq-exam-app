# seed_polity_ch16.py
# Chapter 16 – Vice President of India
# (భారత ఉపరాష్ట్రపతి)
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total Sections: 8 | Total MCQs: 45 | PYQs: 5
# Difficulty: 1=Easy  2=Moderate  3=Tough  4=Toughest
# ─────────────────────────────────────────────────────

import json as _json

POLITY_CH16_SECTIONS = [
    {
        "title": "16.1 ఉపరాష్ట్రపతి — ఎన్నిక మరియు అర్హతలు",
        "sub": "Art.63–66 · Electoral College (Both Houses MPs incl. Nominated) · STV · Qualifications",
        "audio": ""
    },
    {
        "title": "16.2 పదవీ కాలం మరియు తొలగింపు",
        "sub": "Art.67 · 5 Years · Resignation to President · RS Effective Majority + LS Simple Majority · 14 Days Notice",
        "audio": ""
    },
    {
        "title": "16.3 రాజ్యసభ చైర్మన్ పాత్ర",
        "sub": "Art.64 · Ex-officio Chairman · Casting Vote · Not RS Member · Joint Sitting · Art.89",
        "audio": ""
    },
    {
        "title": "16.4 తాత్కాలిక రాష్ట్రపతి బాధ్యతలు",
        "sub": "Art.65 · Acting President · Vacancy · Absence · Salary Continues as Chairman · CJI if Both Vacant",
        "audio": ""
    },
    {
        "title": "16.5 వేతనం, ప్రమాణం మరియు హక్కులు",
        "sub": "Art.69 · Oath by President · Salary as RS Chairman · Official Residence · Perks",
        "audio": ""
    },
    {
        "title": "16.6 రాష్ట్రపతి vs ఉపరాష్ట్రపతి — పోలిక",
        "sub": "Electoral College · Qualifications · Resignation · Removal · Oath · Salary · Differences",
        "audio": ""
    },
    {
        "title": "16.7 ముఖ్యమైన ఉపరాష్ట్రపతులు",
        "sub": "Radhakrishnan · Zakir Husain · V.V. Giri · B.D. Jatti · M. Hidayatullah · Hamid Ansari · Dhankhar",
        "audio": ""
    },
    {
        "title": "16.8 కఠిన ప్రశ్నలు — APPSC/UPSC PYQs",
        "sub": "Electoral College Details · Removal Procedure · Comparison Questions · PYQ Analysis",
        "audio": ""
    },
]

POLITY_CH16_MCQS = [

    # ── Section 0: Election & Qualifications ─────────────────────────────────
    (0, 1,
     "భారత ఉపరాష్ట్రపతి పదవికి సంబంధించిన అనుచ్ఛేదం ఏది?\n(Which Article establishes the office of Vice President of India?)",
     "Art.52", "Art.63",
     "Art.66", "Art.69",
     "b",
     "Art.63: భారతదేశానికి ఒక ఉపరాష్ట్రపతి ఉంటారు (There shall be a Vice President of India). Art.66: VP ఎన్నిక విధానం. Art.69: VP ప్రమాణం.\n(Art.63 establishes the office. Art.66 deals with election method. Art.69 with oath.)"),

    (0, 1,
     "ఉపరాష్ట్రపతి ఎన్నికలో పాల్గొనే ఎలక్టోరల్ కాలేజ్ సభ్యులు ఎవరు?\n(Who forms the Electoral College for Vice Presidential election?)",
     "పార్లమెంట్ ఉభయ సభల ఎన్నికైన సభ్యులు + రాష్ట్రాల MLAs\n(Elected MPs of both Houses + State MLAs)",
     "పార్లమెంట్ ఉభయ సభల ఎన్నికైన సభ్యులు మాత్రమే\n(Only elected MPs of both Houses)",
     "పార్లమెంట్ ఉభయ సభల సభ్యులు — ఎన్నికైన మరియు నామినేట్ చేయబడిన వారు\n(Members of both Houses — elected AND nominated)",
     "రాజ్యసభ సభ్యులు మాత్రమే\n(Only Rajya Sabha members)",
     "c",
     "Art.66(1): ఉపరాష్ట్రపతి ఎన్నిక — పార్లమెంట్ ఉభయ సభల (లోక్‌సభ + రాజ్యసభ) ఎన్నికైన మరియు నామినేట్ చేయబడిన సభ్యులందరూ పాల్గొంటారు. రాష్ట్ర MLAs పాల్గొనరు — ఇది రాష్ట్రపతి ఎన్నికకు ముఖ్యమైన తేడా.\n(Art.66(1): All members of both Houses of Parliament — elected AND nominated — vote. State MLAs do NOT participate. Key difference from Presidential election.)"),

    (0, 2,
     "ఉపరాష్ట్రపతి ఎన్నికకు రాష్ట్ర శాసనసభ సభ్యులు (MLAs) పాల్గొంటారా?\n(Do State Legislative Assembly members (MLAs) participate in VP election?)",
     "అవును, అన్ని రాష్ట్రాల MLAs పాల్గొంటారు",
     "అవును, కానీ కేవలం 28 రాష్ట్రాల MLAs మాత్రమే",
     "కాదు, MLAs ఉపరాష్ట్రపతి ఎన్నికలో పాల్గొనరు\n(No, MLAs do NOT participate in VP election)",
     "అవును, ఢిల్లీ మరియు పుదుచ్చేరి MLAs మాత్రమే",
     "c",
     "ఉపరాష్ట్రపతి ఎన్నికకు రాష్ట్ర MLAs పాల్గొనరు — ఇది రాష్ట్రపతి ఎన్నికకు ముఖ్యమైన తేడా. రాష్ట్రపతి ఎన్నికలో రాష్ట్రాల MLAs పాల్గొంటారు; ఉపరాష్ట్రపతి ఎన్నికలో పార్లమెంట్ సభ్యులు (ఎన్నికైన + నామినేట్) మాత్రమే.\n(State MLAs do NOT vote in VP election. This is the KEY difference: President election = MPs + MLAs (elected only); VP election = MPs (both elected AND nominated), NO MLAs.)"),

    (0, 1,
     "ఉపరాష్ట్రపతి ఎన్నికలో నామినేట్ చేయబడిన పార్లమెంట్ సభ్యులు పాల్గొంటారా?\n(Do nominated members of Parliament vote in VP election?)",
     "కాదు, నామినేటెడ్ సభ్యులు పాల్గొనరు",
     "అవును, నామినేటెడ్ సభ్యులు పాల్గొంటారు\n(Yes, nominated members DO participate)",
     "కేవలం రాజ్యసభ నామినేటెడ్ సభ్యులు మాత్రమే",
     "కేవలం లోక్‌సభ నామినేటెడ్ సభ్యులు",
     "b",
     "ఉపరాష్ట్రపతి ఎన్నికలో పార్లమెంట్ ఉభయ సభల నామినేటెడ్ సభ్యులు పాల్గొంటారు — ఇది రాష్ట్రపతి ఎన్నికకు వ్యత్యాసం (రాష్ట్రపతి ఎన్నికలో నామినేటెడ్ మినహాయించారు).\n(In VP election, nominated members of both Houses DO participate — unlike Presidential election where nominated members are EXCLUDED.)"),

    (0, 1,
     "ఉపరాష్ట్రపతి పదవికి అర్హతలు ఏవి? (Art.66(3))\n(What are the qualifications for VP under Art.66(3)?)",
     "భారత పౌరుడు, 35 సంవత్సరాలు, లోక్‌సభ సభ్యత్వానికి అర్హుడు\n(Indian citizen, 35 yrs, eligible for LS membership)",
     "భారత పౌరుడు, 30 సంవత్సరాలు, రాజ్యసభ సభ్యత్వానికి అర్హుడు",
     "భారత పౌరుడు, 35 సంవత్సరాలు, రాజ్యసభ సభ్యత్వానికి అర్హుడు, లాభదాయక పదవి లేనివాడు\n(Indian citizen, 35 yrs, eligible for RS membership, holds no office of profit)",
     "భారత పౌరుడు, 25 సంవత్సరాలు, రాజ్యసభ సభ్యత్వానికి అర్హుడు",
     "c",
     "Art.66(3): ఉపరాష్ట్రపతి అర్హతలు — (1) భారత పౌరుడు, (2) 35 సంవత్సరాలు పూర్తి, (3) రాజ్యసభ సభ్యత్వానికి అర్హుడు (లోక్‌సభ కాదు — ఇది రాష్ట్రపతి అర్హత నుండి తేడా), (4) లాభదాయక పదవి లేనివాడు.\n(Art.66(3): Qualifications — Indian citizen, 35 years, eligible for RS membership (NOT LS — key difference from President), holds no office of profit.)"),

    (0, 2,
     "ఉపరాష్ట్రపతి అర్హతలో రాష్ట్రపతి అర్హత నుండి ముఖ్యమైన తేడా ఏమిటి?\n(What is the key qualification difference between VP and President?)",
     "ఉపరాష్ట్రపతికి 30 సంవత్సరాలు; రాష్ట్రపతికి 35 సంవత్సరాలు",
     "ఉపరాష్ట్రపతి రాజ్యసభ సభ్యత్వానికి అర్హుడై ఉండాలి; రాష్ట్రపతి లోక్‌సభకు అర్హుడై ఉండాలి\n(VP: eligible for RS; President: eligible for LS)",
     "ఉపరాష్ట్రపతికి 40 సంవత్సరాలు కావాలి",
     "ఉపరాష్ట్రపతి పార్లమెంట్ సభ్యుడై ఉండాలి",
     "b",
     "ముఖ్యమైన తేడా: రాష్ట్రపతి అర్హత = లోక్‌సభ సభ్యత్వానికి అర్హుడు (Art.58); ఉపరాష్ట్రపతి అర్హత = రాజ్యసభ సభ్యత్వానికి అర్హుడు (Art.66(3)). వయసు రెండింటికీ 35 సంవత్సరాలే.\n(Key difference: President must be eligible for LS membership (Art.58); VP must be eligible for RS membership (Art.66(3)). Age is same — 35 years for both.)"),

    (0, 1,
     "ఉపరాష్ట్రపతి ఎన్నికలో ఉపయోగించే పద్ధతి ఏది?\n(What electoral method is used for VP election?)",
     "ప్రత్యక్ష ఎన్నిక (Direct election by citizens)",
     "సాధారణ మెజారిటీ — FPTP",
     "నిష్పత్తి ప్రాతినిధ్యం — ఒకే బదిలీయోగ్య ఓటు (STV) — రహస్య బ్యాలెట్\n(Proportional Representation — Single Transferable Vote — Secret Ballot)",
     "పార్లమెంట్‌లో చేతులు ఎత్తడం",
     "c",
     "Art.66(1): ఉపరాష్ట్రపతి ఎన్నిక — నిష్పత్తి ప్రాతినిధ్యం — ఒకే బదిలీయోగ్య ఓటు (STV) పద్ధతిలో, రహస్య బ్యాలెట్ ద్వారా. రాష్ట్రపతి ఎన్నికకు అదే పద్ధతి.\n(Art.66(1): VP election uses Proportional Representation with Single Transferable Vote (STV) by secret ballot — same as Presidential election method.)"),

    (0, 2,
     "ఉపరాష్ట్రపతి నామినేషన్‌కు ఎంత మంది ప్రతిపాదకులు మరియు అనుమోదకులు అవసరం?\n(How many proposers and seconders are required for VP nomination?)",
     "25 ప్రతిపాదకులు + 25 అనుమోదకులు + ₹10,000 డిపాజిట్",
     "50 ప్రతిపాదకులు + 50 అనుమోదకులు + ₹15,000 డిపాజిట్",
     "20 ప్రతిపాదకులు + 20 అనుమోదకులు + ₹15,000 డిపాజిట్\n(20 proposers + 20 seconders + ₹15,000 deposit)",
     "100 ప్రతిపాదకులు + 100 అనుమోదకులు",
     "c",
     "VP ఎన్నికలో నామినేషన్‌కు 20 ప్రతిపాదకులు + 20 అనుమోదకులు (ఎలక్టోరల్ కాలేజ్ సభ్యులు అయిన MPs) + ₹15,000 సెక్యూరిటీ డిపాజిట్ అవసరం. రాష్ట్రపతి ఎన్నికలో 50+50 అవసరం.\n(VP nomination requires 20 proposers + 20 seconders (from Electoral College i.e. MPs) + ₹15,000 security deposit. Compare: Presidential election needs 50+50.)"),

    (0, 3,
     "ఉపరాష్ట్రపతి ఎన్నికలో వివాదాల విచారణ ఎవరు చేస్తారు?\n(Who adjudicates disputes regarding VP election?)",
     "రాష్ట్రపతి",
     "హైకోర్టు",
     "సుప్రీం కోర్టు (Supreme Court)\n(Art.71 — Same as Presidential election disputes)",
     "ఎన్నికల కమిషన్",
     "c",
     "Art.71: రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి ఎన్నికలకు సంబంధించిన వివాదాలు సుప్రీం కోర్టు విచారిస్తుంది.\n(Art.71: Disputes relating to election of President AND Vice President are decided by the Supreme Court.)"),

    (0, 2,
     "ఉపరాష్ట్రపతి ఎన్నికకు Election Commission నిర్వహించే పాత్ర ఏమిటి?\n(What role does the Election Commission play in VP election?)",
     "ఉపరాష్ట్రపతి ఎన్నికలో Election Commission పాత్ర లేదు",
     "Election Commission ఎన్నిక నిర్వహిస్తుంది మరియు తేదీ నిర్ణయిస్తుంది\n(Election Commission conducts the election and fixes the date)",
     "రాష్ట్రపతి నేరుగా ఎన్నికను నిర్వహిస్తారు",
     "లోక్‌సభ స్పీకర్ నిర్వహిస్తారు",
     "b",
     "ఉపరాష్ట్రపతి ఎన్నికను భారత ఎన్నికల కమిషన్ (Election Commission of India) నిర్వహిస్తుంది — రాష్ట్రపతి ఎన్నికకు మాదిరిగానే.\n(The Election Commission of India conducts the VP election — same as for Presidential election.)"),

    # ── Section 1: Term & Removal ─────────────────────────────────────────────
    (1, 1,
     "ఉపరాష్ట్రపతి పదవీ కాలం ఎంత?\n(What is the term of office of the Vice President?)",
     "4 సంవత్సరాలు", "5 సంవత్సరాలు",
     "6 సంవత్సరాలు", "పార్లమెంట్ నిర్ణయిస్తుంది",
     "b",
     "Art.67(a): ఉపరాష్ట్రపతి పదవీ కాలం 5 సంవత్సరాలు — పదవి స్వీకరించిన తేదీ నుండి. పునర్ ఎన్నికకు అర్హుడు.\n(Art.67(a): VP holds office for 5 years from the date of entering office. Eligible for re-election.)"),

    (1, 1,
     "ఉపరాష్ట్రపతి రాజీనామా ఎవరికి ఇవ్వాలి?\n(To whom does the VP submit resignation?)",
     "లోక్‌సభ స్పీకర్‌కు",
     "రాజ్యసభ చైర్మన్‌కు",
     "రాష్ట్రపతికి\n(To the President — Art.67(a))",
     "ప్రధానమంత్రికి",
     "c",
     "Art.67(a): ఉపరాష్ట్రపతి పదవి నుండి తప్పుకోవాలంటే రాష్ట్రపతికి స్వహస్తంతో లిఖిత రాజీనామా ఇవ్వాలి. (రాష్ట్రపతి రాజీనామా ఉపరాష్ట్రపతికి ఇస్తారు — ఇది వ్యత్యాసం.)\n(Art.67(a): VP resigns by writing to the President. Compare: President resigns to the VP.)"),

    (1, 2,
     "ఉపరాష్ట్రపతి తొలగింపు విధానం ఏమిటి?\n(What is the procedure for removal of the Vice President?)",
     "రాజ్యాంగ సవరణ ద్వారా మాత్రమే",
     "రాజ్యసభలో ప్రత్యేక మెజారిటీ తీర్మానం + లోక్‌సభ ఆమోదం\n(RS special majority resolution + LS agreement)",
     "రాజ్యసభ సమర్థ మెజారిటీ (Effective Majority) తీర్మానం + 14 రోజుల నోటీసు + లోక్‌సభ సాధారణ మెజారిటీ ఆమోదం\n(RS Effective Majority + 14 days notice + LS Simple Majority agreement)",
     "రెండు సభలలో 2/3 మెజారిటీ తీర్మానం",
     "c",
     "Art.67(b): ఉపరాష్ట్రపతి తొలగింపు — (1) రాజ్యసభ సమర్థ మెజారిటీ (Effective Majority = RS మొత్తం సభ్యత్వంలో సగానికి పైగా) తీర్మానం, (2) 14 రోజుల ముందు నోటీసు, (3) లోక్‌సభ సాధారణ మెజారిటీతో ఆమోదం.\n(Art.67(b): Removal — RS passes resolution by Effective Majority (majority of total RS membership) with 14 days notice; LS agrees by Simple Majority.)"),

    (1, 2,
     "ఉపరాష్ట్రపతి తొలగింపు తీర్మానానికి ముందు ఎంత రోజుల నోటీసు ఇవ్వాలి?\n(How many days' notice is required before a resolution for VP removal?)",
     "7 రోజులు", "10 రోజులు",
     "14 రోజులు\n(14 days advance notice required — Art.67(b))",
     "30 రోజులు",
     "c",
     "Art.67(b): ఉపరాష్ట్రపతి తొలగింపు తీర్మానం ప్రవేశపెట్టే ముందు ఉపరాష్ట్రపతికి కనీసం 14 రోజుల ముందు నోటీసు ఇవ్వాలి.\n(Art.67(b): At least 14 days' advance notice must be given before moving a resolution for VP's removal.)"),

    (1, 3,
     "ఉపరాష్ట్రపతి తొలగింపుకు రాజ్యసభలో ఏ మెజారిటీ అవసరం?\n(What majority is required in RS for VP removal?)",
     "హాజరైన వారిలో 2/3 మెజారిటీ (2/3 of present and voting)",
     "మొత్తం RS సభ్యత్వంలో 2/3 మెజారిటీ",
     "సమర్థ మెజారిటీ — RS మొత్తం సభ్యత్వంలో సగానికి పైగా (Effective Majority — majority of total RS membership)",
     "మొత్తం పార్లమెంట్ సభ్యత్వంలో 2/3",
     "c",
     "Art.67(b): ఉపరాష్ట్రపతి తొలగింపు తీర్మానం రాజ్యసభ 'సమర్థ మెజారిటీ' (Effective Majority) తో ఆమోదించాలి — అంటే RS మొత్తం సభ్యత్వంలో సగానికి పైగా. అనంతరం లోక్‌సభ సాధారణ మెజారిటీతో అంగీకరిస్తుంది.\n(Art.67(b): RS passes resolution by Effective Majority = majority of TOTAL RS membership. Then LS agrees by Simple Majority (majority of present and voting).)"),

    (1, 3,
     "రాష్ట్రపతి Impeachment మరియు ఉపరాష్ట్రపతి తొలగింపు మధ్య ముఖ్యమైన తేడా ఏమిటి?\n(Key difference between Presidential Impeachment and VP Removal?)",
     "రెండింటిలోనూ 2/3 మెజారిటీ కావాలి",
     "రాష్ట్రపతి Impeachment కి 1/4 నోటీసు + రెండు సభలలో 2/3; ఉపరాష్ట్రపతి తొలగింపుకు నిర్దిష్ట కారణం అవసరం లేదు — రాజ్యసభ Effective Majority మాత్రమే\n(President: 1/4 notice + 2/3 in both Houses for violation of Constitution; VP: no specific ground + RS Effective Majority + LS agreement)",
     "రెండింటిలోనూ రాజ్యసభలో మాత్రమే నిర్ణయం",
     "ఉపరాష్ట్రపతి తొలగింపుకు న్యాయసభ అవసరం",
     "b",
     "రాష్ట్రపతి Impeachment: రాజ్యాంగ ఉల్లంఘన (specified ground), 1/4 నోటీసు, రెండు సభలలో 2/3 (total membership). ఉపరాష్ట్రపతి తొలగింపు: నిర్దిష్ట కారణం అవసరం లేదు, 14 రోజుల నోటీసు, RS Effective Majority + LS Simple Majority మాత్రమే.\n(President Impeachment: requires violation of Constitution; 1/4 notice + 2/3 total membership in BOTH houses. VP Removal: NO specific ground needed; 14 days notice; RS Effective Majority + LS Simple Majority.)"),

    # ── Section 2: RS Chairman Role ──────────────────────────────────────────
    (2, 1,
     "ఉపరాష్ట్రపతి రాజ్యసభ చైర్మన్ పాత్ర ఏ అనుచ్ఛేదం ప్రకారం?\n(Under which Article is VP the ex-officio Chairman of RS?)",
     "Art.63", "Art.64",
     "Art.65", "Art.89",
     "b",
     "Art.64: ఉపరాష్ట్రపతి రాజ్యసభ పదవీపూర్వక (ex-officio) చైర్మన్. Art.89(1): రాజ్యసభ చైర్మన్ = ఉపరాష్ట్రపతి అని నిర్ధారిస్తుంది.\n(Art.64: VP is ex-officio Chairman of Rajya Sabha. Art.89(1) also confirms this. Art.65 = Acting President. Art.63 = Office of VP.)"),

    (2, 1,
     "ఉపరాష్ట్రపతి రాజ్యసభ సభ్యుడా?\n(Is the VP a member of Rajya Sabha?)",
     "అవును, RS సభ్యుడు",
     "కాదు, VP రాజ్యసభ సభ్యుడు కాదు — కేవలం చైర్మన్ మాత్రమే\n(No, VP is NOT a member of RS — only its Chairman)",
     "అవును, నామినేటెడ్ సభ్యుడిగా",
     "VP అవసరమైనప్పుడు మాత్రమే సభ్యుడవుతారు",
     "b",
     "ఉపరాష్ట్రపతి రాజ్యసభకు చైర్మన్ అయినప్పటికీ, RS సభ్యుడు కాదు. అందువల్ల సాధారణ ఓటింగ్‌లో పాల్గొనలేరు — కేవలం Tie అయినప్పుడు Casting Vote వేయగలరు.\n(The VP, though Chairman of RS, is NOT a member of RS. Therefore, does not vote in normal proceedings — only has the Casting Vote in case of a tie.)"),

    (2, 2,
     "ఉపరాష్ట్రపతి/రాజ్యసభ చైర్మన్ ఎప్పుడు ఓటు వేయగలరు?\n(When can the VP/RS Chairman cast a vote?)",
     "ప్రతి ఓటింగ్‌లో",
     "RS సభ్యత్వం ఉన్నప్పుడు మాత్రమే",
     "Tie (సమ ఓట్లు) అయినప్పుడు మాత్రమే Casting Vote వేయగలరు\n(Only in case of a tie — Casting Vote)",
     "ముఖ్యమైన బిల్లులపై మాత్రమే",
     "c",
     "రాజ్యసభ చైర్మన్ (VP) సాధారణ ఓటింగ్‌లో పాల్గొనలేరు — ఎందుకంటే RS సభ్యుడు కాదు. కేవలం ఓట్లు Tie అయినప్పుడు మాత్రమే Casting Vote వేయగలరు.\n(RS Chairman/VP does not vote in ordinary proceedings as not a RS member. Can only cast a Casting Vote in case of a tie — to resolve the deadlock.)"),

    (2, 2,
     "సంయుక్త సమావేశం (Joint Sitting) లో ఉపరాష్ట్రపతి అధ్యక్షత వహిస్తారా?\n(Does the VP preside over a Joint Sitting of Parliament?)",
     "అవును, VP రాజ్యసభ చైర్మన్ కాబట్టి అధ్యక్షత వహిస్తారు",
     "కాదు, Joint Sitting లో లోక్‌సభ స్పీకర్ అధ్యక్షత వహిస్తారు\n(No, Speaker of Lok Sabha presides over Joint Sitting — Art.118)",
     "రాష్ట్రపతి నిర్ణయిస్తారు",
     "VP మరియు Speaker ఇద్దరూ మారు మారు అధ్యక్షత వహిస్తారు",
     "b",
     "Art.118: సంయుక్త సమావేశం (Joint Sitting) లో లోక్‌సభ స్పీకర్ అధ్యక్షత వహిస్తారు — ఉపరాష్ట్రపతి కాదు. ఎందుకంటే Joint Sitting = పార్లమెంట్ ఉభయ సభల సమావేశం; Speaker = Lower House అధిపతి.\n(Art.118: Speaker of Lok Sabha presides over Joint Sitting — NOT the VP/RS Chairman. Because Joint Sitting is of both Houses together and the Speaker of the Lower House presides.)"),

    (2, 2,
     "ఉపరాష్ట్రపతి మనీ బిల్లు (Money Bill) విషయంలో ఏ అధికారం కలిగి ఉంటారు?\n(What power does the VP have with regard to Money Bills?)",
     "మనీ బిల్లు నిర్ణయిస్తారు",
     "మనీ బిల్లు RS లో ప్రవేశపెట్టవచ్చు",
     "మనీ బిల్లు విషయంలో VP కి ప్రత్యేక అధికారం లేదు — Money Bill నిర్ణయం LS స్పీకర్ చేస్తారు\n(VP has no special power over Money Bills — Speaker of LS certifies Money Bills)",
     "మనీ బిల్లుపై VP Veto వేయగలరు",
     "c",
     "మనీ బిల్లు విషయంలో ఉపరాష్ట్రపతికి ప్రత్యేక అధికారం లేదు. మనీ బిల్లు అని నిర్ణయించే అధికారం (Certification) లోక్‌సభ స్పీకర్‌కు చెందుతుంది (Art.110) — తుది నిర్ణయం స్పీకర్‌ది.\n(VP has no special power over Money Bills. Certification of Money Bill is done by LS Speaker (Art.110) whose decision is final.)"),

    (2, 3,
     "ఉపరాష్ట్రపతి తొలగింపు తీర్మానం pending లో ఉన్నప్పుడు రాజ్యసభ అధ్యక్షత వహించగలరా?\n(Can VP preside over RS when a removal resolution against them is pending?)",
     "అవును, ఎల్లప్పుడూ అధ్యక్షత వహించగలరు",
     "కాదు, తీర్మానం pending లో ఉన్నప్పుడు VP సభలో కూర్చోలేరు",
     "అవును, కానీ Casting Vote వేయలేరు; తొలగింపు తీర్మానంపై ఓటు వేయలేరు\n(Yes, can preside but cannot preside during the debate on removal resolution itself)",
     "అవును, కానీ సభ్యులు పాల్గొనలేరు",
     "c",
     "ఉపరాష్ట్రపతి తొలగింపు తీర్మానం pending లో ఉన్నప్పుడు — సాధారణ అధ్యక్షత వహించగలరు, కానీ ఆ తొలగింపు తీర్మానంపై జరిగే చర్చను స్వయంగా నిర్వహించలేరు. LS స్పీకర్ తో పోలిస్తే అదే విధానం.\n(VP can continue to preside over RS when a removal resolution is pending — but cannot preside over debates specifically on that removal motion.)"),

    (2, 2,
     "Anti-Defection Law (10వ షెడ్యూల్) కింద RS సభ్యుల అనర్హత నిర్ణయం ఎవరు చేస్తారు?\n(Who decides disqualification of RS members under Anti-Defection Law?)",
     "లోక్‌సభ స్పీకర్",
     "రాజ్యసభ చైర్మన్ (ఉపరాష్ట్రపతి)\n(Chairman of Rajya Sabha — the VP)",
     "రాష్ట్రపతి",
     "సుప్రీం కోర్టు",
     "b",
     "10వ షెడ్యూల్: లోక్‌సభ సభ్యుల Anti-Defection నిర్ణయం = LS Speaker; రాజ్యసభ సభ్యుల Anti-Defection నిర్ణయం = RS Chairman (ఉపరాష్ట్రపతి). Kihoto Hollohan Case (1992): ఈ నిర్ణయం న్యాయసమీక్షకు లోబడి ఉంటుంది.\n(10th Schedule: LS members' disqualification → LS Speaker; RS members' disqualification → RS Chairman (VP). Kihoto Hollohan (1992): Judicial review is available.)"),

    # ── Section 3: Acting President ──────────────────────────────────────────
    (3, 1,
     "ఏ అనుచ్ఛేదం ప్రకారం ఉపరాష్ట్రపతి తాత్కాలిక రాష్ట్రపతిగా వ్యవహరిస్తారు?\n(Under which Article does VP act as President?)",
     "Art.63", "Art.64",
     "Art.65", "Art.67",
     "c",
     "Art.65: రాష్ట్రపతి పదవి ఖాళీ అయినప్పుడు (మరణం, రాజీనామా, తొలగింపు) లేదా రాష్ట్రపతి అనారోగ్యం/గైర్హాజరు వల్ల విధులు నిర్వర్తించలేనప్పుడు — ఉపరాష్ట్రపతి తాత్కాలిక రాష్ట్రపతిగా వ్యవహరిస్తారు.\n(Art.65: VP acts as President when the Presidential office is vacant (death/resignation/removal) or President is unable to discharge duties due to illness/absence.)"),

    (3, 2,
     "ఉపరాష్ట్రపతి తాత్కాలిక రాష్ట్రపతిగా వ్యవహరించే సమయంలో వేతనం ఏమిటి?\n(What salary does VP receive while acting as President?)",
     "ఉపరాష్ట్రపతిగా వేతనం అందుకుంటారు",
     "రాష్ట్రపతి వేతనం అందుకుంటారు\n(Receives President's salary/emoluments while acting)",
     "రెండూ కలిపి అందుకుంటారు",
     "ఆ కాలంలో ఎటువంటి వేతనం అందుకోరు",
     "b",
     "ఉపరాష్ట్రపతి తాత్కాలిక రాష్ట్రపతిగా వ్యవహరించే సమయంలో రాష్ట్రపతి వేతనం మరియు సౌకర్యాలు అందుకుంటారు. రాష్ట్రపతి భవన్‌లో నివసిస్తారు.\n(While acting as President, VP receives the President's salary and emoluments — not the VP/RS Chairman salary. Also entitled to use Rashtrapati Bhavan.)"),

    (3, 2,
     "రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి రెండు పదవులూ ఖాళీ అయినప్పుడు ఎవరు తాత్కాలిక రాష్ట్రపతిగా వ్యవహరిస్తారు?\n(Who acts as President when both President and VP offices are vacant?)",
     "లోక్‌సభ స్పీకర్",
     "రాజ్యసభ డిప్యూటీ చైర్మన్",
     "సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి (Chief Justice of India)\n(Chief Justice of India acts as President)",
     "ప్రధానమంత్రి",
     "c",
     "Art.65 read with Art.70: రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి రెండు పదవులూ ఖాళీ అయినప్పుడు, సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి (CJI) తాత్కాలిక రాష్ట్రపతిగా వ్యవహరిస్తారు.\n(When BOTH President and VP offices are vacant, the Chief Justice of India acts as President.)"),

    (3, 3,
     "ఫక్రుద్దీన్ అలీ అహ్మద్ (President) 1977లో మరణించినప్పుడు తాత్కాలిక రాష్ట్రపతిగా ఎవరు వ్యవహరించారు?\n(Who acted as President when President Fakhruddin Ali Ahmed died in 1977?)",
     "V.V. గిరి", "N. సంజీవ రెడ్డి",
     "B.D. జట్టీ (B.D. Jatti — VP at that time)",
     "మొరార్జీ దేశాయ్",
     "c",
     "ఫక్రుద్దీన్ అలీ అహ్మద్ 1977 ఫిబ్రవరిలో పదవిలో ఉండగా మరణించారు. ఆ సమయంలో ఉపరాష్ట్రపతిగా ఉన్న B.D. జట్టీ (Basappa Danappa Jatti) తాత్కాలిక రాష్ట్రపతిగా వ్యవహరించారు.\n(When President Fakhruddin Ali Ahmed died in office (Feb 1977), the then VP B.D. Jatti acted as President until N. Sanjiva Reddy was elected as the new President.)"),

    (3, 3,
     "V.V. గిరి ఉపరాష్ట్రపతి పదవికి రాజీనామా ఎందుకు చేశారు?\n(Why did V.V. Giri resign as VP?)",
     "ఆరోగ్య కారణాల వల్ల",
     "1969 రాష్ట్రపతి ఎన్నికలో స్వతంత్ర అభ్యర్థిగా పాల్గొనడానికి\n(To contest the 1969 Presidential election as an independent candidate)",
     "ప్రధానమంత్రితో విభేదాల వల్ల",
     "పార్టీ ఆదేశం మేరకు",
     "b",
     "V.V. గిరి 1969 రాష్ట్రపతి ఎన్నికలో స్వతంత్ర అభ్యర్థిగా పాల్గొనడానికి ఉపరాష్ట్రపతి పదవికి రాజీనామా చేశారు. STV రెండవ ప్రాధాన్యతా ఓట్ల ద్వారా రాష్ట్రపతిగా ఎన్నికైయ్యారు.\n(V.V. Giri resigned as VP in 1969 to contest the Presidential election as an independent candidate. He won through second preference votes under STV — demonstrating the STV mechanism.)"),

    # ── Section 4: Salary, Oath & Conditions ────────────────────────────────
    (4, 1,
     "ఉపరాష్ట్రపతి ప్రమాణం ఎవరి సమక్షంలో జరుగుతుంది?\n(In whose presence does the VP take the oath of office?)",
     "సుప్రీం కోర్టు ప్రధాన న్యాయమూర్తి (CJI)",
     "రాష్ట్రపతి\n(The President — Art.69)",
     "లోక్‌సభ స్పీకర్",
     "రాజ్యసభ డిప్యూటీ చైర్మన్",
     "b",
     "Art.69: ఉపరాష్ట్రపతి ప్రమాణం రాష్ట్రపతి సమక్షంలో లేదా రాష్ట్రపతి నిర్దేశించిన వ్యక్తి సమక్షంలో చేస్తారు. (రాష్ట్రపతి ప్రమాణం CJI సమక్షంలో చేస్తారు — ఇది వ్యత్యాసం.)\n(Art.69: VP takes oath before the President or person appointed by the President. Compare: President's oath is before the CJI.)"),

    (4, 2,
     "ఉపరాష్ట్రపతి వేతనం ఏ రూపంలో అందుకుంటారు?\n(In what capacity does the VP receive salary?)",
     "ఉపరాష్ట్రపతి హోదాలో ప్రత్యేక వేతనం",
     "రాజ్యసభ చైర్మన్ హోదాలో వేతనం\n(Salary as Chairman of Rajya Sabha — not a separate VP salary)",
     "రాష్ట్రపతి వేతనంలో సగం",
     "పార్లమెంట్ నిర్ణయించిన ప్రత్యేక వేతనం",
     "b",
     "ఉపరాష్ట్రపతికి ప్రత్యేక వేతనం లేదు — రాజ్యసభ చైర్మన్ హోదాలో వేతనం మరియు సౌకర్యాలు పొందుతారు. ఇది రాష్ట్రపతి వేతనానికి భిన్నం (రాష్ట్రపతి వేతనం పార్లమెంట్ నిర్ణయిస్తుంది).\n(VP has no separate salary as VP — receives salary and perks as Chairman of Rajya Sabha. This is different from President whose salary is determined by Parliament.)"),

    (4, 1,
     "ఉపరాష్ట్రపతి అధికారిక నివాసం ఏది?\n(What is the official residence of the VP?)",
     "రాష్ట్రపతి భవన్", "ప్రధానమంత్రి నివాసం",
     "6, మౌలానా ఆజాద్ రోడ్, న్యూఢిల్లీ\n(6, Maulana Azad Road, New Delhi)",
     "10, జనపథ్",
     "c",
     "ఉపరాష్ట్రపతి అధికారిక నివాసం న్యూఢిల్లీలోని 6, మౌలానా ఆజాద్ రోడ్ (6, Maulana Azad Road). తాత్కాలిక రాష్ట్రపతిగా వ్యవహరించే సమయంలో రాష్ట్రపతి భవన్‌లో ఉంటారు.\n(VP's official residence is 6, Maulana Azad Road, New Delhi. When acting as President, VP resides at Rashtrapati Bhavan.)"),

    (4, 3,
     "ఉపరాష్ట్రపతి పదవిలో ఉన్నప్పుడు పార్లమెంట్ ఉభయ సభలలో వాదించగలరా?\n(Can the VP address both Houses of Parliament?)",
     "కేవలం రాజ్యసభలో మాత్రమే మాట్లాడగలరు",
     "కేవలం లోక్‌సభలో మాట్లాడగలరు",
     "ఉభయ సభలలో మాట్లాడగలరు, కానీ ఓటు వేయలేరు\n(Can address both Houses but cannot vote — not a member of either House)",
     "ఎటువంటి అధికారంలేదు",
     "c",
     "ఉపరాష్ట్రపతి రాజ్యాంగ పదవి ద్వారా పార్లమెంట్ ఉభయ సభలలోనూ మాట్లాడగలరు — కానీ ఏ సభలోనూ ఓటు వేయలేరు (ఏ సభకూ సభ్యుడు కాదు).\n(VP can address both Houses of Parliament but cannot vote in either — as VP is not a member of either House.)"),

    # ── Section 5: President vs VP Comparison ───────────────────────────────
    (5, 2,
     "రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి ఎన్నికల మధ్య ఎలక్టోరల్ కాలేజ్ తేడా ఏమిటి?\n(What is the Electoral College difference between Presidential and VP elections?)",
     "రెండింటికీ అదే ఎలక్టోరల్ కాలేజ్",
     "రాష్ట్రపతి: MPs (elected) + MLAs (elected); ఉపరాష్ట్రపతి: MPs (elected + nominated) మాత్రమే — MLAs పాల్గొనరు\n(President: Elected MPs + Elected MLAs; VP: All MPs (elected + nominated) only — NO MLAs)",
     "ఉపరాష్ట్రపతి ఎన్నికలో MLAs మాత్రమే పాల్గొంటారు",
     "రెండింటికీ MPs మరియు MLAs పాల్గొంటారు",
     "b",
     "రాష్ట్రపతి ఎలక్టోరల్ కాలేజ్: పార్లమెంట్ ఉభయ సభల ఎన్నికైన సభ్యులు + రాష్ట్రాల విధానసభల ఎన్నికైన సభ్యులు + ఢిల్లీ/పుదుచ్చేరి MLAs. ఉపరాష్ట్రపతి ఎలక్టోరల్ కాలేజ్: పార్లమెంట్ ఉభయ సభల ఎన్నికైన మరియు నామినేటెడ్ సభ్యులు — రాష్ట్ర MLAs పాల్గొనరు.\n(President: Elected MPs + Elected MLAs. VP: ALL MPs (elected + nominated) — NO state MLAs. This is THE KEY DIFFERENCE.)"),

    (5, 2,
     "రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి ఇద్దరికీ ఉమ్మడిగా ఉన్న అర్హత ఏమిటి?\n(What qualification is COMMON to both President and VP?)",
     "లోక్‌సభ సభ్యత్వానికి అర్హత",
     "రాజ్యసభ సభ్యత్వానికి అర్హత",
     "35 సంవత్సరాల వయసు, భారత పౌరుడు, లాభదాయక పదవి లేనివాడు\n(35 years of age, Indian citizen, no office of profit — common to both)",
     "30 సంవత్సరాల వయసు",
     "c",
     "రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి ఇద్దరికీ: భారత పౌరుడు, 35 సంవత్సరాలు, లాభదాయక పదవి లేనివాడు. తేడా: రాష్ట్రపతి = LS అర్హత; ఉపరాష్ట్రపతి = RS అర్హత.\n(Common: Indian citizen, 35 years, no office of profit. Difference: President must be eligible for LS; VP must be eligible for RS.)"),

    (5, 3,
     "రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి రెండు పదవుల మధ్య ప్రమాణం విషయంలో తేడా ఏమిటి?\n(How does the oath differ between President and VP?)",
     "రెండూ CJI సమక్షంలో జరుగుతాయి",
     "రాష్ట్రపతి ప్రమాణం CJI సమక్షంలో (Art.60); ఉపరాష్ట్రపతి ప్రమాణం రాష్ట్రపతి సమక్షంలో (Art.69)\n(President: Oath before CJI; VP: Oath before President)",
     "రెండూ రాష్ట్రపతి సమక్షంలో జరుగుతాయి",
     "రెండూ లోక్‌సభ స్పీకర్ సమక్షంలో",
     "b",
     "Art.60: రాష్ట్రపతి ప్రమాణం — CJI లేదా SC సీనియర్ న్యాయమూర్తి సమక్షంలో. Art.69: ఉపరాష్ట్రపతి ప్రమాణం — రాష్ట్రపతి సమక్షంలో.\n(Art.60: President's oath is before CJI. Art.69: VP's oath is before the President. This is a frequently asked comparison.)"),

    (5, 2,
     "రాష్ట్రపతి తొలగింపుకు (Impeachment) మరియు ఉపరాష్ట్రపతి తొలగింపుకు ఉమ్మడిగా ఉన్న నిబంధన ఏమిటి?\n(What is common between Presidential Impeachment and VP Removal procedures?)",
     "రెండింటికీ 2/3 మెజారిటీ",
     "రెండింటికీ 1/4 నోటీసు అవసరం",
     "రెండింటికీ 14 రోజుల ముందు నోటీసు అవసరం\n(Both require 14 days advance notice)",
     "రెండింటికీ రాజ్యాంగ ఉల్లంఘన అవసరం",
     "c",
     "రాష్ట్రపతి Impeachment (Art.61) మరియు ఉపరాష్ట్రపతి తొలగింపు (Art.67(b)) రెండింటికీ 14 రోజుల ముందు నోటీసు అవసరం. తేడా: Impeachment కి 1/4 మంది నోటీసు + రాజ్యాంగ ఉల్లంఘన అవసరం; VP తొలగింపుకు నిర్దిష్ట కారణం అవసరం లేదు.\n(Common: Both require 14 days' advance notice. Difference: President Impeachment needs 1/4 notice + constitutional violation ground; VP removal has no specific ground requirement.)"),

    # ── Section 6: Notable VPs ───────────────────────────────────────────────
    (6, 1,
     "భారతదేశపు మొదటి ఉపరాష్ట్రపతి ఎవరు?\n(Who was the first Vice President of India?)",
     "జాకీర్ హుసేన్", "V.V. గిరి",
     "డా. సర్వేపల్లి రాధాకృష్ణన్\n(Dr. Sarvepalli Radhakrishnan — 1952–1962)",
     "B.D. జట్టీ",
     "c",
     "డా. సర్వేపల్లి రాధాకృష్ణన్ 1952–1962 వరకు రెండు పదవీ కాలాలు భారతదేశపు మొదటి ఉపరాష్ట్రపతిగా పనిచేశారు. తర్వాత 1962–1967 వరకు రాష్ట్రపతిగా పనిచేశారు.\n(Dr. S. Radhakrishnan was the first VP of India (1952–1962) — served two terms. Subsequently served as President (1962–1967).)"),

    (6, 2,
     "ఉపరాష్ట్రపతి పదవి నుండి రాష్ట్రపతి పదవికి వెళ్ళిన వ్యక్తులు ఎవరు?\n(Which VPs later became Presidents of India?)",
     "V.V. గిరి మరియు జాకీర్ హుసేన్ మాత్రమే",
     "రాధాకృష్ణన్, జాకీర్ హుసేన్, V.V. గిరి, R. వెంకటరామన్, K.R. నారాయణన్\n(Radhakrishnan, Zakir Husain, V.V. Giri, R. Venkataraman, K.R. Narayanan)",
     "హమీద్ అన్సారీ మరియు M. వెంకయ్య నాయుడు",
     "ఒక్కరు మాత్రమే — జాకీర్ హుసేన్",
     "b",
     "VP నుండి President అయిన వారు: (1) రాధాకృష్ణన్ (2nd Pres.), (2) జాకీర్ హుసేన్ (3rd Pres.), (3) V.V. గిరి (4th Pres.), (4) R. వెంకటరామన్ (8th Pres.), (5) K.R. నారాయణన్ (10th Pres.).\n(VPs who became Presidents: Radhakrishnan, Zakir Husain, V.V. Giri, R. Venkataraman, K.R. Narayanan.)"),

    (6, 2,
     "అత్యంత ఎక్కువ కాలం ఉపరాష్ట్రపతిగా పనిచేసిన వ్యక్తి ఎవరు?\n(Who served as VP for the longest period?)",
     "డా. రాధాకృష్ణన్ (2 పదవీ కాలాలు)",
     "హమీద్ అన్సారీ — 2 పదవీ కాలాలు (2007–2017)\n(Hamid Ansari — 2 terms, 2007–2017)",
     "M. వెంకయ్య నాయుడు",
     "కృష్ణ కాంత్",
     "b",
     "హమీద్ అన్సారీ 2007–2017 వరకు రెండు పదవీ కాలాలు (10 సంవత్సరాలు) ఉపరాష్ట్రపతిగా పనిచేశారు — భారతదేశంలో అత్యంత ఎక్కువ కాలం. డా. రాధాకృష్ణన్ కూడా రెండు పదవీ కాలాలు పనిచేశారు.\n(Hamid Ansari served two terms (2007–2017) = 10 years as VP — longest continuous tenure. Dr. Radhakrishnan also served two terms but Ansari's combined tenure is longest.)"),

    (6, 3,
     "M. హిదాయతుల్లా ఉపరాష్ట్రపతి అవ్వడానికి ముందు ఏ పదవిలో ఉన్నారు?\n(What position did M. Hidayatullah hold before becoming VP?)",
     "ప్రధాన న్యాయమూర్తి (CJI) మరియు అనంతరం Acting President\n(Chief Justice of India and subsequently Acting President)",
     "లోక్‌సభ స్పీకర్",
     "ప్రధానమంత్రి",
     "రాష్ట్ర గవర్నర్",
     "a",
     "M. హిదాయతుల్లా (1979–1984 VP): CJI (1968–70) గా పనిచేసిన తర్వాత VP అయ్యారు. CJI గా 1969లో V.V. గిరి రాజీనామా తర్వాత రెండుసార్లు Acting President గా వ్యవహరించారు — ఉపరాష్ట్రపతిగా 1982లో మళ్లీ Acting President గా వ్యవహరించారు.\n(M. Hidayatullah was CJI (1968–70) before becoming VP (1979–84). He acted as President twice — once as CJI and once as VP. Famous for being both CJI and VP.)"),

    # ── Section 7: Hard PYQs ─────────────────────────────────────────────────
    (7, 3,
     "ఉపరాష్ట్రపతి ఎన్నికలో ఒక పార్లమెంట్ సభ్యుడు లోక్‌సభలో ఓటు వేసినప్పుడు ఎంత ఓటు విలువ ఉంటుంది?\n(What is the vote value of an MP in VP election?)",
     "MLAs ఓటు విలువకు సమానం",
     "ఒక్కొక్క MP ఓటు విలువ 1 మాత్రమే\n(Each MP's vote value is 1 only)",
     "రాష్ట్రానికి జనాభా ఆధారంగా నిర్ణయిస్తారు",
     "MP సీనియారిటీ ఆధారంగా నిర్ణయిస్తారు",
     "b",
     "ఉపరాష్ట్రపతి ఎన్నికలో ప్రతి MP ఓటు విలువ 1 మాత్రమే — రాష్ట్రపతి ఎన్నికలో మాదిరిగా రాష్ట్ర జనాభా ఆధారంగా వేరే విలువ ఉండదు. ఎందుకంటే VP ఎన్నికలో MLAs పాల్గొనరు, కేవలం MPs మాత్రమే ఓటు వేస్తారు.\n(In VP election, each MP's vote value = 1. Unlike Presidential election where vote values differ based on state population, in VP election all MPs have equal vote value of 1 since no MLAs participate.)"),

    (7, 3,
     "ఉపరాష్ట్రపతి తొలగింపు తీర్మానం ఏ సభలో ప్రవేశపెట్టాలి?\n(In which House must a VP removal resolution be introduced?)",
     "లోక్‌సభలో మాత్రమే",
     "రాజ్యసభలో మాత్రమే\n(Only in Rajya Sabha — Art.67(b))",
     "ఏ సభలోనైనా",
     "రెండు సభలలో ఏకకాలంలో",
     "b",
     "Art.67(b): ఉపరాష్ట్రపతి తొలగింపు తీర్మానం రాజ్యసభలో మాత్రమే ప్రవేశపెట్టాలి (RS = VP చైర్మన్ పాత్ర వహించే సభ). లోక్‌సభ తర్వాత సాధారణ మెజారిటీతో అంగీకరిస్తుంది మాత్రమే. రాష్ట్రపతి Impeachment మాత్రం ఏ సభలోనైనా ప్రవేశపెట్టవచ్చు.\n(Art.67(b): VP removal resolution must be introduced in Rajya Sabha ONLY (since VP chairs RS). LS then agrees by Simple Majority. Compare: Presidential Impeachment can be introduced in EITHER House.)"),

    (7, 4,
     "ఉపరాష్ట్రపతి పదవి ఖాళీ అయినప్పుడు తక్షణ ఎన్నిక నిర్వహించాలా?\n(Must a VP election be held immediately when the office falls vacant?)",
     "అవును, 30 రోజులలోపు ఎన్నిక జరగాలి",
     "అవును, 6 నెలలలోపు ఎన్నిక జరగాలి",
     "కాదు, రాజ్యాంగంలో VP ఖాళీని పూరించే కాల పరిమితి లేదు; కానీ రాష్ట్రపతి ఖాళీ అయినప్పుడు 6 నెలలు నిర్ణయించబడింది\n(No specific time limit for VP vacancy — unlike Presidential vacancy which has 6 months limit)",
     "అవును, 90 రోజులలోపు",
     "c",
     "రాజ్యాంగంలో ఉపరాష్ట్రపతి పదవి ఖాళీ అయినప్పుడు ఎంత కాలంలో ఎన్నిక నిర్వహించాలి అని నిర్దిష్టంగా చెప్పలేదు — రాష్ట్రపతి ఖాళీకి 6 నెలల పరిమితి ఉంది. ఇది రాజ్యాంగంలో ఖాళీగా ఉన్న అంశం.\n(No specific time limit is prescribed in the Constitution for filling VP vacancy — unlike the 6-month limit for filling Presidential vacancy. This is a constitutional lacuna.)"),

    (7, 3,
     "జాకీర్ హుసేన్ గురించి సరైన వాక్యం ఏది?\n(Which statement about Zakir Husain is correct?)",
     "మొదటి ఉపరాష్ట్రపతి",
     "ఉపరాష్ట్రపతి మరియు తర్వాత రాష్ట్రపతి అయ్యారు; రాష్ట్రపతిగా పదవిలో ఉండగా మరణించారు\n(Served as VP then as President; died while serving as President)",
     "రెండు పదవీ కాలాలు ఉపరాష్ట్రపతిగా పనిచేశారు",
     "మొదటి ముస్లిం ఉపరాష్ట్రపతి మాత్రమే",
     "b",
     "జాకీర్ హుసేన్: 1962–1967 VP (భారత 2వ VP); 1967–1969 భారత 3వ రాష్ట్రపతి. రాష్ట్రపతిగా పదవిలో ఉండగా 1969లో మరణించారు (ఫక్రుద్దీన్ అలీ అహ్మద్ కూడా రాష్ట్రపతిగా పదవిలో మరణించారు — రెండు అరుదైన సంఘటనలు).\n(Zakir Husain: VP 1962–67 (2nd VP); President 1967–69 (3rd President); died in office in 1969 while serving as President.)"),

    (7, 4,
     "ఉపరాష్ట్రపతి 'రాజ్యసభ సభ్యుల ప్రత్యక్ష ఎన్నిక' ద్వారా ఎన్నికవుతారని చెప్పడం సరైనదా?\n(Is it correct to say VP is elected by direct election of RS members only?)",
     "అవును, కేవలం RS సభ్యులు ఎన్నుకుంటారు",
     "కాదు — VP పార్లమెంట్ ఉభయ సభల (LS + RS) సభ్యులందరూ — ఎన్నికైన మరియు నామినేట్ — ఎన్నుకుంటారు; ప్రత్యక్ష ఎన్నిక కాదు\n(Incorrect — all MPs (both Houses, elected + nominated) elect VP; it is indirect election)",
     "అవును, LS + RS ఎన్నికైన సభ్యులు మాత్రమే",
     "అవును, ఒక్క నోటు వేయడం ద్వారా",
     "b",
     "VP ఎన్నిక: (1) ప్రత్యక్ష కాదు — MPs (ఎన్నికైన + నామినేట్) STV ద్వారా ఎన్నుకుంటారు; (2) RS మాత్రమే కాదు — LS + RS రెండూ; (3) MLAs పాల్గొనరు. ఇవి అన్నీ సాధారణ తప్పులు.\n(VP election: Indirect (not direct by citizens); by ALL MPs (elected + nominated) of BOTH Houses; MLAs do NOT participate; STV method with secret ballot.)"),

]


# ─────────────────────────────────────────────────────────────
def _seed_polity_ch16_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    """Insert Chapter 16 study note row (idempotent)."""
    existing = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=16"
    ).fetchone()
    if existing and not force:
        return

    sections_json = _json.dumps(POLITY_CH16_SECTIONS, ensure_ascii=False)
    ph = '%s' if use_postgres else '?'

    if existing and force:
        db_exec_fn(conn,
            f"UPDATE study_notes SET sections_json={ph}, chapter_title_en={ph}, chapter_title_te={ph} "
            f"WHERE topic='Indian_Polity' AND chapter_num=16",
            (sections_json,
             "Vice President of India",
             "భారత ఉపరాష్ట్రపతి")
        )
        return

    db_exec_fn(conn,
        f"""INSERT INTO study_notes
            (subject, topic, subtopic, chapter_num,
             chapter_title_te, chapter_title_en, pages_ref, sections_json)
            VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
        ('GK', 'Indian_Polity', 'Lakshmikanth', 16,
         'భారత ఉపరాష్ట్రపతి',
         'Vice President of India',
         'Ch.16',
         sections_json)
    )


def _seed_polity_ch16_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    """Insert Chapter 16 MCQs (skip if already present)."""
    note_row = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE topic='Indian_Polity' AND chapter_num=16"
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
    for row in POLITY_CH16_MCQS:
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
