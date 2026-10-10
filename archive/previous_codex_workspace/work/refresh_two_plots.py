"""Independent audit of the equations and numerical protocols in the supplied record.
Requires numpy, scipy, matplotlib. Run from the task directory.
No historical script is executed; results are recomputed here.
"""
from pathlib import Path
import json, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.signal import find_peaks
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Patch
OUT=Path('outputs/verified_figures'); OUT.mkdir(parents=True,exist_ok=True)
R={}; NAMES=['Wood','Fire','Earth','Metal','Water']
COL=['#26845b','#c74641','#a05aa1','#454b57','#347db6']
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':200})
PL=(1,1,1,1,1,1); PS=(2,.5,1,.5,.3)

def lin(t,x,a,b,c,d,g,h):
    return x*(a-b*x+c*np.roll(x,1)-d*np.roll(x,2)-g*np.roll(x,-1)-h*np.roll(x,-2))
def sat(t,x,a,k,c,g,h):
    return a*x-k*x*x+c*np.roll(x,1)/(1+x)-g*x/(1+np.roll(x,-2))-h*x*np.roll(x,2)
def eq_l(p):
    a,b,c,d,g,h=p; M=b+d+g+h-c
    return a/M if M>0 else np.nan
def roots_s(p):
    a,k,c,g,h=p; A=k+h; D=(A-a)**2+4*A*(a+c-g)
    if D<0:return []
    return sorted(set([v for v in ((a-A-np.sqrt(D))/(2*A),(a-A+np.sqrt(D))/(2*A)) if v>0]))
def eq_s(p):
    r=roots_s(p);return max(r) if r else np.nan

def jl(x,p):
    a,b,c,d,g,h=p; J=np.zeros((5,5))
    for i in range(5):
        J[i,i]=a-2*b*x[i]+c*x[(i-1)%5]-d*x[(i-2)%5]-g*x[(i+1)%5]-h*x[(i+2)%5]
        for off,v in [(-1,c),(-2,-d),(1,-g),(2,-h)]:J[i,(i+off)%5]=v*x[i]
    return J

def js(x,p):
    a,k,c,g,h=p; J=np.zeros((5,5))
    for i in range(5):
        s=1+x[i]; ta=x[(i+2)%5]
        J[i,i]=a-2*k*x[i]-c*x[(i-1)%5]/s**2-g/(1+ta)-h*x[(i-2)%5]
        J[i,(i-1)%5]=c/s; J[i,(i+2)%5]=g*x[i]/(1+ta)**2;J[i,(i-2)%5]=-h*x[i]
    return J

def eigs(m,p,x=None):
    if x is None:x=eq_l(p) if m=='lin' else eq_s(p)
    if not np.isfinite(x):return np.full(5,np.nan)
    return np.linalg.eigvals((jl if m=='lin' else js)(np.full(5,x),p))
def alpha(m,p):return np.max(eigs(m,p).real)
def cf_l(p):
    a,b,c,d,g,h=p; x=eq_l(p);th=2*np.pi*np.arange(5)/5
    return x*(-b+(c-g)*np.cos(th)-(d+h)*np.cos(2*th))
def cf_s(p):
    a,k,c,g,h=p;x=eq_s(p);s=1+x;th=2*np.pi*np.arange(5)/5
    D=a-2*k*x-c*x/s**2-g/s-h*x
    return D+c/s*np.cos(th)+x*(g/s**2-h)*np.cos(2*th)
def integrate(m,p,x0,T=120,method='DOP853',n=3001):
    r=solve_ivp(lin if m=='lin' else sat,(0,T),x0,args=p,method=method,
                rtol=1e-10,atol=1e-12,t_eval=np.linspace(0,T,n))
    if not r.success: raise RuntimeError(r.message)
    return r

def save(name,fig):
    fig.savefig(OUT/(name+'.png'),bbox_inches='tight');fig.savefig(OUT/(name+'.svg'),bbox_inches='tight');plt.close(fig)


R=json.loads(Path('outputs/audit_results.json').read_text())
fig,ax=plt.subplots(figsize=(7.5,4.5),layout='constrained')
ax.axvspan(0,1,color='#f9e8e6');ax.axvline(0,c='0.3',lw=1);ax.axhline(0,c='0.8',lw=.7)
for m,p,col,mk,lab in [('lin',PL,'#bb453d','o','Lin: all coefficients = 1'),('sat',PS,'#24628d','x','Modified: (2, 0.5, 1, 0.5, 0.3)')]:
    es=eigs(m,p);xe=eq_l(p) if m=='lin' else eq_s(p)
    R['baseline'][m]={'xstar':xe,'alpha':float(max(es.real)),'eigenvalues':[[float(z.real),float(z.imag)] for z in sorted(es,key=lambda z:-z.real)]}
    ax.scatter(es.real,es.imag,c=col,marker=mk,s=80,label=lab)
ax.set(xlabel=r'Re $\lambda$',ylabel=r'Im $\lambda$',xlim=(-2.6,.8),ylim=(-1.3,1.3),title='Local stability at the stated baseline parameters')
ax.legend(loc='lower right',fontsize=8);ax.grid(alpha=.18);save('01_baseline_eigenvalues',fig)
R['stable_lin_counterexample']={'params':[1,2,1,1,1,1],'xstar':eq_l((1,2,1,1,1,1)),'alpha':alpha('lin',(1,2,1,1,1,1))}

fig,axes=plt.subplots(1,2,figsize=(10.7,4.6),layout='constrained')
for ax,key,title in zip(axes,['conditional','unconditional'],['Among draws with positive balance','Among all 1,200 draws']):
    x=np.arange(3)
    for m,offset,col,lab in [('lin',-.18,'#c05b53','Lin'),('sat',.18,'#347aa2','Modified')]:
        vals=[100*R['monte_carlo'][s][m][key] for s in R['monte_carlo']]
        bars=ax.bar(x+offset,vals,.36,color=col,label=lab)
        for b,val in zip(bars,vals):ax.text(b.get_x()+b.get_width()/2,val+1.5,f'{val:.1f}%',ha='center',fontsize=8)
    ax.set_xticks(x,['Uniform','Ordered','Tiered']);ax.set(ylim=(0,111),ylabel='Draws with locally stable positive balance (%)',title=title);ax.legend(frameon=False,fontsize=8)
fig.suptitle('Stability frequencies depend on the specified sampling scheme',fontsize=13)
save('04_sampling_denominators',fig)
