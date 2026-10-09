# Chapter 1 closure package: preparation handoff (superseded in part by the production change plan; nothing run on production)

Package: `aph-u1-c01-closure-20261009`, 129 questions, `questions.jsonl` sha256 `1f1ad6fd94259c93f707b58fbb010d7b1fa877d441811cab5c5b9274cdcc6d73`. The frozen package was not edited. Nothing was imported, seeded or deployed on production.

## 1. `note_anchors.json` versus the addendum text
Title correction: my progress message said four mismatches; the correct number is **three** real title differences (A05, A07, A10). Nine other titles differ only in capitalisation (the text file is upper case) and are not discrepancies. The "four" was my miscount.

Core connections: `note_anchors.json` has them for A01–A03 (identical to the text). It has **none for A04–A12**; the text's `Core:` lines supply them.

| Anchor | Current title in note_anchors.json | Title in addendum text | Proposed title | Missing core connections in json (from text) |
|---|---|---|---|---|
| CH01-A01 | Amaravati: a specific donation record | same (case only) | no change | none (S22, S27 present) |
| CH01-A02 | Junagadh: Sudarshana Lake | same (case only) | no change | none (S22 present) |
| CH01-A03 | Bhattiprolu: language and script | same (case only) | no change | none (S21 present) |
| CH01-A04 | Bhattiprolu: relics, writing and Kubhiraka | same (case only) | no change | S21, S23 |
| CH01-A05 | Amaravati: donor groups | Amaravati: who supported the shrine? | Amaravati: who supported the shrine? | S27 |
| CH01-A06 | Amaravati: symbols and the human figure | same (case only) | no change | S27 |
| CH01-A07 | Patagandigudem: Ikshvaku grant | Patagandigudem: an Ikshvaku grant | Patagandigudem: an Ikshvaku grant | S23, S24 |
| CH01-A08 | Phanigiri: a physician's dharma-chakra | same (case only) | no change | S24 |
| CH01-A09 | River settings | same (case only) | no change | S01, S28 |
| CH01-A10 | Builder and dating ruler | Builder and ruler | Builder and ruler (the text heading; the Telugu heading is about the temple builder and ruler) | S24 |
| CH01-A11 | Secular buildings | same (case only) | no change | S27 |
| CH01-A12 | Medieval Telugu record | same (case only) | no change | S24, S29 |

Core anchors S01–S50: headings and section numbers all match the text. The importer treats the addendum text as authoritative and reports these as warnings; a corrected `note_anchors.json` is a package-owner decision (new frozen version, new hash).

## 2. Overlap decisions (cross-package only)
Neither the earlier 64-question set (`aph-u1c01-…` import refs) nor the 129 set exists in any database I can inspect: the local test database used had no `import_ref` or `source_qid` columns yet, and nothing was applied to production (whose contents I cannot inspect). Both overlaps are therefore recorded as **cross-package overlaps only**; no retain/skip action is needed unless the 64-set is ever applied. The overlap guard stays on (apply is blocked until a human decides) and was not bypassed.

| New question | Earlier question | Match | Difference | If both ever present, proposed decision (for approval) |
|---|---|---|---|---|
| APH-U1-C1-B20261009-Q026 "To which language family does Telugu belong?" | aph-u1c01-AP9-00126 | same English stem, same answer (Dravidian) | options and Telugu wording differ; package lists it in `related_old_package_refs` | retain the 129-set version; skip/retire the older one |
| APH-U1-C1-B20261009-Q099 "Which Ashokan edict names the Andhras?" | aph-u1c01-B006 | same stem, options, answer and Telugu text | none; **not** in `related_old_package_refs` | retain one only; propose retaining the 129-set version and asking the package owner to add the link |
The package also names 29 older refs as related (superseded) items; the same rule would apply. Legacy 380 questions: no overlap, no action.

## 3. Production Alembic revision (the only Railway environment)
Not confirmed. This session has no authorized database access (no credentials on the linked computer, the cloud cannot reach the host, and `/healthz` does not expose a revision). Nothing was run against production. Read-only check for you, which prints only the revision (do not paste the URL):
`set DATABASE_URL=<Railway PRODUCTION Postgres URL>` then `python -m alembic current`
(this is the PRODUCTION database)

Migration chain (repo head `b8c9d0e1f2a3`): `c68decc8a6c3` baseline → `a1b2c3d4e5f6` → `b2c3d4e5f6a7` → `c3d4e5f6a7b8` → `d4e5f6a7b8c9` (question note link/provenance; my earlier migration) → `f6a7b8c9d0e1` (canonical syllabus + provenance columns) → `a7b8c9d0e1f2` (microtopics) → `b8c9d0e1f2a3` (expanded notes). The local test database was at `c3d4e5f6a7b8`; production's revision is unverified.

Required steps, in this order, **not executed**, each needing your approval:
1. `python -m alembic upgrade head`
2. `python scripts/seed_ap_canonical.py` (preview), then `--apply --with-subtopics` (5 units, 31 core + 4 supplementary chapters, 187 subtopics, 317 microtopics)
3. `python scripts/import_ap_v1.py notes <pkg>` then `--apply --approval-ref "<ref>"`
4. `python scripts/import_ap_v1.py questions <pkg>` then `--apply --approval-ref "<ref>"`

## 4. The two Telugu warnings (validator `non_normalized_term`, warnings only)
A validator warning does not show a misspelling. Both are alternative forms the project's taxonomy file has standardised; neither is judged wrong here.
- **Q075** (`u1-c01-literary-sources`, Firishta/Deccan, Golconda): uses `కుతుబ్‌షాహీ(లు)` with a zero-width non-joiner, in the explanation and in option D. The taxonomy's learner-facing form is `కుతుబ్ షాహీ`. The ZWNJ spelling is a legitimate orthographic choice; the difference is spacing convention. Changing it would edit option text in the frozen package.
- **R2-Q004** (`u1-c01-inscriptions`, Kharavela): uses `హాథీగుంఫా` in the question stem. The taxonomy's form is `హాతిగుంఫా` (the Telugu-style rendering of Hathigumpha). Both transliterations are in use; the choice is a consistency decision for the Telugu reviewer under the TELUGU-001 rule.
No change made. Importing is not blocked by these. Decision needed: keep as is, or normalise in a new package version.

## 5. Handoff facts
- Branch `feature/ap-history-v1-native`, implementation commit `3322666` (on canonical `842a696`, on `1303cf0`); this handoff doc is committed on top, see `git log`.
- Bundle `ap-history-v1-native.bundle` in `mcq_app\_review`.
- Migration dependencies: `b8c9d0e1f2a3` ← `a7b8c9d0e1f2` ← `f6a7b8c9d0e1` ← `d4e5f6a7b8c9` ← `c3d4e5f6a7b8`. The importer needs the canonical structure and subtopics seeded and the package notes loaded first.
- Exact preview commands (write nothing; run against a local test database, or against production only after approval):
  `python scripts/import_ap_v1.py notes C:\Users\AashrithaNagababu\Documents\Codex\AP_History_Working\05_claude_import\aph-u1-c01-closure-20261009`
  `python scripts/import_ap_v1.py questions C:\Users\AashrithaNagababu\Documents\Codex\AP_History_Working\05_claude_import\aph-u1-c01-closure-20261009`
  The package path must sit under a folder named `05_claude_import`. Without `--apply` both commands only print a report.
- Expected preview on a seeded database: notes 74 to add, questions 129 to import, 0 overlaps, 0 unresolved links, validator errors 0 and warnings 2.
- Remaining open: items 1 and 4 need package-owner / Telugu-reviewer decisions; item 3 needs your read-only revision check.
