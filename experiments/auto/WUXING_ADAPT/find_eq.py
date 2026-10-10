# find_eq.py
import numpy as np
from scipy.optimize import fsolve

def rhs(x, a=2.0, u=0.5, c=1.0, g=0.5, h=0.3,
        th0=1.0, alp=0.1, bet=0.1, nh=2.0, w=0.0, eps=0.5):

    x1,x2,x3,x4,x5 = x

    # set points
    th = [
        th0 + alp*x5 - bet*x4,
        th0 + alp*x1 - bet*x5,
        th0 + alp*x2 - bet*x1,
        th0 + alp*x3 - bet*x2,
        th0 + alp*x4 - bet*x3,
    ]
    th = [max(t, 1e-10) for t in th]

    def hill_p(xi, thi):
        return a*xi * thi**nh / (thi**nh + xi**nh)

    def hill_u(xi, thi):
        return u * thi**nh / (thi**nh + xi**nh)

    # sigma: mothers
    xmom = [x5, x1, x2, x3, x4]
    # kappa: Ke targets
    xtar = [x3, x4, x5, x1, x2]
    # rho: Ke controllers
    xcon = [x4, x5, x1, x2, x3]

    xv = [x1,x2,x3,x4,x5]
    f = []
    for i in range(5):
        fi = (hill_p(xv[i], th[i])
            + hill_u(xv[i], th[i])
            + c*xmom[i]/(1+xv[i])
            - g*xv[i]/(1+xtar[i])
            - h*xv[i]*xcon[i]
            - w*xtar[i]/(1 + xv[i]/eps))
        f.append(fi)
    return f

# Try symmetric initial guess
x0 = [1.0, 1.0, 1.0, 1.0, 1.0]
sol = fsolve(rhs, x0, full_output=True)
print("Equilibrium:", sol[0])
print("Residual:", np.max(np.abs(rhs(sol[0]))))
