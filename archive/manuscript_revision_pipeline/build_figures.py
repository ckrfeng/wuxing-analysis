from pathlib import Path
import ast,json
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path.cwd()
ns={'np':np,'solve_ivp':solve_ivp}
tree=ast.parse((ROOT/'work/clean_package/audit.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'<retained functions>','exec'),ns)
R=json.loads((ROOT/'outputs/audit_results.json').read_text())
colors=['wxWood','wxFire','wxEarth','wxMetal','wxWater']
lines=[r'\definecolor{wxWood}{HTML}{26845B}',r'\definecolor{wxFire}{HTML}{C74641}',r'\definecolor{wxEarth}{HTML}{A05AA1}',r'\definecolor{wxMetal}{HTML}{454B57}',r'\definecolor{wxWater}{HTML}{347DB6}',r'\definecolor{wxStable}{HTML}{347AA2}',r'\definecolor{wxUnstable}{HTML}{C05B53}',r'\definecolor{wxMissing}{HTML}{B9BEC6}']
def node(x,y,text,opts=''):
 return rf'\node[{opts}] at ({x:.4f},{y:.4f}) {{{text}}};'
def plot_axes(x,y,w,h,xlim,ylim,xticks,yticks,xlabel,ylabel,title):
 out=[]
 def X(t):return x+w*(t-xlim[0])/(xlim[1]-xlim[0])
 def Y(t):return y+h*(t-ylim[0])/(ylim[1]-ylim[0])
 for t in xticks:
  xx=X(t);out.append(rf'\draw[gray!25] ({xx:.4f},{y:.4f}) -- ({xx:.4f},{y+h:.4f});')
  out.append(node(xx,y-.18,f'{t:g}','anchor=north'))
 for t in yticks:
  yy=Y(t);out.append(rf'\draw[gray!25] ({x:.4f},{yy:.4f}) -- ({x+w:.4f},{yy:.4f});')
  out.append(node(x-.12,yy,f'{t:g}','anchor=east'))
 out.append(rf'\draw[black!60] ({x:.4f},{y:.4f}) rectangle ({x+w:.4f},{y+h:.4f});')
 out.extend([node(x+w/2,y-.65,xlabel),node(x-.65,y+h/2,ylabel,'rotate=90'),node(x+w/2,y+h+.3,title,'font=\small')])
 return out,X,Y
# Spectrum figure.
lines.append(r'\newcommand{\PreliminaryEigenFigure}{%')
lines.append(r'\begin{tikzpicture}[x=1cm,y=1cm,font=\scriptsize]')
a,X,Y=plot_axes(1,1.2,10.8,4.7,(-2.6,.8),(-1.3,1.3),[-2.5,-2,-1.5,-1,-.5,0,.5],[-1,-.5,0,.5,1],r'$\operatorname{Re}\lambda$',r'$\operatorname{Im}\lambda$','Baseline equilibrium spectra')
lines+=a
lines.append(rf'\draw[black,thick] ({X(0):.4f},{Y(-1.3):.4f}) -- ({X(0):.4f},{Y(1.3):.4f});')
for model,col in [('lin','wxUnstable'),('sat','wxStable')]:
 for real,imag in R['baseline'][model]['eigenvalues']:
  xx,yy=X(real),Y(imag)
  if model=='lin':lines.append(rf'\draw[{col},thick] ({xx:.4f},{yy:.4f}) circle (0.07);')
  else:lines.append(rf'\draw[{col},thick] ({xx-.06:.4f},{yy-.06:.4f}) -- ({xx+.06:.4f},{yy+.06:.4f}) ({xx-.06:.4f},{yy+.06:.4f}) -- ({xx+.06:.4f},{yy-.06:.4f});')
lines.extend([node(3,.05,r'\textcolor{wxUnstable}{$\circ$ Lin}'),node(8,.05,r'\textcolor{wxStable}{$\times$ Modified}'),r'\end{tikzpicture}}'])
# Perturbation figure, same integrations and displayed windows as verified figure.
lines.extend([r'\newcommand{\PreliminaryTrajectoryFigure}{%',r'\begin{tikzpicture}[x=1cm,y=1cm,font=\scriptsize]'])
for col,(m,p) in enumerate([('lin',(1,1,1,1,1,1)),('sat',(2,.5,1,.5,.3))]):
 s=ns['eq_l'](p) if m=='lin' else ns['eq_s'](p)
 for row,factor in enumerate([1.05,.3]):
  init=np.full(5,s);init[0]*=factor;sol=ns['integrate'](m,p,init)
  previous=next(t for t in R['perturbations'] if t['model']==m and t['wood_factor']==factor)
  assert abs(np.linalg.norm(sol.y[:,-1]-s)-previous['final_norm'])<1e-8
  T=120 if m=='lin' else 12; mask=sol.t<=T;ts=sol.t[mask];values=sol.y[:,mask]/s
  # Sampling every third point for the long Lin panels; all points for DM.
  if m=='lin':ts=ts[::3];values=values[:,::3]
  ymax=4.1 if m=='lin' else 1.25
  assert values.min()>=0 and values.max()<ymax,(m,values.max())
  x=1+col*7;y=5.1-row*4.05
  title=('Lin' if m=='lin' else 'Modified')+(': Wood $+5\\%$' if row==0 else ': Wood at $30\\%$')
  a,X,Y=plot_axes(x,y,5.75,2.75,(0,T),(0,ymax),[0,40,80,120] if m=='lin' else [0,4,8,12],[0,1,2,3,4] if m=='lin' else [0,.5,1],r'Model time',r'$x_i/s$',title)
  lines+=a;lines.append(rf'\draw[gray,dashed] ({X(0):.4f},{Y(1):.4f}) -- ({X(T):.4f},{Y(1):.4f});')
  for j in range(5):
   coords=' '.join(f'({X(t):.4f},{Y(v):.4f})' for t,v in zip(ts,values[j]))
   lines.append(rf'\draw[{colors[j]},line width=0.45pt] plot coordinates {{{coords}}};')
for j,name in enumerate(['Wood','Fire','Earth','Metal','Water']):
 x=1.3+2.7*j;lines.append(rf'\draw[{colors[j]},thick] ({x:.4f},-0.05) -- ({x+.45:.4f},-0.05);');lines.append(node(x+.55,-.05,name,'anchor=west'))
lines.append(r'\end{tikzpicture}}')
# Categorical rendering of the verified 90-by-90 grid; merge equal-color runs.
lines.extend([r'\newcommand{\PreliminaryMapFigure}{%',r'\begin{tikzpicture}[x=1cm,y=1cm,font=\scriptsize]'])
cs=np.linspace(.3,1.6,90);rs=np.linspace(.1,1,90)
for col,m in enumerate(['lin','sat']):
 grid=np.empty((90,90),dtype=int)
 for iy,r in enumerate(rs):
  for ix,c in enumerate(cs):
   p=(1.5,.65,c,r,.3,.3) if m=='lin' else (1.5,.65,c,.3,r)
   a=ns['alpha'](m,p)
   grid[iy,ix]=2 if not np.isfinite(a) else (0 if a<-1e-9 else (1 if a>1e-9 else 3))
 assert (grid==0).sum()==R['maps']['master'][m]['stable']
 assert (grid!=2).sum()==R['maps']['master'][m]['valid']
 assert not np.any(grid==3)
 x=1+7*col;y=1.2;w=5.75;h=4.1
 for iy,row in enumerate(grid):
  start=0
  for end in range(1,91):
   if end==90 or row[end]!=row[start]:
    # Grid sites are equally spaced, with half-width end cells.
    xl=x+w*max(0,start-.5)/89;xr=x+w*min(89,end-.5)/89
    yl=y+h*max(0,iy-.5)/89;yr=y+h*min(89,iy+.5)/89
    color=['wxStable','wxUnstable','wxMissing'][row[start]]
    lines.append(rf'\fill[{color}] ({xl:.4f},{yl:.4f}) rectangle ({xr:.4f},{yr:.4f});')
    start=end
 a,_,_=plot_axes(x,y,w,h,(.3,1.6),(.1,1),[.3,.6,.9,1.2,1.6],[.1,.4,.7,1],r'Nourishment $c$',r'Received restraint $r$',('Lin: $18.5\\%$ of all points stable' if m=='lin' else 'Modified: $100\\%$ of all points stable'))
 lines+=a
for j,(color,label) in enumerate([('wxStable','Stable'),('wxUnstable','Unstable'),('wxMissing','No positive balance')]):
 x=1.5+4.1*j;lines.append(rf'\fill[{color}] ({x:.4f},-.05) rectangle ({x+.3:.4f},.15);');lines.append(node(x+.45,.05,label,'anchor=west'))
lines.append(r'\end{tikzpicture}}')
(ROOT/'work/latex_revision/inline_figures.tex').write_text('\n'.join(lines))
print('Inline figure source:',len('\n'.join(lines)),'characters')
