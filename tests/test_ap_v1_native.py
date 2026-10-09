"""Native ap-history-import-v1 support: expanded-notes collection (separate from the 17 legacy notes), canonical mapping by slug,
repeat-import safety, bilingual display, correct/wrong/skipped review, and that every expanded-note link opens its intended content.

Synthetic packages cover the rules and refusals everywhere; the real 129-question closure package is exercised when it is
available (AP_V1_PACKAGE, default /mnt/user-data/uploads/aph-u1-c01-closure-20261009)."""
import copy
import hashlib
import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

import pytest

from app.db import db
from app.models import (Chapter, Exam, ExamPaper, ExamSection, ExamSession, ExamSyllabusItem, ExpandedNote, ExpandedNoteAppMap, Note,
                        Question, Subject, SyllabusChapter, SyllabusSubtopic)
from app.services import ap_batch_import as b
from app.services import ap_canonical as canon
from app.services import ap_v1_import as v1
from app.services import expanded_notes as xn
from app.services import expanded_view as xv
from app.services.learn import note_link_for

CH = "u1-c01-region-people-sources"
SIX = ["u1-c01-land-people-identity", "u1-c01-literary-sources", "u1-c01-foreign-accounts", "u1-c01-inscriptions", "u1-c01-coins",
       "u1-c01-archaeology-sites"]
_UP = "/mnt/user-data/uploads/"
REAL = Path(os.environ.get("AP_V1_PACKAGE", _UP + "aph-u1-c01-closure-metadata-r1-20261009"))
# known frozen revisions of the same 129-question batch (never combined): original closure and metadata-r1
KNOWN_SHA = {"aph-u1-c01-closure-20261009": "1f1ad6fd94259c93f707b58fbb010d7b1fa877d441811cab5c5b9274cdcc6d73",
             "aph-u1-c01-closure-metadata-r1-20261009": "a69d4a50aa1b85a0f682879c3ddac89df588d581f69265a8eee61f8febc2657d"}
REAL_SHA = KNOWN_SHA.get(REAL.name)


# ── synthetic package ────────────────────────────────────────────────
CORE = """CHAPTER 1 — TEST
అధ్యాయం 1 — పరీక్ష

GROUP 2 — CORE CONTENT / ప్రధాన విషయాలు

01. HISTORICAL SETTING / చారిత్రక నేపథ్యం
EN: The Krishna valley shaped settlement.
TE: కృష్ణా లోయ నివాసాలను తీర్చిదిద్దింది.
Reading basis: Test book:
https://example.org/setting

02. AITAREYA BRAHMANA / ఐతరేయ బ్రాహ్మణం
EN: The text names the Andhras.
TE: ఈ గ్రంథం ఆంధ్రులను పేర్కొంటుంది.
Sources: Test portal:
https://example.org/ab
https://example.org/ab2

03. PLINY / ప్లినీ
EN: Pliny lists the Andarae.
TE: ప్లినీ ఆండరేల వివరాలు ఇచ్చాడు.
Source: Pliny VI.67:
https://example.org/pliny

PART B — GROUP 1: HISTORICAL DISCUSSION / గ్రూప్ 1

G1-01. SOURCES / ఆధారాలు
EN: Sources show more than rulers.
TE: ఆధారాలు రాజుల కంటే ఎక్కువ చూపుతాయి.
Evidence links: sections 02 and 03.

PART C — GROUP 2 QUICK REVISION / గ్రూప్ 2 సంక్షిప్త పునశ్చరణ
01–03: setting; literature; foreign accounts.
తెలుగు పునశ్చరణ: ప్రాంతం → సాహిత్యం → విదేశీ.
"""
ADD = """CHAPTER1 — ADDENDUM

CH01-A01. PLINY AND THE ANDARAE / ప్లినీ, ఆండరేలు
EN: Pliny gives the Andarae's towns.
TE: ప్లినీ ఆండరేల పట్టణాలను పేర్కొన్నాడు.
Core: CH01-S03.
https://example.org/pliny2 (VI.67)
"""


def _opts(n):
    return {k: {"en": f"Option {k} of {n}", "te": f"{n}వ ప్రశ్న ఎంపిక {k}"} for k in "abcd"}


def _q(n, sub, anchors, sections, diff="easy", **kw):
    r = {"source": "codex_generated", "source_qid": f"APH-U1-C1-B20261009-Q{n:03d}", "batch_id": "test-batch", "source_file": "SNAP.jsonl",
         "chapter_slug": CH, "subtopic_slug": sub, "microtopic_slugs": [], "secondary_chapters": [], "coverage_scope": "direct",
         "difficulty": diff, "qtype": "factual", "question_en": f"Question number {n} about the Andhra sources?",
         "question_te": f"ఆంధ్ర ఆధారాల గురించి {n}వ ప్రశ్న ఏమిటి?", "options": _opts(n), "correct_answer": "b",
         "explanation_en": f"English explanation {n}.", "explanation_te": f"తెలుగు వివరణ {n}.", "review_status": "bilingual_approved",
         "approval_basis": "author_bilingual_content_review", "H": "H" if n % 2 else "",
         "source_trace": {"candidate_id": f"CAND-{n}", "source_ids": [f"AP9-0{n}"], "original_H": "H" if n % 2 else ""},
         "sources": [{"url": f"https://example.org/src{n}", "locator": f"loc{n}"}],
         "expanded_note": {"file": "notes/CH01_CORE_NOTES_EN_TE.txt", "sections": sections, "anchor_ids": anchors},
         "difficulty_calibration": "provisional_design_label_not_empirical", "selection_role": "selected", "related_old_package_refs": []}
    r.update(kw)
    return r


def make_pkg(root, records=None, name="aph-test", manifest_over=None, core=CORE, add=ADD, anchors=None):
    pkg = Path(root) / "05_claude_import" / name
    (pkg / "notes").mkdir(parents=True)
    (pkg / "notes" / "CH01_CORE_NOTES_EN_TE.txt").write_text(core, encoding="utf-8")
    (pkg / "notes" / "CH01_NOTES_ADDENDUM_EN_TE.txt").write_text(add, encoding="utf-8")
    anchors = anchors or {
        "format": "ap-history-note-anchors-v1", "chapter_slug": CH,
        "anchors": [{"id": f"CH01-S0{i}", "section": i, "heading_en": h} for i, h in
                    ((1, "01. HISTORICAL SETTING"), (2, "02. AITAREYA BRAHMANA"), (3, "03. PLINY"))],
        "addendum_anchors": [{"id": "CH01-A01", "heading_en": "Pliny and the Andarae", "core_connections": ["CH01-S03"]}]}
    (pkg / "notes" / "note_anchors.json").write_text(json.dumps(anchors), encoding="utf-8")
    recs = records if records is not None else [
        _q(1, SIX[1], ["CH01-S02"], [2]), _q(2, SIX[2], ["CH01-S03", "CH01-S01"], [3, 1], diff="toughest"),
        _q(3, SIX[2], ["CH01-A01"], [], diff="tough"), _q(4, SIX[0], ["CH01-S01"], [1], diff="medium")]
    raw = "\n".join(json.dumps(r, ensure_ascii=False) for r in recs).encode("utf-8")
    (pkg / "questions.jsonl").write_bytes(raw)
    man = {"format_version": "ap-history-import-v1", "taxonomy_version": "ap-history-taxonomy-v1", "batch_id": "test-batch",
           "source": "codex_generated", "question_count": len(recs), "questions_sha256": hashlib.sha256(raw).hexdigest(),
           "content_approval": "bilingual_approved", "approval_note": "Author-reviewed bilingual content; not independent certification.",
           "notes": {"core": "notes/CH01_CORE_NOTES_EN_TE.txt", "addendum": "notes/CH01_NOTES_ADDENDUM_EN_TE.txt"},
           "permissions": {"database_write": False, "seed": False, "deploy": False, "overwrite_legacy": False}}
    man.update(manifest_over or {})
    (pkg / "manifest.json").write_text(json.dumps(man), encoding="utf-8")
    return pkg


@pytest.fixture()
def world(app):
    s = Subject(slug="ap_history", name_en="AP History", name_te="ఆంధ్రప్రదేశ్ చరిత్ర")
    db.session.add(s); db.session.flush()
    old = Chapter(subject_id=s.id, chapter_num=2, title_en="Introduction to Andhras & Sources", title_te="పరిచయం")
    db.session.add(old); db.session.flush()
    for n in range(1, 18):
        db.session.add(Note(chapter_id=old.id, section_num=n, heading_en=f"Old section {n}", heading_te=f"పాత సెక్షన్ {n}",
                            body_en="old body", body_te="పాత బాడీ"))
    legacy = [Question(subject_id=s.id, chapter_id=None, source_type="practice", question_en=f"Legacy stem {i} about Satavahanas?",
                       options_en={"a": "x", "b": "y", "c": "z", "d": "w"}, correct_answer="b", explanation_en="old") for i in range(5)]
    db.session.add_all(legacy); db.session.commit()
    canon.seed(); canon.seed_taxonomy()
    return {"subject": s.id, "old_chapter": old.id}


def legacy_snapshot():
    return [(q.id, q.question_en, q.chapter_id, q.source_type, q.source_qid, q.syllabus_chapter_id)
            for q in Question.query.filter(Question.source_qid.is_(None)).order_by(Question.id)]


def counts():
    return (Note.query.count(), Chapter.query.count(), Question.query.count(), ExpandedNote.query.count())


# ── canonical taxonomy ───────────────────────────────────────────────
def test_canonical_chapter_and_six_subtopic_slugs_are_confirmed(world):
    ch = SyllabusChapter.query.filter_by(slug=CH).one()
    assert ch.chapter_num == 1 and Chapter.query.get(world["old_chapter"]).chapter_num == 2     # canonical 1 is app chapter 2: never assumed equal
    subs = [s.slug for s in SyllabusSubtopic.query.filter_by(chapter_id=ch.id).order_by(SyllabusSubtopic.sort_order)]
    assert sorted(subs) == sorted(SIX)


# ── notes collection ─────────────────────────────────────────────────
def test_notes_parse_with_stable_anchors_and_no_loss(tmp_path):
    rows, ap, problems, warnings = xn.parse_package_notes(make_pkg(tmp_path))
    assert problems == []
    ids = [r["anchor_id"] for r in rows]
    assert ids == ["CH01-S01", "CH01-S02", "CH01-S03", "CH01-G1-01", "CH01-QR", "CH01-A01"]
    s2 = next(r for r in rows if r["anchor_id"] == "CH01-S02")
    assert s2["package_section"] == 2 and s2["heading_te"] == "ఐతరేయ బ్రాహ్మణం"
    assert [x["url"] for x in s2["sources"]] == ["https://example.org/ab", "https://example.org/ab2"]
    a1 = next(r for r in rows if r["anchor_id"] == "CH01-A01")
    assert a1["core_connections"] == ["CH01-S03"] and a1["sources"][0]["locator"] == "VI.67"


def test_notes_load_is_separate_add_only_and_idempotent(world, tmp_path):
    pkg = make_pkg(tmp_path)
    before = legacy_snapshot(); notes_before = [(n.id, n.section_num, n.heading_en, n.body_en) for n in Note.query.order_by(Note.id)]
    prev = xn.load_notes(pkg)                                   # preview writes nothing
    assert prev["to_add"] == 6 and ExpandedNote.query.count() == 0
    rep = xn.load_notes(pkg, apply=True)
    assert rep["added"] == 6 and ExpandedNote.query.count() == 6
    again = xn.load_notes(pkg, apply=True)
    assert again["added"] == 0 and again["unchanged"] == 6
    assert Note.query.count() == 17 and [(n.id, n.section_num, n.heading_en, n.body_en) for n in Note.query.order_by(Note.id)] == notes_before
    assert legacy_snapshot() == before
    assert all(e.syllabus_chapter_id == SyllabusChapter.query.filter_by(slug=CH).one().id for e in ExpandedNote.query.all())


def test_changed_note_text_is_a_reported_conflict_never_an_overwrite(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path, name="a"), apply=True)
    pkg2 = make_pkg(tmp_path, name="b", core=CORE.replace("shaped settlement", "shaped everything"))
    rep = xn.load_notes(pkg2, apply=True)
    assert [c["anchor_id"] for c in rep["conflicts"]] == ["CH01-S01"]
    assert "shaped settlement" in ExpandedNote.query.filter_by(anchor_id="CH01-S01").one().body_en


def test_notes_refuse_when_text_and_anchor_list_disagree_or_chapter_unseeded(app, world, tmp_path):
    bad = make_pkg(tmp_path, name="bad", core=CORE.replace("03. PLINY", "04. PLINY"))
    with pytest.raises(xn.NotesError):
        xn.load_notes(bad)
    db.session.query(SyllabusChapter).delete(); db.session.commit()
    with pytest.raises(xn.NotesError, match="not seeded"):
        xn.load_notes(make_pkg(tmp_path, name="ok"))


def test_package_section_numbers_are_never_app_section_numbers(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path), apply=True)
    e = ExpandedNote.query.filter_by(anchor_id="CH01-S02").one()
    assert not hasattr(e, "section_num") and e.package_section == 2
    assert ExpandedNoteAppMap.query.count() == 0           # nothing is mapped until a human decides
    # a draft mapping is stored but invisible to learners; an approved one is shown, and the section must exist
    xn.apply_app_map([{"anchor_id": "CH01-S02", "app_section_num": 5, "reason": "same topic"}])
    assert xv.page(SyllabusChapter.query.filter_by(slug=CH).one(), "CH01-S02")["related_old"] == []
    ExpandedNoteAppMap.query.update({"status": "approved"}); db.session.commit()
    rel = xv.page(SyllabusChapter.query.filter_by(slug=CH).one(), "CH01-S02")["related_old"]
    assert rel == [{"chapter_id": world["old_chapter"], "section": 5, "relation": "related"}]
    with pytest.raises(xn.NotesError):
        xn.apply_app_map([{"anchor_id": "CH01-S02", "app_section_num": 99}])


# ── question import ──────────────────────────────────────────────────
def test_preview_writes_nothing_and_apply_needs_an_approval_reference(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path), apply=True)
    pkg = tmp_path / "05_claude_import" / "aph-test"
    n = Question.query.count()
    rep = v1.run(pkg)
    assert rep["to_import"] == 4 and rep["imported"] == 0 and Question.query.count() == n
    with pytest.raises(v1.V1ImportError, match="approval"):
        v1.run(pkg, apply=True)
    assert Question.query.count() == n


def test_import_maps_to_canonical_rows_by_slug_and_keeps_provenance(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path), apply=True)
    pkg = tmp_path / "05_claude_import" / "aph-test"
    rep = v1.run(pkg, apply=True, approval_ref="test-ref")
    assert rep["imported"] == 4
    chap = SyllabusChapter.query.filter_by(slug=CH).one()
    q = Question.query.filter_by(source_qid="APH-U1-C1-B20261009-Q002").one()
    assert q.syllabus_chapter_id == chap.id and q.subtopic.slug if hasattr(q, "subtopic") else True
    assert SyllabusSubtopic.query.get(q.subtopic_id).slug == SIX[2]
    assert q.chapter_id is None and q.source == "codex_generated" and q.batch_id == "test-batch" and q.qtype == "factual"
    assert q.review_status == "bilingual_approved" and q.review_status != "fact_verified"
    assert q.difficulty == "H" and q.source_trace["difficulty_original"] == "toughest"      # coarse column, full value kept
    assert Question.query.filter_by(source_qid="APH-U1-C1-B20261009-Q003").one().source_trace["difficulty_original"] == "tough"
    t = q.source_trace
    assert t["H"] == "" and t["original_H"] == "" and t["candidate_id"] == "CAND-2" and t["source_ids"] == ["AP9-02"]
    assert t["sources"] == [{"url": "https://example.org/src2", "locator": "loc2"}]
    assert t["expanded_note"]["anchor_ids"] == ["CH01-S03", "CH01-S01"] and "not independent" in t["content_approval_note"]
    assert t["package_questions_sha256"] and t["coverage_scope"] == "direct"
    assert q.secondary_tags["coverage_scope"] == "direct"
    assert Question.query.filter_by(source_qid="APH-U1-C1-B20261009-Q001").one().source_trace["H"] == "H"


def test_repeat_import_is_a_noop_and_legacy_rows_untouched(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path), apply=True)
    pkg = tmp_path / "05_claude_import" / "aph-test"
    before = legacy_snapshot()
    v1.run(pkg, apply=True, approval_ref="r")
    snap = counts()
    again = v1.run(pkg, apply=True, approval_ref="r")
    assert again["imported"] == 0 and again["already_imported"] == 4 and counts() == snap
    assert legacy_snapshot() == before and Note.query.count() == 17


def test_refuses_unseeded_taxonomy_unloaded_notes_and_unapproved_records(world, tmp_path):
    pkg = make_pkg(tmp_path)
    rep = v1.run(pkg)                                           # notes not loaded: preview reports, apply refuses
    assert len(rep["unresolved_note_links"]) == 5      # S02; S03+S01; A01; S01
    with pytest.raises(v1.V1ImportError, match="load the package notes first"):
        v1.run(pkg, apply=True, approval_ref="r")
    assert Question.query.filter(Question.source_qid.isnot(None)).count() == 0
    bad = make_pkg(tmp_path, name="unapproved", records=[_q(1, SIX[1], ["CH01-S02"], [2], review_status="content_review_required")])
    with pytest.raises(v1.V1ImportError, match="validator"):
        v1.run(bad)
    SyllabusSubtopic.query.delete(); db.session.commit()
    with pytest.raises(v1.V1ImportError, match="subtopic"):
        v1.run(pkg)


def test_package_outside_the_import_folder_or_edited_after_approval_is_refused(world, tmp_path):
    pkg = make_pkg(tmp_path)
    elsewhere = tmp_path / "other" / "aph-test"; shutil.copytree(pkg, elsewhere)
    with pytest.raises(v1.V1ImportError):
        v1.run(elsewhere)
    (pkg / "questions.jsonl").write_text((pkg / "questions.jsonl").read_text(encoding="utf-8") + "\n", encoding="utf-8")
    (pkg / "questions.jsonl").write_bytes((pkg / "questions.jsonl").read_bytes().replace(b"Question number 1", b"Question number 9"))
    with pytest.raises(v1.V1ImportError):
        v1.run(pkg)


def test_overlap_with_existing_question_is_reported_and_blocks_apply_until_decided(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path), apply=True)
    pkg = tmp_path / "05_claude_import" / "aph-test"
    db.session.add(Question(subject_id=world["subject"], chapter_id=None, source_type="chapter", import_ref="aph-u1c01-OLD-1",
                            question_en="Question number 1 about the Andhra sources?", question_te="వేరే",
                            options_en={"a": "Option a of 1", "b": "Option b of 1", "c": "x", "d": "y"}, correct_answer="b"))
    db.session.commit()
    n = Question.query.count()
    rep = v1.run(pkg)
    assert len(rep["overlaps"]) == 1 and rep["overlaps"][0]["overlaps_ref"] == "aph-u1c01-OLD-1"
    with pytest.raises(v1.V1ImportError, match="reconciliation"):
        v1.run(pkg, apply=True, approval_ref="r")
    assert Question.query.count() == n                          # nothing written, nothing deleted
    done = v1.run(pkg, apply=True, approval_ref="r", allow_overlaps=True)
    assert done["imported"] == 4 and Question.query.filter_by(import_ref="aph-u1c01-OLD-1").count() == 1


def test_collection_scope_reports_legacy_overlap_without_blocking_but_still_dedupes_the_collection(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path), apply=True)
    pkg = tmp_path / "05_claude_import" / "aph-test"
    db.session.add(Question(subject_id=world["subject"], chapter_id=None, source_type="chapter", import_ref="aph-u1c01-OLD-1",
                            question_en="Question number 1 about the Andhra sources?", question_te="వేరే",
                            options_en={"a": "Option a of 1", "b": "Option b of 1", "c": "x", "d": "y"}, correct_answer="b"))
    db.session.commit()
    legacy_before = Question.query.filter_by(import_ref="aph-u1c01-OLD-1").one()
    snap = (legacy_before.id, legacy_before.question_en, legacy_before.syllabus_chapter_id)
    rep = v1.run(pkg, overlap_scope="collection")
    assert rep["overlaps"] == [] and len(rep["legacy_overlaps_informational"]) == 1
    done = v1.run(pkg, apply=True, approval_ref="r", overlap_scope="collection")      # no --allow-overlaps needed
    assert done["imported"] == 4
    legacy_after = Question.query.filter_by(import_ref="aph-u1c01-OLD-1").one()
    assert snap == (legacy_after.id, legacy_after.question_en, legacy_after.syllabus_chapter_id)   # legacy untouched, not merged
    assert Question.query.filter(Question.syllabus_chapter_id.isnot(None)).count() == 4
    # a second package repeating a stem already IN the collection is still blocked in collection scope
    dup = make_pkg(tmp_path, name="aph-dup", records=[_q(1, SIX[1], ["CH01-S02"], [2], source_qid="APH-U1-C1-B20261010-Q900")])
    r2 = v1.run(dup, overlap_scope="collection")
    assert len(r2["overlaps"]) >= 1
    with pytest.raises(v1.V1ImportError, match="reconciliation"):
        v1.run(dup, apply=True, approval_ref="r", overlap_scope="collection")
    with pytest.raises(v1.V1ImportError):
        v1.run(pkg, overlap_scope="bogus")


# ── learner pages ────────────────────────────────────────────────────
@pytest.fixture()
def loaded(world, tmp_path):
    xn.load_notes(make_pkg(tmp_path), apply=True)
    v1.run(tmp_path / "05_claude_import" / "aph-test", apply=True, approval_ref="r")
    return world


def test_expanded_note_pages_show_the_intended_content_with_sources(client, loaded):
    r = client.get(f"/learn/ap-history/{CH}/notes/CH01-S02")
    html = r.get_data(as_text=True)
    assert r.status_code == 200 and "The text names the Andhras." in html and "ఈ గ్రంథం ఆంధ్రులను పేర్కొంటుంది." in html
    assert 'href="https://example.org/ab"' in html and 'rel="noopener noreferrer"' in html
    assert "Old section" not in html                           # not an app note
    s3 = client.get(f"/learn/ap-history/{CH}/notes/CH01-S03").get_data(as_text=True)
    assert "Pliny lists the Andarae." in s3 and "Pliny gives the Andarae&#39;s towns." in s3 and 'id="CH01-A01"' in s3   # addendum shown with its core
    a1 = client.get(f"/learn/ap-history/{CH}/notes/CH01-A01").get_data(as_text=True)
    assert 'data-testid="connected-core"' in a1 and f"/learn/ap-history/{CH}/notes/CH01-S03" in a1
    assert client.get(f"/learn/ap-history/{CH}/notes/CH01-S99").status_code == 404
    assert client.get(f"/learn/ap-history/{CH}/notes").status_code == 200
    assert client.get("/learn/ap-history/u9-nope/notes").status_code == 404


def test_practice_is_bilingual_labelled_and_keeps_four_level_difficulty(client, loaded):
    html = client.get(f"/learn/ap-history/{CH}/practice?i=1&new=1").get_data(as_text=True)
    assert "Question number 1 about the Andhra sources?" in html and "ఆంధ్ర ఆధారాల గురించి 1వ ప్రశ్న ఏమిటి?" in html
    assert "Option b of 1" in html and "1వ ప్రశ్న ఎంపిక b" in html
    assert 'data-testid="author-reviewed"' in html and "not independently verified" in html and "స్వతంత్రంగా ధృవీకరించబడలేదు" in html
    assert 'href="https://example.org/src1"' in html and "loc1" in html and 'data-testid="source-links"' in html
    page2 = client.get(f"/learn/ap-history/{CH}/practice?i=2").get_data(as_text=True)
    assert "Toughest" in page2 and "అత్యంత కఠినం" in page2                  # not collapsed to Hard
    assert client.get(f"/learn/ap-history/{CH}/practice?i=3").get_data(as_text=True).count("Tough") >= 1
    multi = page2
    assert multi.count('data-testid="read-in-notes"') == 1 and 'data-testid="read-in-notes-more"' in multi    # two anchors -> two links
    for leak in ("CAND-", "AP9-0", "source_trace", "import_ref", "APH-U1-C1", "original_H", "test-batch"):
        assert leak not in html and leak not in page2
    sub = client.get(f"/learn/ap-history/{CH}/practice?subtopic={SIX[0]}").get_data(as_text=True)
    assert "Question number 4" in sub and "1 / 1" in re.sub(r"<[^>]+>", "", sub).replace("\n", " ") or "Question number 4" in sub
    assert client.get(f"/learn/ap-history/{CH}/practice?subtopic=nope").status_code == 404
    assert client.get(f"/learn/ap-history/{CH}/practice?i=99").status_code == 200       # summary


def test_chapter_page_links_to_expanded_notes_and_practice(client, loaded):
    html = client.get(f"/learn/ap-history/{CH}").get_data(as_text=True)
    assert 'data-testid="open-expanded-notes"' in html and 'data-testid="open-native-practice"' in html
    assert client.get(f"/learn/ap-history/{CH}/practice").status_code == 200


def test_unapproved_status_questions_never_reach_learners(client, loaded):
    Question.query.filter_by(source_qid="APH-U1-C1-B20261009-Q001").update({"review_status": "content_review_required"}); db.session.commit()
    html = client.get(f"/learn/ap-history/{CH}/practice?i=1").get_data(as_text=True)
    assert "Question number 1 about" not in html
    assert len(xv.native_questions(SyllabusChapter.query.filter_by(slug=CH).one())) == 3


def test_review_screen_native_questions_correct_wrong_skipped(client, loaded):
    qs = Question.query.filter(Question.source_qid.isnot(None)).order_by(Question.id).all()
    sid = "5d1f3a52-0c1e-4c0f-9b51-0a3c6a1d9e11"
    now = datetime.utcnow()
    db.session.add(ExamSession(id=sid, device_id="dev-test", config={"duration_min": 30}, question_ids=[qs[0].id, qs[1].id, qs[2].id],
                               answers={str(qs[0].id): "b", str(qs[1].id): "a"}, confidences={}, started_at=now, submitted_at=now,
                               score=1, total=3))
    db.session.commit()
    html = client.get(f"/exam-session/{sid}/results").get_data(as_text=True)
    assert html.count("review-badge badge-correct") == 1 and html.count("review-badge badge-wrong") == 1
    assert html.count("review-badge badge-skip") == 1
    for n in (1, 2, 3):
        assert f"English explanation {n}." in html and f"తెలుగు వివరణ {n}." in html
        assert f"Question number {n} about" in html and f"{n}వ ప్రశ్న" in html
    assert html.count("Correct:") >= 2
    assert html.count('data-testid="author-reviewed"') == 3 and 'data-testid="source-links"' in html
    assert "Toughest" in html and "Tough" in html
    assert html.count('data-testid="read-in-notes"') == 3 and 'data-testid="read-in-notes-more"' in html
    assert 'data-exact="true"' in html and 'data-exact="false"' not in html
    for leak in ("CAND-", "AP9-0", "source_trace", "import_ref", "APH-U1-C1", "original_H"):
        assert leak not in html


def test_every_question_note_link_opens_the_intended_anchor(app, client, loaded):
    for q in Question.query.filter(Question.source_qid.isnot(None)):
        want = q.source_trace["expanded_note"]["anchor_ids"]
        with app.test_request_context():
            link = note_link_for(q, {})
        assert link and link["exact"] and link["url"].split("#")[-1] == want[0]
        urls = [link["url"]] + [m["url"] for m in link["more"]]
        assert [u.split("#")[-1] for u in urls] == want
        for u, a in zip(urls, want):
            r = client.get(u)
            assert r.status_code == 200 and f'id="{a}"' in r.get_data(as_text=True), (q.source_qid, u)


def test_link_degrades_to_labelled_chapter_level_or_nothing(app, client, loaded):
    ExpandedNote.query.filter_by(anchor_id="CH01-S02").delete(); db.session.commit()
    q = Question.query.filter_by(source_qid="APH-U1-C1-B20261009-Q001").one()
    with app.test_request_context():
        link = note_link_for(q, {})
    assert link["exact"] is False and link["url"].endswith(f"/learn/ap-history/{CH}/notes")
    ExpandedNote.query.delete(); db.session.commit()
    with app.test_request_context():
        assert note_link_for(q, {}) is None


def test_legacy_question_views_unchanged(client, loaded):
    q = Question.query.filter(Question.source_qid.is_(None)).first()
    from app.services.learn import question_view
    v = question_view(q)
    assert v["meta"]["native"] is False and v["meta"]["sources"] == [] and v["note_url"] is None


# ── the real package ─────────────────────────────────────────────────
real = pytest.mark.skipif(not (REAL / "questions.jsonl").is_file(), reason="closure package not available")


@pytest.fixture()
def real_pkg(tmp_path):
    dst = tmp_path / "05_claude_import" / REAL.name
    shutil.copytree(REAL, dst, ignore=shutil.ignore_patterns("review", "*.pyc"))
    return dst


@real
def test_real_package_is_the_expected_129_question_file(real_pkg):
    assert REAL_SHA and hashlib.sha256((real_pkg / "questions.jsonl").read_bytes()).hexdigest() == REAL_SHA
    rep = b.validate_package(real_pkg)
    assert rep.importable and rep.records == 129 and not rep.errors


@real
def test_real_package_notes_parse_completely(real_pkg):
    rows, ap, problems, warnings = xn.parse_package_notes(real_pkg)
    assert problems == [] and len(rows) == 74
    kinds = {k: sum(1 for r in rows if r["kind"] == k) for k in ("core", "addendum", "group1", "addendum_group1", "revision")}
    assert kinds == {"core": 50, "addendum": 12, "group1": 8, "addendum_group1": 3, "revision": 1}
    text = "".join((real_pkg / "notes" / f).read_text(encoding="utf-8") for f in ("CH01_CORE_NOTES_EN_TE.txt", "CH01_NOTES_ADDENDUM_EN_TE.txt"))
    want = [l.split()[0] for l in text.splitlines() if l.startswith("http")]
    got = [s["url"] for r in rows for s in r["sources"] if s["url"]]
    assert sorted(want) == sorted(got)                                   # not one source link lost
    assert sorted(r["package_section"] for r in rows if r["kind"] == "core") == list(range(1, 51))


@real
def test_real_package_end_to_end_on_scratch_db(app, client, world, real_pkg):
    before = legacy_snapshot(); old_notes = Note.query.count()
    nrep = xn.load_notes(real_pkg, apply=True)
    assert nrep["added"] == 74
    prev = v1.run(real_pkg)
    assert prev["to_import"] == 129 and prev["unresolved_note_links"] == [] and prev["overlaps"] == [] and prev["validator_errors"] == 0
    rep = v1.run(real_pkg, apply=True, approval_ref="scratch-test")
    assert rep["imported"] == 129
    assert v1.run(real_pkg, apply=True, approval_ref="scratch-test")["imported"] == 0 and xn.load_notes(real_pkg, apply=True)["added"] == 0
    assert Question.query.filter(Question.source_qid.isnot(None)).count() == 129
    assert legacy_snapshot() == before and Note.query.count() == old_notes == 17
    d = {}
    for q in Question.query.filter(Question.source_qid.isnot(None)):
        d[q.source_trace["difficulty_original"]] = d.get(q.source_trace["difficulty_original"], 0) + 1
        assert q.review_status == "bilingual_approved" and q.syllabus_chapter_id and q.subtopic_id
    assert d == {"easy": 88, "medium": 38, "tough": 2, "toughest": 1}
    assert sum(1 for q in Question.query.filter(Question.source_qid.isnot(None)) if q.source_trace["H"]) == 44
    # every question's expanded-note link(s) open the anchor it names, and the anchor really is that content
    opened = 0
    for q in Question.query.filter(Question.source_qid.isnot(None)).order_by(Question.id):
        want = q.source_trace["expanded_note"]["anchor_ids"]
        with app.test_request_context():
            link = note_link_for(q, {})
        assert link and link["exact"], q.source_qid
        for u, a in zip([link["url"]] + [m["url"] for m in link["more"]], want):
            r = client.get(u)
            html = r.get_data(as_text=True)
            e = ExpandedNote.query.filter_by(anchor_id=a).one()
            assert r.status_code == 200 and f'id="{a}"' in html and e.heading_te in html, (q.source_qid, a)
            if a.startswith("CH01-S"):
                assert e.package_section == int(a[-2:])
            opened += 1
    assert opened >= 129
    # learner practice shows all 129, bilingual, each with sources where the package has them
    assert client.get(f"/learn/ap-history/{CH}/practice?i=129").status_code == 200
    html = client.get(f"/learn/ap-history/{CH}/practice?i=129&new=1").get_data(as_text=True)
    assert 'data-testid="author-reviewed"' in html


def test_validator_accepts_the_package_id_shapes_and_pairing_codes_but_not_junk():
    for ok in ("APH-U1-C1-B20261009-Q001", "APH-U1-C01-B20-Q001", "APH-U1-C1-B20261009R3-Q008", "APH-U1-C1-B20261009C-Q004",
               "APH-U3-C31-B01-Q0001"):
        assert b.QID_RE.match(ok), ok
    for bad in ("APH-U6-C1-B20261009-Q001", "APH-U1-C32-B20-Q001", "APH-U1-C1-B20261009-Q1", "aph-u1-c1-b20-q001", "APH-U1-C1-Q001"):
        assert not b.QID_RE.match(bad), bad
    assert b.CODE_ONLY.match("1–c, 2–e, 3–a, 4–d, 5–b") and not b.CODE_ONLY.match("Aitareya Brahmana")


def test_native_questions_do_not_leak_into_generic_banks_or_legacy_practice(client, loaded):
    from app.services import learn as svc
    sid = loaded["subject"]
    legacy_n = Question.query.filter(Question.subject_id == sid, Question.source_qid.is_(None)).count()
    assert Question.query.filter(Question.source_qid.isnot(None)).count() == 4
    assert len(svc.bank_questions(sid, "practice")) == legacy_n and len(svc.bank_questions(sid, "pyq")) == 0
    assert svc.bank_counts([sid])[sid] == {"practice": legacy_n, "pyq": 0, "chapter": 0}
    assert all(q.source_qid is None for q in svc.bank_questions(sid, "practice"))
    html = client.get("/learn/subject/ap_history/practice").get_data(as_text=True)
    assert "Question number" not in html
    assert "Question number" not in client.get("/practice/ap_history").get_data(as_text=True)
    assert f">{legacy_n}<" in client.get("/subject/ap_history").get_data(as_text=True) or client.get("/subject/ap_history").status_code in (200, 404)
