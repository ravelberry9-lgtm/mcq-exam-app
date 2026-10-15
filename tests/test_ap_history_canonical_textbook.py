import hashlib
from app.db import db
from app.models import Subject
from app.services import ap_canonical, canonical_textbook


def seed_history():
    db.session.add(Subject(slug="ap_history", name_en="AP History", name_te="ఆంధ్ర చరిత్ర")); db.session.commit(); ap_canonical.seed()


def test_canonical_package_and_all_routes(client, app):
    with app.app_context():
        seed_history(); rows = canonical_textbook.all_chapters()
    assert len(rows) == 31 and [r["chapter"] for r in rows] == list(range(1, 32))
    assert rows[8]["languages"] == ["te"]
    for row in rows:
        reader = client.get(f"/learn/ap-history/{row['slug']}/canonical-textbook")
        content = client.get(f"/learn/ap-history/{row['slug']}/canonical-textbook/content")
        assert reader.status_code == content.status_code == 200
        assert hashlib.sha256(content.data).hexdigest().upper() == row["html_sha256"]
        if row["chapter"] < 31:
            assert f"/{rows[row['chapter']]['slug']}/canonical-textbook" in reader.get_data(as_text=True)


def test_chapter9_disables_unapproved_languages(client, app):
    with app.app_context(): seed_history()
    text = client.get('/learn/ap-history/u2-c09-kakatiyas/canonical-textbook').get_data(as_text=True)
    assert "No translation has been fabricated" in text
    assert 'data-v="en"' in text and "disabled" in text
