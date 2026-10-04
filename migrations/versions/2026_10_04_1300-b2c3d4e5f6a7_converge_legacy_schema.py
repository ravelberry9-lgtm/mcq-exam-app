"""converge legacy schemas onto the model (adds questions.q_hash, fixes keys/indexes)

A database created before Alembic (the old app / ``content.db``) is *adopted* by the baseline and then
brought to exactly the schema the models declare, without losing a row:

* ``questions.q_hash`` (md5 content fingerprint) is kept: added if missing, now declared on the model.
* SQLite legacy tables that deviate structurally (nullable key, NOT NULL or type-family mismatch, missing or
  different foreign keys / ON DELETE) are rebuilt in place from the
  frozen definitions below: proper NOT NULL keys, ``ON DELETE CASCADE`` on chapters/notes, the missing
  ``questions.passage_id`` foreign key, declared column types. Rows are copied verbatim.
* Index names are normalised (legacy ``idx_q_*`` become the model's ``ix_questions_*``).

On a database that is already correct (fresh install, or one created by the baseline) every step is a no-op.

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-10-04 13:00:00+00:00
"""
from alembic import op
import sqlalchemy as sa

revision = "b2c3d4e5f6a7"
down_revision = "a1b2c3d4e5f6"
branch_labels = None
depends_on = None

# Frozen copies of the baseline definitions (never import the live models into a migration).
_md = sa.MetaData()
_subjects = sa.Table("subjects", _md,
    sa.Column("id", sa.Integer(), nullable=False), sa.Column("slug", sa.String(64), nullable=False),
    sa.Column("name_en", sa.String(128), nullable=False), sa.Column("name_te", sa.String(128), nullable=False),
    sa.Column("sort_order", sa.Integer()), sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("slug"))
_chapters = sa.Table("chapters", _md,
    sa.Column("id", sa.Integer(), nullable=False), sa.Column("subject_id", sa.Integer(), nullable=False),
    sa.Column("chapter_num", sa.Integer(), nullable=False), sa.Column("title_en", sa.String(256), nullable=False),
    sa.Column("title_te", sa.String(256), nullable=False), sa.Column("est_read_minutes", sa.Integer()),
    sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("subject_id", "chapter_num"))
_pages = sa.Table("pages", _md,
    sa.Column("id", sa.Integer(), nullable=False), sa.Column("slug", sa.String(128), nullable=False),
    sa.Column("title_en", sa.String(256), nullable=False), sa.Column("title_te", sa.String(256), nullable=False),
    sa.Column("body_en", sa.Text()), sa.Column("body_te", sa.Text()), sa.Column("page_type", sa.String(32)),
    sa.Column("visible", sa.Boolean()), sa.Column("created_at", sa.DateTime()), sa.Column("updated_at", sa.DateTime()),
    sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("slug"))
_notes = sa.Table("notes", _md,
    sa.Column("id", sa.Integer(), nullable=False), sa.Column("chapter_id", sa.Integer(), nullable=False),
    sa.Column("section_num", sa.Integer(), nullable=False), sa.Column("heading_en", sa.String(256)),
    sa.Column("heading_te", sa.String(256)), sa.Column("body_en", sa.Text()), sa.Column("body_te", sa.Text()),
    sa.ForeignKeyConstraint(["chapter_id"], ["chapters.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("chapter_id", "section_num"))
_passages = sa.Table("passages", _md,
    sa.Column("id", sa.Integer(), nullable=False), sa.Column("text_en", sa.Text()), sa.Column("text_te", sa.Text()),
    sa.PrimaryKeyConstraint("id"))
_questions = sa.Table("questions", _md,
    sa.Column("id", sa.Integer(), nullable=False), sa.Column("subject_id", sa.Integer(), nullable=False),
    sa.Column("chapter_id", sa.Integer()), sa.Column("source_type", sa.String(16), nullable=False),
    sa.Column("q_hash", sa.String(32)),
    sa.Column("pyq_year", sa.String(8)), sa.Column("pyq_paper", sa.String(64)), sa.Column("difficulty", sa.String(2)),
    sa.Column("question_en", sa.Text()), sa.Column("question_te", sa.Text()),
    sa.Column("options_en", sa.JSON()), sa.Column("options_te", sa.JSON()),
    sa.Column("correct_answer", sa.String(1), nullable=False),
    sa.Column("explanation_en", sa.Text()), sa.Column("explanation_te", sa.Text()),
    sa.Column("passage_id", sa.Integer()), sa.Column("created_at", sa.DateTime()), sa.Column("updated_at", sa.DateTime()),
    sa.ForeignKeyConstraint(["chapter_id"], ["chapters.id"]), sa.ForeignKeyConstraint(["passage_id"], ["passages.id"]),
    sa.ForeignKeyConstraint(["subject_id"], ["subjects.id"]), sa.PrimaryKeyConstraint("id"))
_exam_sessions = sa.Table("exam_sessions", _md,
    sa.Column("id", sa.String(64), nullable=False), sa.Column("device_id", sa.String(64), nullable=False),
    sa.Column("config", sa.JSON(), nullable=False), sa.Column("question_ids", sa.JSON(), nullable=False),
    sa.Column("answers", sa.JSON()), sa.Column("confidences", sa.JSON()),
    sa.Column("started_at", sa.DateTime()), sa.Column("submitted_at", sa.DateTime()),
    sa.Column("score", sa.Integer()), sa.Column("total", sa.Integer()), sa.PrimaryKeyConstraint("id"))

_REBUILD_ORDER = [_subjects, _chapters, _pages, _notes, _questions, _exam_sessions]

# (index name, table, columns) the models declare for these tables
_INDEXES = [
    ("ix_chapters_subject_id", "chapters", ["subject_id"]),
    ("ix_notes_chapter_id", "notes", ["chapter_id"]),
    ("ix_exam_sessions_device_id", "exam_sessions", ["device_id"]),
    ("ix_questions_chapter_id", "questions", ["chapter_id"]),
    ("ix_questions_source_type", "questions", ["source_type"]),
    ("ix_questions_subject_id", "questions", ["subject_id"]),
    ("ix_questions_q_hash", "questions", ["q_hash"]),
]
_LEGACY_INDEXES = [("idx_q_ch", "questions"), ("idx_q_subj", "questions"), ("idx_q_hash", "questions")]


def _affinity(type_):
    """SQLite stores values by affinity, so VARCHAR/TEXT/JSON/DateTime are one family and INTEGER/BOOLEAN another."""
    n = str(type_).upper()
    return "INT" if ("INT" in n or "BOOL" in n) else "TEXT"


def _fk_signature(fks):
    return {(tuple(f["constrained_columns"]), f["referred_table"], tuple(f["referred_columns"]),
             (f.get("options") or {}).get("ondelete")) for f in fks}


def _needs_rebuild(insp, table):
    """True when an existing SQLite table deviates structurally from its frozen definition:
    a nullable key column, a column whose NOT NULL-ness or type family differs, a missing or
    different foreign key (including ON DELETE), or a missing primary key. Not limited to one symptom."""
    name = table.name
    if not insp.has_table(name):
        return False
    have = {c["name"]: c for c in insp.get_columns(name)}
    pk = insp.get_pk_constraint(name).get("constrained_columns") or []
    if pk != [c.name for c in table.primary_key.columns]:
        return True
    for col in table.columns:
        got = have.get(col.name)
        if got is None:
            continue                      # optional columns that are missing are added first (_ensure_columns)
        expect_nullable = col.nullable and not col.primary_key
        if bool(got["nullable"]) != expect_nullable:
            return True
        if _affinity(got["type"]) != _affinity(col.type):
            return True
    want_fks = {(tuple(c.name for c in fk.columns), fk.elements[0].column.table.name,
                 tuple(e.column.name for e in fk.elements), fk.ondelete) for fk in table.foreign_key_constraints}
    return _fk_signature(insp.get_foreign_keys(name)) != want_fks


def _ensure_columns(table):
    """A legacy table may predate some optional columns: add them (nullable) so the rebuild can copy by name.
    A missing NOT NULL column cannot be invented, so stop with a clear message instead."""
    have = {c["name"] for c in sa.inspect(op.get_bind()).get_columns(table.name)}
    for col in table.columns:
        if col.name in have:
            continue
        if not col.nullable and not col.primary_key:
            raise RuntimeError(f"Legacy table {table.name!r} lacks required column {col.name!r}; "
                               "it cannot be converted automatically. Nothing was changed for this table.")
        op.add_column(table.name, sa.Column(col.name, col.type, nullable=True))


def upgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)

    # 1. keep the legacy content fingerprint (both dialects)
    if insp.has_table("questions") and "q_hash" not in {c["name"] for c in insp.get_columns("questions")}:
        op.add_column("questions", sa.Column("q_hash", sa.String(32), nullable=True))

    # 2. SQLite: rebuild legacy-shaped tables in place, rows copied verbatim
    if bind.dialect.name == "sqlite":
        for table in _REBUILD_ORDER:
            if _needs_rebuild(sa.inspect(bind), table):
                _ensure_columns(table)
                with op.batch_alter_table(table.name, copy_from=table, recreate="always"):
                    pass

    # 3. normalise indexes
    for name, tbl in _LEGACY_INDEXES:
        i = sa.inspect(bind)
        if i.has_table(tbl) and any(ix["name"] == name for ix in i.get_indexes(tbl)):
            op.drop_index(name, table_name=tbl)
    for name, tbl, cols in _INDEXES:
        i = sa.inspect(bind)
        if i.has_table(tbl) and not any(ix["name"] == name for ix in i.get_indexes(tbl)) \
                and set(cols) <= {c["name"] for c in i.get_columns(tbl)}:
            op.create_index(name, tbl, cols, unique=False)


def downgrade() -> None:
    # Converging a schema is not reversed: the old shapes had no benefit and rebuilding them risks data.
    pass
