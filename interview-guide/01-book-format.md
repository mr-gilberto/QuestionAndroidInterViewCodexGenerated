# Book Format Recommendation

> Quality status: **88/100, Upgrading**. Target: **95+**. Main gap: add final publishing/export conventions after chapter format stabilizes.

## Source Format

Use Markdown as the source of truth.

Markdown works best for this guide because it supports:

- Git versioning.
- Easy chapter splitting.
- Fast edits.
- Links to research sources.
- Code snippets when needed.
- Tables for question matrices.
- Export to PDF, HTML, DOCX, or EPUB later.

## Export Strategy

Do not design the PDF first. First make the book useful.

Recommended flow:

1. Write and validate chapters in Markdown.
2. Keep one topic per file.
3. Maintain `00-research-matrix.md` as the source-to-topic map.
4. Once the content is stable, export with Pandoc or Quarto.
5. Add a PDF theme only after the content is mature.

## Suggested PDF Pipeline

Later, a simple export could look like:

```bash
pandoc \
  interview-guide/README.md \
  interview-guide/02-kotlin-fundamentals.md \
  interview-guide/03-android-fundamentals.md \
  interview-guide/04-coroutines-flow.md \
  interview-guide/05-architecture.md \
  interview-guide/06-design-patterns.md \
  interview-guide/07-jetpack-compose.md \
  interview-guide/08-mobile-system-design.md \
  interview-guide/09-testing.md \
  interview-guide/10-performance-security-release.md \
  interview-guide/12-soft-skills.md \
  interview-guide/13-mock-interviews.md \
  interview-guide/references.md \
  -o senior-android-kotlin-interview-guide.pdf
```

If the PDF needs a polished book layout later, use Quarto or a custom Pandoc template.

## Chapter Template

```markdown
# Topic Name

## Documentation Anchors

## Forum / Interview Signals

## Why Interviewers Ask This

## Core Mental Model

## What You Must Be Able To Explain

## Interview Drill Chains

## Interview Questions

## Asked As / Question Variations

## What Your Answer Must Cover

## Short Answer

## Strong Interview Answer

## Tricky Follow-Up Questions And Answers

## Internals And Edge Cases

## What Not To Say

## Common Mistakes

## Project Experience Angle

## Mini Oral Exam

## Checklist
```

## Quality Gate

Do not call a chapter finished because it has a list of questions. A chapter is interview-ready only when it is close to 95-100/100 using `16-quality-upgrade-plan.md`.

Minimum chapter requirements:

- at least 3 documentation anchors or a clear reason why fewer exist,
- at least 3 forum/interview signals or company-style question patterns,
- drill chains for every major subtopic,
- at least one common failure answer per drill chain,
- at least one strong answer per major question that is long enough to be spoken in 1-3 minutes,
- edge cases and internals where the topic supports them,
- answers that do not sound memorized and include context, precision, trade-offs, and follow-up hooks,
- a final mini oral exam.

## Answer Quality Rule

Do not use evaluator notes as the answer the candidate should say. This guide is for the person studying, so the center of each section must be the answer they can practice out loud.

Use this distinction:

- **What Your Answer Must Cover**: the concepts your answer must include.
- **Short Answer**: a compact answer for quick checks.
- **Strong Interview Answer**: the actual answer to study and say out loud.
- **Tricky Follow-Up Questions And Answers**: prepared follow-up questions with answers directly underneath.
- **What Not To Say**: weak or incomplete responses.

Strong answers should usually be 120-250 words for broad conceptual questions and 60-120 words for narrow follow-ups. They should sound natural but complete.

They should not sound like memorized theory. A good answer should feel like a developer explaining the concept from experience:

- direct answer first,
- practical explanation,
- Android/Kotlin implication,
- trade-off or trap,
- judgment in the closing sentence.

## Tone Rule

Answers should sound like a senior developer who understands the topic, not like someone reciting a definition.

Bad:

> MVVM is an architectural pattern that separates Model, View, and ViewModel.

Better:

> In Android, I use MVVM as a way to keep the screen rendering separate from state preparation. The composable or view renders state and sends events; the ViewModel owns screen state and coordinates work with the domain or data layer. The value is not the acronym, it is ownership and testability.
