foo = [42, 20, 35, -5, 42, 16, 42, 20, 50, 42]
indexes = []
n = 42
next_index = 0
while n in foo[next_index:]:
    position = foo.index(n, next_index)
    indexes.append(position)
    next_index = position + 1

print(indexes)
