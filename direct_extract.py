#!/usr/bin/env python3
"""
Direct extraction of MCQs 31676-31725 from seed file
Uses Python's ast module to safely parse the file
"""

import ast
import sys

def extract_questions_from_seed():
    """Parse seed file and extract MCQ tuples"""

    # Read the file
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse as Python code
    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"ERROR: Could not parse seed file: {e}")
        return None

    # Find the seed function definition
    seed_func = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'seed':
            seed_func = node
            break

    if not seed_func:
        print("ERROR: Could not find seed() function")
        return None

    # Look for the questions assignment
    questions_list = None
    for node in seed_func.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'questions':
                    questions_list = node.value
                    break

    if not questions_list:
        print("ERROR: Could not find 'questions' list in seed() function")
        return None

    # Extract tuples (ast.Tuple nodes)
    mcqs = {}
    if isinstance(questions_list, ast.List):
        for element in questions_list.elts:
            if isinstance(element, ast.Tuple) and len(element.elts) >= 1:
                # First element is the MCQ ID (ast.Constant)
                id_node = element.elts[0]
                if isinstance(id_node, ast.Constant):
                    mcq_id = id_node.value
                    if 31676 <= mcq_id <= 31725:
                        # Extract all elements
                        elements = []
                        for elt in element.elts:
                            if isinstance(elt, ast.Constant):
                                elements.append(elt.value)
                            elif isinstance(elt, ast.JoinedStr):
                                # f-string, complex handling needed
                                elements.append("[f-string]")
                            else:
                                elements.append(f"[{type(elt).__name__}]")

                        mcqs[mcq_id] = elements

    return mcqs

def main():
    print("Extracting MCQs 31676-31725...")
    mcqs = extract_questions_from_seed()

    if not mcqs:
        print("FAILED to extract MCQs")
        return False

    print(f"Successfully extracted {len(mcqs)} MCQs")

    # Sort by ID
    sorted_ids = sorted(mcqs.keys())
    print(f"ID range: {min(sorted_ids)} to {max(sorted_ids)}")

    # Show structure of first MCQ
    if sorted_ids:
        sample_id = sorted_ids[0]
        elements = mcqs[sample_id]
        print(f"\nMCQ {sample_id} has {len(elements)} elements:")
        print(f"  [0] ID: {elements[0]}")
        print(f"  [1] Question: {str(elements[1])[:100]}")
        print(f"  [2] Opt A: {str(elements[2])[:50]}")
        print(f"  [3] Opt B: {str(elements[3])[:50]}")
        print(f"  [4] Opt C: {str(elements[4])[:50]}")
        print(f"  [5] Opt D: {str(elements[5])[:50]}")
        print(f"  [6] Answer: {elements[6]}")
        print(f"  [7] Explanation: {str(elements[7])[:100]}")
        print(f"  [8] Folder: {elements[8]}")
        print(f"  [9] Topic: {elements[9]}")

    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
