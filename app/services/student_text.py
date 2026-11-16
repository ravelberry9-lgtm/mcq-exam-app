"""Student-facing text helpers for Polity practice pages.

1. ``strip_meta`` hides internal audit / correction / source notes from concept-card text
   at display time (stored content is unchanged; ``scan_meta`` lists what it hides so the
   data can be cleaned later).
2. ``explain_parts`` splits a stored explanation into a summary sentence, further "why"
   sentences and per-option notes, without changing any of the text.
"""
import re

# Each pattern removes one kind of meta note. Order matters: whole parentheticals first.
META_PATTERNS = [
    # parenthetical notes about an earlier/old card or a wrong attribution
    ('old-card-note', re.compile(r"\s*\((?=[^()]*(?:\bold card\b|పాత కార్డు|\bwrongly\b|\bearlier card\b))[^()]*\)", re.I)),
    # parenthetical saying a source/book was wrong: (GBKలో ఉన్న '1986' తప్పు.)
    ('source-error-note', re.compile(r"\s*\((?=[^()]*(?:GBK|Laxmikanth))(?=[^()]*(?:తప్పు|\bwrong\b|\berror\b|misprint))[^()]*\)", re.I)),
    # correction asides: "(not X)", "(... not of the CA.)", "(X కాదు)" / "(... పరిషత్ పై కాదు.)"
    ('not-x-aside', re.compile(r"\s*\(not [^()]*\)", re.I)),
    ('not-x-aside', re.compile(r"\s*\([^()]*,\s*not [^()]*\.\)", re.I)),
    ('not-x-aside', re.compile(r"\s*\([^()]*\bnot (?:of|on|in|by) [^()]*\.\)", re.I)),
    ('kaadu-aside', re.compile(r"\s*\([^(),;]*కాదు\.?\)")),
    ('kaadu-aside', re.compile(r"\s*\([^()]*,\s*[^(),]*పై కాదు\.?\)")),
    # trailing "— X కాదు." / "— not X." correction tails
    ('not-x-tail', re.compile(r"\s*[—–-]\s*[^—–.]*కాదు\.?\s*$")),
    ('not-x-tail', re.compile(r"\s*[—–]\s*not [^—–.]*\.?\s*$", re.I)),
    # bare source tags
    ('source-tag', re.compile(r"\s*\((?:GBK|Laxmikanth|Lax\.?)(?:[ ,]*(?:p|pp|Ch)\.?\s*[\d–-]+)?\)", re.I)),
    ('source-tag', re.compile(r"^(?:GBK|Laxmikanth)\s*:\s*", re.I)),
    # audit footers and markers
    ('audit-footer', re.compile(r"\s*Audited against[^\n]*", re.I)),
    ('audit-marker', re.compile(r"\s*⚠\s*")),
]


def strip_meta(text):
    if not text:
        return text or ''
    out = str(text)
    for _, pat in META_PATTERNS:
        out = pat.sub(' ' if pat.pattern.endswith('⚠\\s*') else '', out)
    out = re.sub(r"\s{2,}", ' ', out).strip()
    out = re.sub(r"\s+([.,;:])", r"\1", out)
    if text.rstrip().endswith('.') and out and out[-1] not in '.!?':
        out += '.'
    return out


def scan_meta(text):
    """Return [(kind, matched string)] for every meta note ``strip_meta`` would hide."""
    found, cur = [], str(text or '')
    for kind, pat in META_PATTERNS:
        for m in pat.finditer(cur):
            if m.group(0).strip():
                found.append((kind, m.group(0).strip()))
        cur = pat.sub(' ', cur)
    return found


# ---------------------------------------------------------------- explanations
_ABBR = re.compile(r"(?:\b(?:Ch|No|Nos|Art|Arts|Sec|Cl|Sch|Vol|vs|v|Dr|Mr|Shri|Smt|Pt|St|etc|viz|cf|ed|Pr|Fig|Sl|Sir)|\b[A-Z])\.$")
_ABBR_TE = re.compile(r"(?:^|[\s.])(?:డా|శ్రీ|శ్రీమతి|[అ-ఔక-హ][ా-ౌం]?(?:[క-హ]్)?)\.$")


def sentences(text):
    out = []
    for par in re.split(r"\n+", (text or '').strip()):
        for x in re.split(r"(?<=[.!?])\s+", par.strip()):
            if out and (_ABBR.search(out[-1]) or _ABBR_TE.search(out[-1])):
                out[-1] += ' ' + x
            elif x:
                out.append(x)
    return out


def _norm(s):
    return re.sub(r"[\W_]+", ' ', (s or '').lower()).strip()


def _mentions(sentence, option):
    o = _norm(option)
    if not o:
        return False
    s = ' ' + _norm(sentence) + ' '
    if len(o) >= 4 or o.isdigit():
        return (' ' + o + ' ') in s
    return False


def explain_parts(text, options=(), answer=None):
    """Split an explanation into lead / why / other-option notes (text unchanged).

    A later sentence that names a wrong option (and not the right one) goes to that option.
    """
    sents = sentences(text)
    if not sents:
        return None
    lists = [list(o or []) for o in options if o]
    lead, rest = sents[0], sents[1:]
    why, others = [], []
    for s in rest:
        hit = set()
        for opts in lists:
            for i, o in enumerate(opts, 1):
                if _mentions(s, o):
                    hit.add(i)
        wrong = []  # option-splitting disabled: misfired on statement-type questions
        if wrong and answer not in hit:
            if others and others[-1]['nums'] == wrong:
                others[-1]['text'] += ' ' + s
            else:
                others.append(dict(nums=wrong, text=s))
        else:
            why.append(s)
    return dict(lead=lead, why=why, others=others)


def options_te_usable(q):
    te, en = q.get('options_te') or [], q.get('options_en') or []
    return bool(te) and len(te) == len(en) and any(a and a.strip() != (b or '').strip() for a, b in zip(te, en))
