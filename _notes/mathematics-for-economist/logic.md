---
layout: single
title: "Introduction to Propositional Logic"
date: 2026-07-21
subject: "Mathematics for Economists"
toc: true
---
<button onclick="window.print()" class="btn btn--primary">📄 Save Note as PDF</button>
## 1. Fundamentals & Definitions

A **proposition** is a declarative statement that is either strictly **true ($T$)** or **false ($F$)**, but never both simultaneously.

* $P$: "The market is in general equilibrium."
* $Q$: "Prices adjust instantaneously to clear supply and demand."

---

## 2. Logical Operators & Truth Tables

We form compound propositions using logical connectives.

### 2.1 Conjunction (AND: $\land$)
The conjunction $P \land Q$ is true **only when both** $P$ and $Q$ are true.

| $P$ | $Q$ | $P \land Q$ |
| :---: | :---: | :---: |
| $T$ | $T$ | **$T$** |
| $T$ | $F$ | **$F$** |
| $F$ | $T$ | **$F$** |
| $F$ | $F$ | **$F$** |

### 2.2 Material Implication (IF... THEN: $\rightarrow$)
The conditional statement $P \rightarrow Q$ asserts that $P$ implies $Q$. It is **false only when** the premise $P$ is true and the conclusion $Q$ is false.

$$\text{Premise } (P) \implies \text{Conclusion } (Q)$$

| $P$ | $Q$ | $P \rightarrow Q$ |
| :---: | :---: | :---: |
| $T$ | $T$ | **$T$** |
| $T$ | $F$ | **$F$** |
| $F$ | $T$ | **$T$** |
| $F$ | $F$ | **$T$** |

---

## 3. Important Equivalences

Two statements are **logically equivalent** ($\equiv$) if they share identical truth values across all possible scenarios.

### De Morgan's Laws
1. $\neg (P \land Q) \equiv \neg P \lor \neg Q$
2. $\neg (P \lor Q) \equiv \neg P \land \neg Q$

### Contraposition
A conditional statement is logically equivalent to its **contrapositive**:

$$(P \rightarrow Q) \equiv (\neg Q \rightarrow \neg P)$$

> **Example:** 
> * **Original:** "If a consumer maximizes utility, then their marginal rate of substitution equals the price ratio."
> * **Contrapositive:** "If a consumer's marginal rate of substitution does not equal the price ratio, then they are not maximizing utility."