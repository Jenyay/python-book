foo: list[str] = []
foo.append("Привет")
foo.append("typing")

# Mypy укажет на потенциальную ошибку
foo.append(42)
