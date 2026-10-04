"""Build the final hierarchy summary (read-only; seeds nothing).

    python scripts/build_ap_hierarchy_summary.py   # writes docs/ap_history_hierarchy_summary.md
"""
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.services import ap_canonical as canon          # noqa: E402
from app.services import ap_canonical_taxonomy as tax   # noqa: E402
import build_ap_note_mapping_draft as mapping           # noqa: E402


def facts():
    mapped = mapping.build()
    taxonomy = tax.build()
    per_chapter = {}
    for _u, num, slug, _en, _te, _c in canon.CHAPTERS:
        per_chapter[num] = (len(taxonomy[num]), sum(len(s["micros"]) for s in taxonomy[num]))
    return mapped, taxonomy, per_chapter


def write(path=ROOT / "docs" / "ap_history_hierarchy_summary.md"):
    mapped, taxonomy, per_chapter = facts()
    subs = sum(v[0] for v in per_chapter.values())
    micros = sum(v[1] for v in per_chapter.values())
    by_chapter = {}
    for m in mapped:
        by_chapter.setdefault(m["canonical_chapter_slug"], Counter())[m["coverage_scope"]] += 1
    scope = Counter(m["coverage_scope"] for m in mapped)
    core = [m for m in mapped if not m["canonical_chapter_slug"].startswith("supp-")]
    supp = [m for m in mapped if m["canonical_chapter_slug"].startswith("supp-")]
    L = ["# AP History — final hierarchy summary (approved)", "",
         "Taxonomy version: **`" + tax.TAXONOMY_VERSION + "`**.", "", "Subject → Official unit → Canonical chapter → Learner-facing subtopic → Internal microtopic. Not seeded into staging or production; no questions imported; nothing deployed.", "",
         "## Totals", "",
         f"- Official units: **{len(canon.UNITS)}**",
         f"- Core chapters: **{len(canon.CHAPTERS)}**",
         f"- Supplementary chapters: **{len(canon.SUPPLEMENTARY)}** (outside the 31; they never count toward direct syllabus completion)",
         f"- Learner-facing subtopics: **{subs}**",
         f"- Internal microtopics: **{micros}** (314 preserved draft subtopics + {micros - 314} new)",
         f"- Source note sections mapped: **{len(mapped)}** (chapters 1-12 from the app database: 225; chapters 13-19 from local HTML: {len(mapped) - 225})", "",
         "## Direct versus supplementary note sections", "",
         "| Measure | Sections |", "|---|---:|",
         f"| Primary home is a core chapter | {len(core)} |", f"| Primary home is a supplementary chapter | {len(supp)} |"]
    for k in ("direct", "mixed", "supplementary_context", "supplementary", "study_aid"):
        L.append(f"| coverage_scope = {k} | {scope[k]} |")
    L += ["", "`direct`: counts as direct syllabus coverage. `mixed`: contains direct and supplementary material; questions take scope from the fact tested. "
          "`supplementary_context`: supporting context inside a core chapter (post-1600 Qutb Shahi material). `supplementary`: the section's primary home is a "
          "supplementary chapter. `study_aid`: introduction, glossary, key sites, revision and similar (not content).", "",
          "## Units and core chapters", "",
          "| Unit | Ch | Chapter | Class | Subtopics | Microtopics | Sections (direct / mixed / context / study aid) |", "|---|---:|---|---|---:|---:|---|"]
    for unit, num, slug, en, _te, cls in canon.CHAPTERS:
        c = by_chapter.get(slug, Counter())
        L.append(f"| {unit} | {num} | {en} | {cls} | {per_chapter[num][0]} | {per_chapter[num][1]} | "
                 f"{c['direct']} / {c['mixed']} / {c['supplementary_context']} / {c['study_aid']} |")
    L += ["", "Per-unit subtopics: " + "; ".join(
        f"Unit {u}: {sum(per_chapter[n][0] for uu, n, *_ in canon.CHAPTERS if uu == u)}" for u, *_ in canon.UNITS), "",
          "## Supplementary chapters (visibly separate; not counted toward completion)", "",
          "| Slug | English title | Type | Source sections with this primary |", "|---|---|---|---:|"]
    for slug, en, _te, kind, _src in canon.SUPPLEMENTARY:
        L.append(f"| `{slug}` | {en} | {kind} | {sum(by_chapter.get(slug, Counter()).values())} |")
    blocked = [m for m in mapped if m["content_use"]]
    low = [m for m in mapped if m["confidence"] == "low"]
    cr = [m for m in mapped if "content_review" in m["flags"].split(";")]
    sb = [m for m in mapped if "scope_boundary" in m["flags"].split(";")]
    amb = [m for m in mapped if "ambiguous" in m["flags"].split(";")]
    multi = [m for m in mapped if m["multi_topic"] == "yes"]
    L += ["", "## Unresolved and blocked mappings", "",
          f"- **Blocked (content_use = blocked_until_verified):** {len(blocked)} — " + "; ".join(
              f"source {m['old_chapter_num']} section {m['section_num']} ({m['heading_en'][:50]})" for m in blocked)
          + ". No MCQs, no factual summaries, no import into approved learner content; see `ap_history_kataya_vema_audit.md`. External verification is handled separately.",
          f"- **Unapproved:** {sum(1 for m in mapped if m['approval_status'] == 'unapproved')} (the same row).",
          f"- **Low confidence:** {len(low)} — " + "; ".join(f"source {m['old_chapter_num']} section {m['section_num']} ({m['heading_en'][:45]})" for m in low) + ".",
          f"- **Flagged content_review:** {len(cr)} (retained at chapter-level or bridge mapping; not mapped to Unit 4 folk/tribal culture).",
          f"- **scope_boundary retained (mixed sections decided by dominant content):** {len(sb)} — " + "; ".join(
              f"source {m['old_chapter_num']} section {m['section_num']}" for m in sb) + ".",
          f"- **Ambiguous (flag):** {len(amb)}.",
          f"- **Multi-topic sections (never split; one primary plus secondaries):** {len(multi)}.",
          "- **Per-question mapping required:** source 16 section 11 (Komaram Bheem). Questions must be mapped individually and do not inherit the section's primary. "
          "The importer or content review must enforce it.",
          "- **Scope inherited from the fact tested:** every mixed section and the Qutb Shahi sections; a section's scope never decides a question's scope.",
          "- **Not yet done by design:** subtopics are not seeded; no learner pages; no importer; no questions imported; legacy 380 questions unchanged; no deploy.",
          "- **Shared MCQ folder:** only `content/AP_History_MCQ_Project/05_claude_import` is an authorized import location; `02_drafts` is never imported.", "",
          "## Bundle note", "",
          "The review bundle is **incremental**: it contains only commits after base commit `e91b270a` (`release/secured-review`) and applies only on top of a repository "
          "that already has that commit. It is not a standalone or complete backup."]
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write(); print("wrote docs/ap_history_hierarchy_summary.md")
