#!/usr/bin/env python3
"""Command-line front end for importing the AP History HTML chapters (static/notes/AP_History/Chapters/).

    python scripts/parse_ap_history_notes.py                   # preview only: prints the plan, changes nothing
    python scripts/parse_ap_history_notes.py --apply           # add missing chapters/sections; keeps everything that exists
    python scripts/parse_ap_history_notes.py --apply --replace-notes --yes    # also replace sections that differ (backed up)
    python scripts/parse_ap_history_notes.py --apply --remove-extra --yes     # also remove live-only sections (backed up)
    python scripts/parse_ap_history_notes.py --restore BATCH_ID --yes

This replaces the old behaviour, which deleted every ap_history chapter and note before re-inserting. Same service as the
admin page (app/services/content_import.py): one transaction, per-subject fingerprint, backup in note_backups, restorable.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402
from app.services import ap_history_parse, content_import as ci  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--notes-dir")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--replace-notes", action="store_true")
    ap.add_argument("--remove-extra", action="store_true")
    ap.add_argument("--restore", metavar="BATCH_ID")
    ap.add_argument("--yes", action="store_true")
    a = ap.parse_args(argv)
    app = create_app()
    with app.app_context():
        try:
            if a.restore:
                if not a.yes:
                    print("--restore needs --yes"); return 2
                print(json.dumps(ci.restore_batch(a.restore), indent=2)); return 0
            with ap_history_parse.build_source(a.notes_dir) as src:
                plan = ci.build_plan(src)
                if not a.apply:
                    print(json.dumps(plan, indent=2, ensure_ascii=False))
                    print("\nPreview only. Nothing was changed. Pass --apply to import.")
                    return 0
                if (a.replace_notes or a.remove_extra) and not a.yes:
                    print("--replace-notes / --remove-extra need --yes. Nothing was changed."); return 2
                res = ci.apply_import(src, [ap_history_parse.SUBJECT_SLUG], plan["fingerprints"], a.replace_notes, a.remove_extra)
                print(json.dumps(res, indent=2)); return 0
        except ci.ContentImportError as e:
            print(f"REFUSED: {e}"); return 1


if __name__ == "__main__":
    sys.exit(main())
