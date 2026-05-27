"""
PDF Parser for MCQ files.
Handles text-based PDFs with passage groups and standalone questions.
Supports 4-option and 5-option formats.
"""

import re
import uuid
import io
import pdfplumber


def parse_pdf_file(content_bytes, folder, topic):
    """Parse PDF MCQ file and return list of question dicts."""
    questions = []

    try:
        with pdfplumber.open(io.BytesIO(content_bytes)) as pdf:
            full_text = ''
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + '\n'
    except Exception as e:
        return []

    # Try to detect format
    # Format 1: SET-based passage format (Puzzles/Reasoning PDFs)
    if re.search(r'\bSET\s*\d+', full_text, re.I):
        questions = _parse_set_format(full_text, folder, topic)
        if questions:
            return questions

    # Format 2: Numbered Q&A format
    questions = _parse_numbered_format(full_text, folder, topic)
    return questions


def _parse_set_format(text, folder, topic):
    """Parse SET-based passage questions (Reasoning/Puzzles style)."""
    questions = []
    lines = text.split('\n')

    # Split into SETs
    set_pattern = re.compile(r'\bSET\s*(\d+)\b', re.I)
    sets_raw = re.split(r'(?=\bSET\s*\d+\b)', text, flags=re.I)

    for set_block in sets_raw:
        if not re.search(r'\bSET\s*\d+\b', set_block, re.I):
            continue

        set_match = re.search(r'\bSET\s*(\d+)\b', set_block, re.I)
        set_num = set_match.group(1) if set_match else '0'

        # Extract passage (text before first question number)
        q_start = re.search(r'^\s*(?:\d+\.|Q\s*\d+[.)])', set_block, re.M)
        if q_start:
            passage = set_block[:q_start.start()].strip()
            # Clean up the SET header from passage
            passage = re.sub(r'\bSET\s*\d+\b\s*', '', passage, flags=re.I).strip()
        else:
            continue

        if len(passage) < 20:
            continue

        passage_group_id = f"set_{set_num}_{folder}_{topic}"

        # Extract Q&A blocks
        q_blocks = re.split(r'(?=^\s*\d+\.)', set_block[q_start.start():], flags=re.M)

        # Also look for answer section
        answer_map = _extract_answers_from_block(set_block)

        q_local_num = 0
        for qblock in q_blocks:
            q_match = re.match(r'\s*(\d+)\.\s*(.+)', qblock, re.DOTALL)
            if not q_match:
                continue

            global_q_num = int(q_match.group(1))
            rest = q_match.group(2)

            # Split question text from options
            opt_split = re.search(r'\n\s*[a-eA-E][.)]\s', rest)
            if opt_split:
                q_text = rest[:opt_split.start()].strip()
                opts_text = rest[opt_split.start():]
            else:
                # Options on same level
                opt_inline = re.search(r'\s+[a-eA-E][.)]\s', rest)
                if opt_inline:
                    q_text = rest[:opt_inline.start()].strip()
                    opts_text = rest[opt_inline.start():]
                else:
                    continue

            # Clean q_text
            q_text = re.sub(r'\s+', ' ', q_text).strip()
            if len(q_text) < 5:
                continue

            # Parse options
            opts = _parse_options(opts_text)
            if len(opts) < 4:
                continue

            correct = answer_map.get(global_q_num, 'A')

            q_local_num += 1
            questions.append({
                'folder': folder,
                'topic': topic,
                'passage': passage,
                'passage_group_id': passage_group_id,
                'question_text': q_text,
                'option_a': opts.get('A', ''),
                'option_b': opts.get('B', ''),
                'option_c': opts.get('C', ''),
                'option_d': opts.get('D', ''),
                'option_e': opts.get('E'),
                'correct_answer': correct,
                'difficulty': 'M',
                'explanation': '',
                'question_order': global_q_num
            })

    return questions


def _extract_answers_from_block(text):
    """Extract answer key from text like '1. Option A  2. Option B'."""
    answer_map = {}

    # Pattern: "1. Option A" or "1. a)" or "Ans: A"
    patterns = [
        r'(\d+)\.\s+(?:Option\s+)?([A-Ea-e])\b',
        r'(\d+)[.)]\s*(?:Answer|Ans)[.:]\s*([A-Ea-e])\b',
        r'Answer\s+(\d+)[.:]\s*([A-Ea-e])\b',
    ]

    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            q_num = int(m.group(1))
            ans = m.group(2).upper()
            answer_map[q_num] = ans

    return answer_map


def _parse_options(text):
    """Parse A) B) C) D) E) options from text."""
    opts = {}
    # Try newline-separated options first
    pattern = re.compile(r'([A-Ea-e])[.)]\s*(.+?)(?=\n\s*[A-Ea-e][.)]|\Z)', re.DOTALL)
    for m in pattern.finditer(text):
        key = m.group(1).upper()
        val = re.sub(r'\s+', ' ', m.group(2)).strip()
        if val:
            opts[key] = val

    if not opts:
        # Try inline options: A) text B) text
        inline = re.compile(r'([A-Ea-e])[.)]\s*(.+?)(?=\s+[A-Ea-e][.)]|\Z)')
        for m in inline.finditer(text):
            key = m.group(1).upper()
            val = re.sub(r'\s+', ' ', m.group(2)).strip()
            if val:
                opts[key] = val

    return opts


def _parse_numbered_format(text, folder, topic):
    """Parse standard numbered Q&A format."""
    questions = []
    lines = text.split('\n')

    i = 0
    answer_section = False
    answer_map = {}

    # First pass: look for answer key section
    for j, line in enumerate(lines):
        if re.search(r'\b(answer\s*key|answers?)\b', line, re.I) and j > len(lines) // 2:
            answer_section_text = '\n'.join(lines[j:])
            answer_map = _extract_answers_from_block(answer_section_text)
            break

    # Second pass: parse questions
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        q_match = re.match(r'^(?:Q\.?\s*)?(\d+)[.)]\s+(.+)', line)
        if q_match:
            q_num = int(q_match.group(1))
            q_text = q_match.group(2).strip()

            i += 1
            # Multi-line question
            while i < len(lines):
                nl = lines[i].strip()
                if not nl:
                    i += 1
                    break
                if re.match(r'^[A-Ea-e][.)]\s', nl):
                    break
                if re.match(r'^(?:Q\.?\s*)?\d+[.)]\s', nl):
                    break
                q_text += ' ' + nl
                i += 1

            # Collect options
            opts_text = ''
            while i < len(lines):
                nl = lines[i].strip()
                opt_match = re.match(r'^([A-Ea-e])[.)]\s', nl)
                if opt_match:
                    opts_text += nl + '\n'
                    i += 1
                elif opts_text and not nl:
                    i += 1
                    break
                else:
                    break

            opts = _parse_options(opts_text)

            # Get answer
            correct = answer_map.get(q_num, 'A')
            if not answer_map:
                # Look ahead for inline answer
                if i < len(lines):
                    ans_match = re.match(r'^(?:Ans(?:wer)?[.:]\s*)([A-Ea-e])', lines[i].strip(), re.I)
                    if ans_match:
                        correct = ans_match.group(1).upper()
                        i += 1

            if len(opts) >= 4 and q_text:
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
