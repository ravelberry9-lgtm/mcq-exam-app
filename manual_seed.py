#!/usr/bin/env python3
"""Manual seeding script to populate AP CA div3 and div4 MCQs."""

import sqlite3
import sys
import os

# Import the seed module functions
sys.path.insert(0, '/sessions/adoring-brave-ptolemy/mnt/mcq_app')

from seed_ap_ca_div3 import _seed_ap_ca_div3_notes_inner, _seed_ap_ca_div3_mcqs_inner
from seed_ap_ca_div4 import _seed_ap_ca_div4_notes_inner, _seed_ap_ca_div4_mcqs_inner

def dict_from_row(row):
    """Convert SQLite row to dict."""
    if isinstance(row, dict):
        return row
    return dict(row) if hasattr(row, 'keys') else {}

def main():
    conn = sqlite3.connect('questions.db')
    conn.row_factory = sqlite3.Row  # Enable dict-like access

    def db_exec(conn, query, params=()):
        """Execute a query with proper parameter handling."""
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            return cursor
        except Exception as e:
            print(f"Error executing: {query[:100]}")
            print(f"  Params: {params}")
            print(f"  Error: {e}")
            return cursor

    def row_to_dict(row):
        """Convert row to dict."""
        if row is None:
            return {}
        if isinstance(row, dict):
            return row
        if hasattr(row, 'keys'):
            return dict(row)
        return {}

    print("Seeding AP CA Division 3...")
    result1 = _seed_ap_ca_div3_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES=False, force=True)
    print(f"  Notes: {result1}")

    result2 = _seed_ap_ca_div3_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES=False, force=True)
    print(f"  MCQs: Seeded")

    print("\nSeeding AP CA Division 4...")
    result3 = _seed_ap_ca_div4_notes_inner(conn, db_exec, row_to_dict, USE_POSTGRES=False, force=True)
    print(f"  Notes: {result3}")

    result4 = _seed_ap_ca_div4_mcqs_inner(conn, db_exec, row_to_dict, USE_POSTGRES=False)
    print(f"  MCQs: Seeded")

    conn.commit()

    # Verify
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM chapter_mcqs")
    count = cursor.fetchone()[0]
    print(f"\n✓ Total MCQs in database: {count}")

    cursor.execute("""SELECT COUNT(*) FROM chapter_mcqs
                     WHERE q_te LIKE '%క్వాంటం%' OR q_te LIKE '%Quantum%'""")
    quantum_count = cursor.fetchone()[0]
    print(f"✓ IBM Quantum MCQs: {quantum_count}")

    conn.close()

if __name__ == '__main__':
    main()
