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

def _seed_ap_ca_div10_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA Division 10."""
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
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (10, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        note_id = row_to_dict(row)['id']
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (10, 'AP_Current_Affairs'))
        if USE_POSTGRES: conn.commit()
    db_exec(conn,
        f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division10', 10,
         'AP పునర్వ్యవస్థీకరణ చట్టం 2014 & సవరణ 2026',
         'AP Reorganisation Act 2014 & Amendment 2026',
         '', _json.dumps(SECTIONS_JSON, ensure_ascii=False)))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'message': 'AP CA Div10 notes seeded!'}
def _seed_ap_ca_div10_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 10 (AP Reorganisation Act 2014)."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn,
        f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
        (10, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div10_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn,
            f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}",
            (10, 'AP_Current_Affairs'))
        row = cur.fetchone()
    if not row:
        print("[div10-mcqs] study_note not found — skipping")
        return
    note_id = row_to_dict(row)['id']
    cur2 = db_exec(conn, f"SELECT COUNT(*) FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    count = list(cur2.fetchone())[0]
    if count > 0 and not force:
        return
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))
    insert_sql = (
        f"INSERT INTO chapter_mcqs "
        f"(study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) "
        f"VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    )
    for mcq in MCQ_DATA:
        # Handle both dict formats: "question"/"options" or "question_te"/"opt_a"-"opt_d"
        q_te = mcq.get('question_te', mcq.get('question', ''))
        if 'options' in mcq:
            opts = mcq['options']
            a, b, c, d = (opts + ['', '', '', ''])[:4]
        else:
            a = mcq.get('opt_a', '')
            b = mcq.get('opt_b', '')
            c = mcq.get('opt_c', '')
            d = mcq.get('opt_d', '')
        correct = str(mcq.get('answer', mcq.get('correct', 'a'))).lower()
        expl = mcq.get('explanation_te', mcq.get('explanation', ''))
        sec = mcq.get('section_idx', 0)
        db_exec(conn, insert_sql, (note_id, sec, 2, q_te, a, b, c, d, correct, expl))
    if USE_POSTGRES:
        conn.commit()
    return {'success': True, 'message': f'AP CA Div10 MCQs seeded! Total: {len(MCQ_DATA)}'}

# Additional MCQs for div10 appended
_EXTRA_MCQ_DATA_10 = [
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "AP Reorganisation Act 2014 Lok Sabha లో ఏ తేదీన ఆమోదం పొందింది?",
        "opt_a": "ఫిబ్రవరి 14, 2014",
        "opt_b": "ఫిబ్రవరి 18, 2014",
        "opt_c": "ఫిబ్రవరి 20, 2014",
        "opt_d": "ఫిబ్రవరి 22, 2014",
        "answer": "B",
        "explanation_te": "APRA 2014 Lok Sabha లో ఫిబ్రవరి 18, 2014న ఆమోదించబడింది. Rajya Sabha ఫిబ్రవరి 20, 2014న ఆమోదించింది."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "APRA 2014 Rajya Sabha లో ఏ తేదీన ఆమోదం పొందింది?",
        "opt_a": "ఫిబ్రవరి 18, 2014",
        "opt_b": "ఫిబ్రవరి 19, 2014",
        "opt_c": "ఫిబ్రవరి 20, 2014",
        "opt_d": "ఫిబ్రవరి 24, 2014",
        "answer": "C",
        "explanation_te": "APRA 2014 Rajya Sabha లో ఫిబ్రవరి 20, 2014న ఆమోదించబడింది. ఇది భారత పార్లమెంట్ ద్వారా చాలా వివాదాస్పదంగా ఆమోదించబడింది."
    },
    {
        "section_idx": 1,
        "difficulty": "medium",
        "question_te": "APRA 2014 Act Number ఏమిటి?",
        "opt_a": "Act No. 2 of 2014",
        "opt_b": "Act No. 4 of 2014",
        "opt_c": "Act No. 6 of 2014",
        "opt_d": "Act No. 10 of 2014",
        "answer": "C",
        "explanation_te": "Andhra Pradesh Reorganisation Act, 2014 — Act No. 6 of 2014. ఇది జూన్ 2, 2014న అమల్లోకి వచ్చింది."
    },
    {
        "section_idx": 1,
        "difficulty": "easy",
        "question_te": "తెలంగాణ భారతదేశంలో ఎన్నవ రాష్ట్రంగా ఏర్పడింది?",
        "opt_a": "27వ",
        "opt_b": "28వ",
        "opt_c": "29వ",
        "opt_d": "30వ",
        "answer": "C",
        "explanation_te": "జూన్ 2, 2014న APRA 2014 అమలుతో తెలంగాణ భారతదేశంలో 29వ రాష్ట్రంగా అవతరించింది."
    },
    {
        "section_idx": 2,
        "difficulty": "easy",
        "question_te": "APRA 2014 Section 30 దేనికి సంబంధించినది?",
        "opt_a": "పోలవరం ప్రాజెక్టు",
        "opt_b": "AP High Court ఏర్పాటు",
        "opt_c": "జల వివాదాలు",
        "opt_d": "ఆస్తుల విభజన",
        "answer": "B",
        "explanation_te": "APRA 2014 Section 30 AP కోసం ప్రత్యేక High Court ఏర్పాటు గురించి. ఇది జనవరి 1, 2019న అమరావతిలో ప్రారంభమైంది."
    },
    {
        "section_idx": 2,
        "difficulty": "medium",
        "question_te": "APRA 2014 ఏ Section పోలవరం ప్రాజెక్టును జాతీయ ప్రాజెక్టుగా ప్రకటించింది?",
        "opt_a": "Section 5",
        "opt_b": "Section 30",
        "opt_c": "Section 90",
        "opt_d": "Section 94",
        "answer": "D",
        "explanation_te": "APRA 2014 Section 94 పోలవరం ప్రాజెక్టును (Indira Sagar Project) జాతీయ ప్రాజెక్టుగా ప్రకటించింది. కేంద్ర ప్రభుత్వం పూర్తి నిధులు అందించాలి."
    },
    {
        "section_idx": 2,
        "difficulty": "hard",
        "question_te": "APRA 2014 Section 5(2) దేనికి సంబంధించినది?",
        "opt_a": "హైదరాబాద్ ఉమ్మడి రాజధాని",
        "opt_b": "AP రాజధాని నగర ఏర్పాటు (2026 సవరణ ద్వారా అమరావతి)",
        "opt_c": "పోలవరం నిర్మాణం",
        "opt_d": "జల పంపకం",
        "answer": "B",
        "explanation_te": "APRA 2014 Section 5(2) మొదట AP రాజధాని గురించి పేర్కొంది. 2026 సవరణ ద్వారా ఇది అమరావతి అని నిర్దిష్టంగా పేర్కొనబడింది."
    },
    {
        "section_idx": 3,
        "difficulty": "easy",
        "question_te": "హైదరాబాద్ ఎంత కాలం ఉమ్మడి రాజధానిగా ఉండాలని APRA 2014 నిర్ణయించింది?",
        "opt_a": "5 సంవత్సరాలు",
        "opt_b": "10 సంవత్సరాలు",
        "opt_c": "15 సంవత్సరాలు",
        "opt_d": "అనిర్దిష్టంగా",
        "answer": "B",
        "explanation_te": "APRA 2014 ప్రకారం హైదరాబాద్ AP-తెలంగాణ రెండు రాష్ట్రాలకు 10 సంవత్సరాలు (2014-2024) ఉమ్మడి రాజధానిగా ఉంటుంది."
    },
    {
        "section_idx": 3,
        "difficulty": "medium",
        "question_te": "Special Category Status (SCS) డిమాండ్ ఎవరు AP కి వాగ్దానం చేశారు?",
        "opt_a": "నరేంద్ర మోదీ",
        "opt_b": "మన్మోహన్ సింగ్",
        "opt_c": "రాహుల్ గాంధీ",
        "opt_d": "పి.వి. నరసింహారావు",
        "answer": "B",
        "explanation_te": "మన్మోహన్ సింగ్ (UPA ప్రభుత్వం) APRA 2014 ఆమోదం సమయంలో AP కి Special Category Status ఇస్తామని వాగ్దానం చేశారు. కానీ ఇది ఇంకా చట్టపూర్వకంగా అమలు కాలేదు."
    },
    {
        "section_idx": 3,
        "difficulty": "hard",
        "question_te": "AP-తెలంగాణ ఆస్తుల విభజన నిష్పత్తి ఏమిటి?",
        "opt_a": "50:50",
        "opt_b": "60:40",
        "opt_c": "58.32:41.68 (AP:TG)",
        "opt_d": "70:30",
        "answer": "C",
        "explanation_te": "APRA 2014 ప్రకారం ఉమ్మడి AP ఆస్తులు 58.32% (AP) : 41.68% (తెలంగాణ) నిష్పత్తిలో జనాభా ఆధారంగా విభజించబడ్డాయి."
    },
    {
        "section_idx": 4,
        "difficulty": "easy",
        "question_te": "14వ ఆర్థిక సంఘం AP SCS డిమాండ్ పై ఏ నిర్ణయం తీసుకుంది?",
        "opt_a": "SCS మంజూరు చేసింది",
        "opt_b": "SCS రద్దు చేసి Special Package ప్రతిపాదించింది",
        "opt_c": "నిర్ణయం వాయిదా వేసింది",
        "opt_d": "AP కి ఎటువంటి రాయితీలు ఇవ్వలేదు",
        "answer": "B",
        "explanation_te": "14వ ఆర్థిక సంఘం (2015) SCS పద్ధతిని రద్దు చేయాలని సిఫారసు చేసింది మరియు AP కి Special Package పద్ధతిలో నిధులు ఇవ్వాలని సూచించింది."
    },
    {
        "section_idx": 5,
        "difficulty": "easy",
        "question_te": "AP Reorganisation Amendment Act 2026 Act Number ఏమిటి?",
        "opt_a": "Act No. 5 of 2026",
        "opt_b": "Act No. 6 of 2026",
        "opt_c": "Act No. 7 of 2026",
        "opt_d": "Act No. 10 of 2026",
        "answer": "C",
        "explanation_te": "AP Reorganisation Amendment Act 2026 — Act No. 7 of 2026. ఇది అమరావతిని AP అధికారిక రాజధానిగా పేర్కొంది."
    },
    {
        "section_idx": 5,
        "difficulty": "medium",
        "question_te": "2026 Amendment Act Lok Sabha లో ఏ తేదీన ఆమోదం పొందింది?",
        "opt_a": "మార్చి 31, 2026",
        "opt_b": "ఏప్రిల్ 1, 2026",
        "opt_c": "ఏప్రిల్ 2, 2026",
        "opt_d": "ఏప్రిల్ 6, 2026",
        "answer": "B",
        "explanation_te": "2026 AP Reorganisation Amendment Act Lok Sabha లో ఏప్రిల్ 1, 2026న ఆమోదించబడింది. Rajya Sabha ఏప్రిల్ 2 న, రాష్ట్రపతి ఏప్రిల్ 6న ఆమోదించారు."
    },
    {
        "section_idx": 6,
        "difficulty": "medium",
        "question_te": "G.O.610 దేనికి సంబంధించినది?",
        "opt_a": "పోలవరం ప్రాజెక్టు",
        "opt_b": "AP విద్య-ఉద్యోగాలలో 6 Zones రోస్టర్ సిస్టమ్",
        "opt_c": "జల వివాదాలు",
        "opt_d": "రాజధాని నిర్మాణం",
        "answer": "B",
        "explanation_te": "G.O.610 AP లో విద్య-ఉద్యోగాలను 6 Zones లో విభజించి స్థానికులకు రక్షణ కల్పించే రోస్టర్ సిస్టమ్ గురించి. ఆర్టికల్ 371-D కింద అమలైంది."
    },
    {
        "section_idx": 6,
        "difficulty": "easy",
        "question_te": "States Reorganisation Act 1956 ఏ ఆధారంగా రాష్ట్రాలను ఏర్పాటు చేసింది?",
        "opt_a": "మతం",
        "opt_b": "భాష",
        "opt_c": "జాతి",
        "opt_d": "ఆర్థిక అభివృద్ధి",
        "answer": "B",
        "explanation_te": "States Reorganisation Act 1956 భాష ఆధారంగా రాష్ట్రాలను పునర్వ్యవస్థీకరించింది. ఫజల్ అలీ కమిషన్ నివేదిక ఆధారంగా అమలైంది. తెలుగు మాట్లాడే ప్రాంతాలు కలిసి AP ఏర్పాటైంది."
    },
    {
        "section_idx": 7,
        "difficulty": "hard",
        "question_te": "AP Reorganisation Amendment Act No. 19 of 2014 దేనికి సంబంధించినది?",
        "opt_a": "రాజధాని నిర్ణయం",
        "opt_b": "7 మండలాలు ఖమ్మం జిల్లా నుండి AP కి బదిలీ",
        "opt_c": "పోలవరం ఆమోదం",
        "opt_d": "SCS మంజూరు",
        "answer": "B",
        "explanation_te": "Amendment Act No. 19 of 2014 (జూలై 11, 2014) ఖమ్మం జిల్లా నుండి 7 మండలాలను తూ/ప గోదావరి జిల్లాలకు బదిలీ చేసింది. పోలవరం ప్రాజెక్టు నిర్మాణం కోసం."
    },
    {
        "section_idx": 7,
        "difficulty": "medium",
        "question_te": "APRA 2014 ప్రకారం పోలవరం ప్రాజెక్టు నిర్మాణ నిధులు ఎవరు భరించాలి?",
        "opt_a": "AP రాష్ట్ర ప్రభుత్వం",
        "opt_b": "కేంద్ర ప్రభుత్వం పూర్తిగా",
        "opt_c": "AP-తెలంగాణ సమానంగా",
        "opt_d": "ప్రైవేట్ సంస్థలు",
        "answer": "B",
        "explanation_te": "APRA 2014 Section 94 ప్రకారం పోలవరం జాతీయ ప్రాజెక్టుగా కేంద్ర ప్రభుత్వం పూర్తి నిధులు అందించాలి. ఇది AP రాష్ట్రానికి గొప్ప ప్రయోజనం."
    },
    {
        "section_idx": 8,
        "difficulty": "easy",
        "question_te": "AP Reorganisation Act 2014 Rajya Sabha లో ఎందుకు వివాదాస్పదంగా ఆమోదించబడింది?",
        "opt_a": "ఆర్థిక కారణాలు",
        "opt_b": "Voting లేకుండా Voice Vote ద్వారా విపక్షాల నిరసన మధ్య ఆమోదించడం",
        "opt_c": "సరైన నోటీసు ఇవ్వకుండా",
        "opt_d": "రాష్ట్రపతి ఆమోదం లేకుండా",
        "answer": "B",
        "explanation_te": "APRA 2014 Rajya Sabha లో ఫిబ్రవరి 20, 2014న విపక్షాల తీవ్ర నిరసన మధ్య Voice Vote ద్వారా ఆమోదించబడింది. AP నుండి సభ్యులు వాకవుట్ చేశారు."
    },
    {
        "section_idx": 0,
        "difficulty": "medium",
        "question_te": "AP రాజ్యాంగ పరిషత్ (State Constituent Assembly) ఎప్పుడు రద్దు అయింది?",
        "opt_a": "1950",
        "opt_b": "1956",
        "opt_c": "1960",
        "opt_d": "AP కి ప్రత్యేక రాజ్యాంగ పరిషత్ లేదు",
        "answer": "D",
        "explanation_te": "AP ఒక భారత రాష్ట్రం. రాష్ట్రాలకు ప్రత్యేక రాజ్యాంగాలు ఉండవు — భారత రాజ్యాంగం మాత్రమే వర్తిస్తుంది."
    },
    {
        "section_idx": 0,
        "difficulty": "easy",
        "question_te": "ఉమ్మడి AP (Undivided AP) ఏ సంవత్సరాల మధ్య ఉంది?",
        "opt_a": "1950–2014",
        "opt_b": "1953–2014",
        "opt_c": "1956–2014",
        "opt_d": "1947–2014",
        "answer": "C",
        "explanation_te": "ఉమ్మడి ఆంధ్రప్రదేశ్ నవంబర్ 1, 1956 (రాష్ట్రాల పునర్వ్యవస్థీకరణ) నుండి జూన్ 1, 2014 (APRA అమలు) వరకు 58 సంవత్సరాలు ఉంది."
    }
]

MCQ_DATA = MCQ_DATA + _EXTRA_MCQ_DATA_10
