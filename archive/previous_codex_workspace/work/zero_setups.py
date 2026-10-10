from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path('outputs')
header='''# Extended model from Part 13 of the supplied Claude record.
# All initial values are positive. Wood x1 crosses zero near t=0.063358.
# Diagnostic example: the rebellion term violates nonnegative-state invariance.
par a=2,k=0.5,c=1,g=0.5,h=0.3
par gd=0.35,b=0.1,eps=0.5
'''
lines=[]
for i in range(5):
 me=f'x{i+1}';mo=f'x{(i-1)%5+1}';ch=f'x{(i+1)%5+1}';ta=f'x{(i+2)%5+1}';co=f'x{(i-2)%5+1}'
 lines.append(f"{me}'=a*{me}-k*{me}^2+c*{mo}/(1+{me})-gd*{ch}*{me}/(1+{me})-g*{me}/(1+{ta})-h*{me}*{co}-b*{ta}/(1+eps*{me})")
text=header+'\n'.join(lines)+'''
init x1=0.01,x2=1,x3=2,x4=1,x5=0.01
@ meth=rungekutta,dt=0.0001,total=0.3
@ xp=t,yp=x1,xlo=0,xhi=0.3,ylo=-0.015,yhi=0.015
@ maxstor=10000,bound=1000
done
'''
(out/'extended_negative_example.ode').write_text(text)
head2='''# Simple modified model: all components approach zero from above.
# This uses the bistable parameter example in the supplied record.
# Initial activity 0.25 is below the synchronous threshold 0.5.
par a=2,k=0.5,c=0.1,g=2.5,h=0.3
'''
lines2=[]
for i in range(5):
 me=f'x{i+1}';mo=f'x{(i-1)%5+1}';ta=f'x{(i+2)%5+1}';co=f'x{(i-2)%5+1}'
 lines2.append(f"{me}'=a*{me}-k*{me}^2+c*{mo}/(1+{me})-g*{me}/(1+{ta})-h*{me}*{co}")
(out/'simple_approach_zero_example.ode').write_text(head2+'\n'.join(lines2)+'''
init x1=0.25,x2=0.25,x3=0.25,x4=0.25,x5=0.25
@ meth=rungekutta,dt=0.01,total=60
@ xp=t,yp=x1,xlo=0,xhi=60,ylo=0,yhi=0.27
@ maxstor=10000,bound=1000
done
''')
# Check all expanded equations against the vector-form equations.
def full(t,x):
 return 2*x-.5*x*x+np.roll(x,1)/(1+x)-.35*np.roll(x,-1)*x/(1+x)-.5*x/(1+np.roll(x,-2))-.3*x*np.roll(x,2)-.1*np.roll(x,-2)/(1+.5*x)
def simple(t,x):
 return 2*x-.5*x*x+.1*np.roll(x,1)/(1+x)-2.5*x/(1+np.roll(x,-2))-.3*x*np.roll(x,2)
rng=np.random.default_rng(0)
for rows,params,fun in [(lines,dict(a=2,k=.5,c=1,g=.5,h=.3,gd=.35,b=.1,eps=.5),full),(lines2,dict(a=2,k=.5,c=.1,g=2.5,h=.3),simple)]:
 for _ in range(50):
  x=rng.uniform(.01,3,5);d=dict(params);d.update({f'x{i+1}':x[i] for i in range(5)})
  vals=np.array([eval(row.split('=',1)[1].replace('^','**'),{'__builtins__':{}},d) for row in rows])
  assert np.allclose(vals,fun(0,x),rtol=1e-13,atol=1e-13)
def ev(t,x):return x[0]
ev.direction=-1
s=solve_ivp(full,(0,.3),[.01,1,2,1,.01],rtol=1e-11,atol=1e-13,method='DOP853',t_eval=np.linspace(0,.3,3001),events=ev,max_step=.001)
u=solve_ivp(simple,(0,60),np.full(5,.25),rtol=1e-11,atol=1e-13,method='DOP853',t_eval=np.linspace(0,60,1201))
# Fixed-step RK4 check matches the specified XPPAUT method and dt.
x=np.array([.01,1,2,1,.01]);dt=.0001;arr=[x.copy()]
for j in range(3000):
 t=j*dt;k1=full(t,x);k2=full(t+dt/2,x+dt*k1/2);k3=full(t+dt/2,x+dt*k2/2);k4=full(t+dt,x+dt*k3)
 x=x+dt*(k1+2*k2+2*k3+k4)/6;arr.append(x.copy())
assert np.max(abs(np.array(arr).T-s.y))<1e-10
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(1,2,figsize=(10.5,4.1),layout='constrained')
ax[0].axhspan(-.015,0,color='#f9e8e6');ax[0].axhline(0,c='black',lw=1)
ax[0].plot(s.t,s.y[0],c='#b7473e',lw=2)
tc=s.t_events[0][0];ax[0].scatter([tc],[0],c='black',zorder=4,s=25)
ax[0].annotate(f'Crosses zero at t = {tc:.5f}',xy=(tc,0),xytext=(.11,.007),arrowprops=dict(arrowstyle='->',color='0.3'),fontsize=9)
ax[0].set(xlabel='Model time',ylabel='Wood activity, $x_1$',xlim=(0,.3),ylim=(-.015,.015),title='Extended model: crosses below zero')
ax[1].semilogy(u.t,u.y[0],c='#24628d',lw=2)
ax[1].set(xlabel='Model time',ylabel='Activity (log scale; all values positive)',xlim=(0,60),title='Simple model: approaches zero from above')
ax[1].text(.04,.09,'All five components coincide.\nAt t = 60: activity is about 4.25 x $10^{-11}$.',transform=ax[1].transAxes,fontsize=9)
fig.savefig(out/'zero_vs_negative_examples.png',dpi=190,bbox_inches='tight')
fig.savefig(out/'zero_vs_negative_examples.svg',bbox_inches='tight')
print('Crossing time',tc)
print('Max RK4 versus DOP853 discrepancy',np.max(abs(np.array(arr).T-s.y)))
print('Saved two XPPAUT setups and a comparison figure.')
