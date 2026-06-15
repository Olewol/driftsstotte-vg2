#!/usr/bin/env python3
"""Check uncited footnotes per file"""
import re, glob

for f_path in sorted(glob.glob('src/content/kompetansemaal/km-*.md')):
    name = f_path.split('/')[-1]
    with open(f_path) as f:
        content = f.read()
    
    marker = '## 📚 Kilder / Sources'
    body = content.split(marker)[0]
    fn_section = content.split(marker)[1]
    
    fn_defs = set()
    for line in fn_section.split('\n'):
        m = re.match(r'^\[\^(\d+)\]:', line)
        if m:
            fn_defs.add(int(m.group(1)))
    
    inline = set(int(m.group(1)) for m in re.finditer(r'\[\^(\d+)\]', body))
    
    uncited = sorted(fn_defs - inline)
    missing = sorted(inline - fn_defs)
    
    if uncited or missing:
        print(f'{name}:')
        if uncited:
            print(f'  Uncited footnotes: [^{"], [^".join(map(str, uncited))}')
        if missing:
            print(f'  Missing footnote defs: [^{"], [^".join(map(str, missing))}')
    else:
        print(f'{name}: All footnotes cited ✅')
