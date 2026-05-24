"""
generate_natl_html.py
Generates 2 HTML MCQ files from the curated seed_national_ca_2026_mcq.py
Output:  static/notes/Indian_Current_Affairs/Divisions/natl_mcqs_part1.html  (126 Qs)
         static/notes/Indian_Current_Affairs/Divisions/natl_mcqs_part2.html  (126 Qs)
"""
import re, os, html as htmlmod

SEED_FILE = "seed_national_ca_2026_mcq.py"
OUT_DIR   = "static/notes/Indian_Current_Affairs/Divisions"

# ── PARSE ──────────────────────────────────────────────────────────────────
with open(SEED_FILE, encoding="utf-8") as f:
    raw = f.read()

def extract_strings(inner):
    """Extract ordered list of string values from a tuple body (after id removed)."""
    strings = []
    i = 0
    while i < len(inner) and len(strings) < 9:
        while i < len(inner) and inner[i] in ' \t\n\r,':
            i += 1
        if i >= len(inner): break
        delim = inner[i]
        if delim not in ('"', "'"): break
        i += 1
        s = []
        while i < len(inner):
            if inner[i] == '\\' and i+1 < len(inner):
                esc = inner[i+1]
                if esc == 'n': s.append('\n')
                elif esc == 't': s.append('\t')
                else: s.append(esc)
                i += 2
            elif inner[i] == delim:
                i += 1
                break
            else:
                s.append(inner[i])
                i += 1
        strings.append(''.join(s))
    return strings

# Find all question positions using both formats
q_pos = [(m.start(), int(m.group(1))) for m in
         re.finditer(r'(?:^|\n)\s+\((\d{5,6}),', raw) if 31000 <= int(m.group(1)) <= 32000]
q_pos.sort()

questions = []
for idx, (pos, qid) in enumerate(q_pos):
    end = q_pos[idx+1][0] if idx+1 < len(q_pos) else len(raw)
    block = raw[pos:end]
    inner = re.sub(r'^\s*\(\d{5,6}\s*,\s*', '', block.strip().rstrip(',)').strip())
    strings = extract_strings(inner)
    if len(strings) < 7:
        continue
    q_text  = strings[0]
    opt_a   = strings[1]
    opt_b   = strings[2]
    opt_c   = strings[3]
    opt_d   = strings[4]
    answer  = strings[5]
    expl    = strings[6]

    # Split bilingual question: English (after \n(...) ) vs Telugu
    if '\n(' in q_text:
        parts = q_text.split('\n(', 1)
        tel_q = parts[0].strip()
        eng_q = parts[1].rstrip(')').strip()
    else:
        eng_q = q_text.strip()
        tel_q = ""

    # Correct answer text
    opts = {'A': opt_a, 'B': opt_b, 'C': opt_c, 'D': opt_d}
    correct_text = opts.get(answer, "")

    # Explanation: extract English part (usually after first sentence or full)
    # Strip Telugu characters roughly: keep lines that are mostly ASCII
    expl_lines = expl.split('\n')
    eng_lines = []
    for line in expl_lines:
        non_ascii = sum(1 for c in line if ord(c) > 127)
        total = len(line.strip())
        if total == 0: continue
        if non_ascii / max(total, 1) < 0.4:  # <40% non-ASCII → keep
            eng_lines.append(line.strip())
    eng_expl = ' '.join(eng_lines).strip() if eng_lines else expl[:300]

    questions.append({
        'id': qid, 'eng_q': eng_q, 'tel_q': tel_q,
        'opt_a': opt_a, 'opt_b': opt_b, 'opt_c': opt_c, 'opt_d': opt_d,
        'answer': answer, 'correct_text': correct_text,
        'expl': eng_expl,
    })

questions.sort(key=lambda x: x['id'])
print(f"Total parsed: {len(questions)} questions")

# ── DIFFICULTY TAG (simple heuristic) ──────────────────────────────────────
def difficulty(q):
    expl_len = len(q['expl'])
    if expl_len < 150: return 'E', 'easy'
    if expl_len < 350: return 'M', 'moderate'
    return 'T', 'tough'

# ── HTML TEMPLATE ───────────────────────────────────────────────────────────
CSS = """<style>
@page{size:A4;margin:15mm 14mm;}
@media print{.page-break{page-break-before:always;}.no-break{page-break-inside:avoid;}body{background:#fff!important;}}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
:root{--a4:794px;--mud:#6b4226;--green:#1a5030;--easy:#1a5030;--moderate:#5a3400;--tough:#8a1a1a;
--easy-bg:#edf7f0;--moderate-bg:#fffbec;--tough-bg:#fff0f0;
--text:#1a1206;--border:#d4b896;--tel-bg:#eef4ff;--tel-bdr:#1a3e7a;}
body{font-family:'Libre Baskerville',Georgia,serif;background:#ddd5c8;color:var(--text);font-size:10pt;line-height:1.6;}
.a4-page{width:var(--a4);min-height:1123px;background:#fff;margin:18px auto;padding:13mm 14mm 12mm;box-shadow:0 2px 18px rgba(0,0,0,.18);}
.screen-header{display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid var(--border);padding-bottom:5px;margin-bottom:10px;}
.sh-left{font-family:'Source Sans 3',sans-serif;font-size:7pt;font-weight:700;letter-spacing:.04em;}
.sh-right{font-family:'Fira Mono',monospace;font-size:7pt;font-weight:600;}
.mcq-title{padding:14px 18px;border-radius:4px;margin-bottom:12px;color:#fff;}
.mcq-title h1{font-size:13pt;font-weight:700;margin-bottom:4px;}
.te-title{font-family:'Noto Serif Telugu','Tiro Telugu',serif;font-size:10.5pt;margin-bottom:8px;display:block;}
.mcq-meta{display:flex;gap:12px;flex-wrap:wrap;}
.mcq-meta span{font-family:'Fira Mono',monospace;font-size:7pt;background:rgba(255,255,255,.15);padding:2px 8px;border-radius:2px;}
.legend{display:flex;gap:10px;margin-bottom:10px;flex-wrap:wrap;}
.leg-item{display:flex;align-items:center;gap:5px;font-family:'Source Sans 3',sans-serif;font-size:8pt;font-weight:600;}
.leg-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;}
.sec-block{color:#fff;padding:6px 12px;border-radius:3px;margin:14px 0 8px;display:flex;justify-content:space-between;align-items:center;}
.sec-block h2{font-family:'Source Sans 3',sans-serif;font-size:10pt;font-weight:700;text-transform:uppercase;letter-spacing:.06em;}
.te-sec{font-family:'Noto Serif Telugu','Tiro Telugu',serif;font-size:9pt;opacity:.85;}
.sec-count{font-family:'Fira Mono',monospace;font-size:7.5pt;opacity:.85;}
.q-card{margin-bottom:7px;border:1px solid var(--border);border-radius:4px;overflow:hidden;}
.q-card.easy{border-left:4px solid var(--easy);}
.q-card.moderate{border-left:4px solid var(--moderate);}
.q-card.tough{border-left:4px solid var(--tough);}
.q-header{display:flex;align-items:flex-start;gap:8px;padding:6px 9px;background:#fffdf9;border-bottom:1px solid #eee0cc;}
.q-num{font-family:'Fira Mono',monospace;font-size:8pt;font-weight:700;color:#fff;background:var(--mud);padding:1px 6px;border-radius:2px;flex-shrink:0;margin-top:1px;}
.tag-diff{font-family:'Fira Mono',monospace;font-size:6.5pt;font-weight:700;padding:1px 5px;border-radius:2px;margin-top:1px;flex-shrink:0;}
.tag-diff.E{background:var(--easy-bg);color:var(--easy);border:1px solid #70b890;}
.tag-diff.M{background:var(--moderate-bg);color:var(--moderate);border:1px solid #c8a830;}
.tag-diff.T{background:var(--tough-bg);color:var(--tough);border:1px solid #c85030;}
.q-text{font-size:9.5pt;line-height:1.5;flex:1;}
.q-te{font-family:'Noto Serif Telugu','Tiro Telugu',serif;font-size:9pt;color:#1a3e7a;display:block;margin-top:2px;}
.q-body{padding:5px 9px 7px;}
.q-options{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:3px 10px;}
.q-options li{font-size:9pt;display:flex;align-items:baseline;gap:4px;}
.opt-label{font-family:'Fira Mono',monospace;font-size:8pt;font-weight:700;color:var(--mud);flex-shrink:0;}
.exp-section{margin-top:18px;border-top:2px solid var(--border);padding-top:10px;}
.exp-section-title{font-family:'Source Sans 3',sans-serif;font-size:11pt;font-weight:700;color:var(--mud);margin-bottom:10px;text-transform:uppercase;letter-spacing:.05em;}
.exp-card{margin-bottom:7px;border:1px solid var(--border);border-radius:4px;overflow:hidden;}
.exp-card.easy{border-left:4px solid var(--easy);}
.exp-card.moderate{border-left:4px solid var(--moderate);}
.exp-card.tough{border-left:4px solid var(--tough);}
.exp-header{display:flex;align-items:center;gap:8px;padding:4px 9px;background:#fffdf9;border-bottom:1px solid #eee0cc;}
.exp-qnum{font-family:'Fira Mono',monospace;font-size:8pt;font-weight:700;color:#fff;background:var(--mud);padding:1px 6px;border-radius:2px;flex-shrink:0;}
.exp-ans-wrap{display:flex;align-items:baseline;gap:4px;flex:1;}
.exp-ans-label{font-family:'Source Sans 3',sans-serif;font-size:7.5pt;font-weight:700;color:var(--green);}
.exp-ans{font-size:8.5pt;font-weight:600;color:var(--green);}
.exp-body{padding:5px 9px 7px;}
.exp-te{font-size:9pt;line-height:1.55;}
.exp-te strong,.exp-te b{color:var(--mud);}
.page-break{page-break-before:always;height:0;}
</style>"""

GOOGLE_FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&family=Fira+Mono:wght@400;700&family=Tiro+Telugu&family=Noto+Serif+Telugu&display=swap" rel="stylesheet">"""

def bold_md(text):
    """Convert **bold** markdown to <strong> tags."""
    text = htmlmod.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return text

def render_opt(opt_text):
    """Strip leading 'A) ' etc and render option text."""
    opt_text = re.sub(r'^[A-D]\)\s*', '', opt_text)
    return htmlmod.escape(opt_text)

def render_question_card(q_num, q, diff_tag, diff_class):
    eng = htmlmod.escape(q['eng_q'])
    tel = htmlmod.escape(q['tel_q']) if q['tel_q'] else ""
    tel_span = f'<span class="q-te">{tel}</span>' if tel else ""
    
    opts_html = ""
    for opt_key, opt_val in [('A',q['opt_a']),('B',q['opt_b']),('C',q['opt_c']),('D',q['opt_d'])]:
        opt_val_clean = re.sub(r'^[A-D]\)\s*', '', opt_val)
        opts_html += f'<li><span class="opt-label">{opt_key})</span> {htmlmod.escape(opt_val_clean)}</li>'
    
    return f'''<div class="q-card {diff_class} no-break"><div class="q-header"><div class="q-num">Q{q_num}</div><span class="tag-diff {diff_tag}">{diff_tag}</span><div class="q-text" style="margin-left:6px">{eng}{tel_span}</div></div><div class="q-body"><ul class="q-options">{opts_html}</ul></div></div>'''

def render_exp_card(q_num, q, diff_tag, diff_class):
    ans_text = re.sub(r'^[A-D]\)\s*', '', q['correct_text'])
    expl_html = bold_md(q['expl'])
    return f'''<div class="exp-card {diff_class} no-break"><div class="exp-header"><div class="exp-qnum">Q{q_num}</div><span class="tag-diff {diff_tag}" style="margin-top:0">{diff_tag}</span><div class="exp-ans-wrap"><span class="exp-ans-label">Ans:</span><span class="exp-ans">{q["answer"]}) {htmlmod.escape(ans_text)}</span></div></div><div class="exp-body"><div class="exp-te">{expl_html}</div></div></div>'''

def build_html(title_en, title_te, qs, part_num, total_parts):
    n = len(qs)
    id_lo = qs[0]['id']
    id_hi = qs[-1]['id']
    grad = "linear-gradient(135deg,#1a3e7a,#0e2454)" if part_num == 1 else "linear-gradient(135deg,#1a5030,#0e3020)"
    
    q_cards = []
    e_cards = []
    for i, q in enumerate(qs, 1):
        dtag, dcls = difficulty(q)
        q_cards.append(render_question_card(i, q, dtag, dcls))
        e_cards.append(render_exp_card(i, q, dtag, dcls))
    
    q_section = "\n".join(q_cards)
    e_section = "\n".join(e_cards)
    
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>National CA MCQs Part {part_num}</title>
{GOOGLE_FONTS}
{CSS}
</head><body>
<div class="a4-page">
<div class="screen-header"><span class="sh-left">NATIONAL CA 2026 · MCQ PART {part_num} OF {total_parts} · CURATED 252 Qs · {n} Qs</span><span class="sh-right">AP HIGH COURT SO 2026</span></div>
<div class="mcq-title" style="background:{grad}"><h1>MCQ Part {part_num} — {title_en}</h1><span class="te-title">{title_te}</span><div class="mcq-meta"><span>Total: {n} Questions</span><span>Seed IDs: {id_lo}–{id_hi}</span><span>Curated May 2026</span></div></div>
<div class="legend"><div class="leg-item"><div class="leg-dot" style="background:var(--easy);"></div><span style="color:var(--easy);">E=Easy</span></div><div class="leg-item"><div class="leg-dot" style="background:var(--moderate);"></div><span style="color:var(--moderate);">M=Moderate</span></div><div class="leg-item"><div class="leg-dot" style="background:var(--tough);"></div><span style="color:var(--tough);">T=Tough</span></div></div>
{q_section}
<div class="page-break"></div>
<div class="exp-section"><div class="exp-section-title">Explanations &amp; Answer Key — Part {part_num}</div>
{e_section}
</div>
</div></body></html>"""

# ── SPLIT & WRITE ──────────────────────────────────────────────────────────
mid = len(questions) // 2
part1 = questions[:mid]
part2 = questions[mid:]

html1 = build_html(
    "Budget | Economy | Defence | ISRO | Sports | Awards",
    "బడ్జెట్ | ఆర్థిక వ్యవస్థ | రక్షణ | ISRO | క్రీడలు | అవార్డులు",
    part1, 1, 2
)
html2 = build_html(
    "Governance | Schemes | Elections | Nobel | Art & Culture",
    "పాలన | పథకాలు | ఎన్నికలు | నోబెల్ | కళ & సంస్కృతి",
    part2, 2, 2
)

os.makedirs(OUT_DIR, exist_ok=True)
out1 = os.path.join(OUT_DIR, "natl_mcqs_part1.html")
out2 = os.path.join(OUT_DIR, "natl_mcqs_part2.html")

with open(out1, 'w', encoding='utf-8') as f: f.write(html1)
with open(out2, 'w', encoding='utf-8') as f: f.write(html2)

print(f"Part 1: {len(part1)} MCQs → {out1}  ({os.path.getsize(out1)//1024}KB)")
print(f"Part 2: {len(part2)} MCQs → {out2}  ({os.path.getsize(out2)//1024}KB)")
print("DONE.")
