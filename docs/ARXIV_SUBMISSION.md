# arXiv submission metadata (Scott 1964 formalization)

Copy-paste fields for the arXiv web form. Regenerate the PDF and zip with
`bash scripts/build_arxiv_pdf.sh` before uploading `dist/arxiv_submit.zip`.

## Abstract (plain text, under 1920 characters)

See the `## Abstract` section in `arxiv.md` (same text appears in the PDF
`\begin{abstract}` block).

## Categories

### What the submit form actually shows

arXiv’s **primary category** picker is organized by **archive** (Mathematics, Computer Science, …). **Economics (`econ.*`) is its own archive**, not a submenu under Math or CS. On a first submission as `math.LO` or `cs.LO`, the dropdown often **does not list any `econ.*` codes**—that is normal, not an error.

Use at submit time:

| Field | Use |
| --- | --- |
| **Primary** | `math.LO` (Logic) — recommended for this formalization |
| **Secondary / cross-list at submit** | `cs.LO` if the UI offers a second category in Math/CS |

**`econ.TH` (Theoretical Economics)** exists on arXiv ([taxonomy](https://arxiv.org/category_taxonomy), [econ.TH listings](https://arxiv.org/list/econ.TH/recent)) but is usually added **after** announcement via the [cross-list tool on your user page](https://info.arxiv.org/help/cross.html), and only if your account is **endorsed for the Economics archive** (same endorsement rules as any new archive). If you are not endorsed for `econ`, Economics will not appear anywhere in the picker.

Do **not** make `econ.TH` the primary category unless you intend a full Economics-archive submission and have (or can obtain) econ endorsement.

For measurement / utility / qualitative probability audience without `econ.TH`, rely on **MSC** (below) and the abstract keywords—not on an econ cross-list.

| System | Recommendation |
| --- | --- |
| **arXiv primary (submit)** | `math.LO` |
| **arXiv secondary (submit, if offered)** | `cs.LO` |
| **Optional cross-list (post-submit)** | `econ.TH` if endorsed and appropriate |
| **Optional cross-list (post-submit)** | `math.ST` if emphasizing qualitative probability |

**MSC 2020** (semicolon-separated for arXiv): `91C05; 15A39; 91B16; 68V20`

- `91C05` — Measurement theory, utility theory
- `15A39` — Linear inequalities
- `91B16` — Utility and decision theory
- `68V20` — Formalization of mathematics (Lean / proof assistants)

**ACM 1998** (semicolon-separated): `J.2; I.2.3; F.4.1`

- `J.2` — Physical sciences and engineering (measurement / mathematical psychology)
- `I.2.3` — Deduction and theorem proving
- `F.4.1` — Mathematical logic

## Compiler

pdfLaTeX (`00README.json` sets `"compiler": "pdflatex"`).

## Repository

https://github.com/catskillsresearch/scott1964
