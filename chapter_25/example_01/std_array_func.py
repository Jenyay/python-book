import array
import math

x_min = -4.0
x_max = 4.0
count = 21

dx = (x_max - x_min) / (count - 1)
x_all = array.array("d")
y_all = array.array("d")

for n in range(count):
    x = x_min + dx * n
    y = math.sin(x) * math.cos(3 * x + math.pi / 3)
    x_all.append(x)
    y_all.append(y)

print(x_all)
print(y_all)
