#!/usr/bin/env python3
"""
Final fixer for remaining 322 markdownlint errors.

Targeted fixes for each rule type:
MD053 (50): Remove unused reference definitions
MD025 (29): Demote extra H1s to H2
MD007 (28): Fix unordered list indentation  
MD038 (18): Fix spaces inside code spans
MD032 (14): Add blank lines around lists
MD009  (9): Remove trailing spaces
MD027  (6): Fix multiple spaces after blockquote symbol
MD012  (5): Remove multiple consecutive blank lines
MD034  (4): Wrap bare URLs in angle brackets
MD031  (4): Add blank lines around fenced code blocks
MD036  (2): Convert emphasis to proper heading
MD029  (2): Fix ordered list prefix numbering
MD004  (1): Fix unordered list style
MD013 (150): Wrap long prose lines
"""
import re
import glob

BASE = "src/content"


def fix_md013(filepath):
    """Wrap prose lines > 120 chars"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    
    # Find YAML frontmatter
    yaml_end = -1
    if lines and lines[0].strip() == '---':
        for i in range(1, min(100, len(lines))):
            if lines[i].strip() == '---':
                yaml_end = i
                break
    
    changed = False
    in_code = False
    result = []
    
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')
        
        # Track code blocks
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_code = not in_code
            result.append(line)
            continue
        if in_code:
            result.append(line)
            continue
        
        # Skip various non-prose structures
        if yaml_end >= 0 and i <= yaml_end:
            result.append(line)
            continue
        if stripped == '':
            result.append(line)
            continue
        if stripped.startswith('#') or stripped.startswith('|'):
            result.append(line)
            continue
        if re.match(r'^[\s>]*[-*+]\s', stripped):
            result.append(line)
            continue
        if re.match(r'^[\s>]*\d+[.)]\s', stripped):
            result.append(line)
            continue
        if stripped.startswith('>'):
            result.append(line)
            continue
        if re.match(r'^\[.*?\]:\s', stripped):
            result.append(line)
            continue
        if stripped.startswith('<!--'):
            result.append(line)
            continue
        if re.match(r'^[-*_]{3,}$', stripped):
            result.append(line)
            continue
        
        # Now handle long prose lines  
        indent = line[:len(line) - len(stripped)]
        
        if len(stripped) > 120:
            # Find sentence break within first 120 chars
            break_at = -1
            # Prefer sentence ending
            for sep in ['. ', '? ', '! ']:
                idx = stripped.rfind(sep, 0, 121)
                if idx > 60:
                    break_at = idx + 1  # include the punctuation
                    break
            
            # Fallback to space break
            if break_at == -1:
                break_at = stripped.rfind(' ', 0, 121)
            
            if break_at > 60:
                result.append(indent + stripped[:break_at].rstrip() + '\n')
                remainder = stripped[break_at:].lstrip()
                if remainder:
                    # Recursively handle long remainder
                    result.append(indent + remainder + '\n')
                changed = True
            else:
                result.append(line)
        else:
            result.append(line)
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(result))
        return True
    return False


def fix_md053(filepath):
    """Remove unused reference definitions"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # Collect used references: [text][ref] and [ref] (without inline URL)
    used_refs = set()
    
    # [text][ref]
    for m in re.finditer(r'\[([^\]]*)\]\[([^\]]*)\]', content):
        ref = m.group(2).strip().lower() if m.group(2).strip() else m.group(1).strip().lower()
        if ref:
            used_refs.add(ref)
    
    # [text] where it's a reference-style link (not followed by ( or :)
    for m in re.finditer(r'(?<!\])\[([^\]]+)\](?!\s*\()', content):
        ref = m.group(1).strip().lower()
        # Skip if it's likely inline formatting [bold] etc
        if ref and not re.match(r'^[*_`~]', ref) and not re.match(r'^\d+$', ref):
            used_refs.add(ref)
    
    lines = content.splitlines(keepends=True)
    changed = False
    result = []
    
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        m = re.match(r'^\[([^\]]+)\]:\s', stripped)
        if m:
            ref_name = m.group(1).strip().lower()
            if ref_name not in used_refs:
                changed = True
                i += 1
                # Also remove any following whitespace-only lines
                # But not content lines
                continue
        result.append(lines[i])
        i += 1
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(result))
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
        if stripped.startswith('# ') and not stripped.startswith('## '):
            h1_indices.append(i)
    
    if len(h1_indices) <= 1:
        return False
    
    changed = False
    for idx in h1_indices[1:]:
        line = lines[idx]
        if line.startswith('# '):
            lines[idx] = '## ' + line[2:]
            changed = True
        elif line.startswith('#') and not line.startswith('##'):
            # Has # with no space, rare but handle
            lines[idx] = '#' + line[1:]
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md007(filepath):
    """Fix unordered list indentation - ensure 2-space multiples"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*)([-*+])\s', line)
        if m:
            indent = m.group(1)
            indent_len = len(indent)
            if indent_len > 0 and indent_len % 2 != 0:
                new_indent = ' ' * (indent_len + 1)
                lines[i] = new_indent + line.lstrip()
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md038(filepath):
    """Fix spaces inside code span elements: ` text ` → `text`"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # Replace ` text ` → `text` (inline code with leading/trailing spaces)
    content = re.sub(r'`\s+(\S[^`]*?)\s+`', r'`\1`', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def fix_md032(filepath):
    """Ensure blank lines around list blocks"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    in_list = False
    result = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        is_list_item = bool(re.match(r'^[\s>]*[-*+]\s', stripped)) or bool(re.match(r'^[\s>]*\d+[.)]\s', stripped))
        is_blank = stripped == ''
        is_code_fence = stripped.startswith('```') or stripped.startswith('~~~')
        is_heading = stripped.startswith('#')
        is_table_row = stripped.startswith('|')
        
        if is_list_item and not in_list:
            # Starting a new list - ensure blank before
            in_list = True
            if result and result[-1].strip() != '' and not result[-1].strip().startswith('#') and not result[-1].strip().startswith('>'):
                result.append('\n')
                changed = True
            result.append(line)
        elif not is_list_item and not is_blank and in_list:
            # End of list - ensure blank after
            in_list = False
            if result and result[-1].strip() != '':
                result.append('\n')
                changed = True
            result.append(line)
        else:
            result.append(line)
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(result))
        return True
    return False


def fix_md009(filepath):
    """Remove trailing whitespace"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        if line != line.rstrip() + '\n':
            lines[i] = line.rstrip() + '\n'
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md027(filepath):
    """Fix multiple spaces after blockquote symbol"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        # >  text → > text
        new = re.sub(r'^(\s*>)\s{2,}(.*)$', r'\1 \2', line)
        # Handle nested: >>  text → >> text
        new = re.sub(r'^(\s*>{1,})\s{2,}(.*)$', r'\1 \2', new)
        if new != line:
            lines[i] = new
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md012(filepath):
    """Collapse multiple consecutive blank lines to one"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
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


def fix_md031(filepath):
    """Ensure blank lines around fenced code blocks"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    in_fence = False
    result = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        is_fence = stripped.startswith('```') or stripped.startswith('~~~')
        
        if is_fence and not in_fence:
            # Opening fence - ensure blank before
            if result and result[-1].strip() != '':
                result.append('\n')
                changed = True
            in_fence = True
            result.append(line)
        elif is_fence and in_fence:
            # Closing fence - ensure blank after
            in_fence = False
            result.append(line)
            # Check next line
            if i + 1 < len(lines):
                next_stripped = lines[i + 1].strip()
                if next_stripped != '' and not next_stripped.startswith('#') and not next_stripped.startswith('|') and not next_stripped.startswith('-') and not next_stripped.startswith('*') and not next_stripped.startswith('>'):
                    result.append('\n')
                    changed = True
        else:
            result.append(line)
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(result))
        return True
    return False


def fix_md036(filepath):
    """Convert emphasis-as-heading to proper heading"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        m = re.match(r'^\*\*(.+?)\*\*$', stripped)
        if not m:
            m = re.match(r'^__(.+?)__$', stripped)
        
        if m:
            text = m.group(1).strip()
            if len(text) < 3 or text.isupper():
                continue
            # Must be on its own line (surrounded by blanks or at boundaries)
            prev_blank = (i == 0 or lines[i-1].strip() == '')
            next_blank = (i + 1 >= len(lines) or lines[i+1].strip() == '')
            
            if prev_blank or next_blank:
                indent = line[:len(line) - len(stripped)]
                lines[i] = indent + '## ' + text + '\n'
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md029(filepath):
    """Fix ordered list prefix - use 1, 2, 3..."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    counters = {}
    
    for i, line in enumerate(lines):
        m = re.match(r'^(\s*)(\d+)([.)]\s)', line)
        if m:
            indent = m.group(1)
            num = int(m.group(2))
            sep = m.group(3)
            indent_level = len(indent)
            
            if indent_level not in counters:
                counters[indent_level] = 1
            else:
                counters[indent_level] += 1
            
            expected = counters[indent_level]
            if num != expected:
                lines[i] = indent + str(expected) + sep + line[len(indent) + len(str(num)) + len(sep):]
                changed = True
        else:
            # Non-list line - reset counters for this level
            stripped = line.strip()
            if stripped != '' and not re.match(r'^\d+[.)]\s', stripped):
                # Check if it's something else at same indent level
                pass
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md004(filepath):
    """Fix unordered list style"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        m = re.match(r'^(\s*)[*+](\s)', stripped)
        if m:
            indent = line[:len(line) - len(stripped)]
            lines[i] = indent + '-' + line[len(indent) + 1:]
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def apply_fixers(filepath):
    """Apply all applicable fixers"""
    changed = False
    
    fixers = [
        ('MD009', fix_md009),
        ('MD012', fix_md012),
        ('MD034', fix_md034),
        ('MD038', fix_md038),
        ('MD027', fix_md027),
        ('MD004', fix_md004),
        ('MD007', fix_md007),
        ('MD025', fix_md025),
        ('MD036', fix_md036),
        ('MD029', fix_md029),
        ('MD053', fix_md053),
        ('MD032', fix_md032),
        ('MD031', fix_md031),
        ('MD013', fix_md013),
    ]
    
    for name, fn in fixers:
        try:
            if fn(filepath):
                if not changed:
                    print(f"  {filepath}:")
                print(f"    - {name}")
                changed = True
        except Exception as e:
            print(f"  ERROR {filepath} {name}: {e}")
    
    return changed


def main():
    files = glob.glob(f"{BASE}/**/*.md", recursive=True)
    print(f"Processing {len(files)} files...")
    changed = 0
    for fp in sorted(files):
        if apply_fixers(fp):
            changed += 1
    print(f"\nModified {changed} files")

if __name__ == "__main__":
    main()
