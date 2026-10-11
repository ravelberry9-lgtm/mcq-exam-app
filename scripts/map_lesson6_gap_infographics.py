"""Make Lesson 6's textual teaching/revision atlases reciprocal with added facts."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
book = root / "content/textbooks/st3-ecosystem-biodiversity"
manifest_path = book / "manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
lesson = next(x for x in manifest["lessons"]
              if x["id"] == "st3-l06-global-frameworks-conventions")
rows = [json.loads(x) for x in (book / "facts.jsonl").read_text(encoding="utf-8").splitlines()]
new = [x for x in rows if x.get("lesson_id") == lesson["id"] and
       x["fact_id"] in {f"st3-l06-{s}" for s in (
           "a-f022","a-f023","a-f024","a-f025","b-f012","b-f013",
           "b-f014","b-f015","c-f010","c-f011","d-f008","d-f009")}]
section_by_id = {x["id"]: x for x in lesson["sections"]}
for graphic in lesson["infographics"]:
    existing = {fid for node in graphic["nodes"] for fid in node["fact_ids"]}
    for fact in new:
        if fact["fact_id"] in existing:
            continue
        section = section_by_id[fact["section_id"]]
        graphic["nodes"].append({
            "title": section["title"],
            "body": {"en": fact["en"], "te": fact["te"]},
            "fact_ids": [fact["fact_id"]],
            "section_id": fact["section_id"],
            "level": section["level"],
            "source_ids": fact["source_ids"],
        })
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                         encoding="utf-8")
print(f"mapped {len(new)} facts into {len(lesson['infographics'])} atlases")
