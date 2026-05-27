# seed_polity_ch20.py
# Chapter 20 — Supreme Court of India
# Total Sections: 8 | Total MCQs: 64 | PYQs: 6
# Sections:
#   0 — Establishment & Composition (8 MCQs)
#   1 — Appointment & Removal of Judges (8 MCQs)
#   2 — Original Jurisdiction (8 MCQs)
#   3 — Appellate Jurisdiction & SLP (8 MCQs)
#   4 — Advisory Jurisdiction & Writ Jurisdiction (8 MCQs)
#   5 — Law of the Land — Art.141 & Precedent (8 MCQs)
#   6 — Collegium System & Judicial Independence (8 MCQs)
#   7 — Miscellaneous / Key Articles (8 MCQs)

_CH = 20
_SUBJECT = 'GK'
_TOPIC   = 'Indian_Polity'
_TITLE_TE = 'భారత సర్వోన్నత న్యాయస్థానం'
_TITLE_EN = 'Supreme Court of India'
_PAGES    = 'Ch.20 (Lakshmikanth)'

_SECTIONS = [
    "స్థాపన & కూర్పు",
    "న్యాయమూర్తుల నియామకం & తొలగింపు",
    "మూల అధికార పరిధి",
    "అప్పీలేట్ అధికార పరిధి & SLP",
    "సలహా & రిట్ అధికార పరిధి",
    "అనుచ్ఛేదం 141 & న్యాయ శాసనం",
    "కొలీజియం వ్యవస్థ & న్యాయ స్వాతంత్ర్యం",
    "విభిన్న కీలక అనుచ్ఛేదాలు",
]

_MCQS = [
    # ── Section 0: Establishment & Composition ─────────────────────────────────
    (0, "easy",
     "సర్వోన్నత న్యాయస్థానం స్థాపనను ప్రస్తావించే అనుచ్ఛేదం ఏది? / Which Article establishes the Supreme Court?",
     "అనుచ్ఛేదం 121 / Art.121",
     "అనుచ్ఛేదం 124 / Art.124",
     "అనుచ్ఛేదం 143 / Art.143",
     "అనుచ్ఛేదం 148 / Art.148",
     "b",
     "అనుచ్ఛేదం 124: 'భారతదేశంలో భారత సర్వోన్నత న్యాయస్థానం అనే ఒక న్యాయస్థానం ఉండాలి'. / Art.124: 'There shall be a Supreme Court of India consisting of a Chief Justice of India…'"),

    (0, "easy",
     "సర్వోన్నత న్యాయస్థానం ప్రారంభంలో ఎంత మంది న్యాయమూర్తులతో ప్రారంభమైంది? / How many judges did the Supreme Court originally have (1950)?",
     "7 (CJI + 6)",
     "8 (CJI + 7)",
     "11 (CJI + 10)",
     "26 (CJI + 25)",
     "b",
     "1950లో SC లో CJI + 7 న్యాయమూర్తులు ఉండేవారు. ప్రస్తుతం CJI + 33 (మొత్తం 34). / Originally CJI + 7 = 8. Current strength: CJI + 33 = 34 (increased over time by Parliament)."),

    (0, "medium",
     "సర్వోన్నత న్యాయస్థానం ప్రస్తుత న్యాయమూర్తుల సంఖ్య ఎంత? / What is the current sanctioned strength of the Supreme Court?",
     "25",
     "28",
     "34",
     "31",
     "c",
     "ప్రస్తుతం SC లో CJI + 33 న్యాయమూర్తులు మొత్తం 34 (Supreme Court (Number of Judges) Amendment Act 2019). / Currently 34 judges (CJI + 33), sanctioned by the 2019 Amendment."),

    (0, "easy",
     "సర్వోన్నత న్యాయస్థాన న్యాయమూర్తుల పదవీ విరమణ వయస్సు ఎంత? / What is the retirement age of SC judges?",
     "60 సంవత్సరాలు / 60 years",
     "62 సంవత్సరాలు / 62 years",
     "65 సంవత్సరాలు / 65 years",
     "70 సంవత్సరాలు / 70 years",
     "c",
     "SC న్యాయమూర్తులు 65 సంవత్సరాల వయస్సులో పదవీ విరమణ చేస్తారు (Art.124(2)). హైకోర్టు న్యాయమూర్తులు 62 సంవత్సరాలకు. / SC judges retire at 65 (Art.124(2)). HC judges retire at 62."),

    (0, "medium",
     "సర్వోన్నత న్యాయస్థానం సీటు ఎక్కడ ఉంది? / Where is the seat of the Supreme Court?",
     "ముంబై / Mumbai",
     "కోల్కతా / Kolkata",
     "నూతన ఢిల్లీ / New Delhi",
     "చెన్నై / Chennai",
     "c",
     "భారత సర్వోన్నత న్యాయస్థానం ఢిల్లీలో ఉంది (Art.130). అయితే CJI అనుమతితో ఇతర చోట్ల కూర్చోవచ్చు. / SC sits in Delhi (Art.130). CJI may appoint other places with President's approval."),

    (0, "medium",
     "సర్వోన్నత న్యాయస్థానం న్యాయమూర్తిగా నియమించబడాలంటే కనీసం ఎంత కాలం హైకోర్టు న్యాయమూర్తిగా పనిచేసి ఉండాలి? / Minimum HC judge experience to qualify for SC?",
     "3 సంవత్సరాలు / 3 years",
     "5 సంవత్సరాలు / 5 years",
     "10 సంవత్సరాలు / 10 years",
     "15 సంవత్సరాలు / 15 years",
     "b",
     "Art.124(3): SC న్యాయమూర్తిగా నియమించబడాలంటే కనీసం 5 సంవత్సరాలు హైకోర్టు న్యాయమూర్తిగా లేదా 10 సంవత్సరాలు HC అడ్వకేట్‌గా పనిచేసి ఉండాలి. / Art.124(3): Must be HC judge for 5 years OR HC advocate for 10 years OR distinguished jurist."),

    (0, "medium",
     "సర్వోన్నత న్యాయస్థాన న్యాయమూర్తి ప్రమాణ స్వీకారం ఎవరి ముందు జరుగుతుంది? / Before whom does an SC judge take oath?",
     "ప్రధాన న్యాయమూర్తి / Chief Justice of India",
     "రాష్ట్రపతి / President of India",
     "ఉపరాష్ట్రపతి / Vice President",
     "స్పీకర్ / Speaker of Lok Sabha",
     "b",
     "Art.124(6): SC న్యాయమూర్తి రాష్ట్రపతి ముందు ప్రమాణ స్వీకారం చేస్తాడు. / SC judge takes oath before the President of India (Art.124(6))."),

    (0, "hard",
     "Ad hoc judge అంటే ఎవరు? / What is an ad hoc judge of the Supreme Court?",
     "పదవీ విరమణ చేసిన SC న్యాయమూర్తి / Retired SC judge",
     "కోరం లేనప్పుడు CJI నియమించే HC న్యాయమూర్తి / HC judge appointed by CJI when quorum lacks",
     "అంతర్జాతీయ న్యాయమూర్తి / International judge",
     "న్యాయ విచారణ కమిషన్ న్యాయమూర్తి / Inquiry commission judge",
     "b",
     "Art.127: కోరం లేనప్పుడు CJI రాష్ట్రపతి అనుమతితో HC న్యాయమూర్తిని 'ad hoc judge'గా నియమించవచ్చు. / Art.127: When quorum lacks, CJI with President's consent may appoint HC judge as ad hoc judge of SC."),

    # ── Section 1: Appointment & Removal ──────────────────────────────────────
    (1, "easy",
     "సర్వోన్నత న్యాయస్థాన న్యాయమూర్తిని ఎవరు నియమిస్తారు? / Who appoints SC judges?",
     "ప్రధానమంత్రి / Prime Minister",
     "ప్రధాన న్యాయమూర్తి / Chief Justice of India",
     "రాష్ట్రపతి / President of India",
     "పార్లమెంట్ / Parliament",
     "c",
     "Art.124(2): SC న్యాయమూర్తులను రాష్ట్రపతి నియమిస్తారు. నియమించేటప్పుడు SC మరియు HC న్యాయమూర్తులను సంప్రదిస్తారు. / Art.124(2): SC judges appointed by President after consultation with SC and HC judges as deemed necessary."),

    (1, "medium",
     "సర్వోన్నత న్యాయస్థాన న్యాయమూర్తిని తొలగించే విధానం ఏమిటి? / How can an SC judge be removed?",
     "రాష్ట్రపతి ఉత్తర్వు మాత్రమే / President's order alone",
     "పార్లమెంట్ సాధారణ మెజారిటీ / Parliament simple majority",
     "పార్లమెంట్ ప్రత్యేక మెజారిటీ + రాష్ట్రపతి ఆదేశం / Special majority + President's order",
     "సుప్రీం కోర్ట్ జడ్జిమెంట్ / SC judgment",
     "c",
     "Art.124(4): Proved misbehaviour లేదా incapacity పై పార్లమెంట్ ప్రత్యేక మెజారిటీ (సభ మొత్తం సభ్యుల మెజారిటీ + హాజరైన 2/3 మెజారిటీ) + రాష్ట్రపతి ఆదేశంతో తొలగించవచ్చు. / Art.124(4): Removal on grounds of proved misbehaviour or incapacity — address by each House with special majority + President's order."),

    (1, "medium",
     "SC న్యాయమూర్తుల జీతాలు ఏ నిధి నుండి చెల్లిస్తారు? / SC judges' salaries are charged to?",
     "భారత ఏకీకృత నిధి / Consolidated Fund of India",
     "ఆకస్మిక నిధి / Contingency Fund",
     "పబ్లిక్ అకౌంట్ / Public Account",
     "భారత్ నిర్మాణ నిధి / Bharat Nirmaan Fund",
     "a",
     "SC న్యాయమూర్తుల జీతాలు భారత ఏకీకృత నిధి (Consolidated Fund of India) నుండి చెల్లిస్తారు — ఇది వారి స్వాతంత్ర్యాన్ని కాపాడుతుంది. / SC judges' salaries charged to CFI (Art.125) — ensures judicial independence."),

    (1, "medium",
     "పదవీ విరమణ తర్వాత SC న్యాయమూర్తి ఏ కోర్టులో వాదించవచ్చు? / Where can a retired SC judge practice after retirement?",
     "ఏ కోర్టులో అయినా / Any court",
     "ఏ కోర్టులో అయినా రాష్ట్రపతి అనుమతితో / Any court with President's approval",
     "ఏ కోర్టులో అయినా కాదు / No court at all",
     "కేవలం ట్రిబ్యునల్స్‌లో / Only tribunals",
     "c",
     "Art.124(7): SC న్యాయమూర్తి పదవీ విరమణ తర్వాత భారతదేశంలో ఏ కోర్టులో అయినా వాదించడం నిషేధం. / Art.124(7): Retired SC judge cannot plead or act in any court or authority in India."),

    (1, "hard",
     "Judges (Inquiry) Act, 1968 ఏ విషయంలో వర్తిస్తుంది? / The Judges (Inquiry) Act 1968 relates to?",
     "న్యాయమూర్తుల నియామకం / Appointment of judges",
     "SC న్యాయమూర్తి తొలగింపు విచారణ విధానం / Procedure for removal of SC judge",
     "హైకోర్టు ఏర్పాటు / Establishment of HC",
     "న్యాయమూర్తుల జీతాల నిర్ణయం / Determination of judges' salaries",
     "b",
     "Judges (Inquiry) Act, 1968: SC/ HC న్యాయమూర్తి తొలగింపు విచారణ విధానాన్ని నిర్దేశిస్తుంది. 3 సభ్యుల కమిటీ ఏర్పాటు: CJI నామినీ, HC CJ,著名 న్యాయవాది. / Judges (Inquiry) Act 1968 lays down the procedure for removal of SC/HC judges — 3-member committee investigates."),

    (1, "medium",
     "సర్వోన్నత న్యాయస్థాన ప్రధాన న్యాయమూర్తి (CJI) నియామకం ఎలా జరుగుతుంది? / How is the CJI appointed?",
     "సీనియారిటీ ఆధారంగా మాత్రమే / By seniority alone",
     "ప్రధానమంత్రి సిఫారసు / PM's recommendation",
     "కొలీజియం సిఫారసుపై రాష్ట్రపతి నియమిస్తారు / President on collegium recommendation",
     "పార్లమెంట్ ఎన్నిక / Parliament election",
     "c",
     "రాష్ట్రపతి SC కొలీజియం సిఫారసుపై CJIని నియమిస్తారు. ఆచారప్రకారం అత్యంత సీనియర్ SC జడ్జి CJI అవుతారు. / President appoints CJI on collegium recommendation; by convention the seniormost SC judge is appointed CJI."),

    (1, "hard",
     "SC న్యాయమూర్తి తొలగింపుకు సంబంధించిన మొదటి తీర్మానం ఏ సంవత్సరంలో పార్లమెంట్‌లో ప్రవేశపెట్టారు? / When was the first impeachment motion against an SC judge moved?",
     "1965",
     "1978",
     "1991",
     "2004",
     "c",
     "1991లో Justice V. Ramaswami పై తొలిసారి తొలగింపు తీర్మానం ప్రవేశపెట్టారు — ఆ తీర్మానం వీగిపోయింది (Lok Sabha failed to pass). / First removal motion moved against Justice V. Ramaswami in 1991; it failed in Lok Sabha."),

    (1, "medium",
     "SC న్యాయమూర్తి తొలగింపు విచారణ 3 సభ్యుల కమిటీ సభ్యులు ఎవరు? / Who are the 3 members of the inquiry committee for SC judge removal?",
     "CJI, Attorney General, CEC / CJI, అటార్నీ జనరల్, CEC",
     "CJI నామినీ, HC CJ,著名 న్యాయవాది / CJI nominee, HC Chief Justice, distinguished jurist",
     "3 మంది SC న్యాయమూర్తులు / 3 SC judges",
     "CAG, AG, Solicitor General",
     "b",
     "Judges Inquiry Act 1968: 3-సభ్య కమిటీ = (1) CJI నియమించే SC న్యాయమూర్తి లేదా HC CJ + (2) HC CJ + (3)著名 న్యాయవాది. / Under Judges Inquiry Act: committee = SC judge/HC CJ nominated by CJI + another HC CJ + a distinguished jurist."),

    # ── Section 2: Original Jurisdiction ──────────────────────────────────────
    (2, "easy",
     "సర్వోన్నత న్యాయస్థానం మూల అధికార పరిధి (Original Jurisdiction) గురించి ఏ అనుచ్ఛేదం? / Which Article deals with original jurisdiction of SC?",
     "అనుచ్ఛేదం 131 / Art.131",
     "అనుచ్ఛేదం 132 / Art.132",
     "అనుచ్ఛేదం 136 / Art.136",
     "అనుచ్ఛేదం 143 / Art.143",
     "a",
     "Art.131: SC మూల అధికార పరిధి — రాష్ట్రాల మధ్య, రాష్ట్ర-కేంద్ర వివాదాలు. / Art.131: Original jurisdiction of SC — disputes between states or between state and Centre."),

    (2, "medium",
     "Art.131 కింద సర్వోన్నత న్యాయస్థానానికి ప్రత్యేక అధికార పరిధి ఎలాంటి వివాదాలపై? / Art.131 gives exclusive original jurisdiction over?",
     "వ్యక్తులు మరియు కేంద్ర ప్రభుత్వం మధ్య / Between individuals and Centre",
     "రెండు లేదా అంతకు మించిన రాష్ట్రాల మధ్య / Between two or more states",
     "కార్పొరేట్ వివాదాలు / Corporate disputes",
     "పేటెంట్ వివాదాలు / Patent disputes",
     "b",
     "Art.131: రెండు లేదు అంతకంటే ఎక్కువ రాష్ట్రాల మధ్య వివాదాలపై SC కి ప్రత్యేక మూల అధికార పరిధి ఉంది; రాష్ట్రం మరియు కేంద్రం మధ్య కూడా. / Art.131 exclusive original jurisdiction: interstate disputes or state vs Centre (on legal rights)."),

    (2, "medium",
     "రాష్ట్రాల మధ్య నదీ జల వివాదాలు (River water disputes) SC Art.131 కింద వస్తాయా? / Do river water disputes between states fall under Art.131?",
     "అవును, ఎల్లప్పుడూ / Yes, always",
     "కాదు, Inter-State Water Disputes Act 1956 కింద ట్రిబ్యునల్ / No — Water Disputes Act 1956 Tribunal",
     "కాదు, రాష్ట్రపతి నిర్ణయిస్తారు / No — President decides",
     "అవును, కేవలం AP మరియు తెలంగాణకు / Yes, only for AP and Telangana",
     "b",
     "Inter-State Water Disputes Act 1956 కింద ఇటువంటి వివాదాలు SC Art.131 నుండి మినహాయించబడ్డాయి — ట్రిబ్యునల్‌కు వెళ్తాయి. / River water disputes between states are excluded from Art.131 — adjudicated by tribunal under Inter-State Water Disputes Act 1956."),

    (2, "easy",
     "ప్రాథమిక హక్కుల ఉల్లంఘనపై సర్వోన్నత న్యాయస్థానంలో నేరుగా విజ్ఞప్తి చేయడానికి ఏ అనుచ్ఛేదం అనుమతిస్తుంది? / Which Article allows direct petition to SC for enforcement of Fundamental Rights?",
     "అనుచ్ఛేదం 226 / Art.226",
     "అనుచ్ఛేదం 32 / Art.32",
     "అనుచ్ఛేదం 131 / Art.131",
     "అనుచ్ఛేదం 143 / Art.143",
     "b",
     "Art.32: ప్రాథమిక హక్కుల అమలు కోసం SC కి నేరుగా వెళ్ళవచ్చు — Dr. Ambedkar దీన్ని 'Constitution యొక్క హృదయం మరియు ఆత్మ' అన్నారు. / Art.32: Right to move SC for enforcement of FRs — called 'heart and soul of the Constitution' by Ambedkar."),

    (2, "hard",
     "రాష్ట్రపతి ఎన్నిక వివాదాలు ఏ కోర్టు పరిశీలిస్తుంది? / Which court adjudicates disputes regarding President's election?",
     "హైకోర్టు / High Court",
     "ఎన్నికల ట్రిబ్యునల్ / Election Tribunal",
     "సర్వోన్నత న్యాయస్థానం / Supreme Court",
     "పార్లమెంట్ / Parliament",
     "c",
     "Art.71: రాష్ట్రపతి మరియు ఉపరాష్ట్రపతి ఎన్నికలకు సంబంధించిన వివాదాలను SC విచారిస్తుంది. / Art.71: Disputes relating to election of President and VP are inquired into by SC."),

    (2, "medium",
     "రాష్ట్రాల మధ్య వివాదాలలో SC మూల అధికార పరిధి కింద స్థాపించబడాల్సిన వివాద స్వభావం ఏది? / What nature of dispute must be shown for Art.131 original jurisdiction?",
     "ఏదైనా వివాదం / Any dispute",
     "చట్టబద్ధ హక్కుల వివాదం / Dispute involving legal right",
     "నైతిక వివాదం / Moral dispute",
     "ఆర్థిక వివాదం / Financial dispute",
     "b",
     "Art.131: వివాదం అనేది 'చట్టబద్ధ హక్కుల' (legal rights) విషయంలో ఉండాలి. సాధారణ రాజకీయ వివాదాలు లేదా ఆర్థిక ఫిర్యాదులు కావు. / Art.131: Only disputes involving legal rights (not political/policy matters) qualify."),

    (2, "medium",
     "రాష్ట్రపతి Reference అంటే ఏమిటి? ఏ అనుచ్ఛేదం? / What is President's Reference under which Article?",
     "Art.131 — మూల అధికార పరిధి",
     "Art.143 — సలహా అధికార పరిధి",
     "Art.32 — రిట్ అధికార పరిధి",
     "Art.136 — SLP",
     "b",
     "Art.143: రాష్ట్రపతి SC అభిప్రాయాన్ని కోరవచ్చు ('Reference'). SC అభిప్రాయం ఇవ్వొచ్చు కానీ రాష్ట్రపతిపై బైండింగ్ కాదు. / Art.143: President can refer questions of law/fact to SC for advisory opinion; SC may give opinion but it's not binding."),

    (2, "hard",
     "Art.131 కింద వివాదంలో ఏ విషయాలు మినహాయించబడ్డాయి? / Which matters are excluded from Art.131?",
     "కేంద్ర-రాష్ట్ర పన్ను వివాదాలు / Centre-state tax disputes",
     "రాష్ట్రాల మధ్య నదీ జలాలు + Treaty/Agreement వివాదాలు / River water + treaty disputes",
     "నేర విషయాలు / Criminal matters",
     "ప్రాథమిక హక్కులు / Fundamental Rights",
     "b",
     "Art.131 నుండి మినహాయింపు: (1) రాష్ట్రాల మధ్య నదీ జల వివాదాలు (ప్రత్యేక చట్టం ఉంది), (2) Treaty లేదా అంతర్జాతీయ ఒప్పందానికి సంబంధించిన వివాదాలు. / Art.131 exclusions: river water disputes (special Act) and treaty/agreement disputes."),

    # ── Section 3: Appellate Jurisdiction & SLP ───────────────────────────────
    (3, "easy",
     "స్పెషల్ లీవ్ పిటిషన్ (SLP) ఏ అనుచ్ఛేదం కింద దాఖలు చేస్తారు? / Under which Article is an SLP filed?",
     "అనుచ్ఛేదం 132 / Art.132",
     "అనుచ్ఛేదం 134 / Art.134",
     "అనుచ్ఛేదం 136 / Art.136",
     "అనుచ్ఛేదం 137 / Art.137",
     "c",
     "Art.136: SLP (Special Leave to Appeal) — ఏ కోర్టు లేదా ట్రిబ్యునల్ తీర్పుపై SC అనుమతితో అప్పీల్ చేసుకోవచ్చు. / Art.136: SC may, in its discretion, grant SLP from any judgment of any court or tribunal."),

    (3, "medium",
     "రాజ్యాంగ అర్థంలో చట్టపరమైన ప్రశ్న ఉంటే అప్పీలేట్ అధికార పరిధి ఏ అనుచ్ఛేదం? / Appellate jurisdiction for constitutional questions?",
     "Art.132",
     "Art.133",
     "Art.134",
     "Art.135",
     "a",
     "Art.132: HC తీర్పు నుండి రాజ్యాంగ ప్రశ్నపై SC కి అప్పీల్ చేసుకోవచ్చు (HC సర్టిఫికేట్‌తో). / Art.132: Appeal from HC judgment involving substantial question of constitutional law (with HC certificate)."),

    (3, "medium",
     "సివిల్ విషయాలలో అప్పీలేట్ అధికార పరిధి ఏ అనుచ్ఛేదం? / Appellate jurisdiction in civil matters?",
     "Art.132",
     "Art.133",
     "Art.134",
     "Art.136",
     "b",
     "Art.133: HC తీర్పు నుండి సివిల్ విషయాలలో SC కి అప్పీల్ (HC యొక్క సర్టిఫికేట్‌తో, రాజ్యాంగ ప్రశ్న ఉంటే). / Art.133: Appeal to SC in civil matters from HC with HC certificate (substantial question of law)."),

    (3, "medium",
     "నేర (Criminal) విషయాలలో SC అప్పీలేట్ అధికార పరిధి ఏ అనుచ్ఛేదం? / Appellate jurisdiction in criminal matters?",
     "Art.132",
     "Art.133",
     "Art.134",
     "Art.136",
     "c",
     "Art.134: నేర విషయాలలో HC నిర్ణయం నుండి SC కి అప్పీల్ — మరణశిక్ష ధృవీకరించినపుడు లేదా మరణశిక్ష విధించినపుడు. / Art.134: SC has appellate jurisdiction in criminal matters — when HC confirms death sentence or reverses acquittal and awards death."),

    (3, "easy",
     "Art.136 (SLP) కింద ఏ కోర్టుల తీర్పులపై అప్పీల్ చేయవచ్చు? / SLP under Art.136 lies against?",
     "కేవలం HC తీర్పులు / Only HC judgments",
     "కేవలం ట్రిబ్యునల్స్ / Only tribunals",
     "ఏ కోర్టు లేదా ట్రిబ్యునల్ తీర్పు అయినా / Any court or tribunal in India",
     "కేవలం జిల్లా కోర్టులు / Only district courts",
     "c",
     "Art.136: SLP ఏ కోర్టు లేదా ట్రిబ్యునల్ తీర్పుపై అయినా SC కి దాఖలు చేయవచ్చు (military tribunals మినహా). / Art.136: SLP can be filed against any court or tribunal (except military tribunals) — SC has discretion to admit or reject."),

    (3, "hard",
     "SC తన స్వంత తీర్పును సమీక్షించే అధికారం ఏ అనుచ్ఛేదం? / SC's power to review its own judgment?",
     "Art.136",
     "Art.137",
     "Art.141",
     "Art.143",
     "b",
     "Art.137: SC తన స్వంత తీర్పు లేదా ఆదేశాన్ని సమీక్షించవచ్చు (Review Petition). / Art.137: SC has power to review any judgment or order made by it, subject to law made by Parliament or rules."),

    (3, "medium",
     "SC అప్పీలేట్ అధికార పరిధి యొక్క విస్తృత స్వభావాన్ని ఏ నిబంధన చూపిస్తుంది? / Which provision shows the widest appellate jurisdiction?",
     "Art.132 — రాజ్యాంగ ప్రశ్నలు",
     "Art.133 — సివిల్",
     "Art.134 — నేర",
     "Art.136 — SLP (విచక్షణ విస్తృత అధికారం)",
     "d",
     "Art.136 అత్యంత విస్తృతమైన అధికారం — ఏ కోర్టు లేదా ట్రిబ్యునల్ తీర్పు అయినా, ఏ విషయమైనా SC వద్దకు వచ్చే అవకాశం. / Art.136 is the widest — any court, any matter, SC has discretion to grant or refuse SLP."),

    (3, "medium",
     "Curative Petition అంటే ఏమిటి? / What is a Curative Petition?",
     "తొలి అప్పీల్ / First appeal",
     "Review Petition తిరస్కరణ తర్వాత చివరి పరిష్కారం / Last remedy after review petition rejected",
     "SLP తో సమానమైనది / Same as SLP",
     "Art.143 Reference / Art.143 Reference",
     "b",
     "Curative Petition: Review Petition తిరస్కరించబడిన తర్వాత దాఖలు చేసే చివరి రక్షణ. Rupa Ashok Hurra v. Ashok Hurra (2002) తీర్పులో SC దీన్ని రూపొందించింది. / Curative Petition: last remedy after review rejected — coined by SC in Rupa Ashok Hurra case (2002)."),

    # ── Section 4: Advisory & Writ Jurisdiction ────────────────────────────────
    (4, "easy",
     "SC రిట్ అధికార పరిధి ఏ అనుచ్ఛేదం? / SC writ jurisdiction under which Article?",
     "Art.32",
     "Art.131",
     "Art.226",
     "Art.143",
     "a",
     "Art.32: SC కి రిట్ జారీ చేసే అధికారం ఉంది — Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto. / Art.32: SC can issue 5 writs for enforcement of Fundamental Rights — it is itself a FR."),

    (4, "medium",
     "HC రిట్ అధికారం (Art.226) SC రిట్ అధికారం (Art.32) కంటే ఎందుకు విస్తృతమైంది? / Why is HC writ jurisdiction (Art.226) wider than SC (Art.32)?",
     "HC ఎక్కువ రిట్స్ జారీ చేయగలదు / HC can issue more types of writs",
     "HC ప్రాథమిక హక్కులతో పాటు ఇతర చట్టపరమైన హక్కులకు కూడా రిట్ జారీ చేయగలదు / HC can issue writs for other legal rights too",
     "HC మాత్రమే Habeas Corpus జారీ చేయగలదు / HC alone issues Habeas Corpus",
     "SC కంటే HC జ్యూరిస్డిక్షన్ పెద్దది / HC territorial jurisdiction is larger",
     "b",
     "Art.226: HC ప్రాథమిక హక్కులను + ఏదైనా చట్టపరమైన హక్కు (any other purpose) ఉల్లంఘనపై రిట్ జారీ చేయగలదు. Art.32: కేవలం ప్రాథమిక హక్కుల ఉల్లంఘనపై మాత్రమే. / Art.226 wider: HC issues writs for FR + any other legal right (Art.226 says 'any other purpose'); Art.32 only for FR."),

    (4, "easy",
     "రాష్ట్రపతి Art.143 కింద SC కి reference ఇస్తే SC తప్పనిసరిగా అభిప్రాయం ఇవ్వాలా? / Is SC bound to give advisory opinion under Art.143?",
     "అవును, తప్పనిసరి / Yes, mandatory",
     "కాదు, SC స్వేచ్ఛగా నిరాకరించవచ్చు / No, SC may refuse",
     "అవును, కానీ కేవలం చట్టపరమైన ప్రశ్నలకు మాత్రమే / Yes but only legal questions",
     "కాదు, ప్రధానమంత్రి అనుమతి కావాలి / No, PM approval needed",
     "b",
     "Art.143: SC అభిప్రాయం ఇవ్వడం తప్పనిసరి కాదు — SC తన అభిప్రాయం ఇవ్వడానికి నిరాకరించవచ్చు. ఇచ్చిన అభిప్రాయం కూడా బైండింగ్ కాదు. / Art.143: SC 'may' give opinion — not mandatory. Opinion, if given, is advisory (not binding on President)."),

    (4, "medium",
     "ఐదు రిట్‌లలో పర్సనల్ లిబర్టీని కాపాడే ముఖ్యమైన రిట్ ఏది? / Which writ protects personal liberty?",
     "Mandamus",
     "Quo Warranto",
     "Habeas Corpus",
     "Certiorari",
     "c",
     "Habeas Corpus (Latin: 'you have the body'): నిర్బంధించబడిన వ్యక్తిని కోర్టు ముందు హాజరుపర్చాలని ఆదేశిస్తుంది — వ్యక్తిగత స్వేచ్ఛకు అత్యంత ముఖ్యమైన రిట్. / Habeas Corpus: directs production of the detained person before court — most important writ for personal liberty."),

    (4, "medium",
     "Quo Warranto రిట్ ఎప్పుడు జారీ అవుతుంది? / When is Quo Warranto issued?",
     "చట్టవిరుద్ధ నిర్బంధం కేసులో / Illegal detention",
     "ప్రభుత్వ అధికారి చట్టబద్ధత సవాలు చేసినప్పుడు / Challenge to public office holder's authority",
     "అక్రమ ఆదేశాలు రద్దు చేయడానికి / Quashing illegal orders",
     "సూచన జారీ చేయడానికి / Directing authority to act",
     "b",
     "Quo Warranto: ఒక వ్యక్తి ప్రభుత్వ పదవిలో ఉండే హక్కు ఏమిటని అడుగుతుంది. పదవి చట్టబద్ధంగా ఆక్రమించారా లేదా అని తేల్చడానికి. / Quo Warranto: challenges the authority by which a person holds a public office — 'by what authority?'"),

    (4, "hard",
     "Certiorari మరియు Prohibition రిట్‌ల మధ్య తేడా ఏమిటి? / Difference between Certiorari and Prohibition?",
     "రెండూ ఒకే విషయం / Both are same",
     "Certiorari పూర్వానికి; Prohibition ముందుకు / Certiorari after decision; Prohibition before",
     "Prohibition పూర్వానికి; Certiorari ముందుకు / Prohibition after decision; Certiorari before",
     "రెండూ వ్యక్తిగత స్వేచ్ఛకు / Both for personal liberty",
     "b",
     "Certiorari: ఒక అక్రమ ఆదేశాన్ని రద్దు చేయడానికి (after decision). Prohibition: దిగువ కోర్టు అధికార పరిధి మించకుండా ముందే ఆపడానికి (before decision). / Certiorari = quash illegal order (post-decision); Prohibition = stop court from exceeding jurisdiction (pre-decision)."),

    (4, "medium",
     "Art.32 (SC రిట్ అధికారం) ను Dr. Ambedkar ఏమని అన్నారు? / What did Dr. Ambedkar call Art.32?",
     "రాజ్యాంగ ఆత్మ / Soul of the Constitution",
     "రాజ్యాంగ హృదయం మరియు ఆత్మ / Heart and soul of the Constitution",
     "ప్రజాస్వామ్య మూలస్తంభం / Pillar of democracy",
     "రాజ్యాంగం యొక్క ముఖ్య సూచిక / Most important index of Constitution",
     "b",
     "Dr. B.R. Ambedkar: Art.32 'రాజ్యాంగ హృదయం మరియు ఆత్మ' (heart and soul of the Constitution) — ఎందుకంటే ఇది ప్రాథమిక హక్కులను అమలు చేసే హామీ. / Ambedkar called Art.32 'the heart and soul of the Constitution' — it is itself a FR and guarantees enforcement of FRs."),

    (4, "medium",
     "Art.143 (SC సలహా అధికార పరిధి) కింద రాష్ట్రపతి SC కి ఏ విషయాలు నివేదించవచ్చు? / President may refer to SC under Art.143 for opinion on?",
     "సుప్రీంకోర్టు కేసులు మాత్రమే / Only Supreme Court cases",
     "చట్టం లేదా వాస్తవం యొక్క ప్రశ్న — ప్రాముఖ్యత ఉన్నది / Question of law or fact of public importance",
     "రాష్ట్రాల మధ్య తగాదాలు మాత్రమే / Only disputes between states",
     "సంధి/ఒప్పందాలకు సంబంధించిన ప్రశ్నలు మాత్రమే / Only treaty questions",
     "b",
     "Art.143: రాష్ట్రపతి చట్టం లేదా వాస్తవంపై ప్రాముఖ్యత ఉన్న ప్రశ్నను SC కి సలహా కోసం నివేదించవచ్చు; SC అభిప్రాయం ఇవ్వవచ్చు కానీ రాష్ట్రపతి దానిని తప్పనిసరిగా పాటించాల్సిన అవసరం లేదు. / Art.143: President may refer question of law/fact of public importance to SC for advisory opinion; SC may give opinion; opinion is advisory not binding."),

    # ── Section 5: Art.141 & Law of the Land ──────────────────────────────────
    (5, "easy",
     "SC ప్రకటించిన చట్టం (Law declared by SC) ఏ అనుచ్ఛేదం? / Law declared by SC binding under?",
     "Art.139",
     "Art.140",
     "Art.141",
     "Art.142",
     "c",
     "Art.141: SC ప్రకటించిన చట్టం భారతదేశంలో అన్ని కోర్టులపై బైండింగ్. / Art.141: Law declared by SC shall be binding on all courts within the territory of India."),

    (5, "medium",
     "Art.142 కింద SC ఏ ప్రత్యేక అధికారం కలిగి ఉంది? / Special power of SC under Art.142?",
     "చట్టాలు చేయడం / To make laws",
     "పూర్తి న్యాయం చేయడానికి ఆదేశాలు ఇవ్వడం / To pass decrees to do complete justice",
     "రాష్ట్రపతిని ఆదేశించడం / To direct the President",
     "బడ్జెట్ ఆమోదించడం / To approve budgets",
     "b",
     "Art.142: SC తన అధికార పరిధి ఉపయోగించేటప్పుడు 'పూర్తి న్యాయం' (complete justice) చేయడానికి ఏ ఆదేశమైనా ఇవ్వగలదు — ఇది SC యొక్క అసాధారణ అధికారం. / Art.142: SC may pass such decrees or orders as necessary for 'complete justice' — extraordinary power."),

    (5, "medium",
     "Stare Decisis సూత్రం అంటే ఏమిటి? / What is the doctrine of Stare Decisis?",
     "SC తీర్పులు ఆటోమేటిగా రద్దవుతాయి / SC judgments auto-expire",
     "పూర్వ తీర్పులను అనుసరించాలి — precedent / Must follow precedents",
     "SC స్వంత తీర్పులను మార్చుకోలేదు / SC cannot change its own judgments",
     "అన్ని న్యాయమూర్తులు ఏకగ్రీవంగా ఉండాలి / All judges must agree",
     "b",
     "Stare Decisis: 'stand by what was decided' — ముందు తీర్పులను అనుసరించే న్యాయ సూత్రం. Art.141 ప్రకారం SC తీర్పులు అన్ని కోర్టులకు బైండింగ్. / Stare Decisis: doctrine that precedents must be followed. Art.141 enforces this — SC law is binding on all courts."),

    (5, "hard",
     "SC తన స్వంత తీర్పును ఎప్పుడు రద్దు చేయగలదు? / When can SC overrule its own earlier judgment?",
     "ఎప్పుడూ చేయలేదు / Never",
     "కేవలం రాష్ట్రపతి అనుమతితో / Only with President's permission",
     "వివేచన (Discretion) ఆధారంగా, ముఖ్యంగా Constitutional Bench తీర్పులలో / At its discretion, especially in constitutional matters",
     "పార్లమెంట్ సూచన మేరకు మాత్రమే / Only on Parliament's direction",
     "c",
     "SC తన స్వంత తీర్పులకు కట్టుబడి ఉండవలసిన అవసరం లేదు — Stare Decisis SC పై బైండింగ్ కాదు (England వలె కాదు). SC ముఖ్యమైన రాజ్యాంగ విషయాలలో Constitutional Bench ద్వారా తన పూర్వ తీర్పులను రద్దు చేయవచ్చు. / SC not bound by its own decisions — unlike UK. It may overrule via a larger constitutional bench."),

    (5, "medium",
     "Art.144 అంటే ఏమిటి? / What does Art.144 state?",
     "SC న్యాయమూర్తుల జీతాలు / SC judges' salaries",
     "SC ఆదేశాలకు అన్ని పౌర మరియు న్యాయ అధికారులు సహాయం చేయాలి / All civil and judicial authorities must act in aid of SC",
     "SC సీటు / SC's seat",
     "SC రికార్డుల నిర్వహణ / SC's record keeping",
     "b",
     "Art.144: భారతదేశంలో అన్ని పౌర మరియు న్యాయ అధికారులు SC ఆదేశాలకు సహాయం చేయాలి. / Art.144: All civil and judicial authorities in India shall act in aid of the Supreme Court."),

    (5, "medium",
     "SC న్యాయమూర్తి సంఖ్య నిర్ణయించే అధికారం ఎవరికి ఉంది? / Who determines the number of SC judges?",
     "రాష్ట్రపతి / President",
     "ప్రధాన న్యాయమూర్తి / CJI",
     "పార్లమెంట్ / Parliament",
     "కేంద్ర మంత్రిమండలి / Union Cabinet",
     "c",
     "Art.124(1): SC న్యాయమూర్తుల సంఖ్యను పార్లమెంట్ చట్టం ద్వారా పెంచవచ్చు. 2019 లో 34 కి పెంచారు. / Art.124(1): Parliament by law may increase the number of SC judges. Currently 34 (CJI + 33)."),

    (5, "hard",
     "Art.129 అంటే ఏమిటి? / What is Art.129?",
     "SC ని 'రికార్డు కోర్టు'గా ప్రకటిస్తుంది / Declares SC as Court of Record",
     "SC సీటు / SC's seat",
     "CJI నియామకం / CJI appointment",
     "SC మూల అధికార పరిధి / SC original jurisdiction",
     "a",
     "Art.129: SC ఒక 'Court of Record' — దాని తీర్పులు శాశ్వతంగా నమోదవుతాయి మరియు contempt of court అధికారం ఉంది. / Art.129: SC is a Court of Record — its judgments are recorded permanently and it has power of contempt of court."),

    (5, "medium",
     "Art.145 కింద SC Rules ఎవరు రూపొందించవచ్చు? / Who may make Rules of SC under Art.145?",
     "పార్లమెంట్ / Parliament",
     "రాష్ట్రపతి అనుమతితో SC / SC with President's approval",
     "CJI స్వంత అధికారం ద్వారా / CJI by own authority",
     "కేంద్ర న్యాయ మంత్రి / Union Law Minister",
     "b",
     "Art.145: రాష్ట్రపతి అనుమతితో SC తన విచారణ విధానాన్ని నియంత్రించే నియమాలను రూపొందించవచ్చు. SC మైనారిటీ కేసులు, కోరం నిర్ణయం (Art.145(3) — 5 న్యాయమూర్తులు కోరం) కూడా ఇందులో ఉంది. / Art.145: SC may make rules with President's approval; Art.145(3) — minimum 5 judges to decide questions involving Constitution's interpretation."),

    # ── Section 6: Collegium System ────────────────────────────────────────────
    (6, "easy",
     "కొలీజియం వ్యవస్థ అంటే ఏమిటి? / What is the Collegium System?",
     "SC మరియు HC న్యాయమూర్తుల నియామకానికి న్యాయమూర్తులే నిర్ణయించే వ్యవస్థ / System where judges decide judicial appointments",
     "పార్లమెంట్ న్యాయమూర్తులను ఎన్నికొనే వ్యవస్థ / Parliament elects judges",
     "రాష్ట్రపతి స్వతంత్రంగా నియమించే వ్యవస్థ / President appoints independently",
     "న్యాయమూర్తుల పారదర్శక ఎంపిక / Transparent public selection",
     "a",
     "కొలీజియం వ్యవస్థ: SC యొక్క సీనియర్ న్యాయమూర్తుల సమూహం (CJI + 4 సీనియర్ జడ్జీలు) SC మరియు HC న్యాయమూర్తులను నిర్ణయిస్తుంది. రాజ్యాంగంలో నేరుగా లేదు — Second Judges Case (1993) తీర్పు ద్వారా వచ్చింది. / Collegium: CJI + 4 senior-most SC judges decide judicial appointments. Not in Constitution — evolved through Second Judges Case (1993)."),

    (6, "medium",
     "కొలీజియం వ్యవస్థ ఏ కేసు ద్వారా స్థాపించబడింది? / Collegium system established through which case?",
     "Kesavananda Bharati Case 1973",
     "Second Judges Case 1993",
     "S.R. Bommai Case 1994",
     "Minerva Mills Case 1980",
     "b",
     "Second Judges Case (Supreme Court Advocates-on-Record Association v. Union of India, 1993): SC 9-జడ్జీల బెంచ్ CJI 'primacy' సూత్రాన్ని నిర్ణయించింది — 'consultation' అంటే 'concurrence'. / Second Judges Case 1993: 9-judge bench — 'consultation' means 'concurrence'; established collegium supremacy."),

    (6, "medium",
     "మొదటి న్యాయమూర్తుల కేసు (First Judges Case, 1981) ఏమి తేల్చింది? / What did the First Judges Case (1981) decide?",
     "కొలీజియం ప్రాధాన్యత ఉంది / Collegium has primacy",
     "కార్యనిర్వాహకుడికి (Executive) ప్రాధాన్యత ఉంది / Executive has primacy",
     "CJI మాత్రమే నిర్ణయిస్తారు / CJI alone decides",
     "పార్లమెంట్ నిర్ణయిస్తుంది / Parliament decides",
     "b",
     "First Judges Case (1981): SC 'consultation' అంటే 'concurrence' కాదు అని తేల్చింది — అంటే ప్రభుత్వం (Executive) కి ప్రాధాన్యత ఉంది. Second Judges Case (1993) దీన్ని తిరగేసింది. / First Judges Case 1981: Executive primacy in appointments. Overruled by Second Judges Case 1993."),

    (6, "hard",
     "NJAC (National Judicial Appointments Commission) ఏ సంవత్సరంలో SC రద్దు చేసింది? / When did SC strike down NJAC?",
     "2010",
     "2013",
     "2015",
     "2018",
     "c",
     "2015లో SC 99వ రాజ్యాంగ సవరణ మరియు NJAC చట్టాన్ని రద్దు చేసింది — కొలీజియం వ్యవస్థను పునరుద్ధరించింది. Fourth Judges Case (Supreme Court Advocates-on-Record v. UOI, 2015). / SC struck down 99th Amendment + NJAC Act in 2015 — Fourth Judges Case — collegium system restored."),

    (6, "medium",
     "HC న్యాయమూర్తుల నియామకంలో కొలీజియంలో ఎంత మంది ఉంటారు? / How many members in collegium for HC judge appointments?",
     "CJI + 2 senior SC judges",
     "CJI + 4 senior SC judges",
     "CJI + Chief Justice of that HC",
     "CJI + 2 senior SC judges + Chief Justice of that HC",
     "a",
     "HC న్యాయమూర్తుల నియామకానికి: CJI + 2 సీనియర్ SC న్యాయమూర్తులు (3-member collegium). SC న్యాయమూర్తుల నియామకానికి: CJI + 4 సీనియర్ SC న్యాయమూర్తులు (5-member collegium). / For HC appointments: CJI + 2 senior SC judges (3-member). For SC appointments: CJI + 4 senior SC judges (5-member)."),

    (6, "hard",
     "కొలీజియం సిఫారసును ప్రభుత్వం రెండుసార్లు తిరిగి పంపిస్తే ఏమవుతుంది? / If government returns collegium recommendation twice?",
     "సిఫారసు రద్దవుతుంది / Recommendation lapses",
     "కొలీజియం నిర్ణయం తీసుకోవాలి / Collegium must reconsider",
     "కొలీజియం సిఫారసు రద్దు చేసి కొత్త పేరు ఇవ్వాలి / Collegium gives new name",
     "కొలీజియం పునరావృతంగా సిఫారసు చేస్తే ప్రభుత్వం నియమించాలి / Government bound to appoint if collegium reiterates",
     "d",
     "Third Judges Case (1998) మరియు Second Judges Case (1993) ప్రకారం: కొలీజియం సిఫారసు పునరావృతంగా పంపినపుడు ప్రభుత్వం నియమించాల్సి ఉంటుంది. / Per Second/Third Judges Cases: if collegium reiterates recommendation, government is bound to appoint."),

    (6, "medium",
     "Memorandum of Procedure (MoP) అంటే ఏమిటి? / What is the Memorandum of Procedure?",
     "న్యాయమూర్తుల తొలగింపు విధానం / Removal procedure",
     "SC మరియు HC న్యాయమూర్తుల నియామక విధానాన్ని నిర్దేశించే పత్రం / Document guiding judicial appointment procedure",
     "రాష్ట్రపతి అభిప్రాయం కోరే విధానం / Procedure for seeking President's opinion",
     "SC రికార్డుల నిర్వహణ నిబంధనలు / SC record-keeping rules",
     "b",
     "MoP: SC మరియు HC న్యాయమూర్తుల నియామక విధానాన్ని నిర్దేశించే పత్రం — కొలీజియం మరియు ప్రభుత్వం మధ్య అంగీకారంపై ఆధారపడింది. / MoP: document outlining procedure for judicial appointments — agreed between collegium and government."),

    (6, "hard",
     "Third Judges Case (1998) ప్రెసిడెన్షియల్ రిఫరెన్స్ ఏమి స్పష్టం చేసింది? / What did the Third Judges Case (1998 Presidential Reference) clarify?",
     "కొలీజియం ఒక్కడే నిర్ణయిస్తారు / Collegium alone decides",
     "SC న్యాయమూర్తుల నియామకానికి CJI + 4 సీనియర్ జడ్జీలు కొలీజియంగా పనిచేస్తారు / CJI + 4 senior judges form collegium for SC appointments",
     "NJAC చట్టబద్ధంగా ఉంది / NJAC is valid",
     "రాష్ట్రపతికి తుది అధికారం / President has final say",
     "b",
     "Third Judges Case (1998 Presidential Reference): SC 9-జడ్జీల బెంచ్ CJI + 4 సీనియర్ SC న్యాయమూర్తులు (5 మంది) = కొలీజియం SC న్యాయమూర్తుల నియామకానికి అని స్పష్టపరించింది. HC కి: CJI + 2 సీనియర్ జడ్జీలు. / Third Judges Case 1998 (Presidential Reference): 9-judge bench — collegium for SC = CJI + 4 senior-most SC judges; for HC = CJI + 2 senior-most."),

    # ── Section 7: Miscellaneous / Key Articles ───────────────────────────────
    (7, "easy",
     "SC అనుచ్ఛేద పరిధి (Art.124 to Art.147) ఏ భాగంలో ఉంది? / SC provisions (Art.124–147) are in which Part?",
     "Part IV",
     "Part V",
     "Part VI",
     "Part VII",
     "b",
     "Art.124-147 Part V లో ఉంది — The Union (Union Judiciary). Part VI = States judiciary (HC). / SC provisions (Art.124–147) in Part V (The Union)."),

    (7, "medium",
     "Art.145 ప్రకారం SC రూల్స్ ఎవరి అనుమతితో తయారవుతాయి? / SC Rules under Art.145 made with whose approval?",
     "పార్లమెంట్ / Parliament",
     "రాష్ట్రపతి / President",
     "కేంద్ర మంత్రిమండలి / Union Cabinet",
     "కేంద్ర న్యాయ మంత్రి / Union Law Minister",
     "b",
     "Art.145: SC రాష్ట్రపతి అనుమతితో తన విచారణ విధానానికి సంబంధించిన నిబంధనలు తయారు చేయగలదు. / Art.145: SC may, with President's approval, make rules regulating practice and procedure of court."),

    (7, "hard",
     "SC తీర్పు ఖచ్చితం చేసే (Finality of SC decree) అనుచ్ఛేదం ఏది? / Article that finalises SC decrees?",
     "Art.140",
     "Art.141",
     "Art.142",
     "Art.143",
     "c",
     "Art.142: SC తీర్పులు/ఆదేశాలు అమలు కోసం దేశంలో ఎక్కడైనా అమలు చేయవచ్చు; 'complete justice' కోసం ఏ ఆదేశమైనా ఇవ్వవచ్చు. / Art.142: SC decrees/orders enforceable throughout India; SC may pass any order for 'doing complete justice'."),

    (7, "medium",
     "SC contempt of court శిక్ష అనుచ్ఛేదం ఏది? / SC contempt power under which Article?",
     "Art.128",
     "Art.129",
     "Art.130",
     "Art.131",
     "b",
     "Art.129: SC 'Court of Record' గా contempt of court కి శిక్ష విధించే అధికారం కలిగి ఉంది. / Art.129: As a Court of Record, SC has power to punish for contempt of court."),

    (7, "medium",
     "SC ఏ కేసులో మౌలిక నిర్మాణం (Basic Structure) సిద్ధాంతాన్ని ప్రతిపాదించింది? / SC propounded Basic Structure doctrine in which case?",
     "Golaknath Case 1967",
     "Minerva Mills Case 1980",
     "Kesavananda Bharati Case 1973",
     "Maneka Gandhi Case 1978",
     "c",
     "Kesavananda Bharati v. State of Kerala (1973): 13-జడ్జీల బెంచ్ 'Basic Structure Doctrine' ప్రతిపాదించింది — పార్లమెంట్ రాజ్యాంగ మూల నిర్మాణాన్ని సవరించలేదు. / Kesavananda Bharati (1973): 13-judge bench — Parliament cannot amend the Basic Structure of the Constitution."),

    (7, "easy",
     "SC ను జాతీయ రాజధానిలో ఏ సంవత్సరం స్థాపించారు? / When was the Supreme Court of India established?",
     "1935",
     "1947",
     "1950",
     "1952",
     "c",
     "భారత సర్వోన్నత న్యాయస్థానం 26 జనవరి 1950 న స్థాపించబడింది — భారత రాజ్యాంగం అమలులోకి వచ్చిన రోజున. / SC established on 26 January 1950 — the day the Constitution came into force."),

    (7, "medium",
     "SC న్యాయమూర్తుల నియామక లేఖ (Warrant of Appointment) ఎవరు జారీ చేస్తారు? / Who issues the warrant of appointment for SC judges?",
     "ప్రధాన న్యాయమూర్తి / CJI",
     "కేంద్ర న్యాయ మంత్రి / Union Law Minister",
     "రాష్ట్రపతి / President",
     "సంయుక్త కార్యదర్శి / Joint Secretary",
     "c",
     "SC న్యాయమూర్తుల నియామక వారెంట్ రాష్ట్రపతి జారీ చేస్తారు — Art.124(2) ప్రకారం. / President issues the warrant of appointment for SC judges (Art.124(2))."),

    (7, "hard",
     "Art.138 ప్రకారం SC అధికార పరిధిని ఎవరు విస్తరించవచ్చు? / Who can extend SC's jurisdiction under Art.138?",
     "కేంద్ర మంత్రిమండలి / Union Cabinet",
     "పార్లమెంట్ / Parliament",
     "రాష్ట్రపతి / President",
     "SC తానే / SC itself",
     "b",
     "Art.138: పార్లమెంట్ చట్టం ద్వారా SC అధికార పరిధిని విస్తరించవచ్చు. / Art.138: Parliament may by law extend the jurisdiction and powers of SC with respect to any matter."),
]


def _seed_polity_ch20_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    ph = '%s' if use_postgres else '?'
    existing = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
        (_SUBJECT, _TOPIC, _CH))
    row = row_to_dict_fn(existing.fetchone())

    if row and not force:
        return row['id']

    import json
    sections_json = json.dumps(_SECTIONS, ensure_ascii=False)

    if row:
        db_exec_fn(conn,
            f"UPDATE study_notes SET chapter_title_te={ph}, chapter_title_en={ph}, "
            f"pages_ref={ph}, sections_json={ph} "
            f"WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
            (_TITLE_TE, _TITLE_EN, _PAGES, sections_json, _SUBJECT, _TOPIC, _CH))
        return row['id']
    else:
        db_exec_fn(conn,
            f"INSERT INTO study_notes (subject, topic, chapter_num, chapter_title_te, "
            f"chapter_title_en, pages_ref, sections_json) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph})",
            (_SUBJECT, _TOPIC, _CH, _TITLE_TE, _TITLE_EN, _PAGES, sections_json))
        cur2 = db_exec_fn(conn,
            f"SELECT id FROM study_notes WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
            (_SUBJECT, _TOPIC, _CH))
        return row_to_dict_fn(cur2.fetchone())['id']


def _seed_polity_ch20_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    ph = '%s' if use_postgres else '?'
    cur = db_exec_fn(conn,
        f"SELECT id FROM study_notes WHERE subject={ph} AND topic={ph} AND chapter_num={ph}",
        (_SUBJECT, _TOPIC, _CH))
    note = row_to_dict_fn(cur.fetchone())
    if not note:
        return
    note_id = note['id']

    existing = db_exec_fn(conn,
        f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    if list(existing.fetchone())[0] > 0:
        return

    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4, 1: 1, 2: 2, 3: 3, 4: 4}

    for row in _MCQS:
        sec_idx  = row[0]
        diff_str = row[1]
        q_te     = row[2]
        opt_a    = row[3]
        opt_b    = row[4]
        opt_c    = row[5]
        opt_d    = row[6]
        correct  = row[7]
        expl     = row[8]
        exam_type = row[9] if len(row) > 9 else 'General'
        if not exam_type:
            exam_type = 'General'

        diff_int = diff_map.get(diff_str, 1)
        db_exec_fn(conn,
            f"""INSERT INTO chapter_mcqs
                (study_note_id, section_idx, difficulty, exam_type,
                 q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
                VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})""",
            (note_id, sec_idx, diff_int, exam_type,
             q_te, opt_a, opt_b, opt_c, opt_d, correct, expl))
