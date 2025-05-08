from textpost import TextPost

post = TextPost("Толстой Л.Н.", "Очень длинный текст...")

print("Автор:", post.author)
print("Дата:", post.date)

print("Изменяем текст поста")
post.text = "Еще более длинный текст..."
