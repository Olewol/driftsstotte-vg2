#!/usr/bin/env python3
"""Analyse bilingual balance for all km files."""
import os, re, sys

base = 'src/content/kompetansemaal'

if not os.path.isdir(base):
    print(f"ERROR: {base} not found from", os.getcwd())
    sys.exit(1)

files = sorted(f for f in os.listdir(base) if f.startswith('km-') and f.endswith('.md'))

print("=== BILINGUAL BALANCE ANALYSIS ===")
print(f"{'File':<38} {'Forkl_NO':<10} {'Forkl_EN':<10} {'Forkl%':<8} {'All_NO':<10} {'All_EN':<10} {'All%':<8}")
print("-"*94)

for fn in files:
    with open(os.path.join(base, fn)) as f:
        content = f.read()
    
    # Forklaring/Explanation section
    m = re.search(r'## [^#]+Forklaring[^#]+Explanation(.*?)(?=\n## |\Z)', content, re.DOTALL)
    no_len = 0
    en_len = 0
    if m:
        sec = m.group(1)
        no_m = re.search(r'### Norsk\n(.*?)(?=\n### English)', sec, re.DOTALL)
        en_m = re.search(r'### English\n(.*?)(?=\n##|\n###|\Z)', sec, re.DOTALL)
        if no_m:
            no_len = len(no_m.group(1).strip())
        if en_m:
            en_len = len(en_m.group(1).strip())
    
    # Total Norsk vs English
    total_no = 0
    total_en = 0
    in_no = False
    in_en = False
    for line in content.split('\n'):
        s = line.strip()
        if s.startswith('### Norsk'):
            in_no = True
            in_en = False
            continue
        elif s == '### English' or s.startswith('### English '):
            in_no = False
            in_en = True
            continue
        elif s.startswith('## '):
            continue
        if in_no and s:
            total_no += len(s)
        elif in_en and s:
            total_en += len(s)
    
    fork_pct = (en_len / no_len * 100) if no_len else 0
    all_pct = (total_en / total_no * 100) if total_no else 0
    
    print(f"{fn:<38} {no_len:<10} {en_len:<10} {fork_pct:<8.0f} {total_no:<10} {total_en:<10} {all_pct:<8.0f}")

print()
print("=== ISSUE VERIFICATION ===")
print()

# Verify specific issues from parent QA report
issues = {
    'km-05-nettverksprotokoller.md': 'en_has_protocol_table_and_osi',
    'km-07-trusler.md': 'en_has_technical_societal_distinction',
    'km-08-risikoanalyse.md': 'en_has_2_examples',
    'km-12-baerekraft.md': 'en_has_actionable_tips',
    'km-09-automatisering.md': 'en_has_ansible_cron_taskscheduler',
    'km-10-sikre-it-losninger.md': 'en_has_all_security_measures',
}

for fn, check in sorted(issues.items()):
    with open(os.path.join(base, fn)) as f:
        content = f.read()
    print(f"--- {fn} ---")
    
    if 'protocol_table' in check:
        has_table_en = 'Key protocols' in content or 'Protocol | Port' in content
        has_osi_en = 'OSI model' in content or 'OSI-modellen' in content
        print(f"  EN protocol table: {'YES' if has_table_en else 'NO'}")
        print(f"  EN OSI/TCP-IP:     {'YES' if has_osi_en else 'NO'}")
    
    if 'distinction' in check:
        has_technical = 'Technical threats' in content
        has_societal = 'Societal threats' in content
        print(f"  EN Technical threats:  {'YES' if has_technical else 'NO'}")
        print(f"  EN Societal threats:   {'YES' if has_societal else 'NO'}")
    
    if '2_examples' in check:
        en_examples = len(re.findall(r'## Example \d', content))
        print(f"  EN examples count: {en_examples}")
    
    if 'actionable_tips' in check:
        has_tips = 'What can you as an IT worker do' in content
        has_green_it = 'Green IT' in content
        print(f"  EN actionable tips:      {'YES' if has_tips else 'NO'}")
        print(f"  EN Green IT definition:  {'YES' if has_green_it else 'NO'}")
    
    if 'cron' in check:
        for tool in ['Ansible', 'Cron', 'Task Scheduler']:
            found = tool in content
            print(f"  EN mentions '{tool}': {'YES' if found else 'NO'}")
    
    if 'security_measures' in check:
        for measure in ['Encryption', 'Firewall', 'Access control', 'Patching', 'logging']:
            found = measure.lower() in content.lower()
            print(f"  EN mentions '{measure}': {'YES' if found else 'NO'}")

print()
print("=== ADDITIONAL CHECKS ===")
print()
# Check cross-references between km files
all_files_content = {}
for fn in files:
    with open(os.path.join(base, fn)) as f:
        all_files_content[fn] = f.read()

# Count cross-references from each file
print("Cross-references (wikilinks to other km files):")
for fn in sorted(files):
    km_links = set()
    for link in re.findall(r'\[\[([^\]]+)\]\]', all_files_content[fn]):
        for other_fn in files:
            other_slug = other_fn.replace('.md', '').replace('km-', '')
            if other_slug in link and other_fn != fn:
                km_links.add(other_fn)
    print(f"  {fn:<38} → {', '.join(sorted(km_links)) if km_links else '(none)'}")

# Check proper info in kilder
print()
print("Source count per file:")
for fn in sorted(files):
    with open(os.path.join(base, fn)) as f:
        c = f.read()
    sources = c.count('[^')
    unique_footnotes = len(re.findall(r'^\[\^\d+\]:', c, re.MULTILINE))
    print(f"  {fn:<38} {unique_footnotes} unique sources, {sources} citations")
