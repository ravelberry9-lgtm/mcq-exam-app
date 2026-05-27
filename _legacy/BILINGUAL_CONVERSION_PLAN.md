# MCQ Bilingual Conversion - Complete Action Plan

**Status as of 2026-05-22**

## Current Progress
- **Total MCQs to convert**: 345 (IDs 31431-31775)
- **File**: seed_national_ca_2026_mcq.py (5076 lines, 775 MCQs total)
- **Safe method**: Python string replacement via mcp__workspace__bash (avoid Edit tool truncation)

## Bucket Status

### ✓ Bucket D - Mixed with Hindi Residue (6 IDs)
- **Status**: 83% complete (5 of 6 bilingual)
- **IDs**: 31476-31480, 31514
- **Work**: 1 ID remaining (31514 - needs format conversion from English|Telugu to Telugu\nEnglish)
- **Estimated time**: 5 minutes

### 🟡 Bucket A - Hindi-only Translation (101 IDs)
- **Status**: 30% complete (3 of 10 sample bilingual)
- **IDs**: 31451-31475, 31510, 31581-31615, 31736-31775
- **Components**:
  - Pure Hindi entries (24): Full translation from Hindi → Telugu+English needed
  - Mixed Hindi+English entries (77): Format fixes + completing missing language
- **Source**: HAIKU_INPUT_broken_source.py has original Hindi content
- **Work approach**:
  1. Extract Hindi question, options, explanation
  2. Translate to Telugu (if not already present)
  3. Translate to English (if not already present)
  4. Format as bilingual: "Telugu\nEnglish" for Q/Expl, "A) Telugu | English" for options
  5. Apply via Python string replacement in batches of 10-15
  6. Verify with AST parse, line count check, tail marker "775 MCQs total"
- **Estimated time**: 2-3 hours (manual translation required)

### ❌ Bucket C - Partial Needs Fix (68 IDs)
- **Status**: 0% complete
- **IDs**: 31431-31450, 31501-31550
- **Analysis**: All 20 sampled entries have Telugu-only questions, missing English
- **Work approach**:
  1. Extract Telugu question text
  2. Translate Telugu → English (or find equivalent English from context)
  3. Create bilingual format with newline: "Telugu\nEnglish"
  4. Convert options to bilingual format with pipe: "A) Telugu | English"
  5. Handle explanations (currently mixed - some have English, need Telugu)
  6. Apply in batches via Python string replacement
- **Challenge**: Requires translating Telugu → English (no source reference available)
- **Estimated time**: 2 hours (if efficient translation method used)

### ❌ Bucket B - English-only Needs Telugu (150 IDs)
- **Status**: 0% complete
- **IDs**: 31551-31580, 31616-31735 (excluding already processed)
- **Analysis**: All entries are pure English (modern governance policies 2024-2025)
- **Work approach**:
  1. Extract English question
  2. Translate English → Telugu
  3. Create bilingual format: "Telugu\nEnglish"
  4. Convert options to bilingual format with pipe
  5. Translate explanations (English) → Telugu
  6. Apply in large batches
- **Challenge**: Large volume (150 IDs) + domain-specific terms (policy names, acronyms)
- **Strategy**: Can use template approach for common terms to speed up
- **Estimated time**: 2-3 hours

## Implementation Strategy for Remaining Work

### Phase 1: Quick Wins (Bucket D Completion)
```python
# Find ID 31514, convert format from English|Telugu to proper bilingual
# This is a 5-minute fix
```

### Phase 2: Efficient Batch Processing (All Buckets)
1. **Extract all remaining MCQs** → Save to JSON with ID as key
2. **Create translation mappings** → Build dict of {old_text: new_text}
3. **Apply via Python string replace** in batches of 15 IDs
4. **Verify after each batch**:
   - AST parse successful
   - Line count maintained (~5076 lines)
   - Tail marker "775 MCQs total" intact

### Phase 3: Verification
```python
# Final verification script:
# 1. Parse entire file with AST
# 2. Count AP_HC entries (should be ≥345)
# 3. Count Devanagari chars in remaining (should be 0 for Hindi)
# 4. Count Telugu chars (should be significant)
# 5. Spot-check 10 random entries from each bucket
# 6. Ensure no tuple truncation or malformation
```

## Safe File Manipulation Rules (CRITICAL)

### ✅ SAFE: Python String Replacement
```python
with open('seed_national_ca_2026_mcq.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Build replacement dict
replacements = {'old_text': 'new_text', ...}

# Apply replacements
for old, new in replacements.items():
    if old in content:
        content = content.replace(old, new)

# Verify AST
compile(content, 'filename.py', 'exec')

# Write back
with open('seed_national_ca_2026_mcq.py', 'w', encoding='utf-8') as f:
    f.write(content)
```

### ❌ NEVER USE: Edit Tool
- Caused file truncation at line 5053 in previous session
- Large string replacements on multi-line tuples cause encoding issues
- **Always use Python string replacement instead**

### ❌ NEVER USE: Write Tool (Full File Rewrite)
- Risk of losing file structure
- Python string replacement is safer and more reliable

## Translation Reference Sources
- **Bucket A**: HAIKU_INPUT_broken_source.py (Hindi source for MCQs 31451+)
- **Bucket C**: Requires Telugu→English translation (no source file)
- **Bucket B**: Requires English→Telugu translation (modern 2024-2025 policies)

## Next Session Checklist
- [ ] Complete Bucket D (1 remaining ID)
- [ ] Translate remaining Bucket A entries (partial implementation started)
- [ ] Implement Bucket C (68 partial fixes)
- [ ] Implement Bucket B (150 English→Telugu)
- [ ] Run final verification script
- [ ] Confirm all 345 MCQs are properly bilingual
- [ ] Deploy to production/test database

## Key Metrics to Track
- **Bilingual conversion %**: (# bilingual MCQs) / 345 * 100
- **File integrity**: Line count should stay at ~5076
- **Character counts**: Track Devanagari (should decrease), Telugu (should increase)
- **AP_HC folder count**: Should be ≥345

---
**Last Updated**: 2026-05-22 (Haiku Agent - Session 2)
**Progress**: ~26 MCQs bilingual, 319 remaining
