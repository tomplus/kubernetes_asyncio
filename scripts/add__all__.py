import sys
import ast

filepath = sys.argv[1]

with open(filepath, "r") as f:
    content = f.read()

tree = ast.parse(content)

if "__all__" in content:
    raise Exception("__all__ already exists")

imports = []

for node in ast.walk(tree):
    if isinstance(node, ast.ImportFrom):
        if node.module != "__future__":
            for alias in node.names:
                imports.append(alias.name)

all_section = "\n__all__ = [\n"
for imp in imports:
    all_section += f'    "{imp}",\n'
all_section += "]\n"

with open(filepath, "a") as f:
    f.write(all_section)
