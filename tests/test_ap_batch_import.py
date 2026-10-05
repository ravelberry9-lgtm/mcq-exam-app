"""Strict dry-run importer: format, taxonomy, content rules, authorization. Nothing here imports anything."""
import copy
import hashlib
import json
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from app.services import ap_batch_import as b
from app.services import ap_canonical_taxonomy as tax

ROOT = Path(__file__).resolve().parent.parent
CH = "u1-c01-region-people-sources"
SUB = "u1-c01-inscriptions"


def rec(n=1, **kw):
    r = {"source": "codex_generated", "source_qid": f"APH-U1-C01-B01-Q{n:03d}", "batch_id": "B01", "source_file": "batch01.md",
         "chapter_slug": CH, "subtopic_slug": SUB, "microtopic_slugs": ["u1-c01-inscriptions"], "coverage_scope": "direct",
         "difficulty": "easy", "qtype": "Factual", "question_te": f"భట్టిప్రోలు శాసనం గురించి ప్రశ్న {n}?", "question_en": f"Question {n} about the Bhattiprolu inscription?",
         "options": {k: {"te": f"ఎంపిక {k}{n}", "en": f"Option {k}{n}"} for k in "abcd"}, "correct_answer": "b",
         "explanation_te": "వివరణ", "explanation_en": "Explanation", "review_status": "bilingual_approved"}
    r.update(kw)
    return r


def make_package(base, records, **manifest_over):
    pkg = Path(base) / "05_claude_import" / "B01"
    pkg.mkdir(parents=True)
    raw = ("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n").encode("utf-8")
    (pkg / "questions.jsonl").write_bytes(raw)
    m = {"format_version": b.FORMAT_VERSION, "taxonomy_version": tax.TAXONOMY_VERSION, "batch_id": "B01", "source": "codex_generated",
         "question_count": len(records), "questions_sha256": hashlib.sha256(raw).hexdigest(), "content_approval": "bilingual_approved"}
    m.update(manifest_over)
    (pkg / "manifest.json").write_text(json.dumps(m), encoding="utf-8")
    return pkg


def codes(rpt, kind="errors"):
    return set(rpt.codes(kind))


def test_a_clean_package_under_05_claude_import_is_importable_in_dry_run(tmp_path):
    rpt = b.validate_package(make_package(tmp_path, [rec(1), rec(2, correct_answer="c")]))
    assert rpt.errors == [] and rpt.importable and rpt.records == 2
    assert rpt.info["answer_distribution"] == {"A": 0, "B": 1, "C": 1, "D": 0}


def test_package_outside_import_dir_or_in_drafts_is_never_importable(tmp_path):
    pkg = make_package(tmp_path, [rec(1)])
    outside = tmp_path / "elsewhere" / "B01"
    outside.parent.mkdir()
    pkg.rename(outside)
    assert "outside_import_dir" in codes(b.validate_package(outside))
    drafts = tmp_path / "02_drafts" / "05_claude_import" / "B01"
    drafts.parent.mkdir(parents=True)
    outside.rename(drafts)
    r = b.validate_package(drafts)
    assert not r.importable and "draft_folder" in codes(r)


@pytest.mark.parametrize("change,code", [
    ({"review_status": "fact_verified"}, "not_approved"), ({"source": "chatgpt"}, "bad_source"), ({"source_qid": "C01-B01-001"}, "bad_id_format"),
    ({"difficulty": "hard"}, "bad_difficulty"), ({"coverage_scope": "mixed"}, "bad_coverage_scope"), ({"correct_answer": "e"}, "bad_answer"),
    ({"question_te": "Only English text"}, "telugu_missing"), ({"question_en": "ఇంగ్లీష్ లేదు"}, "english_missing"),
    ({"chapter_slug": "u9-c99-nope"}, "unknown_chapter"), ({"subtopic_slug": "u1-c01-nope"}, "unknown_subtopic"),
    ({"subtopic_slug": "u1-c02-palaeolithic-mesolithic"}, "subtopic_chapter_mismatch"),
    ({"subtopic_slug": None}, "missing_subtopic"), ({"microtopic_slugs": ["u1-c01-nope"]}, "unknown_microtopic"),
    ({"microtopic_slugs": ["u1-c01-coins"]}, "microtopic_subtopic_mismatch"), ({"secondary_chapters": [CH]}, "secondary_equals_primary"),
    ({"explanation_te": ""}, "missing_field"), ({"options": {"a": {"te": "అ", "en": "A"}}}, "bad_options"),
])
def test_each_rule_is_enforced(tmp_path, change, code):
    assert code in codes(b.validate_package(make_package(tmp_path, [rec(1, **change)])))


def test_options_must_be_bilingual_distinct_and_codes_may_be_language_neutral(tmp_path):
    bad = rec(1)
    bad["options"]["a"] = {"te": "same", "en": "same"}
    assert "option_not_bilingual" in codes(b.validate_package(make_package(tmp_path / "x", [bad])))
    dup = rec(2)
    dup["options"]["b"] = dict(dup["options"]["a"])
    assert "duplicate_options" in codes(b.validate_package(make_package(tmp_path / "y", [dup])))
    ok = rec(3)
    ok["options"] = {"a": {"te": "A-3, B-2, C-1, D-4", "en": "A-3, B-2, C-1, D-4"}, "b": {"te": "A-2, B-3, C-4, D-1", "en": "A-2, B-3, C-4, D-1"},
                     "c": {"te": "A-1, B-4, C-2, D-3", "en": "A-1, B-4, C-2, D-3"}, "d": {"te": "A-4, B-1, C-3, D-2", "en": "A-4, B-1, C-3, D-2"}}
    assert b.validate_package(make_package(tmp_path / "z", [ok])).errors == []


def test_manifest_checksum_count_and_versions_are_enforced(tmp_path):
    assert "checksum" in codes(b.validate_package(make_package(tmp_path / "a", [rec(1)], questions_sha256="0" * 64)))
    assert "question_count" in codes(b.validate_package(make_package(tmp_path / "b", [rec(1)], question_count=5)))
    assert "taxonomy_version" in codes(b.validate_package(make_package(tmp_path / "c", [rec(1)], taxonomy_version="v0")))
    assert "content_approval" in codes(b.validate_package(make_package(tmp_path / "d", [rec(1)], content_approval="raw")))
    assert "format_version" in codes(b.validate_package(make_package(tmp_path / "e", [rec(1)], format_version="x")))
    assert "batch_mismatch" in codes(b.validate_package(make_package(tmp_path / "f", [rec(1, batch_id="B99")])))
    assert "duplicate_source_qid" in codes(b.validate_package(make_package(tmp_path / "g", [rec(1), rec(1)])))
    # file edited after the manifest was written
    pkg = make_package(tmp_path / "h", [rec(1)])
    (pkg / "questions.jsonl").write_text((pkg / "questions.jsonl").read_text(encoding="utf-8") + "\n", encoding="utf-8")
    assert b.validate_package(pkg).importable is False


def test_content_hash_collisions_warn_but_never_discard(tmp_path):
    a, c = rec(1), rec(2)
    for k in ("question_te", "question_en", "options"):
        c[k] = copy.deepcopy(a[k])
    rpt = b.validate_package(make_package(tmp_path, [a, c]))
    assert rpt.errors == [] and "content_hash_collision" in codes(rpt, "warnings") and rpt.records == 2


def test_database_duplicates_are_detected_read_only(tmp_path):
    db = tmp_path / "c.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE questions (id INTEGER PRIMARY KEY, source TEXT, source_qid TEXT, content_hash TEXT)")
    r = rec(1)
    con.execute("INSERT INTO questions (source, source_qid, content_hash) VALUES (?,?,?)", ("codex_generated", r["source_qid"], b.content_hash(r)))
    con.execute("INSERT INTO questions (source, source_qid, content_hash) VALUES (?,?,?)", ("app_master", "X", b.content_hash(rec(2))))
    con.commit(); con.close()
    before = db.read_bytes()
    rpt = b.validate_package(make_package(tmp_path / "p", [r, rec(2)]), db_path=str(db))
    assert "already_imported" in codes(rpt) and "content_hash_collision_db" in codes(rpt, "warnings")
    assert db.read_bytes() == before                      # opened read-only: unchanged
    legacy = tmp_path / "old.db"
    sqlite3.connect(legacy).execute("CREATE TABLE questions (id INTEGER PRIMARY KEY, question_en TEXT)").connection.close()
    assert b.validate_package(make_package(tmp_path / "q", [rec(1)]), db_path=str(legacy)).errors == []


def test_scope_rules_follow_the_fact_tested_not_the_note(tmp_path):
    q = rec(1, chapter_slug="u2-c13-qutb-shahis", subtopic_slug="u2-c13-establishment-rulers", microtopic_slugs=["u2-c13-post-1600-context"])
    assert "scope_mismatch" in codes(b.validate_package(make_package(tmp_path / "a", [q])))
    q["coverage_scope"] = "supplementary_context"
    assert b.validate_package(make_package(tmp_path / "b", [q])).errors == []
    sup = rec(2, chapter_slug="supp-asaf-jahis-hyderabad-state", subtopic_slug="u1-c01-inscriptions")
    assert "subtopic_on_supplementary" in codes(b.validate_package(make_package(tmp_path / "c", [sup])))
    sup2 = rec(3, chapter_slug="supp-asaf-jahis-hyderabad-state", subtopic_slug=None, coverage_scope="supplementary_context", microtopic_slugs=[])
    r = b.validate_package(make_package(tmp_path / "d", [sup2]))
    assert r.errors == [], r.errors


def test_kataya_vema_komaram_bheem_and_rampa_rules(tmp_path):
    kv = rec(1, question_en="Which Reddi ruler was Kataya Vema?")
    assert "content_blocked" in codes(b.validate_package(make_package(tmp_path / "a", [kv])))
    kv_te = rec(2, question_te="కటయ వేమ ఎవరు?")
    assert "content_blocked" in codes(b.validate_package(make_package(tmp_path / "b", [kv_te])))
    kb = rec(3, question_en="Komaram Bheem resisted which administration?")
    assert "komaram_bheem_mapping" in codes(b.validate_package(make_package(tmp_path / "c", [kb])))
    ok = rec(4, question_en="Komaram Bheem resisted which administration?", chapter_slug="supp-asaf-jahis-hyderabad-state", subtopic_slug=None,
             microtopic_slugs=[], secondary_chapters=["u4-c26-folk-tribal-culture"], coverage_scope="supplementary_context")
    assert b.validate_package(make_package(tmp_path / "d", [ok])).errors == []
    ramp = rec(5, question_en="The Rampa Rebellion of 1922 was led by whom?")
    assert "rampa_mapping" in codes(b.validate_package(make_package(tmp_path / "e", [ramp])), "warnings")


def test_non_normalized_telugu_terms_warn(tmp_path):
    q = rec(1, question_te="ఉత్తర సర్కారులు ఏవి?")
    assert "non_normalized_term" in codes(b.validate_package(make_package(tmp_path, [q])), "warnings")


DRAFT = """# Unit 1 · Chapter 1 · Batch 01A

**Status:** Review draft — not yet approved for import  
**Source:** `codex_generated`

---

### C01-B01-001 · Easy · Factual

**TE:** శాసనాలను అధ్యయనం చేసే శాస్త్రం ఏది?  
**EN:** What is the study of inscriptions called?

A. నాణెపు శాస్త్రం / Numismatics  
B. శాసన శాస్త్రం / Epigraphy  
C. పురాలిపి శాస్త్రం / Palaeography  
D. పురావస్తు శాస్త్రం / Archaeology

**Answer: B**

**TE వివరణ:** శాసన పాఠ్యాన్ని అధ్యయనం చేస్తుంది.  
**EN Explanation:** Epigraphy studies inscriptions.

### C01-B01-002 · Tough · Matching

**TE:** జతపరచండి:  
A. శాసన శాస్త్రం  1. నాణేలు  
B. నాణెపు శాస్త్రం  2. శాసనాలు  
**EN:** Match:  
A. Epigraphy  1. Coins  
B. Numismatics  2. Inscriptions

A. A-2, B-1  
B. A-1, B-2  
C. Both  / రెండూ  
D. Neither / రెండూ కావు

**Answer: A**

**TE వివరణ:** శాసనాలు శాసన శాస్త్రం.  
**EN Explanation:** Inscriptions belong to epigraphy.

---
## Draft audit snapshot
"""


def test_draft_markdown_is_parsed_for_a_report_but_is_never_importable(tmp_path):
    f = tmp_path / "Batch01A.md"
    f.write_text(DRAFT, encoding="utf-8")
    rpt, recs = b.validate_draft_files([f])
    assert rpt.records == 2 and not rpt.importable and "draft_not_importable" in codes(rpt)
    assert recs[0]["options"]["b"] == {"te": "శాసన శాస్త్రం", "en": "Epigraphy"} and recs[0]["correct_answer"] == "b"
    assert "A. Epigraphy" in recs[1]["question_en"] and recs[1]["options"]["a"]["te"] == "A-2, B-1"
    assert rpt.info["parsed"]["with_four_options"] == 2 and rpt.info["parsed"]["with_both_explanations"] == 2
    assert "draft_id_format" in codes(rpt, "warnings")


def test_cli_exit_codes_and_no_apply_mode(tmp_path):
    f = tmp_path / "Batch01A.md"
    f.write_text(DRAFT, encoding="utf-8")
    run = lambda *a: subprocess.run([sys.executable, str(ROOT / "scripts" / "ap_batch_import.py"), *a], capture_output=True, text=True, cwd=ROOT)  # noqa: E731
    assert run("drafts", str(f)).returncode == 2
    pkg = make_package(tmp_path / "ok", [rec(1)])
    assert run("package", str(pkg)).returncode == 0
    assert run("package", str(pkg), "--apply").returncode != 0               # there is no apply flag
    assert not [n for n in dir(b) if callable(getattr(b, n)) and ("apply" in n.lower() or n.lower().startswith("import_"))]
    src = (ROOT / "app" / "services" / "ap_batch_import.py").read_text(encoding="utf-8")
    assert "INSERT" not in src.upper().replace("INSERT-ONLY", "") and "commit(" not in src and "session" not in src.lower()


def test_converted_ids_and_chapter_level_fallback_are_accepted_only_when_marked(tmp_path):
    ok = rec(1, source_qid="aph-u1c01-AP9-00004", converted_from="AP_History_U1_C01_Import_Ready.jsonl", subtopic_slug="", subtopic_fallback=True)
    bare = rec(2, source_qid="aph-u1c01-AP9-00005", subtopic_slug="")          # no converted_from, no fallback flag
    rpt = b.validate_package(make_package(tmp_path, [ok, bare]))
    assert {"converted_import_ref_id", "chapter_level_fallback"} <= codes(rpt, "warnings")
    errs = [(e["id"], e["code"]) for e in rpt.to_dict()["errors"]]
    assert ("aph-u1c01-AP9-00005", "bad_id_format") in errs and ("aph-u1c01-AP9-00005", "missing_subtopic") in errs
    assert not [e for e in errs if e[0] == "aph-u1c01-AP9-00004"]


def test_converter_writes_only_preview_packages_and_refuses_the_import_folder(tmp_path):
    src = tmp_path / "05_claude_import"; src.mkdir()
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "convert_prepared_to_v1.py"), str(src), "--out", str(src / "x")],
                       capture_output=True, text=True)
    assert r.returncode != 0 and "refusing" in (r.stderr + r.stdout)
