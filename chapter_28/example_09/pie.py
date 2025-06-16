import matplotlib.pyplot as plt

visitors = [2_248, 34_260, 22_569, 9_778, 5_162, 3_373]
labels = ["<18", "18-24", "25-34", "35-44", "45-54", "55+"]

plt.pie(visitors, labels=labels)
plt.tight_layout()
plt.show()
