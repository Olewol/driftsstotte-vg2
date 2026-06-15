#!/usr/bin/env python3
"""
Pass 2: Fix remaining markdownlint errors in src/content/ after pass 1.

Handles all rules still failing after fix_markdown.py ran:
  MD013  (line-length): 1750 - blockquote-aware line wrapping
  MD036  (emphasis-as-heading): 84 - also handle *italic* emphasis
  MD040  (fenced-code-language): 70 - add language spec
  MD060  (table-column-style): 53 - normalize table pipe alignment
  MD053  (unused-references): 50 - remove unused ref defs
  MD025  (multiple-h1s): 29 - demote extra H1
  MD007  (unordered-list-indent): 28 - nested list indentation
  MD024  (duplicate-headings): 24
  MD032  (blanks-around-lists): 14
  MD009  (trailing-spaces): 9
  MD058  (blanks-around-tables): 7
  MD027  (multiple-space-blockquote): 6
  MD034  (bare-URLs): 5
  MD012  (multiple-blanks): 5
  MD031  (blanks-around-fences): 4
  MD029  (ordered-list-prefix): 2
  MD056  (table-column-count): 1
  MD055  (table-pipe-style): 1
  MD004  (unordered-list-style): 1

Strategy: process files independently, each fix in isolation.
MD013 (line-wrap) is last because it's the most disruptive.
"""
import re, glob, sys

BASE = "src/content"
TOTAL = 0

def log(m): print(f"[FIX] {m}")

def fm_end(lines):
    if not lines or lines[0].strip() != '---': return -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---': return i
    return -1

def blank(l): return l.strip() == ''
def heading(l): return bool(re.match(r'^#{1,6}\s+', l))
def fence(l): return bool(re.match(r'^```', l))
def tblrow(l): return '|' in l and re.match(r'^\s*\|', l)

def fences(lines):
    """Return list of (start, end) for code fence regions."""
    r, i = [], 0
    while i < len(lines):
        if fence(lines[i]):
            s = i; i += 1
            while i < len(lines) and not fence(lines[i]): i += 1
            if i < len(lines):
                r.append((s, i)); i += 1
            else:
                r.append((s, len(lines)-1)); break
        else: i += 1
    return r

def inside(idx, ff):
    return any(s < idx <= e for s, e in ff)

def tbsep(l):
    """True if line is a table separator row like |---|---|"""
    s = l.strip()
    if not s.startswith('|') or not s.endswith('|'): return False
    return all(ch in '-: ' for ch in s[1:-1])

def blockquote_prefix(l):
    """If line starts with blockquote marker, return ('> ', rest) or None."""
    m = re.match(r'^(>\s?)(.*)', l)
    if m:
        return (m.group(1), m.group(2))
    return None

def is_list_line(l):
    """Check if line is a list item (ordered or unordered)."""
    return bool(re.match(r'^(\s*)([-*+]|\d+\.)\s', l))

def list_content_start(l):
    """For a list item, return the indent that continuation lines should use."""
    m = re.match(r'^(\s*)([-*+]|\d+\.)\s', l)
    if m:
        return m.group(1) + ' ' * (len(m.group(2)) + 1)
    return None

# ===== FIX FUNCTIONS =====

def fix_md004(lines, ff):
    """Change * list markers to - for consistency."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        if re.match(r'^\s*\*\s', l):
            r[i] = re.sub(r'^(\s*)\*\s', r'\1- ', l, count=1); f += 1
    return r, f

def fix_md007(lines, ff):
    """Fix unordered list indentation: ensure 2-space increments."""
    f = 0; r = list(lines)
    # Track list level by indentation, enforce multiples of 2
    for i, l in enumerate(r):
        if inside(i, ff): continue
        m = re.match(r'^(\s*)([-*+])\s', l)
        if m:
            indent = len(m.group(1))
            new_indent = (indent // 2) * 2  # round down to nearest 2
            if new_indent != indent:
                r[i] = ' ' * new_indent + l[indent:]
                f += 1
    return r, f

def fix_md009(lines, ff):
    """Strip trailing whitespace."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        s = l.rstrip()
        if s != l.rstrip('\n\r'):
            r[i] = s + '\n'; f += 1
    return r, f

def fix_md012(lines, ff):
    """Collapse to at most 1 consecutive blank line."""
    f = 0; r = []; bc = 0
    for l in lines:
        if l.strip() == '':
            bc += 1
            if bc <= 1: r.append(l)
            else: f += 1
        else:
            bc = 0; r.append(l)
    return r, f

def fix_md025(lines, ff):
    """Demote extra H1 to H2."""
    f = 0; r = list(lines); fm = fm_end(r)
    idxs = [i for i in range(len(r)) if i > fm and not inside(i, ff) and re.match(r'^# [^#]', r[i])]
    if len(idxs) <= 1: return r, 0
    for i in idxs[1:]: r[i] = '#' + r[i]; f += 1
    return r, f

def fix_md027(lines, ff):
    """Remove multiple spaces after > in blockquotes."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        n = re.sub(r'^>\s{2,}', '> ', l)
        if n != l: r[i] = n; f += 1
    return r, f

def fix_md029(lines, ff):
    """Fix ordered list prefix — renumber 1,2,3..."""
    f = 0; r = list(lines); i = 0
    while i < len(r):
        if inside(i, ff): i += 1; continue
        if re.match(r'^\s*\d+\.\s', r[i]):
            s = i
            while i < len(r) and re.match(r'^\s*\d+\.\s', r[i]): i += 1
            for j, n in enumerate(range(s, i), 1):
                m = re.match(r'^(\s*)\d+\.\s', r[n])
                if m:
                    rst = r[n][m.end():]
                    nn = f'{m.group(1)}{j}. {rst}'
                    if nn != r[n]: r[n] = nn; f += 1
        else: i += 1
    return r, f

def fix_md031(lines, ff):
    """Ensure blank lines before and after fenced code blocks."""
    f = 0; r = list(lines); fm = fm_end(r)
    ib = set(); ia = set()
    for s, e in ff:
        if s > fm+1 and s > 0 and not blank(r[s-1]): ib.add(s); f += 1
        if e+1 < len(r) and not blank(r[e+1]): ia.add(e); f += 1
    for idx in sorted(ia, reverse=True): r.insert(idx+1, '')
    for idx in sorted(ib, reverse=True): r.insert(idx, '')
    return r, f

def fix_md032(lines, ff):
    """Ensure blank lines around lists."""
    f = 0; r = list(lines); fm = fm_end(r)
    ib = set(); ia = set()
    i = 0
    while i < len(r):
        if inside(i, ff): i += 1; continue
        if is_list_line(r[i]):
            s = i
            while i < len(r) and is_list_line(r[i]): i += 1
            e = i - 1
            if s > fm+1 and s > 0:
                p = r[s-1]
                if not blank(p) and not heading(p): ib.add(s); f += 1
            if e+1 < len(r):
                n = r[e+1]
                if not blank(n) and not heading(n): ia.add(e); f += 1
        else: i += 1
    for idx in sorted(ia, reverse=True): r.insert(idx+1, '')
    for idx in sorted(ib, reverse=True): r.insert(idx, '')
    return r, f

def fix_md034(lines, ff):
    """Wrap bare URLs in angle brackets."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        if re.search(r'https?://', l) and '(' not in l and '](' not in l:
            n = re.sub(r'(?<!")(?<!\()(https?://[^\s<>"\'\]\)}]+)(?!["\'>\)])', r'<\1>', l)
            if n != l: r[i] = n; f += 1
    return r, f

def fix_md036(lines, ff):
    """Convert standalone emphasis lines to headings.
    Handle both **bold** and *italic* on a single line."""
    f = 0; r = list(lines)
    # Match either **text** or *text* on its own line
    pat_bold = re.compile(r'^\s*\*\*(.+?)\*\*\s*$')
    pat_ital = re.compile(r'^\s*\*(.+?)\*\s*$')  # single asterisk
    pat_und  = re.compile(r'^\s*__(.+?)__\s*$')
    pat_sing = re.compile(r'^\s*_(.+?)_\s*$')    # single underscore
    for i, l in enumerate(r):
        if inside(i, ff) or heading(l) or tblrow(l): continue
        # Also skip lines inside blockquotes (they're likely citations, not headings)
        if l.strip().startswith('>'): continue
        s = l.strip()
        m = pat_bold.match(l) or pat_ital.match(l) or pat_und.match(l) or pat_sing.match(l)
        if m:
            t = m.group(1).strip()
            if t and len(t) < 100:
                # Strip trailing punctuation
                t = re.sub(r'[.:;,!?\u3002\uff0c\uff1b\uff1a\uff01\uff1f\uff09]+$', '', t).strip()
                if t:
                    r[i] = f'## {t}'; f += 1
    return r, f

def fix_md040(lines, ff):
    """Add language spec to code fences missing it."""
    f = 0; r = list(lines)
    for s, e in ff:
        c = r[s].strip()
        if c == '```':
            r[s] = '```text'; f += 1
    return r, f

def fix_md053(lines, ff):
    """Remove unused reference definitions."""
    f = 0; r = list(lines)
    defs = {}; uses = set()
    for i, l in enumerate(r):
        if inside(i, ff): continue
        m = re.match(r'^(\s*)\[([^\]]+)\]:\s+\S', l)
        if m: defs[m.group(2)] = i
    for i, l in enumerate(r):
        if inside(i, ff): continue
        for m in re.finditer(r'(?<!!)\[([^\]]*)\]', l):
            lbl = m.group(1)
            if lbl:
                end = m.end()
                if end < len(l) and l[end] == '(': continue  # link, not reference
                if end+1 < len(l) and l[end:end+2] == ':(': continue
                uses.add(lbl)
    unused = [lbl for lbl in defs if lbl.lower() not in {u.lower() for u in uses}]
    if not unused: return r, 0
    rm = set()
    for lbl in unused:
        idx = defs[lbl]; rm.add(idx)
        if idx > 0 and blank(r[idx-1]): rm.add(idx-1)
        if idx+1 < len(r) and blank(r[idx+1]): rm.add(idx+1)
    r = [l for i,l in enumerate(r) if i not in rm]; f += len(unused)
    return r, f

def fix_md055(lines, ff):
    """Normalize table separator rows."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff) or not tbsep(l): continue
        parts = l.strip().split('|')
        np = ['']
        for p in parts[1:-1]:
            p = p.strip()
            if all(c in '-:' for c in p):
                if p.startswith(':') and p.endswith(':'):
                    np.append(' :---: ')
                elif p.endswith(':'):
                    np.append(' ---: ')
                elif p.startswith(':'):
                    np.append(' :--- ')
                else:
                    np.append(' --- ')
            else:
                np.append(f' {p} ')
        np.append('')
        n = '|'.join(np) + '\n'
        if n.strip() != l.strip(): r[i] = n; f += 1
    return r, f

def fix_md056(lines, ff):
    """Fix table column count consistency."""
    f = 0; r = list(lines); i = 0
    while i < len(r):
        if inside(i, ff): i += 1; continue
        if tblrow(r[i]):
            rows = []
            while i < len(r) and (tblrow(r[i]) or tbsep(r[i])):
                rows.append(i); i += 1
            if len(rows) > 1:
                exp = r[rows[0]].count('|')
                for ri in rows[1:]:
                    act = r[ri].count('|')
                    if act < exp:
                        r[ri] = r[ri].rstrip() + ' |' * (exp - act) + '\n'; f += 1
        else: i += 1
    return r, f

def fix_md058(lines, ff):
    """Ensure blank lines around tables."""
    f = 0; r = list(lines); fm = fm_end(r)
    ib = set(); ia = set()
    i = 0
    while i < len(r):
        if inside(i, ff): i += 1; continue
        if tblrow(r[i]) or tbsep(r[i]):
            s = i
            while i < len(r) and (tblrow(r[i]) or tbsep(r[i])): i += 1
            e = i - 1
            if s > fm+1 and s > 0:
                p = r[s-1]
                if not blank(p) and not heading(p): ib.add(s); f += 1
            if e+1 < len(r):
                n = r[e+1]
                if not blank(n) and not heading(n): ia.add(e); f += 1
        else: i += 1
    for idx in sorted(ia, reverse=True): r.insert(idx+1, '')
    for idx in sorted(ib, reverse=True): r.insert(idx, '')
    return r, f

def fix_md060(lines, ff):
    """Fix table cell spacing — exactly one space around pipes."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        s = l.rstrip()
        if not s or not tblrow(s) or tbsep(s): continue
        parts = s.split('|')
        if len(parts) < 3: continue
        np = [parts[0]]
        for p in parts[1:-1]:
            t = p.strip()
            np.append(f' {t} ' if t else ' ')
        np.append(parts[-1])
        n = '|'.join(np)
        if n != s: r[i] = n + '\n'; f += 1
    return r, f

def fix_md024(lines, ff):
    """Make duplicate headings unique by appending parent context."""
    f = 0; r = list(lines); fm = fm_end(r)
    grp = {}
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff): continue
        m = re.match(r'^(#{1,6})\s+(.+?)(\s*\{[^}]*\})?\s*$', l)
        if m:
            k = (len(m.group(1)), m.group(2).strip().lower())
            grp.setdefault(k, []).append(i)
    for (lv, txt), idxs in grp.items():
        if len(idxs) <= 1: continue
        for idx in idxs[1:]:
            pt = None
            for j in range(idx-1, fm, -1):
                pm = re.match(r'^#{1,6}\s+(.+)$', r[j])
                if pm:
                    cand = pm.group(1).strip()
                    if cand.lower() != txt:
                        pt = cand; break
            if pt:
                r[idx] = re.sub(r'^(#{1,6}\s+)(.+?)(\s*)$',
                                rf'\1\2 ({pt})\3', r[idx]); f += 1
    return r, f

def wrap_line(text, mx, prefix='', cont_prefix=''):
    """
    Smart word-wrap for a single line.
    prefix: the indent/blockquote prefix for the FIRST line
    cont_prefix: the indent/blockquote prefix for CONTINUATION lines
    
    Returns list of lines or [text] if no wrapping needed.
    Handles inline URLs (don't break them) and inline code (don't break them).
    """
    # Strip the prefix from consideration
    if prefix and text.startswith(prefix):
        content = text[len(prefix):]
    else:
        content = text
    
    words = content.split()
    if not words: return [text]
    
    # Calculate available width per line
    first_indent = len(prefix)
    cont_indent = len(cont_prefix)
    first_mx = mx - first_indent
    cont_mx = mx - cont_indent
    
    # If content fits in first line, no wrapping needed
    if len(content) <= first_mx:
        return [text]
    
    out = []
    cur = ''
    for w in words:
        # Check if word has a long URL - never break URLs
        if '://' in w and len(w) > cont_mx:
            # URL is too long for any line, just let it overflow
            if cur:
                out.append(cur)
                cur = cont_prefix + w
            else:
                out.append(cont_prefix + w)
            cur = ''
            continue
        
        candidate = f'{cur} {w}'.strip() if cur else w
        allowed_len = first_mx if not out and not cur else cont_mx
        
        if len(candidate) <= allowed_len:
            cur = candidate
        else:
            if cur:
                line = (prefix if not out else cont_prefix) + cur
                out.append(line)
            cur = w
    
    if cur:
        line = (prefix if not out else cont_prefix) + cur
        out.append(line)
    
    # If still just one line, not worth it
    if len(out) <= 1:
        return [text]
    
    return out


def fix_md013(lines, ff, mx=120):
    """Break long lines at word boundaries, respecting blockquotes and lists."""
    f = 0; r = list(lines); fm = fm_end(r)
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff): continue
        s = l.rstrip('\n\r')
        if not s: continue
        # Skip table rows (config already excludes tables from MD013)
        if tblrow(s) or tbsep(s): continue
        
        if len(s) > mx:
            # Detect blockquote
            bq = blockquote_prefix(s)
            if bq:
                # Blockquote line: `> ` prefix for first line and `> ` for continuation
                prefix = bq[0].rstrip() + ' '  # normalize to "> "
                cont_prefix = '> '
                wr = wrap_line(s, mx, prefix=prefix, cont_prefix=cont_prefix)
                if len(wr) > 1:
                    r[i] = '\n'.join(wr) + '\n'
                    f += 1
                continue
            
            # Detect list item
            if is_list_line(s):
                cont_prefix = list_content_start(s)
                if cont_prefix:
                    m = re.match(r'^(\s*[-*+]|\d+\.)\s', s)
                    prefix = m.group(0) if m else ''
                    # For the first line, use the line's own prefix
                    wr = wrap_line(s, mx, prefix='', cont_prefix=cont_prefix)
                    if len(wr) > 1:
                        # First line keeps original prefix, rest use cont_prefix
                        wr[0] = s[:len(prefix)] + wr[0] if not wr[0].startswith(prefix) else wr[0]
                        # Ensure continuation lines have cont_prefix prepended
                        for j in range(1, len(wr)):
                            if not wr[j].startswith(cont_prefix):
                                wr[j] = cont_prefix + wr[j].lstrip()
                        r[i] = '\n'.join(wr) + '\n'
                        f += 1
                    continue
            
            # Regular paragraph
            wr = wrap_line(s, mx)
            if len(wr) > 1:
                r[i] = '\n'.join(wr) + '\n'
                f += 1
    
    return r, f


# ===== PIPELINE =====

def process_file(fp):
    global TOTAL
    with open(fp, encoding='utf-8') as f: ct = f.read()
    has_nl = ct.endswith('\n')
    ls = ct.split('\n')
    if has_nl and ls and ls[-1] == '': ls = ls[:-1]
    if not ls: return

    ff = fences(ls)
    total_fixed = 0

    # Pass 1: simple text fixes (order matters for some)
    for nm, fn in [
        ('MD004', fix_md004),
        ('MD007', fix_md007),
        ('MD009', fix_md009),
        ('MD025', fix_md025),
        ('MD027', fix_md027),
        ('MD034', fix_md034),
        ('MD036', fix_md036),
        ('MD040', fix_md040),
        ('MD053', fix_md053),
        ('MD055', fix_md055),
        ('MD056', fix_md056),
        ('MD060', fix_md060),
    ]:
        nl, cnt = fn(ls, ff)
        if cnt: total_fixed += cnt; log(f"  {nm}: {cnt}")
        ls = nl; ff = fences(ls)

    # Pass 2: blank line cleanup first
    nl, cnt = fix_md012(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD012: {cnt}")
    ls = nl; ff = fences(ls)

    # Pass 3: structural insertions
    for nm, fn in [
        ('MD031', fix_md031),
        ('MD032', fix_md032),
        ('MD058', fix_md058),
    ]:
        nl, cnt = fn(ls, ff)
        if cnt: total_fixed += cnt; log(f"  {nm}: {cnt}")
        ls = nl; ff = fences(ls)

    # Pass 4: final blank cleanup
    nl, cnt = fix_md012(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD012(final): {cnt}")
    ls = nl; ff = fences(ls)

    # Pass 5: duplicate headings
    nl, cnt = fix_md024(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD024: {cnt}")
    ls = nl; ff = fences(ls)

    # Pass 6: ordered list prefix
    nl, cnt = fix_md029(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD029: {cnt}")
    ls = nl; ff = fences(ls)

    # Pass 7: line length (always last - most disruptive)
    nl, cnt = fix_md013(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD013: {cnt}")
    ls = nl; ff = fences(ls)

    # Write
    out = '\n'.join(ls)
    if has_nl: out += '\n'
    if total_fixed > 0:
        with open(fp, 'w', encoding='utf-8') as f: f.write(out)
        TOTAL += total_fixed
        log(f"Fixed {total_fixed} in {fp}")
    else:
        log(f"No fixes in {fp}")


def main():
    global TOTAL
    fs = sorted(glob.glob(f"{BASE}/**/*.md", recursive=True))
    log(f"Found {len(fs)} files")
    for fp in fs:
        try: process_file(fp)
        except Exception as e:
            log(f"ERROR {fp}: {e}")
            import traceback; traceback.print_exc()
    log(f"\n=== Total: {TOTAL} fixes ===")


if __name__ == '__main__':
    main()
