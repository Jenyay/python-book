import cmath
import math

print("Решение уравнений вида a*x^2 + b*x + c = 0")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

D = b**2 - 4 * a * c

if D < 0:
    print("У уравнения нет действительных корней.")
    print('Введите "д" или "y" для нахождения комплексных корней.')
    answer = input(': ')
    if answer == "д" or answer == "y":
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
        print("x1:", x1)
        print("x2:", x2)
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1:", x1)
    print("x2:", x2)
