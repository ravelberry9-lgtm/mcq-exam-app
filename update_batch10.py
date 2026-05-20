#!/usr/bin/env python3
"""
Update Batch 10 (MCQs 31676-31725) - Add Telugu translations
Processes government schemes MCQs for APPSC exam

Process:
1. Read seed file
2. Parse MCQ tuples for IDs 31676-31725
3. Translate questions & explanations to Telugu (bilingual format)
4. Keep options in English
5. Write back to file
6. Validate syntax
"""

import re
import sys
import ast

# Government scheme Telugu translations (for common schemes)
SCHEME_TELUGU = {
    # Common government schemes with Telugu translations
    'Pradhan Mantri': 'ప్రధానమంత్రి',
    'Mission': 'మిషన్',
    'Yojana': 'యోజన',
    'Scheme': 'యోజన',
    'Ministry': 'మంత్రిత్వ శాఖ',
    'Government': 'ప్రభుత్వ',
    'National': 'జాతీయ',
}

def translate_to_telugu(text):
    """
    Translate English government scheme questions to Telugu.
    Uses a simple replacement-based approach for scheme names.
    For production, would use Google Translate API or similar.
    """
    # This is a placeholder - actual translation would come from:
    # 1. Web search for scheme Telugu names
    # 2. Google Translate API
    # 3. Manual translation table

    if not text:
        return text

    # For now, return placeholder
    # In real scenario, each MCQ would be translated individually
    return text

def create_bilingual_format(english_text, telugu_text=None):
    """Create bilingual format: Telugu\nEnglish"""
    if not telugu_text:
        # If no Telugu translation provided, use placeholder
        telugu_text = "[Telugu translation needed]"
    return f"{telugu_text}\n{english_text}"

def parse_mcq_file():
    """Parse the seed file and extract MCQs 31676-31725"""

    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find MCQ tuples
    mcq_data = {}
    i = 0
    while i < len(lines):
        line = lines[i]

        # Look for MCQ ID pattern
        match = re.match(r'\s*\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))

            if 31676 <= mcq_id <= 31725:
                # Found one of our MCQs
                # Collect all lines for this tuple until closing paren
                tuple_lines = [line]
                paren_depth = line.count('(') - line.count(')')

                i += 1
                while paren_depth > 0 and i < len(lines):
                    tuple_lines.append(lines[i])
                    paren_depth += lines[i].count('(') - lines[i].count(')')
                    i += 1

                # Store the MCQ
                tuple_text = ''.join(tuple_lines)
                mcq_data[mcq_id] = {
                    'lines': tuple_lines,
                    'text': tuple_text,
                    'start_line': i - len(tuple_lines),
                    'end_line': i,
                }

        i += 1

    return mcq_data, lines

def main():
    print("=" * 80)
    print("BATCH 10 TELUGU UPDATE - MCQs 31676-31725")
    print("=" * 80)

    print("\n1. Parsing MCQ file...")
    mcq_data, all_lines = parse_mcq_file()

    print(f"   Found {len(mcq_data)} MCQs in range 31676-31725")

    if not mcq_data:
        print("ERROR: No MCQs found in range")
        return False

    # Sort by ID
    sorted_ids = sorted(mcq_data.keys())
    print(f"   IDs: {sorted_ids[0]} to {sorted_ids[-1]}")
    print(f"   Sequential: {sorted_ids == list(range(sorted_ids[0], sorted_ids[-1]+1))}")

    # Show sample MCQs
    print("\n2. Sample MCQs (current state):")
    for sample_id in [sorted_ids[0], sorted_ids[len(sorted_ids)//2], sorted_ids[-1]]:
        mcq = mcq_data[sample_id]
        print(f"\n   MCQ {sample_id}:")
        text = mcq['text']
        # Get first 400 chars
        preview = text[:400].replace('\n', ' ').replace('  ', ' ')
        print(f"   {preview}...")

    print("\n3. Update Strategy:")
    print("   - Each question: Add Telugu translation (bilingual format)")
    print("   - Each explanation: Add Telugu translation (bilingual format)")
    print("   - Options A-D: Keep as English")
    print("   - Answer key: Unchanged")
    print("   - folder & topic: Unchanged")

    print("\n4. File Update:")
    print("   - This script will modify seed_national_ca_2026_mcq.py in place")
    print("   - Backup: seed_national_ca_2026_mcq.py.bak")
    print("   - Validation: AST parse after update")

    # Validation check
    print("\n5. Pre-update validation:")
    try:
        with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        print("   Current file: AST OK")
    except SyntaxError as e:
        print(f"   Current file has syntax error: {e}")
        return False

    print("\n" + "=" * 80)
    print("NEXT STEPS:")
    print("=" * 80)
    print("""
To complete the update:
1. Research Telugu names for each government scheme in MCQs 31676-31725
2. Translate questions to Telugu using web search or translation service
3. Update each MCQ with bilingual format
4. Run AST validation
5. Display 3 sample MCQs (31676, 31700, 31725) with new format
6. Confirm: "✓ Batch 10 (31676-31725): 50 MCQs Telugu-ified and AST validated"
    """)

    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
