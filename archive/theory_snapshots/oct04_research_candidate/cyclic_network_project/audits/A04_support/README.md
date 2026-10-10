# A04 independent audit support

Main mathematical verdict: **VERIFIED**. No required mathematical or meaning-changing wording corrections. The audited P04 version is v1.0 dated 2026-09-27, 25,792 bytes, 573 lines, full-file SHA-256:

`ab80f695b3e20c852c572b7b174ecaf9964eac1aba62e3e55b2b4d3e60754e0c`

The complete standalone audit is `../A04_arbitrary_nq_fourier_spectrum.tex`; its PDF is a reading copy. All original project files are unchanged. P05 is mathematically cleared after administrative A04 closure records this exact-version verdict; this package does not perform that closure or begin P05.

## Provenance limit

P04 lines 530–545 report a historical numerical run in a separate `P04_validation_support.zip`. That companion was not provided. Its exact execution counts and floating-point maxima remain **UNRESOLVED as historical provenance**, separately from the mathematical verdict. The new exact checker in this package is independently written corroboration, not a reproduction of that old run. None of the audited theorems relies on those run statistics.

## Contents

- `input_hashes.json`: full hashes, byte counts, and line counts of the fifteen requested current inputs and shared macros.
- `archive_member_hashes.json`: complete 75-member original project inventory.
- `line_review.json`: contiguous coverage of every P04 source line, including comments and separators.
- `checks/`: independent standard-library exact checker, complete inputs/results, retained run output, and reproduction instructions.
- `delivery_checks.json`: final source/PDF hashes, build and visual checks, source preservation, and line-coverage verification.

The audit-only ZIP contains only new A04 artifacts under `audits/`. It contains no replacement P04, project manifest, claim registry, compendium, or prior audit. The supplied project ZIP and the new audit-only ZIP should remain separate records.

## Building the audit

From the `audits` directory, with a TeX distribution installed:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error A04_arbitrary_nq_fourier_spectrum.tex
```

The source is standalone and requires no original project files to compile. Its line references are to the exact P04 version named above, not to A04's own lines. See `checks/README.md` for exact-check reproduction against an authenticated original P04 source.

## Interpretation

The written audit proves universal Fourier, multiplicity, normality, norm, and stability assertions analytically. Finite exact calculations challenge and corroborate them; they do not substitute for those proofs. The audit does not establish mode selection, any first-instability path, Hopf bifurcation, transversality, a Lyapunov coefficient, periodic branches, global attraction, or new novelty/priority claims.
