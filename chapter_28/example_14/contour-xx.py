import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xgrid, ygrid = np.meshgrid(x, y)
z = 20 * np.log10(np.abs(np.sinc(xgrid / np.pi) *
                         np.sinc(ygrid / np.pi)))

fig, ax = plt.subplots()
levels = [-50.0, -30.0, -20.0, -13.3, -6.0, -3.0, -0.05]
cs = ax.contour(xgrid, ygrid, z, levels=levels,
                colors='black', linestyles='-', linewidths=0.5)
cs.clabel(colors='black', fmt='%.1f')

fig.tight_layout()
plt.show()
