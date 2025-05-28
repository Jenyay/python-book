with (open("hello.txt", "w", encoding="utf-8") as file_1,
      open("привет.txt", "w", encoding="utf-8") as file_2):
    file_1.write("Hello, world!")
    file_2.write("Привет, мир!")
