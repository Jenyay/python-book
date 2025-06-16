import numpy as np
import matplotlib.pyplot as plt

count = 30
x = np.random.rand(count) * 10
y = np.random.rand(count) * 10
data = np.random.rand(count) * 30

plt.scatter(x, y, s=data * 5 + 1, c=data, marker="o", cmap="jet")
plt.colorbar()
plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel("X")
plt.ylabel("Y", rotation=0)
plt.tight_layout()
plt.show()
