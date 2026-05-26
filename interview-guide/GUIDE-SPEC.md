# Guide Specification

> Quality status: **Editorial source of truth, current**. Last verified: 2026-05-26. The implemented guide structure now follows this student-facing format.

This document defines what the Senior Android / Kotlin interview guide must become. It exists so future iterations do not lose the thread.

## Purpose

The guide is for a developer studying to pass Senior Android Developer / Senior Kotlin Developer interviews.

It must help the reader:

- learn the theory behind each topic,
- recognize how interviewers phrase questions,
- answer naturally and deeply,
- handle follow-up questions,
- avoid shallow or memorized answers,
- connect theory to Android-specific trade-offs,
- prepare for technical, architecture, system design, and behavioral rounds.

## What This Guide Is Not

The guide is not:

- an internal evaluator rubric,
- a list of random topics,
- a collection of short definitions,
- a research dump,
- a checklist for interviewers,
- a generic Android tutorial,
- a LeetCode-only prep plan.

Internal files such as research matrices, scorecards, quality plans, and failure analysis can exist, but they must not be presented as the primary study material.

## Source Of Truth

Primary student-facing file:

- `STUDY-GUIDE.md`
- `QUESTION-BANK.md`
- `MOCK-INTERVIEWS.md`
- `FLASHCARDS.md`

Supporting topic chapters:

- `02-kotlin-fundamentals.md`
- `03-android-fundamentals.md`
- `04-coroutines-flow.md`
- `05-architecture.md`
- `06-design-patterns.md`
- `07-jetpack-compose.md`
- `08-mobile-system-design.md`
- `09-testing.md`
- `10-performance-security-release.md`
- `12-soft-skills.md`

Internal/editorial files:

- `00-research-matrix.md`
- `01-book-format.md`
- `14-iteration-method.md`
- `15-failure-analysis.md`
- `16-quality-upgrade-plan.md`
- `17-chapter-scorecard.md`
- `references.md`

Rule: internal/editorial files may guide improvements, but the user should study from `STUDY-GUIDE.md` and topic chapters.

## Final Study Guide Structure

`STUDY-GUIDE.md` should eventually use this structure:

```text
# Senior Android / Kotlin Developer Interview Study Guide

## How To Use This Guide
## Study Roadmap
## Interview Round Map
## Answering Framework

# Part 1: Kotlin Fundamentals
# Part 2: Android Fundamentals
# Part 3: Coroutines And Flow
# Part 4: Jetpack Compose
# Part 5: Architecture
# Part 6: Design Patterns
# Part 7: Mobile System Design
# Part 8: Testing
# Part 9: Performance, Security, And Release
# Part 10: Soft Skills

# Mock Interviews
# Flashcards
# Final Readiness Checklist
```

Practice files:

- `QUESTION-BANK.md`: questions only, grouped by topic, for active recall.
- `MOCK-INTERVIEWS.md`: timed rounds that simulate real interviews.
- `FLASHCARDS.md`: fast recall prompts for daily review.

## Required Topic Format

Every topic must follow this study-oriented format:

```text
## Topic Name

### Theory
Concise but real explanation of the concept.

### Interview Questions
- Question 1
- Question 2
- Question 3

### Asked As / Variations
- Alternate phrasing 1
- Alternate phrasing 2
- Alternate phrasing 3

### Strong Answer
The answer the candidate should practice out loud. It must sound like a developer explaining what they understand, not like someone reciting theory.

### Tricky Follow-Up Questions And Answers
Each important follow-up must appear as a question with its answer directly underneath. Do not leave follow-ups as unanswered practice bullets, and do not separate follow-up questions into one list and answers into another later section.

### Internals And Edge Cases
What happens under the hood, performance/correctness traps, lifecycle traps, or Android-specific behavior.

### What Not To Say
Weak, shallow, or misleading answers.

### Practice
Mini oral exam, flashcards, or scenario questions.
```

## Answer Quality Standard

Strong answers must:

- be spoken in first person naturally,
- sound conversational, not academic,
- avoid sounding memorized,
- be long enough to answer a real interview question,
- include the direct answer early,
- include technical precision,
- include Android-specific implications when relevant,
- include trade-offs when relevant,
- anticipate at least one follow-up,
- avoid unnecessary filler.
- avoid evaluator-only language such as "what a senior should show" or "evaluator signal."

Strong answers should usually follow this shape:

1. Direct answer in one sentence.
2. Explain the concept in practical terms.
3. Add the Android/Kotlin implication.
4. Mention one trade-off, trap, or edge case.
5. End with a sentence that shows judgment.

The answer should not sound like:

```text
The definition of X is...
According to documentation...
X is a mechanism by which...
```

The answer should sound more like:

```text
I usually think about X as...
The part that matters in Android is...
The trap I watch for is...
In practice I would...
```

Typical length:

- narrow conceptual answer: 80-140 words,
- broad conceptual answer: 150-250 words,
- system design answer: 250-500 words,
- behavioral answer: 200-350 words.

Bad:

```text
A data class stores data and generates equals/hashCode.
```

Good:

```text
A Kotlin data class is useful when the type mostly represents a value, state, DTO, or simple domain model. The compiler generates equals, hashCode, toString, copy, and componentN based on the primary constructor properties. The important part is that equality is structural with ==, so Kotlin compares those constructor properties rather than reference identity. I also care about hashCode because data classes are often used in sets, maps, diffing, or state comparisons. If a mutable property participates in equality and changes after insertion into a HashSet, lookup can break. Also, copy is shallow, so nested mutable objects are still shared unless explicitly copied.
```

## Minimum Coverage Targets

The final guide should include at least:

- 80-120 main interview questions,
- 250-400 question variations,
- 80+ strong answers,
- 150+ follow-up answers,
- 10+ mock interview rounds,
- 100+ flashcards,
- a 2-4 week study roadmap,
- a final readiness checklist.

Minimum question distribution:

| Area | Minimum Main Questions |
|---|---:|
| Kotlin Fundamentals | 15 |
| Android Fundamentals | 12 |
| Coroutines And Flow | 15 |
| Jetpack Compose | 12 |
| Architecture | 12 |
| Design Patterns | 8 |
| Mobile System Design | 8 |
| Testing | 8 |
| Performance/Security/Release | 10 |
| Soft Skills | 10 |

## Required Topics

### Kotlin Fundamentals

Must cover:

- `val` vs `var`
- null safety
- platform types
- `!!`, safe calls, Elvis operator
- `lateinit` vs `lazy`
- data classes
- `equals` / `hashCode`
- `copy()` shallow behavior
- sealed classes and sealed interfaces
- enum vs sealed class
- object and companion object
- extension functions
- scope functions
- inline, noinline, crossinline
- reified generics
- type erasure
- generics variance: `in`, `out`
- collections and mutability

### Android Fundamentals

Must cover:

- Activity lifecycle
- Fragment lifecycle
- configuration changes
- process death
- ViewModel lifetime
- SavedStateHandle
- saved instance state limits
- context types
- memory leaks
- intents
- deep links
- permissions
- broadcasts
- services basics
- WorkManager basics
- resources/configuration

### Coroutines And Flow

Must cover:

- coroutine vs thread
- suspend functions
- structured concurrency
- scopes
- dispatchers
- `launch`, `async`, `withContext`
- cancellation
- `CancellationException`
- exception propagation
- `coroutineScope` vs `supervisorScope`
- Flow cold streams
- StateFlow
- SharedFlow
- Channel
- `stateIn`, `shareIn`
- `flowOn`
- `catch`
- `collectLatest`
- lifecycle-aware collection
- testing coroutines and Flow

### Jetpack Compose

Must cover:

- declarative UI
- recomposition
- state reads
- state hoisting
- `remember`
- `rememberSaveable`
- ViewModel state
- `LaunchedEffect`
- `DisposableEffect`
- `SideEffect`
- `rememberUpdatedState`
- `derivedStateOf`
- snapshot state
- mutable collections pitfalls
- stability/skippability
- lazy list keys
- navigation/effects
- Compose testing
- Compose performance

### Architecture

Must cover:

- MVVM
- MVI
- Clean Architecture
- Repository
- UseCase
- UDF
- single source of truth
- DTO/domain/UI models
- data mapping
- dependency direction
- modularization
- feature modules
- legacy migration
- overengineering

### Design Patterns

Must cover:

- Repository
- Observer
- Strategy
- Factory
- Adapter
- Singleton
- State
- Command
- Decorator
- Dependency Injection
- SOLID principles
- pattern abuse
- Kotlin alternatives to classic patterns

### Mobile System Design

Must cover:

- offline-first design
- cached reads
- offline writes
- sync
- conflict resolution
- WorkManager
- foreground services
- idempotency
- pagination
- chat
- feed
- photo/video upload
- location tracking
- feature flags
- app startup
- auth/token refresh

### Testing

Must cover:

- unit tests
- integration tests
- UI tests
- ViewModel tests
- coroutine tests
- `runTest`
- dispatcher injection
- Flow testing
- StateFlow testing
- fakes vs mocks
- Compose UI tests
- Room migration tests
- CI flakiness

### Performance, Security, And Release

Must cover:

- ANRs
- jank
- startup performance
- memory leaks
- Android Studio profiler
- Perfetto
- Macrobenchmark
- Android Vitals
- token storage
- Android Keystore
- API keys in APK
- certificate pinning
- deep link security
- exported components
- WebView risks
- R8
- ProGuard keep rules
- mapping files
- release builds
- staged rollout
- hotfix/rollback

### Soft Skills

Must cover:

- architecture disagreement
- mentoring
- ownership
- project deep dive
- conflict resolution
- code review feedback
- technical debt
- production incident
- mistake/failure
- ambiguous requirements
- working with product/design/backend
- leadership without authority

## Study Features Required

The final guide must include:

### Study Roadmap

At least:

- 2-week fast track,
- 4-week complete track,
- last-day review plan.

### Interview Round Map

Must explain:

- Kotlin/Android fundamentals round,
- architecture round,
- system design round,
- coding/practical round,
- behavioral round.

### Mock Interviews

Must include:

- Kotlin fundamentals mock,
- Android lifecycle mock,
- coroutines/Flow mock,
- Compose mock,
- architecture mock,
- mobile system design mock,
- testing/performance mock,
- soft skills mock,
- mixed senior round.

### Flashcards

Must include short prompts and answers for rapid review.

### Final Checklist

Must answer:

- Can I explain the basics?
- Can I handle follow-ups?
- Can I answer without memorized theory?
- Can I connect to Android constraints?
- Can I discuss trade-offs?
- Can I tell project stories?

## Research Requirements

For every major area:

- use official docs for correctness,
- use forums/interview reports for phrasing,
- use candidate reports for failure patterns,
- use big-company reports where available,
- cite sources in `references.md`,
- summarize evidence in `00-research-matrix.md`.

Forum sources are used for question patterns, not technical truth. Official docs decide correctness.

## Future Iteration Rule

Every future iteration should do one of these:

1. Add more interview questions.
2. Add stronger answers.
3. Add follow-up answers.
4. Add theory that helps answer questions.
5. Add source-backed question variations.
6. Add mock interview practice.

Do not add more evaluator-only notes to the study guide. If a section cannot help the candidate practice an answer out loud, keep it in an internal audit file, not in the student-facing guide.
