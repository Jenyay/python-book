foo = """Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet."""

old = "ipsum"
new = "*****"

bar = foo.replace(old, new)
baz = foo.replace(old, new, 1)

print("bar: ", bar, end="\n\n")
print("baz: ", baz)
