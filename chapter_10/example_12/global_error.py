foo = "Вне func()"

def func():
    print(f"1) {foo=}")
    foo = "Внутри func()"

func()
print(f"2) {foo=}")
