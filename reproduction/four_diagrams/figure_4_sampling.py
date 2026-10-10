"""Figure 4: Stability frequencies under three sampling schemes.

Draw 1,200 accepted parameter sets per scenario with seed 3.
Reset the generator for each scenario, preserving the original draw order.
Uniform: all six conceptual coefficients uniform on [0.1,2].
Ordered: same distribution conditional on SELF > SHENG > RESTR > TGT.
Tiered: independent draws in the explicit TIERS intervals below.
Each draw is paired across models; CHILD has no counterpart in the modified model.
Preserve TIERS insertion order to reproduce the same seeded results.
Left bars condition on positive-balance existence; right bars use all draws.
The original sampling calculation uses alpha < 0; near-zero cases should be
examined separately if you change these parameters or sampling ranges.

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
TIERS = {'SELF': (1, 2), 'SHENG': (0.5, 1.5), 'SAT': (0.3, 1), 'RESTR': (0.2, 0.8), 'TGT': (0.1, 0.5), 'CHILD': (0.1, 0.5)}

def draw(r, scheme):
    if scheme == 'tiered':
        return {k: r.uniform(*v) for (k, v) in TIERS.items()}
    while True:
        (S, A, SH, RE, TG, CH) = r.uniform(0.1, 2, 6)
        if scheme == 'full_order' and (not S > SH > RE > TG):
            continue
        return dict(SELF=S, SAT=A, SHENG=SH, RESTR=RE, TGT=TG, CHILD=CH)

def to_p(m, d):
    return (d['SELF'], d['SAT'], d['SHENG'], d['RESTR'], d['CHILD'], d['TGT']) if m == 'lin' else (d['SELF'], d['SAT'], d['SHENG'], d['TGT'], d['RESTR'])

def wilson(k, n):
    z = 1.96
    p = k / n
    den = 1 + z * z / n
    ctr = (p + z * z / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [ctr - h, ctr + h]
R['monte_carlo'] = {}
for scheme in ['uniform', 'full_order', 'tiered']:
    r = np.random.default_rng(3)
    v = {m: [] for m in ['lin', 'sat']}
    for _ in range(1200):
        d = draw(r, scheme)
        for m in v:
            v[m].append(alpha(m, to_p(m, d)))
    ss = {}
    common = np.isfinite(v['lin']) & np.isfinite(v['sat'])
    for (m, z) in v.items():
        z = np.array(z)
        va = np.isfinite(z)
        st = va & (z < 0)
        (ns, nv) = (int(st.sum()), int(va.sum()))
        ss[m] = {'stable': ns, 'valid': nv, 'total': 1200, 'conditional': ns / nv, 'unconditional': ns / 1200, 'wilson_conditional': wilson(ns, nv), 'both_exist_n': int(common.sum()), 'both_exist_stable_fraction': float(np.mean(z[common] < 0))}
    R['monte_carlo'][scheme] = ss
(fig, axes) = plt.subplots(1, 2, figsize=(10.7, 4.6), layout='constrained')
for (ax, key, title) in zip(axes, ['conditional', 'unconditional'], ['Among draws with positive balance', 'Among all 1,200 draws']):
    x = np.arange(3)
    for (m, offset, col, lab) in [('lin', -0.18, '#c05b53', 'Lin'), ('sat', 0.18, '#347aa2', 'Modified')]:
        vals = [100 * R['monte_carlo'][s][m][key] for s in R['monte_carlo']]
        bars = ax.bar(x + offset, vals, 0.36, color=col, label=lab)
        for (b, val) in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, val + 1.5, f'{val:.1f}%', ha='center', fontsize=8)
    ax.set_xticks(x, ['Uniform', 'Ordered', 'Tiered'])
    ax.set(ylim=(0, 111), ylabel='Draws with locally stable positive balance (%)', title=title)
    ax.legend(frameon=False, fontsize=8)
fig.suptitle('Stability frequencies depend on the specified sampling scheme', fontsize=13)
save('04_sampling_denominators', fig)

# Save the underlying counts/numerical checks beside the graph.
(OUT / "figure_4_results.json").write_text(json.dumps(R, indent=2))
print(json.dumps(R, indent=2))
print(f"Saved figure files to {OUT}")
