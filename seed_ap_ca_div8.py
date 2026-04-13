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
]


def _seed_ap_ca_div8_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed study notes for AP CA chapter 8 (AP Environment, ISRO & Sports)."""
    existing = db_exec(
        conn,
        "SELECT id FROM study_notes WHERE topic=%s AND chapter_num=%s",
        ("AP_Current_Affairs", 8)
    )
    rows = [row_to_dict(r) for r in existing]
    if rows and not force:
        return

    html_path = os.path.join(
        os.path.dirname(__file__),
        "static", "notes", "ap_ca_div8_notes.html"
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
                "AP పర్యావరణం, ISRO & క్రీడలు",
                html_content,
                sections_data,
                "AP_Current_Affairs",
                8
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
                8,
                "AP పర్యావరణం, ISRO & క్రీడలు",
                html_content,
                sections_data
            )
        )


def _seed_ap_ca_div8_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES, force=False):
    """Seed MCQs for AP CA chapter 8 (AP Environment, ISRO & Sports)."""
    existing = db_exec(
        conn,
        "SELECT id FROM chapter_mcqs WHERE topic=%s AND chapter_num=%s",
        ("AP_Current_Affairs", 8)
    )
    rows = [row_to_dict(r) for r in existing]
    if rows and not force:
        return
    if rows and force:
        db_exec(
            conn,
            "DELETE FROM chapter_mcqs WHERE topic=%s AND chapter_num=%s",
            ("AP_Current_Affairs", 8)
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
                8,
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
