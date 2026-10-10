from pathlib import Path
import hashlib,json,zipfile,re,csv
root=Path('cyclic_network_project'); out=root/'audits/A11_support'
sha=lambda b:hashlib.sha256(b).hexdigest()
manifest=(root/'project_manifest.md').read_text()
controls=['project_manifest.md','claim_registry.md','frozen_theorem_package.md','final_novelty_verdict.md','novelty_decisions.md','open_decisions.md','02_theorem_dependency_map.tex','proofs_compendium.tex','shared_macros.tex','00_canonical_model.tex','01_notation_and_assumptions.tex']
files=[root/f for f in controls]
for tag in ['01','02','03','04','05','07','08','09','10']:
 files.extend([next((root/'proofs').glob('P'+tag+'_*.tex')),next((root/'audits').glob('A'+tag+'_*.tex'))])
files += [root/'proofs/P11_hopf_spectral_conditions.tex',root/'PROPOSED_P11_scope_clarification.md']
records=[]
for p in files:
 b=p.read_bytes(); row={'path':str(p.relative_to(root)),'bytes':len(b),'lines':len(b.splitlines()),'sha256':sha(b)}
 if p.parent.name=='proofs':
  assert row['sha256'] in manifest
  body=b[re.search(rb'^\\section',b,re.M).start():];row['body_sha256']=sha(body)
  row['current_full_hash_in_manifest']=True
 records.append(row)
(out/'input_inventory.json').write_text(json.dumps(records,indent=2)+'\n')
with (out/'input_inventory.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['path','bytes','lines','sha256','body_sha256','current_full_hash_in_manifest']);w.writeheader();w.writerows(records)
archives=[]
for name in ['cyclic_network_project_P11_draft.zip','output/p11/cyclic_network_project_P11_draft.zip','output/p10/cyclic_network_project_P10_audited.zip','output/p11/P11_validation_support.zip']:
 p=Path(name)
 with zipfile.ZipFile(p) as z:
  assert z.testzip() is None
  members=[{'path':n,'bytes':len(z.read(n)),'sha256':sha(z.read(n))} for n in z.namelist() if not n.endswith('/')]
  changes=None
  if 'validation' not in name:
   changes=[m['path'] for m in members if sha(Path(m['path']).read_bytes())!=m['sha256']]
  archives.append({'path':name,'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'members':len(members),'crc':'PASS','working_file_differences':changes})
  if name=='cyclic_network_project_P11_draft.zip':
   assert len(members)==200 and not changes
   (out/'original_project_inventory.json').write_text(json.dumps(members,indent=2)+'\n')
  if 'validation' in name:(out/'developer_validation_inventory.json').write_text(json.dumps(members,indent=2)+'\n')
(out/'archive_authentication.json').write_text(json.dumps(archives,indent=2)+'\n')
(out/'audited_version.txt').write_text('P11 v1.0; 2026-10-03; DRAFT / NOT AUDITED lifecycle preserved\nproofs/P11_hopf_spectral_conditions.tex\n25914 bytes; 600 source lines\nSHA-256: 4be8e9b1e64c022b635f3cca9f7f49ffbc5358a2250dda1715cb60e82d9b073b\nManifest CURRENT entry; all 200 draft archive members match working files.\nA11 audit date: 2026-10-04 America/Chicago\n')
print(json.dumps(archives,indent=2)); print('Authenticated inputs:',len(records))
