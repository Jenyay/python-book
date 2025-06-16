import matplotlib.pyplot as plt

visitors = [2_248, 34_260, 22_569, 9_778, 5_162, 3_373]
labels = ["<18", "18-24", "25-34", "35-44", "45-54", "55+"]
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0",
"#ffb3e6"]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.pie(visitors, labels=labels, startangle=90, counterclock=False,
       autopct="%.1f%%", pctdistance=0.85,
       explode=(0, 0, 0, 0, 0, 0.2),
       colors=colors,
       wedgeprops = {"edgecolor": "black", "linewidth": 1})

fig.tight_layout()
plt.show()
