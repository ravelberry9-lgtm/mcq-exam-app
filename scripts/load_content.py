#!/usr/bin/env python3
"""Command-line front end for the safe content import (app/services/content_import.py).

    python scripts/load_content.py                          # preview only: prints the plan, changes nothing
    python scripts/load_content.py --subjects a,b           # add what is missing for those subjects
    python scripts/load_content.py --all-subjects           # same, for every subject in the source
    python scripts/load_content.py --subjects a --replace-notes --yes   # also replace notes that differ (backed up)
    python scripts/load_content.py --subjects a --remove-extra  --yes   # also remove live-only notes (backed up)
    python scripts/load_content.py --restore BATCH_ID --yes             # put back notes saved by an earlier import

Without --replace-notes / --remove-extra it never modifies or deletes an existing row. Replace/remove need --yes.
Everything runs in one transaction. Reads DATABASE_URL like the app does.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402
from app.services import content_import as ci  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", help="path to content.db (default data/content.db, or data/content.db.gz)")
    ap.add_argument("--subjects", help="comma-separated subject slugs to import")
    ap.add_argument("--all-subjects", action="store_true")
    ap.add_argument("--replace-notes", action="store_true")
    ap.add_argument("--remove-extra", action="store_true")
    ap.add_argument("--restore", metavar="BATCH_ID")
    ap.add_argument("--yes", action="store_true", help="confirm replace/remove/restore")
    a = ap.parse_args(argv)
    app = create_app()
    with app.app_context():
        try:
            if a.restore:
                if not a.yes:
                    print("--restore needs --yes"); return 2
                print(json.dumps(ci.restore_batch(a.restore), indent=2)); return 0
            src, sha = ci.open_source(a.source)
            plan = ci.build_plan(src, sha)
            slugs = [p["slug"] for p in plan["subjects"]] if a.all_subjects else [s for s in (a.subjects or "").split(",") if s]
            if not slugs:
                print(json.dumps(plan, indent=2, ensure_ascii=False))
                print("\nPreview only. Nothing was changed. Pass --subjects or --all-subjects to import.")
                return 0
            if (a.replace_notes or a.remove_extra) and not a.yes:
                print("--replace-notes / --remove-extra need --yes. Nothing was changed."); return 2
            res = ci.apply_import(src, sha, slugs, plan["fingerprint"], a.replace_notes, a.remove_extra)
            print(json.dumps(res, indent=2))
            return 0
        except ci.ContentImportError as e:
            print(f"REFUSED: {e}"); return 1


if __name__ == "__main__":
    sys.exit(main())
