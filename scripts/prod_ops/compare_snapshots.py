#!/usr/bin/env python3
"""Compare two snapshots from readonly_snapshot.py (production vs. its restored backup).

    python scripts/prod_ops/compare_snapshots.py prod_before.json restored.json

Content tables must match exactly (counts and fingerprints), as must the Alembic revision and the canonical inventory.
Activity tables (learner progress, sessions, plans) may legitimately differ on a live site and are only reported.
Exit status 0 = backup verified, 1 = mismatch.
"""
import json
import sys

ACTIVITY = ("user_question_state", "exam_sessions", "chapter_progress", "study_plans", "note_backups")


def compare(a, b):
    bad, info = [], []
    if a["alembic_version"] != b["alembic_version"]:
        bad.append(f"alembic_version {a['alembic_version']} != {b['alembic_version']}")
    for t in sorted(set(a["row_counts"]) | set(b["row_counts"])):
        ca, cb = a["row_counts"].get(t), b["row_counts"].get(t)
        if ca != cb:
            (info if t in ACTIVITY else bad).append(f"{t}: rows {ca} != {cb}")
    for t in sorted(set(a["fingerprints"]) | set(b["fingerprints"])):
        fa, fb = a["fingerprints"].get(t), b["fingerprints"].get(t)
        if fa != fb:
            bad.append(f"{t}: content fingerprint differs")
    if a["canonical_inventory"]["md5"] != b["canonical_inventory"]["md5"]:
        bad.append("canonical inventory differs")
    return bad, info


def main():
    a, b = (json.load(open(p, encoding="utf-8")) for p in sys.argv[1:3])
    bad, info = compare(a, b)
    print(f"A: {a['label']} {a['taken_at_utc']}\nB: {b['label']} {b['taken_at_utc']}")
    for m in info:
        print("note (activity table, may drift on a live site):", m)
    for m in bad:
        print("MISMATCH:", m)
    print("RESULT:", "BACKUP VERIFIED (content identical)" if not bad else "NOT VERIFIED")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
