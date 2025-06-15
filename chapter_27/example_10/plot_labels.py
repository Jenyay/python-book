import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 8.0e-9, 200)
y = np.sin(2e9 * x) * np.cos(5e9 * x)

plt.plot(x, y)
plt.xlabel("Время, с", loc="right",
           labelpad=15, color="blue")
plt.ylabel("U, В", loc="top", rotation=0,
           labelpad=-8, color="blue")
plt.xlim(left=0.0)
plt.ylim(-1.0, 1.0)
plt.title("y = sin(2e9 * x) * cos(5e9 * x)", pad=8)
plt.grid()
plt.tight_layout()
plt.show()
