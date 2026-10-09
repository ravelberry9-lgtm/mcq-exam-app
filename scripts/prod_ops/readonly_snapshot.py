#!/usr/bin/env python3
"""READ-ONLY snapshot of a database: Alembic revision, row counts, content fingerprints, canonical inventory.

    set DATABASE_URL=<the database to inspect>
    python scripts/prod_ops/readonly_snapshot.py --label PRODUCTION --out prod_before.json [--inventory-csv pre_change_inventory.csv]

Safety properties (each is tested in tests/test_prod_ops.py):
* the session is opened read-only (server-side default_transaction_read_only plus a read-only psycopg2 session), so any
  write attempt fails;
* only SELECT statements built in this file are run; table names come from information_schema and are quoted;
* the connection URL, host, user and password are never printed or written, and error text is scrubbed of them;
* --label is printed and stored so a snapshot is always identified as PRODUCTION / BACKUP-RESTORE / LOCAL.
Share the printed summary or the JSON file (it contains counts, hashes and slugs, no learner content).
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys
from urllib.parse import urlparse, unquote

import psycopg2
from psycopg2 import sql

# tables whose full content is fingerprinted (stable between a backup and a quiet production); activity tables get counts only
CONTENT_TABLES = ("subjects", "chapters", "notes", "pages", "passages", "questions", "exams", "exam_papers", "exam_sections",
                  "exam_syllabus_items", "nav_items", "syllabus_units", "syllabus_chapters", "syllabus_subtopics",
                  "syllabus_microtopics", "chapter_source_map", "expanded_notes", "expanded_note_app_map")
INVENTORY = (("unit", "syllabus_units"), ("chapter", "syllabus_chapters"), ("subtopic", "syllabus_subtopics"),
             ("microtopic", "syllabus_microtopics"))


def _dsn_parts(url):
    u = urlparse(url)
    return [p for p in {u.hostname, u.username, unquote(u.password or ""), str(u.port or ""), u.path.lstrip("/")} if p and len(p) > 2]


def scrub(text, url):
    for p in _dsn_parts(url):
        text = text.replace(p, "***")
    return re.sub(r"postgres(ql)?(\+\w+)?://\S+", "<url>", text)


def connect(url):
    if not url:
        sys.exit("DATABASE_URL is not set")
    clean = re.sub(r"^postgres(ql)?\+\w+://", lambda m: "postgresql://", url)
    try:
        con = psycopg2.connect(clean, connect_timeout=20, options="-c default_transaction_read_only=on -c statement_timeout=120000")
    except psycopg2.Error as e:
        sys.exit("could not connect: " + scrub(str(e).splitlines()[0] if str(e) else e.__class__.__name__, url))
    con.set_session(readonly=True, autocommit=False)
    return con


def one(cur, query, *args):
    cur.execute(query, args)
    return cur.fetchone()[0]


def snapshot(con, label):
    cur = con.cursor()
    out = {"tool": "readonly_snapshot/1", "label": label, "taken_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "server_version": one(cur, "show server_version"), "database_size_bytes": one(cur, "select pg_database_size(current_database())"),
           "transaction_read_only": one(cur, "show transaction_read_only")}
    tables = [r[0] for r in (cur.execute("select table_name from information_schema.tables where table_schema='public' "
                                         "and table_type='BASE TABLE' order by 1") or cur.fetchall())]
    out["tables"] = tables
    out["alembic_version"] = [r[0] for r in (cur.execute("select version_num from alembic_version") or cur.fetchall())] if "alembic_version" in tables else None
    counts, prints = {}, {}
    for t in tables:
        counts[t] = one(cur, sql.SQL("select count(*) from {}").format(sql.Identifier(t)))
        if t in CONTENT_TABLES:
            cols = [r[0] for r in (cur.execute("select column_name from information_schema.columns where table_schema='public' and table_name=%s "
                                               "order by ordinal_position", (t,)) or cur.fetchall())]
            order = "id" if "id" in cols else cols[0]
            h = one(cur, sql.SQL("select coalesce(md5(string_agg(md5(t::text), '' order by {o})), 'empty') from {t} t").format(
                o=sql.Identifier(order), t=sql.Identifier(t)))
            prints[t] = {"md5": h, "columns": len(cols)}
    out["row_counts"], out["fingerprints"] = counts, prints
    if "questions" in tables:
        cols = {r[0] for r in (cur.execute("select column_name from information_schema.columns where table_schema='public' and table_name='questions'") or cur.fetchall())}
        out["questions_columns_present"] = {c: (c in cols) for c in ("note_section_num", "note_target_slug", "source_trace", "import_ref",
                                                                       "syllabus_chapter_id", "subtopic_id", "source", "source_qid", "batch_id")}
        cur.execute("select source_type, count(*) from questions group by 1 order by 1")
        out["questions_by_source_type"] = dict(cur.fetchall())
        if "import_ref" in cols:
            out["questions_with_import_ref"] = one(cur, "select count(*) from questions where import_ref is not null")
        if "source_qid" in cols:
            out["questions_with_source_qid"] = one(cur, "select count(*) from questions where source_qid is not null")
        if "batch_id" in cols:
            cur.execute("select batch_id, count(*) from questions where batch_id is not null group by 1 order by 1")
            out["questions_by_batch"] = dict(cur.fetchall())
    if "subjects" in tables and "questions" in tables:
        cur.execute("select s.slug, count(q.id) from subjects s left join questions q on q.subject_id=s.id group by s.slug order by s.slug")
        out["questions_by_subject"] = dict(cur.fetchall())
    inv = []
    for kind, t in INVENTORY:
        if t in tables:
            cur.execute(sql.SQL("select slug from {} order by slug").format(sql.Identifier(t)))
            inv += [(kind, r[0]) for r in cur.fetchall()]
    out["canonical_inventory"] = {"rows": len(inv), "md5": hashlib.md5(json.dumps(inv).encode()).hexdigest(),
                                  "by_kind": {k: sum(1 for x in inv if x[0] == k) for k, _ in INVENTORY}}
    con.rollback()
    return out, inv


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--label", required=True, help="PRODUCTION, BACKUP-RESTORE or LOCAL: identifies what was inspected")
    ap.add_argument("--out", help="write the JSON snapshot here")
    ap.add_argument("--inventory-csv", help="write the canonical-slug inventory used by docs/rollback_c1_additive.sql")
    a = ap.parse_args(argv)
    url = os.environ.get("DATABASE_URL", "")
    con = connect(url)
    try:
        snap, inv = snapshot(con, a.label.upper())
    except psycopg2.Error as e:
        sys.exit("query failed: " + scrub(str(e).splitlines()[0], url))
    finally:
        con.close()
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(snap, f, indent=1, sort_keys=True)
    if a.inventory_csv:
        with open(a.inventory_csv, "w", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(inv)
    print(f"=== READ-ONLY SNAPSHOT: {snap['label']} ({snap['taken_at_utc']}) ===")
    print("alembic_version :", snap["alembic_version"])
    print("server_version  :", snap["server_version"], "| read-only session:", snap["transaction_read_only"])
    print("row counts      :", json.dumps({k: v for k, v in snap["row_counts"].items()}, sort_keys=True))
    print("questions       :", json.dumps(snap.get("questions_by_source_type")), "| columns:", json.dumps(snap.get("questions_columns_present")))
    print("canonical rows  :", json.dumps(snap["canonical_inventory"]["by_kind"]))
    print("fingerprints    :", json.dumps({k: v["md5"][:10] for k, v in snap["fingerprints"].items()}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
