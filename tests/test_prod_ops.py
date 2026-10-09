"""Read-only production check kit: it must never write, never print connection details, and must detect a bad backup."""
import importlib.util
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / "prod_ops" / f"{name}.py")
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m)
    return m


snap = _load("readonly_snapshot")
cmp_ = _load("compare_snapshots")
PG = os.environ.get("TEST_PG_URL")


def test_scrub_removes_every_connection_detail():
    url = "postgresql://dbuser:s3cretpw@host-abc.proxy.example.net:12345/railwaydb"
    msg = 'connection to server at "host-abc.proxy.example.net" (1.2.3.4), port 12345 failed: password s3cretpw user dbuser db railwaydb ' + url
    out = snap.scrub(msg, url)
    for secret in ("s3cretpw", "host-abc", "dbuser", "railwaydb", "12345", "postgresql://"):
        assert secret not in out


def test_failed_connection_never_echoes_the_url(monkeypatch, capsys):
    monkeypatch.setenv("DATABASE_URL", "postgresql://dbuser:s3cretpw@no-such-host-xyz.invalid:5432/railwaydb")
    with pytest.raises(SystemExit) as e:
        snap.main(["--label", "PRODUCTION"])
    text = str(e.value) + capsys.readouterr().out
    for secret in ("s3cretpw", "no-such-host-xyz", "dbuser", "railwaydb"):
        assert secret not in text


def test_label_is_required():
    with pytest.raises(SystemExit):
        snap.main([])


def test_compare_detects_changed_content_missing_rows_and_wrong_revision():
    a = {"label": "PRODUCTION", "taken_at_utc": "t", "alembic_version": ["d4e5f6a7b8c9"], "row_counts": {"questions": 10, "exam_sessions": 5},
         "fingerprints": {"questions": {"md5": "aa"}}, "canonical_inventory": {"md5": "x"}}
    b = {**a, "label": "BACKUP-RESTORE", "row_counts": {"questions": 10, "exam_sessions": 6}}
    bad, info = cmp_.compare(a, b)
    assert bad == [] and info == ["exam_sessions: rows 5 != 6"]          # activity drift is only a note
    b2 = {**b, "row_counts": {"questions": 9, "exam_sessions": 5}, "fingerprints": {"questions": {"md5": "bb"}}, "alembic_version": ["c3d4e5f6a7b8"]}
    bad, _ = cmp_.compare(a, b2)
    assert len(bad) == 3


@pytest.mark.skipif(not PG, reason="needs TEST_PG_URL")
def test_session_is_read_only_and_snapshot_has_no_side_effects():
    import psycopg2
    url = PG.replace("postgresql+psycopg2://", "postgresql://")
    con = snap.connect(url)
    cur = con.cursor()
    cur.execute("show transaction_read_only")
    assert cur.fetchone()[0] == "on"
    with pytest.raises(psycopg2.Error):
        cur.execute("create table should_never_exist(x int)")
    con.rollback()
    s, inv = snap.snapshot(con, "LOCAL")
    assert s["transaction_read_only"] == "on" and s["label"] == "LOCAL"
    con.close()
    con2 = snap.connect(url); c2 = con2.cursor()
    c2.execute("select to_regclass('should_never_exist') is null"); assert c2.fetchone()[0] is True
    con2.close()
