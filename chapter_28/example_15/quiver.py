import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 21)
y = np.linspace(-5, 5, 21)
xgrid, ygrid = np.meshgrid(x, y)

r2 = xgrid**2 + ygrid**2

u = np.exp(-r2 / 3) * xgrid
v = np.exp(-r2 / 10) * ygrid

fig, ax = plt.subplots()

ax.quiver(xgrid, ygrid, u, v)
ax.grid()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xticks(np.arange(-5, 6, 1))
ax.set_yticks(np.arange(-5, 6, 1))

fig.tight_layout()
plt.show()
