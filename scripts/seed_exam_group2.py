"""
Seed APPSC Group 2 exam syllabus.

Walks subjects/chapters that seed_dev.py already inserted and wires
them into exam_papers + exam_sections + exam_syllabus_items per
REBUILD_PLAN_v3.md §6.

Run after seed_dev.py:
    python scripts/seed_dev.py
    python scripts/seed_exam_group2.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app
from app.db import db
from app.models import (
    Exam, ExamPaper, ExamSection, ExamSyllabusItem,
    Subject, Chapter, NavItem,
)


EXAM = {
    "slug": "appsc_group_2",
    "name_en": "APPSC Group 2",
    "name_te": "ఏపీపీఎస్‌సీ గ్రూప్ 2",
    "conducting_body": "Andhra Pradesh Public Service Commission",
}


# Each paper: (paper_num, name_en, name_te, total_marks, duration_min, sections)
# Each section: (label, name_en, name_te, marks, sort_order, [subject_slugs])
# Sections reference WHOLE subjects — syllabus items expand to all chapters
PAPERS = [
    (
        0, "Screening Test", "స్క్రీనింగ్ టెస్ట్", 150, 150,
        [
            (None, "Indian History",   "భారత చరిత్ర",            30, 1, ["indian_history"]),
            (None, "Geography",        "భూగోళశాస్త్రం",          30, 2, ["indian_geography", "ap_geography"]),
            (None, "Indian Society",   "భారత సమాజం",             30, 3, ["indian_society"]),
            (None, "Current Affairs",  "ప్రస్తుత వ్యవహారాలు",   30, 4, ["current_affairs"]),
            (None, "Mental Ability",   "మానసిక సామర్థ్యం",      30, 5, ["mental_ability"]),
        ],
    ),
    (
        1, "Main Paper I", "మెయిన్ పేపర్ I", 150, 150,
        [
            ("A", "AP Social & Cultural History", "ఆంధ్రప్రదేశ్ సామాజిక సాంస్కృతిక చరిత్ర", 75, 1, ["ap_history"]),
            ("B", "Indian Constitution",           "భారత రాజ్యాంగం",                          75, 2, ["indian_constitution"]),
        ],
    ),
    (
        2, "Main Paper II", "మెయిన్ పేపర్ II", 150, 150,
        [
            ("A", "Indian & AP Economy", "భారత & ఆంధ్రప్రదేశ్ ఆర్థిక వ్యవస్థ", 75, 1, ["indian_economy", "ap_economy"]),
            ("B", "Science & Technology", "సైన్స్ & సాంకేతికత",                    75, 2, ["science_technology"]),
        ],
    ),
]


def upsert_exam():
    e = Exam.query.filter_by(slug=EXAM["slug"]).first()
    if e:
        e.name_en = EXAM["name_en"]
        e.name_te = EXAM["name_te"]
        e.conducting_body = EXAM["conducting_body"]
        e.active = True
    else:
        e = Exam(**EXAM, active=True)
        db.session.add(e)
    db.session.flush()
    return e


def upsert_paper(exam_id, num, name_en, name_te, marks, duration):
    p = ExamPaper.query.filter_by(exam_id=exam_id, paper_num=num).first()
    if p:
        p.name_en, p.name_te, p.total_marks, p.duration_min = name_en, name_te, marks, duration
    else:
        p = ExamPaper(exam_id=exam_id, paper_num=num, name_en=name_en, name_te=name_te,
                      total_marks=marks, duration_min=duration)
        db.session.add(p)
    db.session.flush()
    return p


def upsert_section(paper_id, label, name_en, name_te, marks, sort_order):
    q = ExamSection.query.filter_by(paper_id=paper_id, name_en=name_en)
    s = q.first()
    if s:
        s.section_label, s.name_te, s.marks, s.sort_order = label, name_te, marks, sort_order
    else:
        s = ExamSection(paper_id=paper_id, section_label=label,
                        name_en=name_en, name_te=name_te,
                        marks=marks, sort_order=sort_order)
        db.session.add(s)
    db.session.flush()
    return s


def link_chapters_to_section(section, chapter_ids):
    # Wipe + re-insert syllabus items for this section so re-runs are idempotent
    ExamSyllabusItem.query.filter_by(section_id=section.id).delete()
    db.session.flush()
    for order, cid in enumerate(chapter_ids):
        db.session.add(ExamSyllabusItem(section_id=section.id, chapter_id=cid, sort_order=order))


def seed():
    app = create_app()
    with app.app_context():
        # Sanity: subjects must exist
        slugs_needed = set()
        for _, _, _, _, _, sections in PAPERS:
            for _, _, _, _, _, subj_slugs in sections:
                slugs_needed.update(subj_slugs)
        existing = {s.slug: s for s in Subject.query.filter(Subject.slug.in_(slugs_needed)).all()}
        missing = slugs_needed - set(existing.keys())
        if missing:
            print(f"  ERROR: missing subjects, run seed_dev.py first: {missing}")
            return

        # Map subject_slug -> [chapter_id, ...]
        subj_to_chapter_ids = {}
        for slug, subj in existing.items():
            chs = Chapter.query.filter_by(subject_id=subj.id).order_by(Chapter.chapter_num).all()
            subj_to_chapter_ids[slug] = [c.id for c in chs]

        exam = upsert_exam()
        print(f"  exam: {exam.slug} (id={exam.id})")

        total_sections = 0
        total_items = 0
        for paper_num, paper_en, paper_te, marks, duration, sections in PAPERS:
            paper = upsert_paper(exam.id, paper_num, paper_en, paper_te, marks, duration)
            for label, name_en, name_te, sec_marks, sec_order, subj_slugs in sections:
                section = upsert_section(paper.id, label, name_en, name_te, sec_marks, sec_order)
                chapter_ids = []
                for s in subj_slugs:
                    chapter_ids.extend(subj_to_chapter_ids.get(s, []))
                link_chapters_to_section(section, chapter_ids)
                total_sections += 1
                total_items += len(chapter_ids)
        print(f"  papers: {len(PAPERS)} · sections: {total_sections} · syllabus_items: {total_items}")

        # Nav: add Exams parent + Group 2 child if missing
        exams_parent = NavItem.query.filter_by(surface="menu", label_en="Exams", parent_id=None).first()
        if not exams_parent:
            exams_parent = NavItem(surface="menu", label_en="Exams", label_te="పరీక్షలు",
                                   icon="trophy", sort_order=15)
            db.session.add(exams_parent)
            db.session.flush()
        g2 = NavItem.query.filter_by(surface="menu", label_en="APPSC Group 2", parent_id=exams_parent.id).first()
        if not g2:
            db.session.add(NavItem(
                surface="menu", parent_id=exams_parent.id,
                label_en="APPSC Group 2", label_te="ఏపీపీఎస్‌సీ గ్రూప్ 2",
                action_type="exam", action_ref=EXAM["slug"], sort_order=1,
            ))
        print("  nav: Exams > APPSC Group 2 added")

        db.session.commit()
        print("group 2 syllabus seeded.")


if __name__ == "__main__":
    seed()
