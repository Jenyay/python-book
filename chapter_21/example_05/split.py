import os.path as op

print(f"{__file__=}", end="\n\n")

splitted_1 = op.split(__file__)
print(f"{splitted_1=}", end="\n\n")

splitted_2 = op.split(splitted_1[0])
print(f"{splitted_2=}", end="\n\n")
