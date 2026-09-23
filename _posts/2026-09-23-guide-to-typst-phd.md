---
layout: single
title: "Guide to Typst - PhD (Generated using AI)"
date: 2026-09-23
category: "Guide"
subcategory: "PhD"
tags: [PhD, Guide]
classes: wide
---
# Typst for Economics Research: A Practical Guide


This guide is meant to be plundered for snippets. Every example uses real economic notation and terminology instead of generic placeholders, so the code is copy-paste-ready for actual papers, problem sets, and job market presentations. The package choices reflect general best practice across the (still young, fast-moving) Typst ecosystem rather than any single department's house style — if your program or target journal only accepts LaTeX/Word submissions, you'll still need to export to PDF at the end, which Typst does natively.

> **Using the Typst web app?** Everything below works unchanged: at `typst.app` you get a full, current Typst install with the entire package universe (`ctheorems`, `touying`, `cetz`, etc.) available via `#import "@preview/..."` with nothing to download or configure locally. The two places where the web app changes your workflow rather than your code are: (1) you never type compile commands yourself — the web app recompiles as you type, with a live preview pane, and (2) packages are fetched automatically the first time you import them rather than installed via a package manager. Both are called out inline wherever they come up (Section 5 on bibliographies, and the boilerplate in Sections 4 and 6). If you compile locally instead, install the `typst` CLI (current stable is 0.15.x) and packages are cached automatically on first `#import` too — there's no separate package-manager step even offline.

---

## Table of Contents

1. [Document Structure & Setup](#1-document-structure--setup)
2. [Theoretical Economics & Math Formatting](#2-theoretical-economics--math-formatting)
3. [Empirical Economics & Tables](#3-empirical-economics--tables)
4. [Figures & Graphics](#4-figures--graphics)
5. [References & Bibliography](#5-references--bibliography)
6. [Presentations (Touying)](#6-presentations-touying)

---

## 1. Document Structure & Setup

### 1.1 There Is No `\documentclass` — Typst Uses Functions and Templates

Typst has no class system to choose between up front. Every `.typ` file is just a document; page size, margins, and numbering are set with `#set` rules at the top of the file, and the overall "look" (title page, chapter styling, front matter) is applied with a **template function** wrapped around your content via a `#show` rule. This is the single biggest structural difference from LaTeX: there's no `article` vs. `report` vs. `book` decision to make before you start writing, because a template is just a function you can swap out later without touching your prose.

```typst
#set page(paper: "a4", margin: 1in)
#set text(size: 12pt, font: "New Computer Modern")
#set par(justify: true, leading: 0.65em)  // roughly 1.5 line spacing
```

**Rule of thumb:** for a single stand-alone paper or job market paper draft, write directly against a hand-rolled preamble like the one above (Section 1.2) — this is what most conference submission systems and journals expect once exported to PDF. For a dissertation with chapters, front matter, and appendices, reach for a maintained dissertation template from Typst Universe (search `#import "@preview/dissertate:..."` or similar on `typst.app/universe`) rather than building chapter/front-matter machinery from scratch, the way you'd reach for the `book` class in LaTeX.

### 1.2 Essential Preamble for Economics Papers

```typst
#set page(paper: "a4", margin: 1in, numbering: "1")
#set text(size: 12pt, font: "New Computer Modern", lang: "en")
#set par(justify: true, leading: 0.65em, first-line-indent: 1.5em)

// --- Headings ---
#set heading(numbering: "1.1")

// --- Math ---
#set math.equation(numbering: "(1)")

// --- Tables ---
#set table(stroke: none)  // we draw our own rules with booktabs-style strokes, Section 3

// --- Figures ---
#set figure(supplement: [Figure])

// --- Bibliography (economics standard: author-year, e.g. APA-style CSL) ---
// see Section 5 for #bibliography(...) and citation setup

// --- Misc economics conveniences ---
#let R = math.bb("R")
#let E = math.bb("E")
#let N = math.bb("N")
#let argmax = math.op("arg max", limits: true)
#let argmin = math.op("arg min", limits: true)
```

> **Why no `natbib`-equivalent import here?** Typst's citation and bibliography machinery (`#cite`, `#bibliography`) is built into the compiler itself — there's nothing to `#import`. You only reach for a package when you want something beyond the built-ins: theorem environments (`ctheorems`), diagrams (`cetz`), or slides (`touying`). See Section 5 and Section 6.

> **A note on package versions:** unlike LaTeX, where `\usepackage{foo}` picks up whatever version is installed on the system (or on Overleaf), every Typst `#import` names an exact version — `#import "@preview/ctheorems:1.1.2": *`. This means a document that compiles today will keep compiling identically years from now, but it also means you should check Typst Universe (`typst.app/universe`) for the current version before copying snippets verbatim, since these examples will drift out of date faster than the LaTeX ones above.

### 1.3 Document Hierarchy

```typst
= Introduction
== Related Literature on Platform Competition
=== Two-Sided Markets
Indirect network effects arise when...
```

| Command | Numbering Depth | Typical Content |
|---|---|---|
| `=` | 1 | Introduction, Model, Data, Results, Conclusion |
| `==` | 1.1 | Equilibrium Concept, Identification Strategy |
| `===` | 1.1.1 | Specific lemma derivations, robustness sub-checks |
| `====` | 1.1.1.1 | Rarely needed — if you're here, consider restructuring |

There is no separate `\paragraph{}`-style run-in heading command; for a short, unnumbered aside within a subsubsection, just use a bold lead-in with `#strong[Network effects.]` followed by ordinary text, or wrap it in a `#heading(numbering: none, outlined: false)[...]` call if you want it to behave like a heading without entering the numbering scheme.

### 1.4 Table of Contents

```typst
#outline(title: [Table of Contents])
#pagebreak()
```

For dissertations, also generate lists of tables/figures:

```typst
#outline(title: [List of Tables], target: figure.where(kind: table))
#outline(title: [List of Figures], target: figure.where(kind: image))
```

> **Note:** most journal-style papers (single-section, 1.5-spaced, under ~40 pages) don't include a table of contents at all — reserve `#outline()` for term papers, dissertation chapters, and long technical reports. Unlike LaTeX, there's no two-pass compile needed to get the ToC right: Typst's incremental compiler resolves headings, page numbers, and cross-references in a single pass (or effectively-instant background passes in the live preview), so nothing here is stale the way an un-recompiled LaTeX `.toc` file can be.

---

## 2. Theoretical Economics & Math Formatting

### 2.1 Math Mode Is Built In — No Package Trio Needed

Where LaTeX needs `amsmath` + `amssymb` + `amsfonts` loaded explicitly, Typst's math mode, symbol set, and blackboard-bold/Fraktur letters are all part of the core language. `\mathbb{R}` becomes `#math.bb("R")` (or, once you've aliased it as in Section 1.2, just `$R$` after `#let R = math.bb("R")`), and relation symbols like `\succsim` or `\subseteq` are just written as `succsim` or `subset.eq` inside math mode, with no extra import.

```typst
// Common economics symbol shortcuts (put these in your preamble, as in 1.2)
#let R = math.bb("R")
#let E = math.bb("E")          // expectation operator
#let N = math.bb("N")          // player/agent index set
#let argmax = math.op("arg max", limits: true)
#let argmin = math.op("arg min", limits: true)
```

### 2.2 Inline vs. Display Math

```typst
// Inline math: use for short expressions within a sentence
Firm $i$ chooses price $p_i in RR_+$ to maximize profit $pi_i (p_i, p_{-i})$.

// Display math: use for the "headline" equation you want the reader to pause on
$ pi_i (p_i, p_{-i}) = (p_i - c_i) D_i (p_i, p_{-i}) $
```

A few mechanics that trip up LaTeX refugees: math mode is entered and exited with single `$...$` for both inline and display — Typst decides which to render based on surrounding whitespace/newlines, not a different delimiter — and spaces inside `$...$` are meaningful (they control spacing between symbols), unlike LaTeX where they're mostly ignored. Multi-letter identifiers like `pi` or `RR` are parsed as symbol names automatically (so `pi` renders as $\pi$), but a run of letters meant to be literal text (e.g., a variable actually called `cost`) needs quotes or `#` treatment to avoid being parsed as several one-letter variables multiplied together — write `$"cost"_i$` or define it as a function beforehand.

### 2.3 Multi-Line Equations: A Game Theory Optimization Example

A classic Cournot-with-network-effects best-response derivation using the `align` construct built into math mode (via `&` for alignment points, same visual idea as LaTeX's `align` environment but no separate package or environment name needed):

```typst
$ max_(q_i >= 0) quad & pi_i (q_i, q_(-i)) = [a - b(q_i + sum_(j != i) q_j) + gamma x_i] q_i - c q_i \
  "F.O.C.:" quad & a - 2 b q_i - b sum_(j != i) q_j + gamma x_i - c = 0 \
  arrow.r.double quad & q_i^* = (a - c + gamma x_i - b sum_(j != i) q_j) / (2b) $ <eq:cournot-br>
```

Here `x_i` denotes a network-adoption externality term — natural in a network economics context. The mechanics: `&` marks the alignment point on each line, `\` ends a line (same symbol as LaTeX), and the whole block is still just one `$ ... $` pair — there's no separate `align`/`align*` environment to choose between. Numbering is controlled globally by the `#set math.equation(numbering: "(1)")` rule from Section 1.2, and applies to every display equation by default; label individual lines you'll reference with `<eq:label>` right after the line (as on the last line above), and suppress numbering on lines you don't want numbered by wrapping just that equation in `#math.equation(numbering: none)[$ ... $]` rather than switching the whole block to an unnumbered variant the way `align*` does in LaTeX.

```typst
$ U_i (sigma_i, sigma_(-i)) &= sum_(s in S) p(s | sigma) u_i (s) \
  sigma_i^* &in argmax_(sigma_i in Delta(S_i)) U_i (sigma_i, sigma_(-i)^*) $
```

Reference a labelled line in text with `@eq:cournot-br` (Typst's cross-reference syntax, which works identically for equations, figures, tables, and headings — see Section 4).

### 2.4 Integration by Parts (Pedagogical Notation)

For deriving expected consumer surplus or hazard-rate expressions in piracy-deterrence models, here is the classic pedagogical form of integration by parts:

```typst
$ u v = u integral v - integral (d u integral v) $
```

A worked example, e.g. integrating a hazard function for time-to-detection of a pirated good:

```typst
$ integral_0^T t f(t) dif t
  &= [t dot F(t)]_0^T - integral_0^T F(t) dif t \
  &quad #text[(using ] u v = u integral v - integral (d u integral v) #text[ with ] u = t,\ d v = f(t) dif t #text[)] $
```

`dif` is Typst's built-in upright differential operator (renders as an upright "d" with correct spacing before the integration variable) — there's no `\mathrm{d}` workaround needed.

### 2.5 Theorems, Lemmas, and Proofs

Typst has no built-in theorem environment (this is one of the few places core LaTeX actually does more out of the box) — reach for the community `ctheorems` package, which is the de facto standard and plays the same role `amsthm` does:

```typst
#import "@preview/ctheorems:1.1.2": *
#show: thmrules

#set heading(numbering: "1.1")

#let theorem = thmbox("theorem", "Theorem", base: "heading", base_level: 1)
#let lemma = thmbox("lemma", "Lemma", base: "theorem")
#let proposition = thmbox("proposition", "Proposition", base: "theorem")
#let corollary = thmbox("corollary", "Corollary", base: "theorem")

#let definition = thmbox("definition", "Definition", base: "heading", base_level: 1, inset: 1em)
#let assumption = thmbox("assumption", "Assumption", base: "definition")

#let proof = thmproof("proof", "Proof")
```

The mechanics: `thmbox(identifier, "Displayed Name", ...)` creates a new environment function; passing `base: "theorem"` (rather than the default `base: "heading"`) makes an environment **share** theorem's counter, so numbering runs Theorem 2.1, Lemma 2.2, Proposition 2.3 in document order, matching what most economics journals expect — this is the direct analogue of LaTeX's `\newtheorem{lemma}[theorem]{Lemma}`. `base: "heading"` with `base_level: 1` instead resets the counter at each `=`-level section, the analogue of LaTeX's `[section]` argument. Unlike `amsthm`'s `\theoremstyle{plain|definition|remark}` presets, `ctheorems` styling (italics vs. upright body, box fill, spacing) is set per-environment via arguments to `thmbox`/`thmplain` rather than inherited from a named style, which is more verbose up front but easier to override for one specific environment later.

Usage in the body:

```typst
#assumption("Homogeneous Piracy Cost")[
  All consumers face an identical marginal cost of piracy, $kappa > 0$, independent of network size $n$.
] <as:homogeneous-cost>

#proposition[
  Under @as:homogeneous-cost, there exists a unique symmetric Bayesian Nash equilibrium in which the platform sets price $p^* = (a + c + gamma overline(x)) / 2$.
] <prop:unique-equilibrium>

#proof[
  Suppose, for contradiction, that two distinct symmetric equilibria $p_1^* != p_2^*$ exist. By the strict concavity of $pi_i (dot)$ established above, the best-response correspondence is single-valued, a contradiction.
]
```

Note `@as:homogeneous-cost` inside the proposition body — the same `@label` cross-reference syntax used for equations and figures works for theorem-like environments too, since `ctheorems` registers each one as a labelled, referenceable element. There's no `\qedhere` equivalent to worry about: `thmproof` places the ∎ symbol automatically at the end of the proof body regardless of whether it falls mid-equation or after prose.

---

## 3. Empirical Economics & Tables

### 3.1 The Philosophy of Publication-Quality Tables

Economics journals (AER, QJE, Econometrica) follow a shared house style:

- **No vertical rules.** Vertical lines clutter the table and are considered amateurish.
- **Minimal horizontal rules** — typically three: top, one after the header, and bottom.
- **Decimal alignment** in numeric columns so that standard errors line up under coefficients.
- **Notes below the table**, not above, explaining significance stars, standard error clustering, and sample restrictions.

Typst's native `#table()` function draws no rules at all by default once you set `stroke: none` (Section 1.2), so you add exactly the rules you want with `table.hline()` — there's no separate `booktabs`-equivalent package to import; the "no vertical rules, three horizontal rules" convention is just a pattern you apply directly with the built-in function.

### 3.2 `table` Basics

```typst
#figure(
  caption: [Summary Statistics: Platform-Level Network Data],
  table(
    columns: 4,
    stroke: none,
    align: (left, center, center, center),
    table.hline(),
    [Variable], [Mean], [Std. Dev.], [N],
    table.hline(),
    [Active users (000s)], [542.3], [118.7], [1,204],
    [Piracy incidence rate], [0.184], [0.091], [1,204],
    [Platform price (\$)], [9.99], [2.14], [1,204],
    table.hline(),
  )
) <tab:summary-stats>
```

Unlike LaTeX's `1{,}204` workaround for thousands-separator spacing, Typst's text layout doesn't insert extra space after a comma in table cells — `1,204` just works as typed, since table cells are ordinary text content rather than math-adjacent markup.

### 3.3 Regression Tables

Typst has no direct analogue of `dcolumn`'s automatic decimal-point alignment — the common workaround is to right-align the numeric columns and format coefficients with a consistent number of decimal places yourself (or via a helper function), accepting the same "stars slightly break perfect alignment" trade-off that LaTeX users make peace with using `dcolumn`. For anything beyond a small hand-typed table, most economists generate the table body from Stata/R as CSV or a Typst-native data structure and feed it through `#table()` programmatically rather than typing coefficients by hand — see the note on Section 3.4 below.

```typst
#import "@preview/tablex:0.0.9": tablex, colspanx, rowspanx  // optional: richer table layout

#figure(
  caption: [Effect of Network Size on Piracy Take-Up],
  table(
    columns: 4,
    stroke: none,
    align: (left, right, right, right),
    table.hline(),
    [], [(1)\ OLS], [(2)\ IV], [(3)\ Poisson],
    table.hline(),
    [Network size ($ln n_i$)], [0.412#super[***]], [0.389#super[***]], [0.401#super[***]],
    [], [(0.087)], [(0.102)], [(0.093)],
    [Price ($p_i$)], [-0.215#super[**]], [-0.198#super[**]], [-0.207#super[**]],
    [], [(0.094)], [(0.088)], [(0.091)],
    table.hline(),
    [Firm FE], [Yes], [Yes], [Yes],
    [Year FE], [Yes], [Yes], [Yes],
    [Observations], [1,204], [1,204], [1,204],
    table.hline(),
  )
) <tab:reg-main>

#text(size: 9pt)[
  _Notes:_ Standard errors clustered at the platform level in parentheses. $*p<0.10$, $**p<0.05$, $***p<0.01$.
]
```

> **Why no `threeparttable` import:** the width-matching table-notes behavior that `threeparttable` provides in LaTeX is handled natively — wrap the notes text in a `#block(width: ...)` sized to the table, or simply place the `#text(...)` note directly under the `#figure`, and Typst's ordinary paragraph wrapping keeps it legible without a dedicated package. Reach for the `tablex` package (imported above) only when you need column/row spanning, striped rows, or other layout features beyond what core `#table()` offers — it is not required for the basic booktabs-style layout shown here.

### 3.4 Cell Spanning: `table.cell(colspan: ...)`

```typst
#figure(
  caption: [Piracy Deterrence by Enforcement Regime and Market],
  table(
    columns: 4,
    stroke: none,
    align: (left, left, center, center),
    table.hline(),
    table.cell(rowspan: 2)[Enforcement Regime], table.cell(rowspan: 2)[Market],
    table.cell(colspan: 2, align: center)[Piracy Rate],
    table.hline(start: 2, end: 4, stroke: 0.6pt),
    [], [], [Pre-Policy], [Post-Policy],
    table.hline(),
    table.cell(rowspan: 2)[Strict (DMCA-style)], [Streaming], [0.24], [0.11],
    [Software], [0.31], [0.14],
    table.cell(rowspan: 2)[Lenient], [Streaming], [0.29], [0.26],
    [Software], [0.38], [0.35],
    table.hline(),
  )
) <tab:multirow-example>
```

`table.cell(rowspan: 2)[...]` and `table.cell(colspan: 2)[...]` are the direct built-in replacements for `\multirow`/`\multicolumn` — no separate package needed. `table.hline(start: 2, end: 4, stroke: 0.6pt)` is the analogue of `\cmidrule(lr){3-4}`: a partial rule under a subset of columns (Typst's columns are 0-indexed, so `start: 2, end: 4` covers what LaTeX would call columns 3–4).

---

## 4. Figures & Graphics

### 4.1 Inserting Graphics

```typst
#figure(
  image("figures/network_topology.pdf", width: 75%),
  caption: [Simulated Network Topology Under Preferential Attachment ($gamma = 2.1$)]
) <fig:network-topology>
```

- Always use **vector PDF or SVG** (from R's `ggsave(..., device = "pdf")` or Stata's `graph export ..., as(pdf)`), never PNG/JPEG for line plots or network diagrams — this keeps them crisp at any zoom, exactly as in LaTeX.
- Reference figures in text with `@fig:network-topology` — Typst's `@label` cross-reference syntax automatically inserts "Figure" (or whatever supplement the figure kind implies) and the correct number, with no separate `cleveref`-style package needed and no non-breaking-space workaround: Typst keeps the reference text together across line breaks by default.
- **In the web app:** drag your PDF/image files into a `figures` folder in the project file panel (or create one via the "+" button), so the relative path `figures/network_topology.pdf` in `image()` resolves correctly — the file panel mirrors the relative paths you write in the `.typ` source exactly, the same convention as Overleaf's.

### 4.2 Side-by-Side Subfigures (e.g., comparing network structures)

```typst
#figure(
  grid(
    columns: (1fr, 1fr),
    gutter: 1em,
    figure(
      image("figures/network_core.pdf", width: 100%),
      caption: [Core-periphery structure]
    ) <fig:core-periphery>,
    figure(
      image("figures/network_random.pdf", width: 100%),
      caption: [Random graph benchmark]
    ) <fig:random-graph>,
  ),
  caption: [Observed vs. Simulated Network Structures]
) <fig:network-comparison>
```

`grid(columns: (1fr, 1fr), gutter: 1em, ...)` is the direct replacement for `subcaption`'s side-by-side `subfigure` environments plus the manual `\hfill` spacer: `1fr, 1fr` splits the available width evenly between the two panels, and `gutter: 1em` sets the gap between them — no separate package and no fragile `\hfill`/percentage-width arithmetic. Each inner `figure()` still gets its own caption and label, so `@fig:core-periphery` refers to the left panel specifically, while `@fig:network-comparison` refers to the pair as a whole.

### 4.3 Placement: Typst Has No Float Specifiers

This is a genuine simplification, not just a syntax change: Typst has no `[htbp]`-style placement system at all. A `#figure(...)` is laid out at the point it appears in the source, in the normal flow of the document, the way an image in a word processor would be — there is no separate "floats" mechanism trying to find the "best" location on the page, and therefore nothing analogous to `\begin{figure}[H]` to fight with. If a figure would otherwise split awkwardly across a page break, wrap it in `#block(breakable: false)[...]` to keep it together on one page; this is the only placement control most economics documents ever need. For a genuinely large figure or table that should occupy its own page, use `#pagebreak()` before and after it rather than a `p` float specifier.

---

## 5. References & Bibliography

### 5.1 The Hayagriva/BibTeX Workflow

Typst's citation and bibliography engine (`#cite`, `#bibliography`) is built into the compiler — there is no `natbib` vs. `biblatex` choice and no separate compile pass to run. You have two format options for your reference database:

1. **Reuse an existing `.bib` file** — Typst reads standard BibTeX/BibLaTeX files natively, so if you already have `references.bib` from a LaTeX project, it works unchanged.
2. **Hayagriva `.yml`** — a newer, Typst-native format that's more readable and avoids some of BibTeX's quirks (no manual escaping of special characters, native support for URLs and access dates):

```yaml
katz1985network:
  type: article
  title: Network Externalities, Competition, and Compatibility
  author: [Katz, Michael L., Shapiro, Carl]
  date: 1985
  parent:
    type: periodical
    title: American Economic Review
    volume: 75
    issue: 3
  page-range: 424-440

peitz2006piracy:
  type: article
  title: Why the Music Industry May Gain from Free Downloading
  author: [Peitz, Martin, Waelbroeck, Patrick]
  date: 2006
  parent:
    type: periodical
    title: International Journal of Industrial Organization
    volume: 24
    issue: 5
  page-range: 907-913
```

Wire it up with:

```typst
#set bibliography(style: "apa")  // see 5.2 for style choices
#bibliography("references.yml")
```

**In the web app:** upload `references.bib` or `references.yml` via the file panel's upload button, keep `#bibliography("references.bib")` pointing at it, and just keep typing — there is no BibTeX pass to trigger and no Recompile-twice ritual: citations and the reference list resolve together on every keystroke, since Hayagriva runs as part of the ordinary Typst compilation rather than as an external tool. If a citation renders as a broken reference, double-check the key matches the `.bib`/`.yml` entry name exactly — there's no stale-`.aux` failure mode to work around, so a mismatch is almost always a genuine typo.

**Compiling locally** (outside the web app):

```bash
typst compile main.typ
# or, to auto-recompile on save:
typst watch main.typ
```

One command, one pass — no `bibtex`/`pdflatex` dance.

### 5.2 Choosing a Citation Style

| | Typst (`#bibliography`/`#cite`) | LaTeX `natbib` |
|---|---|---|
| Standard in economics? | No single mandated default — pick a CSL style matching your target journal | `natbib` author-year matches AEA/Econometrica house styles |
| Backend | Hayagriva + CSL (Citation Style Language), built into the compiler | BibTeX (or `bibtex8`) |
| Citation commands | `@key` (shorthand) or `#cite(<key>)` (explicit) | `\citet`, `\citep`, `\citeauthor`, `\citeyear` |
| Style files | Any of ~100 bundled CSL styles, or a custom `.csl` file | Journal-supplied `.bst` file |
| Recommendation | Use a bundled author-year CSL style (`"apa"` is the closest general-purpose default) unless your journal supplies its own `.csl` | Use `natbib` for economics papers |

```typst
#set bibliography(style: "apa")     // good general default for economics
// alternative: #set bibliography(style: "ieee") for more technical/IO-adjacent venues
```

If your target journal supplies its own `.csl` file (increasingly common, since CSL is the emerging standard across typesetting systems), point directly at it: `#set bibliography(style: "path/to/journal-style.csl")`.

### 5.3 Citation Syntax

```typst
// Textual citation — reads as part of the sentence
@katz1985network show that network externalities can generate multiple equilibria.
// Output (with an author-year style): "Katz and Shapiro (1985) show that..."

// Parenthetical citation — for supporting evidence at the end of a clause
Network externalities can generate multiple equilibria #cite(<katz1985network>).
// Output: "...multiple equilibria (Katz & Shapiro, 1985)."

// Multiple sources
The piracy-deterrence literature is well established #cite(<peitz2006piracy>, <katz1985network>).
```

There is no separate `\citet` vs. `\citep` command pair to remember: the bare `@key` shorthand and the explicit `#cite(<key>)` call render *identically* by default (both parenthetical, following whatever style is set) — the LaTeX distinction between "textual" and "parenthetical" citation forms is instead a property of how you write the surrounding sentence, since Typst's CSL-driven styles generally don't offer a separate "author as subject of the sentence" mode the way `\citet` does. If your chosen style needs the author's name to read naturally as the sentence's subject (as in the "Katz and Shapiro (1985) show that..." example above), you'll typically write it out by hand rather than relying on a citation command to reshape the sentence for you — a small but real loss of the automation LaTeX's `\citet` provides.

---

## 6. Presentations (Touying)

### 6.1 Complete Boilerplate Template

Typst has no slide-native document type — the community `touying` package plays the role `beamer` does in LaTeX, and is by far the dominant choice (it explicitly inherits concepts and API from the earlier `polylux` package, similar to how modern LaTeX slide decks build on `beamer`'s conventions):

```typst
#import "@preview/touying:0.7.4": *
#import themes.university: *

#show: university-theme.with(
  aspect-ratio: "16-9",
  config-info(
    title: [Network Effects and the Economics of Digital Piracy],
    subtitle: [Job Market Paper],
    author: [Your Name],
    institution: [Indira Gandhi Institute of Development Research],
    date: datetime.today(),
  ),
)

#title-slide()

= Outline
#outline-slide()

= Motivation
== Motivation

- Digital platforms exhibit strong network externalities.
#pause
- Piracy interacts with network size in non-obvious ways.
#pause
- This paper models the joint determination of price, network adoption, and piracy incidence.

= Model
== Setup

Firm $i$ sets price $p_i$ to maximize

$ pi_i (p_i) = (p_i - c) D_i (p_i, x_i) - kappa rho(p_i) $

where $x_i$ is network size and $rho(p_i)$ is the piracy rate.

= Results
== Main Result

#proposition[
  Under mild regularity conditions, equilibrium price is decreasing in the piracy-deterrence cost $kappa$.
]

= Conclusion
== Conclusion

- Network effects amplify the welfare cost of piracy enforcement.
- Policy implication: uniform DMCA-style enforcement may be suboptimal across markets of different network density.

== References

#bibliography("references.yml", title: none, style: "apa")
```

You can use `@key`/`#cite()` inside any slide exactly as in a paper (Section 5.3). In the web app, just upload `references.bib`/`references.yml` alongside your `.typ` file the same way as for a regular paper (Section 5.1) — no extra compile pass for citations in slides either. Compiling locally, it's the same single `typst compile deck.typ` command as any other document (Section 5.1) — Touying decks need no extra passes for citations or a table of contents, unlike Beamer.

### 6.2 Best Professional Themes for Academic Economics

Touying ships several built-in themes, with more available as separate Typst Universe packages:

| Theme | Character | Good For |
|---|---|---|
| `themes.simple` | Minimal, no chrome — closest analogue to Beamer's bare defaults | Quick internal talks, workshop lightning talks |
| `themes.university` | Clean header/footer with institution branding | General seminar talks — the default shown above |
| `themes.metropolis` | Modern flat design, mirrors LaTeX's popular `metropolis` Beamer theme | Talks aiming for a contemporary look |
| `themes.dewdrop` | Understated sidebar-free layout | Job talks — a safe, conservative choice, analogous to Beamer's `Boadilla` |
| `themes.stargazer` | High-contrast dark-friendly palette | Talks presented in bright rooms or hybrid/streamed settings |

```typst
#import themes.dewdrop: *
#show: dewdrop-theme.with(aspect-ratio: "16-9")
```

Unlike Beamer's separate presentation-theme/color-theme split, each Touying theme bundles its own color palette; to restyle just the colors within a theme, override specific theme arguments (consult the theme's own documentation on Typst Universe) rather than swapping in an independent "color theme" package.

### 6.3 Theme Galleries (Browse Before You Commit)

- Touying's own gallery and documentation: `https://touying-typ.github.io`
- Typst Universe, searchable by package (themes, `cetz` for diagrams, etc.): `https://typst.app/universe`

### 6.4 Overlays, `#pause`, and Frame Structure

```typst
== Sequential Reveal of Assumptions

- Assumption 1: Consumers are risk-neutral.
#pause
- Assumption 2: The platform has full commitment power.
#pause
- Assumption 3: Piracy technology is common knowledge.

// Finer-grained control, analogous to LaTeX's <> overlay specifications
#slide[
  #uncover("1-")[This appears from slide 1 onward.]
  #uncover("2-")[This appears from slide 2 onward.]
  #only("3")[This appears only on slide 3.]
]
```

`#pause` plays the same role as LaTeX's `\pause`: it splits everything before it from everything after it into separate reveal steps within one heading-slide, and you can stack several. Touying's finer-grained equivalents of Beamer's `<2->`/`<3>`/`<only@2>` overlay syntax are the `#uncover(...)` (stays in the layout but invisible until its range) and `#only(...)` (removed from the layout entirely outside its range, so later content shifts to fill the gap) functions — same two behaviors LaTeX offers, just as named function calls rather than angle-bracket annotations.

### 6.5 Title Slide Fields

The title slide is generated automatically from the `config-info(...)` call passed to your theme's `#show: ...-theme.with(...)` rule (see the boilerplate above) via `#title-slide()` — the direct analogue of Beamer's `\title`/`\subtitle`/`\author`/`\institute`/`\date` preamble fields feeding `\frame{\titlepage}`.

---

## Quick-Reference Cheat Sheet

```bash
# In the web app: nothing to run — it recompiles live as you type,
# citations and all.

# Compiling locally instead:
typst compile main.typ      # paper with bibliography — one pass, always
typst watch main.typ        # auto-recompile on save
typst compile deck.typ      # Touying slide deck — same single command
```

| Task | Built-in or Package |
|---|---|
| Author-year citations | Built-in `#cite`/`#bibliography`, CSL style |
| Decimal-ish regression tables | Built-in `#table`, right-aligned columns (no direct `dcolumn` equivalent) |
| Rule-based professional tables | Built-in `#table` + `table.hline()` |
| Cross-references (`@label`) | Built-in, no package needed |
| Theorem/lemma/proof environments | `ctheorems` |
| Presentations | `touying` |
| Diagrams (network graphs, trees) | `cetz` |

---

## Further Reading

- **Typst Documentation** (`https://typst.app/docs`) — the authoritative reference for every core function shown above (`table`, `figure`, `bibliography`, math mode).
- **Typst Universe** (`https://typst.app/universe`) — the canonical package repository; search a package name there for its full documentation, version history, and import snippet.
- **Touying Documentation** (`https://touying-typ.github.io`) — the authoritative guide for slide themes, animations (`#pause`, `#uncover`, `#only`), and speaker notes.
- Your target journal's **author guidelines page** may still only formally support Word/LaTeX submission — check before submission, since Typst is newer and not every venue has caught up, even though a Typst-produced PDF is indistinguishable from any other PDF at the point of submission.
