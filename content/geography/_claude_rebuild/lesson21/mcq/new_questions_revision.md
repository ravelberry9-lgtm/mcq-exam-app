# Lesson 21 NEW MCQ revision (step NEW REVISE)

Source edited: q_new.py (backup q_new.prerev.py; previous output new_questions.prerev.json). The edit script is in the scratchpad (l21edits.py), with 30 exact-match replacements.
Result: build.py BUILD CLEAN (0 errors, 0 length flags); check_mcq_giveaways.py 0 problems. 68 questions; ids, keys and key positions unchanged (verified against the prerev JSON). Changed: N004, N008, N009, N011, N013, N017, N018, N020, N028, N030, N038, N041, N046, N054, N062, N065, N068.

## Applied
1. Anachronistic distractors
   - N041: A/C/D are now 2 October 2014, 26 January 2015 and 25 September 2015. Their explanations only use the lesson date (25 September 2014).
   - N017: 1 June 2000 and 1 June 1970 became 1 July 2002 and 1 January 2006 (after the 2002 Act). The explanation now uses only the PMLA and CCI dates.
   - N018 D: now "licence from the SEZ Development Commissioner" (the lesson names this officer at line 823).
2. Explanations not backed by the lesson
   - N013: "from 1991" removed. It now says FIPB "handled non-automatic proposals under the reformed regime; abolished 2017".
   - N018: "defence and media" removed.
   - N054: district names removed from the option explanations.
   - N058: NOT changed. The lesson does state the public hearing (line 1254: "చాలా ప్రాజెక్టులకు అనుమతికి ముందు ప్రజాభిప్రాయ సేకరణ (Public hearing) జరగాలి"), so the reviewer's flag was wrong.
3. Leaks
   - N038: statement 2 is now AP-only ("Prakasam NIMZ has final approval"; still true).
   - N009 C: now "Abolishing industrial licensing for most industries" (no 18).
   - N065 B: 14 changed to 10.
   - N062: "(weight-losing industry)" removed from both stems. The TE bracket is now "(Sugar mills)".
   - N030: statement 2 replaced by "From 1 July 2020 manufacturing and service enterprises share one set of limits" (true). The export-turnover clause was removed from the explanation.
   - N068 D: no longer mentions PAN/GST.
   - N008 C: shortened to "groups under IPR 1948".
4. N046 giveaway: key D shortened to "12 projects in 10 States; 11 sites are named". B is now "12 projects in 9 States, with UP and AP getting two each", with a new explanation. The key is no longer the longest option.
5. Small wording fixes
   - N004 List II item 3: now "The IPR 1948 group kept as a central monopoly".
   - N011 C: now "coal and lignite".
   - N020 statement 2: now "after the Supreme Court ruling of 20 July 2021".
   - N028 EN: now "investment in plant and machinery", matching the TE.

## Not applied (and why)
- Review item 5: re-balancing the statement keys (N012, N020) and moving the matching/sequence keys (N004, N049). Both would change keys or key positions, which this step forbids. The current spread passes the build's variety rules.
- N056 name-vs-role (optional), N057/N036/N047 thin explanations (low), N045/N055 FACT-DOUBT (low; the lesson supports both): left as they are.
- Key-longest tally (14 questions): all are below the 1.3 ratio and the checker reports 0. Only N046 was trimmed.
