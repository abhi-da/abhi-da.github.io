---
layout: single
title: "Guide to Latex - PhD (Generated using AI)"
date: 2026-09-23
category: "Guide"
subcategory: "PhD"
tags: [PhD, Guide]
classes: wide

---
# LaTeX for Economics Research: A Practical Guide
### For PhD Students Working in Network Economics, Industrial Organization, Game Theory & Digital Piracy

This guide is meant to be plundered for snippets. Every example uses real economic notation and terminology (network externalities, Cournot competition, piracy deterrence, regression tables with fixed effects) instead of generic `foo`/`bar` placeholders, so the code is copy-paste-ready for actual papers, problem sets, and job market presentations. The package choices reflect general best practice across economics PhD programs rather than any single department's house style — if your program or target journal supplies its own class/style file, defer to that over the generic settings shown here.

> **Using Overleaf?** Everything below works unchanged, since Overleaf runs a full, current TeX Live distribution — every package mentioned in this guide (`booktabs`, `natbib`, `siunitx`, Beamer themes, etc.) is already installed, so there's nothing to download or configure locally. The two places where Overleaf changes your workflow rather than your code are: (1) you never type compile commands yourself — Overleaf recompiles automatically as you type (or on clicking "Recompile"), and (2) the underlying compiler and bibliography tool are picked from menus rather than flags. Both are called out inline wherever they come up (Section 5.1 on bibliographies, and the boilerplate uploads in Sections 4 and 6).

---

## Table of Contents

1. [Document Structure & Classes](#1-document-structure--classes)
2. [Theoretical Economics & Math Formatting](#2-theoretical-economics--math-formatting)
3. [Empirical Economics & Tables](#3-empirical-economics--tables)
4. [Figures & Graphics](#4-figures--graphics)
5. [References & Bibliography](#5-references--bibliography)
6. [Presentations (Beamer)](#6-presentations-beamer)

---

## 1. Document Structure & Classes

### 1.1 Choosing a Document Class

| Class | Use Case | Typical Economics Use |
|---|---|---|
| `article` | Single, self-contained document with no chapters | Journal papers, working papers, referee reports, problem sets |
| `report` | Longer documents needing chapters but not a full book | Term papers, PhD qualifying exam write-ups, technical reports for funders |
| `book` | Multi-part, multi-chapter, front/back matter | PhD dissertation/thesis, edited volumes |

**Rule of thumb:** use `article` for every stand-alone paper and job market paper draft — this is the structure journals like the *RAND Journal of Economics* or *Journal of Industrial Economics* expect, and it's also what most conference submission systems assume. Reserve `report` for multi-chapter but non-final documents (e.g., a term paper with several loosely connected sections), and reserve `book` for the dissertation itself, where you genuinely need front matter (title page, abstract, acknowledgments), numbered chapters, and possibly appendices per chapter. Switching classes mid-project is painful because section-numbering depth and some package behaviors change, so decide the class before you start writing.

```latex
\documentclass[12pt, a4paper]{article}   % single papers, JMP drafts
\documentclass[12pt, a4paper]{report}    % term papers with chapters
\documentclass[12pt, a4paper, oneside]{book}  % PhD dissertation
```

### 1.2 Essential Preamble for Economics Papers

```latex
\documentclass[12pt, a4paper]{article}

% --- Encoding & fonts ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}          % or newtxtext/newtxmath for a Times-like look

% --- Math ---
\usepackage{amsmath, amssymb, amsfonts, amsthm}
\usepackage{mathtools}        % extends amsmath (e.g. \DeclarePairedDelimiter)
\usepackage{bm}               % bold math symbols, e.g. \bm{\theta}

% --- Tables & floats ---
\usepackage{booktabs}         % professional horizontal rules
\usepackage{dcolumn}          % decimal-aligned columns for regression tables
\usepackage{siunitx}          % alternative/complement to dcolumn
\usepackage{multirow}
\usepackage{array}
\usepackage{threeparttable}   % table notes that respect column width
\usepackage{longtable}        % tables spanning multiple pages

% --- Graphics ---
\usepackage{graphicx}
\usepackage{subcaption}       % subfigures, e.g. network diagrams side-by-side
\usepackage{float}

% --- Bibliography (economics standard: natbib + author-year) ---
\usepackage[authoryear, round]{natbib}

% --- Cross-referencing & hyperlinks ---
\usepackage{hyperref}
\usepackage[capitalise]{cleveref}

% --- Spacing / layout ---
\usepackage{setspace}
\onehalfspacing                % most econ departments want 1.5 or double spacing
\usepackage[margin=1in]{geometry}

% --- Misc economics conveniences ---
\usepackage{enumitem}          % control spacing in lists (assumptions, propositions)
\usepackage{xcolor}            % highlighting derivations/comments during drafting
```

> **Why `natbib` and not `biblatex` here?** See Section 5 — it remains the de facto standard in economics because AEA/Econometrica-style `.bst` files are built around it.

> **A note on package load order:** `hyperref` should almost always be loaded *last* (or second-to-last, just before `cleveref`), since it redefines many internal LaTeX commands that other packages expect to modify first. Loading it early is one of the most common sources of mysterious compilation errors for beginners. `cleveref` specifically must be loaded *after* `hyperref`.

### 1.3 Document Hierarchy

```latex
\section{Introduction}
\subsection{Related Literature on Platform Competition}
\subsubsection{Two-Sided Markets}
\paragraph{Network effects.} Indirect network effects arise when...
```

| Command | Numbering Depth | Typical Content |
|---|---|---|
| `\section{}` | 1 | Introduction, Model, Data, Results, Conclusion |
| `\subsection{}` | 1.1 | Equilibrium Concept, Identification Strategy |
| `\subsubsection{}` | 1.1.1 | Specific lemma derivations, robustness sub-checks |
| `\paragraph{}` | unnumbered, run-in | Short asides, definitions within a subsubsection |

### 1.4 Table of Contents

```latex
\tableofcontents
\newpage
```

For dissertations, also generate lists of tables/figures:

```latex
\listoftables
\listoffigures
```

> **Note:** most journal-style papers (`article` class, single-spaced or 1.5-spaced, under ~40 pages) don't include a table of contents at all — reserve `\tableofcontents` for term papers, dissertation chapters, and long technical reports. Also remember to compile **twice** after adding or changing headings: the first pass writes the section titles/page numbers to an auxiliary `.aux`/`.toc` file, and the second pass reads that file back in to render the ToC correctly.

---

## 2. Theoretical Economics & Math Formatting

### 2.1 The `amsmath` / `amssymb` / `amsfonts` Trio

- **`amsmath`**: the workhorse package. It gives you multi-line equation environments (`align`, `gather`, `cases`), improved fraction/operator spacing, and `\text{}` for inserting normal (non-italic) words inside math mode.
- **`amssymb`**: extra symbols built on top of `amsfonts`' fonts — `\leq`, `\geq`, `\succsim` (preference orderings), `\subseteq`, and dozens of relation/arrow symbols you'll otherwise be unable to typeset.
- **`amsfonts`**: the underlying font package that supplies blackboard bold (`\mathbb{R}` for the real line, `\mathbb{N}` for a player/agent index set) and Fraktur (`\mathfrak{F}` for, e.g., a filtration in a stochastic pricing model). In practice `amssymb` automatically loads `amsfonts`, so listing both is a common (harmless) redundancy for clarity.

```latex
\usepackage{amsmath, amssymb, amsfonts}

% Common economics symbol shortcuts
\newcommand{\R}{\mathbb{R}}
\newcommand{\E}{\mathbb{E}}          % expectation operator
\newcommand{\N}{\mathbb{N}}          % player/agent index set
\newcommand{\argmax}{\operatorname*{arg\,max}}
\newcommand{\argmin}{\operatorname*{arg\,min}}
```

### 2.2 Inline vs. Display Math

```latex
% Inline math: use for short expressions within a sentence
Firm $i$ chooses price $p_i \in \R_+$ to maximize profit $\pi_i(p_i, p_{-i})$.

% Display math: use for the "headline" equation you want the reader to pause on
\[
    \pi_i(p_i, p_{-i}) = (p_i - c_i)\, D_i(p_i, p_{-i})
\]
```

Prefer `\[ ... \]` over the legacy `$$ ... $$` — the latter has spacing bugs under `amsmath`.

### 2.3 Multi-Line Equations: A Game Theory Optimization Example

A classic Cournot-with-network-effects best-response derivation using `align`:

```latex
\begin{align}
    \max_{q_i \geq 0} \quad & \pi_i(q_i, q_{-i}) = \left[ a - b\left(q_i + \sum_{j \neq i} q_j\right) + \gamma \, x_i \right] q_i - c\, q_i \label{eq:cournot-profit} \\
    \text{F.O.C.:} \quad & a - 2bq_i - b\sum_{j \neq i} q_j + \gamma x_i - c = 0 \label{eq:cournot-foc} \\
    \Rightarrow \quad & q_i^{*} = \frac{a - c + \gamma x_i - b\sum_{j \neq i} q_j}{2b} \label{eq:cournot-br}
\end{align}
```

Here `x_i` denotes a network-adoption externality term — natural in a network economics context. Two mechanics worth internalizing: the single `&` on each line marks the alignment point (here, right after the `\quad`, so every right-hand side lines up vertically down the page), and `\\` ends each line. Every `align` line gets its own equation number by default — attach `\label{}` only to lines you actually plan to reference, and consider `\notag` on a line if you want it unnumbered without switching the whole block to `align*`. `align*` suppresses equation numbers entirely when you don't need to reference any line later:

```latex
\begin{align*}
    U_i(\sigma_i, \sigma_{-i}) &= \sum_{s \in S} p(s \mid \sigma) \, u_i(s) \\
    \sigma_i^{*} &\in \argmax_{\sigma_i \in \Delta(S_i)} U_i(\sigma_i, \sigma_{-i}^{*})
\end{align*}
```

Use `\label{}` on any line you'll reference with `\eqref{eq:cournot-br}` in the text (e.g., "Substituting the best response from \eqref{eq:cournot-br} into...").

### 2.4 Integration by Parts (Pedagogical Notation)

For deriving expected consumer surplus or hazard-rate expressions in piracy-deterrence models, here is the classic pedagogical form of integration by parts (the version many intro courses teach before moving to the more common $\int u\,dv = uv - \int v\,du$ shorthand):

```latex
\[
    uv = u \int v - \int \left( du \int v \right)
\]
```

A worked example inside an `align` block, e.g. integrating a hazard function for time-to-detection of a pirated good:

```latex
\begin{align*}
    \int_0^T t \, f(t) \, dt
    &= \Big[ t \cdot F(t) \Big]_0^T - \int_0^T F(t)\, dt \\
    &\quad \text{(using } uv = u\!\int v - \int\!\big(du\!\int v\big) \text{ with } u = t,\ dv = f(t)\,dt \text{)}
\end{align*}
```

### 2.5 Theorems, Lemmas, and Proofs

Set these up once in the preamble with `amsthm`:

```latex
\usepackage{amsthm}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{assumption}[theorem]{Assumption}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

A few mechanics worth understanding rather than just copying: `\theoremstyle{plain}` renders the body in italics (for results), `{definition}` renders it upright (for definitions/assumptions, which readers shouldn't mentally parse as "claims"), and `{remark}` is similar but typically de-emphasized. The `[section]` argument on `\newtheorem{theorem}{Theorem}[section]` resets the theorem counter every time a new `\section` starts, so you get "Theorem 2.1" instead of a single running count through the whole paper. The `[theorem]` argument on the later `\newtheorem` calls (e.g., `\newtheorem{lemma}[theorem]{Lemma}`) makes lemmas, propositions, and corollaries **share** the theorem counter, so numbering runs Theorem 2.1, Lemma 2.2, Proposition 2.3 in document order — which is what most economics journals expect, rather than separate counters for each type.

Usage in the body:

```latex
\begin{assumption}[Homogeneous Piracy Cost]
    \label{as:homogeneous-cost}
    All consumers face an identical marginal cost of piracy, $\kappa > 0$, independent of network size $n$.
\end{assumption}

\begin{proposition}
    \label{prop:unique-equilibrium}
    Under Assumption~\ref{as:homogeneous-cost}, there exists a unique symmetric Bayesian Nash equilibrium in which the platform sets price $p^{*} = \dfrac{a + c + \gamma \bar{x}}{2}$.
\end{proposition}

\begin{proof}
    Suppose, for contradiction, that two distinct symmetric equilibria $p_1^{*} \neq p_2^{*}$ exist. By the strict concavity of $\pi_i(\cdot)$ established in \eqref{eq:cournot-profit}, the best-response correspondence is single-valued, a contradiction. \qedhere
\end{proof}
```

`\qedhere` places the ∎ symbol immediately at the end of the last line rather than on a new line — useful when a proof ends mid-equation.

---

## 3. Empirical Economics & Tables

### 3.1 The Philosophy of Publication-Quality Tables

Economics journals (AER, QJE, Econometrica) follow a shared house style:

- **No vertical rules.** Vertical lines clutter the table and are considered amateurish.
- **Minimal horizontal rules** — typically three: top, one after the header, and bottom. This is exactly what `booktabs` enforces.
- **Decimal alignment** in numeric columns so that standard errors line up under coefficients.
- **Notes below the table**, not above, explaining significance stars, standard error clustering, and sample restrictions.

Never use the default `\hline`-heavy tables from `tabular`. Always load `booktabs`.

The underlying logic: a table's job is to let the eye compare numbers quickly, and every extra ruled line is visual noise competing with that goal. `booktabs` enforces sensible defaults — its rules are drawn at different weights and with built-in spacing, which is why `\toprule`/`\bottomrule` look noticeably better than a hand-drawn `\hline` even though both nominally "just draw a line."

### 3.2 `booktabs` Basics

```latex
\usepackage{booktabs}

\begin{table}[htbp]
    \centering
    \caption{Summary Statistics: Platform-Level Network Data}
    \label{tab:summary-stats}
    \begin{tabular}{lccc}
        \toprule
        Variable & Mean & Std. Dev. & N \\
        \midrule
        Active users (000s)     & 542.3  & 118.7 & 1{,}204 \\
        Piracy incidence rate   & 0.184  & 0.091 & 1{,}204 \\
        Platform price (\$)     & 9.99   & 2.14  & 1{,}204 \\
        \bottomrule
    \end{tabular}
\end{table}
```

Notice `1{,}204` rather than plain `1,204`: LaTeX by default adds a small extra space after a comma inside math-adjacent contexts, so wrapping the comma in braces (`{,}`) suppresses that spacing and keeps the thousands separator looking like ordinary text.

### 3.3 Regression Tables with `dcolumn` / `siunitx`

**Option A — `dcolumn`** (classic, works well with `estout`/`esttab` output from Stata):

> **Common pitfall:** the `D{.}{.}{3.3}` column type aligns strictly on the decimal point, so a cell like `0.412^{***}` will actually misalign slightly because `dcolumn` doesn't know to ignore the superscript stars when computing alignment. In practice, most people either (a) let Stata's `esttab, star` produce the whole table body pre-formatted and just wrap it in the `d` column type, accepting the tiny visual offset, or (b) switch that specific column to plain `c` alignment when stars are present and rely on `booktabs` rules alone for tidiness. Don't spend hours fighting pixel-perfect alignment here — reviewers care about correctness, not sub-millimeter column alignment.

```latex
\usepackage{dcolumn}
\usepackage{threeparttable}
\newcolumntype{d}[1]{D{.}{.}{#1}}

\begin{table}[htbp]
    \centering
    \caption{Effect of Network Size on Piracy Take-Up}
    \label{tab:reg-main}
    \begin{threeparttable}
    \begin{tabular}{l d{3.3} d{3.3} d{3.3}}
        \toprule
        & \multicolumn{1}{c}{(1)} & \multicolumn{1}{c}{(2)} & \multicolumn{1}{c}{(3)} \\
        & \multicolumn{1}{c}{OLS} & \multicolumn{1}{c}{IV} & \multicolumn{1}{c}{Poisson} \\
        \midrule
        Network size ($\ln n_i$)  & 0.412^{***} & 0.389^{***} & 0.401^{***} \\
                                   & (0.087)     & (0.102)     & (0.093) \\
        Price ($p_i$)              & -0.215^{**} & -0.198^{**} & -0.207^{**} \\
                                   & (0.094)     & (0.088)     & (0.091) \\
        \midrule
        Firm FE                   & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} \\
        Year FE                   & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} & \multicolumn{1}{c}{Yes} \\
        Observations               & \multicolumn{1}{c}{1{,}204} & \multicolumn{1}{c}{1{,}204} & \multicolumn{1}{c}{1{,}204} \\
        \bottomrule
    \end{tabular}
    \begin{tablenotes}
        \small
        \item \textit{Notes:} Standard errors clustered at the platform level in parentheses. $^{*}p<0.10$, $^{**}p<0.05$, $^{***}p<0.01$.
    \end{tablenotes}
    \end{threeparttable}
\end{table}
```

> **Why `threeparttable`:** the `tablenotes` environment used for the notes line below the table is provided *by* the `threeparttable` package, and only works when the whole `tabular` is nested inside `\begin{threeparttable}...\end{threeparttable}`. Its main benefit over just typing the notes as ordinary text below the table is that the note text automatically wraps to the same width as the table itself, rather than running the full width of the page — which looks wrong for a narrow table.

**Option B — `siunitx`** (more modern, more configurable, handles negative signs and scientific notation gracefully):

```latex
\usepackage{siunitx}
\sisetup{table-format=1.3, detect-weight=true, detect-family=true}

\begin{tabular}{l S S S}
    \toprule
    {} & {OLS} & {IV} & {Poisson} \\
    \midrule
    $\ln n_i$ & 0.412 & 0.389 & 0.401 \\
    {}        & (0.087) & (0.102) & (0.093) \\
    \bottomrule
\end{tabular}
```

Two things to note in the `siunitx` snippet: the `S` column type (from `siunitx`, distinct from plain `S`-as-in-"strong" text) automatically detects and aligns on the decimal point *and* correctly handles non-numeric content — but any cell that isn't a plain number (like the header text `OLS` or an empty cell) must be wrapped in braces `{...}` so `siunitx` treats it as literal text rather than attempting (and failing) to parse it as a number. `table-format=1.3` tells `siunitx` to reserve space for exactly 1 digit before the decimal and 3 after, so all columns align even before any content is typeset — adjust this to match your actual coefficient magnitudes (e.g., `2.3` if coefficients can run into the tens).

### 3.4 `\multicolumn` and `\multirow`

```latex
\usepackage{multirow}

\begin{table}[htbp]
    \centering
    \caption{Piracy Deterrence by Enforcement Regime and Market}
    \label{tab:multirow-example}
    \begin{tabular}{llcc}
        \toprule
        \multirow{2}{*}{Enforcement Regime} & \multirow{2}{*}{Market} & \multicolumn{2}{c}{Piracy Rate} \\
        \cmidrule(lr){3-4}
        & & Pre-Policy & Post-Policy \\
        \midrule
        \multirow{2}{*}{Strict (DMCA-style)} & Streaming & 0.24 & 0.11 \\
                                              & Software  & 0.31 & 0.14 \\
        \multirow{2}{*}{Lenient}             & Streaming & 0.29 & 0.26 \\
                                              & Software  & 0.38 & 0.35 \\
        \bottomrule
    \end{tabular}
\end{table}
```

`\cmidrule(lr){3-4}` draws a partial rule under columns 3–4 only, with slight left/right trimming — the `booktabs`-approved way to group sub-headers (never use `\cline`).

---

## 4. Figures & Graphics

### 4.1 Inserting Graphics with `graphicx`

```latex
\usepackage{graphicx}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.75\textwidth]{figures/network_topology.pdf}
    \caption{Simulated Network Topology Under Preferential Attachment ($\gamma = 2.1$)}
    \label{fig:network-topology}
\end{figure}
```

- Always compile figures as **vector PDF** (from R's `ggsave(..., device = "pdf")` or Stata's `graph export ..., as(pdf)`), never PNG/JPEG for line plots or network diagrams — this keeps them crisp at any zoom.
- Reference figures in text with `Figure~\ref{fig:network-topology}` or, with `cleveref`, simply `\cref{fig:network-topology}`. The `~` (a non-breaking space) prevents "Figure" and its number from being split across a line break.
- **On Overleaf:** create a folder named `figures` in the file tree (right-click → New Folder) and upload your PDF/image files into it, so the relative path `figures/network_topology.pdf` in `\includegraphics` resolves correctly — Overleaf's file tree mirrors the relative paths you write in the `.tex` source exactly.

### 4.2 Side-by-Side Subfigures (e.g., comparing network structures)

```latex
\usepackage{subcaption}

\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{figures/network_core.pdf}
        \caption{Core-periphery structure}
        \label{fig:core-periphery}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \includegraphics[width=\textwidth]{figures/network_random.pdf}
        \caption{Random graph benchmark}
        \label{fig:random-graph}
    \end{subfigure}
    \caption{Observed vs. Simulated Network Structures}
    \label{fig:network-comparison}
\end{figure}
```

`\hfill` between the two `subfigure` blocks pushes them apart to fill the available horizontal space evenly — without it, the two subfigures would sit flush against each other with no gap. Each subfigure also gets its own `\label`, so you can refer to `\cref{fig:core-periphery}` specifically or `\cref{fig:network-comparison}` for the pair as a whole.

### 4.3 Float Positioning Options

| Specifier | Meaning | When to Use |
|---|---|---|
| `h` | "here", approximately | Small figures that should stay near the surrounding text |
| `t` | top of page | Default preference for most journal figures |
| `b` | bottom of page | Good for wide tables that would otherwise break text flow |
| `p` | dedicated float page | Large figures/tables (e.g., a full-page regression table) |
| `htbp` | try all, in order | The safe, most commonly used combination |

```latex
\begin{figure}[htbp]   % LaTeX will try h, then t, then b, then p
    ...
\end{figure}
```

**Tip:** If LaTeX ignores your `[h]` and pushes the float away, load `\usepackage{float}` and use `[H]` (capital H) to force exact placement — but use sparingly, as it can create ugly whitespace.

---

## 5. References & Bibliography

### 5.1 The BibTeX Workflow

1. Maintain a `references.bib` file with entries like:

```bibtex
@article{katz1985network,
    author  = {Katz, Michael L. and Shapiro, Carl},
    title   = {Network Externalities, Competition, and Compatibility},
    journal = {American Economic Review},
    year    = {1985},
    volume  = {75},
    number  = {3},
    pages   = {424--440}
}

@article{peitz2006piracy,
    author  = {Peitz, Martin and Waelbroeck, Patrick},
    title   = {Why the Music Industry May Gain from Free Downloading},
    journal = {International Journal of Industrial Organization},
    year    = {2006},
    volume  = {24},
    number  = {5},
    pages   = {907--913}
}
```

2. Compile.

**On Overleaf:** upload `references.bib` via the file-tree "Upload" button (or create it directly in the project), keep `\bibliography{references}` pointing at it, and just click **Recompile** — Overleaf detects the `\bibliography{}` command and automatically runs the BibTeX pass for you behind the scenes, no manual command needed. The one setting worth checking is under the project's **Menu → Settings → Bibliography Processor**: it should be set to `bibtex` (the default and correct choice for `natbib`-based papers); only switch it to `biber` if you deliberately move to `biblatex` in Section 5.2 below. If citations show up as `[?]` or "undefined," a plain Recompile a second time usually resolves it, since — same as local compiling — the citation list needs one extra pass to resolve after the `.bib` file changes.

**Compiling locally** (outside Overleaf), run in this order, whether by hand or via `latexmk`:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### 5.2 `natbib` vs. `biblatex`

| | `natbib` | `biblatex` |
|---|---|---|
| Standard in economics? | **Yes** — matches AEA, Econometrica, RAND house styles | Rare in econ; common in humanities/sciences |
| Backend | BibTeX (or `bibtex8`) | Biber (more powerful, slower) |
| Citation commands | `\citet`, `\citep`, `\citeauthor`, `\citeyear` | `\textcite`, `\parencite`, similar but different names |
| Journal `.bst` file support | Extensive (most econ journals supply a `.bst`) | Poor — journals rarely provide `.bbx`/`.cbx` files |
| Recommendation | **Use this for economics papers** | Use only if a specific journal/template mandates it |

Preamble setup for `natbib`:

```latex
\usepackage[authoryear, round]{natbib}
\bibliographystyle{aer}     % or apalike, econometrica, chicago
...
\bibliography{references}
```

### 5.3 `\citet` vs. `\citep`

```latex
% Textual citation — reads as part of the sentence
\citet{katz1985network} show that network externalities can generate multiple equilibria.
% Output: "Katz and Shapiro (1985) show that..."

% Parenthetical citation — for supporting evidence at the end of a clause
Network externalities can generate multiple equilibria \citep{katz1985network}.
% Output: "...multiple equilibria (Katz and Shapiro, 1985)."

% Multiple sources
The piracy-deterrence literature is well established \citep{peitz2006piracy, katz1985network}.

% Citing with a specific page/note
\citet[p.~430]{katz1985network} formalize this as a coordination game.
```

---

## 6. Presentations (Beamer)

### 6.1 Complete Boilerplate Template

```latex
\documentclass[aspectratio=169]{beamer}

\usetheme{Madrid}
\usecolortheme{dolphin}

\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb}
\usepackage{graphicx}
\usepackage[authoryear, round]{natbib}

\title[Network Effects \& Piracy]{Network Effects and the Economics of Digital Piracy}
\subtitle{Job Market Paper}
\author[A.\ Researcher]{Your Name}
\institute[IGIDR]{Indira Gandhi Institute of Development Research}
\date{\today}

\begin{document}

\frame{\titlepage}

\begin{frame}{Outline}
    \tableofcontents
\end{frame}

\section{Motivation}
\begin{frame}{Motivation}
    \begin{itemize}
        \item Digital platforms exhibit strong network externalities.
        \pause
        \item Piracy interacts with network size in non-obvious ways.
        \pause
        \item This paper models the joint determination of price, network adoption, and piracy incidence.
    \end{itemize}
\end{frame}

\section{Model}
\begin{frame}{Setup}
    Firm $i$ sets price $p_i$ to maximize
    \[
        \pi_i(p_i) = (p_i - c)\, D_i(p_i, x_i) - \kappa \, \rho(p_i)
    \]
    where $x_i$ is network size and $\rho(p_i)$ is the piracy rate.
\end{frame}

\section{Results}
\begin{frame}{Main Result}
    \begin{block}{Proposition}
        Under mild regularity conditions, equilibrium price is decreasing in the piracy-deterrence cost $\kappa$.
    \end{block}
\end{frame}

\section{Conclusion}
\begin{frame}{Conclusion}
    \begin{itemize}
        \item Network effects amplify the welfare cost of piracy enforcement.
        \item Policy implication: uniform DMCA-style enforcement may be suboptimal across markets of different network density.
    \end{itemize}
\end{frame}

\begin{frame}{References}
    \bibliographystyle{apalike}
    \bibliography{references}
\end{frame}

\end{document}
```

You can use `\citet{}`/`\citep{}` inside any frame body exactly as in a paper (Section 5.3). On Overleaf, just upload `references.bib` alongside your `.tex` file and hit Recompile — Overleaf runs the necessary BibTeX pass automatically, same as for a regular paper (Section 5.1). Compiling locally, the same `pdflatex → bibtex → pdflatex → pdflatex` sequence applies — Beamer decks with citations need the extra passes just like papers do.

### 6.2 Best Professional Themes for Academic Economics

**Presentation (structural) themes:**

| Theme | Character | Good For |
|---|---|---|
| `Madrid` | Clean header bar with section navigation dots | General seminar talks |
| `Boadilla` | Minimal, sidebar-free, understated | Job talks — very safe, conservative choice |
| `metropolis` | Modern flat design (requires separate package `beamertheme-metropolis`) | Talks aiming for a contemporary look |
| `CambridgeUS` | Traditional, high information density | Long technical seminars with many results |

**Color themes:**

| Color Theme | Palette |
|---|---|
| `dolphin` | Muted blue/gray — professional, low-key |
| `seahorse` | Soft gray-green |
| `whale` | Deep blue, high contrast |
| `default` | Beamer blue — safe but generic |

```latex
\usetheme{Boadilla}
\usecolortheme{seahorse}
```

For `metropolis`, install via your TeX distribution's package manager and use:

```latex
\usetheme{metropolis}
\usepackage{fontawesome5} % metropolis pairs well with icon-based bullets
```

### 6.3 Theme Galleries (Browse Before You Commit)

- Beamer theme matrix (official-style gallery): `https://hartwork.org/beamer-theme-matrix/`
- Overleaf Beamer theme gallery: `https://www.overleaf.com/gallery/tagged/presentation`
- `metropolis` theme repository and preview: `https://github.com/matze/mtheme`

### 6.4 Overlays, `\pause`, and Frame Structure

```latex
\begin{frame}{Sequential Reveal of Assumptions}
    \begin{itemize}
        \item Assumption 1: Consumers are risk-neutral. \pause
        \item Assumption 2: The platform has full commitment power. \pause
        \item Assumption 3: Piracy technology is common knowledge.
    \end{itemize}
\end{frame}

% Finer-grained control with <> overlay specifications
\begin{frame}{Overlay Specification Example}
    \begin{itemize}
        \item<1-> This appears from slide 1 onward.
        \item<2-> This appears from slide 2 onward.
        \item<3> This appears only on slide 3.
        \item<only@2> This appears \emph{only} while on slide 2, then disappears.
    \end{itemize}
\end{frame}
```

`\pause` is the simplest tool: it splits everything before it from everything after it into separate reveal steps, and you can stack several in one frame. The `<...>` overlay syntax gives finer control when `\pause` isn't expressive enough: `<2->` means "visible from slide 2 onward and stays visible," `<3>` means "visible only on slide 3," and `<only@2>` additionally removes the item from the layout (rather than just making it invisible) outside slide 2 — useful when you want a later bullet to shift upward to fill the gap. Mixing `\pause` and `<>` overlays in the same list can produce confusing numbering, so pick one style per frame.

### 6.5 Title Page Fields

The title page is generated automatically from preamble metadata via `\frame{\titlepage}` (or `\maketitle` inside a frame) — see the boilerplate above for the full set of `\title`, `\subtitle`, `\author`, `\institute`, `\date` fields.

---

## Quick-Reference Cheat Sheet

```latex
% On Overleaf: just click Recompile — it handles the bibliography
% pass automatically whenever \bibliography{} is present.

% Compiling locally instead:
pdflatex main && bibtex main && pdflatex main && pdflatex main   % paper with bibliography
pdflatex slides.tex                                              % Beamer deck (run twice if using \tableofcontents or citations)
```

| Task | Package |
|---|---|
| Author-year citations | `natbib` |
| Decimal-aligned regression tables | `dcolumn` or `siunitx` |
| Rule-based professional tables | `booktabs` |
| Cross-references (`\cref`) | `cleveref` |
| Table notes that wrap correctly | `threeparttable` |
| Presentations | `beamer` |

---

## Further Reading

- **The Not So Short Introduction to LaTeX2e** (`https://tobi.oetiker.ch/lshort/lshort.pdf`) — the standard general LaTeX primer if any syntax here feels unfamiliar.
- **The `amsmath` User's Guide** — the authoritative reference for every math environment shown in Section 2.
- **CTAN** (`https://ctan.org`) — the canonical repository for every package mentioned above; search a package name there for its full documentation and options.
- Your target journal's **author guidelines page** almost always lists a required `.cls`/`.bst` file — check before submission, since journal house styles override the generic conventions in this guide.
