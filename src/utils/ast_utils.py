from pathlib import Path
from src.agents.code_analyzer import parse_functions

def get_missing_docstrings(path: Path) -> list[dict]:
    missing = []
    for py_file in path.rglob("*.py"):
        for fn in parse_functions(py_file):
            if not fn["docstring"]:
                missing.append(fn)
    return missing
