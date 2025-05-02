foo = "Вне func()"

def func():
    global foo
    print(f"1) {foo=}")
    foo = "Внутри func()"

func()
print(f"2) {foo=}")
