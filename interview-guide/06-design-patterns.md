# Design Patterns

> Quality status: **80/100, Upgrading**. Target: **96+**. Main gap: add SOLID, Kotlin-specific nuance, pattern abuse, Android framework examples, and stronger drill chains per pattern.

## Why Interviewers Ask This

Design patterns show whether a senior developer can recognize recurring design problems and choose a solution deliberately. In Android interviews, design patterns are usually not asked as "name all Gang of Four patterns." They appear inside architecture, UI events, dependency creation, networking, state modeling, and testability.

The researched sources support design patterns as a medium-strength direct topic and a high-strength supporting topic. Repository, Observer, Singleton, Factory, Adapter, Strategy, State, and Dependency Injection appear naturally in Android architecture discussions and senior design interviews.

## Core Theory

A design pattern is a reusable way to solve a recurring design problem. It is not a rule and not a badge of seniority. A good senior answer explains:

- the problem the pattern solves,
- the trade-off it introduces,
- where it appears in Android/Kotlin,
- when not to use it.

Patterns matter most when they reduce coupling, isolate change, improve testability, or make behavior explicit.

## Patterns Worth Knowing For Android Interviews

### Repository

Problem: UI/domain should not know whether data comes from network, database, cache, or memory.

Android usage: `UserRepository`, `FeedRepository`, `AuthRepository`, usually coordinating Retrofit, Room, DataStore, and sync.

Natural answer:

"Repository is the boundary around a data domain. It gives the ViewModel or use case a stable API while hiding whether data comes from Room, network, cache, or a sync queue. In offline-first Android, it often coordinates local source of truth and remote refresh."

Common mistake: turning Repository into a dumping ground for all app logic.

### Observer

Problem: one part of the app needs to react to changes from another without tight coupling.

Android usage: Flow, StateFlow, LiveData, Compose state, listeners.

Natural answer:

"Observer is the idea behind state streams. The UI observes state and updates when the state changes. In modern Android, I usually see this through Flow/StateFlow or Compose state rather than hand-written observer lists."

Common mistake: using observers as uncontrolled event buses.

### Strategy

Problem: choose behavior at runtime without large conditional blocks.

Android usage: sorting/filtering strategies, sync strategies, auth strategies, image loading policies, validation rules.

Natural answer:

"Strategy is useful when the algorithm varies but the caller should not care which implementation is used. For example, a sync coordinator could use different conflict-resolution strategies depending on product rules."

Common mistake: creating a strategy hierarchy for two simple `if` branches that will never grow.

### Factory / Abstract Factory

Problem: object creation is complex, conditional, or should be hidden from callers.

Android usage: ViewModel factories before Hilt, Retrofit service creation, test fake creation, screen/component builders.

Natural answer:

"Factory is about centralizing creation when construction has logic or dependencies. In Android, DI often replaces a lot of manual factories, but factories still make sense for runtime-selected objects or framework-created classes."

Common mistake: using factories everywhere even when constructor injection is clearer.

### Adapter

Problem: make one interface work with another expected interface.

Android usage: RecyclerView Adapter, API-to-domain mappers, callback-to-Flow wrappers, legacy module integration.

Natural answer:

"Adapter is useful at boundaries. If a legacy SDK exposes callbacks, I might adapt it into Flow. If an API DTO shape does not match domain, I map it before it leaks into the app."

Common mistake: confusing adapter pattern with only `RecyclerView.Adapter`.

### Singleton

Problem: one shared instance is needed.

Android usage: database instance, Retrofit/OkHttp client, application-level services.

Natural answer:

"Singleton can be appropriate for expensive, stateless, or process-wide dependencies like a database or OkHttp client. But I prefer DI-managed singletons over global static access because DI keeps ownership explicit and tests cleaner."

Common mistake: making anything convenient into a singleton, especially objects that hold Activity or screen state.

### Builder

Problem: construct complex objects step by step with readable configuration.

Android usage: OkHttp client, Retrofit, notifications, WorkRequest, Room database builder.

Natural answer:

"Builder is useful when an object has many optional configuration values and construction should remain readable. Android uses it heavily for framework and library APIs."

Common mistake: writing custom builders for simple data classes where named parameters are enough.

### State

Problem: behavior changes depending on current state.

Android usage: UI state machines, auth state, media playback state, upload state.

Natural answer:

"State pattern is useful when valid behavior depends on current state. For a media player or upload flow, modeling states explicitly can prevent impossible combinations like loading and completed at the same time."

Common mistake: representing complex state with many unrelated booleans.

### Command

Problem: represent an action as an object/value so it can be queued, retried, undone, or logged.

Android usage: offline write queues, pending sync operations, analytics commands, user actions.

Natural answer:

"Command is useful in offline-first features. A pending favorite, upload, or edit can be stored as an operation with enough data to retry later."

Common mistake: adding command objects for simple direct method calls that do not need queuing or decoupling.

### Decorator

Problem: add behavior around an object without changing the object.

Android usage: OkHttp interceptors, logging wrappers, caching wrappers, analytics decorators.

Natural answer:

"Decorator is useful for cross-cutting behavior. For example, an OkHttp interceptor can add headers, logging, or auth behavior around network calls without changing each API method."

Common mistake: stacking wrappers until debugging becomes unclear.

### Dependency Injection

Problem: classes should receive dependencies rather than construct them internally.

Android usage: Hilt/Dagger/Koin, constructor injection, test fakes, scoped dependencies.

Natural answer:

"DI is the composition pattern behind testable Android architecture. The class declares what it needs, and the graph decides how to provide it. That makes lifetimes, replacements, and module boundaries clearer."

Common mistake: describing DI only as "for testing" or making every dependency app-scoped.

## Research-Backed Interview Questions

- What design patterns have you used in Android?
- What is the Repository pattern?
- Is Singleton bad?
- How is Observer used in Android?
- Factory vs Dependency Injection?
- Where have you used Strategy?
- What pattern would you use for offline queued writes?
- How do design patterns relate to SOLID?
- When is applying a design pattern overengineering?

## Question Variations

- "Which patterns appear in Android framework APIs?"
- "How would you wrap a callback API into Flow?"
- "How do you avoid huge `when` or `if` blocks?"
- "Why not use a static singleton repository?"
- "How would you design a retryable operation?"
- "What pattern is RecyclerView.Adapter?"

## Natural Interview Answer

"I do not start by trying to force a pattern. I start with the design pressure. If the problem is data-source abstraction, Repository fits. If behavior varies, Strategy may fit. If I need to react to state changes, Observer is the model behind Flow or StateFlow. If creation is complex, Factory or DI helps. The senior part is knowing the trade-off: patterns can reduce coupling, but they can also add unnecessary layers."

## Deep Follow-Ups

### Singleton vs DI

"A singleton describes lifetime: one instance. DI describes how dependencies are provided. I can have a DI-managed singleton, which is usually better than global static access because it keeps construction and replacement controlled."

### Repository vs DAO

"A DAO is a database access boundary. A repository is a data-domain boundary. The repository can use a DAO, remote API, mapper, and sync policy. If the repository only forwards DAO calls, it may not be adding much yet."

### Observer vs Flow

"Flow is not just the Observer pattern, but it serves the same high-level purpose of observing values over time. Flow adds coroutine integration, operators, cancellation, context rules, and structured collection."

### Strategy vs State

"Strategy varies an algorithm selected by context. State varies behavior based on the object's current state. They can look similar, but the reason for variation is different."

## Common Mistakes

- Memorizing pattern definitions without knowing when to use them.
- Calling every class a pattern.
- Using Singleton as a shortcut around dependency ownership.
- Creating use cases, factories, managers, and helpers that only pass data through.
- Ignoring Kotlin features that make some Java-era patterns unnecessary.
- Forgetting that Android framework APIs already embody many patterns.

## Checklist

- Can I explain each pattern by problem and trade-off?
- Can I map patterns to Android examples?
- Can I explain when not to use a pattern?
- Can I connect Repository, Observer, Factory, Adapter, Strategy, State, Command, Singleton, and DI to real interview questions?

## Strong Interview Answer Bank

### What design patterns have you used in Android?

**Strong Interview Answer**

"I would answer that through problems rather than listing patterns. For data boundaries, I use Repository so the UI and domain do not care whether data comes from network, database, or cache. For reacting to state changes, Android now commonly uses observer-like streams through Flow, StateFlow, LiveData, or Compose state. For object creation, I usually prefer dependency injection, but factories still make sense when creation depends on runtime values.

I have also used Strategy when behavior varies, for example different validation or sync conflict policies. Adapter appears both in the Android framework, like RecyclerView Adapter, and at boundaries, like adapting a callback API into Flow or mapping API DTOs into domain models.

The senior point is not to force patterns. Patterns are useful when they reduce coupling or make behavior explicit. They become harmful when they add layers without changing the real design pressure."

### Is Singleton bad?

**Strong Interview Answer**

"Singleton is not automatically bad; it describes a lifetime: one shared instance. In Android, some things are naturally process-wide, like an OkHttp client, Retrofit instance, Room database, or a stateless analytics gateway. The problem is global access and hidden ownership.

I prefer DI-managed singletons over manually accessed global objects. With Hilt or Dagger, the graph controls the lifetime and tests can replace the dependency. A global singleton makes dependencies invisible and often leads to context leaks, especially if it holds an Activity or View reference.

So my answer is: singleton lifetime can be valid, but singleton as an uncontrolled global access pattern is risky. If the object has screen-specific state, user-specific state, or references to lifecycle objects, it should not be a singleton."

### Strategy vs State pattern?

**Strong Interview Answer**

"They can look similar because both move behavior out of conditionals, but the reason is different. Strategy is for choosing an algorithm or policy. For example, a sync component could use last-write-wins, server-wins, or manual merge as different conflict strategies.

State is for behavior that changes based on the object's current state. A media player, upload process, auth session, or checkout flow can have states where different operations are valid. Modeling that explicitly can prevent impossible combinations like `isLoading`, `isComplete`, and `hasError` all being true.

In Kotlin I might implement either pattern with classes, sealed types, or functions depending on complexity. I do not always need a full object hierarchy."
