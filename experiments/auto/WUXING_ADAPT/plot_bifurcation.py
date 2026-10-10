# plot_bifurcation.py
import numpy as np
import matplotlib.pyplot as plt
from auto import loadbd   # AUTO's built-in loader

bd = loadbd('wuxing')

# Extract bifurcation diagram: PAR(9) = n_h vs x1 at equilibrium
nh_vals = []
x1_vals = []
stability = []

for pt in bd:
    nh_vals.append(pt['PAR'][9])
    x1_vals.append(pt['U'][1])
    # pt['PT'] > 0: stable, < 0: unstable (convention depends on AUTO version)
    stability.append(pt['PT'])

nh_vals = np.array(nh_vals)
x1_vals = np.array(x1_vals)

# Separate stable and unstable branches
# AUTO labels: stable = positive determinant in its output
plt.figure(figsize=(8,5))
plt.plot(nh_vals, x1_vals, 'b-', linewidth=1.5, label='$x_1$ equilibrium')
plt.xlabel('Hill exponent $n$', fontsize=13)
plt.ylabel('$x_1^*$ (Liver activity)', fontsize=13)
plt.title('Bifurcation diagram: symmetric Wu-Xing model')
plt.legend()
plt.tight_layout()
plt.savefig('bifurcation.pdf')
plt.show()
