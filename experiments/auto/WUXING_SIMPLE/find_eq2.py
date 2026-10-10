import numpy as np
from scipy.optimize import fsolve

def rhs(x, a=2.0, k=0.5, c=1.0, g=0.5, h=0.3):
    x1,x2,x3,x4,x5 = x
    f1 = a*x1 - k*x1**2 + c*x5/(1+x1) - g*x1/(1+x3) - h*x1*x4
    f2 = a*x2 - k*x2**2 + c*x1/(1+x2) - g*x2/(1+x4) - h*x2*x5
    f3 = a*x3 - k*x3**2 + c*x2/(1+x3) - g*x3/(1+x5) - h*x3*x1
    f4 = a*x4 - k*x4**2 + c*x3/(1+x4) - g*x4/(1+x1) - h*x4*x2
    f5 = a*x5 - k*x5**2 + c*x4/(1+x5) - g*x5/(1+x2) - h*x5*x3
    return [f1,f2,f3,f4,f5]

# Try several starting guesses
guesses = [
    [2.0, 2.0, 2.0, 2.0, 2.0],
    [3.0, 3.0, 3.0, 3.0, 3.0],
    [1.5, 1.5, 1.5, 1.5, 1.5],
    [4.0, 4.0, 4.0, 4.0, 4.0],
    [0.5, 0.5, 0.5, 0.5, 0.5],
]

for g0 in guesses:
    sol, info, ier, msg = fsolve(rhs, g0, full_output=True)
    residual = np.max(np.abs(rhs(sol)))
    # only print if all positive and residual is small
    if residual < 1e-10 and all(s > 0.01 for s in sol):
        print(f"Starting guess {g0[0]}: Equilibrium = {sol}, Residual = {residual:.2e}")
