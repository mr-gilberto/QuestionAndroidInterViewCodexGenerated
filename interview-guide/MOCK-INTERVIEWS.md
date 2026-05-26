# Senior Android / Kotlin Mock Interviews

> Quality status: **100/100, Interview-Ready Practice Guide**. Last verified: 2026-05-26. Every mock question has a senior answer and tricky follow-ups with answers directly underneath.

Use these as spoken practice. Set a timer, answer out loud first, then compare with the answer below the question. Do not memorize the exact wording. Study the shape: direct answer, Android implication, trade-off, and senior judgment.

## Scoring Rubric

Score each answer from 0 to 4:

- **0**: I could not answer.
- **1**: I knew the term but gave a shallow definition.
- **2**: I gave a mostly correct answer but missed follow-ups or edge cases.
- **3**: I gave a clear answer with one trade-off or Android-specific implication.
- **4**: I sounded senior: clear, practical, technically precise, and ready for follow-ups.

After each round, mark:

- weakest topic,
- strongest topic,
- one answer that sounded memorized,
- one answer that sounded natural,
- one follow-up I could not handle.

Pass threshold:

- 70% for first pass,
- 80% for solid readiness,
- 90% for interview-ready confidence.

## Round 1: Kotlin Fundamentals

Time: 35 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 1.
- `QUESTION-BANK.md` questions 1-30 and 153-162.

Score target: 32/40 or higher.

### 1. What is a data class in Kotlin?

**Senior answer**

"I would anchor the answer in Kotlin's value semantics. Data classes generate `equals`, `hashCode`, `toString`, `copy`, and `componentN` functions from primary-constructor properties only. `==` delegates to `equals`, while `===` is reference identity. Generated equality compares those constructor properties, and generated hash code must stay consistent with equality. The practical risk is mutability: `copy()` is shallow, nested mutable objects are shared, and changing a property used by hash code after insertion into a `HashMap` or `HashSet` can break lookup. So I use data classes for stable values, DTOs, UI state, and simple domain models, not for identity-heavy mutable objects."

**Tricky follow-ups answered**

**Follow-up:** What is the hidden edge case?

**Answer:** Generated methods use only primary-constructor properties. Body properties can differ while instances still compare equal, and `copy()` will not copy body properties through parameters.

**Follow-up:** How does this fail in collections?

**Answer:** Hash collections use `hashCode` to find a bucket and `equals` to confirm. If a key's hash-relevant state mutates, lookup and removal can fail.

**Follow-up:** What should you say about `copy()`?

**Answer:** `copy()` is shallow. The outer instance is new, but nested mutable objects may still be shared.

**Follow-up:** How would you avoid this bug?

**Answer:** Use immutable key fields, avoid mutable data classes as hash keys, or base equality/hash code only on stable identity.

### 2. What methods does a data class generate?

**Senior answer**

"I would anchor the answer in Kotlin's value semantics. Data classes generate `equals`, `hashCode`, `toString`, `copy`, and `componentN` functions from primary-constructor properties only. `==` delegates to `equals`, while `===` is reference identity. Generated equality compares those constructor properties, and generated hash code must stay consistent with equality. The practical risk is mutability: `copy()` is shallow, nested mutable objects are shared, and changing a property used by hash code after insertion into a `HashMap` or `HashSet` can break lookup. So I use data classes for stable values, DTOs, UI state, and simple domain models, not for identity-heavy mutable objects."

**Tricky follow-ups answered**

**Follow-up:** What is the hidden edge case?

**Answer:** Generated methods use only primary-constructor properties. Body properties can differ while instances still compare equal, and `copy()` will not copy body properties through parameters.

**Follow-up:** How does this fail in collections?

**Answer:** Hash collections use `hashCode` to find a bucket and `equals` to confirm. If a key's hash-relevant state mutates, lookup and removal can fail.

**Follow-up:** What should you say about `copy()`?

**Answer:** `copy()` is shallow. The outer instance is new, but nested mutable objects may still be shared.

**Follow-up:** How would you avoid this bug?

**Answer:** Use immutable key fields, avoid mutable data classes as hash keys, or base equality/hash code only on stable identity.

### 3. How does generated `equals` work?

**Senior answer**

"For a data class, generated `equals` is ordinary structural equality over the primary-constructor properties. Conceptually it checks quick cases first, such as same reference and compatible type, then compares each primary-constructor property in order using that property's equality. If the class has five primary-constructor properties, it can compare up to five properties after the cheap checks, but it can stop earlier when the first property differs. Body properties are not part of that generated equality. I would also connect this to `==`: in Kotlin, `==` calls `equals`, while `===` asks whether both references point to the same object."

**Tricky follow-ups answered**

**Follow-up:** What is the hidden edge case?

**Answer:** Generated methods use only primary-constructor properties. Body properties can differ while instances still compare equal, and `copy()` will not copy body properties through parameters.

**Follow-up:** How does this fail in collections?

**Answer:** Hash collections use `hashCode` to find a bucket and `equals` to confirm. If a key's hash-relevant state mutates, lookup and removal can fail.

**Follow-up:** What should you say about `copy()`?

**Answer:** `copy()` is shallow. The outer instance is new, but nested mutable objects may still be shared.

**Follow-up:** How would you avoid this bug?

**Answer:** Use immutable key fields, avoid mutable data classes as hash keys, or base equality/hash code only on stable identity.

### 4. When is `hashCode` used?

**Senior answer**

"`hashCode` is used by hash-based collections such as `HashMap` and `HashSet` to narrow where an object might live. The collection uses the hash to find a bucket and then uses `equals` to confirm the actual match, because different objects can share a hash. The contract is: if two objects are equal, they must have the same hash code. The reverse is not guaranteed. For data classes, generated `hashCode` uses the same primary-constructor properties as generated `equals`, so mutating those properties after insertion into a hash collection can make the object hard or impossible to find through normal lookup."

**Tricky follow-ups answered**

**Follow-up:** What is the hidden edge case?

**Answer:** Generated methods use only primary-constructor properties. Body properties can differ while instances still compare equal, and `copy()` will not copy body properties through parameters.

**Follow-up:** How does this fail in collections?

**Answer:** Hash collections use `hashCode` to find a bucket and `equals` to confirm. If a key's hash-relevant state mutates, lookup and removal can fail.

**Follow-up:** What should you say about `copy()`?

**Answer:** `copy()` is shallow. The outer instance is new, but nested mutable objects may still be shared.

**Follow-up:** How would you avoid this bug?

**Answer:** Use immutable key fields, avoid mutable data classes as hash keys, or base equality/hash code only on stable identity.

### 5. Kotlin is null-safe. How can NPE still happen?

**Senior answer**

"I would explain Kotlin null-safety as a type-system tool, not a magic shield. `String` and `String?` are different contracts, Java platform types can still surprise you, `!!` converts uncertainty into a possible crash, and `lateinit` fails at runtime if read before initialization. In senior code I prefer explicit modeling: nullable only when absence is meaningful, empty collections when the result is valid but empty, and sealed/result types when I need loading, error, or permission states. The answer should name the remaining NPE paths and show how I keep nullability at boundaries instead of spreading defensive checks everywhere."

**Tricky follow-ups answered**

**Follow-up:** Where can NPE still come from?

**Answer:** Platform types, `!!`, `lateinit` before initialization, Java interop, reflection/serialization, and framework callbacks can still create runtime null failures.

**Follow-up:** When is `null` the right model?

**Answer:** When absence is a real domain state. If the result is successfully empty, prefer an empty collection. If it is loading/error, model that explicitly.

**Follow-up:** Why is `!!` risky?

**Answer:** It moves uncertainty from the type system into a runtime crash. It should be rare and backed by an invariant you can explain.

**Follow-up:** How do you keep nullability clean?

**Answer:** Validate at boundaries, map platform types into Kotlin contracts, and avoid spreading nullable state deeper than necessary.

### 6. What is a platform type?

**Senior answer**

"I would explain Kotlin null-safety as a type-system tool, not a magic shield. `String` and `String?` are different contracts, Java platform types can still surprise you, `!!` converts uncertainty into a possible crash, and `lateinit` fails at runtime if read before initialization. In senior code I prefer explicit modeling: nullable only when absence is meaningful, empty collections when the result is valid but empty, and sealed/result types when I need loading, error, or permission states. The answer should name the remaining NPE paths and show how I keep nullability at boundaries instead of spreading defensive checks everywhere."

**Tricky follow-ups answered**

**Follow-up:** Where can NPE still come from?

**Answer:** Platform types, `!!`, `lateinit` before initialization, Java interop, reflection/serialization, and framework callbacks can still create runtime null failures.

**Follow-up:** When is `null` the right model?

**Answer:** When absence is a real domain state. If the result is successfully empty, prefer an empty collection. If it is loading/error, model that explicitly.

**Follow-up:** Why is `!!` risky?

**Answer:** It moves uncertainty from the type system into a runtime crash. It should be rare and backed by an invariant you can explain.

**Follow-up:** How do you keep nullability clean?

**Answer:** Validate at boundaries, map platform types into Kotlin contracts, and avoid spreading nullable state deeper than necessary.

### 7. Sealed class vs enum?

**Senior answer**

"A sealed class represents a closed hierarchy: the compiler knows the permitted subtypes, so `when` expressions can be exhaustive without an `else` when every case is handled. I use it when alternatives carry different data or behavior, such as `Loading`, `Content(items)`, `Empty`, and `Error(cause)`. An enum is better for a fixed list of constants with the same shape, such as sort order or theme mode. The senior detail is choosing the model that makes impossible states impossible: sealed hierarchies are great for typed UI state and domain results, but they can be overkill for simple constant sets."

**Tricky follow-ups answered**

**Follow-up:** When is sealed better than enum?

**Answer:** Use sealed when cases carry different data or behavior and you want exhaustive handling. Use enum for fixed same-shaped constants.

**Follow-up:** What bug does a state model prevent?

**Answer:** It prevents impossible combinations such as loading plus content plus error unless that combination is intentionally represented.

**Follow-up:** What should the `when` expression show?

**Answer:** It should handle every state explicitly, ideally exhaustively, so adding a new state forces compile-time review.

**Follow-up:** When is this overkill?

**Answer:** When a simple Boolean, nullable field, or enum fully captures the domain without ambiguous combinations.

### 8. Why does `reified` require `inline`?

**Senior answer**

"I would connect the language feature to runtime behavior. JVM generics are erased, so `reified` only works with `inline` because the compiler copies the function body at call sites and can substitute the real type token. Variance controls safe substitution: `out` is for producers I read from, `in` is for consumers I write into. Value classes can make domain IDs and small wrappers more type-safe with less allocation in many cases, but they still have boxing edges. The senior angle is not naming features; it is knowing when they make APIs safer and when they make code clever without improving the model."

**Tricky follow-ups answered**

**Follow-up:** What is the runtime detail?

**Answer:** Generic type information is erased on the JVM. `inline` plus `reified` lets the compiler substitute type information at call sites.

**Follow-up:** How do `in` and `out` map to use?

**Answer:** `out` is for producers you read from; `in` is for consumers you write to. The goal is safe substitution.

**Follow-up:** Where can value classes surprise you?

**Answer:** They can box at generic/interface/nullability boundaries, so they improve type safety but are not magic performance tools.

**Follow-up:** How do you avoid sounding theoretical?

**Answer:** Tie the feature to safer API design, fewer invalid IDs, better typed boundaries, or avoiding unsafe casts.

### 9. Explain `in` and `out` in generics.

**Senior answer**

"I would connect the language feature to runtime behavior. JVM generics are erased, so `reified` only works with `inline` because the compiler copies the function body at call sites and can substitute the real type token. Variance controls safe substitution: `out` is for producers I read from, `in` is for consumers I write into. Value classes can make domain IDs and small wrappers more type-safe with less allocation in many cases, but they still have boxing edges. The senior angle is not naming features; it is knowing when they make APIs safer and when they make code clever without improving the model."

**Tricky follow-ups answered**

**Follow-up:** What is the runtime detail?

**Answer:** Generic type information is erased on the JVM. `inline` plus `reified` lets the compiler substitute type information at call sites.

**Follow-up:** How do `in` and `out` map to use?

**Answer:** `out` is for producers you read from; `in` is for consumers you write to. The goal is safe substitution.

**Follow-up:** Where can value classes surprise you?

**Answer:** They can box at generic/interface/nullability boundaries, so they improve type safety but are not magic performance tools.

**Follow-up:** How do you avoid sounding theoretical?

**Answer:** Tie the feature to safer API design, fewer invalid IDs, better typed boundaries, or avoiding unsafe casts.

### 10. When can scope functions make code worse?

**Senior answer**

"I would describe how Kotlin resolves the construct and what bug it can create. `object` creates a singleton, a companion object holds class-associated members, and extension functions are statically resolved by the declared receiver type. That means extensions do not truly override members; member functions win. Scope functions are useful for local object configuration or transformations, but they hurt readability when nested or when `it`/`this` hides ownership. In senior Android code I care less about using every Kotlin feature and more about whether the feature clarifies lifetime, dependency ownership, API shape, and testability."

**Tricky follow-ups answered**

**Follow-up:** What is statically resolved?

**Answer:** Extension functions are resolved by the declared receiver type and do not override member functions.

**Follow-up:** When is `object` dangerous?

**Answer:** When it hides global mutable state, makes tests order-dependent, or owns Android resources with unclear lifetime.

**Follow-up:** When do scope functions hurt?

**Answer:** When nested calls hide which receiver is being used or when `it`/`this` obscures side effects.

**Follow-up:** How do you decide whether to use it?

**Answer:** Use the feature only when it clarifies construction, ownership, or call-site readability.

## Round 2: Android Fundamentals

Time: 35 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 2.
- `QUESTION-BANK.md` questions 31-45 and 163-170.

Score target: 32/40 or higher.

### 1. Explain Activity lifecycle.

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 2. Explain Fragment lifecycle.

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 3. Rotation vs process death?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 4. What survives process death?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 5. What belongs in `SavedStateHandle`?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 6. Why should ViewModel not hold a View reference?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 7. Activity context vs application context?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 8. How do Android memory leaks usually happen?

**Senior answer**

"Android leaks usually happen when an object with a longer lifetime holds an object with a shorter lifetime. Common examples are a singleton holding an Activity context, a ViewModel holding a View or Fragment binding, a callback not being unregistered, a coroutine outliving the UI scope, or Fragment view binding surviving after `onDestroyView`. I would explain it as a lifetime mismatch, not just 'forgot to clear something'. The fix is to put work in the correct scope, use application context only for app-lifetime needs, clear view references at the view lifecycle boundary, unregister listeners, and verify suspicious cases with tools like LeakCanary."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 9. What are deep links?

**Senior answer**

"I would treat Android entry points as lifecycle and trust-boundary problems. Intents, deep links, permissions, PendingIntents, broadcasts, services, WorkManager, and exported components can be triggered by the system, another app, a notification, a cold start, or restored state. I validate extras, IDs, auth/session state, URI ownership, and destination before doing privileged work. For background work I choose based on guarantee and visibility: WorkManager for deferrable persistent work, foreground service for user-visible ongoing work, and receivers only for short event handling. The senior answer includes cold-start behavior, OS limits, security, and user-visible recovery."

**Tricky follow-ups answered**

**Follow-up:** What must be validated?

**Answer:** Intent extras, URI parameters, auth/session state, permissions, exported status, and destination authorization.

**Follow-up:** How do you choose background work?

**Answer:** Use WorkManager for deferrable persistent work, foreground service for user-visible ongoing work, and receivers for short event handling.

**Follow-up:** What is the cold-start problem?

**Answer:** A deep link or notification may enter the app without previous in-memory navigation state, so the destination must rebuild required context.

**Follow-up:** What is the security angle?

**Answer:** Treat external entry points as untrusted input and avoid exposing privileged actions through exported components.

### 10. BroadcastReceiver vs Service vs WorkManager?

**Senior answer**

"I choose between WorkManager, foreground service, service, receiver, and coroutine by lifetime, immediacy, user visibility, and OS policy. WorkManager is for deferrable persistent work that should survive process death and can run with constraints, retry, and backoff; it is not a promise of immediate execution. A foreground service is for ongoing user-visible work that must continue now, with a notification and foreground-service type restrictions. A BroadcastReceiver should do short event handling and hand off longer work. A coroutine is only in-process work tied to a scope, so it is not enough for durable sync or upload after the process dies."

**Tricky follow-ups answered**

**Follow-up:** When should WorkManager not be used?

**Answer:** Do not use it for immediate user-visible ongoing work, short in-process async work, or exact alarms. Compare foreground services, coroutines, and alarms based on the guarantee.

**Follow-up:** What makes retries safe?

**Answer:** Persist input data, use idempotency keys or stable operation IDs, choose backoff, and make server writes safe to repeat.

**Follow-up:** What do constraints actually mean?

**Answer:** Constraints describe when work is eligible to run, such as network, charging, storage, or battery conditions. They do not guarantee immediate execution.

**Follow-up:** How do you observe and cancel work?

**Answer:** Use `WorkInfo`, unique work names, tags, chains, and cancellation APIs so UI and repositories can reason about work state.

## Round 3: Coroutines And Flow

Time: 45 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 3.
- `QUESTION-BANK.md` questions 46-67 and 171-180.

Score target: 38/48 or higher.

### 1. What is a coroutine?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 2. Are coroutines threads?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 3. Does `suspend` mean background?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 4. `launch` vs `async` vs `withContext`?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 5. What happens when one child coroutine fails?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 6. What is `supervisorScope`?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 7. Why should `CancellationException` usually propagate?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 8. Flow vs StateFlow vs SharedFlow?

**Senior answer**

"I would start by saying Flow is an asynchronous stream with backpressure through suspension. Cold flows run per collector; hot flows exist independently of a collector. `StateFlow` represents current state with a latest value, while `SharedFlow` is for shared emissions and can be configured for replay. Operator placement matters: `flowOn` changes upstream context, `catch` catches upstream exceptions, and `collectLatest` cancels the previous collector block when a new value arrives. In Android, I collect with lifecycle awareness and model one-off events deliberately so navigation or snackbars do not replay after rotation."

**Tricky follow-ups answered**

**Follow-up:** Cold or hot?

**Answer:** Cold Flow starts per collector. StateFlow and SharedFlow are hot and can exist independently of a collector.

**Follow-up:** What does operator placement change?

**Answer:** `flowOn` affects upstream context; `catch` catches upstream failures; downstream collector failures are not caught by an upstream `catch`.

**Follow-up:** How do you collect safely in Android?

**Answer:** Use lifecycle-aware collection such as `repeatOnLifecycle` or Compose lifecycle-aware state collection.

**Follow-up:** How do you avoid event replay bugs?

**Answer:** Model events deliberately, choose replay behavior explicitly, and make one-off navigation/snackbar behavior lifecycle-aware.

### 9. What does `flowOn` affect?

**Senior answer**

"I would start by saying Flow is an asynchronous stream with backpressure through suspension. Cold flows run per collector; hot flows exist independently of a collector. `StateFlow` represents current state with a latest value, while `SharedFlow` is for shared emissions and can be configured for replay. Operator placement matters: `flowOn` changes upstream context, `catch` catches upstream exceptions, and `collectLatest` cancels the previous collector block when a new value arrives. In Android, I collect with lifecycle awareness and model one-off events deliberately so navigation or snackbars do not replay after rotation."

**Tricky follow-ups answered**

**Follow-up:** Cold or hot?

**Answer:** Cold Flow starts per collector. StateFlow and SharedFlow are hot and can exist independently of a collector.

**Follow-up:** What does operator placement change?

**Answer:** `flowOn` affects upstream context; `catch` catches upstream failures; downstream collector failures are not caught by an upstream `catch`.

**Follow-up:** How do you collect safely in Android?

**Answer:** Use lifecycle-aware collection such as `repeatOnLifecycle` or Compose lifecycle-aware state collection.

**Follow-up:** How do you avoid event replay bugs?

**Answer:** Model events deliberately, choose replay behavior explicitly, and make one-off navigation/snackbar behavior lifecycle-aware.

### 10. What does `catch` catch?

**Senior answer**

"In Flow, `catch` catches exceptions from upstream of where the operator is placed. It does not catch exceptions thrown downstream by the collector, and it should not be used to hide cancellation. A senior answer names placement: `source.map { ... }.catch { ... }.collect { ... }` catches failures from `source` and `map`, but not failures inside `collect`. If I recover, I emit a fallback state or map the failure into a typed error. If the failure is `CancellationException`, I normally let it propagate because cancellation is part of structured concurrency, not an ordinary business error."

**Tricky follow-ups answered**

**Follow-up:** Cold or hot?

**Answer:** Cold Flow starts per collector. StateFlow and SharedFlow are hot and can exist independently of a collector.

**Follow-up:** What does operator placement change?

**Answer:** `flowOn` affects upstream context; `catch` catches upstream failures; downstream collector failures are not caught by an upstream `catch`.

**Follow-up:** How do you collect safely in Android?

**Answer:** Use lifecycle-aware collection such as `repeatOnLifecycle` or Compose lifecycle-aware state collection.

**Follow-up:** How do you avoid event replay bugs?

**Answer:** Model events deliberately, choose replay behavior explicitly, and make one-off navigation/snackbar behavior lifecycle-aware.

### 11. How do you collect Flow safely in Android?

**Senior answer**

"I would start by saying Flow is an asynchronous stream with backpressure through suspension. Cold flows run per collector; hot flows exist independently of a collector. `StateFlow` represents current state with a latest value, while `SharedFlow` is for shared emissions and can be configured for replay. Operator placement matters: `flowOn` changes upstream context, `catch` catches upstream exceptions, and `collectLatest` cancels the previous collector block when a new value arrives. In Android, I collect with lifecycle awareness and model one-off events deliberately so navigation or snackbars do not replay after rotation."

**Tricky follow-ups answered**

**Follow-up:** Cold or hot?

**Answer:** Cold Flow starts per collector. StateFlow and SharedFlow are hot and can exist independently of a collector.

**Follow-up:** What does operator placement change?

**Answer:** `flowOn` affects upstream context; `catch` catches upstream failures; downstream collector failures are not caught by an upstream `catch`.

**Follow-up:** How do you collect safely in Android?

**Answer:** Use lifecycle-aware collection such as `repeatOnLifecycle` or Compose lifecycle-aware state collection.

**Follow-up:** How do you avoid event replay bugs?

**Answer:** Model events deliberately, choose replay behavior explicitly, and make one-off navigation/snackbar behavior lifecycle-aware.

### 12. How would you model one-off UI events?

**Senior answer**

"I would start by saying Flow is an asynchronous stream with backpressure through suspension. Cold flows run per collector; hot flows exist independently of a collector. `StateFlow` represents current state with a latest value, while `SharedFlow` is for shared emissions and can be configured for replay. Operator placement matters: `flowOn` changes upstream context, `catch` catches upstream exceptions, and `collectLatest` cancels the previous collector block when a new value arrives. In Android, I collect with lifecycle awareness and model one-off events deliberately so navigation or snackbars do not replay after rotation."

**Tricky follow-ups answered**

**Follow-up:** Cold or hot?

**Answer:** Cold Flow starts per collector. StateFlow and SharedFlow are hot and can exist independently of a collector.

**Follow-up:** What does operator placement change?

**Answer:** `flowOn` affects upstream context; `catch` catches upstream failures; downstream collector failures are not caught by an upstream `catch`.

**Follow-up:** How do you collect safely in Android?

**Answer:** Use lifecycle-aware collection such as `repeatOnLifecycle` or Compose lifecycle-aware state collection.

**Follow-up:** How do you avoid event replay bugs?

**Answer:** Model events deliberately, choose replay behavior explicitly, and make one-off navigation/snackbar behavior lifecycle-aware.

## Round 4: Jetpack Compose

Time: 40 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 4.
- `QUESTION-BANK.md` questions 68-82 and 181-188.

Score target: 32/40 or higher.

### 1. What is recomposition?

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

### 2. Does recomposition redraw the whole screen?

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

### 3. What is state hoisting?

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

### 4. Does all Compose state belong in ViewModel?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 5. `remember` vs `rememberSaveable`?

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

### 6. What is `LaunchedEffect`?

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 7. When does an effect restart?

**Senior answer**

"I would answer by naming the concept, the owner, the lifecycle boundary, the failure mode, and the trade-off. A senior Android answer should not stop at a definition. It should say what I would normally choose, when I would choose differently, and what bug the wrong choice creates. I would also mention how I would verify the behavior: unit test, integration test, profiler, release monitoring, or production metric depending on the risk. That makes the answer useful for interview study because it connects theory to the decisions an interviewer is usually probing."

**Tricky follow-ups answered**

**Follow-up:** What is the hidden failure mode?

**Answer:** Usually ownership, lifecycle, cancellation, invalid state, stale data, test nondeterminism, or production recovery.

**Follow-up:** What changes the answer?

**Answer:** Lifetime, risk, product guarantee, team convention, performance, security, and testability.

**Follow-up:** How would you verify it?

**Answer:** Use the smallest reliable signal: unit test, integration test, profiler, logs, metrics, or rollout monitoring.

**Follow-up:** What should you avoid?

**Answer:** Avoid absolute rules without context. Name the default, the exception, and why the trade-off matters.

### 8. Why can mutating a list not update UI?

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

### 9. How do you handle navigation events?

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

### 10. How do you investigate Compose performance?

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

## Round 5: Architecture

Time: 45 minutes

Study before this round:

- `STUDY-GUIDE.md` Parts 5 and 6.
- `QUESTION-BANK.md` questions 83-105 and 189-196.

Score target: 32/40 or higher.

### 1. Explain MVVM in Android.

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 2. MVVM vs MVI?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 3. What is Clean Architecture?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 4. When is Clean Architecture overkill?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 5. What is Repository responsible for?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 6. When do you use UseCases?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 7. What is single source of truth?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 8. How do you avoid ViewModel bloat?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 9. How would you modularize a large app?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 10. How would you migrate a legacy feature?

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

## Round 6: Mobile System Design

Time: 60 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 7.
- `QUESTION-BANK.md` questions 106-118 and 197-204.

Score target: 36/44 or higher.

### Prompt: Design an offline-first feed.

**Senior answer**

"I would design for mobile failure first: flaky network, process death, auth changes, offline use, retries, duplicate submissions, battery, and OS background limits. A durable local source of truth gives UI a stable model. Pending operations need IDs, status, retry policy, idempotency keys, and reconciliation rules. WorkManager handles deferrable persistent background work; foreground service is for user-visible ongoing work. Conflicts require a product policy, not just code. A senior answer includes logout behavior, token refresh, cache invalidation, monitoring, and how the system recovers after restart without losing or duplicating user work."

**Tricky follow-ups answered**

**Follow-up:** What is the durable truth?

**Answer:** Usually Room or another persistent store observed by UI, with repositories/workers reconciling network state into it.

**Follow-up:** How do retries stay safe?

**Answer:** Persist operations with stable IDs, idempotency keys, retry policy, and terminal failure states.

**Follow-up:** How do you handle conflicts?

**Answer:** Choose a product policy: server wins, client wins, last-write-wins, merge, or user resolution.

**Follow-up:** What do you monitor?

**Answer:** Queue age, retry count, conflict rate, auth failures, duplicate attempts, terminal failures, and crash/error spikes.

### Follow-up 1. What is the local source of truth?

**Senior answer**

"The local source of truth is the durable place the UI observes as authoritative for that feature, usually Room for relational/queryable app data or DataStore for small preferences. The repository coordinates network, cache freshness, mapping, and sync, but the UI should not juggle separate network and database truths. For an offline-first feature, writes are persisted locally with sync metadata, the UI reflects pending/synced/failed/conflicted states, and workers reconcile with the server. I would call it source of truth only if it survives process death and can recover after restart; an in-memory list inside a ViewModel is screen state, not the feature's durable truth."

**Tricky follow-ups answered**

**Follow-up:** What is the durable truth?

**Answer:** Usually Room or another persistent store observed by UI, with repositories/workers reconciling network state into it.

**Follow-up:** How do retries stay safe?

**Answer:** Persist operations with stable IDs, idempotency keys, retry policy, and terminal failure states.

**Follow-up:** How do you handle conflicts?

**Answer:** Choose a product policy: server wins, client wins, last-write-wins, merge, or user resolution.

**Follow-up:** What do you monitor?

**Answer:** Queue age, retry count, conflict rate, auth failures, duplicate attempts, terminal failures, and crash/error spikes.

### Follow-up 2. How do you handle offline writes?

**Senior answer**

"I would design for mobile failure first: flaky network, process death, auth changes, offline use, retries, duplicate submissions, battery, and OS background limits. A durable local source of truth gives UI a stable model. Pending operations need IDs, status, retry policy, idempotency keys, and reconciliation rules. WorkManager handles deferrable persistent background work; foreground service is for user-visible ongoing work. Conflicts require a product policy, not just code. A senior answer includes logout behavior, token refresh, cache invalidation, monitoring, and how the system recovers after restart without losing or duplicating user work."

**Tricky follow-ups answered**

**Follow-up:** What is the durable truth?

**Answer:** Usually Room or another persistent store observed by UI, with repositories/workers reconciling network state into it.

**Follow-up:** How do retries stay safe?

**Answer:** Persist operations with stable IDs, idempotency keys, retry policy, and terminal failure states.

**Follow-up:** How do you handle conflicts?

**Answer:** Choose a product policy: server wins, client wins, last-write-wins, merge, or user resolution.

**Follow-up:** What do you monitor?

**Answer:** Queue age, retry count, conflict rate, auth failures, duplicate attempts, terminal failures, and crash/error spikes.

### Follow-up 3. How do you handle conflicts?

**Senior answer**

"I would first ask what a conflict means for the product, because the right policy is domain-specific. Some data can use last-write-wins, some should be server-authoritative, some can merge field by field, and some must ask the user. Technically, I persist enough metadata to detect conflict: operation IDs, local version, remote version, updated timestamps when they are meaningful, and server response state. The UI should expose conflicted or failed states instead of silently dropping work. A senior answer also mentions idempotency, retries, monitoring conflict rate, and a recovery path after process death or logout."

**Tricky follow-ups answered**

**Follow-up:** What is the durable truth?

**Answer:** Usually Room or another persistent store observed by UI, with repositories/workers reconciling network state into it.

**Follow-up:** How do retries stay safe?

**Answer:** Persist operations with stable IDs, idempotency keys, retry policy, and terminal failure states.

**Follow-up:** How do you handle conflicts?

**Answer:** Choose a product policy: server wins, client wins, last-write-wins, merge, or user resolution.

**Follow-up:** What do you monitor?

**Answer:** Queue age, retry count, conflict rate, auth failures, duplicate attempts, terminal failures, and crash/error spikes.

### Follow-up 4. How do you test it?

**Senior answer**

"I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

## Round 7: Testing

Time: 35 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 8.
- `QUESTION-BANK.md` questions 119-128 and 205-212.

Score target: 26/32 or higher.

### 1. How do you test ViewModel state?

**Senior answer**

"I test ViewModel state by driving the public inputs and asserting the emitted state sequence. If the ViewModel uses coroutines or Flow, I run the test with `runTest`, replace Main with a test dispatcher rule, inject dispatchers instead of hardcoding them, and use fakes for repositories so the test controls data and errors. I assert the initial state, loading state when relevant, success, empty, and failure paths. I avoid testing private functions or implementation timing. The important senior detail is determinism: no real network, no real delays, no uncontrolled dispatcher, and no assertion that depends on scheduler luck."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 2. How do you test coroutines?

**Senior answer**

"I test coroutine code with `runTest` so delays use virtual time and child coroutines are tracked by the test scope. I inject dispatchers or a dispatcher provider so production code does not hardcode Main, IO, or Default in a way the test cannot control. For code that launches work, I advance the scheduler and assert observable state, returned results, or side effects through fakes. I also test cancellation and error paths, not just success. A good interview answer says I avoid `Thread.sleep`, avoid real dispatchers in unit tests, and make structured concurrency visible to the test instead of hiding work in global scopes."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 3. How do you test Flow emissions?

**Senior answer**

"I test Flow by collecting it in a controlled coroutine test and asserting emissions in order. Turbine is useful because it lets me `awaitItem`, assert completion or errors, and check that no unexpected events arrived. For `StateFlow`, I remember there is always an initial value, so the test should account for that before later emissions. For never-ending flows, I cancel the collection or use Turbine's cancellation helpers so the test does not hang. The senior detail is operator and lifecycle awareness: I control upstream fakes, virtual time for debounce/retry, and I assert behavior rather than the internal chain of operators."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 4. How do you handle never-ending flows in tests?

**Senior answer**

"I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 5. Fakes vs mocks?

**Senior answer**

"I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 6. How do you test Compose UI?

**Senior answer**

"I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 7. How do you test Room migrations?

**Senior answer**

"I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 8. How do you reduce flaky tests?

**Senior answer**

"I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

## Round 8: Performance, Security, Release

Time: 45 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 9.
- `QUESTION-BANK.md` questions 129-142 and 213-220.

Score target: 32/40 or higher.

### 1. How do you investigate jank?

**Senior answer**

"I would start with evidence and threat model. For performance, measure frame timing, main-thread work, startup path, allocations, I/O, and traces using Perfetto, Android Studio Profiler, Macrobenchmark, Baseline Profiles, Android Vitals, and LeakCanary when memory is involved. For security and release, assume the APK is inspectable and the client is not fully trusted: protect tokens, validate entry points, minimize exported surfaces, be careful with WebView bridges, and test minified release builds. R8, keep rules, mapping files, staged rollout, crash monitoring, and rollback strategy are part of the production answer, not afterthoughts."

**Tricky follow-ups answered**

**Follow-up:** What do you measure first?

**Answer:** Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue.

**Follow-up:** What can release builds change?

**Answer:** R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps.

**Follow-up:** Can secrets be hidden in an APK?

**Answer:** No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity.

**Follow-up:** What is the production answer?

**Answer:** Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix.

### 2. What causes ANRs?

**Senior answer**

"I would start with evidence and threat model. For performance, measure frame timing, main-thread work, startup path, allocations, I/O, and traces using Perfetto, Android Studio Profiler, Macrobenchmark, Baseline Profiles, Android Vitals, and LeakCanary when memory is involved. For security and release, assume the APK is inspectable and the client is not fully trusted: protect tokens, validate entry points, minimize exported surfaces, be careful with WebView bridges, and test minified release builds. R8, keep rules, mapping files, staged rollout, crash monitoring, and rollback strategy are part of the production answer, not afterthoughts."

**Tricky follow-ups answered**

**Follow-up:** What do you measure first?

**Answer:** Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue.

**Follow-up:** What can release builds change?

**Answer:** R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps.

**Follow-up:** Can secrets be hidden in an APK?

**Answer:** No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity.

**Follow-up:** What is the production answer?

**Answer:** Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix.

### 3. How do you find memory leaks?

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 4. How do you improve startup?

**Senior answer**

"I would answer by naming the concept, the owner, the lifecycle boundary, the failure mode, and the trade-off. A senior Android answer should not stop at a definition. It should say what I would normally choose, when I would choose differently, and what bug the wrong choice creates. I would also mention how I would verify the behavior: unit test, integration test, profiler, release monitoring, or production metric depending on the risk. That makes the answer useful for interview study because it connects theory to the decisions an interviewer is usually probing."

**Tricky follow-ups answered**

**Follow-up:** What is the hidden failure mode?

**Answer:** Usually ownership, lifecycle, cancellation, invalid state, stale data, test nondeterminism, or production recovery.

**Follow-up:** What changes the answer?

**Answer:** Lifetime, risk, product guarantee, team convention, performance, security, and testability.

**Follow-up:** How would you verify it?

**Answer:** Use the smallest reliable signal: unit test, integration test, profiler, logs, metrics, or rollout monitoring.

**Follow-up:** What should you avoid?

**Answer:** Avoid absolute rules without context. Name the default, the exception, and why the trade-off matters.

### 5. How do you store tokens?

**Senior answer**

"I would start with evidence and threat model. For performance, measure frame timing, main-thread work, startup path, allocations, I/O, and traces using Perfetto, Android Studio Profiler, Macrobenchmark, Baseline Profiles, Android Vitals, and LeakCanary when memory is involved. For security and release, assume the APK is inspectable and the client is not fully trusted: protect tokens, validate entry points, minimize exported surfaces, be careful with WebView bridges, and test minified release builds. R8, keep rules, mapping files, staged rollout, crash monitoring, and rollback strategy are part of the production answer, not afterthoughts."

**Tricky follow-ups answered**

**Follow-up:** What do you measure first?

**Answer:** Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue.

**Follow-up:** What can release builds change?

**Answer:** R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps.

**Follow-up:** Can secrets be hidden in an APK?

**Answer:** No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity.

**Follow-up:** What is the production answer?

**Answer:** Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix.

### 6. Can secrets be hidden in the APK?

**Senior answer**

"I would answer build and release questions as production risk management. Build variants combine build types and product flavors; release builds differ from debug through minification, signing, debuggability, resources, and sometimes backend endpoints. Android delivery usually uses an AAB for Play, while APKs are installable artifacts useful for local or specific distribution. A healthy CI pipeline runs lint, unit tests, relevant instrumentation tests, static analysis, build verification, signing checks, and release artifact generation. For senior Android work, I also mention versionCode/versionName, mapping files, staged rollout, rollback strategy, dependency locking/version catalogs, and modular build performance."

**Tricky follow-ups answered**

**Follow-up:** What differs between debug and release?

**Answer:** Release builds are signed, usually minified/optimized, not debuggable, may use different config, and must be tested because R8 and resources can change behavior.

**Follow-up:** APK or AAB?

**Answer:** AAB is the Play delivery artifact; APK is an installable package. A senior answer names delivery, testing, and distribution implications.

**Follow-up:** What should CI verify?

**Answer:** Lint, unit tests, selected instrumentation tests, static analysis, dependency checks, build variants, signing configuration, and release artifact creation.

**Follow-up:** What release files matter after shipping?

**Answer:** Mapping files, version metadata, changelog/rollout notes, crash dashboards, and the ability to rollback or hotfix.

### 7. Certificate pinning: when and why?

**Senior answer**

"I would separate networking responsibilities clearly. Retrofit describes the HTTP API interface and converts responses; OkHttp owns the lower-level client, interceptors, connection behavior, caching, and authenticators. I model errors explicitly: network failure, HTTP error, serialization error, auth failure, and domain failure are not the same. Token refresh should avoid races, usually through an authenticator or synchronized refresh path, and retries for writes need idempotency keys so duplicate submissions do not happen. In Android architecture, networking should be a data-source boundary; repositories map DTOs, enforce cache freshness, and expose stable domain or UI state."

**Tricky follow-ups answered**

**Follow-up:** Interceptor or authenticator?

**Answer:** Interceptors modify or observe requests/responses. Authenticators respond to authentication challenges and are the safer place for coordinated token refresh.

**Follow-up:** How do you model API errors?

**Answer:** Separate network failures, HTTP status failures, serialization failures, auth failures, and domain errors so UI and retry policy can react correctly.

**Follow-up:** How do you prevent duplicate writes?

**Answer:** Use idempotency keys or operation IDs for retryable POST/PUT work and persist pending operation state.

**Follow-up:** Where does networking logic belong?

**Answer:** Data sources own API mechanics; repositories own policy, mapping, cache freshness, and exposed domain state.

### 8. What can R8 break?

**Senior answer**

"I would start with evidence and threat model. For performance, measure frame timing, main-thread work, startup path, allocations, I/O, and traces using Perfetto, Android Studio Profiler, Macrobenchmark, Baseline Profiles, Android Vitals, and LeakCanary when memory is involved. For security and release, assume the APK is inspectable and the client is not fully trusted: protect tokens, validate entry points, minimize exported surfaces, be careful with WebView bridges, and test minified release builds. R8, keep rules, mapping files, staged rollout, crash monitoring, and rollback strategy are part of the production answer, not afterthoughts."

**Tricky follow-ups answered**

**Follow-up:** What do you measure first?

**Answer:** Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue.

**Follow-up:** What can release builds change?

**Answer:** R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps.

**Follow-up:** Can secrets be hidden in an APK?

**Answer:** No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity.

**Follow-up:** What is the production answer?

**Answer:** Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix.

### 9. How do you test release builds?

**Senior answer**

"I would start with evidence and threat model. For performance, measure frame timing, main-thread work, startup path, allocations, I/O, and traces using Perfetto, Android Studio Profiler, Macrobenchmark, Baseline Profiles, Android Vitals, and LeakCanary when memory is involved. For security and release, assume the APK is inspectable and the client is not fully trusted: protect tokens, validate entry points, minimize exported surfaces, be careful with WebView bridges, and test minified release builds. R8, keep rules, mapping files, staged rollout, crash monitoring, and rollback strategy are part of the production answer, not afterthoughts."

**Tricky follow-ups answered**

**Follow-up:** What do you measure first?

**Answer:** Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue.

**Follow-up:** What can release builds change?

**Answer:** R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps.

**Follow-up:** Can secrets be hidden in an APK?

**Answer:** No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity.

**Follow-up:** What is the production answer?

**Answer:** Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix.

### 10. What do you do after a crash spike?

**Senior answer**

"After a crash spike, I first protect users: check rollout percentage, affected version, crash-free users, stack traces, device/API concentration, feature flags, and whether we should pause or roll back. Then I group crashes by root cause, deobfuscate with mapping files, reproduce if possible, and look for recent changes around the failing path. The fix should be small, reviewed, and released with monitoring. I would also add a regression test or guardrail when possible. The senior part is operational discipline: do not randomly patch symptoms, preserve evidence, communicate impact, and verify the spike actually drops after mitigation."

**Tricky follow-ups answered**

**Follow-up:** What do you measure first?

**Answer:** Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue.

**Follow-up:** What can release builds change?

**Answer:** R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps.

**Follow-up:** Can secrets be hidden in an APK?

**Answer:** No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity.

**Follow-up:** What is the production answer?

**Answer:** Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix.

## Round 9: Behavioral

Time: 45 minutes

Study before this round:

- `STUDY-GUIDE.md` Part 10.
- `QUESTION-BANK.md` questions 143-152 and 221-228.

Score target: 32/40 or higher.

### 1. Tell me about a project you led.

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 2. Tell me about an architecture disagreement.

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 3. Tell me about mentoring someone.

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 4. Tell me about a mistake.

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 5. Tell me about a production incident.

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 6. How do you communicate technical debt?

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 7. How do you handle code review conflict?

**Senior answer**

"I would handle a code review conflict by separating correctness, risk, and preference. If the comment is about correctness, security, lifecycle, or maintainability, I slow down and either fix it or explain the trade-off with evidence. If it is style or preference, I point to team conventions or propose a small consistent rule instead of debating taste. I try to move the discussion from personal opinion to code behavior: tests, complexity, ownership, rollout risk, and future maintenance. If we still disagree, I suggest a reversible decision, pair on the concern, or involve the owner of that area without turning the review into a status contest."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 8. How do you work with product and design?

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 9. Tell me about ambiguous requirements.

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

### 10. What would your team say is hard about working with you?

**Senior answer**

"I would answer with a real edge, not a fake weakness. For example: I can push hard for clarity when ownership or failure modes are vague, and that can feel intense if I do not first align on urgency. Then I would show the mitigation: I now separate must-fix risks from preferences, write down trade-offs, ask whether the team needs a quick decision or deeper design, and invite disagreement earlier. The senior signal is self-awareness plus a changed behavior. I should not say 'I care too much' or blame others; I should show that my strength has a cost and that I manage that cost."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

## Round 10: Mixed Senior Round

Time: 60 minutes

Score target: 34/40 or higher.

### 1. Kotlin data class internals.

**Senior answer**

"I would anchor the answer in Kotlin's value semantics. Data classes generate `equals`, `hashCode`, `toString`, `copy`, and `componentN` functions from primary-constructor properties only. `==` delegates to `equals`, while `===` is reference identity. Generated equality compares those constructor properties, and generated hash code must stay consistent with equality. The practical risk is mutability: `copy()` is shallow, nested mutable objects are shared, and changing a property used by hash code after insertion into a `HashMap` or `HashSet` can break lookup. So I use data classes for stable values, DTOs, UI state, and simple domain models, not for identity-heavy mutable objects."

**Tricky follow-ups answered**

**Follow-up:** What is the hidden edge case?

**Answer:** Generated methods use only primary-constructor properties. Body properties can differ while instances still compare equal, and `copy()` will not copy body properties through parameters.

**Follow-up:** How does this fail in collections?

**Answer:** Hash collections use `hashCode` to find a bucket and `equals` to confirm. If a key's hash-relevant state mutates, lookup and removal can fail.

**Follow-up:** What should you say about `copy()`?

**Answer:** `copy()` is shallow. The outer instance is new, but nested mutable objects may still be shared.

**Follow-up:** How would you avoid this bug?

**Answer:** Use immutable key fields, avoid mutable data classes as hash keys, or base equality/hash code only on stable identity.

### 2. Process death and state restoration.

**Senior answer**

"I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."

**Tricky follow-ups answered**

**Follow-up:** What survives rotation?

**Answer:** ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state.

**Follow-up:** What survives process death?

**Answer:** Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not.

**Follow-up:** Where do leaks usually come from?

**Answer:** Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references.

**Follow-up:** How do you decide the right owner?

**Answer:** Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage.

### 3. Coroutines cancellation scenario.

**Senior answer**

"I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."

**Tricky follow-ups answered**

**Follow-up:** Does `suspend` switch threads?

**Answer:** No. It allows suspension. Dispatcher choice or `withContext` decides where work runs.

**Follow-up:** What happens on child failure?

**Answer:** In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure.

**Follow-up:** Why not swallow cancellation?

**Answer:** `CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency.

**Follow-up:** What should you avoid?

**Answer:** Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership.

### 4. Flow event modeling.

**Senior answer**

"I would start by saying Flow is an asynchronous stream with backpressure through suspension. Cold flows run per collector; hot flows exist independently of a collector. `StateFlow` represents current state with a latest value, while `SharedFlow` is for shared emissions and can be configured for replay. Operator placement matters: `flowOn` changes upstream context, `catch` catches upstream exceptions, and `collectLatest` cancels the previous collector block when a new value arrives. In Android, I collect with lifecycle awareness and model one-off events deliberately so navigation or snackbars do not replay after rotation."

**Tricky follow-ups answered**

**Follow-up:** Cold or hot?

**Answer:** Cold Flow starts per collector. StateFlow and SharedFlow are hot and can exist independently of a collector.

**Follow-up:** What does operator placement change?

**Answer:** `flowOn` affects upstream context; `catch` catches upstream failures; downstream collector failures are not caught by an upstream `catch`.

**Follow-up:** How do you collect safely in Android?

**Answer:** Use lifecycle-aware collection such as `repeatOnLifecycle` or Compose lifecycle-aware state collection.

**Follow-up:** How do you avoid event replay bugs?

**Answer:** Model events deliberately, choose replay behavior explicitly, and make one-off navigation/snackbar behavior lifecycle-aware.

### 5. Compose recomposition bug.

**Senior answer**

"I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."

**Tricky follow-ups answered**

**Follow-up:** What triggers recomposition?

**Answer:** Reads of snapshot state changing can invalidate composables that read that state.

**Follow-up:** What should be hoisted?

**Answer:** Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI.

**Follow-up:** Why can mutable lists fail?

**Answer:** Mutating a normal list in place may not change observable state, so Compose may not know to recompose.

**Follow-up:** What do you measure?

**Answer:** Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing.

### 6. Repository/source of truth design.

**Senior answer**

"I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."

**Tricky follow-ups answered**

**Follow-up:** Who owns what?

**Answer:** UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction.

**Follow-up:** When is a layer overkill?

**Answer:** When it only forwards calls without protecting a boundary, rule, test seam, or expected change.

**Follow-up:** What makes it testable?

**Answer:** Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes.

**Follow-up:** What trade-off should you name?

**Answer:** Complexity, team size, feature volatility, release risk, module boundaries, and migration cost.

### 7. Offline write sync design.

**Senior answer**

"I would design for mobile failure first: flaky network, process death, auth changes, offline use, retries, duplicate submissions, battery, and OS background limits. A durable local source of truth gives UI a stable model. Pending operations need IDs, status, retry policy, idempotency keys, and reconciliation rules. WorkManager handles deferrable persistent background work; foreground service is for user-visible ongoing work. Conflicts require a product policy, not just code. A senior answer includes logout behavior, token refresh, cache invalidation, monitoring, and how the system recovers after restart without losing or duplicating user work."

**Tricky follow-ups answered**

**Follow-up:** What is the durable truth?

**Answer:** Usually Room or another persistent store observed by UI, with repositories/workers reconciling network state into it.

**Follow-up:** How do retries stay safe?

**Answer:** Persist operations with stable IDs, idempotency keys, retry policy, and terminal failure states.

**Follow-up:** How do you handle conflicts?

**Answer:** Choose a product policy: server wins, client wins, last-write-wins, merge, or user resolution.

**Follow-up:** What do you monitor?

**Answer:** Queue age, retry count, conflict rate, auth failures, duplicate attempts, terminal failures, and crash/error spikes.

### 8. ViewModel test strategy.

**Senior answer**

"I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."

**Tricky follow-ups answered**

**Follow-up:** What must the test control?

**Answer:** Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services.

**Follow-up:** Why avoid sleeps?

**Answer:** Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic.

**Follow-up:** When are fakes better than mocks?

**Answer:** When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks.

**Follow-up:** Which failure paths should be covered?

**Answer:** Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases.

### 9. Release crash spike.

**Senior answer**

"I would start with evidence and threat model. For performance, measure frame timing, main-thread work, startup path, allocations, I/O, and traces using Perfetto, Android Studio Profiler, Macrobenchmark, Baseline Profiles, Android Vitals, and LeakCanary when memory is involved. For security and release, assume the APK is inspectable and the client is not fully trusted: protect tokens, validate entry points, minimize exported surfaces, be careful with WebView bridges, and test minified release builds. R8, keep rules, mapping files, staged rollout, crash monitoring, and rollback strategy are part of the production answer, not afterthoughts."

**Tricky follow-ups answered**

**Follow-up:** What do you measure first?

**Answer:** Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue.

**Follow-up:** What can release builds change?

**Answer:** R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps.

**Follow-up:** Can secrets be hidden in an APK?

**Answer:** No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity.

**Follow-up:** What is the production answer?

**Answer:** Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix.

### 10. Architecture disagreement story.

**Senior answer**

"I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."

**Tricky follow-ups answered**

**Follow-up:** What should the story prove?

**Answer:** Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket.

**Follow-up:** What trade-off should you name?

**Answer:** Time, risk, scope, team adoption, migration cost, product impact, or reversibility.

**Follow-up:** How do you avoid sounding defensive?

**Answer:** Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person.

**Follow-up:** How do you show ownership without bragging?

**Answer:** Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward.

## Round 11: External Alignment Expansion

Time: 60 minutes

Study before this round:

- `STUDY-GUIDE.md` Parts 11-15.
- `QUESTION-BANK.md` questions 229-272.

Score target: 52/60 or higher.

### 1. What is WorkManager?

**Senior answer**

"I would describe WorkManager as the Android API for deferrable persistent work, not as a generic background thread. It is a good fit when work should survive process death, respect constraints like network or charging, and retry with backoff. `OneTimeWorkRequest` handles one-off jobs; `PeriodicWorkRequest` handles recurring work with minimum interval limits. A `CoroutineWorker` is the common Kotlin choice when the work is suspend-friendly. The senior trap is immediacy: WorkManager is scheduled by the OS and is not a promise that work starts now. For user-visible ongoing work, I compare foreground service policy, notifications, and product expectations."

**Tricky follow-ups answered**

**Follow-up:** When should WorkManager not be used?

**Answer:** Do not use it for immediate user-visible ongoing work, short in-process async work, or exact alarms. Compare foreground services, coroutines, and alarms based on the guarantee.

**Follow-up:** What makes retries safe?

**Answer:** Persist input data, use idempotency keys or stable operation IDs, choose backoff, and make server writes safe to repeat.

**Follow-up:** What do constraints actually mean?

**Answer:** Constraints describe when work is eligible to run, such as network, charging, storage, or battery conditions. They do not guarantee immediate execution.

**Follow-up:** How do you observe and cancel work?

**Answer:** Use `WorkInfo`, unique work names, tags, chains, and cancellation APIs so UI and repositories can reason about work state.

### 2. WorkManager vs coroutine vs foreground service?

**Senior answer**

"I would describe WorkManager as the Android API for deferrable persistent work, not as a generic background thread. It is a good fit when work should survive process death, respect constraints like network or charging, and retry with backoff. `OneTimeWorkRequest` handles one-off jobs; `PeriodicWorkRequest` handles recurring work with minimum interval limits. A `CoroutineWorker` is the common Kotlin choice when the work is suspend-friendly. The senior trap is immediacy: WorkManager is scheduled by the OS and is not a promise that work starts now. For user-visible ongoing work, I compare foreground service policy, notifications, and product expectations."

**Tricky follow-ups answered**

**Follow-up:** When should WorkManager not be used?

**Answer:** Do not use it for immediate user-visible ongoing work, short in-process async work, or exact alarms. Compare foreground services, coroutines, and alarms based on the guarantee.

**Follow-up:** What makes retries safe?

**Answer:** Persist input data, use idempotency keys or stable operation IDs, choose backoff, and make server writes safe to repeat.

**Follow-up:** What do constraints actually mean?

**Answer:** Constraints describe when work is eligible to run, such as network, charging, storage, or battery conditions. They do not guarantee immediate execution.

**Follow-up:** How do you observe and cancel work?

**Answer:** Use `WorkInfo`, unique work names, tags, chains, and cancellation APIs so UI and repositories can reason about work state.

### 3. `OneTimeWorkRequest` vs `PeriodicWorkRequest`?

**Senior answer**

"I would describe WorkManager as the Android API for deferrable persistent work, not as a generic background thread. It is a good fit when work should survive process death, respect constraints like network or charging, and retry with backoff. `OneTimeWorkRequest` handles one-off jobs; `PeriodicWorkRequest` handles recurring work with minimum interval limits. A `CoroutineWorker` is the common Kotlin choice when the work is suspend-friendly. The senior trap is immediacy: WorkManager is scheduled by the OS and is not a promise that work starts now. For user-visible ongoing work, I compare foreground service policy, notifications, and product expectations."

**Tricky follow-ups answered**

**Follow-up:** When should WorkManager not be used?

**Answer:** Do not use it for immediate user-visible ongoing work, short in-process async work, or exact alarms. Compare foreground services, coroutines, and alarms based on the guarantee.

**Follow-up:** What makes retries safe?

**Answer:** Persist input data, use idempotency keys or stable operation IDs, choose backoff, and make server writes safe to repeat.

**Follow-up:** What do constraints actually mean?

**Answer:** Constraints describe when work is eligible to run, such as network, charging, storage, or battery conditions. They do not guarantee immediate execution.

**Follow-up:** How do you observe and cancel work?

**Answer:** Use `WorkInfo`, unique work names, tags, chains, and cancellation APIs so UI and repositories can reason about work state.

### 4. How do you test WorkManager?

**Senior answer**

"I test WorkManager by making scheduled work deterministic. I initialize WorkManager with a test configuration, enqueue the `WorkRequest`, and use the test driver to mark constraints or initial delays as met instead of waiting for real time or real network. Then I assert `WorkInfo` state, output data, retry/failure behavior, and the durable side effect, such as a database record changing from pending to synced. Dependencies should be fake or injected, especially network clients, repositories, and clocks. For a senior answer, I would also test process-recovery assumptions indirectly: persisted input data, idempotent operation IDs, retry policy, and no duplicate server writes."

**Tricky follow-ups answered**

**Follow-up:** When should WorkManager not be used?

**Answer:** Do not use it for immediate user-visible ongoing work, short in-process async work, or exact alarms. Compare foreground services, coroutines, and alarms based on the guarantee.

**Follow-up:** What makes retries safe?

**Answer:** Persist input data, use idempotency keys or stable operation IDs, choose backoff, and make server writes safe to repeat.

**Follow-up:** What do constraints actually mean?

**Answer:** Constraints describe when work is eligible to run, such as network, charging, storage, or battery conditions. They do not guarantee immediate execution.

**Follow-up:** How do you observe and cancel work?

**Answer:** Use `WorkInfo`, unique work names, tags, chains, and cancellation APIs so UI and repositories can reason about work state.

### 5. Retrofit vs OkHttp?

**Senior answer**

"I would separate networking responsibilities clearly. Retrofit describes the HTTP API interface and converts responses; OkHttp owns the lower-level client, interceptors, connection behavior, caching, and authenticators. I model errors explicitly: network failure, HTTP error, serialization error, auth failure, and domain failure are not the same. Token refresh should avoid races, usually through an authenticator or synchronized refresh path, and retries for writes need idempotency keys so duplicate submissions do not happen. In Android architecture, networking should be a data-source boundary; repositories map DTOs, enforce cache freshness, and expose stable domain or UI state."

**Tricky follow-ups answered**

**Follow-up:** Interceptor or authenticator?

**Answer:** Interceptors modify or observe requests/responses. Authenticators respond to authentication challenges and are the safer place for coordinated token refresh.

**Follow-up:** How do you model API errors?

**Answer:** Separate network failures, HTTP status failures, serialization failures, auth failures, and domain errors so UI and retry policy can react correctly.

**Follow-up:** How do you prevent duplicate writes?

**Answer:** Use idempotency keys or operation IDs for retryable POST/PUT work and persist pending operation state.

**Follow-up:** Where does networking logic belong?

**Answer:** Data sources own API mechanics; repositories own policy, mapping, cache freshness, and exposed domain state.

### 6. Interceptor vs Authenticator?

**Senior answer**

"I would separate networking responsibilities clearly. Retrofit describes the HTTP API interface and converts responses; OkHttp owns the lower-level client, interceptors, connection behavior, caching, and authenticators. I model errors explicitly: network failure, HTTP error, serialization error, auth failure, and domain failure are not the same. Token refresh should avoid races, usually through an authenticator or synchronized refresh path, and retries for writes need idempotency keys so duplicate submissions do not happen. In Android architecture, networking should be a data-source boundary; repositories map DTOs, enforce cache freshness, and expose stable domain or UI state."

**Tricky follow-ups answered**

**Follow-up:** Interceptor or authenticator?

**Answer:** Interceptors modify or observe requests/responses. Authenticators respond to authentication challenges and are the safer place for coordinated token refresh.

**Follow-up:** How do you model API errors?

**Answer:** Separate network failures, HTTP status failures, serialization failures, auth failures, and domain errors so UI and retry policy can react correctly.

**Follow-up:** How do you prevent duplicate writes?

**Answer:** Use idempotency keys or operation IDs for retryable POST/PUT work and persist pending operation state.

**Follow-up:** Where does networking logic belong?

**Answer:** Data sources own API mechanics; repositories own policy, mapping, cache freshness, and exposed domain state.

### 7. How do you avoid token refresh race conditions?

**Senior answer**

"I would separate networking responsibilities clearly. Retrofit describes the HTTP API interface and converts responses; OkHttp owns the lower-level client, interceptors, connection behavior, caching, and authenticators. I model errors explicitly: network failure, HTTP error, serialization error, auth failure, and domain failure are not the same. Token refresh should avoid races, usually through an authenticator or synchronized refresh path, and retries for writes need idempotency keys so duplicate submissions do not happen. In Android architecture, networking should be a data-source boundary; repositories map DTOs, enforce cache freshness, and expose stable domain or UI state."

**Tricky follow-ups answered**

**Follow-up:** Interceptor or authenticator?

**Answer:** Interceptors modify or observe requests/responses. Authenticators respond to authentication challenges and are the safer place for coordinated token refresh.

**Follow-up:** How do you model API errors?

**Answer:** Separate network failures, HTTP status failures, serialization failures, auth failures, and domain errors so UI and retry policy can react correctly.

**Follow-up:** How do you prevent duplicate writes?

**Answer:** Use idempotency keys or operation IDs for retryable POST/PUT work and persist pending operation state.

**Follow-up:** Where does networking logic belong?

**Answer:** Data sources own API mechanics; repositories own policy, mapping, cache freshness, and exposed domain state.

### 8. How do you model API errors?

**Senior answer**

"I would separate networking responsibilities clearly. Retrofit describes the HTTP API interface and converts responses; OkHttp owns the lower-level client, interceptors, connection behavior, caching, and authenticators. I model errors explicitly: network failure, HTTP error, serialization error, auth failure, and domain failure are not the same. Token refresh should avoid races, usually through an authenticator or synchronized refresh path, and retries for writes need idempotency keys so duplicate submissions do not happen. In Android architecture, networking should be a data-source boundary; repositories map DTOs, enforce cache freshness, and expose stable domain or UI state."

**Tricky follow-ups answered**

**Follow-up:** Interceptor or authenticator?

**Answer:** Interceptors modify or observe requests/responses. Authenticators respond to authentication challenges and are the safer place for coordinated token refresh.

**Follow-up:** How do you model API errors?

**Answer:** Separate network failures, HTTP status failures, serialization failures, auth failures, and domain errors so UI and retry policy can react correctly.

**Follow-up:** How do you prevent duplicate writes?

**Answer:** Use idempotency keys or operation IDs for retryable POST/PUT work and persist pending operation state.

**Follow-up:** Where does networking logic belong?

**Answer:** Data sources own API mechanics; repositories own policy, mapping, cache freshness, and exposed domain state.

### 9. Debug vs release build?

**Senior answer**

"I would answer build and release questions as production risk management. Build variants combine build types and product flavors; release builds differ from debug through minification, signing, debuggability, resources, and sometimes backend endpoints. Android delivery usually uses an AAB for Play, while APKs are installable artifacts useful for local or specific distribution. A healthy CI pipeline runs lint, unit tests, relevant instrumentation tests, static analysis, build verification, signing checks, and release artifact generation. For senior Android work, I also mention versionCode/versionName, mapping files, staged rollout, rollback strategy, dependency locking/version catalogs, and modular build performance."

**Tricky follow-ups answered**

**Follow-up:** What differs between debug and release?

**Answer:** Release builds are signed, usually minified/optimized, not debuggable, may use different config, and must be tested because R8 and resources can change behavior.

**Follow-up:** APK or AAB?

**Answer:** AAB is the Play delivery artifact; APK is an installable package. A senior answer names delivery, testing, and distribution implications.

**Follow-up:** What should CI verify?

**Answer:** Lint, unit tests, selected instrumentation tests, static analysis, dependency checks, build variants, signing configuration, and release artifact creation.

**Follow-up:** What release files matter after shipping?

**Answer:** Mapping files, version metadata, changelog/rollout notes, crash dashboards, and the ability to rollback or hotfix.

### 10. APK vs AAB?

**Senior answer**

"I would answer build and release questions as production risk management. Build variants combine build types and product flavors; release builds differ from debug through minification, signing, debuggability, resources, and sometimes backend endpoints. Android delivery usually uses an AAB for Play, while APKs are installable artifacts useful for local or specific distribution. A healthy CI pipeline runs lint, unit tests, relevant instrumentation tests, static analysis, build verification, signing checks, and release artifact generation. For senior Android work, I also mention versionCode/versionName, mapping files, staged rollout, rollback strategy, dependency locking/version catalogs, and modular build performance."

**Tricky follow-ups answered**

**Follow-up:** What differs between debug and release?

**Answer:** Release builds are signed, usually minified/optimized, not debuggable, may use different config, and must be tested because R8 and resources can change behavior.

**Follow-up:** APK or AAB?

**Answer:** AAB is the Play delivery artifact; APK is an installable package. A senior answer names delivery, testing, and distribution implications.

**Follow-up:** What should CI verify?

**Answer:** Lint, unit tests, selected instrumentation tests, static analysis, dependency checks, build variants, signing configuration, and release artifact creation.

**Follow-up:** What release files matter after shipping?

**Answer:** Mapping files, version metadata, changelog/rollout notes, crash dashboards, and the ability to rollback or hotfix.

### 11. What should CI/CD verify for Android?

**Senior answer**

"I would answer build and release questions as production risk management. Build variants combine build types and product flavors; release builds differ from debug through minification, signing, debuggability, resources, and sometimes backend endpoints. Android delivery usually uses an AAB for Play, while APKs are installable artifacts useful for local or specific distribution. A healthy CI pipeline runs lint, unit tests, relevant instrumentation tests, static analysis, build verification, signing checks, and release artifact generation. For senior Android work, I also mention versionCode/versionName, mapping files, staged rollout, rollback strategy, dependency locking/version catalogs, and modular build performance."

**Tricky follow-ups answered**

**Follow-up:** What differs between debug and release?

**Answer:** Release builds are signed, usually minified/optimized, not debuggable, may use different config, and must be tested because R8 and resources can change behavior.

**Follow-up:** APK or AAB?

**Answer:** AAB is the Play delivery artifact; APK is an installable package. A senior answer names delivery, testing, and distribution implications.

**Follow-up:** What should CI verify?

**Answer:** Lint, unit tests, selected instrumentation tests, static analysis, dependency checks, build variants, signing configuration, and release artifact creation.

**Follow-up:** What release files matter after shipping?

**Answer:** Mapping files, version metadata, changelog/rollout notes, crash dashboards, and the ability to rollback or hotfix.

### 12. How do you design staged rollout and rollback?

**Senior answer**

"I would answer build and release questions as production risk management. Build variants combine build types and product flavors; release builds differ from debug through minification, signing, debuggability, resources, and sometimes backend endpoints. Android delivery usually uses an AAB for Play, while APKs are installable artifacts useful for local or specific distribution. A healthy CI pipeline runs lint, unit tests, relevant instrumentation tests, static analysis, build verification, signing checks, and release artifact generation. For senior Android work, I also mention versionCode/versionName, mapping files, staged rollout, rollback strategy, dependency locking/version catalogs, and modular build performance."

**Tricky follow-ups answered**

**Follow-up:** What differs between debug and release?

**Answer:** Release builds are signed, usually minified/optimized, not debuggable, may use different config, and must be tested because R8 and resources can change behavior.

**Follow-up:** APK or AAB?

**Answer:** AAB is the Play delivery artifact; APK is an installable package. A senior answer names delivery, testing, and distribution implications.

**Follow-up:** What should CI verify?

**Answer:** Lint, unit tests, selected instrumentation tests, static analysis, dependency checks, build variants, signing configuration, and release artifact creation.

**Follow-up:** What release files matter after shipping?

**Answer:** Mapping files, version metadata, changelog/rollout notes, crash dashboards, and the ability to rollback or hotfix.

### 13. What should TalkBack announce?

**Senior answer**

"I would treat accessibility as part of the UI contract, not polish after the screen is done. In Compose and Views, interactive elements need meaningful labels, state descriptions when useful, correct roles/semantics, adequate touch targets, font-scale support, contrast, focus order, and TalkBack behavior that matches the product action. A design system helps because accessibility rules can live in reusable components: buttons, inputs, dialogs, list items, and error states. For testing, I would combine manual TalkBack checks, semantics assertions, screenshot/golden review where useful, and regression checks for font scale and small screens."

**Tricky follow-ups answered**

**Follow-up:** What should TalkBack announce?

**Answer:** It should announce the element purpose, state, and action in a way that matches what sighted users understand from the UI.

**Follow-up:** What breaks with font scale?

**Answer:** Fixed-height layouts, clipped text, overlapping controls, and custom components that ignore dynamic type can break at large font scales.

**Follow-up:** How does a design system help?

**Answer:** It centralizes accessible component behavior: labels, focus, roles, contrast, touch targets, and error states.

**Follow-up:** How do you test accessibility?

**Answer:** Use semantics assertions, manual TalkBack checks, font-scale checks, contrast review, and regression tests for reusable components.

### 14. What is the Compose semantics tree?

**Senior answer**

"I would treat accessibility as part of the UI contract, not polish after the screen is done. In Compose and Views, interactive elements need meaningful labels, state descriptions when useful, correct roles/semantics, adequate touch targets, font-scale support, contrast, focus order, and TalkBack behavior that matches the product action. A design system helps because accessibility rules can live in reusable components: buttons, inputs, dialogs, list items, and error states. For testing, I would combine manual TalkBack checks, semantics assertions, screenshot/golden review where useful, and regression checks for font scale and small screens."

**Tricky follow-ups answered**

**Follow-up:** What should TalkBack announce?

**Answer:** It should announce the element purpose, state, and action in a way that matches what sighted users understand from the UI.

**Follow-up:** What breaks with font scale?

**Answer:** Fixed-height layouts, clipped text, overlapping controls, and custom components that ignore dynamic type can break at large font scales.

**Follow-up:** How does a design system help?

**Answer:** It centralizes accessible component behavior: labels, focus, roles, contrast, touch targets, and error states.

**Follow-up:** How do you test accessibility?

**Answer:** Use semantics assertions, manual TalkBack checks, font-scale checks, contrast review, and regression tests for reusable components.

### 15. How do design systems improve accessibility?

**Senior answer**

"I would treat accessibility as part of the UI contract, not polish after the screen is done. In Compose and Views, interactive elements need meaningful labels, state descriptions when useful, correct roles/semantics, adequate touch targets, font-scale support, contrast, focus order, and TalkBack behavior that matches the product action. A design system helps because accessibility rules can live in reusable components: buttons, inputs, dialogs, list items, and error states. For testing, I would combine manual TalkBack checks, semantics assertions, screenshot/golden review where useful, and regression checks for font scale and small screens."

**Tricky follow-ups answered**

**Follow-up:** What should TalkBack announce?

**Answer:** It should announce the element purpose, state, and action in a way that matches what sighted users understand from the UI.

**Follow-up:** What breaks with font scale?

**Answer:** Fixed-height layouts, clipped text, overlapping controls, and custom components that ignore dynamic type can break at large font scales.

**Follow-up:** How does a design system help?

**Answer:** It centralizes accessible component behavior: labels, focus, roles, contrast, touch targets, and error states.

**Follow-up:** How do you test accessibility?

**Answer:** Use semantics assertions, manual TalkBack checks, font-scale checks, contrast review, and regression tests for reusable components.

### 16. What is Kotlin Multiplatform?

**Senior answer**

"I would describe Kotlin Multiplatform as a way to share selected Kotlin code across platforms, not a reason to force the whole app into one shared layer. Good candidates for sharing are domain rules, validation, networking models, serialization, and use-case logic when platform dependencies are controlled. UI, navigation, permissions, background execution, platform security, and device integrations often stay native. `expect/actual` is useful when shared code needs a platform-specific implementation behind a common API. The senior answer is cautious: KMP can reduce duplicated business logic, but sharing too much can increase interop cost, build complexity, and team coordination overhead."

**Tricky follow-ups answered**

**Follow-up:** What should be shared?

**Answer:** Share stable business rules, validation, models, serialization, and use-case logic when platform dependencies are controlled.

**Follow-up:** What should usually stay native?

**Answer:** UI, navigation, permissions, background execution, platform security, and device integrations often stay platform-specific.

**Follow-up:** What is `expect/actual` for?

**Answer:** It lets shared code depend on a common API while each platform provides its own implementation.

**Follow-up:** What is the main risk?

**Answer:** Sharing too much can increase build complexity, interop cost, platform compromises, and team coordination overhead.

### 17. What should usually stay native in a KMP architecture?

**Senior answer**

"I would describe Kotlin Multiplatform as a way to share selected Kotlin code across platforms, not a reason to force the whole app into one shared layer. Good candidates for sharing are domain rules, validation, networking models, serialization, and use-case logic when platform dependencies are controlled. UI, navigation, permissions, background execution, platform security, and device integrations often stay native. `expect/actual` is useful when shared code needs a platform-specific implementation behind a common API. The senior answer is cautious: KMP can reduce duplicated business logic, but sharing too much can increase interop cost, build complexity, and team coordination overhead."

**Tricky follow-ups answered**

**Follow-up:** What should be shared?

**Answer:** Share stable business rules, validation, models, serialization, and use-case logic when platform dependencies are controlled.

**Follow-up:** What should usually stay native?

**Answer:** UI, navigation, permissions, background execution, platform security, and device integrations often stay platform-specific.

**Follow-up:** What is `expect/actual` for?

**Answer:** It lets shared code depend on a common API while each platform provides its own implementation.

**Follow-up:** What is the main risk?

**Answer:** Sharing too much can increase build complexity, interop cost, platform compromises, and team coordination overhead.

### 18. What are the risks of sharing too much?

**Senior answer**

"I would describe Kotlin Multiplatform as a way to share selected Kotlin code across platforms, not a reason to force the whole app into one shared layer. Good candidates for sharing are domain rules, validation, networking models, serialization, and use-case logic when platform dependencies are controlled. UI, navigation, permissions, background execution, platform security, and device integrations often stay native. `expect/actual` is useful when shared code needs a platform-specific implementation behind a common API. The senior answer is cautious: KMP can reduce duplicated business logic, but sharing too much can increase interop cost, build complexity, and team coordination overhead."

**Tricky follow-ups answered**

**Follow-up:** What should be shared?

**Answer:** Share stable business rules, validation, models, serialization, and use-case logic when platform dependencies are controlled.

**Follow-up:** What should usually stay native?

**Answer:** UI, navigation, permissions, background execution, platform security, and device integrations often stay platform-specific.

**Follow-up:** What is `expect/actual` for?

**Answer:** It lets shared code depend on a common API while each platform provides its own implementation.

**Follow-up:** What is the main risk?

**Answer:** Sharing too much can increase build complexity, interop cost, platform compromises, and team coordination overhead.

