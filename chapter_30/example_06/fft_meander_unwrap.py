import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift, fftfreq

def meander(time: npt.NDArray, duty: float, period: float) -> npt.NDArray:
    """Функция генерации последовательности прямоугольных импульсов."""
    s = np.zeros_like(time)
    triangle = (
        np.arcsin(np.sin(2.0 * np.pi / period * time + np.pi / 2)) /
        np.pi + 0.5)
    s[triangle < duty] = 1
    return s

if __name__ == "__main__":
    dt = 20e-12
    signal_len = 8 * 1024
    time = np.arange(signal_len) * dt
    duty = 0.25
    period = 4e-9
    signal = meander(time, duty, period)
    spectrum = fftshift(fft(signal))
    spectrum_mag = np.abs(spectrum)
    spectrum_phase = np.unwrap(np.angle(spectrum))
    freq = fftshift(fftfreq(signal_len, dt))

    freq_min_GHz = -7
    freq_max_GHz = 7

    fig = plt.figure(figsize=(10, 8))

    ax_signal = fig.add_subplot(3, 1, 1)
    ax_signal.plot(time / 1e-9, signal)
    ax_signal.set_title("Сигнал")
    ax_signal.set_xlabel("Время, нс")
    ax_signal.set_ylabel("s(t)")
    ax_signal.set_xlim(0, 20)
    ax_signal.grid()

    ax_spectrum_mag = fig.add_subplot(3, 1, 2)
    ax_spectrum_mag.plot(freq / 1e9, spectrum_mag)
    ax_spectrum_mag.set_title("Амплитудный спектр")
    ax_spectrum_mag.set_xlabel("Частота, ГГц")
    ax_spectrum_mag.set_ylabel("|S(f)|")
    ax_spectrum_mag.set_xlim(freq_min_GHz, freq_max_GHz)
    ax_spectrum_mag.grid()

    ax_spectrum_phase = fig.add_subplot(3, 1, 3)
    ax_spectrum_phase.plot(freq / 1e9, spectrum_phase)
    ax_spectrum_phase.set_title("Фазовый спектр")
    ax_spectrum_phase.set_xlabel("Частота, ГГц")
    ax_spectrum_phase.set_ylabel("arg(S(f))")
    ax_spectrum_phase.set_xlim(freq_min_GHz, freq_max_GHz)
    ax_spectrum_phase.set_ylim(150, 275)
    ax_spectrum_phase.grid()

    fig.tight_layout()
    plt.show()
