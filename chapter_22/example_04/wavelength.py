import sys
from argparse import ArgumentParser
from math import sqrt

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--freq")
    parser.add_argument("-e", "--eps")
    parser.add_argument("-m", "--mu")

    namespace = parser.parse_args()
    print(f"{namespace=}")

    freq = (float(namespace.freq)if namespace.freq is not None
            else None)
    eps = (float(namespace.eps) if namespace.eps is not None
           else 1.0)
    mu = (float(namespace.mu) if namespace.mu is not None
          else 1.0)

    if freq is None:
        print("Не указаны обязательные параметры.")
        parser.print_help()
        sys.exit(1)

    # Скорость света в вакууме в м/с
    c = 299792458

    wavelength = c / (freq * sqrt(eps * mu))
    print(f"Длина волны: {wavelength} м.")
