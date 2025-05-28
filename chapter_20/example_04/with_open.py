with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, ")
    file.write("world!\n")
    lines = ["Привет, мир!\n", "你好世界!\n"]
    file.writelines(lines)
