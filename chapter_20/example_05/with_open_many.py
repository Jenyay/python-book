with (open("hello_en.txt", "w", encoding="utf-8") as file_1,
      open("hello_ru.txt", "w", encoding="utf-8") as file_2):
    file_1.write("Hello, world!")
    file_2.write("Привет, мир!")
