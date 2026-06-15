#!/usr/bin/env python3
"""
Fix MD060 (table-column-style): Add spaces around pipe chars in tables.
The compact style `|cell|cell|` needs to become `| cell | cell |`.
"""
import re
import glob

BASE = "src/content"

def fix_table_line(line):
    """Fix table row spacing - add spaces around pipe chars"""
    # Skip lines that aren't table rows (don't start with | or have only --- separators)
    stripped = line.strip()
    if not stripped.startswith('|'):
        return line
    
    # We need to be careful with the separator row: |---|---|
    # Figure out if this is a separator line
    inner = stripped[1:-1]  # Remove leading and trailing | 
    
    # Check if it's a separator row (only contains -, :, and |)
    sep_pattern = re.compile(r'^[\s\-:|]+$')
    is_separator = bool(sep_pattern.match(inner))
    
    if is_separator:
        # Fix separator: | --- | --- | → | :--- | :---: | ---: |
        parts = re.split(r'(?<!\\)\|', inner)
        fixed_parts = []
        for part in parts:
            p = part.strip()
            if p:
                fixed_parts.append(f" {p} ")
            else:
                fixed_parts.append(" ")
        result = "|" + "|".join(fixed_parts) + "|"
        return result + "\n" if line.endswith('\n') else result
    else:
        # Fix content row: | cell | cell | → ensure proper spacing
        parts = re.split(r'(?<!\\)\|', inner)
        fixed_parts = []
        for part in parts:
            p = part.strip()
            fixed_parts.append(f" {p} " if p else " ")
        result = "|" + "|".join(fixed_parts) + "|"
        return result + "\n" if line.endswith('\n') else result

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    
    in_table = False
    fixed_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|'):
            fixed = fix_table_line(line)
            if fixed != line:
                fixed_lines.append(fixed)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    content = ''.join(fixed_lines)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    files = glob.glob(f"{BASE}/**/*.md", recursive=True)
    changed = 0
    for fp in sorted(files):
        if process_file(fp):
            print(f"  FIXED: {fp}")
            changed += 1
    print(f"\nModified {changed} files")

if __name__ == "__main__":
    main()
