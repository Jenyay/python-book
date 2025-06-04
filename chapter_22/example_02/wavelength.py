import sys
from math import sqrt

if __name__ == "__main__":
    print("sys.argv:", sys.argv)

    if len(sys.argv) < 4:
        print("Не указаны обязательные параметры.")
        print("Формат вызова: python wavelength.py freq eps mu")
        sys.exit(1)

    freq = float(sys.argv[1])
    eps = float(sys.argv[2])
    mu = float(sys.argv[3])

    # Скорость света в вакууме в м/с
    c = 299792458

    wavelength = c / (freq * sqrt(eps * mu))
    print(f"Длина волны: {wavelength} м.")
