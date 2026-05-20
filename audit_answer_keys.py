"""
audit_answer_keys.py
---------------------
Audits MCQ seed files for answer-key mismatches: the option pointed to by the
`answer` letter does not contain the fact stated in the explanation.

Files audited:
  * seed_ap_ca_div1.py .. seed_ap_ca_div10.py
  * seed_national_ca_2026_mcq.py
  * seed_intl_orgs_mcq.py

Uses ast.parse (no exec). Reports only suspected MISMATCHES.

Run:  python audit_answer_keys.py
"""

import ast
import os
import re
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

AP_DIVS = [os.path.join(THIS_DIR, "seed_ap_ca_div%d.py" % i) for i in range(1, 11)]
NATIONAL_FILE = os.path.join(THIS_DIR, "seed_national_ca_2026_mcq.py")
INTL_FILE = os.path.join(THIS_DIR, "seed_intl_orgs_mcq.py")


def _literal(node):
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def find_assignment(tree, name):
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == name:
                    return node.value
    return None


def _safe_parse(src, max_retries=20):
    """Try ast.parse; on SyntaxError, truncate at the error line and retry.
    Useful when file got truncated mid-record. Closes any open `[` so the
    truncated list can still parse as a literal.
    """
    last_err = None
    for _ in range(max_retries):
        try:
            return ast.parse(src)
        except SyntaxError as e:
            last_err = e
            if not e.lineno:
                raise
            lines = src.split("\n")
            # cut everything from the offending line onward
            src = "\n".join(lines[: e.lineno - 1])
            # ensure any open `MCQ_DATA = [` still closes; append `]` if needed
            opens = src.count("[")
            closes = src.count("]")
            if opens > closes:
                src += "\n" + ("]" * (opens - closes))
    raise last_err


def extract_ap_div(path):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        tree = _safe_parse(src)
    val = find_assignment(tree, "MCQ_DATA")
    if val is None or not isinstance(val, (ast.List, ast.Tuple)):
        return
    for elt in val.elts:
        line = getattr(elt, "lineno", 0)
        if isinstance(elt, ast.Tuple):
            items = [_literal(e) for e in elt.elts]
            if len(items) < 9:
                continue
            yield {
                "line": line,
                "question": items[2] or "",
                "opt_a": items[3] or "",
                "opt_b": items[4] or "",
                "opt_c": items[5] or "",
                "opt_d": items[6] or "",
                "answer": items[7] or "",
                "explanation": items[8] or "",
            }
        elif isinstance(elt, ast.Dict):
            d = _literal(elt)
            if not isinstance(d, dict):
                continue
            yield {
                "line": line,
                "question": d.get("question_te") or d.get("question") or "",
                "opt_a": d.get("opt_a") or d.get("option_a") or "",
                "opt_b": d.get("opt_b") or d.get("option_b") or "",
                "opt_c": d.get("opt_c") or d.get("option_c") or "",
                "opt_d": d.get("opt_d") or d.get("option_d") or "",
                "answer": d.get("answer") or d.get("correct_answer") or "",
                "explanation": d.get("explanation_te") or d.get("explanation") or "",
            }


def extract_national(path):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    val = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "questions":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        val = node.value
                        break
            if val is not None:
                break
    if val is None:
        return
    for elt in val.elts:
        line = getattr(elt, "lineno", 0)
        if not isinstance(elt, ast.Tuple):
            continue
        items = [_literal(e) for e in elt.elts]
        if len(items) < 8:
            continue
        yield {
            "line": line,
            "question": items[1] or "",
            "opt_a": items[2] or "",
            "opt_b": items[3] or "",
            "opt_c": items[4] or "",
            "opt_d": items[5] or "",
            "answer": items[6] or "",
            "explanation": items[7] or "",
        }


def extract_intl(path):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    val = find_assignment(tree, "INTL_MCQS")
    if val is None or not isinstance(val, (ast.List, ast.Tuple)):
        return
    for elt in val.elts:
        line = getattr(elt, "lineno", 0)
        if not isinstance(elt, ast.Dict):
            continue
        d = _literal(elt)
        if not isinstance(d, dict):
            continue
        yield {
            "line": line,
            "question": d.get("question", ""),
            "opt_a": d.get("option_a", ""),
            "opt_b": d.get("option_b", ""),
            "opt_c": d.get("option_c", ""),
            "opt_d": d.get("option_d", ""),
            "answer": d.get("correct_answer", ""),
            "explanation": d.get("explanation", ""),
        }


NUM_RE = re.compile(r"\d[\d,\.]*")


def _strip_letter_prefix(opt):
    return re.sub(r"^\s*[A-Da-d][\)\.\:]\s*", "", opt or "").strip()


def _numbers_in(text):
    if not text:
        return set()
    out = set()
    for m in NUM_RE.findall(text):
        s = m.strip(".,")
        if s:
            out.add(s)
    return out


def _options_dict(rec):
    return {
        "a": _strip_letter_prefix(rec["opt_a"]),
        "b": _strip_letter_prefix(rec["opt_b"]),
        "c": _strip_letter_prefix(rec["opt_c"]),
        "d": _strip_letter_prefix(rec["opt_d"]),
    }


def check_record(rec):
    ans_letter = (rec.get("answer") or "").strip().lower()
    if ans_letter not in ("a", "b", "c", "d"):
        return ("unknown", {"reason": "invalid_answer_letter"})

    opts = _options_dict(rec)
    expl = rec.get("explanation") or ""
    qst = rec.get("question") or ""
    if not expl or not any(opts.values()):
        return ("unknown", {"reason": "missing_expl_or_opts"})

    chosen = opts[ans_letter]
    chosen_nums = _numbers_in(chosen)
    expl_nums = _numbers_in(expl)
    q_nums = _numbers_in(qst)
    candidate_nums = [n for n in expl_nums if n not in q_nums and len(n) >= 1]

    if not chosen_nums:
        return ("unknown", {"reason": "chosen_has_no_numbers"})

    opts_nums = {k: _numbers_in(v) for k, v in opts.items()}
    union_opt_nums = set().union(*opts_nums.values())

    relevant = [n for n in candidate_nums if n in union_opt_nums]
    if not relevant:
        return ("unknown", {"reason": "no_overlap"})

    decisive = None
    for n in relevant:
        holders = [k for k, ns in opts_nums.items() if n in ns]
        if len(holders) == 1:
            decisive = (n, holders[0])
            break

    if decisive is None:
        return ("unknown", {"reason": "ambiguous_number_in_options"})

    expected_num, expected_letter = decisive
    if expected_letter == ans_letter:
        return ("match", {"num": expected_num})
    return (
        "mismatch",
        {
            "num": expected_num,
            "expected_letter": expected_letter,
            "expected_opt": opts[expected_letter],
            "current_opt": chosen,
        },
    )


FILES = []
for p in AP_DIVS:
    FILES.append((p, extract_ap_div))
FILES.append((NATIONAL_FILE, extract_national))
FILES.append((INTL_FILE, extract_intl))


def short(text, n=60):
    s = (text or "").replace("\n", " ").strip()
    return s[:n] + (chr(8230) if len(s) > n else "")


def main():
    total = 0
    mism_total = 0
    by_file = {}
    parse_errors = []
    for path, extractor in FILES:
        if not os.path.exists(path):
            continue
        fname = os.path.basename(path)
        try:
            recs = list(extractor(path))
        except SyntaxError as e:
            parse_errors.append((fname, "SyntaxError line %s: %s" % (e.lineno, e.msg)))
            continue
        except Exception as e:
            parse_errors.append((fname, "%s: %s" % (type(e).__name__, e)))
            continue
        for rec in recs:
            total += 1
            status, info = check_record(rec)
            if status == "mismatch":
                mism_total += 1
                by_file.setdefault(fname, []).append((rec, info))

    if parse_errors:
        print("PARSE ERRORS (file skipped):")
        for f, msg in parse_errors:
            print("  %s: %s" % (f, msg))
        print()

    print("=" * 72)
    print("AUDITED %d MCQs across %d files" % (total, len(FILES)))
    print("MISMATCHES FOUND: %d" % mism_total)
    print("=" * 72)
    print()

    for fname in sorted(by_file.keys()):
        rows = by_file[fname]
        print("\n##### %s  (%d mismatches) #####" % (fname, len(rows)))
        for rec, info in rows:
            ans_disp = (rec.get("answer") or "").strip()
            print("  line %s: \"%s\"" % (rec["line"], short(rec["question"])))
            print("    options: a=%s | b=%s | c=%s | d=%s" % (
                short(_strip_letter_prefix(rec["opt_a"]), 40),
                short(_strip_letter_prefix(rec["opt_b"]), 40),
                short(_strip_letter_prefix(rec["opt_c"]), 40),
                short(_strip_letter_prefix(rec["opt_d"]), 40),
            ))
            print("    currently answer='%s' (=%s)" % (
                ans_disp, short(info["current_opt"], 40)
            ))
            print("    explanation cites '%s' --> should be '%s' (=%s)" % (
                info["num"], info["expected_letter"].upper(),
                short(info["expected_opt"], 40),
            ))
            print("    expl: %s" % short(rec["explanation"], 110))
            print()

    print()
    print("=" * 72)
    print("DONE. %d suspected mismatches." % mism_total)
    print("=" * 72)


if __name__ == "__main__":
    main()
