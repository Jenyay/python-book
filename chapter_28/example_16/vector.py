import numpy as np
import matplotlib.pyplot as plt

A = np.array([3.0, 1.0])
B = np.array([-1.0, 2.0])
C = A + B

fig, ax = plt.subplots()

ax.quiver(0, 0, A[0], A[1],
          color='r', scale=1, scale_units='xy', angles='xy')
ax.quiver(0, 0, B[0], B[1],
          color='g', scale=1, scale_units='xy', angles='xy')
ax.quiver(0, 0, C[0], C[1],
          color='b', scale=1, scale_units='xy', angles='xy')

ax.text(A[0], A[1], 'A', fontsize=14, color='r')
ax.text(B[0], B[1], 'B', fontsize=14, color='g')
ax.text(C[0], C[1], 'C', fontsize=14, color='b')
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 4)

ax.grid()
fig.tight_layout()
plt.show()
