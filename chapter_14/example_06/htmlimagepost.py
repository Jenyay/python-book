from imagepost import ImagePost

class HtmlImagePost(ImagePost):
    def format(self):
        return f"""    Автор: <b>{self._author}</b><br/>
    Дата: <i>{self._date:%d.%m.%Y %H:%M:%S}</i><br/>
    Картинка: <img src="{self._image}"/>"""
