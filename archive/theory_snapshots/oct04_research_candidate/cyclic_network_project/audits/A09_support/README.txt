A09 independent audit of exact P09 v1.0, 3 October 2026

Audited source: proofs/P09_transcritical_bifurcation.tex
SHA-256: b2366edf1ff71199b7f1d02a58cf828148d9a697dfafc9e07e70a523e4f26680
539 lines; 24,155 bytes. Mathematical body begins at line 17.
Body SHA-256: a0830944d46d26de35faf09c5f0e4d9f42d6f10620ca22373f6bcf7031705393

All six audit layers and OVERALL VERDICT: VERIFIED.
Required corrections: none. This package does not update P09's lifecycle.
The audit TeX is standalone and embeds its complete source-line review.
No P09 source or other replacement project source is included here.

Evidence hierarchy:
1. Independent analytical audit in A09_transcritical_bifurcation.tex.
2. input_inventory.json and archive_member_hashes.json authenticate the input.
3. line_review.json covers all 539 source lines in consecutive ranges.
4. independent_checks.py and checks/ contain independent corroboration.
5. prior_validation/ records historical developer validation reproduction only.
6. delivery_checks.json and build/ record preservation and artifact QA.

Reproduce independent checks with Python 3 and NumPy:
    python3 independent_checks.py
The deterministic run writes results under checks/ beside the script.
Exact rational identities and ordinary floating point have distinct roles;
finite samples and Newton searches cannot prove local equilibrium completeness.

The initial independent checker was written before reading the developer
checker. Its later series-division clarification still imports no developer
code. The copied prior checker is clearly segregated under prior_validation/.
That script writes only beside its copy. Original inputs are never rewritten.

Recheck input authentication from the workspace containing the original draft:
    python3 authenticate_inputs.py --workspace /absolute/path/to/workspace
This reads output/p09/cyclic_network_project, the P09 draft ZIP copies and
the complete P07-audited baseline; it writes only its audit inventory outputs.
Full current prerequisite body hashes, original audit source hashes and the
CURRENT-manifest P09 digest are recorded. No older P09 placeholder is used.

write_line_review.py regenerates only the ledger in the A09 source, never P09.
The PDF reading copy is compiled from the same standalone A09 TeX.

Original P09 development chat closure:
- Administrative closure may preserve the entire audited mathematical body.
- Keep this independent audit immutable and record its verdicts and hashes.
- After successful closure, create the COMPLETE full-project archive named
  cyclic_network_project_P09_audited.zip in that development chat.
- The audit chat must deliver only cyclic_network_project_A09_audit_only.zip.
- P10 is cleared after administrative audit closure, under its own frozen
  hypotheses and scope. No P10 proof is provided or begun here.
