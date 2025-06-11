import numpy as np

x, y = np.loadtxt("example_26_03.txt", usecols=(0, 2), unpack=True,
                  encoding="utf-8")
print(x)
print(y)
