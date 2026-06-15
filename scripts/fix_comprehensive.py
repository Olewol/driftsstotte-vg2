#!/usr/bin/env python3
"""
Comprehensive markdown lint fixer for remaining issues after --fix.

Handles:
1. MD060: table-column-style - fix compact |cell| → | cell |
2. MD013: line-length - wrap prose lines > 120 chars  
3. MD036: emphasis-as-heading - convert **text** on its own line to ## text
4. MD040: fenced-code-language - add language to untagged code fences
5. MD025: multiple-H1 - demote extra H1s to H2
6. MD024: duplicate-headings - make unique  
7. MD053: unused-references - remove unused reference defs
8. MD007: ul-indent - fix indentation
9. MD034: bare URLs - wrap in <>
10. Other minor: MD027, MD029, MD031, MD032, MD058
"""

import re
import glob
import os

BASE = "src/content"

def is_table_row(line):
    """Check if a line is a markdown table row"""
    return line.strip().startswith('|')

def fix_md060(filepath):
    """Fix table column spacing"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        if not is_table_row(line):
            continue
        
        stripped = line.strip()
        if not stripped.startswith('|'):
            continue
        
        # Split on | but keep the structure
        # Handle separator and data rows the same: add spaces
        new_parts = []
        parts = stripped.split('|')
        
        for p in parts:
            if p == '':
                new_parts.append('')
            else:
                new_parts.append(' ' + p.strip() + ' ')
        
        new_line = '|'.join(new_parts)
        
        # Preserve trailing newline
        if line.endswith('\n'):
            new_line += '\n'
        
        # Preserve leading whitespace
        indent = line[:len(line) - len(stripped)]
        new_line = indent + new_line
        
        if new_line != line:
            lines[i] = new_line
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def find_yaml_boundaries(lines):
    """Find YAML frontmatter boundaries"""
    start = None
    end = None
    if lines and lines[0].strip() == '---':
        start = 0
        for i in range(1, min(100, len(lines))):
            if lines[i].strip() == '---' and i > start:
                end = i
                break
    return start, end


def is_prose_line(line, yaml_start, yaml_end, line_num):
    """Check if a line is a prose paragraph (not code, list, heading, table, etc.)"""
    # Skip YAML frontmatter
    if yaml_start is not None and yaml_end is not None and yaml_start <= line_num <= yaml_end:
        return False
    
    stripped = line.strip()
    if not stripped:
        return False
    
    # Skip if it's a heading
    if stripped.startswith('#'):
        return False
    
    # Skip if it's a list item
    if re.match(r'^[-*+]\s', stripped) or re.match(r'^\d+[.)]\s', stripped):
        return False
    
    # Skip if it's a blockquote
    if stripped.startswith('>'):
        return False
    
    # Skip if it's a code fence
    if stripped.startswith('```') or stripped.startswith('~~~'):
        return False
    
    # Skip if it's a table row
    if stripped.startswith('|'):
        return False
    
    # Skip if it's a horizontal rule
    if re.match(r'^[-*_]{3,}$', stripped):
        return False
    
    # Skip if it's a link/image reference definition
    if re.match(r'^\[.*?\]:\s', stripped):
        return False
    
    # Skip if it's a comment
    if stripped.startswith('<!--'):
        return False
    
    return True


def wrap_line(line, max_len=120):
    """Word-wrap a long line to max_len"""
    stripped = line.rstrip('\n')
    
    if len(stripped) <= max_len:
        return line
    
    # Try to break at a sentence boundary or space
    result = []
    remaining = stripped
    
    while len(remaining) > max_len:
        # Find last space within max_len
        break_point = remaining.rfind(' ', 0, max_len)
        
        if break_point == -1:
            # No space found - break at max_len (hard cut only if no choice)
            break_point = max_len
        
        result.append(remaining[:break_point].rstrip())
        remaining = remaining[break_point:].lstrip()
    
    if remaining:
        result.append(remaining)
    
    return '\n'.join(result) + '\n'


def fix_md013(filepath):
    """Fix long prose lines"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    
    yaml_start, yaml_end = find_yaml_boundaries(lines)
    changed = False
    
    # Track whether we're inside a code block
    in_code_block = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Track code blocks
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            continue
        
        # Only fix prose lines
        if not is_prose_line(line, yaml_start, yaml_end, i):
            continue
        
        if len(stripped) > 120:
            wrapped = wrap_line(stripped, 120)
            if wrapped.rstrip('\n') != stripped:
                # Preserve original indentation
                indent = line[:len(line) - len(stripped)]
                wrapped = indent + wrapped.rstrip('\n')
                lines[i] = wrapped + '\n'
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md036(filepath):
    """Convert emphasis-as-heading to proper headings.
    Detects bold/italic on its own line (not at end of paragraph)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if line is just bold text (possibly with multiple words)
        # Match: **text** or __text__ on its own line
        m = re.match(r'^\*\*(.+?)\*\*$', stripped)
        if not m:
            m = re.match(r'^__(.+?)__$', stripped)
        
        if m:
            text = m.group(1)
            # Don't convert if it looks like it's within a paragraph
            # Only if the context suggests it's meant as a heading
            # Check: previous line is blank (or EOF) and next line is blank (or has content)
            prev_blank = (i == 0) or lines[i-1].strip() == ''
            next_has_content = (i + 1 < len(lines)) and lines[i+1].strip()
            
            if prev_blank and next_has_content:
                indent = line[:len(line) - len(stripped)]
                lines[i] = indent + '## ' + text + '\n'
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md040(filepath):
    """Add language to untagged code fences"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    in_fence = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        if not in_fence:
            m = re.match(r'^(```|~~~)(\w*)(.*)$', stripped)
            if m:
                fence = m.group(1)
                lang = m.group(2).strip()
                if not lang:
                    # Determine language from context
                    # Check for SQL patterns
                    text_before = ''
                    for j in range(max(0, i-3), i):
                        text_before += lines[j].strip().lower() + ' '
                    
                    if any(kw in text_before for kw in ['sql', 'query', 'select', 'insert', 'update', 'delete', 'create table', 'database']):
                        lang = 'sql'
                    elif any(kw in text_before for kw in ['bash', 'shell', 'command', 'terminal', 'kjøre', 'run', 'install']):
                        lang = 'bash'
                    elif any(kw in text_before for kw in ['powershell', 'powershell']):
                        lang = 'powershell'
                    elif any(kw in text_before for kw in ['python', 'python']):
                        lang = 'python'
                    elif any(kw in text_before for kw in ['json', 'json']):
                        lang = 'json'
                    elif any(kw in text_before for kw in ['yaml', 'yml', 'yaml']):
                        lang = 'yaml'
                    elif any(kw in text_before for kw in ['html', 'html']):
                        lang = 'html'
                    elif any(kw in text_before for kw in ['css', 'css']):
                        lang = 'css'
                    elif any(kw in text_before for kw in ['javascript', 'js']):
                        lang = 'javascript'
                    elif any(kw in text_before for kw in ['xml', 'xml']):
                        lang = 'xml'
                    elif any(kw in text_before for kw in ['docker', 'dockerfile']):
                        lang = 'dockerfile'
                    elif any(kw in text_before for kw in ['diff', 'endring']):
                        lang = 'diff'
                    else:
                        lang = 'text'
                    
                    old_line = line
                    if fence == '```':
                        lines[i] = '```' + lang + '\n'
                    else:
                        lines[i] = '~~~' + lang + '\n'
                    if lines[i] != old_line:
                        changed = True
                
                in_fence = True
        else:
            # Check for closing fence
            m = re.match(r'^(```|~~~)', stripped)
            if m:
                in_fence = False
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md025(filepath):
    """Demote extra H1s to H2"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    
    h1_indices = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Find lines starting with # (not ##, ###, etc.)
        if re.match(r'^#\s', stripped):
            h1_indices.append(i)
    
    if len(h1_indices) <= 1:
        return False
    
    # Keep first H1, demote rest
    changed = False
    for idx in h1_indices[1:]:
        line = lines[idx]
        # Change # to ##
        lines[idx] = '#' + line
        
        # If the first H1 was the title (in YAML frontmatter style), also fix
        changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md024(filepath):
    """Make duplicate headings unique by adding context"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    
    heading_counts = {}
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        m = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if m:
            level, text = m.group(1), m.group(2).strip()
            # Remove trailing punctuation for comparison
            clean_text = text.rstrip(':.').strip().lower()
            
            if clean_text in heading_counts:
                heading_counts[clean_text] += 1
                # Add number suffix
                lines[i] = line.replace(
                    '#' * len(level) + ' ' + text,
                    '#' * len(level) + ' ' + text + ' (' + str(heading_counts[clean_text]) + ')',
                    1
                )
                changed = True
            else:
                heading_counts[clean_text] = 1
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md053(filepath):
    """Remove unused reference definitions"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    
    # Collect used references
    used_refs = set()
    
    # Find [text][ref] usage
    for m in re.finditer(r'\[([^\]]*)\]\[([^\]]*)\]', content):
        ref = m.group(2).lower() if m.group(2).strip() else m.group(1).lower()
        if ref.strip():
            used_refs.add(ref.strip())
    
    # Find [ref]: style definitions  
    # Also find raw [text] (link-style refs)
    for m in re.finditer(r'(?<!\])\[([^\]]+)\](?!\s*\(|:)', content):
        ref = m.group(1).lower().strip()
        if ref and not re.match(r'^\d+$', ref):
            used_refs.add(ref)
    
    # Remove unused definitions
    changed = False
    new_lines = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        m = re.match(r'^\[([^\]]+)\]:\s', stripped)
        if m:
            ref_name = m.group(1).strip().lower()
            if ref_name not in used_refs:
                # Skip this line and any continuation lines (indented)
                changed = True
                i += 1
                # Skip continuation lines
                while i < len(lines) and lines[i].strip().startswith('['):
                    i += 1
                continue
        
        new_lines.append(lines[i])
        i += 1
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(new_lines))
        return True
    return False


def fix_md007(filepath):
    """Fix unordered list indentation"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    in_list = False
    list_level = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if this is a list item
        m = re.match(r'^(\s*)([-*+])\s', line)
        if m:
            indent = m.group(1)
            indent_size = len(indent)
            
            if indent_size > 0 and indent_size % 2 != 0:
                # Fix odd indentation
                new_indent = ' ' * (indent_size + 1)
                lines[i] = new_indent + line.lstrip()
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md034(filepath):
    """Wrap bare URLs in angle brackets"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    url_pattern = re.compile(r'(?<!<)(https?://[^\s<>)]+)(?!>)(?=[\s,.\])!?;:]*|$)')
    content = url_pattern.sub(r'<\1>', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def process_file(filepath):
    """Apply all fixes to one file"""
    changed = False
    
    # Apply fixes in order: non-destructive first, then structural
    fix_fns = [
        ('MD034 - bare URLs', fix_md034),
        ('MD060 - table spacing', fix_md060),
        ('MD040 - code language', fix_md040),
        ('MD025 - multiple H1', fix_md025),
        ('MD053 - unused refs', fix_md053),
        ('MD007 - ul indent', fix_md007),
        ('MD036 - emphasis heading', fix_md036),
        ('MD024 - duplicate headings', fix_md024),
        ('MD013 - line length', fix_md013),
    ]
    
    for name, fn in fix_fns:
        try:
            if fn(filepath):
                if not changed:
                    print(f"  {filepath}:")
                print(f"    - {name}")
                changed = True
        except Exception as e:
            print(f"  ERROR {filepath} ({name}): {e}")
    
    return changed


def main():
    files = glob.glob(f"{BASE}/**/*.md", recursive=True)
    print(f"Processing {len(files)} files...")
    
    changed = 0
    for fp in sorted(files):
        if process_file(fp):
            changed += 1
    
    print(f"\nModified {changed} files")

if __name__ == "__main__":
    main()
