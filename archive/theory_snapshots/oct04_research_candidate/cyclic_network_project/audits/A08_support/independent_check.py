#!/usr/bin/env python3
"""Independent A08 corroboration; no draft validation code is imported.
Run with Python 3 and NumPy. Decimal checks are not interval certificates.
All-n conclusions are proved in the audit, not inferred from this run.
"""
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from pathlib import Path
import json, math, sys, platform
import numpy as np

HERE = Path(__file__).resolve().parent
plan = json.loads((HERE / 'expected_counts.json').read_text())
getcontext().prec = 80
PI = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117')
TOL = D('1e-65')
stats = {'checks': 0, 'largest_scaled_residual': D(0)}
records = []

def check(ok, message):
    stats['checks'] += 1
    if not ok:
        raise AssertionError(message)

def dec(x):
    if isinstance(x, F):
        return D(x.numerator)/D(x.denominator)
    return D(x)

def cosine(x):
    x %= 2*PI
    if x > PI:
        x -= 2*PI
    term = total = D(1)
    j = 0
    while abs(term) > D('1e-86'):
        j += 1
        term *= -x*x/D((2*j-1)*(2*j))
        total += term
    return total

def sine(x):
    return cosine(PI/2-x)

grids = {n: [cosine(2*PI*m/n) for m in range(n)] for n in plan['dimensions']}

def coeffs(p, x):
    a,k,c,g,h = p
    s = 1+x
    return -k*x-c*(1+2*x)/(s*s), c/s, g*x/(s*s), h*x

def residual(p,x,model):
    a,k,c,g,h = p
    terms = [a*x,-k*x*x,c*x/(1+x),-g*x/(1+x),-h*x*x] if model == 'DM' else [a*x,-k*x*x,c*x*x,-g*x*x,-h*x*x]
    return sum(terms)/max(D(1),sum(abs(t) for t in terms))

def evaluate(n, p, x, name, expected=None, full=False):
    p = tuple(map(dec,p)); x = dec(x)
    a,k,c,g,h = p
    M=k+g+h-c
    check(min(p)>0 and x>0 and M>0, name+' positivity')
    y=a/M
    for model,z in [('DM',x),('MB',y)]:
        err=abs(residual(p,z,model))
        stats['largest_scaled_residual']=max(stats['largest_scaled_residual'],err)
        check(err<TOL,name+' original '+model+' residual')
    d,C,G,H=coeffs(p,x)
    cs=grids[n]
    dm=[d+C*cs[m]+(G-H)*cs[(2*m)%n] for m in range(n)]
    mb=[y*(-k+c*cs[m]-(g+h)*cs[(2*m)%n]) for m in range(n)]
    ds=max(dm); bs=max(mb)
    sel_d=[m for m in range(n//2+1) if abs(dm[m]-ds)<TOL]
    sel_b=[m for m in range(n//2+1) if abs(mb[m]-bs)<TOL]
    gap_d=sorted(dm[:n//2+1],reverse=True)[0]-sorted(dm[:n//2+1],reverse=True)[1]
    gap_b=sorted(mb[:n//2+1],reverse=True)[0]-sorted(mb[:n//2+1],reverse=True)[1]
    check(abs(mb[0]+a)<TOL*max(1,a),name+' MB zero mode')
    check(abs(dm[0]-x*(-k-h-(c-g)/(1+x)**2))<TOL*max(1,abs(dm[0])),name+' DM scalar derivative')
    rec={'name':name,'n':n,'parameters':p,'x':x,'y':y,'M':M,'mu':a+c-g,'DM_selected':sel_d,'MB_selected':sel_b,'DM_sa':ds,'MB_sa':bs,'DM_rep_gap':gap_d,'MB_rep_gap':gap_b,'DM_Bx':dm[0]/x}
    if expected:
        jd,jb,sd,sb=expected
        check(sel_d==[jd] and sel_b==[jb],name+' selections')
        check(sd*ds>0 and sb*bs>0,name+' stability')
    if full:
        rec['DM_spectrum']=[(dm[m],-C*sine(2*PI*m/n)+(G+H)*sine(4*PI*m/n)) for m in range(n)]
        rec['MB_spectrum']=[(mb[m],y*(-c*sine(2*PI*m/n)+(h-g)*sine(4*PI*m/n))) for m in range(n)]
    records.append(rec)
    return rec

counts={k:0 for k in ['universal_witness','ordered_pairs','reverse_family','lower_family','MB_strict_cells','MB_ties','collision_nq']}
for n in plan['dimensions']:
    J=(n+1)//4
    cs=grids[n]
    beta=[(cs[j]+cs[j+1])/2 for j in range(n//2)]
    check(sum(b>TOL for b in beta)==J,'positive midpoint count')
    alpha=[1/beta[j] for j in range(J)]
    z=[alpha[0]/2]+[(alpha[j-1]+alpha[j])/2 for j in range(1,J)]+[2*alpha[-1]]
    p=tuple(map(dec,[F(1,4),F(1,8),1,1,F(1,8)]))
    rec=evaluate(n,p,1,'universal',full=n<=8)
    check(rec['DM_selected']==[0] and abs(rec['DM_sa']+D(1)/4)<TOL,'forward DM')
    check(len(rec['MB_selected'])==1 and rec['MB_selected'][0]>0 and rec['MB_sa']>=D(3)/16,'forward MB')
    check(1+cs[J]-D(9)/4*cs[J]**2>=D(3)/16,'actual J lower bound')
    counts['universal_witness']+=1
    for jd,eta in enumerate(z):
        for jb,zeta in enumerate(z):
            c=D(4); x=1+eta/zeta; s=1+x
            h=(zeta+s*eta/x)/(s*s+1); g=zeta-h
            k=max(c+zeta,(c-g)/(x*s)-h)+1
            a=(k+h)*x-(c-g)/s
            rec=evaluate(n,(a,k,c,g,h),x,'ordered_pair',expected=(jd,jb,-1,-1))
            check(rec['mu']>0,'pair unique branch')
            check(abs(4*(g+h)/c-zeta)<TOL and abs(4*x*(h*s*s-g)/(c*s)-eta)<TOL,'independent controls')
            counts['ordered_pairs']+=1
    for j,chi in enumerate(z):
        c=4/chi; k=max(D(0),c-1)+2
        vals=[-k+c*u-(2*u*u-1) for u in cs[:n//2+1]]
        check(vals.index(max(vals))==j,'MB strict cell')
        counts['MB_strict_cells']+=1
    for j,b in enumerate(beta[:J]):
        c=4*b; k=max(D(0),c-1)+2
        vals=[-k+c*u-(2*u*u-1) for u in cs[:n//2+1]]
        selected=[i for i,v in enumerate(vals) if abs(v-max(vals))<TOL]
        check(selected==[j,j+1],'MB maximal tie')
        counts['MB_ties']+=1
    if n%4==3:
        tau=sine(PI/(2*n)); g=tau*tau/4; c=tau; h=D(1)
        k=1-D(5)/2*tau*tau; x=2/tau
        a=(k+h)*x-(c-g)/(1+x)
        rec=evaluate(n,(a,k,c,g,h),x,'reverse_family',expected=(J,J,1,-1))
        check(rec['mu']>0 and rec['DM_sa']/x>D(91)/256*tau*tau,'reverse analytic margin')
        counts['reverse_family']+=1
    if n%4:
        rho=max(-cs[(2*m)%n] for m in range(n))
        eps=(1-rho)/24
        a=(1+eps)*(1+2*eps)+eps/(1+eps)
        p=(a,D(1),eps,(1+eps)**3+2*eps,eps)
        rec=evaluate(n,p,eps,'lower_family',full=n==6)
        check(rec['mu']<0 and rec['DM_selected']==[0] and rec['DM_sa']>0 and rec['MB_sa']<0,'lower branch contrast')
        check(abs(rec['DM_sa']-eps**2/(1+eps)**2)<TOL,'lower exact uniform value')
        check(abs(residual(p,eps+eps/(1+eps)**2,'DM'))<TOL,'second positive root')
        check(rec['MB_sa']/rec['y']<-D(13)/24*(1-rho),'lower MB margin')
        counts['lower_family']+=1

# Every explicit rational equilibrium in the draft: exact original residuals.
exact_witnesses=[('dissipative_k_lt_c',8,[F(9,2),7,8,1,1],1),('reverse_selection',8,[F(113,4),9,8,1,1],3),('forward',8,[F(1,4),F(1,8),1,1,F(1,8)],1),('reverse_rational',7,[F(20301,1100),F(17,20),F(1,2),F(1,100),1],10),('both_unstable',8,[F(16351,1100),F(1,2),F(3,2),F(1,100),1],10)]
for h in [F(1,2),F(1),F(2)]:
    exact_witnesses.append(('curvature_'+str(h),8,[1+h,1,4,4,h],1))
e=F(1,48)
exact_witnesses.append(('lower_rational',6,[(1+e)*(1+2*e)+e/(1+e),1,e,(1+e)**3+2*e,e],e))
exact=[]
for name,n,p,x in exact_witnesses:
    a,k,c,g,h=map(F,p); x=F(x); M=k+g+h-c; y=a/M
    fdm=a*x-k*x*x+c*x/(1+x)-g*x/(1+x)-h*x*x
    fmb=a*y-k*y*y+c*y*y-g*y*y-h*y*y
    check(fdm==0 and fmb==0,name+' rational residuals')
    rec=evaluate(n,p,x,name,full=True)
    exact.append({'name':name,'parameters':list(map(str,p)),'x':str(x),'y':str(y),'M':str(M),'residual_DM':str(fdm),'residual_MB':str(fmb)})

# Audit assertions about the explicit examples, including the source error.
named={r['name']:r for r in records if r['name'] not in ['ordered_pair','universal','reverse_family','lower_family']}
for name,jd,jb,sd,sb in [('dissipative_k_lt_c',0,0,-1,-1),('reverse_selection',2,0,-1,-1),('forward',0,2,-1,1),('reverse_rational',2,2,1,-1),('both_unstable',2,1,1,1),('lower_rational',0,1,1,-1)]:
    r=named[name]
    check(r['DM_selected']==[jd] and r['MB_selected']==[jb] and sd*r['DM_sa']>0 and sb*r['MB_sa']>0,name+' claimed explicit behavior')
source_checks={'E01':{'source_lines':[534,535],'claim':'Universal witness selects MB representative 1 for n=5,6,7,8.','observed':{str(r['n']):r['MB_selected'] for r in records if r['name']=='universal' and r['n']<=8},'exact_n8_MB_real_parts':['-1/4','-1/8+sqrt(2)/2','1','-1/8-sqrt(2)/2','-9/4'],'correct_n8_representative':2,'status':'FALSE example label; MINOR ISSUE; universal theorem unaffected'}}
(HERE/'source_claim_checks.json').write_text(json.dumps(source_checks,indent=2)+'\n')

# Both structural growth witnesses, outside the common positive-equilibrium domain.
growth=[]
for c,x in [(D(3),D(1)),(D(4),(D(33).sqrt()-1)/4)]:
    p=(D(1),D(1),c,D(1),D(1)); M=3-c
    check(abs(residual(p,x,'DM'))<TOL,'growth example DM residual')
    s=D('1.7')
    check(sum([s,-s*s,c*s*s,-s*s,-s*s])==s-M*s*s,'growth original MB scalar field')
    d,C,G,H=coeffs(p,x)
    growth.append({'parameters':p,'M':M,'DM_x':x,'DM_coefficients':[d,C,G,H],'MB_positive_root':None,'s0':1,'MB_solution':'exp(t)' if M==0 else 'exp(t)/(2-exp(t))','blowup_time':None if M==0 else 'log(2)'})

# Exact seventh-root isolation signs and all inequalities quoted at L633--653.
poly=lambda u:8*u**3+4*u*u-4*u-1
intervals=[(F(31,50),F(63,100)),(F(-23,100),F(-11,50)),(F(-91,100),F(-9,10))]
signs=[(-1,1),(1,-1),(-1,1)]
for (l,r),(sl,sr) in zip(intervals,signs):
    check(sl*poly(l)>0 and sr*poly(r)>0,'seventh cubic endpoint sign')
upper=[-F(17,20)+F(63,200)+F(101,100)*F(23,100),-F(17,20)-F(11,100)+F(101,100)*F(91,100),-F(17,20)-F(9,20)-F(101,100)*F(31,50)]
check(upper==[F(-3027,10000),F(-409,10000),F(-19262,10000)],'seventh exact MB upper bounds')
check(-F(17,20)-F(21,2420)-F(23,22000)+F(12099,12100)*F(9,10)==F(9729,242000),'seventh DM margin')

# Original-field numerical differentiation and direct Fourier action.
def field(v,p,q,model):
    a,k,c,g,h=p
    vprev=np.roll(v,1); vpq=np.roll(v,-q); vmq=np.roll(v,q)
    return a*v-k*v*v+c*vprev/(1+v)-g*v/(1+vpq)-h*v*vmq if model=='DM' else a*v-k*v*v+c*v*vprev-g*v*vpq-h*v*vmq

matrix_results=[]; max_results=[]
for n in plan['dimensions']:
    for q in sorted(set([1,n-1]+([n//2] if n%2==0 else []))):
        p=np.array([4.5,7.,8.,1.,1.]); x=1.; y=4.5
        theta=2*np.pi*np.arange(n)/n
        Q=np.exp(1j*np.outer(np.arange(n),theta))/np.sqrt(n)
        for model,z in [('DM',x),('MB',y)]:
            v=np.full(n,z); jac=np.empty((n,n))
            for j in range(n):
                pert=v.astype(complex); pert[j]+=1e-25j
                jac[:,j]=np.imag(field(pert,p,q,model))/1e-25
            a,k,c,g,h=p
            if model=='MB':
                lam=y*(-k+c*np.exp(-1j*theta)-g*np.exp(1j*q*theta)-h*np.exp(-1j*q*theta))
            else:
                d=a-2*k*x-c*x/(1+x)**2-g/(1+x)-h*x
                lam=d+c/(1+x)*np.exp(-1j*theta)+g*x/(1+x)**2*np.exp(1j*q*theta)-h*x*np.exp(-1j*q*theta)
            scale=max(1.,np.linalg.norm(jac,2))
            err=np.max(np.abs(jac@Q-Q*lam))/scale
            normerr=np.max(np.abs(jac@jac.T-jac.T@jac))/scale**2
            eig=np.linalg.eigvals(jac)
            eigerr=max(max(min(abs(e-lam)) for e in eig),max(min(abs(v-eig)) for v in lam))/scale
            check(err<1e-12 and normerr<1e-12 and eigerr<1e-12,'collision direct matrix')
            matrix_results.append({'n':n,'q':q,'model':model,'Fourier_error':err,'normality_error':normerr,'eigenvalue_set_error':eigerr})
        for typ in ['unique','tied','all_tied']:
            v=np.linspace(.1,2.,n)
            if typ=='tied':v[0]=v[-1]
            if typ=='all_tied':v[:]=2
            Y=max(v); f=field(v,p,q,'MB'); dplus=max(f[v==Y]); bound=p[0]*Y-(p[1]-p[2])*Y**2
            check(dplus<=bound+1e-12,'maximum collision inequality')
            max_results.append({'n':n,'q':q,'type':typ,'slack':float(bound-dplus)})
        counts['collision_nq']+=1

# Independent deterministic adversarial search in physical parameter space.
rng=np.random.default_rng(20261003)
search=[]
for n in plan['dimensions']:
    P=10**rng.uniform(-3,3,size=(plan['random_tuples_per_dimension'],5))
    a,k,c,g,h=P.T; M=k+g+h-c; mu=a+c-g; A=k+h; b=a-A; discr=b*b+4*A*mu
    cs=np.cos(2*np.pi*np.arange(n//2+1)/n); w=1-2*cs*cs
    mb=-k[:,None]+c[:,None]*cs+(g+h)[:,None]*w
    mbmax=mb.max(axis=1); stable=(M>0)&(mbmax<-1e-10*(1+P.max(axis=1)))
    unique=(M>0)&(mu>0)
    full=(M>0)&(discr>0)
    contradictions=[]; inspected=0; stable_unique=0; stable_lower=0
    for label,sgn in [('upper',1),('lower',-1)]:
        x=(b+sgn*np.sqrt(np.maximum(discr,0)))/(2*A)
        mask=full&(x>0)
        ix=np.where(mask)[0]; xx=x[ix]; ss=1+xx
        d=-k[ix]*xx-c[ix]*(1+2*xx)/(ss*ss)
        r=d[:,None]+(c[ix]/ss)[:,None]*cs+(g[ix]*xx/(ss*ss)-h[ix]*xx)[:,None]*(2*cs*cs-1)
        rm=r.max(axis=1); inspected+=len(ix)
        for pos,i in enumerate(ix):
            if stable[i]:
                if unique[i]:stable_unique+=1
                if label=='lower':stable_lower+=1
                prohibited=n%4==0 or (unique[i] and n%4!=3)
                if prohibited and rm[pos]>1e-9*(1+abs(d[pos])):
                    contradictions.append({'index':int(i),'branch':label,'tuple':P[i].tolist(),'DM_sa':float(rm[pos])})
        check(not contradictions,'random parity counterexample')
    search.append({'n':n,'tuples':len(P),'positive_branch_cases':inspected,'MB_stable_unique_cases':stable_unique,'MB_stable_lower_cases':stable_lower,'counterexamples':contradictions})

for key,value in counts.items():
    check(value==plan[key],'planned count '+key)
results={'method':'Independent reconstruction; Fraction exact arithmetic, Decimal 80-digit trigonometry, NumPy direct original-field checks. Not interval certificates.','python':platform.python_version(),'numpy':np.__version__,'precision':80,'counts':counts,'stats':stats,'cases':records,'exact_witnesses':exact,'growth_witnesses':growth,'collision_checks':matrix_results,'maximum_checks':max_results,'counterexample_search':search}
def stringify(o):
    if isinstance(o,D):return str(o)
    if isinstance(o,np.generic):return o.item()
    raise TypeError(type(o).__name__)
(HERE/'independent_results.json').write_text(json.dumps(results,indent=2,default=stringify)+'\n')
summary={k:v for k,v in results.items() if k not in ['cases','exact_witnesses','growth_witnesses','collision_checks','maximum_checks','counterexample_search']}
summary.update(total_equilibrium_cases=len(records),exact_rational_witnesses=len(exact),direct_matrix_cases=len(matrix_results),maximum_cases=len(max_results),random_tuples=sum(x['tuples'] for x in search),random_branch_cases=sum(x['positive_branch_cases'] for x in search),random_MB_stable_unique_cases=sum(x['MB_stable_unique_cases'] for x in search),random_MB_stable_lower_cases=sum(x['MB_stable_lower_cases'] for x in search),counterexamples=0,max_Fourier_error=max(x['Fourier_error'] for x in matrix_results),max_eigenvalue_set_error=max(x['eigenvalue_set_error'] for x in matrix_results))
(HERE/'independent_summary.json').write_text(json.dumps(summary,indent=2,default=stringify)+'\n')
print(json.dumps(summary,indent=2,default=stringify))
