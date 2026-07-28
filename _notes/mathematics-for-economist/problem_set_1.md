---
layout: single
title: "Problem Set - 1"
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
# Logic Exercises — Problem Set

**Exercise 1.** State the negation of each of the following statements.

**(a)** The real number $r$ is at most 2.
**(b)** The absolute value of the real number $a$ is less than 3.
**(c)** Two angles of the triangle are $45°$.
**(d)** The area of the circle is at least $9\pi$.
**(e)** Two sides of the triangle have the same length.
**(f)** The point $P$ in the plane lies outside of the circle $C$.

---

**Exercise 2.** Let $P$: 15 is odd. and $Q$: 21 is prime. State each of the following in words and determine whether it is true or false.

**(a)** $P \lor Q$
**(b)** $P \land Q$
**(c)** $(\sim P) \lor Q$
**(d)** $P \land (\sim Q)$

---

**Exercise 3.** Consider the statements $P$: $\sqrt{2}$ is rational. and $Q$: $22/7$ is rational. Write each of the following statements in words and indicate whether it is true or false.

**(a)** $P \Rightarrow Q$
**(b)** $Q \Rightarrow P$
**(c)** $(\sim P) \Rightarrow (\sim Q)$
**(d)** $(\sim Q) \Rightarrow (\sim P)$

---

**Exercise 4.** Consider the statements:
$P$: $\sqrt{2}$ is rational.
$Q$: $\sqrt{23}$ is rational.
$R$: $\sqrt{3}$ is rational.

Write each of the following statements in words and indicate whether the statement is true or false.

**(a)** $(P \land Q) \Rightarrow R$
**(b)** $(P \land Q) \Rightarrow (\sim R)$
**(c)** $((\sim P) \land Q) \Rightarrow R$
**(d)** $(P \lor Q) \Rightarrow (\sim R)$

---

**Exercise 5.** Each of the following describes an implication. Write the implication in the form "if, then."

**(a)** Any point on the straight line with equation $2y + x - 3 = 0$ whose $x$-coordinate is an integer also has an integer for its $y$-coordinate.
**(b)** The square of every odd integer is odd.
**(c)** Let $n \in \mathbb{Z}$. Whenever $3n + 7$ is even, $n$ is odd.
**(d)** The derivative of the function $f(x) = \cos x$ is $f'(x) = -\sin x$.
**(e)** Let $C$ be a circle of circumference $4\pi$. Then the area of $C$ is also $4\pi$.
**(f)** The integer $n^3$ is even only if $n$ is even.

---

**Exercise 6.** Determine all values of $n$ in the domain $S = \{1, 2, 3\}$ for which the following is a true statement:

> A necessary and sufficient condition for $\dfrac{n^2+n}{3}$ to be even is that $\dfrac{n^2+n}{2}$ is odd.



---

**Exercise 7.** Determine all values of $n$ in the domain $S = \{2, 3, 4\}$ for which the following is a true statement:

> The integer $\dfrac{n(n-1)}{3}$ is odd if and only if $\dfrac{n(n+1)}{2}$ is even.



---

**Exercise 8.** For statements $P$ and $Q$, determine whether the compound statement

$$(P \lor Q) \lor (Q \Rightarrow P)$$

is a tautology, a contradiction, or neither.

---

**Exercise 9.** For statements $P$ and $Q$, determine whether the compound statement

$$((P \Rightarrow Q) \Rightarrow P) \Rightarrow (P \Rightarrow (Q \Rightarrow P))$$

is a tautology, a contradiction, or neither.

---

**Exercise 10.** For statements $P$, $Q$ and $R$, use a truth table to show that each of the following pairs of statements are logically equivalent.

**(a)** $(P \land Q) \Leftrightarrow P$ and $P \Rightarrow Q$.
**(b)** $P \Rightarrow (Q \lor R)$ and $(\sim Q) \Rightarrow ((\sim P) \lor R)$.

---

**Exercise 11.** For statements $P$ and $Q$, show that $(\sim Q) \Rightarrow (P \land (\sim P))$ and $Q$ are logically equivalent.

---

**Exercise 12.** For statements $P$, $Q$ and $R$, show that $(P \lor Q) \Rightarrow R$ and $(P \Rightarrow R) \land (Q \Rightarrow R)$ are logically equivalent.

---

**Exercise 13.** Two compound statements $S$ and $T$ are comprised of the same component statements $P$, $Q$ and $R$. If $S$ and $T$ are not logically equivalent, then what can we conclude from this?

---

**Exercise 14.** Construct a truth table for $P \land (Q \Rightarrow (\sim P))$.

---

**Exercise 15.** Given that the implication $(Q \lor R) \Rightarrow (\sim P)$ is false and $Q$ is false, determine the truth values of $R$ and $P$.

---

**Exercise 16.** Find a compound statement involving the component statements $P$ and $Q$ that has the following truth table:

|  P  |  Q  | $\sim Q$ |  ?  |
| :-: | :-: | :------: | :-: |
|  T  |  T  |    F     |  T  |
|  T  |  F  |    T     |  T  |
|  F  |  T  |    F     |  F  |
|  F  |  F  |    T     |  T  |

---

**Exercise 17.** Determine the truth value of each of the following quantified statements:

**(a)** $\exists x \in \mathbb{R}, x^3 + 2 = 0$.
**(b)** $\forall n \in \mathbb{N}, 2 \ge 3 - n$.
**(c)** $\forall x \in \mathbb{R}, |x| = x$.
**(d)** $\exists x \in \mathbb{Q}, x^4 - 4 = 0$.
**(e)** $\exists x, y \in \mathbb{R}, x + y = \pi$.
**(f)** $\forall x, y \in \mathbb{R}, x + y = x^2 + y^2$.

---

**Exercise 18.** Rewrite each of the implications below using (1) "only if" and (2) "sufficient."

**(a)** If a function $f$ is differentiable, then $f$ is continuous.
**(b)** If $x = -5$, then $x^2 = 25$.

---

**Exercise 19.** Let $P(n): n^2 - n + 5$ is a prime. be an open sentence over a domain $S$.

**(a)** Determine the truth values of the quantified statements $\forall n \in S, P(n)$ and $\exists n \in S, \sim P(n)$ for $S = \{1, 2, 3, 4\}$.
**(b)** Determine the truth values of the quantified statements $\forall n \in S, P(n)$ and $\exists n \in S, \sim P(n)$ for $S = \{1, 2, 3, 4, 5\}$.
**(c)** How are the statements in (a) and (b) related?

---

**Exercise 20.**

**(a)** For statements $P$, $Q$ and $R$, show that
$$((P \land Q) \Rightarrow R) \equiv ((P \land (\sim R)) \Rightarrow (\sim Q)).$$
**(b)** For statements $P$, $Q$ and $R$, show that
$$((P \land Q) \Rightarrow R) \equiv ((Q \land (\sim R)) \Rightarrow (\sim P)).$$

---

**Exercise 21.** For a fixed integer $n$, use Exercise 20 to restate the following implication in two different ways:

> If $n$ is a prime and $n > 2$, then $n$ is odd.

---

**Exercise 22.** For fixed integers $m$ and $n$, use Exercise 20 to restate the following implication in two different ways:

> If $m$ is even and $n$ is odd, then $m + n$ is odd.

---

**Exercise 23.** For a real-valued function $f$ and a real number $x$, use Exercise 20 to restate the following implication in two different ways:

> If $f'(x) = 3x^2 - 2x$ and $f(0) = 4$, then $f(x) = x^3 - x^2 + 4$.

---

**Exercise 24.** For the set $S = \{1, 2, 3\}$, give an example of three open sentences $P(n)$, $Q(n)$ and $R(n)$, each over the domain $S$, such that (1) each of $P(n)$, $Q(n)$ and $R(n)$ is a true statement for exactly two elements of $S$, (2) all of the implications $P(1) \Rightarrow Q(1)$, $Q(2) \Rightarrow R(2)$ and $R(3) \Rightarrow P(3)$ are true, and (3) the converse of each implication in (2) is false.

---

**Exercise 25.** Do there exist a set $S$ of cardinality 2 and a set $\{P(n), Q(n), R(n)\}$ of three open sentences over the domain $S$ such that the implications $P(a) \Rightarrow Q(a)$, $Q(b) \Rightarrow R(b)$ and $R(c) \Rightarrow P(c)$ are true, where $a, b, c \in S$, and the converses of these implications are all false? (Necessarily, at least two of these elements $a$, $b$, $c$ of $S$ are equal.)

---

**Exercise 26.** Let $A = \{1, 2, \ldots, 6\}$ and $B = \{1, 2, \ldots, 7\}$. For $x \in A$, let $P(x)$: $7x + 4$ is odd. For $y \in B$, let $Q(y)$: $5y + 9$ is odd. Let
$$S = \{(x, y) : x \in A, y \in B, P(x) \Rightarrow Q(y) \text{ is false}\}.$$
What is $|S|$?

---

**Exercise 27.** Let $P(x, y, z)$ be an open sentence, where the domains of $x$, $y$ and $z$ are $A$, $B$ and $C$, respectively.

**(a)** State the quantified statement $\forall x \in A, \forall y \in B, \exists z \in C, P(x, y, z)$ in words.
**(b)** State the quantified statement $\forall x \in A, \forall y \in B, \exists z \in C, P(x, y, z)$ in words for $P(x, y, z): x = yz$.
**(c)** Determine whether the quantified statement in (b) is true when $A = \{4, 8\}$, $B = \{2, 4\}$ and $C = \{1, 2, 4\}$.

---

**Exercise 28.** Let $P(x, y, z)$ be an open sentence, where the domains of $x$, $y$ and $z$ are $A$, $B$ and $C$, respectively.

**(a)** Express the negation of $\forall x \in A, \forall y \in B, \exists z \in C, P(x, y, z)$ in symbols.
**(b)** Express $\sim(\forall x \in A, \forall y \in B, \exists z \in C, P(x, y, z))$ in words.
**(c)** Determine whether $\sim(\forall x \in A, \forall y \in B, \exists z \in C, P(x, y, z))$ is true when $P(x, y, z): x + z = y$, for $A = \{1, 3\}$, $B = \{3, 5, 7\}$ and $C = \{0, 2, 4, 6\}$.

---

**Exercise 29.** Write each of the following using "if, then."

**(a)** A sufficient condition for a triangle to be isosceles is that it has two equal angles.
**(b)** Let $C$ be a circle of diameter $\sqrt{2}/\pi$. Then the area of $C$ is $1/2$.
**(c)** The 4th power of every odd integer is odd.
**(d)** Suppose that the slope of a line $\ell$ is 2. Then the equation of $\ell$ is $y = 2x + b$ for some real number $b$.
**(e)** Whenever $a$ and $b$ are nonzero rational numbers, $a/b$ is a nonzero rational number.
**(f)** For every three integers, there exist two of them whose sum is even.
**(g)** A triangle is a right triangle if the sum of two of its angles is $90°$.
**(h)** The number $\sqrt{3}$ is irrational.

---

**Exercise 30.** State the negation of each of the following statements.

**(a)** The real number $r$ has the property that $3 \le r < \pi$.
**(b)** The real number $r$ has the property that $|r - n| \ge \frac{1}{2}$ for every integer $n$.
**(c)** The real number $r$ has the property that $rs = s$ for every real number $s$.

---

**Exercise 31.** Let $\{S, T\}$ be a partition of the set $\mathbb{N}$ of positive integers and let $U$ be a nonempty subset of $\mathbb{N}$. State the negation of each of the following statements.

**(a)** Every element of $U$ can be expressed as $x + y$, where $x \in S$ and $y \in T$.
**(b)** For every $x \in S$ and $y \in T$, $xy \in S$.
**(c)** For every element $x \in S$, there is an element $y \in T$ such that $y > x$.

---

**Exercise 32.** Let $P(n)$ be an open sentence over the domain $\mathbb{N}$ of positive integers. State the negation of each of the following statements.

**(a)** If $P(n)$ is true for infinitely many $n \in \mathbb{N}$, then $P(n)$ cannot be false for infinitely many $n \in \mathbb{N}$.
**(b)** There is no element $n \in \mathbb{N}$ such that $P(n)$ and $P(n+1)$ are both true.
**(c)** If $P(n)$ is false for some positive integer $n$, then there is a smallest positive integer $m$ such that $P(m)$ is false.

---

**Exercise 33.** Each of the following describes an implication. Write the implication in the form "if, then."

**(a)** For every odd integer $n \ge 3$, the integer $n + m$ is prime for some even integer $m$.
**(b)** Let $n \in \mathbb{N}$. The integer $2n$ is even.
**(c)** We only need to know that $n$ is odd to show that $3n + 4$ is odd.
**(d)** Once we know that $n$ is an even integer, we can conclude that $n^3$ is even.
**(e)** The only possibility for the integer $n - 3$ to be even is for $n$ to be odd.

---

**Exercise 34.** Let $P(n): 2n + 1$ is even. and $Q(n): 3n + 2$ is odd. be open sentences over the domain $S = \{0, 1, 2\}$. For which $n \in S$ is $P(n) \Rightarrow Q(n)$ true?

