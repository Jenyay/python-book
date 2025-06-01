import os.path as op

print(f"{__file__=}", end="\n\n")

dirname = op.dirname(__file__)
basename = op.basename(__file__)

print(f"{dirname=}", end="\n\n")
print(f"{basename=}", end="\n\n")
