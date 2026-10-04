"""Every image a note can show either loads (HTTP 200, an image) or is replaced by a visible 'source needed' notice.

Deterministic: it walks ALL shipped notes (data/content.db.gz) and ALL notes parsed from the tracked AP History HTML,
instead of sampling a few pages in a browser.
"""
import re

import pytest
from bs4 import BeautifulSoup

from app.db import db
from app.models import Subject
from app.services import content_import as ci
from app.services import note_images as ni
from app.services.learn import render_note_html
from tests.real_data import real_slice

IMG = re.compile(r"<img\b[^>]*>", re.I)
SRC = re.compile(r'src="([^"]*)"')


def all_shipped_notes():
    with ci.open_source() as real:
        return [(r["chapter_id"], r["section_num"], (r["body_en"] or "") + "\n" + (r["body_te"] or ""))
                for r in real.execute("SELECT chapter_id, section_num, body_en, body_te FROM notes")]


def rendered_images(bodies):
    urls, notices, tags = set(), 0, 0
    for body in bodies:
        out = render_note_html(body)
        notices += out.count('class="note-img-missing"')
        for tag in IMG.findall(out):
            tags += 1
            m = SRC.search(tag)
            urls.add(m.group(1) if m else None)
    return urls, notices, tags


def assert_all_load(client, urls):
    for u in sorted(urls):
        assert u and (u.startswith("/static/") or u.startswith("https://")), f"an <img> without a loadable src: {u!r}"
        if u.startswith("/static/"):
            r = client.get(u)
            assert r.status_code == 200, u
            assert r.headers["Content-Type"].startswith("image/"), (u, r.headers["Content-Type"])
            assert len(r.data) > 1000, u


# ── every shipped note ────────────────────────────────────────────────────────────────────────────────
def test_every_image_in_every_shipped_note_loads(app, client):
    notes = all_shipped_notes()
    assert len(notes) == 980                                       # the whole shipped set, not a sample
    urls, notices, tags = rendered_images(b for _c, _s, b in notes)
    assert tags >= 14, "the shipped notes are known to contain 14 images"
    assert notices == 0, f"{notices} images have no shipped file"
    assert_all_load(client, urls)
    assert "/static/notes/ap_28_districts_map.jpg" in urls
    assert any(u.startswith("/static/notes/AP_History/Chapters/ap_ch") for u in urls)


def test_no_bare_relative_src_survives_rendering(app):
    for _c, _s, body in all_shipped_notes():
        for tag in IMG.findall(render_note_html(body)):
            m = SRC.search(tag)
            assert m and re.match(r"(/static/|https://)", m.group(1)), tag


# ── every note the AP History HTML source would import ────────────────────────────────────────────────
def test_every_image_in_the_ap_history_html_source_loads_or_becomes_a_notice(app, client):
    db.session.add(Subject(slug="ap_history", name_en="AP History", name_te="ఏపీ చరిత్ర")); db.session.commit()
    from app.services import ap_history_parse as ap
    src = ap.build_source()
    try:
        bodies = [(r[0] or "") + (r[1] or "") for r in src.execute("SELECT body_en, body_te FROM notes")]
        raw_refs = [m for b in bodies for m in re.findall(r'<img[^>]*\ssrc="([^"]+)"', b)]
    finally:
        src.close()
    assert len(bodies) >= 220 and len(raw_refs) >= 12      # the HTML tracked in the repository
    urls, notices, tags = rendered_images(bodies)
    unresolved = [r for r in raw_refs if ni.resolve(r)[1] == "missing"]
    assert notices == len(unresolved)                              # each unresolvable image is a notice, none is dropped
    assert tags == len(raw_refs) - len(unresolved)
    assert_all_load(client, urls)                                  # and every remaining image really loads


# ── the real page, and the legacy reader ──────────────────────────────────────────────────────────────
def test_map_loads_on_the_real_learn_and_legacy_note_pages(app, client):
    real_slice(["ap_history"], chapters_per_subject=12)
    from app.models import Chapter, Note
    ch = Chapter.query.filter_by(chapter_num=1).join(Subject).filter(Subject.slug == "ap_history").one()
    sec = next(n for n in Note.query.filter_by(chapter_id=ch.id) if "ap_prehistoric_sites_annotated" in (n.body_en or "") + (n.body_te or ""))
    page = client.get(f"/learn/topic/{ch.id}/notes?section={sec.section_num}").get_data(as_text=True)
    img = BeautifulSoup(page, "html.parser").select_one("#note img[src*=ap_prehistoric_sites_annotated]")
    assert img and img["src"] == "/static/notes/AP_History/Chapters/ap_prehistoric_sites_annotated.jpg"
    r = client.get(img["src"])
    assert r.status_code == 200 and r.headers["Content-Type"] == "image/jpeg"
    legacy = client.get("/notes/ap_history/1").get_data(as_text=True)
    assert "/static/notes/AP_History/Chapters/ap_prehistoric_sites_annotated.jpg" in legacy
    assert 'src="ap_prehistoric_sites_annotated.jpg"' not in legacy


# ── rules ─────────────────────────────────────────────────────────────────────────────────────────────
def test_existing_district_map_resolves_to_the_absolute_static_path():
    assert ni.resolve("ap_28_districts_map.jpg") == ("/static/notes/ap_28_districts_map.jpg", "local")
    assert ni.resolve("./ap_28_districts_map.jpg")[0] == "/static/notes/ap_28_districts_map.jpg"
    assert ni.resolve("/static/notes/ap_28_districts_map.jpg")[1] == "local"
    assert 'src="/static/notes/ap_28_districts_map.jpg"' in render_note_html('<img src="ap_28_districts_map.jpg" alt="map">')


def test_missing_image_becomes_a_visible_notice_not_a_broken_icon():
    out = render_note_html('<p>before</p><img src="no_such_map.jpg" alt="x"><p>after</p>')
    assert "<img" not in out and 'class="note-img-missing"' in out
    assert "Image unavailable" in out and "source needed" in out and "<code>no_such_map.jpg</code>" in out
    assert "before" in out and "after" in out


@pytest.mark.parametrize("bad", ["javascript:alert(1)", "data:image/png;base64,AAAA", "file:///etc/passwd", "//evil.example/x.jpg",
                                 "../../app/config.py", "/etc/passwd", "/static/../app/config.py", "/static/notes/missing.jpg", "", "   "])
def test_unsafe_or_unloadable_sources_become_notices(bad):
    out = render_note_html(f'<img src="{bad}" alt="x">')
    assert "<img" not in out and "note-img-missing" in out


def test_image_without_any_src_becomes_a_notice():
    assert "note-img-missing" in render_note_html('<img alt="lost">')


def test_notice_escapes_the_file_name():
    out = render_note_html('<img src="a&quot;&gt;&lt;script&gt;alert(1)&lt;/script&gt;.jpg">')
    assert "<script" not in out and "<code>" in out and "alert(1)</script" not in out


def test_external_https_images_are_left_alone():
    out = render_note_html('<img src="https://example.org/a.png" alt="x">')
    assert 'src="https://example.org/a.png"' in out


def test_ambiguous_suffix_is_not_guessed(monkeypatch):
    monkeypatch.setattr(ni, "_index", lambda: ({"a/x.jpg", "b/x.jpg"}, {"x.jpg": ["a/x.jpg", "b/x.jpg"], "a/x.jpg": ["a/x.jpg"], "b/x.jpg": ["b/x.jpg"]}))
    assert ni.resolve("x.jpg") == (None, "missing")
    assert ni.resolve("a/x.jpg")[1] == "local"


def test_unique_suffix_finds_a_nested_file(monkeypatch):
    monkeypatch.setattr(ni, "_index", lambda: ({"AP_History/Chapters/wiki_images/y.jpg"},
                                               {"wiki_images/y.jpg": ["AP_History/Chapters/wiki_images/y.jpg"], "y.jpg": ["AP_History/Chapters/wiki_images/y.jpg"]}))
    assert ni.resolve("wiki_images/y.jpg") == ("/static/notes/AP_History/Chapters/wiki_images/y.jpg", "local")


def test_alt_width_height_survive_and_images_are_lazy():
    out = render_note_html('<img src="ap_28_districts_map.jpg" alt="map of AP" width="300" height="200" onerror="alert(1)" style="x:y">')
    assert 'alt="map of AP"' in out and 'width="300"' in out and 'height="200"' in out and 'loading="lazy"' in out
    assert "onerror" not in out and "style" not in out


def test_the_thirteen_referenced_files_are_in_the_repository():
    import os
    for name in ("ap_prehistoric_sites_annotated", "ap_ch02_historical_sources_map", "ap_ch03_pre_satavahana_sites",
                 "ap_ch04_dynasty_capitals", "ap_ch05_satavahana_sites", "ap_ch06_ikshvaku_sites", "ap_ch07_minor_dynasties_sites",
                 "ap_ch08_vishnukundin_sites", "ap_ch09_eastern_chalukya_sites", "ap_ch10_kakatiya_sites", "ap_ch11_reddy_sites",
                 "ap_ch12_vijayanagara_sites"):
        assert os.path.getsize(os.path.join(ni.NOTES_ROOT, "AP_History", "Chapters", name + ".jpg")) > 100_000
    assert os.path.getsize(os.path.join(ni.NOTES_ROOT, "ap_28_districts_map.jpg")) > 50_000
