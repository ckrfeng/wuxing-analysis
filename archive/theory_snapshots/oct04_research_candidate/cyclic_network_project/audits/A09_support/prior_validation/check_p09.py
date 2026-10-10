"""P09 corroboration only. Standard-library exact jets + NumPy direct matrices.
Run with Python 3 and numpy from any working directory. No input is modified.
"""
from pathlib import Path
from fractions import Fraction as Q
import json, math, sys, platform, hashlib
import numpy as np
OUT=Path(__file__).resolve().parent
# Total-degree-three bivariate Taylor algebra, with exact rational coefficients.
class Jet:
    def __init__(self, x=0):
        self.d=x if isinstance(x,dict) else ({(0,0):Q(x)} if x else {})
    def __add__(self,other):
        o=asjet(other); d=self.d.copy()
        for e,v in o.d.items(): d[e]=d.get(e,Q(0))+v
        return Jet({e:v for e,v in d.items() if v})
    __radd__=__add__
    def __neg__(self): return Jet({e:-v for e,v in self.d.items()})
    def __sub__(self,o): return self+-asjet(o)
    def __rsub__(self,o): return asjet(o)+-self
    def __mul__(self,o):
        d={}
        for (i,j),u in self.d.items():
            for (k,l),v in asjet(o).d.items():
                if i+j+k+l<=3: d[i+k,j+l]=d.get((i+k,j+l),Q(0))+u*v
        return Jet({e:v for e,v in d.items() if v})
    __rmul__=__mul__
    def inv(self):
        a=self.d.get((0,0),Q(0)); assert a
        z=1-self*(1/a)
        return (1+z+z*z+z*z*z)*(1/a)
    def __truediv__(self,o): return self*asjet(o).inv()
    def __rtruediv__(self,o): return asjet(o)*self.inv()
    def at(self,i,j=0): return self.d.get((i,j),Q(0))
def asjet(x): return x if isinstance(x,Jet) else Jet(x)

def field(x,a,k,c,g,h,q):
    n=len(x)
    return [a*x[i]-k*x[i]*x[i]+c*x[(i-1)%n]/(1+x[i])
            -g*x[i]/(1+x[(i+q)%n])-h*x[i]*x[(i-q)%n] for i in range(n)]

def jacobian(x,a,k,c,g,h,q):
    n=len(x); J=np.zeros((n,n))
    for i in range(n):
        J[i,i]+=a-2*k*x[i]-c*x[(i-1)%n]/(1+x[i])**2-g/(1+x[(i+q)%n])-h*x[(i-q)%n]
        J[i,(i-1)%n]+=c/(1+x[i])
        J[i,(i+q)%n]+=g*x[i]/(1+x[(i+q)%n])**2
        J[i,(i-q)%n]-=h*x[i]
    return J

def labelled_spectrum(n,q,r,a,k,c,g,h):
    t=2*np.pi*np.arange(n)/n
    d=a-2*k*r-c*r/(1+r)**2-g/(1+r)-h*r
    C=c/(1+r);G=g*r/(1+r)**2;H=h*r
    return d+C*np.exp(-1j*t)+G*np.exp(1j*q*t)-H*np.exp(-1j*q*t)

def match_spectra(got,expected,tol):
    # Multiplicity-preserving bipartite perfect matching within tolerance.
    owner={}
    def visit(i,seen):
        for j in np.argsort(np.abs(expected-got[i])):
            j=int(j)
            if j in seen or abs(expected[j]-got[i])>tol: continue
            seen.add(j)
            if j not in owner or visit(owner[j],seen): owner[j]=i; return True
        return False
    assert all(visit(i,set()) for i in range(len(got)))
    return max(float(abs(got[i]-expected[j])) for j,i in owner.items())

exact=[]
def check(name,condition,detail=None):
    assert condition,name
    exact.append({'name':name,'pass':True,**({'detail':detail} if detail is not None else {})})
t=Jet({(1,0):Q(1)});m=Jet({(0,1):Q(1)})
networks=[(n,q) for n in [5,6,7,8,9,10,12] for q in range(1,n)]
params=[(Q(a),Q(1),Q(c),Q(1)) for a in [1,2,3] for c in [Q(1),Q(7,3)]]
for a,k,c,h in params:
    A=k+h;b=a-A;gc=a+c
    # Exact original field, not pre-simplified scalar f.
    for n,q in networks:
        vals=field([t]*n,a,k,c,gc-m,h,q)
        expected={(1,1):Q(1),(2,0):b,(3,0):-a,(2,1):Q(-1)}
        expected={e:v for e,v in expected.items() if v}
        check(f'original_directional_jet/{a}/{c}/{n}/{q}',all(v.d==expected for v in vals))
        gvals=field([t]*n,a,k,c,gc+m,h,q)
        check(f'physical_g_mixed_derivative/{a}/{c}/{n}/{q}',all(v.at(1,1)==-1 for v in gvals))
        # Every critical Jacobian column independently from the original rational field.
        cols=[]
        for j in range(n):
            x=[Jet(0) for _ in range(n)];x[j]=t
            cols.append([v.at(1) for v in field(x,a,k,c,gc,h,q)])
        check(f'critical_jacobian/{a}/{c}/{n}/{q}',all(cols[j][i]==c*((1 if j==(i-1)%n else 0)-(1 if i==j else 0)) for i in range(n) for j in range(n)))
        # (lambda+c)^n-c^n has derivative n*c^(n-1)>0 at lambda=0.
        check(f'simple_characteristic_root/{a}/{c}/{n}/{q}',n*c**(n-1)>0)
    check(f'codimension_minor/{a}/{c}',Q(-1)*Q(1)-Q(0)*Q(0)==-1)
    check(f'fold_overlap/{a}/{c}',((a-A)**2/(4*A)==0)==(b==0))
    if b:
        s1=-1/b;s2=A/b**3
        check(f'branch_series/{a}/{c}',-b*s1-1==0 and A*s1*s1-b*s2==0)
        # Exact identity of the two center-vector-field expressions at rational points.
        for r in [Q(1,100),Q(-1,100)]:
            mu=A*r*r-b*r
            lam=r*(b-2*A*r)/(1+r)
            check(f'exact_branch_uniform_sign/{a}/{c}/{r}',lam==-mu*(b-2*A*r)/((1+r)*(b-A*r)) and (lam>0)==(mu<0))
            check(f'physical_side/{a}/{c}/{r}',(r>0)==(mu*b<0))
            for mu0 in [Q(1,1000),Q(-1,1000)]:
                u=A*r*r-b*r;alpha=(2*A*r-b)/((A*r-b)*(1+r))
                f=r*(mu0+b*r-A*r*r)/(1+r)
                check(f'orbital_identity/{a}/{c}/{r}/{mu0}',(2*A*r-b)*f==alpha*u*(mu0-u) and alpha>0)
    else:
        for r in [Q(1,100),Q(-1,100)]:
            mu=A*r*r
            check(f'degenerate_root/{a}/{c}/{r}',mu-A*r*r==0)
            check(f'degenerate_eigenvalue/{a}/{c}/{r}',-2*A*r*r/(1+r)<0)
            check(f'critical_scalar_Lyapunov/{a}/{c}/{r}',-A*r**4/(1+r)<0)

def root_near(mu,A,b):
    return -2*mu/(b+math.copysign(math.sqrt(b*b+4*A*mu),b))
records=[];slopes=[]
for aq,kq,cq,hq in params:
    a,k,c,h=map(float,(aq,kq,cq,hq));A=k+h;b=a-A;gc=a+c
    if b:
        for eps in [1e-5,1e-6,1e-7]:
            slope=(root_near(eps,A,b)-root_near(-eps,A,b))/(2*eps)
            g_slope=(root_near(gc-(gc+eps),A,b)-root_near(gc-(gc-eps),A,b))/(2*eps)
            err=max(abs(slope+1/b),abs(g_slope-1/b));assert err<1e-7
            slopes.append({'a':a,'c':c,'eps':eps,'mu_slope':slope,'g_slope':g_slope,'error':err})
    for n,q in networks:
        delta=c*(1-math.cos(2*math.pi/n))
        critical=c*(np.exp(-2j*np.pi*np.arange(n)/n)-1)
        assert np.max(critical[1:].real)<=-delta+1e-14
        for mu in [-1e-6,-1e-8,0.0,1e-8,1e-6]:
            roots=[('origin',0.0)]
            if b and mu: roots.append(('generic',root_near(mu,A,b)))
            elif not b and mu>0:
                roots.extend([('degenerate_positive',math.sqrt(mu/A)),('degenerate_negative',-math.sqrt(mu/A))])
            for label,r in roots:
                g=gc-mu;assert g>0 and r>-1
                x=np.full(n,r);res=float(np.max(np.abs(field(x,a,k,c,g,h,q))))
                assert res<2e-12
                J=jacobian(x,a,k,c,g,h,q)
                Jcs=np.column_stack([np.imag(field(x.astype(complex)+1e-28j*np.eye(n)[j],a,k,c,g,h,q))/1e-28 for j in range(n)])
                scale=max(1.,float(np.linalg.norm(J,2)))
                cs_error=float(np.max(abs(J-Jcs)))/scale;assert cs_error<1e-13
                spec=labelled_spectrum(n,q,r,a,k,c,g,h)
                mat_error=match_spectra(np.linalg.eigvals(J),spec,1e-10*scale)/scale
                v=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
                fourier_error=float(np.max(abs(J@v-v*spec)))/scale;assert fourier_error<1e-13
                transverse=float(np.max(spec[1:].real));assert transverse<-delta/2
                uni=mu if label=='origin' else r*(b-2*A*r)/(1+r)
                assert abs(spec[0]-uni)<1e-12
                if mu:
                    expected=mu if label=='origin' else (-mu if b else -1.)
                    assert uni*expected>0
                if label=='generic': assert (r>0)==(mu*b<0)
                if label.startswith('degenerate'): assert uni<0
                records.append({'n':n,'q':q,'gcd':math.gcd(n,q),'a':a,'k':k,'c':c,'g':g,'h':h,'mu':mu,'branch':label,'r':r,'residual':res,'jacobian_complex_step_error':cs_error,'spectrum_error':mat_error,'fourier_error':fourier_error,'uniform_eigenvalue':uni,'max_transverse_real':transverse,'delta':delta,'pass':True})
summary={'status':'PASS','role':'corroboration only; not independent A09 audit','python':platform.python_version(),'numpy':np.__version__,'exact_checks':len(exact),'network_pairs':len(networks),'noncoprime_network_pairs':sum(math.gcd(n,q)>1 for n,q in networks),'parameter_tuples':len(params),'matrix_cases':len(records),'slope_checks':len(slopes),'max_original_residual':max(r['residual'] for r in records),'max_scaled_spectrum_error':max(r['spectrum_error'] for r in records),'max_scaled_complex_step_error':max(r['jacobian_complex_step_error'] for r in records),'max_scaled_fourier_error':max(r['fourier_error'] for r in records),'max_slope_error':max(r['error'] for r in slopes),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
for filename,obj in [('exact_results.json',exact),('numerical_results.json',records),('slope_results.json',slopes),('summary.json',summary)]:
    (OUT/filename).write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(summary,indent=2))
