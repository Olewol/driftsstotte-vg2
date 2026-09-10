---
title: "AI_PROJECT_CONTEXT — Driftsstøtte VG2"
public: true
---

# AI Project Context — Driftsstøtte VG2

## Tre repoer

| Repo | Synlighet | URL | Publisert |
|------|-----------|-----|-----------|
| driftsstotte-vault | Privat | github.com/Olewol/driftsstotte-vault | Nei (Obsidian) |
| driftsstotte-vg2 | Public | github.com/Olewol/driftsstotte-vg2 | https://Olewol.github.io/driftsstotte-vg2 |
| oppgaver-for-2IT | Public | github.com/Olewol/oppgaver-for-2IT | https://olewol.github.io/oppgaver-for-2IT |

## Pipeline

driftsstotte-vault (public/emner/*.md) → GitHub Actions (filter_publish.py) → driftsstotte-vg2 (src/content/emner/) → Astro build → GitHub Pages

## Innholdsstatus (27 emner × 2 språk)

- **Norsk (nb)**: 27 emner + 6 oversikter — ✅ komplett med fotnoter
- **Engelsk (en)**: 27 emner + 6 oversikter — ✅ oversatt, mangler inline fotnoter
- **Video**: 18/27 har YouTube/NDLA-video — ❌ 9 mangler
- **Flashcards**: 6 NotebookLM-genererte sett — ✅ lastet ned
- **NotebookLM Audio**: ⏳ 12 podcaster bestilt (cron 08:00)
- **MDX-demo**: 1 interaktiv side med YouTube + 5 flashcards

## Kanban (driftsstotte-board)

Gjenværende tasks:
- Audio Overviews (cron 08:00)
- Video til 9 emner
- Oppgaver til flere KM
- Bygg interaktiv flashcard-seksjon på alle sider

## Astro-plugins (fungerende)

tailwind, mermaid, expressive-code, sitemap, mdx@4, embed-youtube, remark-wiki-link, rehype-external-links

## Alle emner (27 stk)

nettverk: osi-modellen, tcp-ip-modellen, nettverksprotokoller, dns-og-dhcp, segmentering-og-vlan, serverroller, virtuelle-losninger
sikkerhet: trusselbildet, risikoanalyse, brannmur, kryptering, personvern, it-losninger-med-sikkerhet
it-drift: driftsarkitektur, skytjenester, backup-og-gjenoppretting, dokumentasjon-og-planlegging, baerekraft
operativsystem: active-directory, bruker-og-tilgangsstyring, filsystem, linux-grunnleggende
skripting: automatisering, bash-grunnleggende, powershell-grunnleggende
databaser: databaseadministrasjon, sql-grunnleggende
