import numpy as np

x = np.linspace(0.0, 8.0e-9, 200)
y1 = np.sin(2e9 * x) * np.cos(5e9 * x)
y2 = np.sin(3e9 * x) * np.cos(7e9 * x)

filename = "example_26_08.npy"

np.save(filename, np.column_stack((x, y1, y2)))

data = np.load(filename)
print(data)
