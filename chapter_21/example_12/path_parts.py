from pathlib import Path

foo = Path(__file__)
print(f"{foo=}", end="\n\n")

print(f"{foo.parts=}", end="\n\n")
print(f"{list(foo.parents)=}")
