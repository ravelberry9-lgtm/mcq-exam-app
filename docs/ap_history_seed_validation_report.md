# AP History seed validation on a disposable copy

Run by `scripts/validate_ap_seed_on_copy.py`. The copy is decompressed from `data/content.db.gz` into a temporary directory and deleted afterwards. Nothing was seeded into staging, production or any real database.

- Result: **PASS**
- Units / core chapters / supplementary chapters: 5 / 31 / 4
- Learner-facing subtopics / microtopics: 187 / 317 (taxonomy version(s): ap-history-taxonomy-v1)
- Subtopics attached to supplementary chapters: 0
- First run added: {'units_added': 5, 'chapters_added': 31, 'supplementary_added': 4, 'units_existing': 0, 'chapters_existing': 0} and {'subtopics_added': 187, 'subtopics_existing': 0, 'microtopics_added': 317, 'microtopics_existing': 0}
- Second run added: {'units_added': 0, 'chapters_added': 0, 'supplementary_added': 0, 'units_existing': 5, 'chapters_existing': 35} and {'subtopics_added': 0, 'subtopics_existing': 187, 'microtopics_added': 0, 'microtopics_existing': 317} (idempotent)
- Legacy tables before and after (subjects, chapters, notes, questions) identical, column by column: **True**
- Row counts before: {'subjects': 11, 'chapters': 194, 'notes': 980, 'questions': 6737}; after: {'subjects': 11, 'chapters': 194, 'notes': 980, 'questions': 6737}; AP History questions before/after: 380/380
- Questions carrying provenance or canonical mapping after seeding: 0
- chapter_source_map rows (mapping is not seeded): 0
