import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 8.0e-9, 200)
y1 = np.sin(2e9 * x) * np.cos(5e9 * x)
y2 = np.sin(0.5e9 * x) * np.cos(1e9 * x)

# Создаем окно с графиком
fig = plt.figure(figsize=(9, 7))
print(f"{type(fig)=}")

# Создаем оси для графика
axes = fig.add_subplot(1, 1, 1)
print(f"{type(axes)=}")

# Рисуем графики
curves = axes.plot(x, y1, "-k", x, y2, "--r")
print(f"{type(curves[0])=}")

# Настраиваем внешний вид графика
axes.grid()
axes.set_xlim(left=0.0)
axes.set_ylim(-1.0, 1.0)

# Метки около осей
xlabel = axes.set_xlabel("Время, с", loc="right",
                labelpad=15, color="blue")
ylabel = axes.set_ylabel("U, В", loc="top", rotation=0,
                labelpad=-6, color="blue")

print(f"{type(xlabel)=}")
print(f"{type(ylabel)=}")

# Настраиваем заголовок графика
title = axes.set_title("y = sin(2e9 * x) * cos(5e9 * x)", pad=8)
print(f"{type(title)=}")

# Настраиваем легенду
legend = axes.legend(["sin(2e9 * x) * cos(5e9 * x)",
                         "sin(0.5e9 * x) * cos(1e9 * x)"],
                     loc="upper left", shadow=True,
                     facecolor="lightgray", edgecolor="black",
                     title="Сигналы")
print(f"{type(legend)=}")

fig.tight_layout()
plt.show()
