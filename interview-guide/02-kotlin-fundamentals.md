# Kotlin Fundamentals

> Quality status: **Archived modular draft, superseded by `STUDY-GUIDE.md` 100/100**. Last verified: 2026-05-26. The complete student-facing theory, interview answers, and follow-ups now live in `STUDY-GUIDE.md`.

## Data Classes, Equality, and Hashing

### Why Interviewers Ask This

This starts as a basic Kotlin question, but it often turns into a deeper check of whether you understand generated code, equality contracts, collections, and performance.

A common interview chain looks like this:

1. What is a data class?
2. What methods does it generate?
3. How does equality work?
4. Does `==` call `equals`?
5. How many comparisons does generated `equals` do?
6. When is `hashCode` used?
7. What happens in a `HashMap` or `HashSet`?
8. What happens if a property is a list or mutable object?

### Core Theory

A Kotlin `data class` is meant to represent data/value-like objects. For properties declared in the primary constructor, the compiler generates:

- `equals()`
- `hashCode()`
- `toString()`
- `copy()`
- `componentN()` functions for destructuring, one per primary constructor property

Example:

```kotlin
data class User(val id: String, val name: String, val age: Int)
```

The generated behavior is based only on primary constructor properties. Properties declared inside the class body are excluded from generated `equals`, `hashCode`, `toString`, `copy`, and `componentN`.

```kotlin
data class User(val id: String) {
    var lastSeenAt: Long = 0
}
```

Two `User` objects with the same `id` are equal even if `lastSeenAt` is different, because `lastSeenAt` is not part of the primary constructor.

### Generated Methods Mental Model

For:

```kotlin
data class User(val id: String, val name: String)
```

Conceptually, Kotlin generates behavior similar to:

```kotlin
class User(val id: String, val name: String) {
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is User) return false
        if (id != other.id) return false
        if (name != other.name) return false
        return true
    }

    override fun hashCode(): Int {
        var result = id.hashCode()
        result = 31 * result + name.hashCode()
        return result
    }

    override fun toString(): String {
        return "User(id=$id, name=$name)"
    }

    operator fun component1(): String = id
    operator fun component2(): String = name

    fun copy(id: String = this.id, name: String = this.name): User {
        return User(id, name)
    }
}
```

The exact bytecode can differ, but this is the mental model interviewers usually expect.

### `==`, `===`, and `::`

In Kotlin:

- `==` means structural equality. It calls `equals`.
- `===` means referential equality. It checks whether both references point to the same object.
- `::` is not equality. It is used for callable references, such as `User::name` or `::someFunction`.

```kotlin
val a = User("1", "Ana")
val b = User("1", "Ana")

println(a == b)   // true, calls equals()
println(a === b)  // false, different object references
```

Natural interview answer:

"For data classes, `==` uses structural equality through the generated `equals`. `===` checks reference identity. I would be careful not to mix those up. `::` is a callable reference operator, not an equality operator."

### How Many Comparisons Does `equals` Do?

For a data class with `n` primary constructor properties, generated `equals` usually does:

1. A reference check: `this === other`.
2. A type check: is `other` the same data class type?
3. Up to `n` property comparisons, in primary constructor order.

It short-circuits. If the first property is different, it does not compare the rest.

For:

```kotlin
data class User(val id: String, val name: String, val age: Int)
```

Worst case when both objects are the same type and early fields match:

- reference check,
- type check,
- compare `id`,
- compare `name`,
- compare `age`.

The important nuance: a "property comparison" may itself be expensive. Comparing two `Int` values is cheap. Comparing two large `List`s may compare elements. Comparing nested data classes may recursively call their `equals`.

Natural interview answer:

"Generated `equals` first checks if both references are the same, then checks the type, then compares each primary-constructor property in order. So for `n` properties, worst case is up to `n` property comparisons after the initial checks, and it short-circuits as soon as one property differs. The real cost depends on the property types; a list or nested object can make a single property comparison more expensive."

### When Is `hashCode` Used?

`hashCode` is used by hash-based collections and algorithms, especially:

- `HashMap`
- `HashSet`
- `LinkedHashMap`
- `LinkedHashSet`
- keys in maps
- membership checks in hash collections
- operations like `distinct`, `groupBy`, and similar APIs that internally use hashing

The contract is:

- If `a == b`, then `a.hashCode() == b.hashCode()` must be true.
- If two objects have the same hash code, they are not necessarily equal.

Hash-based collections use `hashCode` first to find a bucket, then use `equals` to confirm equality inside that bucket. That is why both methods must be consistent.

Natural interview answer:

"`hashCode` is used when the object participates in hash-based lookup, like being a key in a `HashMap` or an item in a `HashSet`. The collection uses the hash to narrow down where to look, then uses `equals` to confirm the actual match. Equal objects must have the same hash code, but the same hash code does not guarantee equality because collisions are possible."

### Mutable Properties Problem

Be careful using mutable properties in data classes that are used as map keys or set items.

```kotlin
data class User(var id: String)

val user = User("1")
val set = hashSetOf(user)

user.id = "2"

println(set.contains(user)) // can be false
```

The object's hash code changed after it was placed in the set, so the set may look in the wrong bucket.

Natural interview answer:

"I avoid mutable properties in data classes used as keys in maps or items in sets. If a property that participates in `hashCode` changes after insertion, the collection may not be able to find the object anymore."

### `copy()` Is Shallow

`copy()` creates a new instance, but it does not deep-copy nested mutable objects.

```kotlin
data class Team(val members: MutableList<String>)

val a = Team(mutableListOf("Ana"))
val b = a.copy()

b.members.add("Luis")

println(a.members) // [Ana, Luis]
```

Both instances point to the same mutable list.

Natural interview answer:

"`copy()` is shallow. It creates a new object, but nested mutable objects are still shared unless I explicitly copy them too."

### When Not To Use A Data Class

Avoid data classes when:

- identity matters more than value equality,
- the object has lifecycle or resource ownership,
- equality should be custom and not based on all constructor properties,
- mutable properties would make hashing unsafe,
- the class represents behavior more than data,
- invariants require controlled construction and `copy()` would bypass the intended model.

Natural interview answer:

"I use data classes for values: UI state, DTOs, simple domain values. I am more careful with entities where identity matters, mutable objects, or classes with invariants. Data classes are convenient, but generated equality and copy must match the domain."

### Common Interview Questions

- What is a data class?
- What functions does a data class generate?
- What does `copy()` do?
- Is `copy()` deep or shallow?
- What is the difference between `==` and `===`?
- Does `==` call `equals`?
- How does generated `equals` work?
- How many comparisons does `equals` do?
- When is `hashCode` called?
- Why must `equals` and `hashCode` be consistent?
- What happens if a mutable property changes after the object is added to a `HashSet`?
- Are properties inside the body included in generated equality?
- Can you override generated methods?

### Tricky Follow-Up Questions And Answers

**Can you override generated methods?**

"You can explicitly implement `equals`, `hashCode`, or `toString` in a data class. Kotlin will then use your implementation for those. But you cannot provide explicit implementations for `copy` or `componentN`."

**Are body properties included?**

"No. Generated `equals`, `hashCode`, `toString`, `copy`, and `componentN` only use primary constructor properties."

**Are data classes immutable?**

"Not automatically. They can have `var` properties or hold mutable objects. A data class with only `val` properties can still be effectively mutable if those properties reference mutable collections or mutable objects."

**Why does Kotlin generate `componentN()`?**

"For destructuring. If I write `val (id, name) = user`, Kotlin uses `component1()` and `component2()`."

### Common Mistakes

- Saying data classes are always immutable.
- Forgetting that only primary constructor properties participate.
- Saying `copy()` is deep.
- Confusing `==` with `===`.
- Thinking `::` is equality.
- Forgetting hash collisions.
- Using mutable data classes as `HashMap` keys.
- Ignoring the cost of nested equality for lists or large object graphs.

### Checklist

- Can I name the generated methods?
- Can I explain `==`, `===`, and `::`?
- Can I describe generated `equals` step by step?
- Can I explain the number of comparisons and short-circuiting?
- Can I explain when `hashCode` is used?
- Can I explain the equality/hashCode contract?
- Can I explain shallow `copy()`?
- Can I explain why mutable keys are dangerous?

## Strong Interview Answer Bank

### What is a data class in Kotlin, and what methods does it generate?

**Strong Interview Answer**

"A Kotlin data class is a good fit when the class mainly represents a value, state, DTO, or simple domain model rather than an object with identity or complex behavior. For the properties declared in the primary constructor, the compiler generates `equals`, `hashCode`, `toString`, `copy`, and `componentN` functions for destructuring.

The important part is that those generated functions are based only on primary-constructor properties. If I declare a property inside the class body, it is not part of generated equality, hash code, copy, or destructuring. That can be useful, but it can also surprise people.

I also do not treat data classes as automatically immutable. A data class can have `var` properties, or it can hold a mutable list. And `copy()` is shallow, so nested mutable objects can still be shared. In Android I commonly use data classes for UI state and DTOs, but I am careful using them as `HashMap` keys or `HashSet` values if any equality property can change."

**If They Push Deeper**

- `==` calls `equals`; `===` checks reference identity.
- Generated `equals` checks reference, type, then properties in constructor order.
- `hashCode` is used by hash-based collections and must be consistent with `equals`.
- `copy()` is shallow.

**What Not To Say**

"A data class is just a class for storing data." That answer is too shallow and misses Kotlin's generated value semantics.

### How does `equals` work in a data class?

**Strong Interview Answer**

"Conceptually, generated `equals` first checks whether both references are the same object. If they are, it returns true. Then it checks whether the other object is the same data class type. After that, it compares each primary-constructor property in order and short-circuits on the first difference.

So if a data class has three constructor properties, the worst case is the reference check, the type check, and up to three property comparisons. But the real cost depends on those property types. Comparing two integers is trivial; comparing two lists can compare the elements; comparing nested data classes can recursively call their own `equals`.

That matters in Android UI state because large nested state objects may make equality checks more expensive than people expect, especially if the state is used in diffing or recomposition-related decisions. It does not mean data classes are bad; it just means the shape and mutability of state matter."

### When is `hashCode` used, and why should I care?

**Strong Interview Answer**

"`hashCode` matters when the object is used in hash-based lookup: `HashMap`, `HashSet`, `LinkedHashMap`, `LinkedHashSet`, and operations like `distinct` or `groupBy` that may use hashing internally. A hash-based collection uses the hash code to find a bucket, then uses `equals` to confirm the actual match.

The contract is that if two objects are equal, they must have the same hash code. The reverse is not guaranteed; two different objects can have the same hash code because collisions exist.

The practical bug is mutability. If I insert a data class into a `HashSet` and then mutate a property that participates in `hashCode`, the object may now belong to a different bucket, but the set does not move it. After that, `contains` can fail even for the same object. That is why I avoid mutable equality properties for map keys and set elements."
