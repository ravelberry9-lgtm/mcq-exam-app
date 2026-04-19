# seed_polity_ch12.py
# Chapter 12: Basic Structure of the Constitution (రాజ్యాంగ మూల నిర్మాణం)
# Standard : APPSC Group 2 | Source: Lakshmikanth Indian Polity
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

POLITY_CH12_SECTIONS = [
    {"title": "12.1 పూర్వ-కేశవానంద కేసులు", "sub": "Shankari Prasad 1951 · Sajjan Singh 1964 · Golaknath 1967 · 24th & 25th Amendments", "audio": ""},
    {"title": "12.2 కేశవానంద భారతి కేసు 1973", "sub": "13-Judge Bench · 7:6 Majority · Basic Structure Doctrine · A.N. Ray Appointment", "audio": ""},
    {"title": "12.3 మూల నిర్మాణ అంశాలు", "sub": "Elements · Supremacy · Republic · Federalism · Secularism · Judicial Independence · Parliamentary System", "audio": ""},
    {"title": "12.4 కేశవానంద తర్వాత ముఖ్య కేసులు", "sub": "Indira Gandhi 1975 · Minerva Mills 1980 · Waman Rao 1981 · IR Coelho 2007 · NJAC 2015", "audio": ""},
    {"title": "12.5 42వ సవరణ మరియు మూల నిర్మాణం", "sub": "42nd Amendment 1976 · Emergency · Art 368(4)(5) · Minerva Mills 1980 · Restoration", "audio": ""},
    {"title": "12.6 వ్యాప్తి మరియు అనువర్తనం", "sub": "Scope · Only Amendments · Ordinary Laws · German Grundnorm · Evolving List", "audio": ""},
    {"title": "12.7 కఠిన ప్రశ్నలు", "sub": "Tough MCQs · Art 13 vs BS · Omnibus Criticism · Parliament's Unlimited Power · Eternity Clause", "audio": ""},
]

POLITY_CH12_MCQS = [

    # ══════════════ SECTION 0: PRE-KESAVANANDA CASES (7 MCQs) ══════════════

    (0, 1,
     "శంకరి ప్రసాద్ v. భారత యూనియన్ (1951) కేసులో సుప్రీం కోర్టు ఏమి తీర్పు ఇచ్చింది?\n(What did the Supreme Court hold in Shankari Prasad v. Union of India 1951?)",
     "రాజ్యాంగ సవరణలు Art 13(2) లోని 'చట్టం' పరిధిలో వస్తాయి — FRs సవరించలేరు / Amendments fall within 'law' in Art 13(2) — FRs cannot be amended",
     "రాజ్యాంగ సవరణలు Art 13(2) లోని 'చట్టం' పరిధిలో రావు — పార్లమెంట్ FRs సవరించవచ్చు / Amendments do NOT fall under 'law' in Art 13(2) — Parliament can amend FRs",
     "ప్రాథమిక హక్కులు సవరించలేనివి / Fundamental Rights are unamendable",
     "Art 368 సవరణకు వర్తించదు / Art 368 does not apply to amendments",
     "b",
     "శంకరి ప్రసాద్ 1951: SC నిర్ణయించింది — రాజ్యాంగ సవరణలు Art 13(2) లోని 'చట్టం' కిందకు రావు (Constituent Power ≠ Legislative Power). కాబట్టి పార్లమెంట్ Art 368 ద్వారా ప్రాథమిక హక్కులతో సహా ఏ నిబంధనను అయినా సవరించవచ్చు.\nShankari Prasad 1951: SC held amendments do NOT fall within 'law' under Art 13(2) — Constituent Power is separate from Legislative Power. So Parliament can amend any provision including FRs via Art 368."),

    (0, 1,
     "సజ్జన్ సింగ్ v. రాజస్థాన్ రాష్ట్రం (1964) కేసు ఏ సవరణతో సంబంధం కలిగి ఉంది?\n(The Sajjan Singh v. State of Rajasthan 1964 case involved which amendment?)",
     "42వ రాజ్యాంగ సవరణ / 42nd Constitutional Amendment",
     "24వ రాజ్యాంగ సవరణ / 24th Constitutional Amendment",
     "17వ రాజ్యాంగ సవరణ / 17th Constitutional Amendment",
     "1వ రాజ్యాంగ సవరణ / 1st Constitutional Amendment",
     "c",
     "సజ్జన్ సింగ్ 1964 కేసు 17వ రాజ్యాంగ సవరణతో సంబంధం కలిగి ఉంది. SC శంకరి ప్రసాద్ తీర్పును సమర్థించి పార్లమెంట్‌కు FRs సవరించే అధికారం ఉందని నిర్ణయించింది (5:2 మెజారిటీతో). జస్టిస్ హిడయతుల్లా మరియు జస్టిస్ ముధోల్కర్ అసంమతి తెలిపారు.\nSajjan Singh 1964 involved 17th Constitutional Amendment. SC reaffirmed Shankari Prasad — Parliament has power to amend FRs (5:2 majority). Justices Hidayatullah and Mudholkar dissented, raising Basic Structure concerns."),

    (0, 2,
     "గోలక్‌నాథ్ v. పంజాబ్ రాష్ట్రం (1967) కేసులో 11 మంది న్యాయమూర్తులు ఏ నిర్ణయం తీసుకున్నారు?\n(What was the ruling in Golaknath v. State of Punjab 1967 by 11 judges?)",
     "పార్లమెంట్ FRs సవరించవచ్చు — ముందరి కేసులు సమర్థించారు / Parliament can amend FRs — upheld earlier cases",
     "FRs ని సవరించడం నిషేధం — రాజ్యాంగంలో 'ప్రాధాన్యత' ఉంది / Amending FRs is prohibited — they have primacy",
     "పార్లమెంట్ FRs సవరించలేదు — 6:5 మెజారిటీ; Prospective Overruling వర్తింపజేశారు / Parliament cannot amend FRs — 6:5 majority; Prospective Overruling applied",
     "FRs మరియు DPSP కలిసి 'మూల నిర్మాణం' ఏర్పరుస్తాయి / FRs and DPSP together form Basic Structure",
     "c",
     "గోలక్‌నాథ్ 1967: 11 న్యాయమూర్తుల ధర్మాసనం 6:5 మెజారిటీతో: పార్లమెంట్ FRs సవరించే అధికారం లేదు అని నిర్ణయించింది. Prospective Overruling సిద్ధాంతాన్ని వర్తింపజేసింది — పూర్వ సవరణలు చెల్లుబాటులో ఉంటాయి. Chief Justice Subba Rao నేతృత్వంలో.\nGolaknath 1967: 11-judge bench held 6:5 majority: Parliament CANNOT amend FRs. Applied doctrine of Prospective Overruling — previous amendments remain valid. Led by Chief Justice Subba Rao."),

    (0, 2,
     "24వ రాజ్యాంగ సవరణ 1971 ఏ లక్ష్యంతో చేశారు?\n(What was the purpose of the 24th Constitutional Amendment 1971?)",
     "భూ సంస్కరణలు అమలు చేయడానికి / To implement land reforms",
     "గోలక్‌నాథ్ 1967 తీర్పును తిప్పికొట్టి FRs సహా ఏ నిబంధనను అయినా సవరించే అధికారం ఉందని స్పష్టం చేయడానికి / To overturn Golaknath 1967 and clarify Parliament can amend any provision including FRs",
     "న్యాయ నియామకాలలో కార్యనిర్వాహక నియంత్రణ కోసం / For executive control over judicial appointments",
     "సమాజవాదం మరియు లౌకికత పదాలు ప్రస్తావనలో చేర్చడానికి / To add Socialist and Secular to Preamble",
     "b",
     "24వ సవరణ 1971: (1) Art 13 కి సవరణలు వర్తించవు అని స్పష్టం చేసింది, (2) Art 368 కి 'ఈ రాజ్యాంగంలోని ఏ నిబంధనను అయినా సవరించవచ్చు' అని జోడించింది, (3) రాష్ట్రపతి అంగీకారం తప్పనిసరి చేసింది. గోలక్‌నాథ్ కు పార్లమెంటరీ జవాబు.\n24th Amendment 1971: (1) Clarified Art 13 does not apply to amendments, (2) Added Parliament can amend 'any provision', (3) Made President's assent mandatory. Parliamentary response to Golaknath 1967."),

    (0, 2,
     "25వ రాజ్యాంగ సవరణ 1971 ఏ Art ప్రవేశపెట్టింది మరియు దాని ప్రభావం ఏమిటి?\n(Which Article did the 25th Amendment 1971 introduce and what was its effect?)",
     "Art 31D — మైనారిటీ హక్కుల పరిరక్షణ / Art 31D — minority rights protection",
     "Art 31C — DPSPs (Art 39b,c) అమలు చేసే చట్టాలకు Art 14, 19 రక్షణ తొలగించింది / Art 31C — laws implementing DPSPs (Art 39b,c) cannot be challenged under Art 14 or 19",
     "Art 31B — 9వ షెడ్యూల్ రక్షణ / Art 31B — 9th Schedule protection",
     "Art 31A — ఆస్తి సేకరణ చట్టాలకు FR రక్షణ / Art 31A — FR protection for property acquisition laws",
     "b",
     "25వ సవరణ 1971: Art 31C ప్రవేశపెట్టింది — DPSP లు (Art 39b మరియు c) అమలు చేసే చట్టాలు Art 14, Art 19 ఉల్లంఘన ఆరోపణ ఎదుర్కోవు. అంతేకాకుండా Art 31(2) సవరించి 'compensation' బదులు 'amount' చేసింది. ఈ సవరణ కేశవానంద కేసుకు దారి తీసింది.\n25th Amendment 1971: Introduced Art 31C — laws implementing DPSPs (Art 39b,c) cannot be challenged under Art 14 or 19. Also substituted 'amount' for 'compensation' in Art 31(2). This amendment paved the way for the Kesavananda case."),

    (0, 3,
     "కేశవానంద భారతి కేసు ముందు SC తీర్పుల క్రమం ఏది సరైనది?\n(Which is the correct sequence of SC judgments before Kesavananda Bharati?)",
     "Golaknath → Shankari Prasad → Sajjan Singh",
     "Shankari Prasad → Sajjan Singh → Golaknath",
     "Sajjan Singh → Golaknath → Shankari Prasad",
     "Shankari Prasad → Golaknath → Sajjan Singh",
     "b",
     "సరైన క్రమం: (1) శంకరి ప్రసాద్ 1951 — FRs సవరించవచ్చు; (2) సజ్జన్ సింగ్ 1964 — FRs సవరించవచ్చు (శంకరి ప్రసాద్ సమర్థన); (3) గోలక్‌నాథ్ 1967 — FRs సవరించలేరు (రివర్సల్). కేశవానంద 1973 = ఈ వివాదానికి పరిష్కారం.\nCorrect sequence: (1) Shankari Prasad 1951 — FRs can be amended; (2) Sajjan Singh 1964 — FRs can be amended (upheld SP); (3) Golaknath 1967 — FRs CANNOT be amended (reversal). Kesavananda 1973 = resolution of this conflict.",
     "APPSC"),

    (0, 3,
     "నిజ్జలింగప్ప v. జయశ్రీ (1971) కేసు ముఖ్యమైనది ఎందుకు?\n(Why is Nzjalingappa v. Jayashree 1971 important?)",
     "మొదటిసారి 'మూల నిర్మాణం' అనే పదం అధికారికంగా వాడారు / First formal use of the term 'Basic Structure'",
     "మూల నిర్మాణ జాబితా ఖరారు చేశారు / Finalised the Basic Structure list",
     "24వ సవరణ చెల్లుబాటు నిర్ణయించారు / Decided validity of 24th Amendment",
     "Art 358-359 ఆపరేషన్ వివరించారు / Explained operation of Arts 358-359",
     "a",
     "నిజ్జలింగప్ప 1971 కేసులో Justice Sikri మొదటిసారి 'Basic Structure' అనే పదాన్ని అధికారికంగా ఉపయోగించారు. ఇది తర్వాత కేశవానంద భారతి కేసులో అభివృద్ధి చేసిన సిద్ధాంతానికి పూర్వగామి.\nIn Nzjalingappa 1971, Justice Sikri first formally used the term 'Basic Structure'. This preceded and influenced the full doctrine developed in Kesavananda Bharati 1973."),

    # ══════════════ SECTION 1: KESAVANANDA BHARATI CASE 1973 (8 MCQs) ══════════════

    (1, 1,
     "కేశవానంద భారతి v. కేరళ రాష్ట్రం (1973) కేసులో ఎంత మంది న్యాయమూర్తులు విచారించారు మరియు ఏ నిష్పత్తిలో తీర్పు వచ్చింది?\n(How many judges and what was the majority in Kesavananda Bharati 1973?)",
     "9 న్యాయమూర్తులు — 6:3 మెజారిటీ / 9 judges — 6:3 majority",
     "11 న్యాయమూర్తులు — 8:3 మెజారిటీ / 11 judges — 8:3 majority",
     "13 న్యాయమూర్తులు — 7:6 మెజారిటీ / 13 judges — 7:6 majority",
     "7 న్యాయమూర్తులు — 4:3 మెజారిటీ / 7 judges — 4:3 majority",
     "c",
     "కేశవానంద భారతి 1973: భారత రాజ్యాంగ చరిత్రలో అత్యంత పెద్ద ధర్మాసనం — 13 న్యాయమూర్తులు (CJ Sikri తో పాటు 12 మంది). 7:6 అతి సన్నిహిత మెజారిటీతో మూల నిర్మాణ సిద్ధాంతం స్థాపించారు. 68 రోజులు విచారణ జరిపారు.\nKesavananda Bharati 1973: Largest bench in Indian constitutional history — 13 judges (CJ Sikri + 12). Established Basic Structure doctrine by razor-thin 7:6 majority. Heard for 68 days.",
     "APPSC"),

    (1, 2,
     "కేశవానంద భారతి కేసులో SC ఏ ముఖ్యమైన నిర్ణయం తీసుకుంది?\n(What was the key ruling of the SC in Kesavananda Bharati case?)",
     "పార్లమెంట్ రాజ్యాంగంలో ఏ నిబంధనను అయినా సవరించవచ్చు — గోలక్‌నాథ్ సమర్థించారు / Parliament can amend any provision — upheld Golaknath",
     "పార్లమెంట్ రాజ్యాంగంలో ఏ నిబంధనను అయినా సవరించవచ్చు — కానీ మూల నిర్మాణాన్ని నాశనం చేయలేదు / Parliament can amend any provision — but cannot destroy Basic Structure",
     "పార్లమెంట్ FRs సవరించలేదు / Parliament cannot amend FRs",
     "Art 368 రద్దు చేశారు / Art 368 was struck down",
     "b",
     "కేశవానంద భారతి 1973 తీర్పు (7:6): గోలక్‌నాథ్ రద్దు చేశారు — పార్లమెంట్ FRs సహా ఏ నిబంధనను అయినా సవరించవచ్చు. కానీ కీలక పరిమితి: రాజ్యాంగ 'మూల నిర్మాణం' (Basic Structure) ని నాశనం చేయలేరు. ఇదే ప్రపంచంలో అతి ముఖ్యమైన రాజ్యాంగ తీర్పులలో ఒకటి.\nKesavananda Bharati 1973 (7:6): Overruled Golaknath — Parliament can amend any provision including FRs. BUT critical limitation: cannot destroy Basic Structure of the Constitution. One of the most important constitutional judgments in the world.",
     "APPSC"),

    (1, 2,
     "కేశవానంద భారతి కేసులో Chief Justice ఎవరు? తీర్పు తర్వాత ఏమి జరిగింది?\n(Who was CJ in Kesavananda Bharati? What happened after the judgment?)",
     "CJ P.B. Gajendragadkar; తర్వాత న్యాయ సమీక్ష రద్దు చేశారు / CJ Gajendragadkar; later judicial review was abolished",
     "CJ S.M. Sikri; ఆ రోజే పదవీ విరమణ చేశారు; ఇందిరా గాంధీ 3 సీనియర్ న్యాయమూర్తులను దాటి A.N. Ray ని CJ గా నియమించింది / CJ Sikri; retired the same day; Indira Gandhi superseded 3 senior judges appointing A.N. Ray as CJ",
     "CJ A.N. Ray; Collegium పద్ధతి ప్రారంభించారు / CJ A.N. Ray; Collegium system was introduced",
     "CJ Y.V. Chandrachud; 44వ సవరణ ఆమోదించారు / CJ Chandrachud; 44th Amendment was passed",
     "b",
     "CJ S.M. Sikri 1973 ఏప్రిల్ 24న పదవీ విరమణ చేశారు — కేశవానంద తీర్పు రోజే. ఆ తర్వాత ఇందిరా గాంధీ ప్రభుత్వం 3 సీనియర్ న్యాయమూర్తులను (Shelat, Grover, Hegde) దాటవేసి A.N. Ray ని నేరుగా CJ గా నియమించారు. ఇది న్యాయ స్వాతంత్ర్యంపై వివాదం సృష్టించింది.\nCJ S.M. Sikri retired on April 24, 1973 — the very day of Kesavananda judgment. Indira Gandhi's govt superseded 3 senior judges (Shelat, Grover, Hegde — all in majority) and appointed A.N. Ray directly as CJ, sparking judicial independence controversy."),

    (1, 2,
     "కేశవానంద కేసులో Art 31C (25వ సవరణ) పై SC ఏమి నిర్ణయించింది?\n(What did SC decide about Art 31C in Kesavananda case?)",
     "Art 31C పూర్తిగా చెల్లుబాటు / Art 31C fully valid",
     "Art 31C పూర్తిగా రద్దు / Art 31C completely struck down",
     "DPSP అమలు భాగం వర్తిస్తుంది కానీ న్యాయ సమీక్ష నిరాకరించే భాగం రద్దు / DPSP implementation part upheld but part excluding judicial review struck down",
     "Art 31C కేవలం ఆర్థిక చట్టాలకు మాత్రమే వర్తిస్తుంది / Art 31C applies only to economic laws",
     "c",
     "కేశవానంద కేసులో Art 31C: DPSPs (Art 39b, c) అమలు చేసే చట్టాలు Art 14, 19 ల ఉల్లంఘన ఎదుర్కోవు — ఈ భాగం చెల్లుబాటు. కానీ 'ఆ చట్టాలు DPSP అమలు చేస్తున్నాయని ప్రకటన తుది నిర్ణయం' — న్యాయ సమీక్ష తొలగించే భాగం రద్దు — BS ఉల్లంఘన.\nOn Art 31C in Kesavananda: Part protecting DPSP-implementing laws from Art 14/19 challenge = valid. But part making parliamentary declaration final (ousting judicial review) = struck down as violating Basic Structure."),

    (1, 2,
     "కేశవానంద కేసు తర్వాత 1975లో CJ A.N. Ray ఏమి చేయడానికి ప్రయత్నించారు?\n(What did CJ A.N. Ray attempt to do in 1975 after Kesavananda?)",
     "కేశవానంద తీర్పును విస్తరించారు / Extended the Kesavananda judgment",
     "Minerva Mills కేసు విచారించారు / Heard the Minerva Mills case",
     "కేశవానంద తీర్పును తిప్పికొట్టేందుకు 13 న్యాయమూర్తుల ధర్మాసనం ఏర్పాటు చేశారు — కానీ ఒక రోజులోనే రద్దు అయింది / Constituted a 13-judge bench to overrule Kesavananda — but it dissolved within a day",
     "NJAC చట్టం ప్రవేశపెట్టారు / Introduced the NJAC law",
     "c",
     "1975 నవంబర్‌లో CJ A.N. Ray కేశవానంద తీర్పును తిప్పికొట్టేందుకు 13 న్యాయమూర్తుల ధర్మాసనం ఏర్పాటు చేశారు. కానీ ధర్మాసనం ఒక రోజులోనే రద్దు అయింది — ఏ హేతుపూర్వక కారణం ఇవ్వకుండా. కేశవానంద సిద్ధాంతం బలంగా నిలబడిందని నిరూపించింది.\nIn November 1975, CJ A.N. Ray constituted a 13-judge bench to overrule Kesavananda. But the bench dissolved within a single day without any reasoned order — proving the durability of the Kesavananda doctrine.",
     "APPSC"),

    (1, 3,
     "కేశవానంద భారతి కేసు అసలు ఏ విషయం గురించి?\n(What was the original subject matter of Kesavananda Bharati case?)",
     "మతస్వాతంత్ర్యం / Freedom of religion",
     "కేరళ భూ సంస్కరణ చట్టం కింద Edneer Mutt ఆస్తి స్వాధీనత / Acquisition of Edneer Mutt property under Kerala Land Reform Act",
     "ప్రాథమిక విద్యా హక్కు / Right to elementary education",
     "OBC రిజర్వేషన్ విధానం / OBC reservation policy",
     "b",
     "కేశవానంద భారతి కేరళలోని 'Edneer Mutt' హిందూ మఠ పీఠాధిపతి. కేరళ భూ సంస్కరణ (సవరణ) చట్టం 1969 మఠ ఆస్తులను ప్రభావితం చేసింది. ఆయన Art 25, 26 (మత స్వాతంత్ర్యం), Art 14, 19 (సంపత్తి హక్కు) ఉల్లంఘన పేర్చి SC వెళ్ళారు. ఇది తర్వాత రాజ్యాంగ చరిత్రలో అతి ముఖ్యమైన కేసుగా అభివృద్ధి చెందింది.\nKesavananda Bharati was the head of Edneer Mutt in Kerala. Kerala Land Reform (Amendment) Act 1969 affected the Mutt's properties. He approached SC citing violations of Arts 25, 26 and Arts 14, 19. The case grew into the most significant constitutional case in Indian history."),

    (1, 3,
     "కేశవానంద కేసులో మొదటగా మూల నిర్మాణంలో ఉన్నాయని పేర్కొన్న ముఖ్య అంశాలు ఏవి?\n(Which key elements were first identified as Basic Structure in Kesavananda 1973?)",
     "రాజ్యాంగ ఆధిపత్యం, గణతంత్ర-ప్రజాస్వామ్య రూపం, లౌకికత, వేర్పాటు అధికారాలు, FRs / Supremacy of Constitution, Republican-Democratic form, Secularism, Separation of Powers, FRs",
     "ఏకీభవ సార్వభౌమత్వం మాత్రమే / Federal sovereignty only",
     "Arts 14, 19, 21 మాత్రమే / Only Arts 14, 19, 21",
     "చట్ట పరిపాలన మాత్రమే / Rule of Law only",
     "a",
     "కేశవానంద 1973లో వివిధ న్యాయమూర్తులు భిన్న అంశాలు పేర్కొన్నారు. సర్వాంగీణంగా: (1) రాజ్యాంగ ఆధిపత్యం; (2) సార్వభౌమ లౌకిక ప్రజాస్వామ్య గణతంత్ర రాజ్య స్వభావం; (3) లౌకికత; (4) అధికార వేర్పాటు; (5) FRs; (6) చట్ట పరిపాలన; (7) సమానత్వ సూత్రం.\nIn Kesavananda 1973, different judges identified different elements. Broadly: (1) Supremacy of Constitution; (2) Sovereign Democratic Republic character; (3) Secular character; (4) Separation of Powers; (5) FRs; (6) Rule of Law; (7) Principle of Equality."),

    # ══════════════ SECTION 2: ELEMENTS OF BASIC STRUCTURE (7 MCQs) ══════════════

    (2, 1,
     "కింది వాటిలో మూల నిర్మాణం (Basic Structure) కి చెందినవి ఏవి?\n(Which of the following are part of Basic Structure?)",
     "రాజ్యాంగ ఆధిపత్యం, లౌకికత, న్యాయ సమీక్ష, ప్రజాస్వామ్యం / Supremacy of Constitution, Secularism, Judicial Review, Democracy",
     "పంచాయతీ రాజ్, ఆస్తి హక్కు, DPSP లు, OBC రిజర్వేషన్లు / Panchayati Raj, Property Right, DPSPs, OBC Reservations",
     "విద్యా హక్కు, పర్యావరణ రక్షణ, అన్ని FRs / Right to Education, Environment, All FRs",
     "ఒకటవ షెడ్యూల్, రెండవ షెడ్యూల్, పదవ షెడ్యూల్ / 1st Schedule, 2nd Schedule, 10th Schedule",
     "a",
     "SC గుర్తించిన మూల నిర్మాణ అంశాలు (సమగ్ర జాబితా కాదు): (1) రాజ్యాంగ ఆధిపత్యం; (2) లౌకికత; (3) న్యాయ సమీక్ష; (4) ప్రజాస్వామ్యం; (5) సార్వభౌమత; (6) గణతంత్ర రాజ్య స్వభావం; (7) సమాఖ్య స్వభావం; (8) న్యాయ స్వాతంత్ర్యం; (9) అధికార వేర్పాటు; (10) పార్లమెంటరీ పద్ధతి.\nSC-identified Basic Structure elements (not exhaustive): Supremacy of Constitution, Secularism, Judicial Review, Democracy, Sovereignty, Republican character, Federal character, Judicial Independence, Separation of Powers, Parliamentary form.",
     "APPSC"),

    (2, 2,
     "SR బొమ్మై v. భారత యూనియన్ (1994) కేసులో మూల నిర్మాణంలో ఏ అంశం స్థాపించారు?\n(Which BS element was firmly established in SR Bommai v. Union of India 1994?)",
     "న్యాయ సమీక్ష / Judicial Review",
     "లౌకికత (Secularism) — లౌకికేతర రాష్ట్ర ప్రభుత్వాలను రద్దు చేయడానికి Art 356 వాడవచ్చు / Secularism — Art 356 can be used to dismiss anti-secular state governments",
     "సమాఖ్య స్వభావం / Federal character",
     "చట్ట పరిపాలన / Rule of Law",
     "b",
     "SR బొమ్మై 1994: 9 న్యాయమూర్తుల ధర్మాసనం — 'లౌకికత' (Secularism) మూల నిర్మాణంలో భాగమని స్థాపించింది. ఒక రాష్ట్ర ప్రభుత్వం లౌకికత వ్యతిరేక విధానాలు అనుసరిస్తే Art 356 కింద రద్దు చేయవచ్చని నిర్ణయించింది. అయోధ్య వివాద నేపథ్యంలో వచ్చిన కేసు.\nSR Bommai 1994: 9-judge bench firmly established 'Secularism' as Basic Structure. A state government pursuing anti-secular policies can be dismissed under Art 356. Case came in context of Ayodhya dispute."),

    (2, 2,
     "L. చంద్రకుమార్ v. భారత యూనియన్ (1997) కేసు BS సిద్ధాంతానికి ఏ అంశం జోడించింది?\n(What did L. Chandra Kumar v. Union of India 1997 add to BS doctrine?)",
     "లౌకికత పెంపు / Enhancement of Secularism",
     "HC మరియు SC యొక్క న్యాయ సమీక్ష అధికారాలు BS లో భాగం — ట్రిబ్యునళ్ళు వీటిని తొలగించలేవు / Judicial review powers of HC and SC are Basic Structure — cannot be ousted by legislative tribunals",
     "రాష్ట్రపతి ప్రత్యక్ష ఎన్నిక / Direct election of President",
     "పార్లమెంట్ సవరణ అధికారం బలోపేతం / Strengthening Parliament's amending power",
     "b",
     "L. చంద్రకుమార్ 1997: 7 న్యాయమూర్తుల ధర్మాసనం — HC మరియు SC యొక్క న్యాయ సమీక్ష అధికారాలు 'రాజ్యాంగ పరిహార అంగ' స్వభావంలో BS లో భాగం. Administrative Tribunals Act కింద ఏర్పడిన ట్రిబ్యునళ్ళు SC/HC యొక్క న్యాయ సమీక్షను తొలగించలేవు.\nL. Chandra Kumar 1997: 7-judge bench — Judicial review powers of HC/SC are part of Basic Structure as essential remedial organs. Tribunals under Administrative Tribunals Act cannot oust SC/HC's judicial review jurisdiction."),

    (2, 2,
     "పార్లమెంటరీ పద్ధతి ప్రభుత్వం (Parliamentary System of Government) మూల నిర్మాణంలో భాగమని ఏ కేసు నిర్ణయించింది?\n(Which case determined Parliamentary form of government is part of Basic Structure?)",
     "IR Coelho v. State of Tamil Nadu 2007",
     "Kesavananda Bharati v. State of Kerala 1973",
     "Indira Nehru Gandhi v. Raj Narain 1975",
     "SR Bommai v. Union of India 1994",
     "c",
     "ఇంద్రా నెహ్రూ గాంధీ v. రాజ్ నారాయణ్ 1975: SC: ప్రజాస్వామ్యం, స్వేచ్ఛా న్యాయమైన ఎన్నికలు, మరియు 'పార్లమెంటరీ పద్ధతి ప్రభుత్వం' మూల నిర్మాణంలో భాగమని నిర్ణయించింది. 39వ సవరణ (ఎన్నికల వివాదాలను న్యాయ సమీక్ష నుండి తొలగించింది) రద్దు చేశారు.\nIndira Nehru Gandhi v. Raj Narain 1975: SC: Democracy, free & fair elections, and 'Parliamentary form of government' are Basic Structure. 39th Amendment (removing election disputes from judicial review) struck down."),

    (2, 3,
     "NJAC కేసు (2015) లో 99వ రాజ్యాంగ సవరణ రద్దు చేసిన BS ఏమిటి?\n(On what Basic Structure ground did SC strike down 99th Amendment in NJAC case 2015?)",
     "సమాఖ్య స్వభావం ఉల్లంఘన / Violation of Federal character",
     "లౌకికత ఉల్లంఘన / Violation of Secularism",
     "న్యాయ స్వాతంత్ర్యం ఉల్లంఘన / Violation of Independence of Judiciary",
     "ప్రాథమిక హక్కుల ఉల్లంఘన / Violation of Fundamental Rights",
     "c",
     "NJAC కేసు 2015 (5 న్యాయమూర్తులు, 4:1 మెజారిటీ): NJAC ద్వారా కార్యనిర్వాహక సభ్యులు న్యాయమూర్తి నియామకాలలో పాల్గొంటారు — ఇది న్యాయ స్వాతంత్ర్యాన్ని దెబ్బతీస్తుంది, అది BS కి వ్యతిరేకం. 'Collegium' పద్ధతి పునరుద్ధరించారు.\nNJAC case 2015 (5 judges, 4:1 majority): NJAC allowed executive members in judicial appointments — damages Independence of Judiciary, violating Basic Structure. Collegium system restored.",
     "APPSC"),

    (2, 3,
     "ఇంద్రా సాహ్నీ కేసు 1992 (మండల్ కమీషన్) BS సిద్ధాంతానికి ఏ అంశం జోడించింది?\n(What Basic Structure element did Indra Sawhney 1992 reinforce?)",
     "న్యాయ స్వాతంత్ర్యం / Judicial Independence",
     "రిజర్వేషన్లు 50% మించరాదు — సమానత్వ సూత్రం BS అంశం / Reservations must not exceed 50% — Equality principle is BS element",
     "లౌకికత / Secularism",
     "ప్రజాస్వామ్య ఓటు హక్కు / Democratic right to vote",
     "b",
     "ఇంద్రా సాహ్నీ 1992 (9 న్యాయమూర్తులు): OBC రిజర్వేషన్లు (27%) చెల్లుబాటు. రిజర్వేషన్లు మొత్తం 50% దాటరాదు — ఇది Equality Principle ని (BS అంశం) పాటించడానికి. Creamy Layer తొలగింపు తప్పనిసరి.\nIndra Sawhney 1992 (9 judges): OBC reservations (27%) valid. Total reservations must not exceed 50% — to maintain Equality as Basic Structure element. Creamy layer exclusion mandated."),

    (2, 3,
     "మూల నిర్మాణంలో 'అధికార వేర్పాటు' (Separation of Powers) ఏ కేసులో స్థాపించబడింది?\n(Through which case was 'Separation of Powers' established as Basic Structure?)",
     "Kesavananda Bharati v. State of Kerala 1973",
     "Minerva Mills v. UOI 1980",
     "Indira Nehru Gandhi v. Raj Narain 1975",
     "Waman Rao v. UOI 1981",
     "c",
     "ఇంద్రా గాంధీ v. రాజ్ నారాయణ్ 1975 కేసులో SC 'అధికార వేర్పాటు' (Separation of Powers) మూల నిర్మాణంలో భాగమని స్థాపించింది. 39వ సవరణ కింద పార్లమెంట్ న్యాయవ్యవస్థ అధికారాన్ని తొలగించడానికి ప్రయత్నించింది — ఇది BS ఉల్లంఘన అని SC నిర్ణయించింది.\nIndira Gandhi v. Raj Narain 1975: SC established 'Separation of Powers' as Basic Structure. The 39th Amendment tried to remove judicial sphere powers — SC held this violated Basic Structure.",
     "APPSC"),

    # ══════════════ SECTION 3: POST-KESAVANANDA CASES (8 MCQs) ══════════════

    (3, 1,
     "Minerva Mills v. భారత యూనియన్ (1980) కేసులో SC ఏమి నిర్ణయించింది?\n(What did SC decide in Minerva Mills v. Union of India 1980?)",
     "42వ సవరణ యొక్క Art 368(4) మరియు (5) రద్దు చేశారు / Art 368(4) & (5) of 42nd Amendment struck down",
     "42వ సవరణ పూర్తిగా చెల్లుబాటు / 42nd Amendment fully valid",
     "DPSP లు FRs కి ప్రాధాన్యత పొందాయి / DPSPs get priority over FRs",
     "Kesavananda తీర్పు రద్దు చేశారు / Kesavananda judgment overruled",
     "a",
     "Minerva Mills 1980: 42వ సవరణ యొక్క Art 368(4) ('SC న్యాయ సమీక్ష రాజ్యాంగ సవరణలకు వర్తించదు') మరియు Art 368(5) ('పార్లమెంట్ సవరణ అధికారానికి పరిమితి లేదు') రద్దు చేశారు. Kesavananda ని సమర్థించారు. FRs మరియు DPSPs మధ్య సమతుల్యత BS అని నిర్ణయించారు.\nMinerva Mills 1980: Struck down Art 368(4) ('no judicial review for constitutional amendments') and Art 368(5) ('no limitation on Parliament's amending power') of 42nd Amendment. Reaffirmed Kesavananda. Balance between FRs and DPSPs is itself Basic Structure.",
     "APPSC"),

    (3, 1,
     "వామన్ రావు v. భారత యూనియన్ (1981) కేసు ఏ ముఖ్యమైన నిర్ణయం ఇచ్చింది?\n(What important ruling did Waman Rao v. Union of India 1981 give?)",
     "9వ షెడ్యూల్‌లో కేశవానంద తర్వాత చేర్చిన చట్టాలు న్యాయ సమీక్షకు లోబడతాయి / Laws added to 9th Schedule after Kesavananda are subject to judicial review",
     "9వ షెడ్యూల్‌లో చట్టాలు ఎప్పుడూ న్యాయ సమీక్షకు లోబడవు / Laws in 9th Schedule are never subject to judicial review",
     "9వ షెడ్యూల్ మొత్తం రద్దు / Entire 9th Schedule struck down",
     "9వ షెడ్యూల్ కేవలం కేంద్ర చట్టాలకే వర్తిస్తుంది / 9th Schedule applies only to central laws",
     "a",
     "వామన్ రావు 1981: కేశవానంద తీర్పు 24 ఏప్రిల్ 1973 తర్వాత 9వ షెడ్యూల్‌కు చేర్చిన చట్టాలు న్యాయ సమీక్షకు లోబడతాయి అని నిర్ణయించింది. అంతకు ముందు చేర్చిన చట్టాలు రక్షితంగా ఉంటాయి. ఇది తర్వాత IR Coelho 2007 లో మరింత స్పష్టం అయింది.\nWaman Rao 1981: Laws added to 9th Schedule AFTER April 24, 1973 (Kesavananda date) are subject to judicial review if they violate Basic Structure. Laws added before that date remain protected. Further elaborated in IR Coelho 2007."),

    (3, 2,
     "IR Coelho v. తమిళనాడు రాష్ట్రం (2007) లో 9 న్యాయమూర్తులు ఏమి నిర్ణయించారు?\n(What did 9 judges decide in IR Coelho v. State of Tamil Nadu 2007?)",
     "9వ షెడ్యూల్ పూర్తిగా రద్దు / 9th Schedule completely struck down",
     "కేశవానంద తర్వాత 9వ షెడ్యూల్‌కు చేర్చిన చట్టాలు Art 14, 19, 20, 21 లేదా BS ఉల్లంఘిస్తే న్యాయ సమీక్షకు లోబడతాయి / 9th Schedule laws added after Kesavananda subject to review if violating Arts 14,19,20,21 or BS",
     "9వ షెడ్యూల్ కేవలం భూ సంస్కరణ చట్టాలకే వర్తిస్తుంది / 9th Schedule applies only to land reform laws",
     "9వ షెడ్యూల్ చట్టాలు ఎప్పటికీ న్యాయ సమీక్షకు లోబడవు / 9th Schedule laws never subject to judicial review",
     "b",
     "IR Coelho 2007: 9 న్యాయమూర్తుల ధర్మాసనం — వామన్ రావు నిర్ణయాన్ని సమర్థించారు. కేశవానంద తర్వాత 9వ షెడ్యూల్‌కు చేర్చిన చట్టాలు (1) Art 14, 19, 20, 21 లేదా (2) BS ఉల్లంఘిస్తే న్యాయ సమీక్షకు లోబడతాయి. 9వ షెడ్యూల్‌కు రాజ్యాంగ రక్షణ 'అసంతత' (absolute) కాదు.\nIR Coelho 2007: 9-judge bench reaffirmed Waman Rao. Laws added to 9th Schedule after Kesavananda subject to judicial review if violating Arts 14, 19, 20, 21 or Basic Structure. 9th Schedule protection is NOT absolute."),

    (3, 2,
     "ఇంద్రా నెహ్రూ గాంధీ v. రాజ్ నారాయణ్ (1975) కేసులో SC ఏ రాజ్యాంగ సవరణ రద్దు చేసింది?\n(Which amendment did SC strike down in Indira Nehru Gandhi v. Raj Narain 1975?)",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "44వ సవరణ 1978 / 44th Amendment 1978",
     "39వ సవరణ 1975 / 39th Amendment 1975",
     "25వ సవరణ 1971 / 25th Amendment 1971",
     "c",
     "39వ సవరణ 1975: ప్రధానమంత్రి, రాష్ట్రపతి, ఉపరాష్ట్రపతి, లోక్‌సభ స్పీకర్ ఎన్నికల వివాదాలను న్యాయ సమీక్ష నుండి తొలగించింది. SC ఈ సవరణ BS ఉల్లంఘిస్తుందని రద్దు చేసింది — ప్రజాస్వామ్యం, స్వేచ్ఛా ఎన్నికలు, న్యాయ సమీక్ష BS అంశాలు.\n39th Amendment 1975: Placed PM, President, VP and Speaker's election disputes beyond judicial review. SC struck it down as violating Basic Structure — Democracy, Free & Fair Elections, and Judicial Review are BS elements.",
     "APPSC"),

    (3, 2,
     "SR బొమ్మై కేసు మూల నిర్మాణ సిద్ధాంతాన్ని Art 356 కి ఏ విధంగా వర్తింపజేసింది?\n(How did SR Bommai case apply BS doctrine to Art 356?)",
     "Art 356 మూల నిర్మాణంలో భాగమని నిర్ణయించింది / Art 356 is part of Basic Structure",
     "Art 356 కింద రాష్ట్ర ప్రభుత్వాల రద్దు న్యాయ సమీక్షకు లోబడుతుందని నిర్ణయించింది; లౌకికేతర రాష్ట్రాలను రద్దు చేయవచ్చు / Dismissal under Art 356 is judicially reviewable; anti-secular state govts can be dismissed",
     "Art 356 పూర్తిగా రద్దు చేశారు / Art 356 was completely struck down",
     "Art 356 వాడకం BS ఉల్లంఘించదు అని నిర్ణయించింది / Use of Art 356 never violates Basic Structure",
     "b",
     "SR బొమ్మై 1994 (9 న్యాయమూర్తులు): Art 356 కింద రాష్ట్ర ప్రభుత్వాల రద్దు న్యాయ సమీక్షకు లోబడుతుందని నిర్ణయించింది. లౌకికత మూల నిర్మాణంలో భాగం కాబట్టి లౌకికేతర రాష్ట్రాలను రద్దు చేయవచ్చు. భారత సమాఖ్య స్వభావం BS లో భాగమని బలపరచారు.\nSR Bommai 1994 (9 judges): Art 356 dismissal of state governments is judicially reviewable. Since Secularism is Basic Structure, anti-secular state govts can be dismissed. Strengthened Federal character as part of Basic Structure."),

    (3, 3,
     "SP గుప్త (1981 - First Judges Case) మరియు Second Judges Case (1993) ల మధ్య ముఖ్య తేడా ఏమిటి?\n(Key difference between SP Gupta 1981 and Second Judges Case 1993?)",
     "రెండూ executive primacy ని ఒప్పుకున్నాయి / Both endorsed executive primacy",
     "First Judges: కార్యనిర్వాహక ఆధిక్యత. Second Judges: CJI Collegium సిఫారసు కట్టుబడి ఉంది / First Judges: executive primacy. Second Judges: CJI Collegium recommendation binding",
     "రెండూ Collegium పద్ధతి ఒప్పుకున్నాయి / Both endorsed Collegium",
     "రెండూ NJAC పద్ధతి ఒప్పుకున్నాయి / Both endorsed NJAC",
     "b",
     "First Judges Case 1981 (SP Gupta, 7 judges): కార్యనిర్వాహక నిర్ణయమే ఆఖరు — CJI సలహా కట్టుబడి ఉండదు. Second Judges Case 1993 (9 judges): First Judges రద్దు — CJI నేతృత్వంలో Senior Judges Collegium సిఫారసు కార్యనిర్వాహకులకు కట్టుబడి ఉంటుంది. న్యాయ స్వాతంత్ర్యం BS అని నిర్ణయించింది.\nFirst Judges Case 1981: Executive decision final — CJI advice not binding. Second Judges Case 1993: Overruled First Judges — CJI-led Collegium's recommendation is binding on executive. Established judicial independence as Basic Structure."),

    (3, 3,
     "కేశవానంద తర్వాత వచ్చిన ప్రధాన BS కేసుల క్రమం ఏది సరైనది?\n(Correct sequence of major post-Kesavananda BS cases?)",
     "Minerva Mills → Indira Gandhi → Waman Rao → SR Bommai → NJAC",
     "Indira Gandhi (1975) → Minerva Mills (1980) → Waman Rao (1981) → SR Bommai (1994) → IR Coelho (2007) → NJAC (2015)",
     "Waman Rao → Indira Gandhi → SR Bommai → Minerva Mills → NJAC",
     "SR Bommai → Minerva Mills → NJAC → Waman Rao → Indira Gandhi",
     "b",
     "సరైన కాలక్రమం: (1) ఇంద్రా గాంధీ 1975 (39వ సవరణ రద్దు); (2) Minerva Mills 1980 (42వ సవరణ Art 368(4)(5) రద్దు); (3) వామన్ రావు 1981 (9వ షెడ్యూల్ సమీక్ష); (4) SR Bommai 1994 (లౌకికత BS); (5) IR Coelho 2007 (9వ షెడ్యూల్ విస్తృత సమీక్ష); (6) NJAC 2015 (న్యాయ స్వాతంత్ర్యం BS).\nCorrect sequence: Indira Gandhi 1975 → Minerva Mills 1980 → Waman Rao 1981 → SR Bommai 1994 → IR Coelho 2007 → NJAC 2015.",
     "APPSC"),

    # ══════════════ SECTION 4: 42ND AMENDMENT & BASIC STRUCTURE (5 MCQs) ══════════════

    (4, 1,
     "42వ రాజ్యాంగ సవరణ 1976 Art 368 లో ఏ రెండు నిబంధనలు జోడించింది?\n(Which two provisions did the 42nd Amendment 1976 add to Art 368?)",
     "Art 368(1) మరియు Art 368(2) / Art 368(1) and Art 368(2)",
     "Art 368(3) మరియు Art 368(4) / Art 368(3) and Art 368(4)",
     "Art 368(4) మరియు Art 368(5) / Art 368(4) and Art 368(5)",
     "Art 368(6) మరియు Art 368(7) / Art 368(6) and Art 368(7)",
     "c",
     "42వ సవరణ 1976: Art 368 కి రెండు నిబంధనలు జోడించింది: Art 368(4) — రాజ్యాంగ సవరణలకు ఎటువంటి న్యాయ సమీక్ష లేదు; Art 368(5) — పార్లమెంట్ సవరణ అధికారానికి ఎటువంటి పరిమితి లేదు. ఇవి రెండూ Minerva Mills 1980 లో రద్దు అయ్యాయి.\n42nd Amendment 1976 added two provisions to Art 368: Art 368(4) — No judicial review of constitutional amendments; Art 368(5) — No limitation on Parliament's amending power. Both were struck down in Minerva Mills 1980."),

    (4, 2,
     "42వ సవరణ 1976 Art 31C ని ఏ విధంగా విస్తరించింది?\n(How did the 42nd Amendment 1976 expand Art 31C?)",
     "Art 31C ని పూర్తిగా రద్దు చేసింది / Completely removed Art 31C",
     "Art 31C రక్షణని Art 39(b)(c) నుండి అన్ని DPSPs కి విస్తరించింది / Extended Art 31C protection from Art 39(b)(c) to ALL DPSPs",
     "Art 31C ని అన్ని FRs కి వర్తింపజేసింది / Applied Art 31C to all FRs",
     "Art 31C రక్షణని కేవలం రాష్ట్ర చట్టాలకు పరిమితం చేసింది / Limited Art 31C protection only to state laws",
     "b",
     "25వ సవరణ 1971: Art 31C కేవలం Art 39(b)(c) DPSPs కోసం. 42వ సవరణ 1976: Art 31C ని అన్ని DPSP ల కోసం విస్తరించింది. Minerva Mills 1980 లో: 42వ సవరణ విస్తరణ రద్దు — 25వ సవరణ యొక్క అసలు Art 31C చెల్లుబాటు.\n25th Amendment 1971: Art 31C only for Art 39(b)(c). 42nd Amendment 1976: Extended Art 31C to ALL DPSPs. Minerva Mills 1980: 42nd Amendment's extension struck down — original Art 31C from 25th Amendment valid."),

    (4, 2,
     "Minerva Mills 1980 లో FRs మరియు DPSPs మధ్య సంబంధం గురించి SC ఏమి పేర్కొంది?\n(What did SC say about FRs and DPSPs in Minerva Mills 1980?)",
     "DPSPs ఎల్లప్పుడూ FRs కి ప్రాధాన్యత పొందుతాయి / DPSPs always prevail over FRs",
     "FRs ఎల్లప్పుడూ DPSPs కి ప్రాధాన్యత పొందుతాయి / FRs always prevail over DPSPs",
     "FRs మరియు DPSPs మధ్య సమతుల్యత (harmony) మూల నిర్మాణంలో భాగం / Balance between FRs and DPSPs is Basic Structure",
     "FRs మరియు DPSPs ఒక్కటే — భేదం లేదు / FRs and DPSPs are the same",
     "c",
     "Minerva Mills 1980: FRs మరియు DPSPs పరిపూరకమైనవి (complementary) — 'golden triangle' (Art 14, 19, 21) మరియు DPSPs మధ్య సమతుల్యత స్వయంగా BS లో భాగం. 42వ సవరణ DPSPs ని FRs పై ఉంచడం ద్వారా ఈ సమతుల్యతను దెబ్బతీయడం BS ఉల్లంఘన.\nMinerva Mills 1980: FRs and DPSPs are complementary. Balance between 'golden triangle' (Arts 14, 19, 21) and DPSPs is itself Basic Structure. 42nd Amendment's subordination of FRs violated this balance — hence struck down."),

    (4, 2,
     "44వ రాజ్యాంగ సవరణ 1978 42వ సవరణ యొక్క ఏ మార్పులు చేసింది?\n(What key changes did 44th Amendment 1978 make?)",
     "ప్రస్తావన నుండి 'Socialist' మరియు 'Secular' తొలగించింది / Removed 'Socialist' and 'Secular' from Preamble",
     "Art 368(4)(5) రద్దు చేసింది / Struck down Art 368(4) and (5)",
     "ఆస్తి హక్కు FR నుండి తొలగించి Art 300A చేసింది; Emergency నిబంధనలు సవరించింది; Art 20, 21 Emergency లో అమలులో ఉంటాయని నిర్ధారించింది / Property right removed from FRs → Art 300A; Emergency provisions changed; Arts 20, 21 cannot be suspended in Emergency",
     "అన్ని 42వ సవరణ మార్పులు పూర్తిగా రద్దు / All 42nd Amendment changes fully reversed",
     "c",
     "44వ సవరణ 1978 (జనతా ప్రభుత్వం): (1) ఆస్తి హక్కు (Art 19(1)(f) + Art 31) FR నుండి తొలగించి Art 300A కింద చట్టపరమైన హక్కుగా చేసింది; (2) Art 352 — 'Armed Rebellion' పదం; (3) Art 20, 21 Emergency లో కూడా suspend అవ్వవు అని స్పష్టం చేసింది; (4) అనేక Emergency దుర్వినియోగ నిరోధక మార్పులు చేసింది.\n44th Amendment 1978 (Janata Govt): (1) Property right removed from FRs → Art 300A legal right; (2) Art 352 → 'Armed Rebellion'; (3) Arts 20 & 21 cannot be suspended in Emergency; (4) Various safeguards against Emergency abuse.",
     "APPSC"),

    (4, 3,
     "42వ సవరణ (1976) ని 'Mini Constitution' అని ఎందుకు అంటారు?\n(Why is the 42nd Amendment called 'Mini Constitution'?)",
     "అది కేవలం ప్రస్తావన సవరించింది / It only amended the Preamble",
     "అది 59 సవరణలు చేసి రాజ్యాంగంలో విస్తృత మార్పులు చేసి పార్లమెంట్ ఆధిపత్యాన్ని గరిష్ట స్థాయికి తీసుకువెళ్ళింది / It made 59 amendments with sweeping changes and maximized parliamentary supremacy",
     "అది 42 FR లు ప్రవేశపెట్టింది / It introduced 42 Fundamental Rights",
     "అది 42 DPSP లు ప్రవేశపెట్టింది / It introduced 42 DPSPs",
     "b",
     "42వ సవరణ 1976 (అత్యవసర కాలంలో): రాజ్యాంగంలో 59 సవరణలు: (1) 'Socialist', 'Secular', 'Integrity' ప్రస్తావనలో చేర్చింది; (2) Art 368(4)(5) ద్వారా పార్లమెంట్ అపరిమిత సవరణ అధికారం; (3) FRs పై DPSPs ఆధిక్యత; (4) పార్లమెంట్ పదవి 6 సంవత్సరాలు. Minerva Mills 1980 లో అనేక భాగాలు రద్దు అయ్యాయి.\n42nd Amendment 1976 (during Emergency): Made 59 changes to Constitution: (1) Added Socialist/Secular/Integrity to Preamble; (2) Unlimited amending power via Art 368(4)(5); (3) DPSPs over FRs; (4) Parliament term 6 years. Many parts struck down in Minerva Mills 1980."),

    # ══════════════ SECTION 5: SCOPE AND APPLICATION (5 MCQs) ══════════════

    (5, 1,
     "మూల నిర్మాణ సిద్ధాంతం ఏ రకమైన చర్యలకు వర్తిస్తుంది?\n(To what type of actions does Basic Structure doctrine apply?)",
     "సాధారణ చట్టాలు మాత్రమే / Only ordinary legislation",
     "రాజ్యాంగ సవరణలు మాత్రమే / Only constitutional amendments",
     "రాష్ట్రపతి ఉత్తర్వులు మాత్రమే / Only Presidential orders",
     "అన్ని కార్యనిర్వాహక చర్యలు / All executive actions",
     "b",
     "మూల నిర్మాణ సిద్ధాంతం కేవలం రాజ్యాంగ సవరణలకు వర్తిస్తుంది — సాధారణ చట్టాలకు కాదు. సాధారణ చట్టాలు Art 13 కింద FR ఆధారంగా రద్దు అవుతాయి. రాజ్యాంగ సవరణలు BS ఉల్లంఘించినందుకు రద్దు అవుతాయి. ఇవి రెండు వేర్వేరు 'పరీక్షలు'.\nBasic Structure doctrine ONLY applies to constitutional amendments — NOT to ordinary legislation. Ordinary laws are struck down under Art 13 for FR violation. Constitutional amendments are struck down for BS violation. These are two separate tests.",
     "APPSC"),

    (5, 2,
     "మూల నిర్మాణ సిద్ధాంతం ఏ దేశ రాజ్యాంగ భావన నుండి స్ఫూర్తి పొందింది?\n(From which country's constitutional concept was Basic Structure doctrine inspired?)",
     "అమెరికా / USA",
     "యుకె / UK",
     "జర్మనీ (Grundnorm/Eternity Clause) / Germany (Grundnorm/Eternity Clause)",
     "ఆస్ట్రేలియా / Australia",
     "c",
     "జర్మనీ రాజ్యాంగంలో Article 79(3) — 'Eternity Clause' లేదా 'Grundnorm': కొన్ని ముఖ్యమైన నిబంధనలు (మానవ గౌరవం, ప్రజాస్వామ్యం, సమాఖ్య స్వభావం) సవరించడం నిషేధించింది. Justice Mudholkar (Sajjan Singh 1964 dissent) లో ఈ భావనను ప్రస్తావించారు, తర్వాత Kesavananda లో అభివృద్ధి చేశారు.\nGermany's Constitution Art 79(3) — 'Eternity Clause' or 'Grundnorm': Certain essential provisions (human dignity, democracy, federal character) unamendable. Justice Mudholkar referenced this in Sajjan Singh 1964 dissent, later developed in Kesavananda."),

    (5, 2,
     "రాజ్యాంగంలో మూల నిర్మాణ సిద్ధాంతం స్పష్టంగా రాసి ఉందా?\n(Is the Basic Structure doctrine explicitly written in the Constitution?)",
     "అవును — Art 368(3) లో / Yes — in Art 368(3)",
     "అవును — Art 13(1A) లో / Yes — in Art 13(1A)",
     "కాదు — ఇది న్యాయ వ్యాఖ్యాన ద్వారా అభివృద్ధి చేసిన జ్యూడిషియల్ సిద్ధాంతం / No — it is a judicial doctrine developed through judicial interpretation",
     "అవును — 9వ షెడ్యూల్‌లో జాబితా ఉంది / Yes — it is listed in the 9th Schedule",
     "c",
     "మూల నిర్మాణ సిద్ధాంతం రాజ్యాంగంలో ఎక్కడా స్పష్టంగా రాయబడలేదు. ఇది సుప్రీం కోర్టు న్యాయ వ్యాఖ్యానం (judicial interpretation) ద్వారా అభివృద్ధి చేసిన సిద్ధాంతం. కేశవానంద 1973 నుండి మొదలై అభివృద్ధి చెందుతూ వస్తోంది. జాబితా అసంపూర్ణం (evolving list).\nBasic Structure doctrine is nowhere explicitly written in the Constitution. It is a judicial doctrine developed through SC's interpretation, starting from Kesavananda 1973. The list is incomplete/evolving."),

    (5, 2,
     "మూల నిర్మాణ అంశాల జాబితా స్వభావం ఏమిటి?\n(What is the nature of the Basic Structure elements list?)",
     "పూర్తిగా నిర్ణాయకం — SC 1973 లో ఒకసారి జాబితా ఖరారు చేసింది / Completely definitive — finalized in 1973",
     "పార్లమెంట్ నిర్ణయిస్తుంది / Parliament decides",
     "అభివృద్ధి చెందుతున్న జాబితా — SC కేసు నుండి కేసుకు కొత్త అంశాలు గుర్తిస్తూ వస్తోంది / Evolving list — SC identifies new elements case by case",
     "రాజ్యాంగంలో ఖచ్చితంగా రాసి ఉంది / Precisely written in Constitution",
     "c",
     "మూల నిర్మాణ జాబితా 'evolving': Kesavananda 1973 మొదలైంది. Indira Gandhi 1975 — ప్రజాస్వామ్యం, స్వేచ్ఛా ఎన్నికలు, పార్లమెంటరీ పద్ధతి జోడించింది. SR Bommai 1994 — లౌకికత జోడించింది. NJAC 2015 — న్యాయ స్వాతంత్ర్యం నొక్కింది. ఇప్పటికీ కేసుల వారీగా SC నిర్ణయిస్తోంది.\nBasic Structure list is evolving: Kesavananda 1973 started. Indira Gandhi 1975 added Democracy/Free Elections/Parliamentary form. SR Bommai 1994 added Secularism. NJAC 2015 emphasized Judicial Independence. SC continues case-by-case."),

    (5, 3,
     "సార్వజనీన ఓటు హక్కు (Universal Adult Suffrage) మూల నిర్మాణంలో భాగమా?\n(Is Universal Adult Suffrage part of Basic Structure?)",
     "కాదు — ఇది పార్లమెంట్ చట్టం ద్వారా మార్చవచ్చు / No — can be changed by Parliament legislation",
     "అవును — Kesavananda 1973 లో ముఖ్యంగా పేర్కొనబడింది / Specifically mentioned in Kesavananda 1973",
     "అవును — 'స్వేచ్ఛా న్యాయమైన ఎన్నికలు' అనే BS అంశంలో భాగం (Indira Gandhi 1975 కేసు) / Yes — part of BS element 'Free and Fair Elections' (Indira Gandhi 1975)",
     "కాదు — ఎన్నికలు అన్నీ సాధారణ చట్టాల విషయం / No — elections are entirely ordinary law",
     "c",
     "ఇంద్రా గాంధీ v. రాజ్ నారాయణ్ 1975 కేసులో SC: 'Free and Fair Elections' మరియు 'Democratic form of government' BS లో భాగాలు. సార్వజనీన ఓటు హక్కు ప్రజాస్వామ్యానికి ఆధారం కాబట్టి BS లో భాగంగా పరిగణించవచ్చు. రాజ్యాంగ సవరణ ద్వారా ఈ హక్కు రద్దు చేయలేరు.\nIndira Gandhi v. Raj Narain 1975: 'Free and Fair Elections' and 'Democratic form' are Basic Structure. Universal Adult Suffrage is the foundation of democracy — hence part of Basic Structure. Cannot be abolished by constitutional amendment."),

    # ══════════════ SECTION 6: TOUGH MCQs (5 MCQs) ══════════════

    (6, 3,
     "మూల నిర్మాణ సిద్ధాంతం ఏ చర్యలకు వర్తించదు?\n(To which actions does Basic Structure doctrine NOT apply?)",
     "రాజ్యాంగ సవరణలకు / Constitutional amendments",
     "38వ సవరణ 1975 వంటి సవరణలకు / Amendments like 38th Amendment 1975",
     "సాధారణ చట్టాలకు, కార్యనిర్వాహక చర్యలకు / Ordinary legislation and executive actions",
     "9వ షెడ్యూల్ చట్టాలకు (కేశవానంద తర్వాత) / 9th Schedule laws (post-Kesavananda)",
     "c",
     "మూల నిర్మాణ సిద్ధాంతం కేవలం రాజ్యాంగ సవరణలకు వర్తిస్తుంది. సాధారణ చట్టాలకు Art 13 వర్తిస్తుంది (FR పరీక్ష). కార్యనిర్వాహక చర్యలకు FRs వర్తిస్తాయి. BS పరీక్ష ప్రత్యేకంగా Art 368 కింద రాజ్యాంగ సవరణలకు మాత్రమే.\nBasic Structure doctrine ONLY applies to constitutional amendments. For ordinary laws: Art 13 applies (FR test). For executive actions: FRs apply. BS test is specifically for constitutional amendments under Art 368.",
     "APPSC"),

    (6, 3,
     "మూల నిర్మాణ సిద్ధాంతానికి ముఖ్యమైన విమర్శ మరియు దాని రక్షణ ఏమిటి?\n(Key criticism of BS doctrine and its defence?)",
     "విమర్శ: సిద్ధాంతం అర్థం కాదు; రక్షణ: అర్థం అవుతుంది / Criticism: incomprehensible; Defence: understandable",
     "విమర్శ: SC అపరిమిత అధికారం పొందింది, ఏ సవరణ అయినా రద్దు చేయవచ్చు; రక్షణ: 42వ సవరణ దుర్వినియోగ నుండి రాజ్యాంగాన్ని రక్షించే అవసరమైన తనిఖీ / Criticism: SC gets unlimited power; Defence: necessary check against 42nd Amendment-type abuse",
     "విమర్శ: జర్మనీ నుండి కాపీ చేశారు; రక్షణ: స్వదేశీ సిద్ధాంతం / Criticism: borrowed from Germany; Defence: indigenous",
     "విమర్శ: మారదు; రక్షణ: స్థిరత్వం అవసరం / Criticism: doesn't evolve; Defence: stability needed",
     "b",
     "BS విమర్శలు: (1) SC 'Super Parliament' అవుతుంది; (2) నిర్వచనం అస్పష్టంగా ఉంది; (3) అనిర్ణీత జాబితా న్యాయ అనిశ్చితికి దారితీస్తుంది. రక్షణ: (1) 42వ సవరణ దుర్వినియోగ నుండి రాజ్యాంగాన్ని రక్షించింది; (2) FRs, ప్రజాస్వామ్యం, లౌకికత రక్షించడం ప్రజలకు మేలు; (3) రాజ్యాంగ ఆధిపత్యం అవసరం.\nCriticisms: (1) SC becomes 'Super Parliament'; (2) Vague definition; (3) Open-ended list creates uncertainty. Defence: (1) Protected from 42nd Amendment abuse; (2) Protecting FRs/democracy/secularism benefits citizens; (3) Constitutional supremacy requires such a check."),

    (6, 3,
     "Art 13(2) మరియు మూల నిర్మాణ సిద్ధాంతం మధ్య తేడా ఏమిటి?\n(What is the difference between Art 13(2) and Basic Structure doctrine?)",
     "రెండూ ఒకే పరీక్ష — వ్యత్యాసం లేదు / Both are the same test",
     "Art 13(2): సాధారణ చట్టాలు FRs ఉల్లంఘిస్తే రద్దు; BS: రాజ్యాంగ సవరణలు BS ఉల్లంఘిస్తే రద్దు — రెండు వేర్వేరు పరిధులు / Art 13(2): ordinary laws struck down for FR violation; BS: amendments for BS violation — two different spheres",
     "Art 13(2) BS కి లోబడి ఉంది / Art 13(2) is subordinate to BS",
     "BS Art 13(2) ని రద్దు చేసింది / BS overruled Art 13(2)",
     "b",
     "రెండు వేర్వేరు పరీక్షలు: (1) Art 13(2): సాధారణ చట్టాలు (ordinary laws) FR ఉల్లంఘిస్తే void. (2) BS సిద్ధాంతం: రాజ్యాంగ సవరణలు (constitutional amendments) BS ఉల్లంఘిస్తే void. Art 13(2) లోని 'law' రాజ్యాంగ సవరణలను కలిగి ఉండదు — Kesavananda ఇది స్పష్టం చేసింది.\nTwo separate tests: (1) Art 13(2): Ordinary laws struck down for FR violation. (2) BS doctrine: Constitutional amendments struck down for BS violation. 'Law' in Art 13(2) does not include constitutional amendments — Kesavananda clarified this.",
     "APPSC"),

    (6, 3,
     "కింది ఏ పదం భారత రాజ్యాంగంలో BS సిద్ధాంతానికి అత్యంత దగ్గరగా ఉంది?\n(Which concept in the Indian Constitution comes closest to Basic Structure doctrine?)",
     "Art 368(2) — Special Majority requirement",
     "Art 368(3) — State ratification requirement",
     "రాజ్యాంగంలో ఈ సిద్ధాంతానికి ఖచ్చితమైన ప్రతిరూపం లేదు — ఇది పూర్తిగా న్యాయ నిర్మాణం / No exact equivalent in Constitution — entirely judicial construction",
     "Art 13(1) — Pre-constitution laws void if inconsistent with FRs",
     "c",
     "మూల నిర్మాణ సిద్ధాంతం రాజ్యాంగంలో ఎక్కడా స్పష్టంగా పేర్కొనబడలేదు. జర్మనీ Art 79(3) వంటి 'Eternity Clause' భారత రాజ్యాంగంలో లేదు. ఇది పూర్తిగా SC యొక్క న్యాయ వ్యాఖ్యాన నిర్మాణం (judicial construction). రాజ్యాంగానికి 'implied transcendence' ఉందని SC పేర్కొంది.\nBasic Structure doctrine is nowhere explicitly mentioned in the Constitution. India has no 'Eternity Clause' like Germany's Art 79(3). It is entirely a judicial construction. The SC held that the Constitution has an implied transcendence that protects it from being destroyed by amendment."),

    (6, 3,
     "కేశవానంద భారతి 1973 యొక్క చారిత్రక ప్రాముఖ్యత ఏమిటి?\n(What is the historical significance of Kesavananda Bharati 1973?)",
     "అంతర్జాతీయ జోక్యం నుండి రక్షిస్తుంది / Protects from international interference",
     "రాష్ట్ర ప్రభుత్వాల మితిమీరిన చర్యల నుండి రక్షిస్తుంది / Protects from excessive state government actions",
     "రాజ్యాంగాన్ని పూర్తిగా నాశనం చేసే సవరణల నుండి రక్షిస్తుంది — పార్లమెంటరీ నిరంకుశత్వాన్ని నిరోధిస్తుంది / Protects Constitution from amendments that would completely destroy it — prevents constitutional dictatorship",
     "న్యాయ అవినీతి నుండి రక్షిస్తుంది / Protects from judicial corruption",
     "c",
     "కేశవానంద 1973 యొక్క 50 సంవత్సరాల వారసత్వం: రాజ్యాంగ ఆధిపత్యాన్ని రక్షిస్తుంది. 1975-77 Emergency కాలంలో 42వ సవరణ పార్లమెంట్ అధికారాన్ని గరిష్టం చేసి ప్రజాస్వామ్యాన్ని బలహీనపరచడానికి ప్రయత్నించింది. Minerva Mills 1980 తో BS సిద్ధాంతం దాన్ని తిరిగి పరిష్కరించింది. ఇది 'పార్లమెంటరీ నిరంకుశత్వాన్ని' నిరోధించే ఆయుధం.\nThe 50-year legacy of Kesavananda: Protects constitutional supremacy. During 1975-77 Emergency, 42nd Amendment maximized Parliament's power threatening democracy. Minerva Mills 1980 restored the balance using BS doctrine. Kesavananda is the ultimate safeguard against constitutional dictatorship.",
     "APPSC"),

]


def _seed_polity_ch12_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = POLITY_CH12_SECTIONS
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
