"""Five-term demand-modulated model DM_(5,2).

Order: Wood, Fire, Earth, Metal, Water; indices wrap modulo five.
Parameter order: (a, k, c, g, h). Use a,k,c,g,h > 0 and x(0) >= 0.
The exact ODE preserves nonnegativity; numerical solvers have finite error.
This module contains only the canonical model. Requires NumPy.
"""
import numpy as np

BASELINE = (2.0, 0.5, 1.0, 0.5, 0.3)


def rhs(t, x, a, k, c, g, h):
    """Compatible with solve_ivp(..., args=BASELINE)."""
    x = np.asarray(x)
    return (a*x - k*x*x + c*np.roll(x, 1)/(1+x)
            - g*x/(1+np.roll(x, -2)) - h*x*np.roll(x, 2))


def positive_balances(a, k, c, g, h):
    """All positive synchronous levels, sorted; origin exists separately."""
    A = k + h
    D = (A-a)**2 + 4*A*(a+c-g)
    if D < 0:
        return []
    roots = [(a-A-np.sqrt(D))/(2*A), (a-A+np.sqrt(D))/(2*A)]
    return sorted(set(float(s) for s in roots if s > 0))


def jacobian(x, a, k, c, g, h):
    """Jacobian at a five-component state, not only at an equilibrium."""
    x = np.asarray(x)
    J = np.zeros((5, 5))
    for i in range(5):
        mother, target, controller = (i-1) % 5, (i+2) % 5, (i-2) % 5
        J[i, i] = (a - 2*k*x[i] - c*x[mother]/(1+x[i])**2
                   - g/(1+x[target]) - h*x[controller])
        J[i, mother] += c/(1+x[i])
        J[i, target] += g*x[i]/(1+x[target])**2
        J[i, controller] -= h*x[i]
    return J


if __name__ == '__main__':
    s = positive_balances(*BASELINE)[-1]
    alpha = np.linalg.eigvals(jacobian(np.full(5, s), *BASELINE)).real.max()
    print(f'Positive balanced level: {s:.12f}')
    print(f'Largest eigenvalue real part: {alpha:.12f}')
