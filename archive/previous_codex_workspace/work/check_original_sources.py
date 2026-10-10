"""Check reviewed function definitions extracted verbatim from the supplied sources.

No notebook top-level cells or historical filesystem-writing commands are run.
"""
import ast
import json
import re
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
blocks = json.loads((ROOT / 'work/code_blocks.json').read_text())
rng = np.random.default_rng(20261004)


def dm(t, x, a, k, c, g, h):
    return np.array([a*x[i]-k*x[i]**2+c*x[(i-1)%5]/(1+x[i])
                     -g*x[i]/(1+x[(i+2)%5])-h*x[i]*x[(i-2)%5]
                    for i in range(5)])


def lin(t, x, a, b, c, d, g, h):
    return np.array([a*x[i]-b*x[i]**2+c*x[i]*x[(i-1)%5]
                     -d*x[i]*x[(i-2)%5]-g*x[i]*x[(i+1)%5]
                     -h*x[i]*x[(i+2)%5] for i in range(5)])


def extended(t, x, av, k, c, g, h, gd, b, eps):
    return np.array([
        av[i]*x[i]-k*x[i]**2+c*x[(i-1)%5]/(1+x[i])
        -g*x[i]/(1+x[(i+2)%5])-h*x[i]*x[(i-2)%5]
        -gd*x[(i+1)%5]*x[i]/(1+x[i])-b*x[(i+2)%5]/(1+eps*x[i])
        for i in range(5)])


def complex_step_jac(ref, x, p):
    return np.column_stack([ref(0, x.astype(complex)+1e-25j*np.eye(5)[j], *p).imag/1e-25
                            for j in range(5)])


def load_functions(code, namespace=None):
    ns = {'np': np} if namespace is None else namespace
    tree = ast.parse(code)
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    exec(compile(ast.Module(body=funcs, type_ignores=[]), '<original supplied functions>', 'exec'), ns)
    return ns


helpers = load_functions(blocks[59]['code'])
helper_names = ['mother_of', 'child_of', 'controller_of', 'target_of']
sources = []
for idx in [4,11,16,18,26,33,44,47,49,58,60,61,63,64]:
    sources.append((f'chat block {idx}; fence at line {blocks[idx]["line"]}', blocks[idx]['code']))
nb = json.loads(Path('/Users/carterfeng/Downloads/WuXing_Commented.ipynb').read_text())
for i, cell in enumerate(nb['cells']):
    code = ''.join(cell['source'])
    if cell['cell_type'] == 'code' and any(s in code for s in ['def rhs_', 'def jacobian_', 'def balanced_state_']):
        sources.append((f'WuXing_Commented.ipynb cell {i}', code))

results = []
for name, code in sources:
    ns = {'np':np, **{k:helpers[k] for k in helper_names}}
    ns.update({'P':np.cos(2*np.pi/5), 'Q':np.cos(4*np.pi/5)})
    load_functions(code, ns)
    for label, ref, nparams in [('sat',dm,5),('lin',lin,6)]:
        rhs_name = 'rhs_'+label
        jac_name = next((s for s in ['jac_'+label, 'jacobian_'+label] if s in ns), None)
        eq_name = next((s for s in ['eq_'+label, 'balanced_state_'+label] if s in ns), None)
        if label == 'sat' and 'rhs' in ns: rhs_name = 'rhs'
        scalar_jac = label == 'sat' and jac_name is None and 'jac' in ns
        if scalar_jac: jac_name = 'jac'
        if not any([rhs_name in ns, jac_name, eq_name]): continue
        errs = dict(rhs=0.,jacobian=0.,equilibrium_residual=0.)
        counts = dict(rhs=0,jacobian=0,equilibrium_residual=0)
        for _ in range(100):
            x=rng.uniform(.01,5,5); p=rng.uniform(.1,2.5,nparams)
            if rhs_name in ns:
                errs['rhs']=max(errs['rhs'],float(np.max(np.abs(ns[rhs_name](0,x,*p)-ref(0,x,*p)))))
                counts['rhs']+=1
            if jac_name:
                xx=np.full(5,x[0]) if scalar_jac else x
                arg=x[0] if scalar_jac else x
                errs['jacobian']=max(errs['jacobian'],float(np.max(np.abs(ns[jac_name](arg,*p)-complex_step_jac(ref,xx,p)))))
                counts['jacobian']+=1
            if eq_name:
                eq=ns[eq_name](*p)
                if np.isfinite(eq):
                    xx=np.full(5,eq); residual=np.max(np.abs(ref(0,xx,*p)))
                    scale=max(1., float(np.max(np.abs(xx)))**2*float(np.max(p)))
                    errs['equilibrium_residual']=max(errs['equilibrium_residual'],float(residual/scale))
                    counts['equilibrium_residual']+=1
        results.append(dict(source=name,model=label,maximum_errors=errs,counts=counts))

mode_results=[]
for idx, name in [(60,'closed_form'),(61,'modes')]:
    ns=load_functions(blocks[idx]['code'], {'np':np,'P':np.cos(2*np.pi/5),'Q':np.cos(4*np.pi/5)})
    worst=0.;n=0
    for _ in range(1000):
        p=rng.uniform(.1,2.5,5);eq=ns['eq_sat'](*p)
        if not np.isfinite(eq): continue
        vals=ns[name](*p)
        direct=np.sort(np.linalg.eigvals(complex_step_jac(dm,np.full(5,eq),p)).real)
        worst=max(worst,float(np.max(np.abs(direct-np.sort(vals[[0,1,1,2,2]])))))
        n+=1
    mode_results.append(dict(source_line=blocks[idx]['line'],function=name,count=n,max_error=worst))

ext_ns=load_functions(blocks[59]['code'])
ext_err=0.
for _ in range(100):
    x=rng.uniform(.01,5,5);p=(rng.uniform(.1,3,5),*rng.uniform(.1,2,7))
    ext_err=max(ext_err,float(np.max(np.abs(ext_ns['rhs_full'](0,x,*p)-extended(0,x,*p)))))

record=Path('/Users/carterfeng/Downloads/WuXing_Complete_Chat_Record.md').read_text()
ode_results=[]
for filename in ['wuxing_full.ode','wuxing_no_wu.ode']:
    fragment=record.split(f'### `{filename}`',1)[1].split('```text',1)[1].split('```',1)[0]
    equations=re.findall(r"^x[1-5]'\s*=\s*(.*)$",fragment,re.M)
    assert len(equations)==5
    # The reviewed arithmetic-only expressions contain no calls or attributes.
    parsed=[ast.parse(e.replace('^','**'),mode='eval') for e in equations]
    allowed=(ast.Expression,ast.BinOp,ast.UnaryOp,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.USub,ast.Name,ast.Load,ast.Constant)
    assert all(all(isinstance(n,allowed) for n in ast.walk(t)) for t in parsed)
    compiled=[compile(t,'<supplied XPP equation>','eval') for t in parsed]
    error=0.
    for _ in range(100):
        x=rng.uniform(.01,5,5);p=rng.uniform(.1,2.5,5); b,eps=rng.uniform(.1,1,2)
        ns=dict(zip(['a','k','c','g','h'],p));ns.update(b=b,eps=eps)
        ns.update({f'x{i+1}':float(x[i]) for i in range(5)})
        actual=np.array([eval(e,{'__builtins__':{}},ns) for e in compiled])
        expected=dm(0,x,*p)
        if filename=='wuxing_full.ode': expected-=b*np.roll(x,-2)/(1+eps*x)
        error=max(error,float(np.max(np.abs(actual-expected))))
    ode_results.append(dict(file=filename,count=100,max_error=error))

all_results=dict(scope='Original reviewed function definitions; no full notebook or XPP execution.',
                 function_results=results,mode_results=mode_results,
                 extended_rhs_max_error=ext_err,xpp_equation_results=ode_results)
for row in results:
    assert max(row['maximum_errors'].values()) < 1e-10
assert max(r['max_error'] for r in mode_results+ode_results)<1e-10
assert ext_err<1e-10
(ROOT/'outputs/original_code_crosscheck.json').write_text(json.dumps(all_results,indent=2))
totals={k:sum(r['counts'][k] for r in results) for k in ['rhs','jacobian','equilibrium_residual']}
worst={k:max(r['maximum_errors'][k] for r in results) for k in totals}
print(json.dumps(dict(function_groups=len(results),tests=totals,maximum_errors=worst,
                     modes=mode_results,extended_rhs_error=ext_err,xpp=ode_results),indent=2))
