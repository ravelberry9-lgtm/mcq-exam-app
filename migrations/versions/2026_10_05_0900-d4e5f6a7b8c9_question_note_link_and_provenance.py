"""questions: note-section link, note target slug, internal source trace, import reference

Additive and nullable: existing rows are untouched (all four columns stay NULL for them).

Revision ID: d4e5f6a7b8c9
Revises: c3d4e5f6a7b8
Create Date: 2026-10-05 09:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "d4e5f6a7b8c9"
down_revision = "c3d4e5f6a7b8"
branch_labels = None
depends_on = None

_COLUMNS = [
    ("note_section_num", sa.Integer()),
    ("note_target_slug", sa.String(length=96)),
    ("source_trace", sa.JSON()),
    ("import_ref", sa.String(length=64)),
]


def upgrade() -> None:
    insp = sa.inspect(op.get_bind())
    have = {c["name"] for c in insp.get_columns("questions")}
    for name, type_ in _COLUMNS:
        if name not in have:
            op.add_column("questions", sa.Column(name, type_, nullable=True))
    if not any(ix["name"] == "ix_questions_import_ref" for ix in sa.inspect(op.get_bind()).get_indexes("questions")):
        op.create_index("ix_questions_import_ref", "questions", ["import_ref"], unique=False)


def downgrade() -> None:
    # These columns hold content-team provenance and note links: never drop them while any row uses them.
    bind = op.get_bind()
    used = bind.execute(sa.text(
        "SELECT COUNT(*) FROM questions WHERE note_section_num IS NOT NULL OR note_target_slug IS NOT NULL "
        "OR source_trace IS NOT NULL OR import_ref IS NOT NULL")).scalar()
    if used:
        raise RuntimeError("Refusing to drop the question note-link/provenance columns: %d question(s) use them. "
                           "Nothing was changed." % used)
    op.drop_index("ix_questions_import_ref", table_name="questions")
    with op.batch_alter_table("questions") as batch:
        for name, _ in reversed(_COLUMNS):
            batch.drop_column(name)
