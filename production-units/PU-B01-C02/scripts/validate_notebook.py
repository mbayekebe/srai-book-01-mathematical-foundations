import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
nb = json.loads((ROOT / "notebooks" / "M1_N02_sets_logic_relations_functions.ipynb").read_text(encoding="utf-8"))
namespace = {"__name__": "__main__"}
os.chdir(ROOT)
for index, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        try:
            exec(compile("".join(cell["source"]), f"cell-{index}", "exec"), namespace)
        except Exception as exc:
            raise RuntimeError(f"Notebook failed in code cell {index}: {exc}") from exc
print("PASS: all notebook code cells executed in order.")
