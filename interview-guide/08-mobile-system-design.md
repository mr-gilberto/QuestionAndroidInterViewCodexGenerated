# Mobile System Design

> Quality status: **82/100, Upgrading**. Target: **98+**. Main gap: add full design prompts for chat, feed, upload, offline notes, location, feature flags, startup, and explicit failure-mode analysis.

## Why Interviewers Ask This

Senior Android roles increasingly include mobile system design. Forum reports from Android and big-company interview discussions show that candidates fail when they give backend-only designs or answer like a mid-level feature implementer.

Mobile system design should emphasize:

- Android client architecture,
- source of truth,
- offline behavior,
- process death,
- sync,
- caching,
- WorkManager/background constraints,
- battery and network limits,
- UI state,
- testing,
- rollout and observability.

## Interview Drill Chain: Mobile System Design Structure

### Basic Question

Design an Android app/feature like chat, feed, photo upload, task list, or offline notes.

### Follow-Ups

1. What is the local source of truth?
2. What works offline?
3. How do writes sync?
4. How do you handle conflicts?
5. What survives process death?
6. What background API do you use?
7. How do you handle large data?
8. How do you test it?
9. What trade-off did you choose?

### Strong Answer Framework

"I would start by clarifying which user actions must work offline and what freshness means. Then I would define the local source of truth, usually Room for structured data. The UI observes local data, network refresh writes into local storage, and pending writes are persisted so they survive process death. For deferrable sync I would use WorkManager with constraints and backoff. For immediate user-visible long-running work, I would consider a foreground service. The exact design depends on product requirements like latency, battery, and conflict policy."

### What Your Answer Must Cover

- You guide the design toward mobile constraints.
- You do not wait for interviewer to ask about offline/cache.
- You distinguish reads, writes, sync, and conflict handling.
- You know WorkManager is not a magic immediate executor.
- You test process death and retry behavior.

### Weak Answer To Avoid

"I would call the API, store data in Room, and use WorkManager to refresh cache."

Why this is incomplete:

It may be adequate mid-level, but senior design needs trade-offs: source of truth, invalidation, conflicts, retries, idempotency, and UX.

## Interview Drill Chain: Offline-First

### Basic Question

How would you design offline-first?

### Follow-Ups

1. Do all apps need offline-first?
2. Cached reads vs offline writes?
3. What if a write fails?
4. What if the same item is edited twice offline?
5. How do you avoid duplicate writes?
6. How does logout affect pending work?

### Short Answer

"I do not make every app fully offline-first by default. If losing user input is painful, offline behavior should be planned early. Cached reads are simpler: local DB as source of truth, refresh from network. Offline writes are harder: I need a pending operation queue, idempotent request IDs, retry policy, conflict resolution, and clear UI state."

### Weak Answer To Avoid

"Just cache everything in Room."

Why this is incomplete:

Offline-first is not only storage. The hard part is synchronization and product semantics.

## Interview Drill Chain: WorkManager vs Foreground Service

### Basic Question

When do you use WorkManager vs foreground service?

### Follow-Ups

1. What if work must happen immediately?
2. What if work can be delayed?
3. What if work must survive process death?
4. What if work is continuous location tracking?
5. What about Android 12+ foreground service restrictions?
6. What about battery/data constraints?

### Short Answer

"WorkManager is for deferrable persistent work with constraints and retry. It is good for sync, uploads that can be retried, and work that should survive process death. Foreground service is for immediate user-visible ongoing work like active navigation, recording, calls, or continuous location. Newer Android versions restrict foreground service starts, so the choice must account for policy, timing, user visibility, and Play requirements."

### Weak Answer To Avoid

"Use WorkManager for background tasks and service for long tasks."

Why this is incomplete:

The real distinction is not only duration. It is immediacy, persistence, user visibility, constraints, and OS policy.

## Interview Drill Chain: Token And Networking Architecture

### Basic Question

Where do you handle access/refresh tokens?

### Follow-Ups

1. Should token go to ViewModel?
2. Where do you add auth headers?
3. How do you refresh token?
4. How do you avoid multiple refresh calls?
5. What if refresh fails?
6. What should be stored securely?

### Short Answer

"I do not pass tokens through ViewModels. Auth belongs in the data/network layer. Usually an OkHttp interceptor adds access tokens and an Authenticator or coordinated auth component handles refresh. I serialize refresh so many 401s do not trigger many refresh calls. If refresh fails, I clear auth state and move the app to logged-out state. Storage depends on sensitivity and platform security requirements."

### Weak Answer To Avoid

"Keep the token in ViewModel memory so configuration changes are handled."

Why this is incomplete:

Auth is not screen state and ViewModel does not survive process death.

## Interview Drill Chain: Modularization

### Basic Question

How would you modularize a large Android app?

### Follow-Ups

1. Why modularize?
2. When not to modularize?
3. Feature modules or domain modules?
4. How do you avoid dependency cycles?
5. How does it affect build time?
6. What are convention plugins?

### Short Answer

"I modularize when it helps ownership, dependency boundaries, build parallelism, or feature isolation. I avoid doing it only because it looks clean. Common slices are app, core modules, feature modules, and sometimes shared domain modules. The hidden cost is Gradle configuration time and complexity, so module boundaries need rules and convention plugins to keep build setup maintainable."

### Weak Answer To Avoid

"Every feature should be its own module."

Why this is incomplete:

It ignores team size, build costs, shared dependencies, and complexity.

## Common Mistakes

- Designing only backend APIs.
- Not defining source of truth.
- Treating Room cache as full offline-first.
- Not discussing pending writes or conflicts.
- Using WorkManager for immediate user-visible continuous work.
- Ignoring foreground service restrictions.
- Putting auth tokens in ViewModel.
- Modularizing without dependency rules.
- Ignoring process death.

## Checklist

- Can I guide a mobile design discussion?
- Can I define source of truth?
- Can I distinguish cached reads from offline writes?
- Can I choose WorkManager vs foreground service?
- Can I handle auth refresh architecture?
- Can I explain modularization trade-offs?

## Strong Interview Answer Bank

### Design an offline-first feed.

**Strong Interview Answer**

"I would first clarify what offline-first means for this product. Cached reading is very different from offline writing. For a feed, I would usually make local storage the source of truth. The UI observes paged data from Room, and network refresh writes into Room inside a transaction. That keeps rendering consistent because the UI has one source of truth instead of mixing network responses and local cache manually.

For pagination, I need stable remote keys or cursors so refresh and append do not create duplicates. If the network fails and cached data exists, I would show cached content with a non-blocking error or stale indicator rather than a blank screen.

If users can perform actions offline, such as like or save, I need more than cache. I need a pending operation queue, optimistic UI rules, retry policy, idempotent request IDs, and conflict handling. WorkManager can drain the queue when constraints are met. I would also test process death during sync because mobile apps cannot assume the process stays alive."

### Design a photo upload feature that survives app backgrounding.

**Strong Interview Answer**

"I would separate user-visible selection state from durable upload state. Once the user confirms upload, I persist upload records locally with IDs, file references, status, progress, retry count, and any server correlation ID. The UI observes those records so progress can survive Activity recreation.

For background execution, if the upload is deferrable and should survive process death, WorkManager is a good default because it supports constraints and retry. If the upload must be immediate and user-visible for a long time, I would evaluate foreground service or long-running worker behavior depending on OS policy and product requirements.

The tricky parts are idempotency and cleanup. Retrying a failed upload should not create duplicates on the server, so I want stable upload IDs or server-side idempotency. I also need to handle logout, deleted files, network changes, partial failures, and cancellation. Testing should include poor network, process death, retry, and duplicate prevention."

### WorkManager vs foreground service?

**Strong Interview Answer**

"I choose based on guarantee and user visibility. WorkManager is for persistent, deferrable work that should survive process death and can run with constraints like network or charging. It is good for sync and retryable uploads when immediate execution is not required.

A foreground service is for ongoing work the user is actively aware of and expects to continue immediately, like active navigation, recording, calls, or some long-running transfers. It requires a notification and is subject to newer Android foreground-service restrictions and Play policy.

A coroutine is different: it is in-process work tied to a scope. It is fine for work owned by a ViewModel or repository while the process is alive, but it is not a persistence guarantee. The wrong answer is 'use WorkManager for all background tasks' because some work is immediate, some is persistent, and some is just scoped async work."
