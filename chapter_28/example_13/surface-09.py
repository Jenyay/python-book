import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xgrid, ygrid = np.meshgrid(x, y)
z = np.sinc(xgrid / np.pi) * np.sinc(ygrid / np.pi)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_wireframe(xgrid, ygrid, z,
                  edgecolor="black", linewidth=1.0,
                  rstride=5, cstride=5)

fig.tight_layout()
plt.show()
