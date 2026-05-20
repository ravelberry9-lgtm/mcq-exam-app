"""
verify_ocr.py — Sanity-check the OCR setup before running extract_pdfs.py.

Run: `python verify_ocr.py`

Checks:
  1. pytesseract + pdf2image installed
  2. Tesseract binary present at expected path
  3. Tesseract version reports cleanly
  4. Both 'eng' and 'tel' language packs are installed
  5. Poppler is callable (via pdf2image)

If all 5 checks pass -> safe to run extract_pdfs.py.
"""
import os
import sys

OK = "[OK]   "
BAD = "[FAIL] "

problems = []


# ── 1. pytesseract import ──────────────────────────────────────────────
try:
    import pytesseract
    print(OK + "pytesseract is importable")
except ImportError:
    print(BAD + "pytesseract not installed.  Run: pip install pytesseract")
    problems.append("pytesseract")
    sys.exit(1)


# ── 2. pdf2image import ────────────────────────────────────────────────
try:
    from pdf2image import convert_from_path
    print(OK + "pdf2image is importable")
except ImportError:
    print(BAD + "pdf2image not installed.  Run: pip install pdf2image")
    problems.append("pdf2image")


# ── 3. Tesseract binary present ────────────────────────────────────────
tess_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(tess_path):
    pytesseract.pytesseract.tesseract_cmd = tess_path
    print(OK + f"Tesseract binary found at {tess_path}")
else:
    # Try PATH
    try:
        pytesseract.get_tesseract_version()
        print(OK + "Tesseract binary found on PATH")
    except pytesseract.TesseractNotFoundError:
        print(BAD + "Tesseract binary NOT found.")
        print("       Expected at: " + tess_path)
        print("       Install from: https://github.com/UB-Mannheim/tesseract/wiki")
        problems.append("tesseract-binary")


# ── 4. Version check ──────────────────────────────────────────────────
if "tesseract-binary" not in problems:
    try:
        v = pytesseract.get_tesseract_version()
        print(OK + f"Tesseract version: {v}")
    except Exception as e:
        print(BAD + f"Could not get Tesseract version: {e}")
        problems.append("tesseract-version")


# ── 5. Language packs ─────────────────────────────────────────────────
if "tesseract-binary" not in problems:
    try:
        langs = pytesseract.get_languages()
        print(f"       Installed languages: {sorted(langs)}")

        if "eng" in langs:
            print(OK + "English (eng) language pack installed")
        else:
            print(BAD + "English (eng) language pack MISSING")
            problems.append("eng-lang")

        if "tel" in langs:
            print(OK + "Telugu (tel) language pack installed")
        else:
            print(BAD + "Telugu (tel) language pack MISSING")
            print("       Download tel.traineddata from:")
            print("       https://github.com/tesseract-ocr/tessdata/raw/main/tel.traineddata")
            print("       and place it in: C:\\Program Files\\Tesseract-OCR\\tessdata\\")
            problems.append("tel-lang")
    except Exception as e:
        print(BAD + f"Could not list languages: {e}")
        problems.append("lang-list")


# ── 6. Poppler check ──────────────────────────────────────────────────
poppler_found = None

if "pdf2image" not in problems:
    # 6a. Try common paths
    poppler_candidates = [
        r"C:\Program Files\poppler-24.08.0\Library\bin",
        r"C:\Program Files\poppler-25.07.0\Library\bin",
        r"C:\Program Files\poppler-23.11.0\Library\bin",
        r"C:\Program Files\poppler-23.01.0\Library\bin",
        r"C:\poppler-24.08.0\Library\bin",
        r"C:\poppler\Library\bin",
        r"C:\Program Files\poppler\Library\bin",
    ]
    poppler_found = next((p for p in poppler_candidates if os.path.isdir(p)), None)

    # 6b. Search broader if not found in common paths
    if not poppler_found:
        import glob
        search_globs = [
            r"C:\Program Files\poppler*\Library\bin",
            r"C:\Program Files (x86)\poppler*\Library\bin",
            r"C:\poppler*\Library\bin",
            r"C:\Users\*\poppler*\Library\bin",
            r"C:\Users\*\Downloads\poppler*\Library\bin",
            r"C:\tools\poppler*\Library\bin",
        ]
        matches = []
        for pattern in search_globs:
            try:
                matches.extend(glob.glob(pattern))
            except Exception:
                pass
        if matches:
            poppler_found = matches[0]

    # 6c. Check if pdfinfo is on system PATH
    if not poppler_found:
        import shutil
        which_path = shutil.which("pdfinfo") or shutil.which("pdfinfo.exe")
        if which_path:
            poppler_found = os.path.dirname(which_path)

    # 6d. Active test — try calling pdfinfo
    if poppler_found:
        print(OK + f"Poppler bin folder found at {poppler_found}")
        # Try a real call
        try:
            import subprocess
            exe = os.path.join(poppler_found, "pdfinfo.exe")
            if not os.path.exists(exe):
                exe = "pdfinfo"  # fall back to PATH lookup
            result = subprocess.run([exe, "-v"], capture_output=True, text=True, timeout=10)
            ver_out = (result.stderr or result.stdout or "").strip().splitlines()
            ver_line = next((l for l in ver_out if "pdfinfo" in l.lower() or "version" in l.lower()), ver_out[0] if ver_out else "")
            print(OK + f"Poppler executable verified: {ver_line.strip()}")
        except Exception as e:
            print(f"[WARN] Found Poppler folder but couldn't run pdfinfo: {e}")
            problems.append("poppler-broken")
    else:
        print(BAD + "Poppler NOT found anywhere.")
        print("       Searched: C:\\Program Files\\poppler*, C:\\poppler*, C:\\Users\\*\\Downloads\\poppler*")
        print("       Install from: https://github.com/oschwartz10612/poppler-windows/releases")
        print("       Download Release-*.zip, extract to: C:\\Program Files\\poppler-24.08.0\\")
        problems.append("poppler-missing")


# ── Summary ───────────────────────────────────────────────────────────
print()
print("=" * 60)
if problems:
    print(f"FAILED — {len(problems)} issue(s): {', '.join(problems)}")
    print()
    print("Fix the issues above, then re-run this script.")
    sys.exit(1)
else:
    print("ALL CHECKS PASSED — safe to run: python extract_pdfs.py")
    print()
    print("Note: OCR is slow (~30-60 sec per page). 4 PDFs of ~50 pages each")
    print("will take roughly 30-60 minutes total. The extract script prints")
    print("progress every 10 pages so you'll see it's working.")
    sys.exit(0)
