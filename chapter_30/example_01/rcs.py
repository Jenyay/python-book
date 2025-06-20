import numpy as np
from scipy.special import spherical_jn, spherical_yn
from scipy.constants import pi, c
from matplotlib import pyplot as plt

def spherical_hn2(n, x):
    """Функция Ханкеля второго рода"""
    return spherical_jn(n, x) - 1j * spherical_yn(n, x)

def an(n, x):
    return spherical_jn(n, x) / spherical_hn2(n, x)

def bn(n, kr):
    return ((kr * spherical_jn(n - 1, kr) -
             n * spherical_jn(n, kr)) / 
            (kr * spherical_hn2(n - 1, kr) -
             n * spherical_hn2(n, kr)))

def sphere_rcs(r, lmbd, nmax):
    """Расчет эффективной площади рассеяния
    идеально проводящего шара"""
    k = 2 * pi / lmbd
    kr = k * r
    result = 0.0
    for n in range(1, nmax + 1):
        result += (((-1) ** n) * (n + 0.5)
                   * (bn(n, kr) - an(n, kr)))

    return (lmbd**2 / pi) * np.abs(result) ** 2

if __name__ == "__main__":
    # Диапазон частот
    freq = np.linspace(0.01e9, 4e9, 300)

    # Радиус шара
    r = 0.15

    # Количество слагаемых в ряде
    nmax = 20

    # Длина волны
    lmbd = c / freq
    rcs = sphere_rcs(r, lmbd, nmax)

    # Построение ненормированного графика ЭПР от частоты
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(freq / 1e9, rcs)
    ax1.set_xlabel(r"Частота, ГГц")
    ax1.set_ylabel(r"$\sigma, \text{м}^2$")
    ax1.grid()

    # Построение нормированного графика
    x_values = 2 * pi * r / lmbd
    y_values = rcs / (pi * r ** 2)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(x_values, y_values)
    ax2.set_xlabel(r"$2\pi r/\lambda$")
    ax2.set_ylabel(r"$\sigma/(\pi r^2)$")
    ax2.set_xticks(np.arange(0, 14, 1.0))
    ax2.grid()

    fig.tight_layout()
    plt.show()
