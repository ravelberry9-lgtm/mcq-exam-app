"""Turn a spoken/typed reply into an option letter. Grading is deterministic: the LLM never decides right/wrong."""
import re
import unicodedata

LETTERS = "abcde"
# spoken forms -> letter (English, Telugu words, Telugu letters, Telugu-script spellings of A/B/C/D)
WORDS = {
    "a": "a", "ay": "a", "ae": "a", "ఎ": "a", "ఏ": "a", "అ": "a", "ఎయ్": "a",
    "b": "b", "bee": "b", "be": "b", "బి": "b", "బీ": "b",
    "c": "c", "see": "c", "sea": "c", "సి": "c", "సీ": "c",
    "d": "d", "dee": "d", "డి": "d", "డీ": "d",
    "e": "e", "ee": "e", "ఈ": "e", "ఇ": "e",
    "1": "a", "one": "a", "first": "a", "ఒకటి": "a", "ఒకటో": "a", "మొదటి": "a", "మొదటిది": "a", "ఒకటవ": "a",
    "2": "b", "two": "b", "second": "b", "రెండు": "b", "రెండో": "b", "రెండవ": "b", "రెండవది": "b", "రెండోది": "b",
    "3": "c", "three": "c", "third": "c", "మూడు": "c", "మూడో": "c", "మూడవ": "c", "మూడవది": "c", "మూడోది": "c",
    "4": "d", "four": "d", "fourth": "d", "నాలుగు": "d", "నాలుగో": "d", "నాలుగవ": "d", "నాలుగవది": "d", "నాలుగోది": "d",
    "5": "e", "five": "e", "fifth": "e", "ఐదు": "e", "ఐదో": "e", "ఐదవ": "e",
}
FILLER = {"option", "answer", "is", "it", "its", "the", "number", "no", "ఆప్షన్", "ఆన్సర్", "సమాధానం", "అని", "అనే", "నా",
          "ఏమో", "అయి", "ఉంటుంది", "అవుతుంది", "అనుకుంటున్నా", "i", "think", "choose", "pick", "select", "my",
          "కరెక్ట్", "correct", "అయ్యి", "ఉండొచ్చు", "ఉంది", "ఇదే", "నేను", "అనుకుంటా", "అనుకుంటున్నాను"}
SKIP = {"skip", "pass", "next", "తరువాత", "తర్వాత", "స్కిప్", "వద్దు", "తెలియదు", "తెలీదు", "idk", "dontknow", "నెక్స్ట్"}
SKIP_PHRASES = ("don't know", "do not know", "no idea", "not sure", "తెలియదు", "తెలీదు", "గుర్తులేదు")
REPEAT = ("repeat", "again", "మళ్ళీ", "మళ్లీ", "రిపీట్", "ఇంకోసారి", "మరోసారి")


def _toks(s: str):
    s = unicodedata.normalize("NFC", s or "").lower().replace("‌", "").replace("‍", "")
    return re.findall(r"[ఀ-౿]+|[a-z]+|\d+", s)


def parse_answer(text: str, n_options: int = 4, options: dict | None = None):
    """Return ('answer', letter) | ('skip', None) | ('repeat', None) | ('unclear', None).
    `options` ({'a': 'text', ...}) lets the learner answer by saying the option's text instead of its letter."""
    low = (text or "").lower()
    if any(p in low for p in REPEAT):
        return "repeat", None
    if any(p in low for p in SKIP_PHRASES):
        return "skip", None
    toks = _toks(text)
    if not toks:
        return "unclear", None
    if any(t in SKIP for t in toks):
        return "skip", None
    valid = set(LETTERS[:n_options])
    if len(toks) > 1 and "one" in toks and any(t in ("first", "second", "third", "fourth", "fifth", "two", "three", "four", "five") for t in toks):
        toks = [t for t in toks if t != "one"]  # "second one" -> second
    hits = [WORDS[t] for t in toks if t in WORDS and WORDS[t] in valid]
    core = [t for t in toks if t not in FILLER]
    # clean case: after removing filler, exactly one thing left and it names an option
    if len(core) == 1 and core[0] in WORDS and WORDS[core[0]] in valid:
        return "answer", WORDS[core[0]]
    # said the option's text
    if options:
        best, best_score = None, 0.0
        ts = set(toks)
        for k, v in options.items():
            ot = set(_toks(v))
            if not ot:
                continue
            sc = len(ot & ts) / len(ot)
            if sc > best_score:
                best, best_score = k, sc
        if best and best_score >= 0.7 and best in valid:
            return "answer", best
    # short utterance with one distinct option named
    if len(set(hits)) == 1 and len(toks) <= 6:
        return "answer", hits[0]
    return "unclear", None  # ask again; never guess a grade
