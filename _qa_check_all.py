#!/usr/bin/env python3
"""Comprehensive QA check of all 12 kompetansemal files."""
import yaml, os, re, sys

base = "/home/ole/workspace/driftsstotte-vg2"
km_dir = os.path.join(base, "src/content/kompetansemaal")
emner_dir = os.path.join(base, "src/content/emner")

known_emner = set()
for root, dirs, files in os.walk(emner_dir):
    for fn in files:
        if fn.endswith(".md") or fn.endswith(".mdx"):
            known_emner.add(fn.replace(".md", "").replace(".mdx", ""))

errors = []
warnings = []

for fn in sorted(os.listdir(km_dir)):
    if not (fn.startswith("km-") and fn.endswith(".md")):
        continue
    filepath = os.path.join(km_dir, fn)
    content = open(filepath).read()
    
    parts = content.split("---")
    if len(parts) < 3:
        errors.append(f"{fn}: Missing YAML frontmatter")
        continue
    
    try:
        data = yaml.safe_load(parts[1])
    except Exception as e:
        errors.append(f"{fn}: YAML error - {e}")
        continue
    
    required = ["title", "emne", "kompetansemaal", "kilder", "tags", "flashcards", "public"]
    for k in required:
        if k not in data:
            errors.append(f"{fn}: Missing frontmatter key '{k}'")
    
    if "kilder" in data and len(data["kilder"]) < 3:
        errors.append(f"{fn}: Only {len(data['kilder'])} sources (min 3)")
    
    sections = re.findall(r'^## (.*)', content, re.MULTILINE)
    # Match sections flexibly: strip emoji prefixes and handle Unicode/Norwegian chars
    # Actual headings use e.g. "🎯 Mål / Competency Goal", "📘 Forklaring / Explanation"
    def strip_emoji_prefix(text):
        return re.sub(r'^[\U0001F300-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]\s*', '', text)
    stripped = [strip_emoji_prefix(s) for s in sections]
    expected = [
        "Mål / Competency Goal",
        "Forklaring / Explanation",
        "Eksempler / Examples",
        "Oppsummering / Summary",
        "Bridging Exercises",
        "Relevante artikler / Related Articles",
        "Kilder / Sources",
    ]
    for es in expected:
        if not any(es in s for s in stripped):
            errors.append(f"{fn}: Missing section matching '{es}'")
    
    if "Norsk:" not in content:
        errors.append(f"{fn}: Missing Norsk content")
    if "English:" not in content:
        errors.append(f"{fn}: Missing English content")
    
    if "Bridging Exercises" not in content:
        warnings.append(f"{fn}: Missing Bridging Exercises")
    
    if "<<" in content or "=======" in content:
        errors.append(f"{fn}: Contains merge conflict markers!")
    
    links = re.findall(r'\[\[([^\]]+)\]\]', content)
    for link in links:
        slug = link.split("|")[0].strip()
        if slug not in known_emner:
            warnings.append(f"{fn}: Wikilink [[{link}]] may not resolve")
    
    cites = len(re.findall(r'\[\^\d+\]', content))
    footnotes = len(re.findall(r'^\[\^\d+\]:', content, re.MULTILINE))
    
    print(f"  OK: {fn} — {len(sections)} sections, {len(data.get('kilder',[]))} sources, {cites} cites, {footnotes} footnotes")

print(f"\n{'='*50}")
print(f"Errors: {len(errors)}")
for e in errors:
    print(f"  FAIL: {e}")
print(f"Warnings: {len(warnings)}")
for w in warnings:
    print(f"  WARN: {w}")

fc = len([f for f in os.listdir(km_dir) if f.startswith("km-") and f.endswith(".md")])
print(f"\nFiles checked: {fc}")
print(f"Verdict: {'PASS' if not errors else 'FAIL - fix errors above'}")

sys.exit(1 if errors else 0)
