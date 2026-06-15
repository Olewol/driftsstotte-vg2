#!/usr/bin/env python3
"""
Fix MD060 table-column-style: ensure proper spacing around pipe chars in tables.
Line `|cell|cell|` → `| cell | cell |`
"""
import re
import glob

BASE = "src/content"

def fix_table_row(line):
    """Fix spacing in a markdown table row."""
    stripped = line.rstrip('\n')
    if not stripped.startswith('|'):
        return line
    
    # Split on | to get cell contents
    # For a line like `| a | b | c |`, split('|') gives ['', ' a ', ' b ', ' c ', '']
    parts = stripped.split('|')
    
    # Process each cell: strip, then wrap with one space
    fixed = []
    for i, p in enumerate(parts):
        if i == 0 or i == len(parts) - 1:
            # Leading/trailing empty parts stay empty
            fixed.append(p)
        else:
            fixed.append(' ' + p.strip() + ' ')
    
    # Join back with | - no extra wrapping needed since parts[0] and parts[-1]
    # are empty strings, which means joining puts | at both ends naturally
    result = '|'.join(fixed)
    
    # Preserve trailing newline
    if line.endswith('\n'):
        result += '\n'
    else:
        result = result
    
    return result

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('|'):
            # Verify this is actually a table row (not a reference or some other | construct)
            # Check if the line is a logical table row: either a separator or data row
            new_line = fix_table_row(line)
            if new_line != line:
                lines[i] = new_line
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False

def main():
    files = glob.glob(f"{BASE}/**/*.md", recursive=True)
    print(f"Checking {len(files)} files...")
    changed = 0
    for fp in sorted(files):
        if process_file(fp):
            print(f"  FIXED: {fp}")
            changed += 1
    print(f"\nModified {changed} files")

if __name__ == "__main__":
    main()
