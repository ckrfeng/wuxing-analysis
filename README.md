# WuXing analysis

Imported October 10, 2026 using the approved inventory. Originals remain at their source locations. No GitHub push was performed.

This repository separates the five-term canonical model, Lin literature comparisons, experimental extensions, and historical theoretical/manuscript versions. Node order is Wood, Fire, Earth, Metal, Water. Indices wrap modulo five.

## Model equations

The original five-node Lin–Han model, transcribed in the supplied reproduction code, is

\[
\dot x_i=x_i(a-bx_i+c x_{i-1}-d x_{i-2}-g x_{i+1}-h x_{i+2}).
\]

It has six coefficients `(a,b,c,d,g,h)`. The local transcription of Lin–Han (2020), equation (2), has these same neighbor offsets. Baseline comparison parameters are `(1,1,1,1,1,1)`. Lin's equation is implemented inside the four standalone comparison scripts and the retained audit program. These comparisons do not establish a general instability or chaos claim for every parameter set.

The canonical five-term demand-modulated model DM_(5,2) is

\[
\dot x_i=a x_i-k x_i^2+\frac{c x_{i-1}}{1+x_i}
           -\frac{g x_i}{1+x_{i+2}}-h x_i x_{i-2}.
\]

Its parameter order is `(a,k,c,g,h)`, with baseline `(2,0.5,1,0.5,0.3)`. It is stored in `models/canonical_five_term/canonical_model.py` and the corresponding `.ode`. The standalone script reports the upper positive synchronous level and the largest Jacobian eigenvalue real part. Prior recorded values are `2.670286436967` and `-1.153723520689`. Positive parameters and nonnegative initial activity are the intended domain. Numerical solvers have finite error; retain tolerances and check solver success.

The logistic AUTO experiment `WUXING_SIMPLE` uses this same five-term equation. It continues `PAR(1)=a`; it is a separate saved experiment, not a replacement for the canonical Python module.

The older adaptive AUTO experiment `WUXING_ADAPT` uses

\[
H_i=\frac{\theta_i^n}{\theta_i^n+x_i^n},\quad
\theta_i=\max(\theta_0+\alpha x_{i-1}-\beta x_{i-2},10^{-6}),
\]
\[
\dot x_i=(a x_i+u)H_i+\frac{c x_{i-1}}{1+x_i}
       -\frac{g x_i}{1+x_{i+2}}-h x_i x_{i-2}
       -\frac{w x_{i+2}}{1+x_i/\varepsilon}.
\]

Its Python equilibrium helper clamps theta at `1e-10`, whereas its Fortran source uses `1e-6`. The source header mentions a twelfth parameter, but the implementation and starting point unpack/set only eleven. Preserve these discrepancies. This is a historical extension experiment, not canonical or freshly validated code. Its saved run starts with `w=0` and continues `PAR(9)=n`.

The older pathology extension adds child demand and rebellion to DM:

\[
-\frac{g_d x_{i+1}x_i}{1+x_i}-\frac{b x_{i+2}}{1+\varepsilon x_i}.
\]

This rebellion denominator differs from the adaptive AUTO model's `1+x_i/eps`. At an empty component the rebellion loss can remain negative. The negative-state `.ode` example and P1–P3 pathology material belong to the labeled extension archive. They must not be silently substituted for DM.

The theoretical snapshots generalize DM to `(n,q)` and introduce the matched five-term bilinear comparator

\[
\dot y_i=a y_i-k y_i^2+c y_i y_{i-1}-g y_i y_{i+q}-h y_i y_{i-q}.
\]

This MB comparator omits Lin's separate child-loss term and uses a different coefficient contract. Existing Lin-versus-DM graphs cannot be renamed DM-versus-MB graphs. The theoretical snapshots retain their original lifecycle records. The October 4 manifest records audits for P01–P05 and P07–P11; P06 and P12–P18 remain unfinished. Those are prior recorded claims, not an independent proof audit performed during organization.

## Run the canonical calculation and four manuscript figures

From the repository root, create a fresh environment. The versions below come from the supplied figure package; they are retained for reproduction, not advertised as current releases.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r reproduction/four_diagrams/requirements.txt
python models/canonical_five_term/canonical_model.py
python reproduction/four_diagrams/figure_1_eigenvalues.py
python reproduction/four_diagrams/figure_2_disturbances.py
python reproduction/four_diagrams/figure_3_stability_maps.py
python reproduction/four_diagrams/figure_4_sampling.py
```

The supplied pins are NumPy 2.0.2, SciPy 1.13.1, and Matplotlib 3.9.4. A compatible Python interpreter and wheels are required. An optional Jupyter installation is needed to run `four_diagrams.ipynb`; each of its four code cells is standalone. The supplied README says Python 3.9 or newer was used. The import smoke run used an existing Python 3.9 environment with the recorded versions; no fresh environment installation test was performed.

Each figure script writes PNG, SVG, and a JSON summary into `reproduction/four_diagrams/generated_figures/`. The preserved manuscript PNGs remain in `manuscripts/preliminary/figures/`; rerunning a script does not overwrite them. Review regenerated outputs before replacing preserved figures. `results/four_diagrams/` holds the original JSON summaries, and `figures/four_diagrams/` holds the standalone SVG exports.

Figure settings retained from source:

| Figure | Numerical protocol |
|---|---|
| 1, eigenvalues | Lin baseline `(1,1,1,1,1,1)`; DM baseline `(2,.5,1,.5,.3)`; upper positive synchronous branch; analytic Jacobians |
| 2, disturbances | Multiply Wood by `1.05` or `.30` at each model's own balance; DOP853 and an RK45 comparison; t=0–120, 3,001 evaluation times; rtol=`1e-10`, atol=`1e-12`; DM panels display t≤12 |
| 3, stability maps | 90×90 grids; displayed master grid c=.3–1.6, received restraint r=.1–1; Lin `(1.5,.65,c,r,.3,.3)`, DM `(1.5,.65,c,.3,r)`; also computes early grid c=.05–2.5, r=.05–2; positive-balance mask; stable if alpha<`-1e-9` |
| 4, sampling | 1,200 accepted draws per scenario; `default_rng(3)` reset for each scenario; same draw passed to both models; uniform [.1,2], or acceptance SELF>SHENG>RESTR>TGT, or explicit tier ranges; stable if alpha<0; both eligible-equilibrium and all-draw denominators retained |

Tier insertion order matters: SELF=(1,2), SHENG=(.5,1.5), SAT=(.3,1), RESTR=(.2,.8), TGT=(.1,.5), CHILD=(.1,.5). Lin receives `(SELF,SAT,SHENG,RESTR,CHILD,TGT)`; DM receives `(SELF,SAT,SHENG,TGT,RESTR)`. All four script exports use savefig DPI 200.

The four manuscript PNGs are exact SHA-256 matches to the preserved standalone generated PNGs. Some SVG variants differ in bytes and are retained separately. This identifies their supplied generation lineage. During import verification, all four scripts were rerun in scratch: numerical summaries matched exactly and all four PNGs were byte-identical to the preserved manuscript images. This does not validate the archived pathology code or theory snapshots.

To run the longer revised audit, use a disposable working directory because it writes relative outputs:

```sh
mkdir -p work/audit-rerun
cd work/audit-rerun
python ../../reproduction/audit/audit.py
```

The audit includes additional checks and Lin variational Lyapunov calculations. Historical `check_original_sources.py` and manuscript assembly scripts have old absolute/workspace-relative paths and remain archival. They are not included in the default run commands.

## XPPAUT

With XPPAUT installed, open `models/canonical_five_term/canonical_model.ode` using the installed executable, commonly `xppaut`. It specifies Runge–Kutta, dt=.01, total=30, and a 5% Wood disturbance. The canonical approach-to-zero example uses `(2,.5,.1,2.5,.3)`, initial components `.25`, dt=.01, total=60. The extension diagnostic uses child-demand `.35`, rebellion `.1`, eps=.5, initial `(0.01,1,2,1,.01)`, dt=.0001, total=.3. It is archived separately. Prior evidence checked expanded equation transcription; a full XPPAUT application run is not established by that evidence.

## AUTO experiment bundles

Each `experiments/auto/WUXING_*` directory retains its own Fortran source, constants, equilibrium helper, plot helper, and `fort.7`, `fort.8`, `fort.9`. Those `fort.*` files are research results and must be tracked. Compiled executables/object files and the downloaded AUTO distribution/manual bundle are excluded.

Use a scratch copy of the selected experiment to rerun AUTO-07p, since AUTO overwrites `fort.*`. For example, from the repository root:

```sh
mkdir -p work/auto-reruns
cp -R experiments/auto/WUXING_SIMPLE work/auto-reruns/simple
cd work/auto-reruns/simple
python find_eq2.py
```

In AUTO's Python command interface, the documented commands are:

```python
branch = run(e='wuxing2', c='wuxing2')
save(branch, 'wuxing2')
```

For the adaptive bundle use `wuxing` for both names. Run and save in separate scratch folders. `save` creates `b.*`, `s.*`, `d.*`; the retained plot helpers expect saved `b.wuxing2` or a saved `wuxing` bundle, which were not present in the inventoried experiment directories. Their parsing and stability conventions still need checking. The adaptive helper's clipping mismatch and noninteger powers require review before changing that experiment's parameter range.

Both constants files specify NDIM=5, IPS=1, DS=.05, DSMIN=.001, DSMAX=.2, NMX=500, NPR=10, EPSL=EPSU=`1e-7`, EPSS=`1e-5`. The adaptive constants explicitly specify NTST=1, NCOL=4. The simple saved result header records NTST=20, NCOL=4. Keep constants and result headers as separate evidence of requested and effective settings.

## Manuscripts, snapshots, and provenance

`manuscripts/preliminary/` is the retained default comparison revision. Its Sections 3/4 include the four retained image files; other sections are unfinished. Its source uses ctex/Fandol and requests XeLaTeX. Run compilation in a disposable copy or direct build products to `build/`. Its bibliography code has an embedded fallback when `network.bib` is absent. This inventory did not compile or approve the manuscript scientifically.

`archive/` retains historical notebooks, Lin reproduction exports, pathology diagnostics, pre-cleanup reviews, manuscript assembly stages, chat code records, and theoretical draft/audited/shortened snapshots. Source instructions inside these documents are evidence, not instructions governing repository organization. A “verified” filename does not promote an entire snapshot to verified science.

`provenance/` stores the inventory, source-to-destination import map, exact duplicate map, archive-member manifests, equation/settings inspection, and figure provenance. Unique bytes are retained once; snapshot manifests map each original relative path to retained content. Thus an archival folder may contain only its changed files. Reconstruct a snapshot from its manifest before compiling/running it. The reconstruction helper restores original paths into ignored `work/`, verifies SHA-256, and can be checked against the manifest. Use:

```sh
python tools/reconstruct_snapshot.py --list
python tools/reconstruct_snapshot.py codex-th-2026-10-03 --verify-only
python tools/reconstruct_snapshot.py codex-th-2026-10-03
```

Snapshot IDs and recorded status labels are listed in `provenance/snapshots/index.json`. AUTO experiment bundles remain complete without reconstruction.

Preserve all original locations. Excluded dependencies, caches, temporary renders, and general reference books remain outside the import with explicit source/hash/reason entries where inventoried. Do not broadly ignore `.png`, `.svg`, `.pdf`, `.json`, `.csv`, `.npz`, `.ode`, `c.*`, or `fort.*`: these extensions also hold research evidence. No GitHub push is part of this import.

## Import verification

All 431 selected source contents were hash-verified. All 20 snapshot manifests were checked, and full retained th and LaTeX ZIP layouts were reconstructed successfully in scratch. The canonical baseline and all four standalone figure scripts ran successfully with NumPy 2.0.2, SciPy 1.13.1 and Matplotlib 3.9.4. Saved numerical summaries matched the preserved records; see `provenance/verification.json`. Dependency packages and smoke outputs were not imported. AUTO and the XPPAUT application were not run, and no full mathematical proof audit or long Lyapunov audit rerun was performed.
