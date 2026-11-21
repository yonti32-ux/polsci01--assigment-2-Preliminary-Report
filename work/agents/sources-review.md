# Independent source review

Reviewer: source_reviewer, a separate Codex subagent. Date: 2026-11-21. Starting source version: `f04cd64`, with lead-author wording edits appearing during review. This reviewer did not edit chapters or bibliography. Findings below identify passages reviewed before correction; the lead records dispositions separately.

## Scope and limits

Reviewed all 36 bibliography records and the consequential cited claims in the chapter sources. Used publisher pages, journal records, author/institutional repositories, project documentation, and selected passages of primary historical texts. No entire modern historical book was read. Publisher abstracts verify an author's stated thesis, not every detailed assertion or the truth of that thesis. Access failures were not treated as evidence of a fabricated source.

## Findings for the lead author

### S1 — High: Augustine's position is reduced to absence of civic benefit

- Location: `chapters/03-literature.tex`, paragraph under `sec:lit-classic` (original line 18), key `augustine_citygod`.
- Problem: the sentence saying Augustine did not argue Christianity benefits the state, but separated the two spheres, is too categorical. It does not follow from his refusal to treat imperial success as a test of religious truth.
- Primary evidence: [City of God V.24–26](https://www.newadvent.org/fathers/120105.htm) discusses virtues and actions of Christian emperors; [XIX.17](https://www.newadvent.org/fathers/120119.htm) explains Christians' use of earthly peace and civic laws. The [Cambridge copyright/title page](https://assets.cambridge.org/97805214/68435/copyright/9780521468435_copyright_info.pdf) confirms the cited Dyson 1998 edition. The freely available passages use a different English translation, so cite book/chapter locators rather than inventing Dyson page numbers.
- Recommendation: retain the distinction between religious truth and worldly success; explicitly avoid concluding that Augustine denied Christianity any civic benefit or described a modern church/state separation.

### S2 — High: Gibbon is presented as having no account of the East

- Location: `chapters/03-literature.tex`, following paragraph in `sec:lit-classic` (original line 20), key `gibbon_decline`; introductory summaries should remain consistent.
- Problem: the assertion that Gibbon's thesis does not explain the Christian East overlooks his own discussion. His account was not simply that Christianity alone caused the Western collapse.
- Primary evidence: [Gibbon, chapter 38, General Observations](https://sourcebooks.fordham.edu/source/gibbon-fall.asp), especially its discussion of Constantinople and the qualified religion argument. He attributes some effect to Christianity or its abuse, while also describing unifying and moderating effects.
- Recommendation: say that a religion-only explanation would not explain divergent outcomes; acknowledge Gibbon's multi-causal and qualified discussion. Preserve critical comparison without attributing an argument he did not make.

### S3 — Medium: distinguish the Ithaca experiment from this classification task

- Location: `chapters/03-literature.tex`, `sec:lit-computational` (original lines 73–75), key `assael2022ithaca`.
- Primary evidence: [Nature article](https://www.nature.com/articles/s41586-022-04448-z) and [article PDF](https://www.nature.com/articles/s41586-022-04448-z.pdf). Bibliographic identity, year, authors, pages and DOI match the record. The approximate 62 / 25 / 72 percentages are supported, but concern restoration of missing character sequences in ancient Greek inscriptions in that evaluation.
- Recommendation: specify restoration accuracy and the experimental setting, and state that this motivates testing expert assistance rather than proves a general performance advantage for all ancient-text classification tasks. The report's own 85% classification target remains a proposed acceptance criterion, not a result inferred from Ithaca.

### S4 — Medium: Logion is not a second replication of the paired-human accuracy result

- Location: same computational-literature paragraph, key `graziosi2023philology`.
- Primary evidence: [Princeton's author publication record and abstract](https://collaborate.princeton.edu/en/publications/machine-learning-and-the-future-of-philology-a-case-study/) confirms TAPA 153(1), 253–284 (2023), authors and DOI. The work describes a philology case study involving Michael Psellos; it does not establish the same paired human-alone/model-alone/human-plus-model experiment as Ithaca in the available abstract.
- Recommendation: replace “a similar finding” with “another application/case study” unless a specific experiment and locator supporting the stronger statement are provided. Avoid the universal conclusion that combining a model and historian is always better than either alone.

### S5 — Medium: “equal weight” is stronger than the checked Harper evidence

- Location: `chapters/01-intro.tex`, modern-explanations paragraph (original line 37), and `chapters/03-literature.tex`, climate paragraph (original line 31), key `harper2017fate`.
- Evidence: [Princeton publisher description](https://press.princeton.edu/books/hardcover/9780691166834/the-fate-of-rome) and its [2017 catalogue](https://assets.press.princeton.edu/catalogs/F17Seasonal.pdf) support climate and disease as major contributors alongside human decisions. They do not quantify a 50/50 causal allocation.
- Recommendation: use “major factors alongside military, political and economic processes” or equivalent. Do not interpret “alongside” as equal measured weight. The exact dating of the cooling phase was not verified from a full book passage in this review.

### S6 — Low: complete Polaris metadata, but keep the journal's 2025 year

- Location: `references.bib`, key `francois2025polaris`.
- Primary evidence: [official journal PDF](https://escholarship.org/content/qt9wj6z91m/qt9wj6z91m.pdf), cover and printed first page. Repository cover dates it 2025-12-25; volume 16(2), printed pages 117–129. Full title: *The Polaris2025 Seshat Data Release: An Expanded Dataset for Cliodynamic Research*.
- Recommendation: optionally add subtitle, volume, number and pages. A Stanford author publication page lists 2026, and the PDF's internal suggested citation has an apparent “2015” typo, but neither is a reason to replace the journal-cover year with a guessed year. Current 2025 is defensible.

### S7 — Low: make the status of the cited Latin BERT version precise

- Location: `sec:lit-computational`, key `bamman2020latinbert`.
- Primary evidence: [author preprint](https://arxiv.org/abs/2009.10053) supports identity and training on 642.7 million Latin words.
- Recommendation: “the cited version is a preprint” is more precise than a claim that no version has ever passed peer review. No claim about all later publication history was verified here.

## Bibliography coverage register

“Identity checked” means title/author/publication match an authoritative source, not that the complete work or every cited passage was read. A whole-book reading should not be claimed for any of the following books.

| Key | Independent evidence and coverage |
|---|---|
| `augustine_citygod` | [Cambridge edition title/copyright page](https://assets.cambridge.org/97805214/68435/copyright/9780521468435_copyright_info.pdf); selected primary passages V.24–26 and XIX.17 checked separately. S1. |
| `gibbon_decline` | [Primary chapter 38 excerpt](https://sourcebooks.fordham.edu/source/gibbon-fall.asp); textual identity and argument checked, not a collation of all six original imprints. S2. |
| `heather2005fall` | [Author's institutional record](https://kclpure.kcl.ac.uk/portal/en/publications/the-fall-of-the-roman-empire-a-new-history-of-rome-and-the-barbar/) and publisher-prepared edition preview support identity; original and US edition years differ. Current bib explicitly distinguishes them. |
| `wardperkins2005fall` | Primary OUP product endpoint inaccessible in this pass. Identity is consistent with the existing author audit, but this reviewer did not independently verify every imprint field from an accessible primary page. |
| `harper2017fate` | [Princeton publisher page](https://press.princeton.edu/books/hardcover/9780691166834/the-fate-of-rome); author, book and broad thesis checked. S5. |
| `wickham2005framing` | [Oxford book record](https://academic.oup.com/book/27643) confirms 2005 and comparative regional scope. |
| `brown2012needle` | [Princeton book page](https://press.princeton.edu/books/paperback/9780691161778/through-the-eye-of-a-needle) confirms copyright 2012 and the challenge to the wealth-drain account; displayed paperback date is 2014. |
| `brown1961aspects` | [Cambridge journal record](https://www.cambridge.org/core/journals/journal-of-roman-studies/article/abs/aspects-of-the-christianization-of-the-roman-aristocracy/E613F00EDE9F7FE4DAB40E778E127312); identity checked, not full text. |
| `barnes1995statistics` | [Cambridge journal record/extract](https://www.cambridge.org/core/journals/journal-of-roman-studies/article/abs/statistics-and-the-conversion-of-the-roman-aristocracy/FF7EA8D2F9A1E42DDFE2842B6052D1C5); identity and engagement with Brown checked; complete quantitative argument not reread. |
| `salzman2002making` | Harvard endpoint inaccessible in this pass. Existing audit retained; this reviewer did not independently substantiate the exact 414-person/date-span claim from a primary full-text passage. Do not present this pass as such verification. |
| `whelan2018mirrors` | [Cambridge article](https://www.cambridge.org/core/journals/journal-of-roman-studies/article/abs/mirrors-for-bureaucrats-expectations-of-christian-officials-in-the-theodosian-empire/25C99A34791A030385289F5C343E5AD6); identity and rhetoric-of-office topic checked. |
| `whelan2026serving` | [Cambridge front matter](https://assets.cambridge.org/97810097/14709/frontmatter/9781009714709_frontmatter.pdf) confirms the 2026 book, author, open-access availability and stated focus on Christian officeholders. No fabrication concern. |
| `williams1999rome` | [Routledge book page](https://www.routledge.com/The-Rome-that-Did-Not-Fall-The-Survival-of-the-East-in-the-Fifth-Century/Friell-Williams/p/book/9780203982310); identity, 1999 copyright and Eastern survival topic checked. |
| `costambeys2011carolingian` | [Cambridge front matter](https://assets.cambridge.org/97805215/64946/frontmatter/9780521564946_frontmatter.pdf) confirms names, 2011 and ISBN. |
| `dejong2009penitential` | [Cambridge front matter](https://assets.cambridge.org/97805218/81524/frontmatter/9780521881524_frontmatter.pdf) and excerpt support Louis's 833 penance and religious-political accountability thesis. |
| `moore2011sacred` | [CUA Press book page](https://www.cuapress.org/9780813229621/a-sacred-kingdom/) confirms identity and episcopal models for Frankish kingship. Not a full reading. |
| `obrien2026rise` | [Oxford introduction](https://academic.oup.com/book/61836/chapter-abstract/546968304), [Merovingian chapter](https://academic.oup.com/book/61836/chapter-abstract/546969739), and [conclusion](https://academic.oup.com/book/61836/chapter-abstract/546971054) confirm 2026 title/DOI and a nuanced political-practice account. No fabrication concern. |
| `poveda2019clovis` | [Publisher article abstract](https://www.tandfonline.com/doi/abs/10.1080/13507486.2017.1397108?scroll=top&tab=permissions) and [author-institution manuscript](https://uvadoc.uva.es/bitstream/handle/10324/68324/05.%20Poveda_Clovis%20and%20Remigius%20of%20Reims%20in%20the%20making%20of%20the%20Merovingian%20Kingdoms.pdf?sequence=1) support territorial/diocesan argument. Online 2017 vs issue 2019 is not automatically a wrong citation. |
| `barrett2016remigius` | [Author-institution publication record](https://nottingham-repository.worktribe.com/person/1056096/george-woudhuysen/outputs?Organisation=Classics&Year=2016&page=1) and accepted manuscript confirm authors, 2016, 24:471–500 and DOI. |
| `nelson1971synods` | [Cambridge issue record](https://www.cambridge.org/core/journals/studies-in-church-history/volume/councils-and-assemblies/17F87FA560A41F0DFEF86E98B34C26E2) supports 1971 and 41–59. Some publisher catalogue indexes show 41–60; no silent page correction recommended. |
| `nelson1991bailiffs` | [Cambridge article record/extract](https://www.cambridge.org/core/journals/studies-in-church-history-subsidia/article/abs/not-bishops-bailiffs-but-lords-of-the-earth-charles-the-bald-and-the-problem-of-sovereignty/31B655FA3C723CFD29CBFBEFFAF4FA5D) confirms 9 (1991), 23–34; DOI 10.1017/S014304590000185X can be added. |
| `turchin2018quantitative` | [Author repository record](https://dash.harvard.edu/entities/publication/73120379-39d5-6bd4-e053-0100007fdf3b) confirms PNAS 115(2):E144–E151 and the 414-society/30-region scope. |
| `turchin2022disentangling` | [Oxford author-repository paper](https://ora.ox.ac.uk/objects/uuid%3Aa06cf552-439b-4891-afbd-1f13ec1ed21c/files/rxp68kg77w) supports identity, 17 predictors, >100,000 combinations, agricultural productivity and warfare mechanisms. The small proposed study should not claim equivalent causal identification. |
| `assael2022ithaca` | [Nature paper](https://www.nature.com/articles/s41586-022-04448-z) and PDF; bibliographic identity and restoration experiment checked. S3. |
| `sommerschield2023survey` | [ACL journal record](https://aclanthology.org/2023.cl-3.5/) confirms all named authors, 49(3):703–747 and DOI; task taxonomy supports broad literature description. |
| `graziosi2023philology` | [Princeton author record](https://collaborate.princeton.edu/en/publications/machine-learning-and-the-future-of-philology-a-case-study/) confirms TAPA 153(1):253–284 and DOI. S4. |
| `bamman2020latinbert` | [Author preprint](https://arxiv.org/abs/2009.10053) confirms names, 2020, identifier and 642.7-million-word training corpus. S7. |
| `fds2026dh` | [Commercial report page](https://www.futuredatastats.com/digital-humanities-market) checked. Its public content does not substantiate the removed dollar figures. Current explicit limitation is appropriate. |
| `seshat_web` | [Official data page](https://seshatdatabank.info/data) confirms Polaris-2026, snapshots, replication data and API. Current removal of unverified polity totals is appropriate. |
| `francois2025polaris` | [Journal PDF](https://escholarship.org/content/qt9wj6z91m/qt9wj6z91m.pdf); bibliographic details and release description checked. S6. |
| `scheidel2015orbis` | [Author SSRN record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2609654) confirms 2015 working paper, title, author and DOI. Its abstract supports modeled Roman travel cost/time, not a measured project-specific religion indicator. |
| `pleiades_web` | [Project website](https://pleiades.stoa.org/) confirms gazetteer, computational reuse and attribution license. Current record-count caution is appropriate. |
| `perseus_scaife` | Live viewer access was blocked; role checked through the project's own repository, below. Exact totals remain unverified and are correctly omitted. |
| `mgh_dmgh` | [Official indexed page](https://www.mgh.de/en/digital-mgh/dmgh) supports digitized editions and two-year moving wall. Direct fetch had an error; checked indexed primary text. |
| `mgh_openmgh` | [Official indexed page](https://www.mgh.de/en/digital-mgh/openmgh) supports TEI-XML and CC BY 4.0; successive availability should not be equated with guaranteed coverage of every desired item. |
| `scaife_repository` | [Project repository](https://github.com/scaife-viewer/scaife-viewer) confirms the Perseus reading environment and MIT software license. Software licensing is distinct from text/translation licensing, as the revised chapter states. |

## Correction recheck

After the lead's edits, this reviewer reread the revised Augustine/Gibbon paragraphs and the revised Ithaca/Logion discussion. S1–S4 are addressed: the historical arguments are now qualified, the restoration task is specified, and no universal superiority of human-plus-model is asserted. S5 was sent to the lead for the two remaining Harper phrases. S6–S7 are low-priority precision recommendations. This is a textual recheck, not a fresh review of a final PDF.

## Review conclusion

The review found concrete overstatements of primary historical arguments and overgeneralization of AI task results, rather than evidence that the cited 2026 books or flagship research were invented. See the correction recheck for the addressed items. The remaining access limitations above must remain visible; neither automated citation consistency nor this review constitutes complete reading of all 36 works.

## Final source-resolution check

After the lead's subsequent changes, this reviewer verified the actual shared chapter and bibliography files. S5 is addressed: both Harper passages now describe major environmental contributors alongside human processes, without equal-weight quantification; the unsupported precise cooling-start statement was removed. S6 is addressed: Polaris now includes the full title, volume 16, issue 2 and pages 117–129, retaining the journal-cover year 2025. S7 is addressed in both the chapter and bibliography: the cited Latin BERT version is described specifically as an arXiv preprint.

Together with the earlier textual recheck of S1–S4, all seven actionable findings from this review are resolved in the shared source files. The bibliography coverage register and its access limits remain unchanged. This resolution does not certify complete reading of inaccessible books, every historical assertion, or final PDF layout; those are separate coverage questions.
