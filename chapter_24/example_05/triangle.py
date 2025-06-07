import math

class Triangle:
    def __init__(self,
                 p1: tuple[float, float],
                 p2: tuple[float, float],
                 p3: tuple[float, float]):
        self._vertices: list[tuple[float, float]] = [p1, p2, p3]

    def __getitem__(self, index: int) -> tuple[float, float]:
        return self._vertices[index]

    def side_len(self, index1: int, index2: int) -> float:
        p1 = self._vertices[index1]
        p2 = self._vertices[index2]
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
