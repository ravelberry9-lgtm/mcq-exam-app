"""Validation of answer payloads. Bad input is rejected with ValueError, never allowed to raise a server error."""

CONFIDENCE_MAX = 5          # the practice page offers 1..5; 0 / missing means "not given"


def payload_dict(raw):
    if not isinstance(raw, dict):
        raise ValueError("payload must be a JSON object")
    return raw


def parse_confidence(value):
    if value is None or value == "":
        return 0
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError("confidence must be a whole number")
    try:
        n = int(value)
    except ValueError:
        raise ValueError("confidence must be a whole number") from None
    if not 0 <= n <= CONFIDENCE_MAX:
        raise ValueError(f"confidence must be between 0 and {CONFIDENCE_MAX}")
    return n


def parse_choice(value, allow_empty=False):
    if value is None:
        value = ""
    if not isinstance(value, str):
        raise ValueError("chosen must be a letter")
    v = value.strip().lower()
    if v == "" and allow_empty:
        return ""
    if v not in ("a", "b", "c", "d", "e"):
        raise ValueError("chosen must be one of a-e")
    return v


def parse_question_id(value):
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError("question_id must be a whole number")
    try:
        return int(value)
    except ValueError:
        raise ValueError("question_id must be a whole number") from None
