"""Canonical AP History structure: five official APPSC units, 31 internal preparation chapters, and three supplementary
reference chapters. Subject -> Unit -> Chapter -> Subtopic.

* The five units are the official top level. The 31 chapters are *our* preparation structure, not 31 official syllabus lines.
* Slugs are stable identifiers: ``u<unit>-c<NN>-<english-slug>``. They are fixed here and never regenerated from a title, so a
  later title edit cannot change a published slug. ``seed`` only inserts missing rows; it never updates an existing one.
* Local source chapters 4, 14 and 19 are *not* among the 31: they are the supplementary reference chapters at the bottom.
* This module does not touch notes, questions or source files.
"""
from ..db import db
from ..models import Subject, SyllabusChapter, SyllabusSubtopic, SyllabusUnit

SUBJECT_SLUG = "ap_history"

# (unit_num, slug, English, Telugu)
UNITS = [
    (1, "u1-ancient-early-medieval-andhra", "Ancient and Early-Medieval Andhra", "ప్రాచీన మరియు తొలి మధ్యయుగ ఆంధ్ర"),
    (2, "u2-andhradesa-11th-16th-centuries", "Andhradesa from the 11th to 16th Centuries", "11వ నుండి 16వ శతాబ్దాల వరకు ఆంధ్రదేశం"),
    (3, "u3-colonial-nationalist-andhra", "Colonial and Nationalist Andhra", "వలస పాలన మరియు జాతీయోద్యమ ఆంధ్ర"),
    (4, "u4-andhra-movement-andhra-state", "Andhra Movement and Andhra State", "ఆంధ్రోద్యమం మరియు ఆంధ్ర రాష్ట్రం"),
    (5, "u5-formation-development-andhra-pradesh", "Formation and Development of Andhra Pradesh", "ఆంధ్రప్రదేశ్ ఆవిర్భావం మరియు అభివృద్ధి"),
]

# (unit_num, chapter_num, slug, English, Telugu, classification)
CHAPTERS = [
    (1, 1, "u1-c01-region-people-sources", "Andhra Region, People and Historical Sources", "ఆంధ్ర ప్రాంతం, ప్రజలు మరియు చారిత్రక ఆధారాలు", "bridge"),
    (1, 2, "u1-c02-prehistoric-cultures", "Prehistoric Cultures of Andhra", "ఆంధ్రలో చరిత్రపూర్వ సంస్కృతులు", "direct"),
    (1, 3, "u1-c03-pre-satavahana-andhra", "Pre-Satavahana Andhra", "శాతవాహనులకు పూర్వపు ఆంధ్ర", "bridge"),
    (1, 4, "u1-c04-satavahanas", "Satavahanas", "శాతవాహనులు", "direct"),
    (1, 5, "u1-c05-ikshvakus", "Ikshvakus", "ఇక్ష్వాకులు", "direct"),
    (1, 6, "u1-c06-post-ikshvaku-minor-dynasties", "Post-Ikshvaku Minor Dynasties", "ఇక్ష్వాకుల అనంతరం చిన్న రాజవంశాలు", "bridge"),
    (1, 7, "u1-c07-vishnukundins", "Vishnukundins", "విష్ణుకుండినులు", "direct"),
    (1, 8, "u1-c08-eastern-chalukyas-andhra-cholas", "Eastern Chalukyas of Vengi and Andhra Cholas", "వేంగి తూర్పు చాళుక్యులు మరియు ఆంధ్ర చోళులు", "direct"),
    (2, 9, "u2-c09-kakatiyas", "Kakatiyas", "కాకతీయులు", "direct"),
    (2, 10, "u2-c10-musunuri-reddy-velama", "Musunuri Nayakas, Reddy Kingdoms and Velama Chiefs", "ముసునూరి నాయకులు, రెడ్డి రాజ్యాలు మరియు వెలమ నాయకులు", "direct"),
    (2, 11, "u2-c11-vijayanagara-andhra", "Vijayanagara and Andhra", "విజయనగరం మరియు ఆంధ్ర", "direct"),
    (2, 12, "u2-c12-gajapatis-bahmanis-regional-powers", "Gajapatis, Bahmanis and Other Regional Powers", "గజపతులు, బహమనీలు మరియు ఇతర ప్రాంతీయ శక్తులు", "direct"),
    (2, 13, "u2-c13-qutb-shahis", "Qutb Shahis and Sixteenth-Century Andhra", "కుతుబ్‌షాహీలు మరియు పదహారో శతాబ్దపు ఆంధ్ర", "direct"),
    (2, 14, "u2-c14-thematic-history-11th-16th-c", "Thematic History of Andhradesa, 11th–16th Centuries", "ఆంధ్రదేశ చరిత్ర: అంశాల వారీ అవలోకనం (11–16 శతాబ్దాలు)", "thematic"),
    (3, 15, "u3-c15-europeans-company-rule", "Europeans, Trading Centres and Company Rule", "యూరోపియన్లు, వ్యాపార కేంద్రాలు మరియు కంపెనీ పాలన", "direct"),
    (3, 16, "u3-c16-british-rule-revolt-1857", "Establishment of British Rule and the Impact of 1857", "బ్రిటిష్ పాలన స్థాపన మరియు 1857 ప్రభావం", "direct"),
    (3, 17, "u3-c17-socio-cultural-awakening", "Socio-Cultural Awakening", "సామాజిక-సాంస్కృతిక చైతన్యం", "direct"),
    (3, 18, "u3-c18-justice-party-self-respect", "Justice Party and Self-Respect Movement", "జస్టిస్ పార్టీ మరియు ఆత్మగౌరవ ఉద్యమం", "direct"),
    (3, 19, "u3-c19-nationalist-movement-1885-1947", "Nationalist Movement in Andhra, 1885–1947", "ఆంధ్రలో జాతీయోద్యమం (1885–1947)", "direct"),
    (3, 20, "u3-c20-socialists-communists-kisan", "Socialists, Communists, Anti-Zamindari and Kisan Movements", "సోషలిస్టులు, కమ్యూనిస్టులు, జమీందారీ వ్యతిరేక మరియు కిసాన్ ఉద్యమాలు", "direct"),
    (3, 21, "u3-c21-poetry-literature-nataka-samasthalu", "Nationalist Poetry, Revolutionary Literature and Nataka Samasthalu", "జాతీయ కవిత్వం, విప్లవ సాహిత్యం మరియు నాటక సమాజాలు", "direct"),
    (3, 22, "u3-c22-womens-participation", "Women's Participation", "మహిళల భాగస్వామ్యం", "direct"),
    (4, 23, "u4-c23-andhra-movement-origin-growth", "Origin and Growth of the Andhra Movement", "ఆంధ్రోద్యమ ఆవిర్భావం మరియు వికాసం", "direct"),
    (4, 24, "u4-c24-andhra-mahasabhas-leaders", "Andhra Mahasabhas and Prominent Leaders", "ఆంధ్ర మహాసభలు మరియు ప్రముఖ నాయకులు", "direct"),
    (4, 25, "u4-c25-press-library-movement", "Press, Newspapers and the Library Movement", "పత్రికలు, వార్తాపత్రికలు మరియు గ్రంథాలయోద్యమం", "direct"),
    (4, 26, "u4-c26-folk-tribal-culture", "Folk and Tribal Culture", "జానపద మరియు గిరిజన సంస్కృతి", "direct"),
    (4, 27, "u4-c27-formation-andhra-state-1953", "Formation of Andhra State, 1953", "ఆంధ్ర రాష్ట్ర ఏర్పాటు (1953)", "direct"),
    (5, 28, "u5-c28-visalandhra-movement-mahasabha", "Visalandhra Movement and Visalandhra Mahasabha", "విశాలాంధ్ర ఉద్యమం మరియు విశాలాంధ్ర మహాసభ", "direct"),
    (5, 29, "u5-c29-states-reorganisation-commission", "States Reorganisation Commission", "రాష్ట్రాల పునర్వ్యవస్థీకరణ సంఘం", "direct"),
    (5, 30, "u5-c30-gentlemens-agreement-formation-ap", "Gentlemen's Agreement and Formation of Andhra Pradesh", "పెద్దమనుషుల ఒప్పందం మరియు ఆంధ్రప్రదేశ్ ఏర్పాటు", "direct"),
    (5, 31, "u5-c31-social-cultural-events-1956-2014", "Important Social and Cultural Events, 1956–2014", "ముఖ్యమైన సామాజిక మరియు సాంస్కృతిక సంఘటనలు (1956–2014)", "direct"),
]

# Supplementary reference chapters: outside the 31, no unit, no chapter number. (slug, English, Telugu, supplementary_type, local source chapter)
SUPPLEMENTARY = [
    ("supp-dynasties-overview", "Overview of Andhra Dynasties (Reference)", "ఆంధ్ర రాజవంశాల అవలోకనం (సూచిక)", "supplementary_cross_cutting", 4),
    ("supp-asaf-jahis-hyderabad-state", "Asaf Jahis and Hyderabad State (Reference)", "అసఫ్ జాహీలు మరియు హైదరాబాద్ సంస్థానం (సూచిక)", "supplementary_outside_direct_syllabus", 14),
    ("supp-post-2014-andhra-pradesh", "Bifurcation and Post-2014 Andhra Pradesh (Current Context)", "విభజన మరియు 2014 తర్వాత ఆంధ్రప్రదేశ్ (ప్రస్తుత సందర్భం)", "supplementary_post_syllabus", 19),
]
SUPPLEMENTARY_SOURCE_CHAPTER = {slug: src for slug, _e, _t, _k, src in SUPPLEMENTARY}


def seed(session=None, subject_slug=SUBJECT_SLUG, apply=True):
    """Insert the units and chapters that are missing; never update or delete. Returns a report dict.
    With ``apply=False`` nothing is written (preview)."""
    session = session or db.session
    subject = Subject.query.filter_by(slug=subject_slug).first()
    if subject is None:
        raise LookupError(f"subject {subject_slug!r} does not exist; nothing was seeded")
    report = {"units_added": 0, "chapters_added": 0, "supplementary_added": 0, "units_existing": 0, "chapters_existing": 0}
    units = {}
    for num, slug, en, te in UNITS:
        row = SyllabusUnit.query.filter_by(slug=slug).first()
        if row is None:
            report["units_added"] += 1
            row = SyllabusUnit(subject_id=subject.id, unit_num=num, slug=slug, title_en=en, title_te=te, sort_order=num)
            if apply:
                session.add(row)
        else:
            report["units_existing"] += 1
        units[num] = row
    if apply:
        session.flush()
    for unit_num, num, slug, en, te, cls in CHAPTERS:
        if SyllabusChapter.query.filter_by(slug=slug).first():
            report["chapters_existing"] += 1
            continue
        report["chapters_added"] += 1
        if apply:
            session.add(SyllabusChapter(subject_id=subject.id, unit_id=units[unit_num].id, chapter_num=num, slug=slug,
                                        title_en=en, title_te=te, classification=cls, sort_order=num))
    for i, (slug, en, te, kind, _src) in enumerate(SUPPLEMENTARY):
        if SyllabusChapter.query.filter_by(slug=slug).first():
            report["chapters_existing"] += 1
            continue
        report["supplementary_added"] += 1
        if apply:
            session.add(SyllabusChapter(subject_id=subject.id, unit_id=None, chapter_num=None, slug=slug, title_en=en, title_te=te,
                                        classification="supplementary", supplementary_type=kind, sort_order=100 + i))
    if apply:
        session.commit()
    return report


def seed_subtopics(subtopics, session=None, apply=True):
    """Insert missing subtopics from ``subtopics`` ({chapter_slug: [(slug, English, Telugu), ...]}). Not part of the first phase."""
    session = session or db.session
    added = 0
    for chapter_slug, items in subtopics.items():
        ch = SyllabusChapter.query.filter_by(slug=chapter_slug).first()
        if ch is None:
            raise LookupError(f"chapter {chapter_slug!r} is not seeded")
        for i, (slug, en, te) in enumerate(items, 1):
            if SyllabusSubtopic.query.filter_by(slug=slug).first():
                continue
            added += 1
            if apply:
                session.add(SyllabusSubtopic(chapter_id=ch.id, slug=slug, subtopic_en=en, subtopic_te=te, sort_order=i))
    if apply:
        session.commit()
    return added
