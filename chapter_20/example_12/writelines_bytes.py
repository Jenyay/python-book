foo = 1025
bar = -1025

foo_bytes = foo.to_bytes(4, "big")
bar_bytes = bar.to_bytes(4, "big", signed=True)

data = [b"\x50\x4b\x03\x04", b"hello",
        foo_bytes, bar_bytes]

with open("example.dat", "wb") as file:
    file.writelines(data)
