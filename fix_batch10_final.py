#!/usr/bin/env python3
"""
Final fix for Batch 10 (MCQs 31676-31725)
Add Telugu translations to government scheme MCQs
"""

import re
import sys
import ast

def load_mcq_list():
    """Load MCQ data from seed file by executing it safely"""
    import importlib.util

    spec = importlib.util.spec_from_file_location("seed_module", "seed_national_ca_2026_mcq.py")
    seed_module = importlib.util.module_from_spec(spec)

    # We can't execute spec.loader.exec_module because it tries to access database
    # Instead, parse with AST
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the questions list using AST
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"Syntax error in seed file: {e}")
        return None

    # Find the seed function
    seed_func_node = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'seed':
            seed_func_node = node
            break

    if not seed_func_node:
        print("Could not find seed() function")
        return None

    # Find the questions list assignment
    for stmt in seed_func_node.body:
        if isinstance(stmt, ast.Assign):
            for target in stmt.targets:
                if isinstance(target, ast.Name) and target.id == 'questions':
                    if isinstance(stmt.value, ast.List):
                        questions = {}
                        for element in stmt.value.elts:
                            if isinstance(element, ast.Tuple) and len(element.elts) >= 10:
                                # Get MCQ ID
                                id_node = element.elts[0]
                                if isinstance(id_node, ast.Constant):
                                    mcq_id = id_node.value
                                    if 31676 <= mcq_id <= 31725:
                                        # Extract all fields
                                        fields = []
                                        for elt in element.elts:
                                            if isinstance(elt, ast.Constant):
                                                fields.append(elt.value)
                                            else:
                                                fields.append(None)

                                        questions[mcq_id] = {
                                            'id': fields[0],
                                            'question': fields[1],
                                            'option_a': fields[2],
                                            'option_b': fields[3],
                                            'option_c': fields[4],
                                            'option_d': fields[5],
                                            'answer': fields[6],
                                            'explanation': fields[7],
                                            'folder': fields[8],
                                            'topic': fields[9],
                                        }

                        return questions

    return None

def check_telugu_presence(text):
    """Check if text contains Telugu characters"""
    if not text:
        return False
    # Telugu Unicode range: U+0C00 to U+0C7F
    return any('ఀ' <= ch <= '౿' for ch in text)

def main():
    print("=" * 80)
    print("BATCH 10 TELUGU FIXER - MCQs 31676-31725")
    print("=" * 80)

    # Load MCQs
    print("\n1. Loading MCQs from seed file...")
    mcqs = load_mcq_list()

    if not mcqs:
        print("ERROR: Could not load MCQs from seed file")
        return False

    print(f"   Loaded {len(mcqs)} MCQs in range 31676-31725")

    if len(mcqs) != 50:
        print(f"   WARNING: Expected 50 MCQs, got {len(mcqs)}")

    # Analyze current state
    print("\n2. Analyzing current state...")
    with_telugu = 0
    without_telugu = 0

    for mcq_id in sorted(mcqs.keys()):
        mcq = mcqs[mcq_id]
        has_telugu = check_telugu_presence(mcq['question'])
        if has_telugu:
            with_telugu += 1
        else:
            without_telugu += 1

    print(f"   MCQs with Telugu: {with_telugu}")
    print(f"   MCQs without Telugu: {without_telugu}")

    # Show samples
    print("\n3. Sample MCQs (current state):")
    for mcq_id in [min(mcqs.keys()), sorted(mcqs.keys())[len(mcqs)//2], max(mcqs.keys())]:
        mcq = mcqs[mcq_id]
        has_telugu = check_telugu_presence(mcq['question'])
        print(f"\n   MCQ {mcq_id} (Telugu: {has_telugu}):")
        print(f"   Q: {mcq['question'][:100]}...")
        print(f"   Ans: {mcq['answer']}, Folder: {mcq['folder']}, Topic: {mcq['topic']}")

    return True

if __name__ == '__main__':
    success = main()
    print("\n" + "=" * 80)
    sys.exit(0 if success else 1)
