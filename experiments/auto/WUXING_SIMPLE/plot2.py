import numpy as np
import matplotlib.pyplot as plt

def parse_b(filename):
    branches = []
    current = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('!') or line.startswith('BR'):
                if current:
                    branches.append(current)
                    current = []
                continue
            vals = line.split()
            try:
                current.append([float(v) for v in vals])
            except ValueError:
                continue
    if current:
        branches.append(current)
    return branches

branches = parse_b('b.wuxing2')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for br in branches:
    arr = np.array(br)
    # columns: BR, PT, TY, LAB, PAR(ICP), L2NORM, U(1)..U(5)
    if arr.shape[1] < 7:
        continue
    par_vals = arr[:, 4]   # PAR(1) = a
    x1_vals  = arr[:, 6]   # U(1)
    l2_vals  = arr[:, 5]   # L2 norm

    axes[0].plot(par_vals, l2_vals, 'b-', linewidth=1.5)
    axes[1].plot(par_vals, x1_vals, 'r-', linewidth=1.5)

axes[0].set_xlabel('$a$ (self-production rate)', fontsize=13)
axes[0].set_ylabel('L2-norm of equilibrium', fontsize=13)
axes[0].set_title('Bifurcation diagram — L2 norm')
axes[0].grid(True, alpha=0.3)

axes[1].set_xlabel('$a$ (self-production rate)', fontsize=13)
axes[1].set_ylabel('$x_1^*$ (Liver)', fontsize=13)
axes[1].set_title('Bifurcation diagram — $x_1$')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('bifurcation2.pdf')
plt.show()
print("Saved to bifurcation2.pdf")
