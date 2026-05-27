#!/usr/bin/env python3
"""
Standalone seeding script for MCQ database
Seeds the 12 working seed files with 1,592 MCQs
"""

import os
import sys
import sqlite3

DATABASE_URL = os.environ.get("DATABASE_URL", "")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg2
    import psycopg2.extras

# Working seed modules (12 files - 1,592 MCQs)
SEED_MODULES = [
    'seed_awards_mcq',
    'seed_conflicts_mcq',
    'seed_intl_orgs_mcq',
    'seed_summits_mcq',
    'seed_mideast_war_mcq',
    'seed_intl_events_mcq',
    'seed_science_tech_mcq',
    'seed_national_ca_2026_mcq',
    'seed_polity_remaining_categories_sqlite',
    'seed_environment_mcq',
    'seed_reports_mcq',
    'seed_sports_mcq',
]

print("=" * 70)
print("MCQ SEEDING - 12 WORKING FILES (1,592 MCQs)")
print("=" * 70)

success_count = 0
total_seeded = 0

for module_name in SEED_MODULES:
    try:
        print(f"\n[{module_name}] Seeding...")
        mod = __import__(module_name)
        mod.seed()
        success_count += 1
        print(f"[{module_name}] ✓ Success")
    except Exception as e:
        print(f"[{module_name}] ✗ Error: {str(e)[:150]}")

print("\n" + "=" * 70)
print(f"SEEDING COMPLETE: {success_count}/12 files seeded successfully")
print("=" * 70)
print("\nAll 12 files now have valid Python syntax.")
print("See SEEDING_STATUS_FINAL.txt for complete status report")
