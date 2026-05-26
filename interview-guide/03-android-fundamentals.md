# Android Fundamentals

> Quality status: **Archived modular draft, superseded by `STUDY-GUIDE.md` 100/100**. Last verified: 2026-05-26. The complete student-facing theory, interview answers, and follow-ups now live in `STUDY-GUIDE.md`.

## Lifecycle, ViewModel, SavedStateHandle, and Process Death

### Why Interviewers Ask This

Android lifecycle questions look basic, but senior interviews use them to test whether you understand ownership, state restoration, process death, configuration changes, and what should not be kept in memory only.

Forum discussions repeatedly show confusion around:

- rotation vs process death,
- ViewModel lifetime,
- `savedInstanceState` vs `SavedStateHandle`,
- singletons after process death,
- UI state getting out of sync,
- what can and cannot be serialized.

## Interview Drill Chain: ViewModel Lifetime

### Basic Question

What is ViewModel used for?

### Follow-Ups

1. Does ViewModel survive rotation?
2. Does ViewModel survive process death?
3. What happens when the app is killed in the background?
4. What belongs in `SavedStateHandle`?
5. What belongs in Room/DataStore instead?
6. Why should ViewModel not hold Activity or View references?

### Short Answer

"A ViewModel is a state holder for UI-related data and screen logic. It survives configuration changes while its owner is still in the back stack, but it does not survive process death as an object. For process death, I save only the minimal state needed to restore or reload, usually IDs, filters, selected tab, or small form fields through `SavedStateHandle`. Durable data belongs in Room, DataStore, or another persistent source."

### What Your Answer Must Cover

- ViewModel survives rotation, not process death.
- Process death clears in-memory objects.
- `SavedStateHandle` is for small restoration state.
- Persistent/business data belongs in storage.
- ViewModel should not hold lifecycle/UI references.

### Weak Answer To Avoid

"ViewModel survives lifecycle changes, so it keeps the screen state."

Why this is incomplete:

It is incomplete. It usually hides process death and persistence problems.

## Interview Drill Chain: Process Death

### Basic Question

What is process death in Android?

### Follow-Ups

1. How is it different from rotation?
2. Are singletons preserved?
3. Are repositories preserved?
4. What happens to pending work?
5. How do you restore a screen after process death?
6. How do you test or simulate this?

### Short Answer

"Process death means the OS removed the app process, usually while the app was in the background. Everything in memory is gone: ViewModels, singletons, in-memory repositories, threads, cached values. When the user returns, Android recreates components with saved state where available. I restore from small saved keys plus durable storage, not from memory."

### What Your Answer Must Cover

- All memory state is gone.
- Singletons are not magical persistence.
- `SavedStateHandle`/Bundle handles small state.
- Room/DataStore/files handle durable state.
- WorkManager can own persistent deferrable work.

### Weak Answer To Avoid

"The Activity is recreated and the ViewModel restores it."

Why this is incomplete:

The ViewModel object itself is new after process death.

## Interview Drill Chain: State Placement

### Basic Question

Where do you store screen state?

### Follow-Ups

1. Form input?
2. Selected item ID?
3. Scroll position?
4. Cached API response?
5. Auth token?
6. Pending offline write?

### Short Answer

"I choose storage based on lifetime and importance. Ephemeral UI-only state can stay in Compose with `remember`. State that should survive configuration change belongs in ViewModel. Small restoration keys can go in `SavedStateHandle` or `rememberSaveable`. Durable data, cached responses, auth state, and pending writes belong in persistent storage or the data layer."

## Common Mistakes

- Saying ViewModel survives process death.
- Putting large object graphs into saved state.
- Treating singleton repositories as durable storage.
- Keeping Activity/View references in ViewModel.
- Restoring UI from two competing sources of truth.
- Saving auth tokens or large cached data in ViewModel.

## Checklist

- Can I explain rotation vs process death?
- Can I explain ViewModel lifetime precisely?
- Can I choose between `remember`, `rememberSaveable`, ViewModel, SavedStateHandle, Room, and DataStore?
- Can I explain why singletons are not persistence?
- Can I restore a screen from IDs and durable storage?

## Strong Interview Answer Bank

### What survives rotation, and what survives process death?

**Strong Interview Answer**

"Rotation and process death are different problems. During a configuration change like rotation, the Activity is recreated, but a ViewModel scoped to that screen or navigation entry can survive, so it is a good place for screen state and in-flight screen-owned work.

Process death is different. If the OS kills the app process in the background, all in-memory objects are gone: Activities, Fragments, ViewModels, repositories, singletons, coroutine scopes, and cached fields. When the user returns, Android recreates components, but the old objects are not restored. That is why I do not rely on ViewModel or singleton state for anything that must survive process death.

For restoration, I save small pieces of state such as IDs, selected tab, filters, or simple form fields with `SavedStateHandle`, `rememberSaveable`, or saved instance state. Larger or durable data belongs in Room, DataStore, files, or the backend. The screen should be able to reconstruct itself from saved keys plus durable data."

**What Not To Say**

"ViewModel survives lifecycle, so it survives process death." That is the exact trap.

### Where should screen state live?

**Strong Interview Answer**

"I choose the owner based on lifetime. State that only matters while a small composable is on screen can stay local with `remember`. If it should survive configuration change and represents screen state, I usually put it in the ViewModel. If it should survive process recreation and is small enough to save, I use `SavedStateHandle` or `rememberSaveable`. If it is durable data, cached entities, auth state, or pending offline work, it belongs in the data layer, not in ViewModel memory.

The main rule is to avoid having two competing sources of truth. For example, if Room is the source of truth for a list, the ViewModel should expose state derived from Room rather than maintaining a separate mutable copy that can drift. For forms, I may keep temporary input in ViewModel or saveable state depending on how important it is to restore after process death."

### Why is holding Activity or View reference in ViewModel dangerous?

**Strong Interview Answer**

"A ViewModel can outlive a specific Activity or Fragment instance during configuration change. If it holds a reference to an Activity, Fragment, View, or view binding, it can keep the old UI instance alive after it should be destroyed. That creates memory leaks and can also cause updates to go to the wrong UI object.

If the ViewModel needs context-like functionality, I try to avoid it. If it truly needs application-level context, I use application context carefully, often through injected dependencies. UI work should remain in the UI layer: navigation, showing dialogs, reading resources when tied to configuration, and interacting with views should not be hidden inside the ViewModel."
