# ─────────────────────────────────────────────────────────────────────────────
# seed_polity_ch9.py
# Chapter 9 – Directive Principles of State Policy (Art 36–51) · Part IV
# Lakshmikanth's Indian Polity | APPSC Group 2 Standard
# Total MCQs: 75 | PYQs: 15 | Format: Bilingual (Telugu + English)
# ─────────────────────────────────────────────────────────────────────────────

import json as _json

POLITY_CH9_MCQS = [

    # ── Section 0: DPSP Basics – Art 36 & 37 ──────────────────────────────
    (0, 1,
     "రాజ్యాంగంలో రాజ్య నిర్దేశక సూత్రాలు (DPSP) ఏ భాగంలో ఉన్నాయి?\n(In which Part of the Constitution are the Directive Principles of State Policy contained?)",
     "భాగం III / Part III",
     "భాగం IV / Part IV",
     "భాగం IVA / Part IVA",
     "భాగం V / Part V",
     "b",
     "రాజ్య నిర్దేశక సూత్రాలు (DPSP) రాజ్యాంగంలో భాగం IV లో, అనుచ్ఛేదాలు 36–51 లో పేర్కొనబడ్డాయి.\nThe Directive Principles of State Policy (DPSP) are contained in Part IV of the Constitution, covering Articles 36–51."),

    (0, 1,
     "రాజ్య నిర్దేశక సూత్రాలు ఏ దేశ రాజ్యాంగం నుండి స్వీకరించబడ్డాయి?\n(The Directive Principles of State Policy were borrowed from the Constitution of which country?)",
     "అమెరికా / USA",
     "ఐర్లాండ్ / Ireland",
     "కెనడా / Canada",
     "ఆస్ట్రేలియా / Australia",
     "b",
     "DPSP భావన ఐర్లాండ్ (Eire) రాజ్యాంగం 1937 నుండి స్వీకరించబడింది. ఐర్లాండ్ వారు స్పెయిన్ రాజ్యాంగం నుండి ఈ భావనను తీసుకున్నారు.\nThe concept of DPSP was borrowed from the Irish (Eire) Constitution of 1937. Ireland in turn drew inspiration from the Spanish Constitution.",
     "APPSC"),

    (0, 2,
     "అనుచ్ఛేద 37 ప్రకారం రాజ్య నిర్దేశక సూత్రాల స్వభావం ఏమిటి?\n(What is the nature of Directive Principles under Article 37?)",
     "న్యాయస్థానాల ద్వారా అమలు చేయదగినవి / Justiciable by courts",
     "న్యాయస్థానాల ద్వారా అమలు చేయలేనివి కానీ పాలనలో మూలభూతమైనవి / Non-justiciable but fundamental in governance",
     "పూర్తిగా ఐచ్ఛికమైనవి / Completely optional",
     "కేవలం రాష్ట్ర ప్రభుత్వాలకు మాత్రమే వర్తించేవి / Applicable only to State Governments",
     "b",
     "అనుచ్ఛేద 37 ప్రకారం DPSP న్యాయస్థానాల ద్వారా అమలు చేయదగినవి కావు, కానీ దేశ పాలనలో మూలభూతమైనవి; చట్టాలు రూపొందించేటప్పుడు వీటిని దృష్టిలో ఉంచుకోవడం రాజ్యం యొక్క బాధ్యత.\nUnder Article 37, DPSPs are not enforceable by courts but are fundamental in governance; it shall be the duty of the State to apply these principles in making laws."),

    (0, 2,
     "DPSP ని 'బ్యాంకు సౌకర్యానికి చెల్లించే చెక్కు' అని ఎవరు అభివర్ణించారు?\n(Who described DPSPs as 'a cheque payable at the bank's convenience'?)",
     "T.T. కృష్ణమాచారి / T.T. Krishnamachari",
     "K.T. షా / K.T. Shah",
     "B.R. అంబేడ్కర్ / B.R. Ambedkar",
     "జవహర్‌లాల్ నెహ్రూ / Jawaharlal Nehru",
     "b",
     "K.T. షా DPSP లను 'బ్యాంకు సౌకర్యానికి చెల్లించే చెక్కు' అని అభివర్ణించారు, ఎందుకంటే వాటిని అమలు చేయించడానికి న్యాయపరమైన బలం లేదు.\nK.T. Shah described DPSPs as 'a cheque payable at the bank's convenience' because they lack judicial enforceability."),

    (0, 1,
     "అనుచ్ఛేద 36లో 'రాజ్యం' నిర్వచనం ఏ అనుచ్ఛేదం నిర్వచనానికి సమానం?\n(The definition of 'State' in Article 36 is the same as that in which Article?)",
     "అనుచ్ఛేద 10 / Article 10",
     "అనుచ్ఛేద 12 / Article 12",
     "అనుచ్ఛేద 13 / Article 13",
     "అనుచ్ఛేద 19 / Article 19",
     "b",
     "అనుచ్ఛేద 36లో 'రాజ్యం' నిర్వచనం అనుచ్ఛేద 12 లోని నిర్వచనానికి అనుగుణంగా ఉంటుంది — భారత ప్రభుత్వం, పార్లమెంటు, రాష్ట్ర ప్రభుత్వాలు, శాసన సభలు మరియు స్థానిక అధికారులు.\nThe definition of 'State' in Article 36 is the same as in Article 12 — the Government of India, Parliament, State Governments, Legislatures, and local or other authorities."),

    # ── Section 1: Socialistic DPSPs ──────────────────────────────────────
    (1, 2,
     "అనుచ్ఛేద 38 దేనిని నిర్దేశిస్తుంది?\n(What does Article 38 direct?)",
     "ఉచిత న్యాయ సహాయం / Free legal aid",
     "సామాజిక, ఆర్థిక మరియు రాజకీయ న్యాయం సాధించే సామాజిక వ్యవస్థ / Social order securing social, economic and political justice",
     "జీవన వేతనం / Living wage",
     "గ్రామ పంచాయతీలు / Village panchayats",
     "b",
     "అనుచ్ఛేద 38 రాజ్యం సామాజిక, ఆర్థిక మరియు రాజకీయ న్యాయం నిర్ధారించే సామాజిక వ్యవస్థను సురక్షితపరచాలని, ఆదాయం, హోదా, సదుపాయాలలో అసమానతలను తగ్గించాలని నిర్దేశిస్తుంది.\nArticle 38 directs the State to secure a social order in which social, economic and political justice shall inform all institutions, and to minimize inequalities in income, status, facilities and opportunities."),

    (1, 2,
     "అనుచ్ఛేద 39(a) ఏమి నిర్దేశిస్తుంది?\n(What does Article 39(a) direct?)",
     "సమాన వేతనం / Equal pay",
     "స్త్రీ మరియు పురుషులకు జీవనోపాధికి సమాన హక్కు / Equal right to adequate means of livelihood for men and women",
     "కార్మికులకు జీవన వేతనం / Living wage for workers",
     "ఉచిత న్యాయ సహాయం / Free legal aid",
     "b",
     "అనుచ్ఛేద 39(a) రాజ్యం స్త్రీ మరియు పురుష పౌరులకు జీవనోపాధికి సమాన హక్కు ఉందని నిర్ధారించాలని నిర్దేశిస్తుంది — ఇది సమాజవాద నిర్దేశక సూత్రం.\nArticle 39(a) directs the State to ensure that citizens, men and women equally, have the right to an adequate means of livelihood — a Socialistic DPSP."),

    (1, 2,
     "అనుచ్ఛేద 39(b) ఏమి నిర్దేశిస్తుంది?\n(What does Article 39(b) direct?)",
     "సమాన వేతనం / Equal pay",
     "సమాజ భౌతిక వనరులు ఉమ్మడి మేలు కోసం పంపిణీ చేయాలి / Material resources of community distributed for common good",
     "ఉచిత న్యాయ సహాయం / Free legal aid",
     "జీవన వేతనం / Living wage",
     "b",
     "అనుచ్ఛేద 39(b) ప్రకారం సమాజ భౌతిక వనరుల యాజమాన్యం మరియు నియంత్రణ ఉమ్మడి మేలు కోసం పంపిణీ చేయబడాలని నిర్దేశిస్తుంది. ఇది మినర్వా మిల్స్ కేసులో కీలకమైన అంశం.\nArticle 39(b) directs that ownership and control of material resources of the community shall be distributed to best subserve the common good. This was central to the Minerva Mills case."),

    (1, 2,
     "అనుచ్ఛేద 39(c) ఏమి నిర్దేశిస్తుంది?\n(What does Article 39(c) direct?)",
     "ఏకరీతి పౌర స్మృతి / Uniform Civil Code",
     "సంపద మరియు ఉత్పత్తి సాధనాల కేంద్రీకరణ నివారణ / Prevention of concentration of wealth and means of production",
     "వ్యవసాయ పరిరక్షణ / Protection of agriculture",
     "మాతృత్వ సహాయం / Maternity relief",
     "b",
     "అనుచ్ఛేద 39(c) ఆర్థిక వ్యవస్థ అందరికీ హాని కలిగించే విధంగా సంపద మరియు ఉత్పత్తి సాధనాల కేంద్రీకరణకు దారితీయకుండా ఉండాలని నిర్దేశిస్తుంది.\nArticle 39(c) directs that the operation of the economic system should not result in the concentration of wealth and means of production to the common detriment."),

    (1, 1,
     "అనుచ్ఛేద 39A 'సమాన న్యాయం మరియు ఉచిత న్యాయ సహాయం' ఏ రాజ్యాంగ సవరణ ద్వారా జోడించబడింది?\n(Article 39A on 'equal justice and free legal aid' was added by which Constitutional Amendment?)",
     "24వ సవరణ 1971 / 24th Amendment 1971",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "44వ సవరణ 1978 / 44th Amendment 1978",
     "86వ సవరణ 2002 / 86th Amendment 2002",
     "b",
     "అనుచ్ఛేద 39A 42వ రాజ్యాంగ సవరణ చట్టం 1976 ద్వారా జోడించబడింది, ఇది సమాన న్యాయం మరియు ఉచిత న్యాయ సహాయాన్ని నిర్దేశిస్తుంది.\nArticle 39A was added by the 42nd Constitutional Amendment Act, 1976, directing the State to secure equal justice and free legal aid.",
     "APPSC"),

    (1, 2,
     "అనుచ్ఛేద 42 దేనిని నిర్దేశిస్తుంది?\n(What does Article 42 direct?)",
     "జీవన వేతనం / Living wage",
     "న్యాయమైన మరియు మానవీయ పని పరిస్థితులు మరియు మాతృత్వ సహాయం / Just and humane conditions of work and maternity relief",
     "కార్మికుల నిర్వహణ భాగస్వామ్యం / Workers' participation in management",
     "పని హక్కు / Right to work",
     "b",
     "అనుచ్ఛేద 42 రాజ్యం న్యాయమైన మరియు మానవీయ పని పరిస్థితులు మరియు మాతృత్వ సహాయాన్ని నిర్ధారించడానికి చట్టాలు చేయాలని నిర్దేశిస్తుంది — ఇది సమాజవాద నిర్దేశక సూత్రం.\nArticle 42 directs the State to make provision for securing just and humane conditions of work and for maternity relief — a Socialistic DPSP."),

    (1, 1,
     "అనుచ్ఛేద 43A 'కార్మికుల నిర్వహణ భాగస్వామ్యం' ఏ రాజ్యాంగ సవరణ ద్వారా జోడించబడింది?\n(Article 43A on 'participation of workers in management' was added by which Constitutional Amendment?)",
     "25వ సవరణ 1971 / 25th Amendment 1971",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "44వ సవరణ 1978 / 44th Amendment 1978",
     "97వ సవరణ 2011 / 97th Amendment 2011",
     "b",
     "అనుచ్ఛేద 43A 42వ రాజ్యాంగ సవరణ చట్టం 1976 ద్వారా జోడించబడింది, ఇది పరిశ్రమల నిర్వహణలో కార్మికుల భాగస్వామ్యాన్ని నిర్దేశిస్తుంది.\nArticle 43A was added by the 42nd Constitutional Amendment Act, 1976, directing participation of workers in management of industries."),

    (1, 2,
     "సహకార సంఘాల అభివృద్ధికి సంబంధించిన అనుచ్ఛేద 43B ఏ రాజ్యాంగ సవరణ ద్వారా జోడించబడింది?\n(Article 43B on promotion of cooperative societies was added by which Constitutional Amendment?)",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "86వ సవరణ 2002 / 86th Amendment 2002",
     "97వ సవరణ 2011 / 97th Amendment 2011",
     "99వ సవరణ 2014 / 99th Amendment 2014",
     "c",
     "అనుచ్ఛేద 43B 97వ రాజ్యాంగ సవరణ చట్టం 2011 ద్వారా జోడించబడింది, ఇది స్వచ్ఛంద నిర్మాణం, స్వయంప్రతిపత్తి, ప్రజాస్వామ్య నియంత్రణ సూత్రాల ఆధారంగా సహకార సంఘాల అభివృద్ధిని నిర్దేశిస్తుంది.\nArticle 43B was added by the 97th Constitutional Amendment Act, 2011, directing the State to promote voluntary formation, autonomous functioning, democratic control and professional management of cooperative societies.",
     "APPSC"),

    # ── Section 2: Gandhian DPSPs ──────────────────────────────────────────
    (2, 1,
     "గాంధేయ నిర్దేశక సూత్రాలలో ఏ అనుచ్ఛేదం గ్రామ పంచాయతీల సంఘటనకు సంబంధించింది?\n(Which article among Gandhian DPSPs relates to organisation of village panchayats?)",
     "అనుచ్ఛేద 38 / Article 38",
     "అనుచ్ఛేద 40 / Article 40",
     "అనుచ్ఛేద 43 / Article 43",
     "అనుచ్ఛేద 46 / Article 46",
     "b",
     "అనుచ్ఛేద 40 రాజ్యం గ్రామ పంచాయతీలను నిర్మించాలని మరియు వాటి స్వయం పాలన ప్రభావవంత యూనిట్లుగా పనిచేయడానికి అవసరమైన అధికారాలు ఇవ్వాలని నిర్దేశిస్తుంది — ఇది గాంధేయ నిర్దేశక సూత్రం.\nArticle 40 directs the State to organise village panchayats and endow them with powers to function as units of self-government — a Gandhian DPSP."),

    (2, 2,
     "అనుచ్ఛేద 46 ఏ వర్గాల విద్యా మరియు ఆర్థిక ప్రయోజనాలను పెంపొందించాలని నిర్దేశిస్తుంది?\n(Article 46 directs promotion of educational and economic interests of which groups?)",
     "మహిళలు మరియు పిల్లలు / Women and children",
     "SC, ST మరియు బలహీన వర్గాలు / SC, ST and weaker sections",
     "OBC మరియు మైనారిటీలు / OBC and minorities",
     "వికలాంగులు మరియు వృద్ధులు / Differently abled and aged persons",
     "b",
     "అనుచ్ఛేద 46 (గాంధేయ నిర్దేశక సూత్రం) రాజ్యం అనుసూచిత కులాలు, అనుసూచిత తెగలు మరియు ఇతర బలహీన వర్గాల విద్యా మరియు ఆర్థిక ప్రయోజనాలను పెంపొందించాలని, వారిపై సామాజిక అన్యాయం నుండి రక్షించాలని నిర్దేశిస్తుంది.\nArticle 46 (Gandhian DPSP) directs the State to promote the educational and economic interests of SC, ST and other weaker sections, and protect them from social injustice and all forms of exploitation."),

    (2, 2,
     "గోహత్య నిషేధం మరియు పశుపాలన సంఘటనకు సంబంధించిన అనుచ్ఛేదం ఏది?\n(Which article relates to prohibition of cow slaughter and organisation of animal husbandry?)",
     "అనుచ్ఛేద 47 / Article 47",
     "అనుచ్ఛేద 48 / Article 48",
     "అనుచ్ఛేద 48A / Article 48A",
     "అనుచ్ఛేద 49 / Article 49",
     "b",
     "అనుచ్ఛేద 48 రాజ్యం వ్యవసాయాన్ని మరియు పశుపాలనను శాస్త్రీయ పద్ధతుల్లో నిర్వహించాలని, పాడి పశువుల జాతులను సంరక్షించాలని, ఆవులు, దూడలు మరియు ఇతర పాడి మరియు పొలం పశువుల వధను నిషేధించాలని నిర్దేశిస్తుంది.\nArticle 48 directs the State to organise agriculture and animal husbandry on modern scientific lines, preserve breeds, and prohibit slaughter of cows, calves, and milch and draught cattle."),

    (2, 2,
     "అనుచ్ఛేద 47 ఏమి నిర్దేశిస్తుంది?\n(What does Article 47 direct?)",
     "గ్రామ పంచాయతీల స్థాపన / Organisation of village panchayats",
     "పౌష్టికాహారం, జీవన ప్రమాణాల పెంపు మరియు మద్యపాన నిషేధం / Nutrition, raising living standards, and prohibition of intoxicating drinks",
     "వ్యవసాయ శాస్త్రీయ పద్ధతులు / Scientific agriculture",
     "సమాన వేతనం / Equal pay",
     "b",
     "అనుచ్ఛేద 47 రాజ్యం పౌరుల పౌష్టికాహారం మరియు జీవన ప్రమాణాన్ని పెంచాలని, ఆరోగ్యానికి హానికరమైన మాదక పానీయాల వినియోగాన్ని నిషేధించాలని నిర్దేశిస్తుంది (సమాజవాద + గాంధేయ రెండూ).\nArticle 47 directs the State to raise the level of nutrition and standard of living, and prohibit consumption of intoxicating drinks and drugs injurious to health (has both Socialistic and Gandhian character)."),

    # ── Section 3: Liberal-Intellectual DPSPs ─────────────────────────────
    (3, 1,
     "ఏకరీతి పౌర స్మృతి (Uniform Civil Code) కి సంబంధించిన అనుచ్ఛేదం ఏది?\n(Which article relates to Uniform Civil Code?)",
     "అనుచ్ఛేద 43 / Article 43",
     "అనుచ్ఛేద 44 / Article 44",
     "అనుచ్ఛేద 45 / Article 45",
     "అనుచ్ఛేద 50 / Article 50",
     "b",
     "అనుచ్ఛేద 44 రాజ్యం భారత భూభాగం అంతటా పౌరులందరికీ ఏకరీతి పౌర స్మృతి సాధించడానికి ప్రయత్నించాలని నిర్దేశిస్తుంది — ఇది ఉదారవాద-మేధో నిర్దేశక సూత్రం.\nArticle 44 directs the State to secure for citizens a Uniform Civil Code throughout the territory of India — a Liberal-Intellectual DPSP.",
     "APPSC"),

    (3, 2,
     "అసలు అనుచ్ఛేద 45 (86వ సవరణ కు ముందు) ఏమి నిర్దేశించింది?\n(What did the original Article 45 (before 86th Amendment) direct?)",
     "6 సంవత్సరాల లోపు పిల్లలకు సంరక్షణ / Care for children below 6 years",
     "10 సంవత్సరాల వయసు వరకు ఉచిత విద్య / Free education up to age 10",
     "14 సంవత్సరాల వయసు వరకు ఉచిత మరియు నిర్బంధ విద్య / Free and compulsory education up to 14 years of age",
     "18 సంవత్సరాల వయసు వరకు ఉచిత విద్య / Free education up to age 18",
     "c",
     "అసలు అనుచ్ఛేద 45 (1950) 14 సంవత్సరాల వయసు వరకు పిల్లలందరికీ ఉచిత మరియు నిర్బంధ విద్యను అందించాలని నిర్దేశించింది. 86వ సవరణ 2002 తర్వాత 6–14 వయసు విద్య అనుచ్ఛేద 21A ద్వారా మూల హక్కు అయింది; అనుచ్ఛేద 45 ఇప్పుడు 6 సంవత్సరాల లోపు పిల్లల సంరక్షణను నిర్దేశిస్తుంది.\nOriginal Article 45 (1950) directed free and compulsory education for all children up to age 14. After 86th Amendment 2002, education for 6–14 years became a FR under Article 21A; Article 45 now directs early childhood care for children below 6 years."),

    (3, 2,
     "పర్యావరణ పరిరక్షణ మరియు అటవీ సంరక్షణకు సంబంధించిన అనుచ్ఛేద 48A ఏ సవరణ ద్వారా జోడించబడింది?\n(Article 48A on protection of environment and safeguarding forests was added by which amendment?)",
     "24వ సవరణ 1971 / 24th Amendment 1971",
     "42వ సవరణ 1976 / 42nd Amendment 1976",
     "44వ సవరణ 1978 / 44th Amendment 1978",
     "86వ సవరణ 2002 / 86th Amendment 2002",
     "b",
     "అనుచ్ఛేద 48A 42వ రాజ్యాంగ సవరణ చట్టం 1976 ద్వారా జోడించబడింది, రాజ్యం పర్యావరణాన్ని పరిరక్షించాలని మరియు అటవీ మరియు వన్యప్రాణులను సంరక్షించాలని నిర్దేశిస్తుంది.\nArticle 48A was added by the 42nd Constitutional Amendment Act, 1976, directing the State to protect and improve the environment and to safeguard forests and wildlife.",
     "APPSC"),

    (3, 1,
     "జాతీయ ప్రాముఖ్యం గల స్మారక చిహ్నాలను రక్షించాలని నిర్దేశించే అనుచ్ఛేదం ఏది?\n(Which article directs protection of monuments of national importance?)",
     "అనుచ్ఛేద 48 / Article 48",
     "అనుచ్ఛేద 49 / Article 49",
     "అనుచ్ఛేద 50 / Article 50",
     "అనుచ్ఛేద 51 / Article 51",
     "b",
     "అనుచ్ఛేద 49 జాతీయ ప్రాముఖ్యం గల స్మారక చిహ్నాలు, స్థలాలు మరియు వస్తువులను రక్షించాలని రాజ్యానికి నిర్దేశిస్తుంది — ఇది ఉదారవాద-మేధో నిర్దేశక సూత్రం.\nArticle 49 directs the State to protect every monument, place or object of artistic or historic interest declared to be of national importance — a Liberal-Intellectual DPSP."),

    (3, 2,
     "న్యాయవ్యవస్థను కార్యనిర్వాహక వ్యవస్థ నుండి వేరు చేయాలని నిర్దేశించే అనుచ్ఛేదం ఏది?\n(Which article directs separation of judiciary from the executive?)",
     "అనుచ్ఛేద 44 / Article 44",
     "అనుచ్ఛేద 48A / Article 48A",
     "అనుచ్ఛేద 50 / Article 50",
     "అనుచ్ఛేద 51 / Article 51",
     "c",
     "అనుచ్ఛేద 50 రాజ్య పబ్లిక్ సేవలలో న్యాయవ్యవస్థను కార్యనిర్వాహక వ్యవస్థ నుండి వేరు చేయడానికి చర్యలు తీసుకోవాలని నిర్దేశిస్తుంది — ఇది న్యాయ స్వాతంత్ర్యాన్ని నిర్ధారించే ఉదారవాద-మేధో నిర్దేశక సూత్రం.\nArticle 50 directs the State to take steps to separate the judiciary from the executive in the public services of the State — a Liberal-Intellectual DPSP ensuring judicial independence."),

    (3, 1,
     "అంతర్జాతీయ శాంతి మరియు భద్రత ప్రోత్సాహానికి సంబంధించిన అనుచ్ఛేదం ఏది?\n(Which article relates to promotion of international peace and security?)",
     "అనుచ్ఛేద 49 / Article 49",
     "అనుచ్ఛేద 50 / Article 50",
     "అనుచ్ఛేద 51 / Article 51",
     "అనుచ్ఛేద 38 / Article 38",
     "c",
     "అనుచ్ఛేద 51 అంతర్జాతీయ శాంతి మరియు భద్రతను ప్రోత్సహించాలని, దేశాల మధ్య న్యాయమైన సంబంధాలు నెలకొల్పాలని, అంతర్జాతీయ చట్టాలు మరియు ఒప్పందాల పట్ల గౌరవం చూపాలని నిర్దేశిస్తుంది.\nArticle 51 directs the State to promote international peace and security, maintain just and honourable relations between nations, and foster respect for international law and treaty obligations.",
     "APPSC"),

    (3, 2,
     "కింది వాటిలో ఏది ఉదారవాద-మేధో (Liberal-Intellectual) DPSP కాదు?\n(Which of the following is NOT a Liberal-Intellectual DPSP?)",
     "అనుచ్ఛేద 44 - ఏకరీతి పౌర స్మృతి / Art 44 - Uniform Civil Code",
     "అనుచ్ఛేద 50 - న్యాయ-కార్యనిర్వాహక వేర్పాటు / Art 50 - Separation of Judiciary",
     "అనుచ్ఛేద 46 - SC/ST విద్యా ప్రయోజనాలు / Art 46 - Educational interests of SC/ST",
     "అనుచ్ఛేద 48A - పర్యావరణ పరిరక్షణ / Art 48A - Protection of environment",
     "c",
     "అనుచ్ఛేద 46 (SC/ST మరియు బలహీన వర్గాల విద్యా మరియు ఆర్థిక ప్రయోజనాలు) గాంధేయ నిర్దేశక సూత్రం. ఉదారవాద-మేధో DPSPs: 44, 45, 48, 48A, 49, 50, 51. గాంధేయ DPSPs: 40, 43, 46, 47, 48.\nArticle 46 (educational and economic interests of SC/ST and weaker sections) is a Gandhian DPSP. Liberal-Intellectual DPSPs are: 44, 45, 48, 48A, 49, 50, 51. Gandhian DPSPs: 40, 43, 46, 47, 48."),

    (3, 3,
     "అనుచ్ఛేద 41 ఏ హక్కులను నిర్దేశిస్తుంది?\n(Article 41 directs right to what?)",
     "విద్య మాత్రమే / Education only",
     "పని, విద్య మరియు కొన్ని సందర్భాలలో పబ్లిక్ సహాయం / Work, education and public assistance in certain cases",
     "పని మరియు మాతృత్వ సహాయం / Work and maternity relief",
     "పని మరియు జీవన వేతనం / Work and living wage",
     "b",
     "అనుచ్ఛేద 41 రాజ్యం పని హక్కు, విద్య హక్కు మరియు నిరుద్యోగం, వృద్ధాప్యం, అనారోగ్యం, వికలాంగత వంటి సందర్భాలలో పబ్లిక్ సహాయాన్ని అందించాలని నిర్దేశిస్తుంది.\nArticle 41 directs the State to make effective provision for securing the right to work, right to education, and right to public assistance in cases of unemployment, old age, sickness, and disablement."),

    # ── Section 4: FR vs DPSP Conflict & Landmark Cases ──────────────────
    (4, 3,
     "చంపకం దొరైరాజన్ కేసు (1951) దేనికి సంబంధించింది?\n(What was the Champakam Dorairajan case (1951) about?)",
     "అనుచ్ఛేద 19 మరియు DPSP మధ్య వైరుధ్యం / Conflict between Art 19 and DPSP",
     "మత ఆధారిత రిజర్వేషన్లు vs అనుచ్ఛేద 29(2) / Religion-based reservations vs Article 29(2)",
     "ఆస్తి హక్కు రద్దు / Abolition of right to property",
     "అనుచ్ఛేద 32 అమలు పరిధి / Scope of Article 32",
     "b",
     "చంపకం దొరైరాజన్ కేసు (1951)లో సుప్రీంకోర్టు, DPSP మరియు FR మధ్య వైరుధ్యం ఉంటే FR గెలుస్తుందని తీర్పు ఇచ్చింది. మద్రాసు రాష్ట్రంలో మత ఆధారిత సీట్ల కేటాయింపు అనుచ్ఛేద 29(2)కి విరుద్ధంగా ఉందని నిర్ణయించింది.\nIn Champakam Dorairajan case (1951), the SC held that FRs prevail over DPSPs in case of conflict. It struck down Madras State's religion-based seat allocation as violative of Article 29(2).",
     "APPSC"),

    (4, 3,
     "1వ రాజ్యాంగ సవరణ చట్టం 1951 ఏ కొత్త ఖండాన్ని జోడించింది?\n(The 1st Constitutional Amendment Act 1951 added which new clause?)",
     "అనుచ్ఛేద 14(3) / Article 14(3)",
     "అనుచ్ఛేద 15(4) / Article 15(4)",
     "అనుచ్ఛేద 16(4) / Article 16(4)",
     "అనుచ్ఛేద 19(2) / Article 19(2)",
     "b",
     "చంపకం కేసు తీర్పుకు ప్రతిస్పందనగా, 1వ రాజ్యాంగ సవరణ చట్టం 1951 అనుచ్ఛేద 15(4)ని జోడించింది — SC/ST మరియు సాంఘికంగా వెనుకబడిన వర్గాల అభివృద్ధికి ప్రత్యేక నిబంధనలు చేయడానికి అనుమతిస్తుంది.\nIn response to the Champakam verdict, the 1st Amendment 1951 added Article 15(4), permitting the State to make special provisions for advancement of SC/ST and socially and educationally backward classes."),

    (4, 3,
     "గోలక్‌నాథ్ కేసు (1967) లో సుప్రీంకోర్టు ఇచ్చిన తీర్పు ఏమిటి?\n(What was the Supreme Court's ruling in Golak Nath case (1967)?)",
     "పార్లమెంటు ఏ హక్కునైనా సవరించవచ్చు / Parliament can amend any right",
     "పార్లమెంటు మూల హక్కులను సవరించలేదు / Parliament cannot amend Fundamental Rights",
     "DPSP లకు FR లపై ఆధిక్యత ఉంటుంది / DPSPs prevail over FRs",
     "DPSP లు న్యాయస్థానాల ద్వారా అమలు చేయవచ్చు / DPSPs are justiciable",
     "b",
     "గోలక్‌నాథ్ కేసు (1967)లో సుప్రీంకోర్టు పార్లమెంటు మూల హక్కులను (భాగం III) సవరించే అధికారం లేదని తీర్పు ఇచ్చింది. ఈ తీర్పును తిరగదోయడానికి 24వ సవరణ చట్టం 1971 ఆమోదించబడింది.\nIn Golak Nath case (1967), the SC held that Parliament has no power to amend FRs (Part III). The 24th Amendment Act 1971 was passed to overturn this ruling."),

    (4, 3,
     "24వ రాజ్యాంగ సవరణ చట్టం 1971 ఏమి చేసింది?\n(What did the 24th Constitutional Amendment Act 1971 do?)",
     "అనుచ్ఛేద 31C జోడించింది / Added Article 31C",
     "గోలక్‌నాథ్ తీర్పుని తిరగదోసి పార్లమెంటుకు రాజ్యాంగంలో ఏ భాగాన్నైనా సవరించే అధికారం ఇచ్చింది / Overruled Golak Nath and empowered Parliament to amend any part of Constitution",
     "9వ షెడ్యూల్ జోడించింది / Added 9th Schedule",
     "DPSP లను FR లపై ఆధిక్యత ఇచ్చింది / Gave DPSPs precedence over FRs",
     "b",
     "24వ రాజ్యాంగ సవరణ చట్టం 1971 అనుచ్ఛేద 13(4) మరియు 368(3) జోడించింది, గోలక్‌నాథ్ తీర్పుని తిరగదోసింది — పార్లమెంటుకు అనుచ్ఛేద 368 ద్వారా FR లతో సహా రాజ్యాంగంలో ఏ భాగాన్నైనా సవరించే అధికారం ఉందని నిర్ధారించింది.\nThe 24th Amendment 1971 added Articles 13(4) and 368(3), overruling Golak Nath — affirming Parliament's power to amend any part of the Constitution including FRs under Article 368."),

    (4, 3,
     "25వ రాజ్యాంగ సవరణ చట్టం 1971 ద్వారా జోడించబడిన అనుచ్ఛేద 31C ఏమి నిర్దేశించింది?\n(What did Article 31C added by the 25th Constitutional Amendment 1971 provide?)",
     "9వ షెడ్యూల్‌లో జాబితా చేసిన చట్టాలకు రక్షణ / Protection to laws listed in 9th Schedule",
     "అన్ని DPSP లను అమలు చేసే చట్టాలు Art 14/19 ఆధారంగా సవాలు చేయలేవు / Laws implementing all DPSPs cannot be challenged under Art 14/19",
     "Art 39(b) మరియు 39(c) అమలు చేసే చట్టాలు Art 14/19 ఆధారంగా సవాలు చేయలేవు / Laws implementing Arts 39(b)&(c) cannot be challenged under Arts 14 and 19",
     "FR లు DPSP లపై ఆధిక్యత కలిగి ఉంటాయని / FRs prevail over DPSPs",
     "c",
     "25వ సవరణ 1971 అనుచ్ఛేద 31C ని జోడించింది — అనుచ్ఛేద 39(b) మరియు 39(c) అమలు చేసే చట్టాలు అనుచ్ఛేద 14 మరియు 19 ఆధారంగా సవాలు చేయలేవు. 42వ సవరణ ఇది అన్ని DPSPs కు వర్తింపజేసింది, కానీ మినర్వా మిల్స్ 1980 అది రద్దు చేసింది.\nThe 25th Amendment 1971 inserted Article 31C providing that laws implementing Arts 39(b) and 39(c) cannot be challenged under Arts 14 and 19. The 42nd Amendment extended this to all DPSPs, but Minerva Mills 1980 struck down that extension."),

    (4, 3,
     "42వ రాజ్యాంగ సవరణ చట్టం 1976 అనుచ్ఛేద 31C ని ఏ విధంగా విస్తరించింది?\n(How did the 42nd Constitutional Amendment Act 1976 extend Article 31C?)",
     "అనుచ్ఛేద 14 కి మాత్రమే రక్షణ / Protection only from Article 14",
     "అన్ని DPSP లను అమలు చేసే చట్టాలకు Art 14/19 నుండి రక్షణ / Protection to laws implementing all DPSPs from challenge under Arts 14 and 19",
     "అనుచ్ఛేద 21 నుండి మాత్రమే రక్షణ / Protection only from Article 21",
     "మొత్తం భాగం IV రక్షణ / Protection to entire Part IV",
     "b",
     "42వ సవరణ 1976 అనుచ్ఛేద 31C ని విస్తరించింది — అన్ని DPSP లు అమలు చేసే చట్టాలు అనుచ్ఛేద 14 మరియు 19 ఆధారంగా సవాలు చేయలేవు. మినర్వా మిల్స్ కేసు 1980లో ఈ విస్తరణ రద్దు చేయబడింది.\nThe 42nd Amendment 1976 extended Art 31C so laws implementing all DPSPs were protected from challenge under Arts 14 and 19. This extension was struck down in Minerva Mills 1980."),

    (4, 3,
     "మినర్వా మిల్స్ కేసు (1980) లో సుప్రీంకోర్టు ఏ తీర్పు ఇచ్చింది?\n(What was the Supreme Court's ruling in Minerva Mills case (1980)?)",
     "42వ సవరణ చట్టు పూర్తిగా రాజ్యాంగ విరుద్ధం / 42nd Amendment entirely unconstitutional",
     "42వ సవరణ ద్వారా అన్ని DPSP లకు ఇచ్చిన Art 31C విస్తరణ రాజ్యాంగ విరుద్ధం / Extension of Art 31C to all DPSPs by 42nd Amendment is unconstitutional",
     "DPSP లు FR లపై ఆధిక్యత కలిగి ఉంటాయి / DPSPs prevail over FRs",
     "FR మరియు DPSP మధ్య వైరుధ్యం లేదు / No conflict between FRs and DPSPs",
     "b",
     "మినర్వా మిల్స్ కేసు (1980)లో సుప్రీంకోర్టు 42వ సవరణ ద్వారా అన్ని DPSP లకు వర్తింపజేసిన అనుచ్ఛేద 31C విస్తరణ రాజ్యాంగ విరుద్ధంగా ప్రకటించింది. అనుచ్ఛేద 31C మళ్ళీ 39(b) మరియు 39(c) కు మాత్రమే పరిమితమైంది.\nIn Minerva Mills (1980), the SC declared the extension of Art 31C to all DPSPs by 42nd Amendment as unconstitutional. Art 31C was restored to cover only Arts 39(b) and 39(c).",
     "APPSC"),

    (4, 3,
     "కేశవానంద భారతి కేసు (1973) FR మరియు DPSP సంబంధంపై ఏమి స్పష్టపరిచింది?\n(What did Kesavananda Bharati case (1973) clarify about FR-DPSP relationship?)",
     "DPSP లు FR లపై ఆధిక్యత కలిగి ఉంటాయి / DPSPs prevail over FRs",
     "FR లు DPSP లపై ఆధిక్యత కలిగి ఉంటాయి / FRs prevail over DPSPs",
     "FR మరియు DPSP రెండూ మూల నిర్మాణంలో భాగం; మూల నిర్మాణాన్ని మార్చలేరు / Both form part of Basic Structure; Basic Structure cannot be destroyed",
     "FR మరియు DPSP మధ్య ఎప్పుడూ వైరుధ్యం ఉండదు / No conflict ever between FRs and DPSPs",
     "c",
     "కేశవానంద భారతి కేసు (1973)లో సుప్రీంకోర్టు మూల నిర్మాణ సిద్ధాంతాన్ని ప్రతిపాదించింది. FR మరియు DPSP రెండూ రాజ్యాంగ మూల నిర్మాణంలో భాగంగా పేర్కొనబడ్డాయి; పార్లమెంటు FR లను సవరించవచ్చు కానీ మూల నిర్మాణాన్ని మార్చలేదు.\nIn Kesavananda Bharati (1973), the SC propounded the Basic Structure Doctrine. Both FRs and DPSPs were recognized as part of the constitutional Basic Structure; Parliament can amend FRs but cannot destroy the Basic Structure.",
     "APPSC"),

    (4, 2,
     "I.R. కోయెల్హో కేసు (2007) 9వ షెడ్యూల్ గురించి ఏమి నిర్ణయించింది?\n(What did I.R. Coelho case (2007) decide about the 9th Schedule?)",
     "9వ షెడ్యూల్‌లోని అన్ని చట్టాలు న్యాయ సమీక్ష నుండి రక్షింపబడతాయి / All laws in 9th Schedule are protected from judicial review",
     "1973 ఏప్రిల్ 24 తర్వాత 9వ షెడ్యూల్‌కు జోడించిన చట్టాలు న్యాయ సమీక్షకు లోబడతాయి / Laws added to 9th Schedule after April 24, 1973 are subject to judicial review",
     "9వ షెడ్యూల్ రాజ్యాంగ విరుద్ధం / 9th Schedule is unconstitutional",
     "9వ షెడ్యూల్ కేవలం DPSP లకు మాత్రమే వర్తిస్తుంది / 9th Schedule applies only to DPSPs",
     "b",
     "I.R. కోయెల్హో కేసు (2007)లో 9 న్యాయమూర్తుల రాజ్యాంగ ధర్మాసనం: 24 ఏప్రిల్ 1973 (కేశవానంద భారతి తీర్పు తేదీ) తర్వాత 9వ షెడ్యూల్‌కు జోడించిన చట్టాలు మూల నిర్మాణ సిద్ధాంతం ఆధారంగా న్యాయ సమీక్షకు లోబడతాయి.\nIn I.R. Coelho (2007), a 9-judge Constitutional Bench held that laws added to 9th Schedule after April 24, 1973 (Kesavananda date) are subject to judicial review on grounds of Basic Structure violation."),

    # ── Section 5: Saving Clauses – Art 31A, 31B, 31C ─────────────────────
    (5, 2,
     "అనుచ్ఛేద 31A ఏమి రక్షిస్తుంది?\n(What does Article 31A save?)",
     "భూ సంస్కరణ చట్టాలను Art 14 మరియు 19 ఆధారంగా సవాలు నుండి / Land reform laws from challenge under Arts 14 and 19",
     "9వ షెడ్యూల్‌లో జాబితా చేసిన చట్టాలను / Laws listed in the 9th Schedule",
     "అన్ని DPSP అమలు చేసే చట్టాలను / All laws implementing DPSPs",
     "అనుచ్ఛేద 32 ద్వారా సవాలు చేయడం నుండి / From challenge under Article 32",
     "a",
     "అనుచ్ఛేద 31A (1వ సవరణ 1951 ద్వారా జోడించబడింది) భూ సంస్కరణ, ఎస్టేట్ రద్దు, జమీందారీ రద్దు వంటి చట్టాలను అనుచ్ఛేద 14 మరియు 19 ఆధారంగా సవాలు చేయడం నుండి రక్షిస్తుంది.\nArticle 31A (added by 1st Amendment 1951) saves laws relating to land reforms, acquisition of estates, abolition of zamindari etc. from being challenged on grounds of Arts 14 and 19."),

    (5, 2,
     "9వ షెడ్యూల్‌కు సంబంధించిన అనుచ్ఛేదం ఏది?\n(Which article relates to the 9th Schedule?)",
     "అనుచ్ఛేద 31A / Article 31A",
     "అనుచ్ఛేద 31B / Article 31B",
     "అనుచ్ఛేద 31C / Article 31C",
     "అనుచ్ఛేద 32 / Article 32",
     "b",
     "అనుచ్ఛేద 31B (1వ సవరణ 1951) 9వ షెడ్యూల్‌లో జాబితా చేసిన చట్టాలను న్యాయ సమీక్ష నుండి రక్షిస్తుంది. I.R. కోయెల్హో కేసు (2007) తర్వాత 24 ఏప్రిల్ 1973 తర్వాత జోడించిన చట్టాలు న్యాయ సమీక్షకు లోబడతాయి.\nArticle 31B (1st Amendment 1951) saves laws placed in 9th Schedule from judicial review. Post I.R. Coelho (2007), laws added after April 24, 1973 are subject to judicial review for Basic Structure violation."),

    (5, 3,
     "కింది వాటిలో అనుచ్ఛేద 31A, 31B మరియు 31C గురించి సరైనది ఏది?\n(Which of the following is correct about Articles 31A, 31B and 31C?)",
     "అన్నీ 1వ సవరణ ద్వారా జోడించబడ్డాయి / All were added by 1st Amendment",
     "31A మరియు 31B 1వ సవరణ (1951) ద్వారా; 31C 25వ సవరణ (1971) ద్వారా జోడించబడ్డాయి / 31A & 31B by 1st Amdt (1951); 31C by 25th Amdt (1971)",
     "31A మరియు 31C 1వ సవరణ ద్వారా; 31B 25వ సవరణ ద్వారా / 31A & 31C by 1st Amdt; 31B by 25th Amdt",
     "అన్నీ 42వ సవరణ ద్వారా జోడించబడ్డాయి / All were added by 42nd Amendment",
     "b",
     "అనుచ్ఛేద 31A మరియు 31B 1వ రాజ్యాంగ సవరణ చట్టం 1951 ద్వారా జోడించబడ్డాయి (చంపకం కేసు తర్వాత). అనుచ్ఛేద 31C 25వ రాజ్యాంగ సవరణ చట్టం 1971 ద్వారా జోడించబడింది.\nArticles 31A and 31B were added by the 1st Constitutional Amendment Act 1951 (after Champakam case). Article 31C was added by the 25th Constitutional Amendment Act 1971."),

    # ── Section 6: FR vs DPSP Comparison & Scholars ───────────────────────
    (6, 2,
     "FR మరియు DPSP ని 'రాజ్యాంగ మనస్సాక్షి' అని ఎవరు అభివర్ణించారు?\n(Who described FRs and DPSPs together as the 'conscience of the Constitution'?)",
     "B.R. అంబేడ్కర్ / B.R. Ambedkar",
     "గ్రాన్‌విల్ ఆస్టిన్ / Granville Austin",
     "జవహర్‌లాల్ నెహ్రూ / Jawaharlal Nehru",
     "K.M. మున్షీ / K.M. Munshi",
     "b",
     "అమెరికన్ రాజ్యాంగ పండితుడు గ్రాన్‌విల్ ఆస్టిన్ FR మరియు DPSP లను కలిపి 'రాజ్యాంగ మనస్సాక్షి' అని అభివర్ణించారు మరియు 'సామాజిక విప్లవం సాధించే సాధనాలు'గా పేర్కొన్నారు.\nAmerican constitutional scholar Granville Austin described FRs and DPSPs together as the 'conscience of the Constitution' and 'core of the commitment to the social revolution'."),

    (6, 1,
     "DPSP లను 'పవిత్ర కోరికలు' (pious wishes) అని ఎవరు అభివర్ణించారు?\n(Who described DPSPs as 'pious wishes'?)",
     "T.T. కృష్ణమాచారి / T.T. Krishnamachari",
     "B.R. అంబేడ్కర్ / B.R. Ambedkar",
     "K.T. షా / K.T. Shah",
     "నజీరుద్దీన్ అహ్మద్ / Naziruddin Ahmad",
     "a",
     "T.T. కృష్ణమాచారి రాజ్యాంగ పరిషత్‌లో DPSP లను 'పవిత్ర కోరికలు' అని అభివర్ణించారు, ఎందుకంటే వాటిని అమలు చేయించడానికి న్యాయపరమైన శక్తి లేదు.\nT.T. Krishnamachari described DPSPs as 'pious wishes' in the Constituent Assembly because they have no judicial enforcement mechanism."),

    (6, 2,
     "FR మరియు DPSP మధ్య ముఖ్యమైన వ్యత్యాసం ఏమిటి?\n(What is a key difference between FRs and DPSPs?)",
     "DPSP లు న్యాయస్థానాల ద్వారా అమలు చేయవచ్చు, FR లు చేయలేవు / DPSPs are justiciable, FRs are not",
     "FR లు ప్రతికూల బాధ్యతలు (చేయకూడనివి), DPSP లు సానుకూల బాధ్యతలు (చేయవలసినవి) / FRs are negative obligations, DPSPs are positive obligations",
     "FR లు రాజ్యంపై విధించబడతాయి, DPSP లు పౌరులపై / FRs on State, DPSPs on citizens",
     "FR లు సహకార జాబితాలో ఉన్నాయి / FRs are in Concurrent List",
     "b",
     "FR లు ప్రతికూల బాధ్యతలు (రాజ్యం ఏమి చేయకూడదో) కాగా DPSP లు సానుకూల బాధ్యతలు (రాజ్యం ఏమి చేయాలో). FR లు న్యాయస్థానాల ద్వారా అమలు చేయదగినవి; DPSP లు చేయలేనివి.\nFRs are negative obligations (what the State must NOT do) while DPSPs are positive obligations (what the State SHOULD do). FRs are justiciable; DPSPs are non-justiciable."),

    (6, 2,
     "DPSP అమలుకు B.R. అంబేడ్కర్ దృష్టిలో ఏ లక్ష్యం ఉంది?\n(What was B.R. Ambedkar's vision for the purpose of DPSPs?)",
     "DPSP లు అర్థరహితమైన పవిత్ర కోరికలు / DPSPs are meaningless pious wishes",
     "రాజకీయ ప్రజాస్వామ్యాన్ని సాంఘిక-ఆర్థిక ప్రజాస్వామ్యంగా మార్చే సాధనాలు / Instruments to transform political democracy into socio-economic democracy",
     "DPSP లు పాశ్చాత్య సంప్రదాయం / DPSPs are a Western tradition",
     "DPSP లు పాలనపై కేవలం నైతిక బాధ్యతలు / DPSPs are mere moral obligations on governance",
     "b",
     "B.R. అంబేడ్కర్ DPSP లను రాజకీయ ప్రజాస్వామ్యాన్ని సాంఘిక మరియు ఆర్థిక ప్రజాస్వామ్యంగా మార్చే లక్ష్యంతో రూపొందించారు. FR లు రాజకీయ ప్రజాస్వామ్యాన్ని నిర్ధారిస్తే, DPSP లు సామాజిక-ఆర్థిక ప్రజాస్వామ్యాన్ని సాధించడానికి మార్గదర్శనం చేస్తాయి.\nB.R. Ambedkar envisioned DPSPs as instruments to transform political democracy into social and economic democracy. While FRs establish political democracy, DPSPs guide the State towards socio-economic democracy."),

    (6, 3,
     "FR మరియు DPSP ల మధ్య సంఘర్షణ వేళ న్యాయస్థానాల సమన్వయ విధానం ఏమిటి?\n(What is the courts' harmonious construction approach in case of conflict between FRs and DPSPs?)",
     "DPSP లు ఎల్లప్పుడూ FR లపై గెలుస్తాయి / DPSPs always prevail over FRs",
     "FR లు ఎల్లప్పుడూ DPSP లపై గెలుస్తాయి / FRs always prevail over DPSPs",
     "రెండింటికీ ఆచరణ సాధ్యమైన అర్థం ఇవ్వడం; ఒకదాన్ని పూర్తిగా నాశనం చేయకూడదు / Give practical meaning to both without completely abrogating one",
     "పార్లమెంటు తీర్మానం ద్వారా నిర్ణయించబడతాయి / Decided through Parliament resolution",
     "c",
     "సుప్రీంకోర్టు FR మరియు DPSP ల మధ్య సమన్వయ అర్థఘటన విధానాన్ని అనుసరిస్తుంది — రెండింటికీ ఆచరణ సాధ్యమైన అర్థం ఇవ్వడం. కేశవానంద భారతి మరియు మినర్వా మిల్స్ కేసులు ఈ సమతుల్యతను నొక్కిచెప్పాయి.\nThe SC follows harmonious construction — giving practical meaning to both FRs and DPSPs without completely destroying one. Kesavananda Bharati and Minerva Mills cases emphasized this balance."),

    # ── Section 7: Difficult / APPSC-Style MCQs ────────────────────────────
    (7, 3,
     "కింది వాటిలో ఏది సమాజవాద (Socialistic) DPSP కాదు?\n(Which of the following is NOT a Socialistic DPSP?)",
     "అనుచ్ఛేద 39A - ఉచిత న్యాయ సహాయం / Art 39A - Free legal aid",
     "అనుచ్ఛేద 41 - పని హక్కు / Art 41 - Right to work",
     "అనుచ్ఛేద 44 - ఏకరీతి పౌర స్మృతి / Art 44 - Uniform Civil Code",
     "అనుచ్ఛేద 43A - నిర్వహణ భాగస్వామ్యం / Art 43A - Participation in management",
     "c",
     "అనుచ్ఛేద 44 (ఏకరీతి పౌర స్మృతి) ఉదారవాద-మేధో నిర్దేశక సూత్రం. సమాజవాద DPSPs: 38, 39, 39A, 41, 42, 43, 43A, 43B, 47. గాంధేయ: 40, 43, 46, 47, 48. ఉదారవాద-మేధో: 44, 45, 48, 48A, 49, 50, 51.\nArticle 44 (Uniform Civil Code) is a Liberal-Intellectual DPSP. Socialistic DPSPs: 38, 39, 39A, 41, 42, 43, 43A, 43B, 47. Gandhian: 40, 43, 46, 47, 48. Liberal-Intellectual: 44, 45, 48, 48A, 49, 50, 51."),

    (7, 3,
     "కింది DPSP వర్గీకరణ జతలలో ఏది సరైనది?\n(Which DPSP classification pairing is correct?)",
     "అనుచ్ఛేద 40 - సమాజవాద / Art 40 - Socialistic",
     "అనుచ్ఛేద 50 - గాంధేయ / Art 50 - Gandhian",
     "అనుచ్ఛేద 48A - ఉదారవాద-మేధో / Art 48A - Liberal-Intellectual",
     "అనుచ్ఛేద 47 - ఉదారవాద-మేధో / Art 47 - Liberal-Intellectual",
     "c",
     "అనుచ్ఛేద 48A (పర్యావరణ పరిరక్షణ) ఉదారవాద-మేధో నిర్దేశక సూత్రం. అనుచ్ఛేద 40 గాంధేయ, అనుచ్ఛేద 50 ఉదారవాద-మేధో, అనుచ్ఛేద 47 సమాజవాద (పోషణ) మరియు గాంధేయ (నిషేధం) రెండు వర్గాలలోనూ ఉంటుంది.\nArt 48A (Environment protection) is Liberal-Intellectual. Art 40 is Gandhian, Art 50 is Liberal-Intellectual, Art 47 falls under both Socialistic (nutrition) and Gandhian (prohibition) categories."),

    (7, 3,
     "కింది వాటిలో DPSP కాని అంశం ఏది?\n(Which of the following is NOT a DPSP?)",
     "ఏకరీతి పౌర స్మృతి / Uniform Civil Code",
     "న్యాయ-కార్యనిర్వాహక వేర్పాటు / Separation of Judiciary and Executive",
     "అంటరానితనం నిషేధం / Prohibition of Untouchability",
     "అంతర్జాతీయ శాంతి ప్రోత్సాహం / Promotion of International Peace",
     "c",
     "అంటరానితనం నిషేధం (అనుచ్ఛేద 17) ఒక మూల హక్కు (FR), DPSP కాదు. ఏకరీతి పౌర స్మృతి (అనుచ్ఛేద 44), వేర్పాటు (అనుచ్ఛేద 50), అంతర్జాతీయ శాంతి (అనుచ్ఛేద 51) DPSP లు.\nProhibition of untouchability (Article 17) is a Fundamental Right, NOT a DPSP. Uniform Civil Code (Art 44), Separation of Judiciary (Art 50), and International Peace (Art 51) are DPSPs."),

    # ── Section 0 (extra): Instruments of Instructions & Art 38(2) ────────
    (0, 3,
     "B.R. అంబేడ్కర్ DPSP లను ఏ చారిత్రక దస్తావేజుతో పోల్చారు?\n(B.R. Ambedkar compared DPSPs to which historical document?)",
     "1935 భారత ప్రభుత్వ చట్టంలోని 'నిర్దేశ పత్రాలు' / 'Instruments of Instructions' in the Government of India Act 1935",
     "1919 భారత ప్రభుత్వ చట్టంలోని పరిపాలన నిబంధనలు / Administrative rules in the Government of India Act 1919",
     "ఐర్లాండ్ రాజ్యాంగంలోని సూత్రాలు / Principles in the Irish Constitution",
     "బ్రిటన్ మాగ్నా కార్టా / Britain's Magna Carta",
     "a",
     "B.R. అంబేడ్కర్ DPSP లను 1935 భారత ప్రభుత్వ చట్టంలోని 'నిర్దేశ పత్రాలు' (Instruments of Instructions) తో పోల్చారు, ఇవి గవర్నర్-జనరల్ మరియు గవర్నర్లకు తమ విచక్షణాధికారాలను వినియోగించుకునే విధానంపై జారీ చేయబడిన ఆదేశాలు.\nB.R. Ambedkar compared DPSPs to the 'Instruments of Instructions' issued under the Government of India Act 1935 — these were directions issued to the Governor-General and Governors on how to exercise their discretionary powers."),

    (0, 3,
     "అనుచ్ఛేద 38కు రెండవ ఖండం (clause 2) ఏ సవరణ ద్వారా జోడించబడింది మరియు ఏమి నిర్దేశిస్తుంది?\n(Which amendment added clause (2) to Article 38 and what does it direct?)",
     "25వ సవరణ 1971 – సంపద కేంద్రీకరణ నివారణ / 25th Amdt 1971 – prevention of wealth concentration",
     "42వ సవరణ 1976 – పరిశ్రమ నిర్వహణ భాగస్వామ్యం / 42nd Amdt 1976 – industrial management participation",
     "44వ సవరణ 1978 – ఆదాయం, హోదా, సదుపాయాలలో అసమానతలు తగ్గించడం / 44th Amdt 1978 – minimise inequalities in income, status and opportunities",
     "86వ సవరణ 2002 – విద్యా అవకాశాలలో అసమానత నివారణ / 86th Amdt 2002 – educational inequality prevention",
     "c",
     "44వ రాజ్యాంగ సవరణ చట్టం 1978 అనుచ్ఛేద 38కు ఖండం (2) జోడించింది, ఇది రాజ్యం వ్యక్తులలో హోదా, సదుపాయాలు మరియు అవకాశాలలో అసమానతలను తగ్గించడానికి ప్రయత్నించాలని, ప్రాంతాల మధ్య అసమానతలను కూడా తగ్గించాలని నిర్దేశిస్తుంది.\nThe 44th Constitutional Amendment Act 1978 added clause (2) to Article 38, directing the State to minimise inequalities in income, status, facilities and opportunities among individuals, and also to eliminate inequalities among different areas."),

    # ── Extra Socialistic DPSPs (Section 1) ──────────────────────────────────────
    (1, 1,
     "Article 39(b) ఏమి నిర్దేశిస్తుంది?\n(What does Article 39(b) direct?)",
     "సమాన వేతనం (Equal Pay)",
     "సమాజ భౌతిక వనరుల పంపిణీ — సమానత్వం (Distribution of material resources for common good)",
     "పర్యావరణ పరిరక్షణ (Environment Protection)",
     "పాఠశాల విద్య (Free & Compulsory Education)",
     "b",
     "Art.39(b): The State shall direct its policy towards securing that the ownership and control of the material resources of the community are so distributed as best to subserve the common good. Art.39(c): Prevent concentration of wealth. Art.39(d): Equal pay for equal work."),

    (1, 2,
     "కింది DPSP ల జోడీలలో Art.39(d) ఏమి నిర్దేశిస్తుంది?\n(What does Art.39(d) direct?)",
     "పిల్లల ఆరోగ్యకరమైన అభివృద్ధి",
     "మహిళలకు సమాన న్యాయం",
     "స్త్రీ-పురుషులకు సమాన పని కు సమాన వేతనం (Equal pay for equal work for men and women)",
     "పర్యావరణ పరిరక్షణ",
     "c",
     "Art.39(d): Equal pay for equal work for both men and women. ఇది ప్రాథమిక హక్కు కాదు, DPSP మాత్రమే — కానీ Court లు దీన్ని Art.14 (Equality) తో కలిపి అన్వయిస్తాయి. Randhir Singh vs UoI (1982) కేసులో Supreme Court ఈ సూత్రాన్ని అమలు చేసింది.",
     "APPSC"),

    (1, 2,
     "Art.41 ప్రకారం రాజ్యం ఏమి నిర్దేశించాలి?\n(What does Art.41 direct the State to secure?)",
     "ఉచిత విద్య మరియు ఆరోగ్య సేవలు",
     "పని హక్కు, విద్యా హక్కు, నిరుద్యోగం మరియు వృద్ధాప్యంలో సహాయం",
     "గ్రామ పంచాయితీల స్థాపన",
     "ఏకరూప పౌర స్మృతి (Uniform Civil Code)",
     "b",
     "Art.41: The State shall make effective provision for securing the right to work, to education and to public assistance in cases of unemployment, old age, sickness and disablement. ఇది Socialistic DPSP. MGNREGA, National Pension Scheme, Aajeevika వంటివి ఈ ఆర్టికల్ ని అమలు పరుస్తాయి."),

    (1, 2,
     "Art.43 ఏమి నిర్దేశిస్తుంది?\n(What does Art.43 direct?)",
     "పర్యావరణ పరిరక్షణ",
     "కార్మికులకు జీవన వేతనం (Living Wage for Workers)",
     "గ్రామ పంచాయితీల అభివృద్ధి",
     "వ్యవసాయ మద్యపానం నిషేధం",
     "b",
     "Art.43: The State shall endeavour to secure a living wage, work conditions and full enjoyment of leisure for all workers. Art.43A (42nd Amendment 1976): Workers' participation in management of industries. Art.43B (97th Amendment 2011): Promotion of co-operative societies."),

    (1, 3,
     "42వ రాజ్యాంగ సవరణ (1976) DPSP కు ఏ కొత్త ఆర్టికల్స్ జోడించింది?\n(Which new Articles were added to DPSPs by the 42nd Amendment 1976?)",
     "Art.38(2), Art.39A",
     "Art.39A, Art.43A, Art.48A",
     "Art.44, Art.46, Art.47",
     "Art.40, Art.41, Art.42",
     "b",
     "42వ సవరణ 1976: Art.39A (Free legal aid), Art.43A (Workers' participation in management), Art.48A (Environment protection) — ఈ మూడు కొత్తగా DPSP కి జోడించబడ్డాయి. 44వ సవరణ 1978: Art.38(2). 86వ సవరణ 2002: Art.45 ని మార్చి (6 సంవత్సరాల లోపు పిల్లలకు సంరక్షణ)."),

    # ── Extra Gandhian DPSPs (Section 2) ─────────────────────────────────────────
    (2, 1,
     "Art.40 ఏమి నిర్దేశిస్తుంది?\n(What does Art.40 direct?)",
     "సమాన న్యాయం మరియు ఉచిత న్యాయ సహాయం",
     "గ్రామ పంచాయితీల వ్యవస్థాపన మరియు స్వయంపాలన (Village Panchayats organisation and self-governance)",
    "కుటీర పరిశ్రమల అభివృద్ధి",
     "వ్యవసాయ విజ్ఞాన శాస్త్రం అభివృద్ధి",
     "b",
     "Art.40: The State shall take steps to organise village panchayats and endow them with such powers and authority as may be necessary to enable them to function as units of self-government. 73వ సవరణ 1992 ద్వారా ఈ Gandhian DPSP ఆచరణలో అమలైంది — Panchayati Raj constitutional status పొందింది.",
     "APPSC"),

    (2, 2,
     "Art.46 ఏ వర్గాలకు విద్యా-ఆర్థిక అభివృద్ధి నిర్దేశిస్తుంది?\n(Art.46 directs educational and economic development of which groups?)",
     "వ్యవసాయదారులు మరియు కార్మికులు",
     "మహిళలు మరియు పిల్లలు",
     "SC/ST లు మరియు ఇతర బలహీన వర్గాలు (SC, ST and weaker sections)",
     "ముస్లిం మైనారిటీలు",
     "c",
     "Art.46 (Gandhian DPSP): రాజ్యం SC, ST మరియు ఇతర బలహీన వర్గాల (weaker sections) విద్య మరియు ఆర్థిక ప్రయోజనాలను ప్రత్యేక శ్రద్ధతో అభివృద్ధి చేయాలి. వారిని సామాజిక అన్యాయం మరియు అన్ని రూపాల దోపిడీ నుండి రక్షించాలి."),

    (2, 2,
     "Art.47 రాజ్యానికి ఏమి నిర్దేశిస్తుంది?\n(What does Art.47 direct the State?)",
     "పర్యావరణ పరిరక్షణ",
     "పౌషకాహార స్థాయి మరియు ప్రజారోగ్యం మెరుగుపరచడం; మత్తు పదార్థాలు నిషేధించడం\n(Raise nutrition level, public health; prohibit intoxicating drinks except medicinal use)",
     "జంతు వధ నిషేధించడం",
     "పంచాయితీ స్వయంపాలన",
     "b",
     "Art.47 (Gandhian DPSP): రాజ్యం (1) ప్రజల పోషకాహార స్థాయి మరియు జీవన ప్రమాణాన్ని పెంచాలి, (2) ప్రజారోగ్యం మెరుగుపరచాలి, (3) వైద్య ప్రయోజనాలు తప్ప మద్యపానం మరియు ఇతర మత్తు పదార్థాలను నిషేధించాలి. Dry State policies ఈ ఆర్టికల్ ఆధారంగా ఉన్నాయి."),

    (2, 2,
     "Art.48 ఏమి నిర్దేశిస్తుంది?\n(What does Art.48 direct?)",
     "గ్రామ పంచాయితీల బలోపేతం",
     "వ్యవసాయం, పశుసంవర్ధనం నవీకరణ; ఆవులు-దూడల వధ నిషేధం (Agriculture modernisation; prohibit slaughter of cows and calves)",
     "వనాలు సంరక్షణ",
     "కార్మికులకు నీతి నిబంధనలు",
     "b",
     "Art.48 (Gandhian DPSP): రాజ్యం వ్యవసాయం మరియు పశుపోషణను ఆధునిక రీతిలో అమర్చాలి; ముఖ్యంగా ఆవులు, దూడలు మరియు ఇతర పాడి పశువుల వధ నిషేధించడానికి చర్యలు తీసుకోవాలి. Art.48A (42nd Amdt): Environment protection and forests."),

    # ── Extra Liberal-Intellectual DPSPs (Section 3) ─────────────────────────────
    (3, 1,
     "Art.44 ఏ DPSP ని నిర్దేశిస్తుంది?\n(Which DPSP is directed by Art.44?)",
     "న్యాయ సహాయం (Legal Aid)",
     "ఏకరూప పౌర స్మృతి — Uniform Civil Code (UCC)",
     "పర్యావరణ పరిరక్షణ",
     "అంతర్జాతీయ శాంతి",
     "b",
     "Art.44: Uniform Civil Code (UCC) — రాజ్యం భారత భూభాగం అంతటా పౌరులకు ఒకే UCC వర్తింపజేయడానికి ప్రయత్నించాలి. ఇది అత్యంత వివాదాస్పద DPSP — వ్యక్తిగత మత చట్టాలకు వ్యతిరేకంగా పని చేస్తుంది. SC ఈ విషయంలో అనేక కేసుల్లో పార్లమెంట్ ను UCC అమలు చేయమని పిలుపిచ్చింది."),

    (3, 2,
     "Art.45 ప్రస్తుతం (86వ సవరణ 2002 తర్వాత) ఏమి నిర్దేశిస్తుంది?\n(What does Art.45 direct after the 86th Amendment 2002?)",
     "14 సంవత్సరాల వరకు ఉచిత మరియు నిర్బంధ విద్య (Free & Compulsory Education up to 14 yrs)",
     "6 సంవత్సరాల లోపు పిల్లల తొలి బాల్య సంరక్షణ మరియు విద్య (Early childhood care & education for children below 6 yrs)",
     "20 సంవత్సరాల వరకు ఉచిత విద్య",
     "వృత్తి విద్య (Vocational Education)",
     "b",
     "86వ సవరణ 2002 Art.45 ని మార్చింది: ఇప్పుడు 6 సంవత్సరాల కంటే తక్కువ వయసు పిల్లలకు తొలి బాల్య సంరక్షణ మరియు విద్య. మూల Art.45 (14 ఏళ్ళ వరకు ఉచిత విద్య) Art.21A గా ప్రాథమిక హక్కు అయింది (RTE Act 2009). ఇది మాజీ DPSP నుండి ప్రాథమిక హక్కుకు పరిణామం.",
     "APPSC"),

    (3, 2,
     "Art.48A DPSP కు ఎప్పుడు జోడించారు మరియు ఏమి నిర్దేశిస్తుంది?\n(When was Art.48A added and what does it direct?)",
     "44వ సవరణ 1978 — వ్యవసాయం అభివృద్ధి",
     "86వ సవరణ 2002 — ప్రాథమిక విద్య",
     "42వ సవరణ 1976 — పర్యావరణం రక్షించడం, వనాలు మరియు వన్యప్రాణులు (Environment protection, forests, wildlife)",
     "73వ సవరణ 1992 — పంచాయితీ స్వయంపాలన",
     "c",
     "Art.48A: 42వ రాజ్యాంగ సవరణ 1976 ద్వారా జోడించారు. 'The State shall endeavour to protect and improve the environment and to safeguard the forests and wild life of the country.' M.C. Mehta vs Union of India కేసులో Supreme Court ఈ ఆర్టికల్ ను Art.21 తో కలిపి వ్యాఖ్యానించింది."),

    (3, 2,
     "Art.50 ఏమి నిర్దేశిస్తుంది?\n(What does Art.50 direct?)",
     "జ్యుడీషియరీ నియామకాలు",
     "కార్యనిర్వాహక వ్యవస్థ నుండి న్యాయవ్యవస్థ వేర్పాటు (Separation of Judiciary from Executive)",
     "అంతర్జాతీయ సంధులు పాటించడం",
     "మత విద్యాలయాలకు సహాయం",
     "b",
     "Art.50 (Liberal-Intellectual DPSP): రాజ్యం రాజ్యంలోని న్యాయ సేవలలో కార్యనిర్వాహకులను న్యాయమూర్తుల నుండి వేర్పాటు చేయాలి. Subordinate courts లో Executive Magistrates మరియు Judicial Magistrates వేర్పాటు ఈ ఆర్టికల్ ఆదర్శం. న్యాయవ్యవస్థ స్వాతంత్ర్యానికి ప్రాముఖ్యత ఇస్తుంది."),

    (3, 2,
     "Art.51 ఏ DPSP ని నిర్దేశిస్తుంది?\n(Which DPSP does Art.51 direct?)",
     "గ్రామ పంచాయితీలు",
     "ఏకరూప పౌర స్మృతి",
     "అంతర్జాతీయ శాంతి మరియు భద్రత (International Peace and Security)",
     "పర్యావరణ పరిరక్షణ",
     "c",
     "Art.51 (Liberal-Intellectual DPSP): రాజ్యం అంతర్జాతీయ శాంతి మరియు భద్రత కాపాడటానికి, దేశాల మధ్య న్యాయమైన సంబంధాలు అభివృద్ధి చేయడానికి, అంతర్జాతీయ చట్టాన్ని గౌరవించడానికి ప్రయత్నించాలి. India's foreign policy (Non-Alignment, SAARC, UN participation) ఈ ఆర్టికల్ స్ఫూర్తి నుండి వచ్చింది."),

    # ── Extra FR vs DPSP Conflict & Cases (Section 4) ────────────────────────────
    (4, 2,
     "State of Madras vs Champakam Dorairajan (1951) కేసు DPSP-FR వివాదంలో ఏ నిర్ణయం ఇచ్చింది?\n(What was decided in Champakam Dorairajan 1951 regarding DPSP-FR conflict?)",
     "DPSP లు FR కు సమానంగా ఉన్నాయి",
     "FR లు DPSP కంటే ఉన్నతమైనవి — Communal GO రద్దు",
     "DPSP లు FR ను మార్చగలవు",
     "DPSP లు న్యాయస్థానాల ద్వారా అమలు చేయవచ్చు",
     "b",
     "Champakam Dorairajan (1951): SC ruled FR take precedence over DPSP when in conflict. Madras communal GO (caste-based college admissions) violated Art.15(1). This was India's first major FR-DPSP conflict case. 1st Constitutional Amendment (1951): Art.15(4) added to override this judgment.",
     "APPSC"),

    (4, 2,
     "ఏ రాజ్యాంగ సవరణ DPSP ల అమలుకు తీసుకున్న చట్టాలను FR ల నుండి రక్షించింది (Art.31C)?\n(Which Amendment introduced Art.31C to protect DPSP-implementing laws from FR challenge?)",
     "24వ సవరణ 1971", "25వ సవరణ 1971",
     "42వ సవరణ 1976", "44వ సవరణ 1978",
     "b",
     "25వ రాజ్యాంగ సవరణ 1971: Art.31C జోడించారు — DPSP Art.39(b)(c) అమలుకు చేసిన చట్టాలు FR Art.14 & Art.19 లకు వ్యతిరేకంగా న్యాయస్థానంలో సవాల్ చేయలేరు. Kesavananda Bharati (1973) కేసు: Art.31C ని పాక్షికంగా చెల్లుబాటు చేసింది. Minerva Mills (1980): 42nd Amdt విస్తరణ రద్దు చేసింది.",
     "APPSC"),

    (4, 3,
     "Minerva Mills vs Union of India (1980) కేసులో SC ఏ ముఖ్యమైన నిర్ణయం ఇచ్చింది?\n(What important decision was given in Minerva Mills vs UoI 1980?)",
     "DPSP లు FR కంటే ఉన్నతమైనవి",
     "42వ సవరణ ద్వారా అన్ని DPSP లకు రక్షణ ఇవ్వడం రాజ్యాంగ విరుద్ధం — FR-DPSP సమతుల్యత రాజ్యాంగ మూల నిర్మాణంలో భాగం",
     "FR లు DPSP ని రద్దు చేయగలవు",
     "పార్లమెంట్ FR లు తొలగించగలదు",
     "b",
     "Minerva Mills (1980): 42nd Amendment ద్వారా అన్ని DPSP లకు Art.31C రక్షణ విస్తరించడం చెల్లుబాటు కాదు — ఇది FR-DPSP పరస్పర సమతుల్యత (Harmony) ని భంగం చేస్తుంది. SC: FR మరియు DPSP రెండూ రాజ్యాంగ మూల నిర్మాణంలో భాగం — ఒకటి మరొకటిపై ఆధిపత్యం చెలాయించకూడదు.",
     "APPSC"),

    (4, 2,
     "Unnikrishnan vs State of AP (1993) కేసు ఏ హక్కుని DPSP నుండి ప్రాథమిక హక్కు స్థాయికి తీసుకువచ్చింది?\n(Unnikrishnan vs State of AP 1993 elevated which right from DPSP to FR level?)",
     "పని హక్కు (Right to Work)",
     "విద్యా హక్కు (Right to Education)",
     "ఆరోగ్య హక్కు (Right to Health)",
     "వాతావరణ హక్కు (Right to Clean Environment)",
     "b",
     "Unnikrishnan (1993): SC ruled Right to Education is a Fundamental Right derived from Art.21 (Right to Life). ఈ కేసు DPSP Art.45 ని Art.21 తో కలిపి వ్యాఖ్యానించింది. తర్వాత 86వ సవరణ 2002 ద్వారా Art.21A (RTE) ప్రత్యేక ప్రాథమిక హక్కుగా జోడించారు."),

    # ── Extra 9th Schedule / Art.31B (Section 5) ─────────────────────────────────
    (5, 2,
     "9వ షెడ్యూల్ (Ninth Schedule) ఏ సవరణ ద్వారా జోడించారు మరియు ఎందుకు?\n(Ninth Schedule added by which Amendment and why?)",
     "42వ సవరణ 1976 — అత్యవసర పరిస్థితి చట్టాలు రక్షించడానికి",
     "1వ సవరణ 1951 — భూ సంస్కరణ చట్టాలను FR సవాళ్ళ నుండి రక్షించడానికి",
     "25వ సవరణ 1971 — ప్రాపర్టీ హక్కు రద్దుకు",
     "44వ సవరణ 1978 — ఎమర్జెన్సీ తర్వాత పునరుద్ధరణకు",
     "b",
     "9వ షెడ్యూల్: 1వ రాజ్యాంగ సవరణ 1951 ద్వారా జోడించారు. Art.31B కింద: 9వ షెడ్యూల్ లో ఉన్న చట్టాలు FR (Art.13) ద్వారా సవాల్ చేయలేరు. ఉద్దేశ్యం: జమీందారీ విధానం రద్దు చట్టాలు (Land Reforms) రక్షించడం. I.R. Coelho (2007): 1973 తర్వాత జోడించిన 9th Schedule చట్టాలు న్యాయ సమీక్షకు అర్హమైనవి.",
     "APPSC"),

    (5, 3,
     "I.R. Coelho vs State of Tamil Nadu (2007) కేసులో SC ఏ ముఖ్యమైన నిర్ణయం ఇచ్చింది?\n(What key ruling came in I.R. Coelho vs TN 2007?)",
     "9వ షెడ్యూల్ లోని అన్ని చట్టాలు న్యాయ సమీక్షకు అర్హం",
     "Kesavananda Bharati తర్వాత (1973 April 24 తర్వాత) 9వ షెడ్యూల్ కి జోడించిన చట్టాలు BS ని ఉల్లంఘిస్తే న్యాయ సమీక్ష వర్తిస్తుంది",
     "9వ షెడ్యూల్ పూర్తిగా రద్దు",
     "DPSP లు FR కు సమానం",
     "b",
     "I.R. Coelho (2007): 9-judge Constitution Bench — 1973 April 24 (Kesavananda judgment date) తర్వాత 9th Schedule కు జోడించిన చట్టాలు, అవి Basic Structure ని ఉల్లంఘిస్తే, న్యాయ సమీక్షకు అర్హమైనవి. 1973 కంటే ముందు చట్టాలు రక్షింపబడతాయి. ఇది Basic Structure doctrine ని 9th Schedule పై వర్తింపజేసిన సందర్భం."),

    # ── Extra Comparison / Tough (Section 6/7) ───────────────────────────────────
    (6, 1,
     "Granville Austin DPSP మరియు FR ల మధ్య సంబంధాన్ని ఏ పదంతో వర్ణించారు?\n(How did Granville Austin describe the relationship between FR and DPSP?)",
     "Conflict and Contradiction (వివాదం మరియు విరుద్ధం)",
     "Conscience of the Constitution (రాజ్యాంగ చేతన) — రెండూ కలిసి 'Conscience'",
     "Separate and Parallel (వేర్వేరు మరియు సమాంతర)",
     "Primary and Secondary Rights (ప్రాథమిక మరియు ద్వితీయ హక్కులు)",
     "b",
     "Granville Austin: FR మరియు DPSP రెండూ కలిసి 'Conscience of the Constitution' ని ఏర్పరుస్తాయి — ఇవి రాజ్యాంగ సామాజిక విప్లవం (Social Revolution) యొక్క రెండు పక్కలు. FR = Negative Obligations (రాజ్యం చేయకూడనివి). DPSP = Positive Obligations (రాజ్యం చేయవలసినవి)."),

    (6, 2,
     "DPSP లు 'Non-Justiciable' (న్యాయస్థానంలో అమలు చేయలేని) అయినప్పటికీ అవి 'Fundamental' ఎందుకు?\n(Why are DPSPs 'Fundamental' even though Non-Justiciable?)",
     "అవి FR లకు ఉన్నతమైనవి కాబట్టి",
     "అవి పాలనలో ప్రాథమికంగా ఉంటాయి — చట్టాలు చేయడంలో మార్గదర్శకాలు\n(Fundamental in governance — guidelines for law-making)",
     "అవి రాష్ట్రపతి ద్వారా అమలు చేయవచ్చు",
     "అవి Supreme Court తీర్పుల ద్వారా అమలు చేయవచ్చు",
     "b",
     "Art.37: DPSP లు 'fundamental in governance of the country and it shall be the duty of the State to apply these principles in making laws.' అంటే పాలనలో ప్రాథమికమైనవి — court అమలు చేయలేకపోయినా. అందుకే 'Directive Principles of State Policy' — ప్రభుత్వ విధానాలకు మార్గదర్శకాలు."),

    (7, 2,
     "DPSP ల అమలు చేసిన ముఖ్యమైన చట్టాలు — Art.45 ఆధారంగా ఏ చట్టం చేశారు?\n(Which Act was enacted to implement Art.45 — RTE?)",
     "Right to Information Act 2005",
     "Right of Children to Free and Compulsory Education Act 2009 (RTE Act)",
     "Protection of Children from Sexual Offences Act 2012",
     "Juvenile Justice Act 2015",
     "b",
     "Right of Children to Free and Compulsory Education Act 2009 (RTE Act) = Art.21A + Art.45 ఆధారంగా. 6-14 సంవత్సరాల పిల్లలకు ఉచిత మరియు నిర్బంధ విద్య. 86వ సవరణ 2002 ద్వారా Art.21A ప్రాథమిక హక్కు అయింది. ఈ RTE Act 2009 ఏప్రిల్ 1, 2010 నుండి అమలైంది.",
     "APPSC"),

    (7, 3,
     "కింది DPSP ఆర్టికల్స్ జోడీని సరిగ్గా సరిపోల్చండి:\nArt.39A — Art.43A — Art.48A ఏ సవరణ ద్వారా జోడించారు?\n(Art.39A, Art.43A, Art.48A — added by which Amendment?)",
     "1వ సవరణ 1951", "25వ సవరణ 1971",
     "42వ సవరణ 1976", "44వ సవరణ 1978",
     "c",
     "42వ రాజ్యాంగ సవరణ 1976 (అత్యవసర పరిస్థితి కాలంలో): మూడు కొత్త DPSP ఆర్టికల్స్: Art.39A (Equal Justice and Free Legal Aid), Art.43A (Workers' participation in industry management), Art.48A (Environment protection). ఇవి పరీక్షలలో తరచుగా అడుగుతారు — ఈ మూడూ 42nd Amdt అని గుర్తుంచుకోండి.",
     "APPSC"),

    (7, 2,
     "DPSP లు 'Part IV' లో ఉన్నాయి. Part IV ఏ ఆర్టికల్ నుండి ఏ ఆర్టికల్ వరకు ఉంది?\n(Part IV (DPSPs) spans which Articles?)",
     "Art.12 to Art.35", "Art.36 to Art.51",
     "Art.52 to Art.78", "Art.243 to Art.243ZT",
     "b",
     "DPSP లు భారత రాజ్యాంగం Part IV లో Art.36 నుండి Art.51 వరకు ఉన్నాయి. Art.36 = 'State' నిర్వచనం (FRs లాగా). Art.37 = DPSP యొక్క స్వభావం (Non-Justiciable, Fundamental in governance). Art.38-51 = వివిధ DPSP లు."),

    (7, 2,
     "DPSP Art.39A (సమాన న్యాయం మరియు ఉచిత న్యాయ సహాయం) ఏ చట్టం ద్వారా అమలైంది?\n(Art.39A on Equal Justice and Free Legal Aid was implemented through which Act?)",
     "Legal Services Authorities Act 1987",
     "Advocates Act 1961",
     "Criminal Procedure Code 1973",
     "Consumer Protection Act 1986",
     "a",
     "Legal Services Authorities Act 1987 = Art.39A అమలు. National Legal Services Authority (NALSA) ద్వారా పేద మరియు అట్టడుగు వర్గాలకు ఉచిత న్యాయ సహాయం అందిస్తారు. Hussainara Khatoon Case (1979) లో SC ఈ హక్కును Art.21 కింద ప్రాథమిక హక్కుగా గుర్తించింది.",
     "APPSC"),

    (7, 3,
     "DPSP Art.43B ఏ సవరణ ద్వారా జోడించారు మరియు ఏమి నిర్దేశిస్తుంది?\n(Art.43B was added by which Amendment and directs what?)",
     "42వ సవరణ 1976 — పర్యావరణ పరిరక్షణ",
     "86వ సవరణ 2002 — విద్యా హక్కు",
     "97వ సవరణ 2011 — సహకార సంఘాల (Co-operative Societies) ప్రోత్సాహం",
     "101వ సవరణ 2016 — GST అమలు",
     "c",
     "Art.43B: 97వ రాజ్యాంగ సవరణ 2011 ద్వారా జోడించారు. 'The State shall endeavour to promote voluntary formation, autonomous functioning, democratic control and professional management of co-operative societies.' Part IX-B కూడా జోడించారు (Co-operative Societies). ఇది సమీప సంవత్సరాల్లో పరీక్షలలో అడిగే అంశం."),

    (1, 2,
     "Art.39(c) ఏమి నిర్దేశిస్తుంది?\n(What does Art.39(c) direct?)",
     "సమాన వేతనం (Equal Pay for Equal Work)",
     "ఆర్థిక వ్యవస్థలో సంపద మరియు ఉత్పత్తి సాధనాల కేంద్రీకరణ నివారించడం\n(Prevention of concentration of wealth and means of production)",
     "పని హక్కు (Right to Work)",
     "పిల్లల హక్కుల రక్షణ",
     "b",
     "Art.39(c): The State shall direct its policy towards securing that the operation of the economic system does not result in the concentration of wealth and means of production to the common detriment. ఇది ప్రైవేటు మోనోపలీలు, కార్టెల్స్ నివారణకు ఆధారం. Competition Act 2002 ఈ స్ఫూర్తి నుండి వచ్చింది."),
]



import json as _json


def _seed_polity_ch9_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "9.1 DPSP పరిచయం — Art 36-37", "sub": "DPSP Basics · Part IV · Art 36 · Art 37 · Non-Justiciable", "audio": ""},
    {"title": "9.2 సోషలిస్ట్ DPSP లు", "sub": "Socialistic DPSPs · Art 38-39 · Equal Pay · Maternity", "audio": ""},
    {"title": "9.3 గాంధేయ DPSP లు", "sub": "Gandhian DPSPs · Art 40-48 · Panchayats · Cottage Industries", "audio": ""},
    {"title": "9.4 ఉదారవాద DPSP లు", "sub": "Liberal-Intellectual DPSPs · Art 44-51 · UCC · International Peace", "audio": ""},
    {"title": "9.5 FR vs DPSP వివాదం మరియు కేసులు", "sub": "FR-DPSP Conflict · Golaknath · Kesavananda · Minerva Mills", "audio": ""},
    {"title": "9.6 రక్షిత నిబంధనలు — Art 31A-31C", "sub": "Art 31A · Art 31B · Art 31C · 9th Schedule · Saving Clauses", "audio": ""},
    {"title": "9.7 FR vs DPSP పోలిక", "sub": "Comparison · Justiciable vs Non-Justiciable · Granville Austin", "audio": ""},
    {"title": "9.8 కఠిన ప్రశ్నలు", "sub": "Difficult MCQs · APPSC Style · Art 38(2) · Instruments of Instructions", "audio": ""}
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
        (9, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch9 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (9, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 9,
         'రాజ్య నిర్దేశక సూత్రాలు',
         'Directive Principles of State Policy',
         'Ch.9',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch9 notes seeded!'}


def _seed_polity_ch9_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (9, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch9_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (9, 'Indian_Polity'))
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
    for mcq in POLITY_CH9_MCQS:
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

    total = len(POLITY_CH9_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch9 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
