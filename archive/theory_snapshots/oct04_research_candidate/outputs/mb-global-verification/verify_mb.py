"""Reproduce MB global-stability sanity checks: python verify_mb.py.
Requires numpy, scipy, matplotlib. Outputs JSON, trajectory NPZ and PNG here.
Numerical checks corroborate, but do not prove, the accompanying theorem.
"""
from pathlib import Path
import json
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
SEED, RUNS = 20261004, 64
rng = np.random.default_rng(SEED)

def matrix(n, q, p):
    a,k,c,g,h = p
    P = np.roll(np.eye(n), 1, axis=0)  # (P y)_i = y_{i-1}
    return -k*np.eye(n)+c*P-g*np.linalg.matrix_power(P,n-q)-h*np.linalg.matrix_power(P,q)

def mb(y,p,q):
    a,k,c,g,h=p
    return y*(a-k*y+c*np.roll(y,1)-g*np.roll(y,-q)-h*np.roll(y,q))

def dm(x,p,q):
    a,k,c,g,h=p
    return a*x-k*x*x+c*np.roll(x,1)/(1+x)-g*x/(1+np.roll(x,-q))-h*x*np.roll(x,q)

def spec(n,q,p,x):
    a,k,c,g,h=p
    th=2*np.pi*np.arange(n)/n
    b=-k+c*np.exp(-1j*th)-g*np.exp(1j*q*th)-h*np.exp(-1j*q*th)
    s=1+x
    d=a-2*k*x-c*x/s**2-g/s-h*x
    lam=d+(c/s)*np.exp(-1j*th)+(g*x/s**2)*np.exp(1j*q*th)-h*x*np.exp(-1j*q*th)
    M=k+g+h-c
    return float(k+b.real.max()),float(-b.real.max()),a/M,lam,b

t=np.sin(np.pi/14)
family=( (2-2.5*t*t)*2/t-(t-t*t/4)/(1+2/t),1-2.5*t*t,t,t*t/4,1 )
e=1/48
lower=((1+e)*(1+2*e)+e/(1+e),1,e,(1+e)**3+2*e,e)
cases=[
    ('reverse_rational_n7',7,2,(20301/1100,17/20,1/2,1/100,1),10),
    ('reverse_family_n7',7,2,family,2/t),
    ('lower_branch_n6',6,2,lower,e),
    ('stable_k_less_c_n8',8,2,(9/2,7,8,1,1),1),
    ('collision_q3_n6',6,3,(2,3,1/2,1/4,3/4),1),
]
# Last case is an MB collision test; its DM root is computed independently.
a,k,c,g,h=cases[-1][3]
A=k+h; b=a-A; mu=a+c-g
cases[-1]=(*cases[-1][:-1],(b+np.sqrt(b*b+4*A*mu))/(2*A))
report={'seed':SEED,'random_runs_per_case':RUNS,'initial_ratios':'independent log-uniform [1e-3,1e3]',
        'versions':{'numpy':np.__version__,'scipy':scipy.__version__},'cases':[], 'exclusions':[]}
fig,axes=plt.subplots(1,2,figsize=(12,4.6))
archive={}
for name,n,q,p,x in cases:
    K,delta,ys,lam,b=spec(n,q,p,x)
    B=matrix(n,q,p); sym=(B+B.T)/2
    assert delta>0
    np.testing.assert_allclose(np.linalg.eigvalsh(sym),np.sort(b.real),atol=1e-12)
    np.testing.assert_allclose(mb(np.full(n,ys),p,q),0,atol=1e-10)
    np.testing.assert_allclose(dm(np.full(n,x),p,q),0,atol=1e-10)
    # Independent complex-step Jacobian from the original DM field.
    jac=np.column_stack([dm(np.full(n,x,dtype=complex)+1j*1e-25*np.eye(n)[j],p,q).imag/1e-25 for j in range(n)])
    np.testing.assert_allclose(np.sort(np.linalg.eigvals(jac).real),np.sort(lam.real),atol=1e-11)
    T=40/(ys*delta)
    times=np.r_[0,np.geomspace(1e-7*T,T,500)]
    worst_end=0.; max_v_increase=0.; max_identity_error=0.; max_bound_error=0.
    min_ratio=np.inf; max_dv_away=-np.inf; count_away=0
    all_errors=[]; all_v=[]
    # Log coordinates guarantee strict positivity; equilibrium centering
    # avoids cancellation in a + B y at late times.
    for run in range(RUNS):
        u0=rng.uniform(-np.log(1000),np.log(1000),n)
        sol=solve_ivp(lambda _,u: B@(ys*np.expm1(u)),(0,T),u0,
                      method='Radau',jac=lambda _,u:B*(ys*np.exp(u))[None,:],
                      rtol=2e-9,atol=2e-11,t_eval=times)
        assert sol.success,sol.message
        u=sol.y.T; z=ys*np.expm1(u); y=ys*np.exp(u)
        err=np.max(np.abs(z),axis=1)/ys
        V=ys*np.sum(np.expm1(u)-u,axis=1)
        dv=np.einsum('ti,ij,tj->t',z,B,z)
        norm2=np.sum(z*z,axis=1)
        away=err>1e-7
        assert np.all(dv[away]<0)
        count_away+=int(away.sum())
        max_dv_away=max(max_dv_away,float(dv[away].max()))
        direct=np.array([np.dot(1-ys/yy,mb(yy,p,q)) for yy in y])
        max_identity_error=max(max_identity_error,float(np.max(np.abs(direct-dv)/(1+np.abs(dv)))))
        max_bound_error=max(max_bound_error,float(np.max((dv+delta*norm2)/(1+norm2))))
        max_v_increase=max(max_v_increase,float(np.max(np.diff(V))/(1+V[0])))
        min_ratio=min(min_ratio,float(y.min()/ys))
        worst_end=max(worst_end,float(err[-1]))
        all_errors.append(err); all_v.append(V)
    assert worst_end<1e-7
    assert max_identity_error<1e-10 and max_bound_error<1e-10 and max_v_increase<1e-9
    row={'name':name,'n':n,'q':q,'tuple_a_k_c_g_h':p,'x_star':x,'y_star':ys,
         'K':K,'delta':delta,'MB_abscissa':-ys*delta,'DM_abscissa':float(lam.real.max()),
         'T':T,'max_final_relative_inf_error':worst_end,'min_sampled_y_over_y_star':min_ratio,
         'max_normalized_V_increase':max_v_increase,'max_normalized_identity_error':max_identity_error,
         'max_normalized_bound_violation':max_bound_error,'max_Vdot_away':max_dv_away,
         'samples_away_from_roundoff':count_away}
    axes[0].semilogy(times*ys*delta,np.maximum(np.max(all_errors,axis=0),1e-16),label=name)
    archive[name+'_times']=times; archive[name+'_errors']=all_errors; archive[name+'_V']=all_v
    if lam.real.max()>0:
        m=int(np.argmax(lam.real)); alpha=float(lam[m].real)
        v=np.cos(2*np.pi*m*np.arange(n)/n); v/=np.linalg.norm(v)
        # Small perturbation of DM's OWN equilibrium along an unstable real
        # Fourier eigenspace. Norm grows as exp(alpha*t) to first order.
        dt=np.linspace(0,np.log(100)/alpha,400)
        dx0=1e-7*x*v
        sol=solve_ivp(lambda _,xx:dm(xx,p,q),(0,dt[-1]),x+dx0,
                      method='Radau',rtol=2e-11,atol=1e-13*x,t_eval=dt)
        assert sol.success
        growth=np.linalg.norm(sol.y.T-x,axis=1)/np.linalg.norm(dx0)
        slope=np.polyfit(dt[20:160],np.log(growth[20:160]),1)[0]
        row['DM_perturbation']={'mode':m,'T':float(dt[-1]),'growth_factor':float(growth[-1]),
                                'early_log_slope':float(slope),'predicted_slope':alpha}
        assert 90<growth[-1]<110 and abs(slope/alpha-1)<.02
        axes[1].semilogy(alpha*dt,growth,label=name)
        archive[name+'_DM_times']=dt; archive[name+'_DM_growth']=growth
    report['cases'].append(row)
    print(json.dumps(row),flush=True)

for n in [5,6,7,8,11]:
    p=(1/4,1/8,1,1,1/8)
    K,delta,ys,lam,b=spec(n,2,p,1)
    report['exclusions'].append({'name':'universal_forward','n':n,'K':K,'delta':delta,'MB_abscissa':-ys*delta,'DM_abscissa':float(lam.real.max())})
p=(16351/1100,1/2,3/2,1/100,1)
K,delta,ys,lam,b=spec(8,2,p,10)
report['exclusions'].append({'name':'both_unstable_n8','K':K,'delta':delta,'MB_abscissa':-ys*delta,'DM_abscissa':float(lam.real.max())})
axes[0].set(xlabel=r'$t y^*\delta$',ylabel='Worst relative infinity error (64 runs)',title='MB: all sampled positive starts converge')
axes[1].set(xlabel=r'$t\alpha_{DM}$',ylabel='Perturbation norm / initial norm',title='DM: unstable-mode perturbations grow')
for ax in axes:
    ax.grid(alpha=.25);ax.legend(fontsize=7)
fig.tight_layout();fig.savefig(OUT/'trajectories.png',dpi=180)
np.savez_compressed(OUT/'trajectories.npz',**archive)
(OUT/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print('All checks passed; results saved in',OUT)
