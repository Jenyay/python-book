import numpy as np
import matplotlib.pyplot as plt

A = np.array([3.0, 1.0])
B = np.array([-1.0, 2.0])
C = A + B

fig, ax = plt.subplots()

ax.arrow(0, 0, A[0], A[1],
         head_width=0.1, head_length=0.2, length_includes_head=True,
         color='r', linewidth=2)

ax.arrow(0, 0, B[0], B[1],
         head_width=0.1, head_length=0.2, length_includes_head=True,
         color='g', linewidth=2)

ax.arrow(0, 0, C[0], C[1],
         head_width=0.1, head_length=0.2, length_includes_head=True,
         color='b', linewidth=2)

ax.text(A[0], A[1], 'A', fontsize=14, color='r')
ax.text(B[0], B[1], 'B', fontsize=14, color='g')
ax.text(C[0], C[1], 'C', fontsize=14, color='b')
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 4)

ax.grid()
fig.tight_layout()
plt.show()
