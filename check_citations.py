#!/usr/bin/env python3
"""Citation-balance checker for kompetansemaal files."""
import re
import os
import glob

def check_citations(filepath):
    with open(filepath) as f:
        content = f.read()

    # Body citations
    body = content.split('## 📚 Kilder / Sources')[0]
    citations = set(map(int, re.findall(r'\[\^(\d+)\]', body)))

    # Footnote definitions
    sources_section = content.split('## 📚 Kilder / Sources')[-1] if '## 📚 Kilder / Sources' in content else ''
    footnotes = set(map(int, re.findall(r'\[\^(\d+)\]:', sources_section)))

    orphaned = citations - footnotes
    missing = footnotes - citations

    return {
        'file': os.path.basename(filepath),
        'citations_in_body': sorted(citations),
        'footnotes_defined': sorted(footnotes),
        'orphaned': sorted(orphaned),
        'missing': sorted(missing),
        'pass': len(orphaned) == 0 and len(missing) == 0,
    }

results = []
for f in sorted(glob.glob('src/content/kompetansemaal/km-*.md')):
    r = check_citations(f)
    results.append(r)
    status = 'PASS' if r['pass'] else 'FAIL'
    issues = []
    if r['orphaned']:
        issues.append(f"orphaned refs: {r['orphaned']}")
    if r['missing']:
        issues.append(f"missing refs: {r['missing']}")
    print(f"  {status} | {r['file']:40s} | body cit: {r['citations_in_body']}")
    print(f"         | {' '*40} | fnote def: {r['footnotes_defined']}")
    if issues:
        print(f"         | {' '*40} | ISSUES: {', '.join(issues)}")
    else:
        print(f"         | {' '*40} | OK")

print(f"\nTotal: {len(results)} files, {sum(1 for r in results if r['pass'])}/{len(results)} PASS")
