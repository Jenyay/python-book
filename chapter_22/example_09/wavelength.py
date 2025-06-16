from argparse import ArgumentParser
from math import sqrt

if __name__ == "__main__":
    parser = ArgumentParser(prog="python wavelength.py",
                        description="Скрипт для расчета длины волны в среде",
                        epilog="(c) Василий Пупкин, 2025")
    parser.add_argument("freq", type=float,
                        help="Частота, Гц")
    parser.add_argument("-e", "--eps", type=float, default=1.0,
                        help="Относительная диэлектрическая проницаемость")
    parser.add_argument("-m", "--mu", type=float, default=1.0,
                        help="Относительная магнитная проницаемость")
    parser.add_argument("-v", action="store_true",
                        help="Подробный вывод")

    args = parser.parse_args()
    print(f"{args=}")

    freq = args.freq
    eps = args.eps
    mu = args.mu
    verbose = args.v

    # Скорость света в вакууме в м/с
    c = 299792458

    if verbose:
        print(f"Частота: {freq} Гц")
        print(f"Eps: {eps}")
        print(f"Mu: {mu}")

    wavelength = c / (freq * sqrt(eps * mu))
    print(f"Длина волны: {wavelength} м.")
