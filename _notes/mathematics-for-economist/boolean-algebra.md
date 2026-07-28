---
layout: single
title: "Boolean Algebra"
date: 2026-07-28
subject: "Mathematics for Economists"
toc: true
wide: true
order: 4
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



## 1. Boolean Variables & Operations

**Binary Domain:** Variables operate on the set **B = {0, 1}**, where 0 ≡ False and 1 ≡ True.

| Operation | Symbol | Meaning |
|---|---|---|
| OR (Disjunction) | A + B (or A ∨ B) | Outputs 1 if at least one operand is 1 |
| AND (Conjunction) | A · B (or A ∧ B) | Outputs 1 only if both operands are 1 |
| NOT (Negation) | A̅ (or ¬A) | Inverts the binary value (0 → 1, 1 → 0) |

Notice something already — we are writing logic like **ordinary arithmetic**: `+` for OR, `·` for AND. This is not a coincidence, this is the whole trick. Our brain is already trained since school days to manipulate `+` and `·` expressions fast. Boolean Algebra is simply borrowing that comfort and applying it to logic.

---

## 2. Laws of Boolean Algebra

### Commutative & Associative
- A + B = B + A
- A · B = B · A
- (A + B) + C = A + (B + C)
- (A · B) · C = A · (B · C)

### Idempotent & Involution
- A + A = A  |  A · A = A
- A̿ = A  (double negation gives back A)

### Distributive & Identity
- A(B + C) = AB + AC
- A + BC = (A + B)(A + C)
- A + 0 = A  |  A · 1 = A
- A + 1 = 1  |  A · 0 = 0

### Absorption Laws
- A + AB = A
- A(A + B) = A

### De Morgan's Laws
- A₁ · A₂ · · · Aₙ‾‾‾‾‾‾‾‾‾‾‾‾ = A̅₁ + A̅₂ + · · · + A̅ₙ
- A₁ + A₂ + · · · + Aₙ‾‾‾‾‾‾‾‾‾‾‾‾ = A̅₁ · A̅₂ · · · A̅ₙ

In plain words — "the negation of an AND becomes an OR of negations" and vice versa. Very useful when a compound expression is looking messy with brackets everywhere.



---
### Illustration: Deriving a Statement from a Truth Table — SOP and POS (10)

Given a truth table's final column, we can always reconstruct a matching logical expression two ways:

Let us first understand how to derive an expression from a truth table:

#### The Truth Table for $A \lor B$

Union, in set language, is exactly "or" in logic — an element is in $A \cup B$ if it's in $A$, or in $B$, or both:

| $A$ | $B$ | $A \lor B$ |
|:---:|:---:|:---:|
| T | T | **T** |
| T | F | **T** |
| F | T | **T** |
| F | F | **F** |

---

## Deriving the SOP

## Minterm and Maxterm

**Minterm.** For a set of $n$ variables, a **minterm** is an AND-term that includes *every* variable exactly once — either the variable itself or its negation, never both, never left out. Because every variable is forced to take a specific True/False value in a minterm, each minterm corresponds to exactly **one row** of the truth table, and is **True for that one row only, and False everywhere else**.

For two variables $A, B$, there are $2^2 = 4$ possible minterms — one per row:

| Row | $A$ | $B$ | Minterm |
|:---:|:---:|:---:|:---:|
| 1 | T | T | $A \land B$ |
| 2 | T | F | $A \land \neg B$ |
| 3 | F | T | $\neg A \land B$ |
| 4 | F | F | $\neg A \land \neg B$ |

Check row 2's minterm, $A \land \neg B$, against the table: it's True only when $A{=}T$ and $B{=}F$ — exactly row 2, and False in the other three rows. That's the defining property of a minterm — it "picks out" one single row and no other.

---

**Maxterm.** A **maxterm** is the mirror image: an OR-term that includes every variable exactly once — itself or its negation — but built with the *opposite* convention. Because of how OR works, a maxterm is **False for exactly one row, and True everywhere else**.

The same four maxterms for $A, B$:

| Row | $A$ | $B$ | Maxterm |
|:---:|:---:|:---:|:---:|
| 1 | T | T | $\neg A \lor \neg B$ |
| 2 | T | F | $\neg A \lor B$ |
| 3 | F | T | $A \lor \neg B$ |
| 4 | F | F | $A \lor B$ |

Check row 4's maxterm, $A \lor B$: it's False only when $A{=}F$ and $B{=}F$ — exactly row 4 — and True in the other three rows.

---

## Why the Conventions Are Opposite

This is the part that's easy to mix up, so here's the reasoning behind it, not just the rule.

**For a minterm** (built for a *True* row): you want the AND-term to be True *at that row and nowhere else*. AND is True only when every piece is True — so if $A{=}T$ at that row, you keep $A$ (so it can be True there); if $A{=}F$ at that row, you write $\neg A$ instead (so *it* becomes True there). Match the term's truth to the row's actual values.

**For a maxterm** (built for a *False* row): you want the OR-term to be False *at that row and nowhere else*. OR is False only when *every* piece is False — so if $A{=}T$ at that row, you need a piece that's False when $A$ is True, which is $\neg A$; if $A{=}F$ at that row, you need $A$ itself (False when $A$ is False). So you write the *opposite* of what the row shows — which is exactly why the maxterm convention flips the minterm convention.

A minterm is "True exactly at its row," built by matching the row; a maxterm is "False exactly at its row," built by mismatching the row — and SOP/POS are just "OR together the minterms for the True rows" and "AND together the maxterms for the False rows," respectively, which is exactly the recipe you've already been using.

**Rule:** OR together one minterm for every row where the output is **True**. In that minterm, write the variable as-is if it's True in that row, or negate it if it's False.

### A Worked Example: $A \lor B$

Let's apply both definitions to one  table:

| $A$ | $B$ | $A \lor B$ |
|:---:|:---:|:---:|
| T | T | **T** |
| T | F | **T** |
| F | T | **T** |
| F | F | **F** |

**Picking out the minterms (True rows):** rows 1, 2, and 3 are True, so we build one minterm per row and OR them together:

$$(A \land B) \lor (A \land \neg B) \lor (\neg A \land B)$$

Each minterm here is doing exactly what the definition says— $A \land B$ is True only at row 1, $A \land \neg B$ is True only at row 2, $\neg A \land B$ is True only at row 3 — so their OR is True at rows 1, 2, and 3, and False at row 4. That matches the table exactly.

**Picking out the maxterms (False rows):** only row 4 is False, so there's just one maxterm, built with the flipped convention — since $A{=}F$ and $B{=}F$ at that row, we write both variables as-is (no negation):

$$A \lor B$$

This single maxterm is False only at row 4 (where $A{=}F$ and $B{=}F$) and True everywhere else — again matching the table exactly, and in this case handing us back the original expression with no simplification needed at all.

We can simplify this using the laws we already have — $(A\land B)\lor(A\land\neg B) \equiv A$ (Distributive + Negation + Identity), then $A \lor (\neg A\land B) \equiv A\lor B$ (the same pattern from A22 in the last set) — which correctly lands us back at $A \lor B$. 

We can confirm the sam eusing truth table.

---

## 4. Proving Tautologies and Contradictions

A statement is a **tautology** if it is always TRUE, that is, in the truth-table world, the final column is *all T's, no exceptions*. In the Boolean Algebra world, a tautology means the expression algebraically **simplifies to 1** (since 1 ≡ True), no matter what A, B, C stand for.

Before jumping to examples, one small conversion rule you must keep in your pocket, since Boolean Algebra doesn't have `→` and `↔` directly and we don't perform operstion on `→` and `↔`, we convert:

- **P → Q ≡ P̅ + Q**
- **P ↔ Q ≡ (P̅ + Q)(Q̅ + P)**

This conversion is standard and once done, everything is pure `+`, `·`, and `¬` — plain algebra from here.

---


### Example 1 — Modus Ponens: (A  (A → B)) → B


Convert: [A · (A̅ + B)]̅ + B

Step 1 — distribute inside: A(A̅ + B) = AA̅ + AB = 0 + AB = AB  (using A·A̅ = 0 and Identity law)

So expression becomes: (AB)̅ + B

Step 2 — apply De Morgan's: A̅ + B̅ + B

Step 3 — B̅ + B = 1 (a tautology), 

Step 4: and A̅ + 1 = 1 (Identity/Domination law)



---



### Example 2 — Hypothetical Syllogism: ((A → B) ∧ (B → C)) → (A → C)



Convert: [(A̅ + B)(B̅ + C)]̅ + (A̅ + C)

Expand the bracket: (A̅ + B)(B̅ + C) = A̅B̅ + A̅C + BB̅ + BC = A̅B̅ + A̅C + 0 + BC = A̅B̅ + A̅C + BC

Negate using De Morgan's: (A̅B̅ + A̅C + BC)̅ — treat as OR of 3 terms, negate each and AND them:
= (A + B)(A + C̅)(B̅ + C̅)



We have: **X + Y**, where X = (A + B)(A + C̅)(B̅ + C̅) and Y = (A̅ + C)

#### Expand X fully

First multiply the first two brackets:

(A + B)(A + C̅) = AA + AC̅ + AB + BC̅ = A + AC̅ + AB + BC̅

Since A + AC̅ + AB = A(1 + C̅ + B) = A·1 = A (Domination law: 1 + anything = 1), this collapses to:

**(A + B)(A + C̅) = A + BC̅**

Now multiply this result with the third bracket (B̅ + C̅):

(A + BC̅)(B̅ + C̅) = AB̅ + AC̅ + BC̅B̅ + BC̅C̅

Simplify each piece:
- BC̅B̅ = BB̅C̅ = 0·C̅ = 0  (since B·B̅ = 0)
- BC̅C̅ = BC̅  (since C̅·C̅ = C̅, Idempotent law)

So:

**X = AB̅ + AC̅ + BC̅**



#### Add Y

X + Y = AB̅ + AC̅ + BC̅ + A̅ + C

Now here's the neat regrouping — pick out **AC̅** and **C** from this sum:

AC̅ + C = C + AC̅ = (C + A)(C + C̅)  — using Distributive law in reverse (X + YZ pattern, here X=C, Y=A, Z=C̅)

= (C + A)(1) = **A + C**  (since C + C̅ = 1)

So our expression becomes:

X + Y = AB̅ + BC̅ + **(A + C)** + A̅

Rearranging the terms (Commutative law):

= AB̅ + BC̅ + C + **A + A̅**



Now **A + A̅ = 1** (Excluded Middle / Complement law), so:

= AB̅ + BC̅ + C + **1**

And by Domination law, **anything + 1 = 1**, so the whole thing collapses to:

**X + Y = 1**

---

#### Example 3 — A (A + B)  (¬A + C)  (¬B ∨ C) → C



Convert: [(A+B)(A̅+C)(B̅+C)]̅ + C

Step 1 — first simplify (A+B)(A̅+C): expand = AA̅ + AC + A̅B + BC = 0 + AC + A̅B + BC = AC + A̅B + BC

Step 2 — now AND this with (B̅+C): 
(AC + A̅B + BC)(B̅+C) = ACB̅ + AC·C + A̅BB̅ + A̅BC + BCB̅ + BC·C
= ACB̅ + AC + 0 + A̅BC + 0 + BC   (using B·B̅=0, C·C=C)
= AC(B̅+1) + A̅BC + BC = AC + A̅BC + BC   (since B̅+1 = 1)
= AC + BC(A̅+1) = AC + BC   (since A̅+1 = 1)
= C(A+B)   (factoring out C, Distributive law)

Step 3 — negate: [C(A+B)]̅ = C̅ + (A+B)̅ = C̅ + A̅B̅   (De Morgan's twice)

Step 4 — OR with C: C̅ + A̅B̅ + C = (C̅+C) + A̅B̅ = 1 + A̅B̅ = 1



---

#### Example 4: (A + B)·A̅·B̅ 

Expand (A+B) with the AND terms , use Distributive law:

(A + B)·A̅·B̅ = A·A̅·B̅ + B·A̅·B̅

Simplify each term:

A·A̅·B̅ = (A·A̅)·B̅ = 0·B̅ = 0
B·A̅·B̅ = A̅·(B·B̅) = A̅·0 = 0

Add:

= 0 + 0 = 0

 Contradiction.
 ----
 
#### Example 5: A(A̅ + B)B̅ 

Expand A·(A̅+B) first (distribute law):

A·(A̅ + B) = AA̅ + AB = 0 + AB = AB

Now AND with B̅:

AB·B̅ = A·(BB̅) = A·0 = 0

Contradiction

----




