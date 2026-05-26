# Senior Android / Kotlin Developer Interview Study Guide

> Quality status: **Archive/generated draft, superseded by `interview-guide/STUDY-GUIDE.md` 100/100**. Last verified: 2026-05-26. Do not study this file as the primary source.

Last researched: 2026-05-25

Note: this is the first monolithic draft. The modular book structure now lives in `interview-guide/`, with a research matrix, references, and expanded chapters for architecture, design patterns, and soft skills.

This guide is designed as a compact interview study manual for Senior Android Developer and Senior Kotlin Developer roles. It is not a memorized Q&A sheet. The goal is to understand the fundamentals well enough to answer simple questions, handle deeper follow-ups, and explain trade-offs in natural interview language.

The structure is intentionally repetitive:

- Topic theory
- Questions commonly reported in interview preparation resources and forums
- Variations in wording
- Natural answers
- Follow-ups
- Mistakes
- Checklist

## Research Method

The guide was shaped from two directions:

1. Android/Kotlin fundamentals that senior developers are expected to know.
2. Publicly reported interview question patterns from Android interview repositories, Reddit discussions, public interview-prep sites, Android system design resources, and current official documentation.

Community and interview-question sources help identify how questions are phrased. Official documentation is used to anchor the theory.

Primary documentation used:

- [Kotlin null safety](https://kotlinlang.org/docs/null-safety.html)
- [Kotlin coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html)
- [Kotlin coroutine exception handling](https://kotlinlang.org/docs/exception-handling.html)
- [Kotlin Flow documentation](https://kotlinlang.org/docs/flow.html)
- [Kotlin generics](https://kotlinlang.org/docs/generics.html)
- [Android app architecture guide](https://developer.android.com/topic/architecture)
- [Android architecture recommendations](https://developer.android.com/topic/architecture/recommendations)
- [Kotlin flows on Android](https://developer.android.com/kotlin/flow)
- [Compose side effects](https://developer.android.com/develop/ui/compose/side-effects)
- [Android offline-first architecture](https://developer.android.com/topic/architecture/data-layer/offline-first)
- [Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test)
- [Android UI testing overview](https://developer.android.com/training/testing/ui-tests/behavior)
- [Android memory guide](https://developer.android.com/topic/performance/memory)
- [Android performance measurement overview](https://developer.android.com/topic/performance/measuring-performance)
- [Hilt with Jetpack libraries](https://developer.android.com/training/dependency-injection/hilt-jetpack)

Interview-pattern sources used:

- [mohsenoid/Android-Interview-Questions](https://github.com/mohsenoid/Android-Interview-Questions)
- [Android System Design FAQ](https://www.androidsystemdesign.dev/faq)
- [InterviewBee Android Developer question bank](https://interviewbee.ai/resources/role-based-questions/android-developer)
- [Reddit: Senior Android interview checklist discussion](https://www.reddit.com/r/androiddev/comments/13yv1tt)
- [Reddit: Senior interview discussion](https://www.reddit.com/r/androiddev/comments/1r8nkex/senior_interview/)
- [Reddit: experienced Android developer knowledge discussion](https://www.reddit.com/r/androiddev/comments/1r2zy9w/what_should_an_experienced_android_developer/)
- [Reddit: Compose UI state questions](https://www.reddit.com/r/androiddev/comments/1nnqe51)
- [Reddit: Android concurrency interview review](https://www.reddit.com/r/androiddev/comments/1tcgqsz/amo_concurrency_android_interview_review/)

The exact wording below is paraphrased and consolidated from recurring public patterns rather than copied from a single source.

---

## 1. Kotlin Type System and Null Safety

### Why This Appears In Senior Interviews

Kotlin is the default language for modern Android development, and null safety is one of the main reasons teams migrated from Java. Senior interviewers often start with simple nullability questions, then push into platform types, generics, Java interop, initialization, and API design.

### Concise Theory

Kotlin separates nullable and non-nullable types at the type-system level. A `String` cannot hold `null`; a `String?` can. This forces the developer to handle uncertainty explicitly through safe calls, smart casts, Elvis expressions, safe casts, nullable receivers, or controlled assertions.

This does not mean Kotlin eliminates all null pointer exceptions. NPEs can still happen through `!!`, Java interop, initialization leaks, generic type holes, explicit throws, and platform types coming from Java APIs.

The important senior-level idea is this: nullability is not only syntax. It is a contract. When you expose `T?`, callers must handle absence. When you expose `T`, you are promising a valid value. The quality of that contract matters in repositories, ViewModels, UI state, DTO mapping, and public APIs.

### Core Concepts

- Nullable vs non-nullable types: `T` vs `T?`.
- Safe call: `?.`
- Elvis operator: `?:`
- Not-null assertion: `!!`
- Smart casts after checks.
- `lateinit` vs nullable properties vs constructor injection.
- Platform types from Java: values where Kotlin cannot fully know nullability.
- Nullability in collections: `List<String?>` is not the same as `List<String>?`.
- Nullability in generics and Java interop.

### Interview Questions

- How does Kotlin handle null safety?
- Can a Kotlin app still crash with a NullPointerException?
- What is the difference between `String`, `String?`, and `String!`?
- When would you use `!!`?
- What is a platform type?
- What is the difference between `lateinit var`, `lazy`, and a nullable property?
- How do you model an optional value in UI state?
- What is the difference between an empty list and a null list?

### Variations In Wording

- "If Kotlin is null-safe, why do we still see NPEs?"
- "How do you avoid `!!` in production code?"
- "What happens when a Java method returns null into Kotlin?"
- "Would you return null or an empty list from a repository?"
- "How would you represent loading, content, empty, and error states?"

### Natural Interview Answer

"Kotlin makes nullability explicit in the type system. If I have `String`, the compiler treats it as always present; if I have `String?`, I have to handle the missing case before using it. That catches a lot of issues at compile time, but it does not make NPEs impossible. They can still come from `!!`, Java platform types, bad initialization, or generics. In production code I try to make nullability part of the API contract: if absence is meaningful, I expose it clearly; if not, I prefer a non-null value, an empty collection, or a sealed state depending on the domain."

### Deeper Follow-Ups

**When is `!!` acceptable?**

"Rarely. I would use it only when the invariant is guaranteed outside the compiler's visibility and failing fast is better than hiding a bug. Even then, I prefer `requireNotNull`, a clear guard, or redesigning the type so the compiler can help."

**What is a platform type?**

"It is a type coming from Java where Kotlin does not know if it is nullable or not. The compiler lets you treat it as nullable or non-nullable, which is convenient but risky. Around Java boundaries I usually normalize the value quickly, either by checking it, mapping it, or wrapping the API."

**Empty list or null list?**

"If the request succeeded and there are no items, I prefer an empty list. If the data is not loaded yet, unavailable, or failed, that should be modeled separately. A null list often mixes several states into one value."

### Common Mistakes

- Saying Kotlin prevents all NPEs.
- Treating `!!` as normal syntax instead of a last resort.
- Returning `null` for every absence case instead of modeling domain state.
- Not distinguishing `List<T?>` from `List<T>?`.
- Forgetting Java interop and Android framework APIs can weaken null guarantees.

### Checklist

- Can I explain why Kotlin is null-safe but not NPE-proof?
- Can I explain platform types?
- Can I model absence without overusing null?
- Can I discuss `lateinit`, `lazy`, constructor injection, and nullable properties?

---

## 2. Kotlin Classes, Data Classes, Sealed Types, Objects, and Value Classes

### Why This Appears In Senior Interviews

These features shape how Android teams model UI state, network results, domain entities, one-off events, configuration, and dependency boundaries. Interviewers want to see that you choose language constructs based on semantics, not fashion.

### Concise Theory

Kotlin gives several modeling tools:

- `data class` for immutable-ish value containers with generated equality, `copy`, `toString`, and destructuring.
- `sealed class` or `sealed interface` for restricted hierarchies, often used for UI state, results, navigation events, and domain outcomes.
- `object` for a singleton instance.
- `companion object` for members tied to a class rather than an instance.
- `enum class` for a fixed set of constant values.
- `value class` for type-safe wrappers that may avoid allocation in many cases.

Senior-level usage is about picking the construct that expresses the domain correctly. A sealed hierarchy is often better than multiple nullable fields or string constants because the compiler can help enforce exhaustive handling.

### Core Concepts

- Structural equality in data classes.
- `copy()` and immutable UI state updates.
- Shallow copy behavior.
- Sealed hierarchies and exhaustive `when`.
- `object` lifecycle and global state risks.
- `enum` vs sealed class.
- Inline/value classes for typed IDs and domain primitives.

### Interview Questions

- What is a data class and when should you not use one?
- What does `copy()` do in a data class?
- What is the difference between sealed class, enum, and abstract class?
- How would you model loading/error/success UI state?
- What is an `object` in Kotlin?
- What is a value class and why would you use one?

### Variations In Wording

- "Why not just use booleans like `isLoading` and `hasError`?"
- "What happens if a data class contains a mutable list?"
- "How do you force all UI states to be handled?"
- "Would you use enum or sealed class for API result?"

### Natural Interview Answer

"I use data classes when the object is mainly a value: state, DTOs, or simple domain data. For states with mutually exclusive branches, I prefer sealed types because they make impossible states harder to represent. For example, instead of `isLoading`, `error`, and `data` all being nullable or conflicting, I would model `Loading`, `Content`, and `Error` as separate states. That makes the UI code clearer and lets `when` help me handle every case."

### Deeper Follow-Ups

**What methods does a data class generate?**

"For primary constructor properties, Kotlin generates `equals`, `hashCode`, `toString`, `copy`, and `componentN` functions for destructuring. Properties declared in the class body are not included in those generated methods."

**How does generated `equals` work?**

"Conceptually it checks reference equality first, then type, then compares each primary-constructor property in order. It short-circuits when one property differs. For `n` properties, worst case is up to `n` property comparisons after the initial checks, but the real cost depends on the property type. Comparing two lists, for example, can compare their elements."

**When is `hashCode` used?**

"Hash-based collections use it: `HashMap`, `HashSet`, map keys, set membership, and operations such as `distinct` or `groupBy`. The hash narrows the lookup bucket; `equals` confirms the actual match. If two objects are equal, they must have the same hash code, but same hash code does not guarantee equality because collisions exist."

**Is `data class.copy()` deep?**

"No. It is shallow. If a property is a mutable collection or mutable object, both copies can still point to the same underlying instance. For UI state I prefer immutable collections or replacing the whole value."

**Sealed class vs enum?**

"An enum is good for fixed constants with the same shape. A sealed hierarchy is better when each case may carry different data or behavior."

### Common Mistakes

- Assuming data classes make everything deeply immutable.
- Forgetting that `==` calls `equals`, `===` checks reference identity, and `::` is a callable reference.
- Using mutable data classes as `HashMap` keys or `HashSet` items when the mutable property participates in `hashCode`.
- Using nullable fields where a sealed model would express state better.
- Using global `object` state for things that should be injected.
- Using enum for cases that need different payloads.

### Checklist

- Can I explain shallow copy?
- Can I model UI state with sealed types?
- Can I explain enum vs sealed?
- Can I spot impossible states in a bad model?

---

## 3. Kotlin Functions, Lambdas, Scope Functions, Inline, and Reified Generics

### Why This Appears In Senior Interviews

Kotlin-heavy Android code relies on higher-order functions, lambdas, extension functions, DSLs, Compose APIs, Flow operators, and DI helpers. Senior candidates need to explain these without turning Kotlin into Java with different syntax.

### Concise Theory

Functions are first-class in Kotlin. You can pass behavior as values, define extension functions, use lambdas with receivers, and build concise APIs. Scope functions such as `let`, `run`, `also`, `apply`, and `with` are convenience tools, but overusing them can hide intent.

`inline` asks the compiler to copy the function body at call sites. This can reduce allocation overhead for higher-order functions and enables `reified` type parameters. Normal generic type information is erased at runtime on the JVM; an inline function with a `reified` type parameter can access the type at the call site.

### Core Concepts

- Function types and higher-order functions.
- Lambda with receiver.
- Extension functions do not modify the class; they are statically resolved.
- Scope functions and intent.
- Inline functions and lambda allocation.
- `noinline` and `crossinline`.
- Type erasure and `reified`.
- Generics variance: `out` produces, `in` consumes.

### Interview Questions

- What are extension functions?
- Are extension functions polymorphic?
- What is the difference between `let`, `apply`, `also`, `run`, and `with`?
- What does `inline` do?
- Why does `reified` require `inline`?
- What is type erasure?
- Explain `in` and `out` in Kotlin generics.

### Variations In Wording

- "Can an extension function override a member function?"
- "Why can Retrofit or navigation helpers use `reified T`?"
- "What does PECS mean and how does it translate to Kotlin?"
- "When would too many scope functions make code worse?"

### Natural Interview Answer

"Extension functions let me add call-site convenience to a type without changing the type itself. They are resolved statically, so I do not treat them as virtual overrides. For generics, the JVM erases type parameters at runtime, so normally I cannot ask for `T::class` inside a generic function. If the function is inline and `T` is reified, the compiler substitutes the actual type at the call site, which is why helpers like `fromJson<T>()` can be ergonomic."

### Deeper Follow-Ups

**What does `out` mean?**

"`out T` means the type is covariant: it is safe to produce `T` values. A `Producer<Dog>` can be used where `Producer<Animal>` is expected. The rule of thumb is that `out` is for reading/producing."

**What does `in` mean?**

"`in T` means the type is contravariant: it is safe to consume `T` values. A `Consumer<Animal>` can be used where `Consumer<Dog>` is expected, because it can accept any dog as an animal."

**When not to use scope functions?**

"If a scope function makes ownership, return value, or receiver unclear, I avoid it. The goal is readability, not fewer lines."

### Common Mistakes

- Thinking extension functions override class members.
- Using `let`/`apply` chains that obscure what object is being modified.
- Saying `inline` is always a performance win.
- Thinking Kotlin has fully reified generics everywhere.
- Confusing covariance and contravariance.

### Checklist

- Can I explain extension function dispatch?
- Can I explain type erasure and reified generics?
- Can I explain `in` and `out` naturally?
- Can I choose scope functions based on intent?

---

## 4. Coroutines, Structured Concurrency, Dispatchers, and Cancellation

### Why This Appears In Senior Interviews

Coroutines are central to modern Android. Interview reports repeatedly mention lifecycle-aware concurrency, `viewModelScope`, cancellation, exception handling, `launch` vs `async`, dispatcher choices, and avoiding leaks.

### Concise Theory

A coroutine is a lightweight unit of asynchronous work that can suspend without blocking a thread. Coroutines still run on threads, but suspension lets the thread do other work while the coroutine waits.

Structured concurrency means coroutines are launched within a scope that controls their lifetime. Child coroutines are tied to parent scopes. This makes cancellation, cleanup, and error propagation more predictable.

On Android, common scopes include `viewModelScope`, `lifecycleScope`, and controlled application or repository scopes when work must outlive a screen. `GlobalScope` is usually a smell because it detaches work from lifecycle and ownership.

Dispatchers decide where coroutine code runs:

- `Dispatchers.Main` for UI work.
- `Dispatchers.IO` for blocking I/O.
- `Dispatchers.Default` for CPU-heavy work.
- Test dispatchers for deterministic tests.

Cancellation is cooperative. Suspending functions check cancellation naturally, but CPU loops must check `isActive`, call `yield`, or otherwise cooperate.

### Core Concepts

- `suspend` does not mean background thread.
- `launch` returns `Job`; `async` returns `Deferred`.
- `withContext` switches context and returns a result.
- Scope ownership matters.
- Cancellation propagates through parent-child relationships.
- `SupervisorJob` changes child failure behavior.
- Never block the main thread.
- Inject dispatchers for testability.

### Interview Questions

- What is a coroutine?
- What is structured concurrency?
- What is the difference between `launch`, `async`, and `withContext`?
- What happens to a coroutine in `viewModelScope` when the ViewModel is cleared?
- What is the difference between `Dispatchers.IO` and `Dispatchers.Default`?
- Why is `GlobalScope` discouraged?
- How does coroutine cancellation work?
- How do you avoid memory leaks with coroutines?

### Variations In Wording

- "User leaves the screen while a network call is running. What happens?"
- "Does `suspend` automatically move work off the main thread?"
- "How would you run two network calls in parallel?"
- "If one child coroutine fails, what happens to siblings?"
- "Where would you launch work that must finish even if the screen closes?"

### Natural Interview Answer

"A coroutine is a way to write async code sequentially without blocking the thread while it waits. The important part in Android is not just launching a coroutine, but launching it in the right scope. If I use `viewModelScope`, work is cancelled when the ViewModel is cleared, so I do not update dead UI state. If the work must survive the screen, I would move ownership to a repository, application-level scope, or WorkManager depending on the guarantee needed. I also do not assume `suspend` means background thread; if the code does blocking I/O, I explicitly use the right dispatcher or call an API that already handles it."

### Deeper Follow-Ups

**`launch` vs `async`?**

"I use `launch` for fire-and-forget work inside a scope where I care about completion through the `Job`. I use `async` when I need a result through `await`, especially for parallel decomposition. I avoid `async` if I never await it, because then it is usually the wrong abstraction."

**What happens when one child fails?**

"In a normal scope, an unhandled child failure cancels the parent and siblings. If I want siblings to fail independently, I use supervisor semantics, such as `supervisorScope` or a `SupervisorJob`, and handle errors at the right level."

**How do you cancel CPU-heavy work?**

"Suspension points check cancellation, but a tight CPU loop may not suspend. I would check `isActive`, call `yield`, or design the work in chunks so cancellation can be observed."

### Common Mistakes

- Treating coroutines as threads.
- Saying `suspend` means "runs in background."
- Using `GlobalScope` for screen work.
- Forgetting cancellation is cooperative.
- Blocking inside `Dispatchers.Main`.
- Using `async` without `await`.
- Catching `CancellationException` and swallowing it accidentally.

### Checklist

- Can I explain structured concurrency?
- Can I explain scope ownership on Android?
- Can I choose between `launch`, `async`, and `withContext`?
- Can I explain cancellation and supervisor behavior?

---

## 5. Coroutine Exception Handling

### Why This Appears In Senior Interviews

Senior Android interviews often turn basic coroutine knowledge into failure scenarios: one request fails, another should continue; a ViewModel emits errors; an exception disappears inside `async`; a `CoroutineExceptionHandler` does not catch what the candidate expects.

### Concise Theory

Exception behavior depends on coroutine builder and scope.

`launch` propagates unhandled exceptions to the parent. In a root coroutine, they are handled by the default uncaught exception mechanism or a `CoroutineExceptionHandler`.

`async` captures exceptions inside its `Deferred`; the exception is observed when `await()` is called. A `CoroutineExceptionHandler` does not behave like a normal `try/catch` around every child coroutine.

In structured concurrency, child failure normally cancels the parent and siblings. Supervisor scopes allow children to fail independently, but that does not mean errors disappear. You still need a deliberate error-handling strategy.

Cancellation uses `CancellationException`, which should generally be allowed to propagate.

### Core Concepts

- `launch` vs `async` exception behavior.
- Parent-child exception propagation.
- `CoroutineExceptionHandler` works mainly for uncaught exceptions in root coroutines.
- `supervisorScope` and `SupervisorJob`.
- `try/catch` around suspending calls.
- Preserve cancellation.

### Interview Questions

- How do exceptions work in coroutines?
- Why did my `CoroutineExceptionHandler` not catch this error?
- What happens if one `async` fails?
- How would you handle multiple parallel requests where one may fail?
- What is `supervisorScope`?
- Should you catch `CancellationException`?

### Variations In Wording

- "I put a `CoroutineExceptionHandler` in the scope, but the app still crashed. Why?"
- "If one API call fails, should all calls cancel?"
- "How do you show an error in the UI without killing the whole scope?"
- "What is the difference between `coroutineScope` and `supervisorScope`?"

### Natural Interview Answer

"I treat coroutine errors based on ownership and whether the work is all-or-nothing. In a normal structured scope, a child failure cancels the parent and siblings, which is good when the tasks belong to the same operation. If the tasks are independent, I use supervisor semantics and handle each result explicitly. I also remember that `async` stores the exception until `await`, while `launch` propagates unhandled exceptions. For UI, I usually catch domain-level failures in the ViewModel or use a result type so the UI state can represent error cleanly."

### Deeper Follow-Ups

**`coroutineScope` vs `supervisorScope`?**

"`coroutineScope` treats children as one unit: if one fails, the scope fails. `supervisorScope` lets child failures be handled independently. I choose based on whether the operation is atomic or partially useful."

**Should you catch all exceptions in a repository?**

"Not blindly. A repository can map expected failures, like network or parsing errors, into domain results. But swallowing all exceptions can hide bugs and cancellation. I avoid catching `Throwable` unless I rethrow cancellation and have a very specific boundary."

### Common Mistakes

- Expecting `CoroutineExceptionHandler` to replace `try/catch`.
- Forgetting to call `await()` on `async`.
- Swallowing `CancellationException`.
- Using supervisor semantics without any error reporting.
- Turning every exception into a generic "unknown error" too early.

### Checklist

- Can I explain `launch` and `async` exception differences?
- Can I explain `supervisorScope`?
- Can I preserve cancellation correctly?
- Can I design error handling for partial failure?

---

## 6. Flow, StateFlow, SharedFlow, LiveData, and Reactive Streams

### Why This Appears In Senior Interviews

Flow is now a core Android architecture tool. Interviewers commonly ask about cold vs hot streams, `StateFlow` vs `SharedFlow`, lifecycle-aware collection, backpressure-ish behavior, `flowOn`, `catch`, `combine`, and one-off events.

### Concise Theory

`Flow` is a stream of values built on coroutines. A regular `Flow` is cold: the producer does not run until collection starts, and each collector usually gets its own execution.

`StateFlow` is a hot state holder. It always has a current value and is useful for UI state. It conflates updates, meaning collectors observe the latest state rather than every historical state.

`SharedFlow` is a hot broadcast stream configurable with replay and buffer behavior. It can be useful for events, but one-off UI events need careful lifecycle design to avoid loss or duplication.

`flowOn` changes the upstream context. `catch` catches upstream exceptions, not downstream collector exceptions unless the collector logic is moved upstream with operators like `onEach`.

On Android, collection should be lifecycle-aware. In Compose, prefer lifecycle-aware state collection where available.

### Core Concepts

- Cold Flow vs hot Flow.
- Terminal operators start collection.
- `StateFlow` for state.
- `SharedFlow` for shared emissions/events.
- `Channel` for one-consumer event streams in specific cases.
- `flowOn` affects upstream.
- `catch` catches upstream.
- `combine`, `zip`, `flatMapLatest`, `mapLatest`.
- Buffering, conflation, and cancellation.

### Interview Questions

- What is Flow?
- What is the difference between Flow, StateFlow, and SharedFlow?
- What is cold vs hot flow?
- How do you collect Flow safely in Android?
- What is the difference between `collect`, `collectLatest`, and `mapLatest`?
- Where does `flowOn` apply?
- Why does `catch` not catch my collector exception?
- How would you model UI state and one-time events?

### Variations In Wording

- "Should ViewModel expose LiveData or StateFlow?"
- "How would you implement search-as-you-type?"
- "How do you avoid collecting while the screen is stopped?"
- "StateFlow is not emitting duplicate values. Why?"
- "Should navigation events be part of UI state?"

### Natural Interview Answer

"I use Flow for async streams, especially between data/domain layers and the ViewModel. A normal Flow is cold, so it starts when collected. For UI state from the ViewModel, I usually expose `StateFlow` because the screen needs the latest state at any time. For one-off events, I am more careful: sometimes a `SharedFlow` is fine, but often navigation or snackbar effects are better modeled as part of state plus an acknowledgement, depending on lifecycle and replay requirements."

### Deeper Follow-Ups

**Flow vs StateFlow?**

"Flow describes a stream. StateFlow is a state holder with a current value. If the UI needs to render from the latest snapshot, StateFlow fits. If I am representing a sequence of work or values that starts on collection, regular Flow may be better."

**`collectLatest`?**

"It cancels the previous collector block when a new value arrives. It is useful for search queries or rendering work where only the latest value matters."

**`flowOn`?**

"It changes the context of upstream operators before it. It is the right way to move flow production work to another dispatcher; using `withContext` inside a `flow` builder can violate Flow context rules."

**`catch`?**

"`catch` handles exceptions upstream of where it is placed. If the exception is thrown inside `collect`, it is downstream and `catch` will not catch it unless I move that logic into `onEach` before `catch`."

### Common Mistakes

- Using SharedFlow for state.
- Using StateFlow for one-time events without thinking about replay and re-delivery.
- Collecting flows without lifecycle awareness.
- Misunderstanding where `flowOn` applies.
- Believing `catch` catches everything.
- Doing blocking work in flow operators on the wrong dispatcher.

### Mini Exercise

Explain how you would model a screen with:

- cached data from Room,
- network refresh,
- loading indicator,
- retry error,
- snackbar after save,
- navigation after success.

The important part is separating persistent UI state from transient effects.

### Checklist

- Can I explain cold vs hot?
- Can I choose StateFlow vs SharedFlow?
- Can I explain lifecycle-aware collection?
- Can I explain `flowOn`, `catch`, and `collectLatest`?

---

## 7. Android Lifecycle, ViewModel, SavedStateHandle, and Process Death

### Why This Appears In Senior Interviews

Android is lifecycle-heavy. Senior candidates are expected to understand not just Activity callbacks, but ownership: what survives rotation, what survives process death, when work is cancelled, and where state belongs.

### Concise Theory

The Android system can create, stop, destroy, and recreate components based on user navigation, configuration changes, memory pressure, and process death. A ViewModel survives configuration changes while its owner remains in the navigation back stack, but it does not survive process death as an object.

`SavedStateHandle` can store small pieces of state needed to recreate UI after process death. Persistent data belongs in durable storage such as Room, DataStore, or files. Large UI models should usually be reconstructed from repositories rather than saved wholesale.

Lifecycle-aware code avoids doing work when UI is not visible and avoids leaking destroyed views or activities.

### Core Concepts

- Activity/Fragment lifecycle.
- Configuration change vs process death.
- ViewModel lifetime.
- `SavedStateHandle`.
- `repeatOnLifecycle`.
- Avoiding references to `Activity`, `Fragment`, `View`, or `Context` in ViewModel.
- UI state restoration.
- Navigation back stack ownership.

### Interview Questions

- What is the role of ViewModel?
- What survives rotation?
- What survives process death?
- How do you handle state restoration?
- Why should a ViewModel not hold an Activity reference?
- What is `SavedStateHandle` for?
- How do you collect Flow safely with lifecycle?

### Variations In Wording

- "User rotates the phone during a request. What happens?"
- "The app is killed in the background and restored. What state do you expect?"
- "Where do you put selected tab, scroll position, form input, and cached entities?"
- "Why did this Fragment leak?"

### Natural Interview Answer

"I think of lifecycle in terms of ownership. The UI owns rendering and short-lived interaction. The ViewModel owns screen state and survives configuration changes. Persistent data belongs below that, usually in a repository backed by local storage or network. For process death, I do not rely on ViewModel objects still existing; I save the minimum state needed to restore or re-query, often with `SavedStateHandle`, and reconstruct the rest from the data layer."

### Deeper Follow-Ups

**What goes into `SavedStateHandle`?**

"Small, serializable restoration keys: IDs, filters, selected item, maybe form fields if needed. Not large lists, bitmaps, repositories, or complex object graphs."

**How do you avoid lifecycle leaks?**

"I avoid storing views or Activity references in longer-lived objects. I collect flows with lifecycle-aware APIs, cancel callbacks in the right lifecycle method, and keep ViewModel independent of lifecycle classes."

### Common Mistakes

- Saying ViewModel survives process death.
- Saving too much state in bundles.
- Holding `Context` or `View` in ViewModel.
- Launching long-lived work in Activity scope when it belongs elsewhere.
- Treating rotation and process death as the same problem.

### Checklist

- Can I explain ViewModel lifetime precisely?
- Can I distinguish rotation from process death?
- Can I decide what belongs in SavedStateHandle?
- Can I explain lifecycle-aware Flow collection?

---

## 8. Jetpack Compose State, Recomposition, Effects, and Performance

### Why This Appears In Senior Interviews

Compose is common in modern Android interviews, but many candidates know syntax without understanding state, recomposition, stability, side effects, and performance trade-offs. Forum discussions show repeated confusion around mutable lists, recomposition scope, and effects.

### Concise Theory

Compose is declarative: UI is described as a function of state. When state changes, Compose may re-invoke composable functions to produce updated UI. Recomposition can happen often, can be skipped, and can be cancelled. Composables should ideally be side-effect free.

State should be hoisted when a parent or caller needs control. The ViewModel usually exposes screen UI state; composables render it and send events upward. Local UI-only state can live in Compose with `remember` or `rememberSaveable`.

Effects such as `LaunchedEffect`, `DisposableEffect`, `SideEffect`, `produceState`, and `rememberUpdatedState` exist for controlled side effects. They should be used deliberately, not as a place to hide business logic.

Performance in Compose is often about state reads, recomposition scope, stable parameters, keys in lists, avoiding unnecessary allocations, and measuring before optimizing.

### Core Concepts

- Declarative UI.
- State drives UI.
- Recomposition.
- `remember` vs `rememberSaveable`.
- State hoisting.
- Unidirectional data flow.
- Stable vs unstable parameters.
- `LaunchedEffect` keys.
- `DisposableEffect` cleanup.
- `derivedStateOf` for derived state when useful.
- Lazy list keys.
- Avoiding business logic inside composables.

### Interview Questions

- What is recomposition?
- What triggers recomposition?
- What is state hoisting?
- What is the difference between `remember` and `rememberSaveable`?
- What is `LaunchedEffect` and when does it restart?
- How do you handle one-off events in Compose?
- How do you avoid unnecessary recomposition?
- Why is mutating a list in place often a problem in Compose?

### Variations In Wording

- "I changed a mutable list but the UI did not update. Why?"
- "Why is my `LaunchedEffect` running multiple times?"
- "Where should navigation happen: ViewModel or composable?"
- "How do you collect StateFlow in Compose?"
- "Why should composables be side-effect free?"

### Natural Interview Answer

"In Compose, I try to make UI a function of state. The ViewModel exposes state, the composable reads it, and user actions go back up as events. Recomposition is Compose re-running composables when observed state changes, but I do not rely on exact recomposition timing for correctness. For side effects, I use the effect APIs with stable keys. For example, if a coroutine should run when a screen ID changes, the screen ID should be the key. If the effect needs cleanup, I use `DisposableEffect`."

### Deeper Follow-Ups

**`remember` vs `rememberSaveable`?**

"`remember` keeps a value across recompositions while the composable remains in the composition. `rememberSaveable` also saves through configuration change and process recreation when the value can be saved. For important screen state, I still prefer ViewModel and persistence where appropriate."

**Mutable list issue?**

"If I mutate a regular mutable list in place, Compose may not see a new state value. I prefer immutable list updates, snapshot-aware state lists, or replacing the list in a state holder."

**`LaunchedEffect` keys?**

"The key defines when the effect should restart. A changing key restarts the coroutine; a constant key runs for the lifetime of that composition. Wrong keys cause repeated work or stale captures."

**How do you handle navigation events?**

"I avoid making the ViewModel directly depend on NavController. Usually the UI observes state or effects and calls navigation. The exact pattern depends on whether the event must survive configuration change, whether it can be repeated, and how the team models effects."

### Common Mistakes

- Putting business logic directly in composables.
- Using effects as a general-purpose event bus.
- Mutating state in place and expecting recomposition.
- Passing entire ViewModels deep into UI trees by habit.
- Using unstable keys in lazy lists.
- Assuming recomposition means redrawing everything.
- Optimizing recomposition without measuring.

### Mini Exercise

Explain a login screen in Compose:

- email and password input,
- validation,
- loading button,
- error message,
- navigation after success.

Focus on what lives in ViewModel state, what is local UI state, and how one-off navigation is handled.

### Checklist

- Can I explain recomposition without oversimplifying?
- Can I choose `remember`, `rememberSaveable`, or ViewModel state?
- Can I explain effect APIs and keys?
- Can I handle mutable state correctly?

---

## 9. Android Architecture: MVVM, MVI, Clean Architecture, Repositories, and UDF

### Why This Appears In Senior Interviews

Senior Android roles expect architectural judgment. Interviewers want to know how you structure large codebases, separate responsibilities, migrate legacy code, avoid overengineering, and keep features testable.

### Concise Theory

Modern Android architecture usually separates UI, state holders, domain/use cases when useful, repositories, and data sources. Android documentation emphasizes layered architecture, UI driven by data models, unidirectional data flow, ViewModels as state holders, coroutines/Flow, and dependency injection.

MVVM is common: View renders state and forwards events; ViewModel prepares UI state and coordinates use cases/repositories. MVI is stricter about state reduction and event handling. Clean Architecture adds boundaries around domain logic and dependencies.

Senior-level architecture is not about naming folders. It is about dependency direction, testability, ownership, lifecycle, change isolation, and avoiding impossible states.

### Core Concepts

- UI layer vs domain layer vs data layer.
- ViewModel as screen state holder.
- Repository as data abstraction, not a dumping ground.
- Data sources: remote, local, cache.
- Use cases/interactors when they add clarity.
- Unidirectional data flow.
- Single source of truth.
- Dependency inversion.
- Feature modules.
- Avoiding over-abstraction.

### Interview Questions

- Explain MVVM in Android.
- What is Clean Architecture?
- What is the role of a repository?
- When would you use use cases?
- What is unidirectional data flow?
- What is single source of truth?
- How would you migrate a legacy MVP app to modern architecture?
- How do you structure a large Android app?

### Variations In Wording

- "Where should business logic live?"
- "Is ViewModel part of the domain layer?"
- "Should every repository have an interface?"
- "How do you prevent ViewModel from becoming too large?"
- "How would you split modules for a large team?"

### Natural Interview Answer

"I care less about the acronym and more about clear ownership. The UI renders state and sends events. The ViewModel owns screen state and coordinates work. Repositories hide data-source details and expose domain-friendly data. If business rules become reusable or complex, I introduce use cases; if they are just pass-through wrappers, I avoid adding them mechanically. For larger apps, I also think about module boundaries, build time, and team ownership."

### Deeper Follow-Ups

**Repository role?**

"A repository should provide a clean API for data needed by the app. It can coordinate local and remote sources, caching, mapping, and sync policy. It should not become a random utility class or contain UI-specific decisions."

**Use cases always?**

"No. They are useful when they capture meaningful business operations, combine repositories, enforce rules, or improve testability. A one-line use case that only forwards a repository call may be unnecessary unless the project has a strict convention."

**MVI vs MVVM?**

"MVVM is a broad pattern around ViewModel state and binding. MVI is usually more explicit about events, reducers, immutable state, and one-way data flow. MVI can make complex screens predictable, but it can also add ceremony."

### Common Mistakes

- Reciting Clean Architecture without explaining dependency direction.
- Creating interfaces for every class without a reason.
- Putting Android framework types in domain models.
- Letting repositories know about UI state.
- Treating ViewModel as a place for everything.
- Using architecture as decoration rather than solving coupling.

### Mini Exercise

Design the layers for a "Saved Articles" feature:

- local cache,
- remote API,
- offline read,
- sync after login,
- Compose screen,
- tests.

Explain boundaries and data flow.

### Checklist

- Can I explain architecture by responsibility, not buzzwords?
- Can I justify use cases?
- Can I explain UDF and single source of truth?
- Can I describe migration from legacy architecture?

---

## 10. Offline-First, Local Persistence, Room, DataStore, and Sync

### Why This Appears In Senior Interviews

Mobile apps run on unreliable networks, limited battery, process death, and intermittent connectivity. Senior Android system design questions often involve offline-first behavior, caching, Room, conflict resolution, WorkManager, and synchronization.

### Concise Theory

Offline-first means the app remains useful when network is unavailable. A common pattern is local database as the source of truth, UI observes local data, network refresh updates local storage, and background work handles retries or synchronization.

Room is commonly used for structured relational local data. DataStore is used for small key-value or typed preference-like data. WorkManager is appropriate for deferrable persistent background work with constraints and retries.

Sync design must answer:

- What is the source of truth?
- What happens when reads fail?
- What happens when writes fail?
- Are writes queued?
- How are conflicts resolved?
- How are retries handled?
- What does the user see?

### Core Concepts

- Source of truth.
- Cache vs persistent local model.
- Room entities and migrations.
- DAO returning Flow.
- Transaction boundaries.
- DataStore vs SharedPreferences.
- WorkManager for persistent deferrable work.
- Exponential backoff.
- Conflict resolution.
- Idempotent writes.

### Interview Questions

- How would you design an offline-first app?
- Room vs DataStore vs SharedPreferences?
- How do you handle Room migrations?
- How would you sync local changes with the server?
- How do you handle conflicts?
- When should you use WorkManager?
- How do you expose cached data to the UI?

### Variations In Wording

- "User favorites an item offline. What happens?"
- "Network refresh fails but cached data exists. What should UI show?"
- "How do you avoid duplicate writes after retry?"
- "How do you migrate a database safely?"
- "Should repository return network data directly or database Flow?"

### Natural Interview Answer

"For offline-first, I usually make local storage the source of truth for the UI. The screen observes Room through Flow. Network refresh writes into Room, and the UI updates from the database instead of depending directly on the network response. For writes, I decide whether they must be immediate or can be queued. If they can be retried, I persist the pending operation and use WorkManager with constraints and backoff. Conflict handling depends on the product: last-write-wins, server authority, merge, or user resolution."

### Deeper Follow-Ups

**Room migration strategy?**

"I treat migrations as part of the release. I write explicit migrations for schema changes, test them with representative old schemas, and avoid destructive migration unless data loss is acceptable. For complex migrations, I separate schema evolution from data backfill where possible."

**DataStore vs Room?**

"Room is for structured relational data and queryable models. DataStore is for small preferences or typed settings. I would not store a large relational cache in DataStore."

**WorkManager vs coroutine?**

"A coroutine is tied to its scope and process. WorkManager is for deferrable work that should survive process death and respect constraints. If the work must reliably happen later, WorkManager is the better fit."

### Common Mistakes

- Calling any cache "offline-first."
- Making UI depend directly on network responses while also having a database.
- Not persisting pending writes.
- Ignoring idempotency and duplicate retries.
- Using WorkManager for immediate UI work.
- Avoiding migration tests.

### Mini Exercise

Design offline favorite/unfavorite:

- user toggles favorite offline,
- UI updates optimistically,
- app process dies,
- network returns conflict,
- user logs out.

Explain what is stored, retried, rolled back, or reconciled.

### Checklist

- Can I design local source of truth?
- Can I explain queued writes and retries?
- Can I justify Room vs DataStore?
- Can I explain WorkManager ownership?

---

## 11. Networking, Retrofit, OkHttp, Serialization, and API Error Design

### Why This Appears In Senior Interviews

Android apps are network clients. Senior interviews often ask about API layering, error handling, interceptors, retries, cancellation, serialization, pagination, authentication, and mapping DTOs to domain models.

### Concise Theory

Retrofit defines type-safe HTTP APIs. OkHttp handles HTTP execution, interceptors, connection pooling, caching, and lower-level concerns. Serialization libraries map JSON to DTOs.

Senior-level networking is not just "call API." It includes:

- cancellation tied to coroutine scope,
- mapping DTOs away from UI/domain when useful,
- clear error classification,
- authentication refresh,
- retry policy,
- pagination,
- timeouts,
- observability,
- avoiding duplicate requests,
- offline/cache behavior.

### Core Concepts

- DTO vs domain model vs UI model.
- HTTP status codes vs network exceptions vs parsing errors.
- Interceptors: application vs network.
- Auth token refresh.
- Idempotent retries.
- Pagination and cache invalidation.
- Timeout and cancellation.
- OkHttp cache vs app-level cache.
- Multipart and large downloads/uploads.

### Interview Questions

- How do Retrofit and OkHttp work together?
- How do you handle API errors?
- Where do you map DTOs to domain models?
- How do you implement token refresh?
- How do you prevent duplicate network requests?
- How do you handle pagination?
- How do you handle cancellation when user leaves the screen?

### Variations In Wording

- "API returns 200 with an error body. What do you do?"
- "Refresh token request fails. How do you avoid infinite loops?"
- "Would you retry all failed requests?"
- "How do you handle slow network and timeout?"
- "Where should JSON parsing exceptions be handled?"

### Natural Interview Answer

"I separate transport errors, HTTP errors, parsing errors, and domain errors. Retrofit and OkHttp give me the raw network boundary, but I usually map that into a result the rest of the app understands. For authentication, I centralize token attachment and refresh carefully so concurrent 401s do not trigger multiple refreshes or infinite retry loops. I also avoid retrying blindly; retries should be limited, usually idempotent, and aware of the user experience."

### Deeper Follow-Ups

**Where to map DTOs?**

"Usually near the data layer boundary. DTOs represent the API contract, not necessarily my domain. Mapping prevents API shape from leaking everywhere and gives me one place to handle missing fields or version differences."

**Token refresh concurrency?**

"I would serialize refresh work, make waiting requests share the result, avoid refreshing the refresh endpoint itself, and clear auth state if refresh fails with an unrecoverable error."

**Retry policy?**

"I retry only when it is safe and useful: transient network failures, selected 5xx responses, idempotent operations, with backoff. For non-idempotent writes, I need request IDs or server support to avoid duplicates."

### Common Mistakes

- Treating all errors as the same.
- Retrying POST requests blindly.
- Leaking DTOs into UI by default.
- Doing token refresh in every repository manually.
- Ignoring cancellation.
- Assuming HTTP cache solves offline-first requirements.

### Checklist

- Can I classify network errors?
- Can I design token refresh safely?
- Can I explain DTO mapping?
- Can I discuss retry and idempotency?

---

## 12. Dependency Injection: Hilt, Dagger, Koin, and Testability

### Why This Appears In Senior Interviews

DI affects architecture, testability, build time, modularity, and lifecycle ownership. Android senior candidates are often asked about Hilt scopes, ViewModel injection, Worker injection, and why DI matters beyond "less boilerplate."

### Concise Theory

Dependency Injection means dependencies are provided from the outside rather than constructed internally. This makes classes easier to test, configure, and compose. Hilt is the standard Jetpack-integrated DI solution built on Dagger. Dagger/Hilt generate code at compile time. Koin is a runtime DI/service-locator style framework popular for simpler setup.

Important Android DI questions are about scopes:

- application-wide singletons,
- Activity/Fragment scoped objects,
- ViewModel scoped objects,
- Worker dependencies,
- test replacements.

Constructor injection is usually preferred. Module provider methods are useful when constructing dependencies you do not own or that require special setup.

### Core Concepts

- Constructor injection.
- Provider modules.
- Scopes and component lifetimes.
- Qualifiers.
- Hilt ViewModel integration.
- Worker injection.
- Test modules/fakes.
- DI vs Service Locator.
- Compile-time vs runtime dependency resolution.

### Interview Questions

- What is dependency injection?
- Why use Hilt/Dagger?
- Hilt vs Dagger vs Koin?
- What are scopes in Hilt?
- How do you inject a ViewModel?
- How do you inject WorkManager workers?
- How do you replace dependencies in tests?
- What is the difference between constructor injection and provider methods?

### Variations In Wording

- "Why not just instantiate dependencies directly?"
- "What should be a singleton?"
- "How do you inject different dispatchers?"
- "How do you avoid leaking Activity with singleton dependencies?"
- "Why is DI useful for testing?"

### Natural Interview Answer

"DI gives ownership and construction to the composition layer instead of scattering `new` calls across the app. In Android, that matters because dependencies often have different lifetimes. A singleton repository is not the same as a ViewModel-scoped object or an Activity-scoped object. With Hilt, I prefer constructor injection where possible, use modules for things I cannot construct directly, and use qualifiers for multiple instances like dispatchers or Retrofit clients."

### Deeper Follow-Ups

**What should be singleton?**

"Only dependencies that are safe and intended to live for the app process: stateless services, repositories when appropriate, database instance, Retrofit/OkHttp clients. I would not singleton-scope an object that holds Activity, View, or screen-specific state."

**Hilt vs Koin?**

"Hilt/Dagger give compile-time graph validation and strong Android integration, at the cost of annotation processing and some complexity. Koin is simpler and flexible, but errors can surface at runtime. I choose based on team size, app complexity, build constraints, and existing stack."

### Common Mistakes

- Calling DI only "for testing."
- Making everything singleton.
- Injecting Activity context into long-lived objects.
- Using modules when constructor injection would be cleaner.
- Not qualifying dispatchers or Retrofit clients.
- Ignoring DI graph cost in large modular apps.

### Checklist

- Can I explain DI in terms of ownership?
- Can I explain scopes and lifetimes?
- Can I compare Hilt, Dagger, and Koin fairly?
- Can I describe test dependency replacement?

---

## 13. Testing Strategy: Unit, Integration, UI, Compose, Coroutines, and Fakes

### Why This Appears In Senior Interviews

Senior developers are expected to design test strategy, not just write tests. Interviewers ask how to test ViewModels, Flows, repositories, Room migrations, Compose UI, and coroutine code deterministically.

### Concise Theory

Android testing exists at multiple levels:

- Unit tests for pure Kotlin logic, ViewModels, use cases, mappers.
- Integration tests for repositories, database, API boundaries, DI wiring.
- UI tests for user behavior in Views or Compose.
- End-to-end tests for critical flows when worth the cost.

Coroutine tests need deterministic dispatchers and virtual time. `runTest` provides a test coroutine scope and can skip delays. Code that hardcodes `Dispatchers.Main` or creates unmanaged scopes is harder to test.

Good tests use fakes when behavior matters. Mocks are useful, but over-mocking implementation details makes tests brittle.

### Core Concepts

- Test pyramid adjusted for mobile cost.
- Fakes vs mocks.
- `runTest`.
- `StandardTestDispatcher` vs `UnconfinedTestDispatcher`.
- Replacing Main dispatcher in local tests.
- Testing Flow emissions.
- Compose UI tests.
- Espresso synchronization.
- Robolectric.
- Room migration tests.

### Interview Questions

- How do you test a ViewModel with coroutines?
- How do you test Flow emissions?
- How do you test Compose UI?
- What is the difference between unit, integration, and UI tests?
- How do you test Room migrations?
- How do you make coroutine code testable?
- Mocks vs fakes?

### Variations In Wording

- "My coroutine test is flaky. Why?"
- "How do you test loading then success state?"
- "Would you test ViewModel and Compose together?"
- "How do you avoid waiting real time in coroutine tests?"
- "How much UI testing is worth it?"

### Natural Interview Answer

"I try to put most logic in testable Kotlin classes and ViewModels, then cover key integrations and only the most important UI flows. For coroutines, I use `runTest`, inject dispatchers or scopes where needed, and avoid real delays. For Flow, I assert emissions with controlled collection and cancellation. For UI, Compose and Espresso can test behavior, but I keep UI tests focused because they are more expensive to maintain."

### Deeper Follow-Ups

**Fake vs mock?**

"A fake has working behavior, usually simplified. A mock verifies interactions. For repositories or data sources, fakes often make tests more realistic and less brittle. Mocks are useful for narrow boundaries or when I care that a collaborator was called."

**Testing ViewModel state?**

"I drive the ViewModel through public events, control dispatcher execution, collect its state, and assert meaningful states: initial, loading, success, error. I avoid testing private methods."

**Testing Compose?**

"I prefer testing visible behavior and semantics, not implementation details. Good semantic tags and accessible UI make Compose tests cleaner."

### Common Mistakes

- Hardcoding dispatchers.
- Using real delays in tests.
- Testing implementation details instead of behavior.
- Overusing mocks for everything.
- Having many brittle UI tests with low value.
- Forgetting to cancel never-ending flows in tests.

### Checklist

- Can I test coroutine code deterministically?
- Can I test Flow and ViewModel state?
- Can I explain fakes vs mocks?
- Can I design a balanced mobile test strategy?

---

## 14. Android Performance, Memory, Startup, ANRs, and Profiling

### Why This Appears In Senior Interviews

Performance questions reveal whether a candidate can diagnose real production issues. Senior interviews often ask about jank, ANRs, memory leaks, app startup, RecyclerView/Compose performance, image loading, and profiling tools.

### Concise Theory

Android performance is user-perceived responsiveness under resource constraints. Common problem categories:

- Main-thread blocking causing jank or ANRs.
- Excessive recomposition or layout work.
- Slow startup due to eager initialization, I/O, dependency graph cost, or ContentProviders.
- Memory leaks from long-lived references to short-lived objects.
- Excess allocations and GC pressure.
- Large images or unbounded caches.
- Inefficient database queries.
- Network work without caching or pagination.

Senior-level performance work starts with measurement. Use profilers, traces, benchmarks, Android Vitals, logs, and production metrics. Guessing can waste time.

### Core Concepts

- Main thread and frame deadlines.
- ANR causes.
- Memory leaks and lifecycle references.
- Android Studio profiler.
- Perfetto/System Trace.
- Baseline profiles.
- Macrobenchmark and startup measurement.
- Lazy initialization.
- Image loading and caching.
- Pagination.
- Database query performance.

### Interview Questions

- How do you investigate app jank?
- What causes ANRs?
- How do you detect memory leaks?
- How do you improve cold start?
- How do you optimize a slow Compose screen?
- What tools do you use for performance?
- How do you handle large images or lists?

### Variations In Wording

- "The app freezes when opening the home screen. What do you check?"
- "Users report slow startup after a release. How do you debug?"
- "How do you know if a leak is real?"
- "RecyclerView/Compose list scrolls badly. What now?"
- "Would you optimize code before measuring?"

### Natural Interview Answer

"I start by reproducing and measuring. If it is jank, I look at main-thread work, rendering, layout/recomposition, I/O, and allocation pressure using profiler or traces. If it is startup, I check eager initialization, ContentProviders, dependency graph creation, disk I/O, and network work during launch. For memory, I look for retained Activity/View references and use tools like the memory profiler or LeakCanary. I try to connect local traces with production signals because a fast test device can hide real user pain."

### Deeper Follow-Ups

**ANR?**

"An ANR happens when the main thread cannot respond in time. Causes include blocking I/O, long computation, deadlocks, synchronous binder calls, or waiting on locks. The fix depends on trace evidence."

**Cold start optimization?**

"I delay non-critical initialization, move blocking work off the startup path, reduce dependency graph cost, avoid unnecessary ContentProviders, measure time-to-initial-display, and consider Baseline Profiles for startup and critical paths."

**Compose performance?**

"I check state read scope, unstable parameters, list keys, expensive work during composition, unnecessary allocations, image loading, and whether recomposition is actually the bottleneck. I measure before changing architecture."

### Common Mistakes

- Optimizing without measuring.
- Blaming Compose or coroutines generically.
- Doing disk/network work on main thread.
- Ignoring production device diversity.
- Holding Activity references in singletons.
- Treating all GC as a fatal performance issue.

### Checklist

- Can I explain ANR diagnosis?
- Can I describe startup profiling?
- Can I detect lifecycle leaks?
- Can I discuss Compose/list performance with measurement?

---

## 15. Android Background Work: WorkManager, Services, Broadcasts, and Alarms

### Why This Appears In Senior Interviews

Mobile background execution is constrained and changes across Android versions. Senior candidates must know when to use WorkManager, foreground services, exact alarms, push notifications, or simple coroutines.

### Concise Theory

Background work should match the guarantee required:

- Coroutine in a scope: in-process async work tied to owner lifetime.
- WorkManager: deferrable, persistent work that should survive process death and can run with constraints.
- Foreground service: user-visible ongoing work that must continue immediately.
- AlarmManager: time-sensitive scheduled work, especially exact timing when justified.
- Push notifications/server-driven sync: often better than polling.

WorkManager is not for immediate UI tasks. Foreground services require a visible notification and policy compliance.

### Core Concepts

- Deferrable vs immediate work.
- Persistent vs in-memory work.
- Constraints: network, charging, idle.
- Unique work.
- Backoff and retry.
- Foreground service restrictions.
- Broadcast receiver limits.
- Doze and battery optimization.

### Interview Questions

- When do you use WorkManager?
- WorkManager vs coroutine?
- WorkManager vs foreground service?
- How do you handle periodic sync?
- How do you retry failed background work?
- How do you make background work idempotent?
- How do you inject dependencies into Workers?

### Variations In Wording

- "Upload should continue after the user leaves the app. What do you use?"
- "User starts music playback. WorkManager or service?"
- "Sync data once network returns. How?"
- "Why did background work stop on newer Android versions?"

### Natural Interview Answer

"I choose background APIs based on ownership and guarantees. If the work is only needed while the screen exists, a lifecycle or ViewModel coroutine is enough. If it must survive process death and can be deferred, WorkManager is a good fit. If it is immediate and user-visible, like navigation or active recording, a foreground service may be appropriate. I also design retries to be idempotent, because Android may rerun work."

### Deeper Follow-Ups

**Periodic sync?**

"I avoid aggressive polling. If sync is needed, I use WorkManager with constraints and reasonable intervals, or push/server signals where possible. The UI should still be able to refresh on demand."

**Unique work?**

"Unique work helps avoid duplicate jobs. I choose keep, replace, or append behavior based on whether a new request supersedes old work or should be queued."

### Common Mistakes

- Using WorkManager for immediate UI work.
- Using coroutine when process-death survival is required.
- Ignoring idempotency.
- Forgetting foreground service notification requirements.
- Retrying forever without backoff or limits.

### Checklist

- Can I choose between coroutine, WorkManager, and foreground service?
- Can I explain constraints and retries?
- Can I design idempotent background work?

---

## 16. Security, Privacy, and Mobile-Specific Risk

### Why This Appears In Senior Interviews

Senior mobile developers handle tokens, PII, local storage, network security, deep links, WebViews, logs, and reverse-engineering risk. Even if the role is not security-focused, fundamentals matter.

### Concise Theory

Mobile security is layered. You cannot make a client fully trusted because it runs on user-controlled devices. The goal is to reduce risk:

- protect sensitive local data,
- use TLS and correct network config,
- avoid logging secrets,
- validate deep links and intents,
- keep auth flows robust,
- protect WebView boundaries,
- rely on server-side authorization,
- make reverse engineering harder but not impossible.

### Core Concepts

- Server-side trust boundary.
- OAuth/token storage.
- Encrypted storage where appropriate.
- Android Keystore.
- Network Security Config.
- Certificate pinning trade-offs.
- Deep link validation.
- Intent spoofing/exported components.
- WebView JavaScript bridge risks.
- Obfuscation with R8/ProGuard.

### Interview Questions

- How do you store tokens securely?
- Is certificate pinning always a good idea?
- How do you secure deep links?
- What should never be logged?
- How do you protect API keys in an Android app?
- What are risks of WebView?
- How do you handle exported components?

### Variations In Wording

- "Can we hide a secret in the APK?"
- "What happens if someone decompiles the app?"
- "Should refresh tokens be stored in SharedPreferences?"
- "How would you handle malicious intents?"
- "What security checks belong on client vs server?"

### Natural Interview Answer

"I assume anything shipped in the APK can eventually be inspected, so I do not treat client-side secrets as truly secret. For auth tokens, I use the platform security tools available, minimize lifetime and scope, avoid logs, and rely on server-side authorization. For deep links and intents, I validate inputs and component exposure. For certificate pinning, I see it as a trade-off: it can reduce certain MITM risks but can also create operational risk if rotation is mishandled."

### Deeper Follow-Ups

**API keys in app?**

"If the key is in the app, it is not a strong secret. I restrict it by package/signing certificate or backend policy where possible, and avoid using mobile API keys as authorization."

**Certificate pinning?**

"Useful in high-risk apps, but dangerous if not planned with backup pins and rotation. It should be driven by threat model, not added automatically."

### Common Mistakes

- Claiming secrets can be safely hidden in APK.
- Logging tokens or PII.
- Trusting client-side checks for authorization.
- Enabling exported components accidentally.
- Adding pinning without operational planning.

### Checklist

- Can I explain mobile trust boundaries?
- Can I discuss secure token storage?
- Can I reason about deep links and exported components?
- Can I explain certificate pinning trade-offs?

---

## 17. Gradle, Modularization, Build Performance, and Release Engineering

### Why This Appears In Senior Interviews

Senior Android developers often influence build health and release quality. Interviewers ask about modules, build times, version catalogs, KSP/KAPT, flavors, CI, signing, R8, and migration strategy.

### Concise Theory

Gradle is the build system. Large Android apps need build hygiene:

- clear module boundaries,
- minimal dependencies between modules,
- convention plugins,
- version catalogs,
- build cache and configuration cache,
- avoiding unnecessary annotation processing,
- using KSP where supported,
- release variants and signing,
- R8 shrinking/obfuscation,
- CI reproducibility.

Modularization is not automatically good. It helps when it improves ownership, build parallelism, feature isolation, or dependency control. Too many modules can add complexity.

### Core Concepts

- App, feature, core, data, domain modules.
- API vs implementation dependencies.
- KAPT vs KSP.
- Annotation processing cost.
- Build variants/flavors.
- R8/ProGuard rules.
- Baseline profiles.
- CI pipelines.
- Semantic versioning for internal libraries where useful.

### Interview Questions

- How would you modularize a large Android app?
- How do you improve Gradle build time?
- KAPT vs KSP?
- What is R8?
- How do build variants and flavors work?
- How do you manage dependencies across modules?
- How do you handle release signing and CI?

### Variations In Wording

- "Build takes 15 minutes. What do you investigate?"
- "Should every feature be a module?"
- "How do you prevent dependency cycles?"
- "What happens if R8 removes code used by reflection?"
- "How do you migrate Java/KAPT code to KSP?"

### Natural Interview Answer

"For build performance, I first measure where time is going: configuration, compilation, annotation processing, tests, packaging. Then I look at dependency graph size, module boundaries, KAPT usage, non-cacheable tasks, and CI configuration. Modularization can help, but only with sensible boundaries. I prefer modules that reflect ownership or dependency direction, not hundreds of tiny modules that slow everyone down."

### Deeper Follow-Ups

**R8?**

"R8 shrinks, optimizes, and obfuscates code. It can remove unused code, but reflection, serialization, DI, and Android framework entry points may need keep rules. Release builds must be tested with minification enabled."

**KSP vs KAPT?**

"KSP works at the Kotlin symbol level and is generally more Kotlin-friendly and often faster. KAPT generates Java stubs and can be expensive. Migration depends on library support."

### Common Mistakes

- Modularizing without dependency rules.
- Ignoring annotation processing cost.
- Testing only debug builds.
- Adding broad keep rules that disable shrinking benefits.
- Letting modules depend on each other cyclically.

### Checklist

- Can I diagnose slow builds?
- Can I justify module boundaries?
- Can I explain R8 and keep rules?
- Can I discuss KSP vs KAPT?

---

## 18. Android System Design for Senior Interviews

### Why This Appears In Senior Interviews

Senior roles frequently include mobile system design: design an offline-first app, chat, feed, media upload, location tracking, payments, or migration plan. The expected answer is not backend-only system design; it must include mobile constraints.

### Concise Theory

Android system design should cover:

- user requirements,
- data flow,
- local persistence,
- network strategy,
- background work,
- lifecycle and process death,
- sync and conflict handling,
- UI state,
- performance,
- security,
- testing,
- observability,
- release/migration plan.

The senior signal is trade-off clarity. You do not need one perfect architecture; you need a defensible design that handles mobile realities.

### Common Prompts

- Design an offline-first notes app.
- Design a chat feature.
- Design a paginated feed with cache.
- Design photo/video upload with retry.
- Design location tracking.
- Design migration from XML/MVP/Java to Kotlin/Compose/MVVM.
- Design a feature flag system for mobile.
- Design app startup for a large app.

### Natural Answer Framework

Use this structure:

1. Clarify requirements and constraints.
2. Define source of truth.
3. Define data model and state model.
4. Explain UI architecture.
5. Explain networking and local persistence.
6. Explain background work and process death.
7. Explain error handling and retry.
8. Explain security/privacy constraints.
9. Explain testing and observability.
10. Call out trade-offs.

### Example: Offline-First Feed

"I would make the local database the source of truth. The feed screen observes paged local data. A refresh fetches from the network, writes results into Room in a transaction, and the UI updates from Room. For pagination, I track remote keys or cursors. If refresh fails, I show cached content with a non-blocking error. For writes like likes or saves, I can update optimistically and persist a pending operation queue. WorkManager drains the queue when network is available, with idempotent request IDs to avoid duplicates."

### Follow-Ups

**What if server order changes?**

"I need stable server ordering or cursor semantics. The local model should store order metadata, and refresh should reconcile rather than blindly append duplicates."

**What if user logs out?**

"User-scoped data must be cleared or partitioned by account. Pending work must be cancelled, re-authenticated, or discarded based on product rules."

**What if app is killed mid-sync?**

"Sync progress should be recoverable. Work should be idempotent, and local pending operations should record enough state to resume."

### Common Mistakes

- Giving backend-only design.
- Ignoring process death.
- Ignoring offline behavior.
- Not defining source of truth.
- Forgetting retries and idempotency.
- Skipping testing and observability.

### Checklist

- Can I design with mobile constraints?
- Can I define source of truth?
- Can I discuss sync and conflict resolution?
- Can I handle process death and background work?

---

## Tricky Or Badly Phrased Questions

### "Are coroutines threads?"

Natural answer:

"No. Coroutines are units of asynchronous work that run on threads. They can suspend without blocking the underlying thread, which is why they scale better for many async tasks. But CPU work still uses real threads."

### "Does suspend mean background?"

Natural answer:

"No. `suspend` means the function can suspend and resume. It does not decide the thread. Dispatcher or the called API decides where work runs."

### "Is Compose faster than XML?"

Natural answer:

"Not automatically. Compose can be very productive and performant, but performance depends on state modeling, recomposition scope, list keys, allocations, and measurement. XML and Compose both can be fast or slow depending on implementation."

### "Does ViewModel survive process death?"

Natural answer:

"The ViewModel object survives configuration changes while its owner remains, but not process death. After process death, it is recreated, so important restoration data must come from SavedStateHandle or persistent storage."

### "Is Clean Architecture always better?"

Natural answer:

"No. Clean boundaries are useful when they reduce coupling and improve testability. If applied mechanically, they add ceremony. I choose the amount of structure based on feature complexity, team size, and expected change."

### "Should all errors be handled in repository?"

Natural answer:

"Expected data-source errors can be mapped there, but the repository should not blindly swallow everything. Some errors belong at domain boundaries, some at UI state, and cancellation should generally propagate."

---

## When You Know The Concept But Forgot The Exact Term

Use this answer pattern:

1. State the behavior you know.
2. Give a small example.
3. Name the trade-off.
4. Ask or recover the exact term naturally.

Example:

"I may be blanking on the exact API name, but the behavior I mean is: the child failure should not cancel its siblings. In coroutines I would use the supervisor-style scope or job for that, then handle each child result explicitly. The trade-off is that errors no longer cancel the whole operation automatically, so I need deliberate reporting."

This sounds stronger than pretending or guessing an API name.

---

## Most Frequently Asked Fundamentals

Based on the researched patterns, these appear repeatedly:

1. Kotlin null safety and Java interop.
2. Data classes, sealed classes, and UI state modeling.
3. Coroutines: scope, dispatcher, cancellation.
4. Coroutine exception handling and supervisor behavior.
5. Flow, StateFlow, SharedFlow, lifecycle-aware collection.
6. Compose state, recomposition, and side effects.
7. ViewModel lifecycle, SavedStateHandle, process death.
8. MVVM/MVI, repositories, Clean Architecture trade-offs.
9. Offline-first architecture with Room and WorkManager.
10. Retrofit/OkHttp networking and API error handling.
11. Hilt/Dagger/Koin DI and scoping.
12. Testing ViewModels, Flows, coroutines, Compose, and Room.
13. Performance: ANRs, startup, memory leaks, jank.
14. Background execution constraints.
15. Gradle modularization and release build issues.

---

## Prioritized Study Roadmap

### Week 1: Kotlin Core

- Null safety, platform types, `lateinit`, `lazy`.
- Data/sealed/value classes.
- Extension functions, lambdas, scope functions.
- Generics, `in`, `out`, type erasure, `reified`.

Outcome: You can answer Kotlin language questions without sounding like Java translated to Kotlin.

### Week 2: Coroutines and Flow

- Structured concurrency.
- Scope ownership.
- Dispatchers.
- Cancellation.
- Exception handling.
- Flow/StateFlow/SharedFlow.
- Testing coroutines.

Outcome: You can handle lifecycle and failure scenarios.

### Week 3: Android Architecture

- ViewModel, SavedStateHandle, process death.
- MVVM/MVI/UDF.
- Repository and source of truth.
- Offline-first with Room, DataStore, WorkManager.
- Networking and error mapping.

Outcome: You can design features with real mobile constraints.

### Week 4: Compose, Testing, Performance, Release

- Compose state/recomposition/effects.
- Testing strategy.
- Performance diagnosis.
- DI scopes.
- Gradle/build/release/R8.
- Security basics.

Outcome: You can answer senior-level judgment questions.

---

## Mock Senior Android / Kotlin Interview

### Round 1: Kotlin and Coroutines

1. Kotlin is null-safe. Why do we still get NPEs?
2. Explain `launch`, `async`, and `withContext`.
3. A user leaves the screen while a request is running. What happens?
4. What is structured concurrency?
5. What is `supervisorScope` useful for?
6. Why does `reified` require `inline`?
7. Explain `out` and `in` generics.

### Round 2: Flow and Architecture

1. Flow vs StateFlow vs SharedFlow.
2. How would you model UI state for loading/content/error?
3. What should a repository do?
4. What is the source of truth in an offline-first app?
5. How do you handle one-off events in Compose?
6. What survives rotation? What survives process death?

### Round 3: Compose and Android Internals

1. What is recomposition?
2. What is state hoisting?
3. `LaunchedEffect` runs more than expected. Why?
4. A mutable list changes but UI does not update. Why?
5. How do you avoid leaking Activity?
6. How do you detect an ANR root cause?

### Round 4: System Design

Design a photo upload feature:

- user can select multiple photos,
- upload continues after app is backgrounded,
- retry on network failure,
- show progress,
- avoid duplicate uploads,
- handle logout,
- support poor network.

Strong answer should include:

- local pending upload table,
- WorkManager or foreground service depending on immediacy and UX,
- idempotent upload IDs,
- progress persistence,
- cancellation behavior,
- auth refresh handling,
- user-visible state,
- cleanup and retry policy,
- tests for process death and retry.

---

## Glossary

- **ANR**: Application Not Responding; usually main thread blocked too long.
- **Cold Flow**: Flow that starts producing when collected.
- **Hot Flow**: Stream/state that exists independently of collectors.
- **StateFlow**: Hot state holder with current value.
- **SharedFlow**: Hot shared emission stream with configurable replay/buffer.
- **Structured Concurrency**: Coroutine lifetimes organized by parent scopes.
- **Dispatcher**: Controls where coroutine execution happens.
- **ViewModel**: State holder for UI data and logic scoped to a screen/back stack owner.
- **SavedStateHandle**: Small state restoration mechanism for ViewModels.
- **Source of Truth**: Authoritative place where current data is read from.
- **UDF**: Unidirectional Data Flow; state flows down, events flow up.
- **DTO**: Data Transfer Object matching external API/storage shape.
- **R8**: Android shrinker, optimizer, and obfuscator.
- **KSP**: Kotlin Symbol Processing API.
- **KAPT**: Kotlin annotation processing tool using Java stubs.
- **Idempotency**: Operation can be repeated without unintended duplicate effects.

---

## Source-Informed Patterns Found During Research

The strongest recurring pattern is that senior Android interviews often begin with basic concepts but quickly test edge cases:

- "What is a coroutine?" becomes lifecycle ownership, cancellation, and exception propagation.
- "What is Flow?" becomes hot/cold streams, `StateFlow`, events, `flowOn`, and lifecycle collection.
- "What is ViewModel?" becomes process death, SavedStateHandle, and avoiding lifecycle leaks.
- "What is Compose recomposition?" becomes mutable state, side effects, keys, and performance.
- "What is Clean Architecture?" becomes migration, modularity, source of truth, and avoiding overengineering.
- "How do you cache data?" becomes offline-first sync, WorkManager, conflict resolution, and idempotency.
- "How do you test it?" becomes deterministic coroutine testing, fakes, Flow collection, and UI test trade-offs.

For senior roles, the answer quality usually depends less on naming a tool and more on explaining ownership, lifecycle, failure behavior, and trade-offs.
