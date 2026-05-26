# Jetpack Compose

> Quality status: **78/100, Draft**. Target: **98+**. Main gap: add stability/skippability, snapshot state, side-effect APIs, navigation/lifecycle, lazy list keys, performance, and Compose testing.

## Why Interviewers Ask This

Compose questions often start with simple terms like recomposition and state hoisting, then move into lifecycle, navigation, `rememberSaveable`, `LaunchedEffect`, mutable state, performance, and whether the candidate understands declarative UI rather than just syntax.

Forum signals show common interview gotchas:

- recomposition misunderstood,
- state hoisting misunderstood,
- mutable objects not triggering UI updates,
- `LaunchedEffect` key mistakes,
- Compose navigation/lifecycle questions,
- `remember` vs `rememberSaveable`,
- performance and unnecessary recomposition.

## Interview Drill Chain: Recomposition

### Basic Question

What is recomposition?

### Follow-Ups

1. What triggers recomposition?
2. Does recomposition redraw the whole screen?
3. Can recomposition be skipped?
4. Can recomposition be cancelled?
5. Why should composables be side-effect free?
6. Why did mutating a list not update the UI?

### Short Answer

"Recomposition is Compose re-invoking composable functions that read changed state so it can update the UI description. It does not mean the whole screen is redrawn. Compose can skip work when inputs are stable and unchanged, and recomposition can be cancelled. I avoid relying on exact recomposition timing for correctness, and I keep side effects in effect APIs."

### What Your Answer Must Cover

- Recomposition is function re-execution, not full redraw.
- State reads define invalidation scope.
- Mutating non-observable state may not trigger recomposition.
- Composables should be side-effect free.
- Performance must be measured.

### Weak Answer To Avoid

"Whenever state changes, Compose redraws everything."

Why this is incomplete:

It misses skipping, scope, and declarative rendering mechanics.

## Interview Drill Chain: State Hoisting

### Basic Question

What is state hoisting?

### Follow-Ups

1. Does all state go to ViewModel?
2. What is the lowest common owner?
3. What state can stay local?
4. How does this help previews/tests?
5. How do events flow back up?

### Short Answer

"State hoisting means moving state to the owner that needs to read or modify it. That is not always the ViewModel. Screen state often belongs in ViewModel, but local UI state can stay in Compose. The pattern is state down, events up: the composable receives values and callbacks, which makes it easier to preview, test, and reuse."

### Weak Answer To Avoid

"State hoisting means putting state in the ViewModel."

Why this is incomplete:

It ignores local state and ownership.

## Interview Drill Chain: `remember`, `rememberSaveable`, and ViewModel

### Basic Question

What is the difference between `remember` and `rememberSaveable`?

### Follow-Ups

1. What survives recomposition?
2. What survives configuration change?
3. What survives process death?
4. When do you use ViewModel instead?
5. What cannot be saved?

### Short Answer

"`remember` keeps a value while the composable remains in composition. `rememberSaveable` uses saveable state so it can survive configuration change and process recreation for supported values. ViewModel is better for screen state, business interaction, and data loading. Durable state still belongs below the UI layer."

## Interview Drill Chain: `LaunchedEffect`

### Basic Question

What is `LaunchedEffect`?

### Follow-Ups

1. When does it run?
2. When does it restart?
3. What do keys mean?
4. What happens if the key changes too often?
5. What if the lambda captures stale values?
6. When use `rememberUpdatedState`?

### Short Answer

"`LaunchedEffect` runs a coroutine tied to the composition. Its keys define when the effect is cancelled and restarted. If I key it incorrectly, I can accidentally restart work too often or keep stale values. If I need the latest callback inside a long-running effect without restarting it, `rememberUpdatedState` can help."

### Weak Answer To Avoid

"I use `LaunchedEffect(Unit)` whenever I need to call something from a composable."

Why this is incomplete:

It can hide lifecycle, key, and stale-capture bugs.

## Common Mistakes

- Putting business logic in composables.
- Treating recomposition as full redraw.
- Mutating regular lists and expecting UI updates.
- Using `remember` for state that must survive process recreation.
- Using `LaunchedEffect` without understanding keys.
- Passing ViewModel deep into every child composable.
- Optimizing recomposition before measuring.

## Checklist

- Can I explain recomposition and skipping?
- Can I explain state hoisting by ownership?
- Can I choose `remember`, `rememberSaveable`, or ViewModel?
- Can I explain `LaunchedEffect` keys?
- Can I explain mutable state pitfalls?
- Can I discuss Compose performance without hand-waving?

## Strong Interview Answer Bank

### What is recomposition?

**Strong Interview Answer**

"Recomposition is Compose re-invoking composable functions whose observed state may have changed, so it can produce an updated UI description. It is not the same as redrawing the whole screen. Compose tracks state reads and can recompose only affected parts of the tree. It can also skip recomposition when inputs are stable and unchanged.

The important practical rule is that composables should be safe to call many times. I should not put uncontrolled side effects, network calls, database writes, or navigation directly in the body of a composable. Those belong in ViewModel logic or in Compose effect APIs like `LaunchedEffect` or `DisposableEffect` with the correct keys.

If a UI does not update after I change something, I check whether the value is actually observable Compose state. Mutating a regular mutable list in place may not trigger recomposition because Compose may not see a new state value. I usually prefer immutable state updates or snapshot-aware state containers."

### What is state hoisting?

**Strong Interview Answer**

"State hoisting means moving state to the owner that needs to read or modify it. It does not automatically mean putting every variable in the ViewModel. The right owner depends on lifetime and sharing.

For example, a text field's temporary UI value may live locally if only that composable cares. If validation, submit behavior, loading, or error rendering depends on it, it may belong in the ViewModel as part of screen state. The composable then receives state and callbacks: state flows down, events flow up.

The benefit is that composables become easier to preview, test, and reuse because they are not secretly owning business logic. The trade-off is that over-hoisting trivial state can make simple UI feel noisy, so I choose the lowest common owner rather than blindly moving everything upward."

### How do `remember`, `rememberSaveable`, and ViewModel differ?

**Strong Interview Answer**

"`remember` stores a value across recompositions while that composable remains in the composition. It is good for local UI state that does not need to survive the composable leaving the tree.

`rememberSaveable` also saves through configuration changes and process recreation when the value can be stored in saved state. It is useful for small UI values like text input or selected tab, but it is not meant for large object graphs or durable app data.

ViewModel is a screen state holder. It survives configuration changes and coordinates business interactions, loading, validation, and repository calls. It does not survive process death as the same object, so important restoration still needs saved keys or persistent storage. In practice, I choose based on ownership and lifetime, not by habit."
