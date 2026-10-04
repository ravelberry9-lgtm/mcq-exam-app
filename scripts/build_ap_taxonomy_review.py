"""Build the bilingual DRAFT subtopic-taxonomy review files (read-only; seeds nothing, touches no database).

    python scripts/build_ap_taxonomy_review.py   # writes docs/ap_history_subtopic_taxonomy_review.{csv,md}

Rows are ordered Unit -> Chapter -> subtopic. Source-support counts come from the draft note-section mapping.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.services import ap_canonical as canon          # noqa: E402
from app.services import ap_canonical_subtopics as sub  # noqa: E402
import ap_taxonomy_review_spec as spec                   # noqa: E402
import build_ap_note_mapping_draft as mapping            # noqa: E402

COLUMNS = ["unit", "chapter_num", "chapter_slug", "chapter_title_en", "subtopic_slug", "subtopic_en", "subtopic_te",
           "chapter_classification", "primary_sections", "secondary_sections", "review_flags", "reviewer_note", "decision"]
FLAG_ORDER = ["duplicate", "overlap", "narrow", "note_driven", "no_source", "telugu_review", "by_design"]
THRESHOLD_MANY, THRESHOLD_FEW = 14, 7


def build():
    mapped = mapping.build()
    prim = Counter(m["proposed_subtopic_slug"] for m in mapped if m["proposed_subtopic_slug"])
    sec = Counter(s for m in mapped for s in m["secondary_mappings"].split("; ") if s)
    units = {u: (en, te) for u, en, te in canon.UNITS} if hasattr(canon, "UNITS") and canon.UNITS and len(canon.UNITS[0]) == 3 else {}
    te_issue = {(c, s) for c, s, *_ in spec.TELUGU_ISSUES}
    rows = []
    for unit, num, slug, en, _te, cls in canon.CHAPTERS:
        for sub_slug, s_en, s_te in sub.expanded()[slug]:
            suffix = sub_slug.split("-", 2)[2]
            flags, note = spec.FINDINGS.get((num, suffix), ("", ""))
            fl = set(f for f in flags.split(";") if f)
            if (num, suffix) in te_issue:
                fl.add("telugu_review")
            if prim[sub_slug] == 0 and sec[sub_slug] == 0:
                fl.add("no_source")
            elif prim[sub_slug] == 1 and sec[sub_slug] == 0 and "narrow" in fl:
                fl.add("note_driven")
            if prim[sub_slug] + sec[sub_slug] > 0:
                fl.discard("no_source")
            flags_txt = ";".join(f for f in FLAG_ORDER if f in fl)
            rows.append({"unit": unit, "chapter_num": num, "chapter_slug": slug, "chapter_title_en": en, "subtopic_slug": sub_slug,
                         "subtopic_en": s_en, "subtopic_te": s_te, "chapter_classification": cls, "primary_sections": prim[sub_slug],
                         "secondary_sections": sec[sub_slug], "review_flags": flags_txt, "reviewer_note": note,
                         "decision": "proposed" if not flags_txt else "needs_decision"})
    return rows


def write(rows, out_dir=ROOT / "docs"):
    with open(out_dir / "ap_history_subtopic_taxonomy_review.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(rows)
    by_ch = {}
    for r in rows:
        by_ch.setdefault((r["unit"], r["chapter_num"], r["chapter_title_en"]), []).append(r)
    fc = Counter(f for r in rows for f in r["review_flags"].split(";") if f)
    L = ["# AP History subtopic taxonomy — DRAFT for bilingual review", "",
         "Nothing here is seeded. The subtopics stay a draft until you approve them; the importer will not create any. "
         "Source-support counts come from the draft note-section mapping (`ap_history_note_mapping_draft.csv`); a count of 0 is a fact about the "
         "current notes, not a verdict that the subtopic is wrong (some are exam topics the notes do not yet cover).", "",
         f"- Subtopics: **{len(rows)}** in {len(by_ch)} chapters. Flagged for a decision: {sum(1 for r in rows if r['decision'] == 'needs_decision')}. "
         f"Flag counts: " + ", ".join(f"{k} {fc[k]}" for k in FLAG_ORDER),
         "- Flags: `duplicate` same concept, different name; `overlap` overlaps another subtopic; `narrow` one person/event/paper; "
         "`note_driven` exists mainly for one current note heading; `no_source` no note section maps here; `telugu_review` Telugu wording needs a decision; "
         "`by_design` overlap is deliberate (thematic chapter 14).", "",
         "## Chapters with too many or too few subtopics", ""]
    for (u, n, t), rs in by_ch.items():
        cnt = len(rs)
        nos = sum(1 for r in rs if "no_source" in r["review_flags"])
        if cnt >= THRESHOLD_MANY or cnt <= THRESHOLD_FEW or nos * 2 >= cnt:
            L.append(f"- Chapter {n} — {t}: {cnt} subtopics, {nos} without source. " + spec.CHAPTER_NOTES.get(n, ""))
    L += ["", "## Pairs to merge or decide (duplicate or overlapping concepts)", ""]
    for r in rows:
        if "duplicate" in r["review_flags"]:
            L.append(f"- ch{r['chapter_num']} `{r['subtopic_slug'].split('-', 2)[2]}` — {r['subtopic_en']}: {r['reviewer_note']}")
    L += ["", "## Subtopics that exist mainly for one note heading", ""]
    for r in rows:
        if "note_driven" in r["review_flags"]:
            L.append(f"- ch{r['chapter_num']} `{r['subtopic_slug'].split('-', 2)[2]}` — {r['subtopic_en']} ({r['primary_sections']} section). {r['reviewer_note']}")
    L += ["", "## Telugu translations needing review", "",
          "Evidence is how often each spelling appears in the current notes (chapters 1-12 in the app database, 13-19 in the local HTML files). "
          "No automatic translation is used at render time; whichever form is chosen becomes the one the bank uses.", "",
          "| Ch | Subtopic | Current Telugu | Issue | Suggestion |", "|---|---|---|---|---|"]
    te = {(r["chapter_num"], r["subtopic_slug"].split("-", 2)[2]): r["subtopic_te"] for r in rows}
    ch_te = {n: t for _u, n, _s, _e, t, _c in canon.CHAPTERS}
    for c, s, cur, issue, sug in spec.TELUGU_ISSUES:
        cur = cur or te.get((c, s)) or ch_te.get(c, "")
        L.append(f"| {c} | `{s}` | {cur} | {issue} | {sug} |")
    L += ["", "## Full taxonomy: Unit → Chapter → subtopic (English / Telugu / classification)", ""]
    last_u = None
    for (u, n, t), rs in by_ch.items():
        if u != last_u:
            L += [f"### Unit {u}", ""]
            last_u = u
        L += [f"#### Chapter {n} — {t} ({rs[0]['chapter_classification']})", "",
              "| Subtopic (English) | Subtopic (Telugu) | Src (P/S) | Flags |", "|---|---|---|---|"]
        for r in rs:
            L.append(f"| {r['subtopic_en']} | {r['subtopic_te']} | {r['primary_sections']}/{r['secondary_sections']} | {r['review_flags']} |")
        L.append("")
    (out_dir / "ap_history_subtopic_taxonomy_review.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    rows = build()
    write(rows)
    print(f"wrote {len(rows)} subtopic rows")
