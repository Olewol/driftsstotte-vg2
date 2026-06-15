#!/usr/bin/env python3
"""
Comprehensive markdownlint auto-fix for src/content/.
Strategy:
  Pass A: Text-level fixes (MD004, MD025, MD026, MD034, MD036, MD037, MD038,
           MD040, MD053, MD055, MD056, MD060, MD009)
  Pass B: Collapse multiple blank lines (MD012)
  Pass C: Structural blank-line insertions (MD022, MD031, MD032, MD058)
  Pass D: Final collapse (MD012 again)
  Pass E: Line length (MD013)
  Pass F: Duplicate headings (MD024), Ordered list prefix (MD029)
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

def inside(idx, f):
    return any(s < idx <= e for s, e in f)

def tbsep(l):
    """True if line is a table separator row like |---|---|"""
    s = l.strip()
    if not s.startswith('|') or not s.endswith('|'): return False
    return all(ch in '-: ' for ch in s[1:-1])

# -- helpers --
def safe_fences(ff, lines):
    """Recalculate fences; fences param might be stale if lines changed."""
    return fences(lines)

# ===== PASS A: TEXT FIXES =====

def a_md004(lines, ff):
    """Change * list markers to - for consistency."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        if re.match(r'^\s*\*\s', l):
            r[i] = re.sub(r'^(\s*)\*\s', r'\1- ', l, count=1); f += 1
    return r, f

def a_md009(lines, ff):
    """Strip trailing whitespace."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        s = l.rstrip()
        if s != l:
            # preserve the trailing newline
            r[i] = s + '\n'; f += 1
    return r, f

def a_md025(lines, ff):
    """Demote extra H1 to H2."""
    f = 0; r = list(lines); fm = fm_end(r)
    idxs = [i for i in range(len(r)) if i > fm and not inside(i, ff) and re.match(r'^# [^#]', r[i])]
    if len(idxs) <= 1: return r, 0
    for i in idxs[1:]: r[i] = '#' + r[i]; f += 1
    return r, f

def a_md026(lines, ff):
    """Remove trailing punctuation from headings."""
    f = 0; r = list(lines); fm = fm_end(r)
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff): continue
        m = re.match(r'^(#{1,6}\s+)(.+?)([.:;,!?。，；：！？\)）]+)(\s*)$', l)
        if m:
            r[i] = f'{m.group(1)}{m.group(2)}{m.group(4)}'; f += 1
    return r, f

def a_md034(lines, ff):
    """Wrap bare URLs in angle brackets."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff) or '](' in l: continue
        def w(m):
            u = m.group(0); p = m.start()
            if p > 0 and l[p-1] == '<': return u
            return f'<{u}>'
        n = re.sub(r'(?<!<)(https?://[^\s<>"\'\]\)}]+)(?!>)', w, l)
        if n != l: r[i] = n; f += 1
    return r, f

def a_md036(lines, ff):
    """Convert **text** or __text__ on its own line to heading."""
    f = 0; r = list(lines)
    pat = re.compile(r'^\s*(\*\*|__)(.+?)(\*\*|__)\s*$')
    for i, l in enumerate(r):
        if inside(i, ff) or heading(l): continue
        m = pat.match(l)
        if m and m.group(1) == m.group(3):
            t = m.group(2).strip()
            if t and len(t) < 100:
                # Strip trailing punctuation for MD026 compliance
                t = re.sub(r'[.:;,!?。，；：！？\)）]+$', '', t).strip()
                if t:
                    r[i] = f'## {t}'; f += 1
    return r, f

def a_md037(lines, ff):
    """Remove spaces inside emphasis markers."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        n = re.sub(r'\*\*\s+([^*]+?)\s+\*\*', r'**\1**', l)
        n = re.sub(r'(?<!\*)\*\s+([^*]+?)\s+\*(?!\*)', r'*\1*', n)
        if n != l: r[i] = n; f += 1
    return r, f

def a_md038(lines, ff):
    """Remove spaces inside code span markers."""
    f = 0; r = list(lines)
    for i, l in enumerate(r):
        if inside(i, ff): continue
        n = re.sub(r'`\s+([^`]+?)\s+`', r'`\1`', l)
        if n != l: r[i] = n; f += 1
    return r, f

def a_md040(lines, ff):
    """Add 'text' language to code fences missing it."""
    f = 0; r = list(lines)
    for s, e in ff:
        c = r[s].strip()
        if c == '```':
            r[s] = '```text'; f += 1
    return r, f

def a_md053(lines, ff):
    """Remove unused reference definitions."""
    f = 0; r = list(lines)
    defs = {}; uses = set()
    for i, l in enumerate(r):
        if inside(i, ff): continue
        m = re.match(r'^(\s*)\[([^\]]+)\]:\s+\S', l)
        if m: defs[m.group(2)] = i
    for i, l in enumerate(r):
        if inside(i, ff): continue
        for m in re.finditer(r'(?<!!)\[([^\]]+)\]', l):
            lbl = m.group(1)
            if lbl:
                end = m.end()
                if end < len(l) and l[end] == '(': continue
                if end < len(l) and l[end:end+1] == ':': continue
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

def a_md055(lines, ff):
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

def a_md056(lines, ff):
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

def a_md060(lines, ff):
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

# ===== PASS B: COLLAPSE BLANK LINES =====

def b_md012(lines):
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

# ===== PASS C: STRUCTURAL INSERTIONS =====

def c_md022(lines, ff):
    """Ensure blank lines before headings (above) and after (below)."""
    f = 0; r = list(lines); fm = fm_end(r)
    ib = set(); ia = set()
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff) or not heading(l): continue
        # Above
        if i > 0 and not blank(r[i-1]) and i > fm+1:
            ib.add(i); f += 1
        # Below (skip if next is another heading or blank or eof)
        if i+1 < len(r) and not blank(r[i+1]) and not heading(r[i+1]):
            ia.add(i); f += 1
    for idx in sorted(ia, reverse=True): r.insert(idx+1, '')
    for idx in sorted(ib, reverse=True): r.insert(idx, '')
    return r, f

def c_md031(lines, ff):
    """Ensure blank lines before and after fenced code blocks."""
    f = 0; r = list(lines); fm = fm_end(r)
    ib = set(); ia = set()
    for s, e in ff:
        if s > fm+1 and s > 0 and not blank(r[s-1]): ib.add(s); f += 1
        if e+1 < len(r) and not blank(r[e+1]): ia.add(e); f += 1
    for idx in sorted(ia, reverse=True): r.insert(idx+1, '')
    for idx in sorted(ib, reverse=True): r.insert(idx, '')
    return r, f

def c_md032(lines, ff):
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

def c_md058(lines, ff):
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

# ===== PASS D/E/F: FINAL TOUCHES =====

def e_md013(lines, ff, mx=120):
    """Break long lines at word boundaries."""
    f = 0; r = list(lines); fm = fm_end(r)
    for i, l in enumerate(r):
        if i <= fm or inside(i, ff): continue
        s = l.rstrip()
        if tblrow(s) or tbsep(s): continue
        if len(s) > mx:
            im = re.match(r'^(\s*)', s)
            ind = im.group(1) if im else ''
            ww = wrap(s, mx, ind)
            if len(ww) > 1: r[i] = '\n'.join(ww) + '\n'; f += 1
    return r, f

def wrap(text, mx, ind=''):
    ws = text.split()
    if not ws: return [text]
    out = []; cur = ''
    for w in ws:
        n = f'{cur} {w}'.strip() if cur else w
        if len(n) <= mx: cur = n
        else:
            if cur: out.append(cur)
            cur = ind + w
    if cur: out.append(cur)
    return out if len(out) > 1 else [text]

def f_md024(lines, ff):
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
            # find nearest parent heading
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

def f_md029(lines, ff):
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

# ===== MAIN PIPELINE =====

def process_file(fp):
    global TOTAL
    with open(fp, encoding='utf-8') as f: ct = f.read()
    has_nl = ct.endswith('\n')
    ls = ct.split('\n')
    if has_nl and ls and ls[-1] == '': ls = ls[:-1]
    if not ls: return

    ff = fences(ls)
    total_fixed = 0

    # Pass A: text fixes
    for nm, fn in [
        ('MD004', a_md004), ('MD025', a_md025), ('MD026', a_md026),
        ('MD034', a_md034), ('MD036', a_md036), ('MD037', a_md037),
        ('MD038', a_md038), ('MD040', a_md040), ('MD053', a_md053),
        ('MD055', a_md055), ('MD056', a_md056), ('MD060', a_md060),
        ('MD009', a_md009),
    ]:
        nl, c = fn(ls, ff)
        if c: total_fixed += c; log(f"  {nm}: {c}")
        ls = nl; ff = fences(ls)

    # Pass B: initial blank cleanup
    nl, c = b_md012(ls)
    if c: total_fixed += c; log(f"  MD012(A): {c}")
    ls = nl; ff = fences(ls)

    # Pass C: structural insertions
    for nm, fn in [
        ('MD022', c_md022), ('MD031', c_md031),
        ('MD032', c_md032), ('MD058', c_md058),
    ]:
        nl, c = fn(ls, ff)
        if c: total_fixed += c; log(f"  {nm}: {c}")
        ls = nl; ff = fences(ls)

    # Pass D: final blank cleanup
    nl, c = b_md012(ls)
    if c: total_fixed += c; log(f"  MD012(B): {c}")
    ls = nl; ff = fences(ls)

    # Pass E: line length
    nl, c = e_md013(ls, ff)
    if c: total_fixed += c; log(f"  MD013: {c}")
    ls = nl; ff = fences(ls)

    # Pass F: duplicates & ordered lists
    for nm, fn in [('MD024', f_md024), ('MD029', f_md029)]:
        nl, c = fn(ls, ff)
        if c: total_fixed += c; log(f"  {nm}: {c}")
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
