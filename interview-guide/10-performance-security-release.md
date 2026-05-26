# Performance, Security, And Release Engineering

> Quality status: **72/100, Draft**. Target: **97+**. Main gap: split into deeper performance, security, and release sections with tools, edge cases, official docs, and interview failure patterns.

## Performance Drill Chain

### Basic Question

How do you investigate poor performance or jank?

### Follow-Ups

1. Is the main thread blocked?
2. Is it layout/recomposition?
3. Is it I/O or database?
4. Is it image loading?
5. Is it memory pressure or GC?
6. How do you measure?
7. What production signal would you check?

### Short Answer

"I start by measuring. For jank or freezes, I look at main-thread work, traces, layout or recomposition cost, disk I/O, database queries, image loading, and allocation pressure. For memory, I look for retained Activity/View references and use profiler or LeakCanary. I try to connect local traces with production data like crash reports, ANRs, vitals, or performance metrics."

### Weak Answer To Avoid

"I would move work to a background thread."

Why this is incomplete:

It may be part of the fix, but senior diagnosis starts with evidence and the exact bottleneck.

## Security Drill Chain

### Basic Question

How do you store tokens and secure network communication?

### Follow-Ups

1. Can secrets be hidden in the APK?
2. Should token be in ViewModel?
3. What about encrypted storage?
4. Certificate pinning: always good?
5. What is the operational risk?
6. What should the server enforce?
7. How do you avoid logging sensitive data?

### Short Answer

"I assume anything shipped in the APK can be inspected, so mobile API keys are not true secrets. Tokens belong in the auth/data layer, stored according to sensitivity and platform guidance. Server-side authorization is still the real trust boundary. For certificate pinning, I treat it as a trade-off: it can reduce certain MITM risks, but it creates rotation and outage risk if not managed carefully."

### Weak Answer To Avoid

"We encrypt the token and pin the certificate, so it is secure."

Why this is incomplete:

It ignores client trust boundaries, operations, server authorization, and rotation.

## Release Engineering Drill Chain

### Basic Question

What do you watch for in release builds?

### Follow-Ups

1. What can R8 break?
2. How do you test minified builds?
3. What are keep rules?
4. How do you monitor rollout?
5. How do you handle crash spikes?
6. How do you rollback or hotfix?

### Short Answer

"Release builds can behave differently because of minification, resource shrinking, build variants, signing, and feature flags. R8 can break reflection-heavy code if keep rules are wrong. I test critical flows in release-like builds, roll out gradually when possible, monitor crashes/ANRs, and have a rollback or hotfix path."

### Weak Answer To Avoid

"If debug works, release should work."

Why this is incomplete:

Senior Android candidates are expected to know release builds are different.

## Common Mistakes

- Optimizing without profiling.
- Blaming Compose or coroutines generically.
- Treating client secrets as real secrets.
- Adding certificate pinning without rotation strategy.
- Logging tokens or PII.
- Testing only debug builds.
- Adding broad keep rules that remove R8 value.
- Ignoring staged rollout signals.

## Checklist

- Can I explain performance diagnosis with tools?
- Can I explain ANRs and memory leaks?
- Can I discuss token storage and trust boundaries?
- Can I discuss certificate pinning trade-offs?
- Can I explain R8 and release-build risk?
- Can I explain rollout monitoring?

## Strong Interview Answer Bank

### How do you investigate app jank or freezes?

**Strong Interview Answer**

"I start by measuring instead of guessing. If users report jank or freezes, I want to know whether the main thread is blocked, whether frames are missed during rendering, whether we are doing disk or database work on the main thread, whether image loading is too heavy, or whether allocation pressure is causing frequent GC.

Locally I would use Android Studio profiler, traces, and depending on the case Perfetto or Macrobenchmark. In production I would look at Android Vitals, ANRs, crash reports, device distribution, and any performance metrics we have. A bug that does not reproduce on a high-end dev device can still be severe on real user devices.

I also avoid vague fixes like 'move it to background' without knowing the bottleneck. If the issue is too much recomposition, the fix differs from a slow SQL query, a large bitmap, startup initialization, or lock contention. Senior performance work is evidence-driven."

### How do you detect and fix memory leaks?

**Strong Interview Answer**

"In Android, many leaks come from lifetime mismatches. A long-lived object holds a reference to a short-lived Activity, Fragment, View, binding, adapter, callback, or coroutine collector. After configuration change, the old UI instance should be collectible, but the reference keeps it alive.

I would reproduce the flow, rotate or navigate away, then inspect retained objects with the memory profiler or LeakCanary if the project uses it. I look for references from singletons, static fields, callbacks, coroutines, observers, or adapters. The fix is usually to move ownership to the right lifecycle, clear references, use application context where appropriate, or avoid storing UI references in ViewModel or singleton objects.

The key is not just 'use weak references'. Most leaks are design ownership bugs. Weak references can hide the symptom without fixing the lifetime model."

### How do you think about token storage and mobile security?

**Strong Interview Answer**

"I assume the mobile client is not a fully trusted environment. Anything shipped in the APK can be inspected eventually, so API keys in the app are not true secrets. The server must enforce authorization; the client can improve security posture but should not be the trust boundary.

For tokens, I keep them out of ViewModels and UI state. Auth belongs in the data/auth layer. Storage depends on sensitivity and product requirements, but I would use platform-supported secure storage patterns where appropriate and avoid logging tokens or PII. I also keep token lifetime and scope limited where possible.

Certificate pinning is a trade-off. It can reduce some MITM risk, but it adds operational risk if certificates rotate or pinning is misconfigured. I would only use it with a clear threat model, backup pins or a rotation plan, and monitoring."

### What can go wrong in release builds?

**Strong Interview Answer**

"Release builds can behave differently from debug builds. R8 can shrink, optimize, and obfuscate code. That is useful for size and performance, but it can break code that depends on reflection, serialization, dependency injection, or framework entry points if keep rules are wrong.

I want critical flows tested in a release-like build, not only debug. That includes minification, resource shrinking, signing configuration, build variants, feature flags, and backend environments. I also want mapping files preserved so obfuscated crash reports can be understood.

For rollout, I prefer staged release when possible. If there is a crash spike or ANR regression, I want the team to stop rollout, identify the release diff, hotfix or rollback if available, and then add a prevention test or release checklist item. The senior answer is not just knowing R8 exists; it is treating release as an engineering system."
