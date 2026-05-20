"""
HTML Parser for MCQ files.
Handles multiple HTML formats:
  - Strategy 1: q-card format (ArtCulture style)
  - Strategy 2: qb/ak format (bilingual Telugu/English style)
  - Strategy 3: Generic numbered MCQ text format
"""

import re
import uuid
from bs4 import BeautifulSoup


def parse_html_file(content, folder, topic):
    """Parse HTML MCQ file and return list of question dicts."""
    soup = BeautifulSoup(content, 'html.parser')

    # ── Strategy 1: q-card format (like ArtCulture HTML) ──
    q_cards = soup.find_all('div', class_='q-card')
    if q_cards:
        questions = _parse_qcard_format(soup, folder, topic)
        if questions:
            return questions

    # ── Strategy 2: qb/ak format (like seating_puzzles bilingual HTML) ──
    qb_cards = soup.find_all('div', class_='qb')
    if qb_cards:
        questions = _parse_qb_format(soup, folder, topic)
        if questions:
            return questions

    # ── Strategy 3: Generic numbered MCQ text format ──
    return _parse_generic_format(soup, folder, topic)


# ─────────────────────────────────────────────
# STRATEGY 1 — q-card / ans-card format
# ─────────────────────────────────────────────
def _parse_qcard_format(soup, folder, topic):
    """Parse the structured q-card + ans-card format."""
    questions = []
    answer_map = {}
    explanation_map = {}

    ans_cards = soup.find_all('div', class_='ans-card')
    for ac in ans_cards:
        num_el = ac.find(class_='ac-num')
        ans_el = ac.find(class_='ac-ans')
        exp_el = ac.find(class_='ac-en')
        if num_el and ans_el:
            try:
                num = int(re.sub(r'[^\d]', '', num_el.get_text()))
                ans_text = ans_el.get_text(strip=True)
                ans_letter = re.search(r'\b([A-Ea-e])\b', ans_text)
                if ans_letter:
                    answer_map[num] = ans_letter.group(1).upper()
                explanation_map[num] = exp_el.get_text(strip=True) if exp_el else ''
            except:
                pass

    q_cards = soup.find_all('div', class_='q-card')
    for i, card in enumerate(q_cards):
        try:
            num_el = card.find(class_='q-num')
            q_el = card.find(class_='q-text')
            opts_el = card.find(class_='q-options')
            if not (q_el and opts_el):
                continue

            q_num = int(re.sub(r'[^\d]', '', num_el.get_text())) if num_el else i + 1
            q_text = q_el.get_text(strip=True)

            difficulty = 'M'
            badge = card.find(lambda tag: tag.name and 'lbadge' in tag.get('class', []))
            if badge:
                classes = badge.get('class', [])
                if 'lb-e' in classes:
                    difficulty = 'E'
                elif 'lb-t' in classes:
                    difficulty = 'T'

            opt_els = opts_el.find_all('div', class_='q-opt')
            opts = {}
            for opt in opt_els:
                span = opt.find('span')
                if span:
                    key = re.sub(r'[^A-Ea-e]', '', span.get_text()).upper()
                    text = opt.get_text(strip=True)
                    text = re.sub(r'^[A-E]\)', '', text).strip()
                    opts[key] = text

            if len(opts) < 4:
                continue

            questions.append({
                'folder': folder,
                'topic': topic,
                'question_text': q_text,
                'option_a': opts.get('A', ''),
                'option_b': opts.get('B', ''),
                'option_c': opts.get('C', ''),
                'option_d': opts.get('D', ''),
                'option_e': opts.get('E'),
                'correct_answer': answer_map.get(q_num, 'A'),
                'difficulty': difficulty,
                'explanation': explanation_map.get(q_num, ''),
                'question_order': q_num
            })
        except Exception:
            continue

    return questions


# ─────────────────────────────────────────────
# STRATEGY 2 — qb/ak bilingual format
# ─────────────────────────────────────────────
def _parse_qb_format(soup, folder, topic):
    """
    Parse the qb/ak bilingual format (e.g. seating_puzzles_50mcq_telugu.html).

    Question:
      <div class="qb easy-q|mod-q|tough-q|toughest-q">
        <div class="qb-head"><span class="q-no">Q1</span></div>
        <div class="qb-body">
          <div class="q-en">English question text</div>
          <div class="opts">
            <div class="opt"><span class="k">A)</span> text</div>
            ...
          </div>
        </div>
      </div>

    Answer key:
      <div class="ak easy-c|mod-c|tough-c|toughest-c">
        <div class="num">Q1</div>
        <div class="ans">A</div>
      </div>
    """
    questions = []

    # Build answer map
    answer_map = {}
    for ak in soup.find_all('div', class_='ak'):
        num_el = ak.find('div', class_='num')
        ans_el = ak.find('div', class_='ans')
        if num_el and ans_el:
            num_text = re.sub(r'[^\d]', '', num_el.get_text())
            ans_text = ans_el.get_text(strip=True).upper()
            if num_text and re.match(r'^[A-E]$', ans_text):
                answer_map[int(num_text)] = ans_text

    # Build explanation map
    explanation_map = {}
    for exp in soup.find_all('div', class_='exp'):
        label_el = exp.find('div', class_='en')
        exp_el = exp.find('div', class_='en-exp')
        if label_el:
            num_match = re.search(r'Q\.?\s*(\d+)', label_el.get_text())
            if num_match and exp_el:
                explanation_map[int(num_match.group(1))] = exp_el.get_text(strip=True)

    diff_map = {
        'easy-q': 'E',
        'mod-q': 'M',
        'tough-q': 'T',
        'toughest-q': 'T',
    }

    for card in soup.find_all('div', class_='qb'):
        try:
            q_no_el = card.find('span', class_='q-no')
            if not q_no_el:
                continue
            q_num = int(re.sub(r'[^\d]', '', q_no_el.get_text()))

            # English question text
            q_en_el = card.find('div', class_='q-en')
            if q_en_el:
                q_text = q_en_el.get_text(strip=True)
            else:
                body_el = card.find('div', class_='qb-body')
                q_text = body_el.get_text(separator=' ', strip=True) if body_el else ''

            if not q_text:
                continue

            # Options — extract key span text then get remaining text
            opts = {}
            for opt_el in card.find_all('div', class_='opt'):
                key_el = opt_el.find('span', class_='k')
                if key_el:
                    key = re.sub(r'[^A-Ea-e]', '', key_el.get_text()).upper()
                    key_el.extract()
                    text = opt_el.get_text(strip=True)
                    if key and text:
                        opts[key] = text

            if len(opts) < 4:
                continue

            # Difficulty from CSS class
            classes = card.get('class', [])
            difficulty = 'M'
            for cls in classes:
                if cls in diff_map:
                    difficulty = diff_map[cls]
                    break

            questions.append({
                'folder': folder,
                'topic': topic,
                'question_text': q_text,
                'option_a': opts.get('A', ''),
                'option_b': opts.get('B', ''),
                'option_c': opts.get('C', ''),
                'option_d': opts.get('D', ''),
                'option_e': opts.get('E'),
                'correct_answer': answer_map.get(q_num, 'A'),
                'difficulty': difficulty,
                'explanation': explanation_map.get(q_num, ''),
                'question_order': q_num
            })
        except Exception:
            continue

    return questions


# ─────────────────────────────────────────────
# STRATEGY 3 — Generic numbered text format
# ─────────────────────────────────────────────
def _parse_generic_format(soup, folder, topic):
    """
    Parse generic HTML MCQ format.
    Looks for patterns like:
    Q1. Question text
    A) option1  B) option2  C) option3  D) option4
    Answer: B
    """
    questions = []
    text = soup.get_text('\n')
    lines = [l.strip() for l in text.split('\n') if l.strip()]

    i = 0
    q_num = 0
    while i < len(lines):
        line = lines[i]

        q_match = re.match(r'^(?:Q\.?\s*)?(\d+)[.)]\s+(.+)', line)
        if q_match:
            q_num = int(q_match.group(1))
            q_text = q_match.group(2).strip()

            i += 1
            while i < len(lines):
                next_line = lines[i]
                if re.match(r'^[A-Ea-e][.)]\s', next_line):
                    break
                if re.match(r'^(?:Q\.?\s*)?\d+[.)]\s', next_line):
                    break
                q_text += ' ' + next_line
                i += 1

            opts = {}
            while i < len(lines):
                opt_match = re.match(r'^([A-Ea-e])[.)]\s*(.+)', lines[i])
                if opt_match:
                    opts[opt_match.group(1).upper()] = opt_match.group(2).strip()
                    i += 1
                else:
                    break

            correct = 'A'
            if i < len(lines):
                ans_match = re.match(r'^(?:Ans(?:wer)?[.:]\s*)([A-Ea-e])', lines[i], re.I)
                if ans_match:
                    correct = ans_match.group(1).upper()
                    i += 1

            if len(opts) >= 4:
                questions.append({
                    'folder': folder,
                    'topic': topic,
                    'question_text': q_text.strip(),
                    'option_a': opts.get('A', ''),
                    'option_b': opts.get('B', ''),
                    'option_c': opts.get('C', ''),
                    'option_d': opts.get('D', ''),
                    'option_e': opts.get('E'),
                    'correct_answer': correct,
                    'difficulty': 'M',
                    'explanation': '',
                    'question_order': q_num
                })
        else:
            i += 1

    return questions
