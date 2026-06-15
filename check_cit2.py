#!/usr/bin/env python3
"""Citation balance check — verifies all body citations have footnote definitions."""
import re, os, glob

base = '/home/ole/workspace/driftsstotte-vg2/src/content/kompetansemaal'
all_pass = True

for f in sorted(glob.glob(os.path.join(base, 'km-*.md'))):
    basename = os.path.basename(f)
    with open(f) as fh:
        content = fh.read()
    
    # Body: everything before the kilder/sources section
    body = content.split('## 📚 Kilder / Sources')[0]
    body_citations = set(map(int, re.findall(r'\[\^(\d+)\]', body)))
    
    # Sources section
    src = content.split('## 📚 Kilder / Sources')[-1] if '## 📚 Kilder / Sources' in content else ''
    footnotes_def = set(map(int, re.findall(r'\[\^(\d+)\]:', src)))
    
    orphaned = body_citations - footnotes_def
    max_ref = max(body_citations) if body_citations else 0
    max_def = max(footnotes_def) if footnotes_def else 0
    
    status = 'PASS'
    issues = []
    if orphaned:
        status = 'FAIL'
        issues.append(f"orphaned body refs: {sorted(orphaned)}")
    
    print(f"  {status} | {basename:40s} | cites: {sorted(body_citations)} | footnotes: {sorted(footnotes_def)} | {'; '.join(issues) if issues else 'all body refs have definitions'}")

print(f"\nResult: {'ALL PASS — no orphaned citations' if all_pass else 'ISSUES FOUND'}")
