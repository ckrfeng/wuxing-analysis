# Phase 1B novelty decisions

Audit date: 2026-09-24. These are research-planning recommendations, not verified mathematical statements or authorization to begin proofs. The canonical models, original Phase 1 audit, and P01–P18 fragments are preserved. Every proof module remains TODO. “Move to supplement” describes a proposed manuscript role; no file is moved. Source identifiers and exact locations are in [04_adversarial_novelty_audit.tex](04_adversarial_novelty_audit.tex).

The strongest surviving **candidate** is a model-specific classification linking realizable q=2 wave selection and first Hopf criticality to a qualitative DM–MB contrast. It is unproved and its coupling-law priority is unresolved. No original target receives GREEN. The weakest principal novelty claim is arbitrary-(n,q) Fourier diagonalization; the inverse Fourier Green function is similarly standard. The most dangerous program overlap is van Kekem–Sterk’s Lorenz–96 analysis (S03); the largest unresolved model-priority risk is the Lin–Shi–Han enzymatic sequence (S13–S16).

## One disposition for every proof module

| Module | Decision | Reason and proposed role | Gate before completion |
|---|---|---|---|
| P01 — well-posedness and absorbing region | NOVELTY IRRELEVANT BUT NEEDED TECHNICALLY | Necessary model foundation; standard ODE/comparison methods are not the principal contribution. | Resolve B01 wording; prove the actual domain and attraction/absorption statement later. |
| P02 — synchrony and equilibria | KEEP AS LEMMA / SUPPORTING RESULT | Supplies branches needed for a meaningful selection and bifurcation classification. | Complete branch/existence cases and physical-domain restrictions. |
| P03 — origin and linearization | KEEP AS LEMMA / SUPPORTING RESULT | Model-specific differentiation is necessary, not a new linearization method. | Independently verify coefficients and coincident offsets. |
| P04 — arbitrary-(n,q) Fourier spectrum | KEEP AS LEMMA / SUPPORTING RESULT | Generic circulant theory, S07/S09. Retain general q economically. | Correct shift signs, multiplicities, normality and exact hypotheses. |
| P05 — q=2 mode selection | STRENGTHEN BEFORE PROVING | The quadratic maximizer alone is too close to S03 and elementary optimization. | Proposed statement S05 below; admissible parameter realizability. |
| P06 — large-n limit | STRENGTHEN BEFORE PROVING | A fixed-symbol limit is routine and has a close S03 precedent. | Proposed statement S06; fixed family and useful threshold consequence. |
| P07 — five-node specialization | MOVE TO SUPPLEMENT | Explicit constants are useful checks; golden-ratio values are not new theory. A short motivating example may remain in the main text. | Specialize verified general results; credit Wu-Xing precedents. |
| P08 — matched bilinear comparison | STRENGTHEN BEFORE PROVING | MB at five nodes is a known subfamily of S05. A calibrated qualitative contrast is the promising part. | Proposed statement S08; B05 comparison convention and branch eligibility. |
| P09 — transcritical bifurcation | KEEP AS LEMMA / SUPPORTING RESULT | Use only to organize relevant branches. Generic transcritical machinery is known. | B02 path; boundary interpretation and nondegeneracy. |
| P10 — saddle-node and bistability | KEEP AS LEMMA / SUPPORTING RESULT | Useful for the branch diagram if needed by the core; no broad basin theorem is justified by two roots. | B03: local stable coexistence versus global claims; full-system spectrum. |
| P11 — Hopf spectral conditions | STRENGTHEN BEFORE PROVING | Conditional imaginary-axis equations do not establish a realizable first bifurcation. | Proposed statement S11; a positive admissible path and all-mode exclusions. |
| P12 — Hopf transversality | KEEP AS LEMMA / SUPPORTING RESULT | Essential to the core, but the chain rule is not novel. | Include equilibrium motion; certify a nonzero derivative on the stated regime. |
| P13 — first Lyapunov coefficient | STRENGTHEN BEFORE PROVING | Fourier reduction including cubic terms is already in S02; S08 gives a broad quadratic reduction. | Proposed statement S13; analytic sign information and convention checks. |
| P14 — rotating waves | KEEP AS LEMMA / SUPPORTING RESULT | Conditional symmetry conclusion follows established equivariant Hopf theory, S22. | Verified P11–P13; isotropy, phase sign and exact versus leading-order statement. |
| P15 — heterogeneous equilibrium persistence | NOVELTY IRRELEVANT BUT NEEDED TECHNICALLY | Implicit-function persistence is standard. Needed only if the optional heterogeneity component is retained. | B08 family; invertibility, positivity and stability distinguished. |
| P16 — static sensitivity and Green function | STRENGTHEN BEFORE PROVING | DFT inversion and generic decay are known, S07/S19. Not essential to the recommended core. | Proposed statement S16; a substantive improvement beyond a matrix-function bound. |
| P17 — transient and harmonic response | MOVE TO SUPPLEMENT | Linear propagator/resolvent identities are supporting tools, not a separate discovery. | Distinguish norm/coordinate response, linear/nonlinear dynamics and forcing projections. |
| P18 — stability radius and Hopf shift | STRENGTHEN BEFORE PROVING | Generic bounds/derivatives are known, S10/S11/S21. Optional extension, not a prerequisite for the smallest package. | Proposed statement S18; actual uncertainty class, nonlinear error and sharpness. |

No module is promoted to KEEP AS MAIN THEOREM yet: the candidates need sharper statements and later independent proofs. This is intentional, not a missing disposition.

## Proposed strengthened statements — no proofs

The following are specifications to test, not claims that the desired conclusions hold. If the proposed effect is impossible under the positive parameter domain, a rigorous obstruction is a legitimate outcome. Neither an empty parameter region nor a conditional theorem whose hypotheses are never realized is an adequate substitute for the proposed result.

### S05 — P05: admissible finite-size selection classification

For q=2 and every n≥5, on each explicitly identified positive synchronous equilibrium branch, classify the **entire set** of mode pairs maximizing the modal real part over all modes, in the original positive parameters and equilibrium branch coordinate. Give exact region inequalities, including equality boundaries, uniform mode, and the real Nyquist mode where present. State which regions are nonempty under the equilibrium relation. Distinguish conjugate pairing from ties between distinct pairs. Together with P11–P12, identify which regions can contain a first transverse nonzero-frequency instability along the chosen parameter path. Any claimed change in the selected mode must be realized by admissible parameters or by an explicitly fixed sequence of sizes, not just by free coefficients of an unattached polynomial.

This proposal is more informative than a quadratic vertex formula but still needs the comparison/Hopf consequence to justify principal significance.

### S06 — P06: quantitative finite-size consequences

Freeze a q=2 parameter family and positive branch that do not drift with n except through the stated sampling problem. On an explicitly specified compact parameter set, assume a unique interior continuous-symbol maximizer with uniformly nonzero curvature; for threshold estimates additionally assume a uniformly transverse crossing and branch regularity. Seek explicit constants independent of n that bound selected-angle error by C/n and first-threshold error by C/n² relative to the continuous-symbol threshold, allowing set-valued finite-grid ties. Identify the regimes where these estimates fail or change, including endpoint maxima, vanishing curvature, branch folds and degeneracy of the threshold. Explain a consequence for the DM–MB comparison or wavelength prediction.

These are proposed targets, not established error bounds. The broad approximation method is generic; constants alone are unlikely to be a principal novelty claim. B04 must specify the family first. Angle error and nearest-cosine selection must not be conflated.

### S08 — P08: a meaningful matched-model distinction

Record a comparison rule before computing the contrast. A natural candidate is the same positive parameter tuple in the two canonical equations, with each model evaluated at its own specified positive synchronous branch; this is a recommendation, not resolution of B05. Explicitly restrict to tuples where the compared branches exist. Under the chosen rule, classify a nonempty open regime in which DM and MB have a qualitatively different first instability, selected mode class or Hopf criticality, with both outcomes rigorously certified. State the precise boundary of the contrast and how it changes under any alternative calibration that is actually adopted. If no proposed contrast can occur, replace it by a precise obstruction and reassess its value.

Do not label MB itself new, since S05 contains its five-node instance. Do not interpret topology/parameter-count matching as simultaneous equilibrium, time-scale and interaction-sign matching. If a boundedness-versus-blow-up distinction is used, state whether both compared positive equilibria exist and whether the assertion concerns the full system or only synchrony.

### S11 — P11: realizable first-Hopf regimes

For an explicit positive branch and one-parameter path, identify an open set of the remaining parameters for which the first loss of stability occurs through exactly one conjugate nonuniform pair with nonzero frequency. Give the critical parameter, selected pair and frequency in the chosen exact representation. Require every other eigenvalue to have strictly negative real part at crossing and the equilibrium branch to remain regular and positive. Delimit distinct-pair ties, zero-frequency crossings, branch folds and real-mode crossings. Establish nonemptiness of the claimed regime by rigorous analytic certification; P12 supplies the nonzero crossing derivative and P13 the nonlinear nondegeneracy.

The open set is in the parameters transverse to the chosen crossing path; a Hopf locus itself is not an open subset of the full parameter space. Simultaneous mode crossings are excluded here, not silently described as simple Hopf points.

### S13 — P13: criticality information beyond a formula

On the certified P11–P12 Hopf regime, derive the DM Lyapunov coefficient with the frozen Fourier normalization, Hermitian pairing and Taylor factors, then classify its sign on an explicitly described nonempty parameter region covering every size/mode in the claimed range. State the domain on which the required resolvents exist and delimit harmonic coincidences. Aim for an analytic sign criterion that explains a DM–MB distinction or a transition of criticality; do not substitute a single decimal evaluation for a region theorem. If a zero is retained, classify it only to the order justified: a generalized Hopf claim requires additional nondegeneracy and unfolding conditions beyond l1=0.

A rigorous modest-range sign result can be more valuable than an unsupported all-n assertion. The formula’s reduction technique must be credited to the existing literature.

### S16 — P16: controlled, directional defect response (optional extension)

After B08 fixes the parameter assignment, consider a specified one-node or one-edge coefficient perturbation of size ε at a positive stable homogeneous equilibrium. On a stated compact family with uniform inverse/regularity bounds, seek an explicit first-order response and an O(ε²) remainder in a named norm, uniform in n where claimed. Quantify decay using cyclic graph distance; identify directional rates or a crossover that is sharper than simply applying S19. State the parameter restrictions and show optimality of the claimed rate or a definite gain over a generic bound. A Fourier sum with no estimate does not satisfy this specification.

If uniformity in n is impossible on the intended near-critical family, state the dependence rather than hiding it in constants. A finite-cycle response can wrap around and need not resemble decay on an infinite line. Static zero-frequency response, nonzero-frequency Hopf resonance and nonlinear periodic states are different questions. This strengthened extension should remain optional unless it supports the same core mechanism as selection/criticality.

### S18 — P18: structured parameter tolerance and threshold change (optional extension)

Freeze the heterogeneity family and uncertainty norm (B08–B09). At a specified stable homogeneous base, seek an explicit positive parameter radius r such that every admissible real coefficient perturbation of norm less than r has a unique nearby positive equilibrium in a specified neighborhood and a Hurwitz linearization there. Include direct coefficient effects, equilibrium displacement and controlled higher-order terms. Quantify conservatism against the actual structured distance to instability, or establish the correct asymptotic scaling in a stated regime; an arbitrary sufficient constant alone is not a principal novelty result.

Separately, at a simple transverse Hopf base, seek an expansion of the critical parameter for the same frozen perturbation class with an explicit remainder bound. State when the first-order coefficient vanishes, including any imposed zero-mean constraints. Only if needed, formulate the first nonzero higher-order effect and compare it with existing mode-mixing perturbation results, including S24. Do not infer a positive stability radius at an already critical Hopf point or transfer a full-block linear formula to a repeated/diagonal parameter class without justification.

## Recommended final theorem package and scope

Recommend **strengthened B, including P08 and P13**: a realizable q=2 selection and first-Hopf/criticality classification that yields a robust qualitative DM–MB comparison, with rotating waves as its symmetry conclusion. P01–P04 and relevant branch results support this argument. P06 belongs only if its finite-size consequence is useful. P07 supplies the five-node example. Keep P15–P18 outside the required core unless a sharp result unifies them with that mechanism.

Keep arbitrary n,q in the model and general spectrum; focus the substantive classification on q=2; use n=5,q=2 as motivation and specialization. This is a proposed scope decision. The master, canonical model and dependency files have not been rewritten. There is no publication guarantee and no claim that this proposed package can yet be proved.

## Current blockers and release gates

1. **Coupling-law priority:** retrieve and compare the full S13–S16 models and the highest-risk older Wu-Xing equations listed in [additional_sources_needed.md](additional_sources_needed.md). Until then, T1 stays GRAY.
2. **Precise mathematical targets:** settle branch/path B02, comparison B05 and large-n family B04 before those statements are fixed. Decide whether the core is the strengthened B recommendation.
3. **Optional extension:** B08–B09, a localization observable and a uniformity regime are required before strengthening P16/P18. These do not block a core paper that omits the extension.
4. **Evidence standard:** no novelty verdict upgrades a proof status. The original claims, including the reported numerical Hopf point, remain unverified/unreproduced.

Recommended future order, if authorized: settle scope/statement gates; P01–P04; sharpen P05 with the P08 comparison question; P02/P09/P10 branch results as needed; P11–P13; P14; useful P06/P07 consequences. Optional P15→P16/P17→P18 follows only after its purpose is established. This planning order does not replace the preserved dependency graph.

## Phase 1C current decisions — 2026-09-24

This section supersedes the earlier recommendations and terminology for current planning. Earlier sections remain a dated audit trail. See [final_novelty_verdict.md](final_novelty_verdict.md) for the nine current verdicts and [frozen_theorem_package.md](frozen_theorem_package.md) for the adopted scope. All mathematical statuses remain TODO.

Exact-model priority is **not closed**: S13–S16 main-text inspection is incomplete, although the four-paper chain and the 2024 supplement are now checked to the extent recorded in 05. The supplement supplies concrete topology, equilibrium, Hopf-related and limiting-law overlap; it cannot establish absence from the parent main text. Newly identified direct leads are Lin's 2021 thesis and the citing Xiong–Zhang 2025 paper. No new general survey is requested.

The strongest candidate is a substantive same-coefficient DM–MB contrast. The bare q=2 quadratic rule is a routine adaptation of van Kekem–Sterk's mechanism; its strengthened realizable classification is model-specific. A nontrivial l1 sign region is still unresolved. The frozen package requires it as a research target and postpones sensitivity/robustness extensions.

| Module | Current role / decision |
|---|---|
| P01 | Supporting proposition/lemma; lengthy standard estimates may be supplementary. |
| P02 | Supporting proposition/lemma: complete synchronous-equilibrium classification. |
| P03 | Supporting lemma: correct model-specific linearization. |
| P04 | Supporting proposition/lemma: general Fourier spectrum and normality. |
| P05 | Intended main theorem after strengthening to realizable selection/switch cells. |
| P06 | Conditional corollary only if it adds insight; attempt after the core. |
| P07 | Motivating corollary in the main paper, superseding the earlier supplement-only preference. |
| P08 | Intended main comparison theorem; same-coefficient calibration adopted for this package. |
| P09 | Supporting proposition/lemma. |
| P10 | Supporting proposition/lemma; distinguish stable coexistence from global basin claims. |
| P11 | Spectral component of assembled main Hopf theorem; no standalone conditional-crossing novelty. |
| P12 | Supporting lemma for transversality. |
| P13 | Coefficient proposition/lemma; intended main sign result and assembled Hopf theorem. |
| P14 | Rotating-wave corollary. |
| P15 | Postpone. |
| P16 | Postpone. |
| P17 | Postpone. |
| P18 | Postpone. |

Current attempt order: **P01, P02, P03, P04, P05, P08, P07, P09, P10, P11, P12, P13, P14, P06, P15, P16, P17, P18**. The last four entries are a reserved extension queue; P06 is conditional. P08 criticality comparisons, if claimed, require a later assembly pass after P13. The original dependency graph and proof-compendium reading order remain valid.

B05 is resolved as the same positive coefficient tuple with each model's own explicitly chosen positive synchronous branch on the common existence domain. B02 (branch and crossing path), B04 (if P06 retained), and B07 (normal-form conventions) remain future precise-statement gates. The quantitative sign region cannot be frozen without mathematical work. B08–B09 are dormant because the optional extension is postponed. Old undecided scope/calibration language in preserved historical files should be read with this current overlay.
