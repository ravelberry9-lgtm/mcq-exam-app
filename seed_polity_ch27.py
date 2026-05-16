# seed_polity_ch27.py
# Chapter 27 — Centre-State Relations (కేంద్ర-రాష్ట్ర సంబంధాలు)
# Total Sections: 8 | Total MCQs: 64
# Sections:
#   0 — Legislative Relations — Distribution of Powers (8 MCQs)
#   1 — Union List, State List, Concurrent List (8 MCQs)
#   2 — Parliamentary Legislation on State List (8 MCQs)
#   3 — Administrative Relations (8 MCQs)
#   4 — Financial Relations — Grants & Taxes (8 MCQs)
#   5 — Fiscal Federalism — Finance Commission (8 MCQs)
#   6 — Sarkaria & Punchhi Commission (8 MCQs)
#   7 — Cooperative Federalism & NITI Aayog (8 MCQs)

_CH = 27
_SUBJECT = 'GK'
_TOPIC   = 'Indian_Polity'
_TITLE_TE = 'కేంద్ర-రాష్ట్ర సంబంధాలు'
_TITLE_EN = 'Centre-State Relations'
_PAGES    = 'Ch.27 (Lakshmikanth)'

_SECTIONS = [
    "శాసన సంబంధాలు — అధికారాల విభజన",
    "కేంద్ర జాబితా, రాష్ట్ర జాబితా, ఉమ్మడి జాబితా",
    "రాష్ట్ర జాబితాపై పార్లమెంట్ చట్టాలు",
    "పరిపాలనా సంబంధాలు",
    "ఆర్థిక సంబంధాలు — గ్రాంట్లు & పన్నులు",
    "ఆర్థిక సమాఖ్యవాదం — ఆర్థిక సంఘం",
    "సర్కారియా & పంచి కమిషన్",
    "సహకార సమాఖ్యవాదం & NITI Aayog",
]

_MCQS = [
    # ── Section 0: Legislative Relations — Distribution of Powers ──────────────
    (0, "easy",
     "భారత రాజ్యాంగంలో అధికారాల విభజనను ఏ Article నిర్వచిస్తుంది? / Distribution of powers in Indian Constitution?",
     "Art.245–255",
     "Art.256–263",
     "Art.280–290",
     "Art.300–310",
     "a",
     "Art.245–255 కేంద్ర-రాష్ట్ర శాసన సంబంధాలు నిర్వచిస్తాయి. Art.245 = Parliament మరియు State Legislature చట్టాలు చేసే విస్తీర్ణం. / Arts 245–255 govern Centre-State legislative relations. Art.245 defines territorial extent of legislation."),

    (0, "easy",
     "7వ Schedule లో ఎన్ని జాబితాలు ఉన్నాయి? / How many lists are in the 7th Schedule?",
     "2",
     "3",
     "4",
     "5",
     "b",
     "7వ Schedule లో 3 జాబితాలు: List I (Union List — 97 subjects), List II (State List — 66 subjects), List III (Concurrent List — 47 subjects). / 7th Schedule has 3 lists: Union (97), State (66), Concurrent (47)."),

    (0, "easy",
     "కేంద్ర జాబితా (Union List) లో ప్రస్తుతం ఎన్ని అంశాలు ఉన్నాయి? / How many subjects are currently in the Union List?",
     "97",
     "66",
     "47",
     "100",
     "a",
     "Union List (List I): 97 subjects (originally 97; 42nd Amendment తర్వాత కొన్ని changes జరిగాయి). State List: 66; Concurrent List: 52 (originally 47; 42nd Amendment 5 subjects State→Concurrent moved). / Union List: 97 subjects. State List: 66. Concurrent List: 52 (after 42nd Amendment)."),

    (0, "medium",
     "రాష్ట్ర జాబితా (State List) లో ప్రస్తుతం ఎన్ని అంశాలు ఉన్నాయి? / How many subjects in the State List?",
     "97",
     "66",
     "52",
     "47",
     "b",
     "State List (List II): 66 subjects. 42వ సవరణ 5 subjects ని State List నుండి Concurrent List కి మార్చింది (Education, Forests, Weights & Measures, Protection of wild animals, Administration of justice). / State List: 66. 42nd Amendment moved 5 subjects from State to Concurrent List."),

    (0, "medium",
     "ఉమ్మడి జాబితా (Concurrent List) పై చట్టాల మధ్య వైరుధ్యం వస్తే ఏమి జరుగుతుంది? / What happens when Central and State laws on Concurrent List conflict?",
     "రాష్ట్ర చట్టం అమలవుతుంది",
     "కేంద్ర చట్టం ప్రాధాన్యం పొందుతుంది (Art.254)",
     "Supreme Court నిర్ణయిస్తుంది",
     "రాష్ట్రపతి నిర్ణయిస్తారు",
     "b",
     "Art.254: Concurrent List పై Central మరియు State చట్టాలు వైరుధ్యంలో ఉంటే, Central చట్టం ప్రాధాన్యం (repugnancy doctrine). కానీ President assent పొందిన State law Central law ని override చేయగలదు. / Art.254: Central law prevails over State law on Concurrent List (repugnancy). Exception: state law with President's assent."),

    (0, "hard",
     "ఏ Schedule లో Union, State, Concurrent lists ఉన్నాయి? / Which Schedule contains the three lists?",
     "5వ Schedule",
     "6వ Schedule",
     "7వ Schedule",
     "9వ Schedule",
     "c",
     "7వ Schedule (Art.246) లో మూడు జాబితాలు ఉన్నాయి. 5వ Schedule = Tribal Areas (non-NE); 6వ Schedule = NE Tribal Areas; 9వ Schedule = Land Reform laws (judicial review నుండి రక్షణ). / 7th Schedule (Art.246) has the three lists. 5th Sch = tribal areas; 6th Sch = NE tribal areas; 9th Sch = land reform laws."),

    (0, "hard",
     "Residuary powers (అవశిష్ట అధికారాలు) ఎవరికి చెందుతాయి? / Residuary powers vest with?",
     "రాష్ట్రాలు",
     "కేంద్రం (Parliament)",
     "Concurrent List లో ఉంటాయి",
     "Supreme Court నిర్ణయిస్తుంది",
     "b",
     "Art.248: Residuary powers Parliament కి ఉంటాయి — ఏ List లో లేని విషయాలపై Parliament చట్టాలు చేయగలదు. ఇది USA మాదిరిగా కాదు (USA లో Residuary states కి). / Art.248: Residuary powers vest in Parliament (not states, unlike USA). Parliament can legislate on any subject not in any list."),

    (0, "toughest",
     "42వ రాజ్యాంగ సవరణ Concurrent List కి ఏ 5 అంశాలు జోడించింది? / 5 subjects moved from State to Concurrent List by 42nd Amendment?",
     "Agriculture, Forests, Education, Health, Police",
     "Education, Forests, Weights & Measures, Wild animals protection, Administration of Justice",
     "Police, Local Govt, PR, ULBs, Fisheries",
     "Mining, Irrigation, Land reform, Roads, Markets",
     "b",
     "42వ సవరణ 1976: 5 subjects State List నుండి Concurrent List కి: (1) Education, (2) Forests, (3) Weights & Measures, (4) Protection of wild animals & birds, (5) Administration of justice — constitution/organization of all courts except SC/HC. / 42nd Amendment moved 5 subjects to Concurrent List: Education, Forests, Weights & Measures, Protection of wild animals & birds, Administration of Justice."),

    # ── Section 1: Lists content ──────────────────────────────────────────────
    (1, "easy",
     "రక్షణ (Defence), విదేశీ వ్యవహారాలు (Foreign Affairs) ఏ జాబితాలో ఉన్నాయి? / Defence and Foreign Affairs are in which list?",
     "State List",
     "Concurrent List",
     "Union List",
     "7వ Schedule లో లేవు",
     "c",
     "Defence (Entries 1-6), Foreign Affairs (Entry 10), Atomic Energy (Entry 7), Currency & Coinage (Entry 36) అన్నీ Union List లో ఉంటాయి. / Defence, Foreign Affairs, Atomic Energy, Currency — all in Union List (List I)."),

    (1, "easy",
     "Public Order (శాంతిభద్రతలు), Police ఏ జాబితాలో ఉన్నాయి? / Public Order and Police are in which list?",
     "Union List",
     "State List",
     "Concurrent List",
     "ఏ జాబితాలో లేవు",
     "b",
     "Public Order (Entry 1), Police (Entry 2), Land (Entry 18), Agriculture (Entry 14), Local Govt (Entry 5) అన్నీ State List లో ఉంటాయి. / Public Order (Entry 1), Police (Entry 2), Land (Entry 18), Agriculture — all in State List (List II)."),

    (1, "easy",
     "విద్య (Education) ఏ జాబితాలో ఉంది? / Education is in which list?",
     "Union List",
     "State List",
     "Concurrent List",
     "Residuary Powers",
     "c",
     "Education 42వ సవరణ 1976 తర్వాత Concurrent List కి మార్చబడింది — అంతకు ముందు State List లో ఉండేది. / Education moved from State List to Concurrent List by 42nd Amendment (1976). Before 1976 it was exclusively in State List."),

    (1, "medium",
     "అడవులు (Forests) ఏ జాబితాలో ఉన్నాయి? / Forests are in which list?",
     "Union List",
     "State List",
     "Concurrent List",
     "Residuary",
     "c",
     "Forests కూడా 42వ సవరణ 1976 తర్వాత Concurrent List కి మార్చబడింది. ఇంతకు ముందు State List లో ఉండేది. / Forests moved from State List to Concurrent List by 42nd Amendment (1976)."),

    (1, "medium",
     "Concurrent List లో ప్రస్తుతం ఎన్ని అంశాలు ఉన్నాయి? / How many subjects are currently in Concurrent List?",
     "47",
     "49",
     "52",
     "66",
     "c",
     "Concurrent List లో ప్రస్తుతం 52 అంశాలు (originally 47; 42వ సవరణ 5 State → Concurrent కి జోడించింది). / Concurrent List: originally 47; 42nd Amendment added 5 more from State List = 52 currently."),

    (1, "medium",
     "కింది వాటిలో Concurrent List కి చెందే అంశం ఏది? / Which of the following is in Concurrent List?",
     "Police",
     "Defence",
     "Criminal Law & Procedure",
     "Agriculture",
     "c",
     "Criminal Law (Entry 1) మరియు Criminal Procedure (Entry 2) Concurrent List లో ఉంటాయి. Police, Public Order = State List; Defence = Union List; Agriculture = State List. / Criminal Law & Procedure are in Concurrent List. Police/Agriculture = State List; Defence = Union List."),

    (1, "hard",
     "State List Entry 18 ఏమిటి? / What is State List Entry 18?",
     "Police",
     "Agriculture",
     "Land and land reforms",
     "Forests",
     "c",
     "State List Entry 18 = Land, that is to say, rights in or over land, land tenures including the relation of landlord and tenant, and the collection of rents; transfer and alienation of agricultural land; maintenance of land records; money-lending and money-lenders; relief of agricultural indebtedness. / Entry 18 = Land and land-related rights."),

    (1, "toughest",
     "కింది వాటిలో Union List కి చెందే అంశం ఏది? / Which subject belongs to the Union List?",
     "Local Government",
     "Inter-state rivers and river valleys",
     "Agriculture",
     "Fisheries",
     "b",
     "Inter-state rivers and river valleys (Union List Entry 56) = కేంద్రం పరిధి. Local Government, Agriculture, Fisheries = State List. / Inter-state rivers and river valleys: Union List Entry 56. (Local Govt/Agriculture/Fisheries = State List)."),

    # ── Section 2: Parliament Legislating on State List ──────────────────────
    (2, "easy",
     "జాతీయ ప్రయోజనం పేరుతో Parliament ఏ Article కింద State List పై చట్టాలు చేయగలదు? / Under which Article can Parliament legislate on State List in national interest?",
     "Art.249",
     "Art.252",
     "Art.253",
     "Art.256",
     "a",
     "Art.249: Rajya Sabha 2/3 మెజారిటీతో 'national interest' తీర్మానం ఆమోదిస్తే, Parliament State List విషయంపై చట్టాలు చేయగలదు — 1 సంవత్సరం వరకు. / Art.249: If Rajya Sabha passes resolution by 2/3 majority in national interest, Parliament can legislate on State List (valid for 1 year, extendable)."),

    (2, "easy",
     "రాష్ట్రపతి పాలన అమలులో ఉన్నప్పుడు Parliament ఏ Article కింద State List పై చట్టాలు చేయగలదు? / During President's Rule Parliament can legislate on State List under?",
     "Art.249",
     "Art.250",
     "Art.252",
     "Art.253",
     "b",
     "Art.250: National Emergency (Art.352) అమలులో ఉన్నప్పుడు Parliament State List పై చట్టాలు చేయగలదు. Art.356 (President's Rule) లో కూడా వర్తిస్తుంది. / Art.250: During National Emergency, Parliament can legislate on State List matters."),

    (2, "medium",
     "రెండు లేదా అంతకంటే ఎక్కువ రాష్ట్రాలు అభ్యర్థిస్తే Parliament State List పై ఏ Article కింద చట్టాలు చేయగలదు? / Parliament can legislate on State List if 2 or more states request under?",
     "Art.249",
     "Art.250",
     "Art.252",
     "Art.253",
     "c",
     "Art.252: రెండు లేదా అంతకంటే ఎక్కువ రాష్ట్రాల Legislature లు తీర్మానం ఆమోదిస్తే, Parliament ఆ రాష్ట్రాలకు వర్తించే State List చట్టం చేయగలదు. / Art.252: Parliament can legislate for states on State List if 2 or more states pass resolutions requesting it."),

    (2, "medium",
     "అంతర్జాతీయ ఒప్పందాలు అమలు చేయడానికి Parliament State List పై ఏ Article కింద చట్టాలు చేయగలదు? / Parliament can implement international treaties on State List under?",
     "Art.249",
     "Art.251",
     "Art.252",
     "Art.253",
     "d",
     "Art.253: International treaties, agreements లేదా conventions అమలు కోసం Parliament State List పై కూడా చట్టాలు చేయగలదు — రాష్ట్రాల అనుమతి అవసరం లేదు. / Art.253: Parliament can legislate on any subject (including State List) to implement international treaties/agreements. No state consent required."),

    (2, "medium",
     "Art.249 కింద Rajya Sabha ఆమోదించిన 'national interest' తీర్మానం ఎంత కాలం అమలులో ఉంటుంది? / How long is the Rajya Sabha resolution under Art.249 valid?",
     "6 నెలలు",
     "1 సంవత్సరం (పొడిగించవచ్చు)",
     "2 సంవత్సరాలు",
     "3 సంవత్సరాలు",
     "b",
     "Art.249 కింద Rajya Sabha తీర్మానం 1 సంవత్సరం వర్తిస్తుంది. తిరిగి తీర్మానం ఆమోదించడం ద్వారా పొడిగించవచ్చు (ప్రతి 1 సంవత్సరానికి). / Art.249 resolution is valid for 1 year (extendable by re-passing resolution each year)."),

    (2, "hard",
     "Art.256 కేంద్ర-రాష్ట్ర సంబంధాల్లో ఏమి నిర్దేశిస్తుంది? / What does Art.256 prescribe for Centre-State relations?",
     "నిధుల పంపిణీ",
     "రాష్ట్రాలు కేంద్రం చట్టాలు అమలు చేయాలి; కేంద్రం ఆదేశాలు ఇవ్వగలదు",
     "అంతర్రాష్ట్ర వ్యాపారం నిబంధనలు",
     "రాష్ట్ర న్యాయమూర్తుల నియామకం",
     "b",
     "Art.256: రాష్ట్రాల executive power ఏ విధంగా కేంద్ర చట్టాలు పాటించేలా వినియోగించాలి. కేంద్రం రాష్ట్రాలకు ఆదేశాలు ఇవ్వగలదు. / Art.256: State executive power shall be exercised so as to ensure compliance with central laws. Centre can give directions to states."),

    (2, "hard",
     "Art.254(2) కింద రాష్ట్ర చట్టం Central చట్టాన్ని override చేయగలదా? / Can a state law override central law under Art.254(2)?",
     "కేవలం Rajya Sabha ఆమోదంతో",
     "అవును — రాష్ట్రపతి assent పొందితే",
     "కేవలం Concurrent List అంశాలపై మాత్రమే",
     "కాదు — ఎప్పటికీ కాదు",
     "b",
     "Art.254(2): Concurrent List పై State law కి రాష్ట్రపతి assent వస్తే, ఆ రాష్ట్రంలో State law Central law ని override చేయగలదు. కానీ Parliament తర్వాత ఆ law రద్దు చేయగలదు. / Art.254(2): State law on Concurrent List with President's assent prevails over central law in that state. But Parliament can later override it."),

    (2, "toughest",
     "Art.246A (101వ సవరణ 2016) దేనికి సంబంధించింది? / Art.246A (inserted by 101st Amendment 2016) relates to?",
     "Education",
     "GST — Goods and Services Tax",
     "Inter-State rivers",
     "Atomic energy",
     "b",
     "Art.246A (101వ సవరణ 2016 — GST): Parliament మరియు State Legislature లు రెండూ GST విధించే అధికారం. ఇది Concurrent List కి భిన్నమైన ప్రత్యేక నిబంధన. / Art.246A (101st Amendment 2016): Both Parliament and State Legislature can make laws on GST — special provision for Goods and Services Tax."),

    # ── Section 3: Administrative Relations ──────────────────────────────────
    (3, "easy",
     "కేంద్ర-రాష్ట్ర పరిపాలనా సంబంధాలను ఏ Articles నిర్వచిస్తాయి? / Administrative relations between Centre and States are in?",
     "Art.245–255",
     "Art.256–263",
     "Art.264–280",
     "Art.300–315",
     "b",
     "Art.256–263 కేంద్ర-రాష్ట్ర పరిపాలనా సంబంధాలు నిర్వచిస్తాయి. Art.256 = compliance with central laws; Art.257 = infrastructure protection; Art.261 = Full Faith and Credit; Art.262 = water disputes; Art.263 = Inter-State Council. / Arts 256–263 cover administrative relations."),

    (3, "easy",
     "కేంద్రం రాష్ట్రాలకు Executive directions ఇవ్వడానికి ఏ Article అనుమతిస్తుంది? / Which Article allows Centre to give executive directions to states?",
     "Art.255",
     "Art.256",
     "Art.257",
     "Art.263",
     "b",
     "Art.256: రాష్ట్రాలు Central laws ని పాటించేలా వారి executive power వినియోగించాలి. కేంద్రం ఆదేశాలు (directions) ఇవ్వగలదు. రాజ్యాంగంలో భాగంగా ఇది ఒక Quasi-federal లక్షణం. / Art.256: States must exercise their executive power in compliance with central laws. Centre can give directions."),

    (3, "medium",
     "కేంద్రం రాష్ట్ర Government అధికారులను తమ సేవలకు ఉపయోగించుకోవచ్చా? / Can the Centre use state government officials for its work?",
     "కాదు — ఎప్పటికీ",
     "అవును — Art.258 కింద",
     "కేవలం Emergency లో",
     "President ఆమోదంతో మాత్రమే",
     "b",
     "Art.258: కేంద్రం తన అధికారాలను రాష్ట్రాలకు delegate చేయగలదు; రాష్ట్ర అధికారులు కేంద్రం పని చేయవచ్చు. Art.258A: రాష్ట్రాలు తమ అధికారాలను కేంద్రానికి delegate చేయవచ్చు. / Art.258: Centre can confer powers/functions on state officers. Art.258A: States can entrust functions to the Centre (with consent)."),

    (3, "medium",
     "All India Services (IAS, IPS, IFS) ని ఏ Article నిర్వచిస్తుంది? / All India Services are defined under which Article?",
     "Art.308",
     "Art.312",
     "Art.315",
     "Art.320",
     "b",
     "Art.312: Rajya Sabha 2/3 మెజారిటీ తీర్మానంతో Parliament All India Services సృష్టించగలదు. IAS, IPS, IFoS (Indian Forest Service) = ప్రస్తుత AIS. / Art.312: Parliament can create All India Services if Rajya Sabha passes a resolution by 2/3 majority. Currently: IAS, IPS, IFoS."),

    (3, "medium",
     "కేంద్రం రాష్ట్ర రహదారులపై Military purposes కోసం ఆదేశాలు ఇవ్వడానికి ఏ Article అనుమతిస్తుంది? / Which Article allows Centre to give directions on state highways for military purposes?",
     "Art.256",
     "Art.257",
     "Art.258",
     "Art.260",
     "b",
     "Art.257(2): రాష్ట్రం తన executive power ఏ విధంగా వినియోగించాలో కేంద్రం ఆదేశాలు ఇవ్వగలదు — National Highways, military communication రక్షణకు సంబంధించి. / Art.257(2): Centre can give directions to states for protection of railways and national highways in the state."),

    (3, "hard",
     "Art.261 Full Faith and Credit Rule ఏమి నిర్దేశిస్తుంది? / What does Art.261 Full Faith and Credit prescribe?",
     "రాష్ట్రాలు కేంద్రం Revenue వసూలు చేయాలి",
     "భారతదేశంలో అన్ని చోట్లా Public Acts, Records, Judicial proceedings కి విశ్వాసం & గౌరవం ఉండాలి",
     "Courts రాష్ట్ర న్యాయాన్ని follow చేయాలి",
     "Forests రక్షణ",
     "b",
     "Art.261: Full Faith and Credit Rule — భారతదేశంలోని అన్ని ప్రాంతాల్లో Public Acts, Records, Judicial proceedings కి పూర్తి విశ్వాసం & గౌరవం ఉండాలి. ఇది USA Constitution కి సారూప్యంగా ఉంది. / Art.261: Full Faith and Credit — public acts, records & judicial proceedings of every state shall have full faith across India (similar to USA Art.IV Sec.1)."),

    (3, "hard",
     "Governor కి రాష్ట్రం తరఫున కేంద్రానికి Agent గా వ్యవహరించే అధికారం ఉందా? / Can the Governor act as an Agent of the Centre?",
     "కాదు — Governor రాష్ట్రానికి మాత్రమే",
     "అవును — Art.258A కింద",
     "అవును — Art.239A కింద",
     "కేవలం Emergency లో",
     "b",
     "Art.258A కింద రాష్ట్ర ప్రభుత్వం (Governor) కేంద్ర ప్రభుత్వానికి functions entrust చేసే అవకాశం ఉంది. Governor ని 'Agent of the Centre' అని చెప్పడం కూడా సరైనదే — Central law admin కోసం. / Art.258A: States can entrust functions to the Centre. Governor also acts as Centre's agent in certain matters (e.g., when President's rule is imposed, Governor acts for the Centre)."),

    (3, "toughest",
     "Cooperative Federalism యొక్క ముఖ్య లక్షణం ఏమిటి? / Key feature of Cooperative Federalism?",
     "రాష్ట్రాల సంపూర్ణ స్వాతంత్ర్యం",
     "కేంద్రం రాష్ట్రాలపై ఆధిపత్యం",
     "కేంద్రం మరియు రాష్ట్రాలు సహకారంతో పని చేయడం — రాష్ట్రాలు 'partners'",
     "రాష్ట్రాలు కేంద్రానికి తాబేదారులు",
     "c",
     "Cooperative Federalism: కేంద్రం మరియు రాష్ట్రాలు సమాన భాగస్వాములుగా (equal partners) అభివృద్ధి కోసం సహకరించడం. NITI Aayog ఈ దృక్పధాన్ని ప్రమోట్ చేస్తుంది. SR Bommai కేసు: Federalism = Basic Structure. / Cooperative Federalism: Centre & states as equal partners for development — NITI Aayog's philosophy. SR Bommai: Federalism is a Basic Structure."),

    # ── Section 4: Financial Relations ───────────────────────────────────────
    (4, "easy",
     "కేంద్ర-రాష్ట్ర ఆర్థిక సంబంధాలను ఏ Articles నిర్వచిస్తాయి? / Financial relations are in which Articles?",
     "Art.256–263",
     "Art.264–293",
     "Art.300–330",
     "Art.330–342",
     "b",
     "Art.264–293 కేంద్ర-రాష్ట్ర ఆర్థిక సంబంధాలు నిర్వచిస్తాయి. పన్నులు, Grants, Finance Commission, Borrowing అన్నీ ఇందులో ఉంటాయి. / Arts 264–293 cover financial relations: taxes, grants, Finance Commission, borrowing."),

    (4, "easy",
     "Income Tax వసూలు ఎవరు చేస్తారు? రాష్ట్రాలకు ఎంత వాటా వస్తుంది? / Who collects Income Tax and shares it with states?",
     "రాష్ట్రాలు వసూలు చేస్తాయి; కేంద్రం తీసుకుంటుంది",
     "కేంద్రం వసూలు చేస్తుంది; Finance Commission నిర్దేశించిన నిష్పత్తిలో రాష్ట్రాలకు పంచుతుంది",
     "కేంద్రం వసూలు చేస్తుంది; రాష్ట్రాలకు ఇవ్వదు",
     "రాష్ట్రాలు వసూలు చేస్తాయి; కేంద్రానికి ఇస్తాయి",
     "b",
     "Income Tax కేంద్రం వసూలు చేస్తుంది (Union List Entry 82). రాష్ట్రాలకు వాటా Finance Commission నిర్దేశించిన నిష్పత్తిలో ఉంటుంది. Art.270 = Taxes shared between Centre & States. / Income Tax: collected by Centre (Union List Entry 82); distributed to states as per Finance Commission's formula under Art.270."),

    (4, "medium",
     "రాష్ట్రాలు మాత్రమే వసూలు చేయగలిగే ముఖ్యమైన పన్ను ఏది? / Important tax that only states can levy?",
     "Income Tax",
     "Customs Duty",
     "Land Revenue",
     "Corporation Tax",
     "c",
     "Land Revenue (State List Entry 45) రాష్ట్రాలు మాత్రమే వసూలు చేస్తాయి. ఇతర: Sales Tax (కానీ ఇప్పుడు GST లో భాగం), State Excise, Stamp Duty (except commercial bills). / Land Revenue is exclusively a state tax. Other state taxes: state excise on alcohol, stamp duty (except commercial papers), etc."),

    (4, "medium",
     "Art.275 కింద ప్రత్యేక Grants ఏ రాష్ట్రాలకు ఇవ్వబడతాయి? / Grants under Art.275 are for which purpose?",
     "అన్ని రాష్ట్రాలకు సమానంగా",
     "ప్రాంతీయ అభివృద్ధికి మాత్రమే",
     "Scheduled Tribes అభివృద్ధి & Scheduled Areas administration కోసం",
     "రక్షణ అవసరాల కోసం",
     "c",
     "Art.275: Parliament Scheduled Tribes welfare మరియు Scheduled Areas administration కోసం ప్రత్యేక grants (రాష్ట్రాలకు) ఇవ్వగలదు. 42వ సవరణ: Panchayats కు కూడా. / Art.275: Parliament may grant sums to states for promotion of welfare of Scheduled Tribes and Scheduled Areas administration."),

    (4, "hard",
     "రాష్ట్రాలు బయటి రుణాలు తీసుకోవడానికి ఎవరి అనుమతి అవసరం? / States need whose permission to borrow from external sources?",
     "Finance Commission",
     "Parliament",
     "కేంద్ర ప్రభుత్వం (Art.293)",
     "Reserve Bank of India",
     "c",
     "Art.293: రాష్ట్రాలు Indian territory లో మాత్రమే రుణాలు తీసుకోగలవు. కేంద్రానికి రాష్ట్రంపై outstanding loan ఉంటే, రాష్ట్రం మరింత రుణం తీసుకోవడానికి కేంద్రం అనుమతి అవసరం. / Art.293: States can borrow only within India. If Centre has outstanding loan on a state, the state needs Centre's consent for further borrowing."),

    (4, "hard",
     "Art.282 కింద Discretionary Grants ఎవరు ఇవ్వగలరు? / Discretionary grants under Art.282 can be given by?",
     "కేవలం రాష్ట్రపతి",
     "కేంద్రం లేదా రాష్ట్రాలు రెండూ — ఏ Public Purpose కోసమైనా",
     "కేవలం Finance Commission సిఫారసుపై",
     "కేవలం Scheduled Tribes welfare కోసం",
     "b",
     "Art.282: కేంద్రం లేదా రాష్ట్రాలు రెండూ ఏ Public Purpose కోసమైనా Discretionary grants ఇవ్వగలవు — Finance Commission సిఫారసు అవసరం లేదు. / Art.282: Both Centre and states can make grants for any public purpose, without Finance Commission recommendation."),

    (4, "toughest",
     "GST లో రాష్ట్రాల నష్టాన్ని భర్తీ చేయడానికి ఏ నిబంధన ఉంది? / What provision compensates states for GST losses?",
     "Art.269A",
     "Art.270",
     "Art.246A",
     "Art.279A",
     "d",
     "Art.279A (101వ సవరణ): GST Council ఏర్పాటు. Art.246A: Parliament + States = dual power on GST. Art.269A: Interstate trade & commerce GST కేంద్రం వసూలు చేసి రాష్ట్రాలకు పంచుతుంది. GST Compensation Act 2017: 5 సంవత్సరాలు రాష్ట్రాల నష్టం భర్తీ. / Art.279A: GST Council. Art.246A: concurrent GST powers. Art.269A: inter-state GST collected by Centre and divided."),

    (4, "medium",
     "Art.360 Financial Emergency లో రాష్ట్ర సేవకుల జీతాలపై కేంద్రానికి ఏ అధికారం ఉంటుంది? / Under Art.360 Financial Emergency, Centre can?",
     "రాష్ట్ర సేవకుల జీతాలు తగ్గించవచ్చు",
     "రాష్ట్ర బడ్జెట్ రద్దు చేయవచ్చు",
     "రాష్ట్రాల పన్ను అధికారాలు రద్దు చేయవచ్చు",
     "Consolidated Fund of India లో కలిపేయవచ్చు",
     "a",
     "Art.360 Financial Emergency లో President రాష్ట్ర, కేంద్ర సేవకుల జీతాలు తగ్గించవచ్చు. రాష్ట్రాల Money Bills రాష్ట్రపతి ఆమోదం కోసం reserve చేయాలి. ఇప్పటి వరకు Financial Emergency ఒక్కసారి కూడా ప్రకటించబడలేదు. / Art.360: President can reduce salaries of state/central employees; state Money Bills reserved for President. Never proclaimed so far."),

    # ── Section 5: Finance Commission ────────────────────────────────────────
    (5, "easy",
     "Finance Commission ని ఏ Article నిర్వచిస్తుంది? / Finance Commission is defined in which Article?",
     "Art.263",
     "Art.270",
     "Art.280",
     "Art.312",
     "c",
     "Art.280 Finance Commission నిర్వచిస్తుంది. రాష్ట్రపతి ప్రతి 5 సంవత్సరాలకు Finance Commission నియమిస్తారు. కేంద్ర-రాష్ట్రాల మధ్య పన్నుల పంపిణీ, Grants సిఫారసులు ఇస్తుంది. / Art.280: Finance Commission — appointed by President every 5 years to recommend distribution of taxes between Centre and states."),

    (5, "easy",
     "Finance Commission ఎంత కాలానికి ఒకసారి నియమించబడుతుంది? / Finance Commission is appointed every?",
     "3 సంవత్సరాలు",
     "4 సంవత్సరాలు",
     "5 సంవత్సరాలు",
     "10 సంవత్సరాలు",
     "c",
     "Art.280(1): రాష్ట్రపతి Finance Commission ని ప్రతి 5 సంవత్సరాలకు నియమిస్తారు (or such earlier time). 16వ Finance Commission 2026–2031 కాలానికి నియమించబడింది. / Art.280: President appoints Finance Commission every 5 years. 16th FC is for 2026–2031."),

    (5, "medium",
     "Finance Commission లో ఎంత మంది సభ్యులు ఉంటారు? / Finance Commission consists of?",
     "1 Chairman + 3 Members",
     "1 Chairman + 4 Members",
     "1 Chairman + 5 Members",
     "3 Members (no Chairman)",
     "b",
     "Art.280(1): Finance Commission = 1 Chairman + 4 Members, రాష్ట్రపతి నియమిస్తారు. Chairman అర్హత: Public affairs లో అనుభవం. / Art.280: Finance Commission = 1 Chairman + 4 members appointed by President. Chairman: person with wide experience in public affairs."),

    (5, "medium",
     "Finance Commission యొక్క ప్రాథమిక విధి ఏమిటి? / Primary function of Finance Commission?",
     "కేంద్ర బడ్జెట్ తయారు చేయడం",
     "Union & State Tax revenues పంపిణీ సిఫారసులు",
     "విదేశీ రుణాలు నిర్ణయించడం",
     "పంచవర్ష ప్రణాళిక రూపకల్పన",
     "b",
     "Art.280(3): Finance Commission సిఫారసులు: (a) Tax revenue పంపిణీ Centre-States మధ్య; (b) Art.275 grants; (c) Consolidated Fund of State లో finance అభివృద్ధి. / Finance Commission recommends: (a) distribution of tax revenues; (b) grants to states; (c) finance of states' Consolidated Funds."),

    (5, "medium",
     "15వ Finance Commission ఏ కాలానికి? / 15th Finance Commission covered which period?",
     "2015–20",
     "2020–25",
     "2016–21",
     "2021–26",
     "b",
     "15వ Finance Commission (Chairman: N.K. Singh) 2020–25 కాలానికి నియమించబడింది. రాష్ట్రాల vertical share: 41% (14th FC లో 42% ఉండేది — J&K రాష్ట్రం UT అవడంతో 1% తగ్గింది). / 15th Finance Commission (NK Singh): 2020–25. States' share: 41% (down from 42% in 14th FC due to J&K becoming UT)."),

    (5, "hard",
     "Consolidated Fund of India (CFI) ఏ Article కింద నిర్వచించబడింది? / Consolidated Fund of India is defined in?",
     "Art.264",
     "Art.266",
     "Art.267",
     "Art.280",
     "b",
     "Art.266(1) = Consolidated Fund of India (CFI) — అన్ని tax revenues, loans జమ అవుతాయి; Parliament ఆమోదంతో మాత్రమే వ్యయం. Art.266(2) = Consolidated Fund of State. Art.267 = Contingency Fund. / Art.266(1) = Consolidated Fund of India; Art.267 = Contingency Fund (at President's disposal for urgent expenditure)."),

    (5, "hard",
     "Charged Expenditure అంటే ఏమిటి? / What is Charged Expenditure?",
     "Parliament ఆమోదం అవసరమైన వ్యయం",
     "Parliament ఓటింగ్ అవసరం లేకుండా CFI నుండి చెల్లించబడే వ్యయం",
     "రాష్ట్రాలకు Grants",
     "Finance Commission సిఫారసు చేసిన వ్యయం",
     "b",
     "Charged Expenditure = Art.112(3) కింద CFI నుండి Parliament ఓటు లేకుండా చెల్లించబడే వ్యయం. ఉదా: President వేతనం, SC న్యాయమూర్తుల వేతనాలు, రుణ వడ్డీలు, CAG వేతనం. / Charged Expenditure: paid from CFI without Parliament's vote (Art.112(3)). Examples: President's salary, SC judges' salaries, loan interest, CAG salary."),

    (5, "toughest",
     "GST Compensation Fund ఎంత కాలానికి అమలులో ఉంది? / GST Compensation Fund was effective for?",
     "3 సంవత్సరాలు",
     "5 సంవత్సరాలు",
     "7 సంవత్సరాలు",
     "10 సంవత్సరాలు",
     "b",
     "GST (Compensation to States) Act 2017 ప్రకారం రాష్ట్రాలకు GST నష్టాల భర్తీ 5 సంవత్సరాల పాటు (2017–2022) అందజేయబడింది. తర్వాత postponed చేశారు. / GST Compensation to states was provided for 5 years (2017–2022) under GST (Compensation to States) Act 2017."),

    # ── Section 6: Sarkaria & Punchhi Commission ──────────────────────────────
    (6, "easy",
     "Sarkaria Commission ఏ విషయాన్ని పరిశీలించింది? / Sarkaria Commission examined which issue?",
     "Election reforms",
     "కేంద్ర-రాష్ట్ర సంబంధాలు / Centre-State Relations",
     "Panchayati Raj strengthening",
     "Constitutional Amendments",
     "b",
     "Sarkaria Commission (1983, Chairman: R.S. Sarkaria) కేంద్ర-రాష్ట్ర సంబంధాలను పరిశీలించి 1988లో నివేదిక ఇచ్చింది. Inter-State Council ఏర్పాటు సిఫారసు ముఖ్యమైనది. / Sarkaria Commission (1983, Chairman: R.S. Sarkaria) examined Centre-State relations; submitted report in 1988. Recommended Inter-State Council."),

    (6, "easy",
     "Sarkaria Commission ఏ సంవత్సరం ఏర్పాటైంది? / Sarkaria Commission was set up in?",
     "1977",
     "1980",
     "1983",
     "1990",
     "c",
     "Sarkaria Commission జూన్ 1983లో Indira Gandhi ప్రభుత్వం ఏర్పాటు చేసింది. 1988లో నివేదిక సమర్పించింది. / Sarkaria Commission set up in June 1983 by Indira Gandhi government; submitted report in 1988."),

    (6, "medium",
     "Sarkaria Commission ముఖ్య సిఫారసు ఏమిటి? / Key recommendation of Sarkaria Commission?",
     "రాష్ట్రాలకు అధిక అధికారాలు ఇవ్వాలి",
     "Inter-State Council ఏర్పాటు",
     "Finance Commission రద్దు",
     "Planning Commission బలోపేతం",
     "b",
     "Sarkaria Commission యొక్క ముఖ్య సిఫారసు: Art.263 కింద Permanent Inter-State Council (ISC) ఏర్పాటు — ఇది 1990లో Janata Dal ప్రభుత్వంలో స్థాపించబడింది. / Sarkaria Commission's key recommendation: set up a permanent Inter-State Council under Art.263 — implemented in 1990."),

    (6, "medium",
     "Punchhi Commission ఏ సంవత్సరం ఏర్పాటైంది? / Punchhi Commission was set up in?",
     "2000",
     "2005",
     "2007",
     "2010",
     "c",
     "Punchhi Commission (Chairman: M.M. Punchhi, former CJI) 2007లో ఏర్పాటైంది; 2010లో నివేదిక ఇచ్చింది. Sarkaria Commission తర్వాత Centre-State relations పై రెండవ ముఖ్య కమిషన్. / Punchhi Commission (former CJI M.M. Punchhi) set up in 2007; submitted report in 2010. Second major commission on Centre-State relations after Sarkaria."),

    (6, "medium",
     "Sarkaria Commission కింది వాటిలో ఏ అంశంపై Governor విషయంలో ముఖ్య సిఫారసు చేసింది? / Sarkaria Commission's key recommendation on Governor?",
     "Governor పదవీకాలం 3 సంవత్సరాలుగా నిర్ణయించాలి",
     "Governor ఆ రాష్ట్రంలో ఏ రాజకీయ కార్యకలాపాలు నిర్వహించని వ్యక్తిగా ఉండాలి",
     "Governors రాష్ట్రపతి నేరుగా నియమించకూడదు",
     "Governor CM సలహాపై పని చేయాలి మాత్రమే",
     "b",
     "Sarkaria Commission: Governor ఆ రాష్ట్రంలో ఇటీవల రాజకీయ కార్యకలాపాలు నిర్వహించని ఒక 'detached' వ్యక్తి అయి ఉండాలి. / Sarkaria Commission: Governor should be a person who has not taken part in state politics recently — an 'eminent, detached' person."),

    (6, "hard",
     "Sarkaria Commission Art.356 (President's Rule) కి సంబంధించి ఏ ముఖ్య సిఫారసు చేసింది? / Sarkaria Commission's key recommendation on Art.356?",
     "Art.356 రద్దు చేయాలి",
     "Art.356 'last resort' గా మాత్రమే ఉపయోగించాలి",
     "Art.356 కి Parliament Special Majority అవసరం",
     "Art.356 కి Supreme Court అనుమతి తీసుకోవాలి",
     "b",
     "Sarkaria Commission: Art.356 (President's Rule) 'last resort' (చివరి మార్గం) గా మాత్రమే ఉపయోగించాలి; దాని దుర్వినియోగాన్ని అరికట్టాలి. SR Bommai కేసు (1994) దీనిని judicial support ఇచ్చింది. / Sarkaria Commission: Art.356 should be used only as a last resort. SR Bommai case gave this judicial endorsement."),

    (6, "hard",
     "Punchhi Commission యొక్క ముఖ్య సిఫారసు ఏమిటి? / Key recommendation of Punchhi Commission?",
     "Planning Commission రద్దు",
     "Governor తొలగింపు విధానం: Impeachment ద్వారా",
     "All India Services రద్దు",
     "Rajya Sabha రద్దు",
     "b",
     "Punchhi Commission: Governor తొలగింపు విధానం మార్చాలి — 5 సంవత్సరాల నిర్ణీత పదవీకాలం ఉండాలి; తొలగింపుకు Impeachment విధానం ఉండాలి. / Punchhi Commission recommended: Governor should have fixed tenure of 5 years; removal procedure similar to impeachment."),

    (6, "toughest",
     "Rajamannar Committee (1969) దేనికి సంబంధించింది? / Rajamannar Committee (1969) related to?",
     "Election reforms",
     "రాష్ట్రాలకు మరింత స్వయంప్రతిపత్తి — Centre-State relations review",
     "Panchayati Raj",
     "Language policy",
     "b",
     "Rajamannar Committee (1969, Tamil Nadu) Centre-State సంబంధాలను పరిశీలించి రాష్ట్రాలకు మరింత స్వయంప్రతిపత్తి ఇవ్వాలని సిఫారసు చేసింది. ఇది Sarkaria Commission కి ముందే Centre-State relations మీద పని చేసింది. / Rajamannar Committee (1969, Tamil Nadu): Reviewed Centre-State relations and recommended greater autonomy to states — precursor to Sarkaria Commission."),

    # ── Section 7: Cooperative Federalism & NITI Aayog ───────────────────────
    (7, "easy",
     "Competitive Federalism భావన ఏ సంస్థ ప్రవేశపెట్టింది? / Competitive Federalism concept was introduced by?",
     "Planning Commission",
     "NITI Aayog",
     "Finance Commission",
     "Inter-State Council",
     "b",
     "NITI Aayog 'Competitive Federalism' అనే భావనను ప్రవేశపెట్టింది — రాష్ట్రాలు అభివృద్ధి సూచికలలో పోటీపడాలి; Ease of Doing Business Rankings వంటివి. / NITI Aayog introduced 'Competitive Federalism' — states compete on development indicators like Ease of Doing Business, Health Index, etc."),

    (7, "easy",
     "GST Council నిర్ణయాలకు ఎంత Weighted majority అవసరం? / What weighted majority is required for GST Council decisions?",
     "1/2 (50%)",
     "2/3 (66.67%)",
     "3/4 (75%)",
     "1/3 (33.33%)",
     "c",
     "GST Council (Art.279A) నిర్ణయాలకు కనీసం 3/4 (75%) weighted majority అవసరం. Voting weight: కేంద్రానికి 1/3; అన్ని రాష్ట్రాలకు కలిసి 2/3. / GST Council decisions require at least 3/4 weighted majority. Voting: Centre = 1/3; states collectively = 2/3."),

    (7, "medium",
     "Fiscal Federalism యొక్క ముఖ్య లక్షణం ఏమిటి? / Key feature of Fiscal Federalism?",
     "రాష్ట్రాలు అన్ని పన్నులు నిర్ణయిస్తాయి",
     "కేంద్రం & రాష్ట్రాల మధ్య ఆర్థిక వనరుల రాజ్యాంగబద్ధ విభజన",
     "కేంద్రం మాత్రమే వ్యయం నిర్ణయిస్తుంది",
     "Finance Commission = supreme body",
     "b",
     "Fiscal Federalism: కేంద్రం & రాష్ట్రాల మధ్య ఆర్థిక వనరుల రాజ్యాంగబద్ధ పంపిణీ (taxation + expenditure). Finance Commission Tax Devolution నిర్ణయిస్తుంది. / Fiscal Federalism: constitutional division of financial resources between Centre and states (taxation + expenditure). Finance Commission determines tax devolution."),

    (7, "medium",
     "Inter-State Council ఏ సంవత్సరం ఏర్పాటైంది? / Inter-State Council was established in?",
     "1983",
     "1988",
     "1990",
     "1995",
     "c",
     "Inter-State Council Art.263 కింద 1990లో V.P. Singh ప్రభుత్వంలో ఏర్పాటైంది — Sarkaria Commission సిఫారసు మేరకు. PM అధ్యక్షుడు; అన్ని రాష్ట్రాల CM సభ్యులు. / Inter-State Council (Art.263) established in 1990 (VP Singh govt) on Sarkaria Commission's recommendation. Chaired by PM."),

    (7, "medium",
     "Centre-State relations పరంగా భారత రాజ్యాంగ స్వభావం ఏమిటి? / Character of Indian Constitution in Centre-State relations?",
     "Federal",
     "Unitary",
     "Quasi-federal — సమయాన్ని బట్టి Unitary లేదా Federal",
     "Confederation",
     "c",
     "భారత రాజ్యాంగం 'Quasi-federal' లేదా 'Federal with unitary bias' (K.C. Wheare వ్యాఖ్య). సాధారణంగా Federal; అవసరమైనప్పుడు Unitary గా పని చేస్తుంది. / India's constitution is 'Quasi-federal' or 'Federal with unitary bias' (K.C. Wheare). Federal in normal times, unitary in emergencies."),

    (7, "hard",
     "Art.263 కింద రాష్ట్రపతి ఏ సంస్థను ఏర్పాటు చేయగలరు? / President can establish which body under Art.263?",
     "Finance Commission",
     "Planning Commission",
     "Inter-State Council",
     "Zonal Councils",
     "c",
     "Art.263: రాష్ట్రాల మధ్య వివాదాల పరిష్కారానికి, రాష్ట్రాలకు నిర్దిష్ట ప్రయోజనకరమైన విషయాలపై సమన్వయానికి President ఒక Council ఏర్పాటు చేయగలరు — ఇది Inter-State Council. / Art.263: President may establish a council (Inter-State Council) for inquiry into disputes between states and coordinating policies."),

    (7, "hard",
     "India లో Centre-State సంబంధాలను 'Cooperative Federalism' అని ఎవరు అభివర్ణించారు? / Who described India's Centre-State relations as 'Cooperative Federalism'?",
     "B.R. Ambedkar",
     "Jawaharlal Nehru",
     "Granville Austin",
     "K.C. Wheare",
     "c",
     "Granville Austin భారత రాజ్యాంగాన్ని 'Cooperative Federalism' అని అభివర్ణించారు తన పుస్తకం 'The Indian Constitution: Cornerstone of a Nation' లో. / Granville Austin described India's constitution as a 'cooperative federalism' in his book 'The Indian Constitution: Cornerstone of a Nation'."),

    (7, "toughest",
     "Art.355 కేంద్ర-రాష్ట్ర సంబంధాల్లో ఏమి నిర్దేశిస్తుంది? / What does Art.355 prescribe in Centre-State relations?",
     "Finance Commission నియామకం",
     "కేంద్రం రాష్ట్రాలను బాహ్య దురాక్రమణ & అంతర్గత అలజడుల నుండి రక్షించాలి",
     "రాష్ట్రాలు కేంద్ర మార్గదర్శకాలు పాటించాలి",
     "రాష్ట్రాల Governors నియామకం",
     "b",
     "Art.355: కేంద్రం 'duty': (1) రాష్ట్రాలను External aggression & Internal disturbance నుండి రక్షించడం; (2) రాష్ట్ర ప్రభుత్వాలు రాజ్యాంగ నిబంధనల ప్రకారం నడవడం నిర్ధారించడం. ఇది Art.356 కి prerequisite. / Art.355: Centre's duty to protect states from external aggression and internal disturbance, and to ensure State govt runs per Constitution — prerequisite for Art.356."),
]


# ── NOTES HTML ────────────────────────────────────────────────────────────────

NOTES_HTML = """<!DOCTYPE html>
<html lang="te">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ch27 – Centre-State Relations</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;600;700&family=Noto+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:'Noto Sans Telugu','Noto Sans',sans-serif;font-size:15px;line-height:1.6;background:#f5f5f5;color:#212121}
  .page{width:210mm;min-height:297mm;margin:0 auto 18px;background:#fff;padding:14mm 13mm 12mm;box-shadow:0 2px 8px rgba(0,0,0,.13)}
  .hdr{background:linear-gradient(135deg,#1a237e 0%,#283593 100%);color:#fff;border-radius:8px;padding:14px 18px 10px;margin-bottom:14px}
  .hdr h1{font-size:20px;font-weight:700;letter-spacing:.3px}
  .hdr h2{font-size:13px;font-weight:400;opacity:.88;margin-top:3px}
  .badge{display:inline-block;background:rgba(255,255,255,.2);border-radius:12px;padding:2px 10px;font-size:11.5px;margin-top:6px}
  .sh{font-size:14px;font-weight:700;color:#1a237e;background:#e8eaf6;border-left:5px solid #3949ab;border-radius:0 5px 5px 0;padding:5px 10px;margin:12px 0 7px}
  .c{border-radius:6px;padding:9px 12px;margin-bottom:7px;border:1px solid transparent}
  .c.r{background:#fff8f8;border-color:#ffcdd2}
  .c.b{background:#e8eaf6;border-color:#9fa8da}
  .c.a{background:#fff8e1;border-color:#ffe082}
  .c.p{background:#f3e5f5;border-color:#ce93d8}
  .c.g{background:#e8f5e9;border-color:#a5d6a7}
  .c.gr{background:#f5f5f5;border-color:#e0e0e0}
  .c.t{background:#e0f2f1;border-color:#80cbc4}
  .ch{font-size:13px;font-weight:700;color:#1a237e;border-bottom:1px solid #c5cae9;padding-bottom:4px;margin-bottom:5px}
  .fact{margin:3px 0;font-size:14.5px}
  .fact::before{content:"• ";color:#3949ab;font-weight:700}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:8px}
  table{width:100%;border-collapse:collapse;font-size:13px;margin-top:4px}
  th{background:#1a237e;color:#fff;padding:5px 8px;text-align:left}
  td{padding:4px 8px;border-bottom:1px solid #c5cae9}
  tr:nth-child(even) td{background:#f0f1fa}
  .pills{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
  .pill{background:#1a237e;color:#fff;border-radius:20px;padding:3px 12px;font-size:12.5px}
  .pill.o{background:#3949ab}
  .pill.b{background:#1565c0}
  .pill.g{background:#2e7d32}
  .pill.r{background:#c62828}
  .pill.p{background:#6a1b9a}
</style>
</head>
<body>

<!-- PAGE 1 -->
<div class="page">
<div class="hdr">
  <h1>Ch 27 — Centre-State Relations (కేంద్ర-రాష్ట్ర సంబంధాలు)</h1>
  <h2>శాసన • పరిపాలన • ఆర్థిక సంబంధాలు — Art.245–293</h2>
  <span class="badge">Indian Polity</span>
</div>

<div class="sh">⚖️ 1. శాసన సంబంధాలు — 7వ Schedule</div>
<table>
  <tr><th>జాబితా</th><th>సంఖ్య</th><th>ముఖ్య అంశాలు</th></tr>
  <tr><td>Union List (List I)</td><td>97</td><td>Defence, Foreign Affairs, Atomic Energy, Currency, Railways, Post &amp; Telegraph</td></tr>
  <tr><td>State List (List II)</td><td>66</td><td>Public Order, Police, Land, Agriculture, Local Govt, Forests (before 1976)</td></tr>
  <tr><td>Concurrent List (List III)</td><td>52</td><td>Criminal Law, Marriage, Education (after 1976), Forests (after 1976), Contracts</td></tr>
</table>
<div class="c a" style="margin-top:7px">
  <div class="fact">Art.246 — 7వ Schedule లో 3 Lists; Art.248 — Residuary powers = Parliament కి</div>
  <div class="fact">Art.254 — Concurrent List పై conflict: Central law wins; Exception: State law with President's assent</div>
  <div class="fact">42వ సవరణ 1976: Education, Forests, Weights &amp; Measures, Wild Animals Protection, Administration of Justice → State → Concurrent</div>
  <div class="fact">Art.246A (101వ సవరణ 2016): Parliament + State Legislature లు రెండూ GST విధించగలవు</div>
</div>

<div class="sh">📜 2. Parliament — State List పై చట్టాలు (5 సందర్భాలు)</div>
<table>
  <tr><th>Article</th><th>సందర్భం</th><th>Method</th><th>కాలవ్యవధి</th></tr>
  <tr><td>Art.249</td><td>National Interest</td><td>Rajya Sabha 2/3 తీర్మానం</td><td>1 సంవత్సరం (పొడిగించవచ్చు)</td></tr>
  <tr><td>Art.250</td><td>National Emergency (Art.352)</td><td>Emergency అమలులో ఉన్నప్పుడు</td><td>Emergency + 6 నెలలు</td></tr>
  <tr><td>Art.252</td><td>2+ States అభ్యర్థన</td><td>State Legislatures తీర్మానం</td><td>రాష్ట్రాలు రద్దు చేసే వరకు</td></tr>
  <tr><td>Art.253</td><td>International Treaties</td><td>Parliament నేరుగా</td><td>అనిశ్చిత కాలం</td></tr>
  <tr><td>Art.356</td><td>President's Rule (రాష్ట్రపతి పాలన)</td><td>President's Rule అమలులో</td><td>President's Rule + 6 నెలలు</td></tr>
</table>

<div class="sh">🔗 3. పరిపాలనా సంబంధాలు — Art.256–263</div>
<div class="two">
  <div class="c b">
    <div class="ch">కేంద్రం నుండి రాష్ట్రాలకు</div>
    <div class="fact">Art.256: రాష్ట్రాలు Central laws పాటించేలా executive power వినియోగించాలి</div>
    <div class="fact">Art.257: జాతీయ రహదారులు, రైల్వేలు రక్షణకు ఆదేశాలు</div>
    <div class="fact">Art.258: కేంద్రం రాష్ట్ర అధికారులకు functions delegate చేయగలదు</div>
    <div class="fact">Art.355: బాహ్య దురాక్రమణ, అంతర్గత అలజడి నుండి రాష్ట్రాలను రక్షించడం కేంద్రం duty</div>
  </div>
  <div class="c g">
    <div class="ch">రాష్ట్రాల నుండి కేంద్రానికి</div>
    <div class="fact">Art.258A: రాష్ట్రాలు కేంద్రానికి functions entrust చేయవచ్చు</div>
    <div class="fact">Art.261: Full Faith &amp; Credit — అన్ని Public Acts, Records, Judicial proceedings కి గుర్తింపు</div>
    <div class="fact">All India Services (Art.312): IAS, IPS, IFoS — both Central &amp; State</div>
    <div class="fact">Art.312: Rajya Sabha 2/3 తీర్మానంతో Parliament కొత్త AIS సృష్టించగలదు</div>
  </div>
</div>
</div>

<!-- PAGE 2 -->
<div class="page">

<div class="sh">💰 4. ఆర్థిక సంబంధాలు — Art.264–293</div>
<div class="two">
  <div class="c a">
    <div class="ch">కేంద్రం వసూలు చేసి రాష్ట్రాలతో పంచుకునే పన్నులు</div>
    <div class="fact">Income Tax (Union List Entry 82)</div>
    <div class="fact">Corporation Tax (Union List Entry 85)</div>
    <div class="fact">Central GST + Interstate GST (Art.246A, Art.269A)</div>
    <div class="fact">Art.270: Finance Commission నిర్దేశించిన నిష్పత్తిలో పంపిణీ</div>
  </div>
  <div class="c r">
    <div class="ch">రాష్ట్రాలు మాత్రమే వసూలు చేసే పన్నులు</div>
    <div class="fact">Land Revenue (Entry 45), Agricultural Income Tax</div>
    <div class="fact">State Excise (Alcohol)</div>
    <div class="fact">Stamp Duty (commercial bills మినహా)</div>
    <div class="fact">State GST (intra-state trade)</div>
    <div class="fact">Professional Tax (max Rs.2,500/year)</div>
  </div>
</div>
<div class="c gr">
  <div class="ch">Consolidated Funds & Contingency</div>
  <div class="fact">Art.266(1) = CFI (Consolidated Fund of India) — అన్ని revenues; Parliament ఆమోదం తప్పనిసరి</div>
  <div class="fact">Art.267 = Contingency Fund of India — రాష్ట్రపతి నిర్వహిస్తారు; urgent unforeseen expenditure</div>
  <div class="fact">Charged Expenditure = Parliament vote లేకుండా CFI నుండి: President/Speaker/SC Judges వేతనాలు, రుణ వడ్డీ, CAG వేతనం</div>
</div>

<div class="sh">📊 5. Finance Commission & Sarkaria Commission</div>
<div class="two">
  <div class="c t">
    <div class="ch">Finance Commission (Art.280)</div>
    <div class="fact">రాష్ట్రపతి ప్రతి 5 సంవత్సరాలకు నియమిస్తారు</div>
    <div class="fact">1 Chairman + 4 Members</div>
    <div class="fact">15వ FC: N.K. Singh, 2020–25 (States' share 41%)</div>
    <div class="fact">14వ FC: Y.V. Reddy, 2015–20 (States' share 42%)</div>
    <div class="fact">సిఫారసు: Tax Devolution + Grants + State CF</div>
  </div>
  <div class="c p">
    <div class="ch">Sarkaria & Punchhi Commission</div>
    <div class="fact">Sarkaria Commission: 1983–88, R.S. Sarkaria; ముఖ్య సిఫారసు: ISC ఏర్పాటు</div>
    <div class="fact">Punchhi Commission: 2007–10, M.M. Punchhi; Governor fixed tenure 5 years</div>
    <div class="fact">Rajamannar Committee (1969, TN): రాష్ట్రాలకు అధిక స్వాయత్తత</div>
    <div class="fact">Art.356 = "last resort" — Sarkaria + SR Bommai (1994) వాదన</div>
  </div>
</div>

<div class="sh">⚡ Quick Revision Pills</div>
<div class="pills">
  <span class="pill">Union List = 97; State List = 66; Concurrent = 52</span>
  <span class="pill o">Art.246 = 7th Schedule Lists</span>
  <span class="pill b">Art.248 = Residuary → Parliament</span>
  <span class="pill g">Art.249 = National Interest (Rajya Sabha 2/3, 1 year)</span>
  <span class="pill r">Art.252 = 2+ states request</span>
  <span class="pill p">Art.253 = International Treaties</span>
  <span class="pill">Art.254 = Repugnancy → Central law wins</span>
  <span class="pill o">42వ సవరణ = Education, Forests → Concurrent</span>
  <span class="pill b">Art.280 = Finance Commission (5 సం.); 1 Chm + 4 Mbrs</span>
  <span class="pill g">15th FC = 2020–25; States 41%</span>
  <span class="pill r">Sarkaria = 1983 (ISC సిఫారసు); Punchhi = 2007</span>
  <span class="pill p">Art.355 = కేంద్రం duty (protect states)</span>
  <span class="pill">Art.246A (2016) = GST — Parliament + State Legislature</span>
  <span class="pill o">CFI = Art.266(1); Contingency = Art.267</span>
</div>
</div>

</body>
</html>
"""


# ── SEED FUNCTIONS ────────────────────────────────────────────────────────────

def _seed_polity_ch27_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False):
    check = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE subject=? AND topic=? AND chapter_num=?",
        (_SUBJECT, _TOPIC, _CH))
    row = check.fetchone()
    if row and not force:
        return
    if row and force:
        db_exec_fn(conn, "DELETE FROM study_notes WHERE subject=? AND topic=? AND chapter_num=?",
                   (_SUBJECT, _TOPIC, _CH))
    db_exec_fn(conn,
        """INSERT INTO study_notes
           (subject, topic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json)
           VALUES (?,?,?,?,?,?,?)""",
        (_SUBJECT, _TOPIC, _CH, _TITLE_TE, _TITLE_EN, _PAGES, json.dumps(_SECTIONS, ensure_ascii=False)))


def _seed_polity_ch27_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres):
    cur = db_exec_fn(conn,
        "SELECT id FROM study_notes WHERE subject=? AND topic=? AND chapter_num=?",
        (_SUBJECT, _TOPIC, _CH))
    note_row = cur.fetchone()
    if not note_row:
        return
    note_id = row_to_dict_fn(note_row)['id']

    diff_map = {"easy": 1, "medium": 2, "hard": 3, "toughest": 4, 1: 1, 2: 2, 3: 3, 4: 4}

    cur2 = db_exec_fn(conn,
        "SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id=?", (note_id,))
    cnt_row = cur2.fetchone()
    if cnt_row and list(cnt_row)[0] >= 64:
        return

    db_exec_fn(conn, "DELETE FROM chapter_mcqs WHERE study_note_id=?", (note_id,))

    for row in _MCQS:
        sec_idx   = row[0]
        diff_str  = row[1]
        q_te      = row[2]
        opt_a     = row[3]
        opt_b     = row[4]
        opt_c     = row[5]
        opt_d     = row[6]
        correct   = row[7]
        expl      = row[8]
        exam_type = row[9] if len(row) > 9 else 'General'
        if exam_type is None:
            exam_type = 'General'
        diff_int  = diff_map.get(diff_str, 2)
        db_exec_fn(conn,
            """INSERT INTO chapter_mcqs
               (study_note_id, section_idx, difficulty, exam_type,
                q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (note_id, sec_idx, diff_int, exam_type,
             q_te, opt_a, opt_b, opt_c, opt_d, correct, expl))


import json
