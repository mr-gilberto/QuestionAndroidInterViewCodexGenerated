# Senior Android / Kotlin Flashcards

> Quality status: **Student practice draft**. Target: 100+ flashcards.

Use these for fast recall. Answer before expanding the card.

## Kotlin

1. **Q:** `==` vs `===`?  
   **A:** `==` calls `equals` for structural equality. `===` checks reference identity.

2. **Q:** What does data class `copy()` do?  
   **A:** It creates a new outer instance with selected properties changed. It is shallow.

3. **Q:** When is `hashCode` used?  
   **A:** Hash-based collections such as `HashMap`, `HashSet`, and operations like `distinct`.

4. **Q:** What is a platform type?  
   **A:** A Java-interoperability type where Kotlin does not know exact nullability.

5. **Q:** Why can Kotlin still throw NPE?  
   **A:** `!!`, Java interop, platform types, bad initialization, `lateinit`, explicit throws, generic holes.

6. **Q:** Sealed class vs enum?  
   **A:** Enum is fixed constants with same shape. Sealed hierarchy can carry different data per case.

7. **Q:** Why does `reified` require `inline`?  
   **A:** JVM erases generic types; inline lets compiler substitute the actual type at call site.

8. **Q:** `out` in generics?  
   **A:** Covariant producer. Safe to read/produce `T`.

9. **Q:** `in` in generics?  
   **A:** Contravariant consumer. Safe to accept/consume `T`.

10. **Q:** Extension functions dispatch?  
    **A:** They are statically resolved; they do not override class members.

## Android Fundamentals

11. **Q:** Does ViewModel survive rotation?  
    **A:** Yes, while scoped owner remains.

12. **Q:** Does ViewModel survive process death?  
    **A:** No. It is recreated after process death.

13. **Q:** What belongs in `SavedStateHandle`?  
    **A:** Small restoration state: IDs, filters, selected tab, simple form values.

14. **Q:** What belongs in Room/DataStore?  
    **A:** Durable data, cached entities, auth/session data, preferences, pending work metadata.

15. **Q:** Why avoid Activity reference in ViewModel?  
    **A:** ViewModel can outlive Activity instance and leak it.

16. **Q:** Application context vs Activity context?  
    **A:** Application context lives for the process; Activity context is tied to UI lifecycle.

## Coroutines And Flow

17. **Q:** Are coroutines threads?  
    **A:** No. They run on threads but can suspend without blocking them.

18. **Q:** Does `suspend` mean background?  
    **A:** No. It means the function can suspend; dispatcher/implementation determines thread.

19. **Q:** `launch` returns?  
    **A:** `Job`.

20. **Q:** `async` returns?  
    **A:** `Deferred<T>`.

21. **Q:** What happens if `async` fails?  
    **A:** Exception is observed on `await`, while still participating in parent cancellation rules.

22. **Q:** What is structured concurrency?  
    **A:** Coroutines are tied to parent scopes so lifetime, cancellation, and failures are controlled.

23. **Q:** Why avoid swallowing `CancellationException`?  
    **A:** It can break cancellation and keep work running after scope cancellation.

24. **Q:** Flow cold or hot?  
    **A:** Regular Flow is cold by default.

25. **Q:** StateFlow use?  
    **A:** Hot state holder with current value, good for UI state.

26. **Q:** SharedFlow use?  
    **A:** Hot shared stream with replay/buffer config, useful for shared emissions when lifecycle semantics fit.

27. **Q:** `flowOn` affects?  
    **A:** Upstream operators before it.

28. **Q:** `catch` catches?  
    **A:** Upstream exceptions from where it is placed.

## Compose

29. **Q:** What is recomposition?  
    **A:** Re-invoking composables whose observed state may have changed.

30. **Q:** Does recomposition redraw everything?  
    **A:** No. Compose can recompose affected parts and skip unchanged work.

31. **Q:** State hoisting?  
    **A:** Move state to the owner that needs to read/change it.

32. **Q:** Does all state belong in ViewModel?  
    **A:** No. Ownership depends on lifetime and sharing.

33. **Q:** `remember` vs `rememberSaveable`?  
    **A:** `remember` survives recomposition while in composition. `rememberSaveable` can survive config/process recreation for saveable values.

34. **Q:** `LaunchedEffect` key controls?  
    **A:** When the effect cancels and restarts.

35. **Q:** Mutable list not updating UI?  
    **A:** Compose may not observe in-place mutation; use observable state or immutable replacement.

## Architecture

36. **Q:** MVVM core idea?  
    **A:** UI renders state and sends events; ViewModel owns screen state; data/domain layers provide work/data.

37. **Q:** Clean Architecture core idea?  
    **A:** Dependency direction and separation from framework details.

38. **Q:** Repository responsibility?  
    **A:** Data boundary and policy: sources, mapping, caching, sync, errors.

39. **Q:** UseCase when?  
    **A:** When it represents meaningful business operation or orchestration.

40. **Q:** Single source of truth?  
    **A:** One authoritative place for current data/state.

## System Design

41. **Q:** Offline-first hardest part?  
    **A:** Offline writes, sync, conflicts, idempotency, user-visible state.

42. **Q:** WorkManager use?  
    **A:** Deferrable persistent work with constraints/retry.

43. **Q:** Foreground service use?  
    **A:** Immediate ongoing user-visible work.

44. **Q:** Idempotency?  
    **A:** Repeating operation does not create unintended duplicate effects.

45. **Q:** Cached reads vs offline writes?  
    **A:** Cached reads show stored data. Offline writes require persisted pending operations and sync policy.

## Testing

46. **Q:** Why use `runTest`?  
    **A:** Controls coroutine execution and virtual time.

47. **Q:** Why inject dispatchers?  
    **A:** Avoid hardcoded dispatchers and make tests deterministic.

48. **Q:** Fake vs mock?  
    **A:** Fake has behavior; mock verifies interactions.

49. **Q:** StateFlow testing gotcha?  
    **A:** It has an initial value and may never complete.

50. **Q:** Room migration test should verify?  
    **A:** Old data survives and new schema is valid.

## Performance, Security, Release

51. **Q:** ANR cause?  
    **A:** Main thread cannot respond in time, often blocking I/O, long work, locks, binder waits.

52. **Q:** Jank diagnosis starts with?  
    **A:** Measurement/traces, not guessing.

53. **Q:** Can APK secrets be hidden?  
    **A:** Not reliably. Client is not a trusted environment.

54. **Q:** Certificate pinning trade-off?  
    **A:** Reduces some MITM risk but adds rotation/outage risk.

55. **Q:** R8 can break?  
    **A:** Reflection, serialization, DI/framework entry points if keep rules are wrong.

56. **Q:** Mapping files used for?  
    **A:** Deobfuscating release crash reports.

## Soft Skills

57. **Q:** Behavioral answer shape?  
    **A:** Context, constraint, action, trade-off, result, reflection.

58. **Q:** Architecture disagreement should show?  
    **A:** Criteria, trade-offs, low ego, decision path.

59. **Q:** Mistake story should show?  
    **A:** Ownership, correction, prevention, learning.

60. **Q:** Mentorship story should show?  
    **A:** How the other developer became more independent.

61. **Q:** `lateinit` risk?  
    **A:** Access before initialization throws `UninitializedPropertyAccessException`.

62. **Q:** `lazy` initializes when?  
    **A:** On first access, using its configured thread-safety mode.

63. **Q:** Value class use?  
    **A:** Type-safe lightweight wrapper, often for IDs or domain primitives.

64. **Q:** Sealed UI state benefit?  
    **A:** Makes mutually exclusive states explicit and exhaustive.

65. **Q:** Fragment view lifecycle matters because?  
    **A:** Fragment can outlive its View; bindings/collectors tied to View must be cleared/stopped.

66. **Q:** PendingIntent is?  
    **A:** A token allowing another app/system component to perform an action as your app later.

67. **Q:** Exported component risk?  
    **A:** Other apps can invoke it if exported; validate inputs and restrict exposure.

68. **Q:** CPU-heavy dispatcher?  
    **A:** `Dispatchers.Default`.

69. **Q:** Blocking I/O dispatcher?  
    **A:** Usually `Dispatchers.IO`.

70. **Q:** `combine` vs `zip`?  
    **A:** `combine` emits when any source emits after all have values. `zip` pairs emissions.

71. **Q:** `flatMapLatest` behavior?  
    **A:** Cancels previous inner flow when a new upstream value arrives.

72. **Q:** `callbackFlow` needs?  
    **A:** `awaitClose` to unregister callbacks and clean up.

73. **Q:** Compose stability helps?  
    **A:** Compose can skip recomposition when stable inputs are unchanged.

74. **Q:** `derivedStateOf` use?  
    **A:** Cache derived state that changes less often than its inputs.

75. **Q:** Lazy list keys help?  
    **A:** Preserve item identity across moves/updates.

76. **Q:** Hilt scope controls?  
    **A:** Dependency lifetime.

77. **Q:** Singleton scope should avoid?  
    **A:** Activity/View references and screen-specific state.

78. **Q:** Qualify dispatchers why?  
    **A:** Avoid ambiguity and make test replacement easy.

79. **Q:** Dependency inversion?  
    **A:** High-level policy depends on abstractions, not low-level details.

80. **Q:** Offline write requires?  
    **A:** Persisted pending operation, retry policy, idempotency, conflict handling.

81. **Q:** Token refresh concurrency issue?  
    **A:** Many 401s can trigger many refresh calls unless refresh is serialized/shared.

82. **Q:** Logout with pending work?  
    **A:** Cancel, clear, or re-scope work based on product/security rules.

83. **Q:** `MainDispatcherRule` purpose?  
    **A:** Replace Main dispatcher in coroutine tests.

84. **Q:** `advanceUntilIdle()`?  
    **A:** Runs scheduled coroutine work until no tasks remain.

85. **Q:** Turbine is for?  
    **A:** Testing Flow emissions.

86. **Q:** UI test flakiness often comes from?  
    **A:** Timing, async work, animations, network/data dependencies, weak synchronization.

87. **Q:** Cold start?  
    **A:** App process is not running and must be created.

88. **Q:** Baseline profiles?  
    **A:** Precompile critical paths to improve startup/runtime performance.

89. **Q:** Macrobenchmark?  
    **A:** Measures app-level performance such as startup and scrolling.

90. **Q:** LeakCanary detects?  
    **A:** Retained objects that should have been garbage collected.

91. **Q:** WebView bridge risk?  
    **A:** JavaScript bridge can expose native functionality to untrusted content.

92. **Q:** Deep link security rule?  
    **A:** Treat link parameters as untrusted input.

93. **Q:** R8 keep rule purpose?  
    **A:** Prevent shrinking/obfuscation from breaking reflection/framework-used code.

94. **Q:** Mapping files?  
    **A:** Map obfuscated release stack traces back to original symbols.

95. **Q:** Strong conflict story shows?  
    **A:** Decision criteria, listening, trade-offs, and outcome.

96. **Q:** Strong mistake story shows?  
    **A:** Ownership, fix, prevention, learning.

97. **Q:** Technical debt pitch should mention?  
    **A:** Delivery risk, regressions, cost, and options.

98. **Q:** Leadership without authority shows?  
    **A:** Influence through clarity, trust, alignment, and follow-through.

99. **Q:** Ambiguity answer should start with?  
    **A:** Clarifying requirements, constraints, and assumptions.

100. **Q:** Senior answer should always include?  
    **A:** Ownership, trade-offs, and practical consequences.
