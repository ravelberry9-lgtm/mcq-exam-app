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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


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
