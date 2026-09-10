---
title: "Kvalitetsrapport — Driftsstøtte VG2"
emne: driftsstotte
public: true
---

# Kvalitetsrapport — Driftsstøtte VG2

Generert: 2026-05-20

## Målgruppeanalyse

**Målgruppe:** VG2 Informasjonsteknologi-elever, 16-17 år.

### Vurdering av målgruppetilpasning

| Kriterium | Status | Notat |
|-----------|--------|-------|
| Språknivå | ✅ OK | Fagbegreper forklares ved første bruk, aktiv setningsbygning |
| Aktive setninger | ✅ OK | Korte, konsise forklaringer |
| Eksempler fra virkeligheten | ✅ OK | Case-baserte eksempler (Østre Toten, NCS) |
| Visuelle forklaringer | ✅ OK | ASCII-diagrammer, SVG, Mermaid |
| Oppgaveintegrasjon | ⚠️ Delvis | 1 oppgave koblet — flere trengs |
| Varierte læringsstiler | ⚠️ Delvis | Tekst: ✅, Visuelt: ✅, Lyd: ⏳ (audio mangler), Interaktivt: ⏳ |

## Struktursjekk

### 8-seksjoners struktur (emnefiler)
- **Introduksjon** — ✅ alle filer
- **Teori** — ✅ alle filer (med h3/h4 underoverskrifter)
- **Eksempel / lab** — ⚠️ mangler i noen filer
- **Study guide** — ✅ alle filer
- **FAQ** — ✅ alle filer
- **Quiz** — ✅ alle filer
- **Flashcards** — ✅ alle filer (i brødtekst + NotebookLM-genererte)
- **Ressurser / Kilder** — ✅ frontmatter, ⚠️ inline mangler i 26/27 filer

### Forbedringspunkter

1. **Inline kildehenvisning** — kun brannmur.md har fotnoter. 26 filer gjenstår.
2. **Lange avsnitt** — 7 avsnitt over 500 tegn bør splittes
3. **Video** — 9 emner mangler videoressurs (SQL, AD, brukerstyring, filsystem, Linux, dokumentasjon, risikoanalyse, trusselbildet, automatisering)
4. **Audio** — 0/12 podcaster generert (Google rate limited, cron 08:00)
5. **Flere oppgaver** — kun 1 oppgave i oppgaver-for-2IT, trengs for alle KM

## Universell utforming

| Format | Status |
|--------|--------|
| Lesbar (tekst) | ✅ Markdown, alle filer |
| Hørbar (TTS) | ✅ TTSBar.astro med norsk stemme |
| Hørbar (podcast) | ⏳ NotebookLM Audio (i morgen) |
| Synlig (video) | ⚠️ 18/27 med YouTube/NDLA-video |
| Interaktivt (flashcards) | ✅ NotebookLM-generert + egne filer |
| Interaktivt (quiz) | ✅ Innebygd i hver fil |

## Anbefalinger

1. **A:** Fullfør inline kildehenvisning i alle filer
2. **B:** Generér Audio Overviews når kvote resetter
3. **C:** Finn videoer til de 9 manglende emnene
4. **D:** Lag flere oppgaver i oppgaver-for-2IT
5. **E:** Bygg interaktiv flashcard-komponent i Astro
