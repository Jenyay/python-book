def func():
    for n in range(5):
        print(f"{n=}")
        try:
            print("Вошли в блок try.")
            if n == 1:
                print("Прерываем цикл for.")
                break
            print("Выходим из блока try.")
        except ValueError:
            print("Вошли в блок except.")
        else:
            print("Вошли в блок else.")
        finally:
            print("Вошли в блок finally.")

print("Вызов функции func()")
func()
print("Вышли из функции func()")
