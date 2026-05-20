"""
extract_pdfs.py — Extract text from the 4 AP CA monthly PDFs.

If the PDFs have embedded text  -> uses pdfplumber (fast, accurate).
If they're scanned images       -> falls back to OCR via pytesseract.

Run: `python extract_pdfs.py`
Output: jan2026.txt / feb2026.txt / mar2026.txt / apr2026.txt
        in the same folder as the PDFs.
"""
import os
import sys

PDF_DIR = r"C:\Users\AashrithaNagababu\Downloads\mcq_exam_app_fixed\APBOOKS\Current affairs"


def try_text_extract(src_pdf):
    """Try pdfplumber first. Returns (text, n_pages) or (None, n_pages) if no text found."""
    try:
        import pdfplumber
    except ImportError:
        print("  [!] pdfplumber not installed.  pip install pdfplumber")
        return None, 0

    chunks = []
    n_pages = 0
    total_chars = 0
    with pdfplumber.open(src_pdf) as pdf:
        n_pages = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            t = page.extract_text() or ""
            chunks.append(f"\n\n=== PAGE {i+1} ===\n\n{t}")
            total_chars += len(t.strip())

    if total_chars < 100 * n_pages:
        # Less than ~100 chars per page on average — probably scanned.
        return None, n_pages
    return "".join(chunks), n_pages


def ocr_extract(src_pdf):
    """Fallback: OCR each page as an image. Slower but works for scanned PDFs."""
    try:
        from pdf2image import convert_from_path
        import pytesseract
    except ImportError:
        print("  [!] OCR libraries not installed. Install with:")
        print("      pip install pytesseract pdf2image")
        print("      Also install Tesseract OCR (https://github.com/UB-Mannheim/tesseract/wiki)")
        print("      and Poppler for Windows (https://github.com/oschwartz10612/poppler-windows/releases)")
        print("  After installing Tesseract, also install the Telugu language pack:")
        print("      tesseract --list-langs   (should include 'tel' and 'eng')")
        print("      If 'tel' is missing, download tel.traineddata from")
        print("      https://github.com/tesseract-ocr/tessdata/raw/main/tel.traineddata")
        print("      and place it in C:\\Program Files\\Tesseract-OCR\\tessdata\\")
        return None, 0

    # Tesseract path — adjust if needed.
    tess_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(tess_path):
        pytesseract.pytesseract.tesseract_cmd = tess_path

    # Poppler path — required by pdf2image on Windows.
    # Try common install locations then a broader glob; fall back to PATH.
    import glob
    poppler_candidates = [
        r"C:\Program Files\poppler-26.02.0\Library\bin",
        r"C:\Program Files\poppler-24.08.0\Library\bin",
        r"C:\Program Files\poppler\Library\bin",
        r"C:\poppler\Library\bin",
    ]
    poppler_path = next((p for p in poppler_candidates if os.path.isdir(p)), None)
    if not poppler_path:
        # Broader search
        for pattern in (
            r"C:\Program Files\poppler*\Library\bin",
            r"C:\poppler*\Library\bin",
            r"C:\Users\*\Downloads\poppler*\Library\bin",
        ):
            matches = glob.glob(pattern)
            if matches:
                poppler_path = matches[0]
                break

    print(f"  [ocr] converting PDF to images (~30s/page)...")
    if poppler_path:
        images = convert_from_path(src_pdf, dpi=200, poppler_path=poppler_path)
    else:
        images = convert_from_path(src_pdf, dpi=200)

    n_pages = len(images)
    chunks = []
    for i, img in enumerate(images):
        # Try Telugu+English combined — best for bilingual AP CA digests
        try:
            text = pytesseract.image_to_string(img, lang='tel+eng')
        except pytesseract.TesseractError:
            # tel lang pack missing — fall back to English only
            text = pytesseract.image_to_string(img, lang='eng')
        chunks.append(f"\n\n=== PAGE {i+1} ===\n\n{text}")
        if (i + 1) % 10 == 0:
            print(f"  [ocr] {i+1}/{n_pages} pages done")
    return "".join(chunks), n_pages


def extract_one(src_pdf, dst_txt):
    print(f"\n>> {os.path.basename(src_pdf)}")
    text, n_pages = try_text_extract(src_pdf)
    mode = "text"
    if text is None:
        print(f"  [info] no extractable text (likely scanned) — falling back to OCR for {n_pages} pages")
        text, n_pages = ocr_extract(src_pdf)
        mode = "ocr"
    if text is None:
        return False, 0, "—"

    with open(dst_txt, "w", encoding="utf-8") as out:
        out.write(text)
    size_kb = os.path.getsize(dst_txt) // 1024
    print(f"  [ok] {n_pages} pages, {size_kb} KB, mode={mode}")
    return True, n_pages, mode


def main():
    if not os.path.isdir(PDF_DIR):
        print(f"[!] Directory not found: {PDF_DIR}")
        sys.exit(1)

    targets = ["jan2026.pdf", "feb2026.pdf", "mar2026.pdf", "apr2026.pdf"]
    total_pages = 0
    for fname in targets:
        src = os.path.join(PDF_DIR, fname)
        dst = src.replace(".pdf", ".txt")
        if not os.path.exists(src):
            print(f"\n>> {fname}: missing")
            continue
        ok, n, mode = extract_one(src, dst)
        if ok:
            total_pages += n

    print()
    print(f"Done. {total_pages} pages total across all PDFs.")
    print(f"Output folder: {PDF_DIR}")
    print()
    print("If OCR was used, the .txt files may have minor recognition errors.")
    print("Tell Claude the .txt files are ready and quality looks OK.")


if __name__ == "__main__":
    main()
