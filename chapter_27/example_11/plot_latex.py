import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi / 2, np.pi / 2 , 201)
f = np.abs(np.sinc(theta * 5))

plt.plot(np.rad2deg(theta), f)
plt.xlabel(r"$\theta, \degree$")
plt.ylabel(r"$f(\theta)$")
plt.text(40, 0.9, 
    r"$f(\theta) = \left|\frac{sin(5\pi\theta)}{5\pi\theta}\right|$",
    fontsize=15)
plt.xlim(-90, 90)
plt.ylim(0, 1.1)
plt.grid()
plt.tight_layout()
plt.show()
