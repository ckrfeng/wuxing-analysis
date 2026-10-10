# Phase 1C artifact checks

Date: 2026-09-24. These checks certify document organization and preservation, not mathematical truth, numerical results or exact-model priority.

- Phase 1B baseline: 49 files fingerprinted before this pass. Exactly four existing files changed, as requested: novelty_decisions.md, project_manifest.md, claim_registry.md, 02_theorem_dependency_map.tex. Changes are append-only planning overlays; prior text is retained.
- Canonical models, notation, macros, references.bib, numerical plans, prior audits and all P01–P18 fragments match the baseline byte for byte. All 18 proof fragments retain STATUS: TODO and have no proof environment.
- Original and archived master match SHA-256 `0a7850078ed62434b8c37c727637049c583972cd11159ac91345e6a8691e436d`. Synced source material was not edited, moved, renamed or deleted.
- All three requested new documents are present. The audit contains all eight required Lorenz–96 comparison rows and all seven requested columns. The nine claim verdicts use only the requested vocabulary. Historical audit terminology is retained only as historical content.
- Exact attempt order contains every P01–P18 exactly once and respects all original prerequisites, including the conditional P07 prerequisite for a five-node Hopf application. The last four entries are postponed; P06 is conditional.
- The new Phase 1C root compiles with latexmk/pdflatex/BibTeX to 9 pages. Final build has no overfull boxes, undefined references/citations or LaTeX warnings. All pages were rendered and visually reviewed; the two landscape comparison pages were also inspected at full rendering size. No clipped or overlapping content was found.
- The existing proofs_compendium root was rebuilt successfully with the updated dependency map; its proof fragments remain empty. Final build has no overfull boxes, undefined references/citations or LaTeX warnings. The verification PDF remains a temporary build artifact.
- The delivered PDF is byte-identical to the reviewed build. The ZIP was checked for CRC errors, expected member count, one project-folder root, all required outputs and byte equality with the project files.
- The project ZIP contains no downloaded source PDFs/archives, extraction text, browser exports or build intermediates. Earlier delivery ZIPs remain intact.
- No project theorem proof, ODE experiment, continuation, Lyapunov evaluation or literature-result reproduction was performed. Priority is explicitly **not closed** because the named main texts remain incompletely inspected.

The public 2024 supplementary archive was read as source evidence only. Source-access details and hashes are in phase1c_access_log.md. No external source's instructions were executed.
