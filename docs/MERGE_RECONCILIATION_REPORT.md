# Merge report: secured branch + origin/main (fetched 2026-10-04)

* Ours: `design-system-stage-1-2` @ `6516227` (Learn journey, security, Alembic). Theirs: `origin/main` @ `ce2343c` (57 commits ahead of local `main`; 29 of them are new since the 2026-05-30 snapshot ea34696: the AP History notes feature).
* Merge base `2244842`. Done in an independent clone; the original repository, `main`, locks, `static/`, `data/` and Railway were not touched.

## Release blocker: kept out
`origin/main`'s `app/__init__.py` adds `_patch_schema()` (executes `DROP TABLE questions CASCADE` and `DROP TABLE user_question_state CASCADE` at startup when `questions` lacks `subject_id/chapter_id/source_type/options_en`) and `db.create_all()`. Resolution: this file is taken **entirely from the secured branch**. A new test (`test_no_destructive_or_implicit_schema_code_anywhere_in_the_app`) fails if `DROP TABLE`, `drop_all`, `create_all` or `_patch_schema` appears anywhere in `app/` or `wsgi.py`; it flags origin's file.

## The 16 conflicted files

| File | Hunks | Resolution | Why |
|---|---|---|---|
| `app/__init__.py` | 1 (+ auto-merged destructive code) | **ours** (whole file) | origin's only change is the destructive startup patch; ours keeps the blueprint, security headers, note sanitiser, production config check |
| `app/routes/admin.py` | 1 | ours for the import line; origin's new `/parse-ap-history` and `/load-content` changes merged | `hmac`/`time` needed by login throttle; blueprint-wide CSRF covers the new POST routes |
| `app/templates/notes/reader.html` | 1 | **ours** | origin's `{{ body | safe }}` is the stored-XSS bug; ours uses the `note_html` sanitiser. Origin's other fixes (restored `</script>` and `endblock`, `&middot;`) are kept: auto-merged |
| `app/templates/subjects.html` | 2 | ours | origin's copy has double-encoded Telugu (mojibake) |
| `app/templates/admin/parse_ap_history.html` | 5 | ours | origin's copy is mojibake (`â¶`, `â³`) and lacks the CSRF token and header |
| `app/templates/admin/load_content.html` | 2 | ours | identical except CSRF token/header, which origin lacks |
| `app/templates/admin/seed.html` | 2 | **both**: origin's version + CSRF | origin adds fetch error handling; CSRF re-applied |
| `app/templates/exam_session/results.html` | 6 | **theirs** | the branch's Retry was `<a formmethod="post">`: an anchor cannot POST and the start route is POST-only, so it never worked. Origin links to the exam page, where the start form is. Rest is formatting |
| `app/templates/exam_session/take.html` | 11 | ours | origin strips comments and the `aria-checked` updates; behaviour otherwise equal |
| `app/templates/study_plan/dashboard.html` | 3 | ours | origin only strips comments / reflows |
| `app/templates/subject_detail.html` | 2 | ours | formatting and comments only |
| `app/routes/exam_session.py` | 5 | ours | origin only strips comments |
| `app/routes/study_plan.py` | 4 | ours | origin only strips comments |
| `tests/test_exam_session.py` | 12 | ours | origin's fixtures replaced Telugu text with Devanagari (Hindi) script |
| `tests/test_study_plan.py` | 5 | ours | same Devanagari substitution |
| `SESSION_REPORT.md` | 1 | ours; origin's copy kept verbatim as `docs/SESSION_REPORT.origin-main-2026-05-31.md` | nothing lost |

## Merged from origin without conflict (reviewed)
AP History feature: `scripts/load_content.py`, `scripts/fix_notes.py`, `scripts/parse_ap_history_notes.py`, `static/ap_history_notes.css`, 12 AP History chapter HTML files, `data/content.db.gz` (225 AP History sections), `beautifulsoup4` in requirements, `base.html` `head_extra` block, `public.py` duplicate-route removal, `chapter_list.html` entity fix, `app.css`.

## Flagged for your decision (not changed)
1. `/admin/load-content` runs `Note.query.delete()` (all notes) and then reloads from `content.db`; `parse_ap_history_notes.py` deletes the AP History chapters and notes. Notes edited by hand in the admin editor are lost when either runs. Both are PIN + CSRF protected and operator-triggered, not startup. Consider a confirmation step or a "replace only this subject" mode before using them on production.
2. `scripts/scripts/scripts/scripts/load_content.py` is a stray duplicate created by a web upload (kept; delete when convenient).
3. `data/content.db.gz` (3.3 MB binary) is committed on origin.

## Verification (merged tree)
* Full suite: see commit message. Includes security, Alembic and the new guards.
* Real content (copy of `data/content.db`): migrations upgrade to head with `alembic check` clean; 782 requests across all 194 chapters (legacy reader, Learn topic/notes/practice), hub, subjects, settings, healthz, admin login: 0 non-200; 0 reader pages containing script/handler/iframe/style.
