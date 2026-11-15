from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content" / "geography" / "india_ap_chapters" / "5"
NOTES = CHAPTER / "Notes.html"
FRAGMENT = CHAPTER / "book_integration_fragment.html"
MARKER = '<p><strong>Migration status:</strong> Existing material preserved below; manual textbook integration and narrative review are pending.</p>'
INTEGRATED_MARKER = 'aria-label="పాఠ్యపుస్తక సమగ్ర పాఠం"'


def main() -> None:
    notes = NOTES.read_text(encoding="utf-8")
    if INTEGRATED_MARKER in notes:
        return
    if MARKER not in notes:
        raise SystemExit("Chapter 5 migration marker was not found; refusing an ambiguous insertion.")
    fragment = FRAGMENT.read_text(encoding="utf-8").strip()
    NOTES.write_text(notes.replace(MARKER, fragment, 1), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
