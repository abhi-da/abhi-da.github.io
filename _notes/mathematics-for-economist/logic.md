---
layout: single
title: "Introduction to Propositional Logic"
date: 2026-07-21
subject: "Mathematics for Economists"
toc: true
wide: true
---

<button onclick="window.print()">📄 Download as PDF</button>

You might have seen MEMES like: ![Math Meme]({{ '/assets/images/useless_math_meme.jpg' | relative_url }})

But is it really the case?

See, you may not use the exact same problems in your daily life, but it teaches you how to use a that particular tool. It controls the world. We use it to put man in the moon. Yet, it is considered useless by most of the people.

The graduate mathematics is very different then higher secondary schools mathematics, at least in India. There's a lot of rigour in graduate texts. By rigor, I mean doing the same maths with great precision. In senior secondary school, continuity is often taught intuitively: "a function is continuous if you can draw its graph in a single, free-flowing pen stroke without lifting your paper."At the graduate level, however, math demands absolute precision. Intuitive rules are replaced with formal, rigorous definitions (like the $\epsilon$-$\delta$ criterion) which we will study later in limits and continuity.We need this level of rigour because human visual intuition breaks down when dealing with complex functions. For example, $x \cdot \sin\left(\frac{1}{x}\right)$ cannot be hand-drawn. Also, computers cannot read or draw such images on their own. To make them draw such graphs, we need to feed exact definitions to them.

Imagine senior secondary as knowing how to use Python libraries, while in graduation, you are actually building them.

When you know where a particular formula or theorem comes from, the result becomes very interesting.

For example, what does the idiom "Chhattis ka aakda" mean, and how do you think it originated?

Let me ask a simple question. Take a solid ball in 3D space. Is it possible to cut it into 5 pieces, rotate those pieces around, reassemble them without stretching anything, and end up with two identical solid balls of the exact same size as the original? The intuition would say - No. That is not possible. Cause the volume then doubles.

However, [Banach–Tarski paradox](https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox) says, we can.

And No. I have got no idea about how the proof is done. These were just to stimulate the curiosity in the mind that intuition is not always correct and hence we need to define things precisely.

For example, How many months have 28 days? Some would say February. But that is wrong, All 12 months have 28 days.
Precision would mean, How many months have only 28 days. And that again cannot be February, cause we don't know if we are talking about leap or not a leap year.

Now, the above texts were to generate a bit of curiosity in the mind. I hope math sounds interesting now.

With that, let me tell you how to approach math. You cannot just read it like a novel. You can skip things which are not useful. You can move backward and forward between texts. Every author has written books on the basis of their understanding; the same doesn't apply to you.

But you will need to practice and understand how things are working. The more you practice, the better you get. By practicing, I don't mean by-hearting.

The above paragraph were some written by me, and some ideas were borrowed from [How to think like a Mathematician-2009](https://blngcc.wordpress.com/wp-content/uploads/2008/11/2-kevin-houston-how-to-think-like-a-mathematician.pdf)

With that, Let us begin with our topic: **Logic**

It is advisable to give a read to chapter 0 of [Mathematical Proofs: A Transition to Advanced Mathematics - Chartrand et al](https://www.amazon.in/Mathematical-Proofs-Transition-Advanced-Mathematics/dp/0321797094).

## Logic

### Statements

A sentence which can be either _true_ or _false_ but not _both_ is a statement. For example,

1. 2 is an even number. This statement is true.
2. 6 is a prime number. This statement is false.

Now, sometimes a sentence can be true or false, but we cannot immediately declare which. That does not mean we cannot call it a statement — it just means we are not yet able to determine its truth value.

Since statements have truth values, we can build a truth table.

A statement A can either be True or False.

**One statement (A):**

|  A  |
| :-: |
|  T  |
|  F  |

**Two statements (A, B):** each can be True or False, so there are four possible combinations.

|  A  |  B  |
| :-: | :-: |
|  T  |  T  |
|  T  |  F  |
|  F  |  T  |
|  F  |  F  |

**Three statements (A, B, C):** each can be True or False, so there are eight possible combinations.

| **A** |  B  |  C  |
| :---: | :-: | :-: |
|   T   |  T  |  T  |
|   T   |  T  |  F  |
|   T   |  F  |  T  |
|   T   |  F  |  F  |
|   F   |  T  |  T  |
|   F   |  T  |  F  |
|   F   |  F  |  T  |
|   F   |  F  |  F  |

Now we can see a pattern: if there are $n$ statements, there are $2^n$ possible combinations of truth values.

### Negations

Just like there are operations between two numbers, we have operations between two or more statements.

For example, we see $-2$ as the complete opposite of $2$.

Similarly, the negation of a statement $P$ is **not $P$**, denoted by $\neg P$. For example, if $P$: "2 is a whole number," then $\neg P$: "2 is not a whole number."

So the truth table for this new statement is as follows:

|  P  | $\neg P$ |
| :-: | :------: |
|  T  |    F     |
|  F  |    T     |

### Conjunction

Now, one more method to produce a new statement is by joining two statements together.

For example:
A: 2 is a whole number
B: 5 is an odd number

The new statement becomes $Q = A \land B$: "2 is a whole number and 5 is an odd number." This operation is called **conjunction**, and the symbol $\land$ means **and**.

The truth table for conjunction is as follows:

|  A  |  B  | $A \land B$ |
| :-: | :-: | :---------: |
|  T  |  T  |      T      |
|  T  |  F  |      F      |
|  F  |  T  |      F      |
|  F  |  F  |      F      |

**Why we need conjunction:** In everyday language, we often combine two facts into one sentence using "and." Conjunction lets us capture this formally — the combined statement $A \land B$ is true only when _both_ individual statements are true. If either one is false, the combined statement is false. This matches how we naturally think about "and" — saying "it is raining and it is cold" is only true if both parts actually hold.

### Disjunction

Similarly, we can join two statements using **disjunction**, denoted by the symbol $\lor$, which means **or**.

Using the same statements:
A: 2 is a whole number
B: 5 is an odd number

The new statement becomes $Q = A \lor B$: "2 is a whole number or 5 is an odd number."

The truth table for disjunction is as follows:

|  A  |  B  | $A \lor B$ |
| :-: | :-: | :--------: |
|  T  |  T  |     T      |
|  T  |  F  |     T      |
|  F  |  T  |     T      |
|  F  |  F  |     F      |

**Why we need disjunction:** In everyday language, we often say two things are connected by "or" — meaning at least one of them holds. Disjunction captures this formally — the combined statement $A \lor B$ is true if _at least one_ of the individual statements is true. It is false only when both are false. This matches how we think about "or" in most everyday situations — saying "it is raining or it is cold" is true as long as at least one of those is happening.

### Implications

Another way to join two statements is through **implication**, denoted by the symbol $\rightarrow$, which means **if...then**.

Using the same statements:
A: 2 is a whole number
B: 5 is an odd number

The new statement becomes $Q = A \rightarrow B$: "If 2 is a whole number, then 5 is an odd number."

The truth table for implication is as follows:

|  A  |  B  | $A \rightarrow B$ |
| :-: | :-: | :---------------: |
|  T  |  T  |         T         |
|  T  |  F  |         F         |
|  F  |  T  |         T         |
|  F  |  F  |         T         |

**Why we need implication:** In everyday language, we often say things like "if this happens, then that happens." Implication captures this formally — the statement $A \rightarrow B$ is false only in the case where $A$ is true but $B$ turns out false, since that is the one case where the "promise" is broken. In every other case, the implication is considered true. This can feel a bit strange at first — especially that $A \rightarrow B$ is true whenever $A$ is false, regardless of $B$ — but the idea is that if the starting condition never holds, the implication is not violated, so we treat it as true. We call such a case **vacuously true**.

$P \Rightarrow Q$ can also be stated as:

- If $P$, then $Q$
- $Q$ if $P$
- $P$ implies $Q$
- $P$ only if $Q$
- $P$ is sufficient for $Q$
- $Q$ is necessary for $P$

Let's break this down with a simple example. Let:

P: It is raining
Q: The ground is wet

**"If P, then Q," "Q if P," and "P implies Q"** clearly say the same thing: if it is raining, the ground is wet. That part feels obvious.

The tricky part is seeing that **"P only if Q," "P is sufficient for Q,"** and **"Q is necessary for P"** are _also_ saying the same thing.

**P only if Q:** "It is raining only if the ground is wet." This means raining can only happen when the ground is already wet — so if it is raining, the ground _must_ be wet. If the ground were somehow not wet, it could not be raining. That is exactly the same condition as "if P, then Q."

**Q is necessary for P:** "The ground being wet is necessary for it to be raining." Same idea — you cannot have rain without a wet ground. Wet ground is a _requirement_ for rain to be true. Again, this just says: if it is raining, the ground must be wet.

**P is sufficient for Q:** "Raining is sufficient for the ground to be wet." This means rain alone is enough to guarantee wet ground — you do not need anything else. If it is raining, that fact by itself is enough to conclude the ground is wet. This is just "if P, then Q" phrased from the other direction — instead of stating the requirement (Q), it states that P is _enough_ to produce it.

So all six phrasings are really the same rule — "if it is raining, the ground is wet" — just said in different everyday ways.

### Bi-Conditionals

The last basic operation is **biconditional**, denoted by the symbol $\leftrightarrow$, which means **if and only if**.

Consider the following statements:
A: A number $n$ is even
B: $n$ is divisible by 2

The new statement becomes $Q = A \leftrightarrow B$: "A number $n$ is even if and only if $n$ is divisible by 2."

The truth table for biconditional is as follows:

|  A  |  B  | $A \leftrightarrow B$ |
| :-: | :-: | :-------------------: |
|  T  |  T  |           T           |
|  T  |  F  |           F           |
|  F  |  T  |           F           |
|  F  |  F  |           T           |

**Why we need biconditional:** Sometimes we want to say two statements always hold together — either both are true, or both are false. Biconditional captures exactly this — $A \leftrightarrow B$ is true whenever $A$ and $B$ have the _same_ truth value, and false whenever they differ. In our example, whenever $n$ is even, it is also divisible by 2, and whenever it is not even, it is also not divisible by 2 — the two statements always agree, which is exactly what makes this a genuine "if and only if" relationship.

The biconditional $P \leftrightarrow Q$ can be stated in a few equivalent ways:

- $P$ is equivalent to $Q$
- $P$ if and only if $Q$
- $P$ is necessary and sufficient for $Q$

For statements $P$ and $Q$, the biconditional "$P$ if and only if $Q$" is true only when $P$ and $Q$ have the same truth value.

### Tautology and Contradiction

A **tautology** is a statement that is always true, no matter what truth values its parts have. For example, "$P \lor \neg P$" (P or not P) is always true — either P is true, or it isn't. There's no case where this fails.

|  P  | $\neg P$ | $P \lor \neg P$ |
| :-: | :------: | :-------------: |
|  T  |    F     |        T        |
|  F  |    T     |        T        |

A **contradiction** is the opposite — a statement that is always false, no matter what. For example, "$P \land \neg P$" (P and not P) can never be true — a statement and its negation cannot both hold at the same time.

|  P  | $\neg P$ | $P \land \neg P$ |
| :-: | :------: | :--------------: |
|  T  |    F     |        F         |
|  F  |    T     |        F         |

---

### Syllogism and Modus Ponens

A **syllogism** is a form of reasoning where we draw a conclusion from two given statements (called premises). For example:

- All men are mortal.
- Socrates is a man.
- Therefore, Socrates is mortal.

**Modus ponens** is one specific, very common pattern of valid reasoning. It says: if we know "if P, then Q" is true, and we also know P is true, then we can conclude Q is true.

Example:

- If it rains, the ground gets wet. ($P \rightarrow Q$)
- It is raining. ($P$)
- Therefore, the ground is wet. ($Q$)

This pattern is always valid — whenever both premises are true, the conclusion must be true too.

---

### Logical Equivalence

Two statements are **logically equivalent** if they always have the same truth value, no matter what truth values their individual parts take. We showed something similar earlier — "P only if Q," "P is sufficient for Q," and "Q is necessary for P" were all logically equivalent to "if P, then Q," because they matched in every possible case.

To check if two statements are logically equivalent, we build a truth table for both and compare — if the final columns match in every row, the statements are equivalent. For example, $P \rightarrow Q$ and $\neg P \lor Q$ are logically equivalent:

|  P  |  Q  | $P \rightarrow Q$ | $\neg P$ | $\neg P \lor Q$ |
| :-: | :-: | :---------------: | :------: | :-------------: |
|  T  |  T  |         T         |    F     |        T        |
|  T  |  F  |         F         |    F     |        F        |
|  F  |  T  |         T         |    T     |        T        |
|  F  |  F  |         T         |    T     |        T        |

Since the last two columns match in every row, we say $P \rightarrow Q \equiv \neg P \lor Q$.
