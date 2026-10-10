#!/usr/bin/env python3
"""Independent P03 checks; standard-library exact algebra + NumPy secondary checks.

Run: <python3 with numpy> check_p03.py [/path/to/cyclic_network_project]
The direct derivative is obtained by differentiating a common-denominator
polynomial for the canonical vector field AFTER all modular indices are fixed.
It is compared with the proposed additive Kronecker formula by exact integer
polynomial identities.  No stored blueprint Jacobian is read.  Positive-state
Fourier eigenvalues and normality are deliberately outside this checker.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json
import platform
import sys

import numpy as np


class Poly:
    """Small sparse multivariate polynomial with exact integer coefficients."""

    def __init__(self, nv, terms=None):
        self.nv = nv
        self.t = {e: int(v) for e, v in (terms or {}).items() if v}

    @classmethod
    def const(cls, nv, value):
        return cls(nv, {(0,) * nv: value})

    @classmethod
    def var(cls, nv, index):
        e = [0] * nv
        e[index] = 1
        return cls(nv, {tuple(e): 1})

    def coerce(self, other):
        return other if isinstance(other, Poly) else Poly.const(self.nv, other)

    def __add__(self, other):
        other = self.coerce(other)
        out = Counter(self.t)
        for e, v in other.t.items():
            out[e] += v
        return Poly(self.nv, out)

    __radd__ = __add__

    def __neg__(self):
        return Poly(self.nv, {e: -v for e, v in self.t.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        out = Counter()
        for e, v in self.t.items():
            for f, w in other.t.items():
                out[tuple(x + y for x, y in zip(e, f))] += v * w
        return Poly(self.nv, out)

    __rmul__ = __mul__

    def __pow__(self, power):
        assert power >= 0
        out = Poly.const(self.nv, 1)
        for _ in range(power):
            out = out * self
        return out

    def diff(self, index):
        out = {}
        for e, v in self.t.items():
            if e[index]:
                f = list(e)
                f[index] -= 1
                out[tuple(f)] = v * e[index]
        return Poly(self.nv, out)

    def substitute(self, replacements):
        out = Poly.const(self.nv, 0)
        for exponents, value in self.t.items():
            term = Poly.const(self.nv, value)
            for i, power in enumerate(exponents):
                if power:
                    term *= self.coerce(replacements.get(i, Poly.var(self.nv, i))) ** power
            out += term
        return out

    def __eq__(self, other):
        return self.t == self.coerce(other).t


def assert_poly_equal(left, right, label):
    difference = left - right
    if difference.t:
        raise AssertionError(f"Polynomial identity failed: {label}: {difference.t}")


def exact_rank(matrix):
    mat = [[Fraction(int(x)) for x in row] for row in matrix]
    nrows, ncols = len(mat), len(mat[0])
    row = 0
    for col in range(ncols):
        pivot = next((i for i in range(row, nrows) if mat[i][col]), None)
        if pivot is None:
            continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        div = mat[row][col]
        mat[row] = [x / div for x in mat[row]]
        for i in range(nrows):
            if i != row and mat[i][col]:
                factor = mat[i][col]
                mat[i] = [x - factor * y for x, y in zip(mat[i], mat[row])]
        row += 1
        if row == nrows:
            break
    return row


def shift(n):
    p = np.zeros((n, n), dtype=np.int64)
    for i in range(n):
        p[i, (i - 1) % n] = 1
    return p


def exact_checks():
    counts = Counter()
    n_records = []
    for n in range(5, 11):
        nv = n + 6
        xs = [Poly.var(nv, i) for i in range(n)]
        a, k, c, g, h, r = [Poly.var(nv, n + i) for i in range(6)]
        origin = {i: 0 for i in range(n)}
        sync = {i: r for i in range(n)}
        S = 1 + r
        p = shift(n)
        identity = np.eye(n, dtype=np.int64)
        for q in range(1, n):
            pq = np.linalg.matrix_power(p, q)
            pinvq = np.linalg.matrix_power(p, n - q)
            counts["n_q_pairs"] += 1
            if q == 1:
                counts["q_1_pairs"] += 1
            if q == n - 1:
                counts["q_n_minus_1_pairs"] += 1
            if 2 * q == n:
                counts["even_half_pairs"] += 1
            for i in range(n):
                im, ipq, imq = (i - 1) % n, (i + q) % n, (i - q) % n
                xi, xm, xp, xmq = xs[i], xs[im], xs[ipq], xs[imq]
                A, B = 1 + xi, 1 + xp
                D = A * B
                # Single rational expression of the actual identified variables.
                N = (a * xi - k * xi**2 - h * xi * xmq) * D + c * xm * B - g * xi * A
                D2 = D**2
                for j in range(n):
                    # Algorithmic exact differentiation; no analytical Jacobian used.
                    direct = N.diff(j) * D - N * D.diff(j)
                    proposed = Poly.const(nv, 0)
                    if j == i:
                        proposed += (a - 2 * k * xi - h * xmq) * D2 - c * xm * B**2 - g * A**2 * B
                    if j == im:
                        proposed += c * A * B**2
                    if j == ipq:
                        proposed += g * xi * A**2
                    if j == imq:
                        proposed += -h * xi * D2
                    assert_poly_equal(direct, proposed, (n, q, i, j, "general"))
                    counts["general_jacobian_entries"] += 1

                    # Test both rational derivatives separately by cross multiplication.
                    pos_direct = (c * xm).diff(j) * A - c * xm * A.diff(j)
                    pos_expected = (c * A if j == im else 0) - (c * xm if j == i else 0)
                    assert_poly_equal(pos_direct, pos_expected, (n, q, i, j, "positive_input"))
                    neg_direct = (-g * xi).diff(j) * B + g * xi * B.diff(j)
                    neg_expected = (-g * B if j == i else 0) + (g * xi if j == ipq else 0)
                    assert_poly_equal(neg_direct, neg_expected, (n, q, i, j, "negative_input"))
                    counts["separate_rational_derivative_entries"] += 2

                    origin_expected = (a - g if j == i else 0) + (c if j == im else 0)
                    assert_poly_equal(direct.substitute(origin), origin_expected, (n, q, i, j, "origin"))
                    counts["origin_reduction_entries"] += 1

                    # Common denominator (1+r)^4 allows exact generic-r comparison.
                    dnum = (a - 2 * k * r - h * r) * S**4 - c * r * S**2 - g * S**3
                    sync_expected = identity[i, j].item() * dnum + p[i, j].item() * c * S**3 + pinvq[i, j].item() * g * r * S**2 - pq[i, j].item() * h * r * S**4
                    direct_sync = direct.substitute(sync)
                    assert_poly_equal(direct_sync, sync_expected, (n, q, i, j, "synchronous_shift"))
                    counts["homogeneous_shift_entries"] += 1
                    assert pq[i, j] == int(j == imq)
                    assert pinvq[i, j] == int(j == ipq)
                    counts["shift_orientation_entries"] += 2

                    if q == 1:
                        collision = identity[i, j].item() * dnum + p[i, j].item() * (c * S**3 - h * r * S**4) + pinvq[i, j].item() * g * r * S**2
                    elif q == n - 1:
                        collision = identity[i, j].item() * dnum + p[i, j].item() * (c * S**3 + g * r * S**2) - pq[i, j].item() * h * r * S**4
                    elif 2 * q == n:
                        collision = identity[i, j].item() * dnum + p[i, j].item() * c * S**3 + pq[i, j].item() * (g * r * S**2 - h * r * S**4)
                    else:
                        collision = None
                    if collision is not None:
                        assert_poly_equal(direct_sync, collision, (n, q, i, j, "collision"))
                        counts["collision_combination_entries"] += 1

        # Exact Fourier orientation checks in the root-of-unity quotient ring.
        for m in range(n):
            for i in range(n):
                assert (m * ((i - 1) % n)) % n == (-m + m * i) % n
                counts["origin_fourier_monomial_relations"] += 1

        # Independent sparse determinant enumeration of lambda I - (d I + c P).
        t, d, cc = [Poly.var(3, j) for j in range(3)]
        determinant = Poly.const(3, 0)
        nonzero_permutations = 0

        def expand(row, chosen, product):
            nonlocal determinant, nonzero_permutations
            if row == n:
                inversions = sum(chosen[i] > chosen[j] for i in range(n) for j in range(i + 1, n))
                determinant += (-1 if inversions % 2 else 1) * product
                nonzero_permutations += 1
                return
            for col, entry in ((row, t - d), ((row - 1) % n, -cc)):
                if col not in chosen:
                    expand(row + 1, chosen + [col], product * entry)

        expand(0, [], Poly.const(3, 1))
        assert nonzero_permutations == 2
        assert_poly_equal(determinant, (t - d)**n - cc**n, (n, "characteristic_polynomial"))
        counts["origin_characteristic_polynomials"] += 1
        derivative_boundary = determinant.diff(0).substitute({0: 0, 1: -cc})
        assert_poly_equal(derivative_boundary, n * cc**(n - 1), (n, "zero_algebraic_simplicity"))
        counts["boundary_zero_characteristic_derivatives"] += 1
        rank = exact_rank(p - identity)
        assert rank == n - 1
        counts["boundary_exact_ranks"] += 1
        if n % 2 == 0:
            alternating = np.array([(-1)**j for j in range(n)], dtype=np.int64)
            assert np.array_equal(p @ alternating, -alternating)
            assert np.array_equal((identity + p) @ alternating, np.zeros(n, dtype=np.int64))
            counts["nonuniform_zero_off_boundary_examples"] += 1
        n_records.append({"n": n, "q": list(range(1, n)), "rank_P_minus_I": rank, "nullity": n - rank, "determinant_nonzero_permutations": nonzero_permutations})

    # Universal one-variable identities, without a positive-state Fourier formula.
    a, k, c, g, h, r = [Poly.var(6, j) for j in range(6)]
    S = 1 + r
    d_numerator = (a - 2*k*r - h*r)*S**2-c*r-g*S
    simplified_numerator = -k*r*S**2-c*(1+2*r)
    equilibrium_numerator = a*S-(k+h)*r*S-(g-c)
    # This residual vanishes exactly when the P02 nonzero-equilibrium relation
    # a=(k+h)r+(g-c)/(1+r) holds; no division at r=0 is performed here.
    assert_poly_equal(d_numerator-simplified_numerator, equilibrium_numerator*S,
                      "equilibrium_diagonal_simplification")
    counts["equilibrium_diagonal_simplification_identities"] += 1
    scalar_numerator = (a*r-(k+h)*r**2)*S+(c-g)*r
    scalar_derivative_numerator = scalar_numerator.diff(5)*S-scalar_numerator
    row_sum_numerator = d_numerator+c*S+g*r-h*r*S**2
    assert_poly_equal(row_sum_numerator, scalar_derivative_numerator,
                      "row_sum_equals_scalar_derivative")
    counts["row_sum_scalar_derivative_identities"] += 1
    assert_poly_equal((c-h*r*S).substitute({2: h*r*S}), 0,
                      "q1_exact_coefficient_cancellation")
    assert_poly_equal((g*r-h*r*S**2).substitute({3: h*S**2}), 0,
                      "even_half_exact_coefficient_cancellation")
    counts["generic_zero_coefficient_cancellation_identities"] += 2

    cancellation_examples = []
    examples = [("q1_C_equals_H", 5, 1, [Fraction(5, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(1)]),
                ("even_half_G_equals_H", 6, 3, [Fraction(7, 2), Fraction(1), Fraction(1), Fraction(4), Fraction(1)])]
    for label, n, q, parameters in examples:
        a, k, c, g, h = parameters
        r = Fraction(1)
        s = 1+r
        d = a-2*k*r-c*r/s**2-g/s-h*r
        C, G, H = c/s, g*r/s**2, h*r
        assert a*r-(k+h)*r*r+(c-g)*r/s == 0
        assert d == -k*r-c*(1+2*r)/s**2
        if q == 1:
            assert C-H == 0
        else:
            assert G-H == 0
        for i in range(n):
            im, ipq, imq = (i-1)%n, (i+q)%n, (i-q)%n
            for j in range(n):
                di, dm, dpq, dmq = int(j==i), int(j==im), int(j==ipq), int(j==imq)
                # Quotient and product rules applied to each identified variable.
                direct = a*di-2*k*r*di+c*(dm*s-r*di)/s**2-g*(di*s-r*dpq)/s**2-h*(di*r+r*dmq)
                if q == 1:
                    combined = d*di+(C-H)*dm+G*dpq
                else:
                    combined = d*di+C*dm+(G-H)*dmq
                assert direct == combined
                counts["named_cancellation_matrix_entries"] += 1
        cancellation_examples.append({"name": label, "n": n, "q": q, "r": str(r),
                                      "parameters_a_k_c_g_h": [str(v) for v in parameters],
                                      "d_C_G_H": [str(v) for v in [d, C, G, H]],
                                      "positive_synchronous_equilibrium": True,
                                      "cancelled_coefficient": "C-H=0" if q==1 else "G-H=0",
                                      "all_exact_matrix_entries_pass": True})
    counts["named_positive_equilibrium_cancellation_examples"] += len(examples)

    return {"status": "PASS", "arithmetic": "exact integer sparse polynomials and Fraction Gaussian elimination", "counts": dict(counts), "per_n": n_records, "cancellation_examples": cancellation_examples, "identities": {"general": "Direct canonical common-denominator quotient differentiation equals additive Kronecker Jacobian at every entry.", "origin": "J(0)=(a-g)I+cP", "characteristic_polynomial": "det(lambda I-J(0))=(lambda-a+g)^n-c^n", "origin_eigenvalues": "lambda_m=a-g+c exp(-2 pi i m/n); root-of-unity shift orientation checked exactly", "zero_derivative_at_mu_0": "chi'(0)=n c^(n-1)>0", "boundary_geometric_multiplicity": "rank(P-I)=n-1, so kernel dimension=1", "homogeneous": "J=dI+CP+GP^(-q)-HP^q; generic symbolic r, denominator multiplier (1+r)^4", "spectral_abscissa_certificate": "For c>0, Re(lambda_m)<=a-g+c; equality iff the unit root exp(-2 pi i m/n)=1, hence m=0. This elementary inequality is proof-level mathematics, not a floating test.", "nonuniform_zero_off_boundary": "Even n: at a-g=c, the alternating mode m=n/2 has zero eigenvalue; this is away from mu=0.", "equilibrium_diagonal_simplification": "[d-(-kr-c(1+2r)/(1+r)^2)](1+r)^2=[a(1+r)-(k+h)r(1+r)-(g-c)](1+r)", "row_sum_identity": "d+C+G-H = derivative_r[ar-(k+h)r^2+(c-g)r/(1+r)]", "generic_cancellation_q1": "C-H=0 if c=hr(1+r)", "generic_cancellation_even_half": "G-H=0 if g=h(1+r)^2"}}


def vector_field(x, params, q):
    a, k, c, g, h = params
    return a*x-k*x*x+c*np.roll(x, 1)/(1+x)-g*x/(1+np.roll(x, -q))-h*x*np.roll(x, q)


def analytic_jacobian(x, params, q):
    a, k, c, g, h = params
    n = len(x)
    mat = np.zeros((n, n))
    for i in range(n):
        im, ipq, imq = (i-1)%n, (i+q)%n, (i-q)%n
        mat[i, i] += a-2*k*x[i]-c*x[im]/(1+x[i])**2-g/(1+x[ipq])-h*x[imq]
        mat[i, im] += c/(1+x[i])
        mat[i, ipq] += g*x[i]/(1+x[ipq])**2
        mat[i, imq] += -h*x[i]
    return mat


def floating_checks():
    seed = 20260927
    rng = np.random.default_rng(seed)
    records = []
    step_multiplier = 1e-5
    tolerance = 1e-7
    worst_scaled = (0, None)
    worst_absolute = (0, None)
    fd_entries = 0
    sync_entries = 0
    sync_worst = 0.0
    for n in range(5, 11):
        p = shift(n).astype(float)
        for q in range(1, n):
            params = rng.uniform(0.2, 2.3, size=5)
            eq_r = 0.4
            eq_params = params.copy()
            eq_params[0] = (params[1] + params[4])*eq_r + 0.4
            eq_params[3] = params[2] + 0.4*(1+eq_r)
            states = [("origin", np.zeros(n), params),
                      ("sync_negative", np.full(n, -0.65), params),
                      ("sync_positive_low", np.full(n, 0.25), params),
                      ("sync_positive_high", np.full(n, 1.5), params),
                      ("sync_equilibrium", np.full(n, eq_r), eq_params),
                      ("random_domain", rng.uniform(-0.7, 2.0, size=n), params),
                      ("random_positive", rng.uniform(0.05, 3.0, size=n), params),
                      ("random_mixed", rng.uniform(-0.8, 0.6, size=n), params)]
            for label, x, par in states:
                analytic = analytic_jacobian(x, par, q)
                numerical = np.zeros_like(analytic)
                steps = step_multiplier*np.maximum(1.0, np.abs(x))
                for j in range(n):
                    xp, xm = x.copy(), x.copy()
                    xp[j] += steps[j]
                    xm[j] -= steps[j]
                    numerical[:, j] = (vector_field(xp, par, q)-vector_field(xm, par, q))/(2*steps[j])
                error = np.abs(analytic-numerical)
                scaled = error/(1+np.maximum(np.abs(analytic), np.abs(numerical)))
                absmax, scaledmax = float(error.max()), float(scaled.max())
                assert scaledmax <= tolerance, (n, q, label, scaledmax)
                locator = {"n": n, "q": q, "state": label}
                if absmax > worst_absolute[0]:
                    worst_absolute = (absmax, locator | {"entry": list(np.unravel_index(int(error.argmax()), error.shape))})
                if scaledmax > worst_scaled[0]:
                    worst_scaled = (scaledmax, locator | {"entry": list(np.unravel_index(int(scaled.argmax()), scaled.shape))})
                fd_entries += n*n
                record = locator | {"parameters_a_k_c_g_h": par.tolist(), "parameters_hex": [v.hex() for v in par], "x": x.tolist(), "x_hex": [v.hex() for v in x], "steps": steps.tolist(), "max_absolute_error": absmax, "max_scaled_error": scaledmax}
                if label.startswith("sync") or label == "origin":
                    r = float(x[0])
                    s = 1+r
                    a, k, c, g, h = par
                    d = a-2*k*r-c*r/s**2-g/s-h*r
                    C, G, H = c/s, g*r/s**2, h*r
                    homogeneous = d*np.eye(n)+C*p+G*np.linalg.matrix_power(p, n-q)-H*np.linalg.matrix_power(p, q)
                    residual = float(np.max(np.abs(analytic-homogeneous)))
                    assert residual < 1e-12
                    sync_worst = max(sync_worst, residual)
                    sync_entries += n*n
                    record["homogeneous_matrix_residual"] = residual
                if label == "sync_equilibrium":
                    eq_resid = float(np.max(np.abs(vector_field(x, par, q))))
                    assert eq_resid < 1e-12
                    record["equilibrium_residual"] = eq_resid
                records.append(record)

    origin_records = []
    eig_worst = 0.0
    origin_count = 0
    for n in range(5, 11):
        p = shift(n)
        theta = 2*np.pi*np.arange(n)/n
        for label, a, c, g in [("stable", 1.3, .7, 3.0), ("boundary", 1.3, .7, 2.0), ("unstable", 1.3, .7, 1.0), ("even_nonuniform_zero_or_odd_control", 2.0, .7, 1.3)]:
            eigenvalues = a-g+c*np.exp(-1j*theta)
            jacobian = (a-g)*np.eye(n)+c*p
            local_worst = 0.0
            for m in range(n):
                v = np.exp(1j*theta[m]*np.arange(n))/np.sqrt(n)
                err = float(np.max(np.abs(jacobian@v-eigenvalues[m]*v)))
                local_worst = max(local_worst, err)
                origin_count += 1
            assert local_worst < 1e-13
            eig_worst = max(eig_worst, local_worst)
            mu = a+c-g
            assert abs(float(np.max(eigenvalues.real))-mu) < 1e-14
            assert int(np.argmax(eigenvalues.real)) == 0
            gap = float(eigenvalues[0].real-np.max(eigenvalues[1:].real))
            assert gap > 0
            if label == "boundary":
                assert abs(eigenvalues[0]) < 1e-14
                assert np.max(eigenvalues[1:].real) < 0
            if label == "even_nonuniform_zero_or_odd_control" and n % 2 == 0:
                assert abs(eigenvalues[n//2]) < 1e-14
            origin_records.append({"n": n, "label": label, "a_c_g": [a, c, g], "mu": mu, "eigenrelation_max_residual": local_worst, "spectral_abscissa": float(np.max(eigenvalues.real)), "unique_maximizer": 0, "gap_to_next_real_part": gap, "eigenvalues_real_imag": [[float(v.real), float(v.imag)] for v in eigenvalues]})

    return {"status": "PASS", "secondary_only": True, "rng": "numpy.random.default_rng (PCG64)", "seed": seed, "finite_difference_scheme": "centered; step_j=1e-5*max(1,abs(x_j))", "scaled_error_definition": "abs(J_analytic-J_FD)/(1+max(abs(J_analytic),abs(J_FD))) entrywise", "scaled_tolerance": tolerance, "state_count": len(records), "finite_difference_entry_count": fd_entries, "homogeneous_entry_count": sync_entries, "origin_eigenrelation_count": origin_count, "origin_spectral_cases": len(origin_records), "worst_fd_absolute_error": worst_absolute[0], "worst_fd_absolute_location": worst_absolute[1], "worst_fd_scaled_error": worst_scaled[0], "worst_fd_scaled_location": worst_scaled[1], "worst_homogeneous_matrix_residual": sync_worst, "worst_origin_eigenrelation_residual": eig_worst, "state_records": records, "origin_records": origin_records}


def main():
    output_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_directory", nargs="?", type=Path,
                        default=output_dir.parent.parent / "p03_work" / "cyclic_network_project",
                        help="project containing 00_canonical_model.tex and 01_notation_and_assumptions.tex")
    root = parser.parse_args().project_directory.expanduser().resolve()
    source_paths = ["00_canonical_model.tex", "01_notation_and_assumptions.tex"]
    for name in source_paths:
        if not (root / name).is_file():
            parser.error(f"missing project source: {root / name}")
    exact = exact_checks()
    floating = floating_checks()
    report = {"status": "PASS", "scope": "P03 DM general Jacobian, synchronous matrix, and origin only; no positive-state Fourier spectrum or normality theorem", "project_directory": str(root), "software": {"python": sys.version, "python_executable": sys.executable, "numpy": np.__version__, "platform": platform.platform(), "sympy": "not required; original validation environment had no SymPy installed"}, "source_sha256": {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in source_paths}, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "exact": exact, "floating": floating, "failures": []}
    (output_dir / "report.json").write_text(json.dumps(report, indent=2, default=int) + "\n")
    compact = {"status": report["status"], "exact_counts": exact["counts"], "floating": {k: v for k, v in floating.items() if k not in {"state_records", "origin_records"}}, "report": str(output_dir / "report.json")}
    (output_dir / "summary.json").write_text(json.dumps(compact, indent=2, default=int) + "\n")
    print(json.dumps(compact, indent=2, default=int))


if __name__ == "__main__":
    main()
