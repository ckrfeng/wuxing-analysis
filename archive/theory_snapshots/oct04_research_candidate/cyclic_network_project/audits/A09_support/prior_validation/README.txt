P09 v1.0 DRAFT validation companion, 2026-10-03

This companion is corroboration and author review, NOT an independent A09 audit.
No theorem is promoted to VERIFIED or AUDITED by these computations or builds.

Source of truth: cyclic_network_project_P07_audited.zip, authenticated in
input_hashes.json and current_file_check.json. The baseline includes all current
P01-P05, P07, P08 and A01-A05, A07, A08 sources. Synced sources were not edited.

Reproduce computational checks with Python 3 and NumPy:
    python3 check_p09.py
The script writes exact_results.json, numerical_results.json, slope_results.json
and summary.json beside itself. It reads no project source and imports no prior
checker or prior result. The original rational DM field is entered directly;
exact rational third-order Taylor jets check its derivatives, and additive
Jacobian entries are checked against complex-step differentiation. Direct
matrix eigenvalues are matched to the full complex P04 spectrum with a
multiplicity-preserving bipartite matching, rather than a maximum-real-part
comparison. All labels are also checked by Fourier eigenvector residuals.

Coverage: n=5,6,7,8,9,10,12, every q in 1,...,n-1; 50 (n,q) pairs, 20 noncoprime;
six positive fixed parameter tuples, covering b<0, b=0, b>0; both signs of mu;
origin and all relevant local branches from the exact quadratic. Generic roots
use a cancellation-resistant expression. Both mu and physical g branch slopes
are evaluated by separate finite differences. No numerical continuation or
bifurcation detection package is used. No numerical assertion substitutes for
the proofs of the transverse IFT, local completeness or nonlinear stability.

Final run: 1260 exact-arithmetic checks; 2700 original-field/direct-matrix cases;
12 finite-difference slope checks (each checks both parameter orientations).
Floating-point tolerance for matched spectra is 1e-10 times the matrix scale;
recorded residuals and scaled discrepancies are in summary.json. These are
ordinary floating-point checks, not interval-certified enclosures.

internal_check_map.json maps the 17 requested analytical checks to exact P09
proof labels and line numbers. Two additional entries cover the exact orbital
center reduction and the full degenerate Lyapunov argument. This map records
author review only; an independent auditor must reconstruct the arguments.

The existing multi-file latexmk/pdfLaTeX toolchain builds proofs_compendium.tex.
Run from the extracted cyclic_network_project directory:
    latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex
The delivered compendium is 90 pages; P09 is on pages 71-77. Final build logs,
source/reference diagnostics, preservation checks, hashes and visual-review
records are included. The three underfull hboxes belong to the unchanged
historical dependency-map table. Final front matter and all seven P09 pages
were rendered and visually inspected. Baseline PDF text on pages 4-70 is unchanged.

The complete project archive is cyclic_network_project_P09_draft.zip, with
exactly the canonical cyclic_network_project/ root. It retains all 143 baseline
members. Only P09, manifest, registry, compendium source and regenerated PDF
change. No future A09 audit-only or P09-audited archive is produced.
P10 is not begun; no fold saddle-node, true bistability, basin or unfolding is
claimed. Frozen theorem/novelty records and all prior proofs/audits are unchanged.
