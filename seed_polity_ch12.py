# seed_polity_ch12.py
# Chapter 12: Basic Structure of the Constitution (రాజ్యాంగ మూల నిర్మాణం)
# Total MCQs: 45 | PYQs: 10 | Format: Bilingual (Telugu + English)
# Sections:
#   0 = పూర్వ-కేశవానంద కేసులు / Pre-Kesavananda Cases (7 MCQs)
#   1 = కేశవానంద భారతి కేసు 1973 / Kesavananda Bharati Case 1973 (8 MCQs)
#   2 = మూల నిర్మాణ అంశాలు / Elements of Basic Structure (7 MCQs)
#   3 = కేశవానంద తర్వాత ముఖ్య కేసులు / Post-Kesavananda Landmark Cases (8 MCQs)
#   4 = 42వ సవరణ మరియు మూల నిర్మాణం / 42nd Amendment & Basic Structure (5 MCQs)
#   5 = వ్యాప్తి మరియు అనువర్తనం / Scope and Application (5 MCQs)
#   6 = కఠిన ప్రశ్నలు / Tough MCQs (5 MCQs)

import json as _json

POLITY_CH12_MCQS = [

    # ══════════════ SECTION 0: PRE-KESAVANANDA CASES (7 MCQs) ══════════════

    (0, "easy",
     "శంకరి ప్రసాద్ v. భారత యూనియన్ (1951) కేసులో సుప్రీం కోర్టు ఆర్టికల్ 13(2) గురించి ఏమి నిర్ణయించింది?\n(What did SC decide about Art 13(2) in Shankari Prasad v. Union of India (1951)?)",
     "రాజ్యాంగ సవరణలు కూడా Art 13(2) లోని 'చట్టం' (law) పరిధిలో వస్తాయి / Constitutional amendments also fall within 'law' under Art 13(2)",
     "రాజ్యాంగ సవరణలు Art 13(2) లోని 'చట్టం' పరిధిలో రావు — పార్లమెంటు FRs సవరించవచ్చు / Constitutional amendments do NOT fall under 'law' in Art 13(2) — Parliament can amend FRs",
     "ప్రాథమిక హక్కులు సవరించలేనివి / Fundamental Rights are non-amendable",
     "Art 13 రాజ్యాంగ సవరణలకు వర్తించదు అని స్పష్టంగా రాజ్యాంగంలో ఉంది / Constitution explicitly says Art 13 doesn't apply to amendments",
     "B",
     "శంకరి ప్రసాద్ 1951: SC నిర్ణయించింది — రాజ్యాంగ సవరణలు Art 13(2) లోని 'చట్టం' (law) పరిధిలో రావు. కాబట్టి పార్లమెంటు Art 368 ద్వారా ప్రాథమిక హక్కులతో సహా ఏ నిబంధనను అయినా సవరించవచ్చు.\nShankari Prasad 1951: SC held constitutional amendments do NOT fall within 'law' under Art 13(2). Hence Parliament can amend any provision including FRs via Art 368."),

    (0, "medium",
     "సజ్జన్ సింగ్ v. రాజస్థాన్ రాష్ట్రం (1964) కేసులో 'మూల నిర్మాణం' (basic structure) అనే పదబంధాన్ని మొదట ఎవరు వాడారు?\n(Who first used the phrase 'basic structure' in Sajjan Singh v. State of Rajasthan (1964)?)",
     "ప్రధాన న్యాయమూర్తి సుబ్బారావు / Chief Justice Subba Rao",
     "న్యాయమూర్తి హిదయతుల్లా / Justice Hidayatullah",
     "న్యాయమూర్తి ముధోల్కర్ (విభేదించే అభిప్రాయంలో) / Justice Mudholkar (in dissent)",
     "న్యాయమూర్తి వంచూ / Justice Wanchoo",
     "C",
     "సజ్జన్ సింగ్ కేసు 1964లో న్యాయమూర్తి ముధోల్కర్ విభేదించే అభిప్రాయంలో (dissent) మొదటిసారి 'ప్రాథమిక లక్షణాలు' (basic features/pattern) అనే పదాన్ని వాడారు — పార్లమెంటు రాజ్యాంగ మూల లక్షణాలను మార్చగలదా అని ప్రశ్నించారు.\nJustice Mudholkar in his dissent in Sajjan Singh 1964 first raised the question of whether Parliament can change the 'basic features/pattern' of the Constitution — a precursor to the Basic Structure doctrine."),

    (0, "medium",
     "గోలక్‌నాథ్ v. పంజాబ్ రాష్ట్రం (1967) కేసులో సుప్రీం కోర్టు ఏ సిద్ధాంతాన్ని వాడింది — అది ఏమిటి?\n(Which doctrine did the SC apply in Golaknath v. State of Punjab (1967) — and what does it mean?)",
     "పూర్వాన్వయ అమలు (Retrospective Overruling) — గత నిర్ణయాలు కూడా రద్దవుతాయి / Retrospective Overruling — past decisions also annulled",
     "భావి అమలు (Prospective Overruling) — కొత్త నిర్ణయం భవిష్యత్తుకే వర్తిస్తుంది, గతానికి కాదు / Prospective Overruling — new ruling applies only to future, not past",
     "న్యాయ సమీక్ష (Judicial Review) — సవరణ అసంవిధానిక / Judicial Review — amendment unconstitutional",
     "మూల నిర్మాణ పరీక్ష (Basic Structure Test) / Basic Structure Test",
     "B",
     "గోలక్‌నాథ్ 1967లో ప్రధాన న్యాయమూర్తి సుబ్బారావు 'భావి అమలు' (Prospective Overruling) సిద్ధాంతాన్ని వాడారు: శంకరి ప్రసాద్ 1951 మరియు సజ్జన్ సింగ్ 1964 నిర్ణయాలు రద్దు చేయబడ్డాయి, కానీ వాటి ఆధారంగా చేసిన సవరణలు చెల్లుబాటులో ఉంటాయి — కొత్త నిర్ణయం భవిష్యత్తు సవరణలకు మాత్రమే వర్తిస్తుంది.\nCJ Subba Rao in Golaknath 1967 applied 'Prospective Overruling': Shankari Prasad 1951 and Sajjan Singh 1964 overruled, but amendments already made remain valid — the new ruling applies only to future amendments.",
     "APPSC"),

    (0, "medium",
     "గోలక్‌నాథ్ కేసు (1967)లో ఏ సవరణ చట్టాలు సవాల్ చేయబడ్డాయి?\n(Which Amendment Acts were challenged in the Golaknath case (1967)?)",
     "24వ మరియు 25వ సవరణలు / 24th and 25th Amendments",
     "మొదటి, నాల్గవ మరియు 17వ సవరణలు (Land Reform Acts) / 1st, 4th and 17th Amendments (Land Reform Acts)",
     "42వ మరియు 44వ సవరణలు / 42nd and 44th Amendments",
     "7వ మరియు 13వ సవరణలు / 7th and 13th Amendments",
     "B",
     "గోలక్‌నాథ్ కేసు 1967లో 1వ సవరణ చట్టం 1951, 4వ సవరణ చట్టం 1955, మరియు 17వ సవరణ చట్టం 1964 సవాల్ చేయబడ్డాయి — ఇవి అన్నీ భూ సంస్కరణ చట్టాలను 9వ షెడ్యూల్‌లో చేర్చి న్యాయ సమీక్ష నుండి రక్షించడానికి చేసిన సవరణలు.\nIn Golaknath 1967, the 1st Amendment 1951, 4th Amendment 1955, and 17th Amendment 1964 were challenged — all enacted to add land reform laws to 9th Schedule to protect them from judicial review."),

    (0, "hard",
     "25వ సవరణ చట్టం 1971 ఆర్టికల్ 31C జోడించింది. అది ఏమి నిబంధన?\n(25th Amendment 1971 added Article 31C. What does it provide?)",
     "ఆస్తి హక్కు రద్దు చేస్తుంది / Abolishes Right to Property",
     "Art 39(b) మరియు (c) లోని DPSPs అమలు చేసే చట్టాలు Art 14, 19 ఉల్లంఘన కింద సవాల్ చేయలేవు / Laws giving effect to DPSPs under Art 39(b)(c) cannot be challenged as violating Art 14, 19",
     "Art 368 కింద ఏ సవరణను అయినా న్యాయస్థానాలు సమీక్షించలేవు / Courts cannot review any amendment under Art 368",
     "ప్రాథమిక హక్కులు అన్నీ DPSP ల కంటే తక్కువ అని ప్రకటిస్తుంది / Declares all FRs subordinate to all DPSPs",
     "B",
     "25వ సవరణ 1971లో Art 31C జోడించింది: Art 39(b) (పోషణాధికారాల ప్రజా యాజమాన్యం) మరియు Art 39(c) (ఆర్థిక శ్రేయస్సు) అమలు చేసే చట్టాలు Art 14, 19 ఉల్లంఘించినా సవాల్ చేయలేవు. 42వ సవరణ దీన్ని అన్ని DPSPలకు విస్తరించింది, కానీ మినర్వా మిల్స్ 1980 ఆ విస్తరణను రద్దు చేసింది.\n25th Amendment 1971 added Art 31C: Laws giving effect to Art 39(b)(c) cannot be challenged as violating Art 14/19. 42nd Amendment extended this to all DPSPs, but Minerva Mills 1980 struck down that extension."),

    (0, "medium",
     "24వ సవరణ చట్టం 1971 ఆర్టికల్ 13కు ఏమి జోడించింది?\n(What did the 24th Amendment 1971 add to Article 13?)",
     "Art 13(1) — రాజ్యాంగ సవరణలు కూడా 'చట్టాలు' పరిధిలో వస్తాయి / Art 13(1) — constitutional amendments also come within 'laws'",
     "Art 13(4) — ఈ ఆర్టికల్ పార్లమెంటు చేసే రాజ్యాంగ సవరణలకు వర్తించదు / Art 13(4) — this article shall not apply to any amendment of the Constitution by Parliament",
     "Art 13(3) — ప్రాథమిక హక్కుల నిర్వచనాన్ని పొడిగించింది / Art 13(3) — extended definition of Fundamental Rights",
     "Art 13 పూర్తిగా రద్దు చేయబడింది / Art 13 was completely repealed",
     "B",
     "24వ సవరణ 1971: Art 13కు క్లాజ్ (4) జోడించింది — 'ఈ ఆర్టికల్ Art 368 ద్వారా పార్లమెంటు చేసే రాజ్యాంగ సవరణలకు వర్తించదు.' ఇది Art 13(2) మరియు రాజ్యాంగ సవరణల మధ్య వివాదాన్ని శంకరి ప్రసాద్ నిర్ణయాన్ని రాజ్యాంగంలోనే స్పష్టం చేసింది.\n24th Amendment 1971: Added clause (4) to Art 13 — 'Nothing in this article shall apply to any amendment of this Constitution made under Art 368.' This codified the Shankari Prasad ruling and resolved the conflict between Art 13(2) and constitutional amendments."),

    (0, "hard",
     "24వ సవరణకు ముందు Art 368 శీర్షిక ఏమిటి? 24వ సవరణ తర్వాత ఏమి మారింది?\n(What was the heading of Art 368 before the 24th Amendment? What changed after?)",
     "ముందు: 'సవరణ విధానం'; తర్వాత: 'పార్లమెంటు సవరణ అధికారం మరియు విధానం' / Before: 'Procedure for Amendment'; After: 'Power of Parliament to amend the Constitution and procedure therefore'",
     "ముందు: 'రాజ్యాంగ సవరణ'; తర్వాత: 'ప్రాథమిక సవరణ' / Before: 'Constitutional Amendment'; After: 'Fundamental Amendment'",
     "ముందు: 'పార్లమెంటు సవరణ అధికారం'; తర్వాత: 'సవరణ విధానం' / Before: 'Parliament's amending power'; After: 'Amendment procedure'",
     "శీర్షికలో ఎటువంటి మార్పు రాలేదు / No change in heading",
     "A",
     "24వ సవరణ 1971 Art 368 శీర్షికను 'సవరణ విధానం' (Procedure for amendment) నుండి 'రాజ్యాంగాన్ని సవరించే పార్లమెంటు అధికారం మరియు విధానం' (Power of Parliament to amend the Constitution and procedure therefore) గా మార్చింది — పార్లమెంటు అధికారాన్ని స్పష్టంగా పేర్కొంది.\n24th Amendment 1971 changed the heading of Art 368 from 'Procedure for amendment' to 'Power of Parliament to amend the Constitution and procedure therefore' — explicitly asserting Parliament's power."),

    # ══════════════ SECTION 1: KESAVANANDA BHARATI CASE 1973 (8 MCQs) ══════════════

    (1, "easy",
     "కేశవానంద భారతి కేసు (1973) యొక్క పూర్తి పేరు ఏమిటి?\n(What is the full name of the Kesavananda Bharati case (1973)?)",
     "కేశవానంద భారతి v. తమిళనాడు రాష్ట్రం / Kesavananda Bharati v. State of Tamil Nadu",
     "కేశవానంద భారతి శ్రీపాదగళ్వారు v. కేరళ రాష్ట్రం / Kesavananda Bharati Sripadagalvaru v. State of Kerala",
     "కేశవానంద భారతి v. భారత యూనియన్ / Kesavananda Bharati v. Union of India",
     "కేశవానంద భారతి v. కర్ణాటక రాష్ట్రం / Kesavananda Bharati v. State of Karnataka",
     "B",
     "పూర్తి పేరు: కేశవానంద భారతి శ్రీపాదగళ్వారు v. కేరళ రాష్ట్రం (Kesavananda Bharati Sripadagalvaru v. State of Kerala). కేరళలో కాశ్మీర్ సన్యాసి ఆశ్రమం భూమి సంస్కరణ చట్టాల వల్ల ప్రభావితమయినందున ఈ కేసు దాఖలు చేయబడింది.\nFull name: Kesavananda Bharati Sripadagalvaru v. State of Kerala. Filed because land reforms in Kerala affected the Edneer Mutt monastery headed by Swami Kesavananda Bharati."),

    (1, "easy",
     "కేశవానంద భారతి కేసు (1973) లో న్యాయమూర్తుల ధర్మాసనం సభ్యుల సంఖ్య ఎంత?\n(How many judges were on the bench in Kesavananda Bharati case (1973)?)",
     "9 / Nine",
     "11 / Eleven",
     "13 / Thirteen",
     "7 / Seven",
     "C",
     "కేశవానంద భారతి కేసు 1973లో 13 న్యాయమూర్తుల రాజ్యాంగ ధర్మాసనం ఏర్పాటు చేయబడింది — ఇది అప్పటి వరకు అతిపెద్ద ధర్మాసనం. గోలక్‌నాథ్ 1967 (11 న్యాయమూర్తులు) తర్వాత ఇది మరింత పెద్ద బెంచ్.\nKesavananda Bharati 1973 had a 13-judge Constitutional Bench — the largest bench ever constituted at that time. Larger than Golaknath 1967 (11 judges).",
     "APPSC"),

    (1, "easy",
     "కేశవానంద భారతి కేసు తీర్పు తేదీ ఏమిటి?\n(What is the date of the Kesavananda Bharati judgment?)",
     "జనవరి 26, 1973 / January 26, 1973",
     "ఏప్రిల్ 24, 1973 / April 24, 1973",
     "అగస్టు 15, 1973 / August 15, 1973",
     "నవంబర్ 26, 1973 / November 26, 1973",
     "B",
     "కేశవానంద భారతి తీర్పు తేదీ: ఏప్రిల్ 24, 1973. ఈ తేదీ 9వ షెడ్యూల్ రక్షణ గురించి ప్రముఖమైన 'కట్-ఆఫ్ తేదీ'గా మారింది — వామన్ రావు 1981 మరియు IR కోహెలో 2007 కేసులలో ఇది నిర్ణయాత్మకమైంది.\nDate of Kesavananda Bharati judgment: April 24, 1973. This date became the famous 'cut-off date' for 9th Schedule protection — critical in Waman Rao 1981 and IR Coelho 2007.",
     "APPSC"),

    (1, "medium",
     "కేశవానంద భారతి కేసు (1973) లో సుప్రీం కోర్టు ప్రకటించిన మూల నిర్మాణ సిద్ధాంతం ఏమిటి?\n(What is the Basic Structure doctrine announced in Kesavananda Bharati (1973)?)",
     "పార్లమెంటు రాజ్యాంగంలో ఎటువంటి సవరణ చేయలేదు / Parliament cannot make any amendment to the Constitution",
     "పార్లమెంటు రాజ్యాంగ సవరణ చేయవచ్చు కానీ రాజ్యాంగ మూల నిర్మాణాన్ని నాశనం/పాడు చేయలేదు / Parliament can amend the Constitution but cannot destroy/abrogate the basic structure",
     "రాజ్యాంగ మూల నిర్మాణ సవరణ రాష్ట్రాల ఆమోదంతో మాత్రమే సాధ్యం / Basic structure amendment possible only with State ratification",
     "ప్రాథమిక హక్కులే మూల నిర్మాణం — వాటిని సవరించలేమ / Only FRs are basic structure — they cannot be amended",
     "B",
     "కేశవానంద భారతి 1973 తీర్పు: పార్లమెంటు Art 368 కింద రాజ్యాంగంలోని ఏ నిబంధనను అయినా సవరించవచ్చు — ప్రాథమిక హక్కులు సహా. కానీ రాజ్యాంగ 'మూల నిర్మాణాన్ని' (Basic Structure) నాశనం చేయలేదు/పాడుచేయలేదు/సంక్షిప్తం చేయలేదు.\nKesavananda Bharati 1973: Parliament under Art 368 can amend any provision including FRs. BUT it cannot destroy/abrogate/damage the 'Basic Structure' of the Constitution.",
     "APPSC"),

    (1, "hard",
     "కేశవానంద భారతి తీర్పు తర్వాత ఇందిరా గాంధీ ప్రభుత్వం ప్రధాన న్యాయమూర్తిగా ఎవరిని నియమించింది — దీనికి కారణం ఏమిటి?\n(Whom did Indira Gandhi's government appoint as Chief Justice after Kesavananda Bharati judgment — and why?)",
     "న్యాయమూర్తి హెచ్.ఆర్. ఖన్నాను — మెజారిటీ తీర్పు రాసినందుకు / Justice H.R. Khanna — for writing majority judgment",
     "న్యాయమూర్తి ఎ.ఎన్. రేని — మూల నిర్మాణ సిద్ధాంతానికి వ్యతిరేకంగా వాదించిన మైనారిటీలో భాగంగా ఉన్నందుకు / Justice A.N. Ray — as he was part of the minority holding Parliament's power is unlimited",
     "న్యాయమూర్తి వై.వి. చంద్రచూడ్‌ను — అత్యంత సీనియర్ అయినందుకు / Justice Y.V. Chandrachud — as most senior",
     "న్యాయమూర్తి జె.ఎం. షేలాట్‌ను — కేశవానంద కేసు విచారించినందుకు / Justice J.M. Shelat — for hearing Kesavananda case",
     "B",
     "కేశవానంద భారతి తీర్పు తర్వాత ఇందిరా గాంధీ ప్రభుత్వం న్యాయమూర్తి ఎ.ఎన్. రేని ప్రధాన న్యాయమూర్తిగా నియమించింది — ఆయన పార్లమెంటు సవరణ అధికారం అపరిమితమని వాదించిన మైనారిటీలో ఉన్నారు. ఈ నియామకం 3 సీనియర్ న్యాయమూర్తులను అతిక్రమించి చేయబడింది — న్యాయవ్యవస్థ స్వాతంత్ర్య వివాదానికి దారితీసింది.\nAfter Kesavananda Bharati, Indira Gandhi appointed Justice A.N. Ray as CJ — he was in minority holding Parliament's amendment power unlimited. This superseded 3 senior judges — triggering a major controversy about judicial independence."),

    (1, "hard",
     "కేశవానంద భారతి తీర్పు తర్వాత జారీ చేయబడిన '13 న్యాయమూర్తుల ప్రకటన' (Summary Statement) ఏమిటి?\n(What was the 'Summary Statement' issued after the Kesavananda Bharati judgment?)",
     "పార్లమెంటు సవరణ అధికారం సంపూర్ణమని 13 న్యాయమూర్తులు ఐకమత్యంగా ప్రకటించారు / All 13 judges unanimously declared Parliament's amendment power is absolute",
     "13 న్యాయమూర్తులలో 9 మంది మూల నిర్మాణ సిద్ధాంతం కేసు యొక్క నిర్ణయ కారణం (ratio decidendi) అని నిర్ధారించే ప్రకటనపై సంతకం చేశారు / 9 of 13 judges signed a statement confirming basic structure doctrine is the ratio decidendi of the case",
     "మూల నిర్మాణంలో 10 అంశాల జాబితా ప్రకటించబడింది — అన్ని న్యాయమూర్తులు అంగీకరించారు / A list of 10 elements of basic structure was announced — agreed by all judges",
     "కేసు పెద్ద ధర్మాసనానికి పంపాలని ప్రకటించారు / Announced case should be referred to larger bench",
     "B",
     "కేశవానంద భారతి తీర్పు తర్వాత 13 న్యాయమూర్తులలో 9 మంది ఒక ప్రత్యేక ప్రకటనపై సంతకం చేశారు: మూల నిర్మాణ సిద్ధాంతం ఈ కేసు యొక్క ratio decidendi (నిర్ణయ కారణం) అని స్పష్టం చేశారు — ఎందుకంటే తీర్పు విభిన్న అభిప్రాయాలతో సంక్లిష్టంగా ఉంది.\n9 of 13 judges signed a special summary statement after Kesavananda Bharati clarifying that the basic structure doctrine is the ratio decidendi of the case — because the judgment was complex with varying opinions."),

    (1, "medium",
     "కేశవానంద భారతి కేసు (1973) లో పార్లమెంటు సవరణ అధికారాన్ని అపరిమితంగా ప్రకటించిన మైనారిటీ (dissent) న్యాయమూర్తుల సంఖ్య ఎంత?\n(In Kesavananda Bharati (1973), how many judges were in the minority holding Parliament's amendment power unlimited?)",
     "4 / Four",
     "6 / Six",
     "5 / Five",
     "3 / Three",
     "B",
     "కేశవానంద భారతి 1973లో 7 న్యాయమూర్తులు మెజారిటీ (మూల నిర్మాణ సిద్ధాంతం అంగీకరించారు); 6 న్యాయమూర్తులు మైనారిటీ (పార్లమెంటు సవరణ అధికారం అపరిమితమని వాదించారు). మైనారిటీలో: న్యా. ఎ.ఎన్. రే, కె.కె. మాథ్యూ, ఎం.హెచ్. బేగ్, ఎస్.ఎన్. ద్వివేది, వై.వి. చంద్రచూడ్, దీవాన్ బి.పాల్.\nKesavananda Bharati 1973: 7 judges in majority (accepted basic structure doctrine); 6 in minority (held Parliament's amendment power is unlimited). Minority included: Ray, Matthew, Beg, Dwivedi, Chandrachud, Pal."),

    (1, "medium",
     "కేశవానంద భారతి కేసు తర్వాత ఎ.ఎన్. రే ప్రధాన న్యాయమూర్తిగా నియమితులైన తర్వాత ఏమి జరిగింది?\n(What happened after A.N. Ray was appointed Chief Justice after Kesavananda Bharati?)",
     "మూల నిర్మాణ సిద్ధాంతాన్ని రాజ్యాంగంలో చేర్చే ప్రయత్నం / Attempt to incorporate Basic Structure doctrine in Constitution",
     "కేశవానంద భారతి నిర్ణయాన్ని పునఃపరిశీలించడానికి 13-సభ్యుల ధర్మాసనం ఏర్పాటు ప్రయత్నం — కానీ అది విఫలమైంది / Attempt to constitute 13-judge bench to reconsider Kesavananda — but it failed",
     "మూల నిర్మాణ సిద్ధాంతాన్ని ఆమోదించే తీర్పు మరోసారి వచ్చింది / Another judgment affirming the Basic Structure doctrine came",
     "అత్యవసర పరిస్థితిలో మూల నిర్మాణం రద్దు చేయబడింది / Basic Structure was suspended during Emergency",
     "B",
     "ఎ.ఎన్. రే ప్రధాన న్యాయమూర్తిగా నియమితులైన తర్వాత కేశవానంద భారతి నిర్ణయాన్ని పునఃపరిశీలించడానికి ధర్మాసనం ఏర్పాటు చేయడానికి ప్రయత్నించారు. కానీ రెండు రోజులలో ఆ బెంచ్ రద్దయింది — న్యాయవ్యవస్థ స్వాతంత్ర్యంపై భారీ వివాదం నేపథ్యంలో.\nAfter A.N. Ray was appointed CJ, he attempted to constitute a bench to reconsider Kesavananda Bharati. But the bench was dissolved within two days — amid massive controversy over judicial independence."),

    # ══════════════ SECTION 2: ELEMENTS OF BASIC STRUCTURE (7 MCQs) ══════════════

    (2, "medium",
     "మూల నిర్మాణంలో ఏ అంశాలు చేర్చబడ్డాయి? కింది ఏ అంశం మూల నిర్మాణంలో ఉంది?\n(Which of the following is recognized as part of the Basic Structure?)",
     "ఆస్తి హక్కు (Art 300A) / Right to Property (Art 300A)",
     "న్యాయవ్యవస్థ స్వాతంత్ర్యం / Independence of Judiciary",
     "పార్లమెంటు సభ్యుల జీతాలు / Salaries of Members of Parliament",
     "రాష్ట్ర జాబితా అంశాలు / State List subjects",
     "B",
     "మూల నిర్మాణంలో: న్యాయవ్యవస్థ స్వాతంత్ర్యం ✓, రాజ్యాంగ ఆధిపత్యం ✓, లౌకిక స్వభావం ✓, సమాఖ్య స్వభావం ✓, ప్రజాస్వామ్య రూపం ✓, న్యాయ సమీక్ష ✓, స్వేచ్ఛా ఎన్నికలు ✓. ఆస్తి హక్కు (Art 300A) మూల నిర్మాణంలో భాగం కాదు — అది చట్టపరమైన హక్కు మాత్రమే.\nBasic Structure includes: Independence of Judiciary ✓, Constitutional Supremacy ✓, Secular character ✓, Federal character ✓, Democratic form ✓, Judicial Review ✓, Free & Fair Elections ✓. Right to Property (Art 300A) is NOT basic structure — it is only a legal/constitutional right."),

    (2, "medium",
     "మూల నిర్మాణంలో 'సమాఖ్య స్వభావం' (Federal character) అంటే ఏమిటి? ఏ కేసులో ఇది స్పష్టంగా చెప్పబడింది?\n(What is meant by 'Federal character' in Basic Structure? Which case clearly stated this?)",
     "రాష్ట్రాలు స్వతంత్రంగా రాజ్యాంగం రాసుకోవచ్చు / States can write their own Constitution",
     "కేంద్ర-రాష్ట్ర అధికారాల సమతుల్యత మూల నిర్మాణంలో భాగం — SR బొమ్మై కేసు 1994లో స్పష్టపరచబడింది / The balance of Centre-State powers is basic structure — clarified in SR Bommai 1994",
     "రాష్ట్రాల ఆమోదం లేకుండా ఏ చట్టం చేయలేమ / No law can be made without State consent",
     "7వ షెడ్యూల్ మార్చలేమ / 7th Schedule cannot be amended",
     "B",
     "SR బొమ్మై v. భారత యూనియన్ (1994): సమాఖ్య స్వభావం, లౌకికత, ప్రజాస్వామ్య రూపం — ఇవి మూల నిర్మాణంలో భాగమని ఈ కేసు స్పష్టంగా ప్రకటించింది. రాష్ట్రపతి పాలన విధించడంపై కఠినమైన నియంత్రణలు విధించింది.\nSR Bommai v. Union of India (1994): Clearly declared federal character, secularism, and democratic form are part of Basic Structure. Also imposed strict judicial scrutiny on imposition of President's Rule."),

    (2, "easy",
     "మూల నిర్మాణంలో 'న్యాయ సమీక్ష' (Judicial Review) చేర్చబడినందుకు అర్థం ఏమిటి?\n(What does including 'Judicial Review' in Basic Structure mean?)",
     "పార్లమెంటు న్యాయస్థానాల అధికారాలను పూర్తిగా తొలగించవచ్చు / Parliament can completely remove the power of courts",
     "రాజ్యాంగ సవరణ ద్వారా పార్లమెంటు న్యాయస్థానాల న్యాయ సమీక్ష అధికారాన్ని రద్దు చేయలేదు / Parliament cannot by constitutional amendment abolish the power of judicial review of courts",
     "కేవలం SC న్యాయ సమీక్ష అధికారం ఉంది; HC లేదు / Only SC has judicial review; not HCs",
     "న్యాయ సమీక్ష అమెరికా నుండి అరువు తెచ్చిన అంశం — మన రాజ్యాంగంలో స్పష్టంగా లేదు / Judicial review is borrowed from USA — not explicit in our Constitution",
     "B",
     "న్యాయ సమీక్ష మూల నిర్మాణంలో భాగమని అర్థం: రాజ్యాంగ సవరణ ద్వారా కూడా న్యాయస్థానాల న్యాయ సమీక్ష అధికారాన్ని రద్దు చేయలేమ. L. చంద్రకుమార్ కేసు 1997లో: ట్రిబ్యునల్‌ల నుండి SC/HC కు అప్పీల్ అధికారాన్ని తొలగించడం మూల నిర్మాణ ఉల్లంఘన అని తీర్పు వచ్చింది.\nJudicial Review in Basic Structure means: Parliament cannot even by constitutional amendment abolish courts' power of judicial review. L. Chandra Kumar 1997: Removing appellate jurisdiction from SC/HC against Tribunals violates Basic Structure."),

    (2, "medium",
     "మూల నిర్మాణంలో 'లౌకిక స్వభావం' (Secularism) చేర్చబడినందుకు ఏ కేసులో నిర్ధారించబడింది?\n(In which case was 'Secularism' confirmed as part of Basic Structure?)",
     "కేశవానంద భారతి 1973 / Kesavananda Bharati 1973",
     "SR బొమ్మై v. భారత యూనియన్ 1994 / SR Bommai v. Union of India 1994",
     "మినర్వా మిల్స్ 1980 / Minerva Mills 1980",
     "ఇందిరా గాంధీ v. రాజ్‌నారాయణ్ 1975 / Indira Gandhi v. Raj Narain 1975",
     "B",
     "SR బొమ్మై v. భారత యూనియన్ (1994): 9 న్యాయమూర్తుల ధర్మాసనం స్పష్టంగా నిర్ధారించింది — లౌకిక స్వభావం, సమాఖ్య స్వభావం, ప్రజాస్వామ్య రూపం మూల నిర్మాణంలో భాగం. మతాధారిత పార్టీ అధికారంలో ఉన్న రాష్ట్ర ప్రభుత్వాలను రద్దు చేయడం మూల నిర్మాణ ఉల్లంఘన కాదు అని కూడా పేర్కొంది.\nSR Bommai v. Union of India (1994): 9-judge bench clearly declared — secularism, federalism, democratic form are part of Basic Structure. Also stated that dismissing state governments that threaten secularism does not violate Basic Structure.",
     "APPSC"),

    (2, "hard",
     "మూల నిర్మాణంలో 'పార్లమెంటరీ ప్రజాస్వామ్య వ్యవస్థ' (Parliamentary Democracy) ఒక అంశం. దీని అర్థం ఏమిటి?\n(Parliamentary Democracy is an element of Basic Structure. What does this mean?)",
     "ఎన్నికలు తప్పనిసరిగా ప్రతి 5 సంవత్సరాలు జరగాలి — ఏ సవరణతోనూ మార్చలేమ / Elections must be held every 5 years — cannot be changed by any amendment",
     "రాజ్యాంగ సవరణ ద్వారా పార్లమెంటరీ వ్యవస్థను అధ్యక్ష వ్యవస్థగా మార్చలేమ; ప్రజాప్రాతినిధ్య ఎన్నికలు రద్దు చేయలేమ / Parliament cannot by amendment replace Parliamentary system with Presidential; representative elections cannot be abolished",
     "ప్రధానమంత్రి పదవి రద్దు చేయలేమ / Office of Prime Minister cannot be abolished",
     "రాజ్యసభ రద్దు చేయలేమ / Rajya Sabha cannot be abolished",
     "B",
     "పార్లమెంటరీ ప్రజాస్వామ్యం మూల నిర్మాణంలో భాగమని అర్థం: (1) ప్రజల ఓటు ద్వారా ప్రభుత్వం; (2) పాలక మండలి పార్లమెంటుకు జవాబుదారీ; (3) రాజ్యాంగ సవరణ ద్వారా అధ్యక్ష వ్యవస్థ ఏర్పాటు చేయలేమ. స్వేచ్ఛా-నిష్పక్షపాత ఎన్నికలు కూడా మూల నిర్మాణంలో భాగమే (ఇందిరా గాంధీ v. రాజ్‌నారాయణ్ 1975).\nParliamentary Democracy in Basic Structure means: (1) Government by popular vote; (2) Executive accountable to Parliament; (3) Cannot replace Parliamentary with Presidential system by amendment. Free & fair elections are also Basic Structure (Indira Gandhi v. Raj Narain 1975)."),

    (2, "medium",
     "మూల నిర్మాణంలో 'FRs మరియు DPSPs మధ్య సమతుల్యత' ఒక అంశం — ఇది ఏ కేసులో నిర్ణయించబడింది?\n(Harmony between FRs and DPSPs is part of Basic Structure — in which case was this decided?)",
     "కేశవానంద భారతి 1973 / Kesavananda Bharati 1973",
     "IR కోహెలో 2007 / IR Coelho 2007",
     "మినర్వా మిల్స్ లిమిటెడ్ v. భారత యూనియన్ 1980 / Minerva Mills Ltd v. Union of India 1980",
     "SR బొమ్మై 1994 / SR Bommai 1994",
     "C",
     "మినర్వా మిల్స్ 1980: FRs మరియు DPSPs మధ్య సమతుల్యత మరియు సమన్వయం మూల నిర్మాణంలో భాగమని ప్రకటించింది. పార్లమెంటు DPSPs పేరిట FRs పూర్తిగా రద్దు చేయలేదని పేర్కొంది.\nMinerva Mills 1980: Declared that harmony and balance between FRs and DPSPs is part of Basic Structure. Parliament cannot use DPSPs as justification to completely abrogate FRs."),

    (2, "hard",
     "మూల నిర్మాణంలో 'పరిమిత సవరణ అధికారం' (Limited Amending Power) చేర్చబడింది. దీని అర్థం ఏమిటి?\n(Limited Amending Power is part of Basic Structure. What does this mean?)",
     "పార్లమెంటు సంవత్సరానికి కేవలం 3 సవరణలు మాత్రమే చేయవచ్చు / Parliament can make only 3 amendments per year",
     "Art 368 కింద సవరణ అధికారం స్వయంగా పరిమితమైనది — ఈ పరిమితమైన సవరణ అధికారమే మూల నిర్మాణంలో భాగం / The amending power under Art 368 is itself limited — this limited power is part of basic structure",
     "50 కంటే ఎక్కువ నిబంధనలు ఒకే సవరణలో మార్చలేమ / More than 50 provisions cannot be changed in a single amendment",
     "సవరణ అధికారం 1973 వరకు మాత్రమే ఉంది / Amending power exists only till 1973",
     "B",
     "మినర్వా మిల్స్ 1980: పార్లమెంటు సవరణ అధికారం 'పరిమితమైనది' — ఇది మూల నిర్మాణంలో భాగమని తేల్చింది. 42వ సవరణ Art 368(4)(5) ద్వారా సవరణ అధికారాన్ని 'సంపూర్ణం' (absolute) అని ప్రకటించడానికి ప్రయత్నించింది — కానీ ఆ నిబంధనలే మూల నిర్మాణ ఉల్లంఘన కాబట్టి రద్దయ్యాయి.\nMinerva Mills 1980: Held that Parliament's amending power is 'limited' — this very limitedness is part of Basic Structure. The 42nd Amendment's Art 368(4)(5) trying to declare amending power 'absolute' were themselves struck down as violating Basic Structure."),

    # ══════════════ SECTION 3: POST-KESAVANANDA LANDMARK CASES (8 MCQs) ══════════════

    (3, "medium",
     "ఇందిరా గాంధీ v. రాజ్‌నారాయణ్ కేసు (1975) లో సుప్రీం కోర్టు ఏ సవరణను రద్దు చేసింది — ఎందుకు?\n(Which amendment did SC strike down in Indira Gandhi v. Raj Narain (1975) — and why?)",
     "42వ సవరణ — DPSPs FRs కంటే ఎక్కువ ప్రాముఖ్యత ఇచ్చినందుకు / 42nd Amendment — gave DPSPs more importance than FRs",
     "39వ సవరణ — ప్రధానమంత్రి ఎన్నికను న్యాయ సమీక్ష నుండి రక్షించినందుకు (స్వేచ్ఛా ఎన్నికలు మూల నిర్మాణం) / 39th Amendment — protected PM's election from judicial review (free & fair elections = Basic Structure)",
     "44వ సవరణ — ఆస్తి హక్కు తొలగించినందుకు / 44th Amendment — removed Right to Property",
     "36వ సవరణ — సిక్కిం విలీనానికి / 36th Amendment — for merger of Sikkim",
     "B",
     "ఇందిరా గాంధీ v. రాజ్‌నారాయణ్ 1975: 39వ సవరణ రద్దు చేయబడింది — అది ప్రధానమంత్రి మరియు కొన్ని ఉన్నత పదవుల ఎన్నికలను న్యాయ సమీక్ష నుండి రక్షించే ప్రయత్నం. SC నిర్ణయించింది: స్వేచ్ఛా మరియు న్యాయమైన ఎన్నికలు మూల నిర్మాణంలో భాగం — వాటిని న్యాయ సమీక్ష నుండి తొలగించలేమ.\nIndira Gandhi v. Raj Narain 1975: 39th Amendment struck down — it tried to protect election of PM and certain high offices from judicial review. SC held: free & fair elections are Basic Structure — they cannot be shielded from judicial review.",
     "APPSC"),

    (3, "medium",
     "మినర్వా మిల్స్ లిమిటెడ్ v. భారత యూనియన్ (1980) కేసులో ఏ నిర్దిష్ట నిబంధనలు రద్దు చేయబడ్డాయి?\n(Which specific provisions were struck down in Minerva Mills Ltd v. Union of India (1980)?)",
     "42వ సవరణలో Art 368(4) మరియు Art 368(5) — సవరణ అధికారం సంపూర్ణమని ప్రకటించిన నిబంధనలు / Art 368(4) and Art 368(5) of 42nd Amendment — provisions declaring amending power absolute",
     "Art 21A మరియు Art 51A / Art 21A and Art 51A",
     "Art 31C — సంపూర్ణంగా రద్దు చేయబడింది / Art 31C — completely struck down",
     "Art 19 పై 42వ సవరణ నిర్బంధాలు / Restrictions on Art 19 by 42nd Amendment",
     "A",
     "మినర్వా మిల్స్ 1980: 42వ సవరణ చేర్చిన Art 368(4) ('ఏ సవరణనూ న్యాయస్థానంలో ప్రశ్నించలేమ') మరియు Art 368(5) ('పార్లమెంటు సవరణ అధికారంపై ఎటువంటి పరిమితి లేదు') రద్దు చేయబడ్డాయి. Art 31C విస్తరణ (అన్ని DPSPలకు) కూడా రద్దు చేయబడింది; ఆరంభ Art 31C (39b/c) చెల్లుబాటులో ఉంది.\nMinerva Mills 1980: Art 368(4) ('no amendment can be questioned in court') and Art 368(5) ('no limitation on Parliament's amending power') of 42nd Amendment struck down. Extended Art 31C (covering all DPSPs) also struck down; original Art 31C (39b/c) remains valid.",
     "APPSC"),

    (3, "medium",
     "SR బొమ్మై v. భారత యూనియన్ (1994) కేసు ఏ సందర్భంలో వచ్చింది — ఏ నిర్ణయం తీసుకోబడింది?\n(In what context did SR Bommai v. Union of India (1994) arise — what was decided?)",
     "బ్యాంకుల జాతీయీకరణ చట్టాన్ని సవాల్ చేస్తూ / Challenging bank nationalisation law",
     "కర్ణాటక రాష్ట్ర ప్రభుత్వం రద్దు మరియు రాష్ట్రపతి పాలన విధింపుకు సంబంధించి — లౌకికత, సమాఖ్య స్వభావం మూల నిర్మాణంలో భాగమని తేల్చింది / Regarding dismissal of Karnataka government and imposition of President's Rule — held secularism, federalism are Basic Structure",
     "ఆస్తి హక్కు రద్దు చేసిన 44వ సవరణను సవాల్ చేస్తూ / Challenging 44th Amendment removing Right to Property",
     "9వ షెడ్యూల్‌లో చేర్చిన చట్టాలను సవాల్ చేస్తూ / Challenging laws added to 9th Schedule",
     "B",
     "SR బొమ్మై కేసు: 1988లో కర్ణాటక (S.R. Bommai ప్రభుత్వం) మరియు ఇతర రాష్ట్ర ప్రభుత్వాల రద్దుకు వ్యతిరేకంగా వచ్చింది. 9 న్యాయమూర్తులు: లౌకికత, ప్రజాస్వామ్యం, సమాఖ్య స్వభావం మూల నిర్మాణంలో భాగం; రాష్ట్రపతి పాలన తీర్పు న్యాయ సమీక్షకు లోనవుతుంది.\nSR Bommai: Related to dismissal of Karnataka (S.R. Bommai govt) and other state govts in 1988. 9 judges held: Secularism, democracy, federal character = Basic Structure; President's Rule decision is subject to judicial review."),

    (3, "hard",
     "L. చంద్రకుమార్ v. భారత యూనియన్ (1997) కేసులో మూల నిర్మాణం ఏ సందర్భంలో వర్తించింది?\n(In what context was Basic Structure applied in L. Chandra Kumar v. Union of India (1997)?)",
     "రాష్ట్రాల ఆమోదం లేకుండా 7వ షెడ్యూల్ సవరణ / Amendment to 7th Schedule without State ratification",
     "ఆర్టికల్ 323A మరియు 323B కింద ట్రిబ్యునల్‌ల తీర్పులపై SC/HC సమీక్ష తొలగించే నిబంధన మూల నిర్మాణ ఉల్లంఘన / Provision removing SC/HC review over Tribunals under Art 323A and 323B violates Basic Structure",
     "ప్రాథమిక విధులు పాటించకపోవడం / Non-compliance with Fundamental Duties",
     "ఎన్నికల కమిషన్ అధికారాలు తగ్గించే నిబంధన / Provision reducing powers of Election Commission",
     "B",
     "L. చంద్రకుమార్ కేసు 1997: Art 323A (Administrative Tribunals) మరియు Art 323B (వివిధ ట్రిబ్యునల్‌లు) కింద ట్రిబ్యునల్‌ల తీర్పులపై SC/HC న్యాయ సమీక్ష అధికారాన్ని పూర్తిగా తొలగించే నిబంధన మూల నిర్మాణ ఉల్లంఘన. న్యాయ సమీక్ష మూల నిర్మాణంలో భాగం కాబట్టి ట్రిబ్యునల్‌ల నుండి HC/SC కు అప్పీల్ తప్పనిసరి.\nL. Chandra Kumar 1997: Provisions under Art 323A and 323B excluding HC/SC judicial review over Tribunals violate Basic Structure. Since judicial review is Basic Structure, appeals from Tribunals to HC/SC are mandatory."),

    (3, "medium",
     "NJAC కేసు (2015) లో సుప్రీం కోర్టు ఏ సవరణను రద్దు చేసింది — ఎందుకు?\n(In the NJAC case (2015), which amendment did SC strike down — and why?)",
     "102వ సవరణ — NCBC / 102nd Amendment — NCBC",
     "99వ సవరణ — జాతీయ న్యాయ నియామకాల కమిషన్ (NJAC) స్థాపన — న్యాయవ్యవస్థ స్వాతంత్ర్యం మూల నిర్మాణంలో భాగం కాబట్టి / 99th Amendment — establishing NJAC — as Independence of Judiciary is Basic Structure",
     "103వ సవరణ — EWS రిజర్వేషన్ / 103rd Amendment — EWS reservation",
     "98వ సవరణ / 98th Amendment",
     "B",
     "NJAC కేసు 2015 (Supreme Court Advocates-on-Record Association v. Union of India): 99వ సవరణ చట్టం 2014 (National Judicial Appointments Commission ఏర్పాటు) రద్దు చేయబడింది. NJAC వ్యవస్థ న్యాయమూర్తుల నియామకంలో కార్యనిర్వాహకుడి జోక్యాన్ని అనుమతిస్తుంది — ఇది న్యాయవ్యవస్థ స్వాతంత్ర్యాన్ని (మూల నిర్మాణం) ఉల్లంఘిస్తుంది.\nNJAC case 2015 (SC Advocates-on-Record Association v. UoI): 99th Amendment 2014 (establishing NJAC) struck down. NJAC system allows executive interference in judicial appointments — violates Independence of Judiciary (Basic Structure).",
     "APPSC"),

    (3, "hard",
     "IR కోహెలో v. తమిళనాడు రాష్ట్రం (2007) కేసులో 9 న్యాయమూర్తుల ధర్మాసనం ఏ నిర్ణయం తీసుకుంది?\n(What did the 9-judge bench decide in IR Coelho v. State of Tamil Nadu (2007)?)",
     "9వ షెడ్యూల్‌లోని అన్ని చట్టాలు న్యాయ సమీక్షకు లోనవుతాయి / All laws in 9th Schedule are subject to judicial review",
     "9వ షెడ్యూల్‌లోని అన్ని చట్టాలు పూర్తిగా రక్షించబడతాయి / All laws in 9th Schedule are fully protected",
     "ఏప్రిల్ 24, 1973 తర్వాత 9వ షెడ్యూల్‌కు జోడించిన చట్టాలు ప్రాథమిక హక్కుల సారాన్ని నాశనం చేస్తే న్యాయ సమీక్షకు లోనవుతాయి / Laws added to 9th Schedule after April 24, 1973 are reviewable if they damage the essence of Fundamental Rights",
     "9వ షెడ్యూల్ రద్దు చేయాలి / 9th Schedule should be abolished",
     "C",
     "IR కోహెలో 2007 (9 న్యాయమూర్తులు): ఏప్రిల్ 24, 1973 తర్వాత 9వ షెడ్యూల్‌కు జోడించిన చట్టాలు ప్రాథమిక హక్కుల సారాన్ని నాశనం చేస్తే (especially Art 14, 19, 21 మరియు Art 32) న్యాయ సమీక్షకు లోనవుతాయి. ముందు 1973 జోడించిన చట్టాలు రక్షించబడతాయి (వామన్ రావు 1981 ప్రకారం).\nIR Coelho 2007 (9 judges): Laws added to 9th Schedule after April 24, 1973 are subject to judicial review if they damage the essence of Fundamental Rights (esp. Art 14, 19, 21 and Art 32). Laws added before Apr 24, 1973 are protected (per Waman Rao 1981)."),

    (3, "medium",
     "I.R. కోహెలో కేసులో 'ఏప్రిల్ 24, 1973' తేదీ ఎందుకు ముఖ్యమైనది?\n(Why is the date 'April 24, 1973' significant in the IR Coelho case?)",
     "అది Art 368 ఆమోదించిన తేదీ / That is the date Art 368 was adopted",
     "అది కేశవానంద భారతి తీర్పు తేదీ — ఈ తేదీ నుండే మూల నిర్మాణ సిద్ధాంతం అమలులోకి వచ్చింది / That is the date of Kesavananda Bharati judgment — Basic Structure doctrine came into force from this date",
     "అది భారత స్వాతంత్ర్య తేదీ / That is India's independence date",
     "అది గోలక్‌నాథ్ కేసు తేదీ / That is the date of Golaknath case",
     "B",
     "ఏప్రిల్ 24, 1973 — కేశవానంద భారతి తీర్పు తేదీ. ఈ తేదీ నుండే మూల నిర్మాణ సిద్ధాంతం స్పష్టంగా ప్రకటించబడింది. కాబట్టి: (1) ఈ తేదీకి ముందు 9వ షెడ్యూల్‌లో చేర్చబడిన చట్టాలు పూర్తి రక్షణ పొందుతాయి (వామన్ రావు 1981); (2) ఈ తేదీ తర్వాత చేర్చిన చట్టాలు మూల నిర్మాణ పరీక్షకు లోనవుతాయి (IR కోహెలో 2007).\nApril 24, 1973 — date of Kesavananda Bharati judgment. Basic Structure doctrine was explicitly announced from this date. Hence: (1) Laws added to 9th Schedule BEFORE this date get full protection (Waman Rao 1981); (2) Laws added AFTER this date subject to Basic Structure test (IR Coelho 2007)."),

    (3, "hard",
     "మూల నిర్మాణ సిద్ధాంతంపై ఏ విదేశీ రాజ్యాంగం ప్రభావం ఉందని పేర్కొంటారు?\n(Which foreign Constitution's influence is cited for the Basic Structure doctrine?)",
     "అమెరికా / United States",
     "బ్రిటన్ / Britain",
     "జర్మనీ / Germany",
     "ఆస్ట్రేలియా / Australia",
     "C",
     "జర్మనీ రాజ్యాంగం (Basic Law, 1949) 'eternity clauses' (Art 79(3)) ఆధారంగా మూల నిర్మాణ సిద్ధాంతం రూపొందించబడిందని చెప్పబడుతుంది. జర్మనీ రాజ్యాంగంలో 'మానవ గౌరవం', 'ప్రజాస్వామ్యం', 'సమాఖ్య నిర్మాణం' మార్చలేని అంశాలు. ఇది పకిస్తాన్, బంగ్లాదేశ్ రాజ్యాంగాలను కూడా ప్రభావితం చేసింది.\nThe German Constitution (Basic Law 1949) with its 'eternity clauses' (Art 79(3)) is cited as influencing the Basic Structure doctrine. German Constitution makes 'human dignity', 'democracy', 'federal structure' unamendable. This influenced Pakistan and Bangladesh constitutions too."),

    # ══════════════ SECTION 4: 42ND AMENDMENT & BASIC STRUCTURE (5 MCQs) ══════════════

    (4, "medium",
     "42వ సవరణ 1976 Art 368కు జోడించిన క్లాజులు (4) మరియు (5) ఏమి నిర్ణయించాయి?\n(What did clauses (4) and (5) added to Art 368 by the 42nd Amendment 1976 declare?)",
     "(4) రాష్ట్రపతి అనుమతి తప్పనిసరి; (5) రాష్ట్రాల ఆమోదం తప్పనిసరి / (4) President's assent mandatory; (5) State ratification mandatory",
     "(4) ఏ సవరణను న్యాయస్థానంలో ప్రశ్నించలేమ; (5) పార్లమెంటు సవరణ అధికారంపై ఎటువంటి పరిమితి లేదు — మినర్వా మిల్స్ 1980 ఇవి రద్దు చేసింది / (4) No amendment can be questioned in court; (5) No limitation on Parliament's amending power — struck down by Minerva Mills 1980",
     "(4) రాజ్యసభ ఆమోదం లేకుండా సవరణ చెల్లదు; (5) SC తీర్పులు సవరణతో రద్దు చేయవచ్చు / (4) Amendment void without RS consent; (5) SC judgments can be nullified by amendment",
     "(4) మరియు (5) ప్రత్యేక మెజారిటీ నిర్వచనం / (4) and (5) define Special Majority",
     "B",
     "42వ సవరణ 1976 Art 368(4) మరియు (5) జోడించింది: (4) — 'ఈ ఆర్టికల్ కింద చేసిన ఏ రాజ్యాంగ సవరణను అయినా, ఏ కారణంగానైనా, ఏ న్యాయస్థానంలోనూ ప్రశ్నించలేమ'; (5) — 'ఈ ఆర్టికల్ కింద రాజ్యాంగాన్ని సవరించే పార్లమెంటు అధికారాన్ని పరిమితం చేసే అనుబంధం లేదు.' మినర్వా మిల్స్ 1980 ఈ రెండూ రద్దు చేసింది.\n42nd Amendment 1976 added Art 368(4): 'No constitutional amendment under this article shall be called in question in any court on any ground'; and (5): 'There shall be no limitation on the constituent power of Parliament to amend the Constitution.' Both struck down by Minerva Mills 1980."),

    (4, "medium",
     "42వ సవరణ 1976 Art 31C విస్తరించింది. ఇది ఏమిటి? మినర్వా మిల్స్ 1980 దీని గురించి ఏమి నిర్ణయించింది?\n(The 42nd Amendment expanded Art 31C. What was it? What did Minerva Mills 1980 decide?)",
     "25వ సవరణలో Art 31C Art 39(b)(c) అమలు చేసే చట్టాలను రక్షించింది; 42వ సవరణ అన్ని DPSPలకు విస్తరించింది; మినర్వా మిల్స్ విస్తరణ రద్దు చేసింది — ఆరంభ Art 31C చెల్లుబాటులో ఉంది / Original Art 31C protected laws for Art 39(b)(c); 42nd extended to all DPSPs; Minerva Mills struck down extension — original Art 31C valid",
     "Art 31C పూర్తిగా రద్దు / Art 31C completely repealed",
     "Art 31C అన్ని ప్రాథమిక హక్కులను రక్షిస్తుంది / Art 31C protects all FRs",
     "Art 31C FRs DPSPs కంటే ముఖ్యమని ప్రకటించింది / Art 31C declared FRs more important than DPSPs",
     "A",
     "25వ సవరణ 1971: Art 31C — Art 39(b)(c) అమలు చేసే చట్టాలకు Art 14/19 రక్షణ. 42వ సవరణ దీన్ని అన్ని 20 DPSPలకు విస్తరించింది. మినర్వా మిల్స్ 1980 నిర్ణయించింది: విస్తరించిన Art 31C (అన్ని DPSPs) మూల నిర్మాణ ఉల్లంఘన కాబట్టి రద్దు; కానీ ఆరంభ 25వ సవరణ Art 31C (39b/c) చెల్లుబాటులో ఉంది.\n25th Amdt 1971: Art 31C protects laws for Art 39(b)(c). 42nd Amdt extended to all 20 DPSPs. Minerva Mills 1980: Extended Art 31C (all DPSPs) violates Basic Structure — struck down. But original Art 31C (for 39b/c) remains valid."),

    (4, "hard",
     "42వ సవరణ 1976 పీఠికలో మార్పులు చేసింది — ఏ పదాలు జోడించబడ్డాయి? ఇవి తర్వాత ఏమైనా రద్దు చేయబడ్డాయా?\n(42nd Amendment 1976 changed the Preamble — what words were added? Were these later struck down?)",
     "'గణతంత్ర' మరియు 'లౌకిక' జోడించబడ్డాయి — 44వ సవరణ రద్దు చేసింది / 'Republic' and 'Secular' added — 44th Amdt struck them down",
     "'సోషలిస్ట్', 'సెక్యులర్' మరియు 'ఏకాగ్రత' జోడించబడ్డాయి — ఇవి రద్దు చేయబడలేదు; కానీ పీఠిక మూల నిర్మాణంలో భాగమా అనే ప్రశ్న ఇప్పటికీ వివాదాస్పదం / 'Socialist', 'Secular' and 'Integrity' added — not struck down; but whether Preamble is Basic Structure remains debated",
     "పీఠిక పూర్తిగా మార్చబడింది — కేశవానంద 1973 రద్దు చేసింది / Preamble completely changed — Kesavananda 1973 struck it down",
     "'ప్రజాస్వామ్య' పదం తొలగించబడింది — మినర్వా మిల్స్ పునరుద్ధరించింది / 'Democratic' removed — Minerva Mills restored it",
     "B",
     "42వ సవరణ 1976 పీఠికలో 'సార్వభౌమ గణతంత్ర' ముందు 'సోషలిస్ట్ సెక్యులర్' మరియు 'ఐక్యత' తర్వాత 'ఏకాగ్రత' జోడించింది. ఈ మార్పులు తర్వాత రద్దు చేయబడలేదు. కేశవానంద భారతి 1973 పీఠిక రాజ్యాంగంలో భాగమని, 'Basic Features' చూపడానికి ఉపయోగపడుతుందని పేర్కొంది.\n42nd Amdt 1976 added 'Socialist Secular' before 'Sovereign Republic' and 'Integrity' after 'Unity' in Preamble. These were NOT struck down later. Kesavananda 1973 held Preamble is part of the Constitution and can indicate 'basic features.'"),

    (4, "hard",
     "42వ సవరణ 'మిని రాజ్యాంగం' అని పిలవబడడానికి కారణం మూల నిర్మాణ సిద్ధాంతంపై దాని ప్రభావం ఏమిటి?\n(Why is 42nd Amendment called 'Mini Constitution' and what was its impact on Basic Structure doctrine?)",
     "అది రాజ్యాంగాన్ని సంక్షిప్తం చేయడానికి ప్రయత్నించింది / It tried to condense the Constitution",
     "అది కేశవానంద భారతి నిర్ణయాన్ని రద్దు చేయడానికి, న్యాయ సమీక్ష తొలగించడానికి, సవరణ అధికారాన్ని సంపూర్ణం చేయడానికి ప్రయత్నించింది — కానీ మినర్వా మిల్స్ 1980 దాని కీలక నిబంధనలు రద్దు చేసింది / It tried to negate Kesavananda, remove judicial review, make amending power absolute — but Minerva Mills 1980 struck down its key provisions",
     "అది రాజ్యాంగంలో 42 కొత్త ఆర్టికల్‌లు జోడించింది / It added 42 new articles",
     "అది రాష్ట్రపతి పాలనా వ్యవస్థ ప్రవేశపెట్టింది / It introduced Presidential system",
     "B",
     "42వ సవరణ 1976 (అత్యవసర పరిస్థితిలో) మూల నిర్మాణ సిద్ధాంతాన్ని ప్రతిఘటించడానికి: (1) Art 368(4)(5) — సవరణ అధికారం సంపూర్ణం; (2) విస్తరించిన Art 31C — అన్ని DPSPలు FRs కంటే ఎక్కువ; (3) FRs తగ్గించింది, DPSPs బలోపేతం చేసింది. మినర్వా మిల్స్ 1980 (1)(2) రద్దు చేసింది — మూల నిర్మాణ సిద్ధాంతం బలపడింది.\n42nd Amendment 1976 (during Emergency) tried to counter Basic Structure: (1) Art 368(4)(5) — absolute amending power; (2) Extended Art 31C — all DPSPs over FRs; (3) Reduced FRs, strengthened DPSPs. Minerva Mills 1980 struck down (1) and (2) — Basic Structure doctrine strengthened."),

    (4, "medium",
     "మినర్వా మిల్స్ కేసు 1980 యొక్క అత్యంత ముఖ్యమైన నిర్ణయం ఏమిటి — మూల నిర్మాణం విషయంలో?\n(What is the most important holding of Minerva Mills 1980 with respect to Basic Structure?)",
     "పార్లమెంటు అధికారం ఏ విధంగానైనా సవరించడానికి సంపూర్ణం / Parliament's power to amend is absolutely unlimited",
     "FRs మరియు DPSPs మధ్య సమతుల్యత మూల నిర్మాణం; పార్లమెంటు సవరణ అధికారం పరిమితమైనది; Art 368(4)(5) రద్దు / Harmony between FRs and DPSPs is Basic Structure; Parliament's amending power is limited; Art 368(4)(5) struck down",
     "రాజ్యాంగ సవరణలపై న్యాయ సమీక్ష సాధ్యం కాదు / Judicial review of constitutional amendments is not possible",
     "అన్ని DPSPలు FRs కంటే ముఖ్యమైనవి / All DPSPs are more important than FRs",
     "B",
     "మినర్వా మిల్స్ 1980 అత్యంత ముఖ్యమైన నిర్ణయాలు: (1) FRs + DPSPs మధ్య సమతుల్యత మూల నిర్మాణం; (2) పార్లమెంటు సవరణ అధికారం 'పరిమితమైనది' (limited) — ఇది మూల నిర్మాణంలో భాగం; (3) Art 368(4)(5) రద్దు; (4) విస్తరించిన Art 31C రద్దు. ఇది కేశవానంద భారతి సిద్ధాంతాన్ని బలోపేతం చేసింది.\nMinerva Mills 1980 key holdings: (1) Harmony between FRs and DPSPs = Basic Structure; (2) Parliament's amending power is 'limited' — this limitedness is Basic Structure; (3) Art 368(4)(5) struck down; (4) Extended Art 31C struck down. Strengthened Kesavananda Bharati doctrine.",
     "APPSC"),

    # ══════════════ SECTION 5: SCOPE AND APPLICATION (5 MCQs) ══════════════

    (5, "medium",
     "మూల నిర్మాణ సిద్ధాంతం సాధారణ చట్టాలకు (ordinary legislation) వర్తిస్తుందా?\n(Does the Basic Structure doctrine apply to ordinary legislation?)",
     "అవును — అన్ని చట్టాలకు వర్తిస్తుంది / Yes — it applies to all laws",
     "లేదు — మూల నిర్మాణ సిద్ధాంతం కేవలం రాజ్యాంగ సవరణలకు మాత్రమే వర్తిస్తుంది, సాధారణ చట్టాలకు కాదు / No — Basic Structure doctrine applies only to constitutional amendments, not ordinary legislation",
     "కేవలం కేంద్ర చట్టాలకు వర్తిస్తుంది / Applies only to Central laws",
     "కేవలం అత్యవసర పరిస్థితిలో చేసిన చట్టాలకు వర్తిస్తుంది / Applies only to laws made during Emergency",
     "B",
     "మూల నిర్మాణ సిద్ధాంతం కేవలం రాజ్యాంగ సవరణలకు మాత్రమే వర్తిస్తుంది — Art 368 కింద పార్లమెంటు చేసే సవరణలకు. సాధారణ చట్టాలు (ordinary legislation) Part III (FRs) మరియు రాజ్యాంగ నిబంధనలతో సంగతిని బట్టి ప్రశ్నించబడతాయి — కానీ 'Basic Structure' పదాన్ని ఉపయోగించి కాదు.\nBasic Structure doctrine applies ONLY to constitutional amendments under Art 368 — not to ordinary legislation. Ordinary laws are tested against Part III (FRs) and other constitutional provisions — not through Basic Structure doctrine.",
     "APPSC"),

    (5, "medium",
     "మూల నిర్మాణ సిద్ధాంతాన్ని రాష్ట్ర చట్టాలకు వ్యతిరేకంగా వర్తింపజేయవచ్చా?\n(Can the Basic Structure doctrine be applied against State laws?)",
     "అవును — రాష్ట్ర శాసనసభలు కూడా మూల నిర్మాణం ఉల్లంఘిస్తే చట్టం రద్దవుతుంది / Yes — State laws too become void if they violate Basic Structure",
     "లేదు — రాష్ట్ర శాసనసభలు రాజ్యాంగ సవరణ చేయవు; మూల నిర్మాణ సిద్ధాంతం కేవలం రాజ్యాంగ సవరణలకే వర్తిస్తుంది / No — State legislatures do not amend the Constitution; doctrine applies only to constitutional amendments",
     "అవును — కానీ కేవలం 7వ షెడ్యూల్‌కు సంబంధించిన రాష్ట్ర చట్టాలకు / Yes — but only for state laws related to 7th Schedule",
     "రాష్ట్ర చట్టాలను SC తప్ప HC సమీక్షించలేదు / HCs cannot review state laws — only SC can",
     "B",
     "మూల నిర్మాణ సిద్ధాంతం రాష్ట్ర చట్టాలకు వర్తించదు — ఎందుకంటే రాష్ట్ర శాసనసభలు రాజ్యాంగాన్ని సవరించే అధికారం కలిగి లేవు. ఈ సిద్ధాంతం Art 368 కింద పార్లమెంటు సవరణ అధికారంపై మాత్రమే వర్తిస్తుంది. రాష్ట్ర చట్టాలు FRs మరియు ఇతర రాజ్యాంగ నిబంధనల ఆధారంగా ప్రశ్నించబడతాయి.\nBasic Structure doctrine does NOT apply to State laws — State legislatures have no power to amend the Constitution. The doctrine applies only to Parliament's amending power under Art 368. State laws are challenged on grounds of FRs and other constitutional provisions."),

    (5, "hard",
     "అత్యవసర పరిస్థితిలో రాజ్యాంగ సవరణ చేసే అవకాశం ఉంది — మూల నిర్మాణ సిద్ధాంతం అప్పుడు వర్తిస్తుందా?\n(Can constitutional amendments be made during Emergency — does Basic Structure doctrine apply then?)",
     "అత్యవసర పరిస్థితిలో మూల నిర్మాణ సిద్ధాంతం పక్కన పెట్టవచ్చు / Basic Structure doctrine can be suspended during Emergency",
     "అత్యవసర పరిస్థితిలో కూడా రాజ్యాంగ సవరణ చేయవచ్చు, కానీ మూల నిర్మాణ సిద్ధాంతం వర్తిస్తుంది — ఆ సవరణ మూల నిర్మాణాన్ని నాశనం చేయలేదు / Amendments can be made even during Emergency but Basic Structure doctrine still applies — the amendment cannot destroy Basic Structure",
     "అత్యవసర పరిస్థితిలో రాజ్యాంగ సవరణ చేయలేమ / Constitutional amendments cannot be made during Emergency",
     "అత్యవసర పరిస్థితిలో Art 368 తాత్కాలికంగా రద్దవుతుంది / Art 368 temporarily lapses during Emergency",
     "B",
     "అత్యవసర పరిస్థితిలో కూడా రాజ్యాంగ సవరణ చేయవచ్చు — ఇందిరా గాంధీ అత్యవసర పరిస్థితి (1975-77) సమయంలో 42వ సవరణ చేసింది. కానీ ఏ పరిస్థితిలోనైనా మూల నిర్మాణ సిద్ధాంతం వర్తిస్తుంది — అత్యవసర పరిస్థితి సిద్ధాంతాన్ని నిలిపివేయదు.\nConstitutional amendments can be made even during Emergency — Indira Gandhi enacted 42nd Amendment during Emergency (1975-77). BUT Basic Structure doctrine applies in all circumstances — Emergency does not suspend the doctrine."),

    (5, "medium",
     "మూల నిర్మాణ సిద్ధాంతంలో 'ప్రాథమిక హక్కులు' అన్నీ మూల నిర్మాణంలో భాగమా?\n(Are ALL Fundamental Rights part of Basic Structure?)",
     "అవును — Part III లోని అన్ని ప్రాథమిక హక్కులు మూల నిర్మాణంలో భాగం / Yes — all FRs in Part III are Basic Structure",
     "కాదు — ప్రాథమిక హక్కుల సారం (essence/core) మూల నిర్మాణంలో భాగం; అన్ని ప్రాథమిక హక్కులు కాదు. Art 21 వంటి అతి ముఖ్యమైన హక్కుల సారం రక్షించబడుతుంది / No — the essence/core of FRs is Basic Structure; not ALL FRs. Essence of crucial rights like Art 21 is protected",
     "ప్రాథమిక హక్కులు అసలు మూల నిర్మాణంలో భాగం కాదు / FRs are not part of Basic Structure at all",
     "కేవలం Art 14 మరియు Art 21 మూల నిర్మాణంలో భాగం / Only Art 14 and Art 21 are Basic Structure",
     "B",
     "IR కోహెలో 2007: అన్ని ప్రాథమిక హక్కులు మూల నిర్మాణంలో భాగం కాదు — కానీ ప్రాథమిక హక్కుల 'సారం' (essence/core rights) మూల నిర్మాణంలో భాగం. ముఖ్యంగా Art 14 (సమానత్వం), Art 19 (స్వేచ్ఛలు), Art 21 (జీవించే హక్కు), Art 32 (రాజ్యాంగ పరిష్కారాల హక్కు) — వాటి సారం రక్షించబడుతుంది.\nIR Coelho 2007: NOT all FRs are Basic Structure — but the 'essence/core' of Fundamental Rights is Basic Structure. Especially Art 14 (equality), Art 19 (freedoms), Art 21 (right to life), Art 32 (constitutional remedies) — their essence is protected."),

    (5, "hard",
     "మూల నిర్మాణ సిద్ధాంతం అంటే ఒక నిర్ణీత జాబితా ఉందా లేదా అది అభివృద్ధి చెందే సిద్ధాంతమా?\n(Is there a fixed list of Basic Structure elements, or is it an evolving doctrine?)",
     "అవును — కేశవానంద 1973లో స్పష్టమైన 10 అంశాల జాబితా నిర్ణయించబడింది / Yes — a clear list of 10 elements was fixed in Kesavananda 1973",
     "లేదు — మూల నిర్మాణ అంశాల స్థిరమైన జాబితా లేదు; విభిన్న కేసులలో విభిన్న న్యాయమూర్తులు విభిన్న అంశాలు గుర్తించారు — ఇది అభివృద్ధి చెందే సిద్ధాంతం / No — there is no fixed list; different judges in different cases identified different elements — it is an evolving doctrine",
     "కేవలం 5 అంశాలు మాత్రమే మూల నిర్మాణంలో ఉన్నాయి — పార్లమెంట్ మిగిలిన వాటిని మార్చవచ్చు / Only 5 elements are Basic Structure — Parliament can change the rest",
     "సుప్రీం కోర్టు 2007లో స్థిరమైన జాబితా ప్రకటించింది / SC announced a fixed list in 2007",
     "B",
     "మూల నిర్మాణ సిద్ధాంతం అభివృద్ధి చెందే (evolving) సిద్ధాంతం. స్థిరమైన జాబితా లేదు — ప్రతి కేసులో SC ప్రత్యేక సందర్భంలో మూల నిర్మాణ ఉల్లంఘన ఉందా అని పరిశీలిస్తుంది. ఈ వశ్యత (flexibility) సిద్ధాంతాన్ని బలంగా చేస్తుంది — సమాజ మార్పులకు అనుగుణంగా అభివృద్ధి చెందుతుంది.\nBasic Structure doctrine is EVOLVING — there is no fixed list. In each case, SC examines whether the specific provision damages the basic structure in context. This flexibility makes the doctrine powerful — it develops with societal changes."),

    # ══════════════ SECTION 6: TOUGH MCQs (5 MCQs) ══════════════

    (6, "hard",
     "గోలక్‌నాథ్ (1967) మరియు కేశవానంద భారతి (1973) మధ్య ముఖ్యమైన వ్యత్యాసం ఏమిటి — ప్రాథమిక హక్కుల సవరణీయత విషయంలో?\n(Key difference between Golaknath (1967) and Kesavananda Bharati (1973) regarding amendability of FRs?)",
     "రెండూ FRs సవరించవచ్చు అని చెప్పాయి / Both held FRs can be amended",
     "గోలక్‌నాథ్: FRs అసలు సవరించలేమ (పూర్ణ నిషేధం); కేశవానంద: FRs సవరించవచ్చు కానీ మూల నిర్మాణం నాశనం చేయలేమ (పరిమిత అనుమతి) / Golaknath: FRs absolutely cannot be amended; Kesavananda: FRs can be amended but Basic Structure cannot be destroyed",
     "కేశవానంద: FRs అసలు సవరించలేమ; గోలక్‌నాథ్: FRs సవరించవచ్చు / Kesavananda: FRs cannot be amended at all; Golaknath: FRs can be amended",
     "రెండూ FRs సవరించలేమ అని చెప్పాయి / Both held FRs cannot be amended",
     "B",
     "గురుతరమైన వ్యత్యాసం: గోలక్‌నాథ్ 1967 — FRs అసలు సవరించలేమ (absolute prohibition). కేశవానంద భారతి 1973 — FRs సవరించవచ్చు కానీ వాటి 'సారం' (essence) లేదా రాజ్యాంగ మూల నిర్మాణాన్ని నాశనం చేయలేమ (qualified/limited permission). కేశవానంద 24వ సవరణ 1971 యొక్క చెల్లుబాటును ధృవీకరించింది.\nKey difference: Golaknath 1967 — FRs absolutely CANNOT be amended. Kesavananda Bharati 1973 — FRs CAN be amended but their essence/Basic Structure CANNOT be destroyed. Kesavananda upheld the validity of 24th Amendment 1971."),

    (6, "hard",
     "కింది కేసుల-నిర్ణయాల జంటలలో ఏది తప్పు?\n(Which case-holding pair is INCORRECT?)",
     "శంకరి ప్రసాద్ 1951 → FRs సవరించవచ్చు / Shankari Prasad 1951 → FRs can be amended",
     "కేశవానంద భారతి 1973 → మూల నిర్మాణం నాశనం చేయలేమ / Kesavananda Bharati 1973 → Basic Structure cannot be destroyed",
     "మినర్వా మిల్స్ 1980 → Art 368(4)(5) రద్దు / Minerva Mills 1980 → Art 368(4)(5) struck down",
     "SR బొమ్మై 1994 → 9వ షెడ్యూల్ చట్టాలు ఎప్పటికీ సమీక్షించలేమ / SR Bommai 1994 → 9th Schedule laws can never be reviewed",
     "D",
     "SR బొమ్మై 1994 9వ షెడ్యూల్ గురించి కాదు — అది లౌకికత, సమాఖ్య స్వభావం మూల నిర్మాణంలో భాగమని, రాష్ట్రపతి పాలన న్యాయ సమీక్షకు లోనవుతుందని నిర్ణయించింది. '9వ షెడ్యూల్ చట్టాలు ఎప్పటికీ సమీక్షించలేమ' అనే నిర్ణయం తప్పు — IR కోహెలో 2007 ఏప్రిల్ 24, 1973 తర్వాత జోడించిన చట్టాలు సమీక్షించవచ్చని నిర్ణయించింది.\nSR Bommai 1994 is NOT about 9th Schedule — it dealt with secularism, federalism as Basic Structure and judicial review of President's Rule. The pair 'SR Bommai → 9th Schedule laws can never be reviewed' is WRONG — that's IR Coelho 2007 which said post-Apr 24 1973 laws ARE reviewable."),

    (6, "hard",
     "ఏ కేసు 'ప్రాథమిక హక్కుల' మరియు '9వ షెడ్యూల్' మధ్య సంబంధాన్ని అత్యంత సమగ్రంగా నిర్ణయించింది?\n(Which case most comprehensively decided the relationship between Fundamental Rights and the 9th Schedule?)",
     "కేశవానంద భారతి 1973 / Kesavananda Bharati 1973",
     "వామన్ రావు 1981 / Waman Rao 1981",
     "IR కోహెలో v. తమిళనాడు రాష్ట్రం 2007 (9 న్యాయమూర్తులు) / IR Coelho v. State of Tamil Nadu 2007 (9 judges)",
     "మినర్వా మిల్స్ 1980 / Minerva Mills 1980",
     "C",
     "IR కోహెలో v. తమిళనాడు రాష్ట్రం 2007 (9 న్యాయమూర్తుల ధర్మాసనం) ఈ సంబంధాన్ని అత్యంత సమగ్రంగా నిర్ణయించింది: (1) ఏప్రిల్ 24, 1973 కట్-ఆఫ్ తేదీ; (2) తర్వాత జోడించిన చట్టాలు FR సారం ఉల్లంఘిస్తే సమీక్షించవచ్చు; (3) Art 31B రక్షణ పరిమితం — మూల నిర్మాణ ఉల్లంఘనకు వర్తించదు.\nIR Coelho v. State of Tamil Nadu 2007 (9-judge bench) most comprehensively decided this: (1) April 24, 1973 cut-off date; (2) Laws added after that reviewable if they violate essence of FRs; (3) Art 31B protection is limited — does not cover basic structure violations."),

    (6, "hard",
     "కింది ఏ నిర్ణయం 'న్యాయవ్యవస్థ స్వాతంత్ర్యం' మూల నిర్మాణంలో భాగమని అన్ని కేసులకన్నా స్పష్టంగా నిర్ధారించింది?\n(Which case most clearly affirmed that Independence of Judiciary is part of Basic Structure?)",
     "కేశవానంద భారతి 1973 / Kesavananda Bharati 1973",
     "NJAC కేసు 2015 (99వ సవరణ రద్దు) / NJAC case 2015 (99th Amendment struck down)",
     "L. చంద్రకుమార్ 1997 / L. Chandra Kumar 1997",
     "SR బొమ్మై 1994 / SR Bommai 1994",
     "B",
     "NJAC కేసు 2015 (Supreme Court Advocates-on-Record Association v. Union of India): 99వ సవరణ (National Judicial Appointments Commission) రద్దు చేస్తూ, న్యాయవ్యవస్థ స్వాతంత్ర్యం మూల నిర్మాణంలో భాగమని అత్యంత స్పష్టంగా నిర్ధారించింది. NJAC కార్యనిర్వాహక జోక్యాన్ని అనుమతించడం వల్ల న్యాయవ్యవస్థ స్వాతంత్ర్యం దెబ్బతింటుందని పేర్కొంది.\nNJAC case 2015 (SC Advocates-on-Record Association v. UoI): Striking down 99th Amendment (NJAC), most clearly affirmed Independence of Judiciary is Basic Structure. NJAC's executive involvement would damage judicial independence — hence unconstitutional."),

    (6, "hard",
     "మూల నిర్మాణ సిద్ధాంతానికి 'ఆమ్నిమ్నస్' (omnibus) పేర్చే వ్యతిరేకత ఏమిటి — మరియు ఈ సిద్ధాంతం రక్షణ ఏమిటి?\n(What is the 'omnibus' criticism of Basic Structure doctrine — and what is the defence?)",
     "సిద్ధాంతం చాలా కష్టంగా అర్థమవుతుంది అని విమర్శ / Criticism that doctrine is too difficult to understand",
     "విమర్శ: SC అపరిమితమైన అధికారం పొందింది — 'మూల నిర్మాణం' అనే పేరిట ఏ సవరణను అయినా రద్దు చేయవచ్చు; రక్షణ: ఇది అవసరమైన తనిఖీ — చారిత్రక దుర్వినియోగం నుండి రక్షణ కల్పిస్తుంది (42వ సవరణ లాంటివి) / Criticism: SC gets unlimited power — can strike down any amendment as 'Basic Structure'; Defence: It is a necessary check — protects from historical abuse (like 42nd Amendment)",
     "సిద్ధాంతం అమెరికా నుండి అరువు తెచ్చింది అని విమర్శ / Criticism that doctrine is borrowed from USA",
     "సిద్ధాంతం పార్లమెంటరీ ప్రజాస్వామ్యానికి వ్యతిరేకం కాదని విమర్శ / Criticism that doctrine is not against Parliamentary democracy",
     "B",
     "మూల నిర్మాణ విమర్శలు: (1) SC 'super parliament' అవుతుంది; (2) నిర్వచనం అస్పష్టంగా ఉంది; (3) అనిర్ణీత జాబితా న్యాయ అనిశ్చితికి దారితీస్తుంది. రక్షణ: (1) 42వ సవరణ దుర్వినియోగం (1976) నుండి రాజ్యాంగాన్ని రక్షించింది; (2) న్యాయ సమీక్ష రాజ్యాంగ రక్షణకు అవసరం; (3) ప్రజాస్వామ్యం, FRs, లౌకికత రక్షణ ప్రజలకే మేలు.\nCriticisms: (1) SC becomes 'super parliament'; (2) Unclear definition; (3) Open-ended list creates judicial uncertainty. Defence: (1) Protected Constitution from 42nd Amendment abuse (1976); (2) Judicial review essential for constitutional protection; (3) Protecting democracy, FRs, secularism benefits citizens."),

]



import json as _json


def _seed_polity_ch12_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "12.1 పూర్వ-కేశవానంద కేసులు", "sub": "Pre-KB Cases · Shankari Prasad 1951 · Sajjan Singh 1964 · Golaknath 1967", "audio": ""},
    {"title": "12.2 కేశవానంద భారతి కేసు 1973", "sub": "Kesavananda Bharati · 13-Judge Bench · Basic Structure Doctrine · 7:6", "audio": ""},
    {"title": "12.3 మూల నిర్మాణ అంశాలు", "sub": "Elements · Supremacy · Republic · Federalism · Secularism · Judicial Independence", "audio": ""},
    {"title": "12.4 కేశవానంద తర్వాత ముఖ్య కేసులు", "sub": "Post-KB Cases · Indira Gandhi · Minerva Mills · Waman Rao · SR Bommai · NJAC 2015", "audio": ""},
    {"title": "12.5 42వ సవరణ మరియు మూల నిర్మాణం", "sub": "42nd Amendment 1976 · Emergency · Minerva Mills 1980 · Art 368(4)(5)", "audio": ""},
    {"title": "12.6 వ్యాప్తి మరియు అనువర్తనం", "sub": "Scope · Ordinary Laws · Only Amendments · Presidential Power · Germany", "audio": ""},
    {"title": "12.7 కఠిన ప్రశ్నలు", "sub": "Tough MCQs · Criticism · Defence · Parliamentary System · Unlimited Power", "audio": ""}
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
        (12, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch12 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (12, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 12,
         'రాజ్యాంగ మూల నిర్మాణం',
         'Basic Structure of the Constitution',
         'Ch.12',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch12 notes seeded!'}


def _seed_polity_ch12_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (12, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch12_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (12, 'Indian_Polity'))
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
    for mcq in POLITY_CH12_MCQS:
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

    total = len(POLITY_CH12_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch12 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
