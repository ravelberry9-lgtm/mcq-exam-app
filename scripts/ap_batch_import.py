"""STRICT DRY-RUN checker for AP History MCQ batches. There is no apply mode: this tool never writes to any database.

    python scripts/ap_batch_import.py package <dir under 05_claude_import> [--db <sqlite file, read-only>] [--json out.json]
    python scripts/ap_batch_import.py drafts  <file.md> [<file.md> ...]     # report only; drafts are never importable

Exit status: 0 only when a package under 05_claude_import passes every check ("importable"); drafts always exit 2.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services import ap_batch_import as b   # noqa: E402


def render(r):
    d = r.to_dict()
    out = [f"# Dry-run report ({d['mode']})", "", f"Path: {d['path']}", f"Records read: {d['records']}",
           f"Importable: **{'YES' if d['importable'] else 'NO'}**  (dry-run only; nothing was written anywhere)", "",
           f"Errors: {len(d['errors'])}   Warnings: {len(d['warnings'])}", ""]
    for kind in ("errors", "warnings"):
        codes = r.codes(kind)
        if codes:
            out += [f"## {kind.capitalize()} by code", ""] + [f"- `{c}`: {n}" for c, n in sorted(codes.items())] + [""]
    out += ["## Info", "", "```json", json.dumps(d["info"], ensure_ascii=False, indent=1, default=str), "```", ""]
    if d["errors"]:
        out += ["## First errors", ""] + [f"- {e['id']} `{e['code']}`: {e['message']}" for e in d["errors"][:25]] + [""]
    if d["warnings"]:
        out += ["## First warnings", ""] + [f"- {e['id']} `{e['code']}`: {e['message']}" for e in d["warnings"][:25]] + [""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("package"); p1.add_argument("path"); p1.add_argument("--db"); p1.add_argument("--json")
    p2 = sub.add_parser("drafts"); p2.add_argument("paths", nargs="+"); p2.add_argument("--json")
    args = ap.parse_args()
    if args.cmd == "package":
        rpt = b.validate_package(args.path, db_path=args.db)
    else:
        rpt, _ = b.validate_draft_files([Path(p) for p in args.paths])
    print(render(rpt))
    if args.json:
        Path(args.json).write_text(json.dumps(rpt.to_dict(), ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    sys.exit(0 if rpt.importable else 2)


if __name__ == "__main__":
    main()
