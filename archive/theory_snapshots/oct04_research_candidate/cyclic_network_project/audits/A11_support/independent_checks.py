"""Independent A11 corroboration; no developer checker imported or executed.
Exact arithmetic in Q(phi,t), phi^2=phi+1, t=i*sigma, t^2=(phi-3)/4.
Run with Python + NumPy. Results are corroboration, not universal proof.
"""
from fractions import Fraction as Q
from pathlib import Path
import math,json,platform
import numpy as np
class F:
 def __init__(self,a=0,b=0):
  if isinstance(a,F):self.a,self.b=a.a,a.b
  else:self.a,self.b=Q(a),Q(b)
 def __add__(self,o):o=F(o);return F(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return F(-self.a,-self.b)
 def __sub__(self,o):return self+-F(o)
 def __rsub__(self,o):return F(o)+-self
 def __mul__(self,o):o=F(o);return F(self.a*o.a+self.b*o.b,self.a*o.b+self.b*o.a+self.b*o.b)
 __rmul__=__mul__
 def inv(self):d=self.a*self.a+self.a*self.b-self.b*self.b;return F((self.a+self.b)/d,-self.b/d)
 def __truediv__(self,o):return self*F(o).inv()
 def __rtruediv__(self,o):return F(o)*self.inv()
 def __eq__(self,o):o=F(o);return (self.a,self.b)==(o.a,o.b)
 def __pow__(self,n):
  r=F(1)
  for _ in range(n):r=r*self
  return r
 def approx(self):return float(self.a)+float(self.b)*(1+math.sqrt(5))/2
 def __repr__(self):return f'({self.a})+({self.b})phi'
phi=F(0,1); sig2=(3-phi)/4; t2=-sig2
class K:
 def __init__(self,a=0,b=0):
  if isinstance(a,K):self.a,self.b=a.a,a.b
  else:self.a,self.b=F(a),F(b)
 def __add__(self,o):o=K(o);return K(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return K(-self.a,-self.b)
 def __sub__(self,o):return self+-K(o)
 def __rsub__(self,o):return K(o)+-self
 def __mul__(self,o):o=K(o);return K(self.a*o.a+self.b*o.b*t2,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):d=self.a*self.a-self.b*self.b*t2;return K(self.a/d,-self.b/d)
 def __truediv__(self,o):return self*K(o).inv()
 def __eq__(self,o):o=K(o);return self.a==o.a and self.b==o.b
 def conj(self):return K(self.a,-self.b)
 def __pow__(self,n):
  r=K(1)
  for _ in range(n):r=r*self
  return r
 def approx(self):return complex(self.a.approx(),self.b.approx()*math.sqrt(sig2.approx()))
count=0
checks=[]
def eq(a,b,label):
 global count
 assert a==b,(label,a,b);count+=1

def raw_jac(n,x,a,k,c,g,h):
 # Direct component derivatives of canonical F, at constant state x.
 J=[[K(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  J[i][i]+=K(a-2*k*x-c*x/(1+x)**2-g/(1+x)-h*x)
  J[i][(i-1)%n]+=K(c/(1+x))
  J[i][(i+2)%n]+=K(g*x/(1+x)**2)
  J[i][(i-2)%n]-=K(h*x)
 return J

def mv(A,v):return [sum((a*b for a,b in zip(row,v)),K()) for row in A]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),K()) for j in range(len(B))] for i in range(len(A))]
def mateq(A,B,label):
 for i in range(len(A)):
  for j in range(len(A[0])):eq(A[i][j],B[i][j],label)

x=F(1);a=(3*phi+22)/2;k=(3*phi-4)/2;c=F(2);g=F(16);h=F(6)
eq(a*x-k*x*x+c*x/(1+x)-g*x/(1+x)-h*x*x,0,'original component residual')
eq(a-k,13,'a-k')
eq(k, (3*(2*phi-1)-5)/4,'radical k')
J=raw_jac(5,x,a,k,c,g,h)
z=K((phi-1)/2,phi);eq(z**5,1,'fifth root');eq(sum((z**m for m in range(5)),K()),0,'root sum')
v=[[z**(i*m) for i in range(5)] for m in range(5)]
wH=K(0,10-phi); eta=(3*phi+1)/2
lam=[K(-eta),wH,K(-3*(2*phi-1)/2,-1-10*phi),K(-3*(2*phi-1)/2,1+10*phi),-wH]
for m in range(5):
 for i,val in enumerate(mv(J,v[m])):eq(val,lam[m]*v[m][i],'exact direct matrix eigenvector')
 for l in range(5):eq(sum((v[l][i].conj()*v[m][i] for i in range(5)),K()),5 if l==m else 0,'DFT Gram')
JT=[list(row) for row in zip(*J)]
for i,val in enumerate(mv(JT,v[1])):eq(val,-wH*v[1][i],'adjoint opposite sign')
A=[e.a for e in v[1]];bs=[e.b for e in v[1]]
eq(sum((q*q for q in A),F()),Q(5,2),'cos norm before sqrt(2/5)')
eq(sum((q*q*sig2 for q in bs),F()),Q(5,2),'sin norm before sqrt(2/5)')
eq(sum((A[i]*bs[i] for i in range(5)),F()),0,'real orthogonality')
for i in range(5):
 eq(mv(J,[K(q) for q in A])[i],K(-(10-phi)*sig2*bs[i]),'J cos = -omega sin')
 eq(mv(J,[K(q) for q in bs])[i],K((10-phi)*A[i]),'J sin = omega cos')
I=[[K(int(i==j)) for j in range(5)] for i in range(5)]
for shift in [K(0),2*wH]:
 den=[e if shift==0 else shift-e for e in lam]
 assert all(e!=0 for e in den)
 inverse=[[sum((v[m][i]*v[m][j].conj()/den[m]/5 for m in range(5)),K()) for j in range(5)] for i in range(5)]
 base=J if shift==0 else [[shift*I[i][j]-J[i][j] for j in range(5)] for i in range(5)]
 mateq(mm(base,inverse),I,'exact spectral inverse')
eq(2*wH-lam[2],K(3*(2*phi-1)/2,21+8*phi),'mode 2 denominator')
AA=k+h;b=a-AA;mu=a+c-g;lower=-mu/AA
eq(b,7,'branch b');eq(AA-b,mu,'root 1');eq(AA*lower*lower-b*lower-mu,0,'lower residual')
eq(lower,3*(2-phi)/(3*phi+8),'lower exact form');eq(b*b+4*AA*mu,AA*AA*(1-lower)*(1-lower),'positive discriminant identity')
eq(-AA-(c-g)/4,-eta,'B_X local IFT')
# Exact physical strict zero-frequency point, n=5, j=1.
x0=F(Q(1,10));C=F(1);D=F(1);u=(phi-1)/2;G=(phi-1)/2
k0=(D*(1-2*u*u)-C*(1-u+x0/(1+x0)))/x0
c0=C*(1+x0);g0=G*(1+x0)**2/x0;h0=(G+D)/x0;a0=(k0+h0)*x0-(c0-g0)/(1+x0)
J0=raw_jac(5,x0,a0,k0,c0,g0,h0)
eq(2*(D+2*G)*u-C,0,'zero-frequency bracket')
for m in [1,4]:
 for value in mv(J0,v[m]):eq(value,0,'two exact null columns')
# Exact obstruction constants, without numerical inequalities.
u8sq=Q(1,2);eq(F(1-2*u8sq),0,'n8 w=0')
u12=Q(1,2);eq(F((1-2*u12*u12)/(4*(1-u12))),Q(1,4),'n12 B');eq(F((u12+0)/2),Q(1,4),'n12 beta2')
checks.append('Exact four-dimensional algebraic field checks passed, including direct 5x5 eigenvectors, adjoint, real block, both inverse products, roots, and a physical zero-frequency example.')

maxima={'field_residual':0.0,'eigenvector':0.0,'adjoint':0.0,'direct_spectrum':0.0,'chart_uniform':0.0}
counts={'cells':0,'realizable_cells':0,'obstructed_cells':0,'physical_candidates':0,'obstruction_probes':0,'ties':0,'random_candidates':0,'random_trials':0,'direct_matrix_spectra':0}
cell_rows=[]
def numeric_point(n,j,x,z,G):
 C=1.;D=C/(4*z);u=math.cos(2*math.pi*j/n)
 k=(D*(1-2*u*u)-C*(1-u+x/(1+x)))/x
 c=C*(1+x);g=G*(1+x)**2/x;h=(G+D)/x;a=(k+h)*x-(c-g)/(1+x)
 return a,k,c,g,h

def inspect(n,j,x,p,strict=True,direct=True):
 a,k,c,g,h=p;assert min(p)>0
 s=1+x;res=a*x-k*x*x+c*x/s-g*x/s-h*x*x
 maxima['field_residual']=max(maxima['field_residual'],abs(res)/(1+sum(abs(t) for t in p)*max(x,x*x)))
 J=np.zeros((n,n))
 for i in range(n):
  J[i,i]+=a-2*k*x-c*x/s**2-g/s-h*x
  J[i,(i-1)%n]+=c/s;J[i,(i+2)%n]+=g*x/s**2;J[i,(i-2)%n]-=h*x
 theta=2*np.pi*np.arange(n)/n
 C=c/s;G=g*x/s**2;H=h*x;d=a-2*k*x-c*x/s**2-g/s-h*x
 ev=d+C*np.exp(-1j*theta)+G*np.exp(2j*theta)-H*np.exp(-2j*theta)
 scale=1+np.linalg.norm(J,2);q=np.exp(1j*theta[j]*np.arange(n))/np.sqrt(n)
 maxima['eigenvector']=max(maxima['eigenvector'],float(np.linalg.norm(J@q-ev[j]*q)/scale))
 maxima['adjoint']=max(maxima['adjoint'],float(np.linalg.norm(J.T@q-np.conj(ev[j])*q)/scale))
 det=k+h+(c-g)/s**2
 maxima['chart_uniform']=max(maxima['chart_uniform'],abs(det+ev[0].real/x)/(1+abs(det)))
 assert det>0
 if strict:
  out=[i for i in range(n) if i not in [j,n-j]]
  assert abs(ev[j].real)<1e-9*scale and max(ev[out].real)<-1e-10 and abs(ev[j].imag)>1e-9
  assert min(abs(ev))>1e-10 and min(abs(2j*ev[j].imag-ev))>1e-10
  ec=np.sqrt(2)*q.real;es=np.sqrt(2)*q.imag
  assert np.linalg.norm(np.array([ec,es])@np.array([ec,es]).T-np.eye(2))<1e-12
  assert np.linalg.norm(J@ec+ev[j].imag*es)/scale<1e-12
 if direct:
  counts['direct_matrix_spectra']+=1
  observed=np.linalg.eigvals(J)
  err=max(min(abs(observed-e)) for e in ev)/scale
  maxima['direct_spectrum']=max(maxima['direct_spectrum'],float(err));assert err<1e-11
 return ev

for n in range(5,73):
 N=n//2;uj=np.cos(2*np.pi*np.arange(N+1)/n);beta=(uj[:-1]+uj[1:])/2
 for j in range(1,(n+1)//4+1):
  assert j<n/2 and j<N
  L=max(0.,beta[j]);U=beta[j-1];u=uj[j];w=1-2*u*u;B=w/(4*(1-u));ok=w>1e-12 and B-L>1e-12
  counts['cells']+=1;counts['realizable_cells' if ok else 'obstructed_cells']+=1
  cell_rows.append({'n':n,'j':j,'L':L,'U':U,'w':w,'B':B,'criterion':bool(ok)})
  if ok:
   for t in [0.25,0.7]:
    z=L+t*(min(U,B)-L);delta=w/(4*z)-(1-u);x=delta/(3*(1+delta));G=2+1/(4*z)
    p=numeric_point(n,j,x,z,G);inspect(n,j,x,p,direct=n<=32)
    counts['physical_candidates']+=1
  else:
   for t in [0.001,0.1,0.5,0.9,0.999]:
    for x in [1e-8,0.01,0.5,4.]:
     z=L+t*(U-L);assert w/(4*z)-(1-u+x/(1+x))<1e-10;counts['obstruction_probes']+=1
 # Deliberately construct nonuniform critical midpoint ties when positivity allows.
 for j in range(1,(n+1)//4):
  z=beta[j];u=uj[j];delta=(1-2*u*u)/(4*z)-(1-u)
  if delta>1e-10:
   x=delta/(3*(1+delta));p=numeric_point(n,j,x,z,2+1/(4*z));ev=inspect(n,j,x,p,False,n<=32)
   assert abs(ev[j].real-ev[j+1].real)<1e-8
   assert len([e for e in ev if abs(e.real)<1e-8])==4
   counts['ties']+=1
# Independent raw-parameter rejection search, not the sufficiency recipe.
rng=np.random.default_rng(11042026)
for _ in range(1500):
 counts['random_trials']+=1;n=int(rng.integers(5,65));j=int(rng.integers(1,(n+1)//4+1))
 x,c,g,h=np.exp(rng.uniform(-3,3,4));u=math.cos(2*math.pi*j/n);C=c/(1+x);G=g*x/(1+x)**2;H=h*x
 k=(-c*(1+2*x)/(1+x)**2+C*u+(G-H)*(2*u*u-1))/x;a=(k+h)*x-(c-g)/(1+x)
 if min(a,k,c,g,h)<=0 or H<=G:continue
 z=C/(4*(H-G));N=n//2;us=np.cos(2*np.pi*np.arange(N+1)/n);beta=(us[:-1]+us[1:])/2;L=max(0.,beta[j]);U=beta[j-1]
 if not L<z<U:continue
 assert 1-2*u*u>0 and L<(1-2*u*u)/(4*(1-u))
 inspect(n,j,x,(a,k,c,g,h),direct=n<=24);counts['random_candidates']+=1
p5=tuple(float(q.approx()) for q in [(3*phi+22)/2,(3*phi-4)/2,F(2),F(16),F(6)])
ev5=inspect(5,1,1.,p5)
# Physical zero frequency and its two-dimensional real kernel.
p0=tuple(q.approx() for q in [a0,k0,c0,g0,h0]);assert min(p0)>0
J0n=np.array([[q.approx().real for q in row] for row in J0]);assert np.linalg.matrix_rank(J0n,tol=1e-10)==3
assert np.linalg.eigvalsh((J0n+J0n.T)/2)[-3]<0
report={'status':'PASS','python':platform.python_version(),'numpy':np.__version__,'seed':11042026,'exact_assertions':count,'counts':counts,'max_scaled_residuals':maxima,'five_node_spectrum':[[float(v.real),float(v.imag)] for v in ev5], 'zero_frequency_physical_tuple':p0,'notes':checks+['Finite tests do not prove universal statements; exact sign inequalities and all-n proofs are in the A11 source.','No g-path derivative, nonlinear tensor, transversality, or Lyapunov calculation was performed.']}
out=Path(__file__).parent
(out/'independent_results.json').write_text(json.dumps(report,indent=2)+'\n')
(out/'realizability_cells.json').write_text(json.dumps(cell_rows,indent=2)+'\n')
print(json.dumps(report,indent=2))
