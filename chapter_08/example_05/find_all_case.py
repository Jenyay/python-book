foo = """Lorem ipsum dolor sit amet,
Lorem IPSUM dolor sit amet,
Lorem IpSuM dolor sit amet."""

# Искомая строка
sub = "Ipsum"

# Приводим обе строки к нижнему регистру
foo_lower = foo.lower()
sub_lower = sub.lower()

result = []
pos = -1

while (pos := foo_lower.find(sub_lower, pos + 1)) != -1:
    result.append(pos)

print("result:", result)
