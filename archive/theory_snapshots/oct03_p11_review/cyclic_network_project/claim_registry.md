# Claim registry

This is an inventory, not a mathematical or literature audit. Archived mathematical statements and reported numbers are attributed candidates; current verification is recorded separately in the status cells. A formula recorded here is not adopted as a fact, and “partially derived result” describes material already in the immutable archive, not work performed during initialization. “Corrected or rejected claim” records the prompt's terminology decision or an objection needing its own future checking; the initialization itself supplied no replacement proof.

Every proposed theorem has a proof owner. As of 2026-10-03, P01–P04 are VERIFIED / AUDITED under their recorded closures; P05 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION (A05 E01 closed); P08 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION; P07 v1.1 is VERIFIED / AUDITED with metadata-only closure and no required correction; P09 v1.1 is VERIFIED / AUDITED (metadata-only closure, A09 requires no correction); P10 v1.1 is VERIFIED / AUDITED (metadata-only A10 closure, no corrections); P11 v1.0 is DRAFT / NOT AUDITED; P06 and P12–P18 remain TODO. `future_papers/` paths are reserved names for postponed work only and have not been created. Optional items are explicitly excluded from a core module's completion gate unless later adopted. Definitions and modeling assumptions are canonical only when the explicit prompt or the disclosed notation contract says so.

The label “numerical observation” is the requested registry category for both reported observations and intended numerical claims. Rows explicitly say **unreproduced report** or **planned / no observation**. No reported numerical observation has been reproduced, and no numerical simulation has been performed. Source line numbers refer to the byte-identical `archive/directed_cyclic_networks_master.tex`. Repeated versions of a claim share a row. All eight requested claim classes are used.

## Evidence status vocabulary

DRAFT = proposed complete proof awaiting independent audit; TODO = no proof; UNVERIFIED = archived partial calculation; UNREPRODUCED = archived numerical report; NOT RUN = future numerical target; UNREVIEWED = literature not checked; UNESTABLISHED = interpretation only. VERIFIED / AUDITED = independently audited mathematical result, with required corrections closed. Only the P01–P05-, P07-, P08- and P09-owned results identified below have this status. P05 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION following A05 E01. The proof lifecycle is defined in README.md.

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
| C008 | partially derived result | Archived shift eigenvector and conjugate-mode relations. | L351-362 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | VERIFIED / AUDITED (P04 v1.1 metadata-only closure, 2026-09-27; A04 VERIFIED on exact v1.0). thm:P04-spectrum and eq:P04-conjugacy derive the exact shift phases, normalized DFT, modular conjugacy and singleton label structure. A04 requires no correction; audited body unchanged; U01 historical-run reproducibility note is nonblocking. |
| C009 | definition | Five-node mother, target and controller index maps. | `eq:five-maps` (L393) | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Adopt modulo-n definitions; explicitly translate original 1-based node labels. |
| C010 | definition | General step-q architecture and q=2 specialization. | L403-416 | [00_canonical_model.tex](00_canonical_model.tex) | DEFINED / provenance-qualified. Definition and prompt-specified scope; retain all admissible q. |
| C011 | proposed theorem | Step-q edges form one cycle when coprime and decompose into multiple cycles otherwise. | L411-416 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | VERIFIED / AUDITED (P04 v1.1 metadata-only closure; A04 VERIFIED on exact v1.0). prop:P04-step-cycles proves gcd(n,q) step-q cycles of length n/gcd(n,q). No coprimality restriction on Fourier diagonalization and no full-network disconnection inference. A04 requires no correction; audited body unchanged; U01 historical-run reproducibility note is nonblocking. |
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
| C020 | proposed theorem | Local existence and uniqueness, smooth field on an open domain and a precise maximal interval. | L662-671 | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | VERIFIED / AUDITED (2026-09-27). P01 Proposition prop:P01-local proves smoothness on U and local uniqueness/maximal continuation; no sign assumptions needed for local existence. A01: CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION; E01 closed. |
| C021 | proposed theorem | Forward invariance of the nonnegative orthant. | `prop:absorbing-box` (L676) | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | VERIFIED / AUDITED (2026-09-27). P01 Proposition prop:P01-local proves every boundary-face statement and invariance using a negative-part maximum; c>=0 suffices. A01: CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION; E01 closed. |
| C022 | proposed theorem | Candidate invariant globally attracting box with Xmax=(a+sqrt(a^2+4kc))/(2k). | `prop:absorbing-box` (L676) | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | VERIFIED / AUDITED (2026-09-27), strengthened. P01 Lemma lem:P01-bound and Theorems thm:P01-global/thm:P01-absorption use R=max{0,(a-k+sqrt((a+k)^2+4kc))/(2k)}. Canonically the cube is invariant, attracting and finite-time absorbing with a common time for the entire orthant. The archived larger radius remains sufficient. R is not claimed optimal for the full model. A01: CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION; E01 closed. |
| C023 | proposed theorem | Global existence for every nonnegative initial state. | L682-686 | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | VERIFIED / AUDITED (2026-09-27). P01 Theorem thm:P01-global proves compact containment and continuation for k>0; Proposition prop:P01-kzero proves global existence also for k=0 with nonnegative c,g,h. A01: CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION; E01 closed. |
| C024 | partially derived result | Recorded boundary calculation and upper-Dini comparison outline for the maximum coordinate. | L688-707 | [proofs/P01_wellposedness_and_absorbing_box.tex](proofs/P01_wellposedness_and_absorbing_box.tex) | VERIFIED / AUDITED (2026-09-27): the archived outline is independently replaced by Lemmas lem:P01-max/lem:P01-bound and the scalar comparison proof. Every tied maximizer is covered, and the g-loss is retained for exact-radius absorption. A01: CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION; E01 closed. |
| C025 | proposed theorem | Homogeneous synchronous subspace is invariant. | L709-713 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 prop:P02-invariance: direct substitution and P01 uniqueness on the maximal interval in U; no n, q, gcd or distinct-offset restriction beyond indexing. A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C026 | partially derived result | Recorded scalar restriction and its factored expression. | `eq:synchronous-scalar` (L718) | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 eq:P02-scalar-original and eq:P02-scalar: s′=s[mu+(a-A)s-As^2]/(1+s), domain s>-1. Independently derived from canonical DM; A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C027 | definition | Abbreviations A=k+h and mu=a+c−g. | `eq:A-mu` (L731) | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Adopted notation only, not a bifurcation assertion. |
| C028 | partially derived result | Candidate quadratic equation and formal roots of positive synchronous equilibria. | `eq:synchronous-quadratic` (L738); `eq:synchronous-roots` (L743) | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 prop:P02-equation and eq:P02-roots: Q=As^2+(A-a)s-mu, D=(a+A)^2+4A(c-g), s_±=(a-A±sqrt(D))/(2A). Origin handled before division; filter zero and s<=-1. A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C029 | proposed theorem | For mu>0, proposed exactly one positive synchronous root. | `prop:sync-classification` (L755); L757-760 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 thm:P02-complete/thm:P02-positive: mu>0 gives exactly one simple positive root; the negative root is admitted only for g>c. A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C030 | proposed theorem | For mu=0, proposed zero and (a−A)/A branches with a positivity condition. | `prop:sync-classification` (L755); L762-768 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 thm:P02-complete: at mu=0, Q has roots 0 and (a-A)/A; the latter is positive iff a>A, negative if a<A, and merges into the repeated zero if a=A. Count origin once. A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C031 | proposed theorem | For mu<0, proposed exact two-positive-root region with a>A and a+c<g<gf. | `prop:sync-classification` (L755); L770-777 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 thm:P02-positive/cor:P02-canonical: two distinct positive roots iff mu<0, a>A, D>0, equivalently a>A and a+c<g<g_f. Equality and complementary cases included. A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C032 | proposed theorem | Candidate coalescence at gf=a+c+(a−A)^2/(4A), xf=(a−A)/(2A). | `eq:fold-location` (L781) | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 prop:P02-loci: repeated-root locus g_f=a+c+(a-A)^2/(4A), s_f=(a-A)/(2A); positive iff a>A, negative for 0<a<A, zero for a=A. Algebra only; P10 owns any bifurcation theorem. A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C033 | proposed theorem | Complete synchronous-equilibrium classification, including every equality, repeated-root and inadmissible case. | L749-791; Prompt-C5 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 thm:P02-complete: eleven exhaustive canonical cells, all real nonzero-root counts, domain/nonnegative/positive counts, equality and multiplicity cases. No classification of nonsynchronous equilibria. A02 E01 closed; CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED. |
| C034 | partially derived result | Recorded origin Jacobian and Fourier spectrum. | `eq:origin-jacobian` (L797); `eq:origin-spectrum` (L802) | [proofs/P03_origin_and_linearization.tex](proofs/P03_origin_and_linearization.tex) | VERIFIED / AUDITED (P03 v1.1 metadata-only closure, 2026-09-27; A03 VERIFIED on exact v1.0). eq:P03-origin-jacobian and prop:P03-origin-spectrum: direct differentiation gives J(0)=(a-g)I+cP; project DFT gives lambda_m=a-g+c exp(-i theta_m), all simple. A03 requires no correction; audited body unchanged. |
| C035 | proposed theorem | Origin spectral abscissa mu and stable/unstable classification away from mu=0. | L806-811 | [proofs/P03_origin_and_linearization.tex](proofs/P03_origin_and_linearization.tex) | VERIFIED / AUDITED (P03 v1.1 metadata-only closure, 2026-09-27; A03 VERIFIED on exact v1.0). prop:P03-stability/prop:P03-boundary: spectral abscissa mu uniquely at m=0; linear asymptotic stability iff mu<0, instability iff mu>0; at mu=0 one simple zero and all other modes strictly left. Full nonhyperbolicity also occurs on g=a+c cos(theta_m)>0 inside mu>0. Nonlinear boundary behavior remains P09; A03 requires no correction; audited body unchanged. |
| C036 | proposed theorem | Origin behavior at mu=0 beyond linearization. | L810-811; Prompt-C12 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | VERIFIED / AUDITED (P09 v1.1 metadata-only closure; A09 VERIFIED on exact v1.0; no corrections). prop:P09-generic-critical: unstable in U for b!=0 at mu=0; b<0 relative-orthant stability unclaimed. prop:P09-degenerate: b=0 critical origin is locally asymptotically stable in U, not exponentially, with checked center reduction and direct Lyapunov proof. |

## Fourier spectrum, normality and mode selection

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C037 | partially derived result | Recorded homogeneous Jacobian coefficients and shift-polynomial representation. | `eq:linear-coefficients` (L846); `eq:d-diagonal` (L857); `eq:circulant-J` (L867) | [proofs/P03_origin_and_linearization.tex](proofs/P03_origin_and_linearization.tex) | VERIFIED / AUDITED (P03 v1.1 metadata-only closure, 2026-09-27; A03 VERIFIED on exact v1.0). lem:P03-jacobian and prop:P03-homogeneous derive every entry and J=dI+CP+GP^(-q)-HP^q for all x*>-1; q=1, q=n-1 and even half-offset contributions are summed. Circulant structure proved; full homogeneous spectrum/normality deferred to P04; A03 requires no correction; audited body unchanged. |
| C038 | proposed theorem | Arbitrary-(n,q) full complex Fourier eigenvalue formula. | `thm:general-spectrum` (L874); `eq:general-eigenvalue` (L877) | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | VERIFIED / AUDITED (P04 v1.1 metadata-only closure; A04 VERIFIED on exact v1.0). thm:P04-spectrum and prop:P04-multiplicity give every complex eigenvalue, unitary diagonalization, and numerical eigenvalue multiplicity equal to the number of matching Fourier labels. All collision cases included; direct eigendecomposition checks are corroboration only. A04 requires no correction; audited body unchanged; U01 historical-run reproducibility note is nonblocking. |
| C039 | partially derived result | Recorded real/imaginary dispersion components. | `eq:general-real` (L889); `eq:general-imag` (L893) | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | VERIFIED / AUDITED (P04 v1.1 metadata-only closure; A04 VERIFIED on exact v1.0). eq:P04-real and eq:P04-imag derive r_m=d+C cos(theta_m)+(G-H) cos(q theta_m) and omega_m=-C sin(theta_m)+(G+H) sin(q theta_m), with independent sign checks. A04 requires no correction; audited body unchanged; U01 historical-run reproducibility note is nonblocking. |
| C040 | corrected or rejected claim | Master states nonlinear local asymptotic stability iff maximum eigenvalue real part is strictly negative. | L898-902 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | NOT ACCEPTED as stated. P04 replacement VERIFIED / AUDITED (v1.1 metadata-only closure; A04 VERIFIED on exact v1.0): cor:P04-stability gives linear exponential stability iff sa(J)<0. Nonlinear local asymptotic stability follows when sa(J)<0; sa(J)>0 implies instability; sa(J)=0 is generally inconclusive. No blanket nonlinear equivalence. A04 requires no correction; audited body unchanged; U01 historical-run reproducibility note is nonblocking. |
| C041 | proposed theorem | Homogeneous circulant linearization is normal and unitarily diagonalizable. | L908-912 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | VERIFIED / AUDITED (P04 v1.1 metadata-only closure; A04 VERIFIED on exact v1.0). thm:P04-spectrum and prop:P04-normality prove unitary diagonalization and normality at all synchronous states x*>-1, including repeats, cancellations, collisions and noncoprime offsets. No heterogeneous extension. A04 requires no correction; audited body unchanged; U01 historical-run reproducibility note is nonblocking. |
| C042 | proposed theorem | Recorded equality for the Euclidean norm of the homogeneous linear propagator. | `eq:normal-decay` (L914) | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | TODO. Use verified P04 normality and specify time/domain assumptions. |
| C043 | proposed theorem | Stable homogeneous dynamics has no Euclidean nonmodal transient amplification, while individual coordinates may show delayed or oscillatory responses. | L917-924 | [proofs/P17_transient_and_harmonic_response.tex](proofs/P17_transient_and_harmonic_response.tex) | TODO. Separate norm and coordinate claims; no inference for nonlinear or heterogeneous trajectories. |
| C044 | definition | Archived spectral shorthand T0=G0−H0 and u_m=cos(theta_m). | `eq:T-coefficient` (L930) | [01_notation_and_assumptions.tex](01_notation_and_assumptions.tex) | DEFINED / provenance-qualified. Definitions conditional on coefficients later derived; avoid collision with the time scale by using future tau. |
| C045 | partially derived result | Recorded step-two quadratic dispersion expression. | `eq:quadratic-dispersion` (L938) | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P05 v1.1, 2026-10-02; A05 E01 closed). eq:P05-quadratic and eq:P05-square derive the quadratic and its square completion from audited P04; no numerical premise or novelty claim. |
| C046 | proposed theorem | Candidate uniform-mode maximizer when the quadratic coefficient is nonnegative. | `thm:mode-selection` (L944); L949-953 | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P05 v1.1, 2026-10-02; A05 E01 closed). thm:P05-selection includes explicit endpoint differences for T>=0, including T=0, and both parities. |
| C047 | proposed theorem | Candidate concave-case continuous maximizer and nearest-cosine discrete selection rule, including uniform endpoint regime. | `thm:mode-selection` (L944); `eq:u-star` (L959); L955-966 | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P05 v1.1, 2026-10-02; A05 E01 closed). thm:P05-selection and eq:P05-regions give the full nearest-cosine rule, endpoint regimes and exact inequalities; no angular rounding assumption. |
| C048 | proposed theorem | Exact mode-pair tie boundaries and multiplicities of maximizing modes. | L970-972 | [proofs/P05_q2_mode_selection.tex](proofs/P05_q2_mode_selection.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P05 v1.1, 2026-10-02; A05 E01 closed). thm:P05-selection, thm:P05-reachable and thm:P05-realization classify maximal adjacent ties, all Fourier labels, attainable boundaries and local geometry; real-part ties do not imply eigenvalue equality. |
| C049 | proposed theorem | Candidate limit m*/n to arccos(u*)/(2pi). | `eq:large-n-mode` (L978) | [proofs/P06_large_n_limit.tex](proofs/P06_large_n_limit.tex) | TODO. Resolve B04; fix representatives, parameter family and admissible regime. |
| C050 | proposed theorem | Proposed O(n^−2) eigenvalue discretization error away from degeneracies. | L983-988 | [proofs/P06_large_n_limit.tex](proofs/P06_large_n_limit.tex) | TODO. Identify the error quantity, constants, uniformity and endpoint/tie exclusions. |
| C051 | partially derived result | Three recorded five-node real-part expressions involving the golden ratio. | `eq:five-real-0` (L998); `eq:five-real-1` (L1001); `eq:five-real-2` (L1004) | [proofs/P07_five_node_specialization.tex](proofs/P07_five_node_specialization.tex) | VERIFIED / AUDITED (P07 v1.1, metadata-only closure, 2026-10-03). lem:P07-trig and thm:P07-spectrum derive all five complex eigenvalues, exact radicals and conjugacy; thm:P07-ordering compares all three real-part classes. A07 VERIFIED; no correction required; exact audited v1.0 body unchanged. |
| C052 | proposed theorem | Candidate threshold H0−G0>C0/phi^2 for pair {1,4} to overtake the uniform mode. | `eq:five-threshold` (L1011); L1015-1016 | [proofs/P07_five_node_specialization.tex](proofs/P07_five_node_specialization.tex) | VERIFIED / AUDITED (P07 v1.1, metadata-only closure, 2026-10-03). cor:P07-selection proves pair {1,4} is uniquely dominant exactly when H-G>C/phi^2, retains equality, and excludes pair {2,3} directly. Canonical switch includes the equilibrium constraint; no Hopf claim. A07 VERIFIED; no correction required; exact audited v1.0 body unchanged. |

## Matched bilinear and secondary comparison

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C053 | partially derived result | MB scalar restriction, M=k+g+h−c, and candidate y*=a/M when M>0. | L813-820; `eq:bilinear-M` (L822); `eq:bilinear-sync` (L827) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). thm:P08-foundation derives the exact restriction and all real/nonnegative/positive synchronous equilibrium cases; positive iff M>0. |
| C054 | proposed theorem | Proposed finite-time blow-up of positive synchronous MB data for M<0. | L830-832 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). thm:P08-foundation proves synchronous blow-up at log(1+a/(abs(M)s0))/a for M<0 and exponential global growth for M=0; no classification of every trajectory. |
| C055 | proposed theorem | Proposed sufficient full-system MB boundedness condition such as k>c. | L833-835 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). prop:P08-bounds and cor:P08-stability give separate sufficient global/dissipative bounds; k>c is explicitly not necessary. No boundedness conclusion from M>0 alone. |
| C056 | proposed theorem | MB local existence and nonnegative-orthant invariance for positive parameters. | L1088-1090; L2341-2351 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). thm:P08-foundation independently proves polynomial local flow on R^n, face invariance, and coordinate sign preservation on the maximal interval. |
| C057 | partially derived result | Recorded real-part Fourier formula at positive MB synchrony. | `eq:matched-bilinear-real` (L1023) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). thm:P08-spectrum derives the full complex spectrum, signed real/imaginary parts, normality and every offset collision directly from MB. |
| C058 | proposed theorem | Proposed uniform eigenvalue −a and therefore symmetry-breaking instability whenever positive MB synchrony is unstable. | `eq:matched-bilinear-uniform` (L1033); L1035-1038 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). thm:P08-spectrum proves lambda_0=-a by two independent derivations. Any instability is nonuniform; no universal instability or bifurcation type is claimed. |
| C059 | partially derived result | Recorded MB step-two quadratic and continuous maximizer c/[4(g+h)]. | `eq:matched-bilinear-quadratic` (L1041); `eq:bilinear-u-star` (L1048) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). eq:P08-quadratic and eq:P08-vertex prove strict concavity and distinguish the unconstrained vertex from the interval/grid maximizer. |
| C060 | proposed theorem | Full MB complex spectrum, exact step-two selection and all mode-tie boundaries. | L1052-1053 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). thm:P08-selection gives exact finite-grid cells, all maximal ties, labels, parity, reachable set, MB realizability and cell-wise stability. |
| C061 | proposed theorem | Exact controlled DM–MB comparison of positivity, boundedness, equilibrium geometry and spectral selection. | L1077-1098 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). thm:P08-pair-realization, thm:P08-forward, thm:P08-reverse and prop:P08-lower prove exact open same-tuple comparisons with own named branches, including size/branch obstructions. Structural growth comparison is outside the common equilibrium domain. |
| C062 | partially derived result | Recorded receiver-depletion limits of bilinear and demand-modulated predecessor inputs. | L1100-1105 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). Matching remark proves fixed-source z>0 receiver-depletion limits cz and 0 directly. No empirical calibration or medical-superiority inference. |
| C063 | proposed theorem | Claim that bilinear stability has open stable and unstable parameter regions. | L1112-1116 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | VERIFIED / AUDITED AFTER MINOR REVISION (P08 v1.1, 2026-10-03; A08 E01 closed). Exact MB stability criterion and explicit open stable/unstable regions; both stability directions of same-tuple comparison proved with precise size/branch scopes. |
| C064 | proposed theorem | Symmetry-breaking Hopf is asserted possible in selected MB regimes. | L1096-1097 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | TODO. Optional strengthened comparison: requires MB-specific spectral, transverse and nonlinear Hopf checks; cannot borrow DM l1. |
| C065 | partially derived result | Recorded six-term real-part spectrum at a proposed synchronous equilibrium. | `eq:six-term-real` (L1059) | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | UNVERIFIED. Optional secondary application only; verify source model and equilibrium before deriving spectrum. |
| C066 | literature-dependent claim | Random stability fractions depend on coefficient prior and filtering and cannot define prior-independent model quality. | L1118-1121 | [numerics/N03_figure_plan.tex](numerics/N03_figure_plan.tex) | UNREVIEWED. If retained, disclose sampling law, validity filter and classification; no fractions are present or computed here. |

## Steady-state and Hopf bifurcations

| ID | Classification | Candidate claim / archival content | Master locator | Future proof or record owner | Current status; evidence required |
|---|---|---|---|---|---|
| C067 | partially derived result | Recorded critical synchronous scalar form and negative nonsynchronous real parts at mu=0. | L1128-1143 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | VERIFIED / AUDITED (P09 v1.1 metadata-only closure; A09 VERIFIED on exact v1.0; no corrections). lem:P09-gap, prop:P09-coefficients and thm:P09-reduction independently check the critical scalar derivatives, simple zero, explicit transverse gap and completeness of the local synchronous equilibrium set. |
| C068 | proposed theorem | Generic transcritical bifurcation for mu=0 and a≠A. | L1145-1152 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | VERIFIED / AUDITED (P09 v1.1 metadata-only closure; A09 VERIFIED on exact v1.0; no corrections). thm:P09-transcritical, cor:P09-physical: fixed a,k,c,h,n,q, varying g; full-system nondegeneracy, exact center normal form, slopes -1/b in mu and 1/b in g, all-mode stability exchange and physical branch orientation. No nearby nonsynchronous equilibria. |
| C069 | proposed theorem | Candidate codimension-two steady-state degeneracy at mu=0, a=A and a proposed two-parameter unfolding. | L1185-1197 | [proofs/P09_transcritical_bifurcation.tex](proofs/P09_transcritical_bifurcation.tex) | VERIFIED / AUDITED IN PART (P09 v1.1 metadata-only closure; A09 VERIFIED; no corrections). prop:P09-degenerate and prop:P09-codimension establish cubic-degenerate geometry, full local stability and rank-two algebraic/spectral locus only. Proposed two-parameter unfolding remains EXCLUDED / UNPROVED; no pitchfork or other named codimension-two classification. |
| C070 | proposed theorem | Full-system generic positive saddle-node under simple synchronous zero mode and noncritical other modes. | L1154-1166 | [proofs/P10_saddle_node_and_bistability.tex](proofs/P10_saddle_node_and_bistability.tex) | VERIFIED / AUDITED (P10 v1.1; metadata-only A10 closure of exact v1.0). thm:P10-saddle-node: full-system nondegenerate positive fold for all a>k+h and admissible n,q; automatic transverse gap, simple zero, real transverse IFT, nonzero original-vector coefficients and exact center normal form. A10 VERIFIED; no required correction. |
| C071 | proposed theorem | Actual bistable region requires stable origin and all-mode stable upper branch; lower branch allegedly separates relevant basins. | L1168-1183 | [proofs/P10_saddle_node_and_bistability.tex](proofs/P10_saddle_node_and_bistability.tex) | VERIFIED / AUDITED (P10 v1.1; metadata-only A10 closure of exact v1.0). thm:P10-bistability and prop:P10-bistability-set prove nonempty open exponential stable coexistence. prop:P10-ray and prop:P10-local-basins prove the synchronous threshold and a local stable disk with local basin sides only. Complete global boundary/exclusivity is not claimed. B03 scoped locally; A10 VERIFIED; no required correction. |
| C072 | definition | Definition of a candidate symmetry-breaking imaginary-axis pair with nonzero frequency. | `eq:hopf-spectral` (L1208) | [proofs/P11_hopf_spectral_conditions.tex](proofs/P11_hopf_spectral_conditions.tex) | DRAFT (P11 v1.0); def:P11-candidate makes complete strict representative selection, r_j=0 and nonzero frequency explicit. Existence is supplied separately by thm:P11-five; no Hopf conclusion. |
| C073 | numerical observation | Unreproduced five-node crossing: a=1.5, k=0.65, c=1, g=0.5, h≈2.3718; reported pair ±0.310613 i. | L1221-1237 | [proofs/P11_hopf_spectral_conditions.tex](proofs/P11_hopf_spectral_conditions.tex) | UNREPRODUCED or NOT RUN. Archived report only; reproduce equilibrium, full spectrum, critical mode and crossing parameter independently before use. |
| C074 | proposed theorem | A unique simple nonzero-frequency pair with remaining modes off the imaginary axis is planned. | L1239-1250 | [proofs/P11_hopf_spectral_conditions.tex](proofs/P11_hopf_spectral_conditions.tex) | DRAFT (P11 v1.0); thm:P11-strict proves each critical numerical eigenvalue simple, all remaining modes strictly stable, positive gap and both inverse gates. Ties, zero frequency and singletons are excluded explicitly. Independent A11 audit pending. |
| C075 | partially derived result | Recorded total derivative of the modal real part, including equilibrium motion. | `eq:transversality` (L1253) | [proofs/P12_hopf_transversality.tex](proofs/P12_hopf_transversality.tex) | UNVERIFIED. Derive the branch derivative and all path dependence after B02. |
| C076 | proposed theorem | Nonzero Hopf transversality on the chosen path. | L1263-1264 | [proofs/P12_hopf_transversality.tex](proofs/P12_hopf_transversality.tex) | TODO. Give a rigorous sign/nonzero argument, not only a numerical slope. |
| C077 | definition | Archived Taylor expansion uses one-half and one-sixth tensor factors. | `eq:Taylor-vector-field` (L1270) | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | DEFINED / provenance-qualified. Convention candidate requiring B07; no tensors or values have been derived here. |
| C078 | definition | Archived opposite-sign adjoint equation with Hermitian normalization is a standard convention. | L1276-1284; Phase 1 S01 Eq. (16), S02 Appendix B | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | LITERATURE CHECKED convention only. The initialization’s rejection/suspicion is withdrawn; B07 retains scaling and orientation checks. No DM coefficient or proof is verified. |
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
| C145 | corrected or rejected claim | “The bilinear synchronous equilibrium is generically unstable.” | L2223 | [proofs/P08_matched_bilinear_analysis.tex](proofs/P08_matched_bilinear_analysis.tex) | NOT ACCEPTED as stated. P08 v1.1 (VERIFIED / AUDITED AFTER MINOR REVISION; A08 E01 closed) supplies exact MB stability inequalities and explicit open stable and unstable regions; no prior-dependent or universal meaning of generically unstable is asserted. |
| C146 | corrected or rejected claim | “If a+c≤g, no positive synchronous state exists.” | L2224 | [proofs/P02_synchronous_subspace_and_equilibria.tex](proofs/P02_synchronous_subspace_and_equilibria.tex) | NOT ACCEPTED as stated; replacement classification VERIFIED / AUDITED (P02 v1.1, 2026-09-27). P02 cor:P02-canonical and exact cases IV/VIII explicitly refute the archived exclusion at equality and for g>a+c. A02 E01 closed; replacement classification and rejection audited. |
| C147 | corrected or rejected claim | “The whole two-root interval is bistable.” | L2225 | [proofs/P10_saddle_node_and_bistability.tex](proofs/P10_saddle_node_and_bistability.tex) | REFUTED / VERIFIED / AUDITED (P10 v1.1, metadata-only closure of exact v1.0) for universal origin/upper stable coexistence. rem:P10-counterexample: n=6,q=1, (a,k,c,g,h)=(6,1/10,1/10,101/10,9/10), r_+=4, lambda_3=191/125>0. Other-attractor/global-exclusivity interpretations remain unproved; A10 VERIFIED; no required correction. |
| C148 | corrected or rejected claim | “A complex pair crossing the imaginary axis proves Hopf.” | L2226 | [proofs/P13_first_lyapunov_coefficient.tex](proofs/P13_first_lyapunov_coefficient.tex) | NOT ACCEPTED as stated. Archive requires additional hypotheses; P11–P13 own the full theorem. |
| C149 | corrected or rejected claim | “The extended pathology model remains positive.” | L2227 | `future_papers/F02_pathology_models.tex` (reserved; postponed) | NOT ACCEPTED as stated. Archive records an obstruction; independently verify it in the postponed model. |
| C150 | corrected or rejected claim | “The positive input is Holling type II.” | L2228; L526-534 | [00_canonical_model.tex](00_canonical_model.tex) | NOT ACCEPTED as stated. Preferred terminology is demand-modulated by prompt A; no standard Holling label adopted. |
| C151 | corrected or rejected claim | “Two first integrals and small finite-time Lyapunov exponents prove quasiperiodicity.” | L2229 | `future_papers/F07_lyapunov_and_integrability_reanalysis.tex` (reserved; postponed) | NOT ACCEPTED as stated. Not accepted; future integrability or invariant-torus argument required. |
| C152 | corrected or rejected claim | “Equal activity means equal organ function.” | L2230 | [open_decisions.md](open_decisions.md) | NOT ACCEPTED as stated. Normalization assumption only; clinical interpretation not established. |
| C153 | corrected or rejected claim | “A negative spectral abscissa proves global recovery.” | L2231 | [proofs/P04_arbitrary_nq_fourier_spectrum.tex](proofs/P04_arbitrary_nq_fourier_spectrum.tex) | NOT ACCEPTED as stated. P04 v1.1 VERIFIED / AUDITED explains that the negative spectral-abscissa criterion gives local nonlinear stability, without a global-attraction or basin claim. A04 requires no correction; audited body unchanged; U01 historical-run reproducibility note is nonblocking. |
| C154 | corrected or rejected claim | “Random parameter percentages measure model quality objectively.” | L2232 | [numerics/N03_figure_plan.tex](numerics/N03_figure_plan.tex) | NOT ACCEPTED as stated. Archive cautions about priors, validity filters and classifiers; no sampling result available. |
| C155 | corrected or rejected claim | “The golden ratio is a physiological feature.” | L2233 | [proofs/P07_five_node_specialization.tex](proofs/P07_five_node_specialization.tex) | NOT ACCEPTED as stated. P07 lem:P07-trig and rem:P07-geometry establish the algebraic fifth-root origin, VERIFIED / AUDITED by A07; no physiological, medical, biological-optimum or empirical TCM conclusion. P07 v1.1 is metadata-only closure; the rejected interpretation is not promoted. |
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

## Phase 1 literature overlay

The eight main novelty targets are assessed in [novelty_matrix.tex](novelty_matrix.tex), using the sources and locators in [03_literature_audit.tex](03_literature_audit.tex). The blueprint is not novelty evidence. The only changed original claim classification is C078, correcting an initialization convention error. All theorem owners and mathematical TODO statuses remain unchanged. Relevant five-element sources are part of the main novelty audit, regardless of the older reserved archival paths.


## Phase 1B adversarial novelty overlay — 2026-09-24

All 170 original claim records and their owners remain preserved. This overlay concerns priority and presentation, not mathematical truth. Neither RED nor YELLOW establishes a DM theorem; every proposed theorem remains TODO and archived calculations remain unverified. No master statement is used as evidence of novelty. Exact source locations are in [04_adversarial_novelty_audit.tex](04_adversarial_novelty_audit.tex).

| Overlay ID | Existing claims / owners | Current novelty disposition | Evidence / gate |
|---|---|---|---|
| B1-T1 | C001; canonical DM law and five-node motivation | GRAY: exact coupling priority unresolved; topology and saturation alone unsafe as novelty | S13–S18 and older source queue. Retrieve full enzymatic models before priority claim. |
| B1-T2 | C039–C041; P03–P04 | RED for general Fourier/normality novelty; C040 remains rejected in its blanket nonlinear form | S07/S09. Correctly derive the actual Jacobian later; keep as support. |
| B1-T3 | C045–C048; P05 | ORANGE: quadratic rule overlaps standard optimization and S03 | Strengthen to admissible parameter regions, ties and realizable first-instability consequences. |
| B1-T4 | C049–C050; P06 | RED for the basic fixed-symbol limit | S03 Proposition 6; quantitative finite-size consequences proposed, not proved. |
| B1-T5 | C002, C051–C059; P07–P08 | MB at n=5,q=2 is contained in S05; comparative specialization conditionally YELLOW | S05 §2.1 Eq.(2), p.778. Freeze comparison rule and prove an actual contrast; no model novelty inferred. |
| B1-T6 | C074–C085; P11–P14 | ORANGE for l1 reduction; general equivariant rotating-wave machinery is known | S02 Appendix D, S08 Lemma 1, S22. Realizability and sign information remain proposed. C078's Phase 1 convention correction is retained. |
| B1-T7 | C087–C098; P15–P17 | RED for implicit-function/DFT response identities; sharper localization is only a candidate | S07/S19/S20. Specify perturbation family, distance, uniformity and nonlinear remainder. |
| B1-T8 | C099–C103; P18 | RED for generic margin/derivative formulas; structured nonlinear certificate is a candidate | S10/S11/S21; S24 is additional overlap for disorder/mode-mixing narratives. |

The proposed strengthened statements S05/S06/S08/S11/S13/S16/S18 are recorded in [novelty_decisions.md](novelty_decisions.md) as unproved planning specifications, not replacements for the original claims or canonical conventions. The reported numerical crossing C073 and all continuation targets remain unreproduced/not run.

## Phase 1C current novelty overlay — 2026-09-24

The 170 original claim records, classifications and owners are preserved. This overlay supersedes earlier novelty ratings only; it supplies no proof or numerical verification. Source evidence and limits are in `05_priority_closure.tex`. Exact-model priority remains unclosed. The four-paper enzymatic chain is identified and the 2024 supplement inspected, but the main equation/theorem inventories remain incomplete.

| Overlay ID | Proposed claim / owner | Current verdict | Release gate |
|---|---|---|---|
| C1-N1 | Arbitrary-(n,q) spectrum / P04 | KNOWN / ROUTINE | Unitary diagonalization of a circulant is established theory. The DM coefficients still require independent differentiation; no new spectral method is claimed. |
| C1-N2 | q=2 exact finite-n selection / P05 | SUPPORTING SPECIALIZATION | The bare quadratic maximization is a routine adaptation of the mechanism explicitly used by van Kekem–Sterk, §4.2, p.37. A realizable all-parameter classification is a stronger proposed target, not an accomplished theorem. |
| C1-N3 | Mode-switch boundaries / P05, P08 | POSSIBLE NOVEL CONTRIBUTION | Equal-value boundaries alone are routine. Nonempty admissible parameter cells, all ties and exclusions, and a certified change in first instability could add model-specific content. |
| C1-N4 | Large-n selected-wave-number limit / P06 | KNOWN / ROUTINE | A fixed-symbol dense-grid limit has the direct precedent of van Kekem–Sterk Proposition 6, p.13. Retain only as a corollary with an actual comparison or finite-size consequence. |
| C1-N5 | Matched DM–MB comparison / P08; P11–P13 if criticality is compared | STRONG NOVELTY CANDIDATE | This rating applies to an exact qualitative contrast on a nonempty common admissible regime under the frozen same-coefficient rule. It does not apply to listing two spectra, inventing MB, or claiming priority clearance. The enzymatic full-text gap still applies. |
| C1-N6 | Rigorous Hopf theorem / P11–P13 | SUPPORTING SPECIALIZATION | The Hopf theorem is known. A verified, realizable first symmetry-breaking crossing on a positive branch is necessary model-specific support; the stronger regime classification may contribute through items 3 and 5. |
| C1-N7 | First Lyapunov coefficient reduction / P13 | SUPPORTING SPECIALIZATION | Fourier contraction and elimination of inverse matrices are already explicit in van Kekem–Sterk §4.3; cubic-term formulas also have precedents in Pais et al. Appendix D. The exact DM expression must still be derived. |
| C1-N8 | Sign/criticality result for l1 / P13 | UNRESOLVED | No parameter region or sign theorem has yet been established. An analytic nonempty-region result that explains a DM–MB contrast is the intended target. A zero alone would not prove generalized Hopf. |
| C1-N9 | Rotating-wave conclusion / P14 | SUPPORTING SPECIALIZATION | The symmetry mechanism is established. State exact spatiotemporal symmetry, isotropy and phase orientation for the verified branch; do not claim the general rotating-wave principle as new. |

These are overlays, not nine newly proved theorems. The bare q=2 rule is a routine adaptation; the strengthened target is structurally analogous but model-specific. The comparison's rating applies only to a nonempty admissible qualitative contrast. No exact-model novelty assertion is released. P15–P18 are postponed; their existing claims and proof fragments remain intact. The archive's numerical crossing C073 remains unreproduced.

The new source facts (2024 supplement Sections S2–S5; Lin 2021 thesis catalogue entry; Xiong–Zhang 2025 references 4/5/7) are literature-dependent audit observations, not mathematical claims about DM. The source's limiting equations are transcribed in 05 without importing their conclusions as proofs of our claims.

## P01 draft overlay — 2026-09-27

Current mathematical status: **P01 DRAFT; P02–P18 TODO**. This supersedes historical all-TODO wording for P01 only. The current C020–C024 rows identify the independently developed draft arguments. Their archival locators are retained for provenance, not used as proof. No claim is VERIFIED or AUDITED and no numerical claim is changed.

| Draft ID | Classification | Precise foundation claim | Owner / location | Status |
|---|---|---|---|---|
| P01-D1 | proposed theorem | Initially positive coordinates persist; c>0 makes any nonzero nonnegative state strictly positive at every positive time via step one, regardless of q or gcd. | P01, prop:P01-positive | VERIFIED / AUDITED; A01 E01 closed; EXTENDED VERIFIED AFTER MINOR REVISION |
| P01-D2 | proposed theorem | For R>0, distance to K_R decays at least as e^(-kRt) times its initial distance; reciprocal bounds give uniform attraction over the entire orthant and explicit common entry times into every larger cube. | P01, thm:P01-global | VERIFIED / AUDITED; A01 E01 closed; EXTENDED VERIFIED AFTER MINOR REVISION |
| P01-D3 | proposed theorem | In the weak domain n>=1, arbitrary residue q, real a, k>0, c,g,h>=0: R>0 iff a+c>0. For R>0, exact-radius absorption holds iff g>0 or [h>0 and (c>0 or q=0 modulo n)]. R=0 is attracting but never absorbs an initially nonzero trajectory in finite time. | P01, lem:P01-bound; thm:P01-absorption | VERIFIED / AUDITED; A01 E01 closed; EXTENDED VERIFIED AFTER MINOR REVISION |
| P01-D4 | proposed theorem | k>=0 suffices for nonnegative global existence with nonnegative c,g,h; a common bounded region is not guaranteed in the full k=0 class. | P01, prop:P01-kzero | VERIFIED / AUDITED; A01 E01 closed; EXTENDED VERIFIED AFTER MINOR REVISION |

The module's “Checks and possible failure points” records symbolic sign/root checks, parameter-edge counterexamples, and the distinction among invariance, attraction, absorption and stability of a set. A separate independent audit must examine the written proofs; the internal check does not promote their status. No mathematical work on P02–P18, the comparator, modes, bifurcations or numerics is included.

## P01 audit closure — 2026-09-27

**P01 VERIFIED / AUDITED; CORE VERIFIED; EXTENDED VERIFIED AFTER MINOR REVISION.** This supersedes the historical draft-status prose above. C020–C024 and P01-D1–P01-D4 now point to completed, audited P01 results; their archival classifications, statements and locators are preserved. No other claim status is promoted, and P02–P18 remain TODO.

A01's sole required correction E01 replaces `is the nonnegative root of $as-ks^2+c=0$.` with `is the larger real root of $as-ks^2+c=0$, and is nonnegative.` When c=0 and a>0, the quadratic has two nonnegative roots; B selects the larger one. No displayed formula, assumption, inequality, conclusion or proof changes. All other body text, including its historical DRAFT-status sentence, is retained; the revised header gives current status.

Evidence: [audits/A01_wellposedness_and_absorbing_box.tex](audits/A01_wellposedness_and_absorbing_box.tex), E01 at audited source line 428; closure version `P01 v1.1`. Corrected full-file SHA-256: `0d6950821aa83f3d09e8bfe84dab2b0b5020aa6e7881cf6928e984bff1890f1e`. The exact change, hash scope and preservation checks are recorded in the manifest's P01 audit-closure revision log.

## P02 draft overlay — 2026-09-27

**P01 remains VERIFIED / AUDITED; P02 is DRAFT; P03–P18 remain TODO.** The current C025, C026, C028–C033 and C146 status cells supersede their earlier unproved archival status only to the extent explicitly marked DRAFT. The archived claim text and source locators are preserved. No later module, literature claim, or numerical claim is promoted.

| Draft ID | Precise additional P02 claim | Owner / location | Status |
|---|---|---|---|
| P02-D1 | Whenever D>=0, s_+>-1/2 and s_->-1 iff g>c; g=c gives the excluded polynomial root -1. | P02, eq:P02-domain-test | VERIFIED / AUDITED; A02 E01 closed |
| P02-D2 | At mu<0, a<A and D>=0 the real nonzero roots are negative but domain-admissible; at D=0 the negative double root lies in (-1/2,0). | P02, thm:P02-complete, cases X–XI | VERIFIED / AUDITED; A02 E01 closed |
| P02-D3 | The algebraic nonzero-branch continuation meets the origin iff mu=0; the scalar origin has order two for mu=0 and a!=A, and order three at mu=0 and a=A. | P02, thm:P02-complete; prop:P02-loci | VERIFIED / AUDITED; A02 E01 closed |
| P02-D4 | The positive-root alternatives hold for A>0 and real a,c,g, but the full negative-root/domain table is restricted to canonical positive parameters. | P02, weaker-assumption subsection | VERIFIED / AUDITED; A02 E01 closed |

The original scalar residuals, Vieta identities, all eleven cells and equality boundaries, and the four positive-count equivalences were checked internally with exact arithmetic. Those checks and a successful compilation do not constitute an independent mathematical audit. The manifest records the current validation and preservation results.

## P02 audit closure — 2026-09-27

**P02 VERIFIED / AUDITED, version v1.1.** Original A02 verdict: **CORE MINOR REVISION; EXTENDED VERIFIED**. Sole issue **E01 corrected** by explicitly naming `(s_-,s_+)` in the boundary-continuity limits. Closure: **CORE VERIFIED AFTER MINOR REVISION; EXTENDED VERIFIED**. C025, C026, C028–C033, C146's rejection/replacement classification, and P02-D1–D4 now carry the audited status. Their mathematical and archival claim text is unchanged. The dated DRAFT overlay above is historical; no P03–P18 claim is promoted.

Audit file: `audits/A02_synchronous_subspace_and_equilibria.tex`; the source was not supplied. The actual evidence included is [A02 PDF](audits/A02_synchronous_subspace_and_equilibria.pdf). A02 remains tied to the audited v1.0 hash. The manifest records the sole correction and preserved mathematical environments. Corrected P02 full-file SHA-256: `8e057c2cd009659eee45906844e25f4f38c156e5eb2e4130e824aa5e8299c51a`; body SHA-256: `8a061ba81c7ffd2d05b188b9fca4ec1b94bc132147f7f664c8523f0a5f32560c`. P01 and all P03–P18 proof files remain unchanged.

## P03 draft overlay — 2026-09-27

**P01 and P02 remain VERIFIED / AUDITED; P03 is DRAFT; P04–P18 remain TODO.** Only the P03-owned C034, C035 and C037 status cells are updated. Archival claim text, classifications and locators are preserved. No independent A03 audit is claimed; the internal derivation review, symbolic checks, finite differences and compilation do not promote status.

| Draft ID | Precise P03 statement | Location | Status |
|---|---|---|---|
| P03-D1 | General Jacobian entries are a sum of modular Kronecker contributions, including all rational derivatives and collision cases. | lem:P03-jacobian; eq:P03-variable-matrix | VERIFIED / AUDITED; A03 VERIFIED; no correction required; v1.1 metadata-only closure |
| P03-D2 | Full origin nonhyperbolicity iff g=a+c cos(2 pi m/n)>0 for some m; it can coexist with linear instability. The mu=0 boundary has exactly one simple zero, in mode zero. | prop:P03-stability; prop:P03-boundary | VERIFIED / AUDITED; A03 VERIFIED; no correction required; v1.1 metadata-only closure |
| P03-D3 | A nonzero-mode zero away from mu=0 is possible iff n is even, m=n/2 and g=a-c>0; it is simple and mu=2c>0. | rem:P03-other-zero | VERIFIED / AUDITED; A03 VERIFIED; no correction required; v1.1 metadata-only closure |
| P03-D4 | All synchronous-state matrices are circulant; the exhaustive canonical collisions yield C-H, C+G, and G-H at the indicated combined shifts. | homogeneous proposition and collision subsection | VERIFIED / AUDITED; A03 VERIFIED; no correction required; v1.1 metadata-only closure |

The earlier A02 source-unavailability record is historical: its original TeX was located in the companion audit package, authenticated against the audit delivery hashes and matching PDF, and restored byte-for-byte. A02 remains an audit of P02 v1.0; P02 v1.1 and its closed E01 correction are unchanged. The manifest records source selection, checks, build diagnostics and protected-file preservation. P04's full positive-state spectrum/normality, C036/P09 nonlinear boundary behavior, and all later mathematical work remain deferred.

## P03 audit closure — 2026-09-27

**P03 VERIFIED / AUDITED; A03 verdict VERIFIED; no required correction.** Audited P03 v1.0 full-file SHA-256: `0f87f315817429ddb949af5bc6d38db32a0cb6a8f7715dfe941840becd527776`. Current P03 v1.1 full-file SHA-256: `6c3c9bfb2307bdc043eb7f6a874cb222e2ac2ce0750b339181f0088dd0bd859e`. The sole P03 changes are comment metadata; the complete body, including historical status prose, is byte-identical. Its unchanged body SHA-256 is `07d76c8ce0b5232827e9f2c74245188b55b0ce0d1732b3cb2e528d69e8d6b50a`, measured from the first section command through EOF.

Audit evidence: [A03](audits/A03_origin_and_linearization.tex), with the supplied PDF and support directory preserved verbatim. C034, C035, C037 and P03-D1–P03-D4 are now VERIFIED / AUDITED; their mathematical statements, archival classifications and locators remain unchanged. Earlier DRAFT/audit-pending overlays are historical. No optional wording change is applied, and no numerical or literature claim is newly promoted. P01/P02 remain audited and untouched. P04–P18 remain TODO; P04 is not begun. Compilation is not mathematical verification. Full provenance, hash scope and closure checks are recorded in the project manifest.

## P04 draft overlay — 2026-09-27

**P01–P03 remain VERIFIED / AUDITED; P04 v1.0 is DRAFT; P05–P18 remain TODO.** This entry and the current status cells supersede historical P04-placeholder wording. Only P04-owned C008, C011, C038–C041 and C153 status cells are revised. All archival classifications, statements, locators and owners are preserved. The Phase 1C KNOWN / ROUTINE novelty classification is unchanged. No independent A04 audit is claimed.

| Draft ID | Precise P04 statement | Location | Status |
|---|---|---|---|
| P04-D1 | Every numerical eigenvalue has equal algebraic and geometric multiplicities, each equal to its number of Fourier labels; nonsingleton pairs can share real eigenvalues. | prop:P04-multiplicity | VERIFIED / AUDITED; A04 VERIFIED; no correction required; v1.1 metadata-only closure; U01 nonblocking |
| P04-D2 | At every synchronous state x*>-1, lambda_0=f′(x*); at a nonzero equilibrium lambda_0=-x*[(k+h)+(c-g)/(1+x*)^2]=x*/(1+x*)[a-(k+h)-2(k+h)x*]. | eq:P04-synchronous-derivative; eq:P04-equilibrium-zero-mode | VERIFIED / AUDITED; A04 VERIFIED; no correction required; v1.1 metadata-only closure; U01 nonblocking |
| P04-D3 | At a synchronous equilibrium, linear exponential stability iff sa(J)<0, with exact Euclidean propagator norm exp(t sa(J)) for t>=0. | cor:P04-stability; eq:P04-semigroup | VERIFIED / AUDITED; A04 VERIFIED; no correction required; v1.1 metadata-only closure; U01 nonblocking |
| P04-D4 | Hyperbolicity iff every r_m is nonzero; a nonzero imaginary eigenvalue still violates hyperbolicity. Nonlinear conclusions are local and zero abscissa is generally inconclusive. | prop:P04-hyperbolicity; nonlinear implications paragraph | VERIFIED / AUDITED; A04 VERIFIED; no correction required; v1.1 metadata-only closure; U01 nonblocking |
| P04-D5 | Fixed-point dominant labels retain every tie; first loss of stability additionally needs branch, oriented path, prior stability and a crossing event. | Dominant modes and first loss of stability paragraph | VERIFIED / AUDITED; A04 VERIFIED; no correction required; v1.1 metadata-only closure; U01 nonblocking |

The norm identity is explicitly requested local support in P04. C042 retains its P17 owner and TODO status; no P17 response analysis is performed or promoted. P01–P03, P05–P18, canonical and literature files, and all supplied audits remain byte-identical. Internal symbolic/numerical checks and compilation do not verify the theorem. Details and provenance are recorded in the manifest.

## P04 audit closure — 2026-09-27

**P04 VERIFIED / AUDITED; A04 mathematical verdict VERIFIED; no required mathematical or wording correction.** Audited P04 v1.0 full-file SHA-256: `ab80f695b3e20c852c572b7b174ecaf9964eac1aba62e3e55b2b4d3e60754e0c`. Current P04 v1.1 full-file SHA-256: `1331c8598acd0481046250d918cac028ca6d13d2604612448c3459e864321c58`. The sole P04 changes are comment metadata; its complete mathematical body, including historical DRAFT/audit-pending prose and computational statistics, is byte-identical. Unchanged body SHA-256: `3e3d58230c87af3b5f07069d61065362dc081d172ad3b236057fefda25fa5653`, measured from the first line-anchored section command through EOF.

Audit evidence: [A04](audits/A04_arbitrary_nq_fourier_spectrum.tex), its reading PDF and all supplied support files are included unchanged. C008, C011, C038–C041, C153 and P04-D1–P04-D5 now record the audited P04 results. Archival statements, classifications, locators and owners are unchanged; the blanket C040/C153 assertions remain rejected, while their precise replacements are audited. C042 retains its P17 owner and TODO status. No optional wording change is applied.

**Nonblocking reproducibility note (A04 U01):** the original P04 validation companion was unavailable to the independent auditor. The historical numerical-check counts and floating-point error statistics in audited P04 v1.0 lines 530–545 were therefore not independently reproduced. A04’s newly supplied exact checks are separate corroboration, not reproduction of that historical run. No theorem depends on those statistics; A04’s mathematical verdict remains VERIFIED. This administrative closure does not resolve or rerun the historical computation.

Current status: P01–P04 VERIFIED / AUDITED; P05–P18 TODO. Earlier DRAFT/audit-pending overlays are historical. P01–P03 and all P05–P18 files are untouched; P04 body is unchanged. No P05 mathematics or new literature work was begun. Compilation is not mathematical verification. The manifest records exact provenance, preservation and build checks.

## P05 strengthened draft — 2026-10-02

**Current status: P01–P04 VERIFIED / AUDITED; P05 v1.0 DRAFT; P06–P18 TODO.** Historical earlier status prose is retained. C045–C048 status cells alone are updated among the archival C-rows; their classifications, statements, locators and owners are unchanged. The following precise draft claims supplement that archive. An independent A05 audit remains required.

| ID | Classification | Precise draft claim | Evidence / scope | Owner | Status |
|---|---|---|---|---|---|
| P05-D1 | proposed theorem | Complete fixed-equilibrium selection for every C>0 and T=G-H, with all endpoint regimes, nearest-cosine cells and adjacent maximal ties | thm:P05-selection; eq:P05-regions; counts refer to Fourier labels | P05 | VERIFIED / AUDITED AFTER MINOR REVISION; P05 v1.1, A05 E01 closed; U01 nonblocking |
| P05-D2 | proposed theorem | Reachable representatives are exactly 0 through floor((n+1)/4); negative-cosine selection occurs exactly at the terminal representative when n=3 mod 4; even Nyquist singleton excluded | thm:P05-reachable; finite-parameter limit distinguished from the formal zero-vertex tie for n=2 mod 4 | P05 | VERIFIED / AUDITED AFTER MINOR REVISION; P05 v1.1, A05 E01 closed; U01 nonblocking |
| P05-D3 | proposed theorem | Every retained strict cell and positive-midpoint switch is realized by positive canonical parameters satisfying the original DM equilibrium equation | thm:P05-realization; eq:P05-construction; explicit examples | P05 | VERIFIED / AUDITED AFTER MINOR REVISION; P05 v1.1, A05 E01 closed; U01 nonblocking |
| P05-D4 | proposed theorem | Every strict cell contains a nonempty open physical-parameter realization on a specified positive branch; each positive-midpoint switch is a local smooth codimension-one hypersurface at every such branch point | eq:P05-chart-determinant and eq:P05-level-set; no global branch-identification claim | P05 | VERIFIED / AUDITED AFTER MINOR REVISION; P05 v1.1, A05 E01 closed; U01 nonblocking |
| P05-D5 | proposed theorem | Every reachable dominance switch admits a strictly stable canonical branch path; selection does not imply a first instability or a Hopf event | eq:P05-stable-switch; first crossing, frequency and simplicity remain P11/P12 tasks | P05 | VERIFIED / AUDITED AFTER MINOR REVISION; P05 v1.1, A05 E01 closed; U01 nonblocking |

P05 is an intended MAIN THEOREM TARGET only in this strengthened realizability form. The frozen Phase 1B/1C novelty verdict and theorem package are unchanged; no amendment is needed. Priority is not declared closed. No P07, P08 or P11 work is begun; no later theorem is promoted. Computations and compilation are corroboration only, not verification or independent audit.

## P05 audit closure — 2026-10-02

**P05 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION.** The immutable `audits/A05_q2_mode_selection.tex` audits exact P05 v1.0 with original CORE MINOR REVISION, REALIZABILITY VERIFIED and OVERALL MINOR REVISION. Its sole required correction E01 now states that maximization considers all Fourier labels, including mode zero; the selected set consists of actual maximizers, retaining all ties. The remaining P05 mathematical body is unchanged. Exact original/corrected hashes and wording are recorded in the project manifest.

Only C045–C048 and P05-D1–P05-D5 status cells are updated. Every existing claim classification, statement, locator and owner is preserved. Historical DRAFT-status sections describe the pre-audit version and are superseded by this closure. The frozen strengthened theorem role and novelty verdict are unchanged; no priority claim is added. A05 U01 remains a nonblocking historical validation-provenance note, not an unresolved mathematical issue; no historical checker is rerun.

P08 is now cleared to begin under the existing frozen scope, but remains TODO / NOT STARTED. P06–P18 proof files and all their claim statuses remain unchanged. No subsequent module, continuation or literature task is begun. Compilation does not supply the independent audit; A05 does.

## P08 current DRAFT claim overlay — 2026-10-03

P08 v1.0 is DRAFT, not VERIFIED or AUDITED. P01–P05 closure statuses and all earlier nonstatus claim cells are unchanged. The same positive coefficient tuple, same n,q and time variable are compared at each law's own specified positive synchronous equilibrium. No biological calibration or priority claim is made.

| ID | Status | Exact DRAFT scope and proof anchors |
|---|---|---|
| P08-D1 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | MB local flow, invariant faces, scalar equilibria, sufficient global/dissipative bounds and synchronous growth/blow-up; thm:P08-foundation, prop:P08-bounds, cor:P08-stability. |
| P08-D2 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | Arbitrary-(n,q) MB Jacobian, full spectrum, normality, exact stability, all collisions, lambda_0=-a in two ways; thm:P08-spectrum. |
| P08-D3 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | Exact q=2 cells, ties, parity, finite endpoints, reachable labels and MB canonical realization; thm:P08-selection. |
| P08-D4 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | Common domain and branch convention; curvature, face, uniform-mode and structural dissipativity contrasts; prop:P08-structural. |
| P08-D5 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | Every ordered reachable mode pair has a nonempty open common realization with both models stable; thm:P08-pair-realization, prop:P08-open. |
| P08-D6 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | For every n>=5,q=2 an open C_+ region has DM stable/uniform and MB unstable/nonuniform, witnessed by (1/4,1/8,1,1,1/8); thm:P08-forward. |
| P08-D7 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | On C_+, reverse stability exists exactly for n=3 mod 4; analytic family and rational n=7 certificate; thm:P08-reverse. |
| P08-D8 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | On the full branch-labelled domain, reverse stability is impossible for 4 dividing n; otherwise an explicitly fixed lower DM branch realizes it openly; prop:P08-lower. |
| P08-D9 | VERIFIED / AUDITED AFTER MINOR REVISION; P08 v1.1, A08 E01 closed | All five requested types of stability/mode combination have constructive realizations; n=8 both-unstable different-mode witness; eq:P08-both-unstable, prop:P08-open. |

C064 (MB Hopf) and C065 (six-term analysis) remain deferred/unverified; their existing rows are unchanged. No later-module claim is promoted. All computational checks are separate corroboration, not proof premises or independent audit. The frozen theorem package already allows these results and is unchanged. The hoped-for unrestricted reverse stability contrast fails with the exact size/branch obstructions now recorded; this does not require altering the frozen target.

## P08 audit closure — 2026-10-03 (CURRENT)

**P08 v1.1 is VERIFIED / AUDITED AFTER MINOR REVISION.** The immutable `audits/A08_matched_bilinear_analysis.tex` audits P08 v1.0: MB FOUNDATION VERIFIED; MB SPECTRAL VERIFIED; SAME-TUPLE COMPARISON MINOR REVISION; PARITY/OBSTRUCTION VERIFIED; OVERALL MINOR REVISION. Its sole issue E01 is closed by the exact requested sentence replacement: the universal witness selects MB representative 1 for n=5,6,7 and representative 2 for n=8 (Fourier labels {2,6}). All theorem statements, proofs, tuples, formulas, stability inequalities and all-n claims are unchanged. Exact original/corrected hashes are recorded in the manifest.

Only C053–C063, C145, and P08-D1–P08-D9 status cells change. C145's rejected blanket claim remains rejected. C064/C065 remain deferred/unverified, and no later claim is promoted. Every existing nonstatus cell is preserved. Historical DRAFT sections are superseded by this closure, not rewritten.

A08 authenticated and exactly reproduced the original P08 validation summaries/results; its evidence is preserved unchanged. No validation rerun was performed for closure. Compilation is not mathematical verification; A08 supplies the independent audit. Earlier A04/A05 provenance notes, frozen scope and novelty verdicts are unchanged.

P07 is cleared to begin under the frozen attempt order, but remains TODO / NOT STARTED. P06–P07 and P09–P18 proof bodies/placeholders are untouched. This closure performs no subsequent proof, continuation or literature work.

## P07 completed draft — 2026-10-03 (historical; superseded by closure below)

**P07 v1.0 is DRAFT; independent A07 audit pending.** This supersedes earlier scheduling prose that P07 has not begun. P01–P05 and P08 remain audited; P06 and P09–P18 remain TODO. Only archival C051, C052 and C155 status cells change; every archival classification, statement, locator and owner is preserved. C155's physiological assertion remains rejected. No later claim is promoted.

| ID | Status | Exact scoped claim and evidence |
|---|---|---|
| P07-D1 | VERIFIED / AUDITED; A07 VERIFIED; P07 v1.1 metadata only; no correction required | Exact fifth-root radicals, normalized sine, and all five signed DM eigenvalues for n=5,q=2; lem:P07-trig, thm:P07-spectrum. |
| P07-D2 | VERIFIED / AUDITED; A07 VERIFIED; P07 v1.1 metadata only; no correction required | Exhaustive seven-row ordering with three factored gaps; only uniform/pair-1 can dominate, switch H-G=C/phi^2, other two equalities subdominant; thm:P07-ordering, cor:P07-selection. |
| P07-D3 | VERIFIED / AUDITED; A07 VERIFIED; P07 v1.1 metadata only; no correction required | P05 midpoint/chi specialization including H<=G; exact canonical switch constrained by the positive equilibrium; every ordering row canonically realizable; eq:P07-midpoints, eq:P07-chi, eq:P07-canonical-switch, eq:P07-realization. |
| P07-D4 | VERIFIED / AUDITED; A07 VERIFIED; P07 v1.1 metadata only; no correction required | omega_1=sigma(S-phi C), omega_2=-sigma(C+phi S)<0; real pair-1 degeneracy exactly at S=phi C; positive switch intersection G/C=1/phi,H/C=1 with independent codimension-two spectral constraints and a strictly negative semisimple triple value; prop:P07-frequency, prop:P07-intersection. |
| P07-D5 | VERIFIED / AUDITED; A07 VERIFIED; P07 v1.1 metadata only; no correction required | Exhaustive numerical coincidence classification: only pair-1 real double value or its triple intersection with mode 0; no cross-pair equality, pair 2 always simple/nonreal, pair-1 nonreal eigenvalues simple; prop:P07-coincidences. |
| P07-D6 | VERIFIED / AUDITED; A07 VERIFIED; P07 v1.1 metadata only; no correction required | Piecewise strict Hurwitz test; whole dominant tie strictly stable; pair 2 never controls a zero-abscissa state; fixed-state critical-mode ledger with no first-instability or Hopf conclusion; cor:P07-stability, prop:P07-ledger. |

P07 retains P05 as its direct prerequisite, using audited P03/P04 and the P01/P02 foundation transitively. P08 provides no theorem input. Golden-ratio expressions remain supporting network geometry, not standalone novelty. Exact and numerical checks plus compilation are corroboration only; frozen scope and novelty documents are unchanged.

## P07 audit closure — 2026-10-03 (CURRENT)

**P07 v1.1 is VERIFIED / AUDITED.** The immutable `audits/A07_five_node_specialization.tex` verifies exact P07 v1.0 in all five layers (Fourier/trigonometry, ordering/selection, frequency/coincidence, stability/critical-mode, scope/dependency) and overall. **Required corrections: NONE.** Only header metadata changes; every mathematical-body byte, including historical DRAFT wording, is preserved. Original and current full-file hashes and the unchanged body hash are recorded in the manifest.

Only C051/C052/C155 status cells and P07-D1–D6 status cells change; all claim statements, classifications, locators and owners remain unchanged. C155's physiological assertion stays rejected. Earlier P01–P05/P08 claims retain their statuses and content. No later claim is promoted.

A07 authenticated and reproduced the original developer validation: 161 exact checks, 108 numerical cases, and byte-identical summary and result files. Its evidence is preserved unchanged; no suite is rerun for closure. Validation and compilation remain corroboration rather than proof; A07 provides independent mathematical verification.

The direct dependency remains **P05 -> P07**; P03/P04 and P01/P02 are inherited. No P08 theorem is imported. Frozen theorem, novelty and canonical documents remain unchanged. **P09 is cleared to begin but remains TODO / NOT STARTED.** No subsequent proof, numerical continuation or literature work is performed.

## P09 local origin bifurcation draft — 2026-10-03 (CURRENT)

**P09 v1.0 is DRAFT, not VERIFIED; independent A09 audit pending.** This supersedes historical P09 not-started wording. The 170 archival C-rows retain every nonstatus cell. Only C036/C067/C068/C069 status cells change. Prior audited claim rows are unchanged. C069's two-parameter unfolding remains excluded.

| ID | Current status | Precise draft claim and proof anchor |
|---|---|---|
| P09-D1 | VERIFIED / AUDITED; A09 VERIFIED; P09 v1.1 metadata only; no corrections | Simple synchronous zero, explicit transverse gap, and transverse IFT showing every nearby full equilibrium is synchronous for every b; lem:P09-gap, thm:P09-reduction. |
| P09-D2 | VERIFIED / AUDITED; A09 VERIFIED; P09 v1.1 metadata only; no corrections | Full-vector coefficients 1 in mu, -1 in g and 2b in the quadratic tensor contraction; prop:P09-coefficients. |
| P09-D3 | VERIFIED / AUDITED; A09 VERIFIED; P09 v1.1 metadata only; no corrections | Generic full-system transcritical theorem, unique nonzero local branch, slopes and exact orbital center reduction; thm:P09-transcritical. |
| P09-D4 | VERIFIED / AUDITED; A09 VERIFIED; P09 v1.1 metadata only; no corrections | Exact uniform sign, strictly stable transverse spectrum, full stability exchange and physical positive-branch sides; eq:P09-uniform-nonzero, eq:P09-persistent-gap, cor:P09-physical. |
| P09-D5 | VERIFIED / AUDITED; A09 VERIFIED; P09 v1.1 metadata only; no corrections | Generic critical origin is unstable in U; orthant interpretation is explicitly limited; prop:P09-generic-critical. |
| P09-D6 | VERIFIED / AUDITED; A09 VERIFIED; P09 v1.1 metadata only; no corrections | Cubic-degenerate square-root geometry, full stability of both nonzero branches, full critical asymptotic but nonexponential stability, with independent Lyapunov proof; prop:P09-degenerate. |
| P09-D7 | VERIFIED / AUDITED; A09 VERIFIED; P09 v1.1 metadata only; no corrections | Independent codimension-two parameter constraints and algebraic meeting with P02 repeated-root locus at root zero; no unfolding or named codimension-two bifurcation; prop:P09-codimension. |

Dependencies remain P02/P03/P04 with P01 inherited. No P05/P07/P08 theorem is used. Frozen scope/novelty documents are unchanged. P06 and P10–P18 remain TODO; P10 is not begun. Computational corroboration is recorded separately and gives no mathematical promotion.

## P09 audit closure — 2026-10-03 (CURRENT)

**P09 v1.1 is VERIFIED / AUDITED.** The immutable `audits/A09_transcritical_bifurcation.tex` verifies exact P09 v1.0 in all six layers and overall, with **no corrections**. Closure modifies header metadata only; the entire audited mathematical body remains byte-identical. The current header and manifest supersede historical DRAFT/audit-pending prose, which is intentionally retained.

All 170 archival C-rows retain classification, claim, locator and owner. Only the status cells of C036/C067/C068/C069 and P09-D1–D7 are promoted. C069's proposed two-parameter unfolding remains EXCLUDED / UNPROVED. All earlier audited claim rows remain unchanged; no later claim is promoted.

A09 authenticated and reproduced the original validation outputs byte-for-byte (1,260 exact, 2,700 matrix, 12 slope checks); closure preserves and authenticates that evidence without rerunning it. A09's independent mathematical reconstruction supplies verification. Compilation and computational checks remain corroboration.

The theorem edges remain **P02/P03/P04 -> P09**, with inherited **P01**; no P05/P07/P08 or later theorem dependency is introduced. Frozen scope and novelty records are unchanged. **P10 is cleared to begin but remains TODO / NOT STARTED.** No subsequent proof, continuation or literature work is performed.

## P10 positive-fold DRAFT claim overlay — 2026-10-03 (CURRENT)

**P10 v1.0 DRAFT, independent A10 audit pending.** Only C070/C071/C147 status cells change among the 170 archival claims; their statements, classes, locators and owners are preserved. Prior verified claims are unchanged. This overlay supersedes historical P10-TODO wording.

| ID | Draft result | Proof location | Status |
|---|---|---|---|
| P10-D1 | Exact positive fold, square completion and P02 branch reconciliation | eq:P10-data; eq:P10-exact-fold | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D2 | Positive effective fold coefficient; exact full spectrum, strict transverse gap and simple zero | lem:P10-gap | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D3 | Full-system local equilibrium completeness by the real transverse IFT | prop:P10-reduction | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D4 | Original-vector saddle-node coefficients and exact center normal form | prop:P10-coefficients; thm:P10-saddle-node | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D5 | Exact uniform branch signs; full near-fold sink/index-one-saddle classification | prop:P10-branch-signs; cor:P10-near-stability | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D6 | Nonempty open stable coexistence; exact full-spectrum set and sufficient physical inequality | thm:P10-bistability; prop:P10-bistability-set; eq:P10-explicit-margin | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D7 | Exact obstruction to universal upper stability on the whole two-root interval | rem:P10-counterexample | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D8 | Synchronous-ray threshold and exact local unstable synchrony | prop:P10-ray; prop:P10-local-basins | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D9 | Local stable disk and rigorously proved local basin sides; no global partition | prop:P10-local-basins | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |
| P10-D10 | P09 branch connection and degenerate limit; strictly limited later inputs | eq:P10-transcritical-connection; eq:P10-degenerate-limit | VERIFIED / AUDITED (P10 v1.1; A10, no correction) |

Dependencies remain P02/P03/P04/P09 with P01 inherited. No P05/P07/P08 theorem is used. B03 is scoped to coexistence and the explicitly proved local basin statement, not exactly two global attractors. Frozen role S4 and all novelty verdicts remain unchanged. P06 and P11–P18 are untouched; no later bifurcation theorem, continuation or literature work is performed. Computational corroboration is separate and supplies no audit promotion.

## P10 audit closure — 2026-10-03 (CURRENT)

**P10 v1.1 is VERIFIED / AUDITED.** The immutable `audits/A10_saddle_node_and_bistability.tex` verifies exact P10 v1.0 in all six layers (fold geometry/spectrum; full-system saddle-node; branch stability/bistability; coexistence set/counterexample; basin/manifold; scope/dependency) and overall. **Required corrections: NONE.** There is no AFTER MINOR REVISION qualifier. Closure changes only header metadata; the full audited mathematical body is byte-identical. Its retained historical DRAFT/audit-pending text is superseded by the current header and manifest.

Only C070/C071/C147 and P10-D1–D10 status cells are promoted. Every archival classification, statement, locator and owner remains unchanged; all other existing claim rows are unchanged. C147 remains a verified refutation of universal upper/origin stable coexistence throughout the two-root interval, with no conclusion about other attractors. The exact counterexample and lower unstable dimension three are preserved.

A10's independent analytical reconstruction supplies verification. A10 authenticated/inventoried the original developer validation package but did not rerun it or reproduce its historical statistics. A10's independent finite checks are separate corroboration. Both original validation provenance and all immutable A10 evidence are preserved without rerunning either checker for this closure.

Dependencies remain **P02/P03/P04/P09 -> P10**, with **P01 inherited**. P05/P07/P08 are not theorem inputs. Basin statements retain their exact scope: synchronous-ray threshold, local full-space two-basin stable disk relative to V, no complete global basin boundary or whole-orthant partition, and no exactly-two-attractor claim. Frozen scope/novelty and all prior proof/audit bodies remain unchanged. **P11 is cleared to begin but remains TODO / NOT STARTED.** No later proof, continuation or literature work is performed.

## P11 spectral candidate draft — 2026-10-03 (CURRENT)

P11 v1.0 is **DRAFT / NOT AUDITED**. C072 and C074 are covered only to the exact spectral scope above. C073's archived numerical observation remains unchanged and unreproduced. All P01–P05/P07–P10 closures remain in force. P06 and P12–P18 are unchanged and unstarted by this task.

| ID | Result | Exact evidence | Status |
|---|---|---|---|
| P11-D1 | Reachable nonuniform representatives are genuine pairs; signed frequency and exact zero locus | lem:P11-pairs; prop:P11-frequency | DRAFT / A11 pending |
| P11-D2 | One simple imaginary conjugate pair, stable complement, exact positive gap and inverse gates | thm:P11-strict; rem:P11-degeneracies | DRAFT / A11 pending |
| P11-D3 | Orthonormal real critical basis, signed real block and normalized Hermitian adjoint | prop:P11-vectors | DRAFT / A11 pending |
| P11-D4 | Regular branch-state spectral surface; local physical chart transfer and conditional rank-two zero-frequency locus | prop:P11-surface | DRAFT / A11 pending |
| P11-D5 | Necessary-and-sufficient physical candidate realizability test for each strict reachable nonuniform cell; exact obstructions | prop:P11-realizability | DRAFT / A11 pending |
| P11-D6 | Exact positive five-node tuple, original-field residual, complete complex spectrum, gap and upper-root identity | thm:P11-five | DRAFT / A11 pending |
| P11-D7 | Smooth local upper branch, frozen g-path, exact Fourier/adjoint vectors and resolvent denominators | prop:P11-data | DRAFT / A11 pending |
| P11-D8 | H1–H9 spectral handoff and H10–H12 explicitly unestablished later conclusions | prop:P11-ledger | DRAFT / A11 pending |

Direct dependencies remain **P02/P04/P05 -> P11**, with conditional P07 input for n=5 and P03 inherited through P04. P08/P09/P10 are not mathematical premises. The partial derivative with respect to k in branch coordinates is not a fixed-physical-parameter crossing derivative. No equilibrium derivative along g, spectral transversality, tensor, first Lyapunov coefficient, nonlinear Hopf theorem or periodic orbit is established. B02 is fixed for this draft to the local upper branch and pi(g)=(a_H,k_H,2,g,6); spectral certification is exact algebra, not numerical evidence. B07's remaining nonlinear normalization choices stay with P13.

The optional universal cell-existence assertion is false: (n,j)=(8,1) and (12,2) are exact obstructions, while the proved cell criterion is complete within its stated branch-state scope. This does not contradict P05 dominance realizability. `PROPOSED_P11_scope_clarification.md` records older first-crossing planning language as a proposed amendment only; all frozen files and novelty ratings remain unchanged. Independent A11 audit is required before any status promotion.
