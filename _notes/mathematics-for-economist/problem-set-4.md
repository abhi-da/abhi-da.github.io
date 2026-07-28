---
layout: single
title: "Logic: Problem and Solution Set 3"
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

# Problem Set 3 — Logic, Truth Tables, and Symbolization

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

### Deriving the SOP

#### Minterm and Maxterm

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

#### Why the Conventions Are Opposite

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

### Deriving the POS

**Rule:** AND together one maxterm for every row where the output is **False**. In that maxterm, write the *negation* of the variable if it's True in that row, or the variable as-is if it's False — the opposite convention from SOP.

Only **one** row is False: row 4 ($A=F, B=F$).

- **Row 4** ($A=F, B=F$): $A$ is False (write as-is, no negation), $B$ is False (write as-is) → $A \lor B$

Since there's only one False row, there's only one maxterm, and the POS is just that maxterm on its own — no AND needed between multiple clauses:

$$\text{POS: } A \lor B$$

---

If a table has $n$ variables, count the True rows and the False rows separately (they always sum to $2^n$). Whichever count is smaller tells us which form — SOP or POS — will be the shorter expression to write down.

For each truth table below, derive **both** the SOP and POS expressions.

**Q1.**

| $P$ | $Q$ | $R$ | Output |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | T | F | F |
| T | F | T | F |
| T | F | F | T |
| F | T | T | F |
| F | T | F | T |
| F | F | T | F |
| F | F | F | F |

**Q2.**

| $P$ | $Q$ | $R$ | Output |
|:---:|:---:|:---:|:---:|
| T | T | T | F |
| T | T | F | T |
| T | F | T | T |
| T | F | F | F |
| F | T | T | T |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

**Q3.**

| $P$ | $Q$ | Output |
|:---:|:---:|:---:|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

**Q4.**

| $P$ | $Q$ | $R$ | Output |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | T | F | F |
| T | F | T | F |
| T | F | F | F |
| F | T | T | F |
| F | T | F | F |
| F | F | T | F |
| F | F | F | T |

**Q5.**

| $P$ | $Q$ | Output |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**Q6.**

| $P$ | $Q$ | $R$ | Output |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | T | F | T |
| T | F | T | T |
| T | F | F | T |
| F | T | T | T |
| F | T | F | T |
| F | F | T | T |
| F | F | F | F |

**Q7.**

| $P$ | $Q$ | Output |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**Q8.**

| $P$ | $Q$ | $R$ | Output |
|:---:|:---:|:---:|
| T | T | T | T |
| T | T | F | T |
| T | F | T | T |
| T | F | F | F |
| F | T | T | T |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

**Q9.**

| $P$ | $Q$ | Output |
|:---:|:---:|:---:|
| T | T | F |
| T | F | F |
| F | T | F |
| F | F | T |

**Q10.**

| $P$ | $Q$ | $R$ | Output |
|:---:|:---:|:---:|
| T | T | T | T |
| T | T | F | T |
| T | F | T | T |
| T | F | F | T |
| F | T | T | T |
| F | T | F | F |
| F | F | T | F |
| F | F | F | F |

---
---

# Part 2: Proving Logical Equivalence via Truth Table (5)

For each pair, build a truth table for **both** statements and confirm the final columns match.

**Q11.** Show $P \Rightarrow Q \equiv \neg P \lor Q$

**Q12.** Show $\neg(P \land Q) \equiv \neg P \lor \neg Q$

**Q13.** Show $P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R)$

**Q14.** Show $P \leftrightarrow Q \equiv (P \Rightarrow Q) \land (Q \Rightarrow P)$

**Q15.** Show $\neg(P \Rightarrow Q) \equiv P \land \neg Q$

---
---

## Part 3: Simplification Using Laws of Logic (10)

Simplify each expression, naming the law used at each step.

**Q16.** $P \lor (P \land Q)$

**Q17.** $(P \land Q) \lor (\neg P \land Q)$

**Q18.** $\neg(P \lor \neg Q)$

**Q19.** $(P \lor Q) \land \neg P$

**Q20.** $P \lor (\neg P \land \neg Q)$

**Q21.** Prove $(P \Rightarrow Q) \land (Q \Rightarrow R) \Rightarrow (P \Rightarrow R)$ is a tautology using laws (this is the *hypothetical syllogism* pattern — chained implications).

**Q22.** $\neg(P \land \neg Q)$

**Q23.** $(P \lor \neg Q) \land Q$

**Q24.** Simplify $P \land Q \land R$, then rewrite it using only the Commutative Law with the order fully reversed.

**Q25.** $[P \land (Q \lor R)] \lor (\neg P \land Q) \lor (\neg P \land R)$ — *(this one needs two applications of Distributive plus Negation and Identity — take your time)*

---
---

## Part 4: Logical Equivalence Using Boolean Algebra (5)

Using $+$ (or), $\cdot$ (and), and $\bar{X}$ (not), prove each equivalence algebraically — the same way you did for the tautology problem earlier in this course.

**Q26.** Show $P(Q+R) = PQ + PR$

**Q27.** Show $(P+Q)(P+\bar{Q}) = P$

**Q28.** Show $\bar{P}\cdot\bar{Q} = \overline{P+Q}$ (De Morgan's, in algebraic notation)

**Q29.** Show $P + PQ = P$ (Absorption, in algebraic notation)

**Q30.** Show $(P+Q)(\bar{P}+R) = PR + \bar{P}Q$

---
---

# Part 5: Proving a Statement Is a Tautology (5)

Prove each of the following is a tautology (always true) by building its truth table.

**Q31.** $P \lor \neg P$

**Q32.** $(P \land Q) \Rightarrow P$

**Q33.** $\big[(P \Rightarrow Q) \land P\big] \Rightarrow Q$ *(this pattern is called Modus Ponens)*

**Q34.** $P \Rightarrow (Q \Rightarrow P)$

**Q35.** $(P \Rightarrow Q) \lor (Q \Rightarrow P)$

---
---

## Part 6: Proving a Statement Is a Contradiction (5)

Prove each of the following is a contradiction (always false) by building its truth table.

**Q36.** $P \land \neg P$

**Q37.** $(P \Rightarrow Q) \land (P \land \neg Q)$

**Q38.** $(P \leftrightarrow Q) \land (P \land \neg Q)$

**Q39.** $P \land Q \land \neg(P \lor Q)$

**Q40.** $(P \lor Q) \land \neg P \land \neg Q$

---
---

## Part 7: Translating English into Symbolic Logic (10)

For each sentence, define your own propositional variables clearly, then translate the sentence into symbols using $\neg, \land, \lor, \Rightarrow, \leftrightarrow$.

**Q41.** "If the price of a good rises, then the quantity demanded falls."

**Q42.** "The firm will expand only if it secures financing."

**Q43.** "Either inflation rises, or the central bank cuts interest rates, but not both."

**Q44.** "It is not the case that both the market is efficient and prices deviate from fundamentals."

**Q45.** "The student passes the course if and only if she scores at least 40% in the final exam."

**Q46.** "A necessary condition for the market to clear is that supply equals demand."

**Q47.** "If it rains and the match is not cancelled, then the ground will be muddy."

**Q48.** "The policy will succeed only if it is both well-funded and well-implemented."

**Q49.** "Either the equilibrium is unique, or there exist at least two distinct equilibria."

**Q50.** "The candidate wins the election if he secures a majority, but he does not win merely because he has the most votes (i.e. he does not win if he only has a plurality, not a majority)."

---
---
---

# ANSWERS

## Part 1: SOP and POS Answers

**A1.** True rows: $(T,T,T), (T,F,F), (F,T,F)$. False rows: $(T,T,F),(T,F,T),(F,T,T),(F,F,T),(F,F,F)$.

**SOP:** $(P\land Q\land R) \lor (P\land\neg Q\land\neg R) \lor (\neg P\land Q\land\neg R)$

**POS:** $(\neg P\lor\neg Q\lor R)\land(\neg P\lor Q\lor\neg R)\land(P\lor\neg Q\lor\neg R)\land(P\lor Q\lor\neg R)\land(P\lor Q\lor R)$

---

**A2.** True rows: $(T,T,F),(T,F,T),(F,T,T)$.

**SOP:** $(P\land Q\land\neg R)\lor(P\land\neg Q\land R)\lor(\neg P\land Q\land R)$

*(Note: no simpler closed form — this is the "exactly one of the remaining two variables differs" pattern, sometimes called "exactly two true" — same shape as A2 in the earlier problem set.)*

---

**A3.** True rows: $(T,F),(F,T)$.

**SOP:** $(P\land\neg Q)\lor(\neg P\land Q)$

**POS:** (False rows: $(T,T),(F,F)$) $\;(\neg P\lor\neg Q)\land(P\lor Q)$

*(This is the exclusive-or / "P and Q disagree" pattern you saw earlier.)*

---

**A4.** True rows: $(T,T,T),(F,F,F)$.

**SOP:** $(P\land Q\land R)\lor(\neg P\land\neg Q\land\neg R)$

---

**A5.** True rows: $(T,T),(F,T),(F,F)$.

**SOP:** $(P\land Q)\lor(\neg P\land Q)\lor(\neg P\land\neg Q)$

**POS:** (False row: $(T,F)$) $\;(\neg P\lor Q)$

*(Notice: this table is exactly $P\Rightarrow Q$ — the POS form, a single clause, is far more compact than the 3-term SOP. This is a good example of why it's worth deriving both forms and picking the shorter one.)*

---

**A6.** False only at $(F,F,F)$.

**POS:** $(P\lor Q\lor R)$ — a single clause, since there's only one False row.

**SOP** (True rows: all except $(F,F,F)$, so 7 minterms):
$(P\land Q\land R)\lor(P\land Q\land\neg R)\lor(P\land\neg Q\land R)\lor(P\land\neg Q\land\neg R)\lor(\neg P\land Q\land R)\lor(\neg P\land Q\land\neg R)\lor(\neg P\land\neg Q\land R)$

*(This is the clearest illustration yet of why POS is sometimes drastically shorter than SOP — always check which side of the table has fewer rows before committing to one form.)*

---

**A7.** True only at $(T,T)$.

**SOP:** $P \land Q$

**POS:** (False rows: $(T,F),(F,T),(F,F)$) $\;(\neg P\lor Q)\land(P\lor\neg Q)\land(P\lor Q)$

---

**A8.** True rows: $(T,T,T),(T,T,F),(T,F,T),(F,T,T)$ — the "majority" function (at least 2 of 3 true).

**SOP:** $(P\land Q\land R)\lor(P\land Q\land\neg R)\lor(P\land\neg Q\land R)\lor(\neg P\land Q\land R)$

---

**A9.** True only at $(F,F)$.

**SOP:** $\neg P\land\neg Q$

**POS:** (False rows: $(T,T),(T,F),(F,T)$) $\;(\neg P\lor\neg Q)\land(\neg P\lor Q)\land(P\lor\neg Q)$

---

**A10.** True rows: $(T,T,T),(T,T,F),(T,F,T),(T,F,F),(F,T,T)$.

**SOP:** $(P\land Q\land R)\lor(P\land Q\land\neg R)\lor(P\land\neg Q\land R)\lor(P\land\neg Q\land\neg R)\lor(\neg P\land Q\land R)$

**Simplified:** the first four terms all share $P$ and together exhaust every $Q,R$ combination, so $(P\land Q\land R)\lor(P\land Q\land\neg R)\lor(P\land\neg Q\land R)\lor(P\land\neg Q\land\neg R) \equiv P$ (factor $P$ out; the remaining $(Q\land R)\lor(Q\land\neg R)\lor(\neg Q\land R)\lor(\neg Q\land\neg R)$ is a tautology). So the whole thing reduces to $P \lor (\neg P\land Q\land R) \equiv P \lor (Q\land R)$ — the same "$X \lor (\neg X \land Y)$" pattern from an earlier problem set.

---

## Part 2: Logical Equivalence Answers

**A11.**

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg P$ | $\neg P\lor Q$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

Columns match — **equivalent**.

---

**A12.**

| $P$ | $Q$ | $P\land Q$ | $\neg(P\land Q)$ | $\neg P$ | $\neg Q$ | $\neg P\lor\neg Q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

Columns match — **equivalent**.

---

**A13.** (Already fully verified in the "Fundamental Logical Equivalences" slides — 8-row table, both sides give T,T,T,T,T,F,F,F.) **Equivalent.**

---

**A14.**

| $P$ | $Q$ | $P\leftrightarrow Q$ | $P\Rightarrow Q$ | $Q\Rightarrow P$ | $(P\Rightarrow Q)\land(Q\Rightarrow P)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T | T |
| T | F | F | F | T | F |
| F | T | F | T | F | F |
| F | F | T | T | T | T |

Columns match — **equivalent**.

---

**A15.**

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg(P\Rightarrow Q)$ | $\neg Q$ | $P\land\neg Q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | F |
| T | F | F | T | T | T |
| F | T | T | F | F | F |
| F | F | T | F | T | F |

Columns match — **equivalent**.

---

## Part 3: Laws-Based Simplification Answers

**A16.** $P\lor(P\land Q) \equiv \mathbf{P}$ *(Absorption)*

**A17.** $(P\land Q)\lor(\neg P\land Q) \equiv Q\land(P\lor\neg P) \equiv Q\land T \equiv \mathbf{Q}$ *(Distributive, Negation, Identity)*

**A18.** $\neg(P\lor\neg Q) \equiv \neg P\land\neg(\neg Q) \equiv \mathbf{\neg P\land Q}$ *(De Morgan's, Double Negation)*

**A19.** $(P\lor Q)\land\neg P \equiv (P\land\neg P)\lor(Q\land\neg P) \equiv F\lor(\neg P\land Q) \equiv \mathbf{\neg P\land Q}$ *(Distributive, Negation, Identity, Commutative)*

**A20.** $P\lor(\neg P\land\neg Q) \equiv (P\lor\neg P)\land(P\lor\neg Q) \equiv T\land(P\lor\neg Q) \equiv \mathbf{P\lor\neg Q}$ *(Distributive, Negation, Identity)*

**A21.** Let $A = (P\Rightarrow Q)\land(Q\Rightarrow R)$. Rewrite: $A \equiv (\neg P\lor Q)\land(\neg Q\lor R)$. Distribute:
$$A \equiv [(\neg P\lor Q)\land\neg Q] \lor [(\neg P\lor Q)\land R] \equiv (\neg P\land\neg Q)\lor(Q\land\neg Q)\lor(\neg P\land R)\lor(Q\land R)$$
Simplify $Q\land\neg Q \equiv F$ and drop it:
$$A \equiv (\neg P\land\neg Q)\lor(\neg P\land R)\lor(Q\land R)$$
So $A \Rightarrow (P\Rightarrow R)$ becomes $\neg A \lor (\neg P\lor R)$. Since every disjunct of $A$ already contains either $\neg P$ or (via $Q\land R$, combined with the earlier $\neg Q\lor R$ factor) leads to $R$, the whole implication reduces to $T$ — confirmed by direct truth-table check (8 rows, all True). **Tautology confirmed.**
*(This one is genuinely easier to just verify by 3-variable truth table — the pure-law route above is included to show it can be done, but this is a case where the table is the more practical method, echoing the "why do we need laws" discussion from earlier: laws generalize better, but aren't always the fastest tool for one specific check.)*

**A22.** $\neg(P\land\neg Q) \equiv \neg P\lor\neg(\neg Q) \equiv \mathbf{\neg P\lor Q}$ *(De Morgan's, Double Negation — same result as $P\Rightarrow Q$)*

**A23.** $(P\lor\neg Q)\land Q \equiv (P\land Q)\lor(\neg Q\land Q) \equiv (P\land Q)\lor F \equiv \mathbf{P\land Q}$ *(Distributive, Negation, Identity)*

**A24.** $P\land Q\land R$ is already fully simplified — it doesn't reduce further. Reversed order via Commutative Law: $\mathbf{R\land Q\land P}$ (same truth value, every row, by Commutative Law applied twice).

**A25.** $\equiv \mathbf{Q\lor R}$ — full derivation already shown in an earlier problem set (Q19 of the previous set uses this exact expression).

---

## Part 4: Boolean Algebra Answers

**A26.** $P(Q+R) = PQ+PR$ — this **is** the Distributive Law itself, stated in algebraic notation; verify by checking all 8 rows of $P,Q,R\in\{0,1\}$ — both sides agree on every row.

**A27.**
$$(P+Q)(P+\bar Q) = P + Q\bar Q \quad\text{(Distributive)} = P+0 \quad\text{(Complement)} = \mathbf{P} \quad\text{(Identity)}$$

**A28.** $\bar P\cdot\bar Q = \overline{P+Q}$ — this is De Morgan's Law in algebraic form. Direct check: $P+Q=0$ only when $P=Q=0$, in which case $\bar P\cdot\bar Q = 1\cdot 1=1=\overline{0}$; for every other $(P,Q)$, $P+Q=1$ so $\overline{P+Q}=0$, and at least one of $\bar P,\bar Q$ is $0$, making $\bar P\cdot\bar Q=0$ too. Matches in all 4 cases.

**A29.**
$$P+PQ = P(1+Q) \quad\text{(factor } P\text{)} = P\cdot 1 \quad\text{(Annihilator: } 1+Q=1\text{)} = \mathbf{P} \quad\text{(Identity)}$$

**A30.**
$$(P+Q)(\bar P+R) = P\bar P + PR + Q\bar P + QR \quad\text{(expand/Distributive)} = 0+PR+\bar PQ+QR \quad\text{(Complement)}$$
The $QR$ term is redundant here (it's the "consensus term" of $PR$ and $\bar P Q$ — it can be absorbed without changing the value), leaving:
$$= \mathbf{PR+\bar P Q}$$
*(Verified directly by checking all 8 rows — both the full 3-term version and the reduced 2-term version agree with the original on every row.)*

---

## Part 5: Tautology Answers

**A31.**

| $P$ | $\neg P$ | $P\lor\neg P$ |
|:---:|:---:|:---:|
| T | F | **T** |
| F | T | **T** |

All True — **tautology**.

---

**A32.**

| $P$ | $Q$ | $P\land Q$ | $(P\land Q)\Rightarrow P$ |
|:---:|:---:|:---:|:---:|
| T | T | T | **T** |
| T | F | F | **T** |
| F | T | F | **T** |
| F | F | F | **T** |

All True — **tautology**.

---

**A33.**

| $P$ | $Q$ | $P\Rightarrow Q$ | $(P\Rightarrow Q)\land P$ | $[(P\Rightarrow Q)\land P]\Rightarrow Q$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | **T** |
| T | F | F | F | **T** |
| F | T | T | F | **T** |
| F | F | T | F | **T** |

All True — **tautology** (this is Modus Ponens — the reasoning pattern from earlier is itself a tautology, which is exactly why it's always valid).

---

**A34.**

| $P$ | $Q$ | $Q\Rightarrow P$ | $P\Rightarrow(Q\Rightarrow P)$ |
|:---:|:---:|:---:|:---:|
| T | T | T | **T** |
| T | F | T | **T** |
| F | T | F | **T** |
| F | F | T | **T** |

All True — **tautology**.

---

**A35.**

| $P$ | $Q$ | $P\Rightarrow Q$ | $Q\Rightarrow P$ | $(P\Rightarrow Q)\lor(Q\Rightarrow P)$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | **T** |
| T | F | F | T | **T** |
| F | T | T | F | **T** |
| F | F | T | T | **T** |

All True — **tautology**. *(Interesting to notice: an implication and its converse can never both be false at once — one of them is always guaranteed to hold.)*

---

## Part 6: Contradiction Answers

**A36.**

| $P$ | $\neg P$ | $P\land\neg P$ |
|:---:|:---:|:---:|
| T | F | **F** |
| F | T | **F** |

All False — **contradiction**.

---

**A37.**

| $P$ | $Q$ | $P\Rightarrow Q$ | $P\land\neg Q$ | $(P\Rightarrow Q)\land(P\land\neg Q)$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | **F** |
| T | F | F | T | **F** |
| F | T | T | F | **F** |
| F | F | T | F | **F** |

All False — **contradiction**. *(This makes sense: it's asking $P\Rightarrow Q$ to be true and simultaneously demanding the exact combination — $P$ true, $Q$ false — that makes $P\Rightarrow Q$ false.)*

---

**A38.**

| $P$ | $Q$ | $P\leftrightarrow Q$ | $P\land\neg Q$ | Result |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | **F** |
| T | F | F | T | **F** |
| F | T | F | F | **F** |
| F | F | T | F | **F** |

All False — **contradiction**.

---

**A39.**

| $P$ | $Q$ | $P\lor Q$ | $\neg(P\lor Q)$ | $P\land Q\land\neg(P\lor Q)$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | **F** |
| T | F | T | F | **F** |
| F | T | T | F | **F** |
| F | F | F | T | **F** |

All False — **contradiction**.

---

**A40.**

| $P$ | $Q$ | $P\lor Q$ | $\neg P$ | $\neg Q$ | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | **F** |
| T | F | T | F | T | **F** |
| F | T | T | T | F | **F** |
| F | F | F | T | T | **F** |

All False — **contradiction**.

---

## Part 7: Symbolization Answers

**A41.** Let $P$: "the price of a good rises," $Q$: "the quantity demanded falls."
$$P \Rightarrow Q$$

---

**A42.** Let $P$: "the firm expands," $Q$: "the firm secures financing."
$$P \Rightarrow Q$$
*(Recall: "$P$ only if $Q$" translates the same way as "if $P$ then $Q$," as worked through earlier — financing is a **necessary** condition for expansion, not a promise that financing guarantees expansion.)*

---

**A43.** Let $P$: "inflation rises," $Q$: "the central bank cuts interest rates."
$$(P \lor Q) \land \neg(P \land Q)$$
*(This is "exclusive or" — at least one, not both. Equivalently, $P \leftrightarrow \neg Q$.)*

---

**A44.** Let $P$: "the market is efficient," $Q$: "prices deviate from fundamentals."
$$\neg(P \land Q)$$

---

**A45.** Let $P$: "the student passes the course," $Q$: "she scores at least 40% in the final exam."
$$P \leftrightarrow Q$$

---

**A46.** Let $P$: "the market clears," $Q$: "supply equals demand."
$$P \Rightarrow Q$$
*("Necessary condition for $P$" means $Q$ must hold whenever $P$ does — i.e., $P\Rightarrow Q$, the same "necessary" phrasing worked through earlier in this course.)*

---

**A47.** Let $P$: "it rains," $Q$: "the match is not cancelled" (equivalently $\neg C$ where $C$: "the match is cancelled"), $R$: "the ground will be muddy."
$$(P \land Q) \Rightarrow R$$
*(If you instead define $C$: "the match is cancelled" directly, this becomes $(P \land \neg C) \Rightarrow R$ — both are correct, just depends which variable you chose to name.)*

---

**A48.** Let $P$: "the policy succeeds," $Q$: "the policy is well-funded," $R$: "the policy is well-implemented."
$$P \Rightarrow (Q \land R)$$

---

**A49.** Let $P$: "the equilibrium is unique," $Q$: "there exist at least two distinct equilibria."
$$P \lor Q$$
*(Note: in a well-posed model these would typically also be mutually exclusive, i.e. $\neg(P\land Q)$ — but the sentence as given only asserts the "or," so the minimal correct symbolization is just $P \lor Q$.)*

---

**A50.** Let $P$: "the candidate secures a majority," $Q$: "the candidate has the most votes (a plurality)," $W$: "the candidate wins."
$$(P \Rightarrow W) \land (Q \land \neg P \Rightarrow \neg W)$$
*(Two separate implications combined: majority is sufficient to win; a mere plurality without a majority is not sufficient. This is a good example of a sentence that needs to be split into two implications rather than forced into one — a common real translation challenge.)*
