import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from scipy.fft import rfft, irfft, rfftfreq


def rect(time: npt.NDArray, T: float, delay: float) -> npt.NDArray:
    s = np.zeros_like(time)
    s[(time >= delay) & (time < (T + delay))] = 1
    return s

if __name__ == "__main__":
    # Исходные данные
    dt = 20e-12
    signal_len = 8 * 1024
    time = np.arange(signal_len) * dt
    T = 1e-9
    delay = 1e-9
    freq_filter = 4e9

    # Расчет спектра исходного сигнала
    signal = rect(time, T, delay)
    spectrum_src = rfft(signal)
    spectrum_src_mag = np.abs(spectrum_src)
    freq = rfftfreq(signal_len, dt)

    # Фильтрация сигнала
    spectrum_filter = spectrum_src.copy()
    spectrum_filter[freq > freq_filter] = 0
    spectrum_filter_mag = np.abs(spectrum_filter)
    signal_filter = irfft(spectrum_filter)

    # Визуализация результатов
    freq_max_GHz = 7
    fig = plt.figure(figsize=(7, 5))

    # Отображение исходного сигнала и сигнала после фильтрации
    ax_signal = fig.add_subplot(2, 1, 1)
    ax_signal.plot(time / 1e-9, signal, "-b",
                   label="Исходный сигнал")
    ax_signal.plot(time / 1e-9, signal_filter, "-r",
                   label="Cигнал после фильтрации")
    ax_signal.set_title("Сигнал")
    ax_signal.set_xlabel("Время, нс")
    ax_signal.set_ylabel("s(t)")
    ax_signal.set_xlim(0, 10)
    ax_signal.grid()
    ax_signal.legend()

    # Отображение исходного спектра и спектра после фильтрации
    ax_spectrum_mag = fig.add_subplot(2, 1, 2)
    ax_spectrum_mag.plot(freq / 1e9, spectrum_src_mag, "-b",
                         label="Исходный спектр")
    ax_spectrum_mag.plot(freq / 1e9, spectrum_filter_mag, "-r",
                         label="Спектр после фильтрации")
    ax_spectrum_mag.set_title("Амплитудный спектр")
    ax_spectrum_mag.set_xlabel("Частота, ГГц")
    ax_spectrum_mag.set_ylabel("|S(f)|")
    ax_spectrum_mag.set_xlim(0, freq_max_GHz)
    ax_spectrum_mag.grid()
    ax_spectrum_mag.legend()

    fig.tight_layout()
    plt.show()
