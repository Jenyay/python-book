foo = 1025
bar = -1025
with open("example.dat", "wb") as file:
    file.write(b"\x50\x4b\x03\x04")
    file.write(b"hello")

    foo_bytes = foo.to_bytes(4, "big")
    bar_bytes = bar.to_bytes(4, "big", signed=True)
    file.write(foo_bytes)
    file.write(bar_bytes)
