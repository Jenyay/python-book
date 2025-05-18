from typing import Any

foo: dict[str, Any] = {}
foo['bar'] = 1
foo['baz'] = 'hello'
foo['bam'] = [1, 2, 3]

# Mypy укажет на потенциальную ошибку
foo[100] = "error"
