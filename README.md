# Driftsstøtte VG2

Læringsressurser for faget Driftsstøtte (VG2) — bygd med [Astro](https://astro.build) 5 og deployert til GitHub Pages.

## Innhald

- **Fagstoff** — 6 kategoriar med djupneartiklar (nettverk, sikkerheit, IT-drift, operativsystem, skripting, databaser)
- **Repetisjonssider** — 9 eksamensretta faktasider med interaktive element
- **Flashcards** — sjølvtester for kvart emne
- **Årsplan** — oversikt over skuleåret
- **Søk** — fulltekstsøk via Pagefind

## Tospråkleg innhald

Kvart emne har både bokmål (`.md`) og engelsk (`-en.md`) versjonar. Språkveljar i menyen lar elevane veksle mellom språka.

## Køyr lokalt

```bash
npm install
npm run dev        # utviklingsserver på :4321
npm run build      # produksjonsbygg til dist/
npm run preview    # førehandsvis det ferdige bygget
```

## Struktur

```
/
├── public/
│   ├── audio/          # Lydfiler
│   ├── diagrams/       # SVG-diagram (18 stk)
│   └── video/          # Videofiler
├── src/
│   ├── content/
│   │   ├── aarsplan/   # Årsplan
│   │   ├── emner/      # Fagstoff (6 kategoriar × 2 språk)
│   │   ├── flashcards/ # Sjølvtester
│   │   └── oppgaver/   # Øvingsoppgåver
│   ├── components/     # Gjenbrukbare komponentar
│   ├── layouts/        # Sidemalar
│   ├── pages/          # Ruter og sider
│   │   ├── [emne]/     # Dynamiske emnesider
│   │   └── repetisjon/ # Eksamensrepetisjon
│   └── styles/         # Global CSS + Tailwind
├── .github/workflows/
│   ├── deploy.yml      # Bygg + deploy til GitHub Pages
│   └── lint.yml        # Markdown-linting + Astro-typesjekk
└── package.json
```

## CI/CD

- **Deploy** — automatisk bygg og deploy til GitHub Pages ved push til `main`
- **Lint** — markdown-linting med `markdownlint-cli2` og Astro-typesjekk
- **Krav** — Node.js >= 22.12.0

## Lisens

Internt undervisningsmateriell.
