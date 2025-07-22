from pathlib import Path
from tree_sitter import Language, Parser

PY_LANGUAGE = Language("build/my-languages.so", "python")
parser = Parser()
parser.set_language(PY_LANGUAGE)


def parse_functions(file_path: Path) -> list[dict]:
    """
    Returns a list of {name, start_line, docstring_present}
    """
    src = file_path.read_text(encoding="utf-8", errors="ignore")
    tree = parser.parse(bytes(src, "utf8"))
    root = tree.root_node

    results = []
    for node in root.walk():
        if node.type == "function_definition":
            name_node = node.child_by_field_name("name")
            name = src[name_node.start_byte : name_node.end_byte]
            docstring_present = '"""' in src[node.start_byte : node.end_byte].splitlines()[1]
            results.append(
                {
                    "name": name,
                    "start": node.start_point[0] + 1,
                    "docstring": docstring_present,
                    "file": str(file_path),
                }
            )
    return results
