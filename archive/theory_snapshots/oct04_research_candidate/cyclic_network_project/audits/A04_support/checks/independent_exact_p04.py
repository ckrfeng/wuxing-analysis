#!/usr/bin/env python3
"""Independent finite P04 corroboration; Python standard library only.

No project executable is imported or run. All arithmetic is exact Fraction
arithmetic. A custom Q[z]/Phi_n(z) field implements primitive roots of unity.
The input P04 is read ONLY to authenticate its SHA-256. This is corroboration of
finitely many instances, not a proof of arbitrary n or nonlinear conclusions.
"""
from fractions import Fraction as F
from math import gcd
from collections import defaultdict
from pathlib import Path
import argparse
import hashlib
import json
import platform
import sys
import time


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return trim(c)


def pneg(a): return [-v for v in a]


def pmul(a, b):
    c = [F(0)] * max(0, len(a) + len(b) - 1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b):
                if v: c[i+j] += u*v
    return trim(c)


def pdiv(a, b):
    a, b = trim(a), trim(b)
    if not b: raise ZeroDivisionError
    q = [F(0)] * max(0, len(a)-len(b)+1)
    while len(a) >= len(b):
        k = len(a)-len(b)
        v = a[-1]/b[-1]
        q[k] = v
        for j, u in enumerate(b): a[j+k] -= v*u
        a = trim(a)
    return trim(q), a


PHI = {}
def cyclotomic(n):
    if n not in PHI:
        p = [F(-1)] + [F(0)] * (n-1) + [F(1)]
        for d in range(1, n):
            if n % d == 0:
                p, rem = pdiv(p, cyclotomic(d))
                assert not rem
        PHI[n] = tuple(p)
    return PHI[n]


class Field:
    def __init__(self, n):
        self.n, self.phi = n, cyclotomic(n)
        self.degree = len(self.phi)-1
        self.zero = E(self, ())
        self.one = E(self, (F(1),))
        self.roots = [self.one]
        z = E(self, (F(0), F(1)))
        for k in range(1, n): self.roots.append(self.roots[-1]*z)
        assert self.roots[-1]*z == self.one

    def __call__(self, v):
        if isinstance(v, E):
            assert v.field is self
            return v
        return E(self, (F(v),))

    def root(self, k): return self.roots[k % self.n]


class E:
    def __init__(self, field, p):
        self.field = field
        self.p = tuple(pdiv(p, field.phi)[1]) if len(p) > field.degree else tuple(trim(p))

    def __bool__(self): return bool(self.p)
    def __eq__(self, b):
        b = self.field(b)
        return self.p == b.p
    def __hash__(self): return hash(self.p)
    def __add__(self, b):
        b = self.field(b)
        return E(self.field, padd(self.p, b.p))
    __radd__ = __add__
    def __neg__(self): return E(self.field, pneg(self.p))
    def __sub__(self, b): return self + (-self.field(b))
    def __rsub__(self, b): return self.field(b) + (-self)
    def __mul__(self, b):
        b = self.field(b)
        return E(self.field, pmul(self.p, b.p))
    __rmul__ = __mul__
    def inv(self):
        if not self: raise ZeroDivisionError
        a, b = list(self.field.phi), list(self.p)
        s0, s1 = [], [F(1)]
        while b:
            q, r = pdiv(a, b)
            a, b = b, r
            s0, s1 = s1, padd(s0, pneg(pmul(q, s1)))
        assert len(a) == 1
        return E(self.field, [v/a[0] for v in s0])
    def __truediv__(self, b): return self * self.field(b).inv()
    def conj(self):
        return sum((v*self.field.root(-k) for k, v in enumerate(self.p)), self.field.zero)
    def serial(self): return [str(v) for v in self.p] or ['0']


def eye(n): return [[F(i == j) for j in range(n)] for i in range(n)]
def transpose(a): return [list(row) for row in zip(*a)]
def mm(a, b):
    bt = transpose(b)
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def charpoly(a):
    """Faddeev-LeVerrier: independent rational matrix characteristic polynomial."""
    n = len(a)
    b = eye(n)
    out = [F(1)]
    for k in range(1, n+1):
        b = mm(a, b)
        c = -sum(b[i][i] for i in range(n))/k
        out.append(c)
        for i in range(n): b[i][i] += c
    assert all(not v for row in b for v in row)  # Cayley-Hamilton residual
    return out


def rank_field(a, field):
    a = [[field(v) for v in row] for row in a]
    nr, nc, rank = len(a), len(a[0]), 0
    for col in range(nc):
        pivot = next((r for r in range(rank, nr) if a[r][col]), None)
        if pivot is None: continue
        a[rank], a[pivot] = a[pivot], a[rank]
        iv = a[rank][col].inv()
        a[rank] = [v*iv for v in a[rank]]
        for r in range(rank+1, nr):
            fac = a[r][col]
            if fac:
                a[r] = [v-fac*w for v, w in zip(a[r], a[rank])]
        rank += 1
        if rank == nr: break
    return rank


COUNTS = defaultdict(int)
def check(ok, name):
    COUNTS[name] += 1
    if not ok: raise AssertionError(name)


def cycles(n, q):
    unseen = set(range(n))
    out = []
    while unseen:
        start = min(unseen)
        cycle, j = [], start
        while j in unseen:
            unseen.remove(j)
            cycle.append(j)
            j = (j+q) % n
        assert j == start
        out.append(cycle)
    return out


def coefficients(p):
    a, k, c, g, h, x = (p[name] for name in ('a','k','c','g','h','x'))
    s = 1+x
    return (a-2*k*x-c*x/s**2-g/s-h*x, c/s, g*x/s**2, h*x)


def assemble(n, q, d, C, G, H):
    """Accumulate at node indices, with no Fourier formula involved."""
    j = [[F(0)]*n for _ in range(n)]
    for row in range(n):
        for col, value in ((row,d), ((row-1)%n,C), ((row+q)%n,G), ((row-q)%n,-H)):
            j[row][col] += value
    return j


CASES = [
    ('origin_nonhyperbolic_control', dict(a='2', k='1', c='1', g='5/2', h='1', x='0')),
    ('positive_equilibrium_repeated_q1', dict(a='2', k='1', c='4', g='4', h='1', x='1')),
    ('negative_nonstationary', dict(a='2', k='1', c='3', g='5', h='2', x='-1/2')),
    ('positive_nonstationary', dict(a='3/2', k='5/4', c='7/3', g='11/5', h='13/7', x='2/3')),
    ('positive_equilibrium_C_equals_H', dict(a='3', k='1', c='2', g='4', h='1', x='1')),
    ('negative_C_plus_G_cancellation', dict(a='2', k='1', c='1', g='1', h='1', x='-1/2')),
    ('negative_nonzero_equilibrium', dict(a='1', k='1', c='1', g='2', h='1', x='-1/2')),
]
TARGETED = [
    (6,2,'positive_equilibrium_pure_imaginary_boundary',dict(a='17/4',k='1',c='1',g='1',h='13/4',x='1')),
    (5,2,'positive_equilibrium_zero_singleton',dict(a='3',k='1',c='1',g='33/8',h='1',x='1/4')),
    (6,3,'positive_equilibrium_repeated_nonreal',dict(a='4',k='1',c='4',g='8',h='1',x='1')),
    (6,5,'negative_all_one_last_offset_cancellation',dict(a='1',k='1',c='1',g='1',h='1',x='-1/2')),
    (5,2,'audit_named_positive_equilibrium',dict(a='5/2',k='1',c='1',g='2',h='1',x='1')),
    (6,2,'audit_named_positive_equilibrium',dict(a='5/2',k='1',c='1',g='2',h='1',x='1')),
    (6,3,'audit_named_positive_equilibrium',dict(a='5/2',k='1',c='1',g='2',h='1',x='1')),
    (7,1,'audit_named_positive_equilibrium',dict(a='5/2',k='1',c='1',g='2',h='1',x='1')),
    (8,4,'audit_named_positive_equilibrium',dict(a='5/2',k='1',c='1',g='2',h='1',x='1')),
    (6,5,'audit_named_positive_equilibrium',dict(a='5/2',k='1',c='1',g='2',h='1',x='1')),
    (5,2,'audit_named_negative_nonstationary',dict(a='2',k='1',c='4',g='4',h='1',x='-1/2')),
    (6,3,'audit_named_half_offset_cancellation',dict(a='7/2',k='1',c='1',g='4',h='1',x='1')),
]


def field_checks(n, field):
    # U=sqrt(n)Q avoids square roots. U*U=UU*=nI exactly certifies both Q identities.
    for row in range(n):
        for col in range(n):
            left = sum((field.root((col-row)*j) for j in range(n)), field.zero)
            right = sum((field.root((row-col)*m) for m in range(n)), field.zero)
            check(left == n*(row == col), 'DFT_UstarU_entries')
            check(right == n*(row == col), 'DFT_UUstar_entries')
    for m in range(n):
        for shift in range(-2*n, 2*n+1):
            for j in range(n):
                check(field.root(m*((j-shift)%n)) == field.root(-m*shift)*field.root(m*j), 'integer_shift_phases')


def matrix_checks(n, q, name, p, field):
    d,C,G,H = coefficients(p)
    j = assemble(n,q,d,C,G,H)
    lams = [d+C*field.root(-m)+G*field.root(q*m)-H*field.root(-q*m) for m in range(n)]
    for m, lam in enumerate(lams):
        for row in range(n):
            direct = sum((j[row][col]*field.root(m*col) for col in range(n)), field.zero)
            check(direct == lam*field.root(m*row), 'matrix_eigenvector_entries')
        check(lams[-m % n] == lam.conj(), 'conjugate_eigenvalues')
        cos1 = (field.root(m)+field.root(-m))/2
        cosq = (field.root(q*m)+field.root(-q*m))/2
        isin1 = (field.root(m)-field.root(-m))/2
        isinq = (field.root(q*m)-field.root(-q*m))/2
        check((lam+lam.conj())/2 == d+C*cos1+(G-H)*cosq, 'real_dispersion')
        check((lam-lam.conj())/2 == -C*isin1+(G+H)*isinq, 'imaginary_dispersion_times_i')
        if q == 1:
            check(lam == d+(C-H)*field.root(-m)+G*field.root(m), 'q1_collision_formula')
        if q == n-1:
            check(lam == d+(C+G)*field.root(-m)-H*field.root(m), 'last_offset_collision_formula')
        if 2*q == n:
            check(lam == d+C*field.root(-m)+(G-H)*((-1)**m), 'half_offset_collision_formula')
    check(mm(j,transpose(j)) == mm(transpose(j),j), 'rational_matrix_normality')
    for row in range(n):
        for col in range(n):
            reconstructed = sum((lams[m]*field.root(m*(row-col)) for m in range(n)),field.zero)/n
            check(reconstructed == j[row][col], 'Q_Lambda_Qstar_entries')
    cp = charpoly(j)
    prod = [field.one]
    for lam in lams:
        out = [field.zero] * (len(prod)+1)
        for index, v in enumerate(prod):
            out[index] += v
            out[index+1] -= lam*v
        prod = out
    for index, v in enumerate(cp): check(prod[index] == v, 'characteristic_coefficients')
    x,a,k,c,g,h = (p[key] for key in ('x','a','k','c','g','h'))
    s, A = 1+x, k+h
    scalar = a*x-A*x*x+(c-g)*x/s
    derivative = a-2*A*x+(c-g)/s**2
    check(lams[0] == d+C+G-H, 'zero_mode')
    check(lams[0] == derivative, 'synchronous_derivative')
    check(all(sum(row) == derivative for row in j), 'rational_row_sum')
    if n % 2 == 0: check(lams[n//2] == d-C+(G-H)*((-1)**q), 'even_singleton')
    if scalar == 0 and x != 0:
        check(d == -k*x-c/s-c*x/s**2, 'equilibrium_d_simplification')
        check(lams[0] == -x*(A+(c-g)/s**2), 'equilibrium_zero_mode_first')
        check(lams[0] == x*(a-A-2*A*x)/s, 'equilibrium_zero_mode_second')
    groups = defaultdict(list)
    for m, lam in enumerate(lams): groups[lam].append(m)
    if x == 0:
        check(G == H == 0 and C == c and d == a-g, 'origin_coefficients')
        check(len(groups) == n, 'origin_simple_spectrum')
    if name == 'negative_nonzero_equilibrium':
        check(scalar == 0 and x < 0 and G < 0 and H < 0, 'negative_equilibrium_signed_coefficients')
    rank_checks = []
    # Exact elimination for all q=1 repeated-real examples, all n/2 offset
    # cancellations, and the explicit hyperbolicity counterexample.
    do_rank = ((name == 'positive_equilibrium_repeated_q1' and (q == 1 or 2*q == n))
               or (n == 6 and q == 2 and name == 'origin_nonhyperbolic_control')
               or name in ('positive_equilibrium_pure_imaginary_boundary','positive_equilibrium_zero_singleton','positive_equilibrium_repeated_nonreal'))
    if do_rank:
        for lam, labels in groups.items():
            a_minus_lam = [[field(v)-(lam if row == col else 0) for col,v in enumerate(values)] for row, values in enumerate(j)]
            nullity = n-rank_field(a_minus_lam, field)
            check(nullity == len(labels), 'direct_eigenspace_nullities')
            rank_checks.append(dict(labels=labels, nullity=nullity))
    if name == 'positive_equilibrium_repeated_q1' and q == 1:
        check(all(lam == lam.conj() for lam in lams), 'repeated_example_all_real')
        for m in range(1,(n+1)//2):
            check(lams[m] == lams[n-m], 'repeated_example_pair_equalities')
    if name == 'origin_nonhyperbolic_control' and n == 6:
        check(all(lam != 0 for lam in lams), 'invertible_nonhyperbolic_nonzero_values')
        check(lams[1]+lams[1].conj() == 0 and lams[1] != 0, 'invertible_nonhyperbolic_pure_imaginary')
    if name == 'positive_equilibrium_pure_imaginary_boundary':
        check(scalar == 0 and x > 0, 'positive_boundary_equilibrium')
        check(all(lam != 0 for lam in lams), 'positive_boundary_invertible')
        check([(lam+lam.conj())/2 for lam in lams] == [field(F(v)) for v in ('-17/4','0','-1/2','-21/4','-1/2','0')], 'positive_boundary_exact_real_parts')
        check(lams[1]*lams[1] == F(-27,4) and lams[5] == -lams[1], 'positive_boundary_exact_imaginary_pair')
    if name == 'positive_equilibrium_zero_singleton':
        check(scalar == 0 and x > 0 and lams[0] == 0, 'zero_singleton_positive_equilibrium')
        check(C > 0 and G-H > 0 and d+C+G-H == 0, 'zero_singleton_strict_cosine_bound_coefficients')
        check(all(field.root(m) != 1 for m in range(1,n)), 'zero_singleton_nonzero_labels_nontrivial_roots')
    if name == 'positive_equilibrium_repeated_nonreal':
        check(scalar == 0 and x > 0, 'repeated_nonreal_positive_equilibrium')
        check(lams[1] == lams[2] and lams[4] == lams[5] and lams[1] != lams[4], 'repeated_nonreal_nonconjugate_label_coincidences')
        check(lams[0] == -1 and lams[3] == -7 and (lams[1]+4)*(lams[1]+4) == -3, 'repeated_nonreal_exact_values')
    if name == 'negative_all_one_last_offset_cancellation':
        check((d,C,G,H) == (F(5,2),F(2),F(-2),F(-1,2)), 'negative_all_one_exact_coefficients')
        check(all(lams[m] == F(5,2)+F(1,2)*field.root(m) for m in range(n)), 'negative_all_one_cancelled_spectrum')
    if name == 'audit_named_positive_equilibrium':
        check(scalar == 0 and x > 0, 'audit_named_positive_equilibrium')
        check((d,C,G,H) == (F(-7,4),F(1,2),F(1,2),F(1)), 'audit_named_positive_exact_coefficients')
    if name == 'audit_named_negative_nonstationary':
        check(scalar != 0 and x < 0 and G < 0 and H < 0, 'audit_named_negative_state')
        check((d,C,G,H) == (F(7,2),F(8),F(-8),F(-1,2)), 'audit_named_negative_exact_coefficients')
    if name == 'audit_named_half_offset_cancellation':
        check(scalar == 0 and G == H, 'audit_named_half_offset_cancellation_equilibrium')
        check(all(lams[m] == F(-7,4)+F(1,2)*field.root(-m) for m in range(n)), 'audit_named_half_offset_cancelled_spectrum')
    check(all(v > 0 for key,v in p.items() if key != 'x') and x > -1, 'canonical_parameter_domain')
    return dict(n=n,q=q,case=name,parameters={key:str(v) for key,v in p.items()},
                coefficients=dict(zip(('d','C','G','H'),map(str,(d,C,G,H)))),
                equilibrium=(scalar == 0), scalar_field_value=str(scalar),
                characteristic_polynomial_descending=list(map(str,cp)),
                eigenvalue_groups=[dict(labels=labels, cyclotomic_coefficients=lam.serial(),
                                       real=(lam == lam.conj())) for lam,labels in groups.items()],
                direct_nullity_checks=rank_checks)


def symbolic_checks():
    """Formal multivariate polynomial checks after clearing denominators.

    Each monomial is a tuple of powers of (a,k,c,g,h,x). This routine has
    no point evaluations and uses no algebra package.
    """
    class M:
        def __init__(self, terms): self.t = {mon:F(co) for mon,co in terms.items() if co}
        def __add__(self, other):
            if not isinstance(other,M): other = M({(0,)*6:other})
            d = dict(self.t)
            for mon,co in other.t.items(): d[mon] = d.get(mon,F(0))+co
            return M(d)
        __radd__ = __add__
        def __neg__(self): return M({mon:-co for mon,co in self.t.items()})
        def __sub__(self, other): return self + (-other)
        def __rsub__(self, other): return -self + other
        def __mul__(self, other):
            if not isinstance(other,M): other = M({(0,)*6:other})
            d = defaultdict(F)
            for m,c in self.t.items():
                for n,e in other.t.items(): d[tuple(i+j for i,j in zip(m,n))] += c*e
            return M(d)
        __rmul__ = __mul__
        def __pow__(self,n):
            out=M({(0,)*6:1})
            for _ in range(n): out=out*self
            return out
    a,k,c,g,h,x = [M({tuple(int(i==j) for j in range(6)):1}) for i in range(6)]
    s,A = 1+x,k+h
    D = (a-2*k*x-h*x)*s**2-c*x-g*s  # s^2 d
    C,G,H = c*s,g*x,h*x*s**2        # s^2 times each coefficient
    B = (a-A*x)*s+c-g              # s B(x), zero at nonzero equilibrium
    residuals = {
        'row_sum_equals_scalar_derivative':D+C+G-H-((a-2*A*x)*s**2+c-g),
        'equilibrium_d_reduction_mod_B':D-(-k*x*s**2-c*s-c*x)-s*B,
        'equilibrium_zero_mode_first_mod_B':D+C+G-H+x*(A*s**2+c-g)-s*B,
        'equilibrium_zero_mode_second_mod_B':D+C+G-H-x*s*(a-A-2*A*x)-B,
    }
    for name,residual in residuals.items(): check(not residual.t, 'symbolic_'+name)
    return {name:'zero polynomial' for name in residuals}


def main():
    start = time.monotonic()
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--p04-source', type=Path, help='Explicit authenticated P04 TeX source path.')
    parser.add_argument('--authenticate-only', action='store_true', help='Verify the source SHA-256 and stop before any algebraic computations; requires no compiler or numerical library.')
    args = parser.parse_args()
    candidates = ([args.p04_source.expanduser()] if args.p04_source else [
        here.parents[2]/'input/cyclic_network_project/proofs/P04_arbitrary_nq_fourier_spectrum.tex',
        here.parents[2]/'proofs/P04_arbitrary_nq_fourier_spectrum.tex',
    ])
    source = next((candidate.resolve() for candidate in candidates if candidate.is_file()), None)
    if source is None:
        parser.error('P04 source not found. Pass --p04-source PATH. Tried: '+', '.join(map(str,candidates)))
    expected = 'ab80f695b3e20c852c572b7b174ecaf9964eac1aba62e3e55b2b4d3e60754e0c'
    actual = hashlib.sha256(source.read_bytes()).hexdigest()
    check(actual == expected, 'authenticated_P04_sha256')
    if args.authenticate_only:
        print(json.dumps(dict(status='PASS',source=str(source),sha256=actual,
                              method='Python standard-library SHA-256; no compiler or algebraic computations'),indent=2))
        return
    cases = [(name,{k:F(v) for k,v in p.items()}) for name,p in CASES]
    targeted = [(n,q,name,{k:F(v) for k,v in p.items()}) for n,q,name,p in TARGETED]
    symbolic = symbolic_checks()
    results, cycle_results = [], []
    for n in range(5,11):
        field = Field(n)
        field_checks(n, field)
        for q in range(1,n):
            cy = cycles(n,q)
            kap = gcd(n,q)
            check(len(cy) == kap, 'step_q_cycle_count')
            check(all(len(v) == n//kap for v in cy), 'step_q_cycle_lengths')
            check(all(len({j % kap for j in v}) == 1 for v in cy), 'step_q_residue_classes')
            check(sorted(sorted(v) for v in cycles(n,-q)) == sorted(sorted(v) for v in cy), 'reverse_step_same_partition')
            cycle_results.append(dict(n=n,q=q,gcd=kap,cycles=cy))
            for name,p in cases: results.append(matrix_checks(n,q,name,p,field))
        print('Completed exact checks for n=%d' % n, flush=True)
    for n,q,name,p in targeted:
        results.append(matrix_checks(n,q,name,p,Field(n)))
    report = dict(status='PASS', method='stdlib Fraction; custom cyclotomic field; direct modular-index matrix assembly; Faddeev-LeVerrier characteristic polynomial; selected exact nullspace elimination',
                  input_sha256=actual, input_source=str(source), python=sys.version, platform=platform.platform(),
                  counts=dict(COUNTS), total_assertions=sum(COUNTS.values()),
                  tested_pairs=len(cycle_results), tested_matrices=len(results),
                  eigenvalue_occurrences=sum(r['n'] for r in results),
                  cyclotomic_polynomials={str(n):list(map(str,cyclotomic(n))) for n in range(5,11)},
                  symbolic_checks=symbolic,
                  limitations=['Finite n=5,...,10 and seven rational parameter/state families, plus twelve targeted matrices, do not establish universal spectral quantifiers; four separate formal polynomial checks are identities.',
                               'No numerical eigensolver or matrix-exponential tests were used.',
                               'Semigroup norm and nonlinear stability statements require the written analytic audit; these checks certify the finite-instance spectral and normality ingredients.',
                               'No P05 mode selection reduction or P11-P13 analysis is performed.',
                               'No attached executable/checker is imported or executed.'],
                  step_q_cycles=cycle_results, matrices=results,
                  wall_seconds=round(time.monotonic()-start,3))
    output = here/'independent_exact_p04_results.json'
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('status','tested_pairs','tested_matrices','eigenvalue_occurrences','total_assertions','wall_seconds')},indent=2))
    print('Results: '+str(output))


if __name__ == '__main__': main()
