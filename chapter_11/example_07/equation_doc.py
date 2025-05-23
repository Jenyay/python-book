from math import sqrt

def equation(a, b, c):
    """Функция для решения квадратного уравнения.

    Функция возвращает кортеж из двух корней уравнения, 
    если дискриминант неотрицательный, в противном случае 
    возвращает значение None.
    a, b, c -- коэффициенты квадратного уравнения.
    """
    D = b ** 2 - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        return (x1, x2)

print(f"{equation.__doc__}")
