import numpy as np

x = np.linspace(0.0, 8.0e-9, 200)
y = np.sin(2e9 * x) * np.cos(5e9 * x)
np.savetxt("example_26_02.txt", np.column_stack((x, y)))
