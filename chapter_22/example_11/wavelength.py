import sys
from argparse import ArgumentParser
from math import sqrt

if __name__ == "__main__":
    parser = ArgumentParser(prog="python wavelength.py",
                        description="Скрипт для расчета длины волны в среде",
                        epilog="(c) Василий Пупкин, 2025",
                        add_help=False)
    group1 = parser.add_argument_group("Позиционные параметры",
                        "Это обязательные параметры")
    group2 = parser.add_argument_group("Именованные параметры",
                        "Это необязательные параметры")

    group1.add_argument("freq", type=float,
                        help="Частота, Гц")
    group2.add_argument("-e", "--eps", type=float, default=1.0,
                        help="Относительная диэлектрическая проницаемость")
    group2.add_argument("-m", "--mu", type=float, default=1.0,
                        help="Относительная магнитная проницаемость")
    group2.add_argument("-v", action="store_true", default=False,
                        help="Подробный вывод")
    group2.add_argument("-h", "--help", action="help",
                        help="Вывод справки и завершение работы")

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
