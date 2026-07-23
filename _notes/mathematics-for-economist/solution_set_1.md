---
layout: single
title: "Solution Set - 1"
date: 2026-07-21
subject: "Mathematics for Economists"
toc: true
---

---
layout: single
title: "Introduction to  Logic"
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
    max-width: 100% !important; /* Changes maximum reading width to 90% of screen */
    width: 100% !important;
    margin: 0 auto !important; /* Centers the content */
  }

  /* Make tables stretch cleanly across the wider space */
  table {
    width: 100% !important;
    display: table !important; /* Fixes themes that force horizontal table scrolling */
  }
</style>
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

---

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
