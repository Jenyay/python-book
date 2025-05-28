if __name__ == "__main__":
    try:
        print("До броска исключения.")
        raise ValueError("Сообщение для исключения.")
        print("Эта строка никогда не будет выполняться.")
    except ValueError:
        print("Возникло исключение ValueError.")

    print("После обработки исключения.")
