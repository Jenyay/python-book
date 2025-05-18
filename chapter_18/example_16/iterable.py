from collections.abc import Iterable

def sum_squares(items: Iterable[float]) -> float:
    result = 0.0
    for item in items:
        result += item * item
    return result

foo = sum_squares([1, 2, 3])
bar = sum_squares((3, 4, 5))
baz = sum_squares({2, 4, 6})

