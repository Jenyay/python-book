from textpost import TextPost
from htmlimagepost import HtmlImagePost

feed = []
feed.append(TextPost("Толстой Л.Н.", "Очень длинный текст..."))
feed.append(HtmlImagePost("Малевич К.С.", "black_square.jpg"))

for post in feed:
    print()
    print(post.format())
