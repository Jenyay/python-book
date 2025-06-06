from math import sqrt
from typing import Optional

def equation(a: float, b: float, c: float) -> Optional[tuple[float, float]]:
    result = None
    D = b ** 2 - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        result = (x1, x2)

    return result

result_1 = equation(1, 2, 3)
print(f"{result_1}")

result_2 = equation(1.1, 2.5, -3.0)
print(f"{result_2}")
