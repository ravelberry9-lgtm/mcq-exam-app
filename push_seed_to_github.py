#!/usr/bin/env python3
"""
Push seed_national_ca_2026_mcq.py (300 questions) to GitHub.
Run with: python push_seed_to_github.py
"""

import os
import json
import base64
import urllib.request
import urllib.error

# ── Configuration ──────────────────────────────────────────────────────────
REPO = "ravelberry9-lgtm/mcq-exam-app"
PAT  = ""  # set via GITHUB_TOKEN env var
FILE_PATH   = "seed_national_ca_2026_mcq.py"
COMMIT_MSG  = "Expand National CA MCQs from 80 to 300 questions (IDs 31001-31300)"
API_URL     = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
HEADERS     = {
    "Authorization": f"token {PAT}",
    "Content-Type":  "application/json",
    "Accept":        "application/vnd.github.v3+json",
    "User-Agent":    "seed-push-script/1.0",
}

# ── Step 1: Read local file ────────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
local_path = os.path.join(script_dir, FILE_PATH)

print(f"[1/4] Reading local file: {local_path}")
with open(local_path, "rb") as f:
    raw_bytes = f.read()
print(f"      Size: {len(raw_bytes):,} bytes")

# ── Step 2: Base64 encode ──────────────────────────────────────────────────
print("[2/4] Encoding to base64 ...")
content_b64 = base64.b64encode(raw_bytes).decode("ascii")
print(f"      Base64 length: {len(content_b64):,} chars")

# ── Step 3: Get current SHA from GitHub ───────────────────────────────────
print("[3/4] Fetching current file SHA from GitHub ...")
req = urllib.request.Request(API_URL, headers=HEADERS)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
        current_sha = data["sha"]
        print(f"      Current SHA: {current_sha}")
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8", errors="replace")
    print(f"      HTTP {e.code}: {body}")
    raise SystemExit(1)

# ── Step 4: Push to GitHub ─────────────────────────────────────────────────
print("[4/4] Pushing to GitHub ...")
payload = json.dumps({
    "message": COMMIT_MSG,
    "content": content_b64,
    "sha":     current_sha,
}).encode("utf-8")

req = urllib.request.Request(API_URL, data=payload, headers=HEADERS, method="PUT")
try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        result    = json.loads(resp.read())
        new_sha   = result["content"]["sha"]
        commit_sha = result["commit"]["sha"]
        print()
        print("✅  SUCCESS!")
        print(f"    New file SHA  : {new_sha}")
        print(f"    Commit SHA    : {commit_sha}")
        print()
        print("Railway will auto-redeploy in ~1-2 minutes.")
        print("Then visit: https://web-production-ac9f2.up.railway.app/")
        print("  → Practice → National Current Affairs to verify 300 questions load.")
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8", errors="replace")
    print(f"HTTP {e.code} error: {body}")
    raise SystemExit(1)
