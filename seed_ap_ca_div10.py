"""
seed_ap_ca_div10.py
AP Current Affairs — Chapter 10: AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div10_s1",
        "title": "పరీక్ష కోసం కీలక భావనలు",
        "summary": "APRA 2014 అమలు: జూన్ 2, 2014; హైదరాబాద్ 10 సం. ఉమ్మడి; Act No. 6/2014; Amendment 2026: Act No. 7/2026"
    },
    {
        "id": "div10_s2",
        "title": "APRA 2014 — మూల చట్టం వివరాలు",
        "summary": "Lok Sabha: ఫిబ్రవరి 18, 2014; Rajya Sabha: ఫిబ్రవరి 20, 2014; అమలు: జూన్ 2, 2014; తెలంగాణ 29వ రాష్ట్రం"
    },
    {
        "id": "div10_s3",
        "title": "కీలక Sections — 5, 30, 90",
        "summary": "Section 5(2): రాజధాని నిర్ణయం (2026లో సవరణ); Section 30: AP HC ఏర్పాటు; Section 90: పోలవరం జాతీయ ప్రాజెక్టు"
    },
    {
        "id": "div10_s4",
        "title": "Special Category Status (SCS)",
        "summary": "మన్మోహన్ సింగ్ వాగ్దానం (2014); 14వ ఆర్థిక సంఘం రద్దు సిఫారసు (2015); చట్టరూపం లేదు; ఇంకా అమలు కాలేదు"
    },
    {
        "id": "div10_s5",
        "title": "Amendment Act 2026 — అమరావతి రాజధాని",
        "summary": "AP Reorganisation Amendment Act 2026, Act No. 7/2026; Lok Sabha ఏప్రిల్ 1; Rajya Sabha ఏప్రిల్ 2; రాష్ట్రపతి ఏప్రిల్ 6; అమరావతి జూన్ 2, 2024 నుండి (Retrospective)"
    },
    {
        "id": "div10_s6",
        "title": "Article 371-D & చారిత్రక నేపథ్యం",
        "summary": "Article 371-D: 32వ సవరణ 1973; G.O.610 6 Zones; States Reorganisation Act 1956; ఉమ్మడి AP నవంబర్ 1, 1956"
    },
    {
        "id": "div10_s7",
        "title": "7 మండలాల బదిలీ — ఖమ్మం నుండి AP కి",
        "summary": "APRA Amendment Act No. 19/2014 (జూలై 11, 2014); 7 మండలాలు ఖమ్మం → తూ/ప గోదావరి; పోలవరం కోసం; తెలంగాణ 5 గ్రామాల డిమాండ్"
    },
    {
        "id": "div10_s8",
        "title": "Rapid Revision — పరీక్ష పట్టిక",
        "summary": "APRA 2014 అన్ని కీలక తేదీలు, Sections, Amendment 2026 వివరాలు — సంక్షిప్త పట్టిక"
    }
], ensure_ascii=False)

MCQ_DATA = [
    # Section 0 — Key concepts
    {
        "section_idx": 0,
        "question": "Andhra Pradesh Reorganisation Act, 2014 అమల్లోకి వచ్చిన తేదీ ఏది?",
        "options": ["మే 2, 2014", "జూన్ 2, 2014", "జూలై 2, 2014", "ఆగస్టు 2, 2014"],
        "answer": "B",
        "explanation": "APRA 2014 జూన్ 2, 2014న అమల్లోకి వచ్చింది. ఇదే తేదీన తెలంగాణ 29వ రాష్ట్రంగా అవతరించింది."
    },
    {
        "section_idx": 0,
        "question": "APRA 2014 ప్రకారం హైదరాబాద్ ఎన్ని సంవత్సరాలు ఉభయ రాష్ట్రాలకు ఉమ్మడి రాజధానిగా ఉంటుంది?",
        "options": ["5 సంవత్సరాలు", "8 సంవత్సరాలు", "10 సంవత్సరాలు", "15 సంవత్సరాలు"],
        "answer": "C",
        "explanation": "APRA 2014 ప్రకారం హైదరాబాద్ 10 సంవత్సరాలు (2014–2024) AP మరియు తెలంగాణ రెండు రాష్ట్రాలకూ ఉమ్మడి రాజధానిగా ఉంటుంది."
    },
    {
        "section_idx": 0,
        "question": "AP Reorganisation Act 2014 యొక్క Act Number ఏది?",
        "options": ["Act No. 4 of 2014", "Act No. 6 of 2014", "Act No. 8 of 2014", "Act No. 10 of 2014"],
        "answer": "B",
        "explanation": "AP Reorganisation Act 2014 యొక్క Act Number = Act No. 6 of 2014. 2026 Amendment Act Number = Act No. 7 of 2026."
    },
    # Section 1 — APRA 2014 full details
    {
        "section_idx": 1,
        "question": "APRA 2014కి Lok Sabha ఎప్పుడు ఆమోదం తెలిపింది?",
        "options": ["జనవరి 18, 2014", "ఫిబ్రవరి 18, 2014", "మార్చి 18, 2014", "ఏప్రిల్ 18, 2014"],
        "answer": "B",
        "explanation": "APRA 2014కి Lok Sabha ఫిబ్రవరి 18, 2014న మరియు Rajya Sabha ఫిబ్రవరి 20, 2014న ఆమోదం తెలిపాయి. రాష్ట్రపతి మార్చి 1, 2014న సంతకం చేశారు."
    },
    {
        "section_idx": 1,
        "question": "తెలంగాణ భారతదేశంలో ఎన్నవ రాష్ట్రంగా ఏర్పాటైంది?",
        "options": ["27వ రాష్ట్రం", "28వ రాష్ట్రం", "29వ రాష్ట్రం", "30వ రాష్ట్రం"],
        "answer": "C",
        "explanation": "తెలంగాణ జూన్ 2, 2014న భారతదేశంలో 29వ రాష్ట్రంగా అవతరించింది. ప్రస్తుతం 28 రాష్ట్రాలు ఉన్నాయి (J&K UT అయినందున)."
    },
    {
        "section_idx": 1,
        "question": "APRA 2014 ప్రకారం నూతన ఆంధ్రప్రదేశ్ ఎన్ని జిల్లాలతో ఏర్పాటైంది?",
        "options": ["10 జిల్లాలు", "13 జిల్లాలు", "15 జిల్లాలు", "17 జిల్లాలు"],
        "answer": "B",
        "explanation": "APRA 2014 అమలైన జూన్ 2, 2014న నూతన ఆంధ్రప్రదేశ్ 13 జిల్లాలతో ఏర్పాటైంది. తర్వాత 2022 ఏప్రిల్‌లో 26 జిల్లాలుగా, 2026లో 28 జిల్లాలుగా పెరిగాయి."
    },
    # Section 2 — Key Sections
    {
        "section_idx": 2,
        "question": "APRA 2014 యొక్క ఏ Section ఆంధ్రప్రదేశ్ రాజధాని నిర్ణయానికి సంబంధించినది?",
        "options": ["Section 3", "Section 5(2)", "Section 24", "Section 30"],
        "answer": "B",
        "explanation": "APRA 2014 Section 5(2) AP రాజధాని నిర్ణయానికి సంబంధించిన section. దీన్ని 2026 Amendment Act లో సవరించి అమరావతిని అధికారిక రాజధానిగా నిర్ణయించారు."
    },
    {
        "section_idx": 2,
        "question": "APRA 2014 Section 30 దేనికి సంబంధించినది?",
        "options": ["SCS హోదా", "పోలవరం ప్రాజెక్టు", "AP High Court ఏర్పాటు", "నీటి పంపకం"],
        "answer": "C",
        "explanation": "APRA 2014 Section 30 AP కి ప్రత్యేక High Court ఏర్పాటుకు సంబంధించినది. దీని ప్రకారం కేంద్ర ప్రభుత్వానికి AP HC స్థాపించే బాధ్యత ఉంది. AP HC జనవరి 1, 2019న అమరావతిలో ఏర్పాటైంది."
    },
    {
        "section_idx": 2,
        "question": "APRA 2014 Section 90 దేనికి సంబంధించినది?",
        "options": ["Article 371-D", "పోలవరం జాతీయ ప్రాజెక్టు", "Special Category Status", "AP HC"],
        "answer": "B",
        "explanation": "APRA 2014 Section 90 పోలవరం ప్రాజెక్టుకు జాతీయ ప్రాజెక్టు హోదా కల్పించింది. దీని ప్రకారం కేంద్ర ప్రభుత్వం పోలవరం నిధులు పూర్తిగా భరించాలి."
    },
    {
        "section_idx": 2,
        "question": "AP High Court ఏ తేదీన అమరావతిలో ఏర్పాటైంది?",
        "options": ["జూన్ 2, 2017", "జనవరి 1, 2019", "మార్చి 1, 2019", "జూలై 1, 2020"],
        "answer": "B",
        "explanation": "APRA 2014 Section 30 కింద AP కి ప్రత్యేక High Court జనవరి 1, 2019న అమరావతిలో ఏర్పాటైంది. Justice Rakesh Kumar మొదటి Chief Justice."
    },
    # Section 3 — SCS
    {
        "section_idx": 3,
        "question": "AP కి Special Category Status ఇస్తామని 2014లో ఎవరు వాగ్దానం చేశారు?",
        "options": ["నరేంద్ర మోదీ ప్రభుత్వం", "మన్మోహన్ సింగ్ ప్రభుత్వం", "అటల్ బిహారీ వాజ్‌పేయి ప్రభుత్వం", "చంద్రబాబు నాయుడు"],
        "answer": "B",
        "explanation": "2014 APRA Rajya Sabha చర్చ సందర్భంగా మన్మోహన్ సింగ్ నేతృత్వంలోని UPA ప్రభుత్వం AP కి SCS ఇస్తామని వాగ్దానం చేసింది. కానీ ఇది చట్టరూపం తీసుకోలేదు."
    },
    {
        "section_idx": 3,
        "question": "14వ ఆర్థిక సంఘం SCS విషయంలో ఏమి సిఫారసు చేసింది?",
        "options": ["AP కి SCS ఇవ్వాలి", "SCS విధానాన్నే రద్దు చేయాలి", "SCS ని 5 సంవత్సరాలు పొడిగించాలి", "SCS కి బదులు వేరే ప్యాకేజీ ఇవ్వాలి"],
        "answer": "B",
        "explanation": "14వ ఆర్థిక సంఘం (2015) SCS విధానాన్నే రద్దు చేయాలని సిఫారసు చేసింది. ఈ సిఫారసు అమలైంది, దీంతో AP కి SCS ఇచ్చే వీలు లేకుండా పోయింది."
    },
    # Section 4 — Amendment Act 2026
    {
        "section_idx": 4,
        "question": "AP Reorganisation (Amendment) Act, 2026 యొక్క Act Number ఏది?",
        "options": ["Act No. 5 of 2026", "Act No. 7 of 2026", "Act No. 9 of 2026", "Act No. 11 of 2026"],
        "answer": "B",
        "explanation": "AP Reorganisation (Amendment) Act, 2026 యొక్క Act Number = Act No. 7 of 2026. ఇది 2014 మూల చట్టం (Act No. 6 of 2014) Section 5(2) ని సవరించింది."
    },
    {
        "section_idx": 4,
        "question": "అమరావతి బిల్లుకు Lok Sabha ఏ తేదీన ఆమోదం తెలిపింది?",
        "options": ["మార్చి 28, 2026", "ఏప్రిల్ 1, 2026", "ఏప్రిల్ 2, 2026", "ఏప్రిల్ 6, 2026"],
        "answer": "B",
        "explanation": "అమరావతి బిల్లుకు Lok Sabha ఏప్రిల్ 1, 2026న మరియు Rajya Sabha ఏప్రిల్ 2, 2026న ఆమోదం తెలిపాయి. రాష్ట్రపతి ద్రౌపదీ ముర్ము ఏప్రిల్ 6, 2026న సంతకం చేశారు."
    },
    {
        "section_idx": 4,
        "question": "Amendment Act 2026 ప్రకారం అమరావతి ఏ తేదీ నుండి అధికారిక రాజధాని?",
        "options": ["ఏప్రిల్ 6, 2026 నుండి", "మార్చి 28, 2026 నుండి", "జూన్ 2, 2024 నుండి (Retrospective)", "జనవరి 1, 2025 నుండి"],
        "answer": "C",
        "explanation": "Amendment Act 2026 Retrospective గా (వెనక్కి వర్తించే విధంగా) జూన్ 2, 2024 నుండి అమరావతిని అధికారిక రాజధానిగా గుర్తించింది. చట్టం 2026లో ఆమోదించినా, అమరావతి 2024 జూన్ 2 నుండే అధికారిక రాజధాని."
    },
    {
        "section_idx": 4,
        "question": "అమరావతి బిల్లుపై రాష్ట్రపతి ఏ అధికారం కింద సంతకం చేశారు?",
        "options": ["Article 108", "Article 111", "Article 368", "Article 131"],
        "answer": "B",
        "explanation": "రాష్ట్రపతి ద్రౌపదీ ముర్ము Article 111 కింద తమ అధికారాలను ఉపయోగించి అమరావతి బిల్లుపై సంతకం చేశారు. Article 111 — రాష్ట్రపతి Bills కి అంగీకారం తెలిపే Article."
    },
    {
        "section_idx": 4,
        "question": "AP అసెంబ్లీ అమరావతిని రాజధానిగా ప్రకటించాలని కేంద్రానికి ఎప్పుడు తీర్మానం పంపింది?",
        "options": ["మార్చి 28, 2026", "ఫిబ్రవరి 28, 2026", "ఏప్రిల్ 1, 2026", "జనవరి 28, 2026"],
        "answer": "A",
        "explanation": "AP శాసనసభ మార్చి 28, 2026న అమరావతిని రాజధానిగా ప్రకటించాలని కేంద్రానికి తీర్మానం పంపింది. దీన్ని ఆధారంగా కేంద్రం APRA Section 5(2) సవరణ బిల్లు ప్రవేశపెట్టింది."
    },
    # Section 5 — Article 371-D
    {
        "section_idx": 5,
        "question": "Article 371-D ఏ రాజ్యాంగ సవరణ ద్వారా చేర్చబడింది?",
        "options": ["22వ సవరణ, 1969", "32వ సవరణ, 1973", "42వ సవరణ, 1976", "44వ సవరణ, 1978"],
        "answer": "B",
        "explanation": "Article 371-D ని 32వ రాజ్యాంగ సవరణ చట్టం, 1973 ద్వారా ఉమ్మడి AP కి ప్రత్యేక సంరక్షణ కల్పించేందుకు చేర్చారు. ఇది విద్య మరియు ఉద్యోగాల్లో స్థానికత ఆధారంగా రాయితీలు ఇవ్వడానికి అనుమతిస్తుంది."
    },
    {
        "section_idx": 5,
        "question": "ఉమ్మడి AP (States Reorganisation Act 1956 కింద) ఎప్పుడు ఏర్పాటైంది?",
        "options": ["అక్టోబర్ 1, 1953", "నవంబర్ 1, 1956", "జూన్ 2, 1956", "జనవరి 26, 1957"],
        "answer": "B",
        "explanation": "States Reorganisation Act 1956 కింద భాష ఆధారంగా నవంబర్ 1, 1956న ఉమ్మడి ఆంధ్రప్రదేశ్ ఏర్పాటైంది. అక్టోబర్ 1, 1953న ప్రత్యేక ఆంధ్ర రాష్ట్రం (హైదరాబాద్ లేకుండా) ఏర్పాటైంది."
    },
    {
        "section_idx": 5,
        "question": "APRA 2014 ప్రకారం AP లో Rajya Sabha స్థానాలు ఎన్ని?",
        "options": ["7 స్థానాలు", "9 స్థానాలు", "11 స్థానాలు", "13 స్థానాలు"],
        "answer": "C",
        "explanation": "APRA 2014 Section 24 ప్రకారం AP కి 11 Rajya Sabha స్థానాలు, 25 Lok Sabha స్థానాలు, 175 అసెంబ్లీ స్థానాలు ఉన్నాయి."
    },
    # Section 6 — 7 Mandals Transfer
    {
        "section_idx": 6,
        "question": "పోలవరం ప్రాజెక్టు కోసం తెలంగాణ నుండి AP కి బదిలీ చేసిన మండలాల సంఖ్య ఎన్ని?",
        "options": ["5 మండలాలు", "7 మండలాలు", "9 మండలాలు", "11 మండలాలు"],
        "answer": "B",
        "explanation": "APRA Amendment Act 2014 (Act No. 19/2014) ద్వారా తెలంగాణలోని ఖమ్మం జిల్లా నుండి 7 మండలాలు AP కి బదిలీ చేశారు. పోలవరం జాతీయ ప్రాజెక్టు నిర్మాణ ప్రాంతం AP పరిధిలో ఉండేందుకు ఇది చేశారు."
    },
    {
        "section_idx": 6,
        "question": "7 మండలాల బదిలీకి సంబంధించిన AP Reorganisation (Amendment) Act, 2014 యొక్క Act Number ఏది?",
        "options": ["Act No. 6 of 2014", "Act No. 9 of 2014", "Act No. 19 of 2014", "Act No. 25 of 2014"],
        "answer": "C",
        "explanation": "పోలవరం కోసం 7 మండలాల బదిలీకి AP Reorganisation (Amendment) Act, 2014 — Act No. 19 of 2014 పాస్ చేశారు (జూలై 11, 2014). ఇది మూల APRA Act No. 6/2014 కంటే వేరు."
    },
    {
        "section_idx": 6,
        "question": "7 మండలాల బదిలీ చట్టాన్ని Lok Sabha ఎప్పుడు ఆమోదించింది?",
        "options": ["జూన్ 2, 2014", "జూలై 11, 2014", "ఆగస్టు 15, 2014", "సెప్టెంబర్ 1, 2014"],
        "answer": "B",
        "explanation": "7 మండలాల బదిలీ చట్టం (Act No. 19/2014) జూలై 11, 2014న Lok Sabha ఆమోదించింది. ఈ మండలాలు ఖమ్మం జిల్లా నుండి తూర్పు, పశ్చిమ గోదావరి జిల్లాలకు వెళ్ళాయి."
    },
    {
        "section_idx": 6,
        "question": "7 మండలాల్లో తూర్పు గోదావరి జిల్లాలో చేర్చిన మండలం ఏది?",
        "options": ["కుకుణూరు", "వేలేర్పాడు", "కునవరం", "బుర్గంపాడు"],
        "answer": "C",
        "explanation": "కునవరం, వి.ఆర్.పురం, చింతూరు, నెల్లిపాక మండలాలు తూర్పు గోదావరి జిల్లాలో చేర్చారు. వేలేర్పాడు, బుర్గంపాడు, కుకుణూరు పశ్చిమ గోదావరి జిల్లాలో చేర్చారు."
    },
    {
        "section_idx": 6,
        "question": "తెలంగాణ తిరిగి తమకు ఇవ్వాలని డిమాండ్ చేస్తున్న 5 గ్రామాలు ఏ ప్రాంతానికి సంబంధించినవి?",
        "options": ["నల్గొండ", "వరంగల్", "భద్రాచలం", "ఖమ్మం పట్టణం"],
        "answer": "C",
        "explanation": "తెలంగాణ ఏటపాక, కన్నాయిగూడెం, పుచ్చుకలపాడు, పురుషోత్తమపట్నం, గుండాల అనే 5 గ్రామాలు భద్రాచలం డివిజన్ పరిధిలో ఉన్నాయని, అవి పోలవరం మునక ప్రాంతం వెలుపల ఉన్నాయని వాదిస్తోంది."
    },
]

# ── Helper functions ──────────────────────────────────────────────────────────

def _seed_ap_ca_div10_notes_inner(c, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Insert div10 HTML notes into study_notes table."""
    here = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(here, "static", "notes", "ap_ca_div10_notes.html")
    if not os.path.exists(html_path):
        print("[div10] HTML file not found:", html_path)
        return

    with open(html_path, encoding="utf-8") as fh:
        html_content = fh.read()

    if USE_POSTGRES:
        existing = db_exec(c,
            "SELECT id FROM study_notes WHERE topic='AP_Current_Affairs' AND chapter_num=10")
        row = existing.fetchone()
    else:
        existing = db_exec(c,
            "SELECT id FROM study_notes WHERE topic='AP_Current_Affairs' AND chapter_num=10")
        row = existing.fetchone()

    if row:
        if force:
            if USE_POSTGRES:
                db_exec(c,
                    "UPDATE study_notes SET title=%s, content=%s, sections_json=%s "
                    "WHERE topic='AP_Current_Affairs' AND chapter_num=10",
                    ("AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026", html_content, SECTIONS_JSON))
            else:
                db_exec(c,
                    "UPDATE study_notes SET title=?, content=?, sections_json=? "
                    "WHERE topic='AP_Current_Affairs' AND chapter_num=10",
                    ("AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026", html_content, SECTIONS_JSON))
    else:
        if USE_POSTGRES:
            db_exec(c,
                "INSERT INTO study_notes (topic, chapter_num, title, content, sections_json) "
                "VALUES (%s,%s,%s,%s,%s)",
                ("AP_Current_Affairs", 10,
                 "AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026",
                 html_content, SECTIONS_JSON))
        else:
            db_exec(c,
                "INSERT INTO study_notes (topic, chapter_num, title, content, sections_json) "
                "VALUES (?,?,?,?,?)",
                ("AP_Current_Affairs", 10,
                 "AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026",
                 html_content, SECTIONS_JSON))


def _seed_ap_ca_div10_mcqs_inner(c, db_exec, row_to_dict, USE_POSTGRES):
    """Insert div10 MCQs into chapter_mcqs table."""
    if USE_POSTGRES:
        note_row = db_exec(c,
            "SELECT id FROM study_notes WHERE topic='AP_Current_Affairs' AND chapter_num=10"
        ).fetchone()
    else:
        note_row = db_exec(c,
            "SELECT id FROM study_notes WHERE topic='AP_Current_Affairs' AND chapter_num=10"
        ).fetchone()

    if not note_row:
        print("[div10-mcqs] study_note not found — skipping MCQ seed")
        return

    note_id = row_to_dict(note_row)["id"] if callable(row_to_dict) else note_row[0]

    if USE_POSTGRES:
        existing = db_exec(c,
            "SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id=%s", (note_id,))
    else:
        existing = db_exec(c,
            "SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id=?", (note_id,))

    count = list(existing.fetchone())[0]
    if count >= len(MCQ_DATA):
        return  # already seeded

    if USE_POSTGRES:
        db_exec(c, "DELETE FROM chapter_mcqs WHERE study_note_id=%s", (note_id,))
    else:
        db_exec(c, "DELETE FROM chapter_mcqs WHERE study_note_id=?", (note_id,))

    for idx, mcq in enumerate(MCQ_DATA):
        opts = mcq["options"]
        if USE_POSTGRES:
            db_exec(c,
                "INSERT INTO chapter_mcqs "
                "(study_note_id, section_idx, question, opt_a, opt_b, opt_c, opt_d, answer, explanation) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (note_id, mcq["section_idx"], mcq["question"],
                 opts[0], opts[1], opts[2], opts[3],
                 mcq["answer"], mcq["explanation"]))
        else:
            db_exec(c,
                "INSERT INTO chapter_mcqs "
                "(study_note_id, section_idx, question, opt_a, opt_b, opt_c, opt_d, answer, explanation) "
                "VALUES (?,?,?,?,?,?,?,?,?)",
                (note_id, mcq["section_idx"], mcq["question"],
                 opts[0], opts[1], opts[2], opts[3],
                 mcq["answer"], mcq["explanation"]))

    print(f"[div10-mcqs] Inserted {len(MCQ_DATA)} MCQs for div10.")
