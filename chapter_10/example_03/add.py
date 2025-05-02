def add(a, b):
    return a + b

foo = add(10, 20)
bar = add(3+2j, 20.5)
baz = add("hello ", "world")
spam = add([10, 20, 30], ["hello", "world"])

print(f"{foo=}\n{bar=}\n{baz=}\n{spam=}")
