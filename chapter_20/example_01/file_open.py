file = open("example.txt", "wt")
print(f"{type(file)=}")
print(dir(file))
file.close()
