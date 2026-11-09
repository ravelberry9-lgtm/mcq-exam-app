import json
from pathlib import Path

from flask import Blueprint, abort, redirect, render_template, send_from_directory, url_for

bp = Blueprint("polity", __name__, url_prefix="/learn/polity")
CONTENT_ROOT = Path(__file__).resolve().parents[2] / "content" / "polity" / "g2"
SHARED = CONTENT_ROOT / "_shared"
UNIT = CONTENT_ROOT / "6.1" / "6.1.1"


@bp.get("/g2/references/laxmikanth/<int:chapter>")
def lax_reference_chapter(chapter):
    return send_from_directory(CONTENT_ROOT / "references" / "laxmikanth", f"chapter-{chapter:03d}.html")


@bp.get("/g2/master-index")
def master_index():
    return redirect(url_for('polity_unit6.home'))


def master_data():
    return json.loads((CONTENT_ROOT / "MASTER-INDEX.json").read_text(encoding="utf-8-sig"))


def master_chapter(chapter_id):
    data = master_data()
    for unit in data["units"]:
        for section in unit["sections"]:
            for row in section["chapters"]:
                if row["id"] == chapter_id:
                    return row, row.get("legacy_storage_id")
    alias = data.get("legacy_aliases", {}).get(chapter_id)
    if alias:
        row, legacy = master_chapter(alias)
        return row, legacy
    abort(404)


def chapter_directory(row, legacy):
    directory = CONTENT_ROOT / ".".join(row["id"].split(".")[:2]) / row["id"]
    if not (directory / "index.html").is_file():
        abort(404)
    return directory


def normalise_explanations(data):
    """Accept the two authored chapter wrappers and legacy flat records."""
    if "questions" in data:
        return {"questions": data["questions"], "tables": data.get("tables", {})}
    if isinstance(data.get("explanations"), dict):
        return {"questions": data["explanations"], "tables": data.get("tables", {})}
    return {"questions": data, "tables": {}}


def canonical_question_bundle(chapter_id, question_id, shared_explanations):
    """Load one canonical chapter question with its authored rationale and guide."""
    source_row, source_legacy = master_chapter(chapter_id)
    source_directory = chapter_directory(source_row, source_legacy)
    source_bank = json.loads((source_directory / "Questions.json").read_text(encoding="utf-8-sig"))
    matches = [question for question in source_bank["questions"] if question["id"] == question_id]
    if len(matches) != 1:
        abort(500, description="Invalid canonical question reference")
    question = matches[0]
    source_explanation_path = source_directory / "Explanations.json"
    source_local = normalise_explanations(
        json.loads(source_explanation_path.read_text(encoding="utf-8-sig"))
        if source_explanation_path.is_file() else {}
    )
    source_explanations = {
        key: {**shared_explanations[key], **source_local[key]}
        for key in ("questions", "tables")
    }
    explanation_id = question.get("explanation_id", question["id"])
    if explanation_id not in source_explanations["questions"]:
        abort(500, description="Missing canonical question explanation")
    explanation = source_explanations["questions"][explanation_id]
    table_id = explanation.get("table_id")
    table = None
    if table_id:
        table = source_explanations["tables"].get(table_id)
        if table is None:
            abort(500, description="Missing canonical concept guide")
    return source_row, question, explanation_id, explanation, table_id, table


@bp.get("/")
def polity_home():
    return redirect(url_for("polity.master_index"))


@bp.get("/g2/6.1")
@bp.get("/g2/6.1/")
def section_61():
    return canonical_section(6, 1)


@bp.get("/g2/<int:unit>/<int:section>/")
def canonical_section(unit, section):
    section_id = f"{unit}.{section}"
    for item in master_data()["units"]:
        for entry in item["sections"]:
            if entry["id"] == section_id:
                return render_template("ds/polity_section.html", section=entry)
    abort(404)


@bp.get("/g2/6.1/1")
def unit_61():
    questions = json.loads((UNIT / "Questions.json").read_text(encoding="utf-8-sig"))
    pyqs = json.loads((SHARED / "PYQs.json").read_text(encoding="utf-8-sig"))
    shared_explanations = normalise_explanations(json.loads((SHARED / "Explanations.json").read_text(encoding="utf-8-sig")))
    local_path = UNIT / "Explanations.json"
    local_explanations = normalise_explanations(json.loads(local_path.read_text(encoding="utf-8-sig"))) if local_path.exists() else {"questions": {}, "tables": {}}
    explanations = {
        key: {**shared_explanations[key], **local_explanations[key]}
        for key in ("questions", "tables")
    }
    for question in pyqs:
        explanation_id = question.get("explanation_id", question["id"])
        if explanation_id in shared_explanations["questions"]:
            explanations["questions"][explanation_id] = shared_explanations["questions"][explanation_id]
    pyq_mapping = json.loads((SHARED / "PYQ-mapping.json").read_text(encoding="utf-8-sig"))
    expected = json.loads((SHARED / "Expected-Questions.json").read_text(encoding="utf-8-sig"))
    return render_template(
        "ds/polity_unit.html", questions=questions["questions"],
        pyqs=[q for q in pyqs if pyq_mapping.get(q["id"], {}).get("primary_subchapter") == "6.1.1"],
        explanations=explanations, pyq_mapping=pyq_mapping,
        expected=[q for q in expected if q.get("primary_subchapter") == "6.1.1"],
    )


@bp.get("/g2/6.1/notes")
def notes():
    return send_from_directory(UNIT, "Notes.html")


@bp.get("/g2/6.1/laxmikanth")
def laxmikanth():
    return send_from_directory(UNIT, "Laxmikanth.html")


@bp.get("/g2/6.1/group-one")
def group_one():
    return send_from_directory(UNIT, "Group-I.html")


@bp.get("/g2/6.1/2/")
@bp.get("/g2/6.1/2/<any(Notes.html,Laxmikanth.html):filename>")
def chapter_two_reader(filename="index.html"):
    return send_from_directory(CONTENT_ROOT / "6.1" / "6.1.2", filename)


@bp.get("/g2/6.1/2/practice")
def chapter_two_practice():
    return redirect("/learn/polity/g2/6/1/2/practice", code=302)


@bp.get("/g2/6.1/3/")
@bp.get("/g2/6.1/3/<any(Notes.html,Laxmikanth.html):filename>")
def chapter_three_reader(filename="index.html"):
    return send_from_directory(CONTENT_ROOT / "6.1" / "6.1.3", filename)


@bp.get("/g2/6.1/3/practice")
def chapter_three_practice():
    return redirect("/learn/polity/g2/6/1/3/practice", code=302)


@bp.get("/g2/6.1/4/")
@bp.get("/g2/6.1/4/<any(Notes.html,Laxmikanth.html,'Group-I.html'):filename>")
def chapter_four_reader(filename="index.html"):
    return send_from_directory(CONTENT_ROOT / "6.1" / "6.1.4", filename)


@bp.get("/g2/6.1/4/practice")
def chapter_four_practice():
    return redirect("/learn/polity/g2/6/1/4/practice", code=302)


@bp.get("/g2/<int:unit>/<int:section>/<int:chapter>/")
@bp.get("/g2/<int:unit>/<int:section>/<int:chapter>/<any(Notes.html,Laxmikanth.html,'Group-I.html','Teaching-Guide.html','Publisher-review.html','PYQ-review.html','Source-qualifications.html','Chapter-Test.html','Chapter-Test-Answers.html'):filename>")
def catalog_chapter_reader(unit, section, chapter, filename="index.html"):
    requested = f"{unit}.{section}.{chapter}"
    row, legacy = master_chapter(requested)
    if requested != row["id"]:
        a, b, c = map(int, row["id"].split("."))
        return redirect(url_for("polity.catalog_chapter_reader", unit=a, section=b, chapter=c, **({"filename": filename} if filename != "index.html" else {})))
    directory = chapter_directory(row, legacy)
    if legacy == "6.1.1":
        if filename == "index.html":
            return unit_61()
        if filename == "Laxmikanth.html":
            filename = "Laxmikanth.html"
    return send_from_directory(directory, filename)


@bp.get("/g2/<int:unit>/<int:section>/<int:chapter>/practice")
def catalog_chapter_practice(unit, section, chapter):
    requested = f"{unit}.{section}.{chapter}"
    row, legacy = master_chapter(requested)
    if requested != row["id"]:
        a, b, c = map(int, row["id"].split("."))
        return redirect(url_for("polity.catalog_chapter_practice", unit=a, section=b, chapter=c))
    directory = chapter_directory(row, legacy)
    bank = json.loads((directory / "Questions.json").read_text(encoding="utf-8-sig"))
    local_path = directory / "Explanations.json"
    local = json.loads(local_path.read_text(encoding="utf-8-sig")) if local_path.is_file() else {}
    local = normalise_explanations(local)
    # A repeated concept can reuse its canonical question and explanation.
    questions = list(bank["questions"])
    question_ids = {question["id"] for question in questions}
    referenced = {"questions": {}, "tables": {}}
    shared_explanation_path = SHARED / "Explanations.json"
    shared_source_explanations = normalise_explanations(
        json.loads(shared_explanation_path.read_text(encoding="utf-8-sig"))
        if shared_explanation_path.is_file() else {}
    )
    for reference in bank.get("question_references", []):
        source_row, source_question, explanation_id, explanation, table_id, table = canonical_question_bundle(
            reference["chapter"], reference["id"], shared_source_explanations
        )
        if reference["id"] in question_ids:
            abort(500, description="Invalid or duplicate canonical question reference")
        question = {**source_question, "reused_from_chapter": source_row["id"]}
        questions.append(question)
        question_ids.add(question["id"])
        referenced["questions"][explanation_id] = explanation
        if table_id:
            referenced["tables"][table_id] = table
    def section_data(filename, default):
        path = SHARED / filename
        return json.loads(path.read_text(encoding="utf-8-sig")) if path.is_file() else default
    mapping = section_data("PYQ-mapping.json", {})
    pyqs = [q for q in section_data("PYQs.json", []) if mapping.get(q["id"], {}).get("primary_subchapter") == row["id"]]
    # Staged chapter banks may still contain the now-published canonical PYQ.
    # Display its shared record once, in the PYQ section before practice.
    published_pyq_ids = {question["id"] for question in pyqs}
    related_pyqs = [q for q in section_data("PYQs.json", [])
                    if q["id"] not in published_pyq_ids
                    and row["id"] in mapping.get(q["id"], {}).get("related_master_subchapters", [])]
    displayed_pyq_ids = published_pyq_ids | {question["id"] for question in related_pyqs}
    questions = [question for question in questions if question["id"] not in displayed_pyq_ids]
    expected_records = [q for q in section_data("Expected-Questions.json", []) if q.get("primary_subchapter") == row["id"]]
    expected = []
    expected_question_ids = set()
    for record in expected_records:
        if record.get("kind") != "canonical-expected-reference":
            if record["id"] in expected_question_ids:
                abort(500, description="Duplicate Expected question")
            expected.append(record)
            expected_question_ids.add(record["id"])
            continue
        source_row, source_question, explanation_id, explanation, table_id, table = canonical_question_bundle(
            record["canonical_chapter"], record["canonical_question_id"], shared_source_explanations
        )
        if source_question["id"] in expected_question_ids:
            abort(500, description="Duplicate canonical Expected question reference")
        question = {
            **source_question,
            "kind": "canonical-expected-reference",
            "primary_subchapter": row["id"],
            "parent_pyq_id": record["parent_pyq_id"],
            "sources": record.get("sources", source_question.get("sources", {})),
            "expected_reference_id": record["id"],
            "expected_canonical_reuse_from_chapter": source_row["id"],
            "new_original_count": 0,
        }
        expected.append(question)
        expected_question_ids.add(question["id"])
        referenced["questions"][explanation_id] = explanation
        if table_id:
            referenced["tables"][table_id] = table
    # A canonical Expected reference is shown exactly once in the Expected section,
    # not again as an ordinary page-wise card in its home chapter.
    questions = [question for question in questions if question["id"] not in expected_question_ids]
    shared = section_data("Explanations.json", {})
    explanations = {key: {**shared.get(key, {}), **referenced[key], **local.get(key, {})} for key in ("questions", "tables")}
    for question_id in displayed_pyq_ids:
        if question_id in shared.get("questions", {}):
            explanations["questions"][question_id] = shared["questions"][question_id]
    publisher_questions = []
    publisher_path = directory / "Publisher-Questions.json"
    if publisher_path.is_file():
        publisher_bank = json.loads(publisher_path.read_text(encoding="utf-8-sig"))
        for item in publisher_bank.get("items", []):
            if not item.get("practice_approved") or not item.get("scored"):
                continue
            question = dict(item)
            answer = question.get("study_answer")
            if answer not in (1, 2, 3, 4) or not question.get("question_en") or len(question.get("options_en", [])) != 4 or len(question.get("options_te", [])) != 4 or question.get("explanation_id") not in explanations["questions"]:
                abort(500, description="Incomplete approved publisher question")
            question["answer"] = answer
            publisher_questions.append(question)
    bank_pyqs = []
    bank_pyq_path = directory / "PYQ-Set.json"
    if bank_pyq_path.is_file():
        bank_pyqs = json.loads(bank_pyq_path.read_text(encoding="utf-8-sig")).get("questions", [])
        for question in bank_pyqs:
            if question.get("scored") and (question.get("study_answer") not in (1, 2, 3, 4)
                    or question.get("study_answer") != question.get("official_key")
                    or question.get("key_status") in ("disputed", "no_official_key", "needs_user_decision")):
                abort(500, description="Invalid scored PYQ transcription")
    return render_template(
        "ds/polity_chapter_practice.html", questions=questions,
        explanations=explanations, chapter_title=row["id"] + " · " + row["title"], reader_url="./",
        pyqs=pyqs, related_pyqs=related_pyqs, expected=expected, pyq_mapping=mapping, publisher_questions=publisher_questions, bank_pyqs=bank_pyqs,
        pyq_review_url="./PYQ-review.html" if (directory / "PYQ-review.html").is_file() else None,
        chapter_test_url="./Chapter-Test.html" if (directory / "Chapter-Test.html").is_file() else None,
    )
