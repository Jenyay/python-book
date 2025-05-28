with open("example.dat", "rb") as file:
    header = file.read(4)
    hello_bytes = file.read(5)
    foo_bytes = file.read(4)
    bar_bytes = file.read(4)

hello = hello_bytes.decode()
foo = int.from_bytes(foo_bytes, signed=True)
bar = int.from_bytes(bar_bytes, signed=True)

print(f"{header=}")
print(f"{hello=}")
print(f"{foo=}")
print(f"{bar=}")
