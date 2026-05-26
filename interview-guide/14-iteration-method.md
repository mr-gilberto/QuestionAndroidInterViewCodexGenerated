# Iteration Method: From Topic List To Interview-Proof Guide

> Quality status: **Internal process note, current**. Last verified: 2026-05-26. The completed iteration is reflected in the 100/100 study guide and external-alignment audit.

This guide should not grow only by adding more topics. It should grow by pressure-testing every topic against real interview chains, failure reports, strong answers, and follow-up depth.

## The Problem We Are Fixing

A topic-level guide can look complete while still failing a real interview.

Example:

```text
Topic: Kotlin data classes
Weak coverage: "data classes generate equals, hashCode, copy, toString."
Real interview chain:
  What is a data class?
  What methods does it generate?
  How does equals work internally?
  How many comparisons does it do?
  When is hashCode used?
  What happens in HashSet?
  What if a mutable property changes?
```

The second version is what the guide must support.

## New Expansion Rule

For each topic, build an **Interview Drill Chain**:

1. Basic question.
2. First follow-up.
3. Deeper follow-up.
4. Edge case.
5. Performance or correctness implication.
6. Android-specific implication.
7. Natural answer.
8. What the interviewer likely wants to hear.
9. Common failure answer.
10. Recovery answer if you forgot the term.

## Research Rule

For every topic iteration, search for:

- questions people were asked,
- feedback after failing,
- what interviewers say they expected,
- common mistakes or anti-patterns,
- big-company variants,
- forum disagreements that reveal nuance,
- official docs for correctness.

Use sources like:

- Reddit Android/Kotlin threads,
- Reddit ExperiencedDevs for behavioral/senior signals,
- Glassdoor reports,
- public company interview guides,
- Android/Kotlin official docs,
- Android system design resources,
- technical blogs by Android engineers,
- GitHub interview repositories.

## File Update Rule

Each iteration should update three places:

1. The topic chapter.
2. `00-research-matrix.md`, if the evidence changed.
3. `references.md`, if new sources were used.

## Quality Gate

A section is not done until it can answer:

- What is it?
- Why does Android/Kotlin use it?
- How does it work internally?
- Where does it fail?
- What is the common wrong answer?
- What would a senior mention naturally?
- What trade-off exists?
- What follow-up would I ask if I were the interviewer?

## 95-100 Quality Rule

Each chapter should be scored with the rubric in `16-quality-upgrade-plan.md`.

If a chapter scores below 85, treat it as an outline.

If a chapter scores 85-94, treat it as useful but not interview-proof.

If a chapter scores 95-100, it can be considered interview-ready.

## Iteration Checklist

For every iteration:

1. Pick one chapter.
2. Search official docs for correctness.
3. Search forums/interview reports for phrasing and failure signals.
4. Extract question chains, not isolated questions.
5. Add documentation anchors inside the chapter.
6. Add common failure answers.
7. Add tricky follow-up questions with answers directly underneath each question.
8. Add strong interview answers, not only short signals.
9. Add internals and edge cases.
10. Add what not to say.
11. Add a mini oral exam.
12. Rescore the chapter.

## Source Capture Rule

Every new topic claim should be grounded in one of:

- official Android/Kotlin documentation,
- public candidate report,
- forum discussion,
- company-specific interview guide,
- widely used Android interview repository,
- credible technical article by an Android/Kotlin practitioner.

If the source is a forum, treat it as evidence of interview pattern, not as final technical truth. Use official docs for technical correctness.

## Strong Answer Standard

Every important interview question needs an answer the candidate can actually say.

A good answer has:

- a direct first sentence,
- technical precision,
- one or two concrete implications,
- a trade-off or edge case when relevant,
- a natural follow-up hook.

Bad answer:

> A data class generates equals and hashCode.

Strong answer:

> A Kotlin data class is useful when the type mostly represents a value, state, or DTO. The compiler generates `equals`, `hashCode`, `toString`, `copy`, and `componentN` based on the primary constructor properties. The important part is that `==` uses structural equality, so it calls `equals` and compares those properties, not object identity. I also care about `hashCode` because if the object is used in a `HashMap` or `HashSet`, equal objects must hash the same. That is why I avoid mutable properties in data classes used as keys: changing a property after insertion can make the collection unable to find the object.
