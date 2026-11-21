# Independent typography and BiDi review

Reviewer role: typography/BiDi/layout. Date: 2026-11-21.

Reviewed candidate: `main.pdf`, 48 PDF pages, 7 preliminary pages and 41 numbered pages including references. Initial PDF SHA-256: `704878e13bd486631a671e215e0b001a5e6ce25328465c298216e1ed43b639f5`.

This reviewer did not edit the report. The lead author is responsible for applying and verifying corrections.

## T1 — Medium: isolate entire cross-reference ranges in left-to-right direction

- PDF page 15, printed page 8: the chapter 3 introductory paragraph displays section ranges as `3.4–3.1`, `3.6–3.5`, and `3.9–3.8`, although the intended ranges ascend from 3.1 to 3.4, 3.5 to 3.6, and 3.8 to 3.9.
- PDF page 45, printed page 38: the conclusion displays the chapter range visually as `3–2` instead of `2–3`.
- Source locations: `chapters/03-literature.tex`, introductory paragraph around line 12; `chapters/08-summary.tex`, first paragraph around line 10.
- Cause: the pattern `\ref{...}--\ref{...}` is placed directly in an RTL paragraph. The individual cross-reference numbers resolve correctly, but the whole range has no LTR isolation.
- Recommended correction: wrap the entire numeric range in `\LR{\ref{...}--\ref{...}}`, then rebuild and inspect those two pages. Isolating only the endpoints does not protect the range as one unit.

The lead author has acknowledged this finding. Final verification of the repaired ranges is pending the next build.

## Checks that passed in the reviewed candidate

- All six contact sheets were inspected, covering PDF pages 1–48. No blank accidental page, clipped page content, black-box glyphs, or visible overlapping table rows was found in that overview.
- Full-size page images were additionally inspected for PDF pages 1, 2, 7, 12, 14, 15, 21, 26, 27, 28, 31, 32, 33, 35, 38, 39, 40, 41, 43, 45, 46 and 48. This is an all-page overview plus detailed sampling, not a claim that every page was inspected at 100%.
- The cover preserves the selected dark red, purple and cream palette. Both title languages, the original arch illustration, authors and date fit inside the border.
- The executive summary and keyword list remain together on PDF page 2 (printed aleph).
- Abbreviation terms and definitions align correctly on PDF page 7. Hebrew and English strings remain legible.
- Requirement IDs in table 2.3 stay on one line. Table text is readable at the intended font size; no silent table scaling was observed.
- The literature matrix on PDF page 21 (printed 14) has readable wrapped column headings, distinct rows and intact checkmarks.
- The comparison table, radar, scatter plot, decision graph, sensitivity chart, architecture flow, RACI table, Gantt and risk matrix were inspected in detailed pages. Axis labels, legends, arrows and captions remain visible and separable.
- No isolated section or paragraph heading was found without following content in the examined pages. Chapter-ending whitespace was not treated as a defect by itself.
- The final conclusion and its closing keybox now fit together on PDF page 45 (printed 38). The lowest body text ends at approximately 762.6 pt from the top, while the footer text ends at approximately 803.8 pt, leaving about 41 pt separation. No footer collision was found.
- The bibliography is LTR and its URLs/DOIs fit the text block in the inspected pages.
- Both `pypdf` and PDFium extracted 1,625 occurrences of Hebrew nun, no U+F8FF substitute characters, no U+FFFD replacement characters, and no literal double-hyphen strings. Hebrew maqaf, gershayim and geresh were present. These extraction checks complement, rather than replace, the visual review.
- Visible year/date ranges such as 312–843 and task-month ranges were correctly ordered in the inspected pages. T1 concerns the unisolated cross-reference ranges specifically.

## Final repair verification

Pending the lead's repaired and rebuilt PDF. Recheck the three section ranges, the chapter 2–3 range, the conclusion keybox/footer gap, the abstract and any pages shifted by the final wording changes.

### Verification of repaired candidate

Verified the rebuilt candidate with SHA-256 `e63ed593eaec5df9b1cea522d4802de16e224fe0166248ac9b5efa402663f24b` against the newest `delivery/` images. It remains 48 PDF pages / 41 numbered pages.

- PDF page 15 / printed 8: the three cross-reference ranges now display in the correct ascending order: 3.1–3.4, 3.5–3.6 and 3.8–3.9.
- PDF page 45 / printed 38: the conclusion's chapter range now displays as 2–3. The final keybox remains on that same page, with body-text bottom approximately 762.6 pt and footer bottom approximately 803.8 pt; no collision was found.
- PDF page 2: the abstract and keywords remain on one page.
- PDF page 40 / printed 33: the Gantt legend now describes the red chain as estimated; labels, milestones and caption fit.
- PDF page 16 / printed 9 and bibliography page 47 / printed 40 were checked after the wording and metadata changes; no visible clipping or new overlap was found.
- Both extraction engines now return 1,623 nun characters, zero private-use characters, zero replacement characters and zero literal double-hyphen strings.

**Residual of T1 on the same inspected page:** the newly added Augustine locator in chapter 3's first section uses an unisolated literal `24–26`. It displays as `26–24` on PDF page 15 / printed 8. Wrap that locator in `\LR{24--26}` as well. The lead has been notified. The four original cross-reference-range instances are resolved; this new locator is the only remaining visual correction identified in the final narrow verification.

### Final T1 closure

Verified the newly rendered `delivery/locator-final-page-15.png` for the rebuilt PDF with SHA-256 `195658a03294affa2323a37cd66cc6b98cadbf522aa7df690bf3f6b3ebc7c64c`. The Augustine locator now visibly reads chapters **24–26** in ascending LTR order, followed by book XIX, chapter 17. The previously corrected section ranges remain correctly ordered on that page. **T1 is closed; no unresolved visual finding remains from this typography review.** No source edits were made by this reviewer.
