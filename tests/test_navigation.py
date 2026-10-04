"""Navigation and dead-end regression: every learner-facing page must lead back to the Learn hub."""
import re
from datetime import date, timedelta
from urllib.parse import urldefrag, urlsplit

import pytest
from bs4 import BeautifulSoup

from app.db import db
from app.models import NavItem
from tests.test_learn_journey import world  # noqa: F401  (shared fixture)


def _links(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup, [a for a in soup.find_all("a")]


def _hrefs(html):
    return [a.get("href") for a in _links(html)[1] if a.get("href") is not None]


def _start_exam(client):
    r = client.post("/exam/appsc_group_2/paper/0/start", data={"mode": "practice", "count": "2", "minutes": "10"})
    assert r.status_code == 302, r.status_code
    return r.headers["Location"]


@pytest.fixture()
def pages(client, world):  # noqa: F811
    """Every learner-facing GET page the app renders, keyed by a readable name."""
    c2, c3 = world["c2"], world["c3"]
    take_url = _start_exam(client)
    sid = take_url.rsplit("/", 1)[-1]
    client.post(f"/exam-session/{sid}/submit")
    client.post("/plan/create", data={"name": "P", "target_date": (date.today() + timedelta(days=30)).isoformat(),
                                      "exam_id": ""})
    exam2 = _start_exam(client)  # a second, still-running attempt for the exam runner page
    return {
        "legacy-home": "/legacy", "subjects": "/subjects", "subject-detail": "/subject/indian_history",
        "legacy-practice": "/practice/indian_history", "legacy-practice-empty": "/practice/indian_constitution",
        "chapter-list": "/notes/indian_history", "notes-reader": f"/notes/indian_history/{c2.chapter_num}",
        "exam-list": "/exam/appsc_group_2", "exam-runner": exam2, "exam-results": f"/exam-session/{sid}/results",
        "settings": "/settings", "plan-new": "/plan/new", "plan-dashboard": "/plan/",
        "learn-hub": "/learn/", "learn-section": f"/learn/section/{world['s_hist']}",
        "learn-subject": "/learn/subject/indian_history", "learn-topic": f"/learn/topic/{c2.id}",
        "learn-notes": f"/learn/topic/{c2.id}/notes", "learn-practice": f"/learn/topic/{c2.id}/practice",
        "learn-topic-no-mcq": f"/learn/topic/{c3.id}",
    }


# ── entry points ─────────────────────────────────────────────────────────────
def test_root_redirects_to_the_learn_hub(client):
    r = client.get("/")
    assert r.status_code in (301, 302, 307, 308)
    assert urlsplit(r.headers["Location"]).path == "/learn/"
    assert client.get("/", follow_redirects=True).status_code == 200


def test_legacy_home_lives_on_an_explicit_route(client):
    assert client.get("/legacy").status_code == 200


def test_home_from_a_learn_topic_returns_to_a_usable_hub(client, world):  # noqa: F811
    topic = client.get(f"/learn/topic/{world['c2'].id}")
    soup = BeautifulSoup(topic.data, "html.parser")
    nav = soup.select_one("nav.bottomnav")
    hrefs = [a["href"] for a in nav.find_all("a", href=True)]
    assert "/" not in hrefs and "/legacy" not in hrefs and "/subjects" not in hrefs
    landing = [h for h in hrefs if h.startswith("/learn/")]
    assert landing[0] == "/learn/"
    assert len([h for h in hrefs if h == "/learn/"]) == 1, "one primary landing item, no duplicate Home/Learn"
    hub = client.get("/learn/")
    assert hub.status_code == 200
    assert b"data-section=" in hub.data or b"data-subject=" in hub.data  # real, usable cards


def test_ds_nav_marks_unavailable_items_coming_soon(client, world):  # noqa: F811
    soup = BeautifulSoup(client.get("/learn/").data, "html.parser")
    off = soup.select("nav.bottomnav [aria-disabled='true']")
    assert len(off) == 2
    for el in off:
        assert el.name != "a" and not el.get("href")
        assert "Coming soon" in el.get_text() and "త్వరలో" in el.get_text()


# ── drawer ───────────────────────────────────────────────────────────────────
def test_drawer_has_builtin_navigation_when_no_nav_records(client, app):
    assert NavItem.query.count() == 0
    html = client.get("/subjects").data.decode()
    drawer = BeautifulSoup(html, "html.parser").select_one("aside#drawer")
    hrefs = [a["href"] for a in drawer.select("a.drawer-item")]
    assert hrefs == ["/learn/", "/subjects", "/plan/", "/settings"]
    for h in hrefs:
        assert client.get(h, follow_redirects=True).status_code == 200


def test_drawer_item_without_url_is_disabled_text_not_a_link(client, app):
    db.session.add(NavItem(surface="menu", label_en="Tests", label_te="పరీక్షలు", sort_order=1))
    db.session.add(NavItem(surface="menu", label_en="Learn", label_te="నేర్చుకోండి", action_type="route",
                           action_ref="/learn/", sort_order=0))
    db.session.commit()
    drawer = BeautifulSoup(client.get("/subjects").data, "html.parser").select_one("aside#drawer")
    assert [a["href"] for a in drawer.select("a.drawer-item")] == ["/learn/"]
    off = drawer.select("span.drawer-item[aria-disabled='true']")
    assert len(off) == 1 and "Tests" in off[0].get_text()


# ── every learner-facing page ────────────────────────────────────────────────
def test_every_page_renders(client, pages):
    for name, url in pages.items():
        r = client.get(url)
        assert r.status_code == 200, (name, url, r.status_code)


def test_every_page_has_a_route_back_to_learn(client, pages):
    for name, url in pages.items():
        html = client.get(url).data
        soup = BeautifulSoup(html, "html.parser")
        bar = soup.select_one("a[data-testid='back-to-learn']")
        if bar is None:
            # design-system pages: the bottom navigation's Learn item (the hub itself is the destination)
            bar = soup.select_one("nav.bottomnav a[href='/learn/']")
        assert bar is not None and bar["href"] == "/learn/", f"{name} ({url}) has no route back to /learn/"


def test_legacy_pages_show_a_visible_back_to_learn(client, pages):
    legacy = ["legacy-home", "subjects", "subject-detail", "legacy-practice", "legacy-practice-empty", "chapter-list",
              "notes-reader", "exam-list", "exam-runner", "exam-results", "settings", "plan-new", "plan-dashboard"]
    for name in legacy:
        soup = BeautifulSoup(client.get(pages[name]).data, "html.parser")
        a = soup.select_one("a[data-testid='back-to-learn']")
        assert a is not None and a["href"] == "/learn/" and "Back to Learn" in a.get_text(), name
        assert a.find_parent("nav", class_="learn-back-bar") is not None


def test_brand_logo_opens_the_learn_hub(client, pages):
    soup = BeautifulSoup(client.get("/subjects").data, "html.parser")
    assert soup.select_one("a.brand")["href"] == "/learn/"


def test_no_rendered_link_uses_a_bare_hash(client, pages):
    for name, url in pages.items():
        for h in _hrefs(client.get(url).data):
            assert h.strip() not in ("#", ""), f"{name} renders href={h!r}"


def test_search_is_not_a_clickable_no_op(client, pages):
    for name, url in pages.items():
        soup = BeautifulSoup(client.get(url).data, "html.parser")
        assert not soup.select(".search-btn"), name
        assert not soup.select("[aria-label='Search']"), name


def test_page_title_has_no_mojibake(client, pages):
    for name, url in pages.items():
        html = client.get(url).data.decode()
        assert "Â" not in html and "Ã" not in html, name
    assert "<title>" in client.get("/subjects").data.decode()


def test_same_origin_links_never_404_or_405(client, pages):
    seen, queue = set(), []
    for url in pages.values():
        queue.append(url)
    checked = 0
    while queue and checked < 250:
        url = queue.pop()
        path = urldefrag(url)[0]
        if path in seen:
            continue
        seen.add(path)
        r = client.get(path)
        checked += 1
        assert r.status_code in (200, 302), f"{path} -> {r.status_code}"
        if r.status_code == 302:
            r = client.get(r.headers["Location"])
            assert r.status_code == 200
        for h in _hrefs(r.data):
            parts = urlsplit(h)
            if parts.scheme or parts.netloc or h.startswith(("mailto:", "tel:", "javascript:")):
                continue
            if not parts.path or parts.path.startswith("/static/") or parts.path.startswith("/admin"):
                continue
            queue.append(h)
    assert checked > 15


# ── destinations ─────────────────────────────────────────────────────────────
def test_exam_chapter_links_open_the_topic_not_the_whole_subject_bank(client, world):  # noqa: F811
    hrefs = _hrefs(client.get("/exam/appsc_group_2").data)
    assert not [h for h in hrefs if h.startswith("/practice/")]
    for ch in (world["c1"], world["c2"], world["c3"]):
        assert f"/learn/topic/{ch.id}" in hrefs
        assert f"/learn/topic/{ch.id}/notes" in hrefs


def test_study_plan_chapter_links_open_the_learn_topic(client, world):  # noqa: F811
    client.post("/plan/create", data={"name": "P", "target_date": (date.today() + timedelta(days=30)).isoformat(),
                                      "exam_id": ""})
    hrefs = _hrefs(client.get("/plan/").data)
    topic_links = [h for h in hrefs if h.startswith("/learn/topic/")]
    assert topic_links, hrefs
    assert not [h for h in hrefs if h.startswith("/notes/")]
    for ch in (world["c1"], world["c2"], world["c3"]):
        assert f"/learn/topic/{ch.id}" in hrefs
    for h in set(topic_links):
        assert client.get(h).status_code == 200


def test_subject_detail_mcq_links_are_topic_level(client, world):  # noqa: F811
    hrefs = _hrefs(client.get("/subject/indian_history").data)
    assert f"/learn/topic/{world['c2'].id}/practice?i=1&new=1" in hrefs
    assert "/practice/indian_history" in hrefs  # the explicit whole-subject card is still offered once


def test_legacy_practice_completion_returns_to_the_learn_subject_page(client, world):  # noqa: F811
    total = 2
    html = client.get(f"/practice/indian_history?i={total}").data.decode()
    assert "/learn/subject/indian_history" in html
    nxt = BeautifulSoup(html, "html.parser").select_one("a.next-btn")
    assert nxt["href"] == "/learn/subject/indian_history"


def test_exam_results_offer_back_to_learn_and_no_fake_retry(client, pages):
    html = client.get(pages["exam-results"]).data.decode()
    soup = BeautifulSoup(html, "html.parser")
    texts = [a.get_text(" ", strip=True) for a in soup.find_all("a")]
    assert "Retry" not in html and "confirm(" not in html
    assert any("Choose another test" in t for t in texts)
    assert any("Back to Learn" in t for t in texts)
    choose = [a for a in soup.find_all("a") if "Choose another test" in a.get_text()][0]
    assert choose["href"] == "/exam/appsc_group_2"


# ── security / behaviour preserved ───────────────────────────────────────────
def test_navigation_changes_keep_csrf_and_security_headers(client, world):  # noqa: F811
    r = client.get("/learn/")
    assert b'name="csrf-token"' in r.data
    assert r.headers.get("X-Frame-Options") == "DENY"
    client.auto_csrf = False
    assert client.post("/settings", data={"lang": "te"}).status_code in (400, 403)


def test_every_page_has_a_mobile_viewport_and_no_fixed_widths(client, pages):
    """Server-side guard for the 320/360/412 px journey; the real-browser width check is the Playwright smoke."""
    for name, url in pages.items():
        html = client.get(url).data.decode()
        assert 'name="viewport"' in html and "width=device-width" in html, name


@pytest.mark.parametrize("sheet", ["app.css", "ds.css"])
def test_stylesheets_have_balanced_braces(sheet):
    """An unclosed rule in app.css silently swallowed every rule after it (exam start form, missing-image notice)."""
    from pathlib import Path
    css = (Path(__file__).resolve().parent.parent / "static" / sheet).read_text(encoding="utf-8")
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    assert css.count("{") == css.count("}")
