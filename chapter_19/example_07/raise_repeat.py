def wavelength(frequency, speed=3e8):
    try:
        if not isinstance(frequency, (int, float)):
            raise TypeError("Частота должна быть числом")
        if frequency <= 0:
            raise ValueError("Частота должна быть положительной")
    except (TypeError, ValueError) as err:
        print("Ошибка при вызове функции wavelength().", err)
        raise
    return speed / frequency


if __name__ == "__main__":
    frequency = "10 ГГц"
    # frequency = -10e9

    try:
        wl = wavelength(frequency)
        print(f"Длина волны: {wl} м")
    except (TypeError, ValueError) as err:
        print("Что-то пошло не так.", err)

    print("После обработки исключения.")


