from textpost import TextPost

post1 = TextPost("Толстой Л.Н.", "Очень длинный текст...")
post2 = TextPost("Чехов А.П.", "Текст покороче...")

# Доступ к полю класса через имя класса
print(f"{TextPost.db_name=}")

# Доступ к полю класса через экземпляры класса
print(f"{post1.db_name=}")
print(f"{post2.db_name=}")
