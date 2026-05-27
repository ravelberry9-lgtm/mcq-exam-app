"""Phase 0 smoke test — proves the app boots and the schema is queryable."""
from app.models import (
    Subject, Chapter, Note, Page, Passage, Question,
    Exam, ExamPaper, ExamSection, ExamSyllabusItem,
    NavItem, UserQuestionState, ExamSession, StudyPlan, ChapterProgress,
)
from app.db import db


def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"APPSC" in response.data


def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
    assert "phase" in response.json


def test_all_15_tables_exist(app):
    """Every model maps to a real table after create_all."""
    expected = {
        "subjects", "chapters", "notes", "pages", "passages", "questions",
        "exams", "exam_papers", "exam_sections", "exam_syllabus_items",
        "nav_items", "user_question_state", "exam_sessions",
        "study_plans", "chapter_progress",
    }
    actual = set(db.metadata.tables.keys())
    assert expected == actual, f"missing: {expected - actual}, extra: {actual - expected}"


def test_can_insert_subject_and_chapter(app):
    s = Subject(slug="indian_constitution", name_en="Indian Constitution", name_te="భారత రాజ్యాంగం")
    db.session.add(s)
    db.session.flush()
    c = Chapter(subject_id=s.id, chapter_num=1, title_en="Preamble", title_te="ప్రవేశిక")
    db.session.add(c)
    db.session.commit()
    assert s.id is not None
    assert c.subject_id == s.id
    assert len(s.chapters) == 1


def test_can_insert_exam_and_syllabus(app):
    s = Subject(slug="polity", name_en="Polity", name_te="పాలిటీ")
    db.session.add(s)
    db.session.flush()
    c = Chapter(subject_id=s.id, chapter_num=1, title_en="Ch1", title_te="అధ్యాయం 1")
    db.session.add(c)
    db.session.flush()
    e = Exam(slug="appsc_group_2", name_en="APPSC Group 2", name_te="ఏపీపీఎస్‌సీ గ్రూప్ 2")
    db.session.add(e)
    db.session.flush()
    p = ExamPaper(exam_id=e.id, paper_num=1, name_en="Paper I", name_te="పేపర్ I", total_marks=150)
    db.session.add(p)
    db.session.flush()
    sec = ExamSection(paper_id=p.id, section_label="B", name_en="Constitution", name_te="రాజ్యాంగం", marks=75)
    db.session.add(sec)
    db.session.flush()
    item = ExamSyllabusItem(section_id=sec.id, chapter_id=c.id, weight_marks=15)
    db.session.add(item)
    db.session.commit()
    assert item.id is not None
    assert len(sec.syllabus_items) == 1


def test_nav_item_self_reference(app):
    """Side menu with nested children works."""
    parent = NavItem(surface="menu", label_en="Subjects", label_te="విషయాలు")
    db.session.add(parent)
    db.session.flush()
    child = NavItem(surface="menu", parent_id=parent.id,
                    label_en="Polity", label_te="పాలిటీ",
                    action_type="subject", action_ref="polity")
    db.session.add(child)
    db.session.commit()
    assert child.parent_id == parent.id
    assert len(parent.children) == 1
