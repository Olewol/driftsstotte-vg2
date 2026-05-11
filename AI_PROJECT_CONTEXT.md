# AI context for driftsstotte-vg2 repo

## Eksamensrepetisjon-seksjon

Lagt til en underseksjon `repetisjon` for eksamensrepetisjon VG2 Driftsstøtte.

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

|### Design:
|- Mørk tema (matcher resten av siden)
|- RepetisjonLayout: innebygget TOC-generering fra h2-headings, fremdriftsindikator (topic X/9), scroll-spy
|- "Husk til eksamen" callout-boks på hver side (`.eksamen-callout`)
|- "Tips" callout-boks (`.tips-callout`)
- Navigasjon mellom temaer (forrige/neste)
- Oppgaver: interaktive klikk-for-å-se-svar-kort

## Mai 2026 — Oppgradering til Eksamensrepetisjon

### Endringer:
- Nav-etikett: "Eksamen" → "Eksamensrepetisjon"
- Index-side: "Eksamensforberedelse" → "Eksamensrepetisjon"
- Rettet norske skrivefeil fra tidligere humaniseringsrunde (a→å, o→ø, pålitelig, feilsøking, sårbarhetshåndtering, overvåking, nøkkelbegreper m.m.)
- Lagt til ASCII-illustrasjoner i `<pre>`-blokker:
  - AD-hierarki (brukeradministrasjon)
  - OSI-modellen (nettverksprotokoller)
  - TCP 3-way handshake (nettverksprotokoller)
  - Defense in depth-lag med angriper → trygt (sikkerhet-driftsprinsipper)
  - DMZ-arkitektur (nettverkssikkerhet)
  - VLAN-trunking (nettverk-segmentering)
  - DHCP DORA-prosess (nettverk-segmentering)
- Forbedret avsnittsstruktur med flere underoverskrifter og tydeligere visuell organisering
- Consistent norsk bokmål gjennom alle repetisjonssider (med unntak av bransjeord og faguttrykk)
