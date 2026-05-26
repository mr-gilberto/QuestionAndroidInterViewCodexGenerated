# Coroutines And Flow

> Quality status: **88/100, Upgrading**. Target: **98+**. Main gap: add documentation anchors, `stateIn`, `shareIn`, `SharingStarted`, lifecycle APIs, Flow internals, channels, callbackFlow, and testing traps.

## Why Interviewers Ask This

Coroutines and Flow are among the most common senior Android interview topics. They are also a common failure point because many candidates know the API names but not the lifetime, cancellation, exception, and UI-state implications.

Research patterns show interviewers ask:

- basic definitions,
- coroutines vs threads/RxJava,
- scopes and dispatchers,
- `launch` vs `async`,
- cancellation,
- `CancellationException`,
- Flow vs StateFlow vs SharedFlow,
- lifecycle-aware collection,
- one-off events,
- error handling.

## Interview Drill Chain: Coroutine Basics

### Basic Question

What is a coroutine?

### Follow-Ups

1. Is a coroutine a thread?
2. Does `suspend` mean background thread?
3. What is a dispatcher?
4. What is structured concurrency?
5. What happens when the parent scope is cancelled?
6. What if the user leaves the screen during a request?

### Short Answer

"A coroutine is a lightweight unit of asynchronous work. It still runs on threads, but it can suspend without blocking the thread. `suspend` does not mean background; it only means the function can suspend and resume. The dispatcher and the implementation decide where the work runs. In Android, the important part is scope ownership: screen-owned work can use `viewModelScope`, but work that must survive the screen needs a different owner, often repository/application scope or WorkManager."

### What Your Answer Must Cover

- Coroutines are not threads.
- `suspend` is not a thread switch.
- Scope should match work lifetime.
- Cancellation is expected, not an error.
- Avoid `GlobalScope` for normal app work.

### Weak Answer To Avoid

"Coroutines are background threads and I use `viewModelScope` for async work."

Why this is incomplete:

It misses dispatcher behavior, ownership, cancellation, and lifetime.

## Interview Drill Chain: `launch`, `async`, and `withContext`

### Basic Question

What is the difference between `launch`, `async`, and `withContext`?

### Follow-Ups

1. What does `launch` return?
2. What does `async` return?
3. When is `async` wrong?
4. How do exceptions differ between `launch` and `async`?
5. How do you run two requests in parallel?

### Short Answer

"I use `launch` when I want to start work that does not directly return a value to the caller; it returns a `Job`. I use `async` when I need a result, usually with `await`, and especially when I want parallel decomposition. `withContext` switches context for a block and returns the result. I avoid `async` if I never await it, because then I am probably hiding errors or using the wrong abstraction."

### What Your Answer Must Cover

- `launch` returns `Job`.
- `async` returns `Deferred<T>`.
- `await()` observes result and exception.
- `withContext` is for switching context and returning a value.
- Parallel requests need clear failure semantics.

### Weak Answer To Avoid

"`launch` is fire-and-forget and `async` is faster."

Why this is incomplete:

It overstates performance and ignores error handling.

## Interview Drill Chain: Cancellation

### Basic Question

How does coroutine cancellation work?

### Follow-Ups

1. Is cancellation automatic?
2. What does cooperative cancellation mean?
3. What happens in CPU-heavy loops?
4. What is `CancellationException`?
5. Should you catch it?
6. Why can catching `Exception` be dangerous?

### Short Answer

"Cancellation in coroutines is cooperative. Suspending functions usually check cancellation, but CPU-heavy loops need to cooperate by checking `isActive`, yielding, or breaking work into cancellable chunks. `CancellationException` is part of normal cancellation flow. I avoid swallowing it accidentally; if I catch broad exceptions, I make sure cancellation still propagates."

### What Your Answer Must Cover

- Cancellation is cooperative.
- Suspending calls usually observe cancellation.
- CPU loops need explicit checks.
- `CancellationException` should generally propagate.
- Silent catch/log is often a bug.

### Weak Answer To Avoid

"I catch all exceptions so the coroutine does not crash."

Why this is incomplete:

It may break cancellation and hide failures from the UI.

## Interview Drill Chain: Exception Handling

### Basic Question

How do exceptions work in coroutines?

### Follow-Ups

1. What happens when a child coroutine fails?
2. What is the difference between `coroutineScope` and `supervisorScope`?
3. Why did `CoroutineExceptionHandler` not catch my exception?
4. How does `async` handle exceptions?
5. How do you show errors in UI state?

### Short Answer

"In a normal structured scope, a child failure cancels the parent and siblings. That is good for all-or-nothing work. If child tasks should fail independently, I use supervisor semantics and handle each result deliberately. `CoroutineExceptionHandler` is not a replacement for local `try/catch`; it mainly handles uncaught exceptions from root coroutines. With `async`, the exception is observed when I call `await`."

### What Your Answer Must Cover

- Normal scopes propagate child failure.
- Supervisor scopes isolate child failure.
- `CoroutineExceptionHandler` has limited use.
- `async` stores exception until `await`.
- UI should receive error state, not just logs.

### Weak Answer To Avoid

"I add a `CoroutineExceptionHandler` to the scope and it catches coroutine errors."

Why this is incomplete:

It is too broad and often technically wrong.

## Interview Drill Chain: Flow vs StateFlow vs SharedFlow

### Basic Question

What is the difference between Flow, StateFlow, and SharedFlow?

### Follow-Ups

1. Cold vs hot?
2. Why use StateFlow for UI state?
3. Why not use SharedFlow for everything?
4. How do you handle one-off events?
5. What does `collectLatest` do?
6. Where does `flowOn` apply?
7. What does `catch` catch?

### Short Answer

"A regular Flow is usually cold: it starts when collected. StateFlow is hot and always has a current value, which makes it a good fit for UI state. SharedFlow is a hot shared stream with configurable replay and buffering, useful for broadcast-like events when that behavior is really what I need. For one-off UI events I think carefully about lifecycle, replay, and duplication; sometimes state plus acknowledgement is safer than a raw event stream."

### What Your Answer Must Cover

- Flow is cold by default.
- StateFlow is state, not event history.
- SharedFlow is configurable shared emissions.
- One-off events are lifecycle-sensitive.
- `flowOn` affects upstream.
- `catch` catches upstream exceptions.

### Weak Answer To Avoid

"StateFlow is just the new LiveData and SharedFlow is for events."

Why this is incomplete:

It is directionally useful but too shallow for senior follow-ups.

## Interview Drill Chain: Flow Error Handling

### Basic Question

How do you handle errors in Flow?

### Follow-Ups

1. What does `catch` catch?
2. Does it catch collector exceptions?
3. Where should you emit error UI state?
4. What happens to cancellation?
5. Should a repository catch all errors?

### Short Answer

"`catch` handles upstream exceptions from where it is placed. It does not catch exceptions thrown downstream in the collector. If I want declarative handling around collector logic, I can move work into `onEach` before `catch`. For UI, I usually map expected failures into UI state or domain result types. I avoid swallowing cancellation or converting every error into an unhelpful generic state too early."

### What Your Answer Must Cover

- Operator placement matters.
- `catch` is upstream.
- Cancellation should not be swallowed.
- Error state must reach UI.
- Repositories should map expected failures, not hide bugs.

### Weak Answer To Avoid

"I put `.catch { }` at the end of the Flow and log the error."

Why this is incomplete:

The UI may never know the operation failed.

## Interview Drill Chain: Lifecycle-Aware Collection

### Basic Question

How do you collect Flow safely in Android?

### Follow-Ups

1. What happens if you collect while the screen is stopped?
2. How do you collect in Compose?
3. How do you avoid duplicate collectors?
4. What is the role of ViewModel?
5. What happens on configuration change?

### Short Answer

"I collect UI flows in a lifecycle-aware way so the UI does not keep doing work while it is stopped. The ViewModel exposes state, usually as StateFlow, and the UI collects it with lifecycle-aware APIs. I avoid starting collectors from places that can be recreated repeatedly unless the collection is tied to the right lifecycle."

### What Your Answer Must Cover

- Lifecycle matters.
- UI collection should stop/restart appropriately.
- ViewModel state survives configuration change.
- Avoid duplicate collectors and leaks.

### Weak Answer To Avoid

"I collect in `onCreate` or inside a composable directly."

Why this is incomplete:

It may be correct in limited cases but misses lifecycle and recomposition concerns.

## Common Mistakes

- Saying coroutines are threads.
- Saying `suspend` means background.
- Using `GlobalScope`.
- Using `viewModelScope` for work that must outlive the screen.
- Catching all exceptions and swallowing cancellation.
- Using `async` without `await`.
- Assuming `CoroutineExceptionHandler` catches everything.
- Using SharedFlow as default state holder.
- Treating one-off events as simple without lifecycle concerns.
- Logging Flow errors without updating UI state.
- Collecting flows without lifecycle awareness.

## Checklist

- Can I explain coroutine vs thread?
- Can I explain `suspend` accurately?
- Can I choose the right scope?
- Can I explain cancellation and `CancellationException`?
- Can I explain `launch`, `async`, and `withContext`?
- Can I explain normal vs supervisor failure?
- Can I compare Flow, StateFlow, and SharedFlow?
- Can I explain `flowOn`, `catch`, and `collectLatest`?
- Can I discuss lifecycle-aware collection?

## Strong Interview Answer Bank

### What is a coroutine, and is it the same as a thread?

**Strong Interview Answer**

"A coroutine is a lightweight unit of asynchronous work. It is not the same thing as a thread. Coroutines run on threads, but they can suspend without blocking the underlying thread. That is the main benefit: I can write asynchronous code in a sequential style while letting the thread do other work when the coroutine is waiting.

In Android, the important part is not only using coroutines but using the right scope and dispatcher. `suspend` does not mean background thread. A suspend function can run on the main thread unless the implementation or caller switches context. For blocking I/O I need an appropriate dispatcher or an API that already handles threading.

Scope is the ownership model. `viewModelScope` is good for work owned by a screen. If the user leaves and the ViewModel is cleared, that work should usually cancel. But if the work must survive the screen or process, like a durable upload or sync, I should use a different owner such as WorkManager or an application-level component."

### How do coroutine exceptions work?

**Strong Interview Answer**

"Exception behavior depends on the builder and the scope. With `launch`, an unhandled exception normally propagates to the parent and can cancel sibling coroutines in a regular structured scope. With `async`, the exception is captured in the `Deferred` and is observed when I call `await`.

That parent-child behavior matters. If several child coroutines are part of one all-or-nothing operation, normal `coroutineScope` behavior is useful because one failure cancels the operation. If the children are independent, I use `supervisorScope` or a `SupervisorJob`, but then I must handle each error deliberately because failures will not automatically cancel the whole group.

I am also careful with `CancellationException`. Cancellation is normal coroutine control flow, not a business failure. If I catch broad exceptions and accidentally swallow cancellation, I can break structured concurrency and make work continue when it should stop."

### Flow vs StateFlow vs SharedFlow?

**Strong Interview Answer**

"A regular Flow is usually cold: it starts producing values when collected, and each collector can trigger its own execution. That is good for streams of work or data transformations where collection should control execution.

`StateFlow` is a hot state holder. It always has a current value and is a strong fit for ViewModel UI state because the screen can render from the latest snapshot at any time. It is not an event history; it represents current state.

`SharedFlow` is a hot shared stream with configurable replay and buffering. It can be useful for broadcast-like emissions, but I do not use it blindly for all one-off events. Navigation, snackbars, and effects are lifecycle-sensitive. Sometimes a `SharedFlow` is fine; sometimes modeling the effect as state with acknowledgement is safer. The senior decision is not 'StateFlow for state, SharedFlow for events' as a slogan, but understanding replay, lifecycle, duplication, and loss."
