def calculate(a, b, action):
    result = action(a, b)
    action_name = action.__name__
    print(f"{action_name}({a}, {b}) = {result}")
    return result

add = lambda x, y: x + y
mul = lambda x, y: x * y
add_abs = lambda x, y: abs(x + y)
mul_abs = lambda x, y: abs(x * y)

foo = calculate(2, 3, add)
bar = calculate(2, 3, mul)
baz = calculate(2, -5, add_abs)
spam = calculate(2, -5, mul_abs)
