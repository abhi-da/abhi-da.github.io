---
layout: single
title: "Introduction to Logic"
date: 2026-07-21
subject: "Mathematics for Economists"
toc: true
wide: true
---
<style>
  /* Override theme container limits for screen view */
  body, 
  main, 
  article, 
  .container, 
  .wrapper, 
  .content, 
  .post-content {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 auto !important;
  }
  table {
    width: 100% !important;
    display: table !important;
  }

  .back-btn {
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 6px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: background-color 0.2s ease;
  }

  .back-btn:first-child {
    background-color: transparent;
    color: #555;
    border-color: #ccc;
  }
  .back-btn:first-child:hover {
    background-color: #f0f0f0;
    color: #000;
  }

  .back-btn:last-child {
    background-color: #2563eb;
    color: #ffffff;
  }
  .back-btn:last-child:hover {
    background-color: #1d4ed8;
  }

  @media print {
    @page {
      margin: 0.5in;
    }
    .no-print {
      display: none !important;
    }
  }
</style>

<div class="no-print" style="display: flex; gap: 10px; margin-bottom: 20px;">
  <button class="back-btn" onclick="history.back()">← Back</button>
  <button class="back-btn" onclick="window.print()">📄 Download as PDF</button>
</div>

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

The above paragraph were partly written by me, and some ideas were borrowed from [How to think like a Mathematician-2009](https://blngcc.wordpress.com/wp-content/uploads/2008/11/2-kevin-houston-how-to-think-like-a-mathematician.pdf)

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

## 2.9 Some Fundamental Properties of Logical Equivalence

It's probably not surprising that a statement $P$ and its double negation $\sim(\sim P)$ mean the same thing. Let's check this with a truth table.

|  P  | $\sim P$ | $\sim(\sim P)$ |
| :-: | :------: | :------------: |
|  T  |    F     |       T        |
|  F  |    T     |       F        |

The first and last columns match, so $P \equiv \sim(\sim P)$.

We already saw earlier that $P \land Q$ and $Q \land P$ are logically equivalent — order doesn't matter for "and." There are a few more of these basic equivalences that come up all the time, so it's worth knowing them by name.

### Some Fundamental Logical Equivalences

For statements $P$, $Q$, and $R$:

**1. Commutative Laws** : order doesn't matter
(a) $P \lor Q \equiv Q \lor P$
(b) $P \land Q \equiv Q \land P$

**2. Associative Laws** : grouping doesn't matter
(a) $P \lor (Q \lor R) \equiv (P \lor Q) \lor R$
(b) $P \land (Q \land R) \equiv (P \land Q) \land R$

**3. Distributive Laws** : you can "distribute" one operation over the other, just like multiplication distributes over addition in regular algebra
(a) $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$
(b) $P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)$

**4. De Morgan's Laws** : negating an "and/or" statement flips the operation and pushes the negation inside
(a) $\sim(P \lor Q) \equiv (\sim P) \land (\sim Q)$
(b) $\sim(P \land Q) \equiv (\sim P) \lor (\sim Q)$

Each of these can be checked the same way we've been checking equivalences, build a truth table for both sides and confirm the columns match. Let's do this for the first distributive law, $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$:

|  P  |  Q  |  R  | $Q \land R$ | $P \lor Q$ | $P \lor R$ | $P \lor (Q \land R)$ | $(P \lor Q) \land (P \lor R)$ |
| :-: | :-: | :-: | :---------: | :--------: | :--------: | :------------------: | :---------------------------: |
|  T  |  T  |  T  |      T      |     T      |     T      |          T           |               T               |
|  T  |  T  |  F  |      F      |     T      |     T      |          T           |               T               |
|  T  |  F  |  T  |      F      |     T      |     T      |          T           |               T               |
|  T  |  F  |  F  |      F      |     T      |     T      |          T           |               T               |
|  F  |  T  |  T  |      T      |     T      |     T      |          T           |               T               |
|  F  |  T  |  F  |      F      |     T      |     F      |          F           |               F               |
|  F  |  F  |  T  |      F      |     F      |     T      |          F           |               F               |
|  F  |  F  |  F  |      F      |     F      |     F      |          F           |               F               |

The last two columns are identical in every row, confirming the equivalence.

**5. Negation of Implication and Biconditional**
(a) $\sim(P \Rightarrow Q) \equiv P \land (\sim Q)$
(b) $\sim(P \Leftrightarrow Q) \equiv (P \land (\sim Q)) \lor (Q \land (\sim P))$

The first one makes sense if you think about it in words: "$P \Rightarrow Q$" is only broken when $P$ is true but $Q$ turns out false — so saying "$P \Rightarrow Q$ is false" is exactly the same as saying "$P$ is true and $Q$ is false."

Let's verify (a) with a truth table:

|  P  |  Q  | $P \Rightarrow Q$ | $\sim(P \Rightarrow Q)$ | $\sim Q$ | $P \land (\sim Q)$ |
| :-: | :-: | :---------------: | :---------------------: | :------: | :----------------: |
|  T  |  T  |         T         |            F            |    F     |         F          |
|  T  |  F  |         F         |            T            |    T     |         T          |
|  F  |  T  |         T         |            F            |    F     |         F          |
|  F  |  F  |         T         |            F            |    T     |         F          |

The last two columns match, so $\sim(P \Rightarrow Q) \equiv P \land (\sim Q)$.

For (b), the idea is similar: $P \Leftrightarrow Q$ is true exactly when $P$ and $Q$ agree, so it's false exactly when they disagree — either $P$ is true and $Q$ is false, or $Q$ is true and $P$ is false.

|  P  |  Q  | $P \Leftrightarrow Q$ | $\sim(P \Leftrightarrow Q)$ | $P \land (\sim Q)$ | $Q \land (\sim P)$ | $(P \land (\sim Q)) \lor (Q \land (\sim P))$ |
| :-: | :-: | :-------------------: | :-------------------------: | :----------------: | :----------------: | :------------------------------------------: |
|  T  |  T  |           T           |              F              |         F          |         F          |                      F                       |
|  T  |  F  |           F           |              T              |         T          |         F          |                      T                       |
|  F  |  T  |           F           |              T              |         F          |         T          |                      T                       |
|  F  |  F  |           T           |              F              |         F          |         F          |                      F                       |

The last two columns match, so $\sim(P \Leftrightarrow Q) \equiv (P \land (\sim Q)) \lor (Q \land (\sim P))$.

Once we know these basic laws hold, we can use them to prove new logical equivalences just by rewriting one side step by step into the other — without having to build a fresh truth table every time.

## 2.10 Quantified Statements

An **open sentence** is a sentence that contains one or more variables, where each variable stands for some value from a set called the **domain** of that variable. It only becomes a true or false statement once we actually plug in a specific value for the variable.

For example, the open sentence "$3x = 12$," where $x$ is an integer, only becomes true when $x = 4$. For any other integer, it's false.

We usually write an open sentence in $x$ as $P(x)$, $Q(x)$, or $R(x)$. If $P(x)$ is an open sentence and the domain of $x$ is $S$, we say $P(x)$ is an open sentence **over the domain $S$**. Plugging in any specific value of $x$ from $S$ turns $P(x)$ into an actual statement (true or false).

For example, take the open sentence
$$P(x): (x-3)^2 \le 1$$
over the domain $\mathbb{Z}$ (the integers). This is true exactly when $x \in \{2, 3, 4\}$, and false for every other integer.

### Example

Let $S = \{1, 2, \ldots, 7\}$, and let

$$P(n): \frac{2n^2 + 5 + (-1)^n}{2} \text{ is prime.}$$

Plugging in each $n \in S$ gives a statement:

- $P(1)$: 3 is prime. — **True**
- $P(2)$: 7 is prime. — **True**
- $P(3)$: 11 is prime. — **True**
- $P(4)$: 19 is prime. — **True**
- $P(5)$: 27 is prime. — **False**
- $P(6)$: 39 is prime. — **False**
- $P(7)$: 51 is prime. — **False**

### Turning an open sentence into a statement: quantifiers

Besides plugging in a specific value, there's another way to turn an open sentence into a statement — by adding a **quantifier**, a phrase that tells us how many values of the domain the sentence applies to.

**The universal quantifier** ($\forall$) — means "for every," "for each," or "for all." Adding this to an open sentence $P(x)$ over domain $S$ gives:

$$\forall x \in S,\ P(x)$$

which reads: "For every $x \in S$, $P(x)$."

This statement is **true** if $P(x)$ holds for _every single_ $x$ in $S$, and **false** if it fails for even _one_ value of $x$ in $S$.

**The existential quantifier** ($\exists$) — means "there exists," "there is," "for some," or "for at least one." Adding this gives:

$$\exists x \in S,\ P(x)$$

which reads: "There exists $x \in S$ such that $P(x)$."

This statement is **true** if $P(x)$ holds for _at least one_ value of $x$ in $S$, and **false** only if it fails for _every_ value of $x$ in $S$.

### Example

Going back to the open sentence
$$P(n): \frac{2n^2 + 5 + (-1)^n}{2} \text{ is prime.}$$
over $S = \{1, 2, \ldots, 7\}$:

- $\forall n \in S, P(n)$: "For every $n \in S$, ... is prime." — **False**, since $P(5)$ is false.
- $\exists n \in S, P(n)$: "There exists $n \in S$ such that ... is prime." — **True**, since $P(1)$ is true.

So the same open sentence can produce either a true or a false statement, just depending on which quantifier you attach.

### Two variables

Sometimes an open sentence has two variables, each with its own domain (the domains don't have to match). Consider:

> For every two real numbers $x$ and $y$, $x^2 + y^2 \ge 0$.

Let $P(x, y): x^2 + y^2 \ge 0$, where both $x$ and $y$ range over $\mathbb{R}$. We can write this statement as:

$$\forall x \in \mathbb{R}, \forall y \in \mathbb{R}, P(x, y)$$

or equally well with the order of the quantifiers swapped — $\forall y \in \mathbb{R}, \forall x \in \mathbb{R}, P(x,y)$ — since two quantifiers of the _same_ type can be swapped without changing the meaning. We can also just group them: $\forall x, y \in \mathbb{R}, P(x, y)$.

Since $x^2 \ge 0$ and $y^2 \ge 0$ always, their sum $x^2 + y^2 \ge 0$ always too — so this statement is **true**.

### Negating a quantified statement

To negate $\forall x \in \mathbb{R}, \forall y \in \mathbb{R}, P(x, y)$, the universal quantifiers flip into existential ones, and the negation moves inside onto $P(x,y)$:

$$\sim\big(\forall x \in \mathbb{R}, \forall y \in \mathbb{R}, P(x,y)\big) \equiv \exists x \in \mathbb{R}, \exists y \in \mathbb{R}, \sim P(x, y)$$

In words: "There exist real numbers $x$ and $y$ such that $x^2 + y^2 < 0$."

Since we already know the original statement is true, this negation must be **false** — and indeed, $x^2 + y^2$ can never be negative.

---


