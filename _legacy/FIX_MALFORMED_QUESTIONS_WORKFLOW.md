# Fix Malformed MCQ Questions - Complete Workflow

## Problem Summary
A malformed MCQ exists in the database:
- **Question (corrupted)**: "IBM ఆడ్డ ధర?" (Gibberish Telugu)
- **Options**: Agricultural prices (₹15/క.ఎ., ₹20/క.ఎ., ₹30/క.ఎ., ₹50/క.ఎ.)
- **Expected**: Question about IBM Quantum Valley in Andhra Pradesh with tech-related options
- **Root Cause**: Data corruption during database import or question translation

---

## Step-by-Step Fix Process

### STEP 1: Audit & Identify Corrupted Data
```bash
cd /path/to/mcq_app

# Run audit script to find all malformed questions
python3 audit_malformed_questions.py
```

**Expected Output**: Will show the corrupted question and similar issues.

---

### STEP 2: Delete Corrupted MCQ from Database

#### Option A: Via SQLite CLI
```bash
sqlite3 questions.db
```

```sql
-- Find the corrupted question
SELECT id, question_te, option_a, option_b FROM mcqs 
WHERE question_te LIKE '%IBM ఆడ్డ ధర%' 
OR (question_te LIKE '%IBM%' AND option_a LIKE '%₹%' AND option_a LIKE '%క.ఎ.%');

-- Delete it (once confirmed it's the right one)
DELETE FROM mcqs 
WHERE id = <ID_FROM_ABOVE>;

-- Verify deletion
SELECT COUNT(*) FROM mcqs WHERE question_te LIKE '%IBM ఆడ్డ ధర%';

.quit
```

#### Option B: Via Python Script
```python
import sqlite3

conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Find
cursor.execute("""
    SELECT id, question_te FROM mcqs 
    WHERE question_te LIKE '%IBM ఆడ్డ ధర%'
""")
results = cursor.fetchall()

if results:
    for q_id, q_text in results:
        print(f"Found corrupted MCQ ID {q_id}: {q_text}")
        # Delete
        cursor.execute("DELETE FROM mcqs WHERE id = ?", (q_id,))
        print(f"Deleted MCQ ID {q_id}")

conn.commit()
conn.close()
```

---

### STEP 3: Re-seed Correct IBM Quantum Questions

The correct IBM Quantum MCQs are in:
- `seed_ap_ca_div3.py` (4 questions)
- `seed_ap_ca_div4.py` (5 questions)

#### Method A: Auto-seed via Flask app
```bash
# Start the Flask app
python3 app.py

# The app's startup process will:
# 1. Call _auto_seed_ap_ca_divisions()
# 2. Which runs all seed_ap_ca_div*.py files
# 3. Which includes div3.py and div4.py with IBM Quantum MCQs

# Verify questions seeded by checking database
sqlite3 questions.db "SELECT COUNT(*) FROM mcqs WHERE question_te LIKE '%క్వాంటం%';"
```

#### Method B: Manual seed
```bash
python3 seed_ap_ca_div3.py
python3 seed_ap_ca_div4.py
```

---

### STEP 4: Verify Questions in Database

```bash
sqlite3 questions.db
```

```sql
-- Count IBM Quantum questions
SELECT COUNT(*) as quantum_mcqs FROM mcqs 
WHERE question_te LIKE '%క్వాంటం%' OR question_te LIKE '%Quantum%';

-- List all IBM Quantum MCQs (should be 9 total)
SELECT id, question_te, option_a FROM mcqs 
WHERE question_te LIKE '%క్వాంటం%' 
ORDER BY id;

-- Expected: 
-- "అమరావతి క్వాంటం వ్యాలీ ఆలోచన ఏ సంవత్సరం మొదలైంది?"
-- "అమరావతి క్వాంటం వ్యాలీ వైశాల్యం ఎంత?"
-- "అమరావతి క్వాంటం వ్యాలీలో క్వాంటం హార్డ్‌వేర్ సరఫరా చేస్తున్న ముఖ్య కంపెనీ ఏది?"
-- (and 6 more from div4.py)

-- Verify NO corrupted questions remain
SELECT COUNT(*) FROM mcqs WHERE question_te LIKE '%ఆడ్డ ధర%';
-- Expected: 0

.quit
```

---

### STEP 5: Test in Web UI

1. **Start the app**:
   ```bash
   python3 app.py
   ```

2. **Navigate to**: `http://localhost:5000/ap-ca-practice`

3. **Search for IBM Quantum questions**:
   - Look for questions with "క్వాంటం వ్యాలీ" or "Quantum Valley"
   - Verify options are correct (companies, dates, technical specs)
   - Confirm NO agricultural price options appear

4. **Expected questions to see**:
   - "అమరావతి క్వాంటం వ్యాలీ ఆలోచన ఏ సంవత్సరం మొదలైంది?"
   - "అమరావతి క్వాంటం వ్యాలీ వైశాల్యం ఎంత?"
   - "అమరావతి క్వాంటం వ్యాలీలో క్వాంటం హార్డ్‌వేర్ సరఫరా చేస్తున్న ముఖ్య కంపెనీ ఏది?"
   - "అమరావతి క్వాంటం వ్యాలీ ఆలోచన ప్రారంభం నుండి క్వాంటం కంప్యూటర్ల అంకితం వరకు ఎంత సమయం పట్టింది?"
   - "అమరావతి క్వాంటం వ్యాలీ ఫౌండేషన్ స్టోన్ ఏ తేదీన వేశారు?"
   - "అమరావతి క్వాంటం వ్యాలీలో IBM తో కలిసి పని చేస్తున్న ముఖ్య భారతీయ IT కంపెనీ ఏది?"
   - "AP Quantum Computing Policy ఏ నెలలో విడుదలైంది?"
   - "అమరావతి క్వాంటం వ్యాలీలో కంపెనీలు చేరిన నెల ఏది?"
   - "అమరావతి క్వాంటం వ్యాలీ గురించి ఏది తప్పు?"

---

### STEP 6: Audit for Similar Issues

Run comprehensive audit to find other malformed questions:

```bash
python3 audit_malformed_questions.py

# This will check for:
# ✓ Topic-option mismatches (e.g., Quantum question with agricultural options)
# ✓ Corrupted Telugu text
# ✓ Incomplete question text
# ✓ Mixed English-Telugu gibberish
```

---

## Complete SQL Cleanup Script

Save as `cleanup_malformed_mcqs.sql`:

```sql
-- ============================================================
-- CLEANUP SCRIPT FOR MALFORMED MCQs
-- Run: sqlite3 questions.db < cleanup_malformed_mcqs.sql
-- ============================================================

-- 1. BACKUP (optional but recommended)
.output mcqs_backup.sql
.dump mcqs
.output stdout

-- 2. DELETE CORRUPTED QUESTIONS
DELETE FROM mcqs 
WHERE question_te LIKE '%IBM ఆడ్డ ధర%' 
   OR question_te LIKE '%addhe dhara%'
   OR question_te LIKE '%ఆడ్డ.*ధర%';

-- 3. DELETE OTHER SUSPICIOUS PATTERNS
DELETE FROM mcqs 
WHERE question_te REGEXP '[ఀ-్]\s*$'  -- Incomplete Telugu
   OR length(question_te) < 5;           -- Too short

-- 4. VERIFY CLEANUP
SELECT 'Corrupted MCQs remaining:' as check_type;
SELECT COUNT(*) FROM mcqs WHERE question_te LIKE '%IBM ఆడ్డ ధర%';
SELECT COUNT(*) FROM mcqs WHERE question_te LIKE '%addhe%';

-- 5. VERIFY CORRECT QUESTIONS EXIST
SELECT 'Quantum Valley MCQs in database:' as check_type;
SELECT COUNT(*) FROM mcqs WHERE question_te LIKE '%క్వాంటం%';

-- Expected: 9 or more Quantum Valley MCQs after re-seeding
```

**Run cleanup**:
```bash
sqlite3 questions.db < cleanup_malformed_mcqs.sql
```

---

## Verification Checklist

After completing all steps:

- [ ] Corrupted question "IBM ఆడ్డ ధర?" deleted from database
- [ ] 9 IBM Quantum MCQs present and correct
- [ ] All options match question topics (no agricultural prices for quantum questions)
- [ ] Telugu rendering works correctly in web UI
- [ ] No gibberish or corrupted text visible
- [ ] Audit script returns 0 malformed questions
- [ ] App starts without errors
- [ ] Web UI displays all questions properly

---

## Common Issues & Solutions

### Issue 1: Database Still Shows Corrupted Question After Delete
**Solution**: 
```bash
# Force delete and commit
sqlite3 questions.db << EOF
DELETE FROM mcqs WHERE question_te LIKE '%IBM ఆడ్డ ధర%';
VACUUM;
EOF
```

### Issue 2: IBM Quantum Questions Not Appearing After Re-seed
**Solution**:
```bash
# Check if seed files ran successfully
python3 seed_ap_ca_div3.py --verbose
python3 seed_ap_ca_div4.py --verbose

# Manually insert if needed - see IBM_QUANTUM_MCQ_FIX.md for exact MCQ format
```

### Issue 3: Telugu Not Rendering Correctly in Web UI
**Solution**:
```bash
# Check database encoding
sqlite3 questions.db "PRAGMA encoding;"
# Expected: UTF-8

# Check app.py encoding settings
grep -n "utf-8\|UTF-8\|encoding" app.py
```

### Issue 4: Audit Still Finding Malformed Questions
**Solution**:
```bash
# Update audit patterns if new corruption types found
# Edit audit_malformed_questions.py patterns section
# Re-run audit with debug output
python3 audit_malformed_questions.py --verbose
```

---

## Timeline

| Step | Task | Time | Status |
|------|------|------|--------|
| 1 | Run audit | 2 min | ⏳ |
| 2 | Delete corrupted MCQ | 1 min | ⏳ |
| 3 | Re-seed correct MCQs | 2 min | ⏳ |
| 4 | Verify in database | 2 min | ⏳ |
| 5 | Test in web UI | 3 min | ⏳ |
| 6 | Run comprehensive audit | 2 min | ⏳ |
| **TOTAL** | | **12 minutes** | ⏳ |

---

## Need Help?

If you encounter issues:
1. Check `IBM_QUANTUM_MCQ_FIX.md` for correct MCQ formats
2. Run `audit_malformed_questions.py` to identify all issues
3. Check app logs: `tail -f app.log`
4. Verify database integrity: `sqlite3 questions.db "PRAGMA integrity_check;"`
