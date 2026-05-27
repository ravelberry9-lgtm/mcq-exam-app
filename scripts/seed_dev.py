"""
Seed dev data â all 11 v3 subjects, sample chapters, sample bilingual
questions, nav items. Idempotent: re-running upserts by slug.

Run:
    python scripts/seed_dev.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app
from app.db import db
from app.models import Subject, Chapter, Question, NavItem


# All 11 subjects per REBUILD_PLAN_v3.md Â§4
SUBJECTS = [
    ("indian_history",      "Indian History",       "à°­à°¾à°°à°¤ à°à°°à°¿à°¤à±à°°",                  1),
    ("indian_constitution", "Indian Constitution",  "à°­à°¾à°°à°¤ à°°à°¾à°à±à°¯à°¾à°à°à°",                2),
    ("ap_history",          "AP Social & Cultural History", "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°à°°à°¿à°¤à±à°°",   3),
    ("indian_geography",    "Indian Geography",     "à°­à°¾à°°à°¤ à°­à±à°à±à°³à°¶à°¾à°¸à±à°¤à±à°°à°",            4),
    ("ap_geography",        "AP Geography",         "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°­à±à°à±à°³à°¶à°¾à°¸à±à°¤à±à°°à°",     5),
    ("indian_economy",      "Indian Economy",       "à°­à°¾à°°à°¤ à°à°°à±à°¥à°¿à° à°µà±à°¯à°µà°¸à±à°¥",           6),
    ("ap_economy",          "AP Economy",           "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°à°°à±à°¥à°¿à° à°µà±à°¯à°µà°¸à±à°¥",    7),
    ("science_technology",  "Science & Technology", "à°¸à±à°¨à±à°¸à± & à°¸à°¾à°à°à±à°¤à°¿à°à°¤",            8),
    ("indian_society",      "Indian Society",       "à°­à°¾à°°à°¤ à°¸à°®à°¾à°à°",                   9),
    ("mental_ability",      "Mental Ability",       "à°®à°¾à°¨à°¸à°¿à° à°¸à°¾à°®à°°à±à°¥à±à°¯à°",             10),
    ("current_affairs",     "Current Affairs",      "à°ªà±à°°à°¸à±à°¤à±à°¤ à°µà±à°¯à°µà°¹à°¾à°°à°¾à°²à±",          11),
]

# subject_slug -> [(chapter_num, title_en, title_te)]
CHAPTERS = {
    "indian_history": [
        (1, "Indus Valley Civilization", "à°¸à°¿à°à°§à± à°¨à°¾à°à°°à°¿à°à°¤"),
        (2, "Mauryan Empire", "à°®à±à°°à±à°¯ à°¸à°¾à°®à±à°°à°¾à°à±à°¯à°"),
    ],
    "indian_constitution": [
        (1, "Preamble", "à°ªà±à°°à°µà±à°¶à°¿à°"),
        (2, "Fundamental Rights", "à°ªà±à°°à°¾à°¥à°®à°¿à° à°¹à°à±à°à±à°²à±"),
        (3, "Directive Principles", "à°à°¦à±à°¶à° à°¸à±à°¤à±à°°à°¾à°²à±"),
    ],
    "ap_history": [
        (1, "Satavahanas & Ikshvakus", "à°¶à°¾à°¤à°µà°¾à°¹à°¨à±à°²à± & à°à°à±à°·à±à°µà°¾à°à±à°²à±"),
    ],
    "indian_geography": [
        (1, "Location & Physiography", "à°¸à±à°¥à°¾à°¨à° & à°­à±à°¤à°¿à° à°²à°à±à°·à°£à°¾à°²à±"),
    ],
    "ap_geography": [
        (1, "Location & Physical Setting of AP", "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°¸à±à°¥à°¾à°¨à°"),
    ],
    "indian_economy": [
        (1, "National Income", "à°à°¾à°¤à±à°¯ à°à°¦à°¾à°¯à°"),
    ],
    "ap_economy": [
        (1, "AP GSDP & Sectoral Contribution", "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± GSDP"),
    ],
    "science_technology": [
        (1, "Space Technology", "à°à°à°¤à°°à°¿à°à±à°· à°¸à°¾à°à°à±à°¤à°¿à°à°¤"),
    ],
    "indian_society": [
        (1, "Caste, Class & Family", "à°à±à°²à°, à°µà°°à±à°à°, à°à±à°à±à°à°¬à°"),
    ],
    "mental_ability": [
        (1, "Number Series", "à°¸à°à°à±à°¯à°¾ à°¶à±à°°à±à°£à°¿"),
    ],
    "current_affairs": [],  # rolling, no chapters
}

# (subject_slug, chapter_num, qen, qte, oen, ote, correct, eexp, texp, diff)
QUESTIONS = [
    (
        "indian_constitution", 2,
        "In which part of the Indian Constitution are the Fundamental Rights enshrined?",
        "à°­à°¾à°°à°¤ à°°à°¾à°à±à°¯à°¾à°à°à°à°²à± à°ªà±à°°à°¾à°¥à°®à°¿à° à°¹à°à±à°à±à°²à± à° à°­à°¾à°à°à°²à± à°à°¨à±à°¨à°¾à°¯à°¿?",
        {"a": "Part II", "b": "Part III", "c": "Part IV", "d": "Part V"},
        {"a": "à°­à°¾à°à° II", "b": "à°­à°¾à°à° III", "c": "à°­à°¾à°à° IV", "d": "à°­à°¾à°à° V"},
        "b",
        "Articles 12 to 35 in Part III of the Constitution guarantee six categories of fundamental rights.",
        "à°°à°¾à°à±à°¯à°¾à°à°à°à°²à±à°¨à°¿ à°­à°¾à°à° IIIà°²à±à°¨à°¿ à°à°§à°¿à°à°°à°£à°²à± 12 à°¨à±à°à°¡à°¿ 35 à°µà°°à°à± à°à°°à± à°°à°à°¾à°² à°ªà±à°°à°¾à°¥à°®à°¿à° à°¹à°à±à°à±à°²à°¨à± à°¹à°¾à°®à± à°à°¸à±à°¤à°¾à°¯à°¿.",
        "M",
    ),
    (
        "indian_constitution", 1,
        "The Preamble of the Indian Constitution begins with which words?",
        "à°­à°¾à°°à°¤ à°°à°¾à°à±à°¯à°¾à°à° à°ªà±à°°à°µà±à°¶à°¿à° à° à°ªà°¦à°¾à°²à°¤à± à°®à±à°¦à°²à°µà±à°¤à±à°à°¦à°¿?",
        {"a": "We the People", "b": "India that is Bharat", "c": "Sovereign Socialist", "d": "Justice Liberty"},
        {"a": "à°®à±à°®à± à°­à°¾à°°à°¤ à°ªà±à°°à°à°²à°®à±", "b": "à°à°à°¡à°¿à°¯à°¾ à°à°¨à°à°¾ à°­à°¾à°°à°¤à±", "c": "à°¸à°°à±à°µà°¸à°¤à±à°¤à°¾à° à°¸à°¾à°®à±à°¯à°µà°¾à°¦", "d": "à°¨à±à°¯à°¾à°¯à°®à± à°¸à±à°µà±à°à±à°"},
        "a",
        "The Preamble opens with the words 'We, the People of India' â emphasising the source of authority is the people.",
        "à°ªà±à°°à°µà±à°¶à°¿à° 'à°®à±à°®à± à°­à°¾à°°à°¤ à°ªà±à°°à°à°²à°®à±' à°à°¨à± à°ªà°¦à°¾à°²à°¤à± à°®à±à°¦à°²à°µà±à°¤à±à°à°¦à°¿ â à°à°§à°¿à°à°¾à°°à° à°ªà±à°°à°à°² à°¨à±à°à°¡à± à°µà°¸à±à°¤à±à°à°¦à°¨à°¿ à°¤à±à°²à°¿à°¯à°à±à°¸à±à°¤à±à°à°¦à°¿.",
        "E",
    ),
    (
        "indian_history", 1,
        "Which Harappan site was the largest in terms of area?",
        "à°µà°¿à°¸à±à°¤à±à°°à±à°£à° à°ªà±à°°à°à°¾à°°à° à°à°¤à°¿à°ªà±à°¦à±à°¦ à°¹à°°à°ªà±à°ªà°¾ à°à±à°à°¦à±à°°à° à°à°¦à°¿?",
        {"a": "Harappa", "b": "Mohenjo-daro", "c": "Rakhigarhi", "d": "Lothal"},
        {"a": "à°¹à°°à°ªà±à°ªà°¾", "b": "à°®à±à°¹à±à°à°à±à°¦à°¾à°°à±", "c": "à°°à°¾à°à±à°à°¢à±", "d": "à°²à±à°¥à°¾à°²à±"},
        "c",
        "Rakhigarhi in Haryana is now recognised as the largest Harappan site discovered, surpassing Mohenjo-daro in area.",
        "à°¹à°°à±à°¯à°¾à°¨à°¾à°²à±à°¨à°¿ à°°à°¾à°à±à°à°¢à± à°à°ªà±à°ªà°à°¿à°µà°°à°à± à°à°¨à±à°à±à°¨à°¬à°¡à°¿à°¨ à°à°¤à°¿à°ªà±à°¦à±à°¦ à°¹à°°à°ªà±à°ªà°¾ à°à±à°à°¦à±à°°à°à°à°¾ à°à±à°°à±à°¤à°¿à°à°à°¬à°¡à°¿à°à°¦à°¿, à°®à±à°¹à±à°à°à±à°¦à°¾à°°à± à°à°à°à± à°à°à±à°à±à°µ à°µà°¿à°¸à±à°¤à±à°°à±à°£à° à°à°²à°¿à°à°¿ à°à°à°¦à°¿.",
        "H",
    ),
    (
        "indian_geography", 1,
        "Which is the southernmost point of mainland India?",
        "à°­à°¾à°°à°¤ à°ªà±à°°à°§à°¾à°¨ à°­à±à°­à°¾à°à°à°²à± à°à°¤à±à°¯à°à°¤ à°¦à°à±à°·à°¿à°£ à°¬à°¿à°à°¦à±à°µà± à°à°¦à°¿?",
        {"a": "Indira Point", "b": "Kanyakumari", "c": "Rameswaram", "d": "Trivandrum"},
        {"a": "à°à°à°¦à°¿à°°à°¾ à°ªà°¾à°¯à°¿à°à°à±", "b": "à°à°¨à±à°¯à°¾à°à±à°®à°¾à°°à°¿", "c": "à°°à°¾à°®à±à°¶à±à°µà°°à°", "d": "à°¤à°¿à°°à±à°µà°¨à°à°¤à°ªà±à°°à°"},
        "b",
        "Kanyakumari is the southernmost point of the Indian mainland. Indira Point in the Nicobars is southernmost overall but not mainland.",
        "à°à°¨à±à°¯à°¾à°à±à°®à°¾à°°à°¿ à°­à°¾à°°à°¤ à°ªà±à°°à°§à°¾à°¨ à°­à±à°­à°¾à°à°à°²à±à°¨à°¿ à°à°¤à±à°¯à°à°¤ à°¦à°à±à°·à°¿à°£ à°¬à°¿à°à°¦à±à°µà±. à°¨à°¿à°à±à°¬à°¾à°°à±âà°²à±à°¨à°¿ à°à°à°¦à°¿à°°à°¾ à°ªà°¾à°¯à°¿à°à°à± à°®à±à°¤à±à°¤à° à°­à±à°­à°¾à°à°à°²à± à°à°¤à±à°¯à°à°¤ à°¦à°à±à°·à°¿à°£à°, à°à°¾à°¨à± à°ªà±à°°à°§à°¾à°¨ à°­à±à°­à°¾à°à° à°à°¾à°¦à±.",
        "M",
    ),
    (
        "ap_geography", 1,
        "Andhra Pradesh shares its longest land border with which state?",
        "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à° à°°à°¾à°·à±à°à±à°°à°à°¤à± à°à°¤à±à°¯à°à°¤ à°ªà±à°¡à°µà±à°¨ à°­à± à°¸à°°à°¿à°¹à°¦à±à°¦à±à°¨à± à°ªà°à°à±à°à±à°à°à±à°à°¦à°¿?",
        {"a": "Karnataka", "b": "Tamil Nadu", "c": "Telangana", "d": "Odisha"},
        {"a": "à°à°°à±à°£à°¾à°à°", "b": "à°¤à°®à°¿à°³à°¨à°¾à°¡à±", "c": "à°¤à±à°²à°à°à°¾à°£", "d": "à°à°¡à°¿à°¶à°¾"},
        "c",
        "After the 2014 bifurcation, Andhra Pradesh shares its longest land border with the newly formed state of Telangana.",
        "2014 à°µà°¿à°­à°à°¨ à°¤à°°à±à°µà°¾à°¤, à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°à±à°¤à±à°¤à°à°¾ à°à°°à±à°ªà°¡à°¿à°¨ à°¤à±à°²à°à°à°¾à°£ à°°à°¾à°·à±à°à±à°°à°à°¤à± à°à°¤à±à°¯à°à°¤ à°ªà±à°¡à°µà±à°¨ à°­à± à°¸à°°à°¿à°¹à°¦à±à°¦à±à°¨à± à°ªà°à°à±à°à±à°à°à±à°à°¦à°¿.",
        "E",
    ),
]


# (surface, label_en, label_te, icon, action_type, action_ref, parent_label, sort_order)
NAV_ITEMS = [
    ("menu", "Home",     "à°¹à±à°®à±",     "home",     "route", "/",         None,       0),
    ("menu", "Subjects", "à°µà°¿à°·à°¯à°¾à°²à±", "books",    None,    None,        None,      10),
    # Subjects (children of "Subjects" parent) â all 11
    ("menu", "Indian History",       "à°­à°¾à°°à°¤ à°à°°à°¿à°¤à±à°°",            None, "subject", "indian_history",       "Subjects",  1),
    ("menu", "Indian Constitution",  "à°­à°¾à°°à°¤ à°°à°¾à°à±à°¯à°¾à°à°à°",          None, "subject", "indian_constitution",  "Subjects",  2),
    ("menu", "AP History",           "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°à°°à°¿à°¤à±à°°",     None, "subject", "ap_history",           "Subjects",  3),
    ("menu", "Indian Geography",     "à°­à°¾à°°à°¤ à°­à±à°à±à°³à°¶à°¾à°¸à±à°¤à±à°°à°",      None, "subject", "indian_geography",     "Subjects",  4),
    ("menu", "AP Geography",         "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°­à±à°à±à°³à°¶à°¾à°¸à±à°¤à±à°°à°", None, "subject", "ap_geography",         "Subjects",  5),
    ("menu", "Indian Economy",       "à°­à°¾à°°à°¤ à°à°°à±à°¥à°¿à° à°µà±à°¯à°µà°¸à±à°¥",     None, "subject", "indian_economy",       "Subjects",  6),
    ("menu", "AP Economy",           "à°à°à°§à±à°°à°ªà±à°°à°¦à±à°¶à± à°à°°à±à°¥à°¿à° à°µà±à°¯à°µà°¸à±à°¥", None, "subject", "ap_economy",          "Subjects",  7),
    ("menu", "Science & Technology", "à°¸à±à°¨à±à°¸à± & à°¸à°¾à°à°à±à°¤à°¿à°à°¤",     None, "subject", "science_technology",   "Subjects",  8),
    ("menu", "Indian Society",       "à°­à°¾à°°à°¤ à°¸à°®à°¾à°à°",             None, "subject", "indian_society",       "Subjects",  9),
    ("menu", "Mental Ability",       "à°®à°¾à°¨à°¸à°¿à° à°¸à°¾à°®à°°à±à°¥à±à°¯à°",       None, "subject", "mental_ability",       "Subjects", 10),
    ("menu", "Current Affairs",      "à°ªà±à°°à°¸à±à°¤à±à°¤ à°µà±à°¯à°µà°¹à°¾à°°à°¾à°²à±",     None, "subject", "current_affairs",      "Subjects", 11),
    # Top-level shortcuts
    ("menu", "Study Plan", "à°¸à±à°à°¡à± à°ªà±à°²à°¾à°¨à±", "plan", "route", "/plan/",                None, 20),
    ("menu", "Exams",      "à°ªà°°à±à°à±à°·à°²à±",      "exam", "route", "/exam/appsc_group_2",   None, 30),
    # Bottom rail
    ("menu", "Settings", "à°à°®à°°à°¿à°à°²à±",   "settings", "route", "/settings", None, 90),
    ("menu", "Admin",    "à°¨à°¿à°°à±à°µà°¾à°¹à°à±à°¡à±", "lock",     "route", "/admin",    None, 99),
]


def upsert_subject(slug, name_en, name_te, sort_order):
    s = Subject.query.filter_by(slug=slug).first()
    if s:
        s.name_en, s.name_te, s.sort_order = name_en, name_te, sort_order
    else:
        s = Subject(slug=slug, name_en=name_en, name_te=name_te, sort_order=sort_order)
        db.session.add(s)
    db.session.flush()
    return s


def upsert_chapter(subject, chapter_num, title_en, title_te):
    c = Chapter.query.filter_by(subject_id=subject.id, chapter_num=chapter_num).first()
    if c:
        c.title_en, c.title_te = title_en, title_te
    else:
        c = Chapter(subject_id=subject.id, chapter_num=chapter_num,
                    title_en=title_en, title_te=title_te)
        db.session.add(c)
    db.session.flush()
    return c


def seed():
    app = create_app()
    with app.app_context():
        slug_to_subject = {}
        for slug, en, te, order in SUBJECTS:
            slug_to_subject[slug] = upsert_subject(slug, en, te, order)
        print(f"  subjects: {len(slug_to_subject)}")

        chapter_count = 0
        key_to_chapter = {}
        for slug, chapters in CHAPTERS.items():
            for num, en, te in chapters:
                key_to_chapter[(slug, num)] = upsert_chapter(slug_to_subject[slug], num, en, te)
                chapter_count += 1
        print(f"  chapters: {chapter_count}")

        q_added = 0
        for sslug, cnum, qen, qte, oen, ote, correct, eexp, texp, diff in QUESTIONS:
            subj = slug_to_subject[sslug]
            chap = key_to_chapter[(sslug, cnum)]
            existing = Question.query.filter_by(
                subject_id=subj.id, chapter_id=chap.id, question_en=qen
            ).first()
            if existing:
                continue
            db.session.add(Question(
                subject_id=subj.id, chapter_id=chap.id, source_type="chapter",
                difficulty=diff,
                question_en=qen, question_te=qte,
                options_en=oen, options_te=ote,
                correct_answer=correct,
                explanation_en=eexp, explanation_te=texp,
            ))
            q_added += 1
        print(f"  new questions: {q_added}")

        # Nav: parents first
        label_to_id = {}
        for surf, en, te, icon, atype, aref, parent, order in NAV_ITEMS:
            if parent is not None:
                continue
            n = NavItem.query.filter_by(surface=surf, label_en=en, parent_id=None).first()
            if n:
                n.label_te, n.icon, n.action_type, n.action_ref, n.sort_order = te, icon, atype, aref, order
            else:
                n = NavItem(surface=surf, label_en=en, label_te=te, icon=icon,
                            action_type=atype, action_ref=aref, sort_order=order)
                db.session.add(n)
            db.session.flush()
            label_to_id[en] = n.id
        # Then children
        for surf, en, te, icon, atype, aref, parent, order in NAV_ITEMS:
            if parent is None:
                continue
            pid = label_to_id.get(parent)
            n = NavItem.query.filter_by(surface=surf, label_en=en, parent_id=pid).first()
            if n:
                n.label_te, n.icon, n.action_type, n.action_ref, n.sort_order = te, icon, atype, aref, order
            else:
                db.session.add(NavItem(surface=surf, label_en=en, label_te=te, icon=icon,
                                       action_type=atype, action_ref=aref,
                                       parent_id=pid, sort_order=order))
        print(f"  nav items: {len(NAV_ITEMS)} (upserted)")

        db.session.commit()
        print("seed complete.")


if __name__ == "__main__":
    seed()
