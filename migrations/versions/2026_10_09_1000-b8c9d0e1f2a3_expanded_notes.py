"""expanded notes collection + explicit app-section map (additive only)

Creates ``expanded_notes`` (package core/addendum notes, separate from the legacy ``notes`` table) and
``expanded_note_app_map`` (reviewable mapping to existing app note sections). Nothing existing is changed, moved or deleted.

Revision ID: b8c9d0e1f2a3
Revises: a7b8c9d0e1f2
Create Date: 2026-10-09 10:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "b8c9d0e1f2a3"
down_revision = "a7b8c9d0e1f2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    insp = sa.inspect(op.get_bind())
    if not insp.has_table("expanded_notes"):
        op.create_table(
            "expanded_notes",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("subject_id", sa.Integer(), nullable=False),
            sa.Column("syllabus_chapter_id", sa.Integer(), nullable=False),
            sa.Column("anchor_id", sa.String(32), nullable=False),
            sa.Column("kind", sa.String(20), nullable=False),
            sa.Column("package_section", sa.Integer(), nullable=True),
            sa.Column("sort_order", sa.Integer(), nullable=True),
            sa.Column("heading_en", sa.String(300), nullable=False),
            sa.Column("heading_te", sa.String(300), nullable=True),
            sa.Column("body_en", sa.Text(), nullable=True),
            sa.Column("body_te", sa.Text(), nullable=True),
            sa.Column("sources", sa.JSON(), nullable=True),
            sa.Column("core_connections", sa.JSON(), nullable=True),
            sa.Column("package_batch_id", sa.String(64), nullable=True),
            sa.Column("content_hash", sa.String(32), nullable=True),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"], ondelete="CASCADE"),
            sa.ForeignKeyConstraint(["syllabus_chapter_id"], ["syllabus_chapters.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("subject_id", "anchor_id", name="uq_expanded_notes_anchor"),
            sa.CheckConstraint("kind IN ('core','addendum','addendum_group1','group1','revision')", name="ck_expanded_notes_kind"),
        )
        op.create_index("ix_expanded_notes_subject_id", "expanded_notes", ["subject_id"])
        op.create_index("ix_expanded_notes_syllabus_chapter_id", "expanded_notes", ["syllabus_chapter_id"])
    if not insp.has_table("expanded_note_app_map"):
        op.create_table(
            "expanded_note_app_map",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("expanded_note_id", sa.Integer(), nullable=False),
            sa.Column("source_chapter_num", sa.Integer(), nullable=False),
            sa.Column("app_section_num", sa.Integer(), nullable=False),
            sa.Column("relation", sa.String(12), nullable=False),
            sa.Column("status", sa.String(12), nullable=False),
            sa.Column("reason", sa.String(512), nullable=True),
            sa.ForeignKeyConstraint(["expanded_note_id"], ["expanded_notes.id"], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("expanded_note_id", "source_chapter_num", "app_section_num", name="uq_expanded_note_app_map"),
            sa.CheckConstraint("status IN ('draft','approved')", name="ck_expanded_note_app_map_status"),
        )
        op.create_index("ix_expanded_note_app_map_expanded_note_id", "expanded_note_app_map", ["expanded_note_id"])


def downgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)
    for t in ("expanded_note_app_map", "expanded_notes"):
        if insp.has_table(t) and bind.execute(sa.text(f"SELECT COUNT(*) FROM {t}")).scalar():
            raise RuntimeError(f"Refusing to downgrade: {t} holds rows. Export them first; nothing was changed.")
    if insp.has_table("expanded_note_app_map"):
        op.drop_index("ix_expanded_note_app_map_expanded_note_id", table_name="expanded_note_app_map")
        op.drop_table("expanded_note_app_map")
    if insp.has_table("expanded_notes"):
        op.drop_index("ix_expanded_notes_syllabus_chapter_id", table_name="expanded_notes")
        op.drop_index("ix_expanded_notes_subject_id", table_name="expanded_notes")
        op.drop_table("expanded_notes")
