foo = """Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet."""

# Искомая строка
sub = "ipsum"

result = []
pos = -1

while (pos := foo.find(sub, pos + 1)) != -1:
    result.append(pos)
    
print("result:", result)
