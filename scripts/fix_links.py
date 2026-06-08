"""
Batch-fix wiki-links in English (-en.md) files to use -en suffixes.
Only matches [[target]] or [[target|alias]] wiki-link syntax (not bash [[ ]]).
Skips targets that already end with -en.
"""
import re, os

emner_dir = 'src/content/emner'

# Collect all slugs that exist (both -en and non-en)
all_slugs = set()
for emne in os.listdir(emner_dir):
    ep = os.path.join(emner_dir, emne)
    if not os.path.isdir(ep):
        continue
    for f in os.listdir(ep):
        if f.endswith('.md') or f.endswith('.mdx'):
            slug = re.sub(r'\.mdx?$', '', f)
            all_slugs.add(slug)

total_fixed = 0
total_files = 0

for emne in sorted(os.listdir(emner_dir)):
    ep = os.path.join(emner_dir, emne)
    if not os.path.isdir(ep):
        continue
    for f in sorted(os.listdir(ep)):
        if not f.endswith('-en.md') and not f.endswith('-en.mdx'):
            continue
        fp = os.path.join(ep, f)
        with open(fp) as fh:
            content = fh.read()

        # Match wiki-links: [[target]] or [[target|alias]]
        # NOT bash [[ ]] which has spaces inside
        def fix_wikilink(m):
            full = m.group(1)
            if '|' in full:
                target, alias = full.split('|', 1)
            else:
                target = full
                alias = None

            # Skip if already -en, or if it contains spaces (bash [[ ]])
            if target.endswith('-en') or ' ' in target:
                return m.group(0)

            # Check if -en version exists as a slug
            en_target = target + '-en'
            if en_target in all_slugs:
                if alias:
                    return f'[[{en_target}|{alias}]]'
                else:
                    return f'[[{en_target}]]'
            return m.group(0)

        new_content = re.sub(r'\[\[([^\]]+)\]\]', fix_wikilink, content)
        if new_content != content:
            total_fixed += 1
            with open(fp, 'w') as fh:
                fh.write(new_content)
            changed = []
            for line_num, (old, new) in enumerate(zip(content.split('\n'), new_content.split('\n')), 1):
                if old != new:
                    changed.append(line_num)
            print(f'{emne}/{f}: {len(changed)} lines changed: {changed}')

        total_files += 1

print(f'\nDone! Checked {total_files} files, fixed {total_fixed} files.')
