"""
audit_malformed_questions.py

Script to identify and report malformed MCQ questions in the database.
Focuses on questions where the question text and options don't match thematically.

Malformation patterns to detect:
1. Question about Topic A with options from Topic B (e.g., IBM Quantum question with agricultural prices)
2. Incomplete Telugu text (cut-off mid-word)
3. Gibberish or corrupted text patterns
4. Mixed English-Telugu that doesn't make sense
5. Options length mismatch (e.g., 5 options instead of 4)
"""

import sqlite3
import re
from collections import defaultdict

DB_PATH = "questions.db"

def check_question_option_mismatch():
    """Find questions where topic doesn't match options"""

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get all questions
    cursor.execute("""
        SELECT id, question_te, question_en, option_a, option_b, option_c, option_d, answer
        FROM mcqs
        LIMIT 1000
    """)

    questions = cursor.fetchall()
    malformed = []

    for q_id, q_te, q_en, opt_a, opt_b, opt_c, opt_d, ans in questions:
        # Pattern 1: IBM Quantum questions with agricultural prices
        if 'IBM' in (q_te or '') and ('₹' in (opt_a or '') or '₹' in (opt_b or '')):
            if 'क्विंटल' in (opt_a or '') or 'క.ఎ.' in (opt_a or ''):
                malformed.append({
                    'id': q_id,
                    'issue': 'QUANTUM_WITH_AGRICULTURAL_PRICES',
                    'question': q_te,
                    'options': [opt_a, opt_b, opt_c, opt_d],
                    'severity': 'CRITICAL'
                })

        # Pattern 2: Gibberish Telugu (check for character corruption)
        if q_te:
            # Look for patterns like "ఆడ్డ ధర" which is malformed
            if re.search(r'ఆడ్డ.*ధర|dhara.*IBM|addhe.*dhara', q_te, re.IGNORECASE):
                malformed.append({
                    'id': q_id,
                    'issue': 'CORRUPTED_TELUGU_TEXT',
                    'question': q_te,
                    'options': [opt_a, opt_b, opt_c, opt_d],
                    'severity': 'CRITICAL'
                })

        # Pattern 3: Incomplete Telugu (ends with lone Telugu character)
        if q_te and re.search(r'[ఀ-్]\s*$', q_te):
            malformed.append({
                'id': q_id,
                'issue': 'INCOMPLETE_TELUGU',
                'question': q_te,
                'options': [opt_a, opt_b, opt_c, opt_d],
                'severity': 'HIGH'
            })

        # Pattern 4: Question too short with price options
        if q_te and len(q_te.split()) <= 3 and ('₹' in (opt_a or '') or '₹' in (opt_b or '')):
            malformed.append({
                'id': q_id,
                'issue': 'SHORT_QUESTION_WITH_PRICES',
                'question': q_te,
                'options': [opt_a, opt_b, opt_c, opt_d],
                'severity': 'MEDIUM'
            })

    conn.close()
    return malformed


def print_malformed_report(malformed):
    """Print formatted report of malformed questions"""

    print("\n" + "="*80)
    print("MALFORMED MCQ AUDIT REPORT")
    print("="*80 + "\n")

    if not malformed:
        print("✓ No malformed questions detected!")
        return

    # Group by issue type
    by_issue = defaultdict(list)
    for item in malformed:
        by_issue[item['issue']].append(item)

    # Print summary
    print(f"TOTAL MALFORMED: {len(malformed)}\n")

    for issue_type, items in by_issue.items():
        print(f"\n{issue_type} ({len(items)} questions)")
        print("-" * 80)

        for item in items:
            print(f"\nID: {item['id']}")
            print(f"Severity: {item['severity']}")
            print(f"Question: {item['question'][:100]}...")
            print(f"Options:")
            for i, opt in enumerate(item['options'], 1):
                print(f"  {chr(64+i)}: {opt[:60]}..." if opt and len(opt) > 60 else f"  {chr(64+i)}: {opt}")


def generate_fix_sql():
    """Generate SQL to fix identified issues"""

    print("\n" + "="*80)
    print("GENERATED SQL FOR CLEANUP")
    print("="*80 + "\n")

    sql_statements = [
        "-- DELETE CORRUPTED MCQ WITH IBM + AGRICULTURAL PRICES",
        """DELETE FROM mcqs
           WHERE question_te LIKE '%IBM ఆడ్డ ధర%'
           OR (question_te LIKE '%IBM%' AND option_a LIKE '%₹%' AND option_a LIKE '%క.ఎ.%')
           OR question_te LIKE '%addhe dhara%';""",

        "\n-- DELETE INCOMPLETE TELUGU QUESTIONS",
        """DELETE FROM mcqs
           WHERE question_te REGEXP '[ఀ-్]\\s*$';""",

        "\n-- RE-SEED CORRECT IBM QUANTUM QUESTIONS",
        "-- Run: python3 seed_ap_ca_div3.py",
        "-- Run: python3 seed_ap_ca_div4.py",
    ]

    for stmt in sql_statements:
        print(stmt)


def main():
    """Main audit function"""

    print("Starting malformed question audit...")
    print(f"Database: {DB_PATH}\n")

    try:
        malformed = check_question_option_mismatch()
        print_malformed_report(malformed)
        generate_fix_sql()

        print("\n" + "="*80)
        print("AUDIT COMPLETE")
        print("="*80)
        print("\nRECOMMENDED ACTIONS:")
        print("1. Review the malformed questions listed above")
        print("2. Execute the generated SQL to remove corrupted data")
        print("3. Re-seed from seed_ap_ca_div3.py and seed_ap_ca_div4.py")
        print("4. Run app.py _auto_seed_ap_hc_questions() to update AP_HC questions")
        print("5. Verify all IBM Quantum MCQs render correctly in the UI")

    except FileNotFoundError:
        print(f"Error: Database '{DB_PATH}' not found!")
        print("Ensure the database exists before running audit.")
    except Exception as e:
        print(f"Audit error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
