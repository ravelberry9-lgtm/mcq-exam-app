"""Link AP History Chapters 15-41 to the verified RR source library.

Revision ID: t6o7p8q9r0s1
Revises: s5n6o7p8q9r0
"""
from alembic import op
import sqlalchemy as sa


revision = "t6o7p8q9r0s1"
down_revision = "s5n6o7p8q9r0"
branch_labels = None
depends_on = None

BASE = "/static/notes/AP_History/source_facsimiles/RR_Telugu"
MARKER = '<section class="rr-source-library" data-app-chapter="{chapter}">'
CHAPTERS = {
    15: ("ch02_03", 31, 47, "యూరోపియన్ వర్తక సంస్థలు"),
    16: ("ch02_03", 48, 68, "నిజాం ప్రభుత్వం, ఈస్ట్ ఇండియా కంపెనీ"),
    17: ("ch04_05", 69, 90, "కంపెనీ పాలనలో ఆంధ్రదేశం"),
    18: ("ch04_05", 91, 105, "బ్రిటిషు పాలనలో ఆంధ్రదేశం"),
    19: ("ch06", 106, 117, "హైదరాబాద్ రాష్ట్రం, 1857–1911"),
    20: ("ch07_08", 118, 133, "ఆంధ్రదేశంలో ప్రజాచైతన్యం"),
    21: ("ch07_08", 134, 156, "ఆంధ్రోద్యమ ఆవిర్భావం"),
    22: ("ch09_10", 157, 182, "ఆంధ్రలో భారత జాతీయోద్యమం"),
    23: ("ch09_10", 183, 195, "మద్రాసు రాజకీయాల్లో ఆంధ్రులు"),
    24: ("ch11_13", 196, 201, "తెలంగాణలో రాజకీయ చైతన్యం"),
    25: ("ch11_13", 202, 215, "తెలంగాణలో స్వాతంత్ర్యోద్యమం"),
    26: ("ch11_13", 216, 224, "హైదరాబాద్‌పై పోలీసు చర్య"),
    27: ("ch14_15", 225, 242, "ఆంధ్ర రాష్ట్ర అవతరణ"),
    28: ("ch14_15", 243, 257, "ఆంధ్రప్రదేశ్ అవతరణ"),
    29: ("ch16_17", 258, 279, "కమ్యూనిస్టు పార్టీలు, సాయుధ పోరాటాలు"),
    30: ("ch16_17", 280, 291, "1956 తరువాత రాజకీయ సంక్షోభాలు"),
    31: ("ch18_23", 292, 300, "ఎన్టీఆర్ ప్రభుత్వం తొలగింపు"),
    32: ("ch18_23", 301, 305, "ఎన్టీఆర్ మూడవ మంత్రివర్గం"),
    33: ("ch18_23", 306, 309, "పి.వి. నరసింహారావు"),
    34: ("ch18_23", 310, 315, "తెలుగుదేశం పార్టీలో చీలిక"),
    35: ("ch18_23", 316, 318, "చంద్రబాబు నాయుడు ప్రభుత్వం"),
    36: ("ch18_23", 319, 329, "పరిపాలనా సంస్కరణలు"),
    37: ("ch24_25", 330, 338, "కాంగ్రెస్ పునరుజ్జీవనం"),
    38: ("ch24_25", 339, 351, "2009 సాధారణ ఎన్నికలు"),
    39: (None, None, None, "2009 తరువాతి విభజన"),
    40: ("appendix_1", 353, 399, "తెలుగు సాహిత్య చారిత్రక సర్వేక్షణ"),
    41: ("appendix_2", 400, 403, "ప్రముఖ ఆంధ్ర వ్యక్తులు"),
}


def _addition(chapter, volume, first, last, title):
    marker = MARKER.format(chapter=chapter)
    if volume is None:
        return marker + f'''\n<h2>రఘునాథరావు మూలపుటల పరిశీలన</h2>
<p><strong>{title}:</strong> ఈ అంశానికి రఘునాథరావు గ్రంథంలో ఆధార అధ్యాయం లేదు. అందువల్ల RR పేరుతో passage, scan లేదా పుట సంఖ్యను కల్పించలేదు. ఈ అధ్యాయంలోని ఇప్పటికే ఉన్న అధికారిక/ప్రాథమిక మూలాల నోట్స్ యథాతథంగా కొనసాగుతాయి.</p>
</section>'''
    href = f"{BASE}/{volume}/source_pages.html#page-{first:03d}"
    return marker + f'''\n<h2>రఘునాథరావు — పూర్తి మూలపుటలు</h2>
<p><strong>{title}</strong> అంశానికి సంబంధించిన RR ముద్రిత పుటలు <strong>{first}–{last}</strong>. ప్రతి పుటను విడిగా scan రూపంలోనూ, అదే పుటతో మాన్యువల్‌గా ధృవీకరించిన తెలుగు పాఠ్య రూపంలోనూ చూడవచ్చు.</p>
<p><a href="{href}">ముద్రిత పుటలు {first}–{last} / ధృవీకరించిన పాఠ్యం తెరవండి</a></p>
<blockquote><strong>మూల పరిరక్షణ:</strong> ఈ source panel మాత్రమే అదనంగా జతైంది. పై existing RR/HR/APSCHE/CL నోట్స్ లేదా ప్రశ్నలు మార్చబడలేదు.</blockquote>
</section>'''


def _tables(bind):
    meta = sa.MetaData()
    return (
        sa.Table("subjects", meta, autoload_with=bind),
        sa.Table("chapters", meta, autoload_with=bind),
        sa.Table("notes", meta, autoload_with=bind),
    )


def upgrade():
    bind = op.get_bind()
    subjects, chapters, notes = _tables(bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    found = dict(bind.execute(sa.select(chapters.c.chapter_num, chapters.c.id).where(
        chapters.c.subject_id == subject_id,
        chapters.c.chapter_num.between(15, 41),
    )).all())
    missing = sorted(set(CHAPTERS) - set(found))
    if missing:
        raise RuntimeError(f"Cannot attach RR source library; missing chapters: {missing}")

    for chapter, data in CHAPTERS.items():
        note = bind.execute(sa.select(notes).where(
            notes.c.chapter_id == found[chapter]
        ).order_by(notes.c.section_num)).mappings().first()
        if note is None:
            raise RuntimeError(f"Cannot attach RR source library; Chapter {chapter} has no note")
        body = note["body_te"] or ""
        marker = MARKER.format(chapter=chapter)
        if marker in body:
            raise RuntimeError(f"Chapter {chapter} already has an RR source-library marker")
        addition = _addition(chapter, *data)
        updated = body + "\n\n" + addition
        if not updated.startswith(body):
            raise RuntimeError(f"Source-preservation guard failed for Chapter {chapter}")
        bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=updated))


def downgrade():
    bind = op.get_bind()
    subjects, chapters, notes = _tables(bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    found = dict(bind.execute(sa.select(chapters.c.chapter_num, chapters.c.id).where(
        chapters.c.subject_id == subject_id,
        chapters.c.chapter_num.between(15, 41),
    )).all())
    for chapter in CHAPTERS:
        note = bind.execute(sa.select(notes).where(
            notes.c.chapter_id == found[chapter]
        ).order_by(notes.c.section_num)).mappings().first()
        body = note["body_te"] or ""
        token = "\n\n" + MARKER.format(chapter=chapter)
        at = body.find(token)
        if at < 0:
            raise RuntimeError(f"Cannot safely remove RR source-library panel from Chapter {chapter}")
        bind.execute(notes.update().where(notes.c.id == note["id"]).values(body_te=body[:at]))
