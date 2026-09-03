"""Check bounded file inventory and markup; does not grant release approval."""
from pathlib import Path
import hashlib,json
from validate_srai_notebook_markup import audit
root=Path(__file__).resolve().parents[1]
errors=[];count=0
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
    expected,relative=line.split('  ',1)
    path=(root/relative).resolve()
    if not path.is_relative_to(root): raise SystemExit('Unsafe inventory path')
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:errors.append(relative)
    count+=1
nb=root/'notebooks/M1/M1_N06_eigenvalues_eigenvectors_spectral_intuition_v0.1.0.ipynb'
errors.extend(audit(nb)['errors'])
print(json.dumps({'status':'FAIL' if errors else 'PASS','files_verified':count,'errors':errors,'release_ready':False},indent=2))
raise SystemExit(bool(errors))
