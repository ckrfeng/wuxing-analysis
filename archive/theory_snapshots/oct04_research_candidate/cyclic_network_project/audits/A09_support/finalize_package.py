"""Package only A09 artifacts and verify that all authenticated input bytes remain intact.

Run from the original research workspace after compiling the A09 PDF and
rendering/reviewing it. No original project file is written by this script.
"""
from pathlib import Path
from hashlib import sha256
import json, shutil, zipfile
from pypdf import PdfReader

def h(p): return sha256(p.read_bytes()).hexdigest()
def write(p,obj): p.write_text(json.dumps(obj,indent=2)+'\n')

ws=Path.cwd()
base=ws/'output/a09'; root=base/'cyclic_network_project'; audit=root/'audits'
support=audit/'A09_support'; build=base/'build'
source=audit/'A09_transcritical_bifurcation.tex'
pdf=audit/'A09_transcritical_bifurcation.pdf'
input_root=ws/'output/p09/cyclic_network_project'
inventory=json.loads((support/'input_inventory.json').read_text())
members=json.loads((support/'archive_member_hashes.json').read_text())
for name,digest in members.items():
    assert h(input_root.parent/name)==digest, f'Changed input: {name}'
assert h(ws/'cyclic_network_project_P09_draft.zip')==inventory['archive_sha256']
assert h(ws/'output/p09/cyclic_network_project_P09_draft.zip')==inventory['archive_sha256']
assert (input_root/'proofs/P09_transcritical_bifurcation.tex').read_text().startswith('% STATUS: DRAFT')
assert h(ws/'output/p09/P09_validation_support.zip')=='2752687d50610d4f6caea5803fa9436355aea45dbeb499ca6c4ed4093d6b362d'

log=(build/'A09_transcritical_bifurcation.log').read_text()
issues=[s for s in log.splitlines() if any(t in s for t in ['Overfull','Underfull','Warning','undefined']) or s.startswith('!')]
assert not issues,issues
shutil.copyfile(build/pdf.name,pdf)
reader=PdfReader(pdf); assert len(reader.pages)==17
text='\n'.join(p.extract_text() for p in reader.pages)
for token in ['VERIFIED','539','310','2,370','1,580','Closure handoff','cyclic_network_project_P09_audited.zip']:
    assert token in text,token
line_review=json.loads((support/'line_review.json').read_text())
coverage=[j for r in line_review['ranges'] for j in range(r['start'],r['end']+1)]
assert coverage==list(range(1,540))
assert all(r['verdict']=='PASS' for r in line_review['ranges'])
summary=json.loads((support/'checks/summary.json').read_text())
reproduction=json.loads((support/'prior_validation/reproduction_comparison.json').read_text())
assert reproduction['all_byte_identical']
provenance={
 'audit_date':'2026-10-03',
 'analytical_evidence':'Standalone A09 source, six separate verdicts and complete source-line ledger',
 'independent_script_sha256':h(support/'independent_checks.py'),
 'independent_summary':summary,
 'independence':'Initial independent checker authored before developer checker was read; no developer code/results imported. Subsequent series-division clarification is disclosed in README.',
 'developer_companion_authenticated_against_its_zip':True,
 'developer_reproduction':reproduction,
 'limitations':'All numerical checks are ordinary floating point, not interval certificates. No finite search or developer validation is treated as proof. Prior A04/A05 provenance notes remain unchanged.'}
write(support/'validation_provenance.json',provenance)

(support/'build').mkdir(exist_ok=True)
for name in ['A09_transcritical_bifurcation.log','build_console.txt']:
    shutil.copyfile(build/name,support/'build'/name)
render_dir=ws/'tmp/pdfs/a09'
old=json.loads((render_dir/'pre_final_render_hashes.json').read_text())
new={p.name:h(p) for p in sorted(render_dir.glob('page-*.png'))}
changed=[name for name in new if old[name]!=new[name]]
assert changed==['page-09.png','page-10.png'],changed
qa={'pages':17,'native_editor_compile':'success, final source','pdf_export':'Existing local latexmk/pdfLaTeX; no software installed','final_log_diagnostics':issues,'visual_review':'All 17 pages reviewed in contact sheets; final pages 9 and 10 inspected separately at full render size. All other final page images byte-identical to inspected renders. No clipping, overlap, missing formulas or unreadable tables found.','final_render_sha256':new,'final_changed_pages_reinspected':changed,'source_sha256':h(source),'pdf_sha256':h(pdf)}
write(support/'build/verification.json',qa)

delivery={'audited_p09':inventory['p09'],'input_archive_sha256':inventory['archive_sha256'],'all_143_original_members_unchanged':True,'both_draft_zip_copies_unchanged':True,'original_validation_companion_unchanged':True,'all_26_requested_and_additional_inputs_authenticated':len(inventory['inventory'])==26,'complete_line_coverage':True,'line_review_ranges':len(line_review['ranges']),'all_six_layers':'VERIFIED','overall':'VERIFIED','required_corrections':[],'p09_lifecycle_in_input':'DRAFT, unchanged','p10_started':False,'p10_gate':'Cleared after original development chat administrative audit closure','no_replacement_proof_source':True,'pdf_pages':17,'pdf_visual_review':'PASS','native_editor_compile':'success','required_archive':'cyclic_network_project_A09_audit_only.zip','complete_p09_archive_created_here':False}
write(support/'delivery_checks.json',delivery)

hashfile=support/'artifact_hashes.json'
artifacts={str(p.relative_to(root)):h(p) for p in sorted(root.rglob('*')) if p.is_file() and p!=hashfile}
write(hashfile,{'scope':'Every packaged artifact except this self-describing hash file','sha256':artifacts})
archive=ws/'cyclic_network_project_A09_audit_only.zip'
files=sorted(p for p in root.rglob('*') if p.is_file())
for p in files:
    assert p.is_relative_to(audit)
    assert not p.name.startswith('P09_')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        name=str(p.relative_to(root.parent))
        info=zipfile.ZipInfo(name,date_time=(2026,10,3,12,0,0)); info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=0o100644<<16; z.writestr(info,p.read_bytes())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(files)
    assert all(n.startswith('cyclic_network_project/audits/') for n in z.namelist())
    assert all(z.read(str(p.relative_to(root.parent)))==p.read_bytes() for p in files)
    names=z.namelist()
verification={'archive':str(archive),'sha256':h(archive),'bytes':archive.stat().st_size,'members':len(files),'CRC':'PASS','all_member_bytes_match':'PASS','single_canonical_root':'PASS','only_a09_artifacts':'PASS','members_inventory':names,'source_sha256':h(source),'pdf_sha256':h(pdf)}
write(base/'package_verification.json',verification)
print(json.dumps({k:v for k,v in verification.items() if k!='members_inventory'},indent=2))
