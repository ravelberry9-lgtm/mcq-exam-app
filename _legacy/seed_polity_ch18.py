# seed_polity_ch18.py
# Chapter 18 — Governor
# Total Sections: 8 | Total MCQs: 57 | PYQs: 5
# Sections:
#   0 — Appointment & Qualifications (8 MCQs)
#   1 — Term & Removal (8 MCQs)
#   2 — Executive Powers (8 MCQs)
#   3 — Legislative Powers (8 MCQs)
#   4 — Financial & Judicial Powers (7 MCQs)
#   5 — Discretionary Powers (6 MCQs)
#   6 — Governor vs President Comparison (6 MCQs)
#   7 — Miscellaneous / Constitutional Provisions (6 MCQs)

_CH = 18
_SUBJECT = 'GK'
_TOPIC   = 'Indian_Polity'
_TITLE_TE = 'గవర్నర్'
_TITLE_EN = 'Governor'
_PAGES    = 'Ch.18 (Lakshmikanth)'

_SECTIONS = [
    "నియామకం & అర్హతలు",
    "పదవీ కాలం & తొలగింపు",
    "కార్యనిర్వాహక అధికారాలు",
    "శాసన అధికారాలు",
    "ఆర్థిక & న్యాయ అధికారాలు",
    "విచక్షణ అధికారాలు",
    "గవర్నర్ vs రాష్ట్రపతి పోలిక",
    "విభిన్న రాజ్యాంగ నిబంధనలు",
]

_MCQS = [
    # ── Section 0: Appointment & Qualifications ────────────────────────────────
    (0, "easy",
     "రాష్ట్ర గవర్నర్‌ను నియమించే అధికారం ఎవరికి ఉంది? / Who appoints the Governor of a State?",
     "ముఖ్యమంత్రి / Chief Minister",
     "రాష్ట్రపతి / President",
     "ప్రధానమంత్రి / Prime Minister",
     "సుప్రీం కోర్ట్ / Supreme Court",
     "b",
     "అనుచ్ఛేదం 155: గవర్నర్‌ను రాష్ట్రపతి నియమిస్తారు. / Art.155: Governor is appointed by the President."),

    (0, "easy",
     "గవర్నర్ అర్హతలలో వయస్సు పరిమితి ఎంత? / Minimum age for Governor?",
     "25 సంవత్సరాలు / 25 years",
     "30 సంవత్సరాలు / 30 years",
     "35 సంవత్సరాలు / 35 years",
     "40 సంవత్సరాలు / 40 years",
     "c",
     "అనుచ్ఛేదం 157: గవర్నర్ కనీసం 35 సంవత్సరాల వయస్సు ఉండాలి. / Art.157: Governor must be at least 35 years of age."),

    (0, "medium",
     "గవర్నర్ అర్హతలలో ఏది నిజం? / Which is correct about Governor's qualifications?",
     "పార్లమెంటు సభ్యుడిగా ఉండాలి / Must be MP",
     "భారత పౌరుడు మరియు 35 ఏళ్ళు / Indian citizen and 35 years",
     "IAS అధికారిగా ఉండాలి / Must be IAS officer",
     "న్యాయ నిపుణుడుగా ఉండాలి / Must be legal expert",
     "b",
     "అనుచ్ఛేదం 157: గవర్నర్ భారత పౌరుడు మరియు 35 సంవత్సరాలకు పైగా వయస్సు ఉండాలి. / Art.157: Governor must be Indian citizen and not less than 35 years."),

    (0, "hard",
     "గవర్నర్ పార్లమెంటు/రాష్ట్ర శాసనసభ సభ్యుడుగా ఉంటే నియామకానికి ముందు ఏం జరగాలి? / If Governor-appointee is MP/MLA, what must happen?",
     "నియామకానంతర రాజీనామా / Resign after appointment",
     "నియామకానికి ముందు రాజీనామా అవసరం లేదు / No resignation needed",
     "నియామకానికి ముందే రాజీనామా చేయాలి / Must resign before appointment",
     "6 నెలల్లో రాజీనామా / Resign within 6 months",
     "c",
     "గవర్నర్ నియామక తేదీ నుండి పార్లమెంటు / రాష్ట్ర శాసనసభ సభ్యత్వం తనంతట తానే రద్దవుతుంది; ఆచరణలో ముందే రాజీనామా. / Membership auto-terminates; in practice, resign before appointment."),

    (0, "medium",
     "గవర్నర్ పదవికి అర్హుడు కానివాడు ఎవరు? / Who is disqualified for Governor's post?",
     "రిటైర్డ్ IAS అధికారి / Retired IAS officer",
     "న్యాయమూర్తి / Judge",
     "ఆ రాష్ట్ర నివాసి / Resident of that state",
     "రిటైర్డ్ జనరల్ / Retired General",
     "c",
     "అనుచ్ఛేదం 158(1) ప్రకారం గవర్నర్ నియామకమయ్యే రాష్ట్రానికి చెందినవాడు కాకుండా వేరే రాష్ట్రానికి చెందినవాడు అయి ఉండాలి (ఆచారం). / Convention: Governor should not be from the same state (outsider convention)."),

    (0, "medium",
     "గవర్నర్ నియామకంలో ఆచారం ప్రకారం ముఖ్యమంత్రికి ముందుగా సంప్రదించాలని ఏ సంఘం సిఫారసు చేసింది? / Which Commission recommended consulting CM before Governor's appointment?",
     "సర్కారియా కమిషన్ / Sarkaria Commission",
     "పుంఛి కమిషన్ / Punchhi Commission",
     "రాజమన్నార్ కమిటీ / Rajamannar Committee",
     "వెంకటాచలయ్య కమిషన్ / Venkatachalaiah Commission",
     "a",
     "సర్కారియా కమిషన్ (1988): గవర్నర్ నియామకానికి ముందు రాష్ట్ర ముఖ్యమంత్రిని సంప్రదించాలని సిఫారసు చేసింది. / Sarkaria Commission (1988): Recommended CM consultation before Governor's appointment."),

    (0, "hard",
     "ఒకే వ్యక్తి ఒకేసారి రెండు రాష్ట్రాలకు గవర్నర్‌గా పని చేయవచ్చా? / Can same person serve as Governor of two states simultaneously?",
     "ఎప్పుడూ కాదు / Never",
     "అవును, రాష్ట్రపతి అదనపు బాధ్యత అప్పగిస్తే / Yes, if President assigns additional charge",
     "కేవలం పొరుగు రాష్ట్రాలకు మాత్రమే / Only for neighbouring states",
     "రాజ్యసభ ఆమోదంతో మాత్రమే / Only with RS approval",
     "b",
     "అనుచ్ఛేదం 153 నిబంధన: ఒకే వ్యక్తి రెండు రాష్ట్రాలకు గవర్నర్‌గా పని చేయవచ్చు (7వ సవరణ 1956 ద్వారా). / Art.153 proviso: Same person can be Governor of two+ states (7th Amendment 1956)."),

    (0, "easy",
     "గవర్నర్ ప్రమాణ స్వీకారం ఎవరి ముందు చేస్తారు? / Before whom does Governor take oath?",
     "రాష్ట్రపతి / President",
     "ముఖ్యమంత్రి / Chief Minister",
     "హైకోర్టు ప్రధాన న్యాయమూర్తి / Chief Justice of High Court",
     "స్పీకర్ / Speaker",
     "c",
     "అనుచ్ఛేదం 159: గవర్నర్ ఆ రాష్ట్ర హైకోర్టు ప్రధాన న్యాయమూర్తి ముందు ప్రమాణం చేస్తారు. / Art.159: Governor takes oath before the Chief Justice of the concerned High Court."),

    # ── Section 1: Term & Removal ───────────────────────────────────────────────
    (1, "easy",
     "గవర్నర్ పదవీ కాలం ఎంత? / What is the term of a Governor?",
     "3 సంవత్సరాలు / 3 years",
     "4 సంవత్సరాలు / 4 years",
     "5 సంవత్సరాలు / 5 years",
     "6 సంవత్సరాలు / 6 years",
     "c",
     "అనుచ్ఛేదం 156(1): గవర్నర్ 5 సంవత్సరాల పదవీ కాలం పాటు పని చేస్తారు. / Art.156(1): Governor holds office for a term of 5 years."),

    (1, "medium",
     "గవర్నర్‌ను ఎవరు తొలగించవచ్చు? / Who can remove a Governor?",
     "రాష్ట్ర శాసనసభ / State Legislature",
     "రాష్ట్రపతి / President",
     "ప్రధానమంత్రి నేరుగా / PM directly",
     "సుప్రీం కోర్ట్ / Supreme Court",
     "b",
     "అనుచ్ఛేదం 156(1): గవర్నర్ రాష్ట్రపతి సంతోషం ఉన్నంత కాలం పదవిలో ఉంటారు. రాష్ట్రపతి తొలగించవచ్చు. / Art.156(1): Governor holds office at President's pleasure — President can remove."),

    (1, "hard",
     "గవర్నర్ తొలగింపులో రాజ్యాంగ పరిమితులు ఏమిటి? / Constitutional constraints on removing a Governor?",
     "కారణం చెప్పకుండా తొలగించవచ్చు / Can be removed without reason",
     "అభిశంసన ప్రక్రియ అవసరం / Impeachment required",
     "రాష్ట్రపతికి కారణాలు చెప్పాలి — రాజ్యాంగంలో నిర్దిష్ట నిబంధనలు లేవు / Reasons to President — no specific grounds in Constitution",
     "హైకోర్టు తీర్పు అవసరం / HC judgment required",
     "a",
     "రాజ్యాంగం తొలగింపుకు నిర్దిష్ట కారణాలు చెప్పలేదు. రాష్ట్రపతి సంతోషం ఆధారంగా తొలగించవచ్చు — అయితే B.P. Singhal కేసులో SC కారణాలు ఉండాలని తీర్పు. / No specific grounds in Constitution; SC in B.P. Singhal case ruled reasons must exist."),

    (1, "medium",
     "గవర్నర్ రాజీనామా ఎవరికి ఇస్తారు? / To whom does Governor submit resignation?",
     "ముఖ్యమంత్రికి / Chief Minister",
     "రాష్ట్రపతికి / President",
     "లోక్‌సభ స్పీకర్‌కు / LS Speaker",
     "హైకోర్టు CJకి / HC Chief Justice",
     "b",
     "అనుచ్ఛేదం 156(2): గవర్నర్ రాజీనామాను రాష్ట్రపతికి ఇస్తారు. / Art.156(2): Governor resigns by writing to the President."),

    (1, "easy",
     "గవర్నర్ పదవి ఖాళీగా ఉంటే 'లెఫ్టినెంట్ గవర్నర్' పని చేయగలరా? / Can Lieutenant Governor discharge Governor's functions?",
     "అవును / Yes",
     "లేదు / No",
     "పరిమితంగా మాత్రమే / Only partially",
     "రాష్ట్ర అసెంబ్లీ ఆమోదంతో / With state assembly approval",
     "b",
     "గవర్నర్ పదవి ఖాళీగా ఉంటే రాష్ట్రపతి హైకోర్టు CJని లేదా ఇతర గవర్నర్‌ని అదనపు బాధ్యత ఇస్తారు — Lieutenant Governor అనే పదవి రాష్ట్రాల్లో లేదు (UT లో మాత్రమే). / No LG for states; HC CJ or another Governor given additional charge."),

    (1, "hard",
     "గవర్నర్ పదవి ఎప్పుడు ఖాళీ అవుతుంది? / When does Governor's office fall vacant?",
     "5 సంవత్సరాల తర్వాత మాత్రమే / Only after 5 years",
     "మరణం, రాజీనామా, తొలగింపు లేదా పదవీ కాలం ముగిసినప్పుడు / Death, resignation, removal or expiry of term",
     "లోక్‌సభ రద్దు అయినప్పుడు / When LS dissolves",
     "ముఖ్యమంత్రి మారినప్పుడు / When CM changes",
     "b",
     "గవర్నర్ పదవి మరణం, రాజీనామా, రాష్ట్రపతి తొలగింపు లేదా 5 సంవత్సరాల పదవీ కాలం ముగిసినప్పుడు ఖాళీ అవుతుంది. / Governor's office vacates on death, resignation, removal by President, or term expiry."),

    (1, "medium",
     "పదవీ కాలం ముగిసిన తర్వాత గవర్నర్ ఎంత కాలం పని చేయగలరు? / How long can Governor continue after term expiry?",
     "మరో 3 నెలలు / 3 more months",
     "మరో 6 నెలలు / 6 more months",
     "వారసుడు పదవి చేపట్టే వరకు / Until successor takes charge",
     "ఒక్క రోజు కూడా కాదు / Not even one day",
     "c",
     "అనుచ్ఛేదం 156(1) నిబంధన: వారసుడు పదవి చేపట్టే వరకు గవర్నర్ పదవిలో కొనసాగవచ్చు. / Art.156(1) proviso: Governor continues until successor assumes charge."),

    (1, "easy",
     "గవర్నర్ నియామకంలో ఆచారం ప్రకారం ఒక వ్యక్తి ఒక రాష్ట్రంలో ఎంత కాలానికంటే ఎక్కువ గవర్నర్‌గా ఉండకూడదు? / Convention: A Governor should not hold office in same state for more than?",
     "1 పదవీ కాలం / 1 term",
     "2 పదవీ కాలాలు / 2 terms",
     "3 పదవీ కాలాలు / 3 terms",
     "రాజ్యాంగ పరిమితి లేదు / No constitutional limit",
     "d",
     "రాజ్యాంగంలో పదవీ కాల పరిమితి లేదు — ఒకే రాష్ట్రంలో పదే పదే గవర్నర్‌గా ఉండవచ్చు. / No constitutional limit on terms — can be reappointed."),

    # ── Section 2: Executive Powers ─────────────────────────────────────────────
    (2, "easy",
     "రాష్ట్ర ముఖ్యమంత్రిని నియమించే అధికారం గవర్నర్‌కు ఉందా? / Does Governor appoint Chief Minister?",
     "లేదు / No",
     "అవును / Yes",
     "రాష్ట్రపతి ఆమోదంతో / With President's approval",
     "విధానసభ ఎన్నిక చేస్తుంది / Vidhan Sabha elects",
     "b",
     "అనుచ్ఛేదం 164(1): గవర్నర్ ముఖ్యమంత్రిని నియమిస్తారు; ముఖ్యమంత్రి సలహాపై ఇతర మంత్రులను నియమిస్తారు. / Art.164(1): Governor appoints CM; on CM's advice appoints other ministers."),

    (2, "medium",
     "గవర్నర్ రాష్ట్ర అడ్వకేట్ జనరల్‌ను నియమించే అధికారం ఏ అనుచ్ఛేదంలో ఉంది? / Art. for Governor appointing Advocate General of State?",
     "అనుచ్ఛేదం 161 / Art.161",
     "అనుచ్ఛేదం 165 / Art.165",
     "అనుచ్ఛేదం 167 / Art.167",
     "అనుచ్ఛేదం 170 / Art.170",
     "b",
     "అనుచ్ఛేదం 165: గవర్నర్ రాష్ట్ర అడ్వకేట్ జనరల్‌ను నియమిస్తారు. / Art.165: Governor appoints the Advocate General of the State."),

    (2, "easy",
     "రాష్ట్ర పబ్లిక్ సర్వీస్ కమిషన్ అధ్యక్షుడిని నియమించే వ్యక్తి ఎవరు? / Who appoints Chairman of State PSC?",
     "ముఖ్యమంత్రి / Chief Minister",
     "గవర్నర్ / Governor",
     "రాష్ట్రపతి / President",
     "UPSC Chairman",
     "b",
     "అనుచ్ఛేదం 316: గవర్నర్ రాష్ట్ర పబ్లిక్ సర్వీస్ కమిషన్ అధ్యక్షుడిని నియమిస్తారు. / Art.316: Governor appoints Chairman of State PSC."),

    (2, "medium",
     "రాష్ట్రంలో రాష్ట్రపతి పాలన (Art.356) విధించమని రాష్ట్రపతికి నివేదించే వ్యక్తి ఎవరు? / Who reports to President for imposing President's Rule (Art.356)?",
     "ముఖ్యమంత్రి / Chief Minister",
     "హైకోర్టు CJ / HC CJ",
     "గవర్నర్ / Governor",
     "రాజ్యసభ నాయకుడు / RS leader",
     "c",
     "అనుచ్ఛేదం 356: గవర్నర్ నివేదిక ఆధారంగా రాష్ట్రపతి రాష్ట్రపతి పాలన విధిస్తారు. / Art.356: President imposes President's Rule based on Governor's report."),

    (2, "hard",
     "గవర్నర్ అధికారులు 'రాష్ట్రపతి సంతోషం వద్ద' (pleasure doctrine) కింద ఉంటారు — ఇది ఏ అనుచ్ఛేదం? / Which Art states that civil servants hold office at 'pleasure' of Governor?",
     "అనుచ్ఛేదం 154 / Art.154",
     "అనుచ్ఛేదం 162 / Art.162",
     "అనుచ్ఛేదం 309 / Art.309",
     "అనుచ్ఛేదం 310 / Art.310",
     "d",
     "అనుచ్ఛేదం 310: కేంద్ర-రాష్ట్ర పౌర సేవకులు రాష్ట్రపతి/గవర్నర్ సంతోషం వద్ద పదవిలో ఉంటారు. / Art.310: Civil servants hold office during pleasure of President/Governor."),

    (2, "medium",
     "గవర్నర్‌ను 'రాజ్యాంగ కాపలాదారు' (Constitutional Sentinel) అని అభివర్ణించిన పండితుడు ఎవరు? / Who described the Governor as 'Constitutional Sentinel'?",
     "బి.ఆర్. అంబేడ్కర్ / B.R. Ambedkar",
     "జవహర్‌లాల్ నెహ్రూ / Nehru",
     "కె.ఎం. మున్షీ / K.M. Munshi",
     "సర్ అలాడి కృష్ణస్వామి అయ్యర్ / Sir Alladi",
     "c",
     "K.M. Munshi: గవర్నర్ 'రాజ్యాంగ కాపలాదారు' (Constitutional Sentinel) — రాజ్యాంగ విలువలు కాపాడే బాధ్యత గవర్నర్‌కు ఉంటుంది. B.R. Ambedkar గవర్నర్‌ను Centre-State link గా చూశారు. / K.M. Munshi described Governor as 'Constitutional Sentinel' — guardian of constitutional values."),

    (2, "easy",
     "రాష్ట్ర ప్రభుత్వ అన్ని కార్యనిర్వాహక చర్యలు ఏ పేరిట తీసుకోబడతాయి? / All executive actions of state government are taken in whose name?",
     "ముఖ్యమంత్రి / Chief Minister",
     "గవర్నర్ / Governor",
     "రాష్ట్రపతి / President",
     "రాష్ట్ర మంత్రిమండలి / State CoM",
     "b",
     "అనుచ్ఛేదం 154: రాష్ట్ర కార్యనిర్వాహక అధికారం గవర్నర్‌కు ఉంటుంది; అన్ని చర్యలు గవర్నర్ పేరిట. / Art.154: Executive power of state vested in Governor; all actions taken in Governor's name."),

    (2, "hard",
     "గవర్నర్ హంగ్ అసెంబ్లీలో ప్రభుత్వ ఏర్పాటు ఆహ్వానించేటప్పుడు ఎవరిని పిలవాలి? / In case of hung assembly, whom should Governor invite to form government?",
     "అతిపెద్ద పార్టీ / Single largest party",
     "ముందుగా ఏర్పాటైన కూటమి / Pre-poll alliance",
     "అసెంబ్లీలో అత్యధిక మద్దతు నిరూపించగలిగే వ్యక్తి / Person most likely to command majority in House",
     "అంతకు ముందు ముఖ్యమంత్రి / Previous CM",
     "c",
     "S.R. బొమ్మై కేసు (1994): గవర్నర్ అసెంబ్లీలో అత్యధిక మద్దతు నిరూపించగలిగిన వ్యక్తిని ఆహ్వానించాలి — ఊహ ఆధారంగా కాదు. / S.R. Bommai 1994: Invite person most likely to command Assembly majority — test on floor."),

    # ── Section 3: Legislative Powers ───────────────────────────────────────────
    (3, "easy",
     "గవర్నర్ రాష్ట్ర శాసనసభ సమావేశాలు ఏర్పాటు చేయగలరా? / Can Governor summon state legislature sessions?",
     "లేదు / No",
     "అవును / Yes",
     "రాష్ట్రపతి ఆమోదంతో మాత్రమే / Only with President's approval",
     "ముఖ్యమంత్రి మాత్రమే / Only CM",
     "b",
     "అనుచ్ఛేదం 174: గవర్నర్ రాష్ట్ర శాసనసభ సమావేశాలు ఏర్పాటు చేయడం, వాయిదా వేయడం, రద్దు చేయడం చేయవచ్చు. / Art.174: Governor summons, prorogues, dissolves state legislature."),

    (3, "medium",
     "గవర్నర్ రాష్ట్ర శాసనసభకు ఎన్ని సభ్యులను నామినేట్ చేయగలరు (విధానపరిషత్‌కు)? / How many members can Governor nominate to Vidhan Parishad?",
     "6 మంది / 6",
     "1/6 వంతు / 1/6th",
     "12 మంది / 12",
     "రాష్ట్రపతి నిర్ణయించే సంఖ్య / Number decided by President",
     "b",
     "అనుచ్ఛేదం 171(5): గవర్నర్ విధానపరిషత్ (Legislative Council) సభ్యుల 1/6 వంతు నామినేట్ చేయగలరు. / Art.171(5): Governor nominates 1/6th of Vidhan Parishad members."),

    (3, "easy",
     "రాష్ట్ర శాసనసభ ఆమోదించిన బిల్లుకు గవర్నర్ ఏమి చేయవచ్చు? / What can Governor do with a Bill passed by state legislature?",
     "ఆమోదించడం లేదా రాష్ట్రపతికి సూచించడం మాత్రమే / Only assent or refer to President",
     "ఆమోదించడం, తిరస్కరించడం, తిరిగి పంపడం లేదా రాష్ట్రపతి పరిశీలనకు నివేదించడం / Assent, withhold, return or reserve for President",
     "ఆమోదించడం మాత్రమే / Only assent",
     "తిరస్కరించడం మాత్రమే / Only reject",
     "b",
     "అనుచ్ఛేదం 200: గవర్నర్ బిల్లుకు ఆమోదం ఇవ్వవచ్చు, ఆమోదం నిలిపివేయవచ్చు, తిరిగి పంపవచ్చు, లేదా రాష్ట్రపతి పరిశీలనకు నివేదించవచ్చు. / Art.200: Governor may assent, withhold assent, return (except Money Bill), or reserve for President."),

    (3, "hard",
     "గవర్నర్ మనీ బిల్లును తిరిగి పంపవచ్చా? / Can Governor return a Money Bill?",
     "అవును / Yes",
     "లేదు / No",
     "రాష్ట్రపతి అనుమతితో / With President's permission",
     "అత్యవసరంలో మాత్రమే / Only in emergency",
     "b",
     "అనుచ్ఛేదం 200: Money Bill ని గవర్నర్ తిరిగి పంపే అధికారం లేదు — ఆమోదించాలి లేదా రాష్ట్రపతికి నివేదించాలి. / Art.200: Governor cannot return a Money Bill — must either assent or reserve for President."),

    (3, "medium",
     "గవర్నర్ ఆర్డినెన్స్ జారీ చేయగల అనుచ్ఛేదం ఏది? / Which Article empowers Governor to promulgate Ordinance?",
     "అనుచ్ఛేదం 123 / Art.123",
     "అనుచ్ఛేదం 213 / Art.213",
     "అనుచ్ఛేదం 200 / Art.200",
     "అనుచ్ఛేదం 174 / Art.174",
     "b",
     "అనుచ్ఛేదం 213: శాసనసభ సమావేశంలో లేనప్పుడు గవర్నర్ ఆర్డినెన్స్ జారీ చేయగలరు. / Art.213: Governor can promulgate Ordinances when legislature is not in session.", 'APPSC'),

    (3, "medium",
     "గవర్నర్ ఆర్డినెన్స్ శాసనసభ సమావేశమైన తర్వాత ఎంత కాలంలో ఆమోదం పొందాలి? / Within how long must an Ordinance be approved after legislature assembles?",
     "3 నెలలు / 3 months",
     "6 వారాలు / 6 weeks",
     "2 నెలలు / 2 months",
     "1 నెల / 1 month",
     "b",
     "అనుచ్ఛేదం 213(2)(a): ఆర్డినెన్స్ శాసనసభ సమావేశమైన తర్వాత 6 వారాల లోపు ఆమోదం పొందాలి. / Art.213(2)(a): Ordinance must be approved within 6 weeks of legislature reassembling."),

    (3, "easy",
     "గవర్నర్ ఆర్డినెన్స్ జారీ చేయడంలో రాష్ట్రపతితో పోలిక ఏమిటి? / How is Governor's Ordinance power compared to President's?",
     "గవర్నర్ అధికారం ఎక్కువ / Governor's power is greater",
     "రాష్ట్రపతి అధికారానికి సంబంధించిన State List మాత్రమే / Only State List matters",
     "రాష్ట్రపతి Art.123 వంటిదే; గవర్నర్ Art.213 — రాష్ట్ర జాబితాకు మాత్రమే / President Art.123 similar; Governor Art.213 — for State List only",
     "గవర్నర్ ఆర్డినెన్స్ జారీ చేయలేరు / Governor cannot issue Ordinances",
     "c",
     "రాష్ట్రపతి Art.123 — Union List; గవర్నర్ Art.213 — State List. కొన్ని మాత్రల్లో గవర్నర్ రాష్ట్రపతి అనుమతి అవసరం. / President: Art.123 (Union List); Governor: Art.213 (State List). Governor needs Presidential sanction in some cases."),

    (3, "hard",
     "గవర్నర్ ఆర్డినెన్స్ జారీ చేయడానికి రాష్ట్రపతి పూర్వ అనుమతి ఏ విషయాల్లో అవసరం? / In which cases does Governor need prior Presidential sanction for Ordinance?",
     "ఎప్పుడూ అవసరం లేదు / Never required",
     "అసెంబ్లీ ఆమోదం అవసరమయ్యే అంశాలు / Matters requiring Presidential assent for Bills",
     "రాష్ట్ర జాబితా అంశాలు / State List matters only",
     "ఎల్లప్పుడూ అవసరం / Always required",
     "b",
     "Art.213(1) నిబంధన: బిల్లుకు రాష్ట్రపతి ఆమోదం అవసరమయ్యే విషయాల్లో ఆర్డినెన్స్‌కు రాష్ట్రపతి పూర్వ అనుమతి అవసరం. / Art.213(1) proviso: Presidential sanction required for Ordinances on matters needing Presidential assent for Bills."),

    # ── Section 4: Financial & Judicial Powers ─────────────────────────────────
    (4, "easy",
     "రాష్ట్ర బడ్జెట్‌ను శాసనసభలో ప్రవేశపెట్టేందుకు ఎవరి సిఫారసు అవసరం? / Whose recommendation is needed to introduce State Budget in legislature?",
     "ముఖ్యమంత్రి / Chief Minister",
     "ఆర్థిక మంత్రి / Finance Minister",
     "గవర్నర్ / Governor",
     "రాష్ట్రపతి / President",
     "c",
     "అనుచ్ఛేదం 202(1): రాష్ట్ర వార్షిక ఆర్థిక నివేదిక (బడ్జెట్) గవర్నర్ సిఫారసుపై శాసనసభలో ప్రవేశపెట్టబడుతుంది. / Art.202(1): Annual Financial Statement (Budget) laid before legislature by Governor's direction."),

    (4, "medium",
     "క్షమాభిక్ష (Pardon) గవర్నర్ ఏ అనుచ్ఛేదం కింద ఇస్తారు? / Under which Article does Governor grant Pardon?",
     "అనుచ్ఛేదం 72 / Art.72",
     "అనుచ్ఛేదం 161 / Art.161",
     "అనుచ్ఛేదం 163 / Art.163",
     "అనుచ్ఛేదం 165 / Art.165",
     "b",
     "అనుచ్ఛేదం 161: గవర్నర్ రాష్ట్ర చట్టాలకు సంబంధించిన నేరాలకు క్షమాభిక్ష, జరిమానా తగ్గింపు మొదలైన అధికారాలు ఉంటాయి. / Art.161: Governor's pardoning powers for offences against state laws."),

    (4, "hard",
     "గవర్నర్ (Art.161) మరియు రాష్ట్రపతి (Art.72) క్షమాభిక్ష అధికారాల మధ్య తేడా ఏమిటి? / Key difference between Governor (Art.161) and President (Art.72) pardoning powers?",
     "గవర్నర్ మరణ శిక్షలను మాఫీ చేయగలరు / Governor can pardon death sentences",
     "రాష్ట్రపతి మాత్రమే మరణ శిక్షలను మాఫీ చేయగలరు / Only President can pardon death sentences",
     "రెండూ సమానం / Both equal",
     "గవర్నర్ కోర్ట్ మార్షల్ అధికారం ఉంది / Governor has court martial power",
     "b",
     "తేడాలు: రాష్ట్రపతి మాత్రమే (1) మరణ శిక్ష మాఫీ (2) కోర్ట్ మార్షల్ (3) Union చట్టాలు పరిధి. గవర్నర్ వీటిలో మొదటి రెండు అధికారాలు లేవు. / President alone can: pardon death sentence, court martial offences, Union law offences. Governor lacks these two."),

    (4, "medium",
     "రాష్ట్ర హైకోర్టు న్యాయమూర్తుల నియామకంలో గవర్నర్ పాత్ర ఏమిటి? / Governor's role in HC judges' appointment?",
     "నేరుగా నియమిస్తారు / Directly appoints",
     "రాష్ట్రపతికి సంప్రదించబడతారు / Consulted by President",
     "నామినేట్ చేస్తారు / Nominates",
     "ఎలాంటి పాత్ర లేదు / No role",
     "b",
     "అనుచ్ఛేదం 217: రాష్ట్ర హైకోర్టు న్యాయమూర్తులను రాష్ట్రపతి CJI మరియు గవర్నర్‌తో సంప్రదించి నియమిస్తారు. / Art.217: President appoints HC judges after consulting CJI and Governor."),

    (4, "easy",
     "రాష్ట్ర ఆర్థిక సంఘం (State Finance Commission) ఎవరి ఆదేశంపై ఏర్పాటవుతుంది? / State Finance Commission is constituted on whose order?",
     "ముఖ్యమంత్రి / Chief Minister",
     "గవర్నర్ / Governor",
     "రాష్ట్రపతి / President",
     "కేంద్ర ఆర్థిక మంత్రి / Union Finance Minister",
     "b",
     "అనుచ్ఛేదం 243-I: గవర్నర్ రాష్ట్ర ఆర్థిక సంఘాన్ని ఏర్పాటు చేస్తారు — పంచాయతీ సంస్థలకు నిధుల కేటాయింపు. / Art.243-I: Governor constitutes State Finance Commission for Panchayati Raj finance."),

    (4, "medium",
     "రాష్ట్ర శాసనసభ ఆమోదించిన మనీ బిల్లుకు గవర్నర్ ఆమోదం నిరాకరించగలరా? / Can Governor withhold assent to a Money Bill passed by state legislature?",
     "అవును / Yes",
     "లేదు / No",
     "రాష్ట్రపతి ఆజ్ఞతో మాత్రమే / Only on President's instruction",
     "కేవలం రాష్ట్రపతికి నివేదించవచ్చు / Can only reserve for President",
     "d",
     "అనుచ్ఛేదం 200: గవర్నర్ మనీ బిల్లును తిరిగి పంపలేరు; ఆమోదించాలి లేదా రాష్ట్రపతికి నివేదించవచ్చు. / Art.200: Governor cannot return Money Bill — must assent or reserve for Presidential consideration."),

    (4, "hard",
     "గవర్నర్ విచక్షణతో రాష్ట్రపతి పరిశీలనకు బిల్లు నివేదించగల అనుచ్ఛేదం ఏది? / Art. enabling Governor to reserve a Bill for Presidential consideration on own discretion?",
     "అనుచ్ఛేదం 200 / Art.200",
     "అనుచ్ఛేదం 201 / Art.201",
     "అనుచ్ఛేదం 213 / Art.213",
     "అనుచ్ఛేదం 163 / Art.163",
     "a",
     "అనుచ్ఛేదం 200: గవర్నర్ కొన్ని బిల్లులను (ముఖ్యంగా HC అధికారాలను ప్రభావితం చేసే) విచక్షణతో రాష్ట్రపతికి నివేదించవచ్చు. / Art.200: Governor may reserve (on own discretion) Bills affecting HC powers for Presidential consideration."),

    (4, "medium",
     "గవర్నర్ క్షమాభిక్ష (pardon) అధికారాలు ఏ అనుచ్ఛేదం? / Governor's pardon powers are under which Article?",
     "అనుచ్ఛేదం 72 / Art.72",
     "అనుచ్ఛేదం 161 / Art.161",
     "అనుచ్ఛేదం 165 / Art.165",
     "అనుచ్ఛేదం 166 / Art.166",
     "b",
     "అనుచ్ఛేదం 161: గవర్నర్ రాష్ట్ర చట్టాల కింద శిక్షలు అనుభవిస్తున్న నేరస్థులకు క్షమాభిక్ష, తగ్గింపు, మార్పు ఇవ్వవచ్చు. Art.72 = రాష్ట్రపతి పార్డన్ (అన్ని కేసులు + మరణశిక్ష + కోర్ట్ మార్షల్); Art.161 = గవర్నర్ పార్డన్ (రాష్ట్ర చట్టాలు మాత్రమే). / Art.161: Governor's pardon power for offences against state laws. Art.72 = President's broader powers including death sentence and court martial."),

    # ── Section 5: Discretionary Powers ────────────────────────────────────────
    (5, "easy",
     "గవర్నర్ విచక్షణ (discretionary) అధికారాలు ఏ అనుచ్ఛేదంలో ఉన్నాయి? / Governor's discretionary powers are in which Article?",
     "అనుచ్ఛేదం 154 / Art.154",
     "అనుచ్ఛేదం 163 / Art.163",
     "అనుచ్ఛేదం 165 / Art.165",
     "అనుచ్ఛేదం 174 / Art.174",
     "b",
     "అనుచ్ఛేదం 163(1): గవర్నర్ కొన్ని విషయాల్లో విచక్షణతో పని చేయవచ్చు. / Art.163(1): Governor may act in his discretion in certain matters."),

    (5, "medium",
     "హంగ్ అసెంబ్లీలో గవర్నర్ ముఖ్యమంత్రిని నియమించేటప్పుడు ఏ విధమైన అధికారం వినియోగిస్తారు? / What type of power does Governor exercise in appointing CM in hung assembly?",
     "సాంప్రదాయిక అధికారం / Conventional power",
     "విచక్షణ అధికారం / Discretionary power",
     "సాధారణ అధికారం / Normal power",
     "న్యాయ అధికారం / Judicial power",
     "b",
     "హంగ్ అసెంబ్లీలో మెజారిటీ నిర్ణయించడంలో గవర్నర్ విచక్షణ వినియోగిస్తారు. / In a hung assembly, Governor exercises discretion to determine who commands majority."),

    (5, "hard",
     "రాజ్యాంగ అనుచ్ఛేదం 163(2) ప్రకారం గవర్నర్ విచక్షణపై కోర్టు ఏం చేయగలదు? / What can courts do with Governor's discretion under Art.163(2)?",
     "పూర్తిగా పరిశీలించవచ్చు / Can fully review",
     "అసలు పరిశీలించలేరు / Cannot review at all",
     "కేవలం మాల్‌ఫైడ్ నిర్ణయాలు మాత్రమే సవాలు / Only mala fide decisions challenged",
     "రాష్ట్రపతి ఆదేశంతో మాత్రమే / Only on Presidential direction",
     "b",
     "అనుచ్ఛేదం 163(2): గవర్నర్ విచక్షణ వినియోగం సరైనదా కాదా అని పరీక్షించే అధికారం కోర్టులకు లేదు. / Art.163(2): Court cannot inquire into whether Governor should have acted on discretion."),

    (5, "medium",
     "గవర్నర్ 6వ షెడ్యూల్ కింద విచక్షణ అధికారాలు ఏ రాష్ట్రంలో ఉన్నాయి? / Under 6th Schedule, Governor's special discretionary powers are in which states?",
     "ఉత్తరప్రదేశ్ & మహారాష్ట్ర / UP & Maharashtra",
     "అసోం, మేఘాలయ, త్రిపుర, మిజోరాం / Assam, Meghalaya, Tripura, Mizoram",
     "జమ్మూ & కాశ్మీర్ మాత్రమే / J&K only",
     "అన్ని ఈశాన్య రాష్ట్రాలు / All NE states",
     "b",
     "6వ షెడ్యూల్: అసోం, మేఘాలయ, త్రిపుర, మిజోరాంలో గవర్నర్‌కు గిరిజన ప్రాంత నిర్వహణలో ప్రత్యేక విచక్షణ అధికారాలు ఉన్నాయి. / 6th Schedule: Governors of Assam, Meghalaya, Tripura, Mizoram have special tribal area discretionary powers."),

    (5, "easy",
     "రాష్ట్ర మంత్రిమండలి నిర్ణయాలను గవర్నర్‌కు తెలియజేయాలని ఎవరు బాధ్యత వహిస్తారు? / Who is responsible for communicating state cabinet decisions to Governor?",
     "స్పీకర్ / Speaker",
     "ముఖ్యమంత్రి / Chief Minister",
     "అడ్వకేట్ జనరల్ / Advocate General",
     "ముఖ్య కార్యదర్శి / Chief Secretary",
     "b",
     "అనుచ్ఛేదం 167: ముఖ్యమంత్రి రాష్ట్ర వ్యవహారాలు మరియు శాసన ప్రతిపాదనలు గవర్నర్‌కు తెలియజేయాలి. / Art.167: CM must communicate to Governor all decisions of state cabinet and legislative proposals."),

    (5, "hard",
     "గవర్నర్ విచక్షణ అధికారాల పట్టికలో (సర్కారియా కమిషన్ వర్గీకరణ) ఏవి ఉంటాయి? / Per Sarkaria Commission, which are Governor's discretionary powers?",
     "ఆర్థిక అధికారాలు మాత్రమే / Only financial powers",
     "CM నియామకం (హంగ్ అసెంబ్లీ), CM రాజీనామా, Art.356 నివేదిక, బిల్లు రాష్ట్రపతికి నివేదించడం / CM appointment (hung), CM resignation, Art.356 report, reserving Bills",
     "కేవలం అసెంబ్లీ రద్దు / Only dissolution",
     "న్యాయ నియామకాలు మాత్రమే / Only judicial appointments",
     "b",
     "సర్కారియా కమిషన్: గవర్నర్ విచక్షణ అధికారాలు — హంగ్ అసెంబ్లీలో CM నియామకం, CM రాజీనామా, Art.356 నివేదిక పంపడం, అసెంబ్లీ రద్దు. / Sarkaria: CM appointment (hung assembly), CM resignation, Art.356 report, dismissal of ministry, dissolution."),

    (5, "medium",
     "గవర్నర్ Art.163(2) కింద విచక్షణ వ్యాయమం గురించి కోర్టులు ఏమి విచారించగలవు? / Under Art.163(2), what can courts inquire regarding Governor's discretion?",
     "గవర్నర్ విచక్షణ విషయాలు పూర్తిగా కోర్టు సమీక్షకు లోబడతాయి / Fully subject to judicial review",
     "గవర్నర్ విచక్షణ వ్యాయమం సరైనదా అని విచారించలేరు / Courts cannot inquire into whether a matter is within discretion",
     "కేవలం SC విచారించగలదు / Only SC can inquire",
     "రాష్ట్రపతి అనుమతితో మాత్రమే విచారించగలరు / Only with President's permission",
     "b",
     "Art.163(2): గవర్నర్ విచక్షణ వ్యాయమం చేయవలసిన విషయంలో కోర్టు విచారణ చేయలేదు. గవర్నర్ చర్య మంత్రులు సలహాపై చేసిందా లేదా విచక్షణతో చేసిందా అని కూడా కోర్టు విచారించలేదు. / Art.163(2): No inquiry in any court as to whether any and if so what advice was tendered by ministers to Governor."),

    (5, "hard",
     "అసెంబ్లీలో మెజారిటీ రాష్ట్రపతి పాలనకు ముందు CM రాజీనామా చేయలేదు అంటే గవర్నర్ ఏమి చేయాలి? / If CM doesn't resign before Art.356 rule, what should Governor do?",
     "CM ని బలవంతంగా తొలగించాలి / Forcibly remove CM",
     "Art.356 నివేదిక పంపిన తర్వాత CM స్వయంగా పదవి కోల్పోతారు / CM automatically loses office after Art.356",
     "CM ని తొలగించి కొత్త CM నియమించాలి / Remove and appoint new CM",
     "SC సలహా తీసుకోవాలి / Seek SC advice",
     "b",
     "Art.356 ద్వారా రాష్ట్రపతి పాలన విధించినప్పుడు, రాజ్యాంగ యంత్రం విఫలమైనట్లు పరిగణించి, CM సహా మంత్రిమండలి స్వయంగా పదవి కోల్పోతుంది. / When President's Rule is proclaimed under Art.356, the CM and CoM automatically cease to hold office."),

    # ── Section 6: Governor vs President ────────────────────────────────────────
    (6, "easy",
     "గవర్నర్ మరియు రాష్ట్రపతి ఇద్దరూ ఏ అంశంలో సమానం? / In which aspect are Governor and President similar?",
     "ఎన్నికలు / Elections",
     "రాజ్యాంగపరమైన (nominal) అధిపతి / Constitutional head",
     "అధికార కాలం / Term",
     "పదవి ఆదాయం / Income",
     "b",
     "రాష్ట్రపతి కేంద్రానికి రాజ్యాంగపరమైన అధిపతి; గవర్నర్ రాష్ట్రానికి రాజ్యాంగపరమైన అధిపతి — ఇద్దరూ nominal heads. / Both are constitutional (nominal) heads — President for Union, Governor for State."),

    (6, "hard",
     "గవర్నర్ ఎన్నికలో రాష్ట్రపతి ఎన్నికకు ఉన్న 'ఎలక్టోరల్ కాలేజ్' వ్యవస్థ ఉందా? / Is there an 'Electoral College' for Governor's appointment like for President?",
     "అవును, MLAs ఎన్నుకుంటారు / Yes, elected by MLAs",
     "అవును, MPs & MLAs ఎన్నుకుంటారు / Yes, MPs and MLAs",
     "లేదు, రాష్ట్రపతి నేరుగా నియమిస్తారు / No, directly appointed by President",
     "అవును, రాష్ట్ర శాసనసభ ఎన్నుకుంటుంది / Yes, elected by state legislature",
     "c",
     "గవర్నర్‌కు ఎన్నికలు ఉండవు — రాష్ట్రపతి నేరుగా నియమిస్తారు. రాష్ట్రపతికి Electoral College ఉంటుంది. / No elections for Governor — President directly appoints. President has Electoral College."),

    (6, "medium",
     "రాష్ట్రపతి Art.72 కింద మరణ శిక్ష మాఫీ చేయగలరు — గవర్నర్ Art.161 కింద చేయగలరా? / Can Governor pardon death sentence under Art.161?",
     "అవును / Yes",
     "లేదు / No",
     "కేవలం రాష్ట్ర చట్టాలకు సంబంధించినవి మాత్రమే / Only state law offences",
     "రాష్ట్రపతి అనుమతితో / With Presidential sanction",
     "b",
     "తేడా: రాష్ట్రపతి Art.72 కింద మరణ శిక్ష మాఫీ చేయగలరు; గవర్నర్ Art.161 కింద ఈ అధికారం లేదు. / Difference: President (Art.72) can pardon death sentence; Governor (Art.161) cannot."),

    (6, "medium",
     "గవర్నర్‌కు 'వీటో' అధికారాలు రాష్ట్రపతికి పోలితే ఎలా ఉంటాయి? / How do Governor's veto powers compare with President's?",
     "గవర్నర్ అధికారాలు ఎక్కువ / Governor has more powers",
     "రాష్ట్రపతి అధికారాలు ఎక్కువ / President has more powers",
     "రెండూ సమానం / Both equal",
     "గవర్నర్‌కు వీటో లేదు / Governor has no veto",
     "b",
     "రాష్ట్రపతికి Pocket Veto ఉంది; గవర్నర్‌కు లేదు (రాష్ట్రపతి నివేదించాలి). రాష్ట్రపతి అన్ని రకాల బిల్లులు వీటో చేయగలరు. / President has Pocket Veto; Governor doesn't — must report to President. President has broader veto."),

    (6, "hard",
     "గవర్నర్ 'రాష్ట్రపతి ఏజెంట్' గా పని చేసే విధి ఏ అనుచ్ఛేదంలో? / In which Article Governor acts as 'agent of President'?",
     "అనుచ్ఛేదం 155 / Art.155",
     "అనుచ్ఛేదం 239 / Art.239",
     "అనుచ్ఛేదం 200 / Art.200",
     "రాజ్యాంగంలో ప్రత్యేకంగా పేర్కొనబడలేదు / Not explicitly mentioned",
     "d",
     "రాజ్యాంగంలో 'agent' పదం లేదు — 'dual role' (రాష్ట్ర రాజ్యాంగ అధిపతి + కేంద్ర ప్రతినిధి) సూత్రం ఆచారం మరియు వ్యాఖ్యాన ఆధారంగా. / Constitution doesn't use 'agent'; Governor's dual role as state head + Centre's representative is based on convention and interpretation."),

    (6, "easy",
     "రాష్ట్రపతి ఎన్నికలో రాష్ట్రాల శాసనసభ సభ్యులు పాల్గొంటారు — గవర్నర్ నియామకంలో ఎవరు పాల్గొంటారు? / MLAs participate in Presidential election — who decides Governor's appointment?",
     "MLAs & MPs / ఎమ్మెల్యేలు & ఎంపీలు",
     "రాష్ట్రపతి మాత్రమే / President alone",
     "పార్లమెంటు ఉభయ సభలు / Both Houses of Parliament",
     "PM సిఫారసు అవసరం తప్పనిసరి / PM recommendation mandatory",
     "b",
     "గవర్నర్ నియామకం రాష్ట్రపతి ప్రత్యేక హక్కు. ఆచారంలో PM సలహాపై నియమిస్తారు. / Governor's appointment is President's prerogative; in practice on PM's advice."),

    (6, "medium",
     "రాష్ట్రపతి మరియు గవర్నర్ ఇద్దరూ 'రాజ్యాంగ అధిపతులు' — కానీ ఒక ముఖ్యమైన తేడా ఏమిటి? / President and Governor are both nominal heads — what is one key difference?",
     "రాష్ట్రపతి ఎన్నుకోబడతారు; గవర్నర్ నియమించబడతారు / President is elected; Governor is appointed",
     "గవర్నర్ ఎక్కువ అధికారాలు కలిగి ఉంటారు / Governor has more powers",
     "రాష్ట్రపతి పదవీకాలం 4 సంవత్సరాలు; గవర్నర్ 5 సంవత్సరాలు / President 4 years; Governor 5",
     "గవర్నర్ ను SC అభిశంసించగలదు / SC can impeach Governor",
     "a",
     "రాష్ట్రపతి ఎన్నుకోబడతారు (Art.54 — Electoral College); గవర్నర్ రాష్ట్రపతి చేత నియమించబడతారు (Art.155). రాష్ట్రపతి 5 సంవత్సరాలు; గవర్నర్ 5 సంవత్సరాలు (కానీ రాష్ట్రపతి ఇష్టం వరకు). / President is elected via Electoral College (Art.54); Governor appointed by President (Art.155). Both 5-year terms but Governor serves 'at pleasure' of President."),

    (6, "hard",
     "గవర్నర్ వ్యక్తిగత విచక్షణతో (personally) ఉపయోగించే అధికారాలు మంత్రులు సలహా అవసరం లేదు — ఇది ఏ సూత్రం? / Governor using personal discretion without CoM advice follows which principle?",
     "రాజ్యాంగపరమైన ఆచారం / Constitutional convention only",
     "Art.163(1) — రాజ్యాంగం గవర్నర్ విచక్షణకు ప్రత్యేకంగా నిర్ణయించిన సందర్భాల్లో సలహా అవసరం లేదు / Art.163(1) — in functions where Constitution specifically requires Governor to act in discretion",
     "Art.154 — అన్నింటిలో గవర్నర్ స్వతంత్రుడు / Art.154 — Governor is independent in everything",
     "Art.200 — గవర్నర్ అన్ని బిల్లులను విచక్షణతో నిర్ణయించవచ్చు / Art.200 — Governor can decide all bills by discretion",
     "b",
     "Art.163(1): రాజ్యాంగం గవర్నర్ విచక్షణ ప్రకారం పనిచేయవలసిందని నిర్ణయించిన కార్యకలాపాల్లో మాత్రమే — CoM సలహా అవసరం లేదు. మిగతా అన్ని కార్యాలలో CoM సలహాపై వ్యవహరించాలి. / Art.163(1): Governor acts on CoM advice EXCEPT in functions where Constitution requires him to act in his discretion."),

    # ── Section 7: Miscellaneous ────────────────────────────────────────────────
    (7, "easy",
     "గవర్నర్ ప్రమాణ స్వీకారం ఏ షెడ్యూల్‌లో ఉంటుంది? / Governor's oath is in which Schedule?",
     "మొదటి షెడ్యూల్ / First Schedule",
     "మూడో షెడ్యూల్ / Third Schedule",
     "నాల్గో షెడ్యూల్ / Fourth Schedule",
     "ఐదో షెడ్యూల్ / Fifth Schedule",
     "b",
     "తృతీయ షెడ్యూల్ (Third Schedule): గవర్నర్ ప్రమాణ పత్రం ఇందులో ఉంటుంది. / Third Schedule: contains Governor's oath form."),

    (7, "medium",
     "రాష్ట్ర శాసనసభ కింది సభ (Vidhan Sabha) సభ్యులను నామినేట్ చేసే అధికారం గవర్నర్‌కు ఉందా? / Can Governor nominate members to Vidhan Sabha (lower house)?",
     "అవును, 12 మంది / Yes, 12 members",
     "అవును, ఆంగ్లో-ఇండియన్ కమ్యూనిటీకి 1 మంది (రద్దు వరకు) / Yes, 1 Anglo-Indian (until abolished)",
     "లేదు / No",
     "అవును, 6 మంది / Yes, 6 members",
     "b",
     "అనుచ్ఛేదం 333: గవర్నర్ Vidhan Sabha కి ఒక ఆంగ్లో-ఇండియన్‌ను నామినేట్ చేయవచ్చు (104వ సవరణ 2020 ద్వారా రద్దయింది). / Art.333: Governor could nominate one Anglo-Indian to Vidhan Sabha — abolished by 104th Amendment 2020."),

    (7, "hard",
     "గవర్నర్ రాష్ట్ర శాసనసభ సమావేశానికి ముందు ప్రత్యేక ప్రసంగం చేసే అనుచ్ఛేదం ఏది? / Which Article requires Governor to address legislature at the start?",
     "అనుచ్ఛేదం 176 / Art.176",
     "అనుచ్ఛేదం 174 / Art.174",
     "అనుచ్ఛేదం 177 / Art.177",
     "అనుచ్ఛేదం 172 / Art.172",
     "a",
     "అనుచ్ఛేదం 176: గవర్నర్ ప్రతి సంవత్సరం మొదటి సమావేశంలో మరియు సాధారణ ఎన్నికల తర్వాత శాసనసభ/పరిషత్ ఉభయ సభలను ఉద్దేశించి ప్రసంగిస్తారు. / Art.176: Governor addresses legislature at the first session each year and after general elections."),

    (7, "easy",
     "రాష్ట్ర గవర్నర్ అధికారిక నివాసాన్ని ఏమని పిలుస్తారు? / What is the official residence of a State Governor called?",
     "రాష్ట్రపతి భవన్ / Rashtrapati Bhavan",
     "రాజ్‌భవన్ / Raj Bhavan",
     "గవర్నర్ హౌస్ / Governor House",
     "రాజ గేహం / Raja Geham",
     "b",
     "రాష్ట్ర గవర్నర్ అధికారిక నివాసాన్ని రాజ్‌భవన్ (Raj Bhavan) అని పిలుస్తారు. / Official residence of State Governor is called Raj Bhavan."),

    (7, "medium",
     "గవర్నర్ అధికారిక జీతం & భత్యాలు ఏ నిధి నుండి ఇస్తారు? / Governor's salary and allowances are charged to which fund?",
     "కేంద్ర ఏకీకృత నిధి / Consolidated Fund of India",
     "రాష్ట్ర ఏకీకృత నిధి / Consolidated Fund of State",
     "ఆకస్మిక నిధి / Contingency Fund",
     "ప్రజా ఖాతా / Public Account",
     "b",
     "అనుచ్ఛేదం 158(3): గవర్నర్ జీతాలు రాష్ట్ర ఏకీకృత నిధి (Consolidated Fund of State) నుండి ఇవ్వబడతాయి. / Art.158(3): Governor's emoluments charged to the Consolidated Fund of the State."),

    (7, "hard",
     "గవర్నర్ పదవిలో ఉన్నప్పుడు ఏ రక్షణ ఉంటుంది? / What protection does Governor have while in office?",
     "పదవి మారిన తర్వాత మాత్రమే కేసులు దాఖలు / Cases only after leaving office",
     "పదవిలో ఉండగా పూర్తి రక్షణ — సివిల్ & క్రిమినల్ కేసులు దాఖలు కాదు / Full immunity while in office — no civil or criminal cases",
     "కేవలం సివిల్ కేసుల నుండి రక్షణ / Only from civil cases",
     "ఎలాంటి రక్షణ లేదు / No immunity",
     "b",
     "అనుచ్ఛేదం 361: గవర్నర్ పదవిలో ఉండగా ఏ కోర్టులో నేరారోపణలు చేయలేరు (సివిల్ & క్రిమినల్). / Art.361: Governor has immunity — no criminal proceedings during term; civil case notice required."),

    (7, "medium",
     "గవర్నర్ అసెంబ్లీ సమావేశాలు ఏర్పాటు చేయడం/వాయిదా వేయడానికి అనుచ్ఛేదం ఏది? / Art. for Governor summoning/proroguing Assembly?",
     "అనుచ్ఛేదం 174 / Art.174",
     "అనుచ్ఛేదం 175 / Art.175",
     "అనుచ్ఛేదం 176 / Art.176",
     "అనుచ్ఛేదం 177 / Art.177",
     "a",
     "అనుచ్ఛేదం 174: గవర్నర్ రాష్ట్ర శాసనసభ సమావేశాలు ఏర్పాటు చేయడం, వాయిదా వేయడం, లోక్‌సభ రద్దు చేయడం. రెండు సమావేశాల మధ్య 6 నెలలు మించరాదు. / Art.174: Governor summons, prorogues the state legislature and dissolves the Assembly. Gap between sessions ≤ 6 months."),

    (7, "hard",
     "రాష్ట్రపతి 'రాష్ట్రపతి పాలన' (Art.356) కింద రాష్ట్ర అసెంబ్లీని రద్దు చేయవచ్చు — ఇందుకు ఏ ప్రాతిపదికన? / President can dissolve State Assembly under Art.356 — on what basis?",
     "ప్రధానమంత్రి నిర్ణయం మేరకు / On PM's decision alone",
     "గవర్నర్ నివేదిక లేదా ఇతర విధంగా రాజ్యాంగ యంత్రం విఫలమైన విషయం తెలిసినప్పుడు / On Governor's report or otherwise that constitutional machinery has failed",
     "రాజ్యసభ తీర్మానం తర్వాత / After RS resolution",
     "SC సలహా మేరకు / On SC advice",
     "b",
     "Art.356: రాష్ట్ర గవర్నర్ నివేదిక ఆధారంగా లేదా ఇతర విధంగా రాష్ట్రంలో రాజ్యాంగ ప్రభుత్వం నడపడం సాధ్యం కాదని రాష్ట్రపతికి నిర్ధారణ అయినపుడు President's Rule విధించవచ్చు. / Art.356: President may proclaim on Governor's report or otherwise if convinced that government cannot be carried on in accordance with Constitution."),
]


def _seed_polity_ch18_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
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


def _seed_polity_ch18_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
