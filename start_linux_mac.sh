#!/bin/bash
echo ""
echo "============================================"
echo "  MCQ Exam App - Starting..."
echo "============================================"
echo ""

# Install dependencies
echo "Checking dependencies..."
pip3 install flask beautifulsoup4 pdfplumber --quiet 2>/dev/null || \
pip install flask beautifulsoup4 pdfplumber --quiet 2>/dev/null

echo ""
echo "Starting server..."
echo ""
python3 app.py || python app.py
