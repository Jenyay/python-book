text = "LOREM Ipsum dolor SIT amet Consectetur adipiscing Elit"
words = text.split(" ")
words.sort(key=str.lower)
print(f"{words=}")
