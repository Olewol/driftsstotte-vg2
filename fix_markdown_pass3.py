#!/usr/bin/env python3
"""
Pass 3: Fix remaining errors after pass 2.
Remaining: MD012(173), MD013(48), MD025(33), MD028(28), MD053(25), MD032(23),
           MD022(15), MD031(11), MD034(9), MD060(4), MD040(4), MD018(3),
           MD024(2), MD001(2), MD052(1), MD004(1)
"""
import re, glob

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
    s = l.strip()
    if not s.startswith('|') or not s.endswith('|'): return False
    return all(ch in '-: ' for ch in s[1:-1])

# ===== FIXES =====

def fix_md001(lines, ff):
    """Fix heading levels that skip a level."""
    f = 0; r = list(lines); fm = fm_end(r)
    prev = 0
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff): continue
        m = re.match(r'^(#{1,6})\s+', l)
        if m:
            lvl = len(m.group(1))
            if prev > 0 and lvl > prev + 1:
                r[i] = '#' * (prev + 1) + l[lvl:]
                f += 1
                lvl = prev + 1
            prev = lvl
        elif not blank(l):
            prev = 0
    return r, f

def fix_md004(lines, ff):
    """Change + list markers to -"""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        if re.match(r'^\s*\+\s', l):
            r[i] = re.sub(r'^(\s*)\+\s', r'\1- ', l, count=1); f += 1
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

def fix_md018(lines, ff):
    """Fix shebang lines falsely detected as headings: ensure #! lines have context."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        # Check if shebang is after a heading with no space
        m = re.match(r'^(#{1,6})!/', l)
        if m:
            r[i] = l.replace(m.group(1), '')
            f += 1
            continue
        # Check standalone shebang
        if l.strip().startswith('#!'):
            # Already correct - not a heading, but make sure lint doesn't flag it
            pass
        # Check lines like "### Shebang — `#!/bin/bash`TText" - heading directly followed by content
        # This is MD022 (no blank after heading) combined with a shebang inline
    return r, f

def fix_md022(lines, ff):
    """Ensure blank lines after headings."""
    f = 0; r = list(lines); fm = fm_end(r)
    ia = set()
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff) or not heading(l): continue
        if i+1 < len(r) and not blank(r[i+1]) and not heading(r[i+1]):
            ia.add(i); f += 1
    for idx in sorted(ia, reverse=True): r.insert(idx+1, '')
    return r, f

def fix_md024(lines, ff):
    """Make duplicate headings unique."""
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

def fix_md025(lines, ff):
    """Demote extra H1 to H2."""
    f = 0; r = list(lines); fm = fm_end(r)
    idxs = [i for i in range(len(r)) if i > fm and not inside(i, ff) and re.match(r'^# [^#]', r[i])]
    if len(idxs) <= 1: return r, 0
    for i in idxs[1:]: 
        r[i] = '#' + r[i]; f += 1
    return r, f

def fix_md028(lines, ff):
    """Remove blank lines inside blockquotes.
    Two blank lines within a blockquote break it. Remove them."""
    f = 0; r = list(lines)
    i = 0
    while i < len(r):
        if inside(i, ff): i += 1; continue
        if r[i].strip().startswith('>'):
            # Found start of a blockquote
            bq_lines = []
            while i < len(r) and (r[i].strip().startswith('>') or blank(r[i])):
                bq_lines.append(i); i += 1
            # Now check for blank lines within the blockquote range
            # A blank line inside blockquote is when we have:
            # > text
            # (blank)
            # > more text
            # The blank line without > prefix between > lines is the issue
            if len(bq_lines) >= 3:
                to_remove = []
                for j in range(1, len(bq_lines) - 1):
                    idx = bq_lines[j]
                    if blank(r[idx]) and not blank(r[bq_lines[j-1]]) and not blank(r[bq_lines[j+1]]):
                        # This blank line is between two non-blank lines
                        # Check that the surrounding lines are blockquote content
                        before = r[bq_lines[j-1]].strip().startswith('>')
                        after = r[bq_lines[j+1]].strip().startswith('>')
                        if before or after:
                            to_remove.append(idx)
                for idx in sorted(to_remove, reverse=True):
                    r.pop(idx)
                    f += 1
                    # Also need to update bq_lines and i
                    # Instead, restart scan from current position
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
        if re.match(r'^(\s*)([-*+]|\d+\.)\s', r[i]):
            s = i
            while i < len(r) and re.match(r'^(\s*)([-*+]|\d+\.)\s', r[i]): i += 1
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
        if '](' in l: continue  # skip markdown links
        # Match URLs that aren't already in angle brackets
        n = re.sub(r'(?<!")(?<!\()(https?://[^\s<>"\'\]\)}]+)(?!["\'>\)])', r'<\1>', l)
        if n != l: r[i] = n; f += 1
    return r, f

def fix_md040(lines, ff):
    """Add language spec to code fences."""
    f = 0; r = list(lines)
    for s, e in ff:
        c = r[s].strip()
        if c == '```':
            r[s] = '```text'; f += 1
    return r, f

def fix_md052(lines, ff):
    """Fix reference definitions so they're not concatenated incorrectly."""
    f = 0; r = list(lines)
    # Look for patterns like [^1][^2] on same line
    for i, l in enumerate(r):
        if inside(i, ff): continue
        # Fix [^1][^2] - these should be separate references, not concatenated
        m = re.search(r'\[(\^?\w+)\]\[(\^?\w+)\]', l)
        if m:
            # Split them into separate bracket pairs
            r[i] = l.replace(m.group(0), f'{m.group(1)}] [{m.group(2)}')
            f += 1
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
                if end < len(l) and l[end] == '(': continue
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

def fix_md060(lines, ff):
    """Fix table cell spacing."""
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

def wrap_line_strict(text, mx, prefix='', cont_prefix=''):
    """Strict word-wrap: never break URLs or inline code."""
    if prefix and text.startswith(prefix):
        content = text[len(prefix):]
    else:
        content = text
    
    words = content.split()
    if not words: return [text]
    
    first_indent = len(prefix)
    cont_indent = len(cont_prefix)
    first_mx = mx - first_indent
    cont_mx = mx - cont_indent
    
    if len(content) <= first_mx:
        return [text]
    
    out = []
    cur = ''
    for w in words:
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
    
    if len(out) <= 1:
        return [text]
    return out

def fix_md013(lines, ff, mx=120):
    """Break long lines at word boundaries."""
    f = 0; r = list(lines); fm = fm_end(r)
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff): continue
        s = l.rstrip('\n\r')
        if not s: continue
        if tblrow(s) or tbsep(s): continue
        if len(s) > mx:
            # Detect blockquote
            bqm = re.match(r'^(>\s?)(.*)', s)
            if bqm:
                prefix = '> '
                cont_prefix = '> '
                wr = wrap_line_strict(s, mx, prefix=prefix, cont_prefix=cont_prefix)
                if len(wr) > 1:
                    r[i] = '\n'.join(wr) + '\n'
                    f += 1
                continue
            
            # Detect list item
            lim = re.match(r'^(\s*)([-*+]|\d+\.)\s', s)
            if lim:
                first_prefix = lim.group(0)
                cont_indent = lim.group(1) + ' ' * (len(lim.group(2)) + 1)
                wr = wrap_line_strict(s, mx, prefix='', cont_prefix=cont_indent)
                if len(wr) > 1:
                    # Reconstruct: first line uses original prefix, rest use cont indent
                    wr[0] = first_prefix + wr[0].lstrip() if not wr[0].lstrip().startswith(first_prefix.lstrip()) else wr[0]
                    for j in range(1, len(wr)):
                        if not wr[j].startswith(cont_indent):
                            wr[j] = cont_indent + wr[j].lstrip()
                    r[i] = '\n'.join(wr) + '\n'
                    f += 1
                continue
            
            # Regular content
            wr = wrap_line_strict(s, mx)
            if len(wr) > 1:
                r[i] = '\n'.join(wr) + '\n'
                f += 1
    return r, f


def process_file(fp):
    global TOTAL
    with open(fp, encoding='utf-8') as f: ct = f.read()
    has_nl = ct.endswith('\n')
    ls = ct.split('\n')
    if has_nl and ls and ls[-1] == '': ls = ls[:-1]
    if not ls: return

    ff = fences(ls)
    total_fixed = 0

    # Order matters: structural fixes before MD013
    
    for nm, fn in [
        ('MD001', fix_md001),
        ('MD004', fix_md004),
        ('MD018', fix_md018),
        ('MD025', fix_md025),
        ('MD034', fix_md034),
        ('MD040', fix_md040),
        ('MD052', fix_md052),
        ('MD053', fix_md053),
        ('MD060', fix_md060),
    ]:
        nl, cnt = fn(ls, ff)
        if cnt: total_fixed += cnt; log(f"  {nm}: {cnt}")
        ls = nl; ff = fences(ls)

    # Blank collapse
    nl, cnt = fix_md012(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD012: {cnt}")
    ls = nl; ff = fences(ls)

    # Structural
    for nm, fn in [
        ('MD022', fix_md022),
        ('MD028', fix_md028),
        ('MD031', fix_md031),
        ('MD032', fix_md032),
        ('MD024', fix_md024),
    ]:
        nl, cnt = fn(ls, ff)
        if cnt: total_fixed += cnt; log(f"  {nm}: {cnt}")
        ls = nl; ff = fences(ls)

    # Final blank collapse
    nl, cnt = fix_md012(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD012(f): {cnt}")
    ls = nl; ff = fences(ls)

    # MD013 last
    nl, cnt = fix_md013(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD013: {cnt}")
    ls = nl; ff = fences(ls)

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
