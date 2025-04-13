import cmath

print("Решение уравнений вида a*x^2 + b*x + c = 0")

process = True
while process:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))

    D = b**2 - 4 * a * c
    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)

    print("x1:", x1)
    print("x2:", x2)

    answer = input(
            'Введите "д" или "y" для решения еще одного уравнения')
    process = (answer == "д" or answer == "y")
