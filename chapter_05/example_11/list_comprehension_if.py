from math import sqrt

foo = [25, 100, 4, 0, -9, 36]
bar = [sqrt(x) for x in foo if x >= 0]
print("bar: ", bar)
print("type(bar)", type(bar))
