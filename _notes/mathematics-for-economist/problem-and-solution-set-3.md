---
layout: single
title: "Problem Set 3"
date: 2026-07-27
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


# Practice Problem Set 3 — Connectives, Truth Tables, and Laws of Logic

All answers below were checked by direct computation before being written — every truth table and every law-based simplification is verified correct.

---

## Part A: Truth Table Questions (10)

For each statement, construct the truth table and determine whether the statement is a **tautology**, a **contradiction**, or **neither** (a contingency).

**Q1.** $P \land (Q \lor \neg R)$

**Q2.** $(P \lor Q) \Rightarrow R$

**Q3.** $\neg(P \land Q) \lor R$

**Q4.** $(P \Rightarrow Q) \land (Q \Rightarrow P)$

**Q5.** $\neg(P \leftrightarrow Q)$

**Q6.** $(P \land \neg Q) \lor (\neg P \land Q)$

**Q7.** $(P \Rightarrow Q) \land \neg Q$

**Q8.** $P \lor (Q \land R)$

**Q9.** $(P \land Q) \lor (\neg P \land \neg Q)$

**Q10.** $\neg P \lor \neg Q \lor R$

---

## Part B: Laws of Logic Questions (15)

Simplify each expression as far as possible, naming the law used at each step (Commutative, Associative, Distributive, De Morgan's, Absorption, Identity, Negation, Idempotent, Exportation, or Double Negation).

**Q11.** Simplify: $P \land (P \lor Q)$

**Q12.** Simplify: $(P \lor Q) \land (P \lor \neg Q)$

**Q13.** Simplify: $\neg(P \lor Q) \lor (\neg P \land Q)$

**Q14.** Simplify: $P \land (\neg P \lor Q)$

**Q15.** Simplify: $(P \land Q) \lor (P \land \neg Q)$

**Q16.** Simplify: $\neg(\neg P \land \neg Q)$

**Q17.** Rewrite using exportation: $P \Rightarrow (Q \Rightarrow R)$

**Q18.** Simplify: $\neg(P \Rightarrow Q)$

**Q19.** Simplify: $[P \land (Q \lor R)] \lor (\neg P \land Q) \lor (\neg P \land R)$

**Q20.** Express the biconditional $P \leftrightarrow Q$ purely using $\land$, $\lor$, and $\neg$.

**Q21.** Simplify: $\neg(P \land Q) \land (P \lor Q)$

**Q22.** Simplify: $P \lor (\neg P \land Q)$

**Q23.** Simplify: $\neg(P \leftrightarrow Q)$ into a disjunction of two conjunctions.

**Q24.** Simplify: $(P \land Q) \lor (P \land \neg Q) \lor (\neg P \land Q)$

**Q25.** Simplify: $\neg\big(\neg(P \land Q) \land \neg R\big)$

---
---

# Answers

## Part A: Truth Table Answers

**A1.** $P \land (Q \lor \neg R)$

| $P$ | $Q$ | $R$ | $\neg R$ | $Q \lor \neg R$ | $P \land (Q \lor \neg R)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | T | **T** |
| T | T | F | T | T | **T** |
| T | F | T | F | F | **F** |
| T | F | F | T | T | **T** |
| F | T | T | F | T | **F** |
| F | T | F | T | T | **F** |
| F | F | T | F | F | **F** |
| F | F | F | T | T | **F** |

**Neither** (a contingency) — the final column has both T's and F's.

---

**A2.** $(P \lor Q) \Rightarrow R$

| $P$ | $Q$ | $R$ | $P \lor Q$ | $(P\lor Q)\Rightarrow R$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | **T** |
| T | T | F | T | **F** |
| T | F | T | T | **T** |
| T | F | F | T | **F** |
| F | T | T | T | **T** |
| F | T | F | T | **F** |
| F | F | T | F | **T** |
| F | F | F | F | **T** |

**Neither** — contingency.

---

**A3.** $\neg(P \land Q) \lor R$

| $P$ | $Q$ | $R$ | $P\land Q$ | $\neg(P\land Q)$ | $\neg(P\land Q)\lor R$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | F | **T** |
| T | T | F | T | F | **F** |
| T | F | T | F | T | **T** |
| T | F | F | F | T | **T** |
| F | T | T | F | T | **T** |
| F | T | F | F | T | **T** |
| F | F | T | F | T | **T** |
| F | F | F | F | T | **T** |

**Neither** — contingency (false only in one row: $P{=}T,Q{=}T,R{=}F$).

---

**A4.** $(P \Rightarrow Q) \land (Q \Rightarrow P)$

| $P$ | $Q$ | $P\Rightarrow Q$ | $Q\Rightarrow P$ | Result |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | **T** |
| T | F | F | T | **F** |
| F | T | T | F | **F** |
| F | F | T | T | **T** |

**Neither** — contingency. (Notice this is exactly the biconditional $P \leftrightarrow Q$ — mutual implication *is* the biconditional.)

---

**A5.** $\neg(P \leftrightarrow Q)$

| $P$ | $Q$ | $P \leftrightarrow Q$ | $\neg(P\leftrightarrow Q)$ |
|:---:|:---:|:---:|:---:|
| T | T | T | **F** |
| T | F | F | **T** |
| F | T | F | **T** |
| F | F | T | **F** |

**Neither** — contingency. (This is true exactly when $P$ and $Q$ disagree — it's the "exclusive or.")

---

**A6.** $(P \land \neg Q) \lor (\neg P \land Q)$

| $P$ | $Q$ | $P\land\neg Q$ | $\neg P\land Q$ | Result |
|:---:|:---:|:---:|:---:|:---:|
| T | T | F | F | **F** |
| T | F | T | F | **T** |
| F | T | F | T | **T** |
| F | F | F | F | **F** |

**Neither** — contingency. Notice the final column is identical to A5's — this expression is another way of writing $\neg(P\leftrightarrow Q)$.

---

**A7.** $(P \Rightarrow Q) \land \neg Q$

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg Q$ | Result |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | **F** |
| T | F | F | T | **F** |
| F | T | T | F | **F** |
| F | F | T | T | **T** |

**Neither** — contingency. Worth noticing: whenever this is true ($P{=}F,Q{=}F$), $\neg P$ is also true — this is the pattern behind **modus tollens** (from $P\Rightarrow Q$ and $\neg Q$, conclude $\neg P$).

---

**A8.** $P \lor (Q \land R)$

| $P$ | $Q$ | $R$ | $Q\land R$ | Result |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | **T** |
| T | T | F | F | **T** |
| T | F | T | F | **T** |
| T | F | F | F | **T** |
| F | T | T | T | **T** |
| F | T | F | F | **F** |
| F | F | T | F | **F** |
| F | F | F | F | **F** |

**Neither** — contingency.

---

**A9.** $(P \land Q) \lor (\neg P \land \neg Q)$

| $P$ | $Q$ | $P\land Q$ | $\neg P\land\neg Q$ | Result |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | **T** |
| T | F | F | F | **F** |
| F | T | F | F | **F** |
| F | F | F | T | **T** |

**Neither** — contingency. This is true exactly when $P$ and $Q$ **agree** — this is another (equivalent) way of writing the biconditional $P \leftrightarrow Q$ itself.

---

**A10.** $\neg P \lor \neg Q \lor R$

| $P$ | $Q$ | $R$ | Result |
|:---:|:---:|:---:|:---:|
| T | T | T | **T** |
| T | T | F | **F** |
| T | F | T | **T** |
| T | F | F | **T** |
| F | T | T | **T** |
| F | T | F | **T** |
| F | F | T | **T** |
| F | F | F | **T** |

**Neither** — contingency (false only when $P{=}T,Q{=}T,R{=}F$). Note this is logically the same as $\neg(P\land Q)\lor R$ from A3, by De Morgan's Law — compare the two final columns.

---

## Part B: Laws of Logic Answers

**A11.** $P \land (P \lor Q) \equiv \mathbf{P}$
*(Absorption Law: $P \land (P \lor Q) \equiv P$.)*

---

**A12.** $(P \lor Q) \land (P \lor \neg Q) \equiv \mathbf{P}$
$$\begin{aligned}
(P \lor Q) \land (P \lor \neg Q) &\equiv P \lor (Q \land \neg Q) &&\text{(Distributive)}\\
&\equiv P \lor F &&\text{(Negation Law)}\\
&\equiv P &&\text{(Identity Law)}
\end{aligned}$$

---

**A13.** $\neg(P \lor Q) \lor (\neg P \land Q) \equiv \mathbf{\neg P}$
$$\begin{aligned}
\neg(P\lor Q) \lor (\neg P \land Q) &\equiv (\neg P \land \neg Q) \lor (\neg P \land Q) &&\text{(De Morgan's)}\\
&\equiv \neg P \land (\neg Q \lor Q) &&\text{(Distributive)}\\
&\equiv \neg P \land T &&\text{(Negation Law)}\\
&\equiv \neg P &&\text{(Identity Law)}
\end{aligned}$$

---

**A14.** $P \land (\neg P \lor Q) \equiv \mathbf{P \land Q}$
$$\begin{aligned}
P \land (\neg P \lor Q) &\equiv (P \land \neg P) \lor (P \land Q) &&\text{(Distributive)}\\
&\equiv F \lor (P \land Q) &&\text{(Negation Law)}\\
&\equiv P \land Q &&\text{(Identity Law)}
\end{aligned}$$

---

**A15.** $(P \land Q) \lor (P \land \neg Q) \equiv \mathbf{P}$
$$\begin{aligned}
(P \land Q) \lor (P \land \neg Q) &\equiv P \land (Q \lor \neg Q) &&\text{(Distributive)}\\
&\equiv P \land T &&\text{(Negation Law)}\\
&\equiv P &&\text{(Identity Law)}
\end{aligned}$$

---

**A16.** $\neg(\neg P \land \neg Q) \equiv \mathbf{P \lor Q}$
$$\begin{aligned}
\neg(\neg P \land \neg Q) &\equiv \neg(\neg P) \lor \neg(\neg Q) &&\text{(De Morgan's)}\\
&\equiv P \lor Q &&\text{(Double Negation)}
\end{aligned}$$

---

**A17.** $P \Rightarrow (Q \Rightarrow R) \equiv \mathbf{(P \land Q) \Rightarrow R}$
*(This is the Law of Exportation. Sketch: rewrite both sides using $A\Rightarrow B \equiv \neg A \lor B$, then apply Associative and De Morgan's — both sides reduce to $\neg P \lor \neg Q \lor R$.)*

---

**A18.** $\neg(P \Rightarrow Q) \equiv \mathbf{P \land \neg Q}$
*(Negation of Implication Law — this is the one broken "promise" case: $P$ true, $Q$ false.)*

---

**A19.** $[P \land (Q \lor R)] \lor (\neg P \land Q) \lor (\neg P \land R) \equiv \mathbf{Q \lor R}$
$$\begin{aligned}
[P\land(Q\lor R)] \lor (\neg P\land Q)\lor(\neg P\land R) &\equiv [P\land(Q\lor R)] \lor [\neg P \land (Q\lor R)] &&\text{(Distributive, on the last two terms)}\\
&\equiv (Q\lor R)\land(P\lor\neg P) &&\text{(Distributive, factoring } Q\lor R\text{)}\\
&\equiv (Q\lor R)\land T &&\text{(Negation Law)}\\
&\equiv Q\lor R &&\text{(Identity Law)}
\end{aligned}$$

---

**A20.** $P \leftrightarrow Q \equiv \mathbf{(P \land Q) \lor (\neg P \land \neg Q)}$
*(True exactly when $P,Q$ agree — both true, or both false. You can verify this matches the biconditional truth table row by row, as in A9 above.)*

---

**A21.** $\neg(P \land Q) \land (P \lor Q) \equiv \mathbf{(P \land \neg Q) \lor (\neg P \land Q)}$
$$\begin{aligned}
\neg(P\land Q) \land (P\lor Q) &\equiv (\neg P \lor \neg Q) \land (P \lor Q) &&\text{(De Morgan's)}\\
&\equiv [(\neg P \lor \neg Q)\land P] \lor [(\neg P\lor\neg Q)\land Q] &&\text{(Distributive)}\\
&\equiv (\neg P\land P)\lor(\neg Q\land P) \lor (\neg P\land Q)\lor(\neg Q\land Q) &&\text{(Distributive, twice more)}\\
&\equiv F \lor (P\land\neg Q) \lor (\neg P\land Q) \lor F &&\text{(Negation Law)}\\
&\equiv (P\land\neg Q)\lor(\neg P\land Q) &&\text{(Identity Law)}
\end{aligned}$$
*(This is the "exclusive or" of $P$ and $Q$ — true exactly when they differ, matching A5/A6 above.)*

---

**A22.** $P \lor (\neg P \land Q) \equiv \mathbf{P \lor Q}$
$$\begin{aligned}
P \lor (\neg P \land Q) &\equiv (P \lor \neg P) \land (P \lor Q) &&\text{(Distributive)}\\
&\equiv T \land (P \lor Q) &&\text{(Negation Law)}\\
&\equiv P \lor Q &&\text{(Identity Law)}
\end{aligned}$$

---

**A23.** $\neg(P \leftrightarrow Q) \equiv \mathbf{(P \land \neg Q) \lor (\neg P \land Q)}$
*(Directly from A20: negate $(P\land Q)\lor(\neg P\land\neg Q)$ using De Morgan's twice — the disjunction of two conjunctions is exactly the exclusive-or form seen in A21.)*

---

**A24.** $(P \land Q) \lor (P \land \neg Q) \lor (\neg P \land Q) \equiv \mathbf{P \lor Q}$
$$\begin{aligned}
(P\land Q)\lor(P\land\neg Q)\lor(\neg P\land Q) &\equiv [P\land(Q\lor\neg Q)] \lor (\neg P\land Q) &&\text{(Distributive, first two terms)}\\
&\equiv (P \land T) \lor (\neg P\land Q) &&\text{(Negation Law)}\\
&\equiv P \lor (\neg P \land Q) &&\text{(Identity Law)}\\
&\equiv P \lor Q &&\text{(same identity as A22)}
\end{aligned}$$

---

**A25.** $\neg\big(\neg(P \land Q) \land \neg R\big) \equiv \mathbf{(P \land Q) \lor R}$
$$\begin{aligned}
\neg\big(\neg(P\land Q)\land\neg R\big) &\equiv \neg\big(\neg(P\land Q)\big) \lor \neg(\neg R) &&\text{(De Morgan's)}\\
&\equiv (P\land Q) \lor R &&\text{(Double Negation, applied twice)}
\end{aligned}$$

---

## Quick Reference: Laws Used Above

| Law | Statement |
|---|---|
| Commutative | $P\lor Q \equiv Q\lor P$; \ $P\land Q \equiv Q\land P$ |
| Associative | $P\lor(Q\lor R)\equiv(P\lor Q)\lor R$; similarly for $\land$ |
| Distributive | $P\land(Q\lor R)\equiv(P\land Q)\lor(P\land R)$; and the dual form |
| De Morgan's | $\neg(P\lor Q)\equiv\neg P\land\neg Q$; \ $\neg(P\land Q)\equiv\neg P\lor\neg Q$ |
| Absorption | $P\lor(P\land Q)\equiv P$; \ $P\land(P\lor Q)\equiv P$ |
| Identity | $P\land T\equiv P$; \ $P\lor F\equiv P$ |
| Negation | $P\lor\neg P\equiv T$; \ $P\land\neg P\equiv F$ |
| Double Negation | $\neg(\neg P)\equiv P$ |
| Idempotent | $P\lor P\equiv P$; \ $P\land P\equiv P$ |
| Exportation | $P\Rightarrow(Q\Rightarrow R)\equiv(P\land Q)\Rightarrow R$ |
| Negation of Implication | $\neg(P\Rightarrow Q)\equiv P\land\neg Q$ |
