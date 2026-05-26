# Research Matrix

> Quality status: **100/100, External Research Matrix Complete**. Last verified: 2026-05-26. Research signals have been folded into the student-facing guide, question bank, and mock interviews.

Last researched: 2026-05-25

This matrix contrasts the planned guide topics against public interview reports, forums, interview-prep sources, and official documentation. The goal is to avoid inventing a study guide in isolation. If a topic stays in the book, it should be because interviews actually ask it, or because it supports answers to questions that interviews ask.

Evidence strength:

- **High**: repeatedly appears across forums, interview reports, and prep sources.
- **Medium**: appears in several sources or as common follow-up depth.
- **Low**: useful senior knowledge, but less often reported as a direct question.

## Interview Flow Pattern

The common senior Android/Kotlin interview flow found during research:

1. Kotlin fundamentals.
2. Android fundamentals and lifecycle.
3. Coroutines, Flow, and concurrency.
4. Compose or XML/View system depending on stack.
5. Architecture: MVVM/MVI/Clean Architecture, Repository, DI.
6. Mobile system design: offline-first, caching, sync, pagination, uploads, chat/feed.
7. Testing, performance, security, Gradle/release.
8. Soft skills: ownership, conflict, mentorship, project deep-dive, decision-making.

This matches public reports from Reddit Android threads, Glassdoor senior Android reports, Meta mobile interview guides, Google L5 Android discussions, Airbnb Glassdoor reports, and Android-specific prep resources.

## Topic Evidence Table

| Topic | Evidence Strength | Reported Question Patterns | Sources |
|---|---:|---|---|
| Kotlin basics: `val`/`var`, data classes, sealed classes, scope functions | High | "Kotlin basics", "mutable vs immutable", "var vs val", "sealed/data classes", "scope functions" | [Reddit recent Android interviews](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/), [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [Kotlin docs](https://kotlinlang.org/docs/home.html) |
| Data class generated methods, equality, and hashing | High | "What is a data class?", "what methods does it generate?", "`equals`/`hashCode`", "`==` vs `===`", "mutable vs immutable" | [Kotlin data classes docs](https://kotlinlang.org/docs/data-classes.html), [Kotlin equality docs](https://kotlinlang.org/docs/equality.html), [Reddit recent Android interviews](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/), [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm) |
| Null safety and Java interop | High | "Why Kotlin still has NPEs?", "platform types", "when use `!!`?" | [Kotlin null safety docs](https://kotlinlang.org/docs/null-safety.html), [Android/Kotlin interview repositories](https://github.com/mohsenoid/Android-Interview-Questions) |
| Generics, variance, inline/reified | Medium | "Why reified needs inline?", "explain `in` and `out`", "type erasure" | [Kotlin generics docs](https://kotlinlang.org/docs/generics.html), [Droidly Kotlin deep dive](https://droidly.io/) |
| Coroutines basics | High | "What is a coroutine?", "coroutines vs threads", "launch vs async", "dispatchers" | [Reddit recent Android interviews](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/), [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [Kotlin coroutines docs](https://kotlinlang.org/docs/coroutines-guide.html) |
| Coroutine lifecycle/cancellation/structured concurrency | High | "User leaves screen during request", "ViewModel cleared", "why not GlobalScope?", "child failure behavior" | [Android concurrency interview review](https://www.reddit.com/r/androiddev/comments/1tcgqsz/amo_concurrency_android_interview_review/), [Kotlin exception handling](https://kotlinlang.org/docs/exception-handling.html), [Android architecture recommendations](https://developer.android.com/topic/architecture/recommendations) |
| Flow, StateFlow, SharedFlow | High | "Flow vs StateFlow vs SharedFlow", "cold vs hot", "lifecycle-safe collection", "one-off events" | [Android Flow docs](https://developer.android.com/kotlin/flow), [Kotlin Flow docs](https://kotlinlang.org/docs/flow.html), [Droidly coroutines/Flow](https://droidly.io/) |
| Android lifecycle and ViewModel | High | "Activity vs Fragment lifecycle", "ViewModel role", "process death", "SavedStateHandle" | [Reddit recent Android interviews](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/), [Android architecture guide](https://developer.android.com/topic/architecture) |
| Process death and state restoration | High | "ViewModel survives rotation?", "what survives process death?", "SavedStateHandle vs persistent storage", "singletons after process death" | [Android architecture guide](https://developer.android.com/topic/architecture), [Android architecture recommendations](https://developer.android.com/topic/architecture/recommendations), [Reddit recent Android interviews](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/) |
| Jetpack Compose state/recomposition | High | "What is recomposition?", "`@Stable`?", "state hoisting", "mutable list not updating", "LaunchedEffect" | [Reddit recent Android interviews](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/), [Compose UI state discussion](https://www.reddit.com/r/androiddev/comments/1nnqe51), [Compose side effects docs](https://developer.android.com/develop/ui/compose/side-effects) |
| MVVM/MVI/Clean Architecture | High | "What is MVVM?", "MVVM vs MVI", "Clean Architecture overkill?", "where should logic live?" | [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [Clean Architecture overkill discussion](https://www.reddit.com/r/androiddev/comments/1eppoaf), [Android architecture docs](https://developer.android.com/topic/architecture) |
| Repository pattern and source of truth | High | "What is repository?", "Room as source of truth", "network vs database flow" | [InterviewBee Android senior architecture](https://interviewbee.ai/resources/role-based-questions/android-developer), [Android offline-first docs](https://developer.android.com/topic/architecture/data-layer/offline-first), [Android architecture guide](https://developer.android.com/topic/architecture) |
| Dependency Injection: Hilt/Dagger/Koin | High | "DI purpose", "Hilt deep dive", "scopes", "inject ViewModel/Worker", "testing" | [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [Hilt Jetpack docs](https://developer.android.com/training/dependency-injection/hilt-jetpack) |
| Networking: Retrofit/OkHttp/errors/security | High | "What is Retrofit?", "API error handling", "encrypted networking", "MITM", "auth refresh" | [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [InterviewBee Android questions](https://interviewbee.ai/resources/role-based-questions/android-developer) |
| Offline-first, Room, WorkManager, sync | High | "Design offline-first", "cached data", "queued writes", "WorkManager for sync" | [Android offline-first docs](https://developer.android.com/topic/architecture/data-layer/offline-first), [Android System Design FAQ](https://www.androidsystemdesign.dev/faq), [Meta Android system design Reddit](https://www.reddit.com/r/interviewpreparations/comments/1mw4c1b) |
| Background work: WorkManager vs foreground service vs coroutine | High | "background work", "upload after app closes", "foreground service restrictions", "persistent work" | [Android background tasks overview](https://developer.android.com/develop/background-work/background-tasks), [WorkManager docs](https://developer.android.com/reference/androidx/work/WorkManager.html), [WorkManager persistent work docs](https://developer.android.com/topic/libraries/architecture/workmanager/), [Reddit foreground service/WorkManager discussions](https://www.reddit.com/r/androiddev/comments/yc4s0a) |
| Mobile system design | High | "Design chat/feed/photo sharing/offline-first", "mobile architecture, not backend-only" | [Meta Android system design Reddit](https://www.reddit.com/r/interviewpreparations/comments/1mw4c1b), [Google L5 Android system design Reddit](https://www.reddit.com/r/androiddev/comments/1e0kjtu/interviewing_with_google_for_an_l5_role_android/), [Android System Design FAQ](https://www.androidsystemdesign.dev/faq), [Mobile architecture mock interviews](https://mobilearchitecture.dev/) |
| Design patterns | Medium | "Repository", "Observer", "Factory", "Adapter", "Singleton drawbacks", "Strategy", "SOLID" | [Android design pattern discussions](https://www.reddit.com/r/androiddev/comments/gp73rr), [Design patterns for senior engineers](https://www.algoroq.io/interview-questions/design-patterns/), [OOD/design patterns interview guide](https://www.techinterview.org/post/3233474138/coding-interview-oop-design-patterns-strategy-observer-factory-singleton-decorator-adapter-solid-principles/) |
| Testing | High | "TDD", "ViewModel tests", "Flow tests", "Compose UI tests", "fakes vs mocks" | [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [Android coroutine testing docs](https://developer.android.com/kotlin/coroutines/test), [Android UI testing docs](https://developer.android.com/training/testing/ui-tests/behavior) |
| Performance, memory leaks, ANRs, startup | High | "detecting memory leak", "performance bottleneck", "R8", "startup", "jank" | [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [Android performance docs](https://developer.android.com/topic/performance/measuring-performance), [Android memory docs](https://developer.android.com/topic/performance/memory), [Dove Letter Android questions](https://doveletter.dev/interviews) |
| Gradle, modularization, R8/release | Medium | "modular Android SDK", "SDK versioning", "R8", "large app modules" | [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [InterviewBee Android senior architecture](https://interviewbee.ai/resources/role-based-questions/android-developer), [Dove Letter R8 topic](https://doveletter.dev/interviews) |
| Security/privacy | Medium | "encrypted networking", "MITM", "security-related questions", "token storage", "API keys", "certificate pinning" | [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm), [Android security checklist](https://developer.android.com/guide/topics/security/security), [Android security best practices](https://developer.android.com/privacy-and-security/security-best-practices), [Android Keystore/cryptography docs](https://developer.android.com/privacy-and-security/cryptography) |
| Soft skills and behavioral leadership | High | "leadership questions", "feedback", "group collaboration", "conflict", "mentoring", "mistakes", "project deep dive" | [Meta Android interview Reddit](https://www.reddit.com/r/leetcode/comments/1nagyra/meta_software_engineer_android_interview/), [Google Android interview Reddit](https://www.reddit.com/r/androiddev/comments/1mchwbe/android_developer_google_interview/), [ExperiencedDevs behavioral discussion](https://www.reddit.com/r/ExperiencedDevs/comments/t6qiwq), [Teal behavioral guide](https://www.tealhq.com/career-paths/software-engineering-manager-interview-questions/), [EM conflict questions](https://www.em-tools.io/interview-questions/conflict-resolution) |

## Big-Company Signals

### Meta

Public Meta mobile interview guides and Reddit reports point to:

- coding in Kotlin/Java or general languages,
- mobile system/product architecture,
- mobile constraints such as storage, rendering, networking, battery, caching,
- behavioral/leadership rounds.

Useful preparation topics:

- mobile architecture for feed/chat/photo sharing,
- offline-first and sync,
- UI architecture,
- data modeling and API contracts,
- leadership stories.

Sources:

- [Prepfully Meta Android Engineer Guide](https://prepfully.com/interview-guides/meta-android-engineer)
- [Meta Android E6 system design Reddit](https://www.reddit.com/r/interviewpreparations/comments/1mw4c1b)
- [Meta mobile engineer guide](https://dataford.io/interview-guides/meta/mobile-engineer)
- [Meta Android interview Reddit](https://www.reddit.com/r/leetcode/comments/1nagyra/meta_software_engineer_android_interview/)

### Google

Public Google L5 Android discussions indicate:

- DSA rounds still matter,
- Android/system design rounds may include mobile-specific product design,
- candidates report architecture and work-methodology questions.

Useful preparation topics:

- Android app/system design,
- collaborative or offline product features,
- architecture decision-making,
- Kotlin/Android basics,
- behavioral collaboration.

Sources:

- [Google L5 Android system design Reddit](https://www.reddit.com/r/androiddev/comments/1e0kjtu/interviewing_with_google_for_an_l5_role_android/)
- [Google Android interview Reddit](https://www.reddit.com/r/androiddev/comments/1mchwbe/android_developer_google_interview/)
- [Glassdoor Google senior Android result inside broader senior Android page](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm)

### Airbnb

Public Airbnb Android reports point to:

- Android Studio/project-based coding,
- Kotlin/Compose/Java module choices,
- Android system architecture on a whiteboard,
- product-like implementation such as listing apps.

Useful preparation topics:

- project deep dive,
- architecture whiteboarding,
- Compose/XML judgment,
- networking and list/feed UI,
- modular feature structure.

Sources:

- [Airbnb Senior Android Engineer Glassdoor report](https://www.glassdoor.com/Interview/Airbnb-Interview-RVW95616026.htm)
- [Airbnb interview guide, cross-functional/product depth](https://www.techinterview.org/airbnb-interview-guide/)

### Generic Senior Android Market

Across Glassdoor, Reddit, and Android-specific prep resources, repeated topics include:

- Kotlin basics,
- coroutines and Flow,
- lifecycle,
- MVVM/MVI/Clean Architecture,
- Compose,
- Hilt/DI,
- Retrofit/Room/WorkManager,
- testing,
- security,
- performance,
- modularization,
- soft skills.

Sources:

- [Glassdoor senior Android questions](https://www.glassdoor.com/Interview/senior-android-developer-interview-questions-SRCH_KO0%2C24_SDRD.htm)
- [Reddit recent Android interview discussion](https://www.reddit.com/r/androiddev/comments/1dw19ub/those_of_you_who_have_given_android_interviews/)
- [Android System Design FAQ](https://www.androidsystemdesign.dev/faq)
- [Droidly Android Interview Prep](https://droidly.io/)
- [Job Lobster Android Engineer Interview Questions 2026](https://joblobster.ai/guides/interview-prep/android-engineer-interview-questions)

## Topics To Add To The Existing Draft

The root draft already covers many core topics. The next iteration should expand:

1. **Architecture patterns chapter**
   - MVVM vs MVI vs Clean Architecture.
   - Repository, UseCase, UDF, source of truth.
   - When Clean Architecture is overkill.
   - Large app modularization.

2. **Design patterns chapter**
   - Observer, Strategy, Factory, Adapter, Builder, Decorator, State, Command.
   - Singleton vs DI.
   - Repository as architectural pattern.
   - Patterns used by Android APIs and app architecture.

3. **Soft skills chapter**
   - Conflict resolution.
   - Mentorship.
   - Technical leadership without authority.
   - Architecture disagreements.
   - Handling mistakes.
   - Feedback and code review.
   - Stakeholder communication.
   - Project deep dives.

4. **Company-style mock rounds**
   - Meta mobile system design.
   - Google L5 Android architecture/system design.
   - Airbnb Android project architecture.
   - Generic senior Android technical screen.
