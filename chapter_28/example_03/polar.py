import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi, np.pi, 300) + np.pi / 3
r = np.abs(np.sinc(1.5 * (theta - np.pi / 3)))

plt.polar(theta, r)
plt.tight_layout()
plt.show()
