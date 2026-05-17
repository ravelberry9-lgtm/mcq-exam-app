#!/usr/bin/env python3
"""
Push seed_concept_notes_national.py + app.py to GitHub.
Run: python push_national_notes.py
"""
import os, json, base64, urllib.request, urllib.error

REPO    = "ravelberry9-lgtm/mcq-exam-app"
PAT     = ""  # set via GITHUB_TOKEN env var
HEADERS = {
    "Authorization": f"token {PAT}",
    "Content-Type":  "application/json",
    "Accept":        "application/vnd.github.v3+json",
    "User-Agent":    "push-notes/1.0",
}
BASE_URL = f"https://api.github.com/repos/{REPO}/contents"
DIR      = os.path.dirname(os.path.abspath(__file__))

FILES = [
    ("seed_concept_notes_national.py", "Add National CA concept notes (bilingual, 3 tags)"),
    ("app.py",                          "Wire seed_concept_notes_national into startup cache loader"),
]

def get_sha(path):
    """Return current SHA of file on GitHub, or None if it doesn't exist yet."""
    url = f"{BASE_URL}/{path}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())["sha"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None   # new file — no SHA required
        raise

def push_file(path, msg):
    local = os.path.join(DIR, path)
    with open(local, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    sha = get_sha(path)
    url = f"{BASE_URL}/{path}"
    body = {"message": msg, "content": b64}
    if sha:
        body["sha"] = sha   # update existing
    payload = json.dumps(body).encode()
    req = urllib.request.Request(url, data=payload, headers=HEADERS, method="PUT")
    with urllib.request.urlopen(req, timeout=60) as r:
        result = json.loads(r.read())
        return result["commit"]["sha"]

for fpath, msg in FILES:
    print(f"Pushing {fpath} ...")
    commit = push_file(fpath, msg)
    print(f"  ✅  commit {commit}")

print("\nAll done — Railway will redeploy in ~1-2 min.")
print("After deploy, visit /notes/national_ca_budget to verify rich notes appear.")
