# Independent structure and requirements review

Reviewer: `structure_reviewer`, a separate review agent. Date: 2026-11-21. Starting source revision: `f04cd64`; the lead author is integrating changes concurrently. This reviewer did not edit chapter content, charts, the bibliography, or the template. Findings below record the issues found before the lead's corrections; disposition belongs in the lead's response log.

## Scope and evidence

Read the chapter sources, decision/risk/Gantt constants in `code/make_figures.py`, the submission checklist, and the relevant course extracts. The course evidence checked was L03 PDF page 35 (assignment description), L04 PDF pages 30–31 (scope and recommended workflow), and the preparation-report book PDF pages 18 and 46–48 (page allocation, formatting/writing, and seven-item checklist). External historical source verification is assigned to the source reviewer. Final page allocation is pending the lead's rebuilt PDF; the copied repository PDF is not treated as current.

## Findings for lead-author correction

### S1 — Medium: map both hypotheses to an explicit analysis, without treating a null result as proof

Initial locations: `chapters/02-problem.tex`, hypothesis paragraph around line 63; `chapters/05-alternatives.tex`, statistical plan around lines 165–169.

The initial H1 concerned the predictive contribution of Christianization after alternative explanations, but the proposed model listed institutional integration, one control, and state indicators, not Christianization. It therefore did not describe a test of H1. The initial chapter 2 also linked rejection of H2 to possible correctness of Gibbon, and rejection of H1 to causal religious influence, neither of which follows from this small observational comparison.

Suggested correction: separately specify an H1 model with the Christianization predictor and an H2 model with integration, the same prespecified control and regional indicators; require enough variation and coverage before fitting. State that failure to reject a null is not proof of no effect and an observational association is not causal identification. For a count outcome measured over unequal partial intervals, explicitly define exposure and an offset if that model is retained.

### S2 — Medium: resolve the schedule's overlapping prerequisites and quality gate

Initial locations: `chapters/06-workplan.tex`, task table around lines 90–104 and critical-path paragraph around line 116; `code/make_figures.py`, TASKS.

The consistency rerun 3.4 occurs in month 8, but accepted-database task 4.1 depends only on 2.2 and 3.3. Analysis could therefore start after 4.1 without task 3.4 passing REQ-AI-02. Add that gate to the accepted database/analysis prerequisites.

The table also overlaps tasks with their prerequisites: 1.2 starts in month 1 while 1.1 occupies month 1; 1.3 starts in month 2 while 1.2 lasts through month 2; 2.2 and 3.1 start in month 3 while 2.1 lasts through month 3; publication 5.3 starts in month 12 while final writing 5.2 lasts through month 12. Ordinary finish-to-start interpretation of the listed inclusive durations produces a 15-month chain, not 12. This does not invalidate a rolling research schedule, but its handover semantics must be explicit.

Suggested correction: define rolling batch handovers and within-month approval milestones, identify which endpoints are true gates, and describe the red chain as a planning dependency chain rather than a computed zero-float CPM unless that calculation is actually supplied. Keep textual task rows and chart markers consistent. Publication is part of the final endpoint, so a sequential publication step cannot simply be assumed to have unlimited slack.

### S3 — Medium: verify the full population for the 100% provenance requirement

Initial location: `chapters/02-problem.tex`, REQ-DATA-02 around line 118.

The target is a source for 100% of values, but the listed verification was only a sample audit. Sampling checks source accuracy, not the presence of a source on every row.

Suggested correction: automatically check every value for a valid source identifier/link and complete required metadata, then perform a separate sample audit of whether the source supports the value. Both checks serve different purposes.

### S4 — Medium: define exactly what 85% classification agreement means

Initial locations: REQ-AI-01 in chapter 2 around line 120; chapter 5 validation section around lines 156–160.

The model assigns categories such as officeholding, religious legislation and conflict, potentially as multiple labels on a passage. "85% agreement" did not specify whether the denominator was passages, individual binary labels, or an average across categories. Those alternatives produce different acceptance results, especially for rare categories.

Suggested correction: define one prespecified primary passage-level measure, its denominator and treatment of abstentions/unknown labels. Keep the per-category and per-region diagnostics, with rare-class errors visible. The separated development and sealed test samples are a strong existing feature and should remain separate even after a failed test.

### S5 — Medium: avoid duplicate historical events and shared-source pseudo-replication

Initial locations: chapter 2 case table and period counts (312–476 West, 312–610 East), chapter 5 pipeline item "database" and validation split.

The two Roman trajectories share rulers, events and sources during parts of the comparison, particularly before the report's own 395 division landmark. They cannot automatically count as independent state replications. The pipeline initially summed classifications without a stated rule for distinguishing repeated mentions of the same council, rebellion or official from separate events. A prolific surviving author or parallel chronicles could inflate the measured institutional activity.

Suggested correction: call the Roman cases regional trajectories where appropriate; use one event registry with stable event ID, date/uncertainty, territorial scope and multiple supporting source IDs. Count each event once within the defined regional exposure, flag shared events, and avoid treating duplicated mentions as independent evidence. For test leakage prevention, group by the underlying original work, including its translations and editions; alternate editions of the same work must not cross development/test boundaries.

## Checks that passed

- 36 bibliography keys are cited and no cited key is missing. No unused bibliography entries were found. This is a wiring check, not confirmation that every historical claim is supported.
- 73 unique labels; no duplicate labels and no unresolved `ref`/`pageref` targets.
- All 26 figure/table objects have text references.
- The variable table lists 12 measures: four stability, four integration, one Christianization, three controls.
- The proposed 25-year intervals sum to approximately 34 (7 + 12 + 15), with partial intervals requiring an explicit exposure rule.
- Decision weights sum to 1.00 and scores recompute as 2.60, 3.65 and 4.40. Analytic B/C crossover is 0.60; first losing 0.01 grid point is 0.61.
- The seeded sensitivity result is transparently reported as 9,960 / 38 / 2 wins rather than implying that only two alternatives won.
- Risk products before mitigation are 16, 15, 12, 12, 8 and 6; exactly four meet the stated critical threshold. Residual products are 9, 6, 4, 4, 3 and 4. Every initial critical risk has both prevention and fallback actions. They are now described as planning estimates, not observed reductions.
- Approved budget arithmetic is correct: 96,300 NIS subtotal; 14,445 reserve; 110,745 economic total; 22,425 cash including reserve when researcher time is donated. These remain hypothetical planning assumptions; approval is not a claim that research expenditures occurred.
- The report correctly plans research rather than claiming that its corpus, expert validation or historical experiment has already been performed.
- The chapter-per-file structure, CLS separation, original code-based figures, bibliography, named requirements, alternative comparison, WBS/RACI/Gantt and risk register cover the main requested report components.

## Requirement interpretation and human completion

The book's chapter page allocation is a recommended balance, not an instruction to pad or cut a sound report to identical chapter boundaries. L04 asks for approximately 40 report pages. L03 explicitly mentions multiple checking agents; L04 calls the expert-committee workflow recommended. The actual separate-agent reviews in this milestone satisfy the stricter reading without falsely claiming that earlier single-session checks were independent agents.

Preserve the following as pending until the people actually perform them: both authors' final readable-size page review, an outside reader's explanation of the abstract, the shared self-grade, personal details in the submission form, and submission itself. The user has approved the budget assumptions and the revised 1.1 title; these should no longer be marked as awaiting the authors' decision.

## Verification after lead-author corrections

The rebuilt candidate received from the lead contains 48 PDF pages and 41 numbered pages including references. Its abstract is PDF page 2, body starts on PDF page 8, and chapter 8 is PDF page 45 (printed 38). Chapter 8 and bibliography now begin on consecutive pages, so the previous extra conclusion-box page is not present in this candidate. Detailed visible layout remains the typography reviewer's responsibility.

| Item | Verified disposition in current source |
|---|---|
| S1 | Corrected: chapter 2 no longer draws invalid causal or Gibbon conclusions; chapter 5 specifies separate H1/H2 predictors with common controls, regional indicators and log-exposure offset, and declines a claimed test when variation/coverage is insufficient. |
| S2 | Corrected: 4.1 now requires 2.2 and 3.4; 3.4 and 5.3 are marked critical in both the source table and Python TASKS. New text defines rolling batch handovers and within-month gates and explicitly disclaims a full CPM. The red chain is described as estimated. |
| S3 | Corrected: REQ-DATA-02 requires a full field-presence check plus sample content review; chapter 5 excludes undocumented values from approved data. |
| S4 | Corrected: primary agreement is exact-match of the complete label vector on all 300 passages. Abstention is an explicit label and separately reported; difficult passages cannot be silently removed. |
| S5 | Corrected: chapter 2 identifies Roman regional trajectories and shared-event dependence; chapter 5 adds stable event IDs, territorial scope, multiple sources, and original-work grouping across editions/translations. |

Two low-priority wording details can be aligned when the chart is regenerated: its legend still says “נתיב קריטי” whereas the caption and paragraph now say estimated dependency chain; and the assertion that other tasks “can move slightly without delaying the schedule” should be an explicit planning assumption because no slack/CPM calculation is supplied. Neither changes the accepted budget or the approved 1.1 title.

### Current chapter allocation

Derived from PDF bookmark destinations and printed page labels, not estimated from source length.

| Part | Printed pages | Actual count | Book's recommended count |
|---|---|---:|---:|
| Front matter, including cover | Seven PDF pages | 7 | 4 |
| 1 Introduction | 1–3 | 3 | 3 |
| 2 Problem and objectives | 4–7 | 4 | 4 |
| 3 Literature and flagship | 8–15 | 8 | 9 |
| 4 Tools and market | 16–21 | 6 | 6 |
| 5 Alternatives and method | 22–29 | 8 | 8 |
| 6 Work plan and budget | 30–34 | 5 | 4 |
| 7 Risks | 35–37 | 3 | 2 |
| 8 Conclusion | 38 | 1 | 1 |
| References | 39–41 | 3 | 3 |

The body-plus-references total of 41 is consistent with the assignment's approximately 40-page requirement. The distribution differs modestly from the handbook: the literature has one fewer page, while the costed work plan and risks have one more each. This is a reasonable adaptation; padding literature or reducing readable text solely to imitate the allocation is not warranted. The seven-page front matter is longer than the recommended four-page outline and should be reported honestly rather than described as an exact reproduction of that outline.

No unresolved structural finding rises to the level of blocking this preliminary-report milestone after the corrections above. Human final reading, outside-reader comprehension and self-grade remain pending human tasks.

### Final source follow-up

Verified the two low-priority residual wording corrections in the saved sources: `code/make_figures.py` line 290 now labels the red chart chain “שרשרת משוערת”; `chapters/06-workplan.tex` line 118 explicitly calls flexibility an assumption, says its extent has not yet been calculated, and requires changes to be evaluated against handover dates. These resolve the remaining source-level schedule wording concerns. The 48-total/41-numbered allocation above describes the reviewed candidate; final-build pagination should be confirmed by the lead. Human completion items remain pending.
