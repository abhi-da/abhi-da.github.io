---
layout: single
title: "Solution Set - 1"
date: 2026-07-21
subject: "Mathematics for Economists"
toc: true
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
    max-width: 100% !important; /* Changes maximum reading width to 90% of screen */
    width: 100% !important;
    margin: 0 auto !important; /* Centers the content */
  }
  /* Make tables stretch cleanly across the wider space */
  table {
    width: 100% !important;
    display: table !important; /* Fixes themes that force horizontal table scrolling */
  }

  /* Base styles for both */
  .back-btn {
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 6px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: background-color 0.2s ease;
  }

  /* First button (Back) - Secondary look */
  .back-btn:first-child {
    background-color: transparent;
    color: #555;
    border-color: #ccc;
  }
  .back-btn:first-child:hover {
    background-color: #f0f0f0;
    color: #000;
  }

  /* Second button (Download PDF) - Accent/Primary look */
  .back-btn:last-child {
    background-color: #2563eb; /* Clean blue */
    color: #ffffff;
  }
  .back-btn:last-child:hover {
    background-color: #1d4ed8;
  }

  /* Hide the buttons themselves when printing/saving as PDF */
@media print {
  @page {
    margin: 0.5in; /* your own margin, replacing the browser's default print margins */
  }
}
</style>

<div class="no-print" style="display: flex; gap: 10px; margin-bottom: 20px;">
  <button class="back-btn" onclick="history.back()">← Back</button>
  <button class="back-btn" onclick="window.print()">📄 Download as PDF</button>
</div>

# Logic Exercises — Answer Set

**1(a)** Negation: The real number $r$ is greater than 2.

**1(b)** Negation: The absolute value of the real number $a$ is at least 3.

**1(c)** Negation: It is not the case that two angles of the triangle are $45°$ (i.e., at most one angle of the triangle is $45°$).

**1(d)** Negation: The area of the circle is less than $9\pi$.

**1(e)** Negation: No two sides of the triangle have the same length.

**1(f)** Negation: The point $P$ does not lie outside of circle $C$ (i.e., $P$ lies on or inside $C$).

---

**2.** $P$ is **True** (15 is odd). $Q$ is **False** (21 = 3 × 7, not prime).

**(a)** $P \lor Q$: "15 is odd or 21 is prime." — **True**.
**(b)** $P \land Q$: "15 is odd and 21 is prime." — **False**.
**(c)** $(\sim P) \lor Q$: "15 is not odd, or 21 is prime." — **False**.
**(d)** $P \land (\sim Q)$: "15 is odd and 21 is not prime." — **True**.

---

**3.** $P$ is **False** ($\sqrt{2}$ is irrational). $Q$ is **True** ($22/7$ is a ratio of integers).

**(a)** $P \Rightarrow Q$: "If $\sqrt{2}$ is rational, then $22/7$ is rational." — **True** (vacuously, $P$ false).
**(b)** $Q \Rightarrow P$: "If $22/7$ is rational, then $\sqrt{2}$ is rational." — **False**.
**(c)** $(\sim P) \Rightarrow (\sim Q)$: "If $\sqrt{2}$ is not rational, then $22/7$ is not rational." — **False**.
**(d)** $(\sim Q) \Rightarrow (\sim P)$: "If $22/7$ is not rational, then $\sqrt{2}$ is not rational." — **True** (vacuously, $\sim Q$ false).

---

**4.** $P$, $Q$, and $R$ are all **False** (none of $\sqrt{2}$, $\sqrt{23}$, $\sqrt{3}$ is rational).

**(a)** $(P \land Q) \Rightarrow R$: "If $\sqrt{2}$ is rational and $\sqrt{23}$ is rational, then $\sqrt{3}$ is rational." — **True** (vacuously).
**(b)** $(P \land Q) \Rightarrow (\sim R)$: "If $\sqrt{2}$ is rational and $\sqrt{23}$ is rational, then $\sqrt{3}$ is not rational." — **True** (vacuously).
**(c)** $((\sim P) \land Q) \Rightarrow R$: "If $\sqrt{2}$ is not rational and $\sqrt{23}$ is rational, then $\sqrt{3}$ is rational." — **True** (vacuously — $Q$ false makes antecedent false).
**(d)** $(P \lor Q) \Rightarrow (\sim R)$: "If $\sqrt{2}$ is rational or $\sqrt{23}$ is rational, then $\sqrt{3}$ is not rational." — **True** (vacuously).

_All four are vacuously true, since $P$, $Q$, $R$ are all false, making every antecedent built from them false._

---

**5.**

**(a)** "If a point on the line $2y + x - 3 = 0$ has an integer $x$-coordinate, then it has an integer $y$-coordinate."
**(b)** "If $n$ is an odd integer, then $n^2$ is odd."
**(c)** "If $3n + 7$ is even, then $n$ is odd" (for $n \in \mathbb{Z}$).
**(d)** "If $f(x) = \cos x$, then $f'(x) = -\sin x$."
**(e)** "If $C$ is a circle of circumference $4\pi$, then the area of $C$ is $4\pi$."
**(f)** "If $n^3$ is even, then $n$ is even."

---

**6.** ⚠️ Source text for this problem was garbled in extraction and could not be reliably reconstructed — please confirm the exact expressions from your original source.

---

**7.** ⚠️ Source text for this problem was garbled in extraction and could not be reliably reconstructed — please confirm the exact expressions from your original source.

---

**8.** Truth table for $(P \lor Q) \lor (Q \Rightarrow P)$:

|  P  |  Q  | $P \lor Q$ | $Q \Rightarrow P$ | $(P \lor Q) \lor (Q \Rightarrow P)$ |
| :-: | :-: | :--------: | :---------------: | :---------------------------------: |
|  T  |  T  |     T      |         T         |                  T                  |
|  T  |  F  |     T      |         T         |                  T                  |
|  F  |  T  |     T      |         F         |                  T                  |
|  F  |  F  |     F      |         T         |                  T                  |

**Conclusion:** Always True — this is a **tautology**.

---

**9.** Truth table for $((P \Rightarrow Q) \Rightarrow P) \Rightarrow (P \Rightarrow (Q \Rightarrow P))$:

|  P  |  Q  | $P \Rightarrow Q$ | $(P \Rightarrow Q) \Rightarrow P$ | $Q \Rightarrow P$ | $P \Rightarrow (Q \Rightarrow P)$ | Final |
| :-: | :-: | :---------------: | :-------------------------------: | :---------------: | :-------------------------------: | :---: |
|  T  |  T  |         T         |                 T                 |         T         |                 T                 |   T   |
|  T  |  F  |         F         |                 T                 |         T         |                 T                 |   T   |
|  F  |  T  |         T         |                 F                 |         F         |                 T                 |   T   |
|  F  |  F  |         T         |                 F                 |         T         |                 T                 |   T   |

**Conclusion:** Always True — this is a **tautology**.

---

**10(a)** $(P \land Q) \Leftrightarrow P$ and $P \Rightarrow Q$:

|  P  |  Q  | $P \land Q$ | $(P \land Q) \Leftrightarrow P$ | $P \Rightarrow Q$ |
| :-: | :-: | :---------: | :-----------------------------: | :---------------: |
|  T  |  T  |      T      |                T                |         T         |
|  T  |  F  |      F      |                F                |         F         |
|  F  |  T  |      F      |                T                |         T         |
|  F  |  F  |      F      |                T                |         T         |

The last two columns match in every row → **logically equivalent**. ✓

**10(b)** $P \Rightarrow (Q \lor R)$ and $(\sim Q) \Rightarrow ((\sim P) \lor R)$:

|  P  |  Q  |  R  | $Q \lor R$ | $P \Rightarrow (Q \lor R)$ | $\sim Q$ | $\sim P$ | $(\sim P) \lor R$ | $(\sim Q) \Rightarrow ((\sim P) \lor R)$ |
| :-: | :-: | :-: | :--------: | :------------------------: | :------: | :------: | :---------------: | :--------------------------------------: |
|  T  |  T  |  T  |     T      |             T              |    F     |    F     |         T         |                    T                     |
|  T  |  T  |  F  |     T      |             T              |    F     |    F     |         F         |                    T                     |
|  T  |  F  |  T  |     T      |             T              |    T     |    F     |         T         |                    T                     |
|  T  |  F  |  F  |     F      |             F              |    T     |    F     |         F         |                    F                     |
|  F  |  T  |  T  |     T      |             T              |    F     |    T     |         T         |                    T                     |
|  F  |  T  |  F  |     T      |             T              |    F     |    T     |         T         |                    T                     |
|  F  |  F  |  T  |     T      |             T              |    T     |    T     |         T         |                    T                     |
|  F  |  F  |  F  |     F      |             T              |    T     |    T     |         T         |                    T                     |

The last two columns match in every row → **logically equivalent**. ✓

---

**11.** $(\sim Q) \Rightarrow (P \land (\sim P))$ and $Q$:

Since $P \land (\sim P)$ is always **False**, regardless of $P$:

|  Q  | $\sim Q$ | $P \land (\sim P)$ | $(\sim Q) \Rightarrow (P \land (\sim P))$ |
| :-: | :------: | :----------------: | :---------------------------------------: |
|  T  |    F     |         F          |                     T                     |
|  F  |    T     |         F          |                     F                     |

The last column matches the $Q$ column exactly (T, F) → **logically equivalent**. ✓

---

**12.** $(P \lor Q) \Rightarrow R$ and $(P \Rightarrow R) \land (Q \Rightarrow R)$:

|  P  |  Q  |  R  | $P \lor Q$ | $(P \lor Q) \Rightarrow R$ | $P \Rightarrow R$ | $Q \Rightarrow R$ | $(P \Rightarrow R) \land (Q \Rightarrow R)$ |
| :-: | :-: | :-: | :--------: | :------------------------: | :---------------: | :---------------: | :-----------------------------------------: |
|  T  |  T  |  T  |     T      |             T              |         T         |         T         |                      T                      |
|  T  |  T  |  F  |     T      |             F              |         F         |         F         |                      F                      |
|  T  |  F  |  T  |     T      |             T              |         T         |         T         |                      T                      |
|  T  |  F  |  F  |     T      |             F              |         F         |         T         |                      F                      |
|  F  |  T  |  T  |     T      |             T              |         T         |         T         |                      T                      |
|  F  |  T  |  F  |     T      |             F              |         T         |         F         |                      F                      |
|  F  |  F  |  T  |     F      |             T              |         T         |         T         |                      T                      |
|  F  |  F  |  F  |     F      |             T              |         T         |         T         |                      T                      |

The last two columns match in every row → **logically equivalent**. ✓

---

**13.** We can conclude only that there exists **at least one** assignment of truth values to $P$, $Q$, $R$ for which $S$ and $T$ differ — i.e., at least one row of the truth table where one is True and the other is False.

This does **not** mean $S$ and $T$ disagree on every assignment — they may still agree on some rows. "Not logically equivalent" only rules out agreement on _all_ rows.

---

**14.** Truth table for $P \land (Q \Rightarrow (\sim P))$:

|  P  |  Q  | $\sim P$ | $Q \Rightarrow (\sim P)$ | $P \land (Q \Rightarrow (\sim P))$ |
| :-: | :-: | :------: | :----------------------: | :--------------------------------: |
|  T  |  T  |    F     |            F             |                 F                  |
|  T  |  F  |    F     |            T             |                 T                  |
|  F  |  T  |    T     |            T             |                 F                  |
|  F  |  F  |    T     |            T             |                 F                  |

---

**15.** An implication $X \Rightarrow Y$ is false only when $X$ is true and $Y$ is false. So $(Q \lor R) = T$ and $(\sim P) = F$, which gives $P = T$. Since $Q$ is given false and $Q \lor R = T$, we need $R = T$.

**Answer:** $R = T$, $P = T$.

---

**16.** Comparing the given column to standard operations, the truth table matches $Q \Rightarrow P$:

|  P  |  Q  | $Q \Rightarrow P$ |
| :-: | :-: | :---------------: |
|  T  |  T  |         T         |
|  T  |  F  |         T         |
|  F  |  T  |         F         |
|  F  |  F  |         T         |

**Answer:** $Q \Rightarrow P$ (equivalently, $(\sim Q) \lor P$).

---

**17.**

**(a)** $\exists x \in \mathbb{R}, x^3 + 2 = 0$: solving, $x = -\sqrt[3]{2}$, a real number. — **True**.
**(b)** $\forall n \in \mathbb{N}, 2 \ge 3 - n$: for $n = 1$, $2 \ge 2$ holds; for larger $n$, $3-n$ only gets smaller. — **True**.
**(c)** $\forall x \in \mathbb{R}, |x| = x$: fails for any negative $x$, e.g. $x = -1$ gives $|-1| = 1 \ne -1$. — **False**.
**(d)** $\exists x \in \mathbb{Q}, x^4 - 4 = 0$: solving, $x = \pm\sqrt{2}$, which is irrational, not rational. — **False**.
**(e)** $\exists x, y \in \mathbb{R}, x + y = \pi$: e.g. $x = 0, y = \pi$. — **True**.
**(f)** $\forall x, y \in \mathbb{R}, x + y = x^2 + y^2$: fails for e.g. $x = 2, y = 0$ ($2 \ne 4$). — **False**.

---

**18.**

**(a)** If $f$ is differentiable, then $f$ is continuous.

- **Only if:** "$f$ is differentiable only if $f$ is continuous."
- **Sufficient:** "$f$ being differentiable is a sufficient condition for $f$ to be continuous."

**(b)** If $x = -5$, then $x^2 = 25$.

- **Only if:** "$x = -5$ only if $x^2 = 25$."
- **Sufficient:** "$x = -5$ is a sufficient condition for $x^2 = 25$."

---

**19.** $P(n): n^2 - n + 5$ is prime.

**(a)** For $S = \{1,2,3,4\}$: $P(1){=}5$, $P(2){=}7$, $P(3){=}11$, $P(4){=}17$ — all prime, so all four are **True** statements.
$\forall n \in S, P(n)$: **True**. $\exists n \in S, \sim P(n)$: **False** (no counterexample exists).

**(b)** For $S = \{1,2,3,4,5\}$: additionally $P(5) = 25 - 5 + 5 = 25 = 5^2$, **not prime**.
$\forall n \in S, P(n)$: **False** (fails at $n=5$). $\exists n \in S, \sim P(n)$: **True** (witnessed by $n=5$).

**(c)** Adding the element 5 to the domain introduces a counterexample, which flips the universal statement from true to false, and correspondingly flips the existential "some $n$ fails" statement from false to true.

---

**20.**

**(a)** $((P \land Q) \Rightarrow R) \equiv ((P \land (\sim R)) \Rightarrow (\sim Q))$

Using $X \Rightarrow Y \equiv (\sim X) \lor Y$ and De Morgan's law:

$(P \land Q) \Rightarrow R \equiv \sim(P \land Q) \lor R \equiv (\sim P) \lor (\sim Q) \lor R$

$(P \land (\sim R)) \Rightarrow (\sim Q) \equiv \sim(P \land (\sim R)) \lor (\sim Q) \equiv (\sim P) \lor R \lor (\sim Q)$

Both simplify to $(\sim P) \lor (\sim Q) \lor R$ (order doesn't matter by the commutative law), so the two statements are logically equivalent. $\blacksquare$

**(b)** $((P \land Q) \Rightarrow R) \equiv ((Q \land (\sim R)) \Rightarrow (\sim P))$

$(Q \land (\sim R)) \Rightarrow (\sim P) \equiv \sim(Q \land (\sim R)) \lor (\sim P) \equiv (\sim Q) \lor R \lor (\sim P)$

This is the same as $(\sim P) \lor (\sim Q) \lor R$ from part (a), so both sides are equivalent to $(P \land Q) \Rightarrow R$. $\blacksquare$

---

**21.** With $P$: $n$ is prime, $Q$: $n > 2$, $R$: $n$ is odd — the statement "If $n$ is a prime and $n>2$, then $n$ is odd" is $(P \land Q) \Rightarrow R$.

Using the two forms from Exercise 20:

- **Form (a):** "If $n$ is prime and $n$ is even, then $n \le 2$."
- **Form (b):** "If $n > 2$ and $n$ is even, then $n$ is not prime."

---

**22.** With $P$: $m$ is even, $Q$: $n$ is odd, $R$: $m+n$ is odd:

- **Form (a):** "If $m$ is even and $m+n$ is even, then $n$ is even."
- **Form (b):** "If $n$ is odd and $m+n$ is even, then $m$ is odd."

---

**23.** With $P$: $f'(x) = 3x^2 - 2x$, $Q$: $f(0) = 4$, $R$: $f(x) = x^3 - x^2 + 4$:

- **Form (a):** "If $f'(x) = 3x^2 - 2x$ and $f(x) \ne x^3 - x^2 + 4$, then $f(0) \ne 4$."
- **Form (b):** "If $f(0) = 4$ and $f(x) \ne x^3 - x^2 + 4$, then $f'(x) \ne 3x^2 - 2x$."

---

**24.** Over $S = \{1, 2, 3\}$, take:

$$P(n): n > 1, \qquad Q(n): n \text{ is odd}, \qquad R(n): n < 3$$

**Truth values:**

| $n$ | $P(n)$ | $Q(n)$ | $R(n)$ |
| :-: | :----: | :----: | :----: |
|  1  |   F    |   T    |   T    |
|  2  |   T    |   F    |   T    |
|  3  |   T    |   T    |   F    |

Each of $P$, $Q$, $R$ is true for exactly two elements of $S$. ✓

**Checking the required implications:**

- $P(1) \Rightarrow Q(1)$: $F \Rightarrow T = $ **True**; converse $Q(1) \Rightarrow P(1)$: $T \Rightarrow F = $ **False**. ✓
- $Q(2) \Rightarrow R(2)$: $F \Rightarrow T = $ **True**; converse $R(2) \Rightarrow Q(2)$: $T \Rightarrow F = $ **False**. ✓
- $R(3) \Rightarrow P(3)$: $F \Rightarrow T = $ **True**; converse $P(3) \Rightarrow R(3)$: $T \Rightarrow F = $ **False**. ✓

All conditions are satisfied.

---

**25.** **No** — no such $S$ and open sentences exist.

Since $|S| = 2$, the three elements $a, b, c \in S$ cannot all be distinct (pigeonhole principle) — at least two must coincide. We check each possible coincidence and show it leads to a contradiction.

From $P(a) \Rightarrow Q(a)$ true with false converse: $P(a) = F$, $Q(a) = T$.
From $Q(b) \Rightarrow R(b)$ true with false converse: $Q(b) = F$, $R(b) = T$.
From $R(c) \Rightarrow P(c)$ true with false converse: $R(c) = F$, $P(c) = T$.

- If $a = b$: then $Q(a) = T$ (from the first) but $Q(b) = F$ (from the second) — contradiction, since $a=b$ forces $Q(a)=Q(b)$.
- If $b = c$: then $R(b) = T$ (from the second) but $R(c) = F$ (from the third) — contradiction.
- If $a = c$: then $P(a) = F$ (from the first) but $P(c) = T$ (from the third) — contradiction.

Every possible coincidence among $a, b, c$ leads to a contradiction, and by pigeonhole at least one coincidence must occur. Hence no such $S$, $P$, $Q$, $R$ can exist. $\blacksquare$

---

**26.** $P(x): 7x+4$ is odd, for $x \in A = \{1,\ldots,6\}$. Since $7x+4$ has the same parity as $x$ (as $7$ is odd and $4$ is even), $P(x)$ is true exactly when $x$ is odd: $x \in \{1, 3, 5\}$ — **3 values**.

$Q(y): 5y+9$ is odd, for $y \in B = \{1,\ldots,7\}$. Since $5y$ has the same parity as $y$, and adding $9$ (odd) flips the parity, $Q(y)$ is true exactly when $y$ is even: $y \in \{2, 4, 6\}$, so $Q(y)$ is **false** when $y$ is odd: $y \in \{1,3,5,7\}$ — **4 values**.

$P(x) \Rightarrow Q(y)$ is false exactly when $P(x) = T$ and $Q(y) = F$, i.e., $x \in \{1,3,5\}$ and $y \in \{1,3,5,7\}$.

$$|S| = 3 \times 4 = 12$$

---

**27.**

**(a)** In words: "For every $x \in A$ and every $y \in B$, there exists $z \in C$ such that $P(x,y,z)$."

**(b)** For $P(x,y,z): x = yz$: "For every $x \in A$ and every $y \in B$, there exists $z \in C$ such that $x = yz$."

**(c)** With $A = \{4,8\}$, $B = \{2,4\}$, $C = \{1,2,4\}$, check each pair by solving $z = x/y$:

| $x$ | $y$ | $z = x/y$ | In $C$? |
| :-: | :-: | :-------: | :-----: |
|  4  |  2  |     2     |    ✓    |
|  4  |  4  |     1     |    ✓    |
|  8  |  2  |     4     |    ✓    |
|  8  |  4  |     2     |    ✓    |

Every pair has a valid $z \in C$, so the statement is **True**.

---

**28.**

**(a)** $\sim(\forall x \in A, \forall y \in B, \exists z \in C, P(x,y,z)) \equiv \exists x \in A, \exists y \in B, \forall z \in C, \sim P(x,y,z)$

**(b)** In words: "There exists $x \in A$ and there exists $y \in B$ such that for every $z \in C$, $P(x,y,z)$ is false."

**(c)** With $P(x,y,z): x+z=y$, $A=\{1,3\}$, $B=\{3,5,7\}$, $C=\{0,2,4,6\}$: first check whether the _original_ statement ($\forall x,\forall y,\exists z, x+z=y$) is true, by solving $z = y - x$ for each pair:

- $x=1$: $y=3 \Rightarrow z=2 \in C$; $y=5 \Rightarrow z=4 \in C$; $y=7 \Rightarrow z=6 \in C$.
- $x=3$: $y=3 \Rightarrow z=0 \in C$; $y=5 \Rightarrow z=2 \in C$; $y=7 \Rightarrow z=4 \in C$.

Every pair finds a valid $z \in C$, so the original statement is **True** — meaning its negation is **False**.

---

**29.**

**(a)** "If a triangle has two equal angles, then it is isosceles."
**(b)** "If $C$ is a circle of diameter $\sqrt{2}/\pi$, then the area of $C$ is $1/2$."
**(c)** "If $n$ is an odd integer, then $n^4$ is odd."
**(d)** "If the slope of a line $\ell$ is 2, then the equation of $\ell$ is $y = 2x + b$ for some real number $b$."
**(e)** "If $a$ and $b$ are nonzero rational numbers, then $a/b$ is a nonzero rational number."
**(f)** "If three integers are given, then two of them have an even sum."
**(g)** "If the sum of two angles of a triangle is $90°$, then the triangle is a right triangle."
**(h)** "If a number equals $\sqrt{3}$, then it is irrational."

---

**30.**

**(a)** Negation: The real number $r$ does not satisfy $3 \le r < \pi$ — i.e., $r < 3$ or $r \ge \pi$.
**(b)** Negation: There exists an integer $n$ such that $|r - n| < \frac{1}{2}$.
**(c)** Negation: There exists a real number $s$ such that $rs \ne s$.

---

**31.**

**(a)** Negation: There is an element of $U$ that cannot be expressed as $x+y$ for any $x \in S$ and $y \in T$.
**(b)** Negation: There exist $x \in S$ and $y \in T$ such that $xy \notin S$.
**(c)** Negation: There exists an element $x \in S$ such that for every $y \in T$, $y \le x$.

---

**32.**

**(a)** Negation: $P(n)$ is true for infinitely many $n \in \mathbb{N}$, and $P(n)$ is also false for infinitely many $n \in \mathbb{N}$.
**(b)** Negation: There exists an element $n \in \mathbb{N}$ such that $P(n)$ and $P(n+1)$ are both true.
**(c)** Negation: $P(n)$ is false for some positive integer $n$, and there is no smallest positive integer $m$ such that $P(m)$ is false.

---

**33.**

**(a)** "If $n$ is an odd integer with $n \ge 3$, then there exists an even integer $m$ such that $n+m$ is prime."
**(b)** "If $n \in \mathbb{N}$, then $2n$ is even."
**(c)** "If $n$ is odd, then $3n+4$ is odd."
**(d)** "If $n$ is an even integer, then $n^3$ is even."
**(e)** "If $n-3$ is even, then $n$ is odd."

---

**34.** $P(n): 2n+1$ is even. Note that $2n+1$ is **always odd** for any integer $n$ (since $2n$ is even and adding 1 makes it odd), so $P(n)$ is **false** for every $n \in S$.

Since $P(n)$ is false for all $n \in \{0,1,2\}$, the implication $P(n) \Rightarrow Q(n)$ is **vacuously true** for every $n \in S$, regardless of $Q(n)$.

**Answer:** $P(n) \Rightarrow Q(n)$ is true for all $n \in S = \{0, 1, 2\}$.

