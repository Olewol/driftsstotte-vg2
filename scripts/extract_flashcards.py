"""
Extract flashcards from the ## Flashcards section of each emne file.
Outputs to src/data/flashcards.json for use at build time.
Format: term :: definition
"""
import re, os, json

emner_dir = 'src/content/emner'
output = {}

for emne in sorted(os.listdir(emner_dir)):
    ep = os.path.join(emner_dir, emne)
    if not os.path.isdir(ep):
        continue
    for f in sorted(os.listdir(ep)):
        if not f.endswith('.md') and not f.endswith('.mdx'):
            continue
        fp = os.path.join(ep, f)
        with open(fp) as fh:
            content = fh.read()

        # Extract the flashcards section
        m = re.search(r'## Flashcards\n(.*?)(?:\n## |\Z)', content, re.DOTALL)
        if not m:
            continue

        slug = re.sub(r'\.mdx?$', '', f)
        cards = []
        for line in m.group(1).strip().split('\n'):
            line = line.strip()
            if '::' not in line:
                continue
            term, _, defn = line.partition('::')
            term = term.strip().replace('*', '').strip()
            defn = defn.strip().replace('*', '').strip()
            if term and defn and not term.startswith('#'):
                cards.append({'question': term, 'answer': defn})

        if cards:
            output[slug] = cards
            print(f'{emne}/{f}: {len(cards)} flashcards')

# Write output
os.makedirs('src/data', exist_ok=True)
with open('src/data/flashcards.json', 'w') as fh:
    json.dump(output, fh, indent=2, ensure_ascii=False)

print(f'\nDone! {len(output)} files with flashcards written to src/data/flashcards.json')
