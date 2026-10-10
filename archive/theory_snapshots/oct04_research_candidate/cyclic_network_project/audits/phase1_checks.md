# Phase 1 document and preservation checks

Checked 20 September 2026. These are source-identification, document-build and packaging checks. They are not proof verification or numerical validation of the models.

- Six supplied PDFs readable; title/model/result locations inspected at the exact editions in `phase1_source_manifest.md`. Core pages visually checked: Lin–Han p. 778; Wei pp. 3–4; Jaramillo p. 6; Pais p. 13; van Kekem–Sterk p. 13; Nian–Li p. 6. Other listed locations were checked in extracted source text and/or primary web versions.
- Supplemental access limits are explicit, particularly S12–S14. No full-text reading or exact equation locator is claimed for inaccessible portions.
- All 14 bibliography keys are cited and resolve. All eight novelty targets occur in the matrix; its 14 source rows distinguish general theory, analogue, component, non-location and unresolved access.
- The audit and matrix are includable LaTeX fragments and contain no proof environment or document class. The new audit root loads the shared macros and bibliography separately from the original proof root.
- pdfLaTeX/BibTeX compilation through latexmk succeeded: 15 pages. Final log has no undefined references, citation warnings, LaTeX warnings or overfull boxes. Minor bibliography underfull-box spacing messages are typographic only.
- Final page contact sheet and detailed table/source-record pages visually inspected for clipping and table alignment. The build PDF is a temporary validation output and is not part of the source ZIP.
- All 25 protected hashes match initialization: 18 proof fragments, three numerical plans, two canonical/notation files, original master and archived master. The six supplied PDF hashes also match the initial read.
- Comparing the initialized ZIP with current files identifies exactly four modified original files: README, project manifest, open decisions and claim registry. Changes document Phase 1 and correct B07/C078. All other initialized files, including the proof root and templates, are unchanged.
- No source document, source PDF or master was edited. No theorem was proved, no model derivative was computed, and no model experiment was run.

The refreshed source package contains 41 files. The initial `cyclic_network_project.zip` is preserved; `cyclic_network_project_phase1.zip` contains the updated project. No primary PDF, extraction text, rendered page, build log, executable builder or temporary PDF is included.
