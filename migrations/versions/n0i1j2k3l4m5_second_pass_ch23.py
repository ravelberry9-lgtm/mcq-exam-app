"""Add the APSCHE structural-cause bridge to AP History Chapter 23.

Revision ID: n0i1j2k3l4m5
Revises: m9h0i1j2k3l4
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa


revision = "n0i1j2k3l4m5"
down_revision = "m9h0i1j2k3l4"
branch_labels = None
depends_on = None

BATCH = "ap-history-apsche-second-pass-ch23-20261019"
MARKER = '<section class="apsche-second-pass-ch23" data-source="APSCHE second slow pass">'
ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — ప్రత్యేక ఆంధ్ర కోరిక వెనుక దైనందిన అనుభవం</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> Chapter 23లోని RR/HR Justice Party–Andhra University–Rayalaseema–Sribagh కథనం యథాతథంగా ఉంది. ఈ భాగం ఆ రాజకీయ సంఘటనలకు ముందు ఉన్న సామాజిక–పరిపాలనా కారణాన్ని మాత్రమే జతచేస్తుంది. సంఖ్యలను APSCHE పాఠ్య గణాంకాలుగా చదవాలి.</blockquote>

<p>ప్రత్యేక ఆంధ్ర రాష్ట్ర కోరిక కేవలం “తెలుగు భాష మాట్లాడుతున్నాం” అనే భావోద్వేగం నుంచి పుట్టలేదు. మద్రాసు ప్రెసిడెన్సీలో జనాభా, విద్య, ఉద్యోగాలు, వృత్తి విద్య, పరిపాలనలో తమ వాటా మధ్య పెద్ద అంతరం ఉందని ఆంధ్రులు భావించారు. అదే అసంతృప్తి మొదట భాషా–సాంస్కృతిక చైతన్యంగా, తరువాత ప్రత్యేక విశ్వవిద్యాలయం మరియు ప్రత్యేక రాష్ట్ర డిమాండ్లుగా మారింది.</p>

<table><thead><tr><th>APSCHEలో కనిపించే పరిస్థితి</th><th>ఆంధ్ర నాయకులు దానికి ఇచ్చిన రాజకీయ అర్థం</th></tr></thead><tbody>
<tr><td>మద్రాసు రాష్ట్ర విస్తీర్ణంలో ఆంధ్ర ప్రాంతం సుమారు <strong>58%</strong>; జనాభాలో తెలుగువారు దాదాపు <strong>40%</strong></td><td>పెద్ద భౌగోళిక–జనాభా ఉనికి ఉన్నా తగిన గుర్తింపు లేదనే భావన</td></tr>
<tr><td>విద్య, ఉద్యోగాలు, వ్యాపారం, పారిశ్రామిక రంగాల్లో సమాన అవకాశాలు లేవనే అభిప్రాయం</td><td>భాషా సమస్యను ఆర్థిక–పరిపాలనా అవకాశాల సమస్యగా చూడటం</td></tr>
<tr><td>ఆంధ్ర ప్రాంత పాఠశాలలు, కళాశాలల్లో ఆంధ్రేతర అధికారులు పనిచేయడం</td><td>స్థానిక అవసరాలు, తెలుగు బోధనకు తగిన ప్రాధాన్యం దక్కడం లేదనే అసంతృప్తి</td></tr>
<tr><td>APSCHE ప్రకారం 1915 నాటికి మద్రాసు రాష్ట్రంలోని 31 కళాశాలల్లో ఆంధ్ర ప్రాంతంలో ఉన్నవి ఎనిమిది మాత్రమే</td><td>ప్రత్యేక ఆంధ్ర విశ్వవిద్యాలయం, మరిన్ని కళాశాలల డిమాండ్‌కు విద్యాపరమైన నేపథ్యం</td></tr>
<tr><td>ఆంధ్రలో ఇంజనీరింగ్, మెడికల్, లా కళాశాలలు లేవని పాఠ్యం పేర్కొంటుంది</td><td>ఉన్నత–వృత్తి విద్య కోసం ప్రాంతం బయట ఆధారపడాల్సిన పరిస్థితి</td></tr>
<tr><td>రైల్వే నియామకాలలో తమిళ ప్రాంతాలకు ప్రాధాన్యత ఎక్కువగా ఉందనే ఆరోపణ</td><td>ఉద్యోగ ప్రాతినిధ్యం కూడా ప్రత్యేక రాష్ట్ర వాదనలో భాగమైంది</td></tr>
</tbody></table>

<h3>కారణం నుంచి డిమాండ్ వరకు</h3>
<p><strong>అవకాశాల అసమానత భావన → భాషా–సాంస్కృతిక ఆత్మగౌరవం → సంఘాలు, పత్రికలు, సభలు → ప్రత్యేక ఆంధ్ర విశ్వవిద్యాలయం → ప్రత్యేక పరిపాలనా రాష్ట్రం</strong>. ఈ క్రమాన్ని గుర్తుంచుకుంటే Chapter 23లో Justice Party అంతర్గత విభేదాలు, విశ్వవిద్యాలయ కేంద్ర వివాదం, రాయలసీమ భయాలు, శ్రీబాగ్ రక్షణలు ఎందుకు వచ్చాయో అర్థమవుతుంది. అంటే విశ్వవిద్యాలయం ఒక విద్యాసంస్థ మాత్రమే కాదు; వనరులు, ప్రాతినిధ్యం, ప్రాంతీయ సమతుల్యతల రాజకీయ ప్రశ్నగా మారింది.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys = ("a", "b", "c", "d")
    shift = (int(qid.rsplit("-", 1)[1]) - 1) % 4
    if shift:
        options = options[-shift:] + options[:-shift]
    return {
        "qid": qid,
        "question": question,
        "options": dict(zip(keys, options)),
        "answer": keys[shift],
        "explanation": explanation,
        "difficulty": difficulty,
        "qtype": qtype,
    }


QUESTIONS = [
    _q("CH23-APSCHE2-001", "APSCHE ప్రకారం మద్రాసు రాష్ట్ర విస్తీర్ణంలో ఆంధ్ర ప్రాంతం వాటా సుమారు ఎంత?", ["58 శాతం", "40 శాతం", "31 శాతం", "8 శాతం"], "APSCHE పాఠ్య గణాంకం ప్రకారం విస్తీర్ణంలో ఆంధ్ర ప్రాంతం సుమారు 58 శాతం."),
    _q("CH23-APSCHE2-002", "APSCHE ప్రకారం మద్రాసు రాష్ట్ర జనాభాలో తెలుగువారి వాటా దాదాపు ఎంత?", ["40 శాతం", "58 శాతం", "31 శాతం", "8 శాతం"], "పాఠ్యం తెలుగువారి జనాభా వాటాను దాదాపు 40 శాతంగా పేర్కొంటుంది."),
    _q("CH23-APSCHE2-003", "1915 నాటికి మద్రాసు రాష్ట్రంలో ఉన్న 31 కళాశాలల్లో ఆంధ్ర ప్రాంతంలో ఉన్నవి ఎన్ని అని APSCHE పేర్కొంటుంది?", ["ఎనిమిది", "పదిహేను", "ఇరవై మూడు", "ముప్పై ఒకటి"], "APSCHE ప్రకారం 31 కళాశాలల్లో ఆంధ్ర ప్రాంతంలో ఎనిమిది మాత్రమే ఉండేవి."),
    _q("CH23-APSCHE2-004", "ప్రత్యేక ఆంధ్ర విశ్వవిద్యాలయ డిమాండ్‌కు ప్రత్యక్షంగా సంబంధించిన లోపం ఏది?", ["ఆంధ్రలో ఉన్నత, వృత్తి విద్యావకాశాల కొరత", "సముద్రతీరం లేకపోవడం", "తెలుగు పత్రికలు లేకపోవడం", "శాసనసభ ఎన్నికలు లేకపోవడం"], "కళాశాలల కొరత, ఇంజనీరింగ్–మెడికల్–లా విద్యాసంస్థలు లేకపోవడం ప్రత్యేక విశ్వవిద్యాలయ డిమాండ్‌కు విద్యాపరమైన నేపథ్యం."),
    _q("CH23-APSCHE2-005", "కింది జతలను పరిశీలించండి: 1. 58%—మద్రాసు రాష్ట్ర విస్తీర్ణంలో ఆంధ్ర ప్రాంతం; 2. 40%—మద్రాసు రాష్ట్ర జనాభాలో తెలుగువారు. సరైనది ఏది?", ["1, 2 రెండూ సరైనవి", "1 మాత్రమే సరైనది", "2 మాత్రమే సరైనది", "1, 2 రెండూ తప్పు"], "రెండు సంఖ్యలూ APSCHE పాఠ్యంలో ఇచ్చిన అంచనాలు; వాటిని పరస్పరం మార్చకూడదు.", "H", "statements"),
    _q("CH23-APSCHE2-006", "వాదన (A): ప్రత్యేక ఆంధ్ర ఉద్యమం కేవలం భాషా భావోద్వేగ ఉద్యమం కాదు. కారణం (R): విద్య, ఉద్యోగాలు, వ్యాపారం, పరిపాలనా ప్రాతినిధ్యంలో అసమానత ఉందనే భావన కూడా దానికి బలమిచ్చింది.", ["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ", "A, R రెండూ సరైనవి; R సరైన వివరణ కాదు", "A సరైనది; R తప్పు", "A తప్పు; R సరైనది"], "భాషా గుర్తింపుతో పాటు అవకాశాలు, వనరులు, ప్రాతినిధ్యం అనే భౌతిక సమస్యలు ఉద్యమానికి పునాది అయ్యాయి.", "H", "assertion_reason"),
    _q("CH23-APSCHE2-007", "ప్రత్యేక ఆంధ్ర డిమాండ్ ఎదుగుదలను సరైన కారణక్రమంలో చూపినది ఏది?", ["అవకాశాల అసమానత భావన → సాంస్కృతిక చైతన్యం → సంఘాలు/సభలు → విశ్వవిద్యాలయ డిమాండ్ → రాష్ట్ర డిమాండ్", "రాష్ట్ర డిమాండ్ → కళాశాలల మూసివేత → సాంస్కృతిక చైతన్యం → సంఘాలు", "విశ్వవిద్యాలయ స్థాపన → భాషా చైతన్యం → ఉద్యోగ అసమానత → పత్రికలు", "సంఘాలు → రాష్ట్ర ఏర్పాటు → విశ్వవిద్యాలయ డిమాండ్ → అసమానత భావన"], "APSCHE కథలో సామాజిక–ఆర్థిక అసంతృప్తి సాంస్కృతిక, సంస్థాగత, చివరకు రాజకీయ డిమాండ్‌గా ఎదిగింది.", "H", "sequence"),
    _q("CH23-APSCHE2-008", "ఆంధ్ర విశ్వవిద్యాలయ ప్రశ్న తరువాత ప్రాంతీయ రాజకీయ వివాదంగా మారడానికి ప్రధాన కారణం ఏమిటి?", ["విద్యాసంస్థల స్థానం వనరులు, ప్రాతినిధ్యం, ప్రాంతీయ సమతుల్యతతో ముడిపడటం", "విశ్వవిద్యాలయంలో తెలుగు బోధన పూర్తిగా నిషేధించడం", "మద్రాసు విశ్వవిద్యాలయాన్ని వెంటనే మూసివేయడం", "విశ్వవిద్యాలయాన్ని బ్రిటిష్ పార్లమెంట్ నేరుగా నడపడం"], "కేంద్రం, పరిధి, కళాశాలలు ప్రాంతాల మధ్య వనరుల పంపిణీని సూచించడంతో విద్యా ప్రశ్న రాజకీయ సమతుల్యత ప్రశ్నగా మారింది.", "H", "concept"),
]


def _vals(table, values):
    return {key: value for key, value in values.items() if key in table.c}


def upgrade():
    bind = op.get_bind()
    meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("chapters", meta, autoload_with=bind)
    canonical = sa.Table("syllabus_chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind)
    questions = sa.Table("questions", meta, autoload_with=bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 23)).scalar_one()
    syllabus_chapter_id = bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id == subject_id, canonical.c.chapter_num == 23)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    original = note["body_te"] or ""
    if MARKER in original:
        raise RuntimeError("Chapter 23 already has second-pass marker")
    prefix_hash = hashlib.sha256(original.encode()).hexdigest()
    updated = original + "\n\n" + ADDITION
    if not updated.startswith(original):
        raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))
    existing = bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id == subject_id, questions.c.batch_id == BATCH)).scalar_one()
    if existing:
        raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slug = bind.execute(sa.select(canonical.c.slug).where(canonical.c.id == syllabus_chapter_id)).scalar_one()
    now = datetime.utcnow()
    for question in QUESTIONS:
        trace = {
            "source_label": "APSCHE second slow pass",
            "source": "APSCHE History & Culture of Andhra (1512-1956)",
            "scope": "structural causes of separate Andhra demand; figures are source-labelled",
            "preservation": "appended_only_rr_hr_unchanged",
            "chapter_note_prefix_sha256": prefix_hash,
            "review_status": "manual_line_comparison",
        }
        values = {
            "subject_id": subject_id,
            "chapter_id": chapter_id,
            "source_type": "chapter",
            "question_en": "",
            "question_te": question["question"],
            "options_en": {key: "" for key in "abcd"},
            "options_te": question["options"],
            "correct_answer": question["answer"],
            "explanation_en": "",
            "explanation_te": question["explanation"] + "\n" + json.dumps(trace, ensure_ascii=False),
            "difficulty": question["difficulty"],
            "qtype": question["qtype"],
            "syllabus_chapter_id": syllabus_chapter_id,
            "source": "APSCHE",
            "source_file": "APSCHE Modern AP History Telugu PDF - second pass",
            "source_qid": question["qid"],
            "source_chapter": "23",
            "review_status": "author_reviewed",
            "batch_id": BATCH,
            "content_hash": hashlib.md5((question["qid"] + question["question"]).encode()).hexdigest(),
            "q_hash": hashlib.md5((question["question"] + json.dumps(question["options"], ensure_ascii=False, sort_keys=True)).encode()).hexdigest(),
            "note_target_slug": slug + "-main",
            "source_trace": trace,
            "created_at": now,
            "updated_at": now,
        }
        bind.execute(questions.insert().values(**_vals(questions, values)))


def downgrade():
    bind = op.get_bind()
    meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind)
    chapters = sa.Table("chapters", meta, autoload_with=bind)
    notes = sa.Table("notes", meta, autoload_with=bind)
    questions = sa.Table("questions", meta, autoload_with=bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    bind.execute(questions.delete().where(questions.c.subject_id == subject_id, questions.c.batch_id == BATCH))
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 23)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first()
    body = note["body_te"] or ""
    marker_at = body.find("\n\n" + MARKER)
    if marker_at < 0:
        raise RuntimeError("Cannot safely remove Chapter 23 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:marker_at]))
