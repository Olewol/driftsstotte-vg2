---
title: "Innholdskart — Driftsstøtte VG2"
emne: driftsstotte
kompetansemaal: [km-01, km-02, km-03, km-04, km-05, km-06, km-07, km-08, km-09, km-10, km-11, km-12]
public: true
---

# Innholdskart — Driftsstøtte VG2

Generert: 2026-05-20

## Arkitektur

```diff
driftsstotte-vault (Obsidian, private)
  └── public/emner/ → GitHub Actions → driftsstotte-vg2 (Astro 5) → GitHub Pages
                                                       ↕
                                        oppgaver-for-2IT (Astro, public)
```

## Dekningsoversikt

|| KM | Beskrivelse | Dekket av | Status |
|| ---- | ------------ | ----------- | -------- |
|| km-01 | Driftsarkitektur | backup-og-gjenoppretting, driftsarkitektur | ✅ |
|| km-02 | Segmenterte nettverk | segmentering-og-vlan, virtuelle-losninger | ✅ |
|| km-03 | Skytjenester | driftsarkitektur, skytjenester | ✅ |
|| km-04 | Brukere/tilganger | active-directory, bruker-og-tilgangsstyring, filsystem, linux-grunnleggende, databaseadministrasjon, sql-grunnleggende | ✅ |
|| km-05 | Nettverksprotokoller | osi-modellen, tcp-ip-modellen, nettverksprotokoller, dns-og-dhcp, serverroller | ✅ |
|| km-06 | Dokumentasjon | dokumentasjon-og-planlegging | ✅ |
|| km-07 | Trusler | trusselbildet | ✅ |
|| km-08 | Risikoanalyse | risikoanalyse | ✅ |
|| km-09 | Automatisering | automatisering, bash-grunnleggende, powershell-grunnleggende | ✅ |
|| km-10 | Sikkerhet | brannmur, it-losninger-med-sikkerhet, kryptering | ✅ |
|| km-11 | Personvern | personvern | ✅ |
|| km-12 | Bærekraft | baerekraft | ✅ |

*## 12/12 kompetansemål dekket ✅

## Status per emne

### Video (YouTube/NDLA)

|| Emne | Video | Kommentar |
|| ------ | ------- | ----------- |
|| Backup og gjenoppretting | ✅ |  |
|| Bærekraft | ✅ |  |
|| Driftsarkitektur | ✅ |  |
|| Skytjenester | ✅ | NDLA-ressurs |
|| DNS og DHCP | ✅ |  |
|| Nettverksprotokoller | ✅ |  |
|| OSI-modellen | ✅ |  |
|| Segmentering og VLAN | ✅ |  |
|| Serverroller | ✅ |  |
|| TCP/IP-modellen | ✅ |  |
|| Virtuelle løsninger | ✅ |  |
|| Brannmur | ✅ |  |
|| IT-løsninger med sikkerhet | ✅ |  |
|| Kryptering | ✅ |  |
|| Personvern | ✅ |  |
|| Bash | ✅ |  |
|| PowerShell | ✅ |  |
|| **Mangler video:**SQL, dokumentasjon, Active Directory, brukerstyring, filsystem, Linux, risikoanalyse, trusselbildet, automatisering | ❌ 9 stk | Trenger YouTube/NDLA |

### Tospråklig

|| Status | Antall |
|| -------- | -------- |
|| Kun norsk | 27/27 |
|| Engelsk versjon | **0/27**❌ |

### Inline kildehenvisning

|| Status | Antall |
|| -------- | -------- |
|| Med fotnoter i brødtekst | **0/27**❌ |
|| Kun i frontmatter | 27/27 |

### NotebookLM

|| Kategori | Notebook ID | Artifacts |
|| ---------- | ------------ | ----------- |
|| Nettverk | f7e5ad6c... | 1 video, 1 infographic, 2 flashcards, 2 reports |
|| IT-drift | bc9a5656... | ✅ Eksisterer |
|| Skripting | 15678f10... | ✅ Eksisterer |
|| Databaser | e9134332... | ✅ Eksisterer |
|| Operativsystem | 70aa7fff... | ✅ Eksisterer |
|| Sikkerhet | 3e72e53a... | ✅ Eksisterer |

**Mangler:**Audio Overviews (podcast) i ALLE notebooks ❌

## TTS (taleopplesning)

✅ Implementert via TTSBar.astro — Web Speech API, norsk stemme, hastighetskontroll.

## Hull som må fylles

1.**🌐 Engelsk versjon**av alle 27 emner
2.**🎧 NotebookLM Audio Overviews**for alle 6 kategorier (både norsk og engelsk)
3.**📹 Video til 9 emner**som mangler
4.**📝 Inline kildehenvisning**i alle emner
5.**🃏 Interaktive flashcards**— Astro-komponent eller NotebookLM
6.**🔗 Brobygging til oppgaver-for-2IT**
7.**🔌 Astro-plugins**— vurder @astrojs/mdx, astro-embed-youtube, astro-expressive-code

## Anbefalt rekkefølge

1. ✅ Kartlegging (denne filen)
2. 📋 Finn og verifiser eksterne kilder per emne
3. 📋 Oversett alt innhold til engelsk
4. 📋 Legg til inline kildehenvisning
5. 📋 Generér NotebookLM Audio Overviews
6. 📋 Lag flashcards + videoinnhold
7. 📋 Bygg bro til oppgaver-for-2IT
8. 📋 Pedagogisk kvalitetssikring
