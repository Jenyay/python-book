import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xgrid, ygrid = np.meshgrid(x, y)
z = np.sinc(xgrid / np.pi) * np.sinc(ygrid / np.pi)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
print(f"{type(ax)=}")

ax.plot_surface(xgrid, ygrid, z,
                color="white", edgecolor="black", linewidth=0.5,
                rstride=5, cstride=5,
                shade=False)

fig.tight_layout()
plt.show()
