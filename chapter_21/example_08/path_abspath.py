import os
import os.path as op

cwd = os.getcwd()
print(f"{cwd=}", end="\n\n")

rel_paths = [
    "example_1.txt",
    op.join("subdir_1", "subdir_2", "example_2.txt"),
    op.join("..", "..", "example_3.txt"),
]

for rel_path in rel_paths:
    abs_path = op.abspath(rel_path)
    print(f"{rel_path=}")
    print(f"{abs_path=}", end="\n\n")
