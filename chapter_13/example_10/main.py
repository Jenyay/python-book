from textpost import TextPost

post1 = TextPost("Толстой Л.Н.", "Очень длинный текст...")
post2 = TextPost("Чехов А.П.", "Текст покороче...")

print(f"{post1.get_db_name()=}")
