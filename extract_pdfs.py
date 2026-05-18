"""
extract_pdfs.py — One-shot helper to extract text from the 4 AP CA monthly PDFs
so Claude can read them without needing pdftoppm in its sandbox.

Run from anywhere: `python extract_pdfs.py`

Output: jan2026.txt / feb2026.txt / mar2026.txt / apr2026.txt
        in the same folder as the PDFs.
"""
import os
import sys

PDF_DIR = r"C:\Users\AashrithaNagababu\Downloads\mcq_exam_app_fixed\APBOOKS\Current affairs"

try:
    import pdfplumber
except ImportError:
    print("[!] pdfplumber not installed. Run:")
    print("    pip install pdfplumber")
    sys.exit(1)


def extract(src_pdf, dst_txt):
    with pdfplumber.open(src_pdf) as pdf:
        n_pages = len(pdf.pages)
        with open(dst_txt, "w", encoding="utf-8") as out:
            for i, page in enumerate(pdf.pages):
                out.write(f"\n\n=== PAGE {i+1} ===\n\n")
                out.write(page.extract_text() or "")
    return n_pages


def main():
    if not os.path.isdir(PDF_DIR):
        print(f"[!] Directory not found: {PDF_DIR}")
        sys.exit(1)

    targets = ["jan2026.pdf", "feb2026.pdf", "mar2026.pdf", "apr2026.pdf"]
    total = 0
    for fname in targets:
        src = os.path.join(PDF_DIR, fname)
        dst = src.replace(".pdf", ".txt")
        if not os.path.exists(src):
            print(f"  [skip] missing: {fname}")
            continue
        try:
            pages = extract(src, dst)
            size_kb = os.path.getsize(dst) // 1024
            print(f"  [ok]   {fname} -> {os.path.basename(dst)}  ({pages} pages, {size_kb} KB)")
            total += pages
        except Exception as e:
            print(f"  [err]  {fname}: {e}")

    print()
    print(f"Done. Total {total} pages extracted.")
    print(f"Output folder: {PDF_DIR}")
    print()
    print("Next step: tell Claude the .txt files are ready.")


if __name__ == "__main__":
    main()
