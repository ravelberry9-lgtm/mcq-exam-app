#!/usr/bin/env python3
"""
Apply Telugu translations to Batch 10 (MCQs 31676-31725)
Government Schemes MCQs for APPSC exam

Uses web-researched Telugu scheme names and manual translations
"""

import re
import sys
import ast
import shutil
from datetime import datetime

# Tamil/Hindi to Telugu translations for common terms
HINDI_ENGLISH_TO_TELUGU = {
    # Government scheme related words
    'Pradhan Mantri': 'ప్రధానమంత్రి',
    'pradhan mantri': 'ప్రధానమంత్రి',
    'Ujjwala Yojana': 'ఉజ్జ్వల యోజన',
    'ujjwala yojana': 'ఉజ్జ్వల యోజన',
    'Jan Dhan Yojana': 'జన్ ధన్ యోజన',
    'jan dhan yojana': 'జన్ ధన్ యోజన',
    'Kaushal Vikas Yojana': 'కౌశల్ విక్కస్ యోజన',
    'kaushal vikas yojana': 'కౌశల్ విక్కస్ యోజన',
    'Mudra Yojana': 'ముద్ర యోజన',
    'mudra yojana': 'ముద్ర యోజన',
    'Grameen Awas Yojana': 'గ్రామీణ ఆవాస్ యోజన',
    'grameen awas yojana': 'గ్రామీణ ఆవాస్ యోజన',
    'Swachh Bharat': 'స్వచ్ఛ భారత్',
    'swachh bharat': 'స్వచ్ఛ భారత్',
    'Mission': 'మిషన్',
    'mission': 'మిషన్',
    'Scheme': 'యోజన',
    'scheme': 'యోజన',
    'Government': 'ప్రభుత్వ',
    'government': 'ప్రభుత్వ',
    'National': 'జాతీయ',
    'national': 'జాతీయ',
    'Ayushman Bharat': 'ఆయుష్మాన్ భారత్',
    'ayushman bharat': 'ఆయుష్మాన్ భారత్',
}

def safe_read_mcq_lines():
    """Safely read MCQ lines from the file"""
    try:
        with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"ERROR: Could not read seed file: {e}")
        return None

def find_mcq_boundaries():
    """Find line numbers for MCQs 31676-31725"""
    lines = safe_read_mcq_lines()
    if not lines:
        return None

    boundaries = {}
    current_line = 0

    for i, line in enumerate(lines):
        # Look for MCQ tuple start
        match = re.match(r'\s*\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if 31676 <= mcq_id <= 31725:
                boundaries[mcq_id] = {'start': i}

    # Now find end lines for each MCQ
    for i, line in enumerate(lines):
        # Look for closing paren at correct indentation
        if re.match(r'\s*\),\s*$', line):
            # This closes a tuple, try to match with next MCQ start
            pass

    return boundaries

def create_backup():
    """Create backup of original file"""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f'seed_national_ca_2026_mcq.py.bak.{timestamp}'
        shutil.copy2('seed_national_ca_2026_mcq.py', backup_file)
        print(f"Created backup: {backup_file}")
        return backup_file
    except Exception as e:
        print(f"WARNING: Could not create backup: {e}")
        return None

def validate_syntax(filepath):
    """Validate Python file syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        return True, "AST OK"
    except SyntaxError as e:
        return False, f"Syntax Error at line {e.lineno}: {e.msg}"

def main():
    print("=" * 80)
    print("APPLY TELUGU TRANSLATIONS - BATCH 10 (MCQs 31676-31725)")
    print("=" * 80)

    # Validate current file
    print("\n1. Pre-update validation:")
    is_valid, msg = validate_syntax('seed_national_ca_2026_mcq.py')
    print(f"   Current file: {msg}")
    if not is_valid:
        print("   ERROR: Current file has syntax errors, cannot proceed")
        return False

    # Create backup
    print("\n2. Creating backup...")
    backup_file = create_backup()

    # Read file
    print("\n3. Reading MCQs...")
    lines = safe_read_mcq_lines()
    if not lines:
        return False

    # Find MCQs in range
    print("\n4. Locating MCQs 31676-31725...")
    mcq_count = 0
    mcq_ids = []

    for i, line in enumerate(lines):
        match = re.match(r'\s*\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if 31676 <= mcq_id <= 31725:
                mcq_count += 1
                mcq_ids.append(mcq_id)

    print(f"   Found {mcq_count} MCQs in range")
    if mcq_ids:
        print(f"   ID range: {min(mcq_ids)} to {max(mcq_ids)}")

    if mcq_count != 50:
        print(f"   WARNING: Expected 50 MCQs, found {mcq_count}")

    # Show strategy
    print("\n5. Translation Strategy:")
    print("   - Format: 'Telugu translation\\nEnglish original'")
    print("   - Questions: Add bilingual format")
    print("   - Explanations: Add bilingual format")
    print("   - Options A-D: Keep English (scheme names/numbers)")
    print("   - Metadata: folder & topic unchanged")

    print("\n6. Post-update plans:")
    print("   - Validate syntax with AST parser")
    print("   - Show 3 samples (31676, 31700, 31725)")
    print("   - Report: ✓ Batch 10 (31676-31725): 50 MCQs Telugu-ified")

    print("\n" + "=" * 80)
    print("STATUS: Script ready to apply translations")
    print("=" * 80)
    print("\nTo actually update the file, the script needs to:")
    print("1. Parse each MCQ tuple")
    print("2. Extract question and explanation texts")
    print("3. Translate to Telugu (using web search for scheme names)")
    print("4. Reconstruct MCQ with bilingual format")
    print("5. Write back to file")
    print("6. Validate syntax")

    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
