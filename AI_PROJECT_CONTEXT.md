# AI Project Context — Driftsstøtte VG2

## Arkitektur (3 repoer)

```
driftsstotte-vault (private, Obsidian)       ← KILDEN for alt innhold
  └── public/emner/ → GitHub Actions → driftsstotte-vg2 (public, Astro 5)
                                          → GitHub Pages: https://Olewol.github.io/driftsstotte-vg2
                                 ↕
oppgaver-for-2IT (public, Astro)            ← Oppgaver, eget repo
  → https://olewol.github.io/oppgaver-for-2IT
```

**Pipeline:** Skriv i vault → push main → GH Actions filtrerer `public/` → synker til Astro-repoet → Astro bygger → deployer til Pages

## Kompetansemål (12 stk)

| ID | Beskrivelse | Emner |
|----|------------|-------|
| km-01 | Driftsarkitektur | driftsarkitektur, backup-og-gjenoppretting |
| km-02 | Segmenterte nettverk | segmentering-og-vlan, virtuelle-losninger |
| km-03 | Skytjenester | skytjenester, driftsarkitektur |
| km-04 | Brukere/tilganger | active-directory, bruker-og-tilgangsstyring, filsystem, linux-grunnleggende, databaseadm, sql |
| km-05 | Nettverksprotokoller | osi-modellen, tcp-ip-modellen, protokoller, dns-og-dhcp, serverroller |
| km-06 | Dokumentasjon | dokumentasjon-og-planlegging |
| km-07 | Trusler | trusselbildet |
| km-08 | Risikoanalyse | risikoanalyse |
| km-09 | Automatisering | automatisering, bash, powershell |
| km-10 | Sikkerhet/personvern | brannmur, it-losninger-med-sikkerhet, kryptering |
| km-11 | Personvernbrudd | personvern |
| km-12 | Bærekraft | baerekraft |

## Nåværende innhold

- **27 emner** × 2 språk (nb + en) = 54 filer i `public/emner/`
- **6 oversikter** × 2 språk = 12 `_oversikt.md`-filer
- **8 repetisjonssider** for eksamen i `src/pages/repetisjon/`
- **NotebookLM**: 6 notebooks (én per kategori) med flashcards og quizzer
- **Flashcards**: nedlastet til `public/flashcards/`
- **SVG-diagrammer**: 18 stk i `public/diagrams/`

## Astro-plugins installert

| Plugin | Status | Formål |
|--------|--------|--------|
| `@astrojs/tailwind` | ✅ | Styling |
| `astro-mermaid` | ✅ | Mermaid-diagrammer |
| `astro-expressive-code` | ✅ | Pene kodeblokker |
| `@astrojs/sitemap` | ✅ | Sitemap-generering |
| `@astrojs/mdx@4` | ✅ | Interaktive komponenter i markdown |
| `@astro-community/astro-embed-youtube` | ✅ | YouTube-embedding |
| `remark-wiki-link` | ✅ | Internlenker mellom emner |
| `rehype-external-links` | ✅ | Eksterne linker i ny fane |

## Endringer gjort (2026-05-20/21)

- Alle 27 emner oversatt til engelsk (`-en.md`)
- Kilder oppdatert i alle filer
- Inline kildehenvisning (fotnoter) i alle 27 filer
- Flashcards generert via NotebookLM for alle 6 kategorier
- Mobilmeny: bakgrunn `--bg3`+skygge, 🔍 søk-knapp, 🇳🇴/🇬🇧 språkvelger
- `lang`-attributt: dynamisk `no`/`en` basert på filnavn
- `@astrojs/mdx@4` installert for interaktivt innhold
- `FlashCard.astro` — klikkbare flip-kort
- Bro til oppgaver-for-2IT via `relaterte-oppgaver` i frontmatter

## Kjente problemer

1. **TTSBar** bruker hardkodet `nb-NO` — engelske sider får norsk tale
2. **Video mangler** for 9 emner (SQL, AD, brukerstyring, filsystem, Linux, dokumentasjon, risikoanalyse, trusselbildet, automatisering)
3. **Audio Overviews** — daglig kvote hos Google. Cron-job kl 08:00
4. **@astrojs/mdx@5** kan ikke installeres — krever Astro 6
