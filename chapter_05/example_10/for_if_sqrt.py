from math import sqrt

foo = [25, 100, 4, 0, -9, 36]
bar = []
for x in foo:
    if x >= 0:
        bar.append(sqrt(x))
print("bar:", bar)
