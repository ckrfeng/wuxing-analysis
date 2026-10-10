A08 independent audit - 3 October 2026

Audited exact P08 v1.0, 39,287 bytes, 846 lines.
P08 SHA-256: d21a77de84df4c40c2995d30ab740130795adca6c72f52fef9453ad5ddfb18ac
Input ZIP SHA-256: 3cac0e6676575e1c652454a9e28418c04ac5a553d4550c6f8d27f2d873e71e44

VERDICTS
MB FOUNDATION: VERIFIED
MB SPECTRAL: VERIFIED
SAME-TUPLE COMPARISON: MINOR REVISION
PARITY/OBSTRUCTION: VERIFIED
OVERALL: MINOR REVISION

SOLE REQUIRED CORRECTION E01
P08 lines 534-535 incorrectly include n=8 among sizes where the universal
witness selects MB representative 1. It selects representative 2 (labels
2 and 6) at n=8; representative 1 is correct for n=5,6,7.
The exact replacement and proof are on audit page 1. The main all-size
opposite-stability theorem is unaffected.

CURRENT-INPUT POLICY
The supplied ZIP and its current manifest are authoritative. A stale local
P08 placeholder was excluded. All 98 archive members and all 21 selected
inputs were authenticated. Source line numbers count the exact archive
member, including comments and blanks. The current manifest slug determines
the A08_matched_bilinear_analysis basename.

MATHEMATICAL EVIDENCE
The standalone audit reconstructs the ODE, spectral, selection, realization,
parity and openness arguments. It covers all 846 source lines in 65 ranges.
Theorems do not rely on numerical checks. Both models use the same positive
physical tuple, each at its own explicitly named positive equilibrium.

INDEPENDENT CHECKS
independent_check.py is new audit code; it imports no original checker.
Run: python3 independent_check.py
Requires Python 3 and NumPy; the run used Python 3.12.14 and NumPy 2.3.5.
Decimal precision is 80 digits; trigonometric checks are not interval
certificates. expected_counts.json was saved before execution.
Coverage: n=5..40 plus 41,42,43,44,47,51; 2,665 ordered stable mode pairs;
42 universal witnesses; reverse/lower families; 307 cells and 265 ties;
208 direct original-field collision matrix checks; 312 maximum checks;
84,000 deterministic random physical tuples. No mathematical counterexample
was found. source_claim_checks.json separately records the false E01 label.

HISTORICAL VALIDATION REPRODUCTION
The original companion was discovered in the existing output/p08 folder.
Its SHA-256 is 81352ce048f5bd569a4d3b803f2cbd246d412aa829de43f6b6d739f2521b3958.
All 98 member hashes and the project ZIP record match the exact audited input.
The original checker was inspected and rerun only after the independent
mathematical reconstruction and new checker were complete. Its loop counts
were independently derived before comparing its stored summary. All counts,
summary fields and per-case JSON results reproduce exactly. The separately
labelled prior_validation directory preserves that evidence. The historical
checker does not assert the incorrect n=8 prose label, and is not proof.
No unresolved A08 provenance limitation remains. Earlier A04/A05 notes are
preserved, not retrospectively cleared.

READING COPY AND PRESERVATION
The standalone TeX source compiled successfully in the built-in editor.
The PDF export uses the existing pdfLaTeX toolchain; 19 pages, zero final
warnings/errors, all pages visually reviewed. No input proof, manifest,
registry, prior audit, compendium or lifecycle status was edited.
The audit-only ZIP includes no P08 source or replacement project.
The input ZIP and located historical companion remain byte-identical.

P07
P07 is cleared after the original development chat corrects E01 and records
closure on the corrected exact version. It was not begun here. This audit
has not marked P08 VERIFIED or created a P08-audited full-project archive.
