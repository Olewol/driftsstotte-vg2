"""Check remaining consecutive blanks in a file."""
import sys

fp = sys.argv[1]
with open(fp) as f:
    lines = f.read().split('\n')

bc = 0
out = []
for i, l in enumerate(lines):
    if l.strip() == '':
        bc += 1
    else:
        if bc > 2:
            out.append(f"Line {i-bc+1}-{i}: {bc} blanks (3+ lines)")
        elif bc == 2:
            out.append(f"Line {i-bc+1}-{i}: {bc} blanks (MD012 violation)")
        bc = 0
if bc > 2:
    out.append(f"End: {bc} blanks (3+)" if bc > 2 else f"End: {bc} blanks")

if out:
    print(f"\n{fp}: {len(out)} violations")
    for o in out[:20]:
        print(f"  {o}")
else:
    print(f"{fp}: clean")
