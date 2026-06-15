#!/usr/bin/env python3
"""Additional independent QA checks for km files."""
import os, re, sys

base_km = 'src/content/kompetansemaal'
base_emner = 'src/content/emner'

km_files = sorted(f for f in os.listdir(base_km) if f.startswith('km-') and f.endswith('.md'))

# Build known emner slugs
known_emner = set()
for root, dirs, files in os.walk(base_emner):
    for fn in files:
        if fn.endswith('.md') or fn.endswith('.mdx'):
            known_emner.add(fn.replace('.md', '').replace('.mdx', ''))

print("=== WIKILINK VERIFICATION ===")
all_ok = True
for fn in km_files:
    with open(os.path.join(base_km, fn)) as f:
        content = f.read()
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
    for link in wikilinks:
        slug = link.split('|')[0].strip()
        if slug not in known_emner:
            # Check if it's a km-x link pattern
            if not slug.startswith('km-'):
                print(f"  WARN: {fn}: wikilink [[{link}]] → '{slug}' not found in emner/")
                all_ok = False

if all_ok:
    print("  All wikilinks resolve to known emner files.")

print()
print("=== BRIDGING EXERCISES CHECK ===")
for fn in km_files:
    with open(os.path.join(base_km, fn)) as f:
        content = f.read()
    
    has_no_heading = '### Norsk — Praksisoppgaver' in content
    has_en_heading = '### English — Practical Exercises' in content
    
    # Count exercises (## Oppgave / ## Exercise)
    no_exercises = len(re.findall(r'^## Oppgave \d', content, re.MULTILINE))
    en_exercises = len(re.findall(r'^## Exercise \d', content, re.MULTILINE))
    
    status = 'OK' if (no_exercises >= 2 and en_exercises >= 2) else 'ISSUE'
    print(f"  {fn:<38} NO-oppgaver:{no_exercises} EN-exercises:{en_exercises} [{status}]")

print()
print("=== REQUIRED SECTIONS CHECK ===")
expected_headings = [
    'Mål / Competency Goal',
    'Forklaring / Explanation',
    'Eksempler / Examples',
    'Oppsummering / Summary',
    'Bridging Exercises / Praksisoppgaver',
    'Relevante artikler / Related Articles',
    'Kilder / Sources',
]
for fn in km_files:
    with open(os.path.join(base_km, fn)) as f:
        content = f.read()
    sections = re.findall(r'^## [^#].*', content, re.MULTILINE)
    missing = [h for h in expected_headings if not any(h in s for s in sections)]
    if missing:
        print(f"  ISSUE: {fn} missing sections: {missing}")
    else:
        # count sections
        print(f"  OK: {fn:<38} ({len(sections)} sections)")

print()
print("=== YAML FRONTMATTER CHECK ===")
for fn in km_files:
    with open(os.path.join(base_km, fn)) as f:
        content = f.read()
    parts = content.split('---')
    if len(parts) < 3:
        print(f"  FAIL: {fn} — no YAML frontmatter")
        continue
    
    yaml_block = parts[1]
    required = ['title', 'emne', 'kompetansemaal', 'kilder', 'tags', 'public']
    for key in required:
        if key + ':' not in yaml_block:
            print(f"  FAIL: {fn} — missing '{key}' in frontmatter")
            break
    else:
        print(f"  OK: {fn}")
