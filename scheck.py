#!/usr/bin/env python3
"""Check all km files for corruption patterns."""
import re
import os
import glob

base = '/home/ole/workspace/driftsstotte-vg2/src/content/kompetansemaal'

corruption_patterns = {
    'text_duplication': re.compile(r'\b([A-ZÆØÅ])\1[A-ZÆØÅa-zæøå]'),  # TT, EE, PP at start of word
    'star_double_hash': re.compile(r'^\*## '),  # *## at line start
    'triple_star_goal': re.compile(r'^\*\*\*Norsk:|^\*\*\*English:'),  # ***Norsk:
    'norsk_numbered': re.compile(r'### Norsk \(\d+\)'),  # ### Norsk (2)
    'english_numbered': re.compile(r'### English \(\d+\)'),  # ### English (2)
}

for f in sorted(glob.glob(os.path.join(base, 'km-*.md'))):
    basename = os.path.basename(f)
    with open(f) as fh:
        content = fh.read()
    
    issues = []
    for name, pattern in corruption_patterns.items():
        matches = pattern.findall(content)
        if matches:
            issues.append(f'{name}: {len(matches)} matches')
    
    if issues:
        print(f"CORRUPTED | {basename}")
        for issue in issues:
            print(f"           - {issue}")
    else:
        print(f"OK        | {basename}")
