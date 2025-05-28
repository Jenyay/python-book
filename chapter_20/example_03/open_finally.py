file = open("example.txt", "w", encoding="utf-8")
try:
    file.write("Hello, world!\n")
    raise OSError("Что-то пошло не так")
    lines = ["Привет, мир!\n", "你好世界!\n"]
    file.writelines(lines)
finally:
    print("Закрываем файл.")
    file.close()
