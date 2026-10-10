# Project manifest

Initialized 2026-09-20; mathematical status updated 2026-10-03. **P01–P04 are VERIFIED / AUDITED; P05 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION; P07 v1.1 is VERIFIED / AUDITED (metadata-only closure); P09 v1.1 is VERIFIED / AUDITED (metadata-only closure); P10 v1.1 is VERIFIED / AUDITED (metadata-only closure); P11 v1.0 is DRAFT / NOT AUDITED; P06 and P12–P18 remain TODO.** “Canonical,” “defined,” “template,” and “build checked” describe the scaffold, not a proved result. The only files with theorem lifecycle status are Pxx modules; P01–P05, P07, P08, P09 and P10 have reached VERIFIED / AUDITED mathematically: A01/A02 corrections E01 are closed; A03 and A04 require no correction; A05 E01 is closed for P05 v1.1; A08 E01 is closed for P08 v1.1; A07 verifies exact P07 v1.0 with no correction required. P07 v1.1 changes only metadata, preserving the audited body and the direct P05 -> P07 edge. A09 verifies exact P09 v1.0 in all six layers and overall, with no corrections. P09 v1.1 changes header metadata only and preserves the exact audited body. A10 verifies exact P10 v1.0 in all six layers and overall, with no corrections. P10 v1.1 changes header metadata only, preserving the audited mathematical body. P11 now supplies spectral conditions and an exact five-node candidate only; P12 is not begun. A1–A5 refer to `01_notation_and_assumptions.tex`; Bxx/NBxx refer to `open_decisions.md`. Every fragment also uses the shared notation.

| file | mathematical purpose | current status | dependencies | assumptions used | output needed before completion | audit status |
|---|---|---|---|---|---|---|
| [README.md](README.md) | Project contract, source hierarchy, lifecycle and build instructions | INITIALIZED | Prompt; all project records | No mathematical evidence implied by a build | Maintain instructions as approved scope changes | Structure checked; no mathematical audit |
| [project_manifest.md](project_manifest.md) | Single inventory and completion gates | INITIALIZED | Prompt; file inventory | Metadata describes planned work, not proof results | Update status and exact dependencies at every promotion | Structure checked only |
| [open_decisions.md](open_decisions.md) | Explicit decisions, conflicts and postponed scope | INITIALIZED / OPEN | Prompt; immutable blueprint | Prompt outranks conflicting candidate text | Close B01–B09 before their affected claims; preserve decision history | Unresolved items disclosed |
| [claim_registry.md](claim_registry.md) | 170 classified claim records and source-anchor map | INITIALIZED / claims unverified | Immutable blueprint; prompt; proof owners | Archive wording and numbers are not established facts | Complete or reject claims with linked proof/source/computation evidence | Mathematical claims unverified; Phase 1 literature overlay; C078 corrected |
| [shared_macros.tex](shared_macros.tex) | Shared notation and theorem infrastructure | DEFINED | Root AMS packages; 01 conventions | Macros make no mathematical assertions | Maintain stable names and avoid hidden model-specific formulas | Build/structure checked |
| [00_canonical_model.tex](00_canonical_model.tex) | DM, MB and secondary archived comparator contract | CANONICAL / archive qualified | Explicit prompt; master six-term transcription | A1–A3; A4 only as declared; six-term attribution unverified | No proof required; later model changes require explicit recorded authority | Equation transcription checked; no theorem audit |
| [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | Indices, DFT, pairing, state sets and spectral terminology | DEFINED | 00; prompt; disclosed notation choices | A1–A5 distinguish standing from conditional hypotheses | B07 resolves future adjoint/l1 compatibility; other open choices remain explicit | Notation/build checked; derived identities not certified |
| [02_theorem_dependency_map.tex](02_theorem_dependency_map.tex) | Directed graph, completion order, numerical and manuscript gates | PLANNED | P01–P18 metadata; N01–N03 plans | Edges express prerequisites, not established theorems | Keep DAG, root order and manifest synchronized; add conditional scope explicitly | Acyclicity/order checked |
| [03_literature_audit_template.tex](03_literature_audit_template.tex) | Structured future primary-source and novelty audit | TEMPLATE | Prompt; source hierarchy | No source consulted or novelty confirmed | Completed source forms before attribution, overlap or priority claims | Not started |
| [proofs_compendium.tex](proofs_compendium.tex) | Contract and proof compendium: audited P01–P05/P07/P08/P09/P10 plus DRAFT P11 and remaining placeholders | BUILD CHECKED | Shared macros; 00–03; P01–P18; N01–N03; audit form | Compilation is not proof verification; earlier draft and planning status text is historical | Maintain compilation and current banner; P10 VERIFIED / AUDITED, no correction; P11 DRAFT / A11 audit pending | P01, P02 and P03 VERIFIED / AUDITED; A01/A02 E01 closed; A03 requires no correction; P04 VERIFIED / AUDITED; A04 requires no correction; U01 nonblocking; P05 v1.1 VERIFIED / AUDITED AFTER MINOR REVISION; A05 E01 closed; A05 U01 nonblocking; P08 v1.1 VERIFIED / AUDITED AFTER MINOR REVISION; A08 E01 closed; P07 v1.1 VERIFIED / AUDITED; A07 VERIFIED, no correction required; P09 and P10 VERIFIED / AUDITED; A09/A10 require no correction |
| [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | Global nonnegative flow; explicit invariant, attracting and absorbing cubes | VERIFIED / AUDITED | Canonical model and notation only; standard local ODE theory | Canonical A1–A3; proved extension n>=1, any residue q, real a, k>0, c,g,h>=0; k>=0 for global existence alone | Complete: A01 required correction E01 applied; no remaining required P01 revision | CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION; audits/A01_wellposedness_and_absorbing_box.tex |
| [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | Invariant synchrony; complete canonical synchronous-root classification and algebraic branch loci | VERIFIED / AUDITED (P02 v1.1, 2026-09-27) | 00; 01; shared macros; P01 CORE VERIFIED / AUDITED | Canonical A1–A3; positive parameters; scalar domain s>-1; limited weaker-assumption remarks explicitly scoped | Complete: A02 sole required correction E01 applied; no remaining required P02 revision | A02 original CORE MINOR REVISION / EXTENDED VERIFIED; closure CORE VERIFIED AFTER MINOR REVISION / EXTENDED VERIFIED |
| [proofs/P03_origin_and_linearization.tex](proofs/P03_origin_and_linearization.tex) | General Jacobian, full origin spectral structure, homogeneous coefficients and additive offset collisions | VERIFIED / AUDITED (P03 v1.1, metadata-only closure, 2026-09-27) | 00; 01; shared macros; P01/P02 VERIFIED / AUDITED; standard cyclic-permutation/circulant facts only | Canonical A1–A3; x in U; synchronous x* > -1; equilibrium identity used only at nonzero equilibria | Complete: A03 VERIFIED with no required correction; audited mathematical body preserved byte-for-byte | VERIFIED; audits/A03_origin_and_linearization.tex; audited P03 v1.0, current v1.1 metadata only |
| [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | Complete homogeneous Fourier spectrum, multiplicities, normality and exact linear stability | VERIFIED / AUDITED (P04 v1.1, metadata-only closure, 2026-09-27) | 00; 01; shared macros; P01, P02, P03 VERIFIED / AUDITED; standard finite-dimensional linearized-instability theorem | Canonical A1–A3; any admissible q; x*>-1 for spectral algebra; equilibrium for stability; no coprimality requirement | Complete: A04 VERIFIED with no required correction; audited mathematical body preserved byte-for-byte; U01 historical numerical-run provenance remains nonblocking | VERIFIED; audits/A04_arbitrary_nq_fourier_spectrum.tex; audited P04 v1.0, current v1.1 metadata only |
| [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | Exact finite-n step-two selection, reachable modes, canonical realizability and local switch geometry | VERIFIED / AUDITED AFTER MINOR REVISION (P05 v1.1, 2026-10-02) | 00; 01; shared macros; P01–P04 VERIFIED / AUDITED | n>=5; q=2; a,k,c,g,h>0; specified positive synchronous equilibrium; all ties retained | Complete: sole required A05 issue E01 applied; formulas, theorems and proofs otherwise unchanged; P08 prerequisite cleared | Original A05 CORE MINOR REVISION; REALIZABILITY VERIFIED; OVERALL MINOR REVISION; E01 closed; U01 nonblocking; audits/A05_q2_mode_selection.tex |
| [proofs/P06_large_n_limit.tex](proofs/P06_large_n_limit.tex) | Large-n selected-wave-number limit | TODO | 00; 01; shared macros; P05 | A1--A3; q=2; a specified sequence of networks, coefficients and equilibrium branches; canonical representative 0<=m<=floor(n/2). | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. B04: freeze the large-n family and intended uniformity before the theorem statement. | NOT STARTED |
| [proofs/P07_five_node_specialization.tex](proofs/P07_five_node_specialization.tex) | Exact five-node spectrum, all three real-part classes, golden-ratio selection, spectral coincidences and stability | VERIFIED / AUDITED (P07 v1.1, metadata-only closure, 2026-10-03) | 00; 01; shared macros; P05 directly; P03/P04 and P01/P02 inherited; no P08 theorem dependency | A1–A3; n=5, q=2; a,k,c,g,h>0; specified positive synchronous equilibrium | Complete: A07 VERIFIED with no required correction; exact audited mathematical body preserved byte-for-byte; P09 cleared but not begun | VERIFIED in all five layers and overall; audits/A07_five_node_specialization.tex; audited P07 v1.0, current v1.1 metadata only |
| [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | MB foundation, exact finite-n selection, and realizable same-tuple DM–MB stability/mode contrasts | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03); MAIN THEOREM TARGET | 00; 01; shared macros; P01–P05 VERIFIED / AUDITED only | Canonical positive tuple; arbitrary n,q for MB foundation/spectrum; q=2 comparison; same coefficients and time, own named positive synchronous branches | Complete: sole required A08 E01 applied verbatim; all other mathematical body bytes unchanged; P07 cleared but not begun; Hopf/criticality and six-term work remain deferred | Original A08 foundation/spectral/parity VERIFIED; comparison/overall MINOR REVISION; E01 closed; audits/A08_matched_bilinear_analysis.tex |
| [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | Full-system local origin transcritical theorem and cubic-degenerate classification | VERIFIED / AUDITED (P09 v1.1, metadata-only closure, 2026-10-03) | 00; 01; shared macros; P02, P03, P04 VERIFIED / AUDITED; P01 inherited | Canonical A1–A3; fixed a,k,c,h,n,q; g varies near a+c; U for signed branches; generic a != k+h | Complete: A09 VERIFIED with no required correction; exact audited P09 v1.0 mathematical body preserved byte-for-byte; P10 was cleared at that closure | VERIFIED in all six layers and overall; audits/A09_transcritical_bifurcation.tex; no mathematical revision |
| [proofs/P10_saddle_node_and_bistability.tex](proofs/P10_saddle_node_and_bistability.tex) | Full-system positive saddle-node, all-mode branch stability and open stable coexistence | VERIFIED / AUDITED (P10 v1.1, metadata-only closure, 2026-10-03) | 00; 01; shared macros; P02, P03, P04, P09 VERIFIED / AUDITED; P01 inherited | Canonical A1–A3; a>k+h; fixed a,k,c,h,n,q and varying g; no coprimality restriction | Complete: A10 VERIFIED in all six layers and overall; no correction required; exact audited body retained. B03 retains synchronous threshold and local two-basin disk only; no global partition. P11 cleared but not begun | VERIFIED; audits/A10_saddle_node_and_bistability.tex; metadata-only closure of P10 v1.0 |
| [proofs/P11_hopf_spectral_conditions.tex](proofs/P11_hopf_spectral_conditions.tex) | Strict q=2 spectral candidates, simplicity, stable complement, exact five-node point and handoff data | DRAFT / NOT AUDITED (P11 v1.0, 2026-10-03) | 00; 01; shared macros; P02, P04, P05 VERIFIED / AUDITED; P07 conditional five-node input; P03 inherited through P04 | n>=5, q=2, positive coefficients and specified positive synchronous equilibrium; complete strict selection; nonzero frequency | Independent A11 audit. Exact g-path and upper branch frozen; no path derivative, Lyapunov coefficient, Hopf or periodic-branch conclusion | A11 NOT STARTED; exact and numerical corroboration separate |
| [proofs/P12_hopf_transversality.tex](proofs/P12_hopf_transversality.tex) | Hopf transversality | TODO | 00; 01; shared macros; P11 | P11 hypotheses; smooth parameter path and differentiable equilibrium branch; retain state dependence in all derivatives. | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. B02 and B06 must be resolved for the final quantitative statement. | NOT STARTED |
| [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | First Lyapunov coefficient and nondegenerate Hopf theorem | TODO | 00; 01; shared macros; P11, P12 | P11--P12 hypotheses; smooth DM field near the equilibrium; explicitly reconciled Hermitian pairing, adjoint vector and Taylor factorial conventions. | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. B07: resolve adjoint/Taylor/l1 conventions; B06: choose a rigorous sign-certification strategy. | NOT STARTED |
| [proofs/P14_rotating_waves.tex](proofs/P14_rotating_waves.tex) | Equivariant rotating waves | TODO | 00; 01; shared macros; P11, P12, P13 | Verified nondegenerate Hopf hypotheses from P13; exact homogeneous cyclic action P; prescribed mode representative and time orientation. | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. B07 includes the time/phase orientation for translating the Hopf mode into a wave. | NOT STARTED |
| [proofs/P15_heterogeneous_equilibrium_persistence.tex](proofs/P15_heterogeneous_equilibrium_persistence.tex) | Persistence under parameter heterogeneity | TODO | 00; 01; shared macros; P02, P04; optional periodic-orbit extension additionally P14 | A1--A3 at the homogeneous base point; explicit heterogeneous family; coefficient positivity; invertibility or hyperbolicity according to the requested conclusion. | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. B08: freeze the heterogeneous family and coefficient assignment; NB08 decides the optional orbit extension. | NOT STARTED |
| [proofs/P16_static_sensitivity_and_green_function.tex](proofs/P16_static_sensitivity_and_green_function.tex) | Static sensitivity and localized Green function | TODO | 00; 01; shared macros; P04, P15 | Verified P15 family; invertible homogeneous J; canonical DFT and a specified perturbation profile. | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. B08 blocks formulas; NB09 governs directional/localization terminology. | NOT STARTED |
| [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | Transient and harmonic response | TODO | 00; 01; shared macros; P04, P16 | Homogeneous linearization; explicit initial condition or external forcing protocol; stability and resolvent assumptions stated per result. | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. NB09: decide observable and forcing convention before quantitative propagation claims. | NOT STARTED |
| [proofs/P18_stability_radius_and_hopf_shift.tex](proofs/P18_stability_radius_and_hopf_shift.tex) | Stability radius and Hopf-threshold sensitivity | TODO | 00; 01; shared macros; P04, P12, P13, P15, P16 | For radius: a strictly stable homogeneous base; for threshold shift: a simple transverse Hopf point; specified norm and heterogeneous family; treat these as different parameter regimes. | Exact scoped statements and complete independent proofs; required checks closed; verification and audit evidence. B08 and B09: fix the heterogeneous family and norm/uncertainty class; B07 governs eigenvector conventions. | NOT STARTED |
| [PROPOSED_P11_scope_clarification.md](PROPOSED_P11_scope_clarification.md) | Proposed clarification of older first-crossing wording and optional cell realizability | PROPOSED ONLY | Current P11 assignment; frozen S11 and attempt-order row 10 | No frozen file is changed | Review scope wording at later assembly; no theorem status promotion | Not an audit |
| [numerics/N01_validation_protocol.tex](numerics/N01_validation_protocol.tex) | Independent checks and reproducibility protocol | TODO / PLAN ONLY | P01–P18 according to each test | B02/B06/B07/B08 and NB11–NB12 when applicable | Two independent l1 implementations; all declared residual/spectrum/symmetry/continuation checks and refinement records | NOT RUN |
| [numerics/N02_continuation_plan.tex](numerics/N02_continuation_plan.tex) | Equilibrium, periodic and heterogeneous continuation plan | TODO / PLAN ONLY | N01; P02–P04/P08; P09–P14; P15–P18 by stage | Explicit model, branch, path, software and precision; ordinary versus validated numerics distinguished | Raw branches, full spectra, Floquet records, independent validation and reproduction settings | NOT RUN |
| [numerics/N03_figure_plan.tex](numerics/N03_figure_plan.tex) | Nine evidence-gated figure specifications | TODO / PLAN ONLY | Canonical contract; each figure’s Pxx owners; N01/N02 | Explicit calibration, parameters, norms and evidence type | Validated data, regeneration scripts and claim-matched captions | NOT RUN |
| [audits/A09_transcritical_bifurcation.tex](audits/A09_transcritical_bifurcation.tex) | Independent audit of exact P09 v1.0 | IMMUTABLE AUDIT; all six layers and overall VERIFIED | Exact authenticated P09 v1.0 and P01–P04 foundations | Original version and body hashes recorded in A09 | No corrections required; metadata-only P09 v1.1 closure | COMPLETE; source, PDF and all support preserved byte-for-byte |
| [audits/audit_template.tex](audits/audit_template.tex) | Independent adversarial proof/source audit form | TEMPLATE | Prompt; proof lifecycle; exact reviewed version | Reviewer must distinguish assertion, proof and computation | Completed verdict and revision closure for every submitted claim | Blank template; no verdict issued |
| [audits/A07_five_node_specialization.tex](audits/A07_five_node_specialization.tex) | Immutable independent audit of exact P07 v1.0 | AUDIT PRESERVED; VERIFIED | Exact audited P07 full/body hashes; P03–P05 verified inputs | Canonical positive equilibrium; n=5,q=2; exact source scope | Complete: no correction required; all supplied audit support retained unchanged | All five layer verdicts and overall VERIFIED |
| [audits/A01_wellposedness_and_absorbing_box.tex](audits/A01_wellposedness_and_absorbing_box.tex) | Independent P01 audit and exact reviewed-version evidence | AUDIT PRESERVED; E01 CLOSED IN P01 v1.1 | Audited draft SHA-256 and P01 statements | Exact assumptions and scope recorded in A01 | Complete: sole required wording correction applied; audit source retained unchanged | CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION as recorded in current P01 header |
| [audits/initialization_checks.md](audits/initialization_checks.md) | Packaging and LaTeX verification record | STRUCTURE CHECKED | All packaged files; immutable source digest; build log | No mathematical, numerical or literature verification | Record source integrity, required files, placeholder purity, DAG, source anchors and build outcome | Initialization only |
| [archive/directed_cyclic_networks_master.tex](archive/directed_cyclic_networks_master.tex) | Byte-identical immutable research blueprint | IMMUTABLE / UNVERIFIED ARCHIVE | Supplied source; SHA-256 in README | Contains unfinished and possibly incorrect claims; exclude from compendium | Never edit or overwrite; consult as provenance only | Integrity checked; contents not mathematically audited |

## Completion and dependency policy

P01–P18 are included in increasing numeric order, a valid topological ordering. P06 and P07 do not depend on each other. P15 equilibrium persistence does not depend on Hopf results; its optional orbit extension would. P17's use of P16 is a deliberate reuse of the response conventions and Green-function setup. P18 has separate stable-base and Hopf-base statements; the hypotheses must not be conflated.

Proof promotion requires a scoped exact statement, independent derivation, complete assumptions, checked prerequisites and the module's required checks. A candidate may be narrowed or rejected when the evidence demands it, with a registry record. Optional archive-derived extensions (six-term application, MB Hopf, codimension-two classification, periodic-orbit persistence) must be separately adopted and cannot silently enlarge a completed core theorem.

The three numerical files are plans and provide no results. `future_papers/` paths in the registry are reserved owners, not missing deliverables. The ZIP contains all 32 requested files, the immutable archival copy and this initialization-check record; no simulation code or final manuscript is supplied.

## Phase 1 additions and current status

The initialization table above is retained as its historical baseline. The current literature status is below; no proof file has advanced beyond TODO. Six supplied papers now have version-specific audit records. The Lin–Han equation attribution is checked in Phase 1, while the canonical file remains byte-for-byte preserved.

| file | mathematical purpose | current status | dependencies | assumptions used | output needed before completion | audit status |
|---|---|---|---|---|---|---|
| [03_literature_audit.tex](03_literature_audit.tex) | Six core source audits plus methodological context and evidence gaps | PHASE 1 REVIEW, WITH GAPS | Six supplied PDFs; supplemental primary sources; canonical contract | Exact source versions; absence is corpus-limited | Close source gaps L01–L03 before strong priority claims | Locations checked; source theorems not re-proved |
| [references.bib](references.bib) | Fourteen bibliographic records | POPULATED; disclosed metadata gaps | Source title pages; publisher/author records | Partial sources explicitly marked | Complete Jaramillo article number and missing full-text locators | Citation keys/build checked |
| [novelty_matrix.tex](novelty_matrix.tex) | Source-by-target matrix and five-category classification | PROVISIONAL NOVELTY ASSESSMENT | 03; references; frozen program | No theorem truth or universal priority inferred | Reassess after precise statements and literature gaps close | All eight targets covered |
| [overlap_risk_report.md](overlap_risk_report.md) | Main-paper overlap risks, access gaps and release gates | PHASE 1 COMPLETE WITH LIMITS | 03; matrix; metadata corrections | No separate archival research track | Close L01–L04 as applicable | Evidence limits disclosed |
| [literature_audit_compendium.tex](literature_audit_compendium.tex) | Separate compilable audit root | BUILD CHECKED | shared_macros; 03; matrix; references.bib | Build is not mathematical verification | Rebuild after later edits | See phase1_checks.md |
| [audits/phase1_source_manifest.md](audits/phase1_source_manifest.md) | Exact supplied file provenance and hashes | RECORDED | Six read-only local PDFs | No source PDF included in ZIP | Retain version-specific locators when editions change | Source fingerprints recorded |
| [audits/phase1_checks.md](audits/phase1_checks.md) | Preservation and LaTeX checks | STRUCTURE CHECKED | Package; original protected hashes; build log | No model numerical validation | Refresh after document changes | No proof status promotion |


## Phase 1B append-only update — 2026-09-24

The original inventory above remains a historical record. All P01–P18 mathematical statuses remain TODO; their proposed manuscript roles are now evaluated in `novelty_decisions.md`. No canonical model, proof, numerical plan, master, original audit or original novelty matrix was changed. Audit completion is qualified by explicit source-access gaps.

| file | mathematical purpose | current status | dependencies | assumptions used | output needed before completion | audit status |
|---|---|---|---|---|---|---|
| [04_adversarial_novelty_audit.tex](04_adversarial_novelty_audit.tex) | Adversarial source comparison; packages A–D; scope recommendation | PHASE 1B ASSESSED / ACCESS GAPS | Original six papers; S07–S29; source locators | Model-specific mathematics unproved; priority not inferred from absence | Retrieve blocking model sources before a priority assertion; later independent proofs | Literature assessment only |
| [revised_novelty_matrix.tex](revised_novelty_matrix.tex) | Eight targets with seven challenge questions each and color verdicts | CURRENT NOVELTY ASSESSMENT | 04; original matrix preserved | RED is not a proof that every DM statement has appeared verbatim | Reassess after sharpened statements and missing exact equations | No GREEN; T1 remains GRAY |
| [novelty_decisions.md](novelty_decisions.md) | One disposition per P01–P18; proposed strengthened statements | RECOMMENDATIONS / NOT ADOPTED THEOREMS | 04; matrix; B02/B04/B05/B08/B09 | Proposed effects may fail; no theorem truth assumed | Author scope choices and future independent derivation | All 18 covered; no proof started |
| [additional_sources_needed.md](additional_sources_needed.md) | Prioritized retrieval and statement-specific clearance gates | OPEN RETRIEVAL QUEUE | Backward references and access log | Missing bodies cannot be cleared from abstracts | Exact equation/theorem/version comparisons for listed blockers | Access limitations explicit |
| [adversarial_audit_compendium.tex](adversarial_audit_compendium.tex) | Compilable Phase 1B review root | BUILD CHECKED | shared_macros; 04; revised matrix; bibliography | Compilation has no mathematical evidentiary force | Maintain build and citation integrity | Separate from preserved Phase 1 root |
| [adversarial_audit_compendium.pdf](adversarial_audit_compendium.pdf) | Portable reading copy of the new audit and matrix | GENERATED REVIEW COPY | New root | Same limitations as source fragments | Regenerate when those files change | Layout/build checked |
| [audits/phase1b_search_log.md](audits/phase1b_search_log.md) | Search scope, backward paths and access quality | RECORDED | Searches dated 2026-09-24 | Search results are not exhaustive absence evidence | Continue only targeted retrieval when needed | Primary evidence separated from discovery leads |
| [audits/phase1b_checks.md](audits/phase1b_checks.md) | Preservation, structure, citation and build checks | CHECKED | Baseline SHA-256 inventory; build | Checks certify artifacts only | Retain with delivered package | No numerical or mathematical tests |
| [references.bib](references.bib) | Expanded source index | APPENDED; original 14 records preserved | Publisher/author metadata; 04 access notes | Bibliography presence does not mean full-text inspection | Complete metadata where explicitly marked incomplete | Versions/access states recorded |
| [claim_registry.md](claim_registry.md) | Append novelty assessment to existing claims | ORIGINAL 170 RECORDS PRESERVED | 04; revised matrix | Novelty status differs from mathematical status | Later proofs and any revised novelty assessment | Phase 1B overlay only |
| [open_decisions.md](open_decisions.md) | Add priority and scope choices | ORIGINAL ENTRIES PRESERVED | New audit and retrieval queue | Recommendations do not change the canonical model | Close relevant gates before claim release | New decisions B1-01–B1-06 |

To compile the new review document from this folder: `latexmk -pdf adversarial_audit_compendium.tex`. The original `literature_audit_compendium.tex` and `proofs_compendium.tex` remain available and unchanged. The new root does not input proof modules or the blueprint.

## Phase 1C current scope and deliverables — 2026-09-24

The following is the current planning overlay; older inventories remain historical. The frozen scope and attempt order in `frozen_theorem_package.md` supersede earlier recommendations. All proof modules remain TODO and are byte-identical to the Phase 1B baseline. Source and canonical files are unchanged. Bibliography records are preserved; newly discovered source leads have full records and links in 05 and the access log.

| file | mathematical purpose | current status | dependencies | assumptions used | output needed before completion | audit status |
|---|---|---|---|---|---|---|
| [05_priority_closure.tex](05_priority_closure.tex) | Targeted source-chain inventory and eight-object Lorenz–96 comparison | TARGETED PASS FINISHED; PRIORITY NOT CLOSED | S13–S16; 2024 supplement; supplied Lorenz–96 version | Missing bodies are unknown, never absence | Inspect named missing main texts before exact-model priority assertion | Inspected locations separated from access gaps |
| [final_novelty_verdict.md](final_novelty_verdict.md) | Nine current verdicts using the requested vocabulary | CURRENT PLANNING ASSESSMENT | 05; prior checked primary sources | Candidate rating is not proof or priority clearance | Later exact statements, proofs and named-source clearance | All nine covered |
| [frozen_theorem_package.md](frozen_theorem_package.md) | One frozen paper scope, roles and all-module attempt queue | FROZEN RESEARCH SCOPE | 05; canonical contract; original DAG | Effects may fail; branch/path/sign region not invented | Future independent mathematics; explicit scope revision if core fails | All P01–P18 assigned |
| [novelty_decisions.md](novelty_decisions.md) | Current scope and module disposition overlay | UPDATED APPEND-ONLY | Final verdict; frozen package | Historical recommendations remain dated | Apply current overlay in future work | No proof status changes |
| [claim_registry.md](claim_registry.md) | Nine current novelty overlays | ORIGINAL CLAIMS PRESERVED | 05; final verdict | Novelty distinct from correctness | Keep proof and priority gates separate | C1-N1–C1-N9 added |
| [02_theorem_dependency_map.tex](02_theorem_dependency_map.tex) | Current attempt order and assembly gates | PLANNING ONLY | Original acyclic graph; frozen package | Schedule arrows are not new prerequisites | Follow source and mathematical release gates | All module dependencies retained |
| [priority_closure_compendium.tex](priority_closure_compendium.tex) | Separate compilable Phase 1C reading root | BUILD CHECKED | shared macros; 05; bibliography | Does not input proofs or master | Rebuild after changes | See phase1c_checks.md |
| [priority_closure_compendium.pdf](priority_closure_compendium.pdf) | Portable reading copy of Phase 1C | GENERATED | New root | Same explicit access limitations | Preserve with source | Render/build checked |
| [audits/phase1c_access_log.md](audits/phase1c_access_log.md) | Exact source URLs, access attempts and supplement provenance | RECORDED | Bounded backward/forward tracing | Catalogue entries and snippets are partial evidence | Named source-body inspection only; no general search queue | Limits explicit |
| [audits/phase1c_checks.md](audits/phase1c_checks.md) | Package preservation, build and layout checks | STRUCTURE CHECKED | Baseline hashes; LaTeX build; PDF render | Not mathematical/numerical validation | Retain alongside ZIP | No proof or model experiment |

Compile the new reading copy from this folder with `latexmk -pdf priority_closure_compendium.tex`. The original proof and literature roots remain available. `cyclic_network_project_phase1c.zip` is the current delivery; earlier ZIPs are preserved. The 2024 publisher archive and source PDFs are not redistributed inside the project ZIP.

## P01 mathematical draft — 2026-09-27

This is the current mathematical-status update and supersedes earlier all-TODO wording for P01 only. The literature-priority phase and frozen scope are unchanged. No literature search or numerical experiment was performed.

P01 now contains full proposed proofs of local uniqueness, nonnegative invariance, strict positivity and step-one propagation, the tied-maximum Dini estimate, scalar comparison, global continuation, and explicit invariant/attracting/absorbing cubes. Under the canonical assumptions the improved radius is `R=(a-k+sqrt((a+k)^2+4kc))/(2k)`. The cube absorbs the entire orthant by `log(2)/(kR)+(1+R)/g`. This improves the archived larger radius without claiming a smallest cube for the full system.

For the stated weaker coefficient domain, P01 also distinguishes R=0, classifies precisely when its exact-radius cube is absorbing, gives uniform entry bounds for every larger cube, and proves global continuation with k=0 while exhibiting the failure of a universal bounded region in that class. All scalar roots and counterexamples concern these foundation claims; no later module has been developed.

B01's attraction/absorption distinction is resolved in the DRAFT statement, subject to independent audit. No source file, canonical convention, other Pxx body, numerical plan or frozen literature file was modified. The current `proofs_compendium.tex` contains the updated mathematical-status banner and compiles successfully. The included `proofs_compendium.pdf` is a reading copy, not evidence of verification.

Independent-auditor focus: tangent-face invariance; tied maxima and the sign of the rational loss bound; clipping the scalar radius at zero when a+c<=0; uniform absorption of the whole unbounded orthant; the finite-step integral lower bound when g=0 and c,h>0; and sharp failure cases of the exact-radius absorption criterion. P01 remains DRAFT until a separate independent audit is completed.

## P01 audit closure and revision log — 2026-09-27

This is the current status record: **P01 VERIFIED / AUDITED**; **CORE VERIFIED**; **EXTENDED VERIFIED AFTER MINOR REVISION**. P02–P18 remain TODO and unchanged. The dated draft records above are historical.

- Audit evidence: [A01](audits/A01_wellposedness_and_absorbing_box.tex), issue E01, subsection “Archived radius: the single required correction,” referring to line 428 of the audited draft.
- Exact sole body correction: `is the nonnegative root of $as-ks^2+c=0$.` → `is the larger real root of $as-ks^2+c=0$, and is nonnegative.`
- Reason: for c=0 and a>0, both 0 and a/k are nonnegative roots; the displayed B selects the larger root. Its formula, all hypotheses, inequalities, conclusions, constants, and proofs remain unchanged.
- The requested header now records status, audit file, both verdicts, date and version/hash. All other P01 body bytes are preserved. In particular, the old body sentence about DRAFT status is retained to respect the instruction limiting body edits to E01; the current header and this record govern status.
- No optional audit suggestions were applied. A01 itself, the immutable blueprint, canonical files, and every other proof body remain unchanged. P02 was not begun.
- Version: `P01 v1.1`. The header hash covers UTF-8 bytes from the first `\section{P01:` line through end of file, avoiding a self-referential file digest.
- Audited draft SHA-256: `ba881a703b7c1dedefce4ccb920f7b8243418cccd9219eb8285fbb707911941b`.
- Corrected body SHA-256: `a640b2bf9a160feed273dc667c6b44a6923a1d68d6dd81acd35640cc0e4d5808`.
- Corrected full-file SHA-256: `0d6950821aa83f3d09e8bfe84dab2b0b5020aa6e7881cf6928e984bff1890f1e`.

The revised compendium reports the completed audit and preserves historical status wording in previously audited and planning text. Its input order is unchanged. Compilation passed: 38 pages, with no LaTeX warnings, undefined references, or overfull boxes. Changed pages 1, 2 and 16 were rendered and visually checked; page numbering is unchanged.

Preservation checks passed: the P01 body equals the exact audited body with the one E01 replacement; all proof, theorem, lemma, proposition, corollary, equation and align environments are byte-identical. Every other proof module, A01, and all frozen/source files match the pre-revision SHA-256 inventory. Only the four authorized source files and the regenerated reading PDF changed. The ZIP was checked for archive integrity and exact agreement with the project folder.

Current delivery: [cyclic_network_project_P01_audited.zip](../cyclic_network_project_P01_audited.zip). The prior draft ZIP is preserved.


## P02 draft and internal-check record — 2026-09-27

**Current status: P01 VERIFIED / AUDITED; P02 DRAFT; P03–P18 TODO.** This supersedes earlier dated P02-TODO wording. The frozen literature phase, model, notation, scope, and dependency graph remain unchanged. The graph's historical all-TODO statements are not current proof statuses. P02 has no new literature or numerical dependency and has not received an independent audit.

Current input is `cyclic_network_project_P01_audited.zip`. Its embedded A01 is byte-identical to the separately supplied audit archive. P01 v1.1 already contains the exact E01 correction, and its full-file SHA-256 matches `0d6950821aa83f3d09e8bfe84dab2b0b5020aa6e7881cf6928e984bff1890f1e`; no P01 revision is outstanding and no P01 bytes were changed. All twelve requested current files were located and used before P02 mathematics began.

P02 v1.0 supplies direct componentwise invariance, the scalar equation `s' = s[mu+(a-A)s-As^2]/(1+s)`, the separately retained origin, and an eleven-cell exhaustive classification of the quadratic `Q(s)=As^2+(A-a)s-mu`. It distinguishes mathematical roots, roots in s>-1, nonnegative equilibria, and positive equilibria. It proves necessary-and-sufficient positive counts, the branch-intersection locus `g=a+c`, the repeated-root locus `g_f=a+c+(a-A)^2/(4A)`, and the degeneracy `a=A, g=a+c`. No stability or bifurcation type is asserted.

Internal checking used five exact symbolic polynomial identities, all eleven displayed rational representatives, and 2,868 distinct positive rational parameter tuples from a specified grid plus exact equality and neighboring-boundary cases. Tests included 4,438 exact residual substitutions into the original rational scalar field, 217 explicitly rejected s=-1 roots, Vieta relations, all four necessary-and-sufficient alternatives and their converses, origin multiplicities, and 424 synchronous component substitutions including coincident and non-coprime offsets. No counterexample to a P02 equivalence was found. The proof and explicit continuity analysis, not these finite checks, justify the proposed statements. No ODE integration, continuation, spectrum, or later-module numerical task was performed.

Independent-auditor priorities are listed in P02's final paragraph: reconstruct the maximal-domain invariance proof; division and domain filtering; discriminant and Vieta identities; every count and multiplicity; both directions of positive-existence conditions; both branch loci and their common degeneracy; boundary limits and the local quadratic coefficient; representative residuals; and the scope of weaker assumptions. P02 remains DRAFT.

### P02 validation, build, and preservation

The explicit boundary-limit analysis was supplemented by 102 exact shrinking-parameter root-error bounds on neighboring real-root regions, including `g=c`, `mu=0`, `D=0`, `a=A`, and the common degeneracy; five exact numerator-order cases separately check the origin multiplicities. These are internal algebra checks, not an independent audit.

Compilation passed using the existing README workflow: `latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex` with pdfLaTeX. The reading PDF has **45 pages**, with P02 on pages **18–25**. There are **three underfull-hbox diagnostics** in the unchanged `02_theorem_dependency_map.tex` at source lines 126–127, 129–130, and 130 (badness 1286, 1275, 10000). They concern justified table-cell spacing. There are **no overfull boxes, undefined references, duplicate-label warnings, macro conflicts, LaTeX/package warnings, or compilation errors**. All 146 labels in the included source tree are unique. The title/contents, the affected preserved dependency-map pages, and every P02 page were rendered and visually inspected; no clipping or overlap was found. Compilation does not verify the mathematics.

P02 v1.0 full-file SHA-256: `a63f0757eb0de6462b7ce18c179f6f5c21079a8c3e8d0f9c3ed53d6ce7b256f3`. The exact current module awaits a separate A02 audit; no VERIFIED or AUDITED label is assigned to it.

The authorized source changes are exactly `proofs/P02_synchronous_subspace_and_equilibria.tex`, `project_manifest.md`, `claim_registry.md`, and `proofs_compendium.tex`; the existing reading copy `proofs_compendium.pdf` is regenerated. SHA-256 comparison against the supplied audited archive confirms that every other existing file, including P01, A01, P03–P18, all canonical/notation/macro files, the dependency map, the immutable master, and all literature-audit files, is byte-identical. The source inventory and compendium input order are unchanged. Build intermediates and scratch checking scripts are excluded from the project ZIP.

Current delivery: `cyclic_network_project_P02_draft.zip`. The uploaded P01-audited and A01 archives are preserved. The project ZIP contains the same relative file inventory as the supplied project, with only the five authorized source/reading-copy replacements above; archive integrity and exact member-byte agreement were checked.

## P02 audit closure and revision log — 2026-09-27

**Current status: P01 and P02 VERIFIED / AUDITED; P03–P18 remain TODO.** This supersedes the dated P02 draft records above. Version: **P02 v1.1**. The original A02 verdict is **CORE MINOR REVISION; EXTENDED VERIFIED**. Closure: **E01 corrected; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED**.

- Audit file registered as requested: `audits/A02_synchronous_subspace_and_equilibria.tex`.
- Available audit evidence: [A02 PDF](audits/A02_synchronous_subspace_and_equilibria.pdf), supplied by the user and retained byte-for-byte. The `.tex` source was not supplied or located; no replacement or reconstructed audit source has been invented. A02 PDF SHA-256: `089f40bfd3d8c0b62fb6eda7eac391c093bb023b150a88771a5cd00b5e23eff6`.
- A02 identifies the exact audited P02 v1.0 full-file SHA-256 `a63f0757eb0de6462b7ce18c179f6f5c21079a8c3e8d0f9c3ed53d6ce7b256f3` and project ZIP SHA-256 `68e5b8a2277ee89d37816a440e9c487b36b2ec873aea336fba02ad83bd6eaa7e`; both match the current pre-correction files.
- Sole P02 body correction: A02 E01, boundary-continuity paragraph (audited lines 548–552). The limits now explicitly name the ordered pair `(s_-,s_+)`: `(0,b/A)` when mu tends to zero at fixed b>0, `(b/A,0)` at fixed b<0, and `(-1,a/A)` when g tends to c. The b=0 both-zero limit and exclusion of the first root at g=c are retained. The clarification uses inline mathematics, leaving every displayed formula unchanged.
- No theorem statement, proof, displayed formula, count, classification table, assumption, or other mathematical passage is changed. Historical DRAFT/audit-pending sentences in the P02 body are retained; the updated header and this closure record govern current status.
- Corrected body SHA-256: `8a061ba81c7ffd2d05b188b9fca4ec1b94bc132147f7f664c8523f0a5f32560c`. Scope: UTF-8 bytes from the first `\section{P02:` line through EOF.
- Corrected full-file SHA-256: `8e057c2cd009659eee45906844e25f4f38c156e5eb2e4130e824aa5e8299c51a`.

The manifest, current P02-owned registry status cells, and compendium banner record this closure. No optional revision or new mathematics is authorized or undertaken; P03 is not begun. Build and byte-preservation results follow below.

### A02 closure build and preservation checks

- Build: PASS using the existing `latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex` workflow; regenerated compendium is 45 pages.
- Diagnostics: the same three underfull-hbox diagnostics in unchanged `02_theorem_dependency_map.tex` (source lines 126–127, 129–130, and 130; badness 1286, 1275, and 10000). No overfull boxes, undefined references, duplicate-label warnings, macro conflicts, or LaTeX/package warnings.
- Visual check: the regenerated status page and corrected continuity page were rendered and inspected; no clipping or layout defect was found.
- P02 body comparison: exactly the single E01 text replacement and no other body change. All 2 theorem, 3 proposition, 1 corollary, 6 proof, 18 equation, 2 align, and 3 tabular environments, plus every unnumbered displayed formula, are byte-identical to v1.0.
- P01 and all P03–P18: all 17 full source files are byte-identical to the exact audited pre-closure project. Every other pre-existing source or audit file outside the four authorized edits is also unchanged; only the compendium reading PDF is regenerated.
- Source/claim preservation: compendium input order and every registry claim's mathematical text, classification, and archival locator are unchanged. Only P02-owned status cells are promoted.
- The supplied A02 PDF is added as the audit evidence; its original verdict and original audited hash are preserved. No A02 TeX source is fabricated.
- Current delivery: `cyclic_network_project_P02_audited.zip`. The 58-file prior project inventory is retained and the supplied A02 PDF is the sole new project member (59 members total). Archive CRC and exact member-byte agreement are checked before delivery. The prior local draft ZIP and uploaded audit PDF remain unchanged.

## P03 draft and validation record — 2026-09-27

**Current status: P01 and P02 VERIFIED / AUDITED; P03 DRAFT; P04–P18 TODO.** This supersedes historical status wording above only for P03. No independent A03 audit has been performed, and neither symbolic checks nor compilation verify the mathematics. The canonical model, notation, dependency map, frozen scope, and literature decisions are unchanged. No work on P04 was begun.

### Current source selection and provenance

The authoritative input is `cyclic_network_project_P02_audited.zip`, SHA-256 `1159236d96b587a2bb8f71531557f5db3218e2ada2c447afd23024b823dffe9f`. The older `cyclic_network_project` and `cyclic_network_project 2` folders contain P02 placeholders; `p02_audit_input` is the audited P02 v1.0 draft. Neither replaces the supplied current v1.1 archive. All fourteen requested current files were located and consulted before mathematics began. The input digests below refer to pre-P03 versions.

| Current input | Full-file SHA-256 |
|---|---|
| `project_manifest.md` | `17c830f153f3943e327550b88e6ce74de00b89269caeca553e6907b65a4734e3` |
| `claim_registry.md` | `ad281531ca386d07ce6e14cf6c985cabd3436136de6c695cd0a4f2aa157472fb` |
| `frozen_theorem_package.md` | `724adf3d04a7f9661a2e53fbae359192e8a5a5ee56737bdca2379209b556ea63` |
| `final_novelty_verdict.md` | `5fa8ddd5ada9628b104dba68dd535356442c5e62ec45b72f3c2c354dec6037ea` |
| `02_theorem_dependency_map.tex` | `a1a4435f36fc1d1b6f0b2c5226a913283c76658d55b96493e6c50a8693831cac` |
| `proofs_compendium.tex` | `ea81554a1b0f4e22137b8199737c97b5587abf6ca8bc854e52365ba2be9d4d65` |
| `shared_macros.tex` | `f4a18a440e1214b619bf18f4a81fee507239460ca796d8ca3916791069d6a7ad` |
| `00_canonical_model.tex` | `c209981cb2924e8a782f24aa2904e8c85a105ff99319dd6aada12f48a351c2a4` |
| `01_notation_and_assumptions.tex` | `97d993c6d3986524dbcc29659ee73d257be1b03a35c44401e8ef4534303eeb91` |
| `proofs/P01_wellposedness_and_absorbing_box.tex` | `0d6950821aa83f3d09e8bfe84dab2b0b5020aa6e7881cf6928e984bff1890f1e` |
| `audits/A01_wellposedness_and_absorbing_box.tex` | `8d5c1b2ec782dbe49b07d2bbe529ee474d4c142695c53b523ccb41d63bb33098` |
| `proofs/P02_synchronous_subspace_and_equilibria.tex` | `8e057c2cd009659eee45906844e25f4f38c156e5eb2e4130e824aa5e8299c51a` |
| `audits/A02_synchronous_subspace_and_equilibria.tex` | `ca3d723d9fcfac14f5129583441e611a65e41848ec44f3b5e3a0072f795d84ac` |
| `proofs/P03_origin_and_linearization.tex` | `8906056fbc57d1de4110395f68dfcfbf2e354cb5b69d5a3efc6b756d9832677e` |

The current archive omitted the A02 TeX source, but its exact original was located at the workspace's `audits/A02_synchronous_subspace_and_equilibria.tex`. It matches the member of `cyclic_network_project_A02_audit_only.zip` and the digest recorded in `audits/A02_support/delivery_checks.json`. Its paired PDF is byte-identical to the current archive's A02 PDF (SHA-256 `089f40bfd3d8c0b62fb6eda7eac391c093bb023b150a88771a5cd00b5e23eff6`). The source is restored unchanged to this package. The prior statement that it had not been supplied or located is historical, as is the corresponding comment preserved in P02. A02 continues to record its original verdict against P02 v1.0; the current P02 v1.1 header and audit-closure record remain authoritative. Neither P01 nor P02 was edited.

### P03 statements and scope

P03 v1.0 derives every Jacobian entry directly from the canonical field, using summed modular Kronecker symbols and a separate directional-derivative check. The origin matrix is `J(0)=(a-g)I+cP`; with the positive-exponent project Fourier vectors, `lambda_m=a-g+c exp(-2 pi i m/n)`. Every eigenvalue is simple and the unique real-part maximizer is m=0, giving spectral abscissa `mu=a+c-g`. Linear asymptotic stability holds exactly for mu<0, linear instability exactly for mu>0, and the linear system is stable but not asymptotically stable at mu=0. Nonlinear boundary stability is not classified.

Full nonhyperbolicity holds exactly when `g=a+c cos(2 pi m/n)>0` for some mode. Consequently the full nonhyperbolic set can overlap the linearly unstable region and depends on n, whereas the spectral-abscissa sign does not. Neither criterion depends on q or gcd. At mu=0, only mode zero has zero real part; its zero eigenvalue has algebraic and geometric multiplicity one. Elsewhere, a nonuniform zero is possible exactly for even n, m=n/2, g=a-c>0; the origin is then already unstable through m=0. This is not a bifurcation assertion.

For any synchronous state x*>-1, P03 gives the unsimplified coefficients and `J=dI+CP+GP^(-q)-HP^q`. It then applies P02's nonzero-equilibrium relation only to the optional diagonal simplification. Collision sums are `(C-H)P` at q=1, `(C+G)P` at q=n-1, and `(G-H)P^(n/2)` for even n,q=n/2; the list is exhaustive under n>=5. Circulant structure is proved through the polynomial in P. P04's general homogeneous spectrum/normality and P09's nonlinear boundary conclusions remain deferred.

### Internal symbolic and secondary numerical checks

All checks passed. These are internal corroboration; the analytic proofs in P03, not finite computation, establish the proposed universally quantified statements. Python 3.12.14 and NumPy 2.3.5 were used. SymPy is unavailable; exact integer sparse-polynomial arithmetic and rational Gaussian elimination are implemented directly. Differentiation uses the numerator and denominator of the actual modularly identified canonical vector field, then cross-multiplies to compare polynomial coefficients; it does not import the proposed Jacobian for the differentiation step.

For every n=5,...,10 and every q=1,...,n-1 (39 pairs), checks comprise 2,570 generic general-Jacobian entry identities, 5,140 separate rational-derivative identities, 2,570 origin reductions, 2,570 generic-symbolic synchronous-state identities, 5,140 shift-orientation entries, and 910 collision-form entries. Coverage includes six q=1 pairs, six q=n-1 pairs, and all three even half-offset pairs. Exact origin checks comprise 355 root-of-unity exponent identities, six independent sparse-determinant identities, six boundary characteristic-derivative identities, and six exact rank(P-I)=n-1 calculations. Three even-dimension examples also check the nonuniform zero away from mu=0. The elementary cosine inequality and root-of-unity argument in the proof, not numerical tolerance, settle spectral ordering and simplicity for arbitrary n.

Additional universal polynomial identities check the P02-only diagonal simplification and the independent synchronous row-sum derivative. Two generic cancellation identities and all 61 entries of two named positive-equilibrium matrices were checked exactly: r=1, (n,q)=(5,1), (a,k,c,g,h)=(5/2,1,2,3,1) gives C=H=1; r=1, (n,q)=(6,3), parameters (7/2,1,1,4,1) gives G=H=1.

Secondary finite differences use NumPy PCG64 seed 20260927. For each of the 39 pairs, the parameter vector is sampled uniformly from [0.2,2.3)^5. The eight states are the origin; synchronous r=-0.65,0.25,1.5; a positive synchronous equilibrium r=0.4; and three nonsynchronous vectors sampled coordinatewise from [-0.7,2), [0.05,3), and [-0.8,0.6). For the equilibrium case only, replace a by (k+h)r+0.4 and g by c+0.4(1+r), retaining the other sampled coefficients. This keeps every coefficient positive and enforces the equilibrium relation. Each coordinate uses a centered difference with step `1e-5 max(1,abs(x_j))`; all perturbed states stay in U.

The 312 states give 20,560 finite-difference entries. The entrywise scaled error is `abs(J-J_FD)/(1+max(abs(J),abs(J_FD)))`, with tolerance 1e-7. The worst scaled error is 2.6907607135803086e-9 and worst absolute error is 7.230752174791633e-8. Direct versus homogeneous matrices agree exactly in floating arithmetic across 12,850 entries. Twenty-four origin parameter/dimension cases test 180 eigenvector relations, with worst residual 1.1889678785578623e-15. Stable, boundary, unstable, even nonuniform-zero, and odd control cases are included. No positive-state eigenvalue formula, normality theorem, trajectory integration, or bifurcation computation is performed.

The separately delivered `P03_validation_support.zip` contains the portable checker, exact input records (including floating-point hexadecimal strings), compact results, and usage instructions. It is kept outside the project ZIP to avoid adding mathematical modules or changing numerical plans. The checker and its finite test results do not replace an independent P03 audit.

### Priority checks for the independent P03 auditor

1. Re-derive both rational derivatives and every Jacobian contribution from the canonical equation.
2. Check modular addition, the three exhaustive collision cases, and possible coefficient cancellation.
3. Verify predecessor-shift orientation and the negative DFT exponent at the origin.
4. Prove the unique origin real-part maximizer, the full nonhyperbolic set, and both multiplicities of the boundary zero; include the even-n zero away from the boundary.
5. Distinguish linear stability from nonlinear boundary behavior, and apply P02's simplification only at a nonzero equilibrium.
6. Confirm all protected files and scope boundaries, including the deferred P04/P09 claims.

### P03 build, preservation, and exact delivered version

Compilation: **PASS**, using `latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex` with an external build directory; pdfLaTeX/TeX Live 2026 and latexmk 4.88. The regenerated reading copy has **50 pages**, with P03 on **26–31**. The title/contents and all six P03 pages were rendered and visually inspected; no clipping, overlap, or new spacing defect was found.

Diagnostics: **three pre-existing underfull-hbox diagnostics**, all in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130, and 130–130 (badness 1286, 1275, 10000). **No overfull boxes, undefined references, duplicate labels, macro conflicts, LaTeX/package warnings, or compilation errors.** All 171 labels in the included source tree are unique. Compilation is not mathematical verification.

Byte-preservation checks against the current P02-audited ZIP pass: P01 and P02, all P04–P18 files, A01 and the supplied A02 PDF, the canonical model, notation, shared macros, dependency map, immutable blueprint, numerical plans, and every literature/frozen-scope file remain unchanged. Existing files changed are exactly `proofs/P03_origin_and_linearization.tex`, `project_manifest.md`, `claim_registry.md`, `proofs_compendium.tex`, and the regenerated `proofs_compendium.pdf`. The only added project member is the authenticated, unchanged A02 TeX source. Historical records remain intact except the explicitly current status cells/banner. The compendium input order and existing claim classifications, mathematical text, and archival locators are preserved. No P04 mathematics was begun.

The updated project ZIP contains 60 members. Build intermediates and checker outputs are excluded; the separate validation-support ZIP contains reproducible checks and build/preservation evidence. Archive CRC integrity and exact member-byte agreement with the delivered project folder are checked before delivery.

| Delivered component | SHA-256 |
|---|---|
| `proofs/P03_origin_and_linearization.tex` | `0f87f315817429ddb949af5bc6d38db32a0cb6a8f7715dfe941840becd527776` |
| `proofs_compendium.tex` | `c9cad0e029f4f43fcfbc4d6375c1a4f3b43a6342d51d906ec434a822406a10bb` |
| `proofs_compendium.pdf` | `4245c11b6de769aef1b4b2a72ebc4bfd4f6ca732341b416c610dd8bc4e988478` |
| Portable P03 checker | `73784fd269f445a80639175b8901610e89a517469d69ddc5d397200dc5412bbb` |

Current delivery: `cyclic_network_project_P03_draft.zip`; optional reproducibility companion: `P03_validation_support.zip`. P03 remains DRAFT pending independent audit.

## P03 audit closure — 2026-09-27

**Current status: P01, P02 and P03 VERIFIED / AUDITED; P04–P18 TODO.** A03's independent verdict is **VERIFIED**, with no required mathematical or wording correction. This entry supersedes historical P03 DRAFT/audit-pending status prose. The closure is administrative only; P04 has not been begun and no new mathematics is introduced.

- Audit source: [audits/A03_origin_and_linearization.tex](audits/A03_origin_and_linearization.tex).
- The audit-only package's 15 files (source, PDF and original support records) are added verbatim. Its SHA-256 is `3ef6a0b0f96319fcbcb919574100a838064ce3cf381a1beeaa675ca281b9753c`. Audit source SHA-256: `e1008f98ba9667b92b8d74f1bc7d21e021414b454ac976ae0db1500b4b7ef8d1`; audit PDF SHA-256: `c817b753f257d27471c416925fb97ddaef6ae539ee980d80705aaa8fa9b7f0b2`.
- Exact current input: `cyclic_network_project_P03_draft.zip`, SHA-256 `768c76b7b53e0af2807d3eab81cbe38134425c3ff477585559428b9614d1fb96`. All 13 audit-input hashes match this archive. Older local placeholders are excluded.
- Audited version: **P03 v1.0, 2026-09-27**, 18,921 bytes and 433 lines; full-file SHA-256 `0f87f315817429ddb949af5bc6d38db32a0cb6a8f7715dfe941840becd527776`.
- Audited and current body SHA-256: `07d76c8ce0b5232827e9f2c74245188b55b0ce0d1732b3cb2e528d69e8d6b50a`. Scope: UTF-8 bytes beginning with the first line-anchored section command through EOF, including whitespace and final newline.
- Current verified version: **P03 v1.1, 2026-09-27**, a metadata-only closure; full-file SHA-256 `6c3c9bfb2307bdc043eb7f6a874cb222e2ac2ce0750b339181f0088dd0bd859e`. The P03 header records the invariant body hash and points here for the full-file digest, avoiding a self-referential hash.
- The mathematical body is byte-for-byte identical to the independently audited v1.0 body. This includes the old DRAFT/audit-pending sentences; they remain historical because the user explicitly required preservation. The current header, this closure record and the compendium banner govern status.
- Only P03's comment header, this manifest, P03-owned registry status cells, and the compendium's current status/date prose are updated. The regenerated compendium PDF is a reading copy. No mathematical correction, optional wording suggestion, proof revision or audit-source modification is applied.
- C034, C035, C037 and P03-D1–P03-D4 now carry VERIFIED / AUDITED status. Their statements, classifications, locators and scope are unchanged. No later claim is promoted.

| Added audit record | Status | Scope |
|---|---|---|
| [A03 source](audits/A03_origin_and_linearization.tex) | VERIFIED; preserved unchanged | Independent audit of exact P03 v1.0; no correction required |
| [A03 reading copy](audits/A03_origin_and_linearization.pdf) | Preserved unchanged | Supplied 12-page audit PDF |
| [A03 support](audits/A03_support/README.md) | Preserved unchanged | Original provenance, exact checks and reproduction records; no scripts rerun for this administrative closure |

### A03 closure compilation and preservation checks

- **Compilation: PASS.** pdfLaTeX / TeX Live 2026 with `latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex`, using a separate output directory. The rebuilt reading PDF has 50 pages; P03 remains on pages 26–31. Only title/contents pages 1–2 have changed text; they were rendered and visually inspected with no clipping or overlap.
- **Diagnostics:** the same three pre-existing underfull-hbox spacing diagnostics in unchanged `02_theorem_dependency_map.tex`, source lines 126–127, 129–130 and 130–130 (badness 1286, 1275 and 10000). No overfull boxes, undefined references, duplicate labels, macro conflicts, LaTeX/package warnings or compilation errors. All 171 labels in the included source tree are unique. Compilation is not mathematical verification.
- **P03 body: PASS, byte-for-byte unchanged.** The prefix changes are comment metadata only. The body hash above matches the exact audited v1.0 body, including historical status prose.
- **Other proof preservation: PASS.** P01, P02 and P04–P18 (17 complete source files, not just their mathematical bodies) are byte-identical to the current draft project. No P04 work was begun.
- **Remaining project preservation: PASS.** Every other existing file outside the four authorized source edits and regenerated compendium PDF is byte-identical. The model, notation, shared macros, dependency map, archived blueprint, numerical plans, prior audits and literature files are unchanged. The compendium input sequence is unchanged.
- **Registry preservation: PASS.** All 170 archival C-rows and 12 additional P01–P03 claim rows are retained. Only C034, C035, C037 and P03-D1–P03-D4 status cells changed; every nonstatus cell is unchanged.
- **Audit inclusion: PASS.** All 15 supplied A03 members are copied byte-for-byte, retaining original verdicts, audited-version hashes and support data. They are the only added project members; the final inventory is 75 files.
- **Packaging: PASS.** The updated ZIP has valid CRCs and its member bytes match the delivery folder. Prior draft and audit-only ZIPs are preserved. Build intermediates are outside the project ZIP.

Current delivery: `cyclic_network_project_P03_audited.zip`. P03 v1.1 is VERIFIED / AUDITED by metadata-only closure; no mathematical corrections were required or applied.

## P04 draft and internal validation — 2026-09-27

**Current status: P01–P03 VERIFIED / AUDITED; P04 v1.0 DRAFT; P05–P18 TODO.** This record supersedes historical P04-placeholder statements only. P04 is supporting / known machinery under the unchanged Phase 1C novelty decision. No independent A04 audit or VERIFIED status is claimed. The only new mathematical body is P04. No P05 selection, Hopf analysis or new literature search was performed.

### Current-file selection and provenance

All sixteen requested current files were located before mathematics began. Authoritative input: `cyclic_network_project_P03_audited.zip`, SHA-256 `5f861b1ec231201637620c8cd84409bd2f971003a46907ee3f205f443f6d222c`. Its 75 members match the prior P03-audited delivery folder byte-for-byte and its hash matches the external A03 closure log and checks. P01/P02/P03 v1.1 full-file and body hashes agree with their closure records. Older local placeholders and draft archives were excluded. Historical DRAFT prose and P02's obsolete absent-A02-source comment remain preserved under the current closure metadata.

| Current input (before P04 edits) | Full-file SHA-256 |
|---|---|
| `project_manifest.md` | `10a0a3aa29b5732a5533f299d94f30243bc9c7057a263e6d382e7d841fedaa59` |
| `claim_registry.md` | `50a128d1b304453f66ecf51939240a9f95968aab0465c113a411d80ce226a6b2` |
| `frozen_theorem_package.md` | `724adf3d04a7f9661a2e53fbae359192e8a5a5ee56737bdca2379209b556ea63` |
| `final_novelty_verdict.md` | `5fa8ddd5ada9628b104dba68dd535356442c5e62ec45b72f3c2c354dec6037ea` |
| `02_theorem_dependency_map.tex` | `a1a4435f36fc1d1b6f0b2c5226a913283c76658d55b96493e6c50a8693831cac` |
| `proofs_compendium.tex` | `825e5ef2d563a1dab48c1826b40d62078032d333599284fce2a17c01db7307a5` |
| `shared_macros.tex` | `f4a18a440e1214b619bf18f4a81fee507239460ca796d8ca3916791069d6a7ad` |
| `00_canonical_model.tex` | `c209981cb2924e8a782f24aa2904e8c85a105ff99319dd6aada12f48a351c2a4` |
| `01_notation_and_assumptions.tex` | `97d993c6d3986524dbcc29659ee73d257be1b03a35c44401e8ef4534303eeb91` |
| `proofs/P01_wellposedness_and_absorbing_box.tex` | `0d6950821aa83f3d09e8bfe84dab2b0b5020aa6e7881cf6928e984bff1890f1e` |
| `audits/A01_wellposedness_and_absorbing_box.tex` | `8d5c1b2ec782dbe49b07d2bbe529ee474d4c142695c53b523ccb41d63bb33098` |
| `proofs/P02_synchronous_subspace_and_equilibria.tex` | `8e057c2cd009659eee45906844e25f4f38c156e5eb2e4130e824aa5e8299c51a` |
| `audits/A02_synchronous_subspace_and_equilibria.tex` | `ca3d723d9fcfac14f5129583441e611a65e41848ec44f3b5e3a0072f795d84ac` |
| `proofs/P03_origin_and_linearization.tex` | `6c3c9bfb2307bdc043eb7f6a874cb222e2ac2ce0750b339181f0088dd0bd859e` |
| `audits/A03_origin_and_linearization.tex` | `e1008f98ba9667b92b8d74f1bc7d21e021414b454ac976ae0db1500b4b7ef8d1` |
| `proofs/P04_arbitrary_nq_fourier_spectrum.tex` | `b68f6b7b45ccc985545187c885f5a5966f8582462eeb0e7f3234e1234f22ffae` |

### Completed draft statements and boundaries

P04 reconstructs the shift phases directly from P03, obtaining `lambda_m=d+C exp(-i theta_m)+G exp(i q theta_m)-H exp(-i q theta_m)`. Its real and signed imaginary parts are `d+C cos(theta_m)+(G-H) cos(q theta_m)` and `-C sin(theta_m)+(G+H) sin(q theta_m)`. A geometric-sum proof supplies the unitary DFT with the project's exact normalization; full diagonalization gives normality and numerical eigenvalue multiplicity equal to the number of matching labels. Algebraic and geometric multiplicities coincide; Fourier labels are not all simple numerical eigenvalues.

Conjugacy uses `(-m) mod n`; only 0 and (for even n) n/2 are singleton labels. Their eigenvalues are `d+C+G-H` and `d-C+(G-H)(-1)^q`. Non-singleton pairs can share real eigenvalues, as shown by the exact positive-equilibrium example q=1, x*=1, (a,k,c,g,h)=(2,1,4,4,1). All three collision cases reduce directly from the same master formula, including cancellations. No coprimality hypothesis is used. The step-q permutation alone has gcd(n,q) cycles of length n/gcd(n,q); this is no full-network disconnection or block-decomposition claim.

At all synchronous states, lambda_0=f'(x*). At a positive (or other nonzero admissible) synchronous equilibrium, the optional diagonal simplification from P03 and the two lambda_0 identities are derived with the equilibrium hypothesis explicit. No comparison among the other growth rates is made. At a synchronous equilibrium, linear exponential stability holds exactly when `sa(J)=max_m r_m<0`, and `||exp(tJ)||_2=exp(t sa(J))` for t>=0. Zero abscissa gives linear Lyapunov stability without attraction; positive abscissa gives linear instability. Hyperbolicity requires every r_m to be nonzero, even if no eigenvalue is zero.

Nonlinear local exponential stability for negative abscissa is proved by a remainder estimate and Gronwall. The standard C^1 linearized-instability theorem is stated with all hypotheses checked for positive abscissa. At zero abscissa linearization is generally inconclusive; two scalar examples illustrate the limitation without classifying DM boundary behavior. These are local statements in the open domain, with no global-attraction claim. A fixed-point dominant-label set retains every tie; first instability additionally needs a branch, oriented path, prior stability and a crossing.

C008, C011, C038–C041 and C153 have updated P04-only status cells; archival claims and owners are preserved. C040 and C153 remain rejected as blanket assertions. New draft records P04-D1–D5 capture precise replacement/support statements. The optional semigroup identity is included as explicitly requested P04 support; C042 keeps its P17 owner and TODO status, with no P17 response analysis or promotion. No shared macro or dependency-map change was needed.

### Internal checks and reproducibility

All internal analytic review and computational checks passed; neither constitutes an independent A04 audit. Python 3.12.14 and NumPy 2.3.5 were used, seed 40420260927, with no additional packages or network access. The portable checker and complete per-case input/result records are supplied separately in `P04_validation_support.zip`, keeping the project inventory and numerical plans unchanged.

Coverage is all 39 pairs `5<=n<=10, 1<=q<n`: 522 matrices, 4,144 eigenvalue occurrences, 264 positive states, 141 negative states in (-1,0), 117 origins, and 312 equilibrium matrices (including origins). This includes all requested examples (5,2), (6,2), (6,3), (7,1), (8,4), every tested q=n-1, 172 noncoprime cases, 15 explicit cancellations, and six repeated-real-eigenvalue controls. There are 84 q=1, 84 q=n-1 and 42 half-offset matrices. Stable, zero-abscissa and unstable origin/positive-equilibrium controls are included. Finite stability classifications are diagnostic only, not a mode-selection theorem.

The direct matrix accumulates each canonical derivative contribution at modular column indices, independently of the shift-polynomial and Fourier implementation. NumPy eigendecomposition is matched to all Fourier values by a one-to-one bottleneck assignment, retaining multiplicity. Matrix entries, shift orientations, DFT normalization, diagonalization, signed dispersion, conjugacy, singletons, collision reductions, numerical cluster counts/SVD nullities, normality, row sum and equilibrium substitutions are checked. The numerical clusters do not prove exact multiplicities. The largest scaled eigenvalue error is 5.9441661113841894e-15; full diagonalization error is 5.444622457435257e-15; normality error is 1.8704877555222115e-16. Non-exponential checks use tolerance 2e-10. Matrix residuals are scaled by max(1,||J||_2), or its square for normality; unitary/shift residuals are unscaled.

A separate real-matrix Taylor scaling-and-squaring exponential uses no Fourier spectral input. At t=0,0.125,0.75,2 it supplies 2,088 matrix/time checks. SVD gives the induced norm, compared to exp(t max Re(lambda)); the worst relative norm error is 1.6820400089081265e-13 and the worst matrix relative error is 4.610186087864788e-13, below tolerance 5e-10. Five exact rational cleared-denominator polynomial checks corroborate the row-sum derivative, equilibrium diagonal, two lambda_0 forms and the scalar polynomial derivative/discriminant identity. These finite computations are not proof premises.

### Priority checks for the independent P04 auditor

1. Authenticate the current P01–P03 and audit versions; retain P04's DRAFT status and supporting role.
2. Reconstruct all three shift phases and the imaginary G+H sign.
3. Check normalization, complete unitary diagonalization, numerical eigenvalue multiplicities and nonsingleton real pairs.
4. Verify all three offset collisions, cancellations, m=0 and the even-n singleton parity formula.
5. Check lambda_0=f'(x*) without equilibrium; restrict equilibrium simplifications to their hypotheses.
6. Check normality, the t>=0 norm identity and both directions of the linear exponential-stability criterion.
7. Keep hyperbolicity, zero eigenvalue, zero abscissa, local nonlinear stability and global attraction distinct; check the standard instability theorem hypotheses.
8. Verify step-q cycles without imposing coprimality; require branch/path/prior stability/crossing data for first-instability language.
9. Treat internal checks and compilation as corroboration, not mathematical verification; confirm no P05 or Hopf analysis.

### Compilation, preservation and delivery

Compilation: **PASS**, pdfLaTeX / TeX Live 2026 with latexmk 4.88, external build directory, command `latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex`. Final PDF: **57 pages**, P04 on **32–39**. The front matter and all eight P04 pages were rendered and visually inspected; no clipping, overlap or layout defect was found.

Diagnostics: the same **three pre-existing underfull-hbox spacing warnings** in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130, badness 1286, 1275 and 10000. **No undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings, or compilation errors.** All 194 labels in the included source tree are unique. Compilation is not mathematical verification.

Existing files changed are exactly P04, `project_manifest.md`, `claim_registry.md`, `proofs_compendium.tex`, and the regenerated `proofs_compendium.pdf`. All other 70 members are byte-identical to the authoritative input, including complete P01–P03 and P05–P18 files, canonical model/notation/macros/dependency map, all audits/support files, literature/frozen-scope files, numerical plans and archived blueprint. There are no added or removed project members. Compendium input order and every original registry nonstatus cell are unchanged; only the seven identified P04 status cells change, with five new P04 draft rows appended. The separately delivered support ZIP contains computations and build/preservation evidence, not a new theorem or audit module.

The updated project ZIP retains 75 members, passes CRC checks, and matches the delivered project folder byte-for-byte. Build intermediates are excluded. Delivery: `cyclic_network_project_P04_draft.zip`; companion: `P04_validation_support.zip`.

| Delivered component | SHA-256 |
|---|---|
| `proofs/P04_arbitrary_nq_fourier_spectrum.tex` | `ab80f695b3e20c852c572b7b174ecaf9964eac1aba62e3e55b2b4d3e60754e0c` |
| `proofs_compendium.tex` | `7acc9796e47c47a91d6e32b192dddc15c8e0c164be3b8c59db201265ef8137b5` |
| `proofs_compendium.pdf` | `03f8a67acab7018fd1e5389889967155d82f5d029ae7796d8d1fc4a7c64c8163` |
| Portable checker | `e5d1690f1945777e202f2620bdcc51e3f4eea103ed973c06273815756936a871` |

## P04 audit closure — 2026-09-27

**Current status: P01–P04 VERIFIED / AUDITED; P05–P18 TODO.** A04's independent mathematical verdict is **VERIFIED**, with no required mathematical or wording correction. This administrative entry supersedes historical P04 DRAFT/audit-pending status prose. No mathematical revision or optional wording adjustment is made. P05 has not been begun.

- Audit source: [audits/A04_arbitrary_nq_fourier_spectrum.tex](audits/A04_arbitrary_nq_fourier_spectrum.tex).
- The audit-only package's 12 files (source, PDF and original support records) are added verbatim. Its SHA-256 is `806fcd65b2b0230a233b762950e2927b55aae8a035172a2a0073e5b544278f4a`. Audit source SHA-256: `8a57079241269c92a3c3e8dc4dccf8592da2d1a636fca0c0990a4f318396d869`; audit PDF SHA-256: `90819c883fc561c2a1c4435186b2b501488e1b13699e2c1073a95bff6e982359`.
- Exact current input: `cyclic_network_project_P04_draft.zip`, SHA-256 `11a2383d3f61e001c400f61744d6cacd94b0b02d670bd7240e0dbb948fc0610f`. Both local draft ZIP copies agree. All 16 A04 input-hash records and its complete 75-member archive inventory match this archive. Older placeholders are excluded.
- Audited version: **P04 v1.0, 2026-09-27**, 25,792 bytes and 573 lines; full-file SHA-256 `ab80f695b3e20c852c572b7b174ecaf9964eac1aba62e3e55b2b4d3e60754e0c`.
- Audited and current mathematical-body SHA-256: `3e3d58230c87af3b5f07069d61065362dc081d172ad3b236057fefda25fa5653`. Scope: UTF-8 bytes beginning at the first line-anchored section command through EOF, including every whitespace byte and the final newline (25,137 bytes).
- Current verified version: **P04 v1.1, 2026-09-27**, a metadata-only closure; full-file SHA-256 `1331c8598acd0481046250d918cac028ca6d13d2604612448c3459e864321c58`. The P04 header records the unchanged body hash and points here for the full-file digest, avoiding a self-referential hash.
- The complete mathematical body is byte-for-byte identical to audited v1.0, including historical DRAFT/audit-pending text, numerical-check statistics and the auditor-priority checklist. Current metadata, this closure record and the compendium status banner govern the current status.
- Only P04 comment metadata, this manifest, P04-owned registry status cells and an appended closure note, and the compendium's status/date prose change. The regenerated compendium PDF is a reading copy. No proof, formula, assumption, claim text, optional A04 T01 notation suggestion, audit source or historical statistics are revised.
- C008, C011, C038–C041, C153 and P04-D1–P04-D5 now record VERIFIED / AUDITED P04 results. Archival classifications, mathematical statements, locators and owners are preserved. C040/C153's blanket assertions remain rejected; their precise replacement statements are audited. C042 remains P17-owned and TODO; no later claim is promoted.

### Nonblocking reproducibility note: A04 U01

The original P04 validation companion was unavailable to the independent auditor. Consequently the historical numerical-check counts and floating-point error maxima in audited P04 v1.0 lines 530–545 were not independently reproduced. A04 labels that historical computational provenance UNRESOLVED; its newly written exact checks are independent corroboration, not reproduction of the old run. These statistics are not theorem premises. **This note is nonblocking and A04's mathematical verdict remains VERIFIED.** This administrative closure does not rerun either checker, certify the historical statistics, or claim to resolve U01. Their preserved historical wording in P04 is governed by this qualification.

| Added audit record | Status | Scope |
|---|---|---|
| [A04 source](audits/A04_arbitrary_nq_fourier_spectrum.tex) | VERIFIED; preserved unchanged | Independent mathematical audit of exact P04 v1.0; no correction required |
| [A04 reading copy](audits/A04_arbitrary_nq_fourier_spectrum.pdf) | Preserved unchanged | Supplied 14-page audit PDF |
| [A04 support](audits/A04_support/README.md) | Preserved unchanged | Original provenance, line review, independent exact checker and results; no scripts rerun for closure |

### A04 closure compilation and preservation checks

- **Compilation: PASS.** pdfLaTeX / TeX Live 2026 with latexmk 4.88, `latexmk -pdf -interaction=nonstopmode -halt-on-error proofs_compendium.tex`, using a separate output directory. The regenerated reading copy has 57 pages; P04 remains on pages 32–39. Changed title/contents pages 1–2 were rendered and visually inspected with no clipping or overlap.
- **Diagnostics:** the same three pre-existing underfull-hbox spacing diagnostics in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130 (badness 1286, 1275 and 10000). No undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings or compilation errors. All 194 labels in the included source tree are unique. Compilation is not mathematical verification.
- **P04 mathematical body: PASS, byte-for-byte unchanged.** The prefix edits are comment metadata only. The invariant body hash above matches the audited P04 v1.0 body, including historical status prose and numerical statistics.
- **All 18 proof bodies: PASS, byte-for-byte unchanged.** P01–P04 mathematical bodies and P05–P18 proof bodies match the current draft archive. Additionally, all 17 complete P01–P03/P05–P18 source files are byte-identical; no metadata in those modules was changed.
- **Remaining project preservation: PASS.** The only changed existing files are P04 comment metadata, `project_manifest.md`, `claim_registry.md`, `proofs_compendium.tex` and the regenerated `proofs_compendium.pdf`. The other 70 original members are unchanged. Canonical model, notation, shared macros, dependency map, literature files, prior audits/support, numerical plans and archived blueprint are preserved. The compendium input sequence is unchanged.
- **Registry preservation: PASS.** All 170 archival C-rows and 17 additional P01–P04 claim rows are retained. Only the seven P04-owned C-row status cells and P04-D1–D5 status cells change; every nonstatus cell is unchanged. An administrative closure note is appended. No later mathematical claim is promoted.
- **Audit inclusion: PASS.** All 12 supplied A04 members are copied byte-for-byte, retaining their original verdict, exact audited-version hashes, U01 qualification, optional T01 note and original support records. They are the sole added project members, for a final inventory of 87 files. No source audit or validation code was rerun.
- **Packaging: PASS.** The updated project ZIP has valid CRCs and member bytes matching the delivery folder. Prior draft and audit-only ZIPs remain unchanged. Build intermediates and external closure-delivery logs are excluded from the project ZIP.

Current delivery: `cyclic_network_project_P04_audited.zip`. P04 v1.1 is VERIFIED / AUDITED by metadata-only closure; A04 requires no mathematical or wording correction. U01 remains a nonblocking historical reproducibility note. P05 has not been begun.

## P05 strengthened draft and internal checks — 2026-10-02

**Current status: P01–P04 VERIFIED / AUDITED; P05 v1.0 DRAFT; P06–P18 TODO.** This entry supersedes historical P05-placeholder statements only. P05 awaits an independent A05 audit. Its intended MAIN THEOREM TARGET role applies only to the strengthened realizability result, not the routine quadratic reduction. Compilation and internal checks are not verification.

### Current-file selection

The authoritative baseline is `output/p04_audited/cyclic_network_project_P04_audited.zip`, SHA-256 `0b5da1dfca9447a4b4373041a355fe66de52a6dc99abb5278b2f8377707a266e`. Its 87 member bytes match the prior delivery folder, its hash matches the P04 closure record, and all 18 baseline module body hashes agree with that closure. All 19 requested current inputs were located before mathematical development; their sizes and full hashes are in the separate validation support. Older placeholders and pre-closure drafts were excluded. The audited P01–P04 files and audit records are unchanged, including the nonblocking historical P04 U01 provenance qualification.

### Draft theorem scope

- **Theorem A (`thm:P05-selection`):** `r(u)=d-T+Cu+2Tu^2`, with `T=G-H`; selection is independent of d. If T>=0 the unique representative is 0. If T<0, the exact rule is nearest cosine to `u*=C/[4(H-G)]`, with full endpoint cells and all ties. Interior closed cells are `[beta_j,beta_(j-1)]`. Maximal ties are adjacent only; Fourier-label counts retain conjugate pairs and singletons.
- **Theorem B (`thm:P05-reachable`):** reachable representatives are exactly `0,...,J`, `J=floor((n+1)/4)`. The midpoint identity is `beta_j=cos(pi/n) cos((2j+1)pi/n)`. Precisely beta_0 through beta_(J-1) are positive and give switch thresholds for `chi=4(H-G)/C`. For n=3 mod 4 the terminal selected cosine is negative. For n=2 mod 4 the formal zero-vertex tie is unattainable at finite parameters; its positive-versus-negative cosine growth-rate gap remains `2C sin(pi/n)`. The even Nyquist singleton is excluded.
- **Theorem C (`thm:P05-realization`):** choose x,c,g,v>0, set `h=g/(1+x)^2+c/[4(1+x)xv]`, choose `k>max(0,(c-g)/[(1+x)x]-h)`, and set `a=(k+h)x-(c-g)/(1+x)`. Every coefficient is positive, the original DM residual vanishes, and u*=v. Every reachable strict cell and positive-midpoint tie is therefore nonempty. Both signs of T and T=0 have exact canonical examples.
- **Local geometry:** in equilibrium coordinates `(x,k,c,g,h)`, projection to `(a,k,c,g,h)` has determinant `k+h+(c-g)/(1+x)^2`, which is strictly positive throughout the concave regime. Every strict cell has a nonempty open physical-parameter realization on a specified positive branch. Each positive-midpoint switch has regular level function `h-g/(1+x)^2-c/[4(1+x)x beta_j]`, with partial derivative 1 in h, giving a local smooth codimension-one hypersurface. No global identification across branch labels is claimed.
- **Separation from instability:** the exact family `x*=1, c=g=4, h=1+chi/2, a=k+h` realizes every positive chi. Around any switch choose fixed k larger than half the upper chi endpoint; all real parts stay below -1 while the dominant representative changes. No first-instability or Hopf theorem is asserted. Real-part ties do not imply complex-eigenvalue equality. Frequency, simplicity and first-crossing work remain deferred to P11/P12.

The module includes exact grids/midpoints for n=5 through 12, explicit uniform/nonuniform/tie examples, highest-mode examples for all four residue classes, the fixed-n large-restraint behavior, and an independent-auditor checklist. P07's polished five-node specialization, P08 and P11 were not begun. The frozen theorem package and novelty decisions require no amendment and are preserved unchanged. No new literature search or priority-clearance claim was made.

### Reproducible corroboration

The separate `P05_validation_support.zip` contains a standard-library-only Python checker and all per-case data, baseline/input hashes, structural preservation checker, final build evidence and visual-review spreads. The run used Python 3.12.14. Sixteen exact rational-function identities passed by sparse polynomial cross multiplication. Decimal evaluations use 100 digits with 112-digit trigonometric work and 120-digit pi; tolerance is 1e-70 on a max(1,magnitude) scale. These are finite-precision checks, not interval certificates or exact transcendental proofs.

Coverage: every n=5 through 40; 1,872 main cases; 5,616 direct original-P04 dispersion comparisons at three additive constants per case; all 198 positive-midpoint switches; several interior values in every cell and two offsets on each side of every switch; T>0, T=0, u*=1 and u*=1e-20; all four parity classes. There are 2,466 canonical realizations including 594 stable-path points, plus eight explicit proof examples. Every constructed example is checked in the original five-term DM equation. All checks passed. The largest main-case scaled original-DM residual is below 4.30e-100; the largest scaled quadratic-versus-trigonometric discrepancy is below 1.43e-79. Full counts, precision, inputs and errors are in the support results. None is a proof premise or independent audit result.

### Compilation, preservation and delivery

- **Compilation: PASS.** pdfLaTeX / TeX Live 2026 with latexmk 4.88; final compendium 66 pages, P05 on pages 41–49. The build uses an external output directory. Front matter pages 1–3 and every P05 page were rendered and visually inspected, with no clipping or overlap.
- **Final diagnostics:** three unchanged underfull-hbox warnings in `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130, badness 1286, 1275 and 10000. No undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings or compilation errors. All 218 labels in 28 included source files are unique. No new macros are defined by P05; table spacing changes are locally scoped.
- **Preservation: PASS.** Exactly five existing members change: P05, this manifest, the registry, compendium root and regenerated compendium PDF. The other 82 members are byte-identical, including all 17 other complete proof files, all audit sources/PDFs/support, canonical contract, notation, macros, dependency map, frozen/literature records, numerical plans and archive. No project members are added or removed; the compendium input sequence is unchanged.
- **Registry: PASS.** All 170 archival C-rows and their nonstatus fields are unchanged. Only C045–C048 status cells change; P05-D1–D5 are appended as DRAFT. No later claim is promoted.
- **Delivery:** `cyclic_network_project_P05_draft.zip` retains the 87-member project inventory, with a separate `P05_validation_support.zip`. ZIP checksums and byte comparisons are recorded externally to avoid self-referential hashes. Build intermediates are excluded from the project ZIP. Prior packages and all synced source material are preserved.

### Priority checks for the independent P05 auditor

1. Authenticate current P01–P04 closure versions and retain P05 DRAFT status.
2. Check square completion, descending-grid midpoint inequalities, both endpoint cells, the continuous endpoint versus the first discrete switch, and all maximal tie counts.
3. Derive the mod-4 classification and floor((n+1)/4), especially the reachable negative-cosine mode and the unattainable zero-midpoint boundary.
4. Check positivity and original-DM equilibrium residuals in both realization families.
5. Verify branch regularity, openness after projection and the local regular-level-set argument; do not infer a global manifold after forgetting branch labels.
6. Separate label ties from numerical-eigenvalue coincidence and dominance from first instability; inspect the stable switch path and confirm no hidden use of P07/P08/P11–P13.

## P05 audit closure — 2026-10-02

**P05 v1.1: VERIFIED / AUDITED AFTER MINOR REVISION.** P01–P04 remain VERIFIED / AUDITED; P06–P18 remain TODO. A05 E01 is the sole required correction and has been applied verbatim. P08 is now cleared to begin under the frozen attempt order and comparison conventions; no P08 or later module is begun. This current closure supersedes historical P05 DRAFT/audit-pending status prose without rewriting that history.

### Exact versions, audit and required correction

- Audit: [audits/A05_q2_mode_selection.tex](audits/A05_q2_mode_selection.tex), immutable audit of original **P05 v1.0, 2026-10-02**, 26,848 bytes and 591 lines.
- Original P05 full-file SHA-256: `b7123736242554bd7fc1f6a56d8788b6c5413a25930e5360d7ea5babe44184d4`.
- Original P05 body SHA-256: `25ab3e4ed5d871ab2884210e6d8e7f3631acee3f7a1c662d3c33de441048810d`.
- Corrected version: **P05 v1.1, 2026-10-02**.
- Corrected P05 full-file SHA-256: `054a047a55ef37815485f6c225be2f6322ca8cf1c272614dd1dc4bb10ae8e1dd`.
- Corrected P05 body SHA-256: `7e1fd7765ed81e9c5f24ebe07e450e3fd76caf6b16264aac3c3a21edacd8bb97`.
- Body hashes cover every byte from the first line-anchored section command through EOF. The full-file digest is stored here rather than inside the hashed file, avoiding a self-referential hash.
- Immutable A05 source SHA-256: `0f7e9836b91009a201185a4acbbb99715f3c65df715e405962b7d6852ff27031`.
- Original A05 verdicts: **CORE MINOR REVISION; REALIZABILITY VERIFIED; OVERALL MINOR REVISION**. These original verdicts are preserved, not retroactively changed.
- Closure disposition after E01: **VERIFIED / AUDITED AFTER MINOR REVISION**.

Original E01 sentence (audited P05 lines 30–31):

> Selection always includes mode zero and means maximizing the real part at this equilibrium, retaining all ties.

Exact replacement requested by A05 and applied here:

> The maximization is over all Fourier labels, including mode zero, and selection means the complete set maximizing the real part at this equilibrium, retaining all ties.

The following coprimality sentence is unchanged. Mode zero is a candidate in the maximization; selected representatives are exactly those attaining the maximum, including all ties. No theorem statement, displayed formula, definition, selection inequality, boundary, parity result, realization, geometry argument, stable-switch construction, example, proof or validation result is changed. All other mathematical-body bytes, including historical DRAFT/audit-pending prose, are preserved; the current header, this closure and compendium banner govern lifecycle status.

### Input authentication and immutable audit inclusion

The authoritative full baseline is `cyclic_network_project_P05_draft.zip`, SHA-256 `e82f95c958744643ca54ddc06fdd0e3e30c47e8e577ed7b15909a4337c500f5e`, with 87 members. Both local draft ZIP copies match. All 19 inputs authenticated by A05 match its recorded full-file hashes; P01–P04 body hashes match the audit records. A05 is the twentieth requested closure input. No older placeholder or chat reconstruction was used.

The supplied audit-only archive is named `A05_q2_mode_selection_audit_only.zip`, SHA-256 `7b1f144b507d78f97c300bfef28a568ef34f5078c7e67c5e5d452d796b53cf59`. It is preserved under its supplied name, without replacement or renaming. Its 11 members, including the A05 source and all supplied support records, are copied byte-for-byte into the existing `cyclic_network_project/` tree. No A05 PDF was supplied or generated by this closure. The resulting full-project snapshot contains 98 members, including all 87 original project members. The required new complete archive is `cyclic_network_project_P05_audited.zip`; draft and audit-only archives remain preserved.

### Nonblocking provenance note: A05 U01

A05 records that the original P05 validation companion was unavailable to that independent auditor, so the historical checker, run counts and error maxima were not independently reproduced. U01 concerns historical computational provenance only; it does not block the mathematical or realizability verdicts or P08 clearance. This closure does not rerun, reconstruct, certify, or claim to resolve that historical validation. A05's independent checker/results and P05's historical text are retained unchanged. No numerical continuation or new literature work is performed.

### A05 closure compilation and explicit preservation checks

- **Compilation: PASS.** Existing pdfLaTeX / TeX Live 2026 and latexmk 4.88 process, with an external build directory. Final reading copy: **66 pages**, with P05 on **41–49**. Front matter pages 1–3 and every P05 page were rendered and visually inspected with no clipping or overlap.
- **Diagnostics:** the same three pre-existing underfull-hbox spacing warnings in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130 (badness 1286, 1275, 10000). **No new diagnostics, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings, or compilation errors.** All 218 labels in the 28 included sources are unique. Compilation does not verify the mathematics; A05 supplies the independent audit.
- **P05 exact-change check: PASS.** The current body equals the exact audited body after the single literal E01 sentence substitution. All remaining body bytes are identical; all other full-file changes are comment-only audit/status/version metadata. The following coprimality sentence, every theorem, displayed formula, proof, example and validation result are unchanged.
- **P01–P04 preservation: PASS.** Complete source files and mathematical bodies are byte-identical to the authenticated draft project.
- **P06–P18 preservation: PASS.** All thirteen complete source files and mathematical bodies are byte-identical; no later module was begun.
- **A01–A05 preservation: PASS.** All audit sources are unchanged. A01–A04 and their existing support/PDF records match the baseline project; A05 and all ten supplied support files match the audit-only archive byte-for-byte. No audit source, verdict, support code or result was rewritten.
- **Canonical/frozen preservation: PASS.** Model, notation, shared macros, dependency map, frozen theorem package and novelty documents remain byte-identical, with no status-reference exception needed. All numerical plans, archived material and other existing project files are preserved.
- **Registry preservation: PASS.** All 170 archival C-rows and 22 additional P01–P05 claim rows remain. Only C045–C048 and P05-D1–P05-D5 status cells change; every nonstatus cell is unchanged. No later claim is promoted. The compendium input sequence is unchanged.
- **Inventory: PASS.** Exactly five original members change: P05, manifest, registry, compendium source and regenerated compendium PDF. The other 82 original members are unchanged. The 11 immutable A05 archive members are the only additions, giving **98 members** and no removals.
- **Packaging: PASS.** `cyclic_network_project_P05_audited.zip` is the complete current `cyclic_network_project/` tree. ZIP CRC checks and every member-byte comparison pass. Build intermediates and external closure logs are excluded. Both draft ZIP copies and the supplied audit-only archive retain their original hashes and filenames; nothing under `sources/` is changed.

Current delivery: **`cyclic_network_project_P05_audited.zip`**. Final P05 disposition: **VERIFIED / AUDITED AFTER MINOR REVISION**. **P08 is cleared to begin, but remains NOT STARTED.** This task performs audit closure and packaging only.

## P08 completed draft — 2026-10-03 (historical; superseded by closure below)

**Current lifecycle: P01–P05 VERIFIED / AUDITED; P08 v1.0 DRAFT; P06–P07 and P09–P18 TODO.** This entry supersedes historical P08-not-started prose. No P08 result is VERIFIED or independently audited. The frozen MAIN THEOREM TARGET role is supported by substantive qualitative DRAFT proofs, without a priority-clearance claim.

### Current-file authentication

The authoritative baseline is `cyclic_network_project_P05_audited.zip`, SHA-256 `0fdd85b0e1671d1c11b7a909ae1e7ea3480b65f94e7bfa7d9b7f34d82d6ceb1c`, containing 98 members. Both delivered ZIP copies and the P05 audited directory agree byte-for-byte. All 21 requested current inputs were located before mathematics. Current P01–P05 body hashes and A05 E01 closure were authenticated against the closure records; the P05 full-file hash is `054a047a55ef37815485f6c225be2f6322ca8cf1c272614dd1dc4bb10ae8e1dd`. The new draft uses the manifest filename `proofs/P08_matched_bilinear_analysis.tex` inside `cyclic_network_project/`. Stale top-level folders were not used. A04/A05 U01 historical validation-provenance notes remain unchanged and are not claimed resolved. Full input/member hashes are in the separate P08 validation support.

### Completed DRAFT mathematical scope

- **MB foundation:** polynomial local uniqueness on R^n; every coordinate face invariant; sign and strict coordinate positivity preserved on the maximal interval. Synchrony is `s'=as-Ms²`, `M=k+g+h-c`. Positive synchrony exists exactly when M>0 and is `y*=a/M`. M=0 gives global exponential growth; M<0 gives finite-time blow-up from positive synchronous data at `log(1+a/(|M|s0))/a`. These are scalar examples, not classifications of all MB trajectories.
- **Full-system bounds:** `D+Y <= aY-(k-c)Y²`; k>=c gives global nonnegative existence, k>c gives dissipativity, with finite absorption into every strictly larger comparison cube. An additional sufficient condition `k>K_nq`, where `K_nq=max_m[c cos(theta_m)-(g+h)cos(q theta_m)]`, gives a sum-of-coordinates logistic bound. This condition is exactly strict stability of positive MB synchrony. Neither sufficient bound is called necessary; `(a,k,c,g,h)=(9/2,7,8,1,1)` at q=2 explicitly has k<c and a dissipative MB flow.
- **Spectrum:** MB Jacobian derived before using equilibrium, with all offset collisions added. At positive synchrony it is `y*[-kI+cP-gP^(-q)-hP^q]`, with full signed Fourier spectrum and normality. The uniform eigenvalue is -a by both the matrix spectrum and the scalar derivative. Instability, if present, is nonuniform; no bifurcation type follows.
- **q=2 selection:** always strictly concave, vertex `c/[4(g+h)]`; exact P05 generic cosine-grid cells with `chi_MB=4(g+h)/c`, all ties, labels, reachable `0,...,floor((n+1)/4)`, parity and finite-parameter endpoints. MB-specific realizability is proved anew. The exact stability inequality in selected cell j is `k>(g+h)+c u_j-2(g+h)u_j²`.
- **Fair comparison and structural distinctions:** full common existence domain from P02 plus M>0; primary open region `C_+={M>0,a+c>g}` has unique positive DM root x_+. DM `chi=4x*[h(1+x*)²-g]/[c(1+x*)]` can have either sign; MB chi is positive and independent of a. All DM curvature regimes occur on the common domain. Coordinate faces, uniform eigenvalues, and whole-class dissipativity differ. Blow-up comparisons lie outside the common positive-equilibrium domain.
- **All stable ordered pairs (thm:P08-pair-realization):** every ordered pair of reachable dominant representatives is realized strictly on a nonempty open subset of C_+ with both equilibria stable. In particular both directions of uniform/nonuniform selection and distinct nonuniform pairs (n>=7) occur. Equilibrium coordinates are used to construct positive coefficients, then scalar regularity gives openness in all five physical parameters.
- **Universal forward stability contrast (thm:P08-forward):** at q=2, every n>=5 has a nonempty open common region with DM stable/uniform and MB unstable/nonuniform. The single rational witness `(1/4,1/8,1,1,1/8)` has x*=y*=1 as independently calculated values. DM abscissa is -1/4; an actual MB label J has real part >=3/16. An algebraic-integer argument excludes all representative ties at vertex 2/9.
- **Reverse contrast on the unique DM branch (thm:P08-reverse):** existence of DM-unstable/MB-stable tuples in C_+ occurs exactly for n=3 mod 4. An analytic positive family proves nonempty openness for each such size. For other sizes MB strict stability implies DM strict stability on C_+, by an exact modal inequality and the signs of reachable cosines. At n=7, the rational witness `(20301/1100,17/20,1/2,1/100,1)` has x*=10 and y*=20301/1496, with both selecting 2; rational isolating intervals for seventh-root cosines certify opposite stability.
- **Full-domain branch qualification (prop:P08-lower):** when 4 divides n, MB strict stability implies every positive DM equilibrium is strictly stable. For every other size a separate explicitly named lower-positive-root family realizes DM unstable/uniform and MB stable. The two DM roots, original residuals and branch regularity are all checked. At n=6 this family is rational (epsilon=1/48). This does not contradict the C_+ obstruction.
- **Both unstable with different modes:** at n=8, `(16351/1100,1/2,3/2,1/100,1)` has x*=10, y*=16351/11, and selected pair (2,1), with strict positive maxima and an open neighborhood. Thus all five requested types of stability/mode combination have realizations, without claiming each at every size.

### Deferred scope and frozen package

Only P01–P05 are prerequisites. No P06/P07 or P09–P18 result is used or begun. Six-term analysis, full MB Hopf, transversality, l1 and criticality remain deferred. P08 supplies spectra and open-region inputs for later P11–P13, but no first-crossing or Hopf conclusion. The frozen package already requests this comparison and needs no amendment. Frozen novelty/literature files remain unchanged; priority is not declared closed.

### Reproducible corroboration

The separate `P08_validation_support.zip` contains the checker, all per-case data, exact residual/interval certificates, authentication, preservation and build evidence. Python 3.12.14 / NumPy 2.3.5; scaled tolerance 2e-10. All checks PASS: 271 two-model equilibrium/matrix cases; 11 exact equilibrium families including original-component checks; 280 MB cell/tie cases; 28 collision/complex-step cases; 198 maximum-inequality cases. Coverage includes n=5,6,7,8 and q=1,n-1,n/2, plus deterministic dimensions through 32, all stable ordered pairs for n=5..16, the parity contrast families, and the rational witnesses. Largest scaled direct-eigenvalue error is below 2.12e-14; original-equilibrium residual below 1.74e-16. Checks are corroboration only, not interval certification, proof of openness, mathematical verification, or independent audit.

### Compilation, preservation and delivery

Build and preservation details are finalized below after compilation. The required complete draft archive is `cyclic_network_project_P08_draft.zip`. Future A08 and P08-audited archives are not created. P01–P05, A01–A05, canonical/frozen files and all other proof bodies are protected. The P08 auditor checklist is included in the proof source.
### Final P08 build and delivery record

- **Compilation: PASS**, pdfLaTeX / TeX Live 2026 with latexmk 4.88; **77 pages**, P08 on **52–63**. The multi-file compendium was compiled with the existing project toolchain into an external build directory.
- **Diagnostics:** three unchanged underfull-hbox spacing warnings from the protected dependency map, lines 126–127, 129–130 and 130–130 (badness 1286, 1275, 10000). Zero undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings, or errors. All **261 labels in 28 included source files** are unique; P08 defines no macros.
- **Visual review: PASS.** Front matter pages 1–3 and every P08 page (52–63) were rendered and inspected. The final wording-only revision on page 56 was re-rendered and inspected. No clipping, overlap, or missing equations found. Compilation is not verification.
- **Preservation: PASS.** Exactly five existing members change: P08 source, manifest, registry, compendium source, and regenerated compendium PDF. The other **93 of 98 members** are byte-identical. All 17 other proof files, A01–A05 and all their support, canonical model/notation/macros, dependency map, frozen and novelty files, numerical plans, and archive are unchanged. No project members are added or removed; compendium input order is unchanged. All 170 archival C-rows retain every nonstatus cell; only C053–C063 and C145 status cells change, and nine DRAFT P08 rows are added. Earlier P01–P05 claim rows are unchanged.
- **Packaging:** complete 98-member `cyclic_network_project_P08_draft.zip`, with root exactly `cyclic_network_project/`, plus separate `P08_validation_support.zip`. ZIP CRCs and member bytes are checked. Build intermediates remain outside the project ZIP. No A08 audit-only or P08-audited archive is produced, and no synced source file is changed.
- **P08 v1.0 full-file SHA-256:** `d21a77de84df4c40c2995d30ab740130795adca6c72f52fef9453ad5ddfb18ac`.

## P08 audit closure — 2026-10-03 (CURRENT)

**P08 v1.1: VERIFIED / AUDITED AFTER MINOR REVISION.** P01–P05 retain their audited statuses. P06–P07 and P09–P18 remain TODO. P07 is now cleared to begin under the frozen attempt order but is not begun in this closure. This entry supersedes historical P08 DRAFT/audit-pending prose without changing its mathematical body beyond E01.

### Exact versions and immutable audit

- Original audited version: **P08 v1.0, 2026-10-03**, 39,287 bytes and 846 lines.
- Original full-file SHA-256: `d21a77de84df4c40c2995d30ab740130795adca6c72f52fef9453ad5ddfb18ac`.
- Original body SHA-256: `3c4393e8a8285f946a67634addbd71d617985f7f153f4963fdcbde90ca123a0d`.
- Corrected version: **P08 v1.1, 2026-10-03**.
- Corrected full-file SHA-256: `81d273f0bad1714d2470e9fc826f0819e9dde367a9c42633705a275b404e5454`.
- Corrected body SHA-256: `67909444bd10dde10f2784db560e7ffb4165f34b63c0a72a356a35d38ba4cc85`.
- Body hashes cover all bytes from the first line-anchored section command through EOF. The full-file digest is recorded outside the hashed file to avoid self-reference.
- Immutable audit: [audits/A08_matched_bilinear_analysis.tex](audits/A08_matched_bilinear_analysis.tex), SHA-256 `87cd4a03061648eb4cf1c65d1afa47c7132c1f7eed10d546784ee166c8e5c935`.
- Original A08 verdicts: **MB FOUNDATION VERIFIED; MB SPECTRAL VERIFIED; SAME-TUPLE COMPARISON MINOR REVISION; PARITY/OBSTRUCTION VERIFIED; OVERALL MINOR REVISION**. The original audit and these verdicts are preserved unchanged.
- Sole required correction: **E01**, erroneous n=8 selected representative in original lines 534–535.
- Closure disposition: **VERIFIED / AUDITED AFTER MINOR REVISION**.

### Exact E01 correction and scope

Original text:

> For n=5,6,7,8 this witness selects MB representative 1; other sizes follow the exact finite-grid rule and need not retain that label.

Exact replacement (retaining LaTeX math delimiters in the source):

> For n=5,6,7 this witness selects MB representative 1; for n=8
> it selects representative 2. Other sizes follow the exact finite-grid
> rule and need not retain either label.

At n=8, representative 2 corresponds to Fourier labels {2,6}. This explanatory record adds no further proof-body text. The witness tuple, both equilibrium amplitudes, DM abscissa -1/4, MB bound sa(J_MB)>=3/16, all-n contrast theorem, all-pair theorem, reverse-stability parity theorem, every obstruction, and all surrounding proofs are unchanged. Every other body byte, including historical DRAFT/audit-pending wording, is preserved; the current header and this closure govern lifecycle status.

### Authentication and validation provenance

The complete authenticated draft is `cyclic_network_project_P08_draft.zip`, SHA-256 `3cac0e6676575e1c652454a9e28418c04ac5a553d4550c6f8d27f2d873e71e44`, with 98 members. Both existing copies match. All 21 inputs authenticated by A08 match its hashes; A08 is the twenty-second required closure input. The stale top-level P08 placeholder is excluded.

The immutable `cyclic_network_project_A08_audit_only.zip`, SHA-256 `17eab7f3b684d5b4fd061d6cafb1cd4fad64a612bb50c0188e25456a6d4eaa27`, contributes 20 new members, including A08 source/PDF and all supplied support records, copied byte-for-byte. The full audited snapshot therefore contains **118 members**, retaining all 98 draft members. Existing A01–A05 and new A08 sources are included unchanged; no A06/A07 source exists and none is fabricated.

A08 located and authenticated the original `P08_validation_support.zip`, independently derived its loop counts, and exactly reproduced all reported summaries and result data. The preserved evidence is in `audits/A08_support/prior_validation/`, including `reproduction_comparison.json`. No A08 validation-provenance issue remains. The closure does not rerun the validation suite. This provenance is distinct from the mathematical audit. A04/A05 historical notes remain unchanged.

### Preservation, compilation and delivery

The closure performs only E01, comment metadata, lifecycle bookkeeping, compilation and full-project packaging. Detailed final build and byte-preservation checks follow below. Frozen theorem, novelty, canonical and notation files require no bookkeeping exception and remain unchanged. P07 and every subsequent module are not begun. Draft and audit-only archives retain their names and bytes. The complete delivery is `cyclic_network_project_P08_audited.zip` with sole project root `cyclic_network_project/`.

### Final A08 closure checks and delivery record

- **Compilation: PASS.** Existing latexmk/pdfLaTeX process; 77 pages, P08 on pages 52–63. All 261 labels across 28 included sources are unique, and compendium input order is unchanged.
- **Diagnostics:** exactly three pre-existing underfull-hbox spacing diagnostics in the unchanged dependency map, lines 126–127, 129–130, 130–130 (badness 1286, 1275, 10000), matching the authenticated draft build. Zero new diagnostics, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings, or errors.
- **Visual review: PASS.** Front matter pages 1–3 and all P08 pages 52–63 were rendered and inspected. E01 is legible on page 59; no clipping, overlap, or missing equations was observed.
- **Preservation: PASS.** P08 differs only in comment metadata and the exact E01 replacement. Every other body byte and every theorem/proof environment is unchanged. All 17 other proof files, all existing A01–A05 audit/support files, and all 20 supplied A08 members are byte-identical. Canonical model, notation, shared macros, dependency map, frozen scope, novelty documents, numerical plans and existing project support are unchanged.
- **Registry: PASS.** All 170 archival C-rows retain every nonstatus cell. Only C053–C063 and C145 status cells change; C145's blanket assertion stays rejected. P08-D1–D9 change only in their status cells. Earlier P01–P05 claims and C064/C065 are unchanged.
- **Full snapshot:** 118 members under the sole root `cyclic_network_project/`: all 98 draft members plus the 20 immutable A08 members. Exactly five original members change: P08 source, manifest, registry, compendium source, and regenerated compendium PDF. The other 93 original members are byte-identical. Existing audits A01–A05 and A08 are included; absent A06/A07 audits are not fabricated.
- **Delivery:** `cyclic_network_project_P08_audited.zip`. Final ZIP CRC and per-member byte checks are recorded in the external closure evidence. Both original draft copies, the audit-only archive, and original P08 validation archive remain unchanged. No build intermediates enter the project snapshot.
- **Validation provenance:** A08's exact reproduction is recorded from its immutable evidence; the validation suite was not rerun for closure. Compilation and preservation checks do not replace the mathematical audit.
- **Scope closed:** P08 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION. P07 is cleared but not begun; no subsequent module, numerical continuation, or literature work was started.

## P07 completed draft — 2026-10-03 (historical; superseded by closure below)

**P07 v1.0: DRAFT, independent A07 audit pending.** P01–P05 and P08 retain their VERIFIED / AUDITED statuses and closure qualifications. P06 and P09–P18 remain TODO. This current entry supersedes historical P07-not-started wording, including the P08 closure's scheduling record. No later proof is begun.

### Authoritative inputs and dependency boundary

The baseline is `cyclic_network_project_P08_audited.zip`, SHA-256 `dd1551f5a5b151c928fda77b030d1e41fcb81696e61ed42251e78695cca97dfe`, containing 118 members under `cyclic_network_project/`. Its CRC, every member against the audited directory, all 23 requested current files, and the P05/P08 audit closures were checked before mathematics. Full current-input and archive-member hashes are in the separate P07 validation support. Older top-level projects were excluded.

The current filename remains `proofs/P07_five_node_specialization.tex`. The direct dependency remains P05 -> P07; P03/P04 and P01/P02 are inherited. P08 is consulted for version and scope context only; no MB result is imported and no P08 -> P07 theorem edge is added. The frozen theorem package, novelty decisions, canonical model, notation, macros, and dependency map need no amendment and are unchanged. Historical audit-provenance qualifications in A04/A05 remain unchanged.

### Completed DRAFT theorem package

- `lem:P07-trig`, `thm:P07-spectrum`: fifth-root derivation of phi, both exact cosine values and a consistent positive sigma; all five signed Fourier eigenvalues and conjugate labels.
- `thm:P07-ordering`: three factored gaps and all seven ordering rows, including distinct dominant and subdominant ties at t=-phi^(-2), t=1, and t=-phi^2. Ordering cancels d.
- `cor:P07-selection`: pair {2,3} is never maximal by direct three-class algebra. The dominant switch is H-G=C/phi^2; beta_0=phi^2/4 and alpha_0=4/phi^2=6-2sqrt(5). The current P05 defines chi for all signs; H<=G is uniform-selected. The canonical switch is subject to the P02 equilibrium equation.
- `prop:P07-frequency`: omega_1=sigma(S-phi C), omega_2=-sigma(C+phi S)<0. Frequency degeneracy of pair {1,4} occurs exactly at S=phi C and is described only spectrally.
- `prop:P07-intersection`: simultaneous switch and frequency degeneracy give G/C=1/phi, H/C=1, with a positive canonical witness and independent codimension-two spectral constraints on a regular positive branch. The common eigenvalue at labels {0,1,4} is semisimple, triple and strictly negative.
- `prop:P07-coincidences`: exhaustive numerical coincidence classification; no cross-pair equality is possible, labels 2 and 3 always have simple nonreal values, and pair-1 nonreal values are simple. The only repetitions are the real pair-1 double value or its triple intersection with label 0.
- `cor:P07-stability`, `prop:P07-ledger`: exact piecewise Hurwitz test. The entire dominant tie, not only its frequency intersection, is strictly stable at positive synchrony. The ledger is fixed-state eligibility, not a parameter-path first-instability theorem.
- `eq:P07-realization`: every positive effective coefficient triple is realized at x*=1 by (a,k,c,g,h)=(H+2G,C,2C,4G,H). Thus every ordering row is canonically nonempty without using P08.

P07 supplies exact spectral inputs for later five-node work in P11–P14; no Hopf existence, first crossing, transversality, crossing derivative, Lyapunov coefficient, normal form, or periodic/rotating-wave result is attempted. Golden-ratio constants are fifth-root geometry only and carry no physiological, medical, biological-optimum, or TCM-validation conclusion. The independent-auditor priority checklist is included in P07.

### Reproducible corroboration

The new P07 checker uses exact rational arithmetic in Q(sqrt(5),sigma,i), with sigma^2=(5-sqrt(5))/8, and separate NumPy direct matrices. **161 exact checks and 108 canonical matrix cases PASS**, covering 18 settings, every ordering row, both sides of the dominant switch, both subdominant ties, the frequency locus and nearby points. Each setting uses x*=1/4,1,3 and C=1,7/3. Full original-vector-field residuals, independently differentiated Jacobians, complex-step derivative checks, labelled Fourier residuals, and multiplicity-preserving direct eigendecompositions are recorded. The largest scaled eigendecomposition discrepancy is below 1.46e-15 at tolerance 2e-10. Python 3.12.14; NumPy 2.3.5. These checks supplement the written proofs and confer neither VERIFIED nor AUDITED status.

The separate `P07_validation_support.zip` retains the checker, complete exact and numerical results, baseline authentication, build evidence and preservation/delivery checks. The required full snapshot is `cyclic_network_project_P07_draft.zip`; neither future A07 audit-only nor P07-audited archive is created.

### Final P07 build and delivery record

- **Compilation: PASS**, using the existing multi-file latexmk/pdfLaTeX toolchain, **84 pages**; P07 occupies **51–58**. All **295 labels in 28 included source files** are unique; the compendium input sequence is unchanged.
- **Diagnostics:** exactly three pre-existing underfull-hbox spacing diagnostics in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130, 130–130 (badness 1286, 1275, 10000). Zero new warnings, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings, or compilation errors. Compilation is not mathematical verification.
- **Visual review: PASS.** Front matter pages 1–3 and every P07 page 51–58 were rendered and inspected. No clipping, overlap or missing equations was observed.
- **Preservation: PASS.** Exactly five of the 118 baseline members change: P07 source, manifest, claim registry, compendium source and regenerated compendium PDF. The other 113 members are byte-identical. All 17 other proof files, existing A01–A05/A08 audit sources and support, canonical model, notation, macros, dependency map, frozen theorem/novelty documents, numerical plans and archived material are unchanged. No source under `sources/` is changed.
- **Registry: PASS.** All 170 archival C-rows retain their nonstatus cells. Only C051, C052 and C155 status cells change, and six DRAFT P07 records are added. All earlier P01–P05/P08 claim rows remain byte-identical; C155's physiological assertion remains rejected.
- **Full snapshot:** `cyclic_network_project_P07_draft.zip`, exactly 118 files under the sole root `cyclic_network_project/`, with no added or removed project member. ZIP CRC and every member's bytes are checked. No build intermediates or validation-support files enter the project ZIP. The separate companion is `P07_validation_support.zip`.
- **P07 v1.0 full-file SHA-256:** `fc10d257e8126b79a56cc7dd4c55b14b0266e250cbe40dbecb6c6a18658d09de`.
- **P07 v1.0 mathematical-body SHA-256:** `66a5b8f078cb0fc30f4d7c72c22a26b965fd8ded491f53450d604fe7a21ccdea` (bytes from first line-anchored section command through EOF).
- **Status:** P07 DRAFT; independent A07 audit remains required. No A07 audit-only or P07-audited archive is created. No P08 dependency or P09–P18 work is introduced.

## P07 audit closure — 2026-10-03 (CURRENT)

**P07 v1.1: VERIFIED / AUDITED.** A07 requires no mathematical or wording correction. This is a metadata-only administrative closure of exact audited P07 v1.0; the mathematical body remains byte-for-byte unchanged. P01–P05 and P08 retain their existing audited statuses. P06 and P09–P18 remain TODO. **P09 is cleared to begin, but is not begun in this closure.** This entry supersedes historical P07 DRAFT/audit-pending prose.

### Exact versions, hashes and immutable audit

- Audited version: **P07 v1.0, 2026-10-03**, 24,180 bytes and 555 lines.
- Original audited full-file SHA-256: `fc10d257e8126b79a56cc7dd4c55b14b0266e250cbe40dbecb6c6a18658d09de`.
- Audited mathematical-body SHA-256: `66a5b8f078cb0fc30f4d7c72c22a26b965fd8ded491f53450d604fe7a21ccdea`.
- Current version: **P07 v1.1, 2026-10-03; metadata-only closure**.
- Current full-file SHA-256: `1258641da2b1b729523da6262cf75345f5ef1eabf7a9f693a8b13dd34deec393`.
- Current mathematical-body SHA-256: `66a5b8f078cb0fc30f4d7c72c22a26b965fd8ded491f53450d604fe7a21ccdea` (**unchanged**).
- Body scope: exact bytes from the first line-anchored section command through EOF, including comments, whitespace and the final newline. Only header comments before that body change. Current full-file hashes are recorded outside the hashed file to avoid self-reference.
- Immutable audit: [audits/A07_five_node_specialization.tex](audits/A07_five_node_specialization.tex), SHA-256 `b3923d6520cc249c508b80dd06a2b515f054e1510e255224a864e986cd38ce4b`. Its exact-version references, verdicts, mathematical text and every supplied support file remain unchanged.

A07 layer verdicts: **FOURIER / TRIGONOMETRY VERIFIED; ORDERING / SELECTION VERIFIED; FREQUENCY / COINCIDENCE VERIFIED; STABILITY / CRITICAL-MODE VERIFIED; SCOPE / DEPENDENCY VERIFIED; OVERALL VERIFIED.** Required corrections: **NONE**.

All formulas, theorem statements, proofs, examples, labels, comments and historical DRAFT/audit-pending sentences within P07's mathematical body are retained. The current header and this closure govern lifecycle status. The verified spectrum, seven-row ordering, selection threshold, pair-2 exclusion, frequency locus, positive codimension-two spectral intersection, semisimple triple eigenvalue, full coincidence classification, strict stability of the entire dominant tie, critical-mode ledger, canonical realization, P11-input ledger and geometry-only interpretation are unchanged.

### Authentication, dependencies and validation provenance

The complete draft is `cyclic_network_project_P07_draft.zip`, SHA-256 `2a49a916659df343995adf5b6e75975f1d05b97f2d0bf24f43db631d0472106c`, with 118 members. Both existing draft ZIP copies match. Every member matches the current draft directory, and all 23 A07 input records (including full/body hashes where recorded) authenticate against the draft. The supplied A07 source is the twenty-fourth closure input.

The immutable `cyclic_network_project_A07_audit_only.zip`, SHA-256 `70995326e03f8a0d02f375680774160081a83ddc0dc7ed130c73ec09f5baeacb`, contributes 25 new members copied byte-for-byte: A07 source/PDF and its complete support. The audited snapshot retains all 118 draft files, for 143 total files. Existing audits A01–A05, A07 and A08 are included; no A06 audit exists in these inputs and none is fabricated.

The direct theorem dependency remains **P05 -> P07**. P03/P04 and P01/P02 are inherited prerequisites. P08-before-P07 is an attempt-order relation only; no P08 theorem dependency is introduced. The dependency map, canonical/notation/macro files, frozen theorem package and novelty documents need no lifecycle exception and remain byte-identical.

A07 authenticated the original `P07_validation_support.zip` (SHA-256 `cabf306b6a95db0951f320ba472ee401f050ec014a7ee12b6a558f9f41b2abc5`), reproduced its **161 exact checks and 108 numerical cases**, and obtained byte-identical summary, exact-results and numerical-results files. The closure reads and preserves that evidence in `audits/A07_support/prior_validation/`; it also checks the saved original/reproduced file bytes without rerunning either historical suite. Validation is corroboration, not proof; A07's independent reconstruction supplies mathematical verification. Earlier A04/A05 provenance qualifications remain unchanged.

### Closure scope and complete delivery

Only P07 header comments, necessary manifest/registry/compendium bookkeeping and the regenerated compendium PDF change. All P07 mathematical-body bytes and every other proof/audit source are protected. All 170 archival C-rows retain their nonstatus cells; only C051/C052/C155 status cells and P07-D1–D6 status cells change. C155's physiological assertion remains rejected. No P09 or later result is promoted.

The full snapshot is **`cyclic_network_project_P07_audited.zip`**, with sole root `cyclic_network_project/`. Draft and audit-only ZIPs are preserved. This task contains no P06/P09–P18 proof development, numerical continuation or new literature work. Final build and preservation results are recorded below.

### Final A07 closure checks and delivery record

- **Compilation: PASS.** Existing latexmk/pdfLaTeX build; **84 pages**, P07 on **51–58**. All 295 labels across 28 included source files are unique; compendium input order is unchanged.
- **Diagnostics:** exactly three pre-existing underfull-hbox spacing diagnostics in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130, 130–130 (badness 1286, 1275, 10000). Zero new warnings, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings, or errors. A transient front-matter spacing warning was removed before the final build; no proof source was altered for layout.
- **Visual review: PASS.** Current front matter pages 1–3 were rendered and inspected. All eight freshly rendered P07 pages 51–58 are byte-identical to the draft's previously inspected renders. Extracted text on pages 4–84 is unchanged. Historical DRAFT wording within P07 is intentionally preserved; current front matter and header govern its VERIFIED / AUDITED status.
- **P07 preservation: PASS.** Every byte from the first line-anchored section command through EOF is unchanged. Mathematical-body SHA-256 remains `66a5b8f078cb0fc30f4d7c72c22a26b965fd8ded491f53450d604fe7a21ccdea`. Full-file hash changes only because header comments changed.
- **Other proofs and audits: PASS.** P01–P05, P08, P06 and P09–P18 complete source files and mathematical bodies are byte-identical. Existing A01–A05/A08 audit sources, PDFs and support are unchanged. A07 source/PDF and all 23 support files match its immutable audit-only archive byte-for-byte. No A06 audit was supplied or fabricated.
- **Canonical and frozen preservation: PASS.** Model, notation, shared macros, dependency map, frozen theorem package, novelty documents, numerical planning and all remaining existing project files are byte-identical; no lifecycle exception was necessary. No synced `sources/` file is changed.
- **Registry: PASS.** All 170 archival C-rows retain every nonstatus cell. Only C051/C052/C155 status cells and P07-D1–D6 status cells change; every earlier claim row is unchanged. C155's physiological assertion remains rejected.
- **Complete snapshot:** 143 files under sole root `cyclic_network_project/`: all 118 draft files plus all 25 immutable A07 files. Exactly five draft members change: P07 source, manifest, registry, compendium source, and regenerated compendium PDF. The other 113 draft members are unchanged. No draft member is removed and no build intermediate enters the snapshot.
- **Delivery:** `cyclic_network_project_P07_audited.zip`. ZIP CRC and every member's bytes pass. Both draft ZIP copies, the audit-only ZIP, and the original P07 validation companion retain their names and bytes. Detailed closure evidence is external to the project snapshot.
- **Validation provenance:** A07's authenticated reproduction of 161 exact checks and 108 numerical cases, with byte-identical results, is recorded from its immutable evidence. No historical suite is rerun for closure. Validation and compilation are not proof; A07 provides independent mathematical verification.
- **Final status:** P07 v1.1 **VERIFIED / AUDITED**, metadata-only closure of exact P07 v1.0, no corrections required. Direct dependency remains **P05 -> P07**. **P09 is cleared but not begun**; no later module, continuation or literature work was started.

## P09 draft — 2026-10-03 (CURRENT)

**P09 v1.0 is DRAFT; independent A09 audit pending.** This supersedes historical P09 TODO / not-started prose. P01–P05, P07 and P08 retain their audited status. P06 and P10–P18 remain TODO. No P10 work is begun.

### Current-file selection and dependency discipline

The authenticated baseline is `cyclic_network_project_P07_audited.zip`, SHA-256 `1dcbdac11cab4da00cf88da2d03d066417fbdfe59091acb08d8594d360a7b87e`, containing 143 files under `cyclic_network_project/`. Every archive member matches `output/p07_audited/cyclic_network_project` byte-for-byte. Its CURRENT A07 closure includes completed A08; the P08-audited snapshot is earlier and leaves P07 TODO. All ten required control files and every P01–P05/P07/P08 and A01–A05/A07/A08 source are present and authenticated. The P09 filename is preserved. A02's old header about source absence is superseded by the manifest's authenticated source-restoration record; its TeX is present.

The theorem edges remain **P02, P03, P04 -> P09**, with P01's local smoothness inherited. There is no P05, P07, P08 or later theorem dependency. B02 is resolved for P09 only by fixing a,k,c,h,n,q and varying g, equivalently mu=a+c-g. NB07 permits only the recorded algebraic/spectral codimension and one-parameter cubic case; no two-parameter unfolding is performed. No contradiction with frozen scope was found, and no amendment is needed.

### Draft theorem package and exact checks

- `lem:P09-gap`: Jc=c(P-I), one algebraically simple zero with kernel span{1}, all transverse real parts at most -delta_n, delta_n=c[1-cos(2pi/n)]>0; no gcd condition.
- `thm:P09-reduction`: on the real mean-zero subspace, the transverse derivative is invertible. The implicit-function solution y=psi(r,mu) equals zero by exact synchrony and uniqueness. Every local equilibrium is synchronous, including b=0.
- `prop:P09-coefficients`: full-vector mixed coefficient 1 in mu and -1 in g, quadratic tensor contraction 2b, Taylor coefficient b; origin persists.
- `thm:P09-transcritical`: b!=0 gives exactly the origin and the unique local branch, slopes -1/b in mu and 1/b in g, distinct tangents, and full stability exchange. The exact center coordinate u=Ar^2-br and a positive time factor reduce the center field to u'=u(mu-u). The proof does not claim an exact full-system decoupling.
- `eq:P09-uniform-nonzero`: lambda0=-mu(b-2Ar)/[(1+r)(b-Ar)], whose extra factor is positive locally. All transverse modes remain strictly below -delta_n/2 by P04 continuity over finitely many labels. No P05 selection is used.
- `cor:P09-physical`: for b<0 the local positive branch lies on g<gc and is exponentially stable; for b>0 it lies on g>gc and is unstable. The origin has the opposite stability. A positive uniform eigenvector and exact synchronous escape establish origin instability relative to the orthant for mu>0.
- `prop:P09-generic-critical`: at mu=0, b!=0, exact synchronous escape makes the origin unstable in U; the b<0 proof uses negative states and makes no blanket relative-orthant stability claim.
- `prop:P09-degenerate`: b=0 gives only the origin for mu<=0 and exactly the two nonzero roots +/-sqrt(mu/A) for mu>0 locally. Both nonzero roots are full-system exponentially stable; only the positive root is physical. At mu=0 the full origin is locally asymptotically stable but not exponentially stable: the center-manifold hypotheses are checked and a direct strict Lyapunov estimate independently proves the conclusion. Synchronous decay has magnitude asymptotic to (2At)^(-1/2).
- `prop:P09-codimension`: independent constraints a-k-h=0 and g-a-c=0 give codimension two in the positive physical parameter space for each fixed n,q; the zero eigenvalue is still simple. P02's repeated-root locus meets gc there at root zero. No named codimension-two bifurcation or pitchfork label is asserted.

The 17 requested exact checks are addressed analytically in these results; the validation companion maps each check to proof evidence. P09's role remains supporting local steady-state bifurcation theory. No positive-fold saddle-node, true bistability, basin, Hopf, transversality, Lyapunov coefficient, rotating wave, large-n result, DM–MB comparison, or new literature work is included. P10 owns the subsequent saddle-node and stable-coexistence theorem, with its own hypotheses and audit.

### Build, validation and delivery

Final measured build, corroboration and preservation results are recorded below after execution. Compilation and numerical checks do not give VERIFIED or AUDITED status. The full snapshot is named exactly `cyclic_network_project_P09_draft.zip`. The external validation companion is `P09_validation_support.zip`. No future A09-audit-only or P09-audited archive is created.

### Final P09 draft delivery record

- **Compilation: PASS**, existing multi-file latexmk/pdfLaTeX toolchain; **90 pages**, P09 on **71–77**. All **326 labels in 28 included source files** are unique; the compendium input order is unchanged.
- **Diagnostics:** exactly three pre-existing underfull-hbox spacing diagnostics in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130 (badness 1286, 1275, 10000). Zero new warnings, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings or compilation errors. Compilation is not mathematical verification.
- **Visual review: PASS.** Final front matter pages 1–3 and all P09 pages 71–77 rendered and inspected; no clipping, overlap or missing equations. Metadata font sizing and a deliberate contents-page break keep front matter compact. Baseline PDF text on pages 4–70 is unchanged. The final comment-only rebuild has identical decoded content streams on all pages to the visually reviewed PDF.
- **Computational corroboration: PASS.** Python 3.12.14, NumPy 2.3.5; **1260 exact-arithmetic checks**, **2700 original-field/direct-matrix cases**, and **12 finite-difference slope checks**, each testing both mu and physical g orientation. Seven dimensions n=5,6,7,8,9,10,12, all admissible q, 50 network pairs (20 noncoprime), six fixed positive tuples, both generic signs and b=0, both parameter sides. Maximum original-field equilibrium residual 3.673e-19; maximum scaled direct-spectrum discrepancy 4.694e-15; maximum scaled complex-step Jacobian discrepancy 2.918e-16; maximum slope error 2.804e-09. These are corroboration, not interval certification or independent audit.
- **Analytical review:** all 17 requested exact checks have proof anchors in the separate companion; additional anchors cover the exact orbital center reduction and the degenerate full Lyapunov proof. The independent-auditor priority checklist is in P09 itself.
- **Preservation: PASS.** Exactly five baseline members change: P09 source, manifest, claim registry, compendium source and regenerated compendium PDF. The other **138 of 143** members remain byte-identical. All 17 other proof files, every existing audit source/PDF/support file, the model, notation, macros, dependency map, frozen scope/novelty documents, numerical plans and archived material are unchanged. No synced `sources/` file is edited.
- **Registry: PASS.** Every nonstatus cell in all 170 archival C-rows is unchanged. Only C036, C067, C068 and C069 status cells change; seven P09 DRAFT records are added. C069's proposed two-parameter unfolding remains explicitly excluded. All previous audited claim rows are unchanged.
- **P09 v1.0 full-file SHA-256:** `b2366edf1ff71199b7f1d02a58cf828148d9a697dfafc9e07e70a523e4f26680`.
- **Complete snapshot:** `cyclic_network_project_P09_draft.zip`, exactly 143 files under the sole root `cyclic_network_project/`; no project member is added or removed. ZIP CRC and every member's bytes are checked. No build intermediates or validation files enter the project ZIP. The separate companion is `P09_validation_support.zip`.
- **Status:** P09 is **DRAFT**, awaiting independent A09 audit. P10 is not begun. No future A09-audit-only or P09-audited archive is created. No literature work or frozen-scope change occurs.

## P09 audit closure — 2026-10-03 (CURRENT)

**P09 v1.1: VERIFIED / AUDITED.** A09 requires no mathematical or wording correction. This is an administrative metadata-only closure of exact audited P09 v1.0, not a mathematical revision. Every mathematical-body byte is preserved. This entry and the current header supersede historical DRAFT/audit-pending wording, including the unchanged body status sentence. P01–P05, P07 and P08 retain their audited statuses. P06 and P10–P18 remain TODO. **P10 is cleared to begin but is not begun in this closure.**

### Exact versions, hashes and immutable audit

- Audited source: `proofs/P09_transcritical_bifurcation.tex`, **P09 v1.0, 2026-10-03**, 24,155 bytes, 539 lines.
- Original audited full-file SHA-256: `b2366edf1ff71199b7f1d02a58cf828148d9a697dfafc9e07e70a523e4f26680`.
- Original audited mathematical-body SHA-256: `a0830944d46d26de35faf09c5f0e4d9f42d6f10620ca22373f6bcf7031705393`.
- Current version: **P09 v1.1, 2026-10-03; metadata-only closure**.
- Current full-file SHA-256: `5d357a5be97dfbad62a0107ca2e010ff97e0c11a719ee850df69411275f11ff8`.
- Current mathematical-body SHA-256: `a0830944d46d26de35faf09c5f0e4d9f42d6f10620ca22373f6bcf7031705393` (**unchanged**).
- Body scope: first line-anchored section command through EOF, preserving all formulas, wording, labels, comments, whitespace and final newline. The original body starts on line 17. A full-file hash is recorded outside the hashed file to avoid self-reference.
- Immutable audit: `audits/A09_transcritical_bifurcation.tex`, SHA-256 `1234e02d7cf620511bfd7b9306dbb72ac68929ef01e8c3ba70bd3615bcd2b943`; exact-version references, verdicts, line review, hashes, support references and closure handoff remain unchanged.

| A09 layer | Verdict |
|---|---|
| CRITICAL SPECTRUM / REDUCTION | VERIFIED |
| GENERIC TRANSCRITICAL | VERIFIED |
| STABILITY / PHYSICAL-BRANCH | VERIFIED |
| GENERIC CRITICAL-DYNAMICS | VERIFIED |
| DEGENERATE CRITICAL-STABILITY | VERIFIED |
| CODIMENSION / SCOPE | VERIFIED |
| OVERALL | VERIFIED |

**Required corrections: NONE.** No AFTER MINOR REVISION qualifier applies to P09. All thirteen results listed in the closure request are preserved, including the transverse IFT, exact center orbital normal form, all-mode stability and physical orientation, full degenerate critical Lyapunov proof, nonexponential decay, and algebraic/spectral codimension with a still-simple center zero. All original exclusions are unchanged.

### Current-file authentication and dependencies

Both copies of `cyclic_network_project_P09_draft.zip` have SHA-256 `61df24eb644771cbb84027447c4a21ba1c1d0e1d44dc8c35cf34a0a0c755c8de`. All 143 members matched the open current project before closure, including the exact audited P09 full/body hashes. The 26 A09 input inventory entries authenticate against those current files. The ten required control files and P01–P05/P07/P08 with their audits are present. A02's restored audit source is present; its historical absence note remains superseded.

The immutable `cyclic_network_project_A09_audit_only.zip`, SHA-256 `4518b61aec90e42106865a01ef99d9cda1b9b660a726fc5112becc2f8425de55`, contributes **33 new members**: A09 source/PDF and 31 support files. Every member is copied byte-for-byte. The complete snapshot therefore has **176 files**. All existing audit sources through A09 are included; no A06 audit exists in the inputs and none is fabricated.

The mathematical dependency remains **P02, P03, P04 -> P09**, with **P01 inherited**. No P05, P07, P08, P10 or later theorem dependency is introduced. The dependency map and frozen scope/novelty documents need no lifecycle exception and remain byte-identical. No P10–P18, P06, continuation or literature work is performed.

### Validation provenance

A09 independently reconstructs and verifies the mathematics; it is the independent verification, not the build or numerical output. A09 also authenticated `P09_validation_support.zip` (SHA-256 `2752687d50610d4f6caea5803fa9436355aea45dbeb499ca6c4ed4093d6b362d`) and preserved its original checker (SHA-256 `b42af82b97c187b3a61238b7cc2aba9d35e44d210a38ec88421b10d5be2fcf93`). Its historical rerun reproduced all four result/summary files byte-for-byte: **1,260 exact checks, 2,700 matrix cases, 12 slope checks**. Closure authenticates these saved original/rerun bytes and checker against the companion ZIP; it does not rerun the checker.

A09's own corroboration additionally records 310 exact rational checks, 2,370 equilibrium/matrix cases, 316 slope cases, 474 transverse Newton searches and 1,580 direct Lyapunov/remainder cases. These remain finite computational corroboration, not proof or interval certificates. All immutable provenance and limitations are retained in `audits/A09_support/`; prior A04/A05 qualifications are unchanged.

### Closure scope and complete delivery

Only P09 header comments, necessary manifest/registry/compendium bookkeeping and the regenerated compendium PDF change. All P09 mathematical bytes and all other proof/audit sources are protected. The 170 archival C-rows preserve every nonstatus cell; only C036/C067/C068/C069 status cells and P09-D1–D7 status cells change. C069's two-parameter unfolding remains explicitly excluded/unproved.

The new full snapshot is **`cyclic_network_project_P09_audited.zip`**, with sole root `cyclic_network_project/`. Both draft ZIP copies, the audit-only ZIP and the original validation companion remain unchanged. Final compilation and explicit preservation results follow below.

### Final A09 closure checks and delivery record

- **Compilation: PASS.** Existing multi-file latexmk/pdfLaTeX build; **90 pages**, P09 on **71–77**. All **326 labels across 28 included source files** are unique; the compendium input order is unchanged.
- **Diagnostics:** exactly three pre-existing underfull-hbox spacing diagnostics in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130 (badness 1286, 1275, 10000). Zero new warnings, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings or errors. One transient front-matter overfull box was removed by a metadata-only wording adjustment before final compilation; no proof source body was altered.
- **Editor check:** the same open P09 file was edited in place and checked with the built-in compiler. Its standalone preview reports an undefined section command because P09 is a project fragment without a document preamble and shared inputs. The fragment is preserved exactly; the full compendium is the successful canonical build. No replacement document or new tab is opened; the original editor remains open.
- **Visual review: PASS.** Final front matter pages 1–3 rendered and inspected. All seven freshly rendered P09 pages 71–77 are byte-identical to the previously inspected draft renders. Extracted text on pages 4–90 is unchanged. Historical DRAFT/audit-pending wording in the P09 mathematical body is intentionally preserved; current header and front matter govern VERIFIED / AUDITED status.
- **P09 body preservation: PASS.** Every byte from the first line-anchored section command through EOF remains identical to exact A09-audited v1.0. Mathematical-body SHA-256 remains `a0830944d46d26de35faf09c5f0e4d9f42d6f10620ca22373f6bcf7031705393`. The current full-file hash changes solely because header comments changed.
- **All other proofs and audits: PASS.** Complete P01–P05, P07, P08, P06 and P10–P18 source files, and hence their mathematical bodies/placeholders, remain byte-identical. All existing A01–A05/A07/A08 audit sources, PDFs and support remain unchanged. A09 source/PDF and all 31 support files match the immutable audit-only archive byte-for-byte. No A06 audit exists in the inputs and none is fabricated.
- **Canonical and frozen preservation: PASS.** Model, notation, shared macros, dependency map, frozen theorem package, novelty files, numerical plans and all other existing project members are unchanged. No lifecycle exception in frozen files was needed; no synced `sources/` file was changed.
- **Registry: PASS.** All 170 archival C-rows retain every nonstatus cell. Only C036/C067/C068/C069 and P09-D1–D7 status cells change. Every other existing claim row is byte-identical. C069's optional two-parameter unfolding remains excluded/unproved.
- **Complete snapshot:** **176 files** under sole root `cyclic_network_project/`: all 143 draft members plus all 33 immutable A09 members. Exactly five draft members change: P09 header, manifest, registry, compendium source and regenerated compendium PDF. The other 138 draft members are unchanged. No draft member is removed; no build intermediate enters the full snapshot. Two macOS Finder `.DS_Store` housekeeping files are excluded from the ZIP and left untouched on disk.
- **Delivery:** `cyclic_network_project_P09_audited.zip`. ZIP CRC and all member bytes pass. Both copies of `cyclic_network_project_P09_draft.zip`, `cyclic_network_project_A09_audit_only.zip` and `P09_validation_support.zip` retain their original names and hashes. Detailed closure evidence is kept outside the project snapshot.
- **Validation provenance: PASS.** The preserved original checker and four pairs of original/reproduced outputs authenticate against the developer companion and A09's saved hashes. A09's byte-identical reproduction of 1,260 exact checks, 2,700 matrix cases and 12 slope checks is recorded. Neither historical nor independent numerical checker was rerun for this closure. A09's mathematical reconstruction supplies independent verification; computations and compilation remain corroboration.
- **Final status:** P09 v1.1 **VERIFIED / AUDITED**, metadata-only closure of exact P09 v1.0; **no corrections**. Dependency remains **P02/P03/P04 -> P09, P01 inherited**, without P05/P07/P08 or later theorem dependencies. **P10 is cleared but not begun.** No subsequent proof, continuation, unfolding or literature work was started.

## P10 positive saddle-node and stable coexistence — 2026-10-03 (CURRENT)

**P10 v1.0 is DRAFT; independent A10 audit pending.** P01–P05, P07, P08 and P09 retain their exact audited versions. P06 and P11–P18 remain TODO and unchanged. This entry supersedes earlier P10-TODO/cleared-not-begun lifecycle wording only. Compilation and finite computational checks do not promote mathematical status.

The current baseline is `cyclic_network_project_P09_audited.zip`, SHA-256 `db6344c5ed7c96f244f99eefa589ae8631c3aaf15278577e607e246026b22bf2`. Its 176 files match the P09 working project byte-for-byte. All ten control files and all required P01–P05/P07/P08/P09 and A01–A05/A07/A08/A09 sources are present and authenticated. A02's source-restoration closure governs its historical missing-source header. The new complete snapshot retains the sole root `cyclic_network_project/` and all baseline members.

The direct dependencies are **P02, P03, P04, P09 -> P10**, with **P01 inherited**. P05/P07/P08 are authenticated but are not theorem inputs. No dependency-map change is made. The new P10 remains within frozen supporting role S4; no scope amendment or novelty change is needed. Standard real IFT and local stable/unstable manifold theory are used without new literature work.

### Draft result and scope inventory

- `eq:P10-exact-fold`: exact square completion and synchronous restriction, with P02 branch labels reconciled. P10's denominator s_f=1+r_f is explicitly distinguished from P02's fold amplitude s_f=r_f.
- `lem:P10-gap`: automatic strict transverse fold stability for every admissible n,q, with gap c/(1+r_f) times (1-cos(2*pi/n)); simple uniform zero; exact complex spectrum.
- `prop:P10-reduction`, `prop:P10-coefficients`, `thm:P10-saddle-node`: full real transverse IFT, original-vector nondegeneracy derivatives with the Taylor factor one-half, parameter-extended nilpotent center block and exact positive-time center normal form.
- `prop:P10-branch-signs`, `cor:P10-near-stability`: exact uniform signs on the entire two-root interval; near-fold upper sink and lower index-one saddle with n-1 stable dimensions.
- `thm:P10-bistability`, `prop:P10-bistability-set`: stable origin and stable upper coexist on a nonempty interval, persist openly in all five coefficients, and have an exact finite-spectrum coexistence set. G>=H suffices, including equality. An explicit sufficient near-fold interval is supplied.
- `rem:P10-counterexample`: exact canonical n=6,q=1 witness inside the two-root interval with upper eigenvalue lambda_3=191/125>0. Thus C147's universal origin/upper stable-coexistence interpretation is false; no claim about other attractors is made.
- `prop:P10-ray`, `prop:P10-local-basins`: exact synchronous-ray threshold; local unstable-manifold equality with synchrony; local stable disk tangent to E and an explicitly proved small-neighborhood partition into the two sink basins. The cap-exit proof is local; it does not identify a complete global basin boundary or exclude other attractors. B03 is resolved for this DRAFT to this scope only.
- P09 connection and b-down-to-zero limit are recorded without a two-parameter unfolding. P11 receives only the recorded branch signs, stable-fold data and the fact that any later upper instability in the interval must be nonuniform. No Hopf existence/frequency, pair simplicity, transversality, Lyapunov coefficient or periodic branch theorem is begun.

Only P10, this manifest, the necessary claim-registry and compendium bookkeeping, and the regenerated compendium PDF change. All other proofs, audits and support, canonical files, frozen theorem/novelty files and the dependency map remain byte-identical. No synced source is modified. Validation evidence and checker are delivered separately as `P10_validation_support.zip`.

The complete DRAFT archive is named exactly `cyclic_network_project_P10_draft.zip`. Neither the future `cyclic_network_project_A10_audit_only.zip` nor `cyclic_network_project_P10_audited.zip` is created.

P10 v1.0 full-file SHA-256: `a28ea2b4ca96f381f06fa82849d4289fcc0e9c41e646ca66595621922f385a07`. Hash scope: complete UTF-8 proof source.

### P10 final compilation, corroboration and preservation

- **Compilation: PASS.** Existing multi-file latexmk/pdfLaTeX build; **99 pages**, P10 on **78–87**. All 370 labels across 28 included source files are unique; input order is unchanged.
- **Diagnostics:** zero undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings or new warnings. Three pre-existing underfull-hbox spacing diagnostics remain in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130 (badness 1286, 1275 and 10000). A draft P10 display was reflowed before final compilation.
- **Visual review: PASS.** Front matter pages 1–3 and all ten P10 pages 78–87 were rendered and inspected. No clipping, overlap or missing text. PDF text on unchanged pages 4–77 is identical to the authenticated P09 baseline. P10 is a project fragment; the complete multi-file compendium is the canonical successful build.
- **Corroboration: PASS.** 1,534 exact rational assertions; 4,500 original-field/direct-matrix cases across 50 (n,q) pairs and six positive tuples, including 600 closest-to-fold branch checks; 4,000 additional static parameter-search cases; 180 transverse Newton probes. Python 3.12.14 / NumPy 2.3.5. Maximum scaled direct-spectrum discrepancy 2.458e-14; maximum scaled original-field residual 1.137e-16. All finite checks are corroboration, not proof, interval certification or independent audit.
- **Counterexample search:** the broad sample found 436 unstable-upper points and 1,138 lower-branch points with more than one unstable label. The source proves an exact rational witness for both failures away from the fold. No near-fold theorem is weakened and no P11 analysis is performed.
- **Preservation: PASS.** All 17 other Pxx files, all existing audit sources/PDFs/support, canonical files, shared macros, dependency map, frozen theorem/novelty documents and numerical plans remain byte-identical. Only P10, manifest, registry, compendium source and its regenerated PDF differ from the 176-member baseline. C070/C071/C147 change only their status cells; all other archival claim cells and all other prior claim rows are unchanged. No source file under synced `sources/` was modified.
- **Delivery:** `cyclic_network_project_P10_draft.zip`, complete 176-file snapshot under sole root `cyclic_network_project/`, plus separate `P10_validation_support.zip`. No future A10 or audited-P10 archive is created. Exact member hashes, CRC checks, checker and numerical outputs, build log and renders are in the validation companion. P10 remains **DRAFT / NOT AUDITED**; P11 is not begun.

## P10 audit closure — 2026-10-03 (CURRENT)

**P10 v1.1: VERIFIED / AUDITED. Required corrections: NONE.** A10 independently verifies exact P10 v1.0 in all six layers and overall. This is an administrative header-metadata closure, not a mathematical revision, and carries no AFTER MINOR REVISION qualifier. Every byte from the first line-anchored section command through EOF is preserved, including historical DRAFT/audit-pending wording. This entry and the current P10 header govern lifecycle status. P01–P05, P07, P08 and P09 retain their audited versions. P06 and P11–P18 remain TODO. **P11 is cleared to begin, but is not begun here.**

| A10 layer | Verdict |
|---|---|
| FOLD GEOMETRY / SPECTRUM | VERIFIED |
| FULL-SYSTEM SADDLE-NODE | VERIFIED |
| BRANCH STABILITY / BISTABILITY | VERIFIED |
| COEXISTENCE SET / COUNTEREXAMPLE | VERIFIED |
| BASIN / MANIFOLD | VERIFIED |
| SCOPE / DEPENDENCY | VERIFIED |
| OVERALL | VERIFIED |

### Exact version identity and authentication

- Audited source: `proofs/P10_saddle_node_and_bistability.tex`, P10 v1.0, 2026-10-03, 32,560 bytes, 707 lines; mathematical body begins at original line 19.
- Original audited full-file SHA-256: `a28ea2b4ca96f381f06fa82849d4289fcc0e9c41e646ca66595621922f385a07`.
- Original audited mathematical-body SHA-256: `5cfd8afb91b7f23575e1b4bd9c7c28f3b433affefae9bb0d5f7700d030fcba81`.
- Current P10 v1.1 full-file SHA-256: `37542cc5409d7db33ca183869933fbdbad673628f69f6988f2778a84bc84094f`.
- Current mathematical-body SHA-256: `5cfd8afb91b7f23575e1b4bd9c7c28f3b433affefae9bb0d5f7700d030fcba81`. **BYTE-FOR-BYTE UNCHANGED.**
- Immutable audit: `audits/A10_saddle_node_and_bistability.tex`, SHA-256 `ff2ebb0f84ae79fc9aad012a3945ef236e8ccdac9f47d64fd708e4dc66963b19`. Its PDF and all 21 supplied support files are also retained byte-for-byte.

Both copies of `cyclic_network_project_P10_draft.zip` have SHA-256 `a3b8ba33e16095a8880637bdfe74a2fcb2e26bcc1ada8d941efe85cbccf5c42e`. All 176 members matched the current working project before closure. A10's 28 input-inventory records authenticate against those files. All requested controls, proofs and prior audit sources are present. A02's historical missing-source note remains superseded by its source-restoration closure.

The immutable `cyclic_network_project_A10_audit_only.zip`, SHA-256 `0581dbd989d017d6a45b79b096aa64dc61be08cc92055f71acfb9808cc32b4c7`, contributes 23 new members. The complete current snapshot therefore has **199 files**. All existing audit sources through A10 are included; no A06 exists in the baseline or audit input, and none is fabricated.

### Scope and dependencies preserved

The direct dependency remains **P02/P03/P04/P09 -> P10**, with **P01 inherited**. P05/P07/P08 are authenticated context only, not theorem premises. There is no dependency on P11 or later results and no frozen-DAG change. All positive-fold geometry, effective-coefficient positivity, transverse gap, simple zero, transverse IFT, original-vector coefficients, exact center restriction, branch spectra, stable coexistence, physical openness, exact coexistence set, sufficient condition and explicit interval are retained unchanged.

The exact `(n,q)=(6,1)`, `(a,k,c,g,h)=(6,1/10,1/10,101/10,9/10)` counterexample remains unchanged, including upper `lambda_0=-12/5`, upper `lambda_3=191/125`, and lower unstable dimension three. The P09 connection, degenerate limit and all P11 exclusions remain unchanged.

Basin scope is exactly preserved: the threshold is global only on the invariant synchronous ray; the stable disk is the common basin boundary only relative to the sufficiently small full-space neighborhood V. No complete global basin boundary, whole-orthant partition, exactly-two-attractor assertion, exclusion of periodic attractors or Hopf/periodic-branch theorem is added.

### Validation provenance

A10 supplies independent analytical verification. It authenticated and inventoried the original `P10_validation_support.zip`, SHA-256 `3b545b222be77d2e8714784da34cea6494b4739b5241c3c60cd697ac69f4d760`, but **did not rerun the developer checker or independently reproduce its historical statistics**. Closure verifies the package hash and all 28 inventory member hashes; the original package is unchanged. It is not a mathematical premise.

A10's own separate corroboration records 794 exact assertions, 15,651 matrix cases across 139 network pairs, 1,668 near-fold branch cases, and 1,500 random interior tuples with both branches. These saved independent outputs and checker are preserved; neither developer nor audit checker is rerun for administrative closure. Finite computation and compilation remain corroboration, not proof, interval certification or manifold/basin certification. Prior A04/A05 provenance qualifications remain unchanged.

### Closure scope and delivery

Only P10 header comments, necessary manifest/registry/compendium status bookkeeping and the regenerated compendium PDF change. All other proof files, all completed audit sources/PDFs/support, canonical model, notation, shared macros, dependency map, frozen scope/novelty records and numerical plans are protected. Frozen files contain historical planning language and require no lifecycle exception.

The 170 archival claim rows retain all nonstatus cells. Only C070/C071/C147 and P10-D1–D10 status cells are promoted; C147 retains its precise universal origin/upper-coexistence interpretation and global exclusions. No later claim is promoted.

The complete audited snapshot is **`cyclic_network_project_P10_audited.zip`**, with sole root `cyclic_network_project/`. Both draft ZIP copies, the original audit-only ZIP and the original developer validation ZIP remain unchanged. Final compilation and preservation details follow below. No P11, P06, later module, numerical continuation or literature work is performed.

### Final A10 closure checks and delivery record

- **Compilation: PASS.** Current multi-file latexmk/pdfLaTeX build; **99 pages**, P10 on **78–87**. All **370 labels across 28 included source files** are unique; the input order is unchanged.
- **Diagnostics:** three pre-existing underfull-hbox spacing diagnostics in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130 (badness 1286, 1275, 10000). Zero new warnings, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings or errors. A transient front-matter spacing warning and spillover page were eliminated by shortening only the closure status paragraph before final compilation.
- **Visual review: PASS.** Final front matter pages 1–3 rendered and inspected. All ten P10 pages 78–87 are byte-identical to the previously reviewed draft renders. Extracted PDF text on pages 4–99 is unchanged. Historical DRAFT/audit-pending wording within P10 is intentionally preserved; its current header, front matter and manifest govern VERIFIED / AUDITED status.
- **P10 body preservation: PASS.** Every byte from the first line-anchored section command through EOF is identical to A10-audited v1.0; body SHA-256 remains `5cfd8afb91b7f23575e1b4bd9c7c28f3b433affefae9bb0d5f7700d030fcba81`. The current full-file hash differs solely because header comments changed.
- **All other proof/audit preservation: PASS.** The other 17 complete Pxx source files, including all P06/P11–P18 placeholders, are byte-identical. All existing audit sources/PDFs/support through A09 are unchanged. The A10 source/PDF and 21 support files match the immutable audit-only ZIP exactly. No A06 exists in the supplied project and none is fabricated.
- **Canonical and frozen preservation: PASS.** Canonical model, notation, shared macros, dependency map, frozen theorem and novelty files, numerical plans and all other existing members remain unchanged. No frozen lifecycle exception was necessary; synced `sources/` files are unchanged.
- **Registry preservation: PASS.** All 170 archival C-rows preserve every nonstatus cell. Only C070/C071/C147 and P10-D1–D10 status cells change; all other pre-existing claim rows remain byte-identical. No P11/later claim is promoted and all global-basin exclusions remain.
- **Validation provenance: PASS.** The original developer validation ZIP and every member authenticate against A10's inventory and remain unchanged. A10 inventoried/authenticated it but did not rerun or reproduce it. Its separate independent checker/results remain immutable corroboration. Neither checker is rerun for closure; A10's analytical reconstruction is the independent verification.
- **Complete snapshot:** **199 files** under sole root `cyclic_network_project/`: all 176 draft members plus all 23 A10 members. Exactly five draft members change: P10 header, manifest, registry, compendium source and regenerated PDF. The other 171 draft members are unchanged. No member is removed and no build intermediate is added to the snapshot.
- **Delivery:** `cyclic_network_project_P10_audited.zip`. ZIP CRC and every member byte pass. Both copies of `cyclic_network_project_P10_draft.zip`, `cyclic_network_project_A10_audit_only.zip` and the original `P10_validation_support.zip` retain their original names and hashes. Detailed closure evidence is separate from the project snapshot.
- **Final status:** P10 v1.1 **VERIFIED / AUDITED**, metadata-only closure of exact P10 v1.0; **no corrections**. Dependencies remain **P02/P03/P04/P09 -> P10, P01 inherited**, without P05/P07/P08 or later theorem inputs. All mathematical and basin-scope content is unchanged. **P11 is cleared but not begun.** No subsequent proof, continuation, unfolding or literature work was performed.

## P11 spectral conditions draft — 2026-10-03 (CURRENT)

**P11 v1.0 is DRAFT / NOT AUDITED. Independent A11 audit pending.** This entry supersedes earlier P11-TODO/cleared-not-begun wording only. P01–P05 and P07–P10 retain their audited versions; P06 and P12–P18 remain unchanged. P12 is not begun.

### Current-input authentication

The baseline is `cyclic_network_project_P10_audited.zip`, SHA-256 `e0ecae17063fced8ed0a6ebb6fcf44456d5c22065f51059274a0231659dcaaf5`. Its 199 members match the current P10 working project byte-for-byte. All ten requested control files and all P01–P05/P07–P10 and A01–A05/A07–A10 sources are present and authenticated. The current proof hashes match their manifest closures; metadata-only and minor-revision closures govern older historical body wording. A02's source-restoration closure remains in force.

The manifest-designated P11 filename remains `proofs/P11_hopf_spectral_conditions.tex`. The direct dependencies remain **P02, P04, P05 -> P11**, with **P07 as the conditional five-node input** and P03 inherited through P04. P08/P09/P10 are not mathematical premises and the frozen dependency map is unchanged.

### Draft result inventory and scope

- `lem:P11-pairs`, `prop:P11-frequency`: all reachable nonuniform representatives are genuine conjugate pairs; exact signed q=2 frequency and zero locus, with automatic negative frequency for u_j<=0.
- `thm:P11-strict`, `prop:P11-vectors`, `rem:P11-degeneracies`: complete strict selection gives one algebraically/geometrically simple imaginary pair, stable complement, positive gap, both inverse gates, real critical plane and Hermitian adjoint normalization. Ties and semisimple repeated zero eigenvalues are excluded precisely.
- `prop:P11-surface`: exact branch-state real part and k_H graph, partial_k R_j=-x; local physical transfer under P05's concave positive-chart hypotheses. The excluded zero-frequency locus has rank two where it exists for a genuine pair with positive cosine. No global topology is asserted.
- `prop:P11-realizability`: complete necessary-and-sufficient criterion for existence in each strict reachable nonuniform cell. The optional universal existence assertion fails at (n,j)=(8,1) and (12,2). P05's dominance realizability remains unchanged.
- `thm:P11-five`: exact physical tuple ((47+3sqrt(5))/4,(3sqrt(5)-5)/4,2,16,6), x_H=1; original-field residual zero; complete labeled complex spectrum; positive frequency sigma(10-phi); exact noncritical gap (3phi+1)/2; simple critical labels 1,4; exact two-root/upper-branch identity.
- `prop:P11-data`, `prop:P11-ledger`: fixed pi(g)=(a_H,k_H,2,g,6), local positive upper branch through x_+(16)=1; exact right/adjoint vectors, real block, inverse operators and mode denominators; H1–H9 established in the draft and H10–H12 expressly unestablished.

B02 is fixed for this draft to the stated upper branch and g-path. B06's spectral certification is exact algebra, with no numerical dependency. B07's Hermitian pairing/adjoint sign is checked; all nonlinear convention choices remain for P13. C073's archived numerical point is not used or reproduced. Only C072/C074 status cells change among the 170 archival claim rows, and P11-D1–D8 are added. No later claim is promoted.

No state derivative along g, eigenvalue crossing derivative, transversality, derivative tensor, first Lyapunov coefficient, first-loss theorem, nonlinear Hopf theorem, periodic branch or rotating-wave conclusion is included. `PROPOSED_P11_scope_clarification.md` proposes a clarification of older first-crossing planning wording; all frozen theorem/novelty documents remain byte-identical.

### Compilation, corroboration and delivery

- **Compilation: PASS.** Existing multi-file latexmk/pdfLaTeX build; **106 pages**, P11 on **88–95**. All 409 labels across 28 included source files are unique; input order is unchanged.
- **Diagnostics:** zero errors, undefined references, duplicate labels, macro conflicts, overfull boxes, LaTeX/package warnings or new diagnostics. Three inherited underfull-hbox diagnostics remain in unchanged `02_theorem_dependency_map.tex`, lines 126–127, 129–130 and 130–130 (badness 1286, 1275, 10000). Compilation does not verify mathematics.
- **Visual review: PASS.** Final front matter pages 1–3 and all P11 pages 88–95 rendered and inspected. No clipping, overlap or missing glyphs. Extracted PDF text on unchanged pages 4–87 matches the authenticated P10 baseline.
- **Corroboration: PASS.** 423 exact assertions; 100-digit radical readings; 510 reachable cells for n=5,...,64; 622 physical strict candidates; six critical ties and one exact physical zero-frequency example correctly excluded; 7,280 obstruction probes and 600 nonpositive-cosine frequency probes. Of 1,600 random trials, 329 are admissible strict candidates. Maximum scaled direct-spectrum discrepancy 8.6721e-14. Finite computation is not proof, interval certification or independent audit.
- **Preservation: PASS.** All 17 other Pxx sources, every completed audit and its support, canonical/notation files, shared macros, dependency map, frozen records and all remaining baseline members are byte-identical. Synced `sources/` files are untouched. Only P11, this manifest, the registry, compendium source and regenerated PDF change. One explicitly proposed note is added.
- **Complete snapshot:** 200 files under sole root `cyclic_network_project/`, retaining every baseline member. Exact name: **`cyclic_network_project_P11_draft.zip`**. Separate developer evidence: **`P11_validation_support.zip`**. Neither future `cyclic_network_project_A11_audit_only.zip` nor `cyclic_network_project_P11_audited.zip` is created.

P11 v1.0 full-file SHA-256: `4be8e9b1e64c022b635f3cca9f7f49ffbc5358a2250dda1715cb60e82d9b073b`. Hash scope: complete UTF-8 proof source. Final status: **DRAFT / NOT AUDITED; P12 not begun**.
