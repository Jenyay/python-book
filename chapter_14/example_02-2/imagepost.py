from basepost import BasePost

class ImagePost(BasePost):
    """Класс поста с картинкой для блога"""

    def __init__(self, author, image):
        print("ImagePost.__init__()")
        BasePost.__init__(self, author)
        self._image = image
        self._save()

    def _save(self):
        print("Пост с картинкой сохранен.")

    @property
    def image(self): return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self._save()

    def format(self):
        return f"""    Автор: {self._author}
    Дата: {self._date:%d.%m.%Y %H:%M:%S}
    Картинка: {self._image}"""
