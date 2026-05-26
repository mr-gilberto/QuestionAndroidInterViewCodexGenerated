# Answer Quality Audit

> Last audit: 2026-05-25. Scope: `STUDY-GUIDE.md` topic-drill questions, long-form follow-ups, and `MOCK-INTERVIEWS.md` mock questions.

## Quality Gate

The guide is treated as a study guide for the candidate, not as an interviewer rubric. A block only passes when it has:

- a direct senior-level spoken answer under the question,
- enough theory to study from without jumping to another file,
- tricky follow-up questions directly under the topic,
- an answer directly under every follow-up,
- no evaluator-only labels such as `What a senior should show`,
- no cross-topic answers attached to the wrong subject.

## Latest Metrics

| File | Main questions | Main answers | Avg words | Min words | Main answers under 90 | Follow-ups | Follow-up answers | Bad follow-up blocks |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `STUDY-GUIDE.md` | 274 | 274 | 95.7 | 90 | 0 | 1096 | 1096 | 0 |
| `MOCK-INTERVIEWS.md` | 113 | 113 | 95.8 | 90 | 0 | 452 | 452 | 0 |

## Corrections In This Pass

- Regenerated all topic-drill and mock-interview answer blocks from a stricter topic classifier.
- Fixed the previous false match where words such as `sealed` were classified as behavioral because of substring matching.
- Reordered classification so testing questions stay testing questions, local-source-of-truth questions stay mobile system design, and code review conflict stays behavioral.
- Replaced meta follow-ups such as `What makes it senior?` with actual interview-style follow-up questions.
- Verified high-risk samples: data-class `equals`/`hashCode`, mutable `HashMap` keys, sealed classes, null vs empty list, Android leaks, oversized `Bundle`, Flow `catch`, offline conflicts, ViewModel testing, coroutine testing, and code review conflict.

- Added external-alignment expansion chapters for WorkManager/background work, networking/auth, Build/Gradle/CI/CD, accessibility/design systems, and optional KMP.
- Added Round 11 mock interview and question-bank items 229-272.
- Verified the new external-alignment sections do not fall back to generic answer templates.

## Current Result

The primary study files now pass the structural and answer-quality gate: every main question has a direct answer, every tricky follow-up has its own answer, and known evaluator-only phrases are absent from the study-facing documents.
