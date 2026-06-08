"""Check slug mapping for English wiki-links."""
import os, re, json

def slugify(s):
    s = s.lower()
    s = s.replace('æ', 'ae').replace('ø', 'oe').replace('å', 'aa')
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

BASE = '/driftsstotte-vg2'
emner_dir = 'src/content/emner'
slug_to_emne = {}

for emne in os.listdir(emner_dir):
    emne_path = os.path.join(emner_dir, emne)
    if os.path.isdir(emne_path):
        for f in os.listdir(emne_path):
            if f.endswith('.md') or f.endswith('.mdx'):
                slug = slugify(re.sub(r'\.mdx?$', '', f))
                slug_to_emne[slug] = emne

print("EN slugs in mapping:")
for s in sorted(slug_to_emne.keys()):
    if s.endswith('-en'):
        print(f"  {s} -> {slug_to_emne[s]}")

print(f"\nTotal slugs: {len(slug_to_emne)}")
print(f"Total en-slugs: {len([s for s in slug_to_emne if s.endswith('-en')])}")

# Collect all wiki-links from English files
print("\n\nWiki-links from English (-en.md) files that need updating:")
for emne in sorted(os.listdir(emner_dir)):
    emne_path = os.path.join(emner_dir, emne)
    if not os.path.isdir(emne_path):
        continue
    for f in sorted(os.listdir(emne_path)):
        if not f.endswith('-en.md') and not f.endswith('-en.mdx'):
            continue
        filepath = os.path.join(emne_path, f)
        with open(filepath) as fh:
            content = fh.read()
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        for wl in wikilinks:
            target = wl.split('|')[0]  # before alias
            if not target.endswith('-en'):
                print(f"  {emne}/{f}: [[{wl}]] -> should be [[{target}-en]]")
