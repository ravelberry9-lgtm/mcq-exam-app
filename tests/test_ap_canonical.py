"""Phase 1 of the AP History canonical structure: schema, seed data, stable slugs, bilingual titles, the draft note
mapping, and proof that nothing existing is changed."""
import importlib.util
import re
import sys
from pathlib import Path

import pytest
from sqlalchemy.exc import IntegrityError

from app.db import db
from app.models import (
    CHAPTER_CLASSIFICATIONS, LEARNER_VISIBLE_STATUS, QUESTION_SOURCES, REVIEW_STATUSES, SUPPLEMENTARY_TYPES,
    Chapter, Note, Question, Subject, SyllabusChapter, SyllabusSubtopic, SyllabusUnit,
)
from app.services import ap_canonical as canon
from app.services import ap_canonical_subtopics as subs

ROOT = Path(__file__).resolve().parent.parent
TELUGU = re.compile(r"[ఀ-౿]")
SLUG = re.compile(r"^u([1-5])-c(\d\d)-[a-z0-9]+(?:-[a-z0-9]+)*$")


@pytest.fixture()
def hist(app):
    s = Subject(slug="ap_history", name_en="AP History", name_te="ఆంధ్రప్రదేశ్ చరిత్ర")
    db.session.add(s); db.session.commit()
    return s


@pytest.fixture()
def seeded(hist):
    canon.seed()
    return hist


# ── seed data ────────────────────────────────────────────────────────
def test_structure_is_five_units_31_core_chapters_and_three_supplementary():
    assert [u[0] for u in canon.UNITS] == [1, 2, 3, 4, 5]
    assert [c[1] for c in canon.CHAPTERS] == list(range(1, 32))
    assert len(canon.SUPPLEMENTARY) == 3
    ranges = {1: range(1, 9), 2: range(9, 15), 3: range(15, 23), 4: range(23, 28), 5: range(28, 32)}
    for unit, num, *_ in canon.CHAPTERS:
        assert num in ranges[unit], (unit, num)


def test_seed_creates_expected_rows_and_is_idempotent(hist):
    r = canon.seed()
    assert (r["units_added"], r["chapters_added"], r["supplementary_added"]) == (5, 31, 3)
    assert (SyllabusUnit.query.count(), SyllabusChapter.query.count()) == (5, 34)
    again = canon.seed()
    assert (again["units_added"], again["chapters_added"], again["supplementary_added"]) == (0, 0, 0)
    assert SyllabusChapter.query.count() == 34


def test_preview_writes_nothing_and_missing_subject_is_refused(hist):
    r = canon.seed(apply=False)
    assert r["chapters_added"] == 31 and SyllabusChapter.query.count() == 0
    with pytest.raises(LookupError):
        canon.seed(subject_slug="no_such_subject")


def test_classifications(seeded):
    cls = {c.chapter_num: c.classification for c in SyllabusChapter.query.filter(SyllabusChapter.chapter_num.isnot(None))}
    assert {1, 3, 6} == {n for n, c in cls.items() if c == "bridge"}
    assert [n for n, c in cls.items() if c == "thematic"] == [14]
    assert set(cls.values()) <= set(CHAPTER_CLASSIFICATIONS) - {"supplementary"}


def test_supplementary_chapters_are_not_core(seeded):
    supp = {c.slug: c for c in SyllabusChapter.query.filter_by(classification="supplementary")}
    assert {c.supplementary_type for c in supp.values()} == set(SUPPLEMENTARY_TYPES)
    assert all(not c.is_core and c.unit_id is None and c.chapter_num is None for c in supp.values())
    assert supp["supp-dynasties-overview"].supplementary_type == "supplementary_cross_cutting"
    assert supp["supp-asaf-jahis-hyderabad-state"].supplementary_type == "supplementary_outside_direct_syllabus"
    assert supp["supp-post-2014-andhra-pradesh"].supplementary_type == "supplementary_post_syllabus"
    assert SyllabusChapter.query.filter(SyllabusChapter.classification != "supplementary").count() == 31


def test_database_refuses_inconsistent_core_vs_supplementary_rows(seeded):
    unit = SyllabusUnit.query.first()
    bad = [  # a supplementary chapter inside a unit; a core chapter with no unit/number; an unknown classification
        dict(classification="supplementary", supplementary_type="supplementary_post_syllabus", unit_id=unit.id),
        dict(classification="direct", unit_id=None, chapter_num=None),
        dict(classification="elective", unit_id=unit.id, chapter_num=99),
    ]
    for i, kw in enumerate(bad):
        db.session.add(SyllabusChapter(subject_id=seeded.id, slug=f"bad-{i}", title_en="x", title_te="x", **kw))
        with pytest.raises(IntegrityError):
            db.session.commit()
        db.session.rollback()


def test_titles_are_bilingual(seeded):
    for u in SyllabusUnit.query:
        assert u.title_en.isascii() and TELUGU.search(u.title_te) and u.title_en.strip() and u.title_te.strip()
    for c in SyllabusChapter.query:
        assert c.title_en.strip() and not TELUGU.search(c.title_en), c.slug
        assert TELUGU.search(c.title_te), c.slug


# ── stable slugs ─────────────────────────────────────────────────────
def test_slugs_follow_the_scheme_and_are_unique():
    slugs = [c[2] for c in canon.CHAPTERS]
    assert len(set(slugs)) == 31
    for unit, num, slug, *_ in canon.CHAPTERS:
        m = SLUG.match(slug)
        assert m and int(m.group(1)) == unit and int(m.group(2)) == num, slug
    assert "u1-c04-satavahanas" in slugs
    assert len({u[1] for u in canon.UNITS} | set(slugs) | {s[0] for s in canon.SUPPLEMENTARY}) == 39


def test_editing_a_title_never_changes_a_slug_and_reseed_does_not_overwrite(seeded):
    ch = SyllabusChapter.query.filter_by(slug="u1-c04-satavahanas").one()
    ch.title_en = "The Satavahana Dynasty"; db.session.commit()
    canon.seed()
    ch = SyllabusChapter.query.filter_by(slug="u1-c04-satavahanas").one()
    assert (ch.slug, ch.title_en) == ("u1-c04-satavahanas", "The Satavahana Dynasty")


# ── draft subtopics (taxonomy only; not seeded in phase 1) ───────────
def test_draft_subtopics_are_bilingual_unique_and_prefixed_by_their_chapter():
    exp = subs.expanded()
    assert set(exp) == {c[2] for c in canon.CHAPTERS}
    allslugs = [s for lst in exp.values() for s, _en, _te in lst]
    assert len(allslugs) == len(set(allslugs)) >= 300
    for ch_slug, lst in exp.items():
        assert lst, ch_slug
        prefix = "-".join(ch_slug.split("-")[:2])
        for s, en, te in lst:
            assert s.startswith(prefix + "-") and SLUG.match(s), s
            assert en.strip() and TELUGU.search(te) and not TELUGU.search(en), s
    for approved in ("u1-c04-origin-homeland", "u1-c04-administration", "u1-c04-economy-trade", "u1-c04-religion",
                     "u1-c04-literature", "u1-c04-art-architecture"):
        assert approved in allslugs


def test_subtopic_seeding_works_when_asked_but_is_not_part_of_seed(seeded):
    assert SyllabusSubtopic.query.count() == 0
    n = canon.seed_subtopics(subs.expanded())
    assert n == SyllabusSubtopic.query.count() >= 300
    assert canon.seed_subtopics(subs.expanded()) == 0


# ── draft note mapping ───────────────────────────────────────────────
@pytest.fixture(scope="module")
def mapping_mod():
    sys.path.insert(0, str(ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location("build_map", ROOT / "scripts" / "build_ap_note_mapping_draft.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def test_note_mapping_covers_every_note_section_exactly_once(mapping_mod):
    rows = mapping_mod.load_notes()
    mapped = mapping_mod.build(rows)
    assert len(rows) == len(mapped) == 225
    assert len({(m["old_chapter_num"], m["section_num"]) for m in mapped}) == 225
    valid_ch = {c[2] for c in canon.CHAPTERS} | {s[0] for s in canon.SUPPLEMENTARY}
    for m in mapped:
        assert m["canonical_chapter_slug"] in valid_ch
        assert m["confidence"] in ("high", "medium", "low")
        assert m["mapping_kind"] in ("direct", "bridge", "cross_cutting", "supplementary")
        assert (m["mapping_kind"] == "cross_cutting") == (m["canonical_chapter_slug"] == "supp-dynasties-overview")
        if m["proposed_subtopic_slug"]:
            assert m["proposed_subtopic_slug"].startswith("-".join(m["canonical_chapter_slug"].split("-")[:2]))
        assert m["reason"].strip()
    # supplementary Asaf Jahi / post-2014 chapters have no notes in the app database, so nothing maps to them
    assert not any("asaf" in m["canonical_chapter_slug"] or "post-2014" in m["canonical_chapter_slug"] for m in mapped)
    assert {m["old_chapter_num"] for m in mapped if m["canonical_chapter_slug"] == "supp-dynasties-overview"} == {4}


@pytest.fixture(scope="module")
def full_map(mapping_mod):
    return mapping_mod.build()


def _row(full_map, ch, sec):
    return next(m for m in full_map if m["old_chapter_num"] == ch and m["section_num"] == sec)


def test_full_mapping_includes_html_chapters_13_to_19_once_each(full_map):
    assert len(full_map) == 338
    assert len({(m["old_chapter_num"], m["section_num"]) for m in full_map}) == 338
    assert sum(1 for m in full_map if m["old_chapter_num"] >= 13) == 113
    assert all(m["note_id"] == "" and m["old_chapter_id"] == "" for m in full_map if m["old_chapter_num"] >= 13)


def test_chapters_13_to_19_follow_the_approved_targets(full_map):
    def chs(n):
        return {m["canonical_chapter_slug"] for m in full_map if m["old_chapter_num"] == n}
    assert chs(14) == {"supp-asaf-jahis-hyderabad-state"}
    assert chs(19) == {"supp-post-2014-andhra-pradesh"}
    assert chs(18) == {"u5-c31-social-cultural-events-1956-2014"}
    assert all(s.startswith("u2-c13") for s in chs(13))
    assert {s.split("-")[1] for s in chs(15)} <= {"c15", "c16", "c17", "c18"}
    assert {s.split("-")[1] for s in chs(16)} <= {f"c{n}" for n in range(17, 28)}  # content-driven: source 16 also covers 1920s-1953 sections
    assert {s.split("-")[1] for s in chs(17)} <= {f"c{n}" for n in range(23, 31)}
    kinds = {m["mapping_kind"] for m in full_map if m["old_chapter_num"] in (14, 19)}
    assert kinds == {"supplementary"}


def test_multi_topic_sections_are_flagged_not_split(full_map):
    assert sum(1 for m in full_map if m["multi_topic"] == "yes") > 0
    for m in full_map:
        assert (m["multi_topic"] == "yes") == ("multi_topic" in m["flags"].split(";"))
    # one row per source section: nothing was split
    assert len(full_map) == len({(m["old_chapter_num"], m["section_num"]) for m in full_map})


def test_pedavegi_row_has_salankayana_primary_and_a_justified_secondary(full_map):
    r = _row(full_map, 7, 10)
    assert r["proposed_subtopic_slug"] == "u1-c06-salankayanas"
    assert r["secondary_mappings"] == "u1-c08-vengi-foundation"
    assert "10.2" in r["reason"]


def test_kataya_vema_row_is_flagged_and_unapproved(full_map):
    r = _row(full_map, 11, 12)
    assert r["approval_status"] == "unapproved" and "attribution_check" in r["flags"].split(";") and r["needs_review"] == "yes"
    assert "UNAPPROVED" in r["reason"]
    assert sum(1 for m in full_map if m["approval_status"] == "unapproved") == 1


def test_low_confidence_rows_stay_flagged_and_out_of_folk_tribal_culture(full_map):
    for key in ((1, 5), (2, 13)):
        r = _row(full_map, *key)
        assert r["confidence"] == "low" and "content_review" in r["flags"].split(";")
        assert not r["canonical_chapter_slug"].startswith("u4-c26")
        assert not any("c26" in x for x in r["secondary_mappings"].split("; "))


def test_architecture_section_goes_to_the_general_subtopic_not_pancharamas(full_map):
    r = _row(full_map, 9, 16)
    assert r["proposed_subtopic_slug"] == "u1-c08-art-architecture"
    assert "pancharamas" not in r["proposed_subtopic_slug"]


def test_shared_name_alone_never_creates_a_secondary_link(full_map):
    # every secondary named in the mapping exists in the draft taxonomy and differs from the primary
    titles = {s for lst in subs.expanded().values() for s, _e, _t in lst}
    chapter_slugs = {c[2] for c in canon.CHAPTERS} | {x[0] for x in canon.SUPPLEMENTARY}
    for m in full_map:
        for sec in (x for x in m["secondary_mappings"].split("; ") if x):
            assert sec in titles or sec in chapter_slugs
            assert sec != m["proposed_subtopic_slug"]


def test_taxonomy_review_file_covers_every_draft_subtopic_and_matches_generator(tmp_path):
    spec = importlib.util.spec_from_file_location("build_tax", ROOT / "scripts" / "build_ap_taxonomy_review.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    rows = mod.build()
    assert [r["subtopic_slug"] for r in rows] == [s for lst in subs.expanded().values() for s, _e, _t in lst]
    assert all(r["subtopic_en"].strip() and r["subtopic_te"].strip() for r in rows)
    assert any(r["unit"] == 1 for r in rows) and {r["unit"] for r in rows} == {1, 2, 3, 4, 5}
    mod.write(rows, out_dir=tmp_path)
    for name in ("ap_history_subtopic_taxonomy_review.csv", "ap_history_subtopic_taxonomy_review.md"):
        assert (tmp_path / name).read_bytes() == (ROOT / "docs" / name).read_bytes(), f"re-run scripts/build_ap_taxonomy_review.py ({name})"


def test_taxonomy_stays_a_draft_and_is_not_seeded_by_the_seeder(seeded):
    assert SyllabusSubtopic.query.count() == 0


def test_checked_in_review_files_match_the_generator(mapping_mod, tmp_path):
    mapping_mod.write(mapping_mod.build(), out_dir=tmp_path)
    for name in ("ap_history_note_mapping_draft.csv", "ap_history_note_mapping_draft.md"):
        assert (tmp_path / name).read_bytes() == (ROOT / "docs" / name).read_bytes(), f"re-run scripts/build_ap_note_mapping_draft.py ({name})"


# ── provenance columns and non-destructive compatibility ─────────────
def _q(subject, **kw):
    base = dict(subject_id=subject.id, source_type="practice", correct_answer="a", question_en="Q?", options_en={"a": "x", "b": "y"})
    base.update(kw)
    return Question(**base)


def test_vocabularies_match_the_approved_workflow():
    assert QUESTION_SOURCES == ("codex_generated", "app_master", "hanumanthrao", "pyq_compiled", "verified_pyq", "legacy_db")
    assert REVIEW_STATUSES == ("raw", "structurally_valid", "content_review_required", "fact_verified", "bilingual_approved", "rejected")
    assert LEARNER_VISIBLE_STATUS == "bilingual_approved"


def test_existing_style_rows_keep_null_provenance_and_report_legacy_db(hist):
    q = _q(hist); db.session.add(q); db.session.commit()
    q = db.session.get(Question, q.id)
    assert (q.source, q.source_qid, q.review_status, q.syllabus_chapter_id, q.subtopic_id, q.content_hash) == (None,) * 6
    assert q.effective_source == "legacy_db"


def test_source_and_source_qid_are_unique_but_null_rows_may_repeat(seeded):
    ch = SyllabusChapter.query.filter_by(slug="u1-c04-satavahanas").one()
    db.session.add_all([_q(seeded), _q(seeded)]); db.session.commit()            # many legacy (NULL) rows are fine
    db.session.add(_q(seeded, source="codex_generated", source_qid="AP-U1-C04-0001", syllabus_chapter_id=ch.id, review_status="raw"))
    db.session.add(_q(seeded, source="app_master", source_qid="AP-U1-C04-0001"))   # same id in another collection is fine
    db.session.commit()
    db.session.add(_q(seeded, source="codex_generated", source_qid="AP-U1-C04-0001"))
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()


def test_seeding_changes_no_existing_content_and_learn_pages_are_identical(hist, client):
    ch = Chapter(subject_id=hist.id, chapter_num=5, title_en="Satavahana Dynasty", title_te="శాతవాహనులు")
    db.session.add(ch); db.session.flush()
    db.session.add(Note(chapter_id=ch.id, section_num=1, heading_en="Intro", heading_te="పరిచయం", body_en="<p>x</p>", body_te="<p>x</p>"))
    db.session.add(_q(hist, question_te="ప్ర?", options_te={"a": "అ", "b": "ఆ"}, pyq_year="2018", source_type="pyq"))
    db.session.commit()
    urls = ["/learn/", "/learn/subject/ap_history", f"/learn/topic/{ch.id}", f"/learn/topic/{ch.id}/notes", f"/learn/topic/{ch.id}/practice"]

    def snap():
        csrf = re.compile(rb'(name="csrf-token" content=")[^"]*|(name="csrf_token" value=")[^"]*')
        return {u: (client.get(u).status_code, csrf.sub(rb"\1\2", client.get(u).data)) for u in urls}

    before_db = [Chapter.query.count(), Note.query.count(), Question.query.count()]
    before = snap()
    canon.seed(); canon.seed_subtopics(subs.expanded())
    assert [Chapter.query.count(), Note.query.count(), Question.query.count()] == before_db
    assert snap() == before
    assert all(code == 200 for code, _ in before.values())


def test_migration_downgrade_refuses_to_discard_provenance_or_canonical_rows(tmp_path, monkeypatch):
    import sqlalchemy as sa
    from alembic import command
    from alembic.config import Config as AlembicConfig
    url = f"sqlite:///{tmp_path / 'p.db'}"
    monkeypatch.setenv("ALEMBIC_DATABASE_URL", url)
    cfg = AlembicConfig(str(ROOT / "alembic.ini")); cfg.set_main_option("script_location", str(ROOT / "migrations"))
    command.upgrade(cfg, "head")
    eng = sa.create_engine(url)
    with eng.begin() as c:
        c.execute(sa.text("INSERT INTO subjects (id,slug,name_en,name_te) VALUES (1,'ap_history','AP','ఏపీ')"))
        c.execute(sa.text("INSERT INTO questions (subject_id,source_type,correct_answer,source,source_qid) VALUES (1,'chapter','a','codex_generated','X1')"))
    with pytest.raises(RuntimeError, match="Refusing to drop provenance"):
        command.downgrade(cfg, "c3d4e5f6a7b8")
    with eng.begin() as c:
        c.execute(sa.text("UPDATE questions SET source=NULL, source_qid=NULL"))
        c.execute(sa.text("INSERT INTO syllabus_units (subject_id,unit_num,slug,title_en,title_te) VALUES (1,1,'u1','a','అ')"))
    with pytest.raises(RuntimeError, match="Refusing to drop syllabus_units"):
        command.downgrade(cfg, "c3d4e5f6a7b8")
