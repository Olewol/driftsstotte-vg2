#!/usr/bin/env python3
# Test the table fixer
line = '|---|---|'
parts = line.rstrip().split('|')
print('parts:', parts)
fixed = []
for i, p in enumerate(parts):
    if i == 0 or i == len(parts) - 1:
        fixed.append(p)
    else:
        fixed.append(' ' + p.strip() + ' ')
print('fixed:', fixed)
print('result:', repr('|'.join(fixed)))

# Test content row
line2 = '| **Tabell** | En samling rader med samme kolonnestruktur |'
parts2 = line2.split('|')
print('\nparts2:', parts2)
fixed2 = []
for i, p in enumerate(parts2):
    if i == 0 or i == len(parts2) - 1:
        fixed2.append(p)
    else:
        fixed2.append(' ' + p.strip() + ' ')
print('fixed2:', fixed2)
print('result2:', repr('|'.join(fixed2)))
