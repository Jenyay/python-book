import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi, np.pi, 300) + np.pi / 3
r = np.abs(np.sinc(1.5 * (theta - np.pi / 3)))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
print(f"{type(ax)=}")

ax.plot(theta, r)
ax.set_rmax(1.0)
ax.set_rticks(np.arange(0, 1.1, 0.2))
ax.set_thetagrids(np.arange(0, 360, 15))
plt.tight_layout()
plt.show()
