# Open decisions and conflict register

No unresolved decision blocks initialization. The DM and MB systems are accepted exactly as specified in the prompt; no inconsistency making the canonical equations undefined on the intended state domain was identified. Entries below block only the indicated later claim or module. They are questions to resolve during future work, not requests for permission to initialize the project.

## Settled canonical choices

DM and MB equations; n≥5; 1≤q≤n−1; all five coefficients strictly positive; modulo-n indexing; dimensionless normalized activities; connected step-q interpretation only under gcd(n,q)=1; q=2 as the principal exact-selection scope; n=5,q=2 application; “demand-modulated” terminology; six-term model secondary only; immutable master; requested modular layout.

Explicit scaffold notation choices: node representatives 0,…,n−1; predecessor shift `(Pz)_j=z_{j−1}`; Fourier exponent `+i theta_m j`, normalization `1/sqrt(n)`; Hermitian pairing `u* v`; strict and nonnegative orthants distinguished; local DM extension domain `(-1,infinity)^n`; `sa(J)` for spectral abscissa. These are disclosed conventions, not derived claims. Unspecified substantive modeling choices remain below.

## Blocking decisions for later work

| ID | Decision still needed | Blocks | Source and required resolution |
|---|---|---|---|
| B01 | Is the exact boundary box claimed to attract asymptotically, or to be entered in finite time? Is a larger box needed for the intended “absorbing” statement? | Final P01 box statement | Master `prop:absorbing-box` and P01 filename use different strengths of language. Define attraction (pointwise versus uniform on bounded sets) and absorption precisely; independently prove the chosen statement. |
| B02 | Which equilibrium branch, network size, scalar parameter path and orientation define each bifurcation and “first instability”? | Final P09–P14 and Hopf part of P18; path-based portion of P05 | The master suggests varying h near one unverified five-node crossing but does not freeze a path. Snapshot mode selection remains possible without this choice. |
| B03 | Does “true bistable region” mean coexistence of two locally attracting equilibria, exactly two attractors, or a global basin-separation theorem? | Final P10 bistability and basin claims | Master “actual bistable region” adds a lower-branch basin claim. Specify attractor class, state domain and local/global quantifiers before a theorem. |
| B04 | What parameters and equilibrium branch remain fixed, or vary with n, in the large-n family? What uniformity and tie/end-point regime is required? | P06 precise asymptotic statement | Master `eq:large-n-mode`; select the n-sequence and error quantity explicitly. A wave-number limit is not automatically a continuum dynamical limit. |
| B05 | How are laws quantitatively calibrated for comparative figures or claims of improved stability? Same coefficients, matched equilibrium, matched local slope, or another declared rule? | Quantitative interpretation in P08 and N03, not the definition of MB | Master functional-form comparison TODO. Topology and parameter count are already fixed; biological equivalence or fairness is not. |
| B06 | How will the chosen Hopf point, nonzero crossing derivative and l1 sign be rigorously certified? Exact identities, analytic bounds, or a separately validated numerical proof? | VERIFIED status of quantitative P11–P13 and P18 claims | Approximate values in the master are starting points only. Ordinary continuation is not a rigorous certification method by itself. |
| B07 | Reconcile adjoint eigenvector equation, phase and scaling, Taylor factorials, l1 orientation and wave time-shift sign with the frozen Hermitian pairing. | P13–P14 and eigenvalue-perturbation part of P18 | Master pairs `J v=i omega v`, `J* p=−i omega p` and `<p,v>=1` without defining a consistent pairing. Record this as a convention inconsistency requiring independent checking; do not copy it into a theorem. No correction is derived in this initialization. |
| B08 | Is heterogeneity assigned to the receiving equation, source, or edge? Which coefficients vary, with what regularity, positivity constraints, amplitude and perturbation profiles? | P15–P18 heterogeneous formulas | Master `eq:heterogeneous` proposes receiving-equation assignment, while the work plan says to freeze it later. It is an archived candidate, not a canonical choice imposed by the prompt. |
| B09 | Which parameter-profile norm and uncertainty class define the sufficient stability radius, and over which neighborhood are constants/remainders uniform? | Explicit parameter tolerance in P18 | Matrix norm is fixed as the induced 2-norm; the parameter-space norm and structured versus arbitrary perturbations remain open. |

## Nonblocking decisions and proof obligations

| ID | Unsettled issue | Resolution gate |
|---|---|---|
| NB01 | Physical activity scales, common versus node-specific reference scales, dimensional coefficients and time scale | Required before a dimensional or physiological interpretation, not for the given dimensionless ODE. Do not invent measured units or data. |
| NB02 | Availability and exact provenance of the author drafts, generated pasted texts and example papers | Obtain them before attributing a particular candidate to author-originated material. The master alone does not distinguish every source passage reliably. |
| NB03 | Exact Lin–Han model, coefficient domain, index directions, bibliographic details and status of the arbitrary-n extension | Primary-source literature audit before any secondary six-term application. Missing source does not block DM/MB. |
| NB04 | “Locally asymptotically stable iff all real parts are negative” in master `thm:general-spectrum` | P04 must distinguish Hurwitz/linear stability from nonlinear classification at zero real part; no blanket nonlinear equivalence is accepted. This is a proof-statement review, not a newly proved correction. |
| NB05 | Terminology of connected control cycle versus connectivity of the full graph; coincident offsets when q=1, n−1, or n/2 | Keep the prompt's gcd condition limited to the step-q interpretation. P03/P04 must add coincident derivative contributions and cover even n. No silent generic-offset assumption. |
| NB06 | Least-stable mode versus first unstable mode, ties, mode aliases and branch dependence | Use set-valued maximizers at a fixed point; P05/P11 must classify ties and multiple critical modes; first crossing needs B02. |
| NB07 | Depth and location of the a=A, mu=0 unfolding and fold–Hopf, zero–Hopf, Hopf–Hopf, generalized-Hopf or mode-tie analysis | P09/P10/P13 can record exclusions; decide main text, supplement, or later paper after the core generic theorems. No such point is assumed to exist. |
| NB08 | Optional persistence of a periodic orbit under heterogeneity | Main requested program includes equilibrium persistence. Decide whether to add the orbit theorem after P14 and Floquet/hyperbolicity evidence; it is not silently included in P15 completion requirements. |
| NB09 | Meaning of localized response, directionality and spatial decay on a finite ring; forcing protocol and propagation observable | P16/P17 before claims about decay, velocity, resonance or direction. “Localized forcing” need not mean a localized response. |
| NB10 | Main-text versus supplement placement of harmonic response, full tensors, general-(n,q) maps, extra figures and random-heterogeneity covariance | All requested tasks retain proof owners. Placement can be decided after their mathematical scope is known. |
| NB11 | Numerical software, exact versions, precision, tolerances, continuation settings, l1 implementations and rigorous-validation tools | N01/N02 before computations. Archived rtol=1e−9 and atol=1e−11 are proposals only. |
| NB12 | Baseline parameters, test sizes, parameter planes, initial conditions and representative regimes | N02/N03 after theory; the master baseline and reported Hopf point are unverified starting choices. Add even n and offset-collision cases to later validation. |
| NB13 | Monte Carlo priors, validity filters, uncertainty summaries and whether to include random stability percentages | Optional supplement only; no fraction or model-quality conclusion is available. |
| NB14 | Novelty, priority, overlap, precise citations and classical-language translations | Complete 03 later. All confirmed-novelty fields remain empty now. |
| NB15 | Interpretation of “balance,” normal operation, organ labels and applicability beyond five nodes | Keep these as modeling interpretations. No clinical conclusion, data fit or physiological golden-ratio claim is authorized. |
| NB16 | Final title, author/affiliation list, acknowledgment/grant details, page allocation, license, public repository and journal formatting | Writing and release stage. SIADS is a target, not an assessed acceptance claim. No final manuscript prose is generated. |
| NB17 | Terminology “same signs” in structural comparison | P08 must distinguish signs of displayed interaction terms from signs of Jacobian entries and resulting dynamical effects. Topology/parameter-count matching does not resolve this interpretation. |

## Conflicts or tensions resolved for the scaffold

| ID | Master location | Authority and disposition |
|---|---|---|
| C01 | Optional source-saturating variant TODO at lines 640–655 asks which base model to use | Prompt A settles DM. The variant is postponed; no base-model decision remains open. |
| C02 | Fourier vectors at lines 342–362 are unnormalized; DFT/Green-function normalization later left TODO | Prompt requests a frozen normalization. Use the unitary convention in 01. All derived coefficients must be independently translated; none are imported as verified. |
| C03 | Five-node labels use 1,…,5 while Z_n is used abstractly | Use representatives 0,…,n−1 and map original label r to r−1. Direction and cyclic order are retained. |
| C04 | Six-term model is discussed as a published comparator before source verification | Prompt B makes MB primary. The six-term equation is an unverified archival transcription, conditional secondary application only. |
| C05 | The master suggests a manuscript/code repository layout at lines 1644–1665 | Prompt D controls this initialization. The requested modular layout replaces that proposal; no code or manuscript tree is created. |
| C06 | Draft uses T0 for both a dimensional time scale and a spectral coefficient; alpha/eta also have multiple uses | 01 discloses reserved names: time scale T_scale, future spectral tau, spectral abscissa sa, positive margin delta and collective profile zeta. Coefficient formulas remain TODO. |
| C07 | Master mathematical and numerical assertions sometimes read as established prose | Prompt F and task restrictions control. All such assertions are quarantined in the registry with their actual evidence status. |
| C08 | Master may treat the generated six-term reanalysis, motives and extensions as a broad contribution package | The requested 18 proof modules define the active package. Future-paper claims retain explicit reserved owners in the registry and are not silently promoted into this paper. |

## Issues postponed to another paper

- **F01 local motifs:** one- and two-node analyses; piecewise-smooth sectors and switching; recover the undefined `G(x,x_c)` in the three-node draft before any analysis; justify slow–fast isolation. The missing term makes that archived motif incomplete, not the canonical DM model.
- **F02 pathology extensions:** choose and justify overdraw and counter-action mechanisms; resolve the archived positivity objection; recompute the system from its final equations.
- **F03 adaptive set points:** positivity of set points, regulation law and any dynamical set-point variables.
- **F04 intervention/control:** objective, admissible controls and interpretive scope.
- **F05 stochastic and delay extensions:** noise model, delay distribution, state domain and stability framework.
- **F06 data and calibration:** valid measurements, identifiable parameters and normalized reference scales.
- **F07 prior Lyapunov and integrability reanalysis:** original six-term source and numerical setup; exact restrictions; periodic/boundary claims; zero-exponent hypotheses; independent first integrals; periodic Volterra/Kac–van Moerbeke relationship; no torus or quasiperiodicity inference from the archived spectra alone.
- **F08 source-saturating variant:** separate model contract and fresh equilibrium, spectrum, bifurcation and sensitivity analyses; never mix it with DM.

These reservations do not authorize work now. The corresponding future-paper proof paths in the registry are names for later modules only.
