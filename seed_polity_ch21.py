# seed_polity_ch21.py
# Chapter 21 — High Courts & Subordinate Courts
# Total Sections: 8 | Total MCQs: 56
# Sections:
#   0 — Establishment & Composition of High Courts (7 MCQs)
#   1 — Appointment & Removal of HC Judges (8 MCQs)
#   2 — Original Jurisdiction of HC (7 MCQs)
#   3 — Appellate Jurisdiction of HC (7 MCQs)
#   4 — Writ Jurisdiction — Art.226 (7 MCQs)
#   5 — Supervisory & Other Powers (7 MCQs)
#   6 — Subordinate Courts (6 MCQs)
#   7 — Miscellaneous / Key Articles (7 MCQs)

_CH = 21
_SUBJECT = 'GK'
_TOPIC   = 'Indian_Polity'
_TITLE_TE = 'హైకోర్టులు & అధీన న్యాయస్థానాలు'
_TITLE_EN = 'High Courts & Subordinate Courts'
_PAGES    = 'Ch.21 (Lakshmikanth)'

_SECTIONS = [
    "హైకోర్టుల స్థాపన & కూర్పు",
    "HC న్యాయమూర్తుల నియామకం & తొలగింపు",
    "HC మూల అధికార పరిధి",
    "HC అప్పీలేట్ అధికార పరిధి",
    "రిట్ అధికార పరిధి — అనుచ్ఛేదం 226",
    "పర్యవేక్షణ & ఇతర అధికారాలు",
    "అధీన న్యాయస్థానాలు",
    "విభిన్న కీలక అనుచ్ఛేదాలు",
]

_MCQS = [
    # ── Section 0: Establishment & Composition ─────────────────────────────────
    (0, "easy",
     "హైకోర్టుల స్థాపనను ప్రస్తావించే అనుచ్ఛేదం ఏది? / Which Article establishes High Courts?",
     "అనుచ్ఛేదం 212 / Art.212",
     "అనుచ్ఛేదం 214 / Art.214",
     "అనుచ్ఛేదం 226 / Art.226",
     "అనుచ్ఛేదం 231 / Art.231",
     "b",
     "Art.214: ప్రతి రాష్ట్రానికి హైకోర్టు ఉంటుంది. / Art.214: There shall be a High Court for each State."),

    (0, "easy",
     "హైకోర్టు న్యాయమూర్తుల పదవీ విరమణ వయస్సు ఎంత? / Retirement age of HC judges?",
     "60 సంవత్సరాలు / 60 years",
     "62 సంవత్సరాలు / 62 years",
     "65 సంవత్సరాలు / 65 years",
     "70 సంవత్సరాలు / 70 years",
     "b",
     "HC న్యాయమూర్తులు 62 సంవత్సరాలకు పదవీ విరమణ చేస్తారు; SC న్యాయమూర్తులు 65 సంవత్సరాలకు. / HC judges retire at 62; SC judges at 65."),

    (0, "medium",
     "రాజ్యాంగం ప్రకారం హైకోర్టుల పరిధి (Part VI) ఏ అనుచ్ఛేదాల నుండి? / HC provisions are in which Articles?",
     "Art.200 నుండి Art.215 వరకు",
     "Art.214 నుండి Art.231 వరకు",
     "Art.124 నుండి Art.147 వరకు",
     "Art.168 నుండి Art.212 వరకు",
     "b",
     "HC కి సంబంధించిన అంశాలు Part VI లో Art.214 నుండి Art.231 వరకు ఉంటాయి. / HC provisions: Part VI (States), Art.214–231."),

    (0, "medium",
     "రెండు రాష్ట్రాలకు ఉమ్మడి హైకోర్టు ఏర్పాటు చేయడానికి ఏ అనుచ్ఛేదం? / Which Article allows common HC for two or more states?",
     "Art.214",
     "Art.231",
     "Art.226",
     "Art.222",
     "b",
     "Art.231: పార్లమెంట్ రెండు లేదా అంతకు మించిన రాష్ట్రాలకు ఉమ్మడి హైకోర్టు స్థాపించవచ్చు. / Art.231: Parliament may establish a common HC for two or more states (e.g., Guwahati HC for NE states)."),

    (0, "medium",
     "హైకోర్టు 'Court of Record' అని ఏ అనుచ్ఛేదం చెప్తుంది? / Which Article declares HC as Court of Record?",
     "Art.214",
     "Art.215",
     "Art.216",
     "Art.217",
     "b",
     "Art.215: హైకోర్టు 'Court of Record' — దాని తీర్పులు శాశ్వతంగా నమోదవుతాయి మరియు contempt of court అధికారం ఉంది. / Art.215: HC is a Court of Record with power of contempt of court."),

    (0, "hard",
     "హైకోర్టు న్యాయమూర్తుల సంఖ్యను ఎవరు నిర్ణయిస్తారు? / Who determines the strength of HC judges?",
     "రాష్ట్ర ముఖ్యమంత్రి / Chief Minister",
     "హైకోర్టు ప్రధాన న్యాయమూర్తి / HC Chief Justice",
     "రాష్ట్రపతి / President of India",
     "పార్లమెంట్ / Parliament",
     "c",
     "హైకోర్టు న్యాయమూర్తుల సంఖ్యను రాష్ట్రపతి నిర్ణయిస్తారు (Art.216). / Art.216: President determines the strength of each HC."),

    (0, "medium",
     "హైకోర్టు ప్రధాన న్యాయమూర్తి ప్రమాణ స్వీకారం ఎవరి ముందు జరుగుతుంది? / HC Chief Justice takes oath before?",
     "ముఖ్యమంత్రి / Chief Minister",
     "రాష్ట్రపతి / President",
     "గవర్నర్ / Governor",
     "భారత ప్రధాన న్యాయమూర్తి / CJI",
     "c",
     "Art.219: HC న్యాయమూర్తులు గవర్నర్ ముందు ప్రమాణ స్వీకారం చేస్తారు. / Art.219: HC judges take oath before the Governor of the state."),

    (0, "hard",
     "HC Acts (పాత HC చట్టాలు) కింద ఉన్న HCలు రాజ్యాంగం ద్వారా కొనసాగుతున్నాయి — ఏ అనుచ్ఛేదం? / HCs existing under HC Acts continue under Constitution — which Article?",
     "Art.214",
     "Art.215",
     "Art.225",
     "Art.231",
     "c",
     "Art.225: హైకోర్టు ప్రస్తుతం ఉన్న అధికార పరిధి, అధికారాలు మరియు విధానం కొనసాగుతాయి (Letters Patent Acts మరియు పాత HC చట్టాలు కింద). / Art.225: Jurisdiction, powers, authority and law administered by existing HCs shall continue subject to Parliament's law."),

    # ── Section 1: Appointment & Removal ──────────────────────────────────────
    (1, "easy",
     "హైకోర్టు న్యాయమూర్తులను ఎవరు నియమిస్తారు? / Who appoints HC judges?",
     "గవర్నర్ / Governor",
     "ముఖ్యమంత్రి / Chief Minister",
     "రాష్ట్రపతి / President",
     "భారత ప్రధాన న్యాయమూర్తి / CJI",
     "c",
     "Art.217: హైకోర్టు న్యాయమూర్తులను రాష్ట్రపతి నియమిస్తారు — CJI, రాష్ట్ర గవర్నర్, HC ప్రధాన న్యాయమూర్తిని సంప్రదించిన తర్వాత. / Art.217: HC judges appointed by President after consulting CJI, Governor, and HC Chief Justice."),

    (1, "medium",
     "HC న్యాయమూర్తి నియామకానికి కొలీజియంలో ఎంత మంది ఉంటారు? / Collegium for HC judge appointment?",
     "CJI + 4 SC న్యాయమూర్తులు / CJI + 4 SC judges",
     "CJI + 2 SC సీనియర్ న్యాయమూర్తులు / CJI + 2 senior SC judges",
     "CJI + HC CJ + రాజ్యాంగ న్యాయమూర్తి / CJI + HC CJ + constitutional judge",
     "CJI మాత్రమే / CJI alone",
     "b",
     "HC న్యాయమూర్తుల నియామకానికి: CJI + 2 సీనియర్ SC న్యాయమూర్తులు (3-member collegium). SC నియామకానికి 5-member. / For HC appointments: CJI + 2 senior SC judges (3-member collegium)."),

    (1, "medium",
     "హైకోర్టు న్యాయమూర్తి నియామకానికి అర్హతలు ఏమిటి? / Qualifications for HC judge appointment (Art.217)?",
     "25 సంవత్సరాల వయస్సు; 5 సంవత్సరాల HC అనుభవం",
     "భారత పౌరుడు; HC న్యాయమూర్తిగా 10 సం. లేదా HC అడ్వకేట్‌గా 10 సం.",
     "భారత పౌరుడు; HC అడ్వకేట్‌గా 5 సం.",
     "30 సంవత్సరాల వయస్సు; జిల్లా జడ్జి అనుభవం",
     "b",
     "Art.217: (1) భారత పౌరుడు; (2) HC న్యాయమూర్తిగా 10 సంవత్సరాలు లేదా HC అడ్వకేట్‌గా 10 సంవత్సరాలు. వయస్సు పరిమితి లేదు. / Art.217: Must be citizen + HC judge for 10 years OR HC advocate for 10 years."),

    (1, "medium",
     "HC న్యాయమూర్తిని ఒక HC నుండి మరొక HC కి బదిలీ చేయడానికి ఏ అనుచ్ఛేదం? / Transfer of HC judge between HCs?",
     "Art.218",
     "Art.220",
     "Art.222",
     "Art.224",
     "c",
     "Art.222: CJI సంప్రదింపు తర్వాత రాష్ట్రపతి HC న్యాయమూర్తిని ఒక HC నుండి మరొక HC కి బదిలీ చేయగలరు. / Art.222: President may transfer HC judge to another HC after consulting CJI."),

    (1, "hard",
     "పదవీ విరమణ తర్వాత HC న్యాయమూర్తి ఏ కోర్టులో వాదించవచ్చు? / Where can a retired HC judge practice?",
     "ఏ కోర్టులో అయినా / Any court",
     "కేవలం SC లో / Only in SC",
     "ఆ రాష్ట్ర HC లేదా దాని అధీన కోర్టులలో కాదు; కానీ SC లో లేదా ఇతర HCలలో వాదించవచ్చు / Not in that HC or subordinate courts; may in SC/other HCs",
     "ఎక్కడా వాదించలేదు / Cannot practice anywhere",
     "c",
     "Art.220: HC న్యాయమూర్తి పదవీ విరమణ తర్వాత తాను పనిచేసిన HC లో లేదా దాని అధీన కోర్టులలో వాదించలేరు. SC లో లేదా ఇతర HCలలో వాదించవచ్చు. / Art.220: Retired HC judge cannot plead in that HC or its subordinate courts; may in SC or other HCs."),

    (1, "medium",
     "HC న్యాయమూర్తి తొలగింపు విధానం SC న్యాయమూర్తి వలె ఉంటుందా? / Removal of HC judge — same as SC judge?",
     "కాదు, రాష్ట్ర అసెంబ్లీ ద్వారా / No, through state assembly",
     "అవును, అదే విధానం / Yes, same procedure",
     "కాదు, గవర్నర్ తొలగిస్తారు / No, Governor removes",
     "కాదు, SC ఆదేశంపై / No, on SC order",
     "b",
     "HC న్యాయమూర్తి తొలగింపు SC న్యాయమూర్తి వలె అదే — పార్లమెంట్ ప్రత్యేక మెజారిటీ + రాష్ట్రపతి ఆదేశం (Art.217 read with Art.124(4)). / HC judge removal same as SC — special majority of Parliament + President's order."),

    (1, "hard",
     "HC న్యాయమూర్తి నియామకానికి Art.217(3) ప్రకారం వయస్సు వివాదం ఎవరు నిర్ణయిస్తారు? / Who decides age dispute of HC judge (Art.217(3))?",
     "SC / Supreme Court",
     "రాష్ట్రపతి / President",
     "CJI / Chief Justice of India",
     "HC ప్రధాన న్యాయమూర్తి / HC Chief Justice",
     "c",
     "Art.217(3): HC న్యాయమూర్తి వయస్సు గురించి ఏదైనా వివాదం తలెత్తితే CJI నిర్ణయం తుది నిర్ణయం. / Art.217(3): If dispute arises as to age of HC judge, CJI's decision is final."),

    (1, "medium",
     "Acting Chief Justice HC లో ఎప్పుడు నియమించబడతారు? / When is an Acting CJ appointed for HC?",
     "CJ మరణించినప్పుడు / When CJ dies",
     "CJ అనారోగ్యం, సెలవు లేదా ఇతర కారణాలతో లేనప్పుడు / When CJ is absent/unable to perform",
     "HC మసిలిపోయినప్పుడు / When HC is dissolved",
     "చట్ట మంత్రి ఆదేశంపై / On Law Minister's direction",
     "b",
     "Art.223: CJ అందుబాటులో లేనప్పుడు రాష్ట్రపతి HC న్యాయమూర్తులలో ఒకరిని Acting CJ గా నియమించవచ్చు. / Art.223: President may appoint HC judge as Acting CJ when CJ's office is vacant or CJ is absent/unable to perform."),

    # ── Section 2: Original Jurisdiction ──────────────────────────────────────
    (2, "easy",
     "హైకోర్టు మూల అధికార పరిధి (Original Jurisdiction) దేనిపై? / HC original jurisdiction?",
     "కేవలం నేర విషయాలు / Only criminal matters",
     "కేవలం పన్ను వివాదాలు / Only tax disputes",
     "వివాహం, వీలునామా, దివాళా, నౌకాయానం, రాజ్యాంగ విషయాలు / Matrimonial, probate, insolvency, admiralty, constitutional matters",
     "కేవలం SC కి అప్పీల్ / Only SC appeals",
     "c",
     "HC మూల అధికార పరిధి రాష్ట్రం బట్టి మారుతుంది — ముఖ్యంగా Calcutta, Bombay, Madras HCలు వివాహ, వీలునామా, దివాళా, నౌకాయానం విషయాలలో మూల అధికార పరిధి కలిగి ఉన్నాయి. / HC original jurisdiction varies by state; Calcutta, Bombay, Madras HCs have original jurisdiction in matrimonial, probate, insolvency, admiralty, constitutional matters."),

    (2, "medium",
     "హైకోర్టుకు ఎన్నికల విషయాలలో మూల అధికార పరిధి ఉంటుందా? / Does HC have original jurisdiction in election matters?",
     "కాదు / No",
     "అవును — MP, MLA ఎన్నికలపై / Yes — MPs, MLAs elections",
     "కేవలం రాష్ట్రపతి ఎన్నికపై / Only President election",
     "కేవలం స్థానిక సంస్థ ఎన్నికలపై / Only local body elections",
     "b",
     "Art.329: MP మరియు MLA ఎన్నికలకు సంబంధించిన వివాదాలు HC లో Election Petition ద్వారా పరిష్కారమవుతాయి. / Art.329: Election disputes regarding MPs and MLAs are heard by HC through election petitions."),

    (2, "medium",
     "Art.226 కింద రిట్ అధికార పరిధి HC మూల అధికార పరిధిలో భాగమా? / Is Art.226 writ jurisdiction part of HC original jurisdiction?",
     "కాదు / No",
     "అవును / Yes",
     "కొంత భాగం మాత్రమే / Partially",
     "SC ఆదేశం మేరకు మాత్రమే / Only on SC direction",
     "b",
     "Art.226 కింద రిట్ జారీ చేసే అధికారం HC మూల అధికార పరిధిలో భాగం — ఇది ప్రాథమిక హక్కులతో పాటు ఇతర చట్టపరమైన హక్కులకూ వర్తిస్తుంది. / Art.226 writ power is part of HC's original jurisdiction — wider than SC's (Art.32)."),

    (2, "hard",
     "ఏ రాష్ట్రాల HCలు వాణిజ్య (Commercial) విషయాలలో మూల అధికార పరిధి కలిగి ఉన్నాయి? / Which HCs have original commercial jurisdiction?",
     "అన్ని హైకోర్టులు / All High Courts",
     "Calcutta, Bombay, Madras (ఆంగ్లో చట్టంపై ఆధారపడి) / Calcutta, Bombay, Madras",
     "ఢిల్లీ మరియు Bombay HCలు / Delhi and Bombay HCs",
     "ఏ హైకోర్టుకూ లేదు / None",
     "b",
     "Calcutta, Bombay, Madras HCలు చారిత్రకంగా (Letters Patent) మూల వాణిజ్య అధికార పరిధి కలిగి ఉన్నాయి. / Calcutta, Bombay, Madras HCs have original commercial jurisdiction based on their Letters Patent/Charter."),

    (2, "medium",
     "Art.228 ప్రకారం HC ఏ అధికారాన్ని కలిగి ఉంది? / What does Art.228 provide?",
     "HC అప్పీలేట్ అధికార పరిధి",
     "HC సూపర్వైజరీ అధికారం",
     "రాజ్యాంగ ప్రశ్న ఉంటే దిగువ కోర్టు కేసులను HC కి బదిలీ చేయడం",
     "HC contempt అధికారం",
     "c",
     "Art.228: దిగువ కోర్టులో విచారణలో ఉన్న కేసులో రాజ్యాంగ ప్రశ్న తలెత్తితే HC ఆ కేసును తన దగ్గరికి తీసుకోవచ్చు లేదా రాజ్యాంగ ప్రశ్నను నిర్ణయించి వాపసు పంపవచ్చు. / Art.228: HC may withdraw case from subordinate court involving constitutional question and decide it or return it after deciding the constitutional issue."),

    (2, "medium",
     "హైకోర్టు contempt of court అధికారం ఏ అనుచ్ఛేదం? / HC contempt power?",
     "Art.214",
     "Art.215",
     "Art.226",
     "Art.227",
     "b",
     "Art.215: HC 'Court of Record' హోదా ప్రకారం contempt of court అధికారం కలిగి ఉంది. / Art.215: As a Court of Record, HC has power to punish for contempt."),

    (2, "hard",
     "Letters Patent Appeals (LPAs) అంటే ఏమిటి? / What are Letters Patent Appeals?",
     "SC నుండి HC కి అప్పీళ్ళు / Appeals from SC to HC",
     "HC single judge నిర్ణయానికి వ్యతిరేకంగా HC division bench కి అప్పీల్ / Appeal from single HC judge to division bench within same HC",
     "SC అప్పీళ్ళు / SC appeals",
     "HC నుండి అడ్మినిస్ట్రేటివ్ ట్రిబ్యునల్‌కు అప్పీల్ / Appeal from HC to Admin tribunal",
     "b",
     "LPAs: HC single judge తీర్పుపై అదే HC division bench కి అప్పీల్ — ముఖ్యంగా Calcutta, Bombay, Madras, Allahabad HCలలో. / LPAs: Appeal from single HC judge to HC division bench within same HC (mainly in Calcutta, Bombay, Madras, Allahabad)."),

    (2, "medium",
     "రెవిన్యూ విషయాలలో HC కి మూల అధికార పరిధి ఉంటుందా? / Does HC have original jurisdiction in revenue matters?",
     "అవున, అన్ని HCలలో / Yes, in all HCs",
     "కాదు — రాజ్యాంగం ప్రత్యేకంగా ఇవ్వలేదు / No — Constitution does not give this",
     "అవున, Art.226 కింద / Yes under Art.226",
     "అవున, Art.131 కింద / Yes under Art.131",
     "b",
     "Art.225: రాజ్యాంగ ప్రభావంతో HC లకు రెవిన్యూ విషయాలలో మూల అధికార పరిధి తొలగించబడింది — ఉన్న Letters Patent HCలకు తప్ప (Calcutta, Bombay, Madras). / Art.225 proviso: Original jurisdiction of HCs (other than Letters Patent HCs) in Revenue matters is not preserved by Constitution."),

    # ── Section 3: Appellate Jurisdiction ──────────────────────────────────────
    (3, "easy",
     "హైకోర్టు అప్పీలేట్ అధికార పరిధి ఏ విషయాలలో ఉంది? / HC appellate jurisdiction covers?",
     "కేవలం నేర విషయాలు / Only criminal matters",
     "సివిల్ మరియు నేర విషయాలలో / Civil and criminal matters",
     "కేవలం పన్ను విషయాలు / Only tax matters",
     "కేవలం రాజ్యాంగ విషయాలు / Only constitutional matters",
     "b",
     "HC అప్పీలేట్ అధికార పరిధి సివిల్ మరియు నేర విషయాలలో ఉంది — దిగువ కోర్టుల తీర్పులపై. / HC appellate jurisdiction covers both civil and criminal matters — from subordinate courts."),

    (3, "medium",
     "HC కి నేర (Criminal) అప్పీల్‌లో ఏ విషయాలు వస్తాయి? / Criminal appeals to HC?",
     "7 సంవత్సరాల కంటే ఎక్కువ జైలు శిక్ష కేసులు మాత్రమే / Only cases with 7+ year imprisonment",
     "Sessions court తీర్పులపై + మరణ శిక్ష నిర్ణయాలు / Sessions court judgments + death sentence orders",
     "అన్ని మేజిస్ట్రేట్ తీర్పులు / All magistrate judgments",
     "కేవలం SC నుండి అప్పీళ్ళు / Only from SC",
     "b",
     "HC నేర అప్పీలేట్ అధికార పరిధి: Sessions court తీర్పులపై, మరణ శిక్ష నిర్ణయాలను ధృవీకరించడానికి HC విచారిస్తుంది. / HC criminal appellate: appeals from Sessions courts; HC must confirm death sentences."),

    (3, "medium",
     "HC సివిల్ అప్పీల్ ఏ కోర్టుల తీర్పులపై? / Civil appeals to HC from?",
     "కేవలం జిల్లా కోర్టుల నుండి / Only from District Courts",
     "అన్ని సివిల్ కోర్టుల నుండి / All civil courts",
     "కేవలం ట్రిబ్యునల్స్ నుండి / Only from tribunals",
     "జిల్లా కోర్టులు మరియు జిల్లా స్థాయి సివిల్ కోర్టుల నుండి / From District and subordinate civil courts",
     "d",
     "HC సివిల్ అప్పీలేట్ అధికార పరిధి: జిల్లా కోర్టులు మరియు దాని దిగువ సివిల్ కోర్టుల తీర్పులపై. / HC civil appellate: from District Court and subordinate civil courts."),

    (3, "medium",
     "HC తీర్పుకు వ్యతిరేకంగా SC కి ఎప్పుడు అప్పీల్ చేయవచ్చు? / When can HC judgment be appealed to SC?",
     "ఎల్లప్పుడూ / Always",
     "HC ఇచ్చే ధృవీకరణ పత్రం (Certificate) తో లేదా SLP (Art.136) ద్వారా / With HC certificate or SLP (Art.136)",
     "SC అనుమతి లేకుండా / Without SC permission",
     "రాష్ట్రపతి ఆదేశంతో మాత్రమే / Only on President's order",
     "b",
     "HC తీర్పు నుండి SC కి అప్పీల్ HC certificate (Art.132, 133, 134) తో లేదా SC వద్ద SLP (Art.136) దాఖలు చేయవచ్చు. / From HC to SC: with HC certificate (Art.132/133/134) or SLP under Art.136."),

    (3, "hard",
     "HC తీర్పుపై SC కి Certificate of Appeal ఇవ్వడానికి HC నిరాకరిస్తే ఏమి చేయాలి? / If HC refuses certificate, what is the remedy?",
     "అప్పీల్ సాధ్యం కాదు / No appeal possible",
     "రాష్ట్రపతికి పిటిషన్ / Petition to President",
     "Art.136 కింద SLP దాఖలు / File SLP under Art.136",
     "పార్లమెంట్‌కు ఫిర్యాదు / Complain to Parliament",
     "c",
     "HC Certificate నిరాకరించినా SC Art.136 కింద SLP దాఖలు చేయవచ్చు — SC స్వంత విచక్షణతో అప్పీల్ అంగీకరించవచ్చు లేదా తిరస్కరించవచ్చు. / If HC refuses certificate, party may file SLP under Art.136 — SC has discretion to admit or reject."),

    (3, "medium",
     "HC మొదటిసారి నేరం నిరూపించి మరణ శిక్ష విధిస్తే SC కి ఆటోమేటిగ్ అప్పీల్ ఉంటుందా? / Automatic appeal to SC when HC sentences death?",
     "అవును, Art.134 కింద / Yes under Art.134",
     "కాదు, SLP మాత్రమే / No, only SLP",
     "అవును, Art.132 కింద / Yes under Art.132",
     "కాదు, HC Certificate కావాలి / No, HC certificate needed",
     "a",
     "Art.134: HC Sessions Court నిర్ణయాన్ని తిప్పికొట్టి నేరంగా మరణ శిక్ష విధించినప్పుడు SC కి ఆటోమేటిగ్ అప్పీల్ ఉంటుంది. / Art.134(1)(a): Automatic appeal to SC when HC reverses acquittal and awards death sentence."),

    (3, "medium",
     "Art.133 కింద సివిల్ అప్పీల్ SC కి వెళ్ళడానికి ఏ ప్రమాణం? / Standard for civil appeal to SC under Art.133?",
     "HC ఆమోదం మాత్రమే / HC certificate only",
     "HC చట్టం యొక్క ముఖ్యమైన ప్రశ్న అని ధ్రువీకరిస్తే / HC certifies substantial question of law",
     "విచారణలో ఎంత మొత్తం ఉంటే / Based on amount involved",
     "ఎల్లప్పుడూ SC కి వెళ్ళవచ్చు / Always can appeal",
     "b",
     "Art.133: సివిల్ అప్పీళ్ళు — HC ధ్రువీకరిస్తే SC కి వెళ్ళవచ్చు — 'substantial question of law of general importance' అని నిరూపించాలి. / Art.133: Civil appeals to SC require HC certificate that it involves a substantial question of law of general importance."),

    (3, "hard",
     "Art.132 కింద HC నుండి SC అప్పీల్‌కు ఏ ప్రమాణం అవసరం? / What is needed for Art.132 appeal from HC to SC?",
     "మతపరమైన ప్రశ్న / Religious question",
     "రాజ్యాంగపరమైన అర్థ నిర్వచన ప్రశ్న తీర్పు — HC ధ్రువీకరణ / Constitutional interpretation question in judgment — HC certification",
     "విచారణలో రాష్ట్ర ప్రయోజనాలు ఉంటే / State interests involved",
     "2 లక్షలకు మించిన మొత్తం / Amount over 2 lakhs",
     "b",
     "Art.132: సివిల్, నేర, లేదా ఇతర కేసుల్లో HC తీర్పు 'రాజ్యాంగ అర్థ నిర్వచనం' యొక్క ముఖ్యమైన ప్రశ్నకు సంబంధించినదని HC ధ్రువీకరిస్తే SC కి అప్పీల్ వెళ్ళవచ్చు. / Art.132: Appeal to SC from HC if HC certifies that the case involves a substantial question of law as to interpretation of the Constitution."),

    # ── Section 4: Writ Jurisdiction Art.226 ──────────────────────────────────
    (4, "easy",
     "హైకోర్టు రిట్ అధికార పరిధి ఏ అనుచ్ఛేదం కింద? / HC writ jurisdiction?",
     "Art.32",
     "Art.224",
     "Art.226",
     "Art.227",
     "c",
     "Art.226: HC ప్రాథమిక హక్కులకు + ఇతర చట్టపరమైన హక్కులకు కూడా రిట్ జారీ చేయగలదు. / Art.226: HC may issue writs for FR enforcement + any other purpose (wider than SC's Art.32)."),

    (4, "medium",
     "Art.226 (HC రిట్) మరియు Art.32 (SC రిట్) లో మూలభూత తేడా ఏమిటి? / Key difference between Art.226 and Art.32?",
     "HC ఎక్కువ రిట్ రకాలు జారీ చేయగలదు / HC issues more types of writs",
     "Art.226 ప్రాథమిక హక్కులతో పాటు ఇతర చట్టపరమైన హక్కులకు కూడా వర్తిస్తుంది; Art.32 ప్రాథమిక హక్కులకు మాత్రమే / Art.226 for FR + other legal rights; Art.32 only for FR",
     "HC మాత్రమే Habeas Corpus జారీ చేయగలదు / Only HC issues Habeas Corpus",
     "Art.32 విస్తృతమైనది / Art.32 is wider",
     "b",
     "Art.226 విస్తృతమైనది: ప్రాథమిక హక్కులతో పాటు 'ఏ ఇతర ప్రయోజనానికైనా' రిట్ జారీ చేయగలదు. Art.32 కేవలం ప్రాథమిక హక్కుల ఉల్లంఘనపై మాత్రమే. / Art.226 wider: HC issues writs for FR + any other purpose; Art.32 only for FR violations."),

    (4, "medium",
     "HC Art.226 కింద ప్రైవేట్ వ్యక్తులపై రిట్ జారీ చేయగలదా? / Can HC issue writs against private individuals under Art.226?",
     "అవును, ఎల్లప్పుడూ / Yes, always",
     "కాదు, కేవలం ప్రభుత్వ అధికారులపై మాత్రమే / No, only against govt authorities",
     "కొంత మేరకు — Quo Warranto వంటి నిర్దిష్ట సందర్భాలలో / Limited — specific writs like Quo Warranto",
     "కాదు, ట్రిబ్యునల్‌కు వెళ్ళాలి / No, must go to tribunal",
     "c",
     "సాధారణంగా రిట్లు ప్రభుత్వ అధికారులు మరియు సంస్థలపై జారీ అవుతాయి. Quo Warranto మాత్రం ప్రభుత్వ పదవిలో ఉన్న ప్రైవేట్ వ్యక్తులపై కూడా వర్తించవచ్చు. / Writs generally against state/govt authorities; Quo Warranto can extend to private individuals holding public office."),

    (4, "hard",
     "Art.226(2) ప్రకారం HC అధికార పరిధి లేని ప్రభుత్వ అధికారులపై రిట్ జారీ చేయగలదా? / Can HC issue writs against authorities outside its territorial jurisdiction?",
     "కాదు, అసాధ్యం / No, impossible",
     "అవును, కారణ సంఘటన HC అధికార పరిధిలో జరిగితే / Yes, if cause of action arose within HC's jurisdiction",
     "అవును, ఎల్లప్పుడూ / Yes, always",
     "కాదు, SC మాత్రమే చేయగలదు / No, only SC",
     "b",
     "Art.226(2): రిట్ కారణం (cause of action) HC అధికార పరిధిలో పూర్తిగా లేదా పాక్షికంగా జరిగితే HC ఆ అధికార పరిధి వెలుపల ఉన్న అధికారులపై కూడా రిట్ జారీ చేయగలదు. / Art.226(2): HC may issue writs even against authorities outside its territory if cause of action arose (wholly or partly) within its jurisdiction."),

    (4, "medium",
     "Habeas Corpus రిట్ ఎవరికి జారీ అవుతుంది? / Who can petition for Habeas Corpus?",
     "కేవలం నిర్బంధించబడిన వ్యక్తి / Only the detained person",
     "ఎవరైనా (బంధువు, స్నేహితుడు, ప్రజా ప్రయోజన వ్యాజ్యం) / Anyone on behalf of detainee (relative, friend, PIL)",
     "కేవలం న్యాయవాది / Only a lawyer",
     "కేవలం ప్రభుత్వం / Only government",
     "b",
     "Habeas Corpus: నిర్బంధించబడిన వ్యక్తి తరపున ఎవరైనా కోర్టుకు వెళ్ళవచ్చు — బంధువులు, స్నేహితులు లేదా PIL ద్వారా. / Habeas Corpus: can be filed by anyone on behalf of the detainee — relative, friend, or via PIL."),

    (4, "medium",
     "రిట్ పిటిషన్ HC తిరస్కరిస్తే SC కి ఏ మార్గం ఉంది? / If HC rejects writ petition, remedy in SC?",
     "ఏ మార్గమూ లేదు / No remedy",
     "Art.32 కింద SC కి నేరుగా వెళ్ళవచ్చు / Can go directly to SC under Art.32",
     "రాష్ట్రపతికి అప్పీల్ / Appeal to President",
     "Art.136 SLP మాత్రమే / Only Art.136 SLP",
     "b",
     "HC రిట్ పిటిషన్ తిరస్కరించినా Art.32 కింద SC కి నేరుగా వెళ్ళవచ్చు (ప్రాథమిక హక్కుల విషయంలో) లేదా Art.136 SLP దాఖలు చేయవచ్చు. / If HC rejects writ, can still file under Art.32 in SC (for FR) or SLP under Art.136."),

    (4, "medium",
     "రిట్ కోసం HC లో దాఖలు చేయడం SC ని నేరుగా సంప్రదించే హక్కును తొలగిస్తుందా? / Does filing writ in HC bar direct SC petition?",
     "అవును, ఒకే విషయంపై రెండూ కాదు / Yes, cannot file in both",
     "కాదు, ఒకే సమయంలో SC కి Art.32 కింద కూడా వెళ్ళవచ్చు / No, can still file in SC",
     "అవును, SC అనుమతి అవసరం / Yes, SC permission needed",
     "అవును, కానీ Art.136 SLP మాత్రమే / Yes but only Art.136 SLP",
     "b",
     "పార్టీ HC లో రిట్ దాఖలు చేసినా SC Art.32 కింద లేదా Art.136 SLP ద్వారా వేరుగా వెళ్ళవచ్చు — SC ముందుగా HC ని ప్రయత్నించమని చెప్పవచ్చు (exhaustion of remedies). / Filing in HC does not bar SC petition — SC may ask party to exhaust HC remedy first but it's not mandatory."),

    (4, "hard",
     "Art.226 కింద HC రిట్ — ఏ సంస్థలకు వ్యతిరేకంగా జారీ చేయవచ్చు? / HC writ under Art.226 can be issued against whom?",
     "ప్రభుత్వ అధికారులకు మాత్రమే / Only government officials",
     "ప్రభుత్వ అధికారులు మరియు ఏ వ్యక్తి లేదా సంస్థకైనా / Government authorities AND any person or authority",
     "కేవలం రాష్ట్ర ప్రభుత్వానికి / Only state government",
     "ప్రాథమిక హక్కుల ఉల్లంఘన కేసుల్లో మాత్రమే / Only in FR violation cases",
     "b",
     "Art.226: SC Art.32 కన్నా విస్తృతమైనది — HC ఏ వ్యక్తి లేదా అధికారానికైనా (ప్రభుత్వ అధికారి కాకపోయినా) 'ఏ ప్రయోజనం కోసమైనా' రిట్ జారీ చేయవచ్చు. Art.32 ప్రాథమిక హక్కుల అమలు మాత్రమే. / Art.226 is wider — HC can issue writs to any person/authority for any purpose; Art.32 (SC) only for enforcement of Fundamental Rights."),

    # ── Section 5: Supervisory & Other Powers ─────────────────────────────────
    (5, "easy",
     "హైకోర్టు పర్యవేక్షణ అధికారం (Supervisory Jurisdiction) ఏ అనుచ్ఛేదం కింద? / HC supervisory jurisdiction?",
     "Art.224",
     "Art.225",
     "Art.226",
     "Art.227",
     "d",
     "Art.227: HC దాని పరిధిలోని అన్ని కోర్టులు మరియు ట్రిబ్యునల్స్ పై (military courts మినహా) పర్యవేక్షణ అధికారం కలిగి ఉంది. / Art.227: HC has superintendence over all courts and tribunals in its territory (except military courts)."),

    (5, "medium",
     "Art.227 మరియు Art.226 మధ్య తేడా ఏమిటి? / Difference between Art.227 and Art.226?",
     "రెండూ ఒకే విషయం / Both are same",
     "Art.227 పర్యవేక్షణ అధికారం; Art.226 రిట్ అధికారం / Art.227 = supervisory; Art.226 = writ",
     "Art.226 పర్యవేక్షణ; Art.227 రిట్ / Art.226 = supervisory; Art.227 = writ",
     "Art.227 అప్పీలేట్; Art.226 మూల / Art.227 = appellate; Art.226 = original",
     "b",
     "Art.226: రిట్ జారీ చేసే అధికారం. Art.227: అన్ని దిగువ కోర్టులు మరియు ట్రిబ్యునల్స్ పై పర్యవేక్షణ మరియు నియంత్రణ. / Art.226 = writ jurisdiction; Art.227 = superintendence over subordinate courts and tribunals."),

    (5, "hard",
     "Art.227 కింద HC పర్యవేక్షణలో ఏ సంస్థలు వస్తాయి? / What comes under Art.227 superintendence?",
     "కేవలం జిల్లా కోర్టులు / Only District Courts",
     "అన్ని కోర్టులు + సివిల్ ట్రిబ్యునల్స్ (military మినహా) / All courts + civil tribunals (except military)",
     "SC మరియు HC లు / SC and HCs",
     "కేవలం ట్రిబ్యునల్స్ / Only tribunals",
     "b",
     "Art.227: HC అన్ని దిగువ కోర్టులు మరియు ట్రిబ్యునల్స్ పై (military tribunals మినహా) పర్యవేక్షణ అధికారం కలిగి ఉంది. / Art.227: superintendence over all courts and tribunals (except military) within its territorial jurisdiction."),

    (5, "medium",
     "HC న్యాయమూర్తులు న్యాయ అధికారులకు సూచనలు ఇవ్వవచ్చా? / Can HC issue instructions to judicial officers?",
     "కాదు, పూర్తిగా నిషేధం / No, absolutely prohibited",
     "అవును, Art.227 కింద పర్యవేక్షణ అధికారంతో / Yes, under Art.227 superintendence",
     "కేవలం SC అనుమతితో / Only with SC permission",
     "కేవలం రాష్ట్రపతి ఆదేశంపై / Only on President's direction",
     "b",
     "Art.227 కింద HC న్యాయ అధికారులకు సూచనలు, నిర్దేశాలు ఇవ్వగలదు మరియు ప్రక్రియలు నిర్దేశించగలదు. / Under Art.227, HC can issue guidelines, instructions to subordinate judicial officers."),

    (5, "medium",
     "Art.229 ప్రకారం HC అధికారులు మరియు సిబ్బంది నియామకం ఎవరి అధికారం? / Who appoints HC officers and staff (Art.229)?",
     "రాష్ట్ర ప్రభుత్వం / State Government",
     "కేంద్ర ప్రభుత్వం / Central Government",
     "HC ప్రధాన న్యాయమూర్తి / HC Chief Justice",
     "రాష్ట్ర PSC / State PSC",
     "c",
     "Art.229: HC అధికారులు మరియు సిబ్బంది నియామకం HC ప్రధాన న్యాయమూర్తి అధికారంలో ఉంటుంది. రాష్ట్ర PSC నుండి మినహాయింపు కూడా CJ ఇవ్వవచ్చు. / Art.229: Officers and servants of HC appointed by CJ (or such judge as CJ directs); HC CJ may make rules exempting from State PSC."),

    (5, "hard",
     "Art.230 ఏమి చెప్తుంది? / What does Art.230 say?",
     "HC ఏర్పాటు",
     "HC పరిధిని కేంద్రపాలిత ప్రాంతాలకు పొడిగించే అధికారం పార్లమెంట్‌కు ఉంది",
     "HC కి advisory jurisdiction ఉంది",
     "HC అప్పీలేట్ పరిధి",
     "b",
     "Art.230: పార్లమెంట్ చట్టం ద్వారా HC పరిధిని కేంద్రపాలిత ప్రాంతాలకు పొడిగించవచ్చు లేదా మినహాయించవచ్చు. / Art.230: Parliament may by law extend the jurisdiction of HC to a Union Territory or exclude it."),

    (5, "medium",
     "HC Vacation Judge (వెకేషన్ జడ్జి) అంటే ఏమిటి? / What is an HC Vacation Judge?",
     "పదవీ విరమణ తర్వాత నియమించిన జడ్జి / Judge appointed after retirement",
     "సెలవుల సమయంలో అత్యవసర విషయాలు చూసే జడ్జి / Judge handling urgent matters during court vacation",
     "Ad hoc నియమించిన జడ్జి / Ad hoc appointed judge",
     "ట్రిబ్యునల్ జడ్జి / Tribunal judge",
     "b",
     "వెకేషన్ జడ్జి: న్యాయస్థానం సెలవులలో అత్యవసర విషయాలను (Habeas Corpus, బెయిల్ మొదలైనవి) పరిశీలించడానికి నియమించబడిన జడ్జి. / Vacation Judge: HC judge designated to hear urgent matters (habeas corpus, bail, injunctions) during court vacations."),

    (5, "hard",
     "Art.227 కింద HC పర్యవేక్షణ అధికారం ఏ కోర్టులకు వర్తిస్తుంది? / HC supervisory jurisdiction under Art.227 extends to which courts?",
     "కేవలం జిల్లా కోర్టులు / Only district courts",
     "HC అధికార పరిధిలో ఉన్న అన్ని కోర్టులు మరియు ట్రిబ్యునళ్ళు (సైనిక ట్రిబ్యునళ్ళు మినహా) / All courts and tribunals within HC territory (except military tribunals)",
     "కేవలం దిగువ నేర కోర్టులు / Only lower criminal courts",
     "కేవలం సివిల్ కోర్టులు / Only civil courts",
     "b",
     "Art.227: HC అన్ని కోర్టులు మరియు ట్రిబ్యునళ్ళపై పర్యవేక్షణ అధికారం కలిగి ఉంటుంది — సైనిక ట్రిబ్యునళ్ళు మినహా. ఇది అప్పీల్ కాదు — పర్యవేక్షణ (supervisory). / Art.227: HC superintendence over all courts and tribunals within its territory except military tribunals — supervisory not appellate."),

    # ── Section 6: Subordinate Courts ─────────────────────────────────────────
    (6, "easy",
     "జిల్లా న్యాయమూర్తుల నియామకం గురించి ఏ అనుచ్ఛేదం? / Appointment of District Judges?",
     "Art.233",
     "Art.235",
     "Art.237",
     "Art.229",
     "a",
     "Art.233: జిల్లా న్యాయమూర్తుల నియామకం గవర్నర్ చేస్తారు — HC తో సంప్రదించిన తర్వాత. / Art.233: District judges appointed by Governor in consultation with HC."),

    (6, "medium",
     "జిల్లా న్యాయమూర్తి అర్హత ఏమిటి? / Qualification for District Judge (Art.233)?",
     "HC అడ్వకేట్‌గా 7 సం. / HC advocate for 7 years",
     "Law degree + 5 సం. అనుభవం / Law degree + 5 years experience",
     "7 సంవత్సరాల న్యాయ అభ్యాసకుడు లేదా కేంద్ర/రాష్ట్ర సేవలో న్యాయాధికారి / 7 years advocate or judicial officer in union/state service",
     "IPS అధికారి / IPS officer",
     "c",
     "Art.233: జిల్లా న్యాయమూర్తి కాలేయందుకు: (1) 7 సంవత్సరాల అడ్వకేట్ అనుభవం లేదా (2) ఇప్పటికే కేంద్ర/రాష్ట్ర న్యాయ సేవలో ఉన్నవారు. / Art.233: District Judge must be advocate for 7 years or serving judicial officer in central/state service."),

    (6, "medium",
     "జిల్లా కోర్టుల నియంత్రణ ఏ అనుచ్ఛేదం కింద HC కి ఉంది? / HC control over district courts?",
     "Art.233",
     "Art.234",
     "Art.235",
     "Art.236",
     "c",
     "Art.235: జిల్లా న్యాయమూర్తుల నియంత్రణ (Control) HC కి ఉంటుంది — పోస్టింగ్, పదోన్నతి, సెలవు మొదలైనవి. / Art.235: HC has control over district courts and courts subordinate to district courts."),

    (6, "hard",
     "Art.236 లో 'District Judge' నిర్వచనంలో ఏ అధికారులు వస్తారు? / Art.236 definition of 'District Judge' includes?",
     "కేవలం జిల్లా మరియు సెషన్స్ జడ్జి / Only District and Sessions Judge",
     "Chief Presidency Magistrate, Sessions Judge, Addl. District Judge, Asst. Sessions Judge సహా / Includes Chief Presidency Magistrate, Sessions Judge, Addl. District Judge, Asst. Sessions Judge",
     "కేవలం Civil Judge / Only Civil Judge",
     "జిల్లా కలెక్టర్ / District Collector",
     "b",
     "Art.236: 'District Judge' అంటే — Sessions Judge, Addl. Sessions Judge, Asst. Sessions Judge, Chief Presidency Magistrate, Addl. Chief Presidency Magistrate, Sessions Judges of City Civil Courts, మొదలైనవారు. / Art.236: 'District Judge' includes Sessions Judge, Chief Presidency Magistrate, Addl. District Judge, etc."),

    (6, "medium",
     "న్యాయాధికారుల (Judicial Officers) నియామకం ఏ విధంగా జరుగుతుంది? / How are judicial officers below District Judge recruited?",
     "ముఖ్యమంత్రి నేరుగా / CM directly",
     "గవర్నర్ రాష్ట్ర PSC మరియు HC సంప్రదింపుతో / Governor in consultation with State PSC and HC",
     "HC మాత్రమే / HC alone",
     "UPSC ద్వారా / Through UPSC",
     "b",
     "Art.234: జిల్లా జడ్జి కంటే దిగువ న్యాయాధికారుల నియామకం గవర్నర్ చేస్తారు — రాష్ట్ర PSC మరియు HC సంప్రదింపు తర్వాత. / Art.234: Persons other than district judges to judicial service appointed by Governor in consultation with State PSC and HC."),

    (6, "hard",
     "Magistrate (మేజిస్ట్రేట్) మరియు Civil Judge (సివిల్ జడ్జి) మధ్య అధికార పరిధి తేడా ఏమిటి? / Difference between Magistrate and Civil Judge?",
     "రెండూ ఒకే విషయాలు చూస్తారు / Both handle same matters",
     "Magistrate — నేర విషయాలు; Civil Judge — సివిల్ విషయాలు / Magistrate — criminal; Civil Judge — civil",
     "Civil Judge — నేర విషయాలు; Magistrate — సివిల్ విషయాలు / Civil Judge — criminal; Magistrate — civil",
     "రెండూ సంబంధం లేదు / Both unrelated",
     "b",
     "Magistrate (మేజిస్ట్రేట్) నేర విషయాలు (CrPC కింద) పరిశీలిస్తారు. Civil Judge సివిల్ విషయాలు (CPC కింద) పరిశీలిస్తారు. / Magistrate handles criminal matters (under CrPC); Civil Judge handles civil matters (under CPC)."),

    (6, "medium",
     "జిల్లా న్యాయమూర్తి నియామకంలో ఏ అనుచ్ఛేదం ప్రకారం HC సంప్రదించాలి? / HC consultation is required for District Judge appointment under which Article?",
     "Art.233",
     "Art.234",
     "Art.235",
     "Art.237",
     "a",
     "Art.233(1): జిల్లా న్యాయమూర్తుల నియామకం — గవర్నర్ HC తో సంప్రదించి నియమిస్తారు. Art.234: న్యాయ సేవలలో ఇతర సభ్యుల నియామకం — రాష్ట్ర PSC మరియు HC తో సంప్రదించి. / Art.233(1): District Judges appointed by Governor in consultation with HC. Art.234: Other judicial service members appointed in consultation with SPSC and HC."),

    (6, "hard",
     "Art.235 కింద HC జిల్లా న్యాయమూర్తులు మరియు దిగువ న్యాయస్థానాలపై ఎలాంటి నియంత్రణ కలిగి ఉంటుంది? / What control does HC have over district judges under Art.235?",
     "నియామకాలు మాత్రమే / Only appointments",
     "పోస్టింగులు, ప్రమోషన్లు, సెలవులు — అన్ని నియంత్రణ HC కి / Postings, promotions, leave — all control with HC",
     "జిల్లా న్యాయమూర్తి తొలగింపు / Removal of district judge",
     "జీతాల నిర్ణయం / Determination of salaries",
     "b",
     "Art.235: HC జిల్లా న్యాయమూర్తులు మరియు దిగువ న్యాయస్థానాలపై నియంత్రణ కలిగి ఉంటుంది — పోస్టింగులు, ప్రమోషన్లు, సెలవులు. కానీ జిల్లా న్యాయమూర్తి తొలగింపు Art.311 ద్వారా. / Art.235: HC controls district courts and subordinate courts regarding postings, promotions, leave. Removal under Art.311 procedural safeguards."),

    # ── Section 7: Miscellaneous / Key Articles ───────────────────────────────
    (7, "easy",
     "HC Art.226 కింద రిట్ జారీ చేయడానికి కారణం అంటే ఏమిటి? / Cause of action for HC writ (Art.226)?",
     "కేవలం రాష్ట్రంలో జరిగిన సంఘటనలు / Only events in that state",
     "HC అధికార పరిధిలో పూర్తిగా లేదా పాక్షికంగా జరిగిన సంఘటన / Wholly or partly within HC's territorial jurisdiction",
     "కేవలం ఢిల్లీలో జరిగిన సంఘటనలు / Only events in Delhi",
     "కేవలం SC అనుమతితో / Only with SC permission",
     "b",
     "Art.226(2): Cause of action అంటే HC అధికార పరిధిలో పూర్తిగా లేదా పాక్షికంగా జరిగి ఉండాలి. / Art.226(2): HC can issue writs where cause of action arose wholly or partly within its territorial jurisdiction."),

    (7, "medium",
     "HC Art.225 ఏమి చెప్తుంది? / What does Art.225 say?",
     "HC ఏర్పాటు / Establishment of HC",
     "HC లో ముందున్న అధికార పరిధి, చట్టాలు కొనసాగుతాయి / Existing jurisdiction, laws continue in HC",
     "HC రిట్ అధికారం / HC writ power",
     "HC న్యాయమూర్తుల జీతాలు / HC judges' salaries",
     "b",
     "Art.225: సంవిధాన రచనకు ముందు ఉన్న HC అధికార పరిధి కొనసాగుతుంది — రాజ్యాంగంలో లేదా పార్లమెంట్ చట్టం ద్వారా మార్పు అయ్యే వరకు. / Art.225: Jurisdiction of existing HC continues as before — until altered by Parliament or Constitution."),

    (7, "hard",
     "HC న్యాయమూర్తి జీతాలు ఏ నిధి నుండి? / HC judges' salaries charged to?",
     "రాష్ట్ర ఏకీకృత నిధి / Consolidated Fund of State",
     "భారత ఏకీకృత నిధి / Consolidated Fund of India",
     "రాష్ట్ర ఆకస్మిక నిధి / State Contingency Fund",
     "కేంద్ర Votable appropriation",
     "a",
     "HC న్యాయమూర్తుల జీతాలు రాష్ట్ర ఏకీకృత నిధి నుండి చెల్లిస్తారు (Art.221). అయితే పదవీ విరమణ పెన్షన్లు కేంద్ర ఏకీకృత నిధి నుండి. / HC judges' salaries: Consolidated Fund of State (Art.221); pensions: CFI."),

    (7, "medium",
     "HC లో Advocate General (రాష్ట్ర ప్రభుత్వ అడ్వకేట్ జనరల్) నియమించే అధికారం ఎవరికి? / Who appoints Advocate General of State?",
     "ముఖ్యమంత్రి / Chief Minister",
     "HC ప్రధాన న్యాయమూర్తి / HC Chief Justice",
     "రాష్ట్ర గవర్నర్ / Governor of the State",
     "రాష్ట్రపతి / President",
     "c",
     "Art.165: రాష్ట్ర Advocate General ని గవర్నర్ నియమిస్తారు. అతడు HC జడ్జి పదవికి అర్హుడైన వ్యక్తి అయి ఉండాలి. / Art.165: AG of State appointed by Governor; must be qualified to be HC judge."),

    (7, "medium",
     "ఒక HC తన సర్క్యూట్ బెంచ్‌ను ఎక్కడ ఏర్పాటు చేయగలదు? / Where can a HC establish circuit bench?",
     "కేవలం రాజధానిలో / Only in state capital",
     "ఇతర నగరాలలో — రాష్ట్రపతి అనుమతితో / Other cities — with President's approval",
     "ఏ రాష్ట్రంలో అయినా / Any state",
     "SC అనుమతితో మాత్రమే / Only with SC permission",
     "b",
     "HC సర్క్యూట్ బెంచ్ రాష్ట్రపతి అనుమతితో రాష్ట్రంలోని వేరే నగరాలలో ఏర్పాటు చేయవచ్చు. / HC circuit bench may be established in other cities within the state with President's approval."),

    (7, "medium",
     "Art.226A (ప్రకారం రద్దు) — Art.226లో ఏమి చేర్చారు? / 44th Amendment (1978) deleted which article related to HC?",
     "Art.226A అనే వేరే అనుచ్ఛేదం రద్దు చేశారు / Deleted Art.226A",
     "Art.31C (National emergency) HC అప్పీల్ ఆగే నిబంధన / Art.31C provision suspending HC jurisdiction",
     "రాష్ట్ర అత్యవసర పరిస్థితిలో HC రిట్ అధికారాన్ని తాత్కాలికంగా నిలిపే Art.226A రద్దు / Deleted Art.226A that suspended HC writ power during state emergency",
     "Art.220A రద్దు / Deletion of Art.220A",
     "c",
     "44వ సవరణ (1978): Art.226A రద్దు చేసింది — ఇది Art.359 కింద జాతీయ అత్యవసర పరిస్థితిలో HC రిట్ అధికారాన్ని తాత్కాలికంగా నిలిపేది. / 44th Amendment 1978 deleted Art.226A which allowed suspension of HC writ power during national emergency under Art.359."),

    (7, "hard",
     "ఒకే రాష్ట్రంలో రెండు హైకోర్టులు ఏర్పాటు చేయవచ్చా? / Can there be two HCs for one state?",
     "అవును, పార్లమెంట్ చట్టం ద్వారా / Yes, by Parliament",
     "కాదు, ఒక రాష్ట్రానికి ఒక HC మాత్రమే / No, one state one HC",
     "అవున, రాష్ట్రపతి ఆదేశంతో / Yes, on President's order",
     "అవున, రాజ్యాంగ సవరణతో / Yes, with constitutional amendment",
     "b",
     "Art.214: ప్రతి రాష్ట్రానికి కేవలం ఒక్క HC మాత్రమే ఉంటుంది. రెండు రాష్ట్రాలకు ఒక్క HC ఉండవచ్చు (Art.231) కానీ ఒక రాష్ట్రానికి రెండు HCలు ఉండవు. / Art.214: One HC per state. Two states may share one HC (Art.231), but one state cannot have two HCs."),

    (7, "medium",
     "HC న్యాయమూర్తి పదవీ విరమణ తర్వాత ఏ న్యాయస్థానంలో వకీలు చేయలేరు? / After retirement, HC judge cannot practice in which court?",
     "ఏ కోర్టులోనూ చేయలేరు / Cannot practice in any court",
     "సొంత HC లో చేయలేరు / Cannot practice in own HC",
     "SC లో చేయలేరు / Cannot practice in SC",
     "ఏ ట్రిబ్యునల్‌లోనూ చేయలేరు / Cannot practice in any tribunal",
     "b",
     "Art.220: HC న్యాయమూర్తి పదవీ విరమణ తర్వాత తాను న్యాయమూర్తిగా పనిచేసిన HC లో వకీలు చేయలేరు — ఇతర HCలలో లేదా SC లో చేయవచ్చు. / Art.220: After retirement, HC judge cannot practice in that particular HC; can practice in SC or other HCs."),
]


def _seed_polity_ch21_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
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


def _seed_polity_ch21_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
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
