import numpy as np

xmin = -4.0
xmax = 4.0
count = 21
x = np.linspace(xmin, xmax, count)
y = np.sin(x) * np.cos(3 * x + np.pi / 3)

print(f"{type(x)=}")
print(f"{type(y)=}")
print(x)
print(y)
