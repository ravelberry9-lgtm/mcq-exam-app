"""Seed the canonical AP History structure (5 units, 31 core chapters, 4 supplementary reference chapters).

    python scripts/seed_ap_canonical.py                 # PREVIEW only (default): prints what would be added
    python scripts/seed_ap_canonical.py --apply         # insert the missing units/chapters (never updates or deletes)
    python scripts/seed_ap_canonical.py --apply --with-subtopics   # also insert subtopics + microtopics of ap-history-taxonomy-v1

Requires Alembic migrations d4e5f6a7b8c9 and e5f6a7b8c9d0 to be applied first. Idempotent. Touches no notes, questions or source chapters.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app                                   # noqa: E402
from app.services import ap_canonical, ap_canonical_taxonomy  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write the missing rows (default is preview only)")
    ap.add_argument("--with-subtopics", action="store_true", help="also seed the learner-facing subtopics and microtopics of the taxonomy (needs the chapters first)")
    args = ap.parse_args()
    app = create_app()
    with app.app_context():
        rep = ap_canonical.seed(apply=args.apply)
        print(("APPLIED" if args.apply else "PREVIEW (nothing written)"), rep)
        if args.with_subtopics:
            if not args.apply:
                print("subtopics: preview skipped (chapters must exist first); re-run with --apply")
            else:
                print(f"taxonomy {ap_canonical_taxonomy.TAXONOMY_VERSION}:", ap_canonical.seed_taxonomy())


if __name__ == "__main__":
    main()
