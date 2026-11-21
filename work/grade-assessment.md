# Grade assessment – Assignment 2 (preliminary report)

Prepared by Claude for Liron Ben Yosef and Yonatan Kliger, 21.11.2026.
Assessed version: commit `790f4b3` / `fb48565`, `main.pdf` with 48 pages.

**This is advice, not the grade.** The self-assessed grade in the submission file is the authors' decision.

## 1. What the assessment is based on

Only the instructions the team received:

| Source | What it sets |
|---|---|
| Lesson 4 summary, section 9 (Table 9) | About 40 pages; pairs; a project with a main file and a `.tex` file per chapter; graphs generated in Python; no copyrighted images, with code-drawn figures (TikZ) preferred; originality ("not the model's default"); a professional, book-style report with a CLS template, figures, heading levels and graphs |
| Lesson 4, sections 9.3–9.5 | The booklet as a "tender document" that every requirement must answer; an agent committee (recommended, not required; three agents are enough); "think big"; tell the story of a project someone would want to fund |
| Lesson 3 summary, section 17 | GitHub with all sections, a README and the final files; correct Hebrew–English text; real sources; several checking agents, each checking something different; the self-assessment field, where overestimating counts against you and initiative is rewarded |
| Booklet "מהבעיה אל ה-PDF", Part A | The page map (Table 1.1), the content of each chapter, the 7-item pre-submission checklist and the "ten things to remember" |
| Booklet, Part B | The template checklist (6 items), the nine families of checks (Table 19.1) and the 6-item sign-off list (section 19.5) |

**No official rubric with point weights was published.** The weights in section 4 are my own. I based them on what the instructions stress: the page map puts most of the weight on literature, market and alternatives; lesson 4 stresses the LaTeX project, graphs and originality; lesson 3 stresses GitHub and the checking agents.

**Conflict of interest.** I wrote the first drafts of most chapters, so I'm likely to be generous about the content. Section 5 corrects for this.

## 2. The booklet's checklists, item by item

### Pre-submission checklist (booklet, Part A)

| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | Summary is the required length, with keywords under it | ✅ | 296 words (250–350); 7 keywords |
| 2 | Every requirement has a target value and a verification method | ✅ | Table 2.3, seven requirements |
| 3 | Flagship paper analyzed; knowledge gap in one sentence | ✅ | Sections 3.11–3.12; the box at the end of chapter 3 |
| 4 | Decision-matrix weights add up to 1.0 | ✅ | 0.30 + 0.20 + 0.20 + 0.15 + 0.15 = 1.00 |
| 5 | Every critical risk has a prevention step and a contingency plan | ✅ | Table 7.2, R1–R4, threshold R ≥ 12 |
| 6 | Every figure and table is mentioned in the text | ✅ | All 26 are mentioned |
| 7 | Every source in the list is cited, and every citation is in the list | ✅ | 36/36 |

### Sign-off list (booklet, section 19.5)

| # | Item | Result | Note |
|---|---|---|---|
| 1 | Zero compile errors, no unresolved references | ✅ | Clean build log |
| 2 | No reversed Hebrew, no text outside the margins | ✅ | Checked by the typography agent and by `build.ps1` |
| 3 | Tables aligned, all images appear | ✅ | |
| 4 | **Every source checked and read** | 🟨 Partly | Every source was checked to exist with correct details, and each claim was checked against it. Not every book was read in full. The report says so honestly, which is the right call, but the item is not fully met. |
| 5 | You went over every page yourselves | ✅ | Confirmed by the authors |
| 6 | Another person read the summary and understood it | ✅ | Confirmed by the authors |

### Page map (booklet, Table 1.1) compared with the PDF

| Part | Booklet | Report | |
|---|---|---|---|
| Front matter | 4 | 7 | Larger because of the lists of figures and tables and the abbreviations page. The booklet calls these parts "front matter" too, so this is fine. |
| 1 Introduction | 3 | 3 | ✅ |
| 2 Problem and goals | 4 | 4 | ✅ |
| 3 Literature and flagship paper | 9 | 8 | ✅ (−1) |
| 4 Market research | 6 | 6 | ✅ |
| 5 Design alternatives | 8 | 8 | ✅ |
| 6 Work plan | 4 | 5 | ✅ (+1) |
| 7 Risks | 2 | 3 | ✅ (+1) |
| 8 Summary | 1 | 1 | ✅ |
| **Numbered body** | **about 40** | **41 (38 + 3 of references)** | ✅ |

The balance matches the booklet's main point: most of the weight is in literature, market and alternatives (22 of 38 body pages), not in the introduction.

## 3. Lesson-by-lesson requirements

| Requirement | Result | Evidence |
|---|---|---|
| About 40 pages | ✅ | 41 numbered pages |
| Pairs | ✅ | Liron and Yonatan |
| Main file plus a `.tex` per chapter | ✅ | `main.tex` and `chapters/00–08` |
| Your own CLS template | ✅ | `template.cls` v1.0, with dark red, purple and cream and bundled Noto fonts |
| Graphs generated in Python | ✅ | Six graphs from `code/make_figures.py`: radar, scatter, decision matrix, sensitivity, Gantt and risk matrix |
| Figures in code, no copyrighted images | ✅ | Six TikZ figures plus the arches on the cover; no outside images |
| Originality, not the model's default | ✅ | The palette, cover and fonts were the authors' choices (font option 2 was chosen over the alternative) |
| Correct Hebrew–English | ✅ | `\en`/`\LR` used throughout, plus a dedicated typography review |
| Real sources | ✅ | 36 sources, each checked to exist; see `work/source-audit.md` |
| Several checking agents, each checking something different | ✅ | Three separate sub-agents (sources, structure, typography), with instructions, findings and fixes in `work/agents/` |
| GitHub with everything, README, final files | ✅ | |
| "Think big" | 🟨 | See weakness 2 |

## 4. Scoring by category

| Category | Weight | Score | Reasoning |
|---|---|---|---|
| A. Completeness and structure under Part A | 20 | 19 | Every chapter and front-matter part is present and close to the page map. −1: the authors' names appear on the cover in Hebrew only; the booklet's cover anatomy lists the names in both languages. |
| B. Content quality | 30 | 26 | Strong: measurable research question and hypotheses, including H0; seven requirements, each with a target and a verification method; a thematic literature review with a literature matrix; a flagship paper with three stated limitations; three genuinely different alternatives with weights set before scoring and a sensitivity analysis; WBS, RACI, Gantt, critical path and milestones; scored risks with a before/after matrix. −2: market size is described in three layers (TAM/SAM/SOM), but the numbers were removed because they couldn't be verified, so the chapter gives no market volume. −1: the "think big" vision is modest. −1: the many hedges added after the review make some passages dry, and the booklet asks for a story someone would want to fund. |
| C. Sources and integrity | 10 | 9 | 36 real, cited sources and an honest statement of how they were checked. −1: sign-off item 4 is only partly met, because the books were not read in full. |
| D. The LaTeX project and template | 15 | 14 | The CLS has a version, there is a build script that stops on errors or wide tables, the fonts are licensed, and recurring problems were fixed in the template rather than in the text, as the booklet's rule 9 asks. −1: two items from the template checklist are missing: a changelog, and a prompt file that would let a new model write another document from the template. |
| E. Figures and graphs | 10 | 10 | Six Python graphs and six TikZ figures, each one answering a question. Hebrew in the graphs renders correctly. |
| F. Originality of design | 5 | 5 | Your own design, not a default. |
| G. Process, documentation and initiative | 10 | 9 | Separate agents, documented resolutions, a log of author decisions, a budget calculator with formulas, and a README with a statement on AI use. Initiative rewarded under lesson 3: a sealed 300-passage test set, a check with random weights, and pooling rules for events shared between East and West. −1: GitHub history shows commits by Claude and Yonatan only. Liron's work went in through Claude's commits, so her own contribution isn't visible in the history. One line in the README would fix this. |
| **Total** | **100** | **92** | |

## 5. Recommendation for the self-assessed grade

- **My estimate: 92.**
- **Reasonable range: 88–93.**
- **Recommended self-grade: 90.**

Why 90 and not 92:
1. **The lesson 3 rule.** A grade that is too high counts against you, while a modest grade that the grader then raises doesn't hurt.
2. **My conflict of interest.** I wrote much of the content, so I take two points off my own content scores.
3. **Uncertainty about the grader's priorities.** The missing market volume and the modest vision depend on the grader's taste. One grader may count them as one point, another as three.

If you fix the quick items in section 6 before Tuesday, I'd consider 91–92 justified.

## 6. What could still raise the grade before submission (quick fixes, in order of value)

1. **The authors' names in English on the cover.** Add the English names to `\authors` (5 minutes, Yonatan).
2. **A line on contributions in the README.** For example, "Liron: chapters 1–3, 8 and the summary, through Claude; Yonatan: the template and chapters 4–7." This makes Liron's work visible in the repo (5 minutes).
3. **A changelog and a prompt file for the template.** A short `CHANGELOG` and `work/template-prompt.md`; this closes two items on the template checklist (20 minutes).
4. **Optional:** one paragraph in chapter 4 explaining why there is no market volume. It's a research project, not a product, and the market is defined by a "use" metric: the number of digital humanities projects and courses. This turns a gap into a deliberate decision.

## 7. Suggested wording for the self-assessment in the submission file

> **Self-assessed grade: 90.** The report meets all seven items of the booklet's pre-submission checklist and follows the page map closely (41 numbered pages). It is a full LaTeX project with our own template, six Python graphs and six TikZ figures, and 36 real sources. Three separate checking agents ran, and their findings and fixes are documented in the repository. Limitations: not every source was read in full (the report says so); market volume is not quantified, because no verifiable figure was found; and the scope of the vision is modest. That's why we chose 90 and not higher.
