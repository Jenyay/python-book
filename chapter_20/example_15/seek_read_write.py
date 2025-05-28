import os

with open("example.dat", "r+b") as file:
    file.seek(-4, os.SEEK_END)
    file.write((42).to_bytes(4, "big"))

    file.seek(4, os.SEEK_SET)
    hello_bytes = file.read(5)

    file.seek(4, os.SEEK_CUR)
    bar_bytes = file.read(4)

    file.seek(-8, os.SEEK_END)
    foo_bytes = file.read(4)

    file.seek(0, os.SEEK_SET)
    header = file.read(4)

hello = hello_bytes.decode()
foo = int.from_bytes(foo_bytes, signed=True)
bar = int.from_bytes(bar_bytes, signed=True)

print(f"{header=}")
print(f"{hello=}")
print(f"{foo=}")
print(f"{bar=}")
