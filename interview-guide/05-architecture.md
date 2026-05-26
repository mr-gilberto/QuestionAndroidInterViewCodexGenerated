# Architecture

> Quality status: **Archived modular draft, superseded by `STUDY-GUIDE.md` 100/100**. Last verified: 2026-05-26. The complete student-facing theory, interview answers, and follow-ups now live in `STUDY-GUIDE.md`.

## Why Interviewers Ask This

Senior Android interviews usually move from Kotlin and Android fundamentals into architecture because architecture reveals judgment. Interviewers want to know whether you can structure a feature, reason about ownership, avoid lifecycle leaks, test the design, and explain trade-offs without hiding behind buzzwords.

Public reports repeatedly mention MVVM, MVI, Clean Architecture, Repository, Hilt/DI, modularization, scalable app design, and system architecture whiteboarding.

## Core Theory

Architecture is the assignment of responsibilities and dependencies. In Android, the recurring problem is not only "where do files go?" but:

- who owns UI state,
- who owns business rules,
- who owns data synchronization,
- who survives lifecycle changes,
- who can depend on Android framework types,
- how easy it is to test a piece in isolation,
- how safely the app can evolve.

Modern Android architecture usually separates:

- **UI layer**: Compose screens or Views render state and send user events.
- **State holder layer**: ViewModel prepares UI state and coordinates user actions.
- **Domain layer**: use cases or domain services, when business logic is complex enough to justify them.
- **Data layer**: repositories, data sources, network APIs, database, cache, sync logic.
- **Infrastructure layer**: DI, logging, analytics, config, build/release wiring.

The key is dependency direction. UI depends on state holders. State holders depend on domain/data abstractions. Domain should not depend on Android UI classes. Data layer can know about Retrofit, Room, DataStore, and platform APIs when appropriate.

## What You Must Be Able To Explain

- MVVM as presentation architecture.
- MVI as stricter unidirectional state/event architecture.
- Clean Architecture as dependency-boundary discipline, not folder naming.
- Repository as a data boundary and source-of-truth coordinator.
- Use cases as meaningful business operations, not mandatory pass-through classes.
- UDF: state flows down, events flow up.
- Single source of truth.
- DI as ownership/composition, not just "for testing."
- Modularization by feature/core/domain boundaries.
- How to migrate legacy architecture incrementally.

## Research-Backed Interview Questions

- Explain MVVM in Android.
- What is the difference between MVVM and MVI?
- What is Clean Architecture?
- Is Clean Architecture overkill?
- What is the role of a Repository?
- Where should business logic live?
- When do you use UseCases?
- How do you communicate from ViewModel back to UI?
- How would you design a scalable Android app?
- How would you migrate a Java/MVP/XML app to Kotlin/Compose/Clean Architecture?
- How do you structure modules in a large Android codebase?
- Should every repository have an interface?
- How do you avoid ViewModel becoming too large?

## Question Variations

- "Which architecture do you normally use in Android projects and why?"
- "What is your thought process when creating an app using MVVM?"
- "Would you use MVI for every screen?"
- "Where do you put validation logic?"
- "What belongs in ViewModel vs UseCase vs Repository?"
- "How do you handle one-off events?"
- "How would you organize a feature module?"
- "How would you handle shared data across features?"

## Natural Interview Answers

### Explain MVVM in Android

"In Android, I use MVVM mainly as a presentation-layer pattern. The UI renders state and forwards user actions. The ViewModel owns screen state, starts work in a lifecycle-aware way, and coordinates with repositories or use cases. The value is that the UI stays mostly declarative and the state preparation is testable outside the screen."

### MVVM vs MVI

"MVVM is broader. A ViewModel exposes state and handles actions, but the exact event/state model can vary. MVI is stricter: events go in, a reducer or state machine updates immutable state, and the UI renders that state. I like MVI for complex screens where predictability matters, but I do not force it onto simple screens if it adds ceremony without value."

### Clean Architecture

"Clean Architecture is about dependency boundaries. The domain should not know about Retrofit, Room, Activity, or Compose. The data layer can implement the details, and the UI layer can adapt state for rendering. I use it when the project has enough complexity that boundaries pay for themselves. If the app is small, a lighter layered architecture can be more honest."

### Repository

"A repository gives the rest of the app a clean data API. It can coordinate remote and local data, caching, mapping, synchronization, and error policy. In an offline-first feature, I often make Room the source of truth: network refresh writes to Room, and UI observes Room through Flow."

### Use Cases

"I use use cases when they represent a real operation or business rule: combining repositories, validating permissions, orchestrating sync, or making a decision that multiple screens share. I avoid creating a use case that only calls one repository method unless the team convention is strong and the consistency is worth it."

## Deep Follow-Ups

### Should every repository have an interface?

"Not automatically. Interfaces are useful when I need multiple implementations, test replacement, module boundary inversion, or API stability. If there is only one implementation and tests can use fakes at a higher boundary, an interface may be ceremony. In larger modular apps, interfaces can help enforce dependency direction."

### Is ViewModel part of the domain layer?

"No, I treat ViewModel as presentation/state-holder layer. It can call domain use cases or repositories, but it prepares UI state and understands screen behavior. Domain logic should be usable without Android lifecycle classes."

### Where should validation live?

"It depends on the validation. UI formatting validation can live near the UI or ViewModel. Business validation belongs in domain/use case. Server-authoritative validation still needs backend enforcement, with client-side validation for UX."

### How do you prevent ViewModel bloat?

"I watch for unrelated responsibilities. If the ViewModel is doing network mapping, business decisions, analytics policy, sync orchestration, and UI state, I split responsibilities. Sometimes a use case helps; sometimes a mapper or coordinator is enough."

### How would you migrate legacy architecture?

"I would not stop releases for a full rewrite. I would create a target architecture, add boundaries around new or changed features, introduce Kotlin and DI incrementally, and migrate high-change areas first. I would measure build time, test coverage, crash risk, and team velocity rather than migrating for aesthetics."

## Common Mistakes

- Treating MVVM, MVI, and Clean Architecture as competing names for the same thing.
- Saying Clean Architecture means "ViewModel, UseCase, Repository folders."
- Creating pass-through UseCases everywhere.
- Returning network DTOs directly to UI because it is faster today.
- Letting ViewModel depend on Activity, Fragment, View, or NavController by default.
- Making repositories responsible for UI state.
- Over-modularizing without dependency rules.
- Under-modularizing so every feature can import everything.

## Project Experience Angle

Mention project experience when the question is about trade-offs:

- "In a previous app, we used Room as source of truth because network was unreliable."
- "We avoided full Clean Architecture for simple CRUD screens, but used use cases for payment flow because rules were shared and test-heavy."
- "We migrated feature-by-feature from MVP to MVVM because a rewrite would have blocked weekly releases."

Keep it short. The project story should prove judgment, not become a monologue.

## Checklist

- Can I explain MVVM without reciting only the acronym?
- Can I explain when MVI helps and when it is too much?
- Can I describe Clean Architecture by dependency direction?
- Can I justify Repository and UseCase decisions?
- Can I design source-of-truth data flow?
- Can I explain modularization trade-offs?
- Can I describe a migration plan for legacy Android?

## Strong Interview Answer Bank

### Explain MVVM in Android.

**Strong Interview Answer**

"In Android, I think of MVVM as a presentation architecture, not just three folders. The UI layer, whether it is Compose or XML, renders state and sends user actions. The ViewModel owns the screen state, coordinates user events, and calls into use cases or repositories. The data layer handles where data comes from and how it is cached or synchronized.

The benefit is ownership. The UI does not need to know how data is loaded, and the ViewModel does not need to know how the UI is drawn. That makes the screen easier to test because I can drive the ViewModel with events and assert state without launching the whole UI.

The trap is putting everything in the ViewModel. If the ViewModel is doing API mapping, database policy, business validation, analytics rules, and navigation all together, it becomes a god object. For simple screens, MVVM can stay lightweight. For complex flows, I may introduce use cases, reducers, mappers, or coordinators based on the actual pressure."

### What is Clean Architecture, and when is it overkill?

**Strong Interview Answer**

"Clean Architecture is mainly about dependency direction and separation of responsibilities. The domain or business rules should not depend on Android UI classes, Retrofit DTOs, Room entities, or Compose. The outer layers can know about frameworks, but the core rules should remain testable and independent.

In Android, that often becomes UI, ViewModel, domain/use cases, repositories, and data sources. But the folders are not the architecture. The important question is whether the boundaries reduce coupling and make change safer.

It becomes overkill when the app or feature is simple and the layers are just pass-through wrappers. A `GetUserUseCase` that only calls `userRepository.getUser()` may not add value unless the team needs strict consistency. I prefer to add structure where it solves a real problem: shared business logic, complex orchestration, testability, multiple data sources, or team/module boundaries."

### What is the Repository pattern in Android?

**Strong Interview Answer**

"A repository is a boundary around a data area. It gives the rest of the app a clean API and hides whether the data comes from network, Room, DataStore, cache, or a combination. In a senior Android design, I expect the repository to own data policy: source of truth, refresh strategy, mapping, error classification, and sometimes sync coordination.

For offline-first features, I often make local storage the source of truth. The UI observes Room through Flow, a refresh fetches from the network, and the repository writes the result into the database. That way the UI is not split between network state and local state.

The repository should not become a dumping ground. UI decisions do not belong there, and not every business rule belongs there. If the rule is reusable or combines multiple repositories, a use case or domain service may be clearer."
