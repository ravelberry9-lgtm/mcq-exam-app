#!/usr/bin/env python3
"""Apply FINAL/fixes.json to a COPY of the Chapter 1 bank and validate it.

Usage: python3 -I validate_and_patch.py [--include-pending] [--bank PATH] [--out PATH]
The original bank is opened read-only and its SHA-256 is checked before and after.
Exit code 0 = all checks pass, 1 = errors (listed on stdout).
Field-key format: see README.md in this folder.
"""
import argparse, copy, hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('--bank', default='/mnt/user-data/uploads/geography/chapter01_bilingual.json')
ap.add_argument('--fixes', default=str(HERE / 'fixes.json'))
ap.add_argument('--out', default=str(HERE / 'chapter01_bilingual.patched.json'))
ap.add_argument('--include-pending', action='store_true', help='also apply entries with a "status" (e.g. pending-page15)')
a = ap.parse_args()

bank_path = Path(a.bank)
assert Path(a.out).resolve() != bank_path.resolve(), 'refusing to overwrite the original bank'
sha_before = hashlib.sha256(bank_path.read_bytes()).hexdigest()
orig = json.loads(bank_path.read_text())
bank = copy.deepcopy(orig)
fixes = json.load(open(a.fixes))
Q, OQ = bank['questions'], orig['questions']

KEY = re.compile(r'^(?:(answer|held)|(te|en)\.(question|options|explanation|option_explanations|matching_lists\.(?:left|right))(?:\[(\d+)\])?)$')
errors, warnings, applied, skipped = [], [], 0, []

def get_parent(var, field):
    if field.startswith('matching_lists.'):
        side = field.split('.')[1]
        return var.get('matching_lists'), side
    return var, field

for qid, fx in fixes.items():
    if qid not in Q:
        errors.append(f'{qid}: id not in bank'); continue
    if fx.get('status') and not a.include_pending:
        skipped.append(qid); continue
    flds = fx.get('fields', {})
    # whole-value keys first, then indexed keys, so an index refines a whole-array replacement
    for key in sorted(flds, key=lambda k: '[' in k):
        val = flds[key]
        mt = KEY.match(key)
        if not mt:
            errors.append(f'{qid}: unknown field key {key!r}'); continue
        top, lang, field, idx = mt.groups()
        if top:
            Q[qid][top] = val; applied += 1; continue
        parent, name = get_parent(Q[qid]['variants'][lang], field)
        if parent is None or name not in parent:
            errors.append(f'{qid}: {key} targets a field the question does not have'); continue
        if idx is None:
            if isinstance(parent[name], list) != isinstance(val, list):
                errors.append(f'{qid}: {key} type mismatch (list vs string)'); continue
            parent[name] = val
        else:
            i = int(idx)
            if not isinstance(parent[name], list) or i >= len(parent[name]):
                errors.append(f'{qid}: {key} index out of range'); continue
            parent[name][i] = val
        applied += 1

def walk_empty(x, path):
    if isinstance(x, str):
        if not x.strip(): errors.append(f'{path}: empty string')
    elif isinstance(x, list):
        if not x: errors.append(f'{path}: empty list')
        for i, y in enumerate(x): walk_empty(y, f'{path}[{i}]')
    elif isinstance(x, dict):
        for k, y in x.items(): walk_empty(y, f'{path}.{k}')

held_changes = []
for qid, q in Q.items():
    o = OQ[qid]
    flags = fixes.get(qid, {}).get('flags', [])
    if q['answer'] != o['answer']:
        ev = fixes[qid].get('evidence') or ''
        if 'WRONG-KEY' not in flags or not ev.strip():
            errors.append(f'{qid}: answer changed {o["answer"]}->{q["answer"]} without WRONG-KEY flag + evidence')
    if q['held'] != o['held']: held_changes.append(f'{qid}: held {o["held"]}->{q["held"]}')
    te, en = q['variants']['te'], q['variants']['en']
    for lang in ('te', 'en'):
        n0 = len(o['variants'][lang]['options']); n1 = len(q['variants'][lang]['options'])
        if n0 != n1: errors.append(f'{qid}: {lang} options count changed {n0}->{n1}')
        if len(q['variants'][lang]['option_explanations']) != n1:
            errors.append(f'{qid}: {lang} option_explanations count {len(q["variants"][lang]["option_explanations"])} != options {n1}')
        if 'matching_lists' in o['variants'][lang]:
            for side in ('left', 'right'):
                if len(q['variants'][lang]['matching_lists'][side]) != len(o['variants'][lang]['matching_lists'][side]):
                    errors.append(f'{qid}: {lang} matching_lists.{side} length changed')
    if len(te['options']) != len(en['options']): errors.append(f'{qid}: te/en option counts differ')
    if not 1 <= q['answer'] <= len(en['options']): errors.append(f'{qid}: answer {q["answer"]} out of range')
    if 'matching_lists' in te and q['variants']['en'].get('options') != te['options']:
        warnings.append(f'{qid}: match-code options differ between te and en')
    walk_empty(q['variants'], qid)

sha_after = hashlib.sha256(bank_path.read_bytes()).hexdigest()
if sha_before != sha_after: errors.append('ORIGINAL BANK CHANGED during run')

bank['patched_from_sha256'] = sha_before
bank['patch_note'] = f'FINAL/fixes.json applied ({"incl." if a.include_pending else "excl."} pending)'
Path(a.out).write_text(json.dumps(bank, ensure_ascii=False, indent=2))

print(f'fix entries: {len(fixes)}  field writes applied: {applied}  pending skipped: {skipped}')
print('held changes:', held_changes or 'none')
print(f'original bank sha256 unchanged: {sha_before == sha_after} ({sha_before[:16]}…)')
for w in warnings: print('WARN', w)
for e in errors: print('ERROR', e)
print('RESULT:', 'PASS' if not errors else f'FAIL ({len(errors)} errors)', '->', a.out)
sys.exit(1 if errors else 0)
