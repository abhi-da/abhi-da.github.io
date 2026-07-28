---
layout: single
title: "Systematic Method for Constructing Truth Tables for $n$ Statements"
date: 2026-07-28
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
---


# Systematic Method for Constructing Truth Tables for $n$ Statements

When constructing a truth table for $n$ propositional statements $P_1, P_2, P_3, \dots, P_n$, follow this recursive halving procedure to ensure all unique combinations of truth values ($\text{T}$ and $\text{F}$) are systematically enumerated without repetition or omission.

---

## The General Algorithm

### **Step 1: Determine Dimensions**

* **Total Rows:** For $n$ binary statements, there are $2^n$ unique truth-value combinations.
* **Total Columns:** Prepare $n$ initial columns for the input statements $P_1, P_2, \dots, P_n$ (plus additional columns for composite logical expressions as needed).

---

### **Step 2: Fill Column 1 ($P_1$)**

* Since there are $2^n$ rows, divide the total rows into two equal halves of size $\frac{2^n}{2} = 2^{n-1}$.
* Fill the **first $2^{n-1}$ rows** with **$\text{T}$**.
* Fill the **remaining $2^{n-1}$ rows** with **$\text{F}$**.

---

### **Step 3: Fill Column 2 ($P_2$)**

* Halve the block size again to $\frac{2^{n-1}}{2} = 2^{n-2}$.
* Alternately fill blocks of size $2^{n-2}$ with **$\text{T}$** and **$\text{F}$**:
* Top half (where $P_1 = \text{T}$): First $2^{n-2}$ rows $\text{T}$, next $2^{n-2}$ rows $\text{F}$.
* Bottom half (where $P_1 = \text{F}$): Next $2^{n-2}$ rows $\text{T}$, remaining $2^{n-2}$ rows $\text{F}$.



---

### **Step $k$: General Rule for Column $k$ ($P_k$)**

* For the $k$-th column ($1 \le k \le n$), the block size of repeating truth values is:

$$\text{Block Size} = 2^{n-k}$$


* Alternate between blocks of $2^{n-k}$ $\text{T}$s and $2^{n-k}$ $\text{F}$s until all $2^n$ rows are filled.
* The final column ($P_n$) will always alternate strictly row-by-row ($2^{n-n} = 2^0 = 1$): $\text{T}, \text{F}, \text{T}, \text{F}, \dots$.

---

# Examples

## 1. Example: $n = 3$ Statements ($A, B, C$)

* **Total Rows:** $2^3 = 8$
* **Column 1 ($A$):** Block size $2^{3-1} = 4 \implies 4\text{ T}'\text{s}, 4\text{ F}'\text{s}$
* **Column 2 ($B$):** Block size $2^{3-2} = 2 \implies 2\text{ T}'\text{s}, 2\text{ F}'\text{s}, 2\text{ T}'\text{s}, 2\text{ F}'\text{s}$
* **Column 3 ($C$):** Block size $2^{3-3} = 1 \implies \text{Alternating } 1\text{ T}, 1\text{ F}$

| $A$ | $B$ | $C$ |
| --- | --- | --- |
| T | T | T |
| T | T | F |
| T | F | T |
| T | F | F |
| F | T | T |
| F | T | F |
| F | F | T |
| F | F | F |

---

## 2. Example: $n = 4$ Statements ($A, B, C, D$)

* **Total Rows:** $2^4 = 16$
* **Block sizes:** $A = 8$, $B = 4$, $C = 2$, $D = 1$

| Row | $A$ | $B$ | $C$ | $D$ |
| --- | --- | --- | --- | --- |
| 1 | T | T | T | T |
| 2 | T | T | T | F |
| 3 | T | T | F | T |
| 4 | T | T | F | F |
| 5 | T | F | T | T |
| 6 | T | F | T | F |
| 7 | T | F | F | T |
| 8 | T | F | F | F |
| 9 | F | T | T | T |
| 10 | F | T | T | F |
| 11 | F | T | F | T |
| 12 | F | T | F | F |
| 13 | F | F | T | T |
| 14 | F | F | T | F |
| 15 | F | F | F | T |
| 16 | F | F | F | F |

---

## 3. Example: $n = 5$ Statements ($A, B, C, D, E$)

* **Total Rows:** $2^5 = 32$
* **Block sizes:** $A = 16$, $B = 8$, $C = 4$, $D = 2$, $E = 1$

| Row | $A$ | $B$ | $C$ | $D$ | $E$ |
| --- | --- | --- | --- | --- | --- |
| 1 | T | T | T | T | T |
| 2 | T | T | T | T | F |
| 3 | T | T | T | F | T |
| 4 | T | T | T | F | F |
| 5 | T | T | F | T | T |
| 6 | T | T | F | T | F |
| 7 | T | T | F | F | T |
| 8 | T | T | F | F | F |
| 9 | T | F | T | T | T |
| 10 | T | F | T | T | F |
| 11 | T | F | T | F | T |
| 12 | T | F | T | F | F |
| 13 | T | F | F | T | T |
| 14 | T | F | F | T | F |
| 15 | T | F | F | F | T |
| 16 | T | F | F | F | F |
| 17 | F | T | T | T | T |
| 18 | F | T | T | T | F |
| 19 | F | T | T | F | T |
| 20 | F | T | T | F | F |
| 21 | F | T | F | T | T |
| 22 | F | T | F | T | F |
| 23 | F | T | F | F | T |
| 24 | F | T | F | F | F |
| 25 | F | F | T | T | T |
| 26 | F | F | T | T | F |
| 27 | F | F | T | F | T |
| 28 | F | F | T | F | F |
| 29 | F | F | F | T | T |
| 30 | F | F | F | T | F |
| 31 | F | F | F | F | T |
| 32 | F | F | F | F | F |
