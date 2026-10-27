from bs4 import BeautifulSoup


def test_geography_landing_has_exactly_two_umbrellas(client):
    response = client.get("/learn/geography/")
    soup = BeautifulSoup(response.data, "html.parser")
    cards = soup.select("[data-geography-umbrella]")
    assert response.status_code == 200
    assert [card["data-geography-umbrella"] for card in cards] == ["world", "india-ap"]
    assert cards[0]["href"] == "/learn/geography/world"
    assert cards[1]["href"] == "/learn/geography/india-ap"
    assert not soup.select("[data-geography-unit]")


def test_world_umbrella_keeps_29_chapters_and_scoped_pyqs(client):
    response = client.get("/learn/geography/world")
    soup = BeautifulSoup(response.data, "html.parser")
    assert response.status_code == 200
    assert len(soup.select("[data-world-chapter]")) == 29
    assert soup.select_one("[data-world-pyqs]")["href"] == "/learn/geography/pyqs?umbrella=world"
    pyqs = client.get("/learn/geography/pyqs?umbrella=world")
    assert pyqs.status_code == 200
    assert b'name="umbrella" value="world"' in pyqs.data


def test_legacy_world_chapter_keeps_notes_mcqs_and_pyqs(client):
    response = client.get("/learn/geography/world/4")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "/learn/geography/lesson/04" in html
    assert "/learn/geography/original-practice?chapter=04" in html
    assert "/learn/geography/pyqs?umbrella=world&amp;lesson=04" in html


def test_india_ap_umbrella_excludes_world_lessons(client):
    response = client.get("/learn/geography/india-ap")
    soup = BeautifulSoup(response.data, "html.parser")
    assert response.status_code == 200
    assert soup.select("[data-geography-unit]")
    assert not soup.select_one('[data-geography-lesson="01"]')
    assert "/learn/geography/pyqs?umbrella=india-ap" in response.get_data(as_text=True)


def test_umbrella_pyq_filters_reject_cross_scope_lessons(client):
    assert client.get("/learn/geography/pyqs?umbrella=india-ap&lesson=01").status_code == 404
    assert client.get("/learn/geography/pyqs?umbrella=unknown").status_code == 400
