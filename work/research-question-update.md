# Research-question PDF update

Date: 2026-11-21. Based on Liron's commit `1706d2131b812986f87cf23b862024661a175ace`.

- Preserved the revised question in chapter 2, the updated abstract and README, and Liron's updated XLSX workbook.
- Existing hypotheses and chapter 5's two exploratory candidate models remain consistent with the revised association-focused question and its institutional-integration comparison. No new empirical result or causal claim was added.
- The first rebuild placed the last constraint bullet alone on another page. Added the reusable `reportconstraints` list environment in the class and used it for this list; changed list spacing only, with the same body font size and all original constraint text.
- Rebuilt with LuaLaTeX/Biber and resolved references. Final logs have no warnings, overflows, missing glyphs or wide-table warnings.
- Final count: 48 PDF pages, seven preliminary and 41 numbered, including references. Abstract: 296 whitespace-delimited words after relevant formatting commands are removed; it remains on one page.
- Rechecked all 36 citation keys, 73 unique labels and 26 text-referenced figures/tables. Both PDF extractors preserve Hebrew characters and punctuation without U+F8FF/U+FFFD substitution or literal double hyphens.
- Visually inspected the updated abstract, question and following pages, the now-complete constraint list, the next chapter opening and the conclusion's closing box.

This is an incremental build/layout check. The three prior independent reviews retain their original scope and PDF identifiers; no claim is made that all three were rerun for this wording update. Author reading, external-reader comprehension, self-grade and submission remain human tasks.

Final PDF SHA-256: `d5ad179a876b74d3e961e7b634b2ca8f1b0e51e1a232f29cb932a6402d991417`.
