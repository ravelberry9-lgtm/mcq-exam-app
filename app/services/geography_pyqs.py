"""Source-preserving geography PYQs with server-enforced scoring holds."""
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlsplit
import html
import json
import re
import markdown
import bleach
from flask import current_app


@lru_cache(maxsize=4)
def _read(path, modified):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if (data.get("format") != "geography-pyq-release-v1"
            or len(data.get("records", [])) != 976
            or sum(r.get("must_disable_scoring") is True for r in data["records"]) != 244):
        raise ValueError("Invalid geography release controls")
    records = data["records"]
    if len({r["source"]["id"] for r in records}) != 976:
        raise ValueError("Duplicate geography PYQ IDs")
    return records


def records():
    path = Path(current_app.root_path).parent / "content/geography/pyqs.json"
    return _read(str(path), path.stat().st_mtime_ns)


def question(question_id):
    return next((r for r in records() if r["source"]["id"] == question_id), None)


def options(record):
    source = record["source"]
    bilingual = source.get("options_bilingual")
    if isinstance(bilingual, str):
        matches = list(re.finditer(r"(?:^|;\s*)(?:\(([1-4])\)|([1-4])\.(?=\s))\s*", bilingual))
        if [m[1] or m[2] for m in matches] == ["1", "2", "3", "4"]:
            bilingual = [bilingual[m.end():matches[i+1].start() if i+1 < 4 else len(bilingual)].strip()
                         for i, m in enumerate(matches)]
    en, te = source.get("options_en"), source.get("options_te")
    if isinstance(en, list) and len(en) == 4 and all(isinstance(x, str) and x.strip() for x in en):
        if isinstance(te, list) and len(te) == 4 and all(isinstance(x, str) and x.strip() for x in te):
            return [{"number": i+1, "text": v, "te": te[i]} for i, v in enumerate(en)]
        if isinstance(bilingual, list) and len(bilingual) == 4 and all(isinstance(x, str) and x.strip() for x in bilingual):
            return [{"number": i+1, "text": v, "te": ""} for i, v in enumerate(bilingual)]
        return [{"number": i+1, "text": v, "te": ""} for i, v in enumerate(en)]
    if isinstance(bilingual, list) and len(bilingual) == 4 and all(isinstance(x, str) and x.strip() for x in bilingual):
        return [{"number": i+1, "text": v, "te": ""} for i, v in enumerate(bilingual)]
    return []


def accepted_options(record):
    """Use explicit option numbers only; conflicting or incomplete keys fail closed."""
    source = record["source"]
    if (record.get("must_disable_scoring") is not False
            or source.get("practice_scorable") is not True
            or source.get("editorial_quarantine") is not False
            or source.get("answer_available") is not True
            or len(options(record)) != 4):
        return ()
    text = str(source.get("answer_text") or "").strip()
    if source.get("answer_status") == "multiple_accepted":
        match = re.fullmatch(r"Multiple accepted answers\s*[—-]\s*([1-4]) and ([1-4])\.", text)
        return tuple(sorted({int(match[1]), int(match[2])})) if match else ()
    if source.get("answer_status") not in {"single", "official_final_key", "editorially_reviewed", "editorially_reviewed_against_official_paper"}:
        return ()
    values = []
    for key in ("answer_index", "final_answer_index"):
        value = source.get(key)
        if value is not None:
            if type(value) is not int or value not in (1, 2, 3, 4):
                return ()
            values.append(value)
    match = re.match(r"^(?:Option\s+)?([1-4])(?:$|\s|[.])", text, re.I)
    if match:
        values.append(int(match[1]))
    if not values or len(set(values)) != 1:
        return ()
    return (values[0],)


def grade(record, choice):
    """Holds ignore any client-supplied key, score or eligibility fields."""
    accepted = accepted_options(record)
    if not accepted:
        return {"status": "unscored", "score": None, "correct": None}
    if type(choice) is not int or choice not in (1, 2, 3, 4):
        raise ValueError("Choose an option from 1 to 4")
    correct = choice in accepted
    return {"status": "scored", "score": int(correct), "correct": correct}


def rich(text):
    # Escape source HTML before Markdown; tables and statements retain their structure.
    rendered = markdown.markdown(html.escape(str(text or "")), extensions=["tables"])
    return bleach.clean(rendered,
                        tags={"p", "br", "strong", "em", "ul", "ol", "li", "table", "thead", "tbody", "tr", "th", "td", "code", "pre", "blockquote", "hr", "a"},
                        attributes={"a": ["href", "title"]}, protocols={"https", "http"}, strip=True)


def display(record):
    source = record["source"]
    explanation = ""
    match = re.search(r"\*\*Explanation:\*\*\s*(.*?)(?=\n\*\*|\n---|\Z)", source.get("record_markdown") or "", re.S)
    if match:
        explanation = match[1].strip()
    links = []
    for key, label in (("source_url", "Original paper / source"), ("official_key_url", "Answer key source")):
        url = source.get(key)
        if isinstance(url, str) and urlsplit(url).scheme in {"https", "http"} and urlsplit(url).netloc:
            links.append({"url": url, "label": label})
    # This inherited Telugu field gives the solved matching pairs, rather than a prompt.
    solved_te = source["id"] == "APPSC-G2-GEO-0043"
    return {"record": record, "source": source, "options": options(record),
            "stem_en": rich(source.get("question_en")),
            "stem_te": rich(source.get("question_te")) if not solved_te else "",
            "study_te": rich(source.get("question_te")) if solved_te else "",
            "explanation": rich(explanation), "links": links,
            "scorable": bool(accepted_options(record))}


def filtered(unit=None, lesson=None, exam=None, year=None, mode=None, search=None):
    result = []
    needle = (search or "").strip().casefold()
    for record in records():
        source = record["source"]
        if unit and not any(str(r["unit"]) == str(unit) for r in record["routes"]):
            continue
        if lesson and not any(r["lesson_id"] == lesson for r in record["routes"]):
            continue
        if exam and source.get("exam") != exam:
            continue
        if year and str(source.get("year")) != year:
            continue
        if mode == "held" and not record["must_disable_scoring"]:
            continue
        if mode == "scored" and not accepted_options(record):
            continue
        if needle and needle not in " ".join(str(source.get(k) or "") for k in ("id", "question_en", "question_te", "exam", "topic")).casefold():
            continue
        result.append(record)
    return result


def summary(items=None):
    items = records() if items is None else items
    return {"total": len(items), "held": sum(r["must_disable_scoring"] for r in items),
            "scorable": sum(bool(accepted_options(r)) for r in items)}
