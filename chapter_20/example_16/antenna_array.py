import pickle

class Point:
    """Класс для представления точки в трехмерном пространстве."""
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Source:
    def __init__(self, point: Point, frequency: float,
                 mag:float, phase_deg:float):
        """"Класс для представления источника
        электромагнитного излучения."""
        self.point = point
        self.frequency = frequency
        self.mag = mag
        self.phase_deg = phase_deg

    def __str__(self):
        return (f"""Координаты: {self.point}
Частота: {self.frequency} Гц
Амплитуда: {self.mag} В
Фаза: {self.phase_deg} град.""")


class AntennaArray:
    def __init__(self, sources: list[Source], comment: str):
        """Класс для представления антенной решетки."""
        self.sources = sources
        self.comment = comment


if __name__ == "__main__":
    sources = [
            Source(Point(0.0, 0.0, 0.0), 1e9, 1.0, 0.0),
            Source(Point(0.15, 0.0, 0.0), 1e9, 1.0, 30.0),
            Source(Point(0.30, 0.0, 0.0), 1e9, 1.0, 60.0),
            ]

    antenna_array = AntennaArray(sources, "Пример антенной решетки")

    # Сериализация объекта AntennaArray в файл с использованием pickle
    file_name = "antenna_array.dat"
    with open(file_name, "wb") as file:
        pickle.dump(antenna_array, file)

    # Десериализация объекта AntennaArray из файла
    with open(file_name, "rb") as file:
        antenna_array_loaded = pickle.load(file)

    # Вывод информации о загруженной антенной решетке
    print(f"{antenna_array_loaded.comment}")
    for source in antenna_array_loaded.sources:
        print(source)
        print()
