import matplotlib.pyplot as plt

y = [0, 1, 2, 4, 5, 8]
height = [0.1, 0.2, 0.4, 0.8, 0.6, 0.1]

plt.barh(y, height)
plt.tight_layout()
plt.show()
