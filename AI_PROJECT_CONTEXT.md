# Driftsstøtte VG2 – AI Project Context & Architectural Memory

> **Agent Note:** Read this file to understand the critical design decisions and non-obvious context of the `driftsstotte-vg2` (Astro frontend) and `driftsstotte-vault` (Obsidian source) projects.

## 1. The Two-Repository Structure
This project is split into two parts:
1. **The Vault (`driftsstotte-vault`):** Serves as the single source of truth for all Markdown content. It is structured like an Obsidian vault.
2. **The Frontend (`driftsstotte-vg2`):** An Astro site that consumes the Vault's Markdown to build the static web pages.

## 2. Zero-Bloat Media Strategy (NotebookLM)
Per the user's explicit request, we **do not** store generated AI media (podcasts, flashcards, slide decks, infographics) locally in the repository to prevent content bloat.
Instead, we rely on Google NotebookLM:
- **Workflow:** The user uses `notebooklm-py` (CLI) running locally to upload sources and generate rich media artifacts.
- **Integration:** Markdown files use frontmatter flags (e.g., `flashcards: "https://notebooklm.google.com/..."`). The Astro components (specifically `AIFeatures.astro` and `ContentLayout.astro`) dynamically read these URLs and present styled link buttons to the students.
- **Mapping:** The course topics (`emne`) are strictly mapped to distinct NotebookLM Notebook UUIDs (see `src/data/notebooks.json`).

## 3. Competence Goals (`kompetansemaal`) Resolution
In the Markdown frontmatter, the competence goals are written in a shorthand tag format (e.g., `km-05`). 
You should **not** rewrite these to their full text inside the Markdown. 
Instead, the Astro framework dynamically parses these tags into human-readable sentences at build-time using the lookup dictionary located at `src/data/kompetansemaal.json`.

## 4. Link Philosophy
- All external links (like NDLA and NSM) are enforced to open in new tabs via `rehype-external-links` configured in `astro.config.mjs`.
- If links break in the future, use the Python script `check_links.py` in the vault to asynchronously scan all Markdown files before attempting to update them.
