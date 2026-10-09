"""Native ``ap-history-import-v1`` importer (preview by default; apply only with an explicit approval reference).

Built on the strict validator in ``ap_batch_import`` (taxonomy, bilingual completeness, approval status, manifest checksum,
authorized folder ``05_claude_import``). Add-only, single transaction, idempotent through the unique ``(source, source_qid)`` pair.

What is preserved, and where
* ``source_qid`` / ``source`` / ``batch_id`` / ``source_file`` / ``qtype`` / ``review_status`` -> the canonical provenance columns.
* ``chapter_slug`` / ``subtopic_slug`` -> ``syllabus_chapter_id`` / ``subtopic_id`` (resolved by slug in THIS database; no ids are trusted).
* ``secondary_chapters`` / ``microtopic_slugs`` / ``coverage_scope`` -> ``secondary_tags`` (JSON).
* ``H``, ``sources``, ``expanded_note``, original four-level ``difficulty`` and calibration note, the package hash and the
  author-review basis -> ``source_trace`` (JSON). The four-level difficulty is kept exactly; the legacy single-letter column only
  receives the coarse display value (easy->E, medium->M, tough/toughest->H) and learner pages read the four-level value.
* Author-reviewed status is stored as ``review_status = bilingual_approved`` plus ``source_trace.content_approval``; it is never
  recorded as independent verification (``fact_verified``).

Nothing existing is updated or deleted. A record that overlaps an existing question (same stem, or near-identical stem with the
same correct answer) is reported and, unless ``allow_overlaps`` is set, blocks the apply so a human can reconcile first.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path

from sqlalchemy.exc import IntegrityError

from ..db import db
from ..models import (ExpandedNote, Question, Subject, SyllabusChapter, SyllabusSubtopic, SyllabusMicrotopic)
from . import ap_batch_import as b
from . import ap_canonical_taxonomy as tax
from . import mcq_import as legacy

DIFF_DISPLAY = {"easy": "E", "medium": "M", "tough": "H", "toughest": "H"}
APPROVAL_NOTE_KEY = "content_approval_note"


class V1ImportError(Exception):
    pass


def _flat(rec, lang):
    return {k: (rec["options"][k] or {}).get(lang) for k in b.OPTION_KEYS}


def _as_legacy_shape(rec):
    return {"question_en": rec["question_en"], "question_te": rec["question_te"], "options_en": _flat(rec, "en"),
            "options_te": _flat(rec, "te"), "correct_answer": rec["correct_answer"]}


def _trace(rec, manifest, pkg_sha):
    t = rec.get("source_trace") or {}
    return {
        "format_version": manifest.get("format_version"), "taxonomy_version": manifest.get("taxonomy_version"),
        "package_questions_sha256": pkg_sha,
        APPROVAL_NOTE_KEY: manifest.get("approval_note"), "approval_basis": rec.get("approval_basis"),
        "candidate_id": t.get("candidate_id"), "source_ids": t.get("source_ids"), "original_H": t.get("original_H"),
        "H": rec.get("H", ""), "coverage_scope": rec.get("coverage_scope"),
        "difficulty_original": rec.get("difficulty"), "difficulty_calibration": rec.get("difficulty_calibration"),
        "sources": rec.get("sources") or [], "expanded_note": rec.get("expanded_note"),
        "selection_role": rec.get("selection_role"), "related_old_package_refs": rec.get("related_old_package_refs"),
        "editorial_change": rec.get("editorial_change"), "previous_batch_id": rec.get("previous_batch_id"),
        "retained_from_batch": rec.get("retained_from_batch"),
    }


def run(pkg_dir, apply=False, approval_ref=None, allow_overlaps=False, overlap_scope="all"):
    """Preview (default) or apply one v1 package. Returns a report dict; raises ``V1ImportError`` for a refusal.

    ``overlap_scope``: ``all`` (default) checks every existing question of the subject and blocks apply on any overlap.
    ``collection`` is for the fresh AP History collection: only questions already in the native collection
    (``syllabus_chapter_id`` set) can block an apply; overlaps with legacy-bank questions are still listed, as
    ``legacy_overlaps_informational``, and never imported-over, merged or modified. The guard itself stays on in both modes.
    """
    if overlap_scope not in ("all", "collection"):
        raise V1ImportError("overlap_scope must be 'all' or 'collection'")
    pkg = Path(pkg_dir)
    vrep = b.validate_package(pkg)
    rep = {"package": pkg.name, "records": vrep.records, "validator_errors": len(vrep.errors), "validator_warnings": len(vrep.warnings),
           "applied": bool(apply), "to_import": 0, "imported": 0, "already_imported": 0, "overlaps": [], "legacy_overlaps_informational": [], "overlap_scope": overlap_scope, "unresolved_note_links": [],
           "warnings": [], "difficulty": {}, "content_approval": "author-reviewed (bilingual_approved); not independently verified"}
    if not vrep.importable:
        rep["validator_first_errors"] = vrep.errors[:10]
        raise V1ImportError(f"package refused by the strict validator ({len(vrep.errors)} error(s); first: "
                            f"{vrep.errors[0]['code'] if vrep.errors else vrep.mode})")
    if apply and not (approval_ref or "").strip():
        raise V1ImportError("apply needs an explicit import approval reference (--approval-ref); nothing was written")
    manifest = json.loads((pkg / "manifest.json").read_text(encoding="utf-8"))
    raw = (pkg / "questions.jsonl").read_bytes()
    pkg_sha = hashlib.sha256(raw).hexdigest()
    recs = [json.loads(l) for l in raw.decode("utf-8").splitlines() if l.strip()]

    # canonical structure: resolved by slug in this database, and checked against the approved taxonomy in code
    chap_slugs = {r["chapter_slug"] for r in recs} | {c for r in recs for c in (r.get("secondary_chapters") or [])}
    chapters = {c.slug: c for c in SyllabusChapter.query.filter(SyllabusChapter.slug.in_(chap_slugs)).all()}
    missing = sorted(chap_slugs - set(chapters))
    if missing:
        raise V1ImportError(f"canonical chapter(s) not seeded in this database: {missing}; seed the canonical structure first")
    sub_slugs = {r["subtopic_slug"] for r in recs if r.get("subtopic_slug")}
    subs = {s.slug: s for s in SyllabusSubtopic.query.filter(SyllabusSubtopic.slug.in_(sub_slugs)).all()}
    missing = sorted(sub_slugs - set(subs))
    if missing:
        raise V1ImportError(f"canonical subtopic(s) not seeded in this database: {missing}; seed the canonical taxonomy first")
    code_subs = {sb["slug"] for subs_ in tax.build().values() for sb in subs_}
    for slug, s in subs.items():
        if slug not in code_subs:
            raise V1ImportError(f"subtopic {slug!r} is not in {tax.TAXONOMY_VERSION}")
        if s.chapter_id != chapters[next(r["chapter_slug"] for r in recs if r.get("subtopic_slug") == slug)].id:
            raise V1ImportError(f"subtopic {slug!r} belongs to a different chapter in this database")
        if s.taxonomy_version not in (None, manifest.get("taxonomy_version")):
            rep["warnings"].append(f"subtopic {slug} carries taxonomy_version {s.taxonomy_version}, package says {manifest.get('taxonomy_version')}")
    micro_slugs = {m for r in recs for m in (r.get("microtopic_slugs") or [])}
    if micro_slugs:
        have = {m.slug for m in SyllabusMicrotopic.query.filter(SyllabusMicrotopic.slug.in_(micro_slugs)).all()}
        if micro_slugs - have:
            raise V1ImportError(f"canonical microtopic(s) not seeded: {sorted(micro_slugs - have)}")
    subject_ids = {c.subject_id for c in chapters.values()}
    if len(subject_ids) != 1:
        raise V1ImportError("the package's chapters span more than one subject")
    subject_id = subject_ids.pop()
    if db.session.get(Subject, subject_id) is None:
        raise V1ImportError("subject not found")

    # notes: every expanded-note anchor a question names must exist in the loaded collection
    have_anchors = {a for (a,) in db.session.query(ExpandedNote.anchor_id).filter(ExpandedNote.subject_id == subject_id)}
    existing = {(s, q) for (s, q) in db.session.query(Question.source, Question.source_qid).filter(Question.source_qid.isnot(None))}
    index = legacy._existing_index(subject_id)
    native_ids = {i for (i,) in db.session.query(Question.id).filter(Question.syllabus_chapter_id.isnot(None))}
    refs = {e["ref"]: e for e in index if e["ref"]}
    rows, seen = [], []
    for r in recs:
        if (r["source"], r["source_qid"]) in existing:
            rep["already_imported"] += 1
            continue
        for aid in (r.get("expanded_note") or {}).get("anchor_ids") or []:
            if aid not in have_anchors:
                rep["unresolved_note_links"].append({"source_qid": r["source_qid"], "anchor_id": aid})
        shaped = _as_legacy_shape(r)
        def _bucket(eid):
            # in collection scope only members of the native collection (or this batch, id None) can block
            return rep["overlaps"] if (overlap_scope == "all" or eid is None or eid in native_ids) else rep["legacy_overlaps_informational"]
        if overlap_scope == "collection":
            # checked separately, so a legacy match can never mask a duplicate inside the collection
            sets = [[e for e in index if e["id"] is None or e["id"] in native_ids],
                    [e for e in index if e["id"] is not None and e["id"] not in native_ids]]
        else:
            sets = [index]
        for part in sets:
            dup, why = legacy._dup_of(shaped, part)
            if dup:
                _bucket(dup["id"]).append({"source_qid": r["source_qid"], "overlaps_question_id": dup["id"],
                                           "overlaps_ref": dup["ref"], "reason": why})
        for old in r.get("related_old_package_refs") or []:
            if old in refs:
                _bucket(refs[old]["id"]).append({"source_qid": r["source_qid"], "overlaps_question_id": refs[old]["id"], "overlaps_ref": old,
                                                 "reason": "related_old_package_refs names a question already in this database"})
        ch = chapters[r["chapter_slug"]]
        sb = subs.get(r.get("subtopic_slug"))
        row = Question(
            subject_id=subject_id, chapter_id=None, source_type="chapter", q_hash=legacy.q_hash(shaped),
            difficulty=DIFF_DISPLAY[r["difficulty"]], question_en=r["question_en"].strip(), question_te=r["question_te"].strip(),
            options_en=_flat(r, "en"), options_te=_flat(r, "te"), correct_answer=r["correct_answer"],
            explanation_en=r["explanation_en"].strip(), explanation_te=r["explanation_te"].strip(),
            note_section_num=None, note_target_slug=r.get("subtopic_slug") or r["chapter_slug"],
            source_trace=_trace(r, manifest, pkg_sha), import_ref=r["source_qid"],
            syllabus_chapter_id=ch.id, subtopic_id=sb.id if sb else None,
            secondary_tags={"chapters": r.get("secondary_chapters") or [], "microtopics": r.get("microtopic_slugs") or [],
                            "coverage_scope": r["coverage_scope"]},
            source=r["source"], source_file=r.get("source_file"), source_qid=r["source_qid"], qtype=r["qtype"],
            review_status=r["review_status"], batch_id=r["batch_id"], content_hash=b.content_hash(r))
        rows.append(row)
        rep["difficulty"][r["difficulty"]] = rep["difficulty"].get(r["difficulty"], 0) + 1
        index.append({"id": None, "ref": r["source_qid"], "stem": legacy.norm(r["question_en"]), "tok": legacy._tokens(r["question_en"]),
                      "ans": legacy._answer_text(shaped, "en"), "ans_te": legacy._answer_text(shaped, "te"),
                      "stem_te": legacy.norm(r["question_te"])})
    rep["to_import"] = len(rows)
    rep["by_subtopic"] = dict(Counter(r.get("subtopic_slug") for r in recs))
    if apply:
        if rep["unresolved_note_links"]:
            raise V1ImportError(f"{len(rep['unresolved_note_links'])} question note link(s) point at anchors not loaded in this "
                                f"database; load the package notes first. Nothing was written")
        if rep["overlaps"] and not allow_overlaps:
            raise V1ImportError(f"{len(rep['overlaps'])} overlap(s) with existing questions need reconciliation first "
                                f"(pass --allow-overlaps only after deciding). Nothing was written")
        if rows:
            try:
                db.session.add_all(rows)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                raise V1ImportError("a (source, source_qid) pair already exists; nothing was written")
            except Exception:
                db.session.rollback()
                raise
            rep["imported"] = len(rows)
        rep["approval_ref"] = approval_ref
    return rep
