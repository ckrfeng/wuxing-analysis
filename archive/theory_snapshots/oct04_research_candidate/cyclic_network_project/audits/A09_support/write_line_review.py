"""Maintain the complete, consecutive line ledger in the standalone A09 source."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
# Each row gives the inclusive final line. Starts are computed consecutively.
rows=[
(15,'Metadata correctly declares DRAFT, fixed parameter path, direct P02--P04 dependencies, inherited P01 and scope exclusions.'),
(20,'Title and status agree with the exact CURRENT manifest; no verification is self-awarded.'),
(27,'Canonical tuple and abbreviations are consistent; $b$ is unambiguously local and $A>0$.'),
(33,'All five original DM terms are transcribed with correct indices and $g=g_c-\\mu$.'),
(39,'Joint smoothness, positive $g$ neighborhood, open domain and parameter-dependent locality are correct; no global invariance or uniform-in-$n$ claim.'),
(49,'P02 import is the exact invariant restriction with denominator $1+r$; no global completeness is inferred here.'),
(53,'Subsection and anchor only; no added claim.'),
(70,'Critical spectrum lemma: algebraically simple zero, real kernel, explicit positive gap and arbitrary admissible $q$ are correct.'),
(80,'Original differentiation, Fourier phases, characteristic-polynomial derivative and real kernel are independently correct.'),
(85,'Cosine comparison covers odd/even dimensions and all paired/singleton nonzero labels.'),
(97,'Local equilibrium completeness is stated in state and parameter neighborhoods, including $b=0$.'),
(107,'Mean coordinates and orthogonal mean-zero projection give a real linear isomorphism; normalization agrees with scalar amplitude.'),
(115,'Projected derivative preserves $E$; complexification has no kernel, which does imply invertibility of the real restriction.'),
(124,'Real IFT product and uniqueness imply $\\psi\\equiv0$; zero belongs to one common transverse neighborhood.'),
(130,'Both equilibrium implications are proved; multiplication by positive $1+r$ is harmless; shrinking gives a state/parameter product.'),
(135,'Subsection/proposition opening has no unsupported claim.'),
(141,'Scalar derivative values and mixed derivative are correct.'),
(154,'Left/right vectors have pairing one; full contractions, Taylor half-factor and opposite physical-$g$ coefficient are correct.'),
(159,'Scalar expansion has cubic coefficient $-(A+b)$ and quadratic derivative $2b$.'),
(169,'Original-field mixed derivatives and all five second directional contributions are correct; averaging introduces no extra $n$.'),
(175,'Generic theorem title is justified by the ensuing full-system proof.'),
(189,'Branch completeness, smoothness and expansions have fixed-$b$ local scope; both slope orientations are correct.'),
(206,'Tangents are in the synchronous state--parameter plane; full nonlinear stability table and transcritical conclusion have the stated generic hypotheses.'),
(215,'Second IFT constructs the unique small root; nonzero iff $\\mu\\ne0$; the other root stays excluded for fixed $b\\ne0$.'),
(225,'First/second derivatives and tangent vectors are correct; $d\\mu/dg=-1$ is explicitly used.'),
(235,'Invariant line is a fixed-parameter center manifold; its product with parameter is the full extended center manifold because $F_\\mu(0,0)=0$.'),
(244,'Coordinate $u=Ar^2-br$ is locally invertible; exact transformed vector field and rational time factor are correct.'),
(249,'Denominators stay nonzero, time factor is positive, and orbital equivalence is limited to the center restriction.'),
(254,'Full derivative of the scalar field is taken before imposing equilibrium; product-rule terms are correct.'),
(261,'Uniform eigenvalue and alternative expression use the equilibrium relation with the correct minus sign.'),
(270,'Both $b$ factors retain their sign locally; the exact sign proof is primary and the expansion only corroborates it.'),
(282,'General P04 coefficients and phase signs remain valid at negative synchronous states and colliding offsets.'),
(293,'Finite-label continuity yields one common strict transverse gap, including $b=0$; no selection theorem is used.'),
(303,'Origin sign and nonlinear linearization results prove the exchange. Exactly one unstable real direction refers to the off-critical hyperbolic equilibria just treated.'),
(315,'Physical corollary has correct branch side and stability for each sign of $b$; orthant statements are off-critical.'),
(324,'Positive synchronous escape, with a fixed radius for each fixed $\\mu>0$, supplies an admissible trajectory proving relative instability.'),
(330,'Nonnegative invariance restricts stability; interior positive-branch instability and the separate away-from-zero root are correctly scoped.'),
(338,'Generic critical instability is in $\\U$; the $b<0$ orthant conclusion is expressly withheld.'),
(343,'Critical synchronous equation is exact.'),
(353,'Magnitude bound $|b|r^2/3$, sign choice for $r$, finite exit, domain preservation until exit and orthant limitation are correct.'),
(359,'Degenerate subsection/proposition opening does not assume genericity.'),
(367,'For $\\mu<0$ and $\\mu=0$, local root counts and stability types are correct; triple zero describes the scalar field.'),
(377,'Two roots for $\\mu>0$ are in $\\U$ locally; both are exponentially stable there; origin is unstable and only the positive root is nonnegative.'),
(382,'Translation to $g$ is correct; pitchfork and two-parameter unfolding are explicitly not asserted.'),
(388,'The transverse reduction applies without $b\\ne0$; both roots can be placed in a common local neighborhood with $r>-1$.'),
(393,'Critical cubic derivative is $-6A$; scalar zero multiplicity is exactly three.'),
(403,'Uniform eigenvalue is negative on both signed branches; transverse continuity and the earlier positive escape supply full off-critical conclusions.'),
(415,'The fixed-parameter center-stability theorem is stated with and satisfies all hypotheses; the neutral parameter direction is explicitly excluded.'),
(418,'Independent direct Lyapunov proof is at the fixed degenerate tuple in real mean/transverse coordinates.'),
(426,'Circulant column sums kill all linear-in-$y$ mean terms for every $r$; uniform transverse Taylor remainder is $O(\\norm y_2^2)$.'),
(432,'Vanishing transverse field on synchrony gives the exact integral factorization and the displayed operator $B:E\\to E$.'),
(436,'Operator norm of $B$ shrinks to zero; the quadratic-form estimate follows from unitary Fourier diagonalization, or explicitly its real symmetric part.'),
(444,'Radius choice is feasible with a fixed $K$; the $rR$ bound and denominator comparison give the strict negative derivative for both signs of $r$.'),
(450,'Compact sublevels lie in $\\U$ and the estimate neighborhood, are invariant, and ensure continuation and full asymptotic stability.'),
(460,'Sign preservation and convergence justify the reciprocal-square derivative limit, algebraic asymptotic, and impossibility of full exponential stability.'),
(471,'Codimension proposition concerns the positive physical parameter space and an algebraic meeting of loci only.'),
(480,'Gradients have rank two, the regular-level theorem applies, and the locus is nonempty.'),
(483,'The center zero remains spectrally simple; no double-zero claim.'),
(492,'P02 formulas give equality of loci iff $a=A$, at root zero; positive repeated root and saddle-node scope are correctly distinguished.'),
(500,'B02 resolution is limited to P09; NB07, frozen supporting role and exclusion of unfolding are respected.'),
(512,'Analytical checks are actually in the proof; computational provenance is separate and has been reproduced, without treating validation as proof.'),
(518,'Audit-priority preamble and IFT/slope priorities accurately identify the proof obligations.'),
(524,'Coefficient and center-normal-form audit requests preserve normalization and full-system completeness.'),
(528,'Spectral and physical-side priorities explicitly include negative states, collisions and open-domain versus orthant distinctions.'),
(534,'Degenerate Lyapunov and codimension priorities are correctly scoped; no named pitchfork/cusp classification is asserted.'),
(539,'Final exclusions retain the P10 boundary and all other forbidden later-module claims; closing environment is complete.')
]

records=[]; start=1
for end,reason in rows:
    assert end>=start
    records.append({'start':start,'end':end,'verdict':'PASS','reason_tex':reason})
    start=end+1
assert start==540
(HERE/'line_review.json').write_text(json.dumps({'audited_p09_sha256':'b2366edf1ff71199b7f1d02a58cf828148d9a697dfafc9e07e70a523e4f26680','line_count':539,'range_count':len(records),'all_lines_covered_once':True,'ranges':records},indent=2)+'\n')
parts=[r'\begin{longtable}{@{}p{0.11\textwidth}p{0.10\textwidth}p{0.70\textwidth}@{}}',r'\toprule Lines & Verdict & Finding\\\midrule\endhead']
for row in records:
    parts.append(f"{row['start']}--{row['end']} & \\pass & {row['reason_tex']}"+r'\\')
parts.extend([r'\bottomrule',r'\end{longtable}'])
p=HERE.parent/'A09_transcritical_bifurcation.tex'; source=p.read_text()
before,rest=source.split('% A09-LINE-LEDGER-START\n'); old,after=rest.split('% A09-LINE-LEDGER-END')
p.write_text(before+'% A09-LINE-LEDGER-START\n'+'\n'.join(parts)+'\n% A09-LINE-LEDGER-END'+after)
print(f'Inserted {len(records)} consecutive ranges covering all 539 lines.')
