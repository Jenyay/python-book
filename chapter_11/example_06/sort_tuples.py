foo = [(10, 10), (0, -2), (2, -3), (15, 12), (15, 0)]
foo_sorted = sorted(foo, key=lambda item: item[1])
print(f"{foo=}")
print(f"{foo_sorted=}")
