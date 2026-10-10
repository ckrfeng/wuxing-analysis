#!/usr/bin/env python3
"""Independent exact P03 check; standard library only, no spectral calculations.

The oracle is forward automatic differentiation of the original canonical
field, not the asserted Jacobian. Fractions and full derivative vectors make
every check exact. Finite checks corroborate, rather than prove, identities.
"""
from fractions import Fraction as Q
from collections import Counter
import json
from pathlib import Path


class Dual:
    def __init__(self, value, gradient):
        self.value = Q(value)
        self.gradient = tuple(map(Q, gradient))

    def promote(self, other):
        return other if isinstance(other, Dual) else Dual(other, [0]*len(self.gradient))

    def __add__(self, other):
        other = self.promote(other)
        return Dual(self.value+other.value,
                    [a+b for a,b in zip(self.gradient, other.gradient)])
    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, [-a for a in self.gradient])

    def __sub__(self, other):
        return self + -self.promote(other)

    def __rsub__(self, other):
        return self.promote(other) + -self

    def __mul__(self, other):
        other = self.promote(other)
        return Dual(self.value*other.value,
                    [a*other.value+self.value*b
                     for a,b in zip(self.gradient, other.gradient)])
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.promote(other)
        assert other.value != 0
        return Dual(self.value/other.value,
                    [(a*other.value-self.value*b)/(other.value*other.value)
                     for a,b in zip(self.gradient, other.gradient)])

    def __rtruediv__(self, other):
        return self.promote(other) / self


def original_field(state, q, params):
    a,k,c,g,h = params
    n = len(state)
    return [a*state[i] - k*state[i]*state[i]
            + c*state[(i-1)%n]/(1+state[i])
            - g*state[i]/(1+state[(i+q)%n])
            - h*state[i]*state[(i-q)%n] for i in range(n)]


def automatic_jacobian(state, q, params):
    n = len(state)
    variables = [Dual(state[j], [int(j == k) for k in range(n)])
                 for j in range(n)]
    values = original_field(variables, q, params)
    return [list(v.gradient) for v in values], [v.value for v in values]


def asserted_jacobian(state, q, params):
    a,k,c,g,h = params
    n = len(state)
    matrix = [[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        xi = state[i]
        matrix[i][i] += (a-2*k*xi-c*state[(i-1)%n]/(1+xi)**2
                         -g/(1+state[(i+q)%n])-h*state[(i-q)%n])
        matrix[i][(i-1)%n] += c/(1+xi)
        matrix[i][(i+q)%n] += g*xi/(1+state[(i+q)%n])**2
        matrix[i][(i-q)%n] -= h*xi
    return matrix


def coefficients(r, params):
    a,k,c,g,h = params
    s = 1+r
    return a-2*k*r-c*r/s**2-g/s-h*r, c/s, g*r/s**2, h*r


def homogeneous_matrix(n, q, coef):
    d,C,G,H = coef
    return [[d*int(i==j)+C*int(j==(i-1)%n)
             +G*int(j==(i+q)%n)-H*int(j==(i-q)%n)
             for j in range(n)] for i in range(n)]


def reduced_collision_matrix(n, q, coef):
    d,C,G,H = coef
    terms = [(0,d)]
    if q == 1:
        terms += [(1,C-H),(-1,G)]
    elif q == n-1:
        terms += [(1,C+G),(-1,-H)]
    elif 2*q == n:
        terms += [(1,C),(n//2,G-H)]
    else:
        terms += [(1,C),(-q,G),(q,-H)]
    return [[sum((v for power,v in terms if j==(i-power)%n), Q(0))
             for j in range(n)] for i in range(n)]


def scalar_original(r, params):
    a,k,c,g,h = params
    return a*r-k*r*r+c*r/(1+r)-g*r/(1+r)-h*r*r


counts = Counter()
coverage = Counter()
worked = []


def check_case(n, q, state, params, family, equilibrium=False):
    assert n >= 5 and 1 <= q < n
    assert all(p > 0 for p in params)
    assert all(x > -1 for x in state)
    oracle, values = automatic_jacobian(state, q, params)
    asserted = asserted_jacobian(state, q, params)
    assert oracle == asserted, (family,n,q,state,params)
    counts['jacobian_cases'] += 1
    counts['jacobian_entries'] += n*n
    coverage[family] += 1
    # A nonconstant exact probe verifies receiving-row placement and shifts.
    z = [Q((-1)**j*(j+2),j+1) for j in range(n)]
    a,k,c,g,h = params
    for i,xi in enumerate(state):
        Di = a-2*k*xi-c*state[(i-1)%n]/(1+xi)**2-g/(1+state[(i+q)%n])-h*state[(i-q)%n]
        row_action = (Di*z[i]+c/(1+xi)*z[(i-1)%n]
                      +g*xi/(1+state[(i+q)%n])**2*z[(i+q)%n]
                      -h*xi*z[(i-q)%n])
        assert row_action == sum(oracle[i][j]*z[j] for j in range(n))
        counts['directional_rows'] += 1
    if len(set(state)) == 1:
        r = state[0]
        coef = coefficients(r,params)
        assert oracle == homogeneous_matrix(n,q,coef)
        assert oracle == reduced_collision_matrix(n,q,coef)
        counts['homogeneous_cases'] += 1
        counts['homogeneous_matrix_entries'] += n*n
        counts['reduced_matrix_entries'] += n*n
        scalar_dual = scalar_original(Dual(r,[1]),params)
        d,C,G,H = coef
        assert scalar_dual.gradient[0] == a-2*(k+h)*r+(c-g)/(1+r)**2
        assert scalar_dual.gradient[0] == d+C+G-H
        assert all(sum(row) == scalar_dual.gradient[0] for row in oracle)
        counts['row_sum_rows'] += n
        if r == 0:
            origin = [[(a-g)*int(i==j)+c*int(j==(i-1)%n)
                       for j in range(n)] for i in range(n)]
            assert oracle == origin
            assert all(v == 0 for v in values)
            counts['origin_cases'] += 1
            counts['origin_matrix_entries'] += n*n
        if equilibrium:
            assert r != 0
            assert all(v == 0 for v in values)
            assert scalar_dual.value == 0
            assert a-(k+h)*r+(c-g)/(1+r) == 0
            simplified = -k*r-c*(1+2*r)/(1+r)**2
            assert d == simplified
            counts['equilibrium_cases'] += 1
            counts['equilibrium_residual_components'] += n
            counts['equilibrium_diagonal_comparisons'] += n
            coverage['positive_equilibria' if r > 0 else 'negative_equilibria'] += 1
    return oracle, values


ns = [5,6,8]
parameter_sets = [tuple(map(Q,t)) for t in [
    (Q(2),Q(1,2),Q(3,2),Q(5,4),Q(2,3)),
    (Q(1,3),Q(7,5),Q(2,7),Q(11,6),Q(5,8)),
    (Q(5,2),Q(3,4),Q(7,3),Q(4,9),Q(2,5))]]
sync_states = list(map(Q,[Q(-3,4),Q(-1,2),Q(-1,5),0,Q(1,4),1,Q(7,3)]))
equilibrium_states = list(map(Q,[Q(-3,4),Q(-1,2),Q(-1,4),Q(1,4),Q(1,2),1,2]))

for n in ns:
    nonsync_states = [
        [Q(j+1,j+2) for j in range(n)],
        [Q((-1)**j*(j+1),2*(j+2)) for j in range(n)],
        [Q([-3,-1,0,2,4,1,-2,3][j],4) for j in range(n)],
        [Q(-j-1,n+1) for j in range(n)]]
    for q in range(1,n):
        neighbors = [(i)%n for i in [-1,q,-q]]
        collisions = len(set(neighbors)) < 3
        predicted = q in [1,n-1] or 2*q == n
        assert collisions == predicted
        assert 0 not in neighbors
        assert len(set(neighbors)) >= 2
        counts['offset_exhaustiveness_cases'] += 1
        coverage[f'n={n},q={q}'] += 1
        for params in parameter_sets:
            for state in nonsync_states:
                check_case(n,q,state,params,'nonsynchronous')
            for r in sync_states:
                check_case(n,q,[r]*n,params,'synchronous_arbitrary')
        for r in equilibrium_states:
            a,k,c,h = Q(4),Q(1,2),Q(3,2),Q(1,3)
            g = c+(1+r)*(a-(k+h)*r)
            params = (a,k,c,g,h)
            check_case(n,q,[r]*n,params,'synchronous_nonzero_equilibrium',True)
            if n==6 and q==3 and r in [Q(-1,2),Q(1,2)]:
                worked.append({'kind':'actual_equilibrium','n':n,'q':q,'r':str(r),
                               'parameters_a_k_c_g_h':list(map(str,params)),
                               'd_C_G_H':list(map(str,coefficients(r,params))),
                               'row_sum':str(scalar_original(Dual(r,[1]),params).gradient[0])})

# Each possible collision has a deliberately exact cancellation. The last-
# offset cancellation uses admissible negative synchrony (C+G can vanish).
for n in ns:
    cancellation_cases = [
        (1,Q(1),(Q(4),Q(1,2),Q(2),Q(3),Q(1)),'C-H'),
        (n-1,Q(-1,2),(Q(4),Q(1,2),Q(2),Q(2),Q(1)),'C+G')]
    if n%2 == 0:
        cancellation_cases.append((n//2,Q(1),(Q(4),Q(1,2),Q(2),Q(4),Q(1)),'G-H'))
    for q,r,params,label in cancellation_cases:
        mat,_ = check_case(n,q,[r]*n,params,'synchronous_cancellation')
        canceled_column = (n//2 if label=='G-H' else n-1)
        assert mat[0][canceled_column] == 0
        assert all(mat[i][(i+canceled_column)%n] == 0 for i in range(n))
        counts['synchronous_cancellation_entries'] += n
        coverage[f'cancellation_{label}'] += 1
        if n==6:
            worked.append({'kind':'synchronous_cancellation','n':n,'q':q,'r':str(r),
                           'parameters_a_k_c_g_h':list(map(str,params)),
                           'd_C_G_H':list(map(str,coefficients(r,params))),
                           'row_0':list(map(str,mat[0]))})
    # Separate nonsynchronous cancellation cases verify use of the repeated
    # coordinate before combination, especially the rational denominator.
    for label in ['C-H','C+G']+(['G-H'] if n%2==0 else []):
        state = [Q(j+1,2*n) for j in range(n)]
        if label == 'C-H':
            q=1; state[0]=Q(1); state[-1]=Q(-1,2)
            params=(Q(2),Q(1),Q(2),Q(3),Q(1)); column=n-1
        elif label == 'C+G':
            q=n-1; state[0]=Q(-1,2); state[-1]=Q(0)
            params=(Q(2),Q(1),Q(1),Q(4),Q(1)); column=n-1
        else:
            q=n//2; state[0]=Q(1); state[q]=Q(1,2)
            params=(Q(2),Q(1),Q(2),Q(9,4),Q(1)); column=q
        mat,_=check_case(n,q,state,params,'nonsynchronous_cancellation')
        assert mat[0][column] == 0
        counts['nonsynchronous_cancellation_entries'] += 1

# Explicitly demonstrate why the nonzero-equilibrium d formula is unavailable
# at an arbitrary origin: it gives -c, whereas the correct d is a-g.
origin_params = tuple(map(Q,[2,1,3,1,1]))
assert coefficients(Q(0),origin_params)[0] == 1
assert -origin_params[2] == -3
counts['origin_simplification_counterexamples'] += 1
worked.append({'kind':'origin_nonzero_equilibrium_shortcut_counterexample',
               'parameters_a_k_c_g_h':list(map(str,origin_params)),
               'actual_d':'1','invalid_shortcut_d':'-3'})

report = {
    'status':'PASS',
    'arithmetic':'fractions.Fraction; all equalities exact; no tolerance',
    'derivative_oracle':'forward automatic differentiation of original five-term vector field',
    'scope':'Jacobian, orientations, collision sums, origin, homogeneous row sum, equilibrium-only diagonal; no homogeneous spectrum or normality',
    'n_values':ns,
    'all_canonical_q_for_each_n':True,
    'parameter_sets':[[str(p) for p in params] for params in parameter_sets],
    'arbitrary_synchronous_states':list(map(str,sync_states)),
    'nonzero_equilibrium_states':list(map(str,equilibrium_states)),
    'counts':dict(sorted(counts.items())),
    'coverage':dict(sorted(coverage.items())),
    'worked_exact_examples':worked,
    'limitation':'Finite exact checks are corroboration; general validity comes from independent differentiation and modular-index proof.'
}
output=Path(__file__).with_name('exact_jacobian_results.json')
output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':report['status'],'counts':report['counts'],
                  'output':str(output)},indent=2))
