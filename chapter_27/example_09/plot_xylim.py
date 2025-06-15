import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi * 2, np.pi * 2 , 201)
y = np.sinc(x)

plt.plot(x, y)
plt.xlim(-4, 4)
plt.ylim(-1, 2)
plt.show()
