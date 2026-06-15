#!/usr/bin/env python3
"""Structural audit of all 12 km files."""
import re, os, glob

base = '/home/ole/workspace/driftsstotte-vg2/src/content/kompetansemaal'

required_sections = [
    '🎯 Mål / Competency Goal',
    '📘 Forklaring / Explanation',
    '💡 Eksempler / Examples',
    '📝 Oppsummering / Summary',
    '🔧 Bridging Exercises / Praksisoppgaver',
    '🔗 Relevante artikler / Related Articles',
    '📚 Kilder / Sources',
]

required_language_elements = [
    '### Norsk',
    '### English',
]

print(f"{'File':45s} {'Sections':8s} {'Lang':5s} {'Bridges':8s} {'Status':8s}")
print('-' * 80)

for f in sorted(glob.glob(os.path.join(base, 'km-*.md'))):
    basename = os.path.basename(f)
    with open(f) as fh:
        content = fh.read()
    
    # Check all required sections
    sections_found = sum(1 for s in required_sections if s in content)
    sections_ok = sections_found == len(required_sections)
    
    # Check bilingual
    lang_ok = all(lang in content for lang in required_language_elements)
    
    # Check bridging exercises have both languages
    has_no_bridge = '### Norsk — Praksisoppgaver' in content
    has_en_bridge = '### English — Practical Exercises' in content
    bridges_ok = has_no_bridge and has_en_bridge
    
    issues = []
    if not sections_ok:
        missing = [s for s in required_sections if s not in content]
        issues.append(f"missing: {missing}")
    if not lang_ok:
        issues.append("missing bilingual sections")
    if not bridges_ok:
        issues.append("missing practical exercises in one language")
    
    status = 'PASS' if (sections_ok and lang_ok and bridges_ok) else 'FAIL'
    summary = f"{sections_found}/{len(required_sections)}"
    
    print(f"{basename:45s} {summary:8s} {'OK' if lang_ok else 'MISS':5s} {'OK' if bridges_ok else 'MISS':8s} {status:8s}")
    if issues:
        for issue in issues:
            print(f"  {'':45s} → {issue}")
