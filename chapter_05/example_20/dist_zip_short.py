from math import sqrt

x = [0.0, 1.0, 2.0]
y = [0.0, -2.0, 1.5, 2.5]
z = [0.0, 2.0, -3.0, -1.5]

dist = []
for n in range(min(len(x), len(y), len(z))):
    dist.append(sqrt(x[n]**2 + y[n]**2 + z[n]**2))
print("Расстояния: ", dist)
