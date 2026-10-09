"""Expanded notes: parse a package's bilingual core + addendum notes and load them as a collection that is SEPARATE from the
17 legacy ``notes`` rows.

* Parsing is pure (no database); loading is preview by default and add-only (an existing anchor is never overwritten: identical
  content is ``unchanged``, differing content is reported as a ``conflict`` and left alone).
* Anchors are stable ids from the package's ``note_anchors.json`` (CH01-S14, CH01-A04). The package's section numbers
  (1..50) are stored as ``package_section`` and are never treated as app note section numbers.
* The destination chapter is the canonical syllabus chapter found by slug, so nothing depends on a database id.
* Explicit mapping to the existing app sections is a separate, reviewable table (``ExpandedNoteAppMap``): rows start as
  ``draft`` and only ``approved`` rows are shown to learners.
"""
import hashlib
import json
import re
from pathlib import Path

from ..db import db
from ..models import ExpandedNote, ExpandedNoteAppMap, Note, Chapter, Subject, SyllabusChapter

FORMAT = "ap-history-note-anchors-v1"
TELUGU = re.compile("[ఀ-౿]")
URL = re.compile(r"^(https?://\S+)(?:\s+\((.+)\))?\s*$")
ANCHOR = re.compile(r"CH\d{2}-[A-Z]+\d*-?\d*")
CORE_CONN = re.compile(r"CH\d{2}-S\d{2}")
LABEL = re.compile(r"^(Sources?|Reading basis|Evidence links?|Additional source|Additional bibliographic corroboration|"
                   r"Institutional corroboration|Editorial locator)\s*:\s*(.*)$")
CONN_LINE = re.compile(r"^(Core|Core connections?|Expanded core connections?)\s*:\s*(.*)$")
CORE_HEAD = re.compile(r"^(\d{2})\.\s+(.+)$")
G1_HEAD = re.compile(r"^G1-(\d{2})\.\s+(.+)$")
ADD_HEAD = re.compile(r"^(CH\d{2}-A\d{2})\.\s+(.+)$")
GROUP_HEAD = re.compile(r"^GROUP1 (CONNECTION|ADDITION)\b[^/]*/\s*(.+)$")


class NotesError(Exception):
    pass


def _split_heading(rest):
    """'ENGLISH / తెలుగు' -> (en, te); the separator is the last ' / ' (English headings can hold a slash-free phrase only)."""
    if " / " in rest:
        en, te = rest.rsplit(" / ", 1)
        if TELUGU.search(te):
            return en.strip(), te.strip()
    return rest.strip(), ""


class _Item:
    def __init__(self, anchor_id, kind, en, te, section=None):
        self.anchor_id, self.kind, self.heading_en, self.heading_te, self.package_section = anchor_id, kind, en, te, section
        self.en, self.te, self.sources, self.connections, self.unparsed = [], [], [], [], []
        self._label, self._label_has_url = None, False
        self._last = None

    def _flush_label(self):
        if self._label and not self._label_has_url:
            self.sources.append({"label": self._label, "url": None})
        self._label, self._label_has_url = None, False

    def feed(self, line):
        s = line.strip()
        if not s:
            return
        if s.startswith("EN:"):
            self._flush_label(); self.en.append(s[3:].strip()); self._last = "en"; return
        if s.startswith("TE:"):
            self._flush_label(); self.te.append(s[3:].strip()); self._last = "te"; return
        m = CONN_LINE.match(s)
        if m:
            self._flush_label(); self.connections += CORE_CONN.findall(m.group(2)); self._last = None; return
        m = LABEL.match(s)
        if m:
            self._flush_label()
            self._label, self._label_has_url = (m.group(2).strip().rstrip(":").strip() or m.group(1)), False
            self._last = None
            return
        m = URL.match(s)
        if m:
            self.sources.append({"label": self._label, "url": m.group(1), **({"locator": m.group(2)} if m.group(2) else {})})
            self._label_has_url = True
            return
        # an unlabelled line: an English or Telugu continuation / closing sentence of the body
        self._flush_label()
        (self.te if TELUGU.search(s) else self.en).append(s)

    def finish(self):
        self._flush_label()
        seen, out = set(), []
        for c in self.connections:
            if c not in seen:
                seen.add(c); out.append(c)
        self.connections = out
        return self

    def as_dict(self, order):
        body_en, body_te = "\n\n".join(self.en), "\n\n".join(self.te)
        payload = json.dumps([self.heading_en, self.heading_te, body_en, body_te, self.sources, self.connections],
                             ensure_ascii=False, sort_keys=True)
        return {"anchor_id": self.anchor_id, "kind": self.kind, "package_section": self.package_section, "sort_order": order,
                "heading_en": self.heading_en, "heading_te": self.heading_te, "body_en": body_en, "body_te": body_te,
                "sources": self.sources, "core_connections": self.connections or None,
                "content_hash": hashlib.md5(payload.encode("utf-8")).hexdigest()}


def parse_core(text, prefix):
    items, cur = [], None
    for raw in text.splitlines():
        s = raw.strip()
        m = CORE_HEAD.match(s)
        g = G1_HEAD.match(s)
        if m and " / " in m.group(2):
            cur and items.append(cur.finish())
            en, te = _split_heading(m.group(2))
            cur = _Item(f"{prefix}-S{m.group(1)}", "core", en, te, int(m.group(1)))
        elif g and " / " in g.group(2):
            cur and items.append(cur.finish())
            en, te = _split_heading(g.group(2))
            cur = _Item(f"{prefix}-G1-{g.group(1)}", "group1", en, te)
        elif s.startswith("PART C"):
            cur and items.append(cur.finish())
            en, te = _split_heading(s[len("PART C"):].lstrip(" —-"))
            cur = _Item(f"{prefix}-QR", "revision", en, te)
        elif s.startswith(("PART A", "PART B", "GROUP 2", "GROUP 1", "EDITORIAL STATUS")):
            cur and items.append(cur.finish())
            cur = None
        elif cur is not None:
            cur.feed(s)
    cur and items.append(cur.finish())
    return items


def parse_addendum(text, prefix):
    items, cur, since_group, gcount = [], None, [], 0
    for raw in text.splitlines():
        s = raw.strip()
        a = ADD_HEAD.match(s)
        g = GROUP_HEAD.match(s)
        if a and " / " in a.group(2):
            cur and items.append(cur.finish())
            en, te = _split_heading(a.group(2))
            cur = _Item(a.group(1), "addendum", en, te)
            since_group.append(cur)
        elif g:
            cur and items.append(cur.finish())
            gcount += 1
            label = "Group 1 connection" if g.group(1) == "CONNECTION" else "Group 1 addition"
            full = s.split("/", 1)
            en = (full[0].strip().title() if g.group(1) == "CONNECTION" else full[0].strip().split(":", 1)[-1].strip().title()) or label
            cur = _Item(f"{prefix}-AG1-{gcount:02d}", "addendum_group1", en, g.group(2).strip())
            cur.connections = [c for it in since_group for c in it.connections]
            since_group = []
        elif cur is not None:
            cur.feed(s)
    cur and items.append(cur.finish())
    return items


def parse_package_notes(pkg_dir):
    """Return (items, anchors_json, problems, warnings). ``items`` are dicts ready to load; ``problems`` block loading."""
    pkg = Path(pkg_dir)
    ap = json.loads((pkg / "notes" / "note_anchors.json").read_text(encoding="utf-8"))
    problems, warnings = [], []
    if ap.get("format") != FORMAT:
        problems.append(f"note_anchors.json format is {ap.get('format')!r}, expected {FORMAT!r}")
    prefix = ap["anchors"][0]["id"].split("-")[0]
    man = json.loads((pkg / "manifest.json").read_text(encoding="utf-8")) if (pkg / "manifest.json").is_file() else {}
    core_file = (man.get("notes") or {}).get("core") or "notes/CH01_CORE_NOTES_EN_TE.txt"
    add_file = (man.get("notes") or {}).get("addendum") or "notes/CH01_NOTES_ADDENDUM_EN_TE.txt"
    core = parse_core((pkg / core_file).read_text(encoding="utf-8"), prefix)
    add = parse_addendum((pkg / add_file).read_text(encoding="utf-8"), prefix)
    by_id = {}
    for it in core + add:
        if it.anchor_id in by_id:
            problems.append(f"duplicate anchor {it.anchor_id}")
        by_id[it.anchor_id] = it
    # the parsed text must match the package's own anchor list exactly
    want_core = {a["id"]: a for a in ap["anchors"]}
    for aid, a in want_core.items():
        it = by_id.get(aid)
        if not it:
            problems.append(f"{aid}: in note_anchors.json but not found in the core notes text"); continue
        if it.package_section != a["section"]:
            problems.append(f"{aid}: section {it.package_section} in text, {a['section']} in note_anchors.json")
        if a["heading_en"].split(". ", 1)[-1].casefold() != it.heading_en.casefold():
            problems.append(f"{aid}: heading differs ({it.heading_en!r} vs {a['heading_en']!r})")
    for a in ap["addendum_anchors"]:
        it = by_id.get(a["id"])
        if not it:
            problems.append(f"{a['id']}: in note_anchors.json but not found in the addendum text"); continue
        if a.get("core_connections") is None:
            warnings.append(f"{a['id']}: note_anchors.json lists no core_connections; using the 'Core:' line in the addendum text {it.connections}")
        elif sorted(it.connections) != sorted(a["core_connections"]):
            problems.append(f"{a['id']}: core connections differ (text {it.connections}, json {a['core_connections']})")
        if not it.connections:
            problems.append(f"{a['id']}: no core connection found in the addendum text")
        if a["heading_en"].casefold() != it.heading_en.casefold():
            warnings.append(f"{a['id']}: anchor-list title {a['heading_en']!r} differs from the text heading {it.heading_en!r} (text heading used)")
    known = set(want_core) | {a["id"] for a in ap["addendum_anchors"]}
    for it in core + add:
        for c in it.connections:
            if c not in want_core:
                problems.append(f"{it.anchor_id}: connects to unknown core anchor {c}")
        if not (it.en or it.te):
            problems.append(f"{it.anchor_id}: no body text parsed")
        if it.kind in ("core", "addendum") and (not it.en or not it.te):
            problems.append(f"{it.anchor_id}: missing {'English' if not it.en else 'Telugu'} body")
        for s in it.sources:
            if s["url"] and not s["url"].startswith(("http://", "https://")):
                problems.append(f"{it.anchor_id}: unsafe source url")
    extra = [it.anchor_id for it in core + add if it.kind in ("core", "addendum") and it.anchor_id not in known]
    if extra:
        problems.append(f"anchors in the text but not in note_anchors.json: {extra}")
    rows = [it.as_dict(i) for i, it in enumerate(core + add, 1)]
    return rows, ap, problems, warnings


def load_notes(pkg_dir, apply=False, collection_id="ap-history-fresh-v1"):
    """Preview (default) or apply the package notes. Add-only; one transaction. Returns a report dict."""
    rows, ap, problems, warnings = parse_package_notes(pkg_dir)
    rep = {"chapter_slug": ap["chapter_slug"], "parsed": len(rows), "by_kind": {}, "problems": problems, "warnings": warnings, "to_add": 0, "added": 0,
           "unchanged": 0, "conflicts": [], "applied": bool(apply), "collection_id": collection_id}
    for r in rows:
        rep["by_kind"][r["kind"]] = rep["by_kind"].get(r["kind"], 0) + 1
    if problems:
        raise NotesError("package notes do not match their anchor list: " + "; ".join(problems[:5]))
    ch = SyllabusChapter.query.filter_by(slug=ap["chapter_slug"]).first()
    if ch is None:
        raise NotesError(f"canonical chapter {ap['chapter_slug']!r} is not seeded in this database (run the canonical seed first)")
    batch = _batch_id(pkg_dir)
    new = []
    for r in rows:
        have = ExpandedNote.query.filter_by(subject_id=ch.subject_id, anchor_id=r["anchor_id"]).first()
        if have is None:
            new.append(ExpandedNote(subject_id=ch.subject_id, syllabus_chapter_id=ch.id, package_batch_id=batch, collection_id=collection_id, **r))
        elif have.content_hash == r["content_hash"]:
            rep["unchanged"] += 1
            if have.collection_id != collection_id:      # never re-tagged silently: report it so a human decides
                rep["conflicts"].append({"anchor_id": r["anchor_id"], "reason": f"same content but collection_id is {have.collection_id!r}, not {collection_id!r}; left as is"})
        else:
            rep["conflicts"].append({"anchor_id": r["anchor_id"], "reason": "an anchor with this id exists with different content; left as is"})
    rep["to_add"] = len(new)
    if apply and new:
        try:
            db.session.add_all(new)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        rep["added"] = len(new)
    return rep


def _batch_id(pkg_dir):
    p = Path(pkg_dir) / "manifest.json"
    return json.loads(p.read_text(encoding="utf-8")).get("batch_id") if p.is_file() else None


# ── draft mapping to the existing app sections (never shown to learners until approved) ──
def propose_app_map(source_chapter_num=2, subject_slug="ap_history"):
    """Suggest (do not write) which existing app note sections relate to which package anchors, by shared distinctive words
    between the package heading and the app section heading. Returns a list for human review."""
    sub = Subject.query.filter_by(slug=subject_slug).first()
    ch = Chapter.query.filter_by(subject_id=sub.id, chapter_num=source_chapter_num).first() if sub else None
    if not ch:
        return []
    app = [(n.section_num, n.heading_en or "", n.heading_te or "") for n in Note.query.filter_by(chapter_id=ch.id).order_by(Note.section_num)]
    out = []
    for e in ExpandedNote.query.filter_by(subject_id=sub.id).filter(ExpandedNote.kind == "core").order_by(ExpandedNote.sort_order):
        w = {x for x in re.findall(r"[a-z]{5,}", e.heading_en.lower())}
        for num, h_en, _ in app:
            common = w & set(re.findall(r"[a-z]{5,}", h_en.lower()))
            if common:
                out.append({"anchor_id": e.anchor_id, "app_section_num": num, "app_heading": h_en, "shared_words": sorted(common)})
    return out


def apply_app_map(entries, source_chapter_num=2, status="draft", subject_slug="ap_history"):
    """Store reviewed mapping rows ({anchor_id, app_section_num, relation?, reason?}); add-only. The section must exist."""
    sub = Subject.query.filter_by(slug=subject_slug).first()
    ch = Chapter.query.filter_by(subject_id=sub.id, chapter_num=source_chapter_num).first()
    have_sections = {n for (n,) in db.session.query(Note.section_num).filter(Note.chapter_id == ch.id)}
    added = 0
    for e in entries:
        note = ExpandedNote.query.filter_by(subject_id=sub.id, anchor_id=e["anchor_id"]).first()
        if note is None or e["app_section_num"] not in have_sections:
            raise NotesError(f"mapping {e} refers to a missing anchor or app section")
        if ExpandedNoteAppMap.query.filter_by(expanded_note_id=note.id, source_chapter_num=source_chapter_num,
                                              app_section_num=e["app_section_num"]).first():
            continue
        db.session.add(ExpandedNoteAppMap(expanded_note_id=note.id, source_chapter_num=source_chapter_num,
                                          app_section_num=e["app_section_num"], relation=e.get("relation", "related"),
                                          status=status, reason=e.get("reason")))
        added += 1
    db.session.commit()
    return added
