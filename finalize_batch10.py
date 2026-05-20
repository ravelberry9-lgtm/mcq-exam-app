#!/usr/bin/env python3
"""
Fix Batch 10 (MCQs 31676-31725) - Add Telugu translations
Government Schemes focus for APPSC examination

Strategy:
1. Extract MCQs from seed file
2. Add Telugu translations to questions and explanations
3. Keep options in English (scheme names/numbers)
4. Validate with AST parsing
"""

import re
import ast

def read_seed_file():
    """Read the seed file and extract raw content"""
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        return f.read()

def validate_python_syntax(filepath):
    """Validate that a Python file has correct syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        return True, "AST OK"
    except SyntaxError as e:
        return False, f"Syntax Error: {e}"

def create_bilingual_question(english_q, telugu_q):
    """Format question as bilingual: Telugu\nEnglish"""
    return f"{telugu_q}\n{english_q}"

def create_bilingual_explanation(english_exp, telugu_exp):
    """Format explanation as bilingual: Telugu\nEnglish"""
    return f"{telugu_exp}\n{english_exp}"

# Government schemes information for batch 10 (these are examples)
# In production, these would be researched for actual MCQ IDs 31676-31725
SCHEME_TRANSLATIONS = {
    # Example structure - actual MCQs need specific scheme names
    # 'Scheme Name (English)': ('Scheme Name (Telugu)', 'Abbreviated Telugu')
    'Pradhan Mantri Kaushal Vikas Yojana': ('ప్రధానమంత్రి కౌశల్ విక్కస్ యోజన', 'PMKVY'),
    'Swachh Bharat Mission': ('స్వచ్ఛ భారత్ మిషన్', 'SBM'),
    'Pradhan Mantri Ujjwala Yojana': ('ప్రధానమంత్రి ఉజ్జ్వల యోజన', 'PMUY'),
    'Pradhan Mantri Jan Dhan Yojana': ('ప్రధానమంత్రి జన్ ధన్ యోజన', 'PMJDY'),
    'Ayushman Bharat': ('ఆయుష్మాన్ భారత్', 'AB'),
    'National Health Mission': ('జాతీయ ఆరోగ్య మిషన్', 'NHM'),
    'Pradhan Mantri Fasal Bima Yojana': ('ప్రధానమంత్రి ఫసల్ బీమా యోజన', 'PMFBY'),
    'National Rural Livelihood Mission': ('జాతీయ గ్రామీణ జీవనోపాధి మిషన్', 'NRLM'),
}

def main():
    print("=" * 70)
    print("BATCH 10 TELUGU TRANSLATOR - MCQs 31676-31725")
    print("=" * 70)

    # Read the seed file
    content = read_seed_file()
    print(f"\n1. Read seed file: seed_national_ca_2026_mcq.py")
    print(f"   File size: {len(content)} bytes")

    # Find MCQs in range
    mcq_pattern = r'\(\s*(\d{5}),'
    matches = list(re.finditer(mcq_pattern, content))

    target_mcqs = []
    for match in matches:
        mcq_id = int(match.group(1))
        if 31676 <= mcq_id <= 31725:
            target_mcqs.append(mcq_id)

    print(f"\n2. Found {len(target_mcqs)} MCQs in range 31676-31725")
    if target_mcqs:
        target_mcqs.sort()
        print(f"   ID range: {min(target_mcqs)} to {max(target_mcqs)}")

    # NOTE: At this point, we would:
    # 1. Extract each MCQ tuple
    # 2. Identify the question and explanation text
    # 3. Get Telugu translations (either from web or from a translation table)
    # 4. Format as bilingual
    # 5. Reconstruct the tuple
    # 6. Replace in the original file
    # 7. Validate syntax

    print(f"\n3. Translation process:")
    print(f"   - Each question: 'Telugu version\\nEnglish version'")
    print(f"   - Each explanation: 'Telugu version\\nEnglish version'")
    print(f"   - Options A-D: Remain in English (scheme names/numbers only)")
    print(f"   - folder='AP_HC', topic='National_Current_Affairs_2026': Unchanged")
    print(f"   - Answer key: Unchanged")

    print(f"\n4. Sample MCQ format after translation:")
    print(f"   Original: (31676, \"Which scheme...\", \"A) ...\", ...)")
    print(f"   Updated:  (31676, \"కేటలోగ్ ఇక్కడ...\\nWhich scheme...\", \"A) ...\", ...)")

    print(f"\n5. AST Validation: Will be performed after updates")
    print(f"   Command: python -c \"import ast; ast.parse(open(...).read()); print('AST OK')\"")

    return True

if __name__ == '__main__':
    success = main()
    print("\n" + "=" * 70)
    print("NEXT STEPS:")
    print("=" * 70)
    print("""
1. Identify the actual government schemes in MCQs 31676-31725
2. Research Telugu names for each scheme (using web search if needed)
3. Generate bilingual questions and explanations
4. Update the seed file with new format
5. Validate syntax with AST parser
6. Show 3 sample MCQs (31676, 31700, 31725) in output
    """)
