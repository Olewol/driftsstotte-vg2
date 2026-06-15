#!/usr/bin/env python3
"""Check all km files for corruption patterns."""
import re, os, glob

base = '/home/ole/workspace/driftsstotte-vg2/src/content/kompetansemaal'

patterns = {
    'char_dup (e.g. TTrussel)': re.compile(r'^([A-ZÆØÅ])\1[a-zæøå]'),
    '*## headings': re.compile(r'^\*## '),
    '### Norsk (2)': re.compile(r'^### (Norsk|English) \(\d+\)'),
    '***Norsk:' : re.compile(r'^\*\*\*Norsk:|^\*\*\*English:'),
}

all_clean = True
for f in sorted(glob.glob(os.path.join(base, 'km-*.md'))):
    basename = os.path.basename(f)
    with open(f) as fh:
        content = fh.read()
    found = []
    for name, pat in patterns.items():
        m = pat.findall(content)
        if m:
            found.append(f"{name} ({len(m)})")
    if found:
        all_clean = False
        print(f"CORRUPTED | {basename} | {', '.join(found)}")
    else:
        print(f"CLEAN     | {basename}")

print(f"\nResult: {'ALL CLEAN' if all_clean else 'FIX NEEDED'}")
