#!/usr/bin/env python3
"""Preview (default) or apply a prepared MCQ chapter file.

    python scripts/import_mcq_batch.py path/to/AP_History_U1_C01_Import_Ready.jsonl            # preview only
    python scripts/import_mcq_batch.py path/to/file.jsonl --apply                               # add the new questions

Add-only; never edits or deletes existing questions. Reads DATABASE_URL like the app does.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402
from app.services import mcq_import  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv)
    app = create_app()
    with app.app_context():
        try:
            rep = mcq_import.run(a.file, apply=a.apply)
        except mcq_import.McqImportError as e:
            print(f"REFUSED: {e}")
            return 1
        print(json.dumps(rep, indent=2, ensure_ascii=False))
        if not a.apply:
            print("\nPreview only. Nothing was changed. Pass --apply to import.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
