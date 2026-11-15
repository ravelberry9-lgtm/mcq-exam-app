# Geography rebuild plan — Chapter 4 onward (written 2026-11-04)

Skill: telugu-exam-lessons (latest package). Outputs go to `content/geography/_claude_rebuild/<chapter>/`.
Original lesson and bank files are never edited.

## What the syllabus says (APPSC Group 2 screening; Group 2 Mains has no geography)
1. General and physical geography: Earth in the Solar System, interior, landforms, climate, atmosphere, ocean water (tides, waves, currents).
2. India and AP: physiography, climate, drainage, soils, vegetation; natural hazards and disaster management.
3. Economic geography of India and AP: resources, agriculture, industries, transport, communication, tourism, trade.
4. Human geography of India and AP: human development, demography, urbanisation, migration, race/tribe/religion/language groups.
World regional and world human geography are not in the Group 2 list; they matter for Group 1 only (to be confirmed against the Group 1 syllabus).

## Order and grouping — superseded by lesson_map.md (new numbers 1–38, grouped by syllabus)
Priority A — Group 2 physical (world chapters):
- U4: W4 Interior, rocks, geological time (pilot of the lean pipeline)
- U5: W5 Plate tectonics + W6 Weathering/geomorphic processes (W6 has only 24 questions)
- U6: W7 Mountains, plateaus, plains
- U7: W8 Fluvial, aeolian, karst, glacial, coastal landforms
- U8: W9 Atmosphere + W10 Insolation…rainfall (W10 is large; may split)
- U9: W11 World climate regions
- U10: W12 Ocean basins + W13 Waves, tides, currents + W14 Coral reefs/ocean resources
- U11: W15 Soils, vegetation, biomes
Priority B — India/AP physical (I1–I7, I20): each India chapter is large (notes up to 777 KB) — split big ones (I6, I8) into two lessons rather than clubbing.
Priority C — India/AP economic and human (I8–I19).
Priority D — Group 1 only: W16–W19 world human, W20–W27 continents as one "World regions" lesson pair, W28–W29 revision banks (questions only, no lesson).

## Lean pipeline (to save usage)
Chapters 1–3 used a writer + reviewer + reviser for every concept, a full Telugu rewrite of every question by agents, and a separate trim pass. New pipeline:
1. Outline (1 Opus agent): concept list, owning section for each concept, fact ledger, word budget (aim ~15–20k words per lesson — Chapter 1 size).
2. Write (2–3 Opus agents in parallel): no-repetition rules applied while writing, lint + self student-read before handing back. No trim pass needed.
3. Review (1 Sonnet agent, whole lesson, flags only) → revise (1 Opus agent, flagged items only).
4. Assemble + HTML by script.
5. MCQs:
   a. Script pass first: English names written in Telugu script → Latin script, using a glossary built from the Chapter 1–3 fixes. No agent cost.
   b. Check (Sonnet, ~200 questions per agent): link to section, verify key, fix only flagged questions (giveaways, weak explanations, wrong facts).
   c. Merge + validate by script.
   d. New questions only for untested fact lines (1 Opus), 1 blind Sonnet review, 1 Opus revise.
6. Spot-check by the user: ~10 questions and 2 sections per unit.
