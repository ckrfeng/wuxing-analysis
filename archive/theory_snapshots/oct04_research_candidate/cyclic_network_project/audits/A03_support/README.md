# A03 independent audit delivery

Main verdict: VERIFIED. No required correction to the exact P03 v1.0 audited.
P04 is cleared after A03 audit closure is recorded; it was not begun.

Audited P03 full-file SHA-256:
0f87f315817429ddb949af5bc6d38db32a0cb6a8f7715dfe941840becd527776

The audit-only ZIP adds only the A03 TeX source, a 12-page PDF reading copy,
and this support directory under cyclic_network_project/audits/. It contains
no replacement proof, manifest, registry, compendium, or later module.
All 60 extracted supplied-project members remain byte-identical to the input
ZIP. P03 is unchanged. Current status files still contain the pre-audit DRAFT
status; this audit supplies the independent VERIFIED verdict.

## Read and compile

The source is standalone and needs no project macros. From audits/, run:

    latexmk -pdf -interaction=nonstopmode -halt-on-error A03_origin_and_linearization.tex

The delivered PDF compiled with pdfLaTeX / TeX Live 2026 and latexmk 4.88.
Final build: no warnings, undefined references, overfull or underfull boxes.
All rendered pages were inspected; the final pagination has 12 pages.
The line-disposition table covers P03 lines 1–433 exactly once.

## Reproduce independent exact checks

From this support directory, using ordinary Python 3 with its standard library:

    python3 checks/exact_jacobian_check.py
    python3 checks/exact_origin_check.py

Each script writes its result JSON alongside itself. All arithmetic is exact.
The Jacobian checker evaluates the original five-term field with rational
automatic differentiation. It passes 656 cases / 29,820 full matrix entries
across every q for n=5,6,8, including signed nonsynchronous states, positive
and negative synchrony, all collisions and cancellations, 48 origins, 112
actual nonzero equilibria, and 3,020 row-sum comparisons. Overlapping check
counts must not be added as independent samples.
The origin checker uses sparse Leibniz determinants and rational row reduction.
Finite checking corroborates, and does not replace, the proofs in A03.

## Reproduce the original P03 validation report

The matching pre-existing companion was found at output/p03/P03_validation_support.zip.
Companion ZIP SHA-256:
cedf6a8ceae60fcca10020ee0681d9d5fe4db9c4f117d7cc4b47909158860518
Portable original checker SHA-256:
73784fd269f445a80639175b8901610e89a517469d69ddc5d397200dc5412bbb

The inspected checker was copied and rerun with Python 3.12.14 / NumPy 2.3.5.
Its full exact and floating result dictionaries match the original report.
The original_* files are preserved comparison records; report.json and
summary.json are the rerun. To rerun with a supplied project folder:

    python3 prior_validation/check_p03.py /absolute/path/to/cyclic_network_project

This checker needs NumPy and reads the canonical/notation hashes. It writes
report.json and summary.json alongside itself. Historical residual matching
is supplementary reproducibility evidence, not proof or a universal bound.

## Closure and limits

Record A03 acceptance against the exact P03 digest above in the appropriate
project status records. No mathematical correction is needed. If a separately
authorized metadata update changes the P03 header, retain the audited digest
and explain that metadata-only difference; do not silently substitute a new
proof. A substantive proof revision requires review of the changed version.
P09 still additionally depends on P04. Nonlinear boundary stability, Hopf,
transcritical bifurcation, positive-equilibrium spectrum, normality and later
results remain outside this audit. Literature-priority status is unchanged.
