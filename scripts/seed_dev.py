"""
Seed dev data — all 11 v3 subjects, sample chapters, sample bilingual
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


# All 11 subjects per REBUILD_PLAN_v3.md §4
SUBJECTS = [
    ("indian_history",      "Indian History",       "భారత చరిత్ర",                  1),
    ("indian_constitution", "Indian Constitution",  "భారత రాజ్యాంగం",                2),
    ("ap_history",          "AP Social & Cultural History", "ఆంధ్రప్రదేశ్ చరిత్ర",   3),
    ("indian_geography",    "Indian Geography",     "భారత భూగోళశాస్త్రం",            4),
    ("ap_geography",        "AP Geography",         "ఆంధ్రప్రదేశ్ భూగోళశాస్త్రం",     5),
    ("indian_economy",      "Indian Economy",       "భారత ఆర్థిక వ్యవస్థ",           6),
    ("ap_economy",          "AP Economy",           "ఆంధ్రప్రదేశ్ ఆర్థిక వ్యవస్థ",    7),
    ("science_technology",  "Science & Technology", "సైన్స్ & సాంకేతికత",            8),
    ("indian_society",      "Indian Society",       "భారత సమాజం",                   9),
    ("mental_ability",      "Mental Ability",       "మానసిక సామర్థ్యం",             10),
    ("current_affairs",     "Current Affairs",      "ప్రస్తుత వ్యవహారాలు",          11),
]

# subject_slug -> [(chapter_num, title_en, title_te)]
CHAPTERS = {
    "indian_history": [
        (1, "Indus Valley Civilization", "సింధు నాగరికత"),
        (2, "Mauryan Empire", "మౌర్య సామ్రాజ్యం"),
    ],
    "indian_constitution": [
        (1, "Preamble", "ప్రవేశిక"),
        (2, "Fundamental Rights", "ప్రాథమిక హక్కులు"),
        (3, "Directive Principles", "ఆదేశక సూత్రాలు"),
    ],
    "ap_history": [
        (1, "Satavahanas & Ikshvakus", "శాతవాహనులు & ఇక్ష్వాకులు"),
    ],
    "indian_geography": [
        (1, "Location & Physiography", "స్థానం & భౌతిక లక్షణాలు"),
    ],
    "ap_geography": [
        (1, "Location & Physical Setting of AP", "ఆంధ్రప్రదేశ్ స్థానం"),
    ],
    "indian_economy": [
        (1, "National Income", "జాతీయ ఆదాయం"),
    ],
    "ap_economy": [
        (1, "AP GSDP & Sectoral Contribution", "ఆంధ్రప్రదేశ్ GSDP"),
    ],
    "science_technology": [
        (1, "Space Technology", "అంతరిక్ష సాంకేతికత"),
    ],
    "indian_society": [
        (1, "Caste, Class & Family", "కులం, వర్గం, కుటుంబం"),
    ],
    "mental_ability": [
        (1, "Number Series", "సంఖ్యా శ్రేణి"),
    ],
    "current_affairs": [],  # rolling, no chapters
}

# (subject_slug, chapter_num, qen, qte, oen, ote, correct, eexp, texp, diff)
QUESTIONS = [
    (
        "indian_constitution", 2,
        "In which part of the Indian Constitution are the Fundamental Rights enshrined?",
        "భారత రాజ్యాంగంలో ప్రాథమిక హక్కులు ఏ భాగంలో ఉన్నాయి?",
        {"a": "Part II", "b": "Part III", "c": "Part IV", "d": "Part V"},
        {"a": "భాగం II", "b": "భాగం III", "c": "భాగం IV", "d": "భాగం V"},
        "b",
        "Articles 12 to 35 in Part III of the Constitution guarantee six categories of fundamental rights.",
        "రాజ్యాంగంలోని భాగం IIIలోని అధికరణలు 12 నుండి 35 వరకు ఆరు రకాల ప్రాథమిక హక్కులను హామీ ఇస్తాయి.",
        "M",
    ),
    (
        "indian_constitution", 1,
        "The Preamble of the Indian Constitution begins with which words?",
        "భారత రాజ్యాంగ ప్రవేశిక ఏ పదాలతో మొదలవుతుంది?",
        {"a": "We the People", "b": "India that is Bharat", "c": "Sovereign Socialist", "d": "Justice Liberty"},
        {"a": "మేము భారత ప్రజలము", "b": "ఇండియా అనగా భారత్", "c": "సర్వసత్తాక సామ్యవాద", "d": "న్యాయము స్వేచ్ఛ"},
        "a",
        "The Preamble opens with the words 'We, the People of India' — emphasising the source of authority is the people.",
        "ప్రవేశిక 'మేము భారత ప్రజలము' అనే పదాలతో మొదలవుతుంది — అధికారం ప్రజల నుండే వస్తుందని తెలియజేస్తుంది.",
        "E",
    ),
    (
        "indian_history", 1,
        "Which Harappan site was the largest in terms of area?",
        "విస్తీర్ణం ప్రకారం అతిపెద్ద హరప్పా కేంద్రం ఏది?",
        {"a": "Harappa", "b": "Mohenjo-daro", "c": "Rakhigarhi", "d": "Lothal"},
        {"a": "హరప్పా", "b": "మొహెంజోదారో", "c": "రాఖీగఢీ", "d": "లోథాల్"},
        "c",
        "Rakhigarhi in Haryana is now recognised as the largest Harappan site discovered, surpassing Mohenjo-daro in area.",
        "హర్యానాలోని రాఖీగఢీ ఇప్పటివరకు కనుగొనబడిన అతిపెద్ద హరప్పా కేంద్రంగా గుర్తించబడింది, మొహెంజోదారో కంటే ఎక్కువ విస్తీర్ణం కలిగి ఉంది.",
        "H",
    ),
    (
        "indian_geography", 1,
        "Which is the southernmost point of mainland India?",
        "భారత ప్రధాన భూభాగంలో అత్యంత దక్షిణ బిందువు ఏది?",
        {"a": "Indira Point", "b": "Kanyakumari", "c": "Rameswaram", "d": "Trivandrum"},
        {"a": "ఇందిరా పాయింట్", "b": "కన్యాకుమారి", "c": "రామేశ్వరం", "d": "తిరువనంతపురం"},
        "b",
        "Kanyakumari is the southernmost point of the Indian mainland. Indira Point in the Nicobars is southernmost overall but not mainland.",
        "కన్యాకుమారి భారత ప్రధాన భూభాగంలోని అత్యంత దక్షిణ బిందువు. నికోబార్‌లోని ఇందిరా పాయింట్ మొత్తం భూభాగంలో అత్యంత దక్షిణం, కానీ ప్రధాన భూభాగం కాదు.",
        "M",
    ),
    (
        "ap_geography", 1,
        "Andhra Pradesh shares its longest land border with which state?",
        "ఆంధ్రప్రదేశ్ ఏ రాష్ట్రంతో అత్యంత పొడవైన భూ సరిహద్దును పంచుకుంటుంది?",
        {"a": "Karnataka", "b": "Tamil Nadu", "c": "Telangana", "d": "Odisha"},
        {"a": "కర్ణాటక", "b": "తమిళనాడు", "c": "తెలంగాణ", "d": "ఒడిశా"},
        "c",
        "After the 2014 bifurcation, Andhra Pradesh shares its longest land border with the newly formed state of Telangana.",
        "2014 విభజన తర్వాత, ఆంధ్రప్రదేశ్ కొత్తగా ఏర్పడిన తెలంగాణ రాష్ట్రంతో అత్యంత పొడవైన భూ సరిహద్దును పంచుకుంటుంది.",
        "E",
    ),
]


# (surface, label_en, label_te, icon, action_type, action_ref, parent_label, sort_order)
NAV_ITEMS = [
    ("menu", "Home",     "హోమ్",     "home",     "route", "/",         None,       0),
    ("menu", "Subjects", "విషయాలు", "books",    None,    None,        None,      10),
    # Subjects (children of "Subjects" parent) — all 11
    ("menu", "Indian History",       "భారత చరిత్ర",            None, "subject", "indian_history",       "Subjects",  1),
    ("menu", "Indian Constitution",  "భారత రాజ్యాంగం",          None, "subject", "indian_constitution",  "Subjects",  2),
    ("menu", "AP History",           "ఆంధ్రప్రదేశ్ చరిత్ర",     None, "subject", "ap_history",           "Subjects",  3),
    ("menu", "Indian Geography",     "భారత భూగోళశాస్త్రం",      None, "subject", "indian_geography",     "Subjects",  4),
    ("menu", "AP Geography",         "ఆంధ్రప్రదేశ్ భూగోళశాస్త్రం", None, "subject", "ap_geography",         "Subjects",  5),
    ("menu", "Indian Economy",       "భారత ఆర్థిక వ్యవస్థ",     None, "subject", "indian_economy",       "Subjects",  6),
    ("menu", "AP Economy",           "ఆంధ్రప్రదేశ్ ఆర్థిక వ్యవస్థ", None, "subject", "ap_economy",          "Subjects",  7),
    ("menu", "Science & Technology", "సైన్స్ & సాంకేతికత",     None, "subject", "science_technology",   "Subjects",  8),
    ("menu", "Indian Society",       "భారత సమాజం",             None, "subject", "indian_society",       "Subjects",  9),
    ("menu", "Mental Ability",       "మానసిక సామర్థ్యం",       None, "subject", "mental_ability",       "Subjects", 10),
    ("menu", "Current Affairs",      "ప్రస్తుత వ్యవహారాలు",     None, "subject", "current_affairs",      "Subjects", 11),
    # Bottom rail
    ("menu", "Settings", "అమరికలు",   "settings", "route", "/settings", None, 90),
    ("menu", "Admin",    "నిర్వాహకుడు", "lock",     "route", "/admin",    None, 99),
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
