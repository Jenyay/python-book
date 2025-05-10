from basepost import BasePost
from mixins import TextMixin, ImageMixin

class TextImagePost(BasePost, TextMixin, ImageMixin):
    """Класс текстового поста для блога"""

    def __init__(self, author, text, image):
        print("TextImagePost.__init__()")
        BasePost.__init__(self, author)
        TextMixin.__init__(self, text)
        ImageMixin.__init__(self, image)
        self._save()

    def _save(self):
        print("Пост с текстом и картинкой сохранен.")

    def format(self):
        return f"""    Автор: {self._author}
    Дата: {self._date:%d.%m.%Y %H:%M:%S}
    Картинка: {self._image}
    ----
    {self._text}"""
