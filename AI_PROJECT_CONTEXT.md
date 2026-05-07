# AI context for driftsstotte-vg2 repo

## Eksamensrepetisjon-seksjon

Lagt til en ny underseksjon `repetisjon` for eksamensforberedelse VG2 Driftsstøtte.

### Sider lagt til:
- `src/pages/repetisjon/index.astro` — oversikt med kort
- `src/pages/repetisjon/oppgaver.astro` — interaktive oppgaver
- `src/pages/repetisjon/brukeradministrasjon.astro`
- `src/pages/repetisjon/infrastruktur-maskinvare.astro`
- `src/pages/repetisjon/nettverk-segmentering.astro`
- `src/pages/repetisjon/nettverkssikkerhet.astro`
- `src/pages/repetisjon/servermodeller-virtualisering.astro`
- `src/pages/repetisjon/backup-gjenoppretting.astro`
- `src/pages/repetisjon/dokumentasjon-planlegging.astro`
- `src/pages/repetisjon/nettverksprotokoller.astro`
- `src/pages/repetisjon/sikkerhet-driftsprinsipper.astro`

### Layout:
- `src/layouts/RepetisjonLayout.astro` — layout for faktasider med TOC, callout-boks, navigasjon

### Endringer i eksisterende filer:
- `src/components/Nav.astro` — lagt til "Eksamen"-lenke
- `./.gitignore` — legg til node_modules

### Design:
- Mørk tema (matcher resten av siden)
- RepetisjonLayout: innebygget TOC-generering fra h2-headings
- "Husk til eksamen" callout-boks
- Navigasjon mellom temaer (forrige/neste)
- Oppgaver: interaktive klikk-for-å-se-svar-kort
