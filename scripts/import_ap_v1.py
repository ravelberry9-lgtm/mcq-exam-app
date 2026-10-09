#!/usr/bin/env python3
"""Native ap-history-import-v1 import: package notes first, then questions. Preview is the default; nothing is written
without --apply AND --approval-ref (a reference to the human import approval). Add-only; never touches existing rows.

    python scripts/import_ap_v1.py notes     <package dir>                       # preview the notes collection
    python scripts/import_ap_v1.py questions <package dir>                       # preview the questions
    python scripts/import_ap_v1.py notes     <package dir> --apply --approval-ref "<ref>"
    python scripts/import_ap_v1.py questions <package dir> --apply --approval-ref "<ref>" [--allow-overlaps]

The package must live under a folder named 05_claude_import. Reads DATABASE_URL like the app does.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402
from app.services import ap_v1_import, expanded_notes  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("what", choices=("notes", "questions"))
    ap.add_argument("package")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--approval-ref")
    ap.add_argument("--allow-overlaps", action="store_true")
    a = ap.parse_args(argv)
    app = create_app()
    with app.app_context():
        try:
            if a.what == "notes":
                if a.apply and not (a.approval_ref or "").strip():
                    print("REFUSED: --apply needs --approval-ref"); return 1
                rep = expanded_notes.load_notes(a.package, apply=a.apply)
            else:
                rep = ap_v1_import.run(a.package, apply=a.apply, approval_ref=a.approval_ref, allow_overlaps=a.allow_overlaps)
        except (ap_v1_import.V1ImportError, expanded_notes.NotesError) as e:
            print(f"REFUSED: {e}")
            return 1
        print(json.dumps(rep, indent=2, ensure_ascii=False))
        if not a.apply:
            print("\nPreview only. Nothing was changed.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
