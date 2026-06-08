"""
Remove the ## Flashcards section from all emne files since they're now
rendered as interactive flipcards from flashcards.json data.
"""
import re, os

emner_dir = 'src/content/emner'
count = 0

for emne in sorted(os.listdir(emner_dir)):
    ep = os.path.join(emner_dir, emne)
    if not os.path.isdir(ep):
        continue
    for f in sorted(os.listdir(ep)):
        if not f.endswith('.md') and not f.endswith('.mdx'):
            continue
        if f == '_oversikt.md':
            continue
        fp = os.path.join(ep, f)
        with open(fp) as fh:
            content = fh.read()

        # Remove ## Flashcards section (everything between ## Flashcards and the next ## or end)
        new_content = re.sub(
            r'\n## Flashcards\n.*?(?=\n## |\Z)',
            '',
            content,
            count=1,
            flags=re.DOTALL
        )

        if new_content != content:
            count += 1
            with open(fp, 'w') as fh:
                fh.write(new_content)
            print(f'Removed flashcards section from {emne}/{f}')

print(f'\nDone! Processed {count} files.')
