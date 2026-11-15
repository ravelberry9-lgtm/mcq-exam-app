import json
from pathlib import Path


path = Path("content/geography/india_ap_chapters/7/Questions.json")
data = json.loads(path.read_text(encoding="utf-8"))

# One-time, manually chosen permutations for the newly added questions.
orders = {
    "IA07-031": [1, 0, 2, 3],
    "IA07-033": [1, 2, 0, 3],
    "IA07-034": [1, 2, 3, 0],
    "IA07-035": [1, 2, 3, 0],
}
for question in data["questions"]:
    order = orders.get(question["id"])
    if order is None:
        continue
    old_answer = question["answer"] - 1
    for field in ("options_te", "options_en", "option_explanations_te", "option_explanations_en"):
        values = question[field]
        question[field] = [values[index] for index in order]
    question["answer"] = order.index(old_answer) + 1

path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
