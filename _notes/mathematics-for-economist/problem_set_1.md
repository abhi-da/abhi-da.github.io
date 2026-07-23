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


# Logic Exercises — Problem Set

### **Exercise 1.** State the negation of each of the following statements.

**(a)** The real number $r$ is at most 2.
**(b)** The absolute value of the real number $a$ is less than 3.
**(c)** Two angles of the triangle are $45°$.
**(d)** The area of the circle is at least $9\pi$.
**(e)** Two sides of the triangle have the same length.
**(f)** The point $P$ in the plane lies outside of the circle $C$.

---

## **Exercise 2.** Let $P$: 15 is odd. and $Q$: 21 is prime. State each of the following in words and determine whether it is true or false.

**(a)** $P \lor Q$
**(b)** $P \land Q$
**(c)** $(\sim P) \lor Q$
**(d)** $P \land (\sim Q)$

---

## **Exercise 3.** Consider the statements $P$: $\sqrt{2}$ is rational. and $Q$: $22/7$ is rational. Write each of the following statements in words and indicate whether it is true or false.

**(a)** $P \Rightarrow Q$
**(b)** $Q \Rightarrow P$
**(c)** $(\sim P) \Rightarrow (\sim Q)$
**(d)** $(\sim Q) \Rightarrow (\sim P)$

---

## **Exercise 4.** Consider the statements:
$P$: $\sqrt{2}$ is rational.
$Q$: $\sqrt{23}$ is rational.
$R$: $\sqrt{3}$ is rational.

Write each of the following statements in words and indicate whether the statement is true or false.

**(a)** $(P \land Q) \Rightarrow R$
**(b)** $(P \land Q) \Rightarrow (\sim R)$
**(c)** $((\sim P) \land Q) \Rightarrow R$
**(d)** $(P \lor Q) \Rightarrow (\sim R)$

---

## **Exercise 5.** Each of the following describes an implication. Write the implication in the form "if, then."

**(a)** Any point on the straight line with equation $2y + x - 3 = 0$ whose $x$-coordinate is an integer also has an integer for its $y$-coordinate.
**(b)** The square of every odd integer is odd.
**(c)** Let $n \in \mathbb{Z}$. Whenever $3n + 7$ is even, $n$ is odd.
**(d)** The derivative of the function $f(x) = \cos x$ is $f'(x) = -\sin x$.
**(e)** Let $C$ be a circle of circumference $4\pi$. Then the area of $C$ is also $4\pi$.
**(f)** The integer $n^3$ is even only if $n$ is even.

---

## **Exercise 6.** Determine all values of $n$ in the domain $S = \{1, 2, 3\}$ for which the following is a true statement:

> A necessary and sufficient condition for $\dfrac{n^2+n}{3}$ to be even is that $\dfrac{n^2+n}{2}$ is odd.

---

## **Exercise 7.** Determine all values of $n$ in the domain $S = \{2, 3, 4\}$ for which the following is a true statement:

> The integer $\dfrac{n(n-1)}{3}$ is odd if and only if $\dfrac{n(n+1)}{2}$ is even.

---

## **Exercise 8.** For statements $P$ and $Q$, determine whether the compound statement

$$(P \lor Q) \lor (Q \Rightarrow P)$$

is a tautology, a contradiction, or neither.

---

## **Exercise 9.** For statements $P$ and $Q$, determine whether the compound statement

$$((P \Rightarrow Q) \Rightarrow P) \Rightarrow (P \Rightarrow (Q \Rightarrow P))$$

is a tautology, a contradiction, or neither.

---

## **Exercise 10.** For statements $P$, $Q$ and $R$, use a truth table to show that each of the following pairs of statements are logically equivalent.

**(a)** $(P \land Q) \Leftrightarrow P$ and $P \Rightarrow Q$.
**(b)** $P \Rightarrow (Q \lor R)$ and $(\sim Q) \Rightarrow ((\sim P) \lor R)$.

---

## **Exercise 11.** For statements $P$ and $Q$, show that $(\sim Q) \Rightarrow (P \land (\sim P))$ and $Q$ are logically equivalent.

---

## **Exercise 12.** For statements $P$, $Q$ and $R$, show that $(P \lor Q) \Rightarrow R$ and $(P \Rightarrow R) \land (Q \Rightarrow R)$ are logically equivalent.

---

## **Exercise 13.** Two compound statements $S$ and $T$ are comprised of the same component statements $P$, $Q$ and $R$. If $S$ and $T$ are not logically equivalent, then what can we conclude from this?
