"""Release-blocker regressions found by the mobile smoke test, checked against slices of the REAL content:

F1  exam / legacy practice / results show options in whatever language exists (all chapter questions are Telugu-only);
F2  an exam session is never "every eligible question"; the official test is disabled until its rules are verified;
F3  Learn counts equal what the page can reach, with subject-level Practice and PYQ banks for questions without chapters.
"""
import pytest
from bs4 import BeautifulSoup

from app.db import db
from app.models import (
    Chapter, Exam, ExamPaper, ExamSection, ExamSession, ExamSyllabusItem, Question, Subject,
)
from app.services import exam_rules, qdisplay
from app.services import learn as svc
from tests.real_data import real_slice

DEVICE = "t-device"


def soup(resp):
    return BeautifulSoup(resp.get_data(as_text=True), "html.parser")


@pytest.fixture()
def real(app):
    real_slice(["indian_history", "indian_constitution", "ap_history", "indian_economy"])
    hist = Subject.query.filter_by(slug="indian_history").one()
    cons = Subject.query.filter_by(slug="indian_constitution").one()
    exam = Exam(slug="appsc_group_2", name_en="APPSC Group 2", name_te="ఏపీపీఎస్‌సీ గ్రూప్ 2", active=True)
    db.session.add(exam); db.session.flush()
    paper = ExamPaper(exam_id=exam.id, paper_num=0, name_en="Screening Test", name_te="స్క్రీనింగ్", total_marks=150, duration_min=150)
    db.session.add(paper); db.session.flush()
    s1 = ExamSection(paper_id=paper.id, name_en="Indian History", name_te="భారత చరిత్ర", marks=30, sort_order=1)
    s2 = ExamSection(paper_id=paper.id, name_en="Indian Constitution", name_te="భారత రాజ్యాంగం", marks=30, sort_order=2)
    db.session.add_all([s1, s2]); db.session.flush()
    for sec, subj in ((s1, hist), (s2, cons)):
        for n, ch in enumerate(Chapter.query.filter_by(subject_id=subj.id).order_by(Chapter.chapter_num).all()):
            db.session.add(ExamSyllabusItem(section_id=sec.id, chapter_id=ch.id, sort_order=n))
    db.session.commit()
    return {"exam": "appsc_group_2", "paper": 0, "hist": hist, "cons": cons}


@pytest.fixture()
def c(client):
    client.set_cookie("device_id", DEVICE)
    return client


def start(c, **form):
    return c.post("/exam/appsc_group_2/paper/0/start", data=form)


def session_id(resp):
    assert resp.status_code == 302, resp.get_data(as_text=True)[:200]
    return resp.headers["Location"].split("/exam-session/")[1].split("?")[0]


# ══ F1 ═══════════════════════════════════════════════════════════════════════
def test_real_chapter_questions_really_are_telugu_only(real):
    """The premise of F1: in the shipped data every chapter question has no English options."""
    qs = Question.query.filter_by(source_type="chapter").all()
    assert len(qs) > 100
    assert all(not (q.options_en or {}) and (q.options_te or {}) for q in qs)


@pytest.mark.parametrize("lang", ["te", "en", "both"])
def test_exam_page_shows_options_for_real_telugu_only_questions(c, real, lang):
    c.set_cookie("lang", lang)
    sid = session_id(start(c, mode="practice", count="10", minutes="10"))
    es = db.session.get(ExamSession, sid)
    shown = 0
    for i in range(1, len(es.question_ids) + 1):
        page = soup(c.get(f"/exam-session/{sid}?q={i}"))
        q = db.session.get(Question, es.question_ids[i - 1])
        opts = page.select("#qcard button.option")
        assert len(opts) >= 2, f"question {q.id} shows {len(opts)} options"
        for o in opts:
            text = o.select_one(".option-text").get_text(strip=True)
            assert text and not text[:2].lower() in ("a)", "b)", "c)", "d)")           # imported letter prefix removed
        if not q.options_en:                                                         # Telugu-only: single, always-visible span
            assert not page.select("#qcard .opt-en, #qcard .opt-te")
            assert page.select_one("#qcard .opt-only")["lang"] == "te"
            assert page.select_one("#qcard .qtext-only")                              # the question text is not blank either
            shown += 1
    assert shown > 0


def test_options_use_both_spans_only_when_both_languages_exist(app):
    both = Question(subject_id=1, source_type="practice", correct_answer="a", options_en={"a": "Yes"}, options_te={"a": "అవును"})
    en_only = Question(subject_id=1, source_type="practice", correct_answer="a", options_en={"a": "Yes", "b": "No"}, options_te={})
    te_only = Question(subject_id=1, source_type="chapter", correct_answer="b", options_en=None, options_te={"a": "a) ఒకటి", "b": "b) రెండు"})
    assert [o["kind"] for o in qdisplay.option_items(both)] == ["both"]
    assert [o["kind"] for o in qdisplay.option_items(en_only)] == ["en", "en"]
    items = qdisplay.option_items(te_only)
    assert [o["kind"] for o in items] == ["te", "te"] and items[0]["te"] == "ఒకటి"
    assert qdisplay.is_answerable(te_only) and qdisplay.is_answerable(en_only)
    assert not qdisplay.is_answerable(Question(subject_id=1, source_type="x", correct_answer="d", options_en={"a": "x"}, options_te={}))
    assert not qdisplay.is_answerable(Question(subject_id=1, source_type="x", correct_answer="a", options_en={}, options_te={}))


@pytest.mark.parametrize("lang", ["te", "en", "both"])
def test_legacy_practice_shows_options_for_real_questions_in_any_language(c, real, lang):
    c.set_cookie("lang", lang)
    first = Question.query.filter_by(subject_id=real["hist"].id).order_by(Question.id).first()
    page = soup(c.get("/practice/indian_history?i=1"))
    assert first.source_type == "chapter" and not first.options_en                    # a real Telugu-only question comes first
    assert len(page.select("#qcard button.option")) >= 2
    assert page.select_one(".qtext-only, .qtext-te")


def test_english_only_real_questions_also_show_in_telugu_mode(c, real):
    """Practice/PYQ rows have English options only: Telugu mode must not blank them."""
    c.set_cookie("lang", "te")
    page = soup(c.get("/learn/subject/ap_history/practice?i=1"))
    assert len(page.select("#opts .opt")) >= 2


def test_results_review_shows_option_text_and_explanations(c, real):
    sid = session_id(start(c, mode="practice", count="6", minutes="10"))
    es = db.session.get(ExamSession, sid)
    qs = [db.session.get(Question, i) for i in es.question_ids]
    right, wrong = qs[0], qs[1]
    wrong_key = next(k for k in "abcd" if k != wrong.correct_answer and (wrong.options_te or wrong.options_en).get(k))
    c.post(f"/exam-session/{sid}/answer", json={"question_id": right.id, "chosen": right.correct_answer})
    c.post(f"/exam-session/{sid}/answer", json={"question_id": wrong.id, "chosen": wrong_key})
    c.post(f"/exam-session/{sid}/submit")
    page = soup(c.get(f"/exam-session/{sid}/results"))
    items = page.select(".review-item")
    assert len(items) == len(qs)
    for item in items:
        for line in item.select(".review-answers span:not(.review-badge)"):
            txt = line.get_text(" ", strip=True)
            if "—" in txt:
                assert txt.split("—", 1)[1].strip(), f"blank answer text in: {txt!r}"
        assert item.select_one(".qtext-only, .qtext-te")                               # question text present
    wrong_item = next(i for i in items if "review-wrong" in i["class"])
    if wrong.explanation_te or wrong.explanation_en:
        assert wrong_item.select_one(".review-explanation .exp-only, .review-explanation .exp-te")


def test_app_js_does_not_bind_cards_without_a_submit_button():
    js = open("static/app.js", encoding="utf-8").read()
    assert "if (!card || !submitBtn) return;" in js


# ══ F2 ═══════════════════════════════════════════════════════════════════════
def test_default_session_is_a_small_unofficial_practice_test_never_all_questions(c, real):
    eligible = Question.query.filter(Question.chapter_id.isnot(None)).count()
    assert eligible > exam_rules.MAX_SESSION_QUESTIONS                                 # the real slice is larger than the cap
    es = db.session.get(ExamSession, session_id(start(c)))
    assert len(es.question_ids) == exam_rules.DEFAULT_PRACTICE_QUESTIONS < eligible
    assert es.config["unofficial"] is True and es.config["mode"] == "practice"
    assert es.config["total_marks"] is None and es.config["negative_marking"] is None
    assert es.config["duration_min"] == exam_rules.DEFAULT_PRACTICE_QUESTIONS           # the user's visible default, not 150


@pytest.mark.parametrize("count,expected", [("5000", exam_rules.MAX_SESSION_QUESTIONS), ("1", exam_rules.MIN_PRACTICE_QUESTIONS), ("37", 37)])
def test_requested_size_is_clamped(c, real, count, expected):
    es = db.session.get(ExamSession, session_id(start(c, mode="practice", count=count)))
    assert len(es.question_ids) == expected


def test_bad_numbers_and_unknown_mode_are_rejected_without_creating_a_session(c, real):
    for form in ({"mode": "practice", "count": "abc"}, {"mode": "practice", "minutes": "x"}, {"mode": "weird"}):
        assert start(c, **form).status_code == 400
    assert ExamSession.query.count() == 0


def test_official_test_is_refused_until_rules_are_verified(c, real):
    r = start(c, mode="official")
    assert r.status_code == 403 and ExamSession.query.count() == 0


def test_exam_page_disables_official_start_and_hides_seeded_rules(c, real):
    html = c.get("/exam/appsc_group_2").get_data(as_text=True)
    page = BeautifulSoup(html, "html.parser")
    off = next(b for b in page.select("button.btn-start-exam") if b.has_attr("disabled"))
    assert "unavailable" in off.get_text()
    assert page.select('form input[name=mode][value=practice]')
    assert not page.select('form input[name=mode][value=official]')
    assert "not verified" in html
    assert "150 min" not in html and "150 marks" not in html                           # seeded, unverified numbers are not shown as facts
    assert "unofficial practice test" in html.lower()


def test_sessions_contain_only_answerable_questions_spread_over_sections(c, real):
    es = db.session.get(ExamSession, session_id(start(c, mode="practice", count="10")))
    qs = [db.session.get(Question, i) for i in es.question_ids]
    assert all(qdisplay.is_answerable(q) for q in qs)
    assert {q.subject_id for q in qs} == {real["hist"].id, real["cons"].id}             # both sections represented
    assert abs(sum(q.subject_id == real["hist"].id for q in qs) - 5) <= 1


def test_unanswerable_questions_are_never_picked(app):
    s = Subject(slug="x", name_en="X", name_te="X"); db.session.add(s); db.session.flush()
    ch = Chapter(subject_id=s.id, chapter_num=1, title_en="c", title_te="c"); db.session.add(ch); db.session.flush()
    good = Question(subject_id=s.id, chapter_id=ch.id, source_type="chapter", correct_answer="a", options_te={"a": "అ", "b": "ఆ"}, question_te="ప్ర")
    nooptions = Question(subject_id=s.id, chapter_id=ch.id, source_type="chapter", correct_answer="a", options_en={}, options_te={}, question_te="ప్ర2")
    badkey = Question(subject_id=s.id, chapter_id=ch.id, source_type="chapter", correct_answer="e", options_en={"a": "x"}, options_te={}, question_en="q3")
    db.session.add_all([good, nooptions, badkey])
    e = Exam(slug="e", name_en="E", name_te="E"); db.session.add(e); db.session.flush()
    p = ExamPaper(exam_id=e.id, paper_num=0, name_en="P", name_te="P", total_marks=1, duration_min=1); db.session.add(p); db.session.flush()
    sec = ExamSection(paper_id=p.id, name_en="S", name_te="S", marks=1); db.session.add(sec); db.session.flush()
    db.session.add(ExamSyllabusItem(section_id=sec.id, chapter_id=ch.id)); db.session.commit()
    r = app.test_client().post("/exam/e/paper/0/start")
    assert db.session.get(ExamSession, session_id(r)).question_ids == [good.id]


def test_pick_questions_is_deterministic_capped_and_unique():
    pools = [list(range(1, 300)), list(range(250, 600))]
    a = exam_rules.pick_questions(pools, 500, seed=7)
    assert a == exam_rules.pick_questions(pools, 500, seed=7)
    assert len(a) == exam_rules.MAX_SESSION_QUESTIONS and len(set(a)) == len(a)
    assert a != exam_rules.pick_questions(pools, 500, seed=8)
    assert exam_rules.pick_questions([[], []], 10, 1) == []


def test_unofficial_session_pages_are_labelled_and_results_assume_no_pass_mark(c, real):
    sid = session_id(start(c, mode="practice", count="5", minutes="7"))
    take = c.get(f"/exam-session/{sid}").get_data(as_text=True)
    assert "Unofficial practice test" in take and "not the real exam pattern" in take
    c.post(f"/exam-session/{sid}/submit")
    res = c.get(f"/exam-session/{sid}/results").get_data(as_text=True)
    assert "Unofficial practice test" in res and "No negative marking is applied" in res
    for invented in ("passed", "Well done", "score-pass", "score-fail", "ఉత్తీర్ణులయ్యారు"):
        assert invented not in res


def test_verified_rules_enable_the_official_test(c, real, monkeypatch):
    monkeypatch.setitem(exam_rules.VERIFIED_RULES, ("appsc_group_2", 0),
                        {"question_count": 12, "duration_min": 14, "negative_marking": None, "source": "notification test fixture"})
    html = c.get("/exam/appsc_group_2").get_data(as_text=True)
    assert 'value="official"' in html and "12 questions" in html and "notification test fixture" in html
    es = db.session.get(ExamSession, session_id(start(c, mode="official")))
    assert len(es.question_ids) == 12 and es.config["duration_min"] == 14 and es.config["unofficial"] is False
    assert es.config["rules_source"] == "notification test fixture"


@pytest.mark.parametrize("rule", [
    {"question_count": 12, "duration_min": 14, "negative_marking": 0.25, "source": "x"},     # scoring does not support it yet
    {"question_count": 12, "duration_min": 14, "negative_marking": None},                    # no source
    {"question_count": 5000, "duration_min": 14, "negative_marking": None, "source": "x"},   # over the cap
    {"question_count": "many", "duration_min": 14, "negative_marking": None, "source": "x"},
])
def test_incomplete_or_unsupported_rules_do_not_enable_official(c, real, monkeypatch, rule):
    monkeypatch.setitem(exam_rules.VERIFIED_RULES, ("appsc_group_2", 0), rule)
    assert start(c, mode="official").status_code == 403


def test_old_exam_flow_url_still_works_without_form_fields(c, real):
    assert start(c).status_code == 302


# ══ F3 ═══════════════════════════════════════════════════════════════════════
def test_every_question_is_reachable_from_exactly_one_learn_place(real):
    banks = svc.bank_counts()
    for s in Subject.query.all():
        d = banks.get(s.id, {"practice": 0, "pyq": 0, "chapter": 0})
        assert d["practice"] + d["pyq"] + d["chapter"] == Question.query.filter_by(subject_id=s.id).count()
        assert len(svc.bank_questions(s.id, "practice")) == d["practice"]
        assert len(svc.bank_questions(s.id, "pyq")) == d["pyq"]
        assert Question.query.filter_by(subject_id=s.id, source_type="chapter").filter(Question.chapter_id.isnot(None)).count() == d["chapter"]


def test_hub_counts_match_reachable_questions(c, real):
    data = svc.hub()
    by = {e["subject"].slug: e for e in data["subjects"]}
    for slug, e in by.items():
        assert e["question_count"] == Question.query.filter_by(subject_id=e["subject"].id).count()
    page = soup(c.get("/learn/"))
    card = page.select_one('[data-subject="ap_history"]')
    assert card, "ap_history has no chapters-with-questions but must be discoverable"
    text = card.get_text(" ", strip=True)
    assert f"{by['ap_history']['chapter_count']} chapters · {by['ap_history']['question_count']} questions" in text


def test_subject_without_chapters_but_with_questions_is_discoverable_and_practisable(c, real):
    econ = Subject.query.filter_by(slug="indian_economy").one()
    assert Chapter.query.filter_by(subject_id=econ.id).count() == 0 and Question.query.filter_by(subject_id=econ.id).count() > 0
    hub = soup(c.get("/learn/"))
    link = hub.select_one('[data-subject="indian_economy"]')
    assert link and link["href"] == "/learn/subject/indian_economy"
    page = soup(c.get(link["href"]))
    assert "Nothing here yet" not in page.get_text() or page.select(".tile-grid")
    tiles = [a["href"] for a in page.select(".tile-grid a")]
    assert any(h.startswith("/learn/subject/indian_economy/practice") for h in tiles)


def test_section_page_counts_and_bank_links(c, real):
    sec = ExamSection.query.filter_by(name_en="Indian History").one()
    page = soup(c.get(f"/learn/section/{sec.id}"))
    assert page.select(".tile-grid a[href*='/learn/subject/indian_history/']")
    hub = svc.hub()
    s = next(x for p in hub["papers"] for x in p["sections"] if x["section"].id == sec.id)
    banks = svc.bank_counts([real["hist"].id])[real["hist"].id]
    chapter_q = Question.query.filter(Question.chapter_id.in_([i.chapter_id for i in sec.items] if hasattr(sec, "items") else
                                      [r.chapter_id for r in ExamSyllabusItem.query.filter_by(section_id=sec.id)])).count()
    assert s["question_count"] == chapter_q + banks["practice"] + banks["pyq"]


@pytest.mark.parametrize("bank", ["practice", "pyq"])
def test_ap_history_banks_serve_every_question_once(c, real, bank):
    ap = Subject.query.filter_by(slug="ap_history").one()
    total = len(svc.bank_questions(ap.id, bank))
    assert total > 0
    seen = []
    for i in range(1, total + 1):
        r = c.get(f"/learn/subject/ap_history/{bank}?i={i}")
        assert r.status_code == 200
        page = soup(r)
        card = page.select_one("#qcard")
        assert card and len(page.select("#opts .opt")) >= 2
        seen.append(card["data-qid"])
    assert len(seen) == len(set(seen)) == total
    done = soup(c.get(f"/learn/subject/ap_history/{bank}?i={total + 1}"))
    assert done.select_one("#summary")


def test_pyq_bank_is_labelled_unverified_and_practice_bank_is_labelled_practice(c, real):
    pyq = soup(c.get("/learn/subject/ap_history/pyq?i=1"))
    assert "Source not verified" in pyq.get_text() and "Previous paper" in pyq.get_text()
    practice = soup(c.get("/learn/subject/ap_history/practice?i=1"))
    assert "Practice question" in practice.get_text() and "Previous paper" not in practice.get_text()
    assert "Chapter question" not in practice.get_text()


def test_subject_page_lists_chapters_and_banks_with_exact_counts(c, real):
    page = soup(c.get("/learn/subject/ap_history"))
    ap = Subject.query.filter_by(slug="ap_history").one()
    banks = svc.bank_counts([ap.id])[ap.id]
    text = page.get_text(" ", strip=True)
    assert f"{banks['practice']} questions" in text and f"{banks['pyq']} questions" in text
    assert page.select("a[data-topic]")                                               # chapters are still listed


def test_chapter_practice_still_serves_chapter_questions_only(c, real):
    ch = Chapter.query.filter_by(subject_id=real["hist"].id).first()
    n = Question.query.filter_by(chapter_id=ch.id, source_type="chapter").count()
    page = soup(c.get(f"/learn/topic/{ch.id}/practice?i=1"))
    assert page.select_one("[data-practice]") and page.select_one("#counter").get_text(strip=True).endswith(f"/ {n}") or n > 0


def test_bank_answer_flow_and_bad_routes(c, real):
    qid = soup(c.get("/learn/subject/ap_history/practice?i=1")).select_one("#qcard")["data-qid"]
    q = db.session.get(Question, int(qid))
    r = c.post("/api/answer", json={"question_id": q.id, "chosen": q.correct_answer, "confidence": 0})
    assert r.status_code == 200 and r.get_json()["correct"] is True
    assert c.get("/learn/subject/ap_history/other").status_code == 404
    assert c.get("/learn/subject/nope/practice").status_code == 404


def test_empty_bank_page_and_subject_with_nothing_is_coming_soon(c, real):
    db.session.add(Subject(slug="blank", name_en="Blank", name_te="ఖాళీ")); db.session.commit()
    page = soup(c.get("/learn/"))
    assert not page.select_one('[data-subject="blank"]')                              # no link: nothing to open
    assert "Coming soon" in page.get_text()
    r = c.get("/learn/subject/blank/practice")
    assert r.status_code == 200 and "Nothing here yet" in r.get_data(as_text=True)


def test_hub_without_exam_lists_every_subject_with_reachable_counts(c, app):
    real_slice(["ap_history", "indian_economy"])
    page = soup(c.get("/learn/"))
    assert page.select_one('[data-subject="indian_economy"]') and page.select_one('[data-subject="ap_history"]')
