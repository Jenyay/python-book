from math import sqrt

items = [25, 100, 4, 0, -9, 36]
result = []
for x in items:
    if x < 0:
        continue
    result.append(sqrt(x))
print("result:", result)
