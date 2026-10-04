"""Interface text for the design-system templates (ds/*).

Every entry is (English, Telugu). Templates call ``t('key', n=3)`` which renders a bilingual
span; CSS (``html[data-lang]``) shows Telugu, English or both. Telugu is a DRAFT for a fluent
reader to review. Content from the database (notes, questions) is never put here.
"""
from markupsafe import Markup, escape

UI = {
    "app.name": ("APPSC Prep", "APPSC ప్రిపరేషన్"),
    "nav.main": ("Main navigation", "ప్రధాన నావిగేషన్"),
    "nav.home": ("Home", "హోమ్"), "nav.learn": ("Learn", "నేర్చుకోండి"), "nav.practice": ("Practice", "ప్రాక్టీస్"),
    "nav.tests": ("Tests", "పరీక్షలు"), "nav.progress": ("Progress", "పురోగతి"),
    "lang.label": ("Language", "భాష"), "lang.te": ("Telugu", "తెలుగు"), "lang.en": ("English", "ఇంగ్లీష్"),
    "lang.both": ("Telugu and English", "తెలుగు మరియు ఇంగ్లీష్"), "lang.changed": ("Language changed", "భాష మార్చబడింది"),
    "common.prelims": ("Prelims", "ప్రిలిమ్స్"), "common.mains": ("Mains", "మెయిన్స్"), "common.exam": ("Exam", "పరీక్ష"),
    "common.soon": ("Coming soon", "త్వరలో"), "common.available": ("Available", "అందుబాటులో ఉంది"),
    "common.back": ("Back", "వెనుకకు"), "common.marks": ("{n} marks", "{n} మార్కులు"),
    "common.questions": ("{n} questions", "{n} ప్రశ్నలు"), "common.sections": ("{n} sections", "{n} విభాగాలు"),
    "common.chapters": ("{n} chapters", "{n} అధ్యాయాలు"), "common.chapter": ("Chapter {n}", "అధ్యాయం {n}"),
    "common.empty": ("Nothing here yet", "ఇక్కడ ఇంకా ఏమీ లేదు"),
    # learn hub
    "learn.title": ("Learn", "నేర్చుకోండి"),
    "learn.prelims_note": ("Screening test, 150 marks (30 per subject)", "స్క్రీనింగ్ టెస్ట్, 150 మార్కులు (ఒక్కో సబ్జెక్టుకు 30)"),
    "learn.mains_note": ("Main examination papers", "మెయిన్ పరీక్ష పేపర్లు"),
    "learn.no_content": ("Content not added yet", "కంటెంట్ ఇంకా జోడించలేదు"),
    "learn.continue": ("CONTINUE", "కొనసాగించండి"), "learn.resume": ("Resume", "కొనసాగించు"),
    "learn.no_exam": ("The exam syllabus is not set up yet. Showing all subjects.", "పరీక్ష సిలబస్ ఇంకా సిద్ధం కాలేదు. అన్ని సబ్జెక్టులు చూపబడుతున్నాయి."),
    "learn.all_subjects": ("All subjects", "అన్ని సబ్జెక్టులు"),
    "learn.content_counts": ("{c} chapters · {q} questions", "{c} అధ్యాయాలు · {q} ప్రశ్నలు"),
    # section page
    "section.topics": ("Topics", "టాపిక్‌లు"), "section.no_topics": ("No topics in this section yet.", "ఈ విభాగంలో ఇంకా టాపిక్‌లు లేవు."),
    "section.topic_line": ("{n} note sections · {q} questions", "{n} నోట్స్ విభాగాలు · {q} ప్రశ్నలు"),
    "status.not_started": ("Not started", "ప్రారంభించలేదు"), "status.in_progress": ("In progress", "కొనసాగుతోంది"),
    "status.completed": ("Completed", "పూర్తైంది"),
    # topic hub
    "topic.notes": ("Notes", "నోట్స్"), "topic.mcqs": ("MCQs", "ప్రశ్నలు"), "topic.pyq": ("Previous papers", "గత ప్రశ్నపత్రాలు"),
    "topic.infog": ("Infographics", "ఇన్ఫోగ్రాఫిక్స్"), "topic.news": ("Related news", "సంబంధిత వార్తలు"),
    "topic.test": ("Topic test", "టాపిక్ టెస్ట్"), "topic.mark_done": ("Mark chapter complete", "అధ్యాయం పూర్తైనట్లు గుర్తించు"),
    "topic.done": ("Chapter marked complete", "అధ్యాయం పూర్తైనట్లు గుర్తించబడింది"),
    "topic.no_mcqs": ("No questions for this topic yet", "ఈ టాపిక్‌కు ఇంకా ప్రశ్నలు లేవు"),
    # notes
    "notes.section_of": ("Section {a} of {b}", "విభాగం {a} / {b}"), "notes.prev": ("Previous section", "మునుపటి విభాగం"),
    "notes.next": ("Next section", "తదుపరి విభాగం"), "notes.practise": ("Practise this topic", "ఈ టాపిక్ ప్రాక్టీస్ చేయండి"),
    "notes.no_te": ("Telugu text for this section is not available yet. English is shown.", "ఈ విభాగానికి తెలుగు పాఠ్యం ఇంకా లేదు. ఇంగ్లీష్ చూపబడుతోంది."),
    "notes.no_en": ("English text for this section is not available yet. Telugu is shown.", "ఈ విభాగానికి ఇంగ్లీష్ పాఠ్యం ఇంకా లేదు. తెలుగు చూపబడుతోంది."),
    "notes.empty": ("There are no notes for this topic yet.", "ఈ టాపిక్‌కు ఇంకా నోట్స్ లేవు."),
    "notes.sections": ("Sections", "విభాగాలు"), "notes.jump": ("Jump to section", "విభాగానికి వెళ్ళండి"),
    # practice
    "prac.q": ("Q {a} / {b}", "ప్ర {a} / {b}"), "prac.choose": ("Choose one answer", "ఒక సమాధానం ఎంచుకోండి"),
    "prac.skip": ("Skip", "దాటవేయి"), "prac.next": ("Next", "తదుపరి"), "prac.finish": ("Finish", "ముగించు"),
    "prac.correct": ("Correct", "సరైనది"), "prac.correct_ans": ("Correct answer", "సరైన సమాధానం"), "prac.yours": ("Your answer", "మీ సమాధానం"),
    "prac.expl": ("EXPLANATION", "వివరణ"), "prac.no_expl": ("No explanation has been added for this question yet.", "ఈ ప్రశ్నకు వివరణ ఇంకా జోడించలేదు."),
    "prac.open_notes": ("Read the topic notes", "టాపిక్ నోట్స్ చదవండి"),
    "prac.end": ("End session", "సెషన్ ముగించు"), "prac.progress": ("Session progress", "సెషన్ పురోగతి"),
    "prac.summary": ("Session summary", "సెషన్ సారాంశం"), "prac.right": ("Correct", "సరైనవి"), "prac.wrong": ("Wrong", "తప్పులు"),
    "prac.skipped": ("Skipped", "దాటవేసినవి"), "prac.again": ("Practise again", "మళ్ళీ ప్రాక్టీస్ చేయండి"),
    "prac.back_topic": ("Back to topic", "టాపిక్‌కు తిరిగి"), "prac.save_failed": ("Could not save the answer. Check your connection.", "సమాధానం సేవ్ కాలేదు. కనెక్షన్ చూడండి."),
    "common.unavailable": ("not available", "అందుబాటులో లేదు"),
    "prac.src.pyq": ("Previous paper", "గత ప్రశ్నపత్రం"), "prac.src.unverified": ("Source not verified", "మూలం ధృవీకరించబడలేదు"),
    "prac.incorrect": ("Incorrect", "తప్పు"), "topic.done_err": ("Could not save. Check your connection and try again.", "సేవ్ చేయలేకపోయాం. కనెక్షన్ చూసి మళ్లీ ప్రయత్నించండి."),
    "prac.src.chapter": ("Chapter question", "చాప్టర్ ప్రశ్న"),
    "prac.diff.E": ("Easy", "సులభం"), "prac.diff.M": ("Medium", "మధ్యస్థం"), "prac.diff.H": ("Hard", "కఠినం"),
    "prac.lang_fallback_te": ("This question exists in Telugu only.", "ఈ ప్రశ్న తెలుగులో మాత్రమే ఉంది."),
    "prac.lang_fallback_en": ("This question exists in English only.", "ఈ ప్రశ్న ఇంగ్లీష్‌లో మాత్రమే ఉంది."),
}


def entry(key: str):
    if key not in UI:
        return (key, key)
    return UI[key]


def t(key: str, **vars) -> Markup:
    """Bilingual span for an interface string."""
    en, te = entry(key)
    en = str(escape(en.format(**vars) if vars else en))
    te = str(escape(te.format(**vars) if vars else te))
    return Markup(f'<span class="bi"><span class="en" lang="en">{en}</span><span class="te" lang="te">{te}</span></span>')


def tl(key: str, **vars) -> str:
    """Plain 'English / Telugu' text for attributes such as aria-label."""
    en, te = entry(key)
    if vars:
        en, te = en.format(**vars), te.format(**vars)
    return f"{en} / {te}"
