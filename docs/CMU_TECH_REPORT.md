# CMU School of Computer Science technical report

Publication checklist for *Formalization of Scott's Measurement Structures
and Linear Inequalities in Lean 4*.

## Report metadata

- **Series:** Carnegie Mellon University School of Computer Science Technical
  Report
- **Number:** `CMU-CS-26-XXX` (placeholder)
- **Date:** September 2026
- **Authors:** Lars Warren Ericson, Dana S. Scott, Vijay D'Silva, and Brian Milnes
- **Institutional address:** School of Computer Science, Carnegie Mellon
  University, Pittsburgh, PA 15213
- **arXiv cross-archive:** `cs.LO` / `math.LO`
- **Palomar registration:** `PALOMAR-YYYY-MM-DD-NNNNNN` (placeholder)

Lars Warren Ericson is an independent researcher, d/b/a Catskills Research
Company (`lars.ericson@catskillsresearch.com`). Dana S. Scott is affiliated with the
Computer Science Department, Carnegie Mellon University, Emeritus. Vijay D'Silva
is affiliated with Google Research. Brian Milnes is an Independent Researcher
affiliated with XBRLCloud.

## Build

```bash
lake exe cache get
lake build
bash scripts/build_arxiv_pdf.sh
```

The build produces:

- `arxiv.pdf` — CMU-formatted report PDF;
- `arxiv.tex` — generated complete LaTeX source (gitignored);
- `lean-listings/` and `figures/` — generated report inputs (gitignored);
- `dist/arxiv_submit.zip` — pdfLaTeX-ready cross-archive bundle, including
  `cmu-titlepage2.sty`.

The title page uses the report-mode layout from CMU's
`cmu-titlepage2.sty`. The same generated document is intended for the CMU
series and arXiv cross-archive.

## Before public release

1. Replace every `CMU-CS-26-XXX` occurrence with the assigned CMU report
   number.
2. Replace every `PALOMAR-YYYY-MM-DD-NNNNNN` occurrence after registration.
3. Replace the editorial placeholder in “Retrospective Remarks by Dana S.
   Scott” with Dana's approved text.
4. Confirm the author order, affiliations, September 2026 date, and
   correspondence email.
5. Run `python3 scripts/check_concordance.py`, `lake build`, and
   `bash scripts/build_arxiv_pdf.sh`.
6. Inspect the cover, abstract, table of contents, List of Figures,
   numbered figures, acknowledgments, references, Concordance methodology
   appendix, Lean module appendix, and the Scott 1964 source-paper appendix.
7. Upload `dist/arxiv_submit.zip` only after deleting prior arXiv submission
   files so the source set is replaced rather than merged.

