import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi * 2, np.pi * 2 , 201)
y1 = np.sinc(x)
y2 = np.sinc(x / 2.5)

plt.plot(x, y1, "-k", label="sinc(x)")
plt.plot(x, y2, "--r", label="sinc(x/2.5)")
plt.legend()
plt.show()
