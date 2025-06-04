from argparse import ArgumentParser
from math import sqrt

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("freq", type=float)
    parser.add_argument("-e", "--eps", type=float, default=1.0)
    parser.add_argument("-m", "--mu", type=float, default=1.0)

    namespace = parser.parse_args()
    print(f"{namespace=}")

    freq = namespace.freq
    eps = namespace.eps
    mu = namespace.mu

    # Скорость света в вакууме в м/с
    c = 299792458

    wavelength = c / (freq * sqrt(eps * mu))
    print(f"Длина волны: {wavelength} м.")
