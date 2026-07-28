---
layout: single
title: "Proof Techniques"
date: 2026-07-21
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
# How Do We *Prove* Something Is True?

## Setting the Scene

Up to now, you've built a toolbox — statements, connectives, quantifiers, logical equivalence. Time to actually use it.

From here on, we ask one question, over and over: **given a mathematical statement that is true, how do we *show* that it's true?**

This is genuinely different from what "proof" meant in school. In school, "prove" often meant "manipulate the algebra until you reach the given answer." Here, "prove" means: start from what's known, and reason forward, step by step, using only logically valid moves, until you reach the claim — with every step defensible if someone challenges it.

## Some Vocabulary You'll See Constantly

Mathematicians have a small set of words for "a true statement," and the choice of word signals something about the statement's role, not its truth. None of these words means "more true" than another — a statement is either true or it isn't. They differ in *why we're stating it*.

- **Axiom** — a starting statement we simply *agree* to accept, without proof. It's the foundation everything else is built on. Example: Euclid's parallel postulate — through a point not on a line, there is exactly one line parallel to it. We don't prove axioms; we choose them as our starting rules of the game.
- **Theorem** — a true statement that has been proved, and is significant enough that we'll lean on it later to prove other things. Not every true fact earns this label — "2 + 3 = 5" is true, but nobody calls it a theorem.
- **Proposition / Result / Observation / Fact** — other names for a true, provable statement, chosen based on how important or how difficult it is. In this course we'll mostly say "Result," because most of what we prove here exists to *illustrate a technique*, not to become a famous fact you'll cite for the rest of your career.
- **Lemma** — a "helper" result. It isn't interesting on its own; its whole purpose is to make the proof of some *other*, more important result possible. (Fun fact: the German word is *hilfsatz*, literally "helping theorem.")
- **Corollary** — a result that falls out almost for free once some earlier result is already proved.

Nearly every result you'll meet in this course is phrased as an implication: *if [some condition], then [some conclusion]*. So before we can prove anything, we need to understand exactly what we're being asked to establish about that implication.

---

## Reading an Implication Correctly

Most results look like this:

> Let $x \in S$. If $P(x)$, then $Q(x)$.

or equivalently

> For all $x \in S$, if $P(x)$, then $Q(x)$.

Both are just informal ways of writing the quantified statement $\forall x \in S,\ P(x) \Rightarrow Q(x)$.

Here's the part that trips people up: **this statement isn't really about one specific $x$.** It's a claim about *every single* $x$ in the domain $S$ at once. It's true only if $P(x) \Rightarrow Q(x)$ holds for *every* $x \in S$ — and false if there's even *one* $x \in S$ where it fails.

Recall the implication's truth table:

| $P(x)$ | $Q(x)$ | $P(x) \Rightarrow Q(x)$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

Look closely at this table, and two shortcuts jump out — cases where you don't even need to check both $P(x)$ and $Q(x)$ properly, because the outcome is guaranteed no matter what.

### Trivial Proof: When $Q(x)$ Is Just Always True

Look at the table again: whenever $Q(x)$ is true, the whole row reads T — regardless of what $P(x)$ is. So if you can show $Q(x)$ is true for *every* $x$ in the domain, without even touching $P(x)$, you're done. This is called a **trivial proof**, and no, "trivial" isn't an insult here — it's a technical term for "the conclusion holds unconditionally, so the hypothesis was never needed."

**Example.** *Let $x \in \mathbb{R}$. If $x < 0$, then $x^2 + 1 > 0$.*

We never actually need $x < 0$ here. For **any** real $x$, $x^2 \geq 0$, so $x^2 + 1 \geq 1 > 0$. Done — $Q(x)$ was true all along, for every real number, hypothesis or no hypothesis.

### Vacuous Proof: When $P(x)$ Is Just Always False

Now look at the F rows in the hypothesis column: whenever $P(x)$ is false, the whole implication is true, no matter what $Q(x)$ says. So if you can show $P(x)$ is *never* true on the domain, the implication is true automatically — for the slightly uncomfortable reason that the "if" part never even gets triggered. This is a **vacuous proof**.

**Example.** *Let $n \in \mathbb{Z}$. If $n^3 > 0$ and $3$ is even, then [anything at all].* Since $3$ is never even, the hypothesis can never be true, so the implication holds vacuously — there's simply nothing to check.

These two tricks are rare — most results genuinely need both $P(x)$ and $Q(x)$ to interact. But they're worth spotting, because when they apply, they save you all the real work.

---

## Direct Proof — the Workhorse

This is the technique you will use more than any other, by a wide margin. The idea is almost embarrassingly simple once it's said out loud:

> To prove $\forall x \in S,\ P(x) \Rightarrow Q(x)$: pick an **arbitrary** $x \in S$, **assume** $P(x)$ is true for that $x$, and **show** $Q(x)$ must also be true for that same $x$.

Why is this enough to cover *every* $x \in S$, when we only checked one? Because we never used anything special about the $x$ we picked — no particular value, no extra property beyond "it's in $S$ and $P(x)$ holds." Since the argument works for a completely generic, unspecified element, it works for literally every element that satisfies $P$. This is the single most important idea to internalize about direct proofs: **"arbitrary" is doing all the work.**

There's also a small logical shortcut hiding here. Go back to the truth table: whenever $P(x)$ is false, the implication is automatically true (we just saw this with vacuous proofs). So a direct proof only needs to worry about the case where $P(x)$ is true — that's the *only* case where the implication could possibly fail, so that's the only case we need to check by hand.

### Before the Example: Two Definitions We'll Lean On Constantly

We'll use even and odd integers to illustrate proof techniques for a while, so let's nail down precise definitions — because in this course, "even" isn't a vague idea, it's a specific, checkable condition.

- An integer $n$ is **even** if $n = 2k$ for some integer $k$.
- An integer $n$ is **odd** if $n = 2k + 1$ for some integer $k$.

Notice we *defined* odd this way rather than as "not even" — technically equivalent, but far more useful, because it hands you a concrete algebraic form ($2k+1$) to compute with.

We'll also freely use three facts about integers, without re-proving them each time:

1. The negative of an integer is an integer.
2. The sum (or difference) of two integers is an integer.
3. The product of two integers is an integer.

But — and this is important — properties of *even and odd* integers specifically are **not** free. "The sum of two even integers is even" sounds obvious, but until it's proved from the definition above, we're not allowed to use it.

### Worked Example

> **Result.** If $n$ is an odd integer, then $3n + 7$ is an even integer.

**Proof.** Assume $n$ is an odd integer. Since $n$ is odd, we can write $n = 2k + 1$ for some integer $k$. Then
$$3n + 7 = 3(2k+1) + 7 = 6k + 3 + 7 = 6k + 10 = 2(3k+5).$$
Since $3k + 5$ is an integer (product and sum of integers), $3n + 7$ is even by definition. $\blacksquare$

**What just happened, in plain terms:**

- We didn't pick a *specific* odd number like $n = 7$. We let $n$ stand for *any* odd integer at all, which is why the proof covers all of them at once.
- We used the *definition* of odd — writing $n$ as $2k+1$ — rather than any vague description. This is non-negotiable: to use "$n$ is odd" in a calculation, you must convert it to its defining algebraic form.
- The whole goal was to force the final expression into the shape "$2 \times (\text{some integer})$", because that's exactly what the definition of *even* demands. Once you see $6k+10$, spotting that it factors as $2(3k+5)$ is really just working backward from what you needed to show.

**One phrasing detail worth noticing:** the proof says *"Since $n$ is odd, we can write..."* — not *"if $n$ is odd."* We already assumed $n$ is odd in the first line; by the second line it's an established fact for this proof, not a hypothesis still up in the air. Small wording, but it reflects a real distinction in what you currently know versus what you're still assuming.

---

## Proof by Contrapositive

Sometimes a direct proof forces you into a mess. Here's the escape hatch.

For statements $P$ and $Q$, the **contrapositive** of $P \Rightarrow Q$ is $(\sim Q) \Rightarrow (\sim P)$. The critical fact — and it's worth checking on a truth table until it feels obvious — is that **an implication and its contrapositive are logically equivalent**:
$$P \Rightarrow Q \;\equiv\; (\sim Q) \Rightarrow (\sim P).$$

| $P$ | $Q$ | $P\Rightarrow Q$ | $\sim Q$ | $\sim P$ | $(\sim Q)\Rightarrow(\sim P)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | T |
| T | F | F | T | F | F |
| F | T | T | F | T | T |
| F | F | T | T | T | T |

The last two columns match on every row — so proving one is exactly as good as proving the other. This means: **to prove $P(x) \Rightarrow Q(x)$ for all $x \in S$, it is completely legitimate to instead assume $\sim Q(x)$ and prove $\sim P(x)$.** You're not cutting a corner — you're proving a *different but equivalent* statement, and equivalence means the truth of one guarantees the truth of the other.

### Why Bother? A Case Where Direct Proof Genuinely Struggles

> **Result.** Let $x \in \mathbb{Z}$. If $5x - 7$ is even, then $x$ is odd.

Try a direct proof first, just to feel the pain: assume $5x - 7$ is even, so $5x - 7 = 2a$ for some integer $a$. Solving for $x$ gives $x = (2a+7)/5$. Now you're stuck — it isn't even obvious from this expression that $x$ is an integer, let alone odd, even though we already know $x$ *is* an integer because the problem told us so. The algebra fights you.

Now try the contrapositive. We want $(\sim Q(x)) \Rightarrow (\sim P(x))$: *if $x$ is even, then $5x-7$ is odd.*

**Proof.** Assume $x$ is even. Then $x = 2a$ for some integer $a$. So
$$5x - 7 = 5(2a) - 7 = 10a - 7 = 10a - 8 + 1 = 2(5a-4) + 1.$$
Since $5a - 4$ is an integer, $5x - 7$ is odd. $\blacksquare$

Night and day. Substituting $x = 2a$ into $5x - 7$ is trivial algebra; substituting a messy expression for $x$ was not.

**How do you know in advance which technique to reach for?** A useful rule of thumb: ask which starting assumption gives you something *simpler* to substitute. A direct proof of this result would force you to start from "$5x - 7$ is even" — a clunky expression. The contrapositive instead lets you start from "$x$ is even" — clean and immediately usable. When the *conclusion's negation* is simpler to work with than the *hypothesis itself*, that's your signal to try the contrapositive.

---

## Proof by Cases

Sometimes an element $x$ doesn't hand you one clean algebraic form to substitute — but it does fall into one of a small number of categories, and each category is easy to handle on its own. **Proof by cases** means: split the domain into pieces that cover every possibility, and prove the result separately within each piece.

Common ways to split (you'll see these constantly):

- $n$ even, or $n$ odd (covers all integers)
- $x = 0$, or $x < 0$, or $x > 0$ (covers all reals)
- $n = 1$, or $n \geq 2$ (covers all positive integers)

The only rule: your cases must genuinely cover the *entire* domain between them, with no element slipping through the gaps.

### Worked Example

> **Result.** If $n \in \mathbb{Z}$, then $n^2 + 3n + 5$ is an odd integer.

Here, there's no single algebraic substitution that handles all integers at once — but "even or odd" splits $\mathbb{Z}$ completely, and each half is easy.

**Proof.** We proceed by cases.

**Case 1: $n$ is even.** Then $n = 2x$ for some integer $x$. So
$$n^2+3n+5 = (2x)^2 + 3(2x) + 5 = 4x^2+6x+5 = 2(2x^2+3x+2)+1.$$
Since $2x^2+3x+2$ is an integer, $n^2+3n+5$ is odd.

**Case 2: $n$ is odd.** Then $n = 2y+1$ for some integer $y$. So
$$n^2+3n+5 = (2y+1)^2+3(2y+1)+5 = 4y^2+10y+9 = 2(2y^2+5y+4)+1.$$
Since $2y^2+5y+4$ is an integer, $n^2+3n+5$ is odd. $\blacksquare$

Since every integer is either even or odd, and the result holds in both cases, it holds for every integer.

**A related idea you'll see by name:** two integers $x, y$ are of the **same parity** if both are even or both are odd, and of **opposite parity** if one is even and the other odd. Any result phrased in terms of "same parity" or "opposite parity" is basically begging for a proof by cases, since the definition itself is a two-way split.

---

## Disproving a Statement: Counterexamples

Not every quantified claim you're handed will be true — and showing a claim is *false* uses a completely different (and much shorter) strategy than proving it true.

Recall: $\sim(\forall x \in S,\ R(x)) \equiv \exists x \in S,\ \sim R(x)$. In words: if "$R(x)$ holds for all $x$" is false, that's exactly the same as saying "some $x$ makes $R(x)$ false." Such an $x$ is called a **counterexample**.

This matters because it tells you the proof burden is completely asymmetric:

- To prove $\forall x \in S,\ R(x)$, you must handle *every* $x$ — one exception ruins it.
- To disprove it, you only need *one* $x$ that fails. A single counterexample is a complete, valid proof of falsehood — nothing more is required.

**Example.** Consider the claim: *for every real $x$, $(x^2-1)^2 > 0$.*

Try $x = 1$: $(1^2-1)^2 = 0^2 = 0$, which is *not* greater than $0$. So $x=1$ is a counterexample, and the claim is false. ($x = -1$ also works, and these turn out to be the *only* two counterexamples — meaning the modified claim "for every real $x \neq \pm 1$, $(x^2-1)^2 > 0$" is actually true.)

---

## Proof by Contradiction

This technique doesn't care whether your statement is phrased as an implication at all — it works on any statement $R$ you're trying to establish.

The idea: **assume $R$ is false, and show that this assumption forces something impossible** — a statement $C$ that is both true and false at once ($C: P \land (\sim P)$ for some fact $P$ you already know). Once you've derived an impossibility from "$R$ is false," that assumption itself must have been the problem — so $R$ has to be true after all.

If $R$ happens to be the implication $\forall x \in S,\ P(x) \Rightarrow Q(x)$, here's the useful part: negating it gives
$$\sim(\forall x \in S,\ P(x)\Rightarrow Q(x)) \;\equiv\; \exists x \in S,\ (P(x) \land \sim Q(x)).$$

So a proof by contradiction of an implication always starts the same way: **assume there exists some $x \in S$ for which $P(x)$ is true and $Q(x)$ is false — i.e., assume a counterexample exists — and derive an impossibility from that assumption.** You'll often see proofs literally open with the phrase *"Assume, to the contrary, that..."* — that phrase is your cue that a contradiction is coming.

### A Clean, Classic Example

> **Result.** There is no smallest positive real number.

This isn't an implication, so direct proof and contrapositive don't naturally apply here — but contradiction handles it easily.

**Proof.** Assume, to the contrary, that there *is* a smallest positive real number; call it $r$. Since $0 < r/2 < r$, the number $r/2$ is a positive real number smaller than $r$. But we assumed $r$ was the *smallest* positive real number — contradiction. $\blacksquare$

The trick, as always with contradiction, is to name the thing you're assuming exists (here, $r$), and then hunt for something that breaks the very property that made it special.

---

## Comparing All Three Techniques on the Same Result

It's worth seeing direct proof, contrapositive, and contradiction attack the *same* claim side by side, so the differences stop being abstract.

> **Result.** If $n$ is an even integer, then $3n + 7$ is odd.

**Direct proof.** Let $n$ be even, so $n = 2x$ for some integer $x$. Then
$$3n+7 = 3(2x)+7 = 6x+7 = 2(3x+3)+1.$$
Since $3x+3$ is an integer, $3n+7$ is odd. $\blacksquare$

**Contrapositive.** Assume $3n+7$ is even, so $3n+7 = 2y$ for some integer $y$. Then
$$n = (3n+7) + (-2n-7) = 2y - 2n - 7 = 2(y-n-4)+1.$$
Since $y - n - 4$ is an integer, $n$ is odd. $\blacksquare$

**Contradiction.** Assume, to the contrary, that there's an even integer $n$ with $3n+7$ *also* even. Since $n$ is even, $n = 2x$, so $3n+7 = 6x+7 = 2(3x+3)+1$, which is odd — contradicting our assumption that it's even. $\blacksquare$

All three are valid. But look at how different the *effort* is: the direct proof is one clean substitution; the contrapositive requires an awkward algebraic rearrangement of $n$ in terms of $y$; the contradiction proof basically repeats the direct proof's calculation and then adds a contradiction at the end. **When a direct proof is available and clean, most mathematicians reach for it first** — it's usually the easiest to both write and read. But this is a guideline, not a rule; sometimes, as with $5x-7$ earlier, direct proof is the one that fights back.

### A Trickier Comparison: Inequalities

> **Result.** Let $x$ be a nonzero real number. If $x + \dfrac{1}{x} < 2$, then $x < 0$.

**Direct proof.** Assume $x + \frac{1}{x} < 2$. Since $x \neq 0$, $x^2 > 0$. Multiply both sides by $x^2$:
$$x^2\left(x+\frac{1}{x}\right) < 2x^2 \implies x^3 + x - 2x^2 < 0 \implies x(x-1)^2 < 0.$$
Since $(x-1)^2 \geq 0$ always, and the product $x(x-1)^2$ is strictly negative, $(x-1)^2$ can't be $0$ here — so $(x-1)^2 > 0$ strictly. A negative number divided by a positive number is negative, so $x < 0$. $\blacksquare$

**Contrapositive.** We instead prove: if $x \geq 0$, then $x + \frac{1}{x} \geq 2$.

*Strategy first:* working backward from the target inequality $x + \frac1x \ge 2$, multiplying through by $x$ gives $x^2+1 \ge 2x$, i.e. $(x-1)^2 \ge 0$ — which we already know is always true. Reversing that chain of steps gives the proof:

**Proof.** Assume $x \geq 0$; since $x \neq 0$, $x > 0$. We know $(x-1)^2 \geq 0$, i.e., $x^2 - 2x + 1 \geq 0$, i.e., $x^2+1 \geq 2x$. Dividing both sides by the positive number $x$ gives $x + \frac{1}{x} \geq 2$, as desired. $\blacksquare$

**Contradiction.** Assume, to the contrary, that there's a nonzero real $x$ with $x + \frac1x < 2$ *and* $x \geq 0$. Since $x \ne 0$, $x > 0$. Multiplying $x+\frac1x<2$ by $x$ gives $x^2+1 < 2x$, i.e. $(x-1)^2 < 0$ — impossible, since a square can never be negative. Contradiction. $\blacksquare$

Notice the contrapositive proof here is noticeably *cleaner* than the direct one — the direct proof has to fight to justify that $(x-1)^2$ is strictly positive rather than just non-negative, while the contrapositive sidesteps that entirely. This is exactly the kind of situation — inequalities where the conclusion's negation gives you a friendlier starting point — where contrapositive tends to shine.

### A Cheat Sheet: What to Assume, and What Counts as a Mistake

When you're proving $\forall x \in S,\ P(x) \Rightarrow Q(x)$, here's what's valid to assume at the *start* of a proof, and what silently breaks the logic:

| You start by assuming... | What this means |
|---|---|
| $P(x)$ true, for arbitrary $x$ | ✅ Direct proof. Goal: show $Q(x)$ true. |
| $\sim Q(x)$ true, for arbitrary $x$ | ✅ Proof by contrapositive. Goal: show $\sim P(x)$ true. |
| There exists $x$ with $P(x)$ true and $Q(x)$ false | ✅ Proof by contradiction. Goal: derive an impossibility. |
| $P(x)$ false, for arbitrary $x$ | ❌ Mistake — this proves nothing about the implication. |
| $Q(x)$ false, for arbitrary $x$ | ❌ Mistake. |
| $P(x)$ and $Q(x)$ both false, for arbitrary $x$, or various other "there exists" combinations mixing true/false | ❌ Mistake, except the one contradiction-style opening above. |

The pattern to notice: a valid proof either (a) fixes an *arbitrary* element and assumes something about $P$ or $\sim Q$ specifically — never $\sim P$ or $Q$ alone — or (b) assumes the *existence* of a counterexample, for contradiction. Every other opening move quietly assumes something that doesn't actually pin down the truth of the implication.

---

## Mathematical Induction

All four techniques so far — direct, contrapositive, cases, contradiction — can, in principle, be used to prove a statement about *every* element of a set. But for one particular kind of domain — the positive integers — there's a technique tailor-made for the job, because of how that set is built: $1, 2, 3, \ldots$, each one obtained from the last by adding $1$.

### The Idea, Before the Formal Statement

Imagine an infinite line of dominoes. If you can guarantee two things — (1) the first domino falls, and (2) *whenever* any domino falls, it knocks over the next one — then you know, without checking each one individually, that *every* domino eventually falls. That's induction, in one picture.

### The Formal Principle

**Principle of Mathematical Induction.** For each positive integer $n$, let $P(n)$ be a statement. If

1. $P(1)$ is true, and
2. for every positive integer $k$, the implication "if $P(k)$, then $P(k+1)$" is true,

then $P(n)$ is true for every positive integer $n$.

Step (1) is called the **base case** — checking the first domino falls. Step (2) is called the **inductive step** — checking that each domino, if it falls, knocks over the next one. Crucially, in step (2) you are *not* claiming $P(k)$ is actually true for every $k$ — that would be assuming the very thing you're trying to prove. You're only claiming the *implication* $P(k) \Rightarrow P(k+1)$ holds, for an arbitrary fixed $k$. This is itself just... a direct proof, nested inside an induction argument.

*(Where does this principle itself come from? It follows from a deeper fact called the* **Well-Ordering Principle** *— that every nonempty subset of the positive integers has a smallest element. That's a separate discussion; for now, treat induction as a tool you're licensed to use.)*

### Worked Example: The Sum of the First $n$ Positive Integers

> **Result.** For every positive integer $n$,
> $$1+2+3+\cdots+n = \frac{n(n+1)}{2}.$$

**Proof.** We use induction.

**Base case ($n=1$):** $1 = \frac{1 \cdot 2}{2}$, so the statement holds for $n=1$.

**Inductive step:** Assume, for some positive integer $k$, that
$$1+2+3+\cdots+k = \frac{k(k+1)}{2}.$$
(This assumption is called the **inductive hypothesis**.) We must show the statement also holds for $k+1$, i.e., that $1+2+\cdots+(k+1) = \frac{(k+1)(k+2)}{2}$.

$$1+2+\cdots+(k+1) = \underbrace{(1+2+\cdots+k)}_{\text{use the inductive hypothesis here}} + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1)+2(k+1)}{2} = \frac{(k+1)(k+2)}{2}.$$

By the Principle of Mathematical Induction, the formula holds for every positive integer $n$. $\blacksquare$

**A word of warning that trips up almost everyone the first time:** in the inductive step, we assumed the formula holds *for the one specific value $k$*, not for every positive integer up to $k$, and certainly not for all $n$. Writing "assume the formula is true for all positive integers $k$" would be circular — you'd be assuming the very conclusion you're trying to reach. The inductive hypothesis is a single, local assumption: *if* it's true at $k$, *then* it's true at $k+1$ — and the base case is what gets this chain started.

### Where This Formula Actually Comes From — Gauss's Trick

The induction proof above is completely rigorous, but it doesn't really explain *why* the formula is $\frac{n(n+1)}{2}$ — it just confirms it. There's a famous, much more intuitive derivation, often attributed to a young Carl Friedrich Gauss.

Let $S = 1+2+3+\cdots+n$. Write the same sum backward:
$$S = n+(n-1)+(n-2)+\cdots+1.$$
Now add the two versions of $S$ term by term:
$$2S = (n+1)+(n+1)+(n+1)+\cdots+(n+1) \quad (n \text{ copies, one per term}).$$
So $2S = n(n+1)$, giving $S = \frac{n(n+1)}{2}$ — the same formula, reached by a clever trick rather than by induction.

**Why show you both?** Induction is a completely general machine — it will grind through *any* claim about positive integers, whether or not a clever shortcut exists. Gauss's trick is elegant but specific to this one sum; it doesn't generalize to arbitrary claims. In this course, you'll mostly rely on induction precisely *because* it's the general-purpose tool, even when — as here — a shorter, cleverer argument happens to exist for a particular case.

---

## Putting It All Together

You now have five genuinely different strategies for proving $\forall x \in S,\ P(x) \Rightarrow Q(x)$ (plus induction, for when $S$ is specifically the positive integers), and one strategy for disproving it:

- **Trivial / vacuous proof** — for the rare cases where the truth table already guarantees the answer without real work.
- **Direct proof** — assume $P(x)$, derive $Q(x)$. Try this first.
- **Proof by contrapositive** — assume $\sim Q(x)$, derive $\sim P(x)$. Reach for this when the *negated conclusion* is easier to compute with than the original hypothesis.
- **Proof by cases** — split the domain into pieces that cover everything, and handle each piece separately.
- **Proof by contradiction** — assume a counterexample exists, and derive something impossible.
- **Mathematical induction** — for claims about all positive integers: check the base case, then show each case implies the next.
- **Counterexample** — to *disprove* a universal claim, one failing instance is a complete proof.

None of these is "the right one" in general — picking a technique is itself part of the mathematical skill you're building, and often the fastest way to find out which one fits is simply to *start* a direct proof and see whether the algebra cooperates.

