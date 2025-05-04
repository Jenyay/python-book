def calculate(a, b, action):
    result = action(a, b)
    action_name = action.__name__
    print(f"{action_name}({a}, {b}) = {result}")
    return result

foo = calculate(2, 3, lambda x, y: x + y)
bar = calculate(2, 3, lambda x, y: x * y)
baz = calculate(2, -5, lambda x, y: abs(x + y))
spam = calculate(2, -5, lambda x, y: abs(x * y))
