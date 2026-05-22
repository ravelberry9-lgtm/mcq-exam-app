#!/usr/bin/env python3
"""
BUCKET A CONVERSION: Hindi → Telugu+English
IDs: 31451-31475, 31510, 31581-31615, 31736-31775 (101 total)

Strategy: Extract Hindi from HAIKU_INPUT_broken_source.py and create bilingual format
"""

import re
import json

# Comprehensive Hindi→Telugu term mappings
HINDI_TELUGU_DICT = {
    # Cities & Urban
    'शहर': 'నగర',
    'शहरी': 'పట్టణ',
    'शहरों': 'నగరాల్లో',
    'शहरों में': 'నగరాల్లో',
    'नगर': 'నగర',
    'नगरों': 'నగరాల',

    # Housing
    'आवास': 'గృహం',
    'आवास योजना': 'గృహ యోజన',
    'प्रधानमंत्री आवास': 'ప్రధానమంత్రి గృహ',
    'घर': 'ఇల్లు',
    'मकान': 'ఇల్లు',

    # Infrastructure & Transport
    'परिवहन': 'రవాణా',
    'सड़क': 'రోడ్డు',
    'सड़कों': 'రోడ్ల',
    'मेट्रो': 'మెట్రో',
    'बस': 'బస్',
    'रेल': 'రైలు',
    'जल': 'నీరు',
    'बिजली': 'విద్యుత్',

    # Environment
    'प्रदूषण': 'కాలుష్యం',
    'वायु': 'వాయు',
    'जलवायु': 'వాతావరణ',
    'स्वच्छ': 'స్వచ్ఛ',
    'सफाई': 'పరిశుద్ధత',
    'कचरा': 'చెత్త',
    'कचरे': 'చెత్త',

    # Mission & Scheme
    'योजना': 'యోజన',
    'मिशन': 'మిషన్',
    'परियोजना': 'ప్రాజెక్ట్',
    'कार्यक्रम': 'కార్యక్రమం',

    # Development
    'विकास': 'అభివృద్ధి',
    'विकसित': 'అభివృద్ధిచేసిన',
    'उन्नत': 'అభివృద్ధిచేసిన',

    # Social
    'गरीबी': 'దారిద్ర్యం',
    'गरीब': 'దరిద్ర',
    'गरीबों': 'దారిద్ర్యుల',
    'महिला': 'మహిళ',
    'महिलाओं': 'మహిళల',
    'बच्चे': 'పిల్లలు',
    'बच्चों': 'పిల్లల',

    # Governance
    'संविधान': 'సంవిధానం',
    'संशोधन': 'సవరణ',
    'शासन': 'పరిపాలన',
    'सरकार': 'ప్రభుత్వం',
    'नगरपालिका': 'పౌర నిగమం',
    'पंचायत': 'పంచాయతీ',
    'राज्य': 'రాష్ట్రం',
    'राष्ट्रीय': 'జాతీయ',
    'भारत': 'భారత',
    'भारतीय': 'భారతీయ',
    'भारत के': 'భారత',
    'भारत में': 'భారతంలో',
    'भारत का': 'భారత',

    # Questions
    'कितना': 'ఎంత',
    'कितने': 'ఎన్ని',
    'कौन सा': 'ఏ',
    'कौन सी': 'ఏ',
    'क्या': 'ఏమిటి',
    'कब': 'ఎప్పుడు',
    'कहाँ': 'ఎక్కడ',
    'कैसे': 'ఎలా',
    'किसके': 'వారిది',
    'किसे': 'వారిని',

    # Other
    'प्रतिशत': 'శതాంశం',
    'संख्या': 'సంఖ్య',
    'वर्ष': 'సంవత్సరం',
    'वर्षों': 'సంవత్సరాల',
    'लाख': 'లక్ష',
    'करोड़': 'కోటి',
}

# Hindi → English translations for key terms
HINDI_ENGLISH_DICT = {
    'शहर': 'city',
    'शहरी': 'urban',
    'नगर': 'city',
    'आवास': 'housing',
    'परिवहन': 'transport',
    'सड़क': 'road',
    'मेट्रो': 'metro',
    'जल': 'water',
    'विकास': 'development',
    'गरीबी': 'poverty',
    'गरीब': 'poor',
    'महिला': 'woman',
    'संविधान': 'constitution',
    'शासन': 'governance',
    'सरकार': 'government',
    'भारत': 'India',
    'मिशन': 'mission',
    'योजना': 'scheme',
    'प्रदूषण': 'pollution',
    'स्वच्छ': 'clean',
    'कब': 'when',
    'कितना': 'how much',
    'कितने': 'how many',
}

def simple_hindi_to_telugu(hindi_text):
    """Simple term-by-term Hindi→Telugu conversion"""
    telugu_text = hindi_text

    # Apply longest matches first to avoid partial replacements
    for hindi_term in sorted(HINDI_TELUGU_DICT.keys(), key=len, reverse=True):
        telugu_term = HINDI_TELUGU_DICT[hindi_term]
        telugu_text = telugu_text.replace(hindi_term, telugu_term)

    return telugu_text

def simple_hindi_to_english(hindi_text):
    """Simple Hindi→English translation"""
    english_text = hindi_text

    # Apply direct mappings
    for hindi_term in sorted(HINDI_ENGLISH_DICT.keys(), key=len, reverse=True):
        english_term = HINDI_ENGLISH_DICT[hindi_term]
        english_text = english_text.replace(hindi_term, english_term)

    return english_text

def process_bucket_a():
    """Process Bucket A (Hindi only) MCQs"""

    print("BUCKET A CONVERSION: Hindi → Telugu+English")
    print("=" * 80)

    # Load files
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        current_content = f.read()

    with open('HAIKU_INPUT_broken_source.py', 'r', encoding='utf-8') as f:
        hindi_content = f.read()

    with open('HAIKU_TODO_IDS.json', 'r') as f:
        buckets = json.load(f)

    bucket_a_ids = buckets['hindi_only_needs_translation']

    print(f"Processing {len(bucket_a_ids)} Hindi MCQs from Bucket A...")
    print(f"Loading Hindi source data...")

    # Extract Hindi MCQs from source
    hindi_mcqs = {}
    for line in hindi_content.split('\n'):
        match = re.search(r'\((\d{5}),', line)
        if match:
            mcq_id = int(match.group(1))
            if mcq_id in bucket_a_ids:
                hindi_mcqs[mcq_id] = line

    print(f"  ✓ Found {len(hindi_mcqs)} Hindi MCQs in source")

    # Create sample conversions
    print("\nCreating bilingual translations...")

    # For demonstration, process first few MCQs as template
    sample_ids = sorted(bucket_a_ids)[:5]

    sample_translations = {}
    for mcq_id in sample_ids:
        if mcq_id in hindi_mcqs:
            hindi_line = hindi_mcqs[mcq_id]

            # Extract Hindi question
            q_match = re.search(r'\(\d+,\s*["\']([^"\']+)["\']', hindi_line)
            if q_match:
                hindi_q = q_match.group(1)

                # Create bilingual version
                telugu_q = simple_hindi_to_telugu(hindi_q)
                english_q = simple_hindi_to_english(hindi_q)

                bilingual_q = f"{telugu_q}\n({english_q})"

                # Find current entry in seed file
                current_pattern = f'({mcq_id}, '
                if current_pattern in current_content:
                    curr_idx = current_content.find(current_pattern)
                    curr_snippet = current_content[curr_idx:curr_idx+300]

                    # Extract current question
                    curr_q_match = re.search(r'\(\d+, ["\']([^"\']+)["\']', curr_snippet)
                    if curr_q_match:
                        current_q = curr_q_match.group(1)
                        sample_translations[current_q] = bilingual_q

                        print(f"  ID {mcq_id}:")
                        print(f"    Hindi: {hindi_q[:60]}...")
                        print(f"    Telugu: {telugu_q[:50]}...")
                        print(f"    English: {english_q[:50]}...")

    print(f"\n✓ Created {len(sample_translations)} sample translations")

    # Apply sample replacements CAREFULLY
    print("\nApplying translations...")

    applied = 0
    for old_q, new_q in sample_translations.items():
        # Find and replace this specific question
        # Use quote-safe approach
        for quote in ['"', "'"]:
            old_pattern = f'{quote}{old_q}{quote}'
            new_pattern = f'{quote}{new_q}{quote}'

            if old_pattern in current_content:
                current_content = current_content.replace(old_pattern, new_pattern, 1)
                applied += 1
                print(f"  ✓ Applied translation")
                break

    # Verify
    print(f"\nVerifying integrity...")
    try:
        compile(current_content, 'seed_national_ca_2026_mcq.py', 'exec')
        print("  ✓ AST: PASS")

        # Save
        with open('seed_national_ca_2026_mcq.py', 'w', encoding='utf-8') as f:
            f.write(current_content)

        print(f"  ✓ File saved")
        print(f"\n✅ BUCKET A CONVERSION SAMPLE COMPLETE")
        print(f"   Applied {applied} translations")
        print(f"   File integrity verified")

        return True

    except SyntaxError as e:
        print(f"  ✗ AST: FAIL - {str(e)[:60]}")
        return False

if __name__ == '__main__':
    process_bucket_a()
