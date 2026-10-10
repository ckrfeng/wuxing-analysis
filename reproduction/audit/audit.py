"""Reproduction audit for Lin and the nonnegative five-term modified model.
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

# Independent complex-step derivative check and Fourier eigenvalue check.
rng=np.random.default_rng(71);jacerr={};eigerr={};res={}
for m,n,fun,jfun,ef,cf in [('lin',6,lin,jl,eq_l,cf_l),('sat',5,sat,js,eq_s,cf_s)]:
    je=ee=rr=0
    for _ in range(1000):
        p=rng.uniform(.1,2,n);x=rng.uniform(.2,3,5)
        JC=np.column_stack([fun(0,x.astype(complex)+1e-25j*np.eye(5)[i],*p).imag/1e-25 for i in range(5)])
        je=max(je,float(np.max(np.abs(JC-jfun(x,p)))))
        xe=ef(p)
        if np.isfinite(xe):
            rr=max(rr,float(np.max(np.abs(fun(0,np.full(5,xe),*p)))))
            ee=max(ee,float(np.max(np.abs(np.sort(eigs(m,p).real)-np.sort(cf(p))))))
    jacerr[m]=je;eigerr[m]=ee;res[m]=rr
R['checks']={'jacobian_complex_step_max_abs_error':jacerr,'fourier_eigen_max_abs_error':eigerr,'equilibrium_residual_max_abs':res,'draws_per_model':1000}
R['baseline']={}
fig,ax=plt.subplots(figsize=(7.5,4.5),layout='constrained')
ax.axvspan(0,1,color='#f9e8e6');ax.axvline(0,c='0.3',lw=1);ax.axhline(0,c='0.8',lw=.7)
for m,p,col,mk,lab in [('lin',PL,'#bb453d','o','Lin: all coefficients = 1'),('sat',PS,'#24628d','x','Modified: (2, 0.5, 1, 0.5, 0.3)')]:
    es=eigs(m,p);xe=eq_l(p) if m=='lin' else eq_s(p)
    R['baseline'][m]={'xstar':xe,'alpha':float(max(es.real)),'eigenvalues':[[float(z.real),float(z.imag)] for z in sorted(es,key=lambda z:-z.real)]}
    ax.scatter(es.real,es.imag,c=col,marker=mk,s=80,label=lab)
ax.set(xlabel=r'Re $\lambda$',ylabel=r'Im $\lambda$',xlim=(-2.6,.8),ylim=(-1.3,1.3),title='Local stability at the stated baseline parameters')
ax.legend(loc='lower right',fontsize=8);ax.grid(alpha=.18);save('01_baseline_eigenvalues',fig)
R['stable_lin_counterexample']={'params':[1,2,1,1,1,1],'xstar':eq_l((1,2,1,1,1,1)),'alpha':alpha('lin',(1,2,1,1,1,1))}

# Reproduce original protocol; normalize states for a readable comparison.
fig,axes=plt.subplots(2,2,figsize=(10.4,6.3),layout='constrained');R['perturbations']=[]
for col,(m,p) in enumerate([('lin',PL),('sat',PS)]):
    xe=eq_l(p) if m=='lin' else eq_s(p)
    for row,factor in enumerate([1.05,.3]):
        x=np.full(5,xe);x[0]*=factor;s=integrate(m,p,x)
        check=integrate(m,p,x,method='RK45')
        R['perturbations'].append({'model':m,'wood_factor':factor,'initial_norm':float(np.linalg.norm(x-xe)),
             'final_norm':float(np.linalg.norm(s.y[:,-1]-xe)),'minimum_over_run':float(s.y.min()),
             'RK45_DOP853_max_abs_difference':float(np.max(np.abs(s.y-check.y)))})
        ax=axes[row,col]
        for i in range(5):ax.plot(s.t,s.y[i]/xe,c=COL[i],lw=1.05,label=NAMES[i])
        ax.axhline(1,c='0.6',ls='--',lw=.8)
        ax.set(xlabel='Model time',ylabel=r'$x_i / x^*$',title=f"{'Lin' if m=='lin' else 'Modified'}: Wood {'+5%' if row==0 else 'reduced to 30%'}")
        ax.set_xlim(0,120 if m=='lin' else 12)
fig.legend(NAMES,loc='outside lower center',ncol=5,frameon=False)
fig.suptitle('Response to a one-component initial disturbance',fontsize=13)
save('02_perturbation_recovery',fig)

# Both historical map windows and corrected master maps.
R['maps']={};maps=[]
for name,N,cs,rs in [('early',90,np.linspace(.05,2.5,90),np.linspace(.05,2,90)),('master',90,np.linspace(.3,1.6,90),np.linspace(.1,1,90))]:
    arr=[];stats={}
    for m in ['lin','sat']:
        z=np.full((N,N),np.nan)
        for iy,r in enumerate(rs):
            for ix,c in enumerate(cs):
                p=((1,1,c,1,1,r) if m=='lin' else (2,.5,c,.5,r)) if name=='early' else ((1.5,.65,c,r,.3,.3) if m=='lin' else (1.5,.65,c,.3,r))
                z[iy,ix]=alpha(m,p)
        valid=np.isfinite(z);stable=valid&(z < -1e-9)
        stats[m]={'stable':int(stable.sum()),'valid':int(valid.sum()),'total':N*N,'fraction_all':float(stable.mean()),'fraction_valid':float(stable.sum()/valid.sum()),'min':float(np.nanmin(z)),'max':float(np.nanmax(z))}
        arr.append(z)
    R['maps'][name]=stats
    if name=='master':maps=arr;mapcs=cs;maprs=rs
fig,axes=plt.subplots(1,2,figsize=(11,4.7),layout='constrained');vm=max(.5,np.nanpercentile(np.abs(np.concatenate([z.ravel() for z in maps])),90))
cmap=plt.get_cmap('RdBu_r').copy();cmap.set_bad('#b9bec6')
for ax,m,z in zip(axes,['lin','sat'],maps):
    im=ax.pcolormesh(mapcs,maprs,z,cmap=cmap,norm=TwoSlopeNorm(0,-vm,vm),shading='nearest')
    if np.nanmin(z)<0<np.nanmax(z):ax.contour(mapcs,maprs,z,levels=[0],colors='k',linewidths=1.4)
    st=R['maps']['master'][m]
    ax.set(xlabel='Nourishment coefficient c',ylabel='Received restraint d (Lin)' if m=='lin' else 'Received restraint h (modified)',title=f"{'Lin' if m=='lin' else 'Modified'}: {100*st['fraction_all']:.1f}% of all grid points stable")
    ax.text(.02,.025,f"Among positive balanced equilibria: {100*st['fraction_valid']:.1f}%",transform=ax.transAxes,fontsize=8,bbox={'fc':'white','ec':'none','alpha':.9})
    fig.colorbar(im,ax=ax,extend='both',label=r'$\max\mathrm{Re}\,\lambda$ (color limits clipped)')
fig.suptitle('Balanced-equilibrium stability on the master notebook grid',fontsize=13)
fig.legend(handles=[Patch(color='#b9bec6',label='No positive balanced equilibrium'),plt.Line2D([],[],c='k',label='Interpolated zero contour')],loc='outside lower center',ncol=2,frameon=False,fontsize=8)
save('03_corrected_stability_maps',fig)

# Reproduce exact seed and paired draw order, report both denominators.
TIERS={'SELF':(1,2),'SHENG':(.5,1.5),'SAT':(.3,1),'RESTR':(.2,.8),'TGT':(.1,.5),'CHILD':(.1,.5)}
def draw(r,scheme):
    if scheme=='tiered':return {k:r.uniform(*v) for k,v in TIERS.items()}
    while True:
        S,A,SH,RE,TG,CH=r.uniform(.1,2,6)
        if scheme=='full_order' and not S>SH>RE>TG:continue
        return dict(SELF=S,SAT=A,SHENG=SH,RESTR=RE,TGT=TG,CHILD=CH)
def to_p(m,d):
    return (d['SELF'],d['SAT'],d['SHENG'],d['RESTR'],d['CHILD'],d['TGT']) if m=='lin' else (d['SELF'],d['SAT'],d['SHENG'],d['TGT'],d['RESTR'])
def wilson(k,n):
    z=1.96;p=k/n;den=1+z*z/n;ctr=(p+z*z/(2*n))/den;h=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return [ctr-h,ctr+h]
R['monte_carlo']={}
for scheme in ['uniform','full_order','tiered']:
    r=np.random.default_rng(3);v={m:[] for m in ['lin','sat']}
    for _ in range(1200):
        d=draw(r,scheme)
        for m in v:v[m].append(alpha(m,to_p(m,d)))
    ss={};common=np.isfinite(v['lin'])&np.isfinite(v['sat'])
    for m,z in v.items():
        z=np.array(z);va=np.isfinite(z);st=va&(z<0);ns,nv=int(st.sum()),int(va.sum())
        ss[m]={'stable':ns,'valid':nv,'total':1200,'conditional':ns/nv,'unconditional':ns/1200,'wilson_conditional':wilson(ns,nv),'both_exist_n':int(common.sum()),'both_exist_stable_fraction':float(np.mean(z[common]<0))}
    R['monte_carlo'][scheme]=ss
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
# Child ablation same seeds as record, plus counts.
R['child_ablation']={}
for name,m,n in [('full','lin',6),('no_child','lin',6),('modified','sat',5)]:
    r=np.random.default_rng(11);st=va=0
    for _ in range(3000):
        p=r.uniform(.1,2,n)
        if name=='no_child':p[4]=0
        z=alpha(m,p)
        if np.isfinite(z):va+=1;st+=int(z<0)
    R['child_ablation'][name]={'stable':st,'valid':va,'total':3000,'conditional':st/va}

# Locate actual crossings with sign-checked brackets; calculate transversality.
R['crossings']=[]
for c in [.5,1,1.5,2]:
    f=lambda h:alpha('sat',(1.5,.65,c,.5,h))
    hs=np.linspace(.05,20,1000);brackets=[(lo,hi) for lo,hi in zip(hs[:-1],hs[1:]) if f(lo)*f(hi)<0]
    for lo,hi in brackets:
        hc=brentq(f,lo,hi,xtol=1e-13);es=eigs('sat',(1.5,.65,c,.5,hc));z=es[np.argmax(es.real)]
        R['crossings'].append({'c':c,'hc':hc,'frequency':float(abs(z.imag)),'derivative':float((f(hc+1e-5)-f(hc-1e-5))/2e-5),'xstar':eq_s((1.5,.65,c,.5,hc))})
R['p4_slice_max_h_2_alpha']=alpha('sat',(1.5,.65,1,.5,2))
R['bistability']={str(x):float(max(eigs('sat',(2,.5,.1,2.5,.3),x).real)) for x in [0,.5,1]}
R['bistable_branch_scan']={'upper_max_alpha':-np.inf,'lower_min_alpha':np.inf}
for g in np.linspace(2.10001,2.54999,1000):
    roots=roots_s((2,.5,.1,g,.3));a=[max(eigs('sat',(2,.5,.1,g,.3),x).real) for x in roots]
    R['bistable_branch_scan']['upper_max_alpha']=float(max(R['bistable_branch_scan']['upper_max_alpha'],a[1]));R['bistable_branch_scan']['lower_min_alpha']=float(min(R['bistable_branch_scan']['lower_min_alpha'],a[0]))

# Repeat key Lin reproduction; no regime labels inferred from visual irregularity.
s=integrate('lin',PL,np.arange(1.,6),T=300,n=30001);mask=s.t>150;pk=find_peaks(s.y[1,mask])[0]
R['lin_period']=float(np.diff(s.t[mask][pk]).mean())
s=integrate('lin',(0,0,0,1,0,1),np.arange(1.,6),T=60);R['restriction_end']=s.y[:,-1].tolist()
R['symmetric_subspace']={'baseline_all_equal_limit':1/3,'transverse_alpha':alpha('lin',PL),
    'c3_9_scalar_limit':10.,'record_claimed_max':131.,'explanation':'The exact symmetric scalar trajectory from 1 increases monotonically to 10; larger excursions indicate loss of symmetry/numerical error, not this scalar trajectory.'}

# Variational QR Lyapunov estimates using an independently implemented loop.
print('Core checks complete; computing Lyapunov convergence.',flush=True)
def lin_fast(x,p):
    a,b,c,d,g,h=p
    return np.array([x[i]*(a-b*x[i]+c*x[(i-1)%5]-d*x[(i-2)%5]-g*x[(i+1)%5]-h*x[(i+2)%5]) for i in range(5)])
def spectrum(p,T=2000):
    x=solve_ivp(lambda t,x:lin_fast(x,p),(0,100),np.arange(1.,6),method='DOP853',rtol=1e-10,atol=1e-12).y[:,-1]
    Q=np.eye(5);acc=np.zeros(5);data={}
    def rhs(t,Y):
        x=Y[:5];return np.r_[lin_fast(x,p),(jl(x,p)@Y[5:].reshape(5,5)).ravel()]
    for step in range(1,int(T/.5)+1):
        sol=solve_ivp(rhs,(0,.5),np.r_[x,Q.ravel()],method='DOP853',rtol=1e-10,atol=1e-12)
        if not sol.success:raise RuntimeError(sol.message)
        x=sol.y[:5,-1];Q,Rq=np.linalg.qr(sol.y[5:,-1].reshape(5,5));acc+=np.log(abs(np.diag(Rq)))
        if step in [1000,2000,3000,4000]:data[str(step*.5)]=np.sort(acc/(step*.5))[::-1].tolist()
    return data
R['lyapunov_conservative']=spectrum((0,0,1,0,1,0))
R['lyapunov_periodic']=spectrum(PL,T=1500)
R['lin_paper_chaos_spectrum_sum']=sum([.6700,.6606,-.0761,-.0794,-1.1751])
Path('outputs/audit_results.json').write_text(json.dumps(R,indent=2))
print(json.dumps(R,indent=2),flush=True)
