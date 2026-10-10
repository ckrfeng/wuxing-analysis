DIRECTED CYCLIC NETWORKS — SHORTENED PROOF EDITION
4 October 2026

Open proofs_compendium.pdf to read the revised manuscript.
In-text citations are bright red, including brackets and optional locators,
in both editable versions and the included PDF.

Editable sources
  proofs_compendium.tex     Modular master; edit individual files in proofs/.
  proofs_standalone.tex     Self-contained copy for the built-in LaTeX editor.
  references.bib            Ten cited and existence-checked references.
  shared_macros.tex         Original notation and theorem infrastructure.
  00_canonical_model.tex    Model equations and parameter contract.
  01_notation_and_assumptions.tex

The standalone copy embeds the sources and generated bibliography. It is an
alternative editing copy, not an input to the modular master. If you edit
the modular project, regenerate it before using it as an updated copy.

Compile the modular version with:
  latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex
or run pdflatex, bibtex, pdflatex, pdflatex in that order.
The included .bbl also permits compilation without rerunning BibTeX when
the bibliography has not changed. The standalone file needs no external
project inputs or BibTeX pass.

Review records
  CHANGE_REPORT.txt                What was shortened and what was retained.
  CITATION_VERIFICATION.txt        URLs, checked locations and access limits.
  VALIDATION.txt                   Compilation and source-conservation checks.
  review/proof_changes.patch       Full P01–P18 source differences.
  review/source_counts_and_hashes.json

Status and scope
This is an editorial revision of the user-specified Literature_Review
project. The original project was not modified. Earlier independent audit
verdicts apply to their original versions and are not represented as audits
of this revision. The source's P08 global-interior additions were already
awaiting independent audit, and remain so here.

P06 and P12–P18 had no completed proofs in the supplied project. They are
now concise, cited conditional frameworks with the unfinished calculations
explicitly identified. No nonlinear Hopf existence, Lyapunov-coefficient
sign, or heterogeneous quantitative estimate has been fabricated.

This ZIP is a focused proof manuscript, not a replacement archive of the
entire historical research workspace. Old audit PDFs, build debris, unused
literature entries, planning registries and numerical support archives are
not duplicated. They remain in the original project.
