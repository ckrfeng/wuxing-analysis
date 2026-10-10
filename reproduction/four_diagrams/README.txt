CODE FOR THE FOUR SUPPLIED DIAGRAMS

Each Python file is standalone: no shared local module is required.
The model and Jacobian definitions needed for that figure are included.
The notebook contains the same four independent scripts as separate cells.

1. figure_1_eigenvalues.py: baseline eigenvalue plane.
2. figure_2_disturbances.py: small and large Wood disturbances.
3. figure_3_stability_maps.py: the continuous two-parameter heatmaps.
4. figure_4_sampling.py: uniform, ordered, and tiered sampling bars.

With Python 3.9 or newer, install the tested dependency versions:
    python -m pip install -r requirements.txt
Then run any script, for example:
    python figure_1_eigenvalues.py

Each script saves PNG and SVG images plus a JSON numerical summary under
its generated_figures folder. Running all four produces all four graphs.
For a notebook/Colab workflow, open four_diagrams.ipynb and run the desired
cell after installing the dependencies in that environment.

Parameters are explicit in each script. Lin uses six coefficients and the
modified model uses five, but both have five state variables. The modified
model is DM_(5,2). These scripts contain no rebellion-model extension and
do not implement the newer matched bilinear comparator.

These are the standalone reproduction scripts for the four verified graphs
in the manuscript, extracted from the checked audit program. They are not
presented as unchanged historical Claude notebook exports. The equations,
parameter values, sampling order, integration settings and plot settings
are retained. The code for each figure is independently executable.

The numerical stability frequencies describe the specified parameters and
sampling assumptions; they do not isolate a single changed interaction law.
