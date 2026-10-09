# Native `ap-history-import-v1` import (notes collection + questions)

Branch `feature/ap-history-v1-native`. Tested only on isolated local databases. **Nothing has been run against production** (the only Railway environment). Any production change needs separate approval; see `AP_HISTORY_C1_PRODUCTION_CHANGE_PLAN.md`.

## Order of operations (any database)
1. Alembic to head (`b8c9d0e1f2a3` adds `expanded_notes` and `expanded_note_app_map`; additive).
2. Canonical structure seeded: `python scripts/seed_ap_canonical.py --apply --with-subtopics`.
3. Notes: `python scripts/import_ap_v1.py notes <05_claude_import/package>` (preview) then `--apply --approval-ref "<ref>"`.
4. Questions: `python scripts/import_ap_v1.py questions <package>` (preview) then `--apply --approval-ref "<ref>"`.
Preview is the default. Apply is add-only, single transaction, idempotent. Questions refuse to apply while any question names an expanded-note anchor that is not loaded, or while an overlap with an existing question is unreconciled (`--allow-overlaps` after a human decision). Nothing is deleted or updated.

## Canonical mapping
`chapter_slug` / `subtopic_slug` / `secondary_chapters` / `microtopic_slugs` are resolved **by slug in the target database** and checked against `ap-history-taxonomy-v1` in code. Package, app-chapter and database ids are never trusted (canonical Chapter 1 is app chapter 2 in the local test data; ids differ per database).

## Where package fields land
| Package field | Stored in |
|---|---|
| `source`, `source_qid`, `batch_id`, `source_file`, `qtype`, `review_status` | provenance columns (unique `(source, source_qid)`) |
| `difficulty` (easy/medium/tough/toughest) | `source_trace.difficulty_original` (full value, shown to learners); `questions.difficulty` gets E/M/H/H for legacy displays |
| `H`, `source_trace.original_H`, `candidate_id`, `source_ids` | `source_trace` (internal, never rendered) |
| `sources` | `source_trace.sources`; rendered to learners as links (host + locator) |
| `expanded_note` | `source_trace.expanded_note`; the link resolves anchors in `expanded_notes` |
| `coverage_scope`, `microtopic_slugs`, `secondary_chapters` | `secondary_tags` |
| manifest `approval_note`, package sha256 | `source_trace.content_approval_note`, `.package_questions_sha256` |

Learners see "Author-reviewed · not independently verified" on every such question. `review_status` stays `bilingual_approved`; it is never `fact_verified`.

## Expanded notes
Separate table, keyed by canonical chapter and stable anchor id (`CH01-S14`, `CH01-A04`, `CH01-G1-01`, `CH01-AG1-01`, `CH01-QR`). `package_section` is the package's own number and is never used as an app note section number. The 17 existing notes are not touched. Mapping to existing app sections lives in `expanded_note_app_map` (rows start `draft`; only `approved` rows are shown). Learner routes: `/learn/ap-history/<slug>/notes`, `/learn/ap-history/<slug>/notes/<anchor_id>` (a core section shows its connected addendum items; an addendum item links back to its core sections), `/learn/ap-history/<slug>/practice[?subtopic=<slug>]`.

## Validator changes needed for the real package
`QID_RE` now also accepts `C1` (as well as `C01`), dated batch parts (`B20261009`) and a revision suffix (`R2`, `R3`, `C`); ids are stored verbatim. `CODE_ONLY` accepts pairing codes with up to five items (`1–c, 2–e`).
