from pathlib import Path

foo = Path(__file__)
print(f"{foo=}")

print(f"{foo.parent=}")
print(f"{foo.name=}")
print(f"{foo.stem=}")
print(f"{foo.suffix=}")
print(f"{foo.drive=}")
