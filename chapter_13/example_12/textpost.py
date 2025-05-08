from datetime import datetime, timezone

class TextPost:
    """Класс текстового поста для блога"""

    def __init__(self, author, text):
        self._author = author
        self._text = TextPost.prepare_text(text)
        self._date = datetime.now(timezone.utc)
        self._save()

    @staticmethod
    def prepare_text(text):
        result = text.strip()
        return result.capitalize()

    @property
    def text(self): return self._text

    @text.setter
    def text(self, value):
        self._text = TextPost.prepare_text(value)
        self._save()

    def _save(self):
        print(f"Пост сохранен в базу данных.")

    @property
    def author(self): return self._author

    @property
    def date(self): return self._date
