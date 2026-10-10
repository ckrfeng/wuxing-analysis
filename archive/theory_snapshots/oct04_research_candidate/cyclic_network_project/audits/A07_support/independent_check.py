#!/usr/bin/env python3
"""Independent A07 corroboration. No P07/developer-checker code is imported.

Exact arithmetic: Q(sqrt(5)) and r + i*sigma*w, sigma^2=(5-sqrt(5))/8.
Signs in Q(sqrt(5)) are decided by rational comparisons, never decimals.
Numerical spectra are compared over all 120 bijections, preserving multiplicity.
This finite suite is corroboration, not the universal proof in A07.
"""
from dataclasses import dataclass
from fractions import Fraction as R
from itertools import product, permutations
from pathlib import Path
import argparse, hashlib, json, math, platform
import numpy as np

@dataclass(frozen=True)
class Q:
    a: R = R(0)
    b: R = R(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', R(self.a))
        object.__setattr__(self, 'b', R(self.b))
    def __add__(self, y):
        y=q(y); return Q(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,y): return self+-q(y)
    def __rsub__(self,y): return q(y)+-self
    def __mul__(self,y):
        y=q(y);return Q(self.a*y.a+5*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,y):
        y=q(y); norm=y.a*y.a-5*y.b*y.b
        if not norm: raise ZeroDivisionError
        return self*Q(y.a/norm,-y.b/norm)
    def __rtruediv__(self,y): return q(y)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        v=Q(1)
        for _ in range(n):v=v*self
        return v
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        delta=a*a-5*b*b
        return ((delta>0)-(delta<0))*(1 if a>0 else -1)
    def __float__(self):return float(self.a)+float(self.b)*math.sqrt(5)
    def data(self):return [str(self.a),str(self.b)]
def q(v):return v if isinstance(v,Q) else Q(v)

SQ5=Q(0,1); PHI=(1+SQ5)/2; SIG2=(5-SQ5)/8
@dataclass(frozen=True)
class E:
    r: Q = Q()
    w: Q = Q()
    def __post_init__(self):
        object.__setattr__(self,'r',q(self.r));object.__setattr__(self,'w',q(self.w))
    def __add__(self,y):
        y=e(y);return E(self.r+y.r,self.w+y.w)
    __radd__=__add__
    def __neg__(self):return E(-self.r,-self.w)
    def __sub__(self,y):return self+-e(y)
    def __rsub__(self,y):return e(y)+-self
    def __mul__(self,y):
        y=e(y);return E(self.r*y.r-SIG2*self.w*y.w,self.r*y.w+self.w*y.r)
    __rmul__=__mul__
    def __pow__(self,n):
        v=E(1)
        for _ in range(n):v=v*self
        return v
    def conj(self):return E(self.r,-self.w)
    def data(self):return {'real':self.r.data(),'imag_over_sigma':self.w.data()}
def e(v):return v if isinstance(v,E) else E(v)

checks=[]
def check(name, condition):
    ok=bool(condition);checks.append({'name':name,'pass':ok})
    if not ok:raise AssertionError(name)
def eq(name,a,b):check(name,a==b)
def positive(name,a):check(name,q(a).sign()>0)

def spectrum(C,G,H,d):
    T=G-H;S=G+H
    a=E(d+C+T)
    b=E(d+C/(2*PHI)-PHI*T/2,S-PHI*C)
    c=E(d-PHI*C/2+T/(2*PHI),-C-PHI*S)
    return [a,b,c,c.conj(),b.conj()]

def exact_suite():
    for name,a,b in [
        ('phi quadratic',PHI**2,PHI+1),('phi inverse',1/PHI,PHI-1),
        ('phi inverse square',PHI**-2,2-PHI),('sum',PHI+1/PHI,SQ5),
        ('sigma radical square',SIG2,(10-2*SQ5)/16),
        ('sin72 radical square',PHI**2*SIG2,(10+2*SQ5)/16),
        ('cos36 Pythagoras',SIG2+(PHI/2)**2,Q(1)),
        ('beta0',(1+1/(2*PHI))/2,PHI**2/4),
        ('beta1',(1/(2*PHI)-PHI/2)/2,Q(R(-1,4))),
        ('alpha0',4/PHI**2,6-2*SQ5)]:eq(name,a,b)
    positive('phi positive',PHI);positive('sigma squared positive',SIG2)
    z=E(1/(2*PHI),PHI)
    eq('primitive root fifth power',z**5,E(1))
    eq('root geometric sum',sum(z**m for m in range(5)),E())
    rows=[(Q(1),Q(),Q(1),Q()),(1/(2*PHI),PHI,-PHI/2,Q(1)),
          (-PHI/2,Q(1),1/(2*PHI),-PHI),
          (-PHI/2,Q(-1),1/(2*PHI),PHI),
          (1/(2*PHI),-PHI,-PHI/2,Q(-1))]
    for m,(c,s,c2,s2) in enumerate(rows):
        eq(f'phase theta {m}',z**m,E(c,s))
        eq(f'phase twice theta {m}',z**((2*m)%5),E(c2,s2))
    # Basis tests prove these linear coefficient identities in C,G,H,d.
    for j,(C,G,H,d) in enumerate([(Q(1),Q(),Q(),Q()),(Q(),Q(1),Q(),Q()),
                                  (Q(),Q(),Q(1),Q()),(Q(),Q(),Q(),Q(1))]):
        L=spectrum(C,G,H,d);T=G-H
        for m in range(5):
            raw=E(d)+E(C)*z**((-m)%5)+E(G)*z**((2*m)%5)-E(H)*z**((-2*m)%5)
            eq(f'raw spectrum basis {j} label {m}',L[m],raw)
        eq(f'gap12 basis {j}',L[1].r-L[2].r,SQ5*(C-T)/2)
        eq(f'gap01 basis {j}',L[0].r-L[1].r,SQ5*PHI*(T+C/PHI**2)/2)
        eq(f'gap02 basis {j}',L[0].r-L[2].r,SQ5*(T+PHI**2*C)/(2*PHI))
    ts=[Q(2),Q(1),Q(),-PHI**-2,Q(-1),-PHI**2,Q(-3)]
    expected=[(-1,1,1),(0,1,1),(1,1,1),(1,0,1),(1,-1,1),(1,-1,0),(1,-1,-1)]
    cases=[]
    for i,t in enumerate(ts):
        for C in [Q(R(1,7)),Q(1),Q(11)]:
            G=C*(1+(t if t.sign()>0 else 0));H=C*(1+(-t if t.sign()<0 else 0))
            cases.append((f'row{i+1}',C,G,H))
            L=spectrum(C,G,H,-5*C/2);r=[v.r for v in L[:3]]
            eq(f'ordering row{i+1} scale{C.data()}',tuple((r[a]-r[b]).sign() for a,b in [(1,2),(0,1),(0,2)]),expected[i])
    for t in [-PHI+Q(R(1,10)),Q(-1),-PHI**-2,Q(),Q(1),PHI-Q(R(1,10))]:
        cases.append(('frequency_locus',Q(1),(PHI+t)/2,(PHI-t)/2))
    for C,G,H in product([Q(R(1,5)),Q(1),Q(3),Q(13)],repeat=3):
        cases.append(('positive_grid',C,G,H))
    exact_cases=[]
    for idx,(name,C,G,H) in enumerate(cases):
        positive(f'case {idx} C',C);positive(f'case {idx} G',G);positive(f'case {idx} H',H)
        a=H+2*G;k=C;c=2*C;g=4*G;h=H;x=Q(1);d=-5*C/2
        eq(f'case {idx} original DM',a*x-k*x*x+c*x/(1+x)-g*x/(1+x)-h*x*x,Q())
        eq(f'case {idx} original diagonal',a-2*k*x-c*x/(1+x)**2-g/(1+x)-h*x,d)
        L=spectrum(C,G,H,d);r=[v.r for v in L[:3]]
        check(f'case {idx} excludes dominant pair2',(r[0]-r[2]).sign()>0 or (r[1]-r[2]).sign()>0)
        positive(f'case {idx} pair2 nonreal',-L[2].w)
        actual=[(i,j) for i in range(5) for j in range(i+1,5) if L[i]==L[j]]
        freq=G+H==PHI*C;tie=G-H==-C/PHI**2
        expected_pairs=[(0,1),(0,4),(1,4)] if freq and tie else [(1,4)] if freq else []
        eq(f'case {idx} exhaustive ten pairs',actual,expected_pairs)
        if tie:
            eq(f'case {idx} stable tie value',r[0],-k*x-C*x/(1+x)-C/PHI**2)
            positive(f'case {idx} stable tie strict',-r[0])
        if idx<21:
            # Direct original-component Jacobian on unnormalized exact Fourier vectors.
            J=[[Q() for j in range(5)] for i in range(5)]
            for i in range(5):
                J[i][i]=a-2*k*x-c*x/(1+x)**2-g/(1+x)-h*x
                J[i][(i-1)%5]=c/(1+x)
                J[i][(i+2)%5]=g*x/(1+x)**2
                J[i][(i-2)%5]=-h*x
            for m in range(5):
                v=[z**((m*j)%5) for j in range(5)]
                check(f'case {idx} exact matrix mode {m}',all(sum(E(J[i][j])*v[j] for j in range(5))==L[m]*v[i] for i in range(5)))
        exact_cases.append({'kind':name,'C':C.data(),'G':G.data(),'H':H.data(),'eigenvalues':[v.data() for v in L],'coincident_pairs':actual})
    eq('intersection G', (PHI-PHI**-2)/2,1/PHI)
    eq('intersection H', (PHI+PHI**-2)/2,Q(1))
    eq('witness original bracket',SQ5-2+(2-4/PHI)/2,Q())
    eq('witness common value',-Q(R(5,2))+1/PHI,-Q(R(3,2))-PHI**-2)
    eq('effective gradient determinant',Q(-1)*1-Q(1)*1,Q(-2))
    # General physical identities: exact coefficients at independent sample states;
    # the universal symbolic derivation is in the audit, not inferred from samples.
    for x in [Q(R(1,100)),Q(R(1,4)),Q(1),Q(3),Q(100)]:
        s=1+x;C=Q(R(7,3));G=Q(R(2,7));H=G+C/PHI**2;k=Q(2)+C/x
        c=C*s;g=G*s*s/x;h=H/x;a=(k+h)*x-(c-g)/s
        positive('general tie a '+str(x.data()),a)
        eq('general tie DM '+str(x.data()),a*x-k*x*x+c*x/s-g*x/s-h*x*x,Q())
        d=a-2*k*x-c*x/s**2-g/s-h*x
        eq('general tie value '+str(x.data()),d+C+G-H,-k*x-C*x/s-C/PHI**2)
        positive('general tie negative '+str(x.data()),-(d+C+G-H))
        det=k+h+(c-g)/s**2
        positive('branch determinant '+str(x.data()),det)
        eq('physical constraint determinant '+str(x.data()),(-x/s**2)*x-x*(x/s**2),-2*x*x/s**2)
    return exact_cases,ts

def numeric_suite(ts):
    phi=(1+math.sqrt(5))/2;sig=math.sin(math.pi/5)
    cases=[]
    settings=[('row'+str(i+1),float(t)) for i,t in enumerate(ts)]
    for name,t in settings:
        for C,x in product([0.13,1.0,7.0],[0.02,1.0,9.0]):
            cases.append((name,C,C*(1+max(t,0)),C*(1+max(-t,0)),x))
    for t in [-phi+0.01,-1,-1/phi**2,0,1,phi-0.01]:
        for C,x in product([0.13,1.,7.],[0.02,1.,9.]):
            cases.append(('frequency',C,C*(phi+t)/2,C*(phi-t)/2,x))
    for t in [1-1e-7,1+1e-7,-1/phi**2-1e-7,-1/phi**2+1e-7,-phi**2-1e-7,-phi**2+1e-7]:
        cases.append(('near_tie',1,1+max(t,0),1+max(-t,0),0.7))
    rng=np.random.default_rng(70032026)
    for _ in range(300):
        C,G,H,x=10**rng.uniform(-3,3,4)
        cases.append(('random_positive',C,G,H,x))
    # Targeted attempts to violate stable-tie and distinctness claims.
    for _ in range(60):
        C,G,x=10**rng.uniform(-3,3,3);H=G+C/phi**2
        cases.append(('random_dominant_tie',C,G,H,x))
    perms=np.array(list(permutations(range(5))));records=[]
    maxima={key:0. for key in ['equilibrium','matrix_derivative','eigenvalue','fourier','symbol']}
    failures=[];tolerance=2e-10
    def F(v,a,k,c,g,h):
        return a*v-k*v*v+c*np.roll(v,1)/(1+v)-g*v/(1+np.roll(v,-2))-h*v*np.roll(v,2)
    for index,(kind,C,G,H,x) in enumerate(cases):
        s=1+x;c=C*s;g=G*s*s/x;h=H/x
        k=1+C/x # ensures a= x+H+G*s/x >0; no parameter search needed.
        a=(k+h)*x-(c-g)/s
        if min(a,k,c,g,h,x)<=0:raise AssertionError('positive realization')
        v=np.full(5,x);d=a-2*k*x-c*x/s**2-g/s-h*x
        J=np.zeros((5,5))
        for i in range(5):
            J[i,i]=d;J[i,(i-1)%5]=c/s;J[i,(i+2)%5]=g*x/s**2;J[i,(i-2)%5]=-h*x
        eps=1e-25
        Jcs=np.column_stack([np.imag(F(v.astype(complex)+1j*eps*np.eye(5)[j],a,k,c,g,h))/eps for j in range(5)])
        T=G-H;S=G+H
        l0=d+C+T;l1=d+C/(2*phi)-phi*T/2+1j*sig*(S-phi*C)
        l2=d-phi*C/2+T/(2*phi)-1j*sig*(C+phi*S)
        labels=np.array([l0,l1,l2,np.conj(l2),np.conj(l1)])
        ev=np.linalg.eigvals(J)
        matched=float(np.min(np.max(np.abs(ev[perms]-labels),axis=1)))
        theta=2*np.pi*np.arange(5)/5;V=np.exp(1j*np.outer(np.arange(5),theta))/math.sqrt(5)
        sym=d+C*np.exp(-1j*theta)+G*np.exp(2j*theta)-H*np.exp(-2j*theta)
        scale=max(1.,float(np.linalg.norm(J,ord=np.inf)),float(np.max(np.abs(labels))))
        residual=float(np.max(np.abs(F(v,a,k,c,g,h))))/max(1.,abs(a*x)+abs(k*x*x)+abs(c*x/s)+abs(g*x/s)+abs(h*x*x))
        errors={'equilibrium':residual,'matrix_derivative':float(np.max(np.abs(J-Jcs)))/scale,
                'eigenvalue':matched/scale,'fourier':float(np.max(np.abs(J@V-V*labels)))/scale,
                'symbol':float(np.max(np.abs(sym-labels)))/scale}
        for key,val in errors.items():maxima[key]=max(maxima[key],val)
        passed=all(val<tolerance for val in errors.values())
        if kind=='random_dominant_tie':
            expected=-k*x-C*x/s-C/phi**2
            passed=passed and expected<0 and abs(l0-expected)/scale<tolerance
        if not passed:failures.append(index)
        records.append({'index':index,'kind':kind,'C':C,'G':G,'H':H,'x':x,
                        'physical':[a,k,c,g,h],'labelled_spectrum':[[float(z.real),float(z.imag)] for z in labels],
                        'matrix_eigenvalues':[[float(z.real),float(z.imag)] for z in ev],
                        'errors':errors,'pass':bool(passed)})
    if failures:raise AssertionError(failures)
    return records,maxima,tolerance

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',default=str(Path(__file__).parent));args=p.parse_args()
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    ex,ts=exact_suite();num,maxima,tol=numeric_suite(ts)
    summary={'status':'PASS','scope':'finite corroboration only; analytic proofs are in A07',
             'python':platform.python_version(),'numpy':np.__version__,
             'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'exact_assertions':len(checks),'exact_coefficient_cases':len(ex),
             'exact_direct_matrix_cases':21,'numerical_cases':len(num),'ordering_rows':7,
             'random_seed':70032026,'tolerance':tol,'max_scaled_errors':maxima,
             'counterexamples_found':0}
    for name,data in [('independent_exact_results.json',{'checks':checks,'cases':ex}),
                      ('independent_numerical_results.json',num),('independent_summary.json',summary)]:
        (out/name).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
