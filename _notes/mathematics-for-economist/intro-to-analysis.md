---
layout: single
title: "Intro to Analysis"
date: 2026-08-03
subject: "Mathematics for Economists"
toc: true
wide: true
order: 11
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

# Before we start
You already know sets, relations, and functions at a basic level, plus a bit of logic
(∀, ∃, ¬, ∧, ∨). That's all we need. Everything specific to analysis will be built up
from scratch, starting here.

A quick recap of one idea we'll reuse a lot: a **relation** on a set $S$ is just a rule
that lets you compare pairs of elements of $S$ — it tells you, for a given pair
$(x, y)$, whether the relation holds between them or not. "$<$" on $\mathbb{Q}$ or
$\mathbb{R}$ is the most familiar example, but as you'll see below, "order" is defined
abstractly, so it can apply to sets that don't look like numbers at all

---

# Ordered Sets



.



## 1. Definition — Order

> **Definition.** Let $S$ be a set. An **order** on $S$ is a relation, denoted by $<$,
> with the following two properties:
>
> **(i)** If $x \in S$ and $y \in S$, then **one and only one** of the statements
> $$x < y, \qquad x = y, \qquad y < x$$
> is true. *(This is called the law of trichotomy or completeness, used in Microeconomics)*
>
> **(ii)** If $x, y, z \in S$, and $x < y$ and $y < z$, then $x < z$.
> *(This is called transitivity.)*

"$x < y$" can be read as "$x$ is less than $y$", "$x$ is smaller than
$y$", or "$x$ precedes $y$", the last phrasing matters because an order need not be
about size at all; it could be about which element "comes first". Ordering just means you are able to rank the elements in the set, and that is why we need to define relation between two elements.

Ordering just means being able to rank the elements of a set, and that's why we need to define a relation between any two elements.

For example, a set 
S
S can be defined as: 
S={Abhijeet, Anshu, Raghav, Nandu}
S={Abhijeet, Anshu, Raghav, Nandu}. We could define a relation 
R
R such that the person who appears first in a dictionary (alphabetical) list is ranked first, and this way, we're able to rank the elements of the set.


Condition (i) guarantees that *any* two elements can be
compared — nothing is left undecided, and you never get two of the three holding
simultaneously. Condition (ii) guarantees the order behaves consistently, it rules
out "cycles" like $x < y < z < x$.

---

## 2. Definition - Ordered Set

> **Definition.** An **ordered set** is a set $S$ in which an order is defined.

An ordered set is just a set where you've picked a rule (like "smaller than" or "comes before") that lets you compare any two elements and say which one ranks first. Without that rule, the elements are just a pile of items with no way to say which comes first and whihc comes later.


**Example.** $\mathbb{Q}$ (the rationals) is an ordered set, where $r < s$ is defined
to mean:
$$s - r \text{ is a positive rational number.}$$

Check for yourself that this satisfies both conditions of Definition of ordered set — for any two
rationals $r, s$, exactly one of $s - r > 0$, $s - r = 0$, $s - r < 0$ holds, and if
$s - r > 0$ and $t - s > 0$ then $t - r = (t-s) + (s-r) > 0$.

**Example.** Suppose $S$ is the set of ice-cream flavors you like, and you define a relation $<$ where $a < b$ means "you prefer $b$ over $a$."

This is an order as long as your preferences satisfy the same two conditions:

- **Trichotomy:** for any two flavors $a, b \in S$, exactly one of "$a$ preferred over $b$", "$b$ preferred over $a$", or "$a = b$" holds — you can't be genuinely indifferent between two *different* flavors, and you can't prefer both ways at once.
- **Transitivity:** if you prefer $b$ over $a$, and $c$ over $b$, then you must prefer $c$ over $a$ too — no "I like chocolate more than vanilla, vanilla more than mango, but mango more than chocolate" cycles allowed.

If your preferences genuinely behave this way, they define an order on $S$ — you can now line up every flavor from least to most preferred, just like $\mathbb{Q}$ can be lined up using $<$.

Let $$S = \{\text{Vanilla, Chocolate, Mango, Strawberry, Butterscotch, Pistachio, Coffee, Mint}\}$$

Suppose your personal preferences rank them like this, from least to most liked:

$$\text{Mint} < \text{Coffee} < \text{Pistachio} < \text{Butterscotch} < \text{Strawberry} < \text{Mango} < \text{Vanilla} < \text{Chocolate}$$

(read $a < b$ as "you like $a$ less than $b$")

Let's check this really is an order on $S$:

- **Trichotomy:** Take any two flavors, say Mango and Pistachio. Exactly one of these is true: you like Mango less than Pistachio, you like them equally, or you like Pistachio less than Mango. According to the ranking above, Pistachio $<$ Mango — and that's the *only* one of the three that holds. This works for every pair in the list.

- **Transitivity:** Say Pistachio $<$ Strawberry and Strawberry $<$ Mango. Transitivity says this forces Pistachio $<$ Mango — and indeed, that's consistent with the ranking above. As long as your taste doesn't loop back on itself (liking Mint more than Chocolate somewhere down the line, say), transitivity holds for the whole set.

Because both conditions hold, this preference relation $<$ is a genuine order on $S$, and $(S, <)$ is an ordered set — you've successfully lined up all 8 flavors from least to most preferred.

---

## 3. Definition  — Bounded Above, Upper Bound

> **Definition.** Suppose $S$ is an ordered set, and $E \subset S$. If there exists a
> $\beta \in S$ such that
> $$x \le \beta \quad \text{for every } x \in E,$$
> we say that $E$ is **bounded above**, and call $\beta$ an **upper bound** of $E$.

Key things to notice:

- $\beta$ does **not** need to belong to $E$.
- If one upper bound exists, then **infinitely many** do — anything bigger than an
  upper bound is also an upper bound.
- "Bounded above" is a property of the *set* $E$; "upper bound" is a property of a
  specific candidate element $\beta$.

### Example

Let $S = \mathbb{R}$ with the usual order, and let
$$E = \{x \in \mathbb{R} : 0 < x < 1\} \quad \text{(the open interval } (0,1)\text{)}.$$

```
                 E = (0, 1)
        ─────────●═══════════●───────────●────────►
       -1        0            1           2
                              ▲           ▲
                        smallest       another
                        upper bound    upper bound
                        (β = 1)        (β = 2)
```

Here $\beta = 1$ is an upper bound: every $x \in E$ satisfies $x < 1 \le 1$. So is
$\beta = 2$, or $\beta = 100$. In fact **every** real number $\beta \ge 1$ is an upper
bound of $E$. Note $1 \notin E$, yet $1$ is still perfectly valid as an upper bound —
the definition never required $\beta \in E$.

---

## 4. Lower Bound, Bounded Below

Defined the same way, with $\ge$ in
place of $\le$:

> **Definition.** Suppose $S$ is an ordered set, and $E \subset S$. If there exists an
> $\alpha \in S$ such that
> $$x \ge \alpha \quad \text{for every } x \in E,$$
> we say that $E$ is **bounded below**, and call $\alpha$ a **lower bound** of $E$.

Everything said about upper bounds mirrors here: $\alpha$ need not be in $E$, and if
one lower bound exists, so do infinitely many (anything smaller also qualifies).

### Example

Take the same set $E = (0, 1) \subset \mathbb{R}$.

```
                 E = (0, 1)
        ─────────●═══════════●───────────●────────►
       -1        0            1           2
        ▲        ▲
   another    largest
   lower       lower bound
   bound       (α = 0)
   (α = -1)
```

Here $\alpha = 0$ is a lower bound: every $x \in E$ satisfies $x > 0 \ge 0$. So is
$\alpha = -1$, or $\alpha = -50$. Every real number $\alpha \le 0$ is a lower bound of
$E$. Again, $0 \notin E$, but that doesn't stop $0$ from being a valid lower bound.

So $E = (0,1)$ is both **bounded above** (by $1$, or anything larger) and
**bounded below** (by $0$, or anything smaller).

---

## 5. A set that is bounded only on one side

Not every set is bounded on both sides. Let
$$F = \{x \in \mathbb{R} : x > 0\} \quad \text{(all positive reals)}.$$

```
        ─────────●═══════════════════════════►
       -1        0                          (no end)
        ▲
   lower bound
   (α = 0, or any α ≤ 0)

        no upper bound exists — for ANY candidate β,
        you can always find x ∈ F with x > β (e.g. x = β + 1)
```

$F$ is bounded below (e.g. by $\alpha = 0$), but **not bounded above** — no real
number $\beta$ can satisfy $x \le \beta$ for every positive $x$, since $\beta + 1$ is
always a bigger positive number. This is the kind of set where "bounded above" fails
in a very concrete, checkable way.

---
## 7. Definition - Supremum and Infimum
 
We saw that a set $E$ can have *many* upper bounds. That immediately raises a
question: among all of them, is there always a **smallest** one? That special upper
bound (when it exists) is called the **supremum**.
 
> **Definition.** Suppose $S$ is an ordered set, $E \subset S$, and $E$ is bounded
> above. Suppose there exists $\alpha \in S$ with the following properties:
>
> **(i)** $\alpha$ is an upper bound of $E$.
>
> **(ii)** If $\gamma < \alpha$, then $\gamma$ is **not** an upper bound of $E$.
>
> Then $\alpha$ is called the **least upper bound** of $E$, or the **supremum** of
> $E$, written
> $$\alpha = \sup E.$$
 
Condition (ii) is the important new ingredient. It says: *nothing smaller than
$\alpha$ can also be an upper bound.* This is exactly what "least" means, and it's
also why there can be **at most one** such $\alpha$ — if two different numbers both
satisfied (i) and (ii), each would have to be smaller than the other, which is
impossible.
 
> The **infimum** (greatest lower bound) is defined the same way, mirrored:
> $$\alpha = \inf E$$
> means $\alpha$ is a lower bound of $E$, and no $\beta > \alpha$ is a lower bound of
> $E$.
 
### Example — $\sup$ and $\inf$ of an interval
 
Let $E = (0, 1) = \{x \in \mathbb{R} : 0 < x < 1\}$, as before.
 
```
                 E = (0, 1)
        ─────────●═══════════●───────────●────────►
       -1        0            1           2
                              ▲
                     α = sup E = 1
                     ● smallest upper bound
                     ● 1 ∉ E, but that's fine!
```
 
- $\sup E = 1$. Check: $1$ is an upper bound (every $x \in E$ has $x < 1$), and
  nothing smaller than $1$ works — for any $\gamma < 1$, you can always find some
  $x \in E$ with $\gamma < x < 1$ (just pick $x$ between $\gamma$ and $1$), so $\gamma$
  fails to be an upper bound.
- Similarly, $\inf E = 0$.
Notice: **neither $0$ nor $1$ belongs to $E$.** The supremum and infimum don't need to
be elements of the set they bound — this trips people up constantly, so it's worth
sitting with.
 
### Counterexample — why $\beta = 2$ is *not* $\sup E$
 
Take the same $E = (0,1)$. Is $\beta = 2$ a candidate for $\sup E$?
 
- Check (i): is $2$ an upper bound? Yes — every $x \in E$ has $x < 1 < 2$.
- Check (ii): is there some $\gamma < 2$ that is *still* an upper bound? Yes —
  $\gamma = 1$ works, and $1 < 2$.
So condition (ii) **fails** for $\beta = 2$: there's a smaller number ($1$) that is
still an upper bound. This is exactly why $2$ is *an* upper bound but not *the least*
upper bound. Being an upper bound is easy; being the supremum is a much stronger,
more specific claim.
 
### Counterexample — a set where $\sup$ doesn't exist (in the set you're working in)
 
This is the crucial one, and it's why analysis cares about $\mathbb{R}$ so much. Let
$$E = \{x \in \mathbb{Q} : x > 0 \text{ and } x^2 < 2\},$$
thought of as a subset of the ordered set $\mathbb{Q}$ (not $\mathbb{R}$).
 
```
        Q:  0    ...   1     1.4  1.41  1.414 ...  √2 ...   2
                       └──────── E lives here ────────┘
                                                       ▲
                                              "should be" sup E,
                                              but √2 ∉ Q !
```
 
$E$ is bounded above in $\mathbb{Q}$ — for instance $\beta = 2$ works, since any
rational with $x^2 < 2$ must have $x < 2$. But **no rational number is the least
upper bound**. Intuitively, the "true" least upper bound is $\sqrt{2}$, but
$\sqrt{2} \notin \mathbb{Q}$. Whatever rational upper bound you propose, you can
always find a smaller rational that's still an upper bound (squeezing closer to
$\sqrt{2}$ without ever reaching it) — so condition (ii) can never be satisfied by any
element of $\mathbb{Q}$.
 

 
### Example — infimum with a counterexample
 
Let $E = \{1, 1/2, 1/3, 1/4, \dots\} = \{1/n : n \in \mathbb{N}\} \subset \mathbb{R}$.
 
```
        ●───●──●─●●●●●●●●●●●●●●●●●●●●●●───────────►
        0   1/4 1/3  1/2                1
        ▲
    α = inf E = 0
    (0 ∉ E, but every term gets arbitrarily close to it)
```
 
- $\inf E = 0$: it's a lower bound (every $1/n > 0$), and no $\beta > 0$ can be a
  lower bound, because you can always find $n$ large enough that $1/n < \beta$.
- **Counterexample check:** is $\beta = -1$ a valid candidate for $\inf E$? It *is* a
  lower bound (every $1/n > -1$), but it fails condition (ii): $0 > -1$ is *also* a
  lower bound, so $-1$ isn't the *greatest* one. This is the mirror image of the
  $\beta = 2$ counterexample above.
- $\sup E = 1$ here, and this time $1 \in E$ — supremum *can* belong to the set; it
  just doesn't have to.
---
## 8. Definition  — The Least-Upper-Bound Property
 
Now we can finally name the property that was  behind the $x^2 < 2$ example.
 
> **Definition.** An ordered set $S$ is said to have the **least-upper-bound
> property** if the following is true: if $E \subset S$, $E$ is not empty, and $E$ is
> bounded above, then $\sup E$ **exists in $S$**.
 
Read this carefully — it's not just saying "some sets have a supremum." It's a
statement about the *entire ordered set $S$*: it says that **every single time** you
hand it a nonempty, bounded-above subset, a supremum is guaranteed to exist,
*and to exist inside $S$ itself* (not off in some bigger set).
 
This is a strong requirement. All it takes is **one** bad subset — one nonempty,
bounded-above $E \subset S$ whose supremum fails to exist in $S$ — to disqualify $S$
from having this property.
 
### Counterexample — $\mathbb{Q}$ does NOT have the least-upper-bound property
 
 Take
$$E = \{x \in \mathbb{Q} : x > 0 \text{ and } x^2 < 2\} \subset \mathbb{Q}.$$
 
- $E$ is not empty ($1 \in E$).
- $E$ is bounded above in $\mathbb{Q}$ (e.g. by $2$).
- But $\sup E$ does not exist in $\mathbb{Q}$ — no rational number satisfies both
  conditions of Definition 1.8, since the "natural" candidate is $\sqrt{2}$, which
  isn't rational.
This single example is enough: $\mathbb{Q}$, as an ordered set, **fails** the
least-upper-bound property. It doesn't matter that *most* bounded-above subsets of
$\mathbb{Q}$ behave nicely and do have a rational supremum (e.g. $E = \{x \in
\mathbb{Q} : x < 5\}$ has $\sup E = 5 \in \mathbb{Q}$, no problem there) — the
property demands it work for *every* such subset, with **no exceptions**, and we just
found one.
 
### Example — $\mathbb{R}$ DOES have the least-upper-bound property
 
This is one of the most important facts in the entire course, and it's really an
*assumption* (or, if you build $\mathbb{R}$ from $\mathbb{Q}$ via Dedekind cuts or
Cauchy sequences, a *theorem*) rather than something you check case by case:
 
$$\mathbb{R} \text{ has the least-upper-bound property.}$$
 
Concretely, this means: whenever $E \subset \mathbb{R}$ is nonempty and bounded above,
$\sup E$ is guaranteed to exist as a real number — no gaps, no missing suprema. In
particular, the very set that broke $\mathbb{Q}$,
$$E = \{x \in \mathbb{R} : x > 0 \text{ and } x^2 < 2\},$$
does have a supremum in $\mathbb{R}$, namely $\sqrt{2}$. $\mathbb{R}$ was built
precisely to fill in the hole that $\mathbb{Q}$ left behind.
 
### Why this matters going forward
 
The least-upper-bound property is the single defining feature that makes
$\mathbb{R}$ suitable for analysis (limits, continuity, integration — all of it
secretly leans on this). Every time you'll later see a proof that says "let $\alpha =
\sup E$" and just assumes it exists, this is the property being invoked.
 
```
   ordered set          has LUB property?
  ─────────────────────────────────────────
   Q  (rationals)              ✗   (gaps, e.g. at √2)
   R  (reals)                  ✓   (no gaps — this is the point of R)
```
 
---
## 9. Theorem
 
> **Theorem.** Suppose $S$ is an ordered set with the least-upper-bound property,
> $B \subset S$, $B$ is not empty, and $B$ is bounded below. Let $L$ be the set of all
> lower bounds of $B$. Then $\alpha = \sup L$ exists in $S$, and $\alpha = \inf B$.
 
This theorem's whole point is: **the least-upper-bound property secretly gives you a
greatest-lower-bound property for free.** You never need to separately assume $S$
has a "GLB property" — it follows automatically. The proof builds $\inf B$ entirely
out of $\sup$, by looking at the set of lower bounds instead of $B$ itself.
 
Here is every line of the proof, with the definition it's using made explicit.
 
---
 
**"Since $B$ is bounded below, $L$ is not empty."**
 
$B$ bounded below means (Def 1.7) there exists **at least one** $\alpha_0 \in S$ with
$x \ge \alpha_0$ for every $x \in B$. That $\alpha_0$ is, by definition, a lower bound
of $B$ — so $\alpha_0 \in L$. One element is enough to make $L$ nonempty.
 
*If this failed:* if $B$ weren't bounded below, $L$ could be empty, and "sup of the
empty set" isn't something Definition 1.8 lets you talk about — the whole argument
would collapse at step one.
 
---
 
**"Since $L$ consists of exactly those $y \in S$ which satisfy $y \le x$ for every
$x \in B$, we see that every $x \in B$ is an upper bound of $L$."**
 
This is the clever pivot of the whole proof — read it twice. By definition of $L$:
$$y \in L \iff y \le x \text{ for every } x \in B. \tag{$\ast$}$$
 
Now fix any *one* particular $x_0 \in B$, and look at ($\ast$) from $x_0$'s point of
view: every $y \in L$ satisfies $y \le x_0$. But "every element of a set is $\le$ some
fixed value" is *exactly* Definition 1.7's condition for that fixed value to be an
**upper bound** of the set. Here the set is $L$, and the fixed value is $x_0$. So
$x_0$ is an upper bound of $L$. Since $x_0 \in B$ was arbitrary, **every** $x \in B$ is
an upper bound of $L$.
 
---
 
**"Thus $L$ is bounded above."**
 
We just found at least one upper bound of $L$ (any $x \in B$ works, and $B \ne
\emptyset$), so by Definition 1.7, $L$ is bounded above.
 
**"Our hypothesis about $S$ implies therefore that $L$ has a supremum in $S$; call it
$\alpha$."**
 
This is exactly where Definition 1.10 (the least-upper-bound property) gets used:
$S$ has the LUB property, $L \subset S$, $L$ is not empty, $L$ is bounded above — so
the definition guarantees $\sup L$ exists in $S$. Call it $\alpha$.
 
*If this failed:* if $S$ were, say, $\mathbb{Q}$ instead of an LUB-property set, this
step could break — $L$ might be a perfectly good nonempty, bounded-above subset that
still has no supremum *in $S$*, exactly like the $x^2 < 2$ example from Section 8.
This is precisely why the hypothesis "$S$ has the least-upper-bound property" is
non-negotiable for this theorem.
 
---
 
**"If $\gamma < \alpha$ then (see Definition 1.8) $\gamma$ is not an upper bound of
$L$, hence $\gamma \notin B$."**
 
Since $\alpha = \sup L$, condition (ii) of Definition 1.8 says: nothing smaller than
$\alpha$ is an upper bound of $L$. So $\gamma < \alpha \implies \gamma$ is not an
upper bound of $L$.
 
Now recall the earlier pivot: we showed **every element of $B$ is an upper bound of
$L$.** So if $\gamma$ is *not* an upper bound of $L$, $\gamma$ cannot be an element of
$B$ (otherwise it would have to be one). Hence $\gamma \notin B$.
 
**"It follows that $\alpha \le x$ for every $x \in B$. Thus $\alpha \in L$."**
 
We've just shown: $\gamma < \alpha \implies \gamma \notin B$. Taking the contrapositive:
$x \in B \implies x \ge \alpha$, i.e. $\alpha \le x$ for every $x \in B$. But "$\alpha
\le x$ for every $x \in B$" is *precisely* Definition 1.7's condition for $\alpha$ to
be a lower bound of $B$. And $L$ was defined as the set of **all** lower bounds of
$B$ — so $\alpha \in L$.
 
---
 
**"If $\alpha < \beta$ then $\beta \notin L$, since $\alpha$ is an upper bound of
$L$."**
 
By condition (i) of Definition 1.8, $\alpha = \sup L$ is itself an upper bound of $L$
— meaning $y \le \alpha$ for **every** $y \in L$ (Def 1.7). So if some $\beta$
satisfied $\beta \in L$, we'd need $\beta \le \alpha$. Contrapositive: if $\beta >
\alpha$, then $\beta \notin L$ — i.e., $\beta$ is **not** a lower bound of $B$.
 
---
 
**"We have shown that $\alpha \in L$ but $\beta \notin L$ if $\beta > \alpha$. In
other words, $\alpha$ is a lower bound of $B$, but $\beta$ is not if $\beta > \alpha$.
This means that $\alpha = \inf B$."**
 
Put the last two boxed results together:
 
- $\alpha \in L$ means $\alpha$ *is* a lower bound of $B$ — condition (i) of
  Definition 1.8's infimum clause.
- For every $\beta > \alpha$, $\beta \notin L$ means $\beta$ is *not* a lower bound of
  $B$ — condition (ii) of Definition 1.8's infimum clause (no number greater than
  $\alpha$ is a lower bound).
Both conditions of Definition 1.8 (mirrored for infimum) are satisfied by $\alpha$ —
so $\alpha = \inf B$, exactly as claimed. $\blacksquare$
 
---
 
### Why every hypothesis was load-bearing
 
| Hypothesis | Where it's used | What breaks without it |
|---|---|---|
| $S$ has the LUB property | getting $\sup L$ to exist *in $S$* | $L$ could be a valid bounded-above set with no supremum in $S$ (Section 8's $\mathbb{Q}$ example) |
| $B \ne \emptyset$ | making $L$ bounded above | if $B$ were empty, every $x_0 \in B$ argument has nothing to fix, and $L$ could equal all of $S$, which may not be bounded above |
| $B$ bounded below | making $L$ nonempty | with no lower bound of $B$ to start with, $L = \emptyset$, and $\sup \emptyset$ isn't defined |
 
---
# Euclidean Spaces

## 10. What $\mathbb{R}^k$ actually is

For a positive integer $k$, $\mathbb{R}^k$ is just the set of all ordered $k$-tuples
of real numbers:
$$\mathbf{x} = (x_1, x_2, \dots, x_k).$$

That's it — no extra machinery yet. If $k = 1$, $\mathbb{R}^1$ is just the real line
you already know. If $k = 2$, it's ordered pairs $(x_1, x_2)$ — the usual $xy$-plane.
If $k = 3$, it's $(x_1, x_2, x_3)$ — ordinary 3D space. $\mathbb{R}^k$ simply lets you
go beyond 3 coordinates without needing a picture — the algebra works exactly the
same way no matter how large $k$ is.

The individual numbers $x_1, \dots, x_k$ are called the **coordinates** of
$\mathbf{x}$. Elements of $\mathbb{R}^k$ are called **points** when you're thinking
geometrically, or **vectors** when you're thinking of them as things you can add and
scale — same object, just a different mindset depending on context. That's why
they're written in bold: $\mathbf{x}$, $\mathbf{y}$, $\mathbf{z}$.

```
   k = 1:  R¹  ───●───────●───────►     (just a number line)
                 x₁       y₁

   k = 2:  R²        ● y = (y₁, y₂)
                     │
                     │
           ──────────●──────────►      (the ordinary plane)
                    x = (x₁, x₂)

   k = 3:  R³  — same idea, one more coordinate, harder to draw but
               algebraically no different.

   k = 7:  R⁷  — can't draw it, but every definition below works
               exactly the same way.
```

---

## 11 The two operations: addition and scalar multiplication

Given $\mathbf{x} = (x_1, \dots, x_k)$ and $\mathbf{y} = (y_1, \dots, y_k)$ in
$\mathbb{R}^k$, and a real number $\alpha$:

$$\mathbf{x} + \mathbf{y} = (x_1 + y_1, \ \dots, \ x_k + y_k)$$
$$\alpha \mathbf{x} = (\alpha x_1, \ \dots, \ \alpha x_k)$$

In words: **add coordinate by coordinate; scale coordinate by coordinate.** Nothing
mysterious — you're just doing ordinary real-number addition/multiplication $k$ times
in parallel, once per slot.

**Example** ($k = 3$): if $\mathbf{x} = (1, 2, 3)$ and $\mathbf{y} = (4, -1, 0)$,
$$\mathbf{x} + \mathbf{y} = (5, 1, 3), \qquad 2\mathbf{x} = (2, 4, 6).$$

Because these operations satisfy the commutative, associative, and distributive laws
(they inherit these directly from the real numbers, coordinate by coordinate),
$\mathbb{R}^k$ becomes what's called a **vector space over $\mathbb{R}$** — a set
where "adding two elements" and "scaling an element by a real number" both make
sense and behave the way you'd expect from ordinary algebra.

The **zero vector** (or **origin**), written $\mathbf{0}$, is just the point with
every coordinate equal to $0$: $\mathbf{0} = (0, 0, \dots, 0)$.

---

## 12. The inner product (dot product)

For $\mathbf{x}, \mathbf{y} \in \mathbb{R}^k$, define
$$\mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^{k} x_i y_i.$$

This is a single **number** (not a vector) — multiply corresponding coordinates and
add up all the products.

**Example**: $\mathbf{x} = (1, 2, 3)$, $\mathbf{y} = (4, -1, 0)$:
$$\mathbf{x} \cdot \mathbf{y} = (1)(4) + (2)(-1) + (3)(0) = 4 - 2 + 0 = 2.$$

The dot product is the algebraic tool that lets you talk about **angles and length**
in $\mathbb{R}^k$, even when $k$ is too big to draw — this is exactly what the
*norm* below is built from.

---

## 13. The norm (length of a vector)

$$|\mathbf{x}| = (\mathbf{x} \cdot \mathbf{x})^{1/2} = \left( \sum_{i=1}^{k} x_i^2 \right)^{1/2}$$

This is just the familiar Pythagorean-theorem idea, generalized: square every
coordinate, add them up, take the square root. In $\mathbb{R}^2$, this is exactly the
distance formula you already know: $|\mathbf{x}| = \sqrt{x_1^2 + x_2^2}$.

**Example**: for $\mathbf{x} = (3, 4)$ in $\mathbb{R}^2$,
$$|\mathbf{x}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5.$$

Nothing new here if $k \le 3$ — it's just "length" the way you've always understood
it. The point of Definition is that this same formula keeps making sense for
every $k$, letting you talk about "length" and "distance" in spaces you can't
visualize.

---

## 14. Euclidean $k$-space

$\mathbb{R}^k$ by itself is just a set of tuples. Once you equip it with:

- **addition** and **scalar multiplication** (making it a vector space), and
- the **inner product** $\mathbf{x} \cdot \mathbf{y}$ and the **norm** $|\mathbf{x}|$
  built from it,

Tthe whole package : set + operations + inner product + norm — is called
**Euclidean $k$-space**. 
---

## 15. Theorem 
For $\mathbf{x}, \mathbf{y}, \mathbf{z} \in \mathbb{R}^k$ and real $\alpha$, these
facts hold:

| Property | Statement | Plain-language meaning |
|---|---|---|
| (a) | $$|\mathbf{x}| \ge 0$$ | length is never negative |
| (b) | $$|\mathbf{x}| = 0 \iff \mathbf{x} = \mathbf{0}$$ | only the origin has zero length |
| (c) | $$|\alpha \mathbf{x}| = |\alpha||\mathbf{x}|$$ | scaling a vector by $$\alpha$$ scales its length by $|\alpha|$ |
| (d) | $$|\mathbf{x} \cdot \mathbf{y}| \le |\mathbf{x}||\mathbf{y}|$$ | the Cauchy–Schwarz inequality |
| (e) | $$|\mathbf{x} + \mathbf{y}| \le |\mathbf{x}| + |\mathbf{y}|$$ | the triangle inequality — going "directly" is never longer than going via a detour |
| (f) | $$|\mathbf{x} - \mathbf{z}| \le |\mathbf{x} - \mathbf{y}| + |\mathbf{y} - \mathbf{z}|$$ | triangle inequality again, phrased as distances between three points |

These are exactly the properties that make $$|\mathbf{x} - \mathbf{y}|$$ behave like a
sensible notion of "distance" between two points — this is what eventually lets you
define open sets, limits, and continuity in $\mathbb{R}^k$, all using the same
machinery you'll soon see for metric spaces in general.

---
# Some Examples

## (a) $(b^m)^{1/n} = (b^p)^{1/q}$ when $m/n = p/q$

Since $b > 1$, $b^m > 0$ and $b^p > 0$, so their positive real $n$-th and $q$-th roots exist (uniquely) by the least-upper-bound property of $\mathbb{R}$.

Let $x = (b^m)^{1/n}$ and $y = (b^p)^{1/q}$, so $x^n = b^m$ and $y^q = b^p$, with $x, y > 0$.

From $m/n = p/q$ we get $mq = np$.

Raise both sides to compatible powers:
$$x^{nq} = (x^n)^q = (b^m)^q = b^{mq}, \qquad y^{nq} = (y^q)^n = (b^p)^n = b^{pn}.$$

Since $mq = np$, the right-hand sides are equal: $x^{nq} = y^{nq}$.

The map $t \mapsto t^{nq}$ is strictly increasing on positive reals (since $nq$ is a positive integer), hence **injective** there. As $x, y > 0$ and $x^{nq} = y^{nq}$, we conclude
$$x = y, \quad \text{i.e.} \quad (b^m)^{1/n} = (b^p)^{1/q}.$$

This shows the value doesn't depend on which fraction $m/n$ is used to represent $r$ — so $b^r := (b^m)^{1/n}$ is unambiguous, and it makes sense to write $b^r$ for rational $r$. $\blacksquare$

---

## (b) $b^{r+s} = b^r b^s$ for rational $r, s$

Write $r = m/n$, $s = p/q$ with $n, q > 0$ integers, so $r + s = \dfrac{mq + np}{nq}$.

Let $x = (b^m)^{1/n} = b^r$ and $y = (b^p)^{1/q} = b^s$, so $x^n = b^m$, $y^q = b^p$.

Now, Compute:
$$(xy)^{nq} = x^{nq} y^{nq} = (x^n)^q (y^q)^n = (b^m)^q (b^p)^n = b^{mq} \, b^{pn} = b^{mq+np}.$$

By definition, $z := b^{r+s} = \big(b^{mq+np}\big)^{1/(nq)}$ satisfies $z^{nq} = b^{mq+np}$.

So $(xy)^{nq} = z^{nq}$, with $xy > 0$ and $z > 0$. Since $t \mapsto t^{nq}$ is injective on positive reals,
$$xy = z, \quad \text{i.e.} \quad b^r b^s = b^{r+s}. \qquad \blacksquare$$

---

## (c) $b^r = \sup B(r)$ for rational $r$

**$t \mapsto b^t$ is strictly increasing on rationals (given $b>1$).**

First, for any positive integer $n$, $b^n > 1$ (product of $n$ factors each $> 1$). For a positive rational $s = p/q$, $b^s = (b^p)^{1/q}$ where $b^p > 1$; if $b^s \le 1$ then $(b^s)^q \le 1$, but $(b^s)^q = b^p > 1$ — contradiction. So $b^s > 1$ for every positive rational $s$.

Now if $t_1 < t_2$ are rational, $t_2 - t_1 > 0$ is rational, so by part (b),
$$b^{t_2} = b^{t_1} \cdot b^{t_2 - t_1} > b^{t_1} \cdot 1 = b^{t_1},$$
since $b^{t_2-t_1} > 1$ and $b^{t_1} > 0$. So $t \mapsto b^t$ is strictly increasing on $\mathbb{Q}$.

**$b^r$ is an upper bound of $B(r)$.**

$B(r) = \{ b^t : t \in \mathbb{Q},\ t \le r \}$. By monotonicity, every $t \le r$ gives $b^t \le b^r$. So $b^r$ is an upper bound.

**$b^r$ is the *least* upper bound.**

Since $r$ itself is rational and $r \le r$, we have $b^r \in B(r)$. So $b^r$ isn't just *an* upper bound, it's the **maximum element** of $B(r)$ itself. Any upper bound of $B(r)$ must be $\ge$ every element of $B(r)$, in particular $\ge b^r$. So $b^r$ is the smallest upper bound:
$$b^r = \sup B(r). \qquad \blacksquare$$

This identity is exactly what licenses the extension: since $b^r$ agrees with $\sup B(r)$ whenever $r$ is rational, defining
$$b^x := \sup B(x)$$
for *every* real $x$ is a genuine extension of the rational case, not a redefinition. ($B(x)$ is nonempty — pick any rational $t \le x$ — and bounded above, e.g. by $b^N$ for any integer $N > x$, using the Archimedean property plus monotonicity — so $\sup B(x)$ exists in $\mathbb{R}$ by the least-upper-bound property.)

---

## (d) $b^{x+y} = b^x b^y$ for all real $x, y$

We show $b^{x+y} \le b^x b^y$ and $b^{x+y} \ge b^x b^y$ separately.

**Part 1: $b^{x+y} \le b^x b^y$.**

Let $u$ be any rational with $u \le x + y$. Since $u - y \le x$, the interval $[u-y,\ x]$ is nonempty, so (by density of $\mathbb{Q}$) it contains some rational $t$ with
$$u - y \le t \le x.$$
Set $s = u - t$. Then $s \le y$, $s$ is rational, and $t + s = u$.

Since $t \le x$, we have $b^t \in B(x)$, so $b^t \le \sup B(x) = b^x$. Similarly $b^s \le b^y$. Then, using part (b):
$$b^u = b^{t+s} = b^t b^s \le b^x b^y.$$

Since $u \le x+y$ was an arbitrary rational, $b^x b^y$ is an upper bound of $B(x+y)$. Hence
$$b^{x+y} = \sup B(x+y) \le b^x b^y.$$

**Part 2: $b^{x+y} \ge b^x b^y$.**

For any rationals $t \le x$ and $s \le y$, $t + s \le x + y$ is rational, so $b^{t+s} \in B(x+y)$, giving
$$b^t b^s = b^{t+s} \le \sup B(x+y) = b^{x+y}.$$

Fix $s$ and take the supremum over all rational $t \le x$ on the left: since $b^s > 0$ is a fixed positive constant, $\sup_t (b^t b^s) = b^s \sup_t b^t = b^s b^x$. So
$$b^x b^s \le b^{x+y} \quad \text{for every rational } s \le y.$$

Now take the supremum over all rational $s \le y$: similarly, $\sup_s (b^x b^s) = b^x \sup_s b^s = b^x b^y$. So
$$b^x b^y \le b^{x+y}.$$

**Conclusion.** Combining both parts,
$$b^{x+y} \le b^x b^y \quad \text{and} \quad b^x b^y \le b^{x+y} \implies b^{x+y} = b^x b^y. \qquad \blacksquare$$

# Metric Spaces

## 1. Definition — Metric Space

> A set $X$ is a **metric space** if with any two points $p, q \in X$ there's an
> associated real number $d(p,q)$, called the distance from $p$ to $q$, satisfying:
>
> **(a)** $d(p,q) > 0$ if $p \ne q$; $d(p,p) = 0$.
> **(b)** $d(p,q) = d(q,p)$.
> **(c)** $d(p,q) \le d(p,r) + d(r,q)$, for any $r \in X$.

Any function satisfying these three rules is called a **metric** (or distance
function). Notice the definition never says $X \subset \mathbb{R}^k$ — a metric space
can be built on *any* set, as long as you can define a sensible notion of distance
on it.

### Example 1 — the usual metric on $\mathbb{R}$

$$d(x,y) = |x - y|$$.

- (a) $$|x-y| > 0$ whenever $x \ne y$, and $|x-x|=0$$. ✓
- (b) $$|x-y| = |y-x|$$. ✓
- (c) $$|x-y| \le |x-r| + |r-y|$$ — this is just the ordinary triangle inequality for
  absolute value. ✓

### Example 2 — Euclidean distance on $\mathbb{R}^k$

$$d(\mathbf{x}, \mathbf{y}) = |\mathbf{x} - \mathbf{y}|$$ (the norm from Section on
Euclidean spaces). All three properties hold — 

### Example 3 — the discrete metric (a metric with no numbers in sight)

Let $$X$$ be **any** set at all (say, $$X = \{\text{cat, dog, tree}\}$$), and define
$$d(p,q) = \begin{cases} 0 & p = q \\ 1 & p \ne q \end{cases}$$

Check the axioms:
- (a) $$d(p,q) = 1 > 0$ whenever $p \ne q$; $d(p,p) = 0$$. ✓
- (b) Symmetric by construction. ✓
- (c) Triangle inequality: if $$p = q$$, LHS is $$0$$, automatically $$\le$$ anything
  nonnegative. If $$p \ne q$$, LHS is $$1$$; on the right, at least one of $$d(p,r),
  d(r,q)$$ must be $$1$$ (since $$r$$ can't equal both $$p$$ and $$q$$ unless $$p=q$$), so RHS
  $$\ge 1$$. ✓

This shows metrics don't need to come from "distance" in the usual geometric
sense at all — any set can be turned into a metric space this way. It's a useful
 example precisely *because* it's so unlike $$\mathbb{R}^k$$.

### Counterexample — a function that fails to be a metric

Try $$d(x,y) = (x-y)^2$$ on $$\mathbb{R}$$.

- (a) and (b) hold fine.
- (c) **fails.** Take $$x = 0$$, $$r = 1$$, $$y = 2$$:
$$d(x,y) = (0-2)^2 = 4, \qquad d(x,r) + d(r,y) = (0-1)^2 + (1-2)^2 = 1 + 1 = 2.$$
Since $$4 > 2$$, the triangle inequality is violated: $$d(x,y) \not\le d(x,r) + d(r,y)$$.
So squared difference is **not** a metric — a good reminder that not every
nonnegative, symmetric function of two points is automatically a legitimate
distance function.

---

## 2. Definition - Vocabulary of Metric Spaces

From here on, fix a metric space $X$; all points and sets below live in $X$. Unless
stated otherwise, the examples use $X = \mathbb{R}$ with the usual metric
$$d(x,y) = |x-y|$$.

### (a) Neighborhood

> $$N_r(p) = \{q : d(p,q) < r\}$ for some $$r > 0$$, called the neighborhood of $p$ with
> radius $$r$$.

**Example.** In $$\mathbb{R}$$, $$N_{0.5}(3) = \{q : |q - 3| < 0.5\} = (2.5,\ 3.5)$$ — an
open interval centered at $$3$$.

**Counterexample:** is $$[2.5, 3.5]$$ (the *closed* interval) a neighborhood
of $$3$$ under this definition? **No** , the definition uses strict inequality $$d(p,q)
< r$$, so a neighborhood is always an *open* ball; a closed interval, taken as a whole
object, doesn't match the definition of $$N_r(p)$ for any $$r$$.

### (b) Limit point

> $$p$$ is a limit point of $$E$$ if **every** neighborhood of $$p$$ contains some point
> $$q \ne p$$ with $$q \in E$$.

**Example.** Let $$E = (0,1) \subset \mathbb{R}$$. The point $0$ is a limit point of
$E$: take any neighborhood $$N_r(0) = (-r, r)$$; no matter how small $$r>0$$ is, it
contains points of $E$ like $$\min(r,1)/2$$. Note $$0 \notin E$$ , a limit point need not
belong to the set at all. Every point of $$(0,1)$$ is also a limit point of $$E$$ (and so
is $$1$$).

**Counterexample.** Let $$E = \{1, 2, 3\} \subset \mathbb{R}$$. Is $$1$$ a limit point of
$$E$$? Take $$r = 0.5$$: $$N_{0.5}(1) = (0.5, 1.5)$$ contains **no** point of $$E$$ other than
$$1$$ itself (and $$1$$ doesn't count, the definition requires $$q \ne p$$). So $1$ is
**not** a limit point of $E$. The same argument works for $2$ and $3$. In fact $E$ has
**no** limit points at all.

### (c) Isolated point

> If $p \in E$ and $p$ is *not* a limit point of $E$, then $p$ is an isolated point of
> $E$.

**Example.** Every point of $E = \{1,2,3\}$ from above is isolated, each one sits
alone with a neighborhood containing no other point of $E$.

**Counterexample.** No point of $E = (0,1)$ is isolated — we just showed every point
of $(0,1)$ is a limit point, so none of them can also be isolated (the two notions
are exact opposites, for points that belong to $E$).

### (d) Closed

> $E$ is closed if every limit point of $E$ is a point of $E$.

**Example.** $E = [0,1]$ is closed. Its limit points are exactly the points of
$[0,1]$ itself (check: is $2$ a limit point? No, $N_{0.5}(2)$ misses $E$ entirely.
Is $0.5$? Yes, and $0.5 \in E$. Is $0$? Yes, and $0 \in E$.), every limit point is
already inside $E$.

**Counterexample.** $E = (0,1)$ is **not** closed. We showed $0$ is a limit point of
$E$, but $0 \notin E$ — a single "missing" limit point is enough to disqualify $E$
from being closed.

**Vacuous example.** $E = \{1,2,3\}$ **is** closed — it has *no* limit points at all,
so the condition "every limit point of $E$ is in $E$" holds *vacuously* (there's
nothing to check). This trips people up: closed doesn't mean "big" or "continuous
looking" — a finite set is automatically closed.

### (e) Interior point

> $p$ is an interior point of $E$ if there's a neighborhood $N$ of $p$ with
> $N \subset E$.

**Example.** For $E = [0,1]$, the point $p = 0.5$ is an interior point: take
$N_{0.1}(0.5) = (0.4, 0.6) \subset [0,1]$. ✓

**Counterexample.** For the *same* set $E = [0,1]$, the point $p = 0$ is **not** an
interior point. Any neighborhood $N_r(0) = (-r, r)$ contains negative numbers (e.g.
$-r/2$), which are not in $E$. So no matter how small $r$ is, $N_r(0) \not\subset E$.
Same story for $p = 1$. This is the key example showing endpoints of a closed
interval fail to be interior points, even though they belong to the set.

### (f) Open

> $E$ is open if every point of $E$ is an interior point of $E$.

**Example.** $E = (0,1)$ is open: for any $p \in (0,1)$, let $\varepsilon =
\min(p, 1-p) > 0$; then $N_\varepsilon(p) \subset (0,1)$. Every single point clears
the bar.

**Counterexample.** $E = [0,1]$ is **not** open — we just showed $0 \in E$ is not an
interior point of $E$. One bad point (an endpoint, here) is enough to disqualify the
whole set.

*(This is also exactly Theorem 2.19 from your screenshot: every neighborhood $N_r(p)$
is automatically open — see Section 3 below for why.)*

### (g) Complement

> $E^c = \{p \in X : p \notin E\}$.

**Example.** If $E = (0,1) \subset \mathbb{R}$, then $E^c = (-\infty, 0] \cup
[1, \infty)$.

There's no real "counterexample" needed here — complement is just set-theoretic
negation, applied inside the ambient space $X$. Worth noting though: $E$ open and
$E^c$ closed always go together (and vice versa) — you'll likely meet this as a
theorem shortly.

### (h) Perfect

> $E$ is perfect if $E$ is closed **and** every point of $E$ is a limit point of $E$.

**Example.** $E = [0,1]$ is perfect: it's closed (Section (d) above), and every point
of $[0,1]$ is a limit point of $[0,1]$ (e.g. $0$: every neighborhood of $0$ contains
other points of $[0,1]$, like small positive numbers).

**Counterexample.** $E = \{1,2,3\}$ is closed (vacuously, as shown above) but **not**
perfect — none of its points are limit points of $E$ (they're all isolated, per
Section (c)). So being closed is *not enough*; you additionally need no isolated
points. This is exactly why the finite-set example, harmless for "closed," fails
"perfect."

### (i) Bounded

> $E$ is bounded if there's a real number $M$ and a point $q \in X$ such that
> $d(p,q) < M$ for all $p \in E$.

**Example.** $E = (0,1) \subset \mathbb{R}$ is bounded: take $q = 0$, $M = 2$; every
$p \in (0,1)$ has $d(p, 0) = |p| < 1 < 2$.

**Counterexample.** $E = \mathbb{Z}$ (the integers) is **not** bounded in
$\mathbb{R}$: for any proposed $q$ and $M$, you can always find an integer $p$ with
$|p - q| \ge M$ (just go far enough in either direction) — no single $M$ works for
every point simultaneously.

### (j) Dense

> $E$ is dense in $X$ if every point of $X$ is a limit point of $E$, or a point of
> $E$ (or both).

**Example.** $\mathbb{Q}$ is dense in $\mathbb{R}$: every real number, rational or
not, is a limit point of $\mathbb{Q}$ — any neighborhood of any real number contains
infinitely many rationals (this uses the fact that between any two reals there's a
rational).

**Counterexample.** $\mathbb{Z}$ is **not** dense in $\mathbb{R}$: take $x = 0.5 \in
\mathbb{R}$. Is $0.5$ a point of $\mathbb{Z}$? No. Is it a limit point of
$\mathbb{Z}$? No — $N_{0.1}(0.5) = (0.4, 0.6)$ contains no integer at all. So $0.5$
fails both conditions, and $\mathbb{Z}$ is not dense.

---

## 3. Theorem 2.19 — Every Neighborhood Is an Open Set

> **Theorem.** Consider a neighborhood $E = N_r(p)$, and let $q$ be any point of $E$.
> Then there's a positive real number $h$ such that $d(p,q) = r - h$.
>
> For all points $s$ such that $d(q,s) < h$, we have then
> $$d(p,s) \le d(p,q) + d(q,s) < r - h + h = r,$$
> so that $s \in E$. Thus $q$ is an interior point of $E$.

Since $q$ was an *arbitrary* point of $E$, this proves **every** point of a
neighborhood is an interior point of it, i.e., by Definition 2.18(f), every
neighborhood is open.

### Worked numeric example

Let $X = \mathbb{R}$, $p = 0$, $r = 5$, so $E = N_5(0) = (-5, 5)$. Take
$q = 3 \in E$.

- $d(p,q) = |0 - 3| = 3$, so $h = r - d(p,q) = 5 - 3 = 2$.
- Claim: every $s$ with $d(q,s) < 2$, i.e. every $s \in (1, 5)$, is still in $E =
  (-5,5)$. Check with the triangle inequality: $d(p,s) \le d(p,q) + d(q,s) < 3 + 2 =
  5$. ✓ So $N_2(3) = (1,5) \subset (-5,5)$ , $q=3$ has a whole neighborhood sitting
  safely inside $E$, confirming $3$ is an interior point of $E$.

### Why the specific choice $h = r - d(p,q)$ works

$h$ is exactly "how much room is left" between $q$ and the edge of $E$. Since $q \in
E = N_r(p)$, we know $d(p,q) < r$, so $h = r - d(p,q) > 0$ , that's *why* such an $h$
exists at all. The triangle inequality then guarantees that shrinking the radius
around $q$ down to $h$ keeps you safely inside the original ball around $p$, no
matter which point $s$ you pick within that smaller radius.
