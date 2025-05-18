foo: dict[str, float] = {}
foo["pi"] = 3.14159
foo["e"] = 2.72

# Mypy укажет на потенциальную ошибку
foo[6.28] = "tau"
