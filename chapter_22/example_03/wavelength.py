import sys
from math import sqrt

if __name__ == "__main__":
    print("sys.argv:", sys.argv)

    freq = None
    eps = 1.0
    mu = 1.0

    n = 1
    while n < len(sys.argv) - 1:
        current = sys.argv[n]
        if current == "-f" or current == "--freq":
            freq = float(sys.argv[n + 1])
            n += 2
            continue

        if current == "-e" or current == "--eps":
            eps = float(sys.argv[n + 1])
            n += 2
            continue

        if current == "-m" or current == "--mu":
            mu = float(sys.argv[n + 1])
            n += 2
            continue
        n += 1

    if freq is None:
        print("Не указаны обязательные параметры.")
        print("Формат вызова:")
        print("python wavelength.py --freq freq [--eps eps] [--mu mu]")
        sys.exit(1)

    # Скорость света в вакууме в м/с
    c = 299792458

    wavelength = c / (freq * sqrt(eps * mu))
    print(f"Длина волны: {wavelength} м.")
