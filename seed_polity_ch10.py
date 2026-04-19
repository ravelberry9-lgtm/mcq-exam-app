# seed_polity_ch10.py
# Chapter 10: Fundamental Duties (ప్రాథమిక విధులు — Prathamika Vidhulu)
# Total MCQs: 48 | PYQs: 7 | Format: Bilingual (Telugu + English)
# Sections:
#   0 = పరిచయం / Introduction (7 MCQs)
#   1 = 11 విధుల జాబితా / List of 11 Duties (11 MCQs)
#   2 = స్వభావం & లక్షణాలు / Nature & Features (6 MCQs)
#   3 = స్వర్ణ సింగ్ కమిటీ / Swaran Singh Committee (4 MCQs)
#   4 = 86వ సవరణ - 11వ విధి / 86th Amendment - 11th Duty (4 MCQs)
#   5 = పోలిక / FR vs FD vs DPSP Comparison (5 MCQs)
#   6 = ముఖ్య కేసులు & PYQs / Cases & PYQs (5 MCQs)
#   7 = కఠిన ప్రశ్నలు / Tough MCQs (4 MCQs)

import json as _json

POLITY_CH10_MCQS = [

    # ══════════════ SECTION 0: INTRODUCTION (7 MCQs) ══════════════

    (0, "easy",
     "ప్రాథమిక విధులు రాజ్యాంగంలో ఏ భాగంలో ఉన్నాయి?\n(Fundamental Duties are contained in which Part of the Constitution?)",
     "భాగం III / Part III",
     "భాగం IV / Part IV",
     "భాగం IVA / Part IVA",
     "భాగం V / Part V",
     "C",
     "ప్రాథమిక విధులు భాగం IVA (ఆర్టికల్ 51A) లో ఉన్నాయి. 42వ సవరణ 1976 ద్వారా జోడించిన కొత్త భాగం ఇది.\nFundamental Duties are in Part IVA (Article 51A), a new Part added by the 42nd Amendment 1976."),

    (0, "easy",
     "ప్రాథమిక విధులు ఏ ఆర్టికల్‌లో పేర్కొనబడ్డాయి?\n(In which Article are Fundamental Duties enumerated?)",
     "ఆర్టికల్ 49 / Article 49",
     "ఆర్టికల్ 50 / Article 50",
     "ఆర్టికల్ 51 / Article 51",
     "ఆర్టికల్ 51A / Article 51A",
     "D",
     "ప్రాథమిక విధులు ఆర్టికల్ 51A లో ఉన్నాయి. ఆర్టికల్ 51 అంతర్జాతీయ శాంతి మరియు భద్రతను ప్రోత్సహించడం గురించిన DPSP.\nFundamental Duties are in Article 51A. Article 51 is a DPSP on promoting international peace and security."),

    (0, "easy",
     "ప్రాథమిక విధులు ఏ రాజ్యాంగ సవరణ ద్వారా జోడించబడ్డాయి?\n(Fundamental Duties were added by which Constitutional Amendment?)",
     "40వ సవరణ చట్టం, 1976 / 40th Amendment Act, 1976",
     "42వ సవరణ చట్టం, 1976 / 42nd Amendment Act, 1976",
     "44వ సవరణ చట్టం, 1978 / 44th Amendment Act, 1978",
     "86వ సవరణ చట్టం, 2002 / 86th Amendment Act, 2002",
     "B",
     "ప్రాథమిక విధులు 42వ రాజ్యాంగ సవరణ చట్టం 1976 ద్వారా జోడించబడ్డాయి. ఇది స్వర్ణ సింగ్ కమిటీ సిఫారసు మేరకు జరిగింది.\nFundamental Duties were added by the 42nd Constitutional Amendment Act, 1976, based on recommendations of the Swaran Singh Committee.",
     "APPSC"),

    (0, "medium",
     "ప్రాథమిక విధులు ఏ దేశ రాజ్యాంగం నుండి స్వీకరించబడ్డాయి?\n(Fundamental Duties were borrowed from the constitution of which country?)",
     "USA",
     "ఐర్లాండ్ / Ireland",
     "USSR (సోవియట్ యూనియన్) / USSR (Soviet Union)",
     "జపాన్ / Japan",
     "C",
     "ప్రాథమిక విధులు USSR (సోవియట్ యూనియన్) రాజ్యాంగం నుండి స్వీకరించబడ్డాయి.\nFundamental Duties were borrowed from the Constitution of the USSR (Soviet Union).",
     "APPSC"),

    (0, "medium",
     "మూలభూత విధులను సిఫారసు చేసిన కమిటీ ఏది?\n(Which committee recommended Fundamental Duties?)",
     "బలవంత్రాయ్ మెహతా కమిటీ / Balwantrai Mehta Committee",
     "స్వర్ణ సింగ్ కమిటీ / Swaran Singh Committee",
     "అశోక్ మెహతా కమిటీ / Ashok Mehta Committee",
     "వర్మా కమిటీ / Verma Committee",
     "B",
     "స్వర్ణ సింగ్ కమిటీ (1976) మూలభూత విధులను సిఫారసు చేసింది. ఇందిరా గాంధీ ప్రభుత్వం ఈ కమిటీని ఏర్పాటు చేసింది.\nSwaran Singh Committee (1976) recommended Fundamental Duties. It was set up by the Indira Gandhi government.",
     "APPSC"),

    (0, "medium",
     "42వ సవరణ 1976 మూలభూత విధులను జోడించడానికి ముందు రాజ్యాంగంలో ఎన్ని ప్రాథమిక విధులు ఉండేవి?\n(Before the 42nd Amendment 1976 added Fundamental Duties, how many were in the Constitution?)",
     "5 / 5",
     "8 / 8",
     "10 / 10",
     "0 / 0 (అసలు లేవు / None at all)",
     "D",
     "42వ సవరణ 1976 కు ముందు రాజ్యాంగంలో ప్రాథమిక విధులు అసలు లేవు. ఇవి 1976లో కొత్తగా జోడించబడ్డాయి.\nBefore the 42nd Amendment 1976, there were no Fundamental Duties in the Constitution at all. They were newly added in 1976."),

    (0, "medium",
     "ప్రాథమిక విధులు రాజ్యాంగంలో DPSPs తర్వాత ఎందుకు ఉంచబడ్డాయి?\n(Why are Fundamental Duties placed after DPSPs in the Constitution?)",
     "అవి DPSPs అనుబంధ నిబంధనలు / They are supplementary to DPSPs",
     "అవి DPSPs కంటే తక్కువ ముఖ్యమైనవి / They are less important than DPSPs",
     "పౌరుల విధులు రాజ్యం విధులు (DPSPs) తర్వాత వస్తాయి — సమతుల్య రాజ్యాంగ ప్రతిబింబం / Citizens' duties follow State's duties (DPSPs) — balanced constitutional scheme",
     "అవి DPSPs లాగా న్యాయ-అమలు యోగ్యం కావు కాబట్టి / Because they are non-justiciable like DPSPs",
     "C",
     "DPSPs రాజ్యానికి నిర్దేశాలు, FDs పౌరులకు నిర్దేశాలు. రాజ్యం విధులు తర్వాత పౌరుల విధులు ఉంచడం సమతుల్య రాజ్యాంగ పథకాన్ని ప్రతిబింబిస్తుంది.\nDPSPs are directives to the State, FDs are duties for citizens. Placing citizens' duties after State's duties reflects a balanced constitutional scheme."),

    # ══════════════ SECTION 1: LIST OF 11 DUTIES (11 MCQs) ══════════════

    (1, "easy",
     "జాతీయ గీతాన్ని పాటించి గౌరవించడం ఏ మూలభూత విధి కిందకు వస్తుంది?\n(Abiding by the Constitution, respecting National Flag and National Anthem falls under which Fundamental Duty?)",
     "ఆర్టికల్ 51A(a) / Article 51A(a)",
     "ఆర్టికల్ 51A(b) / Article 51A(b)",
     "ఆర్టికల్ 51A(c) / Article 51A(c)",
     "ఆర్టికల్ 51A(d) / Article 51A(d)",
     "A",
     "Art 51A(a): రాజ్యాంగాన్ని పాటించడం, దాని ఆదర్శాలు & వ్యవస్థలను గౌరవించడం, జాతీయ పతాకం & జాతీయ గీతాన్ని గౌరవించడం.\nArt 51A(a): Abide by the Constitution, respect its ideals & institutions, National Flag & National Anthem."),

    (1, "easy",
     "స్వాతంత్ర్య ఉద్యమాన్ని ఉత్తేజపరిచిన ఉదాత్త ఆదర్శాలను మనసారా పాటించడం — ఇది ఏ ఆర్టికల్ 51A(?)\n(Cherish and follow the noble ideals which inspired the freedom struggle — which Art 51A(?))",
     "Art 51A(a)",
     "Art 51A(b)",
     "Art 51A(c)",
     "Art 51A(d)",
     "B",
     "Art 51A(b): స్వాతంత్ర్య ఉద్యమానికి స్ఫూర్తినిచ్చిన ఉదాత్త ఆదర్శాలను మనసారా పాటించడం ప్రతి పౌరుని విధి.\nArt 51A(b): It is the duty of every citizen to cherish and follow the noble ideals which inspired the national struggle for freedom."),

    (1, "medium",
     "భారతదేశ సార్వభౌమత్వం, ఐక్యత మరియు సమగ్రతను నిలబెట్టడం మరియు రక్షించడం — ఏ ఆర్టికల్ 51A(?)?\n(Uphold and protect the sovereignty, unity and integrity of India — which Art 51A(?))",
     "Art 51A(b)",
     "Art 51A(c)",
     "Art 51A(d)",
     "Art 51A(e)",
     "B",
     "Art 51A(c): సార్వభౌమత్వం, ఐక్యత మరియు సమగ్రత. ఇది రాష్ట్ర విభజన లేదా రాజద్రోహ కార్యకలాపాలకు వ్యతిరేకం.\nArt 51A(c): Sovereignty, unity and integrity. This is directed against secessionist or anti-national activities."),

    (1, "medium",
     "దేశాన్ని రక్షించడం మరియు పిలిచినప్పుడు జాతీయ సేవ చేయడం — ఏ ఆర్టికల్ 51A(?)?\n(Defend the country and render national service when called upon — which Art 51A(?))",
     "Art 51A(c)",
     "Art 51A(d)",
     "Art 51A(e)",
     "Art 51A(f)",
     "B",
     "Art 51A(d): దేశ రక్షణ మరియు జాతీయ సేవ. ఇది National Service Act మరియు సైనిక సేవకు పౌర విధిని ప్రతిబింబిస్తుంది.\nArt 51A(d): Defence of the country and national service. This reflects the civic duty of military service and National Service Act."),

    (1, "medium",
     "సహోదర భావనను పెంపొందించడం మరియు మహిళలకు అవమానకరమైన ఆచారాలను త్యజించడం — ఏ ఆర్టికల్ 51A(?)?\n(Promote harmony and spirit of common brotherhood; renounce practices derogatory to the dignity of women — which Art 51A(?))",
     "Art 51A(d)",
     "Art 51A(e)",
     "Art 51A(f)",
     "Art 51A(g)",
     "B",
     "Art 51A(e): మత, భాషా, ప్రాంతీయ వైవిధ్యాలను అధిగమించి సహోదర భావన పెంపొందించడం; మహిళలను అవమానించే ఆచారాలు విరమించడం.\nArt 51A(e): Promote harmony transcending religious, linguistic, regional diversities; renounce practices derogatory to the dignity of women."),

    (1, "medium",
     "భారతదేశ సమ్మిళిత సంస్కృతి యొక్క గొప్ప వారసత్వాన్ని విలువకట్టడం మరియు పరిరక్షించడం — ఏ ఆర్టికల్ 51A(?)?\n(Value and preserve the rich heritage of our composite culture — which Art 51A(?))",
     "Art 51A(e)",
     "Art 51A(f)",
     "Art 51A(g)",
     "Art 51A(h)",
     "B",
     "Art 51A(f): భారత సమ్మిళిత సంస్కృతి వారసత్వాన్ని విలువకట్టడం — ఇందులో కళ, సాహిత్యం, భాష, పురావస్తు, స్మారకాలు చేర్చబడతాయి.\nArt 51A(f): Value and preserve composite cultural heritage — includes art, literature, language, archaeological sites, monuments."),

    (1, "medium",
     "సహజ పర్యావరణాన్ని రక్షించడం మరియు మెరుగుపరచడం (అడవులు, సరస్సులు, నదులు, వన్యప్రాణులు) — ఏ ఆర్టికల్ 51A(?)?\n(Protect and improve the natural environment including forests, lakes, rivers and wildlife — which Art 51A(?))",
     "Art 51A(f)",
     "Art 51A(g)",
     "Art 51A(h)",
     "Art 51A(i)",
     "B",
     "Art 51A(g): సహజ పర్యావరణ పరిరక్షణ. అడవులు, సరస్సులు, నదులు, వన్యప్రాణులతో సహా; జీవులపట్ల కరుణ చూపడం.\nArt 51A(g): Protect and improve natural environment including forests, lakes, rivers, wildlife and have compassion for living creatures."),

    (1, "medium",
     "శాస్త్రీయ దృక్పథం, మానవతావాదం మరియు జ్ఞాన విచారణ స్ఫూర్తిని పెంపొందించడం — ఏ ఆర్టికల్ 51A(?)?\n(Develop scientific temper, humanism and the spirit of inquiry and reform — which Art 51A(?))",
     "Art 51A(g)",
     "Art 51A(h)",
     "Art 51A(i)",
     "Art 51A(j)",
     "B",
     "Art 51A(h): శాస్త్రీయ దృక్పథం, మానవతావాదం మరియు విచారణ & సంస్కరణ స్ఫూర్తి. ఇది అంధ విశ్వాసాలకు వ్యతిరేకం.\nArt 51A(h): Develop scientific temper, humanism and spirit of inquiry and reform — directed against blind superstition and fatalism."),

    (1, "easy",
     "సార్వజనిక ఆస్తిని సంరక్షించడం మరియు హింసను విరమించడం — ఏ ఆర్టికల్ 51A(?)?\n(Safeguard public property and abjure violence — which Art 51A(?))",
     "Art 51A(g)",
     "Art 51A(h)",
     "Art 51A(i)",
     "Art 51A(j)",
     "C",
     "Art 51A(i): సార్వజనిక ఆస్తి సంరక్షణ మరియు హింస విరమింపు. ఇది నిరసన సమయంలో ప్రభుత్వ ఆస్తికి నష్టం చేయడాన్ని నిషేధిస్తుంది.\nArt 51A(i): Safeguard public property and abjure violence — prohibits damaging government property during protests."),

    (1, "medium",
     "వ్యక్తిగత మరియు సామూహిక కార్యకలాపాలన్నింటిలో శ్రేష్ఠతకు కృషి చేయడం — ఏ ఆర్టికల్ 51A(?)?\n(Strive towards excellence in all spheres of individual and collective activity — which Art 51A(?))",
     "Art 51A(h)",
     "Art 51A(i)",
     "Art 51A(j)",
     "Art 51A(k)",
     "C",
     "Art 51A(j): వ్యక్తిగత మరియు సామూహిక కార్యకలాపాలలో శ్రేష్ఠత — దేశం నిరంతర ఎదుగుదలకు పౌరులు కృషి చేయాలి.\nArt 51A(j): Strive towards excellence so that the nation constantly rises to higher levels of endeavour and achievement."),

    (1, "easy",
     "6-14 సంవత్సరాల వయస్సు గల పిల్లలకు విద్యా అవకాశాలు కల్పించడం — ఇది ఏ ఆర్టికల్ 51A(?)\n(Provide opportunities for education to children between the age of 6-14 years — which Art 51A(?))",
     "Art 51A(i)",
     "Art 51A(j)",
     "Art 51A(k)",
     "Art 51A(l)",
     "C",
     "Art 51A(k): 6-14 సంవత్సరాల పిల్లలకు విద్యా అవకాశాలు కల్పించడం తల్లిదండ్రులు లేదా సంరక్షకుని విధి. 86వ సవరణ 2002 ద్వారా జోడించబడింది.\nArt 51A(k): It is the duty of every parent or guardian to provide educational opportunities for the child (6-14 years). Added by 86th Amendment 2002."),

    # ══════════════ SECTION 2: NATURE & FEATURES (6 MCQs) ══════════════

    (2, "medium",
     "ప్రాథమిక విధులు న్యాయస్థానం ద్వారా అమలు చేయగలిగేవా?\n(Are Fundamental Duties enforceable through courts?)",
     "అవును, మూలభూత హక్కుల మాదిరిగా / Yes, like Fundamental Rights",
     "అవును, కానీ కేవలం సుప్రీం కోర్టు ద్వారా / Yes, but only through Supreme Court",
     "కాదు, అవి న్యాయ-అమలు యోగ్యం కాదు (Non-justiciable) / No, they are non-justiciable",
     "అవును, DPSP లాగా / Yes, like DPSPs",
     "C",
     "ప్రాథమిక విధులు న్యాయ-అమలు యోగ్యం కాదు — వాటిని ఉల్లంఘించినందుకు నేరుగా న్యాయస్థానంలో అమలు చేయలేరు. అయితే పార్లమెంటు వాటిని అమలు చేయడానికి చట్టాలు చేయవచ్చు.\nFundamental Duties are non-justiciable — they cannot be directly enforced in courts. However, Parliament can make laws to enforce them."),

    (2, "easy",
     "ప్రాథమిక విధులు ఎవరికి వర్తిస్తాయి?\n(Fundamental Duties apply to whom?)",
     "కేవలం ప్రభుత్వ ఉద్యోగులకు / Only Government employees",
     "కేవలం పౌరులకు / Only Citizens of India",
     "పౌరులు మరియు విదేశీయులకు / Citizens and foreigners",
     "భారత్‌లో నివసించే అందరికీ / All residents of India",
     "B",
     "ప్రాథమిక విధులు కేవలం భారత పౌరులకే వర్తిస్తాయి, విదేశీయులకు కావు. ఇది మూలభూత హక్కులతో వ్యత్యాసం — కొన్ని మూలభూత హక్కులు విదేశీయులకు కూడా వర్తిస్తాయి.\nFundamental Duties apply only to Indian citizens, not foreigners. This differs from FRs where some apply to non-citizens too."),

    (2, "medium",
     "ప్రాథమిక విధులు ఉల్లంఘించినప్పుడు ఏమి జరుగుతుంది?\n(What happens when Fundamental Duties are violated?)",
     "మూలభూత హక్కుల మాదిరిగా న్యాయస్థానంలో అమలు చేయవచ్చు / Directly enforceable in courts like FRs",
     "పార్లమెంటు చట్టం ద్వారా శిక్ష విధించవచ్చు / Parliament can prescribe punishment through law",
     "స్వయంచాలకంగా పౌరసత్వం కోల్పోతారు / Citizenship is lost automatically",
     "కేవలం నైతిక అపఖ్యాతి మాత్రమే / Only moral stigma — no legal consequence",
     "B",
     "ప్రాథమిక విధులు న్యాయ-అమలు యోగ్యం కాదు అయినా, పార్లమెంటు వాటి ఉల్లంఘనకు చట్టం ద్వారా శిక్షలు నిర్ణయించవచ్చు. వర్మా కమిటీ 2002 ఇప్పటికే చాలా చట్టాలు ఉన్నాయని పేర్కొంది.\nThough non-justiciable, Parliament can prescribe penalties through law for violation. Verma Committee (2002) noted many existing laws already implement FDs."),

    (2, "hard",
     "మూలభూత విధుల గురించి కింది ఏ వ్యాఖ్య సరైనది?\n(Which statement about Fundamental Duties is correct?)",
     "అవి న్యాయస్థానం ద్వారా అమలు చేయగలిగేవి / They are directly enforceable in courts",
     "విదేశీయులకు కూడా వర్తిస్తాయి / They also apply to foreigners",
     "చట్టాల రాజ్యాంగ చెల్లుబాటు నిర్ణయించడానికి న్యాయస్థానాలు వాటిని ఉపయోగించవచ్చు / Courts can use them to determine constitutionality of laws",
     "అవి రాజ్యానికి కూడా వర్తిస్తాయి / They also apply to the State",
     "C",
     "AIIMS విద్యార్థుల సంఘం v. AIIMS (2001) కేసులో SC నిర్ణయించింది: ప్రాథమిక విధులు చట్టాల రాజ్యాంగ చెల్లుబాటు నిర్ణయించడానికి ఉపయోగపడతాయి.\nIn AIIMS Students Union v. AIIMS (2001), SC held: FDs can be used to determine the constitutional validity of laws."),

    (2, "easy",
     "రాజ్యాంగంలో ప్రాథమిక విధులు ఎక్కడ ఉన్నాయి?\n(Where in the Constitution are Fundamental Duties placed?)",
     "మూలభూత హక్కులు (భాగం III) తర్వాత / After Fundamental Rights (Part III)",
     "DPSPs (భాగం IV) తర్వాత — కొత్త భాగం IVA లో / After DPSPs (Part IV) — in new Part IVA",
     "పీఠికకు ముందు / Before the Preamble",
     "భాగం V లో / In Part V",
     "B",
     "ప్రాథమిక విధులు DPSPs (భాగం IV) తర్వాత కొత్తగా సృష్టించిన భాగం IVA లో ఆర్టికల్ 51A లో ఉన్నాయి.\nFundamental Duties are in Part IVA (newly created by 42nd Amendment) as Article 51A, placed after DPSPs (Part IV)."),

    (2, "medium",
     "ఆర్టికల్ 51A ప్రస్తుతం ఎన్ని విభాగాలు (clauses) కలిగి ఉంది?\n(How many clauses does Article 51A currently have?)",
     "9 విభాగాలు / 9 clauses",
     "10 విభాగాలు / 10 clauses",
     "11 విభాగాలు (a నుండి k వరకు) / 11 clauses (a to k)",
     "12 విభాగాలు / 12 clauses",
     "C",
     "ఆర్టికల్ 51A ప్రస్తుతం 11 విభాగాలు (a నుండి k వరకు) కలిగి ఉంది. a-j విభాగాలు 42వ సవరణ 1976 ద్వారా, k విభాగం 86వ సవరణ 2002 ద్వారా జోడించబడ్డాయి.\nArt 51A currently has 11 clauses (a to k). Clauses a-j were added by 42nd Amendment 1976; clause k was added by 86th Amendment 2002."),

    # ══════════════ SECTION 3: SWARAN SINGH COMMITTEE (4 MCQs) ══════════════

    (3, "medium",
     "స్వర్ణ సింగ్ కమిటీని ఎవరు ఏర్పాటు చేశారు?\n(Who set up the Swaran Singh Committee?)",
     "రాష్ట్రపతి ఫక్రుద్దీన్ అలీ అహ్మద్ / President Fakhruddin Ali Ahmed",
     "ఇందిరా గాంధీ నేతృత్వంలో కాంగ్రెస్ ప్రభుత్వం / Congress government under Indira Gandhi",
     "జయప్రకాశ్ నారాయణ్ / Jayaprakash Narayan",
     "మొరార్జీ దేశాయి ప్రభుత్వం / Morarji Desai government",
     "B",
     "స్వర్ణ సింగ్ కమిటీని 1976 లో ఇందిరా గాంధీ నేతృత్వంలో కాంగ్రెస్ ప్రభుత్వం ఏర్పాటు చేసింది. స్వర్ణ సింగ్ ఆనాటి కేంద్ర మంత్రి.\nSwaran Singh Committee was set up in 1976 by the Congress government under Indira Gandhi. Swaran Singh was a senior Cabinet Minister."),

    (3, "hard",
     "స్వర్ణ సింగ్ కమిటీ ఎన్ని మూలభూత విధులను సిఫారసు చేసింది?\n(How many Fundamental Duties did the Swaran Singh Committee recommend?)",
     "6 / 6",
     "8 / 8",
     "10 / 10",
     "11 / 11",
     "B",
     "స్వర్ణ సింగ్ కమిటీ 8 విధులను సిఫారసు చేసింది. అయితే పార్లమెంటు 2 అదనపు విధులు జోడించి మొత్తం 10 విధులు (42వ సవరణ 1976లో) ఆమోదించింది.\nSwaran Singh Committee recommended 8 duties. However, Parliament added 2 more, making it 10 duties in total (through 42nd Amendment 1976)."),

    (3, "medium",
     "స్వర్ణ సింగ్ కమిటీ మూలభూత విధుల ఉల్లంఘన గురించి ఏమి సిఫారసు చేసింది?\n(What did the Swaran Singh Committee recommend about violation of Fundamental Duties?)",
     "విధులను న్యాయ-అమలు యోగ్యం చేయడం / Make duties justiciable in courts",
     "ఉల్లంఘించినందుకు పార్లమెంటు శిక్షలు నిర్ణయించాలి / Parliament should prescribe penalties for breach",
     "విధుల ఉల్లంఘనకు పౌరసత్వం రద్దు / Revocation of citizenship for breach",
     "DPSPs మాదిరిగా మార్గదర్శకాలుగా వదిలివేయడం / Leave them as directives like DPSPs",
     "B",
     "స్వర్ణ సింగ్ కమిటీ విధులు ఉల్లంఘించినందుకు పార్లమెంటు శిక్షలు నిర్ణయించాలని సిఫారసు చేసింది. ఇది వాటిని పరోక్షంగా అమలు చేయగలిగేలా చేస్తుంది.\nSwaran Singh Committee recommended that Parliament should prescribe penalties for breach of duties, making them indirectly enforceable."),

    (3, "hard",
     "స్వర్ణ సింగ్ కమిటీ మూలభూత విధులను రాజ్యాంగంలో ఎక్కడ ఉంచమని సిఫారసు చేసింది?\n(Where did the Swaran Singh Committee recommend placing Fundamental Duties in the Constitution?)",
     "భాగం III (మూలభూత హక్కులు)లో / In Part III (Fundamental Rights)",
     "ప్రత్యేక షెడ్యూల్‌లో / In a separate Schedule",
     "DPSPs (భాగం IV) తర్వాత ఒక కొత్త భాగంగా / As a new Part after DPSPs (Part IV)",
     "పీఠికలో (Preamble) / In the Preamble",
     "C",
     "స్వర్ణ సింగ్ కమిటీ DPSPs (భాగం IV) తర్వాత ఒక కొత్త భాగంగా చేర్చమని సిఫారసు చేసింది. 42వ సవరణ ఆ సిఫారసు మేరకు కొత్త భాగం IVA సృష్టించింది.\nSwaran Singh Committee recommended a new Part after DPSPs (Part IV). The 42nd Amendment created new Part IVA accordingly."),

    # ══════════════ SECTION 4: 86th AMENDMENT - 11th DUTY (4 MCQs) ══════════════

    (4, "easy",
     "86వ రాజ్యాంగ సవరణ చట్టం ఏ సంవత్సరంలో ఆమోదించబడింది?\n(In which year was the 86th Constitutional Amendment Act passed?)",
     "2000 / 2000",
     "2001 / 2001",
     "2002 / 2002",
     "2004 / 2004",
     "C",
     "86వ రాజ్యాంగ సవరణ చట్టం 2002లో ఆమోదించబడింది. ఇది ఆర్టికల్ 21A (6-14 విద్యా హక్కు) మరియు ఆర్టికల్ 51A(k) (11వ మూలభూత విధి) జోడించింది.\n86th Constitutional Amendment Act was passed in 2002. It added Art 21A (Right to Education 6-14) and Art 51A(k) (11th Fundamental Duty).",
     "APPSC"),

    (4, "medium",
     "86వ సవరణ 2002 ద్వారా జోడించబడిన 11వ మూలభూత విధి ఏమిటి?\n(What is the 11th Fundamental Duty added by the 86th Amendment 2002?)",
     "పర్యావరణ పరిరక్షణ / Protect natural environment",
     "6-14 సంవత్సరాల మధ్య పిల్లలకు విద్యా అవకాశాలు కల్పించడం తల్లిదండ్రులు/సంరక్షకుల విధి / It shall be the duty of every parent or guardian to provide educational opportunities for the child (6-14 yrs)",
     "జాతీయ ఐక్యత కాపాడడం / Uphold national unity",
     "శాస్త్రీయ దృక్పథం పెంపొందించడం / Develop scientific temper",
     "B",
     "11వ విధి [Art 51A(k)]: 6-14 సంవత్సరాల మధ్య పిల్లలకు విద్యా అవకాశాలు కల్పించడం ప్రతి తల్లిదండ్రి లేదా సంరక్షకుని విధి. ఇది Art 21A విద్యా హక్కుకు అనుసంధానమై ఉంది.\n11th Duty [Art 51A(k)]: Every parent/guardian has duty to provide educational opportunities for child (6-14). This is linked to Art 21A Right to Education.",
     "APPSC"),

    (4, "medium",
     "86వ సవరణ 2002 ఏ ఆర్టికల్‌ను మరియు ఏ మూలభూత విధిని జోడించింది?\n(The 86th Amendment 2002 added which Article AND which Fundamental Duty?)",
     "Art 21 మరియు Art 51A(j) / Art 21 and Art 51A(j)",
     "Art 21A మరియు Art 51A(k) / Art 21A and Art 51A(k)",
     "Art 21A మాత్రమే / Art 21A only",
     "Art 51A(k) మాత్రమే / Art 51A(k) only",
     "B",
     "86వ సవరణ 2002 రెండింటినీ జోడించింది: (1) Art 21A — 6-14 సంవత్సరాల పిల్లలకు ఉచిత మరియు నిర్బంధ విద్య; (2) Art 51A(k) — తల్లిదండ్రుల మూలభూత విధి.\n86th Amendment 2002 added both: (1) Art 21A — free and compulsory education 6-14 years; (2) Art 51A(k) — fundamental duty of parents."),

    (4, "hard",
     "ఆర్టికల్ 51A(k) ప్రకారం, 6-14 సంవత్సరాల పిల్లలకు విద్యా అవకాశాలు కల్పించడం ఎవరి విధి?\n(According to Art 51A(k), it is whose duty to provide educational opportunities for children 6-14?)",
     "కేవలం తల్లి విధి / Duty of mother only",
     "కేవలం తండ్రి విధి / Duty of father only",
     "తల్లిదండ్రి లేదా సంరక్షకుని విధి / Duty of every parent or guardian",
     "రాజ్యం (ప్రభుత్వం) విధి / Duty of the State (Government)",
     "C",
     "Art 51A(k): ప్రతి తల్లిదండ్రి లేదా సంరక్షకుడు 6-14 సంవత్సరాల పిల్లలకు విద్యా అవకాశాలు కల్పించడానికి బాధ్యులు. (Art 21A కింద రాజ్యం బాధ్యత వేరే).\nArt 51A(k): Every parent or guardian has the duty to provide educational opportunities for children between 6-14 years. (The State's duty is separately under Art 21A)."),

    # ══════════════ SECTION 5: FR vs FD vs DPSP COMPARISON (5 MCQs) ══════════════

    (5, "medium",
     "మూలభూత హక్కులు (FRs) మరియు ప్రాథమిక విధులు (FDs) మధ్య ముఖ్య తేడా ఏమిటి?\n(What is the key difference between Fundamental Rights (FRs) and Fundamental Duties (FDs)?)",
     "FRs కేవలం పౌరులకు, FDs అందరికీ / FRs only to citizens, FDs to all",
     "FRs న్యాయ-అమలు యోగ్యం, FDs న్యాయ-అమలు యోగ్యం కాదు / FRs justiciable, FDs non-justiciable",
     "FRs DPSPsలో ఉన్నాయి, FDs భాగం III లో / FRs in DPSPs, FDs in Part III",
     "FRs సవరించలేమ, FDs సవరించవచ్చు / FRs unamendable, FDs amendable",
     "B",
     "FRs న్యాయ-అమలు యోగ్యం (Art 32/226 ద్వారా కోర్టు అమలు చేస్తుంది), FDs న్యాయ-అమలు యోగ్యం కాదు (అయినా పార్లమెంటు చట్టం ద్వారా అమలు చేయవచ్చు).\nFRs are justiciable (enforced by courts via Art 32/226), FDs are non-justiciable (though Parliament can enforce them through law)."),

    (5, "medium",
     "FDs మరియు DPSPs మధ్య సారూప్యత ఏమిటి?\n(What is the key similarity between Fundamental Duties (FDs) and DPSPs?)",
     "రెండూ పౌరులకు మాత్రమే వర్తిస్తాయి / Both apply only to citizens",
     "రెండూ న్యాయ-అమలు యోగ్యం కాదు / Both are non-justiciable",
     "రెండూ 42వ సవరణ ద్వారా జోడించబడ్డాయి / Both added by 42nd Amendment",
     "రెండూ జాతి ఆదేశ సూత్రాలు / Both are national directive principles",
     "B",
     "FDs మరియు DPSPs రెండూ న్యాయ-అమలు యోగ్యం కాదు. తేడా: DPSPs రాజ్యానికి నిర్దేశాలు; FDs పౌరులకు నిర్దేశాలు.\nBoth FDs and DPSPs are non-justiciable. Difference: DPSPs are directives to the State; FDs are duties for citizens."),

    (5, "hard",
     "కింది జోడి సరైనది: మూలభూత విధుల మూలం?\n(Which pair is correct: Source of Fundamental Duties?)",
     "FDs → USA Bill of Rights",
     "FDs → USSR రాజ్యాంగం / USSR Constitution",
     "FDs → ఐర్లాండ్ రాజ్యాంగం / Irish Constitution",
     "FDs → జపాన్ రాజ్యాంగం / Japanese Constitution",
     "B",
     "ప్రాథమిక విధులు USSR (సోవియట్ యూనియన్) రాజ్యాంగం నుండి స్వీకరించబడ్డాయి. (పోల్చడానికి: DPSPs → ఐర్లాండ్; FRs → USA; Parliamentary వ్యవస్థ → UK)\nFundamental Duties are borrowed from USSR Constitution. (Compare: DPSPs → Ireland; FRs → USA; Parliamentary system → UK)",
     "APPSC"),

    (5, "medium",
     "మూలభూత హక్కులు (FRs) మరియు ప్రాథమిక విధులు (FDs) మధ్య ఉమ్మడి లక్షణం ఏది?\n(What common feature do Fundamental Rights and Fundamental Duties share?)",
     "రెండూ ప్రభుత్వానికి నిర్దేశాలు / Both are directives for government",
     "రెండూ పూర్తిగా పౌరులకు మాత్రమే వర్తిస్తాయి / Both apply exclusively only to citizens",
     "రెండూ న్యాయ-అమలు యోగ్యం / Both are justiciable",
     "రెండూ పార్లమెంటు ద్వారా సవరించవచ్చు / Both can be amended by Parliament",
     "D",
     "FRs మరియు FDs రెండూ పార్లమెంటు ద్వారా సవరించవచ్చు. అయితే FRs పౌరులు + కొన్ని అన్యులకు వర్తిస్తాయి; FDs కేవలం పౌరులకు వర్తిస్తాయి.\nBoth FRs and FDs can be amended by Parliament. However FRs apply to citizens + some aliens; FDs apply only to citizens."),

    (5, "hard",
     "కింది ఏ అంశం మూలభూత విధుల గురించి సరైనది కాదు?\n(Which of the following is NOT true about Fundamental Duties?)",
     "పార్లమెంటు చట్టం ద్వారా వాటిని అమలు చేయవచ్చు / They can be enforced through Parliament's law",
     "అవి కేవలం పౌరులకే వర్తిస్తాయి / They apply only to citizens",
     "అవి న్యాయస్థానం ద్వారా నేరుగా అమలు చేయగలిగేవి / They are directly enforceable through courts",
     "అవి 42వ సవరణ 1976 ద్వారా జోడించబడ్డాయి / They were added by 42nd Amendment 1976",
     "C",
     "ప్రాథమిక విధులు న్యాయస్థానం ద్వారా నేరుగా అమలు చేయగలిగేవి కావు (non-justiciable). మిగతా అన్ని వ్యాఖ్యలు సరైనవే.\nFundamental Duties are NOT directly enforceable through courts (non-justiciable). All other statements are correct."),

    # ══════════════ SECTION 6: CASES & PYQs (5 MCQs) ══════════════

    (6, "hard",
     "బిజో ఎమ్మాన్యూయేల్ v. కేరళ రాష్ట్రం (1986) కేసు దేనికి సంబంధించినది?\n(Bijoe Emmanuel v. State of Kerala (1986) case relates to which Fundamental Duty?)",
     "శిశు శ్రమ నిషేధానికి / Child labour prohibition",
     "జాతీయ గీతం పాడటానికి నిరాకరించినందుకు — Art 51A(a) విధి vs Art 25 హక్కు / Refusal to sing National Anthem — Art 51A(a) duty vs Art 25 right",
     "మత మార్పిడి నిషేధానికి / Prohibition of religious conversion",
     "పర్యావరణ పరిరక్షణకు / Environmental protection",
     "B",
     "బిజో ఎమ్మాన్యూయేల్ కేసు: జెహోవా సాక్షుల విద్యార్థులు జాతీయ గీతం పాడటానికి నిరాకరించారు. SC Art 25 (మత స్వాతంత్ర్యం) కింద రక్షణ కల్పించింది — Art 51A(a) విధి ఉన్నప్పటికీ.\nBijoe Emmanuel case: Jehovah's Witness students refused to sing National Anthem. SC protected them under Art 25 (religious freedom) despite Art 51A(a) duty."),

    (6, "hard",
     "వర్మా కమిటీ 2002 (జస్టిస్ J.S. వర్మా) ఏ అంశంపై నిర్మించబడింది?\n(The Verma Committee 2002 (Justice J.S. Verma) was constituted on what subject?)",
     "మూలభూత విధుల అమలు / Operationalisation of Fundamental Duties",
     "రాజ్యాంగ సవరణ ప్రక్రియ / Constitutional amendment procedure",
     "మూలభూత హక్కుల విస్తరణ / Extension of Fundamental Rights",
     "DPSPs అమలు / Implementation of DPSPs",
     "A",
     "జస్టిస్ J.S. వర్మా కమిటీ (2002) మూలభూత విధుల అమలుపై నిర్మించబడింది. ఇప్పటికే ఉన్న చట్టాలు వాటిని అమలు చేస్తున్నాయని నివేదించింది. ఉదా: Protection of Civil Rights Act 1955, Environment Protection Act 1986 మొదలైనవి.\nJustice Verma Committee (2002) on operationalisation of FDs. Reported existing laws already implement them e.g., Protection of Civil Rights Act 1955, Environment Protection Act 1986."),

    (6, "medium",
     "AIIMS విద్యార్థుల సంఘం v. AIIMS (2001) కేసులో సుప్రీం కోర్టు మూలభూత విధుల గురించి ఏమి పేర్కొంది?\n(What did the Supreme Court state about Fundamental Duties in AIIMS Students Union v. AIIMS (2001)?)",
     "FDs న్యాయ-అమలు యోగ్యం / FDs are justiciable",
     "FDs ను రద్దు చేయాలి / FDs should be repealed",
     "FDs చట్టాల రాజ్యాంగ చెల్లుబాటు నిర్ణయించడానికి ఉపయోగపడతాయి / FDs are useful in determining constitutional validity of laws",
     "FDs FRs కంటే శ్రేష్ఠమైనవి / FDs are superior to FRs",
     "C",
     "AIIMS Students Union కేసులో (2001) SC: ప్రాథమిక విధులు చట్టాల రాజ్యాంగ చెల్లుబాటు నిర్ణయించడానికి ఉపయోగపడతాయి. అవి నేరుగా అమలు చేయగలిగేవి కాకపోయినా న్యాయ దృష్టిలో పరిగణించబడతాయి.\nIn AIIMS Students Union (2001): FDs are useful in determining constitutional validity of laws — they are taken into account even though not directly enforceable."),

    (6, "easy",
     "ప్రస్తుతం భారత రాజ్యాంగంలో మొత్తం ప్రాథమిక విధులు ఎన్ని ఉన్నాయి?\n(How many Fundamental Duties are there currently in the Indian Constitution?)",
     "9 / 9",
     "10 / 10",
     "11 / 11",
     "12 / 12",
     "C",
     "ప్రస్తుతం 11 ప్రాథమిక విధులు ఉన్నాయి — 42వ సవరణ 1976 ద్వారా 10 (a-j), 86వ సవరణ 2002 ద్వారా 11వ విధి (k) జోడించబడింది.\nCurrently 11 Fundamental Duties — 10 (a-j) added by 42nd Amendment 1976; 11th (k) added by 86th Amendment 2002.",
     "APPSC"),

    (6, "medium",
     "ఏ చట్టం ఆర్టికల్ 51A(e) — మహిళల గౌరవం మరియు సహోదర భావన విధిని అమలు చేస్తుంది?\n(Which Act operationalises Art 51A(e) — duty of harmony and renouncing practices derogatory to women?)",
     "నాగరిక హక్కుల రక్షణ చట్టం 1955 / Protection of Civil Rights Act 1955",
     "అనైతిక రవాణా నివారణ చట్టం 1956 / Immoral Traffic (Prevention) Act 1956",
     "పర్యావరణ పరిరక్షణ చట్టం 1986 / Environment Protection Act 1986",
     "బంధిత కార్మిక వ్యవస్థ రద్దు చట్టం 1976 / Bonded Labour System (Abolition) Act 1976",
     "A",
     "వర్మా కమిటీ 2002 నివేదిక: నాగరిక హక్కుల రక్షణ చట్టం 1955 — అస్పృశ్యత మరియు సహోదర భావన విధి (Art 51A(e)) ను అమలు చేస్తుంది.\nVerma Committee 2002: Protection of Civil Rights Act 1955 operationalises the duty of harmony and renouncing discriminatory practices (Art 51A(e))."),

    (6, "medium",
     "ఏ చట్టం ఆర్టికల్ 51A(g) — సహజ పర్యావరణ పరిరక్షణ విధిని అమలు చేస్తుంది?\n(Which Act operationalises Art 51A(g) — duty to protect and improve natural environment?)",
     "అటవీ పరిరక్షణ చట్టం 1980 / Forest Conservation Act 1980",
     "వన్యప్రాణుల రక్షణ చట్టం 1972 / Wildlife Protection Act 1972",
     "పర్యావరణ పరిరక్షణ చట్టం 1986 / Environment Protection Act 1986",
     "నీటి కాలుష్య నివారణ చట్టం 1974 / Water Pollution Prevention Act 1974",
     "C",
     "వర్మా కమిటీ 2002 నివేదిక: పర్యావరణ పరిరక్షణ చట్టం 1986 — సహజ పర్యావరణాన్ని రక్షించే విధి (Art 51A(g)) ను అమలు చేస్తుంది.\nVerma Committee 2002: Environment Protection Act 1986 operationalises the duty to protect and improve natural environment (Art 51A(g))."),

    (6, "medium",
     "ప్రాథమిక విధులు రాజ్యాంగంలో ఏ షెడ్యూల్‌లో ఉన్నాయి?\n(In which Schedule of the Indian Constitution are Fundamental Duties listed?)",
     "మూడవ షెడ్యూల్‌లో / Third Schedule",
     "ఏ షెడ్యూల్‌లోనూ లేవు — నేరుగా ఆర్టికల్ 51A లో / Not in any Schedule — directly in Article 51A",
     "నాలుగవ షెడ్యూల్‌లో / Fourth Schedule",
     "తొమ్మిదవ షెడ్యూల్‌లో / Ninth Schedule",
     "B",
     "ప్రాథమిక విధులు ఏ షెడ్యూల్‌లోనూ లేవు. అవి నేరుగా ఆర్టికల్ 51A (భాగం IVA) లో ఉన్నాయి. (పోల్చడానికి: FRs భాగం III లో; DPSPs భాగం IV లో)\nFundamental Duties are not in any Schedule. They are directly in Article 51A (Part IVA). Compare: FRs in Part III; DPSPs in Part IV."),

    # ══════════════ SECTION 7: TOUGH MCQs (4 MCQs) ══════════════

    (7, "hard",
     "కింది ఏది ఆర్టికల్ 51A కింద మూలభూత విధి కాదు?\n(Which of the following is NOT a Fundamental Duty under Article 51A?)",
     "శాస్త్రీయ దృక్పథం పెంపొందించడం / Develop scientific temper",
     "పన్నులు సకాలంలో చెల్లించడం / Pay taxes promptly",
     "సహజ పర్యావరణాన్ని రక్షించడం / Protect natural environment",
     "జాతీయ గీతాన్ని పాటించడం / Abide by the National Anthem",
     "B",
     "పన్నులు చెల్లించడం 11 మూలభూత విధులలో లేదు. ఇది సాధారణ పౌర బాధ్యత, కానీ Art 51A కింద మూలభూత విధి కాదు.\nPaying taxes is NOT among the 11 Fundamental Duties. It is a general civic obligation but not a Fundamental Duty under Art 51A."),

    (7, "hard",
     "కింది వ్యాఖ్యలలో ఏవి మూలభూత విధుల గురించి సరైనవి?\n1. అవి 44వ సవరణ 1978 ద్వారా జోడించబడ్డాయి\n2. అవి USSR నుండి స్వీకరించబడ్డాయి\n3. అవి కేవలం పౌరులకే వర్తిస్తాయి\n4. 11వ విధి 86వ సవరణ 2002 ద్వారా జోడించబడింది\n(Which statements are correct about Fundamental Duties?)",
     "2, 3 మరియు 4 మాత్రమే / Only 2, 3 and 4",
     "1, 2 మరియు 3 మాత్రమే / Only 1, 2 and 3",
     "3 మరియు 4 మాత్రమే / Only 3 and 4",
     "అన్నీ సరైనవి / All are correct",
     "A",
     "వ్యాఖ్య 1 తప్పు: FDs 42వ సవరణ 1976 ద్వారా జోడించబడ్డాయి (44వ సవరణ 1978 కాదు — 44వ సవరణ ఆస్తి హక్కు తొలగించింది). వ్యాఖ్యలు 2, 3, 4 అన్నీ సరైనవి.\nStatement 1 is wrong: FDs were added by 42nd Amendment 1976 (NOT 44th Amendment 1978 — which removed Right to Property). Statements 2, 3, 4 are all correct."),

    (7, "hard",
     "ఆర్టికల్ 51A(g) కింద మూలభూత విధి ఏమిటి?\n(What is the Fundamental Duty under Article 51A(g)?)",
     "సమ్మిళిత సంస్కృతి వారసత్వాన్ని విలువకట్టడం / Value rich heritage of composite culture",
     "సహజ పర్యావరణాన్ని రక్షించి మెరుగుపరచడం (అడవులు, సరస్సులు, నదులు, వన్యప్రాణులు) / Protect and improve natural environment (forests, lakes, rivers, wildlife)",
     "శాస్త్రీయ దృక్పథం పెంపొందించడం / Develop scientific temper and humanism",
     "సార్వజనిక ఆస్తి సంరక్షించడం / Safeguard public property",
     "B",
     "Art 51A విభాగాలు: (f) సమ్మిళిత సంస్కృతి; (g) సహజ పర్యావరణం; (h) శాస్త్రీయ దృక్పథం; (i) సార్వజనిక ఆస్తి. (g) = సహజ పర్యావరణ పరిరక్షణ.\nArt 51A clauses: (f) composite culture; (g) natural environment; (h) scientific temper; (i) public property. Art 51A(g) = Protect natural environment."),

    (7, "hard",
     "42వ సవరణ 1976 కింద జోడించిన 10 మూలభూత విధుల గురించి స్వర్ణ సింగ్ కమిటీ సిఫారసు మేరకు ఎన్ని విధులు ఉన్నాయి?\n(Of the 10 Fundamental Duties added by 42nd Amendment 1976, how many were as per Swaran Singh Committee's recommendation?)",
     "10 — అన్నీ కమిటీ సిఫారసు మేరకు / 10 — all as per Committee recommendation",
     "8 — కమిటీ 8 సిఫారసు చేసింది; పార్లమెంటు 2 అదనంగా జోడించింది / 8 — Committee recommended 8; Parliament added 2 more",
     "6 — పార్లమెంటు 4 మార్చింది / 6 — Parliament modified 4",
     "5 — సగం మాత్రమే / 5 — only half",
     "B",
     "స్వర్ణ సింగ్ కమిటీ 8 విధులు సిఫారసు చేసింది. 42వ సవరణ 1976 ద్వారా పార్లమెంటు 10 విధులు ఆమోదించింది — 2 అదనంగా జోడించింది.\nSwaran Singh Committee recommended 8 duties. The 42nd Amendment 1976 approved 10 duties — Parliament added 2 extra on its own."),

]



import json as _json


def _seed_polity_ch10_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    import json as _j
    ph = '%s' if use_postgres else '?'
    _sections = [
    {"title": "10.1 ప్రాథమిక విధులు పరిచయం", "sub": "Introduction · Part IVA · Art 51A · 42nd Amdt 1976 · USSR", "audio": ""},
    {"title": "10.2 11 విధుల జాబితా", "sub": "List of 11 Duties · Art 51A(a) to 51A(k) · All Duties", "audio": ""},
    {"title": "10.3 స్వభావం మరియు లక్షణాలు", "sub": "Nature · Features · Non-Justiciable · Moral Obligations", "audio": ""},
    {"title": "10.4 స్వర్ణ సింగ్ కమిటీ", "sub": "Swaran Singh Committee · 1976 · Recommendations · 8 Duties", "audio": ""},
    {"title": "10.5 86వ సవరణ — 11వ విధి", "sub": "86th Amendment 2002 · Art 51A(k) · 11th Duty · Education", "audio": ""},
    {"title": "10.6 FR vs FD vs DPSP పోలిక", "sub": "Comparison · Justiciable · Non-Justiciable · Sources", "audio": ""},
    {"title": "10.7 ముఖ్య కేసులు", "sub": "Cases · PYQs · APPSC · Fundamental Duties enforcement", "audio": ""},
    {"title": "10.8 కఠిన ప్రశ్నలు", "sub": "Tough MCQs · APPSC Style · Verma Committee · Art 51A clauses", "audio": ""}
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
        (10, 'Indian_Polity'))
    row = cur.fetchone()
    if row and not force:
        return {'success': True, 'already_exists': True,
                'message': 'Polity Ch10 notes already seeded.'}
    if row and force:
        db_exec_fn(conn,
            f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (10, 'Indian_Polity'))
    if use_postgres:
        conn.commit()

    db_exec_fn(conn,
        f"INSERT INTO study_notes "
        f"(subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'Indian_Polity', '', 10,
         'ప్రాథమిక విధులు',
         'Fundamental Duties',
         'Ch.10',
         _j.dumps(_sections, ensure_ascii=False)))
    conn.commit()
    return {'success': True, 'message': 'Polity Ch10 notes seeded!'}


def _seed_polity_ch10_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
        (10, 'Indian_Polity'))
    row = cur.fetchone()
    if not row:
        _seed_polity_ch10_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)
        cur = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (10, 'Indian_Polity'))
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
    for mcq in POLITY_CH10_MCQS:
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

    total = len(POLITY_CH10_MCQS)
    return {
        'success': True,
        'message': f'Polity Ch10 MCQs seeded! Total: {total}',
        'inserted': total,
        'easy': easy, 'medium': medium, 'hard': hard,
        'toughest': toughest, 'pyq': pyq
    }
