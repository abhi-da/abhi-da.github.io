---
layout: single
title: "Logic - Reference Sheet: All Laws Used in Logical Equivalence"
date: 2026-07-28
subject: "Mathematics for Economists"
toc: true
wide: true
order: 8
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

# Reference Sheet: All Laws Used in Boolean Algebra & Logical Equivalence
### Abhijeet | Logic — Boolean Algebra | July 28, 2026

---

## Why This Sheet Exists

Across all the tautology, contradiction, and equivalence problems we've solved so far, you'll notice the *same* handful of laws showing up again and again, just combined differently. This sheet collects every law used, in **both notations** side by side — Boolean form (+, ·, overline) and standard Logic form (∧, ∨, ¬) — so you have one single place to refer back to instead of hunting through each problem set.

Keep this page open while solving; almost every proof you do will only ever need these laws.

---

## 1. Commutative Law

**What it says:** Order doesn't matter for OR or AND.

| Boolean Form | Logic Form |
|---|---|
| A + B = B + A | A ∨ B ≡ B ∨ A |
| A · B = B · A | A ∧ B ≡ B ∧ A |



---

## 2. Associative Law

**What it says:** Grouping/bracket placement doesn't matter for OR or AND, as long as the operation stays the same throughout.

| Boolean Form | Logic Form |
|---|---|
| (A + B) + C = A + (B + C) | (A ∨ B) ∨ C ≡ A ∨ (B ∨ C) |
| (A · B) · C = A · (B · C) | (A ∧ B) ∧ C ≡ A ∧ (B ∧ C) |



---

## 3. Idempotent Law

**What it says:** Repeating the same variable with itself changes nothing.

| Boolean Form | Logic Form |
|---|---|
| A + A = A | A ∨ A ≡ A |
| A · A = A | A ∧ A ≡ A |



---

## 4. Double Negation (Involution) Law

**What it says:** Negating something twice brings it back to the original.

| Boolean Form | Logic Form |
|---|---|
| A̿ = A | ¬¬A ≡ A |



---

## 5. Identity Law

**What it says:** OR-ing with False (0) or AND-ing with True (1) changes nothing.

| Boolean Form | Logic Form |
|---|---|
| A + 0 = A | A ∨ False ≡ A |
| A · 1 = A | A ∧ True ≡ A |


---

## 6. Domination (Null) Law

**What it says:** OR-ing with True (1) always gives True; AND-ing with False (0) always gives False — the "dominant" value wins no matter what the other term is.

| Boolean Form | Logic Form |
|---|---|
| A + 1 = 1 | A ∨ True ≡ True |
| A · 0 = 0 | A ∧ False ≡ False |

**Used for:** the fastest way to prove a Tautology — if you can manipulate an expression until a bare "+1" appears anywhere, you're instantly done, the whole thing collapses to 1.

---

## 7. Complement Law

**What it says:** A variable OR-ed with its own negation is always True; AND-ed with its own negation is always False.

| Boolean Form | Logic Form |
|---|---|
| A + A̅ = 1 | A ∨ ¬A ≡ True |
| A · A̅ = 0 | A ∧ ¬A ≡ False |



---

## 8. Distributive Law (Two Forms — Important!)

**What it says:** AND distributes over OR, **and** (unlike ordinary arithmetic) OR also distributes over AND. This second form doesn't exist in normal number algebra, so it always feels surprising the first time.

| Boolean Form | Logic Form |
|---|---|
| A(B + C) = AB + AC | A ∧ (B ∨ C) ≡ (A∧B) ∨ (A∧C) |
| A + BC = (A + B)(A + C) | A ∨ (B ∧ C) ≡ (A∨B) ∧ (A∨C) |



---

## 9. Absorption Law

**What it says:** A bigger, more complicated term gets "absorbed" into a simpler one that already contains it.

| Boolean Form | Logic Form |
|---|---|
| A + AB = A | A ∨ (A∧B) ≡ A |
| A(A + B) = A | A ∧ (A∨B) ≡ A |



---

## 10. De Morgan's Laws

**What it says:** Negating an AND turns it into an OR of negations, and negating an OR turns it into an AND of negations. Works for any number of terms, not just two.

| Boolean Form | Logic Form |
|---|---|
| (A · B)‾ = A̅ + B̅ | ¬(A ∧ B) ≡ ¬A ∨ ¬B |
| (A + B)‾ = A̅ · B̅ | ¬(A ∨ B) ≡ ¬A ∧ ¬B |
| A₁·A₂···Aₙ‾‾‾‾‾‾‾ = A̅₁+A̅₂+···+A̅ₙ | ¬(A₁∧A₂∧···∧Aₙ) ≡ ¬A₁∨¬A₂∨···∨¬Aₙ |



---

## 11. Conversion Rules 


| Rule | Form |
|---|---|
| Conversion of Implication | A → B ≡ ¬A ∨ B |
| Conversion of Biconditional | A ↔ B ≡ (A → B) ∧ (B → A) ≡ (¬A∨B) ∧ (¬B∨A) |


---





Every single problem we solve follows the *same* overall rhythm:

1. **Convert** (→ and ↔ )
2. **De Morgan's + Double Negation** (get rid of all negations)
3. **Distribute / Expand** (open up all brackets)
4. **Complement + Identity/Domination** (kill the  0's and 1's that appear)
5. **Absorb / Commute / Associate** (arrange the terms for a clean expression)




