# Reusable prompt for authoring with template.cls

Copy the prompt below into a new model session together with the class and its supporting files. `main.tex` is the complete multifile example; `template-needs.md` explains the interface, `template-api.json` is its machine-readable index, and `../CHANGELOG.md` records changes.

## Prompt

Create a Hebrew/English preliminary report using the supplied `template.cls` version 1.1. Read the class, the API index and the existing example before writing. Use supported commands; do not invent macros or claim to have compiled a document without a successful build.

Inputs I will supply: topic, audience, approved research question, authors' Hebrew and English names, institution, course, semester, lecturer, submission date, chapter outline and verifiable source material. If a required input is unavailable, leave a clearly identified draft placeholder and report it to me; do not invent personal details, citations, empirical results or funding approval.

Deliver `main.tex`, one source file per chapter under `chapters/`, a checked `references.bib`, and original code-generated figures under `figures/`. Keep design rules in the class. Keep the original bundled `fonts/` directory and OFL license files. No system font installation is required. The existing copyright line is 2026: review it explicitly if preparing a document for another year.

Use `\en{...}` for short English strings within Hebrew and isolate entire numeric/reference ranges with `\LR{...}`. Use `keybox` for an unbroken highlighted block, and `reportconstraints` for a compact list of related constraints. Avoid simulated Hebrew italic. Use explicit table column widths at readable font sizes: table-width warnings must be fixed in the chapter, not hidden by scaling.

Use the title/author commands in the example below. Set short running titles for the new topic using `\runningtitles`. Put the abstract in `executivesummary`, followed by `\keywords`. Put abbreviations in `abbreviations` with one `\abbr{term}{definition}` per row. Figures need captions below, tables captions above; every figure/table must be referenced and discussed in the text. Cite only sources that actually support the relevant statements and distinguish full-text evidence from metadata/abstract-only checks.

Build with LuaLaTeX, Biber, then LuaLaTeX twice, or use `build.ps1`. Check logs for missing references/glyphs, overflow and wide tables. Render and inspect the pages, especially the cover, mixed-direction text, tables, reference ranges, bibliography and page endings. Correct and rebuild as needed. Preserve separate front-matter and body numbering. Report the actual page count, performed checks and unresolved limitations. Do not mark human approval or submission as completed unless I confirm it. Update the README and changelog when the interface or design changes.

## Minimal example of supported syntax

```latex
\documentclass{template}
\addbibresource{references.bib}
\reporttitle{כותרת הדוח}{Report title}
\reportsubtitle{כותרת משנה}{Report subtitle}
\reporttype{דוח מכין}{Preliminary Report}
\institution{שם המוסד}{Institution name}
\course{שם הקורס}
\semester{הסמסטר}
\authors[English Name One \and English Name Two]{שם ראשון \and שם שני}
\lecturer{שם המרצה}
\submissiondate{24.11.2026}
\runningtitles{כותרת קצרה}{Short title}
\begin{document}
\frontmatter
\makecoverpage
\begin{executivesummary}
כאן ייכתב התקציר לפי ההיקף הנדרש.
\end{executivesummary}
\keywords{מונח ראשון; מונח שני}
\tableofcontents
\listoffigures
\listoftables
\begin{abbreviations}
\abbr{\en{AI}}{בינה מלאכותית}
\end{abbreviations}
\mainmatter
\chapter{מבוא}
טקסט בעברית עם \en{English} וטווח \LR{312--843}.
\begin{keybox}{נקודה מרכזית}
תוכן קצר ומבוסס.
\end{keybox}
\begin{reportconstraints}
\item אילוץ זמן.
\item אילוץ משאבים.
\end{reportconstraints}
\printbibliography
\end{document}
```

The example demonstrates syntax only. A real report must supply its actual evidence, citations and assignment-specific content; it is not a completed deliverable.
