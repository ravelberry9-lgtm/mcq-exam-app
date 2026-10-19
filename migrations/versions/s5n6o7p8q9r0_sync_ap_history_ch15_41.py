"""Synchronise the AP History 15-41 location metadata.

Revision ID: s5n6o7p8q9r0
Revises: r4m5n6o7p8q9
"""
from alembic import op
import sqlalchemy as sa


revision = "s5n6o7p8q9r0"
down_revision = "r4m5n6o7p8q9"
branch_labels = None
depends_on = None


UNITS = {
    3: ("u3-colonial-nationalist-andhra", "Colonial and Nationalist Andhra", "వలస పాలన మరియు జాతీయోద్యమ ఆంధ్ర"),
    4: ("u4-andhra-movement-andhra-state", "Andhra Movement and Andhra State", "ఆంధ్రోద్యమం మరియు ఆంధ్ర రాష్ట్రం"),
    5: ("u5-formation-development-andhra-pradesh", "Formation and Development of Andhra Pradesh", "ఆంధ్రప్రదేశ్ ఆవిర్భావం మరియు అభివృద్ధి"),
}

OLD_UNITS = {
    3: ("ancient", "Ancient", "Ancient"),
    4: ("medieval", "Medieval", "Medieval"),
    5: ("modern", "Modern", "Modern"),
}

CHAPTER_UNITS = {
    **{number: 3 for number in range(15, 23)},
    **{number: 4 for number in range(23, 28)},
    **{number: 5 for number in range(28, 42)},
}


def _tables(bind):
    meta = sa.MetaData()
    return (
        sa.Table("subjects", meta, autoload_with=bind),
        sa.Table("syllabus_units", meta, autoload_with=bind),
        sa.Table("syllabus_chapters", meta, autoload_with=bind),
        sa.Table("questions", meta, autoload_with=bind),
    )


def upgrade():
    bind = op.get_bind()
    subjects, units, chapters, questions = _tables(bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    unit_ids = {}
    for number, (slug, title_en, title_te) in UNITS.items():
        unit_id = bind.execute(sa.select(units.c.id).where(units.c.subject_id == subject_id, units.c.unit_num == number)).scalar_one()
        bind.execute(units.update().where(units.c.id == unit_id).values(slug=slug, title_en=title_en, title_te=title_te, sort_order=number))
        unit_ids[number] = unit_id

    found = dict(bind.execute(sa.select(chapters.c.chapter_num, chapters.c.id).where(
        chapters.c.subject_id == subject_id,
        chapters.c.chapter_num.between(15, 41),
    )).all())
    missing = sorted(set(CHAPTER_UNITS) - set(found))
    if missing:
        raise RuntimeError(f"Cannot synchronise AP History; missing canonical chapters: {missing}")

    for chapter_num, unit_num in CHAPTER_UNITS.items():
        bind.execute(chapters.update().where(chapters.c.id == found[chapter_num]).values(
            unit_id=unit_ids[unit_num], sort_order=chapter_num
        ))

    bad_targets = bind.execute(sa.select(sa.func.count()).select_from(questions).join(
        chapters, questions.c.syllabus_chapter_id == chapters.c.id
    ).where(
        questions.c.subject_id == subject_id,
        chapters.c.chapter_num.between(15, 41),
        questions.c.note_target_slug.is_not(None),
        questions.c.note_target_slug != chapters.c.slug + "-main",
    )).scalar_one()
    if bad_targets:
        raise RuntimeError(f"AP History contains {bad_targets} out-of-sync question note targets")


def downgrade():
    bind = op.get_bind()
    subjects, units, _chapters, _questions = _tables(bind)
    subject_id = bind.execute(sa.select(subjects.c.id).where(subjects.c.slug == "ap_history")).scalar_one()
    for number, (slug, title_en, title_te) in OLD_UNITS.items():
        bind.execute(units.update().where(
            units.c.subject_id == subject_id, units.c.unit_num == number
        ).values(slug=slug, title_en=title_en, title_te=title_te, sort_order=number))
