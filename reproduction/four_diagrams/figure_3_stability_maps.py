"""Figure 3: Two-parameter stability maps.

For the displayed master grid: c in [0.3,1.6], restraint in [0.1,1.0].
Lin tuple = (1.5,0.65,c,restraint,0.3,0.3).
Modified tuple = (1.5,0.65,c,0.3,restraint).
At each grid point, select positive balance, compute eigenvalues, then color
by the largest real part. Count stability using alpha < -1e-9.
The earlier grid is also computed for the supplementary numerical comparison;
only the master grid is plotted. Missing equilibria are gray, not unstable.
Color magnitudes are clipped at a shared percentile, not the data itself.

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
R['maps'] = {}
maps = []
for (name, N, cs, rs) in [('early', 90, np.linspace(0.05, 2.5, 90), np.linspace(0.05, 2, 90)), ('master', 90, np.linspace(0.3, 1.6, 90), np.linspace(0.1, 1, 90))]:
    arr = []
    stats = {}
    for m in ['lin', 'sat']:
        z = np.full((N, N), np.nan)
        for (iy, r) in enumerate(rs):
            for (ix, c) in enumerate(cs):
                p = ((1, 1, c, 1, 1, r) if m == 'lin' else (2, 0.5, c, 0.5, r)) if name == 'early' else (1.5, 0.65, c, r, 0.3, 0.3) if m == 'lin' else (1.5, 0.65, c, 0.3, r)
                z[iy, ix] = alpha(m, p)
        valid = np.isfinite(z)
        stable = valid & (z < -1e-09)
        stats[m] = {'stable': int(stable.sum()), 'valid': int(valid.sum()), 'total': N * N, 'fraction_all': float(stable.mean()), 'fraction_valid': float(stable.sum() / valid.sum()), 'min': float(np.nanmin(z)), 'max': float(np.nanmax(z))}
        arr.append(z)
    R['maps'][name] = stats
    if name == 'master':
        maps = arr
        mapcs = cs
        maprs = rs
(fig, axes) = plt.subplots(1, 2, figsize=(11, 4.7), layout='constrained')
vm = max(0.5, np.nanpercentile(np.abs(np.concatenate([z.ravel() for z in maps])), 90))
cmap = plt.get_cmap('RdBu_r').copy()
cmap.set_bad('#b9bec6')
for (ax, m, z) in zip(axes, ['lin', 'sat'], maps):
    im = ax.pcolormesh(mapcs, maprs, z, cmap=cmap, norm=TwoSlopeNorm(0, -vm, vm), shading='nearest')
    if np.nanmin(z) < 0 < np.nanmax(z):
        ax.contour(mapcs, maprs, z, levels=[0], colors='k', linewidths=1.4)
    st = R['maps']['master'][m]
    ax.set(xlabel='Nourishment coefficient c', ylabel='Received restraint d (Lin)' if m == 'lin' else 'Received restraint h (modified)', title=f"{('Lin' if m == 'lin' else 'Modified')}: {100 * st['fraction_all']:.1f}% of all grid points stable")
    ax.text(0.02, 0.025, f"Among existing positive equilibria: {100 * st['fraction_valid']:.1f}%", transform=ax.transAxes, fontsize=8, bbox={'fc': 'white', 'ec': 'none', 'alpha': 0.9})
    fig.colorbar(im, ax=ax, extend='both', label='$\\max\\mathrm{Re}\\,\\lambda$ (color limits clipped)')
fig.suptitle('Balanced-equilibrium stability on the master notebook grid', fontsize=13)
fig.legend(handles=[Patch(color='#b9bec6', label='No positive balanced equilibrium'), plt.Line2D([], [], c='k', label='Interpolated zero contour')], loc='outside lower center', ncol=2, frameon=False, fontsize=8)
save('03_corrected_stability_maps', fig)

# Save the underlying counts/numerical checks beside the graph.
(OUT / "figure_3_results.json").write_text(json.dumps(R, indent=2))
print(json.dumps(R, indent=2))
print(f"Saved figure files to {OUT}")
