# Phase 1 overlap and novelty report

Date: 20 September 2026. **Literature audit completed for the six supplied PDFs, with explicit supplemental-source gaps. All proposed project theorems remain TODO.** No proofs, numerical experiments or final-paper drafting were performed. The master and its archive were not edited.

## Main finding

The exact demand-modulated equation was not located in the six supplied papers. That finding supports a provisional model-specific contribution; it does **not** establish priority. Several proposed techniques already have close precedents, and the five-node matched bilinear comparator is contained in Lin and Han's published model.

The decisive comparison is van Kekem and Sterk's Lorenz-96 analysis: the supplied manuscript already contains a two-harmonic cosine spectrum, first-mode selection, an explicit large-network wave-number limit and a Fourier reduction of the first Lyapunov coefficient. Cite these as antecedents, and assess the contribution of the particular DM coefficient restrictions and resulting conclusions. Exact locations: §2.1, pp. 8–9, Eqs. (3)–(6); Proposition 5, pp. 11–12; Proposition 6, p. 13; Theorem 4, p. 11; §4.3, pp. 38–46, especially Eq. (36), p. 44. [Published article](https://doi.org/10.1016/j.physd.2017.11.008).

## Eight requested decisions

| Target | Current classification | Consequence |
|---|---|---|
| Exact demand-modulated model | Apparently new specialization; priority unresolved | Not located in the six core equations. Obtain the related enzymatic five-element papers before claiming a new coupling law. |
| Arbitrary-(n,q) Fourier spectrum | Directly implied by known circulant theory once the actual Jacobian is verified | The model coefficients and offset collisions need independent checking; Fourier diagonalization and normality are known. |
| Exact q=2 mode selection | Apparently new specialization; underlying quadratic method known | A complete DM parameter/tie classification may be useful. Do not claim first quadratic-cosine mode selection. |
| Large-n selected-wave-number limit | Direct implication/specialization for a fixed symbol; stronger claims unresolved | A closely analogous explicit limit is already published. Fix the varying-n family before assessing more ambitious novelty. |
| Matched bilinear comparison | Comparator component definitely known; exact DM–MB comparison apparently new specialization | MB at n=5,q=2 is a subfamily of Lin–Han. Comparison calibration remains open. |
| Explicit first Lyapunov reduction | General reduction definitely known; DM formula apparently new specialization; sign theorem unresolved | Nonzero cubic derivatives and a proved sign region distinguish the remaining work from known quadratic reductions. |
| Heterogeneous Fourier Green function | Homogeneous-base inverse response directly implied; localization novelty unresolved | First-order sensitivity at a circulant base is different from exact Fourier diagonalization after heterogeneity. Inverse localization has substantial prior theory. |
| Robustness bounds and Hopf shift | Matrix bounds and simple-eigenvalue sensitivity directly implied; explicit parameter theorem unresolved | Specify the uncertainty class and norm and include equilibrium movement. No explicit DM radius has been established. |

**Apparently new theorem** is kept as a separate category, but no complete project theorem receives that label unconditionally in this audit. It would require a precise additional conclusion beyond known specialization and adequate comparison literature. A rigorous DM sign region or a sharp parameter-dependent robustness certificate may ultimately qualify; neither has been established or sufficiently delimited here.

## Highest overlap risks

1. **Generic methods presented as new results.** Circulant normality and inversion are covered by Gray, §3.1–3.2, printed pp. 32–35, Theorem 3.1. Pais et al. already give a network-specific analytical Hopf coefficient (Lemma 4.6, manuscript p. 13; Appendix D, pp. 26–28). Kerin–Engler give a general quadratic circulant reduction (Lemma 1, Eq. (29), p. 12). These sources are recorded in the [main audit](03_literature_audit.tex) and [bibliography](references.bib). [Gray](https://ee.stanford.edu/~gray/toeplitz.pdf), [Kerin–Engler](https://arxiv.org/abs/2005.07767v2).

2. **Five-node comparator presented as a new model.** Lin–Han, §2.1, printed p. 778, Eq. (2), permits nonnegative coefficients. Its coefficient tuple `(a_L,b_L,c_L,d_L,g_L,h_L)=(a,k,c,h,0,g)` gives exactly MB at n=5,q=2. Its equal-activity scalar reduction is already in §2.2.1, Case 4, p. 779, Eqs. (5)–(7). This equation matching has been visually checked in the supplied PDF. It does not establish the proposed comparative dynamical conclusions. [Lin–Han 2020](https://doi.org/10.23919/CCC50068.2020.9188438).

3. **Coupling-law priority inferred from an incomplete corpus.** The 2021 *Analysis of Enzymatic Regulatory Five-Element Model* and 2024 *What is special of “five” in biological regulatory networks?* are directly relevant. Their complete models were not available here. The 2024 publisher abstract explicitly concerns enzymatic networks, multiple network sizes and the five-element topology. These are main-paper gaps, not a separate archival track. [2021 paper](https://doi.org/10.23919/CCC52363.2021.9550151), [2024 paper](https://link.springer.com/article/10.1007/s11071-024-09374-5).

4. **A Fourier inverse mistaken for a localization or robustness theorem.** The inverse representation does not by itself imply concentration near a forced node, uniform decay with network size, or parameter tolerance. Demko–Moss–Smith already treat inverse decay (inspected publisher-indexed p. 493, Proposition 2.3 and Theorem 2.4); exact applicability to the cyclic geometry remains open. Matrix perturbation bounds also do not substitute for controlling the changed equilibrium. [Inverse-decay source](https://www.ams.org/mcom/1984-43-168/S0025-5718-1984-0758197-9/S0025-5718-1984-0758197-9.pdf).

## Blocking gaps for strong novelty claims

These block the indicated publication claims, not use of the scaffold or future independent mathematical work.

| Gap | Needed evidence | Affected claims |
|---|---|---|
| L01: full 2021 and 2024 enzymatic papers | Displayed coupling laws, rescalings, parameter domains, analytical results and supplements | Priority of DM, demand modulation, five-node specialization and exact comparison |
| L02: earlier Wu-Xing equations | Follow Lin–Han p. 781 references [9], [10], [14]: Wang's 2008 thesis; Ding–Wang 2008, pp. 269–270; Li 1987, pp. 966–969 | Prior receiver dependence and five-node response/comparison results |
| L03: localization and robustness coverage | Complete Demko paper and subsequent sparse/graph-distance results; structured stability-radius and cyclic-feedback literature | Any claim of a new localization theorem or new general robustness method |
| L04: exact proposed theorem scope | Resolve B02/B04/B05/B08/B09: path, large-n family, comparison calibration, heterogeneity assignment and parameter norm | Whether the remaining contribution is a specialization or a new theorem |

L02 references are leads recorded in an inspected bibliography. Their full texts and exact theorem/equation locations are not claimed to have been checked. Titles and identifiers for L01 are in `references.bib`; no missing equation number has been invented. A 2023 *Comparison of Multi-Node Networks on Biological Properties* conference paper (DOI 10.23919/CCC58697.2023.10239797) is an additional full-text lead in the same research lineage, not yet an audited source.

## Source reliability and convention corrections

- **Adjoint convention corrected in project metadata.** The initialization's B07/C078 concern about opposite adjoint signs was mistaken. Jaramillo et al., p. 6, Eq. (16), Pais et al., Appendix B, pp. 24–25, and Kerin–Engler, p. 12, Eq. (28), use the same Hermitian convention: `Jv=iωv`, `J*p=−iωp`, `<p,v>=1` for real J. That sign is standard. Scaling, phase, Taylor factors and the actual model coefficient remain for later verification.
- **Wei manuscript cautions.** The attached 18-page copy has inconsistent dimensions in Eqs. (2.6)–(2.7), p. 3; fixes and varies m simultaneously in Theorem 2.1, p. 4; and combines a negative reported coefficient with an unstable-cycle statement in Theorem 2.2, pp. 4–5. These are disclosed source inconsistencies. This phase does not repair or disprove those results. Compare the final publisher text/errata before relying on them. Its journal issue year is 2021 despite the supplied filename's 2020.
- **Five-element numerical reports remain source reports.** Lin–Han's trajectories/exponents and Nian–Li's fitted examples have not been reproduced. Neither supplies evidence for the DM model's validity or the proposed general theorems.
- **Edition limits are explicit.** The supplied Pais, van Kekem–Sterk, Wei and Jaramillo copies use author-manuscript pagination. Do not convert these page references into journal pages by adding an assumed offset. Jaramillo's final article number is still a bibliography completion item.

## Files and use

- `03_literature_audit.tex`: six full core records, eight supplemental/lead records, exact locators, assumptions and evidence limits.
- `references.bib`: fourteen source records, with unreviewed/partial sources clearly marked.
- `novelty_matrix.tex`: every source against all eight targets, detailed classifications and manuscript-claim gates.
- `overlap_risk_report.md`: this decision report.
- `literature_audit_compendium.tex`: separate compilable root loading the audit, matrix and bibliography.
- `audits/phase1_source_manifest.md`: supplied-file fingerprints and reproducible source identifiers.
- `audits/phase1_checks.md`: document-build and preservation checks, not a mathematical verification.

The initialized proof root and all Pxx/Nxx fragments are preserved. The new audit root has a preamble; the two audit `.tex` files are includable fragments. Compile from `cyclic_network_project/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error literature_audit_compendium.tex
```

Alternatively run pdfLaTeX, BibTeX, then pdfLaTeX twice on `literature_audit_compendium`. The audit root uses `plainurl.bst` from the TeX `urlbst` package to display URLs and DOIs. All bibliography entries are local; compilation needs no internet access or shell escape. No primary PDF is redistributed in the ZIP. Its contents are the research package and audit sources, not a paper manuscript.

## Handoff

Read the main audit and novelty matrix before writing novelty prose. Close L01–L03 where needed for priority claims. Independently derive P01–P18 only in a later authorized phase, with the existing dependency order and verification lifecycle. This report makes no change to the canonical models and promotes no proof status.
