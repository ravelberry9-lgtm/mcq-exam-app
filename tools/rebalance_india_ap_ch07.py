import json
from pathlib import Path


path = Path(__file__).resolve().parents[1] / "content/geography/india_ap_chapters/7/Questions.json"
data = json.loads(path.read_text(encoding="utf-8"))

# New order is expressed as old zero-based option indexes. The same permutation is
# applied to Telugu, English and both explanation arrays; the scientific answer is unchanged.
orders = {
    "IA07-006": [1, 0, 2, 3],
    "IA07-010": [1, 0, 2, 3],
    "IA07-014": [1, 0, 2, 3],
    "IA07-019": [1, 0, 2, 3],
}

for question in data["questions"]:
    order = orders.get(question["id"])
    if order is None:
        continue
    old_answer_index = question["answer"] - 1
    for field in ("options_te", "options_en", "option_explanations_te", "option_explanations_en"):
        old = question[field]
        question[field] = [old[index] for index in order]
    question["answer"] = order.index(old_answer_index) + 1

path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
