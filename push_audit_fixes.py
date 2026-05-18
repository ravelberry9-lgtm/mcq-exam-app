#!/usr/bin/env python3
"""
Push all audited AP CA MCQ fixes and new concept notes to GitHub.
Run with: GITHUB_TOKEN=ghp_xxx python push_audit_fixes.py
"""
import os, json, base64, urllib.request, urllib.error

REPO   = "ravelberry9-lgtm/mcq-exam-app"
BRANCH = "main"
TOKEN  = os.environ.get("GITHUB_TOKEN", "")
BASE   = f"https://api.github.com/repos/{REPO}/contents"

if not TOKEN:
    raise SystemExit("ERROR: Set GITHUB_TOKEN environment variable first.\n"
                     "  Windows: set GITHUB_TOKEN=ghp_...\n"
                     "  Then run: python push_audit_fixes.py")

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json",
}

script_dir = os.path.dirname(os.path.abspath(__file__))

# All files to push with their commit messages
FILES = [
    # Fixed MCQ seed files
    ("seed_ap_ca_div1.py",             "fix: div1 MCQs — DGP name, CS name, Darsi district"),
    ("seed_ap_ca_div2.py",             "fix: div2 MCQs — Deepam 2.0 wait time 48h (not 3 months)"),
    ("seed_ap_ca_div3.py",             "fix: div3 MCQs — Yogandhra count 3.01 lakh (not 5 lakh)"),
    ("seed_ap_ca_div4.py",             "fix: div4 MCQs — CII 45 countries (not 61), 2014 AP 13 districts"),
    ("seed_ap_ca_div8.py",             "fix: div8 MCQs — SDSC SHAR Tirupati dist, Rollapadu Nandyal, Polavaram S94"),
    ("seed_ap_ca_div9.py",             "fix: div9 MCQs — K.Viswanath award, MM Keeravani district, Balakrishna Padma Bhushan"),
    # New concept notes seeders
    ("seed_concept_notes_div1div2.py",       "feat: concept notes div1+div2 — 17 rich notes (cabinet, elections, schemes)"),
    ("seed_concept_notes_div3div4.py",       "feat: concept notes div3+div4 — 21 rich notes (events Jan-Apr 2026)"),
    ("seed_concept_notes_div5div6div7.py",   "feat: concept notes div5+6+7 — 27 rich notes (arts, economy, history)"),
    ("seed_concept_notes_div8div9div10.py",  "feat: concept notes div8+9+10 — 27 rich notes (env, sports, awards, APRA)"),
    # Updated app.py to wire new seeders
    ("app.py",                         "feat: wire 4 new div concept notes seeders in _load_concept_cache"),
]


def get_sha(path):
    url = f"{BASE}/{path}?ref={BRANCH}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())["sha"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def push_file(fname, msg):
    local = os.path.join(script_dir, fname)
    if not os.path.exists(local):
        print(f"  ⚠️  SKIP {fname} — file not found locally")
        return
    with open(local, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    sha = get_sha(fname)
    body = {"message": msg, "content": b64, "branch": BRANCH}
    if sha:
        body["sha"] = sha
    data = json.dumps(body).encode()
    req = urllib.request.Request(f"{BASE}/{fname}", data=data, headers=HEADERS, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            result = json.loads(r.read())
            print(f"  ✅  {fname} → commit {result['commit']['sha'][:8]}")
    except urllib.error.HTTPError as e:
        body_err = e.read()[:300].decode("utf-8", errors="replace")
        print(f"  ❌  {fname} failed: HTTP {e.code}: {body_err}")


print(f"Pushing {len(FILES)} files to {REPO} (branch: {BRANCH})...\n")
for fname, msg in FILES:
    print(f"Pushing {fname}...")
    push_file(fname, msg)

print("\n✅ All done! Railway will auto-redeploy in ~1-2 minutes.")
print("   Visit: https://web-production-ac9f2.up.railway.app/practice")
print("   → AP Current Affairs → pick any topic → verify MCQs + concept notes")
