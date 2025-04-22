from math import sqrt

x = [0.0, 1.0, 2.0, -0.5]
y = [0.0, -2.0, 1.5, 2.5]
z = [0.0, 2.0, -3.0, -1.5]

dist = []
for x_val, y_val, z_val in zip(x, y, z):
    dist.append(sqrt(x_val**2 + y_val**2 + z_val**2))
print("Расстояния: ", dist)
