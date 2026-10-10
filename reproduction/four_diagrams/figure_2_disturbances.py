"""Figure 2: Responses to the two Wood disturbances.

Start at each model's equilibrium; multiply Wood by 1.05 or 0.30.
All runs reach t=120; modified-model panels display only t<=12.
The RK45 rerun checks the plotted DOP853 trajectories.

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

def integrate(m, p, x0, T=120, method='DOP853', n=3001):
    """Full five-node integration on 3,001 sampled times; check solver success."""
    r = solve_ivp(lin if m == 'lin' else sat, (0, T), x0, args=p, method=method, rtol=1e-10, atol=1e-12, t_eval=np.linspace(0, T, n))
    if not r.success:
        raise RuntimeError(r.message)
    return r

# Calculate the data and draw this figure.
(fig, axes) = plt.subplots(2, 2, figsize=(10.4, 6.3), layout='constrained')
R['perturbations'] = []
for (col, (m, p)) in enumerate([('lin', PL), ('sat', PS)]):
    xe = eq_l(p) if m == 'lin' else eq_s(p)
    for (row, factor) in enumerate([1.05, 0.3]):
        x = np.full(5, xe)
        x[0] *= factor
        s = integrate(m, p, x)
        check = integrate(m, p, x, method='RK45')
        R['perturbations'].append({'model': m, 'wood_factor': factor, 'initial_norm': float(np.linalg.norm(x - xe)), 'final_norm': float(np.linalg.norm(s.y[:, -1] - xe)), 'minimum_over_run': float(s.y.min()), 'RK45_DOP853_max_abs_difference': float(np.max(np.abs(s.y - check.y)))})
        ax = axes[row, col]
        for i in range(5):
            ax.plot(s.t, s.y[i] / xe, c=COL[i], lw=1.05, label=NAMES[i])
        ax.axhline(1, c='0.6', ls='--', lw=0.8)
        ax.set(xlabel='Model time', ylabel='$x_i / x^*$', title=f"{('Lin' if m == 'lin' else 'Modified')}: Wood {('+5%' if row == 0 else 'reduced to 30%')}")
        ax.set_xlim(0, 120 if m == 'lin' else 12)
fig.legend(NAMES, loc='outside lower center', ncol=5, frameon=False)
fig.suptitle('Response to a one-component initial disturbance', fontsize=13)
save('02_perturbation_recovery', fig)

# Save the underlying counts/numerical checks beside the graph.
(OUT / "figure_2_results.json").write_text(json.dumps(R, indent=2))
print(json.dumps(R, indent=2))
print(f"Saved figure files to {OUT}")
