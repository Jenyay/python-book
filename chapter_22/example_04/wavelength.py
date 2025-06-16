import sys
from argparse import ArgumentParser
from math import sqrt

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--freq")
    parser.add_argument("-e", "--eps")
    parser.add_argument("-m", "--mu")

    args = parser.parse_args()
    print(f"{args=}")

    freq = (float(args.freq)if args.freq is not None
            else None)
    eps = (float(args.eps) if args.eps is not None
           else 1.0)
    mu = (float(args.mu) if args.mu is not None
          else 1.0)

    if freq is None:
        print("Не указаны обязательные параметры.")
        parser.print_help()
        sys.exit(1)

    # Скорость света в вакууме в м/с
    c = 299792458

    wavelength = c / (freq * sqrt(eps * mu))
    print(f"Длина волны: {wavelength} м.")
