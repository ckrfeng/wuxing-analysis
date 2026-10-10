from pathlib import Path
source=Path('/Users/carterfeng/.codex/attachments/d8b39480-61c6-47e9-9bbe-e5eadc5b878b/Pasted text.txt').read_text()
start=source.index("\\section{Dynamics of Lin's Model}")
end=source.index('\\section{Conclusion and Discussion}',start)
s=source[:start]+Path('work/latex_revision/sections.tex').read_text()+'\n'+source[end:]
s=s.replace('\\usepackage{graphicx} % Required for inserting images\n','')
s=s.replace('\\begin{document}',Path('work/latex_revision/inline_figures.tex').read_text()+'\n\n\\begin{document}')
old='\\bibliography{Chinese_med,network}   % name your BibTeX data base'
new=r'''% The original bibliography files were not supplied with the pasted source.
% Restore both .bib files for the complete introduction bibliography.
\IfFileExists{Chinese_med.bib}{%
  \IfFileExists{network.bib}{\bibliography{Chinese_med,network}}{\PreliminaryReferenceFallback}%
}{\PreliminaryReferenceFallback}'''
s=s.replace(old,new)
fallback=r'''\newcommand{\PreliminaryReferenceFallback}{%
\begin{thebibliography}{99}
\bibitem{Lin2020} H. Lin and J. Han.
Analysis of Dynamic Five-Element Model.
In \emph{Proceedings of the 39th Chinese Control Conference},
pages 777--781, 2020.
\href{https://doi.org/10.23919/CCC50068.2020.9188438}{doi:10.23919/CCC50068.2020.9188438}.
\end{thebibliography}}
'''
s=s.replace('\\begin{document}',fallback+'\n\\begin{document}')
header='% Revised Sections 3 and 4: preliminary complete-model comparisons.\n% Figures are embedded as TikZ for a standalone editable preview.\n% Introduction and other unfinished sections retain the supplied prose.\n'
Path('outputs/WuXing_Preliminary_Comparisons.tex').write_text(header+s)
print('Saved editable manuscript:',len(s),'characters')
