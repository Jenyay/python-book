def add(a: float | str, b: float | str) -> float | str:
    return a + b

foo = add(10, 20.5)
bar = add("Привет, ", "typing")
spam = add("Привет, ", 42)
