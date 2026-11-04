from answers import parse_answer as p
O = {"a": "శాతవాహనులు", "b": "ఇక్ష్వాకులు", "c": "పల్లవులు", "d": "చాళుక్యులు"}
cases = [("B", ("answer","b")), ("option C", ("answer","c")), ("the answer is d", ("answer","d")),
 ("రెండో", ("answer","b")), ("ఆప్షన్ సి", ("answer","c")), ("మూడవది", ("answer","c")), ("నాలుగు", ("answer","d")),
 ("option two", ("answer","b")), ("second one", ("answer","b")), ("ఇక్ష్వాకులు", ("answer","b")),
 ("I think it is bee", ("answer","b")), ("skip", ("skip",None)), ("నాకు తెలియదు", ("skip",None)),
 ("repeat the question", ("repeat",None)), ("మళ్ళీ చెప్పండి", ("repeat",None)),
 ("a or b", ("unclear",None)), ("hmm", ("unclear",None)), ("", ("unclear",None)), ("option five", ("unclear",None))]
bad = 0
for t, exp in cases:
    got = p(t, 4, O)
    ok = got == exp; bad += not ok
    print("ok " if ok else "BAD", repr(t), got, "" if ok else f"expected {exp}")
print("failures:", bad)
