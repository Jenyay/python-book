with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
