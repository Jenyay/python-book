from textpost import TextPost
from imagepost import ImagePost
from basepost import BasePost

feed = []

feed.append(TextPost("Толстой Л.Н.", "Очень длинный текст..."))
feed.append(ImagePost("Малевич К.С.", "black_square.jpg"))
feed.append(BasePost("Аноним"))

for post in feed:
    print()
    print(post.format())
