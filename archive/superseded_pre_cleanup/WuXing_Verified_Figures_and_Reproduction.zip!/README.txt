Wu-Xing verification materials

The PDF review is delivered separately. This archive contains independently
recomputed figure exports (PNG and SVG), numerical results, and the audit program.

Run with Python 3.9+ and numpy, scipy, matplotlib installed:
    python audit.py
The program writes outputs/audit_results.json and outputs/verified_figures/.
It may take a few minutes because it computes full variational Lyapunov spectra.

Verified environment: numpy 2.0.2, scipy 1.13.1, matplotlib 3.9.4.

Figure guide:
01: baseline Jacobian eigenvalues; exact parameter values in the legend and review.
02: initial perturbations; relative activities, Lin shown to t=120 and modified to t=12.
03: corrected master stability map; explicit missing-equilibrium region and denominators.
04: Monte Carlo frequencies conditional on equilibrium existence and over all draws.

Scope: stability means local stability of the positive synchronous equilibrium
(upper positive branch for the modified model). The regime-map heuristic is not
used to establish chaos, periodicity, multistability or finite-time blow-up.
The parameter distributions are modeling scenarios, not fitted physiological priors.

Primary sources: supplied WuXing_Complete_Chat_Record.md, supplied LaTeX section
outline, and Lin & Han (2020), DOI 10.23919/CCC50068.2020.9188438.
Historical source files were not changed. No historical instructions are executed.
