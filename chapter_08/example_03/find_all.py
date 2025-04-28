foo = """Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet."""

# Искомая строка
sub = "ipsum"

result = []

pos = foo.find(sub)
while pos != -1:
    result.append(pos)
    pos = foo.find(sub, pos + 1)

print("result:", result)
