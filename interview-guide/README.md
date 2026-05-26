# Senior Android / Kotlin Interview Guide

> Quality status: **90/100, Near Ready**. Target: **95+**. This file is the navigation hub; chapter readiness is tracked in `17-chapter-scorecard.md`.

This folder is the working book structure for the Senior Android / Kotlin Developer interview guide.

The source format is Markdown first, then PDF/HTML export later. Markdown is easier to edit, review, version, split by chapter, and expand with research notes. Once the content stabilizes, export can be done with Pandoc, Quarto, or another Markdown publishing pipeline.

## Recommended Reading Order

1. `GUIDE-SPEC.md`
2. `STUDY-GUIDE.md`
3. `QUESTION-COVERAGE.md`
4. `SENIOR-ANSWER-AUDIT.md`
5. `QUESTION-BANK.md`
6. `MOCK-INTERVIEWS.md`
7. `FLASHCARDS.md`
8. `STUDY-AUDIT.md`
9. `02-kotlin-fundamentals.md`
10. `03-android-fundamentals.md`
11. `04-coroutines-flow.md`
12. `07-jetpack-compose.md`
13. `05-architecture.md`
14. `06-design-patterns.md`
15. `08-mobile-system-design.md`
16. `09-testing.md`
17. `10-performance-security-release.md`
18. `12-soft-skills.md`

Inside `STUDY-GUIDE.md`, every topic now ends with `Topic Drill Questions`. Study those first because they sit directly under the theory and strong answers. Use `QUESTION-BANK.md` later as the global/random review bank. `MOCK-INTERVIEWS.md` contains mixed timed rounds where every question has its answer directly underneath.

Internal/editorial files:

- `00-research-matrix.md`
- `01-book-format.md`
- `14-iteration-method.md`
- `15-failure-analysis.md`
- `16-quality-upgrade-plan.md`
- `17-chapter-scorecard.md`
- `references.md`

The existing root file `../senior-android-kotlin-interview-guide.md` remains the first full draft. This folder is the modular version that should grow into the final book.

## Final Book Shape

```text
interview-guide/
  README.md
  GUIDE-SPEC.md
  STUDY-GUIDE.md
  STUDY-AUDIT.md
  SENIOR-ANSWER-AUDIT.md
  QUESTION-COVERAGE.md
  QUESTION-BANK.md
  MOCK-INTERVIEWS.md
  FLASHCARDS.md
  00-research-matrix.md
  01-book-format.md
  02-kotlin-fundamentals.md
  03-android-fundamentals.md
  04-coroutines-flow.md
  05-architecture.md
  06-design-patterns.md
  07-jetpack-compose.md
  08-mobile-system-design.md
  09-testing.md
  10-performance-security-release.md
  11-project-deep-dives.md
  12-soft-skills.md
  13-mock-interviews.md
  14-iteration-method.md
  15-failure-analysis.md
  16-quality-upgrade-plan.md
  17-chapter-scorecard.md
  references.md
```

## Quality Standard

The target is not "complete enough." The target is 95-100/100 per chapter.

Before a chapter is considered interview-ready, it should satisfy the rubric in `16-quality-upgrade-plan.md`:

- clear structure,
- visible documentation anchors,
- forum/interview signals,
- drill chains with follow-ups,
- internals and edge cases,
- strong answers that sound natural and not memorized,
- weak answers to avoid,
- senior trade-offs,
- checklist or mini oral exam.

The monolithic root file is draft v1. The modular files are the source of truth.

## Chapter Format

Each chapter should use this rhythm:

1. Documentation anchors.
2. Forum/interview signals.
3. Theory.
4. Interview questions.
5. Asked as / variations.
6. Strong answer.
7. Follow-up answers.
8. Internals and edge cases.
9. What not to say.
10. Practice.

## Evidence Rule

Every major topic should be backed by at least one of:

- official Android/Kotlin documentation,
- public interview report,
- forum discussion,
- Glassdoor-style candidate report,
- known interview-prep source that names Android/Kotlin senior interview patterns,
- big-company mobile interview guide or candidate report.

When a topic is important but less directly reported, mark it as "architecture judgment" rather than pretending it is a frequently asked exact question.
