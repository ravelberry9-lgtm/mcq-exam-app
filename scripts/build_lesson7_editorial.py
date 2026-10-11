import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "content" / "textbooks" / "st3-ecosystem-biodiversity"
LESSON_ID = "st3-l07-indian-law-protected-areas-institutions"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def read_jsonl(path):
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def write_jsonl(path, rows):
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows) + "\n",
        encoding="utf-8",
    )


manifest_path = BOOK / "manifest.json"
facts_path = BOOK / "facts.jsonl"
section_map_path = BOOK / "section_map.json"
manifest = read_json(manifest_path)
facts = read_jsonl(facts_path)
section_map = read_json(section_map_path)
lesson = next(item for item in manifest["lessons"] if item["id"] == LESSON_ID)

draft_sections = {}
for name in ("l7_ab_rewrite.json", "l7_cd_rewrite.json"):
    draft = read_json(BOOK / "drafts" / name)
    for section in draft["sections"]:
        draft_sections[section["id"]] = section

expected = {section["id"] for section in lesson["sections"]}
if set(draft_sections) != expected:
    raise SystemExit(f"draft section mismatch: {set(draft_sections)} != {expected}")

fact_by_id = {row["fact_id"]: row for row in facts}
for section in lesson["sections"]:
    section_id = section["id"]
    old_paragraphs = section["paragraphs"]
    new_paragraphs = draft_sections[section_id]["paragraphs"]
    if not all(set(item) >= {"en", "te"} for item in new_paragraphs):
        raise SystemExit(f"{section_id}: every paragraph needs en and te")

    # When counts are unchanged, replace fact-ledger narration by exact old paragraph.
    if len(old_paragraphs) == len(new_paragraphs):
        replacement = {
            (old["en"], old["te"]): (new["en"], new["te"])
            for old, new in zip(old_paragraphs, new_paragraphs)
        }
        for row in facts:
            pair = (row.get("en"), row.get("te"))
            if row.get("section_id") == section_id and pair in replacement:
                row["en"], row["te"] = replacement[pair]

    # Consolidated paragraphs carry explicit fact_ids and become the canonical text.
    for paragraph in new_paragraphs:
        for fact_id in paragraph.get("fact_ids", []):
            if fact_id not in fact_by_id:
                raise SystemExit(f"unknown fact mapping: {fact_id}")
            fact_by_id[fact_id]["en"] = paragraph["en"]
            fact_by_id[fact_id]["te"] = paragraph["te"]

    section["paragraphs"] = [
        {"en": item["en"], "te": item["te"]} for item in new_paragraphs
    ]


def refresh_nodes(value):
    if isinstance(value, list):
        for item in value:
            refresh_nodes(item)
    elif isinstance(value, dict):
        ids = value.get("fact_ids") or []
        if ids and isinstance(value.get("body"), dict):
            fact = next((fact_by_id.get(fact_id) for fact_id in ids if fact_id in fact_by_id), None)
            if fact:
                value["body"] = {"en": fact["en"], "te": fact["te"]}
        for child in value.values():
            refresh_nodes(child)


refresh_nodes(lesson.get("infographics", []))
refresh_nodes(section_map)

write_json(manifest_path, manifest)
write_jsonl(facts_path, facts)
write_json(section_map_path, section_map)

titles = {
    "l7-a": ("Wildlife Law and Protected Areas", "Wildlife law, protected areas మధ్య legal distinctions", "🛡️"),
    "l7-b": ("Biological Diversity Act and Local Institutions", "NBA, SBB, BMC, ABS rolesను clearగా వేరు చేయండి", "🧬"),
    "l7-c": ("Forests, Rights, Wetlands and Coasts", "Land regulation, community rights, aquatic landscapes", "🌿"),
    "l7-d": ("National Institutions and Biodiversity Planning", "Policy, regulation, research, monitoring, adjudication", "🏛️"),
}

parts = [
    '<article class="editorial-lesson" data-editorial-html="true">',
    '  <header class="editorial-lesson-intro">',
    '    <div class="hero-copy"><p class="eyebrow">APPSC · SCIENCE &amp; TECHNOLOGY</p><h2>Indian Conservation Law and Institutions</h2><p class="hero-subtitle">Laws · Protected Areas · Rights · Institutions</p><p class="lesson-deck">Indiaలో conservation governanceను law, authority, procedure, institution ఆధారంగా అర్థం చేసుకోండి. Similar-looking labelsను legal statusతో వేరు చేయడం ఈ lesson ప్రధాన లక్ష్యం.</p></div>',
    '    <div class="hero-orbit" aria-hidden="true"><span>LAW</span><span>RIGHTS</span><span>ACTION</span><b>⚖️</b></div>',
    '    <nav class="chapter-map" aria-label="Lesson map">',
]
for index, section in enumerate(lesson["sections"], 1):
    title, subtitle, _ = titles[section["id"]]
    anchor = f"{LESSON_ID}-{section['id']}"
    parts.append(
        f'      <a href="#{anchor}"><span>{index:02d}</span><strong>{html.escape(title)}</strong><small>{html.escape(subtitle)}</small></a>'
    )
parts.extend(["    </nav>", "  </header>"])

for index, section in enumerate(lesson["sections"], 1):
    title, subtitle, icon = titles[section["id"]]
    anchor = f"{LESSON_ID}-{section['id']}"
    level = section.get("level", "group1")
    level_label = "Foundation" if level == "group2" else "Advanced depth"
    parts.extend(
        [
            f'  <section class="editorial-section" id="{anchor}" data-level="{level}">',
            f'    <header class="editorial-section-heading"><div class="section-icon" aria-hidden="true">{icon}</div><div><span class="level-pill">{level_label} · {index:02d}</span><h3>{html.escape(title)}</h3><p>{html.escape(subtitle)}</p></div></header>',
            f'    <aside class="concept-ribbon"><strong>Reading key</strong><span>{html.escape(subtitle)}</span></aside>',
        ]
    )
    for paragraph in section["paragraphs"]:
        parts.append(f"    <p>{html.escape(paragraph['te'])}</p>")
    parts.append("  </section>")
parts.append("</article>")

lesson_path = BOOK / "lessons" / f"{LESSON_ID}.html"
lesson_path.write_text("\n".join(parts) + "\n", encoding="utf-8")
print(f"updated {LESSON_ID}: {sum(len(s['paragraphs']) for s in lesson['sections'])} paragraphs")
