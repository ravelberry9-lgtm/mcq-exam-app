# usage: bash tools/install_lessons.sh 15 16 ...
set -e
python3 tools/apply_new_notes.py "$@"
python3 tools/build_g2_geography.py | tail -1
python3 - "$@" <<'P'
import json,re,sys
for n in map(int,sys.argv[1:]):
    h=open(f'content/geography/g2/{n}/Notes.html',encoding='utf-8').read();ids=set(re.findall(r'id="([^"]+)"',h))
    q=json.load(open(f'content/geography/g2/{n}/Questions.json',encoding='utf-8'))['questions']
    ok=all(x['section'] in ids for x in q); print(n,len(q),'sections_ok' if ok else 'SECTION-MISMATCH',h.count('box fact'))
    assert ok
P
cl(){ find .git -name "*.lock" -not -name "*stale*" | while read f; do mv "$f" "$f.stale$RANDOM"; done; }
cl; git add content/geography/g2 content/geography/g2_fixes content/geography/_claude_rebuild content/geography/g2_review/new_notes tools >/dev/null 2>&1 || true; cl
git -c user.name=Claude -c user.email=noreply@anthropic.com commit -q -m "feat(geography): notes rewritten in new style for lesson(s) $*

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Ya92NUNfM5kfu285M8y6sy" >/dev/null 2>&1 || true; cl
git log --oneline | head -1
