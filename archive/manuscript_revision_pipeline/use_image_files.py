from pathlib import Path
import shutil,re,zipfile
root=Path('outputs');p=root/'WuXing_Preliminary_Comparisons.tex';s=p.read_text()
shutil.copy2(p,'work/latex_revision/before_image_replacement.tex')
a=s.index('\\definecolor{wxWood}');b=s.index('\\newcommand{\\PreliminaryReferenceFallback}',a)
s=s[:a]+s[b:]
s=s.replace('% Figures are embedded as TikZ for a standalone editable preview.','% Figures use ordinary image files in the figures folder.')
for i,cmd in enumerate(['PreliminaryEigenFigure','PreliminaryTrajectoryFigure','PreliminaryMapFigure'],1):
 s=s.replace('\\'+cmd,r'\includegraphics[width=\linewidth]{figures/figure'+str(i)+'.png}')
s=s.replace('classification. Of 8,100 grid points','stability landscape. Of 8,100 grid points')
a=s.index('\\caption{Local stability classifications');b=s.index('\\label{fig:stability-maps}',a)
s=s[:a]+r'''\caption{Stability maps on the verified $90\times90$ parameter grids.
Horizontal axis: nourishment $c$. Vertical axis: received restraint,
meaning $d$ in Lin and $h$ in the modified model.
Lin uses $(a,b,c,d,g,h)=(1.5,0.65,c,d,0.3,0.3)$; the modified model uses
$(a,k,c,g,h)=(1.5,0.65,c,0.3,h)$. Colors show the largest real part of
the Jacobian eigenvalues at the selected positive balanced equilibrium:
blue indicates negative values and red positive values. Color limits are
clipped, so the darkest colors also represent values beyond the displayed
scale. Gray denotes no positive balanced equilibrium; the black line is
an interpolated zero contour. Titles give the stable fraction among all
grid points, while inset labels condition on existence of positive balance.
These are specified slices of different complete models, including a fixed
child-loss coefficient $g=0.3$ in Lin; they do not isolate a single change
in interaction law.}
'''+s[b:]
s=s.replace('(Table~\\ref{tab:sampling}). For a shared conceptual draw','(Figure~\\ref{fig:sampling} and Table~\\ref{tab:sampling}). For a shared conceptual draw')
s=s.replace('267 / 1145  & 23.3 & 22.3','267 / 1145  & 23.3 & 22.2')
figure=r'''
\begin{figure}[tbp]
\centering
\includegraphics[width=\linewidth]{figures/figure4.png}
\caption{Stability frequencies under the uniform, ordered, and tiered
sampling schemes described in the text, with 1,200 draws per scheme and
seed 3. Left: the fraction with a locally stable positive balanced
equilibrium among draws admitting the selected positive balance. Right:
the fraction among all 1,200 draws. Exact counts are given in
Table~\ref{tab:sampling}. These percentages depend on the sampling
assumptions and eligibility rule; they are not probabilities that a model
is correct or physiologically healthy. The comparison changes several
mechanisms simultaneously and does not attribute the differences to one
interaction law.}
\label{fig:sampling}
\end{figure}

'''
s=s.replace('\\subsection{Interpretation and limitations of the preliminary comparison}',figure+'\\subsection{Interpretation and limitations of the preliminary comparison}')
# Avoid an unnecessary custom bibliography command as well.
a=s.index('\\newcommand{\\PreliminaryReferenceFallback}');b=s.index('\\begin{document}',a)
fallback=s[a:b]; bib=fallback[fallback.index('\\begin{thebibliography}'):fallback.index('\\end{thebibliography}')+len('\\end{thebibliography}')]
s=s[:a]+s[b:]
s=s.replace('\\PreliminaryReferenceFallback',bib)
p.write_text(s)
folder=root/'figures';folder.mkdir(exist_ok=True)
for i,name in enumerate(['01_baseline_eigenvalues','02_perturbation_recovery','03_corrected_stability_maps','04_sampling_denominators'],1):
 shutil.copy2(root/'verified_figures'/f'{name}.png',folder/f'figure{i}.png')
assert 'PreliminaryEigenFigure' not in s and 'PreliminaryTrajectoryFigure' not in s and 'PreliminaryMapFigure' not in s
assert len(re.findall(r'\\includegraphics',s))==4
labels=re.findall(r'\\label\{([^}]+)\}',s);refs=re.findall(r'\\ref\{([^}]+)\}',s)
assert set(refs)<=set(labels)
with zipfile.ZipFile(root/'WuXing_LaTeX_With_Figures.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.write(p,p.name)
 for f in sorted(folder.glob('figure[1-4].png')):z.write(f,'figures/'+f.name)
 z.writestr('README.txt','Open WuXing_Preliminary_Comparisons.tex as the main file. Keep the figures folder beside it. Use XeLaTeX, as required by the existing ctex package. All four plots use ordinary includegraphics commands. The existing network diagram remains in Section 2, so LaTeX numbers the four results figures 2 through 5 in the full manuscript. The original Chinese_med.bib and network.bib were not supplied; add them to restore the existing introduction references. Captions are in LaTeX, not embedded in the included PNGs.\n')
print('Saved ordinary LaTeX source and package with four images.')
