@echo off
title MCQ Exam App
echo.
echo ============================================
echo   MCQ Exam App - Starting...
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing/checking dependencies...
pip install flask beautifulsoup4 pdfplumber --quiet --break-system-packages 2>nul
pip install flask beautifulsoup4 pdfplumber --quiet 2>nul

echo.
echo Starting server...
echo.
python app.py

pause
