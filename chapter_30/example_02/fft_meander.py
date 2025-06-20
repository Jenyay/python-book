import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from scipy.fft import fft

def meander(time: npt.NDArray, duty: float, period: float) -> npt.NDArray:
    """Функция генерации последовательности прямоугольных импульсов."""
    s = np.zeros_like(time)
    newtime = (
        np.arcsin(np.sin(2.0 * np.pi / period * time + np.pi / 2)) /
        np.pi + 0.5)
    s[newtime < duty] = 1
    return s

if __name__ == "__main__":
    # Шаг дискретизации сигнала по времени в секундах
    dt = 20e-12

    # Длина сигнала в отсчетах
    signal_len = 8 * 1024

    # Временыне отсчеты в секундах
    time = np.arange(signal_len) * dt

    # Коэффициент заполнения
    duty = 0.25

    # Период сигнала в секундах
    period = 4e-9

    # Исследуемый сигнал
    signal = meander(time, duty, period)

    # Спектр сигнала (массив комплексных чисел)
    spectrum = fft(signal)

    # Амплитудный спектр
    spectrum_mag = np.abs(spectrum)

    # Фазовый спектр
    spectrum_phase = np.angle(spectrum)

    # Вывод графиков
    fig = plt.figure(figsize=(10, 8))

    # Вывод сигнала
    ax_signal = fig.add_subplot(3, 1, 1)
    ax_signal.plot(time / 1e-9, signal)
    ax_signal.set_title("Сигнал")
    ax_signal.set_xlabel("Время, нс")
    ax_signal.set_ylabel("s(t)")
    ax_signal.set_xlim(0, 20)
    ax_signal.grid()

    # Вывод амплитудного спектра
    ax_spectrum_mag = fig.add_subplot(3, 1, 2)
    ax_spectrum_mag.plot(spectrum_mag)
    ax_spectrum_mag.set_title("Амплитудный спектр")
    ax_spectrum_mag.set_xlabel("Частота, отсчеты")
    ax_spectrum_mag.set_ylabel("|S(f)|")
    ax_spectrum_mag.grid()

    # Вывод фазового спектра
    ax_spectrum_phase = fig.add_subplot(3, 1, 3)
    ax_spectrum_phase.plot(spectrum_phase)
    ax_spectrum_phase.set_title("Фазовый спектр")
    ax_spectrum_phase.set_xlabel("Частота, отсчеты")
    ax_spectrum_phase.set_ylabel("arg(S(f))")
    ax_spectrum_phase.grid()

    fig.tight_layout()
    plt.show()
