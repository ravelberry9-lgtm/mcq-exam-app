"""Strict DRY-RUN validator for AP History MCQ batches (format ``ap-history-import-v1``).

This module never writes to a database and has no apply mode. It reads a batch (an import package, or a draft markdown file for
reporting only), checks it against the approved taxonomy ``ap-history-taxonomy-v1`` and the project rules, and returns a report.

Authorization: only a package that lives under ``content/AP_History_MCQ_Project/05_claude_import/`` and passes every check can ever be
called *importable*; anything read from ``02_drafts`` (or anywhere else) is reported as NOT IMPORTABLE whatever it contains.
"""
import hashlib
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path

from . import ap_canonical as canon
from . import ap_canonical_taxonomy as tax

FORMAT_VERSION = "ap-history-import-v1"
IMPORT_DIR_NAME = "05_claude_import"
DRAFT_DIR_NAME = "02_drafts"
SOURCES = ("codex_generated", "app_master", "hanumanthrao", "pyq_compiled", "verified_pyq")
DIFFICULTIES = ("easy", "medium", "tough", "toughest")
OPTION_KEYS = ("a", "b", "c", "d")
QID_RE = re.compile(r"^APH-U[1-5]-C(0[1-9]|[12][0-9]|3[01])-B\d{2}-Q\d{3,4}$")
DRAFT_QID_RE = re.compile(r"^C\d{2}-B\d{2}-\d{3,4}$")
# ids kept from the prepared (F-shape) packages by the converter: the content team's own import_ref
CONVERTED_QID_RE = re.compile(r"^aph-u[1-5]c(0[1-9]|[12][0-9]|3[01])-(AP9-\d{5}|B\d{3})$")
TELUGU = re.compile("[ఀ-౿]")
LATIN = re.compile("[A-Za-z]")
CODE_ONLY = re.compile(r"^[\sA-Da-d0-9,\-–.;()]+$")
REQUIRED = ("source", "source_qid", "batch_id", "source_file", "chapter_slug", "coverage_scope", "difficulty", "qtype", "question_te",
            "question_en", "options", "correct_answer", "explanation_te", "explanation_en", "review_status")
COVERAGE = ("direct", "supplementary_context")
REVIEW_STATUSES = ("raw", "structurally_valid", "content_review_required", "fact_verified", "bilingual_approved", "rejected")

# Content that must not be generated or imported until externally verified (see docs/ap_history_kataya_vema_audit.md).
BLOCKED_TERMS = ("Kataya Vema", "Kataya Vema Reddi", "కటయ వేమ", "కాటయ వేమ", "కటయవేమ", "కాటయవేమ")
KOMARAM_TERMS = ("Komaram Bheem", "కొమరం భీం", "కొమురం భీం")
KOMARAM_ALLOWED_CHAPTERS = ("supp-asaf-jahis-hyderabad-state", "u4-c26-folk-tribal-culture", "u3-c19-nationalist-movement-1885-1947")
RAMPA_TERMS = ("Rampa Rebellion", "రంపా")
RAMPA_CHAPTER = "u3-c19-nationalist-movement-1885-1947"


def _norm(text):
    return re.sub(r"\s+", " ", (text or "").strip()).lower()


def content_hash(rec):
    """md5 of the normalised stems and options (both languages); a collision is a warning, never a silent discard."""
    parts = [rec.get("question_en"), rec.get("question_te")]
    opts = rec.get("options") or {}
    for k in OPTION_KEYS:
        o = opts.get(k) or {}
        parts += [o.get("en"), o.get("te")]
    return hashlib.md5("␟".join(_norm(p) for p in parts).encode("utf-8")).hexdigest()


class Taxonomy:
    """Lookup of valid slugs from the approved taxonomy and chapter list."""

    def __init__(self):
        self.core = {slug: num for _u, num, slug, *_ in canon.CHAPTERS}
        self.supp = {s[0] for s in canon.SUPPLEMENTARY}
        self.chapter_of_sub, self.sub_of_micro, self.micro_scope = {}, {}, {}
        chap = {num: slug for _u, num, slug, *_ in canon.CHAPTERS}
        for num, subs in tax.build().items():
            for sb in subs:
                self.chapter_of_sub[sb["slug"]] = chap[num]
                for m in sb["micros"]:
                    self.sub_of_micro[m["slug"]] = sb["slug"]
                    self.micro_scope[m["slug"]] = m["scope"]

    @property
    def chapters(self):
        return set(self.core) | self.supp


class Report:
    def __init__(self, path, mode):
        self.path, self.mode = str(path), mode
        self.errors, self.warnings, self.records = [], [], 0
        self.info = {}

    def error(self, qid, code, msg):
        self.errors.append({"id": qid, "code": code, "message": msg})

    def warn(self, qid, code, msg):
        self.warnings.append({"id": qid, "code": code, "message": msg})

    @property
    def importable(self):
        return self.mode == "package" and not self.errors and self.records > 0

    def codes(self, kind="errors"):
        return Counter(e["code"] for e in getattr(self, kind))

    def to_dict(self):
        return {"path": self.path, "mode": self.mode, "records": self.records, "importable": self.importable, "errors": self.errors,
                "warnings": self.warnings, "info": self.info}


# ── record validation ────────────────────────────────────────────────
def validate_record(rec, rpt, taxo, draft=False):
    qid = rec.get("source_qid") or "(no id)"
    missing = [f for f in REQUIRED if rec.get(f) in (None, "", {})]
    for f in missing:
        rpt.error(qid, "missing_field", f"required field '{f}' is missing or empty")
    if rec.get("source") and rec["source"] not in SOURCES:
        rpt.error(qid, "bad_source", f"source {rec['source']!r} is not one of {SOURCES}")
    if rec.get("source_qid"):
        if CONVERTED_QID_RE.match(rec["source_qid"]) and rec.get("converted_from"):
            rpt.warn(qid, "converted_import_ref_id", "source_qid is the prepared package's import_ref (converted record), not APH-U#-C##-B##-Q###")
        elif not (QID_RE.match(rec["source_qid"]) or (draft and DRAFT_QID_RE.match(rec["source_qid"]))):
            rpt.error(qid, "bad_id_format", "source_qid must match APH-U{unit}-C{chapter}-B{batch}-Q{number}")
        elif DRAFT_QID_RE.match(rec["source_qid"]):
            rpt.warn(qid, "draft_id_format", "short draft id; must be normalised to APH-U#-C##-B##-Q### after approval, before any import")
    if rec.get("difficulty") and str(rec["difficulty"]).lower() not in DIFFICULTIES:
        rpt.error(qid, "bad_difficulty", f"difficulty {rec['difficulty']!r} not in {DIFFICULTIES}")
    if rec.get("coverage_scope") and rec["coverage_scope"] not in COVERAGE:
        rpt.error(qid, "bad_coverage_scope", f"question coverage_scope must be one of {COVERAGE}")
    if rec.get("review_status") and rec["review_status"] not in REVIEW_STATUSES:
        rpt.error(qid, "bad_review_status", f"review_status {rec['review_status']!r} unknown")
    elif rec.get("review_status") and rec["review_status"] != "bilingual_approved":
        rpt.error(qid, "not_approved", f"review_status is {rec['review_status']!r}; only bilingual_approved may be imported")
    # language completeness
    for f in ("question_te", "explanation_te"):
        v = rec.get(f)
        if v and not TELUGU.search(v):
            rpt.error(qid, "telugu_missing", f"{f} contains no Telugu text")
    for f in ("question_en", "explanation_en"):
        v = rec.get(f)
        if v and not LATIN.search(v):
            rpt.error(qid, "english_missing", f"{f} contains no English text")
    # options and answer
    opts = rec.get("options")
    if isinstance(opts, dict) and opts:
        if sorted(opts) != list(OPTION_KEYS):
            rpt.error(qid, "bad_options", f"options must be exactly a, b, c, d (got {sorted(opts)})")
        texts = []
        for k in OPTION_KEYS:
            o = opts.get(k)
            if not isinstance(o, dict) or not (o.get("te") or "").strip() or not (o.get("en") or "").strip():
                rpt.error(qid, "option_incomplete", f"option {k} needs non-empty te and en")
                continue
            if o["te"].strip() == o["en"].strip() and not CODE_ONLY.match(o["en"]):
                rpt.error(qid, "option_not_bilingual", f"option {k} has identical te and en text that is not a language-neutral code")
            elif not TELUGU.search(o["te"]) and not CODE_ONLY.match(o["te"]):
                rpt.error(qid, "option_telugu_missing", f"option {k} te has no Telugu text")
            texts.append(_norm(o.get("en")))
        if len(set(texts)) < len(texts):
            rpt.error(qid, "duplicate_options", "two options have the same English text")
    elif opts not in (None, "", {}):
        rpt.error(qid, "bad_options", "options must be an object")
    ans = (rec.get("correct_answer") or "").lower()
    if rec.get("correct_answer") and ans not in OPTION_KEYS:
        rpt.error(qid, "bad_answer", "correct_answer must be one of a, b, c, d")
    # taxonomy
    ch, st = rec.get("chapter_slug"), rec.get("subtopic_slug")
    if ch and ch not in taxo.chapters:
        rpt.error(qid, "unknown_chapter", f"chapter_slug {ch!r} is not in the canonical chapters")
    if ch in taxo.supp:
        if st:
            rpt.error(qid, "subtopic_on_supplementary", "supplementary chapters have no subtopics; leave subtopic_slug empty")
        if rec.get("coverage_scope") == "direct":
            rpt.warn(qid, "supplementary_marked_direct", "primary chapter is supplementary; it never counts as direct syllabus coverage")
    elif ch in taxo.core:
        if not st and rec.get("subtopic_fallback"):
            rpt.warn(qid, "chapter_level_fallback", "no subtopic: integrated question kept at chapter level (subtopic_fallback)")
        elif not st:
            rpt.error(qid, "missing_subtopic", "a core-chapter question needs one primary subtopic_slug")
        elif st not in taxo.chapter_of_sub:
            rpt.error(qid, "unknown_subtopic", f"subtopic_slug {st!r} is not in ap-history-taxonomy-v1")
        elif taxo.chapter_of_sub[st] != ch:
            rpt.error(qid, "subtopic_chapter_mismatch", f"subtopic {st!r} belongs to {taxo.chapter_of_sub[st]!r}, not {ch!r}")
    micros = rec.get("microtopic_slugs") or []
    if not isinstance(micros, list):
        rpt.error(qid, "bad_microtopics", "microtopic_slugs must be a list")
        micros = []
    for m in micros:
        if m not in taxo.sub_of_micro:
            rpt.error(qid, "unknown_microtopic", f"microtopic {m!r} is not in ap-history-taxonomy-v1")
        elif st and taxo.sub_of_micro[m] != st:
            rpt.error(qid, "microtopic_subtopic_mismatch", f"microtopic {m!r} is not under the primary subtopic {st!r}; list it in secondary_microtopics")
        if taxo.micro_scope.get(m) == "supplementary_context" and rec.get("coverage_scope") == "direct":
            rpt.error(qid, "scope_mismatch", f"microtopic {m!r} is supplementary_context but coverage_scope is direct")
    for m in rec.get("secondary_microtopics") or []:
        if m not in taxo.sub_of_micro:
            rpt.error(qid, "unknown_microtopic", f"secondary microtopic {m!r} is not in ap-history-taxonomy-v1")
    for c in rec.get("secondary_chapters") or []:
        if c not in taxo.chapters:
            rpt.error(qid, "unknown_chapter", f"secondary chapter {c!r} is not in the canonical chapters")
        if c == ch:
            rpt.error(qid, "secondary_equals_primary", "a secondary chapter must differ from the primary chapter")
    # content rules
    blob = " ".join(str(rec.get(f) or "") for f in ("question_en", "question_te", "explanation_en", "explanation_te")
                    ) + " " + " ".join(f"{(o or {}).get('en', '')} {(o or {}).get('te', '')}" for o in (opts or {}).values() if isinstance(o, dict))
    if any(t in blob for t in BLOCKED_TERMS):
        rpt.error(qid, "content_blocked", "mentions Kataya Vema: blocked_until_verified (see ap_history_kataya_vema_audit.md); no questions from that material")
    if any(t in blob for t in KOMARAM_TERMS) and ch not in KOMARAM_ALLOWED_CHAPTERS:
        rpt.error(qid, "komaram_bheem_mapping", "Komaram Bheem questions must be mapped individually: supplementary Asaf Jahi primary, Chapter 26 for Gond culture, "
                  "Chapter 19 only for Hyderabad freedom leaders; never an Andhra-Movement chapter")
    elif any(t in blob for t in KOMARAM_TERMS) and ch == "u4-c26-folk-tribal-culture" and "supp-asaf-jahis-hyderabad-state" not in (rec.get("secondary_chapters") or []):
        rpt.warn(qid, "komaram_bheem_context", "Chapter 26 primary: add the Asaf Jahi supplementary chapter as secondary context where the question concerns the movement")
    if any(t in blob for t in RAMPA_TERMS) and ch != RAMPA_CHAPTER:
        rpt.warn(qid, "rampa_mapping", "Rampa Rebellion is primary Chapter 19 (secondary Chapter 26, microtopic rampa-rebellion)")
    for bad, good in tax.TERM_REPLACEMENTS:
        if bad in blob:
            rpt.warn(qid, "non_normalized_term", f"{bad!r} found; the approved learner-facing form is {good!r}")


def _db_state(db_path):
    if not db_path:
        return None
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        have = {c[1] for c in con.execute("PRAGMA table_info(questions)")}
        if "source_qid" not in have:
            return {"pairs": set(), "hashes": {}, "note": "database has no provenance columns yet"}
        pairs = {(r[0], r[1]) for r in con.execute("SELECT source, source_qid FROM questions WHERE source_qid IS NOT NULL")}
        hashes = {}
        for h, s, q in con.execute("SELECT content_hash, source, source_qid FROM questions WHERE content_hash IS NOT NULL"):
            hashes.setdefault(h, []).append(f"{s}:{q}")
        return {"pairs": pairs, "hashes": hashes, "note": ""}
    finally:
        con.close()


def validate_records(records, rpt, draft=False, db_path=None):
    taxo = Taxonomy()
    state = _db_state(db_path)
    seen, hashes = {}, {}
    for rec in records:
        rpt.records += 1
        validate_record(rec, rpt, taxo, draft=draft)
        qid = rec.get("source_qid") or "(no id)"
        if qid in seen:
            rpt.error(qid, "duplicate_source_qid", "source_qid appears more than once in this batch")
        seen[qid] = True
        h = content_hash(rec)
        if h in hashes:
            rpt.warn(qid, "content_hash_collision", f"same normalised content as {hashes[h]} in this batch (kept, not discarded; review for duplicates)")
        hashes.setdefault(h, qid)
        if state is not None:
            if (rec.get("source"), rec.get("source_qid")) in state["pairs"]:
                rpt.error(qid, "already_imported", "(source, source_qid) already exists in the database")
            if h in state["hashes"]:
                rpt.warn(qid, "content_hash_collision_db", f"same normalised content as database rows {state['hashes'][h][:3]} (warning, not a discard)")
    if state is not None and state["note"]:
        rpt.info["database"] = state["note"]
    dist = Counter((r.get("correct_answer") or "").upper() for r in records)
    rpt.info["answer_distribution"] = {k: dist.get(k, 0) for k in "ABCD"}
    rpt.info["difficulty"] = dict(Counter(str(r.get("difficulty")).lower() for r in records))
    rpt.info["qtype"] = dict(Counter(r.get("qtype") for r in records))
    rpt.info["subtopics"] = dict(Counter(r.get("subtopic_slug") or r.get("chapter_slug") for r in records))
    return rpt


# ── package (authorized format) ──────────────────────────────────────
def _under(path, dirname):
    return dirname in Path(path).resolve().parts


def validate_package(pkg_dir, db_path=None):
    pkg = Path(pkg_dir)
    rpt = Report(pkg, "package")
    if not _under(pkg, IMPORT_DIR_NAME):
        rpt.mode = "not_authorized"
        rpt.error("(package)", "outside_import_dir", f"only packages under {IMPORT_DIR_NAME}/ can be imported; this path is not")
    if _under(pkg, DRAFT_DIR_NAME):
        rpt.mode = "not_authorized"
        rpt.error("(package)", "draft_folder", f"{DRAFT_DIR_NAME}/ is never imported")
    mpath, qpath = pkg / "manifest.json", pkg / "questions.jsonl"
    if not mpath.is_file() or not qpath.is_file():
        rpt.error("(package)", "missing_file", "a package needs manifest.json and questions.jsonl")
        return rpt
    try:
        manifest = json.loads(mpath.read_text(encoding="utf-8"))
    except ValueError as e:
        rpt.error("(manifest)", "bad_manifest", f"manifest.json is not valid JSON: {e}")
        return rpt
    for f in ("format_version", "taxonomy_version", "batch_id", "source", "question_count", "questions_sha256", "content_approval"):
        if manifest.get(f) in (None, ""):
            rpt.error("(manifest)", "manifest_field", f"manifest field '{f}' is missing")
    if manifest.get("format_version") not in (None, FORMAT_VERSION):
        rpt.error("(manifest)", "format_version", f"format_version must be {FORMAT_VERSION}")
    if manifest.get("taxonomy_version") not in (None, tax.TAXONOMY_VERSION):
        rpt.error("(manifest)", "taxonomy_version", f"taxonomy_version must be {tax.TAXONOMY_VERSION}")
    if manifest.get("content_approval") not in (None, "bilingual_approved"):
        rpt.error("(manifest)", "content_approval", "manifest content_approval must be bilingual_approved")
    raw = qpath.read_bytes()
    if manifest.get("questions_sha256") and hashlib.sha256(raw).hexdigest() != manifest["questions_sha256"]:
        rpt.error("(manifest)", "checksum", "questions.jsonl does not match manifest questions_sha256 (file changed after approval)")
    records = []
    for i, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except ValueError:
            rpt.error(f"line {i}", "bad_json", "line is not valid JSON")
    if manifest.get("question_count") not in (None, len(records)):
        rpt.error("(manifest)", "question_count", f"manifest says {manifest.get('question_count')} questions, file has {len(records)}")
    for r in records:
        if manifest.get("batch_id") and r.get("batch_id") != manifest["batch_id"]:
            rpt.error(r.get("source_qid") or "(no id)", "batch_mismatch", "record batch_id differs from manifest batch_id")
        if manifest.get("source") and r.get("source") != manifest["source"]:
            rpt.error(r.get("source_qid") or "(no id)", "source_mismatch", "record source differs from manifest source")
    validate_records(records, rpt, db_path=db_path)
    rpt.info["manifest"] = {k: manifest.get(k) for k in ("batch_id", "source", "question_count", "taxonomy_version")}
    return rpt


# ── draft markdown (report only; never importable) ───────────────────
HEAD = re.compile(r"^### (C\d{2}-B\d{2}-\d{3,4}) · ([^·]+) · (.+?)\s*$")
OPT = re.compile(r"^([A-D])\.\s+(.*?)\s*$")


def _split_option(text):
    parts = text.split(" / ")
    if len(parts) == 1:
        return {"te": text, "en": text}
    for i in range(len(parts) - 1, 0, -1):
        left, right = " / ".join(parts[:i]), " / ".join(parts[i:])
        if not TELUGU.search(right):
            return {"te": left.strip(), "en": right.strip()}
    return {"te": parts[0].strip(), "en": " / ".join(parts[1:]).strip()}


def parse_draft_markdown(path):
    """Parse a Codex draft batch (markdown) into records. Fields the draft does not carry stay absent."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    status = next((re.sub(r"\*+", "", ln).split(":", 1)[1].strip() for ln in lines if ln.startswith("**Status:**")), "")
    source = next((re.sub(r"[*`]", "", ln).split(":", 1)[1].strip() for ln in lines if ln.startswith("**Source:**")), "")
    recs, i = [], 0
    while i < len(lines):
        m = HEAD.match(lines[i])
        if not m:
            i += 1
            continue
        qid, diff, qtype = m.group(1), m.group(2).strip(), m.group(3).strip()
        j, block = i + 1, []
        while j < len(lines) and not HEAD.match(lines[j]) and not lines[j].startswith("---") and not lines[j].startswith("## "):
            block.append(lines[j]); j += 1
        i = j
        text = "\n".join(block)
        rec = {"source": source or None, "source_qid": qid, "source_file": Path(path).name, "difficulty_label": diff, "qtype": qtype, "options": {}}
        te = re.search(r"\*\*TE:\*\*\s*(.*?)\n\*\*EN:\*\*", text, re.S)
        en = re.search(r"\*\*EN:\*\*\s*(.*?)\n\s*\n(?=[A-D]\. )", text, re.S)
        rec["question_te"] = re.sub(r" {2,}\n", "\n", te.group(1)).strip() if te else None
        rec["question_en"] = re.sub(r" {2,}\n", "\n", en.group(1)).strip() if en else None
        for grp in text.split("\n\n"):
            g = grp.strip("\n").splitlines()
            if len(g) >= 4 and g[0].startswith("A. ") and all(OPT.match(x) for x in g[:4]):
                for ln in g[:4]:
                    om = OPT.match(ln)
                    rec["options"][om.group(1).lower()] = _split_option(om.group(2))
                break
        a_ = re.search(r"\*\*Answer:\s*([A-D])\*\*", text)
        rec["correct_answer"] = a_.group(1).lower() if a_ else None
        xt = re.search(r"\*\*TE వివరణ:\*\*\s*(.*?)\n\*\*EN Explanation:\*\*", text, re.S)
        xe = re.search(r"\*\*EN Explanation:\*\*\s*(.*)$", text, re.S)
        rec["explanation_te"] = xt.group(1).strip() if xt else None
        rec["explanation_en"] = xe.group(1).strip() if xe else None
        recs.append(rec)
    return recs, status


# Fields and checks that a draft cannot satisfy by definition; reported once as "gaps to close before packaging".
DRAFT_EXPECTED_MISSING = {"batch_id", "coverage_scope", "review_status", "subtopic_slug", "chapter_slug", "difficulty"}
DRAFT_LABELS = {"easy": "easy", "medium": "medium", "tough": "tough", "toughest": "toughest"}


def validate_draft_files(paths):
    """Report-only validation of draft markdown files. The result is never importable."""
    rpt = Report(", ".join(str(p) for p in paths), "draft_report")
    rpt.error("(draft)", "draft_not_importable", "draft files are never imported; this report checks structure and mapping readiness only")
    records, statuses = [], set()
    for p in paths:
        recs, status = parse_draft_markdown(p)
        statuses.add(status)
        records += recs
    taxo = Taxonomy()
    sub = Report(rpt.path, "draft_report")
    for r in records:
        probe = dict(r)
        num = int(re.match(r"C(\d{2})-", r["source_qid"]).group(1))
        probe["chapter_slug"] = next((slug for _u, n, slug, *_ in canon.CHAPTERS if n == num), None)
        probe["difficulty"] = DRAFT_LABELS.get(r["difficulty_label"].lower(), r["difficulty_label"])
        probe.update(batch_id="draft", coverage_scope="direct", review_status="bilingual_approved")   # neutralise fields a draft cannot have
        probe["subtopic_slug"] = next((sb["slug"] for sb in tax_first_sub(num)), None)
        validate_record(probe, sub, taxo, draft=True)
    ids = [r["source_qid"] for r in records]
    for qid in sorted({i for i in ids if ids.count(i) > 1}):
        rpt.error(qid, "duplicate_source_qid", "id appears more than once across the draft files")
    rpt.records = len(records)
    rpt.errors += sub.errors
    rpt.warnings += sub.warnings
    dist = Counter((r.get("correct_answer") or "").upper() for r in records)
    rpt.info["answer_distribution"] = {k: dist.get(k, 0) for k in "ABCD"}
    rpt.info["difficulty_labels"] = dict(Counter(r["difficulty_label"] for r in records))
    rpt.info["qtype"] = dict(Counter(r["qtype"] for r in records))
    rpt.info["draft_status_lines"] = sorted(statuses)
    rpt.info["parsed"] = {
        "questions": len(records),
        "with_te_and_en_stem": sum(1 for r in records if r["question_te"] and r["question_en"]),
        "with_four_options": sum(1 for r in records if len(r["options"]) == 4),
        "with_answer": sum(1 for r in records if r["correct_answer"]),
        "with_both_explanations": sum(1 for r in records if r["explanation_te"] and r["explanation_en"])}
    hashes, dups = {}, []
    for r in records:
        h = content_hash(r)
        if h in hashes:
            dups.append((r["source_qid"], hashes[h]))
        hashes.setdefault(h, r["source_qid"])
    rpt.info["content_hash_collisions"] = dups
    rpt.info["fields_absent_from_every_draft"] = sorted(
        ["subtopic_slug", "microtopic_slugs", "coverage_scope", "review_status", "batch_id", "chapter_slug (derivable from the id prefix)",
         "normalised source_qid (APH-U#-C##-B##-Q###)", "numeric difficulty label (draft uses Easy/Medium/Tough/Toughest)"])
    return rpt, records


def tax_first_sub(num):
    """Placeholder subtopic so the structural checks can run on a draft (a draft carries no subtopic)."""
    return tax.build().get(num, [])[:1]
