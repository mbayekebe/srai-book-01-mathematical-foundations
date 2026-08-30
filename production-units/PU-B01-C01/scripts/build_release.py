#!/usr/bin/env python3
"""Validate repository structure, write controls, and build the release ZIP."""
from __future__ import annotations
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZIP_PATH = ROOT.parent / "PU-B01-C01_GitHub_Repository_v1.0.1.zip"
REQUIRED = [
    "README.md", "requirements.txt", "requirements-colab.txt",
    "pyproject.toml", "COLAB_SETUP.md", "CITATION.cff",
    "RIGHTS_AND_REUSE.md",
    "RELEASE_RECORD.md",
    "notebooks/M1_N01_mathematical_thinking.ipynb",
    "srai_math/__init__.py", "srai_math/utils/__init__.py",
    "srai_math/utils/reproducibility.py", "scripts/validate_notebook.py",
    "docs/SRAI_Book1_Chapter1_Audited_Controlled_Edition_v1.0.pdf",
    "docs/PU-B01-C01_Executive_Brief_v1.1.pdf",
    "docs/PU-B01-C01_Educational_Exercises_and_Solutions_v1.0.pdf",
]

def digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024*1024), b""): h.update(chunk)
    return h.hexdigest()

def files_for_controls():
    excluded={"SHA256SUMS.txt","MANIFEST.txt"}
    return sorted((p for p in ROOT.rglob("*") if p.is_file() and p.relative_to(ROOT).as_posix() not in excluded and ".venv" not in p.parts and ".git" not in p.parts and "__pycache__" not in p.parts and p.suffix != ".pyc"), key=lambda p: p.relative_to(ROOT).as_posix())

def main():
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    if missing: raise SystemExit(f"Missing required files: {missing}")

    readme=(ROOT/"README.md").read_text(encoding="utf-8")
    links=re.findall(r"\[[^\]]+\]\(([^)]+)\)",readme)
    broken=[]
    for link in links:
        target=link.split("#",1)[0]
        if not target or re.match(r"^[a-z]+://",target): continue
        if not (ROOT/target).exists(): broken.append(link)
    if broken: raise SystemExit(f"Broken relative README links: {broken}")

    result=subprocess.run([sys.executable,str(ROOT/"scripts/validate_notebook.py")],cwd=ROOT,text=True,capture_output=True)
    if result.returncode: raise SystemExit(result.stdout+result.stderr)

    report={
        "production_unit":"PU-B01-C01","release":"1.0.1","status":"PASS",
        "required_files":len(REQUIRED),"relative_readme_links_checked":len(links),
        "notebook_validation":result.stdout.strip(),
        "expected_predictions":[170.0,182.5,195.0],"expected_sensitivity":[2.5],"seed":42,
        "owner_approval":{"status":"PASS","confirmed_date":"2026-08-30","scope":"metadata and packaging repair v1.0.1"},
        "publication_status":"APPROVED FINAL CONTROLLED RELEASE",
    }
    (ROOT/"VALIDATION_REPORT.json").write_bytes((json.dumps(report,indent=2)+"\n").encode("utf-8"))

    files=files_for_controls()
    manifest="\n".join(p.relative_to(ROOT).as_posix() for p in files)+"\n"
    (ROOT/"MANIFEST.txt").write_bytes(manifest.encode("utf-8"))
    checksum_files=files+[ROOT/"MANIFEST.txt"]
    checks="\n".join(f"{digest(p)}  {p.relative_to(ROOT).as_posix()}" for p in checksum_files)+"\n"
    (ROOT/"SHA256SUMS.txt").write_bytes(checks.encode("utf-8"))

    all_files = sorted((p for p in ROOT.rglob("*") if p.is_file() and ".venv" not in p.parts and ".git" not in p.parts and "__pycache__" not in p.parts and p.suffix != ".pyc"), key=lambda p: p.relative_to(ROOT.parent).as_posix())
    with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as zf:
        for p in all_files: zf.write(p,p.relative_to(ROOT.parent))
    print(json.dumps({"status":"PASS","files":len(all_files),"zip":str(ZIP_PATH),"zip_sha256":digest(ZIP_PATH)}))

if __name__=="__main__": main()
