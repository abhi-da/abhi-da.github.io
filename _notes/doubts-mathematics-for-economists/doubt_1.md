---
layout: single
title: "Doubt 1: August 18, 2026"
date: 2026-08-19
subject: "Doubts - Mathematics for Economists"
toc: true
wide: true
order: 1
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
---


---



OKAY! Let's attempt this.

The Theorem says:

## Theorem 

Let $$X \subseteq \mathbb{R}$$ be non-empty and bounded.
Then, $$M_X^* = \sup X$$ iff:

1. $$M_X^*$$ is an upper bound of $$X$$.
2. $$\forall \varepsilon > 0, \exists x' \in X$$, $$M_X^* - \varepsilon < x' \le M_X^*$$.

Before beginning with the proof, let's get back to the definitions of Supremum, upper bound, and bounded set.

* **Bounded Set:** A set $$X$$ is bounded if there is a real $$M > 0$$ such that $$\forall x \in X$$, $$\vert{}x\vert{} < M$$.
* **Upper Bound:** A set $$X$$ is said to be bounded above, if there exists a real $$\beta$$ such that $$x \le \beta$$ for every $$x \in X$$, and we call $$\beta$$ an upper bound of $$X$$.
* **Least Upper Bound (Supremum):** Suppose $$E$$ is bounded above, and there exists an $$\alpha$$ with the following properties:
1. $$\alpha$$ is an upper bound of $$X$$.
2. If $$\gamma < \alpha$$, then $$\gamma$$ is not an upper bound of $$X$$.


Then we call $$\alpha = \sup(X)$$.

---

Understanding "If and Only If" (iff) Statements

Now, that we recalled the defs, let's look at how do we prove iff (if and only if) statements.

Iff statements are written as:


$$A \iff B$$

This statement is equivalent to:


$$(A \implies B) \land (B \implies A)$$

We can check the truth table:

| $$A$$ | $$B$$ | $$A \iff B$$ | $$A \implies B$$ | $$B \implies A$$ | $$(A \implies B) \land (B \implies A)$$ |
| --- | --- | --- | --- | --- | --- |
| T | T | T | T | T | T |
| T | F | F | F | T | F |
| F | T | F | T | F | F |
| F | F | T | T | T | T |


So we need to prove both $$(A \implies B) \land (B \implies A)$$ to be true statements 

---

## Applying the Structure to the Theorem

Let's revisit the theorem again,

Let $$X \subseteq \mathbb{R}$$ be non-empty & bounded (Assumption). 
Then,


$$\underbrace{M_X^* = \sup X}_{A}$$


iff


$$\underbrace{\text{(i) } M_X^* \text{ is an upper bound of } X}_{B}$$

$$\underbrace{\text{(ii) } \forall \varepsilon > 0, \exists x' \in X, M_X^* - \varepsilon < x' \le M_X^*}_{B}$$



--- 

## Proof

We must prove both directions of the "if and only if" statement: $$(A \implies B)$$ and $$(B \implies A)$$.

### Part 1: Proving $$A \implies B$$ ("Only If")

**Assumption ($$A$$):** Let $$M_X^* = \sup X$$.
**To Show ($$B$$):**

1. $$M_X^*$$ is an upper bound of $$X$$.
2. $$\forall \varepsilon > 0, \exists x' \in X$$ such that $$M_X^* - \varepsilon < x' \le M_X^*$$.

* **Proof of Condition 1:**
By definition, the supremum of a set is its least upper bound, which inherently means $$M_X^*$$ is an upper bound of $$X$$. Thus, condition (1) holds automatically.
* **Proof of Condition 2:**
Let $$\varepsilon > 0$$ be given. Because $$M_X^*$$ is the *least* upper bound ($$\sup X$$), any number strictly less than $$M_X^*$$ cannot be an upper bound of $$X$$.
Since $$\varepsilon > 0$$, we have:

$$\gamma = M_X^* - \varepsilon < M_X^*$$



Therefore, $$\gamma$$ is not an upper bound of $$X$$. By the definition of an upper bound, for $$\gamma$$ to fail to be an upper bound, there must exist some element $$x' \in X$$ that exceeds it:

$$M_X^* - \varepsilon < x'$$



Furthermore, since $$M_X^*$$ is an upper bound of $$X$$, every element in $$X$$ is less than or equal to $$M_X^*$$, meaning $$x' \le M_X^*$$.
Combining these gives:

$$M_X^* - \varepsilon < x' \le M_X^*$$



This completes the proof of Part 1.

---

### Part 2: Proving $$B \implies A$$ ("If")

**Assumption ($$B$$):**

1. $$M_X^*$$ is an upper bound of $$X$$.
2. $$\forall \varepsilon > 0, \exists x' \in X$$, $$M_X^* - \varepsilon < x' \le M_X^*$$.

**To Show ($$A$$):** $$M_X^* = \sup X$$.

The strategy is to use contradiction and assume that $$M_X^* \neq \sup{X}$$. If $$M_X^* \neq \sup{X}$$, then there must be some other number less than $$M_X^*$$ which would be the supremum. We can assume that number to be $$\gamma$$. Using the given assumptions in (B), we would finally show that $$\exists x' \in X$$ such that $$x'> \gamma$$ and so $$\gamma$$ cannot be supremum. 

* **Proof:**
We already know from assumption (1) that $$M_X^*$$ is an upper bound of $$X$$. To show that $$M_X^*$$ is the *least* upper bound ($$\sup X$$), we must show that no number strictly less than $$M_X^*$$ can be an upper bound.
We proceed by contradiction. Assume that $$M_X^*$$ is **not** the supremum. Then there exists some upper bound $$\gamma$$ of $$X$$ such that:

$$\gamma < M_X^*$$



Let us define $$\varepsilon = M_X^* - \gamma$$. Since $$\gamma < M_X^*$$, it follows that $$\varepsilon > 0$$.
By our assumption (2), because $$\varepsilon > 0$$, there exists an element $$x' \in X$$ such that:

$$M_X^* - \varepsilon < x'$$


Substituting our definition of $$\varepsilon$$ = ($$M_X^* - \gamma$$) back into the inequality gives:

$$M_X^* - (M_X^* - \gamma) < x' \implies \gamma < x'$$


**The Contradiction:** We have found an element $$x' \in X$$ that is strictly greater than $$\gamma$$ ($$\gamma < x'$$). This directly contradicts the assumption that $$\gamma$$ is an upper bound of $$X$$.
Therefore, no upper bound can be strictly less than $$M_X^*$$, proving that $$M_X^*$$ is indeed the least upper bound.
Thus, $$M_X^* = \sup X$$.  We proved $$B \implies A$$.


### Part 2: Proving $$B \implies A$$ ("If") [By Contrapositive]



Instead of a direct proof, we use **contraposition**:


$$\sim A \implies \sim B$$

Where **Statement $$A$$** is $$M_X^* = \sup X$$, and **Statement $$B$$** is the conjunction of conditions (1) and (2):

1. $$M_X^*$$is an upper bound of $$X$$.
2. $$\forall \varepsilon > 0, \exists x' \in X$$, $$M_X^* - \varepsilon < x' \le M_X^*$$.

By De Morgan's Laws, the negation ($$\sim B$$) is an **"OR"** statement:

1. $$M_X^*$$ is **not** an upper bound of $$X$$, **OR**
2. $$\exists \varepsilon > 0, \forall x' \in X$, $x' \le M_X^* - \varepsilon$$.

We assume $$\sim A$$ ($$M_X^* \neq \sup X$$) and show that it forces $$\sim B$$ to be true by two distinct cases.


To be a supremum ($$\alpha = \sup X$$), a number must satisfy an **AND** condition: it must be an upper bound ($$\alpha$$ is an upper bound of $$X$$) $$\land$$ it must be the least upper bound ($$\forall \gamma < \alpha$$, $$\gamma$$ is not an upper bound of $$X$$). Both conditions have to simultaneously hold true.[**From the definition of supremum**]

Therefore, when we want to prove something is not the supremum ($$\sim A$$ or $$M_X^* \neq \sup X$$), we are saying that the definition of supremum has failed. Because it required both things to be true together, failing to be a supremum means at least one of those conditions broke down. That brings us right back to De Morgan's Law:

If the "AND" definition fails $$\sim (P \land Q)$$, it means $$\sim P \lor \sim Q$$ ([Condition 1 failed] $$\lor$$ [Condition 2 failed]).

This is precisely why our proof splits into two distinct cases:

* **Case I:** It failed because it's not even an upper bound to begin with ($$\sim P$$).
* **Case II:** It failed because, even though it is an upper bound ($$P$$), it's not the least one (meaning $$\sim Q$$).

#### Case I: $$M_X^*$$ is not an upper bound of $$X$$

* If $$M_X^*$$ is not an upper bound of $$X$$, then condition (1) of statement $$B$$ is directly violated.
* Since part (1) of the "OR" statement for $$\sim B$$ is satisfied, $$\sim B$$ holds true.

#### Case II: $$M_X^*$$ is an upper bound, but not the supremum

* If $$M_X^*$$ is an upper bound but not the supremum, there exists another upper bound $$M_X^{**}$$ such that $$M_X^{**} < M_X^*$$.
* Let us choose $$\varepsilon = M_X^* - M_X^{**}$$. Since $$M_X^{**}} < M_X^*$$, it follows that $$\varepsilon > 0$$.
* Because $$M_X^{**}$$ is an upper bound, every element $$x' \in X$$ satisfies:

$$x' \le M_X^{**} = M_X^* - \varepsilon < M_X^*$$


* This means there exists an $$\varepsilon > 0$$ for which **no** element in $$X$$ can satisfy $$M_X^* - \varepsilon < x'$$, directly violating condition (2) of statement $$B$$. 
* So part (2) of the "OR" statement for $$\sim B$$ is satisfied (Cause part 2 of B is not satisfied, $$\sim B$$ holds true.

In all cases, $$\sim A \implies \sim B$$. Therefore, by contraposition, $$B \implies A$$, establishing that $$M_X^* = \sup X$$.



