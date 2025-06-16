import numpy as np
import matplotlib.pyplot as plt

dates = ["Янв.", "Фев.", "Март", "Апр.", "Май", "Июнь", 
         "Июль", "Авг.", "Сент.", "Окт.", "Нояб.", "Дек."]
visitors = [10_748, 12_610, 15_245, 14_468, 14_897, 10_441,
            8_904, 9_301, 11_272, 14_083, 12_788, 11_748]
search = [8_649, 10_431, 12_751, 12_375, 12_464, 8_610,
          7_113, 6_652, 9_193, 11_689, 9_936, 9_497]

width = 0.3
positions = np.arange(1, len(dates) + 1)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(positions - width / 2, visitors, linewidth=1.0, edgecolor="k",
        width=width)

ax.bar(positions + width / 2, search, linewidth=1.0, edgecolor="k", 
        width=width)

ax.set_xticks(positions, dates, rotation=45)

ax.grid()
fig.tight_layout()
plt.show()
