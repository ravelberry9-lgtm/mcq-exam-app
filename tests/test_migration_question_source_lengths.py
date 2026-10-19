import ast
from pathlib import Path

from app.models import Question


def test_question_source_literals_fit_database_column():
    """Keep migration inserts compatible with PostgreSQL's VARCHAR limit."""
    source_limit = Question.__table__.c.source.type.length
    migrations = Path(__file__).parents[1] / "migrations" / "versions"
    violations = []

    for path in migrations.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Dict):
                continue

            literal_items = {
                key.value: value.value
                for key, value in zip(node.keys, node.values)
                if isinstance(key, ast.Constant)
                and isinstance(key.value, str)
                and isinstance(value, ast.Constant)
                and isinstance(value.value, str)
            }
            # Question insert dictionaries carry both fields; trace dictionaries do not.
            if "source_file" not in literal_items or "source" not in literal_items:
                continue

            source = literal_items["source"]
            if len(source) > source_limit:
                violations.append(
                    f"{path.name}:{node.lineno} source={source!r} "
                    f"({len(source)} > {source_limit})"
                )

    assert not violations, "Question.source values exceed the database limit:\n" + "\n".join(violations)
