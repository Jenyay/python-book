class Triangle:
    def __init__(self,
                 p1: tuple[float, float],
                 p2: tuple[float, float],
                 p3: tuple[float, float]):
        self._vertices: list[tuple[float, float]] = [p1, p2, p3]

    def __getitem__(self, index: int) -> tuple[float, float]:
        return self._vertices[index]
