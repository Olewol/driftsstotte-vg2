#!/usr/bin/env python3
"""Fix exercise count check — exercises are **bold** not ## headings."""
import os, re

base_km = 'src/content/kompetansemaal'
km_files = sorted(f for f in os.listdir(base_km) if f.startswith('km-') and f.endswith('.md'))

print("=== BRIDGING EXERCISES (bold format) ===")
for fn in km_files:
    with open(os.path.join(base_km, fn)) as f:
        content = f.read()
    
    no_exercises = len(re.findall(r'\*\*Oppgave \d:', content))
    en_exercises = len(re.findall(r'\*\*Exercise \d:', content))
    
    status = 'OK' if (no_exercises >= 2 and en_exercises >= 2) else 'ISSUE'
    print(f"  {fn:<38} NO:{no_exercises} EN:{en_exercises} [{status}]")

print()
print("=== SUMMARY TABLE FORMAT CHECK ===")
for fn in km_files:
    with open(os.path.join(base_km, fn)) as f:
        content = f.read()
    # Extract Oppsummering section
    m = re.search(r'## .*Oppsummering.*Summary(.*?)(?=\n##)', content, re.DOTALL)
    if m:
        table = m.group(1)
        rows = [l for l in table.split('\n') if '|' in l and '---' not in l]
        has_bilingual = all('Norsk' in l or 'English' in l for l in rows[:2])
        if has_bilingual:
            print(f"  OK: {fn} — bilingual summary table")
        else:
            print(f"  WARN: {fn} — table format unexpected")

print()
print("=== CITATION FORMAT CHECK ===")
cite_issues = []
for fn in km_files:
    with open(os.path.join(base_km, fn)) as f:
        content = f.read()
    # Check all [^N] have matching [^N]: definitions
    inline = set(re.findall(r'\[\^(\d+)\]', content))
    definitions = set(re.findall(r'^\[\^(\d+)\]:', content, re.MULTILINE))
    orphaned = inline - definitions
    undefined = definitions - inline
    if orphaned:
        print(f"  WARN: {fn} — orphaned citations: {orphaned}")
    if undefined:
        print(f"  WARN: {fn} — unused definitions: {undefined}")
    if not orphaned and not undefined:
        print(f"  OK: {fn} — all citations matched")
