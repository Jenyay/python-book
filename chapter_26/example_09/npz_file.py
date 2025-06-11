import numpy as np

x = np.linspace(0.0, 8.0e-9, 200)
y1 = np.sin(2e9 * x) * np.cos(5e9 * x)
y2 = np.sin(3e9 * x) * np.cos(7e9 * x)

filename = "example_26_09.npz"
np.savez(filename, x=x, y1=y1, y2=y2)
with np.load(filename) as data:
    print(type(data))
    x = data["x"]
    y1 = data["y1"]
    y2 = data["y2"]
