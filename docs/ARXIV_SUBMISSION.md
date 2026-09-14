# arXiv submission metadata (Scott 1964 formalization)

Copy-paste fields for the arXiv web form. Regenerate the PDF and zip with
`bash scripts/build_arxiv_pdf.sh` before uploading `dist/arxiv_submit.zip`.

## Abstract (plain text, under 1920 characters)

See the `## Abstract` section in `arxiv.md` (same text appears in the PDF
`\begin{abstract}` block).

## Categories

| System | Recommendation |
| --- | --- |
| **arXiv primary** | `math.LO` (Logic) |
| **arXiv secondary** | `econ.TH` (Theoretical Economics); `cs.LO` (Logic in Computer Science) |
| **Optional arXiv** | `math.ST` (Statistics Theory) if emphasizing qualitative probability |

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
