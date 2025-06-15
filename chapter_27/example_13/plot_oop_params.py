import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 8.0e-9, 200)
y1 = np.sin(2e9 * x) * np.cos(5e9 * x)
y2 = np.sin(0.5e9 * x) * np.cos(1e9 * x)

# Создаем окно с графиком
fig = plt.figure()
fig.set_size_inches(9, 7)

# Создаем оси для графика
axes = fig.add_subplot(1, 1, 1)

# Рисуем графики
curve1, curve2 = axes.plot(x, y1, x, y2)

curve1.set_linestyle('-')
curve1.set_color('black')
curve1.set_label("sin(2e9 * x) * cos(5e9 * x)")

curve2.set_linestyle('--')
curve2.set_color('red')
curve2.set_label("sin(0.5e9 * x) * cos(1e9 * x)")

# Настраиваем внешний вид графика
axes.grid()
axes.set_xlim(left=0.0)
axes.set_ylim(-1.0, 1.0)

# Метки около осей
xlabel = axes.set_xlabel('Время, с', loc='right', labelpad=15)
xlabel.set_color('blue')

ylabel = axes.set_ylabel('U, В', loc='top', labelpad=-6)
ylabel.set_color('blue')
ylabel.set_rotation(0)

# Настраиваем заголовок графика
title = axes.set_title("y = sin(2e9 * x) * cos(5e9 * x)", pad=8)

# Настраиваем легенду
legend = axes.legend()
legend.set_loc('upper left')
legend.set_title('Сигналы')
legend.shadow = True

# Настраиваем рамку легенды
legend_frame = legend.get_frame()
print(f"{type(legend_frame)=}")
legend_frame.set_facecolor('lightgray')
legend_frame.set_edgecolor('black')

fig.tight_layout()

plt.show()
