# Template changelog

## 1.1 — 2026-11-21

- Added an optional English author line: `\authors[English names]{Hebrew names}`. The one-argument form remains supported.
- Added `\runningtitles{Hebrew short title}{English short title}` so another document can set its running headers without editing the class.
- Documented the supported interface in `work/template-api.json` and provided a reusable authoring prompt and minimal example in `work/template-prompt.md`.
- The current report now prints both authors' names in both languages.

## Earlier development — 2026-11-21

These are historical changes in Git, rather than invented release numbers:

- `f0c8a8b`: initial report class, original cover, palette, build script and chart colors.
- `b42ab3f`: TeX ligatures, abbreviation alignment, paragraph-heading protection and related source fixes.
- `c6f67bb`: bundled OFL Noto fonts, condensed headings, explicit table-width checks and float tuning.
- `4cbf42c`: corrections from three independent review agents, including isolated numeric reference ranges.
- `790f4b3`: rebuilt the revised research question and added `reportconstraints` to prevent an isolated constraint bullet.

The class deliberately centralizes styling. Content, author metadata and short running titles belong in the document source. Table widths belong in the relevant chapter; the class warns instead of silently shrinking table text.
