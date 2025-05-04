def calculate(a, b, action):
    result = action(a, b)
    action_name = action.__name__
    print(f"{action_name}({a}, {b}) = {result}")
    return result

def add(a, b): return a + b

def mul(a, b): return a * b

def add_abs(a, b): return abs(a + b)

def mul_abs(a, b): return abs(a * b)

baz = calculate(2, -5, add_abs)
print(f"{baz=}")

spam = calculate(2, -5, mul_abs)
print(f"{spam=}")
