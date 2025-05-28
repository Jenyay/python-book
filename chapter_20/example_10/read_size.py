size = 5
with open("example.txt", "r", encoding="utf-8") as file:
    while (chars := file.read(size)) != "":
        print(chars, "|", sep="", end="")
