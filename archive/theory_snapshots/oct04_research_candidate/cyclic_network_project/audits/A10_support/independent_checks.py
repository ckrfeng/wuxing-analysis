"""A10 corroboration, independently written from the original five-term field.
Finite floating-point searches are not proofs or interval certificates.
No P10 developer checker is imported, executed, or used to generate this file.
Run with Python 3 plus NumPy; outputs go beside this script.
"""
from pathlib import Path
from fractions import Fraction as Q
import csv, json, math, platform
import numpy as np
out=Path(__file__).resolve().parent
checks=0

def ck(value):
 global checks
 checks+=1
 assert value, f'exact assertion {checks}'

def scalar(r,a,k,c,g,h):
 return a*r-k*r*r+c*r/(1+r)-g*r/(1+r)-h*r*r

def coeff(r,a,k,c,g,h):
 s=1+r
 return a-2*k*r-c*r/s**2-g/s-h*r, c/s, g*r/s**2, h*r

# Exact rational original-field and derivative checks at six folds.
tuples=[tuple(Q(s) for s in row) for row in [
 ('3','1','1','1'),('6','1/10','1/10','9/10'),
 ('101/50','1','3/7','1'),('23','2','1/20','1'),
 ('7/3','1/7','9/5','2/3'),('11','3/2','7','1/2')]] # (a,k,c,h)
exact_rows=[]
for a,k,c,h in tuples:
 A=k+h;b=a-A;rf=b/(2*A);sf=1+rf;gc=a+c;gf=gc+b*b/(4*A)
 ck(b>0);ck(sf==(a+A)/(2*A));ck(gf==c+A*sf*sf)
 ck(gf-gc==b*b/(4*A));ck(scalar(rf,a,k,c,gf,h)==0)
 d,C,G,H=coeff(rf,a,k,c,gf,h)
 ck(d+C+G-H==0);ck(G-H==rf*(k+c/sf**2));ck(G-H>0)
 derivatives=[Q(0),-2*k,-2*c/sf**3,2*gf/sf**3,-2*h]
 ck(sum(derivatives)==-2*A*rf/sf);ck(sum(derivatives)/2==-A*rf/sf)
 ck(-rf/sf<0)
 for ufrac in [Q(-2,5),Q(-1,10),Q(0),Q(1,7),Q(2,5)]:
  u=ufrac*rf;r=rf+u
  for nufrac in [Q(-1,3),Q(0),Q(1,17),Q(1,2)]:
   nu=nufrac*A*rf**2;g=gf-nu;mu=gc-g
   ck(mu+b*r-A*r*r==nu-A*u*u)
   ck(scalar(r,a,k,c,g,h)==r/(1+r)*(nu-A*u*u))
   ck(r/(1+r)>= (rf/2)/(1+3*rf/2))
 for tfrac in [Q(1,10000),Q(1,5),Q(1,2),Q(9,10)]:
  t=tfrac*rf;nu=A*t*t;g=gf-nu;Delta=2*A*t;rm=rf-t;rp=rf+t
  ck(gc<g<gf);ck(Delta**2==b*b+4*A*(gc-g));ck(0<Delta<b)
  for r,sgn in [(rm,1),(rp,-1)]:
   ck(scalar(r,a,k,c,g,h)==0)
   d,C,G,H=coeff(r,a,k,c,g,h)
   ck(d+C+G-H==sgn*r/(1+r)*Delta)
  for r,sgn in [(rm/2,-1),((rm+rp)/2,1),(rp+1,-1)]:
   ck(scalar(r,a,k,c,g,h)==-A*r/(1+r)*(r-rm)*(r-rp))
   ck(sgn*scalar(r,a,k,c,g,h)>0)
 M=gf-h*sf*sf;ck(M==c+k*sf*sf);ck(M>0)
 # Rational t chosen by exact halving to satisfy all three defining bounds.
 t=rf/4
 while not (t<M/(4*h*sf) and t*t<M/(2*(A+h))):t/=2
 ck(t<rf/2);ck(2*h*sf*t<M/2);ck((A+h)*t*t<M/2)
 ck(gf-A*t*t-h*(sf+t)**2==M-2*h*sf*t-(A+h)*t*t)
 ck(gf-A*t*t-h*(sf+t)**2>0)
 exact_rows.append({'a':str(a),'k':str(k),'c':str(c),'h':str(h),'rf':str(rf),'gf':str(gf),'Gf_minus_Hf':str(rf*(k+c/sf**2))})

# The supplied counterexample, with all six real parts retained exactly.
a,k,c,g,h=map(Q,['6','1/10','1/10','101/10','9/10'])
A=k+h;b=a-A;gc=a+c;gf=gc+b*b/(4*A)
ck((A,b,gc,gf)==(Q(1),Q(5),Q(61,10),Q(247,20)));ck(gc<g<gf)
cosines=[Q(1),Q(1,2),Q(-1,2),Q(-1),Q(-1,2),Q(1,2)]
witness={}
for r in [Q(1),Q(4)]:
 ck(scalar(r,a,k,c,g,h)==0)
 d,C,G,H=coeff(r,a,k,c,g,h)
 reals=[d+(C+G-H)*v for v in cosines]
 witness[str(r)]={'d':str(d),'C':str(C),'G':str(G),'H':str(H),'real_parts':list(map(str,reals)),'unstable_real_dimension':sum(x>0 for x in reals)}
 if r==4:
  ck((d,C,G,H)==(Q(-109,250),Q(1,50),Q(202,125),Q(18,5)))
  ck(reals[0]==Q(-12,5));ck(reals[3]==Q(191,125))
 else:
  ck(reals[0]==Q(3,2));ck(reals[1]==reals[5]==Q(53,80));ck(sum(x>0 for x in reals)==3)
# Canonical equality G=H at the upper root: r+=2, r-=8/5.
ea,ek,ec,eg,eh=map(Q,['23/5','1/10','3/10','81/10','9/10'])
ck(scalar(Q(2),ea,ek,ec,eg,eh)==0)
ed,eC,eG,eH=coeff(Q(2),ea,ek,ec,eg,eh)
ck(eG==eH);ck(ed+eC+eG-eH==Q(-4,15));ck(ea+ec<eg<ea+ec+(ea-ek-eh)**2/(4*(ek+eh)))

# Direct original-field and additive coordinate Jacobian implementation.
def field(x,a,k,c,g,h,q):
 return a*x-k*x*x+c*np.roll(x,1)/(1+x)-g*x/(1+np.roll(x,-q))-h*x*np.roll(x,q)
def jac(x,a,k,c,g,h,q):
 n=len(x);J=np.zeros((n,n))
 for i in range(n):
  im=(i-1)%n;ipq=(i+q)%n;imq=(i-q)%n
  J[i,i]+=a-2*k*x[i]
  J[i,im]+=c/(1+x[i]);J[i,i]+=-c*x[im]/(1+x[i])**2
  J[i,i]+=-g/(1+x[ipq]);J[i,ipq]+=g*x[i]/(1+x[ipq])**2
  J[i,i]+=-h*x[imq];J[i,imq]+=-h*x[i]
 return J

def spectrum(n,q,r,a,k,c,g,h):
 d,C,G,H=coeff(r,a,k,c,g,h);theta=2*np.pi*np.arange(n)/n
 return d+C*np.exp(-1j*theta)+G*np.exp(1j*q*theta)-H*np.exp(-1j*q*theta)

rows=[];maxerr=0.;maxres=0.;maxsym=0.;maxfd=0.
def match_spectra(direct,pred,scale):
 # Perfect bipartite matching under tolerance retains all multiplicities.
 cost=abs(direct[:,None]-pred[None,:]);owner={}
 def augment(i,seen):
  for j in np.argsort(cost[i]):
   j=int(j)
   if cost[i,j]>2e-11*scale:break
   if j in seen:continue
   seen.add(j)
   if j not in owner or augment(owner[j],seen):owner[j]=i;return True
  return False
 assert all(augment(i,set()) for i in range(len(direct)))
 return max(float(cost[i,j]) for j,i in owner.items())/scale

def inspect(n,q,r,a,k,c,g,h,category,branch):
 global maxerr,maxres,maxsym
 x=np.full(n,r);J=jac(x,a,k,c,g,h,q);pred=spectrum(n,q,r,a,k,c,g,h)
 direct=np.linalg.eigvals(J)
 scale=max(1.,np.linalg.norm(J,2));err=match_spectra(direct,pred,scale)
 assert err<2e-11
 residual=float(np.max(abs(field(x,a,k,c,g,h,q)))/max(1.,abs(a*r)+abs(k*r*r)+abs(c*r/(1+r))+abs(g*r/(1+r))+abs(h*r*r)))
 assert residual<2e-12
 # Symmetric part spectrum independently sorted, including repeated values.
 symerr=float(np.max(abs(np.linalg.eigvalsh((J+J.T)/2)-np.sort(pred.real)))/scale)
 assert symerr<2e-11
 maxerr=max(maxerr,err);maxres=max(maxres,residual);maxsym=max(maxsym,symerr)
 row=dict(n=n,q=q,category=category,branch=branch,r=r,g=g,max_real=float(max(pred.real)),max_transverse=float(max(pred[1:].real)),unstable_labels=int(sum(pred.real>1e-10*scale)),scaled_spectral_error=err,scaled_residual=residual)
 rows.append(row)
 return pred

ns=[5,6,7,8,9,10,12,15,16,18,21,24]
pairs=[(n,q) for n in ns for q in range(1,n)]
for n,q in pairs:
 for aa,kk,cc,hh in tuples:
  a,k,c,h=map(float,(aa,kk,cc,hh));A=k+h;b=a-A;rf=b/(2*A);sf=1+rf;gc=a+c;gf=gc+b*b/(4*A)
  delta=c/sf*(1-math.cos(2*math.pi/n))
  lam=inspect(n,q,rf,a,k,c,gf,h,'fold','double')
  assert abs(lam[0])<2e-12*max(1,abs(gf))
  assert max(lam[1:].real)<=-delta+1e-12*max(1,abs(gf))
  assert min(abs(lam[1:]))>delta*.99999
  # Both roots in a sufficiently small neighborhood, found independently.
  t=rf*1e-5
  for attempt in range(60):
   g=gf-A*t*t
   near=[spectrum(n,q,rf+s*t,a,k,c,g,h) for s in [-1,1]]
   if all(max(v[1:].real)<-delta/2 for v in near):break
   t/=2
  else:raise AssertionError('no finite near-fold witness found')
  for s,name in [(-1,'lower'),(1,'upper')]:
   lam=inspect(n,q,rf+s*t,a,k,c,g,h,'near_fold',name)
   assert max(lam[1:].real)<-delta/2
   assert (-s)*lam[0].real>0
  for frac in [.05,.25,.6,.9,.99]:
   t=rf*frac;g=gf-A*t*t
   for s,name in [(-1,'lower'),(1,'upper')]:
    lam=inspect(n,q,rf+s*t,a,k,c,g,h,'interior',name)
    assert (-s)*lam[0].real>0
  M=gf-h*sf*sf;tstar=min(rf/2,M/(4*h*sf),math.sqrt(M/(2*(A+h))))
  for frac in [.25,.999]:
   t=tstar*frac;g=gf-A*t*t;r=rf+t
   lam=inspect(n,q,r,a,k,c,g,h,'explicit_interval','upper')
   assert gc<g<gf and g-h*(1+r)**2>0 and max(lam.real)<0
 for r in [1.,4.]:
  if n==6 and q==1:inspect(n,q,r,6.,.1,.1,10.1,.9,'exact_counterexample','lower' if r==1 else 'upper')
 lam=inspect(n,q,2.,float(ea),float(ek),float(ec),float(eg),float(eh),'G_equals_H','upper')
 assert max(lam.real)<0

# Static random counterexample search, no path continuation or Hopf analysis.
rng=np.random.default_rng(100310)
search=[]
for case in range(1500):
 n,q=pairs[int(rng.integers(len(pairs)))];k,c,h=10**rng.uniform(-1.5,1.3,3);A=k+h;b=A*10**rng.uniform(-1.5,1.2);a=A+b
 rf=b/(2*A);gf=a+c+b*b/(4*A);t=rf*rng.uniform(.03,.999);g=gf-A*t*t
 vals=[]
 for s in [-1,1]:
  lam=inspect(n,q,rf+s*t,a,k,c,g,h,'random_interior','lower' if s==-1 else 'upper');vals.append(lam)
 upper_condition=g/(1+rf+t)**2>=h
 if upper_condition:assert max(vals[1].real)<0
 search.append(dict(case=case,n=n,q=q,a=a,k=k,c=c,g=g,h=h,upper_max=float(max(vals[1].real)),lower_unstable=int(sum(vals[0].real>1e-9))))
# Test the direct Jacobian away from synchrony by complex-step differentiation.
for n,q in pairs:
 x=rng.uniform(.1,3,n);a,k,c,g,h=3.,.7,.3,4.,.5
 J=jac(x,a,k,c,g,h,q)
 Jcs=np.column_stack([field(x.astype(complex)+1e-25j*np.eye(n)[j],a,k,c,g,h,q).imag/1e-25 for j in range(n)])
 err=float(np.max(abs(J-Jcs))/max(1.,np.max(abs(J))));maxfd=max(maxfd,err);assert err<1e-12

with (out/'matrix_cases.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
with (out/'static_search.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(search[0]));w.writeheader();w.writerows(search)
summary=dict(status='PASS',exact_assertions=checks,exact_folds=exact_rows,counterexample=witness,dimensions=ns,nq_pairs=len(pairs),matrix_cases=len(rows),near_fold_branch_cases=sum(r['category']=='near_fold' for r in rows),random_parameter_cases=len(search),random_upper_unstable=sum(r['upper_max']>1e-9 for r in search),random_lower_index_above_one=sum(r['lower_unstable']>1 for r in search),max_scaled_spectral_error=maxerr,max_scaled_field_residual=maxres,max_scaled_symmetric_part_error=maxsym,max_scaled_complex_step_jacobian_error=maxfd,environment={'python':platform.python_version(),'numpy':np.__version__},scope='Finite corroboration only; no interval proof, local-equilibrium completeness certificate, invariant-manifold computation, Hopf result or global basin classification.')
(out/'independent_results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['exact_folds']},indent=2))
