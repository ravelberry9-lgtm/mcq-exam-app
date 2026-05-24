"""
build_natl_250.py
Curates seed_national_ca_2026_mcq.py from 791 → 249 MCQs
Generates:
  - seed_national_ca_2026_mcq.py (curated, in-place via overwrite)
  - archive_deleted_mcqs_natl.py
  - static/notes/Indian_Current_Affairs/Divisions/natl_mcqs_part1.html (~124 Qs)
  - static/notes/Indian_Current_Affairs/Divisions/natl_mcqs_part2.html (~125 Qs)
"""
import re, os, sys

SEED_FILE = os.path.join(os.path.dirname(__file__), "seed_national_ca_2026_mcq.py")
ARCHIVE_FILE = os.path.join(os.path.dirname(__file__), "archive_deleted_mcqs_natl.py")
DIVS = os.path.join(os.path.dirname(__file__),
       "static/notes/Indian_Current_Affairs/Divisions")

KEPT_IDS = set([
    31001,31004,31007,31009,31010,31011,31012,31015,31016,31019,31020,31022,31024,
    31026,31027,31029,31030,31033,31034,31037,31038,31043,31047,31048,31050,31051,
    31053,31057,31058,31061,31062,31063,31064,31065,31066,31067,31068,31069,31070,
    31071,31075,31077,31078,31080,31081,31082,31088,31089,31090,31091,31092,31093,
    31098,31099,31100,31101,31102,31103,31106,31108,31109,31110,31111,31112,31114,
    31115,31116,31117,31118,31121,31123,31124,31125,31126,31127,31128,31129,31130,
    31131,31132,31133,31134,31139,31140,31142,31143,31144,31145,31151,31154,31157,
    31158,31162,31165,31166,31167,31168,31170,31172,31174,31177,31180,31183,31184,
    31186,31191,31196,31197,31198,31199,31200,31201,31202,31204,31205,31207,31210,
    31212,31213,31215,31217,31220,31221,31225,31226,31228,31231,31234,31235,31244,
    31246,31248,31249,31255,31266,31273,31292,31293,31294,31296,31297,31299,
    # PM Schemes section
    31300,31301,31309,31310,31311,31313,31314,31318,31321,31322,31323,31324,31327,
    31328,31329,31330,31335,31336,31337,31339,31341,31342,31354,31355,31357,31358,
    31360,31361,31362,31363,31365,31366,31367,31371,31373,31376,31377,31378,31379,
    31380,31381,31382,31383,31389,31391,31393,31395,31396,31397,31398,31399,31400,
    31401,31402,31408,31409,31410,31411,31413,31430,
    # 31431-31800 selects
    31433,31456,31498,31513,31542,31544,31545,31546,31547,31548,31551,31552,31556,
    31559,31564,31565,31567,31575,31581,31582,31586,31588,31590,31600,31615,31617,
    31618,31691,31692,31703,31775,31776,31778,31779,31780,31781,31782,31786,31787,
    31788,31789,31790,31791,31792,31794,31795,31798,
])
print(f"KEPT_IDS count: {len(KEPT_IDS)}")

# ── PARSE SEED FILE ──────────────────────────────────────────────────────────
with open(SEED_FILE, encoding="utf-8") as f:
    raw = f.read()

# Locate the questions list
list_start = raw.find("questions = [")
list_end   = raw.rfind("]") + 1
header = raw[:list_start + len("questions = [")]
footer = raw[list_end:]
body   = raw[list_start + len("questions = [") : list_end - 1]

# Split into individual question blocks
# Each block starts with optional whitespace then (NNNNN,
q_pattern = re.compile(r'(?:^|\n)(\s+\(\d{5,6},)', re.MULTILINE)
positions = [(m.start(), m) for m in q_pattern.finditer(body)]

blocks = []
for i, (pos, m) in enumerate(positions):
    end = positions[i+1][0] if i+1 < len(positions) else len(body)
    block_text = body[pos:end].rstrip().rstrip(',').strip()
    # Extract ID
    id_m = re.match(r'\s*\((\d{5,6}),', block_text)
    if not id_m:
        continue
    qid = int(id_m.group(1))
    blocks.append((qid, block_text))

print(f"Parsed {len(blocks)} question blocks")

# ── PARSE QUESTION FIELDS ────────────────────────────────────────────────────
def parse_block(qid, block_text):
    """Return dict with id, question, opts, answer, explanation, folder, subcat"""
    # For single-line inline format, use simpler regex
    # General: extract all quoted strings in order
    # Remove the opening ( and closing )
    inner = re.sub(r'^\s*\(', '', block_text)
    inner = re.sub(r'\)\s*$', '', inner)
    
    # Extract first number (id)
    inner = re.sub(r'^\s*\d{5,6}\s*,\s*', '', inner)
    
    # Extract strings: handle both " and ' delimiters, and multiline
    strings = []
    i = 0
    while i < len(inner) and len(strings) < 9:
        # skip whitespace and commas
        while i < len(inner) and inner[i] in ' \t\n\r,':
            i += 1
        if i >= len(inner): break
        delim = inner[i]
        if delim not in ('"', "'"):
            break
        i += 1
        s = []
        while i < len(inner):
            if inner[i] == '\\' and i+1 < len(inner):
                s.append(inner[i+1])
                i += 2
            elif inner[i] == delim:
                i += 1
                break
            else:
                s.append(inner[i])
                i += 1
        strings.append(''.join(s))
    
    if len(strings) < 7:
        return None
    
    question = strings[0]
    opt_a = strings[1] if len(strings) > 1 else ""
    opt_b = strings[2] if len(strings) > 2 else ""
    opt_c = strings[3] if len(strings) > 3 else ""
    opt_d = strings[4] if len(strings) > 4 else ""
    answer = strings[5] if len(strings) > 5 else "A"
    explanation = strings[6] if len(strings) > 6 else ""
    folder = strings[7] if len(strings) > 7 else "AP_HC"
    subcat = strings[8] if len(strings) > 8 else "National_Current_Affairs_2026"
    
    return {
        'id': qid, 'question': question, 'opt_a': opt_a, 'opt_b': opt_b,
        'opt_c': opt_c, 'opt_d': opt_d, 'answer': answer,
        'explanation': explanation, 'folder': folder, 'subcat': subcat,
        'raw': block_text,
    }

parsed = []
for qid, block in blocks:
    p = parse_block(qid, block)
    if p:
        parsed.append(p)
    else:
        print(f"  PARSE ERROR: ID {qid}")

print(f"Successfully parsed: {len(parsed)} questions")

kept   = [p for p in parsed if p['id'] in KEPT_IDS]
deleted= [p for p in parsed if p['id'] not in KEPT_IDS]
kept.sort(key=lambda x: x['id'])
deleted.sort(key=lambda x: x['id'])
print(f"KEPT: {len(kept)} | DELETED: {len(deleted)}")

# ── WRITE ARCHIVE FILE ──────────────────────────────────────────────────────
with open(ARCHIVE_FILE, 'w', encoding='utf-8') as f:
    f.write(f'"""Archive of {len(deleted)} deleted National CA MCQs — May 2026 curation\nOriginal file: seed_national_ca_2026_mcq.py (791 → 249)\n"""\n\n')
    f.write("DELETED_NATL_MCQS = [\n")
    for p in deleted:
        f.write(f'    {{"id":{p["id"]},"question_text":{repr(p["question"][:80])},"answer":"{p["answer"]}"}},\n')
    f.write("]\n")
print(f"Archive written: {ARCHIVE_FILE}")

# ── WRITE CURATED SEED FILE ─────────────────────────────────────────────────
# Rebuild the seed file keeping only KEPT blocks
kept_ids_set = {p['id'] for p in kept}

new_body_lines = []
for p in kept:
    new_body_lines.append("        " + p['raw'].strip() + ",")

new_seed = header + "\n"
new_seed += "\n".join(new_body_lines)
new_seed += "\n    ]\n" + footer.lstrip()

# Fix the DELETE range in the seed
new_seed = new_seed.replace(
    "DELETE FROM questions WHERE id >= 31001 AND id <= 31799",
    "DELETE FROM questions WHERE id >= 31001 AND id <= 31800"
)

with open(SEED_FILE, 'w', encoding='utf-8') as f:
    f.write(new_seed)
print(f"Curated seed written: {len(kept)} MCQs")

# ── QUICK VERIFY ─────────────────────────────────────────────────────────────
with open(SEED_FILE, encoding='utf-8') as f:
    verify = f.read()
found_ids = re.findall(r'\((\d{5,6}),', verify)
found_ids = [int(i) for i in found_ids if 31000 <= int(i) <= 32000]
print(f"Verification: {len(found_ids)} question IDs in new seed file")

print("\nDONE — archive + seed updated. HTML generation next.")
