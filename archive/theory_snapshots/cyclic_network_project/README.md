# Directed cyclic network research project

Initialized 2026-09-20. This is a modular research workspace for a possible SIAM Journal on Applied Dynamical Systems paper. It is not a manuscript and does not establish any mathematical result. All 18 proof fragments are TODO; no proof, numerical experiment, literature review, or mathematical TODO from the blueprint has been completed during initialization.

The canonical main model is the demand-modulated DM model, the primary comparator is the matched bilinear MB model, and the six-term Lin–Han attribution is archived and unverified. Exact wave-number selection is planned primarily for q=2, with n=5, q=2 as the motivating specialization. General n,q remain allowed under the parameter domain in `00_canonical_model.tex`.

## Source hierarchy

Apply this order when sources disagree:

1. Explicit mathematical decisions in the initialization prompt.
2. Author-originated material.
3. Primary literature later supplied by the author.
4. Independently checked derivations.
5. Independently reproduced computations.
6. Candidate prose and claims in the master blueprint.

This is a provenance and project-choice hierarchy, not a rule that makes an unproved assertion true. A mathematical result requires its own verified derivation and audit regardless of source rank. Where a source conflicts with the canonical contract, record the conflict in `open_decisions.md`; never silently change the model.

The supplied file is `sources/directed_cyclic_networks_master.tex` in the original workspace. A byte-identical, read-only copy is packaged at `archive/directed_cyclic_networks_master.tex`. Its SHA-256 is:

```text
0a7850078ed62434b8c37c727637049c583972cd11159ac91345e6a8691e436d
```

The master blueprint is never overwritten, edited, renamed, or repurposed as a proof file. The archival copy is excluded from the compendium. It preserves old equations, incomplete arguments and numerical reports solely as reference material. The author drafts `main2-2.tex` and `chineseOrgans-2.tex`, the two pasted-text files, example papers and primary literature named by the blueprint were not separately supplied. Their content and attribution have not been independently checked.

## Files and conventions

Read `00_canonical_model.tex` and `01_notation_and_assumptions.tex` first. Index nodes from 0 to n−1 modulo n; use the predecessor shift and unitary DFT specified there. The vector fields, parameter domain and preferred terminology are frozen by the prompt. Those files contain specifications and definitions, not theorem conclusions. The remaining choices are recorded explicitly in `open_decisions.md`.

`claim_registry.md` records proposed mathematics, important archived numerical values, interpretations and rejected wording, including postponed appendices. Every proposed theorem has a designated proof owner. Future-paper paths mentioned there are reservations only and are not files created in this package. Repeated claims across the master share a registry entry; the source-anchor coverage index makes equation-level coverage checkable.

`project_manifest.md` lists the purpose, dependencies, assumptions, completion evidence and audit status of every packaged file. `02_theorem_dependency_map.tex` contains the graph, completion order, numerical gates and manuscript gates. `03_literature_audit_template.tex` is an empty literature-review form. `numerics/` contains plans only. `audits/audit_template.tex` is a blank adversarial mathematical-review form.

## Proof lifecycle

- **TODO:** planned scope and empty statement slots only. No result may be cited as established.
- **DRAFT:** exact hypotheses, complete candidate statement and derivation have been written, with all unresolved steps disclosed and linked to claim IDs. A draft is not verified.
- **VERIFIED:** the author or an identified checker has independently checked every argument, required dependency, edge case and applicable computational cross-check. Record who checked it, the date, the file version or hash and evidence. A numerical agreement cannot replace proof. Unresolved mathematical TODOs prevent this promotion.
- **AUDITED:** a separate adversarial review using `audits/audit_template.tex` has reached “verified”; all required revisions are closed and the audited version is recorded. “Revision needed,” “false,” and “unresolved” are audit verdicts, not completed statuses.

Dependencies must be VERIFIED before a dependent proof is promoted to VERIFIED. Drafting can proceed with clearly marked conditional inputs. Changes to a verified assumption, formula or dependency invalidate affected verification and audit records; return those files to DRAFT or TODO until rechecked. Update the manifest, registry and dependency map together. Rejecting a candidate is a valid research outcome: preserve its original source, record the corrected/rejected claim, and do not disguise it as a successful proof.

## Compile

Use a TeX installation with `latexmk`, pdfLaTeX, AMS packages, `geometry`, `longtable`, `array`, `booktabs`, `enumitem` and `hyperref`. From this project directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex
```

Alternatively, run `pdflatex -interaction=nonstopmode -halt-on-error proofs_compendium.tex` twice. No shell escape or bibliography download is needed. Only `proofs_compendium.tex` has a document class and preamble. Every Pxx file is an includable fragment with planning comments and empty subsection placeholders; load it through the root. The root loads all proof files in dependency order, followed by the numerical plans and audit form. It does not load the immutable blueprint or treat a successful build as mathematical verification.

The initialization build and file-integrity checks are recorded in `audits/initialization_checks.md`. Their scope is packaging and LaTeX structure only.

## Next work

Follow P01 → P02 → P03 → P04 → P05, then the acyclic order P06 through P18 shown in the dependency map. The order is a valid completion sequence, not a claim that every consecutive pair has a direct dependency. There is no blocker to using this scaffold. The later proof-specific blocking choices are B01–B09 in `open_decisions.md`.
