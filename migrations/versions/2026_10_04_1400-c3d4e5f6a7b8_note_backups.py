"""note_backups: undo copies taken before an import replaces or removes notes

Revision ID: c3d4e5f6a7b8
Revises: b2c3d4e5f6a7
Create Date: 2026-10-04 14:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "c3d4e5f6a7b8"
down_revision = "b2c3d4e5f6a7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    insp = sa.inspect(op.get_bind())
    if not insp.has_table("note_backups"):
        op.create_table(
            "note_backups",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("batch_id", sa.String(length=32), nullable=False),
            sa.Column("reason", sa.String(length=16), nullable=False),
            sa.Column("chapter_id", sa.Integer(), nullable=False),
            sa.Column("section_num", sa.Integer(), nullable=False),
            sa.Column("heading_en", sa.String(length=256), nullable=True),
            sa.Column("heading_te", sa.String(length=256), nullable=True),
            sa.Column("body_en", sa.Text(), nullable=True),
            sa.Column("body_te", sa.Text(), nullable=True),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint("id"),
        )
    if not any(ix["name"] == "ix_note_backups_batch_id" for ix in sa.inspect(op.get_bind()).get_indexes("note_backups")):
        op.create_index("ix_note_backups_batch_id", "note_backups", ["batch_id"], unique=False)


def downgrade() -> None:
    # Backups are the only copy of replaced notes: never drop them while they hold rows.
    bind = op.get_bind()
    if sa.inspect(bind).has_table("note_backups"):
        if bind.execute(sa.text("SELECT COUNT(*) FROM note_backups")).scalar():
            raise RuntimeError("Refusing to drop note_backups: it contains saved copies of replaced notes. Nothing was changed.")
        op.drop_index("ix_note_backups_batch_id", table_name="note_backups")
        op.drop_table("note_backups")
