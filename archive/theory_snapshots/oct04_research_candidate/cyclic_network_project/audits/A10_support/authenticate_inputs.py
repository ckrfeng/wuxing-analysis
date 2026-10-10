"""Read-only authentication of supplied P10 inputs; writes audit evidence only."""
from pathlib import Path
from zipfile import ZipFile
import hashlib, json, re, sys
workspace=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
out=Path(__file__).resolve().parent
root=workspace/'output/p10/cyclic_network_project'
sha=lambda b:hashlib.sha256(b).hexdigest()
expected='a28ea2b4ca96f381f06fa82849d4289fcc0e9c41e646ca66595621922f385a07'
slug='proofs/P10_saddle_node_and_bistability.tex'
controls=['project_manifest.md','claim_registry.md','frozen_theorem_package.md','final_novelty_verdict.md','novelty_decisions.md','02_theorem_dependency_map.tex','proofs_compendium.tex','shared_macros.tex','00_canonical_model.tex','01_notation_and_assumptions.tex']
refs=[root/c for c in controls]
for i in [1,2,3,4,5,7,8,9]:
 for d,prefix in [('proofs','P'),('audits','A')]:
  found=list((root/d).glob(f'{prefix}{i:02}_*.tex'));assert len(found)==1;refs+=found
refs+=[root/slug,root/'open_decisions.md']
inv=[]
for p in refs:
 data=p.read_bytes();body=re.search(rb'^\\section\{',data,re.M)
 inv.append(dict(path=p.relative_to(root).as_posix(),sha256=sha(data),bytes=len(data),lines=len(data.splitlines()),body_sha256=sha(data[body.start():]) if body else None))
assert sha((root/slug).read_bytes())==expected
manifest=(root/'project_manifest.md').read_text()
assert expected in manifest[manifest.index('## P10 positive saddle-node'):]
archives={}
for rel in ['cyclic_network_project_P10_draft.zip','output/p10/cyclic_network_project_P10_draft.zip','cyclic_network_project_P09_audited.zip','output/p10/P10_validation_support.zip']:
 archives[rel]=sha((workspace/rel).read_bytes())
assert archives['cyclic_network_project_P10_draft.zip']==archives['output/p10/cyclic_network_project_P10_draft.zip']
assert archives['cyclic_network_project_P09_audited.zip']=='db6344c5ed7c96f244f99eefa589ae8631c3aaf15278577e607e246026b22bf2'
with ZipFile(workspace/'cyclic_network_project_P10_draft.zip') as z, ZipFile(workspace/'cyclic_network_project_P09_audited.zip') as b:
 assert z.testzip() is None and b.testzip() is None
 names=[x for x in z.namelist() if not x.endswith('/')]
 assert len(names)==176 and len(names)==len(set(names))
 assert set(names)=={x for x in b.namelist() if not x.endswith('/')}
 members={x:sha(z.read(x)) for x in names}
 assert all(x.startswith('cyclic_network_project/') for x in names)
 assert all((root/Path(x).relative_to('cyclic_network_project')).read_bytes()==z.read(x) for x in names)
 changed=[x for x in names if z.read(x)!=b.read(x)]
 assert {str(Path(x).relative_to('cyclic_network_project')) for x in changed}=={slug,'project_manifest.md','claim_registry.md','proofs_compendium.tex','proofs_compendium.pdf'}
protected={str(p.relative_to(workspace)):sha(p.read_bytes()) for p in sorted(root.rglob('*')) if p.is_file()}
protected.update({str(p.relative_to(workspace)):sha(p.read_bytes()) for p in sorted((workspace/'sources').rglob('*')) if p.is_file()})
protected.update(archives)
result=dict(status='PASS',proof_version='P10 v1.0',proof_sha256=expected,proof_body_sha256=next(x['body_sha256'] for x in inv if x['path']==slug),draft_member_count=176,working_copy_mismatches=[],changed_from_P09=changed,archives=archives,inputs=inv)
(out/'input_inventory.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'draft_member_hashes.json').write_text(json.dumps(members,indent=2)+'\n')
(out/'protected_before.json').write_text(json.dumps(protected,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='inputs'},indent=2))
