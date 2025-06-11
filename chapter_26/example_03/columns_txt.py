import numpy as np

x = np.linspace(0.0, 8.0e-9, 200)
y1 = np.sin(2e9 * x) * np.cos(5e9 * x)
y2 = np.sin(3e9 * x) * np.cos(7e9 * x)

np.savetxt("example_26_03.txt", np.column_stack((x, y1, y2)),
           fmt=("%.3e", "%10.5f", "%10.5f"),
           header="t [с]      U1 [В]     U2 [В]",
           encoding="utf-8")
