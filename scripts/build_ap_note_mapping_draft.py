"""Build the DRAFT note-section -> canonical mapping review files from the bundled content source (read-only).

    python scripts/build_ap_note_mapping_draft.py          # writes docs/ap_history_note_mapping_draft.{csv,md}

Reads data/content.db.gz (AP History notes) and scripts/ap_note_mapping_spec.py. Writes only the two review files. Touches no database.
"""
import csv
import gzip
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.services import ap_canonical as canon          # noqa: E402
from app.services import ap_canonical_subtopics as sub  # noqa: E402
import ap_note_mapping_spec as spec                      # noqa: E402

COLUMNS = ["old_chapter_id", "old_chapter_num", "old_chapter_title", "note_id", "section_num", "heading_en", "heading_te",
           "canonical_unit", "canonical_chapter_num", "canonical_chapter_slug", "canonical_chapter_title_en",
           "proposed_subtopic_slug", "proposed_subtopic_en", "confidence", "mapping_kind", "needs_review", "reason", "secondary_mappings"]


def load_notes(path=ROOT / "data" / "content.db.gz"):
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


def chapter_index():
    by_num = {num: (unit, slug, en, cls) for unit, num, slug, en, _te, cls in canon.CHAPTERS}
    by_slug = {slug: (unit, num, slug, en, cls) for unit, num, slug, en, _te, cls in canon.CHAPTERS}
    supp = {slug: (None, None, slug, en, "supplementary") for slug, en, _te, _k, _s in canon.SUPPLEMENTARY}
    return by_num, {**by_slug, **supp}


def resolve(chapter_ref, by_num, by_slug):
    """chapter number or supplementary slug -> (unit, num, slug, title_en, classification)"""
    if isinstance(chapter_ref, int):
        unit, slug, en, cls = by_num[chapter_ref]
        return unit, chapter_ref, slug, en, cls
    return by_slug[chapter_ref]


def kind_for(cls):
    return {"direct": "direct", "bridge": "bridge", "thematic": "direct", "supplementary": "cross_cutting"}[cls]


def build(rows=None):
    rows = rows or load_notes()
    by_num, by_slug = chapter_index()
    sub_titles = {s: en for lst in sub.expanded().values() for s, en, _te in lst}
    out = []
    for cid, cnum, ctitle, nid, snum, hen, hte in rows:
        entry = spec.SPEC.get((cnum, snum))
        if entry is None:
            if (hen or "").strip() not in spec.GENERIC_HEADINGS:
                raise SystemExit(f"unmapped non-generic section: chapter {cnum} section {snum} {hen!r}")
            ref, st, conf, reason, secs = spec.DEFAULT_CHAPTER[cnum], None, "high", spec.GENERIC_REASON, []
        else:
            ref, st, conf, reason, secs = entry
        unit, num, slug, en, cls = resolve(ref, by_num, by_slug)
        prefix = "-".join(slug.split("-")[:2]) if not slug.startswith("supp-") else None
        sub_slug = f"{prefix}-{st}" if st else ""
        if sub_slug and sub_slug not in sub_titles:
            raise SystemExit(f"unknown subtopic {sub_slug!r} for chapter {cnum} section {snum}")
        sec_txt = []
        for sc, ss in secs:
            _u, _n, sslug, _en, _c = resolve(sc, by_num, by_slug)
            sp = "-".join(sslug.split("-")[:2])
            full = f"{sp}-{ss}" if ss else sslug
            if ss and full not in sub_titles:
                raise SystemExit(f"unknown secondary subtopic {full!r} for chapter {cnum} section {snum}")
            sec_txt.append(full)
        ambiguous = "Ambiguous" in reason or "should be split" in reason or "Propose adding" in reason or "should be checked" in reason
        out.append({
            "old_chapter_id": cid, "old_chapter_num": cnum, "old_chapter_title": ctitle, "note_id": nid, "section_num": snum,
            "heading_en": hen or "", "heading_te": hte or "", "canonical_unit": unit or "—", "canonical_chapter_num": num or "—",
            "canonical_chapter_slug": slug, "canonical_chapter_title_en": en, "proposed_subtopic_slug": sub_slug,
            "proposed_subtopic_en": sub_titles.get(sub_slug, "(chapter level)"), "confidence": conf, "mapping_kind": kind_for(cls),
            "needs_review": "yes" if (conf != "high" or ambiguous) else "", "reason": reason, "secondary_mappings": "; ".join(sec_txt),
        })
    return out


def coverage_gaps(mapped):
    used = {m["proposed_subtopic_slug"] for m in mapped if m["proposed_subtopic_slug"]}
    used |= {s for m in mapped for s in m["secondary_mappings"].split("; ") if s}
    by_num, _ = chapter_index()
    gaps = {}
    for num in range(1, 14):
        slug = by_num[num][1]
        missing = [en for s, en, _te in sub.expanded()[slug] if s not in used]
        if missing:
            gaps[(num, by_num[num][2])] = missing
    return gaps


def write(mapped, out_dir=ROOT / "docs"):
    out_dir.mkdir(exist_ok=True)
    with open(out_dir / "ap_history_note_mapping_draft.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(mapped)
    n = len(mapped)
    conf = {c: sum(1 for m in mapped if m["confidence"] == c) for c in ("high", "medium", "low")}
    lines = ["# AP History note-section mapping — DRAFT for review", "",
             "Generated from the bundled content source (`data/content.db.gz`). Nothing in any database was changed; "
             "this is a proposal. Source chapter numbers are preserved in the CSV. Database ids (old_chapter_id, note_id) are those of "
             "the bundled source and differ per environment, so the future import will key on (source chapter number, section number).", "",
             f"- Sections mapped: **{n}** (source chapters 1-12; chapters 13-19 exist only as local HTML and are not in the app database)",
             f"- Confidence: high {conf['high']}, medium {conf['medium']}, low {conf['low']}",
             f"- Flagged `needs_review`: {sum(1 for m in mapped if m['needs_review'])}",
             f"- Mapped at chapter level (no subtopic): {sum(1 for m in mapped if not m['proposed_subtopic_slug'])}", "",
             "## Where each source chapter went", ""]
    by_src = {}
    for m in mapped:
        by_src.setdefault((m["old_chapter_num"], m["old_chapter_title"]), {}).setdefault(m["canonical_chapter_slug"], 0)
        by_src[(m["old_chapter_num"], m["old_chapter_title"])][m["canonical_chapter_slug"]] += 1
    for (cn, ct), d in by_src.items():
        lines.append(f"- Source {cn} — {ct}: " + ", ".join(f"`{s}` ({c})" for s, c in d.items()))
    lines += ["", "## Flagged sections (needs_review)", "", "| Src ch | Sec | Heading | Proposed | Conf | Why |", "|---|---|---|---|---|---|"]
    for m in mapped:
        if m["needs_review"]:
            lines.append(f"| {m['old_chapter_num']} | {m['section_num']} | {m['heading_en'][:50]} | {m['proposed_subtopic_slug'] or m['canonical_chapter_slug']} | {m['confidence']} | {m['reason']} |")
    lines += ["", "## Canonical subtopics with no note section (content gaps for chapters 1-13)", ""]
    for (num, title), miss in coverage_gaps(mapped).items():
        lines.append(f"- Chapter {num} — {title}: " + "; ".join(miss))
    lines += ["", "Canonical chapters 14-31 have no source notes at all (only local chapters 15-19 exist as HTML, not yet mapped)."]
    (out_dir / "ap_history_note_mapping_draft.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    m = build()
    write(m)
    print(f"wrote {len(m)} rows")
