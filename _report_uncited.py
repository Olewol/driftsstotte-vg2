#!/usr/bin/env python3
"""Report uncited footnotes per file"""
import yaml, re, glob, sys

for f_path in sorted(glob.glob('src/content/kompetansemaal/km-*.md')):
    name = f_path.split('/')[-1]
    with open(f_path) as f:
        content = f.read()
    
    marker = '## 📚 Kilder / Sources'
    if marker not in content:
        print(f'{name}: No Sources section')
        continue
    
    fn_section = content.split(marker)[1]
    body = content.split(marker)[0]
    
    fn_entries = {}
    for line in fn_section.split('\n'):
        m = re.match(r'^\[\^(\d+)\]:\s*(.*)', line)
        if m:
            fn_entries[int(m.group(1))] = m.group(2).strip()
    
    inline_refs = set(int(m.group(1)) for m in re.finditer(r'\[\^(\d+)\]', body))
    
    defined = set(fn_entries.keys())
    unused = sorted(defined - inline_refs)
    
    if unused:
        print(f'{name}:')
        for fn_num in unused:
            print(f'  [^{fn_num}]: {fn_entries[fn_num][:80]}')
