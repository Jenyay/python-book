from pathlib import Path

foo = Path(__file__)
print(f"{foo=}")
print(f"{foo.exists()=}")
print(f"{foo.is_file()=}")
print(f"{foo.is_dir()=}")

print()
bar = Path("path_methods.py")
print(f"{bar=}")
print(f"{bar.absolute()=}")
print(f"{foo.samefile(bar)=}")

print()
spam = Path("examples", "images", "42.png")
print(f"{spam=}")
print(f"{spam.absolute()=}")
