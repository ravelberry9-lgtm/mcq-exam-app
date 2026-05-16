"""
seed_ap_ca_div6.py
AP Current Affairs — Chapter 6: AP ఆర్థిక వ్యవస్థ, పరిశ్రమలు & మౌలిక సదుపాయాలు
Complete seed file with 60 MCQs in tuple format and seed functions
"""

import os
import json

SECTIONS_JSON = json.dumps([
    {
        "id": "div6_s0",
        "title": "AP GSDP & ఆర్థిక స్నాప్‌షాట్ 2024-25",
        "summary": "GSDP ₹16.41 లక్షల కోట్లు, వృద్ధి 12.5%, వాస్తవ వృద్ధి 8.21% (7వ స్థానం), GDP సహకారం 4.72%"
    },
    {
        "id": "div6_s1",
        "title": "Swarnandhra 2047 విజన్",
        "summary": "2047 లక్ష్యం GSDP $2.4T, తలసరి $43000, నిరంతర వృద్ధి 15%, 10 మార్గదర్శక సూత్రాలు"
    },
    {
        "id": "div6_s2",
        "title": "AP వ్యవసాయ & జలసంపద rankings",
        "summary": "AP 1వ: మిరపకాయ, కోకో (41%), ఆయిల్ పాం, టమాట, నిమ్మ; 2వ: మామిడి, జీడిపప్పు; రొయ్యల 70%"
    },
    {
        "id": "div6_s3",
        "title": "CII Partnership Summit 2025",
        "summary": "30వ సదస్సు, నవం 14-15, విశాఖపట్నం; ₹13.26 లక్ష పెట్టుబడులు, 613 MoU, 16.31 లక్ష ఉద్యోగాలు"
    },
    {
        "id": "div6_s4",
        "title": "Google AI Hub & Quantum Computing",
        "summary": "$15B పెట్టుబడి, విశాఖపట్నం AI hub, అమెరికా తర్వాత ప్రపంచంలో 2వ, IBM Quantum 133-Qubit"
    },
    {
        "id": "div6_s5",
        "title": "ArcelorMittal Steel & ఖనిజ సంపద",
        "summary": "AMNS నక్కపల్లి, ₹1.5 లక్ష పెట్టుబడి, 24 MT సామర్థ్యం, Heavy Minerals 359.79 MT"
    },
    {
        "id": "div6_s6",
        "title": "మౌలిక సదుపాయాలు — పోర్టులు, విమానాశ్రయాలు",
        "summary": "విశాఖ Major పోర్టు, 5 Non-major, 3 అంతర్జాతీయ విమానాశ్రయాలు, భోగాపురం GMR Group"
    }
], ensure_ascii=False)

# 60 MCQs in tuple format: (section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct_letter, explanation_te)
MCQ_DATA = [
    # Section 0: GSDP & Economic Snapshot (10 MCQs)
    (0, 1, "AP GSDP (2024-25) ప్రస్తుత ధరలు ఎంత?", "₹15.2 లక్షల కోట్లు", "₹16.41 లక్షల కోట్లు", "₹17.5 లక్షల కోట్లు", "₹18 లక్షల కోట్లు", "b", "AP GSDP 2024-25: ₹16.41 లక్షల కోట్లు (12.5% వృద్ధి)."),
    (0, 1, "AP దేశ GDP లో సహకారం ఎంత?", "3.2%", "4.72%", "5.5%", "6.1%", "b", "జాతీయ GDP లో AP సహకారం 4.72%."),
    (0, 2, "AP రియల్ వృద్ధిరేటు 2024-25 దేశంలో ఏ స్థానం?", "3వ", "5వ", "7వ", "9వ", "c", "AP వాస్తవ వృద్ధిరేటు 8.21% — దేశంలో 7వ స్థానం."),
    (0, 1, "AP తలసరి ఆదాయం?", "₹1,50,000", "₹2,00,000", "₹2,66,240", "₹3,10,000", "c", "AP తలసరి ఆదాయం ₹2,66,240 — జాతీయ సగటుకు 1.3 రెట్లు."),
    (0, 2, "AP ఆర్థిక rank దేశంలో?", "5వ", "7వ", "9వ", "11వ", "c", "AP 9వ స్థానం."),
    (0, 1, "AP బడ్జెట్ 2025-26?", "₹2.5 లక్షల కోట్లు", "₹3,22,359 కోట్లు", "₹3.8 లక్షల కోట్లు", "₹4.1 లక్షల కోట్లు", "b", "AP బడ్జెట్ 2025-26: ₹3,22,359 కోట్లు."),
    (0, 2, "AP GSVA లో పరిశ్రమల నిష్పత్తి?", "15.8%", "21.16%", "28.5%", "35.2%", "b", "AP GSVA: సేవలు 41.64%, వ్యవసాయం 37.20%, పరిశ్రమలు 21.16%."),
    (0, 3, "GST వసూళ్లు 2025-26 (4 నెలలు) లక్ష్యంలో ఎంత శాతం?", "45%", "52%", "61%", "72%", "c", "GST వసూళ్లు ₹16,754 కోట్లు — వార్షిక లక్ష్యంలో 61%."),
    (0, 2, "AP సేవల రంగ GSVA వాటా?", "35%", "41.64%", "48%", "52%", "b", "సేవల రంగం GSVA లో 41.64%."),
    (0, 1, "AP GSDP వృద్ధిరేటు 2024-25?", "8%", "10.5%", "12.5%", "14%", "c", "GSDP వృద్ధిరేటు 12.5%."),

    # Section 1: Swarnandhra 2047 (10 MCQs)
    (1, 1, "Swarnandhra 2047 విజన్ ఆవిష్కారం ఎప్పుడు?", "సెప్టెంబర్ 2024", "నవంబర్ 2024", "డిసెంబర్ 14, 2024", "జనవరి 2025", "c", "Swarnandhra 2047 డిసెంబర్ 14, 2024న CM చంద్రబాబు ఆవిష్కారం."),
    (1, 1, "Swarnandhra 2047 GSDP లక్ష్యం?", "$1.5 ట్రిలియన్", "$1.8 ట్రిలియన్", "$2.4 ట్రిలియన్", "$3 ట్రిలియన్", "c", "2047 లక్ష్యం: GSDP $2.4 ట్రిలియన్."),
    (1, 2, "Swarnandhra నిరంతర వృద్ధిరేటు?", "10%", "12%", "15%", "18%", "c", "నిరంతర వృద్ధిరేటు లక్ష్యం 15%."),
    (1, 1, "Swarnandhra 2047 మార్గదర్శక సూత్రాలు సంఖ్య?", "7", "8", "10", "12", "c", "10 మార్గదర్శక సూత్రాలు."),
    (1, 3, "Swarnandhra Action Units ఏ స్థాయిలో అందిస్తున్నారు?", "జిల్లా", "అసెంబ్లీ నియోజకవర్గం", "మండలం", "పాఞ్చాయితీ", "b", "175 అసెంబ్లీ నియోజకవర్గాలలో Action Units."),
    (1, 1, "తలసరి ఆదాయ లక్ష్యం?", "$25,000", "$35,000", "$43,000", "$50,000", "c", "తలసరి ఆదాయ లక్ష్యం $43,000."),
    (1, 2, "Green Energy సూత్రం స్థానం?", "చిన్న అంశం", "ఐచ్ఛిక", "10 సూత్రాలలో ఒకటి", "నిర్ణయ సమయం", "c", "Green Energy 10 సూత్రాలలో ఒకటి."),
    (1, 1, "పేదరిక నిర్మూలన స్థానం?", "చిన్న", "ఐచ్ఛిక", "1వ సూత్రం", "లేదు", "c", "పేదరిక నిర్మూలన 1వ సూత్రం."),
    (1, 2, "నీటి భద్రత Swarnandhra లో?", "చిన్న భాగం", "రెండవ ప్రాధాన్యం", "ముఖ్య సూత్రం", "చిన్న", "c", "నీటి భద్రత ముఖ్య సూత్రాలలో ఒకటి."),
    (1, 1, "Swarnandhra 2047 అవిష్కారం చేసిన వ్యక్తి?", "నెలూర్ జూన్", "చంద్రబాబు నాయుడు", "లోకేష్ నాయుడు", "కమిటీ", "b", "CM చంద్రబాబు నాయుడు ఆవిష్కారం."),

    # Section 2: AP Agriculture Rankings (10 MCQs)
    (2, 1, "AP ఏ పంటల సాగులో దేశంలో 1వ స్థానం?", "గోధుమ", "మిరపకాయ", "గవారం", "చెరకు", "b", "AP 1వ స్థానం: మిరపకాయ, కోకో, ఆయిల్ పాం, పప్పాయి, టమాట, నిమ్మ."),
    (2, 1, "AP కోకో ఉత్పత్తి దేశ శాతం (మార్చి 2026)?", "25%", "35%", "41%", "55%", "c", "AP కోకో ఉత్పత్తి 47,060 హెక్టార్లు — దేశ మొత్తంలో 41%."),
    (2, 1, "AP మామిడి ఉత్పత్తిలో దేశంలో ఏ స్థానం?", "1వ", "2వ", "3వ", "4వ", "b", "AP 2వ స్థానం."),
    (2, 2, "AP జీడిపప్పు ఉత్పత్తిలో స్థానం?", "1వ", "2వ", "3వ", "4వ", "b", "AP 2వ స్థానం."),
    (2, 1, "AP కొబ్బరి ఉత్పత్తిలో స్థానం?", "1వ", "2వ", "3వ", "4వ", "c", "AP 4వ స్థానం."),
    (2, 1, "AP రొయ్యల ఉత్పత్తిలో దేశ సహకారం?", "50%", "60%", "70%", "80%", "c", "AP దేశ మొత్తం 70%."),
    (2, 2, "AP చేప & రొయ్యల ఉత్పత్తి (2024-25)?", "2.5 MT", "3.2 MT", "4.13 MT", "5.1 MT", "c", "4.13 MT."),
    (2, 2, "AP సముద్ర ఉత్పత్తుల ఎగుమతులు (FY25)?", "₹15,000 కోట్లు", "₹20,000 కోట్లు", "₹28,466 కోట్లు", "₹35,000 కోట్లు", "c", "₹28,466 కోట్లు ($3.21 bn)."),
    (2, 2, "AP merchandise exports (FY25)?", "₹1,00,000 కోట్లు", "₹1,50,000 కోట్లు", "₹1,84,277 కోట్లు", "₹2,00,000 కోట్లు", "c", "₹1,84,277 కోట్లు ($20.78 bn)."),
    (2, 1, "Barites ఉత్పత్తిలో AP దేశంలో ఏ స్థానం?", "1వ", "2వ", "3వ", "4వ", "a", "AP 1వ స్థానం (కడప జిల్లా)."),

    # Section 3: CII Partnership Summit 2025 (10 MCQs)
    (3, 1, "CII-AP భాగస్వామ్య సదస్సు ఎన్నవ సంచయం?", "25వ", "28వ", "30వ", "32వ", "c", "30వ సదస్సు — నవంబర్ 14-15, 2025."),
    (3, 1, "CII సదస్సు నగరం?", "విజయవాడ", "విశాఖపట్నం", "తిరుపతి", "హైదరాబాద్", "b", "విశాఖపట్నంలో."),
    (3, 1, "CII సదస్సుకు ఆకర్షిత మొత్తం పెట్టుబడులు?", "₹8 లక్షల కోట్లు", "₹10.5 లక్షల కోట్లు", "₹13.26 లక్షల కోట్లు", "₹15 లక్షల కోట్లు", "c", "₹13.26 లక్షల కోట్లు."),
    (3, 1, "CII సదస్సుకు సంబంధం ఉన్న MoU లు?", "450", "530", "613", "750", "c", "613 MoU."),
    (3, 2, "CII సదస్సు ఆధారంగా సృష్టించిన ఉద్యోగ అవకాశాలు?", "8 లక్షల", "12 లక్షల", "16.31 లక్షల", "20 లక్షల", "c", "16.31 లక్షల."),
    (3, 2, "ReNew Power MoU పెట్టుబడి?", "₹50,000 కోట్లు", "₹70,000 కోట్లు", "₹82,000 కోట్లు", "₹1 లక్ష కోట్లు", "c", "₹82,000 కోట్లు."),
    (3, 1, "CII సదస్సులో పాల్గొన్న దేశాలు?", "30", "38", "45", "55", "c", "45 దేశాలు."),
    (3, 2, "CII సదస్సులో పాల్గొన్న రంగాలు?", "8", "10", "12", "14", "c", "12 రంగాలు."),
    (3, 2, "CII సదస్సు నిర్ణీత కాలం?", "నవం 10-12", "నవం 14-15", "డిసం 1-2", "జనం 5-6", "b", "నవంబర్ 14-15, 2025."),
    (3, 1, "సదస్సుకు ప్రతిభాశాలిన ఆర్థిక సంస్థలు?", "ఉన్నాయి", "లేవు", "పాక్షికం", "తెలియదు", "a", "అనేక దేశీయ-విదేశీ సంస్థలు."),

    # Section 4: Google AI Hub & Quantum Computing (10 MCQs)
    (4, 1, "Google-AP AI Hub ఒప్పందం ఏ తేదీన?", "సెప్టెంబర్ 2025", "అక్టోబర్ 14, 2025", "నవంబర్ 2025", "డిసెంబర్ 2025", "b", "అక్టోబర్ 14, 2025న దిల్లీ తాజ్ మాన్‌సింగ్ హోటల్."),
    (4, 1, "Google పెట్టుబడి?", "$8 బిలియన్", "$10 బిలియన్", "$15 బిలియన్", "$20 బిలియన్", "c", "$15 బిలియన్ (5 సంవత్సరాలు)."),
    (4, 2, "Google AI Hub ప్రత్యేకత?", "ఆసియా అతిపెద్ద", "అమెరికా నుండి బయట అతిపెద్ద", "అమెరికా తర్వాత ప్రపంచంలో", "యూరప్ కంటే పెద్ద", "c", "అమెరికా తర్వాత ప్రపంచంలో అతిపెద్ద AI Hub."),
    (4, 1, "Google AI Hub నగరం?", "హైదరాబాద్", "విశాఖపట్నం", "అమరావతి", "విజయవాడ", "b", "విశాఖపట్నం."),
    (4, 1, "IBM Quantum Computer Qubit సంఖ్య?", "100", "133", "150", "175", "b", "133-Qubit, 5K gates."),
    (4, 1, "IBM Quantum Computer నగరం?", "విశాఖపట్నం", "విజయవాడ", "అమరావతి", "తిరుపతి", "c", "అమరావతి AQCC."),
    (4, 1, "దేశంలోనే తొలి Quantum Hardware Test Beds ఎప్పుడు?", "జూన్ 14, 2025", "సెప్టెంబర్ 14, 2025", "ఏప్రిల్ 14, 2026", "జూలై 14, 2026", "c", "ఏప్రిల్ 14, 2026 (World Quantum Day)."),
    (4, 1, "Quantum Test Beds నగరాలు?", "అమరావతి", "విజయవాడ", "SRM (అమరావతి) & Medha (విజయవాడ)", "తిరుపతి", "c", "SRM విశ్వవిద్యాలయం (అమరావతి) & Medha Towers (విజయవాడ)."),
    (4, 2, "IBM అద్దె ధర?", "₹15/చ.అ.", "₹20/చ.అ.", "₹30/చ.అ.", "₹50/చ.అ.", "c", "₹30/చ.అ. (2,000 చ.అ.)."),
    (4, 1, "BQRF సంక్షిప్త రూపం?", "Bharat Quantum", "Reference Facilities", "Bharat Quantum Reference Facilities", "Broad Quantum", "c", "Bharat Quantum Reference Facilities."),

    # Section 5: ArcelorMittal Steel & Mineral Resources (10 MCQs)
    (5, 1, "AMNS steel కర్మాగారం నగరం?", "విశాఖపట్నం", "నక్కపల్లి", "కర్నూలు", "చిత్తూరు", "b", "నక్కపల్లి, అనకాపల్లి జిల్లా."),
    (5, 1, "AMNS శంకుస్థాపన ఎప్పుడు?", "జనవరి 2026", "ఫిబ్రవరి 2026", "మార్చి 23, 2026", "ఏప్రిల్ 2026", "c", "మార్చి 23, 2026న CM చంద్రబాబు నిర్వహించారు."),
    (5, 1, "AMNS పెట్టుబడి?", "₹80,000 కోట్లు", "₹1.2 లక్ష కోట్లు", "₹1.5 లక్ష కోట్లు", "₹1.8 లక్ష కోట్లు", "c", "₹1.5 లక్ష కోట్లు."),
    (5, 1, "AMNS ఉత్పాదన సామర్థ్యం?", "10 MT", "15 MT", "24 MT", "30 MT", "c", "24 MT (రెండు దశలు)."),
    (5, 2, "RINL కంపెనీ స్థితి?", "SAIL సహాయక సంస్థ", "స్వతంత్ర CPSE", "నిజామ్ సంస్థ", "AP రాష్ట్ర సంస్థ", "b", "స్వతంత్ర CPSE — SAIL కి అనుబంధం కాదు."),
    (5, 1, "AP భారీ ఖనిజాలు (మార్చి 2026)?", "200 MT", "300 MT", "359.79 MT", "450 MT", "c", "359.79 MT, 25 deposits."),
    (5, 1, "Ilmenite సంచయాలు?", "100 MT", "150 MT", "178.75 MT", "220 MT", "c", "178.75 MT."),
    (5, 1, "Sillimanite సంచయాలు?", "50 MT", "70 MT", "81.85 MT", "100 MT", "c", "81.85 MT."),
    (5, 1, "Garnet సంచయాలు?", "45 MT", "60 MT", "67.30 MT", "75 MT", "c", "67.30 MT."),
    (5, 2, "Barites ఉత్పత్తిలో AP స్థానం?", "1వ", "2వ", "3వ", "4వ", "a", "AP 1వ స్థానం (కడప జిల్లా)."),

    # Section 6: Infrastructure — Ports & Airports (10 MCQs)
    (6, 1, "AP ప్రధాన పోర్టు?", "కృష్ణపట్నం", "విశాఖపట్నం", "కాకినాడ", "గంగవరం", "b", "విశాఖపట్నం — Eastern Coast అతిపెద్ద."),
    (6, 1, "AP నాన్-మేజర్ పోర్టుల సంఖ్య?", "3", "4", "5", "6", "c", "5 (కృష్ణపట్నం, గంగవరం, కాకినాడ, రావా, భావనపాడు)."),
    (6, 2, "AP Ports దేశంలో Cargo rank?", "1వ", "2వ", "3వ", "4వ", "c", "3వ highest cargo."),
    (6, 1, "AP అంతర్జాతీయ విమానాశ్రయాలు సంఖ్య?", "2", "3", "4", "5", "b", "3 (విశాఖపట్నం, తిరుపతి, విజయవాడ)."),
    (6, 1, "భోగాపురం విమానాశ్రయం నిర్మాత?", "Airports Authority", "GMR Group", "Adani Enterprises", "Reliance Infrastructure", "b", "GMR Group."),
    (6, 2, "AP దేశీయ విమానాశ్రయాలు?", "2", "3", "4", "5", "a", "2 (రాజమహేంద్రవరం, దొనకొండ)."),
    (6, 1, "విశాఖపట్నం పోర్టు స్థితి?", "Major పోర్టు", "Non-major", "మీడియం", "చిన్న", "a", "Major పోర్టు."),
    (6, 2, "మచిలీపట్నం పోర్టు?", "Major", "Non-major", "గ్రీన్‌ఫీల్డ్", "చిన్న", "c", "గ్రీన్‌ఫీల్డ్ పోర్టు."),
    (6, 1, "గ్రీన్‌ఫీల్డ్ పోర్టుల సంఖ్య (నిర్మాణంలో)?", "2", "3", "4", "5", "c", "4 (భావనపాడు, రామాయపట్నం, మచిలీపట్నం, కాకినాడ SEZ)."),
    (6, 2, "AP పోర్టుల స్థానాల్లో rank?", "1వ", "2వ", "3వ", "4వ", "c", "3వ (కార్గోలో)."),
]

def _seed_ap_ca_div6_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA chapter 6 (AP Economy Industries Infrastructure)."""
    ph = '%s' if USE_POSTGRES else '?'
    try:
        conn.execute("""CREATE TABLE IF NOT EXISTS study_notes (
            id INTEGER PRIMARY KEY,
            subject TEXT, topic TEXT, subtopic TEXT,
            chapter_num INTEGER, chapter_title_te TEXT,
            chapter_title_en TEXT, pages_ref TEXT, sections_json TEXT
        )""")
        if USE_POSTGRES: conn.commit()
    except Exception: pass

    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if row and not force: return {'success': True, 'already_exists': True}
    if row and force:
        db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id IN (SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph})", (6, 'AP_Current_Affairs'))
        db_exec(conn, f"DELETE FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
    if USE_POSTGRES: conn.commit()

    db_exec(conn, f"INSERT INTO study_notes (subject, topic, subtopic, chapter_num, chapter_title_te, chapter_title_en, pages_ref, sections_json) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})",
        ('GK', 'AP_Current_Affairs', 'Division6', 6, 'AP ఆర్థిక వ్యవస్థ & మౌలిక సదుపాయాలు', 'AP Economy Industries & Infrastructure', '', SECTIONS_JSON))
    conn.commit()
    return {'success': True, 'message': 'AP CA Div6 notes seeded!'}

def _seed_ap_ca_div6_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES):
    """Seed MCQs for AP CA chapter 6 (AP Economy Industries Infrastructure)."""
    ph = '%s' if USE_POSTGRES else '?'
    cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
    row = cur.fetchone()
    if not row:
        _seed_ap_ca_div6_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False)
        cur = db_exec(conn, f"SELECT id FROM study_notes WHERE chapter_num={ph} AND topic={ph}", (6, 'AP_Current_Affairs'))
        row = cur.fetchone()
    note_id = row_to_dict(row)['id'] if callable(row_to_dict) else row[0]
    db_exec(conn, f"DELETE FROM chapter_mcqs WHERE study_note_id={ph}", (note_id,))

    insert_sql = f"INSERT INTO chapter_mcqs (study_note_id, section_idx, difficulty, q_te, opt_a, opt_b, opt_c, opt_d, correct, explanation_te) VALUES ({ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph},{ph})"
    for (sec_idx, diff, q_te, a, b, c, d, correct, expl) in MCQ_DATA:
        db_exec(conn, insert_sql, (note_id, sec_idx, diff, q_te, a, b, c, d, correct.lower(), expl))
    if USE_POSTGRES: conn.commit()
    return {'success': True, 'inserted': len(MCQ_DATA)}
