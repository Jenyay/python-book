from textpost import TextPost

post = TextPost("Толстой Л.Н.", "Очень длинный текст...")
print(dir(post))

post.set_id(42)
print(dir(post))
