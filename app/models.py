"""
SQLAlchemy models — the 15 tables of the v3 schema.

Schema decisions baked in here (from REBUILD_PLAN_v3.md):
  - subjects + chapters are the durable library
  - questions is one table for practice/chapter/pyq via source_type
  - exams + exam_papers + exam_sections + exam_syllabus_items curate
    chapters into per-exam syllabi (so APPSC Group 2, Group 1, AP HC
    Civil Judge all share the subject library)
  - notes attach to chapters; pages are free-form admin content
  - nav_items unifies home tiles + side menu (surface column distinguishes)
  - study_plans + chapter_progress track per-user progress (device_id
    kept for future multi-device; login deferred per 26-May decision)
"""
from datetime import datetime, date
from .db import db


# ─── Durable subject library ────────────────────────────────────

class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(64), unique=True, nullable=False)
    name_en = db.Column(db.String(128), nullable=False)
    name_te = db.Column(db.String(128), nullable=False)
    sort_order = db.Column(db.Integer, default=0)
    chapters = db.relationship("Chapter", back_populates="subject", cascade="all, delete-orphan")


class Chapter(db.Model):
    __tablename__ = "chapters"
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False, index=True)
    chapter_num = db.Column(db.Integer, nullable=False)
    title_en = db.Column(db.String(256), nullable=False)
    title_te = db.Column(db.String(256), nullable=False)
    est_read_minutes = db.Column(db.Integer, default=20)
    subject = db.relationship("Subject", back_populates="chapters")
    notes = db.relationship("Note", back_populates="chapter", cascade="all, delete-orphan")
    __table_args__ = (db.UniqueConstraint("subject_id", "chapter_num"),)


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False, index=True)
    section_num = db.Column(db.Integer, nullable=False)
    heading_en = db.Column(db.String(256))
    heading_te = db.Column(db.String(256))
    body_en = db.Column(db.Text)  # sanitized HTML
    body_te = db.Column(db.Text)
    chapter = db.relationship("Chapter", back_populates="notes")
    __table_args__ = (db.UniqueConstraint("chapter_id", "section_num"),)


class NoteBackup(db.Model):
    """A copy of a note taken *before* an import replaced or removed it, so the change can be undone.

    Deliberately has no foreign keys: a backup must outlive the chapter or note it was taken from.
    ``batch_id`` groups everything one import (or restore) touched; ``reason`` is 'replaced' or 'removed'.
    """
    __tablename__ = "note_backups"
    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.String(32), nullable=False, index=True)
    reason = db.Column(db.String(16), nullable=False)
    chapter_id = db.Column(db.Integer, nullable=False)
    section_num = db.Column(db.Integer, nullable=False)
    heading_en = db.Column(db.String(256))
    heading_te = db.Column(db.String(256))
    body_en = db.Column(db.Text)
    body_te = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Page(db.Model):
    """Admin-authored free-form content. Linkable from nav_items by slug."""
    __tablename__ = "pages"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(128), unique=True, nullable=False)
    title_en = db.Column(db.String(256), nullable=False)
    title_te = db.Column(db.String(256), nullable=False)
    body_en = db.Column(db.Text)
    body_te = db.Column(db.Text)
    page_type = db.Column(db.String(32), default="page")  # 'page' | 'notes' | 'guide'
    visible = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Passage(db.Model):
    """Shared reading-comprehension passage. Questions FK to this."""
    __tablename__ = "passages"
    id = db.Column(db.Integer, primary_key=True)
    text_en = db.Column(db.Text)
    text_te = db.Column(db.Text)


class Question(db.Model):
    """The one MCQ table. Replaces v1 questions + chapter_mcqs + pyq_questions."""
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False, index=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapters.id"), nullable=True, index=True)
    source_type = db.Column(db.String(16), nullable=False, index=True)  # 'practice'|'chapter'|'pyq'
    # md5 fingerprint of the question text, set by the content loader to avoid duplicates (kept from the legacy schema)
    q_hash = db.Column(db.String(32), index=True)
    pyq_year = db.Column(db.String(8))
    pyq_paper = db.Column(db.String(64))
    difficulty = db.Column(db.String(2), default="M")  # E/M/H
    question_en = db.Column(db.Text)
    question_te = db.Column(db.Text)
    options_en = db.Column(db.JSON)  # {"a": "...", "b": "...", ...}
    options_te = db.Column(db.JSON)
    correct_answer = db.Column(db.String(1), nullable=False)  # 'a'..'e' lowercase
    explanation_en = db.Column(db.Text)
    explanation_te = db.Column(db.Text)
    passage_id = db.Column(db.Integer, db.ForeignKey("passages.id"), nullable=True)
    # Where "Read this in notes" points. ``note_section_num`` is the section_num of a note in this question's chapter
    # (stable across note re-imports, unlike a note row id); NULL means "no exact section", and the review screens then
    # offer a clearly labelled chapter-level link instead. ``note_target_slug`` keeps the human-readable target the content
    # team assigned. Neither is ever shown as such to learners.
    note_section_num = db.Column(db.Integer, nullable=True)
    note_target_slug = db.Column(db.String(96), nullable=True)
    # Internal provenance (source ids, benchmark/origin, 'H' marker for Hanumanth Rao). Never rendered to learners.
    source_trace = db.Column(db.JSON, nullable=True)
    # Stable identifier from a prepared import package; makes re-running an import a no-op.
    import_ref = db.Column(db.String(64), nullable=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # ── canonical syllabus identity + provenance (all NULL for rows that predate them; see ``effective_source``) ──
    # Canonical identity: ONE primary chapter per question; further chapters are only tags.
    syllabus_chapter_id = db.Column(db.Integer, db.ForeignKey("syllabus_chapters.id"), nullable=True, index=True)
    subtopic_id = db.Column(db.Integer, db.ForeignKey("syllabus_subtopics.id"), nullable=True, index=True)
    secondary_tags = db.Column(db.JSON)       # e.g. {"chapters": ["u2-c14-..."], "subtopics": [...]}
    # Original source identity: never rewritten after import.
    source = db.Column(db.String(24))         # one of QUESTION_SOURCES
    source_file = db.Column(db.String(256))
    source_qid = db.Column(db.String(128))    # the id/number used in the source collection
    source_chapter = db.Column(db.String(64))  # original source chapter label, as written there
    qtype = db.Column(db.String(24))
    review_status = db.Column(db.String(24))  # one of REVIEW_STATUSES
    batch_id = db.Column(db.String(64))       # import batch that created the row
    # md5 of normalised question text + options; a cross-collection collision is a *warning*, never a silent discard
    content_hash = db.Column(db.String(32), index=True)

    __table_args__ = (db.Index("uq_questions_source_qid", "source", "source_qid", unique=True),)

    @property
    def effective_source(self):
        """Rows that predate provenance columns are the migrated old database: report them as ``legacy_db``
        without writing anything to them."""
        return self.source or "legacy_db"


# Allowed values, enforced by the importer and tests (the legacy ``questions`` table cannot take CHECK constraints in SQLite).
QUESTION_SOURCES = ("codex_generated", "app_master", "hanumanthrao", "pyq_compiled", "verified_pyq", "legacy_db")
REVIEW_STATUSES = ("raw", "structurally_valid", "content_review_required", "fact_verified", "bilingual_approved", "rejected")
LEARNER_VISIBLE_STATUS = "bilingual_approved"   # the only status shown in the canonical practice flow
CHAPTER_CLASSIFICATIONS = ("direct", "bridge", "thematic", "supplementary")
MICROTOPIC_SCOPES = ("direct", "supplementary_context")
SUPPLEMENTARY_TYPES = ("supplementary_cross_cutting", "supplementary_outside_direct_syllabus", "supplementary_post_syllabus",
                       "supplementary_context")


# ─── Canonical syllabus hierarchy (Subject → Unit → Chapter → Subtopic); separate from the source ``chapters`` ──

class SyllabusUnit(db.Model):
    """One of the five official APPSC units. Slugs are stable identifiers: never derived from, or changed with, a title."""
    __tablename__ = "syllabus_units"
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False, index=True)
    unit_num = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(64), unique=True, nullable=False)
    title_en = db.Column(db.String(256), nullable=False)
    title_te = db.Column(db.String(256), nullable=False)
    sort_order = db.Column(db.Integer, default=0)

    __table_args__ = (db.UniqueConstraint("subject_id", "unit_num"),)


class SyllabusChapter(db.Model):
    """An internal preparation chapter (NOT an official syllabus line). Core chapters have a unit and a number 1..31;
    the four supplementary reference chapters have neither and are never counted as core."""
    __tablename__ = "syllabus_chapters"
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False, index=True)
    unit_id = db.Column(db.Integer, db.ForeignKey("syllabus_units.id", ondelete="CASCADE"), nullable=True, index=True)
    chapter_num = db.Column(db.Integer)       # 1..31 for core chapters, NULL for supplementary
    slug = db.Column(db.String(96), unique=True, nullable=False)
    title_en = db.Column(db.String(256), nullable=False)
    title_te = db.Column(db.String(256), nullable=False)
    classification = db.Column(db.String(16), nullable=False)       # CHAPTER_CLASSIFICATIONS
    supplementary_type = db.Column(db.String(48))                   # SUPPLEMENTARY_TYPES, only when classification == 'supplementary'
    sort_order = db.Column(db.Integer, default=0)

    __table_args__ = (
        db.UniqueConstraint("subject_id", "chapter_num"),
        db.CheckConstraint("classification IN ('direct','bridge','thematic','supplementary')", name="ck_syllabus_chapters_classification"),
        db.CheckConstraint(
            "(classification = 'supplementary' AND supplementary_type IS NOT NULL AND unit_id IS NULL AND chapter_num IS NULL) OR "
            "(classification <> 'supplementary' AND supplementary_type IS NULL AND unit_id IS NOT NULL AND chapter_num IS NOT NULL)",
            name="ck_syllabus_chapters_core_vs_supplementary"),
    )

    @property
    def is_core(self):
        return self.classification != "supplementary"

    @property
    def counts_toward_completion(self):
        """Only the 31 core chapters count toward direct syllabus completion; supplementary chapters never do."""
        return self.is_core


class SyllabusSubtopic(db.Model):
    __tablename__ = "syllabus_subtopics"
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("syllabus_chapters.id", ondelete="CASCADE"), nullable=False, index=True)
    slug = db.Column(db.String(128), unique=True, nullable=False)
    subtopic_en = db.Column(db.String(256), nullable=False)
    subtopic_te = db.Column(db.String(256), nullable=False)
    search_key_te = db.Column(db.String(256))              # Telugu label with zero-width characters removed (for search)
    taxonomy_version = db.Column(db.String(32))            # e.g. 'ap-history-taxonomy-v1'
    sort_order = db.Column(db.Integer, default=0)


class SyllabusMicrotopic(db.Model):
    """Internal fine-grained tag under a learner-facing subtopic. Used for filtering and question tagging, never for navigation.
    ``old_draft_slug`` keeps the identity of the earlier 314-item draft subtopic that became this microtopic."""
    __tablename__ = "syllabus_microtopics"
    id = db.Column(db.Integer, primary_key=True)
    subtopic_id = db.Column(db.Integer, db.ForeignKey("syllabus_subtopics.id", ondelete="CASCADE"), nullable=False, index=True)
    slug = db.Column(db.String(128), unique=True, nullable=False)
    micro_en = db.Column(db.String(256), nullable=False)
    micro_te = db.Column(db.String(256), nullable=False)
    search_key_te = db.Column(db.String(256))
    scope = db.Column(db.String(24), nullable=False, default="direct")     # MICROTOPIC_SCOPES
    old_draft_slug = db.Column(db.String(128))
    taxonomy_version = db.Column(db.String(32))
    sort_order = db.Column(db.Integer, default=0)

    __table_args__ = (db.CheckConstraint("scope IN ('direct','supplementary_context')", name="ck_syllabus_microtopics_scope"),)


class ChapterSourceMap(db.Model):
    """Old-source-content → canonical mapping (note sections now; question collections later). Keyed by the *source chapter
    number* and section number, not by database ids, which differ between environments. Rows start as ``draft``; nothing reads
    this table for display until a mapping is approved."""
    __tablename__ = "chapter_source_map"
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False, index=True)
    source_chapter_num = db.Column(db.Integer, nullable=False)
    section_num = db.Column(db.Integer)       # NULL = the whole source chapter
    syllabus_chapter_id = db.Column(db.Integer, db.ForeignKey("syllabus_chapters.id", ondelete="CASCADE"), nullable=False, index=True)
    subtopic_id = db.Column(db.Integer, db.ForeignKey("syllabus_subtopics.id", ondelete="SET NULL"), nullable=True)
    relation = db.Column(db.String(12), nullable=False, default="primary")   # 'primary' | 'secondary'
    mapping_kind = db.Column(db.String(24))   # direct | bridge | cross_cutting | supplementary
    confidence = db.Column(db.String(8))      # high | medium | low
    reason = db.Column(db.String(512))
    status = db.Column(db.String(12), nullable=False, default="draft")       # 'draft' | 'approved'

    __table_args__ = (db.UniqueConstraint("subject_id", "source_chapter_num", "section_num", "syllabus_chapter_id", "relation"),)


class ExpandedNote(db.Model):
    """Package notes (core sections, addendum items, Group-1 discussions) kept SEPARATE from the 17 legacy ``notes`` rows.
    Keyed by the canonical syllabus chapter (portable across databases) and a stable ``anchor_id`` such as CH01-S14.
    ``package_section`` is the section number inside the package and is never an app note section number."""
    __tablename__ = "expanded_notes"
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False, index=True)
    syllabus_chapter_id = db.Column(db.Integer, db.ForeignKey("syllabus_chapters.id", ondelete="CASCADE"), nullable=False, index=True)
    anchor_id = db.Column(db.String(32), nullable=False)
    kind = db.Column(db.String(20), nullable=False)          # core | addendum | addendum_group1 | group1 | revision
    package_section = db.Column(db.Integer)                  # core sections only
    sort_order = db.Column(db.Integer, default=0)
    heading_en = db.Column(db.String(300), nullable=False)
    heading_te = db.Column(db.String(300))
    body_en = db.Column(db.Text)
    body_te = db.Column(db.Text)
    sources = db.Column(db.JSON)                             # [{"label": "...", "url": "..."}]
    core_connections = db.Column(db.JSON)                    # anchor ids of core sections an addendum item extends
    package_batch_id = db.Column(db.String(64))
    content_hash = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint("subject_id", "anchor_id", name="uq_expanded_notes_anchor"),
                      db.CheckConstraint("kind IN ('core','addendum','addendum_group1','group1','revision')", name="ck_expanded_notes_kind"))


class ExpandedNoteAppMap(db.Model):
    """Explicit, reviewable mapping from a package note anchor to an EXISTING app note section (``notes.section_num`` of a
    legacy source chapter, identified by chapter number, never by database id). Rows start as ``draft``; learner pages only use
    ``approved`` rows. Package section numbers are never reused as app section numbers."""
    __tablename__ = "expanded_note_app_map"
    id = db.Column(db.Integer, primary_key=True)
    expanded_note_id = db.Column(db.Integer, db.ForeignKey("expanded_notes.id", ondelete="CASCADE"), nullable=False, index=True)
    source_chapter_num = db.Column(db.Integer, nullable=False)
    app_section_num = db.Column(db.Integer, nullable=False)
    relation = db.Column(db.String(12), nullable=False, default="related")   # same_topic | related
    status = db.Column(db.String(12), nullable=False, default="draft")       # draft | approved
    reason = db.Column(db.String(512))

    __table_args__ = (db.UniqueConstraint("expanded_note_id", "source_chapter_num", "app_section_num", name="uq_expanded_note_app_map"),
                      db.CheckConstraint("status IN ('draft','approved')", name="ck_expanded_note_app_map_status"))


# ─── Exam definitions (curated views over the subject library) ──

class Exam(db.Model):
    __tablename__ = "exams"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(64), unique=True, nullable=False)
    name_en = db.Column(db.String(128), nullable=False)
    name_te = db.Column(db.String(128), nullable=False)
    conducting_body = db.Column(db.String(128))
    active = db.Column(db.Boolean, default=True)
    papers = db.relationship("ExamPaper", back_populates="exam", cascade="all, delete-orphan")


class ExamPaper(db.Model):
    __tablename__ = "exam_papers"
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey("exams.id", ondelete="CASCADE"), nullable=False, index=True)
    paper_num = db.Column(db.Integer, nullable=False)  # 0 = screening
    name_en = db.Column(db.String(128), nullable=False)
    name_te = db.Column(db.String(128), nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)
    duration_min = db.Column(db.Integer)
    exam = db.relationship("Exam", back_populates="papers")
    sections = db.relationship("ExamSection", back_populates="paper", cascade="all, delete-orphan")
    __table_args__ = (db.UniqueConstraint("exam_id", "paper_num"),)


class ExamSection(db.Model):
    __tablename__ = "exam_sections"
    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey("exam_papers.id", ondelete="CASCADE"), nullable=False, index=True)
    section_label = db.Column(db.String(8))  # 'A' | 'B' | None
    name_en = db.Column(db.String(256), nullable=False)
    name_te = db.Column(db.String(256), nullable=False)
    marks = db.Column(db.Integer, nullable=False)
    sort_order = db.Column(db.Integer, default=0)
    paper = db.relationship("ExamPaper", back_populates="sections")
    syllabus_items = db.relationship("ExamSyllabusItem", back_populates="section", cascade="all, delete-orphan")


class ExamSyllabusItem(db.Model):
    """Join: section ↔ chapter, with optional marks weighting."""
    __tablename__ = "exam_syllabus_items"
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey("exam_sections.id", ondelete="CASCADE"), nullable=False, index=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False, index=True)
    weight_marks = db.Column(db.Integer)
    sort_order = db.Column(db.Integer, default=0)
    section = db.relationship("ExamSection", back_populates="syllabus_items")
    __table_args__ = (db.UniqueConstraint("section_id", "chapter_id"),)


# ─── Navigation (unified home tiles + side menu) ────────────────

class NavItem(db.Model):
    """Both home tiles and side-menu items live here, distinguished by surface."""
    __tablename__ = "nav_items"
    id = db.Column(db.Integer, primary_key=True)
    surface = db.Column(db.String(8), nullable=False, index=True)  # 'home' | 'menu'
    parent_id = db.Column(db.Integer, db.ForeignKey("nav_items.id", ondelete="CASCADE"), nullable=True, index=True)
    label_en = db.Column(db.String(128), nullable=False)
    label_te = db.Column(db.String(128), nullable=False)
    icon = db.Column(db.String(64))
    action_type = db.Column(db.String(32))  # 'subject'|'exam'|'chapter'|'page'|'route'|'url'
    action_ref = db.Column(db.String(256))
    sort_order = db.Column(db.Integer, default=0)
    visible = db.Column(db.Boolean, default=True)
    children = db.relationship("NavItem", backref=db.backref("parent", remote_side=[id]))


# ─── Per-user state (device_id kept for future multi-device) ────

class UserQuestionState(db.Model):
    __tablename__ = "user_question_state"
    device_id = db.Column(db.String(64), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id", ondelete="CASCADE"), primary_key=True)
    seen_count = db.Column(db.Integer, default=0)
    wrong_count = db.Column(db.Integer, default=0)
    flagged = db.Column(db.Boolean, default=False)
    saved = db.Column(db.Boolean, default=False)
    last_seen_at = db.Column(db.DateTime)
    last_confidence = db.Column(db.Integer)  # 1..5


class ExamSession(db.Model):
    __tablename__ = "exam_sessions"
    id = db.Column(db.String(64), primary_key=True)  # uuid
    device_id = db.Column(db.String(64), nullable=False, index=True)
    config = db.Column(db.JSON, nullable=False)
    question_ids = db.Column(db.JSON, nullable=False)
    answers = db.Column(db.JSON, default=dict)
    confidences = db.Column(db.JSON, default=dict)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    submitted_at = db.Column(db.DateTime)
    score = db.Column(db.Integer)
    total = db.Column(db.Integer)


class StudyPlan(db.Model):
    """One active plan at a time per device (enforced in service layer for now)."""
    __tablename__ = "study_plans"
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), nullable=False, index=True)
    exam_id = db.Column(db.Integer, db.ForeignKey("exams.id"), nullable=True)
    name = db.Column(db.String(128), nullable=False)
    subject_ids = db.Column(db.JSON)  # optional subset of exam's subjects
    target_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(16), default="active")  # active|paused|completed|template
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ChapterProgress(db.Model):
    __tablename__ = "chapter_progress"
    device_id = db.Column(db.String(64), primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey("chapters.id", ondelete="CASCADE"), primary_key=True)
    status = db.Column(db.String(16), nullable=False, default="not_started")  # not_started|in_progress|completed
    current_section = db.Column(db.Integer)
    marked_complete_at = db.Column(db.DateTime)
    last_opened_at = db.Column(db.DateTime)
