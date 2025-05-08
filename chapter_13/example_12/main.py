from textpost import TextPost

post = TextPost("Толстой Л.Н.", "  очень длинный текст...  ")
print(f"{post.text=}")

text = TextPost.prepare_text("     ещё более длинный текст...   ")
print(f"{text=}")
