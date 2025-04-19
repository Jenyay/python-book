from math import sqrt

x = [0.0, 1.0, 2.0]
y = [0.0, -2.0, 1.5, 2.5]
z = [0.0, 2.0, -3.0, -1.5]

for x_val, y_val, z_val in zip(x, y, z, strict=True):
    dist = sqrt(x_val**2 + y_val**2 + z_val**2)
    print("(", x_val, ", ", 
          y_val, ", ", z_val, ") -> ", 
          dist, sep="")
