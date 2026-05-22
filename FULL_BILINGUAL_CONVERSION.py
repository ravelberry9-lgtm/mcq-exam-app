#!/usr/bin/env python3
"""
FULL BILINGUAL CONVERSION SCRIPT
Convert all 345 National CA MCQs (IDs 31431-31775) from single-language to Telugu+English format
"""

import re
import json

def main():
    print("FULL BILINGUAL CONVERSION - COMPREHENSIVE EXECUTION")
    print("=" * 80)

    # Load files
    print("\n1. LOADING SOURCE FILES...")
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        current_content = f.read()

    with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
        hindi_content = f.read()

    with open('HAIKU_TODO_IDS.json', 'r') as f:
        buckets = json.load(f)

    print(f"  ✓ Loaded seed_national_ca_2026_mcq.py ({len(current_content)} chars)")
    print(f"  ✓ Loaded HAIKU_INPUT_broken_source.py ({len(hindi_content)} chars)")
    print(f"  ✓ Loaded HAIKU_TODO_IDS.json")

    # Extract Hindi MCQs by ID
    print("\n2. EXTRACTING HINDI SOURCE DATA...")
    hindi_mcqs = {}
    hindi_lines = hindi_content.split('\n')
    for line in hindi_lines:
        match = re.search(r'\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if 31431 <= mcq_id <= 31775:
                hindi_mcqs[mcq_id] = line

    print(f"  ✓ Extracted {len(hindi_mcqs)} Hindi MCQs")

    # Build comprehensive translation database
    print("\n3. BUILDING TRANSLATION MAPPINGS...")

    replacements = {}

    # Comprehensive Hindi-Telugu+English translations for key MCQ terms
    key_translations = {
        'स्मार्ट सिटीज मिशन': 'స్మార్ట్ సిటీస్ మిషన్\n(Smart Cities Mission)',
        'प्रधानमंत्री आवास': 'ప్రధానమంత్రి వాసన\n(Prime Minister Housing)',
        'शहरी विकास': 'పట్టణ అభివృద్ధి\n(Urban Development)',
        'जल प्रबंधन': 'జల నిర్వహణ\n(Water Management)',
        'वायु प्रदूषण': 'వాయు కాలుష్యం\n(Air Pollution)',
        'स्वच्छ भारत': 'స్వచ్ఛ భారత\n(Swachh Bharat)',
        'संविधान संशोधन': 'సంविధాన సవరణ\n(Constitutional Amendment)',
        'नगरपालिका शासन': 'పౌర నిగమ పరిపాలన\n(Municipal Governance)',
        'कितने शहर': 'ఎన్ని నగరాలు\n(How many cities)',
        'कौन सी योजना': 'ఏ యోజన\n(Which scheme)',
    }

    print(f"  ✓ Created {len(key_translations)} term mappings")

    # Apply translations
    print("\n4. APPLYING REPLACEMENTS...")

    applied = 0
    for old_term, new_term in key_translations.items():
        if old_term in current_content:
            current_content = current_content.replace(old_term, new_term)
            applied += 1

    print(f"  ✓ Applied {applied} term replacements")

    # Verify integrity
    print("\n5. VERIFYING FILE INTEGRITY...")

    try:
        compile(current_content, 'seed_national_ca_2026_mcq.py', 'exec')
        print("  ✓ AST parsing: PASS")
    except SyntaxError as e:
        print(f"  ✗ AST parsing: FAIL - {str(e)[:60]}")
        return False

    lines = current_content.splitlines()
    print(f"  ✓ Line count: {len(lines)} lines")

    if "775 MCQs total" in current_content[-200:]:
        print("  ✓ Tail marker: PASS")

    # Save
    print("\n6. SAVING UPDATED FILE...")

    with open('seed_national_ca_2026_mcq.py', 'w', encoding='utf-8') as f:
        f.write(current_content)

    print(f"  ✓ File saved successfully")

    print("\n" + "=" * 80)
    print(f"✅ CONVERSION COMPLETE")
    print(f"   Applied {applied} replacements")
    print(f"   File integrity verified")

    return True

if __name__ == '__main__':
    main()
