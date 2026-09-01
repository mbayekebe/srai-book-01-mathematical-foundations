"""Read-only checksums, then optional math tests. Never commits or changes approval."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parent
WHEEL = 'srai_math-1.1.1rc1-py3-none-any.whl'
WHEEL_SHA = '6e7033465ad3d9bf4650227a11be0380512a44fd476a83d5828ad4ec4f07e923'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mathematics', action='store_true', help='Requires NumPy; uses bundled wheel without installing it')
    args = ap.parse_args()
    entries = {}
    for line in (ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8-sig').splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        if not m:
            raise RuntimeError('Malformed checksum entry')
        digest, name = m.groups()
        target = (ROOT/name).resolve()
        if name in entries or not target.is_relative_to(ROOT) or not target.is_file():
            raise RuntimeError('Duplicate, unsafe or missing file: '+name)
        if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            raise RuntimeError('Checksum mismatch: '+name)
        entries[name] = digest
    if not entries:
        raise RuntimeError('Empty checksum manifest')
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
              and p.name != 'SHA256SUMS.txt' and '__pycache__' not in p.parts
              and '.pytest_cache' not in p.parts and p.suffix != '.pyc'}
    if actual != set(entries):
        raise RuntimeError('Unlisted or missing files: '+str(sorted(actual ^ set(entries))))
    report = {'status': 'PASS', 'files_verified': len(entries), 'release_ready': False}
    if args.mathematics:
        wheel = ROOT/'wheels'/WHEEL
        if hashlib.sha256(wheel.read_bytes()).hexdigest() != WHEEL_SHA:
            raise RuntimeError('Pinned runtime checksum mismatch')
        if any(n == 'srai_math' or n.startswith('srai_math.') for n in sys.modules):
            raise RuntimeError('Start this verification in a fresh Python process')
        sys.dont_write_bytecode = True
        sys.path.insert(0, str(wheel))
        suite = unittest.defaultTestLoader.discover(str(ROOT/'tests'), pattern='test_*.py')
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if not result.wasSuccessful():
            raise SystemExit(1)
        report['mathematical_tests_passed'] = result.testsRun
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
