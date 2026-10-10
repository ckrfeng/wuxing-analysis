#!/usr/bin/env python3
"""Independent A05 finite-precision corroboration, not a proof or old-run replay.

Standard library only. Run from any directory; outputs sit beside this script.
No P05 validation code is imported. The direct P04 expression is maximized
over all n Fourier labels; the predicted cells use separate integer indexing.
"""
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import platform

getcontext().prec = 120
TOL = D('1e-85')

def atan_inv(q):
    z = D(1)/q
    term = z
    out = term
    j = 1
    while True:
        term *= -z*z
        add = term/(2*j+1)
        new = out+add
        if new == out:
            return new
        out = new
        j += 1

PI = 16*atan_inv(D(5))-4*atan_inv(D(239))

def cos(z):
    z %= 2*PI
    if z > PI:
        z -= 2*PI
    term = out = D(1)
    j = 1
    while True:
        term *= -z*z / ((2*j-1)*(2*j))
        new = out+term
        if new == out:
            return new
        out = new
        j += 1

def near(a,b):
    return abs(a-b) <= TOL*max(D(1),abs(a),abs(b))

def selected(values):
    top=max(values)
    return [j for j,v in enumerate(values) if near(v,top)]

def labels(n,reps):
    return sorted({m for j in reps for m in (j,(-j)%n)})

records=[]
summary={'dimensions':36, 'switches':0, 'strict_cells':0,
         'cases_by_kind':{}, 'max_scaled_residual':D(0),
         'max_scaled_dispersion_error':D(0), 'stable_path_points':0}
grids={}
for n in range(5,41):
    all_u=[cos(2*PI*m/n) for m in range(n)]
    all_w=[cos(4*PI*m/n) for m in range(n)]
    N=n//2
    J=(n+1)//4
    u=all_u[:N+1]
    beta=[(u[j]+u[j+1])/2 for j in range(N)]
    assert all(u[j]>u[j+1] for j in range(N))
    positive=[j for j in range(N) if 4*j+2<n]
    assert positive==list(range(J))
    for j,b in enumerate(beta):
        assert near(b,cos(PI/n)*cos((2*j+1)*PI/n))
        if 4*j+2==n:
            assert near(b,D(0))
        elif 4*j+2<n:
            assert b>0
        else:
            assert b<0
    alpha=[1/beta[j] for j in positive]
    grids[n]=(all_u,all_w,u,beta,alpha)
    summary['switches']+=len(positive)
    summary['strict_cells']+=J+1

def check(n,chi,reps,kind,k=D(1),x=D(1),c=D(4),g=D(4),h=None):
    chi,k,x,c,g=map(D,(chi,k,x,c,g))
    s=1+x
    if h is None:
        h=g/s**2+chi*c/(4*s*x)
    h=D(h)
    a=(k+h)*x-(c-g)/s
    assert min(a,k,c,g,h,x)>0
    C=c/s;G=g*x/s**2;H=h*x
    assert near(chi,4*(H-G)/C)
    # Original five-term DM expression, not a stored scalar residual.
    terms=[a*x,-k*x*x,c*x/s,-g*x/s,-h*x*x]
    residual=sum(terms)
    scaled=abs(residual)/max(D(1),sum(abs(t) for t in terms))
    summary['max_scaled_residual']=max(summary['max_scaled_residual'],scaled)
    assert scaled<TOL
    d=a-2*k*x-c*x/s**2-g/s-h*x
    all_u,all_w,_,_,_=grids[n]
    direct=[d+C*u+(G-H)*w for u,w in zip(all_u,all_w)]
    quadratic=[d-(G-H)+C*u+2*(G-H)*u*u for u in all_u]
    for a1,b1 in zip(direct,quadratic):
        e=abs(a1-b1)/max(D(1),abs(a1),abs(b1))
        summary['max_scaled_dispersion_error']=max(summary['max_scaled_dispersion_error'],e)
        assert e<TOL
    got=selected(direct)
    assert got==labels(n,reps),(n,kind,str(chi),got,labels(n,reps))
    if chi>0:
        assert k+h+(c-g)/s**2>0
    if kind=='stable_path':
        assert max(direct)<-1
        summary['stable_path_points']+=1
    summary['cases_by_kind'][kind]=summary['cases_by_kind'].get(kind,0)+1
    records.append({'n':n,'kind':kind,'chi':str(chi),'x':str(x),
                    'parameters':list(map(str,(a,k,c,g,h))),
                    'expected_representatives':reps,'selected_labels':got,
                    'max_real_part':str(max(direct)),'scaled_residual':str(scaled)})

for n in range(5,41):
    _,_,u,beta,alpha=grids[n]
    J=len(alpha)
    # Three strictly interior vertices per retained cell.
    for j in range(J+1):
        low=max(D(0),beta[j])
        high=D(1) if j==0 else beta[j-1]
        for weight in (D('0.2'),D('0.5'),D('0.8')):
            v=low+weight*(high-low)
            check(n,1/v,[j],'cell')
            # A second canonical construction away from the simple family.
            x=D(2)/3;c=D(7)/5;g=D(11)/7
            check(n,1/v,[j],'general_realization',k=D(3),x=x,c=c,g=g)
    for j,threshold in enumerate(alpha):
        check(n,threshold,[j,j+1],'tie')
        lower=D(0) if j==0 else alpha[j-1]
        upper=threshold+1 if j==J-1 else alpha[j+1]
        radius=min(threshold-lower,upper-threshold)/4
        eps=radius*D('1e-12')
        check(n,threshold-eps,[j],'immediate_left')
        check(n,threshold+eps,[j+1],'immediate_right')
        k=(threshold+radius)/2+1
        for chi,reps in ((threshold-radius,[j]),(threshold,[j,j+1]),(threshold+radius,[j+1])):
            check(n,chi,reps,'stable_path',k=k)
        # Finite-difference crossing in branch coordinates; analytic derivative is in A05.
        assert (1-(threshold-eps)*beta[j])>0
        assert (1-(threshold+eps)*beta[j])<0
    for chi,reps,kind in ((D(-1),[0],'convex'),(D(0),[0],'T_zero'),
                          (D(1),[0],'vertex_one'),(D('1e30'),[J],'large_chi')):
        check(n,chi,reps,kind)
    # All negative-midpoint equalities: tune canonical g to keep h positive.
    for j,b in enumerate(beta):
        if 4*j+2>n:
            chi=1/b
            check(n,chi,[0],'negative_midpoint_lower_tie',g=4*(abs(chi)+1))

# All explicit examples, including three regime representatives and four terminal cases.
for chi in (D(-1),D(0),D(1)):
    check(5,chi,[0],'explicit_regime')
for n,chi,reps in ((5,D(0),[0]),(8,D(2),[1]),(6,D(4)/3,[0,1]),
                  (8,2*D(2).sqrt(),[1,2])):
    check(n,chi,reps,'explicit_example')
for n in (8,9,10,11):
    beta=grids[n][3];J=(n+1)//4
    check(n,2/beta[J-1],[J],'explicit_terminal')

# Analytically identified fold and two-branch cautions, exact rational arithmetic.
def rational_residual(a,k,c,g,h,x):
    return a*x-k*x*x+c*x/(1+x)-g*x/(1+x)-h*x*x
assert rational_residual(F(6),F(1),F(1),F(9),F(1),F(1))==0
assert F(1)+F(1)+(F(1)-F(9))/4==0
for x in (F(1,4),F(3)):
    assert rational_residual(F(17,2),F(1),F(1),F(11),F(1),x)==0
check(8,D(-10),[0],'fold_caution',c=D(1),g=D(9),h=D(1))
for x in (D('0.25'),D(3)):
    C=1/(1+x);G=11*x/(1+x)**2;H=x
    chi=4*(H-G)/C
    check(8,chi,[0] if x<1 else [2],'two_branch_caution',x=x,c=D(1),g=D(11),h=D(1))

assert summary['switches']==sum((n+1)//4 for n in range(5,41))==198
assert summary['strict_cells']==234
summary['total_cases']=len(records)
summary['python_version']=platform.python_version()
summary['precision_digits']=getcontext().prec
summary['comparison_tolerance']=str(TOL)
summary['trigonometry']='Decimal Taylor cosine; pi by Machin formula, both at 120 digits'
summary['scope']='Independent corroboration; neither interval certificate nor reproduction of P05 historical run'
summary['passed']=True
summary={key:str(value) if isinstance(value,D) else value for key,value in summary.items()}
out=Path(__file__).resolve().parent
(out/'independent_results.json').write_text(json.dumps({'summary':summary,'cases':records},indent=2)+'\n')
(out/'independent_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
