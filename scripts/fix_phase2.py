#!/usr/bin/env python3
"""
Targeted fixer for remaining markdownlint errors.
Rules: MD013, MD036, MD040, MD060, MD025, MD024, MD056, MD055
"""
import re
import glob

BASE = "src/content"

def fix_md060(filepath):
    """Fix MD060 table-column-style: ensure proper spacing around pipes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith('|'):
            continue
        
        # Parse the table row
        parts = stripped.split('|')
        fixed = []
        for j, p in enumerate(parts):
            if j == 0 or j == len(parts) - 1:
                # Leading/trailing empty parts
                fixed.append(p)
            else:
                fixed.append(' ' + p.strip() + ' ')
        
        result = '|'.join(fixed)
        # Preserve indent
        indent = line[:len(line) - len(stripped)]
        if line.endswith('\n'):
            result = indent + result + '\n'
        else:
            result = indent + result
        
        if result != line:
            lines[i] = result
            changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md040(filepath):
    """Add language identifiers to fenced code blocks."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    # Context-heavy language detection based on nearby text
    lang_keywords = {
        'bash': ['bash', 'shell', 'terminal', 'kjøre', 'run', 'install', 'apt', 'yum', 'dnf', 'chmod', 'chown', 'ls ', 'cd ', 'mkdir', 'rm ', 'cp ', 'mv ', 'grep', 'systemctl', 'service ', 'scp', 'ssh '],
        'sql': ['sql', 'select', 'insert into', 'update ', 'delete from', 'create table', 'alter table', 'drop table', 'join ', 'where ', 'from ', 'database', 'query'],
        'powershell': ['powershell', 'get-', 'set-', 'remove-', 'new-', 'write-', 'import-module'],
        'python': ['python', 'def ', 'import ', 'class ', 'print(', 'return '],
        'json': ['json'],
        'yaml': ['yaml', 'yml'],
        'diff': ['diff', '--- ', '+++ ', '@@'],
        'xml': ['xml'],
        'javascript': ['javascript', 'js', 'const ', 'let ', 'var ', 'function'],
        'dockerfile': ['docker', 'dockerfile', 'from ', 'run ', 'cmd ', 'entrypoint'],
        'text': []  # default
    }
    
    in_fence = False
    fence_lang = None
    fence_start = -1
    
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')
        m = re.match(r'^(```|~~~)(\w*)\s*$', stripped)
        if m and not in_fence:
            fence = m.group(1)
            lang = m.group(2)
            fence_start = i
            in_fence = True
            fence_lang = None
            
            if not lang:
                # Look at nearby text before the fence
                context = ''
                for j in range(max(0, i-8), i):
                    context += lines[j].strip().lower() + ' '
                
                detected = 'text'  # default
                for language, keywords in lang_keywords.items():
                    if any(kw in context for kw in keywords):
                        detected = language
                        break
                
                # Also check content inside the code block for better detection
                code_content = ''
                for j in range(i+1, min(i+15, len(lines))):
                    cl = lines[j].strip()
                    if cl.startswith('```') or cl.startswith('~~~'):
                        break
                    code_content += cl.lower() + ' '
                
                # Check code content for clues
                for language, keywords in lang_keywords.items():
                    if any(kw in code_content for kw in keywords):
                        detected = language
                        break
                
                fence_lang = fence + detected
                old_line = lines[i]
                lines[i] = fence_lang + '\n' if line.endswith('\n') else fence_lang
                if lines[i] != old_line:
                    changed = True
                    
        elif (stripped.startswith('```') or stripped.startswith('~~~')) and in_fence:
            in_fence = False
            fence_lang = None
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md025(filepath):
    """Demote extra H1s to H2."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    
    h1_indices = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r'^#[^#]', stripped) and not stripped.startswith('##'):
            h1_indices.append(i)
    
    if len(h1_indices) <= 1:
        return False
    
    changed = False
    for idx in h1_indices[1:]:
        line = lines[idx]
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        # Change '# ' to '## '
        lines[idx] = indent + '#' + stripped
        changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md024(filepath):
    """Suffix duplicate headings with (N)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    
    heading_counts = {}
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        m = re.match(r'^(#{1,6})\s+(.+?)(\s*)$', stripped)
        if m:
            level = m.group(1)
            text = m.group(2).rstrip(':.').strip().lower()
            
            if text in heading_counts:
                heading_counts[text] += 1
                n = heading_counts[text]
                # Append (N) to the heading
                orig_text = stripped[len(level)+1:].rstrip()
                new_text = orig_text.rstrip(':.').strip() + f' ({n})'
                lines[i] = line.replace(orig_text.rstrip(':.').strip(), new_text, 1)
                changed = True
            else:
                heading_counts[text] = 1
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md036(filepath):
    """Convert emphasis-on-its-own-line to proper headings.
    Detects **text** pattern on its own line, surrounded by blank lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    lines = content.splitlines(keepends=True)
    changed = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Must be exactly **text** on its own line (no other content)
        m = re.match(r'^\*\*(.+?)\*\*$', stripped)
        if not m:
            m = re.match(r'^__(.+?)__$', stripped)
        
        if m:
            text = m.group(1).strip()
            # Skip short text and likely inline emphasis
            if len(text) < 3 or text.isupper():
                continue
            # Must be preceded/followed by blank line or file boundary
            prev_blank = (i == 0 or lines[i-1].strip() == '')
            next_blank = (i + 1 >= len(lines) or lines[i+1].strip() == '')
            
            # Also check it's not inside a list
            is_in_list = False
            for j in range(i-1, -1, -1):
                l = lines[j].strip()
                if l.startswith('-') or l.startswith('*') or l.startswith('+') or re.match(r'^\d+[.)]', l):
                    is_in_list = True
                    break
                if l == '':
                    break
            
            if not is_in_list and (prev_blank or next_blank):
                indent = line[:len(line) - len(stripped)]
                lines[i] = indent + '## ' + text + '\n'
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_md013(filepath):
    """Wrap prose lines > 120 chars. Only wrap non-code, non-table, non-heading lines."""
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
    
    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')
        
        # Track code blocks
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_code = not in_code
            continue
        if in_code:
            continue
        
        # Skip YAML, headings, lists, tables, blockquotes, refs, fences, comments
        if yaml_end >= 0 and i <= yaml_end:
            continue
        if stripped.startswith('#') or stripped.startswith('|'):
            continue
        if re.match(r'^[\s>]*[-*+]\s', stripped) or re.match(r'^[\s>]*\d+[.)]\s', stripped):
            continue
        if stripped.startswith('>'):
            continue
        if re.match(r'^\[.*?\]:\s', stripped):
            continue
        if stripped.startswith('<!--') or stripped.startswith('-->'):
            continue
        if re.match(r'^[-*_]{3,}$', stripped):
            continue
        
        # Only wrap pure prose lines
        if len(stripped) > 120:
            # Find a good break point - prefer sentence end or space
            break_at = stripped.rfind('. ', 0, 121)
            if break_at > 80:
                break_at += 1  # Include the period
            else:
                break_at = stripped.rfind(' ', 0, 121)
                if break_at < 60:
                    # Hard wrap if no good break point
                    break_at = 120
            
            indent = line[:len(line) - len(stripped)]
            wrapped = stripped[:break_at].rstrip()
            rest = stripped[break_at:].lstrip()
            
            if rest:
                lines[i] = indent + wrapped + '\n'
                lines.insert(i+1, indent + rest + '\n')
                changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(''.join(lines))
        return True
    return False


def fix_file(filepath):
    """Apply all fixes to a file."""
    changed = False
    
    fixers = [
        ('MD060', fix_md060),
        ('MD040', fix_md040),
        ('MD025', fix_md025),
        ('MD036', fix_md036),
        ('MD024', fix_md024),
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
        if fix_file(fp):
            changed += 1
    print(f"\nModified {changed} files")

if __name__ == "__main__":
    main()
