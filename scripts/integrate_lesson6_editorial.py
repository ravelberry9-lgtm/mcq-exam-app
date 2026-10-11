"""Integrate the manually reviewed Lesson 6 section drafts into the textbook."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "content/textbooks/st3-ecosystem-biodiversity"

with (BOOK / "manifest.json").open(encoding="utf-8") as handle:
    manifest = json.load(handle)
with (BOOK / "drafts/l6_ab_rewrite.json").open(encoding="utf-8") as handle:
    ab = json.load(handle)
with (BOOK / "drafts/l6_cd_rewrite.json").open(encoding="utf-8") as handle:
    cd = json.load(handle)

lesson = next(item for item in manifest["lessons"]
              if item["id"] == "st3-l06-global-frameworks-conventions")
replacements = {item["id"]: item for item in ab["sections"] + cd["sections"]}
assert set(replacements) == {item["id"] for item in lesson["sections"]}
lesson["sections"] = [replacements[item["id"]] for item in lesson["sections"]]

sources = {
    "src-cbd-treaty": ("CBD Convention Text", "https://www.cbd.int/convention/text", "Objectives and Article 6"),
    "src-cbd-protocols": ("CBD Protocols", "https://www.cbd.int/", "Cartagena and Nagoya Protocols"),
    "src-cbd-gbf": ("Kunming–Montreal Global Biodiversity Framework", "https://www.cbd.int/gbf", "Goals and targets"),
    "src-cbd-cali-fund": ("CBD Cali Fund", "https://www.cbd.int/article/cali-fund-launch-2025", "DSI benefit-sharing mechanism"),
    "src-cites-official": ("CITES Convention", "https://cites.org/eng/disc/text.php", "Appendices, permits and NDF"),
    "src-cms-official": ("Convention on Migratory Species", "https://www.cms.int/", "Convention and appendices"),
    "src-cms-cop15-2026": ("CMS COP15 revised appendices", "https://www.cms.int/news/2026012-revised-cms-appendices", "2026 amendments"),
    "src-ramsar-official": ("Convention on Wetlands", "https://www.ramsar.org/", "Ramsar Sites and Montreux Record"),
    "src-unesco-mab-biosphere-reserves": ("UNESCO Man and the Biosphere Programme", "https://www.unesco.org/en/mab", "MAB functions and zonation"),
    "src-unesco-cold-desert-2025": ("UNESCO Cold Desert Biosphere Reserve", "https://www.unesco.org/en/mab/cold-desert", "India WNBR update"),
    "src-unesco-world-heritage-criteria": ("UNESCO World Heritage criteria", "https://whc.unesco.org/en/criteria/", "Inscription conditions"),
    "src-moefcc-india-biosphere-reserves": ("MoEFCC Biosphere Reserve Programme", "https://moef.gov.in/", "Indian programme and legal context"),
    "src-fao-itpgrfa-overview": ("FAO International Treaty on Plant Genetic Resources", "https://www.fao.org/plant-treaty/overview/en/", "MLS and Farmers' Rights"),
    "src-ipbes-global-assessment-2019": ("IPBES Global Assessment 2019", "https://www.ipbes.net/global-assessment", "Global biodiversity assessment"),
    "src-un-bbnj-official": ("United Nations BBNJ Agreement", "https://www.un.org/bbnjagreement/en", "Treaty text and entry into force"),
    "src-unct-bbnj-status-india": ("UN Treaty Collection — BBNJ status", "https://treaties.un.org/pages/ViewDetails.aspx?chapter=21&mtdsg_no=XXI-10&src=TREATY", "India participation status"),
    "src-gef-conventions-and-funds": ("Global Environment Facility", "https://www.thegef.org/", "GEF, GBFF and financial mechanisms"),
    "src-pib-india-nbsap-2024": ("PIB — India NBSAP 2024–2030", "https://www.pib.gov.in/", "23 National Biodiversity Targets"),
    "src-pib-india-biodiversity-reports-2026": ("PIB — India Seventh CBD National Report", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2240576", "2026 national reporting"),
}
existing = {item["id"] for item in lesson["sources"]}
for source_id, (label, url, locator) in sources.items():
    if source_id not in existing:
        lesson["sources"].append({"id": source_id, "label": label,
                                  "url": url, "locator": locator})

(BOOK / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Normalize Lesson 6 question mappings and type labels without changing content.
section_by_stream = {
    "a": "st3-l06-global-biodiversity-governance-l6-a",
    "b": "st3-l06-global-biodiversity-governance-l6-b",
    "c": "st3-l06-global-biodiversity-governance-l6-c",
    "d": "st3-l06-global-biodiversity-governance-l6-d",
}
question_path = BOOK / "questions.jsonl"
questions = []
for line in question_path.read_text(encoding="utf-8").splitlines():
    row = json.loads(line)
    if row.get("lesson_id") == lesson["id"]:
        for stream, section_id in section_by_stream.items():
            if row["id"].startswith((f"st3-l06-{stream}-", f"st3-l6{stream}-",
                                     f"st3-l06-l6{stream}-")):
                row["section_id"] = section_id
                break
        row["qtype"] = {
            "assertion_reason": "assertion-reason",
            "match-the-following": "match",
            "source_trap": "source-trap",
        }.get(row.get("qtype"), row.get("qtype"))
    questions.append(row)
question_path.write_text("".join(
    json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
    for row in questions), encoding="utf-8")

# Make the section registry reciprocal with the final lesson sections.
map_path = BOOK / "section_map.json"
section_map = json.loads(map_path.read_text(encoding="utf-8"))
for order, section in enumerate(lesson["sections"], 1):
    entry = section_map[section["id"]]
    entry["order"] = order
    entry["fact_ids"] = list(dict.fromkeys(section["fact_ids"]))
    entry["mcq_ids"] = list(dict.fromkeys(section["mcq_ids"]))
map_path.write_text(json.dumps(section_map, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
