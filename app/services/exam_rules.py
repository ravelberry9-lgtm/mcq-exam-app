"""Exam rules and how a test session is built.

Nothing here knows the real APPSC pattern. The seeded paper rows (marks, duration) are unverified placeholders, so:

* an **official** test can be started only for a paper that has an entry in ``VERIFIED_RULES`` (question count, duration,
  negative marking and where each was confirmed). The registry is empty until the rules are checked against the notification;
* everything else is an **unofficial practice test** with a question count and time limit that the *user* picks, clearly
  labelled as such, and never larger than ``MAX_SESSION_QUESTIONS``.

Sessions never contain "every eligible question": a session has an explicit, capped size.
"""
import random

MIN_PRACTICE_QUESTIONS = 5
DEFAULT_PRACTICE_QUESTIONS = 20
MAX_SESSION_QUESTIONS = 100
MIN_MINUTES, MAX_MINUTES = 5, 180

# {(exam_slug, paper_num): {"question_count": int, "duration_min": int, "negative_marking": None | 0,
#                           "source": "<notification / page where each value was confirmed>"}}
# Negative marking other than none is rejected until the scoring supports it (see ``verified_rules``).
VERIFIED_RULES = {}


def verified_rules(exam_slug, paper_num):
    """Return the verified rules for a paper, or None when they are missing, incomplete or not yet supported."""
    rule = VERIFIED_RULES.get((exam_slug, paper_num))
    if not rule:
        return None
    try:
        n, minutes = int(rule["question_count"]), int(rule["duration_min"])
    except (KeyError, TypeError, ValueError):
        return None
    if not (1 <= n <= MAX_SESSION_QUESTIONS and MIN_MINUTES <= minutes <= MAX_MINUTES) or not rule.get("source"):
        return None
    if rule.get("negative_marking") not in (None, 0):
        return None                      # the score is a plain count of correct answers; do not claim otherwise
    return {"question_count": n, "duration_min": minutes, "negative_marking": None, "source": rule["source"]}


def clamp_practice(count, minutes):
    """Validate user-chosen practice settings. Raises ValueError for non-numbers; clamps numbers into range."""
    count = DEFAULT_PRACTICE_QUESTIONS if count in (None, "") else int(count)
    n = max(MIN_PRACTICE_QUESTIONS, min(MAX_SESSION_QUESTIONS, count))
    minutes = n if minutes in (None, "") else int(minutes)       # default: 1 minute per question, shown to the user
    return n, max(MIN_MINUTES, min(MAX_MINUTES, minutes))


def pick_questions(section_question_ids, count, seed):
    """Choose up to ``count`` question ids, spread evenly over the sections (round robin), shuffled with ``seed`` so the
    same seed gives the same test. ``section_question_ids`` is a list of id lists, one per section."""
    rng = random.Random(seed)
    pools = []
    for ids in section_question_ids:
        ids = list(dict.fromkeys(ids))
        rng.shuffle(ids)
        if ids:
            pools.append(ids)
    rng.shuffle(pools)
    count = min(count, MAX_SESSION_QUESTIONS)
    chosen, seen = [], set()
    while pools and len(chosen) < count:
        for pool in list(pools):
            while pool and pool[-1] in seen:
                pool.pop()
            if not pool:
                pools.remove(pool)
                continue
            qid = pool.pop()
            seen.add(qid); chosen.append(qid)
            if len(chosen) >= count:
                break
    rng.shuffle(chosen)
    return chosen
