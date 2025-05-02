def func():
    global foo
    foo = "Внутри func()"
    print(f"1) {foo=}")

func()
print(f"2) {foo=}")
