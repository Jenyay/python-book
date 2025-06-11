import numpy as np

x = np.linspace(0.0, 8.0e-9, 200)
y1 = np.sin(2e9 * x) * np.cos(5e9 * x)
y2 = np.sin(3e9 * x) * np.cos(7e9 * x)

np.savetxt("example_26_06.csv", np.column_stack((x, y1, y2)),
           fmt=("%.3e", "%.5f", "%.5f"),
           delimiter=",", encoding="utf-8")

readed_x, readed_y = np.loadtxt("example_26_05.csv", delimiter=",",
                                usecols=(0, 2), unpack=True,
                                encoding="utf-8")

print(readed_x)
print(readed_y)
