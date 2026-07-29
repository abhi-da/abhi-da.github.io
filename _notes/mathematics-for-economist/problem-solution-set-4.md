---
layout: single
title: "Logic: Problem and Solution Set 4"
date: 2026-07-28
subject: "Mathematics for Economists"
toc: true
wide: true
order: 9
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

# Logic & Boolean Algebra Practice Set


## Section A: Logical Equivalence (20 Questions)

*Use laws such as Distributive, De Morgan's, Absorption, Idempotent, Commutative, Associative, etc.*


1. Prove: ¬(A → (B → C)) ≡ (A ∧ B) ∧ ¬C

2. Prove: (A → B) ∨ (A → C) ≡ A → (B ∨ C)

3. Prove: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ C) ≡ (A ∨ B) ∧ C

4. Prove: (A ∨ B) ∧ (A ∨ ¬B) ∧ (¬A ∨ B) ≡ A ∧ B





5. Prove: $\neg(p \to q) \equiv p \land \neg q$

6. Prove: $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$

7. Prove: $(p \to q) \land (p \to r) \equiv p \to (q \land r)$

8. Prove: $(p \to r) \land (q \to r) \equiv (p \lor q) \to r$

9. Prove: $\neg(p \leftrightarrow q) \equiv p \leftrightarrow \neg q$

10. Prove: $p \lor \neg(p \land q) \equiv T$ (Tautology)

11. Prove: $p \land \neg(p \lor q) \equiv F$ (Contradiction)

12. Prove: $(p \lor q) \land (\neg p \lor q) \equiv q$

13. Prove: $(p \land q) \lor (p \land \neg q) \equiv p$

14. Prove: $p \lor (\neg p \land q) \equiv p \lor q$

15. Prove: $\neg p \to (q \to p) \equiv p \lor \neg q$

16. Prove: $(p \to q) \to r \equiv (\neg p \lor q) \to r$

17. Prove: $[(p \lor q) \land \neg p] \to q$ is a tautology


---


## Section B: Boolean Algebra Laws (10 Questions)

*Simplify each expression using laws such as Idempotent, Complement, Absorption, Distributive, De Morgan's, Consensus, etc.*


1. Simplify: $A + A \cdot B$

2. Simplify: $A \cdot (A + B)$

3. Simplify: $A + A' \cdot B$

4. Simplify: $A \cdot (A' + B)$

5. Simplify: $(A + B) \cdot (A + B')$

6. Simplify: $A \cdot B + A \cdot B' + A' \cdot B$

7. Simplify: $(A + B)' + (A' \cdot B)$

8. Simplify: $A \cdot B + A' \cdot C + B \cdot C$ (Consensus theorem)

9. Simplify: $(A + B) \cdot (A + C) \cdot (B + C)$

10. Simplify: $A' \cdot B' \cdot C + A' \cdot B \cdot C + A \cdot B' \cdot C$


---


## Section C: Truth Table → Statement (5 Questions)

For each truth table, determine a logical statement (using $p, q$, and connectives $\land, \lor, \neg, \to, \leftrightarrow$) that produces the given output column.


**1.**


| p | q | Output |

|---|---|--------|

| T | T | T |

| T | F | F |

| F | T | F |

| F | F | T |


**2.**


| p | q | Output |

|---|---|--------|

| T | T | T |

| T | F | T |

| F | T | F |

| F | F | T |


**3.**


| p | q | Output |

|---|---|--------|

| T | T | F |

| T | F | T |

| F | T | T |

| F | F | F |


**4.**


| p | q | Output |

|---|---|--------|

| T | T | F |

| T | F | F |

| F | T | F |

| F | F | T |


**5.**


| p | q | r | Output |

|---|---|---|--------|

| T | T | T | T |

| T | T | F | T |

| T | F | T | T |

| T | F | F | F |

| F | T | T | T |

| F | T | F | F |

| F | F | T | F |

| F | F | F | F |





# Answer Key


## Section A: Logical Equivalence Proofs


**1.** 

 
¬(A → (B → C)) 
 
 
= ¬(¬A ∨ (B → C)) (Converted the outer implication term)
 

 
= ¬(¬A ∨ (¬B ∨ C)) ((Converted the inner implication term)
 

 
= ¬¬A ∧ ¬(¬B ∨ C) (De-Morgan)
 

 
= A ∧ ¬(¬B ∨ C) (Double Negation on A)
 

 
= A ∧ (¬¬B ∧ ¬C) (De-Morgan)
 

 
= A ∧ (B ∧ ¬C) (De-Morgan)
 

 
= (A ∧ B) ∧ ¬C = RHS (Associative) 
 
---



**2.**

 
(A → B) ∨ (A → C)
 
 
= (¬A ∨ B) ∨ (¬A ∨ C) (Converting the Implications)
 

 
= ¬A ∨ B ∨ ¬A ∨ C (Associative Law)
 

 
= (¬A ∨ ¬A) ∨ B ∨ C (Commutative Law)
 

 
= ¬A ∨ B ∨ C (Idempotent Law (¬A ∨ ¬A = ¬A))
 

 
= ¬A ∨ (B ∨ C) (Associative Law)
 

 
= A → (B ∨ C) = RHS (Reverse Conversion of →)
 
---



**3.** 

 
(A ∨ B) ∧ (¬A ∨ C) = (A ∧ ¬A) ∨ (A ∧ C) ∨ (B ∧ ¬A) ∨ (B ∧ C)  ( Distributive Law)
 

 
= False ∨ (A ∧ C) ∨ (¬A ∧ B) ∨ (B ∧ C)  (Complement Law (A ∧ ¬A ≡ False)
 

 
= (A ∧ C) ∨ (¬A ∧ B) ∨ (B ∧ C) (Identity Law (False ∨ X ≡ X))
 
**Now AND this whole thing with the third bracket (¬B ∨ C):**

 
[(A∧C) ∨ (¬A∧B) ∨ (B∧C)] ∧ (¬B∨C)
= (A∧C∧¬B) ∨ (A∧C∧C) ∨ (¬A∧B∧¬B) ∨ (¬A∧B∧C) ∨ (B∧C∧¬B) ∨ (B∧C∧C) (Distributive Law)
 

 
= (A∧C∧¬B) ∨ (A∧C) ∨ (¬A∧B∧¬B) ∨ (¬A∧B∧C) ∨ (B∧C∧¬B) ∨ (B∧C) ( Idempotent Law)
 

 
= (A∧C∧¬B) ∨ (A∧C) ∨ False ∨ (¬A∧B∧C) ∨ False ∨ (B∧C)  (Complement Law)
 

 
= (A∧¬B∧C) ∨ (A∧C) ∨ (¬A∧B∧C) ∨ (B∧C) (Identity Law)
 

 
(A∧C) ∨ (A∧¬B∧C) = A∧C (Absorption Law)
 

 
(B∧C) ∨ (¬A∧B∧C) = B∧C  (Absorption Law)
 
 we are left with:
 
= (A∧C) ∨ (B∧C)
 

 
= C ∧ (A ∨ B) (Distributive Law)
 

 
= (A ∨ B) ∧ C = RHS (Commutative Law)
 
---



**4.** 

(A ∨ B) ∧ (A ∨ ¬B)



= A ∨ (B ∧ ¬B)  (Distributive Law )



= A ∨ False   (Complement Law )



= A  (Identity Law (A ∨ False ≡ A))

So the first two brackets together collapse to just A. Now bring in the third bracket:

A ∧ (¬A ∨ B)



= (A ∧ ¬A) ∨ (A ∧ B)  (Distributive Law)



= False ∨ (A ∧ B)  (Complement Law (A ∧ ¬A ≡ False))



= A ∧ B = RHS  (Identity Law)








**5.**

$$\neg(p\to q) \equiv \neg(\neg p \lor q) \equiv \neg\neg p \land \neg q \equiv p \land \neg q$$

*(Law 7 → De Morgan's → Double Negation)*


**6.** $p \leftrightarrow q \equiv (p\to q)\land(q\to p)$ — definition of biconditional


**7.**

$$(p\to q)\land(p\to r) \equiv (\neg p \lor q)\land(\neg p \lor r) \equiv \neg p \lor (q\land r) \equiv p\to(q\land r)$$

*(Law 7 → Distributive → Law 7)*


**8.**

$$(p\to r)\land(q\to r) \equiv (\neg p\lor r)\land(\neg q \lor r) \equiv (\neg p \land \neg q)\lor r \equiv \neg(p\lor q)\lor r \equiv (p\lor q)\to r$$


**9.**

$$\neg(p\leftrightarrow q) \equiv (p\land\neg q)\lor(q\land\neg p)$$

$$p \leftrightarrow \neg q \equiv (\neg p \lor \neg q)\land(p\lor q) \equiv (p\land\neg q)\lor(\neg p \land q)$$

Both sides equal — **Equivalent**


**10.**

$$p \lor \neg(p\land q) \equiv p\lor(\neg p \lor \neg q) \equiv (p\lor\neg p)\lor \neg q \equiv T \lor \neg q \equiv T$$


**11.**

$$p \land \neg(p\lor q) \equiv p\land(\neg p\land\neg q) \equiv (p\land\neg p)\land\neg q \equiv F\land\neg q \equiv F$$


**12.**

$$(p\lor q)\land(\neg p\lor q) \equiv q \lor (p\land\neg p) \equiv q\lor F \equiv q$$


**13.**

$$(p\land q)\lor(p\land\neg q) \equiv p\land(q\lor\neg q) \equiv p\land T \equiv p$$


**14.**

$$p\lor(\neg p\land q) \equiv (p\lor\neg p)\land(p\lor q) \equiv T\land(p\lor q) \equiv p\lor q$$


**15.**

$$\neg p\to(q\to p) \equiv p \lor(\neg q\lor p) \equiv p\lor\neg q$$


**16.**

$$(p\to q)\to r \equiv \neg(p\to q)\lor r \equiv (p\land\neg q)\lor r$$

$$(\neg p\lor q)\to r \equiv \neg(\neg p\lor q)\lor r \equiv (p\land\neg q)\lor r$$

Both sides equal — **Equivalent**


**17.**

$$[(p\lor q)\land\neg p] \equiv (p\land\neg p)\lor(q\land\neg p) \equiv q\land\neg p$$

$$(q\land\neg p)\to q \equiv \neg(q\land\neg p)\lor q \equiv (\neg q\lor p)\lor q \equiv T\lor p \equiv T \quad \textbf{(Tautology ✓)}$$


---


## Section B: Boolean Algebra Simplifications


| # | Expression | Simplified Result |

|---|---|---|

| 1 | $A + AB$ | $A$ |

| 2 | $A(A+B)$ | $A$ |

| 3 | $A + A'B$ | $A + B$ |

| 4 | $A(A'+B)$ | $AB$ |

| 5 | $(A+B)(A+B')$ | $A$ |

| 6 | $AB + AB' + A'B$ | $A + B$ |

| 7 | $(A+B)' + A'B$ | $A'$ |

| 8 | $AB + A'C + BC$ | $AB + A'C$ |

| 9 | $(A+B)(A+C)(B+C)$ | $AB + AC + BC$ |

| 10 | $A'B'C + A'BC + AB'C$ | $A'C + B'C$ |


**Key steps for tricky ones:**

- **#7:** $(A+B)' + A'B = A'B' + A'B = A'(B'+B) = A'$

- **#8:** $BC$ is the *consensus term* of $AB$ and $A'C$ — it's redundant and drops out.

- **#10:** $A'C(B'+B) + AB'C = A'C + AB'C = C(A' + AB') = C(A'+B')$


---


## Section C: Truth Table → Statement


**1.** Output: T, F, F, T → **$p \leftrightarrow q$**

(True exactly when $p$ and $q$ match)


**2.** Output: T, T, F, T → **$q \to p$**

(False only when $p=F, q=T$)


**3.** Output: F, T, T, F → **$p \oplus q$** (i.e. $\neg(p\leftrightarrow q)$, or $(p\land\neg q)\lor(\neg p\land q)$)

(True exactly when $p,q$ differ — exclusive OR)


**4.** Output: F, F, F, T → **$\neg p \land \neg q$** (equivalently $\neg(p\lor q)$, the NOR)

(True only when both are false)


**5.** Output: T,T,T,F,T,F,F,F (for TTT, TTF, TFT, TFF, FTT, FTF, FFT, FFF) → **$(p\land q)\lor(p\land r)\lor(q\land r)$**

(This is the **majority function** — true when at least two of $p, q, r$ are true. Verify e.g. at $TFF$: only $p$ true → majority false ✓; at $FTT$: $q,r$ true → majority true ✓.)
