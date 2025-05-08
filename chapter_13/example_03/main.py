from textpost import TextPost

post = TextPost("Толстой Л.Н.", "Очень длинный текст...")
post.new_field = 24
print(dir(post))
