# Internal Failure Analysis Notes

> Quality status: **Internal analysis archive, superseded by 100/100 guide content**. Last verified: 2026-05-26. Resolved failure patterns were folded into `STUDY-GUIDE.md`, `QUESTION-BANK.md`, and `MOCK-INTERVIEWS.md`.

Last researched: 2026-05-25

This is an internal editorial/research file, not the study guide.

Use `STUDY-GUIDE.md` and the topic chapters for studying. This file captures failure patterns found in forums, interview reports, and prep resources so those patterns can be converted into better questions and stronger study answers.

## Cross-Topic Failure Patterns

### 1. Knowing Names But Not Ownership

Common failure:

> "Use ViewModel, Repository, Hilt, Flow."

Why this is incomplete:

It lists tools but does not explain who owns state, who owns work, who survives lifecycle changes, or what happens when work fails.

Study answer pattern:

Explain ownership:

- UI renders state.
- ViewModel owns screen state.
- Repository owns data policy.
- WorkManager owns persistent background work.
- DI owns construction/lifetimes.

### 2. Knowing Modern APIs But Not Trade-Offs

Common failure:

> "Use Compose because it is modern."

Study answer pattern:

Explain why and when:

- Compose helps declarative UI and state-driven rendering.
- XML may still exist in legacy screens.
- Migration can be incremental.
- Performance still needs measurement.
- Navigation, lifecycle, and side effects need care.

### 3. Treating Senior Android As UI-Only

Common failure:

> Focus only on screens and ignore data, networking, sync, process death, testing, and product constraints.

Study answer pattern:

Mention mobile constraints:

- unreliable network,
- process death,
- offline behavior,
- battery,
- memory,
- app startup,
- caching,
- security,
- release risk.

### 4. Vague Behavioral Answers

Common failure:

> "We communicated better and solved it."

Study answer pattern:

Give context, personal action, trade-off, result, and reflection.

## Kotlin Failure Patterns

### Data Classes

Weak answer to avoid:

> "A data class stores data and creates getters/setters."

What the study answer must include:

- generated methods,
- primary-constructor-only behavior,
- `==` vs `===`,
- `equals` flow,
- `hashCode` usage,
- shallow `copy`,
- mutable key danger.

Study answer pattern:

> "A data class generates `equals`, `hashCode`, `toString`, `copy`, and `componentN` from primary constructor properties. `==` calls `equals`, while `===` checks reference identity. `hashCode` matters when the object is used in hash-based collections. I avoid mutable properties in keys because changing a property can change the hash after insertion."

Sources:

- [Kotlin data classes](https://kotlinlang.org/docs/data-classes.html)
- [Kotlin equality](https://kotlinlang.org/docs/equality.html)

### Null Safety

Weak answer to avoid:

> "Kotlin prevents null pointer exceptions."

What the study answer must include:

- `!!`,
- platform types,
- Java interop,
- initialization leaks,
- generic nullability,
- `lateinit` exceptions.

Study answer pattern:

> "Kotlin makes nullability explicit, but NPEs can still come from `!!`, Java platform types, initialization issues, or generic interop. I treat nullability as an API contract."

## Coroutines Failure Patterns

### Scope Misuse

Weak answer to avoid:

> "Just use `viewModelScope`."

Study answer pattern:

> "I would not answer coroutine scope questions with only 'use `viewModelScope`.' The right scope depends on who owns the work. If the work is screen-owned, like loading data for a screen or reacting to a user action whose result only matters while that screen exists, `viewModelScope` is a good fit because it cancels when the ViewModel is cleared.
>
> If the work must continue after the user leaves the screen, the ownership should move somewhere else. For example, a retryable upload, sync job, or operation that must survive process death should usually be modeled with persistent state and WorkManager. A repository or application-level scope can make sense for process-level work, but only if the lifetime and cancellation policy are explicit.
>
> The core idea is that coroutine scope is not just syntax. It is a lifetime contract. I choose the scope based on how long the work should live, what should cancel it, and where the result should be observed."

### Swallowing `CancellationException`

Weak answer to avoid:

> "I catch all exceptions and log them."

Study answer pattern:

> "In coroutine code I am careful with broad `try/catch` blocks because cancellation is part of normal coroutine control flow. `CancellationException` is how a coroutine is told to stop, and it should generally be allowed to propagate. If I catch `Exception` around a suspending call and then just log it or convert it to a generic error, I may accidentally swallow cancellation.
>
> That can break structured concurrency. For example, a ViewModel may be cleared, the parent scope may cancel, but a child operation keeps running because cancellation was caught and treated as a normal failure. That can lead to wasted work, stale UI updates, or cleanup code not behaving as expected.
>
> In practice, I either catch more specific expected exceptions, like network or parsing failures, or I rethrow `CancellationException` before mapping the error. My mental model is: expected business/data failures can become UI state; cancellation should usually remain cancellation."

Sources:

- [Reddit: common coroutine mistakes](https://www.reddit.com/r/androiddev/comments/1scf1mt/what_are_common_mistakes_when_using_coroutines_in/)
- [Kotlin coroutine exception handling](https://kotlinlang.org/docs/exception-handling.html)

### `suspend` Means Background

Weak answer to avoid:

> "`suspend` runs on a background thread."

Study answer pattern:

> "`suspend` means the function can suspend without blocking. It does not choose the thread. Dispatcher and implementation decide where code runs."

### Coroutines vs Threads/Rx

Weak answer to avoid:

> "Coroutines replace threads."

Study answer pattern:

> "Coroutines run on threads but are lighter units of work. They can suspend and resume without blocking a thread. Rx is a reactive library with a broader operator model; Flow covers many stream use cases with coroutine/lifecycle integration."

Sources:

- [Reddit: coroutines/threads/RxJava](https://www.reddit.com/r/androiddev/comments/1ldv0vv)
- [Reddit: recent Android interviews](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/)

## Compose Failure Patterns

### Recomposition Misunderstood

Weak answer to avoid:

> "Recomposition redraws the whole screen whenever state changes."

Study answer pattern:

> "Recomposition re-invokes composables that read changed state. It can be skipped or cancelled. I do not rely on exact recomposition timing for correctness."

### State Hoisting

Weak answer to avoid:

> "State hoisting means putting all state in the ViewModel."

Study answer pattern:

> "State hoisting means moving state to the lowest common owner that needs to read or change it. Some state belongs in ViewModel, some local UI state can stay in Compose."

### `rememberSaveable` / Lifecycle / Navigation

Failure point:

Candidates coming from hybrid/declarative UI may know the mental model but miss Android-specific lifecycle and navigation.

Study answer pattern:

- `remember` survives recomposition.
- `rememberSaveable` survives configuration/process recreation when saveable.
- ViewModel survives configuration change but not process death.
- Navigation side effects must be lifecycle-aware.

Sources:

- [Reddit: Senior interview](https://www.reddit.com/r/androiddev/comments/1r8nkex/senior_interview/)
- [Reddit: Compose interview questions](https://www.reddit.com/r/androiddev/comments/1glbg3e)
- [Compose side effects docs](https://developer.android.com/develop/ui/compose/side-effects)

## Architecture Failure Patterns

### Clean Architecture As Folder Naming

Weak answer to avoid:

> "Clean Architecture is ViewModel, UseCase, Repository."

Study answer pattern:

> "Clean Architecture is about dependency direction and separation of concerns. UseCases are useful when they represent meaningful business operations, not when they are pass-through wrappers."

### Overengineering

Weak answer to avoid:

> "I use Clean Architecture for everything."

Study answer pattern:

> "I use the amount of structure justified by complexity, team size, testability, and expected change. Too many layers can become abstract spaghetti."

Sources:

- [Reddit: Clean Architecture overkill](https://www.reddit.com/r/androiddev/comments/1eppoaf)
- [Reddit: MVVM with Clean Architecture](https://www.reddit.com/r/androiddev/comments/ebib18)

## System Design Failure Patterns

### Backend-Only Design

Weak answer to avoid:

> Designs server APIs and databases but barely talks about the Android client.

Study answer pattern:

Talk about:

- local source of truth,
- offline behavior,
- sync,
- caching,
- process death,
- WorkManager,
- battery,
- UI state,
- testing,
- rollout.

Sources:

- [Meta Android E6 system design Reddit](https://www.reddit.com/r/interviewpreparations/comments/1mw4c1b)
- [Google L5 Android system design Reddit](https://www.reddit.com/r/androiddev/comments/1e0kjtu/interviewing_with_google_for_an_l5_role_android/)
- [Android System Design FAQ](https://www.androidsystemdesign.dev/faq)

## Behavioral Failure Patterns

### Vague Seniority

Weak answer to avoid:

> "I helped the team and communicated with stakeholders."

Study answer pattern:

- specific situation,
- personal action,
- trade-off,
- measurable or observable result,
- reflection.

### Ego In Conflict

Failure point:

Forums repeatedly mention that good senior engineers show low ego, ask for help, give feedback constructively, and do not make others feel stupid.

Study answer pattern:

> "I made the decision criteria explicit, listened to the concerns, and moved the team toward a reversible decision."

Sources:

- [Reddit: Senior interview](https://www.reddit.com/r/androiddev/comments/1r8nkex/senior_interview/)
- [ExperiencedDevs behavioral discussion](https://www.reddit.com/r/ExperiencedDevs/comments/t6qiwq)

## Iteration 2: Broader Forum Findings

This iteration expanded beyond Kotlin/coroutines into Android fundamentals, Compose, DI, networking, WorkManager, modularization, performance, security, and behavioral signals.

### Android Fundamentals

Observed pattern:

Candidates often know Activity/Fragment lifecycle names but fail when asked about process death, saved state, singletons, and what survives.

Study answer pattern:

> "Rotation recreates UI but ViewModel can survive. Process death kills all in-memory objects, including ViewModels and singletons. I restore with small saved keys and durable storage."

Topics to strengthen:

- process death,
- `SavedStateHandle`,
- `rememberSaveable`,
- singletons after process death,
- state placement.

Source signals:

- Reddit Android lifecycle/interview discussions,
- Android architecture docs,
- Compose/lifecycle forum discussions.

### Dependency Injection

Observed pattern:

Candidates describe Hilt as boilerplate reduction but miss scopes, lifecycle, test replacement, and context leaks.

Study answer pattern:

> "DI is about ownership and lifetime. A singleton dependency must not hold Activity context. ViewModel-scoped dependencies are different from app-scoped dependencies. Constructor injection is preferred when possible."

Topics to strengthen:

- Hilt components/scopes,
- `@ApplicationContext` vs Activity context,
- Worker injection,
- replacing dependencies in tests,
- Hilt vs Koin trade-offs.

### Testing

Observed pattern:

Candidates say they write unit/UI tests but struggle with coroutine virtual time, Flow assertions, fake repositories, and Compose semantics.

Study answer pattern:

> "I test ViewModels by driving public events, controlling dispatchers with `runTest`, collecting state emissions deterministically, and using fakes when behavior matters."

Topics to strengthen:

- `runTest`,
- dispatcher injection,
- Flow testing,
- Compose UI semantics,
- migration tests for Room,
- fakes vs mocks.

### Networking

Observed pattern:

Candidates explain Retrofit but miss token refresh concurrency, error classification, idempotent retries, and cancellation.

Study answer pattern:

> "I separate transport errors, HTTP errors, parsing errors, and domain failures. Token refresh should be centralized and serialized so concurrent 401s do not trigger multiple refresh requests."

Topics to strengthen:

- Retrofit/OkHttp responsibilities,
- Interceptor vs Authenticator,
- token refresh locking,
- retry/backoff,
- idempotency,
- API DTO mapping.

### WorkManager And Background Work

Observed pattern:

Candidates say "use WorkManager for background work" without distinguishing deferrable persistent work from immediate user-visible work.

Study answer pattern:

> "WorkManager is for deferrable persistent work with constraints and retry. Foreground service is for immediate user-visible ongoing work. Coroutines are in-process and tied to scope lifetime."

Topics to strengthen:

- WorkManager vs coroutine vs foreground service,
- constraints,
- unique work,
- retries,
- idempotency,
- Android foreground-service restrictions.

### Gradle, Modularization, And Release

Observed pattern:

Candidates talk about clean module structure but miss build-time cost, dependency cycles, R8/release differences, and CI validation.

Study answer pattern:

> "Modularization must improve ownership, boundaries, or build performance. Release builds must be tested because R8, resources, signing, and variants can change behavior."

Topics to strengthen:

- feature/core modules,
- dependency direction,
- KAPT/KSP cost,
- convention plugins,
- R8 keep rules,
- release-like testing,
- staged rollout.

### Security

Observed pattern:

Candidates overclaim mobile security, especially hiding secrets in APK or saying certificate pinning makes the app secure.

Study answer pattern:

> "The client is not a trusted environment. Secrets in the APK are inspectable. Server-side authorization is the real trust boundary. Certificate pinning is a threat-model trade-off with rotation risk."

Topics to strengthen:

- token storage,
- Android Keystore,
- API keys in APK,
- certificate pinning trade-offs,
- deep links and exported components,
- WebView risks,
- logging sensitive data.

### Behavioral

Observed pattern:

Senior candidates fail when behavioral stories are vague or ego-driven. Technical strength is not enough if they cannot show collaboration, ownership, and judgment.

Study answer pattern:

> "I can describe the context, my action, the trade-off, the result, and what I learned. I can disagree without making it personal."

Topics to strengthen:

- conflict,
- mentorship,
- code review feedback,
- technical debt,
- incident handling,
- product/design/backend alignment,
- project deep dives.
