#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert MCQs 31576-31600 to Telugu+English bilingual format
"""

import re

# MCQ bilingual data
mcq_data = {
    31576: ("Government Service Excellence Index (GSEI)\nరాజ్య సేవా శ్రేష్ఠత్వ సూచిక", "A"),
    31577: ("Integrated District Administration (IDA) Model\nసమన్విత జిల్లా పరిపాలన", "A"),
    31578: ("Whistleblower Protection and Incentivization Scheme (WPIS)\nవిస్ఫోటక సంరక్షణ పథకం", "A"),
    31579: ("Adaptive Governance Initiative\nసమీకరణ పరిపాలన", "A"),
    31580: ("Governance for Development Framework\nఆర్థిక అభివృద్ధి కోసం పాలన", "A"),
    31581: ("PM-KISAN Scheme (Dec 2018)\nPM-కిసాన్ పథకం", "A"),
    31582: ("PM-KISAN Annual Financial Assistance\nPM-కిసాన్ వార్షిక సహాయం", "C"),
    31583: ("PM Gati Shakti National Master Plan - Ministry\nPM గతి శక్తి జాతీయ మాస్టర్ ప్లాన్", "C"),
    31584: ("PM Gati Shakti Budget Allocation (2021-2026)\nPM గతి శక్తి బడ్జెట్", "B"),
    31585: ("NRLM Focus Area\nNRLM ఫోకస్ ప్రాంతం", "B"),
    31586: ("NRLM Self Help Groups (SHGs) May 2026\nNRLM స్వయం సహాయ సమూహాలు", "C"),
    31587: ("PMKVY Primary Focus\nPMKVY ప్రధాన ఫోకస్", "B"),
    31588: ("PMKVY Youth Trained May 2026\nPMKVY శిక్ష్ణ యువకులు", "C"),
    31589: ("Women Empowerment Through Financial Inclusion\nమహిళా సాధికారత ఆర్థిక సంభందం", "C"),
    31590: ("PM Mudra Yojana Total Disbursement May 2026\nPM ముద్రా యోజన మొత్తం", "C"),
    31591: ("PM Vaya Vandana Yojana (PMVVY) Primary Objective\nPMVVY ప్రధాన లక్ష్యం", "B"),
    31592: ("PMVVY Senior Citizens Enrolled May 2026\nPMVVY నమోదు చేసిన సీనియర్లు", "C"),
    31593: ("Disability Pension Scheme\nవికలాంగత పెన్షన్ పథకం", "A"),
    31594: ("Persons with Disabilities Covered May 2026\nవికలాంగ వ్యక్తులు కవర్ చేయబడ్డారు", "B"),
    31595: ("PM Matritva Vandana Yojana (PMMVY) Focus\nPMMVY ఫోకస్", "B"),
    31596: ("PMMVY Pregnant Women Benefited May 2026\nPMMVY గర్భవతి మహిళలు", "C"),
    31597: ("PM Awas Yojana (Housing for All) Objective\nPM ఆవాస యోజన ఉద్దేశ్యం", "B"),
    31598: ("PM Awas Yojana Houses Completed May 2026\nPM ఆవాస యోజన ఇళ్ళు పూర్తిచేసారు", "C"),
    31599: ("Direct Cash Transfer via Aadhaar\nఆధార్ నేరుగా నగదు బదిలీ", "B"),
    31600: ("PMJDY Jan Dhan Accounts Opened May 2026\nPMJDY జన ధన్ ఖాతాలు తెరవబడ్డాయి", "C"),
}

# Generate output file
output = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCQ 31576-31600 Telugu+English Bilingual Format
National Current Affairs 2026 - Government Schemes & Initiatives
AP_HC Folder | National_Current_Affairs_2026 Topic
"""

BILINGUAL_MCQS_31576_31600 = [
'''

# Add MCQs
count = 0
for mcq_id in range(31576, 31601):
    if mcq_id in mcq_data:
        title, answer = mcq_data[mcq_id]
        count += 1
        output += f"    # MCQ {mcq_id}\n"
        output += f"    # {title}\n"
        output += f"    ({mcq_id}, \"{title}\", \"Option A\", \"Option B\", \"Option C\", \"Option D\", \"{answer}\", \"Explanation\", \"AP_HC\", \"National_Current_Affairs_2026\"),\n\n"

output += "]\n\nprint(f'Loaded {len(BILINGUAL_MCQS_31576_31600)} bilingual MCQs')\n"

with open('MCQ_31576_31600_bilingual_template.py', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Generated template file with {count} MCQs")
print("\nSample MCQ 31576:")
print(f"  Title: {mcq_data[31576][0]}")
print(f"  Answer: {mcq_data[31576][1]}")

print("\nSample MCQ 31588:")
print(f"  Title: {mcq_data[31588][0]}")
print(f"  Answer: {mcq_data[31588][1]}")

print("\nSample MCQ 31600:")
print(f"  Title: {mcq_data[31600][0]}")
print(f"  Answer: {mcq_data[31600][1]}")

# Validate Python syntax
try:
    compile(output, 'MCQ_31576_31600_bilingual_template.py', 'exec')
    print("\n✓ Python syntax is valid!")
except SyntaxError as e:
    print(f"\n✗ Syntax error: {e}")
