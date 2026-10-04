# AP History MCQ import package — format `ap-history-import-v1` (dry-run validator only)

Status: **proposed format; the importer is a strict dry-run validator and has no apply mode.** Nothing is imported until a package placed by
the content team under `content/AP_History_MCQ_Project/05_claude_import/` passes validation **and** a later instruction authorizes the apply step.
Files in `02_drafts/`, `03_audits/` and anywhere else are never importable; the validator can parse a Codex draft markdown file only to produce a
readiness report.

## Layout

```
05_claude_import/<batch_id>/
    manifest.json
    questions.jsonl        # one JSON object per line, UTF-8
```

`manifest.json`: `format_version` (`ap-history-import-v1`), `taxonomy_version` (`ap-history-taxonomy-v1`), `batch_id`, `source`
(`codex_generated`), `question_count`, `questions_sha256` (sha256 of `questions.jsonl`, so any edit after approval is detected),
`content_approval` (`bilingual_approved`).

## One question record (all fields required unless marked optional)

| Field | Rule |
|---|---|
| `source` | one of `codex_generated, app_master, hanumanthrao, pyq_compiled, verified_pyq`; same as the manifest |
| `source_qid` | stable id `APH-U{unit}-C{chapter}-B{batch}-Q{number}`; unique within the batch; `(source, source_qid)` must not already exist in the database |
| `batch_id`, `source_file` | provenance; `batch_id` equals the manifest |
| `chapter_slug` | a canonical chapter slug: one of the 31 core chapters or a supplementary chapter |
| `subtopic_slug` | one primary learner-facing subtopic of that chapter; empty for supplementary chapters (they have no subtopics) |
| `microtopic_slugs` (optional list) | microtopics under the **primary** subtopic; `secondary_microtopics` (optional) may name any microtopic |
| `secondary_chapters` (optional list) | other chapters as tags only; must differ from the primary |
| `coverage_scope` | `direct` or `supplementary_context`, decided from the fact tested, not from the note section; a `supplementary_context` microtopic (for example `post-1600-context`) forbids `direct` |
| `difficulty` | `easy, medium, tough, toughest` |
| `qtype` | free label from the coverage plan (for example `Statements`, `Matching`, `Assertion–Reason`) |
| `question_te`, `question_en` | non-empty; Telugu text must contain Telugu script, English must contain Latin letters |
| `options` | exactly `a, b, c, d`, each `{ "te": ..., "en": ... }`, distinct; identical te/en text is accepted only for language-neutral codes such as `A-3, B-2, C-1, D-4` or `1 only` |
| `correct_answer` | `a`–`d` |
| `explanation_te`, `explanation_en` | non-empty |
| `review_status` | must be `bilingual_approved` |
| `coverage_plan_id` (optional) | the planner's subtopic id (for example `C01-S07`), kept as provenance |

## Checks (errors stop a package; warnings are reported and kept)

Errors: missing or empty field; bad source; bad id format; duplicate `source_qid`; already imported `(source, source_qid)`; unknown chapter,
subtopic or microtopic; subtopic not in the chapter; microtopic not under the primary subtopic; scope mismatch; options not exactly a–d,
incomplete, duplicated or not bilingual; Telugu or English text missing; review status other than `bilingual_approved`; manifest, count or checksum
mismatch; package outside `05_claude_import/` or inside `02_drafts/`; and three content rules:

* **Kataya Vema** (`content_use = blocked_until_verified`): any mention is rejected.
* **Komaram Bheem:** each question is mapped on its own; the primary chapter must be the supplementary Asaf Jahi chapter, Chapter 26 (Gond culture) or Chapter 19 (Hyderabad freedom leaders); never an Andhra-Movement chapter.
* Supplementary chapters take no subtopic.

Warnings: content-hash collision (inside the batch or against the database; the row is kept, never silently discarded); non-normalized Telugu
terminology (with the approved form); Rampa Rebellion outside Chapter 19; Chapter 26 Komaram Bheem question without the Asaf Jahi secondary; a
supplementary-chapter question marked `direct`; draft-style ids.

`content_hash` is the md5 of the normalised Telugu and English stems and options. It only detects duplicates inside this bank and against rows
that already carry a `content_hash`; legacy questions carry only the older `q_hash`, so cross-collection duplicate detection against the 380 legacy
questions and the app-master, Hanumanthrao and PYQ collections needs a separate comparison step.

## Mapping to the `questions` table (not executed)

| Package field | Column |
|---|---|
| `source`, `source_qid`, `source_file`, `batch_id`, `qtype`, `review_status`, `content_hash` | same-named columns |
| `chapter_slug` | `syllabus_chapter_id` |
| `subtopic_slug` | `subtopic_id` |
| `microtopic_slugs`, `secondary_microtopics`, `secondary_chapters` | `secondary_tags` JSON |
| `options` | `options_te` / `options_en` (keys `a`–`d`) |

Gaps with the current schema that need a decision before the apply step exists: no column for `coverage_scope`, for the four-level difficulty
(the table holds `E/M/H`), for `taxonomy_version` or for `coverage_plan_id` (all can go in `secondary_tags` JSON, or in a small additive
migration); `source_type` is NOT NULL and the package does not say which of `practice | chapter | pyq` to use (proposal: `practice` for
`codex_generated`); `subject_id` is derived (AP History); the legacy `chapter_id` stays NULL for new questions.

## Running the dry run

```
python scripts/ap_batch_import.py package content/AP_History_MCQ_Project/05_claude_import/<batch_id> [--db <sqlite file, opened read-only>]
python scripts/ap_batch_import.py drafts <draft.md> ...      # report only; always exits 2
```

## Coverage plan alignment — Chapter 1 (`U1_C01_Coverage_Matrix.md`) against `ap-history-taxonomy-v1`

The coverage plan has 12 subtopics (C01-S01 … C01-S12); the approved taxonomy has 6 learner-facing subtopics for Chapter 1. Nine plan items fit an
existing subtopic or microtopic; **three have no home** and need a decision before questions for them can be packaged. Nothing was changed.

| Plan id | Plan subtopic | Taxonomy v1 home |
|---|---|---|
| C01-S01 | Andhradesa: geographical setting | `u1-c01-land-people-identity`, microtopic `geography-extent` |
| C01-S02 | Andhra, Telugu and Tenugu: names and identity | `u1-c01-land-people-identity`, microtopics `people-name-origin`, `telugu-identity-language` |
| C01-S03 | Earliest literary references to the Andhras | `u1-c01-literary-sources` |
| C01-S04 | Classification of historical sources | **no home** (cross-cutting method and evidence types) |
| C01-S05 | Indian literary sources | `u1-c01-literary-sources` |
| C01-S06 | Foreign accounts | `u1-c01-foreign-accounts` |
| C01-S07 | Epigraphy | `u1-c01-inscriptions` |
| C01-S08 | Numismatics | `u1-c01-coins` |
| C01-S09 | Archaeology, monuments and material evidence | `u1-c01-archaeology-sites`, microtopic `archaeological-evidence` |
| C01-S10 | Important source sites | `u1-c01-archaeology-sites`, microtopic `important-sites` |
| C01-S11 | Historical reasoning and source criticism | **no home** |
| C01-S12 | Integrated mapping and chronology | **no home** |

Options for S04, S11 and S12 (a decision for the reviewer, not applied): add one learner-facing subtopic "Historical sources: classification, criticism and integration"
to Chapter 1 (the taxonomy would become 188 subtopics), or add them as microtopics under an existing subtopic. Note also that the plan now requires every question
to test an Andhra-specific fact, so S04, S11 and S12 questions must be anchored to a named Andhra source.
