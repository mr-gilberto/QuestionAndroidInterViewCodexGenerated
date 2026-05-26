# Testing

> Quality status: **Archived modular draft, superseded by `STUDY-GUIDE.md` 100/100**. Last verified: 2026-05-26. The complete student-facing theory, interview answers, and follow-ups now live in `STUDY-GUIDE.md`.

## Why Interviewers Ask This

Senior Android interviews use testing questions to evaluate engineering maturity. It is not enough to say "I write unit tests." Interviewers usually probe whether you can test asynchronous state, Flow emissions, Compose UI, database migrations, and architecture boundaries without creating brittle tests.

## Interview Drill Chain: ViewModel And Coroutine Tests

### Basic Question

How do you test a ViewModel that uses coroutines?

### Follow-Ups

1. How do you avoid real delays?
2. How do you control dispatchers?
3. How do you test loading then success?
4. How do you test errors?
5. How do you avoid testing private methods?
6. What if the Flow never completes?

### Short Answer

"I test the ViewModel through public events and observed state. For coroutines I use `runTest` and inject dispatchers so the test controls execution and virtual time. I collect state emissions, trigger the action, advance the scheduler if needed, and assert meaningful states like initial, loading, success, or error. I avoid testing private methods directly because that couples the test to implementation."

### What Your Answer Must Cover

- `runTest` and virtual time.
- Dispatcher injection.
- Public behavior over private implementation.
- State emission assertions.
- Proper cancellation of never-ending collections.

### Weak Answer To Avoid

"I use `Thread.sleep` and then check the value."

Why this is incomplete:

It creates flaky and slow tests.

## Interview Drill Chain: Flow Testing

### Basic Question

How do you test Flow?

### Follow-Ups

1. Cold or hot flow?
2. How do you assert multiple emissions?
3. How do you cancel collection?
4. How do you test StateFlow initial value?
5. How do you test `catch` or retry?
6. What if two flows are combined?

### Short Answer

"I test Flow by collecting it in a controlled test scope and asserting emissions. For StateFlow, I remember there is an initial value. For flows that do not complete, I cancel collection deliberately. I also test error and retry behavior by using fakes that emit success, failure, or delayed values."

### Weak Answer To Avoid

"I call `.first()` on the Flow."

Why this is incomplete:

Sometimes `first()` is enough, but it misses multi-emission state flows, loading states, and ongoing streams.

## Interview Drill Chain: Fakes vs Mocks

### Basic Question

Mocks or fakes?

### Follow-Ups

1. When is a fake better?
2. When is a mock fine?
3. How do mocks make tests brittle?
4. How do you fake a repository?
5. How do you test error behavior?

### Short Answer

"I prefer fakes when the collaborator has meaningful behavior, especially repositories or data sources. A fake can return state, emit flows, and simulate errors without tying the test to exact method-call order. Mocks are useful for narrow boundaries or verifying a specific interaction, but overusing them often tests implementation rather than behavior."

## Interview Drill Chain: Compose UI Tests

### Basic Question

How do you test Compose UI?

### Follow-Ups

1. What do you assert?
2. Do you test implementation details?
3. How do semantics help?
4. How do you test navigation?
5. How many UI tests are worth it?

### Short Answer

"I test Compose UI through visible behavior and semantics. I prefer asserting that the user can see text, click controls, and observe expected state changes rather than testing composable internals. For navigation, I usually test that the expected event or route is triggered, depending on how navigation is wired. I keep UI tests focused because they are more expensive than unit tests."

## Interview Drill Chain: Room Migrations

### Basic Question

How do you test database migrations?

### Follow-Ups

1. Why not use destructive migration?
2. How do you test old schemas?
3. What data should be in the migration test?
4. How do you handle large migrations?
5. What happens if migration fails in production?

### Short Answer

"I test Room migrations with representative old schemas and data. The test should verify that old data survives and the new schema is valid. I avoid destructive migration unless data loss is acceptable. For large changes, I try to break migration into safer steps and treat it as a release risk."

## Common Mistakes

- Using real delays.
- Hardcoding dispatchers.
- Testing private methods.
- Using mocks for everything.
- Only testing the final success state.
- Not testing errors or cancellation.
- Forgetting initial StateFlow emissions.
- Leaving never-ending Flow collections active.
- Having many brittle UI tests with low value.
- Not testing Room migrations.

## Checklist

- Can I explain `runTest`?
- Can I inject dispatchers?
- Can I test loading/success/error state?
- Can I test Flow emissions and cancellation?
- Can I explain fakes vs mocks?
- Can I test Compose behavior through semantics?
- Can I test Room migrations?

## Strong Interview Answer Bank

### How do you test a ViewModel that uses coroutines and Flow?

**Strong Interview Answer**

"I test the ViewModel through public behavior, not private methods. I create the ViewModel with fake dependencies, trigger public events, and assert the emitted UI state. For coroutine code, I use `runTest` so the test controls virtual time instead of sleeping. I also inject dispatchers or a dispatcher provider, because hardcoded `Dispatchers.Main` or `Dispatchers.IO` makes tests harder to control.

For state, I usually assert the sequence: initial state, loading, success or error. If the ViewModel exposes `StateFlow`, I remember it has an initial value. If the Flow never completes, I collect it in a test coroutine and cancel it deliberately. For repository behavior, I prefer fakes that can emit loading, success, error, or delayed responses.

The main thing I want from these tests is confidence in behavior: when the user taps retry, when a network call fails, when validation fails, or when cached data arrives before fresh data. I do not want tests that only verify implementation details like 'method X was called once' unless that interaction is the actual behavior."

**What Not To Say**

"I use `Thread.sleep` and then check the value." That is a flakiness smell.

### How do you test Flow emissions?

**Strong Interview Answer**

"I first identify what kind of Flow I am testing. A cold Flow that emits once can sometimes be tested with `first()`, but that is not enough for UI state flows where the sequence matters. For multi-emission flows, I collect in a controlled coroutine test scope and assert emissions in order: initial, loading, content, error, and so on.

For StateFlow, the initial value is part of the contract, so I account for it. For combined flows, I set up fake upstreams and drive them intentionally so I know which emission should happen. If the Flow is infinite or hot, I make sure the collection is cancelled at the end of the test.

The failure I try to avoid is testing only the final value. A bug can be in the transition: loading never appears, error overwrites cached data, retry duplicates emissions, or cancellation leaves a collector running."

### Fakes or mocks?

**Strong Interview Answer**

"I use both, but for different reasons. I prefer fakes when the dependency has meaningful behavior. For example, a fake repository can expose a Flow, emit cached data, then emit refreshed data, or throw a controlled error. That makes the test closer to real behavior and less tied to implementation.

Mocks are useful for narrow boundaries, especially when I need to verify a specific interaction with an external collaborator. But if every test is a list of mocked method calls, I am probably testing implementation details. Those tests break easily when I refactor without changing behavior.

For senior Android code, I want tests that survive refactoring. If the ViewModel still emits the right UI state after a user action, I usually do not care whether the internal method name changed."

### How do you test Room migrations?

**Strong Interview Answer**

"I treat Room migrations as release-risk tests, not just database code. A migration test should create a database using an old schema, insert representative old data, run the migration, validate the new schema, and verify the data still means what it should mean.

I avoid destructive migration unless data loss is explicitly acceptable. That might be okay for a disposable cache, but not for user-created data or pending offline work. For complex migrations, I prefer smaller incremental steps and tests for important historical versions.

The interview-level point is that persistence bugs are not like UI bugs. If a migration corrupts data in production, a rollback may not restore the old local database. So migrations deserve specific tests and release attention."
