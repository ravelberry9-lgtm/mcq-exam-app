"""Read-only loader for the hash-locked local AP History HTML corpus."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flask import current_app

EXPECTED_MANIFEST_SHA256 = "48BCBB69D4F01ACE966F418CC18BC3C8AB5F20CE57A2A1552B59E7A35C596447"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def root() -> Path:
    return Path(current_app.config["AP_HISTORY_CANONICAL_ROOT"]).resolve()


def all_chapters() -> list[dict]:
    if not current_app.config.get("AP_HISTORY_CANONICAL_ENABLED", False):
        return []
    base = root()
    try:
        data = json.loads((base / "index.json").read_text(encoding="utf-8"))
        rows = data["chapters"]
        if data.get("format") != "ap-history-canonical-html-v1" or data.get("manifest_sha256") != EXPECTED_MANIFEST_SHA256:
            return []
        if len(rows) != 31 or {r["chapter"] for r in rows} != set(range(1, 32)) or len({r["slug"] for r in rows}) != 31:
            return []
        for row in rows:
            path = (base / row["html_file"]).resolve()
            if not path.is_relative_to(base) or not path.is_file() or _sha(path) != row["html_sha256"]:
                return []
        return sorted(rows, key=lambda r: r["chapter"])
    except (OSError, ValueError, KeyError, TypeError):
        current_app.logger.warning("Canonical AP History textbook package rejected")
        return []


def load(slug: str) -> dict | None:
    rows = all_chapters()
    for index, row in enumerate(rows):
        if row["slug"] == slug:
            item = dict(row)
            item["previous"] = rows[index - 1] if index else None
            item["following"] = rows[index + 1] if index + 1 < len(rows) else None
            return item
    return None


def html_path(item: dict) -> Path | None:
    base = root()
    path = (base / item["html_file"]).resolve()
    return path if path.is_relative_to(base) and path.is_file() and _sha(path) == item["html_sha256"] else None
