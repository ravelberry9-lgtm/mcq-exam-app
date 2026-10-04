"""Build the DRAFT note-section -> canonical mapping review files (read-only; touches no database).

    python scripts/build_ap_note_mapping_draft.py          # writes docs/ap_history_note_mapping_draft.{csv,md}

Inputs: data/content.db.gz (AP History source chapters 1-12, as loaded into the app) and scripts/ap_source_sections_13_19.json
(section structure of the local HTML chapter files 13-19, produced by snapshot_ap_sections_13_19.py), plus scripts/ap_note_mapping_spec.py.
"""
import csv
import gzip
import json
import shutil
import sqlite3
import sys
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.services import ap_canonical as canon          # noqa: E402
from app.services import ap_canonical_taxonomy as tax  # noqa: E402
import ap_note_mapping_spec as spec                      # noqa: E402

COLUMNS = ["source", "old_chapter_id", "old_chapter_num", "old_chapter_title", "note_id", "section_num", "heading_en", "heading_te",
           "canonical_unit", "canonical_chapter_num", "canonical_chapter_slug", "canonical_chapter_title_en",
           "proposed_subtopic_slug", "proposed_subtopic_en", "proposed_microtopic_slug", "proposed_microtopic_en", "draft_subtopic_slug",
           "coverage_scope", "confidence", "mapping_kind", "multi_topic", "flags", "approval_status",
           "needs_review", "content_use", "reason", "secondary_mappings", "secondary_microtopics"]
SECTIONS_JSON = ROOT / "scripts" / "ap_source_sections_13_19.json"


def load_notes(path=ROOT / "data" / "content.db.gz"):
    """Source chapters 1-12 from the bundled content database: (chapter id, num, title, note id, section, heading_en, heading_te)."""
    tmp = Path(tempfile.mkdtemp()) / "c.db"
    with gzip.open(path, "rb") as src, open(tmp, "wb") as dst:
        shutil.copyfileobj(src, dst)
    con = sqlite3.connect(tmp)
    rows = con.execute(
        "SELECT c.id, c.chapter_num, c.title_en, n.id, n.section_num, n.heading_en, n.heading_te FROM notes n "
        "JOIN chapters c ON c.id = n.chapter_id JOIN subjects s ON s.id = c.subject_id WHERE s.slug = 'ap_history' "
        "ORDER BY c.chapter_num, n.section_num").fetchall()
    con.close()
    return rows


def load_html_sections(path=SECTIONS_JSON):
    """Source chapters 13-19 from the snapshot of the local HTML files: same tuple shape, with no database ids."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    rows = []
    for num in sorted(data, key=int):
        ch = data[num]
        for s in ch["sections"]:
            rows.append((None, int(num), ch["title"], None, s["section_num"], s["heading_en"], s["heading_te"]))
    return rows


def all_rows():
    return load_notes() + load_html_sections()


def chapter_index():
    by_num = {num: (unit, slug, en, cls) for unit, num, slug, en, _te, cls in canon.CHAPTERS}
    by_slug = {slug: (unit, num, slug, en, cls) for unit, num, slug, en, _te, cls in canon.CHAPTERS}
    supp = {slug: (None, None, slug, en, "supplementary") for slug, en, _te, _k, _s in canon.SUPPLEMENTARY}
    return by_num, {**by_slug, **supp}


def resolve(ref, by_num, by_slug):
    """canonical chapter number or supplementary slug -> (unit, num, slug, title_en, classification)"""
    if isinstance(ref, int):
        unit, slug, en, cls = by_num[ref]
        return unit, ref, slug, en, cls
    return by_slug[ref]


def kind_for(slug, cls):
    if cls == "supplementary":
        kinds = {s: k for s, _e, _t, k, _src in canon.SUPPLEMENTARY}
        return "cross_cutting" if kinds[slug] == "supplementary_cross_cutting" else "supplementary"
    return {"direct": "direct", "bridge": "bridge", "thematic": "direct"}[cls]


def _majority(rows):
    """For source chapters spanning several canonical chapters: the canonical chapter that gets most substantive sections
    (ties go to the earliest chapter number)."""
    counts = {}
    for _c, cnum, _t, _n, snum, _hen, _hte in rows:
        e = spec.SPEC.get((cnum, snum))
        if e and e[0] != spec.AID and isinstance(e[0], int):
            counts.setdefault(cnum, Counter())[e[0]] += 1
    return {c: sorted(k.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] for c, k in counts.items()}


def build(rows=None):
    rows = rows or all_rows()
    by_num, by_slug = chapter_index()
    micro = {m["slug"]: (sb, m) for subs in tax.build().values() for sb in subs for m in sb["micros"]}
    majority = _majority(rows)
    span = {c: len({e[0] for (cc, ss), e in spec.SPEC.items() if cc == c and isinstance(e[0], int)}) for c in {r[1] for r in rows}}
    out = []
    for cid, cnum, ctitle, nid, snum, hen, hte in rows:
        entry = spec.SPEC.get((cnum, snum))
        generic = False
        if entry is None:
            if (hen or "").strip() not in spec.GENERIC_HEADINGS:
                raise SystemExit(f"unmapped non-generic section: chapter {cnum} section {snum} {hen!r}")
            generic = True
            ref, st, conf, reason, secs = spec.DEFAULT_CHAPTER[cnum], None, "high", spec.GENERIC_REASON, []
        else:
            ref, st, conf, reason, secs = entry
        flags = [f for f in spec.FLAGS.get((cnum, snum), "").split(";") if f]
        if ref in (spec.MAJORITY, spec.AID):
            ref = majority[cnum]
            conf, reason = "medium", reason + " Assigned to the canonical chapter that receives most of this source chapter's sections."
            flags.append("multi_topic")
        elif generic and span.get(cnum, 1) > 1:
            conf = "medium"; flags.append("multi_topic")
        unit, num, slug, en, cls = resolve(ref, by_num, by_slug)
        prefix = None if slug.startswith("supp-") else "-".join(slug.split("-")[:2])
        micro_slug = f"{prefix}-{st}" if st else ""
        if micro_slug and micro_slug not in micro:
            raise SystemExit(f"unknown subtopic {micro_slug!r} for chapter {cnum} section {snum}")
        sb, mi = micro[micro_slug] if micro_slug else (None, None)
        sub_slug = sb["slug"] if sb else ""
        sec_txt, sec_micro = [], []
        for sc, ss in secs:
            _u, _n, sslug, _en, _c = resolve(sc, by_num, by_slug)
            full = f"{'-'.join(sslug.split('-')[:2])}-{ss}" if ss else sslug
            if ss and full not in micro:
                raise SystemExit(f"unknown secondary subtopic {full!r} for chapter {cnum} section {snum}")
            target = micro[full][0]["slug"] if ss else sslug
            if ss:
                sec_micro.append(full)
            if target != sub_slug and target not in sec_txt:
                sec_txt.append(target)
        if "Ambiguous" in reason:
            flags.append("ambiguous")
        flags = sorted(set(flags))
        approval = "unapproved" if (cnum, snum) in spec.UNAPPROVED else "draft"
        if approval == "unapproved":
            reason = reason + " UNAPPROVED: " + spec.UNAPPROVED[(cnum, snum)]
        src = "app database (content.db.gz)" if cid is not None else "local HTML file (not in the app database)"
        out.append({
            "source": src, "old_chapter_id": cid if cid is not None else "", "old_chapter_num": cnum, "old_chapter_title": ctitle,
            "note_id": nid if nid is not None else "", "section_num": snum, "heading_en": hen or "", "heading_te": hte or "",
            "canonical_unit": unit or "—", "canonical_chapter_num": num or "—", "canonical_chapter_slug": slug,
            "canonical_chapter_title_en": en, "proposed_subtopic_slug": sub_slug,
            "proposed_subtopic_en": sb["en"] if sb else "(chapter level)", "proposed_microtopic_slug": micro_slug,
            "proposed_microtopic_en": mi["en"] if mi else "", "draft_subtopic_slug": micro_slug if mi and mi["from_draft"] else "",
            "coverage_scope": ("study_aid" if generic else spec.COVERAGE.get((cnum, snum)) or ("supplementary" if slug.startswith("supp-") else "direct")),
            "confidence": conf,
            "mapping_kind": kind_for(slug, cls), "multi_topic": "yes" if "multi_topic" in flags else "", "flags": ";".join(flags),
            "approval_status": approval, "needs_review": "yes" if (conf != "high" or flags or approval != "draft") else "",
            "content_use": "blocked_until_verified" if approval == "unapproved" else "",
            "reason": reason, "secondary_mappings": "; ".join(sec_txt), "secondary_microtopics": "; ".join(sec_micro),
        })
    return out


def coverage_gaps(mapped):
    """Learner-facing subtopics that no note section reaches (primary or secondary)."""
    used = {m["proposed_subtopic_slug"] for m in mapped if m["proposed_subtopic_slug"]}
    used |= {s for m in mapped for s in m["secondary_mappings"].split("; ") if s}
    by_num, _ = chapter_index()
    gaps = {}
    for num, subs in tax.build().items():
        missing = [sb["en"] for sb in subs if sb["slug"] not in used]
        if missing:
            gaps[(num, by_num[num][2])] = (missing, len(subs))
    return gaps


def write(mapped, out_dir=ROOT / "docs"):
    out_dir.mkdir(exist_ok=True)
    with open(out_dir / "ap_history_note_mapping_draft.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(mapped)
    n = len(mapped)
    conf = Counter(m["confidence"] for m in mapped)
    flagc = Counter(f for m in mapped for f in m["flags"].split(";") if f)
    lines = ["# AP History note-section mapping — DRAFT for review", "",
             "A proposal only: nothing in any database was changed, and no note was rewritten or split. Source chapter and section numbers are "
             "kept in the CSV. For chapters 1-12 the ids come from the bundled content database (they differ per environment, so a future import "
             "keys on source chapter number + section number). Chapters 13-19 exist only as local HTML files; their section structure is snapshotted in "
             "`scripts/ap_source_sections_13_19.json` with file hashes.", "",
             f"- Sections mapped: **{n}** (chapters 1-12: 225, from the app database; chapters 13-19: {n - 225}, from local HTML)",
             f"- Confidence: high {conf['high']}, medium {conf['medium']}, low {conf['low']}",
             f"- Flagged for review: {sum(1 for m in mapped if m['needs_review'])}; multi-topic sections: {flagc['multi_topic']}; "
             f"scope-boundary: {flagc['scope_boundary']}; ambiguous: {flagc['ambiguous']}; content-review: {flagc['content_review']}; "
             f"unapproved: {sum(1 for m in mapped if m['approval_status'] == 'unapproved')}",
             f"- Mapped at chapter level (no subtopic): {sum(1 for m in mapped if not m['proposed_subtopic_slug'])}",
             "- Coverage scope: " + ", ".join(f"{k} {v}" for k, v in sorted(Counter(m['coverage_scope'] for m in mapped).items())),
             f"- cross_unit_context: {flagc['cross_unit_context']}; supplementary_cross_context: {flagc['supplementary_cross_context']}", "",
             "Subtopics shown are the **rationalized** learner-facing subtopics (see `ap_history_subtopic_taxonomy_proposed.md`); the old 314-item draft slug is kept in "
             "`draft_subtopic_slug` and every draft item is now a microtopic (`proposed_microtopic_slug`). Nothing is seeded.", "",
             "Scope rules: " + spec.RULE_NOTES["qutb_shahi"] + " " + spec.RULE_NOTES["chapter_18"] + " " + spec.RULE_NOTES["question_scope"], "",
             "Rule for future questions from source 16.11: " + spec.RULE_NOTES["komaram_bheem"], "",
             "Rules used: one primary chapter and subtopic per section; multi-topic sections keep secondary links and a `multi_topic` flag and are not split; "
             "a shared place name is not a cross-topic link; the supplementary reference chapters are outside the 31 core chapters.", "",
             "## Where each source chapter went", ""]
    by_src = {}
    for m in mapped:
        by_src.setdefault((m["old_chapter_num"], m["old_chapter_title"].split(" (")[0][:80]), Counter())[m["canonical_chapter_slug"]] += 1
    for (cn, ct), d in by_src.items():
        lines.append(f"- Source {cn} — {ct}: " + ", ".join(f"`{s}` ({c})" for s, c in sorted(d.items())))
    lines += ["", "## Flagged sections", "", "| Src ch | Sec | Heading | Proposed | Conf | Flags | Why |", "|---|---|---|---|---|---|---|"]
    for m in mapped:
        if m["needs_review"] and m["confidence"] != "high" or m["flags"] or m["approval_status"] != "draft":
            lines.append(f"| {m['old_chapter_num']} | {m['section_num']} | {m['heading_en'][:40]} | {m['proposed_subtopic_slug'] or m['canonical_chapter_slug']} | "
                         f"{m['confidence']} | {m['flags']}{' ; UNAPPROVED' if m['approval_status'] == 'unapproved' else ''} | {m['reason'][:260]} |")
    lines += ["", "## Learner-facing subtopics with no note section (primary or secondary)", ""]
    for (num, title), (miss, total) in coverage_gaps(mapped).items():
        lines.append(f"- Chapter {num} — {title}: {len(miss)} of {total}: " + "; ".join(miss))
    lines += ["", "## Bundle note", "",
              "The review bundle is **incremental**: it contains only the commits made after base commit `e91b270a` (`release/secured-review`) and "
              "applies only on top of a repository that already has that commit. It is not a standalone or complete backup."]
    (out_dir / "ap_history_note_mapping_draft.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    m = build()
    write(m)
    print(f"wrote {len(m)} rows")
