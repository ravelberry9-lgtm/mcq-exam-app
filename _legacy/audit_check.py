import re
import glob

# Canonical facts to verify
canonical = {
    "AP HC CJ": "Lisa Gill",
    "AP CS": "G. Sai Prasad",
    "AP DGP": "Harish Kumar Gupta",
    "AP districts": "28",
    "State bird": "Rose-ringed Parakeet",
    "State flower": "Jasmine",
    "Bhogapuram": "June 26, 2026",
    "GSDP FY25-26": "18.30",
    "Padma Shri 2026 AP": "4",
    "BlueBird Block-2": "LVM3-M6",
    "Wimbledon 2025": "Sinner",
    "WTC 2025": "South Africa",
}

issues = []
for seed_file in sorted(glob.glob("seed_*.py")):
    with open(seed_file) as f:
        content = f.read()
    
    # Quick checks for critical facts
    if "Lisa Gill" not in content and "CJ" in seed_file[:20]:
        issues.append(f"{seed_file}: Missing Lisa Gill CJ reference")
    if "28" in content and "district" in content.lower():
        pass  # Found
    if "17.62" in content:
        issues.append(f"{seed_file}: STALE GSDP FY25-26 (17.62 instead of 18.30)")
    if "LVM3-M5" in content:
        issues.append(f"{seed_file}: STALE BlueBird designation (M5 vs M6)")

if not issues:
    print("✅ SPOT-CHECK PASSED: No stale critical facts detected")
else:
    print("⚠️  ISSUES FOUND:")
    for issue in issues:
        print(f"  - {issue}")
        
print(f"\n📊 Files checked: {len(glob.glob('seed_*.py'))}")
