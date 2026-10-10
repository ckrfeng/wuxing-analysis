#!/usr/bin/env python3
"""P07 corroboration: exact Q(sqrt(5),sigma,i) arithmetic and direct matrices.
Run: python3 check_p07.py --output DIRECTORY
Uses only standard library and NumPy. Never edits the project.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from pathlib import Path
import argparse, itertools, json, math, platform, hashlib
import numpy as np

@dataclass(frozen=True)
class K:
    a: F=F(0)
    b: F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def cast(x): return x if isinstance(x,K) else K(x)
    def __add__(self,x):
        x=K.cast(x);return K(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,x):return self+-K.cast(x)
    def __rsub__(self,x):return K.cast(x)+-self
    def __mul__(self,x):
        x=K.cast(x);return K(self.a*x.a+5*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def inv(self):
        den=self.a*self.a-5*self.b*self.b
        if not den: raise ZeroDivisionError
        return K(self.a/den,-self.b/den)
    def __truediv__(self,x):return self*K.cast(x).inv()
    def __rtruediv__(self,x):return K.cast(x)*self.inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        out=K(1)
        for _ in range(n):out=out*self
        return out
    def sign(self):
        a,b=self.a,self.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if a*b>0:return (a>0)-(a<0)
        d=a*a-5*b*b
        return ((a>0)-(a<0))*((d>0)-(d<0))
    def __float__(self):return float(self.a)+float(self.b)*math.sqrt(5)
    def data(self):return [str(self.a),str(self.b)]

phi=K(F(1,2),F(1,2));root5=K(0,1)
u1=1/(2*phi);u2=-phi/2;sig2=(5-root5)/8

@dataclass(frozen=True)
class E:
    # basis [1,sigma,i,i*sigma], coefficients in Q(sqrt5)
    v:tuple=(K(),K(),K(),K())
    @staticmethod
    def cast(x):return x if isinstance(x,E) else E((K.cast(x),K(),K(),K()))
    def __add__(self,x):
        x=E.cast(x);return E(tuple(a+b for a,b in zip(self.v,x.v)))
    __radd__=__add__
    def __neg__(self):return E(tuple(-a for a in self.v))
    def __sub__(self,x):return self+-E.cast(x)
    def __rsub__(self,x):return E.cast(x)+-self
    def __mul__(self,x):
        x=E.cast(x);o=[K() for _ in range(4)]
        for j,a in enumerate(self.v):
            for k,b in enumerate(x.v):
                factor=K(1)
                if j&k&1:factor=factor*sig2
                if j&k&2:factor=-factor
                o[j^k]=o[j^k]+a*b*factor
        return E(tuple(o))
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        out=E.cast(1)
        for _ in range(n):out=out*self
        return out
    def conj(self):return E((self.v[0],self.v[1],-self.v[2],-self.v[3]))
    def data(self):return [a.data() for a in self.v]

exact=[]
def eq(name,a,b=0):
    aa,bb=(E.cast(a),E.cast(b)) if isinstance(a,E) or isinstance(b,E) else (K.cast(a),K.cast(b))
    assert aa==bb,(name,aa,bb)
    exact.append({'name':name,'passed':True,'difference':(aa-bb).data()})
def sign(name,x,s):
    x=K.cast(x);assert x.sign()==s,(name,x,s)
    exact.append({'name':name,'passed':True,'value':x.data(),'sign':s})

eq('phi quadratic',phi**2,phi+1)
eq('phi inverse',1/phi,phi-1);eq('phi inverse square',phi**-2,(3-root5)/2)
eq('phi plus inverse',phi+1/phi,root5)
eq('u1 radical',u1,(root5-1)/4);eq('u2 radical',u2,-(root5+1)/4)
eq('cosine difference',u1-u2,root5/2)
eq('fifth root cosine quadratic',4*u1*u1+2*u1-1)
eq('double cosine 1',2*u1*u1-1,u2);eq('double cosine 2',2*u2*u2-1,u1)
eq('sigma squared radical',16*sig2,10-2*root5)
eq('sin72 squared radical',16*phi**2*sig2,10+2*root5)
eq('cos36 sigma identity',phi**2/4+sig2,1)
eq('sin72 normalization squared',phi**2*sig2,1-u1*u1)
sign('sigma positive square',sig2,1)
I=E((K(),K(),K(1),K()));sigma=E((K(),K(1),K(),K()))
z=E.cast(u1)+I*sigma*phi
eq('fifth root power',z**5,1);eq('geometric sum',sum(z**j for j in range(5)),0)
eq('unit modulus',z*z.conj(),1)
cosines=[K(1),u1,u2,u2,u1];sinfactors=[K(),phi,K(1),K(-1),-phi]
for m in range(5):
    eq(f'phase row {m}',z**m,E.cast(cosines[m])+I*sigma*sinfactors[m])
    eq(f'double phase row {m}',z**((2*m)%5),E.cast(cosines[(2*m)%5])+I*sigma*sinfactors[(2*m)%5])
# Candidate coefficients in order d,C,G,H, independently compared with shift powers.
candidates=[
 [1,1,1,-1],
 [1,E.cast(1/(2*phi))-I*sigma*phi,E.cast(-phi/2)+I*sigma,E.cast(phi/2)+I*sigma],
 [1,E.cast(-phi/2)-I*sigma,E.cast(1/(2*phi))-I*sigma*phi,E.cast(-1/(2*phi))-I*sigma*phi],
]
candidates += [[E.cast(v).conj() for v in candidates[2]], [E.cast(v).conj() for v in candidates[1]]]
for m in range(5):
    raw=[E.cast(1),z**((-m)%5),z**((2*m)%5),-(z**((-2*m)%5))]
    for name,a,b in zip(['d','C','G','H'],raw,candidates[m]):eq(f'spectrum m={m} coefficient {name}',a,b)
    for j in range(4):eq(f'conjugacy m={m} coefficient {j}',E.cast(candidates[m][j]).conj(),candidates[(-m)%5][j])
# Coefficients in d,C,T of each real part and pairwise factorization.
r=[[K(1),K(1),K(1)],[K(1),u1,u2],[K(1),u2,u1]]
gaps=[(1,2,[0,root5/2,-root5/2]),(0,1,[0,root5/(2*phi),root5*phi/2]),(0,2,[0,root5*phi/2,root5/(2*phi)])]
for a,b,target in gaps:
    for j in range(3):eq(f'gap {a}-{b} coefficient {j}',r[a][j]-r[b][j],target[j])
def realclasses(t):return [K(1)+t,u1+t*u2,u2+t*u1]
regions=[('above_1',K(2),[-1,1,1]),('at_1',K(1),[0,1,1]),('middle_uniform',K(0),[1,1,1]),('dominant_tie',-phi**-2,[1,0,1]),('middle_pair1',K(-1),[1,-1,1]),('lower_tie',-phi**2,[1,-1,0]),('below_lower_tie',K(-4),[1,-1,-1])]
for name,t,expected in regions:
    rr=realclasses(t)
    for (a,b),s in zip([(1,2),(0,1),(0,2)],expected):sign(f'ordering {name} {a}-{b}',rr[a]-rr[b],s)
eq('beta0',(1+u1)/2,phi**2/4);eq('beta1',(u1+u2)/2,-F(1,4))
eq('alpha0',4/phi**2,6-2*root5)
eq('switch phi negative square',-phi**-2,(root5-3)/2)
eq('other threshold',-phi**2,-(3+root5)/2)
# Canonical switch holds coefficientwise in g,c for any rational x.
for x in [F(1,4),F(1),F(3)]:
    s=1+x
    eq(f'canonical switch g coefficient x={x}',K(x)/s**2-K(x)/s**2)
    eq(f'canonical switch c coefficient x={x}',K(x)/(phi**2*s*x),1/(phi**2*s))
eq('intersection G',(phi-phi**-2)/2,phi**-1);eq('intersection H',(phi+phi**-2)/2,1)
eq('triple value shift',1-phi**-2,phi**-1)
eq('stable tie identity',-1+1/phi,-phi**-2)
eq('intersection witness equilibrium',root5-2+(2-4/phi)/2)
eq('subdominant pair tie gap',realclasses(K(1))[0]-realclasses(K(1))[1],F(5,2))
eq('subdominant uniform tie gap',realclasses(-phi**2)[1]-realclasses(-phi**2)[0],5*phi/2)
eq('coefficient codimension determinant',-2,-2)
eq('impossible cross equality same sign S/C',(phi-1)/(phi+1),phi**-3)
eq('impossible cross equality opposite sign S/C',-(phi+1)/(phi-1),-phi**3)
sign('same-sign equality below positive T=C range',1-phi**-3,1)
sign('opposite-sign equality is negative',-phi**3,-1)
# Direct canonical residual and triple negativity, entirely exact at witness.
C=K(1);G=1/phi;H=K(1);d=K(-F(5,2))
for j in [0,1,4]:
    v=E.cast(candidates[j][0])*d+E.cast(candidates[j][1])*C+E.cast(candidates[j][2])*G+E.cast(candidates[j][3])*H
    eq(f'triple witness label {j}',v,d+1/phi)
sign('triple witness negative',d+1/phi,-1)

# Numerical corroboration; signed labels checked by DFT residual, unordered
# eigenvalues compared with every bijection (5!=120), retaining multiplicities.
tol=2e-10
ph=float(phi);sg=math.sqrt(float(sig2));perms=list(itertools.permutations(range(5)))
q=np.exp(2j*np.pi*np.outer(np.arange(5),np.arange(5))/5)/math.sqrt(5)
def field(y,p):
    a,k,c,g,h=p
    return a*y-k*y*y+c*np.roll(y,1)/(1+y)-g*y/(1+np.roll(y,-2))-h*y*np.roll(y,2)
def jacobian(y,p):
    a,k,c,g,h=p;J=np.zeros((5,5))
    for i in range(5):
        J[i,i]+=a-2*k*y[i]-c*y[(i-1)%5]/(1+y[i])**2-g/(1+y[(i+2)%5])-h*y[(i-2)%5]
        J[i,(i-1)%5]+=c/(1+y[i])
        J[i,(i+2)%5]+=g*y[i]/(1+y[(i+2)%5])**2
        J[i,(i-2)%5]+=-h*y[i]
    return J
cases=[]
settings=[(name,t,None) for name,t,_ in regions]
settings += [('below_switch',-phi**-2-K(F(1,100)),None),('above_switch',-phi**-2+K(F(1,100)),None)]
for tname,t in [('pair1',K(-F(1,2))),('switch',-phi**-2),('subdominant_pair_tie',K(1))]:
    for delta in [-F(1,100),F(0),F(1,100)]:settings.append((f'frequency_{tname}_{delta}',t,phi+K(delta)))
for name,t,Srat in settings:
    if Srat is None:
        gt=K(1)+(t if t.sign()>0 else K())
        ht=K(1)+(-t if t.sign()<0 else K())
    else:
        gt=(Srat+t)/2;ht=(Srat-t)/2
    sign(f'case positivity {name} G',gt,1);sign(f'case positivity {name} H',ht,1)
    for xrat in [F(1,4),F(1),F(3)]:
        for Crat in [F(1),F(7,3)]:
            x=float(xrat);s=1+x;C=float(Crat);G=C*float(gt);H=C*float(ht)
            k=(max(C-H-G*s/x,0)+C/4)/x
            c=C*s;g=G*s*s/x;h=H/x;a=k*x+H-C+G*s/x
            p=(a,k,c,g,h);assert min(p)>0
            y=np.full(5,x);J=jacobian(y,p)
            ds=-k*x-C-C*x/s;T=G-H;S=G+H
            ev=np.array([ds+C+T,ds+C/(2*ph)-ph*T/2+1j*sg*(S-ph*C),ds-ph*C/2+T/(2*ph)-1j*sg*(C+ph*S),0,0],complex)
            ev[3]=ev[2].conjugate();ev[4]=ev[1].conjugate()
            calc=np.linalg.eigvals(J)
            scale=max(1,np.linalg.norm(J,2),max(abs(ev)))
            error,bijection=min((max(abs(calc[list(perm)]-ev))/scale,perm) for perm in perms)
            fourier_error=float(np.max(abs(J@q-q*ev))/scale)
            direct=np.empty((5,5))
            for col in range(5):
                yy=y.astype(complex);yy[col]+=1e-25j;direct[:,col]=field(yy,p).imag/1e-25
            derivative_error=float(np.max(abs(J-direct))/scale)
            residual=float(np.max(abs(field(y,p)))/max(1,sum(abs(v) for v in p)*max(1,x*x)))
            theta=2*np.pi*np.arange(5)/5
            symbol=ds+C*np.exp(-1j*theta)+G*np.exp(2j*theta)-H*np.exp(-2j*theta)
            symbol_error=float(np.max(abs(symbol-ev))/scale)
            tt=float(t);expected_reps=[0] if tt>-1/ph**2+1e-12 else [1] if tt<-1/ph**2-1e-12 else [0,1]
            rr=ev[:3].real;maxr=max(rr);actual_reps=[j for j in range(3) if abs(rr[j]-maxr)<tol*scale]
            assert actual_reps==expected_reps,(name,actual_reps,expected_reps)
            if Srat is not None and Srat==phi:
                assert abs(ev[1].imag)<tol*scale
            assert ev[2].imag<0
            assert max(error,fourier_error,derivative_error,residual,symbol_error)<tol
            data={'name':name,'x':x,'parameters':p,'C_G_H':[C,G,H],'t_exact':t.data(),'S_over_C_exact':(gt+ht).data(),'t_numeric':T/C,'real_classes':list(rr),'selected_representatives':actual_reps,'closed_eigenvalues':[[v.real,v.imag] for v in ev],'matrix_eigenvalues':[[v.real,v.imag] for v in calc],'best_bijection':list(bijection),'scaled_eigenvalue_error':float(error),'scaled_fourier_error':fourier_error,'scaled_derivative_error':derivative_error,'scaled_equilibrium_residual':residual,'scaled_symbol_error':symbol_error}
            cases.append(data)
summary={'status':'PASS','python_version':platform.python_version(),'numpy_version':np.__version__,'exact_checks':len(exact),'numerical_cases':len(cases),'distinct_case_settings':len(settings),'ordering_rows':7,'scaled_tolerance':tol,'scope':'corroboration only; not proof, audit, or numerical continuation','checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
for key in ['scaled_eigenvalue_error','scaled_fourier_error','scaled_derivative_error','scaled_equilibrium_residual','scaled_symbol_error']:summary['max_'+key]=max(c[key] for c in cases)
args=argparse.ArgumentParser();args.add_argument('--output',type=Path,required=True);dest=args.parse_args().output;dest.mkdir(parents=True,exist_ok=True)
(dest/'exact_results.json').write_text(json.dumps(exact,indent=2)+'\n')
(dest/'numerical_results.json').write_text(json.dumps(cases,indent=2)+'\n')
(dest/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
