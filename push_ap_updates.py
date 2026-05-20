#!/usr/bin/env python3
"""Push AP CA updates to GitHub: seed_concept_notes_ap.py, seed_ap_ca_2026_mcq.py, app.py"""
import base64, json, urllib.request, urllib.error

REPO   = "ravelberry9-lgtm/mcq-exam-app"
BRANCH = "main"
TOKEN  = ""  # set via GITHUB_TOKEN env var
BASE   = f"https://api.github.com/repos/{REPO}/contents"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json",
}

FILES = [
    "seed_concept_notes_ap.py",
    "seed_ap_ca_2026_mcq.py",
    "app.py",
]

import os
script_dir = os.path.dirname(os.path.abspath(__file__))

def get_sha(path):
    url = f"{BASE}/{path}?ref={BRANCH}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())["sha"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise

def push_file(local_path, remote_path, message):
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    sha = get_sha(remote_path)
    payload = {"message": message, "content": content, "branch": BRANCH}
    if sha:
        payload["sha"] = sha
    data = json.dumps(payload).encode()
    req = urllib.request.Request(f"{BASE}/{remote_path}", data=data, headers=HEADERS, method="PUT")
    try:
        with urllib.request.urlopen(req) as r:
            result = json.loads(r.read())
            print(f"  ✅ {remote_path} → {result['commit']['sha'][:8]}")
    except urllib.error.HTTPError as e:
        print(f"  ❌ {remote_path} failed: {e.code} {e.read()[:200]}")

for fname in FILES:
    local = os.path.join(script_dir, fname)
    print(f"Pushing {fname}...")
    push_file(local, fname, f"feat: AP CA updates — {fname}")

print("\nDone! Railway will auto-redeploy and seed AP concept notes on restart.")
