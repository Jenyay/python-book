import os
import os.path as op

dir_full = op.join("examples", "data", "example_001")
os.makedirs(dir_full, exist_ok=True)
assert op.isdir(dir_full)
