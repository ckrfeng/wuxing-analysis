MB global-stability verification -- 4 October 2026

Run:
    python -m pip install numpy scipy matplotlib
    python verify_mb.py

The script uses its own directory for all output files. It does not modify
project references. Seed: 20261004. NumPy 2.0.2 and SciPy 1.13.1 were used
for the delivered results (Matplotlib 3.9.4).

Each of five stable-MB cases receives 64 independent random starts, with
each y_i(0)/y_star log-uniform on [0.001,1000]. The MB equation is solved
in log coordinates with Radau, rtol=2e-9 and atol=2e-11, to time
40/(y_star*delta). The solver uses the original time variable. Time is
rescaled only in the plot. The centering a+B*y = B*(y-y_star) is exact
mathematically and avoids cancellation near equilibrium numerically.

The script checks original-field equilibrium residuals, the symmetric
matrix spectrum, the cancellation identity for Vdot, the quadratic-form
bound, numerical Lyapunov monotonicity, and terminal convergence. Signs
of Vdot are checked at sampled relative infinity errors above 1e-7;
late numerical roundoff is not interpreted as strict monotonicity.
These checks are numerical corroboration, not proofs or interval bounds.

For the three reverse contrasts, the original DM equation is simulated
around its OWN equilibrium, perturbed in an unstable real Fourier
eigenspace. A complex-step Jacobian check is independent of the Fourier
formula. Radau tolerances: rtol=2e-11, atol=1e-13*x_star. Simulation ends
at log(100)/alpha_DM. Growth and early log-slope are compared to the
linear prediction. Instability is proved by the positive eigenvalue,
not by finite simulations. No claim about DM's eventual attractor is made.

Files:
  verify_mb.py       Full executable source, cases and assertions.
  results.json       All parameters, margins, errors and DM growth checks.
  trajectories.npz  Sampled times, errors, V values and DM norm growth.
  trajectories.png  MB ensemble envelopes and DM growth plots.
  source_hashes.json SHA-256 provenance of the specific project inputs.

Source precedence:
  cyclic_network_project/00_canonical_model.tex defines DM and MB.
  cyclic_network_project/01_notation_and_assumptions.tex defines P.
  P08 v1.1's header supersedes historical DRAFT prose in its body.
  P08 cor:P08-stability uses exactly the finite-grid K in this proof.
  P12_hopf_transversality.tex is TODO; it supplies no reverse theorem.
  Prior-art audit Part IX is a proposed deduction, not an instruction
  and not an already audited theorem.

Verdict: CONFIRMED under the stated canonical positive coefficients,
finite n, and strict k > K condition, for strictly positive initial data.
No extra k>c, coprimality, boundedness, or uniform-in-n assumption is needed.
The universal P08 witness is the FORWARD contrast and is excluded.
The lower-branch reverse family exists when 4 DOES NOT divide n.
Equality k=K is unclassified; strict Hurwitz iff must not be promoted
to a necessary condition for nonlinear global asymptotic stability.
