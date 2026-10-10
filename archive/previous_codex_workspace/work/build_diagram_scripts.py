from pathlib import Path
import ast,json
source=Path('work/clean_package/audit.py').read_text()
functions={n.name:ast.get_source_segment(source,n) for n in ast.parse(source).body if isinstance(n,ast.FunctionDef)}
output=Path('outputs/diagram_code')
shared=['lin','sat','eq_l','roots_s','eq_s','jl','js','eigs','alpha']
sections=[
 ('figure_1_eigenvalues.py','Baseline Jacobian eigenvalues',shared,source[source.index("R['baseline']={}"):source.index("R['stable_lin_counterexample']")], 'baseline'),
 ('figure_2_disturbances.py','Responses to the two Wood disturbances',['lin','sat','eq_l','roots_s','eq_s','integrate'],source[source.index('# Reproduce original protocol;'):source.index('# Both historical map windows')], 'perturbations'),
 ('figure_3_stability_maps.py','Two-parameter stability maps',shared,source[source.index("R['maps']={}"):source.index('# Reproduce exact seed')], 'maps'),
 ('figure_4_sampling.py','Stability frequencies under three sampling schemes',shared,source[source.index("TIERS="):source.index('# Child ablation')], 'monte_carlo')]
docs={
 'eq_l':'Positive synchronous level of Lin; NaN means no such equilibrium.',
 'roots_s':'All positive synchronous levels of the five-term model, sorted.',
 'eq_s':'Select the upper positive synchronous branch used in the figures.',
 'jl':'Lin Jacobian at a five-component state; p=(a,b,c,d,g,h).',
 'js':'Five-term modified Jacobian; p=(a,k,c,g,h).',
 'eigs':'Compute all five Jacobian eigenvalues at the selected balanced level.',
 'alpha':'Largest eigenvalue real part; NaN if positive balance is absent.',
 'lin':'Lin six-term equation. Node order: Wood, Fire, Earth, Metal, Water.',
 'sat':'Canonical five-term DM_(5,2). No additional loss terms are included.',
 'integrate':'Full five-node integration on 3,001 sampled times; check solver success.'}
header='''from pathlib import Path
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

'''
notes={
 1:'Each marker is a Jacobian eigenvalue at the stated model baseline.\nNegative real parts imply local exponential stability; positive parts imply instability.',
 2:'Start at each model\'s equilibrium; multiply Wood by 1.05 or 0.30.\nAll runs reach t=120; modified-model panels display only t<=12.\nThe RK45 rerun checks the plotted DOP853 trajectories.',
 3:'For the displayed master grid: c in [0.3,1.6], restraint in [0.1,1.0].\nLin tuple = (1.5,0.65,c,restraint,0.3,0.3).\nModified tuple = (1.5,0.65,c,0.3,restraint).\nAt each grid point, select positive balance, compute eigenvalues, then color\nby the largest real part. Count stability using alpha < -1e-9.\nThe earlier grid is also computed for the supplementary numerical comparison;\nonly the master grid is plotted. Missing equilibria are gray, not unstable.\nColor magnitudes are clipped at a shared percentile, not the data itself.',
 4:'Draw 1,200 accepted parameter sets per scenario with seed 3.\nReset the generator for each scenario, preserving the original draw order.\nUniform: all six conceptual coefficients uniform on [0.1,2].\nOrdered: same distribution conditional on SELF > SHENG > RESTR > TGT.\nTiered: independent draws in the explicit TIERS intervals below.\nEach draw is paired across models; CHILD has no counterpart in the modified model.\nPreserve TIERS insertion order to reproduce the same seeded results.\nLeft bars condition on positive-balance existence; right bars use all draws.\nThe original sampling calculation uses alpha < 0; near-zero cases should be\nexamined separately if you change these parameters or sampling ranges.'}
for i,(filename,title,names,body,key) in enumerate(sections,1):
 formatted=[]
 for name in names:
  node=ast.parse(functions[name]).body[0]
  node.body.insert(0,ast.Expr(value=ast.Constant(value=docs[name])))
  formatted.append(ast.unparse(ast.fix_missing_locations(node)))
 # Unparse only to expand compressed statements; computations stay unchanged.
 if i == 3:
  body=body.replace('Among positive balanced equilibria:', 'Among existing positive equilibria:')
 code=ast.unparse(ast.parse(body))
 intro='"""Figure '+str(i)+': '+title+'.\n\n'+notes[i]+'\n\nRequires numpy, scipy, matplotlib. Run this file by itself.\n"""\n'
 text=intro+header+'\n\n'.join(formatted)+'\n\n# Calculate the data and draw this figure.\n'+code+'\n'
 text+=f'\n# Save the underlying counts/numerical checks beside the graph.\n(OUT / "figure_{i}_results.json").write_text(json.dumps(R, indent=2))\nprint(json.dumps(R, indent=2))\nprint(f"Saved figure files to {{OUT}}")\n'
 compile(text,filename,'exec');(output/filename).write_text(text)
# Optional notebook: the same four standalone code blocks, without outputs.
cells=[{'cell_type':'markdown','metadata':{},'source':['# Code for the four figures\n','Each section is independent. Run the cell for the figure you want.\n','These reproduce the original Lin-versus-five-term-model comparisons.']}]
for filename,title,*_ in sections:
 cells.append({'cell_type':'markdown','metadata':{},'source':['## '+title+'\n',filename]})
 cells.append({'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source':(output/filename).read_text().splitlines(keepends=True)})
for idx, cell in enumerate(cells): cell['id'] = f'figure-cell-{idx}'
notebook={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.9'}},'nbformat':4,'nbformat_minor':5}
(output/'four_diagrams.ipynb').write_text(json.dumps(notebook,indent=2))
(output/'requirements.txt').write_text('numpy==2.0.2\nscipy==1.13.1\nmatplotlib==3.9.4\n')
(output/'README.txt').write_text('''CODE FOR THE FOUR SUPPLIED DIAGRAMS

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
''')
print('Created four standalone scripts and a notebook.')
