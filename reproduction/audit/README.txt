Wu-Xing verification materials - revised October 4, 2026

The revised PDF review is delivered separately. Its code appendix contains
only the five-term demand-modulated model DM_(5,2).

FILES
canonical_model.py: standalone five-term model, positive synchronous
  equilibria and analytic Jacobian. Parameter order (a,k,c,g,h).
canonical_model.ode: matching XPPAUT setup with a 5% Wood disturbance.
canonical_checks.json: fresh checks of these standalone files.
Figure_Model_Code_Check.txt: retained figure-to-model mapping and limitations.
audit.py: comparison reproduction program for DM_(5,2) and six-term Lin.
outputs/audit_results.json: verified retained numerical results.
outputs/verified_figures/: the four retained comparison figures, PNG and SVG.

RUN
With NumPy installed:
    python canonical_model.py
Expected balanced level: 2.670286436967
Expected largest eigenvalue real part: -1.153723520689

To regenerate comparison results and figures, install requirements.txt, then:
    python audit.py
Run from the extracted archive directory. This takes a few minutes because
it includes variational Lyapunov calculations for the Lin reference model.
Verified environment: NumPy 2.0.2, SciPy 1.13.1, Matplotlib 3.9.4.

FIGURES
01: baseline Jacobian eigenvalues, with parameter values in the legend.
02: initial perturbations; normalized activities, Lin to t=120 and DM to t=12.
03: corrected master stability map with missing equilibria and denominators.
04: sampling frequencies among eligible equilibria and among all draws.

SCOPE
Use positive parameters and nonnegative initial activities for canonical DM.
The exact model preserves nonnegative states and is bounded for k>0;
numerical solvers still have finite error. No trajectory clipping is used.
Lin is a separate literature comparator that also preserves nonnegativity
while solutions exist. It is retained for the mentor's Section 3.
The theoretical project's matched five-term MB comparator is not implemented
here; these plots must not be relabeled as DM-versus-MB comparisons.
Stability refers to the specified synchronous equilibrium, with the upper
positive DM branch used in the comparison maps. Parameter distributions are
illustrative assumptions, not fitted physiological priors.
XPPAUT equation transcription was checked; the XPPAUT application was not run.

Sources: supplied Claude record and section outline; Lin and Han (2020),
DOI 10.23919/CCC50068.2020.9188438. Original supplied sources remain intact.
