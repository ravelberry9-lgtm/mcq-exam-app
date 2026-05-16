"""
Fix Telugu bilingual prefixes in MCQ seed files.
Replaces questions missing Telugu Unicode with properly formatted bilingual versions.
"""
import re

# Map of old question strings -> new bilingual question strings

FIXES_CH72 = {
    "SBC disciplinary committee ऎমি? / What is SBC's disciplinary committee?":
        "SBC disciplinary committee ఏమిటి? / What is SBC's disciplinary committee?",

    "AIBE ने वकालत profession में क्या change लाया? / What change did AIBE bring to the legal profession?":
        "AIBE న్యాయ వృత్తిలో ఏ మార్పు తెచ్చింది? / What change did AIBE bring to the legal profession?",

    "AIBE full form? / What is AIBE full form?":
        "AIBE full form ఏమిటి? / What is AIBE full form?",
}

FIXES_CH73 = {
    "Law Commission reports binding on government? / Are Law Commission reports binding on the government?":
        "లా కమిషన్ నివేదికలు binding గా ఉంటాయా? / Are Law Commission reports binding on the government?",

    "Law Commission reports Parliament में कैसे reach होती हैं? / How do Law Commission reports reach Parliament?":
        "లా కమిషన్ నివేదికలు Parliament కి ఎలా చేరుతాయి? / How do Law Commission reports reach Parliament?",

    "Law Commission recommendations accept/reject करने का अधिकार किसको है? / Who has the right to accept/reject Law Commission recommendations?":
        "లా కమిషన్ సిఫారసులు accept/reject చేసే హక్కు ఎవరికి ఉంది? / Who has the right to accept/reject Law Commission recommendations?",

    "Law Commission किन restrictions के साथ काम करती है? / What restrictions does Law Commission work under?":
        "లా కమిషన్ ఏ పరిమితులతో పని చేస్తుంది? / What restrictions does Law Commission work under?",

    "Law Commission sedition law (Sec.124A IPC) पर क्या कहा? / What did Law Commission say about sedition law (Sec.124A IPC)?":
        "లా కమిషన్ sedition law (Sec.124A IPC) పై ఏమి చెప్పింది? / What did Law Commission say about sedition law (Sec.124A IPC)?",

    "Law Commission reports publicly available? / Are Law Commission reports publicly available?":
        "లా కమిషన్ నివేదికలు publicly available గా ఉంటాయా? / Are Law Commission reports publicly available?",

    "Law Commission निरंतरता की समस्या क्या है? / What is Law Commission's continuity problem?":
        "లా కమిషన్ continuity సమస్య ఏమిటి? / What is Law Commission's continuity problem?",

    "Law Commission India लाखों में क्या बदला है? / What has Law Commission changed in millions of Indians' lives?":
        "లా కమిషన్ కోట్లాది భారతీయుల జీవితాల్లో ఏమి మార్చింది? / What has Law Commission changed in millions of Indians' lives?",

    "First British India Law Commission chairman? / Who chaired the first British India Law Commission?":
        "మొదటి British India లా కమిషన్ chairman ఎవరు? / Who chaired the first British India Law Commission?",

    "First post-independence Law Commission year? / What year was the first post-independence Law Commission?":
        "స్వాతంత్ర్యానంతర మొదటి లా కమిషన్ ఏ సంవత్సరం? / What year was the first post-independence Law Commission?",

    "Law Commission reports binding? / Are Law Commission reports binding?":
        "లా కమిషన్ నివేదికలు binding గా ఉంటాయా? / Are Law Commission reports binding?",
}

FIXES_CH74 = {
    "Malapportionment अंत क्या है Delimitation context लो? / What is malapportionment in Delimitation context?":
        "నియోజకవర్గ పరిమితిలో Malapportionment ఏమిటి? / What is malapportionment in Delimitation context?",

    "Art.327 Delimitation कि ऐसे connect? / How does Art.327 connect to Delimitation?":
        "Art.327 నియోజకవర్గ పరిమితితో ఎలా connect అవుతుంది? / How does Art.327 connect to Delimitation?",

    "106th Amendment 2023 Delimitation কি ऐसे connect? / How does 106th Amendment 2023 connect to Delimitation?":
        "106th Amendment 2023 నియోజకవర్గ పరిమితితో ఎలా connect అవుతుంది? / How does 106th Amendment 2023 connect to Delimitation?",

    "42nd Amendment year? / What year is the 42nd Amendment?":
        "42nd Amendment ఏ సంవత్సరం? / What year is the 42nd Amendment?",

    "84th Amendment year? / What year is the 84th Amendment?":
        "84th Amendment ఏ సంవత్సరం? / What year is the 84th Amendment?",
}

FIXES_CH75 = {
    "NEC member states total number? / What is the total number of NEC member states?":
        "NEC సభ్య రాష్ట్రాల సంఖ్య ఎంత? / What is the total number of NEC member states?",

    "Union HM NEC chairman বনিং purpose ऎমি? / What purpose does the Union HM serving as NEC Chairman serve?":
        "Union HM NEC chairman గా ఉండటం వల్ల ప్రయోజనం ఏమిటి? / What purpose does the Union HM serving as NEC Chairman serve?",

    "NEC DoNER Ministry साथ कैसे काम करती है? / How does NEC work with DoNER Ministry?":
        "NEC DoNER Ministry తో ఎలా పని చేస్తుంది? / How does NEC work with DoNER Ministry?",

    "NEC Act year? / What year is NEC Act?":
        "NEC Act ఏ సంవత్సరం? / What year is NEC Act?",

    "NEC Chairman (post-2002)? / Who is NEC Chairman after 2002?":
        "NEC Chairman (2002 తర్వాత) ఎవరు? / Who is NEC Chairman after 2002?",

    "NEC first meeting year? / What year was NEC's first meeting?":
        "NEC మొదటి సమావేశం ఏ సంవత్సరం? / What year was NEC's first meeting?",
}

ALL_FIXES = {
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch72.py': FIXES_CH72,
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch73.py': FIXES_CH73,
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch74.py': FIXES_CH74,
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch75.py': FIXES_CH75,
}

telugu_range = re.compile(r'[\u0c00-\u0c7f]')

for filepath, fixes in ALL_FIXES.items():
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()

    applied = 0
    for old_q, new_q in fixes.items():
        if old_q in content:
            content = content.replace(old_q, new_q)
            applied += 1
        else:
            print(f"WARNING: Not found in {filepath.split('/')[-1]}: {old_q[:60]!r}")

    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(content)

    print(f"Applied {applied}/{len(fixes)} fixes to {filepath.split('/')[-1]}")

# Verify all files
print("\n=== VERIFICATION ===")

all_files = [
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch71.py',
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch72.py',
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch73.py',
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch74.py',
    '/sessions/vigilant-vibrant-fermat/mnt/mcq_app/seed_polity_ch75.py',
]

for f in all_files:
    with open(f, encoding='utf-8') as fh:
        content = fh.read()

    mcq_start = content.find('MCQ_DATA = [')
    pattern = re.compile(r'\(\s*\d+\s*,\s*\"(easy|medium|hard)\"\s*,\s*\"(.*?)\"', re.DOTALL)
    matches = pattern.findall(content[mcq_start:])

    total = len(matches)
    with_telugu = sum(1 for _, q in matches if telugu_range.search(q))
    missing = [(diff, q) for diff, q in matches if not telugu_range.search(q)]

    status = "PASS" if with_telugu == 64 and total == 64 else "FAIL"
    print(f"[{status}] {f.split('/')[-1]}: {with_telugu}/{total} questions have Telugu Unicode")
    if missing:
        for diff, q in missing:
            print(f"  MISSING: {q[:80]!r}")
