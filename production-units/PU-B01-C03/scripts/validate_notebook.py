"""Validate the canonical M1_N03 notebook from a clean namespace."""

import ast
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "M1_N03_vector_foundations.ipynb"
sys.path.insert(0, str(ROOT))

document = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
namespace = {"__name__": "__main__"}
code_cells = 0

os.chdir(ROOT)
for index, cell in enumerate(document["cells"]):
    if cell.get("cell_type") != "code":
        continue
    code_cells += 1
    source = "".join(cell.get("source", []))
    try:
        tree = ast.parse(source, filename=f"cell-{index}", mode="exec")
        exec(compile(tree, f"cell-{index}", "exec"), namespace)
    except Exception as exc:
        raise RuntimeError(f"Notebook failed in code cell {index}: {exc}") from exc

if code_cells != 22:
    raise RuntimeError(f"Expected 22 code cells; found {code_cells}.")

markdown = "\n".join(
    "".join(cell.get("source", []))
    for cell in document["cells"]
    if cell.get("cell_type") == "markdown"
)
for obsolete in (r"\[", r"\]", r"\(", r"\)"):
    if obsolete in markdown:
        raise RuntimeError(f"Obsolete math delimiter remains: {obsolete}")

print(f"PASS: executed {code_cells} notebook code cells in order.")
print("PASS: portable notebook math delimiters verified.")
