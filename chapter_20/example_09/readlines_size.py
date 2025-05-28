size = 15
with open("example.txt", "r", encoding="utf-8") as file:
    while (lines := file.readlines(size)) != []:
        print("Прочитано строк:", len(lines))
        for line in lines:
            print(line.rstrip())
