"""Stage 1-2 tests: design-system shell + Learn -> Section -> Topic -> Notes -> Practice -> Explanation."""
import pytest
from app.db import db
from app.models import (
    Chapter, ChapterProgress, Exam, ExamPaper, ExamSection, ExamSyllabusItem,
    Note, Question, Subject, UserQuestionState,
)
from app.services.learn import display_title, render_note_html, strip_option_prefix

DEVICE = {"device_id": "t-device"}


@pytest.fixture()
def world(app):
    """History (2 chapters: notes + chapter MCQs), Polity (1 chapter, notes only), seeded exam."""
    hist = Subject(slug="indian_history", name_en="Indian History", name_te="భారత చరిత్ర", sort_order=1)
    pol = Subject(slug="indian_constitution", name_en="Indian Constitution", name_te="భారత రాజ్యాంగం", sort_order=2)
    db.session.add_all([hist, pol]); db.session.flush()
    c1 = Chapter(subject_id=hist.id, chapter_num=1, title_en="Chapter (recovered, sn_id=14)", title_te="x")
    c2 = Chapter(subject_id=hist.id, chapter_num=2, title_en="Vedic Civilisation", title_te="వైదిక నాగరికత")
    c3 = Chapter(subject_id=pol.id, chapter_num=1, title_en="Preamble", title_te="ప్రవేశిక")
    db.session.add_all([c1, c2, c3]); db.session.flush()
    notes = [
        Note(chapter_id=c2.id, section_num=1, heading_en="Rigveda", heading_te="ఋగ్వేదం",
             body_en="<p>Oldest Veda</p><script>alert(1)</script><p onclick=\"x()\" style=\"color:red\">Hymns</p>",
             body_te="<p>పురాతన వేదం</p>"),
        Note(chapter_id=c2.id, section_num=2, heading_en="Society", heading_te="సమాజం", body_en="<p>Tribes</p>", body_te=""),
        Note(chapter_id=c2.id, section_num=3, heading_en="Religion", heading_te="మతం", body_en="", body_te="<p>మతం గురించి</p>"),
        Note(chapter_id=c1.id, section_num=1, heading_en="Intro", heading_te="పరిచయం", body_en="<p>Intro</p>", body_te="<p>పరిచయం</p>"),
        Note(chapter_id=c3.id, section_num=1, heading_en="Preamble", heading_te="ప్రవేశిక", body_en="<p>We the people</p>", body_te="<p>మేము</p>"),
    ]
    qs = [
        # Telugu-only chapter MCQ with imported 'a) ' prefixes, like the real data
        Question(subject_id=hist.id, chapter_id=c2.id, source_type="chapter", difficulty="E",
                 question_en=None, question_te="గాయత్రీ మంత్రం ఏ వేదంలో ఉంది?",
                 options_en={}, options_te={"a": "a) ఋగ్వేదం", "b": "b) సామవేదం", "c": "c) యజుర్వేదం", "d": "d) అథర్వణవేదం"},
                 correct_answer="a", explanation_en=None, explanation_te="ఋగ్వేదంలో ఉంది."),
        Question(subject_id=hist.id, chapter_id=c2.id, source_type="chapter", difficulty="M",
                 question_en="Which Veda is a collection of melodies?", question_te="రాగాల సంకలనం ఏ వేదం?",
                 options_en={"a": "Rigveda", "b": "Samaveda"}, options_te={"a": "ఋగ్వేదం", "b": "సామవేదం"},
                 correct_answer="b", explanation_en="Samaveda.", explanation_te="సామవేదం."),
    ]
    db.session.add_all(notes + qs)
    exam = Exam(slug="appsc_group_2", name_en="APPSC Group 2", name_te="ఏపీపీఎస్‌సీ గ్రూప్ 2", active=True)
    db.session.add(exam); db.session.flush()
    p0 = ExamPaper(exam_id=exam.id, paper_num=0, name_en="Screening Test", name_te="స్క్రీనింగ్", total_marks=150, duration_min=150)
    p1 = ExamPaper(exam_id=exam.id, paper_num=1, name_en="Main Paper I", name_te="మెయిన్ I", total_marks=150, duration_min=150)
    db.session.add_all([p0, p1]); db.session.flush()
    s_hist = ExamSection(paper_id=p0.id, name_en="Indian History", name_te="భారత చరిత్ర", marks=30, sort_order=1)
    s_geo = ExamSection(paper_id=p0.id, name_en="Geography", name_te="భూగోళశాస్త్రం", marks=30, sort_order=2)
    s_pol = ExamSection(paper_id=p1.id, section_label="B", name_en="Indian Constitution", name_te="భారత రాజ్యాంగం", marks=75, sort_order=1)
    db.session.add_all([s_hist, s_geo, s_pol]); db.session.flush()
    db.session.add_all([
        ExamSyllabusItem(section_id=s_hist.id, chapter_id=c1.id, sort_order=0),
        ExamSyllabusItem(section_id=s_hist.id, chapter_id=c2.id, sort_order=1),
        ExamSyllabusItem(section_id=s_pol.id, chapter_id=c3.id, sort_order=0),
    ])
    db.session.commit()
    return dict(hist=hist, c1=c1, c2=c2, c3=c3, s_hist=s_hist.id, s_geo=s_geo.id, s_pol=s_pol.id, q=[q.id for q in qs])


@pytest.fixture()
def c(client):
    client.set_cookie("device_id", "t-device")
    return client


# ── unit helpers ───────────────────────────────────────────────────
def test_display_title_replaces_recovered_placeholder():
    class Ch: chapter_num = 3; title_en = "Chapter (recovered, sn_id=14)"; title_te = "x"
    assert display_title(Ch) == ("Chapter 3", "అధ్యాయం 3")


def test_strip_option_prefix():
    assert strip_option_prefix("a) ఋగ్వేదం") == "ఋగ్వేదం"
    assert strip_option_prefix("B. Samaveda") == "Samaveda"
    assert strip_option_prefix("Aryabhata") == "Aryabhata"   # a real word starting with a letter is untouched


def test_render_note_html_strips_active_content():
    out = render_note_html('<p style="x" onclick="y()">hi</p><script>alert(1)</script><style>p{}</style><a href="javascript:x()">l</a>')
    assert "script" not in out and "alert" not in out and "onclick" not in out and "style" not in out and "javascript:" not in out
    assert "hi" in out


# ── shell, language, nav ───────────────────────────────────────────
def test_shell_has_fixed_layout_assets_and_lang_default(c, world):
    html = c.get("/learn/").get_data(as_text=True)
    assert "ds.css" in html and "ds.js" in html
    assert 'data-lang="both"' in html
    assert 'class="bottomnav"' in html and 'aria-current="page"' in html


def test_language_cookie_is_applied_server_side(c, world):
    c.set_cookie("lang", "te")
    assert 'data-lang="te"' in c.get("/learn/").get_data(as_text=True)
    c.set_cookie("lang", "bogus")
    assert 'data-lang="both"' in c.get("/learn/").get_data(as_text=True)


def test_static_assets_exist(c):
    for f in ("ds.css", "ds.js", "fonts/noto-sans-telugu-telugu-400-normal.woff2", "fonts/plus-jakarta-sans-latin-400-normal.woff2"):
        assert c.get("/static/" + f).status_code == 200


# ── hub ────────────────────────────────────────────────────────────
def test_hub_lists_sections_and_marks_empty_ones_coming_soon(c, world):
    html = c.get("/learn/").get_data(as_text=True)
    assert f'/learn/section/{world["s_hist"]}' in html
    assert f'/learn/section/{world["s_pol"]}' in html
    assert f'/learn/section/{world["s_geo"]}' not in html        # no chapters: not a link
    assert "Coming soon" in html and 'aria-disabled="true"' in html
    assert "Prelims" in html and "Mains" in html


def test_hub_does_not_publish_unverified_exam_rules(c, world):
    html = c.get("/learn/").get_data(as_text=True)
    assert "150 min" not in html and "duration" not in html.lower() and "negative" not in html.lower()


def test_hub_falls_back_to_subject_list_without_exam(c, app):
    s = Subject(slug="x", name_en="Only", name_te="ఒకటి", sort_order=1); db.session.add(s); db.session.flush()
    db.session.add(Chapter(subject_id=s.id, chapter_num=1, title_en="A", title_te="ఎ")); db.session.commit()
    html = c.get("/learn/").get_data(as_text=True)
    assert "/learn/subject/x" in html and "not set up yet" in html


# ── section ────────────────────────────────────────────────────────
def test_section_lists_topics_with_counts_and_clean_titles(c, world):
    html = c.get(f'/learn/section/{world["s_hist"]}').get_data(as_text=True)
    assert "Vedic Civilisation" in html and "Chapter 1" in html and "recovered" not in html
    assert f'/learn/topic/{world["c2"].id}' in html
    assert "3 note sections" in html and "2 questions" in html


def test_section_404(c, world):
    assert c.get("/learn/section/9999").status_code == 404
    assert c.get("/learn/subject/nope").status_code == 404


# ── topic ──────────────────────────────────────────────────────────
def test_topic_hub_enables_real_tiles_and_disables_unbuilt_ones(c, world):
    html = c.get(f'/learn/topic/{world["c2"].id}').get_data(as_text=True)
    assert f'/learn/topic/{world["c2"].id}/notes' in html
    assert f'/learn/topic/{world["c2"].id}/practice?i=1&amp;new=1' in html
    assert html.count('aria-disabled="true"') >= 4              # PYQ, infographics, news, test
    # a chapter without MCQs: the MCQ tile is inert
    html = c.get(f'/learn/topic/{world["c3"].id}').get_data(as_text=True)
    assert "/practice" not in html


# ── notes ──────────────────────────────────────────────────────────
def test_notes_reader_sanitises_and_shows_both_languages(c, world):
    html = c.get(f'/learn/topic/{world["c2"].id}/notes?section=1').get_data(as_text=True)
    assert "Oldest Veda" in html and "పురాతన వేదం" in html
    assert "<script>alert" not in html and "onclick" not in html and "color:red" not in html
    assert "Section 1 of 3" in html


def test_notes_missing_language_falls_back_with_notice(c, world):
    cid = world["c2"].id
    html = c.get(f"/learn/topic/{cid}/notes?section=2").get_data(as_text=True)     # no Telugu body
    assert "Tribes" in html and "Telugu text for this section is not available" in html
    html = c.get(f"/learn/topic/{cid}/notes?section=3").get_data(as_text=True)     # no English body
    assert "మతం గురించి" in html and "English text for this section is not available" in html


def test_notes_prev_next_and_unknown_section(c, world):
    cid = world["c2"].id
    html = c.get(f"/learn/topic/{cid}/notes?section=2").get_data(as_text=True)
    assert "section=1" in html and "section=3" in html
    assert c.get(f"/learn/topic/{cid}/notes?section=99").status_code == 404


def test_notes_empty_chapter_has_message(c, app):
    s = Subject(slug="z", name_en="Z", name_te="జ"); db.session.add(s); db.session.flush()
    ch = Chapter(subject_id=s.id, chapter_num=1, title_en="Empty", title_te="ఖాళీ"); db.session.add(ch); db.session.commit()
    r = c.get(f"/learn/topic/{ch.id}/notes")
    assert r.status_code == 200 and "no notes for this topic" in r.get_data(as_text=True)


def test_section_progress_api_and_resume_card(c, world):
    cid = world["c2"].id
    assert c.post(f"/learn/api/topic/{cid}/section", json={"section": 99}).status_code == 400
    assert c.post(f"/learn/api/topic/{cid}/section", json={"section": "x"}).status_code == 400
    r = c.post(f"/learn/api/topic/{cid}/section", json={"section": 2})
    assert r.status_code == 200 and r.get_json()["current_section"] == 2
    prog = ChapterProgress.query.filter_by(device_id="t-device", chapter_id=cid).one()
    assert prog.status == "in_progress"
    hub = c.get("/learn/").get_data(as_text=True)
    assert 'data-testid="resume"' in hub and f"/learn/topic/{cid}/notes?section=2" in hub
    # reader reopens at the saved section
    assert "Section 2 of 3" in c.get(f"/learn/topic/{cid}/notes").get_data(as_text=True)


# ── practice + explanation ─────────────────────────────────────────
def test_practice_question_markup_and_no_answer_leak(c, world):
    html = c.get(f'/learn/topic/{world["c2"].id}/practice?i=1').get_data(as_text=True)
    assert "గాయత్రీ మంత్రం" in html and "ఋగ్వేదం" in html
    assert "a) ఋగ్వేదం" not in html                       # imported prefix removed; the badge shows the letter
    assert "data-correct" not in html                     # the key is only revealed by the API after answering
    assert "This question exists in Telugu only" in html  # English requested but missing
    assert "Q 1 / 2" in html


def test_practice_second_question_is_bilingual_and_last_flag(c, world):
    html = c.get(f'/learn/topic/{world["c2"].id}/practice?i=2').get_data(as_text=True)
    assert "Which Veda is a collection of melodies?" in html and "రాగాల సంకలనం" in html
    assert 'data-last="1"' in html


def test_practice_summary_and_empty_states(c, world):
    html = c.get(f'/learn/topic/{world["c2"].id}/practice?i=3').get_data(as_text=True)
    assert 'id="summary"' in html and 'data-stat="r"' in html
    html = c.get(f'/learn/topic/{world["c3"].id}/practice').get_data(as_text=True)
    assert "No questions for this topic yet" in html or "ఈ టాపిక్‌కు ఇంకా ప్రశ్నలు లేవు" in html


def test_answer_api_works_for_new_ui_and_tracks_state(c, world):
    qid = world["q"][0]
    r = c.post("/api/answer", json={"question_id": qid, "chosen": "b", "confidence": 0})
    d = r.get_json()
    assert r.status_code == 200 and d["correct"] is False and d["correct_answer"] == "a"
    st = UserQuestionState.query.filter_by(device_id="t-device", question_id=qid).one()
    assert st.seen_count == 1 and st.wrong_count == 1


def test_explanation_present_in_page_but_hidden_until_answered(c, world):
    html = c.get(f'/learn/topic/{world["c2"].id}/practice?i=1').get_data(as_text=True)
    assert 'id="expl" hidden' in html and "ఋగ్వేదంలో ఉంది." in html
    assert "/learn/topic/%d/notes" % world["c2"].id in html     # link from explanation to the topic notes


# ── regression: existing routes untouched ──────────────────────────
def test_old_routes_still_work(c, world):
    for url in ("/subjects", "/subject/indian_history", "/practice/indian_history", "/notes/indian_history", "/settings", "/healthz"):
        # 200, or a redirect on older revisions of a route; never 404/500
        assert c.get(url).status_code in (200, 301, 302), url


# ── review fixes ───────────────────────────────────────────────────
def test_chapter_practice_excludes_pyq_and_practice_rows(c, world):
    c2 = world["c2"]
    db.session.add(Question(subject_id=world["hist"].id, chapter_id=c2.id, source_type="pyq", pyq_year="2019",
                            question_en="PYQ?", question_te="", options_en={"a": "x", "b": "y"}, options_te={},
                            correct_answer="a"))
    db.session.commit()
    html = c.get(f"/learn/topic/{c2.id}/practice?i=1&new=1").get_data(as_text=True)
    assert "PYQ?" not in html
    assert "Previous paper" not in html


def test_pyq_view_is_labelled_source_not_verified(app, world):
    from app.services.learn import question_view
    q = Question(subject_id=world["hist"].id, source_type="pyq", pyq_year="2019", pyq_paper="12-03-2019 Shift 2",
                 question_en="Q", options_en={"a": "x"}, options_te={}, correct_answer="a")
    v = question_view(q)
    assert v["is_pyq"] and v["pyq_year"] == "2019"
    assert question_view(Question(subject_id=1, source_type="chapter", question_en="Q", options_en={"a": "x"},
                                  options_te={}, correct_answer="a"))["is_pyq"] is False


def test_topic_back_link_uses_only_safe_local_targets(c, world):
    cid = world["c2"].id
    ok = c.get(f"/learn/topic/{cid}?back=/learn/section/{world['s_hist']}").get_data(as_text=True)
    assert f'href="/learn/section/{world["s_hist"]}"' in ok
    for bad in ("https://evil.example/", "//evil.example", "/learn/section/1/../../x", "javascript:alert(1)"):
        html = c.get(f"/learn/topic/{cid}", query_string={"back": bad}).get_data(as_text=True)
        assert "evil.example" not in html and "javascript:alert" not in html
        assert "/learn/subject/indian_history" in html


def test_section_page_links_topics_with_back_param(c, world):
    html = c.get(f"/learn/section/{world['s_hist']}").get_data(as_text=True)
    assert f"/learn/topic/{world['c2'].id}?back=" in html


def test_notes_jump_options_carry_both_languages_and_disabled_nav_is_named(c, world):
    html = c.get(f"/learn/topic/{world['c2'].id}/notes?section=1").get_data(as_text=True)
    assert 'data-en="Rigveda"' in html and 'data-te="ఋగ్వేదం"' in html
    assert 'aria-disabled="true" aria-label=' in html   # first section: prev is inert but named


def test_js_keyboard_tabs_wrap_and_language_relabel_present(client):
    js = client.get("/static/ds.js").get_data(as_text=True)
    assert '"Home"' in js and '"End"' in js and "relabel(v)" in js
    assert "msgOk" in js and 'announce(res.correct ? "Correct"' not in js


def test_bi_macro_renders_once_when_languages_identical(app):
    from flask import render_template_string
    with app.test_request_context("/"):
        same = render_template_string('{% import "ds/_c.html" as c %}{{ c.bi("Vedic", "Vedic") }}')
        diff = render_template_string('{% import "ds/_c.html" as c %}{{ c.bi("Vedic", "వేద") }}')
    assert same.count("Vedic") == 1 and 'class="en keep"' in same
    assert "Vedic" in diff and "వేద" in diff
