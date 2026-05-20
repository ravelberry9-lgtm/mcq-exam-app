"""
seed_concept_notes_div8div9div10.py
Question-specific concept notes for AP Current Affairs Divisions 8, 9, 10.

Source of truth: HTML notes div08, div09, div10 (AP Environment/ISRO/Sports,
Awards/Courts/Constitution, Reorganisation Act).

Each note is keyed by a unique tag and covers exactly the facts tested in MCQs.
"""


def seed():
    from app import get_db
    db = get_db()
    db.autocommit = True
    cur = db.cursor()

    notes = [

        # ─── DIVISION 8: ENVIRONMENT ──────────────────────────────────────────

        {
            'tag': 'nagarjunasagar_srisailam_tiger_reserve',
            'title': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం',
            'body': '''నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం (NSTR)
భారతదేశంలో అత్యధిక వైశాల్యం: ~3,728 చ.కి.మీ
రెండు రాష్ట్రాలు: AP (కర్నూలు, నంద్యాల, ప్రకాశం) + తెలంగాణ
AP వాటా: ~3,568 చ.కి.మీ
పర్వతశ్రేణి: నల్లమల కొండలు
నది: కృష్ణా నది ఒడ్డున; శ్రీశైలం ఆనకట్ట సమీపం
గిరిజనులు: చెంచు
పరీక్ష: "భారత అతి పెద్ద పులుల అభయారణ్యం" = నాగార్జునసాగర్-శ్రీశైలం''',
            'tags_json': '["Tiger Reserve","NSTR","AP Environment","Wildlife","Nallamala"]',
            'lang': 'te'
        },

        {
            'tag': 'koringa_mangroves_kakinada',
            'title': 'కొరింగ వన్యప్రాణి అభయారణ్యం — AP అతి పెద్ద మడ అడవి',
            'body': '''కొరింగ వన్యప్రాణి అభయారణ్యం
స్థానం: కాకినాడ జిల్లా, గోదావరి నది ముఖద్వారం వద్ద
AP అతి పెద్ద మడ అడవి (Mangrove Forest)
35+ మడ చెట్ల జాతులు
120+ పక్షి జాతులు (వలస)
ప్రత్యేక జంతువులు: Irrawaddy dolphins, ఆలివ్ రిడ్లీ తాబేళ్ళు
Ramsar Convention కింద తడి భూమి (Wetland) గుర్తింపు
పరీక్ష: "AP అతి పెద్ద మడ అడవి" = కొరింగ, కాకినాడ''',
            'tags_json': '["Koringa","Mangrove","Kakinada","Ramsar","AP Environment","Wildlife"]',
            'lang': 'te'
        },

        {
            'tag': 'koundinya_elephant_sanctuary',
            'title': 'కౌండిణ్య వన్యప్రాణి అభయారణ్యం — AP ఏకైక ఏనుగుల అభయారణ్యం',
            'body': '''కౌండిణ్య వన్యప్రాణి అభయారణ్యం
స్థానం: చిత్తూరు జిల్లా, కర్నాటక సరిహద్దు దగ్గర
AP లో ఏకైక ఏనుగుల అభయారణ్యం (Elephant Reserve)
ఏనుగుల సంఖ్య: ~60
పరీక్ష: "AP ఏకైక ఏనుగుల అభయారణ్యం" = కౌండిణ్య, చిత్తూరు''',
            'tags_json': '["Koundinya","Elephant","Chittoor","AP Environment","Wildlife"]',
            'lang': 'te'
        },

        {
            'tag': 'rollapadu_great_indian_bustard',
            'title': 'రోళ్లపాడు — Great Indian Bustard అభయారణ్యం (నందయాల జిల్లా)',
            'body': '''రోళ్లపాడు వన్యప్రాణి అభయారణ్యం
స్థానం: నందయాల జిల్లా (పూర్వం కర్నూలు జిల్లా) — పల్నాడు/గుంటూరు కాదు
Great Indian Bustard (GIB / జటాయువు) అభయారణ్యం
GIB: అత్యంత అంతరించిపోయే పక్షి జాతి
AP రాష్ట్ర జంతువు: కృష్ణజింక (Blackbuck) — ఇక్కడే ప్రసిద్ధి
పరీక్ష పాయింట్: రోళ్లపాడు = నందయాల జిల్లా (X పల్నాడు తప్పు)''',
            'tags_json': '["Rollapadu","GIB","Great Indian Bustard","Nandyal","AP Environment","Blackbuck"]',
            'lang': 'te'
        },

        {
            'tag': 'pulicat_lake_ap',
            'title': 'పులికాట్ సరస్సు — భారత 2వ అతి పెద్ద ఉప్పు సరస్సు',
            'body': '''పులికాట్ సరస్సు
స్థానం: తిరుపతి జిల్లా (సుల్లురుపేట ప్రాంతం) — శ్రీహరికోట పక్కన
భారత 2వ అతి పెద్ద ఉప్పు సరస్సు (మొదటిది: చిల్కా, ఒడిశా)
ఫ్లమింగో వలస పక్షుల ప్రసిద్ధ నిలయం
SDSC SHAR (శ్రీహరికోట) ఇక్కడే ఉంది
Ramsar Wetland Site
పరీక్ష: పులికాట్ = 2వ ఉప్పు సరస్సు; తిరుపతి జిల్లా''',
            'tags_json': '["Pulicat","Lake","Flamingo","Tirupati","AP Environment","SDSC SHAR"]',
            'lang': 'te'
        },

        {
            'tag': 'ap_state_symbols',
            'title': 'AP రాష్ట్ర చిహ్నాలు — జంతువు, పక్షి, చెట్టు, పువ్వు, చేప',
            'body': '''AP రాష్ట్ర చిహ్నాలు — పరీక్ş వివరాలు
రాష్ట్ర జంతువు: కృష్ణజింక (Blackbuck / Indian Antelope)
  — రోళ్లపాడు (నందయాల జిల్లా) ప్రసిద్ధి
రాష్ట్ర పక్షి: Indian Rose-ringed Parakeet (తోటాకిలి)
రాష్ట్ర చెట్టు: Neem (వేప)
రాష్ట్ర పువ్వు: Jasmine (మల్లె)
రాష్ట్ర చేప: Murrel (కోరి / కోర చేప)
పరీక్ష: కృష్ణజింక = రాష్ట్ర జంతువు; తోటాకిలి = రాష్ట్ర పక్షి''',
            'tags_json': '["AP State Symbols","Blackbuck","Parakeet","AP Environment"]',
            'lang': 'te'
        },

        {
            'tag': 'red_sanders_rayalaseema',
            'title': 'Red Sanders (ఎర్ర చందనం) — రాయలసీమ CITES రక్షిత జాతి',
            'body': '''Red Sanders (Pterocarpus santalinus / ఎర్ర చందనం)
ప్రత్యేక ప్రాంతం: రాయలసీమ అడవులు (కడప, తిరుపతి, చిత్తూరు, నంద్యాల జిల్లాలు)
శేషాచలం కొండలు — చిత్తూరు, కడప జిల్లాలు
CITES (Convention on International Trade in Endangered Species) రక్షిత జాతి
అంతర్జాతీయ అక్రమ రవాణా నిరోధానికి AP ప్రత్యేక task force (2024-25)
శ్రీ లంకమల్లేశ్వర వన్యప్రాణి అభయారణ్యం (నంద్యాల) — Red Sanders రక్షణ
పరీక్ష: Red Sanders = రాయలసీమ మాత్రమే; CITES రక్షణ''',
            'tags_json': '["Red Sanders","CITES","Rayalaseema","AP Environment","Seshachalam"]',
            'lang': 'te'
        },

        # ─── DIVISION 8: ISRO ─────────────────────────────────────────────────

        {
            'tag': 'sdsc_shar_sriharikota',
            'title': 'SDSC SHAR — శ్రీహరికోట స్పేస్ సెంటర్ (తిరుపతి జిల్లా)',
            'body': '''SDSC SHAR — Satish Dhawan Space Centre SHAR
SHAR = Sriharikota High Altitude Range
స్థానం: శ్రీహరికోట — తిరుపతి జిల్లా, AP (పులికాట్ సరస్సు పక్కన)
పేరు: మాజీ ISRO చైర్మన్ సతీష్ ధవన్ పేరిట (2002 మరణం తర్వాత)
లాంచ్ పాడ్‌లు: 3 (FLP, SLP, 3rd నిర్మాణంలో)
మొత్తం ప్రయోగాలు (డిసె. 2025): 104 (88 సఫలం, 5 పాక్షిక, 11 వైఫల్యం)
100వ ప్రయోగం: NVS-02 / GSLV-F15 — జనవరి 29, 2025
పరీక్ష: SDSC SHAR = తిరుపతి జిల్లా (X నెల్లూరు జిల్లా తప్పు)''',
            'tags_json': '["SDSC SHAR","ISRO","Sriharikota","Tirupati","Space","AP"]',
            'lang': 'te'
        },

        {
            'tag': 'nvs02_gslv_f15_100th_launch',
            'title': 'NVS-02 / GSLV-F15 — SDSC SHAR 100వ ప్రయోగం (జన. 29, 2025)',
            'body': '''NVS-02 ఉపగ్రహ ప్రయోగం — 100వ ప్రయోగం
తేదీ: జనవరి 29, 2025
రాకెట్: GSLV-F15 (Geosynchronous Satellite Launch Vehicle)
ఉపగ్రహం: NVS-02 — 2,232 కిలోలు; GTO కక్ష్య
ప్రయోజనం: NavIC (Navigation with Indian Constellation) వ్యవస్థ
NavIC = భారత స్వదేశీ GPS ప్రత్యామ్నాయం
ప్రాధాన్యత: SDSC SHAR శతక ప్రయోగం (100th launch milestone)
పరీక్ష: 100వ ప్రయోగం = NVS-02; GSLV-F15; జన. 29, 2025''',
            'tags_json': '["NVS-02","GSLV-F15","NavIC","100th Launch","ISRO","SDSC SHAR"]',
            'lang': 'te'
        },

        {
            'tag': 'spadex_space_docking',
            'title': 'SpaDeX — భారత తొలి స్పేస్ డాకింగ్ (జన. 16, 2025)',
            'body': '''SpaDeX = Space Docking Experiment
ప్రయోగం: డిసెంబర్ 30, 2024 — PSLV-C60 ద్వారా
స్పేస్‌క్రాఫ్ట్‌లు: SDX01 (Chaser) + SDX02 (Target)
డాకింగ్ సఫలం: జనవరి 16, 2025
పేలోడ్‌లు: 24
భారత్ స్థానం: 4వ దేశం (USA, Russia, China తర్వాత)
భవిష్యత్తు: Chandrayaan-4, Bharatiya Antariksh Station (BAS) కోసం
పరీక్ష: SpaDeX = భారత తొలి స్పేస్ డాకింగ్; జన. 16, 2025; 4వ దేశం''',
            'tags_json': '["SpaDeX","Space Docking","ISRO","PSLV-C60","SDX01","SDX02"]',
            'lang': 'te'
        },

        {
            'tag': 'chandrayaan3_moon_landing',
            'title': 'చంద్రయాన్-3 — చంద్రుని దక్షిణ ధ్రువం (ఆగ. 23, 2023)',
            'body': '''చంద్రయాన్-3
ప్రయోగం: LVM-3 (GSLV Mk3) రాకెట్ ద్వారా
లాండింగ్: ఆగస్టు 23, 2023 — చంద్రుని దక్షిణ ధ్రువ ప్రాంతం
లాండర్: విక్రమ్; రోవర్: ప్రజ్ఞాన్
భారత్ స్థానం: దక్షిణ ధ్రువంలో మొదటి దేశంగా సాఫ్ట్ ల్యాండింగ్
పరీక్ష: చంద్రయాన్-3 = ఆగ. 23, 2023; దక్షిణ ధ్రువం''',
            'tags_json': '["Chandrayaan-3","Moon","ISRO","Vikram","Pragyan","South Pole"]',
            'lang': 'te'
        },

        # ─── DIVISION 8: SPORTS ───────────────────────────────────────────────

        {
            'tag': 'pv_sindhu_olympics_bwf',
            'title': 'PV సింధు — ఒలింపిక్ పతకాలు, BWF Commission (2025)',
            'body': '''PV సింధు (Pusarla Venkata Sindhu)
జననం: జూలై 5, 1995 — హైదరాబాద్ (తెలుగు కుటుంబం)
ఒలింపిక్ పతకాలు:
  రియో 2016 → రజత పతకం (Silver)
  టోక్యో 2020 → కాంస్య పతకం (Bronze)
పారిస్ 2024: Opening Ceremony జెండా ఆజమాయిషీదారు
BWF Athletes Commission: 2025లో సభ్యురాలిగా ఎన్నిక
పురస్కారాలు: Padma Shri (2015), Rajiv Gandhi Khel Ratna (2016), Padma Bhushan (2020)
గురువు: పుల్లేల గోపీచంద్
పరీక్ష: సింధు = రజతం (2016) + కాంస్యం (2020); BWF Commission 2025''',
            'tags_json': '["PV Sindhu","Badminton","Olympics","Silver","Bronze","BWF","AP Sports"]',
            'lang': 'te'
        },

        {
            'tag': 'kidambi_srikanth_badminton',
            'title': 'కిడంబి శ్రీకాంత్ — BWF వరల్డ్ చాంపియన్‌షిప్ రజతం (2021)',
            'body': '''కిడంబి శ్రీకాంత్
జననం: ఫిబ్రవరి 7, 1993 — గుంటూరు, AP
BWF World Ranking పీక్: నంబర్ 1 (2018)
BWF World Championship 2021: రజత పతకం (ఫైనల్లో ఓడిపోయాడు)
Thomas Cup 2022: భారత్ తొలి విజయంలో కీలక సభ్యుడు
పురస్కారాలు: Arjuna Award (2018), Padma Shri (2022)
పరీక్ష: శ్రీకాంత్ = గుంటూరు జిల్లా; BWF 2021 రజతం; Thomas Cup 2022''',
            'tags_json': '["Kidambi Srikanth","Badminton","BWF","Guntur","Thomas Cup","AP Sports"]',
            'lang': 'te'
        },

        {
            'tag': 'pullela_gopichand_coach',
            'title': 'పుల్లేల గోపీచంద్ — AP బ్యాడ్మింటన్ గురువు',
            'body': '''పుల్లేల గోపీచంద్
జననం: నవంబర్ 16, 1973 — నాగందల, ప్రకాశం జిల్లా, AP
All England Champion: 2001
AP Badminton Academy: హైదరాబాద్
శిష్యులు: PV సింధు, సైనా నెహ్వాల్, కిడంబి శ్రీకాంత్
పురస్కారాలు: Padma Bhushan (2014), Dronacharya Award (2009)
పరీక్ష: గోపీచంద్ = ప్రకాశం జిల్లా; Padma Bhushan 2014; Dronacharya 2009''',
            'tags_json': '["Gopichand","Badminton Coach","Prakasam","AP Sports","Dronacharya"]',
            'lang': 'te'
        },

        {
            'tag': 'satwik_rankireddy_paris_2024',
            'title': 'సాత్విక్ రాంకిరెడ్డి — 2024 పారిస్ ఒలింపిక్స్ (AP బ్యాడ్మింటన్)',
            'body': '''సాత్విక్ సాయిరాజ్ రాంకిరెడ్డి
AP కనెక్షన్: అమలాపురం, తూర్పు గోదావరి జిల్లా, AP
క్రీడ: బ్యాడ్మింటన్ — మెన్స్ డబుల్స్
జంట: చిరాగ్ శెట్టితో కలిసి ఆడతాడు
BWF World Ranking: నంబర్ 1 జంట (పీక్)
2024 పారిస్ ఒలింపిక్స్: మెన్స్ డబుల్స్‌లో పాల్గొన్నాడు
గమనిక: పారిస్ 2024లో స్వర్ణ పతకం సాధించలేదు
పరీక్ష: సాత్విక్ = అమలాపురం AP; పారిస్ 2024 మెన్స్ డబుల్స్; BWF నంబర్ 1''',
            'tags_json': '["Satwik Rankireddy","Badminton","Paris Olympics 2024","Amalapuram","AP Sports"]',
            'lang': 'te'
        },

        {
            'tag': 'nitesh_kumar_para_olympics_2024',
            'title': 'నితేష్ కుమార్ — పారిస్ 2024 Para Olympics స్వర్ణ పతకం',
            'body': '''నితేష్ కుమార్
క్రీడ: Para Badminton
2024 పారిస్ Para Olympics: స్వర్ణ పతకం (Gold Medal)
AP కనెక్షన్: గోపీచంద్ అకాడమీ లో శిక్షణ
పరీక్ష: నితేష్ కుమార్ = Para Badminton; పారిస్ 2024 Para Olympics స్వర్ణం''',
            'tags_json': '["Nitesh Kumar","Para Badminton","Para Olympics","Gold Medal","AP Sports"]',
            'lang': 'te'
        },

        # ─── DIVISION 9: AWARDS ───────────────────────────────────────────────

        {
            'tag': 'sp_balasubrahmanyam_padma_vibhushan',
            'title': 'SP బాలసుబ్రహ్మణ్యం — Padma Vibhushan 2021 (మరణానంతరం)',
            'body': '''SP బాలసుబ్రహ్మణ్యం (Sripathi Panditaradhyula Balasubrahmanyam)
జననం: జూన్ 4, 1946 — కోనేటమ్మపేట, నెల్లూరు జిల్లా, AP
మరణం: సెప్టెంబర్ 25, 2020 — COVID-19 (చెన్నైలో)
విజయాలు: 40,000+ పాటలు; 16 భాషలు; Guinness World Record
6 జాతీయ చలనచిత్ర పురస్కారాలు (ఉత్తమ గాయకుడు)
తొలి National Award: "Ek Duje Ke Liye" (1981) హిందీ పాట
పురస్కారాల క్రమం: Padma Shri (1981) → Padma Bhushan (2001) → Padma Vibhushan (2021 మరణానంతరం)
పరీక్ష: SPB = నెల్లూరు జిల్లా; Padma Vibhushan 2021; మరణానంతరం''',
            'tags_json': '["SP Balasubrahmanyam","SPB","Padma Vibhushan","Nellore","Music","Awards"]',
            'lang': 'te'
        },

        {
            'tag': 'k_viswanath_padma_falke',
            'title': 'K. విశ్వనాథ్ — Padma Shri 1992 + దాదాసాహేబ్ ఫాల్కే 2016',
            'body': '''K. విశ్వనాథ్ (Kovelamudi Viswanath)
జననం: ఫిబ్రవరి 19, 1930 — మచిలీపట్నం, కృష్ణా జిల్లా
ముఖ్య చిత్రాలు: శంకరాభరణం (1980), స్వాతిముత్యం, సాగర సంగమం, స్వర్ణకమలం
5 జాతీయ పురస్కారాలు (ఉత్తమ దర్శకుడు)
పురస్కారాలు: Padma Shri (1992), దాదాసాహేబ్ ఫాల్కే (2016)
గమనిక: ఆయనకు Padma Vibhushan రాలేదు — ఇది తరచు పరీక్షల్లో తప్పుగా ఇస్తారు
పరీక్ష: K. విశ్వనాథ్ = Padma Shri (1992) + Falke (2016); Padma Vibhushan కాదు''',
            'tags_json': '["K Viswanath","Padma Shri","Dadasaheb Phalke","Telugu Cinema","Awards","Krishna District"]',
            'lang': 'te'
        },

        {
            'tag': 'naatu_naatu_oscar_2023',
            'title': '"నాటు నాటు" Oscar 2023 — MM కీరవాణి, చంద్రబోస్, SS రాజమౌళి',
            'body': '''నాటు నాటు — Oscar 2023
పురస్కారం: Academy Award (Oscar) — Best Original Song
వేడుక: 95వ Academy Awards, మార్చి 12, 2023
చిత్రం: RRR (2022) — దర్శకుడు SS రాజమౌళి
సంగీత దర్శకుడు: MM కీరవాణి
  జన్మస్థానం: కొవ్వూరు (Kovvur), పశ్చిమ గోదావరి జిల్లా, AP
  గమనిక: కోడూరు/కృష్ణా జిల్లా కాదు — తరచు తప్పుగా ఇస్తారు
సాహిత్యకర్త: చంద్రబోస్ — AP
Golden Globe 2023: Best Original Song కూడా సాధించింది
ప్రాధాన్యత: భారతదేశానికి తొలి Oscar Best Original Song
పరీక్ష: MM కీరవాణి = కొవ్వూరు, పశ్చిమ గోదావరి; Oscar 2023''',
            'tags_json': '["Naatu Naatu","Oscar","MM Keeravani","RRR","Kovvur","AP Awards","Golden Globe"]',
            'lang': 'te'
        },

        {
            'tag': 'allu_arjun_national_award',
            'title': 'అల్లు అర్జున్ — 69వ జాతీయ Best Actor పురస్కారం (Pushpa)',
            'body': '''అల్లు అర్జున్ — జాతీయ చలనచిత్ర పురస్కారం
పురస్కారం: 69వ జాతీయ చలనచిత్ర పురస్కారాలు (2022)
విభాగం: Best Actor
చిత్రం: Pushpa: The Rise (2021)
ప్రాధాన్యత: తెలుగు నటులలో తొలి జాతీయ Best Actor పురస్కారం
అదే వేడుక:
  దేవి శ్రీ ప్రసాద్ (DSP) → Best Music Direction (Songs) — Pushpa
  MM కీరవాణి → Best Music Direction (Background) — RRR
  Pushpa: The Rise → Popular Film Providing Wholesome Entertainment
71వ జాతీయ పురస్కారాలు (2025): Bhagavanth Kesari → Best Telugu Film (బాలకృష్ణ)
పరీక్ష: అల్లు అర్జున్ = 69వ NFA Best Actor; Pushpa; తొలి తెలుగు నటుడు''',
            'tags_json': '["Allu Arjun","National Award","Best Actor","Pushpa","69th NFA","Telugu Cinema"]',
            'lang': 'te'
        },

        {
            'tag': 'padma_awards_2025_telugu',
            'title': 'Padma Awards 2025 — తెలుగు రాష్ట్రాల గ్రహీతలు (7 మంది)',
            'body': '''2025 Padma Awards — తెలుగు రాష్ట్రాలు
మొత్తం తెలుగు గ్రహీతలు: 7 (AP: 5, Telangana: 2)

Padma Vibhushan (1):
  Dr. Duvvur Nageshwar Reddy — Medicine; Telangana
  (Asian Institute of Gastroenterology వ్యవస్థాపకుడు)

Padma Bhushan (1):
  Nandamuri Balakrishna — Art (Telugu Cinema); Andhra Pradesh
  (గమనిక: Padma Bhushan — Padma Vibhushan కాదు)

Padma Shri AP (4):
  Madugula Nagaphani Sarma — Art (Avadhanam)
  K.L. Krishna — Literature & Education
  Miriyala Apparao — Art (Burrakatha) — మరణానంతరం; తాడేపల్లిగూడెం
  Vadiraj Panchamukhi — Literature & Education

Padma Shri Telangana (1):
  Manda Krishna Madiga — Public Affairs (SC వర్గీకరణ ఉద్యమ నేత)

పరీక్ష: 2025 = 7 Telugu (AP:5, TG:2); Balakrishna = Padma Bhushan (Vibhushan కాదు)''',
            'tags_json': '["Padma Awards 2025","Balakrishna","Nageshwar Reddy","Telugu","AP Awards","Telangana"]',
            'lang': 'te'
        },

        {
            'tag': 'padma_awards_2026_telugu',
            'title': 'Padma Awards 2026 — తెలుగు రాష్ట్రాల గ్రహీతలు (12 మంది)',
            'body': '''2026 Padma Awards — తెలుగు రాష్ట్రాలు
ప్రకటన: జనవరి 25, 2026
మొత్తం గ్రహీతలు: 12 (AP: 4, Telangana: 7, USA-Telugu: 1)

Padma Bhushan (1):
  Dr. Nori Dattatreyudu — Medicine; USA (తెలుగు మూలాలు)

AP Padma Shri (4):
  Gadde Babu Rajendra Prasad — Art
  Garimella Balakrishna Prasad — Art (మరణానంతరం)
  Maganti Murali Mohan — Art
  Vempaty Kutumba Sastry — Literature & Education

Telangana Padma Shri (7):
  Chandramouli Gaddamanugu — Science & Engineering
  Deepika Reddy — Art
  Guduru Venkat Rao — Medicine
  Krishnamurty Balasubramanian — Science & Engineering
  Kumarasamy Thangaraj — Science & Engineering
  Palkonda Vijay Anand Reddy — Medicine
  Rama Reddy Mamidi — Animal Husbandry (మరణానంతరం)

పరీక్ష: 2026 = 12 Telugu; AP:4, TG:7, USA:1; Dr. Nori Dattatreyudu = Padma Bhushan''',
            'tags_json': '["Padma Awards 2026","Nori Dattatreyudu","Telugu","AP Awards","Telangana"]',
            'lang': 'te'
        },

        {
            'tag': 'viswanadha_satyanarayana_jnanpith',
            'title': 'విశ్వనాధ సత్యనారాయణ — జ్ఞానపీఠ పురస్కారం 1970',
            'body': '''విశ్వనాధ సత్యనారాయణ (కవి సమ్రాట్)
జననం: సెప్టెంబర్ 10, 1895 — నందమూరు, కృష్ణా జిల్లా
మరణం: అక్టోబర్ 18, 1976
జ్ఞానపీఠ పురస్కారం: 1970 — తెలుగు నుండి మొదటి జ్ఞానపీఠ గ్రహీత
ముఖ్య రచన: "వేయిపడగలు" నవల (తెలుగు సాహిత్యంలో అత్యుత్తమ)
ఇతర రచన: "రామాయణ కల్పవృక్షం" — 5 జాతీయ పురస్కారాలు
బిరుదు: "కవి సమ్రాట్"
పరీక్ష: విశ్వనాధ సత్యనారాయణ = 1970 జ్ఞానపీఠ; తెలుగు తొలి; కృష్ణా జిల్లా''',
            'tags_json': '["Viswanatha Satyanarayana","Jnanpith","Telugu Literature","1970","Awards"]',
            'lang': 'te'
        },

        # ─── DIVISION 9: COURTS & CONSTITUTION ───────────────────────────────

        {
            'tag': 'ap_high_court_history',
            'title': 'AP హైకోర్టు — స్థాపన చరిత్ర (జన. 1, 2019)',
            'body': '''AP హైకోర్టు చరిత్ర
2014 ముందు: హైదరాబాద్ HC లో AP + తెలంగాణ కలిసి
APRA 2014 Section 30: AP కి ప్రత్యేక HC ఏర్పాటు చేయాల్సిన బాధ్యత కేంద్రానికి
2014–2018: హైదరాబాద్ HC తాత్కాలికంగా రెండు రాష్ట్రాలకు ఉమ్మడి HC
AP HC ప్రారంభం: జనవరి 1, 2019 — అమరావతిలో
మొదటి CJ (శాశ్వత): Justice J.K. Maheshwari (2019)
3వ CJ: Justice Prashant Kumar Mishra (2021-2023)
5వ CJ: Justice Dhiraj Singh Thakur — జులై 28, 2023 నుండి ఏప్రిల్ 24, 2026
6వ CJ: Justice Lisa Gill — ఏప్రిల్ 25, 2026 నుండి
పరీక్ష: AP HC = జన. 1, 2019; APRA Section 30; అమరావతి''',
            'tags_json': '["AP High Court","Amaravati","Section 30","APRA 2014","Constitution"]',
            'lang': 'te'
        },

        {
            'tag': 'justice_lisa_gill_ap_hc_cj',
            'title': 'Justice Lisa Gill — AP HC 6వ CJ, తొలి మహిళా CJ (ఏప్రిల్ 25, 2026)',
            'body': '''Justice Lisa Gill — AP High Court
పదవి: 6వ ప్రధాన న్యాయమూర్తి (Chief Justice)
ప్రాధాన్యత: AP HC చరిత్రలో తొలి మహిళా ప్రధాన న్యాయమూర్తి
మునుపటి HC: Punjab & Haryana High Court
పదవి స్వీకారం: ఏప్రిల్ 25, 2026
నియామకం: SC కొలీజియం సిఫారసు మేరకు రాష్ట్రపతి నియమించారు
నేపథ్యం: మార్చి 2026లో AP HC న్యాయమూర్తిగా ప్రమాణస్వీకారం
5వ CJ Justice Dhiraj Singh Thakur పదవీ విరమణ: ఏప్రిల్ 24, 2026
పరీక్ష: Lisa Gill = AP HC 6వ CJ; తొలి మహిళా CJ; ఏప్రిల్ 25, 2026; P&H HC''',
            'tags_json': '["Lisa Gill","AP High Court","CJ","First Woman","Chief Justice","AP Constitution"]',
            'lang': 'te'
        },

        {
            'tag': 'article_371d_ap',
            'title': 'ఆర్టికల్ 371-D — AP కి ప్రత్యేక రాజ్యాంగ సంరక్షణ (32వ సవరణ 1973)',
            'body': '''ఆర్టికల్ 371-D
రాష్ట్రం: ఆంధ్రప్రదేశ్
రాజ్యాంగ సవరణ: 32వ సవరణ చట్టం, 1973
ఉద్దేశ్యం: ఉమ్మడి AP లో వివిధ ప్రాంతాల ప్రజలకు విద్య, ఉద్యోగాల్లో సమతుల్యత
Presidential Order: G.O.610 — రాష్ట్రాన్ని 6 Zones గా విభజన (స్థానిక ఉద్యోగ కోటా)
Administrative Tribunal: ఏర్పాటు అధికారం
విభజన తర్వాత: AP (తెలంగాణ మినహా) కు వర్తించడం కొనసాగింది
పరీక్ష: ఆర్టికల్ 371-D = AP; 32వ సవరణ 1973; G.O.610; 6 Zones''',
            'tags_json': '["Article 371-D","AP Constitution","32nd Amendment","GO610","Zones","Mulki Rules"]',
            'lang': 'te'
        },

        {
            'tag': 'aiims_mangalagiri',
            'title': 'AIIMS మంగళగిరి — AP మొదటి AIIMS (గుంటూరు జిల్లా)',
            'body': '''AIIMS మంగళగిరి
పూర్తి పేరు: All India Institute of Medical Sciences, Mangalagiri
స్థానం: మంగళగిరి — అమరావతి రాజధాని సమీపం; గుంటూరు జిల్లా
PMSSY: Pradhan Mantri Swasthya Suraksha Yojana కింద స్థాపన
విద్యా ప్రారంభం: 2020 (MBBS తరగతులు)
ఆసుపత్రి ప్రారంభం: 2022 (OPD సేవలు)
BHISHMA Cubes (2025): జులై 19, 2025న 3 BHISHMA క్యూబ్‌లు స్థాపన
  ఒక్కో cube: 72 యూనిట్లు; 10 నిమిషాల్లో 200 మందికి చికిత్స
ప్రాధాన్యత: AP లో మొదటి AIIMS
పరీక్ష: AIIMS మంగళగిరి = గుంటూరు జిల్లా; PMSSY; 2022; AP మొదటి''',
            'tags_json': '["AIIMS Mangalagiri","Guntur","PMSSY","Medical","AP Institutions","BHISHMA"]',
            'lang': 'te'
        },

        {
            'tag': 'iit_tirupati',
            'title': 'IIT తిరుపతి — AP ఏకైక IIT (2015)',
            'body': '''IIT తిరుపతి
స్థానం: యెర్పేడు మండలం, తిరుపతి జిల్లా (550+ ఎకరాలు)
స్థాపన: 2015
AP కి APRA 2014 ప్రకారం మంజూరు అయిన IIT
భారత 23 IITలలో ఒకటి — AP ఏకైక IIT
కోర్సులు: B.Tech, M.Tech, MBA, PhD; CSE, ECE, ME, CE, EE
పరిశోధన: AI, Clean Energy, Biotechnology
NIRF 2024: Engineering విభాగంలో top 50
పరీక్ష: IIT తిరుపతి = యెర్పేడు, తిరుపతి జిల్లా; 2015; AP ఏకైక IIT''',
            'tags_json': '["IIT Tirupati","Yerpedu","Tirupati","AP Institutions","Engineering","2015"]',
            'lang': 'te'
        },

        # ─── DIVISION 10: REORGANISATION ACT ─────────────────────────────────

        {
            'tag': 'apra_2014_key_facts',
            'title': 'APRA 2014 — ముఖ్య వివరాలు (Act No. 6/2014)',
            'body': '''Andhra Pradesh Reorganisation Act, 2014
Act Number: Act No. 6 of 2014
Lok Sabha ఆమోదం: ఫిబ్రవరి 18, 2014
Rajya Sabha ఆమోదం: ఫిబ్రవరి 20, 2014
రాష్ట్రపతి ఆమోదం: మార్చి 1, 2014
అమలు తేదీ: జూన్ 2, 2014
తెలంగాణ: 29వ రాష్ట్రంగా అవతరణ
నూతన AP: 13 జిల్లాలతో
హైదరాబాద్: 10 సంవత్సరాలు ఉమ్మడి రాజధాని (2014–2024)
పరీక్ష: APRA = Act No. 6/2014; జూన్ 2, 2014; తెలంగాణ 29వ రాష్ట్రం''',
            'tags_json': '["APRA 2014","Act 6","Bifurcation","Telangana","AP Reorganisation","June 2014"]',
            'lang': 'te'
        },

        {
            'tag': 'apra_2014_key_sections',
            'title': 'APRA 2014 — కీలక Sections (5, 30, 94)',
            'body': '''APRA 2014 కీలక Sections
Section 5(1): తెలంగాణ రాజధాని = హైదరాబాద్
Section 5(2): AP రాజధాని నిర్ణయం (2026 సవరణ ద్వారా అమరావతి)
Section 24: AP అసెంబ్లీ 175 స్థానాలు; Lok Sabha 25; Rajya Sabha 11
Section 30: AP కి ప్రత్యేక High Court ఏర్పాటు — కేంద్రం బాధ్యత
  → AP HC: జనవరి 1, 2019 — అమరావతి
Section 93: పుదుచ్చేరి, యానాం అంశాలు
Section 94: పోలవరం ప్రాజెక్టు జాతీయ ప్రాజెక్టుగా గుర్తింపు
  → కేంద్రం 100% నిధులు ఇవ్వాలి
SCS: Rajya Sabha చర్చలో మన్మోహన్ సింగ్ వాగ్దానం; చట్టరూపం లేదు
పరీక్ష: Section 30 = AP HC; Section 94 = పోలవరం; Section 5(2) = రాజధాని''',
            'tags_json': '["APRA 2014","Section 30","Section 94","Polavaram","AP HC","Key Sections"]',
            'lang': 'te'
        },

        {
            'tag': 'polavaram_national_project_section94',
            'title': 'పోలవరం జాతీయ ప్రాజెక్టు — APRA Section 94',
            'body': '''పోలవరం ప్రాజెక్టు — జాతీయ ప్రాజెక్టు హోదా
APRA Section: Section 94 — జాతీయ ప్రాజెక్టుగా గుర్తింపు
స్థానం: పశ్చిమ గోదావరి జిల్లా, ఏలేశ్వరం వద్ద; గోదావరి నది
ప్రయోజనాలు: 7.2 లక్షల ఎకరాలకు సాగునీరు; 960 MW విద్యుత్; తాగునీరు
కేంద్రం బాధ్యత: జాతీయ ప్రాజెక్టుగా కేంద్రం 100% నిధులు
రివైజ్డ్ అంచనా: ~₹1,50,000 కోట్లు
7 మండలాల బదిలీ: APRA Amendment Act No. 19/2014 (జూలై 11, 2014)
  ఖమ్మం → తూర్పు/పశ్చిమ గోదావరి (పోలవరం నిర్మాణ ప్రాంతం AP లో ఉండేందుకు)
పరీక్ష: పోలవరం = Section 94; జాతీయ ప్రాజెక్టు; కేంద్రం నిధులు''',
            'tags_json': '["Polavaram","Section 94","National Project","APRA 2014","AP Water","Godavari"]',
            'lang': 'te'
        },

        {
            'tag': 'apra_amendment_2026_amaravati',
            'title': 'AP Reorganisation Amendment Act 2026 — అమరావతి రాజధాని (Act No. 7/2026)',
            'body': '''AP Reorganisation (Amendment) Act, 2026
Act Number: Act No. 7 of 2026
సవరించిన Section: APRA 2014 Section 5(2)
AP అసెంబ్లీ తీర్మానం: మార్చి 28, 2026
Lok Sabha ఆమోదం: ఏప్రిల్ 1, 2026 (మూజువాణి ఓటు)
Rajya Sabha ఆమోదం: ఏప్రిల్ 2, 2026 (మూజువాణి ఓటు)
రాష్ట్రపతి ఆమోదం: ఏప్రిల్ 6, 2026 — ద్రౌపదీ ముర్ము (Article 111 కింద)
అమరావతి రాజధాని తేదీ: జూన్ 2, 2024 నుండి (Retrospective)
నేపథ్యం: APRA 2014 లో రాజధాని నిర్దిష్టంగా పేర్కొనలేదు; 2026 సవరణ స్పష్టం
పరీక్ష: Act 7/2026; ఏప్రిల్ 1/2/6, 2026; అమరావతి = జూన్ 2, 2024 (Retrospective)''',
            'tags_json': '["Amendment Act 2026","Amaravati","Capital","Act 7","APRA","Section 5"]',
            'lang': 'te'
        },

        {
            'tag': 'scs_special_category_status',
            'title': 'Special Category Status (SCS) — AP డిమాండ్ & 14వ ఆర్థిక సంఘం',
            'body': '''Special Category Status (SCS) — AP
SCS వాగ్దానం: 2014 Rajya Sabha చర్చలో మన్మోహన్ సింగ్ ప్రభుత్వం
చట్టరూపం: APRA లో SCS కి సంబంధిత Section లేదు
14వ ఆర్థిక సంఘం (2015): SCS విధానాన్నే రద్దు చేయాలని సిఫారసు
NITI Aayog: SCS గుర్తింపు ఇవ్వలేదు
"Special Assistance" రూపంలో నిధులు అందజేస్తున్నారు
AP కి ఇచ్చిన ప్యాకేజీలు (SCS బదులు):
  పోలవరం జాతీయ ప్రాజెక్టు; VCIC; IIT, NIT, AIIMS, IISER
ప్రస్తుత స్థితి: SCS ఇంకా రాలేదు; రాజకీయ అంశంగా కొనసాగుతోంది
పరీక్ష: SCS వాగ్దానం = మన్మోహన్ సింగ్; 14వ ఆర్థిక సంఘం = రద్దు సిఫారసు''',
            'tags_json': '["SCS","Special Category Status","AP","14th Finance Commission","APRA 2014"]',
            'lang': 'te'
        },

        {
            'tag': 'ap_districts_reorganisation',
            'title': 'AP జిల్లాలు — 13 → 26 → 28 పునర్వ్యవస్థీకరణ',
            'body': '''AP జిల్లాల పునర్వ్యవస్థీకరణ
2014 వరకు: 13 జిల్లాలు
ఏప్రిల్ 4, 2022: 26 జిల్లాలు (YSRCP ప్రభుత్వం)
జనవరి 1, 2026: 28 జిల్లాలు (TDP ప్రభుత్వం)
  కొత్త జిల్లాలు: పోలవరం + మర్కాపురం (2 కొత్తవి)
  పోలవరం జిల్లా: పశ్చిమ గోదావరి (ఏలూరు) నుండి వేరు
  మర్కాపురం జిల్లా: ప్రకాశం జిల్లా నుండి వేరు
7 మండలాల బదిలీ: 2014లో ఖమ్మం నుండి AP కి (APRA Act 19/2014)
  కునవరం, వి.ఆర్.పురం, చింతూరు, నెల్లిపాక → తూ.గో.
  వేలేర్పాడు, బుర్గంపాడు, కుకుణూరు → ప.గో.
పరీక్ష: 2022 = 26 జిల్లాలు; 2026 = 28 జిల్లాలు; పోలవరం + మర్కాపురం''',
            'tags_json': '["AP Districts","26 Districts","28 Districts","Polavaram","Markapuram","Reorganisation"]',
            'lang': 'te'
        },

        {
            'tag': 'ap_legislature_seats',
            'title': 'AP శాసనసభ — 175 స్థానాలు, Lok Sabha 25, Rajya Sabha 11',
            'body': '''AP శాసన వ్యవస్థ (APRA 2014 Section 24)
శాసనసభ (Vidhan Sabha): 175 స్థానాలు
లోక్‌సభ (Lok Sabha): 25 స్థానాలు
  2024 ఫలితం: TDP 16, YSRCP 4, Jana Sena 2, BJP 3
రాజ్యసభ (Rajya Sabha): 11 స్థానాలు
పదవీ కాలం: 5 సంవత్సరాలు; ఏప్రిల్-మే 2024 ఎన్నికలు
AP CM: N. చంద్రబాబు నాయుడు — జూన్ 12, 2024 నుండి (TDP-JSP-BJP కూటమి)
AP గవర్నర్: S. అబ్దుల్ నజీర్ — 2023 ఫిబ్రవరి నుండి (మాజీ SC జస్టిస్)
పరీక్ష: AP = 175 అసెంబ్లీ; 25 LS; 11 RS; CM చంద్రబాబు (2024)''',
            'tags_json': '["AP Assembly","175 Seats","Lok Sabha 25","Rajya Sabha 11","Section 24","APRA"]',
            'lang': 'te'
        },

    ]

    for n in notes:
        cur.execute("""
            INSERT INTO concept_notes (tag, title, body, tags_json, lang)
            VALUES (%(tag)s, %(title)s, %(body)s, %(tags_json)s, %(lang)s)
            ON CONFLICT (tag) DO UPDATE
              SET title=EXCLUDED.title, body=EXCLUDED.body,
                  tags_json=EXCLUDED.tags_json, lang=EXCLUDED.lang
        """, n)
    cur.close()
    print(f'[div8div9div10 notes] seeded {len(notes)} concept notes')


if __name__ == '__main__':
    seed()
