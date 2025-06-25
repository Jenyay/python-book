def add[T: (str, float)](a: T, b: T) -> T:
    return a + b

foo = add(10, 20.5)
bar = add("Привет, ", "typing")
spam = add("Привет, ", 42)
