import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xgrid, ygrid = np.meshgrid(x, y)
z = 20 * np.log10(np.abs(np.sinc(xgrid / np.pi) *
                         np.sinc(ygrid / np.pi)))

fig, ax = plt.subplots()
ax.contour(xgrid, ygrid, z)

fig.tight_layout()
plt.show()
