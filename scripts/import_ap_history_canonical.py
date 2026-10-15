"""Validate and copy the approved AP History HTML corpus; never touches a database."""
from __future__ import annotations
import argparse, ast, csv, hashlib, json, shutil
from pathlib import Path

EXPECTED = "48BCBB69D4F01ACE966F418CC18BC3C8AB5F20CE57A2A1552B59E7A35C596447"
ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def slugs():
    tree = ast.parse((ROOT / "app/services/ap_canonical.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "CHAPTERS" for t in node.targets):
            return {int(row[1]): row[2] for row in ast.literal_eval(node.value)}
    raise RuntimeError("Canonical taxonomy missing")


def provenance(path):
    path = Path(path)
    try:
        marker = path.parts.index("AP_History_Working")
        return "/".join(path.parts[marker + 1:])
    except ValueError:
        return path.name


def run(package, output, check=False):
    manifest = package / "CANONICAL_CHAPTER_MANIFEST.csv"
    if sha(manifest) != EXPECTED:
        raise RuntimeError("Canonical manifest hash mismatch")
    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        source = list(csv.DictReader(handle))
    if len(source) != 31 or {int(r["Chapter"]) for r in source} != set(range(1, 32)):
        raise RuntimeError("Expected Chapters 1-31 exactly once")
    chapter_slugs, rows = slugs(), []
    for r in source:
        number, html = int(r["Chapter"]), Path(r["HtmlPath"])
        if r["PublicationStatus"] != "PUBLICATION APPROVED" or not html.is_file() or sha(html) != r["HtmlSHA256"]:
            raise RuntimeError(f"Chapter {number} source verification failed")
        acceptance = Path(r["AuthoritativeAcceptanceReport"])
        if not acceptance.is_file():
            raise RuntimeError(f"Chapter {number} acceptance report missing")
        filename = f"chapter-{number:02d}.html"
        te, en = int(r["FoundationTeluguParagraphs"]) + int(r["Group1TeluguParagraphs"]), int(r["FoundationEnglishParagraphs"]) + int(r["Group1EnglishParagraphs"])
        rows.append({"chapter": number, "unit": int(r["Unit"]), "slug": chapter_slugs[number], "title": r["Title"], "status": r["PublicationStatus"], "html_file": filename, "html_sha256": r["HtmlSHA256"], "manuscript_sha256": r["ManuscriptSHA256"], "foundation_te": int(r["FoundationTeluguParagraphs"]), "foundation_en": int(r["FoundationEnglishParagraphs"]), "group1_te": int(r["Group1TeluguParagraphs"]), "group1_en": int(r["Group1EnglishParagraphs"]), "source_coverage": r["SourceCoverageStatus"], "limitation": r["RemainingLimitation"], "acceptance_report": provenance(acceptance), "languages": (["te"] if te else []) + (["en"] if en else []), "separate_group1": bool(int(r["Group1TeluguParagraphs"]) or int(r["Group1EnglishParagraphs"]))})
        if not check:
            output.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(html, output / filename)
    if not check:
        (output / "index.json").write_text(json.dumps({"format": "ap-history-canonical-html-v1", "manifest_sha256": EXPECTED, "chapter_count": 31, "chapters": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if any(sha(output / r["html_file"]) != r["html_sha256"] for r in rows):
            raise RuntimeError("Post-copy verification failed")
    print(f"validated={len(rows)} manifest={EXPECTED} mode={'check' if check else 'local-import'}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--package", type=Path, required=True); p.add_argument("--output", type=Path, default=ROOT / "content/ap_history_canonical"); p.add_argument("--check", action="store_true"); a = p.parse_args()
    run(a.package.resolve(), a.output.resolve(), a.check)
