#!/usr/bin/env python3
"""Add Digdir as 4th source to km-06. Safe replace operations."""
path = "/home/ole/workspace/driftsstotte-vg2/src/content/kompetansemaal/km-06-dokumentasjon.md"
content = open(path).read()

# 1. Frontmatter kilder
c1 = content.replace(
"  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372\n  - https://www.itil.org/",
"  - https://www.udir.no/lk20/itk02-01/kompetansemaal-og-vurdering/kv372\n  - https://www.digdir.no/informasjonssikkerhet/\n  - https://www.itil.org/"
)

# 2. Norsk planning methodology
c2 = c1.replace(
"- **ITIL** — Beste praksis for IT-tjenestehandtering\n- **PDCA (Plan-Do-Check-Act)** — Sirkulaer forbedringsprosess\n- **Tidsestimering** — Aa kunne anslaa hvor lang tid oppgaver tar",
"- **ITIL** — Beste praksis for IT-tjenestehandtering\n- **Digdir** — Digitaliseringsdirektoratets retningslinjer for informasjonssikkerhet[^4]\n- **PDCA (Plan-Do-Check-Act)** — Sirkulaer forbedringsprosess\n- **Tidsestimering** — Aa kunne anslaa hvor lang tid oppgaver tar"
)

# 3. English planning methodology
c3 = c2.replace(
"- **ITIL** — Best practice for IT service management\n- **PDCA (Plan-Do-Check-Act)** — Continuous improvement cycle\n- **Time estimation** — Being able to estimate how long tasks will take",
"- **ITIL** — Best practice for IT service management\n- **Digdir** — Norwegian Digitalisation Agency's guidelines for information security[^4]\n- **PDCA (Plan-Do-Check-Act)** — Continuous improvement cycle\n- **Time estimation** — Being able to estimate how long tasks will take"
)

# 4. Footnotes
c4 = c3.replace(
"[^3]: AXELOS. ITIL Foundation. https://www.itil.org/",
"[^3]: AXELOS. ITIL Foundation. https://www.itil.org/\n[^4]: Digdir. Informasjonssikkerhet. https://www.digdir.no/informasjonssikkerhet/"
)

open(path, "w").write(c4)
print("Done. File updated.")

# Verify
verify = open(path).read()
print(f"Size: {len(verify)} chars, {verify.count(chr(10))} lines")
print(f"Frontmatter kilder: {verify.count('  - https://')}")
print(f"Digdir mentions: {verify.count('Digdir')}")
print(f"Footnotes: {len([l for l in verify.split(chr(10)) if l.startswith('[^')])}")
