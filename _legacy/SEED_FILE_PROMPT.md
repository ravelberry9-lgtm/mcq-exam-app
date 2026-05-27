# Master Prompt — Seed File Creation
# Use this prompt (with PDF attached) to build any new chapter seed file
# Last updated: April 2026

---

You are helping me build a seed file for Chapter [X] of [Subject/Topic] — [Chapter Name].
The app is Flask + SQLite/PostgreSQL. Seed file: seed_ch[X].py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BEFORE YOU WRITE A SINGLE LINE OF CODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. READ THE ENTIRE PDF FIRST
   - Read the full chapter PDF before writing anything
   - Every fact (date, name, number, place) must come
     from the PDF — not your training knowledge
   - If PDF says 1955, write 1955. Not 1957.
   - If you are not sure about a fact, say so — don't guess
   - Count distinct topics/concepts in the PDF
   - That count determines sections and MCQs — not a fixed number
   - Tell me: "I see X topics, Y key facts, Z exam points
     — I plan N sections and ~N MCQs"
   - Wait for my confirmation before writing anything

2. READ THE SCHEMA FIRST
   - grep app.py for CREATE TABLE
   - Use exact table names and column names found there
   - Check admin.html JS: what fields does it check?
     (success, message, easy, medium, hard, error, etc.)
   - Do this before writing any function

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTIONS & MCQ COUNT — BASED ON CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sections:
- One section per distinct topic in the PDF
- Not fixed — could be 10 or 25 depending on chapter
- If a topic has sub-topics worth separate audio
  narration, make them separate sections
- LAST SECTION must always be the Cinematic Story
  (see story narration rules below)

MCQs:
- Not fixed — scale with chapter size
- Minimum 5 MCQs per section
- Split: 40% easy, 40% medium, 20% hard
- Easy   = direct recall from PDF
- Medium = application or comparison
- Hard   = multi-fact, assertion-reason, match the
           following, or "which is incorrect" type
- Tell me your planned MCQ count after reading PDF
  and wait for my confirmation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FILE STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CH[X]_SECTIONS = [ {title, sub, audio}, ... ]
CH[X]_MCQS = [ (sec_idx, difficulty, q, a, b, c, d, correct, expl), ... ]

def _seed_ch[X]_notes_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres, force=False)
def _seed_ch[X]_mcqs_inner(conn, db_exec_fn, row_to_dict_fn, use_postgres)

Seed functions must:
- Use study_notes and chapter_mcqs tables (not notes/mcqs)
- Return {"success": True/False, "message": ...,
          "easy": N, "medium": N, "hard": N}
- CREATE TABLE IF NOT EXISTS at start of each function
- notes inner: stores all sections as JSON in
  study_notes.sections_json (one row per chapter)
- mcqs inner: one row per MCQ in chapter_mcqs,
  linked by study_note_id

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHUNK STRATEGY — STRICT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- Write maximum 4 sections per message
- Stop after 4. Wait for me to say "continue"
- If token limit hits mid-section, stop cleanly at
  end of current section, tell me exactly which
  section number to resume from
- Never attempt the entire file in one shot
- MCQs: write in batches of 25-30, stop, wait

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NARRATION RULES — SECTION AUDIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE GOLDEN RULE:
Write as if a professor is speaking directly to a
student — warmth, logic, drama. NOT a textbook.
NOT a Wikipedia article. A human talking to another
human who needs to pass an exam.

── LANGUAGE RULES ──────────────────────

L1. NEVER use passive voice. Ever.
    Bad:  నియమించబడ్డాడు / సంతకమైంది / ఓడించబడ్డాడు
    Good: నియమించారు / సంతకం పెట్టాడు / ఓడిపోయాడు

L2. NEVER use "యొక్క". Ever.
    Bad:  Clive యొక్క సైన్యం
    Good: Clive సైన్యం

L3. English words — only where necessary:
    Use for: proper nouns (names, places), technical
             terms with no Telugu equivalent
             (Subsidiary Alliance, GDP, Monsoon),
             Treaty/Battle/Act names
    NEVER for: common words
    Bad:  "detailed గా", "background", "support ఇచ్చారు",
          "important", "advantage", "basically"
    Good: "వివరంగా", "నేపథ్యం", "మద్దతు ఇచ్చారు",
          "ముఖ్యమైన", "పై చేయి"

L4. NEVER directly translate English idioms into Telugu.
    Bad:  "British India తండ్రి అయ్యాడు"  (funny/wrong)
    Good: "British India పునాది వేశాడు"
    Rule: Keep English titles in English.
          "Clive of India" — OK.
          "India యొక్క Clive" — never.

── STRUCTURE RULES ──────────────────────

S1. Every section MUST have a unique opening.
    NEVER start with:
      "ఇప్పుడు X గురించి వివరంగా నేర్చుకుందాం!"
      "ఇప్పుడు మనం X చూద్దాం"
    These are dead openings — every section sounds same.

    Use one of these patterns (rotate, never repeat):
    1. Year/Event Hook:
       "1757. ఆ ఒక్క సంవత్సరం భారతదేశం మారిపోయింది."
    2. Question Hook:
       "ఒక clerk — soldier కాదు — ఎలా చరిత్ర మార్చాడు?"
    3. Contrast Hook:
       "ఒక వైపు వేల మంది. మరో వైపు 500 మంది. గెలిచింది ఎవరో తెలుసా?"
    4. Character Intro Hook:
       "ఆయన పేరు Siraj ud-Daulah. వయసు 23. Bengal నవాబు."
    5. Consequence Hook:
       "ఈ ఒక్క యుద్ధం వల్ల 200 సంవత్సరాల బానిసత్వం మొదలైంది."
    6. Curiosity Hook:
       "మీరు ఎప్పుడైనా ఆలోచించారా — వర్షం ఎందుకు ఒక చోట పడుతుంది, మరో చోట పడదు?"

S2. Introduce every character when they appear first time.
    Pattern: "[పేరు] — [ఎవరు], [ఏం చేశారు/చేయాలనుకున్నారు]."
    Example:
      "Mir Jafar — Siraj మామ, సైన్యాధిపతి. నవాబు కావాలని కోరిక."
    Cross-reference earlier sections:
      "Chanda Sahib — గుర్తుందా, మొదటి కర్నాటిక్ యుద్ధంలో పరిచయమైన ఆయన..."

S3. Facts as cause-effect — NEVER as a list.
    Bad:  "1749లో అంబూర్ యుద్ధం జరిగింది. అన్వరుద్దీన్ మరణించాడు."
    Good: "1749లో అంబూర్ యుద్ధంలో అన్వరుద్దీన్ మరణించాడు —
           దాంతో కర్నాటిక్ నవాబు లేకుండాపోయింది.
           Chanda Sahib ఆ అవకాశం తీసుకున్నాడు."
    Connectors: దాంతో / అందుకే / దీని వల్ల / ఫలితంగా / కానీ / అప్పుడు

S4. Famous names need weight — never just a mention.
    Bad:  "Clive 500 మంది తో Arcot ఆక్రమించాడు."
    Good: "Robert Clive — EIC లో clerk గా పని చేసే యువకుడు.
           Soldier కాదు, General కాదు. కానీ 1751లో
           ఐదువందల మంది తో అర్కాట్ పట్టుకున్నాడు.
           వేల మంది శత్రువులు వచ్చారు. యాభైమూడు రోజులు
           వెనక్కి అడుగు వేయలేదు."

── EMOTIONAL RULES ──────────────────────

E1. Every section needs at least one emotional beat —
    a moment where the student stops and thinks.
    "ఆలోచించండి — 23 ఏళ్ల అబ్బాయి. సొంత మామే వ్యతిరేకంగా."
    "53 రోజులు. తినడం లేదు. ఒక్క అడుగు వెనక్కి వేయలేదు."

E2. Engagement markers — use naturally, not forcibly:
    "రాసుకోండి"     — before exam-critical facts
    "అర్థమైందా?"    — after complex concepts
    "ఆలోచించండి —"  — before emotional moments
    "గుర్తుంచుకోండి —" — before recap
    "పరీక్షలో తప్పకుండా వస్తుంది" — for high-priority facts
    Do NOT overuse. One or two per section, natural only.

── SECTION TYPE RULES ──────────────────

War sections:    Introduce both sides first (who vs who, why).
                 One key turning point. End with consequence.
Personality:     Age + background first. Unique quality.
                 Legacy — why remembered today.
Treaty/Act:      "Before this, what happened?" first.
                 3-4 main provisions only — not all.
                 "What changed because of this?"
Geography:       Comparisons (bigger than our state, etc.)
                 Why it matters. Connect to student's life.
Economy/Polity:  Simple analogy first. Real-life example.
                 Explain jargon immediately when used.

── RECAP RULE ──────────────────────────

End every section with "గుర్తుంచుకోండి —"
Make it punchy — not a dry list.
End with a forward bridge to next section.

Bad:
  "గుర్తుంచుకోండి — రెండవ కర్నాటిక్ యుద్ధం 1749-54.
   అంబూర్ యుద్ధం: అన్వరుద్దీన్ మరణం."

Good:
  "గుర్తుంచుకోండి —
   Nasir Jung = నిజాం కొడుకు = British వైపు.
   Muzaffar Jung = నిజాం మనవడు = French వైపు.
   Arcot వీరుడు = Clive. 500 మంది. 53 రోజులు.
   ముగింపు = పాండిచ్చేరి సంధి 1754.
   British గెలిచారు — ఇది pattern, తర్వాత కూడా అదే జరుగుతుంది!"

── TONE GUIDE BY SUBJECT ────────────────

History   → Storytelling, drama, suspense. "ఏం జరిగిందంటే..."
Geography → Wonder, comparison, scale. "ఆలోచించండి..."
Polity    → Logical, relatable, real-life. "మన జీవితంలో..."
Economy   → Simple analogy. "ఒక ఇంటి budget లాంటిదే..."
Science   → Curiosity, wonder. "ఎందుకు ఇలా జరుగుతుందో తెలుసా?"

── PRE-WRITE CHECKLIST (each section) ──

Before writing any section audio, answer:
1. Core message — one sentence
2. What should student feel after reading?
3. Key characters — did I intro them?
4. Where does the emotional beat come?
5. Is cause → effect clear?

── POST-WRITE CHECKLIST (each section) ──

After writing, verify:
[ ] No passive voice (బడ్డాడు / మైంది endings gone?)
[ ] No "యొక్క"
[ ] No dead opening ("ఇప్పుడు X గురించి వివరంగా నేర్చుకుందాం"?)
[ ] First-time characters introduced?
[ ] Famous names given weight?
[ ] Cause-effect, not fact-list?
[ ] At least one emotional beat?
[ ] English only where necessary?
[ ] No English idiom translated literally?
[ ] Recap punchy + forward bridge?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STORY NARRATION — LAST SECTION (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The final section of every chapter must be a
cinematic story that covers the ENTIRE chapter
as one flowing narrative.

Title format: "సినిమాటిక్ కథ — [Chapter Name]"

Story structure:
- Divide into 8-10 sub-chapters
- Each sub-chapter: one major theme from the chapter
- Each has a Telugu title + English subtitle
- All key facts, dates, names woven into the story
- No bullet points — flowing Telugu prose

Story narration rules (stricter than section rules):

OPENING:
  Must hook immediately — contrast, consequence, or
  a single dramatic line.
  Bad:  "ఈ అధ్యాయంలో మనం చదివిన అంశాలు..."
  Good: "వర్తకులుగా వచ్చారు — చక్రవర్తులుగా వెళ్ళారు.
         ఆ కథ ఎలా జరిగిందో విందాం."

CHARACTERS:
  Every major personality gets a 2-3 line portrait
  when they first appear in the story.
  Age, background, what made them unique.

FLOW:
  Each sub-chapter must end connecting to the next.
  "Plassey British ని రాజకీయ శక్తిగా చేసింది.
   Buxar ఆ శక్తిని confirm చేసింది."

EMOTIONAL PEAK:
  Every story must have one moment of genuine emotion —
  tragedy, betrayal, courage, or irony.
  "Tipu చనిపోయాడు — కానీ పారిపోలేదు."
  "150 సంవత్సరాల స్వప్నం కూలిపోయింది."

CLOSING:
  End with meaning — not just facts.
  Connect history to why the student is reading it.
  "ఆ చరిత్రను మనం ఇక్కడ చదివాం — పరీక్షలో
   రాయడానికి మాత్రమే కాదు, మళ్ళీ జరగకూడదని
   గుర్తుంచుకోవడానికి."

RECAP in story:
  "గుర్తుంచుకోండి —" at the very end.
  Full chapter timeline in punchy = format.
  "EIC 1600 → కర్నాటిక్ (3) → Plassey 1757 → ..."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MCQ QUALITY RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- correct field: lowercase only — "a", "b", "c", or "d"
- Every answer must be verifiable from the PDF
- All 4 options must be plausible (no obviously wrong)
- At least 20% of MCQs must have Telugu question text
- Hard MCQs must include:
  assertion-reason, match the following,
  "which is incorrect", multi-statement types

Self-check after all MCQs written:
  python3 -c "
  from seed_ch[X] import CH[X]_MCQS
  bad = [i for i,t in enumerate(CH[X]_MCQS)
         if t[7] not in ('a','b','c','d')]
  print('Bad correct fields:', bad or 'None — all good')
  e=sum(1 for t in CH[X]_MCQS if t[1]==1)
  m=sum(1 for t in CH[X]_MCQS if t[1]==2)
  h=sum(1 for t in CH[X]_MCQS if t[1]==3)
  print(f'Easy:{e} Medium:{m} Hard:{h} Total:{e+m+h}')
  "

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERIFICATION — DO NOT SKIP EVER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After full file is written, run all 3:

1. Syntax check:
   python3 -c "import ast; ast.parse(open('seed_ch[X].py').read()); print('OK')"

2. Full seed test (in-memory SQLite):
   python3 -c "
   import sqlite3, sys
   sys.path.insert(0,'.')
   from seed_ch[X] import _seed_ch[X]_notes_inner, _seed_ch[X]_mcqs_inner
   conn = sqlite3.connect(':memory:')
   conn.row_factory = sqlite3.Row
   conn.executescript('''
     CREATE TABLE study_notes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       subject TEXT, topic TEXT, chapter_num INTEGER,
       chapter_title_te TEXT, chapter_title_en TEXT,
       pages_ref TEXT DEFAULT \"\",
       sections_json TEXT DEFAULT \"[]\",
       subtopic TEXT DEFAULT \"\",
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
     CREATE TABLE chapter_mcqs (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       study_note_id INTEGER, section_idx INTEGER,
       difficulty INTEGER, exam_type TEXT DEFAULT \"General\",
       q_te TEXT, opt_a TEXT, opt_b TEXT, opt_c TEXT, opt_d TEXT,
       correct TEXT, explanation_te TEXT DEFAULT \"\",
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
   ''')
   def db_exec(c,s,p=()): return c.execute(s,p)
   def rtd(r): return dict(r) if r else None
   r1 = _seed_ch[X]_notes_inner(conn,db_exec,rtd,False)
   r2 = _seed_ch[X]_mcqs_inner(conn,db_exec,rtd,False)
   print('Notes:', r1)
   print('MCQs:', r2)
   assert r1['success'], 'Notes seed failed!'
   assert r2['success'], 'MCQ seed failed!'
   n = conn.execute('SELECT COUNT(*) FROM study_notes').fetchone()[0]
   m = conn.execute('SELECT COUNT(*) FROM chapter_mcqs').fetchone()[0]
   print(f'study_notes rows: {n} | chapter_mcqs rows: {m}')
   "

3. Show output. Do NOT say done until:
   - success:True for both notes and MCQs
   - MCQ count matches planned count
   - No syntax errors

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PDF ACCURACY CROSS-CHECK — MANDATORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

At the end of all sections AND MCQs:
- Re-read the PDF one more time
- Check every date, name, number against PDF
- Check every MCQ answer against PDF
- List any corrections made
- Confirm: "All facts verified against PDF. X corrections made."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOW TO START
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Say this to start (attach PDF):

"Read the full PDF [attach PDF here].
 Read app.py schema and admin.html JS.
 Tell me: how many sections and MCQs you plan.
 Wait for my confirmation.
 Then write sections 0-3 only."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUICK REFERENCE — WHAT NOT TO WRITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Never write this kind of narration:
  "లండన్‌లో ఒక రాజ్య ఆదేశం సంతకమైంది."
  → passive, dry, no emotion

  "Clive యొక్క 200 సైనికులతో Arcot ఆక్రమించబడింది."
  → "యొక్క" + passive — double mistake

  "ఇప్పుడు రెండవ కర్నాటిక్ యుద్ధం గురించి వివరంగా నేర్చుకుందాం!
   రెండవ కర్నాటిక్ యుద్ధానికి ప్రధాన కారణాలు రెండు — మొదటిది..."
  → dead opening, fact-dump, no story

Always write like this:
  "నిజాం చనిపోయాడు. వారసత్వం కోసం రెండు పక్షాలు —
   Nasir Jung British వైపు నిలబడ్డాడు, Muzaffar Jung
   French వైపు చేరాడు. అర్థమైందా?"
  → active, Telugu flow, character intro, engagement
