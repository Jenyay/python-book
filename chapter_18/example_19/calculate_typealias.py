from collections.abc import Callable

Action = Callable[[float, float], float]

def calculate(a: float, b: float, action: Action) -> float:
    result = action(a, b)
    action_name = action.__name__
    print(f"{action_name}({a}, {b}) = {result}")
    return result

def add(a: float, b: float) -> float: return a + b

def mul(a: float, b: float) -> float: return a * b

foo = calculate(2, 3, add)
bar = calculate(2, 3, mul)
