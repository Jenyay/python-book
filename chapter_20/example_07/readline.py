with open("example.txt", "r", encoding="utf-8") as file:
    while (line := file.readline()) != "":
        print(line.rstrip())
