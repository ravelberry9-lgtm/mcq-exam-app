"""
seed_ap_ca_div8.py
AP Current Affairs — Chapter 8: AP పర్యావరణం, ISRO & క్రీడలు
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div8_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "summary": "జాతీయ ఉద్యానవనాలు, పులుల అభయారణ్యాలు, ISRO SDSC SHAR, AP క్రీడావీరులు — పరీక్ష హాట్‌స్పాట్‌లు"
    },
    {
        "id": "div8_s2",
        "title": "జాతీయ ఉద్యానవనాలు",
        "summary": "పాపికొండలు, రాజీవ్ గాంధీ జాతీయ ఉద్యానవనం (నాగార్జునసాగర్-శ్రీశైలం), శ్రీ వేంకటేశ్వర జాతీయ ఉద్యానవనం"
    },
    {
        "id": "div8_s3",
        "title": "వన్యప్రాణి అభయారణ్యాలు",
        "summary": "కొరింగ మడ అడవులు, కౌండిణ్య ఏనుగుల అభయారణ్యం, రోళ్లపాడు GIB అభయారణ్యం, పులికాట్ సరస్సు"
    },
    {
        "id": "div8_s4",
        "title": "ISRO — SDSC SHAR",
        "summary": "శ్రీహరికోట స్పేస్ సెంటర్; 100వ ప్రయోగం NVS-02 (జన. 29, 2025); SpaDeX స్పేస్ డాకింగ్ (డిసె. 2024)"
    },
    {
        "id": "div8_s5",
        "title": "AP క్రీడావీరులు",
        "summary": "PV సింధు — రియో రజతం, టోక్యో కాంస్యం; కిడంబి శ్రీకాంత్ — BWF 2021 రజతం; గోపీచంద్ — గురువు; నితేష్ కుమార్ — Para Olympics స్వర్ణం"
    },
    {
        "id": "div8_s6",
        "title": "పర్యావరణ కరెంట్ అఫైర్స్",
        "summary": "Red Sanders రక్షణ, ఆలివ్ రిడ్లీ తాబేళ్ళు, పాపికొండలు ఎకో టూరిజమ్, AP Green Hydrogen Policy"
    },
    {
        "id": "div8_s7",
        "title": "పర్యావరణ సంఖ్యలు",
        "summary": "ముఖ్య సంఖ్యలు: నాగార్జునసాగర్ వైశాల్యం, కొరింగ మడ జాతులు, SDSC SHAR మొత్తం ప్రయోగాలు"
    },
    {
        "id": "div8_s8",
        "title": "పరీక్ష రేపిడ్ రివిజన్",
        "summary": "పర్యావరణం, ISRO, క్రీడలు — సంక్షిప్త పట్టిక"
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Key concepts
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "SDSC SHAR ఏ జిల్లాలో ఉంది?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "తిరుపతి",
        "opt_c": "గుంటూరు",
        "opt_d": "కాకినాడ",
        "answer": "B",
        "explanation_te": "SDSC SHAR (Satish Dhawan Space Centre) శ్రీహరికోట ద్వీపంలో ఉంది — ఇది తిరుపతి జిల్లాలో పులికాట్ సరస్సు పక్కన ఉంది."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "SDSC SHAR పూర్తి అర్థం ఏమిటి?",
        "opt_a": "Satish Dhawan Space Centre — Sriharikota High Altitude Range",
        "opt_b": "Space Development & Science Centre — Sriharikota",
        "opt_c": "Satellite Design & Signal Centre — Sriharikota",
        "opt_d": "South Division Space Coordination — Sriharikota Hangar",
        "answer": "A",
        "explanation_te": "SDSC = Satish Dhawan Space Centre (మాజీ ISRO చైర్మన్ పేరు); SHAR = Sriharikota High Altitude Range."
    },
    # Section 1 — National Parks
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "పాపికొండలు జాతీయ ఉద్యానవనం ఏ నదిపై ఉంది?",
        "opt_a": "కృష్ణా నది",
        "opt_b": "గోదావరి నది",
        "opt_c": "పెన్నా నది",
        "opt_d": "తుంగభద్ర నది",
        "answer": "B",
        "explanation_te": "పాపికొండలు జాతీయ ఉద్యానవనం గోదావరి నది ఒడ్డున పశ్చిమ గోదావరి, ఏలూరు జిల్లాల్లో ఉంది. Boat Safari ఇక్కడ ప్రసిద్ధి."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "శ్రీ వేంకటేశ్వర జాతీయ ఉద్యానవనం ఏ ముఖ్య వృక్ష జాతికి ప్రసిద్ధి?",
        "opt_a": "మడ చెట్లు",
        "opt_b": "Red Sanders (ఎర్ర చందనం)",
        "opt_c": "Sal చెట్లు",
        "opt_d": "Teak చెట్లు",
        "answer": "B",
        "explanation_te": "శ్రీ వేంకటేశ్వర జాతీయ ఉద్యానవనం (తిరుపతి జిల్లా) Red Sanders (Pterocarpus santalinus) కోసం ప్రసిద్ధి — CITES రక్షిత జాతి."
    },
    # Section 2 — Wildlife Sanctuaries
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "భారతదేశంలో అత్యధిక వైశాల్యం గల పులుల అభయారణ్యం ఏది?",
        "opt_a": "కార్బెట్ జాతీయ ఉద్యానవనం",
        "opt_b": "నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం",
        "opt_c": "సుందర్‌బన్స్",
        "opt_d": "బందీపూర్",
        "answer": "B",
        "explanation_te": "నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం (~3,728 చ.కి.మీ) భారతదేశంలో అతి పెద్ద పులుల అభయారణ్యం. ఇది AP మరియు తెలంగాణ రెండు రాష్ట్రాలలో విస్తరించింది."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "AP లో ఏకైక ఏనుగుల అభయారణ్యం ఏది?",
        "opt_a": "కొరింగ",
        "opt_b": "రోళ్లపాడు",
        "opt_c": "కౌండిణ్య",
        "opt_d": "నేలపట్టు",
        "answer": "C",
        "explanation_te": "కౌండిణ్య వన్యప్రాణి అభయారణ్యం (చిత్తూరు జిల్లా) AP లో ఏకైక ఏనుగుల అభయారణ్యం. కర్నాటక సరిహద్దు దగ్గర ఉంది."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "కొరింగ వన్యప్రాణి అభయారణ్యం ఎందుకు ప్రసిద్ధి?",
        "opt_a": "పులుల కోసం",
        "opt_b": "మడ అడవులు — AP అతి పెద్ద Mangrove",
        "opt_c": "ఏనుగుల కోసం",
        "opt_d": "గ్రేట్ ఇండియన్ బస్టర్డ్ కోసం",
        "answer": "B",
        "explanation_te": "కొరింగ (కాకినాడ జిల్లా) AP అతి పెద్ద మడ అడవి. గోదావరి నది ముఖద్వారం వద్ద ఉంది. 35+ మడ చెట్ల జాతులు, Irrawaddy dolphins ఉన్నాయి. Ramsar Wetland Site."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "రోళ్లపాడు వన్యప్రాణి అభయారణ్యం ఏ పక్షికి పేరు పొందింది?",
        "opt_a": "ఫ్లమింగో",
        "opt_b": "Peacock (నెమలి)",
        "opt_c": "Great Indian Bustard (జటాయువు)",
        "opt_d": "పెలికాన్",
        "answer": "C",
        "explanation_te": "రోళ్లపాడు (పల్నాడు జిల్లా) Great Indian Bustard (GIB) కోసం ప్రసిద్ధి. GIB అత్యంత అంతరించిపోయే పక్షి; AP రాష్ట్ర జంతువు Blackbuck కూడా ఇక్కడ ఉంటుంది."
    },
    {
        "section_idx": 2,
        "difficulty": "hard",
        "question_te": "పులికాట్ సరస్సు గురించి సరైన వాక్యం ఏది?",
        "opt_a": "భారత్ అతి పెద్ద ఉప్పు సరస్సు",
        "opt_b": "భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు — ఫ్లమింగో వలస",
        "opt_c": "AP లో ఏకైక Ramsar Site",
        "opt_d": "కొరింగ మడ అడవుల కంటే పెద్దది",
        "answer": "B",
        "explanation_te": "పులికాట్ సరస్సు భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు (చిల్కా (ఒడిశా) అతి పెద్దది). ఫ్లమింగో వలస పక్షులకు ముఖ్య నిలయం. SDSC SHAR శ్రీహరికోట పులికాట్ పక్కన ఉంది."
    },
    # Section 3 — ISRO
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "SDSC SHAR నుండి 100వ ప్రయోగం ఏది?",
        "opt_a": "Chandrayaan-3",
        "opt_b": "SpaDeX",
        "opt_c": "NVS-02 / GSLV-F15",
        "opt_d": "Aditya-L1",
        "answer": "C",
        "explanation_te": "జనవరి 29, 2025న GSLV-F15 రాకెట్ ద్వారా NVS-02 ఉపగ్రహం ప్రయోగం SDSC SHAR నుండి 100వ ప్రయోగం. ఇది NavIC నావిగేషన్ కోసం."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "SpaDeX మిషన్ లో ఏమి జరిగింది?",
        "opt_a": "చంద్రుడిపై ల్యాండింగ్",
        "opt_b": "భారత తొలి స్పేస్ డాకింగ్ — SDX01+SDX02",
        "opt_c": "సూర్యుడి అధ్యయనం",
        "opt_d": "మార్స్ ఆర్బిటర్",
        "answer": "B",
        "explanation_te": "SpaDeX (Space Docking Experiment) — డిసెంబర్ 30, 2024న PSLV-C60 ద్వారా ప్రయోగం; జనవరి 16, 2025న SDX01 (Chaser) + SDX02 (Target) స్పేస్ డాకింగ్ సఫలం."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "స్పేస్ డాకింగ్ సాంకేతికత నేర్పడంలో భారత్ ఏ స్థానంలో ఉంది?",
        "opt_a": "మొదటి",
        "opt_b": "రెండవ",
        "opt_c": "మూడవ",
        "opt_d": "నాల్గవ",
        "answer": "D",
        "explanation_te": "USA, Russia, China తర్వాత భారత్ 4వ దేశంగా స్పేస్ డాకింగ్ సాంకేతికత సాధించింది (SpaDeX — జనవరి 2025)."
    },
    {
        "section_idx": 3,
        "difficulty": "hard",
        "question_te": "NVS-02 ఉపగ్రహం ఏ ప్రయోజనం కోసం?",
        "opt_a": "వాతావరణ పరిశీలన",
        "opt_b": "NavIC నావిగేషన్ వ్యవస్థ",
        "opt_c": "రిమోట్ సెన్సింగ్",
        "opt_d": "సైనిక నిఘా",
        "answer": "B",
        "explanation_te": "NVS-02 NavIC (Navigation with Indian Constellation) వ్యవస్థ కోసం. NavIC భారత స్వదేశీ GPS ప్రత్యామ్నాయం."
    },
    # Section 4 — Sports
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "PV సింధు రియో 2016 ఒలింపిక్స్‌లో ఏ పతకం సాధించింది?",
        "opt_a": "స్వర్ణ పతకం",
        "opt_b": "రజత పతకం",
        "opt_c": "కాంస్య పతకం",
        "opt_d": "పతకం రాలేదు",
        "answer": "B",
        "explanation_te": "PV సింధు రియో 2016లో రజత పతకం మరియు టోక్యో 2020లో కాంస్య పతకం సాధించింది. ఆమె రెండు ఒలింపిక్ పతకాలు సాధించిన అరుదైన భారత క్రీడాకారిణి."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "కిడంబి శ్రీకాంత్ ఏ జిల్లాకు చెందినవాడు?",
        "opt_a": "విశాఖపట్నం",
        "opt_b": "గుంటూరు",
        "opt_c": "కర్నూలు",
        "opt_d": "నెల్లూరు",
        "answer": "B",
        "explanation_te": "కిడంబి శ్రీకాంత్ ఫిబ్రవరి 7, 1993న గుంటూరు, AP లో జన్మించాడు. BWF World Championship 2021లో రజత పతకం సాధించాడు."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "2022 Thomas Cup లో భారత్ జట్టులో AP కి చెందిన ముఖ్య సభ్యుడు ఎవరు?",
        "opt_a": "PV సింధు",
        "opt_b": "కిడంబి శ్రీకాంత్",
        "opt_c": "గోపీచంద్",
        "opt_d": "సైనా నెహ్వాల్",
        "answer": "B",
        "explanation_te": "2022 Thomas Cup (పురుషుల టీమ్ బ్యాడ్మింటన్) లో భారత్ తొలిసారి విజయం సాధించింది. శ్రీకాంత్ కీలక సభ్యుడు. ఇది AP గర్వించే విజయం."
    },
    {
        "section_idx": 4,
        "difficulty": "hard",
        "question_te": "PV సింధు 2025లో ఏ పాత్రలో ఎన్నికైంది?",
        "opt_a": "IOC Athletes Commission",
        "opt_b": "BCCI Board Member",
        "opt_c": "BWF Athletes Commission",
        "opt_d": "Olympic Council of Asia",
        "answer": "C",
        "explanation_te": "PV సింధు 2025లో BWF (Badminton World Federation) Athletes Commission సభ్యురాలిగా ఎన్నికైంది — క్రీడా నిర్వహణలో చురుకైన పాత్ర."
    },
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "పారిస్ 2024 Olympics Opening Ceremony లో భారత్ జెండా ఆజమాయిషీదారు ఎవరు?",
        "opt_a": "నీరజ్ చోప్రా",
        "opt_b": "PV సింధు",
        "opt_c": "మనుభాకర్",
        "opt_d": "వినేశ్ ఫోగాట్",
        "answer": "B",
        "explanation_te": "పారిస్ 2024 ఒలింపిక్స్ Opening Ceremony లో PV సింధు భారత్ జెండా ఆజమాయిషీదారు. ఆమె AP / తెలుగు పౌరురాలికి ఇది మరింత గర్వప్రదం."
    },
    # Section 5 — Environment Current Affairs
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "Red Sanders (ఎర్ర చందనం) AP లో ఏ ప్రాంతంలో పెరుగుతుంది?",
        "opt_a": "తీర ఆంధ్ర",
        "opt_b": "ఉత్తరాంధ్ర",
        "opt_c": "రాయలసీమ అడవులు",
        "opt_d": "పాపికొండ",
        "answer": "C",
        "explanation_te": "Red Sanders (Pterocarpus santalinus) ప్రత్యేకంగా రాయలసీమ అడవులలో (నంద్యాల, కర్నూలు జిల్లాలు) పెరుగుతుంది. CITES రక్షిత జాతి."
    },
    # Section 6 — Numbers
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "SDSC SHAR నుండి మొత్తం ప్రయోగాలు డిసెంబర్ 2025 నాటికి ఎన్ని?",
        "opt_a": "75",
        "opt_b": "88",
        "opt_c": "100",
        "opt_d": "104",
        "answer": "D",
        "explanation_te": "డిసెంబర్ 2025 నాటికి SDSC SHAR నుండి మొత్తం 104 ప్రయోగాలు జరిగాయి (88 సఫలం, 5 పాక్షిక, 11 వైఫల్యం)."
    },
    # Section 7 — Rapid revision
    {
        "section_idx": 7,
        "difficulty": "hard",
        "question_te": "పులికాట్ సరస్సు AP లో ఏ ప్రత్యేకత ఉంది?",
        "opt_a": "AP అతి పెద్ద తాజా నీటి సరస్సు",
        "opt_b": "AP లో Ramsar Site; భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు",
        "opt_c": "AP అతి పెద్ద మడ అడవి",
        "opt_d": "AP లో ఏకైక నేషనల్ పార్క్",
        "answer": "B",
        "explanation_te": "పులికాట్ సరస్సు Ramsar Convention Wetland Site; భారత్ 2వ అతి పెద్ద ఉప్పు సరస్సు (మొదటిది చిల్కా, ఒడిశా). ఇక్కడ SDSC SHAR శ్రీహరికోట ఉంది."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "AP రాష్ట్ర జంతువు ఏది?",
        "opt_a": "పులి",
        "opt_b": "ఏనుగు",
        "opt_c": "కృష్ణజింక (Blackbuck)",
        "opt_d": "సింహం",
        "answer": "C",
        "explanation_te": "AP రాష్ట్ర జంతువు కృష్ణజింక (Blackbuck / Indian Antelope). రోళ్లపాడు వన్యప్రాణి అభయారణ్యంలో ప్రసిద్ధి. రాష్ట్ర పక్షి: Indian Rose-ringed Parakeet."
    },

    # --- additional MCQs ---
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'AP లో పాపికొండలు జాతీయ ఉద్యానవనం ఏ జిల్లాలో ఉంది?',
        'opt_a': 'కృష్ణా జిల్లా',
        'opt_b': 'పశ్చిమ గోదావరి, ఏలూరు జిల్లాలు',
        'opt_c': 'కర్నూలు',
        'opt_d': 'శ్రీకాకుళం',
        'answer': 'B',
        'explanation_te': 'పాపికొండలు జాతీయ ఉద్యానవనం పశ్చిమ గోదావరి మరియు ఏలూరు జిల్లాలలో ఉంది. గోదావరి నది ఒడ్డున విస్తరించి ఉన్న ఈ పార్క్ 1,012 చ.కి.మీ విస్తీర్ణం కలిగి ఉంది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం AP వాటా ఎంత?',
        'opt_a': '~1,000 చ.కి.మీ',
        'opt_b': '~2,000 చ.కి.మీ',
        'opt_c': '~3,568 చ.కి.మీ',
        'opt_d': '~500 చ.కి.మీ',
        'answer': 'C',
        'explanation_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం (NSTR) లో AP వాటా ~3,568 చ.కి.మీ. ఇది భారతదేశంలో అతిపెద్ద పులుల అభయారణ్యాలలో ఒకటి.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'AP రాష్ట్రంలో పులుల అభయారణ్యం ఏ పర్వతశ్రేణిలో ఉంది?',
        'opt_a': 'ఎర్ర అడవులు',
        'opt_b': 'నల్లమల కొండలు',
        'opt_c': 'ఆనమల కొండలు',
        'opt_d': 'శేషాచలం కొండలు',
        'answer': 'B',
        'explanation_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం నల్లమల కొండల మధ్య ఉంది. ఇది AP మరియు తెలంగాణ రాష్ట్రాల మధ్య విస్తరించి ఉంది.',
    },
    {
        'section_idx': 0,
        'difficulty': 'easy',
        'question_te': 'AP లో రాజీవ్ గాంధీ జాతీయ ఉద్యానవనం ఎక్కడ ఉంది?',
        'opt_a': 'విశాఖ జిల్లా',
        'opt_b': 'కడప జిల్లా',
        'opt_c': 'కర్నూలు జిల్లా',
        'opt_d': 'నెల్లూరు జిల్లా',
        'answer': 'B',
        'explanation_te': 'రాజీవ్ గాంధీ జాతీయ ఉద్యానవనం (లంకమల NP) కడప జిల్లాలో ఉంది. 353 చ.కి.మీ విస్తీర్ణంతో ఇది AP లో తక్కువ విస్తీర్ణం కలిగిన జాతీయ ఉద్యానవనం.',
    },
    {
        'section_idx': 0,
        'difficulty': 'medium',
        'question_te': 'AP లో ఎర్ర చందనం (Red Sanders) ప్రత్యేకంగా ఏ జిల్లాలో పెరుగుతుంది?',
        'opt_a': 'కృష్ణా',
        'opt_b': 'కడప, తిరుపతి, చిత్తూరు జిల్లాలు',
        'opt_c': 'నెల్లూరు',
        'opt_d': 'కర్నూలు',
        'answer': 'B',
        'explanation_te': 'ఎర్ర చందనం (Red Sanders / రక్తచందనం) రాయలసీమలో ముఖ్యంగా కడప, తిరుపతి, చిత్తూరు జిల్లాలలో పెరుగుతుంది. ఇది CITES రక్షిత జాతి మరియు అంతర్జాతీయంగా చాలా విలువైనది.',
    },
    {
        'section_idx': 1,
        'difficulty': 'easy',
        'question_te': 'పులికాట్ సరస్సు AP కి ఏమిటి?',
        'opt_a': 'మంచినీటి సరస్సు',
        'opt_b': 'భారతదేశంలో 2వ అతి పెద్ద ఉప్పు సరస్సు, ఫ్లమింగో వలస',
        'opt_c': 'హ్రాదరేసర్వాయర్',
        'opt_d': 'ISRO ప్రయోగ కేంద్రం',
        'answer': 'B',
        'explanation_te': 'పులికాట్ సరస్సు భారతదేశంలో 2వ అతి పెద్ద ఉప్పు సరస్సు. ఇది నెల్లూరు జిల్లాలో ఉంది మరియు శీతాకాలంలో ఫ్లమింగో వలసలకు ప్రసిద్ధి.',
    },
    {
        'section_idx': 1,
        'difficulty': 'medium',
        'question_te': 'కోరింగ వన్యప్రాణి అభయారణ్యం ఏ జిల్లాలో ఉంది?',
        'opt_a': 'విశాఖపట్నం',
        'opt_b': 'కాకినాడ (తూర్పు గోదావరి)',
        'opt_c': 'కృష్ణా',
        'opt_d': 'నెల్లూరు',
        'answer': 'B',
        'explanation_te': 'కోరింగ వన్యప్రాణి అభయారణ్యం కాకినాడ జిల్లాలో మడ అడవులకు ప్రసిద్ధి. ఇది ఒలీవ్ రిడ్లీ తాబేళ్ళ గూళ్ళకు ముఖ్యమైన స్థలం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'ISRO SDSC SHAR కేంద్రం ఎక్కడ ఉంది?',
        'opt_a': 'బెంగళూరు',
        'opt_b': 'హైదరాబాద్',
        'opt_c': 'శ్రీహరికోట (నెల్లూరు జిల్లా)',
        'opt_d': 'తిరుపతి',
        'answer': 'C',
        'explanation_te': 'ISRO సతీష్ ధవన్ స్పేస్ సెంటర్ (SDSC SHAR) నెల్లూరు జిల్లా శ్రీహరికోటలో ఉంది. ఇది భారతదేశంలో ప్రయోగ వాహనాల ప్రయోగ కేంద్రం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'SDSC SHAR కేంద్రం ఏ వ్యక్తి పేరిట నామకరణం జరిగింది?',
        'opt_a': 'విక్రమ్ సారాభాయ్',
        'opt_b': 'సతీష్ ధవన్',
        'opt_c': 'APJ అబ్దుల్ కలామ్',
        'opt_d': 'ఉడుపి రామచంద్ర రావు',
        'answer': 'B',
        'explanation_te': 'SDSC SHAR కేంద్రం ISRO మాజీ అధ్యక్షుడు సతీష్ ధవన్ పేరిట నామకరణం జరిగింది. 2002లో ఆయన మరణం తర్వాత ఈ కేంద్రానికి ఆయన పేరు పెట్టారు.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'చంద్రయాన్-3 చంద్రుని దక్షిణ ధ్రువం వద్ద ఎప్పుడు దిగింది?',
        'opt_a': 'ఆగస్టు 14, 2023',
        'opt_b': 'ఆగస్టు 23, 2023',
        'opt_c': 'జూలై 14, 2023',
        'opt_d': 'సెప్టెంబర్ 5, 2023',
        'answer': 'B',
        'explanation_te': 'చంద్రయాన్-3 లాండర్ "విక్రమ్" మరియు రోవర్ "ప్రజ్ఞాన్" ఆగస్టు 23, 2023న చంద్రుని దక్షిణ ధ్రువ ప్రాంతంలో సురక్షితంగా దిగాయి. భారతదేశం ఈ ఘనత సాధించిన 4వ దేశం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'ఆదిత్య-L1 మిషన్ ఏ కోసం పంపబడింది?',
        'opt_a': 'చంద్రుని అధ్యయనానికి',
        'opt_b': 'సూర్యుని అధ్యయనానికి',
        'opt_c': 'అంగారకుని మిషన్',
        'opt_d': 'GPS నేవిగేషన్',
        'answer': 'B',
        'explanation_te': 'ఆదిత్య-L1 సెప్టెంబర్ 2, 2023న ప్రయోగించబడింది. ఇది సూర్యుని అధ్యయనానికి భారతదేశం పంపిన తొలి మిషన్. L1 పాయింట్ వద్ద ఉంచబడింది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'NavIC అంటే ఏమిటి?',
        'opt_a': 'ISRO ఉపగ్రహ ఉప్పు కేంద్రం',
        'opt_b': 'భారత నావిగేషన్ ఉపగ్రహ వ్యవస్థ',
        'opt_c': 'AP నావిక దళం',
        'opt_d': 'ISRO రాకెట్ రకం',
        'answer': 'B',
        'explanation_te': 'NavIC (Navigation with Indian Constellation) భారత స్వంత నావిగేషన్ ఉపగ్రహ వ్యవస్థ. జనవరి 29, 2025న GSLV-F15 ద్వారా NavIC ఉపగ్రహం ప్రయోగించబడింది - ఇది SDSC SHAR శతక ప్రయోగం.',
    },
    {
        'section_idx': 2,
        'difficulty': 'hard',
        'question_te': 'SDSC SHAR కేంద్రం ఏ సంవత్సరంలో 100వ ప్రయోగం సాధించింది?',
        'opt_a': '2023',
        'opt_b': '2024',
        'opt_c': '2025',
        'opt_d': '2026',
        'answer': 'C',
        'explanation_te': 'జనవరి 29, 2025న GSLV-F15 ప్రయోగంతో SDSC SHAR 100వ ప్రయోగం (శతక ప్రయోగం) సాధించింది. ఇది ISRO కి చాలా ముఖ్యమైన మైలురాయి.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'PV సింధు ఏ క్రీడలో ప్రపంచ ప్రసిద్ధి?',
        'opt_a': 'టెన్నిస్',
        'opt_b': 'బ్యాడ్మింటన్',
        'opt_c': 'క్రికెట్',
        'opt_d': 'షూటింగ్',
        'answer': 'B',
        'explanation_te': 'PV సింధు (పుసర్ల వెంకట సింధు) బ్యాడ్మింటన్ క్రీడలో ప్రపంచ ప్రసిద్ధి. ఆమె 2016 (రజత), 2020 (కాంస్య) ఒలింపిక్ పతకాలు మరియు 2019 BWF వరల్డ్ చాంపియన్\u200cషిప్ గెలిచింది.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'PV సింధు కి ఏ ఒలింపిక్ పతకాలు వచ్చాయి?',
        'opt_a': 'బంగారం మరియు రజత',
        'opt_b': '2 బంగారం పతకాలు',
        'opt_c': 'రజత (2016), కాంస్య (2020)',
        'opt_d': 'రజత (2016), బంగారం (2020)',
        'answer': 'C',
        'explanation_te': 'PV సింధు రియో 2016 ఒలింపిక్\u200cలో రజత పతకం, టోక్యో 2020 ఒలింపిక్\u200cలో కాంస్య పతకం గెలిచింది. ఆమె AP, హైదరాబాద్ కి చెందిన ఆటగాళ్ళు.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'AP లో Padma Shri 2020 బ్యాడ్మింటన్ కి ఎవరు పొందారు?',
        'opt_a': 'PV సింధు',
        'opt_b': 'సాయినా నేహ్వాల్',
        'opt_c': 'PV సింధు కోచ్ పుల్లెల గోపీచంద్',
        'opt_d': 'కరణ్ మెహ్తా',
        'answer': 'C',
        'explanation_te': 'పుల్లెల గోపీచంద్ 2014లో Padma Bhushan పొందాడు. ఆయన బ్యాడ్మింటన్ కోచ్ మరియు నాగందల, ప్రకాశం జిల్లా సంబంధీకుడు. 2009లో Dronacharya Award పొందాడు.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'AP లో జన్మించిన రెజ్లర్ సుశీల్ కుమార్ ఒలింపిక్ పతకాలు?',
        'opt_a': 'AP కి సంబంధించినవి కావు',
        'opt_b': 'రజత (2012 లండన్), కాంస్య (2008 బీజింగ్)',
        'opt_c': 'రజత, బంగారం',
        'opt_d': 'కాంస్య రెండు',
        'answer': 'B',
        'explanation_te': 'సుశీల్ కుమార్ రెజ్లింగ్\u200cలో 2008 బీజింగ్\u200cలో కాంస్యం, 2012 లండన్\u200cలో రజతం గెలిచాడు. ఆయన ఢిల్లీ కి చెందినవాడు, AP కి కాదు.',
    },
    {
        'section_idx': 3,
        'difficulty': 'easy',
        'question_te': 'AP లో జన్మించిన ఒలింపిక్ బంగారు పతక విజేత ఎవరు (2024 ప్యారిస్)?',
        'opt_a': 'పీఆర్ శ్రీజేష్',
        'opt_b': 'నీరజ్ చోప్రా',
        'opt_c': 'సాత్విక్ సాయిరాజ్ రాంకిరెడ్డి',
        'opt_d': 'లక్ష్య సేన్',
        'answer': 'C',
        'explanation_te': 'సాత్విక్ సాయిరాజ్ రాంకిరెడ్డి AP (అమలాపురం) కి చెందిన బ్యాడ్మింటన్ ఆటగాడు. 2024 ప్యారిస్ ఒలింపిక్\u200cలో మిక్స్డ్ డబుల్స్\u200cలో వెళ్ళాడు.',
    },
    {
        'section_idx': 3,
        'difficulty': 'hard',
        'question_te': 'ISSF వరల్డ్ చాంపియన్\u200cషిప్\u200cలో 10m ఎయిర్ రైఫిల్\u200cలో AP ఆటగాడు 2023లో సాధించాడు?',
        'opt_a': 'అర్జున్ బబుతా (హర్యానా)',
        'opt_b': 'దివ్యాంశ్ సింగ్ పన్వార్',
        'opt_c': 'సిఫత్ కౌర్ సమ్రా',
        'opt_d': 'ఎల్లేన్ అషిటే',
        'answer': 'A',
        'explanation_te': 'అర్జున్ బబుతా హర్యానాకు చెందినవాడు. AP నుండి షూటింగ్\u200cలో అనేక ఆటగాళ్ళు ఉన్నారు. AP సంబంధిత ప్రశ్న.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'AP లో హంపి ప్రక్కన ఉన్న UNESCO వారసత్వ స్థానం ఏది?',
        'opt_a': 'అమరావతి',
        'opt_b': 'హంపి (కర్ణాటకలో, AP లో కాదు)',
        'opt_c': 'శ్రీశైలం',
        'opt_d': 'లేపాక్షి (గుంటూరు)',
        'answer': 'B',
        'explanation_te': 'హంపి కర్ణాటక రాష్ట్రంలో ఉంది, AP లో కాదు. AP UNESCO వారసత్వ ప్రతిపాదనలో అమరావతి స్తూపం ఉంది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'AP లో ఏ ప్రాజెక్టు జాతీయ ప్రాజెక్టుగా APRA 2014 లో గుర్తించబడింది?',
        'opt_a': 'నాగార్జునసాగర్',
        'opt_b': 'పోలవరం ప్రాజెక్టు',
        'opt_c': 'శ్రీశైలం',
        'opt_d': 'తెలుగుగంగ',
        'answer': 'B',
        'explanation_te': 'పోలవరం ప్రాజెక్టు AP Reorganisation Act 2014 సెక్షన్ 94 ద్వారా జాతీయ ప్రాజెక్టుగా గుర్తించబడింది. ఇది పూర్తిగా కేంద్ర ప్రభుత్వ నిధులతో నిర్మించబడుతుంది.',
    },
    {
        'section_idx': 4,
        'difficulty': 'easy',
        'question_te': 'AP లో మొత్తం అడవుల విస్తీర్ణం సుమారు ఎంత?',
        'opt_a': '10,000 చ.కి.మీ',
        'opt_b': '23,000 చ.కి.మీ',
        'opt_c': '50,000 చ.కి.మీ',
        'opt_d': '5,000 చ.కి.మీ',
        'answer': 'B',
        'explanation_te': 'AP లో మొత్తం అడవుల విస్తీర్ణం సుమారు 23,000 చ.కి.మీ. రాష్ట్ర మొత్తం భూమిలో సుమారు 17% అడవులు ఉన్నాయి.',
    },
    {
        'section_idx': 4,
        'difficulty': 'medium',
        'question_te': 'AP లో కాప్పు సెంచురీ (Kappus Centuary) అంటే ఏమిటి?',
        'opt_a': 'ఆయుర్వేద మొక్కల వనం',
        'opt_b': '100 ఏళ్ళ నాటి చెట్లకు హెరిటేజ్ హోదా',
        'opt_c': 'కాప్పు జాతి రక్షణ ప్రాంతం',
        'opt_d': 'వెదురు అడవి',
        'answer': 'B',
        'explanation_te': 'AP ప్రభుత్వం 100 సంవత్సరాల కంటే పాత చెట్లను Heritage Trees గా ప్రకటించి అడవి కాప్పు (సెంటీనల్ ట్రీ) హోదా ఇస్తుంది.',
    },
    {
        'section_idx': 5,
        'difficulty': 'medium',
        'question_te': 'నాగార్జునసాగర్-శ్రీశైలం పులుల అభయారణ్యం (మొత్తం) ఎంత విస్తీర్ణం కలిగి ఉంది?',
        'opt_a': '~3,500 చ.కి.మీ',
        'opt_b': '~2,000 చ.కి.మీ',
        'opt_c': '~5,000 చ.కి.మీ',
        'opt_d': '~8,000 చ.కి.మీ',
        'answer': 'A',
        'explanation_te': 'NSTR మొత్తం ~3,500 చ.కి.మీ విస్తీర్ణం కలిగి AP-తెలంగాణ రాష్ట్రాల మీదుగా విస్తరించి ఉంది. ఇది భారతదేశంలో అతిపెద్ద పులుల అభయారణ్యాలలో ఒకటి.',
    },
    {
        'section_idx': 5,
        'difficulty': 'easy',
        'question_te': 'AP లో ఏ వన్యప్రాణి అభయారణ్యం ఒలీవ్ రిడ్లీ తాబేళ్ళకు ప్రసిద్ధి?',
        'opt_a': 'నాగార్జునసాగర్',
        'opt_b': 'పాపికొండలు',
        'opt_c': 'కోరింగ',
        'opt_d': 'నెలపట్టు',
        'answer': 'C',
        'explanation_te': 'కోరింగ వన్యప్రాణి అభయారణ్యం కాకినాడ జిల్లాలో ఒలీవ్ రిడ్లీ తాబేళ్ళ గూళ్ళకు ముఖ్యమైన స్థలం. మడ అడవులకు కూడా ప్రసిద్ధి.',
    },
    {
        'section_idx': 6,
        'difficulty': 'medium',
        'question_te': 'AP లో క్లైమేట్ చేంజ్ కార్యాచరణ ప్రణాళికలో ఏ లక్ష్యం ఉంది?',
        'opt_a': '2030 నాటికి 100% పునరుత్పాదక శక్తి',
        'opt_b': '2030 నాటికి కార్బన్ న్యూట్రల్ అవ్వడం',
        'opt_c': 'ఆర్\u200cటీఇ అమలు',
        'opt_d': '1 కోటి ఉద్యోగాలు',
        'answer': 'B',
        'explanation_te': 'AP ప్రభుత్వం Swarnandhra విజన్ లో 2030 నాటికి పర్యావరణ కార్బన్ న్యూట్రల్ లక్ష్యాలను చేర్చింది. గ్రీన్ ఎనర్జీ 10 మార్గదర్శక సూత్రాలలో ఒకటి.',
    },
    {
        'section_idx': 6,
        'difficulty': 'easy',
        'question_te': 'AP లో Solar Energy సంస్థాపన సామర్థ్యం 2024 నాటికి ఎంత?',
        'opt_a': '2 GW',
        'opt_b': '5 GW',
        'opt_c': '9 GW కంటే ఎక్కువ',
        'opt_d': '1 GW',
        'answer': 'C',
        'explanation_te': 'AP 2024 నాటికి 9 GW కంటే ఎక్కువ Solar Energy సంస్థాపన సామర్థ్యం సాధించింది. AP సోలార్ శక్తిలో దేశంలో అగ్రగాముల్లో ఒకటి.',
    },
    {
        'section_idx': 4,
        'difficulty': 'hard',
        'question_te': 'శేషాచలం కొండలలో ఏ ఖనిజం ముఖ్యంగా దొరుకుతుంది?',
        'opt_a': 'బొగ్గు',
        'opt_b': 'ఎర్ర చందనం (Red Sanders)',
        'opt_c': 'ఇనుమురాయి',
        'opt_d': 'అల్యూమినా',
        'answer': 'B',
        'explanation_te': 'శేషాచలం కొండలు (చిత్తూరు, కడప జిల్లాలు) ఎర్ర చందనానికి (Red Sanders) ప్రసిద్ధి. ఇది CITES రక్షిత జాతి మరియు అంతర్జాతీయంగా 1 కిలో $100,000 కంటే ఎక్కువ ధర పలుకుతుంది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'medium',
        'question_te': 'LVM-3 (GSLV Mk3) రాకెట్ ఉపయోగం ఏమిటి?',
        'opt_a': 'చిన్న ఉపగ్రహాలు',
        'opt_b': 'భారీ ఉపగ్రహాల ప్రయోగం',
        'opt_c': 'మిలిటరీ ఉపగ్రహం',
        'opt_d': 'వాతావరణ పరిశోధన',
        'answer': 'B',
        'explanation_te': 'LVM-3 (Launch Vehicle Mark-3) ISRO యొక్క అత్యంత శక్తివంతమైన రాకెట్. చంద్రయాన్-3 మిషన్ ఈ రాకెట్ ద్వారా ప్రయోగించబడింది.',
    },
    {
        'section_idx': 2,
        'difficulty': 'easy',
        'question_te': 'భారతదేశం ఏ మిషన్ తో చంద్రుని దక్షిణ ధ్రువంలో తొలిగా దిగింది?',
        'opt_a': 'చంద్రయాన్-2',
        'opt_b': 'చంద్రయాన్-3',
        'opt_c': 'మంగళయాన్',
        'opt_d': 'ఆదిత్య-L1',
        'answer': 'B',
        'explanation_te': 'చంద్రయాన్-3 ఆగస్టు 23, 2023న చంద్రుని దక్షిణ ధ్రువ ప్రాంతంలో సురక్షితంగా దిగింది. ఈ ఘనత సాధించిన 4వ దేశంగా భారతదేశం నిలిచింది.',
    },
    {
        'section_idx': 3,
        'difficulty': 'medium',
        'question_te': 'AP లో తెలుగు ఆటగాళ్ళు ఆడిన ప్రపంచ కప్ (2023 క్రికెట్) లో మంచి ప్రదర్శన చేసిన ఆటగాడు?',
        'opt_a': 'శుభమన్ గిల్',
        'opt_b': 'KS భరత్ (AP రెడ్డి)',
        'opt_c': 'విరాట్ కోహ్లి',
        'opt_d': 'రోహిత్ శర్మ',
        'answer': 'B',
        'explanation_te': 'KS భరత్ AP కి చెందిన క్రికెటర్. ఆయన 2023 ODI వరల్డ్ కప్ స్క్వాడ్\u200cలో ఉన్నాడు మరియు AP రంజీ జట్టు వికెట్ కీపర్.',
    },
    {
        'section_idx': 1,
        'difficulty': 'medium',
        'question_te': 'AP లో నెలపట్టు అభయారణ్యం ఎందుకు ప్రసిద్ధి?',
        'opt_a': 'పులులు',
        'opt_b': 'ఫ్లమింగో మరియు తెల్ల పెలికాన్లు',
        'opt_c': 'ఏనుగులు',
        'opt_d': 'ఆదివాసీ జాతులు',
        'answer': 'B',
        'explanation_te': 'నెలపట్టు అభయారణ్యం నెల్లూరు జిల్లాలో ఉంది. శీతాకాలంలో ఫ్లమింగో మరియు తెల్ల పెలికాన్లు వలస వస్తాయి, ఇది పక్షి పరిశీలకులకు ప్రసిద్ధ స్థానం.',
    },
    {
        'section_idx': 0,
        'difficulty': 'hard',
        'question_te': 'AP లో ఎన్ని జాతీయ ఉద్యానవనాలు ఉన్నాయి?',
        'opt_a': '1',
        'opt_b': '2',
        'opt_c': '3',
        'opt_d': '4',
        'answer': 'B',
        'explanation_te': 'AP లో 2 జాతీయ ఉద్యానవనాలు ఉన్నాయి: 1) పాపికొండలు జాతీయ ఉద్యానవనం 2) రాజీవ్ గాంధీ జాతీయ ఉద్యానవనం (కడప). NSTR మాత్రం వన్యప్రాణి అభయారణ్యం.',
    },
    {
        'section_idx': 5,
        'difficulty': 'easy',
        'question_te': 'AP లో సెలూరు అభయారణ్యం ఎందుకు ప్రసిద్ధి?',
        'opt_a': 'ఎర్ర చందనం',
        'opt_b': 'నల్ల జింక (Blackbuck)',
        'opt_c': 'పులులు',
        'opt_d': 'ఏనుగులు',
        'answer': 'B',
        'explanation_te': 'సెలూరు అభయారణ్యం ప్రకాశం జిల్లాలో నల్ల జింకలకు (Blackbuck/కృష్ణ జింక) ప్రసిద్ధి. కృష్ణ జింక AP రాష్ట్ర జంతువు.',
    },
]


def _seed_ap_ca_div8_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 8."""
    ph = '%s' if USE_POSTGRES else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT NOT NULL DEFAULT 'GK',
            topic TEXT NOT NULL DEFAULT 'AP_Current_Affairs', subtopic TEXT DEFAULT '',
            chapter_num INTEGER NOT NULL, chapter_title_te TEXT NOT NULL DEFAULT '',
            chapter_title_en TEXT NOT NULL DEFAULT '', pages_ref TEXT DEFAULT '',
            sections_json TEXT NOT NULL DEFAULT '[]', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        if USE_POSTGRES: conn.commit()
    except Exception: pass
    import json as _json
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (8, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (8, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division8', 8,
         'AP పర్యావరణం, ISRO & క్రీడలు',
         'AP Environment, ISRO & Sports',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div8 notes seeded!'}
def _seed_ap_ca_div8_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 8."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (8, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div8_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (8, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print(f"[div8-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    cur2 = db_exec(conn, f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    count = list(row_to_dict_fn(cur2.fetchone()).values())[0]
    if count > 0 and not force:
        return
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    diff_map = {'easy': 1, 'medium': 2, 'hard': 3, 1: 1, 2: 2, 3: 3}
    for mcq in MCQ_DATA:
        diff = diff_map.get(mcq.get('difficulty', 'medium'), 2)
        q_te = mcq.get('question_te', mcq.get('question_te', ''))
        db_exec(conn, insert_sql, (
            note_id,
            mcq['section_idx'],
            diff,
            q_te,
            mcq['opt_a'], mcq['opt_b'], mcq['opt_c'], mcq['opt_d'],
            str(mcq['answer']).lower(),
            mcq['explanation_te']
        ))
    if USE_POSTGRES:
        conn.commit()
    return {'success': True, 'message': f'AP CA Div8 MCQs seeded! Total: {len(MCQ_DATA)}'}
