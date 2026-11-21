# Follow-up to Liron's template review

2026-11-21. Original review: `template-review.md`. Starting commit: `e208f20`.

| Review item | Disposition |
|---|---|
| 1–5: dashes, abbreviation alignment, orphan headings, requirement IDs, Biber dates | Liron's fixes retained. Rebuilt and checked again with Noto. |
| 6: float placement | Applied top/bottom/text/float-page fractions 0.85 / 0.6 / 0.1 / 0.75. Reinspect the new page locations rather than assuming the old page numbers still apply. |
| 7: silent table shrinking | Removed scaling. Tables are measured at their actual font size. A wide-table warning now fails `build.ps1`. Fixed source column widths in chapters 2 and 3. |
| 8: Hebrew nun extraction | Both PDF extractors preserve nun and Hebrew punctuation, with no U+F8FF substitutions. Noto replaces the previous system-font dependency. |
| 9: simulated Hebrew italic | Removed FakeSlant. Hebrew emphasis uses upright bold; English has actual italic font files. |
| 10: generated PDF in Git | Commit a PDF at the reviewed milestone only. Intermediate builds stay in a temporary workspace. |
| Font decision | User selected Noto Sans Hebrew with Noto Sans. Regular width for body; 75% width bold Hebrew headings. Fonts and OFL licenses bundled in `fonts/`. |

## Content work in chapters 4–7

- Removed unsupported market/database totals and recorded the evidence in `source-audit.md`.
- Added source-access and per-case corpus feasibility checks.
- Separated 150 development passages from a sealed 300-passage final test; no tuning on the final test set.
- Distinguished text count from the roughly 34 state-period observations, and limited statistical and causal claims.
- Added a costed resource plan with explicit hypothetical rates and spending controls.
- Corrected the sensitivity percentages and clarified the crossover.
- Kept 25-year coverage requirements intact when using 50-year sensitivity checks; scope reductions need a documented decision.
- Treated residual risk scores as planning estimates, not accomplished reductions.

## Checks and remaining joint decisions

Three separate checks are recorded: typography/text extraction, references/evidence, and page layout. They were performed in one assistant session, not by independent subagents. The lecture describes an agent committee as recommended rather than mandatory; this repository must not claim a committee ran without evidence.

Liron's historical narrative has not been rewritten. Only necessary table-width edits were made in chapters 2 and 3. Before submission, both authors should review the abstract and conclusion against the revised method, qualify universal novelty/causality claims in the historical chapters, agree the hypothetical budget, and complete the submission form and self-grade. No research, human validation, or model-classification experiment has been performed for this preliminary report.

Final validation: 47 PDF pages, 7 front-matter pages and 40 numbered pages including references. All 36 citation keys and 73 labels resolve. LaTeX/Biber logs have no warnings, overflows or missing characters. Every page was rendered and its layout reviewed; detailed checks included the cover, abbreviations, requirement identifiers, literature matrix, graphs, validation plan, budget, summary callout and bibliography. Keyboxes use 11-point text with 1.15 spacing; body text remains 12-point with 1.5 spacing. The final summary box now stays on the summary page.


## עדכון לאחר שלוש ביקורות נפרדות

המצב שתואר לעיל כבדיקות בשיחה אחת הוא היסטורי. בסבב הנוכחי הופעלו בפועל שלושה סוכני משנה נפרדים ונשמרו הוראותיהם וממצאיהם ב־`agents/`. הסוכן הראשי תיקן את הממצאים וקיבל אימות חוזר. `agents/resolution.md` ו־`submission-checklist.md` הם התיעוד העדכני. התקציב וכותרת 1.1 אושרו על ידי המחברים; קריאה אנושית, קורא חיצוני וציון עצמי לא אושרו במקום המחברים.
