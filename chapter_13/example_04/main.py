from textpost import TextPost

post = TextPost("Толстой Л.Н.", "Очень длинный текст...")

print("Автор:", post.get_author())
print("Дата:", post.get_date())

print("Изменяем текст поста")
post.set_text("Еще более длинный текст...")
