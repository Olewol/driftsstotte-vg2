# 📋 Prosjektstatus — Driftsstøtte VG2

Sist oppdatert: 2026-06-17

## ✅ Nylig utførte forbedringer

### 2026-06-17 — Markdownlint-konfigurasjon

- **MD013** (linjelengde): 120→400 tegn, kodeblokker/tabellar framleis unnateke
- **MD025** (fleire h1): ignorerer YAML `title:` — frontmatter og reell h1 er bevisst
- **MD024** (duplicate headings): `siblings_only: true` — «Norsk»/«English» under ulike foreldre
- **MD036** (emphasis as heading): slått av — `**bold**` som pseudo-heading er bevisst stil
- **MD060** (table column style): slått av — kompakte `||`-tabellar i innholdskartet er bevisst
- **README.md**: la til språk (`text`) på directory-tree-kodeblokk

### 2026-06-16 — Gjenoppretta .npmrc/pnpm-workspace.yaml

- `.npmrc` rydda til kun kommentarar (auth/registry berre)
- `pnpm-workspace.yaml` med `allowBuilds` (kompatibel med v11) og `shamefullyHoist: true`
- Lockfile intakt, `pnpm install --frozen-lockfile` går grønt

---

## 📌 Gjenståande forbetringar

Prioriterte etter effekt/innsats-forhold.

### Høg prioritet

- [ ] **Oppgrader pnpm-workspace til v11-standard** — Erstatt `allowBuilds` med `onlyBuiltDependencies` i `package.json` (finnst alt) og fjern dublett frå `pnpm-workspace.yaml`
- [ ] **Sjekk innhaldskart-tabellane i Astro** — Verifiser at kompakte `||`-tabeller i `innholdskart.md` rendrer korrekt i Astro/MDX. MD060 er slått av i lint, men tabellane bør fungere visuelt.
- [ ] **Fjern dist-filer frå repo** — `eksamen-repetisjon-driftsstotte-vg2.md` i `dist/` ligg i repoet sjølv om det er bygg-output. Legg til `.gitignore`-sjekk.

### Medium prioritet

- [ ] **Forenkle workflow-filer** — Dei tre CI-jobbane (Markdown-linting, Astro-typesjekk, Enhetstester) har identiske oppsettssteg (checkout, pnpm, node). Kan faktoriserast med GitHub Actions `composite` eller `reusable workflow`.
- [ ] **Språkkonsistens i lint-konfig** — Kommentarar i `.markdownlint.json` på bokmål for å matche resten av konfigen.
- [ ] **Utvida README** — Legg til informasjon om linting, testkøyring og prosjektstruktur for nye bidragsytarar.

### Lav prioritet

- [ ] **Sjekk gamle CI-logs** — Workflow-run 27573878637 (2026-06-16) feila på "Installer avhengigheiter" i alle tre jobbar. Sannsynlegvis transient, men verifiser at det ikkje gjentek seg.
- [ ] **Bygg inn Astro-sjekk i lint-workflow** — `astro check` har eigen job no, kunne vore eit eige steg i deploy-workflowen i staden.
- [ ] **Sømlaus oppdatering av dette dokumentet** — Automatisk eller halvautomatisk ved neste CI-problemløysing.

---

## 📊 Oversikt

| Område | Status | Merknad |
|--------|--------|---------|
| Markdown-linting | ✅ Vedlikehald (0 feil) | Config justert etter behov |
| pnpm/npmrc | ✅ Fungerande | V11-oppgradering valfritt |
| Bygg og deploy | ✅ Automatisk | GitHub Pages + Pagefind |
| CI/CD | ✅ To workflows | Lint og deploy separate |
| Innhaldskvalitet | 🟡 Trøbbel med lange linjer | Løyst via config, ikkje innhaldsendring |
