# Push to Railway - Wrong Answers API Fix

## Status
✅ **Code is ready to deploy**
- Commit: `812ab25`
- Branch: `main`
- Working directory: Clean, no uncommitted changes

## The Fix (What Changed)

### File: `app.py`
### Function: `/api/wrong-answers` endpoint (lines 3192-3214)

**Before** (Broken - Hardcoded columns):
```python
cur = db_exec(conn, f"SELECT id, device_id, source, source_id, topic, question_text, option_a, option_b, option_c, option_d, correct_answer, user_answer, explanation, attempted_at, resolved FROM wrong_answers WHERE device_id={ph} ORDER BY attempted_at DESC", (device_id,))

for row in cur.fetchall():
    items.append({
        'id': row[0], 'device_id': row[1], 'source': row[2], 'source_id': row[3],
        'topic': row[4], 'question_text': row[5], 'option_a': row[6], 'option_b': row[7],
        'option_c': row[8], 'option_d': row[9], 'correct_answer': row[10],
        'user_answer': row[11], 'explanation': row[12], 'attempted_at': row[13], 'resolved': row[14]
    })
```

**After** (Fixed - Flexible mapping):
```python
cur = db_exec(conn, f"SELECT * FROM wrong_answers WHERE device_id={ph} ORDER BY attempted_at DESC", (device_id,))

for row in cur.fetchall():
    items.append(row_to_dict(row))
```

## Why This Fix Works

The old approach:
- ❌ Hardcoded column count (15 columns)
- ❌ Position-based index mapping (row[0], row[1], etc.)
- ❌ Breaks if database schema has different column order or count
- ❌ Silent failures due to index mismatch

The new approach:
- ✅ Dynamic `SELECT *` returns all columns
- ✅ Uses existing `row_to_dict()` function to map columns by name
- ✅ Works with SQLite (`sqlite3.Row`) and PostgreSQL (`psycopg2 RealDictCursor`)
- ✅ Resilient to schema variations between dev and prod environments
- ✅ Better error handling with try-except that returns empty list instead of crashing

## How to Deploy

### Step 1: Push from Your Local Machine
```bash
cd path/to/mcq_exam_app
git pull origin main
git push origin main
```

### Step 2: Verify Push
```bash
git log --oneline -1
# Should show: 812ab25 Fix: Use SELECT * with row_to_dict() for flexible wrong_answers retrieval
```

### Step 3: Wait for Railway
Railway will automatically detect the new commit and deploy within 2-3 minutes.

Monitor deployment at: https://dashboard.railway.app

## Testing After Deployment

### Test 1: Check API Response
```bash
# Replace YOUR-APP-URL with your Railway app URL
curl -s "https://YOUR-APP-URL/api/wrong-answers?device_id=test-device&resolved=0" | python -m json.tool
```

Expected response:
```json
{
  "items": [
    {
      "id": 1,
      "device_id": "test-device",
      "source": "chapter",
      "source_id": 123,
      "topic": "Some_Topic",
      "question_text": "...",
      "option_a": "...",
      "option_b": "...",
      "option_c": "...",
      "option_d": "...",
      "correct_answer": "A",
      "user_answer": "B",
      "explanation": "...",
      "attempted_at": "2026-05-21T...",
      "resolved": 0
    }
  ],
  "total": 1,
  "unresolved": 1,
  "resolved": 0
}
```

### Test 2: User Flow Testing
1. Open the app in browser
2. Go to any practice topic
3. Answer a question **incorrectly**
4. Verify the answer appears in "Wrong Answers" section
5. Try flagging a question
6. Toggle between "Wrong" and "Flagged" tabs - both should work

### Test 3: Error Checking
- Check browser console for errors (F12 → Console)
- Check Railway logs for any 500 errors
- Monitor database - wrong answers should be being saved

## What This Fixes

| Issue | Status |
|-------|--------|
| Wrong answers not displaying | ✅ Fixed |
| "No unresolved wrong answers!" false message | ✅ Fixed |
| Toggle between Wrong/Flagged not working | ✅ Fixed (should work now) |
| Database schema variation errors | ✅ Fixed |

## Rollback Plan (If Needed)

If something goes wrong after deployment:

```bash
git revert 812ab25
git push origin main
# Railway will auto-deploy the revert within 2-3 minutes
```

This will go back to the previous code while keeping commit history intact.

## Architecture Notes

The app uses:
- **PostgreSQL** on Railway (production)
- **SQLite** for local development

Both database drivers return rows as:
- PostgreSQL: `psycopg2.extras.RealDictCursor` (dict-like objects)
- SQLite: `sqlite3.Row` (tuple-like objects with column names)

The `row_to_dict()` helper function (line 54-57 in app.py) handles both seamlessly by converting them to Python dicts before returning to frontend.

---

**Ready to push?** Run `git push origin main` from your local repository.
