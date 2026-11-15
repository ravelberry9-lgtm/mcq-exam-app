# L32 MCQ NEW REVISE (Opus)

Result: 51 -> 47 questions (dropped 005, 007, 009, 011; ids kept as gaps). build.py CLEAN (0 errors, 0 length flags); check_mcq_giveaways.py 0 problems.
New keys A10 B13 C12 D12 (A 21%, least frequent as build requires); combined with linked 55: A25 B26 C24 D27.
Re-solved all 47 after rebuild: every key matches its single defensible answer.

## Review items
- Q034 rewritten per shared Census 2027 facts: "latest published ST figure as of Nov 2026" (key 2011, 8.6%); distractors 2011/8.20%, 2001/8.20%, 2026 house-listing phase. Explanation gives the phased schedule (HLO Apr–Sep 2026; snow-bound Sep 2026; Goa/UP/Punjab/Uttarakhand Dec 2026–Jan 2027; rest Feb 2027), figures not yet published. CENS table row updated. Key C.
- Q044: "we have not confirmed" removed -> "no extension announced as of Nov 2026"; new near-period distractors (2023–24 to 2027–28, 2022–23 to 2024–25, 2024–25 to 2026–27); Gaurav Divas stretch removed. JAN table row reworded. Key A.
- Giveaways: Q001 TE "(Ethnicity)" removed (now "(Group identity)"), key D. Q015 TE "ఆదేశం" -> "పత్రం"; all options are plain document names (key "The Presidential Order of 1950"). Q024 all four options now land-related (PESA Gram Sabha land, FRA forest land, Sixth Schedule land rule, key AP amendment). Q027 options Fourth/Fifth/Seventh/Eighth (key no longer the middle value), key B.
- Leaks: Q011 dropped (Q008 leak gone). Q048 now tests Polavaram HQ (false: Rampachodavaram) + Markapuram from Prakasam (true), key B; high-ST-district line removed, so Q051 stem no longer proves it and Q051 explanation no longer gives Polavaram source/HQ. Q049 explanation drops the undivided-AP Sugali line and uses a new Telangana-only table (TGBIG). Q017 explanation drops MoTA 1999 and uses a new NCST table instead of STORG (which showed all Q018 dates).
- Weak distractors: Q012 (language-based types, exactly six fixed groups, measurement accuracy); Q019 manual wrong orders (no Phratry-first); Q020 (endogamy-only, exogamy-only, own clan); Q029 (fell-then-rose, rose-then-fell, flat-then-rose); Q037 stem now "north-eastern community" so Adi/Nyishi compete; Q048, Q051 rebuilt (count vs share, density, Sugali), Q051 key D.
- Guha cluster 7 -> 3: kept Q006 (rewritten as a "How" stem, Risley 1901/seven types as a distractor, F016), Q008 (Santhal -> Chenchu to keep F025), Q010 ("just two" absolute removed). Dropping Q007 also removes the Q007/Q013 Dravidian duplicate.
- Mappila: Q036 statement/explanations and LAK table use "Mappila", no "religious community" clause.
- Also: Q021 TE stem "మానవశాస్త్ర నమోదుల్లో", option C/D explanations state facts; Q026 "Integrated Tribal Development Agency"; Q035 TE "పహారీ ఎత్నిక్ గ్రూప్"; Q017 65th/86th explanations trimmed to "did not insert 338A".

## Not changed (with reason)
- Two-statement keys stay A/B: build.py requires 2-statement keys to be A and B only.
- Q023 TE option stays "కేరళ" (build forbids brackets in TE options); Keralam line is in option explanation and explanation.
- Q041, Q040, Q005-type low-priority items and Q043 stem date (15 Nov 2023) left as is.
- Facts now without a question after the drops: F015 (anthropometry), F019 (Guha six-race list), F022 (Mongoloid sub-groups); earlier gaps F065, F090, X06, X15 unchanged.

Patch script: /tmp/claude-0/-home-claude/f2b50ec2-2ed3-5e64-b457-0f70e1f1710b/scratchpad/patch32.py (pre-revision copy: scratchpad/q_new_L32_prerev.py).
