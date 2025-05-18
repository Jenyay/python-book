foo: set[str] = set()
foo.add("Привет")
foo.add("typing")

# Mypy укажет на потенциальную ошибку
foo.add(42)
