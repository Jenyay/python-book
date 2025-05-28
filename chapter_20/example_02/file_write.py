file = open("example.txt", "wt", encoding="utf-8")

file.write("Hello, ")
file.write("world!\n")

lines = ["Привет, мир!\n", "你好世界!\n"]
file.writelines(lines)

file.close()
