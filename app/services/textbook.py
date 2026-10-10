"""Versioned textbook packages. Read-only; drafts are admin-only, fail closed."""
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from flask import current_app

ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
ANCHOR = re.compile(r"[A-Za-z0-9_-]{1,64}\Z")


class PackageError(ValueError):
    pass


def validate(data, slug):
    def require(ok, message):
        if not ok:
            raise PackageError(message)

    def bilingual(item):
        require(isinstance(item, dict), "Bilingual object required")
        require(all(isinstance(item.get(k), str) and item[k].strip() for k in ("en", "te")), "Both languages required")

    require(isinstance(data, dict), "Package must be an object")
    require(data.get("format") == "ap-textbook-v1" and data.get("chapter_slug") == slug, "Wrong format/chapter")
    require(data.get("status") in ("draft", "approved"), "Invalid status")
    require(isinstance(data.get("version"), str) and data["version"].strip(), "Version required")
    bilingual(data.get("title"))
    lessons = data.get("lessons")
    require(isinstance(lessons, list) and lessons, "Lessons required")
    seen, aliases = set(), set()
    for lesson in lessons:
        require(isinstance(lesson, dict), "Lesson must be an object")
        key = lesson.get("id", "")
        require(isinstance(key, str) and ID.fullmatch(key) and key not in seen, "Invalid/duplicate lesson id")
        seen.add(key)
        bilingual(lesson.get("title"))
        require(isinstance(lesson.get("subtopic_slugs"), list) and lesson["subtopic_slugs"] and all(isinstance(x, str) and ID.fullmatch(x) for x in lesson["subtopic_slugs"]), "Canonical subtopics required")
        sources = lesson.get("sources", [])
        require(isinstance(sources, list), "Sources must be a list")
        source_ids = set()
        for source in sources:
            require(isinstance(source, dict), "Invalid source")
            sid = source.get("id", "")
            require(isinstance(sid, str) and ID.fullmatch(sid) and sid not in source_ids, "Invalid source id")
            source_ids.add(sid)
            require(isinstance(source.get("label"), str) and bool(source["label"].strip()), "Source label required")
            url = source.get("url", "")
            require(isinstance(url, str), "Invalid source URL")
            require((urlsplit(url).scheme in ("http", "https") and bool(urlsplit(url).netloc)) if url else bool(source.get("locator")), "Unsafe URL or missing book locator")
        sections = lesson.get("sections")
        require(isinstance(sections, list) and sections, "Sections required")
        section_ids, facts = set(), set()
        for section in sections:
            require(isinstance(section, dict), "Invalid section")
            sid = section.get("id", "")
            require(isinstance(sid, str) and ID.fullmatch(sid) and sid not in section_ids, "Invalid/duplicate section id")
            section_ids.add(sid)
            require(section.get("level") in ("group2", "group1"), "Invalid level")
            bilingual(section.get("title"))
            ps = section.get("paragraphs")
            require(isinstance(ps, list) and ps, "Teaching paragraphs required")
            for p in ps:
                bilingual(p)
            fids, refs = section.get("fact_ids"), section.get("source_ids")
            require(isinstance(fids, list) and fids and all(isinstance(x, str) and ID.fullmatch(x) for x in fids), "Fact ids required")
            require(isinstance(refs, list) and refs and all(isinstance(x, str) for x in refs) and set(refs) <= source_ids, "Unresolved evidence")
            facts.update(fids)
        require(any(s["level"] == "group2" for s in sections), "Group 2 foundation required")
        maps = lesson.get("note_anchors", {})
        require(isinstance(maps, dict), "Anchor map required")
        for anchor, section_id in maps.items():
            require(isinstance(anchor, str) and ANCHOR.fullmatch(anchor) and anchor not in aliases and isinstance(section_id, str) and section_id in section_ids, "Invalid/ambiguous note mapping")
            aliases.add(anchor)
        graphics = lesson.get("infographics", [])
        require(isinstance(graphics, list), "Infographics must be a list")
        types = set()
        for graphic in graphics:
            require(isinstance(graphic, dict) and graphic.get("kind") in ("teaching", "revision") and graphic["kind"] not in types, "Invalid/duplicate infographic type")
            types.add(graphic["kind"])
            bilingual(graphic.get("title"))
            nodes = graphic.get("nodes")
            require(isinstance(nodes, list) and nodes, "Diagram nodes required")
            covered = set()
            for node in nodes:
                require(isinstance(node, dict), "Invalid diagram node")
                bilingual(node.get("title"))
                bilingual(node.get("body"))
                refs = node.get("fact_ids")
                require(isinstance(refs, list) and refs and all(isinstance(x, str) for x in refs) and set(refs) <= facts, "Infographic contains untracked facts")
                covered.update(refs)
            if graphic["kind"] == "teaching":
                require(covered == facts, "Detailed infographic must cover every lesson fact")
                if graphic.get("coverage_type") == "full-paragraph-atlas":
                    expected = {}
                    for section in sections:
                        require(len(section["paragraphs"]) == len(section["fact_ids"]), "Atlas locator count mismatch")
                        for paragraph, fid in zip(section["paragraphs"], section["fact_ids"]):
                            require(fid not in expected, "Atlas locators must be unique")
                            expected[fid] = (section, paragraph)
                    require(len(nodes) == len(expected), "Atlas paragraph omitted or duplicated")
                    atlas_seen = set()
                    for node in nodes:
                        require(len(node["fact_ids"]) == 1, "Atlas node must identify one paragraph")
                        fid = node["fact_ids"][0]
                        require(fid not in atlas_seen, "Atlas paragraph duplicated")
                        atlas_seen.add(fid)
                        section, paragraph = expected[fid]
                        require(node["body"] == paragraph, "Atlas must preserve exact bilingual teaching")
                        require(node.get("section_id") == section["id"] and node.get("level") == section["level"], "Atlas context mismatch")
                        require(node.get("source_ids") == section["source_ids"], "Atlas source mismatch")
        if data["status"] == "approved":
            require(types == {"teaching", "revision"}, "Both infographic types required for publication")
            require(any(s["level"] == "group1" for s in sections), "Group 1 depth required for publication")
            review = lesson.get("review", {})
            require(isinstance(review, dict) and all(review.get(x) is True for x in ("coverage", "factual", "language", "infographics")), "Editorial approval required")
    return data


def load(slug, admin=False):
    if not current_app.config.get("TEXTBOOK_ENABLED", False) or not ID.fullmatch(slug):
        return None
    root = Path(current_app.config.get("TEXTBOOK_ROOT", Path(current_app.root_path).parent / "content" / "textbooks")).resolve()
    path = (root / slug / "manifest.json").resolve()
    if not path.is_relative_to(root) or not path.is_file():
        return None
    try:
        data = validate(json.loads(path.read_text(encoding="utf-8")), slug)
    except (ValueError, TypeError, KeyError, OSError):
        current_app.logger.warning("Textbook package rejected for %s", slug)
        return None
    return data if data["status"] == "approved" or admin else None


def note_target(data, anchor):
    for lesson in data["lessons"]:
        if anchor in lesson.get("note_anchors", {}):
            return lesson["id"], lesson["note_anchors"][anchor]
    return None
