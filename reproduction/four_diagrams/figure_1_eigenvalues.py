"""Figure 1: Baseline Jacobian eigenvalues.

Each marker is a Jacobian eigenvalue at the stated model baseline.
Negative real parts imply local exponential stability; positive parts imply instability.

Requires numpy, scipy, matplotlib. Run this file by itself.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Save images without needing a desktop plot window.
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Patch
from scipy.integrate import solve_ivp

# Lin parameter order:      (a, b, c, d, g, h).
# Modified parameter order: (a, k, c, g, h).
# Received restraint is d in Lin and h in the modified model.
# Lin is the original six-term comparator, not the newer matched comparator.
PL = (1, 1, 1, 1, 1, 1)
PS = (2, 0.5, 1, 0.5, 0.3)
NAMES = ["Wood", "Fire", "Earth", "Metal", "Water"]
COL = ["#26845b", "#c74641", "#a05aa1", "#454b57", "#347db6"]
BASE_DIR = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
OUT = BASE_DIR / "generated_figures"
OUT.mkdir(parents=True, exist_ok=True)
R = {}
plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "savefig.dpi": 200})


def save(name, fig):
    """Write both a PNG image and an editable vector SVG."""
    fig.savefig(OUT / (name + ".png"), bbox_inches="tight")
    fig.savefig(OUT / (name + ".svg"), bbox_inches="tight")
    plt.close(fig)

def lin(t, x, a, b, c, d, g, h):
    """Lin six-term equation. Node order: Wood, Fire, Earth, Metal, Water."""
    return x * (a - b * x + c * np.roll(x, 1) - d * np.roll(x, 2) - g * np.roll(x, -1) - h * np.roll(x, -2))

def sat(t, x, a, k, c, g, h):
    """Canonical five-term DM_(5,2). No additional loss terms are included."""
    return a * x - k * x * x + c * np.roll(x, 1) / (1 + x) - g * x / (1 + np.roll(x, -2)) - h * x * np.roll(x, 2)

def eq_l(p):
    """Positive synchronous level of Lin; NaN means no such equilibrium."""
    (a, b, c, d, g, h) = p
    M = b + d + g + h - c
    return a / M if M > 0 else np.nan

def roots_s(p):
    """All positive synchronous levels of the five-term model, sorted."""
    (a, k, c, g, h) = p
    A = k + h
    D = (A - a) ** 2 + 4 * A * (a + c - g)
    if D < 0:
        return []
    return sorted(set([v for v in ((a - A - np.sqrt(D)) / (2 * A), (a - A + np.sqrt(D)) / (2 * A)) if v > 0]))

def eq_s(p):
    """Select the upper positive synchronous branch used in the figures."""
    r = roots_s(p)
    return max(r) if r else np.nan

def jl(x, p):
    """Lin Jacobian at a five-component state; p=(a,b,c,d,g,h)."""
    (a, b, c, d, g, h) = p
    J = np.zeros((5, 5))
    for i in range(5):
        J[i, i] = a - 2 * b * x[i] + c * x[(i - 1) % 5] - d * x[(i - 2) % 5] - g * x[(i + 1) % 5] - h * x[(i + 2) % 5]
        for (off, v) in [(-1, c), (-2, -d), (1, -g), (2, -h)]:
            J[i, (i + off) % 5] = v * x[i]
    return J

def js(x, p):
    """Five-term modified Jacobian; p=(a,k,c,g,h)."""
    (a, k, c, g, h) = p
    J = np.zeros((5, 5))
    for i in range(5):
        s = 1 + x[i]
        ta = x[(i + 2) % 5]
        J[i, i] = a - 2 * k * x[i] - c * x[(i - 1) % 5] / s ** 2 - g / (1 + ta) - h * x[(i - 2) % 5]
        J[i, (i - 1) % 5] = c / s
        J[i, (i + 2) % 5] = g * x[i] / (1 + ta) ** 2
        J[i, (i - 2) % 5] = -h * x[i]
    return J

def eigs(m, p, x=None):
    """Compute all five Jacobian eigenvalues at the selected balanced level."""
    if x is None:
        x = eq_l(p) if m == 'lin' else eq_s(p)
    if not np.isfinite(x):
        return np.full(5, np.nan)
    return np.linalg.eigvals((jl if m == 'lin' else js)(np.full(5, x), p))

def alpha(m, p):
    """Largest eigenvalue real part; NaN if positive balance is absent."""
    return np.max(eigs(m, p).real)

# Calculate the data and draw this figure.
R['baseline'] = {}
(fig, ax) = plt.subplots(figsize=(7.5, 4.5), layout='constrained')
ax.axvspan(0, 1, color='#f9e8e6')
ax.axvline(0, c='0.3', lw=1)
ax.axhline(0, c='0.8', lw=0.7)
for (m, p, col, mk, lab) in [('lin', PL, '#bb453d', 'o', 'Lin: all coefficients = 1'), ('sat', PS, '#24628d', 'x', 'Modified: (2, 0.5, 1, 0.5, 0.3)')]:
    es = eigs(m, p)
    xe = eq_l(p) if m == 'lin' else eq_s(p)
    R['baseline'][m] = {'xstar': xe, 'alpha': float(max(es.real)), 'eigenvalues': [[float(z.real), float(z.imag)] for z in sorted(es, key=lambda z: -z.real)]}
    ax.scatter(es.real, es.imag, c=col, marker=mk, s=80, label=lab)
ax.set(xlabel='Re $\\lambda$', ylabel='Im $\\lambda$', xlim=(-2.6, 0.8), ylim=(-1.3, 1.3), title='Local stability at the stated baseline parameters')
ax.legend(loc='lower right', fontsize=8)
ax.grid(alpha=0.18)
save('01_baseline_eigenvalues', fig)

# Save the underlying counts/numerical checks beside the graph.
(OUT / "figure_1_results.json").write_text(json.dumps(R, indent=2))
print(json.dumps(R, indent=2))
print(f"Saved figure files to {OUT}")
