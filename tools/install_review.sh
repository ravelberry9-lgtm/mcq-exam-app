#!/bin/bash
# Install manual MCQ review for lesson(s): bash tools/install_review.sh 4 5
set -e
for n in "$@"; do cp content/geography/g2/$n/Questions.json /tmp/qb_$n.json; done
python3 tools/build_g2_geography.py | tail -1
python3 - "$@" <<'P'
import json,sys
for n in sys.argv[1:]:
    a={q['id']:q for q in json.load(open(f'/tmp/qb_{n}.json'))['questions']}
    b={q['id']:q for q in json.load(open(f'content/geography/g2/{n}/Questions.json'))['questions']}
    e=json.load(open(f'content/geography/g2/{n}/Explanations.json'))['questions']
    assert set(a)==set(b) and all(a[i]['answer']==b[i]['answer'] for i in a), f'L{n} ids/answers changed'
    st=sum(1 for v in e.values() if v.get('stale'))
    print(f'L{n}: {len(b)} questions, answers unchanged, stale explanations {st}')
    assert st==0
P
git add content/geography/g2 content/geography/g2_mcq_review tools/build_g2_geography.py tools/install_review.sh
git -c user.name=Claude -c user.email=noreply@anthropic.com commit -q -m "fix(geography): APPSC-standard MCQ review for lesson(s) $*

Every question read manually against APPSC Group 2 standard; none retired. Duplicates rewritten into
new facts, source/meta stems made direct, absurd distractors replaced, ambiguous items given one answer;
correct option kept at the same position; new Telugu/English explanations for every changed question.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Ya92NUNfM5kfu285M8y6sy"
git log --oneline -1
