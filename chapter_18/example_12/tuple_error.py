foo: tuple[int, int] = (1, 2)
foo = (3, 4)

# Mypy укажет на ошибку
foo = (5, 6, 7)
