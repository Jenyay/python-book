import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi * 2, np.pi * 2 , 201)
y1 = np.sinc(x)
y2 = np.sinc(x / 2.5)
y3 = np.sin(x) * np.cos(x * 2)

plt.subplot(2, 2, 1)
plt.plot(x, y1, "-k")

plt.subplot(2, 2, 2)
plt.plot(x, y2, "--b")

plt.subplot(2, 1, 2)
plt.plot(x, y3, "-r")
plt.show()
