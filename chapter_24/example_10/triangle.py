import math

class Triangle:
    """
    Класс, описывающий треугольник с помощью координат
    трех вершин на плоскости.

    >>> triangle = Triangle((0, 0), (0, 1), (2, 0))
    >>> triangle[0]
    (0, 0)
    >>> triangle[1]
    (0, 1)
    >>> triangle[2]
    (2, 0)
    """
    def __init__(self,
                 p1: tuple[float, float],
                 p2: tuple[float, float],
                 p3: tuple[float, float]):
        self._vertices: list[tuple[float, float]] = [p1, p2, p3]

    def __getitem__(self, index: int) -> tuple[float, float]:
        return self._vertices[index]

    def side_len(self, index1: int, index2: int) -> float:
        if index1 < 0 or index1 > 2 or index2 < 0 or index2 > 2:
            raise ValueError("Неправильные индексы вершин")

        p1 = self._vertices[index1]
        p2 = self._vertices[index2]
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
