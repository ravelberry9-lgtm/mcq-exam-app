#!/usr/bin/env python3
import ast
import sys

try:
    with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
        code = f.read()

    ast.parse(code)
    print("✓ AST Validation: PASSED")
    print("✓ The Python file has valid syntax")
    sys.exit(0)
except SyntaxError as e:
    print(f"✗ Syntax Error: {e}")
    print(f"  Line {e.lineno}: {e.text}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
