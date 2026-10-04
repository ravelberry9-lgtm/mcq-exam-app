"""Build the PROPOSED rationalized taxonomy review files (read-only; seeds nothing, touches no database).

    python scripts/build_ap_taxonomy_proposed.py   # writes docs/ap_history_subtopic_taxonomy_proposed.{csv,md}

Unit -> Chapter -> learner-facing subtopic -> internal microtopic, with source support from the draft note mapping.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.services import ap_canonical as canon           # noqa: E402
from app.services import ap_canonical_subtopics as draft  # noqa: E402
from app.services import ap_canonical_taxonomy as tax    # noqa: E402
import ap_taxonomy_review_spec as old_review              # noqa: E402
import build_ap_note_mapping_draft as mapping             # noqa: E402

COLUMNS = ["taxonomy_version", "unit", "chapter_num", "chapter_slug", "chapter_title_en", "chapter_title_te", "subtopic_slug", "subtopic_en", "subtopic_te",
           "subtopic_te_search_key", "microtopic_slug", "microtopic_en", "microtopic_te", "microtopic_scope", "old_draft_slug",
           "subtopic_primary_sections", "subtopic_secondary_sections", "microtopic_primary_sections", "microtopic_secondary_sections",
           "earlier_review_flags"]
LIMIT_NORMAL, LIMIT_LARGE, MIN_TARGET = 12, 15, 6


def build():
    mapped = mapping.build()
    sp = Counter(m["proposed_subtopic_slug"] for m in mapped if m["proposed_subtopic_slug"])
    ss = Counter(x for m in mapped for x in m["secondary_mappings"].split("; ") if x)
    mp = Counter(m["proposed_microtopic_slug"] for m in mapped if m["proposed_microtopic_slug"])
    ms = Counter(x for m in mapped for x in m["secondary_microtopics"].split("; ") if x)
    chap = tax.build()
    old_flags = {}
    for (num, suffix), (flags, _n) in old_review.FINDINGS.items():
        old_flags[(num, suffix)] = flags
    rows = []
    for unit, num, slug, en, te, _cls in canon.CHAPTERS:
        for sb in chap[num]:
            for mi in sb["micros"]:
                rows.append({
                    "taxonomy_version": tax.TAXONOMY_VERSION, "unit": unit, "chapter_num": num, "chapter_slug": slug, "chapter_title_en": en, "chapter_title_te": te,
                    "subtopic_slug": sb["slug"], "subtopic_en": sb["en"], "subtopic_te": sb["te"], "subtopic_te_search_key": tax.search_key(sb["te"]),
                    "microtopic_slug": mi["slug"], "microtopic_en": mi["en"], "microtopic_te": mi["te"], "microtopic_scope": mi["scope"],
                    "old_draft_slug": mi["slug"] if mi["from_draft"] else "",
                    "subtopic_primary_sections": sp[sb["slug"]], "subtopic_secondary_sections": ss[sb["slug"]],
                    "microtopic_primary_sections": mp[mi["slug"]], "microtopic_secondary_sections": ms[mi["slug"]],
                    "earlier_review_flags": old_flags.get((num, mi["old_suffix"]), "") if mi["old_suffix"] else ""})
    return rows


def write(rows, out_dir=ROOT / "docs"):
    with open(out_dir / "ap_history_subtopic_taxonomy_proposed.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS); w.writeheader(); w.writerows(rows)
    chapters, subs = {}, {}
    for r in rows:
        chapters.setdefault((r["unit"], r["chapter_num"], r["chapter_title_en"], r["chapter_title_te"]), {}).setdefault(r["subtopic_slug"], []).append(r)
    n_sub = sum(len(v) for v in chapters.values())
    n_micro = len(rows)
    counts = {k[1]: len(v) for k, v in chapters.items()}
    L = ["# AP History — rationalized taxonomy `" + tax.TAXONOMY_VERSION + "` (approved structure)", "",
         "Taxonomy version: **`" + tax.TAXONOMY_VERSION + "`**. Approved structure; seeded only into disposable validation copies so far, never into staging or production. It replaces the 314-item draft; the earlier review files are kept for the record.", "",
         "Model: **canonical chapter → learner-facing subtopic → internal microtopic.** A question gets one primary subtopic and any number of microtopic tags; "
         "microtopics are filters, never navigation. Every one of the 314 earlier draft subtopics survives as a microtopic (its old slug is kept), so no "
         "historical coverage is removed.", "",
         f"- Learner-facing subtopics: **{n_sub}** (was 314), in 31 chapters; per chapter min {min(counts.values())}, max {max(counts.values())}, "
         f"chapters at or above 10: {sum(1 for c in counts.values() if c >= 10)}",
         f"- Internal microtopics: **{n_micro}** (314 from the draft + {sum(1 for r in rows if not r['old_draft_slug'])} new)",
         f"- Chapters with fewer than {MIN_TARGET} subtopics: {', '.join(str(n) for n, c in counts.items() if c < MIN_TARGET)}. They are small chapters, or chapters with thin source coverage; "
         "merging further would combine unlike themes. They can be split later without losing data because their microtopics already exist.", "",
         "## How the earlier findings were resolved", ""]
    gr = {}
    for num, subs_ in tax.build().items():
        for sb in subs_:
            for mi in sb["micros"]:
                if mi["old_suffix"]:
                    gr[(num, mi["old_suffix"])] = sb
    dup_rows = []
    for (num, suffix), (flags, note) in old_review.FINDINGS.items():
        if "duplicate" in flags.split(";"):
            dup_rows.append((num, suffix, gr[(num, suffix)]))
    L.append(f"- **Exact duplicates ({len(dup_rows)} items):** " + "; ".join(f"ch{n} `{s}` → `{b['key']}`" for n, s, b in dup_rows) + ".")
    narrow_standalone = [(n, s, gr[(n, s)]) for (n, s), (f, _x) in old_review.FINDINGS.items()
                         if ("narrow" in f.split(";") or "note_driven" in f.split(";")) and len(gr[(n, s)]["micros"]) == 1]
    narrow_total = sum(1 for (n, s), (f, _x) in old_review.FINDINGS.items() if "narrow" in f.split(";") or "note_driven" in f.split(";"))
    L.append(f"- **Narrow or note-driven items:** {narrow_total} flagged earlier; {narrow_total - len(narrow_standalone)} are now microtopics inside a broader subtopic. "
             f"{len(narrow_standalone)} remain as their own subtopic and are listed below for your decision.")
    L.append("- **Rulers:** no ruler has a learner-facing subtopic except Krishnadevaraya (Chapter 11, kept because the reign has its own large body of content and exam questions). "
             "Kakatiya rulers (Rudradeva, Mahadeva, Ganapatideva, Rudramadevi, Prataparudra) are microtopics under *Political history and rulers*.")
    L.append("- **Splits that remain deliberate:** Chapter 14 (thematic) overlaps Chapters 8–13 by design; questions keep one primary chapter (the dynasty chapter) unless genuinely comparative.")
    L += ["", "### Subtopics kept standalone although earlier flagged narrow or note-driven", ""]
    for n, s, b in narrow_standalone:
        L.append(f"- ch{n} `{b['key']}` — {b['en']}")
    L += ["", "## Scope rules recorded with the taxonomy", "",
          "- " + mapping.spec.RULE_NOTES["qutb_shahi"],
          "- Microtopic `post-1600-context` (Chapter 13) carries `supplementary_context` scope.",
          "- " + mapping.spec.RULE_NOTES["chapter_18"], "",
          "## Normalized Telugu terminology applied", "",
          "Learner-facing metadata uses the approved forms; source spellings stay untouched in source-text fields. Zero-width characters are avoided in search keys "
          "(`subtopic_te_search_key` strips them). The display form keeps the zero-width non-joiner only where the script needs it: "
          + ", ".join(f"`{a.replace(chr(0x200c), '‌')}`" for a in tax.ZW_ALLOWED) + ".", "",
          "| English | Normalized Telugu |", "|---|---|"]
    for en, te in [("Palaeolithic", "పురాతన శిలాయుగం (పాలియోలిథిక్)"), ("Mesolithic", "మధ్య శిలాయుగం (మెసోలిథిక్)"), ("Neolithic", "నవీన శిలాయుగం (నియోలిథిక్)"),
                   ("Chalcolithic", "రాగి–రాతి యుగం (చాల్కోలిథిక్)"), ("Megalithic", "బృహత్‌శిలా సంస్కృతి (మెగాలిథిక్)"), ("Hathigumpha", "హాతిగుంఫా శాసనం"),
                   ("Punch-marked coins", "ముద్రాంకిత (పంచ్-మార్క్డ్) నాణేలు"), ("Musunuri", "ముసునూరి"), ("Battle of Talikota", "తళ్ళికోట యుద్ధం (Battle of Talikota)"),
                   ("Qutb Shahi", "కుతుబ్ షాహీ"), ("Dakhni", "దక్కనీ"), ("Northern Circars", "ఉత్తర సర్కార్లు"), ("Ceded Districts", "దత్త మండలాలు (సీడెడ్ జిల్లాలు)"),
                   ("Ryotwari", "రైత్వారీ"), ("Sri Bagh Pact", "శ్రీబాగ్ ఒప్పందం"), ("Gentlemen's Agreement", "పెద్దమనుషుల ఒప్పందం (జెంటిల్మెన్స్ అగ్రిమెంట్)"),
                   ("JVP Committee", "జె.వి.పి. కమిటీ (JVP Committee)"), ("States Reorganisation Commission", "రాష్ట్రాల పునర్వ్యవస్థీకరణ సంఘం (SRC)"),
                   ("Home Rule Movement", "హోమ్ రూల్ (స్వపరిపాలన) ఉద్యమం")]:
        L.append(f"| {en} | {te} |")
    L += ["", "## Taxonomy: Unit → Chapter → subtopic → microtopics", ""]
    last_u = None
    for (u, n, t_en, t_te), sub in chapters.items():
        if u != last_u:
            L += [f"### Unit {u}", ""]; last_u = u
        L += [f"#### Chapter {n} — {t_en} / {t_te} ({len(sub)} subtopics)", "",
              "| Subtopic (English) | Subtopic (Telugu) | Src P/S | Microtopics |", "|---|---|---|---|"]
        for slug, rs in sub.items():
            r0 = rs[0]
            micros = "; ".join(f"{r['microtopic_en']}{' [' + r['microtopic_scope'] + ']' if r['microtopic_scope'] != 'direct' else ''}" for r in rs)
            L.append(f"| {r0['subtopic_en']} | {r0['subtopic_te']} | {r0['subtopic_primary_sections']}/{r0['subtopic_secondary_sections']} | {micros} |")
        L.append("")
    (out_dir / "ap_history_subtopic_taxonomy_proposed.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    r = build(); write(r); print(f"wrote {len(r)} microtopic rows")
