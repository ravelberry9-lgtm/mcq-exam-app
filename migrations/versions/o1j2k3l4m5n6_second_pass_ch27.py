"""Add a verified Potti Sriramulu pre-1952 biography to Chapter 27.

Revision ID: o1j2k3l4m5n6
Revises: n0i1j2k3l4m5
"""
from datetime import datetime
import hashlib
import json

from alembic import op
import sqlalchemy as sa


revision = "o1j2k3l4m5n6"
down_revision = "n0i1j2k3l4m5"
branch_labels = None
depends_on = None

BATCH = "ap-history-apsche-second-pass-ch27-20261019"
MARKER = '<section class="apsche-second-pass-ch27" data-source="APSCHE second slow pass and official verification">'
ADDITION = MARKER + r'''
<h2>APSCHE రెండో పరిశీలన — 1952కు ముందు పొట్టి శ్రీరాములు జీవితం</h2>
<blockquote><strong>మూల పరిరక్షణ:</strong> Chapter 27లోని RR/HR రాష్ట్రావతరణ కథ, తుది ఆమరణ దీక్ష, మరణం, ఆంధ్ర రాష్ట్ర ఏర్పాటు వివరాలు మార్చబడలేదు. ఇక్కడ APSCHEలో ఉన్న జీవితచరిత్రను అధికారిక భారత ప్రభుత్వ చరిత్రతో పోల్చి, ధృవీకరించగలిగిన పూర్వ జీవితాన్ని మాత్రమే జతచేస్తున్నాం.</blockquote>

<h3>ముందుగా ఒక ముద్రణ సమస్యను గుర్తించాలి</h3>
<p>ఈ APSCHE ప్రతిలో జనన సంవత్సరం <strong>1911</strong>గా ముద్రితమైంది. అయితే భారత ప్రభుత్వ సాంస్కృతిక మంత్రిత్వ శాఖ Digital District Repository పొట్టి శ్రీరాములు జనన సంవత్సరాన్ని <strong>1901</strong>గా ఇస్తుంది; ఆంధ్రప్రదేశ్ ప్రభుత్వ అధికారిక జయంతి పట్టిక మార్చి 16ను నిర్ధారిస్తుంది. అందువల్ల పరీక్షకు <strong>16 మార్చి 1901</strong>నే ఉపయోగించాలి. APSCHEలోని 1911ను source-print discrepancyగా మాత్రమే గుర్తుంచుకోవాలి.</p>

<h3>వ్యక్తిగత నష్టం నుంచి గాంధేయ సేవకు</h3>
<p>పొట్టి శ్రీరాములు మద్రాసులో ఆర్యవైశ్య కుటుంబంలో జన్మించారు. తండ్రి <strong>గురవయ్య</strong>, తల్లి <strong>మహాలక్ష్మమ్మ</strong>. చదువు పూర్తయ్యాక రైల్వే ఉద్యోగంలో చేరారు. భార్య, తల్లి మరణాల తరువాత ఆయన జీవన దిశ మారింది. ఉద్యోగానికి రాజీనామా చేసి <strong>సబర్మతి ఆశ్రమంలో</strong> చేరి గాంధీకి సన్నిహిత శిష్యుడయ్యారు. ఈ మలుపును అర్థం చేసుకుంటే 1952 దీక్ష అకస్మాత్తుగా తీసుకున్న నిర్ణయం కాదని తెలుస్తుంది—వ్యక్తిగత త్యాగాన్ని ప్రజాసేవగా మార్చుకున్న దీర్ఘ గాంధేయ జీవితం దానికి వెనుక ఉంది.</p>

<h3>జాతీయోద్యమం, ఆశ్రమాలు, నిర్మాణ కార్యక్రమం</h3>
<p>అధికారిక భారత ప్రభుత్వ చరిత్ర ఆయన <strong>1930 ఉప్పు సత్యాగ్రహం</strong>, <strong>1941–42 వ్యక్తిగత సత్యాగ్రహం</strong>, <strong>క్విట్ ఇండియా ఉద్యమం</strong>లో పాల్గొని జైలు శిక్షలు అనుభవించినట్లు నిర్ధారిస్తుంది. APSCHE జాబితాలో సహాయనిరాకరణ ఉద్యమం కూడా ఉంది; కానీ అది ధృవీకరించిన 1901 జనన సంవత్సరంతో సరిపడేలా స్వతంత్ర ఆధారం లేకపోవడంతో ఇక్కడ MCQగా ఉపయోగించడం లేదు.</p>
<p>APSCHE ప్రకారం ఆయన గాంధీ బంధువు నారాయణదాస్ ప్రారంభించిన <strong>ధార్వాడ్ గ్రామ సేవా సంఘం</strong>లో రెండున్నర సంవత్సరాలు సేవ చేశారు. తరువాత ఆంధ్రకు వచ్చి <strong>కొమరవోలు</strong>, <strong>అంగలూరు</strong> గాంధేయ ఆశ్రమాలతో పనిచేశారు. ఖద్దరు, మద్యపాన నిషేధం, హరిజనాభ్యుదయం, హిందూ–ముస్లిం ఐక్యత వంటి నిర్మాణ కార్యక్రమాలను ప్రజల్లోకి తీసుకెళ్లారు. కొమరవోలు ఆశ్రమ అనుబంధాన్ని అధికారిక భారత ప్రభుత్వ చరిత్ర కూడా నిర్ధారిస్తుంది.</p>

<h3>నెల్లూరు హరిజన సేవ — 1952 త్యాగానికి ముందు జరిగిన దీక్షలు</h3>
<table><thead><tr><th>కాలం</th><th>సేవ/దీక్ష</th><th>ఫలితం</th></tr></thead><tbody>
<tr><td>1944 నుంచి</td><td>నెల్లూరు కేంద్రంగా హరిజన అభ్యున్నతికి కృషి</td><td>సామాజిక సమానత్వాన్ని తన నిర్మాణ కార్యక్రమానికి కేంద్రం చేశారు</td></tr>
<tr><td>1946</td><td>23 రోజుల నిరాహార దీక్ష</td><td>నెల్లూరు మూలపేట శ్రీ వేణుగోపాలస్వామి దేవాలయంలో హరిజనుల ప్రవేశానికి మార్గం ఏర్పడింది</td></tr>
<tr><td>1948</td><td>29 రోజుల నిరాహార దీక్ష</td><td>ప్రతి నెల 30వ తేదీని హరిజన సంక్షేమ దినంగా పాటించాలని మద్రాసు ప్రభుత్వం ఉత్తర్వు జారీ చేసింది</td></tr>
</tbody></table>
<p>అందువల్ల పొట్టి శ్రీరాములును కేవలం ‘ఆంధ్ర రాష్ట్రం కోసం 1952లో ప్రాణత్యాగం చేసిన వ్యక్తి’గా చదవడం అసంపూర్ణం. ఆశ్రమ శిక్షణ, జాతీయోద్యమ జైలు జీవితం, గ్రామసేవ, అస్పృశ్యత నిర్మూలన కోసం పూర్వ దీక్షలు—ఇవన్నీ కలిసే ఆయన చివరి ఆమరణ దీక్షకు నైతిక బలం ఇచ్చాయి.</p>
</section>'''


def _q(qid, question, options, explanation, difficulty="M", qtype="direct"):
    keys = ("a", "b", "c", "d")
    shift = (int(qid.rsplit("-", 1)[1]) - 1) % 4
    if shift:
        options = options[-shift:] + options[:-shift]
    return {"qid": qid, "question": question, "options": dict(zip(keys, options)), "answer": keys[shift], "explanation": explanation, "difficulty": difficulty, "qtype": qtype}


QUESTIONS = [
    _q("CH27-APSCHE2-001", "అధికారికంగా ధృవీకరించిన పొట్టి శ్రీరాములు జనన తేదీ ఏది?", ["16 మార్చి 1901", "16 మార్చి 1911", "15 డిసెంబరు 1901", "19 అక్టోబర్ 1901"], "భారత ప్రభుత్వ Digital District Repository జనన సంవత్సరాన్ని 1901గా ఇస్తుంది; AP ప్రభుత్వ జయంతి పట్టిక మార్చి 16ను నిర్ధారిస్తుంది. APSCHE ప్రతిలోని 1911 ముద్రణ వ్యత్యాసం."),
    _q("CH27-APSCHE2-002", "పొట్టి శ్రీరాములు తల్లిదండ్రుల సరైన జత ఏది?", ["గురవయ్య–మహాలక్ష్మమ్మ", "నారాయణదాస్–మహాలక్ష్మమ్మ", "గురవయ్య–సుబ్బమ్మ", "సాంబమూర్తి–మహాలక్ష్మమ్మ"], "APSCHE జీవితచరిత్రలో తండ్రి గురవయ్య, తల్లి మహాలక్ష్మమ్మగా పేర్కొన్నారు."),
    _q("CH27-APSCHE2-003", "APSCHE ప్రకారం పొట్టి శ్రీరాములు ధార్వాడ్ గ్రామ సేవా సంఘంలో ఎంతకాలం సేవ చేశారు?", ["రెండున్నర సంవత్సరాలు", "ఆరు నెలలు", "ఒక సంవత్సరం", "ఐదు సంవత్సరాలు"], "నారాయణదాస్ ప్రారంభించిన ధార్వాడ్ గ్రామ సేవా సంఘంలో పొట్టి శ్రీరాములు రెండున్నర సంవత్సరాలు సేవ చేసినట్లు APSCHE పేర్కొంటుంది."),
    _q("CH27-APSCHE2-004", "పొట్టి శ్రీరాములు ఆంధ్రలో సేవ చేసిన గాంధేయ ఆశ్రమాల సరైన జత ఏది?", ["కొమరవోలు–అంగలూరు", "సబర్మతి–వర్ధా", "మూలపేట–పవనార్", "బాపట్ల–చీరాల"], "APSCHE ప్రకారం ఆయన కొమరవోలు, అంగలూరు గాంధేయ ఆశ్రమాలతో పనిచేశారు."),
    _q("CH27-APSCHE2-005", "పొట్టి శ్రీరాములు జాతీయోద్యమ పాత్రకు అధికారికంగా ధృవీకరించిన సరైన సమూహం ఏది?", ["ఉప్పు సత్యాగ్రహం–వ్యక్తిగత సత్యాగ్రహం–క్విట్ ఇండియా", "స్వదేశీ–హోమ్ రూల్–రౌలట్ సత్యాగ్రహం", "చీరాల పేరాల–పల్నాడు–పెదనందిపాడు", "సైమన్ బహిష్కరణ–బార్డోలీ–కేబినెట్ మిషన్"], "భారత ప్రభుత్వ చరిత్ర 1930 ఉప్పు సత్యాగ్రహం, 1941–42 వ్యక్తిగత సత్యాగ్రహం, క్విట్ ఇండియా పాల్గొనడాన్ని నిర్ధారిస్తుంది.", "H", "grouping"),
    _q("CH27-APSCHE2-006", "పొట్టి శ్రీరాములు 1944 నుంచి ఏ పట్టణాన్ని కేంద్రంగా చేసుకొని హరిజన అభ్యున్నతికి పనిచేశారు?", ["నెల్లూరు", "మద్రాసు", "విజయవాడ", "కర్నూలు"], "APSCHE ప్రకారం 1944 నుంచి నెల్లూరు కేంద్రంగా హరిజన అభ్యున్నతికి కృషి చేశారు."),
    _q("CH27-APSCHE2-007", "1946లో పొట్టి శ్రీరాములు 23 రోజుల దీక్షకు సంబంధించిన ఫలితం ఏది?", ["మూలపేట శ్రీ వేణుగోపాలస్వామి దేవాలయంలో హరిజన ప్రవేశం", "ఆంధ్ర రాష్ట్ర తక్షణ ఏర్పాటు", "మద్రాసును ప్రత్యేక రాష్ట్రంగా ప్రకటించడం", "ఆంధ్ర విశ్వవిద్యాలయాన్ని వాల్తేరుకు మార్చడం"], "నెల్లూరు మూలపేటలోని శ్రీ వేణుగోపాలస్వామి దేవాలయంలో హరిజనుల ప్రవేశం కోసం 23 రోజుల దీక్ష చేశారు."),
    _q("CH27-APSCHE2-008", "వాదన (A): పొట్టి శ్రీరాములు 1952 దీక్షకు ముందే నిరాహార దీక్షను సామాజిక సంస్కరణ సాధనంగా ఉపయోగించారు. కారణం (R): 1948లో ఆయన 29 రోజుల దీక్ష అనంతరం ప్రతి నెల 30వ తేదీని హరిజన సంక్షేమ దినంగా పాటించాలని మద్రాసు ప్రభుత్వం ఉత్తర్వు ఇచ్చింది.", ["A, R రెండూ సరైనవి; R, Aకు సరైన వివరణ", "A, R రెండూ సరైనవి; R సరైన వివరణ కాదు", "A సరైనది; R తప్పు", "A తప్పు; R సరైనది"], "1946 దేవాలయ ప్రవేశ దీక్ష, 1948 హరిజన సంక్షేమ దీక్ష—1952కు ముందే దీక్షను సామాజిక మార్పు సాధనంగా ఉపయోగించినట్లు చూపుతాయి.", "H", "assertion_reason"),
]


def _vals(table, values):
    return {key: value for key, value in values.items() if key in table.c}


def upgrade():
    bind = op.get_bind(); meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind); chapters = sa.Table("chapters", meta, autoload_with=bind)
    canonical = sa.Table("syllabus_chapters", meta, autoload_with=bind); notes = sa.Table("notes", meta, autoload_with=bind); questions = sa.Table("questions", meta, autoload_with=bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 27)).scalar_one()
    syllabus_chapter_id = bind.execute(sa.select(canonical.c.id).where(canonical.c.subject_id == subject_id, canonical.c.chapter_num == 27)).scalar_one()
    note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first(); original = note["body_te"] or ""
    if MARKER in original: raise RuntimeError("Chapter 27 already has second-pass marker")
    prefix_hash = hashlib.sha256(original.encode()).hexdigest(); updated = original + "\n\n" + ADDITION
    if not updated.startswith(original): raise RuntimeError("Source-preservation guard failed")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))
    existing = bind.execute(sa.select(sa.func.count()).select_from(questions).where(questions.c.subject_id == subject_id, questions.c.batch_id == BATCH)).scalar_one()
    if existing: raise RuntimeError(f"Unexpected existing batch rows: {existing}")
    slug = bind.execute(sa.select(canonical.c.slug).where(canonical.c.id == syllabus_chapter_id)).scalar_one(); now = datetime.utcnow()
    for question in QUESTIONS:
        trace = {"source_label": "APSCHE second slow pass with official verification", "source": "APSCHE History & Culture of Andhra (1512-1956); Ministry of Culture Digital District Repository", "scope": "Potti Sriramulu pre-1952 biography", "preservation": "appended_only_rr_hr_unchanged", "chapter_note_prefix_sha256": prefix_hash, "review_status": "manual_line_comparison_and_official_verification"}
        values = {"subject_id": subject_id, "chapter_id": chapter_id, "source_type": "chapter", "question_en": "", "question_te": question["question"], "options_en": {key: "" for key in "abcd"}, "options_te": question["options"], "correct_answer": question["answer"], "explanation_en": "", "explanation_te": question["explanation"] + "\n" + json.dumps(trace, ensure_ascii=False), "difficulty": question["difficulty"], "qtype": question["qtype"], "syllabus_chapter_id": syllabus_chapter_id, "source": "APSCHE+GOI", "source_file": "APSCHE Modern AP History Telugu PDF - second pass", "source_qid": question["qid"], "source_chapter": "27", "review_status": "author_reviewed", "batch_id": BATCH, "content_hash": hashlib.md5((question["qid"] + question["question"]).encode()).hexdigest(), "q_hash": hashlib.md5((question["question"] + json.dumps(question["options"], ensure_ascii=False, sort_keys=True)).encode()).hexdigest(), "note_target_slug": slug + "-main", "source_trace": trace, "created_at": now, "updated_at": now}
        bind.execute(questions.insert().values(**_vals(questions, values)))


def downgrade():
    bind = op.get_bind(); meta = sa.MetaData()
    subjects = sa.Table("subjects", meta, autoload_with=bind); chapters = sa.Table("chapters", meta, autoload_with=bind); notes = sa.Table("notes", meta, autoload_with=bind); questions = sa.Table("questions", meta, autoload_with=bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one(); bind.execute(questions.delete().where(questions.c.subject_id == subject_id, questions.c.batch_id == BATCH))
    chapter_id = bind.execute(sa.select(chapters.c.id).where(chapters.c.subject_id == subject_id, chapters.c.chapter_num == 27)).scalar_one(); note = bind.execute(sa.select(notes).where(notes.c.chapter_id == chapter_id).order_by(notes.c.section_num)).mappings().first(); body = note["body_te"] or ""; marker_at = body.find("\n\n" + MARKER)
    if marker_at < 0: raise RuntimeError("Cannot safely remove Chapter 27 second-pass enrichment")
    bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:marker_at]))
