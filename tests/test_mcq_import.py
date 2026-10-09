"""Prepared-MCQ importer: validation, duplicates, idempotence, note links, and the review screen's three states."""
import copy
import json
import os
from pathlib import Path

import pytest

from app.db import db
from app.models import (Chapter, Exam, ExamPaper, ExamSection, ExamSession, ExamSyllabusItem, Note, Question, Subject)
from app.services import mcq_import
from tests.test_exam_session import _start_and_get_id  # noqa: F401

TITLE = "Introduction to Andhras & Sources"
OPT_EN = {"a": "Aitareya Brahmana", "b": "Arthashastra", "c": "Rajatarangini", "d": "Harshacharita"}
OPT_TE = {"a": "ఐతరేయ బ్రాహ్మణం", "b": "అర్థశాస్త్రం", "c": "రాజతరంగిణి", "d": "హర్షచరితం"}


def rec(n, **kw):
    r = dict(import_ref=f"t-{n}", subject_slug="ap_history", chapter_num=2, chapter_title_en=TITLE, difficulty="M",
             question_en=f"Which source number {n} names the Andhras early?", question_te=f"ఆంధ్రులను ప్రస్తావించిన మూలం సంఖ్య {n} ఏది?",
             options_en={k: f"{v} {n}" for k, v in OPT_EN.items()}, options_te={k: f"{v} {n}" for k, v in OPT_TE.items()},
             correct_answer="a", explanation_en=f"English explanation {n}.", explanation_te=f"తెలుగు వివరణ {n}.",
             note_target_slug="u1-c01-literary-sources", note_section_num=4,
             source_trace={"combined_id": f"AP9-{n:05d}", "origin": "AP_MASTER", "H": "", "secret_marker": "TRACE-XYZ"})
    r.update(kw)
    return r


def write(tmp_path, recs, name="p.jsonl"):
    p = tmp_path / name
    p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in recs), encoding="utf-8")
    return str(p)


@pytest.fixture()
def world(app):
    s = Subject(slug="ap_history", name_en="AP History", name_te="ఏపీ చరిత్ర")
    db.session.add(s); db.session.flush()
    ch = Chapter(subject_id=s.id, chapter_num=2, title_en=TITLE, title_te="పరిచయం")
    db.session.add(ch); db.session.flush()
    for n in (4, 7):
        db.session.add(Note(chapter_id=ch.id, section_num=n, heading_en=f"S{n}", heading_te=f"ఎస్{n}", body_en="b", body_te="బి"))
    legacy = Question(subject_id=s.id, chapter_id=None, source_type="practice", question_en="Legacy stem about Satavahanas?",
                      options_en={"a": "x", "b": "y", "c": "z", "d": "w"}, correct_answer="b", explanation_en="old")
    db.session.add(legacy); db.session.commit()
    return {"subject": s.id, "chapter": ch.id, "legacy": legacy.id}


def test_validate_flags_each_defect():
    assert mcq_import.validate(rec(1)) == []
    bad = rec(1, correct_answer="A"); assert any("lowercase" in e for e in mcq_import.validate(bad))
    bad = rec(1); bad["options_te"].pop("d"); assert any("options_te" in e for e in mcq_import.validate(bad))
    bad = rec(1); bad["options_en"]["b"] = ""; assert any("options_en.b" in e for e in mcq_import.validate(bad))
    bad = rec(1, explanation_te=""); assert any("explanation_te" in e for e in mcq_import.validate(bad))
    bad = rec(1); bad["options_en"]["c"] = "మిశ్రమం"; assert any("contains Telugu" in e for e in mcq_import.validate(bad))
    bad = rec(1, source_trace={}); assert any("source_trace" in e for e in mcq_import.validate(bad))


def test_preview_writes_nothing_and_apply_is_idempotent(app, world, tmp_path):
    f = write(tmp_path, [rec(1), rec(2, note_section_num=None)])
    r = mcq_import.run(f)
    assert (r["to_import"], r["imported"]) == (2, 0)
    assert Question.query.filter(Question.import_ref.isnot(None)).count() == 0
    r = mcq_import.run(f, apply=True)
    assert r["imported"] == 2 and r["note_exact"] == 1 and r["note_chapter_fallback"] == 1
    r = mcq_import.run(f, apply=True)
    assert (r["imported"], r["already_imported"]) == (0, 2)
    q = Question.query.filter_by(import_ref="t-1").one()
    assert q.source_type == "chapter" and q.chapter_id == world["chapter"] and q.note_section_num == 4
    assert q.source_trace["combined_id"] == "AP9-00001"
    assert Question.query.filter_by(import_ref="t-2").one().note_section_num is None


def test_legacy_questions_untouched(app, world, tmp_path):
    before = db.session.get(Question, world["legacy"])
    snap = (before.question_en, before.correct_answer, before.chapter_id, before.note_section_num, before.explanation_en)
    mcq_import.run(write(tmp_path, [rec(1)]), apply=True)
    after = db.session.get(Question, world["legacy"])
    assert snap == (after.question_en, after.correct_answer, after.chapter_id, after.note_section_num, after.explanation_en)
    assert Question.query.filter_by(subject_id=world["subject"]).count() == 2


def test_duplicates_against_bank_and_inside_package(app, world, tmp_path):
    legacy_dup = rec(1, question_en="Legacy stem about Satavahanas?", options_en={"a": "p", "b": "y", "c": "q", "d": "r"},
                     correct_answer="b", import_ref="t-legacy")
    near = rec(3, question_en="Which source number 2 names the Andhras early", import_ref="t-near")
    near["options_en"] = copy.deepcopy(rec(2)["options_en"])
    r = mcq_import.run(write(tmp_path, [legacy_dup, rec(2), near]), apply=True)
    assert r["imported"] == 1
    reasons = {d["import_ref"]: d for d in r["duplicates"]}
    assert reasons["t-legacy"]["duplicate_of_question_id"] == world["legacy"]
    assert reasons["t-near"]["source"] == "AP9-00003"


def test_invalid_records_skipped_not_imported(app, world, tmp_path):
    bad = rec(5); bad["options_te"]["a"] = ""
    r = mcq_import.run(write(tmp_path, [bad, rec(6)]), apply=True)
    assert r["imported"] == 1 and r["invalid"][0]["import_ref"] == "t-5"


def test_missing_section_downgrades_to_chapter_fallback(app, world, tmp_path):
    r = mcq_import.run(write(tmp_path, [rec(7, note_section_num=99)]), apply=True)
    assert r["note_chapter_fallback"] == 1
    assert Question.query.filter_by(import_ref="t-7").one().note_section_num is None


def test_wrong_chapter_title_or_ids_refused(app, world, tmp_path):
    with pytest.raises(mcq_import.McqImportError):
        mcq_import.run(write(tmp_path, [rec(1, chapter_title_en="Something else")]))
    with pytest.raises(mcq_import.McqImportError):
        mcq_import.run(write(tmp_path, [rec(1, subject_id=world["subject"] + 50, chapter_id=world["chapter"])]))
    with pytest.raises(mcq_import.McqImportError):
        mcq_import.run(write(tmp_path, [rec(1, subject_slug="nope")]))


# ── review screen: correct, wrong, skipped ───────────────────────────
@pytest.fixture()
def exam(app, world, tmp_path):
    mcq_import.run(write(tmp_path, [rec(1), rec(2, note_section_num=None), rec(3, note_section_num=7)]), apply=True)
    e = Exam(slug="appsc_g2", name_en="APPSC Group 2", name_te="గ్రూప్ 2"); db.session.add(e); db.session.flush()
    p = ExamPaper(exam_id=e.id, paper_num=1, name_en="P1", name_te="పి1", total_marks=150, duration_min=150)
    db.session.add(p); db.session.flush()
    sec = ExamSection(paper_id=p.id, section_label="A", name_en="H", name_te="హ", marks=75)
    db.session.add(sec); db.session.flush()
    db.session.add(ExamSyllabusItem(section_id=sec.id, chapter_id=world["chapter"])); db.session.commit()
    return {"exam_slug": e.slug, "paper_num": 1}


def test_review_shows_answer_explanation_and_link_for_all_states(client, app, world, exam):
    sid = _start_and_get_id(client, exam)
    es = db.session.get(ExamSession, sid)
    by_ref = {db.session.get(Question, i).import_ref: i for i in es.question_ids}
    assert set(by_ref) == {"t-1", "t-2", "t-3"}
    client.post(f"/exam-session/{sid}/answer", json={"question_id": by_ref["t-1"], "chosen": "a"})   # correct
    client.post(f"/exam-session/{sid}/answer", json={"question_id": by_ref["t-2"], "chosen": "b"})   # wrong
    # t-3 skipped
    client.post(f"/exam-session/{sid}/submit")
    html = client.get(f"/exam-session/{sid}/results").get_data(as_text=True)
    assert html.count("review-badge badge-correct") == 1 and html.count("review-badge badge-wrong") == 1
    assert html.count("review-badge badge-skip") == 1
    for n in (1, 2, 3):
        assert f"English explanation {n}." in html and f"తెలుగు వివరణ {n}." in html
    assert html.count('data-testid="read-in-notes"') == 3
    ch = world["chapter"]
    assert f'href="/learn/topic/{ch}/notes?section=4"' in html and f'href="/learn/topic/{ch}/notes?section=7"' in html
    assert f'data-exact="true"' in html and html.count('data-exact="false"') == 1
    assert "Read the chapter notes" in html          # the fallback is labelled as chapter-level
    # the skipped and wrong rows state the correct answer
    assert html.count("Correct:") >= 2
    # internal provenance never reaches learners
    for leak in ("TRACE-XYZ", "AP9-0000", "u1-c01-literary-sources", "source_trace", "import_ref", "t-1"):
        assert leak not in html


def test_note_links_resolve_to_real_pages(client, app, world, exam):
    sid = _start_and_get_id(client, exam)
    client.post(f"/exam-session/{sid}/submit")
    import re
    html = client.get(f"/exam-session/{sid}/results").get_data(as_text=True)
    hrefs = set(re.findall(r'data-testid="read-in-notes"[^>]*href="([^"]+)"', html)) | set(re.findall(r'href="([^"]+)"[^>]*data-testid="read-in-notes"', html))
    assert hrefs
    for h in hrefs:
        assert client.get(h).status_code == 200, h


def test_chapter_without_notes_gets_no_link(client, app, world, exam):
    Note.query.delete(); db.session.commit()
    sid = _start_and_get_id(client, exam)
    client.post(f"/exam-session/{sid}/submit")
    html = client.get(f"/exam-session/{sid}/results").get_data(as_text=True)
    assert 'data-testid="read-in-notes"' not in html


# ── the real prepared packages (skipped when the content folder is not available) ──
PREP = Path(os.environ["MCQ_PREPARED_DIR"]) if os.environ.get("MCQ_PREPARED_DIR") else Path("/nonexistent-prepared-dir")


@pytest.mark.skipif(not PREP.is_dir(), reason="set MCQ_PREPARED_DIR to the 05_claude_import folder")
def test_real_prepared_files_are_valid_and_unique():
    files = sorted(PREP.glob("AP_History_U1_C0*_Import_Ready.jsonl"))
    assert files
    refs = set()
    for f in files:
        for r in mcq_import.load_prepared(f):
            assert mcq_import.validate(r) == [], (f.name, r["import_ref"])
            assert r["import_ref"] not in refs
            refs.add(r["import_ref"])
            assert r["note_link_status"] in ("exact", "chapter_fallback")
            assert (r["note_section_num"] is not None) == (r["note_link_status"] == "exact")


def test_telugu_option_identical_to_english_is_accepted_but_empty_or_missing_is_not():
    r = rec(1); r["options_en"]["d"] = "La Madeleine"; r["options_te"]["d"] = "La Madeleine"
    assert mcq_import.validate(r) == []
    r["options_te"]["d"] = "Madeleine cave site"
    assert any("options_te.d" in e for e in mcq_import.validate(r))
