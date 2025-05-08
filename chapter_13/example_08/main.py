from textpost import TextPost

post1 = TextPost("Толстой Л.Н.", "Очень длинный текст...")
post2 = TextPost("Чехов А.П.", "Текст покороче...")

TextPost.db_name = "other_db_name"

print(f"{TextPost.db_name=}")
print(f"{post1.db_name=}")
print(f"{post2.db_name=}")

post3 = TextPost("Пелевин В.О.", "Текста нет. Ничего нет.")
