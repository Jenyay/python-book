from math import sqrt

def equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    return (x1, x2)

result_1 = equation(1.5, -2, 5.0)
result_2 = equation(1.5, -2, -5.0)

print(f"{result_1=}")
print(f"{result_2=}")
