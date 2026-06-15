#!/usr/bin/env python3
"""
Final pass: fix remaining errors WITHOUT touching MD013 (line-length).
Remaining: MD012(268), MD053(50), MD013(50), MD025(30), MD007(30),
           MD032(26), MD028(26), MD038(18), MD022(9), MD009(9),
           MD034(4), MD031(4), MD001(2), MD004(1), MD003(1)
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
            if i < len(lines): r.append((s, i)); i += 1
            else: r.append((s, len(lines)-1)); break
        else: i += 1
    return r

def inside(idx, ff):
    return any(s < idx <= e for s, e in ff)

def tbsep(l):
    s = l.strip()
    if not s.startswith('|') or not s.endswith('|'): return False
    return all(ch in '-: ' for ch in s[1:-1])

def is_list_line(l):
    return bool(re.match(r'^(\s*)([-*+]|\d+\.)\s', l))

# ===== FIX FUNCTIONS =====

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
                f += 1; lvl = prev + 1
            prev = lvl
        elif not blank(l): prev = 0
    return r, f

def fix_md003(lines, ff):
    """Ensure heading style is ATX (with #)."""
    f = 0; r = list(lines); fm = fm_end(r)
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff): continue
        m = re.match(r'^(.+)\n={3,}$', l, re.MULTILINE)
        if m: pass  # Would need multi-line approach
        if re.match(r'^#+[^#\s]', l):
            # Close-set heading like ##Heading -> ## Heading
            r[i] = re.sub(r'^(#+)(\S)', r'\1 \2', l); f += 1
    return r, f

def fix_md004(lines, ff):
    """Change + list markers to -"""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        if re.match(r'^\s*\+\s', l):
            r[i] = re.sub(r'^(\s*)\+\s', r'\1- ', l, count=1); f += 1
    return r, f

def fix_md007(lines, ff):
    """Fix unordered list indentation: ensure 2-space increments."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        m = re.match(r'^(\s*)([-*+])\s', l)
        if m:
            indent = len(m.group(1))
            new_indent = (indent // 2) * 2
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
        else: bc = 0; r.append(l)
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

def fix_md025(lines, ff):
    """Demote extra H1 to H2."""
    f = 0; r = list(lines); fm = fm_end(r)
    idxs = [i for i in range(len(r)) if i > fm and not inside(i, ff) and re.match(r'^# [^#]', r[i])]
    if len(idxs) <= 1: return r, 0
    for i in idxs[1:]: r[i] = '#' + r[i]; f += 1
    return r, f

def fix_md028(lines, ff):
    """Remove blank lines inside blockquotes by removing blank lines between > lines."""
    f = 0; r = list(lines)
    to_remove = set()
    i = 0
    while i < len(r):
        if inside(i, ff): i += 1; continue
        if r[i].strip().startswith('>'):
            # Find the blockquote range
            bq_idxs = [i]; i += 1
            while i < len(r) and (r[i].strip().startswith('>') or (r[i].strip() == '' and i+1 < len(r) and r[i+1].strip().startswith('>'))):
                bq_idxs.append(i); i += 1
            # Blank lines inside blockquote: those that are empty but between > lines
            for j in range(1, len(bq_idxs) - 1):
                idx = bq_idxs[j]
                if r[idx].strip() == '':
                    prev_has_bq = r[bq_idxs[j-1]].strip().startswith('>')
                    next_has_bq = r[bq_idxs[j+1]].strip().startswith('>')
                    if prev_has_bq and next_has_bq:
                        to_remove.add(idx); f += 1
        else: i += 1
    if to_remove:
        r = [l for i,l in enumerate(r) if i not in to_remove]
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
    """Ensure blank lines around lists.
    Break lists into groups when indentation changes (ordered → sub-list).
    """
    f = 0; r = list(lines); fm = fm_end(r)
    ib = set(); ia = set()
    i = 0
    while i < len(r):
        if inside(i, ff): i += 1; continue
        if is_list_line(r[i]):
            # Get the indent level of the first list item
            s = i
            first_indent = len(re.match(r'^(\s*)', r[i]).group(1))
            while i < len(r) and is_list_line(r[i]):
                curr_indent = len(re.match(r'^(\s*)', r[i]).group(1))
                if curr_indent != first_indent:
                    break  # indentation changed = new list group
                i += 1
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
        if '](' in l: continue
        n = re.sub(r'(?<!")(?<!\()(https?://[^\s<>"\'\]\)}]+)(?!["\'>\)])', r'<\1>', l)
        if n != l: r[i] = n; f += 1
    return r, f

def fix_md038(lines, ff):
    """Remove spaces inside code span markers."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        n = re.sub(r'`\s+([^`]+?)\s+`', r'`\1`', l)
        if n != l: r[i] = n; f += 1
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


def process_file(fp):
    global TOTAL
    with open(fp, encoding='utf-8') as f: ct = f.read()
    has_nl = ct.endswith('\n')
    ls = ct.split('\n')
    if has_nl and ls and ls[-1] == '': ls = ls[:-1]
    if not ls: return

    ff = fences(ls)
    total_fixed = 0

    for nm, fn in [
        ('MD001', fix_md001),
        ('MD003', fix_md003),
        ('MD004', fix_md004),
        ('MD007', fix_md007),
        ('MD009', fix_md009),
        ('MD025', fix_md025),
        ('MD034', fix_md034),
        ('MD038', fix_md038),
        ('MD053', fix_md053),
    ]:
        nl, cnt = fn(ls, ff)
        if cnt: total_fixed += cnt; log(f"  {nm}: {cnt}")
        ls = nl; ff = fences(ls)

    # Blank collapse (before structural, to reduce noise)
    nl, cnt = fix_md012(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD012: {cnt}")
    ls = nl; ff = fences(ls)

    # Structural: blank line insertions
    for nm, fn in [
        ('MD022', fix_md022),
        ('MD028', fix_md028),
        ('MD031', fix_md031),
        ('MD032', fix_md032),
    ]:
        nl, cnt = fn(ls, ff)
        if cnt: total_fixed += cnt; log(f"  {nm}: {cnt}")
        ls = nl; ff = fences(ls)

    # Final blank collapse
    nl, cnt = fix_md012(ls, ff)
    if cnt: total_fixed += cnt; log(f"  MD012(f): {cnt}")
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
