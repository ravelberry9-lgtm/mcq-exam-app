"""Convert prepared F-shape packages (05_claude_import/*_Import_Ready.jsonl) into ap-history-import-v1 PREVIEW packages.

Read-only on the inputs; writes only to --out (default: <project>/_converted_v1_preview, never 05_claude_import).
Lossy / assumed fields are listed in each manifest ("conversion_notes") and flagged per record. Nothing is imported.

    python scripts/convert_prepared_to_v1.py <05_claude_import dir> [--out DIR]
"""
import argparse, hashlib, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app.services import ap_canonical as canon, ap_canonical_taxonomy as tax

DIFF = {"E": "easy", "M": "medium", "H": "tough"}            # H -> tough is a guess: E/M/H cannot distinguish tough from toughest
SOURCE = {"AP_MASTER": "app_master", "CODEX_DRAFT": "codex_generated", "BENCHMARK_APPROVED": "codex_generated"}
NOTES = ["difficulty: E->easy, M->medium, H->tough (lossy; 'toughest' not recoverable)",
         "coverage_scope defaulted to 'direct' for every record: needs review",
         "review_status is content_review_required unless --approve is given (the approval note is recorded in the manifest)",
         "secondary_chapters and microtopic_slugs left empty (not in the prepared files)",
         "qtype is 'unspecified' (not in the prepared files)",
         "source_qid is the prepared import_ref; BENCHMARK_APPROVED maps to codex_generated (approximate)"]


def sha(b): return hashlib.sha256(b).hexdigest()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--out"); ap.add_argument("--approve", action="append", default=[], help="project chapter to mark bilingual_approved, e.g. U1-C01 (repeatable); only these chapters are converted")
    ap.add_argument("--approval-note", default="")
    a = ap.parse_args()
    src = Path(a.src)
    out = Path(a.out) if a.out else src.parent / "_converted_v1_preview"
    if "05_claude_import" in out.parts or "02_drafts" in out.parts:
        sys.exit("refusing to write inside 05_claude_import or 02_drafts")
    chap = {c[1]: c[2] for c in canon.CHAPTERS}   # keyed by chapter number: the prepared files label C09 as U1 but it is canonical unit 2
    old = tax.old_to_new(); subs = set()
    for ch in tax.build().values():
        def walk(o):
            if isinstance(o, dict):
                if isinstance(o.get("slug"), str): subs.add(o["slug"])
                for v in o.values(): walk(v)
            elif isinstance(o, (list, tuple)):
                for v in o: walk(v)
        walk(ch)
    summary = []
    if a.approve and not a.approval_note:
        sys.exit("--approve needs --approval-note saying who approved and when")
    for f in sorted(src.glob("AP_History_U*_C*_Import_Ready.jsonl")):
        man = json.loads(f.with_name(f.name.replace("Import_Ready.jsonl", "Import_Manifest.json")).read_text(encoding="utf-8"))
        if a.approve and not any(f.name.startswith("AP_History_%s_" % x.replace("-", "_")) for x in a.approve):
            continue
        groups = {}
        for line in f.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            ch = chap[int(r["project_chapter"].split("-C")[1])]
            origin = r["source_trace"].get("origin")
            source = SOURCE[origin]
            t = r.get("note_target_slug")
            sub = old[t][0] if t in old else (t if (t in subs and t != ch and t.startswith(ch[:7])) else "")
            rec = {"source": source, "source_qid": r["import_ref"], "batch_id": None, "source_file": man["source_file"],
                   "chapter_slug": ch, "subtopic_slug": sub, "coverage_scope": "direct", "difficulty": DIFF[r["difficulty"]],
                   "qtype": "unspecified", "question_te": r["question_te"], "question_en": r["question_en"],
                   "options": {k: {"te": r["options_te"][k], "en": r["options_en"][k]} for k in "abcd"},
                   "correct_answer": r["correct_answer"], "explanation_te": r["explanation_te"], "explanation_en": r["explanation_en"],
                   "review_status": "bilingual_approved" if a.approve else "content_review_required", "secondary_chapters": [], "microtopic_slugs": [],
                   "converted_from": f.name, "source_trace": r["source_trace"], "note_target_slug": t,
                   "note_section_num": r.get("note_section_num"), "note_link_status": r.get("note_link_status"),
                   "legacy_difficulty": r["difficulty"], "coverage_scope_review": True}
            if not sub: rec["subtopic_fallback"] = True
            groups.setdefault(source, []).append(rec)
        for source, recs in groups.items():
            batch = f"{f.name.split('_Import_Ready')[0].lower().replace('ap_history_', 'aph-')}-{source}".replace("_", "-")
            for r in recs: r["batch_id"] = batch
            body = ("\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in recs) + "\n").encode("utf-8")
            d = out / batch; d.mkdir(parents=True, exist_ok=True)
            (d / "questions.jsonl").write_bytes(body)
            manifest = {"format_version": "ap-history-import-v1", "taxonomy_version": tax.TAXONOMY_VERSION, "batch_id": batch, "source": source,
                        "question_count": len(recs), "questions_sha256": sha(body), "content_approval": "bilingual_approved" if a.approve else "content_review_required", "approval_note": a.approval_note,
                        "converted_from": f.name, "prepared_sha256": sha(f.read_bytes()), "origin_source_sha256": man.get("source_sha256"),
                        "conversion_notes": NOTES}
            (d / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
            summary.append((batch, len(recs), sum(1 for r in recs if r.get("subtopic_fallback"))))
    for s in summary: print("%-34s %4d records  %3d chapter-level fallback" % s)
    print("total", sum(s[1] for s in summary))


if __name__ == "__main__":
    main()
