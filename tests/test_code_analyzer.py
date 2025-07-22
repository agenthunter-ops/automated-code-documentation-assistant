from pathlib import Path
from src.agents.code_analyzer import parse_functions

def test_parse_functions():
    file_path = Path(__file__).parent / "sample.py"
    file_path.write_text("def foo():\\n    pass\\n")
    results = parse_functions(file_path)
    assert results[0]["name"] == "foo"
