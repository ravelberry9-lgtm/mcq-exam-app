"""
seed_ap_ca_div7.py
AP Current Affairs — Chapter 7: AP చరిత్ర & స్వాతంత్ర్య సమరయోధులు
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div7_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "summary": "AP చారిత్రిక స్వరూపం, పరీక్ష మూలాంశాలు — రాజవంశాల క్రమం, రాజధానులు, స్వాతంత్ర్య సమరయోధుల తేదీలు"
    },
    {
        "id": "div7_s2",
        "title": "ప్రాచీన రాజవంశాలు",
        "summary": "సాతవాహనులు, ఇక్ష్వాకులు, పూర్వ చాళుక్యులు (వేంగి), కాకతీయులు, విజయనగర సామ్రాజ్యం, రెడ్డి రాజ్యం, కుతుబ్ షాహీలు, నిజాంలు"
    },
    {
        "id": "div7_s3",
        "title": "స్వాతంత్ర్య సమరయోధులు",
        "summary": "అల్లూరి సీతారామ రాజు, పొట్టి శ్రీరాముల్లు, ఉయ్యాలవాడ నరసింహారెడ్డి, టంగుటూరి ప్రకాశం పంతులు, కందుకూరి వీరేశలింగం"
    },
    {
        "id": "div7_s4",
        "title": "AP రాష్ట్రం ఏర్పాటు — చారిత్రిక క్రమం",
        "summary": "1920 డిమాండ్ → 1952 పొట్టి నిరాహారదీక్ష → అక్టో 1, 1953 ఆంధ్ర రాష్ట్రం → నవం 1, 1956 AP ఏర్పాటు → 2014 విభజన"
    },
    {
        "id": "div7_s5",
        "title": "ముఖ్య వ్యక్తులు",
        "summary": "సర్ ఆర్థర్ కాటన్, విశ్వనాధ సత్యనారాయణ, నీలం సంజీవ రెడ్డి, దుర్గాబాయి దేశ్‌ముఖ్"
    },
    {
        "id": "div7_s6",
        "title": "చారిత్రిక స్మారకాలు — ఇటీవలి కరెంట్ అఫైర్స్",
        "summary": "అమరావతి UNESCO ప్రతిపాదన, అల్లూరి 125వ జయంతి 2022, అమరజీవి దినం డిసె 15, AP Formation Day నవం 1"
    },
    {
        "id": "div7_s7",
        "title": "ముఖ్య పురావస్తు / చారిత్రిక ప్రాంతాలు",
        "summary": "అమరావతి స్తూప, నాగార్జునకొండ, హంపి, వేంగి, కొండవీడు కోట, లేపాక్షి"
    },
    {
        "id": "div7_s8",
        "title": "పరీక్ష రేపిడ్ రివిజన్",
        "summary": "రాజవంశాలు, స్వాతంత్ర్య సమరయోధులు, AP ఏర్పాటు తేదీలు — సంక్షిప్త పట్టిక"
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Concepts
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "ఆంధ్రప్రదేశ్ రాష్ట్రం ఏ తేదీన ఏర్పాటైంది?",
        "opt_a": "అక్టోబర్ 1, 1953",
        "opt_b": "నవంబర్ 1, 1956",
        "opt_c": "జనవరి 26, 1950",
        "opt_d": "జూన్ 2, 2014",
        "answer": "B",
        "explanation_te": "నవంబర్ 1, 1956న States Reorganisation Act ద్వారా ఆంధ్ర రాష్ట్రం + హైదరాబాద్ తెలుగు జిల్లాలు కలిపి ఆంధ్రప్రదేశ్ ఏర్పాటైంది. అక్టోబర్ 1, 1953న ఆంధ్ర రాష్ట్రం (హైదరాబాద్ లేకుండా) ఏర్పాటైంది."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "ఆంధ్ర రాష్ట్రం ఏర్పాటైనప్పుడు మొదటి రాజధాని ఏది?",
        "opt_a": "హైదరాబాద్",
        "opt_b": "విశాఖపట్నం",
        "opt_c": "కర్నూలు",
        "opt_d": "అమరావతి",
        "answer": "C",
        "explanation_te": "1953 అక్టోబర్ 1న ఆంధ్ర రాష్ట్రం ఏర్పాటైనప్పుడు కర్నూలు రాజధాని. 1956లో AP ఏర్పడినప్పుడు హైదరాబాద్ రాజధానైంది."
    },
    # Section 1 — Dynasties
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "సాతవాహనుల ముఖ్య రాజధాని ఏది?",
        "opt_a": "వరంగల్",
        "opt_b": "అమరావతి / ధాన్యకటకం",
        "opt_c": "హంపి",
        "opt_d": "గోల్కొండ",
        "answer": "B",
        "explanation_te": "సాతవాహనుల ముఖ్య రాజధాని అమరావతి (ధాన్యకటకం). ఇక్కడే ప్రసిద్ధ అమరావతి బుద్ధిస్ట్ మహాస్తూపం నిర్మించారు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "కాకతీయుల రాజధాని ఏది? వారు ఏ సంవత్సరంలో పతనమయ్యారు?",
        "opt_a": "హంపి — 1565",
        "opt_b": "వరంగల్ — 1323",
        "opt_c": "కొండవీడు — 1450",
        "opt_d": "వేంగి — 1130",
        "answer": "B",
        "explanation_te": "కాకతీయుల రాజధాని వరంగల్ (ఓరుగల్లు). 1323లో ఢిల్లీ సుల్తాన్ ఘియాజుద్దీన్ తుగ్లక్ చేత పతనమయ్యారు."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "విజయనగర సామ్రాజ్యం ఎవరు స్థాపించారు?",
        "opt_a": "కృష్ణదేవరాయలు",
        "opt_b": "గణపతి దేవుడు",
        "opt_c": "హరిహర I + బుక్క రాయ I",
        "opt_d": "గౌతమీపుత్ర సాతకర్ణి",
        "answer": "C",
        "explanation_te": "1336లో హరిహర I మరియు బుక్క రాయ I విజయనగర సామ్రాజ్యం స్థాపించారు. కృష్ణదేవరాయలు తర్వాత కాలపు గొప్ప పాలకుడు."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "కృష్ణదేవరాయలుకు ఏ బిరుదు ఉంది?",
        "opt_a": "మన్యం వీరుడు",
        "opt_b": "ఆంధ్రభోజుడు",
        "opt_c": "ఆంధ్ర కేసరి",
        "opt_d": "అమరజీవి",
        "answer": "B",
        "explanation_te": "కృష్ణదేవరాయలు (1509–1529) 'ఆంధ్రభోజుడు' బిరుదు వహించాడు. అల్లసాని పెద్దన అష్ట దిగ్గజ కవులలో ప్రముఖుడు ఆయన ఆస్థానంలో ఉండేవాడు."
    },
    {
        "section_idx": 1,
        "difficulty": "hard",
        "question_te": "మొదటి మహిళా కాకతీయ పాలకురాలు ఎవరు? ఆమె గురించి మార్కో పోలో రాశాడు.",
        "opt_a": "కమలాదేవి",
        "opt_b": "రుద్రమదేవి",
        "opt_c": "చాందు బీబీ",
        "opt_d": "ఇందిరమ్మ",
        "answer": "B",
        "explanation_te": "రుద్రమదేవి కాకతీయ సామ్రాజ్యం మొదటి మహిళా పాలకురాలు. ఇటలీ యాత్రికుడు మార్కో పోలో ఆమె సమర్థ పరిపాలన గురించి అభివర్ణించాడు."
    },
    # Section 2 — Freedom Fighters
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "అల్లూరి సీతారామ రాజుకు ఏ బిరుదు ఉంది?",
        "opt_a": "అమరజీవి",
        "opt_b": "ఆంధ్ర కేసరి",
        "opt_c": "మన్యం వీరుడు",
        "opt_d": "కవిసమ్రాట్",
        "answer": "C",
        "explanation_te": "'మన్యం వీరుడు' అంటే అటవీ గిరిజన ప్రాంతపు వీరుడు అని అర్థం. అల్లూరి 1922–24 రంప తిరుగుబాటు నడిపాడు."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "అల్లూరి సీతారామ రాజు ఏ తేదీన మరణించాడు?",
        "opt_a": "మే 7, 1924",
        "opt_b": "డిసెంబర్ 15, 1952",
        "opt_c": "మే 4, 1898",
        "opt_d": "అక్టోబర్ 19, 1922",
        "answer": "A",
        "explanation_te": "అల్లూరి సీతారామ రాజు మే 7, 1924న కోయూరు వద్ద బ్రిటీష్ పోలీసులచే మరణించాడు. ఆయన జననం 1897/1898 మే 4."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "పొట్టి శ్రీరాముల్లు నిరాహారదీక్ష ఎన్ని రోజులు చేశాడు?",
        "opt_a": "21 రోజులు",
        "opt_b": "48 రోజులు",
        "opt_c": "58 రోజులు",
        "opt_d": "76 రోజులు",
        "answer": "C",
        "explanation_te": "పొట్టి శ్రీరాముల్లు అక్టోబర్ 19, 1952 నుండి డిసెంబర్ 15, 1952 వరకు 58 రోజులు నిరాహారదీక్ష చేశాడు. 58వ రోజు మరణించాడు."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "పొట్టి శ్రీరాముల్లుకు ఏ బిరుదు ఉంది?",
        "opt_a": "మన్యం వీరుడు",
        "opt_b": "అమరజీవి",
        "opt_c": "ఆంధ్ర కేసరి",
        "opt_d": "ఆంధ్రభోజుడు",
        "answer": "B",
        "explanation_te": "'అమరజీవి' అంటే అమరత్వం పొందిన జీవుడు అని అర్థం. పొట్టి శ్రీరాముల్లు ఆంధ్ర రాష్ట్రం కోసం జీవత్యాగం చేశాడు."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "ఉయ్యాలవాడ నరసింహారెడ్డి తిరుగుబాటు ఏ కాలంలో జరిగింది? ఇది ఎందుకు ముఖ్యం?",
        "opt_a": "1857 — మొదటి స్వాతంత్ర్య సంగ్రామం",
        "opt_b": "1922 — అసహకార ఉద్యమం",
        "opt_c": "1846–47 — 1857కి ముందే సాయుధ తిరుగుబాటు",
        "opt_d": "1942 — క్విట్ ఇండియా",
        "answer": "C",
        "explanation_te": "ఉయ్యాలవాడ 1846–47లో కర్నూలు జిల్లాలో తిరుగుబాటు నడిపాడు — 1857 సిపాయి తిరుగుబాటుకు 10 సంవత్సరాల ముందే. ఇది AP లో మొట్టమొదటి సాయుధ ప్రతిఘటన."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "టంగుటూరి ప్రకాశం పంతులుకు ఏ బిరుదు ఉంది?",
        "opt_a": "అమరజీవి",
        "opt_b": "ఆంధ్ర కేసరి",
        "opt_c": "మన్యం వీరుడు",
        "opt_d": "రాయలసీమ సింహం",
        "answer": "B",
        "explanation_te": "'ఆంధ్ర కేసరి' (Lion of Andhra) బిరుదు టంగుటూరి ప్రకాశం పంతులుది. ఆయన ఆంధ్ర రాష్ట్రం మొదటి ముఖ్యమంత్రి (1953–54)."
    },
    # Section 3 — AP Formation
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "ఆంధ్ర రాష్ట్రం (హైదరాబాద్ లేకుండా) ఏ తేదీన ఏర్పాటైంది?",
        "opt_a": "నవంబర్ 1, 1956",
        "opt_b": "అక్టోబర్ 1, 1953",
        "opt_c": "జనవరి 26, 1950",
        "opt_d": "జూన్ 2, 2014",
        "answer": "B",
        "explanation_te": "అక్టోబర్ 1, 1953న మద్రాస్ ప్రెసిడెన్సీ నుండి తెలుగు జిల్లాలు వేరు పడి ఆంధ్ర రాష్ట్రం ఏర్పాటైంది. రాజధాని కర్నూలు."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "AP Formation Day ఏ తేదీన జరుపుకుంటారు?",
        "opt_a": "అక్టోబర్ 1",
        "opt_b": "జనవరి 26",
        "opt_c": "నవంబర్ 1",
        "opt_d": "డిసెంబర్ 15",
        "answer": "C",
        "explanation_te": "నవంబర్ 1, 1956న ఆంధ్రప్రదేశ్ రాష్ట్రం ఏర్పాటైంది కాబట్టి నవంబర్ 1ని AP రాష్ట్ర అవతరణ దినంగా జరుపుకుంటారు."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "AP రాష్ట్రం మొదటి ముఖ్యమంత్రి ఎవరు?",
        "opt_a": "టంగుటూరి ప్రకాశం పంతులు",
        "opt_b": "నీలం సంజీవ రెడ్డి",
        "opt_c": "కాసు బ్రహ్మానంద రెడ్డి",
        "opt_d": "జలగం వెంగళరావు",
        "answer": "B",
        "explanation_te": "నీలం సంజీవ రెడ్డి AP రాష్ట్రం (నవం 1, 1956) మొదటి ముఖ్యమంత్రి. ప్రకాశం పంతులు ఆంధ్ర రాష్ట్రం (1953) మొదటి CM."
    },
    {
        "section_idx": 3,
        "difficulty": "hard",
        "question_te": "AP విభజన జరిగిన తేదీ ఏది? AP మరియు తెలంగాణ అయ్యాయి.",
        "opt_a": "జనవరి 1, 2014",
        "opt_b": "మార్చి 1, 2014",
        "opt_c": "జూన్ 2, 2014",
        "opt_d": "అక్టోబర్ 1, 2014",
        "answer": "C",
        "explanation_te": "Andhra Pradesh Reorganisation Act 2014 ప్రకారం జూన్ 2, 2014న AP రెండు రాష్ట్రాలైంది — AP మరియు తెలంగాణ. హైదరాబాద్ 10 సంవత్సరాలు ఉమ్మడి రాజధాని."
    },
    # Section 4 — Notable People
    {
        "section_idx": 4,
        "difficulty": "medium",
        "question_te": "నీలం సంజీవ రెడ్డి తర్వాత ఏ పదవి చేపట్టారు?",
        "opt_a": "AP ముఖ్యమంత్రి (రెండవసారి)",
        "opt_b": "భారత రాష్ట్రపతి",
        "opt_c": "భారత ప్రధానమంత్రి",
        "opt_d": "AP గవర్నర్",
        "answer": "B",
        "explanation_te": "నీలం సంజీవ రెడ్డి AP మొదటి CM తర్వాత 1977–82 కాలంలో భారత రాష్ట్రపతి అయ్యారు. ఆయన Lok Sabha Speaker కూడా అయ్యారు."
    },
    # Section 5 — Recent Events
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "2022లో అల్లూరి సీతారామ రాజు ఏ జయంతి జరిగింది?",
        "opt_a": "100వ జయంతి",
        "opt_b": "125వ జయంతి",
        "opt_c": "150వ జయంతి",
        "opt_d": "75వ జయంతి",
        "answer": "B",
        "explanation_te": "అల్లూరి జననం 1897 కాబట్టి 2022లో 125వ జయంతి జరుపుకున్నారు. PM మోదీ భీమవరంలో 30 అడుగుల కాంస్య విగ్రహం ఆవిష్కరించారు."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "అమరజీవి దినం ఏ తేదీన జరుపుకుంటారు?",
        "opt_a": "అక్టోబర్ 1",
        "opt_b": "అక్టోబర్ 19",
        "opt_c": "డిసెంబర్ 15",
        "opt_d": "మార్చి 16",
        "answer": "C",
        "explanation_te": "పొట్టి శ్రీరాముల్లు డిసెంబర్ 15, 1952న మరణించాడు కాబట్టి డిసెంబర్ 15ని అమరజీవి దినంగా జరుపుతారు."
    },
    # Section 6 — Heritage Sites
    {
        "section_idx": 6,
        "difficulty": "easy",
        "question_te": "ఇక్ష్వాకుల రాజధాని ఏది?",
        "opt_a": "అమరావతి",
        "opt_b": "విజయపురి (నాగార్జునకొండ)",
        "opt_c": "వేంగి",
        "opt_d": "కొండవీడు",
        "answer": "B",
        "explanation_te": "ఇక్ష్వాకులు (క్రీ.శ. 3వ శతాబ్దం) విజయపురి (నాగార్జునకొండ) రాజధానిగా పాలించారు. నాగార్జున సాగర్ నిర్మించినప్పుడు ఆ ప్రాంతం జలంలో మునిగింది."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "లేపాక్షి గుడి ఏ రాజవంశ కళకు నిదర్శనం?",
        "opt_a": "కాకతీయ",
        "opt_b": "సాతవాహన",
        "opt_c": "విజయనగర",
        "opt_d": "నిజాం",
        "answer": "C",
        "explanation_te": "లేపాక్షి (శ్రీసత్యసాయి జిల్లా) విజయనగర కాలంలో నిర్మించారు. 'వేలాడే స్తంభం', నంది విగ్రహం ప్రసిద్ధి. AP లో ముఖ్య పర్యాటక ప్రాంతం."
    },
    # Section 7 — Rapid Revision
    {
        "section_idx": 7,
        "difficulty": "hard",
        "question_te": "క్రింది జతపరచు: (1) అమరజీవి (2) మన్యం వీరుడు (3) ఆంధ్ర కేసరి (4) ఆంధ్రభోజుడు",
        "opt_a": "పొట్టి శ్రీరాముల్లు, అల్లూరి, ప్రకాశం, కృష్ణదేవరాయలు",
        "opt_b": "అల్లూరి, పొట్టి శ్రీరాముల్లు, ప్రకాశం, కృష్ణదేవరాయలు",
        "opt_c": "ప్రకాశం, అల్లూరి, పొట్టి శ్రీరాముల్లు, కృష్ణదేవరాయలు",
        "opt_d": "పొట్టి శ్రీరాముల్లు, ప్రకాశం, అల్లూరి, కృష్ణదేవరాయలు",
        "answer": "A",
        "explanation_te": "అమరజీవి = పొట్టి శ్రీరాముల్లు; మన్యం వీరుడు = అల్లూరి సీతారామ రాజు; ఆంధ్ర కేసరి = టంగుటూరి ప్రకాశం పంతులు; ఆంధ్రభోజుడు = కృష్ణదేవరాయలు."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "States Reorganisation Act ఏ సంవత్సరం వచ్చింది? దాని ఫలితమేమిటి?",
        "opt_a": "1950 — రిపబ్లిక్ ఏర్పాటు",
        "opt_b": "1956 — భాష ఆధారంగా రాష్ట్రాల విభజన",
        "opt_c": "1953 — ఆంధ్ర రాష్ట్రం",
        "opt_d": "1962 — చైనా యుద్ధం",
        "answer": "B",
        "explanation_te": "1956 States Reorganisation Act భాష ఆధారంగా భారత రాష్ట్రాలను పునర్వ్యవస్థీకరించింది. ఫజల్ అలీ కమిషన్ నివేదిక ఆధారంగా అమలైంది. ఫలితంగా నవం 1, 1956న AP ఏర్పాటైంది."
    },
]


def _seed_ap_ca_div7_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA chapter 7 (AP History & Freedom Fighters)."""
    existing = db_exec(
        conn,
        "SELECT id FROM study_notes WHERE topic=%s AND chapter_num=%s",
        ("AP_Current_Affairs", 7)
    )
    rows = [row_to_dict(r) for r in existing]
    if rows and not force:
        return

    html_path = os.path.join(
        os.path.dirname(__file__),
        "static", "notes", "ap_ca_div7_notes.html"
    )
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    sections = json.loads(SECTIONS_JSON)
    sections_data = json.dumps(sections, ensure_ascii=False)

    if rows:
        db_exec(
            conn,
            "UPDATE study_notes SET title=%s, content=%s, sections=%s WHERE topic=%s AND chapter_num=%s",
            (
                "AP చరిత్ర & స్వాతంత్ర్య సమరయోధులు",
                html_content,
                sections_data,
                "AP_Current_Affairs",
                7
            )
        )
    else:
        ph = "%s" if USE_POSTGRES else "?"

        def _ph(q):
            return q if USE_POSTGRES else q.replace("%s", "?")

        db_exec(
            conn,
            _ph(
                "INSERT INTO study_notes (topic, chapter_num, title, content, sections) "
                "VALUES (%s, %s, %s, %s, %s)"
            ),
            (
                "AP_Current_Affairs",
                7,
                "AP చరిత్ర & స్వాతంత్ర్య సమరయోధులు",
                html_content,
                sections_data
            )
        )


def _seed_ap_ca_div7_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 7 (AP History & Freedom Fighters)."""
    existing = db_exec(
        conn,
        "SELECT id FROM chapter_mcqs WHERE topic=%s AND chapter_num=%s",
        ("AP_Current_Affairs", 7)
    )
    rows = [row_to_dict(r) for r in existing]
    if rows and not force:
        return
    if rows and force:
        db_exec(
            conn,
            "DELETE FROM chapter_mcqs WHERE topic=%s AND chapter_num=%s",
            ("AP_Current_Affairs", 7)
        )

    def _ph(q):
        return q if USE_POSTGRES else q.replace("%s", "?")

    for mcq in MCQ_DATA:
        db_exec(
            conn,
            _ph(
                "INSERT INTO chapter_mcqs "
                "(topic, chapter_num, section_idx, difficulty, question_te, "
                "opt_a, opt_b, opt_c, opt_d, answer, explanation_te) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            ),
            (
                "AP_Current_Affairs",
                7,
                mcq["section_idx"],
                mcq["difficulty"],
                mcq["question_te"],
                mcq["opt_a"],
                mcq["opt_b"],
                mcq["opt_c"],
                mcq["opt_d"],
                mcq["answer"],
                mcq["explanation_te"],
            )
        )
