from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "interview-guide" / "STUDY-GUIDE.md"
MOCKS = ROOT / "interview-guide" / "MOCK-INTERVIEWS.md"


def norm(question: str) -> str:
    return re.sub(r"\s+", " ", question.replace("`", "")).strip().lower()


def has_any(text: str, needles: list[str]) -> bool:
    return any(n in text for n in needles)


def category(question: str) -> str:
    q = norm(question)

    behavior_phrases = [
        "tell me about",
        "code review conflict",
        "architecture disagreement",
        "lead without authority",
        "leading without authority",
        "mentored",
        "mentoring",
        "mistake",
        "production incident",
        "technical debt",
        "work with product",
        "product and design",
        "ambiguous requirements",
        "handled ambiguity",
        "pushed back on product",
        "team say is hard",
        "were wrong",
        "improved team process",
        "reversible decision",
    ]
    if has_any(q, behavior_phrases):
        return "behavior"

    if "local source of truth" in q:
        return "system"
    if has_any(q, ["how do you test release builds", "test release builds"]):
        return "perfsec"
    if has_any(q, ["test", "testing", "fakes", "mocks", "maindispatcherrule", "standardtestdispatcher", "unconfinedtestdispatcher", "advanceuntilidle", "turbine", "virtual time", "flaky"]):
        return "testing"

    if has_any(q, ["data class", "hashcode", "equals", "copy()", "copy(", "==", "===", "diffutil"]):
        return "data"
    if has_any(q, ["null", "npe", "platform type", "!!", "lateinit", "lazy", "empty list"]):
        return "nulls"
    if has_any(q, ["sealed", "enum", "loading", "empty, content", "api result", "result, sealed", "exceptions"]):
        return "modeling"
    if has_any(q, ["inline", "reified", "type erasure", "generics", " in and out", "in and out", "value class"]):
        return "types"
    if has_any(q, ["object declaration", "companion object", "extension function", "scope function"]):
        return "kotlin_objects"

    if has_any(q, ["memory leak", "leaks", "activity lifecycle", "fragment lifecycle", "configuration change", "rotation", "process death", "savedstatehandle", "saved state", "room or datastore", "viewmodel", "activity context", "application context", "oncreate", "onstart", "onresume", "fragment view lifecycle", "binding", "bundle"]):
        return "lifecycle"
    if has_any(q, ["permission", "intent", "deep link", "pendingintent", "broadcastreceiver", "service", "workmanager", "background location", "exported component", "back-stack", "task/back-stack"]):
        return "entrypoints"

    if has_any(q, ["coroutine", "suspend", "structured concurrency", "launch", "async", "withcontext", "supervisorscope", "coroutines cancellation", "cancellationexception", "globalscope", "dispatchers", "noncancellable"]):
        return "coroutines"
    if has_any(q, ["flow", "stateflow", "sharedflow", "flowon", "catch", "collect", "statein", "sharein", "channel", "callbackflow", "awaitclose", "debounce", "combine", "zip", "flatmaplatest", "maplatest", "one-off", "event modeling"]):
        return "flow"

    if has_any(q, ["compose", "recomposition", "state hoisting", "remember", "launchedeffect", "disposableeffect", "rememberupdatedstate", "lazycolumn", "snapshot state", "skippability", "derivedstateof", "semantics", "mutating a list", "navigation events"]):
        return "compose"

    if has_any(q, ["mvvm", "mvi", "clean architecture", "repository", "usecases", "use cases", "single source of truth", "dto", "domain model", "ui model", "viewmodel bloat", "modularize", "legacy", "hilt", "dagger", "koin", "dependency", "qualify dispatchers", "inject workers", "scope"]):
        return "architecture"
    if has_any(q, ["singleton", "factory", "adapter pattern", "observer pattern", "strategy pattern", "state pattern", "command pattern", "pattern"]):
        return "patterns"
    if has_any(q, ["offline", "sync", "chat", "photo upload", "retry", "foreground service", "offline writes", "conflict", "duplicate", "logout", "token refresh", "app startup", "feature flags", "pagination", "local source of truth"]):
        return "system"

    if has_any(q, ["jank", "anr", "startup performance", "performance", "tokens", "secrets", "certificate pinning", "r8", "release", "mapping files", "crash spike", "cold start", "warm start", "baseline profiles", "macrobenchmark", "leakcanary", "webview", "secure"]):
        return "perfsec"

    return "general"


def exact_answer(question: str) -> str | None:
    q = norm(question)

    if "what can go wrong if a mutable data class is used as a hashmap key" in q:
        return (
            "If a mutable data class is used as a `HashMap` key, the dangerous part is not the word data class; it is that the fields used by `equals` and `hashCode` can change after insertion. A hash map chooses a bucket from the original hash. If the key changes later, the object may now produce a different hash, so lookup, remove, or contains can fail even though the object is still physically inside the map. In an interview I would say: keys must be effectively immutable, or equality/hash code must be based only on stable identity. The same idea matters for `HashSet`, DiffUtil, and UI state comparisons."
        )
    if "how does generated equals work" in q or "how many comparisons can equals" in q:
        return (
            "For a data class, generated `equals` is ordinary structural equality over the primary-constructor properties. Conceptually it checks quick cases first, such as same reference and compatible type, then compares each primary-constructor property in order using that property's equality. If the class has five primary-constructor properties, it can compare up to five properties after the cheap checks, but it can stop earlier when the first property differs. Body properties are not part of that generated equality. I would also connect this to `==`: in Kotlin, `==` calls `equals`, while `===` asks whether both references point to the same object."
        )
    if "when is hashcode used" in q:
        return (
            "`hashCode` is used by hash-based collections such as `HashMap` and `HashSet` to narrow where an object might live. The collection uses the hash to find a bucket and then uses `equals` to confirm the actual match, because different objects can share a hash. The contract is: if two objects are equal, they must have the same hash code. The reverse is not guaranteed. For data classes, generated `hashCode` uses the same primary-constructor properties as generated `equals`, so mutating those properties after insertion into a hash collection can make the object hard or impossible to find through normal lookup."
        )
    if "what is a sealed class" in q or q == "sealed class vs enum?":
        return (
            "A sealed class represents a closed hierarchy: the compiler knows the permitted subtypes, so `when` expressions can be exhaustive without an `else` when every case is handled. I use it when alternatives carry different data or behavior, such as `Loading`, `Content(items)`, `Empty`, and `Error(cause)`. An enum is better for a fixed list of constants with the same shape, such as sort order or theme mode. The senior detail is choosing the model that makes impossible states impossible: sealed hierarchies are great for typed UI state and domain results, but they can be overkill for simple constant sets."
        )
    if "would you return null or an empty list" in q:
        return (
            "I would not choose `null` or empty list mechanically; I would choose based on meaning. An empty list means the request succeeded and there are currently zero items. `null` means absence, unknown, not loaded, or not applicable, and that should be explicit because it creates a different UI and data contract. In a repository, I usually avoid `null` collections unless absence is a real domain state. For loading/error/content, I prefer a typed result or UI-state model instead of overloading `null` and empty. That answer prevents bugs where an error or not-yet-loaded state is accidentally rendered as a valid empty screen."
        )
    if "what can go wrong with saving too much state in a bundle" in q:
        return (
            "A `Bundle` is for small, serializable state needed to restore navigation or UI after recreation, not for large object graphs or cached data. Saving too much can cause transaction-size failures, slow recreation, stale state, and duplicated sources of truth. I would save IDs, filters, selected tabs, scroll keys, and lightweight form fields. Large lists, images, entities, and derived data belong in Room, DataStore, files, memory cache, or should be reloaded by repository policy. The senior answer is ownership: saved instance state restores the screen contract; it should not become a database or a replacement for process-death-safe persistence."
        )
    if "what causes memory leaks in android" in q or "memory leaks usually happen" in q:
        return (
            "Android leaks usually happen when an object with a longer lifetime holds an object with a shorter lifetime. Common examples are a singleton holding an Activity context, a ViewModel holding a View or Fragment binding, a callback not being unregistered, a coroutine outliving the UI scope, or Fragment view binding surviving after `onDestroyView`. I would explain it as a lifetime mismatch, not just 'forgot to clear something'. The fix is to put work in the correct scope, use application context only for app-lifetime needs, clear view references at the view lifecycle boundary, unregister listeners, and verify suspicious cases with tools like LeakCanary."
        )
    if "what does catch catch" in q:
        return (
            "In Flow, `catch` catches exceptions from upstream of where the operator is placed. It does not catch exceptions thrown downstream by the collector, and it should not be used to hide cancellation. A senior answer names placement: `source.map { ... }.catch { ... }.collect { ... }` catches failures from `source` and `map`, but not failures inside `collect`. If I recover, I emit a fallback state or map the failure into a typed error. If the failure is `CancellationException`, I normally let it propagate because cancellation is part of structured concurrency, not an ordinary business error."
        )
    if "local source of truth" in q:
        return (
            "The local source of truth is the durable place the UI observes as authoritative for that feature, usually Room for relational/queryable app data or DataStore for small preferences. The repository coordinates network, cache freshness, mapping, and sync, but the UI should not juggle separate network and database truths. For an offline-first feature, writes are persisted locally with sync metadata, the UI reflects pending/synced/failed/conflicted states, and workers reconcile with the server. I would call it source of truth only if it survives process death and can recover after restart; an in-memory list inside a ViewModel is screen state, not the feature's durable truth."
        )
    if "how do you handle conflicts" in q or "sync conflicts" in q:
        return (
            "I would first ask what a conflict means for the product, because the right policy is domain-specific. Some data can use last-write-wins, some should be server-authoritative, some can merge field by field, and some must ask the user. Technically, I persist enough metadata to detect conflict: operation IDs, local version, remote version, updated timestamps when they are meaningful, and server response state. The UI should expose conflicted or failed states instead of silently dropping work. A senior answer also mentions idempotency, retries, monitoring conflict rate, and a recovery path after process death or logout."
        )
    if "how do you handle code review conflict" in q or "code review conflict" in q:
        return (
            "I would handle a code review conflict by separating correctness, risk, and preference. If the comment is about correctness, security, lifecycle, or maintainability, I slow down and either fix it or explain the trade-off with evidence. If it is style or preference, I point to team conventions or propose a small consistent rule instead of debating taste. I try to move the discussion from personal opinion to code behavior: tests, complexity, ownership, rollout risk, and future maintenance. If we still disagree, I suggest a reversible decision, pair on the concern, or involve the owner of that area without turning the review into a status contest."
        )
    if "what would your team say is hard about working with you" in q:
        return (
            "I would answer with a real edge, not a fake weakness. For example: I can push hard for clarity when ownership or failure modes are vague, and that can feel intense if I do not first align on urgency. Then I would show the mitigation: I now separate must-fix risks from preferences, write down trade-offs, ask whether the team needs a quick decision or deeper design, and invite disagreement earlier. The senior signal is self-awareness plus a changed behavior. I should not say 'I care too much' or blame others; I should show that my strength has a cost and that I manage that cost."
        )
    if "what do you do after a crash spike" in q or "crash spikes" in q:
        return (
            "After a crash spike, I first protect users: check rollout percentage, affected version, crash-free users, stack traces, device/API concentration, feature flags, and whether we should pause or roll back. Then I group crashes by root cause, deobfuscate with mapping files, reproduce if possible, and look for recent changes around the failing path. The fix should be small, reviewed, and released with monitoring. I would also add a regression test or guardrail when possible. The senior part is operational discipline: do not randomly patch symptoms, preserve evidence, communicate impact, and verify the spike actually drops after mitigation."
        )
    if "how do you test viewmodel" in q or "test viewmodel state" in q:
        return (
            "I test ViewModel state by driving the public inputs and asserting the emitted state sequence. If the ViewModel uses coroutines or Flow, I run the test with `runTest`, replace Main with a test dispatcher rule, inject dispatchers instead of hardcoding them, and use fakes for repositories so the test controls data and errors. I assert the initial state, loading state when relevant, success, empty, and failure paths. I avoid testing private functions or implementation timing. The important senior detail is determinism: no real network, no real delays, no uncontrolled dispatcher, and no assertion that depends on scheduler luck."
        )
    if "how do you test coroutines" in q:
        return (
            "I test coroutine code with `runTest` so delays use virtual time and child coroutines are tracked by the test scope. I inject dispatchers or a dispatcher provider so production code does not hardcode Main, IO, or Default in a way the test cannot control. For code that launches work, I advance the scheduler and assert observable state, returned results, or side effects through fakes. I also test cancellation and error paths, not just success. A good interview answer says I avoid `Thread.sleep`, avoid real dispatchers in unit tests, and make structured concurrency visible to the test instead of hiding work in global scopes."
        )
    if "how do you test flow emissions" in q or "what is turbine used for" in q:
        return (
            "I test Flow by collecting it in a controlled coroutine test and asserting emissions in order. Turbine is useful because it lets me `awaitItem`, assert completion or errors, and check that no unexpected events arrived. For `StateFlow`, I remember there is always an initial value, so the test should account for that before later emissions. For never-ending flows, I cancel the collection or use Turbine's cancellation helpers so the test does not hang. The senior detail is operator and lifecycle awareness: I control upstream fakes, virtual time for debounce/retry, and I assert behavior rather than the internal chain of operators."
        )
    if "how do you test workmanager" in q:
        return (
            "I test WorkManager by making scheduled work deterministic. I initialize WorkManager with a test configuration, enqueue the `WorkRequest`, and use the test driver to mark constraints or initial delays as met instead of waiting for real time or real network. Then I assert `WorkInfo` state, output data, retry/failure behavior, and the durable side effect, such as a database record changing from pending to synced. Dependencies should be fake or injected, especially network clients, repositories, and clocks. For a senior answer, I would also test process-recovery assumptions indirectly: persisted input data, idempotent operation IDs, retry policy, and no duplicate server writes."
        )
    if "workmanager vs foreground service" in q or "broadcastreceiver vs service vs workmanager" in q:
        return (
            "I choose between WorkManager, foreground service, service, receiver, and coroutine by lifetime, immediacy, user visibility, and OS policy. WorkManager is for deferrable persistent work that should survive process death and can run with constraints, retry, and backoff; it is not a promise of immediate execution. A foreground service is for ongoing user-visible work that must continue now, with a notification and foreground-service type restrictions. A BroadcastReceiver should do short event handling and hand off longer work. A coroutine is only in-process work tied to a scope, so it is not enough for durable sync or upload after the process dies."
        )
    return None


def category_answer(question: str, cat: str) -> str:
    q = question.strip()
    if cat == "data":
        return (
            "I would anchor the answer in Kotlin's value semantics. Data classes generate `equals`, `hashCode`, `toString`, `copy`, and `componentN` functions from primary-constructor properties only. `==` delegates to `equals`, while `===` is reference identity. Generated equality compares those constructor properties, and generated hash code must stay consistent with equality. The practical risk is mutability: `copy()` is shallow, nested mutable objects are shared, and changing a property used by hash code after insertion into a `HashMap` or `HashSet` can break lookup. So I use data classes for stable values, DTOs, UI state, and simple domain models, not for identity-heavy mutable objects."
        )
    if cat == "nulls":
        return (
            "I would explain Kotlin null-safety as a type-system tool, not a magic shield. `String` and `String?` are different contracts, Java platform types can still surprise you, `!!` converts uncertainty into a possible crash, and `lateinit` fails at runtime if read before initialization. In senior code I prefer explicit modeling: nullable only when absence is meaningful, empty collections when the result is valid but empty, and sealed/result types when I need loading, error, or permission states. The answer should name the remaining NPE paths and show how I keep nullability at boundaries instead of spreading defensive checks everywhere."
        )
    if cat == "modeling":
        return (
            "I would focus on modeling the allowed states. Kotlin gives me enums for fixed constants, sealed classes or sealed interfaces for closed alternatives that may carry different data, and typed results for success/failure flows. In Android this matters because UI often has distinct states: loading, empty, content, error, permission required, or stale cached content. A sealed model makes the `when` exhaustive and prevents impossible combinations like `isLoading=true` with stale error data unless I intentionally model that. I would still avoid over-modeling: if the values are simple constants with the same shape, an enum is easier to read and maintain."
        )
    if cat == "types":
        return (
            "I would connect the language feature to runtime behavior. JVM generics are erased, so `reified` only works with `inline` because the compiler copies the function body at call sites and can substitute the real type token. Variance controls safe substitution: `out` is for producers I read from, `in` is for consumers I write into. Value classes can make domain IDs and small wrappers more type-safe with less allocation in many cases, but they still have boxing edges. The senior angle is not naming features; it is knowing when they make APIs safer and when they make code clever without improving the model."
        )
    if cat == "kotlin_objects":
        return (
            "I would describe how Kotlin resolves the construct and what bug it can create. `object` creates a singleton, a companion object holds class-associated members, and extension functions are statically resolved by the declared receiver type. That means extensions do not truly override members; member functions win. Scope functions are useful for local object configuration or transformations, but they hurt readability when nested or when `it`/`this` hides ownership. In senior Android code I care less about using every Kotlin feature and more about whether the feature clarifies lifetime, dependency ownership, API shape, and testability."
        )
    if cat == "lifecycle":
        return (
            "I would answer in terms of lifetime ownership. Activities, Fragments, Fragment views, ViewModels, saved state, and durable storage all survive different things. ViewModel can survive configuration change, but not process death. `SavedStateHandle` and saved instance state are for small restoration keys and UI inputs, while Room/DataStore handle durable data. Fragment view references die at `onDestroyView`, even if the Fragment instance remains. Most leaks are lifetime mismatches: long-lived objects holding Activity, View, binding, callbacks, or coroutines. A senior answer names what survives rotation, what survives process death, and which owner should clean up."
        )
    if cat == "entrypoints":
        return (
            "I would treat Android entry points as lifecycle and trust-boundary problems. Intents, deep links, permissions, PendingIntents, broadcasts, services, WorkManager, and exported components can be triggered by the system, another app, a notification, a cold start, or restored state. I validate extras, IDs, auth/session state, URI ownership, and destination before doing privileged work. For background work I choose based on guarantee and visibility: WorkManager for deferrable persistent work, foreground service for user-visible ongoing work, and receivers only for short event handling. The senior answer includes cold-start behavior, OS limits, security, and user-visible recovery."
        )
    if cat == "coroutines":
        return (
            "I would explain coroutine ownership before syntax. A coroutine is a cancellable unit of async work running in a `CoroutineScope`; it is not the same thing as a thread. `suspend` means the function can suspend without blocking, but it does not automatically switch dispatchers. Structured concurrency means child work is tied to a parent lifetime, so cancellation and failure propagate predictably unless a supervisor boundary is used. `launch` returns `Job`, `async` returns `Deferred`, and `withContext` switches context for a result. I avoid `GlobalScope`, avoid blocking Main, and let `CancellationException` propagate."
        )
    if cat == "flow":
        return (
            "I would start by saying Flow is an asynchronous stream with backpressure through suspension. Cold flows run per collector; hot flows exist independently of a collector. `StateFlow` represents current state with a latest value, while `SharedFlow` is for shared emissions and can be configured for replay. Operator placement matters: `flowOn` changes upstream context, `catch` catches upstream exceptions, and `collectLatest` cancels the previous collector block when a new value arrives. In Android, I collect with lifecycle awareness and model one-off events deliberately so navigation or snackbars do not replay after rotation."
        )
    if cat == "compose":
        return (
            "I would frame Compose as state-driven UI. Recomposition reruns composable functions that read changed state; it does not mean the whole screen is redrawn. State should be hoisted to the owner that can make decisions: ViewModel for screen/business state, local `remember` for ephemeral UI state, and `rememberSaveable` for small values that should survive recreation. Effects like `LaunchedEffect` restart when keys change, so keys must represent the lifetime of the side effect. Performance answers should mention stable models, keys for lazy lists, avoiding mutable collections that Compose cannot observe, and measuring before optimizing."
        )
    if cat == "architecture":
        return (
            "I would answer with ownership boundaries, not architecture buzzwords. UI renders state and emits events. ViewModel owns screen state and user-intent handling. Repositories own data policy: network, database, cache, freshness, sync, and mapping. Data sources own framework or service details. Use cases are useful when a business operation is reused, complex, or deserves a named boundary. DI owns construction and lifetime. Clean Architecture, MVVM, and modularization are tools to control dependency direction and change, but each layer must earn its place. A senior answer names the boundary, the failure it prevents, and when a simpler design is better."
        )
    if cat == "patterns":
        return (
            "I would avoid reciting a pattern catalog and instead name the problem the pattern solves. Observer appears in Flow, LiveData, and UI state observation. Adapter maps one interface or model shape to another. Strategy swaps behavior such as sorting, validation, or retry policy. Factory centralizes object creation when construction has variants. Command can represent persisted offline operations. Singleton is acceptable for true process-wide stateless or coordinated resources, but dependency injection is better for testability and lifetime control. The senior answer also warns against pattern abuse: if the pattern hides simple code or ownership, it is hurting the design."
        )
    if cat == "system":
        return (
            "I would design for mobile failure first: flaky network, process death, auth changes, offline use, retries, duplicate submissions, battery, and OS background limits. A durable local source of truth gives UI a stable model. Pending operations need IDs, status, retry policy, idempotency keys, and reconciliation rules. WorkManager handles deferrable persistent background work; foreground service is for user-visible ongoing work. Conflicts require a product policy, not just code. A senior answer includes logout behavior, token refresh, cache invalidation, monitoring, and how the system recovers after restart without losing or duplicating user work."
        )
    if cat == "testing":
        return (
            "I would emphasize deterministic behavior. Coroutine tests should use `runTest`, injected dispatchers, a Main dispatcher rule when needed, and virtual time instead of sleeps. Flow tests should assert emissions, completion, errors, and absence of extra events; Turbine is useful for that. ViewModel tests should verify state transitions through public inputs, not internal implementation. Compose tests should use semantics and avoid timing assumptions. Room migrations need real schema migration checks, and WorkManager should use its test helpers. The senior answer says what is controlled: time, dispatchers, dependencies, lifecycle, data, and external services."
        )
    if cat == "perfsec":
        return (
            "I would start with evidence and threat model. For performance, measure frame timing, main-thread work, startup path, allocations, I/O, and traces using Perfetto, Android Studio Profiler, Macrobenchmark, Baseline Profiles, Android Vitals, and LeakCanary when memory is involved. For security and release, assume the APK is inspectable and the client is not fully trusted: protect tokens, validate entry points, minimize exported surfaces, be careful with WebView bridges, and test minified release builds. R8, keep rules, mapping files, staged rollout, crash monitoring, and rollback strategy are part of the production answer, not afterthoughts."
        )
    if cat == "behavior":
        return (
            "I would answer with one concrete story, but I would make the structure visible only through natural speech: context, constraint, action, trade-off, result, and what I changed afterward. For a senior Android role, the story should show impact beyond my own ticket: product alignment, technical judgment, risk management, communication, mentoring, and follow-through. I would avoid making other people the problem. If there was conflict, I would separate facts from preferences, show how I created options, and explain how the team converged. The answer should feel honest, specific, and reflective, not like a memorized leadership script."
        )
    return (
        "I would answer by naming the concept, the owner, the lifecycle boundary, the failure mode, and the trade-off. A senior Android answer should not stop at a definition. It should say what I would normally choose, when I would choose differently, and what bug the wrong choice creates. I would also mention how I would verify the behavior: unit test, integration test, profiler, release monitoring, or production metric depending on the risk. That makes the answer useful for interview study because it connects theory to the decisions an interviewer is usually probing."
    )


FOLLOWUPS = {
    "data": [
        ("What is the hidden edge case?", "Generated methods use only primary-constructor properties. Body properties can differ while instances still compare equal, and `copy()` will not copy body properties through parameters."),
        ("How does this fail in collections?", "Hash collections use `hashCode` to find a bucket and `equals` to confirm. If a key's hash-relevant state mutates, lookup and removal can fail."),
        ("What should you say about `copy()`?", "`copy()` is shallow. The outer instance is new, but nested mutable objects may still be shared."),
        ("How would you avoid this bug?", "Use immutable key fields, avoid mutable data classes as hash keys, or base equality/hash code only on stable identity."),
    ],
    "nulls": [
        ("Where can NPE still come from?", "Platform types, `!!`, `lateinit` before initialization, Java interop, reflection/serialization, and framework callbacks can still create runtime null failures."),
        ("When is `null` the right model?", "When absence is a real domain state. If the result is successfully empty, prefer an empty collection. If it is loading/error, model that explicitly."),
        ("Why is `!!` risky?", "It moves uncertainty from the type system into a runtime crash. It should be rare and backed by an invariant you can explain."),
        ("How do you keep nullability clean?", "Validate at boundaries, map platform types into Kotlin contracts, and avoid spreading nullable state deeper than necessary."),
    ],
    "modeling": [
        ("When is sealed better than enum?", "Use sealed when cases carry different data or behavior and you want exhaustive handling. Use enum for fixed same-shaped constants."),
        ("What bug does a state model prevent?", "It prevents impossible combinations such as loading plus content plus error unless that combination is intentionally represented."),
        ("What should the `when` expression show?", "It should handle every state explicitly, ideally exhaustively, so adding a new state forces compile-time review."),
        ("When is this overkill?", "When a simple Boolean, nullable field, or enum fully captures the domain without ambiguous combinations."),
    ],
    "types": [
        ("What is the runtime detail?", "Generic type information is erased on the JVM. `inline` plus `reified` lets the compiler substitute type information at call sites."),
        ("How do `in` and `out` map to use?", "`out` is for producers you read from; `in` is for consumers you write to. The goal is safe substitution."),
        ("Where can value classes surprise you?", "They can box at generic/interface/nullability boundaries, so they improve type safety but are not magic performance tools."),
        ("How do you avoid sounding theoretical?", "Tie the feature to safer API design, fewer invalid IDs, better typed boundaries, or avoiding unsafe casts."),
    ],
    "kotlin_objects": [
        ("What is statically resolved?", "Extension functions are resolved by the declared receiver type and do not override member functions."),
        ("When is `object` dangerous?", "When it hides global mutable state, makes tests order-dependent, or owns Android resources with unclear lifetime."),
        ("When do scope functions hurt?", "When nested calls hide which receiver is being used or when `it`/`this` obscures side effects."),
        ("How do you decide whether to use it?", "Use the feature only when it clarifies construction, ownership, or call-site readability."),
    ],
    "lifecycle": [
        ("What survives rotation?", "ViewModel can survive configuration change; Activity/Fragment views are recreated, and saved instance state can restore small UI state."),
        ("What survives process death?", "Durable persistence such as Room/DataStore and saved-state snapshots can survive. In-memory singletons and ViewModels do not."),
        ("Where do leaks usually come from?", "Long-lived objects retaining shorter-lived Activity, View, binding, callback, context, or coroutine references."),
        ("How do you decide the right owner?", "Use the shortest owner that can safely hold the state, then move only durable or cross-screen data to longer-lived storage."),
    ],
    "entrypoints": [
        ("What must be validated?", "Intent extras, URI parameters, auth/session state, permissions, exported status, and destination authorization."),
        ("How do you choose background work?", "Use WorkManager for deferrable persistent work, foreground service for user-visible ongoing work, and receivers for short event handling."),
        ("What is the cold-start problem?", "A deep link or notification may enter the app without previous in-memory navigation state, so the destination must rebuild required context."),
        ("What is the security angle?", "Treat external entry points as untrusted input and avoid exposing privileged actions through exported components."),
    ],
    "coroutines": [
        ("Does `suspend` switch threads?", "No. It allows suspension. Dispatcher choice or `withContext` decides where work runs."),
        ("What happens on child failure?", "In a regular scope, failure usually cancels siblings and propagates to the parent. Supervisor boundaries isolate sibling failure."),
        ("Why not swallow cancellation?", "`CancellationException` is the cooperative cancellation signal. Swallowing it can keep cancelled work alive and break structured concurrency."),
        ("What should you avoid?", "Avoid `GlobalScope`, blocking Main, fire-and-forget `async`, and broad catches that hide cancellation or ownership."),
    ],
    "flow": [
        ("Cold or hot?", "Cold Flow starts per collector. StateFlow and SharedFlow are hot and can exist independently of a collector."),
        ("What does operator placement change?", "`flowOn` affects upstream context; `catch` catches upstream failures; downstream collector failures are not caught by an upstream `catch`."),
        ("How do you collect safely in Android?", "Use lifecycle-aware collection such as `repeatOnLifecycle` or Compose lifecycle-aware state collection."),
        ("How do you avoid event replay bugs?", "Model events deliberately, choose replay behavior explicitly, and make one-off navigation/snackbar behavior lifecycle-aware."),
    ],
    "compose": [
        ("What triggers recomposition?", "Reads of snapshot state changing can invalidate composables that read that state."),
        ("What should be hoisted?", "Hoist state to the lowest owner that needs to read or change it; use ViewModel for screen/business state and local state for ephemeral UI."),
        ("Why can mutable lists fail?", "Mutating a normal list in place may not change observable state, so Compose may not know to recompose."),
        ("What do you measure?", "Use recomposition tools, tracing, Macrobenchmark, frame timing, and targeted profiling before optimizing."),
    ],
    "architecture": [
        ("Who owns what?", "UI renders, ViewModel owns screen state, repositories own data policy, data sources own framework/API details, and DI owns construction."),
        ("When is a layer overkill?", "When it only forwards calls without protecting a boundary, rule, test seam, or expected change."),
        ("What makes it testable?", "Dependency inversion, injected dispatchers/services, deterministic state transitions, and boundaries that can be replaced with fakes."),
        ("What trade-off should you name?", "Complexity, team size, feature volatility, release risk, module boundaries, and migration cost."),
    ],
    "patterns": [
        ("How should you present a pattern?", "Name the problem first, then the pattern. Do not recite pattern names without a reason."),
        ("When is Singleton okay?", "For true process-wide stateless or coordinated resources. Avoid it for hidden mutable state and hard-to-replace dependencies."),
        ("How does Kotlin change patterns?", "Sealed classes, higher-order functions, extension functions, and data classes can replace some verbose classic pattern implementations."),
        ("What is pattern abuse?", "Adding indirection that hides simple behavior, ownership, or data flow without reducing real complexity."),
    ],
    "system": [
        ("What is the durable truth?", "Usually Room or another persistent store observed by UI, with repositories/workers reconciling network state into it."),
        ("How do retries stay safe?", "Persist operations with stable IDs, idempotency keys, retry policy, and terminal failure states."),
        ("How do you handle conflicts?", "Choose a product policy: server wins, client wins, last-write-wins, merge, or user resolution."),
        ("What do you monitor?", "Queue age, retry count, conflict rate, auth failures, duplicate attempts, terminal failures, and crash/error spikes."),
    ],
    "testing": [
        ("What must the test control?", "Dispatchers, time, dependencies, lifecycle, data, permissions, network, and external services."),
        ("Why avoid sleeps?", "Sleeps make tests slow and flaky. Virtual time and explicit scheduler advancement make timing deterministic."),
        ("When are fakes better than mocks?", "When behavior and state matter across multiple calls. Mocks are useful for narrow interaction checks."),
        ("Which failure paths should be covered?", "Cover errors, cancellation, retries, empty states, race-prone lifecycle changes, and release-sensitive paths, not only happy cases."),
    ],
    "perfsec": [
        ("What do you measure first?", "Frame timing, main-thread blocking, startup phases, allocations, I/O, lock contention, crash rate, or security boundary depending on the issue."),
        ("What can release builds change?", "R8 can remove or rename code used by reflection/serialization, change stack traces, and expose keep-rule gaps."),
        ("Can secrets be hidden in an APK?", "No. The client is inspectable. Authorization must be enforced server-side and secrets should not rely on obscurity."),
        ("What is the production answer?", "Use staged rollout, monitoring, mapping files, rollback/feature flags, and a small verified fix."),
    ],
    "behavior": [
        ("What should the story prove?", "Judgment, ownership, communication, learning, and impact beyond simply finishing a ticket."),
        ("What trade-off should you name?", "Time, risk, scope, team adoption, migration cost, product impact, or reversibility."),
        ("How do you avoid sounding defensive?", "Describe constraints, decisions, and learning. Avoid blaming personalities or making yourself the only reasonable person."),
        ("How do you show ownership without bragging?", "Name the risk, the people affected, the trade-off you chose, the outcome, and what changed afterward."),
    ],
    "general": [
        ("What is the hidden failure mode?", "Usually ownership, lifecycle, cancellation, invalid state, stale data, test nondeterminism, or production recovery."),
        ("What changes the answer?", "Lifetime, risk, product guarantee, team convention, performance, security, and testability."),
        ("How would you verify it?", "Use the smallest reliable signal: unit test, integration test, profiler, logs, metrics, or rollout monitoring."),
        ("What should you avoid?", "Avoid absolute rules without context. Name the default, the exception, and why the trade-off matters."),
    ],
}


def render_study_block(match: re.Match[str]) -> str:
    number = match.group(1)
    question = match.group(2).strip()
    cat = category(question)
    answer = exact_answer(question) or category_answer(question, cat)
    parts = [
        f"#### Question {number}: {question}",
        "",
        f"**Senior answer:** \"{answer}\"",
        "",
        "**Tricky follow-ups answered:**",
        "",
    ]
    for follow, follow_answer in FOLLOWUPS[cat]:
        parts.append(f"**Follow-up:** {follow}")
        parts.append("")
        parts.append(f"**Answer:** {follow_answer}")
        parts.append("")
    return "\n".join(parts).rstrip() + "\n\n"


def render_mock_block(match: re.Match[str]) -> str:
    heading = match.group(1).rstrip()
    question = re.sub(r"^(?:Prompt:\s*|Follow-up\s+\d+\.\s*|\d+\.\s*)", "", heading).strip()
    cat = category(question)
    answer = exact_answer(question) or category_answer(question, cat)
    parts = [
        f"### {heading}",
        "",
        "**Senior answer**",
        "",
        f"\"{answer}\"",
        "",
        "**Tricky follow-ups answered**",
        "",
    ]
    for follow, follow_answer in FOLLOWUPS[cat]:
        parts.append(f"**Follow-up:** {follow}")
        parts.append("")
        parts.append(f"**Answer:** {follow_answer}")
        parts.append("")
    return "\n".join(parts).rstrip() + "\n\n"


def rewrite_study(text: str) -> str:
    pattern = re.compile(r"^#### Question (\d+): (.*?)\n.*?(?=^#### Question \d+: |^## |\Z)", re.M | re.S)
    return pattern.sub(render_study_block, text)


def rewrite_mocks(text: str) -> str:
    pattern = re.compile(r"^### ((?:Prompt: |Follow-up \d+\. |\d+\. ).*?)\n.*?(?=^### (?:Prompt: |Follow-up \d+\. |\d+\. )|^## |\Z)", re.M | re.S)
    return pattern.sub(render_mock_block, text)


def main() -> None:
    old_guide = GUIDE.read_text()
    old_mocks = MOCKS.read_text()
    new_guide = rewrite_study(old_guide)
    new_mocks = rewrite_mocks(old_mocks)
    GUIDE.write_text(new_guide)
    MOCKS.write_text(new_mocks)
    print(f"rewrote {GUIDE}")
    print(f"rewrote {MOCKS}")


if __name__ == "__main__":
    main()
