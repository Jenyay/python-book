correct_password = "secret"  # Правильный пароль
max_attempts = 3             # Максимальное количество попыток
attempts = 0

while attempts < max_attempts:
    password = input("Введите пароль: ")
    if password == correct_password:
        print("Доступ разрешен!")
        break
    print("Неправильный пароль, попробуйте снова.")
    attempts += 1
else:
    print("Попытки исчерпаны. Доступ запрещен.")
