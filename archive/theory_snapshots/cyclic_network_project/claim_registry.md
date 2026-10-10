# Claim registry

This is an inventory, not a mathematical or literature audit. All mathematical statements and reported numbers are attributed candidates. A formula recorded here is not adopted as a fact, and “partially derived result” describes material already in the immutable archive, not work performed during initialization. “Corrected or rejected claim” records the prompt's terminology decision or an objection needing its own future checking; no replacement proof is supplied.

Every proposed theorem has a future proof owner. Main-paper Pxx owners are existing empty fragments. `future_papers/` paths are reserved names for postponed work only and have not been created. Optional items are explicitly excluded from a core module's completion gate unless later adopted. Definitions and modeling assumptions are canonical only when the explicit prompt or the disclosed notation contract says so.

The label “numerical observation” is the requested registry category for both reported observations and intended numerical claims. Rows explicitly say **unreproduced report** or **planned / no observation**. No reported value has been reproduced, and no new number has been computed. Source line numbers refer to the byte-identical `archive/directed_cyclic_networks_master.tex`. Repeated versions of a claim share a row. All eight requested claim classes are used.

## Evidence status vocabulary

TODO = no proof; UNVERIFIED = archived partial calculation; UNREPRODUCED = archived numerical report; NOT RUN = future numerical target; UNREVIEWED = literature not checked; UNESTABLISHED = interpretation only. No row is VERIFIED or AUDITED as a mathematical result. The proof lifecycle is defined in README.md.

## Definitions, model choices and motivating interpretations

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C001 | definition | Demand-modulated equation and its five-node specialization, as displayed in the master. | `eq:five-demand` (L486); `eq:DMnq` (L540) | [00_canonical_model.tex](00_canonical_model.tex) | DEFINED / provenance-qualified. Adopted only because the prompt explicitly freezes this model; no dynamical conclusion follows from adoption. |
| C002 | definition | Topology- and parameter-count-matched bilinear comparator. | `eq:MBnq` (L563) | [00_canonical_model.tex](00_canonical_model.tex) | DEFINED / provenance-qualified. Canonical by prompt B; quantitative calibration remains B05. |
| C003 | modeling assumption | Activities are normalized, dimensionless and intended to be nonnegative. | L313-340 | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. A modeling assumption; a dimensional derivation and individual reference scales remain NB01. |
| C004 | modeling assumption | Homogeneous nodes share an intrinsic law and cyclic wiring. | L460-475 | [00_canonical_model.tex](00_canonical_model.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. Canonical homogeneous modeling assumption; equivariance and consequences belong in later derivations. |
| C005 | modeling assumption | Predecessor input is intended to increase with source activity and encode enhanced demand in a depleted receiver. | L467-470 | [00_canonical_model.tex](00_canonical_model.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. Interpretive motivation; any precise monotonicity or comparison claim belongs in P08. |
| C006 | modeling assumption | Direct restraint is modeled through simultaneous activity; delays, noise and interventions are omitted from the base model. | L470-475 | [00_canonical_model.tex](00_canonical_model.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. Keep extension assumptions separate; no positivity result transfers automatically. |
| C007 | definition | Predecessor shift, Fourier labels and uniform/nonuniform mode terminology. | L342-362 | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Canonical normalization is the unitary convention in 01, not the unscaled vectors in the archive. |
| C008 | partially derived result | Archived shift eigenvector and conjugate-mode relations. | L351-362 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | UNVERIFIED. Independently derive with the fixed Fourier sign; include even-n singleton modes. |
| C009 | definition | Five-node mother, target and controller index maps. | `eq:five-maps` (L393) | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Adopt modulo-n definitions; explicitly translate original 1-based node labels. |
| C010 | definition | General step-q architecture and q=2 specialization. | L403-416 | [00_canonical_model.tex](00_canonical_model.tex) | DEFINED / provenance-qualified. Definition and prompt-specified scope; retain all admissible q. |
| C011 | proposed theorem | Step-q edges form one cycle when coprime and decompose into multiple cycles otherwise. | L411-416 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | TODO. Provide a future graph lemma if used beyond the prompt's connected-cycle convention; no full-graph disconnection inference. |
| C012 | modeling assumption | Archived baseline a=2, k=0.5, c=1, g=0.5, h=0.3. | `eq:baseline-parameters` (L502) | [numerics/N02_continuation_plan.tex](numerics/N02_continuation_plan.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. Parameter choice only, not a simulation or established stable regime. |
| C013 | literature-dependent claim | Five-node six-term equation is attributed to Lin–Han via generated material. | `eq:LB-five` (L583) | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Consult the original publication before confirming attribution, parameter domain or indexing. |
| C014 | modeling assumption | Arbitrary-(n,q) six-term extension is proposed in the master. | `eq:LBnq` (L595) | [00_canonical_model.tex](00_canonical_model.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. Archived only; not a verified literature equation or the primary comparator. |
| C015 | modeling assumption | Receiving-equation heterogeneous coefficients and the five perturbation profiles are proposed. | `eq:heterogeneous` (L617); `eq:hetero-expansion` (L627) | [proofs/P15_heterogeneous_equilibrium_persistence.tex](proofs/P15_heterogeneous_equilibrium_persistence.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. Resolve B08 before adopting this family; no coefficient assignment silently frozen. |
| C016 | modeling assumption | Optional source-saturating/demand-modulated positive input with Ks and Kd. | `eq:true-saturation-candidate` (L645) | `future_papers/F08_source_saturating_model.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Postponed separate model; prompt settles DM for the current project. |
| C017 | interpretation | Architecture organizes available modes while interaction laws organize stability, bifurcation and response. | L267-292; L1745-1776 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNESTABLISHED. Proposed synthesis, conditional on P04–P18 and the future overlap audit. |
| C018 | interpretation | Synchronous normalized activity is proposed as a balance interpretation; arbitrary n is a mathematical generalization. | L153-159; L1753-1759 | [open_decisions.md](open_decisions.md) | UNESTABLISHED. No clinical equivalence or direct general-n TCM claim. |
| C019 | literature-dependent claim | Wu-Xing node labels, generating/control diagrams, and descriptions of discrete versus continuous prior models. | L187-214; L364-401 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Exact primary/scholarly sources and model-by-model verification remain unreviewed. |

## Global foundation and synchronous equilibria

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C020 | proposed theorem | Local existence and uniqueness, smooth field on an open domain and a precise maximal interval. | L662-671 | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | TODO. Derive on the canonical extension domain; specify nonnegative initial data separately. |
| C021 | proposed theorem | Forward invariance of the nonnegative orthant. | `prop:absorbing-box` (L676) | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | TODO. Complete a boundary/uniqueness argument independently; handle all admissible offsets. |
| C022 | proposed theorem | Candidate invariant globally attracting box with Xmax=(a+sqrt(a^2+4kc))/(2k). | `prop:absorbing-box` (L676) | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | TODO. Candidate formula only; prove the precise attraction/absorption statement after B01. |
| C023 | proposed theorem | Global existence for every nonnegative initial state. | L682-686 | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | TODO. Supply a continuation argument after invariance and a suitable bound. |
| C024 | partially derived result | Recorded boundary calculation and upper-Dini comparison outline for the maximum coordinate. | L688-707 | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | UNVERIFIED. An archived outline, not a completed proof; tied maxima and comparison details remain TODO. |
| C025 | proposed theorem | Homogeneous synchronous subspace is invariant. | L709-713 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | TODO. Independently prove within the specified vector-field domain. |
| C026 | partially derived result | Recorded scalar restriction and its factored expression. | `eq:synchronous-scalar` (L718) | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | UNVERIFIED. Derive by substitution from canonical DM; do not use as a verified formula yet. |
| C027 | definition | Abbreviations A=k+h and mu=a+c−g. | `eq:A-mu` (L731) | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Adopted notation only, not a bifurcation assertion. |
| C028 | partially derived result | Candidate quadratic equation and formal roots of positive synchronous equilibria. | `eq:synchronous-quadratic` (L738); `eq:synchronous-roots` (L743) | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | UNVERIFIED. Independent algebra and admissibility checks, including denominators and zero roots. |
| C029 | proposed theorem | For mu>0, proposed exactly one positive synchronous root. | `prop:sync-classification` (L755); L757-760 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | TODO. Complete all assumptions and root-count proof. |
| C030 | proposed theorem | For mu=0, proposed zero and (a−A)/A branches with a positivity condition. | `prop:sync-classification` (L755); L762-768 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | TODO. Check multiplicities and avoid double-counting origin. |
| C031 | proposed theorem | For mu<0, proposed exact two-positive-root region with a>A and a+c<g<gf. | `prop:sync-classification` (L755); L770-777 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | TODO. Derive all inequalities and the complementary no-positive-root cases. |
| C032 | proposed theorem | Candidate coalescence at gf=a+c+(a−A)^2/(4A), xf=(a−A)/(2A). | `eq:fold-location` (L781) | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | TODO. Root coalescence alone is not the full-system saddle-node theorem; P10 owns that extension. |
| C033 | proposed theorem | Complete synchronous-equilibrium classification, including every equality, repeated-root and inadmissible case. | L749-791; Prompt-C5 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | TODO. Do not silently expand this into classification of all nonsynchronous equilibria. |
| C034 | partially derived result | Recorded origin Jacobian and Fourier spectrum. | `eq:origin-jacobian` (L797); `eq:origin-spectrum` (L802) | [proofs/P03_origin_and_linearization.tex](proofs/P03_origin_and_linearization.tex) | UNVERIFIED. Independently differentiate and check the Fourier convention. |
| C035 | proposed theorem | Origin spectral abscissa mu and stable/unstable classification away from mu=0. | L806-811 | [proofs/P03_origin_and_linearization.tex](proofs/P03_origin_and_linearization.tex) | TODO. Derive spectral ordering; separately classify the nonhyperbolic boundary. |
| C036 | proposed theorem | Origin behavior at mu=0 beyond linearization. | L810-811; Prompt-C12 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | TODO. State exactly which generic/degenerate cases and admissible state domain are covered. |

## Fourier spectrum, normality and mode selection

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C037 | partially derived result | Recorded homogeneous Jacobian coefficients and shift-polynomial representation. | `eq:linear-coefficients` (L846); `eq:d-diagonal` (L857); `eq:circulant-J` (L867) | [proofs/P03_origin_and_linearization.tex](proofs/P03_origin_and_linearization.tex) | UNVERIFIED. Differentiate independently and add coincident offsets; no generic-q shortcut. |
| C038 | proposed theorem | Arbitrary-(n,q) full complex Fourier eigenvalue formula. | `thm:general-spectrum` (L874); `eq:general-eigenvalue` (L877) | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | TODO. Derive with multiplicities and all modes; compare with an independent matrix construction later. |
| C039 | partially derived result | Recorded real/imaginary dispersion components. | `eq:general-real` (L889); `eq:general-imag` (L893) | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | UNVERIFIED. Independent sign and indexing checks. |
| C040 | corrected or rejected claim | Master states nonlinear local asymptotic stability iff maximum eigenvalue real part is strictly negative. | L898-902 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | NOT ACCEPTED as stated. Not accepted as a blanket equivalence; distinguish a Hurwitz criterion from nonhyperbolic nonlinear stability. This initialization supplies no replacement proof. |
| C041 | proposed theorem | Homogeneous circulant linearization is normal and unitarily diagonalizable. | L908-912 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | TODO. Prove from the adopted DFT conventions; do not extend to general heterogeneous matrices. |
| C042 | proposed theorem | Recorded equality for the Euclidean norm of the homogeneous linear propagator. | `eq:normal-decay` (L914) | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | TODO. Use verified P04 normality and specify time/domain assumptions. |
| C043 | proposed theorem | Stable homogeneous dynamics has no Euclidean nonmodal transient amplification, while individual coordinates may show delayed or oscillatory responses. | L917-924 | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | TODO. Separate norm and coordinate claims; no inference for nonlinear or heterogeneous trajectories. |
| C044 | definition | Archived spectral shorthand T0=G0−H0 and u_m=cos(theta_m). | `eq:T-coefficient` (L930) | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Definitions conditional on coefficients later derived; avoid collision with the time scale by using future tau. |
| C045 | partially derived result | Recorded step-two quadratic dispersion expression. | `eq:quadratic-dispersion` (L938) | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | UNVERIFIED. Independently derive after P04. |
| C046 | proposed theorem | Candidate uniform-mode maximizer when the quadratic coefficient is nonnegative. | `thm:mode-selection` (L944); L949-953 | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | TODO. Prove on the actual discrete cosine set with parity and all coefficient restrictions. |
| C047 | proposed theorem | Candidate concave-case continuous maximizer and nearest-cosine discrete selection rule, including uniform endpoint regime. | `thm:mode-selection` (L944); `eq:u-star` (L959); L955-966 | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | TODO. Check all regimes and equality cases; angle rounding is not an assumed equivalent rule. |
| C048 | proposed theorem | Exact mode-pair tie boundaries and multiplicities of maximizing modes. | L970-972 | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | TODO. Derive explicitly; separate conjugacy ties from distinct-pair ties. |
| C049 | proposed theorem | Candidate limit m*/n to arccos(u*)/(2pi). | `eq:large-n-mode` (L978) | [proofs/P06_large_n_limit.tex](proofs/P06_large_n_limit.tex) | TODO. Resolve B04; fix representatives, parameter family and admissible regime. |
| C050 | proposed theorem | Proposed O(n^−2) eigenvalue discretization error away from degeneracies. | L983-988 | [proofs/P06_large_n_limit.tex](proofs/P06_large_n_limit.tex) | TODO. Identify the error quantity, constants, uniformity and endpoint/tie exclusions. |
| C051 | partially derived result | Three recorded five-node real-part expressions involving the golden ratio. | `eq:five-real-0` (L998); `eq:five-real-1` (L1001); `eq:five-real-2` (L1004) | [proofs/P07_five_node_specialization.tex](proofs/P07_five_node_specialization.tex) | UNVERIFIED. Recompute all mode classes and full complex spectrum from P04. |
| C052 | proposed theorem | Candidate threshold H0−G0>C0/phi^2 for pair {1,4} to overtake the uniform mode. | `eq:five-threshold` (L1011); L1015-1016 | [proofs/P07_five_node_specialization.tex](proofs/P07_five_node_specialization.tex) | TODO. Compare all three classes, including pair {2,3}, and handle equality; dominance is not a Hopf assertion. |

## Matched bilinear and secondary comparison

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C053 | partially derived result | MB scalar restriction, M=k+g+h−c, and candidate y*=a/M when M>0. | L813-820; `eq:bilinear-M` (L822); `eq:bilinear-sync` (L827) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | UNVERIFIED. Derive all existence cases, including M=0 and M<0. |
| C054 | proposed theorem | Proposed finite-time blow-up of positive synchronous MB data for M<0. | L830-832 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Prove precisely and distinguish the synchronous invariant subspace from general trajectories. |
| C055 | proposed theorem | Proposed sufficient full-system MB boundedness condition such as k>c. | L833-835 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Derive a sufficient statement; do not label it necessary or confuse it with M>0. |
| C056 | proposed theorem | MB local existence and nonnegative-orthant invariance for positive parameters. | L1088-1090; L2341-2351 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Independent polynomial-system argument, separate from the DM proof. |
| C057 | partially derived result | Recorded real-part Fourier formula at positive MB synchrony. | `eq:matched-bilinear-real` (L1023) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | UNVERIFIED. Derive the full complex spectrum and all parameter restrictions. |
| C058 | proposed theorem | Proposed uniform eigenvalue −a and therefore symmetry-breaking instability whenever positive MB synchrony is unstable. | `eq:matched-bilinear-uniform` (L1033); L1035-1038 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Prove after establishing existence; do not infer that MB synchrony is always unstable. |
| C059 | partially derived result | Recorded MB step-two quadratic and continuous maximizer c/[4(g+h)]. | `eq:matched-bilinear-quadratic` (L1041); `eq:bilinear-u-star` (L1048) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | UNVERIFIED. Independent derivation and admissible-mode check. |
| C060 | proposed theorem | Full MB complex spectrum, exact step-two selection and all mode-tie boundaries. | L1052-1053 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Complete the missing result, including uniform and singleton modes. |
| C061 | proposed theorem | Exact controlled DM–MB comparison of positivity, boundedness, equilibrium geometry and spectral selection. | L1077-1098 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Use only completed component theorems; B05 governs quantitative calibration. |
| C062 | partially derived result | Recorded receiver-depletion limits of bilinear and demand-modulated predecessor inputs. | L1100-1105 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | UNVERIFIED. Audit directly under an explicitly fixed source and normalization; no medical superiority claim. |
| C063 | proposed theorem | Claim that bilinear stability has open stable and unstable parameter regions. | L1112-1116 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Derive exact inequalities and exhibit justified regions, not prior-dependent percentages. |
| C064 | proposed theorem | Symmetry-breaking Hopf is asserted possible in selected MB regimes. | L1096-1097 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Optional strengthened comparison: requires MB-specific spectral, transverse and nonlinear Hopf checks; cannot borrow DM l1. |
| C065 | partially derived result | Recorded six-term real-part spectrum at a proposed synchronous equilibrium. | `eq:six-term-real` (L1059) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | UNVERIFIED. Optional secondary application only; verify source model and equilibrium before deriving spectrum. |
| C066 | literature-dependent claim | Random stability fractions depend on coefficient prior and filtering and cannot define prior-independent model quality. | L1118-1121 | [numerics/N03_figure_plan.tex](numerics/N03_figure_plan.tex) | UNREVIEWED. If retained, disclose sampling law, validity filter and classification; no fractions are present or computed here. |

## Steady-state and Hopf bifurcations

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C067 | partially derived result | Recorded critical synchronous scalar form and negative nonsynchronous real parts at mu=0. | L1128-1143 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | UNVERIFIED. Independently check the full spectrum and parameter restrictions. |
| C068 | proposed theorem | Generic transcritical bifurcation for mu=0 and a≠A. | L1145-1152 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | TODO. Resolve B02; verify full-system nondegeneracy and orientation, with the nonnegative-domain qualification. |
| C069 | proposed theorem | Candidate codimension-two steady-state degeneracy at mu=0, a=A and a proposed two-parameter unfolding. | L1185-1197 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | TODO. Optional depth under NB07; derive independently if retained, otherwise explicitly exclude from completed scope. |
| C070 | proposed theorem | Full-system generic positive saddle-node under simple synchronous zero mode and noncritical other modes. | L1154-1166 | [proofs/P10_saddle_node_and_bistability.tex](proofs/P10_saddle_node_and_bistability.tex) | TODO. Verify all nondegeneracy hypotheses; do not infer from the quadratic discriminant alone. |
| C071 | proposed theorem | Actual bistable region requires stable origin and all-mode stable upper branch; lower branch allegedly separates relevant basins. | L1168-1183 | [proofs/P10_saddle_node_and_bistability.tex](proofs/P10_saddle_node_and_bistability.tex) | TODO. Resolve B03; prove local coexistence, exclusivity or basin structure only to the explicitly chosen scope. |
| C072 | definition | Definition of a candidate symmetry-breaking imaginary-axis pair with nonzero frequency. | `eq:hopf-spectral` (L1208) | [proofs/P11_hopf_spectral_conditions.tex](proofs/P11_hopf_spectral_conditions.tex) | DEFINED / provenance-qualified. Not an existence result or a Hopf theorem. |
| C073 | numerical observation | Unreproduced five-node crossing: a=1.5, k=0.65, c=1, g=0.5, h≈2.3718; reported pair ±0.310613 i. | L1221-1237 | [proofs/P11_hopf_spectral_conditions.tex](proofs/P11_hopf_spectral_conditions.tex) | UNREPRODUCED or NOT RUN. Archived report only; reproduce equilibrium, full spectrum, critical mode and crossing parameter independently before use. |
| C074 | proposed theorem | A unique simple nonzero-frequency pair with remaining modes off the imaginary axis is planned. | L1239-1250 | [proofs/P11_hopf_spectral_conditions.tex](proofs/P11_hopf_spectral_conditions.tex) | TODO. Verify simplicity, all other modes and relevant resonant/alias cases for the chosen branch. |
| C075 | partially derived result | Recorded total derivative of the modal real part, including equilibrium motion. | `eq:transversality` (L1253) | [proofs/P12_hopf_transversality.tex](proofs/P12_hopf_transversality.tex) | UNVERIFIED. Derive the branch derivative and all path dependence after B02. |
| C076 | proposed theorem | Nonzero Hopf transversality on the chosen path. | L1263-1264 | [proofs/P12_hopf_transversality.tex](proofs/P12_hopf_transversality.tex) | TODO. Give a rigorous sign/nonzero argument, not only a numerical slope. |
| C077 | definition | Archived Taylor expansion uses one-half and one-sixth tensor factors. | `eq:Taylor-vector-field` (L1270) | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | DEFINED / provenance-qualified. Convention candidate requiring B07; no tensors or values have been derived here. |
| C078 | corrected or rejected claim | Archived adjoint eigenvector equation and normalization are not accepted without reconciliation with a specified inner product. | L1276-1284 | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | NOT ACCEPTED as stated. B07; freeze consistent signs and scale before l1 or Hopf-shift analysis. No corrected equation is supplied now. |
| C079 | partially derived result | Recorded first-Lyapunov formula with bilinear/trilinear tensors and two resolvents. | `eq:first-Lyapunov` (L1288) | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | UNVERIFIED. Verify formula source, factors, adjoint convention and inverse existence; independently derive the model expression. |
| C080 | proposed theorem | Fourier selection rules send B(v_m,conj(v_m)) to mode 0, B(v_m,v_m) to mode 2m and C back to m, suggesting a scalar reduction. | L1303-1315 | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | TODO. Prove with unitary normalization and modular aliasing; audit claimed reduction to modes 0,m,2m. |
| C081 | proposed theorem | Rigorous l1 expression and a nonzero sign on a meaningful parameter interval. | L1313-1315; L2369-2377 | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | TODO. Resolve B06–B07; independently validate derivatives and two implementations later. |
| C082 | proposed theorem | Assembled nondegenerate symmetry-breaking Hopf theorem and super/subcritical branch classification. | L1239-1250; L1317-1326; Prompt-C14 | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | TODO. Combine P11/P12/l1 and precise orientation; stability additionally needs the remaining spectrum. |
| C083 | proposed theorem | A zero of l1 is a candidate generalized-Hopf/Bautin point. | L1322-1324 | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | TODO. Optional candidate only; additional degeneracy and unfolding conditions would need a separate proof slot if retained. |
| C084 | partially derived result | Recorded leading cosine branch and adjacent-node time shift m*T/n. | `eq:rotating-wave` (L1333); `eq:phase-shift` (L1343) | [proofs/P14_rotating_waves.tex](proofs/P14_rotating_waves.tex) | UNVERIFIED. Audit sign, representative and exact versus leading-order phase relation under B07. |
| C085 | proposed theorem | Equivariant rotating-wave conclusion, isotropy and distinct phases versus gcd-based phase clusters. | L1347-1355 | [proofs/P14_rotating_waves.tex](proofs/P14_rotating_waves.tex) | TODO. Apply precise equivariant hypotheses and prove exact nonlinear spatiotemporal symmetry. |
| C086 | numerical observation | Planned two-parameter transcritical, fold, Hopf and mode-switch curves; possible fold–Hopf, zero–Hopf, Hopf–Hopf and generalized-Hopf points. | L1357-1366 | [numerics/N02_continuation_plan.tex](numerics/N02_continuation_plan.tex) | UNREPRODUCED or NOT RUN. No observed diagram or special point is supplied; these are future search targets, not numerical evidence. |

## Heterogeneity, Green functions and response

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C087 | proposed theorem | Local unique smooth heterogeneous equilibrium under invertible Jacobian; stability persistence under suitable stable-base hypotheses. | L1373-1393 | [proofs/P15_heterogeneous_equilibrium_persistence.tex](proofs/P15_heterogeneous_equilibrium_persistence.tex) | TODO. Separate invertibility from hyperbolicity and Hurwitz stability; resolve B08; prove positivity and locality precisely. |
| C088 | partially derived result | Recorded equilibrium expansion x(eps)=x*1+eps*xi+O(eps^2). | `eq:heterogeneous-equilibrium-expansion` (L1379) | [proofs/P15_heterogeneous_equilibrium_persistence.tex](proofs/P15_heterogeneous_equilibrium_persistence.tex) | UNVERIFIED. Derive from a frozen family and specify norm, smoothness and remainder domain. |
| C089 | partially derived result | Recorded first-order parameter forcing for receiving-equation assignment. | `eq:heterogeneity-forcing` (L1400) | [proofs/P16_static_sensitivity_and_green_function.tex](proofs/P16_static_sensitivity_and_green_function.tex) | UNVERIFIED. Recompute after B08; do not import this expression for a different assignment. |
| C090 | partially derived result | Recorded linear correction equation J xi=−b and modal inverse expression. | `eq:Jxi` (L1411); `eq:xi-Fourier` (L1416) | [proofs/P16_static_sensitivity_and_green_function.tex](proofs/P16_static_sensitivity_and_green_function.tex) | UNVERIFIED. Independent derivation with the unitary DFT and invertibility assumptions. |
| C091 | proposed theorem | Proposed exact inverse norm and first-order static sensitivity bound using min mode modulus. | `eq:Jinverse-norm` (L1431); `eq:static-sensitivity-bound` (L1438) | [proofs/P16_static_sensitivity_and_green_function.tex](proofs/P16_static_sensitivity_and_green_function.tex) | TODO. Use verified normality; identify norm and singular cases. |
| C092 | interpretation | Static sensitivity can become large near a zero eigenvalue but need not diverge at a nonzero-frequency Hopf boundary. | L1441-1448 | [proofs/P16_static_sensitivity_and_green_function.tex](proofs/P16_static_sensitivity_and_green_function.tex) | UNESTABLISHED. Make a precise conditional result; do not assert divergence for every forcing direction. |
| C093 | partially derived result | Recorded localized self-production Green-function response with a 1/n Fourier sum. | `eq:green-function` (L1458) | [proofs/P16_static_sensitivity_and_green_function.tex](proofs/P16_static_sensitivity_and_green_function.tex) | UNVERIFIED. Derive localization forcing, conjugacy and normalization; supply a controlled first-order remainder. |
| C094 | proposed theorem | Directed static response need not be reflection-symmetric; quantitative direction and decay measures are proposed. | L1467-1471 | [proofs/P16_static_sensitivity_and_green_function.tex](proofs/P16_static_sensitivity_and_green_function.tex) | TODO. Define the measures under NB09; do not assume localization or a universal asymmetry theorem. |
| C095 | partially derived result | Recorded Fourier propagator for a localized initial perturbation. | `eq:transient-kernel` (L1478) | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | UNVERIFIED. Independently derive the kernel and distinguish linear and nonlinear dynamics. |
| C096 | proposed theorem | Least-stable modes are expected to dominate the late response near instability, with propagation direction inferred from phases or peak times. | L1488-1493 | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | TODO. State projection, gap and tie hypotheses and choose a propagation observable. |
| C097 | partially derived result | Recorded harmonic modal transfer function. | `eq:harmonic-response` (L1500) | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | UNVERIFIED. Specify temporal sign, forcing, stable steady response and resolvent assumptions. |
| C098 | proposed theorem | Near-Hopf dynamic amplification at an appropriate forcing frequency can coexist with moderate static sensitivity. | L1504-1510 | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | TODO. Prove a quantitative conditional response statement and distinguish resonant amplification from instability. |
| C099 | definition | Archived positive stability-margin notation is minus spectral abscissa at a stable base. | `eq:stability-margin` (L1516) | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Use delta to avoid the archive's alpha conflict; no stable regime is asserted. |
| C100 | proposed theorem | Candidate sufficient spectral stability condition based on Jacobian perturbation norm below the homogeneous margin. | `eq:stability-radius` (L1524) | [proofs/P18_stability_radius_and_hopf_shift.tex](proofs/P18_stability_radius_and_hopf_shift.tex) | TODO. Derive with exact assumptions; do not presume perturbed normality or apply a positive-margin bound at Hopf. |
| C101 | proposed theorem | Explicit computable heterogeneity tolerance, including direct coefficient effects and equilibrium shift. | L1529-1537 | [proofs/P18_stability_radius_and_hopf_shift.tex](proofs/P18_stability_radius_and_hopf_shift.tex) | TODO. Resolve B08–B09; control constants, norm and higher-order remainder. |
| C102 | partially derived result | Recorded first-order Hopf-threshold shift from left/right eigenvectors and crossing derivative. | `eq:hopf-threshold-shift` (L1544) | [proofs/P18_stability_radius_and_hopf_shift.tex](proofs/P18_stability_radius_and_hopf_shift.tex) | UNVERIFIED. Reconcile B07 conventions, include equilibrium motion, and derive independently. |
| C103 | proposed theorem | Heterogeneity patterns can advance or delay the threshold as predicted by the first-order shift. | L1557-1559 | [proofs/P18_stability_radius_and_hopf_shift.tex](proofs/P18_stability_radius_and_hopf_shift.tex) | TODO. Define a precise pattern-dependent conclusion and independently validate by continuation later. |
| C104 | proposed theorem | Optional hyperbolic periodic-orbit persistence under small heterogeneity, with exact wave symmetry generally lost. | L1561-1568 | [proofs/P15_heterogeneous_equilibrium_persistence.tex](proofs/P15_heterogeneous_equilibrium_persistence.tex) | TODO. Reserved optional P15 slot; additionally depends on P14 and hyperbolicity modulo phase; NB08 determines inclusion. |

## Numerical program and evidence restrictions

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C105 | modeling assumption | Adaptive Runge–Kutta and LSODA are provisional; rtol=10^−9, atol=10^−11 are recorded starting tolerances; AUTO-07p, MatCont or COCO are suggested. | L1590-1605 | [numerics/N01_validation_protocol.tex](numerics/N01_validation_protocol.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. Choices only; no method has been selected or numerical result produced here. |
| C106 | modeling assumption | Proposed n values 5,7,9,15,31 and ten representative dynamical regimes. | L1624-1642 | [numerics/N03_figure_plan.tex](numerics/N03_figure_plan.tex) | ADOPTED only where prompt-backed; otherwise PROPOSED. A future sampling plan; no regime is known to occur merely because it is listed; add parity and edge-case validation. |
| C107 | numerical observation | Proposed continuation, Floquet, phase-lag and quadratic heterogeneity-remainder agreement. | L1575-1588; L1607-1622; L1699-1715 | [numerics/N01_validation_protocol.tex](numerics/N01_validation_protocol.tex) | UNREPRODUCED or NOT RUN. No observations supplied; validation targets only; record independent implementations and refinement before any claim. |
| C108 | numerical observation | Nine planned figures covering architecture, laws, branches, spectra, comparison, bifurcations, waves, heterogeneity and five-node synthesis. | L1717-1737 | [numerics/N03_figure_plan.tex](numerics/N03_figure_plan.tex) | UNREPRODUCED or NOT RUN. No figure data or numerical conclusions exist at initialization; preserve per-figure proof gates. |

## Motifs and extensions reserved for other papers

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C109 | modeling assumption | Archived one-node logistic motif. | `eq:one-node-logistic` (L1867) | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Separate future-paper model; no phase-line proof included. |
| C110 | proposed theorem | Proposed phase-line analysis and equilibrium behavior of the logistic motif. | L1875-1876 | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | TODO. Future proof owner only; not a file created in this package. |
| C111 | modeling assumption | Archived two-node bilinear mother–child model. | `eq:two-node-bilinear` (L1882) | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Recover author source and reconcile coefficient names before analysis. |
| C112 | partially derived result | Recorded two-node positive equilibrium formula. | `eq:two-node-equilibrium` (L1896) | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | UNVERIFIED. Independent rederivation; archive notes inconsistent a_i/alpha_i and incomplete determinant work. |
| C113 | proposed theorem | Proposed alpha_1>M_2 beta_1 criterion for positivity and local stability of the two-node equilibrium. | L1918-1923 | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | TODO. Separate existence from stability and verify from scratch. |
| C114 | modeling assumption | Archived two-node demand-modulated motif. | `eq:two-node-demand` (L1929) | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Postponed model only. |
| C115 | proposed theorem | Proposed nullcline, equilibrium, invariant-region and local/global stability analysis of the two-node demand motif. | L1942-1943 | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | TODO. Future scoped statements required; no specific outcome assumed. |
| C116 | modeling assumption | Archived piecewise threshold motif with max terms. | `eq:two-node-threshold` (L1949) | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Separate piecewise-smooth model; no smooth-theorem transfer assumed. |
| C117 | proposed theorem | Proposed sector equilibria, invariant regions, switching-manifold and regularity classification. | L1962-1964 | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | TODO. Future proof with exact sectors and boundary conditions. |
| C118 | modeling assumption | Archived three-node motif contains unspecified positive term G(x,x_c). | `eq:three-node-source` (L1972) | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Incomplete model; author clarification required before analysis; not a defect in canonical DM. |
| C119 | proposed theorem | Proposed three-node piecewise-system analysis after recovering the missing term. | L1994-1995 | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | TODO. Cannot draft mathematical statements until that separate model is defined. |
| C120 | modeling assumption | Proposed slow–fast local/rest decomposition. | `eq:slow-fast-motif` (L2004) | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Time-scale separation is an additional future modeling assumption. |
| C121 | proposed theorem | Proposed singular-perturbation theorem tracking a stable frozen local branch. | L2012-2013 | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | TODO. Future hypotheses, time interval, normal hyperbolicity and error estimates needed. |
| C122 | interpretation | Local treatment-rule motifs are interpreted as approximately isolated over a time interval. | L1997-2001 | `future_papers/F01_motifs_and_slow_fast.tex` (reserved; postponed) | UNESTABLISHED. Interpretive claim requiring source and modeling justification; no clinical result. |
| C123 | modeling assumption | Candidate separate mother-loss/child-overdraw term. | `eq:overdraw-term` (L2029) | `future_papers/F02_pathology_models.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Choose a future mechanism and independently analyze the changed system. |
| C124 | modeling assumption | Candidate rebellious counter-action term and full extended pathology equation. | `eq:wu-term-original` (L2037); `eq:extended-pathology` (L2042) | `future_papers/F02_pathology_models.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Archived extension, not part of DM; positivity is specifically questioned in the archive. |
| C125 | partially derived result | Archived boundary calculation identifies a possible outward vector field for the counter-action extension. | L2055-2065 | `future_papers/F02_pathology_models.tex` (reserved; postponed) | UNVERIFIED. Recorded objection only; verify independently before a formal counterexample or rejection theorem. |
| C126 | modeling assumption | Proposed multiplicative or saturating alternative intended to preserve positivity. | `eq:wu-positive-candidate` (L2068) | `future_papers/F02_pathology_models.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Intention is not proof; choose mechanism and redo equilibria/Jacobian. |
| C127 | proposed theorem | Proposed positivity and dynamical analysis of a revised pathology model. | L2073-2075 | `future_papers/F02_pathology_models.tex` (reserved; postponed) | TODO. Future model contract first; no transfer of P01 without new verification. |
| C128 | modeling assumption | Candidate contextual set points and modified self-regulation. | `eq:adaptive-setpoint` (L2081); `eq:adaptive-logistic` (L2090) | `future_papers/F03_adaptive_set_points.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Postponed specification; parameter and state domains remain open. |
| C129 | proposed theorem | Proposed set-point positivity, invariant regions, equilibria and survival of homogeneous Fourier structure. | L2094-2096 | `future_papers/F03_adaptive_set_points.tex` (reserved; postponed) | TODO. Derive separately for the finalized adaptive model. |

## Archived six-term numerical reports and Lyapunov/integrability ideas

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C130 | numerical observation | Reported all-six-coefficients-one spectrum: −1; −0.5393±0.3919i; 0.2060±0.6340i. | `eq:reported-bilinear-eigs` (L2106) | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNREPRODUCED or NOT RUN. Unreproduced generated-draft report; confirm exact published equation, equilibrium and parameter interpretation. |
| C131 | interpretation | Reported spectrum is used to classify that particular synchronous equilibrium as unstable. | L2111-2113 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNESTABLISHED. Conditional interpretation of unverified inputs; not a generic bilinear-instability conclusion. |
| C132 | numerical observation | Reported six-term periodic orbit has period approximately 17.626. | L2114-2118 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNREPRODUCED or NOT RUN. Independently reproduce orbit, period and source settings; not evidence for the current DM model. |
| C133 | partially derived result | Archived differentiation identifies the flow direction as a solution of the variational equation. | L2120-2129 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNVERIFIED. Recheck regularity and exact statement; not an automatic Lyapunov-exponent conclusion. |
| C134 | proposed theorem | A bounded non-equilibrium autonomous trajectory is expected to have a zero flow-direction Lyapunov exponent. | L2129-2132 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | TODO. Specify nonvanishing/asymptotic-speed and spectrum hypotheses; do not accept the blanket statement without audit. |
| C135 | numerical observation | First purported published Lyapunov spectrum: {0.3885,−0.1719,−0.3473,−0.6833,−0.9731}. | `eq:reported-spectra` (L2136); L2138-2139 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNREPRODUCED or NOT RUN. Primary attribution, trajectory type, transient removal and numerical method unverified. |
| C136 | numerical observation | Second purported published Lyapunov spectrum: {0.6700,0.6606,−0.0761,−0.0794,−1.1751}. | `eq:reported-spectra` (L2136); L2139-2144 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNREPRODUCED or NOT RUN. Same source/method audit required; do not infer chaos or error from the list alone. |
| C137 | numerical observation | Candidate recomputed spectrum: {0.0011,−0.1232,−0.2721,−0.2728,−0.9998}. | `eq:recomputed-cycle-spectrum` (L2150) | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNREPRODUCED or NOT RUN. Unreproduced; check orbit, tangent equations, QR normalization and convergence with averaging time. |
| C138 | interpretation | Candidate recomputed list is described as consistent with one zero and four negative exponents. | L2152-2156 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNESTABLISHED. Consistency is not proof of a periodic orbit, exponent convergence or stability. |
| C139 | numerical observation | Restriction-only report: state approximately (0,0,0,2.3426,1.3038) and spectrum {0,0,−1.3038,−2.3426,−3.6464}. | `eq:boundary-equilibrium-spectrum` (L2163); L2167-2173 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNREPRODUCED or NOT RUN. Exact coefficients, residual, zero eigenspace and nonlinear stability remain unverified. |
| C140 | modeling assumption | Archived conservative restriction dot x_i=x_i(x_{i−1}−x_{i+1}) on five nodes. | `eq:volterra-five` (L2179) | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | ADOPTED only where prompt-backed; otherwise PROPOSED. Verify its derivation from the original six-term parameter restriction. |
| C141 | partially derived result | Archive supplies preliminary derivations of conserved I1=sum x_i and I2=product x_i. | `eq:first-integrals` (L2185); L2183-2197 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNVERIFIED. Partially derived in the archive only; independently rederive with domains, including logarithm restrictions. |
| C142 | proposed theorem | Candidate third integral I3=sum x_i x_{i+2}. | `eq:third-integral-candidate` (L2201) | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | TODO. Verify conservation and functional independence; no integral is certified here. |
| C143 | literature-dependent claim | Proposed relation to the periodic Volterra or Kac–van Moerbeke lattice. | L2205-2208 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | UNREVIEWED. Exact model dictionary and primary literature audit needed. |
| C144 | proposed theorem | Possible complete integrability, invariant-torus or quasiperiodicity conclusion. | L2205-2208 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | TODO. Conditional future program only; two integrals and finite-time exponents do not establish the proposed conclusion. |

## Corrections already flagged in the archive or required by the prompt

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C145 | corrected or rejected claim | “The bilinear synchronous equilibrium is generically unstable.” | L2223 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | NOT ACCEPTED as stated. Archive rejects the blanket claim; derive exact parameter regions before replacing it. |
| C146 | corrected or rejected claim | “If a+c≤g, no positive synchronous state exists.” | L2224 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | NOT ACCEPTED as stated. Archive flags missing two-root cases; P02 must independently classify them. |
| C147 | corrected or rejected claim | “The whole two-root interval is bistable.” | L2225 | [proofs/P10_saddle_node_and_bistability.tex](proofs/P10_saddle_node_and_bistability.tex) | NOT ACCEPTED as stated. Not established; B03 and full-system stability/basin analysis required. |
| C148 | corrected or rejected claim | “A complex pair crossing the imaginary axis proves Hopf.” | L2226 | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | NOT ACCEPTED as stated. Archive requires additional hypotheses; P11–P13 own the full theorem. |
| C149 | corrected or rejected claim | “The extended pathology model remains positive.” | L2227 | `future_papers/F02_pathology_models.tex` (reserved; postponed) | NOT ACCEPTED as stated. Archive records an obstruction; independently verify it in the postponed model. |
| C150 | corrected or rejected claim | “The positive input is Holling type II.” | L2228; L526-534 | [00_canonical_model.tex](00_canonical_model.tex) | NOT ACCEPTED as stated. Preferred terminology is demand-modulated by prompt A; no standard Holling label adopted. |
| C151 | corrected or rejected claim | “Two first integrals and small finite-time Lyapunov exponents prove quasiperiodicity.” | L2229 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | NOT ACCEPTED as stated. Not accepted; future integrability or invariant-torus argument required. |
| C152 | corrected or rejected claim | “Equal activity means equal organ function.” | L2230 | [open_decisions.md](open_decisions.md) | NOT ACCEPTED as stated. Normalization assumption only; clinical interpretation not established. |
| C153 | corrected or rejected claim | “A negative spectral abscissa proves global recovery.” | L2231 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | NOT ACCEPTED as stated. Not accepted; local linear conclusions do not provide a global basin/attraction result. |
| C154 | corrected or rejected claim | “Random parameter percentages measure model quality objectively.” | L2232 | [numerics/N03_figure_plan.tex](numerics/N03_figure_plan.tex) | NOT ACCEPTED as stated. Archive cautions about priors, validity filters and classifiers; no sampling result available. |
| C155 | corrected or rejected claim | “The golden ratio is a physiological feature.” | L2233 | [proofs/P07_five_node_specialization.tex](proofs/P07_five_node_specialization.tex) | NOT ACCEPTED as stated. No physiological inference; any algebraic occurrence must be established in P07. |
| C156 | corrected or rejected claim | “The general n model is a direct TCM model.” | L2234 | [open_decisions.md](open_decisions.md) | NOT ACCEPTED as stated. Prompt specifies a mathematical generalization inspired by the five-node case. |
| C157 | corrected or rejected claim | Two zero eigenvalues establish nonlinear neutral stability of the reported boundary equilibrium. | L2171-2173 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | NOT ACCEPTED as stated. Archive says this implication is insufficient; exact nonlinear analysis remains postponed. |

## Historical, interpretive and publication-context claims

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C158 | literature-dependent claim | Mother nourishes child and child draws upon mother. | L424-426 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Exact classical or scholarly wording, source, edition and translation needed. |
| C159 | literature-dependent claim | Deficiency in the mother leads to deficiency in the child. | L427-428 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Same source audit; not an empirical or clinical finding here. |
| C160 | literature-dependent claim | Excess in the mother leads to excess in the child. | L429 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Exact provenance and scope unverified. |
| C161 | literature-dependent claim | Excess child activity overdraws from the mother. | L430-431 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Exact provenance and distinction from the model's demand input needed. |
| C162 | literature-dependent claim | Sustained child weakness eventually weakens the mother. | L432 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Exact source and temporal scope unverified. |
| C163 | literature-dependent claim | Ordinary restraint is interpreted as controller suppression of its target. | L436-437 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Primary/scholarly relation to modeled sign conventions needed. |
| C164 | literature-dependent claim | Over-acting terminology and the excessive-controller or deficient-target narrative. | L438-440 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Check terminology, original wording and conservative translation. |
| C165 | literature-dependent claim | Rebellious counter-acting terminology and reversed weakening narrative. | L441-443 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Check terminology and distinction from a mathematical positivity claim. |
| C166 | literature-dependent claim | Four treatment principles recorded as Chinese phrases in the motif draft. | L447-458 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. Each phrase needs exact edition, chapter/page and translation before quotation or interpretation. |
| C167 | interpretation | Model limitations: abstract normalized activities, symmetry idealization, alternative normal behaviors, uncalibrated parameters and omitted mechanisms. | L1778-1803 | [open_decisions.md](open_decisions.md) | UNESTABLISHED. Preserve as limitations; no new empirical findings or medical conclusion. |
| C168 | literature-dependent claim | SURE-DS 2026 affiliation/support acknowledgment and named grant. | L1842-1850 | [open_decisions.md](open_decisions.md) | UNREVIEWED. Author confirmation at writing stage; copied archival context is not verification. |
| C169 | literature-dependent claim | Bibliographic entries, including placeholder Lin–Han, Nian–Li and classical sources, are proposed citation leads. | L2576-2650 | [03_literature_audit_template.tex](03_literature_audit_template.tex) | UNREVIEWED. No metadata or relevance audit performed; all citation use requires direct support. |
| C170 | interpretation | SIADS target, suggested contribution package, supplement scope and page allocation. | L2496-2553 | [open_decisions.md](open_decisions.md) | UNESTABLISHED. Publication planning only; no assessment of novelty, priority or acceptance is made. |

## Source-anchor coverage index

Every labeled equation, theorem and proposition in the master is mapped below. Unlabeled proposed theorems and important numerical/prose claims are mapped by line range in the entries above. This is a transcription-coverage check only.

| Master anchor | Line | Registry entries |
|---|---|---|
| `eq:five-maps` | 393 | C009 |
| `eq:five-demand` | 486 | C001 |
| `eq:baseline-parameters` | 502 | C012 |
| `eq:DMnq` | 540 | C001 |
| `eq:MBnq` | 563 | C002 |
| `eq:LB-five` | 583 | C013 |
| `eq:LBnq` | 595 | C014 |
| `eq:heterogeneous` | 617 | C015 |
| `eq:hetero-expansion` | 627 | C015 |
| `eq:true-saturation-candidate` | 645 | C016 |
| `prop:absorbing-box` | 676 | C021, C022 |
| `eq:synchronous-scalar` | 718 | C026 |
| `eq:A-mu` | 731 | C027 |
| `eq:synchronous-quadratic` | 738 | C028 |
| `eq:synchronous-roots` | 743 | C028 |
| `prop:sync-classification` | 755 | C029, C030, C031 |
| `eq:fold-location` | 781 | C032 |
| `eq:origin-jacobian` | 797 | C034 |
| `eq:origin-spectrum` | 802 | C034 |
| `eq:bilinear-M` | 822 | C053 |
| `eq:bilinear-sync` | 827 | C053 |
| `eq:linear-coefficients` | 846 | C037 |
| `eq:d-diagonal` | 857 | C037 |
| `eq:circulant-J` | 867 | C037 |
| `thm:general-spectrum` | 874 | C038 |
| `eq:general-eigenvalue` | 877 | C038 |
| `eq:general-real` | 889 | C039 |
| `eq:general-imag` | 893 | C039 |
| `eq:normal-decay` | 914 | C042 |
| `eq:T-coefficient` | 930 | C044 |
| `eq:quadratic-dispersion` | 938 | C045 |
| `thm:mode-selection` | 944 | C046, C047 |
| `eq:u-star` | 959 | C047 |
| `eq:large-n-mode` | 978 | C049 |
| `eq:five-real-0` | 998 | C051 |
| `eq:five-real-1` | 1001 | C051 |
| `eq:five-real-2` | 1004 | C051 |
| `eq:five-threshold` | 1011 | C052 |
| `eq:matched-bilinear-real` | 1023 | C057 |
| `eq:matched-bilinear-uniform` | 1033 | C058 |
| `eq:matched-bilinear-quadratic` | 1041 | C059 |
| `eq:bilinear-u-star` | 1048 | C059 |
| `eq:six-term-real` | 1059 | C065 |
| `eq:hopf-spectral` | 1208 | C072 |
| `eq:transversality` | 1253 | C075 |
| `eq:Taylor-vector-field` | 1270 | C077 |
| `eq:first-Lyapunov` | 1288 | C079 |
| `eq:rotating-wave` | 1333 | C084 |
| `eq:phase-shift` | 1343 | C084 |
| `eq:heterogeneous-equilibrium-expansion` | 1379 | C088 |
| `eq:heterogeneity-forcing` | 1400 | C089 |
| `eq:Jxi` | 1411 | C090 |
| `eq:xi-Fourier` | 1416 | C090 |
| `eq:Jinverse-norm` | 1431 | C091 |
| `eq:static-sensitivity-bound` | 1438 | C091 |
| `eq:green-function` | 1458 | C093 |
| `eq:transient-kernel` | 1478 | C095 |
| `eq:harmonic-response` | 1500 | C097 |
| `eq:stability-margin` | 1516 | C099 |
| `eq:stability-radius` | 1524 | C100 |
| `eq:hopf-threshold-shift` | 1544 | C102 |
| `eq:one-node-logistic` | 1867 | C109 |
| `eq:two-node-bilinear` | 1882 | C111 |
| `eq:two-node-equilibrium` | 1896 | C112 |
| `eq:two-node-demand` | 1929 | C114 |
| `eq:two-node-threshold` | 1949 | C116 |
| `eq:three-node-source` | 1972 | C118 |
| `eq:slow-fast-motif` | 2004 | C120 |
| `eq:overdraw-term` | 2029 | C123 |
| `eq:wu-term-original` | 2037 | C124 |
| `eq:extended-pathology` | 2042 | C124 |
| `eq:wu-positive-candidate` | 2068 | C126 |
| `eq:adaptive-setpoint` | 2081 | C128 |
| `eq:adaptive-logistic` | 2090 | C128 |
| `eq:reported-bilinear-eigs` | 2106 | C130 |
| `eq:reported-spectra` | 2136 | C135, C136 |
| `eq:recomputed-cycle-spectrum` | 2150 | C137 |
| `eq:boundary-equilibrium-spectrum` | 2163 | C139 |
| `eq:volterra-five` | 2179 | C140 |
| `eq:first-integrals` | 2185 | C141 |
| `eq:third-integral-candidate` | 2201 | C142 |

Inventory: 170 claim records; 81 labeled mathematical source anchors mapped. Original master SHA-256: `0a7850078ed62434b8c37c727637049c583972cd11159ac91345e6a8691e436d`.
