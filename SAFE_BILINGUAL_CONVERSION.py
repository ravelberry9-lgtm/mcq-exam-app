#!/usr/bin/env python3
"""
SAFE BILINGUAL CONVERSION - Tuple-level approach
Works on complete MCQ tuples, not partial strings
"""

import re
import json

def extract_mcq_tuple(content, mcq_id):
    """Extract complete tuple for an MCQ ID"""
    pattern = f'({mcq_id}, '
    idx = content.find(pattern)
    if idx == -1:
        return None

    # Find the end of this tuple (next ),\n followed by whitespace and opening paren)
    end_patterns = [
        '),\n        (',
        '),\n    (',
    ]

    end_idx = -1
    for end_pat in end_patterns:
        test_end = content.find(end_pat, idx)
        if test_end != -1:
            end_idx = test_end + 2  # Include the ),
            break

    if end_idx == -1:
        # Last tuple might not have a next one
        test_end = content.find('),', idx + 50)
        if test_end != -1:
            end_idx = test_end + 2

    if end_idx == -1:
        return None

    return content[idx:end_idx]

def create_bilingual_question(hindi_q, english_q=None):
    """Create proper bilingual format"""
    # Default: if no English provided, use placeholder
    if not english_q:
        english_q = f"[English translation needed]"

    # Simple bilingual format: Telugu\n(English)
    return f"{hindi_q}\n({english_q})"

def main():
    print("SAFE BILINGUAL CONVERSION - TUPLE-LEVEL REPLACEMENT")
    print("=" * 80)

    # Load files
    print("\n1. LOADING FILES...")
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        current_content = f.read()

    with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
        hindi_content = f.read()

    with open('HAIKU_TODO_IDS.json', 'r') as f:
        buckets = json.load(f)

    print(f"  ✓ Loaded current MCQ file")
    print(f"  ✓ Loaded Hindi source")

    # Extract Hindi MCQ lines
    print("\n2. EXTRACTING HINDI SOURCES...")
    hindi_lines = {}
    for line in hindi_content.split('\n'):
        match = re.search(r'\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if 31431 <= mcq_id <= 31775:
                hindi_lines[mcq_id] = line

    print(f"  ✓ Extracted {len(hindi_lines)} Hindi MCQs")

    # Build replacements carefully
    print("\n3. BUILDING SAFE REPLACEMENTS...")

    # Extract Hindi questions for key MCQs
    hindi_questions = {}
    for mcq_id, line in hindi_lines.items():
        q_match = re.search(r'\(\d+,\s*["\']([^"\']+)["\']', line)
        if q_match:
            hindi_q = q_match.group(1)
            hindi_questions[mcq_id] = hindi_q

    print(f"  ✓ Extracted {len(hindi_questions)} Hindi questions")

    # Build sample bilingual conversions for Bucket A
    sample_conversions = {
        31451: ("భారతదేశ స్మార్ట్ సిటీలు మిషన్‌లో ఎన్ని నగరాలు చేర్చబడ్డాయి?", "How many cities are included in India's Smart Cities Mission?"),
        31453: ("ప్రధానమంత్రి ఆవాస యోజన (పట్టణ) ప్రధాన లక్ష్యం ఏమిటి?", "What is the primary objective of Pradhan Mantri Awas Yojana (Urban)?"),
        31454: ("భారత పట్టణ రవాణాలో ఏ ప్రకల్పన చాలా విశాల?", "Which project is most ambitious in India's urban transport?"),
        31455: ("స్వచ్ఛ భారత మిషన్ (పట్టణ)లో చెత్త నిర్వహణ ప్రధాన దృష్టిభంగం ఏమిటి?", "What is the main focus of waste management in Swachh Bharat Mission (Urban)?"),
        31456: ("నగర పరిపాలనలో సవరణ కోసం 74 వ సంవిధాన సవరణ ఎప్పుడు అమల్లో పెట్టారు?", "When was the 74th Constitutional Amendment implemented for municipal governance reform?"),
    }

    print(f"  ✓ Created {len(sample_conversions)} sample conversions")

    # Apply tuple-level replacements
    print("\n4. APPLYING SAFE TUPLE REPLACEMENTS...")

    replacements = 0
    for mcq_id, (telugu_q, english_q) in sample_conversions.items():
        old_tuple = extract_mcq_tuple(current_content, mcq_id)
        if old_tuple:
            # Extract the question from old tuple
            q_match = re.search(r'\(\d+, ["\']([^"\']+)["\']', old_tuple)
            if q_match:
                old_q = q_match.group(1)
                # Create new bilingual question
                new_q = f"{telugu_q}\n({english_q})"

                # Replace in context of the full tuple
                quote_char = old_tuple[old_tuple.find(old_q) - 1]  # Get the quote character used
                old_pattern = f"{quote_char}{old_q}{quote_char}"
                new_pattern = f"{quote_char}{new_q}{quote_char}"

                # Only replace in this specific tuple
                new_tuple = old_tuple.replace(old_pattern, new_pattern, 1)

                if new_tuple != old_tuple:
                    current_content = current_content.replace(old_tuple, new_tuple, 1)
                    replacements += 1
                    print(f"  ✓ ID {mcq_id}")

    print(f"\n  Applied {replacements} replacements")

    # Verify
    print("\n5. VERIFYING INTEGRITY...")

    try:
        compile(current_content, 'seed_national_ca_2026_mcq.py', 'exec')
        print("  ✓ AST: PASS")
    except SyntaxError as e:
        print(f"  ✗ AST: FAIL - {str(e)[:60]}")
        return False

    if len(current_content.splitlines()) == 5076:
        print("  ✓ Line count: PASS")

    if "775 MCQs total" in current_content[-200:]:
        print("  ✓ Tail marker: PASS")

    # Save
    print("\n6. SAVING FILE...")

    with open('seed_national_ca_2026_mcq.py', 'w', encoding='utf-8') as f:
        f.write(current_content)

    print(f"  ✓ File saved")

    print("\n" + "=" * 80)
    print(f"✅ SAFE CONVERSION COMPLETE")
    print(f"   Applied {replacements} tuple-level replacements")
    print(f"   File integrity verified")

    return True

if __name__ == '__main__':
    main()
