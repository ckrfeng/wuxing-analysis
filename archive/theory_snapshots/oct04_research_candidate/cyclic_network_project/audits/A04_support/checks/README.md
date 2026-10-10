# Independent exact P04 checks

**Result: PASS.** The retained run checks **39** admissible `(n,q)` pairs,
**285** rational matrices and **2,242** eigenvalue occurrences using **62,094**
named exact assertions. There are no floating-point tolerances. Runtime in the
recorded local environment was about 12.2 seconds.

## Files and reproduction

- `independent_exact_p04.py`: independent checker using Python's standard library.
- `independent_exact_p04_results.json`: complete exact inputs, rational matrix
  characteristic polynomials, cyclotomic eigenvalue groups, selected nullities,
  graph cycles, counts, runtime and scope limits.
- `independent_exact_p04_run.log`: retained console output from the successful run.
- `independent_exact_p04_authentication.json`: retained SHA-256-only run, with
  no compiler or algebraic computations.

From the audit workspace root, run:

```sh
python3 p04_independent_audit/audits/A04_support/checks/independent_exact_p04.py
```

From a project root after the audit-only ZIP has been merged into the original
`cyclic_network_project` directory, run:

```sh
python3 audits/A04_support/checks/independent_exact_p04.py
```

The default locates either the audit workspace's extracted `input` project or
the merged project's `proofs` directory relative to the script, so it does not
depend on the current working directory. If the audit-only package is extracted
separately, supply the original P04 source explicitly:

```sh
python3 audits/A04_support/checks/independent_exact_p04.py --p04-source /path/to/cyclic_network_project/proofs/P04_arbitrary_nq_fourier_spectrum.tex
```

To perform only source authentication, without a compiler, numerical library,
or algebraic test run, add `--authenticate-only` to any command above. This
prints a small JSON report and leaves the full-check results unchanged. An
explicit source path overrides automatic discovery; any hash mismatch fails.

The script imports only standard-library modules. No attached project executable
or internal P04 validation program is imported, run or copied. The only input
file read by the checker is the P04 source, to authenticate its SHA-256:
`ab80f695b3e20c852c572b7b174ecaf9964eac1aba62e3e55b2b4d3e60754e0c`.
Running the script regenerates the JSON; its recorded runtime and environment
metadata need not be byte-identical across runs.

## Independent methods

1. Rational Jacobians are assembled by **adding** four contributions at modular
   node-column indices: `j`, `j-1`, `j+q`, `j-q`. Collisions therefore cannot
   overwrite prior contributions. Exact rational multiplication checks
   `J J^T = J^T J` for all 285 matrices.
2. A small independent polynomial implementation constructs the cyclotomic
   polynomial recursively from `z^n-1` and represents eigenvalue phases in
   `Q[z]/Phi_n(z)`, with `z = exp(2 pi i/n)`. All coefficients use `Fraction`.
   Conjugation substitutes `z^-1`; no approximate complex arithmetic is used.
3. Let `U = sqrt(n) Q`. The checker verifies both `U* U = n I` and `U U* = n I`
   without introducing square roots (710 entry checks). It verifies 12,055
   wraparound identities for integer shifts from `-2n` through `2n` and every
   node and Fourier label, in each dimension 5 through 10.
4. For every matrix, direct matrix-vector multiplication verifies every claimed
   Fourier eigenvector (18,430 entries). A separate inverse Fourier sum verifies
   `J = Q Lambda Q*` (18,430 entries). Both identities, together with exact
   unitarity, also give `Q* J Q = Lambda` for these instances.
5. A rational Faddeev-LeVerrier calculation produces the characteristic
   polynomial directly from the assembled matrix. All 2,527 coefficients agree
   exactly with the product over Fourier labels in the cyclotomic field. This
   includes all repetitions. Exact Gaussian elimination independently checks
   **72** eigenspace nullities against label multiplicities in selected repeated
   real, repeated nonreal, cancelled-offset and boundary controls.
6. Every label's conjugacy, real part and signed imaginary part are checked
   exactly. The latter is checked as `i Im(lambda)` to avoid adjoining an
   unnecessary square root of -1. All three collision formulas, zero labels,
   even singletons and row sums are checked. Four separate formal multivariate
   polynomial identities verify the synchronous derivative and three
   equilibrium reductions after denominators are cleared; equilibrium
   reductions are checked modulo the scalar equilibrium equation.
7. Step-`q` cycles are built by following modular indices. Their count, length,
   residue classes and equality with the reverse-step partition are verified
   for all 39 pairs. No disconnectedness assertion about the full coupling is
   inferred.

## Coverage

All `(n,q)` with `5 <= n <= 10` and `1 <= q < n` occur. This includes `(5,2)`,
`(6,2)`, `(6,3)`, `(7,1)`, `(8,4)`, all last offsets and all noncoprime pairs
in those dimensions. Each pair is tested at seven rational parameter/state
families: an origin control; the positive equilibrium with repeated real values
when `q=1`; a negative nonstationary state; a positive nonstationary state;
a positive equilibrium with `C=H`; a negative state with `C+G=0`; and a
negative nonzero equilibrium. Thus `G=H` half-offset cancellation and both
sign regimes for `G,H` are included.

Twelve additional targeted matrices check:

- `(n,q)=(6,2)`, `x=1`, `(a,k,c,g,h)=(17/4,1,1,1,13/4)`: positive equilibrium,
  nonzero purely imaginary conjugate pair, exact real parts
  `(-17/4,0,-1/2,-21/4,-1/2,0)`, and invertibility.
- `(n,q)=(5,2)`, `x=1/4`, `(a,k,c,g,h)=(3,1,1,33/8,1)`: positive equilibrium
  with zero singleton. The exact conditions `C>0`, `G-H>0`, `lambda_0=0`
  and nontrivial first-harmonic roots for every other label certify strict
  negativity of the other real parts using `cos(theta)<1` for those labels.
- `(n,q)=(6,3)`, `x=1`, `(a,k,c,g,h)=(4,1,4,8,1)`: repeated **nonreal** values
  at nonconjugate labels `1,2` and at `4,5`, with multiplicity two and
  independently checked eigenspace dimension two.
- `(n,q)=(6,5)`, `x=-1/2`, all five parameters equal to one: exact cancellation
  `C+G=0`, giving `J=(5/2)I+(1/2)P^-1`.
- The six pairs `(5,2)`, `(6,2)`, `(6,3)`, `(7,1)`, `(8,4)`, `(6,5)` at `x=1`,
  `(a,k,c,g,h)=(5/2,1,1,2,1)`: the audit's named positive equilibrium examples,
  each with exact `(d,C,G,H)=(-7/4,1/2,1/2,1)`.
- `(n,q)=(5,2)`, `x=-1/2`, `(a,k,c,g,h)=(2,1,4,4,1)`: the audit's named
  negative nonstationary state with exact `(d,C,G,H)=(7/2,8,-8,-1/2)`.
- `(n,q)=(6,3)`, `x=1`, `(a,k,c,g,h)=(7/2,1,1,4,1)`: the audit's named
  positive-equilibrium half-offset cancellation `G=H`, giving
  `J=(-7/4)I+(1/2)P`.

## Limits

These finite matrix instances corroborate the P04 algebra; they do not prove
universal spectral assertions for arbitrary dimension. The four formal
polynomial identities are exact identities, but their intended application
still requires the hypotheses discussed in the audit. No numerical eigensolver
or matrix exponential is used. Exact semigroup norms, all-time linear stability
and nonlinear implications remain matters for the written analytic audit.
The boundary controls assert no Hopf bifurcation or crossing. No P05 selection
reduction or P11-P13 analysis is performed.
