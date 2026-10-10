"""Read-only authentication of the exact A09 input; no project mutation."""
from pathlib import Path
import hashlib, json, re, zipfile, argparse

def digest(data): return hashlib.sha256(data).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--workspace', type=Path, required=True)
    ap.add_argument('--out', type=Path, default=Path(__file__).resolve().parent)
    args=ap.parse_args(); ws=args.workspace; out=args.out; out.mkdir(parents=True, exist_ok=True)
    root=ws/'output/p09/cyclic_network_project'
    archive=ws/'cyclic_network_project_P09_draft.zip'
    names=['project_manifest.md','claim_registry.md','frozen_theorem_package.md','final_novelty_verdict.md','novelty_decisions.md','02_theorem_dependency_map.tex','proofs_compendium.tex','shared_macros.tex','00_canonical_model.tex','01_notation_and_assumptions.tex','open_decisions.md']
    for sub,prefix in [('proofs','P'),('audits','A')]:
        for i in [1,2,3,4,5,7,8]:
            found=list((root/sub).glob(f'{prefix}{i:02d}_*.tex')); assert len(found)==1
            names.append(str(found[0].relative_to(root)))
    p09='proofs/P09_transcritical_bifurcation.tex'; names.append(p09)
    inventory={}
    for name in names:
        data=(root/name).read_bytes(); rec={'sha256':digest(data),'bytes':len(data),'lines':len(data.splitlines())}
        if name.startswith('proofs/'):
            start=re.search(rb'^\\section\{',data,re.M).start()
            rec['body_sha256']=digest(data[start:])
            rec['body_start_line']=data[:start].count(b'\n')+1
            if name!=p09: assert rec['body_sha256'].encode() in data[:start], name
        inventory[name]=rec
    manifest=(root/'project_manifest.md').read_text()
    assert '## P09 draft' in manifest and inventory[p09]['sha256'] in manifest
    assert inventory[p09]['sha256']=='b2366edf1ff71199b7f1d02a58cf828148d9a697dfafc9e07e70a523e4f26680'
    members={}
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for i in z.infolist():
            if i.is_dir(): continue
            assert i.filename.startswith('cyclic_network_project/')
            data=z.read(i.filename); assert data==(root.parent/i.filename).read_bytes()
            members[i.filename]=digest(data)
    assert len(members)==143
    assert archive.read_bytes()==(ws/'output/p09/cyclic_network_project_P09_draft.zip').read_bytes()
    # Prior complete audited snapshot is the unchanged prerequisite baseline.
    with zipfile.ZipFile(ws/'cyclic_network_project_P07_audited.zip') as z:
        changed=[]
        for name,h in members.items():
            if digest(z.read(name))!=h: changed.append(name)
        expected=['claim_registry.md','project_manifest.md','proofs_compendium.pdf','proofs_compendium.tex',p09]
        assert sorted(changed)==sorted('cyclic_network_project/'+s for s in expected)
    refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',(root/p09).read_text())
    external=sorted(set(r for r in refs if not ':P09' in r))
    assert all(re.search(r':P0[1-4](?:-|$)',r) for r in external)
    for r in external: assert any(('\\label{'+r+'}') in (root/n).read_text() for n in names if n.startswith('proofs/'))
    result={'selection':'Manifest lines 693-732 CURRENT P09 v1.0 DRAFT','archive':str(archive),'archive_sha256':digest(archive.read_bytes()),'member_count':143,'all_members_match':True,'baseline_only_changed_members':changed,'p09':inventory[p09],'external_proof_references':external,'inventory':inventory}
    (out/'input_inventory.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'archive_member_hashes.json').write_text(json.dumps(members,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['archive_sha256','member_count','all_members_match','external_proof_references','p09']},indent=2))

if __name__=='__main__': main()
