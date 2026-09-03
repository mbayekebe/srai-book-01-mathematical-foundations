import ast
import hashlib
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from lesson6_reference import eigenpair_residual, residual_power_iteration

NB=ROOT/'notebooks/M1/M1_N06_eigenvalues_eigenvectors_spectral_intuition_v0.1.0.ipynb'
def cells(): return json.loads(NB.read_text())['cells']
def tagged(tag):
    return ''.join(next(c['source'] for c in cells() if tag in c.get('metadata',{}).get('tags',[])))

class MathematicsTests(unittest.TestCase):
    def test_nonzero_guard(self):
        with self.assertRaises(ValueError): eigenpair_residual(np.eye(2),1,[0,0])
    def test_shape_guard(self):
        with self.assertRaises(ValueError): eigenpair_residual(np.ones((2,3)),1,[1,1,1])
    def test_nonfinite_guard(self):
        with self.assertRaises(ValueError): eigenpair_residual(np.eye(2),np.nan,[1,1])
    def test_scale_invariance(self):
        for s in [1e-200,1,1e200]: self.assertLess(eigenpair_residual(np.diag([3,1]),3,[s,0]),1e-14)
    def test_complex_rotation(self):
        self.assertLess(eigenpair_residual([[0,-1],[1,0]],1j,[1,-1j]),1e-14)
    def test_symmetric(self):
        r=residual_power_iteration([[2,1],[1,2]],[1,.2]);self.assertAlmostEqual(r['value'],3);self.assertLessEqual(r['residual'],1e-10)
    def test_negative_dominant(self):
        r=residual_power_iteration(np.diag([-3,1]),[1,1]);self.assertAlmostEqual(r['value'],-3)
    def test_equal_modulus_refused(self):
        with self.assertRaises(RuntimeError): residual_power_iteration(np.diag([1,-1]),[1,1],max_iter=20)
    def test_iteration_limit(self):
        with self.assertRaises(RuntimeError): residual_power_iteration([[2,1],[1,2]],[1,.2],max_iter=1)
    def test_nondominant_start(self):
        self.assertEqual(residual_power_iteration(np.diag([3,1]),[0,1])['value'],1)
    def test_zero_matrix(self):
        self.assertEqual(residual_power_iteration(np.zeros((2,2)))['residual'],0)
    def test_invalid_initial(self):
        with self.assertRaises(ValueError): residual_power_iteration(np.eye(2),[0,0])
    def test_complex_iteration_refused(self):
        with self.assertRaises(ValueError): residual_power_iteration(np.eye(2,dtype=complex))
    def test_bad_limit(self):
        with self.assertRaises(ValueError): residual_power_iteration(np.eye(2),max_iter=0)
    def test_power_answer(self):
        self.assertTrue(np.allclose(np.linalg.matrix_power([[2,1],[1,2]],10),[[29525,29524],[29524,29525]]))
    def test_jordan_boundary(self):
        self.assertTrue(np.allclose(np.linalg.matrix_power([[1,1],[0,1]],10),[[1,10],[0,1]]))
    def test_covariance(self):
        x=np.array([[2,1],[3,2],[4,2.5],[5,4.]])
        self.assertTrue(np.allclose(np.linalg.eigvalsh(np.cov(x,rowvar=False)),[.03039360,3.19877307],atol=1e-8))
    def test_sector(self):
        m=np.array([[.7,.1,.2,.15],[.1,.8,.25,.1],[.25,.1,.75,.3],[.2,.15,.35,.7]])
        r=residual_power_iteration(m)
        self.assertAlmostEqual(r['value'],1.3114820544971353,places=8)
        self.assertTrue(np.allclose(r['vector']/r['vector'].sum(),[.20024812,.23284988,.28255681,.28434520]))

class NotebookControls(unittest.TestCase):
    def test_reference_matches_notebook(self):
        source=(ROOT/'tools/lesson6_reference.py').read_text().split('\n',1)[1].strip()
        self.assertEqual(source,tagged('lesson6-reference-functions').strip())
    def test_markdown(self):
        from validate_srai_notebook_markup import audit
        self.assertEqual(audit(NB)['errors'],[])
    def test_wheel_constant(self):
        tree=ast.parse(tagged('runtime-bootstrap'))
        constants={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['WHEEL_NAME','WHEEL_SHA256']}
        actual=hashlib.sha256((ROOT/'wheels'/constants['WHEEL_NAME']).read_bytes()).hexdigest()
        self.assertEqual(actual,constants['WHEEL_SHA256'])
    def bootstrap_scope(self):
        tree=ast.parse(tagged('runtime-bootstrap'))
        tree.body=[n for n in tree.body if not (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='_SRAI_PUBLIC_TARGET' for t in n.targets))]
        scope={};exec(compile(tree,'bootstrap','exec'),scope);return scope
    def test_bad_local_hash_stops_before_install(self):
        s=self.bootstrap_scope()
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'wheels').mkdir();(p/'wheels'/s['WHEEL_NAME']).write_bytes(b'wrong')
            with patch.object(Path,'cwd',return_value=p),patch('subprocess.check_call') as install:
                with self.assertRaisesRegex(RuntimeError,'checksum mismatch'):s['ensure_srai_runtime']()
                install.assert_not_called()
    def test_network_failure_stops_before_install(self):
        s=self.bootstrap_scope()
        with tempfile.TemporaryDirectory() as d:
            with patch.object(Path,'cwd',return_value=Path(d)),patch('urllib.request.urlopen',side_effect=OSError('offline')),patch('subprocess.check_call') as install:
                with self.assertRaisesRegex(RuntimeError,'download unavailable'):s['ensure_srai_runtime']()
                install.assert_not_called()
    def test_public_bytes_verified_before_install(self):
        import io
        s=self.bootstrap_scope()
        class Response(io.BytesIO):
            def geturl(self):return 'https://example.invalid/test-wheel'
        with tempfile.TemporaryDirectory() as d:
            with patch.object(Path,'cwd',return_value=Path(d)),patch('urllib.request.urlopen',return_value=Response(b'corrupt')),patch('subprocess.check_call') as install:
                with self.assertRaisesRegex(RuntimeError,'checksum mismatch'):s['ensure_srai_runtime']()
                install.assert_not_called()
    def test_valid_bundled_runtime_and_repeat(self):
        bootstrap=tagged('runtime-bootstrap')
        script=bootstrap+'\n'+bootstrap+'\nimport srai_math\nassert srai_math.__version__=="1.1.1rc1"\n'
        run=subprocess.run([sys.executable,'-c',script],cwd=NB.parent,capture_output=True,text=True)
        self.assertEqual(run.returncode,0,run.stderr)
        self.assertEqual(run.stdout.count('local wheel'),2)
    def test_valid_public_response_simulation(self):
        # Simulates transport using bundled bytes: NOT live network verification.
        bootstrap=tagged('runtime-bootstrap')
        wheel=ROOT/'wheels/srai_math-1.1.1rc1-py3-none-any.whl'
        script='import io\nfrom unittest.mock import patch\nfrom pathlib import Path\n'
        script+='class Response(io.BytesIO):\n    def geturl(self): return "https://example.invalid/verified-test-wheel"\n'
        script+=f'payload=Path({str(wheel)!r}).read_bytes()\n'
        script+='with patch("urllib.request.urlopen",return_value=Response(payload)):\n'
        script+='    exec('+repr(bootstrap)+')\n'
        script+='import srai_math\nassert srai_math.__version__=="1.1.1rc1"\n'
        with tempfile.TemporaryDirectory() as d:
            run=subprocess.run([sys.executable,'-c',script],cwd=d,capture_output=True,text=True)
        self.assertEqual(run.returncode,0,run.stderr)
        self.assertIn('public download',run.stdout)

if __name__=='__main__':unittest.main()
