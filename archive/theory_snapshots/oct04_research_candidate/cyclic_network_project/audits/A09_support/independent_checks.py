"""Independent A09 corroboration, authored from the canonical field.

No P09 developer checker is imported or executed here. Exact Fraction checks
and ordinary floating point are distinct. Neither is a substitute for A09's
analytical proof. Requires Python 3 and NumPy; all outputs are reproducible.
"""
from pathlib import Path
from fractions import Fraction as Q
import json, math, platform
import numpy as np

OUT=Path(__file__).resolve().parent/'checks'
OUT.mkdir(exist_ok=True)
exact=[]
def ck(name, value):
    assert value, name
    exact.append({'check':name,'pass':True})

def quotient_series(numerator, denominator, order=3):
    """Exact power series by coefficient convolution, for original summands."""
    result=[]
    for j in range(order+1):
        rhs=Q(numerator[j]) if j<len(numerator) else Q(0)
        rhs-=sum(Q(denominator[k])*result[j-k] for k in range(1,min(j,len(denominator)-1)+1))
        result.append(rhs/Q(denominator[0]))
    return result

def exact_checks():
    # Coefficients in t of the five original directional terms through order 3.
    for a,k,c,h in [(Q(17,5),Q(7,10),Q(3,5),Q(9,10)),(Q(3,5),Q(4,5),Q(13,10),Q(1,2)),(Q(13,10),Q(4,5),Q(2,5),Q(1,2))]:
        A=k+h; b=a-A; gc=a+c
        jets=[quotient_series([0,a],[1]),quotient_series([0,0,-k],[1]),quotient_series([0,c],[1,1]),quotient_series([0,-gc],[1,1]),quotient_series([0,0,-h],[1])]
        ck(f'termwise directional derivatives {a,k,c,h}',[2*j[2] for j in jets]==[0,-2*k,-2*c,2*gc,-2*h])
        ck(f'full jet {a,k,c,h}',[sum(j[i] for j in jets) for i in range(4)]==[0,0,b,-A-b])
        # Coefficient of t in the mu and physical-g directional derivatives.
        ck(f'mixed coefficient {a}',quotient_series([0,1],[1,1])[1]==1 and quotient_series([0,-1],[1,1])[1]==-1)
        for r in [Q(-1,11),Q(-1,100),Q(0),Q(1,100),Q(1,11)]:
            for mu in [Q(-1,103),Q(0),Q(1,103)]:
                raw=a*r-k*r*r+c*r/(1+r)-(gc-mu)*r/(1+r)-h*r*r
                f=r*(mu+b*r-A*r*r)/(1+r)
                ck(f'original scalar identity {a,r,mu}',raw==f)
                fr=a-2*A*r+(c-gc+mu)/(1+r)**2
                ck(f'scalar derivative {a,r,mu}',fr==(mu+b*r-A*r*r)/(1+r)**2+r*(b-2*A*r)/(1+r))
                if b and A*r!=b:
                    u=A*r*r-b*r; alpha=(2*A*r-b)/((A*r-b)*(1+r))
                    ck(f'normal coordinate {a,r,mu}',(2*A*r-b)*f==alpha*u*(mu-u))
            mu=A*r*r-b*r
            ck(f'equilibrium original residual {a,r}',a*r-k*r*r+c*r/(1+r)-(gc-mu)*r/(1+r)-h*r*r==0)
            ck(f'uniform at root {a,r}',a-2*A*r+(c-gc+mu)/(1+r)**2==r*(b-2*A*r)/(1+r))
            if b and b-A*r:
                ck(f'uniform alternate {a,r}',r*(b-2*A*r)/(1+r)==-mu*(b-2*A*r)/((1+r)*(b-A*r)))
            if not b:
                ck(f'degenerate root and eigenvalue {r}',mu==A*r*r and a-2*A*r+(c-gc+mu)/(1+r)**2==-2*A*r*r/(1+r))
                if r: ck(f'decay derivative {r}',-2*r**(-3)*(-A*r**3/(1+r))==2*A/(1+r))
        if b:
            d1=-1/b; d2=2*A/b**3
            ck(f'branch derivative equations {b}',-b*d1==1 and 2*A*d1*d1-b*d2==0)
        ck(f'loci intersection {b}',(b*b/(4*A)==0)==(b==0))
    # Exact rational remainder identity for arbitrary mean-zero y, with collisions.
    for n in [5,6,7,8,10,12]:
        k,h,c=Q(4,5),Q(1,2),Q(2,5); a=k+h; gc=a+c
        vals=[Q(j-(n-1)/2).limit_denominator()/100 for j in range(n)]
        assert sum(vals)==0
        for q in range(1,n):
            for r in [Q(-1,10),Q(0),Q(1,10)]:
                x=[r+v for v in vals]; s=1+r
                F=[a*x[i]-k*x[i]**2+c*x[(i-1)%n]/(1+x[i])-gc*x[i]/(1+x[(i+q)%n])-h*x[i]*x[(i-q)%n] for i in range(n)]
                remainder=0
                for i,y in enumerate(vals):
                    yp,ym,yq=vals[(i-1)%n],vals[(i-q)%n],vals[(i+q)%n]
                    remainder+=-k*y*y-h*y*ym+c*(r*y*y/(s*s*(s+y))-yp*y/(s*(s+y)))-gc*(r*yq*yq/(s*s*(s+yq))-y*yq/(s*(s+yq)))
                ck(f'exact mean remainder n{n} q{q} r{r}',sum(F)/n+(k+h)*r**3/(1+r)==remainder/n)
    gradient1=[Q(1),Q(-1),Q(0),Q(0),Q(-1)]
    gradient2=[Q(-1),Q(0),Q(-1),Q(1),Q(0)]
    ck('codimension minor on columns k,g',gradient1[1]*gradient2[3]-gradient1[3]*gradient2[1]==-1)

def field(x,a,k,c,g,h,q):
    # Direct original five summands; roll follows receiving-node indexing.
    return a*x-k*x*x+c*np.roll(x,1)/(1+x)-g*x/(1+np.roll(x,-q))-h*x*np.roll(x,q)

def jacobian(x,a,k,c,g,h,q):
    n=len(x); J=np.zeros((n,n))
    for i in range(n):
        p=(i-1)%n; u=(i+q)%n; d=(i-q)%n
        J[i,i]+=a-2*k*x[i]
        J[i,p]+=c/(1+x[i]); J[i,i]-=c*x[p]/(1+x[i])**2
        J[i,i]-=g/(1+x[u]); J[i,u]+=g*x[i]/(1+x[u])**2
        J[i,i]-=h*x[d]; J[i,d]-=h*x[i]
    return J

def spectrum(n,q,r,a,k,c,g,h):
    th=2*np.pi*np.arange(n)/n; s=1+r
    d=a-2*k*r-c*r/s**2-g/s-h*r
    return d+c/s*np.exp(-1j*th)+g*r/s**2*np.exp(1j*q*th)-h*r*np.exp(-1j*q*th)

def spectral_error(eig, theo):
    rest=list(eig); errors=[]
    for v in theo:
        j=int(np.argmin([abs(z-v) for z in rest])); errors.append(abs(rest.pop(j)-v))
    return max(errors)/(1+max(abs(theo)))

def small_root(A,b,mu):
    # Cancellation-free local root, sign chosen by continuation to zero.
    return -2*mu/(b+math.copysign(math.sqrt(b*b+4*A*mu),b))

def numerical_checks():
    rng=np.random.default_rng(90261003)
    dimensions=[5,6,7,8,9,10,12,15,16]
    tuples=[(3.4,.7,.6,.9),(.6,.8,1.3,.5),(1.3,.8,.4,.5),(1.5,1.,.02,.5),(1.0001,.6,2.,.4),(.9999,.6,2.,.4)]
    rows=[]; slopes=[]; trans=[]; lyap=[]
    for n in dimensions:
        # Orthonormal real basis of E by QR of e_j-e_last.
        E=np.vstack([np.eye(n-1),-np.ones(n-1)])
        E=np.linalg.qr(E)[0]
        for q in range(1,n):
            for a,k,c,h in tuples:
                A=k+h; b=a-A; gc=a+c
                delta=c*(1-math.cos(2*math.pi/n))
                rad=min(1e-4,delta/(100*(1+a+k+c+gc+h)))
                if b: rad=min(rad,abs(b)/(100*A))
                eps=min(gc/1000,abs(b)*rad/4) if b else A*rad*rad/4
                for mu in [-eps,0.,eps]:
                    g=gc-mu
                    rs=[0.]
                    if b and mu: rs.append(small_root(A,b,mu))
                    if not b and mu>0: rs += [math.sqrt(mu/A),-math.sqrt(mu/A)]
                    for r in rs:
                        x=np.full(n,r); J=jacobian(x,a,k,c,g,h,q)
                        L=spectrum(n,q,r,a,k,c,g,h)
                        residual=float(max(abs(field(x,a,k,c,g,h,q))))
                        er=spectral_error(np.linalg.eigvals(J),L)
                        # complex-step validates entry-wise differentiation including collisions
                        Jcs=np.column_stack([np.imag(field(x.astype(complex)+1e-25j*np.eye(n)[j],a,k,c,g,h,q))/1e-25 for j in range(n)])
                        je=float(np.max(abs(J-Jcs))/(1+np.max(abs(J))))
                        assert residual<1e-12 and er<1e-11 and je<1e-12
                        assert max(L[1:].real)<-delta/2
                        # Tiny b stress cases have eigenvalues near machine precision.
                        # Stability sign is checked in exact scalar formula, not rounded eig.
                        lam=mu if r==0 else r*(b-2*A*r)/(1+r)
                        if mu:
                            expected=np.sign(mu) if r==0 else (-np.sign(mu) if b else -1)
                            assert np.sign(lam)==expected
                        if b and r:
                            assert (r>0)==(np.sign(mu)==-np.sign(b))
                            alpha=(2*A*r-b)/((A*r-b)*(1+r)); assert alpha>0
                        rows.append(dict(n=n,q=q,a=a,k=k,c=c,h=h,b=b,mu=mu,r=r,residual=residual,spectrum_error=er,jacobian_error=je,lambda0=lam,transverse_max=float(max(L[1:].real))))
                if b:
                    dm=eps/10
                    dm_slope=(small_root(A,b,dm)-small_root(A,b,-dm))/(2*dm)
                    dg_slope=(small_root(A,b,-dm)-small_root(A,b,dm))/(2*dm)
                    rel=abs(dm_slope+1/b)/abs(1/b)
                    assert rel<1e-6 and abs(dg_slope-1/b)/abs(1/b)<1e-6
                    slopes.append(dict(n=n,q=q,b=b,relative_error=rel,mu_slope=dm_slope,g_slope=dg_slope))
                # Fixed-mean transverse Newton search on original field.
                # Failure to find y != 0 is not an IFT proof.
                r=rad/2; mu=eps/2; g=gc-mu
                z=rng.normal(size=n-1)*rad/10
                initial=float(np.linalg.norm(z))
                for it in range(8):
                    x=np.full(n,r)+E@z
                    t=E.T@field(x,a,k,c,g,h,q)
                    dz=np.linalg.solve(E.T@jacobian(x,a,k,c,g,h,q)@E,t)
                    z-=dz
                    if np.linalg.norm(dz)<1e-15: break
                zfinal=float(np.linalg.norm(z)); assert zfinal<1e-11
                trans.append(dict(n=n,q=q,b=b,initial_norm=initial,final_norm=zfinal,iterations=it+1))
            # Degenerate full-field stress: explicit conservative K and small radius.
            k,h,c=.8,.5,.4; a=k+h; g=a+c; A=a
            delta=c*(1-math.cos(2*math.pi/n))
            K=(A+(32/9)*(c+g))/n
            Jc=jacobian(np.zeros(n),a,k,c,g,h,q)
            Hs=E.T@((Jc+Jc.T)/2)@E
            assert abs(max(np.linalg.eigvalsh(Hs))+delta)<1e-12
            rho=min(1e-5,delta/(8*K),delta/(200*(a+k+c+g+h)))
            for j in range(20):
                r=float(rng.uniform(-rho,rho)); y=E@rng.normal(size=n-1)
                y*=float(rng.uniform(.02,1)*rho)/np.linalg.norm(y)
                x=np.full(n,r)+y; fx=field(x,a,k,c,g,h,q)
                rr=float(np.mean(fx)); yd=fx-rr
                R=rr+A*r**3/(1+r)
                ratio=abs(R)/(np.dot(y,y))
                assert ratio<=K*(1+1e-7)
                vd=r*rr+float(y@yd)
                bound=-A*r**4/(1+rho)-delta*np.dot(y,y)/4
                assert vd<=bound+1e-25
                # Integral B via five-point Gauss-Legendre, only a numerical check.
                ts,weights=np.polynomial.legendre.leggauss(5)
                B=sum(wt*(E.T@(jacobian(np.full(n,r)+(tt+1)*y/2,a,k,c,g,h,q)-Jc)@E) for tt,wt in zip(ts,weights))/2
                bn=float(np.linalg.norm(B,2)); assert bn<=delta/2
                lyap.append(dict(n=n,q=q,r=r,y_norm=float(np.linalg.norm(y)),R_over_y2=ratio,K=K,Vdot=vd,bound=bound,B_norm=bn,delta=delta))
    summary=dict(python=platform.python_version(),numpy=np.__version__,seed=90261003,dimensions=dimensions,network_pairs=sum(n-1 for n in dimensions),noncoprime_pairs=sum(math.gcd(n,q)>1 for n in dimensions for q in range(1,n)),parameter_tuples=tuples,equilibrium_cases=len(rows),slope_cases=len(slopes),transverse_searches=len(trans),lyapunov_cases=len(lyap),max_equilibrium_residual=max(r['residual'] for r in rows),max_scaled_spectrum_error=max(r['spectrum_error'] for r in rows),max_scaled_jacobian_error=max(r['jacobian_error'] for r in rows),max_relative_slope_error=max(r['relative_error'] for r in slopes),max_transverse_search_norm=max(r['final_norm'] for r in trans),limitations='Ordinary floating point, finite samples, no interval certification. Tiny-b eigenvalue signs use scalar formula; direct numerical eigensolvers cannot certify near-zero signs. Analytical arguments establish the universal claims.')
    for name,data in [('equilibrium_results',rows),('slope_results',slopes),('transverse_search_results',trans),('lyapunov_results',lyap)]:
        (OUT/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
    return summary

if __name__=='__main__':
    exact_checks(); summary=numerical_checks(); summary['exact_fraction_checks']=len(exact)
    (OUT/'exact_results.json').write_text(json.dumps(exact,indent=2)+'\n')
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
