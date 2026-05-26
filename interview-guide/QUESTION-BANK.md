# Senior Android / Kotlin Question Bank

> Quality status: **Student practice draft**. Target: expand to 250-400 variations. This file is for drilling questions without reading full explanations.

Use this after reading each topic in `STUDY-GUIDE.md`. Try answering out loud first, then check the topic chapter or study guide.

The same questions are now also grouped under each topic in `STUDY-GUIDE.md` as `Topic Drill Questions`, so you can study theory and practice immediately without jumping between files. This file remains the global drill bank for random review.

## Answer Map

Use these sections when you get stuck:

- Questions 1-30: `STUDY-GUIDE.md` Part 1, Kotlin Fundamentals.
- Questions 31-45: `STUDY-GUIDE.md` Part 2, Android Fundamentals.
- Questions 46-67: `STUDY-GUIDE.md` Part 3, Coroutines And Flow.
- Questions 68-82: `STUDY-GUIDE.md` Part 4, Jetpack Compose.
- Questions 83-95: `STUDY-GUIDE.md` Part 5, Architecture.
- Questions 96-105: `STUDY-GUIDE.md` Part 6, Design Patterns.
- Questions 106-118: `STUDY-GUIDE.md` Part 7, Mobile System Design.
- Questions 119-128: `STUDY-GUIDE.md` Part 8, Testing.
- Questions 129-142: `STUDY-GUIDE.md` Part 9, Performance, Security, And Release.
- Questions 143-152: `STUDY-GUIDE.md` Part 10, Soft Skills.
- Questions 153-228: follow-up variations. Use the matching topic part in `STUDY-GUIDE.md`, then deepen with the topic chapter.

Study rule: do not read the answer first. Speak for 60-120 seconds, then check the guide.

## Kotlin Fundamentals

### Data Classes And Equality

1. What is a Kotlin data class?
2. What functions does a data class generate?
3. Which properties are included in generated `equals` and `hashCode`?
4. Are properties declared inside the class body included in `copy()`?
5. What is the difference between `==` and `===`?
6. How does generated `equals` work internally?
7. How many comparisons can `equals` do for a data class with five properties?
8. When is `hashCode` used?
9. Why must `equals` and `hashCode` be consistent?
10. What can go wrong if a mutable data class is used as a `HashMap` key?
11. Is `copy()` deep or shallow?
12. When should you avoid a data class?

### Null Safety

13. Kotlin is null-safe. Can it still throw `NullPointerException`?
14. What is a platform type?
15. When would you use `!!`?
16. What is the difference between `String`, `String?`, and a Java platform type?
17. What is the difference between `lateinit`, `lazy`, and nullable properties?
18. Would you return `null` or an empty list from a repository?
19. How do you model loading, empty, content, and error states?

### Language Features

20. What is a sealed class?
21. Sealed class vs enum?
22. What is an object declaration?
23. Companion object vs object?
24. What are extension functions?
25. Can extension functions override member functions?
26. What are Kotlin scope functions and when can they hurt readability?
27. What does `inline` do?
28. Why does `reified` require `inline`?
29. What is type erasure?
30. Explain `in` and `out` in Kotlin generics.

## Android Fundamentals

31. Walk me through Activity lifecycle.
32. Walk me through Fragment lifecycle.
33. What survives configuration change?
34. What survives process death?
35. Does ViewModel survive process death?
36. What belongs in `SavedStateHandle`?
37. What should go into Room or DataStore instead of saved state?
38. Why should ViewModel not hold an Activity or View reference?
39. Application context vs Activity context?
40. What causes memory leaks in Android?
41. How do you handle runtime permissions?
42. What is an intent?
43. Explicit vs implicit intent?
44. What are deep links and what can go wrong with them?
45. BroadcastReceiver vs Service vs WorkManager?

## Coroutines And Flow

46. What is a coroutine?
47. Are coroutines threads?
48. Does `suspend` mean background thread?
49. What is structured concurrency?
50. `launch` vs `async` vs `withContext`?
51. What does `async` return?
52. What happens if you call `async` and never `await`?
53. What happens when a child coroutine fails?
54. `coroutineScope` vs `supervisorScope`?
55. What is `CancellationException`?
56. Why should you not swallow cancellation?
57. Why is `GlobalScope` discouraged?
58. `Dispatchers.IO` vs `Dispatchers.Default`?
59. What is Flow?
60. Cold Flow vs hot Flow?
61. Flow vs StateFlow vs SharedFlow?
62. How do you model one-off events?
63. What does `flowOn` affect?
64. What does `catch` catch?
65. `collect` vs `collectLatest`?
66. `stateIn` vs `shareIn`?
67. How do you collect Flow safely in Android?

## Jetpack Compose

68. What is recomposition?
69. Does recomposition redraw the whole screen?
70. What triggers recomposition?
71. What is state hoisting?
72. Does all state belong in ViewModel?
73. `remember` vs `rememberSaveable`?
74. What should survive process death in Compose?
75. What is `LaunchedEffect`?
76. When does `LaunchedEffect` restart?
77. What is `DisposableEffect`?
78. What is `rememberUpdatedState` for?
79. Why can mutating a list not update Compose UI?
80. What are lazy list keys?
81. How do you handle navigation events in Compose?
82. How do you investigate Compose performance?

## Architecture

83. Explain MVVM in Android.
84. MVVM vs MVI?
85. What is Clean Architecture?
86. When is Clean Architecture overkill?
87. What is the Repository pattern?
88. What should not go into a Repository?
89. When do you use UseCases?
90. What is unidirectional data flow?
91. What is single source of truth?
92. DTO vs domain model vs UI model?
93. How do you avoid ViewModel becoming too large?
94. How would you migrate a legacy MVP/XML app?
95. How would you modularize a large Android app?

## Design Patterns

96. What design patterns have you used in Android?
97. Singleton: when is it okay and when is it dangerous?
98. Factory vs dependency injection?
99. Adapter pattern examples in Android?
100. Observer pattern in Android?
101. Strategy pattern example in Android?
102. State pattern example in Android?
103. Command pattern for offline operations?
104. How do Kotlin features reduce the need for some classic patterns?
105. What is pattern abuse?

## Mobile System Design

106. Design an offline-first feed.
107. Design an offline notes app.
108. Design a chat feature.
109. Design photo upload with retry.
110. Design background sync.
111. WorkManager vs foreground service?
112. How do you handle offline writes?
113. How do you handle sync conflicts?
114. How do you avoid duplicate writes?
115. How do you handle logout with pending offline work?
116. Design token refresh architecture.
117. Design app startup for a large app.
118. Design feature flags for mobile.

## Testing

119. How do you test a ViewModel with coroutines?
120. How do you test Flow emissions?
121. How do you test StateFlow initial state?
122. How do you avoid real delays in tests?
123. What is dispatcher injection?
124. Fakes vs mocks?
125. How do you test Compose UI?
126. How do you test navigation behavior?
127. How do you test Room migrations?
128. How do you reduce flaky UI tests in CI?

## Performance, Security, Release

129. How do you investigate jank?
130. What causes ANRs?
131. How do you investigate memory leaks?
132. How do you improve startup performance?
133. What tools do you use for performance?
134. How do you store auth tokens?
135. Can secrets be hidden in the APK?
136. Certificate pinning: good idea or risk?
137. How do you secure deep links?
138. What are exported component risks?
139. What can R8 break?
140. How do you test release builds?
141. What are mapping files?
142. How do you handle crash spikes after rollout?

## Soft Skills

143. Tell me about a project you led.
144. Tell me about an architecture disagreement.
145. Tell me about a time you mentored someone.
146. Tell me about a mistake you made.
147. Tell me about a production incident.
148. How do you communicate technical debt to product?
149. How do you handle code review conflict?
150. How do you lead without authority?
151. Tell me about ambiguous requirements.
152. What would your team say is hard about working with you?

## More Follow-Up Variations

153. How would you explain a data class without using the word "boilerplate"?
154. What happens if a data class contains a mutable list?
155. How do data classes interact with DiffUtil or Compose state comparisons?
156. Why can `lateinit` be dangerous?
157. When is `lazy` initialized?
158. How would you model an API result in Kotlin?
159. What is the difference between `Result`, sealed classes, and exceptions?
160. Can a sealed class be extended outside its package/module?
161. What is a value class?
162. When would a value class help in domain modeling?

163. What is the difference between `onCreate`, `onStart`, and `onResume`?
164. Fragment view lifecycle vs Fragment lifecycle?
165. Why should Fragment binding be cleared?
166. What is a PendingIntent?
167. What is task/back-stack behavior for deep links?
168. What can go wrong with saving too much state in a Bundle?
169. How do you handle background location permission?
170. What are exported components?

171. What dispatcher should CPU-heavy work use?
172. What dispatcher should blocking I/O use?
173. What happens if you block `Dispatchers.Main`?
174. How do you run two requests in parallel and combine results?
175. What is `NonCancellable` used for?
176. What is `callbackFlow`?
177. Why is `awaitClose` important?
178. What is `debounce` useful for?
179. `combine` vs `zip`?
180. `flatMapLatest` vs `mapLatest`?

181. What makes a type stable in Compose?
182. What is skippability?
183. What is `derivedStateOf` for?
184. When can `derivedStateOf` be overused?
185. How do LazyColumn keys help?
186. How do you avoid repeated navigation in Compose?
187. How do you test Compose semantics?
188. What is snapshot state?

189. Hilt vs Dagger?
190. Hilt vs Koin?
191. What are Hilt scopes?
192. What should be singleton scoped?
193. Why qualify dispatchers in DI?
194. How do you inject workers?
195. How do you replace dependencies in tests?
196. What is dependency inversion?

197. Design offline-first notes with conflict resolution.
198. Design chat message sending with retry.
199. Design pagination with cache invalidation.
200. Design feature flags for Android.
201. Design app startup initialization.
202. How do you handle user logout in an offline-first app?
203. How do you clean pending work after logout?
204. How do you monitor sync failures?

205. What is `MainDispatcherRule`?
206. `StandardTestDispatcher` vs `UnconfinedTestDispatcher`?
207. What does `advanceUntilIdle()` do?
208. How do you test retry with virtual time?
209. What is Turbine used for?
210. How do you test `stateIn`?
211. How do you test WorkManager?
212. What makes UI tests flaky?

213. What is cold start vs warm start?
214. What are baseline profiles?
215. What is Macrobenchmark for?
216. What does LeakCanary detect?
217. How do you secure WebView bridges?
218. What are deep link security risks?
219. What are R8 keep rules?
220. Why preserve mapping files?

221. Tell me about leading without authority.
222. Tell me about a code review conflict.
223. Tell me about a time you pushed back on product.
224. Tell me about technical debt you paid down.
225. Tell me about a time you were wrong in a technical discussion.
226. Tell me about a time you improved team process.
227. Tell me about a time you handled ambiguity.
228. Tell me about a time you had to make a reversible decision.
