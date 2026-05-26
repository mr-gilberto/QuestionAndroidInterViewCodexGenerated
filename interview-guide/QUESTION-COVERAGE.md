# Question Coverage

> Quality status: **Traceability audit**. Last audit: 2026-05-25.

Purpose: verify that the practice questions are answerable from the documented study sections. If a question cannot be answered from `STUDY-GUIDE.md`, the guide is incomplete.

## How To Use This File

1. Pick a question from `QUESTION-BANK.md` or from a `Topic Drill Questions` section in `STUDY-GUIDE.md`.
2. Study the mapped topic section.
3. Answer out loud for 60-120 seconds.
4. If the answer feels thin, mark it as `Needs expansion` and expand the topic section, not only the question bank.

## Coverage Summary

Current exact traceability check:

- `QUESTION-BANK.md` numbered questions: **228**
- `STUDY-GUIDE.md` topic drill questions: **228**
- exact question-bank prompts missing from study guide: **0**
- study-guide drill questions with `Senior answer`: **228**
- study-guide drill questions with `Tricky follow-ups answered`: **228**
- study-guide tricky follow-up questions: **684**
- study-guide tricky follow-up answers: **684**
- mock interview tricky follow-up questions: **285**
- mock interview tricky follow-up answers: **285**

| Question Area | Bank Range | Study Section | Coverage | Notes |
|---|---:|---|---|---|
| Kotlin data classes, equality, null safety, sealed types, generics | 1-30, 153-162 | `STUDY-GUIDE.md` Part 1 | Direct | Expanded data-class internals, equality comparisons, `hashCode`, Kotlin modeling features, value classes, and result modeling. |
| Android lifecycle, saved state, context, intents, permissions, deep links | 31-45, 163-170 | `STUDY-GUIDE.md` Part 2 | Direct | Expanded lifecycle, Fragment view lifecycle, `PendingIntent`, permissions, deep links, exported components. |
| Coroutines, cancellation, Flow, lifecycle collection, operators | 46-67, 171-180 | `STUDY-GUIDE.md` Part 3 | Direct | Expanded `callbackFlow`, `awaitClose`, `combine`, `zip`, `flatMapLatest`, `mapLatest`, `debounce`, dispatchers, and parallel work. |
| Compose state, effects, recomposition, performance, testing | 68-82, 181-188 | `STUDY-GUIDE.md` Part 4 | Direct | Expanded stability, skippability, `derivedStateOf`, LazyColumn keys, snapshot state, semantics testing. |
| Architecture, Clean Architecture, DI, Hilt, modularization | 83-95, 189-196 | `STUDY-GUIDE.md` Part 5 | Direct | Expanded dependency inversion, Hilt/Dagger/Koin, scopes, dispatcher qualifiers, Worker injection, test replacement. |
| Design patterns | 96-105 | `STUDY-GUIDE.md` Part 6 | Direct | Covered through problem-first answers: Repository, Observer, Strategy, Factory, Adapter, Singleton, State, Command, pattern abuse. |
| Mobile system design | 106-118, 197-204 | `STUDY-GUIDE.md` Part 7 | Direct | Expanded offline-first, photo upload, token refresh, chat, pagination, startup, flags, logout, sync observability. |
| Testing | 119-128, 205-212 | `STUDY-GUIDE.md` Part 8 | Direct | Expanded `MainDispatcherRule`, `StandardTestDispatcher`, `UnconfinedTestDispatcher`, virtual time, Turbine, `stateIn`, WorkManager testing. |
| Performance, security, release | 129-142, 213-220 | `STUDY-GUIDE.md` Part 9 | Direct | Expanded startup, baseline profiles, Macrobenchmark, WebView bridges, exported components, R8 rules, mapping files, rollout incidents. |
| Soft skills | 143-152, 221-228 | `STUDY-GUIDE.md` Part 10 | Direct | Expanded leadership, debt, incidents, code review conflict, ambiguity, reversible decisions, AI tooling. |

## Forum-Driven Additions

These additions came from comparing the guide against public candidate/interviewer discussions. Forum sources are used for question phrasing and emphasis, while technical answers are anchored in official Kotlin and Android documentation.

| Source Pattern | Added Or Reinforced In Guide |
|---|---|
| Recent Android interview reports mention MVVM, multimodule setup, coroutines, Compose, DI, Hilt/Koin, testing with MockK/Turbine, Clean Architecture, delegates, and practical code review scenarios. | Architecture, DI, Testing, Coroutines, Compose, and Soft Skills drill questions. |
| Compose interview reports mention state hoisting, modifiers, recomposition, StateFlow, `LaunchedEffect`, `DisposableEffect`, LazyColumn performance, and common recomposition issues. | Compose theory, effects, stability/skippability, lazy keys, and Compose testing. |
| Senior interview advice emphasizes system design, backend/database/networking awareness, pitfalls, Clean Architecture, Hilt, Coroutines/Flow, Room, and lack of ego. | Mobile System Design, Architecture, Android Fundamentals, and Soft Skills. |
| Mobile system design discussions emphasize offline-first/caching, orientation/process death, functional scalability, services/background work, testing, and explaining trade-offs. | Offline-first feed, sync conflict handling, WorkManager, process death, startup, and system design drill questions. |
| Recent candidate feedback mentions identifying unnecessary work, unnecessary recomposition, uncancelled async work, loading images from URLs, and implementing/navigating new screens. | Performance, Compose, Coroutines cancellation, and Android lifecycle sections. |

## High-Risk Questions Now Covered

These were the questions most likely to expose gaps before this pass:

- Data class generated `equals`, number of property comparisons, `hashCode`, shallow `copy`, and mutable keys.
- Fragment view lifecycle and clearing binding.
- `PendingIntent`, deep links, task/back-stack behavior, and exported components.
- `callbackFlow` and why `awaitClose` is not optional.
- `combine` vs `zip`, `flatMapLatest` vs `mapLatest`, `debounce`, and one-shot parallel work with `async`.
- Compose stability, skippability, `derivedStateOf`, LazyColumn keys, snapshot state, and semantics testing.
- Hilt scopes, Hilt vs Dagger vs Koin, dispatcher qualifiers, Worker injection, and dependency replacement in tests.
- WorkManager testing, `MainDispatcherRule`, virtual time, Turbine, and testing `stateIn`.
- Baseline Profiles, Macrobenchmark, WebView bridges, exported component risks, R8 keep rules, and mapping files.
- Behavioral stories for debt, conflict, ambiguity, incidents, leadership without authority, and AI tooling.

## Remaining Improvement Rule

Every future question added to `QUESTION-BANK.md` must be added under the matching `Topic Drill Questions` block in `STUDY-GUIDE.md` and mapped here. If the guide cannot answer it, expand the topic theory and strong answer before adding more questions.
