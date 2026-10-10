"""Deterministic corroboration of DRAFT P08; not a proof or independent audit.
Run: python3 check_p08.py [output_directory]. Requires Python 3 and NumPy.
Original fields, differentiated matrices, and Fourier formulas are separate.
No random sampling, trajectory simulation, or later-module input is used.
"""
from pathlib import Path
from fractions import Fraction as F
import sys, json, math, platform, hashlib
import numpy as np
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
TOL=2e-10
records=[]; errors=[]; exact=[]

def need(ok,what):
    if not bool(ok): raise AssertionError(what)

def field(z,p,q,model):
    a,k,c,g,h=p; n=len(z)
    return np.array([a*z[i]-k*z[i]**2 + (c*z[i]*z[(i-1)%n] if model=='MB' else c*z[(i-1)%n]/(1+z[i])) - (g*z[i]*z[(i+q)%n] if model=='MB' else g*z[i]/(1+z[(i+q)%n])) -h*z[i]*z[(i-q)%n] for i in range(n)])

def matrix(z,p,q,model):
    a,k,c,g,h=p; n=len(z); A=np.zeros((n,n),complex)
    for i in range(n):
        prev,plus,minus=(i-1)%n,(i+q)%n,(i-q)%n
        A[i,i]+=a-2*k*z[i]
        if model=='MB':
            A[i,i]+=c*z[prev]-g*z[plus]-h*z[minus]
            A[i,prev]+=c*z[i]; A[i,plus]-=g*z[i]; A[i,minus]-=h*z[i]
        else:
            A[i,i]+=-c*z[prev]/(1+z[i])**2-g/(1+z[plus])-h*z[minus]
            A[i,prev]+=c/(1+z[i]); A[i,plus]+=g*z[i]/(1+z[plus])**2; A[i,minus]-=h*z[i]
    return A

def spectrum(s,p,n,q,model,equilibrium=True):
    a,k,c,g,h=p; th=2*np.pi*np.arange(n)/n
    if model=='MB':
        d=a+(-2*k+c-g-h)*s
        return d+s*(c*np.exp(-1j*th)-g*np.exp(1j*q*th)-h*np.exp(-1j*q*th))
    d=a-2*k*s-c*s/(1+s)**2-g/(1+s)-h*s
    return d+c/(1+s)*np.exp(-1j*th)+g*s/(1+s)**2*np.exp(1j*q*th)-h*s*np.exp(-1j*q*th)

def close(x,y,name):
    err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))/max(1.,float(np.max(np.abs(x))),float(np.max(np.abs(y))))
    need(err<TOL,name+f' error {err}'); errors.append((name,err)); return err

def selected(r,n):
    r=np.asarray(r).real[:n//2+1]; scale=max(1.,float(np.max(np.abs(r))))
    return [int(j) for j in range(len(r)) if max(r)-r[j] < TOL*scale]

def rule(chi,n):
    J=(n+1)//4; u=np.cos(2*np.pi*np.arange(n//2+1)/n); al=[2/(u[j]+u[j+1]) for j in range(J)]
    for j,t in enumerate(al):
        if abs(chi-t)<TOL*max(1,abs(t)): return [j,j+1]
        if chi<t: return [j]
    return [J]

def check_case(name,p,x,n,q=2,expected=None,expected_modes=None,save=True):
    p=np.array(p,float); a,k,c,g,h=p; M=k+g+h-c; mu=a+c-g
    need(min(p)>0 and M>0,'canonical common '+name); y=a/M
    states={'DM':float(x),'MB':float(y)}; out={'case':name,'n':n,'q':q,'parameters':p.tolist(),'M':float(M),'mu':float(mu),'amplitudes':states,'models':{}}
    for model,s in states.items():
        z=np.full(n,s); A=matrix(z,p,q,model); lam=spectrum(s,p,n,q,model)
        residual=field(z,p,q,model)
        # Residual scaled by the absolute original five-term magnitudes.
        if model=='MB': resscale=max(1,a*s+(k+c+g+h)*s*s)
        else: resscale=max(1,a*s+(k+h)*s*s+(c+g)*s/(1+s))
        reserr=float(max(abs(residual)))/resscale; need(reserr<TOL,name+' residual '+model)
        th=2*np.pi*np.arange(n)/n; Q=np.exp(1j*np.outer(np.arange(n),th))/np.sqrt(n)
        e=close(A@Q,Q*lam, name+' Fourier columns '+model)
        close(Q.conj().T@A@Q,np.diag(lam),name+' diagonalization '+model)
        close(A@A.conj().T,A.conj().T@A,name+' normality '+model)
        direct=np.linalg.eigvals(A); unmatched=list(direct)
        eigerr=0.
        for v in lam:
            j=min(range(len(unmatched)),key=lambda j:abs(unmatched[j]-v))
            eigerr=max(eigerr,abs(unmatched.pop(j)-v)/max(1,abs(v)))
        need(eigerr<TOL,name+' direct eigenvalues '+model)
        sa=float(max(lam.real)); modes=selected(lam.real,n)
        if q==2:
            chi=4*(g+h)/c if model=='MB' else 4*x*(h*(1+x)**2-g)/(c*(1+x))
            need(modes==rule(chi,n),name+' selected '+model)
        if model=='MB': close(lam[0],-a,name+' uniform MB')
        out['models'][model]={'original_residual_scaled':reserr,'spectrum_error_scaled':e,'direct_eigenvalue_error_scaled':float(eigerr),'abscissa':sa,'selected_representatives':modes,'eigenvalues_formula':[[float(v.real),float(v.imag)] for v in lam],'eigenvalues_direct':[[float(v.real),float(v.imag)] for v in direct]}
    if expected:
        for model,want in zip(['DM','MB'],expected):
            need((out['models'][model]['abscissa']<0)==(want=='stable'),name+' verdict '+model)
    if expected_modes:
        for model,want in zip(['DM','MB'],expected_modes): need(out['models'][model]['selected_representatives']==want,name+' expected labels '+model)
    if save: records.append(out)
    return out

# Exact rational residuals, complete original components, not spectral reductions.
def exact_case(name,p,x,y):
    a,k,c,g,h=map(F,p); x,y=F(x),F(y)
    for n in [5,6,7,8]:
        for q in sorted(set([1,2,n-1]+([n//2] if n%2==0 else []))):
            z=[x]*n; v=[y]*n
            for i in range(n):
                dm=a*z[i]-k*z[i]**2+c*z[(i-1)%n]/(1+z[i])-g*z[i]/(1+z[(i+q)%n])-h*z[i]*z[(i-q)%n]
                mb=a*v[i]-k*v[i]**2+c*v[i]*v[(i-1)%n]-g*v[i]*v[(i+q)%n]-h*v[i]*v[(i-q)%n]
                need(dm==0 and mb==0,'exact residual '+name)
    exact.append({'case':name,'parameters':list(map(str,p)),'DM_amplitude':str(x),'MB_amplitude':str(y),'original_component_residuals':'exactly zero'})

fwd=(F(1,4),F(1,8),F(1),F(1),F(1,8))
rev=(F(20301,1100),F(17,20),F(1,2),F(1,100),F(1))
both=(F(16351,1100),F(1,2),F(3,2),F(1,100),F(1))
revsel=(F(113,4),F(9),F(8),F(1),F(1))
uniform=(F(9,2),F(7),F(8),F(1),F(1))
for name,p,x,y in [('forward',fwd,1,1),('reverse_rational',rev,10,F(20301,1496)),('both_unstable',both,10,F(16351,11)),('reverse_selection',revsel,3,F(113,12)),('both_uniform_k_less_c',uniform,1,F(9,2))]: exact_case(name,p,x,y)
for h in [F(1,2),F(1),F(2)]: exact_case('curvature_'+str(h),(1+h,F(1),F(4),F(4),h),1,1)
eps=F(1,48); g=(1+eps)**3+2*eps; a=(1+eps)*(1+2*eps)+eps/(1+eps); p=(a,F(1),eps,g,eps)
exact_case('lower_n6',p,eps,a/(1+g)); exact_case('upper_n6',p,eps+eps/(1+eps)**2,a/(1+g))
# Exact seven-node root interval signs and all inequalities cited in proof.
poly=lambda u:8*u**3+4*u**2-4*u-1
intervals=[(F(31,50),F(63,100)),(F(-23,100),F(-11,50)),(F(-91,100),F(-9,10))]
for lo,hi in intervals: need(poly(lo)*poly(hi)<0,'root isolation')
reverse_lower=-F(17,20)-F(21,2420)-F(23,22000)+F(12099,12100)*F(9,10)
need(reverse_lower==F(9729,242000) and reverse_lower>F(1,25),'reverse lower certificate')
mb_bounds=[-F(17,20)+F(63,200)+F(101,100)*F(23,100),-F(17,20)-F(11,100)+F(101,100)*F(91,100),-F(17,20)-F(9,20)-F(101,100)*F(31,50)]
need(mb_bounds==[F(-3027,10000),F(-409,10000),F(-19262,10000)],'MB certificates')
need(-F(1,2)-F(63,2420)+F(12099,12100)==F(2867,6050),'both unstable certificate')
# Quadratic-field arithmetic for the irrational DM blow-up-comparison root.
# (u,v) represents u+v sqrt(33); division uses conjugation.
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]+33*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,r): return (a[0]*r,a[1]*r)
def div(a,b): return scale(mul(a,(b[0],-b[1])),1/(b[0]**2-33*b[1]**2))
x=(F(-1,4),F(1,4)); s=add((F(1),F(0)),x)
res=add(add(x,scale(mul(x,x),-2)),div(scale(x,3),s))
need(res==(0,0),'original irrational DM residual')
need(F(1)-2+F(2,2)==0,'M0 DM original residual')
exact.append({'case':'growth_and_blowup_DM','roots':['1','(sqrt(33)-1)/4'],'residual':'exact rational/quadratic-field original equation zero','MB_M':[0,-1]})
# All 5<=n<=32: forward contrast, uniform stable witness, parity reverse family,
# and lower-root family. No sampled point is used to prove a region.
for n in range(5,33):
    check_case('forward',fwd,1,n,expected=('stable','unstable'))
    check_case('both_uniform_k_less_c',uniform,1,n,expected=('stable','stable'),expected_modes=([0],[0]))
    if n%4==3:
        tau=math.sin(math.pi/(2*n)); h=1; c=tau; g=tau*tau/4; k=1-2.5*tau*tau; x=2/tau; a=(k+h)*x-(c-g)/(1+x)
        check_case('reverse_family',(a,k,c,g,h),x,n,expected=('unstable','stable'),expected_modes=([(n+1)//4],[(n+1)//4]))
    if n%4:
        rho=max(-np.cos(4*np.pi*np.arange(n)/n)); e=(1-rho)/24; g=(1+e)**3+2*e; a=(1+e)*(1+2*e)+e/(1+e)
        check_case('lower_family',(a,1,e,g,e),e,n,expected=('unstable','stable'))
for n in [5,6,7,8]:
    for name,p,x in [('reverse_rational',rev,10),('both_unstable',both,10),('reverse_selection',revsel,3)]: check_case(name,p,x,n)
check_case('reverse_rational',rev,10,7,expected=('unstable','stable'),expected_modes=([2],[2]))
check_case('both_unstable',both,10,8,expected=('unstable','unstable'),expected_modes=([2],[1]))
check_case('reverse_selection',revsel,3,8,expected=('stable','stable'),expected_modes=([2],[0]))
# Every ordered reachable pair, finite deterministic sample of dimensions.
for n in range(5,17):
    J=(n+1)//4; u=np.cos(2*np.pi*np.arange(n//2+1)/n); al=[2/(u[j]+u[j+1]) for j in range(J)]
    zs=[al[0]/2]+[(al[j-1]+al[j])/2 for j in range(1,J)]+[2*al[-1]]
    for jd,eta in enumerate(zs):
        for jb,zeta in enumerate(zs):
            c=4; S=zeta; x=1+eta/zeta; s=1+x; h=(zeta+s*eta/x)/(s*s+1); g=zeta-h; k=1+max(c+S,(c-g)/(x*s)-h); a=(k+h)*x-(c-g)/s
            check_case('all_pairs',(a,k,c,g,h),x,n,expected=('stable','stable'),expected_modes=([jd],[jb]))
# All MB positive midpoint ties and strict cells for n=5..32, with large k.
selection_tests=[]
for n in range(5,33):
    J=(n+1)//4; u=np.cos(2*np.pi*np.arange(n//2+1)/n); al=[2/(u[j]+u[j+1]) for j in range(J)]
    vals=[al[0]/2]+[(al[j-1]+al[j])/2 for j in range(1,J)]+[2*al[-1]]+al
    for chi in vals:
        c=4/chi; S=1; k=c+S+1; a=2; y=a/(k+S-c)
        A=matrix(np.full(n,y),(a,k,c,.5,.5),2,'MB'); lam=spectrum(y,(a,k,c,.5,.5),n,2,'MB')
        pred=rule(chi,n); need(selected(lam.real,n)==pred,'MB cell/tie')
        close(A@np.ones(n),-a*np.ones(n),'uniform in selection case')
        selection_tests.append({'n':n,'chi':chi,'selected':pred,'maximum':float(max(lam.real))})
# Collision and generic offsets; heterogeneous states derivative vs complex step.
collision=[]
for n in [5,6,7,8]:
    for q in sorted(set([1,2,n-1]+([n//2] if n%2==0 else []))):
        check_case('collision_equilibrium',rev,10,n,q=q)
        p=np.array([1.7,.8,2.3,1.2,.6]); z=np.linspace(.2,1.3,n)
        for model in ['DM','MB']:
            A=matrix(z,p,q,model); B=np.zeros_like(A)
            for j in range(n):
                zz=z.astype(complex); zz[j]+=1e-30j; B[:,j]=field(zz,p,q,model).imag/1e-30
            err=close(A,B,'complexstep_'+model)
            state=.7; Jh=matrix(np.full(n,state),p,q,model); lam=spectrum(state,p,n,q,model)
            Q=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
            close(Jh@Q,Q*lam,'nonequilibrium Fourier '+model)
            collision.append({'n':n,'q':q,'model':model,'complex_step_scaled_error':err})
# Maximum inequality at deterministic nonnegative states with multiple maxima.
max_checks=0
for n in [5,6,7,8]:
 for q in range(1,n):
  for p in [(1,2,1,3,4),(1,1,1,1,1),(1,.2,2,3,4)]:
   for z in [np.ones(n),np.arange(n)%3,np.array([0 if j%2 else 2 for j in range(n)])]:
    Y=max(z); dp=max(field(z,p,q,'MB')[z==Y]); a,k,c,g,h=p
    need(dp<=a*Y-(k-c)*Y*Y+1e-12,'maximum inequality'); max_checks+=1
# Analytic solution identity at exact rational E=exp(at), checked without integration.
for a,M,s0,E in [(F(2),F(3),F(1),F(2)),(F(1),F(0),F(2),F(3)),(F(1),F(-1),F(1),F(3,2))]:
 den=1+M*s0/a*(E-1); s=s0*E/den
 derivative=a*E*(s0*den-s0*E*M*s0/a)/(den*den)
 need(derivative==a*s-M*s*s,'scalar solution derivative exact')
summary={'status':'PASS','date':'2026-10-03','python':sys.version,'numpy':np.__version__,'platform':platform.platform(),'tolerance_scaled':TOL,'equilibrium_matrix_cases':len(records),'exact_equilibrium_families':len(exact),'selection_cell_tie_cases':len(selection_tests),'collision_complexstep_cases':len(collision),'maximum_inequality_cases':max_checks,'largest_scaled_matrix_error':max(e for _,e in errors),'largest_scaled_direct_eigenvalue_error':max(c['models'][m]['direct_eigenvalue_error_scaled'] for c in records for m in ['DM','MB']),'largest_scaled_original_equilibrium_residual':max(c['models'][m]['original_residual_scaled'] for c in records for m in ['DM','MB']),'seven_node_certificates':{'DM_lower':str(reverse_lower),'MB_upper':list(map(str,mb_bounds))},'interpretation':'Finite-precision corroboration, not interval certification, mathematical verification, or independent audit.'}
(OUT/'check_results.json').write_text(json.dumps({'summary':summary,'exact':exact,'equilibrium_cases':records,'selection_cases':selection_tests,'collision_checks':collision},indent=2)+'\n')
(OUT/'check_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
