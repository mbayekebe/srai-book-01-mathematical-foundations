#!/usr/bin/env python3
"""Execute canonical notebook code cells and validate PU-B01-C01 outputs."""
from __future__ import annotations
import json
import os
import sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "M1_N01_mathematical_thinking.ipynb"
sys.path.insert(0, str(ROOT))

def main() -> None:
    os.chdir(ROOT)
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    namespace: dict[str, object] = {"__name__": "__main__"}
    executed = 0
    for index, cell in enumerate(notebook["cells"]):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        try:
            exec(compile(source, f"{NOTEBOOK.name}:cell-{index}", "exec"), namespace)
        except Exception as exc:
            raise RuntimeError(f"Notebook code cell {index} failed") from exc
        executed += 1

    expected = np.array([170.0, 182.5, 195.0])
    np.testing.assert_allclose(namespace["predicted_demand"], expected, atol=1e-12)
    np.testing.assert_allclose(namespace["delta"], [2.5], atol=1e-12)
    assert namespace["SEED"] == 42
    print(f"PASS: {executed} code cells executed; canonical outputs verified; seed=42.")

if __name__ == "__main__":
    main()
