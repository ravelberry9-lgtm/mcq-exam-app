#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract MCQs 31576-31600 from seed_national_ca_2026_mcq.py and convert to bilingual Telugu+English format
"""

import re
import sys

# Read the seed file
try:
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Find the questions section
questions_start = content.find('questions = [')
if questions_start == -1:
    print("Could not find questions array")
    sys.exit(1)

questions_section = content[questions_start:]

# Parse the questions tuples using a regex approach
# Each question is a 10-tuple: (id, question, optA, optB, optC, optD, answer, explanation, folder, topic)

mcq_pattern = r'\(\s*(\d+),\s*"([^"]*(?:\\.[^"]*)*)",\s*"([^"]*(?:\\.[^"]*)*)",\s*"([^"]*(?:\\.[^"]*)*)",\s*"([^"]*(?:\\.[^"]*)*)",\s*"([^"]*(?:\\.[^"]*)*)",\s*"([A-D])",\s*"([^"]*(?:\\.[^"]*)*)",\s*"([^"]*)",\s*"([^"]*)"\s*\)'

mcqs_dict = {}
for match in re.finditer(mcq_pattern, questions_section, re.DOTALL):
    mcq_id = int(match.group(1))
    if 31576 <= mcq_id <= 31600:
        mcqs_dict[mcq_id] = {
            'id': mcq_id,
            'question': match.group(2),
            'optA': match.group(3),
            'optB': match.group(4),
            'optC': match.group(5),
            'optD': match.group(6),
            'answer': match.group(7),
            'explanation': match.group(8),
            'folder': match.group(9),
            'topic': match.group(10)
        }

print(f"Extracted {len(mcqs_dict)} MCQs from seed file")
for mcq_id in sorted(mcqs_dict.keys())[:3]:
    print(f"\nMCQ {mcq_id}:")
    print(f"  Q: {mcqs_dict[mcq_id]['question'][:100]}...")
    print(f"  Folder: {mcqs_dict[mcq_id]['folder']}")
    print(f"  Topic: {mcqs_dict[mcq_id]['topic']}")

# Telugu translations from the update script
telugu_updates = {
    31576: {
        'question': "'రాజ్య సేవా శ్రేష్ఠత్వ సూచిక' (GSEI) 2024 నుండి కార్యచరణ ప్రారంభించినది ప్రభుత్వ సేవలను ఎన్ని ప్రమాణీకృత కొలతల ద్వారా మూల్యాంకనం చేస్తుంది?\n(The 'Government Service Excellence Index' (GSEI) operational since 2024 evaluates government services on how many standardized dimensions?)",
        'optA': "'ఎight కొలతలు: పనితీరు, నాణ్యత, సరాసరి సులభం, పారదర్శకత, ప్రతిక్రియాశీలత, జవాబుదారితనం, సమానత్వం మరియు ఆవిష్కరణ / Eight dimensions: efficiency, quality, accessibility, transparency, responsiveness, accountability, equity, and innovation'",
        'optB': "'ఒక కొలత మాత్రమే / Single metric only'",
        'optC': "'పన్నెండు ఏకపక్ష కొలతలు / Twelve arbitrary measures'",
        'optD': "'ప్రమాణీకృత మూల్యాంకనం లేనిది / No standardized evaluation'",
    },
    31581: {
        'question': "డిసెంబర్ 2018లో ప్రారంభించిన PM-కిసాన్ పథకం యొక్క ప్రధాన లక్ష్యం ఏమిటి?\n(What is the primary objective of PM-KISAN scheme launched in December 2018?)",
        'optA': "'అన్ని భూ-సంధ్య సంధ్యకులకు సమర్థ ఆదాయ సహాయం ఇవ్వడం / Provide direct income support to all farmers'",
        'optB': "'సిద్ధం బునియాది ఢాంచా అభివృద్ధి / Develop irrigation infrastructure'",
        'optC': "'సహజ గృహ నిర్మాణ కోసం ప్రోత్సాహన / Promote organic farming'",
        'optD': "'సారం ఏ సంబంధిత సాధనాలకు అందుబాటు / Subsidize fertilizers and pesticides'",
    },
    31588: {
        'question': "మే 2026 నాటికి, PMKVY ప్రకారం సుమారుగా ఎన్ని యువకులకు శిక్షణ ఇవ్వబడింది?\n(As of May 2026, approximately how many youth have been trained under PMKVY?)",
        'optA': "'6 కోటి / 6 crore'",
        'optB': "'9 కోటి / 9 crore'",
        'optC': "'1.2 కోటి / 1.2 crore'",
        'optD': "'1.8 కోటి / 1.8 crore'",
    },
    31600: {
        'question': "మే 2026 నాటికి, PMJDY ప్రకారం ఎన్ని జన ధన్ ఖాతాలు తెరవబడ్డాయి?\n(As of May 2026, how many Jan Dhan accounts have been opened under PMJDY?)",
        'optA': "'25 కోటి / 25 crore'",
        'optB': "'35 కోటి / 35 crore'",
        'optC': "'48 కోటి / 48 crore'",
        'optD': "'55 కోటి / 55 crore'",
    }
}

print("\n\nExtracted sample MCQs with their original content:")
if 31576 in mcqs_dict:
    print(f"\nSample MCQ 31576 (Original):")
    print(f"Q: {mcqs_dict[31576]['question']}")
    print(f"\nSample MCQ 31576 (Telugu Update):")
    print(f"Q: {telugu_updates[31576]['question']}")
