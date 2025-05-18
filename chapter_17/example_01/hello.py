import numpy as np

print(f"NumPy version: {np.__version__}")
x = np.linspace(0, np.pi * 3, 100)
y = np.sin(x) * np.sin(3 * x)
print(y)
